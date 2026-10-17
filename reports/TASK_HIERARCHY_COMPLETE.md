# Complete biological evaluation hierarchy

[Overview](EVALUATION_OVERVIEW.md) · [Grouped results](RESULTS_GROUPED.md) · [Coverage crosswalk](TASK_COVERAGE_MAP.csv)

All **67 main dataset/protocol groups** and **9 case/diagnostic groups** are retained. Hierarchy: **capability → scientific task → dataset/protocol → scope and execution**. Registry identifiers appear in the crosswalk and provenance JSON rather than human task names.

Stored scores: **2026-10-16 06:49 PDT**. Running-work snapshot: **2026-10-17 10:25 PDT**. Display times use Pacific time.

**\*** marks an incomplete group or setting. Registered scope and current execution status are separate; catalog presence does not imply authorization. Mixed groups show each registered protocol separately. Status unverified is not a claim that a task was never run.

## Protein properties, interactions and developability

### Protein solubility

**Dataset/protocol:** DeepSol solubility — PEER split

**Scope:** Registered · **Execution:** Results available

| Registered scientific setting | Execution status |
|---|---|
| Solubility — PEER | Results available |

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** Test: 1,999 proteins. Train: 62,478; validation: 6,942 (PEER Table 1).

**Input interface:** Protein sequence

**Reference evidence:** Dataset experimental/curated labels

**Published training/inference regime:** Paper-specific; see source qualifications

**Published evidence — not a local result:** Accuracy: BioT5+ 74.37 ± 0.19%; BioT5 74.65 ± 0.49%.

Task-trained models; BioT5+ is multitask and BioT5 single-task. Count is PEER's published split, not a new loader count.

**Solubility — PEER**

Scientific question: Does the expressed protein remain soluble under the dataset's assay setting?

Native metric: Accuracy

Source split: Preserve the official PEER solubility split; exact test size not re-established.

Qualification: Not binding affinity, thermostability, or a guarantee of solubility under every laboratory condition.

