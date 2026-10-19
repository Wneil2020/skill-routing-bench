---
name: calendar-daily-briefing
description: "Use when Fetch today's Google Calendar events and produce a concise Korean briefing with preparation alerts for meetings and interviews. Use when the: covers calendar, daily, briefing, staff, chief"
metadata:
  holon-triggers: |
    today's schedule
    calendar briefing
---

---
name: calendar-daily-briefing
description: >-
  Fetch today's Google Calendar events and produce a concise Korean briefing
  with preparation alerts for meetings and interviews. Use when the user asks
  for "today's schedule", "calendar briefing", "오늘 일정", "캘린더 브리핑", "daily
  briefing", "오늘 미팅", "일정 요약", or "what's on my calendar". Do NOT use for
  creating events (use gws-calendar), email triage (use gmail-daily-triage), or
  weekly digests (use ai-chief-of-staff).
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "execution"
---
# Calendar Daily Briefing

Fetch today's calendar events, classify them, and produce a concise Korean briefing highlighting meetings and interviews that need preparation.

> **Prerequisites**: `gws` CLI installed and authenticated. See `gws-workspace` skill.

## Workflow

### Step 1: Fetch Today's Events

```bash
gws calendar +agenda --today
```

If JSON output is needed for parsing:

```bash
gws calendar events list \
  --params '{"calendarId": "primary", "timeMin": "YYYY-MM-DDT00:00:00+09:00", "timeMax": "YYYY-MM-DDT23:59:59+09:00", "singleEvents": true, "orderBy": "startTime"}' \
  --format json
```

Replace `YYYY-MM-DD` with today's date.

### Step 2: Classify Events

For each event, classify into one of these categories:

| Category | Detection | Priority | Action |
|----------|-----------|----------|--------|
| **Interview** | Title/description contains: "면접", "interview", "채용", "candidate", "지원자" | HIGH | Alert: prepare questions, review resume |
| **External Meeting** | Has attendees from non-company domains | HIGH | Alert: prepare agenda, review context |
| **Team Meeting** | Title contains: "스크럼", "scrum", "데일리", "daily", "스프린트", "sprint", "회의", "meeting" | MEDIUM | Note: check agenda/action items |
| **1:1** | Exactly 2 attendees (including self) | MEDIUM | Note: prepare talking points |
| **Focus Time** | Title contains: "집중", "focus", "deep work", "리팩토링" | LOW | Note: block protected |
| **All-day Event** | No spe
