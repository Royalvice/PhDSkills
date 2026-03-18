# Markdown And MD2All Compatibility

## Goal

Write Markdown that stays semantically clear in source form and maps predictably into `md2all` and Quarto or Pandoc DOCX output.

## Preferred Structure

1. Use exactly one level-1 title at the top of the document.
2. Start major sections at level 2 headings and descend one level at a time.
3. Keep heading text short, formal, and genre-appropriate.
4. Use ordinary paragraphs as the default block form.
5. Use simple ordered or unordered lists only when the genre truly benefits from them.

## Template Mapping

Choose the likely `md2all` target before polishing the Markdown:

- `proposal-midterm`: opening reports, midterm reports, documents with dense academic sectioning, timelines, innovation points, and explicit feasibility discussion
- `academic-report`: research progress summaries, semester or annual progress reports, and other formal academic writeups with moderate section depth

If the document is clearly a research-facing PhD report, prefer one of these two templates before considering non-academic families.

## Avoid Fragile Markdown

Avoid or remove:

- manually simulated heading styles with bold text instead of `#` markers
- excessive blank lines inserted only for visual spacing
- mixed list markers or deeply nested lists without necessity
- tables used only for layout rather than data
- raw HTML unless the user explicitly needs it
- decorative separators such as repeated dashes or asterisks
- ad hoc numbering typed into headings when Markdown heading hierarchy already carries the structure

## Citations And References

Prefer citation forms that map cleanly to Pandoc or Quarto:

- `[@key]`
- `[@key, pp. 3-5]`
- `@key` only when the sentence grammar requires narrative citation

Keep citation keys stable. Do not switch styles mid-document.

If a `参考文献` section is written manually, keep it consistent with the supplied bibliography and avoid mixing free-text references with unresolved citation keys.

## Figures, Tables, And Captions

When the report needs figures or tables:

- use standard Markdown image syntax when possible
- keep captions concise and formal
- refer to figures and tables consistently in the prose
- avoid complex table layouts that depend on merged cells or manual spacing

## Front Matter And Metadata

If metadata is needed, keep YAML front matter minimal and well-formed.

Do not invent fields casually. Add only what the downstream conversion actually uses, such as:

- `title`
- `bibliography`
- `csl`
- `lang`

## Chinese Academic Reports

For Chinese PhD-facing reports rendered to DOCX:

- prefer explicit section headings over inline bold lead-ins
- keep one paragraph focused on one purpose to reduce awkward line wrapping after conversion
- avoid excessive English punctuation patterns inside Chinese prose
- keep bilingual term introductions compact so they do not distort paragraph rhythm
- if using `proposal-midterm`, ensure major level-2 headings align with a proposal or midterm committee reading path
- if using `academic-report`, keep the structure slightly lighter and avoid artificial proposal-only sections

## Final Check

Before finalizing, confirm:

- heading hierarchy is valid
- there is only one document title
- list formatting is consistent
- citation syntax is uniform
- no fragile visual-only Markdown remains

## Front Matter Suggestion

When producing a preflight diagnosis, explicitly state whether front matter should be:

- omitted because the document can rely on body headings only
- added minimally with fields such as `title`, `bibliography`, `csl`, or `lang`
- cleaned because existing YAML is malformed, redundant, or inconsistent with the body title
