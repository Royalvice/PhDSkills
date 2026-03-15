# Markdown Repair Rules

## Default posture

Stay conservative.

Allowed scripted repairs:

- normalize line endings
- normalize YAML front matter boundaries
- convert plain `md` to temporary `qmd`
- repair obvious citation-key mismatches
- replace irrecoverable citation keys with `ref-missing-N`
- normalize obvious cross-reference markers when the target is clear

## Do not do this by default

- rewrite prose
- add missing document titles
- invent headings
- add citations the source does not support
- restructure major sections

## Escalate to LLM only when

- the user explicitly asks for cleanup, rewriting, or polish
- deterministic conversion fails and the user wants fallback help

When escalating, preserve the original intent and keep the change list explicit.
