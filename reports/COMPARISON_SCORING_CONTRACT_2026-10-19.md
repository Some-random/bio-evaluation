# Frozen comparison scoring contract

This offline scorer preserves every declared case, including errors, refusals, truncations and empty finals. It implements the same frozen answer semantics for the archived Qwen outputs and each new model. It performs no inference and does not authorize dispatch.

[Answer policy](../configs/comparison_answer_policy_v1.json) · [Scorer](../scripts/score_model_comparison.py) · [Synthetic and negative checks](../tests/test_score_model_comparison.py).

## What is scored

B01 LitQA2 and B03 SuppQA are the first 279 text cases. B03 is closed-book paper-specific QA: title and DOI are supplied, papers and supplements are not. P03 localization is a committed second stage under its own development check and frozen run contract. FigQA/TableQA require a separate image-byte/order contract; this first text/sequence scorer deliberately rejects their dispatch cohorts.

For each task and model, report native accuracy and separately named unambiguous-answer accuracy over the full planned denominator. Errors, refusals, truncations, missing finals and invalid answers are incorrect; no successful replacement is selected. The native ChemBench parser retains its permissive multiple-tag behavior. The strict diagnostic requires one distinct in-range single-letter tag value, permits repeated identical tags, and rejects conflicting, malformed, mismatched or multi-letter tags. Its plain-letter fallback is an exact raw uppercase letter. P03 uses its original whole-final class-0–9 parser.

An explicit insufficient-information choice is a parsed, usable abstention. Native LAB non-abstention coverage is reported separately from the usable-answer rate. It must not be described as answer delivery. Failure handling is an explicit full-denominator comparison policy, separate from the native parser formula; the original historical scores remain preserved.

Paired reports contain both-correct, OpenAI-only-correct, Qwen-only-correct and both-wrong counts, the OpenAI-minus-Qwen accuracy difference, an exact two-sided McNemar discordance test and a fixed-seed paired percentile bootstrap interval. Both native and strict outcomes get separate paired analyses. B03 DOI groups come only from legitimate frozen input metadata and are resampled together when complete. Without complete grouping metadata, uncertainty is explicitly conditional case-level uncertainty. Protein-family dependence remains unresolved when no verified family grouping is supplied. The McNemar calculation is a conventional case-level discordance test and does not establish case independence.

## Prediction lock and label boundary

Before opening any original target archive, the scorer verifies both complete prediction locks, their SHA-256 seals, exact ordered case IDs, all request/raw-response/final-file hashes and per-case model/run/protocol identity. Missing or reordered cases block scoring. Actual response final text, refusal/truncation flags and returned model identity must agree with the sealed record. The actual public payload must equal the frozen dedicated payload and the original Qwen user prompt including choice order. The OpenAI prediction lock must name the hashes of the exact frozen protocol and minimized request file used by its dispatcher.

Only then does the scorer open each hash-pinned original reference archive. Its hash must equal the original run configuration's pre-inference reference hash. Labels are never inferred from Qwen predictions or correctness flags. Missing originals block scoring. The native answer regex is read from its hash-verified frozen ChemBench constant and compared with the frozen policy literal.

A lock is an integrity record, not proof against an adversary able to rewrite both evidence and trusted hashes. Trusted hashes must remain those recorded in the frozen experiment protocol and original archived run. Read-only files and SHA-256 seals detect subsequent accidental changes; they do not replace trusted source provenance.

## Export the archived Qwen prediction lock

Call `export_qwen_lock` from `scripts/score_model_comparison.py` with the pinned candidate report, case manifest, `['B01', 'B03']`, and a new output directory. It copies exact original request/response bytes and visible-final text into a standalone sealed bundle, without opening the target references. It refuses to replace an existing bundle. The lock records the individual original Qwen run IDs even though the combined panel uses one analysis-side archive-panel ID.

The same function supports the separately named P03 panel. Neither export reruns Qwen or changes its archived outputs.

## Scoring plan template

Fill artifact hashes from the frozen protocol and completed prediction locks. Use **one separate comparison plan per OpenAI model**. `frozen_request_file` must identify the dispatcher's minimized `requests.jsonl`, not the surrounding preparation manifest containing audit metadata. New inference is not performed by this command.

```json
{
  "comparison_id": "luna_vs_qwen_publicqa_4k_v2",
  "tasks": ["B01", "B03"],
  "candidates": {
    "path": "reports/GPT6_LUNA_QWEN_COMPARISON_CANDIDATES_2026-10-19.json",
    "sha256": "FROZEN_CANDIDATE_FILE_SHA256"
  },
  "case_manifest": {
    "path": "results/comparison_preparation/gpt6_luna_qwen_2026-10-19/case_manifest.jsonl",
    "sha256": "FROZEN_ORIGINAL_CASE_MANIFEST_SHA256"
  },
  "answer_policy": {
    "path": "configs/comparison_answer_policy_v1.json",
    "sha256": "FROZEN_ANSWER_POLICY_FILE_SHA256"
  },
  "native_constant": {
    "path": ".local/litqa2_replay/baseline/sources/chembench_constant.py",
    "sha256": "71b4a92edfbe5b33e9a327b0773a2ae9cfd9946b48452f13127929a29e91021d"
  },
  "frozen_protocol": {
    "path": "PATH_TO_FROZEN_PROTOCOL.json",
    "sha256": "FROZEN_PROTOCOL_FILE_SHA256"
  },
  "frozen_request_file": {
    "path": "PATH_TO_LUNA_MINIMIZED_BUNDLE/requests.jsonl",
    "sha256": "FROZEN_DISPATCH_REQUEST_FILE_SHA256"
  },
  "qwen": {
    "model": "Qwen/Qwen3.8-27B",
    "run_id": "archived_qwen_publicqa_panel_2026-10-19_v2",
    "protocol_id": "openai_qwen_publicqa_4k_2026-10-19_v2",
    "response_style": "qwen_archive",
    "lock": {"path": "PATH_TO_ARCHIVE_BUNDLE/predictions_lock.json", "sha256": "COMPLETE_QWEN_LOCK_SHA256"}
  },
  "openai": {
    "model": "gpt-6-luna",
    "run_id": "EXACT_LUNA_RUN_ID",
    "protocol_id": "openai_qwen_publicqa_4k_2026-10-19_v2",
    "response_style": "openai_responses",
    "lock": {"path": "PATH_TO_LUNA_OUTPUT/predictions_lock.json", "sha256": "COMPLETE_LUNA_LOCK_SHA256"}
  },
  "uncertainty_grouping": {"B01": "case", "B03": "group"}
}
```

If an API returns a documented dated snapshot instead of the requested alias, freeze its exact permitted value in `openai.response_models` before scoring; a different unlisted response model blocks scoring. Do not silently accept an arbitrary model prefix.

Run `python scripts/score_model_comparison.py --plan <plan.json> --output <new-score.json>`. Existing score paths are never overwritten. Repeat with a separate fixed Sol plan and lock when that condition is authorized and complete. P03 uses its own protocol ID `openai_qwen_localization_4k_2026-10-19_v2` and `tasks: ["P03"]`; native-constant input is unnecessary for P03-only scoring.

## What the result can establish

This is a comparison of named archived and new model conditions on fixed public cases, supplied inputs and output budgets. Matching nominal token caps does not equalize reasoning compute. Inference-time answer separation is auditable; prior public-question/protein exposure remains unknown. Correct answers do not establish faithful explanations, reading an unfamiliar supplied paper, novel-protein generalization or an overall biological-reasoning score.
