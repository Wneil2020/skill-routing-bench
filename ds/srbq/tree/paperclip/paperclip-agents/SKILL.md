---
name: paperclip-agents
description: "Use when Create, configure, and operate Paperclip agents with heartbeat scheduling, budget enforcement, and runtime skill injection. Use when: covers paperclip, inject, budgets, heartbeat, operate"
metadata:
  holon-triggers: |
    create a paperclip agent
    hire an agent
---

---
name: paperclip-agents
description: >-
  Create, configure, and operate Paperclip agents with heartbeat scheduling,
  budget enforcement, and runtime skill injection. Use when the user asks to
  "create a paperclip agent", "hire an agent", "run heartbeat", "set agent
  budget", "inject skills", "pause agent", "resume agent", "에이전트 생성",
  "하트비트 실행", "예산 설정", "에이전트 예산", "에이전트 일시정지",
  "paperclip agent create", "paperclip heartbeat", or any agent lifecycle
  operation. Do NOT use for task/issue management (use paperclip-tasks). Do NOT
  use for company/goal/approval oversight or company budgets (use
  paperclip-control). Do NOT use for installation (use paperclip-setup).
metadata:
  author: thaki
  version: "1.0.0"
  category: execution
---

# Paperclip Agents — Agent Setup and Operations

Create agents, configure adapters, manage heartbeats, enforce budgets, and inject skills at runtime.

## Prerequisites

- Paperclip server running (default `http://localhost:3100`). If not running, see `paperclip-setup`.
- CLI available via `pnpm paperclipai` from `~/work/thakicloud/paperclip/`
- Context profile configured with `company-id`. See `paperclip-control` for environment setup.
- Set `API_BASE` and `API_KEY` env vars for curl examples (see `paperclip-control`).

## Agent Adapter Types

| Adapter | Description | Key Config |
|---------|-------------|------------|
| `process` | Spawn local child process | `command`, `args`, `cwd`, `env`, `timeoutSec` |
| `claude_local` | Claude Code local agent | `cwd`, `model`, `instructionsFilePath` |
| `codex_local` | OpenAI Codex local agent | `cwd`, `model` |
| `cursor_local` | Cursor agent (local) | `cwd`, `model` |
| `opencode_local` | OpenCode local agent | `cwd`, `model` |
| `http` | External webhook agent | `url`, `method`, `headers`, `payloadTemplate` |
| `openclaw` | OpenClaw SSE/webhook | `callbackUrl`, `paperclipApiUrl` |

Full JSON examples for each adapter: `references/adapter-configs.md`.

## Workflow

### 1. Discover Ada
