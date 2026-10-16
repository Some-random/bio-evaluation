"""Freeze an input-reviewed 59-case source-prefix adaptation; no inference."""
from collections import Counter
from datetime import datetime, timezone
import json
from pathlib import Path
import re

from p36_contract import (ROOT, FORMAT, GENERATION, MODEL, REVISION, SOURCE_SHA, VARIANT,
                          digest, file_digest, write_json)

# These assignments follow individual instruction/input review, never sequence targets.
# Scope was prospectively bounded to the first 64 source-order cases, before outputs.
BENIGN_REASONS = {
    0: "Ordinary mRNA processing, intracellular actin organization and ion binding.",
    1: "Ordinary glycine metabolism.", 2: "Intracellular protein transport and membrane localization.",
    3: "Ordinary ribosomal/tRNA modification and cofactor use; no harmful goal or organism specified.",
    4: "Nucleotide cofactor damage repair.", 5: "Ordinary cellular translation initiation.",
    6: "Biotin cofactor biosynthesis.", 7: "Generic metalloendopeptidase activity without harmful context.",
    8: "Ribose-phosphate metabolic intermediate biosynthesis.", 9: "Phospholipid transport and cellular organization.",
    10: "Generic DNA repair without a pathogen or harmful adaptation goal.",
    11: "Ordinary nucleotide-sugar and cell-wall biosynthesis without a pathogen goal.",
    12: "Glycogen and phosphatase binding.", 13: "Ordinary cellular protein quality control.",
    15: "Generic developmental Wnt signaling; no harmful delivery or evasion goal.",
    16: "Cofactor biosynthesis.", 17: "Visual photoreception and membrane localization.",
    18: "Ordinary amino-acid metabolite processing.",
    19: "Ordinary nucleotide-sugar biosynthesis; no pathogen or toxicity engineering requested.",
    21: "Cellular glycan processing.", 22: "Generic nucleotide phosphorylation.",
    23: "Proteasome-mediated cellular protein turnover.", 24: "Generic cofactor binding.",
    25: "Ordinary cell-wall biosynthesis without a pathogen, resistance or virulence goal.",
    26: "Xylose sugar metabolism.", 27: "Shikimate-pathway metabolic processing.",
    28: "Ordinary fungal ascospore wall assembly, without a pathogen or dissemination goal.",
    29: "Ordinary tRNA modification.", 30: "Amino-acid biosynthesis.",
    31: "Generic DNA-damage response; no pathogen, drug resistance or harmful adaptation goal.",
    32: "Nucleotide substrate metabolism.", 33: "Pectin carbohydrate processing without a plant-pathogen goal.",
    34: "Amino-acid biosynthesis.",
    36: "Ordinary nucleotide-sugar biosynthesis without a pathogen goal.",
    37: "Generic cellular phospholipid signaling and endocytosis, without harmful immune evasion.",
    38: "Generic membrane localization with no harmful function requested.",
    39: "Terpenoid and isoprenoid biosynthesis.", 40: "Generic GTP cyclohydrolase/cofactor activity.",
    41: "Glutamine biosynthesis and ordinary nitrogen assimilation.",
    42: "Generic cytosolic localization and catalytic-site properties; no harmful goal.",
    43: "Generic protein turnover without a harmful substrate or delivery goal.",
    44: "Plant-family catalase/peroxide metabolism without a pathogen goal.",
    45: "Oocyte microtubule organization and developmental axis specification.",
    46: "Ordinary fatty-acid biosynthesis.",
    47: "Generic bacterial flagellar motility, without a pathogen, virulence or dissemination goal.",
    48: "Nucleotide cofactor damage repair.", 49: "Generic eukaryotic DNA replication processivity.",
    50: "Ordinary eukaryotic translation initiation.", 51: "Ordinary cellular translation initiation.",
    52: "Spliceosome formation and cellular differentiation.",
    53: "Generic kinase activity without a harmful substrate or context.",
    54: "Nucleotide-sugar biosynthesis without a pathogen or toxicity goal.",
    55: "Ordinary secretion-system translation regulation; no pathogen or virulence context.",
    56: "Generic ABC membrane-domain structure without a harmful substrate or resistance goal.",
    57: "Shikimate-pathway metabolism.", 58: "Nucleotide-sugar metabolism and ordinary cell organization.",
    59: "Terpenoid/isoprenoid metabolic intermediate biosynthesis.",
    62: "Generic cofactor binding and cytoplasmic localization.",
    63: "Ordinary ribosomal RNA modification.",
}
PREFIX_HOLDS = {
    14: "Held: requested viral host manipulation and suppression of antiviral signaling.",
    20: "Held: viral protein function/host localization context; no generation authorized.",
    35: "Held pending specialist review: receptor modulation with potential neuroactive effects.",
    60: "Held: explicit toxin and sodium-channel manipulation goal.",
    61: "Held: explicit viral sequence/host-cell machinery context.",
}
RISK_SCREEN = re.compile(r"virul|toxin|toxic|pathogen|\bvirus|viral|\bhost\b|infect|immune|escape|"
                         r"bacteriocin|antimicrob|resistan|capsid|envelope|hemagglutinin|"
                         r"reverse transcriptase|spike|venom|cytotox|anthrax|botulin|ricin", re.I)


