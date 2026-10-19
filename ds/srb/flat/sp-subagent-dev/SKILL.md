---
name: sp-subagent-dev
description: "Use when Use when executing implementation plans with independent tasks in the current session. Korean triggers, \"서브에이전트\", \"독립 태스크\". Do NOT use for: covers subagent, dev, 서브에이전트, 독립 태스크, independent"
metadata:
  holon-triggers: |
    executing implementation plans with independent tasks in the current session
---

---
name: subagent-driven-development
description: >-
  Use when executing implementation plans with independent tasks in the current
  session. Korean triggers: "서브에이전트", "독립 태스크". Do NOT use for parallel independent tasks
  (use sp-parallel-agents).
metadata:
  author: "superpowers"
  version: "1.0.0"
  category: "process"
---
# Subagent-Driven Development

Execute plan by dispatching fresh subagent per task, with two-stage review after each: spec compliance review first, then code quality review.

**Core principle:** Fresh subagent per task + two-stage review (spec then quality) = high quality, fast iteration

## When to Use

```dot
digraph when_to_use {
    "Have implementation plan?" [shape=diamond];
    "Tasks mostly independent?" [shape=diamond];
    "Stay in this session?" [shape=diamond];
    "subagent-driven-development" [shape=box];
    "executing-plans" [shape=box];
    "Manual execution or brainstorm first" [shape=box];

    "Have implementation plan?" -> "Tasks mostly independent?" [label="yes"];
    "Have implementation plan?" -> "Manual execution or brainstorm first" [label="no"];
    "Tasks mostly independent?" -> "Stay in this session?" [label="yes"];
    "Tasks mostly independent?" -> "Manual execution or brainstorm first" [label="no - tightly coupled"];
    "Stay in this session?" -> "subagent-driven-development" [label="yes"];
    "Stay in this session?" -> "executing-plans" [label="no - parallel session"];
}
```

**vs. Executing Plans (parallel session):**
- Same session (no context switch)
- Fresh subagent per task (no context pollution)
- Two-stage review after each task: spec compliance first, then code quality
- Faster iteration (no human-in-loop between tasks)

## The Process

```dot
digraph process {
    rankdir=TB;

    subgraph cluster_per_task {
        label="Per Task";
        "Dispatch implementer subagent (./implementer-prompt.md)" [shape=box];
        "Implementer subagent asks questions?" [shape=diamond];
        "Answer question
