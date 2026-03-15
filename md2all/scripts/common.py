#!/usr/bin/env python3
from __future__ import annotations

import json
import platform
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

SKILL_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = SKILL_DIR / "assets"


def detect_platform() -> str:
    system = platform.system().lower()
    if "windows" in system:
        return "windows"
    if "darwin" in system:
        return "macos"
    return system


def find_executable(name: str) -> str | None:
    return shutil.which(name)


def run_command(command: list[str], check: bool = False) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, capture_output=True, text=True, check=check)


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_template_catalog() -> dict[str, Any]:
    return load_json(ASSETS_DIR / "reference-docx" / "template-catalog.json")


def load_csl_catalog() -> dict[str, Any]:
    return load_json(ASSETS_DIR / "csl" / "catalog.json")


def has_han(text: str) -> bool:
    return any("\u4e00" <= char <= "\u9fff" for char in text)


def infer_locale(text: str) -> str:
    return "zh" if has_han(text) else "en"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def eprint(message: str) -> None:
    print(message, file=sys.stderr)
