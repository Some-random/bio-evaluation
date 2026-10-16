"""Prepare the complete pinned public PathVQA mirror test with source caveats.

This is acquisition/preparation only. Images and question text are retained;
answers/groups are scorer-only. No solver, judge, training or inference call.
"""
import base64
from collections import Counter, defaultdict
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import re
import sys
import types

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/"sources/pathvqa_native"
OUTPUT=ROOT/"data/pathvqa_native/V03"
HF_REVISION="1685832883334b5bb5beaf4e4b333fdeecaa4ad9"
ORIGINAL_REVISION="117e7f4ef88a0e65b0e7f37b98a73d6237a3ceab"
LLAVA_REVISION="b9a98a736d2ef05bcf5ff345be6403fb3a664eaf"
VARIANT="SOURCE_QUALIFIED_PATHVQA_HF_TEST_IMAGE_ZERO_SHOT"
TEST_FILES={
 "test-00000-of-00003-e9adadb4799f44d3.parquet":"533175be08e87b9ccf2fc06e2f82e58bb2e9bf2299a4a138cf5311f1d26ac157",
 "test-00001-of-00003-7ea98873fc919813.parquet":"84bde926245c4b136de6ef48b197a0f3f177b3fbcb03b7f3cbfcfcb212f20c50",
 "test-00002-of-00003-1628308435019820.parquet":"ae676f41a7ddfc85be8503a731c719e1608da37ddc981de42a10dd2d55a8ee87"}
ORIGINAL_TEST="original_baselines__method1__saved__lxmert__pvqa_test.json"
ORIGINAL_TEST_BLOB="2f85d6b12cea12c296c6be5f42ac9b9e131b23ea"
MIRROR_CODE_SHA="d0bb086b5f87f883652bfe7dff378b72ea9a72aeedcab5b8d5553fdea59fb7c6"


def sha(raw):return hashlib.sha256(raw).hexdigest()
def file_sha(path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda:f.read(1024*1024),b""):h.update(block)
    return h.hexdigest()


def save(path,raw):
    path.parent.mkdir(parents=True,exist_ok=True)
    if path.exists():
        if file_sha(path)!=sha(raw):raise ValueError("Refuse to replace changed prepared artifact: "+str(path))
        return
    temporary=path.with_suffix(path.suffix+".tmp");temporary.write_bytes(raw);temporary.replace(path)


def save_json(path,value):save(path,(json.dumps(value,ensure_ascii=False,indent=2)+"\n").encode())
def mirror_normalize(text):
    # Verbatim transformation from pinned mirror scripts/processing.py.
    return re.sub(' +',' ',str(text).lower()).replace(" ?","?").strip()


def image_mime(raw):
    if raw.startswith(b"\xff\xd8\xff"):return "image/jpeg",".jpg"
    if raw.startswith(b"\x89PNG\r\n\x1a\n"):return "image/png",".png"
    raise ValueError("Required image bytes missing or unsupported")


def model_case(index,row):
    """Access input fields only; gold cannot change the question or image."""
    raw=row["image"]["bytes"];mime,_=image_mime(raw)
    if not isinstance(row["question"],str) or not row["question"]:raise ValueError("Missing released question")
    return {"task":"V03","case_id":f"V03:hf_test:{index:05d}","variant":VARIANT,"split":"publisher_hf_test",
            "messages":[{"role":"user","content":[{"type":"text","text":row["question"]},
                {"type":"image_url","image_url":{"url":"data:"+mime+";base64,"+base64.b64encode(raw).decode()}}]}]}


