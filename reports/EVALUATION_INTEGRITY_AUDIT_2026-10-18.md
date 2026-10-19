# Evaluation integrity audit

Reviewed October 18, 2026, at 11:00 PM PDT.

**Several results have substantial parsing, output-budget or metric limitations. The suite cannot be treated as a uniformly fair comparison of biological prediction ability.** Keeping a source metric and its full denominator makes a result reproducible; it does not remove these limitations.

## October 19 follow-up

The later review adds three narrower findings. [P36 whitespace normalization](P36_WHITESPACE_DIAGNOSTIC_2026-10-19.md) recovers five complete sequence serializations out of 59 while preserving the exact raw-format result of zero; biological function remains unassessed. Its archived ROUGE uses the target sequence and full input prompt as alternative references. [P08 sensitivity analysis](P08_SENSITIVITY_DIAGNOSTIC_2026-10-19.md) proves that filling only its 235 invalid predictions cannot turn its negative rank agreement positive: a conservative full-test Spearman upper bound is −0.067800. The exact full score remains undefined. [P12–P15 failure analysis](DEEPFRI_FAILURE_ANALYSIS_2026-10-19.md) separates truncation from label-vocabulary and duplicate-key problems and compares references on the same parsed case IDs.

The completed real-GFP validation pilot returned 12 responses: ten normal finite numeric finals and two truncated empty finals. It did not meet complete-delivery requirements. [Task-specific gates](TASK_SPECIFIC_DELIVERY_GATES_2026-10-19.md) replace the shared synthetic-pass gate for future runs. The historical extraction tool now requires actual hash-linked contracts and per-case question types; real historical rescoring remains blocked on missing originals. Full-score withholding when any output is invalid is a local completeness policy, distinct from the underlying numerical metric formulas.

The [action plan](EVALUATION_REPAIR_PLAN_2026-10-19.md) and [decision table](EVALUATION_DECISION_TABLE.md) now separate informative predictive results, answer-delivery failures, scorer failures and extraction diagnostics. The historical findings below remain available; this follow-up updates their interpretation.

- **P16:** The independently frozen terminal-number diagnostic recovers 850 normally finished labels, but only three more correct predictions. Accuracy is **12/5,651 (0.212%)**, alongside the unchanged original **9/5,651 (0.159%)**. This particular formatting repair does little to explain the poor reaction-class recovery under the tested full-sequence, joint-description generative interface. [Rule, counts and reproducible records](REACTION_EXTRACTION_DIAGNOSTIC_2026-10-19.md).
- **P42:** Zero of 200 candidate outputs were accepted; 196 reached the 1,024-token cap with thinking enabled. Its zero oracle-success score leaves candidate quality unmeasured. Any future positive oracle result would concern a trained fluorescence proxy, not experimental validation.
- **P03 and P43:** P03's 724/2,773 correct answers are accompanied by a 98.2% parse rate. Even recovering all 51 invalid answers as correct would reach only 27.95%, below the test set's descriptive 29.14% majority reference. P43's near-chance AUROCs come from valid one-token likelihood scores; the native length finish is intentional. [Prediction-task audit and qualifications](PREDICTION_TASK_AUDIT_2026-10-19.md).
- **B02:** Only 427/520 answers parsed; 93 reached the output cap. Its native non-abstention coverage must not be confused with usable-answer coverage. For B07, 76/86 parsed answers were correct, but that selected-subset rate cannot replace 76/600 full-task accuracy.
- **P12–P15:** The narrow null-versus-empty compatibility repair completed for all four settings. Their full AP/Fmax remain undefined because 285, 434, 296 and 76 predictions respectively remain invalid. Missing final answers remain invalid, genuine nonempty conflicts still fail, and original attempts are preserved. P13 recovery finished October 19 at 4:33 AM PDT. [Repair records](SCORER_COMPATIBILITY_REPAIR_2026-10-19.md).
- **P01 and V01–V05:** Frozen extraction checks are ready, but full rescoring is blocked by unavailable historical raw records in the local copies and public releases checked so far. No improved score is asserted from synthetic tests.

No new full benchmark rerun is part of these changes. The earlier synthetic delivery pilot and the subsequent real-validation pilot remain separate from benchmark scores; the existing mixed-budget results cannot establish a causal benefit from 16K outputs.

## Original October 18 findings

