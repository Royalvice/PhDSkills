# Workflow

## Defaults

- Target format: `docx`
- Input types: `md`, `qmd`
- Scope: single source file
- Output location: next to the source file
- Temp artifacts: temporary directory only
- Validation: basic structural checks
- LLM use: disabled unless the user asks or fallback is explicitly allowed

## Rendering flow

1. Run `scripts/doctor.py` checks or `md2all.py --doctor`.
2. Normalize `md` to temporary `qmd`.
3. Infer template, locale, and default CSL.
4. Resolve bibliography:
   - Use user-supplied bibliography if present.
   - Otherwise infer a minimal `.bib` from reference strings in the Markdown.
5. Build or patch a temporary `reference.docx` for DOCX output.
6. Run `quarto render` with a stable environment for the current platform.
7. Run `scripts/validate_outputs.py`.
8. Only save a report when the user explicitly requests one.

## Output policy

- `docx`: strongest path; prefer editable Office Math and stable captions/cross-references.
- `pdf`: basic but usable; prefer Quarto PDF with TinyTeX.
- `html`: basic readable output with family-specific styling direction.

## Dependency policy

- `quarto` is required for all rendering.
- `python-docx` is required when DOCX output needs a generated built-in `reference.docx`.
- `rsvg-convert` is optional and only needed for deterministic SVG rasterization workflows.
- Missing optional helpers should not block a successful render unless the active path truly depends on them.

## Failure policy

- Do not stop on non-major citation or cross-reference issues.
- Replace unrecoverable citation keys with `ref-missing-N`.
- Warn on formula degradation rather than failing the whole run.
- Fail early when a required dependency for the selected output path is missing.
- Suggest LLM fallback after a deterministic failure; do not auto-rewrite.
