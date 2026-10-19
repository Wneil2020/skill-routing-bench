---
name: skill-seekers
description: "Use when Convert documentation sites, GitHub repos, PDFs, and videos into structured Cursor skill files with conflict detection. Use when converting external: covers seekers, 스킬, 빌드, registry, built"
metadata:
  holon-triggers: |
    converting external docs/repos into skills
    scraping documentation for skill creation
---

---
name: skill-seekers
description: >-
  Convert documentation sites, GitHub repos, PDFs, and videos into structured
  Cursor skill files with conflict detection. Use when converting external
  docs/repos into skills, scraping documentation for skill creation, building
  skills from existing sources, or detecting conflicts with installed skills. Do
  NOT use for creating skills from scratch (use anthropic-skill-creator or
  create-skill). Do NOT use for discovering pre-built skills from a registry
  (use find-skills). Korean triggers: "스킬", "빌드", "생성", "비디오".
metadata:
  upstream: "https://github.com/yusufkaraaslan/Skill_Seekers"
  version: "3.2.0"
  license: "MIT"
  category: "execution"
  author: "thaki"
---
# Skill Seekers — Documentation-to-Skill Converter

Convert any documentation source into a structured Cursor skill file. Supports doc sites (with llms.txt), GitHub repos, PDFs, videos, and local directories.

## Prerequisites

Install the CLI (one-time):

```bash
pip install skill-seekers[all]
```

For MCP integration only:

```bash
pip install skill-seekers[mcp]
```

Verify installation:

```bash
skill-seekers --version
```

## Workflow

### 1. Choose a Source

| Source type | Command |
|-------------|---------|
| Documentation URL | `skill-seekers create https://docs.react.dev/` |
| GitHub repo | `skill-seekers create facebook/react` |
| Local directory | `skill-seekers create ./my-project` |
| PDF file | `skill-seekers create manual.pdf` |
| Video (YouTube) | `skill-seekers video --url <youtube-url> --name <name>` |
| Config preset | `skill-seekers scrape --config configs/react.json` |

### 2. Package for Cursor

```bash
skill-seekers package output/<name> --target cursor
```

This produces a SKILL.md and supporting files in the Cursor-compatible format.

### 3. Install to Cursor

```bash
skill-seekers install-agent output/<name>/ --agent cursor
```

Or manually copy the output directory into `.cursor/skills/<name>/`.

### 4. Detect Conflicts

Before inst
