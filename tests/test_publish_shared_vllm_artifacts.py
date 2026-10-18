"""Publication preserves immutable bytes and separates physical/logical runs."""

import importlib.util
import io
import json
from pathlib import Path
import subprocess
import tarfile
import tempfile
from types import SimpleNamespace
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("publish_shared_vllm_artifacts", ROOT / "scripts/publish_shared_vllm_artifacts.py")
PUBLICATION = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PUBLICATION)
SCANNER = PUBLICATION.module("test_shared_publication_scanner", ROOT / "scripts/daily_backup.py")


class PublicationTests(unittest.TestCase):
    def test_whitespace_exception_requires_pinned_exact_staged_upstream_bytes(self):
        with tempfile.TemporaryDirectory() as temporary:
            checkout = Path(temporary)
            def git(*args, allow_failure=False):
                result = subprocess.run(["git", *args], cwd=checkout, capture_output=True, text=True)
                if result.returncode and not allow_failure:
                    raise RuntimeError(result.stderr)
                return result
            git("init", "-q")
            git("config", "core.autocrlf", "false")
            raw = b"Original upstream spacing must remain exact.  \n"
            digest = PUBLICATION.hashlib.sha256(raw).hexdigest()
            relative = "results/runs/run/shared_infrastructure/" + digest + "-upstream.txt"
            path = checkout / relative
            path.parent.mkdir(parents=True)
            path.write_bytes(raw)
            git("add", "--", relative)
            native = SimpleNamespace(CHECKOUT=checkout, git=git)
            self.assertEqual(PUBLICATION.check_staged_whitespace(native, [relative]), [relative])
            self.assertEqual(path.read_bytes(), raw)
            self.assertEqual(git("show", ":" + relative).stdout.encode(), raw)
            generated = "results/runs/run/generated.txt"
            (checkout / generated).write_bytes(b"New code must pass normal whitespace checks.  \n")
            git("add", "--", generated)
            with self.assertRaisesRegex(ValueError, "outside an immutable"):
                PUBLICATION.check_staged_whitespace(native, [relative, generated])
            git("rm", "--cached", "--", generated)
            path.write_bytes(b"Changed frozen bytes.  \n")
            git("add", "--", relative)
            with self.assertRaisesRegex(ValueError, "differs from its source or staged blob"):
                PUBLICATION.check_staged_whitespace(native, [relative])

    def test_dry_run_checks_frozen_jsonl_evidence_without_remote_or_checkout_writes(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary).resolve()
            source = root / "project/results/runs/run"
            config = root / "project/config.json"
            PUBLICATION.write(config, {"frozen_files_sha256": {}})
            metrics = root / "pool/closed_live_metrics.jsonl"
            metrics.parent.mkdir()
            metrics.write_text('{"running":1,"waiting":0}\n')
            amendment = root / "amendment.json"
            PUBLICATION.write(amendment, {"kind": "shared_vllm_infrastructure_amendment", "execution_authorized": True,
                "scientific_protocol_changes": [], "capacity_evidence_files": [{"path": str(metrics), "sha256": PUBLICATION.sha(metrics)}]})
            PUBLICATION.write(source / "shared_vllm_amendment.json", {"run_id": "run", "amendment_path": str(amendment), "amendment_sha256": PUBLICATION.sha(amendment)})
            PUBLICATION.write(root / "supervisor_plan.json", {})
            spec = {"run_id": "run", "task_id": "P08", "project_root": root / "project", "folder": source,
                    "planned": 1, "kind": "shard_or_test", "config_path": config}
            native = SimpleNamespace(HERE=root, read=PUBLICATION.read, validate_registry=lambda unused: ({}, {"run": spec}), METADATA=())
            receipt = PUBLICATION.publish_once(root, native, SCANNER, root / "pool", dry_run=True, amendment_path=amendment)
            self.assertTrue(receipt["validated_pinned_dependencies"])
            self.assertFalse(receipt["remote_mutation_performed"])
            self.assertFalse((root / "results").exists())
            metrics.write_text('{"running":2,"waiting":0}\n')
            with self.assertRaisesRegex(ValueError, "Pinned publication dependency changed"):
                PUBLICATION.publish_once(root, native, SCANNER, root / "pool", dry_run=True, amendment_path=amendment)

    def test_request_only_upgrade_is_unique_and_saved_response_is_immutable(self):
        original = {"filename": "case.json", "request_sha256": "request", "response_sha256": None, "asset": "old-asset", "archive_sha256": "old-archive", "request_member": "requests/case.json"}
        incoming = {**original, "response_sha256": "response", "asset": "new-asset"}
        merged = PUBLICATION.merge_index([original], [incoming])
        self.assertEqual(len(merged), 1)
        self.assertEqual(merged[0]["response_sha256"], "response")
        self.assertEqual(merged[0]["previous_request_only_archive"]["asset"], "old-asset")
        with self.assertRaisesRegex(ValueError, "response bytes"):
            PUBLICATION.merge_index(merged, [{**incoming, "response_sha256": "changed"}])
        with self.assertRaisesRegex(ValueError, "request bytes"):
            PUBLICATION.merge_index(merged, [{**incoming, "request_sha256": "changed"}])

    def test_receipt_bundles_keep_exact_bytes_and_pending_provenance(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source, destination = root / "source", root / "published"
            directory = source / "shared_vllm_dispatch"
            directory.mkdir(parents=True)
            raw = b'{"filename":"a.json", "status":"response_saved", "extra":"exact spacing"}\n'
            (directory / "a.json").write_bytes(raw)
            (directory / "b.json").write_text('{"filename":"b.json","status":"request_saved"}\n')
            index = [{"filename": "a.json", "archive_sha256": "raw-archive"}]
            self.assertTrue(PUBLICATION.publish_dispatch(source, destination, index, SCANNER))
            published = PUBLICATION.read(destination / "shared_vllm_dispatch_index.json")
            self.assertEqual(len(published), 2)
            a = next(row for row in published if row["filename"] == "a.json")
            with tarfile.open(destination / a["archive"], "r:gz") as archive:
                self.assertEqual(archive.extractfile(a["member"]).read(), raw)
            self.assertIn("pending", next(row for row in published if row["filename"] == "b.json")["archive"])
            self.assertFalse(PUBLICATION.publish_dispatch(source, destination, index, SCANNER))
            self.assertEqual(PUBLICATION.metadata_archive({"a.json": raw}), PUBLICATION.metadata_archive({"a.json": raw}))

    def test_continuation_storage_preserves_logical_source_and_marker_semantics(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            original = root / "results/runs/original"
            derived = root / "results/runs/original_shared_continuation_v1"
            derived.mkdir(parents=True)
            spec = {"run_id": "original", "task_id": "P08", "project_root": root, "folder": original, "planned": 2, "kind": "shard_or_test", "config_path": root / "config.json"}
            runs = PUBLICATION.add_continuation_runs({"original": spec}, {"continuation_run_directories": {"original": str(derived)}})
            continuation = runs[derived.name]
            self.assertEqual(continuation["logical_run_id"], "original")
            self.assertEqual(continuation["config_path"], spec["config_path"])
            self.assertTrue(runs["original"]["retained_partial_source"])
            PUBLICATION.write(derived / "shared_vllm_amendment.json", {"amendment_sha256": "amendment"})
            PUBLICATION.write(derived / "shared_vllm_generation_completion.json", {"run_id": "original", "planned": 2, "amendment_sha256": "amendment", "generation_exit_code": 0, "statuses": {"completed": 2}})
            result = PUBLICATION.generation_outcome(SimpleNamespace(), continuation)
            self.assertTrue(result["generation_terminal"])
            self.assertTrue(result["execution_success"])
            self.assertIsNone(result["native_metrics_valid"])

    def test_scoring_view_keeps_native_protocol_and_external_runner_copy_is_pinned(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            project = root / "project"
            config_path = project / "configs/original.json"
            original = {"run_id": "original", "model": "fixed-model", "runner": "scripts/old.py", "frozen_files_sha256": {}, "temperature": 1}
            PUBLICATION.write(config_path, original)
            spec = {"task_id": "P12", "run_id": "original", "project_root": project, "config_path": config_path, "folder": project / "results/runs/original", "planned": 2, "kind": "full_test"}
            code = root / "actual_runner.py"
            code.write_text("# Synthetic fixture, not an inference runner\n")
            view = {**original, "run_id": "original_shared_scoring", "runner": "../actual_runner.py", "frozen_files_sha256": {"../actual_runner.py": PUBLICATION.sha(code)}, "shared_vllm_scoring_view": {"original_run_id": "original", "original_configuration_sha256": PUBLICATION.sha(config_path)}}
            view_path = project / "configs/original_shared_scoring.json"
            PUBLICATION.write(view_path, view)
            selected = PUBLICATION.add_scoring_views({"original": spec})[view["run_id"]]
            destination = root / "published"
            self.assertTrue(PUBLICATION.publish_dependencies(root, selected, destination, SCANNER))
            manifest = PUBLICATION.read(destination / "shared_frozen_dependencies_manifest.json")
            self.assertEqual((destination / manifest["../actual_runner.py"]["browsable_copy"]).read_bytes(), code.read_bytes())
            view["temperature"] = 2
            PUBLICATION.write(view_path, view)
            with self.assertRaisesRegex(ValueError, "biological configuration"):
                PUBLICATION.add_scoring_views({"original": spec})


if __name__ == "__main__":
    unittest.main()
