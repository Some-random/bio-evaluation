"""Export a sealed V06 local-judge condition and image/reference-free trajectories."""
from __future__ import annotations
import copy
from datetime import datetime
from zoneinfo import ZoneInfo
import fcntl
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import tarfile

ROOT=Path(__file__).resolve().parents[1]
TASK=ROOT/'.local/catalog_execution_2026-10-20/tasks/V06'
CONTINUATION=TASK/'untouched_judge_continuation_v1'


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(path):return json.loads(Path(path).read_text())
def encoded(value):return (json.dumps(value,indent=2,ensure_ascii=False,allow_nan=False)+'\n').encode()


def public_request(payload,phase):
    """Declare transformed requests explicitly; original hashes remain separate."""
    value={key:copy.deepcopy(payload[key]) for key in ['model','temperature','top_p','max_tokens','chat_template_kwargs']}
    messages=[]
    for message in payload['messages']:
        content=copy.deepcopy(message['content'])
        if phase=='solver' and isinstance(content,list):
            content=[{'type':'image_reference','image_bytes_omitted':True,
                      'original_data_URL_sha256':hashlib.sha256(item['image_url']['url'].encode()).hexdigest()}
                     if item.get('type')=='image_url' else item for item in content]
        if phase=='judge' and message['role']=='user':
            quoted=json.loads(content)
            source=quoted['quoted_case']
            content=json.dumps({'quoted_case':{key:source[key] for key in ['question_id','question','candidate_answer']},
                'judge_declaration_sha256':quoted['judge_declaration_sha256'],
                'scorer_only_fields_omitted':['reference_answer','figure_context']},ensure_ascii=False)
        messages.append({'role':message['role'],'content':content})
    value['messages']=messages
    return {'representation':'public_transformed_input_not_original_replay_request',
        'original_image_bytes_and_scorer_reference_context_omitted':True,'payload':value}


