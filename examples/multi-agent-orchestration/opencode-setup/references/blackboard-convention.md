# 黑板（blackboard）目录约定模板（D13）

> 目的：用文件系统做共享状态，实现代理间通信与断点续跑。
> 设计依据：本 skill 树内 references——`../../roles-permissions/references/roles-permissions.md`（文件所有权、key 命名空间、append-only）、
> `./opencode-mapping.md`（§6 黑板文件约定与断点续跑）、
> `../../planning/references/planning.md`（任务清单七字段与验收）。

## 1. 目录结构

```
blackboard/
├── plan.md              # 任务 DAG 清单，planner 写，其他角色只读
├── STATUS.md            # 运行状态清单，编排者/planner 维护，全员先读后写（按规则）
├── notes/               # worker 各自的产出 notes（一单元一文件）
│   └── <topic>.md       # 归对应 worker 所有，如 blackboard/notes/planning.md
├── redteam-r<N>.md      # redteam 第 N 轮攻击报告（只增不改）
└── judge-r<N>.md        # judge 第 N 轮裁决 verdict（只增不改）
```

文件所有权基线：

| 文件 | 所有者 | 其他角色 |
|---|---|---|
| `plan.md`、`STATUS.md` | 编排者/planner | 只读（judge/redteam/worker 均不得改） |
| `notes/<topic>.md` | 对应 worker | 他人 append-only 追加（按 §3 key 规则） |
| `redteam-r<N>.md` | redteam | 只读 |
| `judge-r<N>.md` | judge | 只读 |

## 2. 文件格式模板

### 2.1 plan.md（任务 DAG 清单）

每个子任务必须带七字段（缺一则不可调度、不可验收）：

```markdown
# Plan: <query 摘要>

## 单元清单
- id: D1
  question: <具体、可回答、范围清晰的问题>
  agent_type: worker-<role>
  dependencies: []          # 依赖单元 id 列表；仅当被消费才建依赖
  priority: 1-10
  context_from_deps: false  # true 才注入上游产物（VMAO 七字段之一）
  verification_criteria:    # 1-2 条可判定判据，阈值量化写死
    - completeness ≥ 0.8 且每条结论有出处
```

### 2.2 STATUS.md（运行状态清单）

启动时**第一个读取的文件**；每个单元一行，完成即勾选，支持断点续跑：

```markdown
# STATUS

- 当前阶段: <planning | executing | verifying | done>
- 轮次: r<N>
- 预算: token 用量 / 上限

## 单元状态
- [x] D1  <notes 路径或 N/A>  状态: complete | partial | incomplete
- [ ] D2  阻塞原因: <缺依赖/工具失败/…>
```

注：不记「负责人」列——judge/redteam 盲评要求剥离作者身份，STATUS.md 对全员可读，记负责人会泄露候选归属；归属信息由编排者在自己的调度记录中单独维护。

### 2.3 notes 出处格式

每条结论标注来源；推断性结论显式标注：

```markdown
## <key 命名空间: 小节标题>
- <结论>（出处：https://... 或 文件名:行号，日期 YYYY-MM-DD）
- <结论> [推断]（综合 出处1；出处2）
```

## 3. append-only 与 key 命名空间规则

- **append-only**：黑板内容永不覆盖、永不删除，只可追加。全量审计轨迹使事后 replay 能定位推理错误点。
- **key 命名空间**：每条 key 形如 `<agent_id>:<key_name>`（如 `worker-research:convergence-tmax`），防止写冲突；5 个 agent 即有 10 个潜在并发交互，命名空间是硬约束。
- **更新语义**：要「修改」某 key 时，追加一条带时间戳的新条目，新值以后出现的为准；旧条目保留。
- **fan-in 防「干净报告」假像**：整合 notes 时必须做 coverage accounting——列出未完成/未覆盖单元；「60% 文件无发现」不等于「无发现」。

## 4. 断点续跑协议

1. **启动时先读 STATUS.md**：任何 agent（含新起的会话）第一步读取 `blackboard/STATUS.md` 与 `plan.md`，确定自己负责单元的当前状态：
   - 未开始 → 正常执行；
   - partial/incomplete → 重读对应 `notes/`、`redteam-r*.md`、`judge-r*.md`，带着已有 critique 继续或重试同一单元；
   - complete → 跳过，不重复劳动。
2. **单元粒度 = 文件粒度**：每个子任务产物即一个 notes 文件；「单元完成 → 更新 STATUS.md → 继续下一单元」。
3. **完成即落盘即勾选**：单元产物写入 `notes/<topic>.md` 后立刻在 STATUS.md 勾选，防止中断后状态丢失。
4. **会话级续跑双保险**：文件黑板之外，可用 `opencode --continue` / `--session <ID>` / `--fork` 续会话；两者互为冗余，文件状态为准。
5. **到达最大轮数/预算即带 gaps 收尾**：不要在断点处无限重试；STATUS.md 中如实记录 incomplete 单元与缺口。
