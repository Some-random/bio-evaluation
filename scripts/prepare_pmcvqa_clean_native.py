"""Prepare source clean2000 PMC-VQA contracts; finalize only after image acquisition.

Never starts the acquisition worker, model inference, training or queue changes.
Proposals are disabled and require root's explicit review/activation.
"""
import argparse
from collections import Counter
import csv
import datetime as dt
import fcntl
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import time
import zlib

import pmcvqa_clean_protocol as protocol

ROOT=protocol.ROOT
OUTPUT=protocol.OUTPUT
SOURCE=protocol.SOURCE
REPORT=ROOT/"reports/pmcvqa_clean_native_preparation.json"


class ImagesPending(Exception):pass


def immutable_bytes(path,raw):
    path.parent.mkdir(parents=True,exist_ok=True)
    if path.exists():
        if protocol.file_sha(path)!=hashlib.sha256(raw).hexdigest():raise ValueError("Changed prepared artifact; refuse replacement")
    else:
        tmp=path.with_suffix(path.suffix+".tmp");tmp.write_bytes(raw);tmp.replace(path)


def jsonlines(path,rows):immutable_bytes(path,"".join(json.dumps(r,ensure_ascii=False)+"\n" for r in rows).encode())


def source_rows():
    raw=(SOURCE/"test_clean.csv").read_bytes()
    if hashlib.sha256(raw).hexdigest()!=protocol.CSV_SHA:raise ValueError("Publisher clean2000 CSV hash changed")
    rows=list(csv.DictReader(io.StringIO(raw.decode())))
    if len(rows)!=2000 or len({r["Figure_path"] for r in rows})!=1440:raise ValueError("Require full exact clean2000 test")
    for r in rows:
        p=PurePosixPath(r["Figure_path"])
        if len(p.parts)!=1 or p.suffix.lower()!=".jpg" or p.name!=r["Figure_path"]:raise ValueError("Unsafe original image path")
    return rows


