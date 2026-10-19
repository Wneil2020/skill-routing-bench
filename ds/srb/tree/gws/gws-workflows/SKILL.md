---
name: gws-workflows
description: "Use when Cross-service Google Workspace productivity workflows via the gws CLI -- daily standup reports, meeting preparation, weekly digests: covers gws, 데일리 스탠드업, 주간 요약, announce, announcements"
metadata:
  holon-triggers: |
    a standup summary
    meeting prep
---

---
name: gws-workflows
description: >-
  Cross-service Google Workspace productivity workflows via the gws CLI --
  daily standup reports, meeting preparation, weekly digests, email-to-task
  conversion, and file announcements. Use when the user asks for a standup
  summary, meeting prep, weekly digest, to convert email to a task, or to
  announce a file in Chat. Do NOT use for single-service operations (use
  gws-gmail, gws-calendar, gws-drive, gws-chat directly). Korean triggers:
  "데일리 스탠드업", "주간 요약".
metadata:
  author: "googleworkspace/cli (adapted)"
  version: "1.0.0"
  category: "integration"
---
# Google Workspace Workflows

Cross-service productivity workflows that combine Gmail, Calendar, Drive, Chat, and Tasks. Google Tasks is accessed through these workflow subcommands (no separate gws-tasks skill needed).

> **Prerequisites**: `gws` must be installed and authenticated. See `gws-workspace` skill.

## Standup Report

Generate a daily standup summary: today's meetings + open tasks.

```bash
gws workflow +standup-report
gws workflow +standup-report --format table
```

Combines Calendar agenda and Tasks data into a single standup view.

## Meeting Prep

Prepare for your next meeting: agenda, attendees, and linked docs.

```bash
gws workflow +meeting-prep
gws workflow +meeting-prep --calendar primary
```

| Flag | Default | Description |
|------|---------|-------------|
| `--calendar` | primary | Calendar to check |

Pulls the next upcoming event, lists attendees, extracts linked Drive documents from the event description, and summarizes everything.

## Weekly Digest

Generate a weekly summary: this week's meetings + unread email count.

```bash
gws workflow +weekly-digest
gws workflow +weekly-digest --format table
```

Best run on Monday mornings for weekly planning.

## Email to Task

Convert a Gmail message into a Google Tasks entry.

```bash
gws workflow +email-to-task --message-id <MSG_ID>
gws workflow +email-to-task --message-id MSG_ID --tasklist @defa
