---
name: full-stack-planner
description: "Use when Generate comprehensive multi-phase implementation plans that map a high-level goal to the project's entire skill ecosystem. Produces: covers full, stack, planner, assignments, concurrency"
metadata:
  holon-triggers: |
    create a full implementation plan
    plan a full-stack pipeline
---

---
name: full-stack-planner
description: >-
  Generate comprehensive multi-phase implementation plans that map a high-level
  goal to the project's entire skill ecosystem. Produces 5-phase pipeline plans
  with skill assignments, mermaid diagrams, concurrency strategies, and
  structured outputs via the CreatePlan tool. Use when the user runs
  /full-stack-plan, asks to "create a full implementation plan", "plan a
  full-stack pipeline", "generate a multi-phase plan", "전체 구현 계획",
  "풀스택 파이프라인 계획", or needs an enterprise-grade plan spanning 20-50
  skills across survey, analysis, research, implementation, and testing phases.
  Do NOT use for simple prompt optimization (use plans), runtime workflow
  execution (use mission-control), or developer-focused task lists (use
  sp-writing-plans).
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "planning"
---
# Full-Stack Planner — Multi-Phase Skill Pipeline Generator

Generates comprehensive implementation plans that decompose a high-level goal into 5 standard phases, assign skills to each sub-step, and produce a structured plan via the CreatePlan tool. Each plan includes a mermaid execution flow, concurrency strategy, and skill count summary.

## Workflow

Execute these 6 steps in order.

### Step 1: Receive Goal

Accept the user's high-level implementation goal. This may come from:
- `/full-stack-plan` command `$ARGUMENTS`
- Direct user message
- A feature request, audit scope, or migration brief

If the goal is empty or too vague, ask one clarifying question. Store the original goal text verbatim.

Parse options if present:
- `--phases <list>` — include only specified phases (comma-separated: 1,2,3,4,5)
- `--scope <mode>` — `survey-only` (Phase 1), `plan-only` (Phases 1-3), `full` (default, all 5)
- `--execute` — after plan approval, delegate to mission-control

### Step 2: Survey Project Context

Read current project state to inform phase planning:

1. `README.md` — feature list, tech stack, project overview

