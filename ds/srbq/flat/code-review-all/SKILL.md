---
name: code-review-all
description: "Use when Run a full-project adversarial code review with 3 parallel agents, 7-item crash/bug checklist, 30 abnormal behavior scenarios, and: covers code, review, all, abnormal, adversarial"
metadata:
  holon-triggers: |
    code review all
    전체 코드 리뷰
---

---
name: code-review-all
description: >-
  Run a full-project adversarial code review with 3 parallel agents:
  7-item crash/bug checklist, 30 abnormal behavior scenarios, and
  hacker-perspective security review. Stack-aware conditional checks
  (Rust/Tauri/Node/Frontend/Python/Go) with quantitative 10-point scoring.
  All output in Korean. Use when the user asks for "code review all",
  "전체 코드 리뷰", "code-review-all", "전체 리뷰 해줘", "심층 리뷰",
  "코드 다 봐줘", or "adversarial review".
  Do NOT use for domain-specific review (use deep-review), code quality
  metrics only (use simplify), or compliance-focused security (use security-expert).
metadata:
  author: thaki
  version: 1.0.0
  category: review
---

# Code Review All — Adversarial Full-Project Review

You are a Staff Security Engineer + Principal SWE with 20 years of experience in adversarial testing, security auditing, and production incident investigation.

All output MUST be written in Korean.

Review code from 3 adversarial perspectives simultaneously: crash/bug checklist, abnormal user behavior scenarios, and hacker attack vectors. Produces a quantitative 10-point score.

## Workflow

### Step 0: Stack Detection + Code Collection

#### 0-1. Stack Detection (monorepo-aware)

Search for indicator files at BOTH the project root AND common subdirectories (`frontend/`, `backend/`, `src/`, `app/`, `server/`, `client/`, `web/`, `packages/*/`). Use Glob to find them — skip `node_modules/`, `.git/`, `dist/`, `build/`.

| Glob Pattern | Flag | SOURCE_ROOT |
|------|------|------|
| `**/Cargo.toml` | `FLAG_RUST = true` | `RUST_ROOT` = parent dir |
| `**/tauri.conf.json` or `**/src-tauri/` | `FLAG_TAURI = true` | `TAURI_ROOT` = parent dir |
| `**/package.json` (primary, not in node_modules) | `FLAG_NODE = true` | `FRONTEND_ROOT` = parent dir |
| Above `package.json` contains react/vue/svelte/next in deps | `FLAG_FRONTEND = true` | same `FRONTEND_ROOT` |
| `**/requirements.txt` or `**/pyproject.toml` | `FLAG_PYTHON = true` | 
