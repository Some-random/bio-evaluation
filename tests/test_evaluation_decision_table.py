"""Synthetic tests for aggregate-only decisions, invariance and distinct conditions."""
import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock

SPEC=importlib.util.spec_from_file_location('decision',Path(__file__).resolve().parents[1]/'scripts/update_evaluation_decision_table.py')
report=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(report)


def catalog(tasks):
    return {'meta':{'generatedAt':'2026-10-18T20:00:00+00:00','model':{'name':'synthetic'}},'groups':[
        {'id':task,'category':'Synthetic','task':task,'dataset':'dataset_'+task,'taskIds':[task],
         'status':'Status unverified','inputInterface':'synthetic input','protocols':[{'taskId':task,'title':'Task '+task,'sourceUrl':'https://example.org/'+task}]} for task in tasks]}


def scores(tasks,rows=None):
    return {'generated_at_utc':'2026-10-18T20:00:00+00:00','main_catalog_settings':len(set(tasks)-report.ARCHIVE_IDS),'main_report_scope':{'excluded_task_ids':sorted(report.ARCHIVE_IDS)},'completed_rows':rows or [],'diagnostic_only_finished_runs':[],'excluded_or_not_yet_terminal_runs':[]}


def row(task,run='original',**extra):
    value={'task_id':task,'run_id':run,'protocol_variant':'SYNTHETIC','task_name':'Task '+task,'counts':{'planned':10,'completed':10,'parsed':8,'invalid_outputs':2},'finish_reasons':{'stop':8,'length':2},'generation':{'max_tokens':4096},'metrics':{'accuracy':.4},'source_scores':'results/runs/'+run+'/scores.json','scores_sha256':'pinned-native-hash','case_scope':'synthetic_full'}
    value.update(extra);return value


def reaction_diagnostic():
    return {'post_run_diagnostic':True,'native_score_replaced':False,'native_artifacts_modified':False,
        'inference_or_regeneration':False,'reference_labels_used_to_select_rule':False,
        'clean_directory_reproduction_verified':True,'synthetic_tests':{'passed':True},
        'source_native_run_id':'original','source_native_protocol_variant':'SYNTHETIC',
        'source_scores_sha256':'pinned-native-hash','full_original_denominator':10,
        'counts':{'planned':10,'original_accepted':8,'original_correct':4,
            'diagnostic_accepted':9,'diagnostic_correct':5,'recovered':1,'recovered_correct':1},
        'native_accuracy_unchanged':.4,'diagnostic_accuracy':.5,'diagnostic_variant':'SYNTHETIC_DIAGNOSTIC',
        'diagnostic_result_sha256':'inner-result-hash'}


