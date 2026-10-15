import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location("catalog_numerical", Path(__file__).resolve().parents[1] / "scripts/prepare_catalog_numerical.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class NumericalTests(unittest.TestCase):
    def test_native_test_only_and_labels_separate(self):
        rows = [{"sequence": "MUA", "target": "42.5", "set": "test", "validation": "False"},
                {"sequence": "AAA", "target": "99.1", "set": "train", "validation": "False"},
                {"sequence": "CCC", "target": "17.3", "set": "train", "validation": "True"}]
        inputs, refs = mod.transform(rows)
        self.assertEqual(len(inputs), 1)
        self.assertTrue(inputs[0]["prompt"].endswith("MUA"))
        self.assertNotIn("42.5", inputs[0]["prompt"])
        self.assertEqual(refs[0]["target"], 42.5)

    def test_refuse_ambiguous_splits_and_silent_cleaning(self):
        for row in [{"sequence": "MA", "target": "1", "set": "test", "validation": "True"},
                    {"sequence": "M A", "target": "1", "set": "test", "validation": "False"},
                    {"sequence": "MA", "target": "NaN", "set": "test", "validation": "False"}]:
            with self.assertRaises(ValueError):
                mod.transform([row])


if __name__ == "__main__":
    unittest.main()
