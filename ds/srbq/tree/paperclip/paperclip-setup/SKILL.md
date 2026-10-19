---
name: paperclip-setup
description: "Use when Install, configure, and deploy Paperclip instances for AI agent orchestration. Use when the user asks to \"install paperclip\", \"set up: covers paperclip, setup, onboard, deploy, instances"
metadata:
  holon-triggers: |
    install paperclip
    set up paperclip
---

---
name: paperclip-setup
description: >-
  Install, configure, and deploy Paperclip instances for AI agent orchestration.
  Use when the user asks to "install paperclip", "set up paperclip", "configure
  paperclip", "deploy paperclip", "paperclip doctor", "start paperclip",
  "stop paperclip", "페이퍼클립 설치", "페이퍼클립 설정", "설정 확인",
  "paperclip onboard", "paperclip docker", or any installation, configuration,
  or deployment task. Do NOT use for runtime operations like task management
  (use paperclip-tasks), agent operations (use paperclip-agents), or governance
  (use paperclip-control).
metadata:
  author: thaki
  version: "1.0.0"
  category: execution
---

# Paperclip Setup — Installation and Configuration

Install, configure, and deploy Paperclip AI agent orchestration platform.

## Prerequisites

| Requirement | Version |
|-------------|---------|
| Node.js | >= 20 |
| pnpm | >= 9.15 |
| PostgreSQL | 17 (or use embedded PGlite) |

## Installation Methods

### Method 1: Quick Install (Recommended)

```bash
npx paperclipai onboard --yes
```

This auto-detects the environment, sets up embedded PostgreSQL, and starts the server.

### Method 2: Manual Clone

```bash
git clone https://github.com/paperclipai/paperclip.git ~/work/thakicloud/paperclip
cd ~/work/thakicloud/paperclip
pnpm install --no-frozen-lockfile
pnpm dev
```

### Method 3: Docker Compose (Quickstart)

```bash
cd ~/work/thakicloud/paperclip
docker compose -f docker-compose.quickstart.yml up -d
```

Uses embedded PostgreSQL, requires `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `BETTER_AUTH_SECRET` in `.env`.

### Method 4: Docker Compose (Production)

```bash
cd ~/work/thakicloud/paperclip
docker compose up -d
```

Uses external PostgreSQL 17, configures `PAPERCLIP_DEPLOYMENT_MODE=authenticated` and `PAPERCLIP_DEPLOYMENT_EXPOSURE=private`.

## Configuration

### Server Configuration

```bash
cd ~/work/thakicloud/paperclip
pnpm paperclipai configure --section server
pnpm paperclipai configure --section storage
p
