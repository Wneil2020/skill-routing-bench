---
name: hf-buckets
description: "Use when Manage S3-style object storage (Xet backend) on Hugging Face Hub via the hf CLI. Use when the user asks to create a bucket, upload files to a: covers buckets, HF 버킷, 오브젝트 스토리지, bucket, xet"
metadata:
  holon-triggers: |
    create a bucket
    upload files to a bucket
---

---
name: hf-buckets
description: >-
  Manage S3-style object storage (Xet backend) on Hugging Face Hub via the
  hf CLI. Use when the user asks to create a bucket, upload files to a bucket,
  sync directories, list bucket contents, download from a bucket, or manage
  large artifact storage for checkpoints, logs, and datasets.
  Do NOT use for model uploads to repos (use hf-models with hf upload),
  file management in repos (use hf-repos), dataset CRUD (use hf-datasets),
  or compute jobs (use hf-jobs).
  Korean triggers: "HF 버킷", "오브젝트 스토리지", "버킷 동기화", "체크포인트 저장".
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "ml"
---
# Hugging Face Buckets

> **Prerequisites**: `hf` CLI installed and authenticated. See `hf-hub` skill.
> Buckets use the `hf://buckets/` URI scheme for remote paths.

## Quick Commands

### Create Bucket

```bash
hf buckets create my-checkpoints
hf buckets create my-org/training-logs --private --exist-ok
```

> **Write command** — confirm with the user before creating.

| Flag | Required | Description |
|------|----------|-------------|
| `BUCKET_ID` | Yes | Bucket name (e.g., `user/bucket-name`) |
| `--private` | No | Create as private bucket |
| `--exist-ok` | No | Don't error if bucket already exists |

### List Buckets / Files

```bash
hf buckets list                          # list all your buckets
hf buckets list NAMESPACE                # list buckets in namespace
hf buckets list BUCKET_ID                # list files in bucket
hf buckets list BUCKET_ID -R --tree -h   # recursive tree with human sizes
```

| Flag | Required | Description |
|------|----------|-------------|
| `-R, --recursive` | No | List recursively |
| `--tree` | No | Tree-style display |
| `-h, --human-readable` | No | Human-readable file sizes |

### Copy Files

```bash
# Upload
hf buckets cp ./model.safetensors hf://buckets/user/my-bucket/models/

# Download
hf buckets cp hf://buckets/user/my-bucket/models/model.safetensors ./local/
```

> **Write command** (for
