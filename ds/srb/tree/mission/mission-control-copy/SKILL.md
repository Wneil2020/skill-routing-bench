---
name: mission-control-copy
description: "Use when Orchestrate multi-skill autonomous workflows — decompose high-level goals into sub-tasks, delegate to specialist skills via subagents: covers mission, control copy, 감사, 리뷰, delegate"
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
  prep, quality audit, incident response, or any task spanning multiple domains.
  Do NOT use for single-domain tasks that map to one specific skill. Korean
  triggers: "감사", "리뷰", "워크플로우", "릴리즈".
metadata:
  version: "1.0.0"
  category: "orchestrator"
  author: "thaki"
---
# Mission Control — Agent Orchestrator

The meta-skill that coordinates all other skills. Decomposes high-level goals into sub-tasks, delegates to specialist skills via the Task tool, aggregates results, and tracks progress.

## When to Use

- Any task that spans 2+ specialist domains
- Workflow commands: `/full-quality-audit`, `/feature-pipeline`, `/release-prep`, `/incident-response`, `/dependency-sweep`, `/i18n-check`
- When the user says "do a full review", "prepare for release", "check everything"
- Complex goals that need parallel investigation

## Core Principles

1. **Decompose first**: Break the goal into concrete sub-tasks before acting
2. **Delegate to specialists**: Each sub-task maps to a specific skill
3. **Parallelize**: Use up to 4 Task subagents concurrently
4. **Track progress**: Update `tasks/todo.md` with checkable items
5. **Aggregate results**: Combine outputs into a unified report
6. **Handle failures**: Retry or fall back gracefully

## Skill Registry

22 specialist skills organized into Execution (7), Review (10), and Generation (2) categories, plus this orchestrator. For the full registry and goal-to-skill mapping, see [references/skill-registry.md](references/skill-registry.md).

## Orchestration Protocol

### Step 1: Analyze Goal

Read the user's request and identify:
- **Primary objective**: What needs to be achieved
- **Scope**: Which parts of the codebase are affected
- **Constraints**: Time, safety
