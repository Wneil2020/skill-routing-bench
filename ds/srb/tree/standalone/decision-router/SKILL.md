---
name: decision-router
description: "Use when Detect decision-worthy items from pipeline outputs and route them to the appropriate Slack decision channel. Personal decisions: covers decision, router, partnerships, inline, personal"
metadata:
  holon-triggers: |
    a pipeline skill (google-daily
    bespin-news-digest
---

---
name: decision-router
description: >-
  Detect decision-worthy items from pipeline outputs and route them to the
  appropriate Slack decision channel. Personal decisions (trading, email replies,
  tool adoption) go to #효정-의사결정; team/CTO decisions (infra, strategy,
  partnerships, budget) go to #7층-리더방. Invoked inline by other pipeline
  skills after their main posting is complete. Use when a pipeline skill
  (google-daily, today, bespin-news-digest, twitter-timeline-to-slack,
  x-to-slack) detects content that requires a decision.
  Do NOT use standalone — always invoked as a sub-routine by pipeline skills.
  Do NOT use for general Slack messaging (use kwp-slack-slack-messaging).
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "execution"
---

# Decision Router

Centralized decision detection, scope classification, and Slack routing engine.
Pipeline skills invoke this as an inline sub-routine after completing their
normal posting workflow.

## Channel Registry

| Channel | ID | Scope | Description |
|---|---|---|---|
| `효정-의사결정` | `C0ANBST3KDE` | personal | Solo decisions (trading, email replies, tool adoption) |
| `7층-리더방` | `C0A6Q7007N2` | team | Team/CTO decisions (infra, strategy, partnerships, budget) |

> **Action Required**: Replace `C0ANBST3KDE` and `C0A6Q7007N2` with actual
> channel IDs after creating the channels in Slack. Use `slack_search_channels`
> MCP tool to retrieve IDs.

## Decision Detection Rules

Each source skill has specific criteria for what constitutes a "decision item."

### From `google-daily`

| Signal | Scope | Urgency |
|---|---|---|
| Colleague email requesting approval, budget, or architectural decision | team | HIGH |
| Email with explicit questions requiring a response decision | personal | MEDIUM |
| Calendar conflict needing resolution | personal | HIGH |
| Procurement/vendor request | team | MEDIUM |
| Keywords: 승인, 결정, 예산, 아키텍처, 채용, 제안, 검토 요청 | context-dependent | MEDIUM |

### From `twitter-timeline-to-slack`

|
