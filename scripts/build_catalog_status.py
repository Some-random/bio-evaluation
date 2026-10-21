#!/usr/bin/env python3
"""Build the 57-setting status tracker from aggregate evidence; no model calls."""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime
import hashlib
import json
import math
from pathlib import Path
from zoneinfo import ZoneInfo

PACIFIC = ZoneInfo("America/Los_Angeles")
CATEGORIES = {
    "done": "Done: defined score for the declared evaluated condition",
    "running": "Running generation",
    "queued": "Queued for generation in the frozen runtime",
    "agent_work": "Unfinished agent work",
    "user_held": "Held at the user's request",
    "provider_held": "Biological/provider interruption or restriction",
    "impossible": "Whole setting established impossible",
}
SHORT_LABELS = {"done": "Done", "running": "Running", "queued": "Queued", "agent_work": "Unfinished agent work", "user_held": "User held", "provider_held": "Provider held", "impossible": "Impossible"}
AGENT_ACTIONS = {
    "P04": ("Inventory the acquired 520-case test LMDB, review assay eligibility, isolate targets and freeze a scalar delivery/scoring contract.", ".local/source_acquisition_2026-10-19/prediction_datasets/summary.json", "Source archive acquired; assay eligibility and runtime preparation remain unfinished."),
    "P05": ("Review the available FLIP AAV assay scope, isolate test inputs/targets and freeze scalar delivery and scoring.", "reports/catalog_extended_preparation.json", "Released inputs available; eligibility review and execution preparation unfinished."),
    "P17": ("Review permissible assay scopes in the acquired ProteinGym release and implement a version-matched, full-denominator score adapter.", ".local/source_acquisition_2026-10-19/prediction_datasets/summary.json", "217 released assay CSVs acquired; reviewed execution scope remains unfinished."),
    "P19": ("Preserve the three failed synthetic delivery outputs. Implement and CPU-test input-valid, unique ranking constraints as a separate prospective condition before any new delivery gate; the 34-case benchmark has not started.", ".local/catalog_execution_2026-10-20/tasks/P19/standalone_execution_v1/failure_closure.json", "Independent runtime worked, but all three actual development rankings failed sequence-position validity. Full native coverage separately has 77 unreviewed and 12 held assays."),
    "P21": ("Prepare permitted T3 anchor and candidate inputs from the 67 acquired tables, isolate target scores, and validate complete ranking delivery.", ".local/source_recovery_round2_2026-10-19/pfarena/native_preflight/status.json", "Required source tables acquired; eligibility, input isolation and runtime integration unfinished."),
    "P22": ("Prepare permitted T4 component-context and candidate inputs from the 29 acquired pairs, isolate target scores, and validate complete ranking delivery.", ".local/source_recovery_round2_2026-10-19/pfarena/native_preflight/status.json", "All 29 context/target pairs acquired; eligibility, isolation and runtime integration unfinished."),
    "P27": ("Freeze a defensible available protein-description adaptation with fixed cohort/reference preprocessing; retain exact temporal NatureLM condition as unavailable.", ".local/source_recovery_round2_2026-10-19/paper_artifacts/PUBLIC_SUMMARY.json", "Exact native NCBI dates/accession manifest not found in audited author releases; labelled adaptation remains possible."),
    "P34": ("Integrate the acquired encoder and five existing heads with the released optimization/scoring contract and explicit failure handling; preserve the held sixth landscape.", "reports/SOURCE_ACQUISITION_PROGRESS_2026-10-19.json", "Existing evaluator assets acquired; released-code algorithm and runtime implementation unfinished; no new training."),
    "P35": ("Validate and freeze the native ProtST execution runtime, then run all five top-20 query rankings over the qualified 34,464-input corpus. The CPU runner is ready; the separate CUDA route needs compatibility checks.", ".local/catalog_execution_2026-10-20/tasks/P35/delivery_v1/handoff_manifest.json", "Executable native ProtST demo and nine neutral checks are complete; no pretrained forward has run. It is not a Qwen result. The release provides no relevance gold or aggregate accuracy metric."),
    "P37": ("Assemble and validate an isolated OmegaFold2 runtime/checkpoint, then pass an independent development gate for the declared released-code condition.", ".local/catalog_execution_2026-10-20/tasks/P37/readiness.json", "Matching released-code evaluator assets acquired; exact native sampling and 50% clustering condition unavailable in inspected releases."),
    "P38": ("Validate NetSolP-D runtime, acquire the available ProtT5 encoder for the separate thermal proxy, and freeze independent generation/delivery contracts without training heads.", ".local/catalog_execution_2026-10-20/tasks/P38/readiness.json", "Exact SFM property heads/reference cohort unavailable in inspected releases; distinct available proxy conditions prepared."),
    "P39": ("Freeze a clearly labelled available structural case-study condition and its complete selection/denominator contract using acquired evaluator assets; report proxy evidence without invented binding accuracy.", "reports/REMAINING_DESIGN_SOURCE_FEASIBILITY_2026-10-15.json", "Exact native cohort, selection manifest and scoring contract unreleased in inspected sources; qualitative adaptation remains possible."),
    "P40": ("Independently review the 60 cases and implement a solver adapter that preserves permitted geometric context while hiding target residue identities and coordinates.", ".local/catalog_execution_2026-10-20/tasks/P40/status.json", "60 current-structure mappings/masks prepared; exact historical processed bytes not certified; current-structure adaptation available."),
    "P41": ("Assemble the available released-demo structural runtime and its masking/scoring adapter; document differences from the unreleased native holdout.", "reports/REMAINING_DESIGN_SOURCE_FEASIBILITY_2026-10-15.json", "Released checkpoints/vendor assets and demos acquired; exact SAbDab holdout, masks and full benchmark aggregation unavailable in inspected releases."),
    "P44": ("Recover the explanation-assessment cohort and reference dossier, validate a separately named available judge/rubric adapter, then complete permitted local delivery and scoring.", ".local/catalog_execution_2026-10-20/tasks/P44/task.json", "User removed the BioReason-Pro judging hold; explanation assessment remains distinct from existing GO annotation scores. Exact paper judge/cohort equivalence still requires verification."),
    "V06": ("Prepare the complete image/question cohort with isolated references, validate a declared available judge or human-score adapter and full-denominator aggregation, then complete permitted delivery and scoring.", ".local/catalog_execution_2026-10-20/tasks/V06/task.json", "User waived the original GPT-4-0314 requirement; a replacement judging condition may proceed with its differences explicit. This does not authorize new paid inference."),
    "V07": ("Review the 2,215 question/full-deck scopes, run actual processor expansion and 20-image context checks, then pass the independent delivery gate.", ".local/catalog_execution_2026-10-20/tasks/V07/status.json", "All 8,000 page identities materialized/hash-verified; mixed original/processed image adaptation available; exact Table 3 condition unavailable."),
}
USER_HOLDS = {
    "P33": "New head training remains held. Search already released matching heads and prepare metadata; a different training scope requires a user decision.",
}
PROVIDER_HOLDS = {"P18", "B06", "P20", "P30", "P31", "P32", "P36"}
CONTINUATION_MANIFEST_SHA256 = "64b1f81dfa7a138458905736545ecb93f592c7cd85dc8528b6621ca125b260d4"
BLOCKERS_PATH = "reports/CATALOG_BLOCKERS_2026-10-20.json"
DEEPFRI_OUTPUT_DIMENSIONS = {"P12": 538, "P13": 1943, "P14": 489, "P15": 320}


def load(path: Path):
    return json.loads(path.read_text()) if path.is_file() else None


