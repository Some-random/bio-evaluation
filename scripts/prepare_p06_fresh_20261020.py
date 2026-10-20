"""Freeze a new complete P06 scalar condition, without model calls or test tuning."""
from __future__ import annotations

import csv
from datetime import datetime
import hashlib
import io
import json
from pathlib import Path
import zipfile
from zoneinfo import ZoneInfo

from run_scalar_catalog_20261020 import GENERATION, MODEL, REVISION, sha

ROOT = Path(__file__).resolve().parents[1]
TASK = ROOT / ".local/catalog_execution_2026-10-20/tasks/P06"
VARIANT = "QWEN_ZERO_SHOT_FULL_SEQUENCE_FLIP_HUMAN_CELL_NONTHINKING_REGEX256_20261020_V1"
OLD_VARIANT = "QWEN_ZERO_SHOT_FULL_SEQUENCE_FLIP_HUMAN_CELL"
OBJECTIVE = ("Predict the experimentally measured protein melting temperature in degrees Celsius "
             "for the FLIP Meltome human_cell assay.\nReturn a single numerical value.\nProtein sequence:\n")
MD5 = "0f8b1e848568f7566713d53594c0ca90"


def stamp():
    return datetime.now(ZoneInfo("America/Los_Angeles")).isoformat()


def write_json(path, value):
    if path.exists():
        raise ValueError("Frozen P06 file already exists: " + str(path))
    path.write_text(json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False, allow_nan=False) + "\n")
    path.chmod(0o600)


def input_row(index, row):
    sequence = row["sequence"]
    if not sequence or any(not ("A" <= letter <= "Z") for letter in sequence):
        raise ValueError("Unexpected sequence content; no silent cleaning")
    return {"task_id": "P06", "case_id": f"human_cell:{index}",
            "messages": [{"role": "user", "content": OBJECTIVE + sequence}]}


def select_development(rows, count=16):
    # Split and lengths only; no target values, prior predictions or correctness.
    pool = [(len(row["sequence"]), index) for index, row in enumerate(rows)
            if row["set"] == "train" and row["validation"] == "True"]
    pool.sort()
    if len(pool) < count:
        raise ValueError("Insufficient official validation cases")
    selected = sorted({pool[round(j * (len(pool)-1)/(count-1))][1] for j in range(count)})
    if len(selected) != count:
        raise ValueError("Length-stratified validation selection is not unique")
    return selected


