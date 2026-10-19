用中文分析 holon 字面路由树在公开检索评测中为什么几乎全错。只在本地读文件、跑 python 脚本，不要调用任何 LLM API，不要读写任何 key，不要碰正在运行的 llm_runner.py 或 ds/*/runs/llm-* 文件。

目录 /workspace/work/bench：SPEC.md、TASK_*.md 是规范。holon 源码在 /workspace/work/bench/analysis/holon_src，按 cover-word 字面匹配逐层下钻。数据集 ds/srb（501 skill，sample.jsonl 300 条，queries.jsonl 含 gold）、ds/toolret（200 条）、ds/skillret（6006 skill）。runs/holon-tree.jsonl 是 holon 结果（srb Hit@1 1.0%，toolret 4.5%），runs/llm-tree.jsonl 是 Kimi 按同一棵树逐层选的结果（srb 51.7%，toolret 66%），还有 bm25-desc、dense、hybrid、flat-literal。tree_map.json/tree_index.json 是 skill 到树路径映射。

步骤：
1. 读 holon 路由代码，说明每层如何匹配、何时停止、歧义怎么处理。
2. srb、toolret（有就加 skillret）的 holon-tree 结果逐条分类失败：停在根/组节点、多分支歧义、走错分支、到叶子选错、无匹配；给数量和比例，每类 3 个真实例子。
3. 与 llm-tree 对照：LLM 走对而 holon 走错的查询，差距来自字面匹配（同义、改写）还是树结构（分组、cover word 稀疏）。用确定性脚本做诊断：查询词与 gold 路径 cover word 的词面重叠率；加词干化/小写/简单同义扩展后 holon 命中率能升多少。
4. 结论：主因排序；哪些是评测设定造成（taxonomy 不适配、缺 anti-trigger），哪些是 holon 设计局限；3-5 条可验证改进建议及预期影响。
报告写 /workspace/work/bench/holon_failure_analysis.md，脚本放 /workspace/work/bench/analysis/。卡住超过两次就写下已有结果并结束。
