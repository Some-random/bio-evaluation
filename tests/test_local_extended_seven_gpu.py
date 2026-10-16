"""Synthetic routing, disabled approval, immutable union and global-score tests."""
import contextlib
import copy
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
sys.path.insert(0, str(ROOT / "tests"))
import prepare_local_extended_seven_gpu as prepare
import execute_local_extended_seven_gpu as execute
import aggregate_local_extended_seven_gpu as aggregate
import prepare_local_extended_shards as old_prepare
import run_local_labbench_multimodal as old_runner
import run_local_labbench_eight_gpu as new_runner
import score_local_catalog_extended as scorer
from test_local_extended_shards import SyntheticShards, save


class RoutingFixture:
    def __init__(self, root):
        self.root = root
        for name in [prepare.RUNNER, prepare.PREPARER, prepare.EXECUTOR, prepare.AGGREGATOR, "scripts/original_runner.py"]:
            path = root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("# synthetic dependency: " + name + "\n")
        self.runner_hash = prepare.file_digest(root / prepare.RUNNER)
        self.base = {"model": "synthetic", "model_revision": "pinned", "checkpoint_precision": "BF16",
                     "generation": {"max_tokens": 4096, "n": 1, "temperature": 1., "top_p": .95, "top_k": 20, "seed": 42,
                                    "chat_template_kwargs": {"enable_thinking": True, "reasoning_effort": "medium"}},
                     "concurrency": 4, "variant": "SYNTHETIC", "model_facing_fields": ["sequence"],
                     "prompt_policy": "same full synthetic source prompt", "scorer_reference_file": "not_opened_refs.jsonl",
                     "scorer_reference_sha256": "synthetic-hidden"}
        save(root / "recipe.json", self.base)
        tasks = []
        for task in prepare.TASK_ORDER:
            cases = [{"task": task, "case_id": f"{task}:{i}", "variant": "SYNTHETIC", "split": "synthetic",
                      "messages": [{"role": "user", "content": f"Complete synthetic protein example {task}:{i}"}]} for i in range(2050)]
            full_input, full_review = f"old/{task}/full.jsonl", f"old/{task}/review.json"
            save(root / full_input, cases, True)
            save(root / full_review, {"approved_case_ids": [case["case_id"] for case in cases], "held_cases": []})
            hashes = {name: prepare.file_digest(root / name) for name in [full_input, full_review, "scripts/original_runner.py"]}
            aggregate_name = f"configs/old_{task}_aggregate.json"
            full = {**self.base, "run_id": "old-full-" + task, "approved_task_ids": [task], "input_file": full_input,
                    "review_file": full_review, "runner": "scripts/original_runner.py", "aggregate_only": True,
                    "generator_execution_allowed": False, "endpoint": "aggregate-only://offline", "case_scope": "aggregate_only_full_test",
                    "full_test_case_count": len(cases), "shard_count": 3, "shard_size": 1024, "frozen_files_sha256": hashes}
            entries, groups = [], []
            for index in range(3):
                group = cases[index * 1024:(index + 1) * 1024]
                groups.append(group)
                inp, rev = f"old/{task}/shard{index}.jsonl", f"old/{task}/review{index}.json"
                save(root / inp, group, True)
                save(root / rev, {"approved_case_ids": [case["case_id"] for case in group], "held_cases": []})
                cfg = {**full, "run_id": f"old-shard-{task}-{index}", "input_file": inp, "review_file": rev,
                       "aggregate_only": False, "generator_execution_allowed": True, "case_scope": "task_shard_only",
                       "shard_index": index, "assignment_index": index, "source_start_index": index * 1024,
                       "source_stop_index": min((index + 1) * 1024, len(cases)), "aggregate_config_file": aggregate_name,
                       "full_input_file": full_input, "full_input_sha256": hashes[full_input],
                       "full_review_file": full_review, "full_review_sha256": hashes[full_review],
                       "gpu_ids": [6], "endpoint": "http://127.0.0.1:8027/v1", "serving_config_file": "old-serving.json", "server_record_file": "old-server.json",
                       "frozen_files_sha256": {**hashes, inp: prepare.file_digest(root / inp), rev: prepare.file_digest(root / rev)}}
                name = f"configs/old_{task}_shard{index}.json"
                save(root / name, cfg)
                entries.append({"config_file": name, "config_sha256": prepare.file_digest(root / name), "run_id": cfg["run_id"],
                                "shard_index": index, "cases": len(group), "gpu_ids": [6], "endpoint": cfg["endpoint"]})
            full["shard_configs"] = entries
            full["full_test_id_union_validation"] = prepare.ordered_union(cases, groups)
            save(root / aggregate_name, full)
            tasks.append({"task_id": task, "aggregate_config_file": aggregate_name, "aggregate_config_sha256": prepare.file_digest(root / aggregate_name),
                          "aggregate_run_id": full["run_id"], "full_test_case_count": len(cases), "shard_count": 3, "shards": entries})
        self.plan = {"tasks": tasks, "source_recipe_file": "recipe.json", "source_recipe_sha256": prepare.file_digest(root / "recipe.json"),
                     "generation": self.base["generation"], "model": self.base["model"], "model_revision": self.base["model_revision"], "concurrency": 4}
        save(root / prepare.OLD_PLAN, self.plan)


