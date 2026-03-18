---
name: draft-ai-phd-reports
description: Draft polished AI PhD reports in Markdown from user requirements, outlines, rough notes, existing `.md` text, paper PDFs, or `.bib` files. Use when Codex needs to write or rewrite doctoral proposal reports, daily or weekly or monthly reports, midterm reports, progress summaries, research statements, or other AI PhD-facing academic documents; remove obvious AI-generated tone; preserve a coherent professional narrative; verify factual claims and paper details with live search when needed; and integrate accurate citations or cross-references from user-provided bibliography data or source papers.
---

# Draft AI PhD Reports

## Overview

Write AI PhD reports that read like serious academic prose rather than generic assistant output. Produce a final Markdown document grounded in the user's materials, explicit requirements, verified external facts when needed, and accurate citation handling.

When the user provides an existing Markdown draft, first audit whether its structure, headings, terminology, and Markdown mechanics match the expected report genre and will survive downstream `md2all` conversion cleanly.

Read [references/workflow.md](references/workflow.md) first. Load [references/report-types.md](references/report-types.md) when choosing a document structure. Load [references/style-guide.md](references/style-guide.md) before drafting. Load [references/citation-and-evidence.md](references/citation-and-evidence.md) whenever the user provides papers, claims, URLs, or bibliography files.

## Trigger And Scope

Use this skill when the user asks for any of the following in an AI PhD context:

- draft a new report from requirements
- rewrite a rough draft, notes, or fragmented Markdown into polished prose
- produce a doctoral proposal or opening report
- write a daily, weekly, monthly, semester, or annual progress report
- write a PhD midterm report or related assessment document
- integrate references from `.bib`, manually supplied citations, or source papers
- take an existing report plus a not-yet-cross-referenced `.bib` and weave the bibliography into the body text
- verify research facts, paper claims, dates, benchmarks, or terminology before writing

Do not use this skill for casual blog posts, speculative claims that cannot be sourced, or outputs whose final format is not Markdown unless the user explicitly asks for a later conversion step handled elsewhere.

## Non-Negotiable Rules

1. Treat the user's supplied facts, deadlines, and institutional constraints as primary unless they conflict internally or with verified sources.
2. Browse when claims, paper metadata, timelines, benchmarks, or field status may be stale or uncertain.
3. Do not invent citations, quoted findings, evaluation numbers, project milestones, or advisor expectations.
4. Keep the prose professional, specific, and connected. Avoid list-heavy filler unless the document type truly requires concise enumerations.
5. When writing in Chinese, follow Chinese academic writing habits rather than English sentence order translated into Chinese; prefer natural transitions, moderate sentence length, and institutionally familiar section framing.
6. For Chinese doctoral opening reports and similar formal proposal materials, prefer the institutional self-referential style using 本课题 rather than first-person forms such as 我、我的、本人 unless the user explicitly asks for first-person voice.
6. Preserve the user's actual contribution boundaries. Do not exaggerate progress or claim results the user has not achieved.
7. When evidence is incomplete, write conservatively and mark the gap instead of hallucinating.
8. Output a Markdown file or Markdown-ready body text only.
9. For each input Markdown report, infer the expected institutional genre before rewriting. If the text is an opening report, default to a mainland China PhD opening-report frame unless the user specifies another template.
10. Audit headings and title hierarchy before drafting. Fix malformed heading depth, vague section names, and title wording that does not fit the report type.
11. Audit English terminology inside Chinese text. On first appearance of an important technical term, give the full English form when useful and add the standard abbreviation when needed; later mentions may use the Chinese term, the abbreviation, or the established mixed form consistently.
12. Prefer Markdown structures that are deterministic for `md2all` and Quarto or Pandoc conversion. Avoid decorative formatting that is likely to map poorly to DOCX styles.
13. When the user provides an existing Markdown report, default to a short preflight diagnosis before rewriting so the report type, structure problems, terminology issues, and `md2all` mapping are explicit.
14. When the user provides a report draft plus an uncited `.bib`, treat bibliography integration as a first-class rewriting task rather than a final cosmetic pass.
15. In bibliography-integration tasks, try to use the supplied entries as fully as the evidence allows, but do not force a citation into a claim the paper does not support.

## Workflow

### 1. Establish The Writing Task

Identify:

- document type
- target audience such as advisor, committee, department, or lab
- language preference
- required sections or formatting constraints
- source materials supplied by the user
- whether factual verification or citation integration is required

If the user gives a weak prompt, infer the smallest safe scope and continue.

For an existing Markdown draft, classify the genre before rewriting:

- opening report or doctoral proposal
- midterm report
- periodic progress report
- research statement or summary

Then infer the standard section architecture that a mainland Chinese PhD committee, advisor, or department would usually expect unless the user provides a stricter institutional template.
At the same time, infer the most likely downstream `md2all` template family:

