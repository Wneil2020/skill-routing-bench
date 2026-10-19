---
name: ecc-iterative-retrieval
description: "Use when Progressive context building pattern — start broad, then narrow with successive searches to solve the subagent context problem. Use when: covers ecc, iterative, retrieval, 반복 검색, 컨텍스트 빌딩"
metadata:
  holon-triggers: |
    subagents lack sufficient context
    exploring unfamiliar codebases
---

---
name: ecc-iterative-retrieval
description: >-
  Progressive context building pattern — start broad, then narrow with
  successive searches to solve the subagent context problem. Use when subagents
  lack sufficient context, exploring unfamiliar codebases, or building deep
  understanding of complex systems. Do NOT use for simple file reads (use Read
  tool). Do NOT use for known-location lookups (use Grep). Korean triggers:
  "반복 검색", "컨텍스트 빌딩".
metadata:
  author: "ecc"
  version: "1.0.0"
  category: "engineering"
origin: ECC
---
# Iterative Retrieval Pattern

Solves the "context problem" in multi-agent workflows where subagents don't know what context they need until they start working.

## When to Activate

- Spawning subagents that need codebase context they cannot predict upfront
- Building multi-agent workflows where context is progressively refined
- Encountering "context too large" or "missing context" failures in agent tasks
- Designing RAG-like retrieval pipelines for code exploration
- Optimizing token usage in agent orchestration

## The Problem

Subagents are spawned with limited context. They don't know:
- Which files contain relevant code
- What patterns exist in the codebase
- What terminology the project uses

Standard approaches fail:
- **Send everything**: Exceeds context limits
- **Send nothing**: Agent lacks critical information
- **Guess what's needed**: Often wrong

## The Solution: Iterative Retrieval

A 4-phase loop that progressively refines context:

```
┌─────────────────────────────────────────────┐
│                                             │
│   ┌──────────┐      ┌──────────┐            │
│   │ DISPATCH │─────▶│ EVALUATE │            │
│   └──────────┘      └──────────┘            │
│        ▲                  │                 │
│        │                  ▼                 │
│   ┌──────────┐      ┌──────────┐            │
│   │   LOOP   │◀─────│  REFINE  │            │
│   └──────────┘      └──────────┘            │
│         
