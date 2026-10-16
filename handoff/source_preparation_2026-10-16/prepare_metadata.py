import collections, datetime, hashlib, json, pathlib, tarfile
ROOT=pathlib.Path(__file__).resolve().parent

def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def json_save(path, value):path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(value,indent=2)+"\n")
def jsonl_save(path,rows):path.parent.mkdir(parents=True,exist_ok=True);path.write_text("".join(json.dumps(row,ensure_ascii=False)+"\n" for row in rows))
manifest=json.loads((ROOT/"source_manifest.json").read_text())
for item in manifest["artifacts"]:
    path=ROOT/item["path"]
    assert path.stat().st_size==item["bytes"] and digest(path)==item["sha256"],item["path"]
    item["git_blob_source_representation"]="lfs_pointer" if item.get("publisher_lfs_sha256") else "file"
json_save(ROOT/"source_manifest.json",manifest)
questions=[json.loads(line) for line in (ROOT/"sources/llava_main/data/eval/llava_med_eval_qa50_qa.jsonl").read_text().splitlines()]
images=json.loads((ROOT/"v06_image_recovery.json").read_text())["images"]
image_by_id={row["pair_id"]:row for row in images}
assert len(image_by_id)==50
assert len({q["question_id"] for q in questions})==193
assert len({q["image"] for q in questions})==50
assert all(q["image"]==q["pair_id"]+".jpg" for q in questions)
assert all(q["pair_id"] in image_by_id for q in questions)
question_only=[{key:row[key] for key in ["question_id","image","pair_id","text"]} for row in questions]
assert all(set(row)=={"question_id","image","pair_id","text"} for row in question_only)
jsonl_save(ROOT/"data/V06/input_only_questions.jsonl",question_only)
index=[]
for row in images:
    result={key:row[key] for key in ["pair_id","pmc_tar_url","image_file_path","status"]}
    if row["status"].startswith("recovered"):
        path=ROOT/row["image_path"]
        assert digest(path)==row["image_sha256"]
        result.update(image_path=row["image_path"],image_sha256=row["image_sha256"],image_bytes=path.stat().st_size,image_url=row["image_url"],pmc_page_url=row["pmc_page_url"],exact_article_id_and_filename_matched=True,historical_image_digest_verified=False)
    else:result.update(blocker=row["error"],pmc_page_url=row["pmc_page_url"])
    index.append(result)
