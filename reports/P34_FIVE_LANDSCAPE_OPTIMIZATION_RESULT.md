# MutaPLM: iterative protein optimization with Qwen

This separately declared Qwen3.8-27B condition completed all five reviewed landscapes: 20 independent runs per landscape, 10 rounds per run and 20 proposals per round. All 1,000 Qwen replies and 20,000 candidate predictions plus 100 starting predictions are retained.

| Landscape | Final-round best surrogate fitness, mean of 20 runs | Population variance |
|---|---:|---:|
| AMIE | -2.329451 | 0.048565 |
| avGFP | 1.825646 | 0.255953 |
| E4B | -1.701369 | 0.007273 |
| LGK | -0.504736 | 0.133301 |
| UBE2I | 0.134839 | 0.019373 |

Scores use the released ESM1b landscape heads and native best-so-far aggregation. They are learned surrogate predictions, not experimentally validated function. Qwen selects 20 unique single-substitution actions from every supplied complete parent pool; all 20 candidates become the next parents, with no fitness feedback or fitness-based parent filtering. This proposal distribution differs from the paper’s native MutaPLM sampler.

The evaluated condition covers five of the paper’s six landscapes. The held sixth landscape was not dispatched, and this result does not complete the full native paper scope or the retained catalog.

[Complete evaluated starting questions](questions/P34.md) · [Exact score](../results/runs/qwen38_27b_p34_five_landscape_parent_pool_unique20_uniform16k_2026-10-21_v1/scores.json) · [Raw trajectories](../results/trajectory_archives/qwen38_27b_p34_five_landscape_parent_pool_unique20_uniform16k_2026-10-21_v1_trajectories.tar.gz) · [Source and protocol](../results/protocol_artifacts/qwen38_27b_p34_five_landscape_parent_pool_unique20_uniform16k_2026-10-21_v1_source.tar.gz) · [MutaPLM paper](https://arxiv.org/abs/2410.22949)
