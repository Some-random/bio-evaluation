# Biological evaluation workspace

**Start here: [Evaluation overview](reports/EVALUATION_OVERVIEW.md)** — grouped results, the complete task inventory, execution status, and trajectories in one GitHub view.

Foundation-model papers and literature notes live in the [shared biological
foundation-model catalog](https://github.com/Some-random/paper-extraction-lab/blob/main/reports/bio_foundation_review_2026-10-15/README.md).
It combines model sources, training datasets and amounts, extraction/curation,
figure and citation handling, and disclosure gaps in one entry per model.
This workspace retains evaluation protocols and run provenance.

Private research workspace covering 64 biological evaluation settings. The first local Qwen3.8-27B run completed on 15 October 2026 UTC: **197 reviewed public LAB-Bench LitQA2 questions, 77 correct (39.1% accuracy), 41.0% precision and 95.4% coverage**. No requests failed and all outputs parsed. This is one seeded public subset run; explanation support is unassessed and pretraining exposure is unknown.

- [Grouped results](reports/RESULTS_GROUPED.md) — local scores and published references organized by capability and scientific task.
- [Complete task inventory](reports/TASK_HIERARCHY_COMPLETE.md) — all 67 main groups and 9 diagnostic groups, including tasks without results.
- [Coverage crosswalk](reports/TASK_COVERAGE_MAP.csv) — every catalog group and all 64 registered setting IDs.
- [Reporting package and instructions, 16 October](handoff/Bio_Evaluation_Agent_Package_2026-10-16/START_HERE.md) — the master inventory covers 67 main dataset/protocol groups; these are distinct from the 64 registered settings.
- [Results at a glance](reports/RESULTS_AT_A_GLANCE.md) — incomplete coverage or scoring is marked with an asterisk; counts remain in the structured report.
- [Execution snapshot, 16 October at 07:35 UTC](reports/CURRENT_EXECUTION_STATUS_2026-10-16.json) — eight GPU workers active across the frozen queue for ten settings; this is a dated snapshot, not a live status page.
- [Run artifacts and incremental trajectories](results/runs)
- [First local results and paper context](reports/FIRST_LOCAL_EVALUATION.md)
- [Current evaluation overview](reports/PROJECT_OVERVIEW.md)
- [Task demands and score interpretation](reports/INTERPRETATION_TABLE.md)
- [Readiness of all 64 settings](reports/per_task_readiness.csv)
- [Leakage and memorization controls](reports/MEMORIZATION_PROTOCOL.md)
- [Verified checkpoint and server setup](reports/LOCAL_MODEL_SETUP.md)
- [Native LAB-Bench input corrections](reports/LABBENCH_NATIVE_INPUT_REVIEW_2026-10-15.md)
- [Private snapshot and restore instructions](reports/BACKUP_SETUP.md)

The grouped reports organize capability → scientific task → dataset/protocol, keep **Protein design** as a parent category, and distinguish registered scope, execution status, local results and published references. The package is a reporting and coverage update; catalog inclusion does not authorize a new experiment. Its bundled results snapshot is historical. See the [package verification record](reports/reporting_package_receipt_2026-10-16.json).

All eight public LAB-Bench categories have complete native preparation (1,967 cases), including required figure/table images, paper titles/DOIs and full protocols. Current execution evidence is recorded in the dated snapshot above; preparation, a saved response and a completed native metric are separate states. The OpenAI inference hold and held pathogen-fitness requests remain in place. This repository is an archive and working record, not permission to run unreviewed tasks or change native benchmark restrictions.

Code, configurations, reports, handoff materials and interpretation metadata are stored directly in Git. `artifacts/manifest.json` inventories the compressed snapshot of all data, sources, raw requests/responses, results and logs. Parts in `artifacts/` remain below GitHub's individual-file limit. The public BF16 Qwen checkpoint stays local, as requested. Its exact repository, pinned revision, file digests, precision and serving configuration are preserved in [the verification record](reports/local_model_complete_verification.json) and [the model configuration](configs/local_model.json). No checkpoint weight assets are uploaded.

Credentials, model weights, virtual environments, package/build/download caches and transient process state remain local. Model references, evaluation data and work are preserved in this repository. No unrelated Affibody workspace is included. Automatic daily snapshot uploads remain disabled; explicitly authorized incremental trajectory uploads are active for the running evaluations.

This repository and its archives contain scorer-only reference answers. Keep them outside solver tools, training and retrieval corpora. Task-demand labels remain provisional; outcome agreement does not establish explanation correctness. Read [the execution addendum](handoff/EXECUTION_EXAMPLES.md) and `AGENTS.md` before continuing. The addendum's illustrative examples are not benchmark data.
