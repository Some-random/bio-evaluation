# Execution examples: what is valid, what is not, and what a result supports

**Date:** 13 October 2026  
**Audience:** Execution agent for Dongwei's biological-evaluation project  
**Status:** Proposed evaluation/interpretation guidance, not instructions attributed to Yejin, Fang, or benchmark authors.

## Read this before implementing or interpreting the evaluations

The existing A–F categories describe input compatibility and implementation requirements. They do **not** classify tasks as solvable through verbal reasoning, establish what a model has learned, or predict performance.

Keep biological prediction tasks. Do not remove a task merely because a specialist model might be better, or because its answer cannot be derived from an explicit rule in the prompt. A scientific predictor is allowed to predict held-out outcomes. What it is not allowed to do is treat a convincing explanation as independent validation of that prediction.

For each setting, separately record:

- **Input interface:** text/sequence, protein embeddings, images, structures, or another native input.
- **Likely task demands:** evidence operations, knowledge use, retrieval, learned biological prediction, geometric construction, or a combination. These are provisional task descriptions—not claims about internal model computation.
- **Reference evidence:** experimental measurement, curated annotation, calculated property, reference description, or external-model score.
- **Permitted conclusion:** what a good or bad score actually establishes.

This addendum does not authorize training, extra paid calls, new wet-lab work, relaxed data restrictions, or changes to the initial task list. Run native protocols first. Task-specific usage restrictions override these generic illustrative examples. PG-LLM remains native-only under the current handoff; do not use it for the illustrative auxiliary-context or reasoning-budget ablations below.

**Every numerical example, candidate name, measurement, and miniature scenario below is invented solely to illustrate evaluation design. None is an authentic benchmark row or a verified biological finding. Do not add these examples to scored benchmark sets or a biological training corpus.**

## Example 1 — Reasoning over explicitly supplied measurements

**Illustrative input:** “Under the same assay, A has score 1.2 and B has score 0.8. Higher is better. Which scored higher, and by how much?”

**OK:** Answer A, by 0.4 assay units. Score the arithmetic/comparison using the supplied values. Describe this as interpreting supplied evidence.

**NOT OK:** Report the result as predicting an unknown experimental outcome, demonstrating mutation-effect expertise, or proving that A binds more tightly. The prompt already supplied the measured scores and did not define them as binding affinity.

**Takeaway:** Correct reasoning with supplied measurements and prediction of unseen measurements are different achievements.

## Example 2 — A legitimate sequence-to-outcome prediction task

**Illustrative input:** A reference GFP sequence, candidate variants, and the original assay objective. Held-out fluorescence measurements are retained only by the scorer.

**OK:** Ask each configured model for the output required by the benchmark—numerical scores or a ranking—and score it against the held-out measurements. Record this as biological outcome prediction, potentially requiring learned sequence representations as well as knowledge/reasoning. Use the original split and evaluation unit.

**NOT OK:** Reject the task because the answer is not logically derivable from the prompt. Also do not claim that a poor text-model score proves poor general reasoning, or that a good score proves the generated rationale caused the prediction.

**Takeaway:** A task can be a valid and useful LLM baseline without being a clean test of verbal reasoning.

## Example 3 — Supplied single-mutant measurements do not establish combination outcomes

**Illustrative input:** Change A has measured score 1.1; change B has score 1.2; the reference has score 1.0. The A+B combination has no supplied measurement.

**OK:** Predict the combination under a benchmark that requests it, then compare with its held-out experimental score. Treat supplied component measurements as legitimate inputs when the task defines them that way.

**NOT OK:** Manufacture a “gold” combined score of 1.3 by adding the two improvements. The supplied values do not establish additivity. Do not call a model's additive calculation an experimental reference.

**Takeaway:** Combining evidence can involve a new empirical assumption. The missing outcome still needs an independent reference.

## Example 4 — A correct outcome is not a verified mechanism

**Illustrative reference:** “The variant had lower activity than the reference in assay Z.” No structural or mechanistic evidence is provided.

**Illustrative model answer:** “The larger residue creates a steric clash, which explains the lower activity.”

**OK:** Credit a correct activity-direction prediction where the task's scorer rewards it. Mark the clash explanation as unsupported by the available reference. A model may propose it as a hypothesis; that is different from a verified explanation.

