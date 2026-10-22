# Protein function description: available-source diagnostic

| Evaluation | Source year | Model | Cases | ROUGE-L |
|---|---|---|---:|---:|
| Independent UniProt reviewed-human curation snapshot | 2026 | Qwen3.8-27B | 9 | **0.0462** |

All nine descriptions were delivered with no transport/server errors, truncations, empty or unknown finals. Three of the twelve source-query candidates lacked reference function comments and were excluded before generation.

This is a small separate diagnostic, not completion of NatureLM’s unavailable original temporal evaluation. The result is not paper comparable. ROUGE measures lexical agreement; factual correctness and pretraining novelty were not assessed.

- [Complete questions and saved model responses](../results/runs/qwen38_27b_p27_available_human2026_diagnostic9_20261021/questions_and_responses.json)
- [Exact declared scores](../results/runs/qwen38_27b_p27_available_human2026_diagnostic9_20261021/scores.json)
- [Saved trajectory archive](../results/trajectory_archives/qwen38_27b_p27_available_human2026_diagnostic9_20261021.tar.gz)
- [Source and interpretation](../results/runs/qwen38_27b_p27_available_human2026_diagnostic9_20261021/README.md)
