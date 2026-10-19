---
name: skill-autoimprove
description: "Use when Autonomously optimize any existing skill's prompt by running it repeatedly, scoring outputs against binary evals, mutating one: covers autoimprove, autoresearch, binary, improved, karpathy"
metadata:
  holon-triggers: |
    skill-autoimprove
    auto-improve this skill
---

---
name: skill-autoimprove
description: >-
  Autonomously optimize any existing skill's prompt by running it repeatedly,
  scoring outputs against binary evals, mutating one thing at a time, and
  keeping only improvements. Based on Karpathy's autoresearch methodology.
  Use when the user asks to "skill-autoimprove", "auto-improve this skill",
  "자동 스킬 개선", "autonomous skill optimization", "self-improve skill",
  "test and improve skill", "run evals and fix skill", "스킬 자동 개선",
  "스킬 최적화 루프", "스킬 자동 반복 개선", "skill autoimprove", or wants
  an autonomous loop that tests a skill, finds failures, mutates the prompt,
  and keeps improvements. Outputs: an improved SKILL.md, results.tsv log,
  changelog.md of every mutation tried, and a live HTML dashboard.
  Do NOT use for static skill auditing without mutation (use skill-optimizer
  audit mode). Do NOT use for creating skills from scratch (use
  anthropic-skill-creator or create-skill). Do NOT use for improving output
  quality without changing the skill prompt (use workflow-eval-opt). Do NOT
  use for transcript-based skill evolution (use autoskill-evolve). Do NOT
  use for autonomous research paper pipelines (use auto-research).
---

# Skill Auto-Improve

Most skills work about 70% of the time. The other 30% produces garbage. The fix is not to rewrite the skill from scratch — it is to let an agent run it dozens of times, score every output, and tighten the prompt until that 30% disappears.

This skill adapts Andrej Karpathy's autoresearch methodology (autonomous experimentation loops) to skill prompt optimization. Instead of optimizing ML training code, we optimize skill prompts through measured, one-mutation-at-a-time experiments.

---

## The Core Job

Take any existing skill, define what "good output" looks like as binary yes/no checks, then run an autonomous loop that:

1. Generates outputs from the skill using test inputs
2. Scores every output against the eval criteria
3. Mutates the skill prompt to fix the most 
