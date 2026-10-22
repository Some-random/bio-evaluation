# Remaining evaluation work

Updated **2026-10-21T21:57:40.700441-07:00** (America/Los_Angeles).

[Evaluation results, release years and complete questions](RESULTS_AND_REMAINING_WORK.md)

This is the main work tracker: what remains, why, and who owns the next action. A scored subset can appear in the results document while its wider evaluation remains here. Preparation and saved responses do not count as benchmark scores.

| Evaluation | Status | Owner | Verified progress | Exactly what remains / blocker |
|---|---|---|---|---|
| LAB-Bench / ProtocolQA | Held after interrupted review | Coordinator / provider restriction | ProtocolQA review checkpoint preserved. | Resolution of the interrupted scope; do not retry or reroute it. |
| Beta-lactamase activity — PEER | Endpoint not admitted | Coordinator | Source and synthetic checks exist; native cases unexecuted. | Native task predicts antibiotic-resistance enzyme variant activity; this performance-prediction endpoint is not admitted. |
| AAV variant fitness — FLIP | Endpoint held | Coordinator | Archive/source audit complete; source is available. | Native task predicts engineered viral-capsid packaging viability. Endpoint remains held; missing downloads are not the blocker. |
| GO biological process — DeepFRI split | Generating | Coordinator / existing DeepFRI worker | 1,168/3,416 responses saved at 21:26 PDT. | Finish unchanged generation, seal all outcomes, then native AP/Fmax scoring. |
| GO cellular component — DeepFRI split | Generation complete; scoring pending | Coordinator / existing DeepFRI worker | 3,416/3,416 responses saved and terminal; no score artifact at check. | Run the existing once-only native scorer after its runtime/scoring gate; then publish. |
| ProteinGym DMS substitution benchmark | Generating | ProteinGym owner | 25,279/59,581 outputs delivered at 21:54 PDT for the reviewed 30-assay condition. | Finish outputs, native scoring and publication; remaining assays require separate eligibility/input work. |
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
| NatureLM unconditional generation | Generating | Unconditional-generation owner | 35/1,000 outcomes saved at the latest owner observation; unsealed. | Finish generation, eligible folding, scoring, final audit and publication. Separate one-time publication mechanism still needs coordinator review. |
| NatureLM stability/solubility-conditioned generation | Available condition complete; native equivalence unavailable | Coordinator / source recovery | All 30 generations and substitute proxy scores published. | No execution remains for this condition. Native cohort/evaluator and matched controls are unavailable; short strings limit biological interpretation. |
| NatureLM heme-binding case study | Qualitative case finished; native evaluation unavailable | Coordinator / source recovery | One sequence and five predicted complexes published, all with severe clashes. | Original author cases/settings and binding measurements are required for a native binding score; no further declared run is pending. |
| RAbD CDR-H3 redesign | 38/60 cases scored | Coordinator / remaining input review | Current-coordinate backbone adaptation published. | 22 cases remain outside the evaluated condition; scope review and historical coordinate/protocol provenance are separate remaining requirements. |
| Proteo-R1 all-CDR SAbDab holdout | Released demonstrations finished; paper holdout unavailable | Coordinator / source recovery | All three demonstrations scored and published; GPU released. | Exact paper holdout and structural Loop-RMSD/IMP scorer remain unavailable. No execution remains for the adopted three-case condition. |
| BioReason-Pro explanation assessment | 12 cases scored; full release unfinished | BioReason-Pro owner / coordinator | Reviewed 12-case local solver/judge result published. | 8,618 source cases remain unreviewed; wider permitted inputs need independent review and a frozen condition. Exact native judging differs. |
| Ryze extraction component tests | Model delivery passed; input review unfinished | SlideVQA owner / independent reviewers | Four actual 20-image delivery probes passed; first 200 decks cover 1,047 input-reviewed cases. | Review remaining 200 decks /1,168 cases, reconcile global holds and flagged context, freeze/admit the full condition, then generate and score. |
| LABBench2 (2026) | CPU preparation complete | Coordinator / LABBench2 lane | All 1,211 inputs audited; 36 independent checks; isolated package sealed. | New-suite dispatch authority and actual 128K/52-image/local-judge delivery gates before any benchmark run. |
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
