# BioReason-Pro: 64 additional human proteins

Qwen3.8-27B completed **64/64 functional explanations and 64/64 local judgments**. Its declared local axis-macro score is **6.5199/10**.

These are the first 64 previously unattempted human entries in the released source order. They form a separate fixed extension. The earlier 12-case result remains unchanged and is not pooled into this score. Together the two conditions cover 76 source entries; the release contains 8,630.

| Assessment | Qwen local-judge score / 10 | Evaluated cases |
|---|---:|---:|
| Molecular Function | 5.9683 | 63 |
| Biological Process | 5.3438 | 64 |
| Cellular Component | 7.1935 | 62 |
| Specificity | 8.2656 | 64 |
| Reliability | 5.8281 | 64 |

Only independently reviewed absence of all reference evidence permits an axis to be unevaluable: one molecular-function axis and two cellular-component axes meet that rule. Missing GO labels alone do not establish absence. Source annotation disagreements and three domain-coordinate inconsistencies were preserved.

The solver received complete original sequences and released domain, interaction and fallible predictor context. Reference names, curated function/GO and localization were excluded from solver requests. Every solver outcome was sealed before reference dossiers were parsed into judge prompts; earlier integrity hashing did not expose those references in solver requests.

Both stages used the pinned Qwen3.8-27B BF16 model with nonthinking 16,384-token outputs. This replaces the paper's GPT-5.1 judge and uses the same checkpoint as solver and judge. The score is an uncalibrated local explanation assessment, **not the paper's benchmark score or biological validation of proposed mechanisms**.

Delivery: 0 solver and 0 judge transport errors; 0 solver and 0 judge truncations; 0 solver and 0 judge empty finals. All planned cases remain in the declared score accounting. No selective retries were used.

Full dataset Apache-2.0 and upstream code MIT licenses, the pinned dataset README and source attribution are retained inside the trajectory archive.

Source: [BioReason-Pro released test data](https://huggingface.co/datasets/wanglab/bioreason-pro-test-data), revision `a18315a77d27dd4fe5a28b9b757695cff4ba4e3f`; publisher metadata declares Apache-2.0. [Exact numerical record](P44_HUMAN64_EXTENSION_EXPLANATION_RESULT_2026-10-22.json) · [Audited trajectories](../results/trajectories/qwen38_27b_p44_unattempted_human64_explanation_uniform16k_2026-10-22_v1.tar.gz).