def timestamp(data):
    if not isinstance(data, dict):
        return None
    return next((data[k] for k in ("scored_at_pacific", "updated_at_pacific", "at_pacific", "finished_at_pacific", "generated_at_pacific", "frozen_at_pacific", "observed_at_pacific") if data.get(k)), None)


def age_seconds(value, now):
    if not value:
        return None
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
        return round((now - dt).total_seconds()) if dt.tzinfo else None
    except (TypeError, ValueError):
        return None


def score_defined(data):
    if not isinstance(data, dict):
        return False
    if any(data.get(key) is False for key in ("all_case_primary_available", "full_primary_metric_defined", "full_benchmark_score_defined", "full_planned_primary_metrics_valid")):
        return False
    metrics = data.get("metrics", data)
    values = [metrics.get(key) for key in ("spearman", "accuracy_percent", "accuracy", "auroc", "average_precision", "fmax", "ap", "AP", "Fmax", "auprc@micro", "f1_max")]
    values.append(data.get("primary_metric_value"))
    if "auprc@micro" in metrics or "f1_max" in metrics:
        return all(isinstance(metrics.get(key), (int, float)) and not isinstance(metrics.get(key), bool) and math.isfinite(metrics[key]) for key in ("auprc@micro", "f1_max"))
    return any(isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value) for value in values)


def explain_unfinished(row, reasons):
    """Explain missing work separately from a task's execution category."""
    if row["category"] == "done":
        return {"why_not_done": None, "blocker_owner": None,
                "finish_requirement": "A defined score for this declared condition is already retained.",
                "next_deliverable": row["next_action"], "needs_user_decision": False}
    task = row["task_id"]
    if task == "V06" and row.get("separate_local_execution_verified"):
        return {"why_not_done": row["status"], "blocker_owner": "Existing isolated V06 worker",
                "finish_requirement": row["next_action"], "next_deliverable": row["next_action"],
                "needs_user_decision": False}
    if task in DEEPFRI_OUTPUT_DIMENSIONS and row["category"] in {"running", "queued"}:
        dimension = DEEPFRI_OUTPUT_DIMENSIONS[task]
        runtime = row.get("runtime") or {}
        saved, planned = runtime.get("responses_saved"), runtime.get("planned")
        if row["category"] == "running":
            count = f"{saved:,}/{planned:,} responses saved in the unsealed progress record. " if type(saved) is int and type(planned) is int else ""
            reason = count + f"Generation is still incomplete; each case requires {dimension:,} ordered confidence values. The three active task workers share one A100. Full-cohort scoring has not started."
            deliverable = "Finish the untouched cases, seal all outcomes, then calculate the full-cohort native AP/Fmax scores."
        else:
            reason = f"Its exact benchmark grant is queued, but its worker has not started. The existing three-client runtime starts the grant when a task-worker slot opens. Each answer requires {dimension:,} confidence values."
            deliverable = "Start the existing grant when a task-worker slot opens, then complete and score the fixed cohort."
        return {"why_not_done": reason, "blocker_owner": "Agent scheduling / existing generation workers",
                "finish_requirement": deliverable, "next_deliverable": deliverable,
                "needs_user_decision": False}
    if task in reasons:
        item = reasons[task]
        keys = ("why_not_done", "blocker_owner", "finish_requirement", "next_deliverable", "needs_user_decision")
        if any(key not in item for key in keys) or not all(item[key] for key in keys[:-1]):
            raise ValueError("Incomplete unfinished-work explanation: " + task)
        return {key: item[key] for key in keys}
    return {"why_not_done": row["status"], "blocker_owner": "Agent evidence reconciliation",
            "finish_requirement": row["next_action"], "next_deliverable": row["next_action"],
            "needs_user_decision": False}


def task_queue_evidence(root, task, direct, now):
    """Prefer verified successor queue records; preserve old operational exits."""
    original = root / ".local/catalog_execution_2026-10-20/runtime/queue"
    result = {"grant": original / f"10_{task}_benchmark.grant.json",
              "started": original / f"10_{task}_benchmark.started.json",
              "finished": original / f"10_{task}_benchmark.finished.json",
              "continuation": False, "evidence_paths": []}
    base = root / ".local/catalog_execution_2026-10-20/continuation_v1"
    runtime = base / "runtime"
    stem = f"{task}_benchmark_continuation1"
    grant_path = runtime / "queue" / (stem + ".grant.json")
    paths = {"manifest": base / "manifest.json", "submission": base / "submission_receipt.json",
             "pool": runtime / "status.json", "identity": runtime / "server_identity.json",
             "predecessor": runtime / "predecessor_terminal_receipt.json",
             "boundary": runtime / f"{task}_boundary.json", "grant": grant_path}
    try:
        if not all(path.is_file() and not path.is_symlink() for path in paths.values()):
            return result
        docs = {key: load(path) for key, path in paths.items()}
        manifest, pool, identity, grant = (docs[key] for key in ("manifest", "pool", "identity", "grant"))
        if hashlib.sha256(paths["manifest"].read_bytes()).hexdigest() != CONTINUATION_MANIFEST_SHA256:
            return result
        job = str(docs["submission"]["job_id"])
        age = age_seconds(timestamp(pool), now)
        if (task not in manifest["task_ids"] or pool.get("stage") != "serving_task_queue"
                or age is None or not -60 <= age <= 180
                or str(pool.get("job_id")) != job or str(identity.get("job_id")) != job
                or str(docs["predecessor"].get("successor_job_id")) != job
                or str(docs["predecessor"].get("original_job_id")) != str(manifest["original_job_id"])
                or docs["predecessor"].get("original_job_state") not in {
                    "COMPLETED", "FAILED", "CANCELLED", "TIMEOUT", "PREEMPTED", "NODE_FAIL"}
                or grant.get("task_id") != task or grant.get("authorized") is not True
                or grant.get("config_sha256") != docs["boundary"].get("config_sha256")
                or grant.get("continuation_boundary_sha256") != hashlib.sha256(paths["boundary"].read_bytes()).hexdigest()
                or grant.get("server_identity_sha256") != hashlib.sha256(paths["identity"].read_bytes()).hexdigest()):
            return result
        if direct and (direct.get("run_id") != grant.get("run_id")
                       or direct.get("config_sha256") != grant.get("config_sha256")):
            return result
        result.update(grant=grant_path, started=grant_path.with_name(stem + ".started.json"),
            finished=grant_path.with_name(stem + ".finished.json"), continuation=True,
            job_id=job, active_client=stem in pool.get("active_clients", []),
            evidence_paths=[str(path.relative_to(root)) for path in paths.values()])
    except (OSError, ValueError, TypeError, KeyError):
        pass
    return result


