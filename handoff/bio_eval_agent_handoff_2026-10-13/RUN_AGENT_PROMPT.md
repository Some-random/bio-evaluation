# Prompt 3 — Execute the frozen evaluation and summarize results

Use the already tested harness, PROJECT_CONTEXT.md, TASK_RULES.md, and approved runtime config. This instruction does not override any benchmark's use restrictions or existing cost limits.

1. Confirm exact model IDs, data revisions, native prompts, scoring code, case lists and cost caps. A human-friendly name is not a verified endpoint.
2. Freeze prompts and model choices before held-out scoring. Use development data or artificial fixtures for debugging. PG-LLM must not be used to optimize prompts or select a model.
3. Run the authorized scope. NATIVE comes first; run NO_AUX/WITH_AUX only for task configs that explicitly permit them. Default to no solver-side retrieval, structure prediction or browser access.
4. Keep model, dataset, protocol and context conditions separate in caches. Retry transport failures consistently within budget. Never selectively retry incorrect answers, ask another LLM to improve them, or pick the best completion using the gold label.
5. Save exact requests, raw responses, parsed predictions, status, token/cost metadata, and scorer version. Do not store secrets. Scoring references must not enter solver prompts.
6. Score with the original metric/aggregation. For a new adapter, report its protocol explicitly; do not claim to reproduce a trained-head or richer-modality system.
7. Invalid outputs must remain visible. Use an official penalty where specified. If a ranking/error case has no specified scoring rule, report the issue and conditional valid-only result as such; do not silently repair/drop it and publish a full benchmark score.
8. Report planned, eligible, attempted, completed, parsed, and scorable counts separately. Distinguish transport failures, context overflow, refusals and invalid answers. A low-coverage result cannot be presented as equal-coverage superiority.
9. Keep assay/target/family-level aggregation. Do not pool incomparable assay scores or average ROUGE, AUROC and Spearman into a “bio intelligence” number.
10. For permitted paired context variants, report each score, matched-case difference, sample size, coverage and uncertainty using the biological grouping unit; do not choose variants by inspecting their test results. Additional uncertainty analysis is a proposed supplement, not a substitute for the official metric.

Return:
- results/predictions.jsonl and results/raw_responses.jsonl;
- results/metrics_by_task_model_variant.csv;
- results/coverage_and_failures.csv;
- results/context_comparisons.csv for applicable matched pairs;
- REPORT.md: per-task results, known confounds, runnable/blocked coverage, and a small reference-grounded error analysis;
- the exact command/config needed to reproduce or resume each run.

Separate executed results from cited paper numbers. Note training-regime differences and unequal available information. Do not claim that good predicted structure, a recovered native sequence, an LLM-judged explanation, or a generated candidate's oracle score establishes experimentally measured function. Do not use results from evaluation-only benchmarks for prohibited model selection.

The final report should answer: what the tested systems can do under the stated inputs; where allowed auxiliary text helps; where richer biological inputs help; and what remains uncertain. It should not conclude in advance that a particular architecture, midtraining recipe, or synthetic-data strategy is necessary.
