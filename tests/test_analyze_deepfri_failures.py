import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location("diagnose", Path(__file__).resolve().parents[1] / "scripts/analyze_deepfri_failures.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class FailureClassifierTests(unittest.TestCase):
    def case(self, text, finish="stop"):
        return module.classify(text, finish, {"GO:1", "GO:2"})

    def test_valid_sparse_and_empty_vectors(self):
        for text in (' {"scores":{"GO:1":0.5}}\n', '{"scores":{}}'):
            self.assertEqual(self.case(text)["partition"], "valid")

    def test_length_is_never_repaired_even_with_valid_json(self):
        self.assertEqual(self.case('{"scores":{"GO:1":1}}', "length")["partition"], "unfinished_nonstop")

    def test_empty_and_malformed_have_distinct_partitions(self):
        self.assertEqual(self.case(None)["partition"], "empty_final")
        self.assertEqual(self.case('{"scores":')["partition"], "malformed_json")

    def test_unknown_and_string_are_both_visible(self):
        row = self.case('{"scores":{"UNKNOWN":"1e-2"}}')
        self.assertEqual(row["partition"], "unknown_identifier")
        self.assertEqual(set(row["flags"]), {"unknown_identifier", "numeric_string"})

    def test_wrong_types_and_nonnumeric_string(self):
        row = self.case('{"scores":{"GO:1":true,"GO:2":"likely"}}')
        self.assertEqual(set(row["flags"]), {"wrong_value_type", "nonnumeric_string"})

    def test_duplicate_values_not_silently_overwritten(self):
        equal = self.case('{"scores":{"GO:1":0.5,"GO:1":0.5}}')
        conflict = self.case('{"scores":{"GO:1":0.5,"GO:1":0.7}}')
        self.assertEqual(equal["partition"], "duplicate_identical_only")
        self.assertEqual(conflict["partition"], "duplicate_conflicting")

    def test_bool_and_numeric_duplicates_conflict(self):
        self.assertEqual(self.case('{"scores":{"GO:1":true,"GO:1":1}}')["partition"], "duplicate_conflicting")

    def test_nested_duplicate_and_confidence_object(self):
        row = self.case('{"scores":{"GO:1":{"a":1,"a":2}}}')
        self.assertIn("duplicate_conflicting", row["flags"])
        self.assertIn("wrong_value_type", row["flags"])

    def test_nonfinite_and_range_are_separate(self):
        row = self.case('{"scores":{"GO:1":NaN,"GO:2":2}}')
        self.assertEqual(set(row["flags"]), {"nonfinite_numeric", "out_of_range_numeric"})

    def test_schema_not_accepted_as_confidence_vector(self):
        for text in ('[]', '{"GO:1":0.5}', '{"scores":[]}'):
            self.assertEqual(self.case(text)["partition"], "wrong_schema")

if __name__ == "__main__":
    unittest.main()
