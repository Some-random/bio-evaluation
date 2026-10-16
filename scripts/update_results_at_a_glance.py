"""Concise offline comparison of terminal aggregate results; never read raw cases."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path
import tempfile

COMPARISONS = "reports/PUBLISHED_BENCHMARK_COMPARISONS_2026-10-15.json"
P43_COUNTS = {"human": 1200, "biosnap": 5493, "bindingdb": 9840}
COUNT_KEYS = {"planned", "completed", "parsed", "correct", "invalid", "invalid_outputs", "missing", "held", "total"}
PERCENT_METRICS = {"accuracy", "strict_accuracy", "precision", "coverage", "closed_accuracy", "open_token_recall"}


def sha(raw): return hashlib.sha256(raw).hexdigest()


def number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def clean(value):
    if isinstance(value, float) and not math.isfinite(value): return None
    if isinstance(value, dict): return {key: clean(item) for key, item in value.items()}
    if isinstance(value, list): return [clean(item) for item in value]
    return value


def flatten(metrics, prefix=""):
    for key, value in metrics.items():
        name = prefix + key
        if isinstance(value, dict): yield from flatten(value, name + ".")
        elif key not in COUNT_KEYS and not key.startswith("n_") and (number(value) or value is None): yield name, value


def primary_metrics_valid(score):
    declared = score.get("full_planned_primary_metrics_valid")
    if declared is not None:
        return declared is True
    metrics = score.get("metrics", {})
    # Older frozen regression scorers report a parsed-only diagnostic without
    # the newer validity flag. That diagnostic cannot complete the full test.
    for key, value in metrics.items():
        if key.lower() == "spearman":
            return number(value)
    primary = [(key, value) for key, value in flatten(metrics)
               if "parsed_only" not in key.lower() and "diagnostic" not in key.lower()]
    return bool(primary) and all(number(value) for _, value in primary)


def valid_union(value, expected=None):
    count = value.get("expected_test_case_count")
    return (value.get("complete") is True and value.get("union_matches_full_test_ids") is True
            and type(count) is int and count > 0 and (expected is None or count == expected)
            and value.get("unique_observed_case_count") == count and value.get("missing_case_count") == 0
            and value.get("extra_case_count") == 0 and value.get("duplicate_case_count", 0) == 0)


def coverage_kind(score, config):
    scope = str(score.get("case_scope", config.get("case_scope", ""))).lower()
    if "shard_only" in scope or "shard_index" in score or "shard_index" in config:
        return "shard_only"
    union = score.get("full_test_id_union_validation", {})
    uses_shards = "shard" in scope or any(type(obj.get("shard_count")) is int and obj["shard_count"] > 1 for obj in [score, config])
    if uses_shards and (not valid_union(union, score.get("planned"))
            or config.get("full_test_case_count", score.get("planned")) != score.get("planned")):
        return "unverified_shard_aggregate"
    if score.get("task_id") == "P43" or config.get("approved_task_ids") == ["P43"]:
        if score.get("dataset", config.get("dataset")) in P43_COUNTS: return "dataset_component"
        recognized = scope in {"complete_three_native_tests_separate_metrics", "native_source_test_union_separate_dataset_metrics"}
        if (recognized and valid_union(union, 16533) and score.get("dataset_case_counts") == P43_COUNTS
                and set(score.get("dataset_metrics", score.get("metrics", {}))) == set(P43_COUNTS)):
            return "verified_three_dataset_aggregate"
        return "unverified_dataset_aggregate"
    if score.get("task_id") == "P29" and score.get("native_split") in {"id", "ood"}: return "native_split_component"
    return "completed_declared_run"


def select_reference(task_id, dataset, registry):
    baselines = registry.get("published_baselines", [])
    if task_id.startswith("B"):
        chosen = next((b for b in baselines if "gpt5_2_accuracy_percent" in b.get("metrics", {})), None)
        if chosen:
            return {**chosen, "display_model": "GPT-5.2", "display_metrics": {"accuracy_percent": chosen["metrics"]["gpt5_2_accuracy_percent"]},
                    "display_scope": "public set"}
    if task_id in {"P10", "P11", "P43"}:
        if task_id == "P43" and not dataset: return None
        chosen = next((b for b in baselines if b.get("model") == "BioT5+"), None)
        if chosen:
            key = dataset + "_auroc" if task_id == "P43" and dataset else "accuracy_percent"
            return {**chosen, "display_model": "BioT5+ (supervised)", "display_metrics": {key: chosen.get("metrics", {}).get(key)},
                    "display_scope": "official source split; different training"}
    if baselines:
        chosen = baselines[0]
        return {**chosen, "display_model": chosen.get("model"), "display_metrics": chosen.get("metrics", {}),
                "display_scope": "published protocol; contextual"}
    return None


def build_report(root: Path, generated_at=None):
    root = Path(root); provenance, warnings, excluded, rows, aggregate_containers, diagnostic_rows = {}, [], [], [], [], []
    def read(name, default=None):
        path = root / name
        if not path.exists(): return default
        raw = path.read_bytes(); provenance[name] = sha(raw)
        try: return json.loads(raw)
        except (ValueError, UnicodeError):
            warnings.append("Unfinished/unreadable metadata snapshot: " + name); return default
    registry_doc = read(COMPARISONS, {}) or {}
    registry = {r["task_id"]: r for r in registry_doc.get("tasks", [])}
    qualification = read("reports/v04_output_format_qualification.json", {}) or {}
    vision_audit = read("reports/labbench_vision_aggregate_integrity_qualification.json", {}) or {}
    for path in sorted((root / "results/runs").glob("*/scores.json")):
        base = str(path.parent.relative_to(root)); score_name = base + "/scores.json"
        score = read(score_name, {}) or {}; done = read(base + "/completion.json", {}) or {}
        manifest = read(base + "/run_manifest.json", {}) or {}; config = manifest.get("configuration", {})
        task_id = score.get("task_id")
        if task_id is None and len(config.get("approved_task_ids", [])) == 1: task_id = config["approved_task_ids"][0]
        run_id = score.get("run_id", path.parent.name)
        reason = None
        if not task_id: reason = "ambiguous_or_missing_task_identity"
        elif any(type(done.get(key)) is not int or done[key] != 0 for key in ["generation_exit_code", "scoring_exit_code"]): reason = "missing_or_nonzero_terminal_completion"
        elif not number(score.get("planned")) or score["planned"] <= 0 or score.get("completed") != score["planned"]: reason = "incomplete_planned_outputs"
        elif not isinstance(score.get("metrics"), dict) or not list(flatten(score["metrics"])): reason = "no_reported_primary_metric"
        elif done.get("scores_sha256") and done["scores_sha256"] != provenance[score_name]: reason = "terminal_score_hash_mismatch"
        elif done.get("run_manifest_sha256") and done["run_manifest_sha256"] != provenance.get(base + "/run_manifest.json"): reason = "terminal_manifest_hash_mismatch"
        kind = coverage_kind(score, config)
        if reason is None and kind in {"shard_only", "unverified_shard_aggregate", "unverified_dataset_aggregate"}: reason = kind
        if reason:
            excluded.append({"run_id": run_id, "task_id": task_id, "reason": reason, "source_scores": score_name}); continue
        diagnostic_only = not primary_metrics_valid(score)
        if diagnostic_only:
            kind = "diagnostic_only_primary_metrics_invalid"
            excluded.append({"run_id": run_id, "task_id": task_id, "reason": kind, "source_scores": score_name})
        source = registry.get(task_id, {}); dataset = score.get("dataset", config.get("dataset"))
        caveats = []
        if task_id.startswith("B"):
            public = source.get("released_public_case_count")
            caveats.append(f"Public release {score['planned']}/{public if public is not None else 'unknown'}; one seeded run, no tools; published decoder/repeats differ.")
            if task_id == "B01": caveats.append("197/199 public cases; two held before inference. Original LAB paper includes private cases and means over three runs.")
        if task_id in {"P10", "P11"}: caveats.append("Full source test, all invalid answers retained as failures; zero-shot full sequences versus supervised BioT5+.")
        if task_id in {"B04", "B05"} and any(r.get("run_id") == run_id and r.get("score_sha256") == provenance[score_name]
                for r in vision_audit.get("audited_runs", [])):
            caveats.append("Independent local source/mapping/request audit passed; public pretraining exposure remains unknown.")
            if task_id == "B04" and vision_audit.get("B04_native_wrapper_encoding"):
                caveats.append("Original publisher JPEGs preserved; author-wrapper re-encoding differs in pixels under the diagnostic runtime. Historical encoding and accuracy impact are unknown.")
        if task_id == "P43": caveats.append("AUROC/AP are separate dataset fractions, not pooled. One-token conditional Yes/No likelihood; length finish is expected here.")
        if task_id == "B08" and score.get("parsed") == 0 and score.get("finish_reasons", {}).get("length") == score["planned"]:
            caveats.append(f"All {score['planned']} outputs reached the {config.get('generation', {}).get('max_tokens', 'unknown')}-token limit; zero parsed answers. The zero score does not establish wrong biological predictions.")
            caveats.append("Native abstention-based coverage is not the parse rate.")
        if task_id == "V04":
            caveats.append("Strict whole-final matching; qualified reconstructed scorer versus target-fine-tuned paper model. Zero exact match does not establish wrong clinical predictions or no visual ability.")
            if qualification.get("run_id") == run_id and qualification.get("score_sha256") == provenance[score_name]:
                caveats.append("Prediction-only audit: 500 multiline finals, 15–263 words (median 70); verbose answer format is material.")
        reference = select_reference(task_id, dataset, source)
        row = {"task_id": task_id, "task_name": source.get("task", task_id), "run_id": run_id,
            "dataset": dataset, "native_split": score.get("native_split"), "completion_scope": kind,
            "case_scope": score.get("case_scope", config.get("case_scope")), "model": score.get("model", config.get("model")),
            "model_revision": score.get("model_revision", config.get("model_revision")),
            "checkpoint_precision": config.get("checkpoint_precision"), "protocol_variant": score.get("protocol_variant", config.get("variant")),
            "local_training_regime": "Fixed zero-shot baseline; no benchmark task training or test-guided prompt/model selection",
            "generation": config.get("generation"), "finished_at_utc": done.get("finished_at_utc"),
            "counts": {key: score.get(key) for key in ["planned", "completed", "parsed", "invalid_outputs", "missing_or_failed_outputs", "held_before_inference"]},
            "finish_reasons": score.get("finish_reasons", {}), "metrics": score.get("metrics", {}),
            "metric_units": score.get("metric_units", "Accuracy/precision/coverage fractions; AUROC/AP fractions; other metrics preserve source-native units"),
            "curated_only_diagnostic_metrics": score.get("curated_only_diagnostic_metrics"),
            "comparison_to_paper": score.get("comparison_to_paper"), "comparison_status": "contextual_side_by_side_no_superiority_or_significance_claim",
            "selected_published_reference": reference, "all_published_references": source.get("published_baselines", []),
            "caveats": caveats, "explanation_support_score": score.get("explanation_support_score"),
            "source_scores": score_name, "source_completion": base + "/completion.json", "scores_sha256": provenance[score_name],
            "completion_score_hash_verified": bool(done.get("scores_sha256")), "full_test_id_union_validation": score.get("full_test_id_union_validation"),
            "input_reference_dependence": score.get("native_reference_qualification"), "seed_predictor_overlap": score.get("seed_predictor_overlap")}
        if diagnostic_only:
            row["caveats"].append("All planned requests finished, but the full-test primary metric is undefined. Parsed-only diagnostics do not complete the benchmark and cannot replace its native metric.")
            diagnostic_rows.append(row)
        elif kind == "verified_three_dataset_aggregate": aggregate_containers.append(row)
        else: rows.append(row)
    p43_complete = bool(aggregate_containers)
    p29_splits = {row["native_split"] for row in rows if row["task_id"] == "P29"}
    whole_ids = {row["task_id"] for row in rows if row["completion_scope"] == "completed_declared_run"}
    if p43_complete: whole_ids.add("P43")
    if p29_splits == {"id", "ood"}: whole_ids.add("P29")
    preparation = read("reports/catalog_posttrain_protein_preparation.json", {}) or {}
    seed_audit = {"task_id": "P29", "kind": "offline_input_reference_dependence_audit_not_Qwen_result",
        "source_report": "reports/catalog_posttrain_protein_preparation.json", "native_target_augmentation": preparation.get("native_target_augmentation"),
        "splits": {key: value.get("seed_predictor_overlap") for key, value in preparation.get("splits", {}).items()}}
    blockers = []
    recovery = read("reports/remaining_native_source_recovery_2026-10-15.json", {}) or {}
    pfa = [r for r in recovery.get("tasks", []) if r.get("task_id") in {"P19", "P20", "P21", "P22"}]
    if pfa:
        blockers.append({"task_ids": [r["task_id"] for r in pfa], "description": "PFArena official release found; publisher dataset access is gated and original assay/case review remains pending.",
            "source_report": "reports/remaining_native_source_recovery_2026-10-15.md", "publisher_url": pfa[0].get("official_release", {}).get("dataset_url")})
    gaps = read("reports/posttrain_native_gap_audit.json", {}) or {}
    for task, description in [("N04", "Exact network-held-out CSVs/IDs unavailable; author genomics link redirects to sign-in. Original N01 is not a substitute."),
                              ("N05", "Exact adapted hepatoblastoma split/vector alignment/RNA evaluator missing; upstream MEDEA questions or gene lists do not replace required expression inputs.")]:
        if task in gaps: blockers.append({"task_ids": [task], "description": description, "source_report": "reports/POSTTRAIN_NATIVE_GAP_AUDIT.md", "source_status": gaps[task].get("status")})
    return clean({"generated_at_utc": generated_at or datetime.now(timezone.utc).isoformat(), "catalog_settings": registry_doc.get("task_count"),
        "completed_whole_declared_setting_ids": sorted(whole_ids), "whole_completion_is_not_full_paper_replication": True,
        "completed_rows": sorted(rows, key=lambda r: (r["task_id"], r.get("dataset") or r.get("native_split") or "", r["run_id"])),
        "diagnostic_only_finished_runs": sorted(diagnostic_rows, key=lambda r: (r["task_id"], r["run_id"])),
        "P43": {"whole_setting_complete": p43_complete, "required_tests": P43_COUNTS,
            "completed_components": sorted({r["dataset"] for r in rows if r["task_id"] == "P43" and r["dataset"]}),
            "validated_aggregate_containers": aggregate_containers, "metrics_never_pooled_or_averaged": True},
        "P29_seed_only_offline_audit": seed_audit if seed_audit["splits"] else None,
        "blockers": blockers, "excluded_or_not_yet_terminal_runs": excluded, "warnings": warnings, "source_sha256": provenance,
        "reporting_policy": "Only existing aggregate score/completion/manifest and public reference/report metadata read; no case inputs, per-case outputs, requests, responses, labels, inference or frozen-result edits. Failed/incomplete shards never become whole-task completion. Null metrics stay undefined.",
        "interpretation": "Outcome scores do not validate explanations or establish internal reasoning. Public pretraining exposure unknown. Paper values have different training/protocols and supply no matched superiority/significance claim."})


def format_value(name, value):
    if value is None: return "undefined"
    if not number(value): return str(value)
    leaf = name.rsplit(".", 1)[-1]
    if leaf.endswith("_percent"): return f"{value:.2f}%"
    if leaf in PERCENT_METRICS: return f"{100 * value:.1f}%"
    return f"{value:.4f}"


def local_display(row):
    metrics = list(flatten(row["metrics"]))
    if row["task_id"].startswith("B"):
        keys = ["accuracy", "precision", "coverage"]
        return "; ".join(key + " " + format_value(key, row["metrics"].get(key)) for key in keys)
    if row["task_id"] == "P43":
        return "AUROC " + format_value("auroc", row["metrics"].get("auroc")) + "; AP " + format_value("auprc", row["metrics"].get("auprc"))
    return "; ".join(key + " " + format_value(key, value) for key, value in metrics[:6]) or "metric unavailable"


def published_display(row):
    ref = row["selected_published_reference"]
    if not ref: return "Verified numerical comparator unavailable"
    values = []
    for key, value in list(flatten(ref.get("display_metrics", {})))[:3]:
        # Source registry numbers are rounded paper values: do not add decimal
        # places or invent precision when rendering them beside local scores.
        display = "undefined" if value is None else str(value) + ("%" if key.endswith("_percent") else "")
        dispersion = (ref.get("reported_std") or {}).get(key)
        if number(dispersion): display += " ± " + str(dispersion) + (" percentage points" if key.endswith("_percent") else "")
        label = "AUROC" if key.endswith("_auroc") else key.removesuffix("_percent").replace("_", " ")
        values.append(label + " " + display)
    count = ref.get("test_case_count")
    scope = (f"; n={count}" if count is not None else "")
    return f"{ref.get('display_model')}: {'; '.join(values)}{scope}; [{ref.get('source_locator', 'source')}]({ref.get('source_url')})"


def cell(value): return str(value).replace("|", "\\|").replace("\n", " ")


def render_markdown(report):
    rows = report["completed_rows"]
    limits = sorted({row["generation"]["max_tokens"] for row in rows if isinstance(row.get("generation"), dict)
                     and number(row["generation"].get("max_tokens")) and row["generation"]["max_tokens"] != 1})
    limit_text = "/".join(f"{value:,}" for value in limits) if limits else "unrecorded"
    lines = ["# Results at a glance", "", f"Snapshot: {report['generated_at_utc']}. Fixed local Qwen3.8-27B baseline; "
        f"{len(report['completed_whole_declared_setting_ids'])} settings have completed evaluations of their declared scope. "
        "This does not mean full paper replication. Finished shards and incomplete runs are excluded below.", "",
        "These are contextual comparisons: the local baseline is zero-shot; BioT5+/medical systems use task training. LAB references below use the public-set GPT-5.2 column; prompt/decoding/repeat differences remain. "
        f"B01 covers 197/199 public cases with two held before inference. No superiority or significance claim follows. Generated-answer output caps in this snapshot: {limit_text} tokens; P43 instead uses a prespecified one-token conditional likelihood score. Paper ± values preserve reported dispersion; its definition and repeat counts are not always established.", "",
        "| Setting | Local score | Cases: completed/planned; parsed | Published reference | Qualification |", "|---|---|---|---|---|"]
    for row in rows:
        suffix = " / " + (row.get("dataset") or row.get("native_split") or "") if row.get("dataset") or row.get("native_split") else ""
        counts = row["counts"]; label = row["task_id"] + suffix + " " + row["task_name"].replace("LAB-Bench / ", "")
        caveats = " ".join(row["caveats"])
        if row["completion_scope"] in {"dataset_component", "native_split_component"}: caveats = "Completed component. " + caveats
        if not caveats: caveats = "Declared local variant; input, training and scoring qualifications in linked result and JSON."
        count_text = f"{counts['completed']}/{counts['planned']}; {counts['parsed'] if counts['parsed'] is not None else 'unknown'} parsed"
        lines.append("| " + " | ".join(map(cell, [f"[{label}](../{row['source_scores']})", local_display(row), count_text, published_display(row), caveats])) + " |")
    if not rows: lines += ["", "No verified terminal whole-run or dataset-component score is available yet."]
    diagnostics = report.get("diagnostic_only_finished_runs", [])
    if diagnostics:
        lines += ["", "Finished executions with undefined full-test metrics, excluded from benchmark completion counts:", ""]
        for row in diagnostics:
            counts = row["counts"]
            lines.append(f"- [{row['task_id']} {row['task_name']}](../{row['source_scores']}): "
                         f"{counts['completed']}/{counts['planned']} requests completed, {counts['parsed']} parsed; "
                         f"{local_display(row)}. Parsed-only values are incomplete diagnostics and do not replace the native full-test score.")
    p43 = report["P43"]
    if p43["completed_components"]:
        lines += ["", "P43: " + ", ".join(p43["completed_components"]) + " component tests completed. " +
            ("All 3 tests have an exact 16,533-ID validated aggregate; each dataset's AUROC/AP remains separate." if p43["whole_setting_complete"] else "The whole setting remains incomplete until Human 1,200 + BioSNAP 5,493 + BindingDB 9,840 cases have a validated 16,533-ID union. No pooled score or mean of datasets is reported.")]
    audit = report["P29_seed_only_offline_audit"]
    if audit:
        parts = []
        for split, values in audit["splits"].items():
            parts.append(split.upper() + " " + format_value("F1", values.get("seed_context_only_native_augmented_mean_propagated_F1")) +
                " native / " + format_value("F1", values.get("seed_context_only_curated_mean_propagated_F1_diagnostic")) + " curated diagnostic")
        lines += ["", "Separate offline P29 input/reference audit, **not Qwen results**: " + "; ".join(parts) +
            ". Native targets include predictor-derived terms also supplied in context; this can reward recovery/copying and does not isolate novel function inference. Curated references also overlap predictor context. "
            "[Audit](POSTTRAIN_NATIVE_GAP_AUDIT.md)."]
    if report["blockers"]:
        lines += ["", "Genuine source blockers: " + " ".join("[" + "/".join(b["task_ids"]) + "](" + b["source_report"].removeprefix("reports/") + "): " + b["description"]
            + (" [Publisher release](" + b["publisher_url"] + ")." if b.get("publisher_url") else "") for b in report["blockers"])]
    lines += ["", "Outcome scores do not validate explanations or identify internal reasoning; public pretraining exposure is unknown. Undefined metrics remain undefined. "
        "[Full coverage/provenance](LOCAL_SUITE_RESULTS.md) · [Structured concise report](RESULTS_AT_A_GLANCE.json).", ""]
    if report["warnings"]: lines += ["Snapshot metadata warnings: " + "; ".join(report["warnings"]), ""]
    return "\n".join(lines)


def write_report(root, report):
    outputs = {"reports/RESULTS_AT_A_GLANCE.json": json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False) + "\n",
               "reports/RESULTS_AT_A_GLANCE.md": render_markdown(report)}
    for name, content in outputs.items():
        path = Path(root) / name; path.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent, delete=False) as handle:
            handle.write(content); temporary = Path(handle.name)
        temporary.replace(path)
    return list(outputs)


def main():
    parser = argparse.ArgumentParser(description=__doc__); parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args(); report = build_report(args.root); outputs = write_report(args.root, report)
    print(json.dumps({"outputs": outputs, "completed_rows": len(report["completed_rows"]), "whole_declared_settings": len(report["completed_whole_declared_setting_ids"]), "warnings": report["warnings"]}))


if __name__ == "__main__": main()
