# 场景决策表：6 种任务类型 × 推荐编排方案

来源：AdaptOrch（arXiv:2602.16873v1）、Anthropic multi-agent research system、Anthropic building effective agents、Beam.ai orchestration patterns、LLM Stack、developertoolkit。

> 交叉核对说明：本表由 `../../topologies/references/`（拓扑适用条件）与 `../../cost-selection/references/cost-selection.md`（成本倍数）交叉核对而成。两处来源一致处直接采用；不一致处在表内「成本提示」列与各小节以「⚠️ 口径分歧」并列注明。

## 决策总表

| 任务类型 | 推荐拓扑 | debate / judge | 并行度 | 成本提示 | 退化单代理条件 |
|---|---|---|---|---|---|
| 深度调研 | orchestrator-worker（lead 规划 → 并行 subagent 搜索 → lead 综合；DAG 视角多为 hybrid τX） | 无需多轮 debate；收尾可单轮 LLM-as-judge 按 rubric 打分（0.0–1.0 + pass/fail 一次调用最稳定） | 高：lead 一次 spawn 3–5 个 subagent，subagent 内部 3+ 工具并行；复杂研究可用 >10 个 | 约 15× chat token；按复杂度内嵌伸缩（1 agent / 2–4 / >10 档）；token 用量单独解释 BrowseComp 80% 方差 | 简单事实查证（1 agent + 3–10 次工具调用）；所有 agent 必须共享同一上下文或代理间依赖极多时 |
| 大型代码改造 | orchestrator-workers（中央 LLM 动态拆解、委派、综合；子任务无法预先知道是典型场景） | 不用 debate；优先确定性检查——测试执行结果就是 ground truth 反馈环 | 中：3–8 个并行 worker；超过 4 个 worker 时 orchestrator 易上下文溢出 | AdaptOrch 每 SWE-bench 实例约 41.8K token（vs MoA-3L 84.6K）；编排调用叠加在 worker 之上；$0.50 流程 × 100K 次执行可达 $50K/月 | 小型/单文件改动；可并行子任务比调研少，LLM 不擅长实时协调委派 |
| 写作/报告 | prompt chaining（outline → gate → 正文）+ evaluator-optimizer 循环 | 用 evaluator-optimizer 而非 debate；前提是「反馈能 demonstrably 改进输出」且评估标准清晰 | 低；可并行环节仅分段/分节写作，最终由主代理按 outline 组装 [推断] | 串行链以延迟换精度；3-agent pipeline 约 29K token vs 单代理 10K——不需专业化等于 3 倍价钱买同样结果 | 短文本、一次性文案；长报告结构可预先确定时单代理多轮迭代亦可 [推断] |
| 决策评估 | multi-agent debate 或 maker-checker（cheap/fast 做 maker、capable 做 checker）；DAG 视角路由 τS/τH | 需要：各方案必须看到彼此论据，需共享上下文的串行/层级结构，隔离并行（Static-Parallel）反而劣于单模型 | 低：≤3 个 agent（Microsoft 建议 group chat ≤3 以防不收敛） | 3 agent × 5 轮 = 15 次 LLM 调用/任务；maker-checker 可省 40–60% 成本；警惕 sycophancy cascading | 有唯一可验证答案（用 deterministic check）；决策维度单一 [推断] |
| 开放式探索 | autonomous agent 或 adaptive planning（manager 动态建计划、咨询专家、回退、重规划） | 不用 debate；关键在「每步从环境获得 ground truth」+ stopping conditions + human-in-the-loop 检查点 | 动态：manager 按需委派；诊断结果可使整个计划实时转向 | 成本不可提前预测；回退浪费死胡同分支算力；manager 可能对模糊需求无限循环建「完整计划」 | 时间敏感任务；步骤可预测、可硬编码路径的问题应退化为 workflow |
| 事实准确问答 | 单代理（augmented LLM：检索 + 工具）+ 轻量验证；routing workflow 按难度分流（简单→Haiku，难题→大模型） | 不做 debate；靠 claim 与 source 对齐检查（独立 CitationAgent 定位每条 claim 出处） | 1 | 多代理最不该上场的场景：single-concept recall 上 AdaptOrch 最多持平 Single Best；Princeton：64% 任务单代理已够 | 即默认形态；仅当答案需跨多个独立来源且超出单上下文窗口时才升级 research 编排 [推断] |

