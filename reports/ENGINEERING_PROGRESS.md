# Remaining evaluation work

Updated **2026-10-22T12:04:06.198599-07:00** (America/Los_Angeles).

[Evaluation results, release years and complete questions](RESULTS_AND_REMAINING_WORK.md)

This is the main work tracker: what remains, why, and who owns the next action. A scored subset can appear in the results document while its wider evaluation remains here. Preparation and saved responses do not count as benchmark scores.

**Current comparison: Qwen3.5-4B versus Qwen3.5-4B-Base on protein tasks and text QA.** LAB-Bench LitQA2 and SuppQA are complete and scored for both models (279 questions each). The 34 artificial runtime checks passed, but actual benchmark delivery revealed extensive 16K output exhaustion, especially for the post-trained model. Future queue submissions are paused; affected classification and LABBench2 workers are being drained between batches while current calls and all outputs are preserved. A separate author-recommended sampling correction is adopted for preparation, with actual task-shaped artificial validation and independent review required before any new full-cohort dispatch. No replacement condition or selective retry has been dispatched. The 4B LiveProteinBench and scalar-property jobs have not been submitted. The separate Qwen3.8-27B runs continue. This is a dated snapshot; task-local monitors provide newer runtime evidence. Other rows retain their stated observation times.

| Evaluation | Status | Owner | Verified progress | Exactly what remains / blocker |
|---|---|---|---|---|
| LiveProteinBench — 4B / Base comparison | Admitted; dispatch paused | LiveProteinBench owner / coordinator | 1,736 reviewed questions/model; both original queue requests have zero submission attempts and no job IDs. | Resolve the shared 16K delivery failure before releasing this cohort; preserve the admitted original condition and separately review any prospective repair. |
| PEER solubility and localization — 4B / Base | Draining after delivery failure | Classification delivery owner | At 11:55 PDT localization: Base 1,008/2,773 saved, 863 truncated empty finals; post-trained 576/2,773 saved, all 576 truncated empty. No transport errors. Solubility has not been reached by either sequential worker. | Allow active batches to finish; stop new requests, retain every attempt, diagnose sampling/template behavior using neutral inputs and freeze any prospective repair separately. No native score yet. |
| Meltome, TAPE stability and GFP fluorescence — 4B / Base | Admitted; dispatch paused | Protein properties owner / coordinator | 41,434 fixed inputs/model: 1,366 Meltome, 12,851 stability and 27,217 GFP. Both requests have zero submission attempts and no job IDs. | Resolve shared delivery failure before launching these large cohorts. No benchmark response counts or scores exist for these lanes. |
| LAB-Bench LitQA2 and SuppQA — 4B / Base | Complete and scored | LAB-Bench owner | Both 279/279 sealed. LitQA2 accuracy: Base 22.34%, post-trained 14.72%; SuppQA: 12.20%, 17.07%. Base 10 truncations; post-trained 121 truncations and 124 empty finals. | Publish independently reviewed source, native scores and complete trajectories; finished results are in the results document. Original jobs 246445/246714 completed. |
| LABBench2 BASIC text QA — 4B / Base | Draining after delivery failure | LABBench2 owner | At 11:56 PDT Base 416/542 saved, 59 truncated; post-trained at least 256/542 terminal raw outcomes, 243 truncated. No transport/HTTP errors. Both original jobs had started. | Finish active batches and stop new requests. No complete solver seals or judge score yet. Preserve author BASIC question-only inputs and the declared fixed local judge for any independently frozen continuation. |
| LiveProteinBench — Qwen3.8-27B sequence-only | Generating | LiveProteinBench owner | At 11:54 PDT 1,142/1,736 saved, 1,027 parsed, 79 truncations, no transport/HTTP/empty-final errors. Job 246368 running. | Finish this separate nonthinking sequence-only condition, seal all outcomes, score once and publish; 61 source cases remain excluded. |
| LAB-Bench / ProtocolQA | Held after interrupted review | Coordinator / provider restriction | ProtocolQA review checkpoint preserved. | Resolution of the interrupted scope; do not retry or reroute it. |
| Beta-lactamase activity — PEER | Endpoint not admitted | Coordinator | Source and synthetic checks exist; native cases unexecuted. | Native task predicts antibiotic-resistance enzyme variant activity; this performance-prediction endpoint is not admitted. |
| AAV variant fitness — FLIP | Endpoint held | Coordinator | Archive/source audit complete; source is available. | Native task predicts engineered viral-capsid packaging viability. Endpoint remains held; missing downloads are not the blocker. |
| GO biological process — DeepFRI split | Generating | Existing DeepFRI worker / coordinator | At 11:50 PDT 1,696/3,416 saved; no recorded delivery errors or truncations. Existing successor job 243499 running. | Finish unchanged generation, seal all outcomes and run native AP/Fmax scoring. |
| GO cellular component — DeepFRI split | Complete and scored | Coordinator / independent reviewer | All 3,416 parsed; native AUPRC 0.03705706, Fmax 0.07158192. No delivery failures. | Publish source, complete trajectories and native scores. The launch-only scoring repair is complete; original failure log preserved. |
| ProteinGym DMS substitution benchmark | Reviewed 30-assay condition scored and published | ProteinGym owner | 59,581/59,581 outputs; native mean Spearman −0.01406667 across 30/217 assays. Report and complete trajectories are published and byte-verified. | The other 187 assays remain unadmitted; no full 217-assay completion is claimed. |
| PG-LLM / ProteinGym-LLM ranking | Held after rejected/interrupted work | Coordinator / provider restriction | Prior rejected traffic and review evidence preserved. | Applicable scope/provider resolution; no retries, relabeling or rerouting. |
| PFArena T1: single-mutant generation | 43 assays scored; full panel unfinished | PFArena T1 owner | 34 original and nine additional assays scored and published as separate conditions. | 67 assays remain unadmitted; 12 held and one outside this condition. Two further input proposals need a separate scientific decision. |
| PFArena T2: measurement-free multi-mutant ranking | Held after interrupted preparation | Coordinator / provider restriction | Preparation checkpoint preserved. | Resolve the interrupted scope before continuation; exact trigger is unknown. |
| PFArena T3: anchor-informed ranking | 13 assays scored; full panel unfinished | PFArena T3 owner | Eight original and five additional assays scored and published separately. | 54/67 assays remain input-unreviewed; prepare and independently review permitted inputs before another condition. |
| PFArena T4: single-mutant-informed ranking | Four scored; extension stopped | Coordinator / stopped extension | Four-assay V2 result preserved; new eight-assay preparation encountered a biological-risk interruption. | Preserve checkpoints; no retry or reroute of the interrupted extension. Do not infer the exact trigger. |
| NatureLM protein description | Independent cohort finished; native holdout unavailable | Coordinator / source recovery | Independent nine-record description result published. | Exact original accessions, dated annotation snapshot and ROUGE preprocessing are needed for native paper reproduction. |
| MutaDescribe mutation explanation | Held after interrupted review | Coordinator / provider restriction | MutaDescribe source files are available. | The interrupted biological-content review remains stopped; file availability does not resolve it. |
| MutaDescribe mutation engineering — position supplied | Held after interrupted review | Coordinator / provider restriction | MutaDescribe source files are available. | Same interrupted-review boundary; do not reopen through another worker or setting. |
| MutaDescribe mutation engineering — position unknown | Held after interrupted review | Coordinator / provider restriction | MutaDescribe source files are available. | Same interrupted-review boundary; no native run is currently admitted. |
| MutaPLM low-N fitness regression | Excluded by user: no new head training | Coordinator | Existing-head/source audit only. | A released matching head and exact split would be needed; no new head training will be undertaken. |
| MutaPLM iterative sequence optimization | Five landscapes finished; sixth held | Coordinator / retained hold | Five-landscape surrogate result published. | No execution remains for the five-landscape condition. The held sixth is excluded from a full six-landscape claim. |
| BioT5+ description-guided protein design | Partial archive; extension held | Coordinator / provider restriction | 59 archived responses preserved; no full benchmark score. | Preserve interrupted review; recover permitted alignment/native-metric metadata without restarting the extension. |
| NatureLM unconditional generation | Generating | Unconditional-generation owner | At 11:49 PDT 622/1,000 outcomes saved; no recorded truncations, empty finals or transport errors. | Finish unchanged generation, eligible folding, scoring, final audit and publication. |
| NatureLM stability/solubility-conditioned generation | Available condition complete; native equivalence unavailable | Coordinator / source recovery | All 30 generations and substitute proxy scores published. | No execution remains for this condition. Native cohort/evaluator and matched controls are unavailable; short strings limit biological interpretation. |
| NatureLM heme-binding case study | Qualitative case finished; native evaluation unavailable | Coordinator / source recovery | One sequence and five predicted complexes published, all with severe clashes. | Original author cases/settings and binding measurements are required for a native binding score; no further declared run is pending. |
| RAbD CDR-H3 redesign | 38/60 cases scored | Coordinator / remaining input review | Current-coordinate backbone adaptation published. | 22 cases remain outside the evaluated condition; scope review and historical coordinate/protocol provenance are separate remaining requirements. |
| Proteo-R1 all-CDR SAbDab holdout | Released demonstrations finished; paper holdout unavailable | Coordinator / source recovery | All three demonstrations scored and published; GPU released. | Exact paper holdout and structural Loop-RMSD/IMP scorer remain unavailable. No execution remains for the adopted three-case condition. |
| BioReason-Pro explanation assessment | 12 cases scored; full release unfinished | BioReason-Pro owner / coordinator | Reviewed 12-case local solver/judge result published. | 8,618 source cases remain unreviewed; wider permitted inputs need independent review and a frozen condition. Exact native judging differs. |
| SlideVQA full-deck question answering | Generating | SlideVQA owner | At 11:56 PDT 1,896/2,215 saved; 1,890 valid, six preserved truncated empty finals. No transport/HTTP errors. Job 245973 running. | Finish all 2,215 once-only outcomes, seal, run native scoring and publish. Original historical image-encoding qualifications remain. |
| LABBench2 — remaining modalities and conditions (2026) | Preparation only beyond selected BASIC text QA | LABBench2 owner | The selected 542-case BASIC text comparison is tracked above. The wider package includes additional inputs and image/tool conditions. | Wider multimodal or tool conditions require separate scope and actual delivery checks; they are not part of the current matched text-only dispatch. |
| GeneBench-Pro (2026; public 10) | CPU preparation complete | Coordinator / GeneBench-Pro lane | Portable environment and concurrent once-only recording/scorer harness independently accepted; no real analysis/model calls. | New-suite dispatch authority and actual model/tool delivery; then the declared public-ten run and native grading. |
| BiomniBench-DA (2026; public 50) | Finishing CPU runtime validation | BiomniBench-DA owner | 410 source objects and 50 workspaces verified; Python/R confinement prepared. | Seal final repaired R environment and CPU checks; then independent runtime acceptance. New-suite inference/judge dispatch is not authorized. |
| BixBench3 (2026) | Restricted CPU preparation complete | Coordinator / BixBench3 lane | Recording/scoring/quota guards accepted. Original validation44/45; separate R script-file validation passed. | Review remaining 19 cases; enforce R file-only execution; validate real-case storage/resources and obtain new-suite dispatch authority. |
| scBench (2026; public six) | Deferred by user | Deferred | Public task definitions and deterministic grader preserved. | Required Latch access is unavailable; no further credential request or attempt is pending. |

