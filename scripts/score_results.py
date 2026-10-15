"""Score locked outputs using source parsers, grouping and lexical metrics."""
import ast
from collections import Counter, defaultdict
import csv
import importlib.util
import io
import json
import math
from pathlib import Path
import re
import statistics as st
import tarfile

ROOT = Path(__file__).resolve().parents[1]


def module(name,file):
    spec=importlib.util.spec_from_file_location(name,file)
    result=importlib.util.module_from_spec(spec);spec.loader.exec_module(result)
    return result


def load_responses():
    result={}
    for folder in sorted((ROOT/"results/runs").glob("*")):
        for file in (folder/"responses").glob("*.json"):
            row=json.loads(file.read_text());row["run_id"]=folder.name
            result[(row["task"],row["variant"],row["case_id"])]=row
    return result


def lab_answer(text,n):
    constants=ast.parse((ROOT/"sources/chembench_constant.py").read_text())
    pattern=None
    for node in constants.body:
        if isinstance(node,ast.Assign) and any(isinstance(x,ast.Name) and x.id=="MCQ_REGEX_TEMPLATE_1" for x in node.targets):
            pattern=ast.literal_eval(node.value)
    matches=sorted(set(re.findall(pattern,text,re.DOTALL)))
    # Port of pinned ChemBench prepare_mcq_answer, without its optional LLM fallback.
    alphabet=[chr(i) for i in range(65,91)]
    if matches:prepared=str(matches)
    elif text in alphabet:prepared=text
    elif "," in text:
        split=text.split(",");prepared=",".join(split) if all(x.strip() in alphabet for x in split) else ""
    elif " " in text:
        split=text.split(" ");prepared=",".join(split) if all(x.strip() in alphabet for x in split) else ""
    else:prepared=""
    found=re.search("["+"".join(alphabet[:n])+"]",prepared)
    return found.group(0) if found else None


def score_lab(responses):
    path=ROOT/"data/labbench/scorer_references.jsonl"
    if not path.exists():return [],[]
    groups=defaultdict(list);coverage=[]
    for ref in map(json.loads,path.read_text().splitlines()):
        row=responses.get((ref["task"],"NATIVE_PUBLIC_COT",ref["case_id"]))
        completed=bool(row and row.get("status")=="completed")
        answer=lab_answer(row.get("text",""),ref["choice_count"]) if completed else None
        # Official parser failures are incorrect and non-abstaining. Missing
        # provider outputs are disclosed separately instead of being misnamed abstention.
        groups[ref["task"]].append({"correct":answer==ref["target_choice"],
            "sure":answer!=ref["unsure_choice"],"completed":completed,
            "parsed":answer is not None,"provider_status":row.get("status") if row else "not_attempted"})
    metrics=[]
    for task,rows in groups.items():
        total=len(rows);observed=[x for x in rows if x["completed"]]
        correct=sum(x["correct"] for x in observed);sure=sum(x["sure"] for x in observed)
        denominator=len(observed)
        if denominator==0:
            coverage.append({"task_id":task,"protocol_variant":"NATIVE_PUBLIC_COT","planned":total,
                             "statuses":dict(Counter(x["provider_status"] for x in rows)),"completed":0,"parsed":0})
            continue
        suffix="" if denominator==total else "_completed_cases_only"
        for name,value in [("accuracy"+suffix,correct/denominator),("precision"+suffix,correct/sure if sure else 0),
                           ("coverage"+suffix,sure/denominator)]:
            metrics.append({"task_id":task,"protocol_variant":"NATIVE_PUBLIC_COT","model":"gpt-6-luna",
                "metric":name,"value":value,"planned":total,"completed":sum(x["completed"] for x in rows),
                "parsed":sum(x["parsed"] for x in rows),"case_scope":"full public released category" if denominator==total else "INCOMPLETE: completed cases only",
                "comparison_to_paper":"same public task/prompt/scorer; full private paper set unavailable"})
        coverage.append({"task_id":task,"protocol_variant":"NATIVE_PUBLIC_COT","planned":total,
                         "statuses":dict(Counter(x["provider_status"] for x in rows)),
                         "completed":sum(x["completed"] for x in rows),"parsed":sum(x["parsed"] for x in rows)})
    return metrics,coverage


