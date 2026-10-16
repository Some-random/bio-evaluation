from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import tempfile
import unittest


spec = importlib.util.spec_from_file_location("continuation_coordinator", Path(__file__).with_name("coordinator.py"))
coordinator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(coordinator)


class Process:
    def __init__(self, pid):
        self.pid = pid
        self.exit_code = None

    def poll(self):
        return self.exit_code


class CoordinatorTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.state = self.root / "state"
        self.run = self.root / "run"
        self.run.mkdir()
        self.state.mkdir()
        self.now = 0
        self.calls = []
        self.objects = []
        self.config = {"root": str(self.root), "state_dir": str(self.state), "run_dir": str(self.run),
            "planned_cases": 59, "files_sha256": {}, "restart_delay_seconds": 60,
            "children": {"reporting": ["watch_reporting.py", "--interval", "300"],
                "continuation_upload": ["upload_continuation.py", "--interval", "60"]},
            "scorer": {"launcher_relative": "score_python.sh", "script": "frozen_score_p36.py"}}

    def tearDown(self):
        for obj in self.objects:
            for child in obj.children.values():
                if child["log"] is not None:
                    child["log"].close()
            if obj.score_log is not None:
                obj.score_log.close()
        self.temp.cleanup()

    def popen(self, argv, **kwargs):
        process = Process(1000 + len(self.calls))
        self.calls.append((argv, kwargs, process))
        return process

    def make(self):
        obj = coordinator.Coordinator(self.config, self.root / "runtime", self.popen, lambda: self.now)
        self.objects.append(obj)
        return obj

    def dispatch(self):
        coordinator.save(self.run / "dispatch_summary.json", {"planned": 59, "finished": 59})

    def write_scores(self):
        coordinator.save(self.run / "scores.json", {"task_id": "P36", "planned": 59,
            "completed": 58, "full_benchmark_complete": False, "metrics": {"rougeL": 0.12},
            "case_scope": "PARTIAL_input_reviewed_first64_subset", "missing_or_failed_slots": 1})

    def test_children_restart_after_delay_and_never_invoke_generation(self):
        obj = self.make()
        status = obj.tick()
        self.assertTrue(status["ready"])
        self.assertEqual(len(self.calls), 2)
        self.calls[0][2].exit_code = 1
        obj.tick()
        self.assertEqual(len(self.calls), 2)
        self.now = 59
        obj.tick()
        self.assertEqual(len(self.calls), 2)
        self.now = 60
        obj.tick()
        self.assertEqual(len(self.calls), 3)
        self.assertTrue(all("generation" not in " ".join(call[0]) for call in self.calls))
        self.assertTrue(all(call[1]["env"]["CUDA_VISIBLE_DEVICES"] == "" for call in self.calls))

    def test_scorer_waits_for_dispatch_then_runs_once_and_records_partial(self):
        obj = self.make()
        obj.maintain_scoring()
        self.assertEqual(len(self.calls), 0)
        self.dispatch()
        obj.maintain_scoring()
        self.assertEqual(len(self.calls), 1)
        self.assertEqual(self.calls[0][0][1:], ["frozen_score_p36.py", "--run-dir", str(self.run)])
        self.assertFalse(coordinator.read(self.state / "scoring_status.json")["automatic_retry"])
        self.write_scores()
        self.calls[0][2].exit_code = 0
        obj.maintain_scoring()
        obj.maintain_scoring()
        self.assertEqual(len(self.calls), 1)
        completion = coordinator.read(self.run / "completion.json")
        self.assertEqual(completion["status"], "scored_partial_subset")
        self.assertFalse(completion["full_benchmark_complete"])
        self.assertEqual(completion["metadata"]["missing_or_failed_slots"], 1)
        self.assertNotIn("metrics", completion["metadata"])

    def test_failed_score_is_never_retried(self):
        obj = self.make()
        self.dispatch()
        obj.maintain_scoring()
        self.calls[0][2].exit_code = 1
        obj.maintain_scoring()
        self.now = 100000
        obj.maintain_scoring()
        self.make().maintain_scoring()
        self.assertEqual(len(self.calls), 1)
        self.assertEqual(coordinator.read(self.run / "completion.json")["status"], "scoring_failed_no_retry")

    def test_interrupted_claim_never_restarts_scoring(self):
        self.dispatch()
        coordinator.save(self.state / "scoring_status.json", {"stage": "running", "attempts": 1})
        obj = self.make()
        obj.maintain_scoring()
        self.assertEqual(len(self.calls), 0)
        self.assertEqual(obj.scoring["stage"], "interrupted_no_retry")
        self.assertTrue((self.run / "completion.json").is_file())

    def test_existing_scores_are_reused_without_scorer(self):
        self.write_scores()
        obj = self.make()
        obj.maintain_scoring()
        self.assertEqual(len(self.calls), 0)
        self.assertEqual(obj.scoring["stage"], "completed_partial_subset")
        self.assertTrue(coordinator.read(self.run / "completion.json")["existing_scores_reused"])

    def test_interrupted_coordinator_recovers_existing_valid_score_without_retry(self):
        self.write_scores()
        coordinator.save(self.state / "scoring_status.json", {"stage": "running", "attempts": 1})
        obj = self.make()
        obj.maintain_scoring()
        self.assertEqual(len(self.calls), 0)
        self.assertEqual(obj.scoring["stage"], "completed_partial_subset")
        self.assertTrue(obj.scoring["interruption_recorded"])

    def test_changed_pin_prevents_children_and_consumes_no_retry_score_attempt(self):
        pinned = self.root / "pinned.py"
        pinned.write_text("Changed code\n")
        self.config["files_sha256"] = {str(pinned): "wrong"}
        self.dispatch()
        obj = self.make()
        obj.tick()
        self.assertEqual(len(self.calls), 0)
        self.assertEqual(obj.scoring["stage"], "failed_no_retry")
        self.assertTrue(all(child["stage"] == "restart_wait" for child in obj.children.values()))


if __name__ == "__main__":
    unittest.main()
