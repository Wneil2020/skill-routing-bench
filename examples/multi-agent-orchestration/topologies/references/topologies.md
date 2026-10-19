# 深入参考：多代理拓扑（Topologies）

> 本文是 SKILL.md 的深入参考，面向"要用本 skill 编排任务"的代理。每种拓扑一节：定义 → 适用条件 → 失败模式 → 最小实现要点。末尾附选择速查表。
> 写作立场：先找最简方案，只有简单方案不够时才增加复杂度；agentic 系统以延迟和成本换取任务表现，这个交换必须论证值得（出处：https://www.anthropic.com/engineering/building-effective-agents）。
> 定量背景：单代理 + 相同工具/上下文在 64% 的 benchmark 任务上追平或超过多代理系统；多代理仅 +2.1pp 精度、成本约翻倍（Princeton NLP，经 Beam 转引，出处：https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production）。同源模型采样共享系统性盲区 ρ，再多代理也突破不了 1-ρ 的天花板（出处：https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html）。

## 1. Orchestrator-worker（star）

```
        ┌─ worker A
task ──▶ orchestrator ─┼─ worker B
        └─ worker C
```

- 定义：一个中心 agent 接收任务、拆解为子任务、分发给 specialist worker 并汇总结果；orchestrator 用强模型，worker 可用更便宜的任务专用模型（出处：https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production；https://www.anthropic.com/engineering/building-effective-agents）。
- 适用条件：子任务在设计期可知，或形态不可预知但需单一问责点的复杂任务（多文件代码修改、多源信息搜集）；广度优先、多独立方向并行的查询收益最大——Anthropic 内部评测中 Opus 4 lead + Sonnet 4 subagent 比单 Opus 4 高 90.2%（出处：https://www.anthropic.com/engineering/multi-agent-research-system）。
- 失败模式：orchestrator 是单点故障，任务误分类会派发给错误 worker 且随规模复合放大；orchestrator 累积所有 worker 上下文，≥4 个 worker 时频繁爆 context window；成本随执行量暴涨（测试期 $0.50 的流程在 100K 次执行后可达 $50,000/月）；plan 与 synthesis 本身也是模型调用，会丢件或篡改结果（出处：https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production；https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html）。
- 最小实现要点：
  1. 委派 prompt 必须写明 objective、输出格式、工具/来源指引、清晰任务边界，防止 subagent 误解或重复劳动（真实案例：一个查 2021 汽车芯片危机、另两个重复调查 2025 供应链）；按查询复杂度配 effort：1 agent/3-10 次工具调用 → 简单事实；2-4 subagent → 直接对比；>10 subagent → 复杂研究（出处：https://www.anthropic.com/engineering/multi-agent-research-system）。
  2. 合成结果时逐项核对 worker 回传件，不全则要求补齐，不让 orchestrator 凭印象补全。
  3. worker ≥4 或 context 吃紧时，把计划与产物写文件/Memory、只回传轻量引用（见 blackboard 拓扑）。

## 2. Pipeline（chain / sequential）

```
A ──▶ B ──▶ C ──▶ D     （顺序固定，由代码而非模型决定）
```

- 定义：agent 按设计期固定的线性顺序执行，每个 agent 通过共享状态处理前一个 agent 的输出；可回溯性来自代码而非模型决策（出处：https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production；https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html）。对应 Anthropic 的 prompt chaining（可带 programmatic gate）（出处：https://www.anthropic.com/engineering/building-effective-agents）。
- 适用条件：有清晰线性依赖的多阶段流程——parse→extract→validate→summarize、合同生成、翻译后润色、先大纲后成文；各阶段需不同权限或不同上下文、单次会话 context 会撑爆时优于一个长会话（出处：https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production；https://developertoolkit.ai/en/workflows/automate/orchestration-patterns/）。
- 失败模式：错误传播——第 1 阶段的坏输出无回退地级联到所有下游（N 阶段 pipeline 可靠度约 q^(2N-1)，每次交接都是"错误被继承为 ground truth"的点位）（出处：https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html）；协调与 token 开销——4 agent pipeline 约 950ms 协调开销 vs 500ms 实际处理，3 agent 耗 29K token vs 单 agent 10K（出处：https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production）。
- 最小实现要点：
  1. 阶段间只交接**可校验的文件**而非散文：对照 schema 的 JSON、带验收命令的 branch；交接 prose 只会累积彼此的错误（出处：https://developertoolkit.ai/en/workflows/automate/orchestration-patterns/）。
  2. 每个 stage 入口先做 schema/确定性校验，不通过则拒绝输入或打回上游，不做"尽力而为"。
  3. 若相邻阶段不需要真正的专业化，合并它们——不为同一结果付 3 倍价（出处：https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production）。

## 3. Debate + judge（peer-to-peer）

