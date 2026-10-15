"""Synthetic-only contracts for the native local vision runner."""
import base64
import copy
import hashlib
import struct
import sys
from pathlib import Path
import unittest
import zlib

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import run_local_labbench as original
import run_local_labbench_multimodal as runner


def synthetic_png():
    def chunk(name, data):
        return struct.pack('!I', len(data)) + name + data + struct.pack('!I', zlib.crc32(name + data))
    return (b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('!2I5B', 1, 1, 8, 2, 0, 0, 0))
            + chunk(b'IDAT', zlib.compress(b'\x00\xff\x00\x00')) + chunk(b'IEND', b''))


class MultimodalContractTests(unittest.TestCase):
    def setUp(self):
        self.png = synthetic_png()
        self.url = 'data:image/png;base64,' + base64.b64encode(self.png).decode('ascii')
        self.settings = {
            'model': 'synthetic-model', 'approved_task_ids': ['B01', 'B04'], 'variant': 'SYNTHETIC',
            'model_facing_fields': ['question', 'shuffled_choices', 'native_COT_instructions', 'native_figure_images'],
            'generation': {'max_tokens': 4096, 'temperature': 1.0, 'top_p': .95, 'top_k': 20,
                           'seed': 42, 'n': 1,
                           'chat_template_kwargs': {'enable_thinking': True, 'reasoning_effort': 'medium'}}}
        self.case = {'task': 'B04', 'case_id': 'synthetic-figure-1', 'variant': 'SYNTHETIC',
                     'split': 'synthetic', 'messages': [{'role': 'user', 'content': [
                         {'type': 'text', 'text': 'Synthetic native question\n(A) left\n(B) right'},
                         {'type': 'image_url', 'image_url': {'url': self.url}}]}]}

    def test_native_image_and_prompt_bytes_are_unchanged(self):
        before = copy.deepcopy(self.case)
        payload = runner.payload_for(self.case, self.settings)
        self.assertEqual(payload['messages'], before['messages'])
        self.assertEqual(self.case, before)
        self.assertEqual(payload['max_tokens'], 4096)
        self.assertNotIn('tools', payload)
        record = runner.request_record(self.case, self.settings)
        self.assertEqual(record['request_sha256'], original.digest(payload))
        self.assertEqual(record['supplied_fields'], self.settings['model_facing_fields'])
        self.assertEqual(record['image_sha256'], [hashlib.sha256(self.png).hexdigest()])
        self.assertEqual(record['supplied_images'][0]['part_index'], 1)
        self.assertEqual(record['supplied_images'][0]['bytes'], len(self.png))
        self.assertEqual(record['supplied_images'][0]['mime_type'], 'image/png')
        self.assertEqual(base64.b64decode(payload['messages'][0]['content'][1]['image_url']['url'].split(',')[1]), self.png)

    def test_multiple_original_image_parts_keep_order_and_hashes(self):
        self.case['messages'][0]['content'].append({'type': 'image_url', 'image_url': {'url': self.url, 'detail': 'high'}})
        record = runner.request_record(self.case, self.settings)
        self.assertEqual([entry['part_index'] for entry in record['supplied_images']], [1, 2])
        self.assertEqual(len(record['image_sha256']), 2)
        self.assertEqual(record['payload']['messages'], self.case['messages'])

    def test_remote_file_and_unsupported_data_urls_fail(self):
        for url in ['https://example.org/image.png', 'http://127.0.0.1/image.png', 'file:///tmp/image.png',
                    'data:image/svg+xml;base64,PHN2Zz4=', 'data:image/png,not-base64', 'data:image/gif;base64,R0lGODlh']:
            bad = copy.deepcopy(self.case)
            bad['messages'][0]['content'][1]['image_url']['url'] = url
            with self.subTest(url=url), self.assertRaises(ValueError):
                runner.payload_for(bad, self.settings)

    def test_extra_answer_bearing_fields_fail_at_every_level(self):
        mutations = [
            lambda c: c.update(target_choice='A'),
            lambda c: c['messages'][0].update(reference_answer='A'),
            lambda c: c['messages'][0]['content'][0].update(answer='A'),
            lambda c: c['messages'][0]['content'][1].update(caption='Gold answer A'),
            lambda c: c['messages'][0]['content'][1]['image_url'].update(reference='A'),
            lambda c: c['messages'][0]['content'].append({'type': 'answer', 'text': 'A'}),
            lambda c: c.update(tools=[]),
        ]
        for mutate in mutations:
            bad = copy.deepcopy(self.case)
            mutate(bad)
            with self.assertRaises(ValueError):
                runner.payload_for(bad, self.settings)

    def test_original_text_payload_is_identical(self):
        text = copy.deepcopy(self.case)
        text['task'] = 'B01'
        text['messages'][0]['content'] = 'Original synthetic prompt\nwith exact spaces.  '
        self.assertEqual(runner.payload_for(text, self.settings), original.payload_for(text, self.settings))
        self.assertEqual(runner.request_record(text, self.settings)['image_sha256'], [])

    def test_tools_multiple_completions_and_extra_messages_fail(self):
        for key, value in [('tools', []), ('n', 2), ('n', True)]:
            settings = copy.deepcopy(self.settings)
            settings['generation'][key] = value
            with self.assertRaises(ValueError):
                runner.payload_for(self.case, settings)
        for field, value in [('tools', []), ('tool_access', ['web'])]:
            settings = copy.deepcopy(self.settings)
            settings[field] = value
            with self.assertRaises(ValueError):
                runner.payload_for(self.case, settings)
        case = copy.deepcopy(self.case)
        case['messages'].append({'role': 'user', 'content': 'extra'})
        with self.assertRaises(ValueError):
            runner.payload_for(case, self.settings)

    def test_invalid_base64_mime_and_detail_fail(self):
        for url in ['data:image/png;base64,@@@@', 'data:image/png;base64,////',
                    'data:image/jpeg;base64,' + base64.b64encode(self.png).decode('ascii')]:
            case = copy.deepcopy(self.case)
            case['messages'][0]['content'][1]['image_url']['url'] = url
            with self.assertRaises(ValueError):
                runner.payload_for(case, self.settings)
        case = copy.deepcopy(self.case)
        case['messages'][0]['content'][1]['image_url']['detail'] = 'answer=A'
        with self.assertRaises(ValueError):
            runner.payload_for(case, self.settings)

    def test_review_order_holds_and_field_declarations_remain_enforced(self):
        review = {'approved_case_ids': ['synthetic-figure-1'], 'held_cases': []}
        runner.validate_cases([self.case], self.settings, review)
        review['held_cases'] = [{'case_id': 'synthetic-figure-1'}]
        with self.assertRaises(ValueError):
            runner.validate_cases([self.case], self.settings, review)
        for fields in [None, [], ['question', 'question'], ['question', 1]]:
            settings = copy.deepcopy(self.settings)
            settings['model_facing_fields'] = fields
            with self.assertRaises(ValueError):
                runner.request_record(self.case, settings)


