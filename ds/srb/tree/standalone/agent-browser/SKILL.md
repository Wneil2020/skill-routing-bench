---
name: agent-browser
description: "Use when Headless browser automation via the agent-browser CLI (v0.16.3). Navigates pages, fills forms, clicks elements, takes screenshots, extracts: covers browser, 브라우저, 테스트, allowed, allowlist"
metadata:
  holon-triggers: |
    automate a browser task
    test a web page
---

---
name: agent-browser
description: >-
  Headless browser automation via the agent-browser CLI (v0.16.3). Navigates
  pages, fills forms, clicks elements, takes screenshots, extracts data, diffs
  page states, records video, profiles performance, and manages sessions -- all
  from the terminal. Use when the user asks to "automate a browser task", "test
  a web page", "scrape data", "take a screenshot of a site", "fill out a form",
  "login to a website", "compare two pages", "visual diff", "record browser
  session", "profile page performance", "native mode browser", "stream browser",
  "iOS mobile testing", "auth vault", "cloud browser", or any task requiring
  programmatic browser interaction via CLI. Do NOT use for interactive MCP-based
  browser sessions (use cursor-ide-browser MCP instead), Playwright test suites
  (use webapp-testing skill), or general web fetching without browser rendering
  (use WebFetch). Korean triggers: "브라우저", "테스트", "성능", "스크래핑".
metadata:
  author: "thaki"
  version: "2.0.0"
  upstream: "vercel-labs/agent-browser@0.16.3"
  category: "execution"
---
# Agent Browser — CLI Browser Automation for AI Agents

Automate headless Chromium via the `agent-browser` CLI. Uses a snapshot-ref interaction pattern: navigate to a page, snapshot the accessibility tree to get element refs (`@e1`, `@e2`), then interact using those refs.

## Prerequisites

```bash
which agent-browser || npm install -g agent-browser
agent-browser install  # downloads Chromium (first time only)
```

## Core Workflow

Every browser automation follows this loop:

```
1. Navigate  →  agent-browser open <url>
2. Snapshot  →  agent-browser snapshot -i
3. Interact  →  agent-browser click @e1 / fill @e2 "text"
4. Re-snapshot after page changes
```

```bash
agent-browser open https://example.com/form
agent-browser snapshot -i
# Output: @e1 input "Email", @e2 input "Password", @e3 button "Submit"

agent-browser fill @e1 "user@example.com"
agent-browser fill @e2 "password123"
agent-br
