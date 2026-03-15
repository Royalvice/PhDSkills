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
6. Run `quarto render`.
7. Run `scripts/validate_outputs.py`.
8. Only save a report when the user explicitly requests one.

## Output policy

- `docx`: strongest path; prefer editable Office Math and stable captions/cross-references.
- `pdf`: basic but usable; prefer Quarto PDF with TinyTeX.
- `html`: basic readable output with family-specific styling direction.

## Failure policy

- Do not stop on non-major citation or cross-reference issues.
- Replace unrecoverable citation keys with `ref-missing-N`.
- Warn on formula degradation rather than failing the whole run.
- Suggest LLM fallback after a deterministic failure; do not auto-rewrite.
