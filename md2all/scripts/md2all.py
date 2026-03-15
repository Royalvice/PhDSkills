#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
import subprocess
import uuid
from pathlib import Path

from build_bibliography import build_bib
from common import detect_platform, eprint, find_executable, read_text, run_command, write_text
from infer_template import infer
from validate_outputs import validate


def default_output_path(source: Path, target: str) -> Path:
    return source.with_suffix(f".{target}")


def install_dependencies() -> int:
    platform_name = detect_platform()
    if platform_name == "windows":
        commands = [["winget", "install", "--id", "Quarto.Quarto", "-e"], ["winget", "install", "--id", "Pandoc.Pandoc", "-e"]]
    elif platform_name == "macos":
        commands = [["brew", "install", "--cask", "quarto"], ["brew", "install", "pandoc"]]
    else:
        eprint("Automatic installation is only implemented for Windows and macOS.")
        return 1
    for command in commands:
        print(" ".join(command))
        subprocess.run(command, check=False)
    return 0


def ensure_quarto() -> bool:
    return find_executable("quarto") is not None


def maybe_build_bib(source_text: str, temp_dir: Path) -> Path | None:
    _, bib = build_bib(source_text)
    if not bib.strip():
        return None
    bib_path = temp_dir / "references.bib"
    write_text(bib_path, bib)
    return bib_path


def maybe_make_reference_docx(args: argparse.Namespace, temp_dir: Path) -> Path | None:
    if args.to != "docx":
        return None
    if args.reference_doc:
        return Path(args.reference_doc)
    output = temp_dir / "reference.docx"
    command = ["python", str(Path(__file__).with_name("patch_reference_docx.py")), "--template", args.template, "--output", str(output)]
    if args.font:
        command.extend(["--font", args.font])
    if args.font_size:
        command.extend(["--font-size", str(args.font_size)])
    if args.margin_cm:
        command.extend(["--margin-cm", str(args.margin_cm)])
    result = run_command(command)
    if result.returncode != 0:
        eprint(result.stderr.strip() or result.stdout.strip() or "Failed to generate reference.docx")
        return None
    return output


def build_quarto_command(args: argparse.Namespace, qmd_path: Path, output_path: Path, bib_path: Path | None, reference_doc: Path | None) -> list[str]:
    command = ["quarto", "render", str(qmd_path), "--to", args.to, "--output", output_path.name]
    if bib_path:
        command.extend(["--metadata", f"bibliography={bib_path}"])
    if args.csl:
        command.extend(["--metadata", f"csl={args.csl}"])
    if reference_doc:
        command.extend(["--metadata", f"reference-doc={reference_doc}"])
    if args.locale:
        command.extend(["--metadata", f"lang={args.locale}"])
    return command


def render(args: argparse.Namespace) -> int:
    source = Path(args.input).resolve()
    if not source.exists():
        eprint(f"Input file not found: {source}")
        return 1
    if not ensure_quarto():
        eprint("Quarto is not installed or not on PATH. Run `md2all --install` or `md2all --doctor`.")
        if args.allow_llm_fix:
            eprint("LLM fallback is allowed, but deterministic environment setup is still required before rendering.")
        return 1
    inferred = infer(source)
    args.template = args.template or inferred["template"]
    args.locale = args.locale or inferred["locale"]
    args.csl = args.csl or inferred["csl"]
    output_path = default_output_path(source, args.to)
    source_text = read_text(source)
    work_tmp = source.parent / ".md2all-tmp"
    work_tmp.mkdir(exist_ok=True)
    temp_dir = work_tmp / f"run-{uuid.uuid4().hex}"
    temp_dir.mkdir(parents=True, exist_ok=False)
    try:
        qmd_path = temp_dir / (source.stem + ".qmd")
        write_text(qmd_path, source_text)
        bib_path = Path(args.bibliography).resolve() if args.bibliography else maybe_build_bib(source_text, temp_dir)
        reference_doc = maybe_make_reference_docx(args, temp_dir)
        command = build_quarto_command(args, qmd_path, output_path, bib_path, reference_doc)
        result = subprocess.run(command, cwd=temp_dir, text=True, capture_output=True)
        if result.returncode != 0:
            eprint(result.stderr.strip() or result.stdout.strip() or "Quarto render failed")
            eprint("Deterministic rendering failed. Suggest LLM fallback only if the user wants assisted repair.")
            return result.returncode
        produced = temp_dir / output_path.name
        if not produced.exists():
            eprint(f"Expected output not produced: {produced}")
            return 1
        shutil.copy2(produced, output_path)
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)
    validation = validate(output_path)
    if not validation["ok"]:
        for issue in validation["issues"]:
            eprint(f"Validation issue: {issue}")
        if args.validate:
            return 1
    print(output_path)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="DOCX-first Markdown publishing pipeline for Quarto.")
    parser.add_argument("input", nargs="?")
    parser.add_argument("--to", choices=("docx", "pdf", "html"), default="docx")
    parser.add_argument("--template")
    parser.add_argument("--locale")
    parser.add_argument("--csl")
    parser.add_argument("--bibliography")
    parser.add_argument("--reference-doc")
    parser.add_argument("--font")
    parser.add_argument("--font-size", type=float)
    parser.add_argument("--margin-cm", type=float)
    parser.add_argument("--validate", action="store_true")
    parser.add_argument("--doctor", action="store_true")
    parser.add_argument("--install", action="store_true")
    parser.add_argument("--allow-llm-fix", action="store_true")
    args = parser.parse_args()
    if args.doctor:
        return subprocess.run(["python", str(Path(__file__).with_name("doctor.py"))], check=False).returncode
    if args.install:
        return install_dependencies()
    if not args.input:
        parser.error("input is required unless using --doctor or --install")
    return render(args)


if __name__ == "__main__":
    raise SystemExit(main())
