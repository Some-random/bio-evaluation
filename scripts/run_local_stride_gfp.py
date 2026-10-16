#!/usr/bin/env python3
"""GFP-only fixed200-slot loopback generation; no oracle, keys, tools or retries."""
from __future__ import annotations
import argparse
import base64
import concurrent.futures as cf
from collections import Counter
import datetime as dt
import fcntl
import json
import os
from pathlib import Path
import re
import threading
import time
import urllib.error
import urllib.request

import run_local_labbench_eight_gpu as serving_helpers
import stride_gfp_qualified_contract as contract

ROOT = Path(__file__).resolve().parents[1]
MODEL = 'Qwen/Qwen3.8-27B'
MODEL_REVISION = '1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0'
PROPOSAL = 'configs/stride_gfp_qualified_p42.proposed.json'
VARIANT = 'QWEN_GFP_QUALIFIED_TWO_REGIMES_ENDPOINT_1_TO_3'
RUNNER = 'scripts/run_local_stride_gfp.py'
EXECUTOR = 'scripts/execute_local_stride_gfp.py'
SCORER = 'scripts/score_local_stride_gfp.py'
GENERATION = {'temperature':0.7,'top_p':0.9,'top_k':-1,'min_p':0.0,
              'max_tokens':1024,'n':1,'presence_penalty':0.0,'frequency_penalty':0.0,
              'repetition_penalty':1.0,'chat_template_kwargs':{'enable_thinking':True}}
digest = serving_helpers.digest
file_digest = serving_helpers.file_digest
write_json = serving_helpers.write_json


def local_file(name, directory=None):
    if not isinstance(name, str) or Path(name).is_absolute():
        raise ValueError('Require a relative project file')
    p = ROOT / name
    boundary = ROOT / directory if directory else ROOT
    if not p.resolve().is_relative_to(boundary.resolve()):
        raise ValueError('Project file escaped its declared directory')
    return p


def validate_settings(settings):
    if (settings.get('execution_authorized') is not True
            or settings.get('status') != 'frozen_for_authorized_execution'
            or settings.get('approved_task_ids') != ['P42']
            or settings.get('variant') != VARIANT
            or settings.get('model') != MODEL or settings.get('model_revision') != MODEL_REVISION
            or settings.get('gpu_ids') != [3]
            or settings.get('endpoint') != 'http://127.0.0.1:8033/v1'
            or settings.get('serving_config_file') != 'configs/local_model_gpu3.json'
            or settings.get('server_record_file') != '.local/local_model_server_gpu3.json'
            or settings.get('source_proposal_file') != PROPOSAL
            or settings.get('runner') != RUNNER or settings.get('executor') != EXECUTOR
            or settings.get('scorer') != SCORER
            or settings.get('generation') != GENERATION
            or settings.get('tool_access') != [] or 'tools' in settings
            or settings.get('planned_cases') != 200):
        raise ValueError('P42 execution differs from its fixed qualified recipe or is disabled')
    run_id = settings.get('run_id')
    if not isinstance(run_id, str) or not re.fullmatch(r'[A-Za-z0-9_.-]+', run_id):
        raise ValueError('Invalid run ID')
    if type(settings.get('concurrency')) is not int or not 1 <= settings['concurrency'] <= 4:
        raise ValueError('Invalid concurrency')
    if settings.get('source_sequence_sha256') != 'dd295bd4496d5e13da909a2c59492f00f923f7957a774feeaafaf8c5c235828c':
        raise ValueError('GFP source identity changed')


def case_regime(case):
    regime = case['case_id'].split(':')[1]
    if regime not in contract.REGIMES:
        raise ValueError('Unknown regime')
    return regime


