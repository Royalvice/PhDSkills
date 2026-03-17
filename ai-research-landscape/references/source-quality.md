# Source Quality

## Preferred Evidence Order

1. Official paper landing pages or official archives
2. Top conference or journal pages
3. arXiv
4. OpenReview, CVF, PMLR, ACM, IEEE, Springer, Nature, Science
5. Official lab or company technical blogs
6. Reliable metadata aggregators used only as support, not as sole evidence

## Preferred BibTeX Source Order

1. Crossref DOI content negotiation
2. Official publisher or venue BibTeX
3. Google Scholar `Cite -> BibTeX`
4. DBLP or OpenReview BibTeX
5. Metadata-derived BibTeX generated from a trusted API and explicitly marked as such

The final `.bib` must be traceable. Never fabricate fields or compose a BibTeX entry from memory.

## Venue Taste

Prefer work from strong venues relevant to the topic, for example:

- `CVPR`, `ICCV`, `ECCV`, `NeurIPS`, `ICLR`, `ICML`
- `SIGGRAPH`, `SIGGRAPH Asia`
- `ACL`, `EMNLP`, `NAACL`
- `TPAMI`, `IJCV`, `Nature`, `Science`
- `CoRL`, `RSS`, `ICRA`

Treat recent arXiv papers as acceptable when the field is moving faster than the review cycle and the work is already influential or from credible labs.

## Blog Admissibility

Include a blog or product page only if it is official, technically meaningful, and part of the field's practical trajectory.

Do not include general news reports, reposts, or marketing-only pages.

## Foundational Paper Rule

Older papers should be included only when the work started a major methodological family, remains a citation anchor, or is repeatedly identified as a milestone by later surveys.
