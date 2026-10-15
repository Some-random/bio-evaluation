"""Check native context construction against the pinned task implementations."""
import ast
import copy
from pathlib import Path
import sys
from types import SimpleNamespace
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from prepare_labbench import native_question


class StubBase:
    def get_input_output(self):
        return SimpleNamespace(question=self.question), "A", "B"


def native_source_question(subset, row):
    tree = ast.parse((ROOT / "sources" / f"lab__{subset}__task.py").read_text())
    definition = copy.deepcopy(next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == "EvalInstance"))
    namespace = {"labbench": SimpleNamespace(BaseEvalInstance=StubBase, AgentInput=SimpleNamespace),
                 "Field": lambda **kwargs: None}
    exec(compile(ast.fix_missing_locations(ast.Module(body=[definition], type_ignores=[])), "native-task", "exec"), namespace)
    instance = namespace["EvalInstance"]()
    for key, value in row.items():
        setattr(instance, "title" if key == "paper-title" else key, value)
    return instance.get_input_output()[0].question


class NativeInputPreparationTests(unittest.TestCase):
    def test_supplement_title_doi_match_official_transformation(self):
        row = {"question": "Synthetic question?", "paper-title": "Synthetic study",
               "source": "https://doi.org/example.synthetic", "ideal": "SCORER_ONLY"}
        prepared = native_question(row, "SuppQA")
        self.assertEqual(prepared, native_source_question("SuppQA", row))
        self.assertIn(row["paper-title"], prepared)
        self.assertIn(row["source"], prepared)
        self.assertNotIn(row["ideal"], prepared)

    def test_complete_protocol_matches_official_transformation(self):
        row = {"question": "Synthetic question?", "protocol": "Synthetic context.\n" * 1000,
               "ideal": "SCORER_ONLY"}
        prepared = native_question(row, "ProtocolQA")
        self.assertEqual(prepared, native_source_question("ProtocolQA", row))
        self.assertTrue(prepared.startswith(row["protocol"]))
        self.assertNotIn(row["ideal"], prepared)

    def test_plain_categories_do_not_add_source_only_reference_material(self):
        row = {"question": "Synthetic question?", "key-passage": "SCORER_ONLY",
               "ideal": "SCORER_ONLY", "sources": ["REFERENCE_ONLY"]}
        for subset in ["LitQA2", "DbQA", "SeqQA", "CloningScenarios"]:
            self.assertEqual(native_question(row, subset), row["question"])


if __name__ == "__main__":
    unittest.main()
