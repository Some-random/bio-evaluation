# Qwen/GPT results and exact remaining work

Assembled **2026-10-20T14:12:31.732426-07:00**, America/Los_Angeles. Source-specific verification times are preserved below.

**28 of 57 retained settings have a defined score for a declared evaluated condition.** The other settings comprise four running/queued conditions, 15 agent-owned preparation/implementation tasks, three user-held exceptions and seven biological/provider-held settings. This does not claim that all 28 reproduce the original papers.

- [GPT models versus matched Qwen baselines](#gpt-models-and-matched-archived-qwen-results)
- [All 28 scored Qwen settings, with separate run conditions](#qwen-results-for-the-28-settings-with-a-defined-metric)
- [Exact remaining work for the 15 agent-owned tasks](#the-15-agent-owned-tasks-exact-remaining-work)
- [Source provenance](#source-provenance-appendix)

[Machine-readable metrics and source hashes](RESULTS_AND_REMAINING_WORK.sources.json).

## How to read the results

GPT results are available for **B01, B03 and P03 only** in the verified project benchmark comparison. No comparable GPT score is verified for the other 25 scored Qwen settings; that is not a score of zero or proof that no historical request was ever attempted. Earlier GPT-4o paper numbers are external literature results, not runs performed here.

A score of zero is shown when the recorded scorer produced zero. An undefined metric is shown as undefined. Original runs, replays, new delivery conditions and offline diagnostics are kept separate. No best-run selection or cross-task average is used. Higher is better for the displayed accuracies, correlations, AUROC/AUPRC and ROUGE measures, but their numerical scales and scientific meanings differ.

The latest local progress and task ownership are in the [57-setting tracker](CATALOG_STATUS.md). This document is a dated results and remaining-work report, not a live execution monitor.

## GPT models and matched archived Qwen results

Verified 2026-10-20 02:10 PM PDT from sealed scores and the comparison monitor. Three sealed condition files cover five GPT task/model scores; saved responses alone are not scores.

| Task | Model | Native correct / all | Native accuracy | Strict correct / all | Strict accuracy |
|---|---|---:|---:|---:|---:|
| B01 LitQA2 | Qwen3.8-27B (archived 4K) | 77/197 | 39.09% | 77/197 | 39.09% |
| B01 LitQA2 | gpt-6-luna | 97/197 | 49.24% | 97/197 | 49.24% |
| B01 LitQA2 | gpt-6.1-sol | 112/197 | 56.85% | 112/197 | 56.85% |
| B03 SuppQA | Qwen3.8-27B (archived 4K) | 31/82 | 37.80% | 31/82 | 37.80% |
| B03 SuppQA | gpt-6-luna | 44/82 | 53.66% | 44/82 | 53.66% |
| B03 SuppQA | gpt-6.1-sol | 46/82 | 56.10% | 46/82 | 56.10% |
| P03 localization | Qwen3.8-27B (archived 4K) | 724/2,773 | 26.11% | 724/2,773 | 26.11% |
| P03 localization | gpt-6-luna | 1,575/2,773 | 56.80% | 1,575/2,773 | 56.80% |

Native and strict scores agree in all rows. Luna improves over its matched Qwen baseline by **10.15 percentage points on B01, 15.85 on B03, and 30.69 on P03**; Sol improves by **17.77 points on B01 and 18.29 on B03**. These are within-cohort comparisons, without an overall pooled score.

QA delivered 279/279 responses for each GPT model with no recorded errors, truncations, empty finals or refusals. Luna P03 delivered **2,770/2,773 responses**; its three transport failures remain in the denominator. Archived Qwen P03 has 51 empty finals, including 47 truncated outputs, with no recorded transport/server failures.

**GPT-6.1 Sol P03 has no verified benchmark result:** it is prepared without a runtime record, and continued model scope is Luna only. The four separate 12-case development panels (48 delivered responses) passed delivery checks but did not score biological correctness.

The comparison uses the exact archived **October 16 Qwen 4K runs**, with equal ordered case cohorts and preserved original prompts/choice order. It does not use newer 16K Qwen results or the October 20 regeneration conditions. B01 contains 197 permitted public cases, B03 contains 82 public cases supplied with title/DOI but no paper or retrieval, and P03 contains 2,773 complete-sequence ten-class cases. Equal token caps do not establish equal reasoning compute; training exposure and explanation faithfulness remain unknown.

Sealed score sources:

- [gpt-6-luna — B01, B03](https://github.com/Some-random/bio-evaluation/blob/main/results/comparison_execution/openai_qwen_2026-10-19/analysis/publicqa_gpt-6-luna.scores.json)
- [gpt-6.1-sol — B01, B03](https://github.com/Some-random/bio-evaluation/blob/main/results/comparison_execution/openai_qwen_2026-10-19/analysis/publicqa_gpt-6_1-sol.scores.json)
- [gpt-6-luna — P03](https://github.com/Some-random/bio-evaluation/blob/main/results/comparison_execution/openai_qwen_2026-10-19/analysis/localization_gpt-6-luna.scores.json)

The companion JSON records the original score, plan, protocol, request-file and prediction-lock paths/hashes, cohort checks, detailed delivery metrics and paired analyses. Earlier GPT-4o numbers in repository comparison tables are **external paper results**, not verified completed project runs. No additional scored GPT project runs were found in the checked 123-run local suite report.

## Qwen results for the 28 settings with a defined metric

Captured October 20, 2026, 02:10 PM PDT. There are **28 settings and 35 separately reported primary conditions** below. Original runs, replays, datasets and generation regimes remain separate; no best-run selection or cross-setting average is used.

“Native” describes the recorded metric formula and cohort, not reproduction of a specialist trained model. These are Qwen3.8-27B zero-shot adaptations. **P09 is an offline derived adaptation**, not new generation or verified native NatureLM labels. **P42 reports a qualified oracle endpoint**, with native novelty withheld.

**Evidence:** **V** = available score bytes were hash-verified in this audit; **A** = retained published aggregate, while the named loose score file is currently unavailable locally and in the verified public tree. Neither symbol claims that raw trajectories were re-reviewed. Exact paths and hashes are listed below and in the companion JSON.

| Setting | Condition and scope | Parser-valid / planned† | Qwen result (all reported primary metrics) | Evidence |
|---|---|---:|---|---|
| B01 — LAB-Bench / LitQA2 | Original 15 Oct; 4K; reviewed public subset; 2 held | 197/197 | 77/197 correct; accuracy 39.09%; precision 40.96%; coverage 95.43% | A; Q16 |
| B01 — LAB-Bench / LitQA2 | 16 Oct replay; 4K; reviewed public subset; 2 held | 197/197 | 77/197 correct; accuracy 39.09%; precision 40.96%; coverage 95.43% | V; Q17 |
| B02 — LAB-Bench / DbQA | Original 15 Oct; 4K; reviewed public subset | 427/520 | 163/520 correct; accuracy 31.35%; precision 31.84%; coverage 98.46% | A; Q18 |
| B03 — LAB-Bench / SuppQA | Original 15 Oct; 4K; reviewed public subset | 82/82 | 28/82 correct; accuracy 34.15%; precision 35.90%; coverage 95.12% | A; Q19 |
| B03 — LAB-Bench / SuppQA | 16 Oct replay; 4K; reviewed public subset | 82/82 | 31/82 correct; accuracy 37.80%; precision 39.24%; coverage 96.34% | V; Q20 |
| B04 — LAB-Bench / FigQA | Original 15 Oct; 4K; reviewed public subset | 180/181 | 137/181 correct; accuracy 75.69%; precision 76.97%; coverage 98.34% | A; Q21 |
| B04 — LAB-Bench / FigQA | 16 Oct replay; 4K; reviewed public subset | 180/181 | 131/181 correct; accuracy 72.38%; precision 72.78%; coverage 99.45% | V; Q22 |
| B05 — LAB-Bench / TableQA | Original 15 Oct; 4K; reviewed public subset | 238/244 | 216/244 correct; accuracy 88.52%; precision 90.00%; coverage 98.36% | A; Q23 |
| B05 — LAB-Bench / TableQA | 16 Oct replay; 4K; reviewed public subset | 236/244 | 215/244 correct; accuracy 88.11%; precision 89.96%; coverage 97.95% | V; Q24 |
| B07 — LAB-Bench / SeqQA | Original 15 Oct; 4K; reviewed public subset | 86/600 | 76/600 correct; accuracy 12.67%; precision 12.77%; coverage 99.17% | A; Q25 |
| B08 — LAB-Bench / Cloning scenarios | Original 15 Oct; 4K; reviewed public subset | 0/33 | 0/33 correct; accuracy 0.00%; precision 0.00%; coverage 100.00% | A; Q26 |
| P01 — Solubility — PEER | Original 15 Oct; 4,096 output tokens; full frozen reviewed case set | 930/1,999 | 484/1,999 correct; accuracy 24.21% | A; Q01 |
| P02 — Binary localization — DeepLoc/PEER | Original 15 Oct; 4,096 output tokens; full frozen reviewed case set | 1,496/1,749 | 479/1,749 correct; accuracy 27.39% | A; Q02 |
| P03 — Subcellular localization — DeepLoc | Archived full-test run; 4,096 output tokens; released 2,773-case cohort | 2,722/2,773 | 724/2,773 correct; accuracy 26.11% | V; Q03 |
| P06 — Thermostability — FLIP/Meltome | New 20 Oct; nonthinking constrained scalar; 256 tokens; same full released cohort | 1,366/1,366 | spearman 0.00368 | V; Q04 |
| P07 — GFP fluorescence — TAPE | New 20 Oct; nonthinking constrained scalar; 256 tokens; same full released cohort | 27,217/27,217 | spearman 0.029998 | V; Q05 |
| P08 — Protein stability regression — TAPE | New 20 Oct; nonthinking constrained scalar; 256 tokens; same full released cohort | 12,851/12,851 | spearman 0.226982 | V; Q06 |
| P09 — Stability classification — NatureLM/PEER | Derived from sealed new P08; no extra generation; released 12,851-case adaptation | 12,851/12,851 | 6,848/12,851 correct; accuracy 53.28768% | V; Q07 |
| P10 — Human protein–protein interaction — PEER | Original 15 Oct; 4,096 output tokens; full frozen reviewed case set | 229/237 | 119/237 correct; accuracy 50.21% | A; Q08 |
| P11 — Yeast protein–protein interaction — PEER | Original 15 Oct; 4,096 output tokens; full frozen reviewed case set | 365/394 | 178/394 correct; accuracy 45.18% | A; Q09 |
| P16 — Reaction class — zero-/few-shot | Historical mixed 4K/16K continuation; 4,096 × 4,419; 16,384 × 1,232 (mixed) output tokens; full frozen reviewed ProtST Reaction test | 1,120/5,651 | 9/5,651 correct; accuracy 0.16% | V; Q10 |
| P23 — Mol-Instructions: Protein function generation | Original 15 Oct; 4,096 output tokens; full frozen reviewed BioT5 export test | 3,494/3,494 | rouge1 0.063107; rouge2 0.013863; rougeL 0.043148; rougeLsum 0.05416 | A; Q12 |
| P24 — Mol-Instructions: Catalytic activity generation | Original 15 Oct; 4,096 output tokens; full frozen reviewed BioT5 export test | 1,601/1,601 | rouge1 0.054093; rouge2 0.013951; rougeL 0.039649; rougeLsum 0.047278 | A; Q13 |
| P25 — Mol-Instructions: Domain and motif generation | Original 15 Oct; 4,096 output tokens; full frozen reviewed BioT5 export test | 1,400/1,400 | rouge1 0.03543; rouge2 0.004749; rougeL 0.025868; rougeLsum 0.030632 | A; Q14 |
| P26 — Mol-Instructions: Functional description generation | Original 15 Oct; 4,096 output tokens; full frozen reviewed BioT5 export test | 2,633/2,633 | rouge1 0.080025; rouge2 0.012323; rougeL 0.049423; rougeLsum 0.064936 | A; Q15 |
| P42 — STRIDE GFP generated-candidate evaluation | Insert/delete/replace; archived 1,024-token condition; 100 slots/regime | 100/regime; parser-valid per regime unreported (0/200 combined) | qualified_oracle_success 0.00%; improved_sequence_uniqueness undefined; native_novelty undefined | A; Q27 |
| P42 — STRIDE GFP generated-candidate evaluation | Replace-only; archived 1,024-token condition; 100 slots/regime | 100/regime; parser-valid per regime unreported (0/200 combined) | qualified_oracle_success 0.00%; improved_sequence_uniqueness undefined; native_novelty undefined | A; Q28 |
| P43 — Drug–target interaction — BioSNAP/Human/BindingDB | bindingdb; one-token conditional likelihood; full dataset | 9,840/9,840 | auroc 0.503569; auprc 0.410315 | A; Q36 |
| P43 — Drug–target interaction — BioSNAP/Human/BindingDB | biosnap; one-token conditional likelihood; full dataset | 5,493/5,493 | auroc 0.533563; auprc 0.52166 | A; Q37 |
| P43 — Drug–target interaction — BioSNAP/Human/BindingDB | human; one-token conditional likelihood; full dataset | 1,200/1,200 | auroc 0.474719; auprc 0.419426 | A; Q38 |
| V01 — VQA-RAD | Original 15 Oct; 4,096 output tokens; full native test | 451/451 nonempty (not answer validity) | open_token_recall 0.595404; closed_accuracy 86.76% | A; Q29 |
| V02 — SLAKE — English | Original 15 Oct; 4,096 output tokens; full native test | 1,060/1,061 nonempty (not answer validity) | open_token_recall 0.509797; closed_accuracy 84.62% | A; Q30 |
| V03 — PathVQA | Original 15 Oct; 4K; released 6,719-case mirror | 6,718/6,719 nonempty (not answer validity) | open_token_recall 0.26377; closed_accuracy_corrected 85.87% | A; Q31 |
| V04 — ImageCLEF-VQA 2019 | Original 15 Oct; 4K; original test500; qualified whole-final exact match | 500/500 nonempty (not answer validity) | strict_accuracy 0.00% | A; Q32 |
| V05 — PMC-VQA held-out evaluation | Original 15 Oct; 4K; clean2,000; native | 1,990/2,000 nonempty (not answer validity) | native_td_final_character_accuracy 2.00% | A; Q33 |

† For V01–V05, the available count is **nonempty text**, not validated answers. P42 counts are explicitly separated: 100 planned per regime; 0 parser-valid outputs across the combined 200. LAB-Bench native abstention coverage differs from parser-valid delivery, so B08 can have 100% native coverage and 0/33 valid extracted answers.

Native scores retain all declared cases under their recorded policies. The 4K description runs P23–P26 include truncated nonempty responses that the ROUGE scorer still processes. For P43, a one-token length finish is expected and is not evidence of a failed likelihood request.

### Separate extraction diagnostics — same saved outputs, not replacement primary scores

| Setting | Diagnostic | Result | Evidence |
|---|---|---|---|
| P16 | Offline terminal-class extraction; same mixed 4K/16K cohort | accuracy 0.21% | V; Q11 |
| V05 | Offline full-text similarity extraction; original run | adapted_full_text_closest_choice_accuracy 49.75%; adapted_full_text_released_label_accuracy 49.75% | A; Q34 |
| V05 | Offline strict final-label extraction; original run | strict_final_label_accuracy 0.70% | A; Q35 |

### Earlier scalar runs with undefined full metrics

New P06/P07/P08 conditions did not overwrite these original results. Parsed-only correlations below are incomplete diagnostics, not full benchmark scores.

| Setting | Earlier condition | Valid / planned | Full Spearman | Parsed-only diagnostic | Evidence |
|---|---|---:|---|---:|---|
| P06 | Original 15 Oct; 4,096 output tokens; full frozen reviewed case set | 1,354/1,366 | undefined | 0.025374 | A; Q39 |
| P07 | Historical mixed 4K/16K continuation; 4,096 × 27,146; 16,384 × 71 (mixed) output tokens; full frozen reviewed released test | 1,382/27,217 | undefined | 0.0155 | V; Q40 |
| P08 | Historical mixed 4K/16K continuation; 4,096 × 7,303; 16,384 × 5,548 (mixed) output tokens; full frozen reviewed released test | 12,616/12,851 | undefined | -0.121588 | V; Q41 |

### Interpretation and provenance limits

- **P01 and V01–V05:** the separate recovery audit could not recover original raw requests/responses, frozen manifests or full hash inventories. Their aggregate values can be reported, but raw-output rescoring and extraction diagnostics remain unavailable. Other missing loose score paths are marked A without assuming that every archive/backup is absent.
- **B01/B03/B04/B05:** both original and replay conditions are included. In the separate matched GPT comparison, the Qwen comparator is the archived replay: B01 77/197 and B03 31/82, not the B03 original 28/82.
- **P07/P08:** the new outputs parse completely, but correlation is still weak. This distinction separates delivery repair from biological predictive performance.
- **P09:** 6,848/12,851 correct (53.28768%) applies only to the explicitly declared threshold-derived released-split condition. Its parent is the new P08 run; it adds no model calls.
- **P42:** both success rates are zero with no accepted candidate; native novelty and uniqueness remain undefined. This primarily records delivery failure and cannot isolate underlying design quality.
- **V01–V03:** closed-question scoring uses permissive substring rules; open-question token recall is not exact-answer accuracy. **V04** whole-final exact match is sensitive to verbosity. **V05** native final-character accuracy and alternative extraction diagnostics are kept separate.
- None of these task scores establishes mechanistic explanation correctness, contamination-free evaluation, experimental design success, or matched paper training.


## The 15 agent-owned tasks: exact remaining work

These 15 tasks are not waiting for another general instruction from the user. They require the implementation, review or validation below. A completed download or software test is preparation; it is not a scored evaluation. Existing biological holds, restrictions on new head training and replacement judges still apply.

For every permitted numerical evaluation, completion requires a declared cohort and protocol, separated model inputs and scorer-only references, an independent delivery check, one recorded attempt per planned case, a sealed outcome record, and the correct full-denominator score. Missing/invalid outputs must remain visible. No selective replacement of failed historical answers is allowed. For a qualitative demonstration, completion means a clearly labelled evidence report; it cannot manufacture an unavailable numerical benchmark score.

### P04 — Beta-lactamase activity

**Already available:** publisher source archive. The expected 520 test cases come from the publisher loader; the actual LMDB inventory has not yet verified that count.

1. Inventory the test LMDB and record actual case count, unique IDs, source version and hashes.
2. Complete the independent assay/input eligibility review and record permitted, held or unresolved scope.
3. Produce separate model-input and scorer-reference files for that scope. Implement the scalar-output runner and bind the released scoring rule to the exact IDs.
4. Pass independent delivery checks, then run and score the complete declared permitted cohort.

**Proof of completion:** an inventory/review receipt, frozen input/reference manifests, a sealed full-cohort run and its native score. If scope is reduced, label the subset explicitly; do not call it the full native test.

### P05 — AAV fitness

**Already available:** the exact FLIP `two_vs_many` files and the 50,776-row test inventory. No dataset download is pending.

1. Complete the independent capsid-assay/input eligibility review; preserve any resulting holds.
2. Create the full permitted model-input/reference split, preserving the released split and identifiers.
3. Implement and freeze the scalar prediction/scoring configuration and pass its independent delivery checks.
4. Execute and score all planned cases in the declared scope, with failures retained in the outcome record.

**Proof of completion:** reviewed cohort, separated manifests, delivery receipt, sealed predictions and full-scope score. The missing work is review and execution preparation, not source access.

### P17 — ProteinGym substitutions

**Already available:** the 217-assay release archive and a GFP-only preparation prototype. That prototype is not a complete all-assay evaluation; its expected prepared-data directory is absent.

1. Inventory the release and create an assay-by-assay permitted/held/unresolved roster.
2. Prepare version-matched input/reference manifests for every retained assay; preserve exclusions explicitly.
3. Complete the prediction and native per-assay scoring pipeline. Freeze how the released aggregate is calculated; do not pool unrelated assay values into an invented metric.
4. Validate on independent fixtures, then execute, seal and score the declared assay panel.

**Proof of completion:** exact assay roster plus per-assay and aggregate results whose denominators reconcile. A GFP-only run cannot be presented as the 217-assay benchmark.

### P19 — PFArena T1

**Already available:** a frozen, independently reviewed 34-assay condition, runner/scorer, 37 passing software checks and three passing CPU tokenizer checks. No actual model-delivery gate has run. The broader panel still has 77 unreviewed and 12 held assays.

1. Add a separately frozen P19 entry to the runtime. The existing seven-task runtime does not admit it; this is an implementation handoff, not a new general permission question.
2. Run the three already prepared synthetic model-delivery cases and require a sealed 3/3 delivery pass. The in-memory mock result is insufficient.
3. Execute one attempt for each of the 34 frozen benchmark contexts, seal outcomes, then run the unchanged **NMS@40 and Recall@40** scorer.
4. Keep the 34-assay result distinct from the full 123-assay panel. Complete permissible independent review separately; preserve all held and interrupted scope.

**Proof of completion:** real synthetic delivery receipt and sealed/scored 34-assay condition, with the full-panel limitation stated.

### P21 — PFArena T3

**Already available:** 67 source tables, native builders and synthetic loader checks. Reviewed real model-input manifests and a real delivery gate are not prepared.

1. Review the real assay/input scope and record exact permitted case IDs.
2. Build inputs containing only the allowed supplied context and candidates; keep target measurements exclusively in scorer files. Verify the separation mechanically.
3. Bind a complete-ranking output validator to each exact candidate set, alongside the unchanged native scorer. Native parser acceptance alone does not guarantee a complete ranking.
4. Pass independent delivery checks, then execute and score the complete declared scope.

**Proof of completion:** reviewed real-input manifest, leakage/isolation receipt, complete-ranking delivery receipt, sealed outcomes and native results.

### P22 — PFArena T4

**Already available:** all 29 context/target table pairs and native builders. Only synthetic checks exist so far.

1. Review and freeze the permitted real case roster.
2. Prepare model inputs using only the allowed component measurements; keep combination target measurements in the scorer-only files. Verify every context/target join.
3. Validate full candidate-ranking delivery and preserve the released scoring formula.
4. Execute, seal and score all cases in the declared scope.

**Proof of completion:** context/target join and isolation receipts, independent delivery pass, sealed predictions and native results. The direct text condition does not require new heads or AlphaFold.

### P27 — Protein description

**Actually unavailable for exact native replication:** the original fixed NCBI accession list, absolute temporal cutoff and matching annotation snapshot were not found in the audited releases. An explicitly labelled available alternative is already authorized.

1. Select and freeze an available alternative cohort with exact source version, IDs, reference processing and exclusions.
2. Document how it differs from the original temporal cohort. Do not silently relabel P26 outputs as native P27.
3. Prepare separated model inputs/references and implement a source-grounded scoring contract, including empty/invalid-output handling.
4. Pass delivery checks and run, seal and score the whole declared alternative cohort.

**Proof of completion:** a reproducible, named adaptation and complete results. Exact native reproduction remains unavailable until the original cohort/reference artifacts are obtained.

### P34 — Iterative optimization

**Already available:** the encoder and five existing evaluator heads. No new training is needed for this available condition. The task-specific proposal adapter and optimization/scoring worker have not been implemented.

1. Implement the model-output adapter and validation/error handling against the released evaluator interface.
2. Implement the released-code iteration and scoring behavior. Freeze the budget, cohort, stopping rules and aggregation; document paper-versus-code differences.
3. Validate the adapter/worker on independent fixtures using the existing heads. Keep the held sixth landscape excluded and disclosed.
4. Execute and archive the complete declared trajectory for each permitted context, then calculate the specified aggregate.

**Proof of completion:** tested executable worker, frozen protocol and complete evaluated trajectories/results. Downloaded heads alone do not constitute this evaluation.

### P35 — Text-to-protein retrieval

**Already available:** checkpoint/corpus assets, a successful CPU checkpoint loader and 27 passing tests. The final corpus inclusion/exclusion list and ordering have not been produced; retrieval has not run.

1. Run the existing corpus projector; record every retained/rejected ID and reason, and freeze the exact candidate order and hashes.
2. Complete scope/input review and build the candidate representation cache with the existing checkpoint. Preserve missing or unparseable members explicitly.
3. Validate retrieval delivery, then run all five fixed released queries and archive complete scores and top-20 rankings.
4. Publish the declared retrieval demonstration with its corpus qualifications.

**Numerical-score limitation:** the release supplies no relevance labels or aggregate accuracy definition for those five examples. A benchmark accuracy additionally requires a source-grounded relevance set and scoring contract; rankings alone cannot supply one. Finishing the demonstration does not reproduce an unavailable native accuracy.

### P37 — Unconditional generation

**Preparation now completed:** isolated Python 3.10.18/Torch 1.12 environment, 15 checked dependencies, 17 verified source files, 21 unchanged contract tests, and CPU checkpoint/schema validation for all 3,252 tensors. No model forward or benchmark generation ran.

1. Perform strict combined weight binding in a memory-checked runtime. The current receipt checks the checkpoint and architecture sequentially within an 8 GiB allocation; it does not certify a combined loaded model.
2. Complete an actual independent folding-delivery check and preserve output validity/failure evidence.
3. Review the permitted inputs and freeze the complete generation/evaluation handoff for the prepared 1,000-sample adaptation, including sampling, clustering, references and aggregation.
4. Execute and score that declared adaptation, recording all invalid samples and evaluator failures.

**Proof of completion:** combined-load and delivery receipts, reviewed/frozen protocol, sealed full declared run and qualified evaluation. Original NatureLM sampling/clustering details remain unrecovered; the released-code adaptation must retain that distinction.

### P38 — Conditional generation and property proxies

**Preparation now completed:** 20 solubility and 10 thermal prompt templates, existing NetSolP assets and thermal head, and the full 11,275,562,724-byte ProtT5 encoder. The encoder matched the original publisher SHA-256 at **2:10:53 PM PDT**; all five supporting files also verified. The missing-download blocker is resolved. No evaluator forward or benchmark run occurred.

1. Assemble the isolated NetSolP runtime and validate its synthetic input/output behavior, output interpretation and failure handling.
2. Bind the verified encoder to the existing thermal head and validate that separate runtime; retain its frozen input assumptions.
3. Freeze independent generation and model-delivery gates for the two distinct proxy conditions, including candidate counts, seeds, evaluation outputs and full-denominator failure policy.
4. Review the permissible scope, pass the actual delivery gates, then run and report each complete declared condition separately.

**Proof of completion:** two working evaluated conditions with sealed outputs and qualified proxy results. The original SFM property heads, reference cohort and allocation were not recovered; neither proxy may be renamed the original NatureLM endpoint. No new head training is authorized.

### P39 — Heme-binding case study

**Already available:** structural evaluator dependencies. No prospective case-study configuration or task-specific complex-prediction worker has been implemented. The original cohort, selection rules and quantitative binding-success contract are unreleased.

1. Define and review a clearly labelled available case-study cohort and fixed selection/evaluation rules before generation.
2. Implement and validate the existing-predictor interface and input/output packaging; isolate any scorer-only references.
3. Freeze the declared generation and evidence-collection condition, execute its complete scope and retain all failures.
4. Publish the resulting structural/proxy evidence and its limitations.

**Proof of completion:** a reproducible qualitative case study. Predicted structures or selected examples are not measured binding accuracy; the unreleased original benchmark cannot be reconstructed by inventing its denominator or gold labels.

### P40 — RAbD redesign

**Already available:** all 60 current-structure mappings/masks and 13 passing synthetic checks. Real-case eligibility review and the model-input geometry adapter remain unfinished.

1. Complete the independent permitted-case roster and verify the mapping of each retained case.
2. Implement input packaging that preserves permitted structural context while excluding the target identities and target coordinates; test that separation.
3. Validate the solver-output and evaluator interfaces on independent cases. Freeze aggregation and failure handling for the current-structure condition.
4. Execute, seal and score all cases in the declared scope.

**Proof of completion:** reviewed roster, tested input-isolation and geometry adapter, delivery receipt, sealed outputs and declared metrics. Current official structures are a separate provenance condition from unrecovered historical processed bytes.

### P41 — Structural demonstration adaptation

**Already available:** 16 checkpoint files, five vendor dependencies and 83 fixtures. There is no task-specific masking/preprocessing/scoring worker. The original holdout IDs, canonical masks and aggregation were not released in the inspected sources.

1. Freeze the available released-demonstration roster and explicitly state that it is not the original paper holdout.
2. Implement and test masking, preprocessing, reference separation and scorer input/output packaging.
3. Assemble the existing-checkpoint runtime and pass an independent delivery gate for that precise demonstration condition.
4. Execute its complete scope and publish all results/failures with qualified metrics.

**Proof of completion:** a reproducible released-demo evaluation. Exact paper reproduction additionally needs the missing original cohort/masks/aggregation; five examples cannot stand in for the unreleased holdout.

### V07 — Released-cohort visual extraction adaptation

**Already available:** all 8,000 page identities and 2,215 prepared case/reference records. Materialization is complete; the old file suggesting copying was still running is stale.

1. Complete independent question/full-deck eligibility review and record the exact permitted case IDs.
2. Run the actual model processor on the 20-page inputs, measure expanded input/context usage, and verify that no page or required output budget is silently dropped.
3. Freeze the permitted mixed-image-source condition and pass its independent delivery panel.
4. Execute, seal and score every case in that declared scope with the specified extraction scorer.

**Proof of completion:** review roster, actual processor/context receipt, delivery pass, sealed predictions and scored results. Preserve the 7,700-original/300-processed image distinction. Exact Ryze Table 3 configuration is still unavailable.

### What these 15 do not include

- P12–P14 are already generating dense confidence vectors; P15 is queued. They need their existing full runs and native scoring to finish, not another preparation checklist.
- P33, V06 and P44 retain the user's training/judge holds. P44 still has agent-owned cohort/rubric recovery work despite that hold.
- B06, P18, P20, P30–P32 and P36 retain recorded biological/provider restrictions or interrupted-review holds. This report does not restart or reroute those actions.
- The 12-case GFP delivery pilot and four OpenAI delivery panels are not benchmark scores. The historical 17,145-case continuation is closed. The separate B08 uniform-16K proposal remains unlaunched.

### Evidence for the remaining-work checklist

- [Concrete blocker ledger](CATALOG_BLOCKERS_2026-10-20.json) and [57-setting status tracker](CATALOG_STATUS.md). Those are timestamped reports; the latest task-local receipts take precedence over older preparation wording.
- Source inventories: `.local/source_acquisition_2026-10-19/prediction_datasets/summary.json` and `.local/source_recovery_round2_2026-10-19/pfarena/native_preflight/`.
- P19 gate preparation: `.local/catalog_execution_2026-10-20/tasks/P19/runtime_integration_preparation/`.
- P37 completed CPU preparation: `.local/catalog_execution_2026-10-20/tasks/P37/runtime_preparation/status.json` and `cpu_validation.json`.
- P38 verified source acquisition: `.local/catalog_execution_2026-10-20/tasks/P38/thermal_encoder_acquisition/completion.json`.
- V07 completed materialization: `.local/catalog_execution_2026-10-20/tasks/V07/materialization_resume_20261020_v1/completion.json`.

Paths beginning `.local/` are private workspace evidence, not public GitHub links. No model weights or scorer-reference rows are included in this report.

## Source provenance appendix

### Exact aggregate sources

| Source | SHA-256 |
|---|---|
| reports/EVALUATION_DECISION_TABLE.json | `6f2b270e3b786c4490af6bb261456e425c594d265e06ae08fb9984ceaae22e77` |
| reports/RESULTS_AT_A_GLANCE.json | `d35f142f779433e83bc0fe4ca2413761d9d7c123b1272f692483356d0f9ebeaf` |
| reports/CATALOG_NEW_SCORES_2026-10-20.json | `6c6a316d82eeb0397c6f414090e2978eb568444a5a641e58e3e8461b018b50fe` |
| reports/VERIFIED_RESULTS_SNAPSHOT_2026-10-16T042525.json | `bbc45d078704958137b4ea308b47f15163c72ba357d624f4dd145b5818791451` |
| .local/catalog_resume_2026-10-19/historical/recovery_receipt.json | `a1379d982cb4ad9a1a5cae81f7362bc4f75082349dbf8b2652f8ebd326a138d5` |

Decision-table source timestamp: `2026-10-20T13:34:41.721473-07:00`. New-score export timestamp: `2026-10-20T13:34:29.492465-07:00`. Public source tree checked at commit `2aa34467e81cee20a7da9f4f4f85ab788c70e725` on `2026-10-20T14:09:20.480374-07:00`.

### Per-condition source paths and recorded score hashes

For A entries, the hash is preserved from the aggregate record and is **not newly validated against unavailable score bytes**.

| ID | Run | Score source | Recorded SHA-256 |
|---|---|---|---|
| Q01 | `qwen38_27b_p01_original_test_2026-10-15` | results/runs/qwen38_27b_p01_original_test_2026-10-15/scores.json | `85a31d75557586e850d615b9178d22bd79a75b94a8678c614b9c5c92344dd81b` |
| Q02 | `qwen38_27b_p02_original_test_2026-10-15` | results/runs/qwen38_27b_p02_original_test_2026-10-15/scores.json | `214c93f6e2d725550a75a9b01d54ee155cf1f962ef99e4648a3333abed9d1012` |
| Q03 | `qwen38_27b_p03_full_test_slurm_2026-10-16` | results/runs/qwen38_27b_p03_full_test_slurm_2026-10-16/scores.json | `b2502d3ded2d81fc3f03c8260cd6d2db01dc5ae914e6d84e5ae6c81c18882e4a` |
| Q04 | `qwen38_27b_p06_full_test_nonthinking_regex256_2026-10-20_v1` | results/runs/qwen38_27b_p06_full_test_nonthinking_regex256_2026-10-20_v1/scores.json | `e0231f651a8c6f3fab2ef16cb4ce280c6b78a9b6ada0c216d95bcb698ff6e385` |
| Q05 | `qwen38_27b_p07_full_test_nonthinking_scalar_2026-10-20_v1` | results/runs/qwen38_27b_p07_full_test_nonthinking_scalar_2026-10-20_v1/scores.json | `f79fdcb9a294eb09e09cf8fe4642e04f7eb413f260cf22661054d596dc1416e3` |
| Q06 | `qwen38_27b_p08_full_test_nonthinking_structured_scalar_2026-10-20_v1` | results/runs/qwen38_27b_p08_full_test_nonthinking_structured_scalar_2026-10-20_v1/scores.json | `83ff575019fb3f5305b6b9859edc17e7a4ada3787f3de23e5f7fbddc764da006` |
| Q07 | `qwen38_27b_p09_scireason_gt1_from_p08_2026-10-20_v1` | results/runs/qwen38_27b_p09_scireason_gt1_from_p08_2026-10-20_v1/scores.json | `6e03f9612f876d4b3f570b00c5937607d9bf0c9552eebc783b83238635a91f31` |
| Q08 | `qwen38_27b_p10_original_test_2026-10-15` | results/runs/qwen38_27b_p10_original_test_2026-10-15/scores.json | `a0d8b8777b712a72a1c4d484844c1b990ed44f76fadea824f13f35a45eddea8d` |
| Q09 | `qwen38_27b_p11_original_test_2026-10-15` | results/runs/qwen38_27b_p11_original_test_2026-10-15/scores.json | `4a6ae94af3364fed0da07075b95d89bf9d613c73bbc98a0c9555e3f17b106b06` |
| Q10 | `qwen38_27b_p16_slurm_replay_2026-10-16_mixed_4k16k_scoring_v1` | results/runs/qwen38_27b_p16_slurm_replay_2026-10-16_mixed_4k16k_scoring_v1/scores.json | `024501321eb30797df29401b256007ab6992881a6670027cb5232cce72d5972b` |
| Q11 | `qwen38_27b_p16_slurm_replay_2026-10-16_mixed_4k16k_scoring_v1` | reports/REACTION_EXTRACTION_DIAGNOSTIC_2026-10-19.json | `68d143a13641237c1141b4d47ecdda438f7f81711ffccc7a4cdd6069764f449b` |
| Q12 | `qwen38_27b_p23_description_full_parallel_2026-10-15` | results/runs/qwen38_27b_p23_description_full_parallel_2026-10-15/scores.json | `07ad7b2c42b9101e4518af6261cc09759ecf821103d4028566155843a0186807` |
| Q13 | `qwen38_27b_p24_description_full_parallel_2026-10-15` | results/runs/qwen38_27b_p24_description_full_parallel_2026-10-15/scores.json | `71288d20094fd924286886e3ca16f977f3493c06e457eae198adde9005bfd4cf` |
| Q14 | `qwen38_27b_p25_description_full_parallel_2026-10-15` | results/runs/qwen38_27b_p25_description_full_parallel_2026-10-15/scores.json | `959a351147d67df58e6467069fa7b498e52e5887c5edba273d81b45ff09fa24e` |
| Q15 | `qwen38_27b_p26_description_full_parallel_2026-10-15` | results/runs/qwen38_27b_p26_description_full_parallel_2026-10-15/scores.json | `dc649cf4a62d619b0316bf72b6a0b3b1b292daf0c4516de359895fe30d108063` |
| Q16 | `qwen38_27b_litqa2_public_reviewed_2026-10-15` | results/runs/qwen38_27b_litqa2_public_reviewed_2026-10-15/scores.json | `88bcea024f55c609e71e40b803a226862741a0ae923b5e69eb222b13833f4130` |
| Q17 | `qwen38_27b_litqa2_replay_2026-10-16` | results/runs/qwen38_27b_litqa2_replay_2026-10-16/scores.json | `5b8d04effeec755cb0c0ba3de29dde6b47ce8a7b34a0743766ef4d40f6c4a4fb` |
| Q18 | `qwen38_27b_b02_public_reviewed_2026-10-15` | results/runs/qwen38_27b_b02_public_reviewed_2026-10-15/scores.json | `07448327f790ed477aabbc18271b9f524f4eb0de03729aaa831e98561411e49a` |
| Q19 | `qwen38_27b_b03_public_reviewed_2026-10-15` | results/runs/qwen38_27b_b03_public_reviewed_2026-10-15/scores.json | `0a2d1cf825705c380269275a2a9b00ec7cac3851c36ba35a5f43bf45761ebd3b` |
| Q20 | `qwen38_27b_b03_slurm_replay_2026-10-16` | results/runs/qwen38_27b_b03_slurm_replay_2026-10-16/scores.json | `7aae5d9c7f24d75d42e341d7bd8d174fafc64aff054c6ee6ca6448e73df9e927` |
| Q21 | `qwen38_27b_b04_public_reviewed_2026-10-15` | results/runs/qwen38_27b_b04_public_reviewed_2026-10-15/scores.json | `509f8db69ec61f78e3d74442136c130eecf2c501851abb61e2aca907ec076cf8` |
| Q22 | `qwen38_27b_b04_slurm_replay_2026-10-16` | results/runs/qwen38_27b_b04_slurm_replay_2026-10-16/scores.json | `a8a980724acc6f811f80f9e7ff5f9dd773d3704565da5d9bfd38c8152bf852b5` |
| Q23 | `qwen38_27b_b05_public_reviewed_2026-10-15` | results/runs/qwen38_27b_b05_public_reviewed_2026-10-15/scores.json | `6ad92a6f73845b93d39111bbca3685ac35ad75cc4a0d2e80ac35304587ceb76e` |
| Q24 | `qwen38_27b_b05_slurm_replay_2026-10-16` | results/runs/qwen38_27b_b05_slurm_replay_2026-10-16/scores.json | `1641758fe72f79d51392eeb1aa51c127d16d6e503b69d16cfe9a88c143e96968` |
| Q25 | `qwen38_27b_b07_public_reviewed_2026-10-15` | results/runs/qwen38_27b_b07_public_reviewed_2026-10-15/scores.json | `7485aa61236d103c67a1fe692148d30ef1234e2ff13e72f267096a4a009aa37f` |
| Q26 | `qwen38_27b_b08_public_reviewed_2026-10-15` | results/runs/qwen38_27b_b08_public_reviewed_2026-10-15/scores.json | `d06efe40faf83d49cd688a2f0451006c244b138ea69861d41bc3cd0ff28ff417` |
| Q27 | `qwen38_27b_p42_gfp_qualified_two_regimes_2026-10-15` | results/runs/qwen38_27b_p42_gfp_qualified_two_regimes_2026-10-15/scores.json | `21e2ea0d6c767baf407f1c336e1d47e485aa7d8f9372578c4951cd40121d6a36` |
| Q28 | `qwen38_27b_p42_gfp_qualified_two_regimes_2026-10-15` | results/runs/qwen38_27b_p42_gfp_qualified_two_regimes_2026-10-15/scores.json | `21e2ea0d6c767baf407f1c336e1d47e485aa7d8f9372578c4951cd40121d6a36` |
| Q29 | `qwen38_27b_v01_native_test_2026-10-15` | results/runs/qwen38_27b_v01_native_test_2026-10-15/scores.json | `9852b01a5030104865a23e6fbcc447bcefea5ffa08d71c85081e9afe5cfe1343` |
| Q30 | `qwen38_27b_v02_native_test_2026-10-15` | results/runs/qwen38_27b_v02_native_test_2026-10-15/scores.json | `88807c326e34b7939e70e574a698bbefddb711b880e20f9562704683332ca750` |
| Q31 | `qwen38_27b_v03_full_publisher_mirror_2026-10-15_seven_gpu` | results/runs/qwen38_27b_v03_full_publisher_mirror_2026-10-15_seven_gpu/scores.json | `9275fc494595cfdb04a83e59169462a3958d3763813d8e3c5fe8754f79e5f580` |
| Q32 | `qwen38_27b_v04_original_test500_2026-10-15` | results/runs/qwen38_27b_v04_original_test500_2026-10-15/scores.json | `f026572c716d7755439e0775538f56a6d88e2cd33b74319f5c454bc97e4fe22d` |
| Q33 | `qwen38_27b_v05_pmcvqa_clean2000_td_2026-10-15` | results/runs/qwen38_27b_v05_pmcvqa_clean2000_td_2026-10-15/scores.json | `213b9d584f9cf24673ccf55ae09f621f88680fab80537b9ccdc9978900b07cdf` |
| Q34 | `qwen38_27b_v05_pmcvqa_clean2000_td_2026-10-15` | results/runs/qwen38_27b_v05_pmcvqa_clean2000_td_2026-10-15/scores.json | `213b9d584f9cf24673ccf55ae09f621f88680fab80537b9ccdc9978900b07cdf` |
| Q35 | `qwen38_27b_v05_pmcvqa_clean2000_td_2026-10-15` | results/runs/qwen38_27b_v05_pmcvqa_clean2000_td_2026-10-15/scores.json | `213b9d584f9cf24673ccf55ae09f621f88680fab80537b9ccdc9978900b07cdf` |
| Q36 | `qwen38_27b_dti_bindingdb_likelihood_2026-10-15` | results/runs/qwen38_27b_dti_bindingdb_likelihood_2026-10-15/scores.json | `76450468482a2315f24f82379dfb55e990986128467e9d8a65772baa272645c4` |
| Q37 | `qwen38_27b_dti_biosnap_likelihood_2026-10-15` | results/runs/qwen38_27b_dti_biosnap_likelihood_2026-10-15/scores.json | `e013b6b00b66db8e68748a46addfed7fecdcdc46c278c514717eebc3aedac8af` |
| Q38 | `qwen38_27b_dti_human_likelihood_2026-10-15` | results/runs/qwen38_27b_dti_human_likelihood_2026-10-15/scores.json | `c2c563e1bfd927515341ee54d0555027ae496349fdc6ce8c64825cc44379e962` |
| Q39 | `qwen38_27b_p06_original_test_2026-10-15` | results/runs/qwen38_27b_p06_original_test_2026-10-15/scores.json | `7af3d8a3235930d18d02d85c98cdd04b375db49c72f077d08b2788d49d5e778a` |
| Q40 | `qwen38_27b_p07_full_test_slurm_2026-10-16_mixed_4k16k_scoring_v1` | results/runs/qwen38_27b_p07_full_test_slurm_2026-10-16_mixed_4k16k_scoring_v1/scores.json | `18979759cc43b82517e9933712274c6a82f33bb3b83eaae59b56ba6ac29710e6` |
| Q41 | `qwen38_27b_p08_full_test_slurm_2026-10-16_mixed_4k16k_scoring_v1` | results/runs/qwen38_27b_p08_full_test_slurm_2026-10-16_mixed_4k16k_scoring_v1/scores.json | `53ad6a4142efefdfff140decfaeb16efee1f077ae3629788a57da1fd56f7404e` |
