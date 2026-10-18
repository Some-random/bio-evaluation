"""Real local HTTP/TCP buffering and POSIX stop/kill checks, CPU only."""

from concurrent.futures import ThreadPoolExecutor
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import importlib.util
import json
import multiprocessing
import os
from pathlib import Path
import signal
import subprocess
import sys
import tempfile
import threading
import time
from types import SimpleNamespace
import unittest
from unittest.mock import patch
from urllib.request import ProxyHandler, Request, build_opener


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "drain_vllm_worker.py"
SPEC = importlib.util.spec_from_file_location("drain_vllm_worker", SCRIPT)
DRAIN = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(DRAIN)


def serve(folder, pipe):
    running = 0
    lock = threading.Lock()

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *args):
            pass

        def do_GET(self):
            with lock:
                active = running
            raw = f"vllm:num_requests_running {active}\nvllm:num_requests_waiting 0\n".encode()
            self.send_response(200)
            self.send_header("Content-Length", str(len(raw)))
            self.end_headers()
            self.wfile.write(raw)

        def do_POST(self):
            nonlocal running
            data = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
            with lock:
                running += 1
            DRAIN.write(folder / f"accepted_{data['case']}.json", data)
            time.sleep(1)
            with lock:
                running -= 1
            raw = json.dumps({"result": "synthetic completed output"}).encode()
            self.send_response(200)
            self.send_header("Content-Length", str(len(raw)))
            self.end_headers()
            self.wfile.write(raw)

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    pipe.send(server.server_port)
    pipe.close()
    server.serve_forever()


def client(folder, base_url):
    def execute(index):
        payload = {"model": "synthetic-model", "case": index}
        filename = f"case_{index:03d}.json"
        request_hash = DRAIN.digest(payload)
        DRAIN.write(folder / "requests" / filename, {"payload": payload, "request_sha256": request_hash})
        request = Request(base_url + "/v1/chat/completions", data=json.dumps(payload).encode(), headers={"Content-Type": "application/json"})
        with build_opener(ProxyHandler({})).open(request, timeout=10) as response:
            result = json.loads(response.read())
        if index == 1:
            # Ensure another thread can save and create a blocked next request
            # before the final pre-stop completion is saved.
            time.sleep(.1)
        DRAIN.write(folder / "responses" / filename, {"request_sha256": request_hash, "status": "completed", "http_status": 200, "response": result})

    with ThreadPoolExecutor(max_workers=2) as executor:
        list(executor.map(execute, range(4)))


def native_executor(folder, base_url, pipe):
    exit_codes = []
    def run_child():
        result = subprocess.run([sys.executable, str(Path(__file__).resolve()), "--mock-client", str(folder), base_url])
        exit_codes.append(result.returncode)
    waiter = threading.Thread(target=run_child)
    waiter.start()
    while not (folder / "client_pid.json").exists():
        time.sleep(.01)
    pipe.send(json.loads((folder / "client_pid.json").read_text())["pid"])
    pipe.close()
    waiter.join()
    # Match the native executor's real failure path: it invokes scoring even
    # when generation was killed. A correct committed drain must prevent this.
    DRAIN.write(folder / "SCORE.json", {"client_exit_code": exit_codes[0]})


class DrainTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.folder = Path(self.temporary.name)
        (self.folder / "requests").mkdir()
        (self.folder / "responses").mkdir()
        parent, child = multiprocessing.Pipe()
        self.api = multiprocessing.Process(target=serve, args=(self.folder, child))
        self.api.start()
        self.port = parent.recv()
        parent.close()
        self.base_url = f"http://127.0.0.1:{self.port}"
        parent, child = multiprocessing.Pipe()
        self.executor = multiprocessing.Process(target=native_executor, args=(self.folder, self.base_url, child))
        self.executor.start()
        self.client = SimpleNamespace(pid=parent.recv())
        parent.close()
        deadline = time.monotonic() + 5
        while len(list(self.folder.glob("accepted_*.json"))) < 2:
            if time.monotonic() >= deadline:
                self.fail("Synthetic first batch did not reach the local server")
            time.sleep(.01)

    def tearDown(self):
        try:
            os.kill(self.client.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        for process in (self.executor, self.api):
            if process.is_alive():
                os.kill(process.pid, signal.SIGCONT)
                process.kill()
            process.join(timeout=3)
        self.temporary.cleanup()

    def args(self, expected=2):
        return SimpleNamespace(commit_after_drain=True, base_url=self.base_url, run_directory=self.folder, project_root=self.folder, run_id="synthetic-run", old_job_id="12345", receipt=self.folder / "drain_receipt.json", client_pid=self.client.pid, client_start_ticks=DRAIN.process(self.client.pid)["start_ticks"], api_pid=self.api.pid, api_start_ticks=DRAIN.process(self.api.pid)["start_ticks"], executor_pid=self.executor.pid, executor_start_ticks=DRAIN.process(self.executor.pid)["start_ticks"], expected_inflight=expected, drain_timeout=5, flush_timeout=5, idle_seconds=.05, poll_interval=.01)

    def test_buffered_answers_saved_and_new_requests_proved_unexecuted_before_kill(self):
        args = self.args()
        query = lambda job: {"job_id": str(job), "state": "RUNNING", "exit_code": "0:0"}
        receipt = DRAIN.drain(args, query_accounting=query)
        self.assertEqual(receipt["stage"], "drained_processes_killed_waiting_job_terminal")
        self.assertTrue(all(receipt["proof"][key] is True for key in DRAIN.PROOF_FIELDS))
        self.assertTrue(DRAIN.dead(self.api.pid, args.api_start_ticks))
        self.assertTrue(DRAIN.dead(self.client.pid, args.client_start_ticks))
        self.assertTrue(DRAIN.dead(self.executor.pid, args.executor_start_ticks))
        self.assertFalse((self.folder / "SCORE.json").exists())
        self.assertEqual(receipt["drain_protocol_version"], 2)
        self.assertEqual(len(list(self.folder.glob("accepted_*.json"))), 2)
        self.assertEqual(len(list((self.folder / "responses").glob("*.json"))), 2)
        self.assertGreaterEqual(len(receipt["request_records"]), 1)
        for row in receipt["request_records"]:
            self.assertTrue(row["request_created_after_api_stop"])
            self.assertTrue(row["server_stopped_at_creation"])
            self.assertFalse((self.folder / "responses" / row["filename"]).exists())
            self.assertEqual(row["request_file_sha256"], DRAIN.file_digest(self.folder / "requests" / row["filename"]))
        final = DRAIN.finalize(args.receipt, query_accounting=lambda job: {"job_id": str(job), "state": "FAILED", "exit_code": "0:9"})
        self.assertEqual(final["stage"], "drained_and_job_terminal")
        self.assertEqual(final["terminal_accounting"]["job_id"], "12345")

    def test_precommit_mismatch_resumes_original_client_and_server(self):
        args = self.args(expected=3)
        with self.assertRaisesRegex(ValueError, "Outstanding"):
            DRAIN.drain(args, query_accounting=lambda job: {"job_id": str(job), "state": "RUNNING", "exit_code": "0:0"})
        self.executor.join(timeout=6)
        self.assertEqual(self.executor.exitcode, 0)
        self.assertTrue((self.folder / "SCORE.json").exists())
        self.assertEqual(json.loads((self.folder / "SCORE.json").read_text())["client_exit_code"], 0)
        self.assertNotIn(DRAIN.process(self.api.pid)["state"], {"T", "t"})
        self.assertEqual(len(list(self.folder.glob("accepted_*.json"))), 4)
        self.assertEqual(len(list((self.folder / "responses").glob("*.json"))), 4)
        receipt = json.loads(args.receipt.read_text())
        self.assertEqual(receipt["stage"], "failed_rolled_back_original_processes")
        with self.assertRaises(ValueError):
            DRAIN.finalize(args.receipt)

    def test_failure_after_api_kill_never_resumes_the_held_client(self):
        args = self.args()
        original = DRAIN.kill_stopped

        def kill_then_fail_observation(pid, ticks):
            original(pid, ticks)
            raise RuntimeError("simulated failure after irreversible API kill")

        with patch.object(DRAIN, "kill_stopped", side_effect=kill_then_fail_observation):
            with self.assertRaisesRegex(RuntimeError, "irreversible"):
                DRAIN.drain(args, query_accounting=lambda job: {"job_id": str(job), "state": "RUNNING", "exit_code": "0:0"})
        self.assertTrue(DRAIN.dead(self.api.pid, args.api_start_ticks))
        self.assertIn(DRAIN.process(self.client.pid)["state"], {"T", "t"})
        self.assertIn(DRAIN.process(self.executor.pid)["state"], {"T", "t"})
        self.assertFalse((self.folder / "SCORE.json").exists())
        receipt = json.loads(args.receipt.read_text())
        self.assertEqual(receipt["stage"], "commit_failed_api_kill_started_client_held_for_recovery")
        with self.assertRaises(ValueError):
            DRAIN.finalize(args.receipt)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--mock-client":
        mock_folder = Path(sys.argv[2])
        DRAIN.write(mock_folder / "client_pid.json", {"pid": os.getpid()})
        client(mock_folder, sys.argv[3])
    else:
        unittest.main()
