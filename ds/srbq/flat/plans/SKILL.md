---
name: plans
description: "Use when Two-phase pipeline, optimize a raw prompt using prompt-architect frameworks, then decompose the optimized prompt into a skill-based: covers plans, delegation, ordering, both, decompose"
metadata:
  holon-triggers: |
    plan and optimize
    architect and plan
---

---
name: plans
description: >-
  Two-phase pipeline: optimize a raw prompt using prompt-architect frameworks,
  then decompose the optimized prompt into a skill-based execution plan with
  task delegation, dependency ordering, and verification criteria. Use when the
  user runs /plans, asks to "plan and optimize", "architect and plan", "optimize
  then plan", "프롬프트 최적화 후 계획", "플랜 작성", or wants both prompt optimization and
  execution planning in one flow. Do NOT use for prompt optimization only (use
  prompt-architect), execution only without optimization (use mission-control),
  or simple implementation planning (use /plan command).
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "execution"
---
# Plans — Optimize Prompt, Then Plan Execution

A meta-orchestrator that combines prompt-architect (framework-based prompt design) with mission-control-style skill planning. Takes a raw prompt, structures it using the best framework, then decomposes it into a skill-based execution plan.

## Workflow

Execute these 7 steps in order.

### Step 1: Receive Raw Prompt

Accept the user's raw prompt. This may come from:
- `/plans` command `$ARGUMENTS`
- Direct user message
- Selected text in the editor

If the prompt is empty, ask the user to provide one. Store the original text verbatim for the before/after comparison.

### Step 2: Phase 1 — Optimize the Prompt

Read and follow the `prompt-architect` skill at `.cursor/skills/prompt-architect/SKILL.md`.

Execute its 6-step workflow against the raw prompt:
1. **Score** the original prompt across 5 dimensions (Clarity, Specificity, Context, Completeness, Structure — each 1-10)
2. **Recommend** a framework using the decision tree (or use `--framework` override if provided)
3. **Ask** 3-5 clarifying questions based on framework gaps
4. **Apply** the framework template from `.cursor/skills/prompt-architect/references/templates.md`
5. **Present** before/after comparison with scores
6. **Iterate** if the user wants changes

I
