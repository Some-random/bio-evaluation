# Biological evaluation overview

Model: **Qwen3.8-27B**.

Scores: **2026-10-16 04:25 UTC** · Run status: **2026-10-16 07:35 UTC**.

**25 of 64 evaluation settings have finished runs.** An asterisk (*) marks incomplete coverage or scoring.

**Listed for consideration** means additional datasets outside the original 64-setting list. **Run status unconfirmed** means no verified completion record. Published scores are reference results; full protocol notes are expandable below.

## Protein properties, interactions and developability

| Task | Dataset/protocol | Status | Qwen result | Published reference |
|---|---|---|---|---|
| Protein solubility | DeepSol solubility — PEER split | Finished | accuracy 24.2% | BioT5+: accuracy 74.37% ± 0.19 percentage points; Table 6 · [source](https://arxiv.org/html/2402.17810v2) |
| Binary protein localization | DeepLoc — binary and 10-compartment localization<br>Binary localization — DeepLoc/PEER | Finished | accuracy 27.4% | BioT5+: accuracy 90.41% ± 0.07 percentage points; Table 6 · [source](https://arxiv.org/html/2402.17810v2) |
| Ten-compartment protein localization* | DeepLoc — binary and 10-compartment localization<br>Subcellular localization — DeepLoc | Running or queued | — | Binary accuracy: BioT5+ 90.41%; BioT5 91.69%. 10-class accuracy: ProtST-ESM-2 83.39%; ESM-2 80.84%. · [source](https://arxiv.org/html/2206.02096v2) |
| Enzyme activity* | Envision β-lactamase — PEER split | Run status unconfirmed | — | Spearman: ProtST-ESM-2 0.879; ESM-2 0.867. · [source](https://arxiv.org/html/2206.02096v2) |
| Protein fluorescence* | TAPE GFP / Sarkisyan fluorescence | Running or queued | — | Spearman: ProtST-ESM-2 0.682; ESM-2 0.677. · [source](https://arxiv.org/html/2206.02096v2) |
| Protein stability* | TAPE / Rocklin stability | Running or queued | — | Spearman: ProtST-ESM-2 0.738; ESM-2 0.718. · [source](https://arxiv.org/html/2206.02096v2) |
| AAV variant fitness prediction* | FLIP — AAV and Meltome<br>AAV variant fitness — FLIP | Run status unconfirmed | — | Spearman, ProtST-ESM-2 vs ESM-2: AAV 0.825 vs 0.817; Meltome 0.682 vs 0.672. · [source](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf) |
| Protein thermostability prediction* | FLIP — AAV and Meltome<br>Thermostability — FLIP/Meltome | Partial | **Diagnostic only:** spearman undefined; spearman_parsed_only 0.0254<br>Full native primary metric undefined. | ProtST-ESM-1b: fixed encoder.spearman 0.68; full model tuning.spearman 0.681; Table 2, printed p.6 · [source](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf) |
| Human protein–protein interaction prediction | Human/Pan and yeast/Guo PPI — PEER<br>Human protein–protein interaction — PEER | Finished | accuracy 50.2% | BioT5+ (supervised): accuracy 85.09% ± 0.4 percentage points; Table 6 · [source](https://arxiv.org/html/2402.17810v2) |
| Yeast protein–protein interaction prediction | Human/Pan and yeast/Guo PPI — PEER<br>Yeast protein–protein interaction — PEER | Finished | accuracy 45.2% | BioT5+ (supervised): accuracy 66.16% ± 0.43 percentage points; Table 6 · [source](https://arxiv.org/html/2402.17810v2) |
| Protein stability classification* | NatureLM/PEER binarized stability — paper-specific protocol | Run status unconfirmed | — | NatureLM-8x7B: 72.3% accuracy; SFM-Protein-650M: 58.3%, in NatureLM's stability-classification setup. · [source](https://arxiv.org/html/2502.07527v3) |
| Antibody properties | FLAb / FLAb2 antibody property collection | Listed for consideration | — | No version-matched aggregate model score transcribed; repository supplies per-assay zero-/few-shot evaluation outputs. · [source](https://github.com/Graylab/FLAb) |
| Protein interface contacts | ATOM3D interface contacts (PIP) | Listed for consideration | — | AUROC: 3D-CNN 0.844; GNN 0.669; non-3D baseline 0.841. · [source](https://arxiv.org/html/2012.04035v3) |
| Protein solubility | PFMBench solubility panel | Listed for consideration | — | ESM2-Adapter, Table 1 means: DeepSol AUROC 0.8467; DeepSoluE AUROC 0.7699; ProtSolM AUROC 0.8572; eSOL Spearman 0.2761 · [source](https://arxiv.org/html/2506.14796v1) |
| Localization and sorting signals | PFMBench localization and sorting-signal panel | Listed for consideration | — | ESM2-Adapter, Table 1 means: DeepLocMulti Accuracy 0.7666; DeepLoc2Multi F1 0.7505; DeepLocBinary AUROC 0.9338; SortingSignal F1 0.8598 · [source](https://arxiv.org/html/2506.14796v1) |
| Protein and metal interactions | PFMBench protein and metal-interaction panel | Listed for consideration | — | ESM2-Adapter, Table 1 means: Human_PPI AUROC 0.4828; Yeast_PPI AUROC 0.5343; PPI_Affinity Spearman -0.0047; MetalIonBinding Accuracy 0.7066 · [source](https://arxiv.org/html/2506.14796v1) |
| Protein production and enzyme conditions | PFMBench production and enzyme-operating panel | Listed for consideration | — | ESM2-Adapter, Table 1 means: Optimal_pH Spearman 0.0564; DeepET_Topt Spearman 0.2628; Cloning_CLF AUROC 0.8160; Material_Production Accuracy 0.7982; Enzyme_Eff. Spearman 0.2173; Antib._Res. Accuracy 0.6185; Thermostability AUROC 0.9553 · [source](https://arxiv.org/html/2506.14796v1) |

<details>
<summary>Protocols, qualifications and complete source records</summary>

**DeepSol solubility — PEER split**

Task-trained models; BioT5+ is multitask and BioT5 single-task. Count is PEER's published split, not a new loader count.

Published source size/units: Test: 1,999 proteins. Train: 62,478; validation: 6,942 (PEER Table 1).

**Protein solubility:** Accuracy. Preserve the official PEER solubility split; exact test size not re-established.

Not binding affinity, thermostability, or a guarantee of solubility under every laboratory condition.

<details>
<summary>Solubility — PEER: protocol, counts and complete metric record</summary>

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

</details>

[Source 1](https://arxiv.org/html/2206.02096v2), [Source 2](https://arxiv.org/html/2402.17810v2), [Source 3](https://github.com/DeepGraphLearning/PEER_Benchmark)

**DeepLoc — binary and 10-compartment localization**

Binary comparison uses task-tuned systems. Ten-class numbers use frozen encoders + trained heads. These are distinct endpoints.

Published ten-class count is 2,768; the frozen local run contains 2,773 cases. These source-specific counts are retained separately.

Published source size/units: Published PEER test counts: binary 1,746; 10-compartment 2,768.

**Binary protein localization:** Accuracy. Binary task; do not substitute the separate ten-compartment label set.

'Soluble' in the localization labels is not the same endpoint as expression solubility in P01.

**Ten-compartment protein localization:** Accuracy. Official DeepLoc split. ProtST also tests zero-/few-shot transfer; record shots and whether a supervised head is fitted.

Location is a different question from molecular activity or binding specificity.

<details>
<summary>Binary localization — DeepLoc/PEER: protocol, counts and complete metric record</summary>

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

</details>

[Source 1](https://arxiv.org/html/2206.02096v2), [Source 2](https://arxiv.org/html/2402.17810v2), [Source 3](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf), [Source 4](https://github.com/DeepGraphLearning/PEER_Benchmark), [Source 5](https://github.com/DeepGraphLearning/ProtST)

**Envision β-lactamase — PEER split**

Full-model supervised fine-tuning. Assay-specific ranking, not an overall biology score.

Published source size/units: Test: 520 variants. Train: 4,158; validation: 520.

**Enzyme activity:** Spearman correlation. Official PEER beta-lactamase split.

The numerical endpoint is assay-specific; these tasks do not establish a general ability to explain mechanisms.

Published reference record: Spearman: ProtST-ESM-2 0.879; ESM-2 0.867.

[Source 1](https://arxiv.org/html/2206.02096v2), [Source 2](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf), [Source 3](https://github.com/DeepGraphLearning/PEER_Benchmark)

**TAPE GFP / Sarkisyan fluorescence**

Full-model supervised fine-tuning. Source counts are the TAPE split documented in PEER, not STRIDE's generated batch.

Published source size/units: Test: 27,217 variants. Train: 21,446; validation: 5,362.

**Protein fluorescence:** Spearman correlation. TAPE fluorescence split; sequence-distance extrapolation is part of the benchmark.

The numerical endpoint is assay-specific; these tasks do not establish a general ability to explain mechanisms.

Published reference record: Spearman: ProtST-ESM-2 0.682; ESM-2 0.677.

[Source 1](https://arxiv.org/html/2206.02096v2), [Source 2](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf), [Source 3](https://github.com/songlab-cal/tape)

**TAPE / Rocklin stability**

Full-model supervised fine-tuning. Do not conflate with NatureLM's binarized stability task.

Published source size/units: Test: 12,851 proteins. Train: 53,571; validation: 2,512.

**Protein stability:** Spearman correlation. Official TAPE stability split; retain the numerical target.

The numerical endpoint is assay-specific; these tasks do not establish a general ability to explain mechanisms.

Published reference record: Spearman: ProtST-ESM-2 0.738; ESM-2 0.718.

[Source 1](https://arxiv.org/html/2206.02096v2), [Source 2](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf), [Source 3](https://github.com/songlab-cal/tape)

**FLIP — AAV and Meltome**

Two distinct source datasets, grouped under the FLIP suite. Full-model fine-tuning; no cross-assay average added.

Published source size/units: ProtST splits: AAV two_vs_many; Meltome human_cell. Exact test counts not verified in this review.

**AAV variant fitness prediction:** Spearman correlation. FLIP AAV two_vs_many split.

The numerical endpoint is assay-specific; these tasks do not establish a general ability to explain mechanisms.

**Protein thermostability prediction:** Spearman correlation. FLIP meltome human_cell configuration.

The numerical endpoint is assay-specific; these tasks do not establish a general ability to explain mechanisms.

<details>
<summary>Thermostability — FLIP/Meltome: protocol, counts and complete metric record</summary>

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

</details>

[Source 1](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf), [Source 2](https://github.com/J-SNACKKB/FLIP), [Source 3](https://github.com/J-SNACKKB/FLIP)

**Human/Pan and yeast/Guo PPI — PEER**

Separate human/yeast negatives and splits. Generic PPI, not Affibody–pMHC specificity.

Published source size/units: Published PEER test counts: human 227 pairs; yeast 373 pairs.

**Human protein–protein interaction prediction:** Accuracy. Official human PEER PPI split; preserve negative construction.

Not TCR–pMHC specificity and not a measured dissociation constant.

**Yeast protein–protein interaction prediction:** Accuracy. Official yeast PEER PPI split; preserve negative construction.

Not TCR–pMHC specificity and not a measured dissociation constant.

<details>
<summary>Human protein–protein interaction — PEER: protocol, counts and complete metric record</summary>

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

</details>

<details>
<summary>Yeast protein–protein interaction — PEER: protocol, counts and complete metric record</summary>

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

</details>

[Source 1](https://arxiv.org/html/2206.02096v2), [Source 2](https://arxiv.org/html/2402.17810v2), [Source 3](https://github.com/DeepGraphLearning/PEER_Benchmark)

**NatureLM/PEER binarized stability — paper-specific protocol**

Keep separate from TAPE's continuous stability regression. Do not silently change the paper's endpoint.

Published source size/units: NatureLM §7.2 uses classification. Exact label-conversion rule not resolved in this review.

**Protein stability classification:** Accuracy. NatureLM §7.2 uses classification. Exact label-conversion rule not resolved in this review.

Keep separate from TAPE's continuous stability regression. Do not silently change the paper's endpoint.

Published reference record: NatureLM-8x7B: 72.3% accuracy; SFM-Protein-650M: 58.3%, in NatureLM's stability-classification setup.

[Source 1](https://arxiv.org/html/2502.07527v3), [Source 2](https://github.com/microsoft/SFM)

**FLAb / FLAb2 antibody property collection**

15 reference datasets are excluded from automated scoring; counts are corpus totals. Each assay has its own units, direction and split.

Published source size/units: Current repository: 241 datasets; >3 million assay points. Category counts 31/132/7/4/9/33/25 respectively (see details); not one held-out set.

Published reference record: No version-matched aggregate model score transcribed; repository supplies per-assay zero-/few-shot evaluation outputs.

[Source 1](https://github.com/Graylab/FLAb), [Source 2](https://github.com/Graylab/FLAb)

**ATOM3D interface contacts (PIP)**

Residue-pair contact prediction is not sequence-pair binary PPI and not binding affinity.

Published source size/units: DIPS training and DB5 testing; exact processed test count not transcribed.

Published reference record: AUROC: 3D-CNN 0.844; GNN 0.669; non-3D baseline 0.841.

[Source 1](https://arxiv.org/html/2012.04035v3), [Source 2](https://www.atom3d.ai/pip.html)

**PFMBench solubility panel**

These are PFMBench-specific processed datasets/splits, not interchangeable with PEER/ProtST results. F1 is not Fmax. Affinity-named AUROC tasks are classification, not KD regression. Exact loaders required.

Published source size/units: Test sizes: DeepSol: 6,934; DeepSoluE: 1,454; ProtSolM: 7,173; eSOL: 311

Published reference record: ESM2-Adapter, Table 1 means: DeepSol AUROC 0.8467; DeepSoluE AUROC 0.7699; ProtSolM AUROC 0.8572; eSOL Spearman 0.2761

[Source 1](https://arxiv.org/html/2506.14796v1), [Source 2](https://github.com/biomap-research/PFMBench)

**PFMBench localization and sorting-signal panel**

These are PFMBench-specific processed datasets/splits, not interchangeable with PEER/ProtST results. F1 is not Fmax. Affinity-named AUROC tasks are classification, not KD regression. Exact loaders required.

Published source size/units: Test sizes: DeepLocMulti: 751; DeepLoc2Multi: 2,744; DeepLocBinary: 848; SortingSignal: 186

Published reference record: ESM2-Adapter, Table 1 means: DeepLocMulti Accuracy 0.7666; DeepLoc2Multi F1 0.7505; DeepLocBinary AUROC 0.9338; SortingSignal F1 0.8598

[Source 1](https://arxiv.org/html/2506.14796v1), [Source 2](https://github.com/biomap-research/PFMBench)

**PFMBench protein and metal-interaction panel**

These are PFMBench-specific processed datasets/splits, not interchangeable with PEER/ProtST results. F1 is not Fmax. Affinity-named AUROC tasks are classification, not KD regression. Exact loaders required.

Published source size/units: Test sizes: Human_PPI: 195; Yeast_PPI: 335; PPI_Affinity: 326; MetalIonBinding: 718

Published reference record: ESM2-Adapter, Table 1 means: Human_PPI AUROC 0.4828; Yeast_PPI AUROC 0.5343; PPI_Affinity Spearman -0.0047; MetalIonBinding Accuracy 0.7066

[Source 1](https://arxiv.org/html/2506.14796v1), [Source 2](https://github.com/biomap-research/PFMBench)

**PFMBench production and enzyme-operating panel**

These are PFMBench-specific processed datasets/splits, not interchangeable with PEER/ProtST results. F1 is not Fmax. Affinity-named AUROC tasks are classification, not KD regression. Exact loaders required.

Published source size/units: Test sizes: Optimal_pH: 959; DeepET_Topt: 185; Cloning_CLF: 2,778; Material_Production: 2,775; Enzyme_Eff.: 1,290; Antib._Res.: 339; Thermostability: 4,184

Published reference record: ESM2-Adapter, Table 1 means: Optimal_pH Spearman 0.0564; DeepET_Topt Spearman 0.2628; Cloning_CLF AUROC 0.8160; Material_Production Accuracy 0.7982; Enzyme_Eff. Spearman 0.2173; Antib._Res. Accuracy 0.6185; Thermostability AUROC 0.9553

[Source 1](https://arxiv.org/html/2506.14796v1), [Source 2](https://github.com/biomap-research/PFMBench)

</details>

## Protein function, annotations and descriptions

| Task | Dataset/protocol | Status | Qwen result | Published reference |
|---|---|---|---|---|
| Enzyme Commission annotation* | DeepFRI-derived EC and GO test splits<br>Enzyme Commission labels — DeepFRI split | Running or queued | — | Fmax, ProtST-ESM-2 vs ESM-2: EC 0.878 vs 0.874; GO-BP 0.482 vs 0.472; GO-MF 0.668 vs 0.662; GO-CC 0.487 vs 0.472. · [source](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf) |
| Gene Ontology: biological process* | DeepFRI-derived EC and GO test splits<br>GO biological process — DeepFRI split | Running or queued | — | Fmax, ProtST-ESM-2 vs ESM-2: EC 0.878 vs 0.874; GO-BP 0.482 vs 0.472; GO-MF 0.668 vs 0.662; GO-CC 0.487 vs 0.472. · [source](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf) |
| Gene Ontology: molecular function* | DeepFRI-derived EC and GO test splits<br>GO molecular function — DeepFRI split | Running or queued | — | Fmax, ProtST-ESM-2 vs ESM-2: EC 0.878 vs 0.874; GO-BP 0.482 vs 0.472; GO-MF 0.668 vs 0.662; GO-CC 0.487 vs 0.472. · [source](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf) |
| Gene Ontology: cellular component* | DeepFRI-derived EC and GO test splits<br>GO cellular component — DeepFRI split | Running or queued | — | Fmax, ProtST-ESM-2 vs ESM-2: EC 0.878 vs 0.874; GO-BP 0.482 vs 0.472; GO-MF 0.668 vs 0.662; GO-CC 0.487 vs 0.472. · [source](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf) |
| Protein function description generation | Mol-Instructions — four protein-description subsets<br>Mol-Instructions: Protein function generation | Finished | rouge1 0.0631; rouge2 0.0139; rougeL 0.0431; rougeLsum 0.0542 | Verified numerical comparator unavailable · [source](https://arxiv.org/html/2306.08018v4) |
| Catalytic activity description generation | Mol-Instructions — four protein-description subsets<br>Mol-Instructions: Catalytic activity generation | Finished | rouge1 0.0541; rouge2 0.0140; rougeL 0.0396; rougeLsum 0.0473 | Verified numerical comparator unavailable · [source](https://arxiv.org/html/2306.08018v4) |
| Protein domain and motif description generation | Mol-Instructions — four protein-description subsets<br>Mol-Instructions: Domain and motif generation | Finished | rouge1 0.0354; rouge2 0.0047; rougeL 0.0259; rougeLsum 0.0306 | Verified numerical comparator unavailable · [source](https://arxiv.org/html/2306.08018v4) |
| Protein functional description generation | Mol-Instructions — four protein-description subsets<br>Mol-Instructions: Functional description generation | Finished | rouge1 0.0800; rouge2 0.0123; rougeL 0.0494; rougeLsum 0.0649 | Verified numerical comparator unavailable · [source](https://arxiv.org/html/2306.08018v4) |
| Protein description generation* | NatureLM's NCBI protein-description holdout | Run status unconfirmed | — | ROUGE-L: NatureLM-8x7B 0.585; fine-tuned Llama-3-8B 0.324; GPT-4o 0.091. · [source](https://arxiv.org/html/2502.07527v3) |
| Temporal Gene Ontology annotation* | BioReason-Pro temporal GO test | Running or queued | — | Official repository headline: BioReason-Pro 73.6% Fmax. · [source](https://huggingface.co/datasets/wanglab/bioreason-pro-test-data) |
| Biochemical reaction classification* | ProtST reaction classification — zero/few-shot | Running or queued | — | Zero-/few-shot results are reported, but a numeric value for the exact zero-shot reaction setting is not transcribed here. Do not substitute the fully supervised reaction score. · [source](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf) |
| Species-held-out Gene Ontology annotation* | Bio-posttrain species-held-out protein GO | Running or queued | — | Species-held-out GO evaluation is described; a verified numeric result for the exact protein split is not transcribed here. · [source](https://arxiv.org/html/2606.16517v1) |
| Enzyme and Gene Ontology annotation | PFMBench GO/EC annotation panel | Listed for consideration | — | ESM2-Adapter, Table 1 means: GO-CC F1 0.6130; GO-MF F1 0.6488; GO-BP F1 0.5412; EC F1 0.7379 · [source](https://arxiv.org/html/2506.14796v1) |
| Protein retrieval from functional descriptions* | ProtST text-to-protein retrieval examples | Run status unconfirmed | — | Selected text-to-protein retrieval and docking case studies are reported; no single fixed-corpus Recall@K benchmark result is transcribed. · [source](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf) |
| Evidence support for protein-function explanations* | BioReason-Pro explanation review | Run status unconfirmed | — | Repository reports an LLM-judge score of 8/10 and expert preference over UniProt descriptions in 79% of reviewed cases. · [source](https://www.biorxiv.org/content/10.64898/2026.03.19.712954v2.full) |

<details>
<summary>Protocols, qualifications and complete source records</summary>

**DeepFRI-derived EC and GO test splits**

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

Published reference record: Fmax, ProtST-ESM-2 vs ESM-2: EC 0.878 vs 0.874; GO-BP 0.482 vs 0.472; GO-MF 0.668 vs 0.662; GO-CC 0.487 vs 0.472.

[Source 1](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf), [Source 2](https://github.com/DeepGraphLearning/ProtST)

**Mol-Instructions — four protein-description subsets**

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

<details>
<summary>Mol-Instructions: Protein function generation: protocol, counts and complete metric record</summary>

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

</details>

<details>
<summary>Mol-Instructions: Catalytic activity generation: protocol, counts and complete metric record</summary>

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

</details>

<details>
<summary>Mol-Instructions: Domain and motif generation: protocol, counts and complete metric record</summary>

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

</details>

<details>
<summary>Mol-Instructions: Functional description generation: protocol, counts and complete metric record</summary>

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

</details>

[Source 1](https://arxiv.org/html/2306.08018v4), [Source 2](https://raw.githubusercontent.com/zjunlp/Mol-Instructions/main/README.md), [Source 3](https://arxiv.org/html/2402.17810v2), [Source 4](https://github.com/zjunlp/Mol-Instructions)

**NatureLM's NCBI protein-description holdout**

This is a paper-specific NCBI-derived set, not all NCBI data. Different task-training regimes; text-overlap evaluation.

Published source size/units: Temporal split; exact test count and frozen processed release not recovered.

**Protein description generation:** ROUGE-L. Paper reports a temporal split; exact frozen test release/count not recovered.

Do not replace its temporal test with arbitrary UniProt rows and claim exact reproduction.

Published reference record: ROUGE-L: NatureLM-8x7B 0.585; fine-tuned Llama-3-8B 0.324; GPT-4o 0.091.

[Source 1](https://arxiv.org/html/2502.07527v3), [Source 2](https://github.com/microsoft/SFM)

**BioReason-Pro temporal GO test**

Headline aggregation; exact BP/MF/CC definition must come from official evaluator. Not interchangeable with species-held-out evaluation.

Published source size/units: Released test: 8,630 proteins.

**Temporal Gene Ontology annotation:** Fmax; information-accretion-weighted Fmax. Released test data: 8,630 proteins; preserve the specified temporal and annotation cutoffs.

No observed label is not proof of no function. Separate predicted context from gold annotations.

Published reference record: Official repository headline: BioReason-Pro 73.6% Fmax.

[Source 1](https://huggingface.co/datasets/wanglab/bioreason-pro-test-data), [Source 2](https://raw.githubusercontent.com/bowang-lab/BioReason-Pro/main/README.md), [Source 3](https://huggingface.co/datasets/wanglab/bioreason-pro-test-data)

**ProtST reaction classification — zero/few-shot**

Zero-shot text-label matching is not the same protocol as fitting a fully supervised classifier.

Published source size/units: ProtST zero-shot/few-shot experiment; shots and ensemble settings must be recorded.

**Biochemical reaction classification:** Accuracy. ProtST zero-shot/few-shot experiment; shots and ensemble settings must be recorded.

Zero-shot text-label matching is not the same protocol as fitting a fully supervised classifier.

Published reference record: Zero-/few-shot results are reported, but a numeric value for the exact zero-shot reaction setting is not transcribed here. Do not substitute the fully supervised reaction score.

[Source 1](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf), [Source 2](https://github.com/DeepGraphLearning/ProtST)

**Bio-posttrain species-held-out protein GO**

Do not substitute the original BioReason-Pro 8,630-protein split or its Fmax scorer without documenting the change.

Author resolve_gold_terms_from_row unions curated leaf/ancestor fields AND go_pred_leaf while go_pred is supplied as context. Native reference and input are dependent: the metric can reward recovery/copying of supplied predictions and does not isolate novel function inference. Preserve that augmented target as primary; curated-only reference union is a separate fixed diagnostic, also with predictor overlap and unknown historical independence. Never select the more favorable metric or remove native context.

Published source size/units: Two held-out species in the paper; exact species/counts not established in this review. Also discusses inherited temporal protocol.

**Species-held-out Gene Ontology annotation:** Propagated GO-F1. Two held-out species in the paper; exact species/counts not established in this review. Also discusses inherited temporal protocol.

Do not substitute the original BioReason-Pro 8,630-protein split or its Fmax scorer without documenting the change.

Published reference record: Species-held-out GO evaluation is described; a verified numeric result for the exact protein split is not transcribed here.

[Source 1](https://arxiv.org/html/2606.16517v1), [Source 2](https://github.com/mims-harvard/bio-posttrain)

**PFMBench GO/EC annotation panel**

These are PFMBench-specific processed datasets/splits, not interchangeable with PEER/ProtST results. F1 is not Fmax. Affinity-named AUROC tasks are classification, not KD regression. Exact loaders required.

Published source size/units: Test sizes: GO-CC: 1,400; GO-MF: 2,787; GO-BP: 2,664; EC: 1,604

Published reference record: ESM2-Adapter, Table 1 means: GO-CC F1 0.6130; GO-MF F1 0.6488; GO-BP F1 0.5412; EC F1 0.7379

[Source 1](https://arxiv.org/html/2506.14796v1), [Source 2](https://github.com/biomap-research/PFMBench)

**ProtST text-to-protein retrieval examples**

Retrieval case study Docking and known annotations support case analysis; they do not prove all retrieved candidates bind experimentally.

Published source size/units: Can a functional description retrieve relevant proteins? Selected queries such as heme binding; not a universal, fixed retrieval benchmark with one headline Recall@K.

**Protein retrieval from functional descriptions:** Top-retrieval inspection; docking scores in case studies. Selected queries such as heme binding; not a universal, fixed retrieval benchmark with one headline Recall@K.

Docking and known annotations support case analysis; they do not prove all retrieved candidates bind experimentally.

Published reference record: Selected text-to-protein retrieval and docking case studies are reported; no single fixed-corpus Recall@K benchmark result is transcribed.

[Source 1](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf)

**BioReason-Pro explanation review**

Judged explanation subset Correct GO labels do not guarantee that every intermediate statement is true.

Published source size/units: Are the generated functional explanations helpful and consistent with the reference evidence? Separate from the 8,630-protein GO-label metric; exact scored explanation subset not established here.

**Evidence support for protein-function explanations:** Judge rubrics; qualitative/expert review. Separate from the 8,630-protein GO-label metric; exact scored explanation subset not established here.

Correct GO labels do not guarantee that every intermediate statement is true.

Published reference record: Repository reports an LLM-judge score of 8/10 and expert preference over UniProt descriptions in 79% of reviewed cases.

[Source 1](https://www.biorxiv.org/content/10.64898/2026.03.19.712954v2.full)

</details>

## Mutation-effect interpretation

| Task | Dataset/protocol | Status | Qwen result | Published reference |
|---|---|---|---|---|
| Mutation-effect explanation* | MutaDescribe — mutation explanation | Run status unconfirmed | — | Main-test average ROUGE-L / BLEU-2 (0–100): MutaPLM 21.34 / 13.61; GPT-4-0613, 5-shot kNN: 12.31 / 9.69. · [source](https://arxiv.org/html/2410.22949v1) |

<details>
<summary>Protocols, qualifications and complete source records</summary>

**MutaDescribe — mutation explanation**

The reported 'Average' is retained as the paper defines it. Similarity tiers are not a globally homology-disjoint split.

Published source size/units: Main test: Easy 460; Medium 384; Hard 404 mutation examples. Separate temporal test: 1,611 (not the reported main averages).

**Mutation-effect explanation:** BLEU-2; ROUGE-L; GPT-4-plus-human categorical review. Random split then similarity tiers: Easy 460, Medium 384, Hard 404. Separate temporal test has 1,611 examples.

Similarity tiers do not make the entire split homology-disjoint. Judge output is not independent experimental verification.

Published reference record: Main-test average ROUGE-L / BLEU-2 (0–100): MutaPLM 21.34 / 13.61; GPT-4-0613, 5-shot kNN: 12.31 / 9.69.

[Source 1](https://arxiv.org/html/2410.22949v1), [Source 2](https://huggingface.co/datasets/PharMolix/MutaDescribe)

</details>

## Mutation ranking, affinity and local optimization

| Task | Dataset/protocol | Status | Qwen result | Published reference |
|---|---|---|---|---|
| Mutation-effect ranking* | ProteinGym substitutions — historical ProtST evaluation | Run status unconfirmed | — | UniProt-level mean Spearman: ProtST-ESM-1b 0.412; ESM-1b 0.358; ESM-1v 0.372; Tranception L without retrieval 0.401. · [source](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf) |
| Mutation-effect ranking* | PG-LLM / ProteinGym-LLM — eval-data-v1.2 | On hold | — | No verified release-matched model score was recovered. This does not mean zero performance. · [source](https://raw.githubusercontent.com/rohitarorayyc/proteingym-llm/main/DATA.md) |
| Single-mutant generation* | PFArena — four task settings<br>PFArena T1: single-mutant generation | Blocked | — | Paper's GPT-6 Astra vs ESM-2: T1 Recall@40 0.0254 vs 0.0370; T2 Spearman 0.2726 vs 0.2539; T3 0.3516 vs 0.3128; T4 0.5988 vs 0.3153. · [source](https://arxiv.org/html/2609.28921v1) |
| Multi-mutant ranking without measurements* | PFArena — four task settings<br>PFArena T2: measurement-free multi-mutant ranking | Blocked | — | Paper's GPT-6 Astra vs ESM-2: T1 Recall@40 0.0254 vs 0.0370; T2 Spearman 0.2726 vs 0.2539; T3 0.3516 vs 0.3128; T4 0.5988 vs 0.3153. · [source](https://arxiv.org/html/2609.28921v1) |
| Mutation ranking with anchor measurements* | PFArena — four task settings<br>PFArena T3: anchor-informed ranking | Blocked | — | Paper's GPT-6 Astra vs ESM-2: T1 Recall@40 0.0254 vs 0.0370; T2 Spearman 0.2726 vs 0.2539; T3 0.3516 vs 0.3128; T4 0.5988 vs 0.3153. · [source](https://arxiv.org/html/2609.28921v1) |
| Mutation ranking with single-mutant measurements* | PFArena — four task settings<br>PFArena T4: single-mutant-informed ranking | Blocked | — | Paper's GPT-6 Astra vs ESM-2: T1 Recall@40 0.0254 vs 0.0370; T2 Spearman 0.2726 vs 0.2539; T3 0.3516 vs 0.3128; T4 0.5988 vs 0.3153. · [source](https://arxiv.org/html/2609.28921v1) |
| Mutation engineering with a supplied position* | MutaDescribe — mutation engineering<br>MutaDescribe mutation engineering — position supplied | Run status unconfirmed | — | MutaPLM vs fine-tuned ESM-2: position known accuracy 53.51% vs 51.43%; position unknown Recall@50 40.94% vs 33.77%. · [source](https://arxiv.org/html/2410.22949v1) |
| Mutation engineering with an unknown position* | MutaDescribe — mutation engineering<br>MutaDescribe mutation engineering — position unknown | Run status unconfirmed | — | MutaPLM vs fine-tuned ESM-2: position known accuracy 53.51% vs 51.43%; position unknown Recall@50 40.94% vs 33.77%. · [source](https://arxiv.org/html/2410.22949v1) |
| Low-data fitness regression* | MutaPLM low-data fitness regression | Run status unconfirmed | — | Low-data regression curves are reported with 192 train / 48 validation examples; no exact assay-specific point estimate is transcribed here. · [source](https://arxiv.org/html/2410.22949v1) |
| Antibody affinity ranking | AbBiBench antibody affinity ranking | Listed for consideration | — | Current 16-column leaderboard mean Spearman: ProteinMPNN 0.30; ESM-IF1 0.28; AntiFold 0.21; ESM2 0.02. · [source](https://github.com/MSBMI-SAFE/AbBiBench) |
| Mutation effects on binding affinity | ATOM3D SKEMPI-derived mutation affinity (MSP) | Listed for consideration | — | AUROC: GNN 0.621; 3D-CNN 0.574. · [source](https://arxiv.org/html/2012.04035v3) |
| Mutation and fitness prediction | PFMBench mutation/fitness panel | Listed for consideration | — | ESM2-Adapter, Table 1 means: PETA_CHS_SOL Spearman 0.2738; PETA_LGK_SOL Spearman 0.1558; PETA_TEM_SOL Spearman 0.1433; FLIP_AAV Spearman 0.9412; FLIP_GB1 Spearman 0.9517; TAPE_Stab Spearman 0.3211; TAPE_Fluor Spearman 0.6812; BetaLactamase Spearman 0.5740 · [source](https://arxiv.org/html/2506.14796v1) |
| Peptide–MHC and TCR–pMHC interactions | PFMBench peptide–MHC and TCR–pMHC panel | Listed for consideration | — | ESM2-Adapter, Table 1 means: Pept.HLA/MHC Aff. AUROC 0.9631; TCR.PMHC Aff. AUROC 0.9312 · [source](https://arxiv.org/html/2506.14796v1) |
| Zero-shot mutation-effect ranking | PFMBench ProteinGym zero-shot protocol | Listed for consideration | — | Table 1 reports pretrained ESM2 ProteinGym Spearman 0.4390; do not compare directly to a different snapshot's score. · [source](https://arxiv.org/html/2506.14796v1) |
| Protein-sequence optimization against fitness predictors*<br>Predictor-scored optimization; not measured laboratory success. | MutaPLM iterative optimization | Run status unconfirmed | — | The paper reports predicted-fitness improvement trajectories across six landscapes; these are oracle-based search outcomes, not experimentally measured hit rates. · [source](https://arxiv.org/html/2410.22949v1) |

<details>
<summary>Protocols, qualifications and complete source records</summary>

**ProteinGym substitutions — historical ProtST evaluation**

NEW verified numeric row from ProtST Table 12. Not a current ProteinGym leaderboard result.

Published source size/units: Use the historical ProteinGym snapshot in ProtST. Do not attach the modern 217-assay count to these old results.

**Mutation-effect ranking:** Spearman primary; suite also reports ranking/classification summaries. Pin release: modern v1.3 substitution subset has 217 assays; an older paper may use an earlier snapshot.

Score within each assay. Different assay scores are not a shared physical unit; fitness is not always binding.

Published reference record: UniProt-level mean Spearman: ProtST-ESM-1b 0.412; ESM-1b 0.358; ESM-1v 0.372; Tranception L without retrieval 0.401.

[Source 1](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf), [Source 2](https://github.com/OATML-Markslab/ProteinGym), [Source 3](https://github.com/OATML-Markslab/ProteinGym)

**PG-LLM / ProteinGym-LLM — eval-data-v1.2**

Evaluation-only frozen protocol. Benchmark-specific training, tuning and retrieval augmentation are restricted by its documentation.

Published source size/units: 217 assays; sets of 10, 50 or 100 variants; three seeds.

**Mutation-effect ranking:** Per-assay Spearman. eval-data-v1.2: 217 assays; N=10/50/100; seeds 1/2/3; labels separate from model-facing inputs.

Evaluation-only: do not train, tune prompts, distill or perform retrieval augmentation using these candidate sets/labels.

Published reference record: No verified release-matched model score was recovered. This does not mean zero performance.

[Source 1](https://raw.githubusercontent.com/rohitarorayyc/proteingym-llm/main/DATA.md), [Source 2](https://github.com/rohitarorayyc/proteingym-llm/blob/main/DATA.md)

**PFArena — four task settings**

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

Published reference record: Paper's GPT-6 Astra vs ESM-2: T1 Recall@40 0.0254 vs 0.0370; T2 Spearman 0.2726 vs 0.2539; T3 0.3516 vs 0.3128; T4 0.5988 vs 0.3153.

[Source 1](https://arxiv.org/html/2609.28921v1), [Source 2](https://arxiv.org/html/2609.28921v1)

**MutaDescribe — mutation engineering**

Same source dataset, different task. These are reference-recovery rates, not prospective wet-lab success.

Published source size/units: Same main Easy/Medium/Hard split as explanation: 460 / 384 / 404 examples.

**Mutation engineering with a supplied position:** Accuracy. Same similarity/temporal splits as MutaDescribe; supplied position simplifies the task.

Recovery of one annotated mutation is not the fraction of novel designs that work.

**Mutation engineering with an unknown position:** Recall@50. Search covers 19 × sequence-length substitutions; preserve the paper's candidate definition.

A different useful but unannotated mutation can score as a miss.

Published reference record: MutaPLM vs fine-tuned ESM-2: position known accuracy 53.51% vs 51.43%; position unknown Recall@50 40.94% vs 33.77%.

[Source 1](https://arxiv.org/html/2410.22949v1), [Source 2](https://huggingface.co/datasets/PharMolix/MutaDescribe)

**MutaPLM low-data fitness regression**

This is supervised low-N prediction, not zero-shot generation. Do not reuse the labeled seed points as test examples.

Published source size/units: 192 training + 48 validation examples; five seeds; assay-specific remaining test records

**Low-data fitness regression:** Spearman. 192 training and 48 validation samples; five random seeds. Remaining held-out data evaluated per source.

This is supervised low-N prediction, not zero-shot generation. Do not reuse the labeled seed points as test examples.

Published reference record: Low-data regression curves are reported with 192 train / 48 validation examples; no exact assay-specific point estimate is transcribed here.

[Source 1](https://arxiv.org/html/2410.22949v1), [Source 2](https://github.com/PharMolix/MutaPLM)

**AbBiBench antibody affinity ranking**

Paper size and current leaderboard refer to different snapshots. Do not combine them into a single size-matched result. Generative case study is separate.

Published source size/units: Paper: 155,853 heavy-chain variants, 9 antigens (Section 3.1 lists 11 datasets). Current repository leaderboard: 16 assay columns; expanded payload count not established.

Published reference record: Current 16-column leaderboard mean Spearman: ProteinMPNN 0.30; ESM-IF1 0.28; AntiFold 0.21; ESM2 0.02.

[Source 1](https://github.com/MSBMI-SAFE/AbBiBench), [Source 2](https://arxiv.org/html/2506.04235v1), [Source 3](https://huggingface.co/datasets/AbBibench/Antibody_Binding_Benchmark_Dataset)

**ATOM3D SKEMPI-derived mutation affinity (MSP)**

This is binding-affinity change classification, not folding-stability prediction. Source counts are not test counts.

Published source size/units: Source construction: 893 positive and 3,255 negative mutations; exact test size not recovered.

Published reference record: AUROC: GNN 0.621; 3D-CNN 0.574.

[Source 1](https://arxiv.org/html/2012.04035v3), [Source 2](https://www.atom3d.ai/msp.html)

**PFMBench mutation/fitness panel**

These are PFMBench-specific processed datasets/splits, not interchangeable with PEER/ProtST results. F1 is not Fmax. Affinity-named AUROC tasks are classification, not KD regression. Exact loaders required.

Published source size/units: Test sizes: PETA_CHS_SOL: 484; PETA_LGK_SOL: 1,914; PETA_TEM_SOL: 808; FLIP_AAV: 16,517; FLIP_GB1: 1,745; TAPE_Stab: 6,898; TAPE_Fluor: 27,217; BetaLactamase: 520

Published reference record: ESM2-Adapter, Table 1 means: PETA_CHS_SOL Spearman 0.2738; PETA_LGK_SOL Spearman 0.1558; PETA_TEM_SOL Spearman 0.1433; FLIP_AAV Spearman 0.9412; FLIP_GB1 Spearman 0.9517; TAPE_Stab Spearman 0.3211; TAPE_Fluor Spearman 0.6812; BetaLactamase Spearman 0.5740

[Source 1](https://arxiv.org/html/2506.14796v1), [Source 2](https://github.com/biomap-research/PFMBench)

**PFMBench peptide–MHC and TCR–pMHC panel**

These are PFMBench-specific processed datasets/splits, not interchangeable with PEER/ProtST results. F1 is not Fmax. Affinity-named AUROC tasks are classification, not KD regression. Exact loaders required.

Published source size/units: Test sizes: Pept.HLA/MHC Aff.: 8,406; TCR.PMHC Aff.: 2,482

Published reference record: ESM2-Adapter, Table 1 means: Pept.HLA/MHC Aff. AUROC 0.9631; TCR.PMHC Aff. AUROC 0.9312

[Source 1](https://arxiv.org/html/2506.14796v1), [Source 2](https://github.com/biomap-research/PFMBench)

**PFMBench ProteinGym zero-shot protocol**

These are PFMBench-specific processed datasets/splits, not interchangeable with PEER/ProtST results. F1 is not Fmax. Affinity-named AUROC tasks are classification, not KD regression. Exact loaders required.

Published source size/units: Paper table does not specify the release-matched evaluation denominator.

Published reference record: Table 1 reports pretrained ESM2 ProteinGym Spearman 0.4390; do not compare directly to a different snapshot's score.

[Source 1](https://arxiv.org/html/2506.14796v1), [Source 2](https://github.com/biomap-research/PFMBench)

**MutaPLM iterative optimization**

Predictor-scored search experiment A learned scorer can be exploited; this experiment is not prospective laboratory success.

Published source size/units: Do iterative proposals improve the predicted assay objective? Six landscapes: AAV, AMIE, avGFP, E4B, LGK, UBE2I; 20 independent runs; preserve beam/search settings.

**Protein-sequence optimization against fitness predictors:** Mean predicted fitness trajectory and dispersion. Six landscapes: AAV, AMIE, avGFP, E4B, LGK, UBE2I; 20 independent runs; preserve beam/search settings.

A learned scorer can be exploited; this experiment is not prospective laboratory success.

Published reference record: The paper reports predicted-fitness improvement trajectories across six landscapes; these are oracle-based search outcomes, not experimentally measured hit rates.

[Source 1](https://arxiv.org/html/2410.22949v1)

</details>

## Scientific evidence and biological knowledge

| Task | Dataset/protocol | Status | Qwen result | Published reference |
|---|---|---|---|---|
| Literature evidence question answering* | LAB-Bench — research tasks<br>LAB-Bench / LitQA2 | Partial | accuracy 39.1%; precision 41.0%; coverage 95.4% | GPT-5.2: accuracy 45.7%; n=199; Table 1 · [source](https://arxiv.org/html/2606.00902v1) |
| Biological database question answering | LAB-Bench — research tasks<br>LAB-Bench / DbQA | Finished | accuracy 31.3%; precision 31.8%; coverage 98.5% | GPT-5.2: accuracy 41.7%; n=520; Table 1 · [source](https://arxiv.org/html/2606.00902v1) |
| Supplementary-material question answering | LAB-Bench — research tasks<br>LAB-Bench / SuppQA | Finished | accuracy 34.1%; precision 35.9%; coverage 95.1% | GPT-5.2: accuracy 48.8%; n=82; Table 1 · [source](https://arxiv.org/html/2606.00902v1) |
| Research figure question answering | LAB-Bench — research tasks<br>LAB-Bench / FigQA | Finished | accuracy 75.7%; precision 77.0%; coverage 98.3% | GPT-5.2: accuracy 36.5%; n=181; Table 1 · [source](https://arxiv.org/html/2606.00902v1) |
| Research table question answering | LAB-Bench — research tasks<br>LAB-Bench / TableQA | Finished | accuracy 88.5%; precision 90.0%; coverage 98.4% | GPT-5.2: accuracy 36.9%; n=244; Table 1 · [source](https://arxiv.org/html/2606.00902v1) |
| Experimental protocol question answering* | LAB-Bench — research tasks<br>LAB-Bench / ProtocolQA | On hold | — | Historical 2024 GPT-4o accuracy: LitQA2 27%; SuppQA 13%; FigQA 29%; TableQA 71%; ProtocolQA 53%; Cloning 28%. DbQA variant-from-sequence 42%; SeqQA GC% 29%, ORF-sequence 50% (SUBTASK values only). · [source](https://arxiv.org/html/2407.10362v1) |
| Biological sequence question answering | LAB-Bench — research tasks<br>LAB-Bench / SeqQA | Finished | accuracy 12.7%; precision 12.8%; coverage 99.2% | GPT-5.2: accuracy 47.0%; n=600; Table 1 · [source](https://arxiv.org/html/2606.00902v1) |
| Molecular cloning question answering | LAB-Bench — research tasks<br>LAB-Bench / Cloning scenarios | Finished | accuracy 0.0%; precision 0.0%; coverage 100.0% | GPT-5.2: accuracy 36.4%; n=33; Table 1 · [source](https://arxiv.org/html/2606.00902v1) |
| Protein understanding | ProteinLMBench protein-understanding questions | Listed for consideration | — | InternLM2-7B after SFT: 58.26% accuracy; SSL+SFT: 62.18%. · [source](https://arxiv.org/html/2406.05540v1) |
| Research-abstract question answering | PubMedQA research-abstract questions | Listed for consideration | — | Original BioBERT multi-phase training: 68.1% accuracy; reported human baseline 78.0%. Historical results. · [source](https://arxiv.org/abs/1909.06146) |

<details>
<summary>Protocols, qualifications and complete source records</summary>

**LAB-Bench — research tasks**

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

<details>
<summary>LAB-Bench / LitQA2: protocol, counts and complete metric record</summary>

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

</details>

<details>
<summary>LAB-Bench / DbQA: protocol, counts and complete metric record</summary>

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

</details>

<details>
<summary>LAB-Bench / SuppQA: protocol, counts and complete metric record</summary>

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

</details>

<details>
<summary>LAB-Bench / FigQA: protocol, counts and complete metric record</summary>

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

</details>

<details>
<summary>LAB-Bench / TableQA: protocol, counts and complete metric record</summary>

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

</details>

<details>
<summary>LAB-Bench / SeqQA: protocol, counts and complete metric record</summary>

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

</details>

<details>
<summary>LAB-Bench / Cloning scenarios: protocol, counts and complete metric record</summary>

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

</details>

[Source 1](https://arxiv.org/html/2407.10362v1), [Source 2](https://huggingface.co/datasets/futurehouse/lab-bench)

**ProteinLMBench protein-understanding questions**

Knowledge/test-taking evaluation, not direct novel protein-function prediction.

Published source size/units: 944 manually verified questions; six choices per question.

Published reference record: InternLM2-7B after SFT: 58.26% accuracy; SSL+SFT: 62.18%.

[Source 1](https://arxiv.org/html/2406.05540v1), [Source 2](https://huggingface.co/datasets/tsynbio/ProteinLMBench)

**PubMedQA research-abstract questions**

The conclusion/long answer must stay out of solver input under the reasoning-required protocol.

Published source size/units: 1,000 expert-labeled records total; official evaluation split must be pinned. 61.2K unlabeled and 211.3K artificial records are separate training resources.

Published reference record: Original BioBERT multi-phase training: 68.1% accuracy; reported human baseline 78.0%. Historical results.

[Source 1](https://arxiv.org/abs/1909.06146), [Source 2](https://github.com/pubmedqa/pubmedqa)

</details>

## Protein design

| Task | Dataset/protocol | Status | Qwen result | Published reference |
|---|---|---|---|---|
| Antibody design: CDR-H3 redesign* | RAbD — CDR-H3 redesign | Run status unconfirmed | — | Proteo-R1 vs BoltzGen: AAR 10.75% vs 39.07%; RMSD 2.46 Å vs 2.69 Å; DockQ 0.801 vs 0.473. · [source](https://arxiv.org/html/2605.02937v1) |
| Antibody design: multi-CDR redesign* | SAbDab — Proteo-R1 all-CDR holdout | Run status unconfirmed | — | Proteo-R1 vs MFDesign: H3 RMSD 3.81 Å vs 3.71 Å; Loop-RMSD 4.51 Å vs 4.28 Å; IMP 56.58 vs 59.16 (paper's scale). · [source](https://arxiv.org/html/2605.02937v1) |
| Sequence design by inverse folding | CATH 4.2 / TS50 / TS500 inverse folding | Listed for consideration | — | PiFold repository: CATH recovery 51.66%; TS50 58.72%; TS500 60.42%. · [source](https://github.com/a4bio/pifold) |
| Sequence design by inverse folding | ProteinBench inverse folding — CASP15 / CAMEO / synthetic backbones | Listed for consideration | — | AAR, CASP15/CAMEO: LM-Design 0.516/0.570; ProteinMPNN 0.450/0.468. · [source](https://arxiv.org/html/2409.06744v2) |
| Unconditional protein backbone generation | ProteinBench unconditional backbone generation | Listed for consideration | — | At length 100: RFdiffusion scTM 0.98 ± 0.12 and scRMSD 0.48 ± 0.56 Å; FrameFlow 0.94 ± 0.08 and 0.70 ± 0.70 Å. · [source](https://arxiv.org/html/2409.06744v2) |
| Unconditional protein sequence generation | ProteinBench unconditional sequence generation | Listed for consideration | — | At length 100, predicted AF2 pLDDT: DPLM-650M 85.38 ± 14.20; ProGen2-700M 64.00 ± 21.26. · [source](https://arxiv.org/html/2409.06744v2) |
| Joint sequence and structure generation | ProteinBench joint sequence–structure generation | Listed for consideration | — | Multiflow at length 100: scTM 0.96 ± 0.04; scRMSD 1.10 ± 0.71 Å. At length 200: scTM 0.95; scRMSD 1.61 Å. · [source](https://arxiv.org/html/2409.06744v2) |
| Functional-motif scaffolding | MotifBench functional-motif scaffolding | Listed for consideration | — | Official leaderboard snapshot: RFdiffusion3 43.52 ± 1.35 (Aug 2026); RFdiffusion 21.95 (Feb 2025), in MotifBench-score units. · [source](https://github.com/blt2114/MotifBench) |
| Functional-motif scaffolding | ProteinBench motif scaffolding — legacy motif panel | Listed for consideration | — | Comparative motif-scaffolding results are reported; exact figure-derived score not transcribed. · [source](https://arxiv.org/html/2409.06744v2) |
| Antibody design: CDR-H3 redesign | ProteinBench antibody design — processed RAbD | Listed for consideration | — | DiffAb: AAR 35.04 ± 8.36%, RMSD 2.53 ± 0.60 Å; MEAN: AAR 33.47%, RMSD 1.82 Å. · [source](https://arxiv.org/html/2409.06744v2) |
| Antibody design: epitope-conditioned design | CHIMERA-Bench epitope-conditioned antibody design | Listed for consideration | — | Epitope-group H3: RAAD AAR 0.37, RMSD 1.75 Å, DockQ 0.58; dyMEAN EpiF1 0.23 (RAAD 0.11). · [source](https://arxiv.org/html/2603.13431v1) |
| Target-binder design | ProtDBench de novo target-binder design | Listed for consideration | — | PD-L1 passing-backbone counts: PXDesign 1,247; BoltzGen 549; RFdiffusion3 542; BindCraft 231. TNFα: PXDesign 57; BoltzGen 15. · [source](https://arxiv.org/html/2605.04118v1) |
| Text-conditioned protein-sequence design*<br>Qualitative designs; no measured design-success rate. | BioT5+ description-guided protein generation | Run status unconfirmed | — | Description-guided protein designs are presented as qualitative cases rather than a fixed, experimentally validated design-success rate. · [source](https://arxiv.org/html/2402.17810v2) |
| Unconditional protein generation*<br>Structure quality is predicted; function is not experimentally established. | NatureLM generated proteins: unconditional / property-conditioned / heme<br>NatureLM unconditional generation | Run status unconfirmed | — | Reported outputs are diversity/length distributions and predicted structural confidence. No experimentally measured function-success fraction is supplied by this evaluation. The reported comparison uses learned stability/solubility scores and diversity. No measured stability/solubility success rate is transcribed. Selected heme-binding candidates are screened with descriptions and predicted complexes; this is not experimentally demonstrated heme binding. · [source](https://arxiv.org/html/2502.07527v3) |
| Protein generation for predicted stability and solubility*<br>Stability and solubility are predicted, not measured. | NatureLM generated proteins: unconditional / property-conditioned / heme<br>NatureLM stability/solubility-conditioned generation | Run status unconfirmed | — | Reported outputs are diversity/length distributions and predicted structural confidence. No experimentally measured function-success fraction is supplied by this evaluation. The reported comparison uses learned stability/solubility scores and diversity. No measured stability/solubility success rate is transcribed. Selected heme-binding candidates are screened with descriptions and predicted complexes; this is not experimentally demonstrated heme binding. · [source](https://arxiv.org/html/2502.07527v3) |
| Heme-binding protein candidate generation*<br>Heme binding is a predicted candidate property, not demonstrated binding. | NatureLM generated proteins: unconditional / property-conditioned / heme<br>NatureLM heme-binding case study | Run status unconfirmed | — | Reported outputs are diversity/length distributions and predicted structural confidence. No experimentally measured function-success fraction is supplied by this evaluation. The reported comparison uses learned stability/solubility scores and diversity. No measured stability/solubility success rate is transcribed. Selected heme-binding candidates are screened with descriptions and predicted complexes; this is not experimentally demonstrated heme binding. · [source](https://arxiv.org/html/2502.07527v3) |
| GFP sequence optimization against a fluorescence predictor*<br>Scored by a fluorescence predictor; not a wet-lab result. | STRIDE GFP sequence optimization | Partial | replace_only.qualified_oracle_success 0.0000; replace_only.improved_sequence_uniqueness undefined; replace_only.native_novelty undefined; full_atomic.qualified_oracle_success 0.0000; full_atomic.improved_sequence_uniqueness undefined; full_atomic.native_novelty undefined | STRIDE: success count 61; attempt count 100; unique improved count 59; n=100; Table 4 · [source](https://arxiv.org/html/2603.03573v1) |
| GM2A-targeted binder design<br>Single published target campaign. | Prompteina text-conditioned protein design — GM2A campaign | Listed for consideration | — | 9 of 89 assayed designs classified as binders; 8 fitted apparent KD values. Strongest apparent KD: 107 nM. · [source](https://arxiv.org/html/2610.13917v1) |

<details>
<summary>Protocols, qualifications and complete source records</summary>

**RAbD — CDR-H3 redesign**

Geometry and native-sequence recovery disagree; no dominance claim across all metrics. Not prospective binding success. ProteinBench's 55-complex processed version is separately listed.

Published source size/units: 60 antibody–antigen complexes.

**Antibody design: CDR-H3 redesign:** NatureLM: AAR. Proteo-R1: AAR, RMSD, lDDT, TM-score, DockQ.. 60 complexes; retain paper-specific renumbering, masked region and preprocessing.

High native recovery or geometric similarity does not imply measured binding for a new design.

Published reference record: Proteo-R1 vs BoltzGen: AAR 10.75% vs 39.07%; RMSD 2.46 Å vs 2.69 Å; DockQ 0.801 vs 0.473.

[Source 1](https://arxiv.org/html/2605.02937v1), [Source 2](https://arxiv.org/html/2605.02937v1)

**SAbDab — Proteo-R1 all-CDR holdout**

One dataset, multiple metrics. H3 RMSD and Loop-RMSD are different columns. Oracle-Anchor row is not the deployed system.

Published source size/units: Paper-specific temporal/cluster split; exact processed test count not recovered.

**Antibody design: multi-CDR redesign:** Structural/recovery/interface metrics; Rosetta-derived energy and clash diagnostics. Release-time filtering and 50%-identity H3 clusters; 9:0.5:0.5 cluster split. Exact test count not established.

Computational reconstruction/design. The original docking pose is assumed known; not unconstrained binder discovery.

Published reference record: Proteo-R1 vs MFDesign: H3 RMSD 3.81 Å vs 3.71 Å; Loop-RMSD 4.51 Å vs 4.28 Å; IMP 56.58 vs 59.16 (paper's scale).

[Source 1](https://arxiv.org/html/2605.02937v1), [Source 2](https://arxiv.org/html/2605.02937v1)

**CATH 4.2 / TS50 / TS500 inverse folding**

Recovery is not experimental fold/function validation; named size does not replace retained-record manifest.

Published source size/units: CATH 4.2 exact test count not re-established; TS50/TS500 named test suites (50/500 nominal structures; exact retained manifests must be checked).

Published reference record: PiFold repository: CATH recovery 51.66%; TS50 58.72%; TS500 60.42%.

[Source 1](https://github.com/a4bio/pifold), [Source 2](https://github.com/a4bio/pifold)

**ProteinBench inverse folding — CASP15 / CAMEO / synthetic backbones**

Some models are excluded from native recovery because of training exposure. Synthetic consistency is model-scored, not wet-lab.

Published source size/units: 32 CASP15 structures; 332 CAMEO complexes; synthetic backbones: 10 at each of 5 lengths (100–500 aa).

Published reference record: AAR, CASP15/CAMEO: LM-Design 0.516/0.570; ProteinMPNN 0.450/0.468.

[Source 1](https://arxiv.org/html/2409.06744v2), [Source 2](https://proteinbench.github.io/)

**ProteinBench unconditional backbone generation**

Reported values retained on the paper's scale; structural plausibility does not establish function.

Published source size/units: Length-stratified generation at 100/200/300/400/500 aa; 100 single-chain reference structures. Exact generated count must follow the release.

Published reference record: At length 100: RFdiffusion scTM 0.98 ± 0.12 and scRMSD 0.48 ± 0.56 Å; FrameFlow 0.94 ± 0.08 and 0.70 ± 0.70 Å.

[Source 1](https://arxiv.org/html/2409.06744v2), [Source 2](https://proteinbench.github.io/)

**ProteinBench unconditional sequence generation**

pLDDT is confidence, not experimentally measured protein stability or function.

Published source size/units: 50 sequences per model at each length 100, 200, 300 and 500.

Published reference record: At length 100, predicted AF2 pLDDT: DPLM-650M 85.38 ± 14.20; ProGen2-700M 64.00 ± 21.26.

[Source 1](https://arxiv.org/html/2409.06744v2), [Source 2](https://proteinbench.github.io/)

**ProteinBench joint sequence–structure generation**

These are selected length-specific results, not one design success rate.

Published source size/units: Length-stratified generated samples; exact per-setting candidate count not recovered.

Published reference record: Multiflow at length 100: scTM 0.96 ± 0.04; scRMSD 1.10 ± 0.71 Å. At length 200: scTM 0.95; scRMSD 1.61 Å.

[Source 1](https://arxiv.org/html/2409.06744v2), [Source 2](https://proteinbench.github.io/)

**MotifBench functional-motif scaffolding**

Score is not percentage of experimentally functional proteins. Preserve sampling and evaluator versions.

Published source size/units: 30 motif problems; standard submission 100 scaffolds per problem.

Published reference record: Official leaderboard snapshot: RFdiffusion3 43.52 ± 1.35 (Aug 2026); RFdiffusion 21.95 (Feb 2025), in MotifBench-score units.

[Source 1](https://github.com/blt2114/MotifBench), [Source 2](https://github.com/blt2114/MotifBench)

**ProteinBench motif scaffolding — legacy motif panel**

Do not merge the legacy panel with MotifBench or reuse their scores interchangeably.

Published source size/units: Legacy 17 (25) motif-problem panel described by ProteinBench; not MotifBench's separate 30-problem set.

Published reference record: Comparative motif-scaffolding results are reported; exact figure-derived score not transcribed.

[Source 1](https://arxiv.org/html/2409.06744v2), [Source 2](https://proteinbench.github.io/)

**ProteinBench antibody design — processed RAbD**

Same parent resource does not mean identical split or scorer. This is a distinct protocol, not 55 additional independent complexes.

Published source size/units: 55 retained RAbD complexes; differs from the 60-complex protocol in the earlier catalog.

Published reference record: DiffAb: AAR 35.04 ± 8.36%, RMSD 2.53 ± 0.60 Å; MEAN: AAR 33.47%, RMSD 1.82 Å.

[Source 1](https://arxiv.org/html/2409.06744v2), [Source 2](https://proteinbench.github.io/)

**CHIMERA-Bench epitope-conditioned antibody design**

EpiF1 measures intended-site contact, not empirical selectivity across off-target molecules.

Published source size/units: 2,922 complexes total. Test: 292 epitope-group; 292 antigen-fold; 293 temporal. Splits are alternatives, not additive test sets.

Published reference record: Epitope-group H3: RAAD AAR 0.37, RMSD 1.75 Å, DockQ 0.58; dyMEAN EpiF1 0.23 (RAAD 0.11).

[Source 1](https://arxiv.org/html/2603.13431v1), [Source 2](https://github.com/mansoor181/chimera-bench)

**ProtDBench de novo target-binder design**

Counts of computational passes, not wet-lab hit fractions. Exact target-specific conditions and verifier must match.

Published source size/units: 10 target proteins; 24 h on one A100 per method/target setting. Includes generation, inverse folding and scoring.

Published reference record: PD-L1 passing-backbone counts: PXDesign 1,247; BoltzGen 549; RFdiffusion3 542; BindCraft 231. TNFα: PXDesign 57; BoltzGen 15.

[Source 1](https://arxiv.org/html/2605.04118v1), [Source 2](https://arxiv.org/html/2605.04118v1)

**BioT5+ description-guided protein generation**

Qualitative design case A plausible or similar sequence is not a measured successful design.

Published source size/units: Can the model propose a sequence matching a description? The paper does not define a generally established benchmark for this task.

**Text-conditioned protein-sequence design:** Qualitative cases and sequence/reference comparisons. The paper does not define a generally established benchmark for this task.

A plausible or similar sequence is not a measured successful design.

Published reference record: Description-guided protein designs are presented as qualitative cases rather than a fixed, experimentally validated design-success rate.

[Source 1](https://arxiv.org/html/2402.17810v2)

**NatureLM generated proteins: unconditional / property-conditioned / heme**

Predictor-scored or qualitative design Diversity and predicted structure confidence do not establish function. | Predictor agreement, not experimentally measured stability/solubility of each generated sequence. | Self-description is not independent validation; predicted complexes are not measured binding.

Published source size/units: Does the model generate varied, structurally plausible protein sequences? / Do sequences requested to have a property score well under the evaluator? / Can conditioning suggest proteins plausibly associated with heme? Generated samples compared with natural sequences; not a labeled holdout prediction set. | Paper uses a natural UR50 reference subset of 1,000 sequences in the conditioned comparison. | Selected candidates; no standard released labeled test-set size.

**Unconditional protein generation:** Length distribution; clustering-based diversity; pLDDT. Generated samples compared with natural sequences; not a labeled holdout prediction set.

Diversity and predicted structure confidence do not establish function.

**Protein generation for predicted stability and solubility:** Predicted property scores; diversity. Paper uses a natural UR50 reference subset of 1,000 sequences in the conditioned comparison.

Predictor agreement, not experimentally measured stability/solubility of each generated sequence.

**Heme-binding protein candidate generation:** Qualitative description/complex screening. Selected candidates; no standard released labeled test-set size.

Self-description is not independent validation; predicted complexes are not measured binding.

Published reference record: Reported outputs are diversity/length distributions and predicted structural confidence. No experimentally measured function-success fraction is supplied by this evaluation. The reported comparison uses learned stability/solubility scores and diversity. No measured stability/solubility success rate is transcribed. Selected heme-binding candidates are screened with descriptions and predicted complexes; this is not experimentally demonstrated heme binding.

[Source 1](https://arxiv.org/html/2502.07527v3)

**STRIDE GFP sequence optimization**

Predictor-scored generation These 100 candidates are not a wet-lab test set. Correctly applying edits does not validate fluorescence.

Published source size/units: Do proposed edits improve the fixed scorer's predicted fluorescence? 100 candidates per method from a common source; separate replace-only and full-edit settings.

**GFP sequence optimization against a fluorescence predictor:** Predicted improvement/success; uniqueness; novelty. 100 candidates per method from a common source; separate replace-only and full-edit settings.

These 100 candidates are not a wet-lab test set. Correctly applying edits does not validate fluorescence.

<details>
<summary>STRIDE GFP generated-candidate evaluation: protocol, counts and complete metric record</summary>

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

</details>

[Source 1](https://arxiv.org/html/2603.03573v1)

**Prompteina text-conditioned protein design — GM2A campaign**

Prospective experimental campaign A single target campaign, not a general fixed test set or aggregate success rate. 52.4M captions is a training size.

Published source size/units: Generate target binders from language specifications; measure selected designs prospectively. 1,000-design computational budget; 90 selected; 89 expressed and assayed.

Published reference record: 9 of 89 assayed designs classified as binders; 8 fitted apparent KD values. Strongest apparent KD: 107 nM.

[Source 1](https://arxiv.org/html/2610.13917v1)

</details>

## Structure and conformational prediction

| Task | Dataset/protocol | Status | Qwen result | Published reference |
|---|---|---|---|---|
| Residue identity from local structure | ATOM3D residue identity from local structure (RES) | Listed for consideration | — | ATOM3D 3D-CNN test accuracy: 0.451. · [source](https://arxiv.org/html/2012.04035v3) |
| Protein structure ranking | ATOM3D protein structure ranking (PSR) | Listed for consideration | — | Per-target mean Spearman: GNN 0.515; 3D-CNN 0.431. Global correlations are different metrics. · [source](https://arxiv.org/html/2012.04035v3) |
| Single-state protein folding | ProteinBench single-state folding — CAMEO 2022 | Listed for consideration | — | AF2 mean/median TM-score 0.871/0.952, RMSD 3.21/1.64 Å; ESMFold 0.847/0.929 and 3.98/2.10 Å. · [source](https://arxiv.org/html/2409.06744v2) |
| Multistate protein conformations | ProteinBench multistate conformations — apo/holo and BPTI | Listed for consideration | — | Apo/holo TM-ensemble: AlphaFlow-PDB 0.873; MSA-depth256 0.867. BPTI N=1000: ConfDiff-ESM-force ensemble RMSD 1.36 Å. · [source](https://arxiv.org/html/2409.06744v2) |
| Protein conformational ensembles | ProteinBench ensemble distribution — ATLAS | Listed for consideration | — | AlphaFlow-MD: per-target RMSF correlation 0.85 and PCA-Wasserstein 1.55; ConfDiff PCA-Wasserstein 1.41 (paper's units). · [source](https://arxiv.org/html/2409.06744v2) |
| Protein states, dynamics and free energy | BioEmu benchmark collection — states, dynamics and free energy | Listed for consideration | — | Official model card: domain-motion coverage 83%; cryptic-pocket apo/holo coverage 55%/88%; experimental stability MAE ~0.9 kcal/mol, Spearman ~0.6. · [source](https://github.com/microsoft/bioemu/blob/main/MODEL_CARD.md) |
| Structure-derived protein prediction | PFMBench structure-derived prediction panel | Listed for consideration | — | ESM2-Adapter, Table 1 means: Contact Top L/5 0.7199; FoldClass Accuracy 0.7859; SecondaryStructure Accuracy 0.7601 · [source](https://arxiv.org/html/2506.14796v1) |
| Structure-derived questions and output-format checks<br>Independent held-out questions remain unresolved. | Proteo-R1 internal alignment / structural / CDR diagnostics | Listed for consideration | — | Selected Stage-II M3: contact 58.3%; interface 15.1%; hotspot 11.6%. Separate Stage-I schema 81.4%. No overall score. · [source](https://arxiv.org/html/2605.02937v1) |

<details>
<summary>Protocols, qualifications and complete source records</summary>

**ATOM3D residue identity from local structure (RES)**

Environment count is not protein count. This is an established held-out structure task, unlike unverified internal diagnostics.

Published source size/units: Test: 3,319 PDB structures yielding 1,261,342 local environments; train: 21,147 structures.

Published reference record: ATOM3D 3D-CNN test accuracy: 0.451.

[Source 1](https://arxiv.org/html/2012.04035v3), [Source 2](https://www.atom3d.ai/)

**ATOM3D protein structure ranking (PSR)**

Ranking a supplied set of structures is not de novo structure generation.

Published source size/units: CASP-derived target/decoy split; exact processed test-target/decoy counts not transcribed.

Published reference record: Per-target mean Spearman: GNN 0.515; 3D-CNN 0.431. Global correlations are different metrics.

[Source 1](https://arxiv.org/html/2012.04035v3), [Source 2](https://www.atom3d.ai/)

**ProteinBench single-state folding — CAMEO 2022**

Models may have different MSA/template access. This is a historical target cohort, not the live CAMEO leaderboard.

Published source size/units: 183 proteins (<750 residues), released Aug–Oct 2022.

Published reference record: AF2 mean/median TM-score 0.871/0.952, RMSD 3.21/1.64 Å; ESMFold 0.847/0.929 and 3.98/2.10 Å.

[Source 1](https://arxiv.org/html/2409.06744v2), [Source 2](https://proteinbench.github.io/)

**ProteinBench multistate conformations — apo/holo and BPTI**

Sample count is not the number of independent test proteins; BPTI alone gives narrow generalization evidence.

Published source size/units: Apo/holo: 91 protein pairs, 20 generated conformations per protein. BPTI: one 58-residue protein, 5 MD clusters, N=10/100/1000 samples.

Published reference record: Apo/holo TM-ensemble: AlphaFlow-PDB 0.873; MSA-depth256 0.867. BPTI N=1000: ConfDiff-ESM-force ensemble RMSD 1.36 Å.

[Source 1](https://arxiv.org/html/2409.06744v2), [Source 2](https://proteinbench.github.io/)

**ProteinBench ensemble distribution — ATLAS**

MD reference is simulation-derived, not an exhaustive experimental distribution. Preserve alignment, projection and aggregation.

Published source size/units: 82 held-out proteins; 250 generated conformations per protein.

Published reference record: AlphaFlow-MD: per-target RMSF correlation 0.85 and PCA-Wasserstein 1.55; ConfDiff PCA-Wasserstein 1.41 (paper's units).

[Source 1](https://arxiv.org/html/2409.06744v2), [Source 2](https://proteinbench.github.io/)

**BioEmu benchmark collection — states, dynamics and free energy**

Pin benchmark/model revision: version changes affect values. Panel scores are not one pooled success rate.

Published source size/units: Multiple panels: domain motion, local unfolding, cryptic pockets, MD emulation and experimental folding free energies. Exact panel sizes not re-counted.

Published reference record: Official model card: domain-motion coverage 83%; cryptic-pocket apo/holo coverage 55%/88%; experimental stability MAE ~0.9 kcal/mol, Spearman ~0.6.

[Source 1](https://github.com/microsoft/bioemu/blob/main/MODEL_CARD.md), [Source 2](https://github.com/microsoft/bioemu-benchmarks)

**PFMBench structure-derived prediction panel**

These are PFMBench-specific processed datasets/splits, not interchangeable with PEER/ProtST results. F1 is not Fmax. Affinity-named AUROC tasks are classification, not KD regression. Exact loaders required.

Published source size/units: Test sizes: Contact: 1,501; FoldClass: 1,630; SecondaryStructure: 8,262

Published reference record: ESM2-Adapter, Table 1 means: Contact Top L/5 0.7199; FoldClass Accuracy 0.7859; SecondaryStructure Accuracy 0.7601

[Source 1](https://arxiv.org/html/2506.14796v1), [Source 2](https://github.com/biomap-research/PFMBench)

**Proteo-R1 internal alignment / structural / CDR diagnostics**

Internal diagnostic — holdout unresolved Not a named released PDB benchmark. Eight-response averages are not pass@8. No evidence of leakage is inferred from missing documentation.

Published source size/units: Check training-stage behavior on calculated structural questions and output-schema tasks. Independent held-out question manifest and size unresolved; 9.09M is Stage-II TRAINING instances.

Published reference record: Selected Stage-II M3: contact 58.3%; interface 15.1%; hotspot 11.6%. Separate Stage-I schema 81.4%. No overall score.

[Source 1](https://arxiv.org/html/2605.02937v1)

</details>

## Biomedical visual evidence

| Task | Dataset/protocol | Status | Qwen result | Published reference |
|---|---|---|---|---|
| Radiology image question answering | Biomedical VQA: VQA-RAD / SLAKE-English / PathVQA / VQA-Med 2019<br>VQA-RAD | Finished | open_token_recall 59.5%; closed_accuracy 86.8% | LLaVA-Med 7B, CLIP, 60K-IM, stage1=1/stage2=3/FT=0: open token recall 28.23%; closed accuracy 61.4%; n=451; Table 4(b), PDF p.9 · [source](https://arxiv.org/pdf/2306.00890) |
| Medical image question answering in English | Biomedical VQA: VQA-RAD / SLAKE-English / PathVQA / VQA-Med 2019<br>SLAKE — English | Finished | open_token_recall 51.0%; closed_accuracy 84.6% | LLaVA-Med 7B, CLIP, 60K-IM, stage1=1/stage2=3/FT=0: open token recall 39.17%; closed accuracy 52.16%; n=1061; Table 4(b), PDF p.9 · [source](https://arxiv.org/pdf/2306.00890) |
| Pathology image question answering | Biomedical VQA: VQA-RAD / SLAKE-English / PathVQA / VQA-Med 2019<br>PathVQA | Finished | open_token_recall 26.4%; closed_accuracy_corrected 0.8587 | LLaVA-Med 7B, CLIP, 60K-IM, stage1=1/stage2=3/FT=0: open token recall 12.3%; closed accuracy 54.05%; n=6761; Table 4(b), PDF p.9 · [source](https://arxiv.org/pdf/2306.00890) |
| Medical image question answering | Biomedical VQA: VQA-RAD / SLAKE-English / PathVQA / VQA-Med 2019<br>ImageCLEF-VQA 2019 | Finished | strict_accuracy 0.0% | MedVInT-TE: overall accuracy 70.5%; Table 2 · [source](https://arxiv.org/html/2305.10415v6) |
| Scientific figure question answering | PMC-VQA figure question answering | Finished | native_td_final_character_accuracy 0.0200; adapted_full_text_closest_choice_accuracy 0.4975; adapted_full_text_released_label_accuracy 0.4975; strict_final_label_accuracy 0.0070 | MedVInT-TD / PMC-LLaMA / PMC-CLIP: choice accuracy 40.3%; blank accuracy 33.6%; blank bleu1 21.5%; n=2000; Table 3 · [source](https://arxiv.org/html/2305.10415v6) |
| Biomedical visual conversations* | LLaVA-Med biomedical visual conversations | Run status unconfirmed | — | GPT-assisted relative answer-quality comparisons are reported. A verified single aggregate for the specified qa50 setting is not transcribed here. · [source](https://arxiv.org/abs/2306.00890) |
| Scientific document and figure extraction* | Ryze document-extraction component tests | Run status unconfirmed | — | Ryze extraction-component accuracy: ArXivQA 73.12%, SlideVQA 66.48%, ChartQA 75.8%. · [source](https://arxiv.org/html/2606.00902v1) |

<details>
<summary>Protocols, qualifications and complete source records</summary>

**Biomedical VQA: VQA-RAD / SLAKE-English / PathVQA / VQA-Med 2019**

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

<details>
<summary>VQA-RAD: protocol, counts and complete metric record</summary>

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

</details>

<details>
<summary>SLAKE — English: protocol, counts and complete metric record</summary>

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

</details>

<details>
<summary>PathVQA: protocol, counts and complete metric record</summary>

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

</details>

<details>
<summary>ImageCLEF-VQA 2019: protocol, counts and complete metric record</summary>

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

</details>

[Source 1](https://arxiv.org/abs/2306.00890), [Source 2](https://arxiv.org/html/2305.10415v6), [Source 3](https://arxiv.org/abs/2306.00890), [Source 4](https://arxiv.org/html/2305.10415v6), [Source 5](https://github.com/microsoft/LLaVA-Med), [Source 6](https://github.com/xiaoman-zhang/PMC-VQA)

**PMC-VQA figure question answering**

Specify initial versus cleaned test set. Caption-derived labels need not be visually answerable without filtering.

Published source size/units: Reviewed v6: 50,000 initial test examples; 2,000 manually reviewed clean test examples.

**Scientific figure question answering:** MCQ accuracy; paper's open/blank-answer accuracy and BLEU. v6: 50,000 initial image-disjoint test examples; 2,000 manually reviewed clean test examples. Older site names differ.

Specify initial versus cleaned test set. Caption-derived labels need not be visually answerable without filtering.

<details>
<summary>PMC-VQA held-out evaluation: protocol, counts and complete metric record</summary>

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

</details>

[Source 1](https://arxiv.org/html/2305.10415v6), [Source 2](https://github.com/xiaoman-zhang/PMC-VQA)

**LLaVA-Med biomedical visual conversations**

Teacher reference has textual context that the image may not reveal. Judgment is not direct clinician-verified molecular truth.

Published source size/units: Published 50-image conversation-evaluation setting; teacher-generated text references.

**Biomedical visual conversations:** GPT-assisted relative response assessment. Released qa50 evaluation files; 50-image setting. Use original/v1.5 code and model version consistently.

Teacher reference has textual context that the image may not reveal. Judgment is not direct clinician-verified molecular truth.

Published reference record: GPT-assisted relative answer-quality comparisons are reported. A verified single aggregate for the specified qa50 setting is not transcribed here.

[Source 1](https://arxiv.org/abs/2306.00890), [Source 2](https://github.com/microsoft/LLaVA-Med)

**Ryze document-extraction component tests**

Component ablation These tests evaluate extraction/document understanding, not protein engineering.

Published source size/units: Does document/figure extraction preserve information needed for answering questions? Auxiliary component evaluation, separate from final LAB-Bench scores.

**Scientific document and figure extraction:** Dataset-specific QA accuracy. Auxiliary component evaluation, separate from final LAB-Bench scores.

These tests evaluate extraction/document understanding, not protein engineering.

Published reference record: Ryze extraction-component accuracy: ArXivQA 73.12%, SlideVQA 66.48%, ChartQA 75.8%.

[Source 1](https://arxiv.org/html/2606.00902v1)

</details>

## Other biological modalities and molecular interactions

| Task | Dataset/protocol | Status | Qwen result | Published reference |
|---|---|---|---|---|
| Drug–target interaction | Drug–target interaction: BioSNAP / Human / BindingDB<br>Drug–target interaction — BioSNAP/Human/BindingDB · bindingdb | Finished | AUROC 0.5036; AP 0.4103 | BioT5+ (supervised): AUROC 0.964 ± 0.001; Table 8 · [source](https://arxiv.org/html/2402.17810v2) |
| Drug–target interaction | Drug–target interaction: BioSNAP / Human / BindingDB<br>Drug–target interaction — BioSNAP/Human/BindingDB · biosnap | Finished | AUROC 0.5336; AP 0.5217 | BioT5+ (supervised): AUROC 0.939 ± 0.001; Table 8 · [source](https://arxiv.org/html/2402.17810v2) |
| Drug–target interaction | Drug–target interaction: BioSNAP / Human / BindingDB<br>Drug–target interaction — BioSNAP/Human/BindingDB · human | Finished | AUROC 0.4747; AP 0.4194 | BioT5+ (supervised): AUROC 0.987 ± 0.001; Table 8 · [source](https://arxiv.org/html/2402.17810v2) |
| Pathway and disease prediction | BioReason KEGG pathway/disease | Finished | accuracy 0.0%; STRICT_FINAL_LABEL.accuracy 0.0%; STRICT_FINAL_LABEL.supplemental_macro_f1_fixed_global_vocabulary 0.0000; STRICT_FINAL_LABEL.supplemental_macro_precision_fixed_global_vocabulary 0.0000; STRICT_FINAL_LABEL.supplemental_macro_recall_fixed_global_vocabulary 0.0000 | Qwen3-4B: accuracy 90.0%; macro f1 79.66%; macro precision 88.24%; n=290; Table 1 · [source](https://arxiv.org/html/2505.23579v2) |
| Coding-variant effect prediction | BioReason VEP coding and non-SNV<br>BioReason VEP-Coding | Finished | accuracy 49.1%; f1 0.5213; STRICT_FINAL_LABEL.accuracy 0.0%; STRICT_FINAL_LABEL.f1 0.0000 | Qwen3-4B: accuracy 48.99%; f1 39.58%; Table 2 · [source](https://arxiv.org/html/2505.23579v2) |
| Non-SNV variant effect prediction | BioReason VEP coding and non-SNV<br>BioReason VEP-Non-SNV | Finished | accuracy 89.0%; f1 0.9053; STRICT_FINAL_LABEL.accuracy 0.0%; STRICT_FINAL_LABEL.f1 0.0000 | Qwen3-4B: accuracy 61.86%; f1 67.6%; n=873; Table 2 · [source](https://arxiv.org/html/2505.23579v2) |
| Network-held-out pathway prediction* | Bio-posttrain KEGG unseen-network holdout | Blocked | — | Qwen3-4B DNA OOD accuracy: SFT 0.753; SFT+RL 0.917; biology-CPT+SFT+RL 0.970. · [source](https://arxiv.org/html/2606.16517v1) |
| Expression-conditioned gene selection* | Bio-posttrain MEDEA expression-conditioned gene selection | Blocked | — | The paper reports RNA target-selection ID/OOD experiments. An exact numeric result is not transcribed in this table. · [source](https://arxiv.org/html/2606.16517v1) |
| Protein–ligand binding affinity | ATOM3D protein–ligand affinity (LBA) | Listed for consideration | — | 3D-CNN: RMSE 1.416, Spearman 0.553; GNN: RMSE 1.570, Spearman 0.628. · [source](https://arxiv.org/html/2012.04035v3) |
| Ligand efficacy | ATOM3D ligand efficacy (LEP) | Listed for consideration | — | AUROC: GNN 0.740; 3D-CNN 0.589. · [source](https://arxiv.org/html/2012.04035v3) |
| RNA structure ranking | ATOM3D RNA structure ranking (RSR) | Listed for consideration | — | Mean per-target Spearman: 3D-CNN 0.264; GNN 0.234. · [source](https://arxiv.org/html/2012.04035v3) |
| Small-molecule properties | ATOM3D small-molecule properties (SMP / QM9) | Listed for consideration | — | ENN dipole MAE 0.052 D; 3D-CNN 0.754 D. Property-specific scores must remain separate. · [source](https://arxiv.org/html/2012.04035v3) |
| Protein–ligand binding affinity | PFMBench PDBbind / BindingDB affinity panel | Listed for consideration | — | ESM2-Adapter, Table 1 means: PDBBind Spearman 0.1677; BindingDB Spearman 0.1922 · [source](https://arxiv.org/html/2506.14796v1) |

<details>
<summary>Protocols, qualifications and complete source records</summary>

**Drug–target interaction: BioSNAP / Human / BindingDB**

Secondary to the protein focus. Not protein–protein recognition or Affibody–pMHC evaluation.

Published source size/units: Three source benchmarks; preserve each split/negative/threshold rule.

**Drug–target interaction:** AUROC in BioT5+ comparisons. Three source benchmarks; preserve each split/negative/threshold rule.

Secondary to the protein focus. Not protein–protein recognition or Affibody–pMHC evaluation.

<details>
<summary>Drug–target interaction — BioSNAP/Human/BindingDB · bindingdb: protocol, counts and complete metric record</summary>

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

</details>

<details>
<summary>Drug–target interaction — BioSNAP/Human/BindingDB · biosnap: protocol, counts and complete metric record</summary>

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

</details>

<details>
<summary>Drug–target interaction — BioSNAP/Human/BindingDB · human: protocol, counts and complete metric record</summary>

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

</details>

[Source 1](https://arxiv.org/html/2402.17810v2), [Source 2](https://github.com/QizhiPei/BioT5)

**BioReason KEGG pathway/disease**

Correct final disease labels do not verify every generated mechanistic statement.

Published source size/units: 290 test entries in main table; 1,449 overall entries across splits.

**Pathway and disease prediction:** Accuracy; macro-F1/precision/recall. 290 test entries in main table; 1,449 overall entries across splits.

Correct final disease labels do not verify every generated mechanistic statement.

<details>
<summary>BioReason KEGG pathway/disease test: protocol, counts and complete metric record</summary>

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

</details>

[Source 1](https://arxiv.org/html/2505.23579v2), [Source 2](https://huggingface.co/datasets/wanglab/kegg)

**BioReason VEP coding and non-SNV**

Genomics task, not Affibody binding; annotation confidence and splitting matter. | Non-SNV classification should not be merged with single-amino-acid design accuracy.

Published source size/units: Coding: approximately 1.23K reported test cases; non-SNV: 873. Distinct datasets.

**Coding-variant effect prediction:** Accuracy; F1. Main reported test approximately 1.23K; chromosome 8 held out.

Genomics task, not Affibody binding; annotation confidence and splitting matter.

**Non-SNV variant effect prediction:** Accuracy; F1. 873 test examples in the main report.

Non-SNV classification should not be merged with single-amino-acid design accuracy.

<details>
<summary>BioReason VEP-Coding: protocol, counts and complete metric record</summary>

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

</details>

<details>
<summary>BioReason VEP-Non-SNV: protocol, counts and complete metric record</summary>

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

</details>

[Source 1](https://arxiv.org/html/2505.23579v2), [Source 2](https://github.com/bowang-lab/BioReason)

**Bio-posttrain KEGG unseen-network holdout**

Pin the adapted split and preprocessing.

Published source size/units: Adapted KEGG split by pathway networks; not automatically BioReason's original 290-example test.

**Network-held-out pathway prediction:** Accuracy. Adapted KEGG split by pathway networks; not automatically BioReason's original 290-example test.

Pin the adapted split and preprocessing.

Exact network-held-out CSVs/IDs unavailable; author genomics link redirects to sign-in. Original N01 is not a substitute.

Published reference record: Qwen3-4B DNA OOD accuracy: SFT 0.753; SFT+RL 0.917; biology-CPT+SFT+RL 0.970.

[Source 1](https://arxiv.org/html/2606.16517v1), [Source 2](https://github.com/mims-harvard/bio-posttrain)

**Bio-posttrain MEDEA expression-conditioned gene selection**

Fixed-input target nomination is not the original full agent workflow or clinical validation.

Published source size/units: Held-out disease: hepatoblastoma; additional cell-type analyses reported.

**Expression-conditioned gene selection:** Normalized gene-answer accuracy. Held-out disease: hepatoblastoma; additional cell-type analyses reported.

Fixed-input target nomination is not the original full agent workflow or clinical validation.

Exact adapted hepatoblastoma split/vector alignment/RNA evaluator missing; upstream MEDEA questions or gene lists do not replace required expression inputs.

Published reference record: The paper reports RNA target-selection ID/OOD experiments. An exact numeric result is not transcribed in this table.

[Source 1](https://arxiv.org/html/2606.16517v1), [Source 2](https://github.com/mims-harvard/bio-posttrain)

**ATOM3D protein–ligand affinity (LBA)**

Target transformation and split must match. Not antibody–antigen affinity.

Published source size/units: 30%-identity split: train 3,507, validation 466, test 490 complexes. The 60% split is a different protocol.

Published reference record: 3D-CNN: RMSE 1.416, Spearman 0.553; GNN: RMSE 1.570, Spearman 0.628.

[Source 1](https://arxiv.org/html/2012.04035v3), [Source 2](https://www.atom3d.ai/)

**ATOM3D ligand efficacy (LEP)**

Activity/efficacy is distinct from affinity. Source molecule count is not a test denominator.

Published source size/units: 527 source small molecules; final retained train/test counts not transcribed.

Published reference record: AUROC: GNN 0.740; 3D-CNN 0.589.

[Source 1](https://arxiv.org/html/2012.04035v3), [Source 2](https://www.atom3d.ai/lep.html)

**ATOM3D RNA structure ranking (RSR)**

RNA task retained as adjacent scope, not a protein benchmark.

Published source size/units: RNA-Puzzles 1–21; test puzzles 18–21, with decoys per target. Exact retained test-decoy count not re-counted.

Published reference record: Mean per-target Spearman: 3D-CNN 0.264; GNN 0.234.

[Source 1](https://arxiv.org/html/2012.04035v3), [Source 2](https://www.atom3d.ai/rsr.html)

**ATOM3D small-molecule properties (SMP / QM9)**

Adjacency only; not protein biology. Units depend on property.

Published source size/units: Processed test 12,943 molecules (train 103,547; validation 12,943).

Published reference record: ENN dipole MAE 0.052 D; 3D-CNN 0.754 D. Property-specific scores must remain separate.

[Source 1](https://arxiv.org/html/2012.04035v3), [Source 2](https://www.atom3d.ai/)

**PFMBench PDBbind / BindingDB affinity panel**

These are PFMBench-specific processed datasets/splits, not interchangeable with PEER/ProtST results. F1 is not Fmax. Affinity-named AUROC tasks are classification, not KD regression. Exact loaders required.

Published source size/units: Test sizes: PDBBind: 1,836; BindingDB: 1,139

Published reference record: ESM2-Adapter, Table 1 means: PDBBind Spearman 0.1677; BindingDB Spearman 0.1922

[Source 1](https://arxiv.org/html/2506.14796v1), [Source 2](https://github.com/biomap-research/PFMBench)

</details>

[Raw run artifacts and uploaded trajectories](https://github.com/Some-random/bio-evaluation/tree/main/results/runs)
