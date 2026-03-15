#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import zipfile
from pathlib import Path

from common import read_text


def validate_docx(path: Path) -> list[str]:
    issues: list[str] = []
    if not path.exists():
        return ["DOCX output not found"]
    if path.stat().st_size == 0:
        issues.append("DOCX output is empty")
        return issues
    try:
        with zipfile.ZipFile(path, "r") as archive:
            names = archive.namelist()
            for required in ("[Content_Types].xml", "_rels/.rels", "word/document.xml"):
                if required not in names:
                    issues.append(f"Missing DOCX member: {required}")
    except zipfile.BadZipFile:
        issues.append("DOCX output is not a valid ZIP archive")
    return issues


def validate_pdf(path: Path) -> list[str]:
    issues: list[str] = []
    if not path.exists():
        return ["PDF output not found"]
    if path.stat().st_size == 0:
        issues.append("PDF output is empty")
        return issues
    if path.read_bytes()[:5] != b"%PDF-":
        issues.append("PDF header signature is missing")
    return issues


def validate_html(path: Path) -> list[str]:
    issues: list[str] = []
    if not path.exists():
        return ["HTML output not found"]
    if "<html" not in read_text(path).lower():
        issues.append("HTML root tag not found")
    return issues


def validate(path: Path) -> dict[str, object]:
    suffix = path.suffix.lower()
    if suffix == ".docx":
        issues = validate_docx(path)
    elif suffix == ".pdf":
        issues = validate_pdf(path)
    elif suffix in {".html", ".htm"}:
        issues = validate_html(path)
    else:
        issues = [f"Unsupported output type: {suffix}"]
    return {"path": str(path), "ok": not issues, "issues": issues}


def main() -> int:
    parser = argparse.ArgumentParser(description="Run basic structural validation on md2all outputs.")
    parser.add_argument("output", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = validate(args.output)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"ok={str(result['ok']).lower()}")
        for issue in result["issues"]:
            print(f"issue={issue}")
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
