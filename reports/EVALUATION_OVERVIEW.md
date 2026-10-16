# Biological evaluation overview

Model: **Qwen3.8-27B**.

Scores: **2026-10-16 04:25 UTC** · Run status: **2026-10-16 09:24 UTC**.

**25 of 64 evaluation settings have finished runs.** An asterisk (*) marks incomplete coverage or scoring.

**37 of 64 settings are runnable with the current setup.** Text and vision inputs are supported. Runnable means the required inputs, execution path and scorer are available; it includes explicitly marked reviewed subsets and does not guarantee correct or valid predictions.

Finished, Partial and Running describe saved run status; Ready describes executability. **Run status unconfirmed** means no verified completion record. Missing requirements are listed per row. Published scores are separate reference results; full protocol notes are at the end.

Expand a category to see its tasks and datasets.

<details>
<summary><h2>Protein properties, interactions and developability</h2></summary>

#### Protein solubility

2 dataset groups · results available

| Task | Dataset/protocol | Status / what's missing | Qwen result | Published reference |
|---|---|---|---|---|
| Protein solubility | DeepSol solubility — PEER split | Finished · Ready | accuracy 24.2% | BioT5+: accuracy 74.37% ± 0.19 percentage points; Table 6 · [source](https://arxiv.org/html/2402.17810v2) |
|  | PFMBench solubility panel | Needs data or protocol<br>Needs four PFMBench splits and separate solubility classification/regression scoring. | — | ESM2-Adapter, Table 1 means: DeepSol AUROC 0.8467; DeepSoluE AUROC 0.7699; ProtSolM AUROC 0.8572; eSOL Spearman 0.2761 · [source](https://arxiv.org/html/2506.14796v1) |

#### Protein localization

2 dataset groups · results available · running or queued

| Task | Dataset/protocol | Status / what's missing | Qwen result | Published reference |
|---|---|---|---|---|
| Binary protein localization | DeepLoc — binary and 10-compartment localization<br>Binary localization — DeepLoc/PEER | Finished · Ready | accuracy 27.4% | BioT5+: accuracy 90.41% ± 0.07 percentage points; Table 6 · [source](https://arxiv.org/html/2402.17810v2) |
| Ten-compartment protein localization* | DeepLoc — binary and 10-compartment localization<br>Subcellular localization — DeepLoc | Running or queued · 50.8% trajectories uploaded* · Ready | — | Binary accuracy: BioT5+ 90.41%; BioT5 91.69%. 10-class accuracy: ProtST-ESM-2 83.39%; ESM-2 80.84%. · [source](https://arxiv.org/html/2206.02096v2) |
| Localization and sorting signals | PFMBench localization and sorting-signal panel | Needs data or protocol<br>Needs PFMBench splits, label vocabularies and binary/multilabel scoring. | — | ESM2-Adapter, Table 1 means: DeepLocMulti Accuracy 0.7666; DeepLoc2Multi F1 0.7505; DeepLocBinary AUROC 0.9338; SortingSignal F1 0.8598 · [source](https://arxiv.org/html/2506.14796v1) |

#### Protein activity, stability and production

6 dataset groups · partial results* · running or queued

| Task | Dataset/protocol | Status / what's missing | Qwen result | Published reference |
|---|---|---|---|---|
| Protein fluorescence* | TAPE GFP / Sarkisyan fluorescence | Running or queued · 3.7% trajectories uploaded* · Ready | — | Spearman: ProtST-ESM-2 0.682; ESM-2 0.677. · [source](https://arxiv.org/html/2206.02096v2) |
| Protein stability* | TAPE / Rocklin stability | Running or queued · 0.0% trajectories uploaded* · Ready | — | Spearman: ProtST-ESM-2 0.738; ESM-2 0.718. · [source](https://arxiv.org/html/2206.02096v2) |
| Protein thermostability prediction* | FLIP — AAV and Meltome<br>Thermostability — FLIP/Meltome | Partial* · Ready<br>Existing sequence regression runner and native Spearman scorer are available. | **Diagnostic only:** spearman undefined; spearman_parsed_only 0.0254<br>Full native primary metric undefined. | ProtST-ESM-1b: fixed encoder.spearman 0.68; full model tuning.spearman 0.681; Table 2, printed p.6 · [source](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf) |
| Enzyme activity* | Envision β-lactamase — PEER split | Needs data or protocol*<br>Beta-lactamase assay scope and complete native test inputs are not cleared. | — | Spearman: ProtST-ESM-2 0.879; ESM-2 0.867. · [source](https://arxiv.org/html/2206.02096v2) |
| AAV variant fitness prediction* | FLIP — AAV and Meltome<br>AAV variant fitness — FLIP | Needs data or protocol*<br>FLIP AAV test archive and assay-specific input review remain unfinished. | — | Spearman, ProtST-ESM-2 vs ESM-2: AAV 0.825 vs 0.817; Meltome 0.682 vs 0.672. · [source](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf) |
| Protein stability classification* | NatureLM/PEER binarized stability — paper-specific protocol | Needs data or protocol*<br>NatureLM binary stability labels and conversion rule are unrecovered. | — | NatureLM-8x7B: 72.3% accuracy; SFM-Protein-650M: 58.3%, in NatureLM's stability-classification setup. · [source](https://arxiv.org/html/2502.07527v3) |
| Protein production and enzyme conditions | PFMBench production and enzyme-operating panel | Needs data or protocol<br>Needs seven processed splits and assay-specific protocols; resistance endpoints need scope review. | — | ESM2-Adapter, Table 1 means: Optimal_pH Spearman 0.0564; DeepET_Topt Spearman 0.2628; Cloning_CLF AUROC 0.8160; Material_Production Accuracy 0.7982; Enzyme_Eff. Spearman 0.2173; Antib._Res. Accuracy 0.6185; Thermostability AUROC 0.9553 · [source](https://arxiv.org/html/2506.14796v1) |

#### Protein interactions and interfaces

3 dataset groups · results available

| Task | Dataset/protocol | Status / what's missing | Qwen result | Published reference |
|---|---|---|---|---|
| Human protein–protein interaction prediction | Human/Pan and yeast/Guo PPI — PEER<br>Human protein–protein interaction — PEER | Finished · Ready | accuracy 50.2% | BioT5+ (supervised): accuracy 85.09% ± 0.4 percentage points; Table 6 · [source](https://arxiv.org/html/2402.17810v2) |
| Yeast protein–protein interaction prediction | Human/Pan and yeast/Guo PPI — PEER<br>Yeast protein–protein interaction — PEER | Finished · Ready | accuracy 45.2% | BioT5+ (supervised): accuracy 66.16% ± 0.43 percentage points; Table 6 · [source](https://arxiv.org/html/2402.17810v2) |
| Protein and metal interactions | PFMBench protein and metal-interaction panel | Needs data or protocol<br>Needs paired inputs, metal classes and continuous interaction scores. | — | ESM2-Adapter, Table 1 means: Human_PPI AUROC 0.4828; Yeast_PPI AUROC 0.5343; PPI_Affinity Spearman -0.0047; MetalIonBinding Accuracy 0.7066 · [source](https://arxiv.org/html/2506.14796v1) |
| Protein interface contacts | ATOM3D interface contacts (PIP) | Needs additional models/tools<br>Needs a geometry-input adapter and residue-contact probabilities from 3D structures. | — | AUROC: 3D-CNN 0.844; GNN 0.669; non-3D baseline 0.841. · [source](https://arxiv.org/html/2012.04035v3) |

#### Antibody properties

1 dataset group

| Task | Dataset/protocol | Status / what's missing | Qwen result | Published reference |
|---|---|---|---|---|
| Antibody properties | FLAb / FLAb2 antibody property collection | Needs scoring protocol<br>Pin assay-specific splits, units and Qwen ranking scores; fitted antibody models are separate. | — | No version-matched aggregate model score transcribed; repository supplies per-assay zero-/few-shot evaluation outputs. · [source](https://github.com/Graylab/FLAb) |

</details>

<details>
<summary><h2>Protein function, annotations and descriptions</h2></summary>

#### Gene Ontology and enzyme annotation

4 dataset groups · running or queued

| Task | Dataset/protocol | Status / what's missing | Qwen result | Published reference |
|---|---|---|---|---|
| Enzyme Commission annotation* | DeepFRI-derived EC and GO test splits<br>Enzyme Commission labels — DeepFRI split | Running or queued · 0.0% trajectories uploaded* · Ready | — | Fmax, ProtST-ESM-2 vs ESM-2: EC 0.878 vs 0.874; GO-BP 0.482 vs 0.472; GO-MF 0.668 vs 0.662; GO-CC 0.487 vs 0.472. · [source](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf) |
| Gene Ontology: biological process* | DeepFRI-derived EC and GO test splits<br>GO biological process — DeepFRI split | Running or queued · 0.0% trajectories uploaded* · Ready | — | Fmax, ProtST-ESM-2 vs ESM-2: EC 0.878 vs 0.874; GO-BP 0.482 vs 0.472; GO-MF 0.668 vs 0.662; GO-CC 0.487 vs 0.472. · [source](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf) |
| Gene Ontology: molecular function* | DeepFRI-derived EC and GO test splits<br>GO molecular function — DeepFRI split | Running or queued · 0.0% trajectories uploaded* · Ready | — | Fmax, ProtST-ESM-2 vs ESM-2: EC 0.878 vs 0.874; GO-BP 0.482 vs 0.472; GO-MF 0.668 vs 0.662; GO-CC 0.487 vs 0.472. · [source](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf) |
| Gene Ontology: cellular component* | DeepFRI-derived EC and GO test splits<br>GO cellular component — DeepFRI split | Running or queued · 0.0% trajectories uploaded* · Ready | — | Fmax, ProtST-ESM-2 vs ESM-2: EC 0.878 vs 0.874; GO-BP 0.482 vs 0.472; GO-MF 0.668 vs 0.662; GO-CC 0.487 vs 0.472. · [source](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf) |
| Temporal Gene Ontology annotation* | BioReason-Pro temporal GO test | Running or queued · 0.0% trajectories uploaded* · Ready | — | Official repository headline: BioReason-Pro 73.6% Fmax. · [source](https://huggingface.co/datasets/wanglab/bioreason-pro-test-data) |
| Species-held-out Gene Ontology annotation* | Bio-posttrain species-held-out protein GO | Running or queued · 0.0% trajectories uploaded* · Ready | — | Species-held-out GO evaluation is described; a verified numeric result for the exact protein split is not transcribed here. · [source](https://arxiv.org/html/2606.16517v1) |
| Enzyme and Gene Ontology annotation | PFMBench GO/EC annotation panel | Needs data or protocol<br>Needs PFMBench splits, GO/EC vocabularies and native F1 scoring. | — | ESM2-Adapter, Table 1 means: GO-CC F1 0.6130; GO-MF F1 0.6488; GO-BP F1 0.5412; EC F1 0.7379 · [source](https://arxiv.org/html/2506.14796v1) |

#### Protein function descriptions

2 dataset groups · results available

| Task | Dataset/protocol | Status / what's missing | Qwen result | Published reference |
|---|---|---|---|---|
| Protein function description generation | Mol-Instructions — four protein-description subsets<br>Mol-Instructions: Protein function generation | Finished · Ready | rouge1 0.0631; rouge2 0.0139; rougeL 0.0431; rougeLsum 0.0542 | Verified numerical comparator unavailable · [source](https://arxiv.org/html/2306.08018v4) |
| Catalytic activity description generation | Mol-Instructions — four protein-description subsets<br>Mol-Instructions: Catalytic activity generation | Finished · Ready | rouge1 0.0541; rouge2 0.0140; rougeL 0.0396; rougeLsum 0.0473 | Verified numerical comparator unavailable · [source](https://arxiv.org/html/2306.08018v4) |
| Protein domain and motif description generation | Mol-Instructions — four protein-description subsets<br>Mol-Instructions: Domain and motif generation | Finished · Ready | rouge1 0.0354; rouge2 0.0047; rougeL 0.0259; rougeLsum 0.0306 | Verified numerical comparator unavailable · [source](https://arxiv.org/html/2306.08018v4) |
| Protein functional description generation | Mol-Instructions — four protein-description subsets<br>Mol-Instructions: Functional description generation | Finished · Ready | rouge1 0.0800; rouge2 0.0123; rougeL 0.0494; rougeLsum 0.0649 | Verified numerical comparator unavailable · [source](https://arxiv.org/html/2306.08018v4) |
| Protein description generation* | NatureLM's NCBI protein-description holdout | Needs data or protocol*<br>Publisher unchanged; exact temporal test IDs, sequence/reference snapshots, cutoff and ROUGE-L preprocessing remain missing. | — | ROUGE-L: NatureLM-8x7B 0.585; fine-tuned Llama-3-8B 0.324; GPT-4o 0.091. · [source](https://arxiv.org/html/2502.07527v3) |

#### Biochemical reaction classification

1 dataset group · running or queued

| Task | Dataset/protocol | Status / what's missing | Qwen result | Published reference |
|---|---|---|---|---|
| Biochemical reaction classification* | ProtST reaction classification — zero/few-shot | Running or queued · 0.0% trajectories uploaded* · Ready | — | Zero-/few-shot results are reported, but a numeric value for the exact zero-shot reaction setting is not transcribed here. Do not substitute the fully supervised reaction score. · [source](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf) |

#### Evidence support for protein explanations

1 dataset group

| Task | Dataset/protocol | Status / what's missing | Qwen result | Published reference |
|---|---|---|---|---|
| Evidence support for protein-function explanations* | BioReason-Pro explanation review | Needs scoring protocol*<br>Exact explanation subset, expert/LLM-judge rubric and judging setup are not fixed. | — | Repository reports an LLM-judge score of 8/10 and expert preference over UniProt descriptions in 79% of reviewed cases. · [source](https://www.biorxiv.org/content/10.64898/2026.03.19.712954v2.full) |

#### Protein retrieval from descriptions

1 dataset group

| Task | Dataset/protocol | Status / what's missing | Qwen result | Published reference |
|---|---|---|---|---|
| Protein retrieval from functional descriptions* | ProtST text-to-protein retrieval examples | Needs additional models/tools*<br>Native retrieval needs the full search corpus and trained ProtST representation runtime. | — | Selected text-to-protein retrieval and docking case studies are reported; no single fixed-corpus Recall@K benchmark result is transcribed. · [source](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf) |

</details>

<details>
<summary><h2>Mutation effects, fitness and engineering</h2></summary>

#### Mutation-effect explanation

1 dataset group

| Task | Dataset/protocol | Status / what's missing | Qwen result | Published reference |
|---|---|---|---|---|
| Mutation-effect explanation* | MutaDescribe — mutation explanation | Needs data or protocol*<br>MutaDescribe input eligibility and native prompt/scoring review remain incomplete. | — | Main-test average ROUGE-L / BLEU-2 (0–100): MutaPLM 21.34 / 13.61; GPT-4-0613, 5-shot kNN: 12.31 / 9.69. · [source](https://arxiv.org/html/2410.22949v1) |

#### Mutation fitness prediction and ranking

6 dataset groups

| Task | Dataset/protocol | Status / what's missing | Qwen result | Published reference |
|---|---|---|---|---|
| Mutation-effect ranking* | ProteinGym substitutions — historical ProtST evaluation | Needs data or protocol*<br>Pinned ProteinGym assay set and permitted-case review are not prepared. | — | UniProt-level mean Spearman: ProtST-ESM-1b 0.412; ESM-1b 0.358; ESM-1v 0.372; Tranception L without retrieval 0.401. · [source](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf) |
|  | PG-LLM / ProteinGym-LLM — eval-data-v1.2 | On hold*<br>Existing PG-LLM scope remains held after prior flagged-case rejections. | — | No verified release-matched model score was recovered. This does not mean zero performance. · [source](https://raw.githubusercontent.com/rohitarorayyc/proteingym-llm/main/DATA.md) |
| Single-mutant generation* | PFArena — four task settings<br>PFArena T1: single-mutant generation | Needs data or protocol*<br>PFArena exact assay/candidate bundle requires authorized access and case review. | — | Paper's GPT-6 Astra vs ESM-2: T1 Recall@40 0.0254 vs 0.0370; T2 Spearman 0.2726 vs 0.2539; T3 0.3516 vs 0.3128; T4 0.5988 vs 0.3153. · [source](https://arxiv.org/html/2609.28921v1) |
| Multi-mutant ranking without measurements* | PFArena — four task settings<br>PFArena T2: measurement-free multi-mutant ranking | Needs data or protocol*<br>PFArena exact assay/candidate bundle requires authorized access and case review. | — | Paper's GPT-6 Astra vs ESM-2: T1 Recall@40 0.0254 vs 0.0370; T2 Spearman 0.2726 vs 0.2539; T3 0.3516 vs 0.3128; T4 0.5988 vs 0.3153. · [source](https://arxiv.org/html/2609.28921v1) |
| Mutation ranking with anchor measurements* | PFArena — four task settings<br>PFArena T3: anchor-informed ranking | Needs data or protocol*<br>PFArena exact assay/candidate bundle requires authorized access and case review. | — | Paper's GPT-6 Astra vs ESM-2: T1 Recall@40 0.0254 vs 0.0370; T2 Spearman 0.2726 vs 0.2539; T3 0.3516 vs 0.3128; T4 0.5988 vs 0.3153. · [source](https://arxiv.org/html/2609.28921v1) |
| Mutation ranking with single-mutant measurements* | PFArena — four task settings<br>PFArena T4: single-mutant-informed ranking | Needs data or protocol*<br>PFArena exact assay/candidate bundle requires authorized access and case review. | — | Paper's GPT-6 Astra vs ESM-2: T1 Recall@40 0.0254 vs 0.0370; T2 Spearman 0.2726 vs 0.2539; T3 0.3516 vs 0.3128; T4 0.5988 vs 0.3153. · [source](https://arxiv.org/html/2609.28921v1) |
| Mutation and fitness prediction | PFMBench mutation/fitness panel | Needs data or protocol<br>Needs exact PFMBench splits and assay-specific scope review. | — | ESM2-Adapter, Table 1 means: PETA_CHS_SOL Spearman 0.2738; PETA_LGK_SOL Spearman 0.1558; PETA_TEM_SOL Spearman 0.1433; FLIP_AAV Spearman 0.9412; FLIP_GB1 Spearman 0.9517; TAPE_Stab Spearman 0.3211; TAPE_Fluor Spearman 0.6812; BetaLactamase Spearman 0.5740 · [source](https://arxiv.org/html/2506.14796v1) |
| Zero-shot mutation-effect ranking | PFMBench ProteinGym zero-shot protocol | Needs scoring protocol<br>Needs a Qwen mutation-likelihood protocol; ESM2 masked scoring is not equivalent. | — | Table 1 reports pretrained ESM2 ProteinGym Spearman 0.4390; do not compare directly to a different snapshot's score. · [source](https://arxiv.org/html/2506.14796v1) |
| Low-data fitness regression* | MutaPLM low-data fitness regression | Needs additional models/tools*<br>Native low-data protocol requires a task-trained regression head, outside current baseline scope. | — | Low-data regression curves are reported with 192 train / 48 validation examples; no exact assay-specific point estimate is transcribed here. · [source](https://arxiv.org/html/2410.22949v1) |

#### Mutation engineering and optimization

2 dataset groups

| Task | Dataset/protocol | Status / what's missing | Qwen result | Published reference |
|---|---|---|---|---|
| Mutation engineering with a supplied position* | MutaDescribe — mutation engineering<br>MutaDescribe mutation engineering — position supplied | Needs data or protocol*<br>MutaDescribe input eligibility and native prompt/scoring review remain incomplete. | — | MutaPLM vs fine-tuned ESM-2: position known accuracy 53.51% vs 51.43%; position unknown Recall@50 40.94% vs 33.77%. · [source](https://arxiv.org/html/2410.22949v1) |
| Mutation engineering with an unknown position* | MutaDescribe — mutation engineering<br>MutaDescribe mutation engineering — position unknown | Needs data or protocol*<br>MutaDescribe input eligibility and native prompt/scoring review remain incomplete. | — | MutaPLM vs fine-tuned ESM-2: position known accuracy 53.51% vs 51.43%; position unknown Recall@50 40.94% vs 33.77%. · [source](https://arxiv.org/html/2410.22949v1) |
| Protein-sequence optimization against fitness predictors*<br>Predictor-scored optimization; not measured laboratory success. | MutaPLM iterative optimization | Needs scoring protocol*<br>Full-grid Qwen likelihood adapter and fixed fitness-oracle contract are not activated. | — | The paper reports predicted-fitness improvement trajectories across six landscapes; these are oracle-based search outcomes, not experimentally measured hit rates. · [source](https://arxiv.org/html/2410.22949v1) |

#### Binding affinity and immune interactions

3 dataset groups

| Task | Dataset/protocol | Status / what's missing | Qwen result | Published reference |
|---|---|---|---|---|
| Antibody affinity ranking | AbBiBench antibody affinity ranking | Needs scoring protocol<br>Pin the assay snapshot and Qwen ranking protocol; structural reference methods are separate. | — | Current 16-column leaderboard mean Spearman: ProteinMPNN 0.30; ESM-IF1 0.28; AntiFold 0.21; ESM2 0.02. · [source](https://github.com/MSBMI-SAFE/AbBiBench) |
| Peptide–MHC and TCR–pMHC interactions | PFMBench peptide–MHC and TCR–pMHC panel | Needs data or protocol<br>Needs paired sequences, native splits and continuous classification scores. | — | ESM2-Adapter, Table 1 means: Pept.HLA/MHC Aff. AUROC 0.9631; TCR.PMHC Aff. AUROC 0.9312 · [source](https://arxiv.org/html/2506.14796v1) |
| Mutation effects on binding affinity | ATOM3D SKEMPI-derived mutation affinity (MSP) | Needs additional models/tools<br>Needs wild-type/mutant geometry input and a validated structural prediction adapter. | — | AUROC: GNN 0.621; 3D-CNN 0.574. · [source](https://arxiv.org/html/2012.04035v3) |

</details>

<details>
<summary><h2>Scientific evidence and biological knowledge</h2></summary>

#### Biological research question answering

3 dataset groups · results available · partial results*

| Task | Dataset/protocol | Status / what's missing | Qwen result | Published reference |
|---|---|---|---|---|
| Literature evidence question answering* | LAB-Bench — research tasks<br>LAB-Bench / LitQA2 | Partial* · Ready | accuracy 39.1%; precision 41.0%; coverage 95.4% | GPT-5.2: accuracy 45.7%; n=199; Table 1 · [source](https://arxiv.org/html/2606.00902v1) |
| Biological database question answering | LAB-Bench — research tasks<br>LAB-Bench / DbQA | Finished · Ready | accuracy 31.3%; precision 31.8%; coverage 98.5% | GPT-5.2: accuracy 41.7%; n=520; Table 1 · [source](https://arxiv.org/html/2606.00902v1) |
| Supplementary-material question answering | LAB-Bench — research tasks<br>LAB-Bench / SuppQA | Finished · Ready | accuracy 34.1%; precision 35.9%; coverage 95.1% | GPT-5.2: accuracy 48.8%; n=82; Table 1 · [source](https://arxiv.org/html/2606.00902v1) |
| Research figure question answering | LAB-Bench — research tasks<br>LAB-Bench / FigQA | Finished · Ready | accuracy 75.7%; precision 77.0%; coverage 98.3% | GPT-5.2: accuracy 36.5%; n=181; Table 1 · [source](https://arxiv.org/html/2606.00902v1) |
| Research table question answering | LAB-Bench — research tasks<br>LAB-Bench / TableQA | Finished · Ready | accuracy 88.5%; precision 90.0%; coverage 98.4% | GPT-5.2: accuracy 36.9%; n=244; Table 1 · [source](https://arxiv.org/html/2606.00902v1) |
| Biological sequence question answering | LAB-Bench — research tasks<br>LAB-Bench / SeqQA | Finished · Ready | accuracy 12.7%; precision 12.8%; coverage 99.2% | GPT-5.2: accuracy 47.0%; n=600; Table 1 · [source](https://arxiv.org/html/2606.00902v1) |
| Molecular cloning question answering | LAB-Bench — research tasks<br>LAB-Bench / Cloning scenarios | Finished · Ready | accuracy 0.0%; precision 0.0%; coverage 100.0% | GPT-5.2: accuracy 36.4%; n=33; Table 1 · [source](https://arxiv.org/html/2606.00902v1) |
| Protein understanding | ProteinLMBench protein-understanding questions | Needs data or protocol<br>Needs the released questions, held-out manifest and frozen answer parser. | — | InternLM2-7B after SFT: 58.26% accuracy; SSL+SFT: 62.18%. · [source](https://arxiv.org/html/2406.05540v1) |
| Research-abstract question answering | PubMedQA research-abstract questions | Needs data or protocol<br>Needs the official test split; exclude conclusions from question/abstract inputs. | — | Original BioBERT multi-phase training: 68.1% accuracy; reported human baseline 78.0%. Historical results. · [source](https://arxiv.org/abs/1909.06146) |
| Experimental protocol question answering* | LAB-Bench — research tasks<br>LAB-Bench / ProtocolQA | On hold*<br>ProtocolQA remains under the explicit input-review hold. | — | Historical 2024 GPT-4o accuracy: LitQA2 27%; SuppQA 13%; FigQA 29%; TableQA 71%; ProtocolQA 53%; Cloning 28%. DbQA variant-from-sequence 42%; SeqQA GC% 29%, ORF-sequence 50% (SUBTASK values only). · [source](https://arxiv.org/html/2407.10362v1) |

</details>

<details>
<summary><h2>Protein design</h2></summary>

#### Protein sequence and structure generation

5 dataset groups · running or queued

| Task | Dataset/protocol | Status / what's missing | Qwen result | Published reference |
|---|---|---|---|---|
| Text-conditioned protein-sequence design*<br>Lexical sequence overlap; biological function untested. | BioT5+ description-guided protein generation | Running partial subset · 20.3% trajectories uploaded* · Ready | [59-case reviewed subset](https://github.com/Some-random/bio-evaluation/tree/main/results/runs/p36-qwen3.8-27b-biot5-reviewed59-20261016). Full benchmark incomplete. | Description-guided protein designs are presented as qualitative cases rather than a fixed, experimentally validated design-success rate. · [source](https://arxiv.org/html/2402.17810v2) |
| Unconditional protein backbone generation | ProteinBench unconditional backbone generation | Needs additional models/tools<br>Needs backbone coordinate generation, inverse folding and refolding checks. | — | At length 100: RFdiffusion scTM 0.98 ± 0.12 and scRMSD 0.48 ± 0.56 Å; FrameFlow 0.94 ± 0.08 and 0.70 ± 0.70 Å. · [source](https://arxiv.org/html/2409.06744v2) |
| Unconditional protein sequence generation | ProteinBench unconditional sequence generation | Needs additional models/tools<br>Qwen can propose sequences; native scoring still needs a fixed folding evaluator. | — | At length 100, predicted AF2 pLDDT: DPLM-650M 85.38 ± 14.20; ProGen2-700M 64.00 ± 21.26. · [source](https://arxiv.org/html/2409.06744v2) |
| Joint sequence and structure generation | ProteinBench joint sequence–structure generation | Needs additional models/tools<br>Needs joint sequence/coordinate generation and structural consistency evaluators. | — | Multiflow at length 100: scTM 0.96 ± 0.04; scRMSD 1.10 ± 0.71 Å. At length 200: scTM 0.95; scRMSD 1.61 Å. · [source](https://arxiv.org/html/2409.06744v2) |
| Unconditional protein generation*<br>Structure quality is predicted; function is not experimentally established. | NatureLM generated proteins: unconditional / property-conditioned / heme<br>NatureLM unconditional generation | Needs additional models/tools*<br>OmegaFold evaluator, clustering settings and native generation/reference cohort remain unprepared. | — | Reported outputs are diversity/length distributions and predicted structural confidence. No experimentally measured function-success fraction is supplied by this evaluation. The reported comparison uses learned stability/solubility scores and diversity. No measured stability/solubility success rate is transcribed. Selected heme-binding candidates are screened with descriptions and predicted complexes; this is not experimentally demonstrated heme binding. · [source](https://arxiv.org/html/2502.07527v3) |
| Protein generation for predicted stability and solubility*<br>Stability and solubility are predicted, not measured. | NatureLM generated proteins: unconditional / property-conditioned / heme<br>NatureLM stability/solubility-conditioned generation | Needs additional models/tools*<br>Exact trained stability/solubility classifiers and native reference/sampling rules are missing. | — | Reported outputs are diversity/length distributions and predicted structural confidence. No experimentally measured function-success fraction is supplied by this evaluation. The reported comparison uses learned stability/solubility scores and diversity. No measured stability/solubility success rate is transcribed. Selected heme-binding candidates are screened with descriptions and predicted complexes; this is not experimentally demonstrated heme binding. · [source](https://arxiv.org/html/2502.07527v3) |
| Heme-binding protein candidate generation*<br>Heme binding is a predicted candidate property, not demonstrated binding. | NatureLM generated proteins: unconditional / property-conditioned / heme<br>NatureLM heme-binding case study | Needs additional models/tools*<br>Protenix complex evaluation and native heme-candidate selection protocol are unrecovered. | — | Reported outputs are diversity/length distributions and predicted structural confidence. No experimentally measured function-success fraction is supplied by this evaluation. The reported comparison uses learned stability/solubility scores and diversity. No measured stability/solubility success rate is transcribed. Selected heme-binding candidates are screened with descriptions and predicted complexes; this is not experimentally demonstrated heme binding. · [source](https://arxiv.org/html/2502.07527v3) |

#### GFP sequence optimization

1 dataset group · partial results*

| Task | Dataset/protocol | Status / what's missing | Qwen result | Published reference |
|---|---|---|---|---|
| GFP sequence optimization against a fluorescence predictor*<br>Scored by a fluorescence predictor; not a wet-lab result. | STRIDE GFP sequence optimization | Partial* · Ready<br>Qualified GFP generation and frozen trained SaProt CPU evaluator are prepared. | replace_only.qualified_oracle_success 0.0000; replace_only.improved_sequence_uniqueness undefined; replace_only.native_novelty undefined; full_atomic.qualified_oracle_success 0.0000; full_atomic.improved_sequence_uniqueness undefined; full_atomic.native_novelty undefined | STRIDE: success count 61; attempt count 100; unique improved count 59; n=100; Table 4 · [source](https://arxiv.org/html/2603.03573v1) |

#### Antibody design

4 dataset groups

| Task | Dataset/protocol | Status / what's missing | Qwen result | Published reference |
|---|---|---|---|---|
| Antibody design: CDR-H3 redesign* | RAbD — CDR-H3 redesign | Needs additional models/tools*<br>Processed RAbD contexts and the coordinate/geometry evaluation pipeline are missing. | — | Proteo-R1 vs BoltzGen: AAR 10.75% vs 39.07%; RMSD 2.46 Å vs 2.69 Å; DockQ 0.801 vs 0.473. · [source](https://arxiv.org/html/2605.02937v1) |
|  | ProteinBench antibody design — processed RAbD | Needs additional models/tools<br>Needs complex-geometry conditioning, loop reconstruction and structural scoring. | — | DiffAb: AAR 35.04 ± 8.36%, RMSD 2.53 ± 0.60 Å; MEAN: AAR 33.47%, RMSD 1.82 Å. · [source](https://arxiv.org/html/2409.06744v2) |
| Antibody design: multi-CDR redesign* | SAbDab — Proteo-R1 all-CDR holdout | Needs additional models/tools*<br>All-CDR holdout, specialist structure runtime and complete structural scorer are unreleased or unprepared. | — | Proteo-R1 vs MFDesign: H3 RMSD 3.81 Å vs 3.71 Å; Loop-RMSD 4.51 Å vs 4.28 Å; IMP 56.58 vs 59.16 (paper's scale). · [source](https://arxiv.org/html/2605.02937v1) |
| Antibody design: epitope-conditioned design | CHIMERA-Bench epitope-conditioned antibody design | Needs additional models/tools<br>Needs geometry-conditioned CDR design and docking/contact evaluation. | — | Epitope-group H3: RAAD AAR 0.37, RMSD 1.75 Å, DockQ 0.58; dyMEAN EpiF1 0.23 (RAAD 0.11). · [source](https://arxiv.org/html/2603.13431v1) |

#### Inverse folding

2 dataset groups

| Task | Dataset/protocol | Status / what's missing | Qwen result | Published reference |
|---|---|---|---|---|
| Sequence design by inverse folding | CATH 4.2 / TS50 / TS500 inverse folding | Needs additional models/tools<br>Needs a coordinate-conditioned inverse-folding adapter and retained structure manifests. | — | PiFold repository: CATH recovery 51.66%; TS50 58.72%; TS500 60.42%. · [source](https://github.com/a4bio/pifold) |
|  | ProteinBench inverse folding — CASP15 / CAMEO / synthetic backbones | Needs additional models/tools<br>Needs coordinate-conditioned inverse folding and structure-consistency evaluators. | — | AAR, CASP15/CAMEO: LM-Design 0.516/0.570; ProteinMPNN 0.450/0.468. · [source](https://arxiv.org/html/2409.06744v2) |

#### Functional-motif scaffolding

2 dataset groups

| Task | Dataset/protocol | Status / what's missing | Qwen result | Published reference |
|---|---|---|---|---|
| Functional-motif scaffolding | MotifBench functional-motif scaffolding | Needs additional models/tools<br>Needs motif-coordinate conditioning, scaffold generation and structural verification. | — | Official leaderboard snapshot: RFdiffusion3 43.52 ± 1.35 (Aug 2026); RFdiffusion 21.95 (Feb 2025), in MotifBench-score units. · [source](https://github.com/blt2114/MotifBench) |
|  | ProteinBench motif scaffolding — legacy motif panel | Needs additional models/tools<br>Needs the legacy motif manifest and a geometry-conditioned design/refolding pipeline. | — | Comparative motif-scaffolding results are reported; exact figure-derived score not transcribed. · [source](https://arxiv.org/html/2409.06744v2) |

#### Target-binder design

2 dataset groups

| Task | Dataset/protocol | Status / what's missing | Qwen result | Published reference |
|---|---|---|---|---|
| Target-binder design | ProtDBench de novo target-binder design | Needs additional models/tools<br>Needs target-geometry design, inverse folding and structural filtering under the native time budget. | — | PD-L1 passing-backbone counts: PXDesign 1,247; BoltzGen 549; RFdiffusion3 542; BindCraft 231. TNFα: PXDesign 57; BoltzGen 15. · [source](https://arxiv.org/html/2605.04118v1) |
| GM2A-targeted binder design<br>Single published target campaign. | Prompteina text-conditioned protein design — GM2A campaign | Needs additional models/tools<br>Native binder/KD results require structural selection plus expression and binding assays. | — | 9 of 89 assayed designs classified as binders; 8 fitted apparent KD values. Strongest apparent KD: 107 nM. · [source](https://arxiv.org/html/2610.13917v1) |

</details>

<details>
<summary><h2>Structure and conformational prediction</h2></summary>

#### Local structure and residue prediction

2 dataset groups

| Task | Dataset/protocol | Status / what's missing | Qwen result | Published reference |
|---|---|---|---|---|
| Structure-derived protein prediction | PFMBench structure-derived prediction panel | Needs data or protocol<br>Needs output schemas and native splits; contact-map size must fit the frozen output budget. | — | ESM2-Adapter, Table 1 means: Contact Top L/5 0.7199; FoldClass Accuracy 0.7859; SecondaryStructure Accuracy 0.7601 · [source](https://arxiv.org/html/2506.14796v1) |
| Residue identity from local structure | ATOM3D residue identity from local structure (RES) | Needs additional models/tools<br>Needs a validated adapter for masked 3D atomic environments. | — | ATOM3D 3D-CNN test accuracy: 0.451. · [source](https://arxiv.org/html/2012.04035v3) |

#### Structure-derived questions and output checks

1 dataset group

| Task | Dataset/protocol | Status / what's missing | Qwen result | Published reference |
|---|---|---|---|---|
| Structure-derived questions and output-format checks<br>Independent held-out questions remain unresolved. | Proteo-R1 internal alignment / structural / CDR diagnostics | Needs data or protocol<br>Needs an independent held-out manifest, allowed inputs and per-task scoring schemas. | — | Selected Stage-II M3: contact 58.3%; interface 15.1%; hotspot 11.6%. Separate Stage-I schema 81.4%. No overall score. · [source](https://arxiv.org/html/2605.02937v1) |

#### Protein structure ranking

1 dataset group

| Task | Dataset/protocol | Status / what's missing | Qwen result | Published reference |
|---|---|---|---|---|
| Protein structure ranking | ATOM3D protein structure ranking (PSR) | Needs additional models/tools<br>Needs structural-quality scoring from decoy coordinates and the exact manifest. | — | Per-target mean Spearman: GNN 0.515; 3D-CNN 0.431. Global correlations are different metrics. · [source](https://arxiv.org/html/2012.04035v3) |

#### Protein folding

1 dataset group

| Task | Dataset/protocol | Status / what's missing | Qwen result | Published reference |
|---|---|---|---|---|
| Single-state protein folding | ProteinBench single-state folding — CAMEO 2022 | Needs additional models/tools<br>Needs a folding model and the native MSA/template-access protocol. | — | AF2 mean/median TM-score 0.871/0.952, RMSD 3.21/1.64 Å; ESMFold 0.847/0.929 and 3.98/2.10 Å. · [source](https://arxiv.org/html/2409.06744v2) |

#### Protein conformations and dynamics

3 dataset groups

| Task | Dataset/protocol | Status / what's missing | Qwen result | Published reference |
|---|---|---|---|---|
| Multistate protein conformations | ProteinBench multistate conformations — apo/holo and BPTI | Needs additional models/tools<br>Needs 3D conformational ensemble generation and structural evaluation. | — | Apo/holo TM-ensemble: AlphaFlow-PDB 0.873; MSA-depth256 0.867. BPTI N=1000: ConfDiff-ESM-force ensemble RMSD 1.36 Å. · [source](https://arxiv.org/html/2409.06744v2) |
| Protein conformational ensembles | ProteinBench ensemble distribution — ATLAS | Needs additional models/tools<br>Needs ensemble coordinates, MD references and distributional scoring tools. | — | AlphaFlow-MD: per-target RMSF correlation 0.85 and PCA-Wasserstein 1.55; ConfDiff PCA-Wasserstein 1.41 (paper's units). · [source](https://arxiv.org/html/2409.06744v2) |
| Protein states, dynamics and free energy | BioEmu benchmark collection — states, dynamics and free energy | Needs additional models/tools<br>Needs a conformational sampler and version-pinned state/dynamics/free-energy evaluation. | — | Official model card: domain-motion coverage 83%; cryptic-pocket apo/holo coverage 55%/88%; experimental stability MAE ~0.9 kcal/mol, Spearman ~0.6. · [source](https://github.com/microsoft/bioemu/blob/main/MODEL_CARD.md) |

</details>

<details>
<summary><h2>Biomedical visual evidence</h2></summary>

#### Biomedical visual question answering

1 dataset group · results available

| Task | Dataset/protocol | Status / what's missing | Qwen result | Published reference |
|---|---|---|---|---|
| Radiology image question answering | Biomedical VQA: VQA-RAD / SLAKE-English / PathVQA / VQA-Med 2019<br>VQA-RAD | Finished · Ready | open_token_recall 59.5%; closed_accuracy 86.8% | LLaVA-Med 7B, CLIP, 60K-IM, stage1=1/stage2=3/FT=0: open token recall 28.23%; closed accuracy 61.4%; n=451; Table 4(b), PDF p.9 · [source](https://arxiv.org/pdf/2306.00890) |
| Medical image question answering in English | Biomedical VQA: VQA-RAD / SLAKE-English / PathVQA / VQA-Med 2019<br>SLAKE — English | Finished · Ready | open_token_recall 51.0%; closed_accuracy 84.6% | LLaVA-Med 7B, CLIP, 60K-IM, stage1=1/stage2=3/FT=0: open token recall 39.17%; closed accuracy 52.16%; n=1061; Table 4(b), PDF p.9 · [source](https://arxiv.org/pdf/2306.00890) |
| Pathology image question answering | Biomedical VQA: VQA-RAD / SLAKE-English / PathVQA / VQA-Med 2019<br>PathVQA | Finished · Ready | open_token_recall 26.4%; closed_accuracy_corrected 0.8587 | LLaVA-Med 7B, CLIP, 60K-IM, stage1=1/stage2=3/FT=0: open token recall 12.3%; closed accuracy 54.05%; n=6761; Table 4(b), PDF p.9 · [source](https://arxiv.org/pdf/2306.00890) |
| Medical image question answering | Biomedical VQA: VQA-RAD / SLAKE-English / PathVQA / VQA-Med 2019<br>ImageCLEF-VQA 2019 | Finished · Ready | strict_accuracy 0.0% | MedVInT-TE: overall accuracy 70.5%; Table 2 · [source](https://arxiv.org/html/2305.10415v6) |

#### Scientific figures, documents and visual conversations

3 dataset groups · results available

| Task | Dataset/protocol | Status / what's missing | Qwen result | Published reference |
|---|---|---|---|---|
| Scientific figure question answering | PMC-VQA figure question answering | Finished · Ready | native_td_final_character_accuracy 0.0200; adapted_full_text_closest_choice_accuracy 0.4975; adapted_full_text_released_label_accuracy 0.4975; strict_final_label_accuracy 0.0070 | MedVInT-TD / PMC-LLaMA / PMC-CLIP: choice accuracy 40.3%; blank accuracy 33.6%; blank bleu1 21.5%; n=2000; Table 3 · [source](https://arxiv.org/html/2305.10415v6) |
| Biomedical visual conversations* | LLaVA-Med biomedical visual conversations | Needs scoring protocol*<br>193 questions mapped and 19/50 images recovered; remaining images and native GPT-4 judging are blocked. | — | GPT-assisted relative answer-quality comparisons are reported. A verified single aggregate for the specified qa50 setting is not transcribed here. · [source](https://arxiv.org/abs/2306.00890) |
| Scientific document and figure extraction* | Ryze document-extraction component tests | Needs data or protocol*<br>Publisher unchanged; exact component IDs, original media/page mapping and Table 3 pipeline/scoring contract remain missing. | — | Ryze extraction-component accuracy: ArXivQA 73.12%, SlideVQA 66.48%, ChartQA 75.8%. · [source](https://arxiv.org/html/2606.00902v1) |

</details>

<details>
<summary><h2>Other biological modalities and molecular interactions</h2></summary>

#### Molecular interactions and binding affinity

4 dataset groups · results available

| Task | Dataset/protocol | Status / what's missing | Qwen result | Published reference |
|---|---|---|---|---|
| Drug–target interaction | Drug–target interaction: BioSNAP / Human / BindingDB<br>Drug–target interaction — BioSNAP/Human/BindingDB · bindingdb | Finished · Ready | AUROC 0.5036; AP 0.4103 | BioT5+ (supervised): AUROC 0.964 ± 0.001; Table 8 · [source](https://arxiv.org/html/2402.17810v2) |
|  | Drug–target interaction: BioSNAP / Human / BindingDB<br>Drug–target interaction — BioSNAP/Human/BindingDB · biosnap | Finished · Ready | AUROC 0.5336; AP 0.5217 | BioT5+ (supervised): AUROC 0.939 ± 0.001; Table 8 · [source](https://arxiv.org/html/2402.17810v2) |
|  | Drug–target interaction: BioSNAP / Human / BindingDB<br>Drug–target interaction — BioSNAP/Human/BindingDB · human | Finished · Ready | AUROC 0.4747; AP 0.4194 | BioT5+ (supervised): AUROC 0.987 ± 0.001; Table 8 · [source](https://arxiv.org/html/2402.17810v2) |
| Protein–ligand binding affinity | PFMBench PDBbind / BindingDB affinity panel | Needs data or protocol<br>Needs native partner encodings, processed splits and affinity target transformations. | — | ESM2-Adapter, Table 1 means: PDBBind Spearman 0.1677; BindingDB Spearman 0.1922 · [source](https://arxiv.org/html/2506.14796v1) |
|  | ATOM3D protein–ligand affinity (LBA) | Needs additional models/tools<br>Needs protein-ligand geometry input and a validated affinity-scoring adapter. | — | 3D-CNN: RMSE 1.416, Spearman 0.553; GNN: RMSE 1.570, Spearman 0.628. · [source](https://arxiv.org/html/2012.04035v3) |
| Ligand efficacy | ATOM3D ligand efficacy (LEP) | Needs additional models/tools<br>Needs receptor/ligand conformation input and structural efficacy prediction. | — | AUROC: GNN 0.740; 3D-CNN 0.589. · [source](https://arxiv.org/html/2012.04035v3) |

#### Pathway and disease prediction

2 dataset groups · results available

| Task | Dataset/protocol | Status / what's missing | Qwen result | Published reference |
|---|---|---|---|---|
| Pathway and disease prediction | BioReason KEGG pathway/disease | Finished · Ready | accuracy 0.0%; STRICT_FINAL_LABEL.accuracy 0.0%; STRICT_FINAL_LABEL.supplemental_macro_f1_fixed_global_vocabulary 0.0000; STRICT_FINAL_LABEL.supplemental_macro_precision_fixed_global_vocabulary 0.0000; STRICT_FINAL_LABEL.supplemental_macro_recall_fixed_global_vocabulary 0.0000 | Qwen3-4B: accuracy 90.0%; macro f1 79.66%; macro precision 88.24%; n=290; Table 1 · [source](https://arxiv.org/html/2505.23579v2) |
| Network-held-out pathway prediction* | Bio-posttrain KEGG unseen-network holdout | Needs data or protocol*<br>Exact network-held-out CSVs and network assignments are inaccessible. | — | Qwen3-4B DNA OOD accuracy: SFT 0.753; SFT+RL 0.917; biology-CPT+SFT+RL 0.970. · [source](https://arxiv.org/html/2606.16517v1) |

#### Variant-effect prediction

1 dataset group · results available

| Task | Dataset/protocol | Status / what's missing | Qwen result | Published reference |
|---|---|---|---|---|
| Coding-variant effect prediction | BioReason VEP coding and non-SNV<br>BioReason VEP-Coding | Finished · Ready | accuracy 49.1%; f1 0.5213; STRICT_FINAL_LABEL.accuracy 0.0%; STRICT_FINAL_LABEL.f1 0.0000 | Qwen3-4B: accuracy 48.99%; f1 39.58%; Table 2 · [source](https://arxiv.org/html/2505.23579v2) |
| Non-SNV variant effect prediction | BioReason VEP coding and non-SNV<br>BioReason VEP-Non-SNV | Finished · Ready | accuracy 89.0%; f1 0.9053; STRICT_FINAL_LABEL.accuracy 0.0%; STRICT_FINAL_LABEL.f1 0.0000 | Qwen3-4B: accuracy 61.86%; f1 67.6%; n=873; Table 2 · [source](https://arxiv.org/html/2505.23579v2) |

#### Expression-conditioned gene selection

1 dataset group

| Task | Dataset/protocol | Status / what's missing | Qwen result | Published reference |
|---|---|---|---|---|
| Expression-conditioned gene selection* | Bio-posttrain MEDEA expression-conditioned gene selection | Needs additional models/tools*<br>TranscriptFormer/projector inputs and exact MEDEA adaptation/split alignment are missing. | — | The paper reports RNA target-selection ID/OOD experiments. An exact numeric result is not transcribed in this table. · [source](https://arxiv.org/html/2606.16517v1) |

#### RNA structure ranking

1 dataset group

| Task | Dataset/protocol | Status / what's missing | Qwen result | Published reference |
|---|---|---|---|---|
| RNA structure ranking | ATOM3D RNA structure ranking (RSR) | Needs additional models/tools<br>Needs RNA-decoy coordinate input and structural-quality scoring. | — | Mean per-target Spearman: 3D-CNN 0.264; GNN 0.234. · [source](https://arxiv.org/html/2012.04035v3) |

#### Small-molecule properties

1 dataset group

| Task | Dataset/protocol | Status / what's missing | Qwen result | Published reference |
|---|---|---|---|---|
| Small-molecule properties | ATOM3D small-molecule properties (SMP / QM9) | Needs additional models/tools<br>Needs atomic-geometry input and property-specific molecular regression. | — | ENN dipole MAE 0.052 D; 3D-CNN 0.754 D. Property-specific scores must remain separate. · [source](https://arxiv.org/html/2012.04035v3) |

</details>

<details>
<summary>Protocol notes and sources</summary>

## Protein properties, interactions and developability

#### Protein solubility

#### DeepSol solubility — PEER split

Task-trained models; BioT5+ is multitask and BioT5 single-task. Count is PEER's published split, not a new loader count.

Published source size/units: Test: 1,999 proteins. Train: 62,478; validation: 6,942 (PEER Table 1).

**Protein solubility:** Accuracy. Preserve the official PEER solubility split; exact test size not re-established.

Not binding affinity, thermostability, or a guarantee of solubility under every laboratory condition.

**Protein solubility — Runnable now:** An existing completed declared Qwen run demonstrates that the input interface, execution harness and scorer can be used in this environment. This is readiness of the documented qualified baseline, not a claim of strong performance or full paper replication.

Model compatibility: compatible

Evidence:

```json
[
  "reports/RESULTS_AT_A_GLANCE.json"
]
```

##### Solubility — PEER

**Native/local protocol:** `QWEN_FULL_SEQUENCE_TEXT_BIOT5_TEST`

**Coverage:** full_frozen_reviewed_case_set; completed_declared_run.

**Saved count record:**

```json
{
  "planned": 1999,
  "completed": 1999,
  "parsed": 930,
  "invalid_outputs": 1069,
  "missing_or_failed_outputs": 0,
  "held_before_inference": 0
}
```

**Complete stored metrics, including alternate/diagnostic values:**

```json
{
  "accuracy": 0.24212106053026514,
  "correct": 484,
  "planned": 1999,
  "parsed": 930,
  "missing": 0,
  "invalid": 1069,
  "all_case_rule": "Missing or invalid model answers count as incorrect; report transport failures separately."
}
```

**Comparison qualification:** Native source outcome, data split and metric when separately verified; prompted zero-shot full-sequence Qwen baseline, not matched specialist training. No native BioT5 special-token architecture or fitted regression/classification head reproduced.

**All stored published-reference records — separate from the local run:**

```json
[
  {
    "model": "BioT5+",
    "metrics": {
      "accuracy_percent": 74.37
    },
    "source_id": "BIOT5",
    "source_url": "https://arxiv.org/html/2402.17810v2",
    "source_locator": "Table 6",
    "protocol": "supervised multitask instruction tuning on official PEER splits",
    "value_status": "published_rounded_as_printed",
    "run_count": null,
    "reported_std": {
      "accuracy_percent": 0.19
    },
    "uncertainty_note": "Table prints mean ± dispersion; number of runs/dispersion definition not independently re-established here."
  },
  {
    "model": "NatureLM",
    "metrics": {
      "1B_accuracy": 0.684,
      "8B_accuracy": 0.714,
      "8x7B_accuracy": 0.698
    },
    "source_id": "NATURE",
    "source_url": "https://arxiv.org/html/2502.07527v3",
    "source_locator": "Table 20, Section 7.2",
    "protocol": "task-trained scientific model; adopted PEER splits",
    "value_status": "published_rounded_as_printed",
    "run_count": null,
    "reported_std": null
  }
]
```

[Original score artifact](https://github.com/Some-random/bio-evaluation/blob/main/results/runs/qwen38_27b_p01_original_test_2026-10-15/scores.json)

[Source 1](https://arxiv.org/html/2206.02096v2), [Source 2](https://arxiv.org/html/2402.17810v2), [Source 3](https://github.com/DeepGraphLearning/PEER_Benchmark)

#### PFMBench solubility panel

These are PFMBench-specific processed datasets/splits, not interchangeable with PEER/ProtST results. F1 is not Fmax. Affinity-named AUROC tasks are classification, not KD regression. Exact loaders required.

Published source size/units: Test sizes: DeepSol: 6,934; DeepSoluE: 1,454; ProtSolM: 7,173; eSOL: 311

**Protein solubility — Needs data or protocol:** Sequence input and solubility labels/scores fit a Qwen zero-shot adaptation. The four PFMBench processed datasets, splits and AUROC/regression contracts are not prepared; the reported ESM2-Adapter training regime would not be reproduced.

Model compatibility: compatible

Evidence:

```json
[
  "reports/TASK_HIERARCHY_DATA.json",
  "handoff/Bio_Evaluation_Agent_Package_2026-10-16/EVALUATION_INVENTORY.csv",
  "reports/local_model_capability_smoke.json"
]
```

Published reference record: ESM2-Adapter, Table 1 means: DeepSol AUROC 0.8467; DeepSoluE AUROC 0.7699; ProtSolM AUROC 0.8572; eSOL Spearman 0.2761

[Source 1](https://arxiv.org/html/2506.14796v1), [Source 2](https://github.com/biomap-research/PFMBench)

#### Protein localization

#### DeepLoc — binary and 10-compartment localization

Binary comparison uses task-tuned systems. Ten-class numbers use frozen encoders + trained heads. These are distinct endpoints.

Published ten-class count is 2,768; the frozen local run contains 2,773 cases. These source-specific counts are retained separately.

Published source size/units: Published PEER test counts: binary 1,746; 10-compartment 2,768.

**Binary protein localization:** Accuracy. Binary task; do not substitute the separate ten-compartment label set.

'Soluble' in the localization labels is not the same endpoint as expression solubility in P01.

**Ten-compartment protein localization:** Accuracy. Official DeepLoc split. ProtST also tests zero-/few-shot transfer; record shots and whether a supervised head is fitted.

Location is a different question from molecular activity or binding specificity.

**Binary protein localization — Runnable now:** An existing completed declared Qwen run demonstrates that the input interface, execution harness and scorer can be used in this environment. This is readiness of the documented qualified baseline, not a claim of strong performance or full paper replication.

Model compatibility: compatible

Evidence:

```json
[
  "reports/RESULTS_AT_A_GLANCE.json"
]
```

**Ten-compartment protein localization — Runnable now:** Complete task inputs, a named frozen Qwen protocol and native/qualified scorer are prepared in the sealed current execution plan. Already running or queued; output validity and eventual score are not guaranteed.

Model compatibility: compatible

Evidence:

```json
[
  "reports/CURRENT_EXECUTION_STATUS_2026-10-16.json",
  ".local/remaining_evaluations/supervisor_plan.json",
  ".local/remaining_evaluations/launch_summary.json"
]
```

##### Binary localization — DeepLoc/PEER

**Native/local protocol:** `QWEN_FULL_SEQUENCE_TEXT_BIOT5_TEST`

**Coverage:** full_frozen_reviewed_case_set; completed_declared_run.

**Saved count record:**

```json
{
  "planned": 1749,
  "completed": 1749,
  "parsed": 1496,
  "invalid_outputs": 253,
  "missing_or_failed_outputs": 0,
  "held_before_inference": 0
}
```

**Complete stored metrics, including alternate/diagnostic values:**

```json
{
  "accuracy": 0.27387078330474557,
  "correct": 479,
  "planned": 1749,
  "parsed": 1496,
  "missing": 0,
  "invalid": 253,
  "all_case_rule": "Missing or invalid model answers count as incorrect; report transport failures separately."
}
```

**Comparison qualification:** Native source outcome, data split and metric when separately verified; prompted zero-shot full-sequence Qwen baseline, not matched specialist training. No native BioT5 special-token architecture or fitted regression/classification head reproduced.

**All stored published-reference records — separate from the local run:**

```json
[
  {
    "model": "BioT5+",
    "metrics": {
      "accuracy_percent": 90.41
    },
    "source_id": "BIOT5",
    "source_url": "https://arxiv.org/html/2402.17810v2",
    "source_locator": "Table 6",
    "protocol": "supervised multitask instruction tuning on official PEER splits",
    "value_status": "published_rounded_as_printed",
    "run_count": null,
    "reported_std": {
      "accuracy_percent": 0.07
    },
    "uncertainty_note": "Table prints mean ± dispersion; number of runs/dispersion definition not independently re-established here."
  },
  {
    "model": "ProtST-ESM-1b",
    "metrics": {
      "fixed_encoder": {
        "accuracy_percent": 92.87
      },
      "full_model_tuning": {
        "accuracy_percent": 92.35
      }
    },
    "source_id": "PROTST",
    "source_url": "https://proceedings.mlr.press/v202/xu23t/xu23t.pdf",
    "source_locator": "Table 2, printed p.6",
    "protocol": "two-layer MLP trained on official task split; frozen encoder and full tuning are separate regimes",
    "value_status": "published_rounded_as_printed",
    "run_count": null,
    "reported_std": null
  }
]
```

[Original score artifact](https://github.com/Some-random/bio-evaluation/blob/main/results/runs/qwen38_27b_p02_original_test_2026-10-15/scores.json)

[Source 1](https://arxiv.org/html/2206.02096v2), [Source 2](https://arxiv.org/html/2402.17810v2), [Source 3](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf), [Source 4](https://github.com/DeepGraphLearning/PEER_Benchmark), [Source 5](https://github.com/DeepGraphLearning/ProtST)

#### PFMBench localization and sorting-signal panel

These are PFMBench-specific processed datasets/splits, not interchangeable with PEER/ProtST results. F1 is not Fmax. Affinity-named AUROC tasks are classification, not KD regression. Exact loaders required.

Published source size/units: Test sizes: DeepLocMulti: 751; DeepLoc2Multi: 2,744; DeepLocBinary: 848; SortingSignal: 186

**Localization and sorting signals — Needs data or protocol:** Sequence-to-label prediction is compatible with a Qwen adaptation. Exact PFMBench splits, localization/sorting label vocabularies and binary versus multilabel score formats must be prepared; the existing PEER/DeepLoc runs do not supply these distinct protocols.

Model compatibility: compatible

Evidence:

```json
[
  "reports/TASK_HIERARCHY_DATA.json",
  "handoff/Bio_Evaluation_Agent_Package_2026-10-16/EVALUATION_INVENTORY.csv",
  "reports/local_model_capability_smoke.json"
]
```

Published reference record: ESM2-Adapter, Table 1 means: DeepLocMulti Accuracy 0.7666; DeepLoc2Multi F1 0.7505; DeepLocBinary AUROC 0.9338; SortingSignal F1 0.8598

[Source 1](https://arxiv.org/html/2506.14796v1), [Source 2](https://github.com/biomap-research/PFMBench)

#### Protein activity, stability and production

#### Envision β-lactamase — PEER split

Full-model supervised fine-tuning. Assay-specific ranking, not an overall biology score.

Published source size/units: Test: 520 variants. Train: 4,158; validation: 520.

**Enzyme activity:** Spearman correlation. Official PEER beta-lactamase split.

The numerical endpoint is assay-specific; these tasks do not establish a general ability to explain mechanisms.

**Enzyme activity — Needs data or protocol:** A numeric Qwen sequence-prediction baseline is interface-compatible, but the exact beta-lactamase assay/case eligibility and complete frozen inputs are not prepared. Existing flagged resistance-related restrictions remain; this finding does not authorize those cases.

Model compatibility: compatible

Evidence:

```json
[
  "reports/catalog_execution_review_2026-10-15.json",
  ".local/remaining_evaluations/catalog_plan.json"
]
```

Published reference record: Spearman: ProtST-ESM-2 0.879; ESM-2 0.867.

[Source 1](https://arxiv.org/html/2206.02096v2), [Source 2](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf), [Source 3](https://github.com/DeepGraphLearning/PEER_Benchmark)

#### TAPE GFP / Sarkisyan fluorescence

Full-model supervised fine-tuning. Source counts are the TAPE split documented in PEER, not STRIDE's generated batch.

Published source size/units: Test: 27,217 variants. Train: 21,446; validation: 5,362.

**Protein fluorescence:** Spearman correlation. TAPE fluorescence split; sequence-distance extrapolation is part of the benchmark.

The numerical endpoint is assay-specific; these tasks do not establish a general ability to explain mechanisms.

**Protein fluorescence — Runnable now:** Complete task inputs, a named frozen Qwen protocol and native/qualified scorer are prepared in the sealed current execution plan. Already running or queued; output validity and eventual score are not guaranteed.

Model compatibility: compatible

Evidence:

```json
[
  "reports/CURRENT_EXECUTION_STATUS_2026-10-16.json",
  ".local/remaining_evaluations/supervisor_plan.json",
  ".local/remaining_evaluations/launch_summary.json"
]
```

Published reference record: Spearman: ProtST-ESM-2 0.682; ESM-2 0.677.

[Source 1](https://arxiv.org/html/2206.02096v2), [Source 2](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf), [Source 3](https://github.com/songlab-cal/tape)

#### TAPE / Rocklin stability

Full-model supervised fine-tuning. Do not conflate with NatureLM's binarized stability task.

Published source size/units: Test: 12,851 proteins. Train: 53,571; validation: 2,512.

**Protein stability:** Spearman correlation. Official TAPE stability split; retain the numerical target.

The numerical endpoint is assay-specific; these tasks do not establish a general ability to explain mechanisms.

**Protein stability — Runnable now:** Complete task inputs, a named frozen Qwen protocol and native/qualified scorer are prepared in the sealed current execution plan. Already running or queued; output validity and eventual score are not guaranteed.

Model compatibility: compatible

Evidence:

```json
[
  "reports/CURRENT_EXECUTION_STATUS_2026-10-16.json",
  ".local/remaining_evaluations/supervisor_plan.json",
  ".local/remaining_evaluations/launch_summary.json"
]
```

Published reference record: Spearman: ProtST-ESM-2 0.738; ESM-2 0.718.

[Source 1](https://arxiv.org/html/2206.02096v2), [Source 2](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf), [Source 3](https://github.com/songlab-cal/tape)

#### FLIP — AAV and Meltome

Two distinct source datasets, grouped under the FLIP suite. Full-model fine-tuning; no cross-assay average added.

Published source size/units: ProtST splits: AAV two_vs_many; Meltome human_cell. Exact test counts not verified in this review.

**AAV variant fitness prediction:** Spearman correlation. FLIP AAV two_vs_many split.

The numerical endpoint is assay-specific; these tasks do not establish a general ability to explain mechanisms.

**Protein thermostability prediction:** Spearman correlation. FLIP meltome human_cell configuration.

The numerical endpoint is assay-specific; these tasks do not establish a general ability to explain mechanisms.

**AAV variant fitness prediction — Needs data or protocol:** Qwen can accept the sequence and return a numeric assay score. The pinned FLIP two_vs_many source acquisition and capsid-fitness case/assay review are unfinished; no inference-ready approved input set is documented.

Model compatibility: compatible

Evidence:

```json
[
  "reports/catalog_execution_review_2026-10-15.json",
  ".local/remaining_evaluations/catalog_plan.json"
]
```

**Protein thermostability prediction — Runnable now:** The 1,366-case Qwen run and native Spearman scorer already exist. Its full-test Spearman is undefined because 12 outputs did not parse; this is an observed output-quality failure, not proof of a missing protocol or incompatible model. Keep the undefined primary metric and parsed-only diagnostic distinct; no rescoring or retry is authorized here.

Model compatibility: compatible

Evidence:

```json
[
  "reports/RESULTS_AT_A_GLANCE.json",
  "configs/local_catalog_p06.json",
  "scripts/score_local_catalog_tasks.py"
]
```

##### Thermostability — FLIP/Meltome

**Native/local protocol:** `QWEN_ZERO_SHOT_FULL_SEQUENCE_FLIP_HUMAN_CELL`

**Coverage:** full_frozen_reviewed_case_set; diagnostic_only_primary_metrics_invalid.

**Saved count record:**

```json
{
  "planned": 1366,
  "completed": 1366,
  "parsed": 1354,
  "invalid_outputs": 12,
  "missing_or_failed_outputs": 0,
  "held_before_inference": 0
}
```

**Complete stored metrics, including alternate/diagnostic values:**

```json
{
  "spearman": null,
  "spearman_parsed_only": 0.025374030047975442,
  "planned": 1366,
  "parsed": 1354,
  "missing": 0,
  "invalid": 12,
  "undefined_constant_or_insufficient": false,
  "all_case_rule": "No invented numeric replacement. Full-test Spearman requires all outputs to parse; otherwise parsed-only correlation is explicitly incomplete."
}
```

**Comparison qualification:** Native source outcome, data split and metric when separately verified; prompted zero-shot full-sequence Qwen baseline, not matched specialist training. No native BioT5 special-token architecture or fitted regression/classification head reproduced.

All planned requests finished, but the full-test primary metric is undefined. Parsed-only diagnostics do not complete the benchmark and cannot replace its native metric.

**All stored published-reference records — separate from the local run:**

```json
[
  {
    "model": "ProtST-ESM-1b",
    "metrics": {
      "fixed_encoder": {
        "spearman": 0.68
      },
      "full_model_tuning": {
        "spearman": 0.681
      }
    },
    "source_id": "PROTST",
    "source_url": "https://proceedings.mlr.press/v202/xu23t/xu23t.pdf",
    "source_locator": "Table 2, printed p.6",
    "protocol": "two-layer MLP trained on official task split; frozen encoder and full tuning are separate regimes",
    "value_status": "published_rounded_as_printed",
    "run_count": null,
    "reported_std": null
  }
]
```

[Original score artifact](https://github.com/Some-random/bio-evaluation/blob/main/results/runs/qwen38_27b_p06_original_test_2026-10-15/scores.json)

[Source 1](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf), [Source 2](https://github.com/J-SNACKKB/FLIP), [Source 3](https://github.com/J-SNACKKB/FLIP)

#### NatureLM/PEER binarized stability — paper-specific protocol

Keep separate from TAPE's continuous stability regression. Do not silently change the paper's endpoint.

Published source size/units: NatureLM §7.2 uses classification. Exact label-conversion rule not resolved in this review.

**Protein stability classification:** Accuracy. NatureLM §7.2 uses classification. Exact label-conversion rule not resolved in this review.

Keep separate from TAPE's continuous stability regression. Do not silently change the paper's endpoint.

**Protein stability classification — Needs data or protocol:** The required binary output is compatible with Qwen, but the source processed case manifest, stability threshold and label-conversion rule are missing. Continuous TAPE stability is a different endpoint and cannot substitute.

Model compatibility: compatible

Evidence:

```json
[
  "reports/remaining_native_source_recovery_2026-10-15.json"
]
```

Published reference record: NatureLM-8x7B: 72.3% accuracy; SFM-Protein-650M: 58.3%, in NatureLM's stability-classification setup.

[Source 1](https://arxiv.org/html/2502.07527v3), [Source 2](https://github.com/microsoft/SFM)

#### PFMBench production and enzyme-operating panel

These are PFMBench-specific processed datasets/splits, not interchangeable with PEER/ProtST results. F1 is not Fmax. Affinity-named AUROC tasks are classification, not KD regression. Exact loaders required.

Published source size/units: Test sizes: Optimal_pH: 959; DeepET_Topt: 185; Cloning_CLF: 2,778; Material_Production: 2,775; Enzyme_Eff.: 1,290; Antib._Res.: 339; Thermostability: 4,184

**Protein production and enzyme conditions — Needs data or protocol:** Most endpoints can accept a sequence-to-label/numeric Qwen adaptation. The seven native splits, required context and separate regression/classification scores are not prepared; assay-level scope review is still required for resistance-related endpoints, and no supervised ESM2-Adapter reproduction is implied.

Model compatibility: compatible

Evidence:

```json
[
  "reports/TASK_HIERARCHY_DATA.json",
  "handoff/Bio_Evaluation_Agent_Package_2026-10-16/EVALUATION_INVENTORY.csv",
  "reports/local_model_capability_smoke.json"
]
```

Published reference record: ESM2-Adapter, Table 1 means: Optimal_pH Spearman 0.0564; DeepET_Topt Spearman 0.2628; Cloning_CLF AUROC 0.8160; Material_Production Accuracy 0.7982; Enzyme_Eff. Spearman 0.2173; Antib._Res. Accuracy 0.6185; Thermostability AUROC 0.9553

[Source 1](https://arxiv.org/html/2506.14796v1), [Source 2](https://github.com/biomap-research/PFMBench)

#### Protein interactions and interfaces

#### Human/Pan and yeast/Guo PPI — PEER

Separate human/yeast negatives and splits. Generic PPI, not Affibody–pMHC specificity.

Published source size/units: Published PEER test counts: human 227 pairs; yeast 373 pairs.

**Human protein–protein interaction prediction:** Accuracy. Official human PEER PPI split; preserve negative construction.

Not TCR–pMHC specificity and not a measured dissociation constant.

**Yeast protein–protein interaction prediction:** Accuracy. Official yeast PEER PPI split; preserve negative construction.

Not TCR–pMHC specificity and not a measured dissociation constant.

**Human protein–protein interaction prediction — Runnable now:** An existing completed declared Qwen run demonstrates that the input interface, execution harness and scorer can be used in this environment. This is readiness of the documented qualified baseline, not a claim of strong performance or full paper replication.

Model compatibility: compatible

Evidence:

```json
[
  "reports/RESULTS_AT_A_GLANCE.json"
]
```

**Yeast protein–protein interaction prediction — Runnable now:** An existing completed declared Qwen run demonstrates that the input interface, execution harness and scorer can be used in this environment. This is readiness of the documented qualified baseline, not a claim of strong performance or full paper replication.

Model compatibility: compatible

Evidence:

```json
[
  "reports/RESULTS_AT_A_GLANCE.json"
]
```

##### Human protein–protein interaction — PEER

**Native/local protocol:** `QWEN_FULL_SEQUENCE_TEXT_BIOT5_TEST`

**Coverage:** full_frozen_reviewed_case_set; completed_declared_run.

**Saved count record:**

```json
{
  "planned": 237,
  "completed": 237,
  "parsed": 229,
  "invalid_outputs": 8,
  "missing_or_failed_outputs": 0,
  "held_before_inference": 0
}
```

**Complete stored metrics, including alternate/diagnostic values:**

```json
{
  "accuracy": 0.5021097046413502,
  "correct": 119,
  "planned": 237,
  "parsed": 229,
  "missing": 0,
  "invalid": 8,
  "all_case_rule": "Missing or invalid model answers count as incorrect; report transport failures separately."
}
```

**Comparison qualification:** Native source outcome, data split and metric when separately verified; prompted zero-shot full-sequence Qwen baseline, not matched specialist training. No native BioT5 special-token architecture or fitted regression/classification head reproduced.

Full source test, all invalid answers retained as failures; zero-shot full sequences versus supervised BioT5+.

**All stored published-reference records — separate from the local run:**

```json
[
  {
    "model": "BioT5+",
    "metrics": {
      "accuracy_percent": 85.09
    },
    "source_id": "BIOT5",
    "source_url": "https://arxiv.org/html/2402.17810v2",
    "source_locator": "Table 6",
    "protocol": "supervised multitask instruction tuning on official PEER splits",
    "value_status": "published_rounded_as_printed",
    "run_count": null,
    "reported_std": {
      "accuracy_percent": 0.4
    },
    "uncertainty_note": "Table prints mean ± dispersion; number of runs/dispersion definition not independently re-established here."
  },
  {
    "model": "NatureLM",
    "metrics": {
      "1B_accuracy": 0.781,
      "8B_accuracy": 0.848,
      "8x7B_accuracy": 0.776
    },
    "source_id": "NATURE",
    "source_url": "https://arxiv.org/html/2502.07527v3",
    "source_locator": "Table 20, Section 7.2",
    "protocol": "task-trained scientific model; adopted PEER splits",
    "value_status": "published_rounded_as_printed",
    "run_count": null,
    "reported_std": null
  }
]
```

[Original score artifact](https://github.com/Some-random/bio-evaluation/blob/main/results/runs/qwen38_27b_p10_original_test_2026-10-15/scores.json)

##### Yeast protein–protein interaction — PEER

**Native/local protocol:** `QWEN_FULL_SEQUENCE_TEXT_BIOT5_TEST`

**Coverage:** full_frozen_reviewed_case_set; completed_declared_run.

**Saved count record:**

```json
{
  "planned": 394,
  "completed": 394,
  "parsed": 365,
  "invalid_outputs": 29,
  "missing_or_failed_outputs": 0,
  "held_before_inference": 0
}
```

**Complete stored metrics, including alternate/diagnostic values:**

```json
{
  "accuracy": 0.4517766497461929,
  "correct": 178,
  "planned": 394,
  "parsed": 365,
  "missing": 0,
  "invalid": 29,
  "all_case_rule": "Missing or invalid model answers count as incorrect; report transport failures separately."
}
```

**Comparison qualification:** Native source outcome, data split and metric when separately verified; prompted zero-shot full-sequence Qwen baseline, not matched specialist training. No native BioT5 special-token architecture or fitted regression/classification head reproduced.

Full source test, all invalid answers retained as failures; zero-shot full sequences versus supervised BioT5+.

**All stored published-reference records — separate from the local run:**

```json
[
  {
    "model": "BioT5+",
    "metrics": {
      "accuracy_percent": 66.16
    },
    "source_id": "BIOT5",
    "source_url": "https://arxiv.org/html/2402.17810v2",
    "source_locator": "Table 6",
    "protocol": "supervised multitask instruction tuning on official PEER splits",
    "value_status": "published_rounded_as_printed",
    "run_count": null,
    "reported_std": {
      "accuracy_percent": 0.43
    },
    "uncertainty_note": "Table prints mean ± dispersion; number of runs/dispersion definition not independently re-established here."
  },
  {
    "model": "NatureLM",
    "metrics": {
      "1B_accuracy": 0.561,
      "8B_accuracy": 0.604,
      "8x7B_accuracy": 0.586
    },
    "source_id": "NATURE",
    "source_url": "https://arxiv.org/html/2502.07527v3",
    "source_locator": "Table 20, Section 7.2",
    "protocol": "task-trained scientific model; adopted PEER splits",
    "value_status": "published_rounded_as_printed",
    "run_count": null,
    "reported_std": null
  }
]
```

[Original score artifact](https://github.com/Some-random/bio-evaluation/blob/main/results/runs/qwen38_27b_p11_original_test_2026-10-15/scores.json)

[Source 1](https://arxiv.org/html/2206.02096v2), [Source 2](https://arxiv.org/html/2402.17810v2), [Source 3](https://github.com/DeepGraphLearning/PEER_Benchmark)

#### ATOM3D interface contacts (PIP)

Residue-pair contact prediction is not sequence-pair binary PPI and not binding affinity.

Published source size/units: DIPS training and DB5 testing; exact processed test count not transcribed.

**Protein interface contacts — Needs additional models/tools:** The native input is unbound 3D structures and the output is residue-pair contact probabilities. No validated geometry-input/contact-scoring adapter is present; running the native structural baseline needs additional structural software/models. A sequence-only prompt would change the task.

Model compatibility: needs specialist pipeline

Evidence:

```json
[
  "reports/TASK_HIERARCHY_DATA.json",
  "handoff/Bio_Evaluation_Agent_Package_2026-10-16/EVALUATION_INVENTORY.csv",
  "reports/local_model_capability_smoke.json"
]
```

Published reference record: AUROC: 3D-CNN 0.844; GNN 0.669; non-3D baseline 0.841.

[Source 1](https://arxiv.org/html/2012.04035v3), [Source 2](https://www.atom3d.ai/pip.html)

#### PFMBench protein and metal-interaction panel

These are PFMBench-specific processed datasets/splits, not interchangeable with PEER/ProtST results. F1 is not Fmax. Affinity-named AUROC tasks are classification, not KD regression. Exact loaders required.

Published source size/units: Test sizes: Human_PPI: 195; Yeast_PPI: 335; PPI_Affinity: 326; MetalIonBinding: 718

**Protein and metal interactions — Needs data or protocol:** A sequence/partner-context Qwen adaptation is possible. Exact PFMBench paired inputs, metal classes and continuous scoring for PPI AUROC/affinity Spearman must be prepared; these are not the existing PEER interaction splits or a matched trained ESM2-Adapter.

Model compatibility: compatible

Evidence:

```json
[
  "reports/TASK_HIERARCHY_DATA.json",
  "handoff/Bio_Evaluation_Agent_Package_2026-10-16/EVALUATION_INVENTORY.csv",
  "reports/local_model_capability_smoke.json"
]
```

Published reference record: ESM2-Adapter, Table 1 means: Human_PPI AUROC 0.4828; Yeast_PPI AUROC 0.5343; PPI_Affinity Spearman -0.0047; MetalIonBinding Accuracy 0.7066

[Source 1](https://arxiv.org/html/2506.14796v1), [Source 2](https://github.com/biomap-research/PFMBench)

#### Antibody properties

#### FLAb / FLAb2 antibody property collection

15 reference datasets are excluded from automated scoring; counts are corpus totals. Each assay has its own units, direction and split.

Published source size/units: Current repository: 241 datasets; >3 million assay points. Category counts 31/132/7/4/9/33/25 respectively (see details); not one held-out set.

**Antibody properties — Needs scoring protocol:** Qwen can read the antibody sequences, but this collection has assay-specific directions, units and zero-/few-shot protocols, with 15 reference datasets excluded. A pinned assay subset, split and Qwen sequence-scoring contract are needed; a prompted baseline would not reproduce fitted antibody models.

Model compatibility: compatible

Evidence:

```json
[
  "reports/TASK_HIERARCHY_DATA.json",
  "handoff/Bio_Evaluation_Agent_Package_2026-10-16/EVALUATION_INVENTORY.csv",
  "reports/local_model_capability_smoke.json"
]
```

Published reference record: No version-matched aggregate model score transcribed; repository supplies per-assay zero-/few-shot evaluation outputs.

[Source 1](https://github.com/Graylab/FLAb), [Source 2](https://github.com/Graylab/FLAb)

## Protein function, annotations and descriptions

#### Gene Ontology and enzyme annotation

#### DeepFRI-derived EC and GO test splits

Full-model supervised tuning. Keep ontology branches separate. This is annotation recovery, not verification of every rationale.

Published source size/units: ProtST's 95%-identity split setting. Exact processed test counts not recovered here.

**Enzyme Commission annotation:** Micro-AP/AUPR; Fmax. ProtST uses the DeepFRI task split with a 95% sequence-identity cutoff.

Multilabel annotation recovery; incomplete annotation is not verified absence of an activity.

**Gene Ontology: biological process:** Micro-AP/AUPR; Fmax. Keep BP/MF/CC separate; ProtST's DeepFRI-derived split.

Not a free-form rationale score. GO label incompleteness and ontology propagation affect evaluation.

**Gene Ontology: molecular function:** Micro-AP/AUPR; Fmax. Keep BP/MF/CC separate; ProtST's DeepFRI-derived split.

Not a free-form rationale score. GO label incompleteness and ontology propagation affect evaluation.

**Gene Ontology: cellular component:** Micro-AP/AUPR; Fmax. Keep BP/MF/CC separate; ProtST's DeepFRI-derived split.

Not a free-form rationale score. GO label incompleteness and ontology propagation affect evaluation.

**Enzyme Commission annotation — Runnable now:** Complete task inputs, a named frozen Qwen protocol and native/qualified scorer are prepared in the sealed current execution plan. Already running or queued; output validity and eventual score are not guaranteed.

Model compatibility: compatible

Evidence:

```json
[
  "reports/CURRENT_EXECUTION_STATUS_2026-10-16.json",
  ".local/remaining_evaluations/supervisor_plan.json",
  ".local/remaining_evaluations/launch_summary.json"
]
```

**Gene Ontology: biological process — Runnable now:** Complete task inputs, a named frozen Qwen protocol and native/qualified scorer are prepared in the sealed current execution plan. Already running or queued; output validity and eventual score are not guaranteed.

Model compatibility: compatible

Evidence:

```json
[
  "reports/CURRENT_EXECUTION_STATUS_2026-10-16.json",
  ".local/remaining_evaluations/supervisor_plan.json",
  ".local/remaining_evaluations/launch_summary.json"
]
```

**Gene Ontology: molecular function — Runnable now:** Complete task inputs, a named frozen Qwen protocol and native/qualified scorer are prepared in the sealed current execution plan. Already running or queued; output validity and eventual score are not guaranteed.

Model compatibility: compatible

Evidence:

```json
[
  "reports/CURRENT_EXECUTION_STATUS_2026-10-16.json",
  ".local/remaining_evaluations/supervisor_plan.json",
  ".local/remaining_evaluations/launch_summary.json"
]
```

**Gene Ontology: cellular component — Runnable now:** Complete task inputs, a named frozen Qwen protocol and native/qualified scorer are prepared in the sealed current execution plan. Already running or queued; output validity and eventual score are not guaranteed.

Model compatibility: compatible

Evidence:

```json
[
  "reports/CURRENT_EXECUTION_STATUS_2026-10-16.json",
  ".local/remaining_evaluations/supervisor_plan.json",
  ".local/remaining_evaluations/launch_summary.json"
]
```

Published reference record: Fmax, ProtST-ESM-2 vs ESM-2: EC 0.878 vs 0.874; GO-BP 0.482 vs 0.472; GO-MF 0.668 vs 0.662; GO-CC 0.487 vs 0.472.

[Source 1](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf), [Source 2](https://github.com/DeepGraphLearning/ProtST)

#### BioReason-Pro temporal GO test

Headline aggregation; exact BP/MF/CC definition must come from official evaluator. Not interchangeable with species-held-out evaluation.

Published source size/units: Released test: 8,630 proteins.

**Temporal Gene Ontology annotation:** Fmax; information-accretion-weighted Fmax. Released test data: 8,630 proteins; preserve the specified temporal and annotation cutoffs.

No observed label is not proof of no function. Separate predicted context from gold annotations.

**Temporal Gene Ontology annotation — Runnable now:** Complete task inputs, a named frozen Qwen protocol and native/qualified scorer are prepared in the sealed current execution plan. Already running or queued; output validity and eventual score are not guaranteed.

Model compatibility: compatible

Evidence:

```json
[
  "reports/CURRENT_EXECUTION_STATUS_2026-10-16.json",
  ".local/remaining_evaluations/supervisor_plan.json",
  ".local/remaining_evaluations/launch_summary.json"
]
```

Published reference record: Official repository headline: BioReason-Pro 73.6% Fmax.

[Source 1](https://huggingface.co/datasets/wanglab/bioreason-pro-test-data), [Source 2](https://raw.githubusercontent.com/bowang-lab/BioReason-Pro/main/README.md), [Source 3](https://huggingface.co/datasets/wanglab/bioreason-pro-test-data)

#### Bio-posttrain species-held-out protein GO

Do not substitute the original BioReason-Pro 8,630-protein split or its Fmax scorer without documenting the change.

Author resolve_gold_terms_from_row unions curated leaf/ancestor fields AND go_pred_leaf while go_pred is supplied as context. Native reference and input are dependent: the metric can reward recovery/copying of supplied predictions and does not isolate novel function inference. Preserve that augmented target as primary; curated-only reference union is a separate fixed diagnostic, also with predictor overlap and unknown historical independence. Never select the more favorable metric or remove native context.

Published source size/units: Two held-out species in the paper; exact species/counts not established in this review. Also discusses inherited temporal protocol.

**Species-held-out Gene Ontology annotation:** Propagated GO-F1. Two held-out species in the paper; exact species/counts not established in this review. Also discusses inherited temporal protocol.

Do not substitute the original BioReason-Pro 8,630-protein split or its Fmax scorer without documenting the change.

**Species-held-out Gene Ontology annotation — Runnable now:** Complete task inputs, a named frozen Qwen protocol and native/qualified scorer are prepared in the sealed current execution plan. Already running or queued; output validity and eventual score are not guaranteed. The preserved native target includes supplied GO-predictor terms; future scores do not isolate novel function inference.

Model compatibility: compatible

Evidence:

```json
[
  "reports/CURRENT_EXECUTION_STATUS_2026-10-16.json",
  ".local/remaining_evaluations/supervisor_plan.json",
  ".local/remaining_evaluations/launch_summary.json",
  "reports/posttrain_native_gap_audit.json"
]
```

Published reference record: Species-held-out GO evaluation is described; a verified numeric result for the exact protein split is not transcribed here.

[Source 1](https://arxiv.org/html/2606.16517v1), [Source 2](https://github.com/mims-harvard/bio-posttrain)

#### PFMBench GO/EC annotation panel

These are PFMBench-specific processed datasets/splits, not interchangeable with PEER/ProtST results. F1 is not Fmax. Affinity-named AUROC tasks are classification, not KD regression. Exact loaders required.

Published source size/units: Test sizes: GO-CC: 1,400; GO-MF: 2,787; GO-BP: 2,664; EC: 1,604

**Enzyme and Gene Ontology annotation — Needs data or protocol:** Qwen can generate EC/GO labels as a zero-shot adaptation. The PFMBench-specific splits, vocabularies and F1 computation must be prepared; the active DeepFRI-based tasks use different source protocols and cannot stand in for these datasets.

Model compatibility: compatible

Evidence:

```json
[
  "reports/TASK_HIERARCHY_DATA.json",
  "handoff/Bio_Evaluation_Agent_Package_2026-10-16/EVALUATION_INVENTORY.csv",
  "reports/local_model_capability_smoke.json"
]
```

Published reference record: ESM2-Adapter, Table 1 means: GO-CC F1 0.6130; GO-MF F1 0.6488; GO-BP F1 0.5412; EC F1 0.7379

[Source 1](https://arxiv.org/html/2506.14796v1), [Source 2](https://github.com/biomap-research/PFMBench)

#### Protein function descriptions

#### Mol-Instructions — four protein-description subsets

NEW source result: these are Mol-Instructions' own numbers, NOT BioT5+. BioT5+'s Figure 2 reports its comparisons, but exact plotted values were not transcribed.

Published source size/units: Original Mol-Instructions paper: approximately 1,000 test examples per task; exact released counts not recomputed.

**Protein function description generation:** ROUGE-L in BioT5+ protein-text experiments. Use the Mol-Instructions task-specific split; not one interchangeable pool of protein questions.

Text overlap can reward similar wording without validating every biological claim.

**Catalytic activity description generation:** ROUGE-L in BioT5+ protein-text experiments. Use the Mol-Instructions task-specific split; not one interchangeable pool of protein questions.

Text overlap can reward similar wording without validating every biological claim.

**Protein domain and motif description generation:** ROUGE-L in BioT5+ protein-text experiments. Use the Mol-Instructions task-specific split; not one interchangeable pool of protein questions.

Text overlap can reward similar wording without validating every biological claim.

**Protein functional description generation:** ROUGE-L in BioT5+ protein-text experiments. Use the Mol-Instructions task-specific split; not one interchangeable pool of protein questions.

Text overlap can reward similar wording without validating every biological claim.

**Protein function description generation — Runnable now:** An existing completed declared Qwen run demonstrates that the input interface, execution harness and scorer can be used in this environment. This is readiness of the documented qualified baseline, not a claim of strong performance or full paper replication.

Model compatibility: compatible

Evidence:

```json
[
  "reports/RESULTS_AT_A_GLANCE.json"
]
```

**Catalytic activity description generation — Runnable now:** An existing completed declared Qwen run demonstrates that the input interface, execution harness and scorer can be used in this environment. This is readiness of the documented qualified baseline, not a claim of strong performance or full paper replication.

Model compatibility: compatible

Evidence:

```json
[
  "reports/RESULTS_AT_A_GLANCE.json"
]
```

**Protein domain and motif description generation — Runnable now:** An existing completed declared Qwen run demonstrates that the input interface, execution harness and scorer can be used in this environment. This is readiness of the documented qualified baseline, not a claim of strong performance or full paper replication.

Model compatibility: compatible

Evidence:

```json
[
  "reports/RESULTS_AT_A_GLANCE.json"
]
```

**Protein functional description generation — Runnable now:** An existing completed declared Qwen run demonstrates that the input interface, execution harness and scorer can be used in this environment. This is readiness of the documented qualified baseline, not a claim of strong performance or full paper replication.

Model compatibility: compatible

Evidence:

```json
[
  "reports/RESULTS_AT_A_GLANCE.json"
]
```

##### Mol-Instructions: Protein function generation

**Native/local protocol:** `QWEN_FULL_SEQUENCE_BIOT5_EXPORT_MOLINST_GOLD_ONLY_ROUGE`

**Coverage:** full_frozen_reviewed_BioT5_export_test; completed_declared_run.

**Saved count record:**

```json
{
  "planned": 3494,
  "completed": 3494,
  "parsed": 3494,
  "invalid_outputs": 0,
  "missing_or_failed_outputs": 0,
  "held_before_inference": 0
}
```

**Complete stored metrics, including alternate/diagnostic values:**

```json
{
  "rouge1": 0.06310683515639813,
  "rouge2": 0.013863408860249667,
  "rougeL": 0.043147832149630236,
  "rougeLsum": 0.05416016139070249
}
```

**Comparison qualification:** Native Mol-Instructions gold-only ROUGE scorer algorithm on pinned BioT5+ task-defined test exports; full-sequence zero-shot Qwen is an explicit architecture/context/training adaptation. Pinned BioT5+ scorer passes [gold,decoded_input] pairs despite computing gold-only references_new: exact BioT5+ paper metric equivalence unresolved.

**All stored published-reference records — separate from the local run:**

```json
[]
```

[Original score artifact](https://github.com/Some-random/bio-evaluation/blob/main/results/runs/qwen38_27b_p23_description_full_parallel_2026-10-15/scores.json)

##### Mol-Instructions: Catalytic activity generation

**Native/local protocol:** `QWEN_FULL_SEQUENCE_BIOT5_EXPORT_MOLINST_GOLD_ONLY_ROUGE`

**Coverage:** full_frozen_reviewed_BioT5_export_test; completed_declared_run.

**Saved count record:**

```json
{
  "planned": 1601,
  "completed": 1601,
  "parsed": 1601,
  "invalid_outputs": 0,
  "missing_or_failed_outputs": 0,
  "held_before_inference": 0
}
```

**Complete stored metrics, including alternate/diagnostic values:**

```json
{
  "rouge1": 0.05409324446271062,
  "rouge2": 0.013950959938535082,
  "rougeL": 0.03964896400553061,
  "rougeLsum": 0.047278128885466786
}
```

**Comparison qualification:** Native Mol-Instructions gold-only ROUGE scorer algorithm on pinned BioT5+ task-defined test exports; full-sequence zero-shot Qwen is an explicit architecture/context/training adaptation. Pinned BioT5+ scorer passes [gold,decoded_input] pairs despite computing gold-only references_new: exact BioT5+ paper metric equivalence unresolved.

**All stored published-reference records — separate from the local run:**

```json
[]
```

[Original score artifact](https://github.com/Some-random/bio-evaluation/blob/main/results/runs/qwen38_27b_p24_description_full_parallel_2026-10-15/scores.json)

##### Mol-Instructions: Domain and motif generation

**Native/local protocol:** `QWEN_FULL_SEQUENCE_BIOT5_EXPORT_MOLINST_GOLD_ONLY_ROUGE`

**Coverage:** full_frozen_reviewed_BioT5_export_test; completed_declared_run.

**Saved count record:**

```json
{
  "planned": 1400,
  "completed": 1400,
  "parsed": 1400,
  "invalid_outputs": 0,
  "missing_or_failed_outputs": 0,
  "held_before_inference": 0
}
```

**Complete stored metrics, including alternate/diagnostic values:**

```json
{
  "rouge1": 0.035429920594239744,
  "rouge2": 0.004749318294493327,
  "rougeL": 0.025868349270155935,
  "rougeLsum": 0.030632014797656003
}
```

**Comparison qualification:** Native Mol-Instructions gold-only ROUGE scorer algorithm on pinned BioT5+ task-defined test exports; full-sequence zero-shot Qwen is an explicit architecture/context/training adaptation. Pinned BioT5+ scorer passes [gold,decoded_input] pairs despite computing gold-only references_new: exact BioT5+ paper metric equivalence unresolved.

**All stored published-reference records — separate from the local run:**

```json
[]
```

[Original score artifact](https://github.com/Some-random/bio-evaluation/blob/main/results/runs/qwen38_27b_p25_description_full_parallel_2026-10-15/scores.json)

##### Mol-Instructions: Functional description generation

**Native/local protocol:** `QWEN_FULL_SEQUENCE_BIOT5_EXPORT_MOLINST_GOLD_ONLY_ROUGE`

**Coverage:** full_frozen_reviewed_BioT5_export_test; completed_declared_run.

**Saved count record:**

```json
{
  "planned": 2633,
  "completed": 2633,
  "parsed": 2633,
  "invalid_outputs": 0,
  "missing_or_failed_outputs": 0,
  "held_before_inference": 0
}
```

**Complete stored metrics, including alternate/diagnostic values:**

```json
{
  "rouge1": 0.08002505455026915,
  "rouge2": 0.01232325567816589,
  "rougeL": 0.04942258724738958,
  "rougeLsum": 0.06493613220229738
}
```

**Comparison qualification:** Native Mol-Instructions gold-only ROUGE scorer algorithm on pinned BioT5+ task-defined test exports; full-sequence zero-shot Qwen is an explicit architecture/context/training adaptation. Pinned BioT5+ scorer passes [gold,decoded_input] pairs despite computing gold-only references_new: exact BioT5+ paper metric equivalence unresolved.

**All stored published-reference records — separate from the local run:**

```json
[]
```

[Original score artifact](https://github.com/Some-random/bio-evaluation/blob/main/results/runs/qwen38_27b_p26_description_full_parallel_2026-10-15/scores.json)

[Source 1](https://arxiv.org/html/2306.08018v4), [Source 2](https://raw.githubusercontent.com/zjunlp/Mol-Instructions/main/README.md), [Source 3](https://arxiv.org/html/2402.17810v2), [Source 4](https://github.com/zjunlp/Mol-Instructions)

#### NatureLM's NCBI protein-description holdout

This is a paper-specific NCBI-derived set, not all NCBI data. Different task-training regimes; text-overlap evaluation.

Published source size/units: Temporal split; exact test count and frozen processed release not recovered.

**Protein description generation:** ROUGE-L. Paper reports a temporal split; exact frozen test release/count not recovered.

Do not replace its temporal test with arbitrary UniProt rows and claim exact reproduction.

**Protein description generation — Needs data or protocol:** Protein-to-description generation is compatible with Qwen. The rechecked publisher commit is unchanged; its source tree and NatureLM notebooks were restored, but the exact temporal test case IDs, sequence/reference snapshots, annotation cutoff and executable ROUGE-L preprocessing remain unrecovered. Mol-Instructions or arbitrary current NCBI proteins would define a different protocol.

Model compatibility: compatible

Evidence:

```json
[
  "reports/remaining_native_source_recovery_2026-10-15.json",
  "reports/SOURCE_PREPARATION_2026-10-16.json",
  "handoff/source_preparation_2026-10-16/README.md"
]
```

Published reference record: ROUGE-L: NatureLM-8x7B 0.585; fine-tuned Llama-3-8B 0.324; GPT-4o 0.091.

[Source 1](https://arxiv.org/html/2502.07527v3), [Source 2](https://github.com/microsoft/SFM)

#### Biochemical reaction classification

#### ProtST reaction classification — zero/few-shot

Zero-shot text-label matching is not the same protocol as fitting a fully supervised classifier.

Published source size/units: ProtST zero-shot/few-shot experiment; shots and ensemble settings must be recorded.

**Biochemical reaction classification:** Accuracy. ProtST zero-shot/few-shot experiment; shots and ensemble settings must be recorded.

Zero-shot text-label matching is not the same protocol as fitting a fully supervised classifier.

**Biochemical reaction classification — Runnable now:** Complete task inputs, a named frozen Qwen protocol and native/qualified scorer are prepared in the sealed current execution plan. Already running or queued; output validity and eventual score are not guaranteed.

Model compatibility: compatible

Evidence:

```json
[
  "reports/CURRENT_EXECUTION_STATUS_2026-10-16.json",
  ".local/remaining_evaluations/supervisor_plan.json",
  ".local/remaining_evaluations/launch_summary.json"
]
```

Published reference record: Zero-/few-shot results are reported, but a numeric value for the exact zero-shot reaction setting is not transcribed here. Do not substitute the fully supervised reaction score.

[Source 1](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf), [Source 2](https://github.com/DeepGraphLearning/ProtST)

#### Evidence support for protein explanations

#### BioReason-Pro explanation review

Judged explanation subset Correct GO labels do not guarantee that every intermediate statement is true.

Published source size/units: Are the generated functional explanations helpful and consistent with the reference evidence? Separate from the 8,630-protein GO-label metric; exact scored explanation subset not established here.

**Evidence support for protein-function explanations:** Judge rubrics; qualitative/expert review. Separate from the 8,630-protein GO-label metric; exact scored explanation subset not established here.

Correct GO labels do not guarantee that every intermediate statement is true.

**Evidence support for protein-function explanations — Needs scoring protocol:** Qwen can produce textual functional explanations, but the native assessment requires a defined scored subset and expert/LLM-judge rubric/runtime. These are unresolved, and the existing external provider hold remains. Correct GO labels alone do not validate explanation statements.

Model compatibility: compatible

Evidence:

```json
[
  "reports/catalog_execution_review_2026-10-15.json"
]
```

Published reference record: Repository reports an LLM-judge score of 8/10 and expert preference over UniProt descriptions in 79% of reviewed cases.

[Source 1](https://www.biorxiv.org/content/10.64898/2026.03.19.712954v2.full)

#### Protein retrieval from descriptions

#### ProtST text-to-protein retrieval examples

Retrieval case study Docking and known annotations support case analysis; they do not prove all retrieved candidates bind experimentally.

Published source size/units: Can a functional description retrieve relevant proteins? Selected queries such as heme binding; not a universal, fixed retrieval benchmark with one headline Recall@K.

**Protein retrieval from functional descriptions:** Top-retrieval inspection; docking scores in case studies. Selected queries such as heme binding; not a universal, fixed retrieval benchmark with one headline Recall@K.

Docking and known annotations support case analysis; they do not prove all retrieved candidates bind experimentally.

**Protein retrieval from functional descriptions — Needs additional models/tools:** The native protocol ranks a complete protein corpus with a trained joint sequence/text representation, not ordinary Qwen chat completions. Train/validation corpus assets and the 8.53GB learned checkpoint/runtime are unprepared, and the five qualitative queries do not define an aggregate relevance metric. A new Qwen ranking adaptation would need its own frozen protocol.

Model compatibility: needs specialist pipeline

Evidence:

```json
[
  "reports/REMAINING_DESIGN_SOURCE_FEASIBILITY_2026-10-15.json"
]
```

Published reference record: Selected text-to-protein retrieval and docking case studies are reported; no single fixed-corpus Recall@K benchmark result is transcribed.

[Source 1](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf)

## Mutation effects, fitness and engineering

#### Mutation-effect explanation

#### MutaDescribe — mutation explanation

The reported 'Average' is retained as the paper defines it. Similarity tiers are not a globally homology-disjoint split.

Published source size/units: Main test: Easy 460; Medium 384; Hard 404 mutation examples. Separate temporal test: 1,611 (not the reported main averages).

**Mutation-effect explanation:** BLEU-2; ROUGE-L; GPT-4-plus-human categorical review. Random split then similarity tiers: Easy 460, Medium 384, Hard 404. Separate temporal test has 1,611 examples.

Similarity tiers do not make the entire split homology-disjoint. Judge output is not independent experimental verification.

**Mutation-effect explanation — Needs data or protocol:** The draft text adapter demonstrates a compatible sequence/description or mutation-output interface, but source review stopped before case eligibility and native prompt/scoring normalization were completed. The record holds unreviewed/flagged material; it does not prohibit the entire scientific task. Do not retry or transfer flagged content.

Model compatibility: compatible

Evidence:

```json
[
  "reports/catalog_execution_review_2026-10-15.json",
  "reports/mutadescribe_source_review_hold.json"
]
```

Published reference record: Main-test average ROUGE-L / BLEU-2 (0–100): MutaPLM 21.34 / 13.61; GPT-4-0613, 5-shot kNN: 12.31 / 9.69.

[Source 1](https://arxiv.org/html/2410.22949v1), [Source 2](https://huggingface.co/datasets/PharMolix/MutaDescribe)

#### Mutation fitness prediction and ranking

#### ProteinGym substitutions — historical ProtST evaluation

NEW verified numeric row from ProtST Table 12. Not a current ProteinGym leaderboard result.

Published source size/units: Use the historical ProteinGym snapshot in ProtST. Do not attach the modern 217-assay count to these old results.

**Mutation-effect ranking:** Spearman primary; suite also reports ranking/classification summaries. Pin release: modern v1.3 substitution subset has 217 assays; an older paper may use an earlier snapshot.

Score within each assay. Different assay scores are not a shared physical unit; fitness is not always binding.

**Mutation-effect ranking — Needs data or protocol:** A qualified sequence-to-fitness/ranking adaptation is possible, but the exact ProteinGym release and permitted assay subset are not frozen. Existing pathogen-fitness restrictions remain; no all-assay execution authorization is inferred.

Model compatibility: compatible

Evidence:

```json
[
  "reports/catalog_execution_review_2026-10-15.json",
  ".local/remaining_evaluations/catalog_plan.json"
]
```

Published reference record: UniProt-level mean Spearman: ProtST-ESM-1b 0.412; ESM-1b 0.358; ESM-1v 0.372; Tranception L without retrieval 0.401.

[Source 1](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf), [Source 2](https://github.com/OATML-Markslab/ProteinGym), [Source 3](https://github.com/OATML-Markslab/ProteinGym)

#### PG-LLM / ProteinGym-LLM — eval-data-v1.2

Evaluation-only frozen protocol. Benchmark-specific training, tuning and retrieval augmentation are restricted by its documentation.

Published source size/units: 217 assays; sets of 10, 50 or 100 variants; three seeds.

**Mutation-effect ranking:** Per-assay Spearman. eval-data-v1.2: 217 assays; N=10/50/100; seeds 1/2/3; labels separate from model-facing inputs.

Evaluation-only: do not train, tune prompts, distill or perform retrieval augmentation using these candidate sets/labels.

**Mutation-effect ranking — On hold:** The native text ranking interface is documented, but this existing scope includes prior flagged pathogen-fitness cases and has no cleared replacement scope. Preserve the explicit hold; model compatibility does not authorize retries or transfer.

Model compatibility: compatible

Evidence:

```json
[
  "reports/catalog_execution_review_2026-10-15.json",
  ".local/remaining_evaluations/catalog_plan.json"
]
```

Published reference record: No verified release-matched model score was recovered. This does not mean zero performance.

[Source 1](https://raw.githubusercontent.com/rohitarorayyc/proteingym-llm/main/DATA.md), [Source 2](https://github.com/rohitarorayyc/proteingym-llm/blob/main/DATA.md)

#### PFArena — four task settings

Different assay subsets, not a paired context ablation. Reported aggregates include deterministic random fallback on missing outputs (§10.1/Table 12). Model labels are the paper's, not verified API IDs. Exact public bundle not yet established; retained paper model labels are not executable API identifiers.

Published source size/units: T1: 123 assays / 594,695 measured singles. T2: 74 assays / 6,288 candidates. T3: 67 assays / 3,648 candidates. T4: 29 assays / 2,638 candidates.

**Single-mutant generation:** Recall@40; normalized maximum recovered score. 123 assays; budget 40; 594,695 measured single mutants in the reported source universe

The tasks differ in permitted evidence. 'Anchor' is a tested mutant, not an HLA anchor residue. Assay sets overlap.

PFArena official release found; publisher dataset access is gated and original assay/case review remains pending.

**Multi-mutant ranking without measurements:** Spearman; NDCG; normalized max@K; Recall@K. 74 assays; 6,288 candidates

The tasks differ in permitted evidence. 'Anchor' is a tested mutant, not an HLA anchor residue. Assay sets overlap.

PFArena official release found; publisher dataset access is gated and original assay/case review remains pending.

**Mutation ranking with anchor measurements:** Spearman; NDCG; normalized max@K; Recall@K. 67 assays; 3,648 candidates

The tasks differ in permitted evidence. 'Anchor' is a tested mutant, not an HLA anchor residue. Assay sets overlap.

PFArena official release found; publisher dataset access is gated and original assay/case review remains pending.

**Mutation ranking with single-mutant measurements:** Spearman; NDCG; normalized max@K; Recall@K. 29 assays; 2,638 candidates; 28,609 single-mutant context records

The tasks differ in permitted evidence. 'Anchor' is a tested mutant, not an HLA anchor residue. Assay sets overlap.

PFArena official release found; publisher dataset access is gated and original assay/case review remains pending.

**Single-mutant generation — Needs data or protocol:** The task has a text sequence/proposal/ranking interface, but the official dataset is gated and no authorized complete frozen bundle has been acquired. Native assay/candidate IDs, input review, budgets and failure rules must be fixed before execution.

Model compatibility: compatible

Evidence:

```json
[
  "reports/remaining_native_source_recovery_2026-10-15.json"
]
```

**Multi-mutant ranking without measurements — Needs data or protocol:** The task has a text sequence/proposal/ranking interface, but the official dataset is gated and no authorized complete frozen bundle has been acquired. Native assay/candidate IDs, input review, budgets and failure rules must be fixed before execution.

Model compatibility: compatible

Evidence:

```json
[
  "reports/remaining_native_source_recovery_2026-10-15.json"
]
```

**Mutation ranking with anchor measurements — Needs data or protocol:** The task has a text sequence/proposal/ranking interface, but the official dataset is gated and no authorized complete frozen bundle has been acquired. Native assay/candidate IDs, input review, budgets and failure rules must be fixed before execution.

Model compatibility: compatible

Evidence:

```json
[
  "reports/remaining_native_source_recovery_2026-10-15.json"
]
```

**Mutation ranking with single-mutant measurements — Needs data or protocol:** The task has a text sequence/proposal/ranking interface, but the official dataset is gated and no authorized complete frozen bundle has been acquired. Native assay/candidate IDs, input review, budgets and failure rules must be fixed before execution.

Model compatibility: compatible

Evidence:

```json
[
  "reports/remaining_native_source_recovery_2026-10-15.json"
]
```

Published reference record: Paper's GPT-6 Astra vs ESM-2: T1 Recall@40 0.0254 vs 0.0370; T2 Spearman 0.2726 vs 0.2539; T3 0.3516 vs 0.3128; T4 0.5988 vs 0.3153.

[Source 1](https://arxiv.org/html/2609.28921v1), [Source 2](https://arxiv.org/html/2609.28921v1)

#### MutaPLM low-data fitness regression

This is supervised low-N prediction, not zero-shot generation. Do not reuse the labeled seed points as test examples.

Published source size/units: 192 training + 48 validation examples; five seeds; assay-specific remaining test records

**Low-data fitness regression:** Spearman. 192 training and 48 validation samples; five random seeds. Remaining held-out data evaluated per source.

This is supervised low-N prediction, not zero-shot generation. Do not reuse the labeled seed points as test examples.

**Low-data fitness regression — Needs additional models/tools:** The native five-seed low-data experiment fits a regression head using 192 training and 48 validation examples. Current frozen Qwen inference does not implement that trained-head protocol, and new training is outside the authorized baseline scope. A prompted numeric baseline would be a separate qualified experiment.

Model compatibility: needs specialist pipeline

Evidence:

```json
[
  "reports/catalog_execution_review_2026-10-15.json"
]
```

Published reference record: Low-data regression curves are reported with 192 train / 48 validation examples; no exact assay-specific point estimate is transcribed here.

[Source 1](https://arxiv.org/html/2410.22949v1), [Source 2](https://github.com/PharMolix/MutaPLM)

#### PFMBench mutation/fitness panel

These are PFMBench-specific processed datasets/splits, not interchangeable with PEER/ProtST results. F1 is not Fmax. Affinity-named AUROC tasks are classification, not KD regression. Exact loaders required.

Published source size/units: Test sizes: PETA_CHS_SOL: 484; PETA_LGK_SOL: 1,914; PETA_TEM_SOL: 808; FLIP_AAV: 16,517; FLIP_GB1: 1,745; TAPE_Stab: 6,898; TAPE_Fluor: 27,217; BetaLactamase: 520

**Mutation and fitness prediction — Needs data or protocol:** A sequence-to-numeric Qwen adaptation is possible, but the eight exact PFMBench processed splits and assay-specific scope reviews are not prepared. Similar TAPE/FLIP tasks elsewhere are not interchangeable with every PFMBench endpoint or its supervised reference.

Model compatibility: compatible

Evidence:

```json
[
  "reports/TASK_HIERARCHY_DATA.json",
  "handoff/Bio_Evaluation_Agent_Package_2026-10-16/EVALUATION_INVENTORY.csv",
  "reports/local_model_capability_smoke.json"
]
```

Published reference record: ESM2-Adapter, Table 1 means: PETA_CHS_SOL Spearman 0.2738; PETA_LGK_SOL Spearman 0.1558; PETA_TEM_SOL Spearman 0.1433; FLIP_AAV Spearman 0.9412; FLIP_GB1 Spearman 0.9517; TAPE_Stab Spearman 0.3211; TAPE_Fluor Spearman 0.6812; BetaLactamase Spearman 0.5740

[Source 1](https://arxiv.org/html/2506.14796v1), [Source 2](https://github.com/biomap-research/PFMBench)

#### PFMBench ProteinGym zero-shot protocol

These are PFMBench-specific processed datasets/splits, not interchangeable with PEER/ProtST results. F1 is not Fmax. Affinity-named AUROC tasks are classification, not KD regression. Exact loaders required.

Published source size/units: Paper table does not specify the release-matched evaluation denominator.

**Zero-shot mutation-effect ranking — Needs scoring protocol:** Qwen offers token likelihoods, but ESM2 masked amino-acid scoring is not the same as autoregressive Qwen token scoring. Pin the ProteinGym release/assays and a Qwen mutation-score normalization contract before running a disclosed adaptation; the native ESM2 score requires that model.

Model compatibility: compatible

Evidence:

```json
[
  "reports/TASK_HIERARCHY_DATA.json",
  "handoff/Bio_Evaluation_Agent_Package_2026-10-16/EVALUATION_INVENTORY.csv",
  "reports/local_model_capability_smoke.json"
]
```

Published reference record: Table 1 reports pretrained ESM2 ProteinGym Spearman 0.4390; do not compare directly to a different snapshot's score.

[Source 1](https://arxiv.org/html/2506.14796v1), [Source 2](https://github.com/biomap-research/PFMBench)

#### Mutation engineering and optimization

#### MutaDescribe — mutation engineering

Same source dataset, different task. These are reference-recovery rates, not prospective wet-lab success.

Published source size/units: Same main Easy/Medium/Hard split as explanation: 460 / 384 / 404 examples.

**Mutation engineering with a supplied position:** Accuracy. Same similarity/temporal splits as MutaDescribe; supplied position simplifies the task.

Recovery of one annotated mutation is not the fraction of novel designs that work.

**Mutation engineering with an unknown position:** Recall@50. Search covers 19 × sequence-length substitutions; preserve the paper's candidate definition.

A different useful but unannotated mutation can score as a miss.

**Mutation engineering with a supplied position — Needs data or protocol:** The draft text adapter demonstrates a compatible sequence/description or mutation-output interface, but source review stopped before case eligibility and native prompt/scoring normalization were completed. The record holds unreviewed/flagged material; it does not prohibit the entire scientific task. Do not retry or transfer flagged content.

Model compatibility: compatible

Evidence:

```json
[
  "reports/catalog_execution_review_2026-10-15.json",
  "reports/mutadescribe_source_review_hold.json"
]
```

**Mutation engineering with an unknown position — Needs data or protocol:** The draft text adapter demonstrates a compatible sequence/description or mutation-output interface, but source review stopped before case eligibility and native prompt/scoring normalization were completed. The record holds unreviewed/flagged material; it does not prohibit the entire scientific task. Do not retry or transfer flagged content.

Model compatibility: compatible

Evidence:

```json
[
  "reports/catalog_execution_review_2026-10-15.json",
  "reports/mutadescribe_source_review_hold.json"
]
```

Published reference record: MutaPLM vs fine-tuned ESM-2: position known accuracy 53.51% vs 51.43%; position unknown Recall@50 40.94% vs 33.77%.

[Source 1](https://arxiv.org/html/2410.22949v1), [Source 2](https://huggingface.co/datasets/PharMolix/MutaDescribe)

#### MutaPLM iterative optimization

Predictor-scored search experiment A learned scorer can be exploited; this experiment is not prospective laboratory success.

Published source size/units: Do iterative proposals improve the predicted assay objective? Six landscapes: AAV, AMIE, avGFP, E4B, LGK, UBE2I; 20 independent runs; preserve beam/search settings.

**Protein-sequence optimization against fitness predictors:** Mean predicted fitness trajectory and dispersion. Six landscapes: AAV, AMIE, avGFP, E4B, LGK, UBE2I; 20 independent runs; preserve beam/search settings.

A learned scorer can be exploited; this experiment is not prospective laboratory success.

**Protein-sequence optimization against fitness predictors — Needs scoring protocol:** A qualified Qwen likelihood replacement is mathematically possible, so this task is not excluded for lacking a learned Qwen head. However, full-prefix likelihood runtime, native 33-class support, source-vs-paper search math, starting assets and the fixed ESM1b fitness-oracle runtime are not fully resolved/frozen. Five permitted landscapes and a held sixth remain distinct.

Model compatibility: unresolved

Evidence:

```json
[
  "reports/p34_five_landscape_feasibility_2026-10-15.json",
  "reports/p34_qwen_likelihood_tokenizer_feasibility.json"
]
```

Published reference record: The paper reports predicted-fitness improvement trajectories across six landscapes; these are oracle-based search outcomes, not experimentally measured hit rates.

[Source 1](https://arxiv.org/html/2410.22949v1)

#### Binding affinity and immune interactions

#### AbBiBench antibody affinity ranking

Paper size and current leaderboard refer to different snapshots. Do not combine them into a single size-matched result. Generative case study is separate.

Published source size/units: Paper: 155,853 heavy-chain variants, 9 antigens (Section 3.1 lists 11 datasets). Current repository leaderboard: 16 assay columns; expanded payload count not established.

**Antibody affinity ranking — Needs scoring protocol:** Qwen can accept the sequences, but a fixed mutation/sequence likelihood or numeric ranking contract must be defined and the assay snapshot pinned. Existing leaderboard methods use different sequence/structure scoring models; the sequence-only Qwen adaptation would not reproduce their structural inputs or training.

Model compatibility: compatible

Evidence:

```json
[
  "reports/TASK_HIERARCHY_DATA.json",
  "handoff/Bio_Evaluation_Agent_Package_2026-10-16/EVALUATION_INVENTORY.csv",
  "reports/local_model_capability_smoke.json"
]
```

Published reference record: Current 16-column leaderboard mean Spearman: ProteinMPNN 0.30; ESM-IF1 0.28; AntiFold 0.21; ESM2 0.02.

[Source 1](https://github.com/MSBMI-SAFE/AbBiBench), [Source 2](https://arxiv.org/html/2506.04235v1), [Source 3](https://huggingface.co/datasets/AbBibench/Antibody_Binding_Benchmark_Dataset)

#### ATOM3D SKEMPI-derived mutation affinity (MSP)

This is binding-affinity change classification, not folding-stability prediction. Source counts are not test counts.

Published source size/units: Source construction: 893 positive and 3,255 negative mutations; exact test size not recovered.

**Mutation effects on binding affinity — Needs additional models/tools:** The native classification uses wild-type/mutant 3D complex context. A validated geometry-input adapter or structural prediction model is missing; a sequence-only Qwen adaptation would omit native information and need a separately defined protocol.

Model compatibility: needs specialist pipeline

Evidence:

```json
[
  "reports/TASK_HIERARCHY_DATA.json",
  "handoff/Bio_Evaluation_Agent_Package_2026-10-16/EVALUATION_INVENTORY.csv",
  "reports/local_model_capability_smoke.json"
]
```

Published reference record: AUROC: GNN 0.621; 3D-CNN 0.574.

[Source 1](https://arxiv.org/html/2012.04035v3), [Source 2](https://www.atom3d.ai/msp.html)

#### PFMBench peptide–MHC and TCR–pMHC panel

These are PFMBench-specific processed datasets/splits, not interchangeable with PEER/ProtST results. F1 is not Fmax. Affinity-named AUROC tasks are classification, not KD regression. Exact loaders required.

Published source size/units: Test sizes: Pept.HLA/MHC Aff.: 8,406; TCR.PMHC Aff.: 2,482

**Peptide–MHC and TCR–pMHC interactions — Needs data or protocol:** The paired peptide/MHC or TCR/pMHC sequences can be supplied to Qwen. Exact PFMBench partner inputs, splits, scope review and continuous AUROC scoring must be prepared; the affinity-named tasks here are classification, not KD regression.

Model compatibility: compatible

Evidence:

```json
[
  "reports/TASK_HIERARCHY_DATA.json",
  "handoff/Bio_Evaluation_Agent_Package_2026-10-16/EVALUATION_INVENTORY.csv",
  "reports/local_model_capability_smoke.json"
]
```

Published reference record: ESM2-Adapter, Table 1 means: Pept.HLA/MHC Aff. AUROC 0.9631; TCR.PMHC Aff. AUROC 0.9312

[Source 1](https://arxiv.org/html/2506.14796v1), [Source 2](https://github.com/biomap-research/PFMBench)

## Scientific evidence and biological knowledge

#### Biological research question answering

#### LAB-Bench — research tasks

Original full public+private test; not the public 1,967-question subset. Three-run means. Tool-free models; TableQA and FigQA are images. No new category aggregate invented.

Published source size/units: Original full evaluation: 2,457 questions. LitQA2 248; SuppQA 102; FigQA 226; TableQA 305; DbQA 650; ProtocolQA 135; SeqQA 750; Cloning 41.

**Literature evidence question answering:** Accuracy; selective precision and coverage when abstention is enabled. Public subset commonly 1,967 questions across eight categories; original full set and private portion differ. Pin dataset revision.

Keep resource access fixed. Original model evaluation was tool-free, unlike human baseline. MCQ success can partly reflect distractor elimination.

**Biological database question answering:** Accuracy; selective precision and coverage when abstention is enabled. Public subset commonly 1,967 questions across eight categories; original full set and private portion differ. Pin dataset revision.

Keep resource access fixed. Original model evaluation was tool-free, unlike human baseline. MCQ success can partly reflect distractor elimination.

**Supplementary-material question answering:** Accuracy; selective precision and coverage when abstention is enabled. Public subset commonly 1,967 questions across eight categories; original full set and private portion differ. Pin dataset revision.

Keep resource access fixed. Original model evaluation was tool-free, unlike human baseline. MCQ success can partly reflect distractor elimination.

**Research figure question answering:** Accuracy; selective precision and coverage when abstention is enabled. Public subset commonly 1,967 questions across eight categories; original full set and private portion differ. Pin dataset revision.

Keep resource access fixed. Original model evaluation was tool-free, unlike human baseline. MCQ success can partly reflect distractor elimination.

**Research table question answering:** Accuracy; selective precision and coverage when abstention is enabled. Public subset commonly 1,967 questions across eight categories; original full set and private portion differ. Pin dataset revision.

Keep resource access fixed. Original model evaluation was tool-free, unlike human baseline. MCQ success can partly reflect distractor elimination.

**Experimental protocol question answering:** Accuracy; selective precision and coverage when abstention is enabled. Public subset commonly 1,967 questions across eight categories; original full set and private portion differ. Pin dataset revision.

Keep resource access fixed. Original model evaluation was tool-free, unlike human baseline. MCQ success can partly reflect distractor elimination.

**Biological sequence question answering:** Accuracy; selective precision and coverage when abstention is enabled. Public subset commonly 1,967 questions across eight categories; original full set and private portion differ. Pin dataset revision.

Keep resource access fixed. Original model evaluation was tool-free, unlike human baseline. MCQ success can partly reflect distractor elimination.

**Molecular cloning question answering:** Accuracy; selective precision and coverage when abstention is enabled. Public subset commonly 1,967 questions across eight categories; original full set and private portion differ. Pin dataset revision.

Keep resource access fixed. Original model evaluation was tool-free, unlike human baseline. MCQ success can partly reflect distractor elimination.

**Literature evidence question answering — Runnable now:** An existing completed declared Qwen run demonstrates that the input interface, execution harness and scorer can be used in this environment. This is readiness of the documented qualified baseline, not a claim of strong performance or full paper replication. The reviewed public cohort is 197 cases, not all 199 released public questions or the full paper test.

Model compatibility: compatible

Evidence:

```json
[
  "reports/RESULTS_AT_A_GLANCE.json"
]
```

**Biological database question answering — Runnable now:** An existing completed declared Qwen run demonstrates that the input interface, execution harness and scorer can be used in this environment. This is readiness of the documented qualified baseline, not a claim of strong performance or full paper replication.

Model compatibility: compatible

Evidence:

```json
[
  "reports/RESULTS_AT_A_GLANCE.json"
]
```

**Supplementary-material question answering — Runnable now:** An existing completed declared Qwen run demonstrates that the input interface, execution harness and scorer can be used in this environment. This is readiness of the documented qualified baseline, not a claim of strong performance or full paper replication.

Model compatibility: compatible

Evidence:

```json
[
  "reports/RESULTS_AT_A_GLANCE.json"
]
```

**Research figure question answering — Runnable now:** An existing completed declared Qwen run demonstrates that the input interface, execution harness and scorer can be used in this environment. This is readiness of the documented qualified baseline, not a claim of strong performance or full paper replication.

Model compatibility: compatible

Evidence:

```json
[
  "reports/RESULTS_AT_A_GLANCE.json"
]
```

**Research table question answering — Runnable now:** An existing completed declared Qwen run demonstrates that the input interface, execution harness and scorer can be used in this environment. This is readiness of the documented qualified baseline, not a claim of strong performance or full paper replication.

Model compatibility: compatible

Evidence:

```json
[
  "reports/RESULTS_AT_A_GLANCE.json"
]
```

**Experimental protocol question answering — On hold:** The text question-answering interface is compatible with Qwen, but the current ProtocolQA inputs triggered the recorded biological-risk hold. Preserve that hold; availability of the model and data does not authorize this scope.

Model compatibility: compatible

Evidence:

```json
[
  "reports/catalog_execution_review_2026-10-15.json",
  ".local/remaining_evaluations/catalog_plan.json"
]
```

**Biological sequence question answering — Runnable now:** An existing completed declared Qwen run demonstrates that the input interface, execution harness and scorer can be used in this environment. This is readiness of the documented qualified baseline, not a claim of strong performance or full paper replication.

Model compatibility: compatible

Evidence:

```json
[
  "reports/RESULTS_AT_A_GLANCE.json"
]
```

**Molecular cloning question answering — Runnable now:** An existing completed declared Qwen run demonstrates that the input interface, execution harness and scorer can be used in this environment. This is readiness of the documented qualified baseline, not a claim of strong performance or full paper replication.

Model compatibility: compatible

Evidence:

```json
[
  "reports/RESULTS_AT_A_GLANCE.json"
]
```

##### LAB-Bench / LitQA2

**Native/local protocol:** `NATIVE_PUBLIC_COT_LOCAL_REVIEWED`

**Coverage:** reviewed_public_subset; completed_declared_run.

**Saved count record:**

```json
{
  "planned": 197,
  "completed": 197,
  "parsed": 197,
  "invalid_outputs": 0,
  "missing_or_failed_outputs": null,
  "held_before_inference": 2
}
```

**Complete stored metrics, including alternate/diagnostic values:**

```json
{
  "accuracy": 0.39086294416243655,
  "precision": 0.4095744680851064,
  "coverage": 0.9543147208121827,
  "n_total": 197,
  "n_correct": 77,
  "n_sure": 188
}
```

**Comparison qualification:** Native public questions, COT prompt, shuffle algorithm and deterministic parser/metrics. Two cases held; one seeded Qwen run, not the original three-run mean or full private/public set. No model-based answer-extraction fallback.

Public release 197/199; one seeded run, no tools; published decoder/repeats differ.

197/199 public cases; two held before inference. Original LAB paper includes private cases and means over three runs.

**All stored published-reference records — separate from the local run:**

```json
[
  {
    "model": "GPT-4o",
    "metrics": {
      "accuracy": 0.27,
      "precision": 0.46,
      "coverage": 0.58
    },
    "source_id": "LAB",
    "source_url": "https://arxiv.org/html/2407.10362v1",
    "source_locator": "Appendix Tables 2–4",
    "protocol": "full public+private; no tools; native zero-shot CoT; abstention choice",
    "value_status": "published_rounded_as_printed",
    "run_count": 3,
    "reported_std": null,
    "test_case_count": 248,
    "reported_decimal_places": 2
  },
  {
    "model": "Ryze public-set evaluation",
    "metrics": {
      "qwen3_vl_8b_accuracy_percent": 38.7,
      "gpt5_2_accuracy_percent": 45.7,
      "biovlm_8b_accuracy_percent": 65.5
    },
    "source_id": "RYZE",
    "source_url": "https://arxiv.org/html/2606.00902v1",
    "source_locator": "Table 1",
    "protocol": "1,967 public cases total; sample-weighted overall aggregation",
    "value_status": "published_rounded_as_printed",
    "run_count": null,
    "reported_std": null,
    "test_case_count": 199,
    "reported_decimal_places": 1,
    "scope_note": "BioVLM training/synthesis used benchmark-feedback loop; do not treat as a clean untouched-test model. Prompt, repeats and decoder details insufficiently pinned for exact replication."
  }
]
```

[Original score artifact](https://github.com/Some-random/bio-evaluation/blob/main/results/runs/qwen38_27b_litqa2_public_reviewed_2026-10-15/scores.json)

##### LAB-Bench / DbQA

**Native/local protocol:** `NATIVE_PUBLIC_COT_LOCAL_REVIEWED`

**Coverage:** reviewed_public_subset; completed_declared_run.

**Saved count record:**

```json
{
  "planned": 520,
  "completed": 520,
  "parsed": 427,
  "invalid_outputs": 93,
  "missing_or_failed_outputs": null,
  "held_before_inference": 0
}
```

**Complete stored metrics, including alternate/diagnostic values:**

```json
{
  "accuracy": 0.31346153846153846,
  "precision": 0.318359375,
  "coverage": 0.9846153846153847,
  "n_total": 520,
  "n_correct": 163,
  "n_sure": 512
}
```

**Comparison qualification:** Native public prompts, choices, required context/images and metrics. Reviewed public release; one fixed-seed run, not the original full public/private three-run paper mean. Strict deterministic parser; no model extraction fallback.

Public release 520/520; one seeded run, no tools; published decoder/repeats differ.

**All stored published-reference records — separate from the local run:**

```json
[
  {
    "model": "Ryze public-set evaluation",
    "metrics": {
      "qwen3_vl_8b_accuracy_percent": 31.2,
      "gpt5_2_accuracy_percent": 41.7,
      "biovlm_8b_accuracy_percent": 48.9
    },
    "source_id": "RYZE",
    "source_url": "https://arxiv.org/html/2606.00902v1",
    "source_locator": "Table 1",
    "protocol": "1,967 public cases total; sample-weighted overall aggregation",
    "value_status": "published_rounded_as_printed",
    "run_count": null,
    "reported_std": null,
    "test_case_count": 520,
    "reported_decimal_places": 1,
    "scope_note": "BioVLM training/synthesis used benchmark-feedback loop; do not treat as a clean untouched-test model. Prompt, repeats and decoder details insufficiently pinned for exact replication."
  }
]
```

[Original score artifact](https://github.com/Some-random/bio-evaluation/blob/main/results/runs/qwen38_27b_b02_public_reviewed_2026-10-15/scores.json)

##### LAB-Bench / SuppQA

**Native/local protocol:** `NATIVE_PUBLIC_COT_LOCAL_REVIEWED`

**Coverage:** reviewed_public_subset; completed_declared_run.

**Saved count record:**

```json
{
  "planned": 82,
  "completed": 82,
  "parsed": 82,
  "invalid_outputs": 0,
  "missing_or_failed_outputs": null,
  "held_before_inference": 0
}
```

**Complete stored metrics, including alternate/diagnostic values:**

```json
{
  "accuracy": 0.34146341463414637,
  "precision": 0.358974358974359,
  "coverage": 0.9512195121951219,
  "n_total": 82,
  "n_correct": 28,
  "n_sure": 78
}
```

**Comparison qualification:** Native public prompts, choices, required context/images and metrics. Reviewed public release; one fixed-seed run, not the original full public/private three-run paper mean. Strict deterministic parser; no model extraction fallback.

Public release 82/82; one seeded run, no tools; published decoder/repeats differ.

**All stored published-reference records — separate from the local run:**

```json
[
  {
    "model": "GPT-4o",
    "metrics": {
      "accuracy": 0.13,
      "precision": 0.47,
      "coverage": 0.29
    },
    "source_id": "LAB",
    "source_url": "https://arxiv.org/html/2407.10362v1",
    "source_locator": "Appendix Tables 2–4",
    "protocol": "full public+private; no tools; native zero-shot CoT; abstention choice",
    "value_status": "published_rounded_as_printed",
    "run_count": 3,
    "reported_std": null,
    "test_case_count": 102,
    "reported_decimal_places": 2
  },
  {
    "model": "Ryze public-set evaluation",
    "metrics": {
      "qwen3_vl_8b_accuracy_percent": 24.8,
      "gpt5_2_accuracy_percent": 48.8,
      "biovlm_8b_accuracy_percent": 44.2
    },
    "source_id": "RYZE",
    "source_url": "https://arxiv.org/html/2606.00902v1",
    "source_locator": "Table 1",
    "protocol": "1,967 public cases total; sample-weighted overall aggregation",
    "value_status": "published_rounded_as_printed",
    "run_count": null,
    "reported_std": null,
    "test_case_count": 82,
    "reported_decimal_places": 1,
    "scope_note": "BioVLM training/synthesis used benchmark-feedback loop; do not treat as a clean untouched-test model. Prompt, repeats and decoder details insufficiently pinned for exact replication."
  }
]
```

[Original score artifact](https://github.com/Some-random/bio-evaluation/blob/main/results/runs/qwen38_27b_b03_public_reviewed_2026-10-15/scores.json)

##### LAB-Bench / FigQA

**Native/local protocol:** `NATIVE_PUBLIC_COT_LOCAL_REVIEWED`

**Coverage:** reviewed_public_subset; completed_declared_run.

**Saved count record:**

```json
{
  "planned": 181,
  "completed": 181,
  "parsed": 180,
  "invalid_outputs": 1,
  "missing_or_failed_outputs": null,
  "held_before_inference": 0
}
```

**Complete stored metrics, including alternate/diagnostic values:**

```json
{
  "accuracy": 0.7569060773480663,
  "precision": 0.7696629213483146,
  "coverage": 0.9834254143646409,
  "n_total": 181,
  "n_correct": 137,
  "n_sure": 178
}
```

**Comparison qualification:** Native public prompts, choices, required context/images and metrics. Reviewed public release; one fixed-seed run, not the original full public/private three-run paper mean. Strict deterministic parser; no model extraction fallback.

Public release 181/181; one seeded run, no tools; published decoder/repeats differ.

Independent local source/mapping/request audit passed; public pretraining exposure remains unknown.

Original publisher JPEGs preserved; author-wrapper re-encoding differs in pixels under the diagnostic runtime. Historical encoding and accuracy impact are unknown.

**All stored published-reference records — separate from the local run:**

```json
[
  {
    "model": "GPT-4o",
    "metrics": {
      "accuracy": 0.29,
      "precision": 0.3,
      "coverage": 0.97
    },
    "source_id": "LAB",
    "source_url": "https://arxiv.org/html/2407.10362v1",
    "source_locator": "Appendix Tables 2–4",
    "protocol": "full public+private; no tools; native zero-shot CoT; abstention choice",
    "value_status": "published_rounded_as_printed",
    "run_count": 3,
    "reported_std": null,
    "test_case_count": 226,
    "reported_decimal_places": 2
  },
  {
    "model": "Ryze public-set evaluation",
    "metrics": {
      "qwen3_vl_8b_accuracy_percent": 24.7,
      "gpt5_2_accuracy_percent": 36.5,
      "biovlm_8b_accuracy_percent": 35.2
    },
    "source_id": "RYZE",
    "source_url": "https://arxiv.org/html/2606.00902v1",
    "source_locator": "Table 1",
    "protocol": "1,967 public cases total; sample-weighted overall aggregation",
    "value_status": "published_rounded_as_printed",
    "run_count": null,
    "reported_std": null,
    "test_case_count": 181,
    "reported_decimal_places": 1,
    "scope_note": "BioVLM training/synthesis used benchmark-feedback loop; do not treat as a clean untouched-test model. Prompt, repeats and decoder details insufficiently pinned for exact replication."
  }
]
```

[Original score artifact](https://github.com/Some-random/bio-evaluation/blob/main/results/runs/qwen38_27b_b04_public_reviewed_2026-10-15/scores.json)

##### LAB-Bench / TableQA

**Native/local protocol:** `NATIVE_PUBLIC_COT_LOCAL_REVIEWED`

**Coverage:** reviewed_public_subset; completed_declared_run.

**Saved count record:**

```json
{
  "planned": 244,
  "completed": 244,
  "parsed": 238,
  "invalid_outputs": 6,
  "missing_or_failed_outputs": null,
  "held_before_inference": 0
}
```

**Complete stored metrics, including alternate/diagnostic values:**

```json
{
  "accuracy": 0.8852459016393442,
  "precision": 0.9,
  "coverage": 0.9836065573770492,
  "n_total": 244,
  "n_correct": 216,
  "n_sure": 240
}
```

**Comparison qualification:** Native public prompts, choices, required context/images and metrics. Reviewed public release; one fixed-seed run, not the original full public/private three-run paper mean. Strict deterministic parser; no model extraction fallback.

Public release 244/244; one seeded run, no tools; published decoder/repeats differ.

Independent local source/mapping/request audit passed; public pretraining exposure remains unknown.

**All stored published-reference records — separate from the local run:**

```json
[
  {
    "model": "GPT-4o",
    "metrics": {
      "accuracy": 0.71,
      "precision": 0.75,
      "coverage": 0.95
    },
    "source_id": "LAB",
    "source_url": "https://arxiv.org/html/2407.10362v1",
    "source_locator": "Appendix Tables 2–4",
    "protocol": "full public+private; no tools; native zero-shot CoT; abstention choice",
    "value_status": "published_rounded_as_printed",
    "run_count": 3,
    "reported_std": null,
    "test_case_count": 305,
    "reported_decimal_places": 2
  },
  {
    "model": "Ryze public-set evaluation",
    "metrics": {
      "qwen3_vl_8b_accuracy_percent": 34.0,
      "gpt5_2_accuracy_percent": 36.9,
      "biovlm_8b_accuracy_percent": 45.6
    },
    "source_id": "RYZE",
    "source_url": "https://arxiv.org/html/2606.00902v1",
    "source_locator": "Table 1",
    "protocol": "1,967 public cases total; sample-weighted overall aggregation",
    "value_status": "published_rounded_as_printed",
    "run_count": null,
    "reported_std": null,
    "test_case_count": 244,
    "reported_decimal_places": 1,
    "scope_note": "BioVLM training/synthesis used benchmark-feedback loop; do not treat as a clean untouched-test model. Prompt, repeats and decoder details insufficiently pinned for exact replication."
  }
]
```

[Original score artifact](https://github.com/Some-random/bio-evaluation/blob/main/results/runs/qwen38_27b_b05_public_reviewed_2026-10-15/scores.json)

##### LAB-Bench / SeqQA

**Native/local protocol:** `NATIVE_PUBLIC_COT_LOCAL_REVIEWED`

**Coverage:** reviewed_public_subset; completed_declared_run.

**Saved count record:**

```json
{
  "planned": 600,
  "completed": 600,
  "parsed": 86,
  "invalid_outputs": 514,
  "missing_or_failed_outputs": null,
  "held_before_inference": 0
}
```

**Complete stored metrics, including alternate/diagnostic values:**

```json
{
  "accuracy": 0.12666666666666668,
  "precision": 0.12773109243697478,
  "coverage": 0.9916666666666667,
  "n_total": 600,
  "n_correct": 76,
  "n_sure": 595
}
```

**Comparison qualification:** Native public prompts, choices, required context/images and metrics. Reviewed public release; one fixed-seed run, not the original full public/private three-run paper mean. Strict deterministic parser; no model extraction fallback.

Public release 600/600; one seeded run, no tools; published decoder/repeats differ.

**All stored published-reference records — separate from the local run:**

```json
[
  {
    "model": "Ryze public-set evaluation",
    "metrics": {
      "qwen3_vl_8b_accuracy_percent": 43.4,
      "gpt5_2_accuracy_percent": 47.0,
      "biovlm_8b_accuracy_percent": 42.8
    },
    "source_id": "RYZE",
    "source_url": "https://arxiv.org/html/2606.00902v1",
    "source_locator": "Table 1",
    "protocol": "1,967 public cases total; sample-weighted overall aggregation",
    "value_status": "published_rounded_as_printed",
    "run_count": null,
    "reported_std": null,
    "test_case_count": 600,
    "reported_decimal_places": 1,
    "scope_note": "BioVLM training/synthesis used benchmark-feedback loop; do not treat as a clean untouched-test model. Prompt, repeats and decoder details insufficiently pinned for exact replication."
  }
]
```

[Original score artifact](https://github.com/Some-random/bio-evaluation/blob/main/results/runs/qwen38_27b_b07_public_reviewed_2026-10-15/scores.json)

##### LAB-Bench / Cloning scenarios

**Native/local protocol:** `NATIVE_PUBLIC_COT_LOCAL_REVIEWED`

**Coverage:** reviewed_public_subset; completed_declared_run.

**Saved count record:**

```json
{
  "planned": 33,
  "completed": 33,
  "parsed": 0,
  "invalid_outputs": 33,
  "missing_or_failed_outputs": null,
  "held_before_inference": 0
}
```

**Complete stored metrics, including alternate/diagnostic values:**

```json
{
  "accuracy": 0.0,
  "precision": 0.0,
  "coverage": 1.0,
  "n_total": 33,
  "n_correct": 0,
  "n_sure": 33
}
```

**Comparison qualification:** Native public prompts, choices, required context/images and metrics. Reviewed public release; one fixed-seed run, not the original full public/private three-run paper mean. Strict deterministic parser; no model extraction fallback.

Public release 33/33; one seeded run, no tools; published decoder/repeats differ.

All 33 outputs reached the 4096-token limit; zero parsed answers. The zero score does not establish wrong biological predictions.

Native abstention-based coverage is not the parse rate.

**All stored published-reference records — separate from the local run:**

```json
[
  {
    "model": "GPT-4o",
    "metrics": {
      "accuracy": 0.28,
      "precision": 0.37,
      "coverage": 0.77
    },
    "source_id": "LAB",
    "source_url": "https://arxiv.org/html/2407.10362v1",
    "source_locator": "Appendix Tables 2–4",
    "protocol": "full public+private; no tools; native zero-shot CoT; abstention choice",
    "value_status": "published_rounded_as_printed",
    "run_count": 3,
    "reported_std": null,
    "test_case_count": 41,
    "reported_decimal_places": 2
  },
  {
    "model": "Ryze public-set evaluation",
    "metrics": {
      "qwen3_vl_8b_accuracy_percent": 24.2,
      "gpt5_2_accuracy_percent": 36.4,
      "biovlm_8b_accuracy_percent": 38.4
    },
    "source_id": "RYZE",
    "source_url": "https://arxiv.org/html/2606.00902v1",
    "source_locator": "Table 1",
    "protocol": "1,967 public cases total; sample-weighted overall aggregation",
    "value_status": "published_rounded_as_printed",
    "run_count": null,
    "reported_std": null,
    "test_case_count": 33,
    "reported_decimal_places": 1,
    "scope_note": "BioVLM training/synthesis used benchmark-feedback loop; do not treat as a clean untouched-test model. Prompt, repeats and decoder details insufficiently pinned for exact replication."
  }
]
```

[Original score artifact](https://github.com/Some-random/bio-evaluation/blob/main/results/runs/qwen38_27b_b08_public_reviewed_2026-10-15/scores.json)

[Source 1](https://arxiv.org/html/2407.10362v1), [Source 2](https://huggingface.co/datasets/futurehouse/lab-bench)

#### ProteinLMBench protein-understanding questions

Knowledge/test-taking evaluation, not direct novel protein-function prediction.

Published source size/units: 944 manually verified questions; six choices per question.

**Protein understanding — Needs data or protocol:** Text questions with six choices fit the current Qwen interface. The 944-question release, held-out manifest, exact prompt and answer normalization are not prepared; this can be a zero-shot baseline without reproducing the paper's supervised fine-tuning.

Model compatibility: compatible

Evidence:

```json
[
  "reports/TASK_HIERARCHY_DATA.json",
  "handoff/Bio_Evaluation_Agent_Package_2026-10-16/EVALUATION_INVENTORY.csv",
  "reports/local_model_capability_smoke.json"
]
```

Published reference record: InternLM2-7B after SFT: 58.26% accuracy; SSL+SFT: 62.18%.

[Source 1](https://arxiv.org/html/2406.05540v1), [Source 2](https://huggingface.co/datasets/tsynbio/ProteinLMBench)

#### PubMedQA research-abstract questions

The conclusion/long answer must stay out of solver input under the reasoning-required protocol.

Published source size/units: 1,000 expert-labeled records total; official evaluation split must be pinned. 61.2K unlabeled and 211.3K artificial records are separate training resources.

**Research-abstract question answering — Needs data or protocol:** Question plus abstract is compatible with Qwen. Pin the expert-labeled test split and answer normalization, and exclude the conclusion/long answer from the prompt; the source payload and frozen execution protocol are not prepared.

Model compatibility: compatible

Evidence:

```json
[
  "reports/TASK_HIERARCHY_DATA.json",
  "handoff/Bio_Evaluation_Agent_Package_2026-10-16/EVALUATION_INVENTORY.csv",
  "reports/local_model_capability_smoke.json"
]
```

Published reference record: Original BioBERT multi-phase training: 68.1% accuracy; reported human baseline 78.0%. Historical results.

[Source 1](https://arxiv.org/abs/1909.06146), [Source 2](https://github.com/pubmedqa/pubmedqa)

## Protein design

#### Protein sequence and structure generation

#### ProteinBench unconditional backbone generation

Reported values retained on the paper's scale; structural plausibility does not establish function.

Published source size/units: Length-stratified generation at 100/200/300/400/500 aa; 100 single-chain reference structures. Exact generated count must follow the release.

**Unconditional protein backbone generation — Needs additional models/tools:** The required output is a 3D backbone at a fixed length, followed by inverse-folding/refolding consistency evaluation. The current Qwen baseline has no validated coordinate-generation adapter or structural evaluators; generated amino-acid text would be a different task.

Model compatibility: needs specialist pipeline

Evidence:

```json
[
  "reports/TASK_HIERARCHY_DATA.json",
  "handoff/Bio_Evaluation_Agent_Package_2026-10-16/EVALUATION_INVENTORY.csv",
  "reports/local_model_capability_smoke.json"
]
```

Published reference record: At length 100: RFdiffusion scTM 0.98 ± 0.12 and scRMSD 0.48 ± 0.56 Å; FrameFlow 0.94 ± 0.08 and 0.70 ± 0.70 Å.

[Source 1](https://arxiv.org/html/2409.06744v2), [Source 2](https://proteinbench.github.io/)

#### ProteinBench unconditional sequence generation

pLDDT is confidence, not experimentally measured protein stability or function.

Published source size/units: 50 sequences per model at each length 100, 200, 300 and 500.

**Unconditional protein sequence generation — Needs additional models/tools:** Qwen can propose amino-acid sequences as an adaptation, but the native reported metrics require a fixed folding evaluator such as AF2. That evaluator, length-specific generation contract and full scoring pipeline are not prepared; text generation alone does not complete this benchmark.

Model compatibility: needs specialist pipeline

Evidence:

```json
[
  "reports/TASK_HIERARCHY_DATA.json",
  "handoff/Bio_Evaluation_Agent_Package_2026-10-16/EVALUATION_INVENTORY.csv",
  "reports/local_model_capability_smoke.json"
]
```

Published reference record: At length 100, predicted AF2 pLDDT: DPLM-650M 85.38 ± 14.20; ProGen2-700M 64.00 ± 21.26.

[Source 1](https://arxiv.org/html/2409.06744v2), [Source 2](https://proteinbench.github.io/)

#### ProteinBench joint sequence–structure generation

These are selected length-specific results, not one design success rate.

Published source size/units: Length-stratified generated samples; exact per-setting candidate count not recovered.

**Joint sequence and structure generation — Needs additional models/tools:** The task jointly emits sequence and coordinates and scores structural self-consistency. Current Qwen has no validated joint structure-output adapter and the specialized structural evaluators are not prepared; plain sequence generation would not match the protocol.

Model compatibility: needs specialist pipeline

Evidence:

```json
[
  "reports/TASK_HIERARCHY_DATA.json",
  "handoff/Bio_Evaluation_Agent_Package_2026-10-16/EVALUATION_INVENTORY.csv",
  "reports/local_model_capability_smoke.json"
]
```

Published reference record: Multiflow at length 100: scTM 0.96 ± 0.04; scRMSD 1.10 ± 0.71 Å. At length 200: scTM 0.95; scRMSD 1.61 Å.

[Source 1](https://arxiv.org/html/2409.06744v2), [Source 2](https://proteinbench.github.io/)

#### BioT5+ description-guided protein generation

Qualitative design case A plausible or similar sequence is not a measured successful design.

Published source size/units: Can the model propose a sequence matching a description? The paper does not define a generally established benchmark for this task.

**Text-conditioned protein-sequence design:** Qualitative cases and sequence/reference comparisons. The paper does not define a generally established benchmark for this task.

A plausible or similar sequence is not a measured successful design.

**Text-conditioned protein-sequence design — Runnable now:** A prospectively frozen 59-case benign subset from the first 64 source-order cases is running with the pinned Qwen model and unchanged 4,096-token baseline. Five reviewed cases and 5,812 unreviewed cases remain held. The released paired-reference ROUGE algorithm is hash-pinned and tested; full original prompts/targets and an explicit output-format instruction form a qualified Qwen adaptation. Native T5 tokenizer/truncation and paper normalized Smith-Waterman are not reproduced; no biological-function success or full 5,876-case completion is claimed.

Model compatibility: compatible

Evidence:

```json
[
  "reports/P36_PREPARATION_2026-10-16.json",
  "handoff/p36_reviewed_subset_2026-10-16/proposed_config.json",
  "results/runs/p36-qwen3.8-27b-biot5-reviewed59-20261016/upload_status.json"
]
```

Published reference record: Description-guided protein designs are presented as qualitative cases rather than a fixed, experimentally validated design-success rate.

[Source 1](https://arxiv.org/html/2402.17810v2)

#### NatureLM generated proteins: unconditional / property-conditioned / heme

Predictor-scored or qualitative design Diversity and predicted structure confidence do not establish function. | Predictor agreement, not experimentally measured stability/solubility of each generated sequence. | Self-description is not independent validation; predicted complexes are not measured binding.

Published source size/units: Does the model generate varied, structurally plausible protein sequences? / Do sequences requested to have a property score well under the evaluator? / Can conditioning suggest proteins plausibly associated with heme? Generated samples compared with natural sequences; not a labeled holdout prediction set. | Paper uses a natural UR50 reference subset of 1,000 sequences in the conditioned comparison. | Selected candidates; no standard released labeled test-set size.

**Unconditional protein generation:** Length distribution; clustering-based diversity; pLDDT. Generated samples compared with natural sequences; not a labeled holdout prediction set.

Diversity and predicted structure confidence do not establish function.

**Protein generation for predicted stability and solubility:** Predicted property scores; diversity. Paper uses a natural UR50 reference subset of 1,000 sequences in the conditioned comparison.

Predictor agreement, not experimentally measured stability/solubility of each generated sequence.

**Heme-binding protein candidate generation:** Qualitative description/complex screening. Selected candidates; no standard released labeled test-set size.

Self-description is not independent validation; predicted complexes are not measured binding.

**Unconditional protein generation — Needs additional models/tools:** Qwen can generate protein sequence strings; the task is not blocked by text-interface suitability. Completing the recorded evaluation requires the frozen OmegaFold checkpoint/settings, clustering implementation, native sample/validity rules and UR50 reference cohort. Predicted structure confidence is not measured protein function.

Model compatibility: compatible

Evidence:

```json
[
  "reports/naturelm_generation_feasibility_2026-10-15.json"
]
```

**Protein generation for predicted stability and solubility — Needs additional models/tools:** Conditioned sequence generation is compatible with Qwen, but the original trained SFM-Protein binary property heads, probability orientation, source sampling/failure rules and UR50 reference IDs are unrecovered. Generic sequence heuristics or newly trained substitute heads would not complete this evaluation.

Model compatibility: compatible

Evidence:

```json
[
  "reports/naturelm_generation_feasibility_2026-10-15.json"
]
```

**Heme-binding protein candidate generation — Needs additional models/tools:** Qwen can propose sequence strings from the condition, but the native HemeList, candidate/selection manifest and Protenix structure/complex evaluator are not prepared. No fixed full-cohort success denominator is recovered; predicted complexes do not establish measured heme binding.

Model compatibility: compatible

Evidence:

```json
[
  "reports/REMAINING_DESIGN_SOURCE_FEASIBILITY_2026-10-15.json"
]
```

Published reference record: Reported outputs are diversity/length distributions and predicted structural confidence. No experimentally measured function-success fraction is supplied by this evaluation. The reported comparison uses learned stability/solubility scores and diversity. No measured stability/solubility success rate is transcribed. Selected heme-binding candidates are screened with descriptions and predicted complexes; this is not experimentally demonstrated heme binding.

[Source 1](https://arxiv.org/html/2502.07527v3)

#### GFP sequence optimization

#### STRIDE GFP sequence optimization

Predictor-scored generation These 100 candidates are not a wet-lab test set. Correctly applying edits does not validate fluorescence.

Published source size/units: Do proposed edits improve the fixed scorer's predicted fluorescence? 100 candidates per method from a common source; separate replace-only and full-edit settings.

**GFP sequence optimization against a fluorescence predictor:** Predicted improvement/success; uniqueness; novelty. 100 candidates per method from a common source; separate replace-only and full-edit settings.

These 100 candidates are not a wet-lab test set. Correctly applying edits does not validate fluorescence.

**GFP sequence optimization against a fluorescence predictor — Runnable now:** The existing 200-candidate, two-regime evaluation has a frozen trained SaProt fluorescence CPU evaluator with restored checkpoint tensors and authorized oracle configuration. All 200 outputs were invalid, yielding zero qualified successes and undefined novelty/uniqueness; these are partial observed outcomes, not absence of an oracle. The native novelty reference remains unavailable, and the condition is not full paper replication.

Model compatibility: compatible

Evidence:

```json
[
  "reports/RESULTS_AT_A_GLANCE.json",
  "configs/local_stride_gfp_p42.json",
  "reports/stride_gfp_cpu_oracle_freeze.json",
  "reports/stride_gfp_oracle_state_restoration.json",
  "reports/local_stride_gfp_p42_dispatch.json"
]
```

##### STRIDE GFP generated-candidate evaluation

**Native/local protocol:** `QWEN_GFP_QUALIFIED_TWO_REGIMES_ENDPOINT_1_TO_3`

**Coverage:** qualified_full200_two_endpoint_regimes_native_novelty_withheld; completed_declared_run.

**Saved count record:**

```json
{
  "planned": 200,
  "completed": 200,
  "parsed": 0,
  "invalid_outputs": 200,
  "missing_or_failed_outputs": 0,
  "held_before_inference": null
}
```

**Complete stored metrics, including alternate/diagnostic values:**

```json
{
  "replace_only": {
    "qualified_oracle_success": 0.0,
    "improved_sequence_uniqueness": null,
    "native_novelty": null
  },
  "full_atomic": {
    "qualified_oracle_success": 0.0,
    "improved_sequence_uniqueness": null,
    "native_novelty": null
  }
}
```

**All stored published-reference records — separate from the local run:**

```json
[
  {
    "model": "STRIDE",
    "metrics": {
      "success_count": 61,
      "attempt_count": 100,
      "unique_improved_count": 59,
      "novel_unique_improved_count": 53
    },
    "source_id": "STRIDE",
    "source_url": "https://arxiv.org/html/2603.03573v1",
    "source_locator": "Table 4",
    "protocol": "replace_only; fixed avGFP source, 1–3 edit operations, fixed fluorescence predictor",
    "value_status": "published_rounded_as_printed",
    "run_count": null,
    "reported_std": null,
    "test_case_count": 100,
    "source_inconsistency": null
  },
  {
    "model": "STRIDE",
    "metrics": {
      "success_count": 89,
      "attempt_count": 100,
      "unique_improved_count": 78,
      "novel_unique_improved_count": 76
    },
    "source_id": "STRIDE",
    "source_url": "https://arxiv.org/html/2603.03573v1",
    "source_locator": "Table 3",
    "protocol": "add_delete_replace; fixed avGFP source, 1–3 edit operations, fixed fluorescence predictor",
    "value_status": "published_rounded_as_printed",
    "run_count": null,
    "reported_std": null,
    "test_case_count": 100,
    "source_inconsistency": "Full-action Table3 prints Unique 78/79 although success=89/100 and narrative unique=78; preserve counts and flag denominator inconsistency."
  }
]
```

[Original score artifact](https://github.com/Some-random/bio-evaluation/blob/main/results/runs/qwen38_27b_p42_gfp_qualified_two_regimes_2026-10-15/scores.json)

[Source 1](https://arxiv.org/html/2603.03573v1)

#### Antibody design

#### RAbD — CDR-H3 redesign

Geometry and native-sequence recovery disagree; no dominance claim across all metrics. Not prospective binding success. ProteinBench's 55-complex processed version is separately listed.

Published source size/units: 60 antibody–antigen complexes.

**Antibody design: CDR-H3 redesign:** NatureLM: AAR. Proteo-R1: AAR, RMSD, lDDT, TM-score, DockQ.. 60 complexes; retain paper-specific renumbering, masked region and preprocessing.

High native recovery or geometric similarity does not imply measured binding for a new design.

**Antibody design: CDR-H3 redesign — Needs additional models/tools:** The full sequence/structure redesign protocol requires exact antibody masks, antigen/framework coordinates, processed retained cases and geometry/interface evaluation. Current Qwen text/vision serving does not provide that specialist structure-generation/evaluation pipeline. Dropping 3D context for a sequence-only prompt would change the task.

Model compatibility: needs specialist pipeline

Evidence:

```json
[
  "reports/REMAINING_DESIGN_SOURCE_FEASIBILITY_2026-10-15.json"
]
```

Published reference record: Proteo-R1 vs BoltzGen: AAR 10.75% vs 39.07%; RMSD 2.46 Å vs 2.69 Å; DockQ 0.801 vs 0.473.

[Source 1](https://arxiv.org/html/2605.02937v1), [Source 2](https://arxiv.org/html/2605.02937v1)

#### SAbDab — Proteo-R1 all-CDR holdout

One dataset, multiple metrics. H3 RMSD and Loop-RMSD are different columns. Oracle-Anchor row is not the deployed system.

Published source size/units: Paper-specific temporal/cluster split; exact processed test count not recovered.

**Antibody design: multi-CDR redesign:** Structural/recovery/interface metrics; Rosetta-derived energy and clash diagnostics. Release-time filtering and 50%-identity H3 clusters; 9:0.5:0.5 cluster split. Exact test count not established.

Computational reconstruction/design. The original docking pose is assumed known; not unconstrained binder discovery.

**Antibody design: multi-CDR redesign — Needs additional models/tools:** The exact all-CDR SAbDab holdout/masks and full antigen/framework geometry are missing. Native evaluation also uses specialist structure encoding, CDR hidden-state/diffusion machinery and Rosetta/ABMPNN processing; current Qwen text/vision serving is not that pipeline. Five demonstrations cannot replace the test set.

Model compatibility: needs specialist pipeline

Evidence:

```json
[
  "reports/REMAINING_DESIGN_SOURCE_FEASIBILITY_2026-10-15.json"
]
```

Published reference record: Proteo-R1 vs MFDesign: H3 RMSD 3.81 Å vs 3.71 Å; Loop-RMSD 4.51 Å vs 4.28 Å; IMP 56.58 vs 59.16 (paper's scale).

[Source 1](https://arxiv.org/html/2605.02937v1), [Source 2](https://arxiv.org/html/2605.02937v1)

#### ProteinBench antibody design — processed RAbD

Same parent resource does not mean identical split or scorer. This is a distinct protocol, not 55 additional independent complexes.

Published source size/units: 55 retained RAbD complexes; differs from the 60-complex protocol in the earlier catalog.

**Antibody design: CDR-H3 redesign — Needs additional models/tools:** Native H3 redesign uses complex geometry and masked-loop context and scores both sequence recovery and coordinates. A validated geometry-conditioned design adapter plus structural reconstruction/evaluation are missing; sequence-only CDR text would be a disclosed reduced-input adaptation, not the 55-complex native protocol.

Model compatibility: needs specialist pipeline

Evidence:

```json
[
  "reports/TASK_HIERARCHY_DATA.json",
  "handoff/Bio_Evaluation_Agent_Package_2026-10-16/EVALUATION_INVENTORY.csv",
  "reports/local_model_capability_smoke.json"
]
```

Published reference record: DiffAb: AAR 35.04 ± 8.36%, RMSD 2.53 ± 0.60 Å; MEAN: AAR 33.47%, RMSD 1.82 Å.

[Source 1](https://arxiv.org/html/2409.06744v2), [Source 2](https://proteinbench.github.io/)

#### CHIMERA-Bench epitope-conditioned antibody design

EpiF1 measures intended-site contact, not empirical selectivity across off-target molecules.

Published source size/units: 2,922 complexes total. Test: 292 epitope-group; 292 antigen-fold; 293 temporal. Splits are alternatives, not additive test sets.

**Antibody design: epitope-conditioned design — Needs additional models/tools:** The native output includes CDR sequence and structure conditioned on antigen/framework/epitope context. Current Qwen lacks a validated geometry adapter and the required reconstruction/docking/contact evaluators; matching the paper's retrained design systems is outside a Qwen-only zero-shot baseline.

Model compatibility: needs specialist pipeline

Evidence:

```json
[
  "reports/TASK_HIERARCHY_DATA.json",
  "handoff/Bio_Evaluation_Agent_Package_2026-10-16/EVALUATION_INVENTORY.csv",
  "reports/local_model_capability_smoke.json"
]
```

Published reference record: Epitope-group H3: RAAD AAR 0.37, RMSD 1.75 Å, DockQ 0.58; dyMEAN EpiF1 0.23 (RAAD 0.11).

[Source 1](https://arxiv.org/html/2603.13431v1), [Source 2](https://github.com/mansoor181/chimera-bench)

#### Inverse folding

#### CATH 4.2 / TS50 / TS500 inverse folding

Recovery is not experimental fold/function validation; named size does not replace retained-record manifest.

Published source size/units: CATH 4.2 exact test count not re-established; TS50/TS500 named test suites (50/500 nominal structures; exact retained manifests must be checked).

**Sequence design by inverse folding — Needs additional models/tools:** Native inverse folding conditions on backbone coordinates. The current baseline has no validated coordinate-conditioned sequence adapter; reproducing the native protocol needs inverse-folding/structure tools and retained structure manifests. A sequence-only prompt would omit the conditioning information.

Model compatibility: needs specialist pipeline

Evidence:

```json
[
  "reports/TASK_HIERARCHY_DATA.json",
  "handoff/Bio_Evaluation_Agent_Package_2026-10-16/EVALUATION_INVENTORY.csv",
  "reports/local_model_capability_smoke.json"
]
```

Published reference record: PiFold repository: CATH recovery 51.66%; TS50 58.72%; TS500 60.42%.

[Source 1](https://github.com/a4bio/pifold), [Source 2](https://github.com/a4bio/pifold)

#### ProteinBench inverse folding — CASP15 / CAMEO / synthetic backbones

Some models are excluded from native recovery because of training exposure. Synthetic consistency is model-scored, not wet-lab.

Published source size/units: 32 CASP15 structures; 332 CAMEO complexes; synthetic backbones: 10 at each of 5 lengths (100–500 aa).

**Sequence design by inverse folding — Needs additional models/tools:** Native recovery conditions on CASP15/CAMEO/synthetic backbone coordinates, with structure-based consistency checks. No validated coordinate adapter or associated evaluators are prepared; native execution needs inverse-folding/refolding tools and exact retained manifests.

Model compatibility: needs specialist pipeline

Evidence:

```json
[
  "reports/TASK_HIERARCHY_DATA.json",
  "handoff/Bio_Evaluation_Agent_Package_2026-10-16/EVALUATION_INVENTORY.csv",
  "reports/local_model_capability_smoke.json"
]
```

Published reference record: AAR, CASP15/CAMEO: LM-Design 0.516/0.570; ProteinMPNN 0.450/0.468.

[Source 1](https://arxiv.org/html/2409.06744v2), [Source 2](https://proteinbench.github.io/)

#### Functional-motif scaffolding

#### MotifBench functional-motif scaffolding

Score is not percentage of experimentally functional proteins. Preserve sampling and evaluator versions.

Published source size/units: 30 motif problems; standard submission 100 scaffolds per problem.

**Functional-motif scaffolding — Needs additional models/tools:** Native conditioning includes motif coordinates and geometric constraints, then scaffold generation, sequence design and structural verification. No validated geometry adapter or MotifBench design/refolding pipeline is prepared for Qwen; text-only proposals would change the protocol.

Model compatibility: needs specialist pipeline

Evidence:

```json
[
  "reports/TASK_HIERARCHY_DATA.json",
  "handoff/Bio_Evaluation_Agent_Package_2026-10-16/EVALUATION_INVENTORY.csv",
  "reports/local_model_capability_smoke.json"
]
```

Published reference record: Official leaderboard snapshot: RFdiffusion3 43.52 ± 1.35 (Aug 2026); RFdiffusion 21.95 (Feb 2025), in MotifBench-score units.

[Source 1](https://github.com/blt2114/MotifBench), [Source 2](https://github.com/blt2114/MotifBench)

#### ProteinBench motif scaffolding — legacy motif panel

Do not merge the legacy panel with MotifBench or reuse their scores interchangeably.

Published source size/units: Legacy 17 (25) motif-problem panel described by ProteinBench; not MotifBench's separate 30-problem set.

**Functional-motif scaffolding — Needs additional models/tools:** The legacy panel requires motif-conditioned 3D scaffolds and a fixed structural evaluation pipeline. No validated Qwen geometry adapter or corresponding design/refolding tools are prepared; its legacy manifest must remain separate from MotifBench.

Model compatibility: needs specialist pipeline

Evidence:

```json
[
  "reports/TASK_HIERARCHY_DATA.json",
  "handoff/Bio_Evaluation_Agent_Package_2026-10-16/EVALUATION_INVENTORY.csv",
  "reports/local_model_capability_smoke.json"
]
```

Published reference record: Comparative motif-scaffolding results are reported; exact figure-derived score not transcribed.

[Source 1](https://arxiv.org/html/2409.06744v2), [Source 2](https://proteinbench.github.io/)

#### Target-binder design

#### ProtDBench de novo target-binder design

Counts of computational passes, not wet-lab hit fractions. Exact target-specific conditions and verifier must match.

Published source size/units: 10 target proteins; 24 h on one A100 per method/target setting. Includes generation, inverse folding and scoring.

**Target-binder design — Needs additional models/tools:** The native time-budgeted pipeline combines target geometry, binder generation, inverse folding and structural filtering. Additional design/refolding/scoring tools are required; Qwen sequence proposals alone cannot yield the published passing-backbone counts.

Model compatibility: needs specialist pipeline

Evidence:

```json
[
  "reports/TASK_HIERARCHY_DATA.json",
  "handoff/Bio_Evaluation_Agent_Package_2026-10-16/EVALUATION_INVENTORY.csv",
  "reports/local_model_capability_smoke.json"
]
```

Published reference record: PD-L1 passing-backbone counts: PXDesign 1,247; BoltzGen 549; RFdiffusion3 542; BindCraft 231. TNFα: PXDesign 57; BoltzGen 15.

[Source 1](https://arxiv.org/html/2605.04118v1), [Source 2](https://arxiv.org/html/2605.04118v1)

#### Prompteina text-conditioned protein design — GM2A campaign

Prospective experimental campaign A single target campaign, not a general fixed test set or aggregate success rate. 52.4M captions is a training size.

Published source size/units: Generate target binders from language specifications; measure selected designs prospectively. 1,000-design computational budget; 90 selected; 89 expressed and assayed.

**Text-conditioned target-binder design — Needs additional models/tools:** Qwen can generate sequences from text, but this campaign's binder/KD endpoints require structural selection plus prospective expression and binding assays. Text output cannot reproduce its measured success rate; a new computational-only adaptation would need a separate scoring protocol.

Model compatibility: needs specialist pipeline

Evidence:

```json
[
  "reports/TASK_HIERARCHY_DATA.json",
  "handoff/Bio_Evaluation_Agent_Package_2026-10-16/Biological_Evaluation_Master.xlsx",
  "reports/local_model_capability_smoke.json"
]
```

Published reference record: 9 of 89 assayed designs classified as binders; 8 fitted apparent KD values. Strongest apparent KD: 107 nM.

[Source 1](https://arxiv.org/html/2610.13917v1)

## Structure and conformational prediction

#### Local structure and residue prediction

#### ATOM3D residue identity from local structure (RES)

Environment count is not protein count. This is an established held-out structure task, unlike unverified internal diagnostics.

Published source size/units: Test: 3,319 PDB structures yielding 1,261,342 local environments; train: 21,147 structures.

**Residue identity from local structure — Needs additional models/tools:** Native predictions use masked 3D local atomic environments. No validated atomic-coordinate adapter is prepared for Qwen; a geometry-capable model or separately specified coordinate adapter is required to preserve the task rather than replace it with sequence-context guessing.

Model compatibility: needs specialist pipeline

Evidence:

```json
[
  "reports/TASK_HIERARCHY_DATA.json",
  "handoff/Bio_Evaluation_Agent_Package_2026-10-16/EVALUATION_INVENTORY.csv",
  "reports/local_model_capability_smoke.json"
]
```

Published reference record: ATOM3D 3D-CNN test accuracy: 0.451.

[Source 1](https://arxiv.org/html/2012.04035v3), [Source 2](https://www.atom3d.ai/)

#### PFMBench structure-derived prediction panel

These are PFMBench-specific processed datasets/splits, not interchangeable with PEER/ProtST results. F1 is not Fmax. Affinity-named AUROC tasks are classification, not KD regression. Exact loaders required.

Published source size/units: Test sizes: Contact: 1,501; FoldClass: 1,630; SecondaryStructure: 8,262

**Structure-derived protein prediction — Needs data or protocol:** Sequence input allows a disclosed Qwen adaptation, but the exact processed splits and output schemas are not prepared. Fold class, per-residue secondary structure and ranked contact pairs require separate scoring contracts; a dense contact map may exceed the frozen output budget and must be checked before declaring that endpoint runnable.

Model compatibility: compatible

Evidence:

```json
[
  "reports/TASK_HIERARCHY_DATA.json",
  "handoff/Bio_Evaluation_Agent_Package_2026-10-16/EVALUATION_INVENTORY.csv",
  "reports/local_model_capability_smoke.json"
]
```

Published reference record: ESM2-Adapter, Table 1 means: Contact Top L/5 0.7199; FoldClass Accuracy 0.7859; SecondaryStructure Accuracy 0.7601

[Source 1](https://arxiv.org/html/2506.14796v1), [Source 2](https://github.com/biomap-research/PFMBench)

#### Structure-derived questions and output checks

#### Proteo-R1 internal alignment / structural / CDR diagnostics

Internal diagnostic — holdout unresolved Not a named released PDB benchmark. Eight-response averages are not pass@8. No evidence of leakage is inferred from missing documentation.

Published source size/units: Check training-stage behavior on calculated structural questions and output-schema tasks. Independent held-out question manifest and size unresolved; 9.09M is Stage-II TRAINING instances.

**Internal structural and alignment diagnostics — Needs data or protocol:** The independent held-out question manifest, allowed structural representation and per-task answer/scoring schemas are unresolved. Some schema/text questions may fit Qwen, while geometry questions need an adapter; do not declare the combined diagnostic runnable or treat training-instance counts as test evidence.

Model compatibility: unresolved

Evidence:

```json
[
  "reports/TASK_HIERARCHY_DATA.json",
  "handoff/Bio_Evaluation_Agent_Package_2026-10-16/Biological_Evaluation_Master.xlsx",
  "reports/local_model_capability_smoke.json"
]
```

Published reference record: Selected Stage-II M3: contact 58.3%; interface 15.1%; hotspot 11.6%. Separate Stage-I schema 81.4%. No overall score.

[Source 1](https://arxiv.org/html/2605.02937v1)

#### Protein structure ranking

#### ATOM3D protein structure ranking (PSR)

Ranking a supplied set of structures is not de novo structure generation.

Published source size/units: CASP-derived target/decoy split; exact processed test-target/decoy counts not transcribed.

**Protein structure ranking — Needs additional models/tools:** The task ranks coordinate decoys by structural quality. A validated geometry-to-quality adapter or structural scoring model is missing, along with the exact decoy manifest; language-only descriptions would omit the native inputs.

Model compatibility: needs specialist pipeline

Evidence:

```json
[
  "reports/TASK_HIERARCHY_DATA.json",
  "handoff/Bio_Evaluation_Agent_Package_2026-10-16/EVALUATION_INVENTORY.csv",
  "reports/local_model_capability_smoke.json"
]
```

Published reference record: Per-target mean Spearman: GNN 0.515; 3D-CNN 0.431. Global correlations are different metrics.

[Source 1](https://arxiv.org/html/2012.04035v3), [Source 2](https://www.atom3d.ai/)

#### Protein folding

#### ProteinBench single-state folding — CAMEO 2022

Models may have different MSA/template access. This is a historical target cohort, not the live CAMEO leaderboard.

Published source size/units: 183 proteins (<750 residues), released Aug–Oct 2022.

**Single-state protein folding — Needs additional models/tools:** Native folding requires protein coordinates and structural comparison to references. Current Qwen has no validated structure-generation adapter; a folding model/tool and the exact MSA/template access protocol would be needed, making this more than Qwen-only text inference.

Model compatibility: needs specialist pipeline

Evidence:

```json
[
  "reports/TASK_HIERARCHY_DATA.json",
  "handoff/Bio_Evaluation_Agent_Package_2026-10-16/EVALUATION_INVENTORY.csv",
  "reports/local_model_capability_smoke.json"
]
```

Published reference record: AF2 mean/median TM-score 0.871/0.952, RMSD 3.21/1.64 Å; ESMFold 0.847/0.929 and 3.98/2.10 Å.

[Source 1](https://arxiv.org/html/2409.06744v2), [Source 2](https://proteinbench.github.io/)

#### Protein conformations and dynamics

#### ProteinBench multistate conformations — apo/holo and BPTI

Sample count is not the number of independent test proteins; BPTI alone gives narrow generalization evidence.

Published source size/units: Apo/holo: 91 protein pairs, 20 generated conformations per protein. BPTI: one 58-residue protein, 5 MD clusters, N=10/100/1000 samples.

**Multistate protein conformations — Needs additional models/tools:** The native target is a sampled 3D conformational ensemble, not a text label. A conformational generator and structural ensemble evaluation tools are needed; current Qwen has no validated coordinate/ensemble output protocol.

Model compatibility: needs specialist pipeline

Evidence:

```json
[
  "reports/TASK_HIERARCHY_DATA.json",
  "handoff/Bio_Evaluation_Agent_Package_2026-10-16/EVALUATION_INVENTORY.csv",
  "reports/local_model_capability_smoke.json"
]
```

Published reference record: Apo/holo TM-ensemble: AlphaFlow-PDB 0.873; MSA-depth256 0.867. BPTI N=1000: ConfDiff-ESM-force ensemble RMSD 1.36 Å.

[Source 1](https://arxiv.org/html/2409.06744v2), [Source 2](https://proteinbench.github.io/)

#### ProteinBench ensemble distribution — ATLAS

MD reference is simulation-derived, not an exhaustive experimental distribution. Preserve alignment, projection and aggregation.

Published source size/units: 82 held-out proteins; 250 generated conformations per protein.

**Protein conformational ensembles — Needs additional models/tools:** Native ATLAS evaluation compares distributions of generated coordinates to MD trajectories. Current Qwen has no validated ensemble generator and the alignment/projection/distributional scoring pipeline is not prepared; sequence text alone cannot supply these metrics.

Model compatibility: needs specialist pipeline

Evidence:

```json
[
  "reports/TASK_HIERARCHY_DATA.json",
  "handoff/Bio_Evaluation_Agent_Package_2026-10-16/EVALUATION_INVENTORY.csv",
  "reports/local_model_capability_smoke.json"
]
```

Published reference record: AlphaFlow-MD: per-target RMSF correlation 0.85 and PCA-Wasserstein 1.55; ConfDiff PCA-Wasserstein 1.41 (paper's units).

[Source 1](https://arxiv.org/html/2409.06744v2), [Source 2](https://proteinbench.github.io/)

#### BioEmu benchmark collection — states, dynamics and free energy

Pin benchmark/model revision: version changes affect values. Panel scores are not one pooled success rate.

Published source size/units: Multiple panels: domain motion, local unfolding, cryptic pockets, MD emulation and experimental folding free energies. Exact panel sizes not re-counted.

**Protein states, dynamics and free energy — Needs additional models/tools:** The benchmark needs structural ensembles and specialized state/dynamics/free-energy evaluation. Current Qwen has no validated conformational sampler; a suitable structural model and version-pinned BioEmu benchmark tooling are needed to run the native panels.

Model compatibility: needs specialist pipeline

Evidence:

```json
[
  "reports/TASK_HIERARCHY_DATA.json",
  "handoff/Bio_Evaluation_Agent_Package_2026-10-16/EVALUATION_INVENTORY.csv",
  "reports/local_model_capability_smoke.json"
]
```

Published reference record: Official model card: domain-motion coverage 83%; cryptic-pocket apo/holo coverage 55%/88%; experimental stability MAE ~0.9 kcal/mol, Spearman ~0.6.

[Source 1](https://github.com/microsoft/bioemu/blob/main/MODEL_CARD.md), [Source 2](https://github.com/microsoft/bioemu-benchmarks)

## Biomedical visual evidence

#### Biomedical visual question answering

#### Biomedical VQA: VQA-RAD / SLAKE-English / PathVQA / VQA-Med 2019

Medical-image performance does not show use of protein sequence/structure embeddings. Open-answer scorers differ between papers. | Medical-image performance does not show use of protein sequence/structure embeddings. Open-answer scorers differ between papers. | Medical-image performance does not show use of protein sequence/structure embeddings. Open-answer scorers differ between papers. | Medical-image performance does not show use of protein sequence/structure embeddings. Open-answer scorers differ between papers.

Published source size/units: Distinct official task splits; exact test counts not re-established. Open/closed answer groups must remain separate.

**Radiology image question answering:** Closed-question accuracy; open scoring is paper-specific (e.g. token recall in original LLaVA-Med). Use task's official train/test split; do not use total corpus size as test size.

Medical-image performance does not show use of protein sequence/structure embeddings. Open-answer scorers differ between papers.

**Medical image question answering in English:** Closed-question accuracy; open scoring is paper-specific (e.g. token recall in original LLaVA-Med). English subset; exact partition and normalization must match the target paper.

Medical-image performance does not show use of protein sequence/structure embeddings. Open-answer scorers differ between papers.

**Pathology image question answering:** Closed-question accuracy; open scoring is paper-specific (e.g. token recall in original LLaVA-Med). Official split; keep closed/open question groups separate.

Medical-image performance does not show use of protein sequence/structure embeddings. Open-answer scorers differ between papers.

**Medical image question answering:** Closed-question accuracy; open scoring is paper-specific (e.g. token recall in original LLaVA-Med). The 2019 challenge snapshot, not an arbitrary later VQA-Med release.

Medical-image performance does not show use of protein sequence/structure embeddings. Open-answer scorers differ between papers.

**Radiology image question answering — Runnable now:** An existing completed declared Qwen run demonstrates that the input interface, execution harness and scorer can be used in this environment. This is readiness of the documented qualified baseline, not a claim of strong performance or full paper replication. Actual image-grounded runs and the synthetic vision smoke test verify vision support; this is not an assumed text-only model.

Model compatibility: compatible

Evidence:

```json
[
  "reports/RESULTS_AT_A_GLANCE.json",
  "reports/local_model_capability_smoke.json"
]
```

**Medical image question answering in English — Runnable now:** An existing completed declared Qwen run demonstrates that the input interface, execution harness and scorer can be used in this environment. This is readiness of the documented qualified baseline, not a claim of strong performance or full paper replication. Actual image-grounded runs and the synthetic vision smoke test verify vision support; this is not an assumed text-only model.

Model compatibility: compatible

Evidence:

```json
[
  "reports/RESULTS_AT_A_GLANCE.json",
  "reports/local_model_capability_smoke.json"
]
```

**Pathology image question answering — Runnable now:** An existing completed declared Qwen run demonstrates that the input interface, execution harness and scorer can be used in this environment. This is readiness of the documented qualified baseline, not a claim of strong performance or full paper replication. Actual image-grounded runs and the synthetic vision smoke test verify vision support; this is not an assumed text-only model.

Model compatibility: compatible

Evidence:

```json
[
  "reports/RESULTS_AT_A_GLANCE.json",
  "reports/local_model_capability_smoke.json"
]
```

**Medical image question answering — Runnable now:** An existing completed declared Qwen run demonstrates that the input interface, execution harness and scorer can be used in this environment. This is readiness of the documented qualified baseline, not a claim of strong performance or full paper replication. Actual image-grounded runs and the synthetic vision smoke test verify vision support; this is not an assumed text-only model.

Model compatibility: compatible

Evidence:

```json
[
  "reports/RESULTS_AT_A_GLANCE.json",
  "reports/local_model_capability_smoke.json"
]
```

##### VQA-RAD

**Native/local protocol:** `NATIVE_TEST_QUESTION_IMAGE_LOCAL_ZERO_SHOT`

**Coverage:** full_native_test; completed_declared_run.

**Saved count record:**

```json
{
  "planned": 451,
  "completed": 451,
  "parsed": 451,
  "invalid_outputs": 0,
  "missing_or_failed_outputs": 0,
  "held_before_inference": 0
}
```

**Complete stored metrics, including alternate/diagnostic values:**

```json
{
  "open_token_recall": 0.5954043565269501,
  "closed_accuracy": 0.8676470588235294
}
```

**Comparison qualification:** Original native test split/images/questions and pinned LLaVA-Medv1 normalization/scoring; Qwen is a declared zero-shot vision baseline with its own chat template/generation and no downstream tuning. Compare OPEN recall and CLOSED accuracy separately; full-test claim requires complete native inputs and outputs.

**All stored published-reference records — separate from the local run:**

```json
[
  {
    "model": "LLaVA-Med 7B, CLIP, 60K-IM, stage1=1/stage2=3/FT=0",
    "metrics": {
      "open_token_recall_percent": 28.23,
      "closed_accuracy_percent": 61.4
    },
    "source_id": "LLAVA",
    "source_url": "https://arxiv.org/pdf/2306.00890",
    "source_locator": "Table 4(b), PDF p.9",
    "protocol": "zero-shot downstream transfer; original v1 release",
    "value_status": "published_rounded_as_printed",
    "run_count": null,
    "reported_std": null,
    "test_case_count": 451
  },
  {
    "model": "LLaVA-Med 7B, BioMedCLIP, 60K-IM, downstream FT=9",
    "metrics": {
      "open_token_recall_percent": 64.75,
      "closed_accuracy_percent": 83.09
    },
    "source_id": "LLAVA",
    "source_url": "https://arxiv.org/pdf/2306.00890",
    "source_locator": "Table 4(a,b), PDF p.9",
    "protocol": "supervised downstream tuning; original v1 release",
    "value_status": "published_rounded_as_printed",
    "run_count": null,
    "reported_std": null,
    "test_case_count": 451
  }
]
```

[Original score artifact](https://github.com/Some-random/bio-evaluation/blob/main/results/runs/qwen38_27b_v01_native_test_2026-10-15/scores.json)

##### SLAKE — English

**Native/local protocol:** `NATIVE_TEST_QUESTION_IMAGE_LOCAL_ZERO_SHOT`

**Coverage:** full_native_test; completed_declared_run.

**Saved count record:**

```json
{
  "planned": 1061,
  "completed": 1061,
  "parsed": 1060,
  "invalid_outputs": 1,
  "missing_or_failed_outputs": 0,
  "held_before_inference": 0
}
```

**Complete stored metrics, including alternate/diagnostic values:**

```json
{
  "open_token_recall": 0.5097973319647275,
  "closed_accuracy": 0.8461538461538461
}
```

**Comparison qualification:** Original native test split/images/questions and pinned LLaVA-Medv1 normalization/scoring; Qwen is a declared zero-shot vision baseline with its own chat template/generation and no downstream tuning. Compare OPEN recall and CLOSED accuracy separately; full-test claim requires complete native inputs and outputs.

**All stored published-reference records — separate from the local run:**

```json
[
  {
    "model": "LLaVA-Med 7B, CLIP, 60K-IM, stage1=1/stage2=3/FT=0",
    "metrics": {
      "open_token_recall_percent": 39.17,
      "closed_accuracy_percent": 52.16
    },
    "source_id": "LLAVA",
    "source_url": "https://arxiv.org/pdf/2306.00890",
    "source_locator": "Table 4(b), PDF p.9",
    "protocol": "zero-shot downstream transfer; original v1 release",
    "value_status": "published_rounded_as_printed",
    "run_count": null,
    "reported_std": null,
    "test_case_count": 1061
  },
  {
    "model": "LLaVA-Med 7B, BioMedCLIP, 60K-IM, downstream FT=9",
    "metrics": {
      "open_token_recall_percent": 87.11,
      "closed_accuracy_percent": 86.78
    },
    "source_id": "LLAVA",
    "source_url": "https://arxiv.org/pdf/2306.00890",
    "source_locator": "Table 4(a,b), PDF p.9",
    "protocol": "supervised downstream tuning; original v1 release",
    "value_status": "published_rounded_as_printed",
    "run_count": null,
    "reported_std": null,
    "test_case_count": 1061
  }
]
```

[Original score artifact](https://github.com/Some-random/bio-evaluation/blob/main/results/runs/qwen38_27b_v02_native_test_2026-10-15/scores.json)

##### PathVQA

**Native/local protocol:** `SOURCE_QUALIFIED_PATHVQA_HF_TEST_IMAGE_ZERO_SHOT`

**Coverage:** full_publisher_mirror_test; completed_declared_run.

**Saved count record:**

```json
{
  "planned": 6719,
  "completed": 6719,
  "parsed": 6718,
  "invalid_outputs": 1,
  "missing_or_failed_outputs": 0,
  "held_before_inference": 0
}
```

**Complete stored metrics, including alternate/diagnostic values:**

```json
{
  "open_token_recall": 0.2637701340133019,
  "closed_accuracy_corrected": 0.8587150505651397
}
```

**Comparison qualification:** Full pinned6719-row mirror test (original6761 minus42 duplicate rows, plus documented text normalization), full released image bytes and question strings. Original per-image byte identity is not fully established. Qwen zero-shot vision/training/generation differs from task-trained papers. Compare only declared metric and split-compatible results; no exact paper replication claim.

**All stored published-reference records — separate from the local run:**

```json
[
  {
    "model": "LLaVA-Med 7B, CLIP, 60K-IM, stage1=1/stage2=3/FT=0",
    "metrics": {
      "open_token_recall_percent": 12.3,
      "closed_accuracy_percent": 54.05
    },
    "source_id": "LLAVA",
    "source_url": "https://arxiv.org/pdf/2306.00890",
    "source_locator": "Table 4(b), PDF p.9",
    "protocol": "zero-shot downstream transfer; original v1 release",
    "value_status": "published_rounded_as_printed",
    "run_count": null,
    "reported_std": null,
    "test_case_count": 6761
  },
  {
    "model": "LLaVA-Med 7B, BioMedCLIP, 60K-IM, downstream FT=9",
    "metrics": {
      "open_token_recall_percent": 39.6,
      "closed_accuracy_percent": 91.09
    },
    "source_id": "LLAVA",
    "source_url": "https://arxiv.org/pdf/2306.00890",
    "source_locator": "Table 4(a,b), PDF p.9",
    "protocol": "supervised downstream tuning; original v1 release",
    "value_status": "published_rounded_as_printed",
    "run_count": null,
    "reported_std": null,
    "test_case_count": 6761
  }
]
```

[Original score artifact](https://github.com/Some-random/bio-evaluation/blob/main/results/runs/qwen38_27b_v03_full_publisher_mirror_2026-10-15_seven_gpu/scores.json)

##### ImageCLEF-VQA 2019

**Native/local protocol:** `NATIVE_IMAGECLEF2019_QUESTION_IMAGE_QUALIFIED_STRICT_ACCURACY`

**Coverage:** original_complete_test500; completed_declared_run.

**Saved count record:**

```json
{
  "planned": 500,
  "completed": 500,
  "parsed": 500,
  "invalid_outputs": 0,
  "missing_or_failed_outputs": null,
  "held_before_inference": 0
}
```

**Complete stored metrics, including alternate/diagnostic values:**

```json
{
  "strict_accuracy": 0.0
}
```

**Comparison qualification:** Same original500 test IDs/images/questions; zero-shot Qwen and explicit fixed scorer reconstruction, not target-fine-tuned MedVInT or a claim of byte-identical challenge scoring. Historical strict-accuracy executable not recovered; normalization/reference syntax reconstructed prospectively from organizers. Native2019BLEU withheld rather than substitute another year or arbitrary metric. No claim of matched target fine-tuning or closed/open metric equivalence.

Strict whole-final matching; qualified reconstructed scorer versus target-fine-tuned paper model. Zero exact match does not establish wrong clinical predictions or no visual ability.

Prediction-only audit: 500 multiline finals, 15–263 words (median 70); verbose answer format is material.

**All stored published-reference records — separate from the local run:**

```json
[
  {
    "model": "MedVInT-TE",
    "metrics": {
      "overall_accuracy_percent": 70.5
    },
    "source_id": "PMC",
    "source_url": "https://arxiv.org/html/2305.10415v6",
    "source_locator": "Table 2",
    "protocol": "fine-tuned on target ImageCLEF-VQA2019; free-text answering",
    "value_status": "published_rounded_as_printed",
    "run_count": null,
    "reported_std": null,
    "reported_interval": {
      "overall_accuracy_percent": [
        62.8,
        78.2
      ]
    },
    "uncertainty_note": "Parenthesized range preserved; interval coverage and sampling procedure not independently re-established here."
  }
]
```

[Original score artifact](https://github.com/Some-random/bio-evaluation/blob/main/results/runs/qwen38_27b_v04_original_test500_2026-10-15/scores.json)

[Source 1](https://arxiv.org/abs/2306.00890), [Source 2](https://arxiv.org/html/2305.10415v6), [Source 3](https://arxiv.org/abs/2306.00890), [Source 4](https://arxiv.org/html/2305.10415v6), [Source 5](https://github.com/microsoft/LLaVA-Med), [Source 6](https://github.com/xiaoman-zhang/PMC-VQA)

#### Scientific figures, documents and visual conversations

#### PMC-VQA figure question answering

Specify initial versus cleaned test set. Caption-derived labels need not be visually answerable without filtering.

Published source size/units: Reviewed v6: 50,000 initial test examples; 2,000 manually reviewed clean test examples.

**Scientific figure question answering:** MCQ accuracy; paper's open/blank-answer accuracy and BLEU. v6: 50,000 initial image-disjoint test examples; 2,000 manually reviewed clean test examples. Older site names differ.

Specify initial versus cleaned test set. Caption-derived labels need not be visually answerable without filtering.

**Scientific figure question answering — Runnable now:** An existing completed declared Qwen run demonstrates that the input interface, execution harness and scorer can be used in this environment. This is readiness of the documented qualified baseline, not a claim of strong performance or full paper replication. Actual image-grounded runs and the synthetic vision smoke test verify vision support; this is not an assumed text-only model.

Model compatibility: compatible

Evidence:

```json
[
  "reports/RESULTS_AT_A_GLANCE.json",
  "reports/local_model_capability_smoke.json"
]
```

##### PMC-VQA held-out evaluation

**Native/local protocol:** `NATIVE_PMCVQA_CLEAN2000_TD_PROMPT_QWEN_ZERO_SHOT`

**Coverage:** full_native_clean2000; completed_declared_run.

**Saved count record:**

```json
{
  "planned": 2000,
  "completed": 2000,
  "parsed": 1990,
  "invalid_outputs": 10,
  "missing_or_failed_outputs": 0,
  "held_before_inference": null
}
```

**Complete stored metrics, including alternate/diagnostic values:**

```json
{
  "native_td_final_character_accuracy": 0.02,
  "adapted_full_text_closest_choice_accuracy": 0.4975,
  "adapted_full_text_released_label_accuracy": 0.4975,
  "strict_final_label_accuracy": 0.007
}
```

**Comparison qualification:** Fixed local zero-shot Qwen vision baseline on complete native clean2000 set and source TD question/choice strings. Qwen chat, image preprocessing, free generation and training differ from MedVInT. Match metric/output extraction and clean split before comparing; full-text metric is adapted, TE systems are not exact reproductions. Public pretraining exposure unknown.

**All stored published-reference records — separate from the local run:**

```json
[
  {
    "model": "MedVInT-TD / PMC-LLaMA / PMC-CLIP",
    "metrics": {
      "choice_accuracy_percent": 40.3,
      "blank_accuracy_percent": 33.6,
      "blank_bleu1_percent": 21.5
    },
    "source_id": "PMC",
    "source_url": "https://arxiv.org/html/2305.10415v6",
    "source_locator": "Table 3",
    "protocol": "clean PMC-VQA-test (2,000), trained on PMC-VQA",
    "value_status": "published_rounded_as_printed",
    "run_count": null,
    "reported_std": null,
    "test_case_count": 2000,
    "reported_interval": {
      "choice_accuracy_percent": [
        37.2,
        43.8
      ],
      "blank_accuracy_percent": [
        29.9,
        36.5
      ],
      "blank_bleu1_percent": [
        19.4,
        24.0
      ]
    },
    "uncertainty_note": "Parenthesized intervals preserved; coverage definition not independently re-established."
  }
]
```

[Original score artifact](https://github.com/Some-random/bio-evaluation/blob/main/results/runs/qwen38_27b_v05_pmcvqa_clean2000_td_2026-10-15/scores.json)

[Source 1](https://arxiv.org/html/2305.10415v6), [Source 2](https://github.com/xiaoman-zhang/PMC-VQA)

#### LLaVA-Med biomedical visual conversations

Teacher reference has textual context that the image may not reveal. Judgment is not direct clinician-verified molecular truth.

Published source size/units: Published 50-image conversation-evaluation setting; teacher-generated text references.

**Biomedical visual conversations:** GPT-assisted relative response assessment. Released qa50 evaluation files; 50-image setting. Use original/v1.5 code and model version consistently.

Teacher reference has textual context that the image may not reveal. Judgment is not direct clinician-verified molecular truth.

**Biomedical visual conversations — Needs scoring protocol:** Qwen can accept the native image/question inputs. The official QA50 release and reference mapping are now verified: 193 questions for 50 images, with the native GPT-4-0314 judging contract recovered. Nineteen exact original images are available, covering 73 questions. All legacy archive URLs return 404; the remaining 31 PMC pages returned a browser/reCAPTCHA challenge. The external-provider hold still prevents native GPT judging; a substitute judge would change the metric.

Model compatibility: compatible

Evidence:

```json
[
  "reports/catalog_execution_review_2026-10-15.json",
  "reports/local_model_capability_smoke.json",
  "reports/SOURCE_PREPARATION_2026-10-16.json",
  "handoff/source_preparation_2026-10-16/README.md"
]
```

Published reference record: GPT-assisted relative answer-quality comparisons are reported. A verified single aggregate for the specified qa50 setting is not transcribed here.

[Source 1](https://arxiv.org/abs/2306.00890), [Source 2](https://github.com/microsoft/LLaVA-Med)

#### Ryze document-extraction component tests

Component ablation These tests evaluate extraction/document understanding, not protein engineering.

Published source size/units: Does document/figure extraction preserve information needed for answering questions? Auxiliary component evaluation, separate from final LAB-Bench scores.

**Scientific document and figure extraction:** Dataset-specific QA accuracy. Auxiliary component evaluation, separate from final LAB-Bench scores.

These tests evaluate extraction/document understanding, not protein engineering.

**Scientific document and figure extraction — Needs data or protocol:** Qwen can process images, but the rechecked publisher commit is unchanged and still provides no recovered exact ArXivQA/SlideVQA/ChartQA component manifest, full media/page mapping, extraction condition, downstream answer-model/prompt or native scoring/aggregation contract. Five implementation files were restored with publisher hash verification. Generic synthetic fallback rows are not benchmark data, and direct Qwen image QA would be a different setting.

Model compatibility: compatible

Evidence:

```json
[
  "reports/remaining_native_source_recovery_2026-10-15.json",
  "reports/local_model_capability_smoke.json",
  "reports/SOURCE_PREPARATION_2026-10-16.json",
  "handoff/source_preparation_2026-10-16/README.md"
]
```

Published reference record: Ryze extraction-component accuracy: ArXivQA 73.12%, SlideVQA 66.48%, ChartQA 75.8%.

[Source 1](https://arxiv.org/html/2606.00902v1)

## Other biological modalities and molecular interactions

#### Molecular interactions and binding affinity

#### Drug–target interaction: BioSNAP / Human / BindingDB

Secondary to the protein focus. Not protein–protein recognition or Affibody–pMHC evaluation.

Published source size/units: Three source benchmarks; preserve each split/negative/threshold rule.

**Drug–target interaction:** AUROC in BioT5+ comparisons. Three source benchmarks; preserve each split/negative/threshold rule.

Secondary to the protein focus. Not protein–protein recognition or Affibody–pMHC evaluation.

**Drug–target interaction — Runnable now:** An existing completed declared Qwen run demonstrates that the input interface, execution harness and scorer can be used in this environment. This is readiness of the documented qualified baseline, not a claim of strong performance or full paper replication.

Model compatibility: compatible

Evidence:

```json
[
  "reports/RESULTS_AT_A_GLANCE.json"
]
```

##### Drug–target interaction — BioSNAP/Human/BindingDB · bindingdb

**Native/local protocol:** `QWEN_DTI_FIRST_TOKEN_CONDITIONAL_YES_NO_LIKELIHOOD`

**Coverage:** full_frozen_reviewed_dataset; dataset_component.

**Saved count record:**

```json
{
  "planned": 9840,
  "completed": 9840,
  "parsed": 9840,
  "invalid_outputs": 0,
  "missing_or_failed_outputs": 0,
  "held_before_inference": 0
}
```

**Complete stored metrics, including alternate/diagnostic values:**

```json
{
  "auroc": 0.5035692021569061,
  "auprc": 0.41031521273083055
}
```

**Comparison qualification:** Original released dataset and standard AUROC/AP; fixed first-token Qwen likelihood adapter differs from trained DrugBAN/BioT5 architectures and BioT5 raw-score ratio. No test threshold fitting or exact paper reproduction claim.

AUROC/AP are separate dataset fractions, not pooled. One-token conditional Yes/No likelihood; length finish is expected here.

**All stored published-reference records — separate from the local run:**

```json
[
  {
    "model": "BioT5+",
    "metrics": {
      "biosnap_auroc": 0.939,
      "human_auroc": 0.987,
      "bindingdb_auroc": 0.964
    },
    "source_id": "BIOT5",
    "source_url": "https://arxiv.org/html/2402.17810v2",
    "source_locator": "Table 8",
    "protocol": "supervised DTI; source-specific paired drug SELFIES and protein sequences",
    "value_status": "published_rounded_as_printed",
    "run_count": null,
    "reported_std": {
      "biosnap_auroc": 0.001,
      "human_auroc": 0.001,
      "bindingdb_auroc": 0.001
    }
  }
]
```

[Original score artifact](https://github.com/Some-random/bio-evaluation/blob/main/results/runs/qwen38_27b_dti_bindingdb_likelihood_2026-10-15/scores.json)

##### Drug–target interaction — BioSNAP/Human/BindingDB · biosnap

**Native/local protocol:** `QWEN_DTI_FIRST_TOKEN_CONDITIONAL_YES_NO_LIKELIHOOD`

**Coverage:** full_frozen_reviewed_dataset; dataset_component.

**Saved count record:**

```json
{
  "planned": 5493,
  "completed": 5493,
  "parsed": 5493,
  "invalid_outputs": 0,
  "missing_or_failed_outputs": 0,
  "held_before_inference": 0
}
```

**Complete stored metrics, including alternate/diagnostic values:**

```json
{
  "auroc": 0.5335627434292335,
  "auprc": 0.5216604334511094
}
```

**Comparison qualification:** Original released dataset and standard AUROC/AP; fixed first-token Qwen likelihood adapter differs from trained DrugBAN/BioT5 architectures and BioT5 raw-score ratio. No test threshold fitting or exact paper reproduction claim.

AUROC/AP are separate dataset fractions, not pooled. One-token conditional Yes/No likelihood; length finish is expected here.

**All stored published-reference records — separate from the local run:**

```json
[
  {
    "model": "BioT5+",
    "metrics": {
      "biosnap_auroc": 0.939,
      "human_auroc": 0.987,
      "bindingdb_auroc": 0.964
    },
    "source_id": "BIOT5",
    "source_url": "https://arxiv.org/html/2402.17810v2",
    "source_locator": "Table 8",
    "protocol": "supervised DTI; source-specific paired drug SELFIES and protein sequences",
    "value_status": "published_rounded_as_printed",
    "run_count": null,
    "reported_std": {
      "biosnap_auroc": 0.001,
      "human_auroc": 0.001,
      "bindingdb_auroc": 0.001
    }
  }
]
```

[Original score artifact](https://github.com/Some-random/bio-evaluation/blob/main/results/runs/qwen38_27b_dti_biosnap_likelihood_2026-10-15/scores.json)

##### Drug–target interaction — BioSNAP/Human/BindingDB · human

**Native/local protocol:** `QWEN_DTI_FIRST_TOKEN_CONDITIONAL_YES_NO_LIKELIHOOD`

**Coverage:** full_frozen_reviewed_dataset; dataset_component.

**Saved count record:**

```json
{
  "planned": 1200,
  "completed": 1200,
  "parsed": 1200,
  "invalid_outputs": 0,
  "missing_or_failed_outputs": 0,
  "held_before_inference": 0
}
```

**Complete stored metrics, including alternate/diagnostic values:**

```json
{
  "auroc": 0.4747193063297968,
  "auprc": 0.4194264625175069
}
```

**Comparison qualification:** Original released dataset and standard AUROC/AP; fixed first-token Qwen likelihood adapter differs from trained DrugBAN/BioT5 architectures and BioT5 raw-score ratio. No test threshold fitting or exact paper reproduction claim.

AUROC/AP are separate dataset fractions, not pooled. One-token conditional Yes/No likelihood; length finish is expected here.

**All stored published-reference records — separate from the local run:**

```json
[
  {
    "model": "BioT5+",
    "metrics": {
      "biosnap_auroc": 0.939,
      "human_auroc": 0.987,
      "bindingdb_auroc": 0.964
    },
    "source_id": "BIOT5",
    "source_url": "https://arxiv.org/html/2402.17810v2",
    "source_locator": "Table 8",
    "protocol": "supervised DTI; source-specific paired drug SELFIES and protein sequences",
    "value_status": "published_rounded_as_printed",
    "run_count": null,
    "reported_std": {
      "biosnap_auroc": 0.001,
      "human_auroc": 0.001,
      "bindingdb_auroc": 0.001
    }
  }
]
```

[Original score artifact](https://github.com/Some-random/bio-evaluation/blob/main/results/runs/qwen38_27b_dti_human_likelihood_2026-10-15/scores.json)

[Source 1](https://arxiv.org/html/2402.17810v2), [Source 2](https://github.com/QizhiPei/BioT5)

#### ATOM3D protein–ligand affinity (LBA)

Target transformation and split must match. Not antibody–antigen affinity.

Published source size/units: 30%-identity split: train 3,507, validation 466, test 490 complexes. The 60% split is a different protocol.

**Protein–ligand binding affinity — Needs additional models/tools:** The native input is protein-ligand atomic coordinates and the target is transformed assay affinity. No validated geometry adapter or structural affinity model is prepared; sequence/SMILES prompting would omit native information and require a separate adaptation.

Model compatibility: needs specialist pipeline

Evidence:

```json
[
  "reports/TASK_HIERARCHY_DATA.json",
  "handoff/Bio_Evaluation_Agent_Package_2026-10-16/EVALUATION_INVENTORY.csv",
  "reports/local_model_capability_smoke.json"
]
```

Published reference record: 3D-CNN: RMSE 1.416, Spearman 0.553; GNN: RMSE 1.570, Spearman 0.628.

[Source 1](https://arxiv.org/html/2012.04035v3), [Source 2](https://www.atom3d.ai/)

#### ATOM3D ligand efficacy (LEP)

Activity/efficacy is distinct from affinity. Source molecule count is not a test denominator.

Published source size/units: 527 source small molecules; final retained train/test counts not transcribed.

**Ligand efficacy — Needs additional models/tools:** Native efficacy classification uses receptor/ligand conformations. Current Qwen has no validated molecular-geometry adapter; a structural model/tool or a separately validated representation is needed before preserving this native task.

Model compatibility: needs specialist pipeline

Evidence:

```json
[
  "reports/TASK_HIERARCHY_DATA.json",
  "handoff/Bio_Evaluation_Agent_Package_2026-10-16/EVALUATION_INVENTORY.csv",
  "reports/local_model_capability_smoke.json"
]
```

Published reference record: AUROC: GNN 0.740; 3D-CNN 0.589.

[Source 1](https://arxiv.org/html/2012.04035v3), [Source 2](https://www.atom3d.ai/lep.html)

#### PFMBench PDBbind / BindingDB affinity panel

These are PFMBench-specific processed datasets/splits, not interchangeable with PEER/ProtST results. F1 is not Fmax. Affinity-named AUROC tasks are classification, not KD regression. Exact loaders required.

Published source size/units: Test sizes: PDBBind: 1,836; BindingDB: 1,139

**Protein–ligand binding affinity — Needs data or protocol:** Protein/ligand inputs can support a disclosed Qwen numeric adaptation once the exact PFMBench representation is recovered. PDBbind/BindingDB splits, partner encodings, target transformations and Spearman contracts are not prepared; the existing DrugBAN classification protocol is distinct.

Model compatibility: compatible

Evidence:

```json
[
  "reports/TASK_HIERARCHY_DATA.json",
  "handoff/Bio_Evaluation_Agent_Package_2026-10-16/EVALUATION_INVENTORY.csv",
  "reports/local_model_capability_smoke.json"
]
```

Published reference record: ESM2-Adapter, Table 1 means: PDBBind Spearman 0.1677; BindingDB Spearman 0.1922

[Source 1](https://arxiv.org/html/2506.14796v1), [Source 2](https://github.com/biomap-research/PFMBench)

#### Pathway and disease prediction

#### BioReason KEGG pathway/disease

Correct final disease labels do not verify every generated mechanistic statement.

Published source size/units: 290 test entries in main table; 1,449 overall entries across splits.

**Pathway and disease prediction:** Accuracy; macro-F1/precision/recall. 290 test entries in main table; 1,449 overall entries across splits.

Correct final disease labels do not verify every generated mechanistic statement.

**Pathway and disease prediction — Runnable now:** An existing completed declared Qwen run demonstrates that the input interface, execution harness and scorer can be used in this environment. This is readiness of the documented qualified baseline, not a claim of strong performance or full paper replication.

Model compatibility: compatible

Evidence:

```json
[
  "reports/RESULTS_AT_A_GLANCE.json"
]
```

##### BioReason KEGG pathway/disease test

**Native/local protocol:** `NATIVE_LLM_INTERFACE_FULL_RELEASE_WINDOWS_PREPARED`

**Coverage:** official_released_test_then_val_290; completed_declared_run.

**Saved count record:**

```json
{
  "planned": 290,
  "completed": 290,
  "parsed": 0,
  "invalid_outputs": 290,
  "missing_or_failed_outputs": 0,
  "held_before_inference": 0
}
```

**Complete stored metrics, including alternate/diagnostic values:**

```json
{
  "accuracy": 0.0,
  "STRICT_FINAL_LABEL": {
    "accuracy": 0.0,
    "supplemental_macro_f1_fixed_global_vocabulary": 0.0,
    "supplemental_macro_precision_fixed_global_vocabulary": 0.0,
    "supplemental_macro_recall_fixed_global_vocabulary": 0.0
  }
}
```

**Comparison qualification:** Source outcome predicates retained with explicit decoded-continuation qualification. Full released DNA windows, zero-shot prompted local Qwen, source SFT/encoder systems and author decoder settings differ. N01 macro metrics are supplemental strict-label diagnostics, not verified native paper reproduction.

**All stored published-reference records — separate from the local run:**

```json
[
  {
    "model": "Qwen3-4B",
    "metrics": {
      "accuracy_percent": 90.0,
      "macro_f1_percent": 79.66,
      "macro_precision_percent": 88.24,
      "macro_recall_percent": 75.08
    },
    "source_id": "BIOREASON",
    "source_url": "https://arxiv.org/html/2505.23579v2",
    "source_locator": "Table 1",
    "protocol": "LLM-only task baseline, 290 KEGG test examples",
    "value_status": "published_rounded_as_printed",
    "run_count": null,
    "reported_std": null,
    "test_case_count": 290
  },
  {
    "model": "Evo2 + Qwen3-4B + GRPO",
    "metrics": {
      "accuracy_percent": 98.28,
      "macro_f1_percent": 93.05,
      "macro_precision_percent": 94.12,
      "macro_recall_percent": 92.48
    },
    "source_id": "BIOREASON",
    "source_url": "https://arxiv.org/html/2505.23579v2",
    "source_locator": "Table 1",
    "protocol": "trained DNA-LLM hybrid, 290 KEGG test examples",
    "value_status": "published_rounded_as_printed",
    "run_count": null,
    "reported_std": null,
    "test_case_count": 290
  }
]
```

[Original score artifact](https://github.com/Some-random/bio-evaluation/blob/main/results/runs/qwen38_27b_n01_full_windows_2026-10-15/scores.json)

[Source 1](https://arxiv.org/html/2505.23579v2), [Source 2](https://huggingface.co/datasets/wanglab/kegg)

#### Bio-posttrain KEGG unseen-network holdout

Pin the adapted split and preprocessing.

Published source size/units: Adapted KEGG split by pathway networks; not automatically BioReason's original 290-example test.

**Network-held-out pathway prediction:** Accuracy. Adapted KEGG split by pathway networks; not automatically BioReason's original 290-example test.

Pin the adapted split and preprocessing.

Exact network-held-out CSVs/IDs unavailable; author genomics link redirects to sign-in. Original N01 is not a substitute.

**Network-held-out pathway prediction — Needs data or protocol:** A qualified DNA-text Qwen adaptation is plausible from the documented native inputs, but the author link yields a sign-in page rather than the required network-held-out train/ID/OOD CSVs. N01 or a guessed random/network split cannot substitute for this test.

Model compatibility: compatible

Evidence:

```json
[
  "reports/posttrain_native_gap_audit.json"
]
```

Published reference record: Qwen3-4B DNA OOD accuracy: SFT 0.753; SFT+RL 0.917; biology-CPT+SFT+RL 0.970.

[Source 1](https://arxiv.org/html/2606.16517v1), [Source 2](https://github.com/mims-harvard/bio-posttrain)

#### Variant-effect prediction

#### BioReason VEP coding and non-SNV

Genomics task, not Affibody binding; annotation confidence and splitting matter. | Non-SNV classification should not be merged with single-amino-acid design accuracy.

Published source size/units: Coding: approximately 1.23K reported test cases; non-SNV: 873. Distinct datasets.

**Coding-variant effect prediction:** Accuracy; F1. Main reported test approximately 1.23K; chromosome 8 held out.

Genomics task, not Affibody binding; annotation confidence and splitting matter.

**Non-SNV variant effect prediction:** Accuracy; F1. 873 test examples in the main report.

Non-SNV classification should not be merged with single-amino-acid design accuracy.

**Coding-variant effect prediction — Runnable now:** An existing completed declared Qwen run demonstrates that the input interface, execution harness and scorer can be used in this environment. This is readiness of the documented qualified baseline, not a claim of strong performance or full paper replication.

Model compatibility: compatible

Evidence:

```json
[
  "reports/RESULTS_AT_A_GLANCE.json"
]
```

**Non-SNV variant effect prediction — Runnable now:** An existing completed declared Qwen run demonstrates that the input interface, execution harness and scorer can be used in this environment. This is readiness of the documented qualified baseline, not a claim of strong performance or full paper replication.

Model compatibility: compatible

Evidence:

```json
[
  "reports/RESULTS_AT_A_GLANCE.json"
]
```

##### BioReason VEP-Coding

**Native/local protocol:** `NATIVE_LLM_INTERFACE_FULL_RELEASE_WINDOWS_PREPARED`

**Coverage:** official_released_test; completed_declared_run.

**Saved count record:**

```json
{
  "planned": 1233,
  "completed": 1233,
  "parsed": 0,
  "invalid_outputs": 1233,
  "missing_or_failed_outputs": 0,
  "held_before_inference": 0
}
```

**Complete stored metrics, including alternate/diagnostic values:**

```json
{
  "accuracy": 0.4906731549067315,
  "f1": 0.5213414634146342,
  "STRICT_FINAL_LABEL": {
    "accuracy": 0.0,
    "f1": 0.0
  }
}
```

**Comparison qualification:** Source outcome predicates retained with explicit decoded-continuation qualification. Full released DNA windows, zero-shot prompted local Qwen, source SFT/encoder systems and author decoder settings differ. N01 macro metrics are supplemental strict-label diagnostics, not verified native paper reproduction.

**All stored published-reference records — separate from the local run:**

```json
[
  {
    "model": "Qwen3-4B",
    "metrics": {
      "accuracy_percent": 48.99,
      "f1_percent": 39.58
    },
    "source_id": "BIOREASON",
    "source_url": "https://arxiv.org/html/2505.23579v2",
    "source_locator": "Table 2",
    "protocol": "native variant-effect binary test; deterministic T=0",
    "value_status": "published_rounded_as_printed",
    "run_count": null,
    "reported_std": null,
    "test_case_count": null,
    "test_size_note": "Paper rounds VEP-Coding test size to 1.23K; exact count not inferred."
  },
  {
    "model": "Evo2 + Qwen3-4B",
    "metrics": {
      "accuracy_percent": 80.21,
      "f1_percent": 80.0
    },
    "source_id": "BIOREASON",
    "source_url": "https://arxiv.org/html/2505.23579v2",
    "source_locator": "Table 2",
    "protocol": "native variant-effect binary test; deterministic T=0",
    "value_status": "published_rounded_as_printed",
    "run_count": null,
    "reported_std": null,
    "test_case_count": null,
    "test_size_note": "Paper rounds VEP-Coding test size to 1.23K; exact count not inferred."
  }
]
```

[Original score artifact](https://github.com/Some-random/bio-evaluation/blob/main/results/runs/qwen38_27b_n02_full_windows_2026-10-15/scores.json)

##### BioReason VEP-Non-SNV

**Native/local protocol:** `NATIVE_LLM_INTERFACE_FULL_RELEASE_WINDOWS_PREPARED`

**Coverage:** official_released_test; completed_declared_run.

**Saved count record:**

```json
{
  "planned": 873,
  "completed": 873,
  "parsed": 0,
  "invalid_outputs": 873,
  "missing_or_failed_outputs": 0,
  "held_before_inference": 0
}
```

**Complete stored metrics, including alternate/diagnostic values:**

```json
{
  "accuracy": 0.8900343642611683,
  "f1": 0.9053254437869822,
  "STRICT_FINAL_LABEL": {
    "accuracy": 0.0,
    "f1": 0.0
  }
}
```

**Comparison qualification:** Source outcome predicates retained with explicit decoded-continuation qualification. Full released DNA windows, zero-shot prompted local Qwen, source SFT/encoder systems and author decoder settings differ. N01 macro metrics are supplemental strict-label diagnostics, not verified native paper reproduction.

**All stored published-reference records — separate from the local run:**

```json
[
  {
    "model": "Qwen3-4B",
    "metrics": {
      "accuracy_percent": 61.86,
      "f1_percent": 67.6
    },
    "source_id": "BIOREASON",
    "source_url": "https://arxiv.org/html/2505.23579v2",
    "source_locator": "Table 2",
    "protocol": "native variant-effect binary test; deterministic T=0",
    "value_status": "published_rounded_as_printed",
    "run_count": null,
    "reported_std": null,
    "test_case_count": 873,
    "test_size_note": null
  },
  {
    "model": "Evo2 + Qwen3-4B",
    "metrics": {
      "accuracy_percent": 83.85,
      "f1_percent": 85.02
    },
    "source_id": "BIOREASON",
    "source_url": "https://arxiv.org/html/2505.23579v2",
    "source_locator": "Table 2",
    "protocol": "native variant-effect binary test; deterministic T=0",
    "value_status": "published_rounded_as_printed",
    "run_count": null,
    "reported_std": null,
    "test_case_count": 873,
    "test_size_note": null
  }
]
```

[Original score artifact](https://github.com/Some-random/bio-evaluation/blob/main/results/runs/qwen38_27b_n03_full_windows_2026-10-15/scores.json)

[Source 1](https://arxiv.org/html/2505.23579v2), [Source 2](https://github.com/bowang-lab/BioReason)

#### Expression-conditioned gene selection

#### Bio-posttrain MEDEA expression-conditioned gene selection

Fixed-input target nomination is not the original full agent workflow or clinical validation.

Published source size/units: Held-out disease: hepatoblastoma; additional cell-type analyses reported.

**Expression-conditioned gene selection:** Normalized gene-answer accuracy. Held-out disease: hepatoblastoma; additional cell-type analyses reported.

Fixed-input target nomination is not the original full agent workflow or clinical validation.

Exact adapted hepatoblastoma split/vector alignment/RNA evaluator missing; upstream MEDEA questions or gene lists do not replace required expression inputs.

**Expression-conditioned gene selection — Needs additional models/tools:** The native input includes aligned disease/normal TranscriptFormer vectors for all five candidate genes and a trained projection, not a gene-name-only text prompt. Exact adapted test IDs, vector alignment, native preprocessing/scorer and projection assets are not released in the inspected code.

Model compatibility: needs specialist pipeline

Evidence:

```json
[
  "reports/posttrain_native_gap_audit.json"
]
```

Published reference record: The paper reports RNA target-selection ID/OOD experiments. An exact numeric result is not transcribed in this table.

[Source 1](https://arxiv.org/html/2606.16517v1), [Source 2](https://github.com/mims-harvard/bio-posttrain)

#### RNA structure ranking

#### ATOM3D RNA structure ranking (RSR)

RNA task retained as adjacent scope, not a protein benchmark.

Published source size/units: RNA-Puzzles 1–21; test puzzles 18–21, with decoys per target. Exact retained test-decoy count not re-counted.

**RNA structure ranking — Needs additional models/tools:** Native ranking operates on RNA decoy coordinates. A validated coordinate-to-quality adapter or RNA structural scoring model is missing; Qwen language answers alone do not implement the native geometry-based ranking protocol.

Model compatibility: needs specialist pipeline

Evidence:

```json
[
  "reports/TASK_HIERARCHY_DATA.json",
  "handoff/Bio_Evaluation_Agent_Package_2026-10-16/EVALUATION_INVENTORY.csv",
  "reports/local_model_capability_smoke.json"
]
```

Published reference record: Mean per-target Spearman: 3D-CNN 0.264; GNN 0.234.

[Source 1](https://arxiv.org/html/2012.04035v3), [Source 2](https://www.atom3d.ai/rsr.html)

#### Small-molecule properties

#### ATOM3D small-molecule properties (SMP / QM9)

Adjacency only; not protein biology. Units depend on property.

Published source size/units: Processed test 12,943 molecules (train 103,547; validation 12,943).

**Small-molecule properties — Needs additional models/tools:** Native QM9 property prediction uses molecular atom coordinates with property-specific units. No validated atomic-geometry adapter or molecular property model is prepared; converting to a different text representation would be a newly defined adaptation.

Model compatibility: needs specialist pipeline

Evidence:

```json
[
  "reports/TASK_HIERARCHY_DATA.json",
  "handoff/Bio_Evaluation_Agent_Package_2026-10-16/EVALUATION_INVENTORY.csv",
  "reports/local_model_capability_smoke.json"
]
```

Published reference record: ENN dipole MAE 0.052 D; 3D-CNN 0.754 D. Property-specific scores must remain separate.

[Source 1](https://arxiv.org/html/2012.04035v3), [Source 2](https://www.atom3d.ai/)

</details>

[Raw run artifacts and uploaded trajectories](https://github.com/Some-random/bio-evaluation/tree/main/results/runs)
