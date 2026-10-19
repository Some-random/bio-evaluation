#!/usr/bin/env python3
"""Reproduce P12–P15 matched-subset metrics from the portable evidence bundle.

Requires the recorded Torch/NumPy CPU runtime. Does not use inference, network,
raw model requests, or hidden files. The evidence contains scorer-only labels.
"""
import argparse
import ast
import gzip
import hashlib
import json
import math
from pathlib import Path

def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def close(actual, expected):
    if expected is None:
        assert not math.isfinite(actual)
    else:
        assert math.isclose(actual, expected, rel_tol=1e-7, abs_tol=1e-10), (actual, expected)

def verify(folder):
    import numpy as np
    import torch
    torch.set_num_threads(1)
    torch.set_num_interop_threads(1)
    report = json.loads((folder / "analysis.json").read_text())
    assert torch.__version__ == report["runtime"]["torch"]
    assert np.__version__ == report["runtime"]["numpy"]
    source = folder / "native_metric.py"
    assert sha(source) == report["native_metric_source_sha256"]
    nodes = [node for node in ast.parse(source.read_text()).body if isinstance(node, ast.FunctionDef) and node.name in ("area_under_prc", "f1_max")]
    assert len(nodes) == 2
    for node in nodes:
        node.decorator_list = []
    namespace = {"torch": torch}
    exec(compile(ast.Module(body=nodes, type_ignores=[]), str(source), "exec"), namespace)
    for task in report["tasks"]:
        artifact = folder / (task["task_id"] + "_matched_subset.jsonl.gz")
        assert sha(artifact) == task["matched_subset_evidence_sha256"]
        with gzip.open(artifact, "rt") as f:
            rows = [json.loads(line) for line in f]
        ids = [row["case_id"] for row in rows]
        assert len(rows) == task["same_case_count"] == len(set(ids))
        assert digest(ids) == task["matched_subset_case_ids_sha256"]
        diagnoses = folder / (task["task_id"] + "_output_diagnoses.jsonl.gz")
        assert sha(diagnoses) == task["diagnoses_sha256"]
        with gzip.open(diagnoses, "rt") as f:
            parsed = [json.loads(line) for line in f]
        parsed = [row for row in parsed if row["native_valid"]]
        assert all(json.loads(row["final_text"])["scores"] == row["sparse_scores"] for row in parsed)
        assert [(r["case_id"], r["sparse_scores"]) for r in parsed] == [(r["case_id"], r["sparse_scores"]) for r in rows]
        lookup = {label: index for index, label in enumerate(task["class_ids"])}
        target = torch.zeros((len(rows), len(lookup)), dtype=torch.int64)
        scores = torch.zeros(target.shape, dtype=torch.float32)
        for i, row in enumerate(rows):
            assert row["task_id"] == task["task_id"]
            target[i, row["positive_class_indices"]] = 1
            for key, value in row["sparse_scores"].items():
                scores[i, lookup[key]] = value
        for values, key in ((scores, "model_parsed_subset"), (torch.zeros_like(scores), "matched_subset_all_zero_reference")):
            expected = task[key]
            close(float(namespace["area_under_prc"](values.flatten(), target.flatten())), expected["source_auprc_micro"])
            close(float(namespace["f1_max"](values, target)), expected["source_f1_max"])
            s, y = values.numpy().ravel(), target.numpy().ravel()
            order = np.argsort(s, kind="mergesort")[::-1]
            s, y = s[order], y[order]
            ends = np.r_[np.flatnonzero(np.diff(s)), len(s) - 1]
            tp = np.cumsum(y)[ends]
            ap = float(np.sum((tp / (ends + 1)) * np.diff(np.r_[0, tp])) / y.sum())
            close(ap, expected["tie_grouped_micro_ap"])
        print(task["task_id"], "verified", len(rows), "matched cases")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--evidence", type=Path, default=Path(__file__).resolve().parents[1] / "results/offline_diagnostics/deepfri_failure_analysis_2026-10-19")
    verify(parser.parse_args().evidence)
