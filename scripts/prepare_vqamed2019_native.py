"""Prepare the original 500 ImageCLEF VQA-Med2019 test images/questions.

Uses previously acquired publisher files; does not perform inference.
"""
import base64
from collections import Counter
import hashlib
import json
from pathlib import Path
import zipfile

from run_local_labbench_multimodal import write_json, file_digest, validate_content

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "sources/vqamed2019"
OUTPUT = ROOT / "data/vqamed2019_native"
REVISION = "e673406ebc64cf499397e8abc0b63771b2db4bb9"
VARIANT = "NATIVE_IMAGECLEF2019_QUESTION_IMAGE_QUALIFIED_STRICT_ACCURACY"


def verify_source():
    tree = json.loads((ROOT / "sources/vqamed2019_tree.json").read_text())
    if tree["sha"] != REVISION:
        raise ValueError("Original publisher revision changed")
    provenance = {}
    for item in tree["tree"]:
        if item["type"] != "blob" or item["path"] == ".gitattributes":
            continue
        name = "test_images.zip" if item["path"].endswith(".zip") else item["path"].replace("/", "__")
        path = SOURCE / name
        raw = path.read_bytes()
        blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        if blob != item["sha"] or len(raw) != item["size"]:
            raise ValueError("Publisher Git blob mismatch: " + name)
        provenance[str(path.relative_to(ROOT))] = {"sha256": hashlib.sha256(raw).hexdigest(),
            "publisher_git_blob": blob, "bytes": len(raw),
            "url": f"https://raw.githubusercontent.com/abachaa/VQA-Med-2019/{REVISION}/{item['path']}"}
    return provenance


def prepare():
    if (OUTPUT / "model_inputs.jsonl").exists():
        raise ValueError("Native preparation already exists; do not replace frozen inputs")
    provenance = verify_source()
    questions = [line.split("|", 1) for line in (SOURCE / "VQAMed2019Test__VQAMed2019_Test_Questions.txt").read_text().splitlines() if line]
    references = [line.split("|", 3) for line in (SOURCE / "VQAMed2019Test__VQAMed2019_Test_Questions_w_Ref_Answers.txt").read_text().splitlines() if line]
    if len(questions) != 500 or len(references) != 500:
        raise ValueError("Original complete500-test count changed")
    if len({q[0] for q in questions}) != 500:
        raise ValueError("Duplicate native test image identity")
    OUTPUT.mkdir(parents=True)
    cases, labels, images = [], [], []
    with zipfile.ZipFile(SOURCE / "test_images.zip") as archive:
        members = {Path(name).stem: name for name in archive.namelist() if name.lower().endswith(".jpg") and not name.startswith("__MACOSX/")}
        if set(members) != {q[0] for q in questions}:
            raise ValueError("Original image archive and test-ID union differ")
        for question, reference in zip(questions, references):
            case_id, text = question
            image_id, category, reference_question, answer = reference
            if case_id != image_id or text != reference_question:
                raise ValueError("Question and scorer reference source order differ")
            raw = archive.read(members[case_id])  # ZIP CRC checked by stdlib.
            content = [{"type": "text", "text": text}, {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64," + base64.b64encode(raw).decode()}}]
            validate_content(content)
            path = OUTPUT / "images" / (case_id + ".jpg")
            path.parent.mkdir(exist_ok=True)
            path.write_bytes(raw)
            cases.append({"task": "V04", "case_id": case_id, "variant": VARIANT, "split": "original_ImageCLEF2019_test500",
                "messages": [{"role": "user", "content": content}]})
            labels.append({"task": "V04", "case_id": case_id, "category": category, "reference_answer": answer, "scorer_only": True})
            images.append({"case_id": case_id, "publisher_archive_member": members[case_id], "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()})
    for name, rows in [("model_inputs.jsonl", cases), ("scorer_references.jsonl", labels)]:
        (OUTPUT / name).write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows))
    write_json(OUTPUT / "image_manifest.json", images)
    report = {"task_id": "V04", "cases": 500, "unique_images": len(images), "source_revision": REVISION,
        "source_files": provenance, "license": "Publisher CC BY4.0", "native_case_order_verified": True,
        "category_counts_scorer_only": dict(Counter(r["category"] for r in labels)),
        "model_facing_fields": ["original_question", "original_image_bytes"],
        "reference_answer_source": "Original challenge reference answers manually validated by two medical doctors; # alternatives and parenthesized optional parts preserved scorer-side.",
        "metric_qualification": "Strict accuracy reconstructed from original organizer protocol plus reference syntax. Exact historical2019 executable not recovered. BLEU withheld until original smoothing/tokenization/aggregation verified; no later-year scorer silently substituted.",
        "paper_comparison": "Same original500 test IDs/images/questions; zero-shot Qwen and explicit fixed scorer reconstruction, not target-fine-tuned MedVInT or a claim of byte-identical challenge scoring.",
        "prepared_files_sha256": {name: file_digest(OUTPUT / name) for name in ["model_inputs.jsonl", "scorer_references.jsonl", "image_manifest.json"]},
        "inference_dispatched": False}
    write_json(ROOT / "reports/vqamed2019_native_preparation.json", report)
    print(json.dumps({"cases": 500, "category_counts": report["category_counts_scorer_only"], "source_revision": REVISION}))


if __name__ == "__main__":
    prepare()
