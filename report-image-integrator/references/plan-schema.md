# Plan Schema

Create a JSON object with this shape:

```json
{
  "figure_dir_name": "report-figures",
  "entries": [
    {
      "source_image": "E:/path/raw/loss.png",
      "target_filename": "fig-01-training-loss-curve.png",
      "caption": "Training loss curve",
      "label": "fig:training-loss-curve",
      "insert_after_text": "The model uses a scheduled learning-rate decay to improve convergence stability.",
      "pre_text": "As shown in @fig:training-loss-curve, the training loss drops quickly at first and then stabilizes.",
      "post_text": "This trend indicates that the current optimization setup converges in a stable way."
    }
  ]
}
```

## Required Fields

- `entries`: array of accepted figures
- `source_image`: original image path
- `target_filename`: renamed filename to create inside the figure directory
- `caption`: figure title used in Markdown image syntax
- `label`: figure label used for cross-reference

## Anchor Fields

Each entry must include exactly one of:

- `insert_after_text`
- `insert_before_text`
- `replace_text`

The anchor text must match the Markdown file exactly once.

## Optional Fields

- `figure_dir_name`: sibling directory name to create beside the Markdown file. Default is `<markdown-stem>-figures`.
- `pre_text`: text inserted immediately before the image block
- `post_text`: text inserted immediately after the image block

## Generated Markdown Block

The script generates this block form:

```markdown
{pre_text}

![{caption}]({figure_dir_name}/{target_filename}){{#{label}}}

{post_text}
```

Empty `pre_text` or `post_text` values are omitted cleanly.
