# 多智能体讨论收敛参考：debate、投票/共识、匿名化与停止条件

> 深入参考文档（progressive disclosure 的 references 层）。配套 skill 主文档只给摘要，此处给出完整机制、数值建议与出处。面向需要为 debate/consensus 流程定参数的工程师。

出处标注：[S]=MAD 系统综述 <https://arxiv.org/html/2607.26212v1>；[O]=orchestration 消融实验 <https://arxiv.org/abs/2509.23537>；[A]=Anthropic 工程实践 <https://www.anthropic.com/engineering/building-effective-agents>；[推断]=基于上述出处的综合推断，非原文结论。

## 1. Debate 机制的基本形态

MAD（Multi-Agent Debate）的底线定义：≥2 个 AI agent、可多轮提出反对论点、围绕同一任务讨论。单 agent 自反思、单向反馈、无讨论的信息传递都不算 debate [S]。

三种交互协议及文献中的使用占比：

| 协议 | 占比 | 说明 |
|---|---|---|
| simultaneous | 47.0% | 同轮并行生成各自答案，再广播给所有人 |
| sequential | 42.4% | 固定轮次内遍历 agent 集，每步一个事件，直到达成共识或触达轮数上限（iteration cap） |
| hybrid | 8.0% | 独立探索与串行精修交替 |

[S]

领域默认配置是**静态全连接拓扑 + verbatim 原文交换 + 短期记忆**，但这是"约定俗成"，并非系统比较得出的最优 [S]。不要把它当作必须遵循的规范。

**制造分歧的手段**，按成熟度排序 [S]：

1. **stance 分配**（最成熟）：成对对抗角色，如 angel/devil、prosecution/defence、faithful/unfaithful。
2. **persona 异质性**：heterogeneous persona（53.6% 采用）提升视角多样性、抑制 conformity；homogeneous persona（44.4%）实现简单但易过早收敛与共享错误。注意 heterogeneous 的结果对 persona 指定方式更敏感，需要仔细写 persona [S]。
3. **异质 base model**：混合不同模型可提升鲁棒性（综述谨慎表述为 "may increase robustness"）[S]；echo-chamber 的抑制更直接来自 diversity-pruning / quality-pruning（综述引 Estornell & Liu 2024）[S]。

## 2. 投票/共识规则

agreement 分两层：**Authority**（谁定夺）与 **Resolution**（怎么聚合）[S]。

Authority 占比：Collective（多数决）/ Judge-based 39.1% / Hybrid 4.0% [S]。

Resolution 机制占比 [S]：

| 机制 | 占比 | 适用 |
|---|---|---|
| Majority vote | 46.4% | 绝对主导；有客观 ground truth 的任务（数学/逻辑） |
| Consensus（全员一致） | 20.6% | 保真度高，但轮次与 token 成本更高 |
| Argument evaluation | 13.4% | judge 定性综合；主观/开放任务（文本评估、诊断） |
| Scoring | 10.3% | |
| Weighted vote | 5.2% | 权重可来自 agent 置信度、跨轮一致性（consistency across rounds）[S] |
| Average | 4.1% | |

**选择规则**：客观题走 Collective + majority vote；主观题走 Judge-based + argument evaluation [S]。

**Hybrid 机制**（推荐作为默认）：先集体投票；出现 tie 或限定轮数内未达共识时，才引入 judge 裁决 [S]。

**加权投票的权重来源**：agent 置信度、跨轮一致性 [S]。

**效率-保真权衡**：majority vote 计算效率最高；consensus 与迭代论证评估保真度高但贵。预算受限时优先 majority vote + Hybrid tie-breaker [S]。

**阈值建议** [推断，综合 S/O]：

- 4–5 个 agent 时，简单多数（>50%，即 3/5 或 3/4）即可收敛，无需 supermajority。
- judge tie-breaker 全程最多调用 1 次，避免 judge 事实上独裁 [推断]。

## 3. 匿名化做法

匿名化的动机数据（GPT-5 多 agent 设置）[O]：

- Identified Voting 相比匿名：self-voting 率 81.0%→88.4%；Consensus Tie Rate 14.1%→23.2%；46 个 tie 全部涉及至少 1 个自投票 agent [O]。
- Visible Tally（票数可见）放大 herding：First-voted Selected Rate 54.1%→67.8%；日志中 agent 明确以"已获多数票"为投票理由 [O]。

**默认推荐配置：Anonymous Voting + Hidden Tally**——答案只挂匿名 ID（agent1、agent2），投票前任何 agent 不可见他人票数 [O]。

**顺序发言的 anchoring 效应**：先发言者的内容锚定后续推理、放大 conformity。对策：随机化发言顺序（randomized turn-taking），或由 coordinator 动态选择下一个发言者 [S]。注意：顺序偏差在文献中很少被控制或报告，是被低估的 conformity 来源 [S]。

**减少 echo-chamber 的补充手段**：diversity-pruning / quality-pruning 选择性过滤响应；异质 base model [S]。

## 4. Herding / 过早共识的识别与对策

**量化证据** [O]：

