---
name: system-thinker
description: "Use when Design end-to-end automated trading analysis systems by mapping data flows, identifying bottlenecks, creating feedback loops: covers system, thinker, bottlenecks, interconnected, mechanisms"
metadata:
  holon-triggers: |
    design a system
    map data flow
---

---
name: system-thinker
description: >-
  Design end-to-end automated trading analysis systems by mapping data flows,
  identifying bottlenecks, creating feedback loops (prediction vs actual), and
  designing trigger-based automation. Converts manual task-by-task processes into
  interconnected systems with clear inputs, outputs, and feedback mechanisms.
  Use when the user asks to "design a system", "map data flow", "find
  bottlenecks", "create feedback loop", "automate this process end-to-end",
  "system design", "시스템 설계", "데이터 흐름", "병목 분석", "피드백 루프",
  "convert manual to automated", or wants to think about processes as systems
  rather than individual tasks.
  Do NOT use for AI workflow composition (use ai-workflow-integrator).
  Do NOT use for building specific pipelines (use pipeline-builder).
  Do NOT use for microservice architecture review (use backend-expert).
  Do NOT use for infrastructure design (use sre-devops-expert).
metadata:
  author: thaki
  version: 1.0.0
  category: generation
---

# System Thinker

Transform task-by-task thinking into systems thinking for the stock analytics domain. Instead of asking "what do I need to do next?", ask "how much of this could run without me?"

## Core Framework: DFTS (Data-Flow-Trigger-State)

Every system in this project can be decomposed into four elements:

| Element | Question | Example |
|---------|----------|---------|
| **Data** | What information flows through? | Stock prices, signals, reports |
| **Flow** | How does it move between components? | DB → Script → JSON → Slack |
| **Triggers** | What starts each step? | Cron schedule, price threshold, manual command |
| **State** | What persists between runs? | DB records, signal history, MEMORY.md |

## Workflow

### Mode 1: System Mapping

Create a visual map of an existing or proposed system.

**Step 1 — Identify system boundaries:**

Ask or determine:
- What is the system's purpose? (daily analysis, event response, data collection)
- What are the inputs?
