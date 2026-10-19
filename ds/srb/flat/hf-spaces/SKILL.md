---
name: hf-spaces
description: "Use when Discover, inspect, and develop Hugging Face Spaces (Gradio, Streamlit, Docker apps) via the hf CLI. Use when the user asks to search for: covers spaces, HF 스페이스, 스페이스 검색, gradio, reload"
metadata:
  holon-triggers: |
    search for Spaces
    get Space info
---

---
name: hf-spaces
description: >-
  Discover, inspect, and develop Hugging Face Spaces (Gradio, Streamlit, Docker
  apps) via the hf CLI. Use when the user asks to search for Spaces, get Space
  info, enable dev mode for live development, or hot-reload code changes on a
  running Space. Do NOT use for Inference Endpoints (use hf-endpoints), model
  serving (use hf-endpoints), repo management (use hf-repos), or compute jobs
  (use hf-jobs).
  Korean triggers: "HF 스페이스", "스페이스 검색", "스페이스 개발", "Gradio 앱".
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "ml"
---
# Hugging Face Spaces

> **Prerequisites**: `hf` CLI installed and authenticated. See `hf-hub` skill.

## Quick Commands

### Search Spaces

```bash
hf spaces ls --search "chatbot" --sort trending --limit 10
hf spaces ls --author gradio --format json
hf spaces ls -q  # Space IDs only
```

| Flag | Required | Description |
|------|----------|-------------|
| `--search TEXT` | No | Search query |
| `--author TEXT` | No | Filter by author/org |
| `--sort` | No | `created_at`, `downloads`, `last_modified`, `likes`, `trending_score` |
| `--limit INTEGER` | No | Number of results (default: 10) |
| `--format [table\|json]` | No | Output format |
| `-q, --quiet` | No | Print Space IDs only |

### Get Space Info

```bash
hf spaces info SPACE_ID
hf spaces info SPACE_ID --format json
```

### Dev Mode

Enable dev mode for live development without rebuilding:

```bash
hf spaces dev-mode SPACE_ID --enable
hf spaces dev-mode SPACE_ID --disable
```

> **Write command** — changes the Space's runtime mode.

When dev mode is enabled, code changes are applied without triggering a full rebuild.

### Hot Reload

Push a single file change to a running Space instantly:

```bash
hf spaces hot-reload SPACE_ID --file app.py
```

> **Write command** — modifies the running Space code.

This updates the specified file on the running Space without restarting.

## Common Patterns

```bash
# Find trending Gradio demos
hf spaces ls
