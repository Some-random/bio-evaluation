#!/usr/bin/env python3
"""Render the reviewed evaluation overview from its aggregate metadata snapshot.

No inference, scoring, benchmark payload loading, or changes to run artifacts.
The snapshot retains the source hashes and timestamps from the reviewed export.
"""
from __future__ import annotations

import argparse
import csv
from datetime import datetime
import hashlib
import html
import io
import json
from pathlib import Path
import re
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "reports"
PACIFIC = ZoneInfo("America/Los_Angeles")


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
    assert sum(len(group["results"]) for group in groups) == data["meta"].get("localResultRows", 28)
    assert sum(category["count"] for category in data["categories"]) == 67
    assert "Protein design" in categories(data)
    assert sum(run["planned"] for run in data["runs"]) == data["meta"]["plannedCases"]
    if data["meta"]["savedResponses"] is not None:
        assert sum(run["completed"] for run in data["runs"]) == data["meta"]["savedResponses"]
    else:
        assert all(run["completed"] is None for run in data["runs"])
    if "uploadedResponses" in data["meta"]:
        assert sum(run["uploaded"] for run in data["runs"]) == data["meta"]["uploadedResponses"]


def snapshot_note(data):
    meta = data["meta"]
    return (
        f"Stored scores: **{pacific_time(meta['scoreSnapshotAt'])}**. Running-work snapshot: "
        f"**{pacific_time(meta['runSnapshotAt'])}**. Display times use Pacific time."
    )


def pacific_time(value):
    if not value:
        return "unavailable"
    moment = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if moment.tzinfo is None:
        raise ValueError("A displayed timestamp must include its source timezone")
    return moment.astimezone(PACIFIC).strftime("%Y-%m-%d %H:%M %Z")


def scientific_requirements(group, protocol):
    task_id = protocol["taskId"] if protocol else None
    inputs = {
        "B01": "Text question and choices", "B02": "Database question and choices",
        "B03": "Question with the source paper's title and DOI",
        "B04": "Scientific figure image and question", "B05": "Scientific table image and question",
        "B06": "Protocol text and question", "B07": "Biological sequence and requested operation",
        "B08": "Cloning scenario and sequence constraints",
        "V01": "Radiology image and question", "V02": "Medical image and English question",
        "V03": "Pathology image and question", "V04": "Medical image and question",
        "P19": "Protein sequence and objective; propose single mutations",
        "P20": "Protein variants and objective; rank without measured outcomes",
        "P21": "Measured anchor mutation plus candidate combinations",
        "P22": "Measured single mutations plus candidate combinations",
        "P31": "Protein sequence, desired effect and mutation position",
        "P32": "Protein sequence and desired effect; propose mutation positions and residues",
        "P35": "Functional description and a searchable protein representation corpus",
        "P36": "Functional description → amino-acid sequence",
        "P37": "Generated protein sequences; OmegaFold structural-confidence evaluation",
        "P38": "Property-conditioned sequences and independent property predictors",
        "P39": "Heme-related description; candidate sequences and complex screening",
        "P42": "GFP sequence edits; fixed fluorescence predictor for evaluation",
        "P44": "Protein-function claim and supporting evidence",
        "V07": "Scientific document pages, figures and extraction targets",
    }
    structural = {
        "main-38": "Backbone coordinates → amino-acid sequence; coordinate-conditioned design",
        "main-39": "Backbone coordinates → sequence; AlphaFold2 refolding evaluation",
        "main-40": "Length/constraints → 3D backbone; ProteinMPNN and ESMFold evaluation",
        "main-41": "Generated sequences; AlphaFold2 structural-confidence evaluation",
        "main-42": "Sequence and 3D coordinates; folding and structural comparison",
        "main-43": "Motif coordinates → scaffold; ProteinMPNN, ESMFold and structural comparison",
        "main-44": "Motif coordinates → scaffold; native structural evaluator",
        "main-50": "Protein sequence → 3D coordinates; folding model and structural comparison",
    }
    return inputs.get(task_id) or structural.get(group["id"]) or text(group.get("inputInterface")) or "See the source-defined input and metric below"


