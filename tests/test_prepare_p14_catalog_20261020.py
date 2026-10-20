"""Synthetic safeguards for P14 full-sequence, reference-isolated preparation."""
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import prepare_p14_catalog_20261020 as prep
from run_deepfri_catalog_20261020 import parse_vector


class P14PreparationTests(unittest.TestCase):
    def classes(self):
        return [{"index": i, "class_id": f"GO:{i:07d}", "description": f"invented class {i}"}
                for i in range(prep.CLASS_COUNT)]

    def old_case(self, sequence="ACDEFGHIKL"):
        return {"task": "P14", "case_id": "invented:test", "variant": "historical",
                "split": "released_test95", "messages": [{"role": "user", "content":
                "old instruction\n\nComplete amino acid sequence:\n" + sequence +
                "\n\nFixed global class vocabulary (class ID followed by description):\nclass"}]}

    def test_complete_sequence_extraction(self):
        self.assertEqual(prep.extracted_historical_sequence(self.old_case()), "ACDEFGHIKL")

    def test_wrong_task_rejected(self):
        row = self.old_case(); row["task"] = "P13"
        with self.assertRaises(ValueError): prep.extracted_historical_sequence(row)

    def test_extra_reference_field_rejected(self):
        row = self.old_case(); row["target"] = [1, 0]
        with self.assertRaises(ValueError): prep.extracted_historical_sequence(row)

    def test_multiturn_context_rejected(self):
        row = self.old_case(); row["messages"].append({"role": "assistant", "content": "prior"})
        with self.assertRaises(ValueError): prep.extracted_historical_sequence(row)

    def test_truncated_or_whitespace_sequence_rejected(self):
        for seq in ["ACD...", "AC DE", "", "acd"]:
            with self.subTest(seq=seq), self.assertRaises(ValueError):
                prep.extracted_historical_sequence(self.old_case(seq))

    def test_fasta_preserves_multiline_complete_sequence(self):
        self.assertEqual(prep.fasta_records(">toy-A\nACD\nEFG\n>toy-B description\nHIKL\n"),
                         {"toy-A": "ACDEFG", "toy-B": "HIKL"})

    def test_fasta_duplicate_identity_rejected(self):
        with self.assertRaises(ValueError): prep.fasta_records(">toy\nACD\n>toy\nEFG\n")

    def test_validation_selection_is_disjoint_and_length_only(self):
        seq = {f"v{i}": "A" * (i + 1) for i in range(15)}
        selection, count = prep.select_validation(list(seq), seq, ["t"], ["A" * 5], 3)
        self.assertEqual(count, 14)
        self.assertEqual([x["sequence_length"] for x in selection], [1, 8, 15])

    def test_validation_id_overlap_rejected(self):
        with self.assertRaises(ValueError): prep.select_validation(["v"], {"v": "ACD"}, ["v"], [], 2)

    def test_model_request_has_no_case_id_reference_or_history(self):
        row = prep.model_case("invented:secret-id", "ACDEFGHIKL", self.classes())
        self.assertEqual(set(row), {"task_id", "case_id", "messages"})
        self.assertEqual(len(row["messages"]), 1)
        text = row["messages"][0]["content"]
        self.assertNotIn("invented:secret-id", text)
        self.assertIn("ACDEFGHIKL", text)
        self.assertEqual(text.count("\ninvented class "), 0)

    def test_all_classes_preserve_indexed_order(self):
        text = prep.model_case("toy", "ACD", self.classes())["messages"][0]["content"]
        suffix = text.split("Fixed global class order (zero-based position, class ID, description):\n")[1]
        rows = suffix.splitlines()
        self.assertEqual(len(rows), 489)
        self.assertTrue(rows[0].startswith("0\tGO:0000000\t"))
        self.assertTrue(rows[-1].startswith("488\tGO:0000488\t"))

    def test_valid_native_length_confidence_vector(self):
        text = json.dumps({"scores": [0.123] * 489}, separators=(",", ":"))
        self.assertEqual(parse_vector(text, 489), [0.123] * 489)

    def test_missing_and_truncated_vectors_rejected(self):
        for text, finish in [('{"scores":[0.1]}', "stop"),
                             (json.dumps({"scores": [0.1]*489}, separators=(",", ":")), "length")]:
            with self.assertRaises(ValueError): parse_vector(text, 489, finish)

    def test_immutable_refuses_silent_protocol_replacement(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "test.json"
            prep.immutable(path, b"one")
            prep.immutable(path, b"one")
            with self.assertRaises(ValueError): prep.immutable(path, b"two")


if __name__ == "__main__":
    unittest.main()
