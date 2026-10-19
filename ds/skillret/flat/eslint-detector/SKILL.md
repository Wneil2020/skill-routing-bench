---
name: "eslint-detector"
description: "Use when the task involves analyze code: covers eslint, detector, commands, quality-gates-linter, makefile"
---

# eslint-detector

Detects ESLint configuration and available commands in a repository. Returns structured JSON output designed for consumption by the quality-gates-linter agent. Checks for ESLint config files, extracts lint commands from package.json, Makefile, and CLAUDE.md, and provides command sources for the agen
