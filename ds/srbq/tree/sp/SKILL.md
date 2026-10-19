---
name: sp
description: "Use when the request concerns the sp category of skills: covers sp"
---

Grouping node for the 0 skills of the sp category. 

<!-- sub-skills -->
## Sub-skills (auto-generated, do not edit by hand)

- **sp-brainstorming** (`sp-brainstorming/`): Use when You MUST use this before any creative work - creating features, building components, adding functionality, or modifying behavior: covers brainstorming, 브레인스토밍, 아이디어, explores, modifying
- **sp-core** (`sp-core/`): Use when Use when starting any conversation - establishes how to find and use skills, requiring Skill tool invocation before ANY response including: covers core, 스킬 호출, 스킬 시작, establishes, invocation
- **sp-debugging** (`sp-debugging/`): Use when Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes. Korean triggers, "디버깅", "버그 추적". Do NOT: covers debugging, 디버깅, 버그 추적, proposing, encountering
- **sp-executing-plans** (`sp-executing-plans/`): Use when Use when you have a written implementation plan to execute in a separate session with review checkpoints. Korean triggers, "계획 실행", "구현 플랜": covers executing, plans, 계획 실행, 구현 플랜, written
- **sp-finish-branch** (`sp-finish-branch/`): Use when Use when implementation is complete, all tests pass, and you need to decide how to integrate the work - guides completion of development: covers finish, branch, 브랜치 완료, 작업 마무리, finishing
- **sp-git-worktrees** (`sp-git-worktrees/`): Use when Use when starting feature work that needs isolation from current workspace or before executing implementation plans - creates isolated git: covers git, worktrees, 워크트리, 기능 분리, isolation
- **sp-parallel-agents** (`sp-parallel-agents/`): Use when Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies. Do NOT use for: covers parallel, abort, aborted, adjusting, concurrently
- **sp-receive-review** (`sp-receive-review/`): Use when Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionable -: covers receive, review, 리뷰 피드백, 코드 리뷰 수정, blind
- **sp-request-review** (`sp-request-review/`): Use when Use when completing tasks, implementing major features, or before merging to verify work meets requirements. Korean triggers, "리뷰 요청", "코드 리뷰": covers request, review, 리뷰 요청, 코드 리뷰, receive
- **sp-subagent-dev** (`sp-subagent-dev/`): Use when Use when executing implementation plans with independent tasks in the current session. Korean triggers, "서브에이전트", "독립 태스크". Do NOT use for: covers subagent, dev, 서브에이전트, 독립 태스크, independent
- **sp-tdd** (`sp-tdd/`): Use when Use when implementing any feature or bugfix, before writing implementation code. Korean triggers, "TDD", "테스트 주도", "테스트 먼저 작성". Do NOT use for: covers tdd, TDD, 테스트 주도, 테스트 먼저 작성, bugfix
- **sp-verification** (`sp-verification/`): Use when Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification commands and: covers verification, 검증, 완료 확인, assertions, claim
- **sp-writing-plans** (`sp-writing-plans/`): Use when Use when you have a spec or requirements for a multi-step task, before touching code. Do NOT use for executing plans (use: covers writing, plans, touching, executing, spec
- **sp-writing-skills** (`sp-writing-skills/`): Use when Use when creating new skills, editing existing skills, or verifying skills work before deployment. Korean triggers, "스킬 작성", "스킬 편집". Do NOT use: covers writing, skills, 스킬 작성, 스킬 편집, active

Routing rule: when the task matches one of the sub-skills above, read the SKILL.md in that subdirectory for detailed instructions before acting;
if that sub-skill lists deeper sub-skills, repeat the descent. Load only the documents on the matching path.
<!-- /sub-skills -->
