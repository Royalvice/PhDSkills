# Citation And Evidence

## Inputs You May Receive

The user may provide:

- a `.bib` file
- an existing report whose body does not yet cite the supplied `.bib`
- plain citation text
- paper titles
- PDFs
- URLs
- claims that need support

Normalize these inputs before drafting.

## Core Rules

1. Cite only sources that can be identified with reasonable confidence.
2. Verify bibliographic details before attaching a citation to a claim.
3. Do not attribute a conclusion to a paper unless the paper actually supports it.
4. Distinguish between what the user did and what prior work did.
5. If a citation key is missing or broken, fix the mapping or note the gap explicitly.
6. Keep citation syntax uniform so the document remains compatible with `md2all` and Pandoc-style rendering.

## Working With `.bib`

When a `.bib` file is supplied:

- reuse the user's citation keys where possible
- check whether keys match the cited works in the text
- avoid silently switching to incompatible keys
- keep the prose citation-friendly for later Pandoc or Quarto rendering
- treat the `.bib` as the default evidence pool for the research-status or related-work section
- in that section, discuss the literature through explicit citations to the provided entries instead of writing generic survey prose with sparse references
- prefer organizing the narrative by themes, paradigms, or technical tensions that can be supported directly by the provided bibliography

If the `.bib` clearly contains malformed or duplicate entries, correct them conservatively and mention any unresolved ambiguity. If the `.bib` is too weak or incomplete for a credible research-status section, state the gap and expand the evidence base with verified additional sources rather than hallucinating support.

If the user provides an existing report plus an uncited `.bib`, also do the following:

- audit which entries are already implicit in the draft even if not cited
- decide where each thematic cluster belongs in the document
- expand `国内外研究现状` or other review sections when necessary so the bibliography can be used naturally
- try to maximize defensible coverage of the supplied entries instead of leaving most keys unused
- run a final check for uncited keys and either place them appropriately or leave them out deliberately

## Working With Papers Or URLs

When the user supplies papers or URLs but no bibliography:

- recover canonical metadata from the source
- cite consistently in a Markdown-friendly way
- maintain a short reference list if the document benefits from one

## Claim-Level Verification

Verify claims that include:

- benchmark numbers
- publication years
- novelty statements
- comparisons to prior methods
- dataset descriptions
- policy or industry context

If verification is not possible, soften the statement or remove it.

## Cross-Reference Practice

Use citations to support the narrative, not to decorate it. Introduce related work where it sharpens the argument:

- to define the problem setting
- to show what has been attempted
- to justify a methodological choice
- to explain why the user's direction remains necessary

Avoid dumping multiple citations at the end of a sentence unless each one clearly serves the same point.

When the goal is to use as much of a supplied `.bib` as possible, prefer widening the literature narrative by themes or method families rather than padding unrelated sentences with extra keys.

## Markdown-Friendly Citation Practice

When the final document is intended for Markdown-to-DOCX conversion:

- prefer one citation syntax family throughout the document
- avoid mixing raw bibliography prose with unresolved citation keys
- keep reference-section headings conventional, such as `参考文献` or `References`
- ensure manually written citations and bibliography metadata do not contradict each other
- when a report is rewritten around a supplied `.bib`, do a key-coverage check before finalizing
