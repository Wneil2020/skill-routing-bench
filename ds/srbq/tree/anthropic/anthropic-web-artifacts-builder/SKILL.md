---
name: anthropic-web-artifacts-builder
description: "Use when Build complex HTML artifacts with React, Tailwind, shadcn/ui. Use for complex artifacts requiring state management, routing, or: covers anthropic, web, artifacts, 웹 아티팩트, React 컴포넌트"
---

---
name: anthropic-web-artifacts-builder
description: >-
  Build complex HTML artifacts with React, Tailwind, shadcn/ui. Use for complex
  artifacts requiring state management, routing, or shadcn/ui components. Do NOT
  use for frontend code review (use frontend-expert), UX audits (use ux-expert),
  or simple static HTML (use anthropic-frontend-design). Korean triggers: "웹 아티팩트", "React 컴포넌트", "shadcn".
metadata:
  author: "anthropic"
  version: "1.0.0"
  license: "Complete terms in LICENSE.txt"
  category: "document"
---
# Web Artifacts Builder

To build powerful frontend claude.ai artifacts, follow these steps:
1. Initialize the frontend repo using `scripts/init-artifact.sh`
2. Develop your artifact by editing the generated code
3. Bundle all code into a single HTML file using `scripts/bundle-artifact.sh`
4. Display artifact to user
5. (Optional) Test the artifact

**Stack**: React 18 + TypeScript + Vite + Parcel (bundling) + Tailwind CSS + shadcn/ui

## Design & Style Guidelines

VERY IMPORTANT: To avoid what is often referred to as "AI slop", avoid using excessive centered layouts, purple gradients, uniform rounded corners, and Inter font.

## Quick Start

### Step 1: Initialize Project

Run the initialization script to create a new React project:
```bash
bash scripts/init-artifact.sh <project-name>
cd <project-name>
```

This creates a fully configured project with:
- ✅ React + TypeScript (via Vite)
- ✅ Tailwind CSS 3.4.1 with shadcn/ui theming system
- ✅ Path aliases (`@/`) configured
- ✅ 40+ shadcn/ui components pre-installed
- ✅ All Radix UI dependencies included
- ✅ Parcel configured for bundling (via .parcelrc)
- ✅ Node 18+ compatibility (auto-detects and pins Vite version)

### Step 2: Develop Your Artifact

To build the artifact, edit the generated files. See **Common Development Tasks** below for guidance.

### Step 3: Bundle to Single HTML File

To bundle the React app into a single HTML artifact:
```bash
bash scripts/bundle-artifact.sh
```

This crea
