# 多代理编排失败模式排障手册

> 使用方式：先按现象定位到对应失败模式，按"排查步骤"逐项验证，再落地"预防"措施；末尾 checklist 用于上线前自查与事故复盘。
> 核心背景：多数失败是 organisational 而非 capability——单次模型调用正常，系统仍然失败；工程精力应投在角色规范、交接校验、真实验证，而不是加更多 agent（MAST，出处：https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html）。

## 1. 上下文膨胀（context bloat / overflow）

- **症状**：orchestrator 汇总 worker 输出时 context 超限被截断；pipeline 后期阶段 input token 线性增长、总账单接近二次方；简单查询也被分解出大量子任务（出处：https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production；https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html）
- **根因**：orchestrator 是单一集成点，须把所有 worker 结果放进自己的 context；context forwarding 使每个后续 call 携带此前所有阶段摘要，L 步链的转发成本为 s·L(L−1)/2；orchestrator-worker 模式中 ≥4 个 worker 时 context 常超窗（出处：https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html；https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production）
- **排查步骤**：
  1. 监测每次调用的 input token 随阶段索引的增长曲线，确认是否线性/超线性增长
  2. 检查 orchestrator 在 synthesis 前是否已接近窗口上限
  3. 确认长任务（>200k token）的 plan 是否持久化到外部 memory 而非留在 context（出处：https://www.anthropic.com/engineering/multi-agent-research-system）
- **预防**：subagent 产物写文件系统、只回传轻量引用，避免"传话游戏"式逐级拷贝；由 agent 总结已完成阶段、关键信息存入外部 memory，临近上限时派生干净 context 的新 subagent 并做仔细交接（出处：https://www.anthropic.com/engineering/multi-agent-research-system）；3–8 个 worker 以上改用 blackboard 共享状态替代 orchestrator context 作为集成点 [推断]

## 2. 错误级联（error cascade / blind trust）

- **症状**：stage 1 的错误被下游当作 ground truth 一路传到最后；orchestrator 把 worker 的畸形 JSON 或未验证输出直接转发；产物"自信地错误"（出处：https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html；https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production）
- **根因**：单 context 内矛盾可见、agent 可自纠；跨 context 后下游没有原始上下文去反驳上游错误；N−1 次 pipeline 交接每一处都是"错误被继承为真值"的机会，可靠度约按 q^(2N−1) 相乘（出处：https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html）
- **排查步骤**：
  1. 对失败样本做全链路 trace，定位第一个出错阶段
  2. 检查每个交接边界是否有 schema/内容校验
  3. 对照 single-agent baseline，确认错误是否由分解引入（出处：https://www.anthropic.com/engineering/multi-agent-research-system）
- **预防**：每个 inter-agent 边界用结构化 schema（如 Pydantic）校验 payload，失败要 fail loudly 而非静默污染下游；在 agent 边界放 critic gate——玩具模型中它是"最大单项收益"（约两次调用的代价换取 q 提升）（出处：https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html）；pipeline 各阶段交接可校验的文件（plan.json 对 schema、branch 对验收命令）而非散文（出处：https://developertoolkit.ai/en/workflows/automate/orchestration-patterns/）

## 3. Herding / 过早共识（含 sycophancy cascading）

- **症状**：辩论几轮后 agent 迅速趋同到同一个（可能错误的）答案；结果"自信地错误"；收敛很快但质量未提升（出处：https://arxiv.org/abs/2509.23537；https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production）
- **根因**：agent 倾向于附和大流立场（sycophancy cascading）；实证消融显示向 agent 展示进行中投票会放大 herding——加速收敛但可能造成过早共识；展示答案作者身份会增加 self-voting 与平局（出处：https://arxiv.org/abs/2509.23537）
- **排查步骤**：
  1. 记录每轮各 agent 立场变化，看是否在引入新证据前就倒向多数
  2. 检查 judge/聚合 prompt 是否泄漏了作者身份或当前票数
  3. 对比匿名化前后的一致性（出处：https://arxiv.org/abs/2509.23537）
- **预防**：judge 做 blind comparison——剥离 agent 名、模型名、attempt 编号，并在多次运行间打乱候选顺序（出处：https://developertoolkit.ai/en/workflows/automate/orchestration-patterns/）；用不同 base model、刻意不同 persona/拆解、不同工具访问或更高 temperature 主动 decorrelate agent——同模型同 prompt 的 N 个样本共享系统性盲点，无法突破 1−ρ 上限（出处：https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html）；给辩论设最大轮数与显式停止条件（出处：https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production）

## 4. 死循环 / 不收敛 / goal drift