def quoted_record(value):
    # Escape trailing spaces as entities so Git's whitespace check does not
    # reject verbatim source text that legitimately includes them.
    def escaped(line):
        return html.escape(line.rstrip(" "), quote=False) + "&#32;" * (len(line) - len(line.rstrip(" ")))
    return ["> " + escaped(line) if line else ">" for line in value.strip().splitlines()]


def example_records():
    good = json.loads((REPORTS / "ADVISOR_GOOD_EXAMPLES.json").read_text())["examples"]
    tool_cases = json.loads((REPORTS / "TOOL_REQUIRED_CASES.json").read_text())["cases"]
    return good, tool_cases


def main_example(examples):
    selected = [example for example in examples if example.get("main_example")]
    assert len(selected) == 1, "Select exactly one main example of each kind"
    return selected[0]


def example_question(example):
    return example["question_and_options_exact"].split("Question: ", 1)[1].split("\n\nOptions:", 1)[0].strip()


def example_images(example, title):
    out = []
    for source_image in example["images"]:
        path = source_image["report_asset_path"]
        assert not Path(path).is_absolute() and ".." not in Path(path).parts
        out += [f'<img src="{html.escape(path, quote=True)}" alt="{html.escape(title, quote=True)}" width="600">', ""]
    return out


def example_dataset(example):
    default = {"B01": "LAB-Bench LitQA2", "B04": "LAB-Bench FigQA", "B05": "LAB-Bench TableQA"}
    name = example.get("dataset_name") or default[example["task_id"]]
    url = example.get("dataset_url") or "https://github.com/Future-House/LAB-Bench"
    return f"[{name}]({url})"


def highlight_amino_acid(sequence, position):
    assert 1 <= position <= len(sequence)
    return sequence[:position - 1] + "**" + sequence[position - 1] + "**" + sequence[position:]


def bioemu_description():
    return ("BioEmu is an AI model that takes a protein sequence and generates many possible three-dimensional shapes. "
        "It approximates the mixture of shapes a protein adopts, which would otherwise be expensive to explore "
        "with molecular simulations. These samples can be used to estimate how often the protein stays folded.")


def advisor_examples():
    good, tool_cases = example_records()
    example = main_example(good)
    assert example["local_score_record"]["correct"]
    assert example["local_score_record"]["answer"] == example["native_gold"]["target_choice"]
    title = example.get("main_title", "Interpret biological evidence")
    out = ["## Worked examples", "", f"### Good result: {title}", "",
        f"**Evaluation dataset:** {example_dataset(example)}.", "",
        f"**Question:** {example.get('plain_question', example_question(example))}", ""]
    if example.get("plain_context"):
        out += [example["plain_context"], ""]
    if example.get("main_choices"):
        out += ["**Answer choices:** " + "; ".join(example["main_choices"]) + ".", ""]
    out += example_images(example, title)
    reasoning = example["model_reasoning_text_exact"]
    out += [f"**Qwen's answer:** {example['main_answer']}", "",
        f"**Saved model reasoning (verbatim, {len(reasoning.split())} words):**", ""] + quoted_record(reasoning) + [""]
    if example.get("companion_notes"):
        out += ["**Checks on the saved reasoning:**", ""] + [f"- {note}" for note in example["companion_notes"]] + [""]
    result = example["dataset_result"]
    out += [f"The answer matches the reference label. Dataset accuracy: "
        f"**{100 * result['accuracy']:.1f}%** ({result['correct']}/{result['total']}).", ""]

    example = main_example(tool_cases)
    original = example["input_sequences"]["wild_type"]
    assert len(original["sequence"]) == original["length"]
    out += ["### Tool-use challenge: does one change make a protein less stable?", "",
        f"**Category:** [{example['catalog_category']}](#{anchor(example['catalog_category'])}) "
        f"→ {example['catalog_family']}.", "",
        f"**Evaluation dataset:** [BioEmu folding-free-energy benchmark]({example['source_url']}) "
        "— protein stability.", "",
        "**Question:** Given the protein below, replace amino acid 6 from **Q** to **C**. "
        "Does it become less stable, and by how much?", "",
        highlight_amino_acid(original["sequence"], 6), "",
        "**Reference answer (experiment):** Yes—less stable, with a change of about "
        f"**{example['experimental_reference']['mutant_ddg_exp']:+.2f} kcal/mol** in folding free energy.", "",
        "**What is BioEmu?** " + bioemu_description(), "",
        "**How the published BioEmu workflow gets to a one-number answer:**", "",
        "1. Find related sequences and compute AlphaFold2 representations of the original and changed proteins.",
        "2. Use BioEmu to sample possible shapes; the benchmark recommends **5,000 per protein**.",
        "3. Compare them with the supplied benchmark reference structure to estimate how often each protein is folded, then calculate its folding free energy.",
        "4. Subtract the two energies to predict the stability change.", "",
        "Evaluation compares the predicted number with the experimental reference. "
        "The question and answer are simple; producing a supported prediction involves substantial intermediate computation.", "",
        "[More worked examples, complete saved reasoning, exact inputs and tool details](WORKED_EXAMPLES.md)", ""]
    return out


