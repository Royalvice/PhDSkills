---
name: report-to-flowchart-prompt
description: Turn a report, proposal, thesis chapter, research plan, or other long-form academic text into a highly detailed image-generation prompt for a flat research-overview flowchart. Use when Codex needs to read the source text, extract the internal logical structure between background, objectives, methods, modules, stages, inputs, outputs, and expected results, then produce a Nano Banana compatible prompt that tightly controls layout, wording, aspect ratio, palette, typography, and diagram style. Especially useful for Chinese academic materials such as doctoral proposals, NSFC-style research overview figures, technical roadmaps, and research framework diagrams.
---

# Report To Flowchart Prompt

## Overview

Convert report text into a flowchart-image prompt that preserves the source logic rather than paraphrasing it loosely. Produce prompts for clean, blue-white, flat, research-overview diagrams with solid-color backgrounds, explicit text selection, and no 3D or decorative noise.

Read [references/prompt-spec.md](references/prompt-spec.md) when writing the final prompt. Read [references/relation-patterns.md](references/relation-patterns.md) when the source text is dense, nonlinear, or spans multiple research modules.

## Workflow

### 1. Read the source as a logic system

Identify the report's real structure before drafting the image prompt:

- Research background or motivation
- Core problem or scientific question
- Overall objective
- Research modules or work packages
- Methods, data, models, or experiments attached to each module
- Sequence, dependency, branching, convergence, and feedback relations
- Expected outputs, metrics, or application targets

Do not flatten the report into a generic top-down diagram if the source implies parallel modules, staged iteration, or layered abstraction.

### 2. Extract only text that can appear inside the figure

Select diagram text directly from the report whenever possible. Compress only for fit, clarity, or visual balance.

- Keep technical terminology faithful to the source.
- Preserve distinctions between objectives, methods, and results.
- Do not invent claims, modules, or evaluation targets not grounded in the report.
- Prefer short noun phrases or verb-object phrases suitable for boxes and labels.
- When shortening, keep the same meaning and technical scope.

If the source uses Chinese, keep the figure text in Chinese unless the user asks for English.

### 3. Build the logic map before writing the image prompt

Create an internal representation of:

- Nodes: what boxes or labeled regions exist
- Edges: what relationship each arrow expresses
- Groups: what nodes belong to the same stage or module
- Reading order: how a reviewer should understand the diagram in 5 to 10 seconds

Use the relation patterns in [references/relation-patterns.md](references/relation-patterns.md) to classify the structure. If several patterns coexist, choose one dominant reading path and subordinate the rest visually.

### 4. Choose the visual composition deliberately

Default to a landscape research-overview layout, because this matches proposal-style diagrams better than a poster or infographic layout.

- Prefer `4:3` landscape when the structure has 3 to 5 major stages.
- Prefer `3:2` landscape when the diagram has more horizontal breadth.
- Prefer `16:9` only when the user explicitly asks for a presentation-like canvas.

The figure must look like a polished grant-application overview chart:

- Minimal
- Flat
- Clean
- Structured
- Review-friendly
- Design-aware but not decorative

### 5. Write a high-control image prompt

The final answer should prioritize a single detailed prompt that an image model can follow with minimal ambiguity. The prompt must explicitly control:

- Aspect ratio and orientation
- Background color
- Overall visual style
- Palette, contrast, and accent usage
- Grid or spatial composition
- Exact box hierarchy
- Arrow directions and relation semantics
- Figure text content and language
- Typography style
- Restrictions against 3D, gradients that imply depth, shadows, mockup elements, and scene-like rendering

Use the output structure in [references/prompt-spec.md](references/prompt-spec.md).

## Output Rules

- Output one final production-ready prompt by default.
- Include a short `Logic skeleton` section before the prompt only when the source material is complex enough that the user benefits from seeing the extracted structure.
- Make the prompt concrete enough that another model could reconstruct the whole diagram without seeing the source report.
- Treat text fidelity as a hard constraint, not an optional suggestion.
- When box text is long, instruct the image model to keep the labels concise, aligned, and legible rather than reducing the font to an unreadable size.

## Style Guardrails

- Prefer white or very light solid backgrounds.
- Use blue-white as the dominant palette, with restrained cyan or slate-blue accents only if needed.
- Keep the diagram flat and editorial.
- Avoid 3D, bevels, glassmorphism, dramatic shadows, photographic elements, and textured paper.
- Avoid dark backgrounds unless the user explicitly requests one.
- Avoid poster, game UI, sci-fi HUD, and isometric aesthetics.
- Avoid cartoon icons unless the source explicitly calls for them.

## Failure Modes To Avoid

- Copying the report into the image prompt without restructuring it
- Producing a generic "technology roadmap" that loses the report's actual causal logic
- Mixing objectives, methods, and outputs in the same visual level
- Using vague wording like "some arrows connect the modules"
- Leaving text choice unspecified
- Asking for a beautiful diagram without constraining layout, spacing, and hierarchy
- Introducing colorful infographic styling that weakens academic credibility
