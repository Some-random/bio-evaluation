"""Prospective P36 source-code ROUGE adaptation; no model calls on import."""
import ast
import hashlib
import importlib.metadata
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
VARIANT = "QWEN_FULLTEXT_BIOT5_DESIGN_PAIRED_SOURCE_ROUGE_PARTIAL"
MODEL = "Qwen/Qwen3.8-27B"
REVISION = "1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0"
SOURCE_SHA = "d1239080c09194a71b71374cc4a976ae48184981c14caafce55ec82b2281d880"
HF_METRIC_SHA = "805b71b855be6dc270ce2366639a4e264c2a1fb93a2c8a50f9fb9ef5a2b9c21a"
WRAPPER_SHA = "6717c828e0a9bacdf761f1499672ab551938326fed723e1c805a23ebc9c6d2a9"
FORMAT = ("Return only the protein sequence in the dataset's serialized format: "
          "start with <bop>, write each amino-acid residue as <p> immediately followed "
          "by its uppercase one-letter code, and finish with <eop>. "
          "Do not include spaces, a FASTA header, markdown, or explanatory text.")
GENERATION = {"max_tokens": 4096, "temperature": 1.0, "top_p": 0.95,
              "top_k": 20, "seed": 42, "n": 1,
              "chat_template_kwargs": {"enable_thinking": True, "reasoning_effort": "medium"}}


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False,
                                    separators=(",", ":")).encode()).hexdigest()


def file_digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")
    temporary.chmod(0o600)
    temporary.replace(path)


def read_jsonl(path):
    return [json.loads(line) for line in Path(path).read_text().splitlines() if line]


def validate_cases(config):
    for relative, expected in config["frozen_files_sha256"].items():
        if file_digest(ROOT / relative) != expected:
            raise ValueError("Frozen file changed: " + relative)
    cases = read_jsonl(ROOT / config["input_file"])
    review = json.loads((ROOT / config["review_file"]).read_text())
    ids = [case["case_id"] for case in cases]
    if ids != review["approved_case_ids"] or len(ids) != len(set(ids)):
        raise ValueError("Cases differ from the exact input-only reviewed order")
    if set(ids) & {x["case_id"] for x in review["held_cases"]}:
        raise ValueError("Held case found")
    if digest(cases) != config["case_contract_sha256"]:
        raise ValueError("Input contract changed")
    for case in cases:
        if set(case) != {"task", "case_id", "variant", "split", "messages"}:
            raise ValueError("Unexpected model-facing fields")
        if case["task"] != "P36" or case["variant"] != VARIANT:
            raise ValueError("Wrong task or variant")
        if len(case["messages"]) != 2 or case["messages"][0] != {"role": "system", "content": FORMAT}:
            raise ValueError("Output-format adaptation changed")
        if set(case["messages"][1]) != {"role", "content"} or case["messages"][1]["role"] != "user":
            raise ValueError("Unexpected source prompt")
    if config["model"] != MODEL or config["model_revision"] != REVISION or config["generation"] != GENERATION:
        raise ValueError("Model or generation condition changed")
    return cases, review


def payload(case, config):
    return {"model": config["model"], "messages": case["messages"], **config["generation"]}


def serialization_diagnostic(text):
    valid = isinstance(text, str) and bool(re.fullmatch(r"<bop>(?:<p>[A-Z])+<eop>", text))
    return {"valid_native_protein_serialization": valid,
            "residues": text.count("<p>") if valid else None}


def official_method(path, class_name, namespace):
    tree = ast.parse(path.read_text())
    klass = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == class_name)
    method = next(n for n in klass.body if isinstance(n, ast.FunctionDef) and n.name == "_compute")
    module = ast.fix_missing_locations(ast.Module(body=[method], type_ignores=[]))
    exec(compile(module, str(path), "exec"), namespace)
    return namespace["_compute"]


def paired_rouge(predictions, references, output_tsv):
    """Execute both pinned source methods verbatim, replacing network resolution only."""
    from rouge_score import rouge_scorer, scoring
    import numpy as np
    if importlib.metadata.version("rouge-score") != "0.1.2":
        raise ValueError("Expected rouge-score 0.1.2")
    if not predictions or len(predictions) != len(references):
        raise ValueError("Require one prediction and reference pair per declared slot")
    if any(not isinstance(p, str) for p in predictions):
        raise ValueError("Predictions must be raw final-content strings")
    if any(not isinstance(r, list) or len(r) != 2 or any(not isinstance(v, str) for v in r) for r in references):
        raise ValueError("References must be [target, full source prompt] lists")
    hf_path = ROOT / "sources/hf_rouge_pinned.py"
    wrapper_path = ROOT / "sources/biot5_plus__metrics__pro_understand_metrics__pro_understand_metrics.py"
    if file_digest(hf_path) != HF_METRIC_SHA or file_digest(wrapper_path) != WRAPPER_SHA:
        raise ValueError("Source metric changed")
    hf = official_method(hf_path, "Rouge", {"rouge_scorer": rouge_scorer, "scoring": scoring})

    class FrozenRouge:
        def compute(self, predictions, references):
            return hf(None, predictions, references)

    class FrozenEvaluate:
        @staticmethod
        def load(name):
            if name != "rouge":
                raise ValueError("Unfrozen metric request")
            return FrozenRouge()

    native = official_method(wrapper_path, "Pro_understand", {"evaluate": FrozenEvaluate})
    state = np.random.get_state()
    try:
        np.random.seed(42)
        result = native(None, predictions, references, tsv_path=str(output_tsv))
    finally:
        np.random.set_state(state)
    return {key: float(value) for key, value in result.items()}
