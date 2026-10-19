---
name: anthropic-claude-api
description: "Use when Build apps with the Claude API or Anthropic SDK. Use when code imports anthropic/@anthropic-ai/sdk/claude_agent_sdk, or user asks to: covers anthropic, claude, api, Claude API, Anthropic SDK"
metadata:
  holon-triggers: |
    code imports anthropic/@anthropic-ai/sdk/claude_agent_sdk
    user asks to use Claude API
---

---
name: anthropic-claude-api
description: >-
  Build apps with the Claude API or Anthropic SDK. Use when code imports
  anthropic/@anthropic-ai/sdk/claude_agent_sdk, or user asks to use Claude API,
  Anthropic SDKs, or Agent SDK. Do NOT use for MCP server development (use
  anthropic-mcp-builder). Korean triggers: "Claude API", "Anthropic SDK".
metadata:
  author: "anthropic"
  version: "1.0.0"
  license: "Complete terms in LICENSE.txt"
  category: "document"
---
# Building LLM-Powered Applications with Claude

This skill helps you build LLM-powered applications with Claude. Choose the right surface based on your needs, detect the project language, then read the relevant language-specific documentation.

## Defaults

Unless the user requests otherwise:

For the Claude model version, please use Claude Opus 4.6, which you can access via the exact model string `claude-opus-4-6`. Please default to using adaptive thinking (`thinking: {type: "adaptive"}`) for anything remotely complicated. And finally, please default to streaming for any request that may involve long input, long output, or high `max_tokens` — it prevents hitting request timeouts. Use the SDK's `.get_final_message()` / `.finalMessage()` helper to get the complete response if you don't need to handle individual stream events

---

## Language Detection

Before reading code examples, determine which language the user is working in:

1. **Look at project files** to infer the language:

   - `*.py`, `requirements.txt`, `pyproject.toml`, `setup.py`, `Pipfile` → **Python** — read from `python/`
   - `*.ts`, `*.tsx`, `package.json`, `tsconfig.json` → **TypeScript** — read from `typescript/`
   - `*.js`, `*.jsx` (no `.ts` files present) → **TypeScript** — JS uses the same SDK, read from `typescript/`
   - `*.java`, `pom.xml`, `build.gradle` → **Java** — read from `java/`
   - `*.kt`, `*.kts`, `build.gradle.kts` → **Java** — Kotlin uses the Java SDK, read from `java/`
   - `*.scala`, `build.sbt` → **Java** — Scal