def payload_for(case, settings):
    expected = {'task_id','case_id','protocol_variant','split','sample_index','seed','messages'}
    if not isinstance(case, dict) or set(case) != expected:
        raise ValueError('Unexpected input metadata; no reference fields may be dispatched')
    i = case['sample_index']
    if (type(i) is not int or not 0 <= i < 100 or type(case['seed']) is not int
            or case['seed'] != 42+i or case['task_id'] != 'P42'):
        raise ValueError('Candidate index or distinct fixed seed changed')
    regime = case_regime(case)
    if (case['case_id'] != f'p42:{regime}:{i:03d}'
            or case['protocol_variant'] != f'QWEN_GFP_QUALIFIED_{regime.upper()}_ENDPOINT_1_TO_3'
            or case['split'] != 'fixed_publisher_anchor_generated_candidates'):
        raise ValueError('Candidate identity/variant changed')
    messages = case['messages']
    if not isinstance(messages, list) or len(messages) != 2:
        raise ValueError('Both native roles must be retained')
    for message, role in zip(messages, ('system','user')):
        if (not isinstance(message, dict) or set(message) != {'role','content'}
                or message['role'] != role or not isinstance(message['content'],str)):
            raise ValueError('Only the original text system/user messages are permitted')
    if settings['generation'] != GENERATION or settings.get('tool_access') != []:
        raise ValueError('Sampling/tool recipe changed')
    return {'model':settings['model'],'messages':messages,**GENERATION,'seed':case['seed']}


def request_identity(case):
    return digest(['P42',case['protocol_variant'],case['case_id']])


def read_frozen_config(path):
    settings = json.loads(path.read_text())
    validate_settings(settings)
    frozen = settings.get('frozen_files_sha256',{})
    required = {RUNNER,EXECUTOR,SCORER,'scripts/run_local_labbench_eight_gpu.py',
                'scripts/stride_gfp_qualified_contract.py',PROPOSAL,
                settings['input_file'],settings['review_file']}
    proposal = json.loads(local_file(PROPOSAL,'configs').read_text())
    required.update(row['path'] for row in proposal['inputs'])
    required.update(row['path'] for row in proposal['frozen_dependencies'])
    for row in proposal['frozen_dependencies']:
        if frozen.get(row['path']) != row['sha256']:
            raise ValueError('Frozen source proposal dependency changed: '+row['path'])
    if not required <= set(frozen):
        raise ValueError('Protocol code, inputs or review are not frozen')
    for name, expected in frozen.items():
        if file_digest(local_file(name)) != expected:
            raise ValueError('Frozen dependency changed: '+name)
    if file_digest(local_file(PROPOSAL)) != settings['source_proposal_sha256']:
        raise ValueError('Disabled source proposal changed')
    expected_cases=[]
    for part in proposal['inputs']:
        p=local_file(part['path'],'data')
        if file_digest(p) != part['sha256']:
            raise ValueError('Original prospective input part changed')
        expected_cases.extend(json.loads(line) for line in p.read_text().splitlines() if line)
    cases=[json.loads(line) for line in local_file(settings['input_file'],'data').read_text().splitlines() if line]
    if len(cases)!=200 or cases != expected_cases:
        raise ValueError('Exact full200 case order/payload union changed')
    review=json.loads(local_file(settings['review_file'],'configs').read_text())
    if (review.get('reviewed') is not True or review.get('held_cases') != []
            or review.get('approved_task_ids') != ['P42']
            or review.get('approved_case_ids') != [r['case_id'] for r in cases]):
        raise ValueError('Full ordered GFP-only case review is unapproved')
    for case in cases:
        payload_for(case,settings)
    serving,record_path=serving_helpers.serving_context(settings)
    return settings,cases,serving,record_path


def http_json(endpoint,payload=None,timeout=900):
    """One HTTP attempt, direct loopback, preserving original response bytes."""
    opener=urllib.request.build_opener(urllib.request.ProxyHandler({}))
    data=json.dumps(payload,ensure_ascii=False).encode() if payload is not None else None
    request=urllib.request.Request(endpoint,data=data,headers={'Content-Type':'application/json'})
    raw=b''; code=0; error=None
    try:
        with opener.open(request,timeout=timeout) as response:
            code=response.status;raw=response.read()
    except urllib.error.HTTPError as exc:
        code=exc.code;raw=exc.read();error={'type':'HTTPError'}
    except (urllib.error.URLError,TimeoutError,OSError,ValueError) as exc:
        error={'type':type(exc).__name__}
    parsed=None
    if raw:
        try:parsed=json.loads(raw)
        except (ValueError,UnicodeDecodeError):error=error or {'type':'InvalidJSONResponse'}
    return {'http_status':code,'response':parsed,
            'raw_response_base64':base64.b64encode(raw).decode('ascii'),
            'raw_response_utf8':raw.decode('utf-8',errors='replace'),
            'raw_response_sha256':__import__('hashlib').sha256(raw).hexdigest(),
            'transport_or_schema_error':error}


