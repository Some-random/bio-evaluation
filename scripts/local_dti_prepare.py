"""Build unapproved local DTI run drafts and optionally probe synthetic math."""
import argparse
from collections import Counter
import copy
import datetime as dt
import json
from pathlib import Path

from local_dti_common import (ROOT, MODEL, REVISION, LABELS, VARIANT, GENERATION,
                              call, digest, extract_score, file_digest, validate_server, write_json)

SOURCE_INPUT = "data/catalog_sequence_tasks/P43/model_inputs.jsonl"
SOURCE_REFS = "data/catalog_sequence_tasks/P43/scorer_references.jsonl"
DATASETS = ["human", "biosnap", "bindingdb"]
COUNTS = {"human": 1200, "biosnap": 5493, "bindingdb": 9840}


def input_cases(dataset):
    if dataset not in DATASETS:
        raise ValueError("Unknown source dataset")
    cases = []
    with (ROOT / SOURCE_INPUT).open() as handle:
        for source in map(json.loads, handle):
            if source["dataset"] != dataset:
                continue
            if source["task"] != "P43" or set(source["fields"]) != {"definition", "molecule_selfies", "Protein"}:
                raise ValueError("Unexpected original input allowlist")
            expected = source["fields"]["definition"] + "\nMolecule (SELFIES): " + source["fields"]["molecule_selfies"] + "\nProtein: " + source["fields"]["Protein"]
            if expected != source["prompt"]:
                raise ValueError("Original complete input rendering changed")
            cases.append({"task": "P43", "case_id": source["case_id"], "variant": VARIANT,
                          "split": "official_BioT5_export_" + dataset + "_test",
                          "messages": [{"role": "user", "content": source["prompt"]}]})
    if len(cases) != COUNTS[dataset] or len({c["case_id"] for c in cases}) != len(cases):
        raise ValueError("Original released dataset count/identity changed")
    return cases


def build_draft(dataset, server_state_file):
    server = json.loads((ROOT / server_state_file).read_text())
    cases = input_cases(dataset)
    folder = ROOT / "data/local_dti" / dataset
    folder.mkdir(parents=True, exist_ok=True)
    input_path = folder / "model_inputs.jsonl"
    with input_path.open("w") as handle:
        for case in cases:
            handle.write(json.dumps(case, ensure_ascii=False) + "\n")
    input_path.chmod(0o600)
    review_path = folder / "review.proposed.json"
    review = {"task_id": "P43", "dataset": dataset, "input_review_only": True, "reviewed": False,
              "approved_case_ids": [], "proposed_case_ids": [c["case_id"] for c in cases], "held_cases": [],
              "scope": "Proposed existing therapeutic drug-target interaction prediction inputs only; no design or optimization. Root must review and freeze before dispatch."}
    write_json(review_path, review)
    settings = {"run_id": "qwen38_27b_dti_" + dataset + "_likelihood_2026-10-15", "execution_authorized": False,
                "runner_file": "scripts/local_dti_run.py", "scorer_file": "scripts/local_dti_score.py", "executor_file": "scripts/local_dti_execute.py",
                "model": MODEL, "model_revision": REVISION, "dataset": dataset, "variant": VARIANT,
                "endpoint": f"http://127.0.0.1:{server.get('port', 8026)}/v1", "server_state_file": server_state_file,
                "approved_task_ids": ["P43"], "generation": copy.deepcopy(GENERATION), "concurrency": 4,
                "input_file": str(input_path.relative_to(ROOT)), "review_file": str(review_path.relative_to(ROOT)),
                "scorer_reference_file": SOURCE_REFS, "scorer_reference_sha256": file_digest(ROOT / SOURCE_REFS),
                "source_input_file": SOURCE_INPUT, "source_input_sha256": file_digest(ROOT / SOURCE_INPUT),
                "score_definition": "softmax over raw FIRST-token logp(Yes),logp(No); not sampled hard-label accuracy",
                "frozen_files_sha256": {}, "solver_tools": [], "no_training": True,
                "adapter_note": "Required numerical-output interface, fixed before DTI outputs; no reasoning-budget experiment. Native BioT5 raw-score ratio is not reproduced."}
    for name in [settings["input_file"], settings["review_file"], SOURCE_REFS, SOURCE_INPUT,
                 "scripts/local_dti_common.py", "scripts/local_dti_prepare.py", "scripts/local_dti_run.py", "scripts/local_dti_score.py", "scripts/local_dti_execute.py"]:
        path = ROOT / name
        if path.exists():
            settings["frozen_files_sha256"][name] = file_digest(path)
    config_path = ROOT / ("configs/local_dti_" + dataset + ".proposed.json")
    write_json(config_path, settings)
    return {"dataset": dataset, "cases": len(cases), "config": str(config_path.relative_to(ROOT)),
            "input_file": settings["input_file"], "input_sha256": file_digest(input_path),
            "execution_authorized": False, "reviewed": False}