def contracts():
    rows=source_rows();sources=protocol.native_sources();inputs=[];refs=[]
    for i,row in enumerate(rows):
        prompt,choices=protocol.native_prompt(row);case_id=f"V05:clean2000:{i:04d}"
        inputs.append({"task":"V05","case_id":case_id,"variant":protocol.VARIANT,"split":"test_clean",
            "source_row_index":i,"prompt":prompt,"source_image_name":row["Figure_path"]})
        refs.append({"task":"V05","case_id":case_id,"variant":protocol.VARIANT,"split":"test_clean",
            "native_choices":choices,**protocol.native_label(row,choices)})
    jsonlines(OUTPUT/"input_contracts.jsonl",inputs);jsonlines(OUTPUT/"labels_before_image_binding.jsonl",refs)
    report={"task_id":"V05","status":"contracts_prepared_waiting_original_images","inference_dispatched":False,
        "variant":protocol.VARIANT,"cases":2000,"required_unique_images":1440,
        "source_revision":protocol.DATA_REVISION,"source_code_revision":protocol.CODE_REVISION,
        "source_csv":"sources/pmcvqa_native/test_clean.csv","source_csv_sha256":protocol.CSV_SHA,
        "image_archive":{"url":f"https://huggingface.co/datasets/xmcmic/PMC-VQA/resolve/{protocol.DATA_REVISION}/images.zip",
            "publisher_archive_bytes":18945102275,"publisher_expected_full_sha256":"cc9f909d6804d0b58111ec8aa7c7b564eece237f24fdcb701916c47beec8285e",
            "full_archive_sha256_verified":False,"acquisition_scope":"Only all1440clean-test required JPEG members via strict publisher HTTP ranges and ZIP CRC/length validation"},
        "native_scoring_files":sources,"native_target_vs_released_label_mismatches":sum(not r["native_target_agrees_with_released_label"] for r in refs),
        "released_label_distribution":dict(Counter(r["target_label"] for r in refs)),
        "model_facing_fields":["source_TD_question_all_four_choices_prompt","original_JPEG_bytes"],
        "scorer_only_fields":["Answer","Answer_label","native_target_index","target_index"],
        "prompt_policy":"Unchanged source TD Test choice order and concatenation: Question: +Question+Choices:+combined A/B/C/D+The Answer is:. No answer, label, figure caption, extra instruction or system message. Full source question/all choices and image retained.",
        "metric_policy":{"primary":"native_td_final_character_accuracy: unchanged native TD generated_texts[i][-1], then AST-extracted difflib SequenceMatcher closest-choice mapping for prediction and source Answer label; original tie rule, no trim/lowercase/normalization.",
            "separate_adaptations":["adapted_full_text_closest_choice_accuracy uses full final assistant string and native Answer-derived target","adapted_full_text_released_label_accuracy uses full final assistant string and released Answer_label","strict_final_label_accuracy uses preregistered last-line A/B/C/D parser and released Answer_label"],
            "missing_policy":"Every frozen test case in all denominators; missing/failed/empty predictions score0, no invented closest-choice fill; undefined native mapping and failed outputs disclosed.",
            "no_test_tuning":True},
        "source_qualifications":["Published clean CSV uses Answer and Answer_label; TD code expects misspelled Anwser and also reads absent Caption. Schema adapter keeps Answer scorer-only; no caption supplied.",
            "TD native scorer consumes only decoded final character, which can be sensitive to punctuation/whitespace. Full-text score is an explicit adaptation, not silently called the same native score.",
            "Native Answer-derived target and released Answer_label disagree for1/2000 source cases; preserve all cases/both references, no target-driven filtering.",
            "TE source evaluation uses a different label-based get_generated_texts procedure; no TE exact-paper score or trained-head reproduction claim.",
            "Original full19GB image archive is partially acquired by exact publisher ZIP ranges; full archive SHA256 is not verified. Required member CRC/length/JPEG signatures and range/image SHA256 are verified separately."],
        "interpretation":{"likely_demands":{"labels":["medical_visual_evidence_interpretation","medical_knowledge","multiple_choice_question_answering"],"status":"provisional analyst description, no inference about internal computation"},
            "actually_supplied":"Source TD question plus all four source choices and original required JPEG only","reference_answer_source":"Pinned public PMC-VQA clean-test Answer and Answer_label annotations, stored separately for offline scorer",
            "good_score_establishes":"Recovery of source choice targets under this specified model/input/output-adapter/metric","bad_score_establishes":"Limited answer recovery under this protocol; does not isolate reasoning or establish clinical competence",
            "explanation_correctness":"Unassessed independently of chosen answers; absent mechanistic support is not automatic falsity"},
        "comparison_to_paper":"Fixed local zero-shot Qwen vision baseline on complete native clean2000 set and source TD question/choice strings. Qwen chat, image preprocessing, free generation and training differ from MedVInT. Match metric/output extraction and clean split before comparing; full-text metric is adapted, TE systems are not exact reproductions. Public pretraining exposure unknown."}
    if REPORT.exists() and json.loads(REPORT.read_text()).get("status")=="prepared_full_native_clean2000_test":
        # Re-running contract validation cannot erase completed preparation.
        report=json.loads(REPORT.read_text())
    else:protocol.save_json(REPORT,report)
    return rows,inputs,refs,report


