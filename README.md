# Biological evaluations

**Review the completed work:** [Results, findings, methodology and audit evidence](reports/COMPLETED_WORK_REVIEW.md).

## [All tasks and results](reports/EVALUATION_OVERVIEW.md)

**Model: Qwen3.8-27B.** The overview starts with 31 task families in 8 categories, then one correct answer and one simple question with a substantial tool workflow. Dataset details remain in collapsible categories.

- [More worked examples, complete saved reasoning and tool workflows](reports/WORKED_EXAMPLES.md)
- [External models actually used in the papers](reports/PUBLISHED_TOOL_USE_EXAMPLES.md)

<details>
<summary>Source data and technical records</summary>

- [Run artifacts and trajectories](results/runs)
- [Machine-readable task and result snapshot](reports/TASK_HIERARCHY_DATA.json)
- [Task ID crosswalk](reports/TASK_COVERAGE_MAP.csv)
- [Execution snapshot](reports/CURRENT_EXECUTION_STATUS_2026-10-16.json)
- [Reporting package](handoff/Bio_Evaluation_Agent_Package_2026-10-16/START_HERE.md)
- [Model verification and setup](reports/LOCAL_MODEL_SETUP.md)
- [Original result records](reports/RESULTS_AT_A_GLANCE.json)
- [Archived BioReason and Bio-posttrain evaluations](reports/ARCHIVED_EVALUATIONS.md)
- [Interpretation and task requirements](reports/INTERPRETATION_TABLE.md)
- [Leakage and memorization controls](reports/MEMORIZATION_PROTOCOL.md)
- [Backup and restore instructions](reports/BACKUP_SETUP.md)
- [Shared biological model literature catalog](https://github.com/Some-random/paper-extraction-lab/blob/main/reports/bio_foundation_review_2026-10-15/README.md)

Model weights and credentials stay local. This public repository contains scorer reference answers; keep it outside benchmark solver tools and training or retrieval corpora. Existing execution restrictions are recorded in `AGENTS.md`.

</details>
