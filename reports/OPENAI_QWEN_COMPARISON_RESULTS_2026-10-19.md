# OpenAI and archived Qwen comparison

Updated October 19, 2026, 02:41 PM PDT. Only complete, sealed benchmark score files appear in the accuracy tables. Saved generation responses alone are not completed benchmark scores.

| Dispatched condition | Saved / planned | Complete output lock | Errors | Truncations | Empty finals | Refusals |
|---|---:|---|---:|---:|---:|---:|
| localization_gpt-6-luna | 744/2773 | No | 0 | 0 | 0 | 0 |
| publicqa_gpt-6-luna | 279/279 | Yes | 0 | 0 | 0 | 0 |
| publicqa_gpt-6_1-sol | 279/279 | Yes | 0 | 0 | 0 | 0 |

| Dispatched condition | Recorded input tokens | Recorded output tokens | Cached input tokens | Standard uncached cost estimate |
|---|---:|---:|---:|---:|
| localization_gpt-6-luna | Pending aggregate | Pending aggregate | Pending aggregate | Pending aggregate |
| publicqa_gpt-6-luna | 52485 | 202307 | 0 | $0.106402 |
| publicqa_gpt-6_1-sol | 52485 | 64464 | 0 | $0.749610 |

Runtime aggregate usage may wait for terminal execution metadata; per-response actual token usage is preserved in the linked raw archives. The cost column uses documented Standard uncached prices and is an estimate, not a provider invoice.

Sol protein-localization benchmark inference was **not dispatched; the user chose Luna only for continuing work**. The completed Luna/Sol QA comparisons are preserved, and current inference continues with Luna localization only. [Prospective model scope](../configs/openai_comparison_model_scope_2026-10-19.json).

The original Qwen outputs are reused. SuppQA supplies its title and DOI but no paper, supplement or retrieval. Protein localization supplies the complete published sequence and the same ten-class definitions. FigQA/TableQA remain a separate vision condition.

Both models passed their QA and localization delivery checks: 12/12 per model and condition, with no truncations, empty finals, refusals or API errors. These 48 development responses are delivery evidence; biological correctness was not assessed, and small-panel success does not guarantee all-case reliability.

## Complete benchmark scores

Native and strict unambiguous accuracy use every planned case. An explicit insufficient-information choice is a usable abstention, rather than a substantive answer. Historical headline scores remain preserved separately.

| Task | Model | Native correct / all | Native accuracy | Strict correct / all | Strict accuracy | Native parsed / all | Strict parsed / all | Explicit abstentions |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| LitQA2 (closed-book literature QA) | Qwen3.8-27B archived | 77/197 | 39.09% | 77/197 | 39.09% | 197/197 | 197/197 | 9 |
| LitQA2 (closed-book literature QA) | gpt-6-luna | 97/197 | 49.24% | 97/197 | 49.24% | 197/197 | 197/197 | 8 |
| SuppQA (closed-book paper-specific QA) | Qwen3.8-27B archived | 31/82 | 37.80% | 31/82 | 37.80% | 82/82 | 82/82 | 3 |
| SuppQA (closed-book paper-specific QA) | gpt-6-luna | 44/82 | 53.66% | 44/82 | 53.66% | 82/82 | 82/82 | 1 |
| LitQA2 (closed-book literature QA) | gpt-6.1-sol | 112/197 | 56.85% | 112/197 | 56.85% | 197/197 | 197/197 | 8 |
| SuppQA (closed-book paper-specific QA) | gpt-6.1-sol | 46/82 | 56.10% | 46/82 | 56.10% | 82/82 | 82/82 | 3 |

### Delivery and native abstention measures

| Task | Model | Errors | Not dispatched | Truncations | Empty finals | Refusals | Native non-abstention coverage | Native non-abstention precision |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| B01 | Qwen3.8-27B archived | 0 | 0 | 0 | 0 | 0 | 95.43% | 40.96% |
| B01 | gpt-6-luna | 0 | 0 | 0 | 0 | 0 | 95.94% | 51.32% |
| B03 | Qwen3.8-27B archived | 0 | 0 | 0 | 0 | 0 | 96.34% | 39.24% |
| B03 | gpt-6-luna | 0 | 0 | 0 | 0 | 0 | 98.78% | 54.32% |
| B01 | gpt-6.1-sol | 0 | 0 | 0 | 0 | 0 | 95.94% | 59.26% |
| B03 | gpt-6.1-sol | 0 | 0 | 0 | 0 | 0 | 96.34% | 58.23% |

