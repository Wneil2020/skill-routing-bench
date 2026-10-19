---
name: proactive-meeting-scheduler
description: "Use when Detect implicit meeting requests in emails (\"let's discuss\", \"can we sync\", \"need to talk about\") and proactively propose meetings: covers proactive, meeting, scheduler, agendas, discuss"
metadata:
  holon-triggers: |
    detect meeting needs from email
    auto-schedule from inbox
---

---
name: proactive-meeting-scheduler
description: >-
  Detect implicit meeting requests in emails ("let's discuss", "can we sync",
  "need to talk about") and proactively propose meetings with context-derived
  agendas. Runs after gmail-daily-triage to identify emails that imply a
  meeting is needed. Use when the user asks to "detect meeting needs from
  email", "auto-schedule from inbox", "proactive meeting", "이메일에서 미팅 감지",
  "자동 미팅 제안", "proactive-meeting-scheduler", or wants meetings proposed
  from email context. Do NOT use for explicit meeting scheduling requests
  (use smart-meeting-scheduler), calendar management (use gws-calendar),
  or email triage without meetings (use gmail-daily-triage).
metadata:
  version: "1.0.0"
  category: "execution"
  author: "thaki"
---
# Proactive Meeting Scheduler

Scan processed emails for implicit meeting signals and automatically propose meetings with agendas derived from email context.

## When to Use

- After `gmail-daily-triage` completes — scan reply-needed emails for meeting signals
- As part of the Comms track in the daily pipeline
- When the user wants the system to detect meeting needs autonomously

## Meeting Signal Detection

### Explicit Signals (high confidence)
- "Let's schedule a meeting"
- "Can we set up a call?"
- "I'd like to discuss this in person"
- "Let's sync on this"

### Implicit Signals (medium confidence)
- "We need to talk about..."
- "Can you walk me through..."
- "I have concerns about..."
- "This needs more discussion"
- Long email thread (> 5 replies) without resolution

### Korean Signals
- "미팅을 잡아주세요"
- "한번 얘기해 봐요"
- "회의가 필요할 것 같습니다"
- "논의가 필요합니다"
- "통화 가능하신가요"

## Workflow

### Step 1: Scan Triage Results

Read the output of `gmail-daily-triage` — specifically the "reply-needed" emails:

```bash
gws gmail list --label reply-needed --after yesterday --format json
```

### Step 2: Detect Meeting Signals

For each reply-needed email, analyze with LLM:
- Does this email imply a meeting is neede
