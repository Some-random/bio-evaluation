# Agent brief: complete task hierarchy, not just completed results

Date: 2026-10-16

## Current naming decision

Use **Protein design** as the parent category. Antibody design remains included as a lower-order task. This is a label change, not a scope reduction.

## Purpose

Reorganize the evaluation report into higher-order capabilities, lower-order scientific tasks, and actual datasets/protocols. This is a reporting and coverage pass. Do not rescore, rerun, repair evaluations, start new training, or expand paid execution as part of this request.

The previous `snapshot_view/TASK_HIERARCHY.md` was a view of the current results snapshot, not a complete inventory. It must NOT be used as an allowlist, replacement task registry, or evidence that omitted tasks have been abandoned.

## Inputs and their roles

| Input | Role |
|---|---|
| `Biological_Evaluation_Master.xlsx` | Broader catalog of previously discussed datasets/protocols. Inspect `By category`, `Agent mapping`, `Cases and diagnostics`, and `Limits`. Its reported scores are literature references, not our executed results. Inclusion in the catalog does not mean approved for immediate execution. |
| Existing `task_registry.json` / execution matrix in your working repository | Stable execution-task IDs and approved scope. Preserve these; keep their IDs out of the human-facing task names. The old registry itself was not available for this repackaging; `AGENT_TASK_MAPPING.csv` is a source-derived crosswalk, not a replacement configuration. |
| `RESULTS_AT_A_GLANCE.md` | Supplied snapshot of local results. Not the authoritative list of all tasks. |
| `LOCAL_SUITE_RESULTS.md` and validated local artifacts, when available | Evidence about execution status and completed local runs. Do not presume they are accessible merely because the snapshot links to them. |
| Previous `snapshot_view/TASK_HIERARCHY.md` | An example of the desired category → task → dataset display. Its reduced scope is not intentional project prioritization. |

If an input is unavailable, state which one is missing and limit the completeness claim accordingly. Do not invent its contents or silently treat the subset you can read as the full inventory.

## Coverage pass

1. Reconcile the broader master catalog, the existing execution registry and the actual results. Include catalog-only tasks as such, rather than silently removing them or scheduling them automatically.
2. Preserve every dataset/protocol from the master and every registered execution task. Several can share a scientific-task row, but each result/status must still map back to its exact dataset, split, model and run.
3. Create a complete inventory view and a results-available view, using the same hierarchy. The latter is a filter of the former, not a different task list.
4. Use `Protein design` as the higher-order design category throughout. Antibody design is a lower-order protein-design task, not a separate sibling category. Keep antibody H3 redesign, multi-CDR redesign, de novo binder design, motif scaffolding, inverse folding, and other protein-design tasks visible underneath it; STRIDE GFP is only one subtask. Retain other high-level labels where they fit. Give mutation explanation/ranking and structure/conformation tasks appropriate parent categories. Do not put protein mutation-design tasks under DNA variant classification just because both contain the word 'variant'.
5. Group by scientific capability, not by which paper happens to have results. Do not create a special top-level category for Proteo-R1 or any other model.
6. Generate a coverage crosswalk: every original registry ID and every master dataset/protocol maps either to a main row or to a clearly labeled case/diagnostic appendix. Keep internal IDs in this crosswalk, not in presentation labels.
7. Leave all recorded scores unchanged. Keep local results and published reference numbers in separate columns. Preserve alternate metrics and qualifications in details; do not pick a more favorable scorer while reorganizing.

## Status rules

Use two distinct status fields:

- **Scope:** already approved/registered, catalogued only, or unresolved. Use the existing execution plan for approval status.
- **Execution:** result available; partial; source-blocked; explicitly deferred; not run (only when execution records confirm this); or not reported in this snapshot/status unverified.

A blank result or absence from `RESULTS_AT_A_GLANCE.md` is NOT evidence that the task has never run. Undefined is not zero. An existing number in the master workbook is not evidence that our agent ran the model.

The uploaded snapshot explicitly mentions PFArena, the Bio-posttrain KEGG network split and the MEDEA adaptation as source-blocked. It mentions a separate Bio-posttrain protein-function audit that is NOT a Qwen result. Preserve those distinctions in the inventory even though they were absent from the earlier small hierarchy.

## Where the Proteo-R1-related entries belong

| Higher-order category | Scientific task | Dataset/protocol | Treatment in this report |
|---|---|---|---|
| Protein design | Antibody H3 sequence/structure redesign | RAbD, with the exact paper-specific retained set | Already catalogued as P40. No local result appears in the supplied snapshot. Recover current execution status; do not delete it. |
| Protein design | Multi-CDR sequence/structure redesign | Proteo-R1's SAbDab holdout, with fixed antigen/framework/docking context | Already catalogued as P41. No local result appears in the supplied snapshot. Exact processed holdout availability must be checked. |
| Separate internal-diagnostics appendix | Structure-reading questions, grouped together | Proteo-R1's PDB-derived structural questions: contacts, distances, interfaces, etc. | The existing master flags the independent held-out manifest/protocol as unresolved. Do not present it as an established released evaluation dataset or create separate headline benchmark rows for each diagnostic. |

The broader master also contains inverse folding, backbone/sequence generation, motif scaffolding, epitope-conditioned antibody design and de novo binder design. Retain them in the appropriate inventory category, without treating their inclusion as authorization to run them.

Related antibody-generation protocols can use different retained RAbD sets; do not collapse the 60-complex and ProteinBench 55-complex versions into one result denominator.

## Other examples missing from the small snapshot hierarchy

- PG-LLM / ProteinGym variant ranking and MutaDescribe explanation/engineering.
- PFArena mutation proposal/ranking settings.
- GO/EC function prediction and the BioReason-Pro-related settings.
- LAB-Bench ProtocolQA.
- Broader protein/antibody design and structural-prediction protocols in the master.

This list illustrates the omissions; it is not a substitute for checking every row of the master and execution registry.

## Output

Produce:

1. `TASK_HIERARCHY_COMPLETE.md`: category → scientific task → dataset/protocol → scope → execution/result status. Include tasks without results; do not display opaque IDs in the task names.
2. `RESULTS_GROUPED.md`: the same category/task order with local scores, matched published references, case counts and links. It may filter to available results, but must explicitly link to the complete inventory.
3. `TASK_COVERAGE_MAP.csv`: source master row/group, original registry ID where applicable, display category/task/dataset, scope, status and supporting artifact. Explain any mapping ambiguity; do not drop rows silently.

Do not alter the existing run plan. No score calculations, model calls or new experiments are requested by this reporting change.

## Provenance

This brief is a presentation/coverage correction based on the uploaded `TASK_HIERARCHY.md` (bundled under `snapshot_view/`), `RESULTS_AT_A_GLANCE.md` and `Biological_Evaluation_Master.xlsx`. It is not a fresh verification of the benchmark papers or the current execution workspace. The source snapshot may be older than the agent's current artifacts; use verified run records to update status, not assumptions.
