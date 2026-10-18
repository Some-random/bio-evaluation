# Archived evaluation settings

[Main evaluation overview](EVALUATION_OVERVIEW.md) · [Complete original catalog](TASK_HIERARCHY_COMPLETE.md) · [Original result metadata](RESULTS_AT_A_GLANCE.json)

Scope decision: **2026-10-18 (Pacific time)**. BioReason, BioReason-Pro and Bio-posttrain settings are excluded from the main task map, displayed comparisons and main completion counts.

Set aside the complete family because native scoring/reference dependence or unrecovered native inputs make it unsuitable for the current main comparison. This is a task-family scope decision, not filtering individual cases or low scores.

Keep all original catalog entries, scores, references, interpretation records and saved trajectories unchanged. Exclude these settings only from the main presentation and main completion counts; do not delete or rescore artifacts.

This archive is a presentation record. Runtime changes are recorded separately; archived data are not silently removed from an original run's denominator.

| Setting | Dataset | Reason for setting aside |
|---|---|---|
| P28 | BioReason-Pro temporal GO test | BioReason-Pro is set aside with the complete family; severe output-budget/format limitations remain documented in original records. |
| P29 | Bio-posttrain species-held-out protein GO | Predictor-derived annotations occur in both allowed input context and augmented targets, so the native score does not isolate new function inference. |
| N01 | BioReason KEGG pathway/disease | Native continuation scoring accepts label words in reasoning; strict final-label validity is a separate diagnostic. |
| N02 | BioReason VEP coding and non-SNV | Native continuation scoring accepts label words in reasoning; strict final-label validity is a separate diagnostic. |
| N03 | BioReason VEP coding and non-SNV | Native continuation scoring accepts label words in reasoning; strict final-label validity is a separate diagnostic. |
| N04 | Bio-posttrain KEGG unseen-network holdout | Exact network-held-out inputs and split are not recovered; no substitute is presented as the native evaluation. |
| N05 | Bio-posttrain MEDEA expression-conditioned gene selection | Exact split, expression-vector alignment and native evaluator are not recovered. |

## Preserved dataset and result records

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

The original machine-readable catalog and coverage crosswalk retain all 64 settings. The main presentation retains 57 of those settings; catalog-only datasets and diagnostics remain in their scientific categories.
