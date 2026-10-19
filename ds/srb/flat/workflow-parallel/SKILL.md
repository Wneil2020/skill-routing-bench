---
name: workflow-parallel
description: "Use when Fan out independent tasks to parallel subagents, aggregate results with a defined strategy (merge, vote, defer, union), and handle conflicts. Use: covers parallel, defer, fan, vote, union"
metadata:
  holon-triggers: |
    run in parallel
    fan out
---

---
name: workflow-parallel
description: >-
  Fan out independent tasks to parallel subagents, aggregate results with a
  defined strategy (merge, vote, defer, union), and handle conflicts. Use when
  the user asks to "run in parallel", "fan out", "parallel workflow", "multiple
  perspectives", "concurrent agents", "parallel review", "병렬 실행", "동시 실행",
  or needs multiple independent analyses on the same input.
  Do NOT use for dependent tasks where order matters (use workflow-sequential).
  Do NOT use for iterative quality refinement (use workflow-eval-opt).
  Do NOT use when only 1 task exists.
metadata:
  author: thaki
  version: 1.0.0
  category: orchestration
---

# Workflow Parallel — Fan-Out/Fan-In Task Execution

Distribute independent tasks across parallel subagents, aggregate results using a defined strategy, and handle contradictions. Implements the fan-out/fan-in pattern from distributed systems.

Based on the Parallel workflow pattern from Anthropic's agent workflow patterns. Trades cost (multiple concurrent calls) for speed and separation of concerns.

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| Task list | Yes | List of independent tasks (2+) with names and instructions |
| Aggregation strategy | Yes | One of: `merge`, `vote`, `defer`, `union` |
| Conflict resolution | No | Policy for contradictory results (default: `flag`) |
| Agent config | No | Per-agent model and readonly settings (default: `fast`, `readonly: true`) |
| Shared context | No | Files or data provided to all agents |

## Workflow

### Step 1: Validate Independence

Before launching agents:

1. Verify no task depends on another task's output
2. If dependencies detected, suggest `workflow-sequential` instead and halt
3. Count tasks; if only 1, suggest direct execution and halt

### Step 2: Define Aggregation Strategy

**CRITICAL: Define this BEFORE launching agents.** Changing strategy after results arrive leads to data loss or contradictions.

| St
