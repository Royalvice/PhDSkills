#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from common import ASSETS_DIR, load_json


def load_profile(template_id: str) -> dict:
    catalog = load_json(ASSETS_DIR / "reference-docx" / "template-catalog.json")
    for item in catalog["templates"]:
        if item["id"] == template_id:
            return load_json(ASSETS_DIR / "reference-docx" / item["profile"])
    raise KeyError(f"Unknown template: {template_id}")


def patch_profile(profile: dict, overrides: dict[str, str]) -> dict:
    patched = json.loads(json.dumps(profile))
    if overrides.get("font"):
        patched["body"]["font_zh"] = overrides["font"]
        patched["body"]["font_en"] = overrides["font"]
    if overrides.get("font_size"):
        patched["body"]["size_pt"] = float(overrides["font_size"])
    if overrides.get("margin_cm"):
        patched["page"]["margin_cm"] = float(overrides["margin_cm"])
    return patched


def generate_docx(profile: dict, output: Path) -> None:
    try:
        from docx import Document
        from docx.shared import Cm, Pt
    except ImportError as exc:
        raise RuntimeError("python-docx is required to generate reference.docx templates") from exc
    document = Document()
    section = document.sections[0]
    margin_cm = float(profile["page"]["margin_cm"])
    section.top_margin = Cm(margin_cm)
    section.bottom_margin = Cm(margin_cm)
    section.left_margin = Cm(margin_cm)
    section.right_margin = Cm(margin_cm)
    normal = document.styles["Normal"]
    normal.font.name = profile["body"]["font_en"]
    normal.font.size = Pt(float(profile["body"]["size_pt"]))
    normal.paragraph_format.line_spacing = float(profile["body"]["line_spacing"])
    normal.paragraph_format.space_after = Pt(float(profile["body"]["space_after_pt"]))
    for style_name, heading_name in (("heading1", "Heading 1"), ("heading2", "Heading 2"), ("heading3", "Heading 3")):
        style = document.styles[heading_name]
        config = profile["headings"][style_name]
        style.font.name = config["font_en"]
        style.font.size = Pt(float(config["size_pt"]))
        style.font.bold = bool(config["bold"])
        style.paragraph_format.space_before = Pt(float(config["space_before_pt"]))
        style.paragraph_format.space_after = Pt(float(config["space_after_pt"]))
    document.save(output)


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate or patch a reference.docx file from a built-in template profile.")
    parser.add_argument("--template", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--font")
    parser.add_argument("--font-size")
    parser.add_argument("--margin-cm")
    parser.add_argument("--dump-json", action="store_true")
    args = parser.parse_args()
    profile = load_profile(args.template)
    patched = patch_profile(profile, {"font": args.font or "", "font_size": args.font_size or "", "margin_cm": args.margin_cm or ""})
    if args.dump_json:
        print(json.dumps(patched, ensure_ascii=False, indent=2))
        return 0
    args.output.parent.mkdir(parents=True, exist_ok=True)
    generate_docx(patched, args.output)
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
