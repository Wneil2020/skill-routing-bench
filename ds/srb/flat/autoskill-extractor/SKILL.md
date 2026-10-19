---
name: autoskill-extractor
description: "Use when Extract reusable skill candidates from Cursor agent transcripts by analyzing user interaction patterns, corrections, and: covers autoskill, extractor, durable, preferences, corrections"
metadata:
  holon-triggers: |
    extract skills from sessions
    mine transcripts for skills
---

---
name: autoskill-extractor
description: >-
  Extract reusable skill candidates from Cursor agent transcripts by analyzing
  user interaction patterns, corrections, and durable preferences. Use when the
  user asks to "extract skills from sessions", "mine transcripts for skills",
  "autoskill extract", "find reusable patterns", "스킬 추출", "세션에서 스킬 추출",
  "트랜스크립트 마이닝", or when invoked by autoskill-evolve. Do NOT use for
  creating skills from scratch (use create-skill), optimizing existing skills
  (use skill-optimizer), or general transcript reading (use recall).
metadata:
  author: thaki
  version: "0.1.0"
  category: self-improvement
---

# AutoSkill Extractor

Extract reusable skill candidates from Cursor agent transcripts by analyzing user interaction patterns, corrections, and durable preferences. Adapts AutoSkill's P_ext methodology for the Cursor SKILL.md ecosystem.

## Instructions

### Input

The extractor accepts one of:
- A transcript JSONL file path from `~/.cursor/projects/*/agent-transcripts/*.jsonl`
- A session ID (UUID) to locate the transcript automatically
- `--scope recent` to process the 5 most recent transcripts
- An optional `--hint "focus area"` to guide extraction

### Extraction Process

1. **Load Transcript**: Read the JSONL file. Each line is a structured JSON event containing user messages, assistant responses, and tool calls.

2. **Identify User Evidence**: Extract only from USER turns. Assistant turns provide context but are never source-of-truth for skill requirements. Focus on:
   - Explicit reusable constraints (style, format, audience, conventions)
   - User corrections that encode durable preferences
   - Multi-step workflow specifications
   - Schema/template requirements
   - Implementation policies and rules

3. **Apply Extraction Criteria**:

   **DO Extract**:
   - Repeated corrections across sessions → durable preference
   - Explicit "always do X" / "never do Y" instructions
   - Multi-step workflows the user specified
   - 