- **症状**：debate 组内反复讨论不收敛；dynamic handoff 中 A→B→C→A 循环（头号失败模式）；writer/reviewer 打到第 5 轮；manager 对模糊目标无限迭代建"完整"计划；backtracking 时整条分支白算（出处：https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production；https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html；https://developertoolkit.ai/en/workflows/automate/orchestration-patterns/）
- **根因**：没有硬迭代上限（max_turns/max_iterations）；每次 transfer 无人拥有任务、人人重新规划；目标欠定义（MAST 中 termination condition 错误属 specification issues）；多次迭代后 manager 的 refined plan 偏离原始意图（goal drift）（出处：https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html；https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production）
- **排查步骤**：
  1. 统计 handoff 链长度，检测同一 agent 重复出现的循环（A→B→C→A）
  2. 记录 writer/reviewer 实际轮数
  3. 检查目标是否可验证（有无 pass/fail 判据）（出处：https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production）
- **预防**：永远设 max_turns/max_iterations 硬上限（出处：https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html）；writer/reviewer 固定"最多两轮修复，之后交人工"的停止规则（出处：https://developertoolkit.ai/en/workflows/automate/orchestration-patterns/）；group chat 控制在 3 个 agent 以内以防对话循环（出处：https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production）
- **冲突观点**：Anthropic 用 prompt 中的 scaling rules 而非硬循环上限来匹配投入（出处：https://www.anthropic.com/engineering/multi-agent-research-system）；llm-stack 与 beam 主张硬上限更可靠。实践建议两者结合：软启发式决定投入规模 + 硬上限兜底成本 [推断]

## 5. 文件冲突与 race condition（file collision & shared-state race）

- **症状**：多个 worker 重写同一个文件（barrel files、route 注册、共享类型）；同一 key 被并发写覆盖；读到过期数据；干净报告掩盖缺失覆盖（worker 被停或 API 报错，fan-in 把空结果丢弃）（出处：https://developertoolkit.ai/en/workflows/automate/orchestration-patterns/；https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production）
- **根因**：planner 把共享文件划进了两个 unit；blackboard 天然面临 race condition、stale read、key collision；N 个 agent 有 N(N−1)/2 个潜在并发交互，5 个 agent 即 10 个、10 个即 45 个（出处：https://developertoolkit.ai/en/workflows/automate/orchestration-patterns/；https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production）
- **排查步骤**：
  1. git diff 路径比对，找出出现在多个 unit owned_paths 的路径
  2. blackboard 用 append-only + 全量审计 trace 事后 replay 定位写冲突（出处：https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html）
  3. 检查 fan-in 是否丢失失败/空结果（失败的 agent() 调用 resolve 为 null）（出处：https://developertoolkit.ai/en/workflows/automate/orchestration-patterns/）
- **预防**：一个 path 不得出现在两个 unit 的 owned_paths，多 unit 共享的文件进 foundation 串行先落；worktree 隔离 + lane-gate 脚本（git diff --name-only 对 lane 白名单校验），无模型参与；blackboard 用命名空间 key（agent_id:key）、锁、append-only 版本化（出处：https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html）；worktree baseRef 设为 "head" 而非默认 "fresh"，否则 worker 从默认分支分叉、重复实现已有代码；fan-in 必须产出"未完成清单"并重跑缺失项（出处：https://developertoolkit.ai/en/workflows/automate/orchestration-patterns/）

## 6. 成本失控（cost runaway）

- **症状**：测试时 $0.50 的 workflow 在 100K 执行量下到 $50,000/月（出处：https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production）；Gas Town 一小时约 $100（约为正常 Claude Code 会话单位时间成本的 10 倍）（出处：https://developertoolkit.ai/en/workflows/automate/orchestration-patterns/）；多代理 token 用量约为普通对话的 15 倍（出处：https://www.anthropic.com/engineering/multi-agent-research-system）
- **根因**：orchestrator 在分解+聚合上额外多次调用；每次 API call 重发整个 context；3-agent pipeline 约 29,000 token vs 单 agent 10,000；早期 agent 曾为简单查询派出 50 个 subagent、无休止搜索不存在的来源（出处：https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production；https://www.anthropic.com/engineering/multi-agent-research-system）
- **排查步骤**：
  1. 先量 token 再谈优化——三因素（token 用量、工具调用次数、模型选择）合计可解释 95% 的 BrowseComp 性能方差，其中 token 用量单独解释 80%
  2. 按 stage/agent 归因账单
  3. 对比 single-agent baseline 的 cost per successful run（出处：https://www.anthropic.com/engineering/multi-agent-research-system；https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html）
- **预防**：prompt 中嵌入 scaling rules（简单事实查询 1 个 agent + 3–10 次工具调用；对比类 2–4 subagent 各 10–15 次；复杂研究 >10 subagent 且分工明确）（出处：https://www.anthropic.com/engineering/multi-agent-research-system）；工具侧预算控制：--max-budget-usd、max_goal_token_budget、max_threads、workflowSizeGuideline（出处：https://developertoolkit.ai/en/workflows/automate/orchestration-patterns/）；maker 用便宜快模型、checker 用强模型，可省 40–60%；只在任务价值足以支付溢价时用多代理——质量增益与成本都要实测（出处：https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production；https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html）

