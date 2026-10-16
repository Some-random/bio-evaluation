"""Reporting refresh follows terminal native metadata without touching execution."""
from __future__ import annotations

from datetime import datetime, timedelta, timezone
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/refresh_evaluation_reporting.py"
spec = importlib.util.spec_from_file_location("reporting_refresh", SCRIPT)
refresh = importlib.util.module_from_spec(spec)
spec.loader.exec_module(refresh)
NOW = datetime(2026, 10, 16, 9, tzinfo=timezone.utc)


def score(task_id, metric=0.5, scope="completed_declared_run", planned=1):
    return {"task_id": task_id, "task_name": "Original task " + task_id,
        "run_id": task_id + "_whole", "dataset": None,
        "completion_scope": scope, "case_scope": "full_frozen_reviewed_case_set",
        "counts": {"planned": planned, "completed": planned, "parsed": planned,
            "invalid_outputs": 0, "missing_or_failed_outputs": 0, "held_before_inference": 0},
        "metrics": {"spearman": metric}, "protocol_variant": "UNCHANGED_PROTOCOL",
        "selected_published_reference": {"display_model": "Paper model",
            "display_metrics": {"spearman": 0.75}, "source_url": "https://example.org/paper",
            "source_locator": "Table 2", "scope_note": "Different training"},
        "all_published_references": [{"model": "Paper model", "metrics": {"spearman": 0.75},
            "qualification": {"training": "supervised", "repeats": None}}],
        "caveats": ["Unchanged qualification"], "comparison_to_paper": "Context only",
        "source_scores": "results/runs/" + task_id + "/scores.json",
        "finished_at_utc": NOW.isoformat()}


def run(task_id, planned=2, uploaded=1, kind="shard_or_test", terminal=False, valid=None):
    return {"task_id": task_id, "kind": kind, "planned": planned,
        "uploaded_trajectories": uploaded, "terminal": terminal,
        "execution_success": terminal, "native_metrics_valid": valid}


class RefreshTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.ids = ["P01", "P03", "P06", "P18", "B06", "P19"]
        groups = []
        for index, task_id in enumerate(self.ids):
            state = "Deferred / held" if task_id in {"P18", "B06"} else "Source-blocked" if task_id == "P19" else "Status unverified"
            groups.append({"id": "main-" + str(index), "category": "Original category",
                "task": "Original biological task", "dataset": "Original dataset " + task_id,
                "kind": "main", "scope": "Registered", "status": state,
                "taskIds": [task_id], "notes": ["Preserve this qualification"],
                "literatureText": "Paper result with original caveat", "sourceSize": "Published n=99",
                "customMetadata": {"unknownKey": [1, None, "preserve"]}, "results": [],
                "protocols": [{"taskId": task_id, "title": "Protocol " + task_id,
                    "status": state, "blocker": "Original blocker" if task_id == "P19" else None,
                    "evidenceUrl": "https://example.org/evidence", "nativeMetric": "Spearman",
                    "limitation": "Never broaden this protocol"}]})
        groups.append({"id": "catalog-only", "taskIds": [], "status": "Status unverified",
            "category": "Original category", "scope": "Catalog only", "results": [], "protocols": [],
            "notes": ["Catalog inclusion is not execution evidence"]})
        self.catalog = {"meta": {"registrySettings": len(self.ids), "githubUrl": "https://github.com/example/evals",
            "sourceHashes": {"original-inventory.csv": "unchanged"}, "qualityNotes": ["Preserve"]},
            "categories": [{"name": "Original category", "count": 7}], "groups": groups,
            "runs": [], "modelNotes": ["Original BF16"], "statusLegend": {"Partial": "Original meaning"}}
        self.report = {"generated_at_utc": (NOW - timedelta(hours=1)).isoformat(),
            "completed_whole_declared_setting_ids": ["P01"], "completed_rows": [score("P01")],
            "diagnostic_only_finished_runs": [score("P06", None, "diagnostic_only_primary_metrics_invalid")],
            "blockers": [{"task_ids": ["P19"], "description": "Verified missing release", "source_report": "reports/blocker.md"}]}
        self.status = {"updated_at_utc": NOW.isoformat(), "stage": "watching", "commit_sha": "abc123",
            "repository_private_verified": True, "registry_sealed": True, "all_terminal": False,
            "all_successful_native_metrics": False,
            "runs": {"shard0": run("P03"), "shard1": run("P03"),
                "aggregate": run("P03", 4, 4, "aggregate"),
                "full-test": run("P01", 1, 1, "full_test", True, True)},
            "scheduler": [{"job_id": "11", "state": "RUNNING"}, {"job_id": "12", "state": "PENDING"},
                {"job_id": "99", "state": "RUNNING", "partition": "il-cpu", "gpu_count": 0}]}
        self.write_inputs()

    def tearDown(self):
        self.temp.cleanup()

    def write(self, relative, value):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(refresh.encoded(value))

    def write_inputs(self):
        self.write(refresh.CATALOG, self.catalog)
        self.write(refresh.SCORES, self.report)
        self.write(refresh.SUPERVISOR, self.status)

    def build(self, now=NOW):
        outputs = refresh.build_outputs(self.root, now)
        return json.loads(outputs[refresh.CATALOG]), json.loads(outputs[refresh.PROGRESS])

    def group(self, catalog, task_id):
        return next(group for group in catalog["groups"] if task_id in group["taskIds"])

    def test_aggregate_excluded_full_test_included_and_upload_not_saved(self):
        catalog, progress = self.build()
        self.assertEqual(progress["totals"], {"planned": 5, "uploaded": 3, "saved": None,
            "scheduledSettings": 2, "generationRuns": 3})
        self.assertEqual(progress["scheduler"]["activeWorkers"], 1)
        p03 = next(task for task in progress["tasks"] if task["taskId"] == "P03")
        self.assertEqual(p03["planned"], 4)
        self.assertEqual(p03["uploaded"], 2)
        self.assertIsNone(catalog["meta"]["savedResponses"])
        self.assertTrue(all(row["completed"] is None for row in catalog["runs"]))
        self.assertEqual(self.group(catalog, "P03")["status"], "Running / queued")

    def test_future_whole_task_score_maps_without_catalog_regeneration(self):
        self.report["completed_rows"].append(score("P03", 0.123456789, planned=4))
        self.report["completed_whole_declared_setting_ids"].append("P03")
        self.report["generated_at_utc"] = NOW.isoformat()
        for name in ["shard0", "shard1", "aggregate"]:
            self.status["runs"][name]["terminal"] = True
            self.status["runs"][name]["native_metrics_valid"] = True
        self.write_inputs()
        catalog, _ = self.build()
        group = self.group(catalog, "P03")
        self.assertEqual(group["status"], "Results available")
        self.assertEqual(group["protocols"][0]["status"], "Results available")
        self.assertEqual(group["results"][0]["metrics"], {"spearman": 0.123456789})
        self.assertEqual(catalog["meta"]["completedSettings"], 2)
        self.assertEqual(catalog["meta"]["localResultRows"], 3)

    def test_catalog_metadata_and_published_metrics_remain_exact(self):
        catalog, _ = self.build()
        self.assertEqual(catalog["categories"], self.catalog["categories"])
        self.assertEqual(catalog["modelNotes"], self.catalog["modelNotes"])
        for before, after in zip(self.catalog["groups"], catalog["groups"]):
            self.assertEqual({key: value for key, value in before.items() if key not in {"results", "status", "protocols"}},
                {key: value for key, value in after.items() if key not in {"results", "status", "protocols"}})
            for old, new in zip(before["protocols"], after["protocols"]):
                for key in ["taskId", "title", "nativeMetric", "limitation"]:
                    self.assertEqual(old[key], new[key])
        result = self.group(catalog, "P01")["results"][0]
        self.assertEqual(result["metrics"], self.report["completed_rows"][0]["metrics"])
        self.assertEqual(result["publishedReferences"], self.report["completed_rows"][0]["all_published_references"])
        self.assertEqual(result["caveats"], ["Unchanged qualification"])
        for task_id in ["B06", "P18"]:
            self.assertEqual(self.group(catalog, task_id)["status"], "Deferred / held")
        self.assertEqual(self.group(catalog, "P19")["protocols"][0]["blocker"], "Verified missing release")

    def test_finished_shards_and_invalid_primary_never_complete_task(self):
        for record in self.status["runs"].values():
            record["terminal"] = True
        self.status["runs"]["aggregate"]["native_metrics_valid"] = False
        # Even an inconsistent completion-ID entry cannot promote a null metric.
        self.report["completed_whole_declared_setting_ids"].append("P06")
        self.write_inputs()
        catalog, _ = self.build()
        self.assertEqual(self.group(catalog, "P03")["status"], "Partial")
        self.assertEqual(self.group(catalog, "P06")["status"], "Partial")
        self.assertTrue(self.group(catalog, "P06")["results"][0]["incomplete"])
        self.assertIsNone(self.group(catalog, "P06")["results"][0]["metrics"]["spearman"])
        self.assertEqual(catalog["meta"]["completedSettings"], 1)

    def test_optional_undefined_diagnostic_does_not_undo_native_validation(self):
        # The native report has already distinguished required primary metrics
        # from optional diagnostic fields; preserve that decision and nulls.
        self.report["completed_rows"][0]["metrics"] = {
            "qualified_oracle_success": 0.0, "optional_novelty": None}
        self.write_inputs()
        catalog, _ = self.build()
        self.assertEqual(catalog["meta"]["completedSettings"], 1)
        self.assertEqual(self.group(catalog, "P01")["results"][0]["metrics"], {
            "qualified_oracle_success": 0.0, "optional_novelty": None})

    def test_missing_and_stale_heartbeat_are_explicit(self):
        _, progress = self.build(NOW + timedelta(seconds=301))
        self.assertEqual(progress["heartbeat"]["status"], "stale")
        del self.status["updated_at_utc"]
        self.write_inputs()
        _, progress = self.build()
        self.assertEqual(progress["heartbeat"]["status"], "missing")

    def test_retry_receipt_uses_last_successful_upload_snapshot_and_original_time(self):
        original_time = (NOW - timedelta(minutes=2)).isoformat()
        self.status["updated_at_utc"] = original_time
        self.write(refresh.UPLOAD, self.status)
        retry = {"stage": "retry_pending", "updated_at_utc": NOW.isoformat(),
            "error": "Do not publish raw credential or subprocess details SECRET_SENTINEL"}
        self.write(refresh.SUPERVISOR, retry)
        catalog, progress = self.build()
        self.assertEqual(progress["totals"]["planned"], 5)
        self.assertEqual(progress["totals"]["uploaded"], 3)
        self.assertEqual(progress["scheduler"]["activeWorkers"], 1)
        self.assertEqual(progress["heartbeat"], {"status": "fresh", "updatedAt": original_time,
            "staleAfterSeconds": refresh.HEARTBEAT_LIMIT})
        self.assertEqual(progress["runSnapshotAt"], original_time)
        self.assertEqual(progress["runSnapshotSource"]["path"], refresh.UPLOAD)
        self.assertTrue(progress["runSnapshotSource"]["fallback"])
        self.assertEqual(progress["uploader"]["stage"], "retry_pending")
        self.assertEqual(progress["metadataNotice"]["updatedAt"], NOW.isoformat())
        self.assertNotIn("SECRET_SENTINEL", json.dumps(progress))
        self.assertNotIn("SECRET_SENTINEL", json.dumps(catalog))
        self.assertEqual(progress["sourceHashes"][refresh.UPLOAD], refresh.digest((self.root / refresh.UPLOAD).read_bytes()))
        _, later = self.build(NOW + timedelta(seconds=181))
        self.assertEqual(later["heartbeat"]["status"], "stale")
        self.assertEqual(later["heartbeat"]["updatedAt"], original_time)

    def test_newest_valid_run_snapshot_wins_and_bad_supervisor_falls_back(self):
        self.status["updated_at_utc"] = (NOW - timedelta(minutes=1)).isoformat()
        self.write(refresh.UPLOAD, self.status)
        self.status["updated_at_utc"] = (NOW - timedelta(minutes=10)).isoformat()
        self.write(refresh.SUPERVISOR, self.status)
        _, progress = self.build()
        self.assertEqual(progress["runSnapshotSource"]["path"], refresh.UPLOAD)
        (self.root / refresh.SUPERVISOR).write_text('{broken')
        _, progress = self.build()
        self.assertEqual(progress["totals"]["planned"], 5)
        self.assertEqual(progress["runSnapshotSource"]["path"], refresh.UPLOAD)
        self.assertEqual(progress["metadataErrors"], [{"source": refresh.SUPERVISOR, "reason": "no_valid_run_snapshot"}])

    def test_both_invalid_or_missing_sources_preserve_existing_outputs(self):
        refresh.refresh(self.root, now=NOW)
        paths = [self.root / refresh.CATALOG, self.root / refresh.PROGRESS]
        before = [(path.read_bytes(), path.stat().st_mtime_ns) for path in paths]
        self.write(refresh.SUPERVISOR, {"stage": "retry_pending", "updated_at_utc": NOW.isoformat()})
        (self.root / refresh.UPLOAD).parent.mkdir(parents=True, exist_ok=True)
        (self.root / refresh.UPLOAD).write_text('{broken')
        with self.assertRaisesRegex(ValueError, "No valid run-bearing"):
            refresh.refresh(self.root, now=NOW)
        self.assertEqual([(path.read_bytes(), path.stat().st_mtime_ns) for path in paths], before)
        (self.root / refresh.SUPERVISOR).unlink()
        (self.root / refresh.UPLOAD).unlink()
        with self.assertRaisesRegex(ValueError, "No valid run-bearing"):
            refresh.refresh(self.root, now=NOW)
        self.assertEqual([(path.read_bytes(), path.stat().st_mtime_ns) for path in paths], before)

    def test_idempotent_clock_changes_and_check_writes_nothing(self):
        original = (self.root / refresh.CATALOG).read_bytes()
        self.assertTrue(refresh.refresh(self.root, check=True, now=NOW))
        self.assertEqual((self.root / refresh.CATALOG).read_bytes(), original)
        self.assertFalse((self.root / refresh.PROGRESS).exists())
        self.assertTrue(refresh.refresh(self.root, now=NOW))
        paths = [self.root / refresh.CATALOG, self.root / refresh.PROGRESS]
        stamps = [path.stat().st_mtime_ns for path in paths]
        self.assertEqual(refresh.refresh(self.root, now=NOW + timedelta(seconds=30)), [])
        self.assertEqual([path.stat().st_mtime_ns for path in paths], stamps)
        progress_raw = (self.root / refresh.PROGRESS).read_bytes()
        catalog = json.loads((self.root / refresh.CATALOG).read_bytes())
        self.assertEqual(catalog["meta"]["sourceHashes"][refresh.PROGRESS], refresh.digest(progress_raw))

    def test_unmapped_score_fails_before_any_write(self):
        self.report["completed_rows"].append(score("P99"))
        self.write_inputs()
        before = (self.root / refresh.CATALOG).read_bytes()
        with self.assertRaisesRegex(ValueError, "unmapped"):
            refresh.refresh(self.root, now=NOW)
        self.assertEqual((self.root / refresh.CATALOG).read_bytes(), before)
        self.assertFalse((self.root / refresh.PROGRESS).exists())


if __name__ == "__main__":
    unittest.main()
