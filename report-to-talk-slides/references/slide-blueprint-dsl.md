# Slide Blueprint DSL

Use this file only when generating the final markdown deliverable for the `report-to-talk-slides` skill.

## Goal

Represent a full presentation as a compact but explicit markdown package that another person or agent can implement without guessing the slide logic, content density, visual hierarchy, collaboration reasoning, or delivery flow.

## Output File Names

Prefer a package like:

- `slide-blueprint.md`
- `slide-discussion-memory.md`
- `slide-speaking-aid.md`

Project-specific names are also acceptable, for example:

- `phd-proposal-slide-blueprint.md`
- `phd-proposal-discussion-memory.md`
- `phd-proposal-speaking-aid.md`

## Required Section Order

Use this exact top-level order:

1. `# Project`
2. `# Audience`
3. `# Storyline`
4. `# Design System`
5. `# Slide Blueprint`
6. `# Asset Checklist`
7. `# Open Questions`

If there are no open questions, write `None.` under that heading.

## Companion Deliverables

In addition to the slide blueprint, always produce:

1. a discussion memory markdown file using the exact section order in `## Discussion Memory Schema`
2. a speaking aid markdown file using the exact section order in `## Speaking Aid Schema`

## Project Section Schema

```md
# Project
- Title: ...
- Source Type: ...
- Output Type: Talk-ready slide blueprint
- Target Length: ... slides / ... minutes
- Tone: ...
```

## Audience Section Schema

```md
# Audience
- Primary Audience: ...
- Secondary Audience: ...
- Speaker Goal: ...
- Decision Pressure: high / medium / low
- Audience Prior Knowledge: ...
```

## Storyline Section Schema

```md
# Storyline
## One-Line Thesis
...

## Speaking Spine
1. ...
2. ...
3. ...
4. ...
5. ...

## Compression Strategy
- Keep: ...
- Compress: ...
- Omit: ...
```

## Design System Section Schema

```md
# Design System
- Overall Style: ...
- Typography Mood: ...
- Color Logic: ...
- Layout Rhythm: ...
- Visual Motifs: ...
- Motion Guidance: ...
- Density Rule: ...
```

## Slide Blueprint Section Schema

Each slide must use this exact template.

```md
## Slide NN - Short Title
- Purpose: Why this slide exists in the spoken sequence.
- Core Message: The one thing the audience should remember.
- Narrative Role: opening / context / tension / gap / method / evidence / plan / contribution / summary / closing
- Recommended Duration: ... seconds
- Layout: ...
- Visual Focus: ...
- On-Slide Text:
  - Title: ...
  - Subtitle: ...
  - Bullets:
    - ...
    - ...
    - ...
  - Labels / Callouts: ...
- Visual Elements:
  - Type: image / figure / table / chart / diagram / comparison / timeline / quote / none
  - Spec: ...
  - Source: user-provided / create-new / optional placeholder
- Speaker Notes:
  - ...
  - ...
- Transition In: ...
- Transition Out: ...
```

### Field Rules

#### Purpose
State why the slide must exist. Do not restate the title.

#### Core Message
Must be one sentence. No semicolons. No lists.

#### Narrative Role
Use one label only.

#### Recommended Duration
Use realistic spoken timing. Default range is 20 to 90 seconds.

#### Layout
Use concrete layout language. Good examples:
- `left text / right figure`
- `top thesis band + three comparison cards`
- `full-width pipeline with bottom takeaway strip`
- `2x2 evidence grid with highlighted bottom-right result`

#### Visual Focus
Describe primary and secondary focal areas and how attention should move.

#### On-Slide Text
Keep text sparse.
- Title: required
- Subtitle: optional
- Bullets: optional, max 5
- Labels / Callouts: optional, max 3 short items

Never include paragraphs here.

#### Visual Elements
`Spec` must explain what the visual shows and why it is there.

Examples:
- `A single annotated system diagram showing optical mapping from subpixel arrangement to output rays.`
- `A 4-column comparison table contrasting baseline methods, bottlenecks, proposed method, and expected gain.`
- `A timeline with 5 milestones, with the current stage highlighted in red.`

#### Speaker Notes
Use 2 to 4 short notes. These are for delivery logic, not a hidden transcript.

#### Transition In / Transition Out
Describe how this slide connects logically to adjacent slides.

## Asset Checklist Section Schema

```md
# Asset Checklist
- Required Images:
  - ...
- Required Tables:
  - ...
- Required Charts:
  - ...
- Optional Visual Enhancements:
  - ...
```

