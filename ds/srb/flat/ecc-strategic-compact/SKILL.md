---
name: ecc-strategic-compact
description: "Use when Suggests context compaction at logical workflow boundaries (after research, after debugging, before new phase) rather than arbitrary: covers ecc, strategic, compact, 컨텍스트 압축, 컴팩션"
metadata:
  holon-triggers: |
    running long sessions
    switching task phases
---

---
name: ecc-strategic-compact
description: >-
  Suggests context compaction at logical workflow boundaries (after research,
  after debugging, before new phase) rather than arbitrary auto-compaction.
  Includes a decision guide for when to compact and what survives. Use when
  running long sessions, switching task phases, or approaching context limits.
  Do NOT use for short single-task sessions. Do NOT use for memory persistence
  (use recall or context-engineer). Korean triggers: "컨텍스트 압축", "컴팩션".
metadata:
  author: "ecc"
  version: "1.0.0"
  category: "engineering"
origin: ECC
---
# Strategic Compact Skill

Suggests manual `/compact` at strategic points in your workflow rather than relying on arbitrary auto-compaction.

## When to Activate

- Running long sessions that approach context limits (200K+ tokens)
- Working on multi-phase tasks (research → plan → implement → test)
- Switching between unrelated tasks within the same session
- After completing a major milestone and starting new work
- When responses slow down or become less coherent (context pressure)

## Why Strategic Compaction?

Auto-compaction triggers at arbitrary points:
- Often mid-task, losing important context
- No awareness of logical task boundaries
- Can interrupt complex multi-step operations

Strategic compaction at logical boundaries:
- **After exploration, before execution** — Compact research context, keep implementation plan
- **After completing a milestone** — Fresh start for next phase
- **Before major context shifts** — Clear exploration context before different task

## How It Works

The `suggest-compact.js` script runs on PreToolUse (Edit/Write) and:

1. **Tracks tool calls** — Counts tool invocations in session
2. **Threshold detection** — Suggests at configurable threshold (default: 50 calls)
3. **Periodic reminders** — Reminds every 25 calls after threshold

## Hook Setup

Add to your `~/.claude/settings.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "match
