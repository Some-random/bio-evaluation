import importlib.util
from pathlib import Path
import sys
import unittest

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
spec = importlib.util.spec_from_file_location("prepare_local_deepfri_proposals", SCRIPTS / "prepare_local_deepfri_proposals.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class SparseConfidenceProposalTests(unittest.TestCase):
    def parse(self, text, finish="stop"):
        return mod.parse_sparse_confidence(text, ["CLASS:A", "CLASS:B"], finish)

    def test_explicit_zero_binary_ties_and_real_values_are_retained(self):
        self.assertEqual(self.parse('{"scores":{}}'), {})
        self.assertEqual(self.parse('{"scores":{"CLASS:A":1,"CLASS:B":0}}'), {"CLASS:A": 1, "CLASS:B": 0})
        self.assertEqual(self.parse('{"scores":{"CLASS:A":0.4,"CLASS:B":0.4}}'), {"CLASS:A": 0.4, "CLASS:B": 0.4})

    def test_malformed_missing_unknown_duplicates_and_truncation_are_invalid(self):
        for text, finish in [('', 'stop'), ('{}', 'stop'), ('["CLASS:A"]', 'stop'),
                             ('{"scores":{},"extra":1}', 'stop'),
                             ('{"scores":{"UNKNOWN":0.4}}', 'stop'),
                             ('{"scores":{"CLASS:A":true}}', 'stop'),
                             ('{"scores":{"CLASS:A":"0.4"}}', 'stop'),
                             ('{"scores":{"CLASS:A":NaN}}', 'stop'),
                             ('{"scores":{"CLASS:A":1.1}}', 'stop'),
                             ('{"scores":{"CLASS:A":0.2,"CLASS:A":0.8}}', 'stop'),
                             ('```json\n{"scores":{}}\n```', 'stop'),
                             ('{"scores":{}}', 'length')]:
            with self.subTest(text=text, finish=finish), self.assertRaises(ValueError):
                self.parse(text, finish)

    def test_prompt_uses_full_sequence_and_global_descriptions_only(self):
        text = mod.prompt("P14", "MXAC", [{"class_id": "CLASS:B", "description": "global second"}, {"class_id": "CLASS:A", "description": "global first"}])
        self.assertIn("MXAC", text)
        self.assertLess(text.index("CLASS:B\tglobal second"), text.index("CLASS:A\tglobal first"))
        self.assertIn('omitted permitted class has confidence exactly 0', text)
        self.assertNotIn("CASE-ID", text)


if __name__ == "__main__":
    unittest.main()
