"""Add only a defined full193 V06 result to the single public presentation table."""
from datetime import datetime
from zoneinfo import ZoneInfo
import hashlib
import json
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]
TASK=ROOT/'.local/catalog_execution_2026-10-20/tasks/V06'
CONTINUATION=TASK/'untouched_judge_continuation_v1'
PAPER='https://arxiv.org/pdf/2306.00890'


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(path):return json.loads(Path(path).read_text())


def main():
    stamp=datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()
    plan=read(CONTINUATION/'plan.json');run=Path(plan['output_root']);source_run=Path(plan['source_output_root'])
    completion=read(run/'completion.json');score=read(run/'scores.json')
    if completion['benchmark_primary_defined'] is not True or score['groups']['overall']['valid']!=193:
        raise ValueError('Only a complete193-judgement result can enter the presentation table')
    public_score=ROOT/'results/runs'/plan['run_id']/'scores.json'
    if sha(public_score)!=sha(run/'scores.json'):raise ValueError('V06 public score bytes differ')
    exported=next(row for row in read(ROOT/'reports/CATALOG_NEW_SCORES_2026-10-20.json')['completed_rows']
                  if row['task_id']=='V06' and row['run_id']==plan['run_id'])
    table=read(ROOT/'reports/EVALUATION_DECISION_TABLE.json')
    record=next(row for row in table['rows'] if row['task_id']=='V06' and row['run_id']==plan['run_id'])
    inputs=read(TASK/'real_input_preparation_v1/packets/solver_inputs.json')
    case=next(row for row in inputs if row['question_id']==0)
    request_path=source_run/'solver/000/request.json';request=read(request_path)
    text=next(part['text'] for part in request['messages'][0]['content'] if part['type']=='text')
    if text!=case['text']:raise ValueError('Complete example must match the actual saved solver request')
    image=next(row for row in read(TASK/'real_input_preparation_v1/packets/image_manifest.json') if 0 in row['question_ids'])
    page=ROOT/'reports/questions/V06.md'
    page.write_text('# LLaVA-Med: Biomedical visual chat — complete question and figure\n\n'
        'This is the complete text and figure used for released question 0 of the 193-question, 50-image evaluation.\n\n'
        '## User message\n\n```text\n'+text+'\n```\n\n'
        '## Figure\n\n![Figure supplied with this evaluated question]('+image['image_url']+')\n\n'
        '[Original article](https://pmc.ncbi.nlm.nih.gov/articles/'+image['pmcid']+'/). '
        'Released image: `'+case['image']+'`; source license: '+image['license_code']+'. '
        'The linked current official article/filename copy matches the evaluated image; the original release encoding is not independently verified.\n\n'
        '[Benchmark paper (2023)]('+PAPER+') · [Back to results](../RESULTS_AND_REMAINING_WORK.md)\n')
    value=score['groups']['overall']['released_mean_case_ratio_score']
    row='| LLaVA-Med: Biomedical visual chat | [2023](https://arxiv.org/abs/2306.00890) | “What is the organ in the image?”<br>[Complete question and supplied figure](questions/V06.md) | Relative judged answer score | '+f'{value:.2f}'+' | — | — | [LLaVA-Med 60K-IM: 50.2 (Table 1)]('+PAPER+')<br>GPT-4 judge; our Qwen local self-judge differs. | — |'
    report_path=ROOT/'reports/RESULTS_AND_REMAINING_WORK.md';report=report_path.read_text()
    name='| LLaVA-Med: Biomedical visual chat |'
    if name in report:report='\n'.join(row if line.startswith(name) else line for line in report.split('\n'))
    else:
        needle='| SlideVQA: Slide-deck question answering (Ryze) |'
        if needle not in report:raise ValueError('Expected existing vision table insertion point')
        report=report.replace(needle,row+'\n'+needle,1)
    qualification='**LLaVA-Med:** All 193 questions are scored with Qwen3.8-27B as both solver and declared local judge. The score is 100 × the mean candidate/reference rating ratio, not clinical accuracy. A lossless outer JSON-fence extraction is applied consistently to all judge replies; the earlier strict-parser run is preserved. The paper used GPT-4 judging, so its 50.2 result is not directly comparable.'
    if '**LLaVA-Med:**' in report:
        report=re.sub(r'\*\*LLaVA-Med:\*\*[^\n]*',lambda match:qualification,report)
    else:report=report.replace('**Enzyme Commission classification:**',qualification+'\n\n**Enzyme Commission classification:**',1)
    source_path=ROOT/'reports/RESULTS_AND_REMAINING_WORK.sources.json';source=read(source_path)
    record.update(condition_id='Q_V06_20261021',is_primary_table=True,
        classification='declared_local_self_judge_with_lossless_format_parser_repair',
        evidence_level='full193_score_and_raw_response_bytes_verified',old_undefined_full_metric=False,
        raw_response_reverified_by_this_audit=True,new_score_export=exported,
        score_source={'path':str(public_score.relative_to(ROOT)),'local_present':True,
            'local_sha256':sha(public_score),'recorded_sha256':sha(public_score),'local_hash_matches_recorded':True,
            'note':'Separate V06 publication receipt records remote byte verification.'})
    source['qwen']['records']=[r for r in source['qwen']['records'] if r.get('run_id')!=plan['run_id']]+[record]
    source['qwen']['defined_setting_ids']=sorted(set(source['qwen']['defined_setting_ids'])|{'V06'})
    source['qwen']['defined_setting_count']=len(source['qwen']['defined_setting_ids'])
    source['qwen']['primary_condition_count']=sum(r.get('is_primary_table') is True for r in source['qwen']['records'])
    report=re.sub(r'Results are available for \*\*\d+ of 57 evaluation settings\*\*',
                  'Results are available for **'+str(source['qwen']['defined_setting_count'])+' of 57 evaluation settings**',report)
    report_path.write_text(report)
    question={'task_id':'V06','id':'V06','page_id':'V06','page_path':str(page.relative_to(ROOT)),
        'dataset':'LLaVA-Med biomedical visual chat,193 questions/50 images','case_id':0,
        'status':'complete_saved_evaluated_question_and_official_image_link','complete_question_or_input':True,
        'page_sha256':sha(page),'page_bytes':page.stat().st_size,'source_path':str(request_path.relative_to(ROOT)),
        'source_sha256':sha(request_path),'prediction_lock_sha256':sha(source_run/'prediction_lock.json'),
        'image_url':image['image_url'],'evaluated_image_sha256':image['image_sha256'],
        'image_bytes_published':False,'reference_answers_included':False,'new_case_reviews':0}
    source['verified_questions']=[r for r in source['verified_questions'] if r.get('task_id')!='V06']+[question]
    group=source['question_pages']['qa_vision'];group['records']=[r for r in group['records'] if r.get('task_id')!='V06']+[question]
    best={'task_id':'V06','best_model':'LLaVA-Med 60K-IM','display':'LLaVA-Med 60K-IM:50.2',
        'metric':'GPT-4-judged relative answer score','values':{'overall':50.2},'source_url':PAPER,
        'source_locator':'Table1, printed page6','value_status':'verified_primary_source_printed',
        'selection':'Highest non-oracle overall model result in Table1; not a current leaderboard claim.',
        'comparability':'Same193-question public evaluation, different judge: original GPT-4 versus our declared Qwen local self-judge. Historical original image byte identity unverified.',
        'verified_at_pacific':stamp}
    refs=source['published_model_references'];refs['records']=[r for r in refs['records'] if r.get('task_id')!='V06']+[best]
    for r in source['qwen'].get('sources',[]):
        if r['path'] in ['reports/EVALUATION_DECISION_TABLE.json','reports/CATALOG_NEW_SCORES_2026-10-20.json']:
            r['sha256']=sha(ROOT/r['path'])
    source.update(generated_at_pacific=stamp,report_sha256=sha(report_path),v06_result_added_at_pacific=stamp,
        v06_defined_score_source={'path':str(public_score.relative_to(ROOT)),'sha256':sha(public_score),
            'judge_lock_sha256':sha(run/'judge_lock.json'),'new_model_calls_by_reporting':0})
    source_path.write_text(json.dumps(source,indent=2,ensure_ascii=False)+'\n')
    if report.count(name)!=1 or len([line for line in report.splitlines() if line.startswith('| Evaluation |')])!=1:
        raise ValueError('Presentation must retain exactly one table and one V06 row')
    print(json.dumps({'defined_settings':source['qwen']['defined_setting_count'],'V06_score':value,
                      'public_score_sha256':sha(public_score),'new_model_calls':0}))


if __name__=='__main__':main()
