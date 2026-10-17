"""Freeze disjoint source-order shards for the complete P03/P07/P08 tests.

Input-only preparation. This never authorizes a task or performs inference.
"""
import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path

from prepare_catalog_extended import SPECS

ROOT = Path(__file__).resolve().parents[1]
TASK_ORDER = ("P03", "P07", "P08")
REPLICAS = tuple((0, port) for port in range(8026, 8034))
SHARD_SIZE = 1024
RUNNER = "scripts/run_local_labbench_multimodal.py"
SCORER = "scripts/score_local_catalog_extended.py"
SCRIPTS = (RUNNER, SCORER, "scripts/prepare_catalog_extended.py",
           "scripts/prepare_local_extended_shards.py", "scripts/execute_local_extended_shard.py",
           "scripts/aggregate_local_extended_shards.py")
SHARD_FIELDS = ("shard_index", "shard_count", "shard_size", "full_test_case_count",
                "source_start_index", "source_stop_index", "aggregate_config_file",
                "full_input_file", "full_input_sha256", "full_review_file", "full_review_sha256")


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def file_digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_new(path, value, jsonl=False):
    if path.exists():
        raise ValueError("Refuse to overwrite frozen artifact: " + str(path))
    path.parent.mkdir(parents=True, exist_ok=True)
    text = ("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in value) if jsonl
            else json.dumps(value, ensure_ascii=False, indent=2) + "\n")
    path.write_text(text)
    path.chmod(0o600)


def execution_cases(rows, task, expected_count=None):
    if not rows or (expected_count is not None and len(rows) != expected_count):
        raise ValueError("Wrong complete released test count")
    identities = set()
    cases = []
    for index, row in enumerate(rows):
        if (row["task"] != task or row.get("system") != "" or row["source_index"] != index
                or row["split"] != "official_released_test" or row["variant"] != SPECS[task]["variant"]
                or row["case_id"] in identities):
            raise ValueError("Source order/task/variant/system/identity changed")
        identities.add(row["case_id"])
        prompt = row["prompt"]
        sequence = row["fields"]["sequence"]
        if (hashlib.sha256(prompt.encode()).hexdigest() != row["prompt_sha256"]
                or not sequence or any(not ("A" <= char <= "Z") for char in sequence)
                or not prompt.endswith(sequence) or row["fields"]["objective"] != SPECS[task]["objective"]):
            raise ValueError("Full sequence, objective or prompt integrity changed")
        if task == "P03":
            ontology = row["fields"]["native_label_ontology"]
            if [int(item["id"]) for item in ontology] != list(range(10)):
                raise ValueError("Native ten-class ontology changed")
            expected = SPECS[task]["objective"] + "\n\n" + "\n".join(
                item["id"] + ": " + item["name"] + ". " + item["description"] for item in ontology)
        else:
            expected = SPECS[task]["objective"]
        if prompt != expected + "\n\nComplete protein sequence:\n" + sequence:
            raise ValueError("Unexpected prompt additions or truncation")
        cases.append({key: row[key] for key in ("task", "case_id", "variant", "split")})
        cases[-1]["messages"] = [{"role": "user", "content": prompt}]
    return cases


def partition(cases, size=SHARD_SIZE):
    if size != SHARD_SIZE or not cases:
        raise ValueError("Shard size is preregistered at1024; require nonempty test")
    return [cases[start:start + size] for start in range(0, len(cases), size)]


def ordered_union(full_cases, shards):
    expected = [case["case_id"] for case in full_cases]
    observed = [case["case_id"] for shard in shards for case in shard]
    if len(expected) != len(set(expected)) or len(observed) != len(set(observed)):
        raise ValueError("Duplicate full/shard test identity")
    if observed != expected:
        raise ValueError("Shard ordered union differs from complete original test")
    if [case for shard in shards for case in shard] != full_cases:
        raise ValueError("Shard prompt/split/variant differs from original input")
    return {"complete": True, "union_matches_full_test_ids": True,
            "expected_test_case_count": len(expected), "unique_observed_case_count": len(set(observed)),
            "missing_case_count": 0, "extra_case_count": 0}


def recipe(settings):
    return {name: settings[name] for name in ("model", "model_revision", "checkpoint_precision",
             "generation", "concurrency", "variant", "model_facing_fields", "prompt_policy",
             "scorer_reference_file", "scorer_reference_sha256")}


