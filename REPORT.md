# Literal Tree Routing vs. Retrieval and LLM Routing for Agent Skill Selection: An Empirical Study of holon on Three Public Benchmarks

*Technical report, 2026-10-19. Engineering evaluation only.*

## Abstract

Agent frameworks increasingly organize skills (SKILL.md files) into hierarchies and route a task to one skill by descending the tree. holon routes deterministically: at each level it descends only when exactly one child's *cover words* literally match the task. We build holon-conformant trees for three public skill/tool retrieval benchmarks (SkillRetBench, 501 skills; ToolRet-metatool, 102 tools; SkillRet, 6,006 skills) and compare holon against lexical (BM25), dense, hybrid, and LLM-based routing using three LLMs (Kimi K3, DeepSeek V4.1 Flash, MiniMax M3). Literal holon routing reaches 0.6% Hit@1 on SkillRetBench and 4.5% on ToolRet, while an LLM descending **the same trees** reaches 49.7–52.6% and 58.5–66.0%. A BM25 shortlist followed by LLM reranking reaches 78.3–81.0% on SkillRetBench at ~7 KB read per query. Failure analysis attributes 97% of holon's SkillRetBench failures to root-level ambiguity caused by generic cover words; replacing the uniqueness gate with scored selection, without any LLM, lifts Hit@1 from 0.6% to 46.4%. The tree structure is usable; the strict literal gate is not.

## 1. Introduction

A skill library is useful only if the agent picks the right skill. Two design families exist: (a) flat retrieval over all skill descriptions (BM25, embeddings, LLM reranking) and (b) hierarchical routing, where the agent reads a short routing table at each level. Hierarchical routing promises low read cost and human-auditable paths. holon is a concrete instance with a strict, deterministic rule.

**Research questions.**
- RQ1. How accurate is holon's literal tree routing on real skill libraries, relative to standard retrieval?
- RQ2. Is the tree itself the bottleneck, or the literal matching rule? (LLM descending the same tree.)
- RQ3. What accuracy/cost trade-off do LLM-based methods offer, and how much does the choice of LLM matter?
- RQ4. Why does literal routing fail, and which minimal changes fix it?

## 2. System under test: holon

- Source: holon repository, commit `9a8b29c` (read-only copy in `analysis/holon_src/`).
- Routing logic: `holon/organizer/scripts/organizer_cli.py`, functions `route()` / `match_skill()`. Trees are synced by `holon/scripts/holon.py sync` and checked by `validate`.
- Each node's SKILL.md description follows the three-part form `Use when <context>: covers w1, w2, ...; excludes ...`.
- Rule: at each level, a child is selected only if it is the **unique** child whose cover words occur in the query; zero or several matches stop the descent.

## 3. Benchmarks and skill libraries

All three are public datasets downloaded unchanged into `data/`; each was converted to a common format (`ds/<ds>/skills.jsonl`, `queries.jsonl`, `runs/*.jsonl`, see `SPEC.md`).

| Dataset | Skill library | #Skills | #Queries | LLM sample | Tree grouping |
|---|---|---:|---:|---:|---|
| SkillRetBench (`srb`) | 501 real Cursor-agent SKILL.md files (SEFO framework, Apache-2.0) | 501 | 1,250 (5 settings) | 300 | 46 groups from the skill's own `category` (singletons merged into `misc`) |
| ToolRet-metatool (`toolret`) | ToolRet "customized" tool library (mangopy/ToolRet-Tools) | 102 | 200 | 200 (all) | 10 KMeans clusters over BM25 vectors (no native taxonomy) |
| SkillRet (`skillret`) | `skills_test.jsonl`, two-level taxonomy major→sub | 6,006 | 4,392 | 300 | major → sub → skill |

SkillRetBench settings: single_skill 400, multi_skill_composition 200, distractor 300, outdated_redundant 150, budget_constrained 200.

**Cover-word generation (deterministic, k ≤ 5; `ds/*/build.py`).**
1. Split the skill id on `-`/`_`; keep tokens of length ≥ 3 that are not stopwords (first 3).
2. SRB only: up to 2 dataset-provided Korean triggers.
3. Fill to 5 with the highest-IDF tokens from name + description + trigger phrases (IDF over the library; ties broken lexicographically).
4. Group nodes: group name split on `-`/`_`.

