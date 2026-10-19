"""Synthetic parser, immutable-provenance and full-denominator comparison checks."""
import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location('comparison', Path(__file__).parents[1] / 'scripts/score_model_comparison.py')
m = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(m)
POLICY = json.loads((Path(__file__).parents[1] / 'configs/comparison_answer_policy_v1.json').read_text())


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value))
    return {'path': str(path), 'sha256': m.file_sha(path)}


def lines(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(''.join(json.dumps(r) + '\n' for r in rows))
    return {'path': str(path), 'sha256': m.file_sha(path)}


class Fixture:
    def __init__(self, root):
        self.root = root
        self.policy = copy.deepcopy(POLICY)
        self.policy['uncertainty']['bootstrap_replicates'] = 200
        const = root / 'constant.py'
        const.write_text('MCQ_REGEX_TEMPLATE_1 = ' + repr(self.policy['native_lab']['regex']) + '\n')
        self.policy['native_lab']['constant_sha256'] = m.file_sha(const)
        constant = {'path': str(const), 'sha256': m.file_sha(const)}
        self.ids = ['synthetic-' + str(i) for i in range(4)]
        inputs = [{'task': 'B01', 'case_id': case, 'variant': 'SYNTHETIC', 'prompt': 'Synthetic question ' + case} for case in self.ids]
        input_record = lines(root / 'inputs.jsonl', inputs)
        refs = [{'task': 'B01', 'case_id': case, 'target_choice': target,
                 'unsure_choice': 'C', 'choice_count': 3} for case, target in zip(self.ids, ['A', 'A', 'B', 'A'])]
        reference_record = lines(root / 'references.jsonl', refs)
        source_run = {'configuration': {'run_id': 'original-qwen', 'model': 'qwen', 'model_revision': 'revision', 'variant': 'SYNTHETIC',
                      'scorer_reference_sha256': reference_record['sha256'],
                      'frozen_files_sha256': {'sources/chembench_constant.py': constant['sha256']}}}
        source_run_record = write(root / 'run_manifest.json', source_run)
        self.candidate = {'task_id': 'B01', 'source_qwen_run_id': 'original-qwen', 'source_protocol_variant': 'SYNTHETIC',
                          'model': 'qwen', 'model_revision': 'revision', 'run_artifacts': {'run_manifest.json': source_run_record},
                          'frozen_input_artifact': input_record, 'frozen_case_contract_sha256': m.digest(inputs),
                          'source_case_ids_sha256': m.digest(self.ids), 'counts': {'planned': 4},
                          'source_reference_archive': reference_record}
        cases, frozen = [], []
        for i, case in enumerate(self.ids):
            payload = {'model': 'qwen', 'messages': [{'role': 'user', 'content': inputs[i]['prompt']}]}
            request = {'task': 'B01', 'case_id': case, 'payload': payload, 'request_sha256': m.digest(payload)}
            final = '[ANSWER]' + ['A', 'B', 'C', 'A'][i] + '[/ANSWER]'
            response = {'task': 'B01', 'case_id': case, 'model': 'qwen', 'model_revision': 'revision', 'variant': 'SYNTHETIC',
                        'request_sha256': m.digest(payload), 'http_status': 200, 'status': 'completed',
                        'response': {'choices': [{'message': {'content': final}, 'finish_reason': 'stop'}]}}
            request_record = write(root / f'original/{i}/request.json', request)
            response_record = write(root / f'original/{i}/response.json', response)
            cases.append({'task_id': 'B01', 'case_id': case, 'source_qwen_run_id': 'original-qwen',
                          'source_protocol_variant': 'SYNTHETIC', 'request_artifact': request_record,
                          'response_artifact': response_record, 'request_payload_sha256': m.digest(payload)})
            new_payload = {'model': 'luna', 'input': [{'role': 'user', 'content': [{'type': 'input_text', 'text': inputs[i]['prompt']}]}]}
            frozen.append({'task_id': 'B01', 'case_id': case, 'payload_sha256': m.digest(new_payload),
                           'payload_without_private_safety_identifier': new_payload})
        self.candidate_record = write(root / 'candidates.json', {'tasks': [self.candidate]})
        self.manifest_record = lines(root / 'cases.jsonl', cases)
        self.frozen_record = lines(root / 'frozen.jsonl', frozen)
        qlock = m.export_qwen_lock(root / 'candidates.json', root / 'cases.jsonl', ['B01'], root / 'qwen', root=root, protocol_id='panel', run_id='archive-panel')
        lock_rows = []
        for i, row in enumerate(frozen):
            folder = root / 'openai' / str(i)
            request = {'payload_without_private_safety_identifier': row['payload_without_private_safety_identifier']}
            final = ['[ANSWER]A[/ANSWER] [ANSWER]B[/ANSWER]', '[ANSWER]A[/ANSWER]', '[ANSWER]C[/ANSWER]', '[ANSWER]A[/ANSWER]'][i]
            truncated = i == 3
            raw = {'model': 'luna', 'status': 'incomplete' if truncated else 'completed', 'output': [{'type': 'message', 'role': 'assistant',
                   'content': [{'type': 'output_text', 'text': final}]}], 'incomplete_details': {'reason': 'max_output_tokens'} if truncated else None}
            rr = write(folder / 'request.json', request)
            br = write(folder / 'body.json', raw)
            (folder / 'final.txt').write_text(final)
            lock_rows.append({'task_id': 'B01', 'case_id': row['case_id'], 'protocol_id': 'panel', 'model': 'luna', 'run_id': 'new-luna',
                              'payload_sha256': row['payload_sha256'], 'request_path': str(i) + '/request.json', 'request_sha256': rr['sha256'],
                              'response_path': str(i) + '/body.json', 'response_sha256': br['sha256'],
                              'visible_final_path': str(i) + '/final.txt', 'visible_final_sha256': m.file_sha(folder / 'final.txt'),
                              'terminal_status': 'completed', 'finish_status': raw['status'], 'empty_final': False,
                              'truncated': truncated, 'refused': False, 'http_status': 200})
        protocol = write(root / 'protocol.json', {'protocol_id': 'panel'})
        self.olock = {'frozen_protocol_sha256': protocol['sha256'], 'frozen_request_file_sha256': self.frozen_record['sha256'], 'case_count': 4, 'protocol_id': 'panel', 'model': 'luna', 'run_id': 'new-luna', 'scoring_performed': False, 'rows': lock_rows}
        self.olock_path = root / 'openai/predictions_lock.json'
        self.plan = {'comparison_id': 'synthetic-comparison', 'tasks': ['B01'], 'candidates': self.candidate_record,
                     'case_manifest': self.manifest_record, 'answer_policy': write(root / 'policy.json', self.policy),
                     'native_constant': constant, 'frozen_protocol': protocol, 'frozen_request_file': self.frozen_record,
                     'qwen': {'model': 'qwen', 'run_id': 'archive-panel', 'protocol_id': 'panel', 'response_style': 'qwen_archive',
                              'lock': {'path': qlock['path'], 'sha256': qlock['sha256']}},
                     'openai': {'model': 'luna', 'run_id': 'new-luna', 'protocol_id': 'panel', 'response_style': 'openai_responses', 'lock': {}}}
        self.reseal()
        self.plan_path = root / 'plan.json'
        self.save_plan()

    def reseal(self):
        record = write(self.olock_path, self.olock)
        self.olock_path.with_suffix('.sha256').write_text(record['sha256'] + '\n')
        self.plan['openai']['lock'] = record

    def save_plan(self):
        write(self.root / 'plan.json', self.plan)

    def score(self):
        self.save_plan()
        return m.score_comparison(self.root / 'plan.json', self.root)


class ParserTests(unittest.TestCase):
    def test_native_preserves_permissive_conflicting_tags(self):
        text = '[ANSWER]B[/ANSWER] then [ANSWER]A[/ANSWER]'
        self.assertEqual(m.native_lab_answer(text, 3, POLICY['native_lab']['regex']), 'A')
        self.assertIsNone(m.unambiguous_lab_answer(text, 3))

    def test_strict_tags_and_plain_fallback(self):
        self.assertEqual(m.unambiguous_lab_answer('[ANSWER]B[/ANSWER] [ANSWER]B[/ANSWER]', 3), 'B')
        for text in ['[ANSWER]A,B[/ANSWER]', '[ANSWER]D[/ANSWER]', '[ANSWER]A</ANSWER>', '[ANSWER]A', ' A ', 'A B']:
            self.assertIsNone(m.unambiguous_lab_answer(text, 3), text)
        self.assertEqual(m.unambiguous_lab_answer('A', 3), 'A')

    def test_p03_only_native_ten_classes(self):
        for text, expected in [('Answer: 9.', 9), (' 0 ', 0), ('10', None), ('9 or 1', None), ('Nucleus', None)]:
            self.assertEqual(m.p03_answer(text), expected)

    def test_exact_discordance_math(self):
        self.assertEqual(m.exact_mcnemar(0, 0), 1)
        self.assertAlmostEqual(m.exact_mcnemar(5, 0), .0625)
        self.assertAlmostEqual(m.exact_mcnemar(0, 5), .0625)
        self.assertAlmostEqual(m.exact_mcnemar(2, 2), 1)
        self.assertGreater(m.exact_mcnemar(1500, 1500), .999)

    def test_group_bootstrap_requires_complete_groups(self):
        rows = [{'task_id': 'B01', 'case_id': str(i), 'native_correct': False} for i in range(3)]
        with self.assertRaisesRegex(ValueError, 'group metadata'):
            m.paired_analysis(rows, rows, 'native_correct', grouping='group', replicates=100)
        for row in rows:
            row['group_id'] = 'one-paper'
        result = m.paired_analysis(rows, rows, 'native_correct', grouping='group', replicates=100)
        self.assertEqual(result['resampling_unit_count'], 1)
        self.assertEqual(result['paired_bootstrap_percentile_interval'], [0, 0])


class DispatcherIntegrationTests(unittest.TestCase):
    def test_actual_dispatcher_lock_is_accepted_for_all_terminal_outcomes(self):
        spec = importlib.util.spec_from_file_location('dispatcher', Path(__file__).parents[1] / 'scripts/run_isolated_openai_comparison.py')
        d = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(d)
        rows = []
        for i in range(6):
            payload = {'model': 'gpt-6-luna', 'input': [{'role': 'user', 'content': [{'type': 'input_text', 'text': 'Artificial arithmetic case ' + str(i)}]}],
                       'reasoning': {'effort': 'medium'}, 'max_output_tokens': 4096, 'service_tier': 'default', 'store': False}
            rows.append({'task_id': 'B01', 'case_id': str(i), 'payload_without_private_safety_identifier': payload, 'payload_sha256': m.digest(payload)})
        manifest = {'model': 'gpt-6-luna', 'protocol_id': 'synthetic-integration',
                    'requests_sha256': 'a' * 64, 'frozen_protocol_sha256': 'b' * 64,
                    'source_roster_sha256': 'c' * 64, 'dispatcher_sha256': m.file_sha(Path(d.__file__))}
        normal = {'model': 'gpt-6-luna', 'status': 'completed', 'output': [{'type': 'message', 'role': 'assistant',
                  'content': [{'type': 'output_text', 'text': '[ANSWER]A[/ANSWER]'}]}]}
        truncated = dict(normal, status='incomplete', output=[], incomplete_details={'reason': 'max_output_tokens'})
        empty = dict(normal, output=[])
        refused = dict(normal, output=[{'type': 'refusal', 'refusal': 'Artificial refusal fixture'}])
        replies = [(200, d.canonical(normal)), (200, d.canonical(truncated)), (200, d.canonical(empty)),
                   (500, b'<html>Artificial 500</html>'), ValueError('Artificial transport failure'), (200, d.canonical(refused))]
        calls = []
        def transport(body):
            index = len(calls)
            calls.append(body)
            reply = replies[index]
            if isinstance(reply, Exception):
                raise reply
            return reply
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / 'output'
            output.mkdir()
            d.run_cases(manifest, rows, output, 'synthetic-run', 'SYNTHETIC_PRIVATE_IDENTIFIER', transport, workers=1)
            lock_path = output / 'predictions_lock.json'
            lock, verified = m.validate_lock(temporary, {'path': str(lock_path), 'sha256': m.file_sha(lock_path)}, rows,
                    {'model': 'gpt-6-luna', 'protocol_id': 'synthetic-integration', 'run_id': 'synthetic-run', 'response_style': 'openai_responses'},
                    {(r['task_id'], r['case_id']): r for r in rows})
            self.assertEqual(len(verified), 6)
            self.assertEqual(sum(r['delivery_valid'] for r in verified), 1)
            self.assertEqual(sum(r['observed_truncated'] for r in verified), 1)
            self.assertEqual(sum(r['observed_refused'] for r in verified), 1)
            self.assertEqual(lock['new_inference_calls'], 6)  # Injected transport only; no network.


class ProvenanceAndScoringTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.fixture = Fixture(Path(self.tmp.name))

    def test_full_denominators_and_native_strict_disagreement(self):
        result = self.fixture.score()['tasks']['B01']
        self.assertEqual(result['qwen']['planned'], 4)
        self.assertEqual(result['qwen']['native_correct'], 2)
        self.assertEqual(result['openai']['native_correct'], 2)
        self.assertEqual(result['openai']['unambiguous_correct'], 1)
        self.assertEqual(result['openai']['truncations'], 1)
        self.assertEqual(result['openai']['explicit_parsed_abstentions'], 1)
        self.assertEqual(result['openai']['native_parsed'], 3)
        self.assertEqual([result['native_paired'][key] for key in ['both_correct', 'openai_only_correct', 'qwen_only_correct', 'both_wrong']], [1, 1, 1, 1])

    def test_incomplete_lock_fails_before_opening_references(self):
        self.fixture.olock['rows'].pop()
        self.fixture.reseal()
        with patch.object(m, 'load_references', side_effect=AssertionError('Labels opened too early')):
            with self.assertRaisesRegex(ValueError, 'Incomplete'):
                self.fixture.score()

    def test_missing_lock_or_seal_rejected(self):
        self.fixture.olock_path.with_suffix('.sha256').unlink()
        with self.assertRaisesRegex(ValueError, 'seal'):
            self.fixture.score()

    def test_wrong_run_rejected_even_with_resealed_lock(self):
        self.fixture.olock['rows'][0]['run_id'] = 'different-replay'
        self.fixture.reseal()
        with self.assertRaisesRegex(ValueError, 'identity'):
            self.fixture.score()

    def test_actual_request_modification_cannot_be_hidden_by_reseal(self):
        path = self.fixture.root / 'openai/0/request.json'
        value = m.read_json(path)
        value['payload_without_private_safety_identifier']['input'][0]['content'][0]['text'] += ' Answer is A.'
        write(path, value)
        self.fixture.olock['rows'][0]['request_sha256'] = m.file_sha(path)
        self.fixture.reseal()
        with self.assertRaisesRegex(ValueError, 'frozen payload'):
            self.fixture.score()

    def test_visible_final_must_equal_raw_response(self):
        path = self.fixture.root / 'openai/0/final.txt'
        path.write_text('A')
        self.fixture.olock['rows'][0]['visible_final_sha256'] = m.file_sha(path)
        self.fixture.reseal()
        with self.assertRaisesRegex(ValueError, 'actual response'):
            self.fixture.score()

    def test_traversal_rejected(self):
        self.fixture.olock['rows'][0]['response_path'] = '../references.jsonl'
        self.fixture.reseal()
        with self.assertRaisesRegex(ValueError, 'sealed directory'):
            self.fixture.score()

    def test_missing_reference_is_blocker_not_reconstructed_from_qwen(self):
        (self.fixture.root / 'references.jsonl').unlink()
        with self.assertRaisesRegex(ValueError, 'artifact'):
            self.fixture.score()

    def test_wrong_original_contract_hash_rejected(self):
        value = m.read_json(self.fixture.root / 'candidates.json')
        value['tasks'][0]['frozen_case_contract_sha256'] = 'f' * 64
        self.fixture.plan['candidates'] = write(self.fixture.root / 'candidates.json', value)
        with self.assertRaisesRegex(ValueError, 'input contract'):
            self.fixture.score()

    def test_http_error_raw_html_retained_wrong_in_full_denominator(self):
        row = self.fixture.olock['rows'][0]
        body = self.fixture.root / 'openai/0/body.json'
        body.write_text('<html>503 unavailable</html>')
        final = self.fixture.root / 'openai/0/final.txt'
        final.write_text('')
        row.update(terminal_status='http_error', http_status=503, empty_final=True,
                   response_sha256=m.file_sha(body), visible_final_sha256=m.file_sha(final))
        self.fixture.reseal()
        result = self.fixture.score()['tasks']['B01']['openai']
        self.assertEqual(result['planned'], 4)
        self.assertEqual(result['transport_or_server_errors'], 1)
        self.assertEqual(result['native_correct'], 1)

    def test_refusal_with_answer_text_is_invalid(self):
        body = self.fixture.root / 'openai/1/body.json'
        raw = m.read_json(body)
        raw['output'][0]['content'].append({'type': 'refusal', 'refusal': 'Synthetic refusal'})
        write(body, raw)
        self.fixture.olock['rows'][1]['response_sha256'] = m.file_sha(body)
        self.fixture.olock['rows'][1]['refused'] = True
        self.fixture.reseal()
        result = self.fixture.score()['tasks']['B01']['openai']
        self.assertEqual(result['refusals'], 1)
        self.assertEqual(result['native_correct'], 1)

    def test_wrong_actual_response_model_rejected(self):
        body = self.fixture.root / 'openai/0/body.json'
        raw = m.read_json(body)
        raw['model'] = 'other-model'
        write(body, raw)
        self.fixture.olock['rows'][0]['response_sha256'] = m.file_sha(body)
        self.fixture.reseal()
        with self.assertRaisesRegex(ValueError, 'actual response model'):
            self.fixture.score()

    def test_wrong_frozen_request_lock_association_rejected(self):
        self.fixture.olock['frozen_request_file_sha256'] = '0' * 64
        self.fixture.reseal()
        with self.assertRaisesRegex(ValueError, 'different frozen request'):
            self.fixture.score()

    def test_wrong_native_constant_rejected(self):
        self.fixture.plan['native_constant']['sha256'] = '0' * 64
        with self.assertRaisesRegex(ValueError, 'artifact'):
            self.fixture.score()


if __name__ == '__main__':
    unittest.main()