jsonl_save(ROOT/"data/V06/source_image_index.jsonl",index)
ready={x["pair_id"] for x in index if x["status"].startswith("recovered")}
repo_prefix=".local/continuation_2026-10-16/source_prep/"
report={"created_at_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),"scope":"Public source recovery and metadata validation only. No inference, judge calls, frozen config changes, scoring or training.","inference_performed":False,"provider_keys_read":False,"existing_frozen_files_modified":False,"new_execution_ready_settings":0,"artifacts_root":repo_prefix.rstrip("/"),"verification":{"source_assets":len(manifest["artifacts"]),"publisher_git_blobs_verified":sum(bool(x.get("publisher_blob_verified")) for x in manifest["artifacts"]),"publisher_lfs_payloads_sha256_verified":sum(bool(x.get("publisher_lfs_sha256")) for x in manifest["artifacts"]),"source_and_recovered_image_hashes_revalidated":True},"tasks":[{"task_id":"V06","task":"LLaVA-Med visual conversation (QA50)","status":"source_partially_recovered_native_external_judge_still_held","native_source_pin":manifest["repository_pins"]["llava_main"][1],"original_v1_code_pin":manifest["repository_pins"]["llava_v1"][1],"questions_verified":193,"original_images_expected":50,"question_types":dict(collections.Counter(q["type"] for q in questions)),"questions_matched_to_source_manifest":193,"images_recovered":len(ready),"questions_with_recovered_images":sum(q["pair_id"] in ready for q in questions),"source_archive_urls_http_404":50,"remaining_images":50-len(ready),"remaining_source_blocker":"PMC article pages for the remaining 31 images returned a browser/reCAPTCHA challenge. No challenge solving, bypass, mirror substitution or alternate image selection was attempted.","image_identity":"Recovered bytes use the exact source PMCID and exact original source image filename, from the original NCBI article image URL. Current bytes are hashed; historical publisher image hashes are not available.","input_allowlist":["question_id","image","pair_id","text"],"solver_excluded_fields":["gpt4_answer","fig_caption","in_text_mention","domain","type","fig_label"],"data_inputs":"data/V06/input_only_questions.jsonl","source_image_index":"data/V06/source_image_index.jsonl","native_judge":"GPT-4-0314; teacher answer is assistant 1 and model answer assistant 2; judge sees caption and inline mentions; helpfulness/relevance/accuracy/detail scored 1 through 10.","native_metric":"100 * mean(model_answer_score / teacher_answer_score), grouped by question type/domain and overall, as in the pinned official evaluator; do not substitute ratio of aggregate means.","native_score_blocker":"Native evaluation requires the external GPT-4 judge. The current provider hold remains active; no local substitute judge or fabricated native score.","qwen_capability_vs_execution":"Qwen vision can accept image/question inputs; model compatibility does not resolve missing assets, input review/freeze, or the native external judge.","primary_sources":["https://github.com/microsoft/LLaVA-Med/blob/30697ca50b5c29a8e955c99330b259776aef27b9/README.md#evaluation","https://github.com/microsoft/LLaVA-Med/blob/30697ca50b5c29a8e955c99330b259776aef27b9/llava/eval/eval_multimodal_chat_gpt_score.py","https://github.com/microsoft/LLaVA-Med/blob/30697ca50b5c29a8e955c99330b259776aef27b9/llava/eval/summarize_gpt_review.py"]},{"task_id":"V07","task":"Ryze extraction component tests","status":"exact_component_manifest_and_execution_recipe_unrecovered","publisher_commit":"41b2d77ec0651b9f51b657f524415ee3cc38e115","publisher_commit_changed_since_previous_audit":False,"newly_restored_source_files":5,"source_tree_blob_count":81,"exact_cases_verified":0,"blockers":["Exact component case IDs, splits and source-media/page mapping for ArXivQA, SlideVQA and ChartQA are not present in the inspected public tree.","Extraction condition, answer-model checkpoint/prompt and exact scoring/aggregation contract for Table 3 remain unrecovered.","The generic benchmark loader generates synthetic placeholder data when no benchmark JSON exists; those rows are not benchmark evidence."],"resolution":"Obtain author component manifest and execution recipe; generic direct Qwen image QA is a different baseline and does not complete this extraction setting.","primary_sources":["https://github.com/Chivier/Ryze/tree/41b2d77ec0651b9f51b657f524415ee3cc38e115","https://arxiv.org/html/2606.00902v1#S3.SS3"]},{"task_id":"P27","task":"NatureLM temporal NCBI protein-description test","status":"exact_temporal_test_release_unrecovered","publisher_commit":"bcb1351bc6490d4a98cae74e7eead30a028fae00","publisher_commit_changed_since_previous_audit":False,"newly_restored_source_files":3,"exact_cases_verified":0,"blockers":["The current publisher tree still lacks the exact temporal test case IDs, source sequence/reference snapshots, cutoff and executable ROUGE-L preprocessing."],"resolution":"Obtain author temporal manifest and scoring contract. Do not replace it with Mol-Instructions or arbitrary current NCBI proteins.","primary_sources":["https://github.com/microsoft/SFM/tree/bcb1351bc6490d4a98cae74e7eead30a028fae00/NatureLM","https://arxiv.org/html/2502.07527v3#S4.SS4"]}]}
json_save(ROOT/"audit.json",report)
text="""# Public-source preparation update — 16 October 2026

No model inference, judge calls, training or frozen-run changes were made.

| Setting | Progress | Remaining blocker |
|---|---|---|
| LLaVA-Med visual conversation (QA50) | Publisher-verified 193 questions for 50 images, full teacher/context metadata and native judge scripts recovered. 19 original image files recovered, covering 73 questions. | All 50 legacy archive URLs return 404; 31 remaining PMC pages present a browser/reCAPTCHA challenge. Native score also requires the held external GPT-4 judge. |
| Ryze document extraction | Pinned source tree and 5 relevant implementation files restored; publisher commit unchanged. | Exact ArXivQA/SlideVQA/ChartQA component manifests and Table 3 pipeline/answer/scoring contract are unrecovered. Synthetic fallback rows are invalid benchmark data. |
| NatureLM temporal protein descriptions | Pinned source tree and 3 NatureLM files restored; publisher commit unchanged. | Exact temporal case list, sequence/reference snapshots, cutoff and ROUGE-L preprocessing remain unavailable in inspected release. |

LLaVA-Med's 193 questions comprise 143 conversation and 50 detailed-description prompts. The input-only question export contains only question ID, source image ID, image filename and original question text. Teacher answers, captions and inline mentions remain in the original scorer-side source files. The recovered images match each original article ID and exact source image filename; their current bytes are hashed, but no historical publisher image digest is available. Image acquisition stopped at the access challenge.

The native LLaVA-Med scorer asks GPT-4-0314 to grade the teacher answer and candidate answer with caption/inline context. Its relative score is the mean of per-question candidate/teacher score ratios, multiplied by 100. A substitute judge would change the evaluation. Qwen vision compatibility alone does not remove this external-evaluator blocker.

`audit.json` records exact counts, source pins, blockers and validation; `source_manifest.json` records source URLs and SHA-256 checks. `v06_image_recovery.json` records image provenance and acquisition failures. The source bundle excludes article HTML/browser-challenge responses and contains no credentials or weights.

Sources: [official LLaVA-Med evaluation](https://github.com/microsoft/LLaVA-Med/blob/30697ca50b5c29a8e955c99330b259776aef27b9/README.md#evaluation), [judge](https://github.com/microsoft/LLaVA-Med/blob/30697ca50b5c29a8e955c99330b259776aef27b9/llava/eval/eval_multimodal_chat_gpt_score.py), [native aggregation](https://github.com/microsoft/LLaVA-Med/blob/30697ca50b5c29a8e955c99330b259776aef27b9/llava/eval/summarize_gpt_review.py), [Ryze source](https://github.com/Chivier/Ryze/tree/41b2d77ec0651b9f51b657f524415ee3cc38e115), [NatureLM source](https://github.com/microsoft/SFM/tree/bcb1351bc6490d4a98cae74e7eead30a028fae00/NatureLM).
"""
(ROOT/"audit.md").write_text(text)
paths=[f for f in ROOT.rglob("*") if f.is_file() and "pmc_pages" not in f.parts and f.name not in {"source_prep_bundle.tar.gz","bundle_manifest.json"}]
with tarfile.open(ROOT/"source_prep_bundle.tar.gz","w:gz") as archive:
    for path in sorted(paths):archive.add(path,arcname=str(path.relative_to(ROOT)),recursive=False)
json_save(ROOT/"bundle_manifest.json",{"path":"source_prep_bundle.tar.gz","bytes":(ROOT/"source_prep_bundle.tar.gz").stat().st_size,"sha256":digest(ROOT/"source_prep_bundle.tar.gz"),"members":len(paths),"excluded":"Current PMC article HTML and browser challenge responses.","files":[{"path":str(f.relative_to(ROOT)),"bytes":f.stat().st_size,"sha256":digest(f)} for f in sorted(paths)]})
print(json.dumps({"source_assets_verified":len(manifest["artifacts"]),"questions":len(questions),"images_recovered":len(ready),"questions_with_images":sum(q["pair_id"] in ready for q in questions),"bundle_bytes":(ROOT/"source_prep_bundle.tar.gz").stat().st_size,"bundle_members":len(paths)},indent=2))
