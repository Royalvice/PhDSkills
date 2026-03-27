# Prompt Spec

Use this file when generating the final image prompt.

## Objective

Produce a single prompt that instructs an image model to create a proposal-style research overview flowchart from report text. The prompt should read like a production specification, not a casual art prompt.

## Required Prompt Blocks

Write the final prompt in this order:

1. `Task`
2. `Canvas`
3. `Overall style`
4. `Layout structure`
5. `Nodes and text`
6. `Connections`
7. `Color and typography`
8. `Negative constraints`

## Block Guidance

### 1. Task

State the exact deliverable in one sentence.

Example shape:

- Create a clean academic research-overview flowchart image in Chinese, suitable for a National Natural Science Foundation style proposal summary figure.

### 2. Canvas

Specify:

- landscape orientation
- exact aspect ratio
- high resolution
- solid-color background
- generous margins

Default wording pattern:

- landscape composition, aspect ratio 4:3, high-resolution editorial diagram, pure white background, ample margins, centered composition

### 3. Overall style

Specify:

- flat vector-like flowchart
- academic, minimal, professional
- no 3D
- no scene depth
- no illustrative storytelling

Default wording pattern:

- flat 2D proposal-style flowchart, minimal and precise, clean editorial diagram, strong information hierarchy, polished but restrained, no 3D depth, no photorealism

### 4. Layout structure

Describe the global composition as if placing objects manually.

Include:

- number of tiers, columns, or rows
- dominant reading direction
- central grouping logic
- whether there are parallel modules or convergence stages
- whether the title is embedded or omitted

Example directives:

- top row for research background and core scientific problem
- middle row for three parallel research modules
- lower row for convergence, validation, and expected outcomes
- arrows should flow from left to right with secondary top-to-bottom dependencies

### 5. Nodes and text

Specify every major text-bearing region.

For each node or grouped block, include:

- label type
- exact or near-exact Chinese text
- relative size
- shape style
- whether it is a standalone box, grouped container, or footer result block

Text selection rules:

- Prefer source wording
- Shorten only for fit
- Keep terminology consistent
- Do not add claims absent from the report

### 6. Connections

Describe arrows semantically, not only visually.

Examples:

- solid arrows for main research progression
- thinner arrows for support relations
- converging arrows into the integrated verification module
- feedback arrow from evaluation to model refinement

### 7. Color and typography

Default palette:

- white background
- deep academic blue for headers and key boxes
- medium blue for secondary modules
- pale blue fills for grouped regions
- dark gray or near-black text

Typography rules:

- modern Chinese sans-serif feel
- crisp labels
- moderate font weight
- no handwritten or playful type
- text must remain legible at report-page viewing size

### 8. Negative constraints

Always include strict exclusions:

- no 3D effects
- no gradients that imply volume
- no glossy buttons
- no drop shadows
- no mockup frame
- no office desk background
- no decorative icons unless explicitly needed
- no dark theme
- no chartjunk

## Prompt Template

Use this template and replace the placeholders with report-grounded content:

```text
Create a clean academic research-overview flowchart image in [language], suitable for a National Natural Science Foundation style proposal summary figure.

Canvas: landscape composition, aspect ratio [4:3 or 3:2], high resolution, pure [white/light blue] solid background, ample margins, balanced spacing, print-friendly.

Overall style: flat 2D vector-like flowchart, minimal, rigorous, professional, research-proposal aesthetic, strong hierarchy, clean alignment, subtle design sense, no 3D depth, no photorealism, no scene rendering.

Layout structure: [describe the global arrangement in detail, including rows, columns, grouping blocks, main reading direction, and visual emphasis].

Nodes and text:
- [node 1 position and exact text]
- [node 2 position and exact text]
- [node 3 position and exact text]
- ...

Connections:
- [arrow relation 1]
- [arrow relation 2]
- [feedback or convergence relation]

Color and typography: dominant blue-white palette, deep blue headers, medium blue module boxes, pale blue grouped backgrounds, dark gray text, modern sans-serif Chinese typography, crisp labels, uniform stroke width, restrained accent color usage.

Negative constraints: no 3D, no extrusion, no bevels, no glossy UI, no dramatic shadows, no perspective distortion, no photographic elements, no textured background, no dark background, no decorative clutter, no isometric view.
```

## Quality Bar

The finished prompt should let a downstream image model answer all of these without guessing:

- What is the canvas shape?
- What is the reading order?
- What boxes exist?
- What text goes into each box?
- Which arrows are primary and which are secondary?
- What is the palette?
- What must be avoided?
