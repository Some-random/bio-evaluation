# Scoring completed tasks while generation continues

The scoring bridge now accepts a completed task without waiting for every task
on its GPU host to finish. It validates the frozen completion/provenance records,
physically copies the complete original response union, verifies those bytes
before and after sealing, and passes that fixed snapshot to the unchanged native
scorer. A serial watcher uses the existing ownership lock, task specs, output
directories and terminal-state records; competing locks wait rather than become
scoring failures. Each native scoring attempt remains limited to one.

Native parsers, metric formulas, case denominators and each case's recorded
4,096- or 16,384-token output budget are unchanged. Historical invalid/truncated
outputs remain included. No model cases are rerun.

The preserved synthetic logs record **11 passing bridge tests and 9 passing
watcher tests**, covering immutable inputs, completion/provenance checks,
unchanged native invalid-answer accounting, concurrent ownership, state
continuity, code pins and no-repeat behavior.

[Exact code, contracts, dependency hashes and test logs](benchmark_assets/scoring_completion_bridge_2026-10-18.tar.gz)
· [Package manifest](SCORING_COMPLETION_BRIDGE_2026-10-18.json)
