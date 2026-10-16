# Biological evaluation overview

**25/64 registered settings have completed declared local runs.** The full inventory contains **67 main dataset/protocol groups** and **9 separate case-study/diagnostic groups**. These are different counting units; completing a declared local run does not establish full paper replication.

Stored scores: **2026-10-16T04:25:25.541726+00:00**. Running-work snapshot: **2026-10-16T07:35:08.569499+00:00**. These are timestamped reports, not a live feed.

Model: **Qwen/Qwen3.8-27B**, original BF16, served with **vLLM**. The execution snapshot records **8 GPU workers** covering **10 settings**, with **83,690 planned task-cases** and **294 saved responses**. Saved responses are not completed benchmark metrics, and task-cases are not independent biological observations.

- [Complete hierarchy and execution status](TASK_HIERARCHY_COMPLETE.md)
- [Grouped local results and published comparisons](RESULTS_GROUPED.md)
- [Task coverage crosswalk — all 64 registered settings](TASK_COVERAGE_MAP.csv)
- [Machine-readable hierarchy and source hashes](TASK_HIERARCHY_DATA.json)
- [Stored result report](RESULTS_AT_A_GLANCE.md) · [Execution snapshot](CURRENT_EXECUTION_STATUS_2026-10-16.json)
- [Uploaded trajectories](https://github.com/Some-random/bio-evaluation/tree/main/results/runs) · [Reporting package instructions](https://github.com/Some-random/bio-evaluation/blob/main/handoff/Bio_Evaluation_Agent_Package_2026-10-16/START_HERE.md)

## Browse by scientific capability

| Capability | Main dataset/protocol groups | Inventory | Results |
|---|---:|---|---|
| Protein properties, interactions and developability | 14 | [Browse](TASK_HIERARCHY_COMPLETE.md#protein-properties-interactions-and-developability) | [Browse](RESULTS_GROUPED.md#protein-properties-interactions-and-developability) |
| Protein function, annotations and descriptions | 7 | [Browse](TASK_HIERARCHY_COMPLETE.md#protein-function-annotations-and-descriptions) | [Browse](RESULTS_GROUPED.md#protein-function-annotations-and-descriptions) |
| Mutation-effect interpretation | 1 | [Browse](TASK_HIERARCHY_COMPLETE.md#mutation-effect-interpretation) | [Browse](RESULTS_GROUPED.md#mutation-effect-interpretation) |
| Mutation ranking, affinity and local optimization | 10 | [Browse](TASK_HIERARCHY_COMPLETE.md#mutation-ranking-affinity-and-local-optimization) | [Browse](RESULTS_GROUPED.md#mutation-ranking-affinity-and-local-optimization) |
| Scientific evidence and biological knowledge | 3 | [Browse](TASK_HIERARCHY_COMPLETE.md#scientific-evidence-and-biological-knowledge) | [Browse](RESULTS_GROUPED.md#scientific-evidence-and-biological-knowledge) |
| Protein design | 12 | [Browse](TASK_HIERARCHY_COMPLETE.md#protein-design) | [Browse](RESULTS_GROUPED.md#protein-design) |
| Structure and conformational prediction | 7 | [Browse](TASK_HIERARCHY_COMPLETE.md#structure-and-conformational-prediction) | [Browse](RESULTS_GROUPED.md#structure-and-conformational-prediction) |
| Biomedical visual evidence | 3 | [Browse](TASK_HIERARCHY_COMPLETE.md#biomedical-visual-evidence) | [Browse](RESULTS_GROUPED.md#biomedical-visual-evidence) |
| Other biological modalities and molecular interactions | 10 | [Browse](TASK_HIERARCHY_COMPLETE.md#other-biological-modalities-and-molecular-interactions) | [Browse](RESULTS_GROUPED.md#other-biological-modalities-and-molecular-interactions) |

[Case studies and diagnostics](TASK_HIERARCHY_COMPLETE.md#case-studies-and-diagnostics) remain separate. **Protein design** is the parent category for antibody design, inverse folding, binder design, generation and motif scaffolding.

## How to read the status

Scope and execution are separate fields. **Registered** identifies the original registered settings; **Catalog only** includes 36 additional main groups and does not authorize new experiments. A missing result stays **Status unverified** unless stronger evidence establishes a blocker or hold.

An **asterisk (*)** marks an incomplete group or result. Case counts, parsing failures, native metrics, alternate metrics and protocol qualifications appear in expandable details. An undefined metric stays undefined; it is not zero. Published references remain separate from local outcomes and use their own training and evaluation protocols.

The current snapshot flags frequent output-length stops on the fluorescence run. Its original 4,096-token cap and all stopped/invalid outputs are preserved. Outcome scores do not validate explanations, and public pretraining exposure is unknown.

Regenerate these pages with `python3 scripts/update_grouped_evaluation_reports.py`. This renders the reviewed JSON snapshot only; it does not launch or rescore an evaluation.
