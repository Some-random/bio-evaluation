# Task-specific delivery requirements

Updated October 19, 2026, Pacific time. These are review requirements for separately named future experiments, not authorization to dispatch a new run. Unfinished catalog tasks, offline repairs and optional repeated evaluations remain separate workstreams.

The shared synthetic pilot passed 12 simple checks using only 53–112 output tokens per response. Repeated neutral padding, arithmetic, copied confidence values and a ten-residue edit establish basic serving and formatting. They do not establish answer delivery for a difficult biological task and do not unlock all full evaluations.

The subsequent real GFP validation pilot finished **12/12 responses**, with **10 normal, finite numeric finals** and **two output-cap finishes with empty finals**. There were no transport errors. This falls short of complete answer delivery even on twelve examples; biological correctness was not assessed. It does not establish a reliable full 27,217-case procedure. [Complete evidence](GFP_VALIDATION_DELIVERY_2026-10-19.md).

| Task | Required evidence before reviewing a full run | Current decision |
|---|---|---|
| B08 cloning — 33 cases | Cloning development/examples using the actual prompt structure, relevant long inputs and native answer-tag parser; then freeze the full configuration. | First small complete QA candidate. Source identity and context checks pass; cloning-specific delivery remains untested. |
| B07 sequence QA — 600 cases | Permitted development examples covering representative sequence lengths and source question types; demonstrate native final-answer delivery and record cost. | Next QA priority after its own checks. |
| P42 GFP design — 200 candidate slots | Full-length candidates under both replace-only and full-action regimes, native candidate/operation validation, task-specific sampling and explicit per-slot randomness. | Separate generation branch. The shared toy-edit pilot is insufficient. |
| P16 reaction — 5,651 cases | Actual sequence-plus-joint-class-description development prompts, reliable final class delivery, and a stated question the rerun would resolve. | Defer the large rerun. Recovering 850 labels added only three correct predictions, so parsing alone is not a strong reason to repeat it. |
| P07 fluorescence — 27,217 cases | Publish the real-validation results, characterize finite-scalar delivery and actual cost, and freeze how residual failures affect reporting before the full run. | Last large rerun. Current real-validation delivery is 10/12; even 12/12 would not guarantee full-test coverage. |
| P08 stability | Complete the sensitivity, invalid-format and score-direction audit using existing outputs. | Deprioritize a full rerun whose only purpose is parser repair. |
| P12–P15 protein function | Failure-type/vocabulary analysis and matched-subset comparisons are complete. Any revised interface must address the observed failure categories. | P12 mainly needs completion delivery; P13–P15 primarily need label/schema checks before a new experiment. |

For P42, the retained historical sampling is temperature 0.7, top-p 0.9, top-k −1, with thinking enabled. The shared pilot instead used temperature 1, top-p 0.95 and top-k 20. A new experiment must explicitly choose and freeze its task-specific settings, output allowance, two 100-slot regimes and per-slot randomness. Do not silently substitute the generic pilot's shared seed or sampling parameters. Any oracle success remains success against a trained fluorescence proxy, not an experimental result.

Every new run needs its own reviewed case manifest, model/checkpoint identity, prompt and parser contract, sampling settings, failure policy and run ID. Choose development examples without held-out correctness, preserve complete required inputs, report the whole development set, and keep original generations and scores. A successful delivery check is evidence for a particular interface; it is not by itself dispatch authorization or evidence of biological correctness.

The rule withholding a full score when any prediction is invalid is the local evaluation's completeness policy. It is separate from the numerical metric formula. Clearly named subset analyses and sensitivity bounds can still be informative, but cannot silently replace the original full-score record.

[Machine-readable requirements](../configs/task_specific_delivery_gates_2026-10-19.json) · [Current action plan](EVALUATION_REPAIR_PLAN_2026-10-19.md)
