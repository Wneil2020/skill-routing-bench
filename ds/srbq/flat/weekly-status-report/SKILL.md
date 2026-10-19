---
name: weekly-status-report
description: "Use when Generate automated weekly status reports by aggregating GitHub sprint data, Notion project updates, Slack channel summaries, and: covers weekly, status, report, aggregating, completed"
metadata:
  holon-triggers: |
    generate weekly report
    weekly status
---

---
name: weekly-status-report
description: >-
  Generate automated weekly status reports by aggregating GitHub sprint data,
  Notion project updates, Slack channel summaries, and completed tasks.
  Produces a structured Korean report as .docx + Notion page + Slack post.
  Use when the user asks to "generate weekly report", "weekly status",
  "주간 리포트", "주간 보고서", "weekly-status-report", or wants automated
  weekly reporting. Do NOT use for daily stock reports (use today), GitHub
  activity digests only (use github-sprint-digest), or cross-project portfolio
  reports (use portfolio-report-generator).
metadata:
  version: "1.0.0"
  category: "execution"
  author: "thaki"
---
# Weekly Status Report Generator

Aggregate data from multiple sources into a structured weekly status report, replacing the manual 4-hour weekly reporting process.

## When to Use

- End of each sprint week (typically Friday afternoon)
- When management requests a status update
- As part of the EOD pipeline on reporting days

## Workflow

### Step 1: Gather Data Sources

Collect data from the past 7 days across all sources:

**GitHub** (via `github-sprint-digest` data):
```bash
gh issue list --state all --json number,title,state,labels,closedAt,assignees --search "updated:>=$(date -v-7d +%Y-%m-%d)"
gh pr list --state all --json number,title,state,mergedAt,author --search "updated:>=$(date -v-7d +%Y-%m-%d)"
```

**Notion** (via `planning-weekly-pulse` data):
- Project status changes
- Completed milestones
- Updated roadmap items

**Slack** (via Slack MCP):
- Key decisions from team channels
- Blockers raised and resolved
- Customer feedback highlights

### Step 2: Classify and Organize

Group gathered data into standard sections:

1. **Accomplishments**: Merged PRs, closed issues, completed milestones
2. **In Progress**: Open PRs, active issues, ongoing work
3. **Blockers**: Blocked items, unresolved dependencies, stale reviews
4. **Risks**: Overdue items, scope changes, resource constraints
5. **N
