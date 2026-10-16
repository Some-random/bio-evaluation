# Biological evaluation results by scientific capability

[Overview](EVALUATION_OVERVIEW.md) · [Complete inventory](TASK_HIERARCHY_COMPLETE.md) · [Coverage crosswalk](TASK_COVERAGE_MAP.csv)

Stored scores: **2026-10-16T13:49:27.755824+00:00**. Running-work snapshot: **2026-10-16T11:23:26.367254+00:00**. These are timestamped reports, not a live feed.

Only existing stored local outcomes are shown. The category order matches the complete inventory. **\*** marks incomplete coverage or scoring; count records are in expandable details. Undefined values remain undefined. Published values are separate contextual comparisons, not matched replications, pooled scores or claims of superiority. All reference records and alternate metric values are retained in the details.

A declared run may be complete despite invalid answers when its native scorer explicitly counts invalid answers in the denominator. That is different from an undefined native primary metric; finished runs with undefined primary metrics are labeled diagnostics separately below.

## Protein properties, interactions and developability

### Subcellular localization

**Dataset/protocol:** DeepLoc — binary and 10-compartment localization

| Scientific setting | Local stored result | Published reference — different protocol |
|---|---|---|
| Subcellular localization — DeepLoc | accuracy 26.1% | ProtST-ESM-1b: fixed encoder.accuracy 82.0%; full model tuning.accuracy 78.73%; Table 2, printed p.6 · [source](https://proceedings.mlr.press/v202/xu23t/xu23t.pdf) |

Binary comparison uses task-tuned systems. Ten-class numbers use frozen encoders + trained heads. These are distinct endpoints.

Published ten-class count is 2,768; the frozen local run contains 2,773 cases. These source-specific counts are retained separately.

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

## Protein function, annotations and descriptions

No completed local result in this stored score snapshot. [The inventory](TASK_HIERARCHY_COMPLETE.md) retains running, blocked, held and unverified protocols.

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
| LAB-Bench / SuppQA | accuracy 37.8%; precision 39.2%; coverage 96.3% | GPT-5.2: accuracy 48.8%; n=82; Table 1 · [source](https://arxiv.org/html/2606.00902v1) |
| LAB-Bench / FigQA | accuracy 72.4%; precision 72.8%; coverage 99.4% | GPT-5.2: accuracy 36.5%; n=181; Table 1 · [source](https://arxiv.org/html/2606.00902v1) |
| LAB-Bench / TableQA | accuracy 88.1%; precision 90.0%; coverage 98.0% | GPT-5.2: accuracy 36.9%; n=244; Table 1 · [source](https://arxiv.org/html/2606.00902v1) |

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

## Protein design

No completed local result in this stored score snapshot. [The inventory](TASK_HIERARCHY_COMPLETE.md) retains running, blocked, held and unverified protocols.

## Structure and conformational prediction

No completed local result in this stored score snapshot. [The inventory](TASK_HIERARCHY_COMPLETE.md) retains running, blocked, held and unverified protocols.

## Biomedical visual evidence

No completed local result in this stored score snapshot. [The inventory](TASK_HIERARCHY_COMPLETE.md) retains running, blocked, held and unverified protocols.

## Other biological modalities and molecular interactions

No completed local result in this stored score snapshot. [The inventory](TASK_HIERARCHY_COMPLETE.md) retains running, blocked, held and unverified protocols.

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

**Scope:** Registered · **Execution:** Status unverified. No local result is shown in this snapshot.

**Published evidence only:** Fixed fluorescence-oracle successes: full edit setting 89/100 for STRIDE vs 42/100 SFT; replace-only 61/100 vs 55/100 SFT.

Predictor-scored generation These 100 candidates are not a wet-lab test set. Correctly applying edits does not validate fluorescence.

Case study or diagnostic; kept separate from independent benchmark results.

[Source 1](https://arxiv.org/html/2603.03573v1)

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
