# srb — SkillRetBench

## 数据来源
- Hugging Face dataset **SkillRetBench**（SEFO 框架配套，Apache-2.0），本地快照在
  `data/srb/data/`（`skill_corpus.json`、`skillretbench_queries.json`、`baseline_results.json`）。
- 出处见 `data/srb/README.md`：501 个 Cursor agent SKILL.md 解析出的 skill 库 +
  程序化生成（rng_seed=42）的 1250 条查询，覆盖 5 个 setting
  （single_skill 400 / multi_skill_composition 200 / distractor 300 /
  outdated_redundant 150 / budget_constrained 200）。
- 引用：Han, Hyojung and ThakiCloud AI Research, "SEFO: Self-Evolving Federated
  Orchestration ...", 2026, https://github.com/hyojunguy/ai-model-event-stock-analytics

## 规模
- skills.jsonl：501 条（id / name / description / body≤8000 字符 / group）。
- queries.jsonl：1250 条（qid / query / gold / setting / lang）；lang 按是否含韩文字符
  判定：en=1099，ko=151。gold 全部能在 corpus 中解析到；budget_constrained 每 query
  25 个 gold，single_skill 1 个。

## 建树与分组
- 一级组 = skill 的 `category` 字段（= skill_id 前缀，与 corpus
  `statistics.skills_per_category` 一致）。只有 1 个成员的类别合并到 `misc`。
- 结果 46 个组（含 misc=57 个、standalone=46 个、kwp=95、agency=69、tab=21、
  trading=21、hf=19、anthropic=17 …），树结构 `tree/root/<group>/<skill>/SKILL.md`。
- `flat/` 为平铺对照库：同一批 SKILL.md 全部直接挂根下。
- 有一个非法 id `mission-control copy`（含空格），目录/name 规范化为
  `mission-control-copy`，映射存 `dir_map.json`，输出 ranked 时映射回原 id。

## cover words 规则（确定性，见 build.py，k≤5）
1. **name 切词**：skill_id 按 `-`/`_` 切分，保留 len≥3 且非停用词的 token，按原序取前 3。
2. **korean_triggers**：数据集自带的韩文触发词按原序最多取 2 个（韩文查询可达）。
3. **IDF 填充**：对每个 skill 的 `skill_name + description + trigger_phrases` 切词
   （`[a-z][a-z0-9]{2,}`、去停用词），在 501 篇文档上算 IDF，按 (-IDF, 字典序) 取
   未入选的 token 补足到 5 个。——`trigger_phrases` 因此是 cover words 的候选来源
   （其内容词进入该 skill 的 IDF 候选池），不整句照抄，因为整句作为 cover word
   只会精确匹配，且超长会触发 lint。
4. 组节点 covers = 组名按 `-`/`_` 切词。
description 统一写成三段式 `Use when <截断的描述>: covers w1, w2, ...`（≤200 字符）。
`metadata.holon-triggers` 写入数据集真实 trigger_phrases（最多 2 条）。

## holon 检查状态
- `holon.py sync`：tree 更新 47 个父节点路由表、flat 更新根；`validate`：两库全过
  （548 / 502 skills OK）。
- `organizer_cli.py lint`：547 个 [E] 全部是同一条——`triggers needs 2 正例 + 1 负例`。
  数据集的 anti_triggers 不含目标 skill 路径，无法构造合法的 `should go to <path>`
  负例，按 SPEC 要求不伪造，故保留该 lint 失败。另有 67 [W]（短 cover 词、重复 name
  等）与 65 [·] 提示。

## 方法（全部确定性，1250 条全跑）
| 方法 | 说明 |
|---|---|
| holon-tree | import organizer_cli 的 `route()` 在 `tree/` 上逐级下钻；落叶子 ranked=[该 skill]；停组/停根/歧义 ranked=[] |
| flat-literal | 同一 cover words，`flat/` 平铺库再 route |
| bm25-desc | rank_bm25 BM25Okapi，文档 = name+description |
| bm25-body | 文档 = name+description+body |
| dense | fastembed：英文查询 BAAI/bge-small-en-v1.5，韩文查询 paraphrase-multilingual-MiniLM-L12-v2；编码 name+description，余弦 top20；向量缓存在 emb/ |
| hybrid | bm25-desc 与 dense 的 RRF（k=60）融合 |

分词统一 `re.findall(r"[a-z0-9]+|[가-힣]+", text.lower())`；所有排序平局按 skill id
字典序打破，保证可复现。

## read_bytes 口径
- holon-tree / flat-literal：路由路径上（含根）SKILL.md 的字节和；歧义时只计根。
- bm25-desc / dense / hybrid：全部 501 个 skill 的 name+description UTF-8 字节和
  （292,789 B/查询；hybrid 与 bm25-desc 共享同一次描述读取）。
- bm25-body：name+description+body 字节和（3,373,412 B/查询）。

## 主要结果（详见 results.md）
- **holon-tree 几乎全部歧义**：停根 9 / 停组 21 / 歧义 1212 / 落叶子 8，
  总 Hit@1 = 0.0056。原因是父节点按规范继承全部后代 cover words，46 个组的
  继承词表高度重叠（如 "design"、"workflow"、"report" 同时属于多个组），根级
  必歧义。flat-literal 同样（歧义 1187 / 落叶 39，Hit@1 = 0.0160）。
- bm25-desc 总 Hit@1 = 0.5784 / MRR = 0.6904；dense 0.3808；hybrid 0.5368；
  bm25-body 反而低于 bm25-desc（0.4592），长 body 稀释了路由描述信号。
- 数据集自带 baseline（BM25 MRR≈0.57，dense 为 jaccard fallback）与本次
  bm25-desc 同量级，结果可信。

## 已知偏差
- 查询为模板化程序生成（含 trigger 改写），bm25-desc 因 description 与触发词同源
  而占优；这是数据集构造偏差。
- budget_constrained 每 query 25 个 gold，Recall@5 结构性偏低，不与其它 setting 比。
- 韩文查询 151 条，dense 对韩文用多语言模型、英文用 bge-small-en，两路排名不可互比
  （hybrid 内按 query 语言取对应 dense 排名）。
- lint 的 triggers 负例规则全体失败（见上），不影响 route 匹配本身。

## 文件
- `build.py`：导出 jsonl + 建树 + sync/validate；`run_lexical.py`：树路由 + BM25；
  `run_dense.py`：dense + hybrid；`covers.json`：每个 skill 的 cover words；
  `dir_map.json`：id→目录名；`emb/`：向量缓存；`sample.jsonl`：按 setting 分层、
  seed=0 抽 300 条供 LLM 方法使用。
