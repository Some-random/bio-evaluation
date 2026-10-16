"""Restore exact frozen local inputs/references from public pinned artifacts.

No inference. No sequence contents are printed. Gold stays in ignored local files.
"""
import json
import urllib.request

from p36_contract import ROOT, file_digest, validate_cases
from prepare_p36 import transform


def main():
    manifest = json.loads((ROOT / "source_manifest.json").read_text())
    for source in manifest:
        path = ROOT / source["path"]
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists():
            data = urllib.request.urlopen(source["url"], timeout=120).read()
            path.write_bytes(data)
            path.chmod(0o600)
        if file_digest(path) != source["sha256"] or path.stat().st_size != source["bytes"]:
            raise ValueError("Public artifact does not match frozen source: " + source["path"])
    config = json.loads((ROOT / "proposed_config.json").read_text())
    review = json.loads((ROOT / "input_review.json").read_text())
    source = json.loads((ROOT / "sources/task234_protein_design_molinst_pro_test.json").read_text())["Instances"]
    template = json.loads((ROOT / "sources/biot5_plus__utils__templates__alpaca.json").read_text())
    # Reconstruct exact bytes without changing the frozen review timestamp/config.
    from p36_contract import FORMAT, VARIANT
    cases, references = [], []
    for approved in review["approved_case_reviews"]:
        instance = source[approved["source_index"]]
        if instance["id"] != approved["source_instance_id"]:
            raise ValueError("Source ID/order differs")
        prompt = transform(instance, template)
        cases.append({"task": "P36", "case_id": approved["case_id"], "variant": VARIANT,
                      "split": "official_BioT5_test_reviewed_first64_subset",
                      "messages": [{"role": "system", "content": FORMAT}, {"role": "user", "content": prompt}]})
        references.append({"task": "P36", "case_id": approved["case_id"],
                           "target": instance["output"][0], "source_prompt": prompt})
    for name, rows in [("model_inputs.jsonl", cases), ("scorer_references.jsonl", references)]:
        path = ROOT / "data" / name
        path.parent.mkdir(exist_ok=True)
        data = "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows)
        if path.exists() and path.read_text() != data:
            raise ValueError("Existing frozen data differs: " + name)
        if not path.exists():
            path.write_text(data)
            path.chmod(0o600)
    validate_cases(config)
    if file_digest(ROOT / config["scorer_reference_file"]) != config["scorer_reference_sha256"]:
        raise ValueError("Restored scorer-only reference bytes differ")
    print("Restored59 frozen model inputs/scorer references; all hashes pass. No inference.")


if __name__ == "__main__":
    main()
