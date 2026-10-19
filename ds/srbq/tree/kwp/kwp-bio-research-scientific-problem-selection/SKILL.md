---
name: kwp-bio-research-scientific-problem-selection
description: "Use when This skill should be used when scientists need help with research problem selection, project ideation, troubleshooting stuck projects, or strategic: covers kwp, bio, research, 리서치, 검색"
---

---
name: kwp-bio-research-scientific-problem-selection
description: >-
  This skill should be used when scientists need help with research problem
  selection, project ideation, troubleshooting stuck projects, or strategic
  scientific decisions. Use this skill when users ask to pitch a new research
  idea, work through a project problem, evaluate project risks, plan research
  strategy, navigate decision trees, or get help choosing what scientific
  problem to work on. Typical requests include "I have an idea for a project",
  "I'm stuck on my research", "help me evaluate this project", "what should I
  work on", or "I need strategic advice about my research". Do NOT use for tasks
  outside the bio domain. Korean triggers: "리서치", "검색", "계획", "스킬".
metadata:
  author: "anthropic-kwp"
  version: "1.0.0"
  category: "workflow"
---
# Scientific Problem Selection Skills

A conversational framework for systematic scientific problem selection based on Fischbach & Walsh's "Problem choice and decision trees in science and engineering" (Cell, 2024).

## Getting Started

Present users with three entry points:

**1) Pitch an idea for a new project** — to work it up together

**2) Share a problem in a current project** — to troubleshoot together

**3) Ask a strategic question** — to navigate the decision tree together

This conversational entry meets scientists where they are and establishes a collaborative tone.

---

## Option 1: Pitch an Idea

### Initial Prompt
Ask: **"Tell me the short version of your idea (1-2 sentences)."**

### Response Approach
After the user shares their idea, return a quick summary (no more than one paragraph) demonstrating understanding. Note the general area of research and rephrase the idea in a way that highlights its kernel—showing alignment and readiness to dive into details.

### Follow-up Prompt
Then ask for more detail: "Now give me a bit more detail. You might include, however briefly or even say where you are unsure:
1. What exactly you w