def main():
    source = TASK / "source/meltome_splits.zip"
    if hashlib.md5(source.read_bytes()).hexdigest() != MD5:
        raise ValueError("Pinned FLIP archive changed")
    with zipfile.ZipFile(source) as archive:
        rows = list(csv.DictReader(io.TextIOWrapper(archive.open("splits/human_cell.csv"))))
    if len(rows) != 7158 or any(set(row) != {"sequence", "target", "set", "validation"} for row in rows):
        raise ValueError("Unexpected FLIP native inventory")
    old_config_path = ROOT / "configs/local_catalog_p06.json"
    old_config = json.loads(old_config_path.read_text())
    old_review_path = ROOT / "configs/local_catalog_p06_review.json"
    old_review = json.loads(old_review_path.read_text())
    test_ids = [index for index, row in enumerate(rows) if row["set"] == "test"]
    if len(test_ids) != 1366 or any(rows[index]["validation"] != "False" for index in test_ids):
        raise ValueError("Native test cohort differs")
    if [f"human_cell:{index}" for index in test_ids] != old_review["approved_case_ids"]:
        raise ValueError("Fresh complete cohort differs from original review")
    original_rows, old_requests = [], []
    for index in test_ids:
        row = rows[index]
        prompt = OBJECTIVE + row["sequence"]
        original_rows.append({"task": "P06", "case_id": f"human_cell:{index}", "dataset": "FLIP_Meltome_human_cell",
                              "split": "official_test", "variant": OLD_VARIANT, "source_index": index,
                              "system": "", "prompt": prompt,
                              "fields": {"sequence": row["sequence"], "assay": "FLIP Meltome human_cell", "target_units": "degrees Celsius"},
                              "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest()})
        old_requests.append({"task": "P06", "case_id": f"human_cell:{index}", "variant": OLD_VARIANT,
                             "split": "official_test", "messages": [{"role": "user", "content": prompt}]})
    recovered = {
        "data/catalog_sequence_tasks/P06/model_inputs.jsonl": "".join(json.dumps(row) + "\n" for row in original_rows).encode(),
        "data/local_catalog_suite/P06/model_inputs.jsonl": "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in old_requests).encode(),
    }
    recovered_hashes = {name: hashlib.sha256(raw).hexdigest() for name, raw in recovered.items()}
    for name, digest in recovered_hashes.items():
        if digest != old_config["frozen_files_sha256"][name]:
            raise ValueError("Recovered input differs from historical identity: " + name)
    dev_ids = select_development(rows)
    TASK.mkdir(parents=True, exist_ok=True)
    provenance = []
    for name, indices, split in [("development", dev_ids, "official_validation"), ("full_test", test_ids, "official_test")]:
        cases = [input_row(index, rows[index]) for index in indices]
        path = TASK / (name + "_inputs.jsonl")
        if path.exists():
            raise ValueError("Frozen input already exists")
        path.write_text("".join(json.dumps(case, ensure_ascii=False) + "\n" for case in cases))
        path.chmod(0o600)
        for index in indices:
            sequence = rows[index]["sequence"]
            provenance.append({"phase": name, "case_id": f"human_cell:{index}", "source_row": index,
                               "sequence_length": len(sequence), "sequence_sha256": hashlib.sha256(sequence.encode()).hexdigest(),
                               "prompt_sha256": hashlib.sha256((OBJECTIVE+sequence).encode()).hexdigest()})
        review = {"task_id": "P06", "split": split, "approved_case_ids": [case["case_id"] for case in cases],
                  "reviewed_at_pacific": stamp(), "held_cases": [],
                  "basis": "Same previously reviewed human-cell thermal-property input domain; original complete test identities verified byte-exact. Development cases selected only by native validation membership and sequence-length quantiles.",
                  "full_sequences_preserved": True, "reference_labels_in_requests": False,
                  "selection_uses_test_outcomes": False, "flagged_requests_transferred": False,
                  "biological_scope": "Human-cell melting-temperature prediction; no mutation proposals, pathogen phenotype or operational protocol."}
        write_json(TASK / (name + "_review.json"), review)
    # Separate references are copied mechanically, not displayed or used for selection.
    refs = [{"task_id": "P06", "case_id": f"human_cell:{index}", "target_source_string": rows[index]["target"]} for index in test_ids]
    ref_path = TASK / "scorer_references.jsonl"
    if ref_path.exists():
        raise ValueError("Frozen references already exist")
    ref_path.write_text("".join(json.dumps(row) + "\n" for row in refs))
    ref_path.chmod(0o600)
    write_json(TASK / "input_provenance.json", {"source_archive_sha256": sha(source), "source_member": "splits/human_cell.csv",
               "historical_model_input_hashes_reproduced_exactly": recovered_hashes, "rows": provenance,
               "development_selection": "Sixteen equal sequence-length quantiles of official validation pool; ties by source index; frozen without targets/predictions.",
               "test_targets_used_for_protocol_selection": False, "test_targets_mechanically_copied_only_to_private_scorer_file": True})
    base = {"schema_version": 1, "task_id": "P06", "model": MODEL, "model_revision": REVISION,
            "protocol_variant": VARIANT, "generation": GENERATION, "native_metric": "Spearman correlation",
            "native_numeric_parser_file": str(TASK / "native_numeric_parser.py"),
            "native_numeric_parser_sha256": sha(TASK / "native_numeric_parser.py"),
            "native_numeric_parser_function": "parse_number",
            "files_sha256": {str(path): sha(path) for path in [Path(__file__).resolve(), source, old_review_path, old_config_path, TASK/"input_provenance.json"]},
            "new_condition_differences": ["Thinking disabled prospectively using pinned publisher chat template.",
               "Finite bounded ASCII scalar regex enforced by vLLM structured outputs.", "Per-case output cap 256 tokens instead of historical 4096 reasoning tokens.",
               "Historical complete sequence, assay objective, temperature unit, case order, checkpoint, sampling parameters and seed retained."],
            "native_score_policy": "No invented fill values; complete-case Spearman only if every planned case normally stops with native-parseable finite scalar. Otherwise explicit incomplete coverage and parsed-only diagnostic.",
            "native_training_regime_reproduced": False,
            "paper_comparison": "Prompted zero-shot sequence adaptation versus trained ProtST systems; no fitted regression head or matched training claim.",
            "no_selective_retries": True, "no_tools_or_repository_access": True, "source_revision": "d5c35cc716ca93c3c74a0b43eef5b60cbf88521f"}
    for name, count, split in [("development", len(dev_ids), "official_validation"), ("full_test", len(test_ids), "official_test")]:
        config = {**base, "run_id": f"qwen38_27b_p06_{name}_nonthinking_regex256_2026-10-20_v1",
                  "planned": count, "split": split, "frozen_at_pacific": stamp(),
                  "input_file": str(TASK/(name+"_inputs.jsonl")), "input_sha256": sha(TASK/(name+"_inputs.jsonl")),
                  "review_file": str(TASK/(name+"_review.json")), "review_sha256": sha(TASK/(name+"_review.json"))}
        if name == "full_test":
            config.update(development_config_sha256=sha(TASK/"development_config.json"),
                          scorer_reference_file=str(ref_path), scorer_reference_sha256=sha(ref_path))
        write_json(TASK/(name+"_config.json"), config)
    write_json(TASK / "status.json", {"task_id": "P06", "updated_at_pacific": stamp(), "stage": "prepared_waiting_central_endpoint_and_delivery_gate",
               "full_test_planned": 1366, "development_planned": len(dev_ids), "responses_saved": None,
               "new_inference_calls": 0, "runtime_started": False, "native_scoring_status": "not_started",
               "historical_inputs_recovered_exactly": True, "protected_test_outcomes_used_for_tuning": False,
               "next_action": "Root grant on shared pinned endpoint; complete sixteen-case validation delivery, then independent full fresh 1366-case condition only if gate passes."})
    print(json.dumps({"task_id": "P06", "test_cases": len(test_ids), "development_cases": len(dev_ids),
                      "historical_input_hashes_exact": True, "development_config_sha256": sha(TASK/"development_config.json"),
                      "full_test_config_sha256": sha(TASK/"full_test_config.json")}))


if __name__ == "__main__":
    main()
