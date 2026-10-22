# Qwen3.5-4B and 4B-Base on LAB-Bench: author general-thinking recipe

Native scoring completed at October 22, 2026 at 2:17 PM PDT. Both models received the same 197 reviewed LitQA2 questions and 82 SuppQA questions. Two previously held LitQA2 questions remain excluded.

| Evaluation, year and question | Qwen3.5-4B-Base | Qwen3.5-4B |
|---|---|---|
| LAB-Bench: LitQA2 (2024)<br>[Complete question and input](questions/B01.md) | **22.34%** accuracy (44/197)<br>Precision 22.92%; coverage 97.46% | **22.34%** accuracy (44/197)<br>Precision 23.28%; coverage 95.94% |
| LAB-Bench: SuppQA (2024)<br>[Complete question and input](questions/B03.md) | **9.76%** accuracy (8/82)<br>Precision 12.12%; coverage 80.49% | **19.51%** accuracy (16/82)<br>Precision 21.92%; coverage 89.02% |

These are closed-book text results using the complete released question fields and choices. SuppQA retains its released paper title and DOI. No additional papers, supplements, retrieval, model tools or images were supplied.

Both original BF16 checkpoints used thinking enabled, a 16,384-token output budget including reasoning and a 65,536-token context. The posttrained model card's general-thinking recipe was applied equally to both models: temperature 1, top-p 0.95, top-k 20 and presence penalty 1.5. This is not a separate author recommendation for Base, and the retained 16K output budget is below the card's 32K recommendation.

All 279 raw responses per model were saved and sealed before the one native scoring attempt. Invalid and truncated answers remain in the complete task denominators. Base had 0 truncated answers and 0 empty finals; posttrained 4B had 1 truncated answers and 3 empty finals. Transport errors, HTTP errors, runtime exceptions and recorded refusals were zero in both runs.

LitQA2 — Base: 110/197 parsed, 0 truncated, 0 empty finals; posttrained 4B: 133/197 parsed, 1 truncated, 3 empty finals.

SuppQA — Base: 42/82 parsed, 0 truncated, 0 empty finals; posttrained 4B: 48/82 parsed, 0 truncated, 0 empty finals.

This separately named full-cohort sampling condition preserves the [original 4B comparison](QWEN35_4B_LABBENCH_RESULTS_2026-10-22.md) and all earlier Qwen/GPT results. No failed cases were selectively retried or replaced, and these results do not reproduce the paper's full public/private evaluation. Outcome accuracy does not establish correctness of generated explanations; exposure to public benchmarks during pretraining is unknown.

The exact checkpoints are `Qwen/Qwen3.5-4B-Base@1001bb4d826a52d1f399e183466143f4da7b741b` and `Qwen/Qwen3.5-4B@851bf6e806efd8d0a36b00ddf55e13ccb7b8cd0a`. The new jobs were 247045 and 247047, under scientific plan `9bebb13605b9eddb34f97ea89961e8eff1d2a0a91df7974be315a6e1ab889192`.

[Machine-readable metrics and diagnostics](QWEN35_4B_LABBENCH_RECOMMENDED_SAMPLING_RESULTS_2026-10-22.json) · [Sealed paired scores](../results/runs/qwen35_4b_labbench_reviewed279_author_general_thinking16k_20261022_v2/scores.json) · [Read-only result audit](../results/runs/qwen35_4b_labbench_reviewed279_author_general_thinking16k_20261022_v2/result_audit.json) · [Frozen protocol source archive](../results/protocol_artifacts/qwen35_4b_labbench_reviewed279_author_general_thinking16k_20261022_v2.tar.gz)

[Base complete saved trajectories](../results/trajectory_archives/qwen35_4b_base_labbench_reviewed279_author_general_thinking_raw16k_20261022_v2.tar.gz) · [Archive manifest](../results/trajectory_archives/qwen35_4b_base_labbench_reviewed279_author_general_thinking_raw16k_20261022_v2.tar.manifest.json)

[Posttrained complete saved trajectories](../results/trajectory_archives/qwen35_4b_posttrained_labbench_reviewed279_author_general_thinking_raw16k_20261022_v2.tar.gz) · [Archive manifest](../results/trajectory_archives/qwen35_4b_posttrained_labbench_reviewed279_author_general_thinking_raw16k_20261022_v2.tar.manifest.json)
