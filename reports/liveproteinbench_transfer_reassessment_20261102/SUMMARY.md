# Label distributions, transitions and agreement

**Output usability is separate from scientific answerability.** A usable output is a format-valid review and may label the question reasoning-supported, lookup-dependent or uncertain. Usability does not certify biological correctness. Output errors count model responses, not defective questions or wrong keys.

Every distribution uses that model and round’s usable-output denominator. Each model’s before → after transitions use only the same cases with usable outputs for that model in both rounds. Cases with old output errors are reported separately and cannot enter a label transition. Labels from output errors and empty finals are never repaired or recoded.

## GPT-6 Luna

| Round | Usable outputs / 1,328 | Output errors | Missing records | Key labels, usable only: supported / contradicted / uncertain | Answerability labels, usable only: reasoning / lookup / uncertain |
|---|---|---|---|---|---|
| before | 1328 / 1,328 | 0 | 0 | 1285 / 30 / 13 | 35 / 1292 / 1 |
| after | 1308 / 1,328 | 20 | 0 | 1259 / 28 / 21 | 999 / 294 / 15 |

**Cases with old output errors or missing records, separate from label transitions:** 0. Of those, 0 have a usable new output. Old usable output → new output error/missing record: 20.

New output-error shapes (canonical machine fields retained): `{"no_visible_final_review_text":0,"parsed_visible_review_preserved":2,"visible_text_without_parsed_review":18}`.

### expected answer: before → after

**Same-model denominator with usable outputs before and after: 1308.** Rows before; columns after.

| Before ↓ / after → | supported | contradicted | uncertain |
|---|---|---|---|
| supported | 1253 | 3 | 9 |
| contradicted | 4 | 23 | 3 |
| uncertain | 2 | 2 | 9 |

### answerability: before → after

**Same-model denominator with usable outputs before and after: 1308.** Rows before; columns after.

| Before ↓ / after → | reasoning-supported | lookup-dependent | uncertain |
|---|---|---|---|
| reasoning-supported | 33 | 2 | 0 |
| lookup-dependent | 965 | 292 | 15 |
| uncertain | 1 | 0 | 0 |

## Qwen3.8-Flash-Next-NVFP4

| Round | Usable outputs / 1,328 | Output errors | Missing records | Key labels, usable only: supported / contradicted / uncertain | Answerability labels, usable only: reasoning / lookup / uncertain |
|---|---|---|---|---|---|
| before | 1277 / 1,328 | 51 | 0 | 1252 / 21 / 4 | 684 / 593 / 0 |
| after | 1305 / 1,328 | 23 | 0 | 1281 / 19 / 5 | 1201 / 104 / 0 |

**Cases with old output errors or missing records, separate from label transitions:** 51. Of those, 50 have a usable new output. Old usable output → new output error/missing record: 22.

New output-error shapes (canonical machine fields retained): `{"no_visible_final_review_text":21,"parsed_visible_review_preserved":1,"visible_text_without_parsed_review":1}`.

### expected answer: before → after

**Same-model denominator with usable outputs before and after: 1255.** Rows before; columns after.

| Before ↓ / after → | supported | contradicted | uncertain |
|---|---|---|---|
| supported | 1225 | 2 | 3 |
| contradicted | 4 | 17 | 0 |
| uncertain | 2 | 0 | 2 |

### answerability: before → after

**Same-model denominator with usable outputs before and after: 1255.** Rows before; columns after.

| Before ↓ / after → | reasoning-supported | lookup-dependent | uncertain |
|---|---|---|---|
| reasoning-supported | 673 | 0 | 0 |
| lookup-dependent | 490 | 92 | 0 |
| uncertain | 0 | 0 | 0 |

## Before versus after agreement on the fixed four-way format-valid intersection

**Identical denominator for both rounds: 1238/1,328.** Every included case has usable review outputs from both models in both rounds. This is the comparison of agreement over time. Case IDs are enumerated in summary.json.

