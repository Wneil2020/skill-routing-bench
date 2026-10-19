---
name: standalone
description: "Use when the request concerns the standalone category of skills: covers standalone"
---

Grouping node for the 0 skills of the standalone category. 

<!-- sub-skills -->
## Sub-skills (auto-generated, do not edit by hand)

- **agent-browser** (`agent-browser/`): Use when Headless browser automation via the agent-browser CLI (v0.16.3). Navigates pages, fills forms, clicks elements, takes screenshots, extracts: covers browser, 브라우저, 테스트, allowed, allowlist
- **alphaxiv-paper-lookup** (`alphaxiv-paper-lookup/`): Use when Look up any arXiv paper on alphaxiv.org to get a structured AI-generated overview (machine-readable report) without reading raw PDFs: covers alphaxiv, paper, lookup, 논문 조회, arXiv 요약
- **auto-research** (`auto-research/`): Use when Run the AutoResearchClaw 23-stage autonomous research pipeline that transforms a research topic into a conference-ready: covers auto, research, literature, researchclaw, autoresearchclaw
- **auto-research-distribute** (`auto-research-distribute/`): Use when Distribute AutoResearchClaw pipeline outputs (paper, LaTeX, experiments) to Notion, Slack, NotebookLM, PPTX, and paper-archive: covers auto, research, distribute, autoresearchclaw, latex
- **automation-strategist** (`automation-strategist/`): Use when Strategic automation planning for the stock analytics pipeline — decide what to automate vs keep manual, design human-in-the-loop: covers automation, strategist, roi, thinker, keep
- **calendar-daily-briefing** (`calendar-daily-briefing/`): Use when Fetch today's Google Calendar events and produce a concise Korean briefing with preparation alerts for meetings and interviews. Use when the: covers calendar, daily, briefing, staff, chief
- **ci-quality-gate** (`ci-quality-gate/`): Use when Run the full CI pipeline locally (secret scan, Python lint/test, Go lint/test, frontend lint/test/build, schema check) and produce a pass/fail report: covers quality, gate, 감사, 테스트, pushing
- **code-review-all** (`code-review-all/`): Use when Run a full-project adversarial code review with 3 parallel agents, 7-item crash/bug checklist, 30 abnormal behavior scenarios, and: covers code, review, all, abnormal, adversarial
- **codebase-archaeologist** (`codebase-archaeologist/`): Use when Analyze git history to create ownership maps, churn hotspot analysis, "bus factor" reports, pattern evolution timelines, and dead: covers codebase, archaeologist, archaeology, bus, churn
- **commit-to-issue** (`commit-to-issue/`): Use when Analyze recent git commits and create GitHub issues with project field setup on ThakiCloud project boards. Use when the user asks to "create issues from: covers commit, issue, 커밋, 리뷰, boards
- **context-engineer** (`context-engineer/`): Use when Manage project knowledge architecture — MEMORY.md lifecycle, domain glossary maintenance, context packages per analysis type, knowledge: covers context, engineer, during, done, explaining
- **critical-review** (`critical-review/`): Use when End-to-end CTO/CEO critical review and remediation pipeline, parallel technical and strategic critiques (4 review sections x 4 issues: covers critical, review, critiques, dual, remediation
- **cursor-automations** (`cursor-automations/`): Use when Create, configure, and manage Cursor Automations — always-on cloud agents that run on schedules or respond to events from GitHub: covers cursor, automations, webhooks, involving, linear
- **cursor-sync** (`cursor-sync/`): Use when N-repo bidirectional sync of .cursor/ assets (commands, skills, rules) across all 5 ThakiCloud repositories. Research acts as the merge hub, pull: covers cursor, sync, absorbs, acts, newest
- **daily-am-orchestrator** (`daily-am-orchestrator/`): Use when Morning Pipeline orchestrator, 8 phases covering pre-flight, git sync, Google Workspace, email intelligence, market intelligence: covers daily, orchestrator, evening, routines, covering
- **daily-stock-check** (`daily-stock-check/`): Use when Analyze stocks from Turtle Trading (MA + Donchian) and Bollinger Bands perspectives, then post a buy/sell/neutral summary to Slack. Use when the user asks: covers daily, stock, check, 주식, 체크
- **daily-strategy-post** (`daily-strategy-post/`): Use when Run multi-role strategic analysis on the day's aggregated intelligence and post company/team/product strategy documents to Slack: covers daily, strategy, post, distributed, synthesizes
- **decision-router** (`decision-router/`): Use when Detect decision-worthy items from pipeline outputs and route them to the appropriate Slack decision channel. Personal decisions: covers decision, router, partnerships, inline, personal
- **domain-commit** (`domain-commit/`): Use when Run pre-commit hooks, fix lint errors, and create domain-split git commits from uncommitted changes. Use when the user asks to commit local changes: covers domain, commit, 커밋, 생성, trivial
- **eod-ship** (`eod-ship/`): Use when End-of-day shipping pipeline, cursor-sync assets across projects, then release-ship the current project and 5 managed projects, posting a consolidated: covers eod, ship, scrum, wrap, managed
- **executive-briefing** (`executive-briefing/`): Use when Synthesize multiple role-perspective analysis documents into a unified CEO executive briefing report in Korean. Identifies: covers executive, briefing, CEO 종합 보고서, 경영진 브리핑, collecting
- **fe-pipeline** (`fe-pipeline/`): Use when 자연어 한 줄부터 Swagger+Figma 풀세트까지, 프로젝트 내 API·화면 패턴을 자동 발견하여 기획서·Entity·Feature/Widget/Page·i18n·검증을 체크포인트 기반으로 자동 진행합니다. 새 화면 생성뿐 아니라 기존 화면: covers pipeline, widget, swagger, entity, i18n
- **feature-intake-router** (`feature-intake-router/`): Use when --- description, Automates feature request intake from Slack forms, auto-classifies by product area, creates Notion tickets with stakeholder: covers feature, intake, router, 기능 요청 접수, 요청 라우팅
- **feedback-meeting-scheduler** (`feedback-meeting-scheduler/`): Use when Detect PRs and issues needing discussion (stale reviews, conflicting comments, blocked items) and proactively schedule 1,1 feedback: covers feedback, meeting, scheduler, parties, blocked
- **full-stack-planner** (`full-stack-planner/`): Use when Generate comprehensive multi-phase implementation plans that map a high-level goal to the project's entire skill ecosystem. Produces: covers full, stack, planner, assignments, concurrency
- **helm-validator** (`helm-validator/`): Use when Validate Helm charts using helm lint, helm template rendering, kubeconform schema validation, and kube-score/Polaris policy checks: covers helm, validator, kube, polaris, kubeconform
- **implement-screen** (`implement-screen/`): Use when 화면 기획서와 Figma 디자인을 기반으로 FSD 구조의 프로덕션 코드를 생성하는 마스터 오케스트레이터. 화면 구현, 페이지 만들어줘, 화면 개발, Figma URL + screen spec으로 코드 생성 시 사용합니다. Do NOT use for 기획서만: covers implement, screen, fsd, spec, tds
- **jira-linear-adapter** (`jira-linear-adapter/`): Use when Bidirectional sync adapter between GitHub Issues/Projects and Jira or Linear. Maps fields (status, priority, sprint, assignee) across: covers jira, linear, adapter, assignee, bidirectional
- **k8s-manifest-validator** (`k8s-manifest-validator/`): Use when Validate Kubernetes manifests using kubeconform schema validation, KubeLinter policy checks, and kubectl dry-run server-side validation: covers k8s, manifest, validator, kubectl, kubelinter
- **onboarding-accelerator** (`onboarding-accelerator/`): Use when Generate a complete "new developer kit" by orchestrating 8 existing skills, architecture analysis, code ownership maps, interactive: covers onboarding, accelerator, joining, getting, member
- **performance-profiler** (`performance-profiler/`): Use when Measure API endpoint latency (p50/p95/p99), analyze PostgreSQL slow queries, profile frontend bundle size, and evaluate against SLO targets: covers performance, profiler, 성능, 리뷰, latency
- **pipeline-builder** (`pipeline-builder/`): Use when Build and manage automated data pipelines using existing Python scripts, GitHub Actions, and cron schedules without writing new: covers pipeline, builder, makefile, repeatable, schedules
- **plans** (`plans/`): Use when Two-phase pipeline, optimize a raw prompt using prompt-architect frameworks, then decompose the optimized prompt into a skill-based: covers plans, delegation, ordering, both, decompose
- **ppt-template-engine** (`ppt-template-engine/`): Use when Populate approved PPTX templates with LLM-generated content via JSON specs, enforcing slide master layouts, placeholder contracts, and: covers ppt, template, engine, master, branding
- **prd-research-factory** (`prd-research-factory/`): Use when --- description, End-to-end pipeline that takes a meeting URL or customer interview, auto-researches market context, then writes a complete: covers prd, research, factory, 미팅 기반 PRD, 리서치 PRD
- **problem-definition** (`problem-definition/`): Use when Guide users through a structured 5D framework (Describe, Decompose, Diagnose, Define, Document) to properly define problems before jumping to: covers problem, definition, 리뷰, 테스트, frame
- **proposal-factory** (`proposal-factory/`): Use when --- description, RFP intake → classify requirements → search past proposals via Cognee KG → generate proposal draft with case studies →: covers proposal, factory, 제안서 생성, 제안 팩토리, received
- **refactor-simulator** (`refactor-simulator/`): Use when Before making any code change, simulate the blast radius by analyzing all call sites, import chains, type dependencies, and: covers refactor, simulator, blast, consequences, generalpurpose
- **related-papers-scout** (`related-papers-scout/`): Use when Discover hot related papers from elite institutions (Google, MIT, Stanford, NVIDIA) or with high Twitter/GitHub traction given an input: covers related, papers, scout, elite, institution
- **scrapling** (`scrapling/`): Use when Write Python web scraping scripts using the Scrapling framework — adaptive parsing, anti-bot bypass (Cloudflare Turnstile), concurrent: covers scrapling, 웹 스크래핑, 크롤링, adaptive, bypass
- **security-expert** (`security-expert/`): Use when Perform threat modeling (STRIDE), vulnerability assessments (OWASP Top 10), secret detection, LLM/AI-specific security checks, and PII handling: covers security, expert, 보안, 감사, assessments
- **setup-doctor** (`setup-doctor/`): Use when Scan system prerequisites, environment variables, CLI tools, Python/Node packages, and MCP servers required by all project skills, then: covers setup, doctor, diagnostic, variables, groups
- **simplify** (`simplify/`): Use when Run parallel code review agents to analyze code for reuse opportunities, code quality, tech debt, and performance issues, then auto-fix findings: covers simplify, 리뷰, 분석, individually, reuse
- **sprint-orchestrator** (`sprint-orchestrator/`): Use when Auto-triage incoming GitHub issues and PRs, classify by type, assign priority (P0-P3), suggest assignees from CODEOWNERS/git blame: covers sprint, orchestrator, assignees, blame, codeowners
- **sre-devops-expert** (`sre-devops-expert/`): Use when Design and review CI/CD pipelines, Helm charts, Kubernetes manifests, Docker Compose configs, runbooks, SLO definitions, and rollback procedures. Use when: covers sre, devops, expert, 리뷰, 배포
- **technical-writer** (`technical-writer/`): Use when Author Architecture Decision Records (ADRs), API documentation, operational guides, and changelogs. Use when the user asks to document a design: covers technical, writer, 리뷰, 생성, adr

Routing rule: when the task matches one of the sub-skills above, read the SKILL.md in that subdirectory for detailed instructions before acting;
if that sub-skill lists deeper sub-skills, repeat the descent. Load only the documents on the matching path.
<!-- /sub-skills -->
