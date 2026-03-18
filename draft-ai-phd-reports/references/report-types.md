# Report Types

## Doctoral Proposal Or Opening Report

Recommended `md2all` template: `proposal-midterm`

Typical structure:

1. research background and significance
2. literature review and current state of the art
3. research objectives and key questions
4. research content and technical route
5. innovation points and expected contributions
6. feasibility, prior foundation, and resources
7. timeline and milestones
8. references

Emphasize scholarly positioning, gap identification, and a credible plan rather than overclaiming completed results.

For Chinese PhD opening reports, also audit:

- whether the title explicitly signals `开题报告` or an equivalent formal label
- whether `国内外研究现状` and `研究目标与拟解决的关键问题` are separated clearly
- whether `研究内容` and `技术路线` are distinct rather than merged into vague prose
- whether `创新点` is written conservatively as expected contributions or possible innovations when progress is still preliminary

Checklist:

- title is formal and genre-explicit, not a topic fragment only
- level-2 headings cover background, related work, objectives, content or route, innovation, feasibility, timeline, and references or bibliography as needed
- literature review is not collapsed into a single generic introduction section
- technical route is specific enough to justify feasibility
- timeline is concrete rather than a slogan-like closing paragraph

## Daily, Weekly, Or Monthly Report

Recommended `md2all` template: `academic-report` by default. Use a daily or general template only if the document is plainly administrative and not intended as a research report.

Typical structure:

1. overview of the reporting period
2. concrete work completed
3. interim findings or observations
4. problems encountered and how they were handled
5. next-step plan

Keep these reports compact and specific. Replace inflated summary language with concrete progress, blockers, and near-term actions.

Audit these reports for over-structuring. If the draft looks like a proposal, compress it back to a reporting-period frame.

Checklist:

- title includes the reporting period or stage
- completed work is separated from next-step plan
- problems and responses are concrete rather than generic self-evaluation
- section count stays compact and does not mimic a thesis chapter outline

## Midterm Report

Recommended `md2all` template: `proposal-midterm`

Typical structure:

1. original research plan and adjustments
2. progress against objectives
3. research outputs to date
4. technical difficulties and risk assessment
5. next-stage work plan
6. self-evaluation or stage summary
7. references if required

Balance honesty and confidence. The document should show traction, reflection, and a credible path to completion.

Audit whether the report distinguishes:

- originally planned tasks
- completed work
- current problems
- adjusted next steps

Checklist:

- title explicitly signals `中期报告`, `中期检查报告`, or an institutionally equivalent label
- the original plan and actual progress can be compared directly
- stage outputs are described conservatively and can be evidenced
- risks are real technical or research risks, not empty cautionary language
- next-stage plan responds to the identified deviations or bottlenecks

## Research Progress Summary

Recommended `md2all` template: `academic-report`

Use when the user asks for a generic progress report without a formal template.

Suggested structure:

1. topic and stage definition
2. completed research tasks
3. literature or experimental progress
4. current insights and remaining gaps
5. plan for the next cycle

Checklist:

- title reflects the research stage rather than a vague summary label
- sections stay oriented toward progress, insights, gaps, and next work
- if there is literature content, it supports progress assessment instead of turning into a standalone proposal review

## Adaptation Rules

Adjust the structure based on the user's materials:

- If literature coverage is strong, expand the review and positioning sections.
- If experiments dominate, foreground setup, findings, and interpretation.
- If progress is limited, write candidly about groundwork, reading, implementation, and risk reduction instead of inflating outcomes.
- If the institution requires fixed headings, preserve them and improve only the substance beneath them.
- If the source title or headings do not clearly match the genre, repair the labels before polishing the paragraphs.
- Prefer `proposal-midterm` when the report needs stronger formal academic heading styles and proposal-like sections.
- Prefer `academic-report` when the report is a research-facing narrative progress document without heavy proposal structure.

## Chinese Section Naming

When the document is in Chinese and the user does not provide a fixed template, prefer section names that match Chinese academic usage. Typical options include:

- 研究背景与意义
- 国内外研究现状
- 研究目标与拟解决的关键问题
- 研究内容与技术路线
- 已开展工作与阶段性进展
- 存在的问题与后续计划
- 预期创新点或预期成果
- 进度安排

Adjust these labels to the actual report type instead of applying them mechanically.

If the source Markdown uses generic headings such as `Introduction`, `Method`, or `Plan` for a Chinese doctoral administrative report, replace them with the genre-appropriate Chinese academic labels unless the institution explicitly requires English headings.
