"""Artificial-only delivery/schema/provenance checks for new DeepFRI condition."""
import copy
import hashlib
import json
import io
from pathlib import Path
import sys
import tempfile
import unittest
from types import SimpleNamespace
from unittest.mock import patch

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
import run_deepfri_catalog_20261020 as runner
import score_deepfri_catalog_20261020 as scorer


class DenseConfidenceContractTests(unittest.TestCase):
    def test_full_vector_not_class_keys(self):
        text = '{"scores":['+','.join(['0.125']*538)+']}'
        self.assertEqual(runner.parse_vector(text,538),[.125]*538)
        with self.assertRaises(ValueError):
            runner.parse_vector('{"scores":{"1.1.1.1":0.125}}',538)

    def test_exact_length_no_omission_or_padding(self):
        for text in ['{"scores":[]}','{"scores":[0]}','{"scores":[0,1,0]}']:
            with self.assertRaises(ValueError):
                runner.parse_vector(text,2)

    def test_range_precision_and_json_types(self):
        for value in ['-0.1','1.001','2','0.0001','"0.2"','true','false','null','NaN','Infinity','1e-3']:
            with self.subTest(value=value),self.assertRaises(ValueError):
                runner.parse_vector('{"scores":['+value+']}',1)
        for value in ['0','1','0.0','0.001','0.999','1.000']:
            self.assertEqual(len(runner.parse_vector('{"scores":['+value+']}',1)),1)

    def test_no_duplicate_keys_markdown_multiple_objects_or_extra_fields(self):
        for text in ['{"scores":[0],"scores":[1]}','{"scores":[0],"why":"x"}',
                     '```json\n{"scores":[0]}\n```','{"scores":[0]}{"scores":[0]}']:
            with self.assertRaises(ValueError):
                runner.parse_vector(text,1)

    def test_length_finish_and_empty_final_are_invalid(self):
        for text,finish in [('{"scores":[0]}','length'),('', 'stop'),(None,'stop')]:
            with self.assertRaises(ValueError):
                runner.parse_vector(text,1,finish)

    def body(self,**message):
        return {"model":runner.MODEL,"choices":[{"finish_reason":"stop","message":{"content":'{"scores":[0,1]}',**message}}]}

    def test_reasoning_refusal_and_tools_fail_delivery(self):
        self.assertTrue(runner.parse_delivery(self.body(),2)['delivery_passed'])
        for kw in [{'reasoning':'unfinished thought'},{'refusal':'declined'},{'tool_calls':[{'id':'x'}]}]:
            self.assertFalse(runner.parse_delivery(self.body(**kw),2)['delivery_passed'])

    def test_wrong_model_or_multiple_choices_rejected(self):
        body=self.body();body['model']='another-model'
        with self.assertRaises(ValueError):runner.parse_delivery(body,2)
        body=self.body();body['choices']*=2
        with self.assertRaises(ValueError):runner.parse_delivery(body,2)

    def test_all_four_vector_sizes_fit_same_predeclared_schema(self):
        for task,count in runner.TASKS.items():
            text='{"scores":['+','.join(['0.001']*count)+']}'
            self.assertEqual(len(runner.parse_vector(text,count)),count)
            self.assertFalse(runner.generation_for(count)['chat_template_kwargs']['enable_thinking'])
            self.assertEqual(runner.generation_for(count)['max_tokens'],16384)

    def test_prompt_contains_complete_sequence_and_global_order_only(self):
        classes=[{'index':i,'class_id':f'PUBLIC-{i}','description':f'public class {i}'} for i in range(538)]
        prompt=runner.dense_prompt('P12','ACDEFGHIKLMNPQRSTVWY',classes)
        self.assertIn('Complete amino acid sequence:\nACDEFGHIKLMNPQRSTVWY',prompt)
        self.assertIn('0\tPUBLIC-0\tpublic class 0',prompt)
        self.assertIn('537\tPUBLIC-537\tpublic class 537',prompt)
        self.assertNotIn('case_id',prompt)
        with self.assertRaises(ValueError):runner.dense_prompt('P12','ACDE',list(reversed(classes)))


