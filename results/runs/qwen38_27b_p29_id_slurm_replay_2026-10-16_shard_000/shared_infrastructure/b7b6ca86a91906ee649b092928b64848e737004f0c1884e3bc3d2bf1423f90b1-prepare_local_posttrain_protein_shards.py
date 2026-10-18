"""Freeze disabled P29 ID/OOD source-order shards; no inference or queue edits."""
import datetime as dt
import json

import local_posttrain_protein_shards as common
import posttrain_protein_contract as protocol

ROOT = common.ROOT
POLICY = "Wait for every source shard terminal; lock all outputs/missing slots before labels; preserve every planned failure as empty GO set. Score native augmented-reference mean GO-F1 once per complete ID/OOD union, curated-only diagnostic separately. Nonzero source generation remains nonzero aggregate status. No retries/resampling or score selection."
SCRIPTS = [common.RUNNER, "scripts/run_local_labbench_multimodal.py", "scripts/bioreason_pro_contract.py", "scripts/score_local_bioreason_pro.py",
    common.SCORER, "scripts/posttrain_protein_contract.py", "scripts/prepare_catalog_posttrain_protein.py", "scripts/local_posttrain_protein_shards.py",
    "scripts/prepare_local_posttrain_protein_shards.py", "scripts/execute_local_posttrain_protein_shard.py", "scripts/aggregate_local_posttrain_protein_shards.py"]


def write_new(name, value, jsonl=False):
    path = ROOT / name
    if path.exists(): raise ValueError("Refuse replacement of frozen prospective asset: " + name)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in value) if jsonl else json.dumps(value, ensure_ascii=False, indent=2) + "\n")
    path.chmod(0o600)


