"""Synthetic CPU checks for serving measurement arithmetic and artifact fidelity."""

from contextlib import redirect_stdout
import importlib.util
import io
import json
from pathlib import Path
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import tempfile
import threading
import time
from types import SimpleNamespace
import unittest
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "benchmark_vllm_concurrency.py"
SPEC = importlib.util.spec_from_file_location("benchmark_vllm_concurrency", SCRIPT)
BENCHMARK = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BENCHMARK)


class ArithmeticTests(unittest.TestCase):
    def test_production_sampling_can_be_selected_without_changing_workload_seed(self):
        args = SimpleNamespace(temperature=0, generation_seed=None, seed=20261017, top_p=None, top_k=None, output_tokens=512)
        self.assertEqual(BENCHMARK.sampling_settings(args), {"temperature": 0, "seed": 20261017, "ignore_eos": True, "max_tokens": 512})
        args.temperature, args.generation_seed, args.top_p, args.top_k = 1, 42, .95, 20
        settings = BENCHMARK.sampling_settings(args)
        self.assertEqual(settings["seed"], 42)
        self.assertEqual(settings["top_p"], .95)
        self.assertEqual(settings["top_k"], 20)
        self.assertEqual(args.seed, 20261017)

    def test_failed_requests_remain_in_denominator_and_latency_uses_successes(self):
        records = [
            {"success": True, "elapsed_seconds": 2.0, "prompt_tokens": 10, "completion_tokens": 20},
            {"success": False, "elapsed_seconds": 3.0},
            {"success": True, "elapsed_seconds": 4.0, "prompt_tokens": 10, "completion_tokens": 20},
        ]
        result = BENCHMARK.summarize(records, 10.0, 10, 20)
        self.assertEqual(result["output_tokens_per_second"], 4.0)
        self.assertEqual(result["requests_per_second"], .2)
        self.assertEqual(result["failed_requests"], 1)
        self.assertEqual(result["latency_seconds"]["p50"], 3.0)
        self.assertAlmostEqual(result["latency_seconds"]["p95"], 3.9)
        self.assertFalse(result["comparable_fixed_workload"])

    def test_short_decode_is_preserved_but_not_a_valid_fixed_workload(self):
        result = BENCHMARK.summarize([
            {"success": True, "elapsed_seconds": 1.0, "prompt_tokens": 10, "completion_tokens": 2},
        ], 2.0, 10, 20)
        self.assertEqual(result["actual_completion_tokens"], 2)
        self.assertEqual(result["fixed_workload_mismatch_requests"], 1)
        self.assertFalse(result["comparable_fixed_workload"])

    def test_only_credential_free_loopback_servers_are_allowed(self):
        self.assertEqual(BENCHMARK.validate_base_url("http://127.0.0.1:1234/v1"), "http://127.0.0.1:1234")
        for url in ("https://example.com", "http://example.com", "http://secret@localhost", "http://localhost/?key=secret"):
            with self.assertRaises(ValueError):
                BENCHMARK.validate_base_url(url)


