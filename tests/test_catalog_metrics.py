import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location("catalog_metrics", Path(__file__).resolve().parents[1] / "scripts/catalog_metric_helpers.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class CatalogMetricTests(unittest.TestCase):
    def test_binary_no_conflicting_explanation_or_silent_dropping(self):
        result = mod.classification_accuracy([1, 0, 1, 0], ["Yes.", "Answer: No", "Yes, but No", None])
        self.assertEqual(result["accuracy"], 0.5)
        self.assertEqual((result["parsed"], result["invalid"], result["missing"]), (2, 1, 1))

    def test_numerical_tied_ranks_and_missing_are_distinct(self):
        full = mod.regression_spearman([1., 1., 4., 9.], ["9", "9", "4", "1"])
        self.assertAlmostEqual(full["spearman"], -1)
        partial = mod.regression_spearman([1., 2., 3.], ["3", None, "1"])
        self.assertIsNone(partial["spearman"])
        self.assertAlmostEqual(partial["spearman_parsed_only"], -1)

    def test_undefined_and_nonfinite_outputs(self):
        result = mod.regression_spearman([1., 2.], ["5", "5"])
        self.assertIsNone(result["spearman"])
        self.assertTrue(result["undefined_constant_or_insufficient"])
        for text in ["NaN", "1e999", "The answer is 7 or 8", "7 degrees Celsius"]:
            self.assertIsNone(mod.parse_numeric_answer(text))


if __name__ == "__main__":
    unittest.main()
