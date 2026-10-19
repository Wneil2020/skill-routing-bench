---
name: "agent-browser-loop"
description: "Use when the task involves debug ui_component: covers agent, browser, loop, state, back-and-forth"
---

# agent-browser-loop

Use when an agent must drive a live browser session in a back-and-forth loop (state -> explicit actions -> state) for UI validation, reproducible QA, or debugging UI behavior. Prefer this over one-shot CLI usage when an agent needs inspectable, stepwise control.
