"""Add interpretation metadata without changing benchmark inputs or metrics.

Demand labels are explicit analyst inferences from catalogued inputs, outputs
and reference evidence. A--F compatibility is copied, never used to infer
reasoning suitability. This command makes no provider calls.
"""
import csv
import hashlib
import json
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HANDOFF = ROOT / "handoff/bio_eval_agent_handoff_2026-10-13"
ADDENDUM = ROOT.parent / "EXECUTION_EXAMPLES.md"

# Each profile was authored from the source task contract, not the task name
# or A--F interface code. These are provisional task descriptions.
PROFILES = {
    "DISCRETE_PROTEIN": (
        ["learned_biological_prediction", "biological_knowledge_use", "label_mapping"],
        "A sequence or sequence pair must be mapped to a held-out property/interaction label. The target is not supplied by an arithmetic rule; learned sequence representations may be essential.",
        "Agreement with this dataset's class labels under its fixed split and negative-label construction.",
        "Limited class-label recovery in this input/training regime; label ambiguity, negative construction, distribution shift and representation limitations remain possible.",
        "General verbal-reasoning ability, a physical binding constant, a verified causal mechanism, or success in every laboratory condition.",
        ["curated_annotation"], "label_prediction"),
    "CONTINUOUS_PROTEIN": (
        ["learned_biological_prediction", "assay_context_use", "sequence_representation"],
        "Full variant sequences and an assay definition must predict withheld numerical measurements. Genotype-to-phenotype mapping may require learned protein representations.",
        "Association of predictions with held-out outcomes within the specified assay and official aggregation unit.",
        "Weak assay-specific predictive association; this does not isolate whether the limitation is knowledge, representation, calibration or inference.",
        "Correct mechanistic reasoning, calibrated physical units from correlation alone, or universal biological/general-reasoning failure.",
        ["experimental_measurement"], "outcome_prediction"),
    "MULTILABEL_FUNCTION": (
        ["learned_biological_prediction", "biological_knowledge_use", "ontology_mapping"],
        "Protein information must be mapped to EC/GO vocabulary and the source's ontology/score rules. Annotation recovery can depend on learned sequence representations and permitted context.",
        "Recovery/ranking of recorded annotations with the exact vocabulary, propagation and native metric.",
        "Poor recovery under this annotation/split/scoring contract; missing annotations need not be genuine negatives.",
        "Verified absence of unannotated functions, a validated explanation, interchangeable Fmax/AP/F1 scores, or a frozen operating threshold from Fmax alone.",
        ["curated_annotation"], "annotation_prediction"),
    "PROTEINGYM": (
        ["learned_biological_prediction", "assay_context_use", "sequence_representation"],
        "Reference and variant inputs must predict held-out DMS measurements; allowed extra structures/MSAs define an additional information regime.",
        "Per-assay predictive ordering/association against measured DMS outcomes under the official suite aggregation.",
        "Weak outcome association for these assays and provided information, not a general reasoning diagnosis.",
        "A shared physical scale across assays, experimental binding for every endpoint, or a verified rationale.",
        ["experimental_measurement"], "outcome_prediction"),
    "PG_LLM_NATIVE": (
        ["learned_biological_prediction", "assay_context_use", "candidate_comparison", "ranking_output"],
        "The prompt gives complete sequences and assay context, but no candidate fitness measurements. Ranking unknown outcomes may require learned biological regularities; it is not just comparing supplied numbers.",
        "Agreement with measured fitness ordering within each assay, with the native assay/protein/category aggregation and disclosed coverage.",
        "Poor ranking of these candidate sets under the frozen sequence/text protocol; it does not identify the model's internal computation or general reasoning ability.",
        "Rationale causality/correctness, verified mutation mechanisms, contamination-free exposure, or permission for tuning, model selection or auxiliary-context ablations.",
        ["experimental_measurement"], "outcome_ranking"),
    "PFA_SINGLE": (
        ["conditioned_biological_proposal", "learned_biological_prediction", "biological_knowledge_use"],
        "Propose mutations for a supplied protein/objective without target-specific measured outcomes, within the official proposal budget.",
        "Recovery of measured favorable mutations and best recorded score within the benchmark's measured reference universe and proposal budget.",
        "Low recovery within the measured universe; an unmeasured proposal is not an experimentally confirmed failure.",
        "Prospective wet-lab hit rate for all proposed mutations or correct mechanisms inferred from recovered outcomes.",
        ["experimental_measurement"], "measured_mutation_recovery"),
    "PFA_RANK_NO_MEAS": (
        ["learned_biological_prediction", "assay_context_use", "candidate_comparison"],
        "Candidate multi-mutants are ranked without target-specific measurements; sequence and objective information must support prediction of held-out combination outcomes.",
        "Ranking/recovery of withheld measured multi-mutant outcomes under the exact native gains, cutoffs and direction.",
        "Weak combination-outcome ordering under these inputs; possible representation and epistasis limitations remain hypotheses.",
        "Validated mechanisms or equivalence to measurement-informed PFArena settings.",
        ["experimental_measurement"], "outcome_ranking"),
    "PFA_RANK_ANCHOR": (
        ["supplied_measurement_interpretation", "learned_biological_prediction", "candidate_comparison"],
        "A measured anchor is required evidence, but strictly extending candidates have withheld outcomes. Interpreting the anchor and extrapolating to new combinations can coexist.",
        "Prediction of candidate-extension outcomes conditional on the explicitly supplied anchor measurement.",
        "Weak extension prediction with this evidence; does not establish failure to compare or understand the supplied anchor alone.",
        "Equal-information superiority over measurement-free tasks or a verified mechanism from the anchor value alone.",
        ["experimental_measurement"], "conditional_outcome_ranking"),
    "PFA_RANK_COMPONENTS": (
        ["supplied_measurement_interpretation", "learned_biological_prediction", "combination_effect_prediction"],
        "Single-mutant measurements are legitimate required inputs. Multi-mutant outcomes remain unknown; interpreting components does not establish additivity or remove the need for empirical prediction.",
        "Prediction of withheld multi-mutant outcomes given the authorized component measurements.",
        "Weak combination prediction, not necessarily inability to perform arithmetic on supplied component scores.",
        "A gold combination score manufactured by addition, or an experimentally established additive/epistatic mechanism.",
        ["experimental_measurement"], "conditional_outcome_ranking"),
    "PROTEIN_DESCRIPTION": (
        ["biological_annotation_prediction", "biological_knowledge_use", "sequence_representation", "language_generation"],
        "A sequence and instruction must yield function/activity/domain descriptions without exposing the reference annotation. Learned protein representations may be important alongside knowledge and text generation.",
        "Native lexical agreement with reference descriptions/annotations; independent claim support requires a separate evidence review.",
        "Low lexical agreement can reflect wording, incompleteness or prediction errors; it does not by itself prove every biological statement false.",
        "Verified function, a mechanistic discovery, or factual correctness of all generated claims from ROUGE alone.",
        ["reference_description", "curated_annotation"], "reference_text_similarity"),
    "MUTATION_EXPLANATION": (
        ["mutation_effect_inference", "biological_knowledge_use", "sequence_representation", "explanation_generation"],
        "Reference/variant inputs must support an effect description. Predicting the effect and supporting a proposed mechanism are distinct demands; source context is model/protocol-specific.",
        "BLEU/ROUGE agreement with effect descriptions; a separately configured rubric can establish only the reference support it actually checks.",
        "Low description agreement does not alone establish a wrong effect direction or a false mechanism; these require separate reference-grounded assessment.",
        "Mechanistic truth or independent experimental verification from lexical overlap, fluency, a correct effect prediction or model judging alone.",
        ["curated_annotation", "publication_enriched_reference_description"], "effect_description_similarity"),
    "MUTATION_KNOWN_POSITION": (
        ["conditioned_mutation_proposal", "learned_biological_prediction", "biological_knowledge_use"],
        "The protein, desired effect and designated position constrain an inverse biological prediction: choose a replacement amino acid. The desired effect and position are legitimate task inputs.",
        "Accuracy of recovery of the annotated replacement residue at the supplied position.",
        "Low annotated-residue recovery; another useful replacement can be missed by this single-reference metric.",
        "Experimental success rate of novel proposals or a verified explanation of why the recovered residue works.",
        ["annotated_reference_mutation"], "reference_mutation_recovery"),
    "MUTATION_UNKNOWN_POSITION": (
        ["conditioned_mutation_proposal", "learned_biological_prediction", "position_search", "budgeted_candidate_selection"],
        "The protein and desired effect define an inverse prediction without the target site. Search over positions/replacements under the proposal budget may rely on learned sequence representations.",
        "Recall of the annotated single substitution within the native up-to-50 proposal budget.",
        "Failure to recover the annotation; alternatives without recorded outcomes are not confirmed biological failures.",
        "Experimental hit rate, validated binding/function of all proposals or a verified mechanism.",
        ["annotated_reference_mutation"], "reference_mutation_recovery"),
    "LOW_N_HEAD": (
        ["supervised_biological_prediction", "sequence_representation", "limited_label_learning"],
        "A separately fitted head maps variant representations and allowed low-N fitting measurements to held-out outcomes. Training regime is part of this valid task contract.",
        "Held-out predictive association for the specified low-N training/seed protocol.",
        "Weak generalization under that label/representation regime, not a zero-shot verbal-reasoning diagnosis.",
        "Equivalence to few-shot chat prompting or authorization to train a new head in the current baseline-only assignment.",
        ["experimental_measurement"], "supervised_outcome_prediction"),
    "ITERATIVE_OPTIMIZATION": (
        ["conditioned_sequence_search", "biological_knowledge_use", "oracle_feedback_use"],
        "A starting sequence, objective and defined search/oracle budget produce a trajectory scored by a learned landscape model.",
        "Improvement under the fixed model proxy and exact iteration/query budget.",
        "Limited optimization of this proxy within budget; predictor mismatch and search behavior remain confounded.",
        "New experimental fitness, verified mechanisms or fairness to one-shot systems with different feedback resources.",
        ["external_model_score"], "proxy_optimization"),
    "RETRIEVAL": (
        ["semantic_retrieval", "biological_knowledge_use", "sequence_text_matching"],
        "A text query must select proteins from a fixed corpus with documented relevance/case references. Full-corpus retrieval and ranking a handpicked shortlist differ.",
        "Retrieval/case agreement with recorded annotations and any separately labeled docking proxy analyses.",
        "Weak retrieval/case matching for the fixed corpus; does not establish failed experimental binding.",
        "A fabricated global recall measure from selected cases or experimental success from docking scores.",
        ["curated_annotation", "calculated_docking_proxy"], "retrieval_or_case_analysis"),
    "QUALITATIVE_DESIGN": (
        ["conditioned_sequence_generation", "biological_knowledge_use", "sequence_representation"],
        "Requested properties or molecular conditions guide sequence generation; catalogued validation is case/reference/proxy analysis, not a fully established labeled outcome suite.",
        "Only the specific documented case/reference or predictor-screening observations.",
        "A disappointing case/proxy screen does not quantify a general experimental success rate.",
        "Verified function/binding from self-description, sequence similarity or predicted complexes.",
        ["reference_case", "external_model_score"], "qualitative_or_proxy_analysis"),
    "UNCONDITIONAL_GENERATION": (
        ["protein_sequence_generation", "learned_sequence_distribution_modeling"],
        "Unconditioned samples are assessed for sequence statistics/diversity and fixed structural-predictor confidence; functional guidance would change the task.",
        "The stated sample statistics and fixed predictor-confidence metrics under the sampling protocol.",
        "Poor sampling diversity or predictor confidence in this setting, not proved absence of biological function.",
        "Measured function or binding from diversity, novelty or structure confidence.",
        ["calculated_sequence_statistics", "external_model_score"], "generation_diagnostics"),
    "CONDITIONAL_GENERATION": (
        ["conditioned_sequence_generation", "biological_property_modeling", "sequence_representation"],
        "A requested property guides sequence generation; the reference is a fixed learned property scorer rather than measurements for every generated sequence.",
        "Property-scorer agreement plus the stated diversity diagnostics.",
        "Weak conditioning under this predictor; failure is not experimentally established for every sample.",
        "Experimentally measured solubility/stability or a validated property mechanism.",
        ["external_model_score", "calculated_sequence_statistics"], "proxy_conditioned_generation"),
    "RABD_STRUCTURE": (
        ["geometric_construction", "conditioned_sequence_prediction", "sequence_structure_representation"],
        "Masked H3 recovery is conditioned on native target/framework/complex context. Geometric reconstruction and residue recovery are distinct assessed outputs.",
        "Recovery/geometric similarity to reference H3/complex regions under the original alignments and pose assumptions.",
        "Weak reconstruction under those inputs; a different structure/sequence need not be a failed binder.",
        "Measured binding for a new design, unconstrained docking success or equivalence of a sequence-only subtask to full geometry evaluation.",
        ["reference_structure", "reference_sequence"], "sequence_structure_reconstruction"),
    "SABDAB_STRUCTURE": (
        ["geometric_construction", "conditioned_sequence_prediction", "interface_representation"],
        "Masked CDR sequence/geometry is reconstructed given antigen/framework/docking assumptions; structural and energy diagnostics have different evidence sources.",
        "Native sequence/structure/interface recovery and separately labeled computational energy diagnostics.",
        "Weak reconstruction/proxy geometry in this holdout; it does not establish experimental nonbinding.",
        "Unconstrained binder discovery, physical binding constants or wet-lab success from reconstruction/energy metrics.",
        ["reference_structure", "reference_sequence", "calculated_energy_proxy"], "sequence_structure_reconstruction"),
    "GFP_GENERATED": (
        ["conditioned_sequence_editing", "biological_property_modeling", "edit_constraint_following"],
        "Reference GFP and the edit objective define proposals assessed by a fixed fluorescence predictor, with uniqueness/novelty/edit validity audited separately.",
        "Improvement/success under the fixed SaProt proxy and the defined edit/proposal budget.",
        "Weak proxy improvement or invalid edits; neither proves the actual fluorescence of unmeasured candidates.",
        "Measured fluorescence or successful mechanisms from predictor scores or correctly formatted edits.",
        ["external_model_score", "calculated_sequence_statistics"], "proxy_editing"),
    "DRUG_TARGET": (
        ["learned_biological_prediction", "molecular_representation", "protein_representation"],
        "Molecule/protein information predicts withheld dataset-specific interaction or affinity-derived labels. Negative construction and chemical/protein representations matter.",
        "Continuous-score discrimination of that dataset's labels under its exact split.",
        "Weak label discrimination under that dataset regime; not isolated reasoning failure.",
        "Measured physical affinity for all candidates, protein-protein specificity or a verified interaction mechanism.",
        ["dataset_specific_annotation_or_affinity_derived_label"], "interaction_prediction"),
    "EXPLANATION_ASSESSMENT": (
        ["evidence_support_assessment", "biological_knowledge_use", "explanation_generation"],
        "Claims in an explanation are assessed against a fixed evidence subset and an independent rubric when available; correct GO labels alone cannot validate those claims.",
        "Support or contradiction established by the specific available references and implemented review rubric.",
        "Weak reference support under that rubric; missing support and positive contradiction must be distinguished.",
        "Full mechanistic truth, causal faithfulness or actual expert review from anecdotes or a solver's self-judgment.",
        ["curated_annotation", "reference_description", "judge_or_expert_assessment"], "explanation_support"),
    "LAB_TEXT": (
        ["knowledge_use", "evidence_operations", "scenario_or_sequence_analysis"],
        "Questions/choices, required scenarios or sequences must support an answer. Whether supplied-evidence reading or retrieval is involved depends on the actual resource contract, not the category name.",
        "Reference-answer agreement under the fixed allowed resources, with answered-item precision and coverage when abstention applies.",
        "Limited reference-answer performance under those inputs; errors need not isolate knowledge, retrieval, evidence reading or reasoning.",
        "Experimentally demonstrated protein-design ability, equal-resource comparisons across tool-free/open-book runs, or a verified rationale from MCQ accuracy.",
        ["curated_reference_answer"], "question_answering"),
    "IMAGE_QA": (
        ["visual_information_extraction", "evidence_operations", "domain_knowledge_use"],
        "Required images/documents and questions must be interpreted. Image content, text context and any teacher-only evidence must be accounted for separately.",
        "Agreement with this dataset's image/question references under its native scorer and permitted inputs.",
        "Weak reference agreement; visual ambiguity, reference construction and information mismatch can contribute.",
        "Protein-sequence reasoning, clinical/biological validation or equivalent reproduction after dropping required images.",
        ["curated_reference_answer"], "visual_question_answering"),
    "GENOMIC": (
        ["learned_biological_prediction", "genomic_representation", "pathway_or_variant_context_use"],
        "Reference/variant genomic representations and required context predict curated disease/variant labels. Knowledge, learned representations and context integration may all matter.",
        "Recovery/discrimination of the source's annotation labels under the exact disease/variant split.",
        "Weak annotation prediction in that regime; not a general reasoning diagnosis or confirmed pathogenicity of every error.",
        "Verified generated mechanistic chains, protein-binding specificity or clinical validation from annotation accuracy alone.",
        ["curated_annotation"], "genomic_annotation_prediction"),
    "EXPRESSION": (
        ["expression_information_use", "biological_knowledge_use", "conditioned_target_selection"],
        "Gene choices and disease/cell context must be interpreted together with the required expression representation. Candidate names without expression data do not preserve this task.",
        "Agreement with adapted MEDEA gene-selection answers under the verified expression input/split contract.",
        "Weak nomination agreement under that contract, not confirmed therapeutic failure or a full agent-workflow diagnosis.",
        "Clinical efficacy, validated mechanisms or faithful reproduction after removing expression measurements.",
        ["adapted_reference_answer"], "target_nomination"),
}