def archive_trajectory(plan,done,scanner):
    run=Path(plan['output_root']);source=Path(plan['source_output_root'])
    target=ROOT/'results/trajectory_archives'/(plan['run_id']+'.tar.gz')
    receipt=target.with_suffix('.manifest.json')
    if receipt.exists():
        prior=read(receipt)
        if sha(target)!=prior['archive_sha256'] or prior['judge_lock_sha256']!=sha(run/'judge_lock.json'):
            raise ValueError('Existing V06 trajectory export differs')
        return {'path':str(target.relative_to(ROOT)),'sha256':prior['archive_sha256']}
    if target.exists():raise ValueError('Unsealed V06 archive exists; inspect, never overwrite')
    members={};provenance=[]
    def add(name,data,original=None):
        if name in members:raise ValueError('Duplicate trajectory member')
        scanner.safe_archive_member(name);scanner.scan_bytes(data);members[name]=data
        if original is not None:provenance.append({'public_member':name,'original_path':str(original),
            'original_sha256':sha(original),'public_sha256':hashlib.sha256(data).hexdigest(),
            'bytes_identical':data==Path(original).read_bytes()})
    for qid in range(193):
        solver=source/'solver'/f'{qid:03d}'
        judge=(source if qid<162 else run)/'judge'/f'{qid:03d}'
        for phase,folder in [('solver',solver),('judge',judge)]:
            add(f'{phase}/{qid:03d}/response.body',(folder/'response.body').read_bytes(),folder/'response.body')
            add(f'{phase}/{qid:03d}/outcome.json',(folder/'outcome.json').read_bytes(),folder/'outcome.json')
            add(f'{phase}/{qid:03d}/request.public.json',encoded(public_request(read(folder/'request.json'),phase)),folder/'request.json')
            if phase=='judge':add(f'{phase}/{qid:03d}/source_parsed_outcome.json',
                                  (folder/'parsed_outcome.json').read_bytes(),folder/'parsed_outcome.json')
    for name in ['run_manifest.json','completion.json','judge_lock.json','judgements.json','judge_outcomes.json',
                 'new_judge_outcomes.json','reused_judge_provenance.json','source_prediction_lock.json','scores.json']:
        add('closure/'+name,(run/name).read_bytes(),run/name)
    for name in ['completion.json','prediction_lock.json','judge_lock.json','scores.json']:
        add('preserved_strict_predecessor/'+name,(source/name).read_bytes(),source/name)
    code={
        'continuation_runner.py':CONTINUATION/'continuation_runner.py',
        'worker.py':CONTINUATION/'worker.py','worker.sbatch':CONTINUATION/'worker.sbatch',
        'freeze_plan.py':CONTINUATION/'freeze_plan.py','test_continuation.py':CONTINUATION/'test_continuation.py',
        'validate_contexts_cpu.py':CONTINUATION/'validate_contexts_cpu.py',
        'json_fence.py':TASK/'offline_json_fence_audit_v1/json_fence.py',
        'test_json_fence.py':TASK/'offline_json_fence_audit_v1/test_json_fence.py',
        'offline_judge.py':TASK/'offline_judge_preparation_v1/offline_judge.py',
        'render_envelopes.py':TASK/'real_input_preparation_v1/render_envelopes.py',
        'materialize_inputs.py':TASK/'real_input_preparation_v1/materialize_inputs.py',
        'preserved_v2_runner.py':TASK/'local_execution_v2/v06_runner.py',
        'preserved_v2_worker.py':TASK/'local_execution_v2/worker.py'}
    for name,path in code.items():add('source/'+name,path.read_bytes(),path)
    for name in ['plan.json','freeze_receipt.json','cpu_validation.json','cpu_context_validation.json',
                 'closure_proof.json','submission_receipt.json','root_admission.json']:
        path=CONTINUATION/name
        if path.exists():add('protocol/'+name,path.read_bytes(),path)
    add('public_original_hash_mapping.json',encoded(provenance))
    target.parent.mkdir(parents=True,exist_ok=True)
    temporary=target.with_suffix('.tmp')
    with tarfile.open(temporary,'w:gz') as archive:
        for name,data in sorted(members.items()):
            info=tarfile.TarInfo(name);info.size=len(data);info.mode=0o600;info.mtime=0
            archive.addfile(info,io.BytesIO(data))
    temporary.replace(target);scanner.scan_file(target)
    document={'schema_version':1,'run_id':plan['run_id'],'archive_sha256':sha(target),
        'archive_bytes':target.stat().st_size,'member_count':len(members),
        'files_sha256':{name:hashlib.sha256(data).hexdigest() for name,data in members.items()},
        'solver_response_count':193,'judge_response_count':193,
        'source_solver_responses_reused':193,'source_judge_responses_reused':162,'new_judge_responses':31,
        'source_prediction_lock_sha256':sha(source/'prediction_lock.json'),'judge_lock_sha256':sha(run/'judge_lock.json'),
        'all_raw_model_responses_bytes_identical':True,'original_requests_bytes_identical':False,
        'request_transformations':'Image bytes and judge-only reference/context omitted; original/public SHA mapping retained.',
        'scorer_reference_values_in_requests_included':False,'medical_image_bytes_included':False,
        'model_weights_included':False,'credentials_included':False,'runtime_environments_included':False}
    receipt.write_bytes(encoded(document))
    return {'path':str(target.relative_to(ROOT)),'sha256':document['archive_sha256']}