**NOT OK:** Upgrade the clash claim to mechanistic ground truth because it sounds plausible or agrees with the direction of the measured effect. Also do not label it definitely false solely because the reference omits the mechanism.

**Takeaway:** Separate outcome correctness, reference-supported explanation, plausible hypothesis, and contradicted explanation.

## Example 5 — “No auxiliary text” must keep the task meaningful

**Illustrative native task:** Given a reference sequence and variants, rank them for a specified assay objective.

**OK NO_AUX:** Keep the complete required sequences, mutation identities, question, choices/candidate identifiers, and assay/objective context. Remove only truly optional explanatory material, and only where the source permits this variant.

**OK WITH_AUX:** Add a fixed, authorized field set whose content is available without looking up the held-out target outcome. Record the field provenance and exact text. Use the same cases and scorer in both variants.

**NOT OK:** Remove “rank for fluorescence” and ask the model which variant is “better.” Also do not append “A is the brightest variant” or a source conclusion stating the held-out answer and report the resulting gain as better predictive ability.

**Takeaway:** No additional explanation does not mean no question, no objective, or no essential information. Any altered input protocol is separately labeled.

## Example 6 — An answer-bearing passage can be valid in a reading task

**Illustrative input:** A permitted source passage says A outperformed B in assay Z; the question asks which performed better.

**OK:** Include that passage in an explicitly defined, authorized supplied-evidence reading task. Supplying the evidence is the point of that task. Choose sources using a frozen, answer-blind process or the benchmark's own supplied context—not by inspecting the held-out answer and selecting convenient excerpts.

**NOT OK:** Put the same passage into a supposedly unmeasured-outcome prediction task and call it helpful background. Do not silently turn a closed-book benchmark into an open-book one.

**Takeaway:** Whether context is legitimate depends on the task contract, not whether it contains useful information. Report reading and prediction results separately.

## Example 7 — Raw sequences, encoder features, and extra evidence

**Illustrative comparison:** System A receives an amino-acid string. System B receives features computed from that same string by a fixed pretrained protein encoder.

**OK:** Compare complete systems on the same cases, while disclosing the different representations and prior training. Features computed solely from the same sequence do not constitute a new experimental measurement; they provide access to the encoder's learned representations.

**NOT OK:** Claim that System B's advantage must come from better reasoning or alignment. Do not secretly add a measured structure, an MSA, functional annotations, or extra predictions only to B and describe it as an equal-information comparison.

**Further limit:** Comparing a supervised encoder-plus-head system with a zero-shot API model is allowed when clearly labeled, but it is not a matched-training-regime comparison. The current baseline-only assignment does not authorize training that head; use an available authorized baseline or mark it for a future experiment.

**Takeaway:** Report data exposure, input evidence, representation, training regime, and inference resources separately.

## Example 8 — A longer explanation is not demonstrated reasoning improvement

**Illustrative result:** One configuration produces a much longer rationale than another.

**OK:** Score both final outputs against the same references. Where explicitly permitted, compare preregistered inference settings on the same model and cases, with resource use documented. Describe any gain as a gain under those inference settings, not proof of a particular internal mechanism.

**NOT OK:** Count tokens as correctness; give extra scientific credit for length; ask the solver whether its own explanation is correct and treat that judgment as ground truth; or cherry-pick the most convincing-looking attempt.

**Takeaway:** Distinguish response style, inference effort, answer quality, and explanation support.

## Example 9 — Protein descriptions and label leakage

**Illustrative task:** Predict functional annotations from a protein sequence.

**OK:** Expose only the official allowed input fields. Keep gold function labels and teacher-generated reference rationales on the scorer side. An upstream predictor's annotations may be allowed under some protocols, but must be identified as predictor-derived inputs and included consistently across relevant comparisons.

**NOT OK:** Copy the full dataset row into the prompt because it is convenient. Such a row can include the exact function label, a prose equivalent, a label-revealing protein name, or teacher-only explanation. Do not count an explanation repeating the supplied answer as independent functional inference.

**Takeaway:** Build an explicit input allowlist. Do not declare every annotation forbidden either: the original task determines what is legitimate.

## Example 10 — Preserve required modalities and task-defining context

**Illustrative cases:** Image-based figure/table QA; expression-conditioned gene selection; known-complex CDR redesign.