CONTROL_DEMANDS = {
    "G01": (["continuation_modeling"], "Predict reference continuations with the likelihood/byte-normalized source metric."),
    "G02": (["knowledge_use", "answer_selection"], "Map fixed subject questions and choices to reference answers."),
    "G03": (["factual_knowledge_use", "permitted_evidence_use"], "Answer factual questions with resource access fixed by the source protocol."),
    "G04": (["mathematical_problem_solving", "answer_extraction"], "Solve specified problems and normalize final answers; the answer metric does not verify each step."),
    "G05": (["program_construction", "specification_use"], "Construct code assessed against executable functional tests."),
    "G06": (["code_completion", "context_use"], "Complete the omitted code span under the native loss or task scorer."),
    "G07": (["constraint_or_puzzle_solving", "answer_extraction"], "Produce answers to specified puzzles/constraints; this task description does not reveal internal computation."),
    "G08": (["instruction_constraint_following"], "Meet the explicitly testable constraints in the supplied instructions."),
    "G09": (["response_generation", "preference_alignment"], "Generate responses assessed by a fixed pairwise judge/reference-system protocol."),
    "G10": (["function_schema_use", "tool_call_construction"], "Construct specified function calls and any suite-required execution outcomes."),
    "G11": (["supplied_context_retrieval", "context_use"], "Recover/operate on evidence in the supplied synthetic long context."),
    "G12": (["supplied_context_use", "task_dependent_operations"], "Perform the particular held-out context tasks with lengths and overlap caveats fixed."),
    "G13": (["literature_evidence_use", "permitted_retrieval", "answer_selection"], "Answer literature questions with the stated agent and resource contract; resources differ from tool-free LAB-Bench."),
    "G14": (["suite_dependent_language_tasks"], "Preserve the official collection's constituent tasks and normalization; one aggregate cannot characterize every demand."),
}

