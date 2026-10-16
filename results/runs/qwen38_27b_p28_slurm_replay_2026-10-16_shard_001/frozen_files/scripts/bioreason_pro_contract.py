"""Pinned P28 input and official CAFA metric adapters; no model inference."""
import ast
import functools
import hashlib
import json
from pathlib import Path
import re
import sys
import tarfile

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "sources/bioreason_pro_contract_audit_2026-10-15"
OUTPUT = ROOT / "data/catalog_bioreason_pro/P28"
CODE_REVISION = "a93ac2a96387103c100c4d6a6674d6fe1dfaf9e8"
DATA_REVISION = "a18315a77d27dd4fe5a28b9b757695cff4ba4e3f"
DATA_FILE = "sources/bioreason_pro__data__test-00000-of-00001.parquet"
DATA_SHA256 = "f8acd81f3b08400783a34f4189428e4f41fa0c648bc8e4fa58b10ee58bb66828"
CAFA_SDIST_SHA256 = "abaaa1b225acfba8a188ac29c2b450f2b4b798631d20eeda018a1cd1eda9332b"
VARIANT = "QWEN_FULL_SEQUENCE_BIOREASON_PRO_NATIVE_CONTEXT_LABEL_INDEPENDENT_K1"
INPUT_COLUMNS = ["protein_id", "sequence", "length", "organism", "interpro_formatted", "go_pred", "ppi_formatted"]
ASPECTS = {"BP": "biological_process", "MF": "molecular_function", "CC": "cellular_component"}
ONTOLOGY = SOURCE / "bioreason2__dataset__go-basic.obo"
IA = SOURCE / "data__IA.txt"
EXCLUSIONS = SOURCE / "data__common_proteins.txt"
VENDOR = SOURCE / "cafaeval_1.3.0_src"


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def file_sha(path):
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")
    tmp.chmod(0o600); tmp.replace(path)


def verified_sources():
    tree = json.loads((ROOT / "sources/bio_pro_tree.json").read_text())
    if tree["sha"] != CODE_REVISION:
        raise ValueError("Native BioReason-Pro tree revision changed")
    blobs = {row["path"]: row for row in tree["tree"]}
    result = {}
    for name in ("manifest.json", "additional_manifest.json"):
        manifest = json.loads((SOURCE / name).read_text())
        for record in manifest["records"]:
            path = ROOT / record["file"]
            raw = path.read_bytes()
            blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
            if (record["source_revision"] != CODE_REVISION or file_sha(path) != record["sha256"]
                    or blob != blobs[record["upstream_path"]]["sha"]):
                raise ValueError("Pinned primary source changed: " + record["file"])
            result[record["file"]] = record["sha256"]
    archive = SOURCE / "cafaeval-1.3.0.tar.gz"
    if file_sha(archive) != CAFA_SDIST_SHA256:
        raise ValueError("Official CAFA package source distribution changed")
    with tarfile.open(archive) as source:
        for item in source.getmembers():
            if item.isfile() and "/src/cafaeval/" in item.name and item.name.endswith(".py"):
                relative = item.name.split("/src/", 1)[1]
                path = VENDOR / relative
                expected = hashlib.sha256(source.extractfile(item).read()).hexdigest()
                if file_sha(path) != expected:
                    raise ValueError("Vendored official CAFA source changed")
                result[str(path.relative_to(ROOT))] = expected
    result[str(archive.relative_to(ROOT))] = CAFA_SDIST_SHA256
    return result


@functools.lru_cache(maxsize=1)
def native_formatter():
    verified_sources()
    namespace = {}
    prompt_path = SOURCE / "bioreason2__dataset__prompts__cafa5.py"
    # This pinned module consists only of source prompt constants.
    tree = ast.parse(prompt_path.read_text())
    if any(not isinstance(node, (ast.Assign, ast.Expr)) for node in tree.body):
        raise ValueError("Unexpected executable prompt module content")
    exec(compile(tree, str(prompt_path), "exec"), namespace)
    loader = SOURCE / "bioreason2__dataset__cafa5__load.py"
    nodes = [node for node in ast.parse(loader.read_text()).body if isinstance(node, ast.FunctionDef)
             and node.name in ("_add_uniprot_summary", "_format_reasoning_prompt")]
    if len(nodes) != 2:
        raise ValueError("Native prompt formatter definitions missing")
    namespace["ASPECT_TO_COLUMN"] = {key: "go_" + key.lower() for key in ASPECTS}
    namespace["ast"] = ast
    exec(compile(ast.fix_missing_locations(ast.Module(body=nodes, type_ignores=[])), str(loader), "exec"), namespace)
    return namespace["_format_reasoning_prompt"]


