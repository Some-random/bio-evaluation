# PFArena T3: eleven additional domain-stability assays

| Model | Spearman | NDCG | NMS@5 | Recall@5 | Assays |
|---|---:|---:|---:|---:|---:|
| Qwen3.8-27B | 0.293247 | 0.850503 | 0.790275 | 0.363636 | 11/67 |

The task asked the model to rank all supplied candidates for eleven independently reviewed ordinary isolated-domain stability assays. Three artificial delivery checks passed before benchmark dispatch. This separately attempted cohort is disjoint from the earlier eight- and five-assay results; no pooled metric is reported. The remaining 43 assays are outside this condition.

The declared single-shot baseline retained native messages, legitimate measured anchors, the full candidate permutation and the four native metric formulas. It used pinned original BF16 Qwen3.8-27B, nonthinking, 16,384 output tokens and a mandatory full-permutation JSON constraint preserving every ranking order. Candidate outcome measurements remained scorer-only. This is retrospective agreement with existing measurements, not experimental validation or a matched tool-using paper result. Public pretraining exposure is unknown. GPT models were not evaluated for this cohort.

Native scoring status: `completed_native_scored_reviewed_subset`. Transport/response errors: 0; empty finals: 0; truncations: 0. All eleven cases remain in scope; undefined metrics are not replaced.

- [Exact saved native score](scores.json)
- [Sealed requests, responses and metadata](../../trajectory_archives/qwen38_27b_p21_domains11_full_permutation16k_2026-10-22_v1.tar.gz)
- [Execution code and pinned upstream source references](../../protocol_artifacts/qwen38_27b_p21_domains11_full_permutation16k_2026-10-22_v1_source.tar.gz)
