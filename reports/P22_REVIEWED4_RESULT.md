# PFArena: single-mutant-informed ranking

Qwen3.8-27B ranked every supplied combination candidate for four independently reviewed vertebrate domain-stability assays from PFArena T4: three human domains and one chicken domain.

| Model | Spearman | NDCG | NMS@5 | Recall@5 | Assays |
| --- | ---: | ---: | ---: | ---: | ---: |
| Qwen3.8-27B | 0.163516 | 0.879607 | 0.873182 | 0.150000 | 4/29 |

All four responses contained every supplied candidate exactly once, with no transport/server errors, truncations or empty finals. Complete native prompts, all 397 candidate IDs and all 5,300 legitimately supplied single-mutant context rows were retained. Protected combination measurements were isolated until the outputs were sealed, then scored once with the unchanged native formulas. GPT models were not evaluated on this subset.

This separately declared condition uses compact JSON to enforce input-valid complete permutations. It preserves every possible ranking order and the original 16,384-token budget, sampling and pinned BF16 checkpoint on one GPU. Format validity is imposed; the performance numbers above measure the resulting rankings against existing measurements.

The earlier whole-four condition is retained separately: all four responses were saved, one hit the output limit after excessive JSON whitespace, and its native score was undefined. The corrected condition reran the entire fixed four-assay cohort, with no selective replacement of the failed response. Both complete trajectories and both exact source versions are provided below.

This is a retrospective result for four reviewed domain-stability assays. It does not complete the native 29-assay panel, establish experimental validation or finish the catalog. The other 25 assays were outside this frozen condition.

- [Exact native scores](../results/runs/qwen38_27b_p22_reviewed4_full_permutation16k_2026-10-21_v2/scores.json)
- [Complete corrected-condition questions and responses](../results/trajectory_archives/P22_reviewed4_qwen38_27b_v2_20261021.tar.gz)
- [Preserved earlier four responses and undefined score](../results/trajectory_archives/P22_reviewed4_qwen38_27b_v1_failed_20261021.tar.gz)
- [Exact source for both conditions](../results/protocol_artifacts/P22_reviewed4_qwen38_27b_v2_source_20261021.tar.gz)
