---
name: anthropic-skill-creator
description: "Use when Create new skills, modify and improve existing skills, and measure skill performance. Use when creating a skill from scratch, editing or: covers anthropic, creator, 스킬 생성, 스킬 제작, modify"
metadata:
  holon-triggers: |
    creating a skill from scratch
    optimizing an existing skill
---

---
name: anthropic-skill-creator
description: >-
  Create new skills, modify and improve existing skills, and measure skill
  performance. Use when creating a skill from scratch, editing or optimizing an
  existing skill, running evals to test a skill, benchmarking skill performance
  with variance analysis, or optimizing a skill's description for better
  triggering accuracy. Do NOT use for Cursor-specific skill creation (use
  create-skill skill), or skill auditing/benchmarking only (use
  skill-optimizer). Korean triggers: "스킬 생성", "스킬 제작".
metadata:
  author: "anthropic"
  version: "1.0.0"
  category: "document"
---
# Skill Creator

A skill for creating new skills and iteratively improving them.

At a high level, the process of creating a skill goes like this:

- Decide what you want the skill to do and roughly how it should do it
- Write a draft of the skill
- Create a few test prompts and run claude-with-access-to-the-skill on them
- Help the user evaluate the results both qualitatively and quantitatively
  - While the runs happen in the background, draft some quantitative evals if there aren't any (if there are some, you can either use as is or modify if you feel something needs to change about them). Then explain them to the user (or if they already existed, explain the ones that already exist)
  - Use the `eval-viewer/generate_review.py` script to show the user the results for them to look at, and also let them look at the quantitative metrics
- Rewrite the skill based on feedback from the user's evaluation of the results (and also if there are any glaring flaws that become apparent from the quantitative benchmarks)
- Repeat until you're satisfied
- Expand the test set and try again at larger scale

Your job when using this skill is to figure out where the user is in this process and then jump in and help them progress through these stages. So for instance, maybe they're like "I want to make a skill for X". You can help narrow down what they mean, write a 