def _v06_continuation_evidence(root, now):
    """Prefer admitted untouched31 closure; reject inconsistent completion claims."""
    task = root / ".local/catalog_execution_2026-10-20/tasks/V06"
    base, source = task / "untouched_judge_continuation_v1", task / "local_execution_v2"
    paths = {name: base / filename for name, filename in
             (("plan", "plan.json"), ("admission", "root_admission.json"),
              ("submission", "submission_receipt.json"))}
    # An unadmitted preparation plan alone cannot supersede the strict run.
    if not paths["admission"].exists() and not paths["submission"].exists() and not (base / "runtime/run_v1").exists():
        return None
    digest = lambda path: hashlib.sha256(path.read_bytes()).hexdigest()
    canonical = lambda data: hashlib.sha256(json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()
    result = {"category": "agent_work", "substatus": "V06_continuation_evidence_reconciliation",
        "status": "V06 continuation evidence needs reconciliation; no complete score or current dispatch is established.",
        "next_action": "Inspect preserved admission, identity, source and output-lock evidence; do not automatically retry.",
        "runtime": None, "prepared_benchmark_planned": 193,
        "separate_local_execution_verified": False, "evidence_paths": [],
        "scope_notes": ["The strict predecessor remains unchanged. The continuation reuses 193 solver answers and 162 saved judge replies, and permits only 31 untouched judge calls.",
                        "Single complete outer JSON fences are removed under a separately declared parser repair, with the original identity/numeric validation and mean per-case ratio formula; this local self-judge score is not clinical accuracy."]}

    def require(condition):
        if not condition:
            raise ValueError("Inconsistent V06 continuation evidence")

    def document(path):
        require(path.is_file() and not path.is_symlink())
        result["evidence_paths"].append(str(path.relative_to(root)))
        return load(path)

    def ordered(rows, count):
        return (isinstance(rows, list) and len(rows) == count and
                all(isinstance(row, dict) and type(row.get("question_id")) is int for row in rows) and
                [row["question_id"] for row in rows] == list(range(count)))

    try:
        plan, admission, submission = (document(paths[key]) for key in ("plan", "admission", "submission"))
        plan_sha, admission_sha = digest(paths["plan"]), digest(paths["admission"])
        require(plan.get("task_id") == "V06" and plan.get("planned") == 193 and
                plan.get("execution_scope") == "retained_V06_judge_untouched31_full193closure" and
                plan.get("new_judge_planned") == 31 and plan.get("new_solver_calls_planned") == 0 and
                plan.get("gpus_requested") == 1 and admission.get("admitted") is True and
                admission.get("task_id") == "V06" and admission.get("plan_sha256") == plan_sha and
                admission.get("gpu_count") == 1 and admission.get("project_gpu_ceiling") == 8 and
                admission.get("scope") == "judge_untouched31_once_reuse_locked193solver_and162judge" and
                submission.get("task_id") == "V06" and submission.get("returncode") == 0 and
                submission.get("plan_sha256") == plan_sha and submission.get("admission_sha256") == admission_sha and
                str(submission.get("job_id", "")).isdigit())
        require(Path(plan["source_plan_path"]).resolve() == (source / "plan.json").resolve() and
                plan["source_plan_sha256"] == digest(source / "plan.json") and
                Path(plan["source_output_root"]).resolve() == (source / "runtime/run_v1").resolve() and
                Path(plan["output_root"]).resolve() == (base / "runtime/run_v1").resolve())
        source_plan = document(source / "plan.json")
        require(plan.get("model_configuration") == source_plan.get("model_configuration") and
                plan.get("judge_declaration") == source_plan.get("judge_declaration") and
                plan.get("manifest") == source_plan.get("manifest") and
                plan["model_configuration"].get("max_tokens") == 16384 and
                plan["model_configuration"].get("chat_template_kwargs") == {"enable_thinking": False})
        job = str(submission["job_id"])
        result.update(category="queued", substatus="V06_continuation_submitted_no_dispatch_proof",
            status=f"Independent V06 judge continuation job {job} was submitted; submission is not dispatch evidence.",
            next_action="Let the existing admitted worker pass its own server and neutral judge gates, then finish only the 31 untouched judgements.",
            separate_local_execution_verified=True)
        runtime_path, folder = base / "runtime/status.json", base / "runtime/run_v1"
        runtime = load(runtime_path) or {}
        if runtime:
            result["evidence_paths"].append(str(runtime_path.relative_to(root)))
            if runtime.get("stage") == "stopped_for_review":
                result.update(category="agent_work", substatus="V06_continuation_runtime_stopped_for_review",
                    status="V06 continuation stopped for review; missing progress does not establish zero attempts.")
            elif runtime.get("stage") == "starting_independent_V06_server":
                age = age_seconds(timestamp(runtime), now)
                if str(runtime.get("job_id")) != job or age is None or not -60 <= age <= 600:
                    result.update(category="agent_work", substatus="V06_continuation_stale_startup",
                        status="V06 continuation startup evidence is stale or mismatched; current attempts are unknown.")
        completion_path, progress_path = folder / "completion.json", folder / "progress.json"
        complete, progress = load(completion_path), load(progress_path)
        direct = complete or progress
        if not direct:
            return result
        identity = document(base / "runtime/server_identity.json")
        require(str(identity.get("job_id")) == job and identity.get("plan_sha256") == plan_sha and
                identity.get("admission_sha256") == admission_sha and identity.get("endpoint") == plan.get("endpoint"))
        result["evidence_paths"].append(str((completion_path if complete else progress_path).relative_to(root)))
        counts, new_counts = direct.get("judge"), direct.get("new_judge")
        result["runtime"] = {"run_id": plan["run_id"], "active_job_id": job, "phase": "judge" if new_counts else "neutral_development",
            "recorded_at_pacific": timestamp(direct), "age_seconds_at_observation": age_seconds(timestamp(direct), now),
            "sealed_complete": complete is not None, "unsealed_counts_are_lower_bounds": complete is None,
            "planned": 193, "responses_saved": counts.get("responses_saved") if counts else None,
            "judge": counts, "new_judge": new_counts, "source_solver_responses_reused": 193,
            "source_judge_responses_reused": 162, "native_scoring_status": direct.get("native_scoring_status", "not_started")}
        age, owner_age = age_seconds(timestamp(direct), now), age_seconds(timestamp(runtime), now)
        fresh_owner = (str(runtime.get("job_id")) == job and runtime.get("stage") == "serving_frozen_V06_protocol" and
                       owner_age is not None and -60 <= owner_age <= 180)
        if (not complete and direct.get("stage") == "untouched_judge_generation" and new_counts and
                new_counts.get("attempted_with_observed_outcome", 0) > 0 and
                ((age is not None and -60 <= age <= 600) or fresh_owner)):
            result.update(category="running", substatus="V06_untouched_judge_continuation_live_evidence",
                status=f"Direct V06 untouched-judge progress matches admitted job {job}; saved replies are not a completed score.")
            return result
        if not complete and direct.get("stage") == "neutral_judge_delivery_gates":
            result.update(substatus="V06_continuation_development_only",
                status="V06 continuation is checking neutral judge delivery; this is not benchmark dispatch or scoring.")
            return result
        result.update(category="agent_work", substatus="V06_continuation_lock_or_score_reconciliation",
            status="V06 continuation is terminal or stale; full source/combined locks and a defined 193-case score need verification.")
        if not complete or complete.get("benchmark_primary_defined") is not True:
            return result
        score_path, judge_path, source_lock_path = folder / "scores.json", folder / "judge_lock.json", folder / "source_prediction_lock.json"
        score, judge, prediction_lock = (document(path) for path in (score_path, judge_path, source_lock_path))
        original_folder = source / "runtime/run_v1"
        original_lock = document(original_folder / "prediction_lock.json")
        original_judge_lock = document(original_folder / "judge_lock.json")
        original_outcomes = document(original_folder / "judge_outcomes.json")
        manifest = document(Path(plan["manifest"]))
        predictions = document(original_folder / "predictions.json")
        outcomes, judgements = (document(folder / name) for name in ("judge_outcomes.json", "judgements.json"))
        terminal = document(base / "runtime/terminal_receipt.json")
        require(prediction_lock == original_lock and digest(source_lock_path) == digest(original_folder / "prediction_lock.json") and
                prediction_lock.get("generation_closed") is True and prediction_lock.get("planned") == 193 and
                prediction_lock.get("terminal_records") == 193 and ordered(manifest, 193) and ordered(predictions, 193) and
                prediction_lock.get("manifest_sha256") == canonical(manifest) and
                prediction_lock.get("predictions_sha256") == canonical(predictions) and
                all(row.get("status") == "completed" and isinstance(row.get("text"), str) and row["text"].strip() for row in predictions))
        require(original_judge_lock.get("closed") is True and original_judge_lock.get("planned") == 193 and
                original_judge_lock.get("prediction_lock_sha256") == digest(original_folder / "prediction_lock.json") and
                original_judge_lock.get("outcomes_sha256") == digest(original_folder / "judge_outcomes.json") and
                original_judge_lock.get("judgements_sha256") == digest(original_folder / "judgements.json") and
                ordered(original_outcomes, 193) and
                all(row.get("status") == "not_dispatched_after_stop" for row in original_outcomes[162:]))
        require(judge.get("closed") is True and judge.get("planned") == 193 and judge.get("reused_raw_responses") == 162 and
                judge.get("execution_condition") == plan.get("condition") and
                judge.get("source_prediction_lock_sha256") == digest(source_lock_path) and
                judge.get("judge_declaration_sha256") == canonical(plan["judge_declaration"]) and
                judge.get("outcomes_sha256") == digest(folder / "judge_outcomes.json") and
                judge.get("judgements_sha256") == digest(folder / "judgements.json") and
                ordered(outcomes, 193) and ordered(judgements, 193) and
                all(row.get("status") == "completed" for row in outcomes) and
                all(outcomes[index].get(key) == original_outcomes[index].get(key)
                    for index in range(162) for key in ("request_sha256", "raw_response_sha256")))
        ratios = []
        for row in judgements:
            require(set(row) == {"question_id", "reference_score", "candidate_score", "comment", "judge_declaration_sha256"} and
                    row["judge_declaration_sha256"] == canonical(plan["judge_declaration"]) and
                    isinstance(row["comment"], str) and bool(row["comment"].strip()))
            values = [row["candidate_score"], row["reference_score"]]
            require(all(type(value) in (int, float) and math.isfinite(value) and 1 <= value <= 10 for value in values))
            ratios.append(float(values[0]) / float(values[1]))
        overall = score.get("groups", {}).get("overall", {})
        value = overall.get("released_mean_case_ratio_score")
        require(score.get("execution_condition") == plan.get("condition") and score.get("judge_declaration") == plan.get("judge_declaration") and
                score.get("lock_sha256") == canonical(prediction_lock) and overall.get("complete") is True and
                overall.get("planned") == overall.get("valid") == 193 and
                all(overall.get(key, 0) == 0 for key in ("generation_failure_or_invalid_answer", "missing_judgement", "invalid_judgement")) and
                type(value) in (int, float) and math.isfinite(value) and value == 100 * sum(ratios) / 193 and
                complete.get("released_mean_case_ratio_score") == value and
                complete.get("execution_condition") == plan.get("condition") and complete.get("new_solver_calls") == 0 and
                complete.get("source_solver_responses_reused") == 193 and complete.get("source_judge_responses_reused") == 162 and
                counts.get("planned") == counts.get("responses_saved") == 193 and
                new_counts.get("planned") == new_counts.get("attempted_with_observed_outcome") == new_counts.get("responses_saved") == 31 and
                all(new_counts.get(key, 0) == 0 for key in ("transport_errors", "http_errors", "response_errors", "refusals", "truncations", "empty_finals", "not_dispatched_after_stop")) and
                str(terminal.get("job_id")) == job and terminal.get("completion_sha256") == digest(completion_path) and terminal.get("completion") == complete)
        result.update(category="done", substatus="defined_V06_untouched_judge_continuation_score",
            status="Complete 193-case V06 local-judge score verified against the combined judge closure and unchanged source solver lock.",
            next_action="Preserve the published local-judge/parser-repair score and original strict predecessor; no V06 generation remains.", score=score)
        result["runtime"]["native_scoring_status"] = "completed_verified_full193_local_judge_with_declared_parser_repair"
        return result
    except (OSError, ValueError, TypeError, KeyError, AttributeError):
        return result


def v06_execution_evidence(root, now):
    continuation = _v06_continuation_evidence(root, now)
    return continuation if continuation is not None else _v06_strict_execution_evidence(root, now)


def _v06_strict_execution_evidence(root, now):
    """Read the separately admitted worker; a submission is never dispatch proof."""
    base = root / ".local/catalog_execution_2026-10-20/tasks/V06/local_execution_v2"
    paths = {"plan": base / "plan.json", "admission": base / "root_admission.json",
             "submission": base / "submission_receipt.json"}
    digest = lambda path: hashlib.sha256(path.read_bytes()).hexdigest()
    try:
        if not all(p.is_file() and not p.is_symlink() for p in paths.values()):
            return None
        docs = {k: load(p) for k, p in paths.items()}
        plan, admission, submission = (docs[k] for k in ("plan", "admission", "submission"))
        plan_sha, admission_sha = digest(paths["plan"]), digest(paths["admission"])
        if (plan.get("task_id") != "V06" or plan.get("planned") != 193
                or admission.get("admitted") is not True or admission.get("task_id") != "V06"
                or admission.get("plan_sha256") != plan_sha
                or submission.get("plan_sha256") != plan_sha
                or submission.get("admission_sha256") != admission_sha
                or submission.get("task_id") != "V06" or submission.get("returncode") != 0
                or not str(submission.get("job_id", "")).isdigit()):
            return None
        job = str(submission["job_id"])
        result = {"category": "queued", "substatus": "separate_V06_submitted_no_dispatch_proof",
                  "status": f"Independent V06 job {job} was submitted. No benchmark dispatch is established by the submission receipt.",
                  "next_action": "Let the existing worker finish its pinned runtime/server checks and neutral delivery gates before the one-attempt 193-case solver and local-judge phases.",
                  "runtime": None, "prepared_benchmark_planned": 193,
                  "separate_local_execution_verified": True,
                  "evidence_paths": [str(p.relative_to(root)) for p in paths.values()],
                  "scope_notes": ["V1 job 244379 stopped at a package-version guard before model requests; its failed infrastructure evidence is preserved. V2 installs the pinned runtime independently, with unchanged 193 inputs and 16K solver/judge settings.",
                                  "The user waived GPT-4-0314. This is a separately declared Qwen solver/local-Qwen judge adaptation; a teacher-comparison ratio is not clinical accuracy."]}
        runtime_path = base / "runtime/status.json"
        runtime = load(runtime_path) or {}
        if runtime:
            result["evidence_paths"].append(str(runtime_path.relative_to(root)))
            if str(runtime.get("job_id")) == job and runtime.get("stage") == "starting_independent_V06_server":
                age = age_seconds(timestamp(runtime), now)
                if age is not None and -60 <= age <= 600:
                    result["status"] = f"Independent V06 job {job} is starting its server; benchmark dispatch has not been established."
                else:
                    result.update(category="agent_work", substatus="V06_stale_startup_observation",
                        status="V06's recorded server-startup state is stale; current runtime and benchmark attempts are unknown.",
                        next_action="Inspect the existing job and runtime evidence before describing it as currently running; do not automatically retry.")
            elif runtime.get("stage") == "stopped_for_review":
                result.update(category="agent_work", substatus="V06_runtime_stopped_for_review",
                    status="The independent V06 runtime stopped for review. Missing benchmark progress does not establish zero attempts.",
                    next_action="Diagnose the preserved V06 stop evidence and reconcile any outputs; no automatic retry or protocol change.")
        folder = base / "runtime/run_v1"
        completion_path, progress_path = folder / "completion.json", folder / "progress.json"
        complete, progress = load(completion_path), load(progress_path)
        direct = complete or progress
        if not direct:
            return result
        identity_path = base / "runtime/server_identity.json"
        identity = load(identity_path) or {}
        if (str(identity.get("job_id")) != job or identity.get("plan_sha256") != plan_sha
                or identity.get("admission_sha256") != admission_sha
                or identity.get("endpoint") != plan.get("endpoint")):
            result.update(category="agent_work", substatus="V06_identity_reconciliation",
                          status="V06 runtime records exist but do not match the admitted server identity; current dispatch counts are unverified.",
                          next_action="Inspect the preserved V06 identity/progress mismatch before any continuation; no automatic retry.")
            return result
        result["evidence_paths"].extend(str(p.relative_to(root)) for p in
            (identity_path, completion_path if complete else progress_path))
        phase = "judge" if isinstance(direct.get("judge"), dict) else "solver"
        counts = direct.get(phase)
        result["runtime"] = {"run_id": plan["run_id"], "active_job_id": job,
            "recorded_at_pacific": timestamp(direct), "age_seconds_at_observation": age_seconds(timestamp(direct), now),
            "sealed_complete": complete is not None, "unsealed_counts_are_lower_bounds": complete is None,
            "phase": phase if counts else "neutral_development", "solver": direct.get("solver"), "judge": direct.get("judge"),
            "planned": 193, "responses_saved": counts.get("responses_saved") if counts else None,
            "native_scoring_status": direct.get("native_scoring_status", "not_started")}
        stage, age = direct.get("stage"), age_seconds(timestamp(direct), now)
        runtime_age = age_seconds(timestamp(runtime), now)
        fresh_owner = (str(runtime.get("job_id")) == job and runtime.get("stage") == "serving_frozen_V06_protocol"
                       and runtime_age is not None and -60 <= runtime_age <= 180)
        if stage in {"solver_generation", "local_judging"} and counts and counts.get("attempted_with_observed_outcome", 0) > 0 and ((age is not None and -60 <= age <= 600) or fresh_owner):
            result.update(category="running", substatus="separate_V06_generation_live_evidence",
                status=f"Direct V06 {phase} benchmark progress matches the admitted independent job {job}. Saved responses are not a completed benchmark score.",
                next_action="Finish this existing one-attempt solver/judge cohort, preserve every failure and score only after both output locks close.")
        elif stage == "neutral_delivery_gates":
            result.update(substatus="separate_V06_development_only",
                status="V06 is checking neutral development delivery on its independent server. This is not benchmark scoring or evidence of benchmark dispatch.")
        else:
            result.update(category="agent_work", substatus="V06_terminal_or_stale_runtime_reconciliation",
                status=f"V06's recorded stage is {stage!r}; it does not establish current running generation or a complete defined score.",
                next_action="Inspect the existing V06 terminal/progress evidence and reconcile its full denominator; preserve stop rules and do not automatically retry.")
        if complete and complete.get("benchmark_primary_defined") is True:
            score_path, lock_path, judge_path = folder / "scores.json", folder / "prediction_lock.json", folder / "judge_lock.json"
            score, judge = load(score_path) or {}, load(judge_path) or {}
            overall = score.get("groups", {}).get("overall", {})
            value = overall.get("released_mean_case_ratio_score")
            canonical_digest = lambda data: hashlib.sha256(json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()
            locked = (all(p.is_file() for p in (score_path, lock_path, judge_path))
                      and complete.get("prediction_lock_sealed") is True and complete.get("judge_outcome_lock_sealed") is True
                      and judge.get("closed") is True and judge.get("planned") == 193
                      and judge.get("prediction_lock_sha256") == digest(lock_path)
                      and score.get("lock_sha256") == canonical_digest(load(lock_path))
                      and score.get("judge_declaration") == plan.get("judge_declaration")
                      and all((folder / name).is_file() and digest(folder / name) == judge.get(key)
                              for name, key in (("judge_outcomes.json", "outcomes_sha256"), ("judgements.json", "judgements_sha256"))))
            if locked and overall.get("complete") is True and overall.get("planned") == 193 and overall.get("valid") == 193 and type(value) in (int, float) and math.isfinite(value) and complete.get("released_mean_case_ratio_score") == value:
                result.update(category="done", substatus="defined_separate_local_judge_score",
                    status="Complete declared V06 local-judge condition scored with sealed solver and judge outputs.",
                    next_action="Preserve and publish the separate local-judge score, raw outcomes and qualifications.", score=score)
                result["evidence_paths"].extend(str(p.relative_to(root)) for p in (score_path, lock_path, judge_path))
        return result
    except (OSError, ValueError, TypeError, KeyError):
        return None


def build(root: Path):
    now = datetime.now(PACIFIC)
    table_path = root / "reports/EVALUATION_DECISION_TABLE.json"
    table = load(table_path)
    retained = table["retained_setting_ids"]
    assert len(retained) == len(set(retained)) == 57
    table_rows = table["rows"]
    blocker_document = load(root / BLOCKERS_PATH) or {}
    reasons = blocker_document.get("reasons", {})
    names = {r["task_id"]: r["task"] for r in table_rows}
    task_root = root / ".local/catalog_execution_2026-10-20/tasks"
    queue = root / ".local/catalog_execution_2026-10-20/runtime/queue"
    pool_path = root / ".local/catalog_execution_2026-10-20/runtime/status.json"
    pool = load(pool_path) or {}
    pool_age = age_seconds(timestamp(pool), now)
    pool_fresh = pool_age is not None and pool_age <= 180 and pool.get("stage") == "serving_task_queue"
    historic_done = {r["task_id"] for r in table_rows if r.get("source_row_category") == "completed_rows"}
    evidence_records = {}

    def evidence(relative):
        path = root / relative
        if relative not in evidence_records:
            raw = path.read_bytes() if path.is_file() else None
            data = load(path) if raw and path.suffix == ".json" else None
            evidence_records[relative] = {
                "path": relative,
                "available": raw is not None,
                "sha256": hashlib.sha256(raw).hexdigest() if raw else None,
                "recorded_at_pacific": timestamp(data),
                "observed_at_pacific": now.isoformat(),
            }
        return evidence_records[relative]

    def relative(path):
        return str(path.relative_to(root))

    rows = []
    for task in retained:
        metadata = task_root / task
        completion_path = metadata / "runtime/benchmark/completion.json"
        progress_path = metadata / "runtime/benchmark/progress.json"
        completion, progress = load(completion_path), load(progress_path)
        direct = completion or progress
        row = {
            "task_id": task,
            "task_name": names[task],
            "category": None,
            "substatus": None,
            "status": None,
            "next_action": None,
            "decision_needed": None,
            "exact_native_condition_availability": "A score for the declared evaluated scope does not establish matched-paper reproduction.",
            "whole_setting_established_impossible": False,
            "observed_at_pacific": now.isoformat(),
            "evidence_recorded_at_pacific": None,
            "evidence_paths": [],
            "runtime": None,
            "prepared_benchmark_planned": {"P06": 1366, "P07": 27217, "P08": 12851, "P12": 1919, "P13": 3416, "P14": 3416, "P15": 3416}.get(task),
            "score": None,
            "scope_notes": [],
        }
        if direct:
            row["runtime"] = {k: direct.get(k) for k in ("run_id", "planned", "attempted_confirmed", "terminal", "responses_saved", "delivery_passed", "transport_errors", "http_errors", "response_errors", "truncations", "empty_finals", "refusals", "prediction_lock_sha256")}
            row["runtime"]["recorded_at_pacific"] = timestamp(direct)
            row["runtime"]["age_seconds_at_observation"] = age_seconds(timestamp(direct), now)
            row["runtime"]["sealed_complete"] = completion is not None
            row["runtime"]["unsealed_counts_are_lower_bounds"] = completion is None
            row["evidence_paths"].append(relative(completion_path if completion else progress_path))

        score_candidates = [metadata / "runtime/benchmark/scores.json", metadata / "runtime/benchmark/scoring_repair_v1/scores.json", metadata / "scores.json"]
        def consistent_score(path):
            candidate = load(path)
            if not score_defined(candidate):
                return False
            if completion:
                planned = completion.get("planned")
                if not isinstance(planned, int) or not planned or completion.get("all_passed") is not True:
                    return False
                if any(completion.get(key) != planned for key in ("terminal", "responses_saved", "delivery_passed")):
                    return False
                if candidate.get("prediction_lock_sha256") != completion.get("prediction_lock_sha256"):
                    return False
                lock_path = metadata / "runtime/benchmark/prediction_lock.json"
                if not lock_path.is_file() or hashlib.sha256(lock_path.read_bytes()).hexdigest() != completion.get("prediction_lock_sha256"):
                    return False
                if candidate.get("config_sha256") and completion.get("config_sha256") and candidate["config_sha256"] != completion["config_sha256"]:
                    return False
                for container in (candidate, candidate.get("metrics", {})):
                    if container.get("planned") is not None and container["planned"] != planned:
                        return False
                    if any(container.get(key) is not None and container[key] != planned for key in ("parsed", "valid_predictions", "valid_vectors")):
                        return False
                    if any(container.get(key, 0) != 0 for key in ("invalid", "missing", "invalid_or_missing", "invalid_or_missing_vectors")):
                        return False
            elif task == "P09":
                source_completion = load(task_root / "P08/runtime/benchmark/completion.json") or {}
                source_lock = task_root / "P08/runtime/benchmark/prediction_lock.json"
                metrics = candidate.get("metrics", {})
                if not source_lock.is_file() or hashlib.sha256(source_lock.read_bytes()).hexdigest() != candidate.get("prediction_lock_sha256"):
                    return False
                if source_completion.get("prediction_lock_sha256") != candidate.get("prediction_lock_sha256") or source_completion.get("all_passed") is not True:
                    return False
                if candidate.get("prediction_source_config_sha256") != source_completion.get("config_sha256"):
                    return False
                if metrics.get("planned") != source_completion.get("planned") or metrics.get("valid_predictions") != metrics.get("planned") or metrics.get("invalid_or_missing") != 0:
                    return False
            return True

        score_path = next((p for p in score_candidates if consistent_score(p)), None)
        if score_path:
            score = load(score_path)
            row.update(category="done", substatus="defined_score", status="Scored complete declared condition.", next_action="Preserve sealed predictions and score; reconcile/publicly publish this tracker and report metadata.")
            row["score"] = {k: score.get(k) for k in ("run_id", "protocol_variant", "scored_at_pacific", "planned", "spearman", "metrics", "all_case_primary_available", "prediction_lock_sha256", "interpretation") if k in score}
            row["evidence_paths"].append(relative(score_path))
            row["evidence_paths"].append(relative(metadata / "runtime/benchmark/prediction_lock.json") if completion else ".local/catalog_execution_2026-10-20/tasks/P08/runtime/benchmark/prediction_lock.json")
            score_run = score.get("run_id")
            public_score = root / "results/runs" / str(score_run) / "scores.json"
            public_matching_rows = [r for r in table_rows if r["task_id"] == task and r.get("run_id") == score_run and r.get("source_scores") and (root / r["source_scores"]).is_file()]
            row["public_evidence_path"] = public_matching_rows[0]["source_scores"] if public_matching_rows else (relative(public_score) if public_score.is_file() else "reports/CATALOG_STATUS.json")
            if task == "P09":
                row["exact_native_condition_availability"] = "Original NatureLM binary conversion/test labels unavailable in inspected author releases. Completed declared >1.0 rule-derived adaptation reuses sealed P08 predictions."
                row["scope_notes"].append("53.28768189245972% accuracy (6848/12851); no extra model generation; not native NatureLM label certification.")
        elif task == "V06" and (v06 := v06_execution_evidence(root, now)):
            row.update(v06)
            row["exact_native_condition_availability"] = "All 193 released cases; declared local-Qwen judging and lossless outer-JSON-fence extraction retain the released mean per-case score-ratio formula. The original GPT-4-0314 judge is not reproduced."
        elif task in historic_done:
            originals = [r for r in table_rows if r["task_id"] == task and r.get("source_row_category") == "completed_rows"]
            row.update(category="done", substatus="retained_declared_score", status="Defined retained score for the declared evaluated condition.", next_action="Preserve existing scores and qualifications; no new generation is pending for this setting.")
            row["score"] = [{k: r.get(k) for k in ("run_id", "dataset", "protocol_variant", "score_display", "case_scope", "source_scores", "source_score_sha256")} for r in originals]
            row["evidence_paths"].append("reports/EVALUATION_DECISION_TABLE.json")
            row["evidence_paths"].extend(r["source_scores"] for r in originals if r.get("source_scores"))
            row["scope_notes"] = sorted({r.get("case_scope", "Declared evaluated scope") for r in originals})
            if task in {"P01", "V01", "V02", "V03", "V04", "V05"}:
                row["scope_notes"].append("Retained metrics exist; missing historical raw archives limit further recovery/diagnostics, not the existence of the retained score.")
            if task == "B08":
                row["scope_notes"].append("Separate uniform-16K 33-case proposal remains proposed/not dispatched; it is not an active remaining queue.")
        elif task in {"P07", "P08"} and completion:
            row.update(category="agent_work", substatus="offline_scoring_repair", status="Complete new generation sealed; defined score still needs an offline scoring repair.", next_action="Complete once-only offline scoring against the sealed prediction lock, preserving failed attempt evidence; no regeneration.")
            row["exact_native_condition_availability"] = "Released full test and native correlation formula available; new nonthinking constrained-scalar condition is separate from historical generation."
        elif task in {"P12", "P13", "P14", "P15"}:
            selected = task_queue_evidence(root, task, direct, now)
            grant, started, finished = (selected[key] for key in ("grant", "started", "finished"))
            row["evidence_paths"].extend(selected["evidence_paths"])
            if selected["continuation"]:
                row["scope_notes"].append(f"Current verified successor job {selected['job_id']}; predecessor drain exits remain historical operational evidence.")
                if row["runtime"] is not None:
                    row["runtime"]["active_job_id"] = selected["job_id"]
            row["exact_native_condition_availability"] = "Released test and native AP/Fmax scorer available; dense confidence-vector delivery is a separately frozen new condition."
            progress_fresh = direct and age_seconds(timestamp(direct), now) is not None and age_seconds(timestamp(direct), now) <= 600
            pool_client_active = selected["active_client"] if selected["continuation"] else pool_fresh and f"10_{task}_benchmark" in pool.get("active_clients", [])
            if direct and not completion and started.exists() and not finished.exists() and (progress_fresh or pool_client_active):
                row.update(category="running", substatus="generation_live_evidence", status="Direct generation progress and frozen started grant; recent progress or fresh pool active-client evidence confirms activity.", next_action="Continue the existing one-attempt cohort, seal every outcome, then run native offline scoring after closure.")
                row["evidence_paths"].append(relative(started))
                if pool_client_active and not selected["continuation"]:
                    row["evidence_paths"].append(relative(pool_path))
            elif grant.exists() and not started.exists():
                row.update(category="queued", substatus="frozen_grant_not_started", status="Frozen authorized runtime grant queued; no started record or progress observed.", next_action="Existing runtime starts this grant when a client slot opens; no new permission required.")
                row["evidence_paths"].append(relative(grant))
                row["scope_notes"].append("No progress is not proof of zero requests. This queue classification uses the frozen grant and absence of a started record, not filename response counts.")
            else:
                row.update(category="agent_work", substatus="runtime_observation_or_scoring_needed", status="Runtime evidence needs reconciliation; do not infer current running state from the old controller.", next_action="Inspect direct runner/process and seal evidence; resume only the existing authorized one-attempt queue or score a completed seal.")
        elif task in AGENT_ACTIONS:
            action, source, availability = AGENT_ACTIONS[task]
            row.update(category="agent_work", substatus="implementation_review_preparation", status="Doable preparation/implementation remains unfinished; not in the live generation queue.", next_action=action, exact_native_condition_availability=availability)
            row["evidence_paths"].append(source)
            row["scope_notes"].append("Already authorized agent work; an internal exact frozen grant is an engineering gate, not another broad user permission request.")
            if task == "P35":
                row["scope_notes"].append("Rankings can be produced. A new aggregate correctness metric would require a separate source-grounded research decision; qualitative evidence is not scored accuracy.")
            if task == "V07":
                row["evidence_paths"].append(".local/catalog_execution_2026-10-20/tasks/V07/materialization_resume_20261020_v1/completion.json")
        elif task in USER_HOLDS:
            row.update(category="user_held", substatus="explicit_exception_held", status="User explicitly left this exception on hold.", next_action=USER_HOLDS[task], decision_needed=USER_HOLDS[task])
            row["exact_native_condition_availability"] = "Required training/judge exception remains held; source or solver preparation does not itself complete the score."
            row["evidence_paths"] = ["AGENTS.md", f".local/catalog_execution_2026-10-20/tasks/{task}/task.json"]
        elif task in PROVIDER_HOLDS:
            row.update(category="provider_held", substatus="no_retry_or_reroute", status="Biological/provider restriction or interrupted review remains held.", next_action="Preserve completed evidence and holds; do not retry, rephrase or reroute the interrupted/flagged action. Continue only separate permitted offline metadata/scoring work.", decision_needed="Requires resolution of the applicable provider/scope restriction; a simple user continuation instruction does not remove it.")
            row["exact_native_condition_availability"] = "Source availability is separate from this execution/review hold; no claim that the whole source corpus is prohibited or missing."
            row["evidence_paths"] = ["AGENTS.md", f".local/catalog_execution_2026-10-20/tasks/{task}/task.json"]
            status = metadata / "status.json"
            if status.exists():
                row["evidence_paths"].append(relative(status))
            if task == "P36":
                row["scope_notes"].append("Only historical 59-response partial evidence is generated. Extension preserved 188 prepared inputs, with 5604 unreviewed; later interruption overrides the older continue-from-index-256 checkpoint instruction.")
                row["evidence_paths"].append(".local/catalog_execution_2026-10-20/tasks/P36/review_summary_v2.json")
        else:
            raise AssertionError(f"Unclassified retained setting: {task}")

        row.update(explain_unfinished(row, reasons))
        if task in reasons and row["category"] != "done" and not row.get("separate_local_execution_verified"):
            row["evidence_paths"].append(BLOCKERS_PATH)
            row["evidence_paths"].extend(reasons[task].get("source_paths", []))
            row["next_action"] = row["next_deliverable"]
        row["evidence_paths"] = list(dict.fromkeys(row["evidence_paths"]))
        for item in row["evidence_paths"]:
            evidence(item)
        primary = evidence_records[row["evidence_paths"][0]]
        row["evidence_recorded_at_pacific"] = primary["recorded_at_pacific"]
        if row["runtime"]:
            row["evidence_recorded_at_pacific"] = row["runtime"]["recorded_at_pacific"]
        if row["evidence_recorded_at_pacific"] is None:
            row["scope_notes"].append("Primary source has no embedded timestamp; this read verifies availability, not a fresh execution heartbeat.")
        if not row.get("public_evidence_path"):
            row["public_evidence_path"] = next((item for item in row["evidence_paths"] if not item.startswith(".local/") and evidence_records[item]["available"]), "reports/CATALOG_STATUS.json")
        rows.append(row)

    counts = {key: sum(row["category"] == key for row in rows) for key in CATEGORIES}
    assert sum(counts.values()) == len(rows) == 57
    assert {row["task_id"] for row in rows} == set(retained)
    assert all(row["category"] in CATEGORIES and row["next_action"] and row["evidence_paths"] for row in rows)
    controller = load(root / ".local/catalog_execution_2026-10-20/control/status.json")
    controller_time = timestamp(controller)
    supervisor_path = root / ".local/catalog_execution_2026-10-20/control/driver_supervisor_status.json"
    supervisor = load(supervisor_path) or {}
    supervisor_age = age_seconds(timestamp(supervisor), now)
    active_jobs = sorted({row["runtime"]["active_job_id"] for row in rows
                          if row["task_id"] in DEEPFRI_OUTPUT_DIMENSIONS and row.get("runtime") and row["runtime"].get("active_job_id")})
    if active_jobs:
        pool_path = root / ".local/catalog_execution_2026-10-20/continuation_v1/runtime/status.json"
        pool = load(pool_path) or {}
        pool_age = age_seconds(timestamp(pool), now)
        pool_fresh = pool_age is not None and -60 <= pool_age <= 180 and pool.get("stage") == "serving_task_queue"
    health_path = root / "reports/CATALOG_RUNTIME_IO_2026-10-20.json"
    operational_health = load(health_path)
    current_health = load(root / "reports/CATALOG_RUNTIME_HEALTH_2026-10-20.json")
    for new_health_path in sorted((root / ".local/catalog_execution_2026-10-20/continuation_v1/runtime").glob("health_*.json")):
        fresh_health = load(new_health_path)
        if fresh_health and (timestamp(fresh_health) or "") > (timestamp(current_health) or ""):
            current_health = {**fresh_health, "source_path": str(new_health_path.relative_to(root)),
                "model_id_verified": fresh_health.get("served_model_ids") == ["Qwen/Qwen3.8-27B"],
                "gpu_health_known": bool(fresh_health.get("gpu_health_known", False)),
                "gpu_health_note": fresh_health.get("gpu_observation_note", "Endpoint GET success does not establish current GPU hardware health.")}
    result = {
        "schema_version": 1,
        "generated_at_pacific": now.isoformat(),
        "timezone": "America/Los_Angeles",
        "role": "exhaustive_57_setting_evidence_tracker_not_dispatch_authorization",
        "retained_setting_count": 57,
        "counts": counts,
        "category_definitions": CATEGORIES,
        "agent_work_breakdown": dict(Counter(row["substatus"] for row in rows if row["category"] == "agent_work")),
        "full_catalog_complete": counts["done"] == 57,
        "definitions": {
            "done": "At least one retained defined score for that setting's declared evaluated condition; does not mean every published case, native paper replication, high performance, or rationale validity.",
            "queued": "An exact frozen generation grant exists and no started record/progress is observed; an assignment in a planning registry is not an execution queue.",
            "agent_work": "The next listed step can be advanced under existing authority. It can include review and a later exclusion; it is not a promise that every case is eligible or all native artifacts exist.",
            "impossible": "Requires evidence that the whole setting cannot be pursued; missing exact native artifacts alone do not make a labelled available adaptation impossible.",
            "counts": "Each retained setting appears once. Development panels, OpenAI comparison conditions, archived BioReason settings and the historical 17145-case continuation are not additional settings.",
            "runtime": "Direct progress/completion contents are used; unsealed counts are lower bounds. Missing progress is unknown, not zero calls. No response filename counts used.",
        },
        "freshness": {
            "old_decision_table_generated_at_pacific": table.get("generated_at_pacific"),
            "controller_recorded_at_pacific": controller_time,
            "controller_age_seconds": age_seconds(controller_time, now),
            "controller_is_live_evidence_only_if_recent": age_seconds(controller_time, now) is not None and age_seconds(controller_time, now) <= 180,
            "pool_recorded_at_pacific": timestamp(pool),
            "pool_source_path": str(pool_path.relative_to(root)),
            "active_successor_job_ids": active_jobs,
            "pool_is_fresh": pool_fresh,
            "pool_active_clients": pool.get("active_clients"),
            "supervisor_recorded_at_pacific": timestamp(supervisor),
            "supervisor_is_fresh": supervisor_age is not None and supervisor_age <= 180,
            "supervisor_stage": supervisor.get("stage"),
            "supervised_controller_pid": supervisor.get("child_pid"),
            "controller_repair_note": "Original controller exited with Errno 116 (stale file handle). Root restarted the existing exact controller under supervision at about 12:31 PM PDT; old aggregate status may remain stale while the supervised controller rechecks seals.",
            "note": "This tracker reads direct task evidence and does not promote the old controller or planning registry to live execution.",
        },
        "rows": rows,
        "operational_health_observation": operational_health,
        "current_runtime_health_observation": current_health,
        "unfinished_reason_source": BLOCKERS_PATH if blocker_document else None,
        "evidence": list(evidence_records.values()),
        "validation": {"exactly_57_rows": True, "no_duplicate_setting_ids": True, "exact_retained_id_set": True, "categories_mutually_exclusive": True, "counts_sum_to_57": True},
    }
    return result


def markdown(data):
    def esc(value):
        return str(value).replace("|", "\\|").replace("\n", " ")

    lines = ["# Full retained catalog status", "", f"Observed **{data['generated_at_pacific']}** (America/Los_Angeles). Exactly **57 settings**, one row each.", "", "Done means a defined score for the declared evaluated condition. It does not imply matched-paper replication, complete original-paper scope, or good performance. Saved responses alone do not count as done.", "", "[Qwen/GPT results and exact remaining-work checklists](RESULTS_AND_REMAINING_WORK.md).", "", "| Status | Count |", "|---|---:|"]
    for key, label in CATEGORIES.items():
        lines.append(f"| {label} | {data['counts'][key]} |")
    breakdown = data["agent_work_breakdown"]
    if breakdown:
        lines += ["", "Unfinished agent work includes " + ", ".join(f"{value} {key.replace('_', ' ')}" for key, value in breakdown.items()) + ". These tasks are not all in a live generation queue."]
    health = data.get("operational_health_observation")
    current_health = data.get("current_runtime_health_observation")
    if current_health and current_health.get("health_http_status") == 200 and current_health.get("models_http_status") == 200:
        gpu_note = "Current GPU hardware health is not established by these HTTP checks." if current_health.get("gpu_health_known") is False else "The recorded single A100 observation was busy."
        lines += ["", f"**Latest read-only health check ({current_health['observed_at_pacific']}):** both endpoint GETs returned HTTP 200. {gpu_note} These are point-in-time observations; the JSON tracker retains the source path and date."]
    elif health:
        lines += ["", f"**Dated runtime health observation ({health['observed_at_pacific']}):** HTTP model/health checks timed out while multiple DFS readers and the server stalled in filesystem I/O. GPU activity did not establish healthy HTTP delivery. [Observation details](CATALOG_RUNTIME_IO_2026-10-20.json); current health requires a fresh check."]
    if data["freshness"].get("active_successor_job_ids"):
        lines += ["", "Current successor runtime job: " + ", ".join(data["freshness"]["active_successor_job_ids"]) + ". Old predecessor drain exits remain historical evidence."]
    if not data["freshness"]["controller_is_live_evidence_only_if_recent"]:
        lines += ["", f"**Stale aggregate metadata:** the old controller record is from {data['freshness']['controller_recorded_at_pacific']}. Direct per-task progress/completion/score evidence below takes precedence."]
    if data["freshness"]["supervisor_is_fresh"]:
        lines += ["", f"The existing controller was restarted under supervision around **12:31 PM PDT** after an `Errno 116` stale-file-handle crash. Its supervisor is fresh at {data['freshness']['supervisor_recorded_at_pacific']}; pool heartbeat fresh: **{data['freshness']['pool_is_fresh']}**. This does not create a new protocol or extra inference scope."]
    preparation_count = sum(row["category"] == "agent_work" and row["substatus"] == "implementation_review_preparation" for row in data["rows"])
    lines += ["", "New head training remains user-held. The user removed the BioReason-Pro judging hold and waived LLaVA-Med's original GPT-4-0314 requirement; declared available judging conditions are agent work. Biological/provider holds are separate. Exact native unavailability is tracked separately from whether an available adaptation can proceed.", "", "## Why the unfinished settings are unfinished", "", f"The {preparation_count} preparation/implementation settings need work we have not completed. Source acquisition and synthetic tests did not make those evaluations runnable or scored. Existing instructions cover the listed permissible preparation and labelled adaptations.", "", "| Setting | Concrete reason unfinished | Who owns the missing step | Next concrete deliverable |", "|---|---|---|---|"]
    for row in data["rows"]:
        if row["category"] != "done":
            lines.append("| " + " | ".join(esc(value) for value in (row["task_id"] + " " + row["task_name"], row["why_not_done"], row["blocker_owner"], row["next_deliverable"])) + " |")
    lines += ["", "Several original paper evaluations lack required released artifacts. An available qualitative demonstration or proxy can be prepared, but it cannot supply an invented native accuracy or reproduce an unreleased paper cohort. See the per-setting qualifications below.", "", "## Every retained setting", "", "| ID | Setting | Status | Saved/planned | Next action / decision | Evidence |", "|---|---|---|---:|---|---|"]
    for row in data["rows"]:
        runtime = row["runtime"]
        saved = f"{runtime['responses_saved']:,}/{runtime['planned']:,}" if runtime and isinstance(runtime.get("responses_saved"), int) and isinstance(runtime.get("planned"), int) else (f"Unknown/{row['prepared_benchmark_planned']:,}" if row.get("prepared_benchmark_planned") else "—")
        evidence = row["public_evidence_path"]
        label = SHORT_LABELS[row["category"]]
        if row["substatus"] == "offline_scoring_repair":
            label = "Unfinished agent work: scoring repair"
        lines.append(f"| {row['task_id']} | {esc(row['task_name'])} | {esc(label)} | {saved} | {esc(row['next_action'])} | [{esc(Path(evidence).name)}](../{evidence}) |")
    lines += ["", "## Native-condition and scope qualifications", "", "| ID | Availability / material qualification |", "|---|---|"]
    for row in data["rows"]:
        if row["category"] != "done" or row["task_id"] in {"P09", "B08"}:
            extra = " ".join(row["scope_notes"])
            lines.append(f"| {row['task_id']} | {esc(row['exact_native_condition_availability'] + ' ' + extra)} |")
    lines += ["", "The [JSON tracker](CATALOG_STATUS.json) includes per-setting source times, hashes, all evidence paths, runtime errors and score metadata. Historical metrics and their separate conditions remain in [the decision table](EVALUATION_DECISION_TABLE.md).", "", "Regenerate with `python3 scripts/build_catalog_status.py`. This performs metadata reads and report writes only; it makes no inference calls or dispatch changes.", ""]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root.resolve()
    data = build(root)
    report = root / "reports/CATALOG_STATUS.json"
    report.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    (root / "reports/CATALOG_STATUS.md").write_text(markdown(data))
    print(json.dumps({"generated_at_pacific": data["generated_at_pacific"], "counts": data["counts"], "validation": data["validation"]}))


if __name__ == "__main__":
    main()
