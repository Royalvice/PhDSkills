# Template Selection

## Families

Academic:

- `degree-thesis`
- `proposal-midterm`
- `academic-report`
  - Chinese academic reports default to a doctoral-style layout with asymmetric margins, centered page header, GB/T-friendly body typography, and heading levels through `Heading 4`

Business:

- `business-report`
- `business-brief`
- `business-handout`

Daily:

- `general-document`
- `notice-explanation`
- `resume`

## Heuristics

Use deterministic heuristics before asking the user:

- Prefer academic templates when the document contains many headings, citations, figures, tables, or academic keywords such as `abstract`, `references`, `method`, `实验`, `参考文献`.
- Prefer business templates when the document uses executive, market, project, meeting, or brief-style keywords such as `summary`, `roadmap`, `市场`, `会议纪要`, `汇报`.
- Prefer daily templates for notices, resumes, applications, and general prose.

Use locale-specific defaults:

- detect Chinese by the presence and density of Han characters
- keep the same family but allow locale variants for typography and CSL defaults

## Override policy

- If the user supplies `reference.docx`, use it instead of the built-in template.
- If the user supplies `.csl`, use it instead of the built-in default.
- If the user specifies a template name, skip heuristic selection.
- Allow common CLI overrides for font, font size, and margins.

## Patch scope

The template patcher is allowed to change:

- heading 1/2/3 styles
- body font and size
- line and paragraph spacing
- block quote style
- list formatting basics
- margins
- formal header/footer layout

Do not assume advanced section-level page logic in v1.
