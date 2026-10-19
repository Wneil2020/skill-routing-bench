---
name: "workflow-executor-inline"
description: "Use when the task involves orchestrate pipeline: covers workflow, executor, inline, providers, zenmux"
---

# workflow-executor-inline

Inline workflow executor for proxy providers (ZenMux, custom API providers).
Executes workflow steps directly in the main context WITHOUT spawning Task subagents.

Use this skill when:
- Running looplia workflows via ZenMux or other proxy providers
- Task subagents fail with "invalid_model" errors
-
