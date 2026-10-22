# Qwen3.5-4B and 4B-Base on LAB-Bench

Both runs completed and native scoring finished on October 22, 2026 at 09:31 PDT. Each model received the same 197 reviewed LitQA2 questions and 82 SuppQA questions, using complete released text prompts and choices. The two previously held LitQA2 questions remain excluded.

| Evaluation | Qwen3.5-4B-Base | Qwen3.5-4B |
|---|---:|---:|
| LAB-Bench: LitQA2 (2024) | **22.34%** accuracy (44/197) | **14.72%** accuracy (29/197) |
| LAB-Bench: SuppQA (2024) | **12.20%** accuracy (10/82) | **17.07%** accuracy (14/82) |

[Complete LitQA2 question and input](questions/B01.md) · [Complete SuppQA question and input](questions/B03.md) · [Machine-readable metrics and diagnostics](QWEN35_4B_LABBENCH_RESULTS_2026-10-22.json)

These are closed-book text results: no papers, supplements, retrieval or model tools were supplied beyond the native question fields; SuppQA retains its released paper title and DOI. Both models used original BF16 checkpoints, thinking enabled, a 16,384-token output budget including reasoning, 65,536-token context, identical sampling and native deterministic answer extraction. This is a new matched condition; it does not replace earlier Qwen3.8 or GPT results or reproduce the paper's full public/private evaluation.

All 279 raw responses per model were saved and sealed before scoring. Invalid and truncated answers remain incorrect in the full task denominators. Qwen3.5-4B-Base hit the output limit on 10/279 cases and had 10 empty final answers; Qwen3.5-4B hit it on 121/279 and had 124 empty final answers, including three stop-finished responses with no valid final channel. Transport errors, HTTP errors, runtime exceptions and recorded refusals were zero in both runs. The high output-limit and answer-format failure counts qualify comparisons of underlying model ability.

Per task, Base had 9 truncated/empty LitQA2 answers and 1 truncated/empty SuppQA answer. Posttrained 4B had 94 truncated and 97 empty LitQA2 answers, and 27 truncated/empty SuppQA answers. Native parsing accepted 115/197 and 44/82 Base answers, versus 86/197 and 42/82 posttrained answers. There were no retries, model-based extraction repairs or excluded failed answers.

The frozen model revisions are `Qwen/Qwen3.5-4B-Base@1001bb4d826a52d1f399e183466143f4da7b741b` and `Qwen/Qwen3.5-4B@851bf6e806efd8d0a36b00ddf55e13ccb7b8cd0a`. Original Slurm jobs 246445 and 246714 completed with exit 0; no operational successor was used. Outcome accuracy does not assess the biological correctness of generated explanations, and exposure to public benchmarks during pretraining is unknown.

[Sealed paired scores](../results/runs/qwen35_4b_labbench_reviewed279_thinking16k_20261022/scores.json) · [Read-only result audit](../results/runs/qwen35_4b_labbench_reviewed279_thinking16k_20261022/result_audit.json) · [Frozen protocol source archive](../results/protocol_artifacts/qwen35_4b_labbench_reviewed279_thinking16k_20261022.tar.gz)

[Base complete saved trajectories](../results/trajectory_archives/qwen35_4b_base_labbench_reviewed279_thinking_raw16k_20261022_v1.tar.gz) · [Archive manifest](../results/trajectory_archives/qwen35_4b_base_labbench_reviewed279_thinking_raw16k_20261022_v1.tar.manifest.json)

[Posttrained complete saved trajectories](../results/trajectory_archives/qwen35_4b_posttrained_labbench_reviewed279_thinking_raw16k_20261022_v1.tar.gz) · [Archive manifest](../results/trajectory_archives/qwen35_4b_posttrained_labbench_reviewed279_thinking_raw16k_20261022_v1.tar.manifest.json)
