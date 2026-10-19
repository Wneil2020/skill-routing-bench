---
name: ecc-autonomous-loops
description: "Use when Patterns for autonomous agent loops — sequential pipelines, checkpoint-based recovery, and multi-agent DAG orchestration. Use when designing: covers ecc, autonomous, loops, 자율 루프, 에이전트 루프"
metadata:
  holon-triggers: |
    designing long-running AFK agent workflows
    building agent loop architectures
---

---
name: ecc-autonomous-loops
description: >-
  Patterns for autonomous agent loops — sequential pipelines, checkpoint-based
  recovery, and multi-agent DAG orchestration. Use when designing long-running
  AFK agent workflows, building agent loop architectures, or recovering from
  context window limits. Do NOT use for one-shot task execution. Do NOT use for
  the existing Ralph Loop (use ralph-loop). Do NOT use for daily pipeline
  orchestration (use today). Korean triggers: "자율 루프", "에이전트 루프".
metadata:
  author: "ecc"
  version: "1.0.0"
  category: "engineering"
origin: ECC
---
# Autonomous Loops Skill

> Compatibility note (v1.8.0): `autonomous-loops` is retained for one release.
> The canonical skill name is now `continuous-agent-loop`. New loop guidance
> should be authored there, while this skill remains available to avoid
> breaking existing workflows.

Patterns, architectures, and reference implementations for running Claude Code autonomously in loops. Covers everything from simple `claude -p` pipelines to full RFC-driven multi-agent DAG orchestration.

## When to Use

- Setting up autonomous development workflows that run without human intervention
- Choosing the right loop architecture for your problem (simple vs complex)
- Building CI/CD-style continuous development pipelines
- Running parallel agents with merge coordination
- Implementing context persistence across loop iterations
- Adding quality gates and cleanup passes to autonomous workflows

## Loop Pattern Spectrum

From simplest to most sophisticated:

| Pattern | Complexity | Best For |
|---------|-----------|----------|
| [Sequential Pipeline](#1-sequential-pipeline-claude--p) | Low | Daily dev steps, scripted workflows |
| [NanoClaw REPL](#2-nanoclaw-repl) | Low | Interactive persistent sessions |
| [Infinite Agentic Loop](#3-infinite-agentic-loop) | Medium | Parallel content generation, spec-driven work |
| [Continuous Claude PR Loop](#4-continuous-claude-pr-loop) | Medium | Multi-day iterat
