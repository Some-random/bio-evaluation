import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('v06_export_test',ROOT/'scripts/export_v06_condition_20261021.py')
export=importlib.util.module_from_spec(spec);spec.loader.exec_module(export)


class ExportTests(unittest.TestCase):
    def test_solver_image_bytes_removed_with_original_payload_unchanged(self):
        payload={'model':'artificial','temperature':0,'top_p':1,'max_tokens':16384,'chat_template_kwargs':{'enable_thinking':False},
            'messages':[{'role':'user','content':[{'type':'image_url','image_url':{'url':'data:image/png;base64,PRIVATE_IMAGE_SENTINEL'}},
                                               {'type':'text','text':'Invented neutral question.'}]}]}
        original=copy.deepcopy(payload);public=export.public_request(payload,'solver')
        self.assertEqual(payload,original)
        self.assertNotIn('PRIVATE_IMAGE_SENTINEL',json.dumps(public))
        self.assertEqual(public['payload']['messages'][0]['content'][1]['text'],'Invented neutral question.')
        self.assertEqual(public['representation'],'public_transformed_input_not_original_replay_request')

    def test_judge_reference_context_removed_candidate_and_pin_preserved(self):
        quoted={'quoted_case':{'question_id':7,'question':'Invented question.','reference_answer':'REFERENCE_SENTINEL',
            'figure_context':{'caption':'SCORER_CONTEXT_SENTINEL'},'candidate_answer':'Invented candidate.'},'judge_declaration_sha256':'a'*64}
        payload={'model':'artificial','temperature':0,'top_p':1,'max_tokens':16384,'chat_template_kwargs':{},
            'messages':[{'role':'system','content':'Artificial rubric.'},{'role':'user','content':json.dumps(quoted)}]}
        original=copy.deepcopy(payload);public=export.public_request(payload,'judge')
        self.assertEqual(payload,original)
        self.assertNotIn('REFERENCE_SENTINEL',json.dumps(public))
        self.assertNotIn('SCORER_CONTEXT_SENTINEL',json.dumps(public))
        data=json.loads(public['payload']['messages'][1]['content'])
        self.assertEqual(data['quoted_case']['candidate_answer'],'Invented candidate.')
        self.assertEqual(data['judge_declaration_sha256'],'a'*64)

    def fixture(self,root,*,valid=193,primary=True):
        continuation=root/'continuation';run=root/'run';source=root/'source'
        for path in [continuation,run,source]:path.mkdir()
        def save(path,value):path.write_bytes(export.encoded(value))
        plan={'output_root':str(run),'source_output_root':str(source),'run_id':'artificial_run',
            'condition':'ARTIFICIAL_CONDITION','model_configuration':{'max_tokens':16384},'frozen_files_sha256':{}}
        save(continuation/'plan.json',plan);(continuation/'plan.sha256').write_text(export.sha(continuation/'plan.json')+'\n')
        save(run/'completion.json',{'benchmark_primary_defined':primary,'new_judge':{'attempted_with_observed_outcome':31},
            'judge':{'responses_saved':193},'new_solver_calls':0})
        save(source/'prediction_lock.json',{'artificial_seal':True})
        (run/'source_prediction_lock.json').write_bytes((source/'prediction_lock.json').read_bytes())
        outcomes=[]
        for qid in range(193):
            folder=(source if qid<162 else run)/'judge'/f'{qid:03d}'
            folder.mkdir(parents=True)
            save(folder/'request.json',{'artificial_request':qid})
            save(folder/'response.body',{'artificial_response':qid})
            row={'question_id':qid,'status':'completed','request_sha256':export.sha(folder/'request.json'),
                 'raw_response_sha256':export.sha(folder/'response.body')}
            outcomes.append(row)
            if qid>=162:save(folder/'parsed_outcome.json',row)
        save(run/'judge_outcomes.json',outcomes)
        save(run/'judgements.json',[{'question_id':qid} for qid in range(193)])
        save(run/'judge_lock.json',{'outcomes_sha256':export.sha(run/'judge_outcomes.json'),
            'judgements_sha256':export.sha(run/'judgements.json'),
            'source_prediction_lock_sha256':export.sha(run/'source_prediction_lock.json')})
        save(run/'scores.json',{'execution_condition':plan['condition'],'groups':{'overall':{
            'planned':193,'valid':valid,'complete':valid==193,'released_mean_case_ratio_score':42.0}}})
        return continuation,run,source

    def test_complete193_exports_exact_score_bytes(self):
        with tempfile.TemporaryDirectory() as temporary:
            root=Path(temporary);continuation,run,_=self.fixture(root)
            scanner=type('Scanner',(),{'scan_file':lambda self,path:None})()
            with patch.object(export,'ROOT',root),patch.object(export,'CONTINUATION',continuation):
                rows=export.export_v06(scanner,archive=False)
            self.assertEqual(rows[0]['counts']['parsed'],193)
            self.assertEqual((root/rows[0]['source_scores']).read_bytes(),(run/'scores.json').read_bytes())

    def test_saved193_cannot_promote_missing_judgements(self):
        with tempfile.TemporaryDirectory() as temporary:
            root=Path(temporary);continuation,_,_=self.fixture(root,valid=162)
            with patch.object(export,'ROOT',root),patch.object(export,'CONTINUATION',continuation):
                with self.assertRaises(ValueError):export.export_v06(None,archive=False)
            self.assertFalse((root/'results').exists())

    def test_changed_source_prediction_lock_blocks_export(self):
        with tempfile.TemporaryDirectory() as temporary:
            root=Path(temporary);continuation,_,source=self.fixture(root)
            (source/'prediction_lock.json').write_text('{}')
            with patch.object(export,'ROOT',root),patch.object(export,'CONTINUATION',continuation):
                with self.assertRaises(ValueError):export.export_v06(None,archive=False)

    def test_undefined_primary_produces_no_completed_row(self):
        with tempfile.TemporaryDirectory() as temporary:
            root=Path(temporary);continuation,_,_=self.fixture(root,primary=False)
            with patch.object(export,'ROOT',root),patch.object(export,'CONTINUATION',continuation):
                self.assertEqual(export.export_v06(None,archive=False),[])


if __name__=='__main__':unittest.main()
