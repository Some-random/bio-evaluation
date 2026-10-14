# Public biological evaluations

This workspace is for the eight prioritized protein settings P18, P23–P26,
and P30–P32. Preserve all original 64 IDs in readiness records.
The original handoff is retained under `handoff/`.

Preparation, public source acquisition, CPU-only dry runs, cost estimation,
and leakage checks are authorized. No paid inference budget is approved yet.
Read credentials only from the runtime environment; never print or save them.
Keep the separate Affibody data and evaluations unchanged.

Use official releases, splits, prompts, and scorers where verified. Mark
new text baselines as adaptations. Keep answers and reference explanations
out of requests. Never tune against protected test outcomes. PG-LLM is
native-only and evaluation-only. Preserve complete sequences.

Use synthetic or permitted development cases for tests. Record source versions,
hashes, coverage, failure counts, and estimated costs. Prior model exposure to
public benchmarks is unknown; do not claim contamination-free evaluation.
No new SSH connection is needed for this workspace. The standing limit is
at most one GPU; current preparation uses CPU only.

Read `/data/rustfs1/dongweij/EXECUTION_EXAMPLES.md` before further execution
or interpretation. Record task demands as provisional analyst descriptions
from inputs, output targets and reference evidence, independently of A–F
interface compatibility. Keep valid biological prediction tasks even where
learned protein representations may be essential.

Maintain `results/interpretation_notes.jsonl`, keyed by task ID and protocol
variant, and the separate interpretation table in `reports/`. Distinguish
prepared fields from exact information actually dispatched to the solver.
Separate outcome correctness from reference-supported explanation, unverified
hypothesis, missing support and contradiction. Correct predictions do not
validate rationales, and missing support does not automatically mean false.
The addendum's illustrative values/examples are not benchmark/training data
and do not authorize extra context or reasoning-budget variants. Preserve
native metrics, scope, budgets, restrictions and the existing original catalog.

On 14 October 2026 UTC the user authorized creating a private repository and
uploading this evaluation workspace daily. `scripts/daily_backup.py` commits
code/reports and compressed data/source/result snapshots; check
`reports/BACKUP_SETUP.md` and `.local/backup_status.json` for status. Credentials
stay local. This authorization does not approve paid inference or uploading
unrelated Affibody data. Never give a benchmark solver access to this repository
or its archives, which contain held-out evaluation material.
