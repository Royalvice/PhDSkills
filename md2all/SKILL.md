---
name: md2all
description: Convert Markdown and Quarto Markdown into DOCX, PDF, and HTML publishing outputs with a DOCX-first workflow. Use when Codex needs to render or validate .md or .qmd files, select or patch a reference.docx template, choose a CSL style, repair non-destructive citation or cross-reference issues, run Quarto or Pandoc publishing commands, or install and verify Quarto, Pandoc, and TinyTeX on Windows or macOS. Prefer the built-in scripts and template assets for deterministic conversion; only use LLM-assisted cleanup when the user explicitly asks for editing or when scripted conversion fails and a fallback is needed.
---

# MD2All

## Overview

Use the bundled scripts to turn single-file `md` or `qmd` inputs into publishing outputs with a deterministic, script-first workflow. Default to `DOCX`, keep fixes conservative, and only escalate to LLM help when the user requests revision work or when scripted conversion cannot recover.

## Quick Start

Run the main command from `scripts/md2all.py`.

```bash
python scripts/md2all.py input.md
python scripts/md2all.py input.md --to pdf
python scripts/md2all.py input.md --template degree-thesis --validate
python scripts/md2all.py --doctor
python scripts/md2all.py --install
```

Interpret the workflow this way:

1. Verify the environment first.
2. Normalize `md` into temporary `qmd` when needed.
3. Infer a template and locale unless the user overrides them.
4. Build a minimal `.bib` only when the user did not provide bibliography data.
5. Render with Quarto.
6. For DOCX output, post-process the rendered file to enforce built-in house styles for title, paragraph indentation, captions, and equation numbering.
7. Run structural validation.
8. Suggest LLM fallback only after a scripted failure or when the user asks for cleanup.

On Windows Codex sessions, if `quarto render` fails inside the sandbox with handle or process-spawn errors, rerun the render step outside the sandbox. Treat that as an execution-environment requirement rather than a document-content failure.

## Workflow

### 1. Diagnose before mutating content

Run `python scripts/md2all.py --doctor` or read [references/workflow.md](references/workflow.md) when:

- Quarto or Pandoc might be missing
- PDF output needs TinyTeX
- the user asks to "install", "fix", or "set up" the environment

On Windows, install with `winget`. On macOS, install with `brew`. Follow [references/install-windows-macos.md](references/install-windows-macos.md) for exact expectations.

### 2. Keep rendering deterministic

Default to the script pipeline instead of freeform editing:

- Use `scripts/normalize_markdown.py` to convert plain Markdown into temporary Quarto Markdown.
- Use `scripts/infer_template.py` to pick the closest built-in template.
- Use `scripts/build_bibliography.py` to infer a `.bib` when bibliography metadata is missing.
- Use `scripts/patch_reference_docx.py` to generate or patch `reference.docx`.
- Use `scripts/validate_outputs.py` after rendering.

Read [references/template-selection.md](references/template-selection.md) before overriding template heuristics. Read [references/bibliography-rules.md](references/bibliography-rules.md) before changing citation or bibliography behavior.

### 3. Default output policy

Apply these defaults unless the user overrides them:

- Output target: `docx`
- Output location: next to the source file
- Input scope: one `md` or `qmd` file
- Temporary files: use a temp directory instead of writing intermediates beside the source file
- Validation: run basic structural validation
- Reports: only save a Markdown report if the user explicitly asks for one

### 4. Built-in assets

Use the built-in asset catalogs in `assets/`:

- `assets/reference-docx/template-catalog.json`
- `assets/reference-docx/profiles/*.json`
- `assets/csl/catalog.json`

The template families are:

- Academic: `degree-thesis`, `proposal-midterm`, `academic-report`
- Business: `business-report`, `business-brief`, `business-handout`
- Daily: `general-document`, `notice-explanation`, `resume`

Each built-in template fully defines heading styles, body typography, block quotes, lists, margins, and formal headers and footers. User-supplied `reference.docx` or `.csl` files override the built-ins.

### 5. Conservative repair only

Do not rewrite substance by default. Limit scripted fixes to:

- normalizing line endings and front matter boundaries
- converting `md` to temporary `qmd`
- repairing obvious citation-key mismatches when a deterministic match exists
- replacing irreparable citation keys with `ref-missing-N`
- normalizing obvious cross-reference markers

Do not auto-generate document titles or add substantive headings. If the user explicitly asks for polishing, read [references/markdown-repair-rules.md](references/markdown-repair-rules.md) and then use LLM assistance intentionally.

### 6. LLM escalation boundary

Stay in pure script mode unless one of these is true:

- the user asks to edit, polish, rewrite, or fix the prose
- the user passes an explicit flag such as `--allow-llm-fix`
- scripted conversion fails and the user wants fallback help

When scripted conversion fails, summarize the deterministic failure first. Then propose LLM-assisted repair rather than jumping straight into edits.

## References

Read only what is needed:

- [references/workflow.md](references/workflow.md): end-to-end command flow and defaults
- [references/template-selection.md](references/template-selection.md): template heuristics, locale handling, and override policy
- [references/bibliography-rules.md](references/bibliography-rules.md): citation repair, inferred BibTeX, and CSL defaults
- [references/install-windows-macos.md](references/install-windows-macos.md): installation and verification policy
- [references/markdown-repair-rules.md](references/markdown-repair-rules.md): when to stay conservative and when to escalate
- [references/markdown2docx-borrow-and-avoid.md](references/markdown2docx-borrow-and-avoid.md): what to borrow and what not to copy from the inspected repository
