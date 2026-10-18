#!/usr/bin/env python3
"""Offline, hash-locked scoring for prepared N01/N02/N03 local runs.

Primary accuracy/F1 reproduce the verified source predicates on a qualified
reconstruction of the saved generated continuation. STRICT_FINAL_LABEL is a
fixed, separately named diagnostic. This file never submits inference, changes
inputs/configuration, imports a provider client, or validates mechanisms.
"""
from __future__ import annotations

import argparse
from collections import Counter
import csv
import hashlib
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
TASKS = {"N01", "N02", "N03"}
SOURCE_REVISION = "684ff7c09eb1d65e70925c114a7a05a1fcc0403f"
PUNCTUATION = ".,!?\"'"
PROTOCOL = {
    "version": 1,
    "native_source_revision": SOURCE_REVISION,
    "primary_metrics": "N01 accuracy; N02/N03 accuracy and pathogenic-positive f1. Never replace with a better-looking diagnostic.",
    "native_N01": "Continuation only; extract text after the last case-sensitive literal Answer:, strip/lower, remove . , ! ? double/single quotes from prediction and gold, then test gold substring membership.",
    "native_N02_N03": "Continuation only, including generated reasoning: normalized source gold class as a case-insensitive substring anywhere. Source TP/FN for pathogenic; TN/FP for benign according to whether its own gold substring occurs.",
    "continuation_reconstruction": "Saved message.reasoning (or unambiguous legacy reasoning_content), one newline separator if nonempty, then exact saved message.content. Never append the prompt, reference, a generated Answer: marker or an inferred class.",
    "prompt_exclusion": "BioReason DNALLMModel.generate passes inputs_embeds without input_ids to decoder-only HF generate; the supported Transformers path initializes returned token IDs with length zero. Its vLLM implementation returns out.outputs[0].text. Both are generated continuation paths, not prompt+continuation.",
    "decoder_qualification": "Source dependencies are unpinned; local chat archives lack original generated token IDs and parser-removed boundary markers. Source rules are reproduced on saved fields, not asserted byte-identical to author decoding. Reasoning-parser identity/raw-boundary equivalence remains qualified.",
    "STRICT_FINAL_LABEL": "Use message.content only. Take suffix after last case-insensitive Answer: marker when present. Remove source punctuation, collapse whitespace, match exactly one fixed vocabulary label. For VEP only, permit a semicolon disease suffix; reject both benign/pathogenic word labels anywhere in final content. No synonyms, gold-assisted extraction, reasoning fallback or model judge.",
    "N01_supplemental_macro": "STRICT_FINAL_LABEL only: unweighted mean over all 37 frozen global source classes, including zero-support classes, zero_division=0. Invalid/missing predictions are a separate sentinel: incorrect for accuracy and false-negative for their gold class. Not an exact reconstruction of the unavailable paper macro scorer.",
    "planned_denominator": "Every frozen planned case remains in accuracy denominator. Missing/failed outputs are incorrect; no filtering, fabricated label, retry or completion selection. F1 uses declared confusion counts; no valid-only subset.",
    "source_reference_fields": {"N01": ["task", "case_id", "source_answer", "normalized_label", "scorer_only"],
                                "N02": ["task", "case_id", "source_answer", "normalized_label", "scorer_only"],
                                "N03": ["task", "case_id", "source_answer", "normalized_label", "scorer_only"]},
    "source_response_fields": ["task", "case_id", "variant", "model", "model_revision", "request_sha256", "status", "text", "response.model", "response.choices[0].message.content", "response.choices[0].message.reasoning", "finish_reason"],
}


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def file_digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")
    temporary.chmod(0o600)
    temporary.replace(path)


def normalize_label(task, answer):
    if not isinstance(answer, str):
        raise ValueError("Source answer must be a string")
    if task == "N03":
        answer = answer.replace("[", "").replace("]", "").replace("'", "").replace("_", " ").strip()
    return (answer if task == "N01" else answer.split(";")[0]).strip().lower()


def source_clean(text):
    text = text.strip().lower()
    for char in PUNCTUATION:
        text = text.replace(char, "")
    return text