```
A ──▶ shared thread ◀── B ──▶ ... ──▶ judge 选优 / 判 none
maker → checker（通过为止）  或  best-of-N + judge
```

- 定义：多个 agent 在共享对话中提出立场、相互挑战、跨轮次精炼；变体含 maker-checker（一写一验到通过）与 best-of-N + judge（N 次独立尝试，judge 基于证据选优）（出处：https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production；https://developertoolkit.ai/en/workflows/automate/orchestration-patterns/）。
- 适用条件：需要多专家视角的合规审查、质量保障、高代价错误场景；debate 能降低幻觉（互相抓错）；可用便宜快模型做 maker、强模型做 checker，以 40-60% 更低成本获得 debate 的质量提升（出处：https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production）。best-of-N 要求解空间宽且存在可判定优劣的确定性证据（reproduction test、benchmark、spec check）（出处：https://developertoolkit.ai/en/workflows/automate/orchestration-patterns/）。统计学边界：ensembling 收益在单 agent 成功率 p 中等时最大，p≈1 或 p≈0 只加成本；必须主动 decorrelate——不同基座模型、persona/分解、工具、更高 temperature；同一模型 temperature 0 的 N 份拷贝完全不降低 ρ（出处：https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html）。
- 失败模式：对话循环不收敛（3 agent × 5 轮 = 每任务 15 次 LLM 调用，Microsoft 建议 group chat ≤3 agent）；sycophancy cascading——倾向认同多数立场即使多数错了，产生虚假共识；judge 失效三态：只读代码不跑检查、与 writer 共享上下文、有编辑权导致"自我实现"的 verdict（出处：https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production；https://developertoolkit.ai/en/workflows/automate/orchestration-patterns/）。
- 最小实现要点：
  1. judge 三铁律：先跑确定性检查再评级（证据优先于口味）；候选匿名化（剥离 agent 名、模型名、轮次号）且跨轮打乱顺序；judge 无编辑权（移除 Edit/Write 权限）、每条 verdict 必带 command + exit code、与 CI 结果对账，全不合格判 "none"（出处：https://developertoolkit.ai/en/workflows/automate/orchestration-patterns/）。
  2. 硬上限：最大轮数、最大 fix 轮数（writer/reviewer 最多 2 轮后升人）；在 prompt 中显式鼓励质疑而非附和，对冲 sycophancy（出处：https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production；https://developertoolkit.ai/en/workflows/automate/orchestration-patterns/）。

## 4. Blackboard（shared state）

```
        ┌──────────────┐
worker A ═▶│ blackboard   │◀═ worker B   （读写共享状态，非直接互发消息）
        └──────┬───────┘
               ▼ optional coordinator 轮询决定推进
```

- 定义：用外部共享数据结构替代 orchestrator 上下文，agent 读写 blackboard 而非直接互发消息；可选 coordinator 轮询 blackboard 决定推进时机；append-only 写入天然带完整审计轨迹，可事后 replay 定位推理出错点（出处：https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html）。
- 适用条件：worker 数量增长（3-8 个以上）导致 orchestrator 上下文成为瓶颈时；需要并发写者、涌现式综合（emergent synthesis）；需要完整审计轨迹的可调试性要求（出处：https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html）。落地变体：lead agent 把研究计划写入 Memory 持久化（context 超 200K 会被截断）；subagent 产出写文件系统、只回传轻量引用，避免"传话游戏"式信息丢失并降低 token 开销（出处：https://www.anthropic.com/engineering/multi-agent-research-system）。
- 失败模式：race condition、stale read、key 冲突——共享状态架构必须有 thread-safe 访问与显式冲突解决（出处：https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html）；N 个 agent 有 N(N-1)/2 个潜在并发交互点（5 agent = 10，10 agent = 45）；聚合步骤若用 LLM synthesis 可能幻觉出不存在的共识，并行 agent 意见相左（一个说买、一个说卖）时必须有显式冲突解决策略而非"总结一下结果"（出处：https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production）。
- 最小实现要点：
  1. 规定写入格式（如分节 markdown，含 status 字段），写入必须原子（一次写完整节）或加锁；读者写明所读版本，防 stale read。
  2. 每个 key/路径声明 owner，key 冲突靠 owner 仲裁而非先到先得（出处：https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html）。
  3. 冲突解决走确定性检查或可追溯的裁决流程，不用"让 LLM 综合一下"收场（出处：https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production）。

## 5. Hierarchical（tree）

```
root orchestrator
 ├─ sub-orchestrator 1 ── workers
 └─ sub-orchestrator 2 ── workers   （递归委派）
```

