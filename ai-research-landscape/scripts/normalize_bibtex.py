#!/usr/bin/env python3
"""
Normalize and deduplicate BibTeX entries with stable keys.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


ENTRY_PATTERN = re.compile(r"@(?P<kind>\w+)\s*\{\s*(?P<key>[^,]+),(?P<body>.*?)\n\}\s*", re.DOTALL)
FIELD_PATTERN = re.compile(r"(?P<name>\w+)\s*=\s*(?P<value>\{.*?\}|\".*?\"),?", re.DOTALL)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Normalize BibTeX keys and remove obvious duplicates.")
    parser.add_argument("input_bib", help="Input .bib file")
    parser.add_argument("-o", "--output", help="Output .bib file")
    return parser.parse_args()


def strip_braces(value: str) -> str:
    value = value.strip().rstrip(",")
    if (value.startswith("{") and value.endswith("}")) or (value.startswith('"') and value.endswith('"')):
        return value[1:-1].strip()
    return value


def slug(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def first_author_family(author_field: str) -> str:
    if not author_field:
        return "anon"
    first = author_field.split(" and ")[0].strip()
    if "," in first:
        return slug(first.split(",", 1)[0])
    parts = first.split()
    return slug(parts[-1]) if parts else "anon"


def build_key(fields: dict[str, str]) -> str:
    author = first_author_family(fields.get("author", ""))
    year = re.sub(r"[^0-9]", "", fields.get("year", "")) or "nd"
    title = fields.get("title", "")
    title_words = [slug(word) for word in re.findall(r"[A-Za-z0-9]+", title)[:3]]
    title_part = "".join(word for word in title_words if word) or "untitled"
    return f"{author}{year}{title_part}"


def parse_entries(content: str) -> list[tuple[str, str, dict[str, str]]]:
    parsed = []
    for match in ENTRY_PATTERN.finditer(content):
        kind = match.group("kind").lower()
        key = match.group("key").strip()
        body = match.group("body")
        fields = {}
        for field_match in FIELD_PATTERN.finditer(body):
            name = field_match.group("name").lower()
            fields[name] = strip_braces(field_match.group("value"))
        parsed.append((kind, key, fields))
    return parsed


def dedupe_key(kind: str, fields: dict[str, str]) -> str:
    title = slug(fields.get("title", ""))
    year = re.sub(r"[^0-9]", "", fields.get("year", "")) or "nd"
    return f"{kind}::{year}::{title}"


def format_entry(kind: str, key: str, fields: dict[str, str]) -> str:
    ordered_names = [
        "author",
        "title",
        "booktitle",
        "journal",
        "year",
        "pages",
        "publisher",
        "organization",
        "volume",
        "number",
        "doi",
        "url",
        "eprint",
        "archiveprefix",
        "primaryclass",
        "note",
        "howpublished",
    ]
    field_lines = []
    for name in ordered_names:
        value = fields.get(name)
        if value:
            field_lines.append(f"  {name} = {{{value}}}")
    for name in sorted(fields):
        if name not in ordered_names and fields[name]:
            field_lines.append(f"  {name} = {{{fields[name]}}}")
    return "@{kind}{{{key},\n{body}\n}}".format(kind=kind, key=key, body=",\n".join(field_lines))


def main() -> int:
    args = parse_args()
    input_path = Path(args.input_bib)
    output_path = Path(args.output) if args.output else input_path.with_name(f"{input_path.stem}.normalized.bib")

    entries = parse_entries(input_path.read_text(encoding="utf-8"))
    seen = set()
    output_entries = []
    for kind, _, fields in entries:
        fingerprint = dedupe_key(kind, fields)
        if fingerprint in seen:
            continue
        seen.add(fingerprint)
        new_key = build_key(fields)
        output_entries.append(format_entry(kind, new_key, fields))

    output_path.write_text("\n\n".join(output_entries) + "\n", encoding="utf-8")
    print(f"Wrote {len(output_entries)} normalized entries to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
