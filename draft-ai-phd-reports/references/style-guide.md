# Style Guide

## Target Voice

Write like a careful doctoral researcher addressing an advisor or review committee:

- calm
- specific
- logically connected
- professionally modest
- analytically confident

Avoid the tone of marketing copy, grant hype, or generic AI-generated exposition.

## Default Prose Rules

1. Prefer paragraphs over long bullet lists.
2. Let each paragraph advance one clear idea and connect naturally to the next.
3. State claims with appropriate confidence; use hedging only when evidence is genuinely incomplete.
4. Replace empty intensifiers such as "very important", "highly significant", or "greatly improves" with concrete reasoning.
5. Avoid repetitive rhetorical templates such as "First..., Second..., Finally..." unless the genre requires them.
6. Keep terminology consistent across the document.
7. In Chinese reports, introduce important English technical terms on first appearance when that improves precision, then reuse the established short form consistently.

## Anti-Patterns To Remove

Rewrite or delete:

- generic opening filler about the rapid development of AI unless it is relevant and sourced
- broad claims with no relation to the user's actual topic
- inflated statements about innovation without support
- excessive signposting that fragments the prose
- bullet explosions where connected paragraphs would read better

## Paragraph Construction

Use a simple academic cadence:

1. open with the paragraph's claim or purpose
2. supply evidence, examples, or explanation
3. close by linking to the next issue or implication

## Language Adaptation

If the user writes in Chinese, maintain formal written Chinese rather than translated English syntax. If the user writes in English, prefer direct academic English over bureaucratic phrasing.

When revising bilingual material, preserve technical terms that are standard in the field and avoid unnatural forced translation of paper titles or benchmark names.

For first mentions in Chinese prose:

- if the Chinese term alone may be ambiguous, give `中文名（English Full Name, Abbreviation）`
- if the abbreviation is already the dominant form in the field, give `中文名（Abbreviation, English Full Name）` or a natural equivalent
- later mentions should not repeatedly expand the same term unless a new section genuinely requires reintroduction
- avoid gratuitous English expansion for very common terms that are already standard in Chinese academic writing

## Chinese Writing Adaptation

When the output is Chinese, adapt explicitly to Chinese academic writing habits:

1. Open sections by anchoring the topic, scope, or stage before expanding details.
2. Prefer smooth connective phrasing such as `在此基础上`、`进一步而言`、`结合前述分析`、`总体来看` when transitions are needed, but do not overuse stock connectors.
3. Keep the register formal and steady; avoid spoken fillers, slogan-like emphasis, and translated rhetorical patterns.
4. Use moderate sentence length. Split long English-style chains into two or more Chinese sentences when needed.
5. Let paragraphs accumulate logic gradually; do not force every paragraph into a rigid topic-sentence template if that makes the Chinese read mechanically.
6. Preserve commonly used Chinese academic section names when suitable, such as `研究背景与意义`、`国内外研究现状`、`研究内容`、`技术路线`、`阶段性进展`、`下一步工作计划`.

## Chinese Anti-Patterns

Rewrite or remove:

- `首先、其次、最后` repeated mechanically across many paragraphs
- empty macro statements such as `人工智能技术正在飞速发展` when they do not serve the user's topic
- obvious English-to-Chinese calques such as overusing `对于……来说` or `本文将会`
- stacked four-character phrases used only for decoration
- pseudo-official phrasing that sounds like administrative boilerplate rather than academic writing

## Chinese Tone Target

Aim for the tone commonly found in competent doctoral materials: restrained, clear, evidence-aware, and procedurally grounded. The text should sound like it was written by a serious researcher reporting real work to an advisor or committee, not by a publicity office or a generic assistant.

## Markdown-Aware Writing

Write with downstream DOCX conversion in mind:

1. Prefer true headings over bold pseudo-headings.
2. Keep paragraph structure simple enough for style templates to control spacing.
3. Use tables only for genuine tabular data.
4. Avoid mixing multiple visual conventions for the same semantic role.
5. Keep captions, list items, and citations syntactically regular.
