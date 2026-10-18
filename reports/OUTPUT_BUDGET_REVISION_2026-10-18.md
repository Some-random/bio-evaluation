# Output budget and evaluation scope revision

Prepared October 18, 2026, 12:44 PM PDT. Human-readable times use Pacific time.

The remaining retained evaluations now use **16,384 output tokens**, increased from 4,096. The eight existing A100 80GB replicas continue on vLLM 0.32.0, with 64 queued requests per GPU and 95% GPU memory. Both new dispatchers started successfully, and both hosts passed their revised live health checks. The servers were retained through a clean producer handoff; no weight reload or vLLM restart was needed.

The truncation limit was the output budget. The server context remains 65,536 tokens: the largest reviewed input is 45,219 tokens, and input plus the new output allowance is 61,603. Increasing input context would not address those earlier output-limit finishes.

The prospective cohort contains **17,145 never-dispatched cases**. Only `max_tokens` changes; the original complete inputs, checkpoint, BF16 precision, sampling, seed and native metric formulas remain fixed. Every old response remains immutable, including truncated or invalid answers. No completed or ambiguous case is rerun.

| Retained task | Future cases at 16,384 output tokens |
|---|---:|
| P07 | 71 |
| P08 | 5,548 |
| P12 | 1,470 |
| P13 | 2,968 |
| P14 | 2,928 |
| P15 | 2,928 |
| P16 | 1,232 |

Whole-task scoring joins the complete original case order across the older 4K calls and the new 16K cohort. Results are explicitly labeled **mixed 4K/16K budget**; a task with no future 16K calls retains an all-4K label. The original invalid/missing cases stay in the full denominator. Parsed-only correlations or confidence diagnostics remain separately labeled, and an undefined full primary metric is not promoted to a complete benchmark score.

BioReason, BioReason-Pro and Bio-posttrain settings **N01–N05, P28 and P29** are set aside from the main comparison. P28/P29 received no further new admissions after the old queues were paused; their already-submitted calls drained and were preserved. The main presentation now contains **57 settings, 31 task families and 8 categories**. The original 64-setting catalog, raw outputs and scores remain in the [archive](ARCHIVED_EVALUATIONS.md).

Simple parser repair was tried independently of reference labels. Frozen formatting-only rules covered whitespace, Markdown/code fences and explicit terminal answer labels while preserving native valid predictions. Across **9,005 completed responses**, cleanup recovered **zero additional answers**. P08 had 7,130 valid scalars out of 7,251 completed responses. DeepFRI had 1,289 valid vectors out of 1,754; its 465 invalid responses comprised 407 missing/truncated/unfinished finals, 52 unknown classes or nonnumeric confidences, and 6 duplicate JSON keys. These are retained as invalid outputs. Reasoning is not mined for guessed answers.

The revised pipeline keeps per-minute endpoint, token-progress, response-integrity and output-format checks. Separate CPU scoring waits for complete original case unions and validates each case against its actual frozen output budget. Returned infrastructure errors stop new dispatch and preserve in-flight work. The revised trajectory publisher uses its own state and archives the new raw requests, responses, reasoning and serving provenance incrementally.

The previous completion estimate applied to the earlier 4K, BioReason-inclusive plan. Dropping tasks and raising output allowances both change the workload, so that estimate is superseded; a new estimate requires sustained progress under this revised plan.

[Live deployment snapshot, cohort counts and assumptions](OUTPUT_BUDGET_REVISION_2026-10-18.json) · [Frozen source, tests, cohort and parser evidence](benchmark_assets/output_budget_revision_2026-10-18.tar.gz) · [Main overview](EVALUATION_OVERVIEW.md).
