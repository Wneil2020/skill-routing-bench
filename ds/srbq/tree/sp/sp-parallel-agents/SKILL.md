---
name: sp-parallel-agents
description: "Use when Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies. Do NOT use for: covers parallel, abort, aborted, adjusting, concurrently"
metadata:
  holon-triggers: |
    facing 2+ independent tasks that can be worked on without shared state
    sequential dependencies
---

---
name: dispatching-parallel-agents
description: >-
  Use when facing 2+ independent tasks that can be worked on without shared
  state or sequential dependencies. Do NOT use for sequential dependent tasks
  (use workflow-sequential).
metadata:
  author: "superpowers"
  version: "1.0.0"
  category: "process"
---
# Dispatching Parallel Agents

## Overview

When you have multiple unrelated failures (different test files, different subsystems, different bugs), investigating them sequentially wastes time. Each investigation is independent and can happen in parallel.

**Core principle:** Dispatch one agent per independent problem domain. Let them work concurrently.

## When to Use

```dot
digraph when_to_use {
    "Multiple failures?" [shape=diamond];
    "Are they independent?" [shape=diamond];
    "Single agent investigates all" [shape=box];
    "One agent per problem domain" [shape=box];
    "Can they work in parallel?" [shape=diamond];
    "Sequential agents" [shape=box];
    "Parallel dispatch" [shape=box];

    "Multiple failures?" -> "Are they independent?" [label="yes"];
    "Are they independent?" -> "Single agent investigates all" [label="no - related"];
    "Are they independent?" -> "Can they work in parallel?" [label="yes"];
    "Can they work in parallel?" -> "Parallel dispatch" [label="yes"];
    "Can they work in parallel?" -> "Sequential agents" [label="no - shared state"];
}
```

**Use when:**
- 3+ test files failing with different root causes
- Multiple subsystems broken independently
- Each problem can be understood without context from others
- No shared state between investigations

**Don't use when:**
- Failures are related (fix one might fix others)
- Need to understand full system state
- Agents would interfere with each other

## The Pattern

### 1. Identify Independent Domains

Group failures by what's broken:
- File A tests: Tool approval flow
- File B tests: Batch completion behavior
- File C tests: Abort functionality

Each domain is indep
