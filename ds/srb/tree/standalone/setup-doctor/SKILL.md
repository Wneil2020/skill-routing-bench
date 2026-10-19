---
name: setup-doctor
description: "Use when Scan system prerequisites, environment variables, CLI tools, Python/Node packages, and MCP servers required by all project skills, then: covers setup, doctor, diagnostic, variables, groups"
metadata:
  holon-triggers: |
    check setup
    setup doctor
---

---
name: setup-doctor
description: >-
  Scan system prerequisites, environment variables, CLI tools, Python/Node
  packages, and MCP servers required by all project skills, then produce a
  diagnostic pass/fail report and optionally install missing dependencies.
  Use when the user asks to "check setup", "setup doctor", "verify
  prerequisites", "install dependencies", "check environment", "what's
  missing", "설치 확인", "환경 점검", "의존성 확인", "셋업 닥터",
  or wants to validate that the system is ready to run specific skill groups.
  Do NOT use for creating new skills (use create-skill). Do NOT use for
  running the daily pipeline (use today). Do NOT use for individual tool
  setup guides (use gws-workspace, paperclip-setup, etc. directly).
metadata:
  author: "thaki"
  version: "2.0.0"
  category: "infrastructure"
---

# Setup Doctor

Diagnose and fix missing prerequisites across all project skill groups. Organizes checks by **capability group** (21 functional clusters) rather than 400+ individual skills.

## Input

The user provides:
1. **Mode** (optional) — parsed from `$ARGUMENTS`:
   - *(no args)* — Full scan of all capability groups
   - `--group <name>` — Check a single group (e.g., `--group slack`)
   - `--fix` — Auto-install missing items where safe (brew/pip/npm)
   - `--env` — Environment variable check only
   - `--report` — Generate a markdown report file at `outputs/setup-doctor-report.md`
   - `--slack` — Post the report to Slack `#효정-할일` after scanning

## Capability Groups

| Group | Key Prerequisites | Dependent Skills |
|-------|-------------------|------------------|
| core-platform | PostgreSQL, Redis, Python backend deps | today, daily-stock-check, tab-*, weekly-stock-update |
| llm-apis | OPENAI_API_KEY, ANTHROPIC_API_KEY | today, paper-review, alphaear-*, trading-* |
| slack | SLACK_BOT_TOKEN, plugin-slack-slack MCP | today, x-to-slack, eod-ship, morning-ship |
| notion | NOTION_TOKEN, plugin-notion-workspace-notion MCP | md-to-notion, notion-docs-syn
