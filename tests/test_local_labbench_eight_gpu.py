"""Synthetic admission tests for additional local replicas; no model requests."""
import copy
import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import run_local_labbench_eight_gpu as expanded
import run_local_labbench_multimodal as frozen


class ExpandedReplicaTests(unittest.TestCase):
    def setUp(self):
        self.authority = dict(model='synthetic', revision='r1',
                              benchmark_inference_authorized=True,
                              approved_task_ids=['P12'], model_directory='/synthetic',
                              checkpoint_precision='BF16')
        self.serving = dict(self.authority, host='127.0.0.1', port=8031,
                            gpu_ids=[1], tensor_parallel_size=1, max_num_seqs=4)
        self.settings = dict(model='synthetic', model_revision='r1',
                             approved_task_ids=['P12'], endpoint='http://127.0.0.1:8031/v1',
                             gpu_ids=[1], concurrency=4)

    def test_every_declared_physical_gpu_mapping_is_admitted(self):
        for gpu, port in {5:8026, 6:8027, 7:8028, 4:8029, 0:8030, 1:8031, 2:8032, 3:8033}.items():
            serving = dict(self.serving, gpu_ids=[gpu], port=port)
            settings = dict(self.settings, gpu_ids=[gpu], endpoint=f'http://127.0.0.1:{port}/v1')
            expanded.validate_serving_contract(settings, self.authority, serving)
            record = dict(pid=123, proc_start_ticks='456', model='synthetic', revision='r1',
                          gpu_ids=[gpu], endpoint=settings['endpoint'])
            expanded.validate_server_identity(record, settings, serving, '456')

    def test_valid_local_ports_cannot_be_assigned_to_wrong_physical_gpu(self):
        for gpu in range(8):
            if gpu == 1:
                continue
            with self.assertRaises(ValueError):
                expanded.validate_serving_contract(dict(self.settings, gpu_ids=[gpu]), self.authority,
                                                   dict(self.serving, gpu_ids=[gpu]))

    def test_replicas_cannot_authorize_tasks_or_change_checkpoint(self):
        for change in [dict(approved_task_ids=['P18']), dict(gpu_ids=[True]), dict(gpu_ids=[1,2]),
                       dict(concurrency=5), dict(model_revision='other')]:
            with self.assertRaises(ValueError):
                expanded.validate_serving_contract(dict(self.settings, **change), self.authority, self.serving)
        for change in [dict(checkpoint_precision='FP8'), dict(tensor_parallel_size=2),
                       dict(model_directory='/other'), dict(host='localhost')]:
            with self.assertRaises(ValueError):
                expanded.validate_serving_contract(self.settings, self.authority, dict(self.serving, **change))
        with self.assertRaises(ValueError):
            expanded.validate_serving_contract(self.settings,
                                               dict(self.authority, benchmark_inference_authorized=False), self.serving)

    def test_payload_and_request_record_are_unchanged(self):
        settings = dict(self.settings, variant='SYNTHETIC', model_facing_fields=['complete_sequence'],
                        generation=dict(max_tokens=4096, temperature=1.0, top_p=.95, top_k=20,
                                        seed=42, n=1, chat_template_kwargs=dict(enable_thinking=True, reasoning_effort='medium')))
        case = dict(task='P12', case_id='synthetic-1', variant='SYNTHETIC', split='synthetic',
                    messages=[dict(role='user', content='Synthetic sequence: MAAA\nPreserve spacing.  ')])
        original = copy.deepcopy(case)
        self.assertEqual(expanded.payload_for(case, settings), frozen.payload_for(case, settings))
        self.assertEqual(expanded.request_record(case, settings), frozen.request_record(case, settings))
        self.assertEqual(case, original)


if __name__ == '__main__':
    unittest.main()
