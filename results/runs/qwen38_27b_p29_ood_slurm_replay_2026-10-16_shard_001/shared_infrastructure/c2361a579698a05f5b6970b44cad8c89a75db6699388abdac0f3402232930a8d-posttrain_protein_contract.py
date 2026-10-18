"""Pinned released Bio-posttrain protein RL prompt and GO metric; no inference."""
import ast
import functools
import importlib.util
import json
from pathlib import Path
import sys
from typing import List

from bioreason_pro_contract import digest, file_sha, save, generated_continuation

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "sources/posttrain_gap_audit_2026-10-15"
OUTPUT = ROOT / "data/catalog_posttrain_protein/P29"
CODE_REVISION = "03c872d3a1f38993f98786f774beb738df55a7be"
VARIANT = "QWEN_POSTTRAIN_RELEASED_RL_FULL_CONTEXT_K1_NATIVE_AUGMENTED_GO_REFERENCE"
INPUT_COLUMNS = ["protein_id", "sequence", "length", "organism", "interpro_formatted", "go_pred"]
SPLITS = {"id": ("id-test", 6989, "22ac86ba5007958cca20c67b578ecc30d5a0b1ff8acc90b5a7337888a93229b9"),
          "ood": ("ood-test", 7883, "33eea7afc2e7656907aa4820926e5e8c8cd32c799bfae24b121a18d9f8b5d2d4")}
CURATED_FIELDS = ("go_bp_leaf", "go_mf_leaf", "go_cc_leaf", "go_ids", "go_bp", "go_mf", "go_cc")
GO_SOURCE = SOURCE / "author__BioReason-Pro__bioreason2__utils__go_reward.py"
PROMPT_SOURCE = SOURCE / "author__BioReason-Pro__train_protein_grpo.py"
TEMPLATE_SOURCE = SOURCE / "author__BioReason-Pro__bioreason2__dataset__prompts__cafa5.py"
ONTOLOGY = SOURCE / "author__BioReason-Pro__bioreason2__dataset__go-basic.obo"


def verified_sources():
    tree = json.loads((ROOT / "sources/posttrain_tree.json").read_text())
    if tree["sha"] != CODE_REVISION:
        raise ValueError("Author source revision changed")
    blobs = {r["path"]: r["sha"] for r in tree["tree"]}
    result = {}
    import hashlib
    for name in ["author_source_manifest.json", "additional_author_source_manifest.json", "rl_author_source_manifest.json"]:
        manifest = json.loads((SOURCE / name).read_text())
        if manifest["commit"] != CODE_REVISION:
            raise ValueError("Source manifest revision changed")
        for row in manifest["files"]:
            if row.get("missing_from_tree"):
                continue
            path = ROOT / row["local_file"]
            raw = path.read_bytes()
            blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
            if blob != blobs[row["path"]] or file_sha(path) != row["sha256"]:
                raise ValueError("Pinned primary source changed: " + str(path))
            result[str(path.relative_to(ROOT))] = row["sha256"]
        result[str((SOURCE / name).relative_to(ROOT))] = file_sha(SOURCE / name)
    return result


@functools.lru_cache(maxsize=1)
def native_api():
    verified_sources()
    import obonet
    import networkx
    if obonet.__version__ != "1.1.1" or networkx.__version__ != "3.4.2":
        raise ValueError("Require frozen CPU ontology dependencies obonet1.1.1/networkx3.4.2")
    name = "p29_pinned_author_go_reward"
    spec = importlib.util.spec_from_file_location(name, GO_SOURCE)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


