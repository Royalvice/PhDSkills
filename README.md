# PhDSkills

[![Stars](https://img.shields.io/github/stars/Royalvice/PhDSkills?style=for-the-badge&logo=github)](https://github.com/Royalvice/PhDSkills/stargazers)
[![Visitors](https://komarev.com/ghpvc/?username=Royalvice&repo=PhDSkills&style=for-the-badge)](https://github.com/Royalvice/PhDSkills)
[![Skills](https://img.shields.io/badge/skills-growing-0ea5e9?style=for-the-badge&logo=bookstack&logoColor=white)](#skill-catalog)
[![Status](https://img.shields.io/badge/status-active-22c55e?style=for-the-badge&logo=vercel&logoColor=white)](#)

> Codex skills for PhD workflows: writing, publishing, literature handling, research operations, and academic productivity.

English | [简体中文](./README.zh-CN.md)

## Why This Repository

`PhDSkills` is a curated skill library for Codex users working in research-heavy environments.
It is designed for PhD students, supervisors, research assistants, and academic teams who want reusable, automation-friendly workflows instead of ad hoc prompts.

The repository is structured to scale from a small personal toolbox into a long-lived skills collection covering the full academic lifecycle.

## What It Provides

- `Writing workflows` for academic markdown, manuscripts, thesis drafts, proposals, reports, and revision cycles
- `Publishing workflows` for DOCX, PDF, HTML, Quarto, Pandoc, templates, references, and validation
- `Research operations` for reproducible routines, environment checks, project setup, and task automation
- `Knowledge workflows` for citations, bibliographies, source organization, note pipelines, and reading support
- `Future-ready structure` for adding many more domain-specific skills without changing the repository conventions

## Repository Structure

```text
PhDSkills/
├─ AGENTS.md
├─ README.md
├─ README.zh-CN.md
├─ .gitignore
├─ md2all/
│  ├─ SKILL.md
│  ├─ scripts/
│  ├─ assets/
│  ├─ references/
│  └─ agents/
├─ ai-research-landscape/
│  ├─ SKILL.md
│  ├─ scripts/
│  ├─ assets/
│  ├─ references/
│  └─ agents/
└─ <future-skill>/
   ├─ SKILL.md
   ├─ scripts/
   ├─ assets/
   ├─ references/
   └─ agents/
```

## Skill Catalog

This section is intentionally designed to grow.

| Skill | Status | Focus |
| --- | --- | --- |
| `md2all` | Available | Markdown and Quarto publishing workflows |
| `ai-research-landscape` | Available | Verified AI literature landscapes and curated bibliographies |
| `future-skill` | Reserved | Add new skills here as the library expands |

## Design Principles

- `Deterministic first`: prefer scripts, assets, and explicit workflows over fuzzy behavior
- `Conservative by default`: avoid unnecessary rewriting or hidden changes
- `Composable`: each skill should be usable independently and alongside other skills
- `Portable`: workflows should remain practical across machines and environments
- `Maintainable`: repository metadata and documentation must stay synchronized with the actual skill inventory

## Adding New Skills

Each skill should live in its own top-level directory and include a `SKILL.md` as the entrypoint.

Recommended layout:

```text
new-skill/
├─ SKILL.md
├─ scripts/
├─ assets/
├─ references/
└─ agents/
```

When a new skill is added:

1. Create the skill directory and `SKILL.md`.
2. Add or update supporting `scripts`, `assets`, `references`, and `agents` folders as needed.
3. Update the `Skill Catalog` section in `README.md`.
4. Update the mirrored catalog in `README.zh-CN.md`.
5. Keep repository rules in `AGENTS.md` aligned with the change.

## Intended Use Cases

- building a durable personal Codex skill library for doctoral work
- sharing reusable academic workflows across a lab or research group
- standardizing document conversion and publishing routines
- organizing future skills for thesis, papers, reviews, data work, and academic admin

## Contributing

Contributions should preserve the repository conventions in [`AGENTS.md`](./AGENTS.md).
If you add a new skill, documentation sync is not optional.

## Roadmap

- expand beyond publishing into broader PhD research workflows
- introduce more reusable templates and domain-specific utilities
- improve skill discoverability, validation, and onboarding

## License

Add a license that matches your intended sharing model before wider distribution.
