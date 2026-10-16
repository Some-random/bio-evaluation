"""Pinned PMC-VQA clean-test prompt and source TD choice-scoring contract."""
import ast
import base64
import difflib
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/"sources/pmcvqa_native"
OUTPUT=ROOT/"data/pmcvqa_clean_native"
DATA_REVISION="b56ae594f794867893143b337b4118a835794647"
CODE_REVISION="1678ec2c97f0b2bf84591ddccd2e84932630e450"
CSV_SHA="8523073108666b8f5231c3d40004a7b74a57381ea54ec9a3019edf1b33eab8f7"
VARIANT="NATIVE_PMCVQA_CLEAN2000_TD_PROMPT_QWEN_ZERO_SHOT"
MODEL="Qwen/Qwen3.8-27B"
MODEL_REVISION="1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0"
GENERATION={"max_tokens":4096,"temperature":1.0,"top_p":0.95,"top_k":20,"seed":42,"n":1,
            "chat_template_kwargs":{"enable_thinking":True,"reasoning_effort":"medium"}}
NATIVE_FILES={"src__MedVInT_TD__Dataset__PMC_QA_Dataset.py":
              ("src/MedVInT_TD/Dataset/PMC_QA_Dataset.py","0d9ec2d9265a642b5a7561757c846d3837eab047"),
              "src__MedVInT_TD__test.py":("src/MedVInT_TD/test.py","d058c0a61c52c58738c9ae5b4032682770c445d4"),
              "src__MedVInT_TE__test.py":("src/MedVInT_TE/test.py","02ecb3b239d256de4c325af1e536ac2d7240dbef")}


def digest(value):return hashlib.sha256(json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def file_sha(path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""):h.update(chunk)
    return h.hexdigest()


def save_json(path,value):
    path.parent.mkdir(parents=True,exist_ok=True);tmp=path.with_suffix(path.suffix+".tmp")
    tmp.write_text(json.dumps(value,ensure_ascii=False,indent=2)+"\n");tmp.replace(path)


def native_sources():
    result=[]
    for name,(remote,expected) in NATIVE_FILES.items():
        path=SOURCE/name;raw=path.read_bytes()
        if hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()!=expected:raise ValueError("Pinned native source blob changed")
        result.append({"path":str(path.relative_to(ROOT)),"sha256":hashlib.sha256(raw).hexdigest(),
            "publisher_git_blob_sha1":expected,"publisher_digest_verified":True,
            "url":f"https://raw.githubusercontent.com/xiaoman-zhang/PMC-VQA/{CODE_REVISION}/{remote}"})
    return result


_NATIVE=None
def native_scorer():
    global _NATIVE
    native_sources()
    if _NATIVE is None:
        tree=ast.parse((SOURCE/"src__MedVInT_TD__test.py").read_text())
        nodes=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in {"str_similarity","find_most_similar_index"}]
        if len(nodes)!=2:raise ValueError("Native closest-choice scorer definitions unavailable")
        namespace={"difflib":difflib};exec(compile(ast.Module(body=nodes,type_ignores=[]),"pinned_original_PMCVQA_TD_scoring","exec"),namespace)
        _NATIVE=namespace["find_most_similar_index"]
    return _NATIVE


def native_prompt(row):
    """Input-side source Test formatting, without accessing answer/caption fields."""
    question=row["Question"];original=[row["Choice "+letter] for letter in "ABCD"]
    if not isinstance(question,str) or not question or any(not isinstance(c,str) or not c for c in original):raise ValueError("Missing question/choice")
    choices=original.copy();combined=""
    for i,choice in enumerate(original):
        reflect=" "+"ABCD"[i]+":"
        replaced=choice.replace(' A:',reflect).replace(' B:',reflect).replace(' C:',reflect).replace(' D:',reflect)
        for j in range(4):
            if choices[j]==choice:choices[j]=replaced
        combined+=replaced
    return 'Question: '+question+'Choices:'+combined+'The Answer is:',choices


def model_case(index,row,image):
    if not image.startswith(b"\xff\xd8\xff"):raise ValueError("Required original JPEG missing")
    prompt,_=native_prompt(row)
    return {"task":"V05","case_id":f"V05:clean2000:{index:04d}","variant":VARIANT,"split":"test_clean",
        "messages":[{"role":"user","content":[{"type":"text","text":prompt},
            {"type":"image_url","image_url":{"url":"data:image/jpeg;base64,"+base64.b64encode(image).decode()}}]}]}


def native_label(row,choices):
    # The clean release's Answer is the semantic label used by TD; the code's
    # misspelled Anwser field is absent. Keep this schema adapter scorer-only.
    label=row["Answer"]
    for i,choice in enumerate([row["Choice "+l] for l in "ABCD"]):
        if label==choice:
            replacement=" "+"ABCD"[i]+":"
            label=label.replace(' A:',replacement).replace(' B:',replacement).replace(' C:',replacement).replace(' D:',replacement)
    index=native_scorer()(choices,label)
    if index is None or row["Answer_label"] not in "ABCD" or len(row["Answer_label"])!=1:raise ValueError("Native source answer mapping undefined")
    return {"native_target_index":index,"target_label":row["Answer_label"],"target_index":"ABCD".index(row["Answer_label"]),
            "target_answer":label,"native_target_agrees_with_released_label":index=="ABCD".index(row["Answer_label"])}


def strict_label(text):
    if not isinstance(text,str):return None
    # Strict diagnostic: last nonempty line is exactly a label or fixed answer
    # declaration. The native matching score uses the unchanged final content.
    lines=[line.strip() for line in text.strip().splitlines() if line.strip()]
    if not lines:return None
    match=re.fullmatch(r"(?:Final answer\s*:\s*|The answer is\s*:?\s*|Answer\s*:\s*)?\(?([ABCD])\)?[.:]?",lines[-1],re.I)
    return match[1].upper() if match else None


def score_text(text,reference,completed=True):
    text=text if isinstance(text,str) else ""
    usable=completed and bool(text.strip())
    closest=native_scorer();choices=reference["native_choices"]
    # Preserve source generated_texts[i][-1] exactly, including trailing spaces.
    final_character=text[-1] if usable else None
    final_index=closest(choices,final_character) if final_character is not None else None
    full_index=closest(choices,text) if usable else None
    parsed_label=strict_label(text) if usable else None
    return {"native_final_character":final_character,"native_final_character_index":final_index,
        "native_final_character_correct":int(usable and final_index==reference["native_target_index"]),
        "adapted_full_text_index":full_index,"adapted_full_text_native_target_correct":int(usable and full_index==reference["native_target_index"]),
        "adapted_full_text_released_label_correct":int(usable and full_index==reference["target_index"]),
        "strict_final_label":parsed_label,"strict_final_label_correct":int(parsed_label==reference["target_label"]),
        "native_score_defined":usable and final_index is not None,"full_text_score_defined":usable and full_index is not None}


def metric_summary(rows):
    n=len(rows)
    mapping={"native_td_final_character_accuracy":"native_final_character_correct",
             "adapted_full_text_closest_choice_accuracy":"adapted_full_text_native_target_correct",
             "adapted_full_text_released_label_accuracy":"adapted_full_text_released_label_correct",
             "strict_final_label_accuracy":"strict_final_label_correct"}
    return {name:sum(r["parsed_predictions"][field] for r in rows)/n if n else None for name,field in mapping.items()}
