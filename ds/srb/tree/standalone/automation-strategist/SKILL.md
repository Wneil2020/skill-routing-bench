---
name: automation-strategist
description: "Use when Strategic automation planning for the stock analytics pipeline — decide what to automate vs keep manual, design human-in-the-loop: covers automation, strategist, roi, thinker, keep"
metadata:
  holon-triggers: |
    plan automation
    should I automate this
---

---
name: automation-strategist
description: >-
  Strategic automation planning for the stock analytics pipeline — decide what
  to automate vs keep manual, design human-in-the-loop checkpoints, calculate
  automation ROI, and manage automation risk. Provides decision frameworks for
  "should we automate this?" questions. Use when the user asks to "plan
  automation", "should I automate this", "automation strategy", "human in the
  loop", "automation risk", "what to automate", "자동화 전략", "자동화 판단",
  "휴먼 인 더 루프", "자동화 ROI", or wants to make strategic decisions about
  what to automate in the trading pipeline.
  Do NOT use for building specific pipelines (use pipeline-builder).
  Do NOT use for designing system architecture (use system-thinker).
  Do NOT use for running automated workflows (use ai-workflow-integrator).
  Do NOT use for operational risk assessment (use compliance-governance).
metadata:
  author: thaki
  version: 1.0.0
  category: review
---

# Automation Strategist

Strategic automation planning for the stock analytics pipeline. Knowing what to automate is valuable. Knowing what NOT to automate is more valuable.

## Decision Framework: ARIA (Assess-Risk-Implement-Audit)

### Phase 1: Assess Automation Candidates

For any process the user considers automating, evaluate 5 factors:

| Factor | Question | Score (1-5) |
|--------|----------|-------------|
| **Frequency** | How often does this run? | 1=yearly, 5=hourly |
| **Volume** | How much data/work per run? | 1=single item, 5=hundreds |
| **Consistency** | How rule-based is the logic? | 1=pure judgment, 5=pure rules |
| **Error cost** | What happens if automation is wrong? | 1=catastrophic, 5=trivial |
| **Time saved** | How much human time per run? | 1=seconds, 5=hours |

**Automation Score** = (Frequency + Volume + Consistency + Error_cost + Time_saved) / 5

| Score | Recommendation |
|-------|---------------|
| 4.0 - 5.0 | Automate immediately |
| 3.0 - 3.9 | Automate with monitoring |
| 2.0 - 2.9 | 
