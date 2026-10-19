---
name: kwp-sync
description: "Use when Sync Anthropic Knowledge Work Plugins from GitHub to Cursor IDE rules. Use when the user asks to \"update KWP rules\", \"sync knowledge-work-plugins\": covers kwp, sync, 동기화, 최적화, plugins"
metadata:
  holon-triggers: |
    update KWP rules
    sync knowledge-work-plugins
---

---
name: kwp-sync
description: >-
  Sync Anthropic Knowledge Work Plugins from GitHub to Cursor IDE rules. Use
  when the user asks to "update KWP rules", "sync knowledge-work-plugins",
  "refresh KWP", "add a new KWP plugin", or "check for upstream KWP changes". Do
  NOT use for optimizing existing skills (use skill-optimizer) or creating new
  skills from scratch (use skill-creator). Korean triggers: "동기화", "최적화", "체크",
  "스킬".
metadata:
  version: "1.0.0"
  category: "execution"
  author: "anthropic-kwp"
---
# KWP Sync

Synchronize [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) into Cursor IDE skills (`.cursor/skills/kwp-*/SKILL.md`), commands (`.cursor/commands/kwp-*.md`), and the index rule (`.cursor/rules/kwp-index.mdc`). Supports full sync, incremental updates, and selective plugin import.

## Workflow

### Step 1: Clone or Pull Upstream

```bash
cd /tmp
if [ -d knowledge-work-plugins ]; then
  cd knowledge-work-plugins && git pull
else
  git clone --depth 1 https://github.com/anthropics/knowledge-work-plugins.git
fi
```

### Step 2: Detect Scope

Determine which plugins to sync. Available plugins (19 domains):

**Core plugins (14):** `bio-research`, `customer-support`, `data`, `design`, `engineering`, `enterprise-search`, `finance`, `human-resources`, `legal`, `marketing`, `operations`, `product-management`, `productivity`, `sales`

**Partner-built sub-plugins (4):** `apollo`, `brand-voice`, `common-room`, `slack` (nested under `partner-built/`)

**Meta plugin (1):** `cowork-plugin-management`

If user requests a full sync, process all 19. If selective, process only requested plugins.

### Step 3: Convert Skills and Commands

**Skills** (`{plugin}/skills/*/SKILL.md` -> `.cursor/skills/kwp-{domain}-{skill}/SKILL.md`):
1. Parse YAML frontmatter, extract `description`
2. Extract body content
3. Create skill directory with proper frontmatter (`name`, `description` with negative triggers, `metadata`)
4. Add `## Examples