[Source 1](https://arxiv.org/html/2206.02096v2), [Source 2](https://arxiv.org/html/2402.17810v2), [Source 3](https://github.com/DeepGraphLearning/PEER_Benchmark)

</details>

### Subcellular localization

**Dataset/protocol:** DeepLoc — binary and 10-compartment localization

**Scope:** Registered · **Execution:** Results available

| Registered scientific setting | Execution status |
|---|---|
| Binary localization — DeepLoc/PEER | Results available |
| Subcellular localization — DeepLoc | Results available |

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** Published PEER test counts: binary 1,746; 10-compartment 2,768.

**Input interface:** Protein sequence; Protein sequence; label descriptions in zero-shot mode

**Reference evidence:** Curated localization labels; Curated compartment labels

**Published training/inference regime:** Paper-specific; see source qualifications

**Published evidence — not a local result:** Binary accuracy: BioT5+ 90.41%; BioT5 91.69%. 10-class accuracy: ProtST-ESM-2 83.39%; ESM-2 80.84%.

Binary comparison uses task-tuned systems. Ten-class numbers use frozen encoders + trained heads. These are distinct endpoints.

Published ten-class count is 2,768; the frozen local run contains 2,773 cases. These source-specific counts are retained separately.

**Binary localization — DeepLoc/PEER**

Scientific question: Is the protein membrane-associated or in the non-membrane/soluble class?

Native metric: Accuracy

Source split: Binary task; do not substitute the separate ten-compartment label set.

Qualification: 'Soluble' in the localization labels is not the same endpoint as expression solubility in P01.

**Subcellular localization — DeepLoc**

Scientific question: Which cellular compartment does this protein belong to?

Native metric: Accuracy

Source split: Official DeepLoc split. ProtST also tests zero-/few-shot transfer; record shots and whether a supervised head is fitted.

Qualification: Location is a different question from molecular activity or binding specificity.

[Source 1](https://arxiv.org/html/2206.02096v2), [Source 2](https://arxiv.org/html/2402.17810v2), [Source 3](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf), [Source 4](https://github.com/DeepGraphLearning/PEER_Benchmark), [Source 5](https://github.com/DeepGraphLearning/ProtST)

</details>

### Enzyme activity*

**Dataset/protocol:** Envision β-lactamase — PEER split

**Scope:** Registered · **Execution:** Status unverified

| Registered scientific setting | Execution status |
|---|---|
| Beta-lactamase activity — PEER* | Status unverified |

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** Test: 520 variants. Train: 4,158; validation: 520.

**Input interface:** Protein/variant sequence

**Reference evidence:** Existing experimental measurements

**Published training/inference regime:** Paper-specific; see source qualifications

**Published evidence — not a local result:** Spearman: ProtST-ESM-2 0.879; ESM-2 0.867.

Full-model supervised fine-tuning. Assay-specific ranking, not an overall biology score.

**Beta-lactamase activity — PEER**

Scientific question: How active is this enzyme variant in the measured assay?

Native metric: Spearman correlation

Source split: Official PEER beta-lactamase split.

Qualification: The numerical endpoint is assay-specific; these tasks do not establish a general ability to explain mechanisms.

[Source 1](https://arxiv.org/html/2206.02096v2), [Source 2](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf), [Source 3](https://github.com/DeepGraphLearning/PEER_Benchmark)

</details>

### Protein fluorescence*

**Dataset/protocol:** TAPE GFP / Sarkisyan fluorescence

**Scope:** Registered · **Execution:** Running / queued

| Registered scientific setting | Execution status |
|---|---|
| GFP fluorescence — TAPE* | Running / queued |

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** Test: 27,217 variants. Train: 21,446; validation: 5,362.

**Input interface:** Protein/variant sequence

**Reference evidence:** Existing experimental measurements

**Published training/inference regime:** Paper-specific; see source qualifications

**Published evidence — not a local result:** Spearman: ProtST-ESM-2 0.682; ESM-2 0.677.

Full-model supervised fine-tuning. Source counts are the TAPE split documented in PEER, not STRIDE's generated batch.

**GFP fluorescence — TAPE**

Scientific question: Which GFP variants emit stronger fluorescence under the measured conditions?

Native metric: Spearman correlation

Source split: TAPE fluorescence split; sequence-distance extrapolation is part of the benchmark.

Qualification: The numerical endpoint is assay-specific; these tasks do not establish a general ability to explain mechanisms.

[Source 1](https://arxiv.org/html/2206.02096v2), [Source 2](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf), [Source 3](https://github.com/songlab-cal/tape)

</details>

### Protein stability*

**Dataset/protocol:** TAPE / Rocklin stability

**Scope:** Registered · **Execution:** Running / queued

| Registered scientific setting | Execution status |
|---|---|
| Protein stability regression — TAPE* | Running / queued |

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** Test: 12,851 proteins. Train: 53,571; validation: 2,512.

**Input interface:** Protein/variant sequence

**Reference evidence:** Existing experimental measurements

**Published training/inference regime:** Paper-specific; see source qualifications

**Published evidence — not a local result:** Spearman: ProtST-ESM-2 0.738; ESM-2 0.718.

Full-model supervised fine-tuning. Do not conflate with NatureLM's binarized stability task.

**Protein stability regression — TAPE**

Scientific question: Which sequences have higher scores in the stability assay?

Native metric: Spearman correlation

Source split: Official TAPE stability split; retain the numerical target.

Qualification: The numerical endpoint is assay-specific; these tasks do not establish a general ability to explain mechanisms.

[Source 1](https://arxiv.org/html/2206.02096v2), [Source 2](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf), [Source 3](https://github.com/songlab-cal/tape)

</details>

### Variant fitness and thermostability*

**Dataset/protocol:** FLIP — AAV and Meltome

**Scope:** Registered · **Execution:** Partial

| Registered scientific setting | Execution status |
|---|---|
| AAV variant fitness — FLIP* | Status unverified |
| Thermostability — FLIP/Meltome* | Partial |

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** ProtST splits: AAV two_vs_many; Meltome human_cell. Exact test counts not verified in this review.

**Input interface:** Protein/variant sequence

**Reference evidence:** Existing experimental measurements

**Published training/inference regime:** Paper-specific; see source qualifications

**Published evidence — not a local result:** Spearman, ProtST-ESM-2 vs ESM-2: AAV 0.825 vs 0.817; Meltome 0.682 vs 0.672.

Two distinct source datasets, grouped under the FLIP suite. Full-model fine-tuning; no cross-assay average added.

**AAV variant fitness — FLIP**

Scientific question: Which variants score higher in this particular experimental fitness assay?

Native metric: Spearman correlation

Source split: FLIP AAV two_vs_many split.

Qualification: The numerical endpoint is assay-specific; these tasks do not establish a general ability to explain mechanisms.

**Thermostability — FLIP/Meltome**

Scientific question: Which proteins have greater measured thermal stability?

Native metric: Spearman correlation

Source split: FLIP meltome human_cell configuration.

Qualification: The numerical endpoint is assay-specific; these tasks do not establish a general ability to explain mechanisms.

[Source 1](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf), [Source 2](https://github.com/J-SNACKKB/FLIP), [Source 3](https://github.com/J-SNACKKB/FLIP)

</details>

### Protein–protein interaction

**Dataset/protocol:** Human/Pan and yeast/Guo PPI — PEER

**Scope:** Registered · **Execution:** Results available

| Registered scientific setting | Execution status |
|---|---|
| Human protein–protein interaction — PEER | Results available |
| Yeast protein–protein interaction — PEER | Results available |

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** Published PEER test counts: human 227 pairs; yeast 373 pairs.

**Input interface:** Two full protein sequences

**Reference evidence:** Curated interaction positives and dataset-specific negatives

**Published training/inference regime:** Paper-specific; see source qualifications

**Published evidence — not a local result:** Accuracy, BioT5+ vs BioT5: human 85.09% vs 86.22%; yeast 66.16% vs 64.89%.

Separate human/yeast negatives and splits. Generic PPI, not Affibody–pMHC specificity.

**Human protein–protein interaction — PEER**

Scientific question: Do these two proteins interact under the dataset's interaction definition?

Native metric: Accuracy

Source split: Official human PEER PPI split; preserve negative construction.

Qualification: Not TCR–pMHC specificity and not a measured dissociation constant.

**Yeast protein–protein interaction — PEER**

Scientific question: Do these two proteins interact under the dataset's interaction definition?

Native metric: Accuracy

Source split: Official yeast PEER PPI split; preserve negative construction.

Qualification: Not TCR–pMHC specificity and not a measured dissociation constant.

[Source 1](https://arxiv.org/html/2206.02096v2), [Source 2](https://arxiv.org/html/2402.17810v2), [Source 3](https://github.com/DeepGraphLearning/PEER_Benchmark)

</details>

### Protein stability classification*

**Dataset/protocol:** NatureLM/PEER binarized stability — paper-specific protocol

**Scope:** Registered · **Execution:** Status unverified

| Registered scientific setting | Execution status |
|---|---|
| Stability classification — NatureLM/PEER* | Status unverified |

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** NatureLM §7.2 uses classification. Exact label-conversion rule not resolved in this review.

**Input interface:** Protein sequence

**Reference evidence:** A binarized stability label in this paper's setup

**Published training/inference regime:** Source-specific; not a zero-shot/API claim

**Published evidence — not a local result:** NatureLM-8x7B: 72.3% accuracy; SFM-Protein-650M: 58.3%, in NatureLM's stability-classification setup.

Keep separate from TAPE's continuous stability regression. Do not silently change the paper's endpoint.

**Stability classification — NatureLM/PEER**

Scientific question: Does the protein satisfy the paper's stable/unstable label definition?

Native metric: Accuracy

Source split: NatureLM §7.2 uses classification. Exact label-conversion rule not resolved in this review.

Qualification: Keep separate from TAPE's continuous stability regression. Do not silently change the paper's endpoint.

[Source 1](https://arxiv.org/html/2502.07527v3), [Source 2](https://github.com/microsoft/SFM)

</details>

### Antibody properties*

**Dataset/protocol:** FLAb / FLAb2 antibody property collection

**Scope:** Catalog only · **Execution:** Status unverified

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** Current repository: 241 datasets; >3 million assay points. Category counts 31/132/7/4/9/33/25 respectively (see details); not one held-out set.

**Input interface:** Antibody sequences; task-dependent measured context

**Reference evidence:** Experimental assay collections

**Published training/inference regime:** Separate zero-shot likelihood scoring and few-shot fitted prediction

**Published evidence — not a local result:** No version-matched aggregate model score transcribed; repository supplies per-assay zero-/few-shot evaluation outputs.

15 reference datasets are excluded from automated scoring; counts are corpus totals. Each assay has its own units, direction and split.

Catalog coverage only; inclusion does not authorize an experiment or establish execution status.

[Source 1](https://github.com/Graylab/FLAb), [Source 2](https://github.com/Graylab/FLAb)

</details>

### Protein interface contacts*

**Dataset/protocol:** ATOM3D interface contacts (PIP)

**Scope:** Catalog only · **Execution:** Status unverified

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** DIPS training and DB5 testing; exact processed test count not transcribed.

**Input interface:** Unbound protein structures → residue-pair contact

**Reference evidence:** Contacts calculated from experimental complexes

**Published training/inference regime:** Supervised models; original family/sequence exclusions

**Published evidence — not a local result:** AUROC: 3D-CNN 0.844; GNN 0.669; non-3D baseline 0.841.

Residue-pair contact prediction is not sequence-pair binary PPI and not binding affinity.

Catalog coverage only; inclusion does not authorize an experiment or establish execution status.

[Source 1](https://arxiv.org/html/2012.04035v3), [Source 2](https://www.atom3d.ai/pip.html)

</details>

### Protein solubility*

**Dataset/protocol:** PFMBench solubility panel

**Scope:** Catalog only · **Execution:** Status unverified

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** Test sizes: DeepSol: 6,934; DeepSoluE: 1,454; ProtSolM: 7,173; eSOL: 311

**Input interface:** Protein sequences/features; partner/context inputs for interaction tasks

**Reference evidence:** Source annotations/measurements; structure tasks use structural labels

**Published training/inference regime:** Supervised ESM2-Adapter, three-run mean

**Published evidence — not a local result:** ESM2-Adapter, Table 1 means: DeepSol AUROC 0.8467; DeepSoluE AUROC 0.7699; ProtSolM AUROC 0.8572; eSOL Spearman 0.2761

These are PFMBench-specific processed datasets/splits, not interchangeable with PEER/ProtST results. F1 is not Fmax. Affinity-named AUROC tasks are classification, not KD regression. Exact loaders required.

Catalog coverage only; inclusion does not authorize an experiment or establish execution status.

[Source 1](https://arxiv.org/html/2506.14796v1), [Source 2](https://github.com/biomap-research/PFMBench)

</details>

### Localization and sorting signals*

**Dataset/protocol:** PFMBench localization and sorting-signal panel

**Scope:** Catalog only · **Execution:** Status unverified

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** Test sizes: DeepLocMulti: 751; DeepLoc2Multi: 2,744; DeepLocBinary: 848; SortingSignal: 186

**Input interface:** Protein sequences/features; partner/context inputs for interaction tasks

**Reference evidence:** Source annotations/measurements; structure tasks use structural labels

**Published training/inference regime:** Supervised ESM2-Adapter, three-run mean

**Published evidence — not a local result:** ESM2-Adapter, Table 1 means: DeepLocMulti Accuracy 0.7666; DeepLoc2Multi F1 0.7505; DeepLocBinary AUROC 0.9338; SortingSignal F1 0.8598

These are PFMBench-specific processed datasets/splits, not interchangeable with PEER/ProtST results. F1 is not Fmax. Affinity-named AUROC tasks are classification, not KD regression. Exact loaders required.

Catalog coverage only; inclusion does not authorize an experiment or establish execution status.

[Source 1](https://arxiv.org/html/2506.14796v1), [Source 2](https://github.com/biomap-research/PFMBench)

</details>

### Protein and metal interactions*

**Dataset/protocol:** PFMBench protein and metal-interaction panel

**Scope:** Catalog only · **Execution:** Status unverified

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** Test sizes: Human_PPI: 195; Yeast_PPI: 335; PPI_Affinity: 326; MetalIonBinding: 718

**Input interface:** Protein sequences/features; partner/context inputs for interaction tasks

**Reference evidence:** Source annotations/measurements; structure tasks use structural labels

**Published training/inference regime:** Supervised ESM2-Adapter, three-run mean

**Published evidence — not a local result:** ESM2-Adapter, Table 1 means: Human_PPI AUROC 0.4828; Yeast_PPI AUROC 0.5343; PPI_Affinity Spearman -0.0047; MetalIonBinding Accuracy 0.7066

These are PFMBench-specific processed datasets/splits, not interchangeable with PEER/ProtST results. F1 is not Fmax. Affinity-named AUROC tasks are classification, not KD regression. Exact loaders required.

Catalog coverage only; inclusion does not authorize an experiment or establish execution status.

[Source 1](https://arxiv.org/html/2506.14796v1), [Source 2](https://github.com/biomap-research/PFMBench)

</details>

### Protein production and enzyme conditions*

**Dataset/protocol:** PFMBench production and enzyme-operating panel

**Scope:** Catalog only · **Execution:** Status unverified

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** Test sizes: Optimal_pH: 959; DeepET_Topt: 185; Cloning_CLF: 2,778; Material_Production: 2,775; Enzyme_Eff.: 1,290; Antib._Res.: 339; Thermostability: 4,184

**Input interface:** Protein sequences/features; partner/context inputs for interaction tasks

**Reference evidence:** Source annotations/measurements; structure tasks use structural labels

**Published training/inference regime:** Supervised ESM2-Adapter, three-run mean

**Published evidence — not a local result:** ESM2-Adapter, Table 1 means: Optimal_pH Spearman 0.0564; DeepET_Topt Spearman 0.2628; Cloning_CLF AUROC 0.8160; Material_Production Accuracy 0.7982; Enzyme_Eff. Spearman 0.2173; Antib._Res. Accuracy 0.6185; Thermostability AUROC 0.9553

These are PFMBench-specific processed datasets/splits, not interchangeable with PEER/ProtST results. F1 is not Fmax. Affinity-named AUROC tasks are classification, not KD regression. Exact loaders required.

Catalog coverage only; inclusion does not authorize an experiment or establish execution status.

[Source 1](https://arxiv.org/html/2506.14796v1), [Source 2](https://github.com/biomap-research/PFMBench)

</details>

## Protein function, annotations and descriptions

### Enzyme and Gene Ontology annotation*

**Dataset/protocol:** DeepFRI-derived EC and GO test splits

**Scope:** Registered · **Execution:** Running / queued

| Registered scientific setting | Execution status |
|---|---|
| Enzyme Commission labels — DeepFRI split* | Running / queued |
| GO biological process — DeepFRI split* | Running / queued |
| GO molecular function — DeepFRI split* | Running / queued |
| GO cellular component — DeepFRI split* | Running / queued |

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** ProtST's 95%-identity split setting. Exact processed test counts not recovered here.

**Input interface:** Protein sequence

**Reference evidence:** Curated enzyme-function annotations; Ontology-linked curated annotations

**Published training/inference regime:** Paper-specific; see source qualifications

**Published evidence — not a local result:** Fmax, ProtST-ESM-2 vs ESM-2: EC 0.878 vs 0.874; GO-BP 0.482 vs 0.472; GO-MF 0.668 vs 0.662; GO-CC 0.487 vs 0.472.

Full-model supervised tuning. Keep ontology branches separate. This is annotation recovery, not verification of every rationale.

**Enzyme Commission labels — DeepFRI split**

Scientific question: What classes of chemical reaction does the enzyme catalyze?

Native metric: Micro-AP/AUPR; Fmax

Source split: ProtST uses the DeepFRI task split with a 95% sequence-identity cutoff.

Qualification: Multilabel annotation recovery; incomplete annotation is not verified absence of an activity.

**GO biological process — DeepFRI split**

Scientific question: Which larger biological processes does the protein participate in?

Native metric: Micro-AP/AUPR; Fmax

Source split: Keep BP/MF/CC separate; ProtST's DeepFRI-derived split.

Qualification: Not a free-form rationale score. GO label incompleteness and ontology propagation affect evaluation.

**GO molecular function — DeepFRI split**

Scientific question: What molecular activities does the protein perform?

Native metric: Micro-AP/AUPR; Fmax

Source split: Keep BP/MF/CC separate; ProtST's DeepFRI-derived split.

Qualification: Not a free-form rationale score. GO label incompleteness and ontology propagation affect evaluation.

**GO cellular component — DeepFRI split**

Scientific question: Where does the protein act, or in which complex?

Native metric: Micro-AP/AUPR; Fmax

Source split: Keep BP/MF/CC separate; ProtST's DeepFRI-derived split.

Qualification: Not a free-form rationale score. GO label incompleteness and ontology propagation affect evaluation.

[Source 1](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf), [Source 2](https://github.com/DeepGraphLearning/ProtST)

</details>

### Protein description generation

**Dataset/protocol:** Mol-Instructions — four protein-description subsets

**Scope:** Registered · **Execution:** Results available

| Registered scientific setting | Execution status |
|---|---|
| Mol-Instructions: Protein function generation | Results available |
| Mol-Instructions: Catalytic activity generation | Results available |
| Mol-Instructions: Domain and motif generation | Results available |
| Mol-Instructions: Functional description generation | Results available |

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** Original Mol-Instructions paper: approximately 1,000 test examples per task; exact released counts not recomputed.

**Input interface:** Full protein sequence and instruction

**Reference evidence:** Reference descriptions/annotations in Mol-Instructions

**Published training/inference regime:** Paper-specific; see source qualifications

**Published evidence — not a local result:** Official Mol-Instructions LLaMA model ROUGE-L: function 0.43; general description 0.44; catalytic activity 0.52; domain/motif 0.46.

NEW source result: these are Mol-Instructions' own numbers, NOT BioT5+. BioT5+'s Figure 2 reports its comparisons, but exact plotted values were not transcribed.

**Mol-Instructions: Protein function generation**

Scientific question: Which GO functions/processes/components describe this protein?

Native metric: ROUGE-L in BioT5+ protein-text experiments

Source split: Use the Mol-Instructions task-specific split; not one interchangeable pool of protein questions.

Qualification: Text overlap can reward similar wording without validating every biological claim.

**Mol-Instructions: Catalytic activity generation**

Scientific question: What reaction does this protein catalyze?

Native metric: ROUGE-L in BioT5+ protein-text experiments

Source split: Use the Mol-Instructions task-specific split; not one interchangeable pool of protein questions.

Qualification: Text overlap can reward similar wording without validating every biological claim.

**Mol-Instructions: Domain and motif generation**

Scientific question: Which domains or motifs are annotated for the protein?

Native metric: ROUGE-L in BioT5+ protein-text experiments

Source split: Use the Mol-Instructions task-specific split; not one interchangeable pool of protein questions.

Qualification: Text overlap can reward similar wording without validating every biological claim.

**Mol-Instructions: Functional description generation**

Scientific question: How would you summarize what this protein does?

Native metric: ROUGE-L in BioT5+ protein-text experiments

Source split: Use the Mol-Instructions task-specific split; not one interchangeable pool of protein questions.

Qualification: Text overlap can reward similar wording without validating every biological claim.

[Source 1](https://arxiv.org/html/2306.08018v4), [Source 2](https://raw.githubusercontent.com/zjunlp/Mol-Instructions/main/README.md), [Source 3](https://arxiv.org/html/2402.17810v2), [Source 4](https://github.com/zjunlp/Mol-Instructions)

</details>

### Protein description generation*

**Dataset/protocol:** NatureLM's NCBI protein-description holdout

**Scope:** Registered · **Execution:** Status unverified

| Registered scientific setting | Execution status |
|---|---|
| NatureLM protein description* | Status unverified |

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** Temporal split; exact test count and frozen processed release not recovered.

**Input interface:** Protein sequence

**Reference evidence:** NCBI-derived reference descriptions

**Published training/inference regime:** Paper-specific; see source qualifications

**Published evidence — not a local result:** ROUGE-L: NatureLM-8x7B 0.585; fine-tuned Llama-3-8B 0.324; GPT-4o 0.091.

This is a paper-specific NCBI-derived set, not all NCBI data. Different task-training regimes; text-overlap evaluation.

**NatureLM protein description**

Scientific question: Can the model describe a protein whose annotation was withheld?

Native metric: ROUGE-L

Source split: Paper reports a temporal split; exact frozen test release/count not recovered.

Qualification: Do not replace its temporal test with arbitrary UniProt rows and claim exact reproduction.

[Source 1](https://arxiv.org/html/2502.07527v3), [Source 2](https://github.com/microsoft/SFM)

</details>

### Temporal Gene Ontology annotation*

**Dataset/protocol:** BioReason-Pro temporal GO test

**Scope:** Registered · **Execution:** Running / queued

| Registered scientific setting | Execution status |
|---|---|
| BioReason-Pro temporal GO test* | Running / queued |

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** Released test: 8,630 proteins.

**Input interface:** Protein representations and the context permitted by the released evaluator

**Reference evidence:** New curated target-aspect annotations

**Published training/inference regime:** Paper-specific; see source qualifications

**Published evidence — not a local result:** Official repository headline: BioReason-Pro 73.6% Fmax.

Headline aggregation; exact BP/MF/CC definition must come from official evaluator. Not interchangeable with species-held-out evaluation.

**BioReason-Pro temporal GO test**

Scientific question: Can the model recover newly available functional annotations?

Native metric: Fmax; information-accretion-weighted Fmax

Source split: Released test data: 8,630 proteins; preserve the specified temporal and annotation cutoffs.

Qualification: No observed label is not proof of no function. Separate predicted context from gold annotations.

[Source 1](https://huggingface.co/datasets/wanglab/bioreason-pro-test-data), [Source 2](https://raw.githubusercontent.com/bowang-lab/BioReason-Pro/main/README.md), [Source 3](https://huggingface.co/datasets/wanglab/bioreason-pro-test-data)

</details>

### Biochemical reaction classification*

**Dataset/protocol:** ProtST reaction classification — zero/few-shot

**Scope:** Registered · **Execution:** Running / queued

| Registered scientific setting | Execution status |
|---|---|
| Reaction class — zero-/few-shot* | Running / queued |

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** ProtST zero-shot/few-shot experiment; shots and ensemble settings must be recorded.

**Input interface:** Protein sequence plus reaction-label descriptions

**Reference evidence:** Existing reaction-category labels

**Published training/inference regime:** Source-specific; not a zero-shot/API claim

**Published evidence — not a local result:** Zero-/few-shot results are reported, but a numeric value for the exact zero-shot reaction setting is not transcribed here. Do not substitute the fully supervised reaction score.

Zero-shot text-label matching is not the same protocol as fitting a fully supervised classifier.

**Reaction class — zero-/few-shot**

Scientific question: Which of the specified reaction categories matches this protein?

Native metric: Accuracy

Source split: ProtST zero-shot/few-shot experiment; shots and ensemble settings must be recorded.

Qualification: Zero-shot text-label matching is not the same protocol as fitting a fully supervised classifier.

[Source 1](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf), [Source 2](https://github.com/DeepGraphLearning/ProtST)

</details>

### Species-held-out Gene Ontology annotation*

**Dataset/protocol:** Bio-posttrain species-held-out protein GO

**Scope:** Registered · **Execution:** Running / queued

| Registered scientific setting | Execution status |
|---|---|
| Bio-posttrain species-held-out GO test* | Running / queued |

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** Two held-out species in the paper; exact species/counts not established in this review. Also discusses inherited temporal protocol.

**Input interface:** Protein inputs and permitted contextual annotations

**Reference evidence:** Reference GO annotations

**Published training/inference regime:** Source-specific; not a zero-shot/API claim

**Published evidence — not a local result:** Species-held-out GO evaluation is described; a verified numeric result for the exact protein split is not transcribed here.

Do not substitute the original BioReason-Pro 8,630-protein split or its Fmax scorer without documenting the change.

Author resolve_gold_terms_from_row unions curated leaf/ancestor fields AND go_pred_leaf while go_pred is supplied as context. Native reference and input are dependent: the metric can reward recovery/copying of supplied predictions and does not isolate novel function inference. Preserve that augmented target as primary; curated-only reference union is a separate fixed diagnostic, also with predictor overlap and unknown historical independence. Never select the more favorable metric or remove native context.

**Bio-posttrain species-held-out GO test**

Scientific question: Does protein-function prediction transfer to the held-out species?

Native metric: Propagated GO-F1

Source split: Two held-out species in the paper; exact species/counts not established in this review. Also discusses inherited temporal protocol.

Qualification: Do not substitute the original BioReason-Pro 8,630-protein split or its Fmax scorer without documenting the change.

[Source 1](https://arxiv.org/html/2606.16517v1), [Source 2](https://github.com/mims-harvard/bio-posttrain)

</details>

### Enzyme and Gene Ontology annotation*

**Dataset/protocol:** PFMBench GO/EC annotation panel

**Scope:** Catalog only · **Execution:** Status unverified

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** Test sizes: GO-CC: 1,400; GO-MF: 2,787; GO-BP: 2,664; EC: 1,604

**Input interface:** Protein sequences/features; partner/context inputs for interaction tasks

**Reference evidence:** Source annotations/measurements; structure tasks use structural labels

**Published training/inference regime:** Supervised ESM2-Adapter, three-run mean

**Published evidence — not a local result:** ESM2-Adapter, Table 1 means: GO-CC F1 0.6130; GO-MF F1 0.6488; GO-BP F1 0.5412; EC F1 0.7379

These are PFMBench-specific processed datasets/splits, not interchangeable with PEER/ProtST results. F1 is not Fmax. Affinity-named AUROC tasks are classification, not KD regression. Exact loaders required.

Catalog coverage only; inclusion does not authorize an experiment or establish execution status.

[Source 1](https://arxiv.org/html/2506.14796v1), [Source 2](https://github.com/biomap-research/PFMBench)

</details>

## Mutation-effect interpretation

### Mutation-effect explanation*

**Dataset/protocol:** MutaDescribe — mutation explanation

**Scope:** Registered · **Execution:** Status unverified

| Registered scientific setting | Execution status |
|---|---|
| MutaDescribe mutation explanation* | Status unverified |

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** Main test: Easy 460; Medium 384; Hard 404 mutation examples. Separate temporal test: 1,611 (not the reported main averages).

**Input interface:** Reference and mutant sequences/change, plus model-specific protein context

**Reference evidence:** Expert-source annotations, publication-enriched descriptions; synthetic reversals present in corpus

**Published training/inference regime:** Paper-specific; see source qualifications

**Published evidence — not a local result:** Main-test average ROUGE-L / BLEU-2 (0–100): MutaPLM 21.34 / 13.61; GPT-4-0613, 5-shot kNN: 12.31 / 9.69.

The reported 'Average' is retained as the paper defines it. Similarity tiers are not a globally homology-disjoint split.

**MutaDescribe mutation explanation**

Scientific question: What effect does this amino-acid change have?

Native metric: BLEU-2; ROUGE-L; GPT-4-plus-human categorical review

Source split: Random split then similarity tiers: Easy 460, Medium 384, Hard 404. Separate temporal test has 1,611 examples.

Qualification: Similarity tiers do not make the entire split homology-disjoint. Judge output is not independent experimental verification.

[Source 1](https://arxiv.org/html/2410.22949v1), [Source 2](https://huggingface.co/datasets/PharMolix/MutaDescribe)

</details>

## Mutation ranking, affinity and local optimization

### Mutation-effect ranking*

**Dataset/protocol:** ProteinGym substitutions — historical ProtST evaluation

**Scope:** Registered · **Execution:** Status unverified

| Registered scientific setting | Execution status |
|---|---|
| ProteinGym DMS substitution benchmark* | Status unverified |

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** Use the historical ProteinGym snapshot in ProtST. Do not attach the modern 217-assay count to these old results.

**Input interface:** Reference and variant sequences; optional structure/MSA only if the protocol allows

**Reference evidence:** Measured DMS assay scores

**Published training/inference regime:** Paper-specific; see source qualifications

**Published evidence — not a local result:** UniProt-level mean Spearman: ProtST-ESM-1b 0.412; ESM-1b 0.358; ESM-1v 0.372; Tranception L without retrieval 0.401.

NEW verified numeric row from ProtST Table 12. Not a current ProteinGym leaderboard result.

**ProteinGym DMS substitution benchmark**

Scientific question: Do model scores rank variants in the same order as the experiments?

Native metric: Spearman primary; suite also reports ranking/classification summaries

Source split: Pin release: modern v1.3 substitution subset has 217 assays; an older paper may use an earlier snapshot.

Qualification: Score within each assay. Different assay scores are not a shared physical unit; fitness is not always binding.

[Source 1](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf), [Source 2](https://github.com/OATML-Markslab/ProteinGym), [Source 3](https://github.com/OATML-Markslab/ProteinGym)

</details>

### Mutation-effect ranking*

**Dataset/protocol:** PG-LLM / ProteinGym-LLM — eval-data-v1.2

**Scope:** Registered · **Execution:** Deferred / held

| Registered scientific setting | Execution status |
|---|---|
| PG-LLM / ProteinGym-LLM ranking* | Deferred / held |

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** 217 assays; sets of 10, 50 or 100 variants; three seeds.

**Input interface:** Full reference sequence, assay description, shuffled candidate sequences

**Reference evidence:** Held-out experimental scores

**Published training/inference regime:** Paper-specific; see source qualifications

**Published evidence — not a local result:** No verified release-matched model score was recovered. This does not mean zero performance.

Evaluation-only frozen protocol. Benchmark-specific training, tuning and retrieval augmentation are restricted by its documentation.

**PG-LLM / ProteinGym-LLM ranking**

Scientific question: Can a language model rank a supplied set of variant sequences by assay performance?

Native metric: Per-assay Spearman

Source split: eval-data-v1.2: 217 assays; N=10/50/100; seeds 1/2/3; labels separate from model-facing inputs.

Qualification: Evaluation-only: do not train, tune prompts, distill or perform retrieval augmentation using these candidate sets/labels.

[Source 1](https://raw.githubusercontent.com/rohitarorayyc/proteingym-llm/main/DATA.md), [Source 2](https://github.com/rohitarorayyc/proteingym-llm/blob/main/DATA.md)

</details>

### Protein fitness and affinity*

**Dataset/protocol:** PFArena — four task settings

**Scope:** Registered · **Execution:** Source-blocked

| Registered scientific setting | Execution status |
|---|---|
| PFArena T1: single-mutant generation* | Source-blocked |
| PFArena T2: measurement-free multi-mutant ranking* | Source-blocked |
| PFArena T3: anchor-informed ranking* | Source-blocked |
| PFArena T4: single-mutant-informed ranking* | Source-blocked |

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** T1: 123 assays / 594,695 measured singles. T2: 74 assays / 6,288 candidates. T3: 67 assays / 3,648 candidates. T4: 29 assays / 2,638 candidates.

**Input interface:** Reference protein + objective; no target-specific mutant measurements; Reference + objective + candidate combinations; no target-specific measured labels; A measured anchor mutant + strictly extending candidate combinations; Component single-mutant measurements + candidate multi-mutants

**Reference evidence:** Existing experimental mutation measurements

**Published training/inference regime:** Paper-specific; see source qualifications

**Published evidence — not a local result:** Paper's GPT-6 Astra vs ESM-2: T1 Recall@40 0.0254 vs 0.0370; T2 Spearman 0.2726 vs 0.2539; T3 0.3516 vs 0.3128; T4 0.5988 vs 0.3153.

Different assay subsets, not a paired context ablation. Reported aggregates include deterministic random fallback on missing outputs (§10.1/Table 12). Model labels are the paper's, not verified API IDs. Exact public bundle not yet established; retained paper model labels are not executable API identifiers.

**PFArena T1: single-mutant generation**

Scientific question: Which single substitutions should be proposed?

Native metric: Recall@40; normalized maximum recovered score

Source split: 123 assays; budget 40; 594,695 measured single mutants in the reported source universe

Qualification: The tasks differ in permitted evidence. 'Anchor' is a tested mutant, not an HLA anchor residue. Assay sets overlap.

Documented blocker: PFArena official release found; publisher dataset access is gated and original assay/case review remains pending.

[Blocker evidence](https://github.com/Some-random/bio-evaluation/blob/main/reports/remaining_native_source_recovery_2026-10-15.md)

**PFArena T2: measurement-free multi-mutant ranking**

Scientific question: Which supplied combinations should rank highest without measurements?

Native metric: Spearman; NDCG; normalized max@K; Recall@K

Source split: 74 assays; 6,288 candidates

Qualification: The tasks differ in permitted evidence. 'Anchor' is a tested mutant, not an HLA anchor residue. Assay sets overlap.

Documented blocker: PFArena official release found; publisher dataset access is gated and original assay/case review remains pending.

[Blocker evidence](https://github.com/Some-random/bio-evaluation/blob/main/reports/remaining_native_source_recovery_2026-10-15.md)

**PFArena T3: anchor-informed ranking**

Scientific question: Which additions to an already tested mutant are promising?

Native metric: Spearman; NDCG; normalized max@K; Recall@K

Source split: 67 assays; 3,648 candidates

Qualification: The tasks differ in permitted evidence. 'Anchor' is a tested mutant, not an HLA anchor residue. Assay sets overlap.

Documented blocker: PFArena official release found; publisher dataset access is gated and original assay/case review remains pending.

[Blocker evidence](https://github.com/Some-random/bio-evaluation/blob/main/reports/remaining_native_source_recovery_2026-10-15.md)

**PFArena T4: single-mutant-informed ranking**

Scientific question: Can measurements of individual changes help rank their combinations?

Native metric: Spearman; NDCG; normalized max@K; Recall@K

Source split: 29 assays; 2,638 candidates; 28,609 single-mutant context records

Qualification: The tasks differ in permitted evidence. 'Anchor' is a tested mutant, not an HLA anchor residue. Assay sets overlap.

Documented blocker: PFArena official release found; publisher dataset access is gated and original assay/case review remains pending.

[Blocker evidence](https://github.com/Some-random/bio-evaluation/blob/main/reports/remaining_native_source_recovery_2026-10-15.md)

[Source 1](https://arxiv.org/html/2609.28921v1), [Source 2](https://arxiv.org/html/2609.28921v1)

</details>

### Mutation proposal and engineering*

**Dataset/protocol:** MutaDescribe — mutation engineering

**Scope:** Registered · **Execution:** Status unverified

| Registered scientific setting | Execution status |
|---|---|
| MutaDescribe mutation engineering — position supplied* | Status unverified |
| MutaDescribe mutation engineering — position unknown* | Status unverified |

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** Same main Easy/Medium/Hard split as explanation: 460 / 384 / 404 examples.

**Input interface:** Protein, desired effect, correct mutation position; Protein and desired effect

**Reference evidence:** Annotated reference mutation

**Published training/inference regime:** Paper-specific; see source qualifications

**Published evidence — not a local result:** MutaPLM vs fine-tuned ESM-2: position known accuracy 53.51% vs 51.43%; position unknown Recall@50 40.94% vs 33.77%.

Same source dataset, different task. These are reference-recovery rates, not prospective wet-lab success.

**MutaDescribe mutation engineering — position supplied**

Scientific question: Given a desired effect and a specified position, which residue should replace the original?

Native metric: Accuracy

Source split: Same similarity/temporal splits as MutaDescribe; supplied position simplifies the task.

Qualification: Recovery of one annotated mutation is not the fraction of novel designs that work.

**MutaDescribe mutation engineering — position unknown**

Scientific question: Which 50 single substitutions best fit the requested effect?

Native metric: Recall@50

Source split: Search covers 19 × sequence-length substitutions; preserve the paper's candidate definition.

Qualification: A different useful but unannotated mutation can score as a miss.

[Source 1](https://arxiv.org/html/2410.22949v1), [Source 2](https://huggingface.co/datasets/PharMolix/MutaDescribe)

</details>

### Low-data fitness regression*

**Dataset/protocol:** MutaPLM low-data fitness regression

**Scope:** Registered · **Execution:** Status unverified

| Registered scientific setting | Execution status |
|---|---|
| MutaPLM low-N fitness regression* | Status unverified |

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** 192 training + 48 validation examples; five seeds; assay-specific remaining test records

**Input interface:** Variant representations; a separately fitted regression head

**Reference evidence:** Experimental Spike–ACE2 and avGFP measurements

**Published training/inference regime:** Source-specific; not a zero-shot/API claim

**Published evidence — not a local result:** Low-data regression curves are reported with 192 train / 48 validation examples; no exact assay-specific point estimate is transcribed here.

This is supervised low-N prediction, not zero-shot generation. Do not reuse the labeled seed points as test examples.

**MutaPLM low-N fitness regression**

Scientific question: With a small labeled sample, can features predict held-out assay outcomes?

Native metric: Spearman

Source split: 192 training and 48 validation samples; five random seeds. Remaining held-out data evaluated per source.

Qualification: This is supervised low-N prediction, not zero-shot generation. Do not reuse the labeled seed points as test examples.

[Source 1](https://arxiv.org/html/2410.22949v1), [Source 2](https://github.com/PharMolix/MutaPLM)

</details>

### Antibody affinity ranking*

**Dataset/protocol:** AbBiBench antibody affinity ranking

**Scope:** Catalog only · **Execution:** Status unverified

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** Paper: 155,853 heavy-chain variants, 9 antigens (Section 3.1 lists 11 datasets). Current repository leaderboard: 16 assay columns; expanded payload count not established.

**Input interface:** Antibody/target sequences and permitted structural context; varies by model

**Reference evidence:** Experimental affinity

**Published training/inference regime:** Model-specific scoring, not matched training resources

**Published evidence — not a local result:** Current 16-column leaderboard mean Spearman: ProteinMPNN 0.30; ESM-IF1 0.28; AntiFold 0.21; ESM2 0.02.

Paper size and current leaderboard refer to different snapshots. Do not combine them into a single size-matched result. Generative case study is separate.

Catalog coverage only; inclusion does not authorize an experiment or establish execution status.

[Source 1](https://github.com/MSBMI-SAFE/AbBiBench), [Source 2](https://arxiv.org/html/2506.04235v1), [Source 3](https://huggingface.co/datasets/AbBibench/Antibody_Binding_Benchmark_Dataset)

</details>

### Mutation effects on binding affinity*

**Dataset/protocol:** ATOM3D SKEMPI-derived mutation affinity (MSP)

**Scope:** Catalog only · **Execution:** Status unverified

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** Source construction: 893 positive and 3,255 negative mutations; exact test size not recovered.

**Input interface:** Wild-type/mutant structural context

**Reference evidence:** Experimental mutation affinity measurements

**Published training/inference regime:** Supervised; preserve sequence-based split

**Published evidence — not a local result:** AUROC: GNN 0.621; 3D-CNN 0.574.

This is binding-affinity change classification, not folding-stability prediction. Source counts are not test counts.

Catalog coverage only; inclusion does not authorize an experiment or establish execution status.

[Source 1](https://arxiv.org/html/2012.04035v3), [Source 2](https://www.atom3d.ai/msp.html)

</details>

### Mutation and fitness prediction*

**Dataset/protocol:** PFMBench mutation/fitness panel

**Scope:** Catalog only · **Execution:** Status unverified

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** Test sizes: PETA_CHS_SOL: 484; PETA_LGK_SOL: 1,914; PETA_TEM_SOL: 808; FLIP_AAV: 16,517; FLIP_GB1: 1,745; TAPE_Stab: 6,898; TAPE_Fluor: 27,217; BetaLactamase: 520

**Input interface:** Protein sequences/features; partner/context inputs for interaction tasks

**Reference evidence:** Source annotations/measurements; structure tasks use structural labels

**Published training/inference regime:** Supervised ESM2-Adapter, three-run mean

**Published evidence — not a local result:** ESM2-Adapter, Table 1 means: PETA_CHS_SOL Spearman 0.2738; PETA_LGK_SOL Spearman 0.1558; PETA_TEM_SOL Spearman 0.1433; FLIP_AAV Spearman 0.9412; FLIP_GB1 Spearman 0.9517; TAPE_Stab Spearman 0.3211; TAPE_Fluor Spearman 0.6812; BetaLactamase Spearman 0.5740

These are PFMBench-specific processed datasets/splits, not interchangeable with PEER/ProtST results. F1 is not Fmax. Affinity-named AUROC tasks are classification, not KD regression. Exact loaders required.

Catalog coverage only; inclusion does not authorize an experiment or establish execution status.

[Source 1](https://arxiv.org/html/2506.14796v1), [Source 2](https://github.com/biomap-research/PFMBench)

</details>

### Peptide–MHC and TCR–pMHC interactions*

**Dataset/protocol:** PFMBench peptide–MHC and TCR–pMHC panel

**Scope:** Catalog only · **Execution:** Status unverified

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** Test sizes: Pept.HLA/MHC Aff.: 8,406; TCR.PMHC Aff.: 2,482

**Input interface:** Protein sequences/features; partner/context inputs for interaction tasks

**Reference evidence:** Source annotations/measurements; structure tasks use structural labels

**Published training/inference regime:** Supervised ESM2-Adapter, three-run mean

**Published evidence — not a local result:** ESM2-Adapter, Table 1 means: Pept.HLA/MHC Aff. AUROC 0.9631; TCR.PMHC Aff. AUROC 0.9312

These are PFMBench-specific processed datasets/splits, not interchangeable with PEER/ProtST results. F1 is not Fmax. Affinity-named AUROC tasks are classification, not KD regression. Exact loaders required.

Catalog coverage only; inclusion does not authorize an experiment or establish execution status.

[Source 1](https://arxiv.org/html/2506.14796v1), [Source 2](https://github.com/biomap-research/PFMBench)

</details>

### Zero-shot mutation-effect ranking*

**Dataset/protocol:** PFMBench ProteinGym zero-shot protocol

**Scope:** Catalog only · **Execution:** Status unverified

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** Paper table does not specify the release-matched evaluation denominator.

**Input interface:** Protein sequences/features; partner/context inputs for interaction tasks

**Reference evidence:** Source annotations/measurements; structure tasks use structural labels

**Published training/inference regime:** Zero-shot sequence scoring

**Published evidence — not a local result:** Table 1 reports pretrained ESM2 ProteinGym Spearman 0.4390; do not compare directly to a different snapshot's score.

These are PFMBench-specific processed datasets/splits, not interchangeable with PEER/ProtST results. F1 is not Fmax. Affinity-named AUROC tasks are classification, not KD regression. Exact loaders required.

Catalog coverage only; inclusion does not authorize an experiment or establish execution status.

[Source 1](https://arxiv.org/html/2506.14796v1), [Source 2](https://github.com/biomap-research/PFMBench)

</details>

## Scientific evidence and biological knowledge

### Research evidence and biological knowledge*

**Dataset/protocol:** LAB-Bench — research tasks

**Scope:** Registered · **Execution:** Partial

| Registered scientific setting | Execution status |
|---|---|
| LAB-Bench / LitQA2* | Partial |
| LAB-Bench / DbQA | Results available |
| LAB-Bench / SuppQA | Results available |
| LAB-Bench / FigQA | Results available |
| LAB-Bench / TableQA | Results available |
| LAB-Bench / ProtocolQA* | Deferred / held |
| LAB-Bench / SeqQA | Results available |
| LAB-Bench / Cloning scenarios | Results available |

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** Original full evaluation: 2,457 questions. LitQA2 248; SuppQA 102; FigQA 226; TableQA 305; DbQA 650; ProtocolQA 135; SeqQA 750; Cloning 41.

**Input interface:** Literature question; access to papers depends on evaluation protocol; Database-oriented question; resource access must be stated; Question about supplementary information; supplied/retrieved documents if allowed; Figure and associated question; Table and question; A procedure-related scenario and question; Sequence plus a transformation/analysis question; Scenario and sequence/context information

**Reference evidence:** Benchmark reference answers curated by task creators

**Published training/inference regime:** Paper-specific; see source qualifications

**Published evidence — not a local result:** Historical 2024 GPT-4o accuracy: LitQA2 27%; SuppQA 13%; FigQA 29%; TableQA 71%; ProtocolQA 53%; Cloning 28%. DbQA variant-from-sequence 42%; SeqQA GC% 29%, ORF-sequence 50% (SUBTASK values only).

Original full public+private test; not the public 1,967-question subset. Three-run means. Tool-free models; TableQA and FigQA are images. No new category aggregate invented.

**LAB-Bench / LitQA2**

Scientific question: Can the model answer a question whose answer is in the scientific literature?

Native metric: Accuracy; selective precision and coverage when abstention is enabled

Source split: Public subset commonly 1,967 questions across eight categories; original full set and private portion differ. Pin dataset revision.

Qualification: Keep resource access fixed. Original model evaluation was tool-free, unlike human baseline. MCQ success can partly reflect distractor elimination.

**LAB-Bench / DbQA**

Scientific question: Can the model recover the correct fact from a biological database?

Native metric: Accuracy; selective precision and coverage when abstention is enabled

Source split: Public subset commonly 1,967 questions across eight categories; original full set and private portion differ. Pin dataset revision.

Qualification: Keep resource access fixed. Original model evaluation was tool-free, unlike human baseline. MCQ success can partly reflect distractor elimination.

**LAB-Bench / SuppQA**

Scientific question: Can the model locate information in a paper's supplementary material?

Native metric: Accuracy; selective precision and coverage when abstention is enabled

Source split: Public subset commonly 1,967 questions across eight categories; original full set and private portion differ. Pin dataset revision.

Qualification: Keep resource access fixed. Original model evaluation was tool-free, unlike human baseline. MCQ success can partly reflect distractor elimination.

**LAB-Bench / FigQA**

Scientific question: Can the model interpret a scientific figure?

Native metric: Accuracy; selective precision and coverage when abstention is enabled

Source split: Public subset commonly 1,967 questions across eight categories; original full set and private portion differ. Pin dataset revision.

Qualification: Keep resource access fixed. Original model evaluation was tool-free, unlike human baseline. MCQ success can partly reflect distractor elimination.

**LAB-Bench / TableQA**

Scientific question: Can the model read and reason about a scientific table?

Native metric: Accuracy; selective precision and coverage when abstention is enabled

Source split: Public subset commonly 1,967 questions across eight categories; original full set and private portion differ. Pin dataset revision.

Qualification: Keep resource access fixed. Original model evaluation was tool-free, unlike human baseline. MCQ success can partly reflect distractor elimination.

**LAB-Bench / ProtocolQA**

Scientific question: Can the model identify problems or implications in an experimental procedure?

Native metric: Accuracy; selective precision and coverage when abstention is enabled

Source split: Public subset commonly 1,967 questions across eight categories; original full set and private portion differ. Pin dataset revision.

Qualification: Keep resource access fixed. Original model evaluation was tool-free, unlike human baseline. MCQ success can partly reflect distractor elimination.

**LAB-Bench / SeqQA**

Scientific question: Can the model carry out the requested operation on the supplied sequence?

Native metric: Accuracy; selective precision and coverage when abstention is enabled

Source split: Public subset commonly 1,967 questions across eight categories; original full set and private portion differ. Pin dataset revision.

Qualification: Keep resource access fixed. Original model evaluation was tool-free, unlike human baseline. MCQ success can partly reflect distractor elimination.

**LAB-Bench / Cloning scenarios**

Scientific question: Can the model solve the sequence-constraint problem in a cloning scenario?

Native metric: Accuracy; selective precision and coverage when abstention is enabled

Source split: Public subset commonly 1,967 questions across eight categories; original full set and private portion differ. Pin dataset revision.

Qualification: Keep resource access fixed. Original model evaluation was tool-free, unlike human baseline. MCQ success can partly reflect distractor elimination.

[Source 1](https://arxiv.org/html/2407.10362v1), [Source 2](https://huggingface.co/datasets/futurehouse/lab-bench)

</details>

### Protein understanding*

**Dataset/protocol:** ProteinLMBench protein-understanding questions

**Scope:** Catalog only · **Execution:** Status unverified

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** 944 manually verified questions; six choices per question.

**Input interface:** Text question + choices

**Reference evidence:** Expert-verified answer labels

**Published training/inference regime:** Paper's trained language-model variants

**Published evidence — not a local result:** InternLM2-7B after SFT: 58.26% accuracy; SSL+SFT: 62.18%.

Knowledge/test-taking evaluation, not direct novel protein-function prediction.

Catalog coverage only; inclusion does not authorize an experiment or establish execution status.

[Source 1](https://arxiv.org/html/2406.05540v1), [Source 2](https://huggingface.co/datasets/tsynbio/ProteinLMBench)

</details>

### Research-abstract question answering*

**Dataset/protocol:** PubMedQA research-abstract questions

**Scope:** Catalog only · **Execution:** Status unverified

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** 1,000 expert-labeled records total; official evaluation split must be pinned. 61.2K unlabeled and 211.3K artificial records are separate training resources.

**Input interface:** Question + source abstract

**Reference evidence:** Expert labels + paper conclusions

**Published training/inference regime:** Source-specific training; supplied-evidence QA

**Published evidence — not a local result:** Original BioBERT multi-phase training: 68.1% accuracy; reported human baseline 78.0%. Historical results.

The conclusion/long answer must stay out of solver input under the reasoning-required protocol.

Catalog coverage only; inclusion does not authorize an experiment or establish execution status.

[Source 1](https://arxiv.org/abs/1909.06146), [Source 2](https://github.com/pubmedqa/pubmedqa)

</details>

## Protein design

### Antibody design: CDR-H3 redesign*

**Dataset/protocol:** RAbD — CDR-H3 redesign

**Scope:** Registered · **Execution:** Status unverified

| Registered scientific setting | Execution status |
|---|---|
| RAbD CDR-H3 redesign* | Status unverified |

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** 60 antibody–antigen complexes.

**Input interface:** Antigen, antibody framework, fixed complex context; H3 masked

**Reference evidence:** Reference antibody–antigen structures/sequences

**Published training/inference regime:** Paper-specific; see source qualifications

**Published evidence — not a local result:** Proteo-R1 vs BoltzGen: AAR 10.75% vs 39.07%; RMSD 2.46 Å vs 2.69 Å; DockQ 0.801 vs 0.473.

Geometry and native-sequence recovery disagree; no dominance claim across all metrics. Not prospective binding success. ProteinBench's 55-complex processed version is separately listed.

**RAbD CDR-H3 redesign**

Scientific question: Can the model reconstruct/design an antibody loop in a fixed antigen/framework context?

Native metric: NatureLM: AAR. Proteo-R1: AAR, RMSD, lDDT, TM-score, DockQ.

Source split: 60 complexes; retain paper-specific renumbering, masked region and preprocessing.

Qualification: High native recovery or geometric similarity does not imply measured binding for a new design.

[Source 1](https://arxiv.org/html/2605.02937v1), [Source 2](https://arxiv.org/html/2605.02937v1)

</details>

### Antibody design: multi-CDR redesign*

**Dataset/protocol:** SAbDab — Proteo-R1 all-CDR holdout

**Scope:** Registered · **Execution:** Status unverified

| Registered scientific setting | Execution status |
|---|---|
| Proteo-R1 all-CDR SAbDab holdout* | Status unverified |

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** Paper-specific temporal/cluster split; exact processed test count not recovered.

**Input interface:** Antigen/framework/docking context with CDR sequence/geometry masked

**Reference evidence:** Held-out SAbDab complexes

**Published training/inference regime:** Paper-specific; see source qualifications

**Published evidence — not a local result:** Proteo-R1 vs MFDesign: H3 RMSD 3.81 Å vs 3.71 Å; Loop-RMSD 4.51 Å vs 4.28 Å; IMP 56.58 vs 59.16 (paper's scale).

One dataset, multiple metrics. H3 RMSD and Loop-RMSD are different columns. Oracle-Anchor row is not the deployed system.

**Proteo-R1 all-CDR SAbDab holdout**

Scientific question: Can all designated antibody loops be redesigned consistently with the complex?

Native metric: Structural/recovery/interface metrics; Rosetta-derived energy and clash diagnostics

Source split: Release-time filtering and 50%-identity H3 clusters; 9:0.5:0.5 cluster split. Exact test count not established.

Qualification: Computational reconstruction/design. The original docking pose is assumed known; not unconstrained binder discovery.

[Source 1](https://arxiv.org/html/2605.02937v1), [Source 2](https://arxiv.org/html/2605.02937v1)

</details>

### Sequence design by inverse folding*

**Dataset/protocol:** CATH 4.2 / TS50 / TS500 inverse folding

**Scope:** Catalog only · **Execution:** Status unverified

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** CATH 4.2 exact test count not re-established; TS50/TS500 named test suites (50/500 nominal structures; exact retained manifests must be checked).

**Input interface:** Backbone coordinates → sequence

**Reference evidence:** Reference sequences and structures

**Published training/inference regime:** Trained inverse-folding model

**Published evidence — not a local result:** PiFold repository: CATH recovery 51.66%; TS50 58.72%; TS500 60.42%.

Recovery is not experimental fold/function validation; named size does not replace retained-record manifest.

Catalog coverage only; inclusion does not authorize an experiment or establish execution status.

[Source 1](https://github.com/a4bio/pifold), [Source 2](https://github.com/a4bio/pifold)

</details>

### Sequence design by inverse folding*

**Dataset/protocol:** ProteinBench inverse folding — CASP15 / CAMEO / synthetic backbones

**Scope:** Catalog only · **Execution:** Status unverified

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** 32 CASP15 structures; 332 CAMEO complexes; synthetic backbones: 10 at each of 5 lengths (100–500 aa).

**Input interface:** Coordinates → sequence

**Reference evidence:** Reference structure/sequence and self-consistency predictions

**Published training/inference regime:** Published pretrained-model evaluation

**Published evidence — not a local result:** AAR, CASP15/CAMEO: LM-Design 0.516/0.570; ProteinMPNN 0.450/0.468.

Some models are excluded from native recovery because of training exposure. Synthetic consistency is model-scored, not wet-lab.

Catalog coverage only; inclusion does not authorize an experiment or establish execution status.

[Source 1](https://arxiv.org/html/2409.06744v2), [Source 2](https://proteinbench.github.io/)

</details>

### Unconditional protein backbone generation*

**Dataset/protocol:** ProteinBench unconditional backbone generation

**Scope:** Catalog only · **Execution:** Status unverified

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** Length-stratified generation at 100/200/300/400/500 aa; 100 single-chain reference structures. Exact generated count must follow the release.

**Input interface:** Length/optional constraints → coordinates

**Reference evidence:** Predicted self-consistency

**Published training/inference regime:** Fixed generator plus sequence/structure scorers

**Published evidence — not a local result:** At length 100: RFdiffusion scTM 0.98 ± 0.12 and scRMSD 0.48 ± 0.56 Å; FrameFlow 0.94 ± 0.08 and 0.70 ± 0.70 Å.

Reported values retained on the paper's scale; structural plausibility does not establish function.

Catalog coverage only; inclusion does not authorize an experiment or establish execution status.

[Source 1](https://arxiv.org/html/2409.06744v2), [Source 2](https://proteinbench.github.io/)

</details>

### Unconditional protein sequence generation*

**Dataset/protocol:** ProteinBench unconditional sequence generation

**Scope:** Catalog only · **Execution:** Status unverified

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** 50 sequences per model at each length 100, 200, 300 and 500.

**Input interface:** Text/sequence generation with external structural scoring

**Reference evidence:** Structure-predictor confidence

**Published training/inference regime:** Sequence generator plus fixed folding evaluator

**Published evidence — not a local result:** At length 100, predicted AF2 pLDDT: DPLM-650M 85.38 ± 14.20; ProGen2-700M 64.00 ± 21.26.

pLDDT is confidence, not experimentally measured protein stability or function.

Catalog coverage only; inclusion does not authorize an experiment or establish execution status.

[Source 1](https://arxiv.org/html/2409.06744v2), [Source 2](https://proteinbench.github.io/)

</details>

### Joint sequence and structure generation*

**Dataset/protocol:** ProteinBench joint sequence–structure generation

**Scope:** Catalog only · **Execution:** Status unverified

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** Length-stratified generated samples; exact per-setting candidate count not recovered.

**Input interface:** Length/constraints → sequence + coordinates

**Reference evidence:** Predicted self-consistency

**Published training/inference regime:** Joint generator + specialized scorer

**Published evidence — not a local result:** Multiflow at length 100: scTM 0.96 ± 0.04; scRMSD 1.10 ± 0.71 Å. At length 200: scTM 0.95; scRMSD 1.61 Å.

These are selected length-specific results, not one design success rate.

Catalog coverage only; inclusion does not authorize an experiment or establish execution status.

[Source 1](https://arxiv.org/html/2409.06744v2), [Source 2](https://proteinbench.github.io/)

</details>

### Functional-motif scaffolding*

**Dataset/protocol:** MotifBench functional-motif scaffolding

**Scope:** Catalog only · **Execution:** Status unverified

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** 30 motif problems; standard submission 100 scaffolds per problem.

**Input interface:** Motif coordinates + constraints → backbone; sequence design/scoring pipeline

**Reference evidence:** Structural constraints and computational refolding

**Published training/inference regime:** Fixed proposal budget; standardized evaluation

**Published evidence — not a local result:** Official leaderboard snapshot: RFdiffusion3 43.52 ± 1.35 (Aug 2026); RFdiffusion 21.95 (Feb 2025), in MotifBench-score units.

Score is not percentage of experimentally functional proteins. Preserve sampling and evaluator versions.

Catalog coverage only; inclusion does not authorize an experiment or establish execution status.

[Source 1](https://github.com/blt2114/MotifBench), [Source 2](https://github.com/blt2114/MotifBench)

</details>

### Functional-motif scaffolding*

**Dataset/protocol:** ProteinBench motif scaffolding — legacy motif panel

**Scope:** Catalog only · **Execution:** Status unverified

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** Legacy 17 (25) motif-problem panel described by ProteinBench; not MotifBench's separate 30-problem set.

**Input interface:** Motif structure → scaffold

**Reference evidence:** Structural constraints + predicted designability

**Published training/inference regime:** Paper-defined conditional generation

**Published evidence — not a local result:** Comparative motif-scaffolding results are reported; exact figure-derived score not transcribed.

Do not merge the legacy panel with MotifBench or reuse their scores interchangeably.

Catalog coverage only; inclusion does not authorize an experiment or establish execution status.

[Source 1](https://arxiv.org/html/2409.06744v2), [Source 2](https://proteinbench.github.io/)

</details>

### Antibody design: CDR-H3 redesign*

**Dataset/protocol:** ProteinBench antibody design — processed RAbD

**Scope:** Catalog only · **Execution:** Status unverified

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** 55 retained RAbD complexes; differs from the 60-complex protocol in the earlier catalog.

**Input interface:** Complex structure + masked H3 → sequence/structure

**Reference evidence:** Native sequence/structure

**Published training/inference regime:** Published design-model comparison

**Published evidence — not a local result:** DiffAb: AAR 35.04 ± 8.36%, RMSD 2.53 ± 0.60 Å; MEAN: AAR 33.47%, RMSD 1.82 Å.

Same parent resource does not mean identical split or scorer. This is a distinct protocol, not 55 additional independent complexes.

Catalog coverage only; inclusion does not authorize an experiment or establish execution status.

[Source 1](https://arxiv.org/html/2409.06744v2), [Source 2](https://proteinbench.github.io/)

</details>

### Antibody design: epitope-conditioned design*

**Dataset/protocol:** CHIMERA-Bench epitope-conditioned antibody design

**Scope:** Catalog only · **Execution:** Status unverified

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** 2,922 complexes total. Test: 292 epitope-group; 292 antigen-fold; 293 temporal. Splits are alternatives, not additive test sets.

**Input interface:** Antigen/framework/epitope context → CDR sequence+structure

**Reference evidence:** Reference complex contacts/geometry

**Published training/inference regime:** Eleven methods retrained on shared source splits

**Published evidence — not a local result:** Epitope-group H3: RAAD AAR 0.37, RMSD 1.75 Å, DockQ 0.58; dyMEAN EpiF1 0.23 (RAAD 0.11).

EpiF1 measures intended-site contact, not empirical selectivity across off-target molecules.

Catalog coverage only; inclusion does not authorize an experiment or establish execution status.

[Source 1](https://arxiv.org/html/2603.13431v1), [Source 2](https://github.com/mansoor181/chimera-bench)

</details>

### Target-binder design*

**Dataset/protocol:** ProtDBench de novo target-binder design

**Scope:** Catalog only · **Execution:** Status unverified

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** 10 target proteins; 24 h on one A100 per method/target setting. Includes generation, inverse folding and scoring.

**Input interface:** Target coordinates/sequence/hotspots → proposed binders

**Reference evidence:** Predicted interface/structure criteria; separate retrospective experimental analysis

**Published training/inference regime:** Time-matched generation and filtering

**Published evidence — not a local result:** PD-L1 passing-backbone counts: PXDesign 1,247; BoltzGen 549; RFdiffusion3 542; BindCraft 231. TNFα: PXDesign 57; BoltzGen 15.

Counts of computational passes, not wet-lab hit fractions. Exact target-specific conditions and verifier must match.

Catalog coverage only; inclusion does not authorize an experiment or establish execution status.

[Source 1](https://arxiv.org/html/2605.04118v1), [Source 2](https://arxiv.org/html/2605.04118v1)

</details>

## Structure and conformational prediction

### Residue identity from local structure*

**Dataset/protocol:** ATOM3D residue identity from local structure (RES)

**Scope:** Catalog only · **Execution:** Status unverified

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** Test: 3,319 PDB structures yielding 1,261,342 local environments; train: 21,147 structures.

**Input interface:** 3D local atomic environment → amino-acid label

**Reference evidence:** Structure-derived residue labels

**Published training/inference regime:** Supervised structural model; preserve CATH topology split

**Published evidence — not a local result:** ATOM3D 3D-CNN test accuracy: 0.451.

Environment count is not protein count. This is an established held-out structure task, unlike unverified internal diagnostics.

Catalog coverage only; inclusion does not authorize an experiment or establish execution status.

[Source 1](https://arxiv.org/html/2012.04035v3), [Source 2](https://www.atom3d.ai/)

</details>

### Protein structure ranking*

**Dataset/protocol:** ATOM3D protein structure ranking (PSR)

**Scope:** Catalog only · **Execution:** Status unverified

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** CASP-derived target/decoy split; exact processed test-target/decoy counts not transcribed.

**Input interface:** Candidate coordinates → quality score

**Reference evidence:** Reference structural quality

**Published training/inference regime:** Supervised structural scoring

**Published evidence — not a local result:** Per-target mean Spearman: GNN 0.515; 3D-CNN 0.431. Global correlations are different metrics.

Ranking a supplied set of structures is not de novo structure generation.

Catalog coverage only; inclusion does not authorize an experiment or establish execution status.

[Source 1](https://arxiv.org/html/2012.04035v3), [Source 2](https://www.atom3d.ai/)

</details>

### Single-state protein folding*

**Dataset/protocol:** ProteinBench single-state folding — CAMEO 2022

**Scope:** Catalog only · **Execution:** Status unverified

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** 183 proteins (<750 residues), released Aug–Oct 2022.

**Input interface:** Sequence and protocol-permitted context → coordinates

**Reference evidence:** Experimental reference structures

**Published training/inference regime:** Model-specific structure prediction

**Published evidence — not a local result:** AF2 mean/median TM-score 0.871/0.952, RMSD 3.21/1.64 Å; ESMFold 0.847/0.929 and 3.98/2.10 Å.

Models may have different MSA/template access. This is a historical target cohort, not the live CAMEO leaderboard.

Catalog coverage only; inclusion does not authorize an experiment or establish execution status.

[Source 1](https://arxiv.org/html/2409.06744v2), [Source 2](https://proteinbench.github.io/)

</details>

### Multistate protein conformations*

**Dataset/protocol:** ProteinBench multistate conformations — apo/holo and BPTI

**Scope:** Catalog only · **Execution:** Status unverified

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** Apo/holo: 91 protein pairs, 20 generated conformations per protein. BPTI: one 58-residue protein, 5 MD clusters, N=10/100/1000 samples.

**Input interface:** Sequence → conformational ensemble

**Reference evidence:** Experimental paired states / MD reference clusters

**Published training/inference regime:** Ensemble generation at fixed sampling budget

**Published evidence — not a local result:** Apo/holo TM-ensemble: AlphaFlow-PDB 0.873; MSA-depth256 0.867. BPTI N=1000: ConfDiff-ESM-force ensemble RMSD 1.36 Å.

Sample count is not the number of independent test proteins; BPTI alone gives narrow generalization evidence.

Catalog coverage only; inclusion does not authorize an experiment or establish execution status.

[Source 1](https://arxiv.org/html/2409.06744v2), [Source 2](https://proteinbench.github.io/)

</details>

### Protein conformational ensembles*

**Dataset/protocol:** ProteinBench ensemble distribution — ATLAS

**Scope:** Catalog only · **Execution:** Status unverified

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** 82 held-out proteins; 250 generated conformations per protein.

**Input interface:** Sequence → ensemble

**Reference evidence:** Molecular-dynamics reference distributions

**Published training/inference regime:** Fixed ensemble sampling and distributional metrics

**Published evidence — not a local result:** AlphaFlow-MD: per-target RMSF correlation 0.85 and PCA-Wasserstein 1.55; ConfDiff PCA-Wasserstein 1.41 (paper's units).

MD reference is simulation-derived, not an exhaustive experimental distribution. Preserve alignment, projection and aggregation.

Catalog coverage only; inclusion does not authorize an experiment or establish execution status.

[Source 1](https://arxiv.org/html/2409.06744v2), [Source 2](https://proteinbench.github.io/)

</details>

### Protein states, dynamics and free energy*

**Dataset/protocol:** BioEmu benchmark collection — states, dynamics and free energy

**Scope:** Catalog only · **Execution:** Status unverified

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** Multiple panels: domain motion, local unfolding, cryptic pockets, MD emulation and experimental folding free energies. Exact panel sizes not re-counted.

**Input interface:** Protein sequence → conformational ensemble

**Reference evidence:** Experimental structures/stabilities and MD references

**Published training/inference regime:** Pretrained ensemble generator; specialized evaluation

**Published evidence — not a local result:** Official model card: domain-motion coverage 83%; cryptic-pocket apo/holo coverage 55%/88%; experimental stability MAE ~0.9 kcal/mol, Spearman ~0.6.

Pin benchmark/model revision: version changes affect values. Panel scores are not one pooled success rate.

Catalog coverage only; inclusion does not authorize an experiment or establish execution status.

[Source 1](https://github.com/microsoft/bioemu/blob/main/MODEL_CARD.md), [Source 2](https://github.com/microsoft/bioemu-benchmarks)

</details>

### Structure-derived protein prediction*

**Dataset/protocol:** PFMBench structure-derived prediction panel

**Scope:** Catalog only · **Execution:** Status unverified

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** Test sizes: Contact: 1,501; FoldClass: 1,630; SecondaryStructure: 8,262

**Input interface:** Protein sequences/features; partner/context inputs for interaction tasks

**Reference evidence:** Source annotations/measurements; structure tasks use structural labels

**Published training/inference regime:** Supervised ESM2-Adapter, three-run mean

**Published evidence — not a local result:** ESM2-Adapter, Table 1 means: Contact Top L/5 0.7199; FoldClass Accuracy 0.7859; SecondaryStructure Accuracy 0.7601

These are PFMBench-specific processed datasets/splits, not interchangeable with PEER/ProtST results. F1 is not Fmax. Affinity-named AUROC tasks are classification, not KD regression. Exact loaders required.

Catalog coverage only; inclusion does not authorize an experiment or establish execution status.

[Source 1](https://arxiv.org/html/2506.14796v1), [Source 2](https://github.com/biomap-research/PFMBench)

</details>

## Biomedical visual evidence

### Biomedical visual question answering

**Dataset/protocol:** Biomedical VQA: VQA-RAD / SLAKE-English / PathVQA / VQA-Med 2019

**Scope:** Registered · **Execution:** Results available

| Registered scientific setting | Execution status |
|---|---|
| VQA-RAD | Results available |
| SLAKE — English | Results available |
| PathVQA | Results available |
| ImageCLEF-VQA 2019 | Results available |

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** Distinct official task splits; exact test counts not re-established. Open/closed answer groups must remain separate.

**Input interface:** Radiology images with questions; Medical images with English questions; Pathology images with questions; Medical images and questions

**Reference evidence:** Curated image/answer records; Curated visual questions/answers; Dataset image/answer pairs; Challenge reference answers

**Published training/inference regime:** Source-specific; not a zero-shot/API claim

**Published evidence — not a local result:** MedVInT-TD: 73.7% open-answer and 86.8% closed-answer accuracy on VQA-RAD after task-specific fine-tuning. MedVInT-TE: 88.2% open-answer and 87.7% closed-answer accuracy on SLAKE after task-specific fine-tuning. LLaVA-Med initialized from Vicuna: PathVQA 38.87 open-answer token recall and 91.65% closed-answer accuracy, after task-specific fine-tuning. MedVInT-TE: 70.5% overall accuracy on VQA-Med 2019 after task-specific fine-tuning.

Medical-image performance does not show use of protein sequence/structure embeddings. Open-answer scorers differ between papers. | Medical-image performance does not show use of protein sequence/structure embeddings. Open-answer scorers differ between papers. | Medical-image performance does not show use of protein sequence/structure embeddings. Open-answer scorers differ between papers. | Medical-image performance does not show use of protein sequence/structure embeddings. Open-answer scorers differ between papers.

**VQA-RAD**

Scientific question: Can the model answer a question using the supplied medical image?

Native metric: Closed-question accuracy; open scoring is paper-specific (e.g. token recall in original LLaVA-Med)

Source split: Use task's official train/test split; do not use total corpus size as test size.

Qualification: Medical-image performance does not show use of protein sequence/structure embeddings. Open-answer scorers differ between papers.

**SLAKE — English**

Scientific question: Can the model answer a question using the supplied medical image?

Native metric: Closed-question accuracy; open scoring is paper-specific (e.g. token recall in original LLaVA-Med)

Source split: English subset; exact partition and normalization must match the target paper.

Qualification: Medical-image performance does not show use of protein sequence/structure embeddings. Open-answer scorers differ between papers.

**PathVQA**

Scientific question: Can the model answer a question using the supplied medical image?

Native metric: Closed-question accuracy; open scoring is paper-specific (e.g. token recall in original LLaVA-Med)

Source split: Official split; keep closed/open question groups separate.

Qualification: Medical-image performance does not show use of protein sequence/structure embeddings. Open-answer scorers differ between papers.

**ImageCLEF-VQA 2019**

Scientific question: Can the model answer a question using the supplied medical image?

Native metric: Closed-question accuracy; open scoring is paper-specific (e.g. token recall in original LLaVA-Med)

Source split: The 2019 challenge snapshot, not an arbitrary later VQA-Med release.

Qualification: Medical-image performance does not show use of protein sequence/structure embeddings. Open-answer scorers differ between papers.

[Source 1](https://arxiv.org/abs/2306.00890), [Source 2](https://arxiv.org/html/2305.10415v6), [Source 3](https://arxiv.org/abs/2306.00890), [Source 4](https://arxiv.org/html/2305.10415v6), [Source 5](https://github.com/microsoft/LLaVA-Med), [Source 6](https://github.com/xiaoman-zhang/PMC-VQA)

</details>

### Scientific figure question answering

**Dataset/protocol:** PMC-VQA figure question answering

**Scope:** Registered · **Execution:** Results available

| Registered scientific setting | Execution status |
|---|---|
| PMC-VQA held-out evaluation | Results available |

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** Reviewed v6: 50,000 initial test examples; 2,000 manually reviewed clean test examples.

**Input interface:** Image, question, and optionally answer choices

**Reference evidence:** Synthetic figure-derived labels; manually checked clean subset

**Published training/inference regime:** Source-specific; not a zero-shot/API claim

**Published evidence — not a local result:** The paper reports initial and manually cleaned PMC-VQA tests. A numeric result tied to an exact model and that exact split is not transcribed here.

Specify initial versus cleaned test set. Caption-derived labels need not be visually answerable without filtering.

**PMC-VQA held-out evaluation**

Scientific question: Can the model answer a question from a biomedical paper figure?

Native metric: MCQ accuracy; paper's open/blank-answer accuracy and BLEU

Source split: v6: 50,000 initial image-disjoint test examples; 2,000 manually reviewed clean test examples. Older site names differ.

Qualification: Specify initial versus cleaned test set. Caption-derived labels need not be visually answerable without filtering.

[Source 1](https://arxiv.org/html/2305.10415v6), [Source 2](https://github.com/xiaoman-zhang/PMC-VQA)

</details>

### Biomedical visual conversations*

**Dataset/protocol:** LLaVA-Med biomedical visual conversations

**Scope:** Registered · **Execution:** Status unverified

| Registered scientific setting | Execution status |
|---|---|
| LLaVA-Med visual conversation* | Status unverified |

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** Published 50-image conversation-evaluation setting; teacher-generated text references.

**Input interface:** Biomedical image and conversational questions

**Reference evidence:** Text-only GPT-4 answers generated using captions and inline mentions

**Published training/inference regime:** Source-specific; not a zero-shot/API claim

**Published evidence — not a local result:** GPT-assisted relative answer-quality comparisons are reported. A verified single aggregate for the specified qa50 setting is not transcribed here.

Teacher reference has textual context that the image may not reveal. Judgment is not direct clinician-verified molecular truth.

**LLaVA-Med visual conversation**

Scientific question: Can the model give useful biomedical explanations of a supplied image?

Native metric: GPT-assisted relative response assessment

Source split: Released qa50 evaluation files; 50-image setting. Use original/v1.5 code and model version consistently.

Qualification: Teacher reference has textual context that the image may not reveal. Judgment is not direct clinician-verified molecular truth.

[Source 1](https://arxiv.org/abs/2306.00890), [Source 2](https://github.com/microsoft/LLaVA-Med)

</details>

## Other biological modalities and molecular interactions

### Drug–target interaction

**Dataset/protocol:** Drug–target interaction: BioSNAP / Human / BindingDB

**Scope:** Registered · **Execution:** Results available

| Registered scientific setting | Execution status |
|---|---|
| Drug–target interaction — BioSNAP/Human/BindingDB | Results available |

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** Three source benchmarks; preserve each split/negative/threshold rule.

**Input interface:** Small-molecule representation and protein sequence

**Reference evidence:** Dataset-specific interaction/affinity-derived labels

**Published training/inference regime:** Source-specific; not a zero-shot/API claim

**Published evidence — not a local result:** BioT5+ AUROC: BioSNAP 0.939 ± 0.001; Human 0.987 ± 0.001; BindingDB 0.964 ± 0.001.

Secondary to the protein focus. Not protein–protein recognition or Affibody–pMHC evaluation.

**Drug–target interaction — BioSNAP/Human/BindingDB**

Scientific question: Does a small molecule interact with a protein target?

Native metric: AUROC in BioT5+ comparisons

Source split: Three source benchmarks; preserve each split/negative/threshold rule.

Qualification: Secondary to the protein focus. Not protein–protein recognition or Affibody–pMHC evaluation.

[Source 1](https://arxiv.org/html/2402.17810v2), [Source 2](https://github.com/QizhiPei/BioT5)

</details>

### Pathway and disease prediction

**Dataset/protocol:** BioReason KEGG pathway/disease

**Scope:** Registered · **Execution:** Results available

| Registered scientific setting | Execution status |
|---|---|
| BioReason KEGG pathway/disease test | Results available |

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** 290 test entries in main table; 1,449 overall entries across splits.

**Input interface:** Reference/variant DNA and pathway context

**Reference evidence:** KEGG-linked annotations

**Published training/inference regime:** Source-specific; not a zero-shot/API claim

**Published evidence — not a local result:** Evo2 + Qwen3-4B + GRPO: 98.28% accuracy, 93.05 macro-F1; Qwen3-4B-only: 90.00% accuracy, 79.66 macro-F1.

Correct final disease labels do not verify every generated mechanistic statement.

**BioReason KEGG pathway/disease test**

Scientific question: Which disease is associated with the supplied variant and pathway context?

Native metric: Accuracy; macro-F1/precision/recall

Source split: 290 test entries in main table; 1,449 overall entries across splits.

Qualification: Correct final disease labels do not verify every generated mechanistic statement.

[Source 1](https://arxiv.org/html/2505.23579v2), [Source 2](https://huggingface.co/datasets/wanglab/kegg)

</details>

### Variant-effect prediction

**Dataset/protocol:** BioReason VEP coding and non-SNV

**Scope:** Registered · **Execution:** Results available

| Registered scientific setting | Execution status |
|---|---|
| BioReason VEP-Coding | Results available |
| BioReason VEP-Non-SNV | Results available |

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** Coding: approximately 1.23K reported test cases; non-SNV: 873. Distinct datasets.

**Input interface:** Reference/variant DNA and prompt; Variant representation/context

**Reference evidence:** Curated clinical variant labels; Curated variant labels

**Published training/inference regime:** Source-specific; not a zero-shot/API claim

**Published evidence — not a local result:** Evo2 + Qwen3-4B: 80.21% accuracy, 80.00 F1; Evo2-only: 70.07% accuracy, 49.19 F1. Evo2 + Qwen3-4B: 83.85% accuracy, 85.02 F1; Evo2-only: 76.17% accuracy, 66.51 F1.

Genomics task, not Affibody binding; annotation confidence and splitting matter. | Non-SNV classification should not be merged with single-amino-acid design accuracy.

**BioReason VEP-Coding**

Scientific question: Is this coding variant labeled pathogenic or benign?

Native metric: Accuracy; F1

Source split: Main reported test approximately 1.23K; chromosome 8 held out.

Qualification: Genomics task, not Affibody binding; annotation confidence and splitting matter.

**BioReason VEP-Non-SNV**

Scientific question: Is this non-single-nucleotide variant labeled pathogenic or benign?

Native metric: Accuracy; F1

Source split: 873 test examples in the main report.

Qualification: Non-SNV classification should not be merged with single-amino-acid design accuracy.

[Source 1](https://arxiv.org/html/2505.23579v2), [Source 2](https://github.com/bowang-lab/BioReason)

</details>

### Network-held-out pathway prediction*

**Dataset/protocol:** Bio-posttrain KEGG unseen-network holdout

**Scope:** Registered · **Execution:** Source-blocked

| Registered scientific setting | Execution status |
|---|---|
| Bio-posttrain KEGG network holdout* | Source-blocked |

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** Adapted KEGG split by pathway networks; not automatically BioReason's original 290-example test.

**Input interface:** DNA representations and pathway context

**Reference evidence:** Task reference annotations

**Published training/inference regime:** Source-specific; not a zero-shot/API claim

**Published evidence — not a local result:** Qwen3-4B DNA OOD accuracy: SFT 0.753; SFT+RL 0.917; biology-CPT+SFT+RL 0.970.

Pin the adapted split and preprocessing.

**Bio-posttrain KEGG network holdout**

Scientific question: Does DNA/pathway reasoning generalize to unseen pathway networks?

Native metric: Accuracy

Source split: Adapted KEGG split by pathway networks; not automatically BioReason's original 290-example test.

Qualification: Pin the adapted split and preprocessing.

Documented blocker: Exact network-held-out CSVs/IDs unavailable; author genomics link redirects to sign-in. Original N01 is not a substitute.

[Blocker evidence](https://github.com/Some-random/bio-evaluation/blob/main/reports/POSTTRAIN_NATIVE_GAP_AUDIT.md)

[Source 1](https://arxiv.org/html/2606.16517v1), [Source 2](https://github.com/mims-harvard/bio-posttrain)

</details>

### Expression-conditioned gene selection*

**Dataset/protocol:** Bio-posttrain MEDEA expression-conditioned gene selection

**Scope:** Registered · **Execution:** Source-blocked

| Registered scientific setting | Execution status |
|---|---|
| Bio-posttrain MEDEA target selection* | Source-blocked |

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** Held-out disease: hepatoblastoma; additional cell-type analyses reported.

**Input interface:** Candidate genes, expression representations, disease and cell context

**Reference evidence:** Adapted MEDEA task answers

**Published training/inference regime:** Source-specific; not a zero-shot/API claim

**Published evidence — not a local result:** The paper reports RNA target-selection ID/OOD experiments. An exact numeric result is not transcribed in this table.

Fixed-input target nomination is not the original full agent workflow or clinical validation.

**Bio-posttrain MEDEA target selection**

Scientific question: Which candidate gene is supported by the supplied disease/cell-expression context?

Native metric: Normalized gene-answer accuracy

Source split: Held-out disease: hepatoblastoma; additional cell-type analyses reported.

Qualification: Fixed-input target nomination is not the original full agent workflow or clinical validation.

Documented blocker: Exact adapted hepatoblastoma split/vector alignment/RNA evaluator missing; upstream MEDEA questions or gene lists do not replace required expression inputs.

[Blocker evidence](https://github.com/Some-random/bio-evaluation/blob/main/reports/POSTTRAIN_NATIVE_GAP_AUDIT.md)

[Source 1](https://arxiv.org/html/2606.16517v1), [Source 2](https://github.com/mims-harvard/bio-posttrain)

</details>

### Protein–ligand binding affinity*

**Dataset/protocol:** ATOM3D protein–ligand affinity (LBA)

**Scope:** Catalog only · **Execution:** Status unverified

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** 30%-identity split: train 3,507, validation 466, test 490 complexes. The 60% split is a different protocol.

**Input interface:** Protein–ligand coordinates → assay-derived affinity

**Reference evidence:** PDBbind experimental affinities

**Published training/inference regime:** Supervised regression

**Published evidence — not a local result:** 3D-CNN: RMSE 1.416, Spearman 0.553; GNN: RMSE 1.570, Spearman 0.628.

Target transformation and split must match. Not antibody–antigen affinity.

Catalog coverage only; inclusion does not authorize an experiment or establish execution status.

[Source 1](https://arxiv.org/html/2012.04035v3), [Source 2](https://www.atom3d.ai/)

</details>

### Ligand efficacy*

**Dataset/protocol:** ATOM3D ligand efficacy (LEP)

**Scope:** Catalog only · **Execution:** Status unverified

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** 527 source small molecules; final retained train/test counts not transcribed.

**Input interface:** Ligand/receptor conformations → efficacy class

**Reference evidence:** Curated active/inactive ligand labels

**Published training/inference regime:** Supervised classification

**Published evidence — not a local result:** AUROC: GNN 0.740; 3D-CNN 0.589.

Activity/efficacy is distinct from affinity. Source molecule count is not a test denominator.

Catalog coverage only; inclusion does not authorize an experiment or establish execution status.

[Source 1](https://arxiv.org/html/2012.04035v3), [Source 2](https://www.atom3d.ai/lep.html)

</details>

### RNA structure ranking*

**Dataset/protocol:** ATOM3D RNA structure ranking (RSR)

**Scope:** Catalog only · **Execution:** Status unverified

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** RNA-Puzzles 1–21; test puzzles 18–21, with decoys per target. Exact retained test-decoy count not re-counted.

**Input interface:** RNA candidate coordinates → quality score

**Reference evidence:** RNA reference structures

**Published training/inference regime:** Supervised ranking

**Published evidence — not a local result:** Mean per-target Spearman: 3D-CNN 0.264; GNN 0.234.

RNA task retained as adjacent scope, not a protein benchmark.

Catalog coverage only; inclusion does not authorize an experiment or establish execution status.

[Source 1](https://arxiv.org/html/2012.04035v3), [Source 2](https://www.atom3d.ai/rsr.html)

</details>

### Small-molecule properties*

**Dataset/protocol:** ATOM3D small-molecule properties (SMP / QM9)

**Scope:** Catalog only · **Execution:** Status unverified

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** Processed test 12,943 molecules (train 103,547; validation 12,943).

**Input interface:** Small-molecule atom coordinates → property

**Reference evidence:** Quantum-calculation labels

**Published training/inference regime:** Supervised molecular regression

**Published evidence — not a local result:** ENN dipole MAE 0.052 D; 3D-CNN 0.754 D. Property-specific scores must remain separate.

Adjacency only; not protein biology. Units depend on property.

Catalog coverage only; inclusion does not authorize an experiment or establish execution status.

[Source 1](https://arxiv.org/html/2012.04035v3), [Source 2](https://www.atom3d.ai/)

</details>

### Protein–ligand binding affinity*

**Dataset/protocol:** PFMBench PDBbind / BindingDB affinity panel

**Scope:** Catalog only · **Execution:** Status unverified

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** Test sizes: PDBBind: 1,836; BindingDB: 1,139

**Input interface:** Protein sequences/features; partner/context inputs for interaction tasks

**Reference evidence:** Source annotations/measurements; structure tasks use structural labels

**Published training/inference regime:** Supervised ESM2-Adapter, three-run mean

**Published evidence — not a local result:** ESM2-Adapter, Table 1 means: PDBBind Spearman 0.1677; BindingDB Spearman 0.1922

These are PFMBench-specific processed datasets/splits, not interchangeable with PEER/ProtST results. F1 is not Fmax. Affinity-named AUROC tasks are classification, not KD regression. Exact loaders required.

Catalog coverage only; inclusion does not authorize an experiment or establish execution status.

[Source 1](https://arxiv.org/html/2506.14796v1), [Source 2](https://github.com/biomap-research/PFMBench)

</details>

## Case studies and diagnostics

These nine groups retain their scientific parent category but are not promoted to independent benchmark test sets. The internal structural/alignment diagnostic remains separate until an independent held-out manifest is resolved.

### Protein function, annotations and descriptions — diagnostic appendix

#### Text-to-protein retrieval*

**Dataset/protocol:** ProtST text-to-protein retrieval examples

**Scope:** Registered · **Execution:** Status unverified

| Registered scientific setting | Execution status |
|---|---|
| ProtST text-to-protein retrieval* | Status unverified |

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** Can a functional description retrieve relevant proteins? Selected queries such as heme binding; not a universal, fixed retrieval benchmark with one headline Recall@K.

**Published evidence — not a local result:** Selected text-to-protein retrieval and docking case studies are reported; no single fixed-corpus Recall@K benchmark result is transcribed.

Retrieval case study Docking and known annotations support case analysis; they do not prove all retrieved candidates bind experimentally.

Case study or diagnostic; kept separate from independent benchmark results.

**ProtST text-to-protein retrieval**

Scientific question: Can a functional description retrieve relevant proteins?

Native metric: Top-retrieval inspection; docking scores in case studies

Source split: Selected queries such as heme binding; not a universal, fixed retrieval benchmark with one headline Recall@K.

Qualification: Docking and known annotations support case analysis; they do not prove all retrieved candidates bind experimentally.

[Source 1](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf)

</details>

#### Functional explanation review*

**Dataset/protocol:** BioReason-Pro explanation review

**Scope:** Registered · **Execution:** Status unverified

| Registered scientific setting | Execution status |
|---|---|
| BioReason-Pro explanation assessment* | Status unverified |

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** Are the generated functional explanations helpful and consistent with the reference evidence? Separate from the 8,630-protein GO-label metric; exact scored explanation subset not established here.

**Published evidence — not a local result:** Repository reports an LLM-judge score of 8/10 and expert preference over UniProt descriptions in 79% of reviewed cases.

Judged explanation subset Correct GO labels do not guarantee that every intermediate statement is true.

Case study or diagnostic; kept separate from independent benchmark results.

**BioReason-Pro explanation assessment**

Scientific question: Are the generated functional explanations helpful and consistent with the reference evidence?

Native metric: Judge rubrics; qualitative/expert review

Source split: Separate from the 8,630-protein GO-label metric; exact scored explanation subset not established here.

Qualification: Correct GO labels do not guarantee that every intermediate statement is true.

[Source 1](https://www.biorxiv.org/content/10.64898/2026.03.19.712954v2.full)

</details>

### Mutation ranking, affinity and local optimization — diagnostic appendix

#### Iterative mutation optimization*

**Dataset/protocol:** MutaPLM iterative optimization

**Scope:** Registered · **Execution:** Status unverified

| Registered scientific setting | Execution status |
|---|---|
| MutaPLM iterative sequence optimization* | Status unverified |

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** Do iterative proposals improve the predicted assay objective? Six landscapes: AAV, AMIE, avGFP, E4B, LGK, UBE2I; 20 independent runs; preserve beam/search settings.

**Published evidence — not a local result:** The paper reports predicted-fitness improvement trajectories across six landscapes; these are oracle-based search outcomes, not experimentally measured hit rates.

Predictor-scored search experiment A learned scorer can be exploited; this experiment is not prospective laboratory success.

Case study or diagnostic; kept separate from independent benchmark results.

**MutaPLM iterative sequence optimization**

Scientific question: Do iterative proposals improve the predicted assay objective?

Native metric: Mean predicted fitness trajectory and dispersion

Source split: Six landscapes: AAV, AMIE, avGFP, E4B, LGK, UBE2I; 20 independent runs; preserve beam/search settings.

Qualification: A learned scorer can be exploited; this experiment is not prospective laboratory success.

[Source 1](https://arxiv.org/html/2410.22949v1)

</details>

### Protein design — diagnostic appendix

#### Description-guided protein design*

**Dataset/protocol:** BioT5+ description-guided protein generation

**Scope:** Registered · **Execution:** Status unverified

| Registered scientific setting | Execution status |
|---|---|
| BioT5+ description-guided protein design* | Status unverified |

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** Can the model propose a sequence matching a description? The paper does not define a generally established benchmark for this task.

**Published evidence — not a local result:** Description-guided protein designs are presented as qualitative cases rather than a fixed, experimentally validated design-success rate.

Qualitative design case A plausible or similar sequence is not a measured successful design.

Case study or diagnostic; kept separate from independent benchmark results.

**BioT5+ description-guided protein design**

Scientific question: Can the model propose a sequence matching a description?

Native metric: Qualitative cases and sequence/reference comparisons

Source split: The paper does not define a generally established benchmark for this task.

Qualification: A plausible or similar sequence is not a measured successful design.

[Source 1](https://arxiv.org/html/2402.17810v2)

</details>

#### Unconditional and property-conditioned protein design*

**Dataset/protocol:** NatureLM generated proteins: unconditional / property-conditioned / heme

**Scope:** Registered · **Execution:** Status unverified

| Registered scientific setting | Execution status |
|---|---|
| NatureLM unconditional generation* | Status unverified |
| NatureLM stability/solubility-conditioned generation* | Status unverified |
| NatureLM heme-binding case study* | Status unverified |

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** Does the model generate varied, structurally plausible protein sequences? / Do sequences requested to have a property score well under the evaluator? / Can conditioning suggest proteins plausibly associated with heme? Generated samples compared with natural sequences; not a labeled holdout prediction set. | Paper uses a natural UR50 reference subset of 1,000 sequences in the conditioned comparison. | Selected candidates; no standard released labeled test-set size.

**Published evidence — not a local result:** Reported outputs are diversity/length distributions and predicted structural confidence. No experimentally measured function-success fraction is supplied by this evaluation. The reported comparison uses learned stability/solubility scores and diversity. No measured stability/solubility success rate is transcribed. Selected heme-binding candidates are screened with descriptions and predicted complexes; this is not experimentally demonstrated heme binding.

Predictor-scored or qualitative design Diversity and predicted structure confidence do not establish function. | Predictor agreement, not experimentally measured stability/solubility of each generated sequence. | Self-description is not independent validation; predicted complexes are not measured binding.

Case study or diagnostic; kept separate from independent benchmark results.

**NatureLM unconditional generation**

Scientific question: Does the model generate varied, structurally plausible protein sequences?

Native metric: Length distribution; clustering-based diversity; pLDDT

Source split: Generated samples compared with natural sequences; not a labeled holdout prediction set.

Qualification: Diversity and predicted structure confidence do not establish function.

**NatureLM stability/solubility-conditioned generation**

Scientific question: Do sequences requested to have a property score well under the evaluator?

Native metric: Predicted property scores; diversity

Source split: Paper uses a natural UR50 reference subset of 1,000 sequences in the conditioned comparison.

Qualification: Predictor agreement, not experimentally measured stability/solubility of each generated sequence.

**NatureLM heme-binding case study**

Scientific question: Can conditioning suggest proteins plausibly associated with heme?

Native metric: Qualitative description/complex screening

Source split: Selected candidates; no standard released labeled test-set size.

Qualification: Self-description is not independent validation; predicted complexes are not measured binding.

[Source 1](https://arxiv.org/html/2502.07527v3)

</details>

#### Fluorescence sequence optimization*

**Dataset/protocol:** STRIDE GFP sequence optimization

**Scope:** Registered · **Execution:** Partial

| Registered scientific setting | Execution status |
|---|---|
| STRIDE GFP generated-candidate evaluation* | Partial |

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** Do proposed edits improve the fixed scorer's predicted fluorescence? 100 candidates per method from a common source; separate replace-only and full-edit settings.

**Published evidence — not a local result:** Fixed fluorescence-oracle successes: full edit setting 89/100 for STRIDE vs 42/100 SFT; replace-only 61/100 vs 55/100 SFT.

Predictor-scored generation These 100 candidates are not a wet-lab test set. Correctly applying edits does not validate fluorescence.

Case study or diagnostic; kept separate from independent benchmark results.

**STRIDE GFP generated-candidate evaluation**

Scientific question: Do proposed edits improve the fixed scorer's predicted fluorescence?

Native metric: Predicted improvement/success; uniqueness; novelty

Source split: 100 candidates per method from a common source; separate replace-only and full-edit settings.

Qualification: These 100 candidates are not a wet-lab test set. Correctly applying edits does not validate fluorescence.

[Source 1](https://arxiv.org/html/2603.03573v1)

</details>

#### Text-conditioned target-binder design*

**Dataset/protocol:** Prompteina text-conditioned protein design — GM2A campaign

**Scope:** Catalog only · **Execution:** Status unverified

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** Generate target binders from language specifications; measure selected designs prospectively. 1,000-design computational budget; 90 selected; 89 expressed and assayed.

**Published evidence — not a local result:** 9 of 89 assayed designs classified as binders; 8 fitted apparent KD values. Strongest apparent KD: 107 nM.

Prospective experimental campaign A single target campaign, not a general fixed test set or aggregate success rate. 52.4M captions is a training size.

Case study or diagnostic; kept separate from independent benchmark results.

[Source 1](https://arxiv.org/html/2610.13917v1)

</details>

### Structure and conformational prediction — diagnostic appendix

#### Internal structural and alignment diagnostics*

**Dataset/protocol:** Proteo-R1 internal alignment / structural / CDR diagnostics

**Scope:** Catalog only · **Execution:** Status unverified

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** Check training-stage behavior on calculated structural questions and output-schema tasks. Independent held-out question manifest and size unresolved; 9.09M is Stage-II TRAINING instances.

**Published evidence — not a local result:** Selected Stage-II M3: contact 58.3%; interface 15.1%; hotspot 11.6%. Separate Stage-I schema 81.4%. No overall score.

Internal diagnostic — holdout unresolved Not a named released PDB benchmark. Eight-response averages are not pass@8. No evidence of leakage is inferred from missing documentation.

Case study or diagnostic; kept separate from independent benchmark results.

[Source 1](https://arxiv.org/html/2605.02937v1)

</details>

### Biomedical visual evidence — diagnostic appendix

#### Document and figure extraction*

**Dataset/protocol:** Ryze document-extraction component tests

**Scope:** Registered · **Execution:** Status unverified

| Registered scientific setting | Execution status |
|---|---|
| Ryze extraction component tests* | Status unverified |

<details>
<summary>Scope, source protocols and published evidence</summary>

**Source size/units:** Does document/figure extraction preserve information needed for answering questions? Auxiliary component evaluation, separate from final LAB-Bench scores.

**Published evidence — not a local result:** Ryze extraction-component accuracy: ArXivQA 73.12%, SlideVQA 66.48%, ChartQA 75.8%.

Component ablation These tests evaluate extraction/document understanding, not protein engineering.

Case study or diagnostic; kept separate from independent benchmark results.

**Ryze extraction component tests**

Scientific question: Does document/figure extraction preserve information needed for answering questions?

Native metric: Dataset-specific QA accuracy

Source split: Auxiliary component evaluation, separate from final LAB-Bench scores.

Qualification: These tests evaluate extraction/document understanding, not protein engineering.

[Source 1](https://arxiv.org/html/2606.00902v1)

</details>
