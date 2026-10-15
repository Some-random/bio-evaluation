"""Freeze disabled complete Reaction execution proposal, with six fixed shards."""
import argparse
import datetime as dt
import json
from pathlib import Path

from prepare_catalog_reaction import ROOT, OBJECTIVE, VARIANT, TEST_COUNT, CLASS_COUNT, sha256, canonical_digest
from prepare_local_extended_shards import REPLICAS, SHARD_SIZE, RUNNER, file_digest, write_new

SCORER = "scripts/score_local_reaction.py"
PLAN_FILE = "reports/local_reaction_shard_plan.json"
APPROVAL_FILE = "configs/local_reaction_execution_approval.json"
SCRIPTS = [RUNNER, SCORER, "scripts/prepare_catalog_reaction.py", "scripts/prepare_local_extended_shards.py",
           "scripts/prepare_local_reaction_shards.py", "scripts/execute_local_reaction_shard.py",
           "scripts/aggregate_local_reaction_shards.py"]


def approval_for(config_path, settings):
    if settings.get("execution_authorized") is not False or settings.get("input_review_complete") is not True:
        raise ValueError("Require input-reviewed prospective config, not self-authorization")
    plan_path = ROOT / settings["shard_plan_file"]
    approval_path = ROOT / settings["execution_approval_file"]
    plan, approval = json.loads(plan_path.read_text()), json.loads(approval_path.read_text())
    relative = str(config_path.resolve().relative_to(ROOT.resolve()))
    entries = [entry for task in plan["tasks"] for entry in task["shards"] if entry["config_file"] == relative]
    if (approval.get("execution_authorized") is not True or approval.get("plan_sha256") != file_digest(plan_path)
            or approval.get("model") != settings["model"] or approval.get("model_revision") != settings["model_revision"]
            or approval.get("generation_sha256") != canonical_digest(settings["generation"])
            or not set(settings["approved_task_ids"]) <= set(approval.get("approved_task_ids", []))
            or len(entries) != 1 or entries[0]["config_sha256"] != file_digest(config_path)
            or approval.get("approved_config_sha256", {}).get(relative) != file_digest(config_path)):
        raise ValueError("No exact-plan/model/generation/config execution approval")
    return {"approval_file": str(approval_path.relative_to(ROOT)), "approval_sha256": file_digest(approval_path),
            "plan_sha256": file_digest(plan_path)}


