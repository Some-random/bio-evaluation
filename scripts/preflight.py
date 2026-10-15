"""Offline protein-task preparation and conservative cost planning. No API calls."""
import csv
import hashlib
import importlib.util
import io
import json
import re
import tarfile
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "sources"
HANDOFF = ROOT / "handoff/bio_eval_agent_handoff_2026-10-13"
PG_ARCHIVE_HASH = "b40ca6bb30741a652243e90e08a485ef48a52691bff8a075ec0f396200cf6f8a"
PG_MANIFEST_HASH = "cdb7073cee6a651538c9db042be5fc84ca486d3164e646a686615f95b75cb908"
MOL_FILES = {
    "P23": "task228_protein_function_molinst_pro_test.json",
    "P24": "task222_catalytic_activity_molinst_pro_test.json",
    "P25": "task225_domain_motif_molinst_pro_test.json",
    "P26": "task231_general_function_molinst_pro_test.json",
}
ALLOWLISTS = {
    "P18": ["target_name", "organism", "fitness_description", "wild_type", "candidates"],
    "P23": ["instruction", "sequence"], "P24": ["instruction", "sequence"],
    "P25": ["instruction", "sequence"], "P26": ["instruction", "sequence"],
    "P30": ["wild_type", "variant_sequence", "mutation"],
    "P31": ["wild_type", "function", "desired_effect", "position"],
    "P32": ["wild_type", "function", "desired_effect"],
}