INPUT_OVERRIDES = {
    "P18": ["wild-type sequence", "frozen full candidate sequences/order/IDs", "canonical assay fitness description", "native protein/organism metadata"],
    "P21": ["reference/objective", "tested anchor mutant and its measured value", "strictly extending candidate combinations"],
    "P22": ["reference/objective", "permitted component single-mutant measurements", "candidate multi-mutants"],
    "P31": ["protein", "desired effect", "correct mutation position", "model-specific protein context only as permitted by the native source"],
    "P32": ["protein", "desired effect", "model-specific protein context only as permitted by the native source"],
    "B05": ["original table IMAGE", "question/choices and source-defined context"],
    "N05": ["candidate genes", "required expression representation/measurements", "disease and cell context"],
}
REFERENCE_OVERRIDES = {
    "P01": ["experimental_or_curated_property_label"],
    "P09": ["binarized_stability_label_exact_derivation_unresolved"],
    "P10": ["curated_interaction_positive", "dataset_constructed_negative"],
    "P11": ["curated_interaction_positive", "dataset_constructed_negative"],
    "P36": ["selected_reference_or_case_comparison"],
    "P39": ["generated_self_description", "external_structure_model_proxy"],
    "V05": ["synthetic_figure_derived_answer", "manually_checked_subset"],
    "V06": ["teacher_generated_reference_answer", "model_judge_assessment"],
}