def native_n01_answer(text):
    # Deliberately preserve the source's case-sensitive marker and permissive
    # substring predicate. No strict diagnostic replaces this primary rule.
    return source_clean(text.split("Answer:")[-1]) if "Answer:" in text else ""


def strict_label(task, final_text, vocabulary):
    if final_text is None:
        return None
    if task != "N01" and len(set(re.findall(r"\b(?:benign|pathogenic)\b", final_text.lower()))) > 1:
        return None
    markers = list(re.finditer(r"answer\s*:", final_text, re.I))
    candidate = final_text[markers[-1].end():] if markers else final_text
    if task != "N01":
        candidate = candidate.split(";")[0]
    normalized = " ".join(source_clean(candidate).split())
    normalized_vocabulary = {" ".join(source_clean(label).split()): label for label in vocabulary}
    if len(normalized_vocabulary) != len(vocabulary):
        raise ValueError("Fixed vocabulary has colliding strict normalization")
    return normalized_vocabulary.get(normalized)


def continuation_fields(record):
    """Use actual saved response fields only; never inspect the prompt/gold."""
    response = record.get("response", {})
    choices = response.get("choices", [])
    if len(choices) != 1 or not isinstance(choices[0].get("message"), dict):
        raise ValueError("Completed archive must contain exactly one original message")
    message = choices[0]["message"]
    if message.get("role") != "assistant" or message.get("tool_calls") or message.get("function_call"):
        raise ValueError("Unexpected response role/tool modality")
    final = message.get("content")
    if final is None:
        final = ""
    if not isinstance(final, str) or record.get("text") != final:
        raise ValueError("Saved final text differs from the original response content")
    reasoning_values = [message[key] for key in ("reasoning", "reasoning_content") if message.get(key) is not None]
    if any(not isinstance(value, str) for value in reasoning_values) or len(set(reasoning_values)) > 1:
        raise ValueError("Ambiguous or non-string archived reasoning fields")
    reasoning = reasoning_values[0] if reasoning_values else ""
    continuation = reasoning + ("\n" if reasoning else "") + final
    return continuation, final, {"reasoning_field_present": bool(reasoning_values),
                                 "reasoning_characters": len(reasoning), "final_characters": len(final),
                                 "continuation_sha256": hashlib.sha256(continuation.encode()).hexdigest(),
                                 "final_sha256": hashlib.sha256(final.encode()).hexdigest()}


def _f1(tp, fp, fn):
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    return {"precision": precision, "recall": recall,
            "f1": 2 * precision * recall / (precision + recall) if precision + recall else 0.0}