<details>
<summary>Worker assignments and recent handoffs</summary>

Capacity is 16 workers plus the coordinator; at most eight project GPUs may be requested. A worker finishing a bounded review or CPU package is explicitly reassigned or continues its evaluation. Thread names may retain an earlier task name.

Worker details below were last reconciled at 2026-10-21T21:15:15.022082-07:00; the evaluation table above supersedes older task stages.

| Worker | Assigned role |
|---|---|
| /root/liveprotein_execution | LiveProteinBench sequence-only execution through scoring and publication |
| /root/p17_execution | ProteinGym substitutions |
| /root/p19_remaining_review | PFArena T1 single-mutant generation |
| /root/p21_remaining_review | PFArena T3 anchor-informed ranking |
| /root/p22_remaining_review | Stopped after biological-risk interruption; no reassignment of interrupted action |
| /root/p37_delivery | NatureLM unconditional generation |
| /root/p38_generation | NatureLM conditional generation |
| /root/p41_structure | Proteo-R1 structural demonstration |
| /root/p44_explanation | BioReason-Pro explanations |
| /root/v07_execution | SlideVQA |
| /root/new2026_biomni | BiomniBench-DA |
| /root/new2026_bixbench | BixBench3 |
| /root/v07_execution/v07_runtime_audit | GeneBench-Pro |
| /root/new2026_labbench2 | LABBench2 |
| /root/independent_review | Independent review coordination |
| /root/independent_review/v07_question_prefilter_b | BixBench3 independent technical review |
| /root/p19_remaining_review/metadata_provenance_audit/stability9_peer_check | PFArena T1 independent technical review |
| /root/p05_scope | PFArena T3 / SlideVQA independent review |

