# OpenAI versus archived Qwen: fixed-task comparison

Updated October 19, 2026, Pacific time. **Run the 279 LitQA2/SuppQA cases first with GPT-6 Luna and GPT-6.1 Sol; make protein localization the committed second stage.** Reuse the exact archived Qwen3.8-27B outputs. FigQA/TableQA remain a separate vision comparison.

The user has authorized this new reviewed comparison. Execution still requires independent, model-specific development delivery evidence, frozen contracts, input/risk review and a reviewed cost estimate. This plan is not proof of dispatch or that the 4K budget passed. [Current scope configuration](../configs/openai_qwen_comparison_execution_v2_2026-10-19.json).

| Stage | Task and dataset | Cases | Archived Qwen usable answers | Archived Qwen correct / all cases | Supplied input and interpretation |
|---|---|---:|---:|---:|---|
| First: closed-book QA | B01 — LAB-Bench LitQA2 | 197 | 197/197 (100%) | 77/197 (39.1%) | Original biology question and choices; no retrieval. The two previously held cases remain excluded. |
| First: closed-book QA | B03 — LAB-Bench SuppQA | 82 | 82/82 (100%) | 31/82 (37.8%) | Original question, paper title, DOI and choices; no paper, supplement or retrieval. |
| Committed second stage | P03 — DeepLoc/PEER protein localization | 2,773 | 2,722/2,773 (98.2%) | 724/2,773 (26.1%) | Complete published sequence and the same ten-class ontology; predict one cellular location. |
| Separate vision condition | B04 — LAB-Bench FigQA | 181 | 180/181 (99.4%) | 131/181 (72.4%) | Original scientific figure images, question and choices. |
| Separate vision condition | B05 — LAB-Bench TableQA | 244 | 236/244 (96.7%) | 215/244 (88.1%) | Original table images, question and choices, including multi-image cases. |

These are the specific **archived replay baselines** with inspectable requests, responses and original scorer references. They are not replacements for historical headline scores from other runs. Tasks were selected for delivery/scoring reliability before seeing new OpenAI correctness; individual cases are not selected for Qwen correctness. [Candidate evidence and exact run identities](GPT6_LUNA_QWEN_COMPARISON_CANDIDATES_2026-10-19.json).

“Usable” means a valid answer under the frozen parser and can include the explicit insufficient-information choice: Qwen selected it for nine B01 and three B03 cases. It does not mean a substantive or correct answer. Native LAB non-abstention coverage is separate. B01/B03 have zero truncations, empty finals and transport errors. The selected B04 replay has one truncation/empty final; B05 has eight truncations and seven empty finals; P03 has 47 truncations and 51 empty finals. All five archived conditions report zero transport errors.

## What the comparison measures

LitQA2 tests answers to fixed biological-literature questions without retrieval. SuppQA is **closed-book paper-specific QA**: the paper title and DOI stay because they are legitimate native inputs, but a DOI does not fetch the article. Success could reflect scientific knowledge, remembered literature, option-based inference or prior benchmark exposure. This condition does not establish reading an unfamiliar supplied paper or supplement.

P03 adds a sequence-to-outcome prediction objective. It is committed in both this plan and the current v2 configuration, rather than an optional sequence add-on. Its full Luna run follows the P03-specific development/input gate. The Sol P03 run additionally needs budget review because its output ceiling exceeds the initial spending guard.

## The actual dispatcher and input boundary

[Dispatcher](../scripts/run_isolated_openai_comparison.py) · [Input-isolation and invariance tests](../tests/test_isolated_openai_comparison.py) · [Frozen answer policy](../configs/comparison_answer_policy_v1.json) · [Scoring contract](COMPARISON_SCORING_CONTRACT_2026-10-19.md).

Each preparation row has a dedicated `payload_without_private_safety_identifier` field. The runner submits only that allowlisted payload, adding the existing stable private safety identifier separately. It never serializes the surrounding case manifest, Qwen result, reference row, correctness flag or coding-agent conversation into the model request.

Every request is a fresh single-user context. No system hint, prior assistant solution, shared conversation, previous-response ID, web search, tool, file attachment or extra evidence is supplied. The text/sequence worker runs under Linux Landlock with a minimized bundle and output directory; it cannot read the repository, target references, Qwen responses, reports or unrelated files. Isolation failure blocks execution.

Before each call, the dispatcher verifies exact case identity/order, the frozen user text and choice order, allowed roles/fields, model and generation settings. It records the public-payload hash and the hash of the actual submitted bytes after adding the private identity; the secret value is not published. Source bundle and protocol hashes bind the eventual output lock to what was actually dispatched.

Scorer-data invariance tests change or remove separate labels, predictions, correctness flags and audit paths while keeping legitimate questions/options fixed. Model-facing bytes must remain identical. Changing an option's actual text would change a legitimate input and is not the intended invariance test.

