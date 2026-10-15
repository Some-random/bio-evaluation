"""Offline gold-only native Mol-Instructions ROUGE for a frozen Qwen run.

Uses the hash-pinned official HuggingFace metric function, without evaluate's
network/cache framework. No model judge, reference-based repair or tuning.
"""
import argparse
import ast
from collections import Counter
import csv
import functools
import hashlib
import importlib.metadata
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
METRIC_PATH = "sources/catalog_descriptions__hf__rouge_pinned.py"
METRIC_SHA256 = "805b71b855be6dc270ce2366639a4e264c2a1fb93a2c8a50f9fb9ef5a2b9c21a"
ROUGE_TYPES = ["rouge1", "rouge2", "rougeL", "rougeLsum"]
TASKS = {"P23", "P24", "P25", "P26"}
BOOTSTRAP_SEED = 42


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def file_digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path, value):
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")
    temporary.chmod(0o600)
    temporary.replace(path)


@functools.lru_cache(maxsize=1)
def official_metric_function():
    from rouge_score import rouge_scorer, scoring
    if importlib.metadata.version("rouge-score") != "0.1.2":
        raise ValueError("Expected pinned rouge-score0.1.2 implementation")
    path = ROOT / METRIC_PATH
    if file_digest(path) != METRIC_SHA256:
        raise ValueError("Official HF ROUGE source changed")
    tree = ast.parse(path.read_text())
    klass = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == "Rouge")
    method = next(n for n in klass.body if isinstance(n, ast.FunctionDef) and n.name == "_compute")
    # Execute the original method verbatim. This avoids importing evaluate's
    # download framework while retaining its exact scorer/aggregator behavior.
    module = ast.Module(body=[method], type_ignores=[])
    namespace = {"rouge_scorer": rouge_scorer, "scoring": scoring}
    exec(compile(ast.fix_missing_locations(module), str(path), "exec"), namespace)
    return namespace["_compute"]


def lexical_metrics(predictions, references):
    import numpy as np
    if not predictions or len(predictions) != len(references):
        raise ValueError("Require one output/reference per scored case")
    if any(not isinstance(t, str) for t in predictions + references):
        raise ValueError("Native gold-only protocol requires flat reference strings")
    # HF Evaluate's framework applies an RNG context to metric computation.
    # Fix that previously unspecified source RNG before outputs, and disclose it.
    random_state = np.random.get_state()
    try:
        np.random.seed(BOOTSTRAP_SEED)
        result = official_metric_function()(None, predictions, references,
                    rouge_types=None, use_aggregator=True, use_stemmer=False, tokenizer=None)
    finally:
        np.random.set_state(random_state)
    return {key: float(value) for key, value in result.items()}


def per_case_metrics(prediction, reference):
    from rouge_score import rouge_scorer
    scorer = rouge_scorer.RougeScorer(ROUGE_TYPES, use_stemmer=False)
    result = scorer.score(reference, prediction)
    return {name: {"precision": value.precision, "recall": value.recall, "fmeasure": value.fmeasure}
            for name, value in result.items()}


def expected_payload(case, settings):
    if set(case) != {"task", "case_id", "variant", "split", "messages"}:
        raise ValueError("Unexpected input fields")
    if case["task"] not in settings["approved_task_ids"] or case["variant"] != settings["variant"]:
        raise ValueError("Case outside frozen task/variant")
    if len(case["messages"]) != 1 or set(case["messages"][0]) != {"role", "content"}:
        raise ValueError("Require one source prompt user message")
    if case["messages"][0]["role"] != "user" or not isinstance(case["messages"][0]["content"], str):
        raise ValueError("Unexpected input modality")
    return {"model": settings["model"], "messages": case["messages"], **settings["generation"]}


def lock_outputs(folder, cases):
    files = {"run_manifest.json": file_digest(folder / "run_manifest.json")}
    for case in cases:
        identity = digest([case["task"], case["variant"], case["case_id"]])
        for category in ["requests", "responses"]:
            name = category + "/" + identity + ".json"
            path = folder / name
            files[name] = file_digest(path) if path.exists() else None
    record = {"files_sha256": files, "contract_sha256": digest(files),
              "policy": "All raw outputs and missing slots locked before opening gold references; no output selection, cleanup, reference repair or tuning."}
    path = folder / "scoring_output_lock.json"
    if path.exists() and json.loads(path.read_text()) != record:
        raise ValueError("Pre-scoring output lock changed")
    if not path.exists():
        write_json(path, record)
    return record


