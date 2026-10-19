---
name: "tdd-workflow"
description: "Use when the task involves test code: covers tdd, workflow, state, vitest-mock-extended, violation"
---

# tdd-workflow

Strict TDD state machine with Result types. 7-state workflow (PLANNING, RED, GREEN, REFACTOR, VERIFY, BLOCKED, VIOLATION). Every message MUST announce state. Integrates with fn(args, deps), vitest-mock-extended, and typed error handling.
