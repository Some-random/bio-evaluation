#!/usr/bin/env python3
"""Rebuild aggregate source-audit reports without inference or result changes."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "sources/deepfri_contract_audit_2026-10-15"
REVISIONS = {
    "deepfri": ("flatironinstitute/DeepFRI", "3bd6c7eae67894ccedbe1117e33b3abe544bca71"),
    "torchdrug": ("DeepGraphLearning/torchdrug", "6066fbd82360abb5f270cba1eca560af01b8cc90"),
    "protst": ("DeepGraphLearning/ProtST", "db53a76ed2430eb66dd9c8134ace99fd60980fb3"),
}


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        while data := stream.read(8 * 1024 * 1024):
            h.update(data)
    return h.hexdigest()


def read(path):
    return json.loads((ROOT / path).read_text())


def write(path, value):
    (ROOT / path).write_text(json.dumps(value, indent=2) + "\n")


def build():
    files = []
    for path in sorted(SOURCE.iterdir()):
        if not path.is_file() or path.name == "source_manifest.json" or path.name.endswith(".partial"):
            continue
        item = {"local_path": str(path.relative_to(ROOT)), "bytes": path.stat().st_size, "sha256": sha(path)}
        prefix = path.name.split("__")[0]
        if prefix in REVISIONS and "__" in path.name:
            repository, revision = REVISIONS[prefix]
            source_path = path.name[len(prefix) + 2:].replace("__", "/")
            item.update(repository=repository, revision=revision, source_path=source_path,
                        url=f"https://raw.githubusercontent.com/{repository}/{revision}/{source_path}")
        elif path.name.startswith("expasy__"):
            item.update(publisher="SIB ExPASy ENZYME", release="02-Sep-2026",
                        url="https://ftp.expasy.org/databases/enzyme/" + path.name.removeprefix("expasy__"),
                        qualification="Supplemental display names, not verified 2020 author wording")
        elif path.name.startswith("zenodo__"):
            item.update(publisher="Zenodo 6622158", source_member=path.name.removeprefix("zenodo__").replace("__", "/"),
                        integrity="Member CRC/size and local SHA verified; complete parent archive MD5 not verified")
        files.append(item)
    manifest_name = "sources/deepfri_contract_audit_2026-10-15/source_manifest.json"
    write(manifest_name, {"files": files, "no_training_or_validation_structures_acquired": True,
                         "no_weight_tensors_acquired": True, "full_parent_archive_md5_verified": False})
    tasks = []
    for task in ["P12", "P13", "P14", "P15"]:
        preparation_name = f"data/catalog_deepfri_tasks/{task}/preparation.json"
        preparation = read(preparation_name)
        config_name = f"configs/local_deepfri_{task.lower()}_sparse_confidence_proposed.json"
        config = read(config_name)
        vocabulary = read(config["class_vocabulary_file"])
        tasks.append({"task_id": task, "branch": preparation["branch"],
                      "status": "source_prepared_disabled_confidence_adaptation_frozen",
                      "counts": preparation["counts"], "membership": preparation["membership"],
                      "parser_rejection_counts": preparation["parser_rejection_counts"],
                      "native_docstring_test_count": 1840 if task == "P12" else 2991,
                      "preparation_file": preparation_name, "preparation_sha256": sha(ROOT / preparation_name),
                      "proposed_config": config_name, "proposed_config_sha256": sha(ROOT / config_name),
                      "enabled": config["enabled"], "proposal_status": config["proposal_status"],
                      "missing_class_descriptions": sum(row["description"] is None for row in vocabulary["classes"]),
                      "transferred_or_deleted_current_EC_descriptions": sum((row["description"] or "").startswith(("Transferred entry", "Deleted entry")) for row in vocabulary["classes"])})
    budget_name = "reports/DEEPFRI_SPARSE_CONFIDENCE_TOKEN_BUDGET_2026-10-15.json"
    budget = read(budget_name)
    first = read(tasks[0]["proposed_config"])
    audit = {
        "reviewed_at_utc": datetime.now(timezone.utc).isoformat(), "task_ids": [row["task_id"] for row in tasks],
        "scope": "Natural protein annotation source preparation, native scoring contract and disabled Qwen confidence adaptation",
        "source_revisions": {repository: revision for repository, revision in REVISIONS.values()},
        "source_manifest": manifest_name, "source_manifest_sha256": sha(ROOT / manifest_name), "tasks": tasks,
        "acquired_test_zip_provenance": [read(f"sources/deepfri_contract_audit_2026-10-15/{dataset}.test.zip.provenance.json") for dataset in ["EnzymeCommission", "GeneOntology"]],
        "native_case_identity_qualification": "No released author processed pickle/dependency lock was located. Current RDKit 2024.09.6 residue projection retains 1,853 EC / 3,129 GO, not printed 1,840/2,991, and does not execute every TorchDrug graph/feature operation. Released full-FASTA test-list inputs are a distinct source-qualified adaptation.",
        "native_sequence_contract": "ProtST PretrainESM consumes graph.residue_type rather than coordinates. Annotation configuration deterministically keeps first 550 modeled residues. Full PDB-modeled residues and full released FASTA are preserved separately; no missing residues are invented.",
        "github_vs_native_zenodo": "Zenodo replaces retired EC 1BVS-A with 7OA5-A and GO 6BJ0-A with 6UIQ-A in annotations/FASTA; common-ID sequences match GitHub. EC CSV retains 1BVS-A but is used only to exclude zero flags. EC FASTA has extra 4UDF-1B outside test list. GO 5JM5-A is in full FASTA/test list but absent from the PDB archive.",
        "native_metric_contract": read("sources/deepfri_contract_audit_2026-10-15/native_metric_contract.json"),
        "ontology_contract": read("sources/deepfri_contract_audit_2026-10-15/ontology_contract.json"),
        "head_availability": {
            "audited_official_ProtST_github_release_count": 0,
            "pretrained_checkpoint_metadata": read("sources/deepfri_contract_audit_2026-10-15/protst_checkpoint_metadata_audit.json"),
            "verified_frozen_EC_GO_task_head_available": False,
            "blocker": "All three advertised ProtST checkpoints contain backbones/pretraining heads, no downstream task MLP. Source constructs a fresh task head and trains 50 epochs. New training is prohibited.",
            "next_step": "Obtain author frozen task checkpoints, class order and processed-case/dependency identity for native specialist reproduction without training. The separately frozen Qwen confidence adaptation needs no new head.",
            "different_DeepFRI_specialist_models": read("sources/deepfri_contract_audit_2026-10-15/deepfri_released_model_metadata.json"),
        },
        "qwen_proposal": {
            "variant": first["variant"], "generation_recipe_unchanged": True, "max_output_tokens": 4096,
            "token_budget_audit": budget_name, "all_cases_fit_context": all(row["all_cases_fit"] for row in budget["tasks"]),
            "total_cases": budget["total_cases"], "total_prompt_tokens_no_cache_savings": budget["total_input_tokens_no_prefix_cache_assumed"],
            "total_max_output_tokens": budget["total_maximum_requested_output_tokens"],
            "prefix_cache_qualification": "Fixed class vocabulary follows varying sequence; no ordinary shared-prefix savings assumed.",
            "scorer": first["scorer"], "scorer_sha256": sha(ROOT / first["scorer"]),
            "new_eight_gpu_executor": "scripts/execute_local_deepfri_confidence_eight_gpu.py",
            "new_eight_gpu_executor_sha256": sha(ROOT / "scripts/execute_local_deepfri_confidence_eight_gpu.py"),
            "protocol_sha256": first["scoring_protocol_sha256"], "runtime": read(first["scoring_runtime_file"]),
            "strict_sparse_contract": "Explicit final JSON numeric scores map. Omitted permitted IDs zero by prospective definition; explicit empty scores object valid. Constant/binary/tied vectors retained. Missing/malformed/truncated output invalid; no repair or label-list conversion. Any invalid planned vector makes full native AP/Fmax null; parsed-only diagnostics distinct.",
            "all_zero_reference": "Predeclared all-zero full matrix offline diagnostic, never model predictions or missing-output replacements.",
        },
        "verification": {"reporter_tests": 10, "source_preparation_tests": 4, "sparse_contract_tests": 3, "range_zip_tests": 2, "confidence_scorer_tests": 6,
                         "inference_performed": False, "providers_called": False, "training_performed": False,
                         "central_authorizations_or_queues_changed": False, "B06_or_flagged_P18_content_opened": False,
                         "original_B01_or_interpretation_registry_modified": False,
                         "genomic_scorer_sha256_unchanged": sha(ROOT / "scripts/score_local_genomics.py") == "31b786c16b70e4914268c561244f1fd3ed5c4e049e7ae7a79da3ac973c2e5240"},
        "caveats": ["Released full test-list scope differs from paper/author processed PDB identity.",
                    "Prompted confidence scores differ from trained specialist representations and heads.",
                    "Absent curated labels do not prove biological absence.",
                    "Prediction agreement does not validate explanation, probability calibration or mechanisms.",
                    "Prior public benchmark exposure is unknown.",
                    "Historical ontology bytes and author GPU tie behavior are unavailable; current GO and score propagation were not substituted."],
    }
    report_name = "reports/DEEPFRI_NATIVE_SOURCE_AUDIT_2026-10-15.json"
    write(report_name, audit)
    lines = ["# DeepFRI-derived P12–P15 source and confidence audit", "",
             "All four source contracts and disabled Qwen sparse-confidence proposals are prepared. No inference, provider call, training, central authorization or queue change was performed.", "",
             "| Task | Branch | Released test IDs | Classes | Current RDKit PDBs | Printed native count |",
             "| --- | --- | ---: | ---: | ---: | ---: |"]
    for row in tasks:
        counts = row["counts"]
        lines.append(f"| {row['task_id']} | {row['branch']} | {counts['released_test95_list_ids']} | {counts['global_classes']} | {counts['current_rdkit_projection_retained']} | {row['native_docstring_test_count']} |")
    lines += ["", "Native Zenodo test-only ZIPs total 271,260,486 bytes. Member CRC/size and local SHA-256 are verified; complete parent-archive MD5s are unverified because training/validation structures were skipped. Exact publisher URLs, revisions and hashes are in the source manifest and JSON audit.", "",
              "Full released FASTA and PDB-modeled residues remain separate. Only 105 EC and 142 GO parsed sequences equal full FASTA; 1,748 EC and 2,987 GO differ. The qualified current parser projection cannot establish the authors’ unpublished parsed cache. Native ProtST consumes residue identities and crops to first 550 modeled residues. Every prepared source sequence remains complete.", "",
              "Retired-ID replacements, one outside-test EC FASTA record, and one missing GO test PDB are recorded explicitly. Qwen proposals use exact Zenodo released test lists with complete FASTA, not claimed native paper case identity. Global vocabulary order is complete source-header order, never selected by test-positive labels. GO names are exact native headers; EC supplemental names use ExPASy 02-Sep-2026, including 12 transferred/deleted entries without remapping the original 538 IDs.", "",
              "[Pinned TorchDrug metric code](https://github.com/DeepGraphLearning/torchdrug/blob/6066fbd82360abb5f270cba1eca560af01b8cc90/torchdrug/metrics/metric.py) defines flattened rank-average `auprc@micro` and rank-position `f1_max`. Ties can be evaluated within a score block, unlike sklearn’s threshold-grouped micro AP. Native and supplemental metrics retain separate names; the better result is never selected.", "",
              "GO reference annotations already include source OBO reachability closure, excluding the three roots. Native ProtST scoring applies no output-score propagation. Exact author OBO bytes/version are absent from audited assets; the source collection script uses an unversioned URL. This blocks exact closure regeneration, not scoring the provided target matrix. Current GO was not substituted.", "",
              "Final disabled proposals are `configs/local_deepfri_p12_sparse_confidence_proposed.json` through `p15`; earlier disabled snapshots are preserved. An explicit final numeric JSON scores map declares omitted classes zero; an explicit empty scores object is valid. Constant, binary and tied numeric vectors remain valid. Missing/malformed/truncated answers are invalid, with no repair or hard-label conversion. Any invalid planned vector makes full AP/Fmax null; parsed-only metrics remain separate.", "",
              "The scorer locks all raw outputs/missing slots and validates manifest/config/model/input/reference hashes before labels. CPU float32 native scoring freezes Torch 2.13.0+cu132 and one intraop/interop thread. Separate sklearn 1.5.2 AP uses the existing isolated environment; serving packages were unchanged. `OFFLINE_ALL_ZERO_REFERENCE` is a predeclared diagnostic, never model predictions or invalid-output replacement. Historical author GPU tie equivalence is unknown.", "",
              "Actual tokenizer input IDs verify all 12,167 prompts fit 262,144 tokens. Maximum prompt lengths: EC 11,353 / BP 33,203 / MF 9,627 / CC 5,677, plus unchanged 4,096 output tokens. Total volume is 183,005,770 prompt tokens without cache savings and at most 49,836,032 output tokens. Fixed vocabulary follows the varying sequence, so ordinary shared-prefix savings are not assumed. Output validity and quality remain unmeasured.", "",
              "The [official ProtST release](https://github.com/DeepGraphLearning/ProtST) advertises three pretraining checkpoints. Safe ZIP metadata inspection found no downstream task MLP; tensor weights were not downloaded or unpickled. Source downstream evaluation first trains a fresh head. No frozen EC/GO task head was found in audited official assets. Author task checkpoints plus class/case/dependency identity are needed for native specialist reproduction without training.", "",
              "Separate DeepFRI trained-model archives are reachable, about 904/872 MB, but their contents were not acquired or validated. They would be a different specialist baseline, not an automatic replacement for Qwen or ProtST.", "",
              "Ten reporter, four preparation, three sparse-contract, two range-ZIP and six scorer synthetic tests pass. Original first LitQA2 artifacts, interpretation registry, held content and frozen genomic files remain unchanged. Prediction agreement does not validate explanations, calibration, mechanisms or biological absence. Public pretraining exposure is unknown.", ""]
    (ROOT / report_name).with_suffix(".md").write_text("\n".join(lines))
    return {"json_report": report_name, "markdown_report": report_name.removesuffix(".json") + ".md", "source_files": len(files), "scorer_sha256": audit["qwen_proposal"]["scorer_sha256"], "genomic_unchanged": audit["verification"]["genomic_scorer_sha256_unchanged"]}


if __name__ == "__main__":
    print(json.dumps(build()))