@functools.lru_cache(maxsize=1)
def native_prompt_api():
    api = native_api()
    namespace = {"__name__": "p29_native_prompt_extract", "List": List,
                 "dataclass": __import__("dataclasses").dataclass,
                 "GO_SUMMARY_START": api.GO_SUMMARY_START, "GO_SUMMARY_END": api.GO_SUMMARY_END}
    sys.modules[namespace["__name__"]] = __import__("types").ModuleType(namespace["__name__"])
    tree = ast.parse(TEMPLATE_SOURCE.read_text())
    if any(not isinstance(node, (ast.Assign, ast.Expr)) for node in tree.body):
        raise ValueError("Unexpected executable prompt constants")
    exec(compile(tree, str(TEMPLATE_SOURCE), "exec"), namespace)
    wanted = {"GrpoPromptConfig", "maybe_get", "_go_aspects_suffix", "build_prompt", "_GO_SUMMARY_TAG_INSTRUCTION"}
    selected = []
    for node in ast.parse(PROMPT_SOURCE.read_text()).body:
        name = node.name if isinstance(node, (ast.ClassDef, ast.FunctionDef)) else (
            node.targets[0].id if isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Name) else None)
        if name in wanted:
            selected.append(node)
    if len(selected) != len(wanted):
        raise ValueError("Native RL prompt definitions missing")
    exec(compile(ast.fix_missing_locations(ast.Module(body=selected, type_ignores=[])), str(PROMPT_SOURCE), "exec"), namespace)
    config = namespace["GrpoPromptConfig"](go_gpt_predictions_column="go_pred", interpro_in_prompt=True,
        ppi_in_prompt=False, ask_all_go_aspects=True, append_uniprot_suffix=False, go_summary_tags_in_prompt=True)
    return namespace["build_prompt"], config


def model_case(index, split, row):
    if split not in SPLITS or set(row) != set(INPUT_COLUMNS):
        raise ValueError("Require exact source input allowlist and ID/OOD split")
    sequence = row["sequence"]
    if (not sequence or any(not ("A" <= c <= "Z") for c in sequence)
            or len(sequence) != int(float(row["length"]))):
        raise ValueError("Complete original sequence/length required; no truncation or cleaning")
    if any(not isinstance(row[k], str) or not row[k] for k in INPUT_COLUMNS):
        raise ValueError("Native required source input missing")
    # A singular protein_name is optional in author code but absent from both
    # original CSVs. Never substitute their answer-bearing protein_names field.
    supplied = {k: row[k] for k in ("sequence", "organism", "interpro_formatted", "go_pred")}
    formatter, config = native_prompt_api()
    prompt = formatter(supplied, config)
    return {"task": "P29", "case_id": "P29:" + split + ":" + row["protein_id"], "variant": VARIANT,
            "split": "released_species_" + split + "_test", "messages": [{"role": "user", "content": prompt}]}


def reference(index, split, row):
    api = native_api()
    # This surprising source behavior is preserved and prominently qualified.
    # The curated-only union is a separate diagnostic, never selected by score.
    curated = set().union(*(api.normalize_go_field(row.get(k)) for k in CURATED_FIELDS))
    native = api.resolve_gold_terms_from_row(row)
    if not curated or not native:
        raise ValueError("Unexpected empty reference; do not filter source rows")
    return {"task": "P29", "case_id": "P29:" + split + ":" + row["protein_id"],
            "source_index": index, "protein_id": row["protein_id"], "native_split": split,
            "organism": row["organism"], "native_augmented_go_terms": sorted(native),
            "curated_only_go_terms_diagnostic": sorted(curated),
            "predictor_go_terms_added_to_native_target": sorted(native - curated)}


@functools.lru_cache(maxsize=1)
def native_ontology():
    return native_api().GeneOntology.from_obo(ONTOLOGY)


def score_prediction(terms, ref, ontology=None):
    api = native_api()
    ont = ontology if ontology is not None else native_ontology()
    predicted = ont.propagate(terms)
    native_gold = ont.propagate(ref["native_augmented_go_terms"])
    curated_gold = ont.propagate(ref["curated_only_go_terms_diagnostic"])
    native = api.weighted_precision_recall_f1(predicted, native_gold, ia_weights=None)
    diagnostic = api.weighted_precision_recall_f1(predicted, curated_gold, ia_weights=None)
    return {"native_augmented_precision": native[0], "native_augmented_recall": native[1], "native_augmented_F1": native[2],
            "curated_only_precision_diagnostic": diagnostic[0], "curated_only_recall_diagnostic": diagnostic[1],
            "curated_only_F1_diagnostic": diagnostic[2], "predicted_propagated_go_count": len(predicted)}


def mean_metrics(rows):
    if not rows:
        raise ValueError("No metric denominator")
    keys = ["native_augmented_precision", "native_augmented_recall", "native_augmented_F1",
            "curated_only_precision_diagnostic", "curated_only_recall_diagnostic", "curated_only_F1_diagnostic"]
    return {key: sum(row[key] for row in rows) / len(rows) for key in keys}
