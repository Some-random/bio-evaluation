# Biological Evaluation Results

*October 20, 2026*

Results are available for **28 of 57 evaluation settings**. GPT comparisons currently cover three settings; 15 further evaluations are in preparation.

## Qwen and GPT comparison

**Accuracy (%) on matched test cases.** The Qwen baseline uses the same archived 4K runs and test cases used for the GPT comparison. Unsuccessful responses remain in the denominator.

| Evaluation | Test cases | Qwen3.8-27B | GPT-6 Luna | GPT-6.1 Sol |
|---|---:|---:|---:|---:|
| Literature QA — LitQA2 (B01) | 197 | 39.09% | 49.24% | 56.85% |
| Supplementary-information QA — SuppQA (B03) | 82 | 37.80% | 53.66% | 56.10% |
| Protein subcellular localization (P03) | 2,773 | 26.11% | 56.80% | Not evaluated |

GPT-6 Luna scores higher than Qwen on all three evaluated tasks. GPT-6.1 Sol scores higher than both on the two QA tasks evaluated for that model.

## Additional Qwen results

The table presents the latest completed Qwen result for each evaluation. Correlation, AUROC, AUPRC and ROUGE-L are reported on their original scales; percentages are labelled explicitly.

| Evaluation | Metric | Qwen3.8-27B |
|---|---|---:|
| Database QA — DbQA (B02) | Accuracy | 31.35% |
| Figure QA — FigQA (B04) | Accuracy | 72.38% |
| Table QA — TableQA (B05) | Accuracy | 88.11% |
| Sequence QA — SeqQA (B07) | Accuracy | 12.67% |
| Cloning scenarios (B08) | Accuracy | 0.00% |
| Protein solubility (P01) | Accuracy | 24.21% |
| Binary protein localization (P02) | Accuracy | 27.39% |
| Thermostability (P06) | Spearman correlation | 0.0037 |
| GFP fluorescence (P07) | Spearman correlation | 0.0300 |
| Protein stability (P08) | Spearman correlation | 0.2270 |
| Stability classification (P09)† | Accuracy | 53.29% |
| Human protein interactions (P10) | Accuracy | 50.21% |
| Yeast protein interactions (P11) | Accuracy | 45.18% |
| Reaction classification (P16) | Accuracy | 0.16% |
| Protein function generation (P23) | ROUGE-L | 0.0431 |
| Catalytic activity generation (P24) | ROUGE-L | 0.0396 |
| Domain and motif generation (P25) | ROUGE-L | 0.0259 |
| Functional description generation (P26) | ROUGE-L | 0.0494 |
| GFP candidate generation (P42)‡ | Automated success rate | 0.00% |
| Drug–target interaction — BindingDB (P43) | AUROC / AUPRC | 0.5036 / 0.4103 |
| Drug–target interaction — BioSNAP (P43) | AUROC / AUPRC | 0.5336 / 0.5217 |
| Drug–target interaction — Human (P43) | AUROC / AUPRC | 0.4747 / 0.4194 |
| VQA-RAD (V01) | Open-answer token recall | 59.54% |
| VQA-RAD (V01) | Closed-answer accuracy | 86.76% |
| SLAKE English (V02) | Open-answer token recall | 50.98% |
| SLAKE English (V02) | Closed-answer accuracy | 84.62% |
| PathVQA (V03) | Open-answer token recall | 26.38% |
| PathVQA (V03) | Closed-answer accuracy | 85.87% |
| ImageCLEF-VQA 2019 (V04) | Exact-match accuracy | 0.00% |
| PMC-VQA (V05) | Final-character accuracy | 2.00% |

These evaluations use available released datasets and declared adaptations; they do not imply matched reproduction of the original papers' trained systems. **†** P09 is calculated from P08 predictions rather than a separate generation run. **‡** P42 uses an automated evaluator, not experimental fluorescence measurements; neither evaluated edit setting produced an accepted candidate.

## Evaluations in preparation

| Evaluation | Work required to obtain results |
|---|---|
| Beta-lactamase activity (P04) | Complete test-data inventory and case eligibility review; prepare separate model inputs and reference answers; run prediction and scoring. |
| AAV fitness (P05) | Complete assay eligibility review; prepare the released test split; validate scalar predictions and run scoring. |
| ProteinGym substitutions (P17) | Finalize the eligible assay set and implement the complete per-assay prediction and scoring pipeline. |
| PFArena T1 (P19) | Connect the prepared 34-assay evaluator, pass end-to-end delivery checks, and run NMS@40 and Recall@40 scoring. |
| PFArena T3 (P21) | Prepare reviewed inputs with permitted context, validate complete candidate rankings, and run the released scorer. |
| PFArena T4 (P22) | Separate permitted context from hidden targets, validate complete candidate rankings, and run the released scorer. |
| Protein description (P27) | Select a fixed alternative evaluation cohort and implement its reference processing, generation and scoring. |
| Iterative optimization (P34) | Implement and validate the proposal–evaluation loop using the five available pretrained scoring heads. |
| Text-to-protein retrieval (P35) | Finalize the candidate corpus and run the five released queries. A numerical accuracy additionally needs relevance labels. |
| Unconditional generation (P37) | Validate the combined model/checkpoint and end-to-end folding evaluator, then execute the prepared 1,000-sample evaluation. |
| Conditional generation (P38) | Validate both property evaluators, finalize the separate proxy protocols, and run the reviewed evaluations. |
| Heme-binding case study (P39) | Define a reproducible qualitative case study and implement its structural prediction and evaluation pipeline. |
| RAbD redesign (P40) | Complete case review and the structural input adapter, then run the 60-case evaluation. |
| Structural design demonstration (P41) | Implement masked-input preparation and scoring for the available released demonstrations. |
| Visual extraction — Ryze/SlideVQA (V07) | Validate 20-image processing and context limits, complete case review, and run the prepared 2,215-case evaluation. |

Where original cohorts or scoring definitions are unavailable, the planned result will be labelled as an adaptation or demonstration. It will not be presented as the original paper's benchmark score.
