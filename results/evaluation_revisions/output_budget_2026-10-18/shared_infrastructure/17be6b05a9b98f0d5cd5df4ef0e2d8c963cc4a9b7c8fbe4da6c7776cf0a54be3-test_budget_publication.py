"""Synthetic-only publication tests; temporary local Git, no external calls."""
import ast
import copy
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import tarfile
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch
import urllib.parse

import publish_budget_revision as m

REAL_ROOT = Path(__file__).resolve().parents[3]
bridge = m.module("synthetic_budget_bridge", REAL_ROOT / ".local/shared_vllm_saturation_2026-10-18/publish_saturation_artifacts.py")
scanner = m.module("synthetic_budget_scanner", REAL_ROOT / "scripts/daily_backup.py")


def frozen_archive_helpers(state, remote):
    source = REAL_ROOT / ".local/remaining_evaluations/pool_supervisor_final_v2.py"
    tree = ast.parse(source.read_bytes())
    defs = [node for node in tree.body if isinstance(node, ast.FunctionDef)
            and node.name in {"new_trajectories", "archive_batch"}]
    namespace = {"HERE": state, "read": m.read, "save": m.write,
                 "worker": SimpleNamespace(digest=m.digest, sha=m.sha),
                 "tarfile": tarfile, "urllib": SimpleNamespace(parse=urllib.parse),
                 "remote": remote}
    exec(compile(ast.Module(body=defs, type_ignores=[]), "frozen_archive_helpers", "exec"), namespace)
    return SimpleNamespace(**{name: namespace[name] for name in ["new_trajectories", "archive_batch"]})


