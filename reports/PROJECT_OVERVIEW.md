# Current evaluation situation

Status checked 14 October 2026 UTC. We have a catalog of 64 biological settings,
with eight protein settings prioritized and 18,356 model-facing requests
prepared. These are settings, not independent datasets. No biological model
inference or scored comparison has been run. The OpenAI key authenticated
successfully; billable inference and quota remain untested.

## Which evaluations are useful?

| Settings | Purpose and evidence | Practical priority and limit |
|---|---|---|
| P18: ProteinGym-LLM | Rank candidate protein variants against held-out experimental fitness measurements. | Strong first test of biological prediction. Frozen native inputs are verified; runner and native metric integration still need completion. Agreement with measured ordering does not establish mechanism or contamination-free generalization. |
| P23–P26: protein descriptions | Predict function, catalytic activity, domains/motifs and general descriptions from full sequences. References are annotations/descriptions. | Useful complementary coverage. Prepared TEXT adaptations are separately labeled; lexical metrics do not independently validate every biological claim. |
| P30: mutation explanations | Produce a mutation-effect explanation against source effect descriptions. | Useful for explanation assessment after the exact text protocol is resolved. Prediction accuracy, reference wording and mechanistic support are different outcomes. |
| P31–P32: mutation engineering | Recover a reference substitution given a desired effect, with or without a supplied position. | Useful design/proposal tasks after protocol review. Reference recovery is not an experimental success rate; unannotated alternatives are unresolved. |

These priorities are analyst judgments based on the task contracts and evidence,
not a conclusion that a benchmark diagnoses a model's internal reasoning.
Prediction tasks remain valid where learned protein representations are needed.
An available specialist baseline can provide context, with its training and input
differences disclosed. No new encoder/head training is authorized.

## Execution path

Finish exact protocols, a resumable runner and native scorers. Verify parsing,
errors and metrics using synthetic or permitted development fixtures. Freeze
model, prompts, task inputs, case selection and resource budgets before scored
execution. The proposed pilot is 100 cases per task selected without labels;
use it to check the pipeline and coverage, not to choose models/prompts using
protected outcomes. A paid-run budget remains unapproved.

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

The daily private backup is for reproducibility and recovery. Privacy of the
repository does not make its contents safe to expose to a solver: it includes
held-out benchmark material. See `BACKUP_SETUP.md` for backup and authentication
status, and `MEMORIZATION_PROTOCOL.md` for the detailed evaluation controls.
