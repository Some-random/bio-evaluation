# Biological evaluation results by scientific capability

[Overview](EVALUATION_OVERVIEW.md) · [Complete inventory](TASK_HIERARCHY_COMPLETE.md) · [Coverage crosswalk](TASK_COVERAGE_MAP.csv)

Stored scores: **2026-10-16 06:49 PDT**. Running-work snapshot: **2026-10-17 18:28 PDT**. Display times use Pacific time.

Only existing stored local outcomes are shown. The category order matches the complete inventory. **\*** marks incomplete coverage or scoring; count records are in expandable details. Undefined values remain undefined. Published values are separate contextual comparisons, not matched replications, pooled scores or claims of superiority. All reference records and alternate metric values are retained in the details.

A declared run may be complete despite invalid answers when its native scorer explicitly counts invalid answers in the denominator. That is different from an undefined native primary metric; finished runs with undefined primary metrics are labeled diagnostics separately below.

## Protein properties, interactions and developability

### Protein solubility

**Dataset/protocol:** DeepSol solubility — PEER split

| Scientific setting | Local stored result | Published reference — different protocol |
|---|---|---|
| Solubility — PEER | accuracy 24.2% | BioT5+: accuracy 74.37% ± 0.19 percentage points; Table 6 · [source](https://arxiv.org/html/2402.17810v2) |

Task-trained models; BioT5+ is multitask and BioT5 single-task. Count is PEER's published split, not a new loader count.

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

### Subcellular localization

**Dataset/protocol:** DeepLoc — binary and 10-compartment localization

| Scientific setting | Local stored result | Published reference — different protocol |
|---|---|---|
| Binary localization — DeepLoc/PEER | accuracy 27.4% | BioT5+: accuracy 90.41% ± 0.07 percentage points; Table 6 · [source](https://arxiv.org/html/2402.17810v2) |
| Subcellular localization — DeepLoc | accuracy 26.1% | ProtST-ESM-1b: fixed encoder.accuracy 82.0%; full model tuning.accuracy 78.73%; Table 2, printed p.6 · [source](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf) |

Binary comparison uses task-tuned systems. Ten-class numbers use frozen encoders + trained heads. These are distinct endpoints.

Published ten-class count is 2,768; the frozen local run contains 2,773 cases. These source-specific counts are retained separately.

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

<details>
<summary>Subcellular localization — DeepLoc: protocol, counts and complete metric record</summary>

**Native/local protocol:** `QWEN_ZERO_SHOT_FULL_SEQUENCE_DEEPLOC_NATIVE_LABELS`

**Coverage:** full_frozen_reviewed_released_test; completed_declared_run.

**Saved count record:**

```json
{
  "planned": 2773,
  "completed": 2773,
  "parsed": 2722,
  "invalid_outputs": 51,
  "missing_or_failed_outputs": 0,
  "held_before_inference": 0
}
```

**Complete stored metrics, including alternate/diagnostic values:**

```json
{
  "planned": 2773,
  "parsed": 2722,
  "missing": 0,
  "invalid": 51,
  "accuracy": 0.2610890732059142,
  "correct": 724,
  "all_case_rule": "Invalid/missing classes count incorrect; all planned rows stay in denominator."
}
```

**Comparison qualification:** Original released public test data and native outcome/metric; zero-shot Qwen prompt/representation/training regime differs from native-trained TAPE/ProtST heads.

**All stored published-reference records — separate from the local run:**

```json
[
  {
    "model": "ProtST-ESM-1b",
    "metrics": {
      "fixed_encoder": {
        "accuracy_percent": 82.0
      },
      "full_model_tuning": {
        "accuracy_percent": 78.73
      }
    },
    "source_id": "PROTST",
    "source_url": "https://proceedings.mlr.press/v202/xu23t/xu23t.pdf",
    "source_locator": "Table 2, printed p.6",
    "protocol": "two-layer MLP trained on official task split; frozen encoder and full tuning are separate regimes",
    "value_status": "published_rounded_as_printed",
    "run_count": null,
    "reported_std": null
  },
  {
    "model": "ProtST-ESM-1b",
    "metrics": {
      "zero_shot_accuracy_percent": 43.49
    },
    "source_id": "PROTST",
    "source_url": "https://proceedings.mlr.press/v202/xu23t/xu23t.pdf",
    "source_locator": "Table 11, printed p.15",
    "protocol": "zero-shot embedding similarity to label names in published pretraining template",
    "value_status": "published_rounded_as_printed",
    "run_count": null,
    "reported_std": null
  }
]
```

[Original score artifact](https://github.com/Some-random/bio-evaluation/blob/main/results/runs/qwen38_27b_p03_full_test_slurm_2026-10-16/scores.json)

</details>

### Variant fitness and thermostability*

**Dataset/protocol:** FLIP — AAV and Meltome

**Finished diagnostic only:** the full native primary metric is undefined. The parsed-only value below does not complete the benchmark or replace the native metric.

| Scientific setting | Local stored result | Published reference — different protocol |
|---|---|---|
| Thermostability — FLIP/Meltome* | spearman undefined; spearman_parsed_only 0.0254 | ProtST-ESM-1b: fixed encoder.spearman 0.68; full model tuning.spearman 0.681; Table 2, printed p.6 · [source](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf) |

Two distinct source datasets, grouped under the FLIP suite. Full-model fine-tuning; no cross-assay average added.

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

### Protein–protein interaction

**Dataset/protocol:** Human/Pan and yeast/Guo PPI — PEER

| Scientific setting | Local stored result | Published reference — different protocol |
|---|---|---|
| Human protein–protein interaction — PEER | accuracy 50.2% | BioT5+ (supervised): accuracy 85.09% ± 0.4 percentage points; Table 6 · [source](https://arxiv.org/html/2402.17810v2) |
| Yeast protein–protein interaction — PEER | accuracy 45.2% | BioT5+ (supervised): accuracy 66.16% ± 0.43 percentage points; Table 6 · [source](https://arxiv.org/html/2402.17810v2) |

Separate human/yeast negatives and splits. Generic PPI, not Affibody–pMHC specificity.

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

## Protein function, annotations and descriptions

### Protein description generation

**Dataset/protocol:** Mol-Instructions — four protein-description subsets

| Scientific setting | Local stored result | Published reference — different protocol |
|---|---|---|
| Mol-Instructions: Protein function generation | rouge1 0.0631; rouge2 0.0139; rougeL 0.0431; rougeLsum 0.0542 | Verified numerical comparator unavailable |
| Mol-Instructions: Catalytic activity generation | rouge1 0.0541; rouge2 0.0140; rougeL 0.0396; rougeLsum 0.0473 | Verified numerical comparator unavailable |
| Mol-Instructions: Domain and motif generation | rouge1 0.0354; rouge2 0.0047; rougeL 0.0259; rougeLsum 0.0306 | Verified numerical comparator unavailable |
| Mol-Instructions: Functional description generation | rouge1 0.0800; rouge2 0.0123; rougeL 0.0494; rougeLsum 0.0649 | Verified numerical comparator unavailable |

NEW source result: these are Mol-Instructions' own numbers, NOT BioT5+. BioT5+'s Figure 2 reports its comparisons, but exact plotted values were not transcribed.

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

## Mutation-effect interpretation

No completed local result in this stored score snapshot. [The inventory](TASK_HIERARCHY_COMPLETE.md) retains running, blocked, held and unverified protocols.

## Mutation ranking, affinity and local optimization

No completed local result in this stored score snapshot. [The inventory](TASK_HIERARCHY_COMPLETE.md) retains running, blocked, held and unverified protocols.

## Scientific evidence and biological knowledge

### Research evidence and biological knowledge*

**Dataset/protocol:** LAB-Bench — research tasks

| Scientific setting | Local stored result | Published reference — different protocol |
|---|---|---|
| LAB-Bench / LitQA2* | accuracy 39.1%; precision 41.0%; coverage 95.4% | GPT-5.2: accuracy 45.7%; n=199; Table 1 · [source](https://arxiv.org/html/2606.00902v1) |
| LAB-Bench / DbQA | accuracy 31.3%; precision 31.8%; coverage 98.5% | GPT-5.2: accuracy 41.7%; n=520; Table 1 · [source](https://arxiv.org/html/2606.00902v1) |
| LAB-Bench / SuppQA | accuracy 37.8%; precision 39.2%; coverage 96.3% | GPT-5.2: accuracy 48.8%; n=82; Table 1 · [source](https://arxiv.org/html/2606.00902v1) |
| LAB-Bench / FigQA | accuracy 72.4%; precision 72.8%; coverage 99.4% | GPT-5.2: accuracy 36.5%; n=181; Table 1 · [source](https://arxiv.org/html/2606.00902v1) |
| LAB-Bench / TableQA | accuracy 88.1%; precision 90.0%; coverage 98.0% | GPT-5.2: accuracy 36.9%; n=244; Table 1 · [source](https://arxiv.org/html/2606.00902v1) |
| LAB-Bench / SeqQA | accuracy 12.7%; precision 12.8%; coverage 99.2% | GPT-5.2: accuracy 47.0%; n=600; Table 1 · [source](https://arxiv.org/html/2606.00902v1) |
| LAB-Bench / Cloning scenarios | accuracy 0.0%; precision 0.0%; coverage 100.0% | GPT-5.2: accuracy 36.4%; n=33; Table 1 · [source](https://arxiv.org/html/2606.00902v1) |

Original full public+private test; not the public 1,967-question subset. Three-run means. Tool-free models; TableQA and FigQA are images. No new category aggregate invented.

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

[Original score artifact](https://github.com/Some-random/bio-evaluation/blob/main/results/runs/qwen38_27b_litqa2_replay_2026-10-16/scores.json)

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
  "accuracy": 0.3780487804878049,
  "precision": 0.3924050632911392,
  "coverage": 0.9634146341463414,
  "n_total": 82,
  "n_correct": 31,
  "n_sure": 79
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

[Original score artifact](https://github.com/Some-random/bio-evaluation/blob/main/results/runs/qwen38_27b_b03_slurm_replay_2026-10-16/scores.json)

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
  "accuracy": 0.7237569060773481,
  "precision": 0.7277777777777777,
  "coverage": 0.994475138121547,
  "n_total": 181,
  "n_correct": 131,
  "n_sure": 180
}
```

**Comparison qualification:** Native public prompts, choices, required context/images and metrics. Reviewed public release; one fixed-seed run, not the original full public/private three-run paper mean. Strict deterministic parser; no model extraction fallback.

Public release 181/181; one seeded run, no tools; published decoder/repeats differ.

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

[Original score artifact](https://github.com/Some-random/bio-evaluation/blob/main/results/runs/qwen38_27b_b04_slurm_replay_2026-10-16/scores.json)

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
  "parsed": 236,
  "invalid_outputs": 8,
  "missing_or_failed_outputs": null,
  "held_before_inference": 0
}
```

**Complete stored metrics, including alternate/diagnostic values:**

```json
{
  "accuracy": 0.8811475409836066,
  "precision": 0.899581589958159,
  "coverage": 0.9795081967213115,
  "n_total": 244,
  "n_correct": 215,
  "n_sure": 239
}
```

**Comparison qualification:** Native public prompts, choices, required context/images and metrics. Reviewed public release; one fixed-seed run, not the original full public/private three-run paper mean. Strict deterministic parser; no model extraction fallback.

Public release 244/244; one seeded run, no tools; published decoder/repeats differ.

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

[Original score artifact](https://github.com/Some-random/bio-evaluation/blob/main/results/runs/qwen38_27b_b05_slurm_replay_2026-10-16/scores.json)

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

## Protein design

No completed local result in this stored score snapshot. [The inventory](TASK_HIERARCHY_COMPLETE.md) retains running, blocked, held and unverified protocols.

## Structure and conformational prediction

No completed local result in this stored score snapshot. [The inventory](TASK_HIERARCHY_COMPLETE.md) retains running, blocked, held and unverified protocols.

## Biomedical visual evidence

### Biomedical visual question answering

**Dataset/protocol:** Biomedical VQA: VQA-RAD / SLAKE-English / PathVQA / VQA-Med 2019

| Scientific setting | Local stored result | Published reference — different protocol |
|---|---|---|
| VQA-RAD | open_token_recall 59.5%; closed_accuracy 86.8% | LLaVA-Med 7B, CLIP, 60K-IM, stage1=1/stage2=3/FT=0: open token recall 28.23%; closed accuracy 61.4%; n=451; Table 4(b), PDF p.9 · [source](https://arxiv.org/pdf/2306.00890) |
| SLAKE — English | open_token_recall 51.0%; closed_accuracy 84.6% | LLaVA-Med 7B, CLIP, 60K-IM, stage1=1/stage2=3/FT=0: open token recall 39.17%; closed accuracy 52.16%; n=1061; Table 4(b), PDF p.9 · [source](https://arxiv.org/pdf/2306.00890) |
| PathVQA | open_token_recall 26.4%; closed_accuracy_corrected 0.8587 | LLaVA-Med 7B, CLIP, 60K-IM, stage1=1/stage2=3/FT=0: open token recall 12.3%; closed accuracy 54.05%; n=6761; Table 4(b), PDF p.9 · [source](https://arxiv.org/pdf/2306.00890) |
| ImageCLEF-VQA 2019 | strict_accuracy 0.0% | MedVInT-TE: overall accuracy 70.5%; Table 2 · [source](https://arxiv.org/html/2305.10415v6) |

Medical-image performance does not show use of protein sequence/structure embeddings. Open-answer scorers differ between papers. | Medical-image performance does not show use of protein sequence/structure embeddings. Open-answer scorers differ between papers. | Medical-image performance does not show use of protein sequence/structure embeddings. Open-answer scorers differ between papers. | Medical-image performance does not show use of protein sequence/structure embeddings. Open-answer scorers differ between papers.

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

### Scientific figure question answering

**Dataset/protocol:** PMC-VQA figure question answering

| Scientific setting | Local stored result | Published reference — different protocol |
|---|---|---|
| PMC-VQA held-out evaluation | native_td_final_character_accuracy 0.0200; adapted_full_text_closest_choice_accuracy 0.4975; adapted_full_text_released_label_accuracy 0.4975; strict_final_label_accuracy 0.0070 | MedVInT-TD / PMC-LLaMA / PMC-CLIP: choice accuracy 40.3%; blank accuracy 33.6%; blank bleu1 21.5%; n=2000; Table 3 · [source](https://arxiv.org/html/2305.10415v6) |

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

## Other biological modalities and molecular interactions

### Drug–target interaction

**Dataset/protocol:** Drug–target interaction: BioSNAP / Human / BindingDB

| Scientific setting | Local stored result | Published reference — different protocol |
|---|---|---|
| Drug–target interaction — BioSNAP/Human/BindingDB · bindingdb | AUROC 0.5036; AP 0.4103 | BioT5+ (supervised): AUROC 0.964 ± 0.001; Table 8 · [source](https://arxiv.org/html/2402.17810v2) |
| Drug–target interaction — BioSNAP/Human/BindingDB · biosnap | AUROC 0.5336; AP 0.5217 | BioT5+ (supervised): AUROC 0.939 ± 0.001; Table 8 · [source](https://arxiv.org/html/2402.17810v2) |
| Drug–target interaction — BioSNAP/Human/BindingDB · human | AUROC 0.4747; AP 0.4194 | BioT5+ (supervised): AUROC 0.987 ± 0.001; Table 8 · [source](https://arxiv.org/html/2402.17810v2) |

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

### Pathway and disease prediction

**Dataset/protocol:** BioReason KEGG pathway/disease

| Scientific setting | Local stored result | Published reference — different protocol |
|---|---|---|
| BioReason KEGG pathway/disease test | accuracy 0.0%; STRICT_FINAL_LABEL.accuracy 0.0%; STRICT_FINAL_LABEL.supplemental_macro_f1_fixed_global_vocabulary 0.0000; STRICT_FINAL_LABEL.supplemental_macro_precision_fixed_global_vocabulary 0.0000; STRICT_FINAL_LABEL.supplemental_macro_recall_fixed_global_vocabulary 0.0000 | Qwen3-4B: accuracy 90.0%; macro f1 79.66%; macro precision 88.24%; n=290; Table 1 · [source](https://arxiv.org/html/2505.23579v2) |

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

### Variant-effect prediction

**Dataset/protocol:** BioReason VEP coding and non-SNV

| Scientific setting | Local stored result | Published reference — different protocol |
|---|---|---|
| BioReason VEP-Coding | accuracy 49.1%; f1 0.5213; STRICT_FINAL_LABEL.accuracy 0.0%; STRICT_FINAL_LABEL.f1 0.0000 | Qwen3-4B: accuracy 48.99%; f1 39.58%; Table 2 · [source](https://arxiv.org/html/2505.23579v2) |
| BioReason VEP-Non-SNV | accuracy 89.0%; f1 0.9053; STRICT_FINAL_LABEL.accuracy 0.0%; STRICT_FINAL_LABEL.f1 0.0000 | Qwen3-4B: accuracy 61.86%; f1 67.6%; n=873; Table 2 · [source](https://arxiv.org/html/2505.23579v2) |

Genomics task, not Affibody binding; annotation confidence and splitting matter. | Non-SNV classification should not be merged with single-amino-acid design accuracy.

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

## Case studies and diagnostics

Case studies, predictor-scored optimization, component tests and internal diagnostics remain separate from independent main benchmarks.

### Protein function, annotations and descriptions — diagnostic appendix

#### Text-to-protein retrieval*

**Dataset/protocol:** ProtST text-to-protein retrieval examples

**Scope:** Registered · **Execution:** Status unverified. No local result is shown in this snapshot.

**Published evidence only:** Selected text-to-protein retrieval and docking case studies are reported; no single fixed-corpus Recall@K benchmark result is transcribed.

Retrieval case study Docking and known annotations support case analysis; they do not prove all retrieved candidates bind experimentally.

Case study or diagnostic; kept separate from independent benchmark results.

[Source 1](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf)

#### Functional explanation review*

**Dataset/protocol:** BioReason-Pro explanation review

**Scope:** Registered · **Execution:** Status unverified. No local result is shown in this snapshot.

**Published evidence only:** Repository reports an LLM-judge score of 8/10 and expert preference over UniProt descriptions in 79% of reviewed cases.

Judged explanation subset Correct GO labels do not guarantee that every intermediate statement is true.

Case study or diagnostic; kept separate from independent benchmark results.

[Source 1](https://www.biorxiv.org/content/10.64898/2026.03.19.712954v2.full)

### Mutation ranking, affinity and local optimization — diagnostic appendix

#### Iterative mutation optimization*

**Dataset/protocol:** MutaPLM iterative optimization

**Scope:** Registered · **Execution:** Status unverified. No local result is shown in this snapshot.

**Published evidence only:** The paper reports predicted-fitness improvement trajectories across six landscapes; these are oracle-based search outcomes, not experimentally measured hit rates.

Predictor-scored search experiment A learned scorer can be exploited; this experiment is not prospective laboratory success.

Case study or diagnostic; kept separate from independent benchmark results.

[Source 1](https://arxiv.org/html/2410.22949v1)

### Protein design — diagnostic appendix

#### Description-guided protein design*

**Dataset/protocol:** BioT5+ description-guided protein generation

**Scope:** Registered · **Execution:** Status unverified. No local result is shown in this snapshot.

**Published evidence only:** Description-guided protein designs are presented as qualitative cases rather than a fixed, experimentally validated design-success rate.

Qualitative design case A plausible or similar sequence is not a measured successful design.

Case study or diagnostic; kept separate from independent benchmark results.

[Source 1](https://arxiv.org/html/2402.17810v2)

#### Unconditional and property-conditioned protein design*

**Dataset/protocol:** NatureLM generated proteins: unconditional / property-conditioned / heme

**Scope:** Registered · **Execution:** Status unverified. No local result is shown in this snapshot.

**Published evidence only:** Reported outputs are diversity/length distributions and predicted structural confidence. No experimentally measured function-success fraction is supplied by this evaluation. The reported comparison uses learned stability/solubility scores and diversity. No measured stability/solubility success rate is transcribed. Selected heme-binding candidates are screened with descriptions and predicted complexes; this is not experimentally demonstrated heme binding.

Predictor-scored or qualitative design Diversity and predicted structure confidence do not establish function. | Predictor agreement, not experimentally measured stability/solubility of each generated sequence. | Self-description is not independent validation; predicted complexes are not measured binding.

Case study or diagnostic; kept separate from independent benchmark results.

[Source 1](https://arxiv.org/html/2502.07527v3)

#### Fluorescence sequence optimization*

**Dataset/protocol:** STRIDE GFP sequence optimization

| Scientific setting | Local stored result | Published reference — different protocol |
|---|---|---|
| STRIDE GFP generated-candidate evaluation* | replace_only.qualified_oracle_success 0.0000; replace_only.improved_sequence_uniqueness undefined; replace_only.native_novelty undefined; full_atomic.qualified_oracle_success 0.0000; full_atomic.improved_sequence_uniqueness undefined; full_atomic.native_novelty undefined | STRIDE: success count 61; attempt count 100; unique improved count 59; n=100; Table 4 · [source](https://arxiv.org/html/2603.03573v1) |

Predictor-scored generation These 100 candidates are not a wet-lab test set. Correctly applying edits does not validate fluorescence.

Case study or diagnostic; kept separate from independent benchmark results.

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

#### Text-conditioned target-binder design*

**Dataset/protocol:** Prompteina text-conditioned protein design — GM2A campaign

**Scope:** Catalog only · **Execution:** Status unverified. No local result is shown in this snapshot.

**Published evidence only:** 9 of 89 assayed designs classified as binders; 8 fitted apparent KD values. Strongest apparent KD: 107 nM.

Prospective experimental campaign A single target campaign, not a general fixed test set or aggregate success rate. 52.4M captions is a training size.

Case study or diagnostic; kept separate from independent benchmark results.

[Source 1](https://arxiv.org/html/2610.13917v1)

### Structure and conformational prediction — diagnostic appendix

#### Internal structural and alignment diagnostics*

**Dataset/protocol:** Proteo-R1 internal alignment / structural / CDR diagnostics

**Scope:** Catalog only · **Execution:** Status unverified. No local result is shown in this snapshot.

**Published evidence only:** Selected Stage-II M3: contact 58.3%; interface 15.1%; hotspot 11.6%. Separate Stage-I schema 81.4%. No overall score.

Internal diagnostic — holdout unresolved Not a named released PDB benchmark. Eight-response averages are not pass@8. No evidence of leakage is inferred from missing documentation.

Case study or diagnostic; kept separate from independent benchmark results.

[Source 1](https://arxiv.org/html/2605.02937v1)

### Biomedical visual evidence — diagnostic appendix

#### Document and figure extraction*

**Dataset/protocol:** Ryze document-extraction component tests

**Scope:** Registered · **Execution:** Status unverified. No local result is shown in this snapshot.

**Published evidence only:** Ryze extraction-component accuracy: ArXivQA 73.12%, SlideVQA 66.48%, ChartQA 75.8%.

Component ablation These tests evaluate extraction/document understanding, not protein engineering.

Case study or diagnostic; kept separate from independent benchmark results.

[Source 1](https://arxiv.org/html/2606.00902v1)