（出处：https://www.anthropic.com/engineering/multi-agent-research-system；https://www.anthropic.com/engineering/building-effective-agents；https://arxiv.org/html/2602.16873v1；https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production）

## 1. 深度调研

- 理由：调研是 breadth-first 开放问题，subagent 各自隔离上下文做「压缩」，为 lead 提炼关键 token；内部评测 lead(Opus) + 并行 subagent(Sonnet) 比单 Opus 高 90.2%（出处：https://www.anthropic.com/engineering/multi-agent-research-system）。
- 实操：lead 把计划写入外部 memory 防 200K 截断；引用定位交给独立 CitationAgent；subagent 产出写文件系统、只回传轻量引用，避免「传话游戏」损耗；委派指令须写明 objective、输出格式、任务边界，否则 subagent 会误解任务或重复劳动（出处：https://www.anthropic.com/engineering/multi-agent-research-system）。
- ⚠️ 口径分歧：90.2% 是 Anthropic 内部广度优先查询的评测结果；Princeton NLP（经 Beam 转引）称多代理仅 +2.1pp 且成本翻倍（出处：https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production）。reconciliation [推断]：分歧源于任务类型——广度优先、超出单上下文的任务多代理大胜；单上下文可解的常规任务多代理纯浪费。

## 2. 大型代码改造

- 理由：子任务无法预先知道是 orchestrator-workers 的典型场景；SWE-bench 上 ω≈3.4、γ≤0.4，62% 实例路由到 τX（hybrid）、24% τP、14% τH——「定位/理解/打补丁」中可并行的部分并行、耦合部分串行（出处：https://arxiv.org/html/2602.16873v1；https://www.anthropic.com/engineering/building-effective-agents）。
- 实操：用确定性检查优先（测试执行结果作为 ground truth），这是 coding agent 有效的原因；fan-out 合并后跑一次全量集成检查（出处：https://www.anthropic.com/engineering/building-effective-agents；https://developertoolkit.ai/en/workflows/automate/orchestration-patterns/）。
- ⚠️ 口径分歧：AdaptOrch 显示 SWE-bench 多代理 +9.8（52.6 vs 42.8）；但 Princeton 统计 64% 任务单代理不差（出处：https://arxiv.org/html/2602.16873v1；https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production）。裁定依据 [推断]：任务是否可分解、有无确定性验证反馈——有测试兜底且可拆分的改动多代理收益真实，反之纯加成本。

## 3. 写作/报告

- 理由：写作有清晰线性依赖（大纲 → 检查 → 成文 → 打磨），对应 prompt chaining + evaluator-optimizer；适用信号是「反馈能 demonstrably 改进输出」，评估器需有清晰评价标准（出处：https://www.anthropic.com/engineering/building-effective-agents）。
- 实操：阶段间交接「可校验的文件」而非散文（如 outline 对照 checklist），pipeline 早期错误会无回退地级联；长上下文写作用「分阶段摘要 + 外部记忆 + 干净上下文新 subagent 接力」维持连贯（出处：https://www.anthropic.com/engineering/building-effective-agents；https://www.anthropic.com/engineering/multi-agent-research-system）。
- 注意：不要用多代理 debate 替代 evaluator-optimizer——评估标准单一明确时，一个评估器循环比多视角辩论便宜且更可控 [推断]。

## 4. 决策评估

