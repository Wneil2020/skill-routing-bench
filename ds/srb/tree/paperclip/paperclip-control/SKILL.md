---
name: paperclip-control
description: "Use when Interact with the Paperclip control plane to manage companies, goals, approvals, and dashboard overview. Use when the user asks to: covers paperclip, control, plane, approvals, approve"
metadata:
  holon-triggers: |
    check paperclip status
    list companies
---

---
name: paperclip-control
description: >-
  Interact with the Paperclip control plane to manage companies, goals,
  approvals, and dashboard overview. Use when the user asks to "check
  paperclip status", "list companies", "approve agent hire", "view org chart",
  "paperclip dashboard", "view costs", "paperclip approve", "페이퍼클립 상태",
  "회사 목록", "에이전트 승인", "paperclip 비용", "예산 조회", "활동 로그",
  or any Paperclip governance and oversight task. Do NOT use for task/issue
  CRUD (use paperclip-tasks). Do NOT use for agent creation, heartbeats, agent
  budgets, or agent lifecycle (use paperclip-agents). Do NOT use for
  installation or deployment (use paperclip-setup).
metadata:
  author: thaki
  version: "1.0.0"
  category: execution
---

# Paperclip Control — Core Orchestration

Manage the Paperclip control plane: companies, agents, goals, approvals, costs, and dashboard overview.

## Prerequisites

- Paperclip server running (default `http://localhost:3100`). If not running, see `paperclip-setup`.
- CLI available via `pnpm paperclipai` from `~/work/thakicloud/paperclip/`
- Context profile configured (or use `--api-base` / `--company-id` flags)

## Environment

Set these before using curl examples:

```bash
export API_BASE="http://localhost:3100"
export API_KEY="<your-api-key>"  # or from context: pnpm paperclipai context show
```

Or configure a persistent context profile:

```bash
cd ~/work/thakicloud/paperclip
pnpm paperclipai context set --api-base http://localhost:3100 --company-id <company-id>
pnpm paperclipai context show
```

All CLI commands inherit `api-base` and `company-id` from the active context.

## Workflow

### 1. Dashboard Overview

```bash
pnpm paperclipai dashboard get --company-id <company-id>
```

Returns: agent count, active/paused/terminated counts, pending approvals, total spend, stale tasks, recent activity.

### 2. Company Management

```bash
pnpm paperclipai company list
pnpm paperclipai company get <company-id>
pnpm paperclipai company delete <
