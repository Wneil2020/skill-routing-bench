---
name: kwp-cowork-create-plugin
description: "Use when Guide users through creating a new plugin from scratch in a cowork session. Use when users want to create a plugin, build a plugin, make a new plugin: covers kwp, cowork, create, 생성, 빌드"
metadata:
  holon-triggers: |
    users want to create a plugin
    build a plugin
---

---
name: kwp-cowork-create-plugin
description: >-
  Guide users through creating a new plugin from scratch in a cowork session.
  Use when users want to create a plugin, build a plugin, make a new plugin,
  develop a plugin, scaffold a plugin, start a plugin from scratch, or design a
  plugin. This skill requires Cowork mode with access to the outputs directory
  for delivering the final .plugin file. . Do NOT use for tasks outside the
  cowork domain. Korean triggers: "생성", "빌드", "설계", "스킬".
metadata:
  author: "anthropic-kwp"
  version: "1.0.0"
  category: "workflow"
---
# Create Cowork Plugin

Build a new plugin from scratch through guided conversation. Walk the user through discovery, planning, design, implementation, and packaging — delivering a ready-to-install `.plugin` file at the end.

## Overview

A plugin is a self-contained directory that extends Claude's capabilities with commands, skills, agents, hooks, and MCP server integrations. This skill encodes the full plugin architecture and a five-phase workflow for creating one conversationally.

The process:
1. **Discovery** — understand what the user wants to build
2. **Component Planning** — determine which component types are needed
3. **Design & Clarifying Questions** — specify each component in detail
4. **Implementation** — create all plugin files
5. **Review & Package** — deliver the `.plugin` file

> **Nontechnical output**: Keep all user-facing conversation in plain language. Do not expose implementation details like file paths, directory structures, or schema fields unless the user asks. Frame everything in terms of what the plugin will do.

## Plugin Architecture

### Directory Structure

Every plugin follows this layout:

```
plugin-name/
├── .claude-plugin/
│   └── plugin.json           # Required: plugin manifest
├── commands/                 # Slash commands (.md files)
├── agents/                   # Subagent definitions (.md files)
├── skills/                   # Skills (subdirectories with