For the separate vision comparison, exact required image bytes, order and detail must first be frozen in a dedicated contract. The present text/sequence dispatcher does not enable FigQA/TableQA as text-only substitutes. Both OpenAI model pages document image input; image support alone is not an executed vision evaluation. [Luna documentation](https://developers.openai.com/api/docs/models/gpt-6-luna) · [Sol documentation](https://developers.openai.com/api/docs/models/gpt-6.1-sol).

## Task-specific development gates and budget

The first candidate condition is **4,096 total output tokens**, medium reasoning, Standard processing (`service_tier: default`) and `store: false`. The allowance includes reasoning and visible output; exhaustion can leave no final answer. Qwen's temperature/top-p/top-k and seed are not portable equivalents to OpenAI reasoning controls. Disclose those differences; equal nominal token caps and “medium” do not equalize reasoning compute.

The independent preparation contains **12 newly authored primary-source-grounded QA questions**—six literature-like and six paper-specific—and **12 real P03 validation sequences** spanning 40–1,000 residues. The public LAB release's train-named rows are evaluation material and are not reused as development examples. [Development inputs, provenance and limitations](COMPARISON_DEVELOPMENT_GATE_2026-10-19.md).

Development must run separately for each model. Inspect native and strict final-answer delivery, truncations, empty finals, refusals, errors, actual usage and latency. Freeze the model-specific budget and residual-failure policy before inspecting held-out correctness. Small-panel success is an initial check, not a guarantee of all-case reliability. A failed check stays visible; a changed budget or prompt becomes another named condition. The earlier generic synthetic checks and unrelated GFP pilot are insufficient gates for these tasks.

At documented Standard short-context rates, the output ceilings for one attempt per case are:

| Stage | GPT-6 Luna | GPT-6.1 Sol |
|---|---:|---:|
| LitQA2 + SuppQA: 279 × 4,096 output tokens | $0.571392 | $11.427840 |
| P03: 2,773 × 4,096 output tokens | $5.679104 | $113.582080 |

Input charges and development requests are additional; these are ceilings from the proposed allowance, not measured bills. Luna costs $0.10 input / $0.50 output per million tokens; Sol costs $2 input / $10 output. [Official Luna pricing](https://developers.openai.com/api/docs/models/gpt-6-luna) · [Official Sol pricing](https://developers.openai.com/api/docs/models/gpt-6.1-sol).

Using the frozen user-text byte counts plus a conservative allowance of 100 input tokens per request gives planning totals including input of approximately **$0.596107 Luna / $11.922134 Sol for the 279 QA cases**, and **$6.236182 Luna / $124.723644 Sol for P03**. This byte-based reservation is a conservative planning estimate rather than exact vendor tokenization or a measured bill; development costs remain additional.

The **agent-imposed initial $50 spending guard remains**; it is not a numerical cap supplied by the user. Sol's P03 output ceiling alone exceeds it, so that stage is pending explicit budget review. No automatic Sol localization dispatch is authorized by listing it in the scientific plan.

## Freeze outputs before scoring

[Offline scorer](../scripts/score_model_comparison.py) · [Scorer synthetic and negative tests](../tests/test_score_model_comparison.py).

Save every response, refusal, transport/API error, truncation and empty final. Seal the complete ordered output set before opening the original target references. The scorer verifies actual request/response/final hashes and run/model/protocol associations before reading the hash-pinned original label archives. Labels are never reconstructed from Qwen correctness flags.

Report each task separately, with **native accuracy and unambiguous-answer accuracy over the full denominator**. The same frozen policy applies to archived Qwen and OpenAI. Preserve native permissive parsing beside the strict diagnostic; never choose an interpretation using the gold label. Invalid, missing, refused or truncated outcomes stay in the comparison denominator. Do not selectively replace failures or rerun Qwen to fill its invalid cases.

For both native and strict outcomes, report both-correct, OpenAI-only-correct, Qwen-only-correct and both-wrong counts, the accuracy gap, an exact McNemar discordance test and a paired bootstrap interval. Keep paper/DOI groups together when complete verified grouping is available; otherwise label case-level uncertainty. Protein-family dependence remains unresolved without verified grouping. One SuppQA question changes its accuracy by about 1.22 percentage points, so small gaps require paired uncertainty context. No pooled overall biology score is proposed.

## Authorization, original evidence and claim limits

The historical global OpenAI hold record remains unchanged, and no provider response or warning resolution is claimed. The current user's “let's go” instruction authorizes this **new, narrowly reviewed benign comparison and its development checks**; it does not resume the prior flagged scope. P18's flagged requests and the same two held B01 cases remain excluded. Use the original stable private safety identifier; it is monitoring metadata, not an exemption. Stop new dispatch on policy/access failures and preserve outcomes without identity rotation, provider switching or retries designed to bypass a block.

The [original proposed config](../configs/proposed_gpt6_luna_qwen_comparison_2026-10-19.json) and [279 draft request bytes](../results/comparison_preparation/gpt6_luna_qwen_2026-10-19/luna_text_requests_proposed.jsonl) remain immutable preparation provenance from commit `d7832220`. The original config's `optional_sequence_task` key describes that earlier draft and is superseded by the committed second stage in the [v2 scope](../configs/openai_qwen_comparison_execution_v2_2026-10-19.json). Actual stage-specific protocol, minimized request, review and completion receipts determine execution status.

The [per-case evidence manifest](../results/comparison_preparation/gpt6_luna_qwen_2026-10-19/case_manifest.jsonl) is exclusively audit/scorer material. It contains Qwen correctness flags and response paths and must never become solver input. Five older B01 OpenAI cases existed before the historical hold; this new fixed-cohort comparison remains a separate condition and does not select replacements using those results.

**Inference-time answer separation is auditable; prior training exposure remains unknown for both models.** Public questions or proteins may have been seen during training. Clean requests, shuffled choices and a benchmark canary cannot establish novelty. The result supports a comparison of named model conditions on these fixed cases, inputs and budgets. It does not establish faithful reasoning, unfamiliar-paper reading, novel-protein generalization or a general verdict on biological intelligence.

Reusing the archived Qwen outputs is justified for this unchanged input condition. Supplying papers, altering options, redesigning the answer format or changing the output budget would define a separate experiment and generally require a new matched Qwen condition as well.
