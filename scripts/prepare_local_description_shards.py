"""Prepare disabled, input-reviewed description jobs; no inference or approval."""
import argparse
from collections import Counter
import datetime as dt
import json
from pathlib import Path

from prepare_catalog_descriptions import TASKS, REVISION, VARIANT, TEMPLATE_FILE, TEMPLATE_SHA256
from prepare_local_extended_shards import REPLICAS, SHARD_SIZE, RUNNER, digest, file_digest, ordered_union, partition, write_new
from score_local_descriptions import METRIC_PATH, METRIC_SHA256

ROOT = Path(__file__).resolve().parents[1]
SCORER = "scripts/score_local_descriptions.py"
PLAN_FILE = "reports/local_description_shard_plan.json"
APPROVAL_FILE = "configs/local_description_execution_approval.json"
SCRIPTS = [RUNNER, SCORER, "scripts/prepare_catalog_descriptions.py", "scripts/prepare_local_extended_shards.py",
           "scripts/aggregate_local_extended_shards.py", "scripts/prepare_local_description_shards.py",
           "scripts/execute_local_description_shard.py", "scripts/aggregate_local_description_shards.py"]
METRIC_CAVEAT = "Native Mol-Instructions gold-only HF ROUGE; pinned BioT5+ wrapper computes references_new but passes [gold,decoded_input] pairs to ROUGE, so exact BioT5+ paper metric equivalence remains unresolved."


def execution_cases(rows, task, template, expected_count=None):
    if not rows or (expected_count is not None and len(rows) != expected_count):
        raise ValueError("Wrong complete task test count")
    cases, ids, source_ids = [], set(), set()
    for index, row in enumerate(rows):
        if (row["task"] != task or row["source_index"] != index or row["system"] != ""
                or row["variant"] != VARIANT or row["split"] != "official_BioT5_export_task_test"
                or row["case_id"] != TASKS[task]["filename"] + ":" + str(index)
                or row["case_id"] in ids or row["source_instance_id"] in source_ids
                or set(row["fields"]) != {"instruction", "sequence"}):
            raise ValueError("Source task/order/identity/input field contract changed")
        ids.add(row["case_id"]); source_ids.add(row["source_instance_id"])
        instruction, sequence = row["fields"]["instruction"], row["fields"]["sequence"]
        if (not isinstance(instruction, str) or not instruction.strip() or not sequence
                or any(not ("A" <= char <= "Z") for char in sequence)):
            raise ValueError("Missing exact instruction or complete sequence")
        prompt = template["prompt_input"].format(instruction=instruction, input=sequence)
        import hashlib
        if row["prompt"] != prompt or row["prompt_sha256"] != hashlib.sha256(prompt.encode()).hexdigest():
            raise ValueError("Native instruction/template/full-sequence prompt changed")
        cases.append({**{key: row[key] for key in ("task", "case_id", "variant", "split")},
                      "messages": [{"role": "user", "content": prompt}]})
    return cases


def approval_for(config_path, settings, approval_path=None):
    """Separate exact-plan approval keeps the prospective frozen configs unchanged."""
    if settings.get("execution_authorized") is not False or settings.get("input_review_complete") is not True:
        raise ValueError("Require input-reviewed prospective config, not self-authorization")
    plan_path = ROOT / settings["shard_plan_file"]
    plan = json.loads(plan_path.read_text())
    approval_path = approval_path or ROOT / APPROVAL_FILE
    approval = json.loads(approval_path.read_text())
    relative = str(config_path.resolve().relative_to(ROOT.resolve()))
    matching = [item for task in plan["tasks"] for item in task["shards"] if item["config_file"] == relative]
    if (approval.get("execution_authorized") is not True or approval.get("plan_sha256") != file_digest(plan_path)
            or approval.get("model") != settings["model"] or approval.get("model_revision") != settings["model_revision"]
            or approval.get("generation_sha256") != digest(settings["generation"])
            or not set(settings["approved_task_ids"]) <= set(approval.get("approved_task_ids", []))
            or len(matching) != 1 or matching[0]["config_sha256"] != file_digest(config_path)
            or approval.get("approved_config_sha256", {}).get(relative) != file_digest(config_path)):
        raise ValueError("No exact-plan/model/generation/config execution approval")
    return {"approval_file": str(approval_path.resolve().relative_to(ROOT.resolve())),
            "approval_sha256": file_digest(approval_path), "plan_sha256": file_digest(plan_path)}


