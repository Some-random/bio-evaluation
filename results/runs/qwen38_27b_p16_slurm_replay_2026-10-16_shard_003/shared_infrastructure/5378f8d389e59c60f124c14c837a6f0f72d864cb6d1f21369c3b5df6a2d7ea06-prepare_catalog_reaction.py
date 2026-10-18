"""Prepare native Reaction test rows with all fixed full class descriptions.

No training examples, head fitting, model inference or execution authorization.
"""
import argparse
import csv
import hashlib
import io
import json
from pathlib import Path
import pickle
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
REVISION = "db53a76ed2430eb66dd9c8134ace99fd60980fb3"
ARCHIVE = "sources/catalog_reaction__Reaction.zip"
ARCHIVE_URL = "https://miladeepgraphlearningproteindata.s3.us-east-2.amazonaws.com/data/Reaction.zip"
ARCHIVE_MD5 = "d1c20341616ad3890349247017a34d68"
ARCHIVE_SHA256 = "ec4c8cc70cebca87165f6aeca10f319762bbe9ae0a75b7c8bdd6bb4f40967a80"
TEST_DATA_SHA256 = "99aad9e47cb939393ef706412636b436fa6ff29ee29648bfade511ea1d51de8b"
TEST_COUNT = 5651
CLASS_COUNT = 384
VARIANT = "QWEN_ZERO_SHOT_REACTION_FULL_SEQUENCE_ALL384_FULL_SOURCE_DESCRIPTIONS"
OBJECTIVE = ("Predict which of the 384 original Reaction enzyme classes this complete amino-acid sequence belongs to. "
             "The fixed original class IDs and full ProtST pre-training-template class descriptions are supplied below. "
             "Return only one integer class ID from 0 through 383.")
TABLE_HASHES = {
    "name": "13ddeaee45703ea3f129c7f9d1d851b035a855082d3eba6f0f90981988e04375",
    "language": "0617006ec8e1266915cd96cde9bcf3b02cf27db731c9d06b96fbd05d5bfac5fa",
    "template": "8933b21780c8e03a6c397cfad31049baca301467d8d38406cc11149f84b9db1a",
    "description": "d19d0bd57ea8b8dcf44b4ad6ec4133f18c25c5e943b6a3a5d3d4fb04ebea0201"}