def outcome_metrics(task, labels, continuations, finals, vocabulary):
    """All planned slots; source-native primary and strict diagnostic separate."""
    if task not in TASKS or not labels or not (len(labels) == len(continuations) == len(finals)):
        raise ValueError("Require matching nonempty planned slots for one supported task")
    if any(label not in vocabulary for label in labels):
        raise ValueError("Reference outside frozen global source vocabulary")
    parsed = [strict_label(task, text, vocabulary) for text in finals]
    native_answers = [native_n01_answer(text) if task == "N01" and text is not None else (text.lower() if text is not None else "") for text in continuations]
    native_correct = [(source_clean(label) if task == "N01" else label) in text for label, text in zip(labels, native_answers)]
    metrics = {"accuracy": sum(native_correct) / len(labels)}
    strict = {"accuracy": sum(pred == label for pred, label in zip(parsed, labels)) / len(labels)}
    details = {"planned": len(labels), "native_correct": sum(native_correct), "strict_correct": sum(pred == label for pred, label in zip(parsed, labels)),
               "strict_parsed": sum(pred is not None for pred in parsed),
               "strict_invalid_completed": sum(final is not None and pred is None for final, pred in zip(finals, parsed)),
               "missing_or_failed": sum(text is None for text in finals)}
    vocab_native = [source_clean(label) if task == "N01" else label for label in vocabulary]
    native_mentions = [sum(label in text for label in vocab_native) for text in native_answers]
    details.update(native_invalid_completed=sum(text is not None and mentions == 0 for text, mentions in zip(continuations, native_mentions)),
                   native_ambiguous_completed=sum(text is not None and mentions > 1 for text, mentions in zip(continuations, native_mentions)))
    if task != "N01":
        if vocabulary != ["benign", "pathogenic"]:
            raise ValueError("VEP requires fixed benign/pathogenic source vocabulary")
        native_tp = sum(label == "pathogenic" and correct for label, correct in zip(labels, native_correct))
        native_fn = sum(label == "pathogenic" and not correct for label, correct in zip(labels, native_correct))
        native_tn = sum(label == "benign" and correct for label, correct in zip(labels, native_correct))
        native_fp = sum(label == "benign" and not correct for label, correct in zip(labels, native_correct))
        metrics["f1"] = _f1(native_tp, native_fp, native_fn)["f1"]
        details["native_confusion_counts"] = {"tp": native_tp, "fp": native_fp, "tn": native_tn, "fn": native_fn}
        tp = sum(label == pred == "pathogenic" for label, pred in zip(labels, parsed))
        fp = sum(label != "pathogenic" and pred == "pathogenic" for label, pred in zip(labels, parsed))
        fn = sum(label == "pathogenic" and pred != "pathogenic" for label, pred in zip(labels, parsed))
        strict["f1"] = _f1(tp, fp, fn)["f1"]
        details["strict_confusion_counts"] = {"tp": tp, "fp": fp, "fn": fn, "invalid_sentinel_is_not_an_imputed_class": True}
    else:
        per_class = []
        for label in vocabulary:
            tp = sum(gold == pred == label for gold, pred in zip(labels, parsed))
            fp = sum(gold != label and pred == label for gold, pred in zip(labels, parsed))
            fn = sum(gold == label and pred != label for gold, pred in zip(labels, parsed))
            per_class.append(_f1(tp, fp, fn))
        for metric in ("f1", "precision", "recall"):
            strict["supplemental_macro_" + metric + "_fixed_global_vocabulary"] = sum(row[metric] for row in per_class) / len(vocabulary)
    metrics["STRICT_FINAL_LABEL"] = strict
    return metrics, details, parsed, native_correct


def expected_payload(case, settings):
    if set(case) != {"task", "case_id", "variant", "split", "messages"}:
        raise ValueError("Unexpected frozen case fields")
    if case["task"] not in settings["approved_task_ids"] or case["variant"] != settings["variant"]:
        raise ValueError("Case differs from frozen task/variant")
    if len(case["messages"]) != 1 or set(case["messages"][0]) != {"role", "content"}:
        raise ValueError("Require the reviewed single-user source interface")
    if case["messages"][0]["role"] != "user" or not isinstance(case["messages"][0]["content"], str):
        raise ValueError("Unexpected input modality")
    if settings["generation"].get("n") != 1 or settings.get("tool_access", []) or "tools" in settings:
        raise ValueError("Require one frozen completion without tools")
    return {"model": settings["model"], "messages": case["messages"], **settings["generation"]}


def find_config(root, manifest, config_path=None):
    expected = manifest["configuration_sha256"]
    candidates = [Path(config_path)] if config_path is not None else sorted((root / "configs").glob("*.json"))
    for path in candidates:
        if not path.is_absolute():
            path = root / path
        if path.exists() and file_digest(path) == expected:
            if json.loads(path.read_text()) != manifest["configuration"]:
                raise ValueError("Frozen config content differs from manifest")
            return path
    raise ValueError("No original frozen config matches run_manifest configuration_sha256")


