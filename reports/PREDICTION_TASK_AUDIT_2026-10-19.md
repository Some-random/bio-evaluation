# Prediction-task audit: localization and drug–target interaction

Reviewed October 19, 2026. This audit interprets preserved outputs; it changes no model calls, parsers or native scores.

**P03 protein localization:** the saved result reproduces **724/2,773 correct (26.11%)**, with **2,722 accepted answers and 51 invalid answers**. Even if every invalid answer became correct while existing accepted predictions stayed fixed, accuracy could reach only **775/2,773 (27.95%)**. The largest reference class is nucleus, with **808/2,773 (29.14%)**. That last number is a descriptive test-set majority reference, not a trained baseline, selected classifier or proposed deployment.

The three most frequent predicted classes—cytoplasm, cell membrane and extracellular—account for **2,570/2,773 cases (92.68%)**, or **94.42% of accepted predictions**. For example, nucleus occurs 808 times in the reference but is predicted only 135 times. Formatting alone cannot explain the low accuracy when all existing accepted predictions stay fixed.

| Location | Reference cases | Accepted predictions | Correct |
|---|---:|---:|---:|
| Cell membrane | 273 | 884 | 212 |
| Cytoplasm | 508 | 1193 | 299 |
| Endoplasmic reticulum (ER) | 173 | 8 | 1 |
| Golgi apparatus | 70 | 0 | 0 |
| Lysosome/Vacuole | 64 | 1 | 0 |
| Mitochondrion | 302 | 5 | 1 |
| Nucleus | 808 | 135 | 71 |
| Peroxisome | 30 | 2 | 1 |
| Plastid | 152 | 1 | 0 |
| Extracellular | 393 | 493 | 139 |

The complete 10-by-11 confusion matrix, including an invalid-answer column, is in the [structured audit](PREDICTION_TASK_AUDIT_2026-10-19.json). All 2,773 saved case identities and targets match their pinned references in order; the original ten class IDs and ontology are retained. This result describes zero-shot prediction from raw sequences and differs from systems trained with protein representations and task heads.

**P43 drug–target interaction:** the adapter scores the first-token likelihood of `Yes` relative to `No` and uses the resulting continuous score for AUROC and average precision (AP), separately on each dataset. It does not rank pairs using sampled hard labels. A one-token length finish is intentional and is not an unfinished reasoning response.

| Dataset | Cases | AUROC | AP |
|---|---:|---:|---:|
| BindingDB | 9,840 | 0.50357 | 0.41032 |
| BioSNAP | 5,493 | 0.53356 | 0.52166 |
| Human | 1,200 | 0.47472 | 0.41943 |

These AUROCs indicate limited ranking discrimination under the declared adapter. AP needs the dataset's positive prevalence for a chance-level interpretation; prevalence was not freshly verified. The original P43 raw run folders are absent locally, so this audit checks retained score metadata and code rather than freshly reproducing likelihoods or metrics. Pair-normalized label-token likelihood is not a calibrated physical binding probability or an experimental affinity. The zero-shot adapter and supervised DrugBAN/BioT5 systems have different training and representations.

[Original P03 score](../results/runs/qwen38_27b_p03_full_test_slurm_2026-10-16/scores.json) · [P03 input and ontology preparation](../scripts/prepare_catalog_extended.py) · [P43 likelihood adapter](../scripts/local_dti_common.py#L85) · [P43 metric implementation](../scripts/local_dti_score.py#L12) · [Complete source hashes and audit records](PREDICTION_TASK_AUDIT_2026-10-19.json)
