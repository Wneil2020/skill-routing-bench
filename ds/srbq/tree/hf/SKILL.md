---
name: hf
description: "Use when the request concerns the hf category of skills: covers hf"
---

Grouping node for the 0 skills of the hf category. 

<!-- sub-skills -->
## Sub-skills (auto-generated, do not edit by hand)

- **hf-auto-finetune-planner** (`hf-auto-finetune-planner/`): Use when End-to-end autonomous fine-tuning planner that takes a natural language task description, discovers the optimal base model + training: covers auto, finetune, planner, combination, estimates
- **hf-buckets** (`hf-buckets/`): Use when Manage S3-style object storage (Xet backend) on Hugging Face Hub via the hf CLI. Use when the user asks to create a bucket, upload files to a: covers buckets, HF 버킷, 오브젝트 스토리지, bucket, xet
- **hf-cli** (`hf-cli/`): Use when Execute HuggingFace Hub operations via the hf CLI — download models/datasets, upload files, manage repos, run jobs, and manage auth. Use when uploading: covers cli, 체크, 주식, auth, downloading
- **hf-collections** (`hf-collections/`): Use when Curate and manage collections of models, datasets, spaces, and papers on Hugging Face Hub via the hf CLI. Use when the user asks to: covers collections, 컬렉션 생성, 컬렉션 관리, curate, curated
- **hf-dataset-viewer** (`hf-dataset-viewer/`): Use when Explore and query HuggingFace datasets via the Dataset Viewer REST API — fetch metadata, paginate rows, search text, filter, and: covers dataset, viewer, 데이터셋 탐색, HF 데이터 조회, paginate
- **hf-datasets** (`hf-datasets/`): Use when Create and manage datasets on HuggingFace Hub — initialize repos, stream row updates, run SQL queries, and transform data. Use when: covers datasets, 데이터셋 생성, HF 데이터셋, initialize, curated
- **hf-discussions** (`hf-discussions/`): Use when Manage discussions and pull requests on Hugging Face Hub repos via the hf CLI. Use when the user asks to list discussions, create a PR on: covers discussions, HF 토론, HF PR, 허브 풀리퀘스트, comment
- **hf-endpoints** (`hf-endpoints/`): Use when Deploy, manage, and monitor Hugging Face Inference Endpoints via the hf CLI. Use when the user asks to deploy a model as an API endpoint: covers endpoints, 추론 엔드포인트, 모델 배포, pause, deploy
- **hf-evaluation** (`hf-evaluation/`): Use when Evaluate ML model quality and manage evaluation results in HuggingFace model cards. Supports running benchmarks with: covers evaluation, 모델 평가, 벤치마크, artificial, benchmarks
- **hf-hub** (`hf-hub/`): Use when Install, authenticate, and configure the Hugging Face CLI (hf) for managing models, datasets, repos, jobs, and more from the terminal. Use when: covers hub, HF 설정, HF 인증, cache, authenticate
- **hf-jobs** (`hf-jobs/`): Use when Run compute workloads on HuggingFace Jobs infrastructure — UV scripts, Docker jobs, batch inference, data processing, and scheduled tasks. Use: covers jobs, HF Jobs, GPU 작업, workloads, trl
- **hf-model-arena** (`hf-model-arena/`): Use when Competitive model evaluation arena that discovers competing models for a given task, runs head-to-head evaluations on a standardized: covers model, arena, competing, deploys, dimensional
- **hf-model-trainer** (`hf-model-trainer/`): Use when Train or fine-tune language models (FinBERT, sentence-transformers) on HuggingFace Jobs infrastructure using TRL. Covers SFT, DPO, GRPO, reward: covers model, trainer, 모델 훈련, 파인튜닝, dpo
- **hf-models** (`hf-models/`): Use when Search, discover, inspect, download, and upload models on Hugging Face Hub via the hf CLI. Use when the user asks to find models, search by: covers models, 모델 검색, 모델 다운로드, weights, author
- **hf-papers** (`hf-papers/`): Use when Discover daily and trending papers on Hugging Face Hub via the hf CLI. Use when the user asks to list today's papers, find trending AI: covers papers, 오늘 논문, 트렌딩 논문, publications, scouting
- **hf-repos** (`hf-repos/`): Use when Manage repository lifecycle on Hugging Face Hub — create, delete, branch, tag, configure settings, move, duplicate, and delete files. Use: covers repos, HF 레포 생성, 레포 관리, branches, gating
- **hf-spaces** (`hf-spaces/`): Use when Discover, inspect, and develop Hugging Face Spaces (Gradio, Streamlit, Docker apps) via the hf CLI. Use when the user asks to search for: covers spaces, HF 스페이스, 스페이스 검색, gradio, reload
- **hf-trackio** (`hf-trackio/`): Use when Track and visualize ML training experiments with Trackio — log metrics via Python API, fire alerts for diagnostics, and retrieve metrics: covers trackio, 실험 추적, 학습 모니터링, diagnostics, fire
- **hf-trending-intelligence** (`hf-trending-intelligence/`): Use when Autonomous daily intelligence pipeline that cross-references HF papers, models, datasets, and community activity to detect: covers trending, intelligence, browsing, mainstream, ecosystem

Routing rule: when the task matches one of the sub-skills above, read the SKILL.md in that subdirectory for detailed instructions before acting;
if that sub-skill lists deeper sub-skills, repeat the descent. Load only the documents on the matching path.
<!-- /sub-skills -->