class ReplicaContractTests(unittest.TestCase):
    def setUp(self):
        self.authority = {'model': 'synthetic-model', 'revision': 'synthetic-revision',
                          'benchmark_inference_authorized': True, 'approved_task_ids': ['B04'],
                          'model_directory': '/synthetic/checkpoint', 'checkpoint_precision': 'BF16'}
        self.serving = {**self.authority, 'host': '127.0.0.1', 'port': 8028, 'gpu_ids': [6],
                        'tensor_parallel_size': 1, 'max_num_seqs': 4}
        self.settings = {'model': 'synthetic-model', 'model_revision': 'synthetic-revision',
                         'approved_task_ids': ['B04'], 'endpoint': 'http://127.0.0.1:8028/v1',
                         'gpu_ids': [6], 'concurrency': 4}
        self.server = {'pid': 123, 'proc_start_ticks': '456', 'model': 'synthetic-model',
                       'revision': 'synthetic-revision', 'gpu_ids': [6]}

    def test_all_predeclared_loopback_replicas_and_original_default(self):
        runner.validate_endpoint('http://127.0.0.1:8026/v1')
        for port, gpu in [(8026, 5), (8027, 4), (8028, 6), (8029, 7)]:
            serving = {**self.serving, 'port': port, 'gpu_ids': [gpu]}
            settings = {**self.settings, 'endpoint': f'http://127.0.0.1:{port}/v1', 'gpu_ids': [gpu]}
            server = {**self.server, 'gpu_ids': [gpu]}
            runner.validate_serving_contract(settings, self.authority, serving)
            runner.validate_server_identity(server, settings, serving, '456')

    def test_wrong_host_and_port_are_rejected_even_when_declared(self):
        for host, port in [('api.openai.com', 8028), ('localhost', 8028), ('127.0.0.1', 8030)]:
            serving = {**self.serving, 'host': host, 'port': port}
            settings = {**self.settings, 'endpoint': f'http://{host}:{port}/v1'}
            with self.assertRaises(ValueError):
                runner.validate_serving_contract(settings, self.authority, serving)
        for endpoint in ['http://127.0.0.1:8026/v1', 'http://127.0.0.1:8027/v1',
                         'http://user:password@127.0.0.1:8028/v1', 'https://127.0.0.1:8028/v1']:
            with self.assertRaises(ValueError):
                runner.validate_serving_contract({**self.settings, 'endpoint': endpoint}, self.authority, self.serving)

    def test_wrong_model_revision_and_precision_are_rejected(self):
        for field, value in [('model', 'other-model'), ('revision', 'other-revision'),
                             ('checkpoint_precision', 'FP8'), ('model_directory', '/other/checkpoint')]:
            with self.assertRaises(ValueError):
                runner.validate_serving_contract(self.settings, self.authority, {**self.serving, field: value})
        for field, value in [('model', 'other-model'), ('model_revision', 'other-revision')]:
            with self.assertRaises(ValueError):
                runner.validate_serving_contract({**self.settings, field: value}, self.authority, self.serving)

    def test_gpu_mismatch_unapproved_gpu_and_parallelism_are_rejected(self):
        with self.assertRaises(ValueError):
            runner.validate_serving_contract({**self.settings, 'gpu_ids': [7]}, self.authority, self.serving)
        for gpu_ids, tp in [([0], 1), ([6, 7], 2), ([6], 2), ([True], 1)]:
            with self.assertRaises(ValueError):
                runner.validate_serving_contract({**self.settings, 'gpu_ids': gpu_ids}, self.authority,
                                                 {**self.serving, 'gpu_ids': gpu_ids, 'tensor_parallel_size': tp})
        with self.assertRaises(ValueError):
            runner.validate_server_identity({**self.server, 'gpu_ids': [7]}, self.settings, self.serving, '456')

    def test_actual_server_process_identity_and_declared_endpoint_are_enforced(self):
        for field, value in [('model', 'other-model'), ('revision', 'other-revision'),
                             ('endpoint', 'http://127.0.0.1:8026/v1'), ('port', 8026), ('host', 'localhost')]:
            with self.assertRaises(ValueError):
                runner.validate_server_identity({**self.server, field: value}, self.settings, self.serving, '456')
        with self.assertRaises(ValueError):
            runner.validate_server_identity(self.server, self.settings, self.serving, '789')

    def test_replica_task_allowlist_cannot_expand_central_authorization(self):
        replica = {**self.serving, 'approved_task_ids': ['B04', 'P18']}
        with self.assertRaises(ValueError):
            runner.validate_serving_contract({**self.settings, 'approved_task_ids': ['P18']}, self.authority, replica)
        runner.validate_serving_contract(self.settings, self.authority, {**replica, 'approved_task_ids': []})
        with self.assertRaises(ValueError):
            runner.validate_serving_contract(self.settings, {**self.authority, 'benchmark_inference_authorized': False}, replica)

    def test_config_and_record_paths_stay_inside_project_metadata_directories(self):
        self.assertEqual(runner.project_file('configs/local_model_gpu6.json', 'configs'), ROOT / 'configs/local_model_gpu6.json')
        for name in ['/etc/passwd', 'configs/../../external.json', '.local/local_model_server.json']:
            with self.assertRaises(ValueError):
                runner.project_file(name, 'configs')


if __name__ == '__main__':
    unittest.main()