| Setting | Confirmed finding | What the result supports |
|---|---|---|
| P16 reaction classification | Of 5,651 responses, 1,120 parse and 4,531 are invalid. Among 904 nonempty rejected finals, 851 end with a standalone class number in the allowed range; 850 of these finish normally. The parser requires the entire final text to be a number, optionally prefixed `Answer:`. | The frozen 9/5,651 score measures prediction plus a strict output interface. It is strongly confounded by formatting and truncation. The 851 labels were identified without looking at correctness; their recoverability does not establish that they are correct. |
| P07 GFP fluorescence | 25,741/27,217 responses reached their output cap; only 1,382 parsed. Of the cases, 27,146 retain the historical 4K cap and only 71 use 16K. | Full-test Spearman is undefined. The parsed-only correlation is a diagnostic on a selected subset and does not complete the benchmark. |
| P14/P15 protein function | Both native scorers abort because raw API `content: null` differs from the executor's saved empty string. There are 91 such records for P14 and 18 for P15; no finish-reason mismatch or conflicting nonempty final was found. | This is a scorer/executor contract bug, not a low biological score. The failed attempts remain preserved. P12/P13 use the same guard. |
| B07 sequence questions; B08 cloning | 514/600 SeqQA responses and all 33 cloning responses reached the 4K cap. Those truncated outputs are invalid. | The low scores largely reflect failure to deliver a final answer under this execution budget. Native abstention coverage is not the fraction of parsed answers. |
| P01 solubility | 1,069/1,999 responses are invalid despite only three length finishes. The parser accepts a whole-final Yes/No answer, optionally prefixed `Answer:`. | Output formatting is a serious concern. The historical raw folder is unavailable in this workspace, so recovery was not freshly measured. |
| V01–V03 medical visual QA | The released CLOSED rule uses substring matching, including acceptance of an answer containing both “yes” and “no”. OPEN scoring uses token recall. | High native scores require this qualification: they do not establish unambiguous answer accuracy. V03's corrected denominator does not change the substring rule. |
| V04/V05 medical visual QA | V04 uses strict whole-final matching on verbose responses. V05's native extraction uses the final character; its native score is 2%, while a separately labeled full-text mapping is 49.75%. | These metrics are sensitive to answer formatting. Native and adapted results remain separate; neither extraction rule should silently replace the other. |
| P23–P26 protein descriptions | 3,827/9,128 responses reached the cap. Their parser permits strings, including empty strings. | “Parsed” does not certify a completed or biologically supported annotation. ROUGE is text overlap, not an explanation-support score. |

The P16 budget split makes the interface problem especially clear:

| Cohort | Cases | Parsed | Length finishes | Empty finals | Nonempty rejected finals |
|---|---:|---:|---:|---:|---:|
| Preserved 4K | 4,419 | 817 | 3,444 | 3,414 | 188 |
| Remaining 16K | 1,232 | 303 | 151 | 213 | 716 |
| Combined | 5,651 | 1,120 | 3,595 | 3,627 | 904 |

Length finishes and empty finals overlap. The two cohorts contain different cases; this is not a matched experiment on output budgets.

The earlier zero-recovery formatting diagnostic covered 9,005 P08/DeepFRI responses, not P16. Its finding does not establish that formatting cleanup cannot recover reaction labels.

Checks that passed provide narrower reassurance:

- All 197 LitQA2 replay responses were freshly checked: each has one explicit answer tag, all tags agree with saved predictions, all requests finish normally, and saved text and hashes match the raw records. The arithmetic reproduces 77 correct out of 197. Correctness does not validate the accompanying explanation.
- All 5,651 P16 case IDs appear once in source order, and stored targets match the keyed references. The official 0–383 class mapping is retained. In 48 deterministic raw samples, saved final text matches the API final content. No off-by-one class mapping or discarded nonempty final was found in these checks.
- Existing full 425-case figure/table audits checked source questions, choice permutations, images and requests. Existing protein split audits checked ordered sequence/label hashes. Their documented qualifications remain in force.
- Invalid outputs remain in native denominators. Missing full-test correlations stay undefined. Raw outputs and historical budgets remain preserved.

Paper values are context, rather than a controlled model ranking. Several references use task training or learned protein encoders; this baseline uses generative zero-shot prompts. For example, ProtST scores reaction classes using separate protein/text embeddings and an argmax, while this baseline reads a joint list of class descriptions and must generate a formatted label. The latter introduces an output-format failure channel. Some released test sets and paper test counts also differ.

The P16 headline also selected the wrong label-text reference variant: ProtST reports **21.91%** with pretraining-template descriptions, closer to the text supplied here; **29.85%** uses names and alternative names without scientific comments. Both numbers are valid published results, but they describe different conditions. The reference registry now selects the description variant first and retains the name variant. [Official Table 11 and Appendix B.3](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf#page=15).

Corrections must preserve this distinction. A null-versus-empty compatibility repair can fix the scorer crash while keeping missing finals invalid. Any formatting parser revision must be separately named, frozen before scoring, tested on synthetic answers, and applied to the same full denominator. It must not use reference answers to decide what the model meant. Historical scores must remain available, and selected failures must not be regenerated to improve the score.

This is a targeted audit, not fresh source-level verification of every setting. Several historical source/raw folders are unavailable locally. Public benchmark exposure during model training is unknown.

[Scores and qualifications](RESULTS_AT_A_GLANCE.md) · [Structured score records](RESULTS_AT_A_GLANCE.json) · [Output-budget provenance](OUTPUT_BUDGET_REVISION_2026-10-18.md)