class LocalServerTests(unittest.TestCase):
    def setUp(self):
        self.requests = []
        self.resets = 0
        self.active = 0
        self.peak = 0
        self.allow_reset = True
        self.lock = threading.Lock()
        owner = self

        class Handler(BaseHTTPRequestHandler):
            def log_message(self, *args):
                pass

            def reply(self, response):
                raw = json.dumps(response).encode()
                self.send_response(200)
                self.send_header("Content-Length", str(len(raw)))
                self.end_headers()
                self.wfile.write(raw)

            def do_GET(self):
                raw = b"vllm:num_preemptions_total 0\nvllm:num_requests_running 0\n"
                self.send_response(200)
                self.send_header("Content-Length", str(len(raw)))
                self.end_headers()
                self.wfile.write(raw)

            def do_POST(self):
                if self.path == "/reset_prefix_cache":
                    with owner.lock:
                        owner.resets += 1
                        if owner.active:
                            raise AssertionError("Cache reset overlaps an active request")
                    self.reply(owner.allow_reset)
                    return
                payload = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
                if self.path == "/tokenize":
                    self.reply({"tokens": list(range(len(payload["prompt"])))})
                    return
                with owner.lock:
                    owner.requests.append(payload)
                    owner.active += 1
                    owner.peak = max(owner.peak, owner.active)
                time.sleep(.02)
                with owner.lock:
                    owner.active -= 1
                self.reply({"choices": [{"text": "synthetic response", "finish_reason": "length"}], "usage": {"prompt_tokens": len(payload["prompt"]), "completion_tokens": payload["max_tokens"]}})

        self.server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.client = BENCHMARK.Client(f"http://127.0.0.1:{self.server.server_port}", 5)
        self.temp = tempfile.TemporaryDirectory()
        self.output_dir = Path(self.temp.name)

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()
        self.thread.join()
        self.temp.cleanup()

    def test_paired_stages_reset_cache_and_keep_exact_requests_and_responses(self):
        workload = BENCHMARK.make_workload(self.client, "synthetic-model", 4, 12, 3)
        payloads = [{"model": "synthetic-model", "prompt": row["prompt_token_ids"], "max_tokens": 8, "ignore_eos": True} for row in workload["requests"]]
        progress = {"completed_stages": []}
        with redirect_stdout(io.StringIO()):
            first = BENCHMARK.run_stage(self.client, "first", 1, payloads, self.output_dir, 12, 8, progress, "reset-between-levels")
            second = BENCHMARK.run_stage(self.client, "second", 2, payloads, self.output_dir, 12, 8, progress, "reset-between-levels")
        self.assertEqual(self.resets, 2)
        self.assertEqual(self.peak, 2)
        self.assertEqual(self.requests[:4], self.requests[4:])
        for stage, result in (("first", first), ("second", second)):
            self.assertTrue(result["comparable_fixed_workload"])
            self.assertEqual(result["actual_completion_tokens"], 32)
            self.assertIn("vllm:num_preemptions_total", result["metrics_before"]["selected"])
            for index, payload in enumerate(payloads):
                request = json.loads((self.output_dir / stage / f"request_{index:05d}.json").read_text())
                response = json.loads((self.output_dir / stage / f"response_{index:05d}.json").read_text())
                self.assertEqual(request, payload)
                self.assertEqual(response["request_sha256"], BENCHMARK.canonical_hash(payload))
                self.assertEqual(response["response"]["choices"][0]["text"], "synthetic response")

    def test_refused_cache_reset_stops_before_inference(self):
        self.allow_reset = False
        with self.assertRaisesRegex(RuntimeError, "refused"):
            BENCHMARK.run_stage(self.client, "refused", 1, [{"prompt": [1], "max_tokens": 1}], self.output_dir, 1, 1, {}, "reset-between-levels")
        self.assertEqual(self.requests, [])

    def test_stage_entry_clears_previous_stage_partial_summary(self):
        progress = {"stage_partial_summary": {"completed_requests": 4, "actual_completion_tokens": 256}}
        observed = []
        original_write = BENCHMARK.write_json

        def capture_write(path, value):
            if path.name == "progress.json":
                observed.append(json.loads(json.dumps(value)))
            return original_write(path, value)

        with patch.object(BENCHMARK, "write_json", side_effect=capture_write), redirect_stdout(io.StringIO()):
            BENCHMARK.run_stage(self.client, "new_stage", 1, [{"prompt": [1], "max_tokens": 8}], self.output_dir, 1, 8, progress, "reset-between-levels")
        self.assertEqual(observed[0]["completed_requests"], 0)
        self.assertNotIn("stage_partial_summary", observed[0])
        self.assertEqual(observed[-1]["stage_partial_summary"]["actual_completion_tokens"], 8)


if __name__ == "__main__":
    unittest.main()
