---
name: skill-optimizer
description: "Use when Audit, evaluate, benchmark, and compare existing agent skills (SKILL.md files) for quality assurance. Use when the user asks to \"optimize: covers optimizer, 스킬, 감사, effectiveness, assurance"
metadata:
  holon-triggers: |
    optimize skills
    audit skills
---

---
name: skill-optimizer
description: >-
  Audit, evaluate, benchmark, and compare existing agent skills (SKILL.md
  files) for quality assurance. Use when the user asks to "optimize skills",
  "audit skills", "check skill quality", "evaluate skill", "benchmark skill",
  "test skill effectiveness", "compare skill versions", "skill regression test",
  or "measure skill impact". Do NOT use for creating new skills from scratch
  (use create-skill instead), general code review, or non-skill file
  optimization. Korean triggers: "스킬", "감사", "리뷰", "테스트".
metadata:
  author: "thaki"
  version: "2.0.0"
  category: "execution"
---
# Skill Optimizer

Quality assurance for agent skills: static audit, runtime evaluation, quantitative benchmarking, and A/B comparison. Adapted from Anthropic's Executor/Grader/Comparator/Analyzer pattern for Cursor's Task subagent system.

## Input

The user provides:
1. **Mode** (optional) — `audit` (default), `eval`, `benchmark`, or `compare`
2. **Skills directory** (optional) — defaults to `.cursor/skills/`
3. **Scope** (optional) — "all" (default) or a specific skill name

## Modes

### audit (default) — Static Quality Analysis

Analyze skill files against Anthropic's guide without running them. See [Audit Workflow](#audit-workflow) below.

### eval — Runtime Test Cases

Write and run test cases against a skill using independent subagents. Measures whether a skill produces the intended behavioral change. See [references/eval-framework.md](references/eval-framework.md) for full protocol.

### benchmark — Quantitative Performance Measurement

Run multiple eval iterations and collect statistical metrics: pass rate, quality score, token efficiency, consistency. See [references/benchmark-protocol.md](references/benchmark-protocol.md) for full protocol.

### compare — A/B Blind Comparison

Run identical prompts through two skill versions (or skill vs no-skill) and have an independent Comparator judge outputs blindly. See [references/comparator-prot
