---
name: hf-models
description: "Use when Search, discover, inspect, download, and upload models on Hugging Face Hub via the hf CLI. Use when the user asks to find models, search by: covers models, 모델 검색, 모델 다운로드, weights, author"
metadata:
  holon-triggers: |
    find models
    search by task
---

---
name: hf-models
description: >-
  Search, discover, inspect, download, and upload models on Hugging Face Hub
  via the hf CLI. Use when the user asks to find models, search by task or
  author, check model info, download model weights, upload a trained model,
  or discover trending models. Do NOT use for model training (use hf-model-trainer),
  model evaluation (use hf-evaluation), dataset operations (use hf-datasets),
  or repo lifecycle management (use hf-repos).
  Korean triggers: "모델 검색", "모델 다운로드", "모델 업로드", "HF 모델".
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "ml"
---
# Hugging Face Models

> **Prerequisites**: `hf` CLI installed and authenticated. See `hf-hub` skill.

## Quick Commands

### Search Models

```bash
hf models ls --search "sentiment" --sort trending_score --limit 10
```

| Flag | Required | Description |
|------|----------|-------------|
| `--search TEXT` | No | Search query |
| `--author TEXT` | No | Filter by author/org (e.g., `meta-llama`) |
| `--filter TEXT` | No | Tag filter, repeatable (e.g., `text-classification`) |
| `--num-parameters TEXT` | No | Parameter range (e.g., `min:7B,max:70B`) |
| `--sort` | No | `created_at`, `downloads`, `last_modified`, `likes`, `trending_score` |
| `--limit INTEGER` | No | Number of results (default: 10) |
| `--format [table\|json]` | No | Output format |
| `-q, --quiet` | No | Print model IDs only |
| `--expand TEXT` | No | Extra metadata (e.g., `downloads,likes,tags`) |

### Get Model Info

```bash
hf models info MODEL_ID
hf models info MODEL_ID --format json --expand downloads,likes,tags,safetensors
```

### Download Model

```bash
hf download MODEL_ID
hf download MODEL_ID --include "*.safetensors" --local-dir ./models/
hf download MODEL_ID --include "config.json" "tokenizer*"
```

| Flag | Required | Description |
|------|----------|-------------|
| `MODEL_ID` | Yes | Repository ID (e.g., `meta-llama/Llama-3.2-1B`) |
| `--include` | No | Glob patterns to include |
| `--exclude` | No |
