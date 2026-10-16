"""Gated local PMC-VQA execution; disabled proposals cannot dispatch."""
import argparse
import datetime as dt
import json
from pathlib import Path
import subprocess
import sys

import pmcvqa_clean_protocol as protocol


def validate_activation(path):
    cfg=json.loads(path.read_text());root=protocol.ROOT
    if cfg.get("execution_authorized") is not True or cfg.get("approved_task_ids")!=["V05"]:raise ValueError("V05 proposal is not authorized for execution")
    if cfg.get("generation")!=protocol.GENERATION or cfg.get("variant")!=protocol.VARIANT:raise ValueError("Fixed recipe/variant changed")
    if cfg.get("model")!=protocol.MODEL or cfg.get("model_revision")!=protocol.MODEL_REVISION:raise ValueError("Pinned model identity changed")
    authority=json.loads((root/"configs/local_model.json").read_text())
    if not authority.get("benchmark_inference_authorized") or "V05" not in authority.get("approved_task_ids",[]):raise ValueError("Central V05 execution allowlist is not approved")
    review=json.loads((root/cfg["review_file"]).read_text())
    if review.get("reviewed") is not True or review.get("held_cases") or len(review["approved_case_ids"])!=2000:raise ValueError("Whole native clean2000 review not approved")
    return cfg


def execute(path):
    cfg=validate_activation(path);root=protocol.ROOT
    generation=subprocess.run([sys.executable,"-u",str(root/cfg["runner"]),"--config",str(path)],cwd=root)
    folder=root/"results/runs"/cfg["run_id"]
    if not (folder/"run_manifest.json").exists():return generation.returncode or 1
    scoring=subprocess.run([sys.executable,"-u",str(root/"scripts/score_local_pmcvqa.py"),"--run",cfg["run_id"]],cwd=root)
    completion={"generation_exit_code":generation.returncode,"scoring_exit_code":scoring.returncode,"finished_at_utc":dt.datetime.now(dt.timezone.utc).isoformat()}
    if scoring.returncode==0:
        completion["scores_sha256"]=protocol.file_sha(folder/"scores.json");completion["run_manifest_sha256"]=protocol.file_sha(folder/"run_manifest.json")
        completion["scoring_output_lock_sha256"]=protocol.file_sha(folder/"scoring_output_lock.json")
    protocol.save_json(folder/"completion.json",completion);return generation.returncode or scoring.returncode


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument("--config",type=Path,required=True);args=parser.parse_args();raise SystemExit(execute(args.config))