SCORER_FIELDS = {
    "DISCRETE_PROTEIN": ["held-out per-case class/interaction labels; fixed label vocabulary remains permitted input"],
    "CONTINUOUS_PROTEIN": ["tested variants' held-out measured outcomes"],
    "MULTILABEL_FUNCTION": ["held-out target EC/GO annotations and target-aspect descriptions", "reference/teacher rationales not explicitly provided by the native protocol"],
    "PROTEINGYM": ["tested variants' experimental DMS scores"],
    "PFA_SINGLE": ["measured mutation outcomes and reference positive universe used by the scorer"],
    "PFA_RANK_NO_MEAS": ["held-out candidate multi-mutant measurements and scorer-derived reference ordering"],
    "PFA_RANK_ANCHOR": ["held-out candidate-extension measurements and reference ordering; supplied anchor value remains required input"],
    "PFA_RANK_COMPONENTS": ["held-out multi-mutant combination measurements and reference ordering; supplied single-mutant values remain required inputs"],
    "PROTEIN_DESCRIPTION": ["reference descriptions/annotations and answer-revealing teacher explanations"],
    "MUTATION_KNOWN_POSITION": ["annotated replacement amino acid; designated position remains required input", "source mutation entry/variant sequence revealing the replacement"],
    "MUTATION_UNKNOWN_POSITION": ["annotated target position and replacement amino acid", "source mutation entry/variant sequence revealing the target"],
    "LOW_N_HEAD": ["held-out test measurements; source-defined fitting/development measurements have their own permitted role"],
    "RABD_STRUCTURE": ["native masked H3 sequence/coordinates; permitted target/framework context remains input"],
    "SABDAB_STRUCTURE": ["native masked CDR sequence/coordinates/features; permitted antigen/framework/pose context remains input"],
    "DRUG_TARGET": ["held-out interaction/affinity targets and scorer reference labels"],
    "EXPLANATION_ASSESSMENT": ["independent rubric and reference evidence for the grader; teacher-only information must not enter answer generation"],
    "LAB_TEXT": ["reference answer/abstention key; source-defined supplied passages/scenarios/sequences remain legitimate input"],
    "IMAGE_QA": ["reference answers and teacher-only evidence; required original images/questions remain input"],
    "GENOMIC": ["target disease/variant labels and teacher-only rationales; required pathway context remains input"],
    "EXPRESSION": ["reference target-gene answer; required expression information remains input"],
}