def load_pg_module():
    spec = importlib.util.spec_from_file_location("pinned_pg_prompt", SOURCES / "pg__src__prompt.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def decode_mol_sequence(serialized):
    if not re.fullmatch(r"<bop>(?:<p>[A-Z])+<eop>", serialized):
        raise ValueError("Unexpected BioT5 protein serialization; do not silently alter it")
    sequence = serialized[len("<bop>"):-len("<eop>")].replace("<p>", "")
    assert "<bop>" + "".join("<p>" + aa for aa in sequence) + "<eop>" == serialized
    return sequence

def render_mol(task, instance):
    fields = {"instruction": instance["instruction"],
              "sequence": decode_mol_sequence(instance["input"])}
    # References, example outputs, dataset IDs and task metadata are never copied.
    return render_fields(task, fields), fields

def mutation_fields(task, row):
    site = row["entry"].split("-")[1]
    if not re.fullmatch(r"[A-Z][1-9][0-9]*[A-Z]", site):
        raise ValueError("Unresolved mutation notation")
    pos = int(site[1:-1])
    wild = row["protein1"]
    if pos > len(wild) or wild[pos - 1] != site[0] or site[0] == site[-1]:
        raise ValueError("Mutation numbering, wild-type residue or no-op mismatch")
    if task == "P30":
        return {"wild_type": wild, "variant_sequence": row["protein2"], "mutation": site}
    # The desired effect is a required INPUT for engineering, but a scoring
    # reference for explanation. The field policy is therefore task-specific.
    effect = " ".join(x.strip() for x in (row["uniprot_description"], row["GPT_description"]) if x.strip())
    fields = {"wild_type": wild, "function": row["function"], "desired_effect": effect}
    if task == "P31":
        fields["position"] = pos
    return fields

def render_fields(task, fields):
    if set(fields) != set(ALLOWLISTS[task]):
        raise ValueError(f"Fields outside the frozen allowlist for {task}")
    if task in MOL_FILES:
        return fields["instruction"] + fields["sequence"]
    if task == "P30":
        return ("Explain the biological effect of the specified mutation.\n"
                f"Wild-type sequence:\n{fields['wild_type']}\n"
                f"Variant sequence:\n{fields['variant_sequence']}\nMutation: {fields['mutation']}\n")
    if task in {"P31", "P32"}:
        text = (f"Wild-type sequence:\n{fields['wild_type']}\n"
                f"Protein function:\n{fields['function']}\nDesired effect:\n{fields['desired_effect']}\n")
        if task == "P31":
            return text + f"Position (1-based): {fields['position']}\nReturn the replacement amino acid."
        return text + "Propose up to 50 unique, non-no-op single substitutions in A123V notation."
    raise ValueError("P18 must use the pinned official renderer")

def pg_cases():
    archive = SOURCES / "proteingym-llm-eval-v1.2.tar.gz"
    if hashlib.sha256(archive.read_bytes()).hexdigest() != PG_ARCHIVE_HASH:
        raise ValueError("PG-LLM archive hash mismatch")
    renderer = load_pg_module()
    with tarfile.open(archive) as tar:
        manifest_bytes = tar.extractfile("eval_bundle_manifest.json").read()
        if hashlib.sha256(manifest_bytes).hexdigest() != PG_MANIFEST_HASH:
            raise ValueError("PG-LLM authenticated manifest mismatch")
        manifest = json.loads(manifest_bytes)
        for name, expected in manifest["files"].items():
            payload = tar.extractfile(name).read()
            if len(payload) != expected["size"] or hashlib.sha256(payload).hexdigest() != expected["sha256"]:
                raise ValueError("PG-LLM member integrity mismatch")
        # Label files are hashed for integrity but never parsed or rendered.
        reference = io.TextIOWrapper(tar.extractfile("reference/DMS_substitutions.csv"))
        meta = {r["DMS_id"]: r for r in csv.DictReader(reference)}
        members = sorted(m for m in tar.getnames() if re.search(r"/n50_b[123]\.json$", m))
        if len(members) != 651:
            raise ValueError("Expected 217 assays times three seeds")
        for name in members:
            row = json.load(tar.extractfile(name))
            record = meta[row["assay"]]
            if any(set(v) != {"id", "seq"} for v in row["variants"]):
                raise ValueError("Scoring fields in model-facing PG-LLM file")
            fields = {"target_name": record["UniProt_ID"] or row["assay"],
                      "organism": record.get("source_organism") or record.get("taxon", ""),
                      "fitness_description": record["fitness_description"],
                      "wild_type": record["target_seq"], "candidates": row["variants"]}
            mutants = [(v["id"], v["seq"], 0.0) for v in row["variants"]]
            prompt, _ = renderer.build_user_prompt(fields, fields["wild_type"], mutants)
            yield {"task": "P18", "case_id": name, "split": "n50_three_seeds",
                   "variant": "NATIVE", "system": renderer.SYSTEM_PROMPT,
                   "prompt": prompt, "fields": fields}

def all_cases(issues):
    yield from pg_cases()
    for task, filename in MOL_FILES.items():
        obj = json.loads((SOURCES / ("biot5_data__tasks_plus__" + filename)).read_text())
        for index, instance in enumerate(obj["Instances"]):
            prompt, fields = render_mol(task, instance)
            yield {"task": task, "case_id": f"{filename}:{index}", "split": "official_test",
                   "variant": "TEXT_ADAPTER_FULL_SEQUENCE", "system": "", "prompt": prompt, "fields": fields}
    for path in sorted(SOURCES.glob("muta__*test*.csv")):
        with path.open(newline="") as handle:
            for index, row in enumerate(csv.DictReader(handle)):
                for task in ("P30", "P31", "P32"):
                    try:
                        fields = mutation_fields(task, row)
                    except (ValueError, IndexError, KeyError) as exc:
                        issues.append({"task": task, "source": path.name, "row": index, "error": str(exc)})
                        continue
                    yield {"task": task, "case_id": f"{path.name}:{index}", "split": path.name,
                           "variant": "DRAFT_TEXT_ADAPTER_REQUIRES_PROTOCOL_REVIEW", "system": "",
                           "prompt": render_fields(task, fields), "fields": fields}

def cost_bounds(cases, input_rate, output_rate, batch=False):
    # Conservative plain-text planning proxy, NOT exact model tokenization.
    # Each byte is provisionally counted as one token, plus 256 for formatting.
    # Official Responses token counting must replace this before paid runs.
    factor = 0.5 if batch else 1.0
    input_cost = typical_low = typical_high = cap_cost = 0.0
    long_count = 0
    for case in cases:
        tokens = len((case["system"] + case["prompt"]).encode("utf-8")) + 256
        long = tokens > 272000
        long_count += long
        input_cost += tokens * input_rate * (2 if long else 1) / 1e6
        low, high, cap = (4096, 16384, 128000) if case["task"] == "P18" else (1024, 4096, 4096)
        unit = output_rate * (1.5 if long else 1) / 1e6
        typical_low += low * unit
        typical_high += high * unit
        cap_cost += cap * unit
    return {"calls": len(cases), "long_context_proxy_count": long_count,
            "input_proxy_cost_usd": round(input_cost * factor, 4),
            "scenario_low_usd": round((input_cost + typical_low) * factor, 4),
            "scenario_high_usd": round((input_cost + typical_high) * factor, 4),
            "output_cap_planning_bound_usd": round((input_cost + cap_cost) * factor, 4)}

def main():
    issues = []
    cases = list(all_cases(issues))
    path = ROOT / "data/model_inputs.preparation.jsonl"
    with path.open("w") as handle:
        for case in cases:
            handle.write(json.dumps(case, ensure_ascii=False) + "\n")
    path.chmod(0o600)
    counts = Counter(c["task"] for c in cases)
    split_counts = Counter((c["task"], c["split"]) for c in cases)
    pilot = []
    for task in ALLOWLISTS:
        options = sorted((c for c in cases if c["task"] == task),
                         key=lambda c: hashlib.sha256(c["case_id"].encode()).hexdigest())
        pilot.extend(options[:100])
    estimates = {}
    for label, input_rate, output_rate in (("gpt-6-luna", 0.10, 0.50), ("gpt-6.1-sol", 2.00, 10.00)):
        estimates[label] = {size: {"standard": cost_bounds(selected, input_rate, output_rate),
                                  "batch": cost_bounds(selected, input_rate, output_rate, True)}
                            for size, selected in (("pilot_100_per_task", pilot), ("all_eight_settings", cases))}
    report = {"mode": "offline_preparation", "paid_requests": 0, "api_key_required_for_preparation": False,
              "counts": dict(counts), "split_counts": [{"task": t, "split": s, "count": n} for (t, s), n in split_counts.items()],
              "issues": issues, "pricing_checked_date": "2026-10-13",
              "pricing_source": "https://developers.openai.com/api/docs/pricing",
              "input_token_method": "UTF-8 byte proxy + 256/request; exact provider count pending",
              "output_scenarios": {"P18": {"low": 4096, "high": 16384, "cap": 128000},
                                   "other_tasks": {"low": 1024, "high": 4096, "cap": 4096}},
              "reasoning_tokens_included_in_output_budget": True,
              "estimates": estimates, "no_cache_discount_assumed": True,
              "judge_calls_included": False, "retry_costs_included": False,
              "scope_note": "P18 native primary N=50; P23-P26 full-sequence text adapters; P30-P32 DRAFT adapters awaiting protocol review",
              "limitations": ["No paid inference approval", "Provider model access unverified", "Not a completed inference/scoring harness",
                              "Public-benchmark prior exposure unknown", "Pilot is label-blind, not for test-driven model or prompt selection"]}
    (ROOT / "reports/cost_estimate.json").write_text(json.dumps(report, indent=2) + "\n")
    (ROOT / "configs/field_allowlists.json").write_text(json.dumps(ALLOWLISTS, indent=2) + "\n")
    registry = json.loads((HANDOFF / "task_registry.json").read_text())["tasks"]
    with (ROOT / "reports/per_task_readiness.csv").open("w", newline="") as handle:
        writer = csv.writer(handle); writer.writerow(["id", "task", "readiness", "prepared_case_count", "notes"])
        for task in registry:
            id_ = task["id"]
            status = "verified_inputs_native_protocol" if id_ == "P18" else "adapter_required" if id_ in counts else "deferred_scope"
            notes = "Scoring and paid-run orchestration pending" if id_ in counts else "User prioritized eight protein settings"
            writer.writerow([id_, task["original_catalog"]["task"], status, counts.get(id_, 0), notes])
    print(json.dumps({"counts": dict(counts), "issues": len(issues), "estimates": estimates}, indent=2))

if __name__ == "__main__":
    main()
