# OpenCode 多代理编排落地映射

> 说明：本文把多代理编排模式映射到 OpenCode 的具体配置语法。带 `[推断]` 的内容为基于机制的推断而非官方文档；OpenCode 字段均出自官方文档（出处 URL 保留）。

## 1. `opencode.json` 的 agent 配置 schema

- 配置载体二选一：① `opencode.json` 中的 `agent` 字段（JSON/JSONC，支持 `$schema`）；② Markdown 文件，放在全局 `~/.config/opencode/agents/` 或项目级 `.opencode/agents/`，文件名即 agent 名（如 `review.md` 创建 `review`）。另有 `opencode agent create` 交互式命令可生成 markdown agent（出处：https://opencode.ai/docs/agents/、https://opencode.ai/docs/cli/）
- 顶层 `agent` 是「agent 名 → 配置对象」的映射，agent 名即 key。配置对象字段：
  - `mode`：`"primary" | "subagent" | "all"`，缺省 `"all"`（出处：https://opencode.ai/docs/agents/）
  - `description`：**required**；subagent 的 description 是 primary 自动调度它的唯一依据，须写清「做什么 + 何时用」（出处：https://opencode.ai/docs/agents/）
  - `model`：`"provider/model-id"` 格式，如 `anthropic/claude-sonnet-4-20250514`；未指定时 primary 用全局 `model`、subagent 继承调用它的 primary 的 model（出处：https://opencode.ai/docs/agents/）
  - `prompt`：内联字符串或 `{file:./prompts/xxx.txt}` 文件引用（路径相对配置文件所在目录）；Markdown 形式则为 front matter + 正文 system prompt（出处：https://opencode.ai/docs/agents/、https://opencode.ai/docs/config/）
  - `permission`：对象，与全局 `permission` 同 schema（见第 4 节），per-agent 覆盖全局且 agent 规则优先（merge 语义）（出处：https://opencode.ai/docs/agents/、https://opencode.ai/docs/permissions/）
  - `steps`：agentic 迭代最大步数；旧字段 `maxSteps` 已废弃，到达上限后 agent 会收到特殊 prompt 要求总结并列出剩余任务（出处：https://opencode.ai/docs/agents/）
  - `temperature`：0.0–1.0；`top_p` 为备选多样性控制（出处：https://opencode.ai/docs/agents/）
  - `disable`（`true` 停用）、`color`（UI 颜色）、`hidden`（仅 `mode: subagent` 生效：从 `@` 菜单隐藏，仍可被 Task 工具程序化调用）（出处：https://opencode.ai/docs/agents/）
  - 其他任意字段原样透传给 provider 作 model options（如 `reasoningEffort: "high"`），官方明确 "any other options you specify are passed through directly to the provider"，无白名单（出处：https://opencode.ai/docs/agents/）
- **`tools` 字段已 deprecated**：布尔开关，`true` ≡ `{"*": "allow"}`，`false` ≡ `{"*": "deny"}`；新配置一律使用 `permission`（出处：https://opencode.ai/docs/agents/、https://opencode.ai/docs/permissions/）。注意 agents 文档某示例仍在用 `tools`，与同页废弃声明冲突，以「废弃」为准。

## 2. primary vs subagent

- primary：用户直接交互的主 agent，Tab 键或 `switch_agent` 键位切换，处理主对话（出处：https://opencode.ai/docs/agents/）
- subagent：由 primary 通过 Task 工具自动调用（依据 description 匹配），或用户 `@subagent 消息` 手动触发；每次调用创建 child session（出处：https://opencode.ai/docs/agents/）
- 内置 primary：`build`（默认、全工具）、`plan`（file edits 与 bash 默认 `ask`）；内置 subagent：`general`（全工具）、`explore`（只读）、`scout`（只读外部依赖研究）（出处：https://opencode.ai/docs/agents/）
- 会话导航：`session_child_first` 进入子会话、`session_child_cycle` 在子会话间切换、`session_parent` 返回 parent（出处：https://opencode.ai/docs/agents/）
- `default_agent` 必须指向 primary agent，否则回退 `build` 并告警（出处：https://opencode.ai/docs/config/）

## 3. per-agent 模型与权限配置示例（可粘贴）

强模型配 orchestrator/judge，便宜模型配 worker；permission 规则**最后匹配者生效**，catch-all `"*"` 必须放最前——worker 的 `edit` 收窄为 `{"*": "deny", "blackboard/notes/**": "allow"}`（只写自己的 notes 命名空间，plan.md/STATUS.md/judge/redteam 产物均不可写），judge 的 `edit` 收窄为 `blackboard/judge-*.md`，实现「写权限按文件所有权划分」：

```json
{
  "$schema": "https://opencode.ai/config.json",
  "model": "anthropic/claude-sonnet-4-20250514",
  "subagent_depth": 2,
  "agent": {
    "orchestrator": {
      "mode": "primary",
      "description": "Coordinates worker subagents via a blackboard file convention",
      "model": "anthropic/claude-sonnet-4-20250514",
      "prompt": "{file:.opencode/prompts/orchestrator.txt}",
      "permission": {
        "edit": "ask",
        "bash": { "*": "ask", "git status *": "allow" },
        "task": { "*": "deny", "worker-*": "allow" }
      }
    },
    "worker-research": {
      "mode": "subagent",
      "description": "Parallel research worker; writes notes to blackboard/notes/",
      "model": "anthropic/claude-haiku-4-20250514",
      "temperature": 0.1,
      "steps": 30,
      "prompt": "{file:.opencode/prompts/worker-research.txt}",
      "permission": { "edit": { "*": "deny", "blackboard/notes/**": "allow" }, "bash": "deny", "webfetch": "allow" }
    },
    "worker-judge": {
      "mode": "subagent",
      "description": "Judge that reviews blackboard artifacts and emits verdict files",
      "hidden": true,
      "model": "anthropic/claude-sonnet-4-20250514",
      "prompt": "You are a judge. Read inputs, emit a verdict with PASS/FAIL and evidence.",
      "permission": { "edit": { "*": "deny", "blackboard/judge-*.md": "allow" }, "bash": "ask" }
    }
  }
}
```

