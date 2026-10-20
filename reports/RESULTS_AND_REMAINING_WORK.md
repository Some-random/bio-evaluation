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

## Dataset years and example questions

Years link to the original dataset or evaluation publications. Where two years are shown, they distinguish the underlying dataset from a later evaluation. Examples are short published questions or source-based illustrations; bracketed text stands in for the required sequence, image or other input.

### Scientific question answering

| Dataset / evaluation | Introduced | Example question or task |
|---|---|---|
| LAB-Bench: LitQA2 (B01) | [2024](https://arxiv.org/abs/2407.10362) | According to the study, how does the specified Spindle E variant affect mature piRNA abundance in silkworm cells? |
| LAB-Bench: DbQA (B02) | [2024](https://arxiv.org/abs/2407.10362) | Which listed human gene falls within chromosome band 4q33 in Ensembl Release 110? |
| LAB-Bench: SuppQA (B03) | [2024](https://arxiv.org/abs/2407.10362) | In the supplementary methods for [paper], what incubation duration is used in the specified sample-processing step? |
| LAB-Bench: FigQA (B04) | [2024](https://arxiv.org/abs/2407.10362) | Where does the half waveplate occur relative to the SLM? |
| LAB-Bench: TableQA (B05) | [2024](https://arxiv.org/abs/2407.10362) | Using the table, calculate the ratio of increased crotonylated sites to increased succinylated sites. |
| LAB-Bench: SeqQA (B07) | [2024](https://arxiv.org/abs/2407.10362) | What is the percent GC of the DNA sequence [sequence]? |
| LAB-Bench: Cloning Scenarios (B08) | [2024](https://arxiv.org/abs/2407.10362) | From the supplied plasmid and fragment sequences, identify the element carried by the DNA fragment. |

### Protein prediction and description

| Dataset / evaluation | Introduced | Example question or task |
|---|---|---|
| DeepSol solubility — PEER (P01) | [2018](https://academic.oup.com/bioinformatics/article/34/15/2605/4938490); PEER [2022](https://arxiv.org/abs/2206.02096) | Will [protein sequence] be soluble when expressed? |
| DeepLoc binary localization — PEER (P02) | [2017](https://academic.oup.com/bioinformatics/article/33/21/3387/3931857); PEER [2022](https://arxiv.org/abs/2206.02096) | Is [protein sequence] a membrane-bound or soluble protein? |
| DeepLoc subcellular localization — PEER (P03) | [2017](https://academic.oup.com/bioinformatics/article/33/21/3387/3931857); PEER [2022](https://arxiv.org/abs/2206.02096) | Which cellular compartment contains [protein sequence], among the ten listed locations? |
| Envision beta-lactamase activity — PEER (P04) | [2022](https://arxiv.org/abs/2206.02096) | What activity score does the assay assign to [protein variant sequence]? |
| AAV fitness — FLIP (P05) | [2021](https://www.biorxiv.org/content/10.1101/2021.11.09.467890v1) | What fitness score does the assay assign to [AAV variant sequence]? |
| Meltome thermostability — FLIP (P06) | [2021](https://www.biorxiv.org/content/10.1101/2021.11.09.467890v1) | What is the melting temperature of [protein sequence]? |
| GFP fluorescence — TAPE (P07) | [2019](https://arxiv.org/abs/1906.08230) | What is the log-fluorescence value for [GFP variant sequence]? |
| Protein folding stability — TAPE (P08) | [2019](https://arxiv.org/abs/1906.08230) | What is the folding-stability score of [protein sequence]? |
| Stability classification — NatureLM-style adaptation (P09) | [2025](https://arxiv.org/abs/2502.07527) | Does [protein sequence] meet the benchmark threshold for the stable class? |
| Human protein interactions — PEER (P10) | [2022](https://arxiv.org/abs/2206.02096) | Do [human protein sequence A] and [human protein sequence B] interact? |
| Yeast protein interactions — PEER (P11) | [2022](https://arxiv.org/abs/2206.02096) | Do [yeast protein sequence A] and [yeast protein sequence B] interact? |
| Enzyme reaction classes — IEConv/ProtST (P16) | [2020](https://arxiv.org/abs/2007.06252); ProtST [2023](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf) | Which of the 384 reaction classes matches [protein sequence]? |
| ProteinGym substitutions (P17) | [2022](https://arxiv.org/abs/2205.13760); expanded [2023](https://proceedings.neurips.cc/paper_files/paper/2023/file/cac723e5ff29f65e3fcbb0739ae91bee-Paper-Datasets_and_Benchmarks.pdf) | How do the assay scores differ across [protein variant sequences]? |
| PFArena T1 — single-mutant generation (P19) | [2026](https://arxiv.org/abs/2609.28921) | Task: return single-substitution candidates for [protein] under [assay description]. |
| PFArena T3 — anchor-informed ranking (P21) | [2026](https://arxiv.org/abs/2609.28921) | Rank [candidate variants] using [assay description] and the supplied score for [reference variant]. |
| PFArena T4 — single-mutant-informed ranking (P22) | [2026](https://arxiv.org/abs/2609.28921) | Rank [combined variants] using [assay description] and supplied measurements for their individual substitutions. |
| Mol-Instructions — protein function (P23) | [2023](https://arxiv.org/abs/2306.08018) | What biological function is associated with [protein sequence]? |
| Mol-Instructions — catalytic activity (P24) | [2023](https://arxiv.org/abs/2306.08018) | What reaction does [protein sequence] catalyze? |
| Mol-Instructions — domains and motifs (P25) | [2023](https://arxiv.org/abs/2306.08018) | Describe the domains and motifs associated with [protein sequence]. |
| Mol-Instructions — general function (P26) | [2023](https://arxiv.org/abs/2306.08018) | Write a short description of the overall role of [protein sequence]. |
| NatureLM — protein characteristics description (P27) | [2025](https://arxiv.org/abs/2502.07527) | Describe the properties and functions of [protein sequence]. |

### Generation, retrieval and drug–target interaction

| Dataset / evaluation | Introduced | Example question or task |
|---|---|---|
| MutaPLM iterative optimization evaluation (P34) | [2024](https://arxiv.org/abs/2410.22949) | Given [protein] and [evaluation objective], propose the next candidate in an iterative optimization run. |
| ProtST text-to-protein retrieval (P35) | [2023](https://proceedings.mlr.press/v202/xu23t.html) | Which proteins in [candidate collection] best match [functional description]? |
| NatureLM unconditional protein generation (P37) | [2025](https://arxiv.org/abs/2502.07527) | Input: the protein start token only. Output: a generated protein sequence. |
| NatureLM property-conditioned protein generation (P38) | [2025](https://arxiv.org/abs/2502.07527) | Generate a soluble protein sequence. |
| NatureLM heme-binding generation case study (P39) | [2025](https://arxiv.org/abs/2502.07527) | Design a heme-binding protein sequence. |
| RAbD antibody-region redesign benchmark (P40) | [2018](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1006112); NatureLM [2025](https://arxiv.org/html/2502.07527v3#S4.SS3) | Complete [masked antibody region] using [antigen and antibody-framework context]. |
| Proteo-R1 structural design demonstrations (P41) | [2026](https://arxiv.org/abs/2605.02937) | Complete [masked antibody structure] while preserving [fixed framework context]. |
| STRIDE GFP candidate-editing evaluation (P42) | [2026](https://arxiv.org/abs/2603.03573) | Given [reference GFP sequence], return a candidate using the task's permitted edit notation. |
| Drug-target interaction: BindingDB (DrugBAN split) (P43) | [2000](https://pmc.ncbi.nlm.nih.gov/articles/PMC4702793/); DrugBAN [2022](https://arxiv.org/abs/2208.02194) | Do [drug representation] and [protein sequence] interact? |
| Drug-target interaction: BioSNAP (DrugBAN split) (P43) | [2018](https://snap.stanford.edu/biodata/); DrugBAN [2022](https://arxiv.org/abs/2208.02194) | Do [drug representation] and [protein sequence] interact? |
| Drug-target interaction: Human (DrugBAN split) (P43) | [2015](https://pubmed.ncbi.nlm.nih.gov/26072486/); DrugBAN [2022](https://arxiv.org/abs/2208.02194) | Do [compound representation] and [human protein sequence] interact? |

### Visual question answering

| Dataset / evaluation | Introduced | Example question or task |
|---|---|---|
| VQA-RAD (V01) | [2018](https://www.nature.com/articles/sdata2018251) | Which organ is shown in this radiology image? |
| SLAKE (English) (V02) | [2021](https://arxiv.org/abs/2102.09542) | Does the image contain left lung? |
| PathVQA (V03) | [2020](https://arxiv.org/abs/2003.10286) | What is expanded in the region of epiphysis? |
| ImageCLEF-VQA 2019 (V04) | [2019](https://www.imageclef.org/2019/medical/vqa/) | In what plane is this mammograph taken? |
| PMC-VQA (V05) | [2023](https://arxiv.org/abs/2305.10415) | What is the view of the brain used in the image? |
| SlideVQA / Ryze visual extraction (V07) | [2023](https://arxiv.org/abs/2301.04883); Ryze [2026](https://arxiv.org/abs/2606.00902) | According to the slide, what percentage is attributed to internal meeting decisions? |

The NatureLM dates identify the published evaluations, including case studies; they do not imply that every original test set was publicly released. DrugBAN was first described in 2022 and published in 2023.
