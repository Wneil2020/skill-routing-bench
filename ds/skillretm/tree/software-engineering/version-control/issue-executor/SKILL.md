---
name: "issue-executor"
description: "Use when the task involves orchestrate agent_skill: covers issue, executor, start, work, retrospective"
---

# issue-executor

Use this skill to start work on a GitHub issue. It synthesizes all relevant context (specs, retrospective, issue details) using the Gemini CLI to generate a step-by-step implementation plan, then creates a feature branch to begin work. Triggers include "start work on issue #X" or "implement issue".
