# Start here — consolidated biological-evaluation reporting package

## Assignment

Read `TASK_HIERARCHY_AGENT_BRIEF.md`, then reorganize the existing evaluation reports as:

**Higher-order capability → actual scientific task → dataset / protocol → status and results.**

Use **Protein design** as the higher-order category. Antibody design belongs beneath it, including
H3 redesign (RAbD), multi-CDR redesign (the specified SAbDab holdout), and other antibody/binder tasks.
Do not remove tasks merely because they are absent from the supplied results snapshot.

**This is a reporting and coverage pass only: no rescoring, troubleshooting, model calls, training,
new paid runs, or new experimental work.**

## What is inside

| File | Role |
|---|---|
| `TASK_HIERARCHY_AGENT_BRIEF.md` | The current reporting instructions and completeness/status rules |
| `Biological_Evaluation_Master.xlsx` | Full available research inventory, metric definitions, source links, limits, and old-ID mapping; design labels updated |
| `EVALUATION_INVENTORY.csv` | Flat export of the master's `Filter and trim` sheet |
| `AGENT_TASK_MAPPING.csv` | Export of all existing rows in the master's `Agent mapping` sheet |
| `LEGEND.csv` / `LIMITS.csv` | Exact exported source legend and limitations |
| `RESULTS_AT_A_GLANCE.md` | The uploaded local-results snapshot, copied unchanged |
| `snapshot_view/TASK_HIERARCHY.md` | Earlier, narrower results-only layout; name updated, but not a complete task list |
| `snapshot_view/Evaluation_Task_Hierarchy.xlsx` | Earlier grouped-results workbook, with the design label updated; scores unchanged |
| `MANIFEST.json` / `SHA256SUMS.txt` | Source/validation notes and archive-content checksums |

No need to attach these files individually; they are all in this package.

## Inventory and result status are separate

The full master is an inventory of datasets and published references, not evidence of local execution.
The snapshot is evidence of reported local runs, not the complete inventory.

Produce a complete task inventory and a filtered results-available view using the same hierarchy.
Show missing/blocked/deferred/catalog-only tasks explicitly. Preserve exact protocol versions,
case counts, alternative metrics and existing qualifications in the supporting details. Keep internal
IDs in the crosswalk, not in human-facing task names.

Proteo-R1 is a model, not a parent task category. Its unresolved structure-reading diagnostics remain
in a separate appendix rather than being relabeled as a verified public benchmark.

## Existing repository materials

Use the actual `task_registry.json`, execution matrix, `LOCAL_SUITE_RESULTS.md`, and run artifacts
in your repository if available. The full old execution ZIP and historical final-run reports were
not available in this repackaging and are not fabricated here. The master crosswalk is retained,
but it does not replace exact runtime configuration.

Relative links in `RESULTS_AT_A_GLANCE.md` refer to the originating repository's `reports/` and
`results/` files; those linked run files are not bundled. Resolve links against your checkout.

Some older conversation uploads have expired. Re-upload any missing older files needed for a
historical comparison. Do not call a missing artifact an empty result or evidence that a task never ran.

## Deliverables from the agent

Follow the brief to produce:
- `TASK_HIERARCHY_COMPLETE.md`
- `RESULTS_GROUPED.md`
- `TASK_COVERAGE_MAP.csv`

Leave original run plans, scores and approved execution budgets unchanged.

## Scope of this repackaging

Only top-level design labels and the associated instructions were edited.
All source data counts, reported scores, individual benchmark names and task mappings were retained.
No new scientific literature or model results were introduced.