def prepared_audit():
    path = ROOT / "data/model_inputs.preparation.jsonl"
    counts = Counter()
    field_sets = {}
    with path.open() as handle:
        for line in handle:
            row = json.loads(line)
            key = (row["task"], row["variant"])
            counts[key] += 1
            fields = set(row["fields"])
            if key in field_sets and fields != field_sets[key]:
                raise ValueError("Inconsistent prepared fields within a protocol variant")
            field_sets[key] = fields
    return counts, field_sets, hashlib.sha256(path.read_bytes()).hexdigest()

def native_interface(task, rule):
    if rule == "IMAGE_QA":
        return "VISION/native document input required; exact solver not selected"
    if rule in {"RABD_STRUCTURE", "SABDAB_STRUCTURE"}:
        return "native structural context required; exact structural/sequence-output solver not selected"
    if rule == "EXPRESSION":
        return "native expression representation plus task context; mapping unresolved"
    if task["id"] == "P18":
        return "TEXT/full sequences and native assay context (prepared, not submitted)"
    return "source-native interface not yet instantiated: " + task["model_input"]

def make_native(catalog, record, prepared, fields, addendum_hash):
    task_id = catalog["id"]
    rule = record["handoff_proposal"]["rule_id"] if record else None
    if rule:
        labels, rationale, high, low, unsupported, types, metric_scope = PROFILES[rule]
        compat = record["original_compatibility_annotation"]["Code"]
        source_status = "catalog/source-contract interpretation; release-specific verification pending"
    else:
        labels, rationale = CONTROL_DEMANDS[task_id]
        high = "Performance on this source-defined control and its native reference/scorer."
        low = "Limited performance on this particular control under the recorded inputs/resources."
        unsupported = "Protein-grounded biological capability, universal reasoning, verified intermediate steps or benefits for every training mixture/backbone."
        types, metric_scope, compat = ["source_defined_language_task_reference"], "general_control", None
        source_status = "general-control catalog reference; outside current execution scope"
    key = (task_id, "NATIVE")
    note = {
        "task_id": task_id, "task_name": catalog["task"], "protocol_variant": "NATIVE",
        "catalog_group": "biological" if record else "general_control",
        "original_compatibility_code": compat,
        "input_interface": native_interface(catalog, rule),
        "task_demands": {"labels": labels, "rationale": rationale, "status": "provisional_analyst_inference",
                         "internal_model_computation_established": False},
        "reference_evidence_type": REFERENCE_OVERRIDES.get(task_id, types),
        "reference_answer_source": catalog["reference_evidence"],
        "required_inputs": INPUT_OVERRIDES.get(task_id, [catalog["model_input"]]),
        "permitted_auxiliary_fields": [],
        "auxiliary_policy": "No new auxiliary variants authorized; native required context remains. Per-task source review controls optional fields.",
        "scorer_only_fields": SCORER_FIELDS.get(rule, ["withheld reference for scoring: " + catalog["reference_evidence"], "reference/teacher information not explicitly defined as native task input"]),
        "mechanism_reference_available": "no" if task_id == "P18" else "unresolved",
        "mechanism_reference_note": "No independently verified mechanism reference has been collected for this run; native outcome metrics do not verify rationales.",
        "allowed_result_claim": high, "good_score_establishes": high, "bad_score_establishes": low,
        "unsupported_result_claim": unsupported,
        "native_metric": catalog["metrics"], "metric_scope": metric_scope,
        "source_caveat": catalog["limitation"],
        "prepared_model_facing_fields": sorted(fields.get(key, [])),
        "prepared_case_count": prepared.get(key, 0),
        "actual_supplied_information": {"status": "not_run", "benchmark_requests_submitted": 0,
                                        "observed_model_input_fields": [], "note": "Prepared fields are not evidence of an executed solver request."},
        "outcome_score": None, "explanation_support_score": None, "score_status": "not_run",
        "explanation_support": {"status": "not_assessed", "allowed_review_labels": ["reference_supported", "unsupported_by_available_reference", "hypothesis", "reference_contradicted", "unresolved"],
                                "correct_outcome_validates_rationale": False, "missing_mechanism_evidence_means_false": False,
                                "native_metric_replaced": False},
        "classification_basis": {"kind": "analyst_inference_from_source_inputs_outputs_and_reference",
                                 "catalog_file": "handoff/bio_eval_agent_handoff_2026-10-13/references/evaluation_catalog.json",
                                 "catalog_fields": ["model_input", "model_output", "reference_evidence", "metrics", "limitation"],
                                 "source_locator": catalog["source_locator"], "source_url": catalog["access_url"],
                                 "primary_source_leads": catalog["primary_source"], "verification_status": source_status,
                                 "addendum": str(ADDENDUM), "addendum_sha256": addendum_hash,
                                 "demands_inferred_from_compatibility_code": False},
        "execution_scope_status": "prioritized_source_protocol" if task_id in {t for t, _ in prepared} else "catalog_reference_only_outside_prioritized_scope",
        "illustrative_examples_used_as_benchmark_data": False,
    }
    if rule in {"PFA_RANK_ANCHOR", "PFA_RANK_COMPONENTS", "MUTATION_KNOWN_POSITION", "MUTATION_UNKNOWN_POSITION"}:
        note["input_role_note"] = "Task-defining supplied measurements/desired effects are required inputs, not automatically forbidden labels."
    if rule in {"ITERATIVE_OPTIMIZATION", "RETRIEVAL", "QUALITATIVE_DESIGN", "UNCONDITIONAL_GENERATION", "CONDITIONAL_GENERATION", "GFP_GENERATED"}:
        note["input_role_note"] = "Feedback, corpus annotations and scorer information may have protocol-specific roles. Exact native availability must be verified; this entry grants no new solver resources."
    if task_id == "P18":
        note["auxiliary_policy"] = "NATIVE ONLY; no context/reasoning-budget ablation, retrieval augmentation, prompt tuning, model selection or training on evaluation splits."
        note["classification_basis"]["verification_status"] = "Frozen v1.2 inputs, hashes and pinned prompt/metadata code checked locally; no inference scores."
        note["classification_basis"]["local_sources"] = ["sources/pg_DATA.md", "sources/pg__src__prompt.py", "sources/pg__src__assays.py", "sources/pg__BENCHMARK_USE_POLICY.md"]
        note["scorer_only_fields"] = ["candidate experimental fitness scores in separate .labels.json files"]
    if task_id == "P30":
        note["mechanism_reference_note"] = "Effect annotations/publication-enriched reference descriptions may contain mechanisms, but per-claim independent support is unaudited. Missing support is not contradiction."
        note["scorer_only_fields"] = ["held-out mutation effect description", "teacher/reference explanations", "native judged categories when actually configured"]
    return note

