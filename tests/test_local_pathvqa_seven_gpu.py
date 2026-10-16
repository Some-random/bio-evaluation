"""Synthetic-only exact routing, terminal raw locks and one global VQA scorer."""
import contextlib
import copy
import io
import json
from pathlib import Path
import shutil
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import aggregate_local_pathvqa_seven_gpu as aggregate
import execute_local_pathvqa_seven_gpu as execute
import prepare_local_pathvqa_seven_gpu as prep
import prepare_pathvqa_native as native
import score_local_pathvqa as scorer
from test_pathvqa_native import image_bytes


class PathVQASevenGPU(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        original = json.loads((prep.ROOT / prep.ORIGINAL_CONFIG).read_text())
        original.update(run_id="synthetic_original", input_file="synthetic/inputs.jsonl", review_file="synthetic/review.json",
                        scorer_reference_file="synthetic/labels.jsonl")
        image = image_bytes("red")
        self.cases = [native.model_case(i, {"question": "Synthetic image question?", "image": {"bytes": image}}) for i in range(13)]
        references = []
        for index, case in enumerate(self.cases):
            group, answer = ("OPEN", "alpha beta") if index == 0 else ("CLOSED", "yes" if index % 2 else "no")
            references.append({**{key: case[key] for key in ["task", "case_id", "variant", "split"]},
                               "answer_type": group, "target_answer": answer, "image_sha256": native.sha(image)})
        prep.write_new(self.root / original["input_file"], self.cases, True)
        prep.write_new(self.root / original["review_file"], {"approved_case_ids": [case["case_id"] for case in self.cases], "held_cases": []})
        prep.write_new(self.root / original["scorer_reference_file"], references, True)
        original["scorer_reference_sha256"] = prep.file_digest(self.root / original["scorer_reference_file"])
        dependencies = [prep.RUNNER, prep.SCORER, prep.PREPARER, prep.EXECUTOR, prep.AGGREGATOR,
                        "scripts/prepare_pathvqa_native.py", "scripts/run_local_labbench_multimodal.py",
                        *[row["path"] for row in native.scoring_sources()]]
        for name in dependencies:
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(prep.ROOT / name, path)
        original["frozen_files_sha256"] = {name: prep.file_digest(self.root / name) for name in [original["input_file"], original["review_file"], *dependencies]}
        prep.write_new(self.root / prep.ORIGINAL_CONFIG, original)
        self.original = original
        self.original_bytes = (self.root / prep.ORIGINAL_CONFIG).read_bytes()
        self.patches = [mock.patch.object(prep, "SHARD_SIZE", 2), mock.patch.object(aggregate, "SHARD_SIZE", 2),
                        mock.patch.object(aggregate, "ROOT", self.root), mock.patch.object(execute, "ROOT", self.root)]
        for patch in self.patches:
            patch.start()
            self.addCleanup(patch.stop)
        self.prepared = prep.prepare(self.root, expected_cases=13)
        self.plan = json.loads((self.root / prep.PLAN).read_text())

    def approve(self):
        path = self.root / prep.APPROVAL
        gate = json.loads(path.read_text())
        gate["approved"] = True
        prep.runner.write_json(path, gate)

    def terminal_shards(self, missing_last=False):
        self.approve()
        for item in self.plan["shards"]:
            config_path = self.root / item["config_file"]
            settings = json.loads(config_path.read_text())
            cases = prep.cases_for(self.root, settings)
            folder = self.root / "results/runs" / item["run_id"]
            gpu = settings["gpu_ids"][0]
            server = {"model": settings["model"], "revision": settings["model_revision"],
                      "gpu_ids": [gpu], "pid": 1000 + gpu, "proc_start_ticks": str(8000 + gpu)}
            serving = {"model": settings["model"], "revision": settings["model_revision"], "gpu_ids": [gpu],
                       "host": "127.0.0.1", "port": dict(prep.REPLICAS)[gpu]}
            prep.runner.write_json(folder / "run_manifest.json", {"configuration": settings, "configuration_sha256": item["config_sha256"],
                "runner_sha256": prep.RUNNER_SHA256, "case_contract_sha256": prep.digest(cases), "planned_cases": len(cases),
                "model_selection_on_test": False, "solver_tools": [], "answer_keys_available_to_solver": False,
                "server": server, "serving_configuration": serving})
            missing = False
            for case in cases:
                index = self.cases.index(case)
                if missing_last and index == 12:
                    missing = True
                    continue
                request = prep.runner.request_record(case, settings)
                identity = prep.digest([case["task"], case["variant"], case["case_id"]]) + ".json"
                prep.runner.write_json(folder / "requests" / identity, request)
                text = "alpha alpha" if index == 0 else "yes" if index in [1, 2] else "no" if index % 2 == 0 else "yes"
                raw = {"model": settings["model"], "choices": [{"message": {"content": text}, "finish_reason": "stop"}], "usage": {}}
                prep.runner.write_json(folder / "responses" / identity, {**{key: case[key] for key in ["task", "case_id", "variant", "split"]},
                    "model": settings["model"], "model_revision": settings["model_revision"], "request_sha256": request["request_sha256"],
                    "status": "completed", "http_status": 200, "text": text, "finish_reason": "stop", "response": raw})
            prep.raw_audit(self.root, folder, cases, settings, item["config_sha256"])
            prep.runner.write_json(folder / "completion.json", {"configuration_sha256": item["config_sha256"],
                "run_manifest_sha256": prep.file_digest(folder / "run_manifest.json"), "runner_sha256": prep.RUNNER_SHA256,
                "generation_output_lock_sha256": prep.file_digest(folder / "generation_output_lock.json"),
                "executor_sha256": prep.file_digest(self.root / prep.EXECUTOR), "generation_exit_code": 1 if missing else 0,
                "generation_audit_exit_code": 0, "scoring_exit_code": None, "shard_scoring_performed": False,
                "case_scope": "task_shard_only", "planned": len(cases), "shard_index": settings["shard_index"], "shard_count": len(self.plan["shards"])})

    def test_exact_payloads_images_seven_routes_and_originals_preserved(self):
        self.assertEqual(self.prepared["shard_case_counts"], [2] * 6 + [1])
        self.assertEqual((self.root / prep.ORIGINAL_CONFIG).read_bytes(), self.original_bytes)
        self.assertFalse((self.root / "results/runs/synthetic_original").exists())
        groups = []
        for index, item in enumerate(self.plan["shards"]):
            settings = json.loads((self.root / item["config_file"]).read_text())
            cases = prep.cases_for(self.root, settings)
            self.assertEqual(settings["gpu_ids"], [index + 1])
            for case in cases:
                self.assertEqual(prep.original_runner.request_record(case, self.original), prep.runner.request_record(case, settings))
            groups.append(cases)
        self.assertTrue(prep.ordered_union(self.cases, groups)["complete"])
        full = json.loads((self.root / prep.FULL_CONFIG).read_text())
        self.assertNotIn("gpu_ids", full)
        self.assertEqual(full["paper_comparison"], self.original["paper_comparison"])

    def test_disabled_gate_calls_neither_generation_nor_scorer(self):
        with mock.patch.object(execute.subprocess, "run") as run:
            with self.assertRaisesRegex(ValueError, "disabled"):
                execute.execute(self.root / self.plan["shards"][0]["config_file"])
            with self.assertRaisesRegex(ValueError, "disabled"):
                aggregate.aggregate(self.plan, prep.file_digest(self.root / prep.PLAN))
            run.assert_not_called()

    def test_original_started_even_empty_directory_rejects_migration(self):
        self.approve()
        (self.root / "results/runs/synthetic_original").mkdir(parents=True)
        with self.assertRaisesRegex(ValueError, "never migrate"):
            prep.require_approval(self.root)

    def test_global_native_metrics_once_missing_slots_and_real_servers(self):
        self.terminal_shards(missing_last=True)
        def score_once(command, cwd):
            self.assertEqual(command[-2:], ["--run", self.plan["aggregate_run_id"]])
            with mock.patch.object(scorer, "ROOT", self.root), contextlib.redirect_stdout(io.StringIO()):
                scorer.score(self.root / "results/runs" / self.plan["aggregate_run_id"])
            return SimpleNamespace(returncode=0)
        with mock.patch.object(aggregate.subprocess, "run", side_effect=score_once) as run:
            done = aggregate.aggregate(self.plan, prep.file_digest(self.root / prep.PLAN))
            aggregate.aggregate(self.plan, prep.file_digest(self.root / prep.PLAN))
            run.assert_called_once()
        folder = self.root / "results/runs" / self.plan["aggregate_run_id"]
        result = json.loads((folder / "scores.json").read_text())
        self.assertAlmostEqual(result["metrics"]["open_token_recall"], 2 / 3)
        self.assertAlmostEqual(result["metrics"]["closed_accuracy_corrected"], 10 / 12)
        self.assertAlmostEqual(result["separate_diagnostics"]["closed_bug_compatible_accuracy"], 10 / 11)
        self.assertEqual(result["missing_or_failed_outputs"], 1)
        self.assertEqual(result["metrics_by_answer_type"]["CLOSED"]["eligible"], 12)
        self.assertTrue(result["full_test_id_union_validation"]["complete"])
        self.assertEqual(done["generation_exit_code"], 1)
        self.assertEqual(done["status"], "completed_with_generation_failures")
        self.assertEqual(result["parallel_gpu_metadata"]["gpu_ids"], list(range(1, 8)))
        manifest = json.loads((folder / "run_manifest.json").read_text())
        self.assertNotIn("server", manifest)
        self.assertNotIn("gpu_ids", manifest["configuration"])
        with mock.patch.object(execute.subprocess, "run") as run:
            with self.assertRaisesRegex(ValueError, "Terminal shard"):
                execute.execute(self.root / self.plan["shards"][0]["config_file"])
            run.assert_not_called()

    def test_terminal_raw_mutation_and_missing_slot_appearance_block(self):
        self.terminal_shards(missing_last=True)
        item = self.plan["shards"][-1]
        settings = json.loads((self.root / item["config_file"]).read_text())
        folder = self.root / "results/runs" / item["run_id"]
        case = self.cases[-1]
        identity = prep.digest([case["task"], case["variant"], case["case_id"]]) + ".json"
        prep.runner.write_json(folder / "requests" / identity, prep.runner.request_record(case, settings))
        with self.assertRaisesRegex(ValueError, "Locked raw generation"):
            aggregate.validate(self.plan)

    def test_executor_preserves_failure_codes_and_terminal_hashes(self):
        self.approve()
        item = self.plan["shards"][0]
        with mock.patch.object(execute.subprocess, "run", return_value=SimpleNamespace(returncode=7)):
            self.assertEqual(execute.execute(self.root / item["config_file"]), 7)
        done = json.loads((self.root / "results/runs" / item["run_id"] / "completion.json").read_text())
        self.assertEqual(done["generation_exit_code"], 7)
        self.assertIsNone(done["generation_audit_exit_code"])
        self.assertIsNone(done["scoring_exit_code"])
        self.assertEqual(done["configuration_sha256"], item["config_sha256"])
        with self.assertRaisesRegex(ValueError, "unauditable"):
            aggregate.validate(self.plan)

    def test_failed_single_native_scorer_never_reinvoked(self):
        self.terminal_shards()
        with mock.patch.object(aggregate.subprocess, "run", return_value=SimpleNamespace(returncode=9)) as run:
            with self.assertRaisesRegex(ValueError, "Single original full native scorer failed"):
                aggregate.aggregate(self.plan, prep.file_digest(self.root / prep.PLAN))
            with self.assertRaisesRegex(ValueError, "no rescoring"):
                aggregate.aggregate(self.plan, prep.file_digest(self.root / prep.PLAN))
            run.assert_called_once()
        done = json.loads((self.root / "results/runs" / self.plan["aggregate_run_id"] / "completion.json").read_text())
        self.assertEqual(done["scoring_exit_code"], 9)
        self.assertEqual(done["generation_exit_code"], 0)


if __name__ == "__main__":
    unittest.main()