def prepare():
    if (ROOT / PLAN_FILE).exists():
        raise ValueError("Description plan already frozen")
    template_path = ROOT / TEMPLATE_FILE
    if file_digest(template_path) != TEMPLATE_SHA256 or file_digest(ROOT / METRIC_PATH) != METRIC_SHA256:
        raise ValueError("Pinned template or actual HF ROUGE implementation changed")
    template = json.loads(template_path.read_text())
    timestamp = dt.datetime.now(dt.timezone.utc).isoformat()
    base_path = ROOT / "configs/local_labbench_b07.json"
    base = json.loads(base_path.read_text())
    if base["generation"]["max_tokens"] != 4096:
        raise ValueError("Only the existing4096-token recipe is prepared")
    hashes = {name: file_digest(ROOT / name) for name in SCRIPTS + [TEMPLATE_FILE, METRIC_PATH,
              "sources/mol__evaluation__protein__eval.py", "sources/biot5__biot5_plus__metrics__pro_understand_metrics__pro_understand_metrics.py",
              "configs/local_labbench_b07.json"]}
    entries, assignment = [], 0
    for task in sorted(TASKS):
        spec = TASKS[task]
        folder = f"data/catalog_descriptions/{task}"
        preparation = json.loads((ROOT / folder / "preparation.json").read_text())
        for name in ("model_inputs.jsonl", "native_serialized_inputs.jsonl", "scorer_references.jsonl"):
            if file_digest(ROOT / folder / name) != preparation["files"][name]["sha256"]:
                raise ValueError("Stable prepared artifact changed: " + task + "/" + name)
        source_artifacts = {preparation["source_file"]: spec["sha256"], preparation["test_list_file"]: spec["split_sha256"]}
        for name, expected in source_artifacts.items():
            if file_digest(ROOT / name) != expected:
                raise ValueError("Native release/test-list source changed")
        source_name = folder + "/model_inputs.jsonl"
        rows = [json.loads(line) for line in (ROOT / source_name).read_text().splitlines() if line]
        cases = execution_cases(rows, task, template, spec["count"])
        native = [json.loads(line) for line in (ROOT / folder / "native_serialized_inputs.jsonl").read_text().splitlines() if line]
        if len(native) != len(rows):
            raise ValueError("Native serialization row count mismatch")
        for model, original in zip(rows, native):
            serialized = "<bop>" + "".join("<p>" + aa for aa in model["fields"]["sequence"]) + "<eop>"
            if (original["case_id"] != model["case_id"] or original["instruction"] != model["fields"]["instruction"]
                    or original["native_serialized_input"] != serialized):
                raise ValueError("Complete original sequence/instruction roundtrip changed")
        counts = Counter(row["fields"]["instruction"] for row in rows)
        groups = partition(cases)
        prefix = f"data/local_description_shards/{task}"
        full_input = prefix + "/full/model_inputs.jsonl"
        full_review = f"configs/local_description_{task.lower()}_review.json"
        aggregate_name = f"configs/local_description_{task.lower()}_aggregate.json"
        write_new(ROOT / full_input, cases, True)
        review = {"task_id": task, "input_review_only": True, "input_review_complete": True,
                  "execution_authorized": False, "reviewed_at_utc": timestamp,
                  "source_input_path": source_name, "source_input_sha256": file_digest(ROOT / source_name),
                  "basis": "Every supplied input checked for exact native instance instruction, source order/ID, original Alpaca template and complete decoded sequence; all unique instruction templates reviewed for annotation-description goals. Labels/outcomes excluded from input and partition selection.",
                  "scope": "Sequence-to-annotation descriptions: function/localization/process, catalytic reaction annotation, domains/motifs or general properties. No sequence generation, optimization, operational experimental protocol, or pathogen-fitness objective supplied.",
                  "input_allowlist": ["native_per_instance_instruction", "complete_amino_acid_sequence"],
                  "native_unique_instruction_count": len(counts), "instruction_counts_sha256": digest(dict(counts)),
                  "approved_case_ids": [case["case_id"] for case in cases], "held_cases": [],
                  "approved_cases": len(cases), "full_public_cases": len(cases), "selection_based_on_model_outputs": False,
                  "classification_is_provisional": True, "explanation_support_score": None,
                  "metric_interpretation": "Annotation word overlap is not explanation correctness or independent biological factuality validation."}
        write_new(ROOT / full_review, review)
        settings = {**base, "run_id": f"qwen38_27b_{task.lower()}_description_full_parallel_2026-10-15",
                    "frozen_at_utc": timestamp, "approved_task_ids": [task], "variant": VARIANT,
                    "input_file": full_input, "review_file": full_review, "runner": RUNNER,
                    "reviewed": True, "input_review_complete": True, "execution_authorized": False,
                    "execution_approval_file": APPROVAL_FILE, "shard_plan_file": PLAN_FILE,
                    "source_dataset_revision": REVISION, "source_artifacts_sha256": source_artifacts,
                    "scorer_reference_file": folder + "/scorer_references.jsonl",
                    "scorer_reference_sha256": preparation["files"]["scorer_references.jsonl"]["sha256"],
                    "model_facing_fields": ["instruction", "sequence"], "input_modalities": ["amino_acid_sequence", "text"],
                    "prompt_policy": "Exact source per-instance instruction and pinned Alpaca template; complete native sequence decoded from BioT5 amino-acid tokens, no512-token encoder truncation; fixed zero-shot Qwen adaptation.",
                    "metric_policy": "Gold-only native Mol-Instructions HF ROUGE defaults, all four metrics; official BootstrapAggregator mid.fmeasure, seed42, no stemming. Full-test metric computed once globally from all raw final content.",
                    "paper_comparison": METRIC_CAVEAT, "explanation_support_score": None,
                    "full_test_case_count": len(cases), "shard_count": len(groups), "shard_size": SHARD_SIZE,
                    "aggregate_only": True, "generator_execution_allowed": False,
                    "endpoint": "aggregate-only://offline", "case_scope": "aggregate_only_full_test"}
        for name in ("source_code_revision", "gpu_ids", "serving_config_file", "server_record_file"):
            settings.pop(name, None)
        frozen = {**hashes, **{name: file_digest(ROOT / name) for name in
                   (source_name, folder + "/native_serialized_inputs.jsonl", folder + "/preparation.json", full_input, full_review, preparation["test_list_file"])}}
        settings["frozen_files_sha256"] = frozen
        shards = []
        for index, group in enumerate(groups):
            gpu, port = REPLICAS[assignment % len(REPLICAS)]
            shard_input = prefix + f"/shard_{index:03d}/model_inputs.jsonl"
            shard_review = f"configs/local_description_{task.lower()}_shard_{index:03d}_review.json"
            shard_name = f"configs/local_description_{task.lower()}_shard_{index:03d}.json"
            start, stop = index * SHARD_SIZE, min((index + 1) * SHARD_SIZE, len(cases))
            write_new(ROOT / shard_input, group, True)
            write_new(ROOT / shard_review, {**review, "approved_case_ids": [case["case_id"] for case in group],
                      "approved_cases": len(group), "case_scope": "task_shard_only", "shard_index": index,
                      "source_start_index": start, "source_stop_index": stop,
                      "whole_task_review_file": full_review, "whole_task_review_sha256": file_digest(ROOT / full_review)})
            shard = {**settings, "run_id": settings["run_id"] + f"_shard_{index:03d}",
                     "aggregate_only": False, "generator_execution_allowed": True,
                     "input_file": shard_input, "review_file": shard_review, "case_scope": "task_shard_only",
                     "gpu_ids": [gpu], "endpoint": f"http://127.0.0.1:{port}/v1",
                     "serving_config_file": f"configs/local_model_gpu{gpu}.json" if gpu != 5 else "configs/local_model.json",
                     "server_record_file": f".local/local_model_server_gpu{gpu}.json" if gpu != 5 else ".local/local_model_server.json",
                     "shard_index": index, "source_start_index": start, "source_stop_index": stop,
                     "aggregate_config_file": aggregate_name, "full_input_file": full_input,
                     "full_input_sha256": file_digest(ROOT / full_input), "full_review_file": full_review,
                     "full_review_sha256": file_digest(ROOT / full_review), "assignment_index": assignment}
            assignment += 1
            shard["frozen_files_sha256"] = {**frozen, shard_input: file_digest(ROOT / shard_input), shard_review: file_digest(ROOT / shard_review)}
            write_new(ROOT / shard_name, shard)
            shards.append({"config_file": shard_name, "config_sha256": file_digest(ROOT / shard_name), "run_id": shard["run_id"],
                           "shard_index": index, "cases": len(group), "gpu_ids": [gpu], "endpoint": shard["endpoint"]})
        settings["shard_configs"] = shards
        settings["full_test_id_union_validation"] = ordered_union(cases, groups)
        write_new(ROOT / aggregate_name, settings)
        entries.append({"task_id": task, "aggregate_config_file": aggregate_name,
                        "aggregate_config_sha256": file_digest(ROOT / aggregate_name), "aggregate_run_id": settings["run_id"],
                        "full_test_case_count": len(cases), "shard_count": len(groups), "shards": shards})
    plan = {"frozen_at_utc": timestamp, "execution_authorized": False, "input_review_complete": True,
            "shard_size": SHARD_SIZE, "partition_policy": "Consecutive original source-order1024-row slices, all IDs once; no label/output-based selection.",
            "replica_order": [{"gpu_ids": [gpu], "port": port} for gpu, port in REPLICAS],
            "source_recipe_file": "configs/local_labbench_b07.json", "source_recipe_sha256": file_digest(base_path),
            "model": base["model"], "model_revision": base["model_revision"], "generation": base["generation"], "concurrency": base["concurrency"],
            "tasks": entries, "inference_dispatched": False, "authorizations_or_queues_modified": False,
            "metric_policy": METRIC_CAVEAT, "global_metric_policy": "Run native gold-only ROUGE exactly once over the complete ordered union for each task; no averaging of shard bootstrap scores."}
    write_new(ROOT / PLAN_FILE, plan)
    print(json.dumps({"plan": PLAN_FILE, "sha256": file_digest(ROOT / PLAN_FILE), "cases": sum(e["full_test_case_count"] for e in entries),
                      "shards": sum(e["shard_count"] for e in entries), "execution_authorized": False}))
    return plan


if __name__ == "__main__":
    argparse.ArgumentParser(description=__doc__).parse_args()
    prepare()
