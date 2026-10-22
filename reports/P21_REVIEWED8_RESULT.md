# PFArena: anchor-informed multi-mutant ranking

Qwen3.8-27B ranked all supplied candidates for 8 independently reviewed mammalian domain-stability assays from the 67-assay PFArena T3 panel: 6 human assays and 2 mouse assays.

| Model | Spearman | NDCG | NMS@5 | Recall@5 | Assays |
| --- | ---: | ---: | ---: | ---: | ---: |
| Qwen3.8-27B | 0.233237 | 0.874898 | 0.871693 | 0.375000 | 8/67 |

All 8 responses contained the complete supplied candidate permutation with no duplicate, missing or unknown IDs. There were no transport/server errors, truncations or empty finals. The unchanged native scorer compared these rankings with existing measurements; no candidate measurement was supplied to the solver. The native prompt's legitimate anchor measurement was retained.

The run used the pinned original BF16 checkpoint on one GPU, a uniform 16,384-token output limit, unchanged native prompts and scorer formulas, and a declared constrained JSON output condition. GPT models were not evaluated on this subset. This is a retrospective subset result, not experimental validation or completion of the full 67-assay setting. The other 59 assays were outside this frozen reviewed condition.

- [Exact native scores](../results/runs/qwen38_27b_p21_reviewed8_full_permutation16k_2026-10-21_v1/scores.json)
- [Retained raw requests and responses](../results/trajectory_archives/P21_reviewed8_qwen38_27b_v1_20261021.tar.gz)
- [Exact execution and scoring source](../results/protocol_artifacts/P21_reviewed8_qwen38_27b_v1_source_20261021.tar.gz)
