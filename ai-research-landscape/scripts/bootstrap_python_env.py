#!/usr/bin/env python3
"""
Create or repair a Python environment for the ai-research-landscape skill.
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
import venv
from pathlib import Path

DEFAULT_PACKAGES = ["PyYAML"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a virtual environment and install required packages.")
    parser.add_argument("--venv-dir", default=".venv", help="Virtual environment directory. Defaults to .venv in the current working directory.")
    parser.add_argument("--packages", nargs="*", default=DEFAULT_PACKAGES, help="Packages to install with pip. Defaults to PyYAML.")
    parser.add_argument("--mode", choices=("auto", "venv", "current"), default="auto", help="auto tries venv first and falls back to the current interpreter.")
    parser.add_argument("--dry-run", action="store_true", help="Print commands without executing them.")
    return parser.parse_args()


def venv_python_path(venv_dir: Path) -> Path:
    if os.name == "nt":
        return venv_dir / "Scripts" / "python.exe"
    return venv_dir / "bin" / "python"


def run(command: list[str], dry_run: bool) -> None:
    print(" ".join(command))
    if not dry_run:
        subprocess.run(command, check=True)


def create_venv(venv_dir: Path, dry_run: bool) -> Path:
    if dry_run:
        print(f"Would create virtual environment at {venv_dir}")
        return venv_python_path(venv_dir)
    builder = venv.EnvBuilder(with_pip=True)
    builder.create(venv_dir)
    print(f"Created virtual environment at {venv_dir}")
    return venv_python_path(venv_dir)


def install_packages(python_path: Path, packages: list[str], dry_run: bool) -> None:
    run([str(python_path), "-m", "pip", "install", "--upgrade", "pip"], dry_run)
    if packages:
        run([str(python_path), "-m", "pip", "install", *packages], dry_run)


def main() -> int:
    args = parse_args()
    venv_dir = Path(args.venv_dir).resolve()
    python_path: Path | None = None
    used_mode = args.mode

    if args.mode in ("auto", "venv"):
        try:
            python_path = create_venv(venv_dir, args.dry_run)
            used_mode = "venv"
        except Exception as exc:
            if args.mode == "venv":
                raise
            print(f"Virtual environment creation failed: {exc}")
            print("Falling back to the current interpreter.")
            python_path = Path(sys.executable)
            used_mode = "current"
    else:
        python_path = Path(sys.executable)

    install_packages(python_path, args.packages, args.dry_run)
    print(f"Bootstrap mode: {used_mode}")
    print(f"Use this interpreter for validation and scripts: {python_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