def worked_examples():
    good, tool_cases = example_records()
    out = ["# Worked examples and tool workflows", "",
        "[Back to the task map](EVALUATION_OVERVIEW.md)", "",
        "The overview keeps one correct answer and one tool-use challenge. This document retains the full examples and saved reasoning. "
        "Correct answers do not independently validate every step of a model's explanation. "
        "Tool workflows below are source-backed examples, not measured Qwen failures.", "",
        "## Correct answers from saved Qwen runs", ""]
    titles = {"B01": "Biological knowledge and literature question answering",
        "B04": "Reading a biological figure", "B05": "Comparing values in a scientific table"}
    for example in sorted(good, key=lambda item: not item.get("main_example", False)):
        score = example["local_score_record"]
        assert score["correct"] and score["answer"] == example["native_gold"]["target_choice"]
        out += [f"### {example_question(example)}", "",
            f"**Evaluation dataset:** {example_dataset(example)}.", "",
            f"**Task:** {titles[example['task_id']]} ({example['task_id']}). "
            f"**Case:** `{example['case_id']}`.", "",
            "**Exact question and choices:**", ""] + quoted_record(example["question_and_options_exact"]) + [""]
        out += example_images(example, titles[example["task_id"]])
        out += ["**Saved model reasoning, verbatim:**", ""] + quoted_record(example["model_reasoning_text_exact"]) + ["",
            "**Saved final answer, verbatim:**", ""] + quoted_record(example["assistant_final_text_exact"]) + [""]
        result = example["dataset_result"]
        out += [f"Reference choice: **{score['answer']}** — correct. "
            f"Dataset accuracy: **{100 * result['accuracy']:.1f}%** ({result['correct']}/{result['total']}).", ""]
        if example.get("companion_notes"):
            out += ["**Source check:**", ""] + [f"- {note}" for note in example["companion_notes"]] + [""]
    out += ["[Exact example records and source hashes](ADVISOR_GOOD_EXAMPLES.json)", "",
        "[Additional protein-sequence examples and their limitations](EXAMPLES_SEQUENCE_VISION_TOOLS.md)", "",
        "## Simple answer, substantial computation", ""]
    for example in sorted(tool_cases, key=lambda item: not item.get("main_example", False)):
        dataset = re.sub(r" \(catalog main-\d+\)", "", example["dataset"])
        out += [f"### {example['title']}", "", f"**Dataset:** {dataset}", "",
            f"**Input:** {example['input']}", ""]
        if example.get("plain_question"):
            out += [f"**Category:** {example['catalog_category']} → {example['catalog_family']}.", "",
                f"{example['benchmark_context']} [Dataset provenance]({example['benchmark_context_source']})", "",
                "**What is BioEmu?** " + bioemu_description(), "",
                f"**Plain-language question:** {example['plain_question']}", "",
                f"**Reference answer:** {example['plain_answer']}", "",
                f"**Evidence scope:** {example['result_scope']}", ""]
        for name, sequence in example.get("input_sequences", {}).items():
            assert len(sequence["sequence"]) == sequence["length"]
            out += [f"**{name.replace('_', ' ').capitalize()}** (`{sequence['case_id']}`, {sequence['length']} amino acids):", "",
                "```text", sequence["sequence"], "```", ""]
        if example.get("numbering_caveat"):
            out += [example["numbering_caveat"], ""]
        if example.get("input_sequence"):
            sequence = example["input_sequence"]
            assert len(sequence) == example["input_sequence_length"]
            out += ["```text", sequence, "```", ""]
        out += [f"**Required answer:** {example['required_output']}", "",
            f"**What must be computed:** {example['why_text_answer_is_insufficient']}", "",
            f"**Tool route:** {example['tool_route']}", "",
            f"[Native task and evaluation source]({example['source_url']})", ""]
        if example.get("intermediate_steps"):
            out += [f"{index}. {step}" for index, step in enumerate(example["intermediate_steps"], 1)] + [""]
            reference = example["experimental_reference"]
            out += ["The evaluator compares predicted energies with the experimental records. "
                f"For this pair, the released reference energies are {reference['wild_type_dg_exp']:.5f} "
                f"and {reference['mutant_dg_exp']:.5f} kcal/mol; their difference is "
                f"**{reference['display_ddg_exp']} kcal/mol**. "
                "These are reference measurements, not values computed by a run in this repository.", ""]
        if example.get("evidence_files"):
            out += ["**Source code and records:** " + " · ".join(
                f"[{Path(record['path']).name}]({record['url']})" for record in example["evidence_files"]), ""]
        if example.get("case_source_url"):
            out += [f"[Released example input]({example['case_source_url']})", ""]
    out += ["## What AlphaFold contributes", "",
        "AlphaFold predicts a protein's three-dimensional structure from its amino-acid sequence. "
        "In the BioEmu workflow above, AlphaFold2 supplies learned internal representations; BioEmu then samples many conformations. "
        "The final stability estimate requires additional calculations over that ensemble. "
        "A single predicted structure does not itself establish the experimental stability change. "
        f"[BioEmu method]({main_example(tool_cases)['paper_url']})", "",
        "These examples document particular released workflows. They do not show that every possible solver must use AlphaFold, "
        "or that a general-purpose model has been tested successfully as their tool-using controller.", "",
        "[More external-model computations and results reported in the papers](PUBLISHED_TOOL_USE_EXAMPLES.md)", "",
        "[Full tool-case records, revisions and source hashes](TOOL_REQUIRED_CASES.json)", ""]
    return "\n".join(out)


