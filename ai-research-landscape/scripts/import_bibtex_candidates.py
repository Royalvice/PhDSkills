#!/usr/bin/env python3
"""
Convert BibTeX entries into candidate JSON skeletons for later verification.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ENTRY_PATTERN = re.compile(r"@(?P<kind>\w+)\s*\{\s*(?P<key>[^,]+),(?P<body>.*?)\n\}\s*", re.DOTALL)
FIELD_PATTERN = re.compile(r"(?P<name>\w+)\s*=\s*(?P<value>\{.*?\}|\".*?\"),?", re.DOTALL)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Import BibTeX into candidate JSON skeletons.")
    parser.add_argument("input_bib", help="BibTeX file, including Google Scholar exports.")
    parser.add_argument("-o", "--output", help="Output JSON file")
    parser.add_argument("--discovery-channel", default="scholar", help="Discovery channel label to apply to imported entries.")
    parser.add_argument("--mark-survey", action="store_true", help="Mark all imported entries as surveys.")
    return parser.parse_args()


def strip_braces(value: str) -> str:
    value = value.strip().rstrip(",")
    if (value.startswith("{") and value.endswith("}")) or (value.startswith('"') and value.endswith('"')):
        return value[1:-1].strip()
    return value


def parse_entries(content: str) -> list[dict[str, str]]:
    entries = []
    for match in ENTRY_PATTERN.finditer(content):
        fields = {}
        body = match.group("body")
        for field_match in FIELD_PATTERN.finditer(body):
            fields[field_match.group("name").lower()] = strip_braces(field_match.group("value"))
        entries.append(fields)
    return entries


def parse_authors(author_field: str | None) -> list[str]:
    if not author_field:
        return []
    return [part.strip() for part in author_field.split(" and ") if part.strip()]


def entry_to_candidate(fields: dict[str, str], discovery_channel: str, mark_survey: bool) -> dict:
    url = fields.get("url") or fields.get("doi")
    year = fields.get("year")
    return {
        "title": fields.get("title"),
        "authors": parse_authors(fields.get("author")),
        "organization": fields.get("organization"),
        "year": int(year) if year and year.isdigit() else year,
        "venue": fields.get("booktitle") or fields.get("journal"),
        "citations": None,
        "source_type": "survey" if mark_survey else "paper",
        "canonical_url": url,
        "scholar_url": None,
        "discovery_channels": [discovery_channel],
        "is_survey": mark_survey,
        "is_foundational": False,
        "is_blog": False,
        "is_arxiv": bool(url and "arxiv.org" in url.lower()),
        "verified": False,
        "summary": None,
        "notes": "Imported from BibTeX. Verify metadata against a live source.",
    }


def main() -> int:
    args = parse_args()
    input_path = Path(args.input_bib)
    output_path = Path(args.output) if args.output else input_path.with_suffix(".candidates.json")
    entries = parse_entries(input_path.read_text(encoding="utf-8"))
    candidates = [entry_to_candidate(fields, args.discovery_channel, args.mark_survey) for fields in entries if fields.get("title")]
    output_path.write_text(json.dumps(candidates, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(candidates)} candidate skeletons to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
