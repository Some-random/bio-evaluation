"""Synthetic native384-class scoring, exact approval and global union contracts."""
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
import aggregate_local_reaction_shards as aggregate
import execute_local_reaction_shard as execute
import prepare_local_reaction_shards as prepare
import run_local_labbench_multimodal as runner
import score_local_reaction as scorer
from prepare_local_extended_shards import shard_metadata, ordered_union
from check_reaction_context import input_ids


def save(path, value, jsonl=False):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(row) + "\n" for row in value) if jsonl else json.dumps(value))


class SyntheticReactionShards:
    def __init__(self, root):
        self.root = root
        generation = {"max_tokens": 4096, "temperature": 1., "top_p": .95, "top_k": 20, "seed": 42,
                      "n": 1, "chat_template_kwargs": {"enable_thinking": True, "reasoning_effort": "medium"}}
        self.full = {"run_id": "synthetic-full", "model": "synthetic-model", "model_revision": "synthetic-revision",
                     "checkpoint_precision": "synthetic-BF16", "generation": generation, "concurrency": 4,
                     "variant": "SYNTHETIC", "model_facing_fields": ["sequence", "objective"], "prompt_policy": "fixed artificial prompt",
                     "approved_task_ids": ["P16"], "scorer_reference_file": "refs.jsonl", "input_file": "inputs.jsonl", "review_file": "review.json",
                     "aggregate_only": True, "generator_execution_allowed": False, "endpoint": "aggregate-only://offline",
                     "execution_authorized": False, "input_review_complete": True, "shard_plan_file": "plan.json",
                     "execution_approval_file": prepare.APPROVAL_FILE,
                     "shard_count": 2, "full_test_case_count": 4, "shard_size": 3, "runner": prepare.RUNNER}
        self.cases = [{"task": "P16", "case_id": str(i), "variant": "SYNTHETIC", "split": "synthetic",
                       "messages": [{"role": "user", "content": "Artificial sequence example " + str(i)}]} for i in range(4)]
        save(root / "inputs.jsonl", self.cases, True)
        save(root / "review.json", {"approved_case_ids": [str(i) for i in range(4)], "held_cases": []})
        save(root / "refs.jsonl", [{"task": "P16", "case_id": str(i), "target": [0, 383, 17, 18][i]} for i in range(4)], True)
        self.full["scorer_reference_sha256"] = prepare.file_digest(root / "refs.jsonl")
        (root / prepare.RUNNER).parent.mkdir(parents=True, exist_ok=True)
        (root / prepare.RUNNER).write_text("# synthetic pinned runner\n")
        self.full["frozen_files_sha256"] = {name: prepare.file_digest(root / name) for name in ["inputs.jsonl", "review.json", prepare.RUNNER]}
        save(root / "recipe.json", self.full)
        entries = []
        for index in range(2):
            gpu, port = prepare.REPLICAS[index]
            start, stop = index * 3, min((index + 1) * 3, 4)
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
                        "case_contract_sha256": prepare.canonical_digest(cases), "model_selection_on_test": False,
                        "solver_tools": [], "answer_keys_available_to_solver": False, "server": server,
                        "serving_configuration": {"host": "127.0.0.1", "port": port, "gpu_ids": [gpu], "model": shard["model"], "revision": shard["model_revision"]}}
            save(folder / "run_manifest.json", manifest)
            for case in cases:
                identity = prepare.canonical_digest([case["task"], case["variant"], case["case_id"]])
                request = runner.request_record(case, shard)
                save(folder / "requests" / (identity + ".json"), request)
                text = ["0", "383", "17 or 18", "18"][int(case["case_id"]) ]
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
                 "scores_sha256": prepare.file_digest(folder / "scores.json"), "case_scope": "task_shard_only", **shard_metadata(shard)})
            entries.append({"config_file": config_name, "config_sha256": config_hash, "run_id": shard["run_id"],
                            "shard_index": index, "gpu_ids": [gpu], "endpoint": shard["endpoint"], "cases": len(cases)})
        self.full["shard_configs"] = entries
        save(root / "aggregate.json", self.full)
        self.entry = {"task_id": "P16", "aggregate_config_file": "aggregate.json", "aggregate_config_sha256": prepare.file_digest(root / "aggregate.json"),
                      "aggregate_run_id": "synthetic-full", "full_test_case_count": 4, "shards": entries}
        self.plan = {"source_recipe_file": "recipe.json", "source_recipe_sha256": prepare.file_digest(root / "recipe.json"), "tasks": [self.entry]}

        save(root / "plan.json", self.plan)
        self.approval = {"execution_authorized": True, "plan_sha256": prepare.file_digest(root / "plan.json"),
                         "model": self.full["model"], "model_revision": self.full["model_revision"],
                         "generation_sha256": prepare.canonical_digest(self.full["generation"]), "approved_task_ids": ["P16"],
                         "approved_config_sha256": {item["config_file"]: item["config_sha256"] for item in entries}}
        save(root / prepare.APPROVAL_FILE, self.approval)
        with patch.object(prepare, "ROOT", root):
            for item in entries:
                settings = json.loads((root / item["config_file"]).read_text())
                path = root / "results/runs" / item["run_id"] / "completion.json"
                completion = json.loads(path.read_text())
                completion["execution_approval"] = prepare.approval_for(root / item["config_file"], settings)
                save(path, completion)


