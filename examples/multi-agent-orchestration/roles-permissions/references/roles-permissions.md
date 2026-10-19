# 角色与权限指南（roles-permissions）

面向多代理编排的实现者：定义五类角色的职责边界、上下文隔离契约、文件所有权规则与工具权限映射。除标注 [推断] 外均引自已核实出处。

## 1. 角色职责边界

| 角色 | 输入 | 产出 | 禁止事项 |
|---|---|---|---|
| **planner** | 用户 query、黑板状态（只读）、judge 的评分结果 | 任务分解方案：目标、输出格式、工具/来源指导、清晰任务边界（出处：https://www.anthropic.com/engineering/multi-agent-research-system）；方案落盘为 plan.md | 禁止直接执行子任务（避免 orchestrator 成为瓶颈/单一上下文联点，出处：https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html）；禁止写 worker 的产物文件 |
| **worker** | 任务描述 + 输出契约 + 最小必要上下文（非全历史，见 §2） | 产物写入自有目录/文件，仅回传轻量引用 + 浓缩摘要（出处：https://www.anthropic.com/engineering/multi-agent-research-system） | 禁止读取或修改其他 worker 的命名空间；禁止写共享文件（plan.md、STATUS.md）；禁止自行扩大任务范围（任务边界由 planner 给定，出处：https://www.anthropic.com/engineering/multi-agent-research-system） |
| **redteam** | 被审 artifact 的引用（只读）、攻击任务描述 | 攻击报告，写入自有命名空间（如 `redteam:<finding>`）（出处：https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production）[推断] | 禁止修改被审 artifact——攻击面结论必须基于原始产物，否则不可信（[推断]，类比 judge 只读模式） |
| **judge** | worker 产物引用、评分 rubric | 单次 LLM 调用输出 0.0–1.0 分数 + pass/fail（出处：https://www.anthropic.com/engineering/multi-agent-research-system）；verdict 写入 `judge:<worker_id>:<run>` | 禁止改写被评产物；禁止给出多个分散评分——单一 prompt 单次调用比多 judge 分项评分更一致、更贴近人类判断（出处：https://www.anthropic.com/engineering/multi-agent-research-system）。注意天然失败模式：agents 收敛到同一错误答案、judge 有偏（出处：https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html） |
| **orchestrator** | planner 的方案、worker 回传的引用、judge 评分 | 向 worker pool dispatch 任务、收集引用并合成最终结果；维护共享黑板与 STATUS.md（出处：https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html） | 禁止把 worker 产物全文拉回自己上下文（破坏压缩收益，见 §2）；禁止跳过 judge gate 直接采纳产物——critic gate 以概率 0.7 捕获失败 worker 并重试，可将成功率从 q 提升到 q+(1−q)·0.7·q，代价仅两次调用，是性价比最高的默认闭环（出处：https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html） |

角色专门化的收益：不同 system prompt 使同一模型扮演不同角色时输出先验不同，critic 的 critique 比单一上下文内的自我批评更尖锐（出处：https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html）。

补充角色变体与质量闭环（可选实现，非必需）：

- **maker-checker**：maker 用便宜快模型、checker 用强模型，可用低 40–60% 的成本获得 debate 的质量收益（出处：https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production）。
- **self-critique with routing**：orchestrator 按 rubric 给每个 worker 输出打分，低于阈值则带着 critique 重新 dispatch 给同一 worker（出处：https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html）。
- **judge 评分维度**：factual accuracy、citation accuracy、completeness、source quality、tool efficiency（出处：https://www.anthropic.com/engineering/multi-agent-research-system）。
- **redteam 证据**：本指南未覆盖的攻击者细节见 redteam-maker-checker 笔记与 Beam 的 multi-agent debate 条目（出处：https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production）。

规模与委托经验：

- worker 数量以 3–8 个为宜，再多 orchestrator 在合成时上下文装不下所有结果（出处：https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html）。
- effort scaling 规则：简单事实查找 1 个 agent + 3–10 次工具调用，直接对比 2–4 个 subagent，复杂研究 10+ 个（出处：https://www.anthropic.com/engineering/multi-agent-research-system）。
- 委托指令必须包含：目标、输出格式、工具/来源指导、任务边界——Anthropic 早期 orchestrator 只给「research the semiconductor shortage」这类过短指令，导致 subagent 误解任务或重复搜索；必须教 orchestrator 如何委托（teach the orchestrator how to delegate）（出处：https://www.anthropic.com/engineering/multi-agent-research-system）。

## 2. 上下文隔离原则

