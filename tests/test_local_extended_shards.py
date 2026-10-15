"""Synthetic contracts for complete-test sharding and global metric assembly."""
import contextlib
import copy
import csv
import io
import json
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import aggregate_local_extended_shards as aggregate
import execute_local_extended_shard as execute
import prepare_catalog_extended as source
import prepare_local_extended_shards as prepare
import run_local_labbench_multimodal as runner
import score_local_catalog_extended as scorer


def save(path, value, jsonl=False):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(row) + "\n" for row in value) if jsonl else json.dumps(value))


class SyntheticShards:
    def __init__(self, root):
        self.root = root
        generation = {"max_tokens": 4096, "temperature": 1., "top_p": .95, "top_k": 20, "seed": 42,
                      "n": 1, "chat_template_kwargs": {"enable_thinking": True, "reasoning_effort": "medium"}}
        self.full = {"run_id": "synthetic-full", "model": "synthetic-model", "model_revision": "synthetic-revision",
                     "checkpoint_precision": "synthetic-BF16", "generation": generation, "concurrency": 4,
                     "variant": "SYNTHETIC", "model_facing_fields": ["sequence", "objective"], "prompt_policy": "fixed artificial prompt",
                     "approved_task_ids": ["P07"], "scorer_reference_file": "refs.jsonl", "input_file": "inputs.jsonl", "review_file": "review.json",
                     "aggregate_only": True, "generator_execution_allowed": False, "endpoint": "aggregate-only://offline",
                     "shard_count": 2, "full_test_case_count": 4, "shard_size": 2, "runner": prepare.RUNNER}
        self.cases = [{"task": "P07", "case_id": str(i), "variant": "SYNTHETIC", "split": "synthetic",
                       "messages": [{"role": "user", "content": "Artificial sequence example " + str(i)}]} for i in range(4)]
        save(root / "inputs.jsonl", self.cases, True)
        save(root / "review.json", {"approved_case_ids": [str(i) for i in range(4)], "held_cases": []})
        save(root / "refs.jsonl", [{"task": "P07", "case_id": str(i), "target": float(i + 1)} for i in range(4)], True)
        self.full["scorer_reference_sha256"] = prepare.file_digest(root / "refs.jsonl")
        (root / prepare.RUNNER).parent.mkdir(parents=True, exist_ok=True)
        (root / prepare.RUNNER).write_text("# synthetic pinned runner\n")
        self.full["frozen_files_sha256"] = {name: prepare.file_digest(root / name) for name in ["inputs.jsonl", "review.json", prepare.RUNNER]}
        save(root / "recipe.json", self.full)
        entries = []
        for index in range(2):
            gpu, port = prepare.REPLICAS[index]
            start, stop = index * 2, (index + 1) * 2
            cases = self.cases[start:stop]
            input_name, review_name = f"input{index}.jsonl", f"review{index}.json"
            save(root / input_name, cases, True)
            save(root / review_name, {"approved_case_ids": [c["case_id"] for c in cases], "held_cases": []})
            shard = {**self.full, "run_id": f"synthetic-shard{index}", "aggregate_only": False,
                     "generator_execution_allowed": True, "case_scope": "task_shard_only", "input_file": input_name,
                     "review_file": review_name, "shard_index": index, "source_start_index": start,
                     "source_stop_index": stop, "aggregate_config_file": "aggregate.json", "full_input_file": "inputs.jsonl",
                     "full_review_file": "review.json", "full_input_sha256": prepare.file_digest(root / "inputs.jsonl"),
                     "full_review_sha256": prepare.file_digest(root / "review.json"), "gpu_ids": [gpu],
                     "endpoint": f"http://127.0.0.1:{port}/v1", "assignment_index": index}
            shard["frozen_files_sha256"] = {**self.full["frozen_files_sha256"], input_name: prepare.file_digest(root / input_name), review_name: prepare.file_digest(root / review_name)}
            config_name = f"shard{index}.json"
            save(root / config_name, shard)
            config_hash = prepare.file_digest(root / config_name)
            folder = root / "results/runs" / shard["run_id"]
            server = {"model": shard["model"], "revision": shard["model_revision"], "gpu_ids": [gpu], "pid": 100 + index, "proc_start_ticks": "1234"}
            manifest = {"configuration": shard, "configuration_sha256": config_hash,
                        "runner_sha256": prepare.file_digest(root / prepare.RUNNER), "planned_cases": len(cases),
                        "case_contract_sha256": prepare.digest(cases), "model_selection_on_test": False,
                        "solver_tools": [], "answer_keys_available_to_solver": False, "server": server,
                        "serving_configuration": {"host": "127.0.0.1", "port": port, "gpu_ids": [gpu], "model": shard["model"], "revision": shard["model_revision"]}}
            save(folder / "run_manifest.json", manifest)
            for case in cases:
                identity = prepare.digest([case["task"], case["variant"], case["case_id"]])
                request = runner.request_record(case, shard)
                save(folder / "requests" / (identity + ".json"), request)
                text = str([3, 4, 1, 2][int(case["case_id"])])
                response = {**{key: case[key] for key in ["task", "case_id", "variant", "split"]},
                            "model": shard["model"], "model_revision": shard["model_revision"],
                            "request_sha256": request["request_sha256"], "status": "completed", "http_status": 200,
                            "text": text, "finish_reason": "stop", "response": {"model": shard["model"], "choices": [{"message": {"content": text}, "finish_reason": "stop"}]}}
                save(folder / "responses" / (identity + ".json"), response)
            with patch.object(scorer, "ROOT", root), contextlib.redirect_stdout(io.StringIO()):
                scorer.score(folder)
            execute.mark_shard_scores(folder, shard)
            save(folder / "completion.json", {"generation_exit_code": 0, "scoring_exit_code": 0,
                 "configuration_sha256": config_hash, "run_manifest_sha256": prepare.file_digest(folder / "run_manifest.json"),
                 "scores_sha256": prepare.file_digest(folder / "scores.json"), "case_scope": "task_shard_only", **prepare.shard_metadata(shard)})
            entries.append({"config_file": config_name, "config_sha256": config_hash, "run_id": shard["run_id"],
                            "shard_index": index, "gpu_ids": [gpu], "endpoint": shard["endpoint"], "cases": 2})
        self.full["shard_configs"] = entries
        save(root / "aggregate.json", self.full)
        self.entry = {"task_id": "P07", "aggregate_config_file": "aggregate.json", "aggregate_config_sha256": prepare.file_digest(root / "aggregate.json"),
                      "aggregate_run_id": "synthetic-full", "full_test_case_count": 4, "shards": entries}
        self.plan = {"source_recipe_file": "recipe.json", "source_recipe_sha256": prepare.file_digest(root / "recipe.json"), "tasks": [self.entry]}


