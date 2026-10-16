import base64
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import threading
import unittest
from unittest import mock

SCRIPTS=Path(__file__).parents[1]/'scripts'
sys.path.insert(0,str(SCRIPTS))
import run_local_stride_gfp as r


def case(index=0):
    return {'task_id':'P42','case_id':f'p42:replace_only:{index:03d}',
            'protocol_variant':'QWEN_GFP_QUALIFIED_REPLACE_ONLY_ENDPOINT_1_TO_3',
            'split':'fixed_publisher_anchor_generated_candidates',
            'sample_index':index,'seed':42+index,
            'messages':[{'role':'system','content':'Synthetic system fixture'},
                        {'role':'user','content':'Synthetic user fixture'}]}


def settings():
    return {'model':r.MODEL,'generation':r.GENERATION.copy(),'tool_access':[],
            'endpoint':'http://127.0.0.1:8033/v1','run_id':'synthetic_fixture'}


def good_wire():
    value={'model':r.MODEL,'choices':[{'message':{'content':'{"protein":"ACEE"}',
           'reasoning':'synthetic fixture'},'finish_reason':'stop'}]}
    raw=json.dumps(value).encode()
    return {'http_status':200,'response':value,'raw_response_base64':base64.b64encode(raw).decode(),
            'raw_response_utf8':raw.decode(),'raw_response_sha256':hashlib.sha256(raw).hexdigest(),
            'transport_or_schema_error':None}


class TestGfpRunner(unittest.TestCase):
    def test_payload_retains_roles_distinct_seeds_and_contains_only_permitted_api_fields(self):
        a=r.payload_for(case(0),settings());b=r.payload_for(case(1),settings())
        self.assertEqual([m['role'] for m in a['messages']],['system','user'])
        self.assertEqual(a['seed'],42);self.assertEqual(b['seed'],43)
        self.assertNotEqual(r.digest(a),r.digest(b))
        self.assertNotIn('case_id',a);self.assertNotIn('reference',a);self.assertNotIn('tools',a)
        self.assertEqual(a['max_tokens'],1024);self.assertEqual(a['n'],1)

    def test_input_label_injection_seed_reuse_and_wrong_role_rejected(self):
        for modified in [dict(case(),gold='A'),dict(case(1),seed=42),dict(case(),messages=[{'role':'user','content':'x'}])]:
            with self.assertRaises(ValueError):r.payload_for(modified,settings())
        bad=settings();bad['generation']={**r.GENERATION,'n':10}
        with self.assertRaises(ValueError):r.payload_for(case(),bad)

    def test_disabled_or_wrong_gpu_recipe_rejected_before_any_network(self):
        with self.assertRaises(ValueError):r.validate_settings({'execution_authorized':False})

    def test_native_two_channel_equivalence_and_ambiguous_channel_rejection(self):
        got=r.extract_choice(good_wire()['response'])
        self.assertEqual(got['reasoning_text'],'synthetic fixture')
        response=good_wire()['response'];response['choices'][0]['message']['reasoning_content']='different'
        with self.assertRaises(ValueError):r.extract_choice(response)

    def test_one_saved_request_and_response_then_reuse_without_resampling(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder=Path(tmp);stop=threading.Event()
            with mock.patch.object(r,'http_json',return_value=good_wire()) as call:
                self.assertEqual(r.execute_one(case(),settings(),folder,'ACDE',stop),'completed')
                self.assertEqual(r.execute_one(case(),settings(),folder,'ACDE',stop),'completed')
                self.assertEqual(call.call_count,1)
            response=json.loads(next((folder/'responses').glob('*.json')).read_text())
            self.assertTrue(response['candidate_extraction']['eligible'])
            self.assertEqual(base64.b64decode(response['raw_response_base64']).decode(),response['raw_response_utf8'])

    def test_uncertain_saved_request_is_never_dispatched_again(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder=Path(tmp);r.write_json(folder/'requests'/(r.request_identity(case())+'.json'),{'prior':'request'})
            with mock.patch.object(r,'http_json') as call:
                self.assertEqual(r.execute_one(case(),settings(),folder,'ACDE',threading.Event()),'interrupted_unknown_completion')
                call.assert_not_called()

    def test_transport_error_stops_and_preserves_later_missing_slots(self):
        wire={**good_wire(),'http_status':0,'response':None,'transport_or_schema_error':{'type':'TimeoutError'}}
        with tempfile.TemporaryDirectory() as tmp:
            folder=Path(tmp);stop=threading.Event()
            with mock.patch.object(r,'http_json',return_value=wire) as call:
                self.assertEqual(r.execute_one(case(),settings(),folder,'ACDE',stop),'transport_error')
                self.assertEqual(r.execute_one(case(1),settings(),folder,'ACDE',stop),'not_dispatched_after_error')
                self.assertEqual(call.call_count,1)
            self.assertEqual(len(list((folder/'responses').glob('*.json'))),1)

    def test_lock_contains_complete_slot_list_and_original_hashes(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder=Path(tmp);r.write_json(folder/'run_manifest.json',{'fixture':True});r.write_json(folder/'case_inputs.json',[case(0),case(1)])
            r.write_json(folder/'requests'/(r.request_identity(case())+'.json'),{'fixture':'request'})
            r.write_json(folder/'responses'/(r.request_identity(case())+'.json'),{'fixture':'response'})
            statuses={case()['case_id']:'completed',case(1)['case_id']:'not_dispatched_after_error'}
            terminal=r.seal_generation(folder,settings(),[case(),case(1)],statuses)
            self.assertFalse(terminal['generation_complete']);self.assertEqual(terminal['generation_exit_code'],1)
            lock=json.loads((folder/'generation_artifact_lock.json').read_text())
            self.assertEqual(len(lock['slots']),2);self.assertIsNone(lock['slots'][1]['response_file'])
            self.assertEqual(lock['slots'][0]['response_file_sha256'],r.file_digest(folder/lock['slots'][0]['response_file']))
            self.assertFalse(lock['oracle_forward_performed']);self.assertFalse(lock['scoring_complete'])

if __name__=='__main__':unittest.main()
