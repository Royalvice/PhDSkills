# Workflow

## Goal

Turn a topic such as `real-time video generation` into:

- a verified `research-status.md`
- a verified `references.bib`
- an optional ranked machine-readable candidate list
- an optional reproducible topic workspace with queries and seed candidates

## Environment First

Before doing anything else, run:

- `python scripts/check_python_env.py`
- if missing modules or pip issues are reported: `python scripts/bootstrap_python_env.py --venv-dir .venv`

Then rerun the check with the virtual-environment interpreter. Use that interpreter for `quick_validate.py` and all skill scripts.

## Search Order

1. Generate the search workspace with `scripts/generate_search_plan.py`.
2. Find high-citation surveys or reviews.
3. Use those surveys to identify canonical terms, milestones, and citation hubs.
4. Expand with Google Scholar cited-by and related-articles exploration.
5. Import available BibTeX exports with `scripts/import_bibtex_candidates.py` when useful.
6. Search recent top-venue and arXiv work for the latest two-year frontier.
7. Search official company or lab pages for influential non-paper systems.
8. Verify every shortlisted work individually.
9. Build the final `.bib` only from traceable sources.

## Query Patterns

Use targeted queries rather than a single broad query.

Examples:

- `"real-time video generation" survey`
- `"video generation" CVPR diffusion real-time`
- `"world model" survey robotics`
- `"Genie 3" Google blog`

## Candidate Construction

Maintain a working JSON file with one object per candidate. Include discovery channel, source URL, Scholar URL when available, venue, year, citations, survey or blog flags, BibTeX provenance fields, and notes on why the work matters.

Use `verified: false` until the source is checked.

## Verification Standard

Keep a work only if at least one of these is true:

- the paper is on an official venue or publisher page
- the paper is on arXiv and metadata matches
- the blog is on an official company, lab, or product site
- the metadata is confirmed by a trusted scholarly index and matches the canonical source

Reject or defer candidates with inconsistent year or title, unclear authorship, mirror sites without a canonical source, or likely hallucinated names from memory.

## Ranking Policy

The ranker encodes the default preference:

1. recent and highly cited
2. recent and moderately cited
3. mid-recent and highly cited
4. old but foundational

Manual overrides are expected.

## Curated Set Composition

For a 30-item list, a strong default distribution is:

- 2 to 4 surveys
- 5 to 8 foundational papers
- 8 to 12 transition or consolidation papers
- 8 to 12 recent frontier papers
- 0 to 3 official technical blogs or product pages

## Research Status Markdown Structure

1. Title and scope
2. Executive summary
3. Field evolution
4. Major research threads
5. Current frontier
6. Representative work list
7. Open problems
8. Source and verification notes

## BibTeX Rules

- final BibTeX must come from a traceable source, never from memory
- prefer Crossref DOI BibTeX, official publisher BibTeX, or official venue BibTeX
- Google Scholar BibTeX is acceptable but not mandatory
- DBLP or OpenReview BibTeX is acceptable when it matches the canonical paper metadata
- metadata-derived BibTeX is fallback-only and must be marked in provenance
- normalize keys into a stable format
- deduplicate title variants
- keep URLs for arXiv, OpenReview, CVF, PMLR, and blogs
- use `@misc` for blogs or product pages when no better type exists
