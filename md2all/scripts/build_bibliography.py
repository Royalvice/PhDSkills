#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path

from common import read_text, write_text

REFERENCE_HEADINGS = ("参考文献", "references", "bibliography")


def slugify(value: str) -> str:
    token = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return token or "source"


def parse_reference_lines(text: str) -> list[str]:
    lines = text.splitlines()
    collected: list[str] = []
    capture = False
    for line in lines:
        stripped = line.strip()
        heading_candidate = stripped.lstrip("#").strip().lower().rstrip(":")
        if any(heading_candidate == heading for heading in REFERENCE_HEADINGS):
            capture = True
            continue
        if capture and stripped.startswith("#"):
            break
        if capture and stripped:
            collected.append(stripped.lstrip("-* ").strip())
    return collected


def infer_entry(reference: str, index: int) -> tuple[str, str]:
    parts = [part.strip() for part in reference.split(".") if part.strip()]
    author = parts[0] if parts else f"ref-{index}"
    year_match = re.search(r"(19|20)\d{2}", reference)
    year = year_match.group(0) if year_match else "0000"
    title = parts[1] if len(parts) > 1 else reference
    key = f"{slugify(author)}-{year}-{slugify(title)[:24]}".strip("-")
    if key == f"{slugify(author)}-0000":
        key = f"ref-missing-{index}"
    entry = "\n".join([
        f"@misc{{{key},",
        f"  author = {{{author}}},",
        f"  title = {{{title}}},",
        f"  year = {{{year}}},",
        f"  note = {{{reference}}}",
        "}"
    ])
    return key, entry


def build_bib(text: str) -> tuple[list[str], str]:
    refs = parse_reference_lines(text)
    keys: list[str] = []
    entries: list[str] = []
    for index, reference in enumerate(refs, start=1):
        key, entry = infer_entry(reference, index)
        keys.append(key)
        entries.append(entry)
    return keys, "\n\n".join(entries) + ("\n" if entries else "")


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a minimal bibliography from Markdown reference strings.")
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    _, bib = build_bib(read_text(args.input))
    write_text(args.output, bib)
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
