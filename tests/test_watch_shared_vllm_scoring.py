"""Synthetic CPU coordinator tests; no inference or biological records."""
import json
from pathlib import Path
import sys
import tempfile
import unittest

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
import shared_vllm_scoring as scoring
import watch_shared_vllm_scoring as watcher


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value))


class WatcherTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.full = {"run_id": "synthetic-full"}
        self.source = {"run_id": "synthetic-source"}
        save(self.root / "full.json", self.full)
        save(self.root / "source.json", self.source)
        self.spec = {"task_id": "P07", "project_root": str(self.root), "full_config_file": "full.json",
                     "full_config_sha256": scoring.file_sha(self.root / "full.json"),
                     "sources": [{"config_file": "source.json", "config_sha256": scoring.file_sha(self.root / "source.json")}]}
        self.spec_path = self.root / "spec.json"
        self.plan_path = self.root / "watch.json"
        self.state_path = self.root / "state.json"
        self.refresh_plan()

    def refresh_plan(self):
        save(self.spec_path, self.spec)
        files = [Path(watcher.__file__), Path(scoring.__file__), SCRIPTS / "shared_vllm_resume.py"]
        self.plan = {"schema_version": 1, "spec_files": [{"path": str(self.spec_path), "sha256": scoring.file_sha(self.spec_path)}],
                     "code_files_sha256": {str(p.resolve()): scoring.file_sha(p) for p in files},
                     "state_file": str(self.state_path), "poll_seconds": 20}
        save(self.plan_path, self.plan)
        self.plan_sha = scoring.file_sha(self.plan_path)

    def close_generation(self):
        folder = self.root / "results/runs/synthetic-source"
        save(folder / "shared_vllm_amendment.json", {"synthetic": True})
        save(folder / "shared_vllm_generation_completion.json", {"synthetic": True})

    def test_waits_for_distinct_shared_generation_terminal_marker(self):
        save(self.root / "results/runs/synthetic-source/shared_vllm_amendment.json", {"synthetic": True})
        calls = []
        state, _ = watcher.cycle(self.plan_path, self.plan_sha, score_function=lambda spec: calls.append(spec))
        self.assertEqual(calls, [])
        self.assertEqual(state["tasks"][str(self.spec_path)]["stage"], "pending")
        self.close_generation()
        state, _ = watcher.cycle(self.plan_path, self.plan_sha, score_function=lambda spec: {"state": "completed"})
        self.assertTrue(state["all_completed"])

    def test_completed_native_call_is_not_repeated(self):
        self.close_generation()
        calls = []
        def score(spec):
            calls.append(spec)
            return {"state": "completed"}
        watcher.cycle(self.plan_path, self.plan_sha, score_function=score)
        watcher.cycle(self.plan_path, self.plan_sha, score_function=score)
        self.assertEqual(len(calls), 1)

    def test_failed_native_call_is_preserved_without_retry(self):
        self.close_generation()
        calls = []
        def score(spec):
            calls.append(spec)
            raise scoring.ScoringError("synthetic native failure")
        state, _ = watcher.cycle(self.plan_path, self.plan_sha, score_function=score)
        self.assertTrue(state["all_terminal"])
        self.assertFalse(state["all_completed"])
        watcher.cycle(self.plan_path, self.plan_sha, score_function=score)
        self.assertEqual(len(calls), 1)

    def test_active_producer_can_be_rechecked_without_a_native_attempt(self):
        self.close_generation()
        def pending(spec):
            raise scoring.Pending("worker still flushing")
        state, _ = watcher.cycle(self.plan_path, self.plan_sha, score_function=pending)
        self.assertFalse(state["all_terminal"])
        state, _ = watcher.cycle(self.plan_path, self.plan_sha, score_function=lambda spec: {"state": "completed"})
        self.assertTrue(state["all_completed"])

    def test_running_legacy_native_aggregate_defers_new_invocation(self):
        status = self.root / "legacy-status.json"
        save(status, {"synthetic-task": {"stage": "running"}})
        self.spec["legacy_aggregation_watch"] = {"status_file": str(status), "names": ["synthetic-task"]}
        self.refresh_plan()
        self.close_generation()
        calls = []
        state, _ = watcher.cycle(self.plan_path, self.plan_sha, score_function=lambda spec: calls.append(spec))
        self.assertEqual(calls, [])
        self.assertEqual(state["tasks"][str(self.spec_path)]["reason"], "legacy_native_aggregation_running")

    def test_code_or_spec_change_is_rejected(self):
        self.spec["task_id"] = "P08"
        save(self.spec_path, self.spec)
        with self.assertRaisesRegex(scoring.ScoringError, "specification changed"):
            watcher.cycle(self.plan_path, self.plan_sha)

    def test_generation_override_waits_for_fork_not_terminal_parent(self):
        save(self.root / "results/runs/synthetic-source/completion.json", {"generation_exit_code": -9})
        fork = self.root / "results/runs/synthetic-source_continuation"
        save(fork / "shared_vllm_amendment.json", {"synthetic": True})
        self.spec["sources"][0]["generation_folder"] = str(fork)
        self.refresh_plan()
        calls = []
        state, _ = watcher.cycle(self.plan_path, self.plan_sha, score_function=lambda spec: calls.append(spec))
        self.assertEqual(calls, [])
        self.assertIn("shared_generation_pending", state["tasks"][str(self.spec_path)]["reason"])


if __name__ == "__main__":
    unittest.main()