`metadata.holon-triggers` holds up to 2 real trigger phrases from the dataset. No content was invented; validate checks that cannot be met without fabrication are recorded as failures in each `ds/*/README.md`.

## 4. Methods

| Method | Description |
|---|---|
| `holon-tree` | holon `route()` on the tree, unchanged |
| `flat-literal` | holon's literal matcher over a flat library (all leaves under root) |
| `bm25-desc` / `bm25-body` | BM25 over description / full body |
| `dense` | embedding similarity (cached, batched) |
| `hybrid` | fusion of BM25 and dense |
| `llm-tree` | LLM reads the routing table at each level of the **same holon tree** and picks a child, down to a leaf |
| `llm-rerank` | LLM reranks the top BM25-desc candidates |
| `llm-flat` | LLM sees all skill descriptions at once |

LLMs: Kimi `k3-256k`; DeepSeek `deepseek-v4.1-flash`; MiniMax `MiniMax-M3`. Additional channels were tested for agreement only (Section 6.4). All prompts carried task text only; no personal data.

**Metrics.** Hit@1, Recall@5, MRR, and `read_bytes` (bytes the router must read: sum of SKILL.md on the path for tree methods, all candidate descriptions for flat methods). Results are deduplicated by query id (last record kept).

**Note on populations.** Deterministic baselines were scored on all queries; LLM methods on fixed random samples (300 / 200 / 300). Comparisons across these two groups are indicative; comparisons within the LLM group are on identical queries.

## 5. Results

### 5.1 Hit@1

| Method | SRB | ToolRet | SkillRet |
|---|---:|---:|---:|
| holon-tree | 0.6% | 4.5% | — |
| flat-literal | 1.6% | 4.5% | — |
| bm25-desc | 57.8% | 30.5% | 51.5% |
| bm25-body | 45.9% | 31.0% | — |
| dense | 38.1% | 54.0% | — |
| hybrid | 53.7% | 47.0% | — |
| llm-tree, Kimi | 51.7% | 66.0% | — |
| llm-tree, DeepSeek | 49.7% | 63.5% | 55.3% |
| llm-tree, MiniMax | 52.6% (n=173) | 58.5% | — |
| llm-rerank, Kimi | 81.0% | 63.5% | — |
| llm-rerank, DeepSeek | 78.3% | 64.0% | 70.4% (n=186)¹ |
| llm-rerank, MiniMax | 80.0% | 64.0% | — |
| llm-flat, Kimi | 87.0% (n=131) | 79.0% | — |

¹ Only 186 of the 300 SkillRet sample queries have a BM25-desc candidate list, so rerank covers 186. On the same 186 queries, DeepSeek llm-tree scores 61.3%.

### 5.2 Cost (mean read_bytes per query, SRB)

| Method | read_bytes |
|---|---:|
| holon-tree | 24.6 KB |
| llm-rerank | 7.2 KB |
| llm-tree | 35.0 KB |
| llm-flat | 180 KB |
| bm25-desc | 293 KB |
| bm25-body | 3.4 MB |

### 5.3 Answers to RQ1–RQ3

- **RQ1.** Literal holon routing is near zero (0.6% / 4.5%), far below BM25 (57.8% / 30.5%).
- **RQ2.** The same tree routed by an LLM reaches 49.7–66.0%: the tree is not the bottleneck; the literal gate is.
- **RQ3.** BM25 shortlist + LLM rerank is the best trade-off: 78–81% on SRB at 7 KB, ~5× less reading than llm-tree. llm-flat is most accurate but reads 25× more. The three LLMs are within ~3 points of each other on rerank; the method matters far more than the model.

## 6. Failure analysis of holon (RQ4)

Computed locally over all 1,250 SRB queries (`analysis/route_analysis.py`, `analysis/summary_all.json`).

### 6.1 Where descent stops

| Stop class | Share |
|---|---:|
| ambiguous_root (≥ 2 top-level groups match) | 97.0% |
| stop_group | 1.2% |
| no_match_root | 0.7% |
| ambiguous_group | 0.5% |
| reached a leaf | 0.6% |

A query literally matches on average **7.2** top-level groups (max 19; 1,212 of 1,250 match ≥ 2).

### 6.2 Cause: generic cover words

The words most responsible for root ambiguity occur in the covers of 40+ of the 46 groups: `skills` (580 queries, 46 groups), `candidate` (202, 44), `docs` (157, 41), `automation` (125, 46), `calendar` (82, 45). Automatic IDF-based cover generation does not prevent this, because IDF is computed per document, not per sibling set.

