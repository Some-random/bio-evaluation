"""Synthetic migration tests: immutable history and unchanged all-case scoring."""
import copy
import fcntl
import importlib.util
import json
from pathlib import Path
import shutil
import sys
import tempfile
from types import SimpleNamespace
import unittest

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
import shared_vllm_scoring as mod


def save(path, value, jsonl=False):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(row) + "\n" for row in value) if jsonl else json.dumps(value))


class Fixture:
    def __init__(self, root):
        self.root = root
        self.runner_name = "scripts/run_local_labbench_multimodal.py"
        self.scorer_name = "scripts/score_local_catalog_extended.py"
        for name in (self.runner_name, self.scorer_name):
            path = root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(SCRIPTS / Path(name).name, path)
        self.cases = [{"task": "P03", "case_id": "artificial-" + str(i), "variant": "SYNTHETIC",
                       "split": "synthetic", "messages": [{"role": "user", "content": "Artificial input " + str(i)}]} for i in range(4)]
        save(root / "inputs.jsonl", self.cases, True)
        save(root / "review.json", {"approved_case_ids": [c["case_id"] for c in self.cases], "held_cases": []})
        save(root / "references.jsonl", [{"task": "P03", "case_id": c["case_id"], "target": i} for i, c in enumerate(self.cases)], True)
        self.full = {"run_id": "artificial-full", "approved_task_ids": ["P03"], "model": "synthetic-model",
                     "model_revision": "synthetic-revision", "checkpoint_precision": "BF16", "variant": "SYNTHETIC",
                     "runner": self.runner_name, "input_file": "inputs.jsonl", "review_file": "review.json",
                     "scorer_reference_file": "references.jsonl", "scorer_reference_sha256": mod.file_sha(root / "references.jsonl"),
                     "generation": {"max_tokens": 4096, "temperature": 1., "top_p": .95, "top_k": 20, "seed": 42, "n": 1,
                                    "chat_template_kwargs": {"enable_thinking": True, "reasoning_effort": "medium"}},
                     "model_facing_fields": ["artificial_input"], "concurrency": 4, "full_test_case_count": 4,
                     "tool_access": [], "frozen_files_sha256": {}}
        self.full["frozen_files_sha256"] = {name: mod.file_sha(root / name) for name in
                                           (self.runner_name, self.scorer_name, "inputs.jsonl", "review.json")}
        save(root / "full.json", self.full)
        self.sources = []
        for index in range(2):
            cases = self.cases[index * 2:(index + 1) * 2]
            cfg = copy.deepcopy(self.full)
            cfg.update(run_id="artificial-source-" + str(index), input_file=f"inputs-{index}.jsonl", review_file=f"review-{index}.json")
            save(root / cfg["input_file"], cases, True)
            save(root / cfg["review_file"], {"approved_case_ids": [c["case_id"] for c in cases], "held_cases": []})
            cfg["frozen_files_sha256"].update({name: mod.file_sha(root / name) for name in (cfg["input_file"], cfg["review_file"])})
            cfg_path = root / f"source-{index}.json"
            save(cfg_path, cfg)
            folder = root / "results/runs" / cfg["run_id"]
            runner = mod.load_frozen_runner(root, cfg)
            for i, case in enumerate(cases):
                name = mod.digest([case["task"], case["variant"], case["case_id"]]) + ".json"
                request = runner.request_record(case, cfg)
                save(folder / "requests" / name, request)
                # Last artificial case has an ambiguous old request and no answer.
                if index == 1 and i == 1:
                    continue
                text = str(i) if index == 0 else "invalid artificial output"
                raw = {"model": cfg["model"], "choices": [{"message": {"content": text}, "finish_reason": "stop"}]}
                response = {**{k: case[k] for k in ("task", "case_id", "variant", "split")},
                            "model": cfg["model"], "model_revision": cfg["model_revision"],
                            "request_sha256": request["request_sha256"], "status": "completed", "http_status": 200,
                            "response": raw, "text": text, "finish_reason": "stop"}
                save(folder / "responses" / name, response)
            server = {"model": cfg["model"], "revision": cfg["model_revision"], "pid": 123, "proc_start_ticks": "456"}
            manifest = {"configuration": cfg, "configuration_sha256": mod.file_sha(cfg_path),
                        "case_contract_sha256": mod.digest(cases), "planned_cases": len(cases),
                        "runner_sha256": cfg["frozen_files_sha256"][cfg["runner"]], "solver_tools": [],
                        "answer_keys_available_to_solver": False, "model_selection_on_test": False,
                        "server": server, "serving_configuration": server}
            save(folder / "run_manifest.json", manifest)
            if index == 0:
                raw_hashes, _ = mod.validate_raw(root, cfg, cases, folder)
                locked = {"run_manifest.json": mod.file_sha(folder / "run_manifest.json"), **raw_hashes}
                save(folder / "scoring_output_lock.json", {"files_sha256": locked, "contract_sha256": mod.digest(locked)})
                save(folder / "scores.json", {"planned": 2, "completed": 2})
                save(folder / "completion.json", {"configuration_sha256": mod.file_sha(cfg_path), "scoring_exit_code": 0,
                     "run_manifest_sha256": mod.file_sha(folder / "run_manifest.json"), "scores_sha256": mod.file_sha(folder / "scores.json")})
            else:
                save(folder / "shared_vllm_amendment.json", {"synthetic": True})
                save(folder / "shared_vllm_generation_completion.json", {"synthetic": True})
            self.sources.append({"config_file": cfg_path.name, "config_sha256": mod.file_sha(cfg_path)})
        self.spec = {"task_id": "P03", "project_root": str(root), "full_config_file": "full.json",
                     "full_config_sha256": mod.file_sha(root / "full.json"), "sources": self.sources,
                     "scorer_file": self.scorer_name, "scorer_sha256": mod.file_sha(root / self.scorer_name), "python": sys.executable}
        self.validator_calls = []

    def validator(self, folder, cfg, cases, *, require_terminal):
        self.validator_calls.append((folder, cfg, cases, require_terminal))
        return {"schema_version": 1, "all_saved_responses_verified": True, "actual_servers": [{"synthetic": True}]}


class ScoringMigrationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.fixture = Fixture(self.root)

    def test_unchanged_native_scorer_retains_invalid_and_ambiguous_cases(self):
        before = {str(p.relative_to(self.root)): mod.file_sha(p) for p in self.root.rglob("*.json")}
        result = mod.score_spec(self.fixture.spec, validator=self.fixture.validator)
        self.assertEqual(result["state"], "completed")
        folder = self.root / "results/runs/artificial-full"
        scores = mod.read(folder / "scores.json")
        self.assertEqual(scores["planned"], 4)
        self.assertEqual(scores["completed"], 3)
        self.assertEqual(scores["metrics"]["accuracy"], .5)
        self.assertEqual(scores["invalid_outputs"], 1)
        self.assertEqual(scores["statuses"]["interrupted_unknown_completion"], 1)
        self.assertEqual(mod.read(folder / "run_manifest.json")["runner_role"], "offline_scoring_view_builder")
        self.assertEqual(len(self.fixture.validator_calls), 1)
        self.assertTrue(self.fixture.validator_calls[0][-1])
        for name, sha in before.items():
            self.assertEqual(mod.file_sha(self.root / name), sha, name)
        score_sha = mod.file_sha(folder / "scores.json")
        self.assertEqual(mod.score_spec(self.fixture.spec)["state"], "existing_completed_unchanged")
        self.assertEqual(mod.file_sha(folder / "scores.json"), score_sha)

    def test_duplicate_source_is_rejected_before_scoring(self):
        self.fixture.spec["sources"] = [self.fixture.sources[0], self.fixture.sources[0]]
        with self.assertRaisesRegex(mod.ScoringError, "multiple source"):
            mod.score_spec(self.fixture.spec, validate_only=True, validator=self.fixture.validator)
        self.assertFalse((self.root / "results/runs/artificial-full").exists())

    def test_incomplete_union_is_rejected(self):
        self.fixture.spec["sources"] = self.fixture.sources[:1]
        with self.assertRaisesRegex(mod.ScoringError, "complete native case"):
            mod.score_spec(self.fixture.spec, validate_only=True, validator=self.fixture.validator)

    def test_changed_prompt_is_rejected_even_with_positive_segment_proof(self):
        folder = self.root / "results/runs/artificial-source-1"
        path = next((folder / "requests").glob("*.json"))
        record = mod.read(path)
        record["payload"]["messages"][0]["content"] = "Altered synthetic request"
        record["request_sha256"] = mod.digest(record["payload"])
        save(path, record)
        with self.assertRaisesRegex(mod.ScoringError, "original prompt"):
            mod.score_spec(self.fixture.spec, validate_only=True, validator=self.fixture.validator)

    def test_historical_terminal_score_cannot_change(self):
        save(self.root / "results/runs/artificial-source-0/scores.json", {"changed": True})
        with self.assertRaisesRegex(mod.ScoringError, "terminal artifact"):
            mod.score_spec(self.fixture.spec, validate_only=True, validator=self.fixture.validator)

    def test_different_generation_budget_is_not_a_throughput_amendment(self):
        path = self.root / "source-1.json"
        cfg = mod.read(path)
        cfg["generation"]["max_tokens"] = 8192
        save(path, cfg)
        self.fixture.spec["sources"][1]["config_sha256"] = mod.file_sha(path)
        with self.assertRaisesRegex(mod.ScoringError, "generation/reference recipe differs"):
            mod.score_spec(self.fixture.spec, validate_only=True, validator=self.fixture.validator)

    def test_segment_provenance_failure_cannot_be_bypassed(self):
        def rejected(*args, **kwargs):
            return {"all_saved_responses_verified": False}
        with self.assertRaisesRegex(mod.ScoringError, "provenance is not verified"):
            mod.score_spec(self.fixture.spec, validate_only=True, validator=rejected)

    def test_cpu_runtime_receipt_is_pinned_and_hides_gpus(self):
        receipt = self.root / "runtime-receipt.json"
        save(receipt, {"state": "ready", "python": sys.executable, "python_sha256": mod.file_sha(sys.executable),
                       "observed_versions": {"visible_gpu_count": 0},
                       "environment": {"CUDA_VISIBLE_DEVICES": "", "OMP_NUM_THREADS": "1"}})
        spec = {**self.fixture.spec, "runtime_receipt_file": str(receipt), "runtime_receipt_sha256": mod.file_sha(receipt)}
        environment = mod.native_environment(spec)
        self.assertEqual(environment["CUDA_VISIBLE_DEVICES"], "")
        self.assertEqual(environment["OMP_NUM_THREADS"], "1")
        save(receipt, {"changed": True})
        with self.assertRaisesRegex(mod.ScoringError, "runtime receipt changed"):
            mod.native_environment(spec)

    def test_locked_partial_parent_is_preserved_while_audited_fork_supplies_remaining_response(self):
        cfg = mod.read(self.root / "source-1.json")
        cases = self.fixture.cases[2:]
        parent = self.root / "results/runs" / cfg["run_id"]
        raw_hashes, _ = mod.validate_raw(self.root, cfg, cases, parent)
        files = {"run_manifest.json": mod.file_sha(parent / "run_manifest.json"), **raw_hashes}
        save(parent / "scoring_output_lock.json", {"files_sha256": files, "contract_sha256": mod.digest(files)})
        save(parent / "scores.json", {"planned": 2, "completed": 1, "synthetic_partial": True})
        save(parent / "completion.json", {"generation_exit_code": -9, "scoring_exit_code": 0})
        before = {str(p.relative_to(parent)): mod.file_sha(p) for p in parent.rglob("*.json")}
        fork = parent.with_name(parent.name + "_continuation")
        for name in ("requests", "responses"):
            shutil.copytree(parent / name, fork / name)
        shutil.copyfile(parent / "run_manifest.json", fork / "run_manifest.json")
        marker = {"schema_version": 1, "logical_run_id": cfg["run_id"], "source_run_directory": str(parent),
                  "continuation_run_directory": str(fork), "source_files_sha256": before,
                  "source_scoring_output_lock_sha256": mod.file_sha(parent / "scoring_output_lock.json"),
                  "source_completion_sha256": mod.file_sha(parent / "completion.json"),
                  "source_scores_sha256": mod.file_sha(parent / "scores.json")}
        save(fork / "shared_vllm_fork_manifest.json", marker)
        save(fork / "shared_vllm_amendment.json", {"synthetic": True})
        save(fork / "shared_vllm_generation_completion.json", {"synthetic": True})
        case = cases[1]
        name = mod.digest([case["task"], case["variant"], case["case_id"]]) + ".json"
        request = mod.read(fork / "requests" / name)
        response = {**{k: case[k] for k in ("task", "case_id", "variant", "split")}, "model": cfg["model"],
                    "model_revision": cfg["model_revision"], "request_sha256": request["request_sha256"],
                    "status": "completed", "http_status": 200, "text": "3", "finish_reason": "stop",
                    "response": {"model": cfg["model"], "choices": [{"message": {"content": "3"}, "finish_reason": "stop"}]}}
        save(fork / "responses" / name, response)
        self.fixture.spec["sources"][1]["generation_folder"] = str(fork)
        def proof(folder, settings, checked_cases, *, require_terminal):
            self.assertEqual(folder, fork)
            return {"all_saved_responses_verified": True, "fork_manifest_sha256": mod.file_sha(fork / "shared_vllm_fork_manifest.json"),
                    "original_source_folder": str(parent),
                    "parent_scoring_output_lock_sha256": mod.file_sha(parent / "scoring_output_lock.json"),
                    "parent_completion_sha256": mod.file_sha(parent / "completion.json"),
                    "parent_scores_sha256": mod.file_sha(parent / "scores.json")}
        result = mod.score_spec(self.fixture.spec, validator=proof)
        self.assertEqual(result["state"], "completed")
        scores = mod.read(self.root / "results/runs/artificial-full/scores.json")
        self.assertEqual(scores["planned"], 4)
        self.assertEqual(scores["completed"], 4)
        self.assertEqual(scores["metrics"]["accuracy"], .75)
        for path, expected in before.items():
            self.assertEqual(mod.file_sha(parent / path), expected)
        self.assertFalse((parent / "responses" / name).exists())

    def test_alternate_generation_directory_requires_explicit_fork_proof(self):
        parent = self.root / "results/runs/artificial-source-0"
        fork = parent.with_name(parent.name + "_unaudited")
        shutil.copytree(parent, fork)
        self.fixture.spec["sources"][0]["generation_folder"] = str(fork)
        with self.assertRaisesRegex(mod.ScoringError, "not a shared continuation"):
            mod.score_spec(self.fixture.spec, validate_only=True, validator=self.fixture.validator)

    def test_active_worker_lock_defers_scoring(self):
        with (self.root / "results/runs/artificial-source-1/worker.lock").open("a") as handle:
            fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
            with self.assertRaisesRegex(mod.Pending, "still active"):
                mod.score_spec(self.fixture.spec, validate_only=True, validator=self.fixture.validator)

    def test_unclosed_shared_generation_is_pending(self):
        (self.root / "results/runs/artificial-source-1/shared_vllm_generation_completion.json").unlink()
        with self.assertRaisesRegex(mod.Pending, "not terminal"):
            mod.score_spec(self.fixture.spec, validate_only=True, validator=self.fixture.validator)

    def test_failed_native_invocation_is_never_retried(self):
        calls = []
        def fail(command, **kwargs):
            calls.append(command)
            return SimpleNamespace(returncode=9)
        with self.assertRaisesRegex(mod.ScoringError, "scorer failed"):
            mod.score_spec(self.fixture.spec, validator=self.fixture.validator, run_command=fail)
        with self.assertRaisesRegex(mod.ScoringError, "failed or its provenance"):
            mod.score_spec(self.fixture.spec, validator=self.fixture.validator, run_command=fail)
        self.assertEqual(len(calls), 1)

    def test_deepfri_scoring_view_changes_only_infrastructure_and_keeps_actual_runner(self):
        full = copy.deepcopy(self.fixture.full)
        actual = self.root / "scripts/actual_shared_generator.py"
        actual.write_text("# synthetic actual shared generator\n")
        source = {"run_id": "artificial-source-1"}
        manifest_path = self.root / "results/runs" / source["run_id"] / "run_manifest.json"
        manifest = mod.read(manifest_path)
        manifest["runner_sha256"] = mod.file_sha(actual)
        save(manifest_path, manifest)
        spec = {**self.fixture.spec, "execution_runner_file": str(actual), "execution_runner_sha256": mod.file_sha(actual)}
        view, path = mod.deepfri_view(self.root, full, spec, [source])
        self.assertEqual(view["generation"], full["generation"])
        self.assertEqual(view["scorer_reference_sha256"], full["scorer_reference_sha256"])
        self.assertEqual(view["input_file"], full["input_file"])
        self.assertEqual(view["run_id"], "artificial-full_shared_scoring")
        self.assertEqual(view["frozen_files_sha256"][view["runner"]], mod.file_sha(actual))
        self.assertTrue(path.exists())
        self.assertEqual(full, self.fixture.full)
        actual.write_text("# wrong runner\n")
        with self.assertRaisesRegex(mod.ScoringError, "execution adapter differs"):
            mod.deepfri_view(self.root, full, spec, [source])


if __name__ == "__main__":
    unittest.main()