def overview(data):
    meta = data["meta"]
    feasibility = json.loads((REPORTS / "QWEN_TASK_FEASIBILITY.json").read_text())
    assessment_rank = {
        "Runnable now": 0, "Needs data or protocol": 1, "Needs scoring protocol": 1,
        "Needs additional models/tools": 2, "On hold": 3,
    }

    def assessment(group, protocol=None):
        if protocol:
            value = feasibility["task_assessments"][protocol["taskId"]]
        else:
            value = feasibility["group_assessments"][group["id"]]
        assert value["label"] in assessment_rank
        assert value.get("shortReason") and value.get("reason")
        return value

    for group in data["groups"]:
        for protocol in group["protocols"] or [None]:
            assessment(group, protocol)
    task_ids = {protocol["taskId"] for group in data["groups"] for protocol in group["protocols"]}
    extra_ids = {group["id"] for group in data["groups"] if not group["protocols"]}
    assert len(task_ids) == 64 and task_ids == set(feasibility["task_assessments"])
    assert len(extra_ids) == 38 and extra_ids == set(feasibility["group_assessments"])
    assert feasibility["summary"]["runnable_now"] == sum(
        item["label"] == "Runnable now" for item in feasibility["task_assessments"].values())

    def group_rank(group):
        return min(assessment_rank[assessment(group, protocol)["label"]]
            for protocol in group["protocols"] or [None])

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
        "P36": "Lexical sequence overlap; biological function untested.",
        "P37": "Structure quality is predicted; function is not experimentally established.",
        "P38": "Stability and solubility are predicted, not measured.",
        "P39": "Heme binding is a predicted candidate property, not demonstrated binding.",
        "P42": "Scored by a fluorescence predictor; not a wet-lab result.",
    }
    def main_ids(*values):
        return [f"main-{value:02d}" for value in values]

    megatasks = [
        ("Protein traits and interactions", [
            ("Whether proteins dissolve", main_ids(1, 11)),
            ("Where proteins go in a cell", main_ids(2, 12)),
            ("Protein activity, stability and production", main_ids(3, 4, 5, 6, 8, 14)),
            ("Which proteins bind each other", main_ids(7, 10, 13)),
            ("Antibody properties", main_ids(9)),
        ]),
        ("What proteins do", [
            ("Assigning protein functions and enzyme classes", main_ids(15, 18, 20, 21)),
            ("Protein function descriptions", main_ids(16, 17)),
            ("Biochemical reaction classification", main_ids(19)),
            ("Protein retrieval from descriptions", ["diagnostic-01"]),
            ("Evidence support for protein explanations", ["diagnostic-02"]),
        ]),
        ("Effects of protein mutations", [
            ("Explaining mutation effects", main_ids(22)),
            ("Predicting and ranking mutation effects", main_ids(23, 24, 25, 27, 30, 32)),
            ("Choosing mutations to improve a protein", main_ids(26) + ["diagnostic-03"]),
            ("Binding affinity and immune interactions", main_ids(28, 29, 31)),
        ]),
        ("Answering biology research questions", [
            ("Biological research question answering", main_ids(33, 34, 35)),
        ]),
        ("Designing proteins", [
            ("Antibody design", main_ids(36, 37, 45, 46)),
            ("Finding a sequence for a desired shape", main_ids(38, 39)),
            ("Protein sequence and structure generation", main_ids(40, 41, 42) + ["diagnostic-04", "diagnostic-05"]),
            ("Building around a functional protein part", main_ids(43, 44)),
            ("Designing proteins that bind a target", main_ids(47) + ["diagnostic-07"]),
            ("Making fluorescent proteins brighter", ["diagnostic-06"]),
        ]),
        ("Protein shapes and motion", [
            ("Local structure and residue prediction", main_ids(48, 54)),
            ("Protein structure ranking", main_ids(49)),
            ("Protein folding", main_ids(50)),
            ("Protein shape changes, motion and stability", main_ids(51, 52, 53)),
            ("Structure-derived questions and output checks", ["diagnostic-08"]),
        ]),
        ("Understanding biomedical images", [
            ("Biomedical visual question answering", main_ids(55)),
            ("Scientific figures, documents and visual conversations", main_ids(56, 57) + ["diagnostic-09"]),
        ]),
        ("DNA, RNA and small molecules", [
            ("Molecular interactions and binding affinity", main_ids(58, 63, 64, 67)),
            ("Pathway and disease prediction", main_ids(59, 61)),
            ("Variant-effect prediction", main_ids(60)),
            ("Choosing genes using expression data", main_ids(62)),
            ("RNA structure ranking", main_ids(65)),
            ("Small-molecule properties", main_ids(66)),
        ]),
    ]
    group_by_id = {group["id"]: group for group in data["groups"]}
    assigned = [group_id for _, families in megatasks for _, ids in families for group_id in ids]
    assert len(assigned) == len(set(assigned)) == len(group_by_id) == 76
    assert set(assigned) == set(group_by_id)

    out = [
        "# Biological evaluation overview", "",
        "General-purpose baseline: **Qwen3.8-27B**, with text and image inputs.", "",
        "This catalog spans biological prediction, scientific evidence, protein design and three-dimensional structure. "
        "The map below shows **34 task families in 8 categories** without opening the detailed catalog. "
        "The counts are task families, not datasets or individual test questions.", "",
        "## Task map", "",
        "| Category | Number of task families | Tasks | Typical question or output |", "|---|---:|---|---|",
    ]
    typical = [
        "Will this protein dissolve? Where does it go? What does it bind?",
        "What is this protein's function? Which reaction does it carry out?",
        "What happens after changing a protein? Which change works best?",
        "Answer a question using papers, figures, tables, protocols or sequences",
        "Propose a protein sequence or shape that meets specified requirements",
        "What shape does this protein take? How does it move or stay folded?",
        "Answer questions about medical images and scientific figures",
        "Predict genetic effects, gene activity, molecular binding and chemical properties",
    ]
    for (category, families), interface in zip(megatasks, typical):
        out.append("| " + " | ".join(cell(value) for value in [category, len(families),
            "; ".join(family for family, _ in families), interface]) + " |")
    out += [f"| **Total** | **{sum(len(families) for _, families in megatasks)}** | | |", ""] + advisor_examples()
    out += ["## Dataset catalog", "",
        "Each row is one dataset or source-defined evaluation condition. Expand a category for detail. "
        "The input/computation column describes the scientific requirement, including external models where needed.", "",
        "Qwen results and published reference results use the stated protocols and are not automatically matched comparisons. "
        "**—** means no verified Qwen result is displayed; **\\*** marks limited coverage or scoring. "
        "Source qualifications are collected at the end.", ""]
    all_notes = []
    for category, families in megatasks:
        out += [f'<a id="{anchor(category)}"></a>', "", "<details>", f"<summary><h2>{category}</h2></summary>", ""]
        all_notes += [f"## {category}", ""]
        for family, group_ids in sorted(families,
                key=lambda item: min(group_rank(group_by_id[group_id]) for group_id in item[1])):
            entries = [group_by_id[group_id] for group_id in group_ids]
            out += [f"#### {family}", ""]
            table_rows = []
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
                        task_key = name
                        if result and (result["incomplete"] or
                                result["completionScope"] == "diagnostic_only_primary_metrics_invalid"):
                            name += "*"
                        reviewed = assessment(group, protocol)
                        requirement = scientific_requirements(group, protocol)
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
                        table_rows.append({"key": task_key, "task": name, "dataset": dataset,
                            "requirement": requirement, "local": local, "published": published, "caveat": caveat,
                            "rank": assessment_rank[reviewed["label"]]})
            task_order = list(dict.fromkeys(row["key"] for row in table_rows))
            task_order.sort(key=lambda task_key: min(row["rank"] for row in table_rows if row["key"] == task_key))
            table_rows = [row for task_key in task_order for row in sorted(
                [row for row in table_rows if row["key"] == task_key], key=lambda row: row["rank"])]
            out += ["| Task | Dataset/protocol | Input / required computation | Qwen result | Published reference |", "|---|---|---|---|---|"]
            previous_task = None
            for row in table_rows:
                values = [row["dataset"], row["requirement"], row["local"], row["published"]]
                values.insert(0, "" if row["key"] == previous_task else row["task"])
                out.append("| " + " | ".join(cell(value) for value in values) + " |")
                previous_task = row["key"]
            out.append("")
            all_notes += [f"#### {family}", ""]
            for group in entries:
                all_notes += [f"#### {group['dataset']}", ""]
                for note in group["notes"]:
                    if not note.startswith(("Catalog coverage only;", "Case study or diagnostic; kept separate")):
                        all_notes += [text(note), ""]
                if group.get("sourceSize"):
                    all_notes += ["Published source size/units: " + text(group["sourceSize"]), ""]
                for protocol in group["protocols"]:
                    all_notes += [f"**{names.get(protocol['taskId'], group['task'])}:** "
                        f"{text(protocol.get('scientificQuestion'))} "
                        f"Metric: {text(protocol.get('nativeMetric'))}. {text(protocol.get('nativeSplit'))}", ""]
                    if protocol.get("limitation"):
                        all_notes += [text(protocol["limitation"]), ""]
                for result in group["results"]:
                    if result.get("comparison"):
                        all_notes += [f"**Comparison qualification:** {text(result['comparison'])}", ""]
                all_notes += [source_links(group), ""]
        out += ["</details>", ""]
    out += ["<details>", "<summary>Dataset definitions, scientific qualifications and sources</summary>", ""] + all_notes + ["</details>", ""]
    out += [f"Result references updated: **{pacific_time(meta['scoreSnapshotAt'])}**. "
        "Display times use Pacific time (PST/PDT).", ""]
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
        "WORKED_EXAMPLES.md": worked_examples(),
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
        "diagnostic_groups": 9, "registry_ids": 64,
        "local_result_rows": sum(len(group["results"]) for group in data["groups"]),
        "source_snapshot_sha256": hashlib.sha256(path.read_bytes()).hexdigest()}))


if __name__ == "__main__":
    main()
