#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass

from common import detect_platform, find_executable, run_command


@dataclass
class ToolStatus:
    name: str
    found: bool
    path: str | None
    version: str | None
    notes: str | None = None


def read_version(command: list[str]) -> str | None:
    try:
        result = run_command(command)
    except OSError:
        return None
    output = (result.stdout or result.stderr).strip()
    if not output:
        return None
    return output.splitlines()[0]


def check_tool(name: str, version_command: list[str] | None = None, notes: str | None = None) -> ToolStatus:
    path = find_executable(name)
    if not path:
        return ToolStatus(name=name, found=False, path=None, version=None, notes=notes)
    version = read_version(version_command) if version_command else None
    return ToolStatus(name=name, found=True, path=path, version=version, notes=notes)


def collect_status() -> dict[str, object]:
    return {
        "platform": detect_platform(),
        "tools": [
            asdict(check_tool("quarto", ["quarto", "--version"])),
            asdict(check_tool("pandoc", ["pandoc", "--version"])),
            asdict(check_tool("xelatex", ["xelatex", "--version"], notes="Preferred TeX engine for PDF output")),
            asdict(check_tool("tlmgr", ["tlmgr", "--version"], notes="TinyTeX or TeX Live manager")),
            asdict(check_tool("winget", ["winget", "--version"], notes="Windows installer")),
            asdict(check_tool("brew", ["brew", "--version"], notes="macOS installer"))
        ]
    }


def print_text(status: dict[str, object]) -> None:
    print(f"Platform: {status['platform']}")
    for record in status["tools"]:
        marker = "OK" if record["found"] else "MISS"
        line = f"[{marker}] {record['name']}"
        if record["path"]:
            line += f" -> {record['path']}"
        if record["version"]:
            line += f" ({record['version']})"
        print(line)
        if record["notes"]:
            print(f"      {record['notes']}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Check md2all publishing dependencies.")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    status = collect_status()
    if args.json:
        print(json.dumps(status, ensure_ascii=False, indent=2))
    else:
        print_text(status)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
