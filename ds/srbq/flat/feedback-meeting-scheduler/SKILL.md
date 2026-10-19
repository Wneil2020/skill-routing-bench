---
name: feedback-meeting-scheduler
description: "Use when Detect PRs and issues needing discussion (stale reviews, conflicting comments, blocked items) and proactively schedule 1,1 feedback: covers feedback, meeting, scheduler, parties, blocked"
metadata:
  holon-triggers: |
    schedule feedback meetings
    find items needing discussion
---

---
name: feedback-meeting-scheduler
description: >-
  Detect PRs and issues needing discussion (stale reviews, conflicting comments,
  blocked items) and proactively schedule 1:1 feedback meetings with relevant
  parties. Use when the user asks to "schedule feedback meetings", "find items
  needing discussion", "피드백 미팅 잡아줘", "리뷰 미팅 스케줄",
  "feedback-meeting-scheduler", or wants automated meeting proposals from sprint
  activity. Do NOT use for general meeting scheduling (use
  smart-meeting-scheduler), calendar management (use gws-calendar), or sprint
  triage without meetings (use sprint-orchestrator).
metadata:
  version: "1.0.0"
  category: "execution"
  author: "thaki"
---
# Feedback Meeting Scheduler

Proactively detect work items needing face-to-face discussion and schedule 1:1 meetings with auto-generated agendas.

## When to Use

- After `github-sprint-digest` runs — detect items needing discussion
- When PR reviews are stale (> 48 hours without response)
- When issue discussions have conflicting opinions
- As part of the sprint orchestrator pipeline

## Workflow

### Step 1: Detect Discussion-Worthy Items

Query GitHub for items needing attention:

**Stale PR Reviews** (no review response > 48h):
```bash
gh pr list --state open --json number,title,author,reviewRequests,reviews,updatedAt
```
Filter: PRs where `reviewRequests` exist but no `reviews` submitted, and `updatedAt` > 48h ago.

**Conflicting Discussions** (opposing review comments):
Look for PRs with both "Request changes" and approved reviews, or issues with > 5 comments with no resolution.

**Blocked Items** (labeled or commented as blocked):
Search for issues/PRs with `blocked` label or comments containing "blocked by", "waiting for", "dependency on".

**Failed CI with no action** (CI red > 24h):
PRs where CI checks failed and no new commits pushed since failure.

### Step 2: Identify Participants

For each discussion-worthy item:
- **PR author** + **requested reviewers** for stale reviews
- **A