def shard_metadata(settings):
    return {name: settings[name] for name in SHARD_FIELDS}


def prepare():
    plan_path = ROOT / "reports/local_extended_shard_plan.json"
    if plan_path.exists():
        raise ValueError("Plan already frozen")
    timestamp = dt.datetime.now(dt.timezone.utc).isoformat()
    base_path = ROOT / "configs/local_labbench_b07.json"
    base = json.loads(base_path.read_text())
    common_hashes = {name: file_digest(ROOT / name) for name in SCRIPTS}
    common_hashes["configs/local_labbench_b07.json"] = file_digest(base_path)
    tasks, assignment = [], 0
    for task in TASK_ORDER:
        source_name = f"data/catalog_extended/{task}/model_inputs.jsonl"
        source = ROOT / source_name
        preparation = json.loads((ROOT / f"data/catalog_extended/{task}/preparation.json").read_text())
        if file_digest(source) != preparation["files"]["model_inputs.jsonl"]["sha256"]:
            raise ValueError("Prepared native source inputs changed from release preparation")
        rows = [json.loads(line) for line in source.read_text().splitlines() if line]
        cases = execution_cases(rows, task, SPECS[task]["test_count"])
        groups = partition(cases)
        validation = ordered_union(cases, groups)
        prefix = f"data/local_catalog_extended_shards/{task}"
        full_input = prefix + "/full/model_inputs.jsonl"
        full_review = f"configs/local_extended_{task.lower()}_review.json"
        aggregate_name = f"configs/local_extended_{task.lower()}_aggregate.json"
        write_new(ROOT / full_input, cases, jsonl=True)
        review = {"task_id": task, "input_review_only": True, "reviewed_at_utc": timestamp,
                  "source_input_path": source_name, "source_input_sha256": file_digest(source),
                  "basis": "Input-only schema, complete sequence, native objective and ontology integrity review of every source-order record. No labels/model outputs used for partition or case selection; not a claim of per-residue manual inspection.",
                  "scope": "Benign native localization, GFP fluorescence or short folding-stability outcome prediction. Complete sequence and native class ontology preserved. No operational protocols, pathogen fitness optimization or transferred flagged requests.",
                  "approved_case_ids": [case["case_id"] for case in cases], "held_cases": [],
                  "approved_cases": len(cases), "full_public_cases": len(cases),
                  "selection_based_on_model_outputs": False, "classification_is_provisional": True,
                  "provisional_task_demands": ["biological outcome prediction", "learned sequence representation"]}
        write_new(ROOT / full_review, review)
        reference_name = f"data/catalog_extended/{task}/scorer_references.jsonl"
        settings = dict(base)
        settings.update(run_id=f"qwen38_27b_{task.lower()}_full_test_parallel_2026-10-15",
                        frozen_at_utc=timestamp, approved_task_ids=[task], variant=cases[0]["variant"],
                        input_file=full_input, review_file=full_review, runner=RUNNER,
                        scorer_reference_file=reference_name, scorer_reference_sha256=file_digest(ROOT / reference_name),
                        source_dataset_revision=SPECS[task]["sha256"], source_release_url=SPECS[task]["source_url"],
                        model_facing_fields=sorted(rows[0]["fields"]), input_modalities=["amino_acid_sequence", "task_instruction"],
                        prompt_policy="Exact frozen prepared user prompt, full original sequence and fixed native outcome objective; native ten-class ontology additionally retained for P03. No prompt alteration across shards.",
                        metric_policy="Stable native scorer: all-case localization accuracy or one GLOBAL full-test Spearman. Missing/invalid outputs remain explicit; no shard-correlation averaging or prediction replacement.",
                        paper_comparison="Complete pinned released test and native metric; zero-shot prompted Qwen differs from trained specialist baselines. P08 PyTorch release12851 differs from original2019 paper12839.",
                        full_test_case_count=len(cases), shard_count=len(groups), shard_size=SHARD_SIZE,
                        aggregate_only=True, generator_execution_allowed=False,
                        endpoint="aggregate-only://offline", case_scope="aggregate_only_full_test")
        settings.pop("source_code_revision", None)
        settings.pop("gpu_ids", None)
        settings.pop("serving_config_file", None)
        settings.pop("server_record_file", None)
        hashes = dict(common_hashes)
        for name in (source_name, full_input, full_review, f"data/catalog_extended/{task}/preparation.json"):
            hashes[name] = file_digest(ROOT / name)
        settings["frozen_files_sha256"] = hashes
        entries = []
        for index, group in enumerate(groups):
            gpu, port = REPLICAS[assignment % len(REPLICAS)]
            assignment += 1
            shard_input = prefix + f"/shard_{index:03d}/model_inputs.jsonl"
            shard_review = f"configs/local_extended_{task.lower()}_shard_{index:03d}_review.json"
            shard_config = f"configs/local_extended_{task.lower()}_shard_{index:03d}.json"
            start, stop = index * SHARD_SIZE, min((index + 1) * SHARD_SIZE, len(cases))
            write_new(ROOT / shard_input, group, jsonl=True)
            write_new(ROOT / shard_review, {**review, "approved_case_ids": [c["case_id"] for c in group],
                      "approved_cases": len(group), "case_scope": "task_shard_only",
                      "shard_index": index, "shard_count": len(groups), "source_start_index": start,
                      "source_stop_index": stop, "whole_task_review_file": full_review,
                      "whole_task_review_sha256": file_digest(ROOT / full_review)})
            shard = {**settings, "run_id": settings["run_id"] + f"_shard_{index:03d}",
                     "aggregate_only": False, "generator_execution_allowed": True,
                     "input_file": shard_input, "review_file": shard_review,
                     "endpoint": f"http://127.0.0.1:{port}/v1", "gpu_ids": [gpu],
                     "serving_config_file": f"configs/local_model_gpu{gpu}.json" if gpu != 5 else "configs/local_model.json",
                     "server_record_file": f".local/local_model_server_gpu{gpu}.json" if gpu != 5 else ".local/local_model_server.json",
                     "shard_index": index, "source_start_index": start, "source_stop_index": stop,
                     "aggregate_config_file": aggregate_name, "full_input_file": full_input,
                     "full_input_sha256": file_digest(ROOT / full_input), "full_review_file": full_review,
                     "full_review_sha256": file_digest(ROOT / full_review), "case_scope": "task_shard_only",
                     "assignment_index": assignment - 1}
            shard["frozen_files_sha256"] = {**hashes, shard_input: file_digest(ROOT / shard_input),
                                            shard_review: file_digest(ROOT / shard_review)}
            write_new(ROOT / shard_config, shard)
            entries.append({"config_file": shard_config, "config_sha256": file_digest(ROOT / shard_config),
                            "run_id": shard["run_id"], "shard_index": index, "cases": len(group),
                            "gpu_ids": [gpu], "endpoint": shard["endpoint"]})
        settings["shard_configs"] = entries
        settings["full_test_id_union_validation"] = validation
        write_new(ROOT / aggregate_name, settings)
        tasks.append({"task_id": task, "aggregate_config_file": aggregate_name,
                      "aggregate_config_sha256": file_digest(ROOT / aggregate_name),
                      "aggregate_run_id": settings["run_id"], "full_test_case_count": len(cases),
                      "shard_count": len(groups), "shards": entries})
    plan = {"frozen_at_utc": timestamp, "shard_size": SHARD_SIZE, "partition_policy": "Consecutive source-order1024-row slices; every row once; no labels/outcomes read for partition.",
            "replica_order": [{"gpu_ids": [gpu], "port": port} for gpu, port in REPLICAS],
            "assignment_policy": "Roundrobin across fixed P03,P07,P08 task order, then source-order shard index.",
            "source_recipe_file": "configs/local_labbench_b07.json", "source_recipe_sha256": file_digest(base_path),
            "model": base["model"], "model_revision": base["model_revision"], "generation": base["generation"],
            "concurrency": base["concurrency"], "tasks": tasks, "inference_dispatched": False,
            "authorizations_or_queues_modified": False, "global_metric_policy": "Score combined full ordered predictions once; never average shard correlations."}
    write_new(plan_path, plan)
    print(json.dumps({"plan": str(plan_path.relative_to(ROOT)), "sha256": file_digest(plan_path),
                      "tasks": [{"task": t["task_id"], "cases": t["full_test_case_count"], "shards": t["shard_count"]} for t in tasks]}))
    return plan


if __name__ == "__main__":
    argparse.ArgumentParser(description=__doc__).parse_args()
    prepare()
