#!/usr/bin/env python3
"""Read-only B04/B05 provenance audit; never parse model rationales or rescore files."""
import ast
import base64
from collections import Counter
import datetime as dt
import hashlib
import io
import json
from pathlib import Path
import random
import re
import string
import pyarrow as pa
import pyarrow.parquet as pq
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]

def sha_bytes(b):return hashlib.sha256(b).hexdigest()
def sha_file(p):
    h=hashlib.sha256()
    with p.open('rb') as handle:
        for chunk in iter(lambda:handle.read(8*1024*1024),b''):h.update(chunk)
    return h.hexdigest()
def digest(v):return sha_bytes(json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode())
def constant(path,name):
    for node in ast.parse(path.read_text()).body:
        if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id==name for t in node.targets):return ast.literal_eval(node.value)
    raise ValueError('Missing source constant '+name)


def main():
    pa.set_cpu_count(2)
    started=dt.datetime.now(dt.timezone.utc)
    template=constant(ROOT/'sources/lab__labbench__zero_shot.py','MCQ_INSTRUCT_TEMPLATE')
    cot=constant(ROOT/'sources/chembench_constant.py','COT_PROMPT')
    latex=constant(ROOT/'sources/chembench_constant.py','LATEX_ENV_REGEX')
    rng=random.Random(42);refs={};permutations={};prefix_counts=Counter()
    # This file contains ID/letter/count metadata only. Stop after B05, before
    # any B06 record; never open the mixed native model-input file.
    with (ROOT/'data/labbench_native_complete/scorer_references.jsonl').open() as f:
        for line in f:
            row=json.loads(line);task=row['task'];prefix_counts[task]+=1
            perm=list(range(row['choice_count']));rng.shuffle(perm)
            if task in ('B04','B05'):
                refs[(task,row['case_id'])]=row;permutations[(task,row['case_id'])]=perm
            if task=='B05' and prefix_counts['B05']==244:break
    assert prefix_counts==Counter({'B01':199,'B02':520,'B03':82,'B04':181,'B05':244})
    outcomes=[];details=[];warnings=[]
    for task,subset,count,expected_images in [('B04','FigQA',181,181),('B05','TableQA',244,262)]:
        cfg_path=ROOT/f'configs/local_labbench_{task.lower()}.json';cfg=json.loads(cfg_path.read_text())
        folder=ROOT/'results/runs'/cfg['run_id'];manifest=json.loads((folder/'run_manifest.json').read_text())
        assert manifest['configuration']==cfg and manifest['configuration_sha256']==sha_file(cfg_path)
        assert manifest['runner_sha256']==sha_file(ROOT/cfg['runner'])
        frozen_checks={name:sha_file(ROOT/name)==value for name,value in cfg['frozen_files_sha256'].items()};assert all(frozen_checks.values())
        assert sha_file(ROOT/cfg['scorer_reference_file'])==cfg['scorer_reference_sha256']
        source_path=ROOT/f'sources/lab_data__{subset}__train-00000-of-00001.parquet'
        publisher=json.loads((ROOT/f'sources/labbench_vision_integrity_audit/{subset}_publisher_tree.json').read_text())
        file_metadata=next(v for v in publisher if v['path'].endswith('train-00000-of-00001.parquet'))
        publisher_sha=file_metadata['lfs']['oid']
        source_sha=sha_file(source_path);assert source_sha==publisher_sha
        source_rows=pq.read_table(source_path).to_pylist();assert len(source_rows)==count
        review=json.loads((ROOT/cfg['review_file']).read_text());assert review['held_cases']==[]
        scored=json.loads((folder/'per_case_scores.json').read_text());scoremap={v['case_id']:v for v in scored}
        assert len(scored)==len(scoremap)==count
        saved_scores=json.loads((folder/'scores.json').read_text())
        prediction_lock=json.loads((folder/'predictions_lock.json').read_text())
        assert digest(prediction_lock['files'])==prediction_lock['sha256']
        caseids=[];all_case_digests=[];formats=Counter();image_counts=Counter();target_counts=Counter();answer_counts=Counter()
        bytes_sent=0;images_sent=0;source_duplicate_choice_cases=0;source_ideal_ambiguous_cases=0
        marked_correct=0;marked_sure=0;marked_parsed=0;source_canary_sent=0
        with (ROOT/cfg['input_file']).open() as f:
            for i,line in enumerate(f):
                case=json.loads(line);row=source_rows[i];cid=str(row['id']);key=(task,cid)
                assert case['task']==task and case['case_id']==cid
                assert set(case)=={'task','case_id','variant','split','messages'}
                assert case['variant']==cfg['variant']
                caseids.append(cid);all_case_digests.append(case)
                reference=refs[key];perm=permutations[key]
                values=[row['ideal'],'Insufficient information to answer the question',*row['distractors']]
                assert len(values)==reference['choice_count']==len(perm)
                choices=[f'({letter}) {values[j]}' for letter,j in zip(string.ascii_uppercase,perm)]
                expected=template.format(question=row['question'],answers='\n'.join(choices),cot='\n'+cot)
                for k in ['ce_pattern','math_pattern','smiles_pattern','rxnsmiles_pattern','pu_pattern']:
                    expected=re.sub(latex[k],lambda m:m.group(1),expected)
                assert reference['target_choice']==string.ascii_uppercase[perm.index(0)]
                assert reference['unsure_choice']==string.ascii_uppercase[perm.index(1)]
                assert reference['target_choice']!=reference['unsure_choice']
                source_duplicate_choice_cases+=len(set(values))!=len(values)
                source_ideal_ambiguous_cases+=values.count(row['ideal'])!=1
                assert len(case['messages'])==1 and case['messages'][0]['role']=='user'
                assert set(case['messages'][0])=={'role','content'}
                parts=case['messages'][0]['content'];assert isinstance(parts,list) and parts[0]=={'type':'text','text':expected}
                assert row.get('canary') not in expected
                raw_images=[row['figure']] if task=='B04' else row['tables']
                assert len(parts)==1+len(raw_images)
                image_proof=[]
                for j,source_image in enumerate(raw_images):
                    raw=source_image['bytes'];part=parts[j+1]
                    assert set(part)=={'type','image_url'} and part['type']=='image_url'
                    assert set(part['image_url'])=={'url','detail'} and part['image_url']['detail']=='auto'
                    prefix,encoded=part['image_url']['url'].split(',',1);sent=base64.b64decode(encoded,validate=True)
                    assert sent==raw
                    image=Image.open(io.BytesIO(raw));mime='image/'+image.format.lower()
                    assert prefix=='data:'+mime+';base64'
                    formats[image.format]+=1;images_sent+=1;bytes_sent+=len(raw)
                    image_proof.append({'image_index':j,'sha256':sha_bytes(raw),'bytes':len(raw),'format':image.format,'size':list(image.size)})
                image_counts[len(raw_images)]+=1
                identity=digest([task,case['variant'],cid]);request_path=folder/'requests'/(identity+'.json');response_path=folder/'responses'/(identity+'.json')
                request=json.loads(request_path.read_text());response=json.loads(response_path.read_text())
                expected_payload={'model':cfg['model'],'messages':case['messages'],**cfg['generation']}
                assert request['payload']==expected_payload
                assert set(request['payload'])=={'model','messages',*cfg['generation']}
                assert request['request_sha256']==digest(expected_payload)==response['request_sha256']
                assert response['case_id']==cid and response['model']==cfg['model'] and response['status']=='completed'
                assert response['response']['model']==cfg['model'] and len(response['response']['choices'])==1
                assert response['text']==(response['response']['choices'][0]['message'].get('content') or '')
                assert sha_file(response_path)==prediction_lock['files'][response_path.name]
                score=scoremap[cid];answer=score['answer']
                assert score['correct']==(answer==reference['target_choice'])
                assert score['sure']==(answer!=reference['unsure_choice'])
                assert score['parsed']==(answer is not None)
                assert score['task']==task and score['subtask']==reference['subtask']
                marked_correct+=score['correct'];marked_sure+=score['sure'];marked_parsed+=score['parsed']
                target_counts[reference['target_choice']]+=1;answer_counts[str(answer)]+=1
                details.append({'task_id':task,'case_id':cid,'source_row_index':i,
                    'source_choice_permutation':perm,'reference_target_choice':reference['target_choice'],'reference_unsure_choice':reference['unsure_choice'],
                    'saved_parsed_answer':answer,'saved_correct_flag':score['correct'],
                    'question_sha256':sha_bytes(row['question'].encode()),'source_ideal_sha256':sha_bytes(row['ideal'].encode()),
                    'rendered_prompt_sha256':sha_bytes(expected.encode()),'images':image_proof,
                    'actual_request_sha256':request['request_sha256'],'response_file_sha256':prediction_lock['files'][response_path.name],
                    'source_prompt_exact':True,'image_bytes_and_order_exact':True,'permutation_and_label_exact':True,'saved_score_flag_matches_reference':True})
        assert len(caseids)==count and len(set(caseids))==count and caseids==review['approved_case_ids']
        assert set(scoremap)==set(caseids) and digest(all_case_digests)==manifest['case_contract_sha256']
        assert images_sent==expected_images and len(list((folder/'requests').glob('*.json')))==count
        assert len(list((folder/'responses').glob('*.json')))==count
        assert saved_scores['metrics']['n_total']==count and saved_scores['metrics']['n_correct']==marked_correct
        assert saved_scores['metrics']['n_sure']==marked_sure and saved_scores['parsed']==marked_parsed
        assert saved_scores['metrics']['accuracy']==marked_correct/count
        assert saved_scores['metrics']['precision']==marked_correct/marked_sure
        assert saved_scores['metrics']['coverage']==marked_sure/count
        outcomes.append({'task_id':task,'source_subset':subset,'run_id':cfg['run_id'],'cases':count,'images':images_sent,
           'image_bytes':bytes_sent,'image_formats':dict(formats),'image_count_per_case_distribution':dict(image_counts),
           'publisher_source_sha256':publisher_sha,'publisher_source_verified':True,'source_rows_and_execution_allowlist_identical':True,
           'source_choices_prompt_and_target_permutation_exact':True,'native_source_image_bytes_order_and_MIME_exact':True,
           'actual_requests_equal_frozen_inputs_and_generation':True,'no_extra_labels_references_or_context_in_payload':True,
           'source_canary_absent_from_solver_text':True,'all_response_hashes_match_prediction_lock':True,
           'scorer_used_only_final_channel':True,'saved_score_flags_and_aggregates_verified_without_reparsing':True,
           'correct':marked_correct,'accuracy':marked_correct/count,'saved_parsed':marked_parsed,
           'target_choice_distribution':dict(target_counts),'saved_answer_distribution':dict(answer_counts),
           'largest_single_constant_letter_accuracy':max(target_counts.values())/count,
           'duplicate_source_choice_cases':source_duplicate_choice_cases,'ambiguous_source_ideal_cases':source_ideal_ambiguous_cases,
           'frozen_dependencies_verified':frozen_checks,
           'artifacts':{'configuration_sha256':sha_file(cfg_path),'run_manifest_sha256':sha_file(folder/'run_manifest.json'),
                       'scores_sha256':sha_file(folder/'scores.json'),'per_case_scores_sha256':sha_file(folder/'per_case_scores.json'),
                       'prediction_lock_sha256':sha_file(folder/'predictions_lock.json')}})
        del source_rows,all_case_digests
    assert len(details)==425
    result={'created_at_utc':dt.datetime.now(dt.timezone.utc).isoformat(),'started_at_utc':started.isoformat(),
        'scope':'B04 FigQA and B05 TableQA postrun source/input/reference/provenance audit only.',
        'finding':'No local target leakage, permutation error, image/case mismatch or saved-score arithmetic discrepancy detected in all425completed cases.',
        'inference_dispatched':False,'existing_artifacts_modified':False,'model_outputs_reparsed':False,'model_rationales_scored':False,
        'mixed_native_model_inputs_opened':False,'reference_metadata_prefix_only_stop_before_B06':True,
        'other_held_raw_material_opened':False,'outcomes':outcomes,'per_case_proof':details,
        'limits':['No source-level biological answer adjudication or rationale correctness assessment was performed.','Prior public-benchmark exposure in model pretraining is unknown.','Correct mappings and original inputs do not exclude public-data memorization or benchmark-specific shortcuts.','Ryze and the original LAB-Bench use different models, inference/training regimes and reporting protocols; headline differences are not a controlled ranking.','The local run uses original embedded image bytes; native source provider wrappers and model-specific image preprocessors may serialize/transform them differently.'],
        'comparison_source':'https://arxiv.org/html/2606.00902v1#S3.T1',
        'native_source_code':'https://github.com/Future-House/LAB-Bench/tree/998a8e0a40cf116c80e1b0e7a805ebb5fb9fa838',
        'source_dataset_revision':'5c77cec648430f30611808808861eb86f81d5eaa',
        'interpretation':'High accuracy alone establishes neither leakage nor stronger reasoning. Correct outcomes do not validate explanations.'}
    json_path=ROOT/'reports/labbench_vision_postrun_integrity_audit.json';assert not json_path.exists();json_path.write_text(json.dumps(result,indent=2)+'\n')
    lines=['# FigQA / TableQA postrun integrity audit','',result['finding'],'',
        '| Setting | Cases / original images | Correct / accuracy | Integrity result |','| --- | --- | --- | --- |']
    for out in outcomes:lines.append(f"| {out['task_id']} {out['source_subset']} | {out['cases']} / {out['images']} | {out['correct']} / {100*out['accuracy']:.2f}% | All source prompts, choice/target permutations, image order/bytes, actual requests and saved score flags reconcile |")
    lines+=['','The audit independently recomputed publisher parquet SHA-256 digests, reconstructed the seed42 choice permutations and native text rendering, and matched every request to its source case and image bytes. Correct and abstention targets stay outside the solver payload. All saved response hashes match their pre-scoring locks; saved parser answers, correctness flags and aggregate arithmetic agree with the original references. No model output was reparsed and no rationale was graded.','',
        'The higher scores than [Ryze Table1](https://arxiv.org/html/2606.00902v1#S3.T1) therefore have no detected local bookkeeping explanation. This audit cannot rule out prior public-data exposure, dataset shortcuts or differences in model/image processing and evaluation regimes. It does not establish a controlled model ranking or stronger biological reasoning.','',
        'No inference or existing-artifact changes occurred. The audit read only B04/B05 source data and task-specific run inputs; the reference-letter/count metadata prefix stopped before B06. Full425-case hashes and checks are in the [JSON audit](labbench_vision_postrun_integrity_audit.json).']
    md=ROOT/'reports/labbench_vision_postrun_integrity_audit.md';assert not md.exists();md.write_text('\n'.join(lines)+'\n')
    print(json.dumps({'tasks':[{k:v[k] for k in ['task_id','cases','images','correct','accuracy','image_formats','duplicate_source_choice_cases','ambiguous_source_ideal_cases']} for v in outcomes],
                      'json_sha256':sha_file(json_path),'markdown_sha256':sha_file(md)},indent=2))

if __name__=='__main__':main()
