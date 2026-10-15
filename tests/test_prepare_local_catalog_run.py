"""Check source identity and native/adapted protocol metadata before inference."""
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from run_local_labbench_multimodal import read_frozen_config


class FrozenCatalogConfigTests(unittest.TestCase):
    def test_ready_property_configs_have_correct_source_and_metric_contract(self):
        for task in ["P01", "P02", "P06", "P10", "P11"]:
            path = ROOT / "configs" / f"local_catalog_{task.lower()}.json"
            if not path.exists():
                continue
            settings, cases = read_frozen_config(path)
            self.assertEqual(settings["approved_task_ids"], [task])
            self.assertNotIn("LAB-Bench", settings["paper_comparison"])
            self.assertNotEqual(settings["source_dataset_revision"], "5c77cec648430f30611808808861eb86f81d5eaa")
            self.assertIn("zero-shot", settings["paper_comparison"])
            self.assertIn("Spearman" if task == "P06" else "accuracy", settings["metric_policy"])
            self.assertTrue(cases)


if __name__ == "__main__":
    unittest.main()