- GPQA-Diamond 上 95.5% 的题至少一个 agent 答对，但 orchestration 整体只有 87.4%；错误案例中 64% 仍有 ≥1 个 agent 正确，其中 31% 是 ≥2 个正确 agent 被错误多数带走 [O]。
- 错误共识的另一成因：系统按"分析质量/论证详细程度"而非正确性选 winner——详细但错误的论证压倒正确答案 [O]。
- sycophancy：LLM-as-a-judge 式评估中 agent 互相讨好、强化既有偏差；需多维打分与多样性推理数据监控，CONSENSAGENT 即专门做 sycophancy mitigation [S]。

**识别信号**（出现即应触发对策）[推断，综合 O]：

1. 收敛速度异常快（第 1 轮即多数票一致）。
2. agent 的投票理由引用"已获多数票"而非答案本身的论据 [O]。
3. winner 的论证明显更长/更详细，但与 ground truth 或确定性检查冲突 [O]。
4. 全体成员观点高度同质（homogeneous persona + 同模型时尤其警惕）[S]。

**对策清单**：

| 对策 | 机制 | 出处 |
|---|---|---|
| 匿名投票 + 隐藏票数 | 切断 self-voting 与 bandwagon | [O] |
| 随机发言顺序 / coordinator 选发言者 | 消除 anchoring | [S] |
| 异质 persona / 异质模型 | 保持观点多样性 | [S] |
| stance 强制分歧（devil's advocate） | 保证反对论点始终存在 | [S] |
| diversity-pruning / quality-pruning | 过滤同质化响应 | [S] |
| dynamic restart | 投票期间若有 agent 提交新答案，所有其他 agent 标记 restart，此前票数作废，用最新答案集重新投票 | [O] |

dynamic restart 专门用于防 premature consensus：新答案介入即作废旧票、强制全体重新评估，避免"先投票定终身" [O]。

## 5. 最大轮数与停止条件

- consensus 机制**必须**有最大轮数上限以防死循环 [S]。
- 轮数翻倍（如 2→4、13→25）需重新评估性能与 token 效率，收益递减 [S]。因此实践上应低起点 + cap，而非大轮数起步。
- 工程实践：autonomous agent 应显式设置 stopping conditions（如最大迭代次数）以保持控制 [A]。
- evaluator-optimizer 循环有效的前提：有明确评估标准 + 迭代精修有可度量的价值；否则循环不会收敛到有意义的改进 [A]。
- 每步从环境获取 ground truth（工具返回、代码执行结果）评估进度，是收敛判定最可靠的依据——优于纯文本一致性 [A]。

**数值建议** [推断，综合 S/O/A]：

- 通用 debate：tmax = 3–5 轮。
- consensus 型（全员一致）：tmax ≤ 8–10 轮，并配合 dynamic restart [O]。
- 单轮 majority vote 流程：1–2 轮即可。
- judge tie-breaker 全程最多 1 次 [推断]。

**停止条件（满足任一即停）** [推断，综合 S/A]：

1. 某答案获多数票，且连续 2 轮无新答案、无改票。
2. 达到 tmax。
3. 达到 token/时间预算。
4. 确定性检查通过（测试全绿、编译成功、工具返回 ground truth 确认）。

## 6. 收敛协议模板（可直接套用）

| 参数 | 默认值 | 说明 / 出处 |
|---|---|---|
| 协议形态 | sequential 或 simultaneous | [S] 占比最高两者；顺序发言时随机化轮内顺序 [S] |
| 拓扑 | 全连接、verbatim 交换 | 领域默认 [S]，可按成本裁剪 |
| persona | heterogeneous + 成对 stance | 抑制 conformity [S] |
| 匿名化 | Anonymous Voting + Hidden Tally | 默认必开 [O] |
| 投票规则 | majority vote（>50%） | 客观题默认 [S] |
| tie / 未达共识 | judge 裁决（Hybrid） | judge 全程最多调用 1 次 [S][推断] |
| tmax | 3–5（通用）/ ≤10（consensus 型） | [推断，S] |
| dynamic restart | 开 | 有新答案即作废重投 [O] |
| 收敛阈值 | 多数票 + 连续 2 轮稳定 | [推断] |
| 停止条件 | 上述 4 条满足任一 | [推断，A] |
| 收敛判定依据 | 优先 ground truth / 确定性检查 | [A] |
| 监控项 | self-voting 率、tie rate、收敛轮数、token 消耗 | [O] |

套用步骤：① 按任务类型（客观/主观）定 Authority 与 Resolution；② 打开匿名化与随机发言顺序；③ 设 tmax 与 4 条停止条件；④ 跑小规模基线，记录收敛轮数与 tie rate，再决定是否加轮数或引入 judge [推断，综合 S/O/A]。

## 参考链接

- [S] MAD 综述：<https://arxiv.org/html/2607.26212v1>
- [O] orchestration 消融（匿名化/herding/dynamic restart）：<https://arxiv.org/abs/2509.23537>
- [A] Anthropic, Building Effective Agents：<https://www.anthropic.com/engineering/building-effective-agents>
