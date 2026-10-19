---
name: "agent-orchestrator-manager"
description: "Use when the task involves orchestrate agent_skill: covers agent, orchestrator, manager, tasks, agents"
---

# agent-orchestrator-manager

Orchestrates multi-agent workflows by delegating ALL tasks to spawned subagents via /spawn command. Parallelizes independent work, supervises execution, tracks progress in UUID-based output directories, and generates summary reports. Never executes tasks directly. Triggers on keywords: orchestrate,
