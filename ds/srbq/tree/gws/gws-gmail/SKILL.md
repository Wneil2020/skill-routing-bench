---
name: gws-gmail
description: "Use when Manage Gmail via the gws CLI -- send emails, triage inbox, watch for new messages, manage labels and filters. Use when the user asks to send email: covers gws, gmail, 이메일, 메일 보내기, invites"
metadata:
  holon-triggers: |
    send email
    check inbox
---

---
name: gws-gmail
description: >-
  Manage Gmail via the gws CLI -- send emails, triage inbox, watch for new
  messages, manage labels and filters. Use when the user asks to send email,
  check inbox, read mail, triage messages, or manage Gmail. Do NOT use for
  Google Chat messages (use gws-chat), calendar invites (use gws-calendar), or
  Drive file operations (use gws-drive), or AI-drafted reply workflows with
  approval gates (use email-auto-reply). Korean triggers: "이메일", "메일 보내기", "받은편지함".
metadata:
  author: "googleworkspace/cli (adapted)"
  version: "1.0.0"
  category: "integration"
---
# Gmail

> **Prerequisites**: `gws` must be installed and authenticated. See `gws-workspace` skill.

```bash
gws gmail <resource> <method> [flags]
```

## Quick Commands

### Send Email

```bash
gws gmail +send --to <EMAIL> --subject <SUBJECT> --body <TEXT>
```

| Flag | Required | Description |
|------|----------|-------------|
| `--to` | Yes | Recipient email |
| `--subject` | Yes | Email subject |
| `--body` | Yes | Plain text body |

For HTML, attachments, or CC/BCC, use the raw API: `gws gmail users messages send --json '...'`

> **Write command** -- confirm with the user before executing.

### Triage Inbox

```bash
gws gmail +triage
gws gmail +triage --max 5 --query 'from:boss'
gws gmail +triage --labels --format table
```

| Flag | Default | Description |
|------|---------|-------------|
| `--max` | 20 | Maximum messages to show |
| `--query` | is:unread | Gmail search query |
| `--labels` | off | Include label names |

Read-only -- never modifies your mailbox.

### Watch for New Emails

```bash
gws gmail +watch --project <GCP_PROJECT_ID>
gws gmail +watch --project my-project --label-ids INBOX --once
gws gmail +watch --project my-project --cleanup --output-dir ./emails
```

| Flag | Default | Description |
|------|---------|-------------|
| `--project` | -- | GCP project ID for Pub/Sub |
| `--subscription` | -- | Existing Pub/Sub subscription |
| `--label-ids` | -- | 
