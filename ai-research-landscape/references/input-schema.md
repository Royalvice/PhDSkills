# Input Schema

## Candidate JSON

Create a JSON array. Each item should follow this schema as closely as the available evidence allows.

```json
[
  {
    "title": "Example Paper Title",
    "authors": ["First Author", "Second Author"],
    "organization": null,
    "year": 2025,
    "venue": "CVPR",
    "citations": 184,
    "source_type": "paper",
    "canonical_url": "https://arxiv.org/abs/2501.00001",
    "scholar_url": "https://scholar.google.com/...",
    "discovery_channels": ["survey", "scholar"],
    "is_survey": false,
    "is_foundational": false,
    "is_blog": false,
    "is_arxiv": true,
    "verified": true,
    "bib_key": "example2025paper",
    "bib_source_type": "crossref_bibtex",
    "bib_source_url": "https://doi.org/...",
    "generated_from_metadata": false,
    "summary": "One-sentence reason the work matters.",
    "notes": "Optional evidence notes."
  }
]
```

## Field Guidance

Required in practice:

- `title`
- `year`
- `canonical_url`
- `source_type`
- `verified`

Strongly recommended:

- `authors` or `organization`
- `venue`
- `citations`
- `summary`
- `discovery_channels`
- `bib_key`
- `bib_source_type`
- `bib_source_url`

Useful during semi-automatic ingestion:

- `notes`
- `scholar_url`
- `organization`
- `generated_from_metadata`

## Ranked Output Fields

`rank_candidates.py` appends fields such as:

- `age_years`
- `citation_band`
- `venue_band`
- `priority_bucket`
- `score`
- `rank`

## BibTeX Input

`normalize_bibtex.py` accepts one or more `.bib` files merged into a single input before normalization.

`import_bibtex_candidates.py` converts exported BibTeX into candidate skeletons with `verified=false` for later checking.

## BibTeX Provenance Values

Recommended `bib_source_type` values:

- `crossref_bibtex`
- `publisher_bibtex`
- `venue_bibtex`
- `scholar_bibtex`
- `dblp_bibtex`
- `openreview_bibtex`
- `generated_from_metadata`
- `manual_fallback`

`manual_fallback` should be avoided in the final main bibliography. If it must exist temporarily, keep it outside the final deliverable and resolve it before completion.
