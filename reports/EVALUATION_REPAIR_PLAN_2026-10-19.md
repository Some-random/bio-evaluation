# Evaluation action plan

Updated October 19, 2026, Pacific time. Current priority: improve the existing evidence through offline analyses, and continue resolving unfinished catalog tasks. The optional full-task repetitions below are not an active generation queue and are not the remaining catalog case count. Original scores, raw outputs and denominators stay unchanged.

## Closed items

- P12–P15 null-versus-empty compatibility repair: all four completed and published. Their original failures remain archived; full AP/Fmax remain undefined under the local completeness policy.
- P16 terminal-number diagnostic: published separately, 12/5,651 correct alongside original 9/5,651.
- B02 and P42 output-delivery qualifications: added prominently.
- Historical-output search: documented; absent originals remain unavailable evidence, not zero recovery counts. Further recovery should target the original storage or an identified backup.

These items are not being sent back for another general audit. [Completed-work review](COMPLETED_WORK_REVIEW.md).

## Completed follow-up revision

| Review item | Work | Completed deliverable |
|---|---|---|
| 1 | P36 serialization interpretation | Exact 0/59 preserved; separate outer-whitespace-only 5/59 diagnostic published with hashes. Archived ROUGE uses both target sequence and full input prompt; function/design success remains unassessed. [Evidence](P36_WHITESPACE_DIAGNOSTIC_2026-10-19.md). |
| 2 | P08 stability evidence | Parsed-case correlation reproduced; conservative full-test upper bound −0.067800 established for any finite replacement of missing values. Invalid answers classified without references and native score direction checked. Full-test correlation remains undefined. [Evidence](P08_SENSITIVITY_DIAGNOSTIC_2026-10-19.md). |
| 3 | P12–P15 remaining failures | Failure types separated, including unknown IDs and identical versus conflicting duplicates. All-zero references evaluated on exactly the model's parsed case IDs; native AP and tie-grouped AP preserved. [Evidence](DEEPFRI_FAILURE_ANALYSIS_2026-10-19.md). |
| 4 | Task-specific delivery requirements | Shared synthetic-pass gate replaced. Complete real-GFP pilot published: 12 responses, 10 finite numeric finals, two truncated empty finals, no transport failures. [Requirements](TASK_SPECIFIC_DELIVERY_GATES_2026-10-19.md). |
| 5 | Historical extraction provenance | Tool now opens and hashes the actual original contract, verifies exact case membership and run/protocol/request association, and selects OPEN/CLOSED rules per case. All 23 synthetic checks pass, including wrong-run and bogus-hash cases. Real historical rescoring remains blocked on absent source evidence. [Status](HISTORICAL_EXTRACTION_STATUS_2026-10-19.md). |

The all-outputs-must-parse condition is a local completeness policy, distinct from the numerical metric formula. Clearly labeled subset analyses and sensitivity bounds can be useful without replacing undefined full scores.

## Conditional future runs

There is no unconditional shared “pilot passed, launch everything” sequence. Each optional repeated evaluation requires its own relevant development evidence and separately reviewed frozen protocol. These proposals do not replace work on the unfinished catalog.

| Task | Decision before a full run |
|---|---|
| B08 cloning, 33 cases | First small complete QA candidate after cloning-specific development/example checks using the actual prompt and native answer format. Inputs and context fit are verified; inference has not started. |
| B07 SeqQA, 600 cases | Next QA priority after representative sequence-length and question-type delivery checks. |
| P42 GFP design, 200 slots | Separate generation branch. Validate full-length sequences in both edit regimes; freeze task-specific sampling and per-slot randomness. A ten-residue toy edit is insufficient. |
| P16 reaction, 5,651 cases | Defer the large repeat until actual sequence/class-description delivery is checked and its scientific purpose is stated. Parser recovery alone added only three correct labels. |
| P07 fluorescence, 27,217 cases | Last large repeat. The real-GFP pilot did not achieve complete delivery; define a reliable scalar procedure and residual-failure policy before this workload. |
| P08 stability | Deprioritize a full repeat whose sole purpose is parser repair; the negative-correlation sensitivity result is more informative now. |

[Machine-readable task-specific requirements](../configs/task_specific_delivery_gates_2026-10-19.json) · [Decision table](EVALUATION_DECISION_TABLE.md) · [Integrity audit](EVALUATION_INTEGRITY_AUDIT_2026-10-18.md)

## Completed scoped model comparison

The separately reviewed October 19 comparison has finished and been scored.
Luna answered all 197 LitQA2 and 82 SuppQA cases, scoring 97/197 and 44/82.
Protein localization closed all 2,773 cases with 2,770 delivered responses and
three transport failures; Luna scored 1,575/2,773. Native and strict answer
scores agree. The exact archived Qwen inputs and outputs were reused without
regeneration. The previously completed Sol QA results remain archived; further
Sol inference was cancelled when the user selected Luna only. Figure/table QA
remains a separately proposed visual comparison.

The old global authorization remains disabled as historical incident state.
This later case-scoped comparison did not retry the flagged material and does
not establish provider clearance of the historical warning. The current
results and execution evidence supersede the earlier preparation-only status:
[comparison results](OPENAI_QWEN_COMPARISON_RESULTS_2026-10-19.md),
[dispatcher isolation](COMPARISON_DISPATCH_ISOLATION_2026-10-19.md), and
[incident follow-up](POLICY_INCIDENT_2026-10-14.md).
