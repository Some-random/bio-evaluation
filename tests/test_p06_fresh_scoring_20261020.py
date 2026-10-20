"""Invented three-row regression lock/denominator checks; no biological data."""
from contextlib import redirect_stdout
import hashlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import run_scalar_catalog_20261020 as common
import score_p06_fresh_20261020 as scorer


class ScoringTests(unittest.TestCase):
    def fixture(self, base, texts=('1','2','3')):
        inputs=base/'inputs.jsonl';review=base/'review.json';parser=base/'parser.py';refs=base/'refs.jsonl'
        cases=[{'task_id':'P06','case_id':f'toy:{i}','messages':[{'role':'user','content':f'Toy prediction {i}. Return a number.'}]} for i in range(3)]
        inputs.write_text(''.join(json.dumps(case)+'\n' for case in cases))
        review.write_text(json.dumps({'task_id':'P06','approved_case_ids':[c['case_id'] for c in cases]}))
        parser.write_text('def parse_number(text):\n try:return float(text)\n except (ValueError,TypeError):return None\n')
        refs.write_text(''.join(json.dumps({'case_id':f'toy:{i}','target_source_string':str(i)})+'\n' for i in range(3)))
        config={'task_id':'P06','split':'official_test','run_id':'synthetic','protocol_variant':'synthetic',
                'input_file':str(inputs),'input_sha256':common.sha(inputs),'review_file':str(review),'review_sha256':common.sha(review),
                'native_numeric_parser_file':str(parser),'native_numeric_parser_sha256':common.sha(parser),'native_numeric_parser_function':'parse_number',
                'scorer_reference_file':str(refs),'scorer_reference_sha256':common.sha(refs),'planned':3}
        config_hash=hashlib.sha256(common.canonical(config)).hexdigest()
        run=base/'run';run.mkdir()
        for folder in ['requests','responses','outcomes']:(run/folder).mkdir()
        common.create(run/'run_manifest.json',{'configuration':config,'config_sha256':config_hash})
        files={'run_manifest.json':common.sha(run/'run_manifest.json')}
        for case,text in zip(cases,texts):
            key=hashlib.sha256(case['case_id'].encode()).hexdigest()
            body={'choices':[{'finish_reason':'stop','message':{'content':text}}]}
            for folder,value in [('requests',common.payload(case)),('responses',body),('outcomes',{'case_id':case['case_id'],'status':'response_saved'})]:
                relative=f'{folder}/{key}.json';common.create(run/relative,value);files[relative]=common.sha(run/relative)
        common.create(run/'prediction_lock.json',{'config_sha256':config_hash,'files_sha256':files,'reference_labels_opened':False})
        common.create(run/'completion.json',{'config_sha256':config_hash,'planned':3,'prediction_lock_sha256':common.sha(run/'prediction_lock.json')})
        return run

    def test_complete_native_spearman(self):
        with tempfile.TemporaryDirectory() as tmp:
            run=self.fixture(Path(tmp))
            with redirect_stdout(io.StringIO()):result=scorer.score(run)
            self.assertEqual(result['spearman'],1)
            self.assertIsNone(result['spearman_parsed_only'])
            self.assertEqual(result['planned'],3)
            self.assertEqual(result['missing_or_invalid'],0)

    def test_invalid_output_keeps_full_denominator(self):
        with tempfile.TemporaryDirectory() as tmp:
            run=self.fixture(Path(tmp),('1','no value','3'))
            with redirect_stdout(io.StringIO()):result=scorer.score(run)
            self.assertIsNone(result['spearman'])
            self.assertAlmostEqual(result['spearman_parsed_only'],1)
            self.assertEqual(result['planned'],3)
            self.assertEqual(result['missing_or_invalid'],1)

    def test_all_constant_predictions_remain_undefined(self):
        with tempfile.TemporaryDirectory() as tmp:
            run=self.fixture(Path(tmp),('2','2','2'))
            with redirect_stdout(io.StringIO()):result=scorer.score(run)
            self.assertIsNone(result['spearman'])
            self.assertTrue(result['undefined_constant_or_insufficient'])
            self.assertEqual(result['missing_or_invalid'],0)

    def test_ties_use_native_average_ranks(self):
        with tempfile.TemporaryDirectory() as tmp:
            run=self.fixture(Path(tmp),('1','1','3'))
            with redirect_stdout(io.StringIO()):result=scorer.score(run)
            self.assertAlmostEqual(result['spearman'],0.8660254037844387)

    def test_corrupt_lock_rejected_before_missing_refs_are_opened(self):
        with tempfile.TemporaryDirectory() as tmp:
            run=self.fixture(Path(tmp));(run/'prediction_lock.json').write_text('{}')
            (Path(tmp)/'refs.jsonl').unlink()
            with self.assertRaisesRegex(ValueError,'Prediction lock changed'):scorer.score(run)

    def test_no_implicit_rescore(self):
        with tempfile.TemporaryDirectory() as tmp:
            run=self.fixture(Path(tmp))
            with redirect_stdout(io.StringIO()):scorer.score(run)
            with self.assertRaisesRegex(ValueError,'already sealed'):scorer.score(run)


if __name__=='__main__':unittest.main()