class SevenGpuTests(unittest.TestCase):
    def routing_fixture(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        return RoutingFixture(Path(temporary.name))

    def test_new_plan_preserves_old_bytes_full_messages_recipe_and_seven_gpu_mapping(self):
        fixture = self.routing_fixture()
        before = {str(path.relative_to(fixture.root)): path.read_bytes() for path in fixture.root.rglob("*") if path.is_file()}
        with patch.object(prepare, "RUNNER_SHA256", fixture.runner_hash):
            result = prepare.prepare(fixture.root, expected_shards=9)
        self.assertEqual(result["new_shards"], 9)
        self.assertFalse(result["approved"])
        for name, data in before.items():
            self.assertEqual((fixture.root / name).read_bytes(), data)
        plan = json.loads((fixture.root / prepare.PLAN).read_text())
        shards = [row for task in plan["tasks"] for row in task["shards"]]
        self.assertEqual([row["gpu_ids"][0] for row in shards], [1, 2, 3, 4, 5, 6, 7, 1, 2])
        for task, original in zip(plan["tasks"], fixture.plan["tasks"]):
            full = json.loads((fixture.root / task["aggregate_config_file"]).read_text())
            old_full = json.loads((fixture.root / original["aggregate_config_file"]).read_text())
            self.assertEqual(full["input_file"], old_full["input_file"])
            self.assertEqual(prepare.recipe(full), prepare.recipe(old_full))
            groups = []
            for item, old_item in zip(task["shards"], original["shards"]):
                new = json.loads((fixture.root / item["config_file"]).read_text())
                old = json.loads((fixture.root / old_item["config_file"]).read_text())
                cases = [json.loads(line) for line in (fixture.root / new["input_file"]).read_text().splitlines()]
                groups.append(cases)
                self.assertEqual(new["input_file"], old["input_file"])
                self.assertEqual(old_runner.request_record(cases[0], old), new_runner.request_record(cases[0], new))
            full_cases = [json.loads(line) for line in (fixture.root / full["input_file"]).read_text().splitlines()]
            self.assertTrue(prepare.ordered_union(full_cases, groups)["complete"])

    def test_disabled_gate_then_exact_approval_and_started_old_run_rejection(self):
        fixture = self.routing_fixture()
        with patch.object(prepare, "RUNNER_SHA256", fixture.runner_hash):
            prepare.prepare(fixture.root, expected_shards=9)
            with self.assertRaisesRegex(ValueError, "remains disabled"):
                prepare.require_approval(fixture.root)
            path = fixture.root / prepare.APPROVAL
            approval = json.loads(path.read_text())
            approval["approved"] = True
            save(path, approval)
            plan = prepare.require_approval(fixture.root)
            name = plan["tasks"][0]["shards"][0]["config_file"]
            prepare.require_approval(fixture.root, config_name=name)
            old_run = fixture.plan["tasks"][0]["shards"][0]["run_id"]
            (fixture.root / "results/runs" / old_run).mkdir(parents=True)
            with self.assertRaisesRegex(ValueError, "never migrate"):
                prepare.require_approval(fixture.root)

    def test_started_original_blocks_preparation_before_new_artifacts(self):
        fixture = self.routing_fixture()
        old_run = fixture.plan["tasks"][0]["shards"][0]["run_id"]
        save(fixture.root / "results/runs" / old_run / "requests/case.json", {"synthetic": True})
        with patch.object(prepare, "RUNNER_SHA256", fixture.runner_hash), self.assertRaisesRegex(ValueError, "never migrate"):
            prepare.prepare(fixture.root, expected_shards=9)
        self.assertFalse((fixture.root / prepare.PLAN).exists())
        self.assertFalse((fixture.root / prepare.APPROVAL).exists())

    def test_disabled_executor_never_calls_runner(self):
        fixture = self.routing_fixture()
        with patch.object(prepare, "RUNNER_SHA256", fixture.runner_hash):
            prepare.prepare(fixture.root, expected_shards=9)
        plan = json.loads((fixture.root / prepare.PLAN).read_text())
        path = fixture.root / plan["tasks"][0]["shards"][0]["config_file"]
        with patch.object(execute, "ROOT", fixture.root), patch.object(execute.subprocess, "run") as call:
            with self.assertRaisesRegex(ValueError, "remains disabled"):
                execute.execute(path)
            call.assert_not_called()

    def test_global_spearman_once_uses_full_union_not_shard_averaging(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        with patch.object(old_prepare, "RUNNER", prepare.RUNNER), patch.object(old_prepare, "REPLICAS", prepare.REPLICAS):
            fixture = SyntheticShards(Path(temporary.name))
        called = []
        def score_command(command, cwd):
            called.append(command)
            with patch.object(scorer, "ROOT", fixture.root), contextlib.redirect_stdout(io.StringIO()):
                scorer.score(fixture.root / "results/runs/synthetic-full")
            return SimpleNamespace(returncode=0)
        with patch.object(aggregate, "ROOT", fixture.root), patch.object(aggregate, "SHARD_SIZE", 2), patch.object(aggregate, "require_approval", return_value=fixture.plan), patch.object(aggregate.subprocess, "run", score_command):
            aggregate.aggregate(fixture.entry, fixture.plan, "synthetic-plan-hash")
            aggregate.aggregate(fixture.entry, fixture.plan, "synthetic-plan-hash")
        self.assertEqual(len(called), 1)
        result = json.loads((fixture.root / "results/runs/synthetic-full/scores.json").read_text())
        self.assertAlmostEqual(result["metrics"]["spearman"], -.6)
        self.assertTrue(result["aggregated_from_shards"])
        self.assertTrue(result["full_planned_primary_metrics_valid"])
        self.assertEqual(result["full_test_id_union_validation"]["unique_observed_case_count"], 4)


if __name__ == "__main__":
    unittest.main()