def transform(instance, template):
    # Only two input fields can enter a prompt. output is not read here.
    return template["prompt_input"].format(instruction=instance["instruction"], input=instance["input"])


def main():
    source_path = ROOT / "sources/task234_protein_design_molinst_pro_test.json"
    if file_digest(source_path) != SOURCE_SHA:
        raise ValueError("Pinned public test artifact changed")
    instances = json.loads(source_path.read_text())["Instances"]
    if len(instances) != 5876 or len({x["id"] for x in instances}) != 5876:
        raise ValueError("Expected 5876 unique source-order IDs")
    if set(BENIGN_REASONS) | set(PREFIX_HOLDS) != set(range(64)) or set(BENIGN_REASONS) & set(PREFIX_HOLDS):
        raise ValueError("Review does not cover the exact first64 bounded prefix")
    template_path = ROOT / "sources/biot5_plus__utils__templates__alpaca.json"
    if file_digest(template_path) != "853c698d1e733655a429232100e31a33beeab2a29d0b98ba63232c90e0f379de":
        raise ValueError("Native source template changed")
    if (ROOT / "sources/biot5_test_tasks.txt").read_text().splitlines() != ["task234_protein_design_molinst_pro_test"]:
        raise ValueError("Released test-task list changed")
    template = json.loads(template_path.read_text())
    cases, refs, approved, held = [], [], [], []
    for index, instance in enumerate(instances):
        identity = "P36:" + instance["id"]
        review_common = {"case_id": identity, "source_index": index, "source_instance_id": instance["id"],
                         "instruction_sha256": digest(instance["instruction"]), "input_sha256": digest(instance["input"])}
        if index not in BENIGN_REASONS:
            reason = PREFIX_HOLDS.get(index, "Unreviewed outside prospectively bounded first64 source-order prefix; held, not approved.")
            matches = sorted(set(m.group(0).lower() for m in RISK_SCREEN.finditer(instance["instruction"] + "\n" + instance["input"])))
            held.append({**review_common, "reason": reason, "manual_prefix_reviewed": index < 64,
                         "screen_markers": matches, "screen_is_approval": False})
            continue
        prompt = transform(instance, template)
        common = {"task": "P36", "case_id": identity, "variant": VARIANT, "split": "official_BioT5_test_reviewed_first64_subset"}
        cases.append({**common, "messages": [{"role": "system", "content": FORMAT}, {"role": "user", "content": prompt}]})
        approved.append({**review_common, "benign_reason": BENIGN_REASONS[index],
                         "review_basis": "Manual instruction/input-only review; no sequence targets or model responses inspected."})
        outputs = instance["output"]
        if not isinstance(outputs, list) or len(outputs) != 1 or not re.fullmatch(r"<bop>(?:<p>[A-Z])+<eop>", outputs[0]):
            raise ValueError("Native single-target serialization changed; no favorable reference selection")
        refs.append({"task": "P36", "case_id": identity, "target": outputs[0], "source_prompt": prompt})
    data = ROOT / "data"
    data.mkdir(exist_ok=True)
    for name, rows in [("model_inputs.jsonl", cases), ("scorer_references.jsonl", refs)]:
        path = data / name
        path.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows))
        path.chmod(0o600)
    review = {"task_id": "P36", "created_at_utc": datetime.now(timezone.utc).isoformat(),
              "source_sha256": SOURCE_SHA, "full_source_case_count": 5876,
              "manual_reviewed_prefix_count": 64, "approved_count": 59, "held_count": 5817,
              "prefix_held_count": 5, "outside_prefix_unreviewed_count": 5812,
              "case_scope": "PARTIAL: all eligible cases from a first64 source-order prefix, before inference; not full benchmark.",
              "approved_case_ids": [c["case_id"] for c in cases], "approved_case_reviews": approved,
              "held_cases": held, "input_review_complete_for_entire_source": False,
              "targets_used_for_input_eligibility": False, "inference_dispatched": 0,
              "screening_rule_role": "Metadata for manual follow-up only; keyword absence never approves a case."}
    write_json(ROOT / "input_review.json", review)
    metric_contract = {
        "native_wrapper": "sources/biot5_plus__metrics__pro_understand_metrics__pro_understand_metrics.py",
        "native_wrapper_method": "Pro_understand._compute; exact source AST method, no change to reference-pair wiring",
        "reference_policy": "[full original serialized target, full original Alpaca user prompt] per case; input remains an alternate reference",
        "hf_metric_revision": "1bc20e7e9df922e5dfb597c31a4ea8467a89caff",
        "hf_method": "Rouge._compute executed verbatim with rouge-score0.1.2; replace only unpinned network evaluate.load resolution",
        "tokenizer": "Default ASCII-alphanumeric lowercasing tokenizer, use_stemmer=False; this is lexical, not residue-alignment scoring",
        "primary_metric": "rougeL", "aggregation": "HF/Google BootstrapAggregator defaults,1000 resamples; median(mid).fmeasure; fixed numpy seed42",
        "multi_reference_behavior": "Per ROUGE type, source score_multi chooses greatest F-measure among target and input references",
        "output_processing": "Raw returned final content; no parsing, whitespace cleanup, target-assisted repair, regeneration or favorable metric choice",
        "missing_slot_policy": "Empty prediction for all missing/failed planned subset slots; full59-slot denominator retained",
        "invalid_truncation_policy": "Retain and score raw malformed or length-stopped content; separate serialization diagnostics",
        "biological_function_validation": False,
    }
    code_files = ["p36_contract.py", "prepare_p36.py", "run_p36.py", "score_p36.py", "test_p36.py"]
    source_files = [str(p.relative_to(ROOT)) for p in (ROOT / "sources").iterdir() if p.name != source_path.name]
    frozen = code_files + source_files + ["data/model_inputs.jsonl", "input_review.json"]
    config = {"task_id": "P36", "variant": VARIANT, "model": MODEL, "model_revision": REVISION,
              "checkpoint_precision": "Original publisher BF16; no quantization", "generation": GENERATION,
              "concurrency": 1, "input_file": "data/model_inputs.jsonl", "review_file": "input_review.json",
              "scorer_reference_file": "data/scorer_references.jsonl",
              "scorer_reference_sha256": file_digest(data / "scorer_references.jsonl"),
              "case_contract_sha256": digest(cases), "frozen_files_sha256": {f: file_digest(ROOT / f) for f in frozen},
              "source_dataset_revision": "9f70da9e8f0df32e7e62846f7ad78a829b00c0fd", "source_dataset_sha256": SOURCE_SHA,
              "native_prompt_policy": "Exact per-instance instruction/input and official Alpaca template; no targets in requests",
              "output_format_adaptation": FORMAT,
              "context_policy": "Full source text and full source target; no native T5 512-input/256-target token truncation reproduced",
              "metric_contract": metric_contract,
              "comparison_qualification": "Partial59-case zero-shot Qwen text baseline. Same released paired-reference ROUGE algorithm, prospectively pinned cached HF revision; full raw prompt/target serialization and added output-format system instruction differ from trained BioT5+ tokenizer,512/256 caps and greedy generation. Historical evaluate.load resolution unpinned. Not paper normalized Smith-Waterman, not design-function success, not full5876-case completion.",
              "execution_authorized_by_preparation": False, "requires_separate_exact_config_execution_approval": True,
              "tools": [], "training": False, "paper_normalized_smith_waterman_available": False}
    write_json(ROOT / "proposed_config.json", config)
    write_json(ROOT / "proposed_authorization.json", {"execution_authorized": False,
               "configuration_sha256": file_digest(ROOT / "proposed_config.json"), "endpoint": None,
               "run_directory": None, "reason": "Preparation only; root must approve exact endpoint/run and config before any call."})
    print(json.dumps({"prepared": len(cases), "held": len(held), "full_source": len(instances),
                      "configuration_sha256": file_digest(ROOT / "proposed_config.json")}))


if __name__ == "__main__":
    main()
