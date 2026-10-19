---
name: gws-calendar
description: "Use when Manage Google Calendar via the gws CLI -- view agenda, create events, check availability, and manage invitations. Use when the user asks to check: covers gws, calendar, 캘린더, 일정, automatic"
metadata:
  holon-triggers: |
    check calendar
    schedule meetings
---

---
name: gws-calendar
description: >-
  Manage Google Calendar via the gws CLI -- view agenda, create events, check
  availability, and manage invitations. Use when the user asks to check
  calendar, schedule meetings, view agenda, create events, or find free time. Do
  NOT use for email (use gws-gmail), Chat messages (use gws-chat), task lists
  (use gws-workflows), or email/Slack-based meeting scheduling with automatic
  agenda generation and attendee coordination (use smart-meeting-scheduler).
  Korean triggers: "캘린더", "일정", "일정 관리".
metadata:
  author: "googleworkspace/cli (adapted)"
  version: "1.0.0"
  category: "integration"
---
# Google Calendar

> **Prerequisites**: `gws` must be installed and authenticated. See `gws-workspace` skill.

```bash
gws calendar <resource> <method> [flags]
```

## Quick Commands

### View Agenda

```bash
gws calendar +agenda                       # upcoming events
gws calendar +agenda --today
gws calendar +agenda --tomorrow
gws calendar +agenda --week --format table
gws calendar +agenda --days 3 --calendar 'Work'
```

| Flag | Default | Description |
|------|---------|-------------|
| `--today` | off | Show today's events only |
| `--tomorrow` | off | Show tomorrow's events |
| `--week` | off | Show this week's events |
| `--days` | -- | Number of days ahead |
| `--calendar` | all | Filter to specific calendar |

Read-only -- never modifies events.

### Create an Event

```bash
gws calendar +insert --summary <TEXT> --start <TIME> --end <TIME>
```

| Flag | Required | Default | Description |
|------|----------|---------|-------------|
| `--summary` | Yes | -- | Event title |
| `--start` | Yes | -- | Start time (ISO 8601 / RFC 3339) |
| `--end` | Yes | -- | End time |
| `--calendar` | No | primary | Calendar ID |
| `--location` | No | -- | Event location |
| `--description` | No | -- | Event body |
| `--attendee` | No | -- | Attendee email (repeatable) |

Use RFC 3339 format: `2026-03-10T09:00:00+09:00`

For recurring events or co