（出处：字段与语法见 https://opencode.ai/docs/agents/；`subagent_depth` 见 https://opencode.ai/docs/config/）

- 全局另有 `small_model`（title 生成等轻任务用便宜模型），不属 per-agent 配置（出处：https://opencode.ai/docs/config/）

## 4. permission 规则语法

- 权限 key 全集：`read`、`edit`（覆盖 write/edit/apply_patch）、`glob`、`grep`、`list`、`bash`、`task`、`external_directory`、`webfetch`、`websearch`、`lsp`、`skill`、`question`、`doom_loop`（出处：https://opencode.ai/docs/agents/）
- 每个 key 接受简写动作（`allow|ask|deny`）或「glob/pattern → 动作」细粒度对象；per-agent `permission` 覆盖全局，agent 规则优先（出处：https://opencode.ai/docs/agents/、https://opencode.ai/docs/permissions/）
- `bash` 按命令前缀授权（如 `"git *": "ask"`）；**规则最后匹配者生效**，故 catch-all `"*"` 应放在最前（出处：https://opencode.ai/docs/agents/、https://opencode.ai/docs/permissions/）
- `edit` 按文件路径授权：`{"*": "deny", "blackboard/**": "allow"}` —— 「文件所有权」角色的落地手段（出处：https://opencode.ai/docs/permissions/）
- `task` 用 glob 控制可调用哪些 subagent：被 deny 的会从 Task 工具描述中移除，但用户始终可通过 `@` 菜单直接调用任何 subagent（出处：https://opencode.ai/docs/agents/）
- 默认值：多数权限默认 `allow`；`doom_loop`、`external_directory` 默认 `ask`；`read` 默认 allow 但 `*.env` 系列默认 deny（出处：https://opencode.ai/docs/permissions/）
- 收紧手段：`--auto`/`opencode run --auto` 自动批准未显式 deny 的请求；`"*": "ask"` 可作全局基线；`ask` 弹窗三选 `once`/`always`（本会话内匹配 pattern 永久批准）/`reject`；环境变量 `OPENCODE_PERMISSION` 可内联 JSON 权限（出处：https://opencode.ai/docs/permissions/、https://opencode.ai/docs/cli/）

## 5. 嵌套编排

- `subagent_depth` 控制嵌套深度，默认 `1`（primary 可起 subagent，subagent 不能再起）；`0` 全禁；层级编排 orchestrator→worker→worker 须显式设 `2`（出处：https://opencode.ai/docs/config/）
- 配合 per-agent `permission.task`（如 orchestrator 只放行 `"worker-*"`）实现层级调度与越权隔离（出处：https://opencode.ai/docs/agents/、https://opencode.ai/docs/permissions/）
- 失控保护三件套：`steps` 迭代上限（到达后强制总结并列剩余任务）、`doom_loop`（同参数重复调用 3 次触发 `ask`）、`compaction`（`auto`/`prune`/`reserved` 控制长上下文压缩）（出处：https://opencode.ai/docs/agents/、https://opencode.ai/docs/permissions/、https://opencode.ai/docs/config/）

## 6. 黑板文件约定

- OpenCode 无内置 blackboard/message-bus；subagent 间唯一的原生通信通道是 Task 工具返回值（子会话摘要）与共享文件系统 [推断]
- 目录约定：`blackboard/` 为共享状态根，内含 `STATUS.md`（断点状态）、`notes/`（各单元 append-only 产出）、`judge-r<N>.md`（judge 判定文件，N 为轮次，见 blackboard-convention.md）[推断]
- worker 的 `permission.edit` 只放行 `blackboard/**`、其余 deny，实现「黑板可写、源码只读」边界（permission 语法出处：https://opencode.ai/docs/permissions/；机制为 [推断]）
- **STATUS.md 断点续跑协议**：每个工作单元以文件为粒度切分；单元完成 → 更新 STATUS.md（标记 done + 产物路径）→ 继续下一单元；任何 agent 恢复时先读 STATUS.md 决定执行哪一单元；notes 目录 append-only，只追加不覆盖 [推断]
- 双保险：文件级黑板状态（STATUS.md + notes）+ 会话级续跑（`--continue`/`-c`、`--session <ID>`、`--fork` 分叉）；`opencode session list` 列会话、`opencode export/import` 导出导入会话 JSON、`opencode stats` 看 token 成本（会话命令出处：https://opencode.ai/docs/cli/）

## 7. 后台长跑

- `opencode run "prompt"`：非交互执行，适合脚本化与后台；支持 `--agent`、`--model`、`--format json`、`--title`、`--file`（出处：https://opencode.ai/docs/cli/）
- `opencode serve` 常驻 headless server，`opencode run --attach http://localhost:4096 "..."` 连接已有 server，避免每次冷启动 MCP（出处：https://opencode.ai/docs/cli/）
- 推荐组合：`opencode serve` + 多路 `opencode run --attach`；或 shell 后台 `nohup opencode run ... > log 2>&1 &`（后者为 [推断]）
- 每个 subagent 在 child session 中运行，可通过 TUI 键位实时查看/介入子会话（出处：https://opencode.ai/docs/agents/）