def make_adapter(native, variant, count, field_names):
    note = json.loads(json.dumps(native))
    task_id = note["task_id"]
    note["protocol_variant"] = variant
    note["input_interface"] = "TEXT/full amino-acid strings and task-specific textual inputs (prepared, not submitted)"
    note["required_inputs"] = sorted(field_names)
    note["prepared_model_facing_fields"] = sorted(field_names)
    note["prepared_case_count"] = count
    note["execution_scope_status"] = "prepared_prioritized_text_variant"
    note["permitted_auxiliary_fields"] = []
    note["auxiliary_policy"] = "No extra context ablations authorized. This records the existing prepared variant only."
    note["classification_basis"]["local_sources"] = ["scripts/preflight.py", "configs/field_allowlists.json"]
    note["classification_basis"]["verification_status"] = "Prepared renderer and field roles checked; inference/scoring and exact reproduction remain pending."
    if task_id in {"P23", "P24", "P25", "P26"}:
        note["scorer_only_fields"] = ["source output reference descriptions/annotations", "teacher or positive/negative example answers"]
        note["classification_basis"]["local_sources"] += ["sources/biot5__biot5_plus__metrics__pro_understand_metrics__pro_understand_metrics.py"]
        note["protocol_difference"] = "Source instructions preserved; BioT5 protein markers decoded losslessly to full sequences. This is a TEXT adapter, not its trained-model or truncated-input reproduction."
    elif task_id == "P30":
        note["protocol_difference"] = "Draft single-call TEXT explanation input, without source effect references or extra protein-function text. MutaPLM's native two-stage system is different; official text-baseline review pending."
    else:
        note["protocol_difference"] = "Draft TEXT engineering adapter; desired effect and source-permitted function context are intentional inputs. Official text-baseline review pending."
        note["scorer_only_fields"] = ["annotated replacement amino acid", "mutation-bearing source entry/ID", "variant sequence revealing the target mutation"]
        if task_id == "P32":
            note["scorer_only_fields"].append("annotated target position")
        note["classification_basis"]["local_sources"] += ["sources/muta__dataset__finetune_dataset.py", "sources/muta__model__mutaplm.py", "sources/muta__evaluator.py"]
    return note

