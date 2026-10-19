---
name: hf-cli
description: "Use when Execute HuggingFace Hub operations via the hf CLI — download models/datasets, upload files, manage repos, run jobs, and manage auth. Use when uploading: covers cli, 체크, 주식, auth, downloading"
metadata:
  holon-triggers: |
    uploading financial models to Hub
    downloading pre-trained models (FinBERT
---

---
name: hf-cli
description: >-
  Execute HuggingFace Hub operations via the hf CLI — download models/datasets,
  upload files, manage repos, run jobs, and manage auth. Use when uploading
  financial models to Hub, downloading pre-trained models (FinBERT,
  sentence-transformers), managing HF repos, or checking auth status. Do NOT use
  for model training (use hf-model-trainer). Do NOT use for dataset CRUD (use
  hf-datasets). Do NOT use for stock analysis (use daily-stock-check). Korean
  triggers: "체크", "주식", "모델", "학습".
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "ml"
---
Install: `curl -LsSf https://hf.co/cli/install.sh | bash -s`.

The Hugging Face Hub CLI tool `hf` is available. IMPORTANT: The `hf` command replaces the deprecated `huggingface-cli` command.

Use `hf --help` to view available functions. Note that auth commands are now all under `hf auth` e.g. `hf auth whoami`.

Generated with `huggingface_hub v1.6.0`. Run `hf skills add --force` to regenerate.

## Commands

- `hf download REPO_ID` — Download files from the Hub.
- `hf env` — Print information about the environment.
- `hf sync` — Sync files between local directory and a bucket.
- `hf upload REPO_ID` — Upload a file or a folder to the Hub. Recommended for single-commit uploads.
- `hf upload-large-folder REPO_ID LOCAL_PATH` — Upload a large folder to the Hub. Recommended for resumable uploads.
- `hf version` — Print information about the hf version.

### `hf auth` — Manage authentication (login, logout, etc.).

- `hf auth list` — List all stored access tokens.
- `hf auth login` — Login using a token from huggingface.co/settings/tokens.
- `hf auth logout` — Logout from a specific token.
- `hf auth switch` — Switch between access tokens.
- `hf auth whoami` — Find out which huggingface.co account you are logged in as.

### `hf buckets` — Commands to interact with buckets.

- `hf buckets cp SRC` — Copy a single file to or from a bucket.
- `hf buckets create BUCKET_ID` — Create a new buck