class GenerationLockTests(unittest.TestCase):
    def fixture(self,directory,split='official_validation'):
        base=Path(directory)
        classes=[{'index':i,'class_id':f'C{i}','description':f'class {i}'} for i in range(538)]
        cases=[{'task_id':'P12','case_id':'invented-case','messages':[{'role':'user','content':runner.dense_prompt('P12','ACDEFGHIK',classes)}]}]
        vocab=base/'vocab.json';vocab.write_text(json.dumps({'classes':classes}))
        inputs=base/'inputs.jsonl';inputs.write_text(json.dumps(cases[0])+'\n')
        review=base/'review.json';review.write_text(json.dumps({'task_id':'P12','approved_case_ids':['invented-case'],'held_cases':[]}))
        config={'schema_version':1,'task_id':'P12','class_count':538,'variant':runner.VARIANT,'model':runner.MODEL,'model_revision':runner.REVISION,
                'split':split,'generation':runner.generation_for(538),'input_file':str(inputs),'input_sha256':runner.sha(inputs),
                'review_file':str(review),'review_sha256':runner.sha(review),'vocabulary_file':str(vocab),'vocabulary_sha256':runner.sha(vocab),
                'files_sha256':{},'planned':1,'run_id':'invented-development'}
        path=base/'config.json';path.write_text(json.dumps(config))
        return path,config,cases

    def test_exact_review_and_injected_reference_fields_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path,config,cases=self.fixture(directory)
            self.assertEqual(len(runner.load_contract(path)[1]),1)
            cases[0]['gold_confidence']=1
            input_path=Path(config['input_file']);input_path.write_text(json.dumps(cases[0])+'\n')
            config['input_sha256']=runner.sha(input_path);path.write_text(json.dumps(config))
            with self.assertRaises(ValueError):runner.load_contract(path)

    def test_changed_frozen_vocabulary_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path,config,cases=self.fixture(directory)
            Path(config['vocabulary_file']).write_text('{}')
            with self.assertRaises(ValueError):runner.load_contract(path)

    def test_full_generation_requires_sealed_perfect_development(self):
        with tempfile.TemporaryDirectory() as directory:
            path,config,cases=self.fixture(directory,split='official_test')
            with self.assertRaises(ValueError):runner.validate_development(config,None)

    def test_development_cannot_be_scored(self):
        with tempfile.TemporaryDirectory() as directory:
            path,config,cases=self.fixture(directory)
            with self.assertRaisesRegex(ValueError,'Development panels'):
                scorer.verify_locked_generation(path,Path(directory)/'not-a-run')

    def test_missing_or_invalid_predictions_never_enter_full_metric(self):
        def forbidden(*args,**kwargs):
            raise AssertionError('An invalid row entered native metrics')
        metrics,diagnostics=scorer.matrix_metrics([[.5,.2],None],[[0],[1]],2,
            {'area_under_prc':forbidden,'f1_max':forbidden})
        self.assertEqual(metrics,{'auprc@micro':None,'f1_max':None})
        self.assertEqual(diagnostics['planned'],2)
        self.assertEqual(diagnostics['invalid_or_missing_vectors'],1)

    def test_artificial_terminal_run_lock_replays_exactly_then_rejects_tampering(self):
        with tempfile.TemporaryDirectory() as directory:
            path,config,cases=self.fixture(directory,split='official_test')
            output=Path(directory)/'run';output.mkdir()
            grant=Path(directory)/'grant.json';grant.write_text('{}')
            args=SimpleNamespace(resume_unattempted=False,grant=grant,model_path='unused',
                                 context_limit=65536,concurrency=1,timeout=1)
            body={'model':runner.MODEL,'choices':[{'finish_reason':'stop','message':{'content':'{"scores":['+','.join(['0']*538)+']}'}}]}
            class ArtificialOpener:
                def open(self,request,timeout):
                    if isinstance(request,str):
                        return io.BytesIO(json.dumps({'data':[{'id':runner.MODEL}]}).encode())
                    return io.BytesIO(json.dumps(body).encode())
            with patch.object(runner,'count_tokens',return_value={'artificial':True}),patch.object(runner.urllib.request,'build_opener',return_value=ArtificialOpener()):
                runner.run_locked(args,path,config,cases,runner.parse_vector,{'endpoint':'http://127.0.0.1:1/v1'},{'artificial':True},output)
            done=json.loads((output/'completion.json').read_text())
            self.assertTrue(done['all_passed'])
            parsed=scorer.verify_locked_generation(path,output)
            self.assertEqual(parsed[2],[[0]*538])
            response=next((output/'responses').iterdir())
            response.write_text('{}')
            with self.assertRaisesRegex(ValueError,'Changed or foreign locked'):
                scorer.verify_locked_generation(path,output)


if __name__=='__main__':
    unittest.main()
