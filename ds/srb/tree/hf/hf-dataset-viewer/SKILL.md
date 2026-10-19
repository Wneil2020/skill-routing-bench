---
name: hf-dataset-viewer
description: "Use when Explore and query HuggingFace datasets via the Dataset Viewer REST API — fetch metadata, paginate rows, search text, filter, and: covers dataset, viewer, 데이터셋 탐색, HF 데이터 조회, paginate"
metadata:
  holon-triggers: |
    exploring public financial datasets
    previewing dataset structure before training
---

---
name: hf-dataset-viewer
description: >-
  Explore and query HuggingFace datasets via the Dataset Viewer REST API —
  fetch metadata, paginate rows, search text, filter, and download parquet
  files. Use when exploring public financial datasets, previewing dataset
  structure before training, or extracting specific rows from large datasets. Do
  NOT use for dataset creation or editing (use hf-datasets). Do NOT use for
  local DB queries (use db-expert). Do NOT use for model training (use
  hf-model-trainer). Korean triggers: "데이터셋 탐색", "HF 데이터 조회".
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "ml"
---
# Hugging Face Dataset Viewer

Use this skill to execute read-only Dataset Viewer API calls for dataset exploration and extraction.

## Core workflow

1. Optionally validate dataset availability with `/is-valid`.
2. Resolve `config` + `split` with `/splits`.
3. Preview with `/first-rows`.
4. Paginate content with `/rows` using `offset` and `length` (max 100).
5. Use `/search` for text matching and `/filter` for row predicates.
6. Retrieve parquet links via `/parquet` and totals/metadata via `/size` and `/statistics`.

## Defaults

- Base URL: `https://datasets-server.huggingface.co`
- Default API method: `GET`
- Query params should be URL-encoded.
- `offset` is 0-based.
- `length` max is usually `100` for row-like endpoints.
- Gated/private datasets require `Authorization: Bearer <HF_TOKEN>`.

## Dataset Viewer

- `Validate dataset`: `/is-valid?dataset=<namespace/repo>`
- `List subsets and splits`: `/splits?dataset=<namespace/repo>`
- `Preview first rows`: `/first-rows?dataset=<namespace/repo>&config=<config>&split=<split>`
- `Paginate rows`: `/rows?dataset=<namespace/repo>&config=<config>&split=<split>&offset=<int>&length=<int>`
- `Search text`: `/search?dataset=<namespace/repo>&config=<config>&split=<split>&query=<text>&offset=<int>&length=<int>`
- `Filter with predicates`: `/filter?dataset=<namespace/repo>&config=<config>&split=<split>&where=<predic
