---
name: hf-hub
description: "Use when Install, authenticate, and configure the Hugging Face CLI (hf) for managing models, datasets, repos, jobs, and more from the terminal. Use when: covers hub, HF 설정, HF 인증, cache, authenticate"
metadata:
  holon-triggers: |
    set up hf CLI
    authenticate with Hugging Face
---

---
name: hf-hub
description: >-
  Install, authenticate, and configure the Hugging Face CLI (hf) for managing
  models, datasets, repos, jobs, and more from the terminal. Use when the user
  asks to set up hf CLI, authenticate with Hugging Face, manage cache, install
  agent skills, manage extensions, or check environment info. Do NOT use for
  model search (use hf-models), dataset operations (use hf-datasets), jobs
  (use hf-jobs), repo management (use hf-repos), paper discovery (use hf-papers),
  collection management (use hf-collections), discussions (use hf-discussions),
  endpoints (use hf-endpoints), buckets (use hf-buckets), or spaces (use hf-spaces).
  Korean triggers: "HF 설정", "HF 인증", "HF CLI 설치", "허깅페이스 설정",
  "hf 로그인".
metadata:
  author: "thaki"
  version: "1.1.0"
  category: "ml"
---
# Hugging Face Hub CLI — Setup & Reference

One CLI for all of Hugging Face Hub. Built for humans and AI agents.

> For a quick command cheatsheet, see [references/cli-cheatsheet.md](references/cli-cheatsheet.md).

## Installation

```bash
curl -LsSf https://hf.co/cli/install.sh | bash -s
```

Alternative methods:

```bash
uvx hf                        # run directly via uv
pip install -U huggingface_hub[cli] # install via pip (includes hf CLI)
```

Verify: `hf version`

> **Note:** The modern `hf` CLI (Rust binary) replaces the older `huggingface-cli`. Both
> are installed by `pip install huggingface_hub[cli]`, but prefer `hf` for all operations.

## Authentication

### Token Login

```bash
hf auth login                 # interactive prompt for token
hf auth login --token hf_xxx  # non-interactive
```

Tokens are created at [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens).

### Multiple Accounts

```bash
hf auth list                  # list stored tokens
hf auth switch                # switch active token
hf auth whoami                # show current user
hf auth logout                # remove stored token
```

### Environment Variable (recommended
