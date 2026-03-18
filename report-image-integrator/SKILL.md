---
name: report-image-integrator
description: Integrate image files into an existing Markdown report by inspecting the actual image content, selecting only the figures that strengthen the report, inserting them at coherent positions, adding captions and cross-references, and renaming the image files into a clean structure. Use when Codex receives a report `.md` plus one or more candidate images and must update the original Markdown in place without rewriting unrelated prose.
---

# Report Image Integrator

Integrate user-supplied images into an existing report Markdown file without turning the task into a rewrite. Inspect each image visually, decide whether it belongs in the document, insert only the useful ones at logically justified positions, add figure captions and cross-references, and rename the image files into a stable structure under the report directory.

Read [references/workflow.md](references/workflow.md) first. Use [scripts/apply_image_plan.py](scripts/apply_image_plan.py) after deciding the image insertion plan.

## Non-Negotiable Rules

1. Inspect every candidate image by its visual content. Do not decide based only on the filename, surrounding directory name, or user summary.
2. Preserve the report's existing wording except where figure integration requires local edits:
   - add a lead-in sentence before a figure
   - add a follow-up sentence that references the figure
   - add or adjust a nearby sentence so the cross-reference reads naturally
3. Do not rewrite unrelated paragraphs, reorder sections, or normalize style globally.
4. Exclude images that do not materially help the report, are redundant, are too low quality to explain safely, or conflict with the nearby text.
5. Give every inserted image a descriptive caption grounded in what the image actually shows.
6. Use explicit figure labels and body-text cross-references. Prefer Pandoc-style labels such as `@fig:training-loss-curve`.
7. Rename accepted image files into a single structured figure directory next to the Markdown file. Use deterministic, caption-derived names.
8. Overwrite the original Markdown file only after the insertion plan is internally consistent.

## Workflow

### 1. Build The Working Set

Identify:

- the target Markdown report path
- all candidate image paths
- the report language
- whether the report already contains any figures or figure-reference conventions

If the user gives many images, make a compact inventory table for yourself only:

- source file
- visual summary
- likely section
- keep or drop
- reason

### 2. Inspect Images Before Planning

Open each image and extract the content that matters for report writing:

- chart type, axes, legends, and notable trends
- screenshots, interface states, or pipeline stages
- diagrams, modules, arrows, and labeled components
- tables or metric summaries visible inside the image
- whether the image is blurry, cropped badly, duplicated, or unreadable

Do not infer scientific meaning that the image itself does not support.

### 3. Decide Which Images To Keep

Keep an image only when at least one of these is true:

- it provides evidence for a claim already present in the report
- it clarifies a method, workflow, architecture, or experiment setup already discussed
- it summarizes results better than prose alone
- it prevents a nearby paragraph from being abstract or hard to follow

Drop an image when:

- it repeats another stronger image
- it introduces content the report never explains
- it is mostly decorative
- its labels are too unreadable to describe responsibly

### 4. Choose Insertion Points Conservatively

Insert figures where the image is naturally introduced by existing content. Preferred placement order:

1. immediately after the paragraph that first creates the need for the figure
2. immediately after a subsection heading if the figure frames the whole subsection
3. immediately before a paragraph that interprets the visual evidence

Avoid placing a figure:

- before the concept it visualizes is introduced
- far away from the paragraph that references it
- inside unrelated lists or tables

When integrating a figure, make only the smallest text changes required for coherence:

- add one short lead-in sentence before the figure if no sentence currently introduces it
- add one short interpretive sentence after the figure if needed
- keep the surrounding paragraph structure intact

### 5. Use Stable Figure Syntax

Default figure block:

```markdown
As shown in @fig:method-pipeline, the system contains three stages: preprocessing, feature extraction, and output generation.

![Method pipeline](report-figures/fig-01-method-pipeline.png){#fig:method-pipeline}

This figure makes the module boundaries and data flow explicit.
```

Requirements:

- caption must match visible content
- label must be short, semantic, and unique
- nearby prose must mention the figure explicitly
- image path must point to the renamed file, not the original source path

If the report already uses another figure-reference convention, preserve that convention when it remains deterministic and renderable.

### 6. Execute With The Script

After deciding which images to insert, create a JSON plan and run:

```powershell
python scripts/apply_image_plan.py `
  --markdown "E:\path\report.md" `
  --plan "E:\path\image-plan.json"
```

The script:

- renames accepted images into a single directory beside the Markdown file
- inserts or replaces figure blocks at planned anchors
- overwrites the original Markdown file

Read [references/plan-schema.md](references/plan-schema.md) for the plan format.

### 7. Final Audit

Check all of the following before finishing:

- every kept image was visually inspected
- every inserted figure is referenced in nearby text
- every figure reference points to an existing label
- renamed image files are present in the target figure directory
- unrelated report text is unchanged
- Markdown still reads as a continuous report rather than a patchwork

## Output Standard

Default deliverable:

- the original Markdown file updated in place
- a sibling figure directory containing the renamed accepted images
- captions, labels, and body-text references that are consistent with the inserted figures

If some images are rejected, state which ones were excluded and why.

## Resources

- [references/workflow.md](references/workflow.md)
- [references/plan-schema.md](references/plan-schema.md)
- [scripts/apply_image_plan.py](scripts/apply_image_plan.py)
