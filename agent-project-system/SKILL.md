---
name: agent-project-system
description: Initialize, adopt, recover, and govern an AI-first project state document system for any project. Use when Codex must interrogate goals and constraints, scaffold project documents, keep milestones and TODOs recoverable, record acceptance evidence, and preserve failed explorations without lying about progress.
---

# Agent Project System

## Overview

Build and maintain a project state document system that lets an AI agent recover context quickly, continue work autonomously, and stay evidence-grounded over time.

This skill is for any project type: software engineering, research, literature review, data collection, crawling, report production, or mixed workflows. The goal is not only to scaffold files, but to establish a durable operating system for project intent, state, evidence, failures, and recovery.

Read [references/workflow.md](references/workflow.md) first. Read [references/document-contract.md](references/document-contract.md) before generating or revising any project document set. Read [references/runtime-governance.md](references/runtime-governance.md) before handling recovery, status updates, or autonomous continuation.

## Trigger And Scope

Use this skill when the user asks to do any of the following:

- design a reusable project documentation system for AI agents
- initialize a new project so the AI can continue autonomously later
- adopt an existing project and reconstruct its state documents
- recover a project after interruption and decide what to do next
- keep milestones, TODOs, acceptance evidence, and failed explorations synchronized
- build a project-level `AGENTS.md` contract and a linked `CLAUDE.md`
- make a project recoverable from documents instead of relying on chat history

Do not use this skill for one-off note taking, casual status summaries, or document sets that are only meant for human readers and not for agent recovery.

## Non-Negotiable Rules

1. The user's final goal, requirements, and acceptance standards are the highest-priority truth source.
2. During initialization, keep asking until all issues that require human judgment are pinned down. Do not silently assume them.
3. Once human decisions are locked, the agent may autonomously refine architecture, milestones, TODOs, and implementation paths as long as the original goal and acceptance boundaries remain intact.
4. The agent may be aggressive in exploration, but it must be truthful. No evidence means no claim of completion.
5. Failed explorations are first-class project knowledge. Do not erase them just because they did not work.
6. The project root must contain `AGENTS.md`. The root must also contain `CLAUDE.md` as a hard link to the same content when the filesystem supports it.
7. The primary recovery path is always `AGENTS.md` -> `project-index.md` -> active items -> recent run log.
8. Use globally unique item IDs across the project document set. Document section numbers may exist, but they must not replace item IDs.
9. A TODO is not truly closed until implementation, verification, and document bookkeeping are all complete.
10. When the user language is Chinese, project documents may be Chinese, but code comments and `print` output in scripts must remain English.

## Core Document Model

The default document system has these required roles:

- project-root `AGENTS.md`: project contract, recovery entrypoint, update obligations, escalation rules, and document layout
- project-root `CLAUDE.md`: hard link to `AGENTS.md`
- state `project-index.md`: current truth, active workstreams, current top next action, blockers, recent changes
- state `requirements.md`: human-provided goals, requirements, acceptance criteria, non-goals
- state `change-decisions.md`: later human decisions that revise interpretation without rewriting the original requirements
- state `architecture-milestones.md`: current architecture, workstreams, milestone plan, and milestone acceptance
- state `todo.md`: backlog, active, blocked, done, verified, and abandoned items
- state `acceptance-report.md`: per-item evidence and pass or fail reporting
- state `lessons-learned.md`: failed attempts, traps, conclusions, and retry conditions
- state `run-log.md`: lightweight chronological record of what the agent actually did recently

Read [references/document-contract.md](references/document-contract.md) for the item model, state machine, and file responsibilities.

## Workflow

### 1. Initialization For A New Project

Use this path when the project does not yet have a state-document system.

1. Interrogate the user until all human-owned decisions are explicit.
2. Translate the conversation into the document system rather than dumping a raw transcript.
3. Preserve the user's intent faithfully in `requirements.md`.
4. Create the project root `AGENTS.md` and linked `CLAUDE.md`.
5. Create the state directory and seed the rest of the documents.
6. Populate the first workstreams, milestones, TODOs, evidence expectations, and next action.

When there are still unresolved questions that only the user can answer, do not pretend initialization is finished.

### 2. Adoption For An Existing Project

Use this path when the repository or folder already contains code, notes, outputs, or partial documentation.

1. Audit the existing project first.
2. Infer the current architecture, active workstreams, unfinished work, completed work, and likely acceptance signals.
3. Ask only the questions that cannot be discovered from the project itself and still matter to human intent.
4. Build the document system around the discovered reality.
5. If existing docs are fragmented or low quality, reconstruct a cleaner system rather than preserving chaos.

The default adoption posture is: inspect first, then map, then rebuild the document system if needed.

### 3. Recovery

On project resume:

1. Read the root `AGENTS.md`.
2. Read `project-index.md`.
3. Read the active items referenced from the index.
4. Read the newest relevant entries in `run-log.md`.
5. Only then dive deeper into architecture, acceptance, or lessons as needed.

Do not re-read the whole project by default if the index and recent log are sufficient.

### 4. Runtime Maintenance

This skill should intervene lightly during execution, not dominate every turn.

Update the project state documents when one of these happens:

- a new TODO is created
- an item changes state
- a blocker appears or clears
- a milestone is reached or re-planned
- evidence is produced
- an exploration fails or is abandoned
- an autonomous work session ends

### 5. Truthfulness Guardrail

Every claim that something is complete, verified, or meets a target must be backed by evidence that can be pointed to. If evidence does not exist yet, mark the status as unverified, in progress, or hypothesis.

## Item IDs And State

Use typed item IDs such as:

- `OBJ-001`
- `REQ-001`
- `AC-001`
- `WS-001`
- `MS-001`
- `TD-001`
- `RSK-001`
- `EXP-001`
- `EV-001`
- `CD-001`

Default TODO and milestone states:

- `backlog`
- `ready`
- `doing`
- `blocked`
- `done`
- `verified`
- `abandoned`

Every state transition should have a reason. Every abandoned item should explain why it was abandoned and what would justify retrying it later.

## Scripts And Templates

Use the bundled helpers when possible:

- `scripts/init_project_system.py`: scaffold the document set, write the project root contract, and create the `CLAUDE.md` hard link
- `scripts/allocate_item_id.py`: allocate the next typed project item ID by scanning the existing document set
- `scripts/validate_project_system.py`: validate the presence of required files, link integrity, ID hygiene, and minimum index invariants

Use the Markdown templates under `assets/templates/` as the deterministic baseline for new projects or adoptions.

## Output Standard

When creating or repairing a project document system, the default deliverable is a working document set, not just a prose recommendation.

At minimum, the result should include:

- a project root `AGENTS.md`
- a project root `CLAUDE.md` linked to it
- the state directory with the required documents
- initial content accurate enough that the next recovery can continue from documents alone

## Failure Modes To Avoid

- writing a shallow template pack with no operational rules
- letting requirements drift because architecture changed
- treating TODO completion as sufficient without evidence and bookkeeping
- hiding failed explorations or blockers to make progress look cleaner
- forcing humans to restate decisions that the documents should already preserve
- rebuilding the whole mental model from chat history when the project should have been recoverable from files

## References

- [references/workflow.md](references/workflow.md)
- [references/document-contract.md](references/document-contract.md)
- [references/runtime-governance.md](references/runtime-governance.md)
