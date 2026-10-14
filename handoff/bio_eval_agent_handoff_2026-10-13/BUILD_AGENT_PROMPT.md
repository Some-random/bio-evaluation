# Prompt 2 — Build the evaluation harness

Use Prompt 1 / PROJECT_CONTEXT.md as the project context. Work in the agent's actual workspace; paths from the originating chat are not presumed to exist here.

Build an executable harness and dry-run it now. Do not stop at another literature survey.

## Work order

The proposed first wave is 14 catalog settings:
- P18: PG-LLM / ProteinGym-LLM.
- P30, P31, P32: MutaDescribe explanation and mutation-engineering tasks.
- P23–P26: four Mol-Instructions protein-to-text tasks.
- B01, B02, B03, B06, B07, B08: six LAB-Bench text categories.

This is an implementation priority, not a claim these releases are all already accessible. Continue with other available tasks if one source is blocked.

Next, consider the other compatible A/B rows (including P01/P02/P10/P11 and adapter-dependent property/GO tasks). PFArena P19–P22 must wait for verified official artifacts, not a recreated benchmark. Retain C/D/E/F settings with explicit deferred or blocked status; do not force them into TEXT.

## Source verification and protocol records

For every row, preserve its ID and verify:
- official source, license/use restrictions, version/commit, files and hashes;
- exact split and case identifiers; counts from the actual payload;
- source inputs, labels, preprocessing and biological numbering;
- permitted resources, demonstrations and context;
- official output format and scorer implementation;
- access status: verified_ready / blocked_data / blocked_protocol / adapter_required / deferred_scope.

Do not invent missing tests, resplit a dataset while claiming reproduction, or use the source training split as its held-out benchmark. Where the catalog and official source conflict, write CORRECTIONS.md with evidence and keep the discrepancy visible.

## Harness components

Implement small modules with tests, following existing repository conventions where possible:
1. Dataset adapters that expose model-facing data separately from scoring targets.
2. Prompt renderers for NATIVE and authorized NO_AUX/WITH_AUX variants.
3. Provider/model adapters with configurable, explicitly supplied model identifiers.
4. Immutable raw-response storage and deterministic parsers.
5. Official metric wrappers or documented reproductions, with synthetic/toy tests.
6. A dry-run/cost estimator and resumable inference runner.
7. An aggregation/reporting step.

Never assume “GPT-6” is a valid API model identifier. Resolve the actual provider/model/version from the user-configured environment and current official documentation. Do not replace an unavailable model silently or expose credentials. This handoff contains no API keys, budget approval or model weights.

If a biological model is unavailable, build the interface stub and record the dependency. Do not let it block the text baseline or substitute invented outputs. A prompted baseline is not a replication of a fitted supervised head. No new supervised-head fitting is authorized in this first pass.

## Prompt rendering requirements

Use the exact official prompts when they exist, especially on frozen evaluation-only releases. Generic templates in this package are only for new adapters with no prescribed prompt.

- Preserve complete required sequences, mutation windows, full candidate sets and conditions.
- Calculate actual context usage per model before a request. Overlength cases are explicit failures/ineligible cases; never silently truncate or let only one model see a shortened sequence.
- Do not place biological feature vectors into a text prompt and label it equivalent to native encoder input.
- Fix optional context field selection before looking at outputs; record provenance and timing.
- Preserve the original answer format. JSON wrappers are used only where they do not violate the official protocol.
- Do not request hidden reasoning or assume all models expose it. Store the model's returned final answer and available usage metadata. Use a fixed public-rationale condition only when the task itself needs an explanation.

## Dry-run tests before real API inference

Use artificial fixtures or official development/training examples only where permitted. For protected tests, do not debug prompts by viewing held-out answer performance. Inspect benchmark schemas and label-free rendering; test parsers/scorers on toy data.

Tests must cover:
- no scorer-only fields or reference rationales in model-facing payloads;
- exact sequence preservation and mutation numbering checks;
- ranked lists missing/duplicating IDs or containing hallucinated candidates;
- score direction, ties, constant predictions and official aggregation units;
- transport errors versus invalid model outputs;
- paired-variant case matching;
- finite numeric values and fixed label vocabulary;
- complete modality inputs, including table images;
- resumption without duplicate billed requests.

## Outputs before full inference

Write:
- manifest.json (data/model/scorer/prompt versions and hashes);
- per_task_readiness.csv, preserving all 64 IDs;
- benchmark-specific configs and prompt files;
- field_allowlists.json;
- tests/ plus their actual results;
- COST_AND_RUN_PLAN.md (call counts, lengths, budgets, and blocked items);
- CORRECTIONS.md / BLOCKERS.md where needed.

Cost/run parameters are not supplied here. If already approved in the user's environment, use those limits. Otherwise implement, test, and estimate without launching paid inference or a large GPU run. Report exactly the unresolved fields rather than asking again for information in the catalogs.