def source_identity(original,mirror):
    """Source-only identity audit; never selects cases by predictions or scores."""
    index=defaultdict(set);image_qas=defaultdict(set)
    for row in mirror:
        pair=(row["question"],row["answer"]);h=sha(row["image"]["bytes"])
        index[pair].add(h);image_qas[h].add(pair)
    fingerprints=defaultdict(set)
    for h,pairs in image_qas.items():fingerprints[frozenset(pairs)].add(h)
    triplets=[];candidate_counts=Counter();original_fingerprints=Counter()
    for group in original:
        questions,labels=group["sentf"]["pvqa"],group["labelf"]["pvqa"]
        if len(questions)!=len(labels):raise ValueError("Original source question/label arity mismatch")
        pairs=set()
        for question,label in zip(questions,labels):
            if len(label)!=1 or next(iter(label.values()))!=1:raise ValueError("Unexpected original label ontology")
            answer=next(iter(label));triplets.append((group["img_id"],question,answer))
            pairs.add((mirror_normalize(question),mirror_normalize(answer)))
        if pairs:
            frozen=frozenset(pairs);original_fingerprints[frozen]+=1;candidate_counts[len(fingerprints[frozen])]+=1
    unique=list(dict.fromkeys(triplets))
    native_pairs=Counter((mirror_normalize(q),mirror_normalize(a)) for _,q,a in unique)
    mirror_pairs=Counter((row["question"],row["answer"]) for row in mirror)
    if native_pairs!=mirror_pairs:raise ValueError("Full normalized deduplicated source test QA multiset differs")
    mirror_fingerprints=Counter(frozenset(pairs) for pairs in image_qas.values())
    return {"original_test_question_count":len(triplets),"original_unique_exact_triplet_count":len(unique),
            "mirror_test_question_count":len(mirror),"removed_exact_triplet_duplicates":len(triplets)-len(unique),
            "full_normalized_deduplicated_question_answer_multiset_match":True,
            "source_image_group_count":len(original),"source_image_groups_with_questions":sum(original_fingerprints.values()),
            "mirror_unique_image_bytes":len(image_qas),"full_qa_group_fingerprint_multiset_match":original_fingerprints==mirror_fingerprints,
            "source_image_group_candidate_counts":dict(candidate_counts),
            "original_per_image_byte_identity_verified":False,
            "caveat":"Original native test has duplicate rows and unnormalized text. Mirror de-duplicates exact image/question/answer triplets, then lowercases, collapses spaces, removes space before question mark and strips question/answer strings. Source grouping cannot uniquely identify all original image IDs; original image bytes are unavailable directly. This is the full pinned mirror test, not byte-identical original-paper reproduction."}


def scoring_sources():
    tree=json.loads((ROOT/"sources/medical_vqa/llavamed_v1_tree.json").read_text())["tree"]
    mapping={"sources/pathvqa_native/llava_v1_run_eval_pvqa.py":"llava/eval/run_eval_pvqa.py",
             **{f"sources/medical_vqa/llava_v1_{n}.py":f"llava/eval/eval_metrics/{n}.py" for n in ["evaluate_metrics","glossary","utils"]}}
    result=[]
    for local,remote in mapping.items():
        raw=(ROOT/local).read_bytes();expected=next(r["sha"] for r in tree if r["path"]==remote)
        if hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()!=expected:raise ValueError("Pinned official scorer blob changed")
        result.append({"path":local,"sha256":sha(raw),"publisher_git_blob_sha1":expected,
            "url":f"https://raw.githubusercontent.com/microsoft/LLaVA-Med/{LLAVA_REVISION}/{remote}","publisher_digest_verified":True})
    return result


def source_chain():
    if file_sha(SOURCE/"hf_scripts__processing.py")!=MIRROR_CODE_SHA:raise ValueError("Pinned mirror transformation source changed")
    receipt=json.loads((SOURCE/"original_git_verified_tree.json").read_text())
    if receipt["commit"]!=ORIGINAL_REVISION or receipt.get("git_commit_verified") is not True:raise ValueError("Original Git identity receipt changed")
    names=[ORIGINAL_TEST,"original_git_verified_tree.json","hf_scripts__processing.py","hf_README.md","hf_data_tree.json","hf_metadata.json","original_data__README.md"]
    return [{"path":str((SOURCE/name).relative_to(ROOT)),"sha256":file_sha(SOURCE/name),"bytes":(SOURCE/name).stat().st_size} for name in names]


def native_modules():
    scoring_sources()
    package_name="_bioeval_pathvqa_llava_v1"
    if package_name+".evaluate_metrics" not in sys.modules:
        package=types.ModuleType(package_name);package.__path__=[];sys.modules[package_name]=package
        for name in ["utils","glossary","evaluate_metrics"]:
            path=ROOT/f"sources/medical_vqa/llava_v1_{name}.py"
            spec=importlib.util.spec_from_file_location(package_name+"."+name,path)
            module=importlib.util.module_from_spec(spec);sys.modules[spec.name]=module;spec.loader.exec_module(module)
    return sys.modules[package_name+".glossary"],sys.modules[package_name+".evaluate_metrics"]


