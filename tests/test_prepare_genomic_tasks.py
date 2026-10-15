import importlib.util
import json
from pathlib import Path
import unittest


spec = importlib.util.spec_from_file_location(
    "prepare_genomic_tasks", Path(__file__).resolve().parents[1] / "scripts/prepare_genomic_tasks.py"
)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class GenomicPreparationTests(unittest.TestCase):
    def test_full_indel_windows_and_source_question_survive_without_gold(self):
        row = {"question": "Synthetic input question with required gene/chromosome context.",
               "reference_sequence": "ACGT" * 1024, "mutated_sequence": "ACGT" * 1024 + "AA",
               "answer": "['Pathogenic']; SYNTHETIC_HIDDEN_DISEASE", "cleaned_pathogenicity": "Pathogenic"}
        prepared, provenance, reference = mod.build_record("N03", row, 7, {"split": "test", "path": "synthetic.parquet", "sha256": "fixture"})
        self.assertEqual(list(prepared), ["task", "case_id", "variant", "split", "messages"])
        self.assertEqual([m["role"] for m in prepared["messages"]], ["user"])
        message = prepared["messages"][0]["content"]
        self.assertIn(row["reference_sequence"], message)
        self.assertIn(row["mutated_sequence"], message)
        self.assertIn(row["question"], message)
        self.assertNotIn("SYNTHETIC_HIDDEN_DISEASE", json.dumps(prepared))
        self.assertEqual(reference["normalized_label"], "pathogenic")
        self.assertEqual(provenance["source_fields"]["mutated_sequence"], row["mutated_sequence"])

    def test_teacher_rationale_is_separate_and_split_ids_do_not_collide(self):
        row = {"question": "Synthetic pathway question.", "reference_sequence": "AAAA", "variant_sequence": "AATA",
               "answer": "SYNTHETIC_HIDDEN_LABEL", "reasoning": "SYNTHETIC_HIDDEN_TEACHER"}
        test, _, ref = mod.build_record("N01", row, 0, {"split": "test", "path": "test.parquet", "sha256": "fixture"})
        val, _, _ = mod.build_record("N01", row, 0, {"split": "val", "path": "val.parquet", "sha256": "fixture"})
        self.assertNotEqual(test["case_id"], val["case_id"])
        self.assertNotIn("SYNTHETIC_HIDDEN", json.dumps(test))
        self.assertEqual(ref["source_teacher_reasoning"], row["reasoning"])
        self.assertFalse(ref["teacher_reasoning_is_independently_verified_mechanism"])

    def test_original_coding_id_and_fixed_normalization(self):
        row = {"ID": "SyntheticSourceID", "question": "Synthetic clinical question.",
               "reference_sequence": "AAAA", "variant_sequence": "AATA", "answer": "Benign; ignored scorer-only disease"}
        prepared, provenance, reference = mod.build_record("N02", row, 1, {"split": "test", "path": "test.parquet", "sha256": "fixture"})
        self.assertEqual(prepared["case_id"], row["ID"])
        self.assertEqual(provenance["original_source_id"], row["ID"])
        self.assertEqual(reference["normalized_label"], "benign")


if __name__ == "__main__":
    unittest.main()