def score_pg(responses):
    prompt=module("pg_prompt",ROOT/"sources/pg__src__prompt.py")
    aggregate=module("pg_aggregate",ROOT/"sources/pg__src__aggregate.py")
    seeds=defaultdict(dict);cells=[];meta={};states=Counter()
    with tarfile.open(ROOT/"sources/proteingym-llm-eval-v1.2.tar.gz") as archive:
        for row in csv.DictReader(io.TextIOWrapper(archive.extractfile("reference/DMS_substitutions.csv"))):
            meta[row["DMS_id"]]={"uniprot_id":row["UniProt_ID"],"function":row.get("coarse_selection_type")}
        names=sorted(x for x in archive.getnames() if re.search(r"/n50_b[123]\.json$",x))
        for name in names:
            episode=json.load(archive.extractfile(name))
            row=responses.get(("P18","NATIVE",name))
            status=row.get("status") if row else "not_attempted"
            state=status;rho=None
            if status=="completed":
                ids=[f"M{i+1:02d}" for i in range(50)]
                ranking=prompt.parse_ranking(row.get("text",""),ids)
                if ranking is None:state="invalid_ranking"
                else:
                    labels=json.load(archive.extractfile(name.replace(".json",".labels.json")))
                    mutants=[(v["id"],v["seq"],labels[v["id"]]) for v in episode["variants"]]
                    rho=prompt.score_ranking(ranking,ids,mutants)
                    seeds[episode["seed"]][episode["assay"]]=rho
                    state="scored"
            states[state]+=1
            cells.append({"task_id":"P18","protocol_variant":"NATIVE","case_id":name,
                          "assay":episode["assay"],"seed":episode["seed"],"state":state,"spearman":rho})
    headline={seed:aggregate.macro_from_assay_rho(scores,meta)[0] for seed,scores in seeds.items()}
    scores=[x for x in headline.values() if x is not None]
    metrics=[]
    if scores:
        for name,value in [("nested_macro_spearman",st.mean(scores)),
                ("seed_standard_error",st.stdev(scores)/math.sqrt(len(scores)) if len(scores)>1 else None)]:
            metrics.append({"task_id":"P18","protocol_variant":"NATIVE","model":"gpt-6-luna",
                "metric":name,"value":value,"planned":651,"completed":sum(r["state"] in ["scored","invalid_ranking"] for r in cells),
                "parsed":states["scored"],"case_scope":"217 assays x 3 seeds; official N=50",
                "comparison_to_paper":"native source parser/metric/seed aggregation; disclose missing and blocked cells"})
    with (ROOT/"results/p18_per_cell.csv").open("w",newline="") as stream:
        writer=csv.DictWriter(stream,fieldnames=list(cells[0]));writer.writeheader();writer.writerows(cells)
    return metrics,[{"task_id":"P18","protocol_variant":"NATIVE","planned":651,"statuses":dict(states),
                     "scored":states["scored"],"per_seed_macro":headline}]


def main():
    responses=load_responses();metrics=[];coverage=[]
    for score in [score_pg,score_lab]:
        m,c=score(responses);metrics.extend(m);coverage.extend(c)
    target=ROOT/"results/metrics_by_task_model_variant.csv"
    fields=["task_id","protocol_variant","model","metric","value","planned","completed","parsed","case_scope","comparison_to_paper"]
    with target.open("w",newline="") as stream:
        writer=csv.DictWriter(stream,fieldnames=fields);writer.writeheader();writer.writerows(metrics)
    (ROOT/"results/coverage_and_failures.json").write_text(json.dumps(coverage,indent=2)+"\n")
    print(json.dumps({"metrics":metrics,"coverage":coverage},ensure_ascii=False))


if __name__=="__main__":main()
