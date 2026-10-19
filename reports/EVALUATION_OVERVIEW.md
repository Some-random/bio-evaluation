# Biological evaluation overview

General-purpose baseline: **Qwen3.8-27B**, with text and image inputs.

This catalog spans biological prediction, scientific evidence, protein design and three-dimensional structure. The map below shows **31 task families in 8 categories** without opening the detailed catalog. The counts are task families, not datasets or individual test questions.

BioReason, BioReason-Pro and Bio-posttrain settings are set aside from this main comparison. [Archived settings and original records](ARCHIVED_EVALUATIONS.md) remain available.

## Task map

| Category | Number of task families | Tasks | Typical question or output |
|---|---:|---|---|
| Protein traits and interactions | 5 | Whether proteins dissolve; Where proteins go in a cell; Protein activity, stability and production; Which proteins bind each other; Antibody properties | Will this protein dissolve? Where does it go? What does it bind? |
| What proteins do | 5 | Assigning protein functions and enzyme classes; Protein function descriptions; Biochemical reaction classification; Protein retrieval from descriptions; Evidence support for protein explanations | What is this protein's function? Which reaction does it carry out? |
| Effects of protein mutations | 4 | Explaining mutation effects; Predicting and ranking mutation effects; Choosing mutations to improve a protein; Binding affinity and immune interactions | What happens after changing a protein? Which change works best? |
| Answering biology research questions | 1 | Biological research question answering | Answer a question using papers, figures, tables, protocols or sequences |
| Designing proteins | 6 | Antibody design; Finding a sequence for a desired shape; Protein sequence and structure generation; Building around a functional protein part; Designing proteins that bind a target; Making fluorescent proteins brighter | Propose a protein sequence or shape that meets specified requirements |
| Protein shapes and motion | 5 | Local structure and residue prediction; Protein structure ranking; Protein folding; Protein shape changes, motion and stability; Structure-derived questions and output checks | What shape does this protein take? How does it move or stay folded? |
| Understanding biomedical images | 2 | Biomedical visual question answering; Scientific figures, documents and visual conversations | Answer questions about medical images and scientific figures |
| DNA, RNA and small molecules | 3 | Molecular interactions and binding affinity; RNA structure ranking; Small-molecule properties | Predict molecular binding, RNA structure and chemical properties |
| **Total** | **31** | | |

## Worked examples

### Good result: Predict how an immune-receptor deletion affects neuronal connections

