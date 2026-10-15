"""Freeze one reviewed public LAB category for the existing local server."""
import argparse
import base64
import datetime as dt
import hashlib
import json
from pathlib import Path

from run_local_labbench import ROOT, file_digest, write_json


def native_messages(row):
    original = row["payload"]
    if original.get("tools") or len(original["input"]) != 1:
        raise ValueError("Unexpected native solver tools or conversation")
    message = original["input"][0]
    if message["role"] != "user":
        raise ValueError("Unexpected native role")
    converted, images = [], []
    for item in message["content"]:
        if item["type"] == "input_text" and set(item) == {"type", "text"}:
            converted.append({"type": "text", "text": item["text"]})
        elif item["type"] == "input_image" and set(item) <= {"type", "image_url", "detail"}:
            url = item["image_url"]
            if not url.startswith(("data:image/png;base64,", "data:image/jpeg;base64,")):
                raise ValueError("Only supplied inline original images may reach the solver")
            raw = base64.b64decode(url.split(",", 1)[1], validate=True)
            images.append(hashlib.sha256(raw).hexdigest())
            image = {"url": url}
            if "detail" in item:
                image["detail"] = item["detail"]
            converted.append({"type": "image_url", "image_url": image})
        else:
            raise ValueError("Unexpected native input type")
    if images != row["fields"].get("images_sha256", []):
        raise ValueError("Original image checksums differ")
    content = converted[0]["text"] if len(converted) == 1 and converted[0]["type"] == "text" else converted
    return [{"role": "user", "content": content}]


def prepare(task, runner="scripts/run_local_labbench.py"):
    review_path = ROOT / f"configs/local_labbench_{task.lower()}_review.json"
    review = json.loads(review_path.read_text())
    source = ROOT / review["source_input_path"]
    if file_digest(source) != review["source_input_sha256"] or review["task_id"] != task:
        raise ValueError("Review does not match native source inputs")
    selected = {}
    for line in source.open():
        row = json.loads(line)
        if row["task"] == task:
            selected[row["case_id"]] = row
    allowed = review["approved_case_ids"]
    if len(set(allowed)) != len(allowed) or set(allowed) & {r["case_id"] for r in review["held_cases"]}:
        raise ValueError("Review allowlist overlaps held cases or has duplicates")
    variant = "NATIVE_PUBLIC_COT_LOCAL_REVIEWED"
    cases = [{"task": task, "case_id": identity, "variant": variant,
              "split": selected[identity]["split"], "messages": native_messages(selected[identity])}
             for identity in allowed]
    if runner.endswith("run_local_labbench.py") and any(not isinstance(c["messages"][0]["content"], str) for c in cases):
        raise ValueError("Image cases require the multimodal runner")
    target = ROOT / "data/local_labbench_suite" / task / "model_inputs.jsonl"
    if target.exists():
        raise ValueError("A prepared execution input already exists; do not overwrite frozen runs")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("".join(json.dumps(c, ensure_ascii=False) + "\n" for c in cases))
    local = json.loads((ROOT / "configs/local_model.json").read_text())
    if task not in local["approved_task_ids"]:
        raise ValueError("Local execution authorization must be recorded before freezing this task")
    settings = json.loads((ROOT / "configs/local_labbench_litqa2.json").read_text())
    settings.update(run_id=f"qwen38_27b_{task.lower()}_public_reviewed_2026-10-15",
                    frozen_at_utc=dt.datetime.now(dt.timezone.utc).isoformat(), approved_task_ids=[task],
                    variant=variant, input_file=str(target.relative_to(ROOT)),
                    review_file=str(review_path.relative_to(ROOT)), runner=runner,
                    scorer_reference_file="data/labbench_native_complete/scorer_references.jsonl",
                    scorer_reference_sha256=file_digest(ROOT / "data/labbench_native_complete/scorer_references.jsonl"),
                    model_facing_fields=sorted(set(k for identity in allowed for k in selected[identity]["fields"])),
                    paper_comparison="Native public prompts, choices, required context/images and metrics. Reviewed public release; one fixed-seed run, not the original full public/private three-run paper mean. Strict deterministic parser; no model extraction fallback.")
    files = [settings["input_file"], settings["review_file"], runner,
             "scripts/score_local_labbench_suite.py", "scripts/execute_local_labbench_suite.py",
             "scripts/run_local_labbench.py", "scripts/score_results.py",
             "scripts/prepare_local_labbench_run.py", "sources/chembench_constant.py",
             "reports/labbench_native_complete_preparation.json"]
    settings["frozen_files_sha256"] = {f: file_digest(ROOT / f) for f in sorted(set(files))}
    config_path = ROOT / f"configs/local_labbench_{task.lower()}.json"
    if config_path.exists():
        raise ValueError("Execution config already exists; do not replace a frozen protocol")
    write_json(config_path, settings)
    print(json.dumps({"config": str(config_path.relative_to(ROOT)), "cases": len(cases), "task": task}))
    return config_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--task", required=True)
    parser.add_argument("--runner", default="scripts/run_local_labbench.py")
    args = parser.parse_args()
    prepare(args.task, args.runner)
