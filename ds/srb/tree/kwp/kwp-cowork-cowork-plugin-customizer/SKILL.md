---
name: kwp-cowork-cowork-plugin-customizer
description: "Use when Customize a Claude Cowork plugin for a specific organization — either set up a generic plugin template (replace ~~placeholders) or tweak an: covers kwp, cowork, plugin, connector, packaging"
metadata:
  holon-triggers: |
    customize plugin
    set up plugin
---

---
name: kwp-cowork-cowork-plugin-customizer
description: >-
  Customize a Claude Cowork plugin for a specific organization — either set up
  a generic plugin template (replace ~~placeholders) or tweak an already-configured
  plugin. Guides through knowledge MCP search, todo-driven customization, MCP
  connector discovery, and packaging as a .plugin file.
  Use when the user asks to "customize plugin", "set up plugin", "configure
  plugin", "tailor plugin", or "update the standup command" for a Cowork plugin.
  Do NOT use for tasks outside the cowork domain.
metadata:
  author: anthropic-kwp
  version: 1.0.0
  category: workflow
---

# Cowork Plugin Customization

Customize a plugin for a specific organization — either by setting up a generic plugin template for the first time, or by tweaking and refining an already-configured plugin.

> **Finding the plugin**: To find the plugin's source files, run `find mnt/.local-plugins mnt/.plugins -type d -name "*<plugin-name>*"` to locate the plugin directory, then read its files to understand its structure before making changes. If you cannot find the plugin directory, the user is likely running this conversation in a remote container. Abort and let them know: "Customizing plugins is currently only available in the desktop app's Cowork mode."

## Determining the Customization Mode

After locating the plugin, check for `~~`-prefixed placeholders: `grep -rn '~~\w' /path/to/plugin --include='*.md' --include='*.json'`

> **Default rule**: If `~~` placeholders exist, default to **Generic plugin setup** unless the user explicitly asks to customize a specific part of the plugin.

**1. Generic plugin setup** — The plugin contains `~~`-prefixed placeholders. These are customization points in a template that need to be replaced with real values (e.g., `~~Jira` → `Asana`, `~~your-team-channel` → `#engineering`).

**2. Scoped customization** — No `~~` placeholders exist, and the user asked to customize a specific part of the plugin (e.