def output_lock(root, folder, cases, config_path, settings):
    files = {"run_manifest.json": file_digest(folder / "run_manifest.json"),
             "frozen_config": file_digest(config_path), "scoring_protocol": digest(PROTOCOL)}
    expected_names = set()
    for case in cases:
        identity = digest([case["task"], case["variant"], case["case_id"]]) + ".json"
        expected_names.add(identity)
        for category in ("requests", "responses"):
            name = category + "/" + identity
            path = folder / name
            files[name] = file_digest(path) if path.exists() else None
    for category in ("requests", "responses"):
        if {p.name for p in (folder / category).glob("*.json")} - expected_names:
            raise ValueError("Unexpected alternate case/completion archive")
    for key in ("input_file", "review_file", "class_vocabulary_file", "scorer_reference_file"):
        files["frozen_source/" + key] = file_digest(root / settings[key])
    record = {"files_sha256": files, "contract_sha256": digest(files),
              "policy": "Requests, raw response fields, missing slots and protocol locked before labels; no output selection, repair or retry."}
    path = folder / "scoring_output_lock.json"
    if path.exists() and json.loads(path.read_text()) != record:
        raise ValueError("Pre-scoring output lock changed")
    if not path.exists():
        write_json(path, record)
    return record


def read_locked_json(path, expected):
    path = Path(path)
    if expected is None:
        if path.exists():
            raise ValueError("A locked missing slot was later populated")
        return None
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != expected:
        raise ValueError("Archive changed after output locking")
    return json.loads(raw)


def load_references(path, expected_sha256):
    raw = Path(path).read_bytes()
    if hashlib.sha256(raw).hexdigest() != expected_sha256:
        raise ValueError("Scorer references changed after output locking")
    references = {}
    for ref in map(json.loads, raw.decode().splitlines()):
        key = (ref["task"], ref["case_id"])
        if key in references:
            raise ValueError("Duplicate scorer reference identity")
        if ref.get("scorer_only") is not True or normalize_label(ref["task"], ref["source_answer"]) != ref["normalized_label"]:
            raise ValueError("Reference differs from fixed source normalization")
        references[key] = ref
    return references


