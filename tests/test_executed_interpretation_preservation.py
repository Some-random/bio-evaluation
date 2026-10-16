import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from update_executed_interpretations import executed_record, merge_records
import update_executed_interpretations as reporting


class InterpretationPreservationTests(unittest.TestCase):
    def fixture_run(self, root, task, interpretation):
        folder = root / 'run'
        (folder / 'requests').mkdir(parents=True)
        payload = {'messages': [{'role': 'user', 'content': 'synthetic input'}]}
        config = {'approved_task_ids': [task], 'variant': 'synthetic', 'model': 'synthetic',
                  'model_revision': 'r1', 'run_id': 'run', 'generation': {},
                  'input_modalities': ['original_JPEG_image']}
        values = {'scores.json': {'planned': 1, 'completed': 1, 'metrics': {'value': None},
                                 'interpretation': interpretation, 'request_response_hash_audit': 'passed',
                                 'native_reference_qualification': 'Supplied predictor context contributes to targets.'},
                  'completion.json': {'generation_exit_code': 0, 'scoring_exit_code': 0},
                  'run_manifest.json': {'configuration': config},
                  'requests/synthetic.json': {'payload': payload, 'request_sha256': reporting.digest(payload)}}
        for name, value in values.items():
            (folder / name).write_text(json.dumps(value))
        return folder

    def test_textual_interpretation_and_null_score_are_preserved(self):
        with tempfile.TemporaryDirectory() as name:
            root = Path(name)
            folder = self.fixture_run(root, 'P12', 'Native confidence score is undefined for invalid vectors.')
            with patch.object(reporting, 'ROOT', root):
                row = executed_record({'task_id': 'P12'}, folder)
            self.assertIsNone(row['outcome_score']['value'])
            self.assertIn('undefined', row['execution_interpretation_note'])
            self.assertTrue(row['actual_supplied_information']['native_required_images_preserved'])

    def test_native_predictor_target_overlap_is_not_claimed_absent(self):
        with tempfile.TemporaryDirectory() as name:
            root = Path(name)
            folder = self.fixture_run(root, 'P29', {'likely_demands': {'labels': ['annotation']}})
            with patch.object(reporting, 'ROOT', root):
                row = executed_record({'task_id': 'P29'}, folder)
            info = row['actual_supplied_information']
            self.assertTrue(info['native_predictor_context_contributes_to_scoring_target'])
            self.assertTrue(info['reference_answers_or_explanations_supplied'])
            self.assertFalse(info['direct_curated_reference_files_or_teacher_explanations_supplied'])
            self.assertFalse(row['task_demands']['internal_model_computation_established'])

    def test_qualified_proxy_records_actual_available_reference_and_demands(self):
        with tempfile.TemporaryDirectory() as name:
            root = Path(name)
            interpretation = {'reference_evidence': 'Fixed trained predictor; novelty reference unavailable.',
                              'good_score': 'Improvement in this predictor only.',
                              'bad_score': 'Limited delivery or predicted improvement.',
                              'likely_demands_provisional': ['sequence property prediction']}
            folder = self.fixture_run(root, 'P42', interpretation)
            with patch.object(reporting, 'ROOT', root):
                row = executed_record({'task_id': 'P42'}, folder)
            self.assertEqual(row['reference_answer_source'], interpretation['reference_evidence'])
            self.assertEqual(row['good_score_establishes'], interpretation['good_score'])
            self.assertEqual(row['task_demands']['labels'], interpretation['likely_demands_provisional'])
            self.assertFalse(row['task_demands']['internal_model_computation_established'])

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

    def test_native_id_and_ood_splits_keep_distinct_execution_records(self):
        original = {'task_id': 'P29', 'protocol_variant': 'same_native_protocol',
                    'native_split': 'id', 'run_id': 'id_run'}
        ood = {**original, 'native_split': 'ood', 'run_id': 'ood_run'}
        self.assertEqual(merge_records([original], [ood]), [original, ood])
        with self.assertRaisesRegex(ValueError, 'collision'):
            merge_records([original, ood], [{**ood, 'run_id': 'ood_retry'}])

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
