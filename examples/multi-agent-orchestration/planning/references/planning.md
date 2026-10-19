# Plan→Execute→Verify→Replan：规划与重规划操作指南

> 主框架 VMAO（出处：https://arxiv.org/html/2603.11445v2），辅以 Anthropic evaluator-optimizer 对照（出处：https://www.anthropic.com/engineering/building-effective-agents）。

## 1. 循环各阶段职责

| 阶段 | 职责 | VMAO 对应组件 | Anthropic 对照 |
| --- | --- | --- | --- |
| Plan | 分解查询为子问题，指派 agent 类型，声明依赖与优先级 | QueryPlanner | 人工/LLM 定义 prompt 链 |
| Execute | 识别就绪子问题，按优先级 top-k 并发执行 | DAGExecutor | workflow 并行执行 |
| Verify | 对每条结果按五维评分，产出结构化判定 | ResultVerifier | evaluator 反馈 |
| Replan | 重试低分子问题、补查缺口、合并结果（result preservation） | AdaptiveReplanner | optimizer 迭代精修 |

- Plan：LLM 识别不同信息需求，指派 agent 类型、建立依赖（一个子问题消费另一个的输出时）、设优先级（出处：https://arxiv.org/html/2603.11445v2）。
- Execute：迭代取依赖已满足的"就绪"子问题，按优先级取 top-k（默认 k=3）组成 batch 并行；单执行 timeout 默认 600s，附工具调用限制器防死循环（出处：https://arxiv.org/html/2603.11445v2）。
- Verify：输出 status（complete/partial/incomplete）、completeness_score（0–1）、missing_aspects、contradictions、recommendation（accept/retry/escalate）；complete 结果复用，避免冗余调用（出处：https://arxiv.org/html/2603.11445v2）。
- Replan：重试低分子问题（保留先前结果）、引入新查询补齐缺失方面、合并多次尝试的结果；旧结果落盘并与重试结果合并，渐进细化（出处：https://arxiv.org/html/2603.11445v2）。
- Synthesize：结果集大（>15K 字符或 >10 条）时按 agent 类型分组做 hierarchical synthesis，附 source attribution（出处：https://arxiv.org/html/2603.11445v2）。
- 对照：Anthropic evaluator-optimizer = "一个 LLM 生成、另一个在循环中评估反馈"，适合"有明确评估标准 + 迭代精修有可见价值"的场景；没有明确标准的任务不适用闭环迭代（出处：https://www.anthropic.com/engineering/building-effective-agents）。

## 2. DAG 拆解：单元字段与并行原则

**单元字段模板（七字段，缺一不可）**：`id`、`question`、`agent_type`、`dependencies`、`priority`（1–10）、`context_from_deps`、`verification_criteria`（出处：https://arxiv.org/html/2603.11445v2）。

```yaml
- id: T1
  question: "…具体可回答的问题…"
  agent_type: researcher | coder | verifier
  dependencies: []        # 仅填上游 id 列表
  priority: 5             # 1–10，同 wave 内按此排序
  context_from_deps: false # true 才注入上游产物
  verification_criteria:  # 规划期写死，见 §4
    - "…"
```

拆解三原则（出处：https://arxiv.org/html/2603.11445v2）：

1. **Maximize Parallelism**——独立子问题同时执行；执行按 wave 组织：无依赖者在第 1 wave 并发，依赖者进入后续 wave（DAG 保证 wave 划分总是可行）。
2. **Minimize Dependencies**——仅当结果被其他问题消费时才建立依赖。
3. **RAG First**——优先或并行检索内部知识库。

粒度经验：复杂查询 8–12 个子问题 / 5+ 种 agent 类型；简单查询 3–5 个 / 2–3 种（出处：https://arxiv.org/html/2603.11445v2）。[推断] 一个单元应小到"单次 LLM 调用 + 有限工具使用能完成"，且 verification_criteria 能在一两条判据内检查；粒度过大导致验证不可判定，过小则协调开销超过收益（3-agent pipeline 消耗 29K tokens vs 单 agent 10K，出处：https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production）。并行适用门槛：4 个以上相互独立任务才值得 fan-out，可削减 75% 墙钟时间（同上 Beam 出处）。

## 3. 依赖传递契约

- **接口约定**：依赖通过 `dependencies` 字段（上游 id 列表）声明，规划期显式写出"谁消费谁的产物"；执行器按 `deps ⊆ completed` 判定就绪（出处：https://arxiv.org/html/2603.11445v2）。
- **结果注入**：仅当 `context_from_deps: true` 时，把依赖项的结果 prepend 到该子问题的 prompt（自动 context propagation）（出处：https://arxiv.org/html/2603.11445v2）。
- **[推断] 落盘文件契约**：上游产物落盘为可寻址文件（blackboard 模式），附明确 schema（如 JSON），下游按"路径 + schema"读取——不用纯对话链传递。理由：Anthropic 的 ACI 观点（工具定义应含示例、边界、输入格式，投入与 HCI 同级，出处：https://www.anthropic.com/engineering/building-effective-agents）；且 sequential pipeline 的坏输出会无回退级联到所有下游（出处：https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production）。
- 推荐契约形态：`artifacts/<task_id>.json`，字段含 `task_id`、`producer`、`schema_version`、`content`、`sources[]`（URL/文件/日期）。

