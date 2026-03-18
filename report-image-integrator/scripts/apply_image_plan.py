from __future__ import annotations

import argparse
import json
import re
import shutil
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Apply a figure insertion plan to a Markdown report."
    )
    parser.add_argument("--markdown", required=True, help="Path to the target Markdown file.")
    parser.add_argument("--plan", required=True, help="Path to the JSON insertion plan.")
    return parser.parse_args()


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def slug_stem(label: str) -> str:
    stem = label.strip().lower()
    if stem.startswith("fig:"):
        stem = stem[4:]
    stem = re.sub(r"[^a-z0-9]+", "-", stem).strip("-")
    return stem or "figure"


def build_figure_block(entry: dict, figure_dir_name: str) -> str:
    caption = entry["caption"].strip()
    label = entry["label"].strip()
    target_filename = entry["target_filename"].strip()
    pre_text = entry.get("pre_text", "").strip()
    post_text = entry.get("post_text", "").strip()

    parts: list[str] = []
    if pre_text:
        parts.append(pre_text)
    parts.append(f"![{caption}]({figure_dir_name}/{target_filename}){{#{label}}}")
    if post_text:
        parts.append(post_text)
    return "\n\n".join(parts)


def replace_once(markdown: str, anchor: str, replacement: str, mode: str) -> str:
    count = markdown.count(anchor)
    if count != 1:
        raise ValueError(f"Anchor for {mode} must appear exactly once; found {count}: {anchor!r}")

    if mode == "insert_after_text":
        return markdown.replace(anchor, f"{anchor}\n\n{replacement}", 1)
    if mode == "insert_before_text":
        return markdown.replace(anchor, f"{replacement}\n\n{anchor}", 1)
    if mode == "replace_text":
        return markdown.replace(anchor, replacement, 1)
    raise ValueError(f"Unsupported anchor mode: {mode}")


def validate_entry(entry: dict) -> tuple[str, str]:
    anchor_modes = ["insert_after_text", "insert_before_text", "replace_text"]
    present = [mode for mode in anchor_modes if entry.get(mode)]
    if len(present) != 1:
        raise ValueError(
            "Each entry must define exactly one anchor field: "
            "insert_after_text, insert_before_text, or replace_text."
        )

    for field in ["source_image", "target_filename", "caption", "label"]:
        if not entry.get(field):
            raise ValueError(f"Missing required field: {field}")

    if not re.fullmatch(r"fig:[a-z0-9]+(?:-[a-z0-9]+)*", entry["label"].strip()):
        raise ValueError(f"Invalid figure label: {entry['label']!r}")

    target_path = Path(entry["target_filename"])
    if target_path.name != entry["target_filename"] or target_path.name in {".", ".."}:
        raise ValueError(f"target_filename must be a plain filename: {entry['target_filename']!r}")

    return present[0], str(entry[present[0]])


def main() -> int:
    args = parse_args()
    markdown_path = Path(args.markdown).resolve()
    plan_path = Path(args.plan).resolve()

    markdown = markdown_path.read_text(encoding="utf-8")
    plan = load_json(plan_path)

    entries = plan.get("entries")
    if not isinstance(entries, list) or not entries:
        raise ValueError("Plan must contain a non-empty 'entries' array.")

    figure_dir_name = plan.get("figure_dir_name") or f"{markdown_path.stem}-figures"
    figure_dir = markdown_path.parent / figure_dir_name
    figure_dir.mkdir(parents=True, exist_ok=True)

    seen_labels: set[str] = set()
    seen_targets: set[str] = set()

    for entry in entries:
        mode, anchor = validate_entry(entry)

        label = entry["label"].strip()
        target_filename = entry["target_filename"].strip()

        if label in seen_labels:
            raise ValueError(f"Duplicate figure label: {label}")
        if target_filename in seen_targets:
            raise ValueError(f"Duplicate target filename: {target_filename}")

        seen_labels.add(label)
        seen_targets.add(target_filename)

        source_image = Path(entry["source_image"]).resolve()
        if not source_image.exists():
            raise FileNotFoundError(f"Source image not found: {source_image}")

        target_image = figure_dir / target_filename
        shutil.move(str(source_image), str(target_image))

        figure_block = build_figure_block(entry, figure_dir_name)
        markdown = replace_once(markdown, anchor, figure_block, mode)

    markdown_path.write_text(markdown, encoding="utf-8", newline="\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

