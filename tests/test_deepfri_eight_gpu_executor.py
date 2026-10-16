import importlib.util
import json
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
spec = importlib.util.spec_from_file_location("deepfri_eight_gpu_executor", SCRIPTS / "execute_local_deepfri_confidence_eight_gpu.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class ExecutorTests(unittest.TestCase):
    def fixture(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        root = Path(temporary.name)
        names = ["scripts/run_local_labbench_eight_gpu.py", "scripts/score_local_deepfri_confidence.py"]
        for name in names:
            path = root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("# synthetic pinned implementation\n")
        (root / "runtime.json").write_text('{"synthetic":true}')
        config = {"run_id": "synthetic", "proposal_status": "frozen_for_authorized_execution", "enabled": True,
                  "approved_task_ids": ["P12"], "runner": names[0], "scorer": names[1],
                  "scorer_python": ".venv-vllm/bin/python", "scoring_protocol_sha256": "synthetic-protocol",
                  "scoring_runtime_file": "runtime.json", "frozen_files_sha256": {name: mod.file_digest(root / name) for name in names}}
        path = root / "config.json"
        path.write_text(json.dumps(config))
        return root, path

    def command(self, root, generation_code=0):
        def run(argv, **kwargs):
            if "--describe-protocol" in argv:
                return SimpleNamespace(stdout=json.dumps({"protocol_sha256": "synthetic-protocol", "runtime": {"synthetic": True}}), returncode=0)
            folder = root / "results/runs/synthetic"
            folder.mkdir(parents=True, exist_ok=True)
            if "--run" in argv:
                (folder / "scores.json").write_text('{"synthetic":true}')
                return SimpleNamespace(returncode=0)
            if generation_code == 0:
                (folder / "run_manifest.json").write_text('{"synthetic":true}')
            return SimpleNamespace(returncode=generation_code)
        return run

    def test_success_completion_and_terminal_rerun_rejection(self):
        root, path = self.fixture()
        with patch.object(mod, "ROOT", root), patch.object(mod.subprocess, "run", self.command(root)):
            self.assertEqual(mod.execute(path), 0)
            record = json.loads((root / "results/runs/synthetic/completion.json").read_text())
            self.assertEqual(record["status"], "completed")
            self.assertEqual(record["generation_exit_code"], 0)
            self.assertIn("run_manifest_sha256", record)
            self.assertIn("scorer_sha256", record)
            with self.assertRaisesRegex(ValueError, "terminal completion"):
                mod.execute(path)

    def test_generation_failure_is_terminal_without_fabricated_scoring_code(self):
        root, path = self.fixture()
        with patch.object(mod, "ROOT", root), patch.object(mod.subprocess, "run", self.command(root, 7)):
            self.assertEqual(mod.execute(path), 7)
        record = json.loads((root / "results/runs/synthetic/completion.json").read_text())
        self.assertEqual(record["status"], "failed")
        self.assertEqual(record["generation_exit_code"], 7)
        self.assertIsNone(record["scoring_exit_code"])
        self.assertIn("No immutable run manifest", record["error"])

    def test_disabled_proposal_never_invokes_subprocess(self):
        root, path = self.fixture()
        settings = json.loads(path.read_text())
        settings["enabled"] = False
        path.write_text(json.dumps(settings))
        with patch.object(mod, "ROOT", root), patch.object(mod.subprocess, "run") as run:
            with self.assertRaisesRegex(ValueError, "Disabled proposal"):
                mod.execute(path)
            run.assert_not_called()


if __name__ == "__main__":
    unittest.main()
