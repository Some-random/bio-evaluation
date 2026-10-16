"""Publishing hooks cannot launch native aggregation or report generation."""
import importlib.util
import json
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/publish_native_evaluation_trajectories.py"
spec = importlib.util.spec_from_file_location("publication_only", SCRIPT)
publish = importlib.util.module_from_spec(spec)
spec.loader.exec_module(publish)


class UploadOnlyTests(unittest.TestCase):
    def test_frozen_scoring_and_report_hooks_are_replaced_with_metadata_reads(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "aggregation_status.json").write_text(json.dumps({"p03": {"stage": "terminal"}}))
            (root / "report_update_status.json").write_text(json.dumps({"stage": "updated"}))
            def forbidden(*args):
                raise AssertionError("No scoring or report generation permitted")
            native = SimpleNamespace(HERE=root, aggregate_ready=forbidden, refresh_reports=forbidden)
            publish.install_upload_only_callbacks(native)
            self.assertEqual(native.aggregate_ready({}, {}), {"p03": {"stage": "terminal"}})
            self.assertEqual(native.refresh_reports({}), {"stage": "updated"})

    def test_public_checkpoint_keeps_actual_visibility(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            state = root / ".local/remaining_evaluations"
            state.mkdir(parents=True)
            native = SimpleNamespace(HERE=state,
                helpers=SimpleNamespace(confirm_destination=lambda: {"private": False, "visibility": "public", "destination_policy_sha256": "abc"}),
                cycle=lambda path: {"stage": "watching", "runs": {}, "updated_at_utc": "2026-10-16T19:00:00+00:00"})
            result = publish.publish_once(native, root)
            self.assertFalse(result["repository_private_verified"])
            self.assertEqual(result["repository_visibility"], "public")
            self.assertFalse(result["generation_or_scoring_performed"])
            self.assertEqual(json.loads((state / "upload_status.json").read_text()), result)


if __name__ == "__main__":
    unittest.main()