**只传任务描述，不传全历史。** 每次 API 调用都重发整个上下文；context forwarding 使成本随步数线性增长、总转发成本随链长平方增长（L 步链转发 s token/步共付 s·L(L−1)/2）（出处：https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html）。正面实践：「给 doc writer 只传函数签名，而不是完整上下文历史」（出处：https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html）。反面教训：动态 handoff 中「传全量上下文（昂贵、爆窗口）vs 摘要（有损、误差累积）」是两难，交接次数越多上下文损失越大（出处：https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production）。

**worker 输入契约** [推断]：任务描述 + 明确接口约定（输出格式、落盘路径、回传格式）+ 最小必要共享上下文，禁止整段历史透传。

**产物落盘，只回传引用。** subagent 把产出写入文件系统而非全部经 lead agent 传递，只回传轻量引用给 coordinator，避免多阶段处理的信息丢失与「传话游戏」，并降低大输出复制进对话历史的 token 开销（出处：https://www.anthropic.com/engineering/multi-agent-research-system）。subagent 本质是「智能过滤器」：各自 context window 并行探索，只把最重要的浓缩 token 返回（出处：https://www.anthropic.com/engineering/multi-agent-research-system）。

**可靠性补充。** 上下文逼近上限时，spawn 带干净上下文的新 subagent，通过精心设计的 handoff 保持连续性；计划必须持久化（出处：https://www.anthropic.com/engineering/multi-agent-research-system）。警惕错误放大：pipeline 中 stage 1 的幻觉被 stage 2 当作 ground truth；单 agent 能在同一上下文内自我纠正矛盾，而每个 stage 全新开始的 agent 做不到（出处：https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html）。

## 3. 文件所有权规则

- **写权限按目录/key 命名空间划分**：每个单元/角色拥有固定文件路径（如 `blackboard/notes/<topic>.md` 归对应 worker）[推断]；LangGraph 等框架将共享状态强类型化为 typed state，每个节点是纯函数（state → state patch），所有权边界即状态字段边界（出处：https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html）。
- **append-only 黑板**：key 用命名空间（`"agent_id:key_name"`）+ 永不覆盖 + 全量审计轨迹，可事后 replay 定位推理错误点（出处：https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html）。
- **共享文件**：plan.md、STATUS.md 只允许 orchestrator 写，其他角色只读或按约定追加 [推断]。
- **竞态意识**：N 个 agent 有 N(N−1)/2 个潜在并发交互，5 个 agent 即 10 个潜在冲突（出处：https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production）。
- **反模式 agent soup**：spawn 大量 agent 但角色边界不清，两个 agent 指令重叠会产生矛盾输出，synthesiser 无法调和（出处：https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html）。
- **独立错误处理**：单个 worker 失败不应拖垮整条 pipeline，synthesiser 需要知道哪些 worker 成功（出处：https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html）。
- sandboxing 落在 harness layer：harness 负责 SLA、成本限制与 per-agent sandboxing，之下才是 worker pool 与 tool/resource layer（出处：https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html）。

## 4. 角色 → 工具权限映射

基线 [推断]，权限模型参考 OpenCode（每个 agent 可配置 `permission`，键含 read/edit/glob/grep/list/bash/task/webfetch/websearch/skill，取值 allow/ask/deny，支持 glob 细粒度控制；规则按顺序评估、最后匹配者优先）（出处：https://opencode.ai/docs/agents/）：

| 角色 | read | edit | bash | task（subagent 调用） | external_directory |
|---|---|---|---|---|---|
| planner | allow（全仓 + 黑板） | deny（方案只经 orchestrator 落盘）或 ask | deny | deny（默认 `subagent_depth: 1` 下 subagent 无法再调 subagent；需只读探索时由 orchestrator 代为 dispatch） | ask |
| worker | allow（全仓 + 相关黑板 key） | allow：仅自有目录/文件（glob 限定） | 按类型拆分：worker-research 基本 deny（仅 ls/cat）；worker-code allow 白名单命令（构建/测试类） | deny | ask |
| redteam | allow（被审 artifact + 公开资料） | deny | ask：演示/确定性检查命令请示后放行（webfetch/websearch allow） | deny | deny |
| judge | allow（被评产物引用 + rubric） | deny | ask：重跑测试/lint 等确定性检查时请示 | deny | deny |
| orchestrator | allow（全仓） | allow（共享文件 + 任意产物目录，经引用合成时） | allow | allow：dispatch 白名单（按 glob 控制可调用的 subagent，deny 的从 Task 描述中移除，模型不会尝试调用）（出处：https://opencode.ai/docs/agents/） | ask |

生产先例（出处：https://opencode.ai/docs/agents/）：Explore 只读不改文件、Scout 只读做外部研究；Docs agent 有文件操作但无系统命令；Security auditor / code-reviewer 均 `edit: deny`——只读审阅者、无 shell 的写作者、受限 planner 均有成熟先例，按角色最小化权限即可落地。
