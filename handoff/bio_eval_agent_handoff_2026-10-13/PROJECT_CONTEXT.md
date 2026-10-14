# Prompt 1 — Project context and comparison definitions

We are building an evaluation foundation for Dongwei Jiang's protein / AI-for-science data project with Yejin Choi, collaborating with Fang. The eventual question is whether better biological training data helps models use biological knowledge and molecular inputs on useful tasks. The current job is to establish reproducible baselines and locate capability gaps. Do NOT train, fine-tune, synthesize a training corpus, or optimize prompts on test outcomes in this assignment.

Read:
- references/evaluation_catalog.json: original 64 biological settings plus 14 separately listed general-control groups.
- references/text_model_compatibility_64.csv: source-preserving A–F compatibility classification.
- TASK_RULES.md and task_registry.json: task-specific execution instructions added for this handoff.

The catalogs are previous research notes, not ground truth or proof of execution. Their source URLs, splits, counts and access claims need verification against the actual official release before a task runs. Keep the original fields and log corrections rather than silently rewriting them. They contain no raw benchmarks or predictions. A missing or expired source is a blocker for that source only.

## Objective

1. Benchmark existing frontier LLMs through a text-only interface on compatible protein / biological tasks.
2. Where a working checkpoint and native evaluator are available, compare relevant specialist protein or protein–language models in separately labeled tracks.
3. Where the benchmark permits, measure the benefit of auxiliary biological text, separately from the effect of the input interface.
4. Produce per-task evidence about strengths, errors and limitations that can inform later data work. Do not select or train a model using evaluation-only suites that forbid that use.

## Two axes — do not call both “text vs no text”

Axis A: model input interface.
- TEXT: ordinary text, full amino-acid/DNA strings, and the benchmark-permitted textual inputs. No images, hidden protein embeddings, predicted structures or browser/tool calls by default.
- BIO: an existing system that consumes biological representations through its native encoders. Record whether these are derived only from the same sequence or also use extra structures, MSAs, database annotations or predictors.
- VISION: image-input tasks, kept separate from TEXT and BIO. Do not imply a vision model automatically supports protein embeddings.

A model can be multimodal in general but evaluated in TEXT mode when the actual request contains text only. Record what is actually sent.

Axis B: amount of auxiliary textual evidence.
- NATIVE: exact official benchmark inputs and prompting/resources where available. Run this first.
- NO_AUX: retain the biological object, question, required assay/objective context, choices, and any task-defining measurements; omit OPTIONAL additional descriptions.
- WITH_AUX: identical case plus a preregistered set of legitimate auxiliary text/metadata, only when the task permits this extension.

NO_AUX does not mean remove the instruction, sequence, assay objective, disease context, answer choices, or a task-defining measured anchor. Most useful prompts still contain words. A sequence is a text string, but it is the biological input, not “extra explanatory text.”

Only run a NO_AUX/WITH_AUX pair where removing/adding the optional fields leaves the scientific question intact AND the source's usage rules allow it. Otherwise mark not applicable or prohibited. Do not multiply every one of the 64 rows into an invented 2×2 experiment.

Preserve the same case IDs, data split, output target, scorer, shots and generation budget within each paired comparison. Label new variants separately from official reproduction. BIO and TEXT comparisons with different extra evidence are system-level comparisons, not controlled measurements of alignment.

## Evidence and leakage

Create an explicit field allowlist before rendering a prompt:
- required model-facing fields;
- permitted optional auxiliary fields;
- scorer-only fields;
- provenance/control fields that must not be sent.

Gold GO terms, mutation outcomes for the actual held-out target, reference explanations, and answer-revealing conclusions from related papers stay on the scorer side unless the benchmark explicitly defines them as provided context. PFArena T3's anchor measurement and T4's component single-mutant measurements are permitted inputs by task definition; do not delete them.

For open-book research QA, reference passages may intentionally contain the answer: that is a reading task, not automatically leakage. The item must be labeled open-book, and sources must be obtained by a fixed, answer-blind selection process allowed by the benchmark. Supplying a known mutation outcome to a supposedly outcome-predictive task is different.

Default: no retrieval or browsing by the solver. The execution agent may inspect official papers, download authorized public benchmark data and implement deterministic scoring. These are not extra inference-time tools for the solver.

PG-LLM is native-protocol-only in this initial handoff: preserve frozen prompts/candidates/labels and its restrictions on benchmark-specific training, prompt tuning, retrieval augmentation and model selection. Do not perform arbitrary auxiliary-text variants on it.

Do not send private wet-lab, Slack, WeChat, or unpublished collaboration data to external models. This package concerns public evaluations; it does not authorize any new wet-lab experiment or changes to LibB/LibD training.
