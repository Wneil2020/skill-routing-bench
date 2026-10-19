---
name: slack-agent
description: "Use when Build and deploy Slack bots/agents using Bolt for JavaScript or Express. Guides through project setup, Slack app creation, environment configuration: covers slack, 슬랙 봇, 봇 만들기, bolt, bots"
metadata:
  holon-triggers: |
    build a Slack bot
    create a Slack agent
---

---
name: slack-agent
description: >-
  Build and deploy Slack bots/agents using Bolt for JavaScript or Express.
  Guides through project setup, Slack app creation, environment configuration,
  local testing, and production deployment via an interactive wizard. Deployment
  target is user's choice: Docker/K8s, serverless, PaaS, or any Node.js host.
  Use when the user asks to "build a Slack bot", "create a Slack agent", "deploy
  a Slack app", "slack-agent", or mentions Slack bot development. Do NOT use for
  general Slack messaging (use kwp-slack-slack-messaging), Slack search (use
  kwp-slack-slack-search). Korean triggers: "슬랙 봇", "봇 만들기", "슬랙 앱".
metadata:
  author: "thaki"
  version: "2.0.0"
  category: "execution"
---
# Slack Agent Development

Build Slack bots and AI agents with the official Slack SDK. Framework-agnostic deployment — run on Docker, Kubernetes, serverless, PaaS, or any Node.js host.

## Supported Frameworks

| Aspect | Bolt for JavaScript (Recommended) | Express + Web API |
|--------|-----------------------------------|-------------------|
| **Best for** | Most projects, event-driven bots | Simple webhook-only bots |
| **Package** | `@slack/bolt` | `express` + `@slack/web-api` |
| **Events** | `app.event()`, `app.command()`, `app.action()` | Manual webhook handler |
| **Messages** | `client.chat.postMessage(...)` | `web.chat.postMessage(...)` |
| **UI** | Block Kit JSON via Bolt helpers | Raw Block Kit JSON |
| **Socket Mode** | Built-in support | Manual implementation |
| **Complexity** | Low — handles auth, retry, ack automatically | Higher — manual signature verification |

**Bolt is recommended** for all new projects. It handles signature verification, event acknowledgment (3-second rule), retry logic, and middleware automatically.

## Command Routing

When invoked via `/slack-agent`, check for arguments:

| Argument | Action |
|----------|--------|
| `new` | Start wizard Phase 1: ask what agent to build, generate plan |
| `configure` | St
