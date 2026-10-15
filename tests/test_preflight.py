import importlib.util
import unittest
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "scripts/preflight.py"
spec = importlib.util.spec_from_file_location("preflight", path)
p = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p)

class LeakageTests(unittest.TestCase):
    def setUp(self):
        self.row = {"entry": "SECRET_ACCESSION-A2V", "protein1": "MAAK", "protein2": "MVAK",
                    "function": "General wild-type function", "uniprot_description": "Desired assay effect",
                    "GPT_description": "", "all_description": "SCORER_ONLY_SENTINEL", "rank": "99999"}

    def test_unknown_position_does_not_reveal_target(self):
        fields = p.mutation_fields("P32", self.row)
        text = p.render_fields("P32", fields)
        for forbidden in ("SECRET_ACCESSION", "A2V", "MVAK", "SCORER_ONLY_SENTINEL", "99999"):
            self.assertNotIn(forbidden, text)
        self.assertIn("Desired assay effect", text)
        self.assertIn("MAAK", text)

    def test_known_position_retains_position_without_answer(self):
        text = p.render_fields("P31", p.mutation_fields("P31", self.row))
        self.assertIn("Position (1-based): 2", text)
        self.assertNotIn("A2V", text)
        self.assertNotIn("MVAK", text)

    def test_explanation_does_not_receive_heldout_effect(self):
        text = p.render_fields("P30", p.mutation_fields("P30", self.row))
        self.assertIn("A2V", text)
        self.assertNotIn("Desired assay effect", text)
        self.assertNotIn("SCORER_ONLY_SENTINEL", text)

    def test_mol_keeps_sequence_and_drops_reference(self):
        instance = {"instruction": "Describe: ", "input": "<bop><p>M<p>A<p>X<eop>", "output": ["GOLD_SENTINEL"], "id": "SECRET_ID"}
        text, fields = p.render_mol("P23", instance)
        self.assertEqual(text, "Describe: MAX")
        self.assertNotIn("GOLD_SENTINEL", text)
        self.assertNotIn("SECRET_ID", text)

    def test_extra_field_cannot_pass_allowlist(self):
        fields = p.mutation_fields("P32", self.row)
        fields["variant_sequence"] = self.row["protein2"]
        with self.assertRaises(ValueError):
            p.render_fields("P32", fields)

    def test_numbering_mismatch_fails_explicitly(self):
        self.row["entry"] = "SECRET_ACCESSION-K2V"
        with self.assertRaises(ValueError):
            p.mutation_fields("P31", self.row)

    def test_broken_serialization_is_not_silently_repaired(self):
        with self.assertRaises(ValueError):
            p.decode_mol_sequence("<bop><p>M<p>A<eop>DROP_THIS")

    def test_official_pg_renderer_ignores_scoring_values(self):
        pg = p.load_pg_module()
        meta = {"target_name": "Toy", "organism": "Toy", "fitness_description": "Toy assay"}
        left, ids = pg.build_user_prompt(meta, "MA", [("A2V", "MV", 123456.7), ("A2L", "ML", -123456.7)])
        right, _ = pg.build_user_prompt(meta, "MA", [("A2V", "MV", 0.0), ("A2L", "ML", 0.0)])
        self.assertEqual(left, right)
        self.assertIsNone(pg.parse_ranking('{"ranking":["M01","M01"]}', ids))
        self.assertIsNone(pg.parse_ranking('{"ranking":["M01"]}', ids))

if __name__ == "__main__":
    unittest.main()