def model_case(index, row):
    if set(row) != set(INPUT_COLUMNS):
        raise ValueError("Only the verified source input allowlist may reach prompt construction")
    sequence = row["sequence"]
    if (not isinstance(sequence, str) or not sequence or len(sequence) != row["length"]
            or any(not ("A" <= aa <= "Z") for aa in sequence)):
        raise ValueError("Complete original sequence/length must be retained without cleaning")
    for key in ("organism", "interpro_formatted", "go_pred", "ppi_formatted"):
        if row[key] is not None and not isinstance(row[key], str):
            raise ValueError("Unexpected source input type: " + key)
    if not row["organism"] or not row["go_pred"]:
        raise ValueError("Expected complete native organism and GO-GPT context")
    # No target-aspect, protein_function, name or teacher field is passed, even
    # though fixed True flags already make the native prompt label-independent.
    source = {key: row[key] for key in ("organism", "interpro_formatted", "go_pred", "ppi_formatted")}
    formatted = native_formatter()(source, go_gpt_predictions_column="go_pred", interpro_in_prompt=True,
        ppi_in_prompt=True, include_ground_truth_in_final_answer=False, add_uniprot_summary=True,
        is_swissprot=False, ask_all_go_aspects=True, force_uniprot_summary=True)["prompt"]
    native_text = formatted["system"].strip() + "\n\n" + formatted["user"].strip()
    # Original format.py already combines system and user text into one user
    # turn. Raw sequence replaces the trained protein embedding interface only;
    # GO graph/projector omission is a declared system adaptation, not native.
    prompt = "Complete original protein sequence:\n" + sequence + "\n\n" + native_text
    return {"task": "P28", "case_id": "P28:" + row["protein_id"], "variant": VARIANT,
            "split": "released_temporal_test_native_exclusions", "messages": [{"role": "user", "content": prompt}]}


def generated_continuation(response):
    """Generated channels only: never concatenate input/prompt/predictor context."""
    api = response["response"]
    if response.get("http_status") != 200 or len(api.get("choices", [])) != 1:
        raise ValueError("Require one successful local assistant continuation")
    choice = api["choices"][0]
    message = choice["message"]
    content = message.get("content") or ""
    channels = [message.get(key) for key in ("reasoning", "reasoning_content") if message.get(key) is not None]
    if not isinstance(content, str) or any(not isinstance(text, str) for text in channels):
        raise ValueError("Unexpected generated content/reasoning type")
    if len(channels) == 2 and channels[0] != channels[1]:
        raise ValueError("Conflicting duplicated reasoning channels; no selection allowed")
    reasoning = channels[0] if channels else ""
    if response.get("text") != content or response.get("finish_reason") != choice.get("finish_reason"):
        raise ValueError("Saved final content differs from raw single-completion response")
    return ((reasoning + "\n\n" + content) if reasoning else content), content, reasoning


def extract_go(text):
    return set(re.findall(r"GO:\d{7}", text or ""))


def reference(index, row):
    targets = {}
    for aspect in ASPECTS:
        value = row["go_" + aspect.lower()]
        terms = ast.literal_eval(value) if isinstance(value, str) else value
        if terms is None:
            terms = []
        if not isinstance(terms, list) or any(not isinstance(term, str) or not re.fullmatch(r"GO:\d{7}", term) for term in terms):
            raise ValueError("Unexpected native GO reference serialization")
        targets[aspect] = terms
    return {"task": "P28", "case_id": "P28:" + row["protein_id"], "source_index": index,
            "protein_id": row["protein_id"], "target_aspects": targets}


