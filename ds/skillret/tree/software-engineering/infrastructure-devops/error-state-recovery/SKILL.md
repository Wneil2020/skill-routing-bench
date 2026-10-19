---
name: "error-state-recovery"
description: "Use when the task involves debug pipeline: covers error, state, recovery, escalates, wraps"
---

# error-state-recovery

Wraps command execution in a self-healing loop. Uses heuristics to auto-fix common errors (missing deps, locked files) or escalates to the Agent with structured error context.
