# Workflow

## Intake

Extract the minimum writing brief:

- report type
- topic and research direction
- intended reader
- language
- deadline or reporting period
- required evidence and available materials
- whether a session memory already exists for this report line

If the user supplies only a fragment, infer a sensible academic frame and continue without blocking.

At intake, decide whether the task is memory-worthy. Default to `yes` when the user is iterating on the same report, refining preferences, or likely to return for another revision round.

If the user supplies Markdown, perform a lightweight format diagnosis before rewriting:

- what report genre the Markdown appears to target
- whether the title names that genre explicitly
- whether the heading tree is structurally sound
- whether the current section labels match standard academic usage for that genre
- whether the Markdown is conservative enough for downstream `md2all` DOCX conversion

Unless the user asks for direct drafting only, expose this diagnosis briefly before the rewrite so the editing basis is explicit.

## Decide The Drafting Mode

Use one of four modes:

1. Fresh draft: the user provides requirements but little text.
2. Structural rewrite: the user provides a draft that is factually usable but poorly organized.
3. Evidence-grounded rewrite: the user provides draft text plus papers, URLs, or a `.bib`, and expects stronger factual support.
4. Bibliography-integration rewrite: the user provides an existing report plus a `.bib` whose entries are not yet cross-referenced in the body, and expects a fully cited rewritten Markdown document.

In parallel, choose one memory mode:

1. Resume memory: a prior session-memory file exists and should be loaded first.
2. Start memory: the task is likely to continue across multiple turns or sessions.
3. Skip memory: the task is clearly one-shot and no reuse value is visible.

## Recover The Core Story

Before drafting, identify the thread that should carry the document:

- research problem
- current progress
- why the work matters
- what has been completed
- what remains risky or uncertain
- what the next stage will deliver

The thread should appear across the document, not only in the introduction.

Also recover the behavioral story of the session:

- what the user cares about most
- what kinds of edits the user keeps requesting
- what kinds of generated language the user rejects
- what changes improved acceptance in later iterations

## Infer The Expected Standard Form

For each report, decide what a standard version of that genre should look like before editing the prose.

Examples:

- an opening report should usually follow a mainland Chinese doctoral opening-report frame unless the user provides institution-specific headings
- a midterm report should foreground completed work, deviation from the original plan, current risks, and the next-stage plan
- a periodic progress report should stay concise and should not be inflated into a proposal-style document

Use the inferred standard form to judge whether the source Markdown needs structural repair.

## Audit The Markdown Surface

Before line-level rewriting, check:

- title accuracy and formality
- heading depth and ordering
- whether bold text is being misused as pseudo-headings
- whether key terms in bilingual prose are introduced consistently
- whether list, table, citation, and image syntax is likely to survive `md2all` conversion

Repair the structure first when the current Markdown would otherwise force awkward DOCX output.

If a prior memory exists, use it during the audit to catch known failure patterns early. Example: if the memory says the user rejects list-heavy prose in opening reports, treat that as an audit warning before drafting.

## Preflight Output Format

For existing Markdown drafts, prefer a short preflight summary in this shape:

1. `报告类型判断` or `Report Type`
2. `标准结构判断` or `Expected Structure`
3. `标题与层级问题` or `Heading Issues`
4. `术语与英文首现问题` or `Terminology Issues`
5. `引文与参考文献问题` or `Citation Issues`
6. `推荐 md2all 模板` or `Recommended md2all Template`
7. `Front Matter 建议` or `Front Matter Suggestion`
8. `处理方式` or `Edit Mode`
9. `记忆文件策略` or `Session Memory Mode`

Keep each item brief. The purpose is to guide the rewrite, not to replace it.

When the task is `report draft + uncited .bib`, add two extra checks in the preflight:

10. `文献覆盖计划` or `Citation Coverage Plan`
11. `国内外研究现状是否需要扩写` or `Related-Work Expansion Need`

## Verify Before You Assert

Browse the web whenever the document depends on unstable or specific facts, including:

- paper publication status
- venue names and years
- benchmark results
- claims about what prior work did or did not solve
- recent project timelines
- public policy or funding context

For bibliography-integration tasks, browsing is especially important when the `.bib` contains recent papers, niche model names, or works whose relevance to a paragraph is not obvious from title alone. Use abstract-level verification before attaching those citations.

Prefer primary sources:

- official paper pages
- publisher or venue pages
- arXiv when appropriate
- official lab, company, or project pages

## Draft Order

Draft in this order unless the user requests a different process:

1. title and positioning paragraph
2. section outline
3. core narrative sections
4. evidence and citations
5. conclusion, next-stage plan, or reflective ending

For `existing report + uncited .bib`, insert a citation pass between steps 3 and 4:

- cluster bibliography entries by topic
- expand the literature review where needed so citations enter naturally
- distribute citations across the document rather than stacking them into one paragraph
- check that every intentionally used key appears in the body in Pandoc-compatible form

This order reduces drift and makes it easier to keep the document coherent.

Across the drafting and revision cycle, maintain a lightweight working memory:

- stable user preferences
- repeated edits requested by the user
- bad cases that triggered dissatisfaction
- best practices that resolved those issues

Update the persistent memory file at the end of each meaningful revision round, not only at the very end of the entire project.

## Revision Pass

Perform at least one explicit revision pass for:

- paragraph-to-paragraph transitions
- removal of generic filler
- reduction of repetitive sentence openings
- consistent tense and perspective
- alignment between claims and citations
- compliance with requested Markdown structure
- compliance with the inferred report-standard structure
- first-mention expansion of important English technical terms when needed
- conservative Markdown compatible with `md2all`
- final citation-key coverage for supplied `.bib` files, especially when the original draft had no inline citations
- whether the session memory now captures the stable lessons of this round

## Memory Maintenance Rules

When a session memory is active:

- read it before drafting
- keep updating it when the user adds corrections or rejects a draft
- separate stable preferences from one-off local requests
- record why a bad case failed, not only that it failed
- record what replacement worked better and where it should be reused

At minimum, persist:

- tone preferences that were repeated or clearly emphasized
- structure choices the user corrected more than once
- terminology constraints that should carry forward
- citation handling patterns the user accepted or rejected
- best-practice lessons tied to specific report genres

Use [session-memory-schema.md](session-memory-schema.md) for the final structure.
