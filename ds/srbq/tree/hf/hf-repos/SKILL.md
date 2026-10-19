---
name: hf-repos
description: "Use when Manage repository lifecycle on Hugging Face Hub — create, delete, branch, tag, configure settings, move, duplicate, and delete files. Use: covers repos, HF 레포 생성, 레포 관리, branches, gating"
metadata:
  holon-triggers: |
    create a new HF repo
    manage branches
---

---
name: hf-repos
description: >-
  Manage repository lifecycle on Hugging Face Hub — create, delete, branch,
  tag, configure settings, move, duplicate, and delete files. Use when the
  user asks to create a new HF repo, manage branches or tags, change repo
  settings (gating, visibility), duplicate or move repos, or delete repo files.
  Do NOT use for model search or download (use hf-models), file upload
  (use hf-models with hf upload), discussions/PRs (use hf-discussions),
  or dataset CRUD (use hf-datasets).
  Korean triggers: "HF 레포 생성", "레포 관리", "브랜치 관리", "레포 삭제".
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "ml"
---
# Hugging Face Repos

> **Prerequisites**: `hf` CLI installed and authenticated. See `hf-hub` skill.

## Quick Commands

### Create Repository

```bash
hf repos create ORG/my-model --type model --private
hf repos create my-dataset --type dataset
hf repos create my-space --type space
```

| Flag | Required | Description |
|------|----------|-------------|
| `REPO_ID` | Yes | Repository ID (e.g., `org/name`) |
| `--type` | No | `model` (default), `dataset`, `space` |
| `--private` | No | Create as private repo |

> **Write command** — confirm with the user before executing.

### Delete Repository

```bash
hf repos delete ORG/my-model
hf repos delete ORG/my-dataset --type dataset
```

> **DESTRUCTIVE** — this action is irreversible. Always confirm with the user.

## Raw CLI Commands

### Branch Management

```bash
hf repos branch create REPO_ID BRANCH_NAME
hf repos branch delete REPO_ID BRANCH_NAME
hf repos branch list REPO_ID
```

### Tag Management

```bash
hf repos tag create REPO_ID TAG_NAME --revision COMMIT_HASH
hf repos tag delete REPO_ID TAG_NAME
hf repos tag list REPO_ID
```

### Repository Settings

```bash
hf repos settings REPO_ID --gated auto       # auto-approve access requests
hf repos settings REPO_ID --gated manual      # manual approval
hf repos settings REPO_ID --gated false        # remove gating
hf repos settings 
