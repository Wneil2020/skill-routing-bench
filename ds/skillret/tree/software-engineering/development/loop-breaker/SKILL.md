---
name: "loop-breaker"
description: "Use when the task involves implement pipeline: covers loop, breaker, workers, self-recursion, themselves."
---

# loop-breaker

Scaffold middleware to detect and block Worker self-recursion, infinite fetch chains, and runaway loops. Use this skill when designing Workers that call other Workers, implement webhooks, or handle events that might trigger themselves.
