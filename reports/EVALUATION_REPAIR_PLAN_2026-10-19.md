# Evaluation repair plan

Started October 19, 2026, Pacific time. Immediate scope: repair and interpret saved outputs, then validate answer delivery on synthetic/development inputs. Existing runs and scores remain preserved.

The catalog contains **64 evaluation settings**, with **57 retained in the main view** and seven BioReason-family settings archived. The seven settings in the final overnight continuation (P07, P08, P12–P16) were only the last active batch. Its 17,145 newly generated responses do not represent the full catalog or a uniform-budget rerun. See the [complete decision table](EVALUATION_DECISION_TABLE.md) for every retained setting and its evidence status.

| Work | Concrete output | Status |
|---|---|---|
| P12–P15 scorer compatibility | Separately named scoring runs accepting raw null versus normalized empty final, with the original denominator and metric rules | [All four completed and published; P13 recovery finished October 19 at 4:33 AM PDT. Original failures are preserved. Full AP/Fmax remain undefined because invalid confidence vectors remain](SCORER_COMPATIBILITY_REPAIR_2026-10-19.md) |
| P16 reaction extraction | Frozen terminal-number diagnostic beside the original score, independently checked against all saved cases | Done: [12/5,651 versus original 9/5,651, with reproducible export](REACTION_EXTRACTION_DIAGNOSTIC_2026-10-19.md) |
| P03 localization and P43 interactions | Delivery statistics, retrospective class balance, invalid-answer upper bound, prediction concentration and likelihood-interface check | [Verified: P03 stays below its descriptive majority reference even if every invalid answer is recovered correctly](PREDICTION_TASK_AUDIT_2026-10-19.md) |
| B02 and P42 qualifications | Prominent truncation/zero-accepted-output statements in the public results table | Verified counts; prominent qualifications added |
| P01 and V01–V05 extraction | Recover hash-verified raw records; freeze conservative extraction/ambiguity rules on synthetic cases before rescoring | [Blocked on unavailable original raw files; frozen tools and 18 checks ready](HISTORICAL_EXTRACTION_STATUS_2026-10-19.md) |
| Qwen output-delivery pilot | Same checkpoint, thinking enabled, 16K output cap; synthetic inputs spanning answer formats and context lengths; saved requests/responses, latency and usage | [Completed: 12/12 synthetic checks passed, zero truncated or empty finals](OUTPUT_DELIVERY_PILOT_2026-10-19.md) |
| OpenAI request identity | One persistent end-user safety identifier, three neutral smoke tests, no previously flagged benchmark requests | [Completed: one stable identifier, 3/3 neutral tests passed](OPENAI_SAFETY_IDENTIFIER_CHECK_2026-10-19.md) |

The [decision table](EVALUATION_DECISION_TABLE.md) distinguishes usable-answer coverage, the native metric, separately named diagnostics, and what the evidence supports. Native non-abstention coverage is not presented as the fraction of usable answers.

The pilot is an interface check, not another scored benchmark. Its protocol and acceptance checks were frozen before generation. Passing these simple synthetic cases shows that the tested formats and long inputs can work; it does not establish reliable delivery on difficult biological questions. Real permitted-development validation is still needed before treating the full-rerun configuration as settled. Any subsequent full rerun gets its own run ID and covers the entire declared case set; successful retries will never be spliced into old results.

Proposed full-rerun order after the pilot: **B08 cloning (33), P42 GFP design (200), B07 SeqQA (600), P16 reaction (5,651), then P07 GFP prediction (27,217)**. None of these new full reruns has started under this plan.

Next model comparisons should use identical cases, essential inputs and validated answer semantics. P03, P43, B01, B04 and B05 are the starting candidates, subject to their existing qualifications.

[Integrity audit](EVALUATION_INTEGRITY_AUDIT_2026-10-18.md) · [Current results](RESULTS_AT_A_GLANCE.md)
