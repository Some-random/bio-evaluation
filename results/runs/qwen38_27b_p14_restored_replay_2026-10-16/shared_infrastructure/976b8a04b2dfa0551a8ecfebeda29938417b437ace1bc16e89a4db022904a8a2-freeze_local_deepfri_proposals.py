#!/usr/bin/env python3
"""Freeze NEW disabled proposals after source/scorer/token audits, never launch."""
import argparse
import json
from pathlib import Path
import subprocess

from prepare_local_deepfri_proposals import write_new, digest

ROOT = Path(__file__).resolve().parents[1]


def freeze(root=ROOT):
    description = subprocess.run([str(root / ".venv-vllm/bin/python"), str(root / "scripts/score_local_deepfri_confidence.py"), "--describe-protocol"], check=True, capture_output=True, text=True)
    described = json.loads(description.stdout)
    runtime_name = "configs/local_deepfri_scoring_runtime_proposed.json"
    write_new(root / runtime_name, described["runtime"])
    budget_name = "reports/DEEPFRI_SPARSE_CONFIDENCE_TOKEN_BUDGET_2026-10-15.json"
    budget = json.loads((root / budget_name).read_text())
    if not budget.get("no_inference") or not budget.get("token_count_source", "").startswith("actual input_ids"):
        raise ValueError("Require verified actual-token audit")
    outputs = []
    for task in ["P12", "P13", "P14", "P15"]:
        old_name = f"configs/local_deepfri_{task.lower()}_proposed.json"
        new_name = f"configs/local_deepfri_{task.lower()}_sparse_confidence_proposed.json"
        config = json.loads((root / old_name).read_text())
        for name, expected in config["frozen_files_sha256"].items():
            if digest(root / name) != expected:
                raise ValueError("Prior prospective input contract changed: " + name)
        audited = next(row for row in budget["tasks"] if row["task_id"] == task)
        if not audited["all_cases_fit"] or audited["input_sha256"] != digest(root / config["input_file"]) or audited["proposed_config_sha256"] != digest(root / old_name) or audited["case_count"] != config["planned"]:
            raise ValueError("Token/input/proposal audit mismatch")
        preparation_name = f"data/catalog_deepfri_tasks/{task}/preparation.json"
        preparation = json.loads((root / preparation_name).read_text())
        if preparation["counts"]["released_test95_full_sequences"] != config["planned"]:
            raise ValueError("Released source coverage differs")
        reference_name = f"data/catalog_deepfri_tasks/{task}/scorer_references.jsonl"
        config.update({"proposal_status": "proposed_disabled_requires_root_authorization", "enabled": False,
                       "runner": "scripts/run_local_labbench_multimodal.py", "executor": "scripts/execute_local_deepfri_confidence.py",
                       "scorer": "scripts/score_local_deepfri_confidence.py", "scorer_python": ".venv-vllm/bin/python",
                       "scorer_reference_file": reference_name, "scorer_reference_sha256": digest(root / reference_name),
                       "scoring_runtime_file": runtime_name, "scoring_protocol_sha256": described["protocol_sha256"],
                       "scorer_sha256": described["scorer_sha256"], "token_budget_audit_file": budget_name,
                       "activation_blockers": ["Requires explicit root activation with enabled=true/proposal_status=frozen_for_authorized_execution and central task authorization; no generation was launched."],
                       "frozen_from_disabled_proposal": old_name,
                       "metric_policy": "Exact pinned TorchDrug auprc@micro and f1_max on model-supplied numeric sparse confidences; all planned vectors valid or full primary metrics null. TIE_GROUPED_AP_DIAGNOSTIC and OFFLINE_ALL_ZERO_REFERENCE remain distinct. No output repair, better-score selection or gold-derived ordering."})
        files = [config["runner"], config["executor"], config["scorer"], "scripts/score_local_deepfri_tie_grouped.py", "scripts/score_local_genomics.py", "scripts/freeze_local_deepfri_proposals.py", runtime_name, budget_name, reference_name, preparation_name,
                 "sources/deepfri_contract_audit_2026-10-15/native_metric_contract.json", "sources/deepfri_contract_audit_2026-10-15/ontology_contract.json", "sources/deepfri_contract_audit_2026-10-15/torchdrug__torchdrug__metrics__metric.py"]
        config["frozen_files_sha256"].update({name: digest(root / name) for name in files})
        write_new(root / new_name, config)
        outputs.append({"task_id": task, "config": new_name, "config_sha256": digest(root / new_name), "cases": config["planned"]})
    return {"proposals": outputs, "scorer_sha256": described["scorer_sha256"], "protocol_sha256": described["protocol_sha256"], "runtime": described["runtime"], "no_inference": True, "no_root_authorization_or_queue_edits": True}


if __name__ == "__main__":
    argparse.ArgumentParser(description=__doc__).parse_args()
    print(json.dumps(freeze()))