def write_reports():
    catalog = json.loads((HANDOFF / "references/evaluation_catalog.json").read_text())["tasks"]
    registry = json.loads((HANDOFF / "task_registry.json").read_text())["tasks"]
    by_id = {t["id"]: t for t in registry}
    prepared, fields, input_hash = prepared_audit()
    addendum_hash = hashlib.sha256(ADDENDUM.read_bytes()).hexdigest()
    records = [make_native(c, by_id.get(c["id"]), prepared, fields, addendum_hash) for c in catalog]
    native_by_id = {r["task_id"]: r for r in records}
    for (task_id, variant), count in sorted(prepared.items()):
        if variant != "NATIVE":
            records.append(make_adapter(native_by_id[task_id], variant, count, fields[(task_id, variant)]))
    keys = [(r["task_id"], r["protocol_variant"]) for r in records]
    assert len(keys) == len(set(keys))
    assert {r["task_id"] for r in records if r["catalog_group"] == "biological"} == set(by_id)
    assert set(prepared) <= set(keys)
    for r in records:
        assert r["task_demands"]["status"] == "provisional_analyst_inference"
        assert not r["task_demands"]["internal_model_computation_established"]
        assert not r["classification_basis"]["demands_inferred_from_compatibility_code"]
        assert r["mechanism_reference_available"] in {"yes", "no", "partial", "unresolved"}
        assert r["outcome_score"] is None and r["explanation_support_score"] is None
        if r["task_id"] in by_id:
            assert r["native_metric"] == by_id[r["task_id"]]["original_catalog"]["metrics"]
            assert r["original_compatibility_code"] == by_id[r["task_id"]]["original_compatibility_annotation"]["Code"]
        assert r["task_id"] != "P18" or r["protocol_variant"] == "NATIVE"
    results = ROOT / "results"
    results.mkdir(exist_ok=True)
    output = results / "interpretation_notes.jsonl"
    output.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in records))
    columns = ["task_id", "task_name", "protocol_variant", "catalog_group", "original_compatibility_code",
               "input_interface", "task_demands", "reference_evidence_type", "reference_answer_source",
               "required_inputs", "permitted_auxiliary_fields", "auxiliary_policy", "scorer_only_fields",
               "input_role_note",
               "mechanism_reference_available", "mechanism_reference_note", "good_score_establishes",
               "bad_score_establishes", "unsupported_result_claim", "native_metric", "metric_scope",
               "prepared_model_facing_fields", "prepared_case_count", "actual_supplied_information",
               "score_status", "outcome_score", "explanation_support_score", "classification_basis",
               "execution_scope_status", "source_caveat"]
    with (ROOT / "reports/interpretation_table.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        for r in records:
            writer.writerow({c: json.dumps(r.get(c), ensure_ascii=False) if isinstance(r.get(c), (dict, list)) else r.get(c) for c in columns})
    selected = [r for r in records if (r["task_id"], r["protocol_variant"]) in prepared]
    lines = ["# Interpretation alongside the evaluation records", "",
             "This table describes task contracts and score interpretation. No biological inference scores exist yet; prepared inputs have not been submitted to a solver. Demand labels are provisional analyst inferences, never claims about internal model computation.", "",
             "## Prepared protein settings", "",
             "| Setting / variant | Likely demands (provisional) | Prepared model-facing information; actually submitted: none | Reference answer source | What a good / bad score supports |",
             "|---|---|---|---|---|"]
    def escape(value):
        return str(value).replace("|", "\\|").replace("\n", " ")
    for r in selected:
        cells = [f"{r['task_id']}: {r['task_name']} ({r['protocol_variant']})",
                 "; ".join(r["task_demands"]["labels"]),
                 "; ".join(r["prepared_model_facing_fields"]), r["reference_answer_source"],
                 "Good: " + r["good_score_establishes"] + " Bad: " + r["bad_score_establishes"]]
        lines.append("| " + " | ".join(escape(c) for c in cells) + " |")
    lines += ["", "## Interpretation limits", "",
              "A correct prediction does not validate its explanation or show that the rationale caused the prediction. Reference support, an unverified hypothesis, lack of available support, and positive contradiction are different findings. An unsupported mechanistic claim is not automatically false.", "",
              "Sequence-to-outcome and sequence-to-annotation tasks remain valid even when learned protein representations may be essential. Poor TEXT performance does not diagnose general reasoning. BIO systems using learned features from the same sequence still differ in representation and training regime; additional structures, MSAs, annotations or predictor outputs must be disclosed separately.", "",
              "ROUGE/BLEU quantify reference wording agreement; they do not independently establish mechanism or experimental function. Mutation accuracy/Recall@50 recover annotated mutations, not a prospective experimental hit rate. Correlation measures assay-specific association, not calibration or causal validity. Model proxies and geometric recovery are reported as their own evidence types.", "",
              "Native metrics and restrictions remain unchanged. Coverage, invalid outputs, transport errors and official aggregation must be reported with scores. PFArena anchor/component measurements and engineering desired effects remain task-defining inputs. LAB-Bench TableQA retains its required table image. PG-LLM remains NATIVE only; none of the addendum's examples grants ablation or tuning permission.", "",
              "## Full catalog metadata", "",
              f"`../results/interpretation_notes.jsonl` and `interpretation_table.csv` cover 64 biological settings, 14 separately identified general controls, and {len(records)-len(catalog)} additional existing prepared TEXT variants. Adding metadata does not add execution permissions. The execution scope remains the eight prioritized protein settings; budget approval and protocol blockers remain recorded in the existing configuration.", "",
              "Join future score rows by BOTH `task_id` and `protocol_variant`; also retain model, source/scorer/prompt versions, context condition and run identifiers. Do not silently merge native and adapted protocols. Replace the current not-run input observation with exact dispatched-request provenance when inference is actually executed.", "",
              "The full table preserves original A–F compatibility and metrics. Classification basis points to source catalog fields, cached protocol code for prepared variants, and explicitly marked analyst inference. Other source leads remain subject to release verification. Neither benchmark names nor compatibility codes establish reasoning suitability.", "",
              f"Addendum read: `{ADDENDUM}`. SHA-256: `{addendum_hash}`. Every scenario/value in that file is illustrative; none has been added to benchmark inputs or a training corpus.", ""]
    (ROOT / "reports/INTERPRETATION_TABLE.md").write_text("\n".join(lines))
    validation = {"checked_at_pst": datetime.now(timezone(timedelta(hours=-8))).isoformat(),
                  "biological_settings": len(by_id), "general_control_groups": len(catalog)-len(by_id),
                  "metadata_rows": len(records), "prepared_variants": len(prepared),
                  "prepared_case_count": sum(prepared.values()), "prepared_inputs_sha256": input_hash,
                  "all_task_variant_keys_unique": True, "original_metrics_and_compatibility_retained": True,
                  "demand_classifications_provisional": True, "addendum_sha256": addendum_hash,
                  "benchmark_inference_performed": False, "illustrative_examples_used_as_data": False,
                  "notes": "Interpretation metadata only; native/source and draft TEXT protocol variants remain distinct."}
    (ROOT / "reports/interpretation_validation.json").write_text(json.dumps(validation, indent=2) + "\n")
    print(json.dumps(validation, indent=2))

if __name__ == "__main__":
    write_reports()