def sha256(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical_digest(value):
    return sha256(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode())


def write_new(path, value):
    if path.exists():
        raise ValueError("Refuse to overwrite prepared artifact: " + str(path))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")
    path.chmod(0o600)


def validate_tables(tables, count=CLASS_COUNT):
    expected = [str(i) for i in range(count)]
    for name in ("description", "name", "language", "template"):
        rows = tables[name]
        if [row["id"] for row in rows] != expected or any(None in row for row in rows):
            raise ValueError("Global class IDs must retain source order and complete rows: " + name)
    if len({row["EC_number"] for row in tables["description"]}) != count:
        raise ValueError("Duplicate global EC class mapping")
    ontology = []
    for index, row in enumerate(tables["description"]):
        name = row["name"] + " " + row["alter_name"]
        language = "A " + row["name"] + " enzyme."
        if row["alter_name"]:
            language += " This enzyme is also known as " + row["alter_name"]
        if (tables["name"][index]["name"] != name or tables["language"][index]["name"] != language
                or tables["template"][index]["name"] != "FUNCTION: " + name
                or tables["template"][index]["description"] != "FUNCTION: " + name + " " + row["comment"]):
            raise ValueError("Official template/name/comment mapping mismatch")
        ontology.append({"id": index, "source_fields": row,
                         "native_name_only": tables["name"][index]["name"],
                         "native_natural_language": tables["language"][index]["name"],
                         "native_pretraining_name": tables["template"][index]["name"],
                         "native_full_pretraining_description": tables["template"][index]["description"]})
    return ontology


def load_ontology():
    tree = json.loads((ROOT / "sources/protst_tree.json").read_text())
    if tree["sha"] != REVISION:
        raise ValueError("Native source tree revision changed")
    blobs = {row["path"]: row for row in tree["tree"]}
    tables, provenance = {}, {}
    for name, expected in TABLE_HASHES.items():
        upstream = f"data/zero_shot_classification/reaction_{name}.tsv"
        path = ROOT / ("sources/catalog_reaction__" + upstream.replace("/", "__"))
        raw = path.read_bytes()
        git_blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        if sha256(raw) != expected or git_blob != blobs[upstream]["sha"]:
            raise ValueError("Pinned native class table changed: " + name)
        tables[name] = list(csv.DictReader(io.StringIO(raw.decode()), delimiter="\t"))
        provenance[str(path.relative_to(ROOT))] = {"sha256": expected, "git_blob_sha1": git_blob,
                    "source_url": f"https://github.com/DeepGraphLearning/ProtST/blob/{REVISION}/{upstream}"}
    return validate_tables(tables), provenance


def class_context(ontology):
    if [entry["id"] for entry in ontology] != list(range(CLASS_COUNT)):
        raise ValueError("Require all384 original global classes before opening test labels")
    return "\n".join(str(entry["id"]) + ": " + entry["native_full_pretraining_description"] for entry in ontology)


def transform(index, row, context):
    if set(row) != {"primary", "protein_length", "label"}:
        raise ValueError("Unexpected native LMDB row fields")
    sequence = row["primary"]
    if (not isinstance(sequence, str) or not sequence or any(not ("A" <= aa <= "Z") for aa in sequence)
            or len(sequence) != row["protein_length"]):
        raise ValueError("Complete source sequence/length must be preserved without cleaning")
    target = row["label"]
    if type(target) is not int or not 0 <= target < CLASS_COUNT:
        raise ValueError("Native target outside fixed global384-class mapping")
    prompt = OBJECTIVE + "\n\nOriginal fixed class descriptions:\n" + context + "\n\nComplete protein sequence:\n" + sequence
    common = {"task": "P16", "case_id": "Reaction:test:" + str(index), "variant": VARIANT,
              "split": "official_ProtST_Reaction_test", "source_index": index}
    model = {**common, "system": "", "prompt": prompt, "prompt_sha256": sha256(prompt.encode()),
             "fields": {"sequence": sequence, "objective": OBJECTIVE},
             "class_context_file": "data/catalog_reaction/P16/class_context.txt", "class_context_sha256": sha256(context.encode()),
             "model_facing_fields": ["complete_amino_acid_sequence", "fixed_task_objective", "all384_full_source_class_descriptions"]}
    reference = {**common, "target": target, "target_field": "label"}
    return model, reference


def test_rows():
    import lmdb
    raw = (ROOT / ARCHIVE).read_bytes()
    if sha256(raw) != ARCHIVE_SHA256 or hashlib.md5(raw).hexdigest() != ARCHIVE_MD5:
        raise ValueError("Native publisher Reaction archive changed")
    with zipfile.ZipFile(ROOT / ARCHIVE) as archive:
        payload = archive.read("Reaction/Reaction_test.lmdb/data.mdb")
    if sha256(payload) != TEST_DATA_SHA256:
        raise ValueError("Pinned test LMDB bytes changed")
    folder = ROOT / ".local/reaction_native_test"
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / "data.mdb"
    if path.exists() and sha256(path.read_bytes()) != TEST_DATA_SHA256:
        raise ValueError("Extracted test LMDB changed")
    if not path.exists():
        path.write_bytes(payload); path.chmod(0o600)
    env = lmdb.open(str(folder), readonly=True, lock=False, readahead=False, meminit=False)
    try:
        with env.begin() as transaction:
            if pickle.loads(transaction.get(b"num_examples")) != TEST_COUNT:
                raise ValueError("Native complete test count changed")
            for index in range(TEST_COUNT):
                yield index, pickle.loads(transaction.get(str(index).encode()))
    finally:
        env.close()


def parse_class_id(text):
    match = re.fullmatch(r"\s*(?:Answer\s*:\s*)?(0|[1-9][0-9]{0,2})\.?\s*", text or "", re.IGNORECASE)
    value = int(match.group(1)) if match else None
    return value if value is not None and value < CLASS_COUNT else None


def accuracy(targets, outputs):
    if not targets or len(targets) != len(outputs) or any(type(t) is not int or not 0 <= t < CLASS_COUNT for t in targets):
        raise ValueError("Require all planned native class targets/output slots")
    predictions = [parse_class_id(text) for text in outputs]
    correct = sum(p is not None and p == target for p, target in zip(predictions, targets))
    return {"accuracy": correct / len(targets), "correct": correct, "planned": len(targets),
            "parsed": sum(p is not None for p in predictions), "missing": sum(t is None for t in outputs),
            "invalid": sum(t is not None and p is None for t, p in zip(outputs, predictions)),
            "all_case_policy": "Every original test row remains in denominator; missing/invalid predictions count incorrect."}


def prepare():
    folder = ROOT / "data/catalog_reaction/P16"
    if folder.exists():
        raise ValueError("Reaction preparation already exists")
    # The complete class ontology is independent of test labels and loaded first.
    ontology, provenance = load_ontology()
    protocol = json.loads((ROOT / "sources/catalog_reaction_protocol_fetch.json").read_text())
    for artifact in protocol["records"]:
        if sha256((ROOT / artifact["path"]).read_bytes()) != artifact["sha256"]:
            raise ValueError("Pinned protocol source changed: " + artifact["path"])
    context = class_context(ontology)
    folder.mkdir(parents=True)
    write_new(folder / "class_ontology.json", ontology)
    (folder / "class_context.txt").write_text(context)
    (folder / "class_context.txt").chmod(0o600)
    lengths, case_ids = [], []
    inputs_path, refs_path = folder / "model_inputs.jsonl", folder / "scorer_references.jsonl"
    with inputs_path.open("w") as inputs, refs_path.open("w") as refs:
        for index, row in test_rows():
            model, reference = transform(index, row, context)
            inputs.write(json.dumps(model, ensure_ascii=False) + "\n")
            refs.write(json.dumps(reference, ensure_ascii=False) + "\n")
            lengths.append(len(row["primary"])); case_ids.append(model["case_id"])
    inputs_path.chmod(0o600); refs_path.chmod(0o600)
    if len(case_ids) != TEST_COUNT or len(set(case_ids)) != TEST_COUNT:
        raise ValueError("Complete native test ID contract failed")
    write_new(folder / "ordered_case_ids.json", case_ids)
    record = {"task": "P16", "variant": VARIANT, "cases": TEST_COUNT, "fixed_global_class_count": CLASS_COUNT,
              "source_revision": REVISION, "source_archive": ARCHIVE, "source_archive_url": ARCHIVE_URL,
              "source_archive_md5": ARCHIVE_MD5, "source_archive_sha256": ARCHIVE_SHA256,
              "test_lmdb_member": "Reaction/Reaction_test.lmdb/data.mdb", "test_lmdb_sha256": TEST_DATA_SHA256,
              "label_source_provenance": provenance, "class_context_sha256": sha256(context.encode()),
              "native_code_provenance": protocol,
              "global_class_mapping": "Original integer LMDB label unchanged; official fetch_labels constructs labels[id] from fixed TSV ids0..383. EC/name/comment crosswalk verified across all four native tables; candidates never inferred from observed test labels.",
              "independent_biochemical_remapping": "Not performed: native LMDB carries integer label and sequence, not separate EC annotation. The jointly released loader/evaluator/table contract defines the authoritative mapping.",
              "source_order": "All original LMDB numeric keys0..5650, no filtering/reordering", "complete_sequences_retained": True,
              "sequence_lengths": {"min": min(lengths), "max": max(lengths)}, "class_context_characters": len(context),
              "required_information_actually_prepared": ["complete original amino-acid sequence", "fixed classification objective", "all384 complete original pre-training-template class descriptions, including alternative names and comments"],
              "scorer_only_fields": ["native label"], "native_metric": "top1 multiclass accuracy over all5651 test rows",
              "native_predictor_definition": "One normalized protein embedding and one normalized text embedding per class; scaled dot-product, argmax. Each run uses one selected TSV/field; text encoded with max_length128 and truncation. No prompt ensemble in run_zero_shot.py.",
              "prompt_alternatives": {"name_only": "reaction_name.tsv:name", "natural_language": "reaction_language.tsv:name",
                  "pretraining_name": "reaction_template.tsv:name", "pretraining_full_description": "reaction_template.tsv:description"},
              "ensemble_definition": "Paper predictor ensemble mixes zero-shot classifier with a separately trained supervised predictor; it is distinct from prompt alternatives and is not used here.",
              "published_context": {"paper_url": "https://proceedings.mlr.press/v202/xu23t/xu23t.pdf", "locator": "Table11, printedp15; AppendixB.3",
                  "pretraining_name_accuracy_percent": 29.85, "pretraining_description_accuracy_percent": 21.91,
                  "values_rounded_as_published": True, "unmatched_training_representation_context": True},
              "comparison_caveat": "New zero-shot Qwen generative integer classifier, full raw sequence and all full descriptions jointly supplied; native ProtST encodes descriptions separately with128-token truncation and compares embeddings. This is not a matched architecture/context or few-shot/head-trained reproduction. README's bare-name command and paper's selected pretraining-name29.85 are distinct source variants.",
              "task_demands": {"labels": ["biological reaction-class prediction", "learned sequence representation", "mapping to fixed class descriptions"], "classification_is_provisional": True},
              "reference_evidence": "Existing source EC-derived reaction-category annotation, not a new experimental measurement",
              "good_score_establishes": "Agreement with native reaction classes on the declared released test under this explicit input/model protocol",
              "bad_score_establishes": "Limited source-class recovery; does not isolate general reasoning or biological factuality",
              "explanation_support_score": None, "mechanism_validation": "Not evaluated; correct class does not validate a rationale",
              "contamination": "Public pretraining exposure unknown; no labels sent, no train/dev examples or feedback tuning",
              "repository_license": "Pinned ProtST LICENSE is Apache2.0; archive has no separate data license file, so no independent dataset-license claim is made.",
              "train_or_validation_examples_read": 0, "fewshot_examples_supplied": 0, "new_head_training": False,
              "execution_authorized": False, "inference_dispatched": 0,
              "files": {path.name: {"sha256": sha256(path.read_bytes()), "bytes": path.stat().st_size} for path in folder.iterdir() if path.is_file()}}
    write_new(folder / "preparation.json", record)
    write_new(ROOT / "reports/catalog_reaction_preparation.json", record)
    print(json.dumps({"task": "P16", "cases": TEST_COUNT, "classes": CLASS_COUNT, "input_bytes": inputs_path.stat().st_size,
                      "prepared": str(folder.relative_to(ROOT)), "execution_authorized": False}))
    return record


if __name__ == "__main__":
    argparse.ArgumentParser(description=__doc__).parse_args()
    prepare()
