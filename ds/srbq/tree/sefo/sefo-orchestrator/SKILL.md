---
name: sefo-orchestrator
description: "Use when Orchestrate complex tasks via SEFO's Skill-Aware Dynamic Orchestration (SADO) API. Decomposes tasks into optimal skill: covers sefo, orchestrator, compositions, constrained, decomposes"
metadata:
  holon-triggers: |
    SEFO route
    sefo orchestrate
---

---
name: sefo-orchestrator
description: >-
  Orchestrate complex tasks via SEFO's Skill-Aware Dynamic Orchestration (SADO) API.
  Decomposes tasks into optimal skill compositions using governance-aware routing,
  cost-constrained DAG optimization, and automated subagent execution. Use when the
  user asks to "SEFO route", "sefo orchestrate", "skill-aware routing", "SADO route",
  "SEFO 오케스트레이션", "스킬 라우팅", "SADO 라우팅", or any task that benefits from
  automated multi-skill composition with trust and cost awareness. Do NOT use for
  manual skill execution (invoke skills directly), federation operations (use
  sefo-federation), or governance/trust operations (use sefo-governance).
metadata:
  author: thaki
  version: "0.1.0"
  category: sefo
---

# SEFO Orchestrator

Orchestrate complex tasks using SEFO's Skill-Aware Dynamic Orchestration (SADO) pipeline. This skill extends the agent abstraction from 4-tuple to 5-tuple (Instruction, Context, Tools, Model, Skills) with cost-aware compositional routing.

## Instructions

### Input

- A natural language task description
- Optional budget constraint (default: 100.0 cost units)
- Optional compliance requirements (e.g., ["signed_only", "trust_above_0.7"])

### Orchestration Pipeline

1. **Route via SADO**: Call `POST /api/v1/sefo/sado/route` with:
   ```json
   {
     "task_description": "<task>",
     "budget": 100.0,
     "compliance": ["signed_only"]
   }
   ```
   This returns:
   - `selected_skills`: Skills chosen by the governance-aware router
   - `composition_path`: Optimal execution order (DAG path)
   - `total_cost`: Estimated cost within budget
   - `governance_scores`: Per-skill trust/compliance scores

2. **Validate Composition**: Verify the composition path is a valid DAG by checking `GET /api/v1/sefo/sado/graph`. Ensure no circular dependencies and all required skills are active.

3. **Execute Sequentially**: For each skill in `composition_path`:
   - Launch a subagent with `subagent_type="generalPurpose"` and