def score(folder):
    manifest = json.loads((folder / "run_manifest.json").read_text())
    settings = manifest["configuration"]
    if len(settings["approved_task_ids"]) != 1 or settings["approved_task_ids"][0] not in TASKS:
        raise ValueError("Require one supported frozen description task")
    task = settings["approved_task_ids"][0]
    for name, expected in settings["frozen_files_sha256"].items():
        if file_digest(ROOT / name) != expected:
            raise ValueError("Frozen source changed: " + name)
    cases = [json.loads(s) for s in (ROOT / settings["input_file"]).read_text().splitlines() if s]
    if not cases or digest(cases) != manifest["case_contract_sha256"]:
        raise ValueError("Input contract changed")
    review = json.loads((ROOT / settings["review_file"]).read_text())
    ids = [c["case_id"] for c in cases]
    if ids != review["approved_case_ids"] or len(set(ids)) != len(ids):
        raise ValueError("Cases differ from exact ordered review")
    if set(ids) & {r["case_id"] for r in review.get("held_cases", [])}:
        raise ValueError("Held case found")
    lock = lock_outputs(folder, cases)
    # Verify the actual lexical code before opening the scorer labels.
    official_metric_function()
    reference_path = ROOT / settings["scorer_reference_file"]
    if file_digest(reference_path) != settings["scorer_reference_sha256"]:
        raise ValueError("Scorer reference differs from pre-inference hash")
    references = {}
    for ref in map(json.loads, reference_path.read_text().splitlines()):
        key = (ref["task"], ref["case_id"])
        if key in references:
            raise ValueError("Duplicate reference identity")
        references[key] = ref
    states, finishes, usage = Counter(), Counter(), Counter()
    scored, request_count = [], 0
    for case in cases:
        identity = digest([case["task"], case["variant"], case["case_id"]])
        req_path = folder / "requests" / (identity + ".json")
        res_path = folder / "responses" / (identity + ".json")
        payload = expected_payload(case, settings)
        request = json.loads(req_path.read_text()) if req_path.exists() else None
        response = json.loads(res_path.read_text()) if res_path.exists() else None
        request_count += int(request is not None)
        if request is not None and (digest(request["payload"]) != request["request_sha256"] or request["request_sha256"] != digest(payload)):
            raise ValueError("Request differs from frozen payload")
        if response is not None:
            if request is None:
                raise ValueError("Response missing request")
            for key, expected in [("task", task), ("case_id", case["case_id"]), ("variant", settings["variant"]),
                                  ("model", settings["model"]), ("model_revision", settings["model_revision"]),
                                  ("request_sha256", request["request_sha256"])]:
                if response.get(key) != expected:
                    raise ValueError("Response provenance mismatch: " + key)
        status = response.get("status") if response else ("interrupted_unknown_completion" if request else "not_dispatched")
        states[status] += 1
        completed = status == "completed"
        text = response.get("text", "") if completed else None
        if completed and not isinstance(text, str):
            raise ValueError("Completed description must be raw text")
        target = references[(task, case["case_id"])]["target"]
        if completed:
            finishes[str(response.get("finish_reason"))] += 1
            for name in ["prompt_tokens", "completion_tokens", "total_tokens"]:
                usage[name] += response.get("response", {}).get("usage", {}).get(name, 0) or 0
        scored.append({"task": task, "case_id": case["case_id"], "status": status, "completed": completed,
                       "raw_text": text, "target": target, "empty_output": completed and not text.strip(),
                       "lexical_metrics": per_case_metrics(text, target) if completed else None,
                       "finish_reason": response.get("finish_reason") if response else None,
                       "request_sha256": request["request_sha256"] if request else None})
    completed_rows = [r for r in scored if r["completed"]]
    result = lexical_metrics([r["raw_text"] for r in completed_rows], [r["target"] for r in completed_rows]) if completed_rows else None
    complete = len(completed_rows) == len(cases)
    metrics = {name: result[name] if complete else None for name in ROUGE_TYPES}
    if not complete:
        metrics.update({name + "_completed_only": result[name] if result else None for name in ROUGE_TYPES})
    scope = "full_frozen_reviewed_BioT5_export_test" if complete else "INCOMPLETE_completed_cases_only_not_full_test"
    summary = {"run_id": settings["run_id"], "task_id": task, "model": settings["model"], "model_revision": settings["model_revision"],
               "protocol_variant": settings["variant"], "planned": len(cases), "requests_saved": request_count,
               "completed": len(completed_rows), "parsed": len(completed_rows), "invalid_outputs": 0,
               "empty_outputs": sum(r["empty_output"] for r in scored), "missing_or_failed_outputs": len(cases) - len(completed_rows),
               "statuses": dict(states), "finish_reasons": dict(finishes), "token_usage": dict(usage), "metrics": metrics,
               "input_modalities": ["amino_acid_sequence", "text"], "case_scope": scope,
               "held_before_inference": len(review.get("held_cases", [])), "scoring_output_lock_sha256": lock["contract_sha256"],
               "lexical_metric_contract": {"source": METRIC_PATH, "source_sha256": METRIC_SHA256, "reference_policy": "flat gold target only; no input-as-reference",
                  "use_stemmer": False, "tokenization": "rouge-score0.1.2 DefaultTokenizer: lowercase, replace non-ASCII-alphanumeric spans with spaces, split whitespace, keep valid ASCII-alphanumeric tokens; no stemming",
                  "rouge_types": ROUGE_TYPES, "aggregation": "Official HF function with Google BootstrapAggregator defaults:1000 resamples,95% intervals, median(mid).fmeasure",
                  "bootstrap_rng_seed": BOOTSTRAP_SEED, "output_processing": "Raw returned final content, no answer-guided trimming or reference-based repair",
                  "packages": {p: importlib.metadata.version(p) for p in ["rouge-score", "numpy", "nltk"]}},
               "comparison_to_paper": "Native Mol-Instructions gold-only ROUGE scorer algorithm on pinned BioT5+ task-defined test exports; full-sequence zero-shot Qwen is an explicit architecture/context/training adaptation. Pinned BioT5+ scorer passes [gold,decoded_input] pairs despite computing gold-only references_new: exact BioT5+ paper metric equivalence unresolved.",
               "explanation_support_score": None,
               "interpretation": {"likely_demands": {"labels": ["biological_annotation_prediction", "sequence_representation", "description_generation"], "status": "provisional analyst description, not internal-computation inference"},
                  "actually_supplied": "Exact archived native per-instance instruction and official Alpaca template, with complete raw amino-acid sequence substituted for BioT5 special tokens. No gold descriptions, reference explanations or tools.",
                  "reference_answer_source": "Pinned native task output descriptions, independently hashed before inference and scorer-only",
                  "good_score_establishes": "Lexical agreement with source reference annotations under this declared full-sequence zero-shot baseline",
                  "bad_score_establishes": "Limited lexical recovery; paraphrase differences, annotation incompleteness and biological prediction may all contribute",
                  "explanation_correctness": "ROUGE is not a factuality/mechanism rubric. Correct labels do not certify explanations; unsupported claims are not automatically false."},
               "contamination": "No gold references sent, inputs frozen, outputs hash-locked before scoring, no judges/retrieval/training or test-feedback changes. Public pretraining exposure unknown."}
    write_json(folder / "scores.json", summary)
    write_json(folder / "per_case_scores.json", scored)
    with (folder / "metrics.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["run_id", "task_id", "protocol_variant", "model", "metric", "value", "planned", "completed", "parsed", "case_scope"])
        writer.writeheader()
        for name, value in metrics.items():
            writer.writerow({"run_id": settings["run_id"], "task_id": task, "protocol_variant": settings["variant"], "model": settings["model"],
                             "metric": name, "value": value, "planned": len(cases), "completed": len(completed_rows), "parsed": len(completed_rows), "case_scope": scope})
    print(json.dumps(summary, ensure_ascii=False))
    return summary


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", required=True)
    args = parser.parse_args()
    score(ROOT / "results/runs" / args.run)
