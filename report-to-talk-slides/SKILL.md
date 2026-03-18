---
name: report-to-talk-slides
description: Create talk-ready slide blueprints from dense reports, theses, proposals, technical writeups, or long notes. Use when Codex needs to discuss content with the user, compress it into a coherent speaking storyline, strictly limit text per slide, and output a markdown slide design spec covering page-by-page text, layout, visuals, images, tables, contrast, and presentation flow.
---

# Report To Talk Slides

## Overview

Turn a detailed written report into a concise, speaker-friendly slide blueprint rather than directly generating a finished PPT. Work with the user iteratively, reduce information density aggressively, and produce a final package of markdown deliverables:

- one slide blueprint that specifies every slide's purpose, spoken logic, on-slide text, layout, visuals, images, tables, and contrast cues
- one discussion memory file that captures the multi-round discussion history, the user's preferences, the reasoning path behind major structure decisions, and the final storytelling arc
- one speaking aid file that gives page-by-page delivery logic so the user knows how to talk through each slide without receiving a word-for-word script

Read [references/slide-blueprint-dsl.md](references/slide-blueprint-dsl.md) before drafting the final output. Use its schema and field names exactly for the slide blueprint and the companion file templates.

## Core Operating Rules

- Optimize for live explanation, not document completeness.
- Design for understanding in sequence. Each slide must answer why it exists and why it appears at that point.
- Cut text early. If a sentence is not needed on screen, move it into presenter notes or omit it.
- Default to 1 core message per slide.
- Prefer comparison, hierarchy, and progressive disclosure over paragraph blocks.
- Never let a slide become a report page. If content is crowded, split it.
- Make visual intent explicit even when no image assets exist yet.
- Treat the discussion itself as structured input. During multi-round collaboration, keep track of user preferences, rejected options, framing adjustments, and narrative pivots.
- The discussion memory file and speaking aid file are mandatory outputs, not optional add-ons.
- The speaking aid must explain delivery intent and transition logic for every slide, but it must not become a full sentence-by-sentence script.
- Prefer multi-round clarification over one-shot assumptions when talk structure, audience, or emphasis is unclear.
- Prefer Codex built-in choice-based questioning tools for clarification rounds so the user can select among curated options instead of typing open-ended answers.
- When the built-in questioning tool is available, use it as the default interaction mode for scope, audience, tone, deck length, emphasis, and visual-style decisions.
- When the built-in questioning tool is unavailable in the current mode, fall back to concise plain-text questions, but still frame them as explicit options first and minimize free-form input.
- Do not ask all questions at once. Ask in small batches that directly affect the next structural decision.

## Discussion Workflow

### 0. Run a structured clarification loop

Before outlining slides, drive the conversation through multiple short decision rounds instead of asking for a long free-form brief.

Priority rule:

- first choice: use the Codex built-in questioning tool to ask 1 to 3 multiple-choice questions per round
- second choice: if the tool is unavailable, ask concise plain-text questions that still present explicit options and a recommended default

Question design rules:

- ask only questions that change slide structure, narrative order, density, or visual strategy
- avoid redundant questions when the answer is already implied by the user's material
- keep each round narrow, then use the answers to decide the next round
- prefer user selection over open-ended typing
- do not exceed 3 questions in one round

Recommended early rounds:

- round 1: audience, talk goal, duration
- round 2: deck density, storytelling posture, emphasis area
- round 3: visual style, figure/table allocation, whether to include Q and A or backup slides

### 1. Build the speaking objective

Identify the talk context before outlining slides. Clarify only what materially changes structure:

- audience: advisor committee, defense panel, class, investor, internal team, mixed audience
- talk goal: explain, persuade, defend, align, teach, summarize
- duration: short, medium, long, or exact minutes
- delivery mode: formal academic, technical briefing, public talk, internal review
- available assets: none, figures only, screenshots, charts, tables, logos, photos

If the user already gave enough context, do not ask redundant questions.
But if key presentation choices remain uncertain, do not silently assume them. Run another short question round and resolve them explicitly.

### 2. Distill the report into a speaking spine

Convert the source report into a short narrative spine:

- opening context
- problem tension
- gap or insufficiency in existing work
- proposed idea or contribution
- evidence, plan, or method
- closing value

Write this spine first, even if only internally, before deciding slide count.

Also keep a lightweight running log of:

- user-stated preferences about tone, density, emphasis, and visuals
- user selections made through built-in question tools
- what was debated or reframed during discussion
- why the final speaking spine was chosen over alternatives

### 3. Negotiate scope with the user

Before producing the final blueprint, discuss and align on:

- target slide count or range
- sections to emphasize
- sections to compress or omit
- whether to reserve pages for figures, tables, timelines, or Q and A

When the report is long, explicitly warn that not all source text should appear on slides.

When the user changes emphasis during discussion, record both the original direction and the adjusted direction so the final memory file preserves the reasoning path.
If the user has not yet committed to tradeoffs, use another structured choice round instead of proceeding with implicit assumptions.

### 4. Draft the slide map

Create a provisional slide map with one-line purposes for each slide. Keep it compact and easy to review.

Good pattern:
- Slide 1: topic, positioning, talk promise
- Slide 2: why this problem matters now
- Slide 3: current methods and their limitations
- Slide 4: core research question
- Slide 5: proposed framework