def export_v06(scanner,archive=True):
    plan_path=CONTINUATION/'plan.json'
    if not plan_path.exists():return []
    plan=read(plan_path);run=Path(plan['output_root']);source=Path(plan['source_output_root'])
    if not (run/'completion.json').exists():return []
    done=read(run/'completion.json')
    if done.get('benchmark_primary_defined') is not True:return []
    if sha(plan_path)!=(CONTINUATION/'plan.sha256').read_text().strip():raise ValueError('V06 frozen plan changed')
    for path,pin in plan['frozen_files_sha256'].items():
        if sha(path)!=pin:raise ValueError('V06 frozen source changed')
    lock=read(run/'judge_lock.json');scores=read(run/'scores.json')
    if (lock['outcomes_sha256']!=sha(run/'judge_outcomes.json') or lock['judgements_sha256']!=sha(run/'judgements.json')
            or lock['source_prediction_lock_sha256']!=sha(run/'source_prediction_lock.json')
            or sha(run/'source_prediction_lock.json')!=sha(source/'prediction_lock.json')):
        raise ValueError('V06 judge/source prediction lock mismatch')
    overall=scores['groups']['overall'];outcomes=read(run/'judge_outcomes.json')
    if (overall['planned']!=193 or overall['valid']!=193 or overall['complete'] is not True
            or scores['execution_condition']!=plan['condition'] or [r['question_id'] for r in outcomes]!=list(range(193))
            or any(r['status']!='completed' for r in outcomes) or len(read(run/'judgements.json'))!=193
            or done['new_judge']['attempted_with_observed_outcome']!=31
            or done['judge']['responses_saved']!=193 or done['new_solver_calls']!=0):
        raise ValueError('Only full193 verified V06 local-judge closure may be reported complete')
    for outcome in outcomes:
        folder=(source if outcome['question_id']<162 else run)/'judge'/f"{outcome['question_id']:03d}"
        if sha(folder/'response.body')!=outcome['raw_response_sha256'] or sha(folder/'request.json')!=outcome['request_sha256']:
            raise ValueError('V06 raw judge response or exact original request changed')
        if outcome['question_id']>=162 and read(folder/'parsed_outcome.json')!=outcome:
            raise ValueError('V06 new native validation event changed')
    public=ROOT/'results/runs'/plan['run_id']/'scores.json';public.parent.mkdir(parents=True,exist_ok=True)
    scanner.scan_file(run/'scores.json')
    if public.exists() and public.read_bytes()!=(run/'scores.json').read_bytes():raise ValueError('Existing V06 score export changed')
    public.write_bytes((run/'scores.json').read_bytes())
    row={'task_id':'V06','run_id':plan['run_id'],'protocol_variant':plan['condition'],
        'protocol_description':'193-case multimodal QA; declared Qwen local judge, uniform16K, lossless outer-JSON-fence parser repair',
        'new_complete_generation':True,'full_benchmark_complete':True,'full_primary_metric_defined':True,
        'counts':{'planned':193,'completed':193,'parsed':193,'invalid_outputs':0,'missing_or_failed_outputs':0},
        'finish_reasons':{'length':0,'stop':193},'generation':plan['model_configuration'],
        'metrics':{'relative_judged_answer_score_percent':overall['released_mean_case_ratio_score']},
        'source_scores':str(public.relative_to(ROOT)),'scores_sha256':sha(public),
        'prediction_lock_sha256':sha(source/'prediction_lock.json'),'judge_lock_sha256':sha(run/'judge_lock.json'),
        'config_sha256':sha(plan_path),'source_solver_responses_reused':193,'source_judge_responses_reused':162,
        'new_judge_responses':31,'new_solver_calls_by_continuation':0,
        'case_scope':'All193 released questions over50 images; current official article/filename image copies.',
        'interpretation':'Relative answer-quality score with Qwen3.8-27B as solver and local self-judge. Original numeric rubric and mean candidate/reference ratio retained; declared single-outer-JSON-fence extraction applies to all193 judge replies. The strict predecessor remains unchanged. Historical GPT-4-0314 judging and clinical accuracy are not reproduced.'}
    if archive:row['trajectory_archive']=archive_trajectory(plan,done,scanner)
    return [row]


def main():
    spec=importlib.util.spec_from_file_location('v06_export_secret_scanner',ROOT/'scripts/daily_backup.py')
    scanner=importlib.util.module_from_spec(spec);spec.loader.exec_module(scanner)
    with (ROOT/'.local/catalog_report_generation.lock').open('a') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX)
        rows=export_v06(scanner,True)
        if len(rows)!=1:raise ValueError('A defined V06 full193 score is required before ingestion')
        path=ROOT/'reports/CATALOG_NEW_SCORES_2026-10-20.json';document=read(path)
        if document['historical_artifacts_modified'] is not False:raise ValueError('Historical rows must stay unchanged')
        matching=[r for r in document['completed_rows'] if r['task_id']=='V06' and r['run_id']==rows[0]['run_id']]
        if matching:
            if matching!=rows:raise ValueError('An existing immutable V06 export changed')
        else:document['completed_rows'].extend(rows)
        document['generated_at_pacific']=datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()
        temporary=path.with_suffix('.json.v06.tmp');temporary.write_bytes(encoded(document));temporary.replace(path)
        print(json.dumps({'task_id':'V06','run_id':rows[0]['run_id'],'metrics':rows[0]['metrics'],
            'full193_primary_defined':True,'source_score_sha256':rows[0]['scores_sha256'],
            'new_model_calls_by_exporter':0}))


if __name__=='__main__':main()