### 6.3 Oracle decomposition

| Cause if ambiguity were resolved perfectly | Share |
|---|---:|
| gold reachable; failure is ambiguity only | 74.2% |
| gold's group lacks a matching cover word | 16.8% |
| gold's leaf lacks a matching cover word | 9.0% |

### 6.4 Ablation without any LLM (`analysis/improve_experiment.py`)

| Variant | SRB Hit@1 |
|---|---:|
| holon strict, exact tokens | 0.56% |
| strict + stemming | 0.24% |
| strict + stemming + synonyms | 0.24% |
| scored descent (pick child with most matched cover words), exact | 46.4% |
| scored descent, stemming + synonyms | 39.4% |
| flat scoring over all leaves | 51.4% |

Making matching *looser* (stemming, synonyms) under the strict gate makes results *worse*, because it creates more ambiguity. Replacing the gate with scoring is what matters.

### 6.5 Channel agreement (validity check)

Because several API gateways were used, each new DeepSeek V4.1 channel was checked on the same 40 random SRB queries (rerank) before its results were merged:

| Channel | Hit@1 | Top-1 agreement with reference |
|---|---:|---:|
| reference run | 35/40 | — |
| gateway A, run 1 / run 2 | 33/40, 35/40 | 34/40, 39/40 (run-to-run: 35/40) |
| gateway B | 34/40 | 39/40 |

On 63 SkillRet llm-tree queries, gateway B scored 35 vs. 41 for the reference (discordant 3 vs. 9, exact McNemar p = 0.146); tree routing involves several sequential calls and shows higher run-to-run variance. Weaker models were reported separately and never merged (e.g. DeepSeek V4 Flash 0731: 37.7% SkillRet llm-tree vs. 63.4% for V4.1 on its subset).

## 7. Recommendations for holon

1. **Score instead of gate.** At each level rank children by IDF-weighted matched cover words; never stop on ties.
2. **Beam descent.** Keep the top 2–3 branches; resolve at the leaves.
3. **Sibling-distinct covers.** Compute cover-word distinctiveness over the sibling set; every child needs at least one word no sibling has; generic words (`skills`, `docs`, `automation`) are excluded or down-weighted.
4. **Close coverage gaps.** ~26% of golds are unreachable by words; use `holon-triggers` and `_feedback.md` misses during absorb to add cover words.
5. **Tree to narrow, model to decide.** Beam candidates + LLM rerank should approach the 78–81% rerank result at tree-level read cost.
6. **Write routing tables for models, not string matchers.** The same tables read by an LLM already give 50–66%.

## 8. Threats to validity

- Deterministic baselines and LLM methods were scored on different query populations (all vs. sample).
- Incomplete runs: MiniMax SRB llm-tree 173/300; Kimi SRB llm-flat 131/300; SkillRet rerank limited to 186 queries.
- Trees were generated automatically by a fixed rule; hand-curated covers could do better. ToolRet has no native taxonomy (KMeans groups are noisy).
- LLM results come from third-party gateways; agreement checks (6.5) reduce but do not remove the risk of differing model builds. Single runs; no confidence intervals beyond 6.5.
- The failure analysis and ablation cover SRB in depth; ToolRet and SkillRet analyses are partial.

## 9. Reproduction

```
cd bench
python3 ds/<ds>/build.py            # build skills/queries/tree/flat
python3 ds/<ds>/run_lexical.py      # bm25, flat-literal, holon-tree
python3 ds/<ds>/run_dense.py        # dense, hybrid
CHAT_URL=... MODEL=... OUT_SUFFIX=-<tag> python3 llm_runner.py <ds> llm-tree|llm-rerank|llm-flat <concurrency>
python3 score.py ds/<ds>            # writes ds/<ds>/results.md
python3 analysis/route_analysis.py  # failure classes
python3 analysis/improve_experiment.py
```

API keys are never stored in the repository; set them in the environment. Note `score.py` counts duplicate rows; the tables above deduplicate by qid.

## Appendix: example skill package

`examples/multi-agent-orchestration/` is a hand-written holon-style package (9 sub-skills). Updated after this study: added routing lessons to the root SKILL.md (choose by meaning, keep two candidates when both fit, sibling-distinct covers) and removed a cover-word overlap (`成本失控` in failure-modes vs. `成本` in cost-selection → `开销失控`).
