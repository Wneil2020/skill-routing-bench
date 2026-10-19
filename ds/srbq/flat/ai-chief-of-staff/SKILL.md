---
name: ai-chief-of-staff
description: "Use when Personal AI assistant that combines Gmail, Calendar, and Drive data into actionable briefings via gwcli. Three sub-workflows, Morning Sweep: covers chief, staff, assistant, gwcli, combines"
metadata:
  holon-triggers: |
    morning sweep
    morning briefing
---

---
name: ai-chief-of-staff
description: >-
  Personal AI assistant that combines Gmail, Calendar, and Drive data into
  actionable briefings via gwcli. Three sub-workflows: Morning Sweep (email
  triage + today's calendar + task classification), Meeting Prep (attendee
  context + related docs), and Weekly Digest (weekly calendar + email overview).
  Use when the user asks for "morning sweep", "morning briefing", "daily
  briefing", "meeting prep", "weekly digest", "weekly summary", "start my day",
  "prep my meeting", "what's on my plate", or "아침 브리핑", "미팅 준비", "주간 요약". Do NOT
  use for single-service operations (use gwcli directly).
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "execution"
---
# AI Chief of Staff -- Personal Assistant

A personal AI assistant inspired by Jim Prosser's Claude Code "Chief of Staff" system. Combines Gmail, Calendar, and Drive data into structured, actionable briefings using `gwcli` (google-workspace-cli).

> **Prerequisites**: `gwcli` must be installed and authenticated with a profile. See [gwcli setup](https://github.com/ianpatrickhines/google-workspace-cli).

## Sub-Skill Index

| Sub-Skill | When to Use | Reference |
|-----------|-------------|-----------|
| morning-sweep | "Morning briefing", "start my day", daily triage | [references/morning-sweep.md](references/morning-sweep.md) |
| meeting-prep | "Prep my meeting", "meeting prep", next meeting context | [references/meeting-prep.md](references/meeting-prep.md) |
| weekly-digest | "Weekly summary", "weekly digest", Monday planning | [references/weekly-digest.md](references/weekly-digest.md) |

## gwcli Command Reference

For the full command reference with Gmail, Calendar, Drive, and Profile commands, see [references/gwcli-reference.md](references/gwcli-reference.md). Key pattern: always use `--format json` for structured agent-parseable output.

## Workflow

1. **Route**: Match user intent to one sub-skill from the index.
2. **Read**: Load `references/<sub-skill>.m
