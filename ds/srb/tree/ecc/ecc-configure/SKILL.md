---
name: ecc-configure
description: "Use when Configure and customize Everything Claude Code skills for a specific project. Guides through selecting relevant skills, installing rules: covers ecc, configure, ECC 설정, ECC 구성, installing"
metadata:
  holon-triggers: |
    setting up ECC skills for a new project
    auditing existing ECC configuration
---

---
name: ecc-configure
description: >-
  Configure and customize Everything Claude Code skills for a specific project.
  Guides through selecting relevant skills, installing rules, verifying paths,
  and optimizing installed files. Use when setting up ECC skills for a new
  project or auditing existing ECC configuration. Do NOT use for general skill
  creation (use anthropic-skill-creator). Do NOT use for Cursor settings (use
  update-cursor-settings). Korean triggers: "ECC 설정", "ECC 구성".
metadata:
  author: "ecc"
  version: "1.0.0"
  category: "engineering"
origin: ECC
---
# Configure Everything Claude Code (ECC)

An interactive, step-by-step installation wizard for the Everything Claude Code project. Uses `AskUserQuestion` to guide users through selective installation of skills and rules, then verifies correctness and offers optimization.

## When to Activate

- User says "configure ecc", "install ecc", "setup everything claude code", or similar
- User wants to selectively install skills or rules from this project
- User wants to verify or fix an existing ECC installation
- User wants to optimize installed skills or rules for their project

## Prerequisites

This skill must be accessible to Claude Code before activation. Two ways to bootstrap:
1. **Via Plugin**: `/plugin install everything-claude-code` — the plugin loads this skill automatically
2. **Manual**: Copy only this skill to `~/.claude/skills/configure-ecc/SKILL.md`, then activate by saying "configure ecc"

---

## Step 0: Clone ECC Repository

Before any installation, clone the latest ECC source to `/tmp`:

```bash
rm -rf /tmp/everything-claude-code
git clone https://github.com/affaan-m/everything-claude-code.git /tmp/everything-claude-code
```

Set `ECC_ROOT=/tmp/everything-claude-code` as the source for all subsequent copy operations.

If the clone fails (network issues, etc.), use `AskUserQuestion` to ask the user to provide a local path to an existing ECC clone.

---

## Step 1: Choose Installation 
