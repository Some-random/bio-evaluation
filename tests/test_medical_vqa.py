"""Synthetic input and scorer contracts; no benchmark answers used as tests."""
import base64
import copy
import hashlib
import importlib.util
import struct
import sys
import tempfile
from pathlib import Path
import unittest
import zlib

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import prepare_medical_vqa as prep


def png_bytes():
    def chunk(name, raw):
        return struct.pack('!I', len(raw)) + name + raw + struct.pack('!I', zlib.crc32(name + raw))
    return (b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('!2I5B', 1, 1, 8, 2, 0, 0, 0))
            + chunk(b'IDAT', zlib.compress(b'\x00\x00\xff\x00')) + chunk(b'IEND', b''))


class MedicalVQAContracts(unittest.TestCase):
    def setUp(self):
        self.raw = png_bytes()
        self.row = {'qid': 'synthetic-1', 'question': 'What synthetic shape is shown?  ',
                    'answer': 'triangle', 'answer_type': 'OPEN', 'phrase_type': 'test_freeform',
                    'q_lang': 'en', 'image_name': 'synthetic.png', 'img_name': 'synthetic/source.png'}

    def test_only_source_question_and_original_bytes_reach_model(self):
        case = prep.model_case('V01', self.row, self.raw)
        self.assertEqual(set(case), {'task', 'case_id', 'variant', 'split', 'messages'})
        message = case['messages'][0]
        self.assertEqual(message['content'][0]['text'], self.row['question'])
        self.assertEqual(base64.b64decode(message['content'][1]['image_url']['url'].split(',')[1]), self.raw)
        self.assertNotIn('target_answer', case)
        self.assertNotIn('answer_type', case)
        self.assertEqual(message['role'], 'user')

    def test_answer_or_group_change_cannot_change_dispatched_inputs(self):
        altered = copy.deepcopy(self.row)
        altered.update(answer='a different hidden target', answer_type='CLOSED',
                       image_case_url='https://example.org/answer-bearing-caption', triple=['gold', 'label'])
        for task in ['V01', 'V02']:
            self.assertEqual(prep.model_case(task, self.row, self.raw), prep.model_case(task, altered, self.raw))

    def test_native_test_selection_uses_only_split_and_language(self):
        train = {**self.row, 'qid': 'train', 'phrase_type': 'freeform'}
        test2 = {**self.row, 'qid': 'test2', 'phrase_type': 'test_para', 'answer': 'different'}
        zh = {**self.row, 'qid': 'zh', 'q_lang': 'zh'}
        self.assertEqual([r['qid'] for r in prep.select_test_rows('V01', [train, self.row, test2])], ['synthetic-1', 'test2'])
        self.assertEqual([r['qid'] for r in prep.select_test_rows('V02', [zh, self.row])], ['synthetic-1'])

    def test_labels_are_separate_and_keep_native_group(self):
        label = prep.label_for('V01', {**self.row, 'answer_type': 'CLOSED '}, hashlib.sha256(self.raw).hexdigest())
        self.assertEqual(label['target_answer'], 'triangle')
        self.assertEqual(label['answer_type'], 'CLOSED')
        with self.assertRaises(ValueError):
            prep.label_for('V01', {**self.row, 'answer_type': 'unknown'}, 'synthetic')

    def test_native_open_token_recall_preserves_verbose_output_behavior(self):
        score = prep.score_answer('The left kidney is visible.', {'target_answer': 'left kidney', 'answer_type': 'OPEN'})
        self.assertEqual(score['open_token_recall'], 1)
        self.assertEqual(score['open_token_precision'], .5)
        self.assertAlmostEqual(score['open_token_f1'], 2 / 3)
        self.assertEqual(prep.score_answer('', {'target_answer': 'left kidney', 'answer_type': 'OPEN'})['open_token_recall'], 0)

    def test_native_closed_substring_quirks_are_not_silently_fixed(self):
        label = {'target_answer': 'No', 'answer_type': 'CLOSED'}
        self.assertEqual(prep.score_answer('No.', label)['closed_native_hit'], 1)
        self.assertEqual(prep.score_answer('Yes.', label)['closed_native_hit'], 0)
        self.assertEqual(prep.score_answer('nobody', label)['closed_native_hit'], 1)
        self.assertEqual(prep.score_answer('yes and no', label)['closed_native_hit'], 1)
        self.assertEqual(prep.score_answer(None, label)['closed_native_hit'], 0)

    def test_native_normalization_number_articles_and_punctuation(self):
        result = prep.score_answer('The two synthetic shapes!', {'target_answer': '2 synthetic shapes', 'answer_type': 'OPEN'})
        self.assertEqual(result['open_token_recall'], 1)
        self.assertEqual(result['open_token_precision'], 1)

    def test_unsafe_paths_and_changed_artifacts_fail(self):
        for name in ['../gold.json', '/tmp/gold.json', 'folder/../../gold.json', 'folder\\gold.json']:
            with self.assertRaises(ValueError):
                prep.safe_member(name)
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'original.bin'
            prep.save_bytes(path, b'original')
            prep.save_bytes(path, b'original')
            with self.assertRaises(ValueError):
                prep.save_bytes(path, b'changed')
        with self.assertRaises(ValueError):
            prep.image_format(b'not an image')


if __name__ == '__main__':
    unittest.main()