- 定义：递归委派的树形结构——root orchestrator 下辖 sub-orchestrator，再管自己的 worker；CrewAI 的 Process.hierarchical 即由 manager LLM 决定任务顺序的实例（出处：https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html）。
- 适用条件：任务大到单层 orchestrator 的上下文/能力装不下，需要递归分解；适合结构化 pipeline 的快速原型（出处：https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html）。
- 失败模式：延迟爆炸、跨树通信笨拙（出处：https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html）；扁平变体 dynamic handoff（无中心协调者）的头号失败模式是 A→B→C→A 无限 handoff 循环——每次转交丢上下文（传全文则贵且爆窗、传摘要则有损且错误累积），路由非确定导致同样输入产生完全不同的 agent 链，调试困难（出处：https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production）。
- 最小实现要点：
  1. handoff 次数硬上限 + 每次转交附结构化简报（已完成项/剩余项/已试过的失败路径），不要用自由文本转述全文（出处：https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production）。
  2. 树深控制在 2 层以内，除非有明确证据单层装不下；层数每加一，延迟与上下文转发成本按链长相乘 [推断，基于 hybrid 节的转发成本规律，出处：https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html]。
  3. 跨子树共享的信息走 blackboard，不走逐层上传再下发的转发链（出处：https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html）。

## 6. Hybrid（组合拓扑）

- 定义：真实生产系统通常组合两种以上经典拓扑；外层用 workflow 壳保证确定性与可审计性，内层把 agent 放在叶子节点处理不可预知的子任务（出处：https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html）。实例：Anthropic Research = orchestrator-worker + pipeline 收尾（CitationAgent）+ 记忆外置（plan 写 Memory）（出处：https://www.anthropic.com/engineering/multi-agent-research-system；https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html）。同一套角色（planner/worker/judge）可在 fan-out、pipeline、best-of-N、writer/reviewer 中不同接线——hybrid 是零件库不是新物种（出处：https://developertoolkit.ai/en/workflows/automate/orchestration-patterns/）。
- 适用条件：单拓扑的天生短板须由另一拓扑补偿时（pipeline 的确定性 + orchestrator-worker 的动态拆解；worker 太多时 orchestrator 上下文换 blackboard）（出处：https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html）。[推断：补偿点即接口，接口处是错误传播和成本翻倍的高发区。]
- 失败模式：叠加各拓扑的失败模式，且上下文转发链更长，token 账单与延迟按链长相乘；MAST 分类学（14 种失败模式）指出多数多代理失败是组织性的而非能力性的；通用反模式：agent soup（角色边界不清）、infinite loops（无迭代上限）、blind trust（无输出校验）、over-parallelism（无视 rate limit）（出处：https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html）。
- 最小实现要点：
  1. 画出接线图并标注每处接口的交接物（artifact）与验收方式；无法说清交接物的地方就是风险点 [推断]。
  2. 为每个环、每次 handoff、每轮 fix 设硬上限，并预设 token/并发上限（出处：https://developertoolkit.ai/en/workflows/automate/orchestration-patterns/）。
  3. 决策原则：一个 agent 能在上下文里装下的问题就留在单 agent；编排买到的是广度、隔离与可靠性，从来不是更便宜的难题（出处：https://developertoolkit.ai/en/workflows/automate/orchestration-patterns/）。

## 拓扑选择速查

按「工作形状」而非 agent 数量选（出处：https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production；https://developertoolkit.ai/en/workflows/automate/orchestration-patterns/）：

| 你的工作形状 | 首选拓扑 | 关键约束 |
|---|---|---|
| 固定线性步骤、阶段间可产出可校验 artifact | pipeline | 只交接 schema 化文件；每级入口校验 |
| 子任务设计期可知、需单一问责点 | orchestrator-worker | 委派 prompt 写全边界；≥4 worker 时外置状态 |
| 多独立方向并行搜索/广度优先 | orchestrator-worker（fan-out） | 防重复劳动，列 owned_paths + 覆盖率对账 |
| 质量验证、高代价错误、需多视角 | debate+judge / maker-checker | judge 三铁律；decorrelate 候选；设轮数上限 |
| 长程运行、需审计轨迹、worker 多且并发写 | blackboard | 原子写、owner 仲裁、显式冲突解决 |
| 任务大到单层 orchestrator 装不下 | hierarchical | handoff 硬上限；树深 ≤2 层优先 |
| 单拓扑短板明显、任务形状混合 | hybrid | 标注接口交接物；所有循环硬上限 |

升级触发线：只有当上下文溢出、需要并行/隔离、或错误代价高于多倍 token 时，才从单 agent 升级为多代理（出处：https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html；https://www.anthropic.com/engineering/building-effective-agents）。成本口径：多代理税真实存在（Anthropic 实测约 15× token；DoltHub 实测 Gas Town 一小时约 $100；llm-stack 章节口径：5-agent pipeline 含 context forwarding 约 3–5× token），须以任务价值对冲（出处：https://www.anthropic.com/engineering/multi-agent-research-system；https://developertoolkit.ai/en/workflows/automate/orchestration-patterns/；https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html）。
