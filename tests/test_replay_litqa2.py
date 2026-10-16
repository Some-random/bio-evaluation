"""Synthetic checks for safe replay identifiers and paired score comparisons."""

import contextlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/replay_litqa2.py"
SPEC = importlib.util.spec_from_file_location("replay_litqa2_under_test", SCRIPT)
replay = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(replay)


class ReplayTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.state = self.root / ".local/litqa2_replay"
        self.baseline = self.state / "baseline/results/runs/synthetic_old"
        self.run_id = "synthetic_replay"
        self.current = self.root / "results/runs" / self.run_id
        self.plan = {
            "run_id": self.run_id,
            "baseline": str(self.baseline),
            "all_request_payloads_match_archive": True,
        }
        root_patch = mock.patch.object(replay, "ROOT", self.root)
        state_patch = mock.patch.object(replay, "STATE", self.state)
        root_patch.start()
        state_patch.start()
        self.addCleanup(root_patch.stop)
        self.addCleanup(state_patch.stop)

    @staticmethod
    def write_json(path, value):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value) + "\n")

    def stage_scores(self, old_rows, new_rows, old_metrics=None, new_metrics=None):
        self.write_json(self.baseline / "scores.json", {"metrics": old_metrics or {"accuracy": 0.5}})
        self.write_json(self.current / "scores.json", {"metrics": new_metrics or {"accuracy": 0.5}})
        self.write_json(self.baseline / "per_case_scores.json", old_rows)
        self.write_json(self.current / "per_case_scores.json", new_rows)

    def test_prepare_rejects_unsafe_or_original_ids_before_any_io(self):
        forbidden = ["", ".", "..", "../escape", "nested/replay", "/tmp/replay", replay.OLD_RUN]
        with mock.patch.object(Path, "read_text", side_effect=AssertionError("Unexpected file read")) as read:
            with mock.patch.object(replay.shutil, "copytree", side_effect=AssertionError("Unexpected copy")) as copy:
                for run_id in forbidden:
                    with self.subTest(run_id=run_id):
                        with self.assertRaisesRegex(ValueError, "distinct, simple run ID"):
                            replay.prepare(run_id)
                read.assert_not_called()
                copy.assert_not_called()
        self.assertFalse(self.state.exists())
        self.assertFalse((self.root / "results").exists())

    def test_compare_rejects_different_case_ids_without_writing_a_comparison(self):
        original = [{"case_id": "case_a", "answer": 0, "correct": True}]
        changed = [{"case_id": "case_b", "answer": 0, "correct": True}]
        self.stage_scores(original, changed)
        with self.assertRaisesRegex(ValueError, "case set differs"):
            replay.compare(self.plan)
        self.assertFalse((self.current / "comparison.json").exists())

    def test_compare_rejects_missing_cases_even_if_remaining_scores_match(self):
        original = [
            {"case_id": "case_a", "answer": 0, "correct": True},
            {"case_id": "case_b", "answer": 1, "correct": False},
        ]
        self.stage_scores(original, original[:1])
        with self.assertRaisesRegex(ValueError, "case set differs"):
            replay.compare(self.plan)
        self.assertFalse((self.current / "comparison.json").exists())

    def test_compare_preserves_metrics_and_pairs_answers_by_case_id(self):
        old_rows = [
            {"case_id": "case_a", "answer": 0, "correct": True},
            {"case_id": "case_b", "answer": 1, "correct": True},
            {"case_id": "case_c", "answer": 2, "correct": False},
            {"case_id": "case_d", "answer": 3, "correct": False},
        ]
        new_rows = [
            {"case_id": "case_d", "answer": 3, "correct": False},
            {"case_id": "case_c", "answer": 0, "correct": True},
            {"case_id": "case_b", "answer": 2, "correct": False},
            {"case_id": "case_a", "answer": 0, "correct": True},
        ]
        old_metrics = {"accuracy": 0.5, "precision": 2 / 3, "coverage": 0.75, "n_total": 4}
        new_metrics = {"accuracy": 0.5, "precision": 0.5, "coverage": 1.0, "n_total": 4}
        self.stage_scores(old_rows, new_rows, old_metrics, new_metrics)
        inputs = [self.baseline / "scores.json", self.baseline / "per_case_scores.json",
                  self.current / "scores.json", self.current / "per_case_scores.json"]
        before = {path: path.read_bytes() for path in inputs}

        with contextlib.redirect_stdout(io.StringIO()):
            replay.compare(self.plan)

        result = json.loads((self.current / "comparison.json").read_text())
        self.assertEqual(result["baseline_metrics"], old_metrics)
        self.assertEqual(result["replay_metrics"], new_metrics)
        self.assertEqual(result["baseline_cases"], 4)
        self.assertEqual(result["replay_cases"], 4)
        self.assertTrue(result["identical_case_set"])
        self.assertTrue(result["same_request_payloads"])
        self.assertEqual(result["same_parsed_answer"], 2)
        self.assertEqual(result["correctness_transitions"], {
            "(True, True)": 1, "(True, False)": 1,
            "(False, True)": 1, "(False, False)": 1,
        })
        self.assertEqual({path: path.read_bytes() for path in inputs}, before)


if __name__ == "__main__":
    unittest.main()