class Fixture:
    def __init__(self, root, count=2):
        self.root = root
        self.state = root / ".local/evaluation_revision_2026-10-18/publication"
        self.state.mkdir(parents=True)
        (self.state / "publish_budget_revision.py").write_text("# Synthetic publication source\n")
        self.budget = self.state.parent / "budget_queue"
        self.budget.mkdir()
        (self.budget / "run_budget_revision.py").write_text("# Synthetic execution source\n")
        self.original_id = "synthetic_p08_source"
        self.name = self.original_id + "_output16384_v1"
        self.folder = self.budget / "results/runs" / self.name
        self.project = root / "synthetic_project"
        self.project.mkdir()
        self.config = self.project / "config.json"
        self.old = {"run_id": self.original_id, "approved_task_ids": ["P08"], "model": m.MODEL,
                    "model_revision": m.REVISION, "variant": "SYNTHETIC_VARIANT",
                    "generation": {"max_tokens": 4096, "n": 1, "seed": 42}}
        m.write(self.config, self.old)
        self.new = copy.deepcopy(self.old)
        self.new["generation"]["max_tokens"] = 16384
        self.ids = ["artificial_case_" + str(i) for i in range(count)]
        self.parent = self.project / "results/runs" / self.original_id
        self.parent.mkdir(parents=True)
        (self.parent / "preserved.json").write_text('{"original_output":4096}\n')
        self.checkpoint = self.budget / "checkpoints/source.json"
        m.write(self.checkpoint, {"condition": m.CONDITION, "ambiguous_files": [],
              "ordered_pending_case_ids": self.ids, "original_source_run_id": self.original_id,
              "parent_run_directory": str(self.parent), "selection_uses_correctness_or_finish_reason": False})
        self.identity = self.budget / "server_identity.json"
        m.write(self.identity, {"synthetic_identity": "gpu_only_for_fixture"})
        entry = {"task_id": "P08", "run_id": self.original_id, "project_root": str(self.project),
                 "config_path": "config.json", "config_sha256": m.sha(self.config), "case_count": count + 1}
        self.item = {"entry": entry, "output_directory": str(self.folder), "selected_case_ids": self.ids,
                     "ordered_case_ids_sha256": m.digest(self.ids), "case_scope": "all_never_dispatched_at_clean_pause",
                     "parent_checkpoint": {"path": str(self.checkpoint), "sha256": m.sha(self.checkpoint)}}
        self.plan = {"kind": "explicit_output_budget_revision", "execution_authorized": True,
                     "condition": m.CONDITION, "model": m.MODEL, "model_revision": m.REVISION,
                     "output_budget": 16384, "original_output_budget": 4096,
                     "retries_or_resampling_of_previously_executed_cases": False,
                     "original_model_inputs_and_sampling_preserved_except_max_tokens": True,
                     "authorization_quote": "Synthetic explicit authorization",
                     "code_sha256": m.sha(self.budget / "run_budget_revision.py"),
                     "endpoints": [{"server_identity_file": str(self.identity), "server_identity_sha256": m.sha(self.identity)}],
                     "runs": [self.item]}
        self.plan_path = self.budget / "plan_new_pool.json"
        self.save_plan()
        self.plans, self.runs = m.load_runs(root, self.pins)
        self.spec = self.runs[self.name]
        m.write(self.folder / "run_manifest.json", {"condition": m.CONDITION, "aggregate_budget_condition": m.CONDITION,
              "plan_sha256": m.sha(self.plan_path), "planned_cases": count, "source_entry": entry,
              "configuration": self.new, "original_configuration": self.old,
              "parent_checkpoint": self.item["parent_checkpoint"], "parent_run_directory": str(self.parent),
              "original_artifacts_modified": False, "model_outcome_based_selection": False})

    def save_plan(self):
        m.write(self.plan_path, self.plan)
        self.pins = [{"path": str(self.plan_path), "sha256": m.sha(self.plan_path)}]

    def pair(self, index, receipt_complete=True):
        case_id = self.ids[index]
        name = m.digest(["P08", self.old["variant"], case_id]) + ".json"
        payload = {"model": m.MODEL, "messages": [{"role": "user", "content": "Invented scalar task"}], **self.new["generation"]}
        request = {"task": "P08", "variant": self.old["variant"], "case_id": case_id, "split": "synthetic",
                   "request_sha256": m.digest(payload), "payload": payload}
        m.write(self.folder / "requests" / name, request)
        response = {k: request[k] for k in ["task", "variant", "case_id", "split", "request_sha256"]}
        response.update(condition=m.CONDITION, model=m.MODEL, model_revision=m.REVISION,
                        status="completed", http_status=200, text="0.5", finish_reason="stop",
                        response={"model": m.MODEL, "choices": [{"message": {"content": "0.5", "reasoning": "Synthetic reasoning retained exactly"}, "finish_reason": "stop"}]})
        m.write(self.folder / "responses" / name, response)
        receipt = {"condition": m.CONDITION, "plan_sha256": m.sha(self.plan_path), "case_id": case_id,
                   "request_sha256": request["request_sha256"], "output_budget": 16384,
                   "server_identity_sha256": m.sha(self.identity)}
        if receipt_complete:
            receipt["response_sha256"] = m.sha(self.folder / "responses" / name)
        m.write(self.folder / "dispatch" / name, receipt)
        return name


class SyntheticPublicationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name).resolve()
        self.fixture = Fixture(self.root)

    def tearDown(self):
        self.temporary.cleanup()

    def test_exact_plan_and_manifest(self):
        self.assertTrue(m.validate_manifest(self.fixture.spec))
        manifest = self.fixture.folder / "run_manifest.json"
        value = m.read(manifest)
        value["configuration"]["generation"]["seed"] = 123
        m.write(manifest, value)
        with self.assertRaisesRegex(ValueError, "manifest differs"):
            m.validate_manifest(self.fixture.spec)

    def test_plan_pins_and_prospective_cohort(self):
        self.fixture.plan["runs"][0]["selected_case_ids"] = ["invented_unplanned_case"]
        self.fixture.save_plan()
        with self.assertRaisesRegex(ValueError, "Prospective cohort"):
            m.load_runs(self.root, self.fixture.pins)

    def test_excluded_tasks_cannot_enter_publisher(self):
        self.fixture.plan["runs"][0]["entry"]["task_id"] = "P28"
        self.fixture.save_plan()
        with self.assertRaisesRegex(ValueError, "retained reviewed task scope"):
            m.load_runs(self.root, self.fixture.pins)

    def test_response_receipt_race_is_deferred(self):
        name = self.fixture.pair(0, receipt_complete=False)
        helpers = frozen_archive_helpers(self.fixture.state, None)
        item = helpers.new_trajectories(self.fixture.folder, set(), False)[0]
        self.assertFalse(m.validate_pair(self.fixture.spec, item))
        receipt_path = self.fixture.folder / "dispatch" / name
        receipt = m.read(receipt_path)
        receipt["response_sha256"] = m.sha(self.fixture.folder / "responses" / name)
        m.write(receipt_path, receipt)
        self.assertTrue(m.validate_pair(self.fixture.spec, item))

    def test_wrong_budget_or_condition_rejected(self):
        name = self.fixture.pair(0)
        path = self.fixture.folder / "requests" / name
        req = m.read(path)
        req["payload"]["max_tokens"] = 4096
        req["request_sha256"] = m.digest(req["payload"])
        m.write(path, req)
        helpers = frozen_archive_helpers(self.fixture.state, None)
        with self.assertRaisesRegex(ValueError, "provenance mismatch"):
            helpers.new_trajectories(self.fixture.folder, set(), False)

    def test_identity_and_response_byte_checks(self):
        name = self.fixture.pair(0)
        helpers = frozen_archive_helpers(self.fixture.state, None)
        item = helpers.new_trajectories(self.fixture.folder, set(), False)[0]
        receipt_path = self.fixture.folder / "dispatch" / name
        receipt = m.read(receipt_path)
        receipt["server_identity_sha256"] = "0" * 64
        m.write(receipt_path, receipt)
        with self.assertRaisesRegex(ValueError, "GPU identity"):
            m.validate_pair(self.fixture.spec, item)

    def test_generation_marker_does_not_claim_scoring(self):
        m.write(self.fixture.folder / "generation_completion.json", {"condition": m.CONDITION,
                "plan_sha256": self.fixture.spec["plan_sha256"], "planned": 2,
                "statuses": {"completed": 2}, "generation_exit_code": 0, "scoring_performed": False})
        result = m.outcome(self.fixture.spec)
        self.assertTrue(result["generation_terminal"])
        self.assertFalse(result["scored_benchmark_completed"])
        self.assertIsNone(result["native_metrics_valid"])
        marker = m.read(self.fixture.folder / "generation_completion.json")
        marker["statuses"] = {"completed": 1}
        m.write(self.fixture.folder / "generation_completion.json", marker)
        with self.assertRaisesRegex(ValueError, "completion marker"):
            m.outcome(self.fixture.spec)

    def test_dispatch_archives_are_content_addressed_and_preserve_raw_bytes(self):
        name = self.fixture.pair(0)
        destination = self.root / "synthetic_export"
        m.publish_dispatch(self.fixture.spec, destination, [], bridge, scanner)
        row = m.read(destination / "dispatch_index.json")[0]
        archive = destination / row["archive"]
        before = archive.read_bytes()
        with tarfile.open(fileobj=io.BytesIO(before), mode="r:gz") as handle:
            self.assertEqual(handle.extractfile(row["member"]).read(), (self.fixture.folder / "dispatch" / name).read_bytes())
        m.publish_dispatch(self.fixture.spec, destination, [], bridge, scanner)
        self.assertEqual(before, archive.read_bytes())

    def test_check_only_uses_no_remote_or_git_calls(self):
        self.fixture.pair(0)
        helpers = frozen_archive_helpers(self.fixture.state, None)
        def forbidden(*args, **kwargs):
            self.fail("Check-only attempted an external mutation")
        helpers.helpers = SimpleNamespace(confirm_destination=forbidden)
        helpers.git = forbidden
        before = (self.fixture.parent / "preserved.json").read_bytes()
        with patch.object(m, "PINS", {}):
            result = m.publish_once(self.root, self.fixture.state, helpers, bridge, scanner, self.fixture.pins, check_only=True)
        self.assertFalse(result["remote_mutation_performed"])
        self.assertEqual(result["runs"][self.fixture.name]["ready_saved_pairs"], 1)
        self.assertEqual(before, (self.fixture.parent / "preserved.json").read_bytes())
        self.assertFalse((self.fixture.state / "upload_checkout").exists())

    def test_secret_scan_and_symlink_source_rejected(self):
        unsafe = self.root / "pretend.json"
        unsafe.write_text("ghp_" + "A" * 36)
        with self.assertRaises(scanner.BackupError):
            m.copy_pin(self.root, bridge, scanner, unsafe, self.root / "export.json")
        symlink = self.root / "redirect.json"
        symlink.symlink_to(unsafe)
        with self.assertRaisesRegex(ValueError, "owned directory"):
            m.owned(self.root, symlink)

    def test_native_archive_preserves_reasoning_and_reuses_verified_asset(self):
        name = self.fixture.pair(0)
        calls = []
        def api(url, method="GET", value=None, binary=None):
            self.assertEqual(method, "POST")
            calls.append(binary.read_bytes())
            return {"name": binary.name, "size": binary.stat().st_size, "digest": "sha256:" + m.sha(binary),
                    "id": 7, "browser_download_url": "https://example.invalid/" + binary.name}
        helpers = frozen_archive_helpers(self.fixture.state, SimpleNamespace(api=api))
        items = helpers.new_trajectories(self.fixture.folder, set(), False)
        destination = self.root / "archive_export"
        release = {"upload_url": "https://example.invalid/upload{?name,label}", "_part": 1}
        index = helpers.archive_batch(self.fixture.name, items, release, {}, destination)
        self.assertEqual(len(calls), 1)
        with tarfile.open(fileobj=io.BytesIO(calls[0]), mode="r:gz") as archive:
            self.assertEqual(archive.extractfile("responses/" + name).read(), (self.fixture.folder / "responses" / name).read_bytes())
        self.assertEqual(helpers.archive_batch(self.fixture.name, items, release, {}, destination), index)
        self.assertEqual(len(calls), 1)


