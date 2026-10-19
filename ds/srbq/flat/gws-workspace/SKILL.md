---
name: gws-workspace
description: "Use when Install, authenticate, and configure the Google Workspace CLI (gws) for controlling Gmail, Drive, Calendar, Sheets, Docs, and Chat from: covers gws, workspace, 구글 워크스페이스, gws 설정, controlling"
metadata:
  holon-triggers: |
    set up gws
    configure Google Workspace CLI
---

---
name: gws-workspace
description: >-
  Install, authenticate, and configure the Google Workspace CLI (gws) for
  controlling Gmail, Drive, Calendar, Sheets, Docs, and Chat from the terminal.
  Use when the user asks to set up gws, configure Google Workspace CLI,
  authenticate with Google, or start the gws MCP server. Do NOT use for
  service-specific operations (use gws-gmail, gws-drive, gws-calendar,
  gws-sheets, gws-docs, or gws-chat instead). Korean triggers: "구글 워크스페이스", "gws 설정".
metadata:
  author: "googleworkspace/cli (adapted)"
  version: "1.0.0"
  category: "integration"
---
# Google Workspace CLI — Setup & Reference

One CLI for all of Google Workspace. Built for humans and AI agents.

> For full CLI context and agent rules, see [references/context.md](references/context.md).
> For a quick command cheatsheet, see [references/cli-cheatsheet.md](references/cli-cheatsheet.md).

## Installation

```bash
npm install -g @googleworkspace/cli
```

Verify: `gws --version`

Pre-built binaries also available on [GitHub Releases](https://github.com/googleworkspace/cli/releases).

## Authentication

### Interactive (recommended)

```bash
gws auth setup      # one-time: creates GCP project, enables APIs, logs in (requires gcloud)
gws auth login      # subsequent logins with scope selection
```

For unverified apps (testing mode), select individual service scopes:

```bash
gws auth login --scopes drive,gmail,calendar
```

### Multiple Accounts

```bash
gws auth login --account work@corp.com
gws auth login --account personal@gmail.com
gws auth list
gws auth default work@corp.com
gws --account personal@gmail.com drive files list
```

### Headless / CI

```bash
gws auth export --unmasked > credentials.json
export GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE=/path/to/credentials.json
```

### Service Account

```bash
export GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE=/path/to/service-account.json
export GOOGLE_WORKSPACE_CLI_IMPERSONATED_USER=admin@example.com  # for domain-wide dele
