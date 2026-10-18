"""Public serving evidence must exclude interference and open directories."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/prepare_shared_vllm_publication.py"
SPEC = importlib.util.spec_from_file_location("prepare_shared_publication", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value))


class PublicEvidenceTests(unittest.TestCase):
    def test_successful_client_is_rejected_when_server_did_unrelated_work(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            samples = root / "live.jsonl"
            samples.write_text(json.dumps({"running": 1, "waiting": 0}) + "\n")
            before = {"vllm:prompt_tokens_total{engine=\"0\"}": 100,
                      "vllm:generation_tokens_total{engine=\"0\"}": 200,
                      "vllm:num_requests_running{engine=\"0\"}": 0,
                      "vllm:num_requests_waiting{engine=\"0\"}": 0}
            after = dict(before)
            after['vllm:prompt_tokens_total{engine="0"}'] += 192
            after['vllm:generation_tokens_total{engine="0"}'] += 4096
            row = {"concurrency": 1, "monitoring": {"sample_file": str(samples)},
                   "measured": {"actual_prompt_tokens": 192, "actual_completion_tokens": 4096,
                                "metrics_before": {"selected": before}, "metrics_after": {"selected": after}}}
            self.assertTrue(MODULE.isolation_check(row, root)["passed"])
            after['vllm:generation_tokens_total{engine="0"}'] += 1
            self.assertFalse(MODULE.isolation_check(row, root)["passed"])
            after['vllm:generation_tokens_total{engine="0"}'] -= 1
            samples.write_text(json.dumps({"running": 2, "waiting": 0}) + "\n")
            self.assertFalse(MODULE.isolation_check(row, root)["passed"])

    def test_archive_selection_preserves_closed_exclusion_but_omits_live_files(self):
        with tempfile.TemporaryDirectory() as temporary:
            pool = Path(temporary).resolve()
            code = pool / "frozen.py"
            code.write_text("# frozen source\n")
            write(pool / "plan.json", {"code_sha256": {str(code): MODULE.digest(code.read_bytes())}})
            (pool / "plan.sha256").write_text(MODULE.digest((pool / "plan.json").read_bytes()))
            (pool / "pool.sbatch").write_text("# frozen launcher\n")
            write(pool / "endpoints.json", [])
            closed, opened = pool / "replica_3/length_benchmark", pool / "replica_0/length_benchmark_clean"
            write(closed / "progress.json", {"state": "completed"})
            write(closed / "original_response.json", {"untouched": True})
            write(opened / "progress.json", {"state": "measuring"})
            (pool / "server.log").write_text("live log")
            files = MODULE.frozen_files(pool, [{"directory": str(closed.relative_to(pool)), "closed": True},
                                               {"directory": str(opened.relative_to(pool)), "closed": False}])
            self.assertTrue(any(name.endswith("original_response.json") for name in files))
            self.assertFalse(any("clean" in name or name.endswith("server.log") for name in files))
            self.assertFalse(any(".local" in Path(name).parts for name in files))
            write(pool / "plan.json", {"code_sha256": {str(code): "0" * 64}})
            (pool / "plan.sha256").write_text(MODULE.digest((pool / "plan.json").read_bytes()))
            with self.assertRaisesRegex(ValueError, "hash mismatch"):
                MODULE.frozen_files(pool, [])


if __name__ == "__main__":
    unittest.main()
