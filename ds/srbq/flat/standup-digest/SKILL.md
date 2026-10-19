---
name: standup-digest
description: "Use when Generate multi-source daily standup digests per team member by aggregating GitHub commits/PRs/issues, Slack messages, and calendar: covers standup, digest, blocked, member, aggregating"
metadata:
  holon-triggers: |
    generate standup
    daily standup summary
---

---
name: standup-digest
description: >-
  Generate multi-source daily standup digests per team member by aggregating
  GitHub commits/PRs/issues, Slack messages, and calendar events into
  did/doing/blocked summaries. Use when the user asks to "generate standup",
  "daily standup summary", "스탠드업 요약", "데일리 스탠드업",
  "standup-digest", or wants automated standup reports. Do NOT use for
  GitHub-only activity digests (use github-sprint-digest), weekly status
  reports (use weekly-status-report), or general calendar briefing (use
  calendar-daily-briefing).
metadata:
  version: "1.0.0"
  category: "execution"
  author: "thaki"
---
# Standup Digest

Multi-source daily standup summary: aggregate yesterday's activity per team member into structured "did / doing / blocked" reports.

## When to Use

- Each morning before standup meetings
- As part of the Sprint track in the daily pipeline
- When team leads need a quick overview of team progress

## Data Sources

| Source | What to Collect | Tool |
|--------|----------------|------|
| GitHub | Commits (across all org repos), PR updates, issue comments, reviews | GitHub MCP / `gh` CLI |
| Slack | Messages in team channels, thread replies | Slack MCP |
| Calendar | Yesterday's meetings, today's schedule | `gws-calendar` |
| Sprint Board | Issue status changes, sprint progress | GitHub Projects GraphQL |

## Workflow

### Step 1: Define Team Roster

Read team roster from configuration (`.standup-config.json`):

```json
{
  "team": "platform",
  "members": [
    {"github": "dev1", "slack": "U12345", "email": "dev1@company.com", "name": "Alice"},
    {"github": "dev2", "slack": "U67890", "email": "dev2@company.com", "name": "Bob"}
  ],
  "channel": "#platform-standup",
  "standup_time": "09:30"
}
```

### Step 2: Gather Per-Person Activity

For each team member, collect yesterday's activity (use the team's configured timezone; default to `Asia/Seoul` if not specified):

**GitHub**:
```bash
gh api search/commits --jq '.items[] | {sh
