---
name: anthropic-mcp-builder
description: "Use when Build high-quality MCP (Model Context Protocol) servers that connect LLMs to external APIs and services. Use when building an MCP server: covers anthropic, mcp, builder, MCP 서버, MCP 빌드"
metadata:
  holon-triggers: |
    building an MCP server
    creating MCP tools
---

---
name: anthropic-mcp-builder
description: >-
  Build high-quality MCP (Model Context Protocol) servers that connect LLMs to
  external APIs and services. Use when building an MCP server, creating MCP
  tools, connecting an external API to an LLM, integrating a third-party service
  via MCP, or setting up MCP in Cursor. Supports Python (FastMCP) and
  Node/TypeScript (MCP SDK). Do NOT use for Claude API or Anthropic SDK
  integration (use anthropic-claude-api). Korean triggers: "MCP 서버", "MCP 빌드".
metadata:
  author: "anthropic"
  version: "1.1.0"
  upstream: "https://github.com/ComposioHQ/awesome-claude-skills/tree/master/mcp-builder"
  license: "Apache-2.0 — See LICENSE.txt in skill directory"
  category: "document"
---
# MCP Server Development Guide

## Overview

Create MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. The quality of an MCP server is measured by how well it enables LLMs to accomplish real-world tasks.

---

# Process

## High-Level Workflow

Creating a high-quality MCP server involves four main phases:

### Phase 1: Deep Research and Planning

#### 1.1 Understand Modern MCP Design

**API Coverage vs. Workflow Tools:**
Balance comprehensive API endpoint coverage with specialized workflow tools. Workflow tools can be more convenient for specific tasks, while comprehensive coverage gives agents flexibility to compose operations. Performance varies by client—some clients benefit from code execution that combines basic tools, while others work better with higher-level workflows. When uncertain, prioritize comprehensive API coverage.

**Tool Naming and Discoverability:**
Clear, descriptive tool names help agents find the right tools quickly. Use consistent prefixes (e.g., `github_create_issue`, `github_list_repos`) and action-oriented naming.

**Context Management:**
Agents benefit from concise tool descriptions and the ability to filter/paginate results. Design tools that return foc
