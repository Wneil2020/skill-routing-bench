---
name: workflow-miner
description: "Use when Mine agent transcript files (.jsonl) to discover frequent workflow patterns using Sequential Pattern Mining (SPM). Use when the user asks to \"mine: covers miner, frequent, jsonl, mining, spm"
metadata:
  holon-triggers: |
    mine workflows
    discover patterns
---

---
name: workflow-miner
description: >-
  Mine agent transcript files (.jsonl) to discover frequent workflow patterns
  using Sequential Pattern Mining (SPM). Use when the user asks to "mine
  workflows", "discover patterns", "workflow miner", "transcript mining",
  "워크플로우 마이닝", "패턴 발견", "세션 분석", "autoskill patterns", or wants to
  auto-synthesize optimized workflows from interaction traces. Do NOT use for
  creating skills from scratch (use create-skill), transcript reading for
  context recall (use recall), or general code review.
metadata:
  author: thaki
  version: "0.1.0"
  category: self-improvement
---

# Workflow Miner

Mines agent transcript files (.jsonl) to discover frequent workflow patterns using Sequential Pattern Mining (SPM). Based on AgentOS paper's concept of mining interaction traces to auto-synthesize optimized workflows.

## Instructions

### 1. Parse Agent Transcripts

- Source: transcript JSONL files under `/Users/hanhyojung/.cursor/projects/*/agent-transcripts/**/*.jsonl`
- Each line is a JSON object with `role` ("user" | "assistant") and `message.content` (array of blocks)
- Group events by session (one JSONL file per session)

### 2. Extract Tool-Call Sequences

- For each assistant message, iterate `message.content` and collect items with `type === "tool_use"`
- Extract `name` field (e.g. Read, Grep, WebSearch, StrReplace, Shell) to build ordered sequences
- Preserve order within a turn; concatenate across turns in temporal order
- Result: one sequence of tool names per session (e.g. `["Read","Read","Grep","StrReplace","Read"]`)

### 3. Find Frequent Subsequences (Simplified PrefixSpan)

- Use a sliding-window approach (no external SPM library)
- For window sizes 2..N (default N=6), enumerate all contiguous substrings from each session sequence
- Count frequency of each unique subsequence across all sessions
- A subsequence is frequent if its count ≥ minimum support (default: 3)
- See `references/mining-methodology.md` for algorithm detai
