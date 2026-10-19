---
name: kwp-slack-slack-search
description: "Use when Guidance for effectively searching Slack to find messages, files, channels, and people. Do NOT use for tasks outside the slack domain. Korean: covers kwp, slack, search, 슬랙 검색, 메시지 찾기"
metadata:
  holon-triggers: |
    What is the deadline for project X?
    exact phrase
---

---
name: kwp-slack-slack-search
description: >-
  Guidance for effectively searching Slack to find messages, files, channels,
  and people. Do NOT use for tasks outside the slack domain. Korean triggers:
  "슬랙 검색", "메시지 찾기".
metadata:
  author: "anthropic-kwp"
  version: "1.0.0"
  category: "workflow"
---
# Slack Search

This skill provides guidance for effectively searching Slack to find messages, files, and information.

## Search Tools Overview

| Tool | Use When |
|------|----------|
| `slack_search_public` | Searching public channels only. Does not require user consent. |
| `slack_search_public_and_private` | Searching all channels including private, DMs, and group DMs. Requires user consent. |
| `slack_search_channels` | Finding channels by name or description. |
| `slack_search_users` | Finding people by name, email, or role. |

## Search Strategy

### Start Broad, Then Narrow

1. Begin with a simple keyword or natural language question.
2. If too many results, add filters (`in:`, `from:`, date ranges).
3. If too few results, remove filters and try synonyms or related terms.

### Choose the Right Search Mode

- **Natural language questions** (e.g., "What is the deadline for project X?") — Best for fuzzy, conceptual searches where you don't know exact keywords.
- **Keyword search** (e.g., `project X deadline`) — Best for finding specific, exact content.

### Use Multiple Searches

Don't rely on a single search. Break complex questions into smaller searches:
- Search for the topic first
- Then search for specific people's contributions
- Then search in specific channels

## Search Modifiers Reference

### Location Filters
- `in:channel-name` — Search within a specific channel
- `in:<#C123456>` — Search in channel by ID
- `-in:channel-name` — Exclude a channel
- `in:<@U123456>` — Search in DMs with a user

### User Filters
- `from:<@U123456>` — Messages from a specific user (by ID)
- `from:username` — Messages from a user (by Slack username)
- `to:me` — Message
