"""Execute an exact-plan-approved P28 shard once; no reference reads or CAFA."""
import argparse
import datetime as dt
import json
from pathlib import Path
import subprocess
import sys

import local_bioreason_shards as common


def execute(path):
    cfg=json.loads(path.read_text())
    if cfg.get("aggregate_only") is not False or cfg.get("generator_execution_allowed") is not True or cfg.get("case_scope")!="task_shard_only" or cfg.get("runner")!=common.RUNNER:raise ValueError("Require prospective executable P28 shard")
    approval=common.approval_for(path,cfg);cases=common.cases_for(cfg)
    full=json.loads((common.ROOT/cfg["aggregate_config_file"]).read_text())
    matching=[r for r in full["shard_configs"] if r["shard_index"]==cfg["shard_index"]]
    if len(matching)!=1 or matching[0]["config_sha256"]!=common.file_sha(path):raise ValueError("Shard differs from frozen aggregate plan")
    folder=common.ROOT/"results/runs"/cfg["run_id"]
    if (folder/"completion.json").exists():raise ValueError("Shard already terminal; no retry/resampling")
    generation=subprocess.run([sys.executable,"-u",str(common.ROOT/common.RUNNER),"--config",str(path)],cwd=common.ROOT)
    audit_code=1;error=None
    try:
        summary,lock=common.audit_raw(folder,cases,cfg,common.file_sha(path));common.save(folder/"scores.json",summary);audit_code=0
    except Exception as exc:error=str(exc)
    folder.mkdir(parents=True,exist_ok=True)
    done={"generation_exit_code":generation.returncode,"scoring_exit_code":audit_code,"raw_audit_exit_code":audit_code,
        "native_metric_scoring":"deferred_global_only_no_shard_CAFA","finished_at_utc":dt.datetime.now(dt.timezone.utc).isoformat(),
        "configuration_sha256":common.file_sha(path),"case_scope":"task_shard_only","execution_approval":approval,"retry_or_resampling":False,**common.metadata(cfg)}
    for name in ["run_manifest.json","scores.json","scoring_output_lock.json"]:
        if (folder/name).exists():done[name.replace(".json","")+"_sha256"]=common.file_sha(folder/name)
    if error:done["error"]=error
    common.save(folder/"completion.json",done);return generation.returncode or audit_code


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument("--config",type=Path,required=True);raise SystemExit(execute(parser.parse_args().config))
