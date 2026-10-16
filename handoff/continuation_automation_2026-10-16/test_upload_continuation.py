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

    def test_nonprivate_and_no_permission_rejected_without_network(self):
        github = u.GitHub.__new__(u.GitHub)
        for value in ({"private": False, "push_permission": True}, {"private": True, "push_permission": False}):
            github.helpers = SimpleNamespace(confirm_private=lambda: value)
            with self.assertRaises(u.ValidationError):
                github.private()

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
        (self.run / "run_manifest.json").write_text("late manifest")
        self.assertFalse(u.scoring_success(self.condition, state))

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


if __name__ == "__main__":
    unittest.main()
