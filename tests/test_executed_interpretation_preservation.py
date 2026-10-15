import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from update_executed_interpretations import executed_record, merge_records


class InterpretationPreservationTests(unittest.TestCase):
    def test_existing_executed_record_is_preserved(self):
        original = {"task_id": "B01", "protocol_variant": "NATIVE_PUBLIC_COT_LOCAL_REVIEWED",
                    "run_id": "frozen_first_run", "actual_supplied_information": {"kept": True},
                    "outcome_score": {"accuracy": .39}}
        snapshot = copy.deepcopy(original)
        recomputed = {**original, "outcome_score": {"accuracy": .99}}
        result = merge_records([original], [recomputed])
        self.assertEqual(result, [snapshot])
        self.assertEqual(original, snapshot)

    def test_variant_cannot_silently_replace_different_run(self):
        original = {"task_id": "B03", "protocol_variant": "fixed", "run_id": "first"}
        with self.assertRaisesRegex(ValueError, "collision"):
            merge_records([original], [{**original, "run_id": "retry"}])

    def test_completed_shard_cannot_become_full_task_interpretation(self):
        with tempfile.TemporaryDirectory() as name:
            folder = Path(name)
            values = {
                "scores.json": {"planned": 1024, "completed": 1024, "case_scope": "task_shard_only"},
                "completion.json": {"generation_exit_code": 0, "scoring_exit_code": 0},
                "run_manifest.json": {"configuration": {"case_scope": "task_shard_only"}},
            }
            for filename, value in values.items():
                (folder / filename).write_text(json.dumps(value))
            self.assertIsNone(executed_record({}, folder))

    def test_incomplete_aggregate_cannot_become_full_task_interpretation(self):
        with tempfile.TemporaryDirectory() as name:
            folder = Path(name)
            values = {
                "scores.json": {"planned": 3000, "completed": 3000,
                    "full_test_id_union_validation": {"complete": False, "union_matches_full_test_ids": False}},
                "completion.json": {"generation_exit_code": 0, "scoring_exit_code": 0},
                "run_manifest.json": {"configuration": {"aggregate_only": True}},
            }
            for filename, value in values.items():
                (folder / filename).write_text(json.dumps(value))
            self.assertIsNone(executed_record({}, folder))


if __name__ == "__main__":
    unittest.main()
