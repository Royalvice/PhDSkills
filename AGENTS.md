# AGENTS.md

This repository stores Codex skills for PhD-oriented workflows.
These rules apply to the repository root and all nested skill directories.

## Mission

- Keep `PhDSkills` organized as a long-lived, scalable skill library for academic and research work.
- Prefer reusable workflows, deterministic scripts, and explicit repository conventions.
- Design new skills so they can coexist cleanly with future skills.

## Repository Rules

- Every top-level skill directory must contain a `SKILL.md` entrypoint.
- Every new skill added under the repository root must be reflected in both `README.md` and `README.zh-CN.md`.
- The `Skill Catalog` sections in both READMEs must stay synchronized with the actual top-level skill directories.
- Do not remove a skill from the README files unless the corresponding directory is removed from the repository.
- Do not create undocumented top-level skill folders.
- Keep repository-wide documentation generic enough for future growth; avoid overfitting the root README to a single current skill.

## Skill Layout

Use this layout unless a skill has a justified reason to differ:

```text
skill-name/
├─ SKILL.md
├─ scripts/
├─ assets/
├─ references/
└─ agents/
```

Rules:

- `SKILL.md` is required.
- `scripts/` is for runnable automation and deterministic helpers.
- `assets/` is for templates, catalogs, styles, and static support files.
- `references/` is for workflow notes and implementation guidance.
- `agents/` is for tool-specific or provider-specific configuration files.

## Documentation Sync Policy

When adding or changing a skill:

1. Update `README.md`.
2. Update `README.zh-CN.md`.
3. Confirm the skill name, purpose, and status are represented consistently.
4. Keep examples and repository structure diagrams current.

Documentation sync is mandatory, not optional.

## Authoring Conventions

- Prefer concise, explicit descriptions over vague marketing language.
- Keep workflows deterministic first and editorial or LLM-driven behavior second.
- Do not silently rewrite user content unless the skill explicitly permits it.
- Use ASCII by default in code and configuration unless a file already requires Unicode.
- Keep filenames predictable and stable.

## Git and Maintenance

- Keep commits focused and repository-scoped.
- Avoid unrelated formatting churn when modifying a skill.
- Before publishing, verify that new files are discoverable from the repository root documentation.
- If a new top-level convention is introduced, document it here in `AGENTS.md`.

## Review Checklist

- Is every top-level skill documented in both READMEs?
- Does every skill have a `SKILL.md`?
- Does the repository structure shown in the README still match reality?
- Are new support files placed in the right subdirectories?
- Do repository rules still make sense as the skill library grows?