def extract_choice(response):
    if (not isinstance(response,dict) or response.get('model') != MODEL
            or not isinstance(response.get('choices'),list) or len(response['choices'])!=1):
        raise ValueError('Unexpected served model or choice count')
    choice=response['choices'][0];message=choice.get('message')
    if not isinstance(message,dict) or message.get('content') is not None and not isinstance(message['content'],str):
        raise ValueError('Unexpected final channel type')
    available={k:message[k] for k in ('reasoning','reasoning_content') if message.get(k) is not None}
    if any(not isinstance(v,str) for v in available.values()) or len(set(available.values()))>1:
        raise ValueError('Ambiguous or malformed reasoning channels')
    reasoning=next(iter(available.values()),None)
    return {'final_text':message.get('content') or '', 'reasoning_text':reasoning,
            'reasoning_fields_present':list(available),'finish_reason':choice.get('finish_reason')}


def execute_one(case,settings,folder,source,stopped):
    identity=request_identity(case);request_path=folder/'requests'/(identity+'.json');response_path=folder/'responses'/(identity+'.json')
    if response_path.exists():
        previous=json.loads(response_path.read_text())
        if previous['status']!='completed':stopped.set()
        return previous['status']
    if request_path.exists():
        stopped.set();return 'interrupted_unknown_completion'
    if stopped.is_set():return 'not_dispatched_after_error'
    payload=payload_for(case,settings)
    body=json.dumps(payload,ensure_ascii=False)
    metadata={k:case[k] for k in ('task_id','case_id','protocol_variant','split','sample_index','seed')}
    request={**metadata,'task':'P42','variant':case['protocol_variant'],
             'regime':case_regime(case),'request_sha256':digest(payload),'payload':payload,
             'wire_request_body_utf8':body,'wire_request_body_sha256':__import__('hashlib').sha256(body.encode()).hexdigest(),
             'supplied_fields':['native_system_prompt','publisher_GFP_anchor','native_user_goal','declared_prospective_endpoint_regime'],
             'saved_at_utc':dt.datetime.now(dt.timezone.utc).isoformat()}
    write_json(request_path,request)
    before=time.monotonic()
    wire=http_json(settings['endpoint']+'/chat/completions',payload)
    record={**metadata,'task':'P42','variant':case['protocol_variant'],'regime':case_regime(case),
            'model':MODEL,'model_revision':MODEL_REVISION,'request_sha256':digest(payload),**wire,
            'elapsed_seconds':round(time.monotonic()-before,3),
            'saved_at_utc':dt.datetime.now(dt.timezone.utc).isoformat()}
    if wire['http_status']==200 and wire['transport_or_schema_error'] is None:
        try:
            channels=extract_choice(wire['response']);record.update(channels,status='completed')
            parsed=contract.parse_channels(channels['final_text'],channels['reasoning_text'])
            record['candidate_extraction']={**parsed,**contract.validate_endpoint(source,parsed['protein'],case_regime(case))}
        except (ValueError,TypeError,KeyError):
            record.update(status='response_schema_error');stopped.set()
    else:
        record['status']='transport_error' if wire['http_status']==0 else 'server_error';stopped.set()
    write_json(response_path,record)
    return record['status']


def seal_generation(folder,settings,cases,statuses_by_case):
    """Lock every original request/response and every missing slot before scoring."""
    slots=[]
    for case in cases:
        identity=request_identity(case);slot={'case_id':case['case_id'],'regime':case_regime(case),
            'sample_index':case['sample_index'],'seed':case['seed'],'identity':identity,
            'status':statuses_by_case[case['case_id']]}
        for kind in ('requests','responses'):
            p=folder/kind/(identity+'.json');prefix='request' if kind=='requests' else 'response'
            slot[prefix+'_file']=str(p.relative_to(folder)) if p.exists() else None
            slot[prefix+'_file_sha256']=file_digest(p) if p.exists() else None
        slots.append(slot)
    counts=Counter(statuses_by_case.values());complete=counts['completed']==len(cases)
    terminal={'run_id':settings['run_id'],'planned_cases':len(cases),'statuses':dict(counts),
              'generation_complete':complete,'generation_exit_code':0 if complete else 1,
              'oracle_forward_performed':False,'scoring_complete':False,
              'finished_at_utc':dt.datetime.now(dt.timezone.utc).isoformat()}
    write_json(folder/'generation_completion.json',terminal)
    lock={'schema_version':1,'run_id':settings['run_id'],'planned_cases':len(cases),
          'generation_complete':complete,'slots':slots,
          'run_manifest_sha256':file_digest(folder/'run_manifest.json'),
          'case_inputs_sha256':file_digest(folder/'case_inputs.json'),
          'generation_completion_sha256':file_digest(folder/'generation_completion.json'),
          'oracle_forward_performed':False,'scoring_complete':False,
          'created_at_utc':dt.datetime.now(dt.timezone.utc).isoformat()}
    write_json(folder/'generation_artifact_lock.json',lock)
    return terminal