class LocalGitIntegrationTests(unittest.TestCase):
    def test_new_alias_guards_preserve_original_paths(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary).resolve()
            fixture = Fixture(root)
            m.ensure_new_run_links(root, fixture.runs)
            link = root / "results/runs" / fixture.name
            self.assertTrue(link.is_symlink())
            self.assertEqual(link.resolve(), fixture.folder)
            m.ensure_new_run_links(root, fixture.runs)
            link.unlink()
            link.write_text("Existing path must survive\n")
            with self.assertRaisesRegex(ValueError, "existing original path"):
                m.ensure_new_run_links(root, fixture.runs)
            self.assertEqual(link.read_text(), "Existing path must survive\n")
            link.unlink()
            link.symlink_to(fixture.parent)
            with self.assertRaisesRegex(ValueError, "another source"):
                m.ensure_new_run_links(root, fixture.runs)

    def test_completed_derived_score_publishes_exact_metadata_without_raw_duplicates(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary).resolve()
            fixture = Fixture(root)
            name = fixture.original_id + "_mixed_4k16k_scoring_v1"
            folder = fixture.project / "results/runs" / name
            folder.mkdir()
            registry_path = fixture.state.parent / "scoring/watch_plan_v1.json"
            m.write(registry_path, {"synthetic_registry": True})
            watcher = registry_path.parent / "watcher_status_v1.json"
            m.write(watcher, {"tasks": {}})
            spec = {"task_id": "P08", "full_config_sha256": m.sha(fixture.config)}
            spec_path = registry_path.parent / "p08_mixed_scoring_v1.json"
            m.write(spec_path, spec)
            budget_path = folder / "per_case_budget_map.json"
            m.write(budget_path, {"condition": m.CONDITION, "budgets_by_raw_filename": {"a.json": 4096, "b.json": 16384}})
            cfg = copy.deepcopy(fixture.old)
            cfg.update(run_id=name, mixed_budget_scoring={"condition": m.CONDITION,
                       "original_full_configuration_sha256": spec["full_config_sha256"],
                       "per_case_budget_map": {"path": str(budget_path), "sha256": m.sha(budget_path)}})
            cfg_path = fixture.project / "configs" / (name + ".json")
            m.write(cfg_path, cfg)
            manifest = {"configuration": cfg, "configuration_sha256": m.sha(cfg_path),
                        "planned_cases": 2, "generation_budget_condition": m.CONDITION}
            m.write(folder / "run_manifest.json", manifest)
            scores = {"planned": 2, "completed": 2, "metrics": {"spearman": 0.75},
                      "generation_budget_condition": m.CONDITION,
                      "protocol_variant": fixture.old["variant"] + "__" + m.CONDITION,
                      "generation": {"output_budget_counts": {"4096": 1, "16384": 1}},
                      "native_parser_and_metric_implementation_unchanged": True,
                      "original_case_denominator_unchanged": True}
            m.write(folder / "scores.json", scores)
            m.write(folder / "native_scores_unmodified.json", {"metrics": {"spearman": 0.75}})
            m.write(folder / "mixed_scoring_spec.json", spec)
            m.write(folder / "per_case_scores.json", [{"case_id": "artificial_case_0"}, {"case_id": "artificial_case_1"}])
            m.write(folder / "mixed_budget_output_lock.json", {"spec_sha256": m.digest(spec),
                    "native_denominator": 2, "per_case_budget_map_sha256": m.sha(budget_path)})
            m.write(folder / "native_scorer_invocation.json", {"output_lock_sha256": m.sha(folder / "mixed_budget_output_lock.json")})
            (folder / "native_scorer.log").write_text("Synthetic successful scoring log\n")
            union = {"complete": True, "union_matches_full_test_ids": True,
                     "expected_test_case_count": 2, "unique_observed_case_count": 2,
                     "missing_case_count": 0, "extra_case_count": 0, "duplicate_case_count": 0}
            m.write(folder / "completion.json", {"condition": m.CONDITION, "spec_sha256": m.digest(spec),
                    "configuration_sha256": m.sha(cfg_path), "run_manifest_sha256": m.sha(folder / "run_manifest.json"),
                    "scores_sha256": m.sha(folder / "scores.json"), "full_test_id_union_validation": union,
                    "native_labels_and_denominator_unchanged": True, "retry_or_resampling": False,
                    "scoring_exit_code": 0, "generation_exit_code": 0})
            view = {"run_id": name, "task_id": "P08", "project_root": fixture.project, "folder": folder,
                    "planned": 2, "full": fixture.old, "spec": spec, "spec_path": spec_path,
                    "spec_sha256": m.sha(spec_path), "config_path": cfg_path}
            record = {"path": registry_path, "sha256": m.sha(registry_path),
                      "registry": {"code_files_sha256": {}, "state_file": str(watcher)}}
            m.write(folder / "responses" / "do_not_duplicate.json", {"synthetic_raw_output": True})
            native = SimpleNamespace(outcome_status=lambda value: {"native_metrics_valid": True})
            destination = root / "export"
            result = m.publish_scoring_views(root, fixture.state, record, {name: view}, destination, bridge, scanner, native)
            published = destination / "results/runs" / name
            self.assertTrue(result[name]["scored_benchmark_completed"])
            self.assertEqual((published / "scores.json").read_bytes(), (folder / "scores.json").read_bytes())
            self.assertEqual((published / "native_scorer.log").read_bytes(), (folder / "native_scorer.log").read_bytes())
            self.assertFalse((published / "responses").exists())
            m.ensure_new_run_links(root, {name: view})
            self.assertEqual((root / "results/runs" / name).resolve(), folder)
            bad = m.read(folder / "scores.json")
            bad["generation"]["output_budget_counts"] = {"16384": 2}
            m.write(folder / "scores.json", bad)
            with self.assertRaisesRegex(ValueError, "budget label"):
                m.derived_score_status(view)

    def test_publish_51_cases_in_two_batches_and_preserve_old_condition(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary).resolve()
            fixture = Fixture(root, count=51)
            for i in range(51):
                fixture.pair(i)
            old_bytes = (fixture.parent / "preserved.json").read_bytes()
            upstream = root / "local_upstream"
            upstream.mkdir()
            def git(where, *args, allow_failure=False, cwd=None):
                result = subprocess.run(["git", *args], cwd=cwd or where, text=True, capture_output=True)
                if result.returncode and not allow_failure:
                    raise RuntimeError(result.stderr)
                return result
            git(upstream, "init", "-q", "-b", "main")
            git(upstream, "config", "user.name", "Synthetic")
            git(upstream, "config", "user.email", "synthetic@example.invalid")
            old_public = upstream / "results/runs/original_4096/retained.json"
            old_public.parent.mkdir(parents=True)
            old_public.write_bytes(old_bytes)
            git(upstream, "add", ".")
            git(upstream, "commit", "-qm", "Original synthetic 4k results")
            # Permit pushes into this temporary non-bare repository for testing.
            git(upstream, "config", "receive.denyCurrentBranch", "updateInstead")
            uploads = []
            def api(url, method="GET", value=None, binary=None):
                self.assertEqual(method, "POST")
                uploads.append(binary.read_bytes())
                return {"name": binary.name, "size": binary.stat().st_size, "digest": "sha256:" + m.sha(binary),
                        "id": len(uploads), "browser_download_url": "https://example.invalid/" + binary.name}
            native = frozen_archive_helpers(fixture.state, SimpleNamespace(api=api))
            native.CHECKOUT = fixture.state / "upload_checkout"
            native.ROOT = upstream
            native.helpers = SimpleNamespace(URL=str(upstream), confirm_destination=lambda: {"visibility": "public", "destination_policy_sha256": "synthetic_policy"})
            native.git = lambda *args, **kwargs: git(native.CHECKOUT, *args, **kwargs)
            native.release = lambda: ({"upload_url": "https://example.invalid/upload{?name,label}", "_part": 1}, {})
            with patch.object(m, "PINS", {}):
                result = m.publish_once(root, fixture.state, native, bridge, scanner, fixture.pins)
                again = m.publish_once(root, fixture.state, native, bridge, scanner, fixture.pins)
            self.assertTrue(result["ready"])
            self.assertEqual(len(uploads), 2)
            counts = []
            for raw in uploads:
                with tarfile.open(fileobj=io.BytesIO(raw), mode="r:gz") as archive:
                    counts.append(len([x for x in archive if x.name.startswith("responses/")]))
            self.assertEqual(sorted(counts), [1, 50])
            self.assertEqual(result["commit_sha"], again["commit_sha"])
            self.assertEqual(old_public.read_bytes(), old_bytes)
            self.assertEqual((fixture.parent / "preserved.json").read_bytes(), old_bytes)
            published = upstream / "results/runs" / fixture.name
            self.assertEqual(len(m.read(published / "trajectory_index.json")), 51)
            self.assertEqual(m.read(published / "source_frozen_config_4096.json")["generation"]["max_tokens"], 4096)
            self.assertEqual(m.read(published / "frozen_config_16384.json")["generation"]["max_tokens"], 16384)
            self.assertIn(m.CONDITION, (published / "README.md").read_text())
            self.assertEqual(git(upstream, "status", "--porcelain").stdout.strip(), "")


if __name__ == "__main__":
    unittest.main()
