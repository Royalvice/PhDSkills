#!/usr/bin/env python3
"""
Inspect an arXiv source archive or extracted directory for bibliography files and citation usage.
"""

from __future__ import annotations

import argparse
import json
import re
import tarfile
import tempfile
import zipfile
from pathlib import Path


BIB_COMMAND_PATTERN = re.compile(r"\\bibliography\{([^}]+)\}")
CITE_PATTERN = re.compile(r"\\cite\w*\{([^}]+)\}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Extract bibliography hints from an arXiv source archive.")
    parser.add_argument("source_path", help="Path to a tar.gz, zip, or extracted source directory")
    parser.add_argument("-o", "--output", help="Output JSON path")
    return parser.parse_args()


def iter_files(root: Path):
    for path in root.rglob("*"):
        if path.is_file():
            yield path


def inspect_root(root: Path) -> dict:
    bib_files = []
    tex_files = []
    cite_keys = set()
    bibliography_refs = set()

    for path in iter_files(root):
        suffix = path.suffix.lower()
        if suffix == ".bib":
            bib_files.append(str(path.relative_to(root)))
        if suffix == ".tex":
            tex_files.append(str(path.relative_to(root)))
            content = path.read_text(encoding="utf-8", errors="ignore")
            for match in BIB_COMMAND_PATTERN.finditer(content):
                bibliography_refs.update(name.strip() for name in match.group(1).split(","))
            for match in CITE_PATTERN.finditer(content):
                cite_keys.update(name.strip() for name in match.group(1).split(","))

    return {
        "bib_files": sorted(bib_files),
        "tex_files": sorted(tex_files),
        "bibliography_refs": sorted(bibliography_refs),
        "cite_keys": sorted(cite_keys),
    }


def inspect_path(path: Path) -> dict:
    if path.is_dir():
        return inspect_root(path)

    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_root = Path(tmpdir)
        lower_name = path.name.lower()
        if lower_name.endswith((".tar.gz", ".tgz", ".tar")):
            with tarfile.open(path) as archive:
                archive.extractall(tmp_root)
        elif lower_name.endswith(".zip"):
            with zipfile.ZipFile(path) as archive:
                archive.extractall(tmp_root)
        else:
            raise ValueError("Unsupported source path. Use a directory, .zip, .tar, .tar.gz, or .tgz.")
        return inspect_root(tmp_root)


def main() -> int:
    args = parse_args()
    source_path = Path(args.source_path)
    output_path = Path(args.output) if args.output else source_path.with_suffix(".bibliography.json")

    result = inspect_path(source_path)
    output_path.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote bibliography summary to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
