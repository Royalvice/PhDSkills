# Session Memory Schema

Use this file when the `draft-ai-phd-reports` skill needs to persist what happened across a multi-turn writing or revision session.

Goal:

- preserve stable user preferences that should carry into the next session
- track repeated user corrections rather than only the latest draft state
- record bad cases that caused dissatisfaction or rework
- record best practices that produced better acceptance
- help the next session avoid relearning the same lessons

## When To Create Or Update Memory

Create or update a session memory when any of the following is true:

- the user revises the same report over multiple turns
- the user repeatedly comments on tone, structure, terminology, or citation style
- the task involves iterative polishing rather than one-shot drafting
- the user rejects one or more generated versions and explains why
- the task is likely to continue in later sessions

Do not force a memory file for a trivial one-shot request unless the user explicitly wants persistent reuse.

## Preferred File Naming

Prefer one of these names next to the report output:

- `<report-stem>.session-memory.md`
- `<project-name>-draft-memory.md`

If the user already has a memory file for the same report family, continue updating that file instead of creating competing variants.

## Required Section Order

Use this exact top-level order:

1. `# Session`
2. `# Source Context`
3. `# Stable Preferences`
4. `# Revision Trace`
5. `# Bad Cases`
6. `# Best Practices`
7. `# Reuse Guidance`

## Section Schema

```md
# Session
- Project or Report: ...
- Report Type: ...
- Language: ...
- Main Task: ...
- Current Status: draft / revising / finalized
- Memory Status: new / resumed / consolidated

# Source Context
- Input Materials:
  - ...
- Institutional Constraints:
  - ...
- Downstream Publishing Target:
  - ...
- Known Evidence Limits:
  - ...

# Stable Preferences
- Tone Preferences:
  - ...
- Structure Preferences:
  - ...
- Terminology Preferences:
  - ...
- Citation Preferences:
  - ...
- Explicit Avoidances:
  - ...

# Revision Trace
## Initial Draft Direction
- ...

## Change Requests Across The Session
1. User Request: ...
   - Affected Part: ...
   - Interpretation: ...
   - Action Taken: ...
   - Outcome: accepted / partially accepted / rejected / pending

## Pattern Summary
- Repeated Corrections:
  - ...
- One-Off Corrections:
  - ...

# Bad Cases
1. Pattern: ...
   - Why it failed: ...
   - Evidence from session: ...
   - Avoid next time: ...

# Best Practices
1. Practice: ...
   - Why it worked: ...
   - Evidence from session: ...
   - Reuse scope: opening report / midterm / progress report / literature review / general

# Reuse Guidance
- What to apply immediately next time:
  - ...
- What to verify again instead of assuming:
  - ...
- Open preference questions still unresolved:
  - ...
```

## Writing Rules

- Record only what the session actually supports.
- Prefer pattern-level lessons over storing raw draft fragments.
- Distinguish stable preferences from temporary task-specific instructions.
- Use the user's own terminology when that improves reuse clarity.
- Keep bad cases concrete. A vague item such as `too AI-like` is not enough unless you explain what made it feel that way.
- Keep best practices actionable. A vague item such as `write better` is useless.

## What Counts As A Bad Case

Good examples:

- paragraphs that sound like generic AI summary prose rather than doctoral academic writing
- literature review sections that list papers without synthesizing the research thread
- Chinese text that mirrors English sentence order too closely
- exaggerated contribution claims that go beyond the user's actual progress
- citation dumping where references are appended without claim-level support

Bad examples:

- `user disliked it`
- `style was wrong`
- `needs improvement`

## What Counts As A Best Practice

Good examples:

- using `本课题` instead of first-person voice in formal Chinese proposal writing
- front-loading a short preflight diagnosis before structural rewriting
- expanding the first mention of a technical term with English full name and abbreviation
- distributing citations across concrete claims instead of stacking them in one paragraph
- preserving institution-specific heading frames while improving the prose beneath them

## Reuse Rule

At the start of a future session on the same report line:

1. read the prior memory first
2. extract stable preferences and high-confidence bad cases
3. avoid repeating previously rejected patterns
4. keep unresolved items as questions rather than assumptions
