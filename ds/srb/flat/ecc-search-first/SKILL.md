---
name: ecc-search-first
description: "Use when Research-before-coding workflow — always search for existing tools, libraries, and patterns before writing custom code. Invokes web search and: covers ecc, search, first, 검색 우선, 기존 도구 탐색"
metadata:
  holon-triggers: |
    starting a new feature
    adding a dependency
---

---
name: ecc-search-first
description: >-
  Research-before-coding workflow — always search for existing tools,
  libraries, and patterns before writing custom code. Invokes web search and
  codebase search before implementation. Use when starting a new feature, adding
  a dependency, or solving a problem that likely has existing solutions. Do NOT
  use for known implementations. Do NOT use for general web search (use
  WebSearch directly). Korean triggers: "검색 우선", "기존 도구 탐색".
metadata:
  author: "ecc"
  version: "1.0.0"
  category: "engineering"
origin: ECC
---
# /search-first — Research Before You Code

Systematizes the "search for existing solutions before implementing" workflow.

## Trigger

Use this skill when:
- Starting a new feature that likely has existing solutions
- Adding a dependency or integration
- The user asks "add X functionality" and you're about to write code
- Before creating a new utility, helper, or abstraction

## Workflow

```
┌─────────────────────────────────────────────┐
│  1. NEED ANALYSIS                           │
│     Define what functionality is needed      │
│     Identify language/framework constraints  │
├─────────────────────────────────────────────┤
│  2. PARALLEL SEARCH (researcher agent)      │
│     ┌──────────┐ ┌──────────┐ ┌──────────┐  │
│     │  npm /   │ │  MCP /   │ │  GitHub / │  │
│     │  PyPI    │ │  Skills  │ │  Web      │  │
│     └──────────┘ └──────────┘ └──────────┘  │
├─────────────────────────────────────────────┤
│  3. EVALUATE                                │
│     Score candidates (functionality, maint, │
│     community, docs, license, deps)         │
├─────────────────────────────────────────────┤
│  4. DECIDE                                  │
│     ┌─────────┐  ┌──────────┐  ┌─────────┐  │
│     │  Adopt  │  │  Extend  │  │  Build   │  │
│     │ as-is   │  │  /Wrap   │  │  Custom  │  │
│     └─────────┘  └──────────┘  └─────────┘  │
├─────────────────────────────────────────────┤
│  5. IMPLEMENT   
