---
name: ai-research-landscape
description: Build verified research landscape summaries and curated bibliographies for AI topics. Use when Codex receives a concrete AI research direction, task, or seed papers and needs to search Google Scholar and Google, trace the field through surveys and canonical papers, generate search plans and candidate sets, rank candidates by recency and influence, extract or normalize BibTeX, repair the Python environment when dependencies are missing, and deliver a research-status markdown document plus a source-grounded `.bib` file.
---

# AI Research Landscape

## Overview

Build a literature landscape for a concrete AI topic by combining live search, citation-aware filtering, source verification, deterministic post-processing, and environment self-checks. Produce two primary outputs:

- `research-status.md`
- `references.bib`

Read [references/workflow.md](references/workflow.md) first. Read [references/input-schema.md](references/input-schema.md) before creating or editing the candidate dataset.

## Trigger And Scope

Use this skill when the user gives:

- a research direction such as `real-time video generation` or `world models`
- a concrete task such as `summarize the field`, `collect the 30 representative works`, or `build a bib`
- optional seed papers, labs, venues, or company systems
- a broken Python environment that prevents validation or bibliography tooling

Prefer this skill for AI and ML research mapping. Do not use it for unverifiable speculation or for requests that explicitly avoid live search.

## Required Working Rules

1. Browse the web. Do not rely on memory for paper existence, dates, venues, blogs, or BibTeX fields.
2. Treat Google Scholar and ordinary Google search as the primary discovery surfaces, not the only acceptable bibliography source.
3. Verify every selected work against a real source:
   - paper landing page such as arXiv, OpenReview, CVF, PMLR, ACM, IEEE, Nature, Springer, or a publisher page
   - DOI-backed metadata services such as Crossref when used to obtain BibTeX
   - or an official technical blog or company research page
4. Do not include a work if the title, authorship, year, or source cannot be confirmed.
5. Prefer top venues, top journals, strong arXiv preprints, and official research blogs from major labs.
6. Keep early papers only if they are clearly foundational.
7. Make the final bibliography intentionally curated, not merely the top 30 search hits.
8. The final `.bib` must come from a traceable source. Manual BibTeX invented from memory is forbidden.
9. If Python tooling fails, run `scripts/check_python_env.py` first and repair with `scripts/bootstrap_python_env.py` before continuing.

## Workflow

### 0. Check Or Repair The Python Environment

Run:

- `python scripts/check_python_env.py`
- if not ready: `python scripts/bootstrap_python_env.py --venv-dir .venv`
- then use `.venv\Scripts\python.exe` on Windows or `.venv/bin/python` on Unix-like systems for validation and skill scripts

This skill currently expects Python 3.10+ and `PyYAML` for validator compatibility.

### 1. Capture The Query

Extract the topic, constraints, seed papers, desired count, and output path.

### 2. Generate The Search Workspace

Create a starter workspace with:

- `python scripts/generate_search_plan.py --topic "..." --count 30 --seed-paper "..." --seed-lab "..."`
- generated files: `search-plan.md`, `queries.txt`, `candidates.seed.json`

Use this before live search so the topic, queries, and seed hints stay reproducible.

### 3. Find Surveys First

Search Google Scholar for survey, review, or tutorial papers in the area. Use those surveys to recover canonical subtopics, historical milestones, and citation hubs.

If a survey is on arXiv and a source archive is available, inspect it with `scripts/extract_arxiv_bibliography.py`.

If Scholar exports are available as BibTeX, import them with `scripts/import_bibtex_candidates.py` and merge them into the working candidate JSON.

### 4. Expand The Candidate Pool

Build candidates from:

- survey references
- Google Scholar cited-by and related-articles expansion
- recent venue or archive search
- OpenAlex, Semantic Scholar, Crossref, DBLP, or similar metadata sources for candidate expansion and cross-checking
- official company or lab pages when non-paper systems matter
- imported BibTeX from Google Scholar, publisher pages, OpenReview, DBLP, or Crossref

Keep the working dataset in JSON using [references/input-schema.md](references/input-schema.md).

### 5. Verify Metadata

For each candidate, confirm title, authorship or organization, year, venue, canonical URL, and citation count when available. Use `verified: true` only after a real-source check.

### 6. Rank And Filter

Run `scripts/rank_candidates.py`. The default ranking policy is:

- within 2 years and highly cited
- within 2 years and moderately cited
- within 2 to 5 years and highly cited
- older than 5 years only if highly influential or clearly foundational

Use ranking as a starting point, not as a substitute for judgment.

### 7. Build The Final Set

Aim for coverage across:

- surveys
- foundational works
- major paradigm shifts
- strongest recent papers
- official technical blogs only when they materially shape the field

### 8. Build A Source-Grounded BibTeX

Collect BibTeX only from traceable sources and normalize it with `scripts/normalize_bibtex.py`.

Preferred BibTeX source order:

1. Crossref DOI content negotiation BibTeX
2. Official publisher or venue BibTeX
3. Google Scholar `Cite -> BibTeX`
4. DBLP or OpenReview BibTeX when official and consistent
5. Generated from official JSON metadata only as a documented fallback

For every final entry, record its provenance in the candidate JSON. Do not hand-write BibTeX from memory.

### 9. Draft The Research Status Report

Use `scripts/build_research_digest.py` to draft the markdown, then refine the final narrative manually.

## Output Standard

Default deliverables:

- `research-status.md`
- `references.bib`
- optionally `candidates.ranked.json`
- optionally the topic workspace generated by `scripts/generate_search_plan.py`

If the user requests a different count, pass `--top-n` to the scripts and reflect that number in the report.

## Scripts

- `scripts/check_python_env.py`
- `scripts/bootstrap_python_env.py`
- `scripts/generate_search_plan.py`
- `scripts/import_bibtex_candidates.py`
- `scripts/rank_candidates.py`
- `scripts/normalize_bibtex.py`
- `scripts/build_research_digest.py`
- `scripts/extract_arxiv_bibliography.py`

## References

- [references/workflow.md](references/workflow.md)
- [references/input-schema.md](references/input-schema.md)
- [references/source-quality.md](references/source-quality.md)
- [references/environment.md](references/environment.md)

## Practical Notes

- If Google Scholar is rate-limited or blocked, keep browsing for discovery and verification, then obtain BibTeX from a traceable source such as Crossref, DBLP, OpenReview, a publisher page, or another official metadata endpoint.
- When citation counts are unavailable, set them to `null` rather than guessing.
- When a blog and a paper both describe the same work, prefer the paper in the `.bib` and mention the blog only if it adds unique system detail.
- Prefer a dedicated virtual environment for this skill rather than mutating the global Python installation.
- If a BibTeX entry is generated from metadata rather than downloaded directly, mark that provenance explicitly and keep the upstream source URL.
