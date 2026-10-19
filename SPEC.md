# 多数据集 skill 路由评测（共享规范，所有窗口必须遵守）
目标：在真实公开评测集上比较 holon 树形字面路由与常见检索方法。只做工程评测。
目录：/workspace/work/bench。原始数据在 data/。holon 代码在 holon/（只读；路由逻辑在 holon/organizer/scripts/organizer_cli.py 的 route()/match_skill()，树由 holon/scripts/holon.py sync 生成）。

## 统一格式（每个数据集 <ds> 一个目录 ds/<ds>/）
- skills.jsonl：{"id","name","description","body"(全文，可截断到 8000 字符),"group":[一级,二级...]（树路径，来自数据集自带分类）}
- queries.jsonl：{"qid","query","gold":[skill id...],"setting"(没有就写 "all"),"lang"("en"/"ko"/...)}
- tree/：用 holon 规范建成的真实 holon 库（root/<group1>/<group2>/<skill>/SKILL.md），每个 SKILL.md 的 description 写成 holon 三段式 "Use when ...: covers w1, w2, ...; excludes ..."（excludes 可省）。cover words 必须自动、可复现地生成（规则写进 README：例如 name 按 -/_ 切词 + description 中的高 IDF 名词短语 top-k，k≤5），分组节点的 cover words 用组名切词。建好后跑 holon.py sync 和 validate（validate 的 body/trigger 要求若无法满足，记录哪些检查失败即可，不要伪造内容）。
- runs/<method>.jsonl：每条 {"qid","ranked":[skill id, 最多 20 个],"read_bytes":本次路由需要读取的字节数（树方法=路径上 SKILL.md 字节和；平铺方法=全部候选描述字节和）}
- 评分脚本 score.py（每个数据集共用一份，放 /workspace/work/bench/score.py，若已存在就复用不要重写）：输出每方法×每 setting 的 Hit@1、Recall@5、MRR、平均 read_bytes、n。多 gold 时 Hit@1=首位在 gold 中，Recall@5=gold 中被 top5 覆盖的比例。

## 确定性方法（每个数据集都要跑全部 query）
1. holon-tree：用 organizer_cli 的 route 逻辑（import 调用，不要逐条起子进程）在 tree/ 上路由；落点是叶子则 ranked=[该叶子]；落在中间组或根则 ranked=[]（记为未命中），ambiguous 记为未命中，并单独统计"停在组/停在根/歧义"比例。
2. flat-literal：同样的 cover words，但所有叶子挂在根下（单独建 flat/ 库）再 route。
3. bm25-desc：name+description 上 BM25（自己实现或 pip install rank_bm25），排序 top20。
4. bm25-body：name+description+body。
5. dense（若能装）：pip install fastembed，英文用 BAAI/bge-small-en-v1.5，若有非英文查询另跑 sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2；编码 name+description，余弦排序 top20。缓存向量到 ds/<ds>/emb/。
6. hybrid：bm25-desc 与 dense 的 RRF 融合（k=60）。
每个方法写 runs/<method>.jsonl，跑 score.py 生成 ds/<ds>/results.md。另写 ds/<ds>/README.md：数据来源 URL、规模、建树与 cover word 规则、已知偏差。
LLM 方法由主控另行运行，你不用做，但请额外导出 ds/<ds>/sample.jsonl：按 setting 分层随机抽样（seed=0）最多 300 条 query，供 LLM 方法使用。
注意：只在 /workspace/work/bench 内写文件；CPU 只有 2 核，向量编码注意批大小；单步命令超过 10 分钟就拆分。