- opening report or midterm-heavy academic review: prefer `proposal-midterm`
- general research progress summary or formal academic writeup: prefer `academic-report`
- only fall back to non-academic templates when the genre is clearly administrative rather than research-facing

### 2. Build The Evidence Base

Gather facts from:

- user notes and draft text
- provided `.md`, plain text, PDFs, URLs, or screenshots if available
- provided `.bib` files or citation snippets
- live web search for unstable or missing facts

Verify paper titles, authors, years, venues, and claim-level statements before relying on them.

If the user provides a report draft plus a separate `.bib` that has not yet been cited in the body, explicitly build a citation coverage plan:

- cluster the bibliography by theme
- map each cluster to likely sections or paragraphs in the report
- identify entries that need live abstract or metadata verification before use
- decide whether any section, especially `国内外研究现状`, needs substantive expansion so the bibliography can be integrated naturally

### 3. Audit The Source Markdown First

Before substantive drafting, inspect the source Markdown for:

- whether the document title names the actual report genre clearly
- whether heading levels are monotonic and logically nested
- whether section names match the report type instead of using generic placeholders
- whether bilingual terminology is introduced consistently
- whether citations, figures, tables, and lists are written in a form likely to render stably through `md2all`
- whether the heading and content density match the intended `md2all` academic template

If the source already contains institution-specific headings, preserve that frame and improve the wording beneath it. If the source structure is obviously incompatible with the genre, repair the structure first and then rewrite the prose.

For existing Markdown inputs, provide a short preflight block before the rewrite unless the user explicitly asks for draft-only output.

Recommended fields:

- report type judgment
- expected standard structure
- title or heading problems
- terminology or first-mention English issues
- citation or bibliography issues
- recommended `md2all` template
- whether YAML front matter needs to be added or cleaned
- whether the draft is suitable for direct polishing or needs structural rewrite first

### 4. Choose The Document Architecture

Select a structure from [references/report-types.md](references/report-types.md). Adapt it to the user's institution and maturity of work rather than copying a rigid template.

### 5. Draft In Natural Academic Prose

Apply [references/style-guide.md](references/style-guide.md). Prefer flowing paragraphs, explicit transitions, and claim-evidence-reasoning links. Use bullet lists sparingly and only when they improve readability or satisfy a required format. If the output is in Chinese, default to formal Chinese academic prose shaped by common mainland university report conventions unless the user specifies another regional style.

### 6. Integrate Citations Carefully

Apply [references/citation-and-evidence.md](references/citation-and-evidence.md). Use only citations that can be mapped to actual sources. If the user gives a `.bib`, align citation keys with the written text and write the research-status or related-work section around the supplied bibliography rather than around uncited generalities. If the user gives papers without a `.bib`, cite consistently in Markdown-friendly form and summarize any missing metadata.

For the common case of `existing report + uncited .bib`, do all of the following:

- rewrite the literature review or research-status section around the supplied entries rather than merely appending citations
- expand or split paragraphs when needed so each citation supports a concrete claim
- try to cover as much of the supplied bibliography as is defensible
- run a final citation-key coverage check so uncited entries are deliberate rather than accidental

### 7. Perform A Final Audit

Check:

- tone is not robotic or repetitive
- section ordering is coherent
- claims match the evidence
- dates, metrics, and paper details are internally consistent
- Markdown headings and citation markers are usable as-is
- the document title, section names, and heading levels fit the inferred report genre
- key English technical terms are expanded on first appearance when that helps academic clarity
- Markdown is conservative enough for `md2all` to render into standard DOCX styles without ad hoc cleanup
- the report would map cleanly to the inferred `md2all` template, usually `proposal-midterm` or `academic-report`

## Output Standard

Default output:

- one complete Markdown document
- with a clear title and section hierarchy
- with integrated citations or reference placeholders that correspond to real sources
- with no meta commentary about being an AI assistant unless the user explicitly asks for process notes

For `report draft + uncited .bib` inputs, the default deliverable should be:

- one fully revised Markdown document
- with bibliography-aware rewriting rather than citation-only patching
- with Pandoc-style citation keys already inserted in the body
- with Markdown conservative enough for direct `md2all` conversion to DOCX

When revising an existing Markdown draft, the default interaction may be:

1. a concise preflight diagnosis
2. the revised Markdown document

Keep the diagnosis short and operational rather than essay-like.

If the user asks for revision rather than a fresh draft, preserve the original factual content where valid and improve structure, prose quality, and evidentiary support.

## References

- [references/workflow.md](references/workflow.md)
- [references/report-types.md](references/report-types.md)
- [references/style-guide.md](references/style-guide.md)
- [references/citation-and-evidence.md](references/citation-and-evidence.md)
- [references/markdown-and-md2all-compat.md](references/markdown-and-md2all-compat.md)


