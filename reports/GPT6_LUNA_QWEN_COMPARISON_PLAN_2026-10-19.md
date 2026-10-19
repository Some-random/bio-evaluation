# GPT-6-luna versus Qwen3.8-27B: comparison preparation

Prepared October 19, 2026, Pacific time. **Start with LitQA2 and SuppQA: 279 cases with complete, unambiguous Qwen answer delivery.** This is offline preparation. There are no new GPT benchmark results and no new Qwen generations.

The comparison reuses exact archived Qwen runs whose requests, responses, case identities and scoring references remain available. The table uses those specific replay scores, rather than substituting higher historical headline scores. Tasks are selected for reliable delivery and interpretable scoring; individual cases are not selected for Qwen correctness.

| Priority | Task and dataset | Cases | Qwen usable answers | Qwen correct / all cases | What it tests |
|---|---|---:|---:|---:|---|
| First text comparison | B01 — LAB-Bench LitQA2 | 197 | 197/197 (100%) | 77/197 (39.1%) | Biological literature questions with fixed choices. The same two previously held cases remain excluded. |
| First text comparison | B03 — LAB-Bench SuppQA | 82 | 82/82 (100%) | 31/82 (37.8%) | Paper-specific questions with the original paper title, DOI and choices. |
| Next sequence comparison | P03 — DeepLoc/PEER protein localization | 2,773 | 2,722/2,773 (98.2%) | 724/2,773 (26.1%) | A complete amino-acid sequence goes in; one of ten cellular-location classes comes out. Invalid answers remain wrong in all-case accuracy. |
| Optional visual comparison | B04 — LAB-Bench FigQA | 181 | 180/181 (99.4%) | 131/181 (72.4%) | Scientific figure images, questions and choices. |
| Optional visual comparison | B05 — LAB-Bench TableQA | 244 | 236/244 (96.7%) | 215/244 (88.1%) | Scientific table images, questions and choices, including multiple images. |

“Usable” is native parser validity, not native non-abstention coverage. B01/B03 have no truncations, empty finals or HTTP errors. B04 has one truncation/empty final; B05 has eight truncations and seven empty finals. P03 has 47 truncations and 51 empty finals. All five archived conditions report zero HTTP errors.

An additional output-only check found a single unambiguous native answer value for every parsed B01/B03/B04/B05 response, agreeing with its saved prediction. This does not validate the explanation. [Frozen rule and findings](../results/comparison_preparation/gpt6_luna_qwen_2026-10-19/qwen_answer_semantics_check.json).

## Common comparison contract

- Use the exact same complete case cohorts, user text, choice permutations and required images. Preserve paper metadata for SuppQA and full sequences for P03. No new system prompt, hints, tools or web search.
- Reuse the archived Qwen outputs. Give GPT-6-luna a separate run ID and retain every output, refusal, error and truncation. No selective successful retries or dropping Qwen's invalid cases.
- The proposed first condition uses the same nominal **4,096-token total output cap** as these archived Qwen runs, with medium reasoning requested. It is a comparison under that budget, not a claim about each model's maximum capability.
- OpenAI does not support Qwen's temperature/top-p settings when reasoning is enabled, and Qwen's top-k and fixed seed are not portable equivalents. The proposal omits these parameters and records the difference. Equal token counts and the word “medium” do not equalize actual reasoning compute. A different budget or prompt becomes another named condition.
- Apply the same frozen native scorer and full denominator. Report usable-answer rate, truncations, empty finals, refusals and errors beside accuracy. Native abstention precision and coverage remain separate. Also apply the frozen unambiguity check symmetrically to both models; ambiguous answers do not become clear answers merely because a permissive parser returns a letter.
- Report each task separately, paired correctness disagreements and an uncertainty interval for the accuracy difference. Do not pool the task scores into one biological-capability number.
- Save model identity, request/response hashes, final text, usage, latency and cost. OpenAI exposes reasoning summaries where supported, not raw private reasoning; these are not equivalent to Qwen's saved reasoning text.

Any case-level uncertainty calculation describes this fixed benchmark sample. Questions from the same paper or related protein sequences may be dependent; retain available grouping metadata and use grouped resampling where justified. It is not an interval over independent biological experiments or over every possible model run.

GPT-6-luna accepts text and image inputs, so visual tasks are technically possible. The same original image bytes/order must be preserved; vendor image processing remains a qualification. [Official model documentation](https://developers.openai.com/api/docs/models/gpt-6-luna) · [Reasoning and supported parameters](https://developers.openai.com/api/docs/guides/latest-model) · [Reasoning summaries](https://developers.openai.com/api/docs/guides/reasoning).

At the documented standard output price of $0.50 per million tokens, the first 279 cases have an **output-token cost ceiling of $0.571392** at the proposed cap. Input tokens and any other applicable billing are additional. This is arithmetic from the proposed limit, not a measured bill or completion-time estimate. [Pricing source](https://developers.openai.com/api/docs/models/gpt-6-luna).

## Why these come before other settings

Defer P07/P42, B07/B08 and P12–P15 for this first comparison because their delivery or schema issues need separate work. Defer medical VQA's ambiguous lexical/extraction metrics. P43 drug–target interaction has complete scores, but its one-token Yes/No likelihood method requires a validated probability interface; generated Yes/No answers or self-reported confidence are not interchangeable with that score. P43's original raw response availability is also incomplete.

## Evidence and current execution status

All candidate case sets and scoring references are checked against the archived run manifests. Missing top-level input paths do not require recreating labels: exact frozen copies and matching hashes were located in the retained replay archives. No labels are reconstructed from Qwen correctness flags.

- [Candidate evidence and source hashes](GPT6_LUNA_QWEN_COMPARISON_CANDIDATES_2026-10-19.json)
- [Per-case artifact manifest](../results/comparison_preparation/gpt6_luna_qwen_2026-10-19/case_manifest.jsonl) — analysis/scorer evidence only; never solver input.
- [279 proposed text requests](../results/comparison_preparation/gpt6_luna_qwen_2026-10-19/luna_text_requests_proposed.jsonl) — exact user prompts, no answers, no credentials or private identifier.
- [Proposed configuration](../configs/proposed_gpt6_luna_qwen_comparison_2026-10-19.json)

These files do not enable dispatch. The existing OpenAI benchmark hold remains recorded pending account-scope clarification and task/case review. The earlier three neutral connectivity checks are not benchmark clearance. The existing stable private safety identifier must be preserved at any future authorized dispatch; it is an abuse-monitoring identifier, not an exemption. [Official safety-identifier documentation](https://developers.openai.com/api/docs/guides/safety-checks).

Before a full comparison, validate the API mapping and native answer delivery on suitable permitted development examples, then freeze the protocol before examining held-out GPT correctness. Keep the existing flagged-task holds. Public benchmark pretraining exposure remains unknown for both models, and answer accuracy does not establish faithful biological reasoning.