def score_answer(prediction,reference,group):
    glossary,metrics=native_modules()
    prediction=glossary.normalize_word((prediction if isinstance(prediction,str) else "").lower())
    reference=glossary.normalize_word(reference.lower())
    if group=="OPEN":
        f1,precision,recall=metrics.calculate_f1score(prediction,reference)
        return {"open_token_recall":recall,"open_token_precision":precision,"open_token_f1":f1}
    if group!="CLOSED" or reference not in {"yes","no"}:raise ValueError("Unknown native answer group")
    has_label="yes" in prediction or "no" in prediction
    hit=bool(has_label and reference in prediction)
    return {"closed_native_substring_hit_corrected":int(hit),
            "closed_strict_exact_hit":int(prediction in {"yes","no"} and prediction==reference),
            "closed_bug_compatible_numerator":int(hit),
            "closed_bug_compatible_denominator":int(hit or not has_label)}


def metrics_for(rows):
    """Separate group metrics; the defective source denominator stays visible."""
    opened=[r for r in rows if r["answer_type"]=="OPEN"]
    closed=[r for r in rows if r["answer_type"]=="CLOSED"]
    if len(opened)+len(closed)!=len(rows):raise ValueError("Unknown answer group")
    bug_num=sum(r["native_scores"]["closed_bug_compatible_numerator"] for r in closed)
    bug_den=sum(r["native_scores"]["closed_bug_compatible_denominator"] for r in closed)
    return {"open_token_recall":sum(r["native_scores"]["open_token_recall"] for r in opened)/len(opened) if opened else None,
            "closed_accuracy_corrected":sum(r["native_scores"]["closed_native_substring_hit_corrected"] for r in closed)/len(closed) if closed else None,
            "closed_strict_exact_accuracy":sum(r["native_scores"]["closed_strict_exact_hit"] for r in closed)/len(closed) if closed else None,
            "closed_bug_compatible_accuracy":bug_num/bug_den if bug_den else 0.,
            "closed_bug_compatible_denominator":bug_den,"closed_bug_compatible_omitted":len(closed)-bug_den,
            "open_denominator":len(opened),"closed_corrected_denominator":len(closed)}


