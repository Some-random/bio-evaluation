"""Exercise private report publication against local bare repositories only."""
from __future__ import annotations

import importlib.util
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest


SCRIPT = Path(os.environ.get("WATCHER_UNDER_TEST", Path(__file__).resolve().parents[1] / "scripts/watch_evaluation_reporting.py"))
spec = importlib.util.spec_from_file_location("reporting_watch", SCRIPT)
watch = importlib.util.module_from_spec(spec)
spec.loader.exec_module(watch)


def git(cwd, *args):
    return subprocess.run(["git", *args], cwd=cwd, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True).stdout.strip()


class Helper:
    def __init__(self, url):
        self.URL = str(url)
        self.private = True
        self.calls = []
        self.privacy_checks = 0
        self.before_push = None
        self.before_add = None

    def confirm_private(self):
        self.privacy_checks += 1
        return {"private": self.private, "push_permission": True}

    def git(self, *args, cwd, allow_failure=False):
        self.calls.append(args)
        if args[0] == "push" and self.before_push is not None:
            hook, self.before_push = self.before_push, None
            hook()
        if args[0] == "add" and self.before_add is not None:
            hook, self.before_add = self.before_add, None
            hook(cwd)
        return subprocess.run(["git", *args], cwd=cwd, text=True,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)


class Scanner:
    def __init__(self):
        self.scanned = []

    def scan_file(self, path):
        self.scanned.append(path)
        if b"SECRET_TEST" in path.read_bytes():
            raise RuntimeError("SECRET_TEST should never appear in the receipt")


class WatchTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.base = Path(self.temp.name)
        self.root = self.base / "workspace"
        self.root.mkdir()
        self.remote = self.base / "remote.git"
        git(self.base, "init", "--bare", "--initial-branch=main", str(self.remote))
        self.seed = self.base / "seed"
        git(self.base, "clone", str(self.remote), str(self.seed))
        git(self.seed, "config", "user.name", "Test")
        git(self.seed, "config", "user.email", "test@localhost")
        for name in watch.OWNED:
            path = self.seed / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("Original upstream " + name + "\n")
            local = self.root / name
            local.parent.mkdir(parents=True, exist_ok=True)
            local.write_text("Generated " + name + "\n")
        self.progress = {"scoreSnapshotAt": "2026-10-16T08:00:00+00:00",
            "runSnapshotAt": "2026-10-16T09:00:00+00:00", "heartbeat": {"status": "fresh"},
            "totals": {"planned": 100, "uploaded": 25, "saved": None}}
        (self.root / watch.OWNED[0]).write_text(json.dumps(self.progress))
        git(self.seed, "add", ".")
        git(self.seed, "commit", "-m", "Initial reports")
        git(self.seed, "push", "origin", "main")
        self.helper = Helper(self.remote)
        self.scanner = Scanner()
        self.commands = []

    def tearDown(self):
        self.temp.cleanup()

    def runner(self, argv):
        self.commands.append(argv)

    def publisher(self, **kwargs):
        return watch.Publisher(self.root, helper=self.helper, scanner=self.scanner,
            runner=kwargs.pop("runner", self.runner), **kwargs)

    def remote_head(self):
        return git(self.remote, "rev-parse", "refs/heads/main")

    def upstream_change(self, name, content):
        git(self.seed, "pull", "--ff-only", "origin", "main")
        path = self.seed / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
        git(self.seed, "add", "--", name)
        git(self.seed, "commit", "-m", "Independent upstream change")
        git(self.seed, "push", "origin", "main")

    def test_exact_owned_paths_private_scan_and_idempotent_commit(self):
        original = self.remote_head()
        publisher = self.publisher()
        receipt = publisher.cycle()
        first = self.remote_head()
        self.assertNotEqual(first, original)
        self.assertTrue(receipt["pushed"])
        self.assertEqual(set(receipt["changedPaths"]), set(watch.OWNED))
        self.assertEqual(len(self.scanner.scanned), len(watch.OWNED))
        self.assertGreaterEqual(self.helper.privacy_checks, 2)
        self.assertEqual(git(self.remote, "diff", "--name-only", original, first).splitlines(), sorted(watch.OWNED))
        self.assertTrue(any("--check" in command for command in self.commands))
        self.assertEqual(publisher.checkout, self.root / ".local/reporting_updater/upload_checkout")
        self.assertFalse((self.root / ".local/remaining_evaluations/upload_checkout").exists())
        second = self.publisher().cycle()
        self.assertFalse(second["pushed"])
        self.assertEqual(self.remote_head(), first)
        self.assertEqual(set(second["baselineBlobs"]), set(watch.OWNED))
        self.assertFalse(any("--force" in call for call in self.helper.calls if call[0] == "push"))

    def test_timestamp_and_retry_hash_changes_do_not_create_commits(self):
        self.progress.update(metadataNotice={"stage": "retry_pending", "updatedAt": "2026-10-16T12:00:00+00:00"},
            sourceHashes={".local/remaining_evaluations/supervisor_status.json": "old"})
        (self.root / watch.OWNED[0]).write_text(json.dumps(self.progress))
        self.publisher().cycle()
        head = self.remote_head()
        self.progress["metadataNotice"]["updatedAt"] = "2026-10-16T13:00:00+00:00"
        self.progress["sourceHashes"][".local/remaining_evaluations/supervisor_status.json"] = "new"
        (self.root / watch.OWNED[0]).write_text(json.dumps(self.progress))
        receipt = self.publisher().cycle()
        self.assertFalse(receipt["pushed"])
        self.assertTrue(receipt["metadataOnlyRefreshSkipped"])
        self.assertEqual(self.remote_head(), head)
        self.progress["totals"]["uploaded"] += 1
        (self.root / watch.OWNED[0]).write_text(json.dumps(self.progress))
        self.assertTrue(self.publisher().cycle()["pushed"])
        self.assertNotEqual(self.remote_head(), head)

    def test_recent_original_backlog_yields_without_git_operations(self):
        status = self.root / ".local/remaining_evaluations/supervisor_status.json"
        status.parent.mkdir(parents=True)
        status.write_text(json.dumps({"stage": "retry_pending", "updated_at_utc": watch.stamp(),
                                      "error": "Git push rejected: non-fast-forward"}))
        preserved = status.read_bytes()
        head = self.remote_head()
        receipt = self.publisher().cycle()
        self.assertEqual(receipt["stage"], "yielding_to_trajectory_publication")
        self.assertFalse(receipt["pushed"])
        self.assertEqual(self.helper.calls, [])
        self.assertEqual(self.remote_head(), head)
        self.assertEqual(status.read_bytes(), preserved)

    def test_external_owned_edit_rejected_without_overwriting_it(self):
        self.publisher().cycle()
        name = "reports/EVALUATION_OVERVIEW.md"
        self.upstream_change(name, "Reviewer changed this report\n")
        head = self.remote_head()
        with self.assertRaisesRegex(watch.ReportingError, "Upstream edits changed owned reports"):
            self.publisher().cycle()
        self.assertEqual(self.remote_head(), head)
        self.assertEqual(git(self.remote, "show", "main:" + name), "Reviewer changed this report")
        receipt = json.loads((self.root / ".local/reporting_updater/status.json").read_text())
        self.assertEqual(receipt["stage"], "retry_pending")

    def test_concurrent_trajectory_commit_is_rebased_and_preserved(self):
        self.helper.before_push = lambda: self.upstream_change(
            "results/runs/example/trajectory_index.json", '{"preserved": true}\n')
        receipt = self.publisher().cycle()
        self.assertTrue(receipt["pushed"])
        self.assertTrue(any(call[0] == "rebase" for call in self.helper.calls))
        self.assertEqual(git(self.remote, "show", "main:results/runs/example/trajectory_index.json"), '{"preserved": true}')
        self.assertEqual(git(self.remote, "show", "main:reports/EVALUATION_OVERVIEW.md"),
            "Generated reports/EVALUATION_OVERVIEW.md")

    def test_concurrent_owned_edit_prevents_retry_push(self):
        self.helper.before_push = lambda: self.upstream_change(
            "reports/EVALUATION_OVERVIEW.md", "Concurrent human correction\n")
        with self.assertRaisesRegex(watch.ReportingError, "Upstream edits changed owned reports"):
            self.publisher().cycle()
        self.assertEqual(git(self.remote, "show", "main:reports/EVALUATION_OVERVIEW.md"), "Concurrent human correction")
        self.assertEqual(sum(call[0] == "push" for call in self.helper.calls), 1)

    def test_failed_generation_gate_or_privacy_does_not_publish(self):
        original = self.remote_head()
        def fail_check(argv):
            if "--check" in argv:
                raise watch.ReportingError("Generated output check failed")
        with self.assertRaisesRegex(watch.ReportingError, "check failed"):
            self.publisher(runner=fail_check).cycle()
        self.assertEqual(self.remote_head(), original)
        self.assertFalse(any(call[0] == "push" for call in self.helper.calls))
        self.helper.private = False
        with self.assertRaisesRegex(watch.ReportingError, "not verified"):
            self.publisher().cycle()
        self.assertEqual(self.remote_head(), original)

    def test_secret_scan_failure_stops_push_and_redacts_error(self):
        original = self.remote_head()
        (self.root / "reports/EVALUATION_OVERVIEW.md").write_text("SECRET_TEST")
        with self.assertRaisesRegex(watch.ReportingError, "credential scan"):
            self.publisher().cycle()
        self.assertEqual(self.remote_head(), original)
        receipt = (self.root / ".local/reporting_updater/status.json").read_text()
        self.assertNotIn("SECRET_TEST", receipt)
        self.assertFalse(any(call[0] == "push" for call in self.helper.calls))

    def test_unowned_staged_file_is_rejected(self):
        original = self.remote_head()
        def add_unowned(checkout):
            # Simulate another actor corrupting this reserved publication index.
            path = checkout / "unowned.txt"
            path.write_text("Do not publish\n")
            git(checkout, "add", "--sparse", "--", "unowned.txt")
        self.helper.before_add = add_unowned
        with self.assertRaisesRegex(watch.ReportingError, "Staged paths exceed"):
            self.publisher().cycle()
        self.assertEqual(self.remote_head(), original)

    def test_ownership_scope_cannot_silently_expand(self):
        self.publisher().cycle()
        with self.assertRaisesRegex(watch.ReportingError, "baseline migration"):
            self.publisher(include_score_reports=True)

    def test_optional_score_pair_requires_exact_source_hash_and_rendering(self):
        scripts = self.root / "scripts"
        scripts.mkdir()
        (scripts / "update_results_at_a_glance.py").write_text(
            'def render_markdown(report):\n    return report["text"]\n')
        score_raw = b'{"text": "Validated score snapshot\\n"}\n'
        (self.root / watch.SCORE_PAIR[1]).write_bytes(score_raw)
        (self.root / watch.SCORE_PAIR[0]).write_text("Validated score snapshot\n")
        catalog = {"meta": {"sourceHashes": {watch.SCORE_PAIR[1]: "wrong"}}}
        (self.root / "reports/TASK_HIERARCHY_DATA.json").write_text(json.dumps(catalog))
        original = self.remote_head()
        with self.assertRaisesRegex(watch.ReportingError, "score report pair"):
            self.publisher(include_score_reports=True).cycle()
        self.assertEqual(self.remote_head(), original)
        catalog["meta"]["sourceHashes"][watch.SCORE_PAIR[1]] = watch.sha(score_raw)
        (self.root / "reports/TASK_HIERARCHY_DATA.json").write_text(json.dumps(catalog))
        receipt = self.publisher(include_score_reports=True).cycle()
        self.assertTrue(receipt["pushed"])
        self.assertEqual(set(receipt["ownedPaths"]), set(watch.OWNED + watch.SCORE_PAIR))


if __name__ == "__main__":
    unittest.main()
