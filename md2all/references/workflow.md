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
   - In Windows Codex sessions, if sandboxed execution fails with `Invalid handle` or equivalent process-spawn errors, rerun `quarto render` outside the sandbox.
   - Keep the rendered input file in the source directory when the Markdown uses relative image paths. Do not move the temporary `qmd` into a nested temp folder unless you also rewrite or explicitly set resource paths.
7. For DOCX output, run `scripts/postprocess_docx.py` to normalize house styles and layout details that Quarto may override directly in the document XML.
   - Verify figure captions are numbered as `图N ...` and that figure references like `@fig:...` or `[fig:... ?]` do not remain as raw tokens in the final `docx`.
8. Run `scripts/validate_outputs.py`.
9. Only save a report when the user explicitly requests one.

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

## Recorded Bad Cases

### 2026-03-18: Relative image paths lost during DOCX render

- Symptom: `docx` output was created, but images were missing because `md2all.py` wrote the temporary `.qmd` into `.md2all-tmp/run-*`, so Markdown image paths like `01-立体依据-figures/...` no longer resolved relative to the render input.
- Root cause: Quarto resolved relative resources from the temporary `.qmd` location instead of the original source directory.
- Fix: Write the temporary `.qmd` beside the source file and render from `source.parent`.
- Best practice: After any DOCX render that should include images, inspect the archive for `word/media/*` entries before considering the output complete.

### 2026-03-18: Figure captions and figure references not resolved in DOCX

- Symptom: captions appeared without figure numbers, and body text still contained raw tokens such as `@fig:overall-research-plan` or `[fig:research-status-evolution?]`.
- Root cause: the render path produced bookmarks for figure labels but did not convert all cross-reference syntaxes into final DOCX text.
- Fix: extend `scripts/postprocess_docx.py` to number figure captions in document order and rewrite unresolved figure-reference tokens to `图N`.
- Best practice: After rendering academic Markdown with figures, inspect `word/document.xml` for raw `fig:` tokens and patch them before delivery.