class ReactionRunTests(unittest.TestCase):
    def fixture(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        return SyntheticReactionShards(Path(temporary.name))

    def test_global_accuracy_keeps_original_all_case_denominator(self):
        fixture = self.fixture()
        calls = []
        def score_command(command, cwd):
            calls.append(command)
            self.assertIn("score_local_reaction.py", command[2])
            with patch.object(scorer, "ROOT", fixture.root), contextlib.redirect_stdout(io.StringIO()):
                scorer.score(fixture.root / "results/runs/synthetic-full")
            return SimpleNamespace(returncode=0)
        with patch.object(aggregate, "ROOT", fixture.root), patch.object(aggregate, "SHARD_SIZE", 3), patch.object(prepare, "ROOT", fixture.root), patch.object(aggregate.subprocess, "run", score_command):
            aggregate.aggregate(fixture.entry, fixture.plan, "synthetic-plan-sha")
            aggregate.aggregate(fixture.entry, fixture.plan, "synthetic-plan-sha")
        self.assertEqual(len(calls), 1)
        folder = fixture.root / "results/runs/synthetic-full"
        scores = json.loads((folder / "scores.json").read_text())
        self.assertEqual((scores["planned"], scores["completed"], scores["parsed"], scores["invalid_outputs"]), (4, 4, 3, 1))
        self.assertEqual(scores["metrics"]["accuracy"], .75)
        self.assertEqual(scores["case_scope"], "full_frozen_reviewed_ProtST_Reaction_test")
        self.assertIsNone(scores["explanation_support_score"])
        self.assertEqual(scores["full_test_id_union_validation"]["unique_observed_case_count"], 4)
        changed = copy.deepcopy(scores); changed["metrics"]["accuracy"] = 999
        save(folder / "scores.json", changed)
        with patch.object(aggregate, "ROOT", fixture.root), patch.object(aggregate, "SHARD_SIZE", 3), patch.object(prepare, "ROOT", fixture.root):
            with self.assertRaisesRegex(ValueError, "score/manifest hash changed"):
                aggregate.aggregate(fixture.entry, fixture.plan, "synthetic-plan-sha")

    def test_predictions_lock_before_reference_hash_failure(self):
        fixture = self.fixture()
        folder = fixture.root / "results/runs/synthetic-shard0"
        with (fixture.root / "refs.jsonl").open("a") as handle: handle.write(" ")
        with patch.object(scorer, "ROOT", fixture.root), self.assertRaisesRegex(ValueError, "reference changed"):
            scorer.score(folder)
        self.assertTrue((folder / "scoring_output_lock.json").exists())

    def test_prospective_config_requires_exact_approval_and_aggregate_cannot_dispatch(self):
        fixture = self.fixture()
        settings = json.loads((fixture.root / "shard0.json").read_text())
        with patch.object(prepare, "ROOT", fixture.root):
            self.assertIn("approval_sha256", prepare.approval_for(fixture.root / "shard0.json", settings))
            bad = {**fixture.approval, "model_revision": "different"}
            save(fixture.root / prepare.APPROVAL_FILE, bad)
            with self.assertRaisesRegex(ValueError, "No exact-plan"):
                prepare.approval_for(fixture.root / "shard0.json", settings)
        with self.assertRaises(ValueError): runner.validate_endpoint(fixture.full["endpoint"])
        with self.assertRaisesRegex(ValueError, "Only executable"):
            execute.execute(fixture.root / "aggregate.json")

    def test_missing_duplicate_order_and_recipe_changes_rejected(self):
        cases = [{"case_id": str(i)} for i in range(4)]
        for groups in [[cases[:2], cases[1:]], [cases[:2], cases[3:]], [cases[2:], cases[:2]]]:
            with self.assertRaises(ValueError): ordered_union(cases, groups)
        fixture = self.fixture()
        with self.assertRaisesRegex(ValueError, "recipe mismatch"):
            aggregate.validate_recipe(fixture.full, {**fixture.full, "generation": {"n": 2}}, fixture.full)

    def test_tokenizer_schema_counts_ids_instead_of_mapping_keys(self):
        self.assertEqual(len(input_ids({"input_ids": [1, 2, 3], "attention_mask": [1, 1, 1]})), 3)
        self.assertEqual(len(input_ids({"input_ids": [[1, 2, 3]]})), 3)
        self.assertEqual(input_ids([1, 2]), [1, 2])
        with self.assertRaises(ValueError): input_ids({"input_ids": [[1], [2]]})


if __name__ == "__main__":
    unittest.main()