If a category is empty, write `None.`

## Open Questions Section Schema

Use this section to record blockers that prevent a clean final design.

Examples:
- missing project logo
- no confirmed audience expertise level
- no performance chart available for the method comparison slide

## Discussion Memory Schema

Use this exact top-level order:

1. `# Session`
2. `# User Preferences`
3. `# Discussion Trace`
4. `# Final Story Logic`
5. `# Reuse Notes`

```md
# Session
- Project Title: ...
- Source Type: ...
- Session Goal: ...
- Deck Scope: ... slides / ... minutes
- Current Status: draft / aligned / finalized
- Clarification Mode: built-in choice tool / plain-text fallback

# User Preferences
- Tone Preferences:
  - ...
- Slide Density Preferences:
  - ...
- Visual Preferences:
  - ...
- Storytelling Preferences:
  - ...
- Explicit Avoidances:
  - ...

# Discussion Trace
## Initial Direction
- ...

## Structured Question Rounds
1. Round Focus: ...
   - Options Presented: ...
   - User Selection: ...
   - Why it mattered: ...

## Key Turns
1. ...
2. ...
3. ...

## Decision Log
- Decision: ...
  - Why it changed: ...
  - Effect on deck: ...

# Final Story Logic
## One-Sentence Arc
...

## Story Beats
1. ...
2. ...
3. ...
4. ...
5. ...

## Slide Flow Summary
- Slide 01-03: ...
- Slide 04-06: ...

# Reuse Notes
- What to remember next time: ...
- What the user is likely to care about again: ...
- What should stay stable if this deck is revised: ...
```

### Discussion Memory Rules

- This file must preserve the reasoning path across multi-round discussion, not just the final answer.
- Focus on stable preferences and meaningful pivots.
- Record meaningful question rounds and the user's selections when structured questioning was used.
- Do not fabricate discussion points that did not happen.
- Compress minor back-and-forth, but retain decisions that changed scope, ordering, framing, or emphasis.

## Speaking Aid Schema

Use this exact top-level order:

1. `# Talk Strategy`
2. `# Slide-by-Slide Prompts`
3. `# Delivery Risks`

```md
# Talk Strategy
- Opening Posture: ...
- Explanation Rhythm: ...
- Emphasis Strategy: ...
- Transition Strategy: ...
- Q and A Preparation Cue: ...

# Slide-by-Slide Prompts
## Slide NN - Short Title
- Audience State: What the audience is likely thinking at this moment.
- Speaking Goal: What this slide needs to accomplish aloud.
- How To Explain It:
  1. ...
  2. ...
  3. ...
- Emphasis:
  - ...
- Keep Brief:
  - ...
- Transition Cue: ...

# Delivery Risks
- Risk: ...
  - Mitigation: ...
```

### Speaking Aid Rules

- Cover every slide in order.
- Provide delivery logic, not a hidden manuscript.
- The `How To Explain It` steps should be action-oriented and brief.
- `Keep Brief` should flag content the speaker may over-explain.
- `Audience State` should reflect the logical sequence of the talk.

## Example Slide Block

```md
## Slide 04 - Existing Methods Fall Short
- Purpose: Establish why the audience should not accept the status quo.
- Core Message: Existing methods fail because they optimize the wrong output target.
- Narrative Role: gap
- Recommended Duration: 45 seconds
- Layout: top thesis band + bottom 3-column comparison cards
- Visual Focus: Audience reads the thesis first, then scans left-to-right across three failure points.
- On-Slide Text:
  - Title: Why current pipelines are not enough
  - Subtitle: They are screen-centric, not light-field-native
  - Bullets:
    - Multi-view rendering repeats computation
    - Path tracing cost explodes under dense ray targets
    - Video world models remain physically weak
  - Labels / Callouts: screen-space, redundant rays, uncontrolled physics
- Visual Elements:
  - Type: comparison
  - Spec: Three cards comparing optical target mismatch, compute inefficiency, and controllability limits.
  - Source: create-new
- Speaker Notes:
  - Start from the audience's likely assumption that better compute alone solves the issue.
  - Reframe the problem as target mismatch rather than pure model weakness.
  - Use the final card to pivot into the need for a unified route.
- Transition In: Comes after the motivation slide that established why the application matters.
- Transition Out: Leads naturally into the slide that states the central research question.
```

## Style Preference

Prefer concise markdown that is readable in raw text. Avoid deep nesting beyond one bullet level inside each slide block.
