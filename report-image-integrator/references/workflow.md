# Workflow

## Minimal Path

1. Read the report Markdown and understand its section logic.
2. Inspect every candidate image visually.
3. Decide which images are worth keeping.
4. Draft a small insertion plan with:
   - anchor
   - figure caption
   - figure label
   - renamed filename
   - optional lead-in text
   - optional follow-up text
5. Run `scripts/apply_image_plan.py`.
6. Re-open the Markdown and verify that the figure references read naturally.

## Anchor Strategy

Prefer `insert_after_text` anchors that match an existing paragraph exactly. This is the most conservative mode because it preserves the original report structure.

Use `insert_before_text` only when the figure needs to appear before an interpretation paragraph.

Use `replace_text` only when the report already contains a placeholder image sentence or obsolete image link that should be replaced directly.

Each anchor string should be unique inside the Markdown file. If it is not unique, revise the anchor before running the script.

## Caption And Label Heuristics

Caption:

- describe what the reader can see
- avoid vague names such as `result-figure`
- keep it short but specific

Label:

- use lowercase letters, digits, and hyphens
- encode the content, not the source filename
- examples:
  - `fig:system-overview`
  - `fig:training-loss-curve`
  - `fig:ui-annotation-page`

Renamed image filename:

- start with `fig-XX-`
- reuse the semantic label stem
- preserve the original extension when possible
- example: `fig-02-training-loss-curve.png`

## Editing Boundary

Allowed edits:

- insert figure block
- add one or two local sentences so the figure is introduced and referenced properly
- replace a stale placeholder image link or placeholder sentence

Disallowed edits:

- rewriting whole sections
- changing claims that are unrelated to the figure
- changing terminology globally
- reorganizing headings
