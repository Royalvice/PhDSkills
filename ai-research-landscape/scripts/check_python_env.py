#!/usr/bin/env python3
"""
Check Python runtime health for the ai-research-landscape skill.
"""

from __future__ import annotations

import argparse
import importlib
import json
import shutil
import sys
from pathlib import Path

DEFAULT_MODULES = ["yaml"]
MIN_VERSION = (3, 10)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check Python and dependency availability.")
    parser.add_argument("--modules", nargs="*", default=DEFAULT_MODULES, help="Import names to check. Defaults to yaml.")
    parser.add_argument("--format", choices=("text", "json"), default="text", help="Output format.")
    parser.add_argument("-o", "--output", help="Optional output file path.")
    return parser.parse_args()


def module_status(name: str) -> dict:
    try:
        module = importlib.import_module(name)
        return {"name": name, "ok": True, "version": getattr(module, "__version__", None), "error": None}
    except Exception as exc:
        return {"name": name, "ok": False, "version": None, "error": str(exc)}


def build_report(modules: list[str]) -> dict:
    version_ok = sys.version_info >= MIN_VERSION
    pip_path = shutil.which("pip") or shutil.which("pip3")
    report = {
        "python_executable": sys.executable,
        "python_version": ".".join(str(part) for part in sys.version_info[:3]),
        "python_version_ok": version_ok,
        "minimum_python_version": ".".join(str(part) for part in MIN_VERSION),
        "venv_active": sys.prefix != getattr(sys, "base_prefix", sys.prefix),
        "pip_available": bool(pip_path),
        "pip_path": pip_path,
        "modules": [module_status(name) for name in modules],
    }
    report["all_modules_ok"] = all(item["ok"] for item in report["modules"])
    report["ok"] = report["python_version_ok"] and report["all_modules_ok"] and report["pip_available"]
    return report


def render_text(report: dict) -> str:
    lines = [
        f"Python executable: {report['python_executable']}",
        f"Python version: {report['python_version']} (required >= {report['minimum_python_version']})",
        f"Virtual environment active: {'yes' if report['venv_active'] else 'no'}",
        f"Pip available: {'yes' if report['pip_available'] else 'no'}",
    ]
    for item in report["modules"]:
        if item["ok"]:
            version = f" ({item['version']})" if item["version"] else ""
            lines.append(f"Module {item['name']}: OK{version}")
        else:
            lines.append(f"Module {item['name']}: MISSING - {item['error']}")
    lines.append(f"Overall status: {'OK' if report['ok'] else 'NOT READY'}")
    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()
    report = build_report(args.modules)
    output = json.dumps(report, indent=2, ensure_ascii=False) + "\n" if args.format == "json" else render_text(report)
    if args.output:
        Path(args.output).write_text(output, encoding="utf-8")
    else:
        print(output, end="")
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
