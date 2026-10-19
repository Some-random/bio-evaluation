# Evaluation repair plan

Started October 19, 2026, Pacific time. Immediate scope: repair and interpret saved outputs, then validate answer delivery on synthetic/development inputs. Existing runs and scores remain preserved.

| Work | Concrete output | Status |
|---|---|---|
| P12–P15 scorer compatibility | Separately named scoring runs accepting raw null versus normalized empty final, with the original denominator and metric rules | Implementing; original failed attempts preserved |
| P16 reaction extraction | Frozen terminal-number diagnostic beside the original score, independently checked against all saved cases | Verified 12/5,651 under the specified diagnostic; preparing reproducible export |
| P03 localization | Delivery statistics, retrospective class balance, invalid-answer upper bound and prediction concentration | Verifying saved records |
| B02 and P42 qualifications | Prominent truncation/zero-accepted-output statements in the public results table | Verified counts; prominent qualifications added |
| P01 and V01–V05 extraction | Recover hash-verified raw records; freeze conservative extraction/ambiguity rules on synthetic cases before rescoring | Blocked on unavailable original raw files; frozen extraction tools and checks ready |
| Qwen output-delivery pilot | Same checkpoint, thinking enabled, 16K output cap; synthetic inputs spanning answer formats and context lengths; saved requests/responses, latency and usage | Running 12 synthetic cases in a separate pilot |
| OpenAI request identity | One persistent end-user safety identifier, three neutral smoke tests, no previously flagged benchmark requests | Completed: one stable identifier, 3/3 neutral tests passed |

The decision table will distinguish usable-answer coverage, the native metric, separately named diagnostics, and what the evidence supports. Native non-abstention coverage will not be presented as the fraction of usable answers.

The pilot is a gate, not another scored benchmark. Its protocol and acceptance checks must be frozen before generation. A successful format-only toy test does not establish valid biological predictions. Any subsequent full rerun gets its own run ID and covers the entire declared case set; successful retries will never be spliced into old results.

Proposed full-rerun order after the pilot: **B08 cloning (33), P42 GFP design (200), B07 SeqQA (600), P16 reaction (5,651), then P07 GFP prediction (27,217)**. None of these new full reruns has started under this plan.

Next model comparisons should use identical cases, essential inputs and validated answer semantics. P03, P43, B01, B04 and B05 are the starting candidates, subject to their existing qualifications.

[Integrity audit](EVALUATION_INTEGRITY_AUDIT_2026-10-18.md) · [Current results](RESULTS_AT_A_GLANCE.md)