def prepare():
    if (ROOT / common.PLAN_FILE).exists(): raise ValueError("P29 plan already frozen")
    if common.file_sha(ROOT / common.RUNNER) != common.RUNNER_SHA256: raise ValueError("Root-reviewed expanded runner changed")
    prepared_name = "data/catalog_posttrain_protein/P29/preparation.json"
    prepared = json.loads((ROOT / prepared_name).read_text())
    base_name = "configs/local_labbench_b07.json"; base = json.loads((ROOT / base_name).read_text())
    if base["generation"]["max_tokens"] != 4096: raise ValueError("Only fixed4096-token recipe is proposed")
    timestamp = dt.datetime.now(dt.timezone.utc).isoformat()
    source_hashes = protocol.verified_sources()
    for name in SCRIPTS + [base_name, prepared_name, "reports/POSTTRAIN_NATIVE_GAP_AUDIT.md", "reports/posttrain_native_gap_audit.json"]:
        source_hashes[name] = common.file_sha(ROOT / name)
    aggregates, flat, global_index = [], [], 0
    for split, (_, count, _) in protocol.SPLITS.items():
        folder = "data/catalog_posttrain_protein/P29/" + split; full_input = folder + "/model_inputs.jsonl"
        if common.file_sha(ROOT / full_input) != prepared["splits"][split]["input_sha256"]: raise ValueError("Prepared input changed")
        cases = [json.loads(line) for line in (ROOT / full_input).read_text().splitlines() if line]
        ids = [c["case_id"] for c in cases]
        if len(cases) != count or ids != json.loads((ROOT / folder / "ordered_case_ids.json").read_text()): raise ValueError("Native split/order changed")
        full_review = f"configs/local_posttrain_protein_p29_{split}_review.json"
        full_config = f"configs/local_posttrain_protein_p29_{split}_aggregate.json"
        review = {"task_id": "P29", "native_split": split, "reviewed": True, "input_review_only": True,
            "reviewed_at_utc": timestamp, "source_input_path": full_input, "source_input_sha256": common.file_sha(ROOT / full_input),
            "basis": "All exact author source-order species-split protein annotation cases with complete sequence and native RL organism/InterPro/GO-GPT context. Fixed all3 aspects, no names/gold/teacher/PPI, no sequence optimization or operational protocols; labels/outputs never partition inputs.",
            "approved_case_ids": ids, "approved_cases": count, "held_cases": [], "classification_is_provisional": True, "execution_authorized_by_this_review": False}
        write_new(full_review, review)
        frozen = dict(source_hashes)
        for name in [full_input, full_review, folder + "/ordered_case_ids.json", folder + "/input_provenance.json", folder + "/organism_counts.json"]:
            frozen[name] = common.file_sha(ROOT / name)
        groups = [cases[i:i + common.SHARD_SIZE] for i in range(0, count, common.SHARD_SIZE)]
        full = {**base, "run_id": f"qwen38_27b_p29_{split}_full_released_rl_context_parallel_2026-10-15", "frozen_at_utc": timestamp,
            "execution_authorized": False, "input_review_complete": True, "approved_task_ids": ["P29"], "variant": protocol.VARIANT,
            "native_split": split, "input_file": full_input, "review_file": full_review, "runner": common.RUNNER,
            "scorer_reference_file": folder + "/scorer_references.jsonl", "scorer_reference_sha256": prepared["splits"][split]["files"]["scorer_references.jsonl"]["sha256"],
            "source_code_revision": protocol.CODE_REVISION, "source_dataset_revision": "public_author_Drive_objects_frozen_SHA256",
            "model_facing_fields": prepared["model_facing_fields"], "input_modalities": ["complete_amino_acid_sequence", "organism", "native_InterPro_text", "native_GO_GPT_predictions"],
            "prompt_policy": "Exact released RL build_prompt with full native input allowlist and source flags; one Qwen chat user message, complete original sequence/context, no annotation or teacher fields, no extra retrieval or options.",
            "metric_policy": prepared["native_metric"] + " " + prepared["native_target_augmentation"],
            "paper_comparison": "Same exact released ID6989/OOD7883 species split and source RL text prompt/native set-F1 adaptation; different frozen zero-shot Qwen3.8-27B, chat template and4096-token generation, no author training/checkpoint replication. " + prepared["native_target_augmentation"],
            "source_contract_disagreements": prepared["source_disagreements"], "prospective_interpretation": prepared["interpretation"],
            "seed_predictor_overlap": prepared["splits"][split]["seed_predictor_overlap"],
            "full_test_case_count": count, "shard_count": len(groups), "shard_size": common.SHARD_SIZE,
            "aggregate_only": True, "generator_execution_allowed": False, "endpoint": "aggregate-only://offline",
            "case_scope": "aggregate_only_full_released_species_test", "shard_plan_file": common.PLAN_FILE,
            "incomplete_output_policy": POLICY, "frozen_files_sha256": frozen}
        for key in ["gpu_ids", "serving_config_file", "server_record_file"]: full.pop(key, None)
        entries = []; first_global = global_index
        for index, group in enumerate(groups):
            gpu, port = common.REPLICAS[global_index % len(common.REPLICAS)]
            input_name = f"data/local_posttrain_protein_shards/P29/{split}/shard_{index:03d}/model_inputs.jsonl"
            review_name = f"configs/local_posttrain_protein_p29_{split}_shard_{index:03d}_review.json"
            config_name = f"configs/local_posttrain_protein_p29_{split}_shard_{index:03d}.json"
            start, stop = index * common.SHARD_SIZE, min((index + 1) * common.SHARD_SIZE, count)
            write_new(input_name, group, jsonl=True)
            write_new(review_name, {**review, "approved_case_ids": [r["case_id"] for r in group], "approved_cases": len(group),
                "case_scope": "task_shard_only", "source_start_index": start, "source_stop_index": stop,
                "whole_task_review_file": full_review, "whole_task_review_sha256": common.file_sha(ROOT / full_review)})
            cfg = {**full, "run_id": full["run_id"] + f"_shard_{index:03d}", "aggregate_only": False, "generator_execution_allowed": True,
                "input_file": input_name, "review_file": review_name, "endpoint": f"http://127.0.0.1:{port}/v1", "gpu_ids": [gpu],
                "serving_config_file": f"configs/local_model_gpu{gpu}.json" if gpu != 5 else "configs/local_model.json",
                "server_record_file": f".local/local_model_server_gpu{gpu}.json" if gpu != 5 else ".local/local_model_server.json",
                "shard_index": index, "global_shard_index": global_index, "source_start_index": start, "source_stop_index": stop,
                "aggregate_config_file": full_config, "full_input_file": full_input, "full_input_sha256": common.file_sha(ROOT / full_input),
                "full_review_file": full_review, "full_review_sha256": common.file_sha(ROOT / full_review), "case_scope": "task_shard_only",
                "frozen_files_sha256": {**frozen, input_name: common.file_sha(ROOT / input_name), review_name: common.file_sha(ROOT / review_name)}}
            write_new(config_name, cfg)
            item = {"config_file": config_name, "config_sha256": common.file_sha(ROOT / config_name), "run_id": cfg["run_id"],
                "native_split": split, "shard_index": index, "global_shard_index": global_index, "cases": len(group), "gpu_ids": [gpu], "endpoint": cfg["endpoint"]}
            entries.append(item); flat.append(item); global_index += 1
        union = common.ordered_union(cases, groups); full.update(shard_configs=entries, full_test_id_union_validation=union)
        write_new(full_config, full)
        aggregates.append({"native_split": split, "aggregate_config_file": full_config, "aggregate_config_sha256": common.file_sha(ROOT / full_config),
            "aggregate_run_id": full["run_id"], "source_recipe_file": base_name, "source_recipe_sha256": common.file_sha(ROOT / base_name),
            "full_test_case_count": count, "global_shard_start_index": first_global, "shards": entries, "full_test_id_union_validation": union,
            "incomplete_output_policy": POLICY, "global_metric_policy": "One native augmented-reference mean GO-F1 evaluation from complete combined raw predictions per ID/OOD split, with fixed curated-only diagnostic and organism subgroup accounting. No shard metrics averaged."})
    plan = {"task_id": "P29", "frozen_at_utc": timestamp, "model": base["model"], "model_revision": base["model_revision"],
        "generation": base["generation"], "concurrency": base["concurrency"], "shards": flat, "aggregates": aggregates,
        "full_test_case_count": sum(x["full_test_case_count"] for x in aggregates), "shard_size": common.SHARD_SIZE, "shard_count": len(flat),
        "replica_order": [{"gpu_ids": [g], "port": port} for g, port in common.REPLICAS],
        "partition_policy": "Each native split separately, original source-order consecutive1024 rows, exact union/no duplicates; roundrobin across GPU1–7. No labels, targets, outputs or model scores used for partition.",
        "incomplete_output_policy": POLICY, "execution_authorized": False, "inference_dispatched": False, "authorizations_or_queues_modified": False}
    write_new(common.PLAN_FILE, plan)
    write_new(common.APPROVAL_FILE, {"execution_authorized": False, "approved_task_ids": [], "model": base["model"], "model_revision": base["model_revision"],
        "generation_sha256": common.digest(base["generation"]), "plan_sha256": common.file_sha(ROOT / common.PLAN_FILE), "approved_config_sha256": {}, "incomplete_output_policy": POLICY,
        "activation_order": "Root reviews exact frozen plan/target qualification, authorizes this exact approval, then centralP29allowlist, then gated shard executor only. Generic runner ignores perconfig execution flag."})
    print(json.dumps({"plan": common.PLAN_FILE, "sha256": common.file_sha(ROOT / common.PLAN_FILE), "shards": len(flat), "cases": plan["full_test_case_count"], "execution_authorized": False}))
    return plan


if __name__ == "__main__": prepare()
