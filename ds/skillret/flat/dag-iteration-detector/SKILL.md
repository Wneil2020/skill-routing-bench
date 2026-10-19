---
name: "dag-iteration-detector"
description: "Use when the task involves orchestrate agent_skill: covers dag, iteration, detector, dag-convergence-monitor, dag-feedback-synthesizer"
---

# dag-iteration-detector

Identifies when task outputs require iteration based on quality signals, unmet requirements, or explicit feedback. Triggers appropriate re-execution strategies. Activate on 'needs iteration', 'retry needed', 'not good enough', 'try again', 'refine output'. NOT for feedback generation (use dag-feedba
