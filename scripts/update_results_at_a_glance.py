"""Concise offline comparison of terminal aggregate results; never read raw cases."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path
import tempfile
from zoneinfo import ZoneInfo

COMPARISONS = "reports/PUBLISHED_BENCHMARK_COMPARISONS_2026-10-15.json"
MAIN_SCOPE = "configs/main_evaluation_scope.json"
P43_COUNTS = {"human": 1200, "biosnap": 5493, "bindingdb": 9840}
COUNT_KEYS = {"planned", "completed", "parsed", "correct", "invalid", "invalid_outputs", "missing", "held", "total"}
PERCENT_METRICS = {"accuracy", "strict_accuracy", "precision", "coverage", "closed_accuracy", "open_token_recall"}


def sha(raw): return hashlib.sha256(raw).hexdigest()


def apply_main_scope(report, scope):
    """Keep full aggregate records; qualify their separate main presentation."""
    excluded = scope.get("excluded_task_ids", [])
    if (not isinstance(excluded, list) or any(not isinstance(value, str) for value in excluded)
            or len(excluded) != len(set(excluded))):
        raise ValueError("Invalid main evaluation scope")
    report["main_report_scope"] = scope
    report["main_catalog_settings"] = (report["catalog_settings"] - len(excluded)
        if type(report.get("catalog_settings")) is int else None)
    report["main_completed_whole_declared_setting_ids"] = [task_id
        for task_id in report["completed_whole_declared_setting_ids"] if task_id not in excluded]
    return report


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


def presentation_caveats(row):
    """Add output-delivery/metric qualifications using aggregate metadata only.

    Works on retained historical rows as well as newly collected rows. Never
    reads raw cases or changes scores, denominators or completion decisions.
    """
    caveats = list(row.get("caveats", []))
    task = row.get("task_id")
    counts = row.get("counts") or {}
    planned, parsed = counts.get("planned"), counts.get("parsed")
    invalid = counts.get("invalid_outputs")
    length = (row.get("finish_reasons") or {}).get("length")
    additions = []
    if task == "B02" and type(planned) is int and type(parsed) is int:
        message = f"Usable-answer coverage: {parsed:,}/{planned:,} parsed"
        if type(length) is int:
            message += f"; {length:,}/{planned:,} reached the output cap"
        additions.append(message + ". Answer delivery partly limits this score; native non-abstention coverage is a different quantity.")
    if task == "B07" and type(planned) is int and type(parsed) is int:
        message = f"Output delivery: {parsed:,}/{planned:,} final answers parsed"
        if type(length) is int:
            message += f"; {length:,}/{planned:,} outputs reached the output-token cap"
        additions.append(message + ". The score includes invalid answers and does not isolate biological correctness. Native coverage measures non-abstention, not parsing.")
        correct = (row.get("metrics") or {}).get("n_correct")
        if type(correct) is int and parsed > 0:
            additions.append(f"{correct:,}/{parsed:,} parsed answers were correct ({100 * correct / parsed:.1f}%) on this selected subset; that subset rate is not full-task accuracy.")
    if task == "P01" and type(planned) is int and type(invalid) is int:
        additions.append(f"Strict whole-final Yes/No parsing rejects {invalid:,}/{planned:,} outputs. Invalid answers remain failures; this does not establish that each rejected biological prediction is wrong.")
    if task == "P16" and type(planned) is int and type(parsed) is int:
        additions.append(f"Strict whole-final integer parsing accepts {parsed:,}/{planned:,} answers. The score combines prediction and output-format failures.")
        if row.get("scores_sha256") == "024501321eb30797df29401b256007ab6992881a6670027cb5232cce72d5972b":
            additions.append("A separate frozen terminal-number diagnostic recovers 850 normally finished labels but only three additional correct predictions: 12/5,651 (0.212%) versus the original 9/5,651 (0.159%). The original score remains unchanged; this tested interface still has very poor class recovery. See the reaction extraction diagnostic.")
    if task in {"V01", "V02", "V03"}:
        additions.append("CLOSED uses source substring Yes/No matching, which can credit ambiguous text; OPEN measures token recall. These lexical scores can reward verbose answers and are not strict semantic answer accuracy.")
        if task == "V03":
            additions.append("The corrected CLOSED score fixes the denominator; it retains the source substring rule.")
    if task == "V05":
        additions.append("Native extraction scores only the final character; full-text choice matching is a separate adaptation. The large difference measures output-extraction sensitivity, not a controlled change in medical knowledge.")
    if task == "P42":
        if parsed == 0 and type(planned) is int:
            message = f"Zero accepted candidate outputs: 0/{planned:,} parsed"
            if type(length) is int:
                message += f"; {length:,}/{planned:,} reached the output cap"
            additions.append(message + ". Candidate design quality remains unmeasured; zero oracle success does not show that valid candidates were evaluated and failed.")
        additions.append("The fluorescence evaluator is a trained proxy; proxy improvement is not experimental validation.")
    if task in {"P23", "P24", "P25", "P26"}:
        message = "ROUGE measures lexical overlap, not biological factuality."
        if type(length) is int and type(planned) is int:
            message += f" {length:,}/{planned:,} outputs reached the output-token cap."
        additions.append(message + " Parsed means a text record, even when empty; it does not mean a usable complete annotation.")
    if task == "P07" and type(planned) is int and type(parsed) is int:
        message = f"Output delivery: {parsed:,}/{planned:,} numeric final answers parsed"
        if type(length) is int:
            message += f"; {length:,}/{planned:,} outputs reached the output-token cap"
        if any(key.lower() == "spearman" and value is None for key, value in (row.get("metrics") or {}).items()):
            message += ". Full-test correlation is undefined; parsed-only correlation is incomplete"
        additions.append(message + ".")
    for message in additions:
        if message not in caveats:
            caveats.append(message)
    return caveats


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
    score_paths = list((root / "results/runs").glob("*/scores.json"))
    score_paths += list((root / "results/scoring_corrections").glob("*/scores.json"))
    for path in sorted(score_paths):
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
        if reason is None and path.parent.parent.name == "scoring_corrections":
            correction = read(base + "/scoring_correction.json", {}) or {}
            if (correction.get("task_id") != task_id or correction.get("new_run_id") != run_id
                    or correction.get("protocol_variant") != score.get("protocol_variant")
                    or correction.get("scores_sha256") != provenance[score_name]
                    or correction.get("no_new_model_generation") is not True
                    or correction.get("original_raw_outputs_unchanged") is not True
                    or done.get("generation_attempts") != 0 or not score.get("scorer_recovery")):
                reason = "unverified_scoring_correction"
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
        generation = {**(config.get("generation") or {}), **(score.get("generation") or {})}
        budget_condition = score.get("generation_budget_condition", manifest.get("generation_budget_condition"))
        budget_counts = generation.get("output_budget_counts", {})
        if budget_condition == "MIXED_BUDGET_4K16K_CONTINUATION":
            generation["max_tokens"] = None
            caveats.append("Mixed 4K/16K continuation: "
                f"{budget_counts.get('4096', 'unrecorded')} original cases retain 4,096-token caps; "
                f"{budget_counts.get('16384', 'unrecorded')} previously undispatched cases use 16,384-token caps. "
                "Original invalid/truncated answers remain counted; this is not a uniform-16K evaluation.")
        elif budget_condition == "RETAINED_4K_COMPLETE_UNDER_BUDGET_REVISION":
            caveats.append("All cases completed under the original 4,096-token output budget; no 16K regeneration.")
        elif budget_condition == "PROSPECTIVE_16K_FULL_TASK":
            caveats.append("All original cases were previously undispatched and use the prospective 16,384-token output budget.")
        if score.get("scorer_recovery"):
            caveats.append("Separate offline scorer compatibility repair: explicit raw null and normalized empty final text are treated as equivalent. Missing confidence vectors remain invalid; native parsing, metric formulas, denominators and generations are unchanged. The original failed attempt is preserved.")
        reference = select_reference(task_id, dataset, source)
        row = {"task_id": task_id, "task_name": source.get("task", task_id), "run_id": run_id,
            "dataset": dataset, "native_split": score.get("native_split"), "completion_scope": kind,
            "case_scope": score.get("case_scope", config.get("case_scope")), "model": score.get("model", config.get("model")),
            "model_revision": score.get("model_revision", config.get("model_revision")),
            "checkpoint_precision": config.get("checkpoint_precision"), "protocol_variant": score.get("protocol_variant", config.get("variant")),
            "local_training_regime": "Fixed zero-shot baseline; no benchmark task training or test-guided prompt/model selection",
            "generation": generation or None, "generation_budget_condition": budget_condition,
            "native_protocol_variant": score.get("native_protocol_variant"),
            "finished_at_utc": done.get("finished_at_utc"),
            "counts": {key: score.get(key) for key in ["planned", "completed", "parsed", "invalid_outputs", "missing_or_failed_outputs", "held_before_inference"]},
            "finish_reasons": score.get("finish_reasons", {}), "metrics": score.get("metrics", {}),
            "metric_units": score.get("metric_units", "Accuracy/precision/coverage fractions; AUROC/AP fractions; other metrics preserve source-native units"),
            "curated_only_diagnostic_metrics": score.get("curated_only_diagnostic_metrics"),
            "comparison_to_paper": score.get("comparison_to_paper"), "comparison_status": "contextual_side_by_side_no_superiority_or_significance_claim",
            "selected_published_reference": reference, "all_published_references": source.get("published_baselines", []),
            "caveats": caveats, "explanation_support_score": score.get("explanation_support_score"),
            "scorer_recovery": score.get("scorer_recovery"),
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
    scope = read(MAIN_SCOPE, {}) or {}
    result = clean({"generated_at_utc": generated_at or datetime.now(timezone.utc).isoformat(), "catalog_settings": registry_doc.get("task_count"),
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
    return apply_main_scope(result, scope)


def format_value(name, value):
    if value is None: return "undefined"
    if not number(value): return str(value)
    leaf = name.rsplit(".", 1)[-1]
    if leaf.endswith("_percent"): return f"{value:.2f}%"
    if leaf in PERCENT_METRICS: return f"{100 * value:.1f}%"
    return f"{value:.4f}"


def local_display(row):
    metrics = list(flatten(row["metrics"]))
    if row["task_id"] in {"P12", "P13", "P14", "P15"}:
        return "; ".join(key + " " + format_value(key, row["metrics"].get(key))
                         for key in ("auprc@micro", "f1_max"))
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


def incomplete_evaluation(row, report):
    """Mark missing coverage/scoring, independently of prediction validity."""
    counts = row["counts"]
    planned, completed = counts.get("planned"), counts.get("completed")
    if not number(planned) or not number(completed) or completed < planned:
        return True
    if any(number(counts.get(key)) and counts[key] > 0
           for key in ("held_before_inference", "missing_or_failed_outputs")):
        return True
    if row["task_id"] not in report["completed_whole_declared_setting_ids"]:
        return True
    source_coverage = row.get("full_test_id_union_validation") or {}
    expected_count = source_coverage.get("expected_test_case_count")
    if number(expected_count) and completed < expected_count:
        return True
    return any(value is None for _, value in flatten(row["metrics"]))


def score_href(source, root):
    # Do not fabricate a restored original score from retained aggregate data.
    return "../" + source if (Path(root) / source).is_file() else "RESULTS_AT_A_GLANCE.json"


def render_markdown(report, root=None):
    root = Path(root) if root is not None else Path(__file__).resolve().parents[1]
    scope = report.get("main_report_scope", {})
    excluded = set(scope.get("excluded_task_ids", []))
    def latest_conditions(values):
        if not report.get("metadata_history_retention"):
            return values
        selected = {}
        for row in values:
            key = (tuple(row.get(name) for name in ("task_id", "protocol_variant", "dataset", "native_split", "case_scope")),
                row["counts"].get("planned"), row["counts"].get("held_before_inference"),
                (row.get("full_test_id_union_validation") or {}).get("expected_test_case_count"))
            previous = selected.get(key)
            order = (row.get("finished_at_utc") or "", row["run_id"])
            if previous is None or order > (previous.get("finished_at_utc") or "", previous["run_id"]):
                selected[key] = row
        return sorted(selected.values(), key=lambda row: (row["task_id"], row.get("dataset") or row.get("native_split") or "", row["run_id"]))
    rows = latest_conditions([row for row in report["completed_rows"] if row["task_id"] not in excluded])
    diagnostics = latest_conditions([row for row in report.get("diagnostic_only_finished_runs", []) if row["task_id"] not in excluded])
    completed_ids = [task_id for task_id in report["completed_whole_declared_setting_ids"] if task_id not in excluded]
    main_count = report.get("main_catalog_settings", report["catalog_settings"])
    limits = sorted({row["generation"]["max_tokens"] for row in rows if isinstance(row.get("generation"), dict)
                     and number(row["generation"].get("max_tokens")) and row["generation"]["max_tokens"] != 1}
        | {int(cap) for row in rows for cap, count in (row.get("generation") or {}).get("output_budget_counts", {}).items()
           if str(cap).isdigit() and int(cap) > 1 and type(count) is int and count > 0})
    limit_text = "/".join(f"{value:,}" for value in limits) if limits else "unrecorded"
    moment = datetime.fromisoformat(report["generated_at_utc"].replace("Z", "+00:00"))
    if moment.tzinfo is None:
        raise ValueError("The score timestamp must include its source timezone")
    display_time = moment.astimezone(ZoneInfo("America/Los_Angeles")).strftime("%Y-%m-%d %H:%M %Z")
    lines = ["# Results at a glance", "", f"Snapshot: {display_time}. Fixed local Qwen3.8-27B baseline; "
        f"{len(completed_ids)} of {main_count} main settings have completed evaluations of their declared scope. "
        "This does not mean full paper replication. Finished shards and incomplete runs are excluded below.", "",
        "[Evaluation integrity audit](EVALUATION_INTEGRITY_AUDIT_2026-10-18.md) identifies output-delivery and metric limitations; completed execution does not guarantee an informative model-quality score.",
        "[Action plan](EVALUATION_REPAIR_PLAN_2026-10-19.md) · [Decision table](EVALUATION_DECISION_TABLE.md) · [Separate reaction extraction diagnostic](REACTION_EXTRACTION_DIAGNOSTIC_2026-10-19.md)", "",
        "Where an original detailed score file is unavailable, its link opens the retained aggregate JSON. Original paths and hashes remain recorded; missing originals have not been reconstructed.", "",
        "These are contextual comparisons: the local baseline is zero-shot; BioT5+/medical systems use task training. LAB references below use the public-set GPT-5.2 column; prompt/decoding/repeat differences remain. "
        f"B01 covers 197/199 public cases with two held before inference. No superiority or significance claim follows. Generated-answer output caps in this snapshot: {limit_text} tokens; P43 instead uses a prespecified one-token conditional likelihood score. Paper ± values preserve reported dispersion; its definition and repeat counts are not always established.", "",
        "| Setting | Local score | Published reference | Qualification |", "|---|---|---|---|"]
    if excluded:
        lines[4:4] = [f"{scope['excluded_family']} settings are set aside from the main comparison. "
            f"[Archived settings and original records]({scope['archive_report']}) remain available; "
            "the structured report preserves all original scores and denominators.", ""]
    for row in rows:
        suffix = " / " + (row.get("dataset") or row.get("native_split") or "") if row.get("dataset") or row.get("native_split") else ""
        label = row["task_id"] + suffix + " " + row["task_name"].replace("LAB-Bench / ", "")
        if incomplete_evaluation(row, report): label += "*"
        caveats = " ".join(presentation_caveats(row))
        if row["completion_scope"] in {"dataset_component", "native_split_component"}: caveats = "Completed component. " + caveats
        if not caveats: caveats = "Declared local variant; input, training and scoring qualifications in linked result and JSON."
        lines.append("| " + " | ".join(map(cell, [f"[{label}]({score_href(row['source_scores'], root)})", local_display(row), published_display(row), caveats])) + " |")
    if any(incomplete_evaluation(row, report) for row in rows) or diagnostics:
        lines += ["", "\\* Incomplete benchmark coverage or scoring. Case counts and parsing details remain in the [structured report](RESULTS_AT_A_GLANCE.json)."]
    if not rows: lines += ["", "No verified terminal whole-run or dataset-component score is available yet."]
    if diagnostics:
        lines += ["", "Finished executions with undefined full-test metrics, excluded from benchmark completion counts:", ""]
        for row in diagnostics:
            lines.append(f"- [{row['task_id']} {row['task_name']}*]({score_href(row['source_scores'], root)}): "
                         f"{local_display(row)}. Parsed-only values are incomplete diagnostics and do not replace the native full-test score. "
                         + " ".join(presentation_caveats(row)))
    p43 = report["P43"]
    if p43["completed_components"]:
        lines += ["", "P43: " + ", ".join(p43["completed_components"]) + " component tests completed. " +
            ("All 3 tests have an exact 16,533-ID validated aggregate; each dataset's AUROC/AP remains separate." if p43["whole_setting_complete"] else "The whole setting remains incomplete until Human 1,200 + BioSNAP 5,493 + BindingDB 9,840 cases have a validated 16,533-ID union. No pooled score or mean of datasets is reported.")]
    audit = report["P29_seed_only_offline_audit"] if "P29" not in excluded else None
    if audit:
        parts = []
        for split, values in audit["splits"].items():
            parts.append(split.upper() + " " + format_value("F1", values.get("seed_context_only_native_augmented_mean_propagated_F1")) +
                " native / " + format_value("F1", values.get("seed_context_only_curated_mean_propagated_F1_diagnostic")) + " curated diagnostic")
        lines += ["", "Separate offline P29 input/reference audit, **not Qwen results**: " + "; ".join(parts) +
            ". Native targets include predictor-derived terms also supplied in context; this can reward recovery/copying and does not isolate novel function inference. Curated references also overlap predictor context. "
            "[Audit](POSTTRAIN_NATIVE_GAP_AUDIT.md)."]
    blockers = [b for b in report["blockers"] if set(b["task_ids"]) - excluded]
    if blockers:
        lines += ["", "Genuine source blockers: " + " ".join("[" + "/".join(task_id for task_id in b["task_ids"] if task_id not in excluded) + "](" + b["source_report"].removeprefix("reports/") + "): " + b["description"]
            + (" [Publisher release](" + b["publisher_url"] + ")." if b.get("publisher_url") else "") for b in blockers)]
    lines += ["", "Outcome scores do not validate explanations or identify internal reasoning; public pretraining exposure is unknown. Undefined metrics remain undefined. "
        "[Full coverage/provenance](LOCAL_SUITE_RESULTS.md) · [Structured concise report](RESULTS_AT_A_GLANCE.json).", ""]
    if report["warnings"]: lines += ["Snapshot metadata warnings: " + "; ".join(report["warnings"]), ""]
    return "\n".join(lines)


def write_report(root, report):
    outputs = {"reports/RESULTS_AT_A_GLANCE.json": json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False) + "\n",
               "reports/RESULTS_AT_A_GLANCE.md": render_markdown(report, root)}
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