def image_records(rows):
    progress=ROOT/"reports/pmcvqa_clean_image_acquisition.json"
    if not progress.exists() or json.loads(progress.read_text()).get("stage")!="complete":raise ImagesPending("Existing original-image acquisition is not complete; no duplicate worker started")
    records=[json.loads(s) for s in (SOURCE/"clean_image_acquisition.jsonl").read_text().splitlines() if s]
    mapping={r["image_name"]:r for r in records};expected={r["Figure_path"] for r in rows}
    if len(mapping)!=len(records) or set(mapping)!=expected:raise ValueError("Acquisition journal differs from exact full required image set")
    metadata=json.loads((SOURCE/"selected_image_zip_metadata.json").read_text())
    result=[]
    from PIL import Image
    for name in sorted(expected):
        path=OUTPUT/"images"/name;raw=path.read_bytes();record=mapping[name];member=metadata[name]
        if (hashlib.sha256(raw).hexdigest()!=record["sha256"] or len(raw)!=record["bytes"] or len(raw)!=member["file_size"]
                or zlib.crc32(raw)&0xffffffff!=record["publisher_zip_crc32"] or record["publisher_zip_crc32"]!=member["CRC"]
                or record["publisher_archive_member"]!=member["filename"] or not raw.startswith(b"\xff\xd8\xff")):
            raise ValueError("Required original image changed or ZIP identity inconsistent")
        ranges=record["source_ranges"]
        if (not ranges or ranges[0]["start"]!=member["header_offset"]
                or any(r["bytes"]!=r["end"]-r["start"]+1 or len(r["sha256"])!=64 for r in ranges)):
            raise ValueError("Bounded original image range provenance inconsistent")
        with Image.open(io.BytesIO(raw)) as image:image.verify()
        with Image.open(io.BytesIO(raw)) as image:width,height=image.size;mode=image.mode
        result.append({"path":str(path.relative_to(ROOT)),"image_name":name,"sha256":record["sha256"],"bytes":len(raw),
            "publisher_archive_member":record["publisher_archive_member"],"publisher_zip_crc32":record["publisher_zip_crc32"],
            "width":width,"height":height,"mode":mode,"image_bytes_modified":False,
            "publisher_full_archive_sha256_verified":False,"source_ranges":record["source_ranges"]})
    return result


def finalize(gpu=6):
    rows,inputs,refs,report=contracts();images=image_records(rows);mapping={r["image_name"]:r for r in images}
    target=OUTPUT/"model_inputs.jsonl";temporary=target.with_suffix(".jsonl.finalizing")
    with temporary.open("w") as stream:
        for i,row in enumerate(rows):stream.write(json.dumps(protocol.model_case(i,row,(OUTPUT/"images"/row["Figure_path"]).read_bytes()),ensure_ascii=False)+"\n")
    if target.exists():
        if protocol.file_sha(target)!=protocol.file_sha(temporary):raise ValueError("Frozen complete model inputs changed")
        temporary.unlink()
    else:temporary.replace(target)
    refs=[{**ref,"image_sha256":mapping[row["Figure_path"]]["sha256"]} for row,ref in zip(rows,refs)]
    jsonlines(OUTPUT/"labels.jsonl",refs)
    immutable_bytes(OUTPUT/"image_manifest.json",(json.dumps(images,indent=2)+"\n").encode())
    immutable_bytes(OUTPUT/"ordered_case_ids.json",(json.dumps([r["case_id"] for r in inputs],indent=2)+"\n").encode())
    report.update(status="prepared_full_native_clean2000_test",unique_images=len(images),
        input_file=str(target.relative_to(ROOT)),label_file=str((OUTPUT/"labels.jsonl").relative_to(ROOT)),
        image_manifest=str((OUTPUT/"image_manifest.json").relative_to(ROOT)),
        image_acquisition_report="reports/pmcvqa_clean_image_acquisition.json",publisher_full_archive_sha256_verified=False,
        files=[{"path":str(p.relative_to(ROOT)),"sha256":protocol.file_sha(p),"bytes":p.stat().st_size} for p in sorted(OUTPUT.iterdir()) if p.is_file()])
    protocol.save_json(REPORT,report)
    return propose(inputs,report,gpu)


