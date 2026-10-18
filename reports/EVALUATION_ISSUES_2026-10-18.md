# Evaluation checks and issues found

Prepared October 18, 2026, 12:04 PM PDT; live host snapshots 12:03:58 PM–12:04:03 PM UTC-07:00. This technical report records operational checks, output failures and benchmark limitations separately from the advisor-facing task map.

**Live checks are automatic, but they do not verify biological correctness.** Every 60 seconds the health monitors verify the frozen model/server/GPU identity, request queues, cache usage, token progress, response hashes, HTTP status, token-limit finishes and empty final fields. Busy endpoints with no observed token progress for 10 minutes are flagged. Health checks are read-only and record warnings; they do not restart servers or alter prompts, sampling or output budgets.

The actual dispatcher checks each returned request. A transport/server error, malformed response envelope or infrastructure exception stops new dispatch on that host, while active requests drain and receipts remain saved. Failed or ambiguous calls are not silently retried. Successful HTTP responses that reach the output limit or have an empty final field continue under the frozen protocol. The native scoring watcher checks every 20 seconds and starts each unchanged scorer only after all required generation sources close. Scoring/provenance errors are recorded without an automatic retry. The operational monitor does not judge answer correctness or reasoning.

**All eight endpoints were healthy and progressing. Across 13,324 checked shared responses, there were zero saved transport/server errors, 7,962 token-limit finishes (59.8%), and 5,906 empty final-answer fields (44.3%).**

| Dataset in currently selected runs | Shared responses checked | Reached 4,096-token cap | Empty final-answer field |
|---|---:|---:|---:|
| P07 TAPE GFP fluorescence | 818 | 788 (96.3%) | 791 (96.7%) |
| P08 TAPE protein stability | 3,804 | 5 (0.1%) | 6 (0.2%) |
| P12 DeepFRI enzyme classification | 393 | 202 (51.4%) | 194 (49.4%) |
| P13 DeepFRI GO biological process | 400 | 78 (19.5%) | 67 (16.8%) |
| P14 DeepFRI GO molecular function | 423 | 77 (18.2%) | 74 (17.5%) |
| P15 DeepFRI GO cellular component | 426 | 21 (4.9%) | 16 (3.8%) |
| P16 ProtST reaction classification | 1,144 | 911 (79.6%) | 906 (79.2%) |
| P28 BioReason-Pro temporal protein function | 2,132 | 2,107 (98.8%) | 736 (34.5%) |
| P29 Bio-posttrain protein function, ID/OOD | 3,784 | 3,773 (99.7%) | 3,116 (82.3%) |

These are **37 selected runs**, with 44,977 planned cases, within the larger 83,690-case campaign. They are not complete dataset denominators. The monitor checked shared-dispatch responses from both the previous and upgraded pools; this table does not isolate vLLM 0.32 or concurrency 64. Another 2,953 older saved responses in these runs lack shared-dispatch metadata and are outside this format scan. Empty final means the final content field is blank; reasoning may still be saved separately. A cap hit can still contain a usable final answer. These checks do not compute native parser success or correctness.

The largest ongoing issue is the fixed response budget/output contract: fluorescence, protein reaction classification and the GO tasks often reach the cap, while the selected stability runs rarely do. The full 4,096-token recipe remains frozen, failures remain counted, and no longer-budget run is implied by this report. The historical LAB-Bench cloning run likewise had 33/33 cap hits and no parsed answer. DeepSol solubility had 1,069 invalid outputs out of 1,999; FLIP Meltome had 12 unparsed numeric outputs out of 1,366, leaving its full primary correlation undefined. These historical scores are distinct from today's partial live scan. [Historical results and original score links](RESULTS_AT_A_GLANCE.md), [count records](RESULTS_GROUPED.md).

**Two benchmark measurement issues materially affect interpretation.**

* **BioReason DNA variant-effect scoring (N02/N03):** the released evaluator can credit a target word anywhere in the generated continuation, including reasoning. The saved N03 run scored 89.00% by that native rule over 873 cases while producing zero valid strict final labels; N02 similarly scored 49.07% natively over 1,233 cases with zero valid strict final labels. Native and strict diagnostics stay separate. The native headline cannot establish a clean final classification success rate. [Input/scorer audit](GENOMIC_NATIVE_INPUT_AUDIT_2026-10-15.md), [stored native and strict results](LOCAL_SUITE_RESULTS.md).
* **Bio-posttrain protein-function targets (P29):** the native target includes predictor-derived GO terms while predictor GO annotations are supplied in the input. An offline input-predictor-only baseline achieves native propagated mean F1 of 98.42% on 6,989 ID cases and 98.94% on 7,883 OOD cases. Those are input/reference dependence measurements, not Qwen scores. The score can reward reproducing supplied predictions; high native performance does not isolate new biological inference. Original native scoring and a separate curated-only diagnostic remain recorded, and curated references also overlap input predictions. [Native target construction and overlap audit](POSTTRAIN_NATIVE_GAP_AUDIT.md).

**Concrete pipeline faults were found and fixed.**

* **Premature stability scoring:** our old shutdown helper allowed three P08 shard wrappers to score partial generation. The corrected drain controls the executor parent before draining, and current scoring waits for full source closure. Original partial records remain immutable; separate continuation folders preserve provenance without double-counting. [Shared execution report](SHARED_VLLM_EXECUTION_2026-10-17.md).
* **Missing LAB-Bench context:** earlier preparation omitted titles/DOIs for 82 SuppQA cases and protocol text for 108 ProtocolQA cases. This was corrected before local inference of the affected categories; old frozen artifacts remain preserved. ProtocolQA's separate execution hold remains. [Native input review](LABBENCH_NATIVE_INPUT_REVIEW_2026-10-15.md).

Other qualifications remain. DeepFRI's released full FASTA sequences often differ from structurally modeled residue sequences, so the Qwen full-FASTA condition is labeled an adaptation rather than exact structural-input replication. [Source audit](DEEPFRI_NATIVE_SOURCE_AUDIT_2026-10-15.md). Drug-target interaction uses continuous conditional-likelihood scores for ranking; clean outputs still produced near-chance AUROC (BindingDB 0.5036, BioSNAP 0.5336, Human 0.4747), showing that output formatting does not explain every weak result. [Stored results](RESULTS_AT_A_GLANCE.md).

The figure/table QA integrity audit checked 425 completed cases and found no local image/case mismatches, target-permutation errors, target leakage or score arithmetic discrepancies. Historical image-encoding equivalence and prior model exposure remain separate qualifications. [Vision integrity audit](labbench_vision_postrun_integrity_audit.md).

[Machine-readable snapshots, per-task counts, monitoring behavior and source hashes](EVALUATION_ISSUES_2026-10-18.json). This report launches no inference, retries, scoring or runtime changes.
