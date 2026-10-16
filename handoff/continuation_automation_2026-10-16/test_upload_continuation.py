"""Offline archive/alignment/privacy checks. No credentials or network calls."""
import copy
import importlib.util
import json
from pathlib import Path
import tarfile
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location("upload_continuation", Path(__file__).with_name("upload_continuation.py"))
u = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(u)


class UploadTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.project, self.run = self.root / "project", self.root / "run"
        self.project.mkdir(); self.run.mkdir()
        self.cases = [{"task": "P36", "variant": u.VARIANT, "case_id": "synthetic-" + str(i),
            "messages": [{"role": "user", "content": "Synthetic permitted fixture " + str(i)}]} for i in range(59)]
        self.config = {"task_id": "P36", "variant": u.VARIANT, "model": "Qwen/Qwen3.8-27B",
            "model_revision": u.REVISION, "generation": copy.deepcopy(u.GENERATION),
            "input_file": "inputs.jsonl", "review_file": "review.json",
            "case_contract_sha256": u.digest(self.cases), "frozen_files_sha256": {}}
        (self.project / "inputs.jsonl").write_text("".join(json.dumps(row) + "\n" for row in self.cases))
        u.write(self.project / "review.json", {"approved_case_ids": [row["case_id"] for row in self.cases],
            "full_source_case_count": 5876, "held_cases": []})
        self.path = self.project / "config.json"
        u.write(self.path, self.config)
        self.condition = u.load_condition(self.path, self.run)

    def tearDown(self):
        self.temp.cleanup()

    def trajectory(self, case_index=0, status="completed", response=True):
        filename, expected = list(self.condition["expected"].items())[case_index]
        payload = {"model": self.config["model"], "messages": self.cases[case_index]["messages"], **self.config["generation"]}
        record = {"task": "P36", "case_id": expected["case_id"], "variant": u.VARIANT,
            "model": self.config["model"], "model_revision": u.REVISION, "request_sha256": expected["payload_sha256"]}
        u.write(self.run / "requests" / filename, {**record, "payload": payload})
        if response:
            decoded = {"choices": [{"message": {"content": "synthetic final"}, "finish_reason": "length"}]}
            obj = {**record, "status": status, "http_status": 200, "saved_at_utc": "fixture",
                "raw_response_body": json.dumps(decoded)}
            if status == "completed":
                obj.update(response=decoded, text="synthetic final", finish_reason="length")
            u.write(self.run / "responses" / filename, obj)
        return filename

    def test_completed_error_and_pending_accounting(self):
        self.trajectory(0)
        self.trajectory(1, "error_or_unknown_completion_no_retry")
        self.trajectory(2, response=False)
        current = u.collect_trajectories(self.condition, terminal=False)
        self.assertEqual(len(current), 2)
        self.assertEqual(sum(row["complete_pair"] for row in current), 1)
        final = u.collect_trajectories(self.condition, terminal=True)
        self.assertEqual(len(final), 3)
        self.assertEqual(final[-1]["response_raw"] is None, final[-1]["filename"] == self.trajectory_filename(2))

    def trajectory_filename(self, index):
        return list(self.condition["expected"])[index]

    def test_request_response_alignment(self):
        filename = self.trajectory()
        path = self.run / "responses" / filename
        value = u.read(path); value["case_id"] = "another-case"; u.write(path, value)
        with self.assertRaises(u.ValidationError):
            u.collect_trajectories(self.condition, False)

    def test_payload_and_raw_response_tampering_rejected(self):
        filename = self.trajectory()
        request_path = self.run / "requests" / filename
        value = u.read(request_path); value["payload"]["messages"][0]["content"] = "changed"
        u.write(request_path, value)
        with self.assertRaises(u.ValidationError):
            u.collect_trajectories(self.condition, False)
        self.trajectory()
        response_path = self.run / "responses" / filename
        value = u.read(response_path); value["raw_response_body"] = "{}"; u.write(response_path, value)
        with self.assertRaises(u.ValidationError):
            u.collect_trajectories(self.condition, False)

    def test_deterministic_archive_and_member_hashes(self):
        files = {"requests/a.json": b'{"request":1}', "responses/a.json": b'{"response":1}'}
        first, manifest = u.pack_archive(self.root / "archives", "fixture", files)
        original = first.read_bytes()
        second, repeated = u.pack_archive(self.root / "other", "fixture", files)
        self.assertEqual(original, second.read_bytes())
        self.assertEqual(manifest, repeated)
        with tarfile.open(first) as archive:
            for row in manifest["files"]:
                self.assertEqual(u.sha(archive.extractfile(row["path"]).read()), row["sha256"])
        first.write_bytes(b"corrupt")
        with self.assertRaises(u.ValidationError):
            u.pack_archive(self.root / "archives", "fixture", files)
        with self.assertRaises(u.ValidationError):
            u.pack_archive(self.root / "archives", "fixture", {"../escape": b"x"})

    def test_immutable_manifests_and_previous_index(self):
        path = self.root / "manifest.json"
        u.write(path, {"value": 1}, immutable=True)
        with self.assertRaises(u.ValidationError):
            u.write(path, {"value": 2}, immutable=True)
        self.trajectory()
        rows = u.collect_trajectories(self.condition, False)
        index = [{key: value for key, value in row.items() if not key.endswith("_raw")} for row in rows]
        u.verify_existing_index(index, rows)
        changed = copy.deepcopy(rows); changed[0]["response_sha256"] = "changed"
        with self.assertRaises(u.ValidationError):
            u.verify_existing_index(index, changed)

    def test_unauthorized_and_no_permission_rejected_without_network(self):
        github = u.GitHub.__new__(u.GitHub)
        for value in ({"private": False, "push_permission": True, "publication_authorized": False},
                      {"private": False, "push_permission": False, "publication_authorized": True}):
            github.helpers = SimpleNamespace(confirm_destination=lambda: value)
            with self.assertRaises(u.ValidationError):
                github.private()

    def test_authorized_public_visibility_is_reported_truthfully(self):
        github = u.GitHub.__new__(u.GitHub)
        metadata = {"private": False, "visibility": "public", "push_permission": True, "publication_authorized": True}
        github.helpers = SimpleNamespace(confirm_destination=lambda: metadata)
        self.assertEqual(github.private(), metadata)

    def test_public_pointer_timestamp_is_stable_until_content_changes(self):
        payload = {"task_id": "P36", "uploaded_trajectories": 59, "scoring_success": True}
        previous = {**payload, "updated_at_utc": "2026-10-16T12:00:00+00:00", "commit_sha": "a" * 40}
        result = u.stable_publication_pointer(payload, previous)
        self.assertEqual(result["updated_at_utc"], previous["updated_at_utc"])
        changed = u.stable_publication_pointer({**payload, "scoring_success": False}, previous)
        self.assertNotEqual(changed["updated_at_utc"], previous["updated_at_utc"])

    def fake_push_client(self, staged="", ahead="0"):
        github = u.GitHub.__new__(u.GitHub)
        github.root, github.checkout = self.root, self.root / "checkout"
        calls = []
        def git(*args, **kwargs):
            calls.append(args)
            output = staged if args[0] == "diff" else ahead if args[0] == "rev-list" else "a" * 40
            return SimpleNamespace(stdout=output, returncode=0)
        github.git = git
        github.private = lambda: {"private": True, "push_permission": True}
        return github, calls

    def test_unchanged_publication_does_not_push_or_commit(self):
        github, calls = self.fake_push_client()
        self.assertEqual(github.push(), "a" * 40)
        self.assertFalse(github.published_this_cycle)
        self.assertFalse(any(row[0] in {"push", "commit", "fetch"} for row in calls))

    def test_unpushed_commit_is_retried_without_new_staged_files(self):
        github, calls = self.fake_push_client(ahead="1")
        github.push()
        self.assertTrue(github.published_this_cycle)
        self.assertTrue(any(row[0] == "push" for row in calls))

    def test_recent_original_backlog_defers_our_mutations(self):
        original = self.root / ".local/remaining_evaluations/supervisor_status.json"
        u.write(original, {"stage": "retry_pending", "updated_at_utc": u.stamp(),
                           "error": "Git push rejected (non-fast-forward)"})
        preserved = original.read_bytes()
        github, calls = self.fake_push_client(staged=u.RUN_POINTER.as_posix() + "/upload_status.json")
        with self.assertRaises(u.PublicationDeferred):
            github.push()
        self.assertFalse(any(row[0] in {"push", "commit", "fetch"} for row in calls))
        self.assertEqual(original.read_bytes(), preserved)

    def test_saved_scores_need_matching_output_lock(self):
        state = {"scoring_artifacts_present": True}
        u.write(self.run / "run_manifest.json", {"synthetic": "manifest"})
        locked = {"run_manifest.json": u.sha((self.run / "run_manifest.json").read_bytes())}
        locked.update({kind + "/" + name: None for name in self.condition["expected"]
            for kind in ("requests", "responses")})
        scores = {"task_id": "P36", "planned": 59, "full_source_cases": 5876,
            "protocol_variant": u.VARIANT, "model_revision": u.REVISION,
            "full_benchmark_complete": False, "metrics": {"rougeL": 0.2},
            "scoring_output_lock_sha256": u.digest(locked)}
        u.write(self.run / "scores.json", scores)
        u.write(self.run / "scoring_output_lock.json", {"files_sha256": locked,
            "contract_sha256": u.digest(locked)})
        u.write(self.run / "per_case_scores.json", [{"case_id": row["case_id"]} for row in self.cases])
        self.assertTrue(u.scoring_success(self.condition, state))
        u.write(self.run / "completion.json", {"scorer_exit_code": 1})
        self.assertFalse(u.scoring_success(self.condition, state))
        u.write(self.run / "completion.json", {"scorer_exit_code": 0, "status": "scoring_failed_no_retry"})
        self.assertFalse(u.scoring_success(self.condition, state))
        (self.run / "completion.json").unlink()
        (self.run / "run_manifest.json").write_text("late manifest")
        self.assertFalse(u.scoring_success(self.condition, state))

    def test_coordinator_declared_score_hash_is_required_to_match(self):
        u.write(self.run / "run_manifest.json", {"synthetic": "manifest"})
        locked = {"run_manifest.json": u.sha((self.run / "run_manifest.json").read_bytes())}
        locked.update({kind + "/" + name: None for name in self.condition["expected"]
            for kind in ("requests", "responses")})
        u.write(self.run / "scoring_output_lock.json", {"files_sha256": locked,
            "contract_sha256": u.digest(locked)})
        u.write(self.run / "per_case_scores.json", [{"case_id": row["case_id"]} for row in self.cases])
        u.write(self.run / "scores.json", {"task_id": "P36", "planned": 59,
            "full_source_cases": 5876, "protocol_variant": u.VARIANT,
            "model_revision": u.REVISION, "full_benchmark_complete": False,
            "metrics": {"rougeL": 0.2}, "scoring_output_lock_sha256": u.digest(locked)})
        raw = (self.run / "scores.json").read_bytes()
        u.write(self.run / "completion.json", {"scorer_exit_code": 0,
            "metadata": {"scores_sha256": u.sha(raw)}})
        state = {"scoring_artifacts_present": True}
        self.assertTrue(u.scoring_success(self.condition, state))
        # Even a JSON-equivalent byte change must fail the coordinator hash.
        (self.run / "scores.json").write_bytes(raw + b" ")
        self.assertFalse(u.scoring_success(self.condition, state))
        (self.run / "scores.json").write_bytes(raw)
        self.assertTrue(u.scoring_success(self.condition, state))

    def test_whole_offline_cycle_excludes_full_source_and_preserves_error_pair(self):
        self.trajectory(0, "error_or_unknown_completion_no_retry")
        self.trajectory(1, response=False)
        (self.project / "full_5876_case_source.json").write_text("DO NOT UPLOAD")
        (self.project / "input_review_index.jsonl").write_text("DO NOT UPLOAD")
        source = self.root / ".local/continuation_2026-10-16/source_prep/source_prep_bundle.tar.gz"
        source.parent.mkdir(parents=True); source.write_bytes(b"synthetic source bundle")
        class FakeGitHub:
            def __init__(self, root):
                self.checkout = root / "checkout"; self.scanner = SimpleNamespace(scan_file=lambda path: None)
                self.uploads = []
            def private(self):return {"private": True, "push_permission": True}
            def initialize(self):self.checkout.mkdir(exist_ok=True)
            def ensure_asset(self, path):
                self.uploads.append(path)
                return {"name": path.name, "asset_id": 1, "asset_url": "https://example.invalid/"+path.name,
                    "archive_sha256": u.sha(path.read_bytes()), "archive_bytes": path.stat().st_size}
            def push(self):return "a" * 40
        github = FakeGitHub(self.root)
        with patch.object(u, "SOURCE_SHA", u.sha(source.read_bytes())):
            status = u.upload_cycle(self.root, self.run, self.path, github)
        self.assertEqual(status["uploaded_error_response_pairs"], 1)
        self.assertEqual(status["uploaded_completed_pairs"], 0)
        pointer = u.read(self.root / u.RUN_POINTER / "upload_status.json")
        self.assertEqual(pointer["uploaded_trajectories"], 1)
        self.assertFalse(pointer["scoring_success"])
        self.assertFalse(pointer["full_benchmark_complete"])
        for archive in github.uploads:
            if archive == source:continue
            with tarfile.open(archive) as handle:
                self.assertFalse(any("full_5876" in name or "input_review_index" in name for name in handle.getnames()))
        self.assertEqual(len(u.read(github.checkout / u.RUN_POINTER / "trajectory_index.json")), 1)
        # A terminal scoring snapshot copies diagnostic fields verbatim too.
        u.write(self.run / "run_manifest.json", {"configuration": self.config,
            "configuration_sha256": self.condition["config_sha256"],
            "case_contract_sha256": self.config["case_contract_sha256"]})
        u.write(self.run / "dispatch_summary.json", {"planned": 59})
        locked = {"run_manifest.json": u.sha((self.run / "run_manifest.json").read_bytes())}
        for filename in self.condition["expected"]:
            for kind in ("requests", "responses"):
                path = self.run / kind / filename
                locked[kind + "/" + filename] = u.sha(path.read_bytes()) if path.is_file() else None
        lock = {"files_sha256": locked, "contract_sha256": u.digest(locked)}
        u.write(self.run / "scoring_output_lock.json", lock)
        u.write(self.run / "per_case_scores.json", [{"case_id": case["case_id"]} for case in self.cases])
        (self.run / "native_metric_output.tsv").write_text("synthetic scorer fixture\n")
        diagnostics = {"valid_native_serializations": 0, "completed": 0, "missing_or_failed_slots": 59,
            "finish_reasons": {"synthetic": 0}, "statuses": {"synthetic_error": 59}}
        scores = {"task_id": "P36", "planned": 59, "full_source_cases": 5876,
            "protocol_variant": u.VARIANT, "model_revision": u.REVISION,
            "full_benchmark_complete": False, "metrics": {"rougeL": 0.125},
            "scoring_output_lock_sha256": lock["contract_sha256"], **diagnostics}
        u.write(self.run / "scores.json", scores)
        with patch.object(u, "SOURCE_SHA", u.sha(source.read_bytes())):
            terminal = u.upload_cycle(self.root, self.run, self.path, github)
        self.assertTrue(terminal["scoring_success"])
        for field, value in diagnostics.items():
            self.assertEqual(terminal[field], value)


if __name__ == "__main__":
    unittest.main()
