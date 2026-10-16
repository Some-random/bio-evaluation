#!/usr/bin/env python3
"""Render the reviewed evaluation overview from its aggregate metadata snapshot.

No inference, scoring, benchmark payload loading, or changes to run artifacts.
The snapshot retains the source hashes and timestamps from the reviewed export.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "reports"


def text(value):
    return re.sub(r"\s+", " ", str(value or "")).strip()


def cell(value):
    return text(value).replace("|", "\\|")


def anchor(value):
    return re.sub(r"\s+", "-", re.sub(r"[^\w\- ]", "", value.lower()))


def label(group):
    suffix = "*" if group["status"] != "Results available" else ""
    return group["task"] + suffix


def categories(data):
    return [category["name"] for category in data["categories"]]


def groups_for(data, category, kind="main"):
    return [group for group in data["groups"] if group["category"] == category and group["kind"] == kind]


def source_links(group):
    return ", ".join(f"[Source {index + 1}]({url})" for index, url in enumerate(group["sourceUrls"]))


def validate(data):
    groups = data["groups"]
    ids = [task_id for group in groups for task_id in group["taskIds"]]
    assert len(groups) == 76
    assert sum(group["kind"] == "main" for group in groups) == 67
    assert sum(group["kind"] == "diagnostic" for group in groups) == 9
    assert len(ids) == len(set(ids)) == 64
    assert sum(len(group["results"]) for group in groups) == 28
    assert sum(category["count"] for category in data["categories"]) == 67
    assert "Protein design" in categories(data)
    assert sum(run["planned"] for run in data["runs"]) == data["meta"]["plannedCases"]
    assert sum(run["completed"] for run in data["runs"]) == data["meta"]["savedResponses"]


def snapshot_note(data):
    meta = data["meta"]
    return (
        f"Stored scores: **{meta['scoreSnapshotAt']}**. Running-work snapshot: "
        f"**{meta['runSnapshotAt']}**. These are timestamped reports, not a live feed."
    )


def overview(data):
    meta = data["meta"]
    names = {
        "P02": "Binary protein localization", "P03": "Ten-compartment protein localization",
        "P05": "AAV variant fitness prediction", "P06": "Protein thermostability prediction",
        "P10": "Human protein–protein interaction prediction", "P11": "Yeast protein–protein interaction prediction",
        "P12": "Enzyme Commission annotation", "P13": "Gene Ontology: biological process",
        "P14": "Gene Ontology: molecular function", "P15": "Gene Ontology: cellular component",
        "P19": "Single-mutant generation", "P20": "Multi-mutant ranking without measurements",
        "P21": "Mutation ranking with anchor measurements", "P22": "Mutation ranking with single-mutant measurements",
        "P23": "Protein function description generation", "P24": "Catalytic activity description generation",
        "P25": "Protein domain and motif description generation", "P26": "Protein functional description generation",
        "P31": "Mutation engineering with a supplied position", "P32": "Mutation engineering with an unknown position",
        "B01": "Literature evidence question answering", "B02": "Biological database question answering",
        "B03": "Supplementary-material question answering", "B04": "Research figure question answering",
        "B05": "Research table question answering", "B06": "Experimental protocol question answering",
        "B07": "Biological sequence question answering", "B08": "Molecular cloning question answering",
        "V01": "Radiology image question answering", "V02": "Medical image question answering in English",
        "V03": "Pathology image question answering", "V04": "Medical image question answering",
        "N02": "Coding-variant effect prediction", "N03": "Non-SNV variant effect prediction",
        "P35": "Protein retrieval from functional descriptions",
        "P44": "Evidence support for protein-function explanations",
        "P34": "Protein-sequence optimization against fitness predictors",
        "P36": "Text-conditioned protein-sequence design",
        "P37": "Unconditional protein generation",
        "P38": "Protein generation for predicted stability and solubility",
        "P39": "Heme-binding protein candidate generation",
        "P42": "GFP sequence optimization against a fluorescence predictor",
        "V07": "Scientific document and figure extraction",
    }
    caveats = {
        "P34": "Predictor-scored optimization; not measured laboratory success.",
        "P36": "Qualitative designs; no measured design-success rate.",
        "P37": "Structure quality is predicted; function is not experimentally established.",
        "P38": "Stability and solubility are predicted, not measured.",
        "P39": "Heme binding is a predicted candidate property, not demonstrated binding.",
        "P42": "Scored by a fluorescence predictor; not a wet-lab result.",
    }
    statuses = {
        "Results available": "Finished", "Partial": "Partial", "Running / queued": "Running or queued",
        "Source-blocked": "Blocked", "Deferred / held": "On hold",
        "Status unverified": "Run status unconfirmed",
    }

    def display_status(group, protocol):
        value = protocol["status"] if protocol else group["status"]
        if value == "Status unverified" and group["scope"] == "Catalog only":
            return "Listed for consideration"
        return statuses[value]

    def snapshot(value):
        return value[:10] + " " + value[11:16] + " UTC"

    out = [
        "# Biological evaluation overview", "",
        "Model: **Qwen3.8-27B**.", "",
        f"Scores: **{snapshot(meta['scoreSnapshotAt'])}** · Run status: **{snapshot(meta['runSnapshotAt'])}**.", "",
        f"**{meta['completedSettings']} of {meta['registrySettings']} evaluation settings have finished runs.** "
        "An asterisk (*) marks incomplete coverage or scoring.", "",
        "**Listed for consideration** means additional datasets outside the original 64-setting list. "
        "**Run status unconfirmed** means no verified completion record. Published scores are reference results; "
        "full protocol notes are expandable below.", "",
    ]
    for category in categories(data):
        entries = [group for group in data["groups"] if group["category"] == category]
        out += [f"## {category}", "", "| Task | Dataset/protocol | Status | Qwen result | Published reference |",
            "|---|---|---|---|---|"]
        for group in entries:
            for protocol in group["protocols"] or [None]:
                task_id = protocol["taskId"] if protocol else None
                rows = [row for row in group["results"] if row["taskId"] == task_id] if protocol else []
                for result in rows or [None]:
                    name = names.get(task_id, group["task"])
                    if not protocol and group["dataset"].startswith("Prompteina"):
                        name = "GM2A-targeted binder design"
                    elif not protocol and group["dataset"].startswith("Proteo-R1 internal"):
                        name = "Structure-derived questions and output-format checks"
                    state = display_status(group, protocol)
                    if (protocol and state != "Finished") or (result and result["incomplete"]):
                        name += "*"
                    caveat = caveats.get(task_id)
                    if group["dataset"].startswith("Prompteina"):
                        caveat = "Single published target campaign."
                    elif group["dataset"].startswith("Proteo-R1 internal"):
                        caveat = "Independent held-out questions remain unresolved."
                    if caveat:
                        name += "<br>" + caveat
                    dataset = group["dataset"]
                    if protocol and len(group["protocols"]) > 1:
                        dataset += "<br>" + protocol["title"]
                    if result and len(rows) > 1:
                        dataset += "<br>" + result["title"]
                    local = result["metricText"] if result else "—"
                    if result and result["completionScope"] == "diagnostic_only_primary_metrics_invalid":
                        local = "**Diagnostic only:** " + local + "<br>Full native primary metric undefined."
                    published = result["publishedText"] if result else group["literatureText"]
                    if result and result["publishedUrl"]:
                        published += f" · [source]({result['publishedUrl']})"
                    elif group["sourceUrl"]:
                        published += f" · [source]({group['sourceUrl']})"
                    out.append("| " + " | ".join(cell(value) for value in [name, dataset, state, local, published]) + " |")
        out += ["", "<details>", "<summary>Protocols, qualifications and complete source records</summary>", ""]
        for group in entries:
            out += [f"**{group['dataset']}**", ""]
            for note in group["notes"]:
                if not note.startswith(("Catalog coverage only;", "Case study or diagnostic; kept separate")):
                    out += [text(note), ""]
            if group.get("sourceSize"):
                out += ["Published source size/units: " + text(group["sourceSize"]), ""]
            for protocol in group["protocols"]:
                out += [f"**{names.get(protocol['taskId'], group['task'])}:** "
                    f"{text(protocol.get('nativeMetric'))}. {text(protocol.get('nativeSplit'))}", ""]
                if protocol.get("limitation"):
                    out += [text(protocol["limitation"]), ""]
                if protocol.get("blocker"):
                    out += [text(protocol["blocker"]), ""]
            for result in group["results"]:
                out += result_details(result)
            if not group["results"]:
                out += ["Published reference record: " + text(group["literatureText"]), ""]
            out += [source_links(group), ""]
        out += ["</details>", ""]
    out += [f"[Raw run artifacts and uploaded trajectories]({meta['githubUrl']}/tree/main/results/runs)", ""]
    return "\n".join(out)


def inventory_detail(group):
    out = [
        f"### {label(group)}", "", f"**Dataset/protocol:** {group['dataset']}", "",
        f"**Scope:** {group['scope']} · **Execution:** {group['status']}", "",
    ]
    if group["protocols"]:
        out += ["| Registered scientific setting | Execution status |", "|---|---|"]
        for protocol in group["protocols"]:
            suffix = "*" if protocol["status"] != "Results available" else ""
            out.append(f"| {cell(protocol['title'])}{suffix} | {cell(protocol['status'])} |")
        out.append("")
    out += ["<details>", "<summary>Scope, source protocols and published evidence</summary>", ""]
    if group.get("sourceSize"):
        out += [f"**Source size/units:** {text(group['sourceSize'])}", ""]
    if group.get("inputInterface"):
        out += [f"**Input interface:** {text(group['inputInterface'])}", ""]
    if group.get("evidenceType"):
        out += [f"**Reference evidence:** {text(group['evidenceType'])}", ""]
    if group.get("trainingRegime"):
        out += [f"**Published training/inference regime:** {text(group['trainingRegime'])}", ""]
    out += [f"**Published evidence — not a local result:** {text(group['literatureText'])}", ""]
    for note in group["notes"]:
        out += [text(note), ""]
    for protocol in group["protocols"]:
        out += [f"**{protocol['title']}**", ""]
        for title, key in [("Scientific question", "scientificQuestion"), ("Native metric", "nativeMetric"), ("Source split", "nativeSplit"), ("Qualification", "limitation"), ("Documented blocker", "blocker")]:
            if protocol.get(key):
                out += [f"{title}: {text(protocol[key])}", ""]
        if protocol.get("evidenceUrl"):
            out += [f"[Blocker evidence]({protocol['evidenceUrl']})", ""]
    out += [source_links(group), "", "</details>", ""]
    return out


def complete_inventory(data):
    meta = data["meta"]
    out = [
        "# Complete biological evaluation hierarchy", "",
        "[Overview](EVALUATION_OVERVIEW.md) · [Grouped results](RESULTS_GROUPED.md) · [Coverage crosswalk](TASK_COVERAGE_MAP.csv)", "",
        f"All **{meta['masterGroups']} main dataset/protocol groups** and **{meta['diagnosticGroups']} case/diagnostic groups** are retained. "
        "Hierarchy: **capability → scientific task → dataset/protocol → scope and execution**. "
        "Registry identifiers appear in the crosswalk and provenance JSON rather than human task names.", "",
        snapshot_note(data), "",
        "**\\*** marks an incomplete group or setting. Registered scope and current execution status are separate; "
        "catalog presence does not imply authorization. Mixed groups show each registered protocol separately. "
        "Status unverified is not a claim that a task was never run.", "",
    ]
    for category in categories(data):
        out += [f"## {category}", ""]
        for group in groups_for(data, category):
            out += inventory_detail(group)
    out += ["## Case studies and diagnostics", "",
        "These nine groups retain their scientific parent category but are not promoted to independent benchmark test sets. "
        "The internal structural/alignment diagnostic remains separate until an independent held-out manifest is resolved.", ""]
    for category in categories(data):
        entries = groups_for(data, category, "diagnostic")
        if entries:
            out += [f"### {category} — diagnostic appendix", ""]
            for group in entries:
                detail = inventory_detail(group)
                detail[0] = "#" + detail[0]
                out += detail
    return "\n".join(out)


def result_details(result):
    out = ["<details>", f"<summary>{result['title']}: protocol, counts and complete metric record</summary>", "",
        f"**Native/local protocol:** `{result['protocol']}`", "",
        f"**Coverage:** {result['caseScope']}; {result['completionScope']}.", "",
        "**Saved count record:**", "", "```json", json.dumps(result["counts"], ensure_ascii=False, indent=2), "```", "",
        "**Complete stored metrics, including alternate/diagnostic values:**", "", "```json", json.dumps(result["metrics"], ensure_ascii=False, indent=2), "```", ""]
    if result.get("comparison"):
        out += [f"**Comparison qualification:** {result['comparison']}", ""]
    for caveat in result["caveats"]:
        out += [text(caveat), ""]
    out += ["**All stored published-reference records — separate from the local run:**", "", "```json", json.dumps(result["publishedReferences"], ensure_ascii=False, indent=2), "```", "",
        f"[Original score artifact]({result['sourceUrl']})", "", "</details>", ""]
    return out


def result_section(group, results, diagnostic=False):
    out = [f"### {group['task']}{'*' if diagnostic or any(row['incomplete'] for row in results) else ''}", "",
        f"**Dataset/protocol:** {group['dataset']}", ""]
    if diagnostic:
        out += ["**Finished diagnostic only:** the full native primary metric is undefined. "
            "The parsed-only value below does not complete the benchmark or replace the native metric.", ""]
    out += ["| Scientific setting | Local stored result | Published reference — different protocol |", "|---|---|---|"]
    for result in results:
        suffix = "*" if result["incomplete"] else ""
        reference = cell(result["publishedText"])
        if result["publishedUrl"]:
            reference += f" · [source]({result['publishedUrl']})"
        out.append(f"| {cell(result['title'])}{suffix} | {cell(result['metricText'])} | {reference} |")
    out.append("")
    for note in group["notes"]:
        out += [text(note), ""]
    for result in results:
        out += result_details(result)
    return out


def grouped_results(data):
    out = ["# Biological evaluation results by scientific capability", "",
        "[Overview](EVALUATION_OVERVIEW.md) · [Complete inventory](TASK_HIERARCHY_COMPLETE.md) · [Coverage crosswalk](TASK_COVERAGE_MAP.csv)", "",
        snapshot_note(data), "",
        "Only existing stored local outcomes are shown. The category order matches the complete inventory. "
        "**\\*** marks incomplete coverage or scoring; count records are in expandable details. "
        "Undefined values remain undefined. Published values are separate contextual comparisons, not matched replications, "
        "pooled scores or claims of superiority. All reference records and alternate metric values are retained in the details.", "",
        "A declared run may be complete despite invalid answers when its native scorer explicitly counts invalid answers in the denominator. "
        "That is different from an undefined native primary metric; finished runs with undefined primary metrics are labeled diagnostics separately below.", ""]
    for category in categories(data):
        out += [f"## {category}", ""]
        has_result = False
        for group in groups_for(data, category):
            results = [row for row in group["results"] if row["completionScope"] != "diagnostic_only_primary_metrics_invalid"]
            if results:
                has_result = True
                out += result_section(group, results)
            for result in group["results"]:
                if result["completionScope"] == "diagnostic_only_primary_metrics_invalid":
                    out += result_section(group, [result], diagnostic=True)
        if not has_result:
            out += ["No completed local result in this stored score snapshot. "
                "[The inventory](TASK_HIERARCHY_COMPLETE.md) retains running, blocked, held and unverified protocols.", ""]
    out += ["## Case studies and diagnostics", "",
        "Case studies, predictor-scored optimization, component tests and internal diagnostics remain separate from independent main benchmarks.", ""]
    for category in categories(data):
        entries = groups_for(data, category, "diagnostic")
        if not entries:
            continue
        out += [f"### {category} — diagnostic appendix", ""]
        for group in entries:
            if group["results"]:
                detail = result_section(group, group["results"])
                detail[0] = "#" + detail[0]
                out += detail
            else:
                out += [f"#### {label(group)}", "", f"**Dataset/protocol:** {group['dataset']}", "",
                    f"**Scope:** {group['scope']} · **Execution:** {group['status']}. No local result is shown in this snapshot.", "",
                    f"**Published evidence only:** {text(group['literatureText'])}", ""]
                for note in group["notes"]:
                    out += [text(note), ""]
                out += [source_links(group), ""]
    return "\n".join(out)


def coverage_csv(data):
    output = io.StringIO(newline="")
    writer = csv.writer(output, lineterminator="\n")
    writer.writerow(["Group", "Kind", "Category", "Scientific task", "Dataset / protocol", "Registry ID", "Scope", "Execution status", "Evidence URL"])
    for group in data["groups"]:
        for task_id in group["taskIds"] or [""]:
            protocol = next((item for item in group["protocols"] if item["taskId"] == task_id), None)
            result = next((item for item in group["results"] if item["taskId"] == task_id), None)
            status = protocol["status"] if protocol else group["status"]
            evidence = result["sourceUrl"] if result else protocol.get("evidenceUrl") if protocol else None
            evidence = evidence or group["sourceUrl"]
            writer.writerow([group["id"], group["kind"], group["category"], group["task"], group["dataset"], task_id, group["scope"], status, evidence])
    return output.getvalue()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check outputs match the stored JSON, without writing.")
    args = parser.parse_args()
    path = REPORTS / "TASK_HIERARCHY_DATA.json"
    data = json.loads(path.read_text())
    validate(data)
    outputs = {
        "EVALUATION_OVERVIEW.md": overview(data),
        "TASK_HIERARCHY_COMPLETE.md": complete_inventory(data),
        "RESULTS_GROUPED.md": grouped_results(data),
        "TASK_COVERAGE_MAP.csv": coverage_csv(data),
    }
    for name, content in outputs.items():
        target = REPORTS / name
        if args.check:
            assert target.exists() and target.read_text() == content, f"Output differs: {name}"
        else:
            target.write_text(content)
    print(json.dumps({"checked" if args.check else "written": list(outputs), "main_groups": 67,
        "diagnostic_groups": 9, "registry_ids": 64, "local_result_rows": 28,
        "source_snapshot_sha256": hashlib.sha256(path.read_bytes()).hexdigest()}))


if __name__ == "__main__":
    main()
