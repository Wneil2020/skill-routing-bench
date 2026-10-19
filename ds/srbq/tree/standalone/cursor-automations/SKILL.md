---
name: cursor-automations
description: "Use when Create, configure, and manage Cursor Automations — always-on cloud agents that run on schedules or respond to events from GitHub: covers cursor, automations, webhooks, involving, linear"
metadata:
  holon-triggers: |
    create an automation
    set up a cron agent
---

---
name: cursor-automations
description: >-
  Create, configure, and manage Cursor Automations — always-on cloud agents
  that run on schedules or respond to events from GitHub, Slack, Linear,
  PagerDuty, and webhooks. Guides through trigger selection, tool configuration,
  MCP setup, memory management, and prompt writing. Use when the user asks to
  "create an automation", "set up a cron agent", "automate PR reviews",
  "schedule a daily digest", "cursor automation", "always-on agent",
  "자동화 설정", or any task involving recurring/event-driven cloud agents.
  Do NOT use for local CI checks (use ci-quality-gate), one-time cloud agent
  runs, or Cursor IDE hooks (use hooks configuration).
metadata:
  author: thaki
  version: "1.0.0"
  category: automation
---

# Cursor Automations — Always-On Cloud Agents

Cursor Automations run cloud agents in the background on schedules or in response to events. They spin up an isolated Ubuntu VM, follow your prompt using configured tools and MCPs, and verify their own output.

Create automations at [cursor.com/automations/new](https://cursor.com/automations/new) or start from a [marketplace template](https://cursor.com/marketplace#automations).

## When to Use

- Setting up recurring code review, security scanning, or test coverage agents
- Automating bug triage from Slack channels
- Creating daily/weekly digest summaries posted to Slack
- Responding to GitHub PR events, Linear issues, or PagerDuty incidents
- Building custom event-driven workflows via webhooks

## Quick Start

Four steps to create an automation:

1. **Choose a trigger** — when should it run? (schedule, GitHub event, Slack message, etc.)
2. **Enable tools** — what can the agent do? (open PRs, send Slack messages, use MCP)
3. **Write a prompt** — what should the agent do? (instructions, quality bar, output format)
4. **Launch** — save and watch it run

## Automation Categories

### Review and Monitoring

Automations that catch issues before they reach production.


