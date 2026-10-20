#!/usr/bin/env python3
"""Prepare P12's new full cohort and independent validation delivery gate.

Only reviewed old model inputs, input provenance, public vocabulary, official
validation IDs and full FASTA are inspected. Scorer-reference bytes are hashed
and copied without parsing; no target outcomes select prompts or gate cases.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import sys

from run_deepfri_catalog_20261020 import ROOT, MODEL, REVISION, VARIANT, canonical, dense_prompt, generation_for, sha, stamp

BASE = ROOT/".local/catalog_execution_2026-10-20/tasks/P12"
RESTORED = ROOT/".local/evaluation_revision_2026-10-18/scoring/null_equivalence_recovery_v1/prepared_v2/p12/project"
METRIC_REL = "sources/deepfri_contract_audit_2026-10-15/torchdrug__torchdrug__metrics__metric.py"


def rel(path):
    return str(Path(path).relative_to(ROOT))


def write_new(path, value, lines=False):
    content = (b"".join(canonical(row).replace(b"\n", b"")+b"\n" for row in value)
               if lines else canonical(value))
    if path.exists():
        if path.read_bytes() != content:
            raise ValueError("Preserve changed preparation file: "+str(path))
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as handle:
        handle.write(content)


def fasta(path):
    values, name, parts = {}, None, []
    for line in path.read_text().splitlines():
        if line.startswith(">"):
            if name is not None:
                if name in values:
                    raise ValueError("Duplicate official FASTA ID")
                values[name] = "".join(parts)
            name, parts = line[1:].split()[0], []
        elif line.strip():
            parts.append(line.strip())
    if name is not None:
        if name in values:
            raise ValueError("Duplicate final FASTA ID")
        values[name] = "".join(parts)
    return values


def select_panel(ids, sequences, count=12):
    ordered = sorted(range(len(ids)), key=lambda i: (len(sequences[ids[i]]), i))
    selected = {ordered[round(j*(len(ordered)-1)/(count-1))] for j in range(count)}
    if len(selected) != count:
        raise ValueError("Length quantiles did not produce a complete panel")
    return [case_id for i,case_id in enumerate(ids) if i in selected]


def prepare():
    historical = json.loads((ROOT/"configs/local_deepfri_p12_sparse_confidence.json").read_text())
    old_inputs = RESTORED/historical["input_file"]
    old_vocabulary = RESTORED/historical["class_vocabulary_file"]
    old_references = RESTORED/historical["scorer_reference_file"]
    old_provenance = RESTORED/"data/catalog_deepfri_tasks/P12/input_provenance.jsonl"
    old_review = ROOT/historical["review_file"]
    sources = [old_inputs, old_vocabulary, old_references, old_provenance]
    for path in sources:
        original = str(path.relative_to(RESTORED))
        if sha(path) != historical["frozen_files_sha256"][original]:
            raise ValueError("Recovered source differs from historical freeze: "+original)
    if sha(old_review) != historical["frozen_files_sha256"][historical["review_file"]]:
        raise ValueError("Original exact input review differs")
    review = json.loads(old_review.read_text())
    vocabulary = json.loads(old_vocabulary.read_text())
    classes = vocabulary["classes"]
    old_cases = [json.loads(line) for line in old_inputs.read_text().splitlines()]
    provenance = [json.loads(line) for line in old_provenance.read_text().splitlines()]
    if [c["case_id"] for c in old_cases] != review["approved_case_ids"] or len(old_cases) != 1919 or review["held_cases"]:
        raise ValueError("Full approved P12 cohort differs")
    cases, sequence_audits = [], []
    for case, evidence in zip(old_cases, provenance):
        old_content = case["messages"][0]["content"]
        sequence = old_content.split("\n\nComplete amino acid sequence:\n", 1)[1].split("\n\nFixed global class vocabulary", 1)[0]
        digest = hashlib.sha256(sequence.encode()).hexdigest()
        if evidence["case_id"] != case["case_id"] or digest != evidence["full_sequence_sha256"] or len(sequence) != evidence["sequence_length"]:
            raise ValueError("Full sequence restoration differs")
        cases.append({"task_id":"P12", "case_id":case["case_id"], "messages":[{"role":"user","content":dense_prompt("P12",sequence,classes)}]})
        sequence_audits.append({"case_id":case["case_id"],"sequence_sha256":digest,"sequence_length":len(sequence),"complete_sequence_preserved":True})
    source = BASE/"source"
    validation_ids = (source/"nrPDB-EC_valid.txt").read_text().split()
    sequences = fasta(source/"nrPDB-EC_sequences.fasta")
    if len(set(validation_ids)) != len(validation_ids) or set(validation_ids)&set(review["approved_case_ids"]) or any(i not in sequences for i in validation_ids):
        raise ValueError("Official validation/test isolation differs")
    panel_ids = select_panel(validation_ids, sequences)
    panel = [{"task_id":"P12", "case_id":i,"messages":[{"role":"user","content":dense_prompt("P12",sequences[i],classes)}]} for i in panel_ids]
    for original, target in [(old_vocabulary,BASE/"class_vocabulary.json"), (old_references,BASE/"scorer_only/references.jsonl"), (RESTORED/METRIC_REL,source/"native_metric.py")]:
        target.parent.mkdir(parents=True,exist_ok=True)
        if target.exists() and sha(target)!=sha(original):
            raise ValueError("Changed copied source: "+str(target))
        if not target.exists():
            shutil.copyfile(original,target)
    write_new(BASE/"test.inputs.jsonl",cases,True)
    write_new(BASE/"development.inputs.jsonl",panel,True)
    write_new(BASE/"test.sequence_provenance.json",sequence_audits)
    basis = "Natural protein function annotation from complete sequences and fixed public EC vocabulary. Whole-task input-goal/schema review, no design, optimization or operational protocol request; not manual functional assessment of every residue. No reference outcomes inspected."
    for phase, rows in [("test",cases),("development",panel)]:
        write_new(BASE/(phase+".review.json"),{"task_id":"P12","input_review_only":True,"reviewed":True,"approved_case_ids":[r["case_id"] for r in rows],"held_cases":[],"source_input_sha256":sha(BASE/(phase+".inputs.jsonl")),"basis":basis,"biological_correctness_assessed":False,"selection_based_on_reference_or_model_outcomes":False})
    common = {"schema_version":1,"task_id":"P12","class_count":538,"variant":VARIANT,"model":MODEL,"model_revision":REVISION,
              "generation":generation_for(538),"vocabulary_file":rel(BASE/"class_vocabulary.json"),"vocabulary_sha256":sha(BASE/"class_vocabulary.json"),
              "expected_scoring_runtime":{"python":"3.12.15","torch":"2.13.0+cu130","device":"cpu","dtype":"float32","num_threads":1,"num_interop_threads":1},
              "reporting_protocol_kind":"adapted","reference_labels_in_solver_inputs":False,
              "case_scope":"Exact 1,919 released full FASTA test95 cases; independent official validation delivery panel",
              "paper_comparison":"New nonthinking constrained dense 3-decimal confidence adaptation. Full released FASTA and fixed source-order EC vocabulary retained. Does not reproduce trained DeepFRI/ProtST heads, native first-550 PDB-modeled inputs, or unpublished author-retained IDs. EC descriptions are frozen ExPASy 02-Sep-2026 display names; probability calibration and mechanistic explanation are not validated. Historical sparse reasoning runs remain separate.",
              "files_sha256":{p:sha(ROOT/p) for p in ["scripts/run_deepfri_catalog_20261020.py","scripts/score_deepfri_catalog_20261020.py","scripts/prepare_p12_dense_catalog_20261020.py"]}}
    for phase,rows,split in [("development",panel,"official_validation"),("test",cases,"official_test")]:
        config={**common,"run_id":f"qwen38_27b_p12_dense3dp_nonthinking16k_{phase}_2026-10-20_v1","split":split,"planned":len(rows),
                "input_file":rel(BASE/(phase+".inputs.jsonl")),"input_sha256":sha(BASE/(phase+".inputs.jsonl")),
                "review_file":rel(BASE/(phase+".review.json")),"review_sha256":sha(BASE/(phase+".review.json"))}
        if phase=="test":
            config.update(development_config_sha256=sha(BASE/"development.config.json"),scorer_reference_file=rel(BASE/"scorer_only/references.jsonl"),scorer_reference_sha256=sha(BASE/"scorer_only/references.jsonl"),metric_source_file=rel(source/"native_metric.py"),metric_source_sha256=sha(source/"native_metric.py"))
        write_new(BASE/(phase+".config.json"),config)
    receipt={"task_id":"P12","prepared_at_pacific":stamp(),"status":"offline_ready_requires_live_delivery_gate_and_root_grant","test_cases":len(cases),"classes":len(classes),"development_cases":len(panel),
             "development_selection":"12 evenly spaced sequence-length order quantiles including shortest/longest, source-order tie break; emitted in official source order; input-only selection",
             "development_case_ids":panel_ids,"validation_and_test_disjoint":True,"reference_labels_parsed":False,"new_inference_calls":0,
             "reference_labels_used_for_prompt_or_selection":False,"native_metrics":["auprc@micro","f1_max"],"new_head_training":False,
             "original_input_sha256":sha(old_inputs),"original_vocabulary_sha256":sha(old_vocabulary),"original_review_sha256":sha(old_review),
             "phase_configs":{p:{"path":rel(BASE/(p+".config.json")),"sha256":sha(BASE/(p+".config.json"))} for p in ["development","test"]},
             "material_changes":["Nonthinking final-only generation rather than historical reasoning condition","Exact fixed-order dense confidence array instead of free-form sparse class-key object","At most three decimal places and grammar-constrained serialization","16,384 token output limit for entire fresh condition"],
             "limitations":["Synthetic parser/token checks do not establish live structured-output support or biological correctness","Full test dispatch requires all 12 independent validation cases delivered and parsed without failure","Exact historical PDB/head conditions remain qualified as in original source audit"]}
    (BASE/"preparation.json").write_bytes(canonical(receipt))
    print(json.dumps(receipt))


if __name__=="__main__":
    prepare()