def synthetic_probe(server_state_file):
    server = json.loads((ROOT / server_state_file).read_text())
    settings = {"model": MODEL, "model_revision": REVISION, "endpoint": f"http://127.0.0.1:{server.get('port',8026)}/v1"}
    validate_server(server, settings)
    # A distinct, nonbiological arithmetic case; never an actual DTI input.
    payload = {"model": MODEL, "messages": [{"role": "user", "content": "Reply Yes if two plus two equals five, otherwise No. Reply only Yes or No."}], **GENERATION}
    status, response = call(settings["endpoint"] + "/chat/completions", payload, timeout=60)
    if status != 200:
        raise ValueError("Synthetic API probe failed; no retry or biological dispatch")
    score = extract_score(response)
    return {"synthetic_nonbiological_only": True, "server": server, "payload": payload, "payload_sha256": digest(payload),
            "response": response, "response_sha256": digest(response), "score": score}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset", choices=DATASETS, action="append")
    parser.add_argument("--server-state", default=".local/local_model_server.json")
    parser.add_argument("--synthetic-probe", action="store_true")
    args = parser.parse_args()
    report_path = ROOT / "reports/local_dti_protocol.json"
    report = json.loads(report_path.read_text()) if report_path.exists() else {}
    report.update({"protocol_variant": VARIANT, "model": MODEL, "model_revision": REVISION, "generation": GENERATION,
        "label_token_ids": LABELS, "tokenization": "Yes and No are each one exact token without leading whitespace, verified with pinned local checkpoint tokenizer. Other spellings are excluded.",
        "score_definition": "exp(logpYes-max)/(exp(logpYes-max)+exp(logpNo-max)) from raw first-token conditional model log-likelihoods",
        "normalization": "vLLM0.31 defaults raw full-vocabulary logprobs. Pair renormalization is explicit; raw pair mass is retained and checked<=1. Fixed allowed labels only constrain sampled token.",
        "api_requirement": "logprob_token_ids explicitly requests both labels; top_logprobs2 alone could omit one because defaults return raw vocabulary logprobs. Token IDs also returned for provenance.",
        "classification_adapter": "One fixed no-thinking,one-token numerical score interface, not a reasoning-budget ablation. No actual P43 outputs used to choose settings.",
        "metrics": "Separate AUROC and sklearn average_precision_score(AUPRC/AP) for each original dataset; full metric absent if any approved case score missing/invalid; no filled score or test-threshold tuning.",
        "native_BioT5_caveat": "Pinned BioT5 source takes a ratio of raw first-token Yes/No generation scores rather than softmax probabilities and tunes a threshold using test ROC. This explicit Qwen likelihood adapter is not exact architecture/paper reproduction.",
        "reference_separation": "Runner reads frozen model inputs/review only; labels read only by offline scorer. No solver tools/retrieval/head fitting.",
        "actual_biological_dispatch_by_this_preparation": 0,
        "source_files": {name: file_digest(ROOT / name) for name in [SOURCE_INPUT, SOURCE_REFS, "sources/biot5__biot5_plus__utils__train_utils.py", "sources/biot5__biot5_plus__metrics__dti_metrics__dti_metrics.py"]},
        "updated_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()})
    if args.synthetic_probe:
        report["synthetic_negative_probe"] = synthetic_probe(args.server_state)
    if report.get("synthetic_negative_probe"):
        report["synthetic_negative_probe"]["score"] = extract_score(report["synthetic_negative_probe"]["response"])
    positive_path = ROOT / "reports/local_dti_synthetic_probe.json"
    if positive_path.exists():
        positive = json.loads(positive_path.read_text())
        report["synthetic_positive_probe"] = {"source_file": str(positive_path.relative_to(ROOT)),
            "response_sha256": digest(positive["response"]), "score": extract_score(positive["response"])}
    identity_path = ROOT / "reports/local_dti_source_identity.json"
    if identity_path.exists():
        report["original_split_identity"] = {"source_file": str(identity_path.relative_to(ROOT)), "sha256": file_digest(identity_path),
            "datasets": [{k:r[k] for k in ["dataset","cases","ordered_graph_sequence_and_label_equal","chemical_parse_failures"]}
                         for r in json.loads(identity_path.read_text())["datasets"]]}
    report["installed_vllm_sources"] = {str(path.relative_to(ROOT)): file_digest(path) for path in [
        ROOT / ".venv-vllm/lib/python3.12/site-packages/vllm/entrypoints/openai/chat_completion/protocol.py",
        ROOT / ".venv-vllm/lib/python3.12/site-packages/vllm/v1/sample/sampler.py",
        ROOT / ".venv-vllm/lib/python3.12/site-packages/vllm/config/model.py"]}
    report["actual_prompt_audit"] = "Archived returned prompt-token IDs must match usage length and the pinned closed-thinking assistant suffix; both raw candidate logprobs, sampled token ID/text/channel, one completion token and zero reasoning tokens verified."
    report["activation"] = "Root reviews case IDs/holds, freezes final config/review/hashes, enables local P43 scope plus execution_authorized. Then .venv/bin/python scripts/local_dti_execute.py --config FINAL_CONFIG. Proposed files intentionally cannot dispatch."
    report["proposed_runs"] = [build_draft(dataset, args.server_state) for dataset in args.dataset or DATASETS]
    write_json(report_path, report)
    print(json.dumps({"proposed_runs": report["proposed_runs"], "actual_biological_dispatch": 0}))


if __name__ == "__main__":
    main()