| Measure | Before count / same denominator | After count / same denominator | Change in count |
|---|---|---|---|
| expected_answer_agree | 1214/1238 | 1201/1238 | -13 |
| answerability_agree | 538/1238 | 1023/1238 | +485 |
| both_labels_agree | 530/1238 | 997/1238 | +467 |
| reasoning_supported_by_both | 0/1238 | 948/1238 | +948 |
| lookup_dependent_by_both | 538/1238 | 75/1238 | -463 |

## Before: descriptive agreement on that round’s pairs with two usable outputs

**Round-specific denominator with two usable outputs: 1277/1,328.** This may differ from the four-way format-valid intersection. These descriptive round metrics must not be subtracted to claim a before/after change.

| Measure | Numerator / round-specific denominator |
|---|---|
| expected_answer_agree | 1253/1277 |
| answerability_agree | 558/1277 |
| both_labels_agree | 550/1277 |
| reasoning_supported_by_both | 0/1277 |
| lookup_dependent_by_both | 558/1277 |

### expected answer cross-tab

| Luna ↓ / Qwen → | supported | contradicted | uncertain |
|---|---|---|---|
| supported | 1233 | 1 | 1 |
| contradicted | 13 | 17 | 0 |
| uncertain | 6 | 3 | 3 |

### answerability cross-tab

| Luna ↓ / Qwen → | reasoning-supported | lookup-dependent | uncertain |
|---|---|---|---|
| reasoning-supported | 0 | 35 | 0 |
| lookup-dependent | 683 | 558 | 0 |
| uncertain | 1 | 0 | 0 |

## After: descriptive agreement on that round’s pairs with two usable outputs

**Round-specific denominator with two usable outputs: 1287/1,328.** This may differ from the four-way format-valid intersection. These descriptive round metrics must not be subtracted to claim a before/after change.

| Measure | Numerator / round-specific denominator |
|---|---|
| expected_answer_agree | 1248/1287 |
| answerability_agree | 1056/1287 |
| both_labels_agree | 1028/1287 |
| reasoning_supported_by_both | 969/1287 |
| lookup_dependent_by_both | 87/1287 |

### expected answer cross-tab

| Luna ↓ / Qwen → | supported | contradicted | uncertain |
|---|---|---|---|
| supported | 1234 | 1 | 3 |
| contradicted | 16 | 12 | 0 |
| uncertain | 13 | 6 | 2 |

### answerability cross-tab

| Luna ↓ / Qwen → | reasoning-supported | lookup-dependent | uncertain |
|---|---|---|---|
| reasoning-supported | 969 | 14 | 0 |
| lookup-dependent | 203 | 87 | 0 |
| uncertain | 11 | 3 | 0 |

## New-round completion and output caps

Attempt completion includes output errors. Cap status comes from saved native termination metadata, never from output usability or hidden reasoning. Counts below contain no raw response IDs or private metadata. Actual token usage is available in summary.json. Exact Luna charges are unknown: returned 24h cache retention has no documented matching cache-write rate here. The inherited estimator’s partial priced-response sum and 30m/12h scenarios are not total charges or defensible billing bounds. Qwen’s local API has no per-request charge; GPU allocation cost is unknown.

| Reviewer | Attempted / terminal | Native output-cap reached | Native cap status unknown | Native finish / provider status counts |
|---|---|---|---|---|
| GPT-6 Luna | 1328 / 1328 | 0 | 0 | {&quot;completed&quot;:1328} |
| Qwen3.8-Flash-Next-NVFP4 | 1328 / 1328 | 21 | 0 | {&quot;length&quot;:21,&quot;stop&quot;:1307} |

Agreement, key-support labels and transferability labels are AI judgments. They are not new scientific adjudication or benchmark-solving accuracy. A one-attempt reassessment cannot isolate prompt effects from stochastic variation. No verdict was changed by the report renderer.
