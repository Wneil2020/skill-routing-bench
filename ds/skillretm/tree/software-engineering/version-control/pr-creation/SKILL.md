---
name: "pr-creation"
description: "Use when the task involves deploy code: covers creation, default., review, drafts, body"
---

# pr-creation

MUST be used when creating pull requests. Handles context gathering, title generation (conventional commit format), body formatting, and PR creation via GitHub CLI. Creates PRs as drafts by default. Triggers on: 'create PR', 'open PR', 'ready for review', 'push for PR', 'send for review'.