def native_metrics(predictions, references, folder):
    """Call original CAFA functions globally; keep zero-prediction aspects/rows."""
    import numpy as np
    verified_sources()
    if str(VENDOR) not in sys.path:
        sys.path.insert(0, str(VENDOR))
    from cafaeval.evaluation import evaluate_prediction
    from cafaeval.parser import obo_parser, gt_parser, pred_parser
    from cafaeval.graph import Prediction
    if not Path(evaluate_prediction.__code__.co_filename).resolve().is_relative_to(VENDOR.resolve()):
        raise ValueError("Loaded CAFA evaluator is not the hash-verified official vendored source")
    if np.__version__ != "1.21.5" or sys.modules["pandas"].__version__ != "1.5.3":
        raise ValueError("Use the frozen CPU scoring environment: numpy1.21.5/pandas1.5.3")
    folder.mkdir(parents=True, exist_ok=True)
    gt_path, pred_path = folder / "ground_truth.tsv", folder / "predictions.tsv"
    if set(predictions) != {row["case_id"] for row in references}:
        raise ValueError("Require one prediction set/missing slot per planned eligible case")
    with gt_path.open("w") as gt, pred_path.open("w") as pred:
        for row in references:
            identity = row["case_id"]
            for terms in row["target_aspects"].values():
                for term in terms:
                    gt.write(identity + "\t" + term + "\n")
            for term in sorted(predictions[identity]):
                pred.write(identity + "\t" + term + "\t1.0\n")
    ontologies = obo_parser(str(ONTOLOGY), ("is_a", "part_of"), str(IA), True)
    gt = gt_parser(str(gt_path), ontologies)
    pred = pred_parser(str(pred_path), ontologies, gt, "max", None)
    # The released top-level evaluator omits namespaces with no predictions.
    # Its original underlying matrix metric computes zero for these. Supply a
    # zero matrix, not fabricated terms/probabilities; preserve the full gt rows.
    for namespace in gt:
        if namespace not in pred:
            pred[namespace] = Prediction({}, np.zeros_like(gt[namespace].matrix, dtype=float), namespace)
    table = evaluate_prediction(pred, gt, ontologies, np.array([0.99]), normalization="cafa", n_cpu=1)
    table.to_csv(folder / "native_cafa_threshold_metrics.csv", index=False)
    metrics, eligible = {}, {}
    for aspect, namespace in ASPECTS.items():
        rows = table[table["ns"] == namespace]
        if rows.empty:
            metrics[aspect + "_Fmax"], metrics[aspect + "_IA_weighted_Fmax"] = None, None
            eligible[aspect] = 0
        else:
            metrics[aspect + "_Fmax"] = float(rows["f"].max())
            metrics[aspect + "_IA_weighted_Fmax"] = float(rows["f_w"].max())
            eligible[aspect] = len(gt[namespace].ids)
    return metrics, {"native_ontology_eligible_counts_by_aspect": eligible,
        "package": "official cafaeval1.3.0 source distribution", "sdist_sha256": CAFA_SDIST_SHA256,
        "numpy_version": np.__version__, "pandas_version": sys.modules["pandas"].__version__,
        "ontology_sha256": file_sha(ONTOLOGY), "ontology_release": "2023-01-01", "ia_sha256": file_sha(IA),
        "relations": ["is_a", "part_of"], "propagation": "max for predictions and gold", "include_orphans_roots": True,
        "normalization": "cafa: precision over proteins with positive predicted weight/count, recall over ground-truth proteins",
        "weighted_terms": "Native package uses only finite positive IA terms; zero/missing/nonfinite IA becomes0",
        "hard_prediction_score": 1.0, "thresholds": [0.99],
        "zero_prediction_policy": "Original native matrix functions with zero matrices for absent-prediction namespaces; every ground-truth row retained. No fake terms, success-only filtering or output selection.",
        "historical_package_version": "BioReason-Pro declares unpinned cafaeval; exact historical version unresolved;1.3.0 frozen prospectively before inference."}