Recent handoffs:

- `/root/p05_scope`: FLIP metadata/scope audit, then Proteo-R1 input audit, then PFArena T3 technical admission → SlideVQA exact deck partition.
- `/root/independent_review/v07_question_prefilter_b`: SlideVQA 50-deck full-content review / 242 cases → BixBench3 independent technical review.
- `/root/v07_execution/v07_runtime_audit`: V07 bounded runtime/scorer guard audit → GeneBench-Pro portable CPU/recording preparation.
- `/root/new2026_labbench2`: LABBench2 authorized CPU preparation → BiomniBench-DA independent technical review.
- `/root/p19_remaining_review`: Nine-case input/provenance review milestone → Own separate nine-case execution preparation through closure.
- `/root/p22_remaining_review`: No normal completion: biological-risk interruption → No retry or handoff of the interrupted action.

</details>

Snapshot only; websites and recurring updates remain disabled. Existing biological holds, no-new-head-training and no-paid/OpenAI-benchmark-call restrictions remain. Technical run reports, source records and trajectories support these two main documents.

**Reading the PFArena results:** The 34- and 9-assay T1 rows are two completed, disjoint subsets of the same 123-assay benchmark (43 evaluated; 80 unevaluated). The eight- and five-assay T3 rows likewise cover 13 of 67 assays. Separate scores preserve each fixed cohort; they are not a pooled benchmark score. These completed subset jobs are terminal; further assay review is unfinished.
