---
name: hf-endpoints
description: "Use when Deploy, manage, and monitor Hugging Face Inference Endpoints via the hf CLI. Use when the user asks to deploy a model as an API endpoint: covers endpoints, 추론 엔드포인트, 모델 배포, pause, deploy"
metadata:
  holon-triggers: |
    deploy a model as an API endpoint
    list endpoints
---

---
name: hf-endpoints
description: >-
  Deploy, manage, and monitor Hugging Face Inference Endpoints via the hf CLI.
  Use when the user asks to deploy a model as an API endpoint, list endpoints,
  browse the endpoint catalog, pause or resume an endpoint, scale to zero, or
  delete an endpoint. Do NOT use for cloud compute jobs (use hf-jobs), model
  download (use hf-models), Spaces (use hf-spaces), or model training
  (use hf-model-trainer).
  Korean triggers: "추론 엔드포인트", "모델 배포", "엔드포인트 관리", "HF 엔드포인트".
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "ml"
---
# Hugging Face Inference Endpoints

> **Prerequisites**: `hf` CLI installed and authenticated. See `hf-hub` skill.
> Inference Endpoints require a Pro, Team, or Enterprise plan.

## Quick Commands

### List Endpoints

```bash
hf endpoints ls
hf endpoints ls --namespace my-org --format json
```

### Describe Endpoint

```bash
hf endpoints describe my-endpoint
hf endpoints describe my-endpoint --format json
```

### Deploy from Repository

```bash
hf endpoints deploy my-endpoint \
  --repo meta-llama/Llama-3.2-1B-Instruct \
  --framework pytorch \
  --accelerator gpu \
  --instance-size x1 \
  --instance-type nvidia-a10g \
  --region us-east-1 \
  --vendor aws
```

> **Write command** — deploying creates a billable resource. Confirm with the user.

| Flag | Required | Description |
|------|----------|-------------|
| `NAME` | Yes | Endpoint name |
| `--repo` | Yes | Model repository ID |
| `--framework` | Yes | `pytorch`, `tensorflow`, etc. |
| `--accelerator` | Yes | `cpu`, `gpu` |
| `--instance-size` | Yes | Size tier (e.g., `x1`, `x2`, `x4`) |
| `--instance-type` | Yes | Hardware type (e.g., `nvidia-a10g`, `nvidia-a100`) |
| `--region` | Yes | Cloud region |
| `--vendor` | Yes | Cloud provider (`aws`, `gcp`, `azure`) |
| `--min-replica` | No | Minimum replicas (default: 1) |
| `--max-replica` | No | Maximum replicas for autoscaling |
| `--namespace` | No | Organization namespace |

### Deploy fro
