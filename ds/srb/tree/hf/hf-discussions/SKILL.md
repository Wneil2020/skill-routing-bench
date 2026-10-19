---
name: hf-discussions
description: "Use when Manage discussions and pull requests on Hugging Face Hub repos via the hf CLI. Use when the user asks to list discussions, create a PR on: covers discussions, HF 토론, HF PR, 허브 풀리퀘스트, comment"
metadata:
  holon-triggers: |
    list discussions
    create a PR on an HF repo
---

---
name: hf-discussions
description: >-
  Manage discussions and pull requests on Hugging Face Hub repos via the hf CLI.
  Use when the user asks to list discussions, create a PR on an HF repo, comment
  on a discussion, merge a pull request, view PR diffs, or manage community
  interactions on Hub repositories. Do NOT use for GitHub PRs (use gh CLI),
  repo lifecycle management (use hf-repos), model search (use hf-models),
  or dataset operations (use hf-datasets).
  Korean triggers: "HF 토론", "HF PR", "허브 풀리퀘스트", "HF 디스커션".
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "ml"
---
# Hugging Face Discussions

> **Prerequisites**: `hf` CLI installed and authenticated. See `hf-hub` skill.

## Quick Commands

### List Discussions

```bash
hf discussions list REPO_ID
hf discussions list REPO_ID --kind pull_request --status open
hf discussions list REPO_ID --author username --format json
```

| Flag | Required | Description |
|------|----------|-------------|
| `REPO_ID` | Yes | Repository ID |
| `--kind` | No | `all` (default), `discussion`, `pull_request` |
| `--status` | No | `open`, `closed`, `merged`, `draft`, `all` |
| `--author` | No | Filter by author |
| `--type` | No | Repo type: `model`, `dataset`, `space` |
| `--format [table\|json]` | No | Output format |

### Get Discussion Info

```bash
hf discussions info REPO_ID NUM
hf discussions info REPO_ID NUM --comments   # include comments
hf discussions info REPO_ID NUM --diff        # show PR diff
```

### Create Discussion / Pull Request

```bash
hf discussions create REPO_ID --title "Fix typo in README"
hf discussions create REPO_ID --title "Update model card" --pull-request
hf discussions create REPO_ID --title "Bug report" --body "Description here"
```

> **Write command** — confirm with the user before creating.

| Flag | Required | Description |
|------|----------|-------------|
| `REPO_ID` | Yes | Target repository |
| `--title` | Yes | Discussion/PR title |
| `--pull-request` | No | Create as p
