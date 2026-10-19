---
name: hf-collections
description: "Use when Curate and manage collections of models, datasets, spaces, and papers on Hugging Face Hub via the hf CLI. Use when the user asks to: covers collections, 컬렉션 생성, 컬렉션 관리, curate, curated"
metadata:
  holon-triggers: |
    create a collection
    add items to a collection
---

---
name: hf-collections
description: >-
  Curate and manage collections of models, datasets, spaces, and papers on
  Hugging Face Hub via the hf CLI. Use when the user asks to create a
  collection, add items to a collection, browse collections by owner, update
  collection metadata, or organize Hub resources into curated lists.
  Do NOT use for model search (use hf-models), dataset CRUD (use hf-datasets),
  repo management (use hf-repos), or paper discovery (use hf-papers).
  Korean triggers: "컬렉션 생성", "컬렉션 관리", "HF 컬렉션", "모델 큐레이션".
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "ml"
---
# Hugging Face Collections

> **Prerequisites**: `hf` CLI installed and authenticated. See `hf-hub` skill.

## Quick Commands

### List Collections

```bash
hf collections ls --owner nvidia --sort trending --limit 10
hf collections ls --item MODEL_ID --format json
```

| Flag | Required | Description |
|------|----------|-------------|
| `--owner TEXT` | No | Filter by owner/org |
| `--item TEXT` | No | Find collections containing this item |
| `--sort` | No | `trending`, `created_at`, `last_modified` |
| `--limit INTEGER` | No | Number of results |
| `--format [table\|json]` | No | Output format |
| `-q, --quiet` | No | Print collection slugs only |

### Get Collection Info

```bash
hf collections info COLLECTION_SLUG
hf collections info username/my-collection-123abc --format json
```

### Create Collection

```bash
hf collections create "My Research" --description "Curated models for NLP"
hf collections create "Team Models" --namespace my-org --private
```

> **Write command** — confirm with the user before creating.

| Flag | Required | Description |
|------|----------|-------------|
| `TITLE` | Yes | Collection title |
| `--description` | No | Collection description |
| `--namespace` | No | Owner namespace (user or org) |
| `--private` | No | Create as private collection |

### Add Item to Collection

```bash
hf collections add-item SLUG ITEM_ID model
hf collection
