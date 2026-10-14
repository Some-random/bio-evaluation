# Protein-first biological evaluation preparation

Prioritized settings: P18, P23–P26 and P30–P32.

- [Cost and run plan](reports/COST_AND_RUN_PLAN.md)
- [Memorization protocol](reports/MEMORIZATION_PROTOCOL.md)
- [Machine-readable cost calculations](reports/cost_estimate.json)
- [Readiness of all 64 settings](reports/per_task_readiness.csv)
- [Task demands and score interpretation](reports/INTERPRETATION_TABLE.md)
- [Private repository and daily backup](reports/BACKUP_SETUP.md)
- [Current evaluation overview](reports/PROJECT_OVERVIEW.md)
- [Full interpretation table](reports/interpretation_table.csv)
- Interpretation metadata keyed by task and protocol variant: `results/interpretation_notes.jsonl`
- Original handoff: `handoff/bio_eval_agent_handoff_2026-10-13/`

Verified public test inputs and draft label-separated text adapters are
available. Eight synthetic leakage/serialization tests pass. Preparation
uses CPU and no API credentials or paid model calls. The inference runner,
metric wrappers, and final MutaDescribe text-protocol review remain pending.

```bash
python3 -m unittest discover -s tests -v
python3 scripts/preflight.py
python3 scripts/interpretations.py
```

`configs/proposed_run.json` is an unapproved proposal, not an execution command.
Do not use protected outcomes to select models or tune prompts.

Read `/data/rustfs1/dongweij/EXECUTION_EXAMPLES.md` before continuing.
Demand classifications are provisional and independent of text-interface
compatibility. Keep valid prediction tasks, including those that may require
learned protein representations. Outcome correctness and explanation support
are recorded separately; unsupported mechanisms are not automatically false.
The addendum's examples are never benchmark data or ablation authorization.

The daily private-backup workflow is separate from benchmark inference. It
preserves this evaluation workspace, including compressed inputs, cached sources
and results, while keeping credentials and transient state local. GitHub server
authentication is required for repository creation and unattended pushes.
Backups contain evaluation material and must not become solver context or
training/retrieval data.
