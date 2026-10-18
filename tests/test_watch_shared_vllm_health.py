"""CPU HTTP monitoring checks: no inference, text retention or double counting."""

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import importlib.util
import json
import os
from pathlib import Path
import socket
import tempfile
import threading
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("watch_shared_vllm_health", ROOT / "scripts/watch_shared_vllm_health.py")
HEALTH = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(HEALTH)


class HealthTests(unittest.TestCase):
    def test_response_summary_retains_no_final_reasoning_or_prompt_text(self):
        raw = json.dumps({"status": "completed", "http_status": 200, "finish_reason": "length", "saved_at_utc": "2026-10-18T05:00:00+00:00", "response": {"choices": [{"message": {"content": "", "reasoning": "private reasoning fixture"}}], "usage": {"completion_tokens": 4096}}})
        metadata = HEALTH.response_metadata(raw)
        self.assertTrue(metadata["empty_final"])
        self.assertEqual(metadata["completion_tokens"], 4096)
        self.assertEqual(metadata["saved_at_pacific"], "2026-10-17T22:00:00-07:00")
        self.assertNotIn("private reasoning", json.dumps(metadata))

    def test_live_get_monitor_uses_fork_scope_caches_metadata_and_checks_pins(self):
        posts = []

        class Handler(BaseHTTPRequestHandler):
            def log_message(self, *args):
                pass

            def do_POST(self):
                posts.append(self.path)
                self.send_error(500)

            def do_GET(self):
                raw = json.dumps({"data": [{"id": "synthetic-model"}]}).encode() if self.path.endswith("/models") else b"vllm:num_requests_running 4\nvllm:num_requests_waiting 0\nvllm:kv_cache_usage_perc 0.3\nvllm:num_preemptions_total 0\nvllm:generation_tokens_total 100\n"
                self.send_response(200)
                self.send_header("Content-Length", str(len(raw)))
                self.end_headers()
                self.wfile.write(raw)

        server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            with tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                pool = root / ".local/pool"
                project = root / "project"
                original = project / "results/runs/logical"
                fork = project / "results/runs/logical_shared_continuation_v1"
                HEALTH.write(original / "responses/old.json", {"not_scanned": "parent response text"})
                HEALTH.write(fork / "responses/historical.json", {"not_scanned": "historical copied text"})
                HEALTH.write(fork / "requests/new.json", {"not_scanned": "request text"})
                HEALTH.write(fork / "shared_vllm_dispatch/new.json", {"status": "response_saved"})
                HEALTH.write(fork / "responses/new.json", {"status": "completed", "http_status": 200, "finish_reason": "length", "response": {"choices": [{"message": {"content": "", "reasoning_content": "private reasoning fixture"}}]}})
                HEALTH.write(pool / "plan.json", {"model": "synthetic-model", "revision": "fixed", "replicas": 1, "max_model_len": 65536, "max_num_seqs": 32})
                HEALTH.write(pool / "status.json", {"stage": "evaluating", "updated_at": "2026-10-18T05:00:00+00:00"})
                endpoint = f"http://127.0.0.1:{server.server_port}/v1"
                identity = {"model": "synthetic-model", "revision": "fixed", "dtype": "bfloat16", "tensor_parallel_size": 1, "endpoint": endpoint, "hostname": socket.gethostname(), "pid": os.getpid(), "proc_start_ticks": HEALTH.process_ticks(os.getpid()), "gpu_uuids": ["GPU-synthetic"], "max_model_len": 65536, "max_num_seqs": 32}
                HEALTH.write(pool / "server_identity.json", identity)
                HEALTH.write(pool / "endpoints.json", [{"endpoint_id": "replica_0", "endpoint": endpoint, "server_identity_file": str(pool / "server_identity.json"), "server_identity_sha256": HEALTH.sha(pool / "server_identity.json")}])
                source = root / ".local/source_plan.json"
                HEALTH.write(source, {"workers": [{"entries": [{"run_id": "logical", "project_root": str(project), "task_id": "P08", "case_count": 2}]}]})
                evidence = root / ".local/evidence.json"
                HEALTH.write(evidence, {"synthetic_only": True})
                amendment = root / ".local/amendment.json"
                HEALTH.write(amendment, {"kind": "shared_vllm_infrastructure_amendment", "execution_authorized": True, "scientific_protocol_changes": [], "model": "synthetic-model", "model_revision": "fixed", "run_ids": ["logical"], "source_plans": [{"path": str(source), "sha256": HEALTH.sha(source)}], "continuation_run_directories": {"logical": str(fork)}, "capacity_evidence_files": [{"path": str(evidence), "sha256": HEALTH.sha(evidence)}]})
                plan_path = root / ".local/health_plan.json"
                plan = {"schema_version": 1, "root": str(root), "pool_directory": str(pool), "pool_plan_sha256": HEALTH.sha(pool / "plan.json"), "endpoints_file": str(pool / "endpoints.json"), "endpoints_sha256": HEALTH.sha(pool / "endpoints.json"), "amendment_path": str(amendment), "amendment_sha256": HEALTH.sha(amendment), "state_file": str(root / ".local/health_private.json"), "public_output_file": str(pool / "health_public.json"), "interval_seconds": 60, "thresholds": {"minimum_responses_for_format_warning": 1, "high_truncation_fraction": .5}}
                HEALTH.write(plan_path, plan)
                checksum = HEALTH.sha(plan_path)
                report, _ = HEALTH.cycle(plan_path, checksum)
                self.assertEqual(report["planned_native_cases"], 2)
                self.assertEqual(report["saved_responses_unique_logical_sources"], 2)
                self.assertEqual(report["logical_scope_count"], 1)
                self.assertEqual(report["response_format"]["shared_response_metadata_scanned"], 1)
                self.assertEqual(report["runs"][0]["historical_responses_not_scanned"], 1)
                self.assertTrue(report["endpoints"][0]["healthy"])
                self.assertIn("high_length_finish_fraction", [flag["type"] for flag in report["flags"]])
                self.assertEqual(report["automatic_actions"], [])
                self.assertNotIn("private reasoning", json.dumps(report))
                self.assertNotIn("private reasoning", Path(plan["state_file"]).read_text())
                with patch.object(HEALTH, "response_metadata", side_effect=AssertionError("Cached response was parsed again")):
                    second, _ = HEALTH.cycle(plan_path, checksum)
                self.assertEqual(second["response_format"]["new_responses_since_last_check"], 0)
                old_state = HEALTH.sha(plan["state_file"])
                HEALTH.write(evidence, {"changed": True})
                with self.assertRaisesRegex(ValueError, "capacity evidence"):
                    HEALTH.cycle(plan_path, checksum)
                self.assertEqual(HEALTH.sha(plan["state_file"]), old_state)
                self.assertEqual(posts, [])
        finally:
            server.shutdown()
            server.server_close()
            thread.join()


if __name__ == "__main__":
    unittest.main()