class ExtendedShardTests(unittest.TestCase):
    def fixture(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        return SyntheticShards(Path(temporary.name))

    def test_source_prompts_and_complete_sequences_retained(self):
        rows = [source.transform("P08", i, {"primary": "MAG" + "A" * i, "stability_score": 1000 + i})[0] for i in range(3)]
        cases = prepare.execution_cases(rows, "P08", 3)
        self.assertEqual([case["messages"][0]["content"] for case in cases], [row["prompt"] for row in rows])
        self.assertNotIn("1000", str(cases))
        altered = copy.deepcopy(rows); altered[1]["prompt"] += " omitted"
        with self.assertRaisesRegex(ValueError, "integrity"):
            prepare.execution_cases(altered, "P08", 3)

    def test_fixed_partition_disjoint_exact_union(self):
        cases = [{"case_id": str(i)} for i in range(2050)]
        shards = prepare.partition(cases)
        self.assertEqual([len(shard) for shard in shards], [1024, 1024, 2])
        self.assertEqual(prepare.ordered_union(cases, shards)["unique_observed_case_count"], 2050)
        with self.assertRaises(ValueError):
            prepare.partition(cases, 512)

    def test_duplicate_missing_extra_and_reordered_union_rejected(self):
        cases = [{"case_id": str(i)} for i in range(4)]
        for groups in [[cases[:2], cases[1:]], [cases[:2], cases[3:]], [cases, [{"case_id": "extra"}]], [cases[2:], cases[:2]]]:
            with self.assertRaises(ValueError):
                prepare.ordered_union(cases, groups)

    def test_recipe_mismatch_rejected(self):
        fixture = self.fixture()
        for key, value in [("generation", {"n": 2}), ("model_revision", "different"), ("variant", "changed"), ("prompt_policy", "changed")]:
            changed = {**fixture.full, key: value, "aggregate_only": False, "case_scope": "task_shard_only"}
            with self.assertRaisesRegex(ValueError, "recipe mismatch"):
                aggregate.validate_recipe(fixture.full, changed, fixture.full)

    def test_shard_scores_and_csv_never_claim_full_test(self):
        fixture = self.fixture()
        folder = fixture.root / "results/runs/synthetic-shard0"
        summary = json.loads((folder / "scores.json").read_text())
        self.assertEqual(summary["case_scope"], "task_shard_only")
        with (folder / "metrics.csv").open() as handle:
            rows = list(csv.DictReader(handle))
        self.assertTrue(all(row["case_scope"] == "task_shard_only" and row["full_test_case_count"] == "4" for row in rows))

    def test_global_spearman_computed_from_combined_predictions_once(self):
        fixture = self.fixture()
        called = []
        def score_command(command, cwd):
            called.append(command)
            folder = fixture.root / "results/runs/synthetic-full"
            self.assertFalse((folder / "scoring_output_lock.json").exists())
            with patch.object(scorer, "ROOT", fixture.root), contextlib.redirect_stdout(io.StringIO()):
                scorer.score(folder)
            return SimpleNamespace(returncode=0)
        with patch.object(aggregate, "ROOT", fixture.root), patch.object(aggregate, "SHARD_SIZE", 2), patch.object(aggregate.subprocess, "run", score_command):
            aggregate.aggregate(fixture.entry, fixture.plan, "synthetic-plan-sha")
            aggregate.aggregate(fixture.entry, fixture.plan, "synthetic-plan-sha")
        self.assertEqual(len(called), 1)
        scores = json.loads((fixture.root / "results/runs/synthetic-full/scores.json").read_text())
        self.assertAlmostEqual(scores["metrics"]["spearman"], -.6)
        self.assertEqual(scores["full_test_id_union_validation"]["unique_observed_case_count"], 4)
        self.assertEqual(scores["case_scope"], "full_frozen_reviewed_released_test")

    def test_failed_shard_blocks_and_pending_waits(self):
        fixture = self.fixture()
        path = fixture.root / "results/runs/synthetic-shard0/completion.json"
        path.unlink()
        with patch.object(aggregate, "ROOT", fixture.root):
            with self.assertRaises(aggregate.Pending):
                aggregate.validate_task(fixture.entry, fixture.plan)
            save(fixture.root / "results/runs/synthetic-shard1/completion.json", {"generation_exit_code": 1})
            with self.assertRaisesRegex(ValueError, "Failed shard"):
                aggregate.validate_task(fixture.entry, fixture.plan)

    def test_raw_mutation_or_extra_response_rejected(self):
        fixture = self.fixture()
        folder = fixture.root / "results/runs/synthetic-shard0"
        path = next((folder / "responses").glob("*.json"))
        original = path.read_bytes()
        response = json.loads(original); response["text"] = "different"
        save(path, response)
        with patch.object(aggregate, "ROOT", fixture.root), patch.object(aggregate, "SHARD_SIZE", 2):
            with self.assertRaisesRegex(ValueError, "raw response"):
                aggregate.validate_task(fixture.entry, fixture.plan)
            path.write_bytes(original)
            save(folder / "responses/extra.json", {})
            with self.assertRaisesRegex(ValueError, "extra raw"):
                aggregate.validate_task(fixture.entry, fixture.plan)

    def test_config_hash_mismatch_rejected(self):
        fixture = self.fixture()
        with (fixture.root / "shard0.json").open("a") as handle:
            handle.write(" ")
        with patch.object(aggregate, "ROOT", fixture.root), patch.object(aggregate, "SHARD_SIZE", 2):
            with self.assertRaisesRegex(ValueError, "Frozen file"):
                aggregate.validate_task(fixture.entry, fixture.plan)

    def test_aggregate_config_cannot_invoke_generator(self):
        fixture = self.fixture()
        with self.assertRaises(ValueError):
            runner.validate_endpoint(fixture.full["endpoint"])
        with self.assertRaisesRegex(ValueError, "Only executable"):
            execute.execute(fixture.root / "aggregate.json")


if __name__ == "__main__":
    unittest.main()