- 理由：decision 类是高耦合推理（γ≈0.55），AdaptOrch 上 41% 路由 τS、35% τH、仅 8% τP；Static-Parallel 在这类任务上反而低于单模型基线——各方案评估必须看到彼此论据，故需共享上下文的串行/层级结构（出处：https://arxiv.org/html/2602.16873v1）。
- 实操：限制 ≤3 agent 并设最大轮数上限；防 sycophancy cascading（多数派错误被强化成「自信的共识」）；显式冲突解决策略——意见相左时升级 arbiter，禁止「summarize the results」式含糊聚合；maker-checker 变体可用 cheap/fast maker + capable checker 省 40–60% 成本（出处：https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production；https://arxiv.org/html/2602.16873v1）。
- 注意：debate 的 ensembling 收益有统计学边界——同源模型采样共享系统性盲区 ρ，再多代理也突破不了 1−ρ 上限；须主动 decorrelate（不同基座模型、persona、工具、temperature）（出处：https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html）。

## 5. 开放式探索

- 理由：规划本身需要从协作中「发现」而非执行预定 DAG，对应 autonomous agent / adaptive planning（manager 动态建计划、咨询专家、回退、重规划）（出处：https://www.anthropic.com/engineering/building-effective-agents；https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production）。
- 实操：每步从环境获得 ground truth；设硬 stopping conditions（最大迭代数、handoff 次数上限）；设 human-in-the-loop 检查点；时间敏感任务不用该模式（为正确性牺牲速度）（出处：https://www.anthropic.com/engineering/building-effective-agents；https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production）。
- 失败模式：goal drift、infinite handoff loops、上下文每次转移损耗（全量传=贵且超窗，摘要传=有损）（出处：https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production）。

## 6. 事实准确问答

- 理由：原子单步任务（|V|=1）或 single-concept recall 类任务上 AdaptOrch 最多持平 Single Best，编排增益与可分解性成正比（出处：https://arxiv.org/html/2602.16873v1）。
- 实操：默认单代理 + 检索/工具；routing workflow 按难度分流（简单→小模型，难题→大模型）；事实正确性靠 claim 与 source 对齐检查（独立 CitationAgent 或 LLM judge 核对 factual accuracy）（出处：https://www.anthropic.com/engineering/building-effective-agents；https://www.anthropic.com/engineering/multi-agent-research-system）。
- 升级条件：仅当答案需跨多个独立来源且超出单上下文窗口时，升级为深度调研型编排 [推断]。

## 决策流程

从任务特征到拓扑选择的判断顺序（任一步不满足即停在当前层级）：

1. **先跑单代理基线**：单 prompt + retrieval/in-context examples 能解决就停；只有上下文溢出、需要并行/隔离、或错误代价高于多倍 token 时才升级（出处：https://www.anthropic.com/engineering/building-effective-agents；https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html）。
2. **问可分解性**：能否拆成 |V|≥2、边不稠密的 DAG？原子单问/单概念回忆 → 单代理 + routing（事实准确问答场景）（出处：https://arxiv.org/html/2602.16873v1）。
3. **问耦合与并行宽度（DAG 三特征路由）**：|E|=0 → Parallel；ω=1（纯链）→ Sequential；γ>0.6 且 |V|>5 → Hierarchical；宽且低耦合 → Parallel；其余 → Hybrid（出处：https://arxiv.org/html/2602.16873v1）。注意先判耦合再选并行——GPQA 上全并行比单模型还差（44.1 vs 46.2）。
4. **问验证信号形态**：有确定性 ground truth（测试、引用比对）→ orchestrator-workers / 反馈环，无需 debate；无 ground truth、靠多视角互纠 → debate + judge（≤3 agent、设轮数上限、防 sycophancy）（出处：https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production）。
5. **问子任务可预知性**：可预知且线性 → prompt chaining/pipeline（写作）；不可预知 → orchestrator-workers（代码改造）；连规划都不可预知 → adaptive planning / autonomous agent（开放式探索）（出处：https://www.anthropic.com/engineering/building-effective-agents）。
6. **问价值密度**：任务价值能否覆盖 15× chat token（相对同模型单代理基线为 3–7×，口径见 cost-selection.md）？不能 → 退回单调用 + 按难度 routing 到小模型（出处：https://www.anthropic.com/engineering/multi-agent-research-system；https://arxiv.org/html/2602.16873v1）。
7. **尽早评估**：~20 条真实查询的小样本评测即可发现大效应改动，不必等大规模 eval 才动手（出处：https://www.anthropic.com/engineering/multi-agent-research-system）。