Native coverage is non-abstention, not usable-answer rate. Errors, refusals, truncations, missing finals and invalid answers stay in the comparison denominator.

### Paired differences on exactly the same cases

| Task | OpenAI model | Rule | Both correct | OpenAI only | Qwen only | Both wrong | Accuracy gap | 95% paired bootstrap interval | Exact McNemar p | Resampling unit |
|---|---|---|---:|---:|---:|---:|---:|---|---:|---|
| B01 | gpt-6-luna | Native | 54 | 43 | 23 | 77 | +10.15 pp | [+2.54, +17.77] pp | 0.0186573 | case (197) |
| B01 | gpt-6-luna | Strict | 54 | 43 | 23 | 77 | +10.15 pp | [+2.54, +17.77] pp | 0.0186573 | case (197) |
| B03 | gpt-6-luna | Native | 23 | 21 | 8 | 30 | +15.85 pp | [+3.66, +28.05] pp | 0.0241195 | scorer_group_id (82) |
| B03 | gpt-6-luna | Strict | 23 | 21 | 8 | 30 | +15.85 pp | [+3.66, +28.05] pp | 0.0241195 | scorer_group_id (82) |
| B01 | gpt-6.1-sol | Native | 63 | 49 | 14 | 71 | +17.77 pp | [+10.15, +25.38] pp | 1.1123e-05 | case (197) |
| B01 | gpt-6.1-sol | Strict | 63 | 49 | 14 | 71 | +17.77 pp | [+10.15, +25.38] pp | 1.1123e-05 | case (197) |
| B03 | gpt-6.1-sol | Native | 21 | 25 | 10 | 26 | +18.29 pp | [+4.88, +31.71] pp | 0.0166738 | scorer_group_id (82) |
| B03 | gpt-6.1-sol | Strict | 21 | 25 | 10 | 26 | +18.29 pp | [+4.88, +31.71] pp | 0.0166738 | scorer_group_id (82) |

The paired intervals are conditional on these fixed public cases and one generation per model. DOI groups stay together where verified; protein-family dependence may remain unresolved. The conventional McNemar result does not establish independent cases. No pooled overall biological-capability score is computed.

## Scoring and audit evidence

| Condition | Native scoring state | Evidence |
|---|---|---|
| publicqa_gpt-6-luna | completed | [Sealed full result](../results/comparison_execution/openai_qwen_2026-10-19/analysis/publicqa_gpt-6-luna.scores.json) |
| publicqa_gpt-6_1-sol | completed | [Sealed full result](../results/comparison_execution/openai_qwen_2026-10-19/analysis/publicqa_gpt-6_1-sol.scores.json) |
| localization_gpt-6-luna | awaiting_prediction_lock | Waiting for complete generation/validated scoring |

[Complete reused Qwen request/response/final archives](../results/comparison_execution/openai_qwen_2026-10-19/qwen_archives/manifest.json) · [Generation snapshot and trajectory archives](../results/comparison_execution/openai_qwen_2026-10-19/runtime_snapshot.json) · [Scoring publication inventory](../results/comparison_execution/openai_qwen_2026-10-19/analysis/publication_inventory.json) · [Execution plan](GPT6_LUNA_QWEN_COMPARISON_PLAN_2026-10-19.md) · [Scoring contract](COMPARISON_SCORING_CONTRACT_2026-10-19.md) · [Development review](COMPARISON_DEVELOPMENT_GATE_2026-10-19.md) · [Isolation checks](COMPARISON_DISPATCH_ISOLATION_2026-10-19.md).

The OpenAI public archives preserve public payloads, outbound hashes, privacy-redacted API responses, returned final text, per-response token usage and execution receipts. Immutable original API responses and prediction locks remain private. Publication mappings record original/public file hashes and the removed field paths; original lock hashes refer to those private originals, so a redacted response is not claimed to be byte-identical to its original. Visible-final text and hashes stay unchanged. Private chain of thought is not returned as readable API text and is not archived; opaque encrypted response content is excluded from publication. Any actually returned reasoning summary is distinct from Qwen reasoning text. There are no selective inference retries.

An early public snapshot retained an echoed opaque safety identifier and encrypted response metadata. The corrected current archives remove those fields and document the transformation; no API credential was included. The original Git history is preserved.

This comparison audits inference-time answer separation. Prior training exposure to these public questions or proteins remains unknown for both providers. Equal token caps and nominal medium reasoning do not equalize internal compute. Correct answers do not establish faithful explanations, unfamiliar-paper reading, novel-protein generalization or a model-family-wide verdict.