class DecisionTests(unittest.TestCase):
    def test_complete_retained_coverage_and_no_archived_ids(self):
        ids=['P01','P04','P12','N01'];out=report.build(scores(ids),catalog(ids))
        self.assertEqual(out['retained_setting_ids'],['P01','P04','P12'])
        self.assertEqual({r['task_id']for r in out['rows']},{'P01','P04','P12'})
        self.assertEqual(next(r for r in out['rows']if r['task_id']=='P12')['evidence']['category'],'Scoring unresolved')
    def test_catalog_results_available_does_not_invent_score(self):
        data=catalog(['P04']);data['groups'][0]['status']='Results available'
        value=report.build(scores(['P04']),data)['rows'][0]
        self.assertIsNone(value['native_score']);self.assertEqual(value['evidence']['category'],'No verified result')
    def test_distinct_runs_preserved_and_inputs_immutable(self):
        original=scores(['B04'],[row('B04','first',metrics={'accuracy':.3}),row('B04','replay',metrics={'accuracy':.7})]);copy_before=copy.deepcopy(original)
        out=report.build(original,catalog(['B04']))
        self.assertEqual([r['native_score']['accuracy']for r in out['rows']],[.3,.7]);self.assertEqual(original,copy_before)
        self.assertNotIn('average',out);self.assertNotIn('mean',out)
    def test_p43_datasets_never_pooled(self):
        rows=[row('P43',d,dataset=d,metrics={'auroc':v,'auprc':.4})for d,v in [('bindingdb',.45),('biosnap',.55),('human',.6)]]
        out=report.build(scores(['P43'],rows),catalog(['P43']))
        self.assertEqual(len(out['rows']),3);self.assertEqual({r['dataset']for r in out['rows']},{'bindingdb','biosnap','human'})
    def test_v05_native_and_diagnostics_are_distinct(self):
        native=row('V05',metrics={'native_td_final_character_accuracy':.02,'adapted_full_text_closest_choice_accuracy':.4975,'adapted_full_text_released_label_accuracy':.4975,'strict_final_label_accuracy':.007})
        values=report.build(scores(['V05'],[native]),catalog(['V05']))['rows']
        self.assertEqual(len(values),3);self.assertEqual(sum(v['native_score']is not None for v in values),1)
        self.assertTrue(all(v['usable_answer_rate']['value']is None for v in values))
    def test_text_record_counts_are_not_usable_answers(self):
        source=row('P23',counts={'planned':10,'completed':10,'parsed':10},metrics={'rouge1':.2})
        value=report.build(scores(['P23'],[source]),catalog(['P23']))['rows'][0]
        self.assertIsNone(value['usable_answer_rate']['value']);self.assertIn('string records',value['usable_answer_rate']['display'])
    def test_nonabstention_never_used_as_parse_rate(self):
        source=row('B08',counts={'planned':33,'completed':33,'parsed':0,'invalid_outputs':33},metrics={'accuracy':0.,'coverage':1.})
        value=report.build(scores(['B08'],[source]),catalog(['B08']))['rows'][0]
        self.assertEqual(value['usable_answer_rate']['value'],0.);self.assertIn('0/33',value['usable_answer_rate']['display'])
    def test_likelihood_scores_are_not_named_generated_answers(self):
        value=report.usable(row('P43'),'P43')
        self.assertIn('valid scores',value['display']);self.assertIn('not generated answers',value['definition'])
    def test_p42_aggregate_counts_not_misnamed_per_condition(self):
        source=row('P42',metrics={'replace_only':{'qualified_oracle_success':0.,'native_novelty':None},'full_atomic':{'qualified_oracle_success':0.,'native_novelty':None}})
        values=report.build(scores(['P42'],[source]),catalog(['P42']))['rows']
        self.assertEqual(len(values),2)
        for value in values:
            self.assertIn('across both conditions',value['usable_answer_rate']['display']);self.assertIsNone(value['usable_answer_rate']['value'])
    def test_null_native_metric_stays_undefined(self):
        data=scores(['P07']);data['diagnostic_only_finished_runs']=[row('P07',metrics={'spearman':None,'spearman_parsed_only':.02})]
        value=report.build(data,catalog(['P07']))['rows'][0]
        self.assertIsNone(value['native_score']['spearman']);self.assertIn('spearman undefined',value['score_display'])
    def test_reaction_correction_preserves_original_and_has_distinct_hash(self):
        source=scores(['P16'],[row('P16')]);before=copy.deepcopy(source)
        out=report.build(source,catalog(['P16']),reaction_diagnostic=reaction_diagnostic(),source_hashes={report.REACTION_DIAGNOSTIC:'public-summary-hash'})
        self.assertEqual(len(out['rows']),2);self.assertEqual(source,before)
        native=next(r for r in out['rows']if r['condition_kind']=='native');fixed=next(r for r in out['rows']if r['condition_kind']!='native')
        self.assertEqual(native['native_score'],{'accuracy':.4});self.assertEqual(fixed['diagnostic_score'],{'accuracy':.5})
        self.assertEqual(fixed['counts']['planned'],10);self.assertEqual(fixed['counts']['parsed'],9)
        self.assertEqual(fixed['source_score_sha256'],'public-summary-hash');self.assertEqual(fixed['source_native_score_sha256'],'pinned-native-hash')
    def test_incomplete_or_foreign_reaction_diagnostic_refused(self):
        for field,value in [('clean_directory_reproduction_verified',False),('source_scores_sha256','foreign'),('full_original_denominator',9)]:
            diagnostic=reaction_diagnostic();diagnostic[field]=value
            with self.subTest(field=field),self.assertRaises(ValueError):
                report.build(scores(['P16'],[row('P16')]),catalog(['P16']),reaction_diagnostic=diagnostic)
    def test_reaction_diagnostic_does_not_enable_itself_for_absent_source(self):
        with self.assertRaises(ValueError):report.build(scores(['P16']),catalog(['P16']),reaction_diagnostic=reaction_diagnostic())
    def test_generate_reads_only_two_aggregate_inputs(self):
        with tempfile.TemporaryDirectory()as tmp:
            root=Path(tmp);(root/'reports').mkdir();(root/report.SCORES).write_text(json.dumps(scores(['P04'])));(root/report.CATALOG).write_text(json.dumps(catalog(['P04'])))
            original=Path.read_bytes;opened=[]
            def guarded(path):
                relative=str(path.relative_to(root));opened.append(relative)
                if relative not in {report.SCORES,report.CATALOG}:raise AssertionError('Unexpected read: '+relative)
                return original(path)
            with mock.patch.object(Path,'read_bytes',guarded):out=report.generate(root)
            self.assertEqual(set(opened),{report.SCORES,report.CATALOG});self.assertEqual(out['retained_setting_count'],1)
            self.assertTrue((root/report.OUTPUT_MD).exists())


if __name__=='__main__':unittest.main()