def run(path):
    settings,cases,serving,record_path=read_frozen_config(path)
    source=json.loads(local_file('data/proxy_generation_native/P42/native_reference_contract.json').read_text())['sequence']
    folder=ROOT/'results/runs'/settings['run_id'];folder.mkdir(parents=True,exist_ok=True)
    with (folder/'worker.lock').open('a') as worker_lock:
        fcntl.flock(worker_lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
        if (folder/'generation_artifact_lock.json').exists():
            # A sealed cohort is terminal. Never add samples after viewing scores.
            previous=json.loads((folder/'generation_completion.json').read_text())
            return previous['generation_exit_code']
        server=json.loads(record_path.read_text())
        serving_helpers.validate_server_identity(server,settings,serving,serving_helpers.server_start_ticks(server['pid']))
        manifest={'configuration':settings,'configuration_sha256':file_digest(path),
                  'runner_sha256':file_digest(Path(__file__)),'planned_cases':200,
                  'case_contract_sha256':digest(cases),'model_selection_on_test':False,
                  'solver_tools':[],'answer_keys_available_to_solver':False,
                  'oracle_outputs_available_to_solver':False,'server':server,
                  'serving_configuration':{k:serving[k] for k in ('host','port','gpu_ids','model','revision','tensor_parallel_size','model_directory','checkpoint_precision','max_num_seqs')},
                  'native_paper_replication':False,'scoring_requires_complete_slot_lock':True}
        p=folder/'run_manifest.json'
        if p.exists() and json.loads(p.read_text()) != manifest:
            raise ValueError('Run identity changed; no results can be reused')
        write_json(p,manifest);write_json(folder/'case_inputs.json',cases)
        probe=http_json(settings['endpoint']+'/models',timeout=15)
        write_json(folder/'server_availability_probe.json',probe)
        if probe['http_status']!=200 or not any(r.get('id')==MODEL for r in (probe.get('response') or {}).get('data',[])):
            raise ValueError('Pinned local model is unavailable; no candidate requests dispatched')
        write_json(folder/'worker_process.json',{'pid':os.getpid(),'server':server,'started_at_utc':dt.datetime.now(dt.timezone.utc).isoformat()})
        stopped=threading.Event();statuses={};started=time.monotonic()
        def progress(stage):
            data={'run':settings['run_id'],'stage':stage,'planned':200,'finished':len(statuses),
                  'statuses':dict(Counter(statuses.values())),
                  'requests_saved':len(list((folder/'requests').glob('*.json'))),
                  'elapsed_seconds':round(time.monotonic()-started,2),
                  'updated_at_utc':dt.datetime.now(dt.timezone.utc).isoformat()}
            write_json(folder/'progress.json',data);print(json.dumps(data),flush=True)
        progress('running')
        with cf.ThreadPoolExecutor(max_workers=settings['concurrency']) as pool:
            futures={pool.submit(execute_one,case,settings,folder,source,stopped):case for case in cases}
            for future in cf.as_completed(futures):
                case=futures[future]
                try:statuses[case['case_id']]=future.result()
                except Exception as exc:
                    stopped.set();statuses[case['case_id']]='worker_exception'
                    write_json(folder/'execution_errors'/(request_identity(case)+'.json'),
                               {'case_id':case['case_id'],'error_type':type(exc).__name__})
                progress('running')
        terminal=seal_generation(folder,settings,cases,statuses)
        progress('generation_complete' if terminal['generation_complete'] else 'incomplete')
        return terminal['generation_exit_code']

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--config',type=Path,required=True)
    parser.add_argument('--validate-only',action='store_true');args=parser.parse_args()
    if args.validate_only:
        cfg,cases,_,_=read_frozen_config(args.config)
        print(json.dumps({'validated_cases':len(cases),'model_calls':False,'config_sha256':file_digest(args.config)}))
    else:raise SystemExit(run(args.config))
