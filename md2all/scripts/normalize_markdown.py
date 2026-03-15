#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from common import read_text, write_text


def normalize_text(text: str) -> str:
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    if not normalized.endswith("\n"):
        normalized += "\n"
    return normalized


def convert_md_to_qmd(text: str) -> str:
    return normalize_text(text)


def main() -> int:
    parser = argparse.ArgumentParser(description="Normalize Markdown and emit QMD-compatible text.")
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    converted = convert_md_to_qmd(read_text(args.input))
    write_text(args.output, converted)
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
