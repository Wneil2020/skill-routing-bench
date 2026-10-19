---
name: opencode-setup
description: "Use when 在 OpenCode 中配置子代理编排: covers opencode, permission, 黑板, 断点续跑"
metadata:
  holon-triggers: |
    在 opencode 中配置子代理的 permission 规则
    黑板文件约定和断点续跑怎么做
    辩论循环最大轮数设多少 should go to /convergence
---

# opencode-setup：落地到 OpenCode

1. 在 `opencode.json` 的 `agent` 字段配置角色：`mode: subagent`、`description`（primary 自动调度的唯一依据，写清做什么+何时用）、`prompt`、`model`、`permission`；`tools` 字段已 deprecated，统一用 `permission`，旧 `maxSteps` 用 `steps`。
2. 直接复制 `scripts/opencode-agent-templates.json`：orchestrator（primary）+ planner / worker-research / worker-code / redteam / judge 六个角色的配置模板（worker 写权限限定目录、judge 与 redteam 只读产物且 bash 走 ask 请示、planner 只写 blackboard）。
3. 编排者 primary 用 `permission.task` 白名单只放行 `planner` / `worker-*` / `redteam` / `judge`（其余 deny）；嵌套编排须显式 `subagent_depth: 2`，否则 subagent 不能再起 subagent。
4. 强弱模型搭配：per-agent `model` 直接配 `provider/model`，强模型配 orchestrator/judge，便宜模型配 worker。
5. 黑板机制：按 `references/blackboard-convention.md` 建 blackboard/ 目录（plan.md、STATUS.md、notes/、append-only 规则），断点续跑 = 文件级黑板状态 + 会话续跑（`--continue` / `--session` / `--fork`）。
6. 后台长跑：`opencode serve` 常驻 + `opencode run --attach`，避免 MCP 冷启动；失控保护三件套 `steps` 上限、`doom_loop` ask、`compaction`。
7. 字段级 schema、permission 语法细节与出处见 `references/opencode-mapping.md`。

<!-- sub-skills -->
<!-- /sub-skills -->