def propose(inputs,report,gpu):
    if gpu not in {4,5,6,7}:raise ValueError("Unexpected existing TP1 replica")
    review_name="configs/local_pmcvqa_v05_review.proposed.json";review_path=ROOT/review_name
    review={"task_id":"V05","input_review_only":True,"reviewed":False,"execution_authorized":False,
        "basis":"Proposed whole clean2000 task review; root must review and activate before dispatch. No model-output or label-based case selection.",
        "approved_case_ids":[r["case_id"] for r in inputs],"held_cases":[],"source_input_sha256":protocol.file_sha(ROOT/report["input_file"])}
    immutable_bytes(review_path,(json.dumps(review,indent=2)+"\n").encode())
    serving_name=f"configs/local_model_gpu{gpu}.json" if gpu!=5 else "configs/local_model.json"
    serving=json.loads((ROOT/serving_name).read_text())
    settings=json.loads((ROOT/"configs/local_medical_v01.json").read_text())
    settings.update(run_id="qwen38_27b_v05_pmcvqa_clean2000_td_2026-10-15",execution_authorized=False,
        frozen_at_utc=dt.datetime.now(dt.timezone.utc).isoformat(),approved_task_ids=["V05"],variant=protocol.VARIANT,
        input_file=report["input_file"],review_file=review_name,scorer_reference_file=report["label_file"],
        scorer_reference_sha256=protocol.file_sha(ROOT/report["label_file"]),
        source_dataset_revision=protocol.DATA_REVISION,source_code_revision=protocol.CODE_REVISION,
        source_csv_file="sources/pmcvqa_native/test_clean.csv",source_csv_sha256=protocol.CSV_SHA,
        model_facing_fields=report["model_facing_fields"],input_modalities=["original_JPEG_image","question_all_choices_text"],
        runner="scripts/run_local_labbench_multimodal.py",executor="scripts/execute_local_pmcvqa.py",scorer="scripts/score_local_pmcvqa.py",
        serving_config_file=serving_name,server_record_file=f".local/local_model_server_gpu{gpu}.json" if gpu!=5 else ".local/local_model_server.json",
        gpu_ids=[gpu],endpoint=f"http://127.0.0.1:{serving['port']}/v1",generation=protocol.GENERATION,
        prompt_policy=report["prompt_policy"],metric_policy=report["metric_policy"],paper_comparison=report["comparison_to_paper"])
    files=[review_name,report["input_file"],report["image_manifest"],"data/pmcvqa_clean_native/input_contracts.jsonl",
           "scripts/pmcvqa_clean_protocol.py","scripts/prepare_pmcvqa_clean_native.py","scripts/score_local_pmcvqa.py",
           "scripts/execute_local_pmcvqa.py",settings["runner"],*[r["path"] for r in report["native_scoring_files"]]]
    settings["frozen_files_sha256"]={name:protocol.file_sha(ROOT/name) for name in sorted(set(files))}
    path=ROOT/"configs/local_pmcvqa_v05.proposed.json"
    if path.exists():
        previous=json.loads(path.read_text());settings["frozen_at_utc"]=previous["frozen_at_utc"]
        if previous!=settings:raise ValueError("Existing disabled proposal changed")
    else:protocol.save_json(path,settings)
    print(json.dumps({"status":"prepared_disabled_proposal","cases":2000,"images":1440,"proposal":str(path.relative_to(ROOT))}),flush=True)
    return settings


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument("--finalize",action="store_true");parser.add_argument("--watch-finalize",action="store_true");parser.add_argument("--gpu",type=int,default=6);parser.add_argument("--poll-seconds",type=int,default=30)
    args=parser.parse_args()
    if not 1<=args.poll_seconds<=60:raise SystemExit("Poll interval must be1-60seconds")
    lock_path=ROOT/".local/pmcvqa_clean_preparation.lock";lock_path.parent.mkdir(parents=True,exist_ok=True)
    with lock_path.open("a") as lock:
        fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
        if not args.finalize and not args.watch_finalize:
            _,_,_,report=contracts();print(json.dumps({"status":report["status"],"cases":report["cases"]}));raise SystemExit(0)
        while True:
            try:finalize(args.gpu);break
            except ImagesPending as exc:
                print(json.dumps({"status":"images_pending","detail":str(exc),"inference_dispatched":False}),flush=True)
                if not args.watch_finalize:raise SystemExit(2)
                time.sleep(args.poll_seconds)
