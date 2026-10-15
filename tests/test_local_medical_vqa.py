"""Synthetic end-to-end evidence locking and native medical VQA accounting."""
import contextlib
import csv
import hashlib
import io
import json
import sys
import tempfile
from pathlib import Path
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import prepare_medical_vqa as preparation
import run_local_labbench_multimodal as runner
import score_local_medical_vqa as scorer
from test_medical_vqa import png_bytes


class MedicalRunFixture:
    def __init__(self, root):
        self.root = root
        self.folder = root / 'results/runs/synthetic-vqa'
        self.folder.mkdir(parents=True)
        self.cases, labels = [], []
        for index, group in enumerate(['OPEN', 'CLOSED', 'OPEN', 'CLOSED', 'OPEN', 'CLOSED', 'CLOSED']):
            row = {'qid': str(index), 'question': 'Synthetic image question?',
                   'answer': 'left kidney' if index == 0 else ('No' if index == 1 else 'Yes'),
                   'answer_type': group}
            self.cases.append(preparation.model_case('V01', row, png_bytes()))
            labels.append(preparation.label_for('V01', row, hashlib.sha256(png_bytes()).hexdigest()))
        self.input_file = root / 'data/medical/model_inputs.jsonl'
        self.label_file = root / 'data/medical/labels.jsonl'
        self.review_file = root / 'configs/review.json'
        self.input_file.parent.mkdir(parents=True)
        self.review_file.parent.mkdir(parents=True)
        self.input_file.write_text(''.join(json.dumps(row) + '\n' for row in self.cases))
        self.label_file.write_text(''.join(json.dumps(row) + '\n' for row in labels))
        self.review_file.write_text(json.dumps({'approved_case_ids': [row['case_id'] for row in self.cases], 'held_cases': []}))
        self.settings = {'run_id': 'synthetic-vqa', 'model': 'synthetic-model', 'model_revision': 'synthetic-revision',
                         'approved_task_ids': ['V01'], 'variant': preparation.VARIANT,
                         'input_file': 'data/medical/model_inputs.jsonl', 'review_file': 'configs/review.json',
                         'scorer_reference_file': 'data/medical/labels.jsonl',
                         'scorer_reference_sha256': scorer.file_digest(self.label_file),
                         'model_facing_fields': ['original_question_text', 'original_image_bytes'],
                         'generation': {'max_tokens': 4096, 'temperature': 1.0, 'top_p': .95, 'top_k': 20,
                                        'seed': 42, 'n': 1, 'chat_template_kwargs': {'enable_thinking': True, 'reasoning_effort': 'medium'}},
                         'frozen_files_sha256': {name: scorer.file_digest(root / name)
                                                for name in ['data/medical/model_inputs.jsonl', 'configs/review.json']}}
        self.manifest = {'configuration': self.settings, 'case_contract_sha256': scorer.digest(self.cases),
                         'planned_cases': len(self.cases), 'solver_tools': [], 'answer_keys_available_to_solver': False}
        self.save_manifest()
        for index, text in [(0, 'The left kidney is visible.'), (1, 'No.'), (2, ''), (6, 'yes and no')]:
            self.save_request(index)
            response = {'model': 'synthetic-model', 'choices': [{'message': {'content': text},
                         'finish_reason': 'length' if index == 6 else 'stop'}],
                        'usage': {'prompt_tokens': 10, 'completion_tokens': 3, 'total_tokens': 13}}
            self.save_response(index, {'status': 'completed', 'http_status': 200, 'text': text,
                                      'finish_reason': 'length' if index == 6 else 'stop', 'response': response})
        self.save_request(3)
        self.save_response(3, {'status': 'transport_error', 'http_status': 0, 'response': {'error': {'type': 'SyntheticTimeout'}}})
        self.save_request(5)

    def save_manifest(self):
        (self.folder / 'run_manifest.json').write_text(json.dumps(self.manifest))

    def identity(self, index):
        case = self.cases[index]
        return scorer.digest([case['task'], case['variant'], case['case_id']])

    def record_path(self, category, index):
        return self.folder / category / (self.identity(index) + '.json')

    def save_request(self, index):
        scorer.write_json(self.record_path('requests', index), runner.request_record(self.cases[index], self.settings))

    def save_response(self, index, extra):
        case = self.cases[index]
        record = {key: case[key] for key in ['task', 'case_id', 'variant', 'split']}
        record.update(model='synthetic-model', model_revision='synthetic-revision',
                      request_sha256=scorer.digest(runner.payload_for(case, self.settings)))
        scorer.write_json(self.record_path('responses', index), {**record, **extra})

    def score(self):
        with patch.object(scorer, 'ROOT', self.root), contextlib.redirect_stdout(io.StringIO()):
            return scorer.score(self.folder)


class LocalMedicalScorerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.fixture = MedicalRunFixture(Path(self.temp.name))

    def test_all_cases_remain_in_separate_native_group_denominators(self):
        result = self.fixture.score()
        self.assertEqual(result['planned'], 7)
        self.assertEqual(result['requests_saved'], 6)
        self.assertEqual(result['responses_saved'], 5)
        self.assertEqual(result['completed'], 4)
        self.assertEqual(result['parsed'], 3)
        self.assertEqual(result['invalid_outputs'], 1)
        self.assertEqual(result['missing_or_failed_outputs'], 3)
        self.assertEqual(result['truncated_outputs'], 1)
        self.assertEqual(result['input_modalities'], ['image', 'question_text'])
        self.assertIsNone(result['explanation_support_score'])
        self.assertAlmostEqual(result['metrics']['open_token_recall'], 1 / 3)
        self.assertEqual(result['metrics']['closed_accuracy'], .5)
        self.assertNotIn('accuracy', result['metrics'])
        self.assertEqual(result['metrics_by_answer_type']['OPEN']['eligible'], 3)
        self.assertEqual(result['metrics_by_answer_type']['CLOSED']['eligible'], 4)
        self.assertEqual(result['case_scope'], 'INCOMPLETE_frozen_reviewed_case_set')
        rows = json.loads((self.fixture.folder / 'per_case_scores.json').read_text())
        self.assertEqual(len(rows), 7)
        self.assertEqual(rows[4]['status'], 'not_dispatched')
        self.assertEqual(rows[5]['status'], 'interrupted_unknown_completion')
        with (self.fixture.folder / 'metrics.csv').open() as handle:
            csv_rows = list(csv.DictReader(handle))
        self.assertEqual([int(row['eligible']) for row in csv_rows], [3, 4])
        self.assertEqual([row['units'] for row in csv_rows], ['fraction_0_1', 'fraction_0_1'])

    def test_output_lock_is_written_before_reference_bytes_are_read(self):
        # A label also listed among frozen files is hashed only after the output lock.
        self.fixture.settings['frozen_files_sha256']['data/medical/labels.jsonl'] = scorer.file_digest(self.fixture.label_file)
        self.fixture.save_manifest()
        original_read = Path.read_bytes
        reference_reads = []
        def read(path):
            if path == self.fixture.label_file:
                self.assertTrue((self.fixture.folder / 'scoring_output_lock.json').exists())
                reference_reads.append(path)
            return original_read(path)
        with patch.object(Path, 'read_bytes', read):
            self.fixture.score()
        self.assertEqual(len(reference_reads), 1)

    def test_frozen_input_mutation_fails_before_label_read_or_lock(self):
        self.fixture.input_file.write_text(self.fixture.input_file.read_text() + '\n')
        with self.assertRaisesRegex(ValueError, 'Frozen file changed'):
            self.fixture.score()
        self.assertFalse((self.fixture.folder / 'scoring_output_lock.json').exists())

    def test_reference_hash_mismatch_fails_after_predictions_are_locked(self):
        self.fixture.label_file.write_text(self.fixture.label_file.read_text() + '\n')
        with self.assertRaisesRegex(ValueError, 'Scorer references differ'):
            self.fixture.score()
        self.assertTrue((self.fixture.folder / 'scoring_output_lock.json').exists())

    def test_changed_or_new_raw_outputs_cannot_be_rescored(self):
        self.fixture.score()
        path = self.fixture.record_path('responses', 0)
        path.write_text(path.read_text() + '\n')
        with self.assertRaisesRegex(ValueError, 'output lock changed'):
            self.fixture.score()

    def test_wrong_request_payload_and_model_provenance_fail(self):
        path = self.fixture.record_path('requests', 0)
        request = json.loads(path.read_text())
        request['payload']['messages'][0]['content'][0]['text'] = 'Changed synthetic prompt'
        scorer.write_json(path, request)
        with self.assertRaisesRegex(ValueError, 'Archived request differs'):
            self.fixture.score()

    def test_reference_answer_group_cannot_enter_model_input(self):
        case = self.fixture.cases[0]
        case['answer_type'] = 'OPEN'
        with self.assertRaises(ValueError):
            scorer.expected_payload(case, self.fixture.settings)

    def test_completed_multiple_generations_are_rejected(self):
        path = self.fixture.record_path('responses', 0)
        response = json.loads(path.read_text())
        response['response']['choices'].append(response['response']['choices'][0])
        scorer.write_json(path, response)
        with self.assertRaisesRegex(ValueError, 'single-completion'):
            self.fixture.score()

    def test_unrepresented_group_is_null_and_not_fabricated_zero(self):
        metrics, groups = scorer.metrics_for([])
        self.assertIsNone(metrics['open_token_recall'])
        self.assertIsNone(metrics['closed_accuracy'])
        self.assertEqual(groups['OPEN']['eligible'], 0)


if __name__ == '__main__':
    unittest.main()
