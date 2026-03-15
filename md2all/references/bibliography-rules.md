# Bibliography Rules

## Source order

1. User-provided bibliography file
2. Markdown reference strings inferred into a minimal `.bib`

## Default keys

Generate citation keys in `author-year-slug` form when enough metadata exists.

Examples:

- `zhang-2023-jisuan`
- `smith-2024-transformers`

## Broken key policy

- If a broken citation key can be matched deterministically to an existing entry, replace it.
- If the key cannot be repaired safely, replace it with `ref-missing-N`.
- Do not stop conversion for non-major citation issues.

## Inference policy

When only raw reference strings exist:

- infer the minimal set of BibTeX fields that can be identified
- prefer `misc` when the source type is unclear
- keep uncertain data rather than dropping it

## CSL defaults

- Chinese locale: default to a GB/T 7714 style
- English locale: default to a more suitable built-in style such as APA or IEEE
- user-provided `.csl` overrides the built-in default
