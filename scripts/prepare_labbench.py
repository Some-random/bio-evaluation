"""Prepare complete native public inputs in a new directory, with scorer-only labels."""
import argparse
import ast
import base64
import hashlib
import io
import json
from pathlib import Path
import random
import re
import string

import pyarrow as pa
import pyarrow.parquet as pq

ROOT = Path(__file__).resolve().parents[1]
TASKS = {"LitQA2":"B01","DbQA":"B02","SuppQA":"B03","FigQA":"B04",
         "TableQA":"B05","ProtocolQA":"B06","SeqQA":"B07","CloningScenarios":"B08"}


def constant(path, name):
    for node in ast.parse(path.read_text()).body:
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == name for t in node.targets):
            return ast.literal_eval(node.value)
    raise ValueError("Native prompt constant missing")


def native_question(row, subset):
    """Preserve the task-specific transformations in the pinned official code."""
    if subset == "SuppQA":
        return f"Paper title: {row['paper-title']}\nDOI: {row['source']}\n{row['question']}"
    if subset == "ProtocolQA":
        return row["protocol"] + row["question"]
    return row["question"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=ROOT/"data/labbench_native_complete")
    parser.add_argument("--report", type=Path, default=ROOT/"reports/labbench_native_complete_preparation.json")
    args = parser.parse_args()
    if args.output_dir.resolve() == (ROOT/"data/labbench").resolve() or args.report.resolve() == (ROOT/"reports/labbench_preparation.json").resolve():
        raise ValueError("Preserve the previous preparation and frozen running evaluation")
    if args.output_dir.exists() and any(args.output_dir.iterdir()):
        raise ValueError("Do not overwrite an existing prepared release")
    pa.set_cpu_count(4)
    template = constant(ROOT/"sources/lab__labbench__zero_shot.py", "MCQ_INSTRUCT_TEMPLATE")
    constants = ROOT/"sources/chembench_constant.py"
    cot = constant(constants,"COT_PROMPT")
    latex = constant(constants,"LATEX_ENV_REGEX")
    rng = random.Random(42)
    inputs, references = [], []
    counts, unresolved = {}, []
    for subset, task in TASKS.items():
        path = ROOT/"sources"/("lab_data__" + subset + "__train-00000-of-00001.parquet")
        if not path.exists():
            unresolved.append(task)
            continue
        rows = pq.read_table(path).to_pylist()
        for row in rows:
            values = [row["ideal"],"Insufficient information to answer the question",*row["distractors"]]
            permutation = list(range(len(values)))
            rng.shuffle(permutation)
            choices = [f"({letter}) {values[j]}" for letter,j in zip(string.ascii_uppercase,permutation)]
            question = native_question(row, subset)
            text = template.format(question=question,answers="\n".join(choices),cot="\n"+cot)
            for key in ["ce_pattern","math_pattern","smiles_pattern","rxnsmiles_pattern","pu_pattern"]:
                text = re.sub(latex[key],lambda m:m.group(1),text)
            fields = {"question":row["question"],"choices":choices}
            if subset == "SuppQA":
                fields.update(paper_title=row["paper-title"], doi=row["source"])
            if subset == "ProtocolQA":
                fields["protocol"] = row["protocol"]
            content = [{"type":"input_text","text":text}]
            images = []
            if task in ["B04","B05"]:
                candidates = []
                for key,value in row.items():
                    if key in ["figure","figures","table","tables","image","images"]:
                        candidates.extend(value if isinstance(value,list) else [value])
                for value in candidates:
                    raw = value.get("bytes") if isinstance(value,dict) else None
                    if not raw:
                        raise ValueError("Required image bytes missing; do not run a text substitute")
                    from PIL import Image
                    image = Image.open(io.BytesIO(raw))
                    mime = "image/" + (image.format or "JPEG").lower()
                    content.append({"type":"input_image","image_url":"data:"+mime+";base64,"+base64.b64encode(raw).decode(),"detail":"auto"})
                    images.append(hashlib.sha256(raw).hexdigest())
                if not images:
                    raise ValueError("Required vision input missing")
                fields["images_sha256"] = images
            payload = {"model":"gpt-6-luna","input":[{"role":"user","content":content}],
                       "reasoning":{"effort":"medium"},"max_output_tokens":4096,"store":False,"tools":[]}
            case = {"task":task,"case_id":str(row["id"]),"variant":"NATIVE_PUBLIC_COT",
                    "split":"public_evaluation_release_train_named_partition","fields":fields,"payload":payload}
            inputs.append(case)
            references.append({"task":task,"case_id":case["case_id"],"subtask":row["subtask"],
                               "target_choice":string.ascii_uppercase[permutation.index(0)],
                               "unsure_choice":string.ascii_uppercase[permutation.index(1)],
                               "choice_count":len(choices)})
        counts[task] = len(rows)
    target = args.output_dir
    target.mkdir(parents=True, exist_ok=True)
    for name,records in [("model_inputs.jsonl",inputs),("scorer_references.jsonl",references)]:
        (target/name).write_text("".join(json.dumps(row,ensure_ascii=False)+"\n" for row in records))
        (target/name).chmod(0o600)
    manifest = {"counts":counts,"unavailable_image_partitions":unresolved,"shuffle_seed":42,
                "dataset_revision":"5c77cec648430f30611808808861eb86f81d5eaa",
                "official_code_revision":"998a8e0a40cf116c80e1b0e7a805ebb5fb9fa838",
                "public_subset_only":True,"reference_passages_sent":False,
                "native_required_source_links":{"B03":"paper title and DOI supplied, as required by the official task class"},
                "native_required_context":{"B06":"complete protocol plus question", "B04":"original figure image", "B05":"original table image"},
                "corrected_prior_omissions":["B03 paper title/DOI", "B06 full protocol"],
                "previous_inputs_and_running_manifest_modified":False,
                "rendering_code_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                "task_code_sha256":{subset:hashlib.sha256((ROOT/"sources"/("lab__"+subset+"__task.py")).read_bytes()).hexdigest()
                                    for subset in TASKS if (ROOT/"sources"/("lab__"+subset+"__task.py")).exists()},
                "model_inputs_sha256":hashlib.sha256((target/"model_inputs.jsonl").read_bytes()).hexdigest(),
                "scorer_references_sha256":hashlib.sha256((target/"scorer_references.jsonl").read_bytes()).hexdigest(),
                "paper_full_private_case_set_comparison":False,"tools":[],"prompt_sha256":hashlib.sha256(template.encode()).hexdigest()}
    args.report.write_text(json.dumps(manifest,indent=2)+"\n")
    print(json.dumps(manifest))


if __name__ == "__main__":
    main()
