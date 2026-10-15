# Current evaluation situation

Status checked 15 October 2026 UTC. The complete Qwen3.8-27B BF16 checkpoint is
verified and running on one H200 (GPU 5). The first local benchmark run is complete:
**197 input-reviewed public LAB-Bench LitQA2 questions**. It achieved 77/197 correct
(39.1% accuracy), 41.0% precision and 95.4% coverage, with zero request/parser/truncation
failures. Two cases were held
before inference. Check the saved progress and final scores in
`results/runs/qwen38_27b_litqa2_public_reviewed_2026-10-15/` and the frozen plan in
`FIRST_LOCAL_EVALUATION.md`. The separate offline scorer and
request/output audit both passed. See `local_evaluation_status.json` for the completed status.

The catalog covers 64 biological settings, not 64 independent datasets. Previous
preparation and historical API results are separate from this Qwen baseline.
OpenAI inference remains suspended after the reported policy warning. Flagged
pathogen-fitness requests are not being transferred to the local model.

## Which evaluations are useful?

| Settings | Purpose and evidence | Practical priority and limit |
|---|---|---|
| B01: LAB-Bench LitQA2 | Answer questions about published biological findings; creator-curated multiple-choice references. | First local run: 197 reviewed public cases, exact prepared native prompts/choices, fixed generation settings, native accuracy/precision/coverage. Public-subset and single-run differences from the paper are explicit. |
| P18: ProteinGym-LLM | Rank candidate protein variants against held-out experimental fitness measurements. | Held after the policy incident; no local dispatch. It remains a valid biological prediction task, but blocked pathogen-fitness requests cannot be transferred. Native-only and evaluation-only restrictions remain. |
| P23–P26: protein descriptions | Predict function, catalytic activity, domains/motifs and general descriptions from full sequences. References are annotations/descriptions. | Useful complementary coverage. Prepared TEXT adaptations are separately labeled; lexical metrics do not independently validate every biological claim. |
| P30: mutation explanations | Produce a mutation-effect explanation against source effect descriptions. | Useful for explanation assessment after the exact text protocol is resolved. Prediction accuracy, reference wording and mechanistic support are different outcomes. |
| P31–P32: mutation engineering | Recover a reference substitution given a desired effect, with or without a supplied position. | Useful design/proposal tasks after protocol review. Reference recovery is not an experimental success rate; unannotated alternatives are unresolved. |

These priorities are analyst judgments based on the task contracts and evidence,
not a conclusion that a benchmark diagnoses a model's internal reasoning.
Prediction tasks remain valid where learned protein representations are needed.
An available specialist baseline can provide context, with its training and input
differences disclosed. No new encoder/head training is authorized.

## Execution path

The local LitQA2 runner, frozen manifest and offline native metric integration
are implemented. Seven synthetic contract checks passed; every selected prompt
matches the prepared native prompt byte-for-byte. Runtime requests contain no
answer-key fields. One generation is permitted per reviewed case; uncertain
interrupted requests are not silently resampled. No test outcomes choose models,
prompts or budgets. Complete native public inputs for all eight LAB-Bench categories are now prepared
in `data/labbench_native_complete/` (1,967 cases), including required images, titles/DOIs
and full protocols. Other tasks still require case review and frozen execution configs
before local dispatch.

Lock predictions before scoring. Use native splits, aggregation and invalid-output
rules; report coverage, failures, costs and exact versions. Keep adapted/native
protocols distinct and join results to the interpretation table by task and variant.
There is no proposed single aggregate biological-intelligence score.

## Tools

Preparation/scoring tools are part of the evaluation infrastructure. The tested
solver currently has no enabled tools. A future tool-assisted evaluation must
be permitted by that benchmark and separately declared before execution.
For example, a protein encoder computed from the supplied sequence provides
learned representations; a structure, annotation, MSA or predictor output can
change the evidence supplied and must be recorded. Log every tool's version,
arguments, returned information, failure and cost. Report the model-plus-tools
system's performance, without assigning a tool's contribution to the model alone.
PG-LLM remains native-only under the current execution scope, with no protected
test retrieval or benchmark-specific agent/tool tuning.

Before any tool-enabled solver is run, enforce its access at the process/tool
boundary: supply allowed inputs only and withhold scorer files, evaluation
archives, the backup repository and answer-bearing retrieval sources. This
runtime isolation has not yet been implemented; allowlist preparation tests
are already in place. A prompt saying not to read answers is not access control.

## Leakage and memorization

Three different problems need different controls. Input leakage is addressed
with task-specific field allowlists and serialization checks. Evaluation-driven
overfitting is addressed by freezing decisions before scoring, avoiding protected
test-driven prompt/model/tool selection, and using separate allowed development
fixtures. Prior closed-model exposure to public test data remains unknown and
cannot be removed by rewriting prompts or guaranteed absent by a black-box audit.

Public benchmark scores therefore retain an exposure-unknown qualifier. A
separate fresh holdout would use genuinely new measured outcomes or annotation
records, released after the selected model's documented cutoff, with the underlying
evidence checked for novelty. Hold out related proteins/assays according to the
scientific claim, seal labels and lock predictions before opening them. This
reduces known exposure risks; it does not prove unknown provider training data
are clean. No fresh measured holdout has been acquired yet.

The user canceled daily GitHub updates, and the scheduled upload remains disabled.
Local reports, configuration and outputs are retained for reproducibility. Any
evaluation archive contains held-out material and must stay outside solver
resources. See `MEMORIZATION_PROTOCOL.md` for the detailed evaluation controls.
