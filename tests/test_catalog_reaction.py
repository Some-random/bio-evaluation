"""Synthetic original-ID, full-context, gold-separation and metric contracts."""
import ast
import copy
import csv
import json
import os
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import prepare_catalog_reaction as prepare


def synthetic_tables(count=384):
    tables = {key: [] for key in ["name", "description", "language", "template"]}
    for index in range(count):
        name, alternate, comment = f"Synthetic class{index}.", f"Artificial alias{index}.", f"Complete synthetic comment{index}."
        tables["description"].append({"id": str(index), "EC_number": f"9.9.9.{index}",
              "hier1": "Synthetic.", "hier2": "Synthetic.", "hier3": "Synthetic.",
              "name": name, "comment": comment, "alter_name": alternate})
        tables["name"].append({"id": str(index), "name": name + " " + alternate})
        tables["language"].append({"id": str(index), "name": "A " + name + " enzyme. This enzyme is also known as " + alternate})
        tables["template"].append({"id": str(index), "name": "FUNCTION: " + name + " " + alternate,
                                  "description": "FUNCTION: " + name + " " + alternate + " " + comment})
    return tables


class ReactionTests(unittest.TestCase):
    def test_complete_global_ontology_independent_of_observed_classes(self):
        ontology = prepare.validate_tables(synthetic_tables())
        context = prepare.class_context(ontology)
        self.assertEqual(len(ontology), 384)
        self.assertTrue(all(entry["native_full_pretraining_description"] in context for entry in ontology))
        self.assertIn("Complete synthetic comment383.", context)
        row = {"primary": "MAGZX", "protein_length": 5, "label": 17}
        first, reference = prepare.transform(0, row, context)
        other, _ = prepare.transform(0, {**row, "label": 383}, context)
        self.assertEqual(first, other)
        self.assertEqual(reference["target"], 17)
        self.assertTrue(first["prompt"].endswith(row["primary"]))
        self.assertEqual(first["class_context_sha256"], prepare.sha256(context.encode()))

    def test_mapping_template_or_complete_field_changes_rejected(self):
        for change in ["order", "duplicate_ec", "comment_drop", "alter_name_drop"]:
            tables = synthetic_tables(2)
            if change == "order": tables["name"].reverse()
            if change == "duplicate_ec": tables["description"][1]["EC_number"] = tables["description"][0]["EC_number"]
            if change == "comment_drop": tables["template"][1]["description"] = tables["template"][1]["name"]
            if change == "alter_name_drop": tables["name"][1]["name"] = tables["description"][1]["name"]
            with self.assertRaises(ValueError):
                prepare.validate_tables(tables, 2)
        with self.assertRaisesRegex(ValueError, "all384"):
            prepare.class_context(prepare.validate_tables(synthetic_tables(2), 2))

    def test_no_sequence_cleaning_target_remapping_or_extra_fields(self):
        row = {"primary": "MAG", "protein_length": 3, "label": 383}
        for changed in [{**row, "primary": "M A"}, {**row, "protein_length": 2},
                        {**row, "label": 384}, {**row, "label": True}, {**row, "teacher_explanation": "SECRET"}]:
            with self.assertRaises(ValueError):
                prepare.transform(0, changed, "Synthetic fixed full-context fixture")

    def test_parser_and_all_case_denominator(self):
        for value in ["0", "383", " Answer: 17. "]:
            self.assertIsNotNone(prepare.parse_class_id(value))
        for value in ["384", "-1", "01", "3.0", "17 or 18", "class17", None]:
            self.assertIsNone(prepare.parse_class_id(value))
        result = prepare.accuracy([0, 383, 17, 18], ["0", "383", "17 or 18", None])
        self.assertEqual((result["accuracy"], result["planned"], result["parsed"], result["invalid"], result["missing"]), (.5, 4, 2, 1, 1))

    def test_native_fetch_labels_reconstructs_original_ids_not_test_subset(self):
        path = ROOT / "sources/catalog_reaction__script__run_zero_shot.py"
        tree = ast.parse(path.read_text())
        method = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "fetch_labels")
        namespace = {"os": os, "csv": csv}
        exec(compile(ast.fix_missing_locations(ast.Module(body=[method], type_ignores=[])), str(path), "exec"), namespace)
        with tempfile.TemporaryDirectory() as tmp:
            tsv = Path(tmp) / "synthetic.tsv"
            tsv.write_text("id\tname\tdescription\n2\ttwo\tfull two\n0\tzero\tfull zero\n1\tone\tfull one\n")
            cfg = SimpleNamespace(label=SimpleNamespace(path=str(tsv), field=["description"]))
            self.assertEqual(namespace["fetch_labels"](cfg, None), ["full zero", "full one", "full two"])


if __name__ == "__main__":
    unittest.main()
