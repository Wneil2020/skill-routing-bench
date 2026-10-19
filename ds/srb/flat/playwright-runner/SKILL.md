---
name: playwright-runner
description: "Use when Run ad-hoc Playwright browser automation scripts with a universal Node.js executor. Detects local dev servers, writes scripts to /tmp, and: covers playwright, runner, 테스트, 설계, executor"
metadata:
  holon-triggers: |
    running quick browser tests
    ad-hoc page automation
---

---
name: playwright-runner
description: >-
  Run ad-hoc Playwright browser automation scripts with a universal Node.js
  executor. Detects local dev servers, writes scripts to /tmp, and provides
  helper utilities for common browser tasks (screenshots, form filling,
  responsive testing, link validation, login flows). Use when running quick
  browser tests, ad-hoc page automation, taking screenshots, testing responsive
  design, checking broken links, or automating form interactions. Do NOT use for
  project E2E test suites (use e2e-testing). Do NOT use for Python-based browser
  testing (use anthropic-webapp-testing). Do NOT use for CLI-based browser
  automation (use agent-browser). Korean triggers: "테스트", "설계", "체크", "자동화".
metadata:
  upstream: "https://github.com/lackeyjb/playwright-skill"
  version: "4.1.0"
  license: "MIT"
  category: "execution"
  author: "thaki"
---
# Playwright Runner — Ad-hoc Browser Automation

General-purpose browser automation via a universal Node.js executor. Write custom Playwright scripts, execute them from the skill directory, and get results in real-time with a visible browser window.

## Setup (First Time)

```bash
cd .cursor/skills/playwright-runner && npm run setup
```

This installs Playwright and Chromium. Only needed once.

## Critical Workflow

Follow these steps in order for every automation task:

### Step 1: Detect Dev Servers (for localhost testing)

```bash
cd .cursor/skills/playwright-runner && node -e "require('./lib/helpers').detectDevServers().then(s => console.log(JSON.stringify(s)))"
```

- 1 server found: Use it automatically
- Multiple found: Ask the user which one to test
- None found: Ask for a URL or offer to help start a dev server

### Step 2: Write Script to /tmp

Always write test files to `/tmp/playwright-test-*.js`. Never write to the skill directory or the user's project.

```javascript
// /tmp/playwright-test-page.js
const { chromium } = require('playwright');

const TARGET_URL = 'http://localhost:3
