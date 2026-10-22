# V07: available full-deck SlideVQA condition

The fixed Qwen3.8-27B BF16 checkpoint attempted 2,215/2,215 frozen questions once. There were 2,208 valid answer/evidence outputs; every planned case remains in the metric denominator.

| Released native metric | F1 | Exact match |
| --- | ---: | ---: |
| Answer | 77.73% | 63.16% |
| Evidence pages | 94.42% | 87.67% |
| Joint answer and evidence | 74.63% | 57.56% |

Full generation completed: **True**. Invalid or missing finals: **7**. HTTP/transport/refusal counts: **0/0/0**. Truncations: **7**. No selective retries were performed.

Each dispatched request was constructed with all 20 supplied page images in source order, using 7,700 author-URL files and 300 separately identified processed1024 copies. The pinned model used one GPU, temperature 1.0, top-p 0.95, top-k 20, seed 42, thinking enabled and a 16,384-token output budget. A supported JSON grammar constrained the output shape; the final validator required unique, ascending evidence pages. Four neutral geometric 20-image requests had to pass actual token, first/last-page and output checks before benchmark dispatch.

The unchanged released SlideVQA QA, evidence and joint functions were applied after sealing the full prediction inventory. These metrics are an available local-model adaptation. [Ryze Table 3](https://arxiv.org/abs/2606.00902v1) reports 66.48% SlideVQA accuracy, but its exact cohort, aggregation, OCR/GLM configuration and metric mapping were not recoverable from the inspected release/history. The metric values above therefore do not establish a matched comparison or a reproduction of Table 3. Prior public pretraining exposure is unknown. Correct answers do not validate explanations or biological reasoning.

[SlideVQA source](https://github.com/nttmdlab-nlp/SlideVQA/tree/0d4168a935d60b0b218097205a02fb1133c8bead) · [Evaluation code](https://github.com/Some-random/bio-evaluation/blob/main/results/protocol_artifacts/v07_slidevqa_available_full_guard_v3_source.tar.gz) · [Raw aggregate scores](https://github.com/Some-random/bio-evaluation/blob/main/results/runs/v07_slidevqa_available_full_guard_v3/scores.json)

Licensed questions, page images, references and raw model text remain preserved privately under the existing source restrictions. The public artifact manifest records hashes of the full private prediction seal and the once-only scoring attempt.

The upstream evaluator source and license text are also excluded from this archive because of their distribution restrictions. The evaluated native source has SHA-256 `604be8d606ec46664e36810b43cdb497880043a39c57a687a819abc30660acbb`; consult the [official evaluator](https://github.com/nttmdlab-nlp/SlideVQA/blob/0d4168a935d60b0b218097205a02fb1133c8bead/evaluate.py) and [official terms](https://github.com/nttmdlab-nlp/SlideVQA/blob/0d4168a935d60b0b218097205a02fb1133c8bead/LICENSE) for permitted access.
