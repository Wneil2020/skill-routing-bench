---
name: gmail-daily-triage
description: "Use when Triage yesterday's Gmail inbox, delete spam, move low-priority notifications (Notion, RunPod, GitHub, calendar accepts) to a label, summarize: covers gmail, daily, triage, accepts, runpod"
metadata:
  holon-triggers: |
    triage email
    clean up inbox
---

---
name: gmail-daily-triage
description: >-
  Triage yesterday's Gmail inbox: delete spam, move low-priority notifications
  (Notion, RunPod, GitHub, calendar accepts) to a label, summarize unanswered
  emails with action items into a .docx, compile bespin_news links into a news
  digest .docx via Playwright, open company colleague attachments, and create
  Gmail filters for recurring patterns. Use when the user asks to "triage
  email", "clean up inbox", "yesterday's emails", "메일 정리", "이메일 트리아지", "어제 메일
  정리", "gmail triage", or "inbox cleanup". Do NOT use for sending emails (use
  gws-gmail), reading a single email, or calendar management (use gws-calendar).
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "execution"
---
# Gmail Daily Triage

Automated daily inbox cleanup that classifies yesterday's emails, trashes spam, files low-priority notifications, summarizes actionable emails, and creates Gmail filters.

> **Prerequisites**: `gws` CLI installed and authenticated. See `gws-workspace` skill.

## Sub-Skill Index

| Phase | Description | Reference |
|-------|-------------|-----------|
| Sender Rules | Classification patterns for known senders | [references/sender-rules.md](references/sender-rules.md) |
| Filter Templates | Gmail filter JSON templates | [references/filter-templates.md](references/filter-templates.md) |

## Workflow

### Phase 0: Setup Labels

Ensure the "Low Priority" label exists. If not, create it.

```bash
gws gmail users labels list --params '{"userId": "me"}'
```

If "Low Priority" is missing:

```bash
gws gmail users labels create \
  --params '{"userId": "me"}' \
  --json '{"name": "Low Priority", "labelListVisibility": "labelShow", "messageListVisibility": "show"}'
```

Save the label ID for later use.

### Phase 1: Fetch Yesterday's Emails

Calculate yesterday's date boundaries and fetch all messages.

```bash
gws gmail users messages list \
  --params '{"userId": "me", "q": "after:YYYY/MM/DD before:YYYY/MM/DD", "maxResults"
