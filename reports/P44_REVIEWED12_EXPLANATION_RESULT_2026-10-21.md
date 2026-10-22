# P44: reviewed 12 functional explanation assessment

The declared local Qwen judge scored all **12/12** independently reviewed human protein explanations, with an axis-macro score of **6.0167/10**. All 12 solver and 12 judge responses finished normally, with no transport errors, malformed outputs, refusals, empty finals or truncations. Four artificial delivery checks passed before these real requests.

This is the first 12 human entries in original release order, selected before generation as a prospective interface panel. It does **not** complete the 8,630-case release or reproduce the author's judged cohort; the remaining 8,618 release cases are unreviewed for this condition. The subset is not a representative random sample.

| Axis | Local score/10 | Cases |
|---|---:|---:|
| molecular function | 5.4167 | 12 |
| biological process | 4.8333 | 12 |
| cellular component | 7.1667 | 12 |
| specificity | 7.6667 | 12 |
| reliability | 5.0000 | 12 |

Qwen/Qwen3.8-27B revision 1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0 served as both candidate generator and separate local judge, using BF16 TP1, temperature 0, a 65,536-token context and prospective 16,384-token output caps. Thinking was requested disabled; observed reasoning fields were present in 0 solver and 0 judge responses. Using the same checkpoint to generate and judge explanations can bias these proxy judgments, and no independent human calibration is established.

Solver requests retain complete released amino-acid sequences and permitted organism/domain/interaction/predictor context. Recorded names, curated GO labels, function summaries and locations remain judge-only. Every candidate outcome was sealed before the runtime opened real judge dossiers; actual request/response bytes, locks and case hashes reconcile. There were no selective retries, head training or paid/OpenAI calls. P28/P29 GO scores remain unchanged.

The rubric reconstructs the five axes and evidence rule from [BioReason-Pro Methods 4.4.3 and Appendix C.3](https://www.biorxiv.org/content/10.64898/2026.03.19.712954v1.full). Specificity measures depth/utility and can reward a detailed slightly inaccurate guess; it does not validate its mechanism. Reliability is scored separately. Missing annotation is not proof of biological absence, and -1 requires reviewed silence across all evidence sources. None of these 12 cases required an absent-evidence exclusion. One released sequence/domain-coordinate inconsistency is retained without correction.

The paper reports GPT-5.1 judge means of 8.03 for BioReason-Pro RL, 7.65 for SFT and 4.15 for Prot2Text-v2. Those values use different models, representations, cohorts and judging conditions and are not numerically interchangeable with this local score. Exact original API/schema bytes, judged-ID/output manifests and aggregation code remain unrecovered; indexed primary rubric text is available. Raw sequences replace native trained protein/GO-graph representations. Public pretraining exposure is unknown; these results establish neither contamination-free evaluation nor independently verified mechanisms.

The [machine-readable result](P44_REVIEWED12_EXPLANATION_RESULT_2026-10-21.json), [exact trajectory archive](../results/trajectories/qwen38_27b_p44_human12_explanation_uniform16k_2026-10-21_v1.tar.gz) and [archive member manifest](../results/trajectories/qwen38_27b_p44_human12_explanation_uniform16k_2026-10-21_v1.tar.manifest.json) retain the complete reviewed 12 denominator, raw responses, reference isolation and source/code/grant evidence. No broader unreviewed payload, weights, runtime environments, credentials, website or schedule changes are included.
