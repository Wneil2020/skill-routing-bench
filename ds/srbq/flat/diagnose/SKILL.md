---
name: diagnose
description: "Use when Run 3 parallel analysis agents (Root Cause, Error Context, Impact) to diagnose bugs, errors, and performance issues, then synthesize findings into a: covers diagnose, 진단, 리뷰, debug, why"
metadata:
  holon-triggers: |
    find the bug
    debug this
---

---
name: diagnose
description: >-
  Run 3 parallel analysis agents (Root Cause, Error Context, Impact) to
  diagnose bugs, errors, and performance issues, then synthesize findings into a
  single root cause and apply a fix. Use when the user runs /diagnose, asks to
  "find the bug", "debug this", "why is this failing", "root cause analysis", or
  "diagnose the error". Do NOT use for code review (use /simplify or
  /deep-review), new feature work, or general Q&A. Korean triggers: "진단", "리뷰",
  "디버깅", "수정".
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "execution"
---
# Diagnose — Root Cause Analysis and Fix

When something is broken, run 3 parallel analysis agents to find the root cause from different angles, synthesize a diagnosis, and apply a fix.

## Usage

```
/diagnose                              # analyze current error/issue in context
/diagnose "TypeError in auth module"   # diagnose specific error message
/diagnose src/api/auth.ts              # diagnose specific file
/diagnose --no-fix                     # analysis only, no auto-fix
```

## Workflow

### Step 1: Gather Error Context

Collect all available evidence:

1. **Linter errors**: Run `ReadLints` on relevant files
2. **Recent changes**: `git diff HEAD` and `git log --oneline -5`
3. **Error message**: From user input or terminal output
4. **Related files**: Read files mentioned in error traces or user input
5. **Git blame**: Check who last modified the problematic lines

If the user provides an error message, extract: file path, line number, error type, and stack trace.

### Step 2: Launch 3 Parallel Analysis Agents

Use the Task tool to spawn 3 sub-agents. Each receives the full error context.

For detailed prompts, see [references/agent-prompts.md](references/agent-prompts.md).

```
Agent 1: Root Cause Agent      → 5 Whys, systems thinking, dependency tracing
Agent 2: Error Context Agent   → Stack trace analysis, error patterns, related code
Agent 3: Impact Agent          → Side effec
