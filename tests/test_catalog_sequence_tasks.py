"""Synthetic fixtures only; never tune against benchmark test outcomes."""
import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location("catalog_sequence", Path(__file__).resolve().parents[1] / "scripts/prepare_catalog_sequence_tasks.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class CatalogSequenceTests(unittest.TestCase):
    def test_complete_pair_round_trip(self):
        text, fields = mod.adapt_input("P11", "Protein_A: <bop><p>M<p>A<p>X<eop>\nProtein_B: <bop><p>G<p>G<eop>")
        self.assertEqual(fields, {"Protein_A": "MAX", "Protein_B": "GG"})
        self.assertEqual(text, "Protein_A: MAX\nProtein_B: GG")

    def test_label_and_extra_metadata_cannot_enter_prompt(self):
        obj = {"Definition": ["Classify the protein. Answer Yes or No."],
               "Instances": [{"id": "synthetic", "input": "Protein: <bop><p>M<p>A<eop>", "output": ["No."]}],
               "Gold explanation": "SECRET_SCORER_ONLY"}
        models, native, refs = mod.transform("P01", "synthetic", "fixture.json", obj, "0" * 64)
        self.assertEqual(models[0]["fields"]["Protein"], "MA")
        self.assertNotIn("target", models[0])
        self.assertNotIn("SECRET_SCORER_ONLY", str(models))
        self.assertEqual(refs[0]["target_binary"], 0)
        self.assertEqual(native[0]["native_serialized_input"], obj["Instances"][0]["input"])
        obj["Instances"][0]["gold_explanation"] = "leak"
        with self.assertRaises(ValueError):
            mod.transform("P01", "synthetic", "fixture.json", obj, "0" * 64)

    def test_reject_missing_or_corrupt_modalities(self):
        for text in ["Protein_A: <bop><p>M<eop>", "Protein_A: <bop><p>M<eop>\nProtein_B: MALFORMED"]:
            with self.assertRaises(ValueError):
                mod.adapt_input("P11", text)
        with self.assertRaises(ValueError):
            mod.adapt_input("P43", "Protein: <bop><p>M<eop>")
        text, fields = mod.adapt_input("P43", "Molecule: <bom>[C][O].[Na+1]<eom>\nProtein: <bop><p>M<eop>")
        self.assertEqual(fields["molecule_selfies"], "[C][O].[Na+1]")
        self.assertIn("Molecule (SELFIES): [C][O].[Na+1]", text)


if __name__ == "__main__":
    unittest.main()
