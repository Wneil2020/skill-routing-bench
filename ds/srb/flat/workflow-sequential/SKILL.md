---
name: workflow-sequential
description: "Use when Execute a list of tasks in dependency order with checkpoints, error recovery, and conditional skipping. Use when the user: covers sequential, ordered, skipping, simultaneously, conditional"
metadata:
  holon-triggers: |
    run tasks in order
    sequential pipeline
---

---
name: workflow-sequential
description: >-
  Execute a list of tasks in dependency order with checkpoints, error recovery,
  and conditional skipping. Use when the user asks to "run tasks in order",
  "sequential pipeline", "chain these steps", "execute in sequence",
  "sequential workflow", "순차 실행", "파이프라인 실행", or needs to orchestrate
  dependent tasks where step B requires step A's output.
  Do NOT use for independent tasks that can run simultaneously (use
  workflow-parallel). Do NOT use for iterative quality refinement (use
  workflow-eval-opt). Do NOT use for single-task execution.
metadata:
  author: thaki
  version: 1.0.0
  category: orchestration
---

# Workflow Sequential — Dependency-Ordered Task Execution

Execute tasks in dependency order with checkpoints between stages. Each task receives the output of its predecessor and passes its output to the next. Handles error recovery, conditional skipping, and staged commits.

Based on the Sequential workflow pattern from Anthropic's agent workflow patterns. Trade latency for accuracy by letting each agent focus on a specific subtask instead of handling everything at once.

## Inputs

The user provides (or the orchestrating skill defines):

| Input | Required | Description |
|-------|----------|-------------|
| Task list | Yes | Ordered list of tasks with names and instructions |
| Dependencies | No | Explicit dependency graph (default: linear chain A->B->C) |
| Skip conditions | No | Per-task conditions to skip (flags, data absence) |
| Error policy | No | Per-task: `retry`, `skip-warn`, or `halt` (default: `halt`) |
| Checkpoint | No | Whether to commit/verify after each task (default: verify only) |

## Workflow

### Step 1: Validate Task Graph

Parse the task list and dependency declarations.

1. Build a directed acyclic graph (DAG) of dependencies
2. Detect cycles — if found, report the cycle and halt
3. Topologically sort into execution order
4. If no explicit dependencies, assume linear chain: Task 1 -
