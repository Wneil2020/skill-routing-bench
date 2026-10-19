---
name: paperclip-tasks
description: "Use when Create, assign, track, and manage Paperclip tasks (issues) with atomic checkout, delegation, and status transitions. Use when the user: covers paperclip, tasks, checkout, transitions, atomic"
metadata:
  holon-triggers: |
    create a paperclip task
    list tasks
---

---
name: paperclip-tasks
description: >-
  Create, assign, track, and manage Paperclip tasks (issues) with atomic
  checkout, delegation, and status transitions. Use when the user asks to
  "create a paperclip task", "list tasks", "assign task", "checkout issue",
  "update task status", "delegate work", "paperclip issue", "페이퍼클립 작업",
  "태스크 생성", "이슈 체크아웃", "태스크 할당", "작업 위임", "이슈 목록",
  or any Paperclip issue management operation. Do NOT use for company/agent/goal
  management (use paperclip-control). Do NOT use for agent creation or heartbeats
  (use paperclip-agents). Do NOT use for installation (use paperclip-setup).
metadata:
  author: thaki
  version: "1.0.0"
  category: execution
---

# Paperclip Tasks — Issue Management

Manage the full lifecycle of Paperclip issues: create, assign, checkout, update, comment, delegate, and release.

## Prerequisites

- Paperclip server running (default `http://localhost:3100`). If not running, see `paperclip-setup`.
- CLI available via `pnpm paperclipai` from `~/work/thakicloud/paperclip/`
- Context profile configured with `company-id`. See `paperclip-control` for environment setup.
- Set `API_BASE` and `API_KEY` env vars for curl examples (see `paperclip-control`).

## Issue Lifecycle

Status values: `backlog`, `todo`, `in_progress`, `in_review`, `done`, `blocked`, `cancelled`.
Priority values: `critical`, `high`, `medium`, `low`.

For the full lifecycle diagram, blocked task protocol, and comment conventions, see `references/issue-lifecycle.md`.

## Workflow

### 1. List Issues

```bash
pnpm paperclipai issue list --company-id <company-id> \
  [--status todo,in_progress] \
  [--assignee-agent-id <agent-id>] \
  [--match "search text"]
```

Search with the `q` parameter via REST:

```bash
curl -sS "$API_BASE/api/companies/<company-id>/issues?q=dockerfile&status=todo" \
  -H "Authorization: Bearer $API_KEY"
```

### 2. Get Issue Details

```bash
pnpm paperclipai issue get <issue-id-or-identifier>
```

Returns: issue fields, p