def prepare():
    if (ROOT / PLAN_FILE).exists():
        raise ValueError("Reaction execution proposal already frozen")
    timestamp = dt.datetime.now(dt.timezone.utc).isoformat()
    source_folder = ROOT / "data/catalog_reaction/P16"
    source_preparation = json.loads((source_folder / "preparation.json").read_text())
    for name, metadata in source_preparation["files"].items():
        if file_digest(source_folder / name) != metadata["sha256"]:
            raise ValueError("Prepared source changed: " + name)
    context_validation = json.loads((ROOT / "reports/catalog_reaction_context_validation.json").read_text())
    if (context_validation["fits_without_any_input_truncation"] is not True
            or context_validation["model_context_limit"] != 262144 or context_validation["frozen_output_tokens"] != 4096):
        raise ValueError("Complete fixed context was not verified")
    context = (source_folder / "class_context.txt").read_text()
    common_prefix = OBJECTIVE + "\n\nOriginal fixed class descriptions:\n" + context + "\n\nComplete protein sequence:\n"
    base = json.loads((ROOT / "configs/local_labbench_b07.json").read_text())
    if base["generation"]["max_tokens"] != 4096:
        raise ValueError("Only unchanged4096-token generation is proposed")
    prefix = "data/local_reaction_shards/P16"
    full_input = prefix + "/full/model_inputs.jsonl"
    full_review = "configs/local_reaction_p16_review.json"
    aggregate_name = "configs/local_reaction_p16_aggregate.json"
    total_shards = (TEST_COUNT + SHARD_SIZE - 1) // SHARD_SIZE
    input_paths = [prefix + f"/shard_{i:03d}/model_inputs.jsonl" for i in range(total_shards)]
    handles = []
    for name in [full_input] + input_paths:
        path = ROOT / name
        if path.exists():
            raise ValueError("Refuse to overwrite frozen input")
        path.parent.mkdir(parents=True, exist_ok=True)
        handles.append(path.open("w"))
        path.chmod(0o600)
    ids = []
    try:
        with (source_folder / "model_inputs.jsonl").open() as source:
            for index, line in enumerate(source):
                row = json.loads(line)
                if (row["task"] != "P16" or row["case_id"] != "Reaction:test:" + str(index)
                        or row["source_index"] != index or row["variant"] != VARIANT or row["system"]
                        or row["prompt"] != common_prefix + row["fields"]["sequence"]
                        or row["prompt_sha256"] != sha256(row["prompt"].encode())
                        or row["class_context_sha256"] != sha256(context.encode())):
                    raise ValueError("Original source-order full prompt contract changed")
                case = {**{key: row[key] for key in ("task", "case_id", "variant", "split")},
                        "messages": [{"role": "user", "content": row["prompt"]}]}
                serialized = json.dumps(case, ensure_ascii=False) + "\n"
                handles[0].write(serialized); handles[1 + index // SHARD_SIZE].write(serialized)
                ids.append(row["case_id"])
    finally:
        for handle in handles:
            handle.close()
    if len(ids) != TEST_COUNT or len(set(ids)) != TEST_COUNT:
        raise ValueError("Wrong complete original test ID count")
    review = {"task_id": "P16", "input_review_only": True, "input_review_complete": True, "execution_authorized": False,
              "reviewed_at_utc": timestamp, "source_input_path": "data/catalog_reaction/P16/model_inputs.jsonl",
              "source_input_sha256": source_preparation["files"]["model_inputs.jsonl"]["sha256"],
              "basis": "Every original source-order row retains complete protein sequence, fixed384-class objective and every full original class description. Context precedes variable sequence for prefix reuse; construction fixed without predictions/labels used to select or shorten inputs.",
              "scope": "Native multiclass reaction annotation of an existing protein sequence. No sequence design/optimization, experimental protocols, pathogen-fitness prediction or transferred flagged requests.",
              "approved_case_ids": ids, "held_cases": [], "approved_cases": TEST_COUNT, "full_public_cases": TEST_COUNT,
              "selection_based_on_model_outputs": False, "classification_is_provisional": True,
              "provisional_task_demands": ["biological outcome/annotation prediction", "learned sequence representation", "mapping to fixed reaction descriptions"],
              "explanation_support_score": None}
    write_new(ROOT / full_review, review)
    settings = {**base, "run_id": "qwen38_27b_p16_full_descriptions_parallel_2026-10-15",
                "frozen_at_utc": timestamp, "approved_task_ids": ["P16"], "variant": VARIANT, "input_file": full_input,
                "review_file": full_review, "runner": RUNNER, "reviewed": True, "input_review_complete": True,
                "execution_authorized": False, "execution_approval_file": APPROVAL_FILE, "shard_plan_file": PLAN_FILE,
                "source_dataset_revision": source_preparation["source_revision"],
                "scorer_reference_file": "data/catalog_reaction/P16/scorer_references.jsonl",
                "scorer_reference_sha256": source_preparation["files"]["scorer_references.jsonl"]["sha256"],
                "model_facing_fields": ["complete_amino_acid_sequence", "fixed_task_objective", "all384_full_source_class_descriptions"],
                "input_modalities": ["amino_acid_sequence", "text"], "fixed_global_class_count": CLASS_COUNT,
                "prompt_policy": "Exact prepared objective, all384 complete original pretraining-template descriptions first, then the complete original source sequence. Fixed class order0..383, no class filtering, input truncation, prompt ensemble or test-feedback changes.",
                "metric_policy": "Native top1 multiclass accuracy across all5651test rows. Missing/invalid final class IDs count incorrect; no class remapping, retries or label-guided parsing.",
                "paper_comparison": "Closest native full-description comparator21.91% accuracy, ProtST Table11 printedp15 (rounded). Pretraining-name29.85% is a separate input variant. ProtST uses separately encoded128-token-truncated text/protein embeddings; Qwen receives complete descriptions jointly and the full raw sequence. Not matched architecture/context/training.",
                "explanation_support_score": None, "full_test_case_count": TEST_COUNT, "shard_count": total_shards,
                "shard_size": SHARD_SIZE, "aggregate_only": True, "generator_execution_allowed": False,
                "endpoint": "aggregate-only://offline", "case_scope": "aggregate_only_full_test",
                "source_artifacts_sha256": {source_preparation["source_archive"]: source_preparation["source_archive_sha256"]}}
    for key in ("source_code_revision", "gpu_ids", "serving_config_file", "server_record_file"):
        settings.pop(key, None)
    dependencies = SCRIPTS + [full_input, full_review, "data/catalog_reaction/P16/model_inputs.jsonl",
                  "data/catalog_reaction/P16/class_ontology.json", "data/catalog_reaction/P16/class_context.txt",
                  "data/catalog_reaction/P16/ordered_case_ids.json", "data/catalog_reaction/P16/preparation.json",
                  "reports/catalog_reaction_preparation.json", "reports/catalog_reaction_validation.json",
                  "reports/catalog_reaction_context_validation.json", "configs/local_labbench_b07.json"]
    dependencies += [record["path"] for record in source_preparation["native_code_provenance"]["records"]]
    frozen = {name: file_digest(ROOT / name) for name in dependencies}
    settings["frozen_files_sha256"] = frozen
    shards = []
    for index, input_name in enumerate(input_paths):
        start, stop = index * SHARD_SIZE, min((index + 1) * SHARD_SIZE, TEST_COUNT)
        gpu, port = REPLICAS[index % len(REPLICAS)]
        review_name = f"configs/local_reaction_p16_shard_{index:03d}_review.json"
        config_name = f"configs/local_reaction_p16_shard_{index:03d}.json"
        write_new(ROOT / review_name, {**review, "approved_case_ids": ids[start:stop], "approved_cases": stop - start,
                  "case_scope": "task_shard_only", "shard_index": index, "source_start_index": start,
                  "source_stop_index": stop, "whole_task_review_file": full_review, "whole_task_review_sha256": file_digest(ROOT / full_review)})
        shard = {**settings, "run_id": settings["run_id"] + f"_shard_{index:03d}", "aggregate_only": False,
                 "generator_execution_allowed": True, "input_file": input_name, "review_file": review_name,
                 "case_scope": "task_shard_only", "gpu_ids": [gpu], "endpoint": f"http://127.0.0.1:{port}/v1",
                 "serving_config_file": f"configs/local_model_gpu{gpu}.json" if gpu != 5 else "configs/local_model.json",
                 "server_record_file": f".local/local_model_server_gpu{gpu}.json" if gpu != 5 else ".local/local_model_server.json",
                 "shard_index": index, "assignment_index": index, "source_start_index": start, "source_stop_index": stop,
                 "aggregate_config_file": aggregate_name, "full_input_file": full_input, "full_input_sha256": file_digest(ROOT / full_input),
                 "full_review_file": full_review, "full_review_sha256": file_digest(ROOT / full_review)}
        shard["frozen_files_sha256"] = {**frozen, input_name: file_digest(ROOT / input_name), review_name: file_digest(ROOT / review_name)}
        write_new(ROOT / config_name, shard)
        shards.append({"config_file": config_name, "config_sha256": file_digest(ROOT / config_name), "run_id": shard["run_id"],
                       "shard_index": index, "cases": stop - start, "gpu_ids": [gpu], "endpoint": shard["endpoint"]})
    settings["shard_configs"] = shards
    settings["full_test_id_union_validation"] = {"complete": True, "union_matches_full_test_ids": True,
                 "expected_test_case_count": TEST_COUNT, "unique_observed_case_count": TEST_COUNT, "missing_case_count": 0, "extra_case_count": 0}
    write_new(ROOT / aggregate_name, settings)
    plan = {"frozen_at_utc": timestamp, "execution_authorized": False, "input_review_complete": True,
            "shard_size": SHARD_SIZE, "partition_policy": "Fixed source-order1024-row slices, all5651 IDs exactly once; complete class context precedes varying sequence; no label/output selection.",
            "replica_order": [{"gpu_ids": [gpu], "port": port} for gpu, port in REPLICAS],
            "source_recipe_file": "configs/local_labbench_b07.json", "source_recipe_sha256": file_digest(ROOT / "configs/local_labbench_b07.json"),
            "model": base["model"], "model_revision": base["model_revision"], "generation": base["generation"], "concurrency": base["concurrency"],
            "tasks": [{"task_id": "P16", "aggregate_config_file": aggregate_name, "aggregate_config_sha256": file_digest(ROOT / aggregate_name),
                       "aggregate_run_id": settings["run_id"], "full_test_case_count": TEST_COUNT, "shard_count": total_shards, "shards": shards}],
            "inference_dispatched": False, "authorizations_or_queues_modified": False,
            "global_metric_policy": "Score all original test predictions once globally with fixed384-class native accuracy; no averaging of shard metrics."}
    write_new(ROOT / PLAN_FILE, plan)
    print(json.dumps({"plan": PLAN_FILE, "sha256": file_digest(ROOT / PLAN_FILE), "cases": TEST_COUNT,
                      "shards": total_shards, "execution_authorized": False}))
    return plan


if __name__ == "__main__":
    argparse.ArgumentParser(description=__doc__).parse_args()
    prepare()
