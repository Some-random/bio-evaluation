# PFArena: single-mutant generation

Qwen3.8-27B was evaluated on 34 independently reviewed mammalian domain-stability assays from the 123-assay PFArena T1 panel: 33 human assays and 1 bovine control.

| Model | NMS@40 | Recall@40 | Assays |
| --- | ---: | ---: | ---: |
| Qwen3.8-27B | 0.853716 | 0.036029 | 34/123 |

The native scorer compared each 40-item proposal with existing assay measurements. All 34 saved responses passed the input-valid, unique-ranking delivery checks. There were no transport/server errors, truncations or empty finals. Proposals absent from the measured candidate tables retain the native scoring penalty; they were not removed or selected using measurements.

The run used the pinned original BF16 checkpoint on one GPU, a uniform 16,384-token output limit, unchanged native prompts and scorer formulas, and a declared constrained JSON output condition. GPT models were not evaluated on this subset. This is a retrospective subset result, not experimental validation or completion of the full PFArena setting. The other 89 assays were outside this frozen reviewed condition.

- [Exact native scores](../results/runs/qwen38_27b_p19_reviewed34_unique40_eos16k_2026-10-21_v4/scores.json)
- [Retained raw requests and responses](../results/trajectory_archives/P19_reviewed34_qwen38_27b_v4_20261021.tar.gz)
- [Exact execution and scoring source](../results/protocol_artifacts/P19_reviewed34_qwen38_27b_v4_source_20261021.tar.gz)
