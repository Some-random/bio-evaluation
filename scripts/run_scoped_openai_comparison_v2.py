import argparse, hashlib, importlib.util, json, os
from pathlib import Path
from types import SimpleNamespace
from datetime import datetime
from zoneinfo import ZoneInfo

ROOT=Path('/dfs/scratch0/dongweij/bio-evaluation')
STATE=ROOT/'.local/comparison_execution_2026-10-19'
def digest(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p): return json.loads(Path(p).read_text())
def now(): return datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()
def save(p,v):
 t=Path(str(p)+'.tmp');t.write_text(json.dumps(v,indent=2)+'\n');t.replace(p)

def main():
 parser=argparse.ArgumentParser();parser.add_argument('slug');parser.add_argument('--gate');parser.add_argument('--workers',type=int,default=4);a=parser.parse_args()
 prepared=load(STATE/'prepared_execution_v2.json');entry=next(e for e in prepared['runs'] if e['slug']==a.slug)
 development=entry['stage'].endswith('_development')
 source=ROOT/'scripts/run_isolated_openai_comparison.py'
 assert digest(source)==prepared['dispatcher_sha256']
 publication=load(ROOT/'.local/catalog_resume_2026-10-19/publication/comparison_execution_v2_publication_receipt.json')
 assert publication['remote_bytes_verified'] and publication['stage']=='published'
 assert publication['paths_sha256']['scripts/run_isolated_openai_comparison.py']==digest(source)
 spec=importlib.util.spec_from_file_location('frozen_dispatcher',source);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
 manifest,_=m.load_bundle(entry['bundle'],entry['bundle_sha256'])
 auth=m.parse_json(m.read_pinned(entry['authorization'],entry['authorization_sha256']))
 gate=load(a.gate) if a.gate else None
 m.check_execution_gates(auth,gate,manifest,development=development)
 m.verify_review_receipts(auth,manifest,entry['review_receipt'],entry['review_receipt'])
 evidence=gate['development_evidence_path'] if gate else None
 if not development: m.verify_development_evidence(gate,manifest,evidence)
 # Credentials are opened only after the actual scoped documents and publication
 # have passed, and are supplied only to the launcher's private runtime pipe.
 keyfile=Path.home()/'.config/openai/api_key'
 os.environ['OPENAI_API_KEY']=keyfile.read_text().strip()
 output=STATE/'runtime'/a.slug
 args=SimpleNamespace(command='run-development' if development else 'run',bundle=entry['bundle'],bundle_sha256=entry['bundle_sha256'],output=str(output),run_id='openai_'+a.slug+'_4k_2026-10-19_v2',workers=a.workers,authorization=entry['authorization'],authorization_sha256=entry['authorization_sha256'],development_gate=a.gate,development_gate_sha256=digest(a.gate) if a.gate else None,development_evidence=evidence,reviewed_input_receipt=entry['review_receipt'],risk_review_receipt=entry['review_receipt'])
 runtime=STATE/'runtime'/(a.slug+'.runtime.json')
 state={'stage':'running_development_delivery' if development else 'running_frozen_benchmark','started_at_pacific':now(),'model':entry['model'],'task_ids':entry['task_ids'],'planned':entry['case_count'],'output':str(output),'run_id':args.run_id,'dispatcher_sha256':digest(source),'publication_commit':publication['commit_sha']}
 save(runtime,state); print(json.dumps(state),flush=True)
 try:
  result=m.launch(args)
 except Exception as e:
  state.update(stage='launcher_failed',finished_at_pacific=now(),error_type=type(e).__name__)
  save(runtime,state);raise
 finally: os.environ.pop('OPENAI_API_KEY',None)
 lock=load(output/'predictions_lock.json');usage={'input_tokens':0,'output_tokens':0,'cached_input_tokens':0}
 for row in lock['rows']:
  u=row.get('usage') or {};usage['input_tokens']+=u.get('input_tokens',0);usage['output_tokens']+=u.get('output_tokens',0);usage['cached_input_tokens']+=(u.get('input_tokens_details') or {}).get('cached_tokens',0)
 input_rate,output_rate=(.1,.5) if entry['model']=='gpt-6-luna' else (2.,10.)
 cost=(usage['input_tokens']*input_rate+usage['output_tokens']*output_rate)/1e6
 state.update(stage='terminal',finished_at_pacific=now(),result=result,usage=usage,standard_uncached_cost_estimate_usd=cost,biological_correctness_assessed=False)
 save(runtime,state); print(json.dumps(state),flush=True)

if __name__=='__main__':main()
