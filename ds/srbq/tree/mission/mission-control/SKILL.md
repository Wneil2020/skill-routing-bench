---
name: mission-control
description: "Use when Orchestrate multi-skill autonomous workflows — decompose high-level goals into sub-tasks, delegate to specialist skills via subagents, aggregate: covers mission, control, 감사, 리뷰, alone"
metadata:
  holon-triggers: |
    a full review
    release prep
---

---
name: mission-control
description: >-
  Orchestrate multi-skill autonomous workflows — decompose high-level goals
  into sub-tasks, delegate to specialist skills via subagents, aggregate
  results, and track progress. Use when the user asks for a full review, release
  prep, quality audit, incident response, or any task spanning multiple domains,
  or invokes workflow commands like /full-quality-audit, /feature-pipeline. Do
  NOT use for single-domain tasks that one specific skill can handle alone.
  Korean triggers: "감사", "리뷰", "파이프라인", "워크플로우".
metadata:
  author: "thaki"
  version: "1.1.0"
  category: "execution"
---
# Mission Control — Agent Orchestrator

The meta-skill that coordinates all other skills. Decomposes high-level goals into sub-tasks, delegates to specialist skills via the Task tool, aggregates results, and tracks progress.

## Core Principles

1. **Decompose first**: Break the goal into concrete sub-tasks before acting
2. **Right-size sub-tasks**: Each sub-task should be completable in one agent turn (3-5 files, 15-30 min). If larger, decompose further. If smaller, combine with related work.
3. **Delegate to specialists**: Each sub-task maps to a specific skill
4. **Parallelize**: Use up to 4 Task subagents concurrently
5. **Observe and verify**: After each sub-task completes, verify output against the expected blueprint before proceeding to the next
6. **Track progress**: Update `tasks/todo.md` with checkable items
7. **Aggregate results**: Combine outputs into a unified report
8. **Handle failures with classification**: When a sub-task fails, classify the failure before retrying (see Failure Classification below)

## Skill Registry

Currently available skills: `cursor-sync`, `deep-review`, `design-architect`, `diagnose`, `domain-commit`, `intent-alignment-tracker`, `semantic-guard`, `ship`, `simplify`, `skill-composer`, `skill-optimizer`, `test-suite`, `transcribee`, `ui-suite`, `video-compress`, `visual-explainer`, `workflow-miner`, `x-to-sl