**Evaluation dataset:** [LAB-Bench LitQA2](https://huggingface.co/datasets/futurehouse/lab-bench/tree/5c77cec648430f30611808808861eb86f81d5eaa).

**Question:** In 5XFAD mice, an Alzheimer’s disease model, what happens to post-synaptic terminals when Ifnar1 is deleted specifically in microglia?

Microglia are the brain’s immune cells. IFNAR1 receives type-I interferon signals; post-synaptic terminals are the receiving ends of connections between neurons.

**Answer choices:** (A) increased synaptophysin+ density; (B) increased loss; (C) no effect; (D) attenuation of loss; (E) Insufficient information to answer the question.

**Qwen's answer:** (D)

**Saved model reasoning (verbatim, 281 words):**

> The question asks about the effect of microglia-specific Ifnar1 deletion on post-synaptic terminals in 5XFAD mice.
>
> 5XFAD mice are a well-known transgenic mouse model of Alzheimer's disease that carry five mutations associated with familial Alzheimer's disease.
>
> Ifnar1 encodes the interferon-alpha/beta receptor. In the context of neuroinflammation and Alzheimer's disease, type I interferon signaling plays a role in the inflammatory response.
>
> Microglia are the resident immune cells of the brain, and their activation in Alzheimer's disease can contribute to synaptic loss.
>
> In research on 5XFAD mice, studies have examined the role of interferon signaling in microglia and its effect on synaptopathy. The key study I'm thinking of is one that showed that in 5XFAD mice, there is a loss of synapses (both pre- and post-synaptic), and that this is mediated by interferon signaling in microglia.
>
> Specifically, research has shown that:
> - In 5XFAD mice, there is progressive synaptic loss
> - Microglia contribute to this synaptic loss through interferon signaling
> - Ifnar1 (type I interferon receptor) deletion in microglia attenuates the synaptic loss
>
> Looking at the options:
> (A) increased synaptophysin+ density - synaptophysin is a pre-synaptic marker
> (B) increased loss - this would mean the deletion worsens the problem
> (C) no effect
> (D) attenuation of loss - this would mean the deletion reduces/prevents the synaptic loss
> (E) Insufficient information
>
> The study by Dera et al. (2020) in Nature Neuroscience showed that type I interferon signaling in microglia drives synapse loss in Alzheimer's disease models. They found that microglia-specific Ifnar1 deletion attenuated the loss of synapses in 5XFAD mice.
>
> For post-synaptic terminals specifically (marked by PSD95), the Ifnar1 deletion in microglia would attenuate the loss.
>
> So the answer should be (D) attenuation of loss.

**Reference study:** [Roy et al., 2022, Immunity](https://pmc.ncbi.nlm.nih.gov/articles/PMC9109419/).

The answer matches the reference label. Dataset accuracy: **39.1%** (77/197).

### Bad result (illustrative): a protein-stability answer without the required computation

The failure illustrated here is reporting an unsupported stability number without carrying out the structural sampling and energy calculations in this BioEmu evaluation protocol.

**Category:** [Protein shapes and motion](#protein-shapes-and-motion) → Protein shape changes, motion and stability.

**Evaluation dataset:** [BioEmu folding-free-energy benchmark](https://github.com/microsoft/bioemu-benchmarks/blob/63edbfa2ee5f489d66a4bece96f242a1d28e567d/bioemu_benchmarks/assets/folding_free_energies_benchmark_0.1/folding_free_energies/system_info.csv) — protein stability.

**Question:** Given the protein below, replace amino acid 6 from **Q** to **C**. Does it become less stable, and by how much?

AFSSE**Q**LARLKREFNENRYLTERRRQQLSSELGLNEAQIKIWFQNKRA

**Expected answer (experimental reference):** Yes—less stable, with a change of about **+0.91 kcal/mol** in folding free energy.

**What is BioEmu?** BioEmu is an AI model that takes a protein sequence and generates many possible three-dimensional shapes. It approximates the mixture of shapes a protein adopts, which would otherwise be expensive to explore with molecular simulations. These samples can be used to estimate how often the protein stays folded.

**How the published BioEmu workflow gets to a one-number answer:**

1. Find related sequences and compute AlphaFold2 representations of the original and changed proteins.
2. Use BioEmu to sample possible shapes; the benchmark recommends **5,000 per protein**.
3. Compare them with the supplied benchmark reference structure to estimate how often each protein is folded, then calculate its folding free energy.
4. Subtract the two energies to predict the stability change.

Evaluation compares the predicted number with the experimental reference. The question and answer are simple; producing a supported prediction involves substantial intermediate computation.

[More worked examples, complete saved reasoning, exact inputs and tool details](WORKED_EXAMPLES.md)

## Dataset catalog

Each row is one dataset or source-defined evaluation condition. Expand a category for detail. The input/computation column describes the scientific requirement, including external models where needed.

Qwen results and published reference results use the stated protocols and are not automatically matched comparisons. **—** means no verified Qwen result is displayed; **\*** marks limited coverage or scoring. Source qualifications are collected at the end.

<a id="protein-traits-and-interactions"></a>

<details>
<summary><h2>Protein traits and interactions</h2></summary>

#### Whether proteins dissolve

| Task | Dataset/protocol | Input / required computation | Qwen result | Published reference |
|---|---|---|---|---|
| Protein solubility | DeepSol solubility — PEER split | Protein sequence | accuracy 24.2% | BioT5+: accuracy 74.37% ± 0.19 percentage points; Table 6 · [source](https://arxiv.org/html/2402.17810v2) |
|  | PFMBench solubility panel | Protein sequences/features; partner/context inputs for interaction tasks | — | ESM2-Adapter, Table 1 means: DeepSol AUROC 0.8467; DeepSoluE AUROC 0.7699; ProtSolM AUROC 0.8572; eSOL Spearman 0.2761 · [source](https://arxiv.org/html/2506.14796v1) |

#### Where proteins go in a cell

| Task | Dataset/protocol | Input / required computation | Qwen result | Published reference |
|---|---|---|---|---|
| Binary protein localization | DeepLoc — binary and 10-compartment localization<br>Binary localization — DeepLoc/PEER | Protein sequence; Protein sequence; label descriptions in zero-shot mode | accuracy 27.4% | BioT5+: accuracy 90.41% ± 0.07 percentage points; Table 6 · [source](https://arxiv.org/html/2402.17810v2) |
| Ten-compartment protein localization | DeepLoc — binary and 10-compartment localization<br>Subcellular localization — DeepLoc | Protein sequence; Protein sequence; label descriptions in zero-shot mode | accuracy 26.1% | ProtST-ESM-1b: fixed encoder.accuracy 82.0%; full model tuning.accuracy 78.73%; Table 2, printed p.6 · [source](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf) |
| Localization and sorting signals | PFMBench localization and sorting-signal panel | Protein sequences/features; partner/context inputs for interaction tasks | — | ESM2-Adapter, Table 1 means: DeepLocMulti Accuracy 0.7666; DeepLoc2Multi F1 0.7505; DeepLocBinary AUROC 0.9338; SortingSignal F1 0.8598 · [source](https://arxiv.org/html/2506.14796v1) |

#### Protein activity, stability and production

| Task | Dataset/protocol | Input / required computation | Qwen result | Published reference |
|---|---|---|---|---|
| Protein fluorescence* | TAPE GFP / Sarkisyan fluorescence | Protein/variant sequence | **Diagnostic only:** spearman undefined; spearman_parsed_only 0.0155<br>Full native primary metric undefined. | ProtST-ESM-1b: fixed encoder.spearman 0.523; full model tuning.spearman 0.682; Table 2, printed p.6 · [source](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf) |
| Protein stability | TAPE / Rocklin stability | Protein/variant sequence | — | Spearman: ProtST-ESM-2 0.738; ESM-2 0.718. · [source](https://arxiv.org/html/2206.02096v2) |
| Protein thermostability prediction* | FLIP — AAV and Meltome<br>Thermostability — FLIP/Meltome | Protein/variant sequence | **Diagnostic only:** spearman undefined; spearman_parsed_only 0.0254<br>Full native primary metric undefined. | ProtST-ESM-1b: fixed encoder.spearman 0.68; full model tuning.spearman 0.681; Table 2, printed p.6 · [source](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf) |
| Enzyme activity | Envision β-lactamase — PEER split | Protein/variant sequence | — | Spearman: ProtST-ESM-2 0.879; ESM-2 0.867. · [source](https://arxiv.org/html/2206.02096v2) |
| AAV variant fitness prediction | FLIP — AAV and Meltome<br>AAV variant fitness — FLIP | Protein/variant sequence | — | Spearman, ProtST-ESM-2 vs ESM-2: AAV 0.825 vs 0.817; Meltome 0.682 vs 0.672. · [source](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf) |
| Protein stability classification | NatureLM/PEER binarized stability — paper-specific protocol | Protein sequence | — | NatureLM-8x7B: 72.3% accuracy; SFM-Protein-650M: 58.3%, in NatureLM's stability-classification setup. · [source](https://arxiv.org/html/2502.07527v3) |
| Protein production and enzyme conditions | PFMBench production and enzyme-operating panel | Protein sequences/features; partner/context inputs for interaction tasks | — | ESM2-Adapter, Table 1 means: Optimal_pH Spearman 0.0564; DeepET_Topt Spearman 0.2628; Cloning_CLF AUROC 0.8160; Material_Production Accuracy 0.7982; Enzyme_Eff. Spearman 0.2173; Antib._Res. Accuracy 0.6185; Thermostability AUROC 0.9553 · [source](https://arxiv.org/html/2506.14796v1) |

#### Which proteins bind each other

| Task | Dataset/protocol | Input / required computation | Qwen result | Published reference |
|---|---|---|---|---|
| Human protein–protein interaction prediction | Human/Pan and yeast/Guo PPI — PEER<br>Human protein–protein interaction — PEER | Two full protein sequences | accuracy 50.2% | BioT5+ (supervised): accuracy 85.09% ± 0.4 percentage points; Table 6 · [source](https://arxiv.org/html/2402.17810v2) |
| Yeast protein–protein interaction prediction | Human/Pan and yeast/Guo PPI — PEER<br>Yeast protein–protein interaction — PEER | Two full protein sequences | accuracy 45.2% | BioT5+ (supervised): accuracy 66.16% ± 0.43 percentage points; Table 6 · [source](https://arxiv.org/html/2402.17810v2) |
| Protein and metal interactions | PFMBench protein and metal-interaction panel | Protein sequences/features; partner/context inputs for interaction tasks | — | ESM2-Adapter, Table 1 means: Human_PPI AUROC 0.4828; Yeast_PPI AUROC 0.5343; PPI_Affinity Spearman -0.0047; MetalIonBinding Accuracy 0.7066 · [source](https://arxiv.org/html/2506.14796v1) |
| Protein interface contacts | ATOM3D interface contacts (PIP) | Unbound protein structures → residue-pair contact | — | AUROC: 3D-CNN 0.844; GNN 0.669; non-3D baseline 0.841. · [source](https://arxiv.org/html/2012.04035v3) |

#### Antibody properties

| Task | Dataset/protocol | Input / required computation | Qwen result | Published reference |
|---|---|---|---|---|
| Antibody properties | FLAb / FLAb2 antibody property collection | Antibody sequences; task-dependent measured context | — | No version-matched aggregate model score transcribed; repository supplies per-assay zero-/few-shot evaluation outputs. · [source](https://github.com/Graylab/FLAb) |

</details>

<a id="what-proteins-do"></a>

<details>
<summary><h2>What proteins do</h2></summary>

#### Assigning protein functions and enzyme classes

| Task | Dataset/protocol | Input / required computation | Qwen result | Published reference |
|---|---|---|---|---|
| Enzyme Commission annotation | DeepFRI-derived EC and GO test splits<br>Enzyme Commission labels — DeepFRI split | Protein sequence | — | Fmax, ProtST-ESM-2 vs ESM-2: EC 0.878 vs 0.874; GO-BP 0.482 vs 0.472; GO-MF 0.668 vs 0.662; GO-CC 0.487 vs 0.472. · [source](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf) |
| Gene Ontology: biological process | DeepFRI-derived EC and GO test splits<br>GO biological process — DeepFRI split | Protein sequence | — | Fmax, ProtST-ESM-2 vs ESM-2: EC 0.878 vs 0.874; GO-BP 0.482 vs 0.472; GO-MF 0.668 vs 0.662; GO-CC 0.487 vs 0.472. · [source](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf) |
| Gene Ontology: molecular function | DeepFRI-derived EC and GO test splits<br>GO molecular function — DeepFRI split | Protein sequence | — | Fmax, ProtST-ESM-2 vs ESM-2: EC 0.878 vs 0.874; GO-BP 0.482 vs 0.472; GO-MF 0.668 vs 0.662; GO-CC 0.487 vs 0.472. · [source](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf) |
| Gene Ontology: cellular component | DeepFRI-derived EC and GO test splits<br>GO cellular component — DeepFRI split | Protein sequence | — | Fmax, ProtST-ESM-2 vs ESM-2: EC 0.878 vs 0.874; GO-BP 0.482 vs 0.472; GO-MF 0.668 vs 0.662; GO-CC 0.487 vs 0.472. · [source](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf) |
| Enzyme and Gene Ontology annotation | PFMBench GO/EC annotation panel | Protein sequences/features; partner/context inputs for interaction tasks | — | ESM2-Adapter, Table 1 means: GO-CC F1 0.6130; GO-MF F1 0.6488; GO-BP F1 0.5412; EC F1 0.7379 · [source](https://arxiv.org/html/2506.14796v1) |

#### Protein function descriptions

| Task | Dataset/protocol | Input / required computation | Qwen result | Published reference |
|---|---|---|---|---|
| Protein function description generation | Mol-Instructions — four protein-description subsets<br>Mol-Instructions: Protein function generation | Full protein sequence and instruction | rouge1 0.0631; rouge2 0.0139; rougeL 0.0431; rougeLsum 0.0542 | Verified numerical comparator unavailable · [source](https://arxiv.org/html/2306.08018v4) |
| Catalytic activity description generation | Mol-Instructions — four protein-description subsets<br>Mol-Instructions: Catalytic activity generation | Full protein sequence and instruction | rouge1 0.0541; rouge2 0.0140; rougeL 0.0396; rougeLsum 0.0473 | Verified numerical comparator unavailable · [source](https://arxiv.org/html/2306.08018v4) |
| Protein domain and motif description generation | Mol-Instructions — four protein-description subsets<br>Mol-Instructions: Domain and motif generation | Full protein sequence and instruction | rouge1 0.0354; rouge2 0.0047; rougeL 0.0259; rougeLsum 0.0306 | Verified numerical comparator unavailable · [source](https://arxiv.org/html/2306.08018v4) |
| Protein functional description generation | Mol-Instructions — four protein-description subsets<br>Mol-Instructions: Functional description generation | Full protein sequence and instruction | rouge1 0.0800; rouge2 0.0123; rougeL 0.0494; rougeLsum 0.0649 | Verified numerical comparator unavailable · [source](https://arxiv.org/html/2306.08018v4) |
| Protein description generation | NatureLM's NCBI protein-description holdout | Protein sequence | — | ROUGE-L: NatureLM-8x7B 0.585; fine-tuned Llama-3-8B 0.324; GPT-4o 0.091. · [source](https://arxiv.org/html/2502.07527v3) |

#### Biochemical reaction classification

| Task | Dataset/protocol | Input / required computation | Qwen result | Published reference |
|---|---|---|---|---|
| Biochemical reaction classification | ProtST reaction classification — zero/few-shot | Protein sequence plus reaction-label descriptions | accuracy 0.2% | ProtST-ESM-1b: zero shot accuracy 29.85%; Table 11, printed p.15 · [source](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf) |

#### Evidence support for protein explanations

| Task | Dataset/protocol | Input / required computation | Qwen result | Published reference |
|---|---|---|---|---|
| Evidence support for protein-function explanations | BioReason-Pro explanation review | Protein-function claim and supporting evidence | — | Repository reports an LLM-judge score of 8/10 and expert preference over UniProt descriptions in 79% of reviewed cases. · [source](https://www.biorxiv.org/content/10.64898/2026.03.19.712954v2.full) |

#### Protein retrieval from descriptions

| Task | Dataset/protocol | Input / required computation | Qwen result | Published reference |
|---|---|---|---|---|
| Protein retrieval from functional descriptions | ProtST text-to-protein retrieval examples | Functional description and a searchable protein representation corpus | — | Selected text-to-protein retrieval and docking case studies are reported; no single fixed-corpus Recall@K benchmark result is transcribed. · [source](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf) |

</details>

<a id="effects-of-protein-mutations"></a>

<details>
<summary><h2>Effects of protein mutations</h2></summary>

#### Explaining mutation effects

| Task | Dataset/protocol | Input / required computation | Qwen result | Published reference |
|---|---|---|---|---|
| Mutation-effect explanation | MutaDescribe — mutation explanation | Reference and mutant sequences/change, plus model-specific protein context | — | Main-test average ROUGE-L / BLEU-2 (0–100): MutaPLM 21.34 / 13.61; GPT-4-0613, 5-shot kNN: 12.31 / 9.69. · [source](https://arxiv.org/html/2410.22949v1) |

#### Predicting and ranking mutation effects

| Task | Dataset/protocol | Input / required computation | Qwen result | Published reference |
|---|---|---|---|---|
| Mutation-effect ranking | ProteinGym substitutions — historical ProtST evaluation | Reference and variant sequences; optional structure/MSA only if the protocol allows | — | UniProt-level mean Spearman: ProtST-ESM-1b 0.412; ESM-1b 0.358; ESM-1v 0.372; Tranception L without retrieval 0.401. · [source](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf) |
|  | PG-LLM / ProteinGym-LLM — eval-data-v1.2 | Full reference sequence, assay description, shuffled candidate sequences | — | No verified release-matched model score was recovered. This does not mean zero performance. · [source](https://raw.githubusercontent.com/rohitarorayyc/proteingym-llm/main/DATA.md) |
| Single-mutant generation | PFArena — four task settings<br>PFArena T1: single-mutant generation | Protein sequence and objective; propose single mutations | — | Paper's GPT-6 Astra vs ESM-2: T1 Recall@40 0.0254 vs 0.0370; T2 Spearman 0.2726 vs 0.2539; T3 0.3516 vs 0.3128; T4 0.5988 vs 0.3153. · [source](https://arxiv.org/html/2609.28921v1) |
| Multi-mutant ranking without measurements | PFArena — four task settings<br>PFArena T2: measurement-free multi-mutant ranking | Protein variants and objective; rank without measured outcomes | — | Paper's GPT-6 Astra vs ESM-2: T1 Recall@40 0.0254 vs 0.0370; T2 Spearman 0.2726 vs 0.2539; T3 0.3516 vs 0.3128; T4 0.5988 vs 0.3153. · [source](https://arxiv.org/html/2609.28921v1) |
| Mutation ranking with anchor measurements | PFArena — four task settings<br>PFArena T3: anchor-informed ranking | Measured anchor mutation plus candidate combinations | — | Paper's GPT-6 Astra vs ESM-2: T1 Recall@40 0.0254 vs 0.0370; T2 Spearman 0.2726 vs 0.2539; T3 0.3516 vs 0.3128; T4 0.5988 vs 0.3153. · [source](https://arxiv.org/html/2609.28921v1) |
| Mutation ranking with single-mutant measurements | PFArena — four task settings<br>PFArena T4: single-mutant-informed ranking | Measured single mutations plus candidate combinations | — | Paper's GPT-6 Astra vs ESM-2: T1 Recall@40 0.0254 vs 0.0370; T2 Spearman 0.2726 vs 0.2539; T3 0.3516 vs 0.3128; T4 0.5988 vs 0.3153. · [source](https://arxiv.org/html/2609.28921v1) |
| Mutation and fitness prediction | PFMBench mutation/fitness panel | Protein sequences/features; partner/context inputs for interaction tasks | — | ESM2-Adapter, Table 1 means: PETA_CHS_SOL Spearman 0.2738; PETA_LGK_SOL Spearman 0.1558; PETA_TEM_SOL Spearman 0.1433; FLIP_AAV Spearman 0.9412; FLIP_GB1 Spearman 0.9517; TAPE_Stab Spearman 0.3211; TAPE_Fluor Spearman 0.6812; BetaLactamase Spearman 0.5740 · [source](https://arxiv.org/html/2506.14796v1) |
| Zero-shot mutation-effect ranking | PFMBench ProteinGym zero-shot protocol | Protein sequences/features; partner/context inputs for interaction tasks | — | Table 1 reports pretrained ESM2 ProteinGym Spearman 0.4390; do not compare directly to a different snapshot's score. · [source](https://arxiv.org/html/2506.14796v1) |
| Low-data fitness regression | MutaPLM low-data fitness regression | Variant representations; a separately fitted regression head | — | Low-data regression curves are reported with 192 train / 48 validation examples; no exact assay-specific point estimate is transcribed here. · [source](https://arxiv.org/html/2410.22949v1) |

#### Choosing mutations to improve a protein

| Task | Dataset/protocol | Input / required computation | Qwen result | Published reference |
|---|---|---|---|---|
| Mutation engineering with a supplied position | MutaDescribe — mutation engineering<br>MutaDescribe mutation engineering — position supplied | Protein sequence, desired effect and mutation position | — | MutaPLM vs fine-tuned ESM-2: position known accuracy 53.51% vs 51.43%; position unknown Recall@50 40.94% vs 33.77%. · [source](https://arxiv.org/html/2410.22949v1) |
| Mutation engineering with an unknown position | MutaDescribe — mutation engineering<br>MutaDescribe mutation engineering — position unknown | Protein sequence and desired effect; propose mutation positions and residues | — | MutaPLM vs fine-tuned ESM-2: position known accuracy 53.51% vs 51.43%; position unknown Recall@50 40.94% vs 33.77%. · [source](https://arxiv.org/html/2410.22949v1) |
| Protein-sequence optimization against fitness predictors<br>Predictor-scored optimization; not measured laboratory success. | MutaPLM iterative optimization | See the source-defined input and metric below | — | The paper reports predicted-fitness improvement trajectories across six landscapes; these are oracle-based search outcomes, not experimentally measured hit rates. · [source](https://arxiv.org/html/2410.22949v1) |

#### Binding affinity and immune interactions

| Task | Dataset/protocol | Input / required computation | Qwen result | Published reference |
|---|---|---|---|---|
| Antibody affinity ranking | AbBiBench antibody affinity ranking | Antibody/target sequences and permitted structural context; varies by model | — | Current 16-column leaderboard mean Spearman: ProteinMPNN 0.30; ESM-IF1 0.28; AntiFold 0.21; ESM2 0.02. · [source](https://github.com/MSBMI-SAFE/AbBiBench) |
| Peptide–MHC and TCR–pMHC interactions | PFMBench peptide–MHC and TCR–pMHC panel | Protein sequences/features; partner/context inputs for interaction tasks | — | ESM2-Adapter, Table 1 means: Pept.HLA/MHC Aff. AUROC 0.9631; TCR.PMHC Aff. AUROC 0.9312 · [source](https://arxiv.org/html/2506.14796v1) |
| Mutation effects on binding affinity | ATOM3D SKEMPI-derived mutation affinity (MSP) | Wild-type/mutant structural context | — | AUROC: GNN 0.621; 3D-CNN 0.574. · [source](https://arxiv.org/html/2012.04035v3) |

</details>

<a id="answering-biology-research-questions"></a>

<details>
<summary><h2>Answering biology research questions</h2></summary>

#### Biological research question answering

| Task | Dataset/protocol | Input / required computation | Qwen result | Published reference |
|---|---|---|---|---|
| Literature evidence question answering* | LAB-Bench — research tasks<br>LAB-Bench / LitQA2 | Text question and choices | accuracy 39.1%; precision 41.0%; coverage 95.4% | GPT-5.2: accuracy 45.7%; n=199; Table 1 · [source](https://arxiv.org/html/2606.00902v1) |
| Biological database question answering | LAB-Bench — research tasks<br>LAB-Bench / DbQA | Database question and choices | accuracy 31.3%; precision 31.8%; coverage 98.5% | GPT-5.2: accuracy 41.7%; n=520; Table 1 · [source](https://arxiv.org/html/2606.00902v1) |
| Supplementary-material question answering | LAB-Bench — research tasks<br>LAB-Bench / SuppQA | Question with the source paper's title and DOI | accuracy 37.8%; precision 39.2%; coverage 96.3% | GPT-5.2: accuracy 48.8%; n=82; Table 1 · [source](https://arxiv.org/html/2606.00902v1) |
| Research figure question answering | LAB-Bench — research tasks<br>LAB-Bench / FigQA | Scientific figure image and question | accuracy 72.4%; precision 72.8%; coverage 99.4% | GPT-5.2: accuracy 36.5%; n=181; Table 1 · [source](https://arxiv.org/html/2606.00902v1) |
| Research table question answering | LAB-Bench — research tasks<br>LAB-Bench / TableQA | Scientific table image and question | accuracy 88.1%; precision 90.0%; coverage 98.0% | GPT-5.2: accuracy 36.9%; n=244; Table 1 · [source](https://arxiv.org/html/2606.00902v1) |
| Biological sequence question answering | LAB-Bench — research tasks<br>LAB-Bench / SeqQA | Biological sequence and requested operation | accuracy 12.7%; precision 12.8%; coverage 99.2% | GPT-5.2: accuracy 47.0%; n=600; Table 1 · [source](https://arxiv.org/html/2606.00902v1) |
| Molecular cloning question answering | LAB-Bench — research tasks<br>LAB-Bench / Cloning scenarios | Cloning scenario and sequence constraints | accuracy 0.0%; precision 0.0%; coverage 100.0% | GPT-5.2: accuracy 36.4%; n=33; Table 1 · [source](https://arxiv.org/html/2606.00902v1) |
| Protein understanding | ProteinLMBench protein-understanding questions | Text question + choices | — | InternLM2-7B after SFT: 58.26% accuracy; SSL+SFT: 62.18%. · [source](https://arxiv.org/html/2406.05540v1) |
| Research-abstract question answering | PubMedQA research-abstract questions | Question + source abstract | — | Original BioBERT multi-phase training: 68.1% accuracy; reported human baseline 78.0%. Historical results. · [source](https://arxiv.org/abs/1909.06146) |
| Experimental protocol question answering | LAB-Bench — research tasks<br>LAB-Bench / ProtocolQA | Protocol text and question | — | Historical 2024 GPT-4o accuracy: LitQA2 27%; SuppQA 13%; FigQA 29%; TableQA 71%; ProtocolQA 53%; Cloning 28%. DbQA variant-from-sequence 42%; SeqQA GC% 29%, ORF-sequence 50% (SUBTASK values only). · [source](https://arxiv.org/html/2407.10362v1) |

</details>

<a id="designing-proteins"></a>

<details>
<summary><h2>Designing proteins</h2></summary>

#### Protein sequence and structure generation

| Task | Dataset/protocol | Input / required computation | Qwen result | Published reference |
|---|---|---|---|---|
| Text-conditioned protein-sequence design<br>Lexical sequence overlap; biological function untested. | BioT5+ description-guided protein generation | Functional description → amino-acid sequence | — | Description-guided protein designs are presented as qualitative cases rather than a fixed, experimentally validated design-success rate. · [source](https://arxiv.org/html/2402.17810v2) |
| Unconditional protein backbone generation | ProteinBench unconditional backbone generation | Length/constraints → 3D backbone; ProteinMPNN and ESMFold evaluation | — | At length 100: RFdiffusion scTM 0.98 ± 0.12 and scRMSD 0.48 ± 0.56 Å; FrameFlow 0.94 ± 0.08 and 0.70 ± 0.70 Å. · [source](https://arxiv.org/html/2409.06744v2) |
| Unconditional protein sequence generation | ProteinBench unconditional sequence generation | Generated sequences; AlphaFold2 structural-confidence evaluation | — | At length 100, predicted AF2 pLDDT: DPLM-650M 85.38 ± 14.20; ProGen2-700M 64.00 ± 21.26. · [source](https://arxiv.org/html/2409.06744v2) |
| Joint sequence and structure generation | ProteinBench joint sequence–structure generation | Sequence and 3D coordinates; folding and structural comparison | — | Multiflow at length 100: scTM 0.96 ± 0.04; scRMSD 1.10 ± 0.71 Å. At length 200: scTM 0.95; scRMSD 1.61 Å. · [source](https://arxiv.org/html/2409.06744v2) |
| Unconditional protein generation<br>Structure quality is predicted; function is not experimentally established. | NatureLM generated proteins: unconditional / property-conditioned / heme<br>NatureLM unconditional generation | Generated protein sequences; OmegaFold structural-confidence evaluation | — | Reported outputs are diversity/length distributions and predicted structural confidence. No experimentally measured function-success fraction is supplied by this evaluation. The reported comparison uses learned stability/solubility scores and diversity. No measured stability/solubility success rate is transcribed. Selected heme-binding candidates are screened with descriptions and predicted complexes; this is not experimentally demonstrated heme binding. · [source](https://arxiv.org/html/2502.07527v3) |
| Protein generation for predicted stability and solubility<br>Stability and solubility are predicted, not measured. | NatureLM generated proteins: unconditional / property-conditioned / heme<br>NatureLM stability/solubility-conditioned generation | Property-conditioned sequences and independent property predictors | — | Reported outputs are diversity/length distributions and predicted structural confidence. No experimentally measured function-success fraction is supplied by this evaluation. The reported comparison uses learned stability/solubility scores and diversity. No measured stability/solubility success rate is transcribed. Selected heme-binding candidates are screened with descriptions and predicted complexes; this is not experimentally demonstrated heme binding. · [source](https://arxiv.org/html/2502.07527v3) |
| Heme-binding protein candidate generation<br>Heme binding is a predicted candidate property, not demonstrated binding. | NatureLM generated proteins: unconditional / property-conditioned / heme<br>NatureLM heme-binding case study | Heme-related description; candidate sequences and complex screening | — | Reported outputs are diversity/length distributions and predicted structural confidence. No experimentally measured function-success fraction is supplied by this evaluation. The reported comparison uses learned stability/solubility scores and diversity. No measured stability/solubility success rate is transcribed. Selected heme-binding candidates are screened with descriptions and predicted complexes; this is not experimentally demonstrated heme binding. · [source](https://arxiv.org/html/2502.07527v3) |

#### Making fluorescent proteins brighter

| Task | Dataset/protocol | Input / required computation | Qwen result | Published reference |
|---|---|---|---|---|
| GFP sequence optimization against a fluorescence predictor*<br>Scored by a fluorescence predictor; not a wet-lab result. | STRIDE GFP sequence optimization | GFP sequence edits; fixed fluorescence predictor for evaluation | replace_only.qualified_oracle_success 0.0000; replace_only.improved_sequence_uniqueness undefined; replace_only.native_novelty undefined; full_atomic.qualified_oracle_success 0.0000; full_atomic.improved_sequence_uniqueness undefined; full_atomic.native_novelty undefined | STRIDE: success count 61; attempt count 100; unique improved count 59; n=100; Table 4 · [source](https://arxiv.org/html/2603.03573v1) |

#### Antibody design

| Task | Dataset/protocol | Input / required computation | Qwen result | Published reference |
|---|---|---|---|---|
| Antibody design: CDR-H3 redesign | RAbD — CDR-H3 redesign | Antigen, antibody framework, fixed complex context; H3 masked | — | Proteo-R1 vs BoltzGen: AAR 10.75% vs 39.07%; RMSD 2.46 Å vs 2.69 Å; DockQ 0.801 vs 0.473. · [source](https://arxiv.org/html/2605.02937v1) |
|  | ProteinBench antibody design — processed RAbD | Complex structure + masked H3 → sequence/structure | — | DiffAb: AAR 35.04 ± 8.36%, RMSD 2.53 ± 0.60 Å; MEAN: AAR 33.47%, RMSD 1.82 Å. · [source](https://arxiv.org/html/2409.06744v2) |
| Antibody design: multi-CDR redesign | SAbDab — Proteo-R1 all-CDR holdout | Antigen/framework/docking context with CDR sequence/geometry masked | — | Proteo-R1 vs MFDesign: H3 RMSD 3.81 Å vs 3.71 Å; Loop-RMSD 4.51 Å vs 4.28 Å; IMP 56.58 vs 59.16 (paper's scale). · [source](https://arxiv.org/html/2605.02937v1) |
| Antibody design: epitope-conditioned design | CHIMERA-Bench epitope-conditioned antibody design | Antigen/framework/epitope context → CDR sequence+structure | — | Epitope-group H3: RAAD AAR 0.37, RMSD 1.75 Å, DockQ 0.58; dyMEAN EpiF1 0.23 (RAAD 0.11). · [source](https://arxiv.org/html/2603.13431v1) |

#### Finding a sequence for a desired shape

| Task | Dataset/protocol | Input / required computation | Qwen result | Published reference |
|---|---|---|---|---|
| Sequence design by inverse folding | CATH 4.2 / TS50 / TS500 inverse folding | Backbone coordinates → amino-acid sequence; coordinate-conditioned design | — | PiFold repository: CATH recovery 51.66%; TS50 58.72%; TS500 60.42%. · [source](https://github.com/a4bio/pifold) |
|  | ProteinBench inverse folding — CASP15 / CAMEO / synthetic backbones | Backbone coordinates → sequence; AlphaFold2 refolding evaluation | — | AAR, CASP15/CAMEO: LM-Design 0.516/0.570; ProteinMPNN 0.450/0.468. · [source](https://arxiv.org/html/2409.06744v2) |

#### Building around a functional protein part

| Task | Dataset/protocol | Input / required computation | Qwen result | Published reference |
|---|---|---|---|---|
| Functional-motif scaffolding | MotifBench functional-motif scaffolding | Motif coordinates → scaffold; ProteinMPNN, ESMFold and structural comparison | — | Official leaderboard snapshot: RFdiffusion3 43.52 ± 1.35 (Aug 2026); RFdiffusion 21.95 (Feb 2025), in MotifBench-score units. · [source](https://github.com/blt2114/MotifBench) |
|  | ProteinBench motif scaffolding — legacy motif panel | Motif coordinates → scaffold; native structural evaluator | — | Comparative motif-scaffolding results are reported; exact figure-derived score not transcribed. · [source](https://arxiv.org/html/2409.06744v2) |

#### Designing proteins that bind a target

| Task | Dataset/protocol | Input / required computation | Qwen result | Published reference |
|---|---|---|---|---|
| Target-binder design | ProtDBench de novo target-binder design | Target coordinates/sequence/hotspots → proposed binders | — | PD-L1 passing-backbone counts: PXDesign 1,247; BoltzGen 549; RFdiffusion3 542; BindCraft 231. TNFα: PXDesign 57; BoltzGen 15. · [source](https://arxiv.org/html/2605.04118v1) |
| GM2A-targeted binder design<br>Single published target campaign. | Prompteina text-conditioned protein design — GM2A campaign | See the source-defined input and metric below | — | 9 of 89 assayed designs classified as binders; 8 fitted apparent KD values. Strongest apparent KD: 107 nM. · [source](https://arxiv.org/html/2610.13917v1) |

</details>

<a id="protein-shapes-and-motion"></a>

<details>
<summary><h2>Protein shapes and motion</h2></summary>

#### Local structure and residue prediction

| Task | Dataset/protocol | Input / required computation | Qwen result | Published reference |
|---|---|---|---|---|
| Structure-derived protein prediction | PFMBench structure-derived prediction panel | Protein sequences/features; partner/context inputs for interaction tasks | — | ESM2-Adapter, Table 1 means: Contact Top L/5 0.7199; FoldClass Accuracy 0.7859; SecondaryStructure Accuracy 0.7601 · [source](https://arxiv.org/html/2506.14796v1) |
| Residue identity from local structure | ATOM3D residue identity from local structure (RES) | 3D local atomic environment → amino-acid label | — | ATOM3D 3D-CNN test accuracy: 0.451. · [source](https://arxiv.org/html/2012.04035v3) |

#### Structure-derived questions and output checks

| Task | Dataset/protocol | Input / required computation | Qwen result | Published reference |
|---|---|---|---|---|
| Structure-derived questions and output-format checks<br>Independent held-out questions remain unresolved. | Proteo-R1 internal alignment / structural / CDR diagnostics | See the source-defined input and metric below | — | Selected Stage-II M3: contact 58.3%; interface 15.1%; hotspot 11.6%. Separate Stage-I schema 81.4%. No overall score. · [source](https://arxiv.org/html/2605.02937v1) |

#### Protein structure ranking

| Task | Dataset/protocol | Input / required computation | Qwen result | Published reference |
|---|---|---|---|---|
| Protein structure ranking | ATOM3D protein structure ranking (PSR) | Candidate coordinates → quality score | — | Per-target mean Spearman: GNN 0.515; 3D-CNN 0.431. Global correlations are different metrics. · [source](https://arxiv.org/html/2012.04035v3) |

#### Protein folding

| Task | Dataset/protocol | Input / required computation | Qwen result | Published reference |
|---|---|---|---|---|
| Single-state protein folding | ProteinBench single-state folding — CAMEO 2022 | Protein sequence → 3D coordinates; folding model and structural comparison | — | AF2 mean/median TM-score 0.871/0.952, RMSD 3.21/1.64 Å; ESMFold 0.847/0.929 and 3.98/2.10 Å. · [source](https://arxiv.org/html/2409.06744v2) |

#### Protein shape changes, motion and stability

| Task | Dataset/protocol | Input / required computation | Qwen result | Published reference |
|---|---|---|---|---|
| Multistate protein conformations | ProteinBench multistate conformations — apo/holo and BPTI | Sequence → conformational ensemble | — | Apo/holo TM-ensemble: AlphaFlow-PDB 0.873; MSA-depth256 0.867. BPTI N=1000: ConfDiff-ESM-force ensemble RMSD 1.36 Å. · [source](https://arxiv.org/html/2409.06744v2) |
| Protein conformational ensembles | ProteinBench ensemble distribution — ATLAS | Sequence → ensemble | — | AlphaFlow-MD: per-target RMSF correlation 0.85 and PCA-Wasserstein 1.55; ConfDiff PCA-Wasserstein 1.41 (paper's units). · [source](https://arxiv.org/html/2409.06744v2) |
| Protein states, dynamics and free energy | BioEmu benchmark collection — states, dynamics and free energy | Protein sequence → conformational ensemble | — | Official model card: domain-motion coverage 83%; cryptic-pocket apo/holo coverage 55%/88%; experimental stability MAE ~0.9 kcal/mol, Spearman ~0.6. · [source](https://github.com/microsoft/bioemu/blob/main/MODEL_CARD.md) |

</details>

<a id="understanding-biomedical-images"></a>

<details>
<summary><h2>Understanding biomedical images</h2></summary>

#### Biomedical visual question answering

| Task | Dataset/protocol | Input / required computation | Qwen result | Published reference |
|---|---|---|---|---|
| Radiology image question answering | Biomedical VQA: VQA-RAD / SLAKE-English / PathVQA / VQA-Med 2019<br>VQA-RAD | Radiology image and question | open_token_recall 59.5%; closed_accuracy 86.8% | LLaVA-Med 7B, CLIP, 60K-IM, stage1=1/stage2=3/FT=0: open token recall 28.23%; closed accuracy 61.4%; n=451; Table 4(b), PDF p.9 · [source](https://arxiv.org/pdf/2306.00890) |
| Medical image question answering in English | Biomedical VQA: VQA-RAD / SLAKE-English / PathVQA / VQA-Med 2019<br>SLAKE — English | Medical image and English question | open_token_recall 51.0%; closed_accuracy 84.6% | LLaVA-Med 7B, CLIP, 60K-IM, stage1=1/stage2=3/FT=0: open token recall 39.17%; closed accuracy 52.16%; n=1061; Table 4(b), PDF p.9 · [source](https://arxiv.org/pdf/2306.00890) |
| Pathology image question answering | Biomedical VQA: VQA-RAD / SLAKE-English / PathVQA / VQA-Med 2019<br>PathVQA | Pathology image and question | open_token_recall 26.4%; closed_accuracy_corrected 0.8587 | LLaVA-Med 7B, CLIP, 60K-IM, stage1=1/stage2=3/FT=0: open token recall 12.3%; closed accuracy 54.05%; n=6761; Table 4(b), PDF p.9 · [source](https://arxiv.org/pdf/2306.00890) |
| Medical image question answering | Biomedical VQA: VQA-RAD / SLAKE-English / PathVQA / VQA-Med 2019<br>ImageCLEF-VQA 2019 | Medical image and question | strict_accuracy 0.0% | MedVInT-TE: overall accuracy 70.5%; Table 2 · [source](https://arxiv.org/html/2305.10415v6) |

#### Scientific figures, documents and visual conversations

| Task | Dataset/protocol | Input / required computation | Qwen result | Published reference |
|---|---|---|---|---|
| Scientific figure question answering | PMC-VQA figure question answering | Image, question, and optionally answer choices | native_td_final_character_accuracy 0.0200; adapted_full_text_closest_choice_accuracy 0.4975; adapted_full_text_released_label_accuracy 0.4975; strict_final_label_accuracy 0.0070 | MedVInT-TD / PMC-LLaMA / PMC-CLIP: choice accuracy 40.3%; blank accuracy 33.6%; blank bleu1 21.5%; n=2000; Table 3 · [source](https://arxiv.org/html/2305.10415v6) |
| Biomedical visual conversations | LLaVA-Med biomedical visual conversations | Biomedical image and conversational questions | — | GPT-assisted relative answer-quality comparisons are reported. A verified single aggregate for the specified qa50 setting is not transcribed here. · [source](https://arxiv.org/abs/2306.00890) |
| Scientific document and figure extraction | Ryze document-extraction component tests | Scientific document pages, figures and extraction targets | — | Ryze extraction-component accuracy: ArXivQA 73.12%, SlideVQA 66.48%, ChartQA 75.8%. · [source](https://arxiv.org/html/2606.00902v1) |

</details>

<a id="dna-rna-and-small-molecules"></a>

<details>
<summary><h2>DNA, RNA and small molecules</h2></summary>

#### Molecular interactions and binding affinity

| Task | Dataset/protocol | Input / required computation | Qwen result | Published reference |
|---|---|---|---|---|
| Drug–target interaction | Drug–target interaction: BioSNAP / Human / BindingDB<br>Drug–target interaction — BioSNAP/Human/BindingDB · bindingdb | Small-molecule representation and protein sequence | AUROC 0.5036; AP 0.4103 | BioT5+ (supervised): AUROC 0.964 ± 0.001; Table 8 · [source](https://arxiv.org/html/2402.17810v2) |
|  | Drug–target interaction: BioSNAP / Human / BindingDB<br>Drug–target interaction — BioSNAP/Human/BindingDB · biosnap | Small-molecule representation and protein sequence | AUROC 0.5336; AP 0.5217 | BioT5+ (supervised): AUROC 0.939 ± 0.001; Table 8 · [source](https://arxiv.org/html/2402.17810v2) |
|  | Drug–target interaction: BioSNAP / Human / BindingDB<br>Drug–target interaction — BioSNAP/Human/BindingDB · human | Small-molecule representation and protein sequence | AUROC 0.4747; AP 0.4194 | BioT5+ (supervised): AUROC 0.987 ± 0.001; Table 8 · [source](https://arxiv.org/html/2402.17810v2) |
| Protein–ligand binding affinity | PFMBench PDBbind / BindingDB affinity panel | Protein sequences/features; partner/context inputs for interaction tasks | — | ESM2-Adapter, Table 1 means: PDBBind Spearman 0.1677; BindingDB Spearman 0.1922 · [source](https://arxiv.org/html/2506.14796v1) |
|  | ATOM3D protein–ligand affinity (LBA) | Protein–ligand coordinates → assay-derived affinity | — | 3D-CNN: RMSE 1.416, Spearman 0.553; GNN: RMSE 1.570, Spearman 0.628. · [source](https://arxiv.org/html/2012.04035v3) |
| Ligand efficacy | ATOM3D ligand efficacy (LEP) | Ligand/receptor conformations → efficacy class | — | AUROC: GNN 0.740; 3D-CNN 0.589. · [source](https://arxiv.org/html/2012.04035v3) |

#### RNA structure ranking

| Task | Dataset/protocol | Input / required computation | Qwen result | Published reference |
|---|---|---|---|---|
| RNA structure ranking | ATOM3D RNA structure ranking (RSR) | RNA candidate coordinates → quality score | — | Mean per-target Spearman: 3D-CNN 0.264; GNN 0.234. · [source](https://arxiv.org/html/2012.04035v3) |

#### Small-molecule properties

| Task | Dataset/protocol | Input / required computation | Qwen result | Published reference |
|---|---|---|---|---|
| Small-molecule properties | ATOM3D small-molecule properties (SMP / QM9) | Small-molecule atom coordinates → property | — | ENN dipole MAE 0.052 D; 3D-CNN 0.754 D. Property-specific scores must remain separate. · [source](https://arxiv.org/html/2012.04035v3) |

</details>

<details>
<summary>Dataset definitions, scientific qualifications and sources</summary>

## Protein traits and interactions

#### Whether proteins dissolve

#### DeepSol solubility — PEER split

Task-trained models; BioT5+ is multitask and BioT5 single-task. Count is PEER's published split, not a new loader count.

Published source size/units: Test: 1,999 proteins. Train: 62,478; validation: 6,942 (PEER Table 1).

**Protein solubility:** Does the expressed protein remain soluble under the dataset's assay setting? Metric: Accuracy. Preserve the official PEER solubility split; exact test size not re-established.

Not binding affinity, thermostability, or a guarantee of solubility under every laboratory condition.

**Comparison qualification:** Native source outcome, data split and metric when separately verified; prompted zero-shot full-sequence Qwen baseline, not matched specialist training. No native BioT5 special-token architecture or fitted regression/classification head reproduced.

[Source 1](https://arxiv.org/html/2206.02096v2), [Source 2](https://arxiv.org/html/2402.17810v2), [Source 3](https://github.com/DeepGraphLearning/PEER_Benchmark)

#### PFMBench solubility panel

These are PFMBench-specific processed datasets/splits, not interchangeable with PEER/ProtST results. F1 is not Fmax. Affinity-named AUROC tasks are classification, not KD regression. Exact loaders required.

Published source size/units: Test sizes: DeepSol: 6,934; DeepSoluE: 1,454; ProtSolM: 7,173; eSOL: 311

[Source 1](https://arxiv.org/html/2506.14796v1), [Source 2](https://github.com/biomap-research/PFMBench)

#### Where proteins go in a cell

#### DeepLoc — binary and 10-compartment localization

Binary comparison uses task-tuned systems. Ten-class numbers use frozen encoders + trained heads. These are distinct endpoints.

Published ten-class count is 2,768; the frozen local run contains 2,773 cases. These source-specific counts are retained separately.

Published source size/units: Published PEER test counts: binary 1,746; 10-compartment 2,768.

**Binary protein localization:** Is the protein membrane-associated or in the non-membrane/soluble class? Metric: Accuracy. Binary task; do not substitute the separate ten-compartment label set.

'Soluble' in the localization labels is not the same endpoint as expression solubility in P01.

**Ten-compartment protein localization:** Which cellular compartment does this protein belong to? Metric: Accuracy. Official DeepLoc split. ProtST also tests zero-/few-shot transfer; record shots and whether a supervised head is fitted.

Location is a different question from molecular activity or binding specificity.

**Comparison qualification:** Native source outcome, data split and metric when separately verified; prompted zero-shot full-sequence Qwen baseline, not matched specialist training. No native BioT5 special-token architecture or fitted regression/classification head reproduced.

**Comparison qualification:** Original released public test data and native outcome/metric; zero-shot Qwen prompt/representation/training regime differs from native-trained TAPE/ProtST heads.

[Source 1](https://arxiv.org/html/2206.02096v2), [Source 2](https://arxiv.org/html/2402.17810v2), [Source 3](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf), [Source 4](https://github.com/DeepGraphLearning/PEER_Benchmark), [Source 5](https://github.com/DeepGraphLearning/ProtST)

#### PFMBench localization and sorting-signal panel

These are PFMBench-specific processed datasets/splits, not interchangeable with PEER/ProtST results. F1 is not Fmax. Affinity-named AUROC tasks are classification, not KD regression. Exact loaders required.

Published source size/units: Test sizes: DeepLocMulti: 751; DeepLoc2Multi: 2,744; DeepLocBinary: 848; SortingSignal: 186

[Source 1](https://arxiv.org/html/2506.14796v1), [Source 2](https://github.com/biomap-research/PFMBench)

#### Protein activity, stability and production

#### Envision β-lactamase — PEER split

Full-model supervised fine-tuning. Assay-specific ranking, not an overall biology score.

Published source size/units: Test: 520 variants. Train: 4,158; validation: 520.

**Enzyme activity:** How active is this enzyme variant in the measured assay? Metric: Spearman correlation. Official PEER beta-lactamase split.

The numerical endpoint is assay-specific; these tasks do not establish a general ability to explain mechanisms.

[Source 1](https://arxiv.org/html/2206.02096v2), [Source 2](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf), [Source 3](https://github.com/DeepGraphLearning/PEER_Benchmark)

#### TAPE GFP / Sarkisyan fluorescence

Full-model supervised fine-tuning. Source counts are the TAPE split documented in PEER, not STRIDE's generated batch.

Published source size/units: Test: 27,217 variants. Train: 21,446; validation: 5,362.

**Protein fluorescence:** Which GFP variants emit stronger fluorescence under the measured conditions? Metric: Spearman correlation. TAPE fluorescence split; sequence-distance extrapolation is part of the benchmark.

The numerical endpoint is assay-specific; these tasks do not establish a general ability to explain mechanisms.

**Comparison qualification:** Original released public test data and native outcome/metric; zero-shot Qwen prompt/representation/training regime differs from native-trained TAPE/ProtST heads. Output-budget condition: MIXED_BUDGET_4K16K_CONTINUATION; 27146 historical cases retain4096 tokens and 71 clean never-dispatched cases receive16384 tokens. Original invalid/truncated cases remain included. This is not a uniform16k evaluation or a matched budget comparison.

[Source 1](https://arxiv.org/html/2206.02096v2), [Source 2](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf), [Source 3](https://github.com/songlab-cal/tape)

#### TAPE / Rocklin stability

Full-model supervised fine-tuning. Do not conflate with NatureLM's binarized stability task.

Published source size/units: Test: 12,851 proteins. Train: 53,571; validation: 2,512.

**Protein stability:** Which sequences have higher scores in the stability assay? Metric: Spearman correlation. Official TAPE stability split; retain the numerical target.

The numerical endpoint is assay-specific; these tasks do not establish a general ability to explain mechanisms.

[Source 1](https://arxiv.org/html/2206.02096v2), [Source 2](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf), [Source 3](https://github.com/songlab-cal/tape)

#### FLIP — AAV and Meltome

Two distinct source datasets, grouped under the FLIP suite. Full-model fine-tuning; no cross-assay average added.

Published source size/units: ProtST splits: AAV two_vs_many; Meltome human_cell. Exact test counts not verified in this review.

**AAV variant fitness prediction:** Which variants score higher in this particular experimental fitness assay? Metric: Spearman correlation. FLIP AAV two_vs_many split.

The numerical endpoint is assay-specific; these tasks do not establish a general ability to explain mechanisms.

**Protein thermostability prediction:** Which proteins have greater measured thermal stability? Metric: Spearman correlation. FLIP meltome human_cell configuration.

The numerical endpoint is assay-specific; these tasks do not establish a general ability to explain mechanisms.

**Comparison qualification:** Native source outcome, data split and metric when separately verified; prompted zero-shot full-sequence Qwen baseline, not matched specialist training. No native BioT5 special-token architecture or fitted regression/classification head reproduced.

[Source 1](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf), [Source 2](https://github.com/J-SNACKKB/FLIP), [Source 3](https://github.com/J-SNACKKB/FLIP)

#### NatureLM/PEER binarized stability — paper-specific protocol

Keep separate from TAPE's continuous stability regression. Do not silently change the paper's endpoint.

Published source size/units: NatureLM §7.2 uses classification. Exact label-conversion rule not resolved in this review.

**Protein stability classification:** Does the protein satisfy the paper's stable/unstable label definition? Metric: Accuracy. NatureLM §7.2 uses classification. Exact label-conversion rule not resolved in this review.

Keep separate from TAPE's continuous stability regression. Do not silently change the paper's endpoint.

[Source 1](https://arxiv.org/html/2502.07527v3), [Source 2](https://github.com/microsoft/SFM)

#### PFMBench production and enzyme-operating panel

These are PFMBench-specific processed datasets/splits, not interchangeable with PEER/ProtST results. F1 is not Fmax. Affinity-named AUROC tasks are classification, not KD regression. Exact loaders required.

Published source size/units: Test sizes: Optimal_pH: 959; DeepET_Topt: 185; Cloning_CLF: 2,778; Material_Production: 2,775; Enzyme_Eff.: 1,290; Antib._Res.: 339; Thermostability: 4,184

[Source 1](https://arxiv.org/html/2506.14796v1), [Source 2](https://github.com/biomap-research/PFMBench)

#### Which proteins bind each other

#### Human/Pan and yeast/Guo PPI — PEER

Separate human/yeast negatives and splits. Generic PPI, not Affibody–pMHC specificity.

Published source size/units: Published PEER test counts: human 227 pairs; yeast 373 pairs.

**Human protein–protein interaction prediction:** Do these two proteins interact under the dataset's interaction definition? Metric: Accuracy. Official human PEER PPI split; preserve negative construction.

Not TCR–pMHC specificity and not a measured dissociation constant.

**Yeast protein–protein interaction prediction:** Do these two proteins interact under the dataset's interaction definition? Metric: Accuracy. Official yeast PEER PPI split; preserve negative construction.

Not TCR–pMHC specificity and not a measured dissociation constant.

**Comparison qualification:** Native source outcome, data split and metric when separately verified; prompted zero-shot full-sequence Qwen baseline, not matched specialist training. No native BioT5 special-token architecture or fitted regression/classification head reproduced.

**Comparison qualification:** Native source outcome, data split and metric when separately verified; prompted zero-shot full-sequence Qwen baseline, not matched specialist training. No native BioT5 special-token architecture or fitted regression/classification head reproduced.

[Source 1](https://arxiv.org/html/2206.02096v2), [Source 2](https://arxiv.org/html/2402.17810v2), [Source 3](https://github.com/DeepGraphLearning/PEER_Benchmark)

#### ATOM3D interface contacts (PIP)

Residue-pair contact prediction is not sequence-pair binary PPI and not binding affinity.

Published source size/units: DIPS training and DB5 testing; exact processed test count not transcribed.

[Source 1](https://arxiv.org/html/2012.04035v3), [Source 2](https://www.atom3d.ai/pip.html)

#### PFMBench protein and metal-interaction panel

These are PFMBench-specific processed datasets/splits, not interchangeable with PEER/ProtST results. F1 is not Fmax. Affinity-named AUROC tasks are classification, not KD regression. Exact loaders required.

Published source size/units: Test sizes: Human_PPI: 195; Yeast_PPI: 335; PPI_Affinity: 326; MetalIonBinding: 718

[Source 1](https://arxiv.org/html/2506.14796v1), [Source 2](https://github.com/biomap-research/PFMBench)

#### Antibody properties

#### FLAb / FLAb2 antibody property collection

15 reference datasets are excluded from automated scoring; counts are corpus totals. Each assay has its own units, direction and split.

Published source size/units: Current repository: 241 datasets; >3 million assay points. Category counts 31/132/7/4/9/33/25 respectively (see details); not one held-out set.

[Source 1](https://github.com/Graylab/FLAb), [Source 2](https://github.com/Graylab/FLAb)

## What proteins do

#### Assigning protein functions and enzyme classes

#### DeepFRI-derived EC and GO test splits

Full-model supervised tuning. Keep ontology branches separate. This is annotation recovery, not verification of every rationale.

Published source size/units: ProtST's 95%-identity split setting. Exact processed test counts not recovered here.

**Enzyme Commission annotation:** What classes of chemical reaction does the enzyme catalyze? Metric: Micro-AP/AUPR; Fmax. ProtST uses the DeepFRI task split with a 95% sequence-identity cutoff.

Multilabel annotation recovery; incomplete annotation is not verified absence of an activity.

**Gene Ontology: biological process:** Which larger biological processes does the protein participate in? Metric: Micro-AP/AUPR; Fmax. Keep BP/MF/CC separate; ProtST's DeepFRI-derived split.

Not a free-form rationale score. GO label incompleteness and ontology propagation affect evaluation.

**Gene Ontology: molecular function:** What molecular activities does the protein perform? Metric: Micro-AP/AUPR; Fmax. Keep BP/MF/CC separate; ProtST's DeepFRI-derived split.

Not a free-form rationale score. GO label incompleteness and ontology propagation affect evaluation.

**Gene Ontology: cellular component:** Where does the protein act, or in which complex? Metric: Micro-AP/AUPR; Fmax. Keep BP/MF/CC separate; ProtST's DeepFRI-derived split.

Not a free-form rationale score. GO label incompleteness and ontology propagation affect evaluation.

[Source 1](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf), [Source 2](https://github.com/DeepGraphLearning/ProtST)

#### PFMBench GO/EC annotation panel

These are PFMBench-specific processed datasets/splits, not interchangeable with PEER/ProtST results. F1 is not Fmax. Affinity-named AUROC tasks are classification, not KD regression. Exact loaders required.

Published source size/units: Test sizes: GO-CC: 1,400; GO-MF: 2,787; GO-BP: 2,664; EC: 1,604

[Source 1](https://arxiv.org/html/2506.14796v1), [Source 2](https://github.com/biomap-research/PFMBench)

#### Protein function descriptions

#### Mol-Instructions — four protein-description subsets

NEW source result: these are Mol-Instructions' own numbers, NOT BioT5+. BioT5+'s Figure 2 reports its comparisons, but exact plotted values were not transcribed.

Published source size/units: Original Mol-Instructions paper: approximately 1,000 test examples per task; exact released counts not recomputed.

**Protein function description generation:** Which GO functions/processes/components describe this protein? Metric: ROUGE-L in BioT5+ protein-text experiments. Use the Mol-Instructions task-specific split; not one interchangeable pool of protein questions.

Text overlap can reward similar wording without validating every biological claim.

**Catalytic activity description generation:** What reaction does this protein catalyze? Metric: ROUGE-L in BioT5+ protein-text experiments. Use the Mol-Instructions task-specific split; not one interchangeable pool of protein questions.

Text overlap can reward similar wording without validating every biological claim.

**Protein domain and motif description generation:** Which domains or motifs are annotated for the protein? Metric: ROUGE-L in BioT5+ protein-text experiments. Use the Mol-Instructions task-specific split; not one interchangeable pool of protein questions.

Text overlap can reward similar wording without validating every biological claim.

**Protein functional description generation:** How would you summarize what this protein does? Metric: ROUGE-L in BioT5+ protein-text experiments. Use the Mol-Instructions task-specific split; not one interchangeable pool of protein questions.

Text overlap can reward similar wording without validating every biological claim.

**Comparison qualification:** Native Mol-Instructions gold-only ROUGE scorer algorithm on pinned BioT5+ task-defined test exports; full-sequence zero-shot Qwen is an explicit architecture/context/training adaptation. Pinned BioT5+ scorer passes [gold,decoded_input] pairs despite computing gold-only references_new: exact BioT5+ paper metric equivalence unresolved.

**Comparison qualification:** Native Mol-Instructions gold-only ROUGE scorer algorithm on pinned BioT5+ task-defined test exports; full-sequence zero-shot Qwen is an explicit architecture/context/training adaptation. Pinned BioT5+ scorer passes [gold,decoded_input] pairs despite computing gold-only references_new: exact BioT5+ paper metric equivalence unresolved.

**Comparison qualification:** Native Mol-Instructions gold-only ROUGE scorer algorithm on pinned BioT5+ task-defined test exports; full-sequence zero-shot Qwen is an explicit architecture/context/training adaptation. Pinned BioT5+ scorer passes [gold,decoded_input] pairs despite computing gold-only references_new: exact BioT5+ paper metric equivalence unresolved.

**Comparison qualification:** Native Mol-Instructions gold-only ROUGE scorer algorithm on pinned BioT5+ task-defined test exports; full-sequence zero-shot Qwen is an explicit architecture/context/training adaptation. Pinned BioT5+ scorer passes [gold,decoded_input] pairs despite computing gold-only references_new: exact BioT5+ paper metric equivalence unresolved.

[Source 1](https://arxiv.org/html/2306.08018v4), [Source 2](https://raw.githubusercontent.com/zjunlp/Mol-Instructions/main/README.md), [Source 3](https://arxiv.org/html/2402.17810v2), [Source 4](https://github.com/zjunlp/Mol-Instructions)

#### NatureLM's NCBI protein-description holdout

This is a paper-specific NCBI-derived set, not all NCBI data. Different task-training regimes; text-overlap evaluation.

Published source size/units: Temporal split; exact test count and frozen processed release not recovered.

**Protein description generation:** Can the model describe a protein whose annotation was withheld? Metric: ROUGE-L. Paper reports a temporal split; exact frozen test release/count not recovered.

Do not replace its temporal test with arbitrary UniProt rows and claim exact reproduction.

[Source 1](https://arxiv.org/html/2502.07527v3), [Source 2](https://github.com/microsoft/SFM)

#### Biochemical reaction classification

#### ProtST reaction classification — zero/few-shot

Zero-shot text-label matching is not the same protocol as fitting a fully supervised classifier.

Published source size/units: ProtST zero-shot/few-shot experiment; shots and ensemble settings must be recorded.

**Biochemical reaction classification:** Which of the specified reaction categories matches this protein? Metric: Accuracy. ProtST zero-shot/few-shot experiment; shots and ensemble settings must be recorded.

Zero-shot text-label matching is not the same protocol as fitting a fully supervised classifier.

**Comparison qualification:** Native released Reaction test and384-class top1 accuracy; prompted Qwen has different representation/context/pretraining from ProtST. Closest native full-description comparator21.91% accuracy, ProtST Table11 printedp15 (rounded); paper pretraining-name29.85% is a separate label-text variant. Native text embeddings truncate each description at128tokens; Qwen receives all complete descriptions jointly. Output-budget condition: MIXED_BUDGET_4K16K_CONTINUATION; 4419 historical cases retain4096 tokens and 1232 clean never-dispatched cases receive16384 tokens. Original invalid/truncated cases remain included. This is not a uniform16k evaluation or a matched budget comparison.

[Source 1](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf), [Source 2](https://github.com/DeepGraphLearning/ProtST)

#### Evidence support for protein explanations

#### BioReason-Pro explanation review

Judged explanation subset Correct GO labels do not guarantee that every intermediate statement is true.

Published source size/units: Are the generated functional explanations helpful and consistent with the reference evidence? Separate from the 8,630-protein GO-label metric; exact scored explanation subset not established here.

**Evidence support for protein-function explanations:** Are the generated functional explanations helpful and consistent with the reference evidence? Metric: Judge rubrics; qualitative/expert review. Separate from the 8,630-protein GO-label metric; exact scored explanation subset not established here.

Correct GO labels do not guarantee that every intermediate statement is true.

[Source 1](https://www.biorxiv.org/content/10.64898/2026.03.19.712954v2.full)

#### Protein retrieval from descriptions

#### ProtST text-to-protein retrieval examples

Retrieval case study Docking and known annotations support case analysis; they do not prove all retrieved candidates bind experimentally.

Published source size/units: Can a functional description retrieve relevant proteins? Selected queries such as heme binding; not a universal, fixed retrieval benchmark with one headline Recall@K.

**Protein retrieval from functional descriptions:** Can a functional description retrieve relevant proteins? Metric: Top-retrieval inspection; docking scores in case studies. Selected queries such as heme binding; not a universal, fixed retrieval benchmark with one headline Recall@K.

Docking and known annotations support case analysis; they do not prove all retrieved candidates bind experimentally.

[Source 1](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf)

## Effects of protein mutations

#### Explaining mutation effects

#### MutaDescribe — mutation explanation

The reported 'Average' is retained as the paper defines it. Similarity tiers are not a globally homology-disjoint split.

Published source size/units: Main test: Easy 460; Medium 384; Hard 404 mutation examples. Separate temporal test: 1,611 (not the reported main averages).

**Mutation-effect explanation:** What effect does this amino-acid change have? Metric: BLEU-2; ROUGE-L; GPT-4-plus-human categorical review. Random split then similarity tiers: Easy 460, Medium 384, Hard 404. Separate temporal test has 1,611 examples.

Similarity tiers do not make the entire split homology-disjoint. Judge output is not independent experimental verification.

[Source 1](https://arxiv.org/html/2410.22949v1), [Source 2](https://huggingface.co/datasets/PharMolix/MutaDescribe)

#### Predicting and ranking mutation effects

#### ProteinGym substitutions — historical ProtST evaluation

NEW verified numeric row from ProtST Table 12. Not a current ProteinGym leaderboard result.

Published source size/units: Use the historical ProteinGym snapshot in ProtST. Do not attach the modern 217-assay count to these old results.

**Mutation-effect ranking:** Do model scores rank variants in the same order as the experiments? Metric: Spearman primary; suite also reports ranking/classification summaries. Pin release: modern v1.3 substitution subset has 217 assays; an older paper may use an earlier snapshot.

Score within each assay. Different assay scores are not a shared physical unit; fitness is not always binding.

[Source 1](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf), [Source 2](https://github.com/OATML-Markslab/ProteinGym), [Source 3](https://github.com/OATML-Markslab/ProteinGym)

#### PG-LLM / ProteinGym-LLM — eval-data-v1.2

Evaluation-only frozen protocol. Benchmark-specific training, tuning and retrieval augmentation are restricted by its documentation.

Published source size/units: 217 assays; sets of 10, 50 or 100 variants; three seeds.

**Mutation-effect ranking:** Can a language model rank a supplied set of variant sequences by assay performance? Metric: Per-assay Spearman. eval-data-v1.2: 217 assays; N=10/50/100; seeds 1/2/3; labels separate from model-facing inputs.

Evaluation-only: do not train, tune prompts, distill or perform retrieval augmentation using these candidate sets/labels.

[Source 1](https://raw.githubusercontent.com/rohitarorayyc/proteingym-llm/main/DATA.md), [Source 2](https://github.com/rohitarorayyc/proteingym-llm/blob/main/DATA.md)

#### PFArena — four task settings

Different assay subsets, not a paired context ablation. Reported aggregates include deterministic random fallback on missing outputs (§10.1/Table 12). Model labels are the paper's, not verified API IDs. Exact public bundle not yet established; retained paper model labels are not executable API identifiers.

Published source size/units: T1: 123 assays / 594,695 measured singles. T2: 74 assays / 6,288 candidates. T3: 67 assays / 3,648 candidates. T4: 29 assays / 2,638 candidates.

**Single-mutant generation:** Which single substitutions should be proposed? Metric: Recall@40; normalized maximum recovered score. 123 assays; budget 40; 594,695 measured single mutants in the reported source universe

The tasks differ in permitted evidence. 'Anchor' is a tested mutant, not an HLA anchor residue. Assay sets overlap.

**Multi-mutant ranking without measurements:** Which supplied combinations should rank highest without measurements? Metric: Spearman; NDCG; normalized max@K; Recall@K. 74 assays; 6,288 candidates

The tasks differ in permitted evidence. 'Anchor' is a tested mutant, not an HLA anchor residue. Assay sets overlap.

**Mutation ranking with anchor measurements:** Which additions to an already tested mutant are promising? Metric: Spearman; NDCG; normalized max@K; Recall@K. 67 assays; 3,648 candidates

The tasks differ in permitted evidence. 'Anchor' is a tested mutant, not an HLA anchor residue. Assay sets overlap.

**Mutation ranking with single-mutant measurements:** Can measurements of individual changes help rank their combinations? Metric: Spearman; NDCG; normalized max@K; Recall@K. 29 assays; 2,638 candidates; 28,609 single-mutant context records

The tasks differ in permitted evidence. 'Anchor' is a tested mutant, not an HLA anchor residue. Assay sets overlap.

[Source 1](https://arxiv.org/html/2609.28921v1), [Source 2](https://arxiv.org/html/2609.28921v1)

#### MutaPLM low-data fitness regression

This is supervised low-N prediction, not zero-shot generation. Do not reuse the labeled seed points as test examples.

Published source size/units: 192 training + 48 validation examples; five seeds; assay-specific remaining test records

**Low-data fitness regression:** With a small labeled sample, can features predict held-out assay outcomes? Metric: Spearman. 192 training and 48 validation samples; five random seeds. Remaining held-out data evaluated per source.

This is supervised low-N prediction, not zero-shot generation. Do not reuse the labeled seed points as test examples.

[Source 1](https://arxiv.org/html/2410.22949v1), [Source 2](https://github.com/PharMolix/MutaPLM)

#### PFMBench mutation/fitness panel

These are PFMBench-specific processed datasets/splits, not interchangeable with PEER/ProtST results. F1 is not Fmax. Affinity-named AUROC tasks are classification, not KD regression. Exact loaders required.

Published source size/units: Test sizes: PETA_CHS_SOL: 484; PETA_LGK_SOL: 1,914; PETA_TEM_SOL: 808; FLIP_AAV: 16,517; FLIP_GB1: 1,745; TAPE_Stab: 6,898; TAPE_Fluor: 27,217; BetaLactamase: 520

[Source 1](https://arxiv.org/html/2506.14796v1), [Source 2](https://github.com/biomap-research/PFMBench)

#### PFMBench ProteinGym zero-shot protocol

These are PFMBench-specific processed datasets/splits, not interchangeable with PEER/ProtST results. F1 is not Fmax. Affinity-named AUROC tasks are classification, not KD regression. Exact loaders required.

Published source size/units: Paper table does not specify the release-matched evaluation denominator.

[Source 1](https://arxiv.org/html/2506.14796v1), [Source 2](https://github.com/biomap-research/PFMBench)

#### Choosing mutations to improve a protein

#### MutaDescribe — mutation engineering

Same source dataset, different task. These are reference-recovery rates, not prospective wet-lab success.

Published source size/units: Same main Easy/Medium/Hard split as explanation: 460 / 384 / 404 examples.

**Mutation engineering with a supplied position:** Given a desired effect and a specified position, which residue should replace the original? Metric: Accuracy. Same similarity/temporal splits as MutaDescribe; supplied position simplifies the task.

Recovery of one annotated mutation is not the fraction of novel designs that work.

**Mutation engineering with an unknown position:** Which 50 single substitutions best fit the requested effect? Metric: Recall@50. Search covers 19 × sequence-length substitutions; preserve the paper's candidate definition.

A different useful but unannotated mutation can score as a miss.

[Source 1](https://arxiv.org/html/2410.22949v1), [Source 2](https://huggingface.co/datasets/PharMolix/MutaDescribe)

#### MutaPLM iterative optimization

Predictor-scored search experiment A learned scorer can be exploited; this experiment is not prospective laboratory success.

Published source size/units: Do iterative proposals improve the predicted assay objective? Six landscapes: AAV, AMIE, avGFP, E4B, LGK, UBE2I; 20 independent runs; preserve beam/search settings.

**Protein-sequence optimization against fitness predictors:** Do iterative proposals improve the predicted assay objective? Metric: Mean predicted fitness trajectory and dispersion. Six landscapes: AAV, AMIE, avGFP, E4B, LGK, UBE2I; 20 independent runs; preserve beam/search settings.

A learned scorer can be exploited; this experiment is not prospective laboratory success.

[Source 1](https://arxiv.org/html/2410.22949v1)

#### Binding affinity and immune interactions

#### AbBiBench antibody affinity ranking

Paper size and current leaderboard refer to different snapshots. Do not combine them into a single size-matched result. Generative case study is separate.

Published source size/units: Paper: 155,853 heavy-chain variants, 9 antigens (Section 3.1 lists 11 datasets). Current repository leaderboard: 16 assay columns; expanded payload count not established.

[Source 1](https://github.com/MSBMI-SAFE/AbBiBench), [Source 2](https://arxiv.org/html/2506.04235v1), [Source 3](https://huggingface.co/datasets/AbBibench/Antibody_Binding_Benchmark_Dataset)

#### ATOM3D SKEMPI-derived mutation affinity (MSP)

This is binding-affinity change classification, not folding-stability prediction. Source counts are not test counts.

Published source size/units: Source construction: 893 positive and 3,255 negative mutations; exact test size not recovered.

[Source 1](https://arxiv.org/html/2012.04035v3), [Source 2](https://www.atom3d.ai/msp.html)

#### PFMBench peptide–MHC and TCR–pMHC panel

These are PFMBench-specific processed datasets/splits, not interchangeable with PEER/ProtST results. F1 is not Fmax. Affinity-named AUROC tasks are classification, not KD regression. Exact loaders required.

Published source size/units: Test sizes: Pept.HLA/MHC Aff.: 8,406; TCR.PMHC Aff.: 2,482

[Source 1](https://arxiv.org/html/2506.14796v1), [Source 2](https://github.com/biomap-research/PFMBench)

## Answering biology research questions

#### Biological research question answering

#### LAB-Bench — research tasks

Original full public+private test; not the public 1,967-question subset. Three-run means. Tool-free models; TableQA and FigQA are images. No new category aggregate invented.

Published source size/units: Original full evaluation: 2,457 questions. LitQA2 248; SuppQA 102; FigQA 226; TableQA 305; DbQA 650; ProtocolQA 135; SeqQA 750; Cloning 41.

**Literature evidence question answering:** Can the model answer a question whose answer is in the scientific literature? Metric: Accuracy; selective precision and coverage when abstention is enabled. Public subset commonly 1,967 questions across eight categories; original full set and private portion differ. Pin dataset revision.

Keep resource access fixed. Original model evaluation was tool-free, unlike human baseline. MCQ success can partly reflect distractor elimination.

**Biological database question answering:** Can the model recover the correct fact from a biological database? Metric: Accuracy; selective precision and coverage when abstention is enabled. Public subset commonly 1,967 questions across eight categories; original full set and private portion differ. Pin dataset revision.

Keep resource access fixed. Original model evaluation was tool-free, unlike human baseline. MCQ success can partly reflect distractor elimination.

**Supplementary-material question answering:** Can the model locate information in a paper's supplementary material? Metric: Accuracy; selective precision and coverage when abstention is enabled. Public subset commonly 1,967 questions across eight categories; original full set and private portion differ. Pin dataset revision.

Keep resource access fixed. Original model evaluation was tool-free, unlike human baseline. MCQ success can partly reflect distractor elimination.

**Research figure question answering:** Can the model interpret a scientific figure? Metric: Accuracy; selective precision and coverage when abstention is enabled. Public subset commonly 1,967 questions across eight categories; original full set and private portion differ. Pin dataset revision.

Keep resource access fixed. Original model evaluation was tool-free, unlike human baseline. MCQ success can partly reflect distractor elimination.

**Research table question answering:** Can the model read and reason about a scientific table? Metric: Accuracy; selective precision and coverage when abstention is enabled. Public subset commonly 1,967 questions across eight categories; original full set and private portion differ. Pin dataset revision.

Keep resource access fixed. Original model evaluation was tool-free, unlike human baseline. MCQ success can partly reflect distractor elimination.

**Experimental protocol question answering:** Can the model identify problems or implications in an experimental procedure? Metric: Accuracy; selective precision and coverage when abstention is enabled. Public subset commonly 1,967 questions across eight categories; original full set and private portion differ. Pin dataset revision.

Keep resource access fixed. Original model evaluation was tool-free, unlike human baseline. MCQ success can partly reflect distractor elimination.

**Biological sequence question answering:** Can the model carry out the requested operation on the supplied sequence? Metric: Accuracy; selective precision and coverage when abstention is enabled. Public subset commonly 1,967 questions across eight categories; original full set and private portion differ. Pin dataset revision.

Keep resource access fixed. Original model evaluation was tool-free, unlike human baseline. MCQ success can partly reflect distractor elimination.

**Molecular cloning question answering:** Can the model solve the sequence-constraint problem in a cloning scenario? Metric: Accuracy; selective precision and coverage when abstention is enabled. Public subset commonly 1,967 questions across eight categories; original full set and private portion differ. Pin dataset revision.

Keep resource access fixed. Original model evaluation was tool-free, unlike human baseline. MCQ success can partly reflect distractor elimination.

**Comparison qualification:** Native public questions, COT prompt, shuffle algorithm and deterministic parser/metrics. Two cases held; one seeded Qwen run, not the original three-run mean or full private/public set. No model-based answer-extraction fallback.

**Comparison qualification:** Native public prompts, choices, required context/images and metrics. Reviewed public release; one fixed-seed run, not the original full public/private three-run paper mean. Strict deterministic parser; no model extraction fallback.

**Comparison qualification:** Native public prompts, choices, required context/images and metrics. Reviewed public release; one fixed-seed run, not the original full public/private three-run paper mean. Strict deterministic parser; no model extraction fallback.

**Comparison qualification:** Native public prompts, choices, required context/images and metrics. Reviewed public release; one fixed-seed run, not the original full public/private three-run paper mean. Strict deterministic parser; no model extraction fallback.

**Comparison qualification:** Native public prompts, choices, required context/images and metrics. Reviewed public release; one fixed-seed run, not the original full public/private three-run paper mean. Strict deterministic parser; no model extraction fallback.

**Comparison qualification:** Native public prompts, choices, required context/images and metrics. Reviewed public release; one fixed-seed run, not the original full public/private three-run paper mean. Strict deterministic parser; no model extraction fallback.

**Comparison qualification:** Native public prompts, choices, required context/images and metrics. Reviewed public release; one fixed-seed run, not the original full public/private three-run paper mean. Strict deterministic parser; no model extraction fallback.

[Source 1](https://arxiv.org/html/2407.10362v1), [Source 2](https://huggingface.co/datasets/futurehouse/lab-bench)

#### ProteinLMBench protein-understanding questions

Knowledge/test-taking evaluation, not direct novel protein-function prediction.

Published source size/units: 944 manually verified questions; six choices per question.

[Source 1](https://arxiv.org/html/2406.05540v1), [Source 2](https://huggingface.co/datasets/tsynbio/ProteinLMBench)

#### PubMedQA research-abstract questions

The conclusion/long answer must stay out of solver input under the reasoning-required protocol.

Published source size/units: 1,000 expert-labeled records total; official evaluation split must be pinned. 61.2K unlabeled and 211.3K artificial records are separate training resources.

[Source 1](https://arxiv.org/abs/1909.06146), [Source 2](https://github.com/pubmedqa/pubmedqa)

## Designing proteins

#### Protein sequence and structure generation

#### ProteinBench unconditional backbone generation

Reported values retained on the paper's scale; structural plausibility does not establish function.

Published source size/units: Length-stratified generation at 100/200/300/400/500 aa; 100 single-chain reference structures. Exact generated count must follow the release.

[Source 1](https://arxiv.org/html/2409.06744v2), [Source 2](https://proteinbench.github.io/)

#### ProteinBench unconditional sequence generation

pLDDT is confidence, not experimentally measured protein stability or function.

Published source size/units: 50 sequences per model at each length 100, 200, 300 and 500.

[Source 1](https://arxiv.org/html/2409.06744v2), [Source 2](https://proteinbench.github.io/)

#### ProteinBench joint sequence–structure generation

These are selected length-specific results, not one design success rate.

Published source size/units: Length-stratified generated samples; exact per-setting candidate count not recovered.

[Source 1](https://arxiv.org/html/2409.06744v2), [Source 2](https://proteinbench.github.io/)

#### BioT5+ description-guided protein generation

Qualitative design case A plausible or similar sequence is not a measured successful design.

Published source size/units: Can the model propose a sequence matching a description? The paper does not define a generally established benchmark for this task.

**Text-conditioned protein-sequence design:** Can the model propose a sequence matching a description? Metric: Qualitative cases and sequence/reference comparisons. The paper does not define a generally established benchmark for this task.

A plausible or similar sequence is not a measured successful design.

[Source 1](https://arxiv.org/html/2402.17810v2)

#### NatureLM generated proteins: unconditional / property-conditioned / heme

Predictor-scored or qualitative design Diversity and predicted structure confidence do not establish function. | Predictor agreement, not experimentally measured stability/solubility of each generated sequence. | Self-description is not independent validation; predicted complexes are not measured binding.

Published source size/units: Does the model generate varied, structurally plausible protein sequences? / Do sequences requested to have a property score well under the evaluator? / Can conditioning suggest proteins plausibly associated with heme? Generated samples compared with natural sequences; not a labeled holdout prediction set. | Paper uses a natural UR50 reference subset of 1,000 sequences in the conditioned comparison. | Selected candidates; no standard released labeled test-set size.

**Unconditional protein generation:** Does the model generate varied, structurally plausible protein sequences? Metric: Length distribution; clustering-based diversity; pLDDT. Generated samples compared with natural sequences; not a labeled holdout prediction set.

Diversity and predicted structure confidence do not establish function.

**Protein generation for predicted stability and solubility:** Do sequences requested to have a property score well under the evaluator? Metric: Predicted property scores; diversity. Paper uses a natural UR50 reference subset of 1,000 sequences in the conditioned comparison.

Predictor agreement, not experimentally measured stability/solubility of each generated sequence.

**Heme-binding protein candidate generation:** Can conditioning suggest proteins plausibly associated with heme? Metric: Qualitative description/complex screening. Selected candidates; no standard released labeled test-set size.

Self-description is not independent validation; predicted complexes are not measured binding.

[Source 1](https://arxiv.org/html/2502.07527v3)

#### Making fluorescent proteins brighter

#### STRIDE GFP sequence optimization

Predictor-scored generation These 100 candidates are not a wet-lab test set. Correctly applying edits does not validate fluorescence.

Published source size/units: Do proposed edits improve the fixed scorer's predicted fluorescence? 100 candidates per method from a common source; separate replace-only and full-edit settings.

**GFP sequence optimization against a fluorescence predictor:** Do proposed edits improve the fixed scorer's predicted fluorescence? Metric: Predicted improvement/success; uniqueness; novelty. 100 candidates per method from a common source; separate replace-only and full-edit settings.

These 100 candidates are not a wet-lab test set. Correctly applying edits does not validate fluorescence.

[Source 1](https://arxiv.org/html/2603.03573v1)

#### Antibody design

#### RAbD — CDR-H3 redesign

Geometry and native-sequence recovery disagree; no dominance claim across all metrics. Not prospective binding success. ProteinBench's 55-complex processed version is separately listed.

Published source size/units: 60 antibody–antigen complexes.

**Antibody design: CDR-H3 redesign:** Can the model reconstruct/design an antibody loop in a fixed antigen/framework context? Metric: NatureLM: AAR. Proteo-R1: AAR, RMSD, lDDT, TM-score, DockQ.. 60 complexes; retain paper-specific renumbering, masked region and preprocessing.

High native recovery or geometric similarity does not imply measured binding for a new design.

[Source 1](https://arxiv.org/html/2605.02937v1), [Source 2](https://arxiv.org/html/2605.02937v1)

#### SAbDab — Proteo-R1 all-CDR holdout

One dataset, multiple metrics. H3 RMSD and Loop-RMSD are different columns. Oracle-Anchor row is not the deployed system.

Published source size/units: Paper-specific temporal/cluster split; exact processed test count not recovered.

**Antibody design: multi-CDR redesign:** Can all designated antibody loops be redesigned consistently with the complex? Metric: Structural/recovery/interface metrics; Rosetta-derived energy and clash diagnostics. Release-time filtering and 50%-identity H3 clusters; 9:0.5:0.5 cluster split. Exact test count not established.

Computational reconstruction/design. The original docking pose is assumed known; not unconstrained binder discovery.

[Source 1](https://arxiv.org/html/2605.02937v1), [Source 2](https://arxiv.org/html/2605.02937v1)

#### ProteinBench antibody design — processed RAbD

Same parent resource does not mean identical split or scorer. This is a distinct protocol, not 55 additional independent complexes.

Published source size/units: 55 retained RAbD complexes; differs from the 60-complex protocol in the earlier catalog.

[Source 1](https://arxiv.org/html/2409.06744v2), [Source 2](https://proteinbench.github.io/)

#### CHIMERA-Bench epitope-conditioned antibody design

EpiF1 measures intended-site contact, not empirical selectivity across off-target molecules.

Published source size/units: 2,922 complexes total. Test: 292 epitope-group; 292 antigen-fold; 293 temporal. Splits are alternatives, not additive test sets.

[Source 1](https://arxiv.org/html/2603.13431v1), [Source 2](https://github.com/mansoor181/chimera-bench)

#### Finding a sequence for a desired shape

#### CATH 4.2 / TS50 / TS500 inverse folding

Recovery is not experimental fold/function validation; named size does not replace retained-record manifest.

Published source size/units: CATH 4.2 exact test count not re-established; TS50/TS500 named test suites (50/500 nominal structures; exact retained manifests must be checked).

[Source 1](https://github.com/a4bio/pifold), [Source 2](https://github.com/a4bio/pifold)

#### ProteinBench inverse folding — CASP15 / CAMEO / synthetic backbones

Some models are excluded from native recovery because of training exposure. Synthetic consistency is model-scored, not wet-lab.

Published source size/units: 32 CASP15 structures; 332 CAMEO complexes; synthetic backbones: 10 at each of 5 lengths (100–500 aa).

[Source 1](https://arxiv.org/html/2409.06744v2), [Source 2](https://proteinbench.github.io/)

#### Building around a functional protein part

#### MotifBench functional-motif scaffolding

Score is not percentage of experimentally functional proteins. Preserve sampling and evaluator versions.

Published source size/units: 30 motif problems; standard submission 100 scaffolds per problem.

[Source 1](https://github.com/blt2114/MotifBench), [Source 2](https://github.com/blt2114/MotifBench)

#### ProteinBench motif scaffolding — legacy motif panel

Do not merge the legacy panel with MotifBench or reuse their scores interchangeably.

Published source size/units: Legacy 17 (25) motif-problem panel described by ProteinBench; not MotifBench's separate 30-problem set.

[Source 1](https://arxiv.org/html/2409.06744v2), [Source 2](https://proteinbench.github.io/)

#### Designing proteins that bind a target

#### ProtDBench de novo target-binder design

Counts of computational passes, not wet-lab hit fractions. Exact target-specific conditions and verifier must match.

Published source size/units: 10 target proteins; 24 h on one A100 per method/target setting. Includes generation, inverse folding and scoring.

[Source 1](https://arxiv.org/html/2605.04118v1), [Source 2](https://arxiv.org/html/2605.04118v1)

#### Prompteina text-conditioned protein design — GM2A campaign

Prospective experimental campaign A single target campaign, not a general fixed test set or aggregate success rate. 52.4M captions is a training size.

Published source size/units: Generate target binders from language specifications; measure selected designs prospectively. 1,000-design computational budget; 90 selected; 89 expressed and assayed.

[Source 1](https://arxiv.org/html/2610.13917v1)

## Protein shapes and motion

#### Local structure and residue prediction

#### ATOM3D residue identity from local structure (RES)

Environment count is not protein count. This is an established held-out structure task, unlike unverified internal diagnostics.

Published source size/units: Test: 3,319 PDB structures yielding 1,261,342 local environments; train: 21,147 structures.

[Source 1](https://arxiv.org/html/2012.04035v3), [Source 2](https://www.atom3d.ai/)

#### PFMBench structure-derived prediction panel

These are PFMBench-specific processed datasets/splits, not interchangeable with PEER/ProtST results. F1 is not Fmax. Affinity-named AUROC tasks are classification, not KD regression. Exact loaders required.

Published source size/units: Test sizes: Contact: 1,501; FoldClass: 1,630; SecondaryStructure: 8,262

[Source 1](https://arxiv.org/html/2506.14796v1), [Source 2](https://github.com/biomap-research/PFMBench)

#### Structure-derived questions and output checks

#### Proteo-R1 internal alignment / structural / CDR diagnostics

Internal diagnostic — holdout unresolved Not a named released PDB benchmark. Eight-response averages are not pass@8. No evidence of leakage is inferred from missing documentation.

Published source size/units: Check training-stage behavior on calculated structural questions and output-schema tasks. Independent held-out question manifest and size unresolved; 9.09M is Stage-II TRAINING instances.

[Source 1](https://arxiv.org/html/2605.02937v1)

#### Protein structure ranking

#### ATOM3D protein structure ranking (PSR)

Ranking a supplied set of structures is not de novo structure generation.

Published source size/units: CASP-derived target/decoy split; exact processed test-target/decoy counts not transcribed.

[Source 1](https://arxiv.org/html/2012.04035v3), [Source 2](https://www.atom3d.ai/)

#### Protein folding

#### ProteinBench single-state folding — CAMEO 2022

Models may have different MSA/template access. This is a historical target cohort, not the live CAMEO leaderboard.

Published source size/units: 183 proteins (<750 residues), released Aug–Oct 2022.

[Source 1](https://arxiv.org/html/2409.06744v2), [Source 2](https://proteinbench.github.io/)

#### Protein shape changes, motion and stability

#### ProteinBench multistate conformations — apo/holo and BPTI

Sample count is not the number of independent test proteins; BPTI alone gives narrow generalization evidence.

Published source size/units: Apo/holo: 91 protein pairs, 20 generated conformations per protein. BPTI: one 58-residue protein, 5 MD clusters, N=10/100/1000 samples.

[Source 1](https://arxiv.org/html/2409.06744v2), [Source 2](https://proteinbench.github.io/)

#### ProteinBench ensemble distribution — ATLAS

MD reference is simulation-derived, not an exhaustive experimental distribution. Preserve alignment, projection and aggregation.

Published source size/units: 82 held-out proteins; 250 generated conformations per protein.

[Source 1](https://arxiv.org/html/2409.06744v2), [Source 2](https://proteinbench.github.io/)

#### BioEmu benchmark collection — states, dynamics and free energy

Pin benchmark/model revision: version changes affect values. Panel scores are not one pooled success rate.

Published source size/units: Multiple panels: domain motion, local unfolding, cryptic pockets, MD emulation and experimental folding free energies. Exact panel sizes not re-counted.

[Source 1](https://github.com/microsoft/bioemu/blob/main/MODEL_CARD.md), [Source 2](https://github.com/microsoft/bioemu-benchmarks)

## Understanding biomedical images

#### Biomedical visual question answering

#### Biomedical VQA: VQA-RAD / SLAKE-English / PathVQA / VQA-Med 2019

Medical-image performance does not show use of protein sequence/structure embeddings. Open-answer scorers differ between papers. | Medical-image performance does not show use of protein sequence/structure embeddings. Open-answer scorers differ between papers. | Medical-image performance does not show use of protein sequence/structure embeddings. Open-answer scorers differ between papers. | Medical-image performance does not show use of protein sequence/structure embeddings. Open-answer scorers differ between papers.

Published source size/units: Distinct official task splits; exact test counts not re-established. Open/closed answer groups must remain separate.

**Radiology image question answering:** Can the model answer a question using the supplied medical image? Metric: Closed-question accuracy; open scoring is paper-specific (e.g. token recall in original LLaVA-Med). Use task's official train/test split; do not use total corpus size as test size.

Medical-image performance does not show use of protein sequence/structure embeddings. Open-answer scorers differ between papers.

**Medical image question answering in English:** Can the model answer a question using the supplied medical image? Metric: Closed-question accuracy; open scoring is paper-specific (e.g. token recall in original LLaVA-Med). English subset; exact partition and normalization must match the target paper.

Medical-image performance does not show use of protein sequence/structure embeddings. Open-answer scorers differ between papers.

**Pathology image question answering:** Can the model answer a question using the supplied medical image? Metric: Closed-question accuracy; open scoring is paper-specific (e.g. token recall in original LLaVA-Med). Official split; keep closed/open question groups separate.

Medical-image performance does not show use of protein sequence/structure embeddings. Open-answer scorers differ between papers.

**Medical image question answering:** Can the model answer a question using the supplied medical image? Metric: Closed-question accuracy; open scoring is paper-specific (e.g. token recall in original LLaVA-Med). The 2019 challenge snapshot, not an arbitrary later VQA-Med release.

Medical-image performance does not show use of protein sequence/structure embeddings. Open-answer scorers differ between papers.

**Comparison qualification:** Original native test split/images/questions and pinned LLaVA-Medv1 normalization/scoring; Qwen is a declared zero-shot vision baseline with its own chat template/generation and no downstream tuning. Compare OPEN recall and CLOSED accuracy separately; full-test claim requires complete native inputs and outputs.

**Comparison qualification:** Original native test split/images/questions and pinned LLaVA-Medv1 normalization/scoring; Qwen is a declared zero-shot vision baseline with its own chat template/generation and no downstream tuning. Compare OPEN recall and CLOSED accuracy separately; full-test claim requires complete native inputs and outputs.

**Comparison qualification:** Full pinned6719-row mirror test (original6761 minus42 duplicate rows, plus documented text normalization), full released image bytes and question strings. Original per-image byte identity is not fully established. Qwen zero-shot vision/training/generation differs from task-trained papers. Compare only declared metric and split-compatible results; no exact paper replication claim.

**Comparison qualification:** Same original500 test IDs/images/questions; zero-shot Qwen and explicit fixed scorer reconstruction, not target-fine-tuned MedVInT or a claim of byte-identical challenge scoring. Historical strict-accuracy executable not recovered; normalization/reference syntax reconstructed prospectively from organizers. Native2019BLEU withheld rather than substitute another year or arbitrary metric. No claim of matched target fine-tuning or closed/open metric equivalence.

[Source 1](https://arxiv.org/abs/2306.00890), [Source 2](https://arxiv.org/html/2305.10415v6), [Source 3](https://arxiv.org/abs/2306.00890), [Source 4](https://arxiv.org/html/2305.10415v6), [Source 5](https://github.com/microsoft/LLaVA-Med), [Source 6](https://github.com/xiaoman-zhang/PMC-VQA)

#### Scientific figures, documents and visual conversations

#### PMC-VQA figure question answering

Specify initial versus cleaned test set. Caption-derived labels need not be visually answerable without filtering.

Published source size/units: Reviewed v6: 50,000 initial test examples; 2,000 manually reviewed clean test examples.

**Scientific figure question answering:** Can the model answer a question from a biomedical paper figure? Metric: MCQ accuracy; paper's open/blank-answer accuracy and BLEU. v6: 50,000 initial image-disjoint test examples; 2,000 manually reviewed clean test examples. Older site names differ.

Specify initial versus cleaned test set. Caption-derived labels need not be visually answerable without filtering.

**Comparison qualification:** Fixed local zero-shot Qwen vision baseline on complete native clean2000 set and source TD question/choice strings. Qwen chat, image preprocessing, free generation and training differ from MedVInT. Match metric/output extraction and clean split before comparing; full-text metric is adapted, TE systems are not exact reproductions. Public pretraining exposure unknown.

[Source 1](https://arxiv.org/html/2305.10415v6), [Source 2](https://github.com/xiaoman-zhang/PMC-VQA)

#### LLaVA-Med biomedical visual conversations

Teacher reference has textual context that the image may not reveal. Judgment is not direct clinician-verified molecular truth.

Published source size/units: Published 50-image conversation-evaluation setting; teacher-generated text references.

**Biomedical visual conversations:** Can the model give useful biomedical explanations of a supplied image? Metric: GPT-assisted relative response assessment. Released qa50 evaluation files; 50-image setting. Use original/v1.5 code and model version consistently.

Teacher reference has textual context that the image may not reveal. Judgment is not direct clinician-verified molecular truth.

[Source 1](https://arxiv.org/abs/2306.00890), [Source 2](https://github.com/microsoft/LLaVA-Med)

#### Ryze document-extraction component tests

Component ablation These tests evaluate extraction/document understanding, not protein engineering.

Published source size/units: Does document/figure extraction preserve information needed for answering questions? Auxiliary component evaluation, separate from final LAB-Bench scores.

**Scientific document and figure extraction:** Does document/figure extraction preserve information needed for answering questions? Metric: Dataset-specific QA accuracy. Auxiliary component evaluation, separate from final LAB-Bench scores.

These tests evaluate extraction/document understanding, not protein engineering.

[Source 1](https://arxiv.org/html/2606.00902v1)

## DNA, RNA and small molecules

#### Molecular interactions and binding affinity

#### Drug–target interaction: BioSNAP / Human / BindingDB

Secondary to the protein focus. Not protein–protein recognition or Affibody–pMHC evaluation.

Published source size/units: Three source benchmarks; preserve each split/negative/threshold rule.

**Drug–target interaction:** Does a small molecule interact with a protein target? Metric: AUROC in BioT5+ comparisons. Three source benchmarks; preserve each split/negative/threshold rule.

Secondary to the protein focus. Not protein–protein recognition or Affibody–pMHC evaluation.

**Comparison qualification:** Original released dataset and standard AUROC/AP; fixed first-token Qwen likelihood adapter differs from trained DrugBAN/BioT5 architectures and BioT5 raw-score ratio. No test threshold fitting or exact paper reproduction claim.

**Comparison qualification:** Original released dataset and standard AUROC/AP; fixed first-token Qwen likelihood adapter differs from trained DrugBAN/BioT5 architectures and BioT5 raw-score ratio. No test threshold fitting or exact paper reproduction claim.

**Comparison qualification:** Original released dataset and standard AUROC/AP; fixed first-token Qwen likelihood adapter differs from trained DrugBAN/BioT5 architectures and BioT5 raw-score ratio. No test threshold fitting or exact paper reproduction claim.

[Source 1](https://arxiv.org/html/2402.17810v2), [Source 2](https://github.com/QizhiPei/BioT5)

#### ATOM3D protein–ligand affinity (LBA)

Target transformation and split must match. Not antibody–antigen affinity.

Published source size/units: 30%-identity split: train 3,507, validation 466, test 490 complexes. The 60% split is a different protocol.

[Source 1](https://arxiv.org/html/2012.04035v3), [Source 2](https://www.atom3d.ai/)

#### ATOM3D ligand efficacy (LEP)

Activity/efficacy is distinct from affinity. Source molecule count is not a test denominator.

Published source size/units: 527 source small molecules; final retained train/test counts not transcribed.

[Source 1](https://arxiv.org/html/2012.04035v3), [Source 2](https://www.atom3d.ai/lep.html)

#### PFMBench PDBbind / BindingDB affinity panel

These are PFMBench-specific processed datasets/splits, not interchangeable with PEER/ProtST results. F1 is not Fmax. Affinity-named AUROC tasks are classification, not KD regression. Exact loaders required.

Published source size/units: Test sizes: PDBBind: 1,836; BindingDB: 1,139

[Source 1](https://arxiv.org/html/2506.14796v1), [Source 2](https://github.com/biomap-research/PFMBench)

#### RNA structure ranking

#### ATOM3D RNA structure ranking (RSR)

RNA task retained as adjacent scope, not a protein benchmark.

Published source size/units: RNA-Puzzles 1–21; test puzzles 18–21, with decoys per target. Exact retained test-decoy count not re-counted.

[Source 1](https://arxiv.org/html/2012.04035v3), [Source 2](https://www.atom3d.ai/rsr.html)

#### Small-molecule properties

#### ATOM3D small-molecule properties (SMP / QM9)

Adjacency only; not protein biology. Units depend on property.

Published source size/units: Processed test 12,943 molecules (train 103,547; validation 12,943).

[Source 1](https://arxiv.org/html/2012.04035v3), [Source 2](https://www.atom3d.ai/)

</details>

Result references updated: **2026-10-18 21:00 PDT**. Display times use Pacific time (PST/PDT).