def prepare():
    import pyarrow.parquet as pq
    from PIL import Image
    rows=[];sources=[]
    for name,expected in TEST_FILES.items():
        path=SOURCE/name
        if file_sha(path)!=expected:raise ValueError("Pinned publisher test Parquet SHA mismatch")
        for i,row in enumerate(pq.read_table(path).to_pylist()):rows.append({**row,"_parquet":name,"_row":i})
        sources.append({"path":str(path.relative_to(ROOT)),"sha256":expected,"bytes":path.stat().st_size,
            "publisher_lfs_digest_verified":True,"url":f"https://huggingface.co/datasets/flaviagiammarino/path-vqa/resolve/{HF_REVISION}/data/{name}"})
    if len(rows)!=6719:raise ValueError("Require every row of the exact released mirror test")
    original_path=SOURCE/ORIGINAL_TEST;raw=original_path.read_bytes()
    if hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()!=ORIGINAL_TEST_BLOB:raise ValueError("Pinned original test git blob mismatch")
    identity=source_identity(json.loads(raw),rows)
    save_json(OUTPUT/"source_identity.json",identity)
    labels=[];ledger=[];images={};groups=Counter();input_tmp=OUTPUT/"model_inputs.jsonl.tmp"
    OUTPUT.mkdir(parents=True,exist_ok=True)
    with input_tmp.open("w") as stream:
        for index,row in enumerate(rows):
            raw=row["image"]["bytes"];h=sha(raw);mime,suffix=image_mime(raw);image_path=OUTPUT/"images"/(h+suffix)
            if h not in images:
                save(image_path,raw)
                with Image.open(io.BytesIO(raw)) as image:image.verify()
                with Image.open(io.BytesIO(raw)) as image:width,height=image.size;mode=image.mode
                images[h]={"path":str(image_path.relative_to(ROOT)),"sha256":h,"bytes":len(raw),"mime_type":mime,"width":width,"height":height,"mode":mode,"image_bytes_modified":False}
            case=model_case(index,row);stream.write(json.dumps(case,ensure_ascii=False)+"\n")
            answer=row["answer"]
            if not isinstance(answer,str) or not answer:raise ValueError("Missing released answer")
            group="CLOSED" if answer in {"yes","no"} else "OPEN";groups[group]+=1
            labels.append({"task":"V03","case_id":case["case_id"],"variant":VARIANT,"split":case["split"],"target_answer":answer,"answer_type":group,"image_sha256":h})
            ledger.append({"case_id":case["case_id"],"publisher_parquet":row["_parquet"],"publisher_row_index":row["_row"],"publisher_image_path":row["image"]["path"],"image_sha256":h,"image_path":images[h]["path"],"question_utf8_sha256":sha(row["question"].encode())})
    target=OUTPUT/"model_inputs.jsonl"
    if target.exists():
        if file_sha(target)!=file_sha(input_tmp):raise ValueError("Prepared full input file changed")
        input_tmp.unlink()
    else:input_tmp.replace(target)
    for name,value in [("labels.jsonl",labels),("input_provenance.jsonl",ledger)]:save(OUTPUT/name,"".join(json.dumps(r,ensure_ascii=False)+"\n" for r in value).encode())
    save_json(OUTPUT/"image_manifest.json",list(images.values()))
    save_json(OUTPUT/"ordered_case_ids.json",[r["case_id"] for r in labels])
    metric_sources=scoring_sources()
    report={"task_id":"V03","status":"prepared_full_pinned_publisher_mirror_test","inference_dispatched":False,
        "variant":VARIANT,"cases":len(rows),"unique_images":len(images),"answer_groups":dict(groups),
        "source_revision":HF_REVISION,"original_source_revision":ORIGINAL_REVISION,"original_test_git_blob_sha1":ORIGINAL_TEST_BLOB,
        "source_identity":identity,"sources":sources,"source_chain":source_chain(),"native_scoring_source_revision":LLAVA_REVISION,"native_scoring_files":metric_sources,
        "input_file":str(target.relative_to(ROOT)),"label_file":str((OUTPUT/"labels.jsonl").relative_to(ROOT)),
        "image_manifest":str((OUTPUT/"image_manifest.json").relative_to(ROOT)),
        "model_facing_fields":["released_question_text","released_original_image_bytes"],"input_modalities":["image","question_text"],
        "scorer_only_fields":["target_answer","answer_type"],
        "prompt_policy":"Exact pinned mirror question and original embedded image bytes only. No answer-group hint, caption, answer candidates, labels or system message. No source row removed, modified or selected by model outcomes.",
        "metric_policy":{"open_headline":"Pinned official LLaVA-Med normalize_word and calculate_f1score recall, macro per OPEN case; do not substitute generic multiset recall.",
            "closed_headline":"Declared corrected source substring accuracy with every CLOSED case in denominator; native PathVQA-specific bug-compatible score separately reported with its defective denominator. Strict normalized exact Yes/No accuracy is a separate diagnostic.",
            "native_cli_blockers":["run_eval_pvqa.py omits wrong opposite-label predictions from closed denominator","run_eval_pvqa.py calls calculate_appearance_with_normalization with2arguments but pinned helper requires3; no full native CLI success claim"],
            "missing_output_policy":"Keep every frozen case in corrected group denominators; missing/empty outputs score0. Report failures and truncations. Native bug-compatible diagnostic retains source omission behavior and cannot be treated as unbiased accuracy.",
            "no_combined_metric":True},
        "comparison_to_paper":"Full released6719-row deduplicated/normalized mirror test, with full questions and images; source native6761 questions differ by42 duplicate rows and text normalization. Model is a zero-shot Qwen vision baseline against task-trained source systems. Compare only metric/split-compatible results with this explicit caveat; no exact paper reproduction or contamination-free claim.",
        "interpretation":{"task_demands":{"labels":["visual_evidence_interpretation","pathology_knowledge","question_answering"],"status":"provisional analyst description; model internal computation unknown"},"actually_supplied":"Released question text and image bytes only","reference_answer_source":"Source pathology textbook/PEIR-derived curated question-answer annotations, mirror-normalized, scorer-only","good_score_establishes":"Reference answer recovery under this declared vision and lexical scoring protocol","bad_score_establishes":"Limited reference answer recovery; does not isolate reasoning or establish clinical utility","explanation_correctness":"Unassessed independently of answers; unsupported explanation is not automatically false"},
        "files":[{"path":str(p.relative_to(ROOT)),"sha256":file_sha(p),"bytes":p.stat().st_size} for p in sorted(OUTPUT.iterdir()) if p.is_file()]}
    save_json(ROOT/"reports/pathvqa_native_preparation.json",report)
    print(json.dumps({k:report[k] for k in ["task_id","status","cases","unique_images","answer_groups","input_file"]}))
    return report


if __name__=="__main__":prepare()