Before locking the map, ask the user to choose among plausible structural directions when there is more than one defensible storyline. Good examples:

- more context-first vs more contribution-first opening
- more evidence-heavy vs more plan-heavy middle section
- more formal committee tone vs more intuitive explanation tone

Ask for correction when the structure is high-stakes or ambiguous. Otherwise proceed.

### 5. Expand into the DSL blueprint

After the slide map is acceptable, generate the final markdown blueprint using the DSL reference. Every slide must include the required fields.

After the blueprint is complete, generate the two mandatory companion markdown files:

- a discussion memory file using the companion template in the DSL reference
- a speaking aid file using the companion template in the DSL reference

## Slide Density Rules

Apply these rules strictly.

- Title slide: 1 title, 1 subtitle, optional identity line
- Standard content slide: 1 title plus either 3 to 5 bullets or 1 to 2 short paragraphs
- Comparison slide: 2 to 4 contrast rows or columns, never dense prose on both sides
- Method slide: 3 to 6 pipeline steps max
- Table slide: one compact table only, at most 5 columns and 6 data rows unless the table is purely conceptual
- Figure slide: one dominant figure or image, optional 2 to 3 annotations
- Timeline slide: 4 to 6 milestones max
- Summary slide: 3 takeaways max

Hard bans:
- no full paragraphs copied from the report
- no bullet lists longer than 6 items
- no more than 2 simultaneous visual focal points unless the slide is explicitly comparative
- no unexplained jargon wall

## Visual Design Rules

Specify visual logic even in markdown.

- State the main focal area: left, center, right, top band, split layout, full-bleed visual, etc.
- State what should be large and what should be quiet.
- Use contrast intentionally: problem vs method, before vs after, baseline vs proposed, theory vs system, input vs output.
- Prefer simple geometric composition over decorative clutter.
- Make image roles explicit: evidence, overview, mechanism, comparison, credibility, mood, or closing impression.
- If no image exists, propose a placeholder concept such as schematic, process diagram, 2-column comparison, mini chart, or icon row.

## Images, Tables, and Charts

### Images

When the user provides images:
- map each image to a slide purpose before placing it
- mark whether it is essential or optional
- describe crop, framing, annotation, and caption intent
- avoid repeating the same image unless it serves a new argumentative role

When no images are provided:
- suggest image slots only when they improve explanation
- otherwise use text-visual hybrids such as matrix, pipeline, staged reveal, or comparison cards

### Tables

Only use tables when tabular reading is genuinely faster than prose. A table slide must explain:
- why a table is necessary
- which columns are essential
- which cell or row deserves highlight treatment

### Charts

If quantitative material exists, specify:
- chart type
- x and y semantics
- key takeaway sentence
- highlight target: peak, gap, trend, outlier, or benchmark

## Output Contract

Produce three markdown files as the final deliverable package. Use the exact section order defined in [references/slide-blueprint-dsl.md](references/slide-blueprint-dsl.md).

Required files:
- a slide blueprint markdown file
- a discussion memory markdown file
- a speaking aid markdown file

The slide blueprint must contain:
- project metadata
- audience and talk goal
- storyline summary
- slide-by-slide blueprint
- design system notes
- asset checklist
- open questions if required inputs are missing

The discussion memory file must contain:
- session context and source material summary
- user preference memory
- structured question rounds and the user's selections
- discussion timeline with major decisions and reasoning pivots
- final storytelling arc summary
- future reuse notes so the next session can quickly recover the user's preferred presentation style and the deck's argumentative flow

The speaking aid file must contain:
- a short overall delivery strategy
- per-slide speaking intent
- per-slide explanation order
- per-slide transition cues
- per-slide caution notes about what not to over-explain or what assumptions need to be made explicit

Do not output raw HTML, PPTX instructions, or generic design commentary unless the user asks for them.

## Quality Check Before Finalizing

Before delivering the markdown blueprint, verify all of the following:

- each slide has exactly one core message
- slide order forms a logical spoken progression
- on-slide text is shorter than the source report by a large margin
- visuals are specified, not hand-waved
- image and table usage is justified
- every dense section of the report has either been compressed, visualized, or intentionally removed
- the final deck can plausibly be delivered aloud without reading from the screen
- the discussion memory file captures the actual reasoning path of the collaboration rather than a generic summary
- the discussion memory file records stable user preferences that should be remembered next time
- the discussion memory file preserves the important choice points and what the user selected
- the speaking aid covers every slide in order and gives delivery logic rather than a verbatim script
- the speaking aid is consistent with the final slide blueprint rather than an earlier draft
- the user was guided through multiple short clarification rounds when the task was ambiguous enough to justify them

## Failure Modes To Avoid

- translating headings from the report directly into slides without redesigning the narrative
- producing document summaries instead of speech-oriented slides
- making every slide look structurally identical
- saying "add an image here" without defining its role
- treating layout as an afterthought
- keeping too much terminology on screen because it feels academically safe
- writing content that only works if the audience reads silently for a long time
- asking one large open-ended question and calling that "discussion"
- defaulting to free-text user input when a structured choice would have been clearer and faster

## Final Note

This skill designs the slide blueprint first, then produces the mandatory memory and speaking-aid companions so the final package preserves both the designed deck and the reasoning behind it. If the user later wants a rendered HTML deck or PPT implementation, hand off the approved markdown blueprint to another suitable workflow such as a slide-generation skill.
