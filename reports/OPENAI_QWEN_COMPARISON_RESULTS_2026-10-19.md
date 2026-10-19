# OpenAI and archived Qwen comparison

Updated October 19, 2026, 2:20 PM PDT. The new benchmark runs are underway; no new benchmark accuracy has been calculated yet.

| Task | Cases | Archived Qwen replay | GPT-6 Luna | GPT-6.1 Sol |
|---|---:|---:|---|---|
| LitQA2: closed-book biological literature QA | 197 | 77 correct; 39.09% | Running | Running |
| SuppQA: closed-book paper-specific QA | 82 | 31 correct; 37.80% | Running | Running |
| Protein localization: sequence to one of ten compartments | 2,773 | 724 correct; 26.11% | Running | Development passed; larger-run budget decision pending |

The original Qwen outputs are reused. Question text, choice order, complete protein sequences and the shared localization definitions stay identical. SuppQA supplies paper titles and DOIs, without papers, supplements or retrieval. FigQA and TableQA remain a separate future vision condition requiring the original images.

Both OpenAI models passed their independent QA and localization delivery checks: **12/12 cases per model per condition**, with no truncations, empty finals, refusals or API errors. These 48 development cases are not benchmark scores, and biological correctness was not assessed. The small panels do not guarantee delivery on every benchmark case.

The [live evidence snapshot](../results/comparison_execution/openai_qwen_2026-10-19/runtime_snapshot.json) records observed saved responses, failures and usage with its own Pacific timestamp. Its linked archives contain public request bodies, wire hashes, privacy-redacted responses, visible finals and execution receipts. Exact original responses and prediction locks remain private. Each archive maps original/public hashes and removed metadata fields; the original lock's response hashes refer to the private originals. Unfinished snapshots do not certify complete generations or completed scoring.

An early public snapshot retained the API's echoed opaque safety identifier and encrypted response metadata. Current exports remove those fields while preserving visible final answers and their hashes. No API credential was included. Original Git history is preserved. Readable private chain of thought is not returned by the API; opaque encrypted content is excluded from the public export.

Predictions must be complete and sealed before the separate scorer opens original labels. Reports will show native and unambiguous-answer accuracy over every planned case, explicit abstentions, paired disagreements and uncertainty. There are no selective retries. A parsed insufficient-information choice is an abstention, not necessarily a correct or substantive answer.

The [execution plan](GPT6_LUNA_QWEN_COMPARISON_PLAN_2026-10-19.md), [scoring contract](COMPARISON_SCORING_CONTRACT_2026-10-19.md), [development input review](COMPARISON_DEVELOPMENT_GATE_2026-10-19.md) and [isolation checks](COMPARISON_DISPATCH_ISOLATION_2026-10-19.md) define the conditions. The dispatcher and scorer passed 39 tests, including actual kernel-enforced denial of repository reads and end-to-end failure handling.

This comparison audits inference-time answer separation. Prior training exposure to these public questions or proteins remains unknown for both providers. Equal token caps and nominal medium reasoning do not equalize internal compute. No model-family-wide biological-reasoning claim follows from this selected panel.