## 7. Judge 被 maker 污染（judge capture）

- **症状**：judge 全批通过、候选随后挂 CI；reviewer 批准了自己 context 里的代码；聚合步幻觉出底层结果中不存在的共识；聚合冲突时只是"summarize the results"而没有显式冲突解决（出处：https://developertoolkit.ai/en/workflows/automate/orchestration-patterns/；https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production）
- **根因**：judge 只读代码不跑检查、与 writer 共享 context、或能编辑代码（把判决做成真值）；reveal authorship 增加 self-voting；LLM-based synthesis 可幻觉出共识（出处：https://developertoolkit.ai/en/workflows/automate/orchestration-patterns/；https://arxiv.org/abs/2509.23537；https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production）
- **排查步骤**：
  1. 对比最近 5 次 judge verdict 与 CI 结果，不一致即 judge prompt 是 bug
  2. 检查 judge 的 tools 列表是否含 Edit/Write
  3. 检查候选是否带 agent/attempt 标识（出处：https://developertoolkit.ai/en/workflows/automate/orchestration-patterns/）
- **预防**：judge 只读（移除 Edit/Write）、每条 verdict 须带命令与 exit code、blind 评审、可全不给 winner 时输出 "none"；确定性检查优先于模型判断——judge 先跑 reproduction test、type check、lane tests，只对通过者评风格（以上出处：https://developertoolkit.ai/en/workflows/automate/orchestration-patterns/）；用带 rubric（事实准确、引用准确、完整、来源质量、工具效率）的单次 LLM judge 打 0–1 分 + pass/fail，比多 judge 组合更一致（出处：https://www.anthropic.com/engineering/multi-agent-research-system）；judge 不替换 CI，APPROVE 不替换 gates；防"oracle 被 weakening"：worker 不得改动评判它的测试（出处：https://developertoolkit.ai/en/workflows/automate/orchestration-patterns/）

## Troubleshooting Checklist（上线前自查 / 事故复盘）

按"现象 → 检查项"组织，逐项打勾 [推断]：

- [ ] 1. 输出整体质量差 → 已跑 single-agent baseline；多代理仅在有 decorrelation 与实测增益时保留（出处：https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html）
- [ ] 2. 结果"自信地错误" → 交接边界有 schema 校验；critic gate 在链路里；已做全链路 trace 定位第一个出错阶段（出处：https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html）
- [ ] 3. 辩论过早一致 → 未向 agent 展示进行中投票/作者身份；已启用匿名化与 blind comparison（出处：https://arxiv.org/abs/2509.23537；https://developertoolkit.ai/en/workflows/automate/orchestration-patterns/）
- [ ] 4. 循环/不收敛/卡死 → max_turns/最大轮数/handoff 深度上限已配置；已检测 A→B→C→A 环；writer/reviewer ≤ 两轮；goal 有 pass/fail 判据（出处：https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html；https://developertoolkit.ai/en/workflows/automate/orchestration-patterns/）
- [ ] 5. 合并冲突/文件被覆写 → owned_paths 交集为空；共享文件进 foundation 串行先落；lane-gate 已启用；worktree baseRef 正确（出处：https://developertoolkit.ai/en/workflows/automate/orchestration-patterns/）
- [ ] 6. 报告"干净"但覆盖不全 → fan-in 产出"未完成清单"；未丢弃 null/空结果；缺失项已重跑（出处：https://developertoolkit.ai/en/workflows/automate/orchestration-patterns/）
- [ ] 7. 账单爆炸 → 已按 stage 归因 token；scaling rules 生效；预算上限（max-budget-usd、token budget、并发上限）已配置（出处：https://www.anthropic.com/engineering/multi-agent-research-system；https://developertoolkit.ai/en/workflows/automate/orchestration-patterns/）
- [ ] 8. judge 全过但 CI 挂 → judge 只读（无 Edit/Write）；verdict 带命令 + exit code；blind 评审；近 5 次 judge verdict 与 CI 一致（出处：https://developertoolkit.ai/en/workflows/automate/orchestration-patterns/）
- [ ] 9. 频繁 rate limit/限流 → 并发数对照 rate limit 建模为线程池约束；重试带指数退避（出处：https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production）
- [ ] 10. 子任务重复/遗漏 → 委派指令含 objective/输出格式/工具指引/边界；plan 经人类签收（出处：https://www.anthropic.com/engineering/multi-agent-research-system）
- [ ] 11. 上线后行为漂移 → 全链路 tracing（监控决策模式与交互结构，非对话内容）；prompt registry 版本化；rainbow deployment 灰度（出处：https://www.anthropic.com/engineering/multi-agent-research-system）
- [ ] 12. 上下文被截断/溢出 → plan 持久化到 memory；worker 产物写文件只回传引用；orchestrator 已评估改 blackboard（出处：https://www.anthropic.com/engineering/multi-agent-research-system；https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html）