**OK:** Use the required images, expression information, or structural inputs through a compatible system. When an exact input or evaluator is unavailable, mark the setting blocked or deferred. An authorized transcription or sequence-only subtask receives a new variant name.

**NOT OK:** Drop the image, keep a gene shortlist without the expression information, or omit the structural context, then report the result as faithful reproduction. Never manufacture replacement features from the gold answer.

**Takeaway:** A question being writable in English does not make every required input dispensable. In the existing catalog, LAB-Bench TableQA uses table images; preserve that source-defined format.

## Example 11 — Do not turn proxy performance into experimental success

**Illustrative result:** A fixed biological predictor assigns a generated sequence a high score, or a structural predictor produces a confident structure.

**OK:** Report the score as predictor-based performance with the evaluator version and call budget. Keep biological measurements as a separate evidence category. The evaluator need not be available to the solver; revealing feedback defines a different iterative setting.

**NOT OK:** Report “experimentally validated binder,” a physical dissociation constant, or wet-lab success from a model score alone. Diversity or a fluent self-description does not supply missing functional evidence.

**Takeaway:** The score's evidence source controls the claim.

## Example 12 — Fair accounting and restricted evaluations

**Illustrative result:** Out of 100 planned eligible cases, 80 responses are correct, 10 wrong, and 10 are unparsable.

**OK:** Under a declared all-case rule that scores invalid responses as failures, report 80/100 = 80%, plus a 10% invalid-output rate. If the official scorer has different rules, apply those and separately disclose coverage and missing/invalid cases. Distinguish transport failures from model-produced invalid answers.

**NOT OK:** Quietly drop the 10 unparsable responses and report 80/90 as though it were the all-case score. Do not use the reference to fill a missing ranking, retry only wrong answers, or choose a favorable response with the answer key.

**Restriction:** Protected benchmarks remain protected. Current instructions keep PG-LLM native-only; these examples do not grant permission for prompt optimization, auxiliary-context runs, model selection, or training on its evaluation material.

**Takeaway:** Preserve original scorer rules, failures, resource limits, and benchmark-use restrictions.

## Metadata to add without replacing the original catalog

Add a separate `interpretation_notes.jsonl` keyed by the existing task ID and protocol variant. Do not silently rewrite the A–F compatibility classes.

Each entry should record:

| Field | Meaning |
|---|---|
| `task_id`, `protocol_variant` | Stable link to the original catalog and exact run |
| `input_interface` | What was actually supplied to this solver |
| `task_demands` | Provisional multi-label description, with a brief rationale |
| `reference_evidence_type` | Measurement, annotation, calculation, reference text, or model proxy |
| `required_inputs` | Fields necessary to define the native task |
| `permitted_auxiliary_fields` | Optional context allowed in this exact protocol |
| `scorer_only_fields` | Hidden labels and teacher/reference information |
| `mechanism_reference_available` | Yes, no, partial, or unresolved |
| `allowed_result_claim` | Narrow conclusion justified by the metric and evidence |
| `unsupported_result_claim` | Specific overinterpretation to avoid |
| `classification_basis` | Source file/section or explicitly marked analyst inference |

Do not guess a mechanism label or a demand category just from a task name. Multiple demands can coexist. Input ablations are diagnostics, not conclusive descriptions of internal model computation.

## Execution instruction

Continue the authorized native evaluations. This addendum changes interpretation and validation checks, not the target metrics or run permissions. First-wave scope, original task IDs, exact model identifiers, budget approval, test protection, privacy limits, and blocker handling remain as in the existing handoff.

Use artificial values only for parser/scorer unit tests. Do not use these examples or protected test feedback to tune benchmark prompts. Return official per-task scores and a separate interpretation table explaining what each result does and does not establish. Hypotheses about why a model failed remain hypotheses until tested.

## Provenance

This is a newly authored addendum based on the user's requested distinction between biological prediction, representation learning, and reasoning. The native-input, context, leakage, metric, and execution constraints are preserved from the existing `PROJECT_CONTEXT.md`, `TASK_RULES.md`, and `COPY_PASTE_PROMPTS.md`. No primary paper or benchmark website was freshly re-audited for this drafting step. Existing source caveats remain. No dataset payload, model score, scientific measurement, or verified mechanistic explanation was created.
