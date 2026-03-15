# Borrow and Avoid from `markdown2docx`

## Borrow

- Treat templates as programmable assets rather than fixed files only.
- Run structural validation after conversion.
- Keep configuration and error handling explicit.

## Avoid

- Do not make a thin Pandoc wrapper the whole architecture; keep Quarto as the primary pipeline.
- Do not expose configuration values that have no implemented behavior.
- Do not overclaim output guarantees that validation does not actually verify.
- Do not confuse “file opens successfully” with “publishing result is semantically correct”.
