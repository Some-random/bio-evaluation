"""Invented targets only; verify unchanged Spearman and failure accounting."""
import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
spec = importlib.util.spec_from_file_location("score_p08_new", ROOT / "scripts/score_p08_regeneration_20261020.py")
p08 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p08)


class P08ScorePolicyTests(unittest.TestCase):
    def test_identical_ranks(self):
        self.assertEqual(p08.spearman([1, 2, 3], [4, 5, 6]), 1.0)

    def test_negative_correlation_kept_negative(self):
        self.assertEqual(p08.spearman([1, 2, 3], [6, 5, 4]), -1.0)

    def test_ties_average_rank(self):
        self.assertEqual(p08.ranks([3, 1, 1, 2]), [4, 1.5, 1.5, 3])
        self.assertAlmostEqual(p08.spearman([1, 1, 2], [2, 2, 1]), -1.0)

    def test_empty_or_constant_is_undefined(self):
        for a, b in [([], []), ([1], [2]), ([1, 1], [2, 3]), ([1, 2], [3, 3])]:
            self.assertIsNone(p08.spearman(a, b))

    def test_missing_prediction_retains_denominator(self):
        result = p08.metric_policy([1, 2, 3], [3, None, 1])
        self.assertEqual(result["planned"], 3)
        self.assertEqual(result["valid_predictions"], 2)
        self.assertEqual(result["invalid_or_missing"], 1)
        self.assertIsNone(result["spearman"])
        self.assertEqual(result["spearman_parsed_only"], -1)

    def test_complete_metric_only_when_all_present(self):
        result = p08.metric_policy([1, 2, 3], [1, 2, 3])
        self.assertEqual(result["spearman"], 1)
        self.assertIsNone(result["spearman_parsed_only"])

    def test_nonfinite_not_coerced(self):
        with self.assertRaises(ValueError):
            p08.spearman([1, 2], [float("nan"), 1])

    def test_matching_nonempty_arrays_required(self):
        for targets, predictions in [([], []), ([1, 2], [1]), ([1], [1, 2])]:
            with self.assertRaises(ValueError):
                p08.metric_policy(targets, predictions)

    def test_prediction_seal_rejects_changed_bytes(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            output = root / "synthetic.json"
            output.write_bytes(b'{"prediction": -2.0}\n')
            lock = {output.name: p08.sha(output.read_bytes())}
            p08.verify_locked_files(root, lock)
            output.write_bytes(b'{"prediction": 2.0}\n')
            with self.assertRaises(ValueError):
                p08.verify_locked_files(root, lock)

    def test_prediction_seal_rejects_external_path(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            outside = root / "outside.json"
            outside.write_bytes(b"synthetic")
            run = root / "run"
            run.mkdir()
            with self.assertRaises(ValueError):
                p08.verify_locked_files(run, {"../outside.json": p08.sha(outside.read_bytes())})


if __name__ == "__main__":
    unittest.main()
