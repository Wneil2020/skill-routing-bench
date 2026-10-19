---
name: workflow-eval-opt
description: "Use when Wrap any generation task in an evaluator-optimizer loop with defined quality criteria, iteration limits, and stopping conditions. Separates: covers eval, opt, checkers, deterministic, falls"
metadata:
  holon-triggers: |
    refine this
    iterate until quality
---

---
name: workflow-eval-opt
description: >-
  Wrap any generation task in an evaluator-optimizer loop with defined quality
  criteria, iteration limits, and stopping conditions. Separates generation
  from evaluation for higher output quality. Use when the user asks to "refine
  this", "iterate until quality", "evaluator optimizer", "eval-opt loop",
  "quality loop", "re-evaluate", "refine output", "improve quality iteratively",
  "품질 반복", "평가 최적화", or when first-draft quality consistently falls short.
  Do NOT use when first-draft quality already meets needs. Do NOT use for
  real-time tasks requiring immediate responses. Do NOT use when evaluation
  criteria are too subjective for consistent application. Do NOT use when
  deterministic tools (linters, type checkers, test runners) can check quality
  directly — use those instead.
metadata:
  author: thaki
  version: 1.0.0
  category: orchestration
---

# Workflow Eval-Opt — Evaluator-Optimizer Loop

Wrap any generation task in an iterative refinement cycle: one agent generates, another evaluates against measurable criteria, and the generator refines based on feedback. Continues until quality threshold is met or max iterations reached.

Based on the Evaluator-Optimizer workflow pattern from Anthropic's agent workflow patterns. The key insight: generation and evaluation are different cognitive tasks. Separating them lets each agent specialize. Trades token usage and iteration time for higher output quality.

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| Generator task | Yes | What to generate (code, report, communication, etc.) |
| Evaluation criteria | Yes | Measurable dimensions with scoring rubric |
| Quality threshold | Yes | Minimum score to pass (e.g., 8.0/10, no Critical findings) |
| Max iterations | No | Maximum refinement cycles (default: 2) |
| Evaluator type | No | Which evaluator to use (see Evaluator Configuration) |
| Scope | No | What to re-evaluate on refinement (