def score(folder, root=ROOT, config_path=None):
    root, folder = Path(root).resolve(), Path(folder).resolve()
    manifest = json.loads((folder / "run_manifest.json").read_text())
    settings = manifest["configuration"]
    approved = settings["approved_task_ids"]
    if len(approved) != 1 or approved[0] not in TASKS or not settings.get("model") or not settings.get("model_revision"):
        raise ValueError("Require one supported task and an exact pinned model/revision")
    task = approved[0]
    config_path = find_config(root, manifest, config_path)
    frozen = settings["frozen_files_sha256"]
    required = {"scripts/score_local_genomics.py", settings["input_file"], settings["review_file"], settings["class_vocabulary_file"]}
    if not required <= set(frozen):
        raise ValueError("Scorer, inputs, review and global vocabulary must be frozen before inference")
    for name, expected in frozen.items():
        if file_digest(root / name) != expected:
            raise ValueError("Frozen file changed: " + name)
    if frozen["scripts/score_local_genomics.py"] != file_digest(Path(__file__)):
        raise ValueError("Running scorer differs from its frozen implementation")
    if manifest.get("runner_sha256") != frozen.get(settings.get("runner")):
        raise ValueError("Manifest runner differs from its frozen checksum")
    for snapshot in (manifest.get("server", {}), manifest.get("serving_configuration", {})):
        if snapshot and (snapshot.get("model") != settings["model"] or snapshot.get("revision") != settings["model_revision"]):
            raise ValueError("Serving snapshot differs from pinned model/revision")
    cases = [json.loads(line) for line in (root / settings["input_file"]).read_text().splitlines() if line]
    if not cases or digest(cases) != manifest["case_contract_sha256"] or manifest.get("planned_cases") != len(cases):
        raise ValueError("Frozen planned input contract changed")
    review = json.loads((root / settings["review_file"]).read_text())
    ids = [case["case_id"] for case in cases]
    if ids != review["approved_case_ids"] or len(ids) != len(set(ids)) or set(ids) & {row["case_id"] for row in review.get("held_cases", [])}:
        raise ValueError("Execution set differs from exact ordered reviewed IDs")
    if review.get("input_review_only") is not True:
        raise ValueError("Require an input-only pre-inference case review")
    if file_digest(root / settings["scorer_reference_file"]) != settings["scorer_reference_sha256"]:
        raise ValueError("Scorer reference checksum changed")
    lock = output_lock(root, folder, cases, config_path, settings)
    states, finishes, usage = Counter(), Counter(), Counter()
    outputs, requests, reconstructions = [], 0, Counter()
    for case in cases:
        identity = digest([case["task"], case["variant"], case["case_id"]])
        request_path, response_path = folder / "requests" / (identity + ".json"), folder / "responses" / (identity + ".json")
        request = read_locked_json(request_path, lock["files_sha256"]["requests/" + identity + ".json"])
        response = read_locked_json(response_path, lock["files_sha256"]["responses/" + identity + ".json"])
        payload = expected_payload(case, settings)
        requests += int(request is not None)
        if request is not None:
            if digest(request["payload"]) != request.get("request_sha256") or digest(payload) != request["request_sha256"]:
                raise ValueError("Archived request differs from frozen payload")
            if any(request.get(key) != case[key] for key in ("task", "case_id", "variant", "split")):
                raise ValueError("Request identity differs from frozen case")
        if response is not None:
            if request is None:
                raise ValueError("Response has no archived request")
            for key, value in {"task": task, "case_id": case["case_id"], "variant": settings["variant"], "split": case["split"],
                               "model": settings["model"], "model_revision": settings["model_revision"], "request_sha256": request["request_sha256"]}.items():
                if response.get(key) != value:
                    raise ValueError("Response provenance mismatch: " + key)
        status = response.get("status") if response else ("interrupted_unknown_completion" if request else "not_dispatched")
        states[status] += 1
        continuation = final = None
        field_metadata = None
        if status == "completed":
            if response.get("http_status") != 200 or response.get("response", {}).get("model") != settings["model"]:
                raise ValueError("Completed response identity/status mismatch")
            continuation, final, field_metadata = continuation_fields(response)
            reconstructions["reasoning_field_present" if field_metadata["reasoning_field_present"] else "no_reasoning_field"] += 1
            finishes[str(response.get("finish_reason"))] += 1
            for key in ("prompt_tokens", "completion_tokens", "total_tokens"):
                usage[key] += response.get("response", {}).get("usage", {}).get(key, 0) or 0
        outputs.append({"case": case, "status": status, "continuation": continuation, "final": final, "field_metadata": field_metadata,
                        "request_sha256": request["request_sha256"] if request else None})
    # No references, teacher rationales or case labels are opened before the
    # original raw outputs have been locked and all payload/model checks pass.
    vocabulary_doc = read_locked_json(root / settings["class_vocabulary_file"], lock["files_sha256"]["frozen_source/class_vocabulary_file"])
    vocabulary = vocabulary_doc["classes"]
    if len(set(vocabulary)) != len(vocabulary) or len(vocabulary) != (37 if task == "N01" else 2):
        raise ValueError("Wrong fixed global source vocabulary")
    if task != "N01" and vocabulary != ["benign", "pathogenic"]:
        raise ValueError("Changed binary source class vocabulary")
    references = load_references(root / settings["scorer_reference_file"], lock["files_sha256"]["frozen_source/scorer_reference_file"])
    labels = [references[(task, case["case_id"])]["normalized_label"] for case in cases]
    metrics, counts, parsed, correct = outcome_metrics(task, labels, [o["continuation"] for o in outputs], [o["final"] for o in outputs], vocabulary)
    completed = states["completed"]
    unattempted = {"not_dispatched", "not_dispatched_after_error", "interrupted_unknown_completion"}
    finished = sum(count for status, count in states.items() if status not in unattempted)
    summary = {"run_id": settings["run_id"], "task_id": task, "model": settings["model"], "model_revision": settings["model_revision"],
               "protocol_variant": settings["variant"], "checkpoint_precision": settings.get("checkpoint_precision"),
               "planned": len(cases), "finished": finished, "requests_saved": requests, "completed": completed,
               "parsed": counts["strict_parsed"], "invalid_outputs": counts["strict_invalid_completed"],
               "missing_or_failed_outputs": counts["missing_or_failed"], "statuses": dict(states), "finish_reasons": dict(finishes), "token_usage": dict(usage),
               "metrics": metrics, "metric_counts": counts, "metric_protocol": PROTOCOL,
               "primary_metric_names": ["accuracy"] if task == "N01" else ["accuracy", "f1"],
               "primary_metric_status": "source_rule_on_protocol_qualified_saved_continuation",
               "strict_diagnostic_namespace": "STRICT_FINAL_LABEL", "native_decode_byte_equivalence_claimed": False,
               "continuation_field_counts": dict(reconstructions), "input_modalities": ["DNA_sequence_text", "text"],
               "case_scope": settings.get("case_scope", "full_frozen_reviewed_case_set" if completed == len(cases) else "INCOMPLETE_frozen_reviewed_case_set"),
               "held_before_inference": len(review.get("held_cases", [])), "class_vocabulary_sha256": file_digest(root / settings["class_vocabulary_file"]),
               "class_vocabulary_size": len(vocabulary), "source_dataset_revision": settings.get("source_dataset_revision"), "source_code_revision": SOURCE_REVISION,
               "scorer_sha256": file_digest(Path(__file__)), "scoring_protocol_sha256": digest(PROTOCOL), "configuration_sha256": manifest["configuration_sha256"],
               "scoring_output_lock_sha256": lock["contract_sha256"], "predictions_locked_before_reference_read": True,
               "request_response_hash_audit": "passed", "explanation_support_score": None,
               "comparison_to_paper": "Source outcome predicates retained with explicit decoded-continuation qualification. Full released DNA windows, zero-shot prompted local Qwen, source SFT/encoder systems and author decoder settings differ. N01 macro metrics are supplemental strict-label diagnostics, not verified native paper reproduction.",
               "interpretation": {"good_score_establishes": "Agreement under the explicitly declared source predicate and fixed local inference protocol; native substring scores can credit class mentions in generated reasoning or ambiguous outputs.",
                                  "bad_score_establishes": "Limited outcome recovery under this input/training/scoring regime; not an isolated test of general reasoning.",
                                  "explanation_correctness": "Unassessed. Neither a correct outcome nor a gold-label mention validates a mechanism; unsupported explanations are not automatically false."},
               "contamination": "Reference answers/teacher rationales excluded from requests; raw outputs locked before labels; no training, gold-assisted extraction, scorer selection or test-guided changes. Prior public-benchmark exposure unknown."}
    for key in ("shard_count", "shard_index", "shard_id", "parent_run_id", "source_shard_run_ids", "aggregated_from_shards", "full_test_id_union_validation"):
        if key in settings:
            summary[key] = settings[key]
    scored = [{"task": task, "case_id": case["case_id"], "status": output["status"], "target": label,
               "native_source_correct": native, "STRICT_FINAL_LABEL_prediction": pred,
               "STRICT_FINAL_LABEL_correct": pred == label, "saved_field_metadata": output["field_metadata"], "request_sha256": output["request_sha256"]}
              for case, output, label, pred, native in zip(cases, outputs, labels, parsed, correct)]
    write_json(folder / "scores.json", summary)
    write_json(folder / "per_case_scores.json", scored)
    with (folder / "metrics.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["run_id", "task_id", "protocol_variant", "model", "metric", "value", "planned", "completed", "parsed", "case_scope"])
        writer.writeheader()
        for name, value in metrics.items():
            rows = [(name + "." + key, item) for key, item in value.items()] if isinstance(value, dict) else [(name, value)]
            for metric, item in rows:
                writer.writerow({**{key: summary[key] for key in ("run_id", "task_id", "protocol_variant", "model", "planned", "completed", "parsed", "case_scope")}, "metric": metric, "value": item})
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run")
    parser.add_argument("--config", type=Path)
    parser.add_argument("--describe-protocol", action="store_true")
    args = parser.parse_args()
    if args.describe_protocol:
        print(json.dumps({"scorer_sha256": file_digest(Path(__file__)), "scoring_protocol_sha256": digest(PROTOCOL), "protocol": PROTOCOL}, ensure_ascii=False))
        return
    if not args.run:
        parser.error("--run is required unless --describe-protocol is selected")
    summary = score(ROOT / "results/runs" / args.run, config_path=args.config)
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == "__main__":
    main()
