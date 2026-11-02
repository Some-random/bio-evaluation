# Paired review summary

All per-model label distributions below use that model’s valid-review denominator. Every paired measure uses only the jointly valid denominator. Invalid parsed labels, missing fields, and missing visible finals are never repaired or recoded.

## GPT-6 Luna

**Valid-review denominator: 1735/1,736.**

Saved status counts: `{"invalid_review":1,"valid_review":1735}`.

Invalid review shapes: `{"no_visible_final_review_text":0,"parsed_visible_review_preserved":1,"visible_text_without_parsed_review":0}`. Missing question/attempt records: **0**.

| Expected-answer support | Count / valid denominator |
|---|---|
| supported | 1690 / 1735 |
| contradicted | 31 / 1735 |
| uncertain | 14 / 1735 |

| Reasoning / lookup | Count / valid denominator |
|---|---|
| reasoning-supported | 442 / 1735 |
| lookup-dependent | 1292 / 1735 |
| uncertain | 1 / 1735 |

## Qwen3.8-Flash-Next-NVFP4

**Valid-review denominator: 1675/1,736.**

Saved status counts: `{"invalid_review":61,"valid_review":1675}`.

Invalid review shapes: `{"no_visible_final_review_text":12,"parsed_visible_review_preserved":48,"visible_text_without_parsed_review":1}`. Missing question/attempt records: **0**.

| Expected-answer support | Count / valid denominator |
|---|---|
| supported | 1650 / 1675 |
| contradicted | 21 / 1675 |
| uncertain | 4 / 1675 |

| Reasoning / lookup | Count / valid denominator |
|---|---|
| reasoning-supported | 1082 / 1675 |
| lookup-dependent | 593 / 1675 |
| uncertain | 0 / 1675 |

## Agreement on jointly valid pairs

**Denominator: 1674/1,736; 62 cases are not jointly valid.**

| Paired measure | Count / jointly valid denominator | Percent |
|---|---|---|
| Expected-answer support agrees | 1648 / 1674 | 98.45% |
| Reasoning / lookup agrees | 955 / 1674 | 57.05% |
| Both axes agree | 945 / 1674 | 56.45% |
| Reasoning-supported by both (AI labels) | 397 / 1674 | 23.72% |
| Lookup-dependent by both (AI labels) | 558 / 1674 | 33.33% |

Agreement is not scientific truth, expert adjudication, or a replacement benchmark key. The same supplied evidence can lead both models to share an error.

## Expected-answer support cross-tab

Rows: Luna; columns: Qwen. All cells jointly valid only.

| Luna ↓ / Qwen → | supported | contradicted | uncertain |
|---|---|---|---|
| supported | 1628 | 1 | 1 |
| contradicted | 14 | 17 | 0 |
| uncertain | 7 | 3 | 3 |

## Reasoning / lookup cross-tab

Rows: Luna; columns: Qwen. All cells jointly valid only.

| Luna ↓ / Qwen → | reasoning-supported | lookup-dependent | uncertain |
|---|---|---|---|
| reasoning-supported | 397 | 35 | 0 |
| lookup-dependent | 683 | 558 | 0 |
| uncertain | 1 | 0 | 0 |

## Completion and output limits

Qwen has **1736 attempted and 1736 terminal records**. All HTTP status counts: `{"200":1736}`. Native finishes are **1723 stop + 13 length**. The length-finished records are inside the invalid total, not additional examples. Of the invalid records, 12 have no visible final text and 1 retain visible text without a parsed review. Extraction and validation diagnostic categories can overlap.

Qwen extraction diagnostic counts: `{"ValueError:Qwen final content is not text":12}`. Validation diagnostic counts: `{"answerability_check:missing_item_specific_fact_must_be_text":5,"expected_answer_check:invalid_evidence_ids":1,"incomplete_or_non_native_termination":1,"invalid_json:Unterminated string starting at: line 5 column 15 (char 110)":1,"question_ambiguity:invalid_option_ids":42}`.

Luna’s existing Responses termination metadata reports `{"completed":1736}`; output-cap incompletions: **0**. This is derived from saved provider termination metadata, not from validity labels. The two APIs expose different termination fields.