## 4. 验收标准写法：可检查的五维

每个子问题规划期写死 `verification_criteria`，验证期按五维检查（出处：https://arxiv.org/html/2603.11445v2）：

1. **Completeness**——问题各方面是否都覆盖；
2. **Evidence Quality**——多来源？交叉引用？
3. **Metadata**——来源 URL/文件名/日期是否标注；
4. **Specificity**——具体事实/数字 vs 模糊断言；
5. **Contradictions**——来源间冲突。

验证器输出结构化 JSON：`status`、`score`（0–1 连续分 + 离散档位）、`missing_aspects`、`confidence`、`recommendation`（出处：https://arxiv.org/html/2603.11445v2）。[推断] 可检查性三条判据：① 可由程序或检查清单逐项判定（yes/no 或可复算的数值）；② 失败时定位到具体子问题/方面（missing_aspects）；③ 阈值规划期量化写死（如 completeness ≥ 0.8）。确定性检查（测试、schema、lint）优先于 LLM 主观判断（Anthropic coding agent 以测试结果作为迭代反馈，出处：https://www.anthropic.com/engineering/building-effective-agents）；LLM judge 用与执行器不同且更强的模型（VMAO 用 Opus 评 Sonnet，降低自评偏差，出处：https://arxiv.org/html/2603.11445v2）。

## 5. 重规划触发条件与默认上限

**触发条件**（出处：https://arxiv.org/html/2603.11445v2；https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production）：

- 验证失败：verify 发现缺口，重试低分子问题（所有 incomplete 子问题 ID 必须全部进入 retry 列表）、引入新查询补缺口、遇矛盾加查不同来源；
- 新信息：诊断发现计划前提错误时整个计划实时转向；
- 预算耗尽：token budget 或 max iterations 任一满足即转入 synthesis。

**默认上限（VMAO 默认值，可调）**（出处：https://arxiv.org/html/2603.11445v2）：

| 参数 | 默认值 | 含义 |
| --- | --- | --- |
| batch 大小 k | 3 | 每 wave 并发执行的子问题数 |
| 单执行 timeout | 600s | 防止单个执行挂死 |
| token budget | 1M tokens | 硬停止，超限即 synthesis |
| max iterations | 3 | 最大重规划轮数 |
| ready threshold | 80% 子问题完成 | 满足即提前 synthesis |
| completeness 阈值 | >0.8 即 done | replan prompt 硬规则 |
| diminishing returns | 改进 <5% | 收益递减即停止 |

- 五个可配置停止条件：Ready for Synthesis（80%）、High Confidence（75% 置信 + 50% 覆盖）、Diminishing Returns（<5%）、Token Budget（1M）、Max Iterations（3）。
- [推断] 最大重规划次数必须硬编码默认 3；重规划不得扩大原始目标范围（防 goal drift）；adaptive planning 在目标模糊时会无限循环建"完整"计划（出处：https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production）。
- [推断] 多数 replanning 动作应是重试 incomplete 子问题而非引入全新子问题——执行方差比初始分解错误更常造成缺口（出处：https://arxiv.org/html/2603.11445v2）。Anthropic 建议自主 agent 在 checkpoint 或遇到 blocker 时暂停找人反馈（出处：https://www.anthropic.com/engineering/building-effective-agents）。
- 次数耗尽即带 gaps 收尾并标注，不得无限重试；>75% 的 VMAO 查询以资源型条件终止，默认阈值偏向 thoroughness。

## 6. plan.md 模板

```markdown
# Plan: <任务一句话>

## 目标与范围
- 原始查询：…
- 不做的事（防 goal drift）：…

## 子问题 DAG
| id | question | agent_type | deps | priority | context_from_deps | verification_criteria |
|----|----------|-----------|------|----------|-------------------|----------------------|
| T1 | … | researcher | [] | 5 | false | 五维判据 ≥0.8 |
| T2 | … | coder | [T1] | 4 | true | 测试全绿 + schema 校验 |

## wave 划分
- wave 1: T1, T3（无依赖）
- wave 2: T2（依赖 T1）

## 依赖契约
- artifacts/T1.json: {task_id, producer, schema_version, content, sources[]}

## 验收标准（五维 + 阈值）
- Completeness ≥ 0.8；Evidence: ≥2 来源；Metadata: URL/日期齐全；
  Specificity: 含具体数字；Contradictions: 无未解决冲突。

## 停止条件（默认值）
- max_iterations: 3；token_budget: 1M；timeout/单元: 600s；
  batch k: 3；ready threshold: 80%；diminishing returns: <5%。

## Replan 策略
- 优先 retry incomplete（保留旧结果合并）；其次新增子问题补缺口；
  迭代耗尽 → 带 gaps 收尾并列出 missing_aspects。
```
