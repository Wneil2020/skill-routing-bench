---
name: gws-email-reply
description: "Use when Compose and send email replies via Google Workspace CLI with AI-drafted responses, knowledge-based context retrieval, brand voice enforcement: covers gws, email, reply, continuation, han"
metadata:
  holon-triggers: |
    reply to email
    answer this email
---

---
name: gws-email-reply
description: >-
  Compose and send email replies via Google Workspace CLI with AI-drafted
  responses, knowledge-based context retrieval, brand voice enforcement, and
  mandatory sentence polishing. Supports replying to specific emails by message
  ID, thread continuation, and batch reply to unread reply-needed emails. User
  identity: hyojung.han@thakicloud.co.kr. Use when the user asks to "reply to
  email", "answer this email", "이메일 답장", "메일 답장", "reply-email",
  "gws email reply", "이 메일에 답장해줘", "메일 답장 써줘", or wants to compose
  a reply to a specific Gmail message. Do NOT use for email triage without
  replies (use gmail-daily-triage), calendar-related email actions (use
  gws-calendar or smart-meeting-scheduler), Slack messaging (use
  kwp-slack-slack-messaging), auto-reply without human gate (use
  email-auto-reply), or sending new emails without a reply context (use
  gws-gmail directly).
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "comms-automation"
---
# GWS Email Reply

AI-drafted email replies via Google Workspace CLI with context retrieval, brand voice, and mandatory sentence polishing.

## User Identity

```
Email: hyojung.han@thakicloud.co.kr
Display Name: 한효정 (Hyojung Han)
Organization: ThakiCloud
Default Language: Korean (English for technical terms)
```

## Composed Skills

| Skill | Role | Step |
|-------|------|------|
| `gws-gmail` | Read emails, send replies | 1, 7 |
| `recall` | Cross-session context retrieval | 3 |
| `cognee` | Knowledge graph for sender/topic context | 3 |
| `kwp-customer-support-response-drafting` | Response structure and tone templates | 4 |
| `kwp-brand-voice-brand-voice-enforcement` | Brand voice consistency | 4 |
| `sentence-polisher` | Grammar and sentence quality (MANDATORY) | 5 |
| `gmail-daily-triage` | Email classification patterns | 2 |
| `smart-meeting-scheduler` | Route meeting-related replies | 2 |

## Workflow

### Step 1: Fetch Target Email

**If message ID provided:**


