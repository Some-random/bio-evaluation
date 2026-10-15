"""Freeze original question/image medical VQA tests for local zero-shot runs."""
import argparse
import datetime as dt
import json

from run_local_labbench import ROOT, file_digest, write_json


def prepare(task, gpu):
    if task not in {"V01", "V02"} or gpu not in {4, 5, 6, 7}:
        raise ValueError("Unknown dataset or replica")
    report = json.loads((ROOT / "reports/medical_vqa_preparation.json").read_text())
    dataset = report["datasets"][task]
    path = ROOT / dataset["input_file"]
    cases = [json.loads(line) for line in path.read_text().splitlines()]
    if len(cases) != dataset["cases"] or any(c["task"] != task for c in cases):
        raise ValueError("Native medical split changed")
    if len({c["case_id"] for c in cases}) != len(cases):
        raise ValueError("Duplicate native case ID")
    review_path = ROOT / f"configs/local_medical_{task.lower()}_review.json"
    if review_path.exists():
        raise ValueError("Review already frozen")
    write_json(review_path, {"task_id": task, "input_review_only": True,
               "reviewed_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
               "source_input_path": dataset["input_file"], "source_input_sha256": file_digest(path),
               "basis": "All records validated as public medical-image interpretation questions with exactly the original image and question. Task-level clinical/radiological/anatomical research scope; no biological engineering or operational protocol request. No answer labels, answer groups or model outcomes select inputs.",
               "approved_case_ids": [c["case_id"] for c in cases], "held_cases": [],
               "approved_cases": len(cases), "full_public_cases": len(cases),
               "flagged_requests_transferred": False, "selection_based_on_model_outputs": False,
               "image_contents_manually_reviewed": False,
               "provisional_task_demands": ["medical image evidence interpretation", "medical knowledge", "answer generation"]})
    serving_name = f"configs/local_model_gpu{gpu}.json" if gpu != 5 else "configs/local_model.json"
    serving = json.loads((ROOT / serving_name).read_text())
    settings = json.loads((ROOT / "configs/local_labbench_b03.json").read_text())
    settings.update(run_id=f"qwen38_27b_{task.lower()}_native_test_2026-10-15",
                    frozen_at_utc=dt.datetime.now(dt.timezone.utc).isoformat(), approved_task_ids=[task],
                    variant=dataset["variant"], input_file=dataset["input_file"],
                    review_file=str(review_path.relative_to(ROOT)),
                    runner="scripts/run_local_labbench_multimodal.py", serving_config_file=serving_name,
                    server_record_file=f".local/local_model_server_gpu{gpu}.json" if gpu != 5 else ".local/local_model_server.json",
                    gpu_ids=[gpu], endpoint=f"http://127.0.0.1:{serving['port']}/v1",
                    scorer_reference_file=dataset["label_file"],
                    scorer_reference_sha256=file_digest(ROOT / dataset["label_file"]),
                    source_dataset_revision=dataset.get("source_revision", dataset.get("source_release")),
                    source_code_revision=report["native_scoring_source_revision"],
                    model_facing_fields=dataset["model_facing_fields"], input_modalities=["original_image", "question_text"],
                    prompt_policy=dataset["prompt_policy"],
                    metric_policy="Pinned original LLaVA-Med scorer normalization; OPEN token recall and CLOSED source-rule hit accuracy in separate groups, all eligible cases retained. No mixed overall accuracy or test-derived answer candidates.",
                    paper_comparison="Original dataset question/image test and pinned LLaVA-Med headline scorer; new zero-shot Qwen chat/sampling/training regime differs from task-trained paper systems. Open scoring differs across papers; compare only matching metrics.")
    files = [dataset["input_file"], str(review_path.relative_to(ROOT)), dataset["image_manifest"],
             "scripts/prepare_medical_vqa.py", "scripts/prepare_local_medical_runs.py",
             "scripts/score_local_medical_vqa.py", "scripts/execute_local_medical.py", settings["runner"],
             *[r["path"] for r in report["native_scoring_files"]]]
    settings["frozen_files_sha256"] = {name: file_digest(ROOT / name) for name in sorted(set(files))}
    config = ROOT / f"configs/local_medical_{task.lower()}.json"
    if config.exists():
        raise ValueError("Run config already frozen")
    write_json(config, settings)
    print(json.dumps({"task": task, "cases": len(cases), "gpu": gpu, "config": str(config.relative_to(ROOT))}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--task", required=True)
    parser.add_argument("--gpu", required=True, type=int)
    args = parser.parse_args()
    prepare(args.task, args.gpu)
