"""Only artificial questions/labels and injected transports; no network or keys."""
import argparse
import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import threading
import time
import unittest
from unittest import mock

SPEC = importlib.util.spec_from_file_location("isolated_dispatcher", Path(__file__).resolve().parents[1] / "scripts/run_isolated_openai_comparison.py")
d = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(d)


def fixture(count=3, model="gpt-6-luna"):
    rows = []
    for i in range(count):
        payload = {"model": model, "input": [{"role": "user", "content": [{"type": "input_text", "text": f"Invented arithmetic fixture {i}: choose (A) 2 (B) 3."}]}],
                   "reasoning": {"effort": "medium"}, "max_output_tokens": 4096, "service_tier": "default", "store": False}
        rows.append({"task_id": "B01" if i % 2 == 0 else "B03", "case_id": "fixture_" + str(i),
                     "payload_without_private_safety_identifier": payload,
                     "qwen": {"correct": True, "prediction": "A"}, "gold": "A", "reference_path": "/not/a/real/path"})
    roster = {"protocol_id": "artificial_protocol", "model": model,
              "cases": [{"task_id": r["task_id"], "case_id": r["case_id"], "payload_sha256": d.sha(d.canonical(r["payload_without_private_safety_identifier"]))} for r in rows]}
    return rows, roster


def bundle_at(root, count=3, model="gpt-6-luna"):
    root = Path(root)
    rows, roster = fixture(count, model)
    req = b"".join(d.canonical(r) + b"\n" for r in rows)
    protocol = {"protocol_id": roster["protocol_id"], "allowed_models": [model], "task_ids": ["B01", "B03"],
                "generation": {"max_output_tokens": 4096, "reasoning": {"effort": "medium"}, "service_tier": "default", "store": False}}
    for name, data in (("requests.jsonl", req), ("roster.json", d.canonical(roster)), ("protocol.json", d.canonical(protocol))):
        (root / name).write_bytes(data)
    args = argparse.Namespace(requests=str(root / "requests.jsonl"), requests_sha256=d.sha(req),
                              roster=str(root / "roster.json"), roster_sha256=d.sha(d.canonical(roster)),
                              protocol=str(root / "protocol.json"), protocol_sha256=d.sha(d.canonical(protocol)),
                              protocol_id=roster["protocol_id"], model=model, bundle=str(root / "bundle"))
    result = d.prepare_bundle(args)
    manifest, clean = d.load_bundle(result["bundle"], result["bundle_sha256"])
    return result, manifest, clean


def reply(text="[ANSWER]A[/ANSWER]", status="completed", model="gpt-6-luna", **extra):
    body = {"id": "resp_fixture", "model": model, "status": status, "usage": {"input_tokens": 2, "output_tokens": 3},
            "output": [{"type": "message", "role": "assistant", "content": [{"type": "output_text", "text": text}]}]}
    body.update(extra)
    return 200, d.canonical(body), {"request_id": "req_fixture"}


def authorization(manifest, development=False):
    return {"schema_version": 1, "dispatch_authorized": True, "scope_review_passed": True,
            "prior_flagged_requests_excluded": True, "no_broad_resume": True,
            "purpose": "development_delivery_only" if development else "frozen_benchmark_comparison",
            "current_user_authorization_source": "Artificial fixture authorization; no real execution",
            "allowed_models": [manifest["model"]], "allowed_protocol_ids": [manifest["protocol_id"]],
            "allowed_tasks": ["B01", "B03"], "frozen_roster_sha256": manifest["source_roster_sha256"],
            "frozen_protocol_sha256": manifest["frozen_protocol_sha256"],
            "reviewed_input_receipt_sha256": "a" * 64, "risk_review_receipt_sha256": "b" * 64,
            "spending_guard_usd": 50, "estimated_max_run_cost_usd": 2}


def gate(manifest):
    return {"schema_version": 1, "protocol_id": manifest["protocol_id"], "model": manifest["model"],
            "reviewed": True, "delivery_passed": True, "biological_correctness_assessed": False,
            "max_output_tokens": 4096, "reasoning_effort": "medium", "dispatch_authorized": True,
            "frozen_protocol_sha256": manifest["frozen_protocol_sha256"], "dispatcher_sha256": manifest["dispatcher_sha256"],
            "task_ids": ["B01", "B03"], "development_evidence_sha256": "c" * 64}


class IsolatedComparisonTests(unittest.TestCase):
    def test_scorer_and_prior_answers_cannot_change_frozen_outbound_body(self):
        rows, roster = fixture()
        expected = d.prepare_rows(b"\n".join(d.canonical(r) for r in rows), roster, "artificial_protocol", "gpt-6-luna")
        changed = copy.deepcopy(rows)
        for i, row in enumerate(changed):
            row["gold"] = ["B", "C", "D"][i]
            row["qwen"] = {"prediction": "CHANGED", "correct": False, "reasoning": "DO NOT TRANSMIT"}
            row["messages"] = [{"role": "system", "content": "injected gold"}]
            row["payload"] = {"answer": "injected"}
            row["reference_path"] = "/also/not/readable"
        actual = d.prepare_rows(b"\n".join(d.canonical(r) for r in changed), roster, "artificial_protocol", "gpt-6-luna")
        self.assertEqual(d.canonical(expected), d.canonical(actual))
        self.assertNotIn(b"CHANGED", d.canonical(actual))

    def test_mutating_actual_prompt_or_choice_order_fails_pin(self):
        rows, roster = fixture()
        rows[0]["payload_without_private_safety_identifier"]["input"][0]["content"][0]["text"] = "(B) 3 (A) 2"
        with self.assertRaisesRegex(ValueError, "Frozen payload"):
            d.prepare_rows(b"\n".join(d.canonical(r) for r in rows), roster, "artificial_protocol", "gpt-6-luna")

    def test_exact_case_roster_and_protocol_are_required(self):
        rows, roster = fixture()
        for changed in (rows[::-1], rows[:-1], rows + [rows[0]]):
            with self.assertRaises(ValueError):
                d.prepare_rows(b"\n".join(d.canonical(r) for r in changed), roster, "artificial_protocol", "gpt-6-luna")
        with self.assertRaises(ValueError):
            d.prepare_rows(b"\n".join(d.canonical(r) for r in rows), roster, "other", "gpt-6-luna")

    def test_roles_history_tools_sampling_and_extra_content_rejected(self):
        payload = fixture()[0][0]["payload_without_private_safety_identifier"]
        for key in ("tools", "instructions", "previous_response_id", "conversation", "temperature", "top_p", "seed", "safety_identifier", "metadata", "gold"):
            changed = copy.deepcopy(payload)
            changed[key] = []
            with self.assertRaises(ValueError):
                d.validate_payload(changed, "gpt-6-luna")
        for role in ("assistant", "system", "developer"):
            changed = copy.deepcopy(payload)
            changed["input"][0]["role"] = role
            with self.assertRaises(ValueError):
                d.validate_payload(changed, "gpt-6-luna")
        for change in ({"reasoning": {"effort": "high"}}, {"max_output_tokens": 16384}, {"store": True}, {"model": "gpt-6.1-sol"}):
            with self.assertRaises(ValueError):
                d.validate_payload(dict(payload, **change), "gpt-6-luna")

    def test_duplicate_json_keys_and_nonfinite_rejected(self):
        for text in ('{"model":1,"model":2}', '{"x":NaN}'):
            with self.assertRaises(ValueError):
                d.parse_json(text)

    def test_only_visible_assistant_output_is_extracted(self):
        response = {"output": [{"type": "reasoning", "summary": [{"type": "summary_text", "text": "GOLD MUST NOT COUNT"}]},
                                {"type": "message", "role": "user", "content": [{"type": "output_text", "text": "INJECTED"}]},
                                {"type": "message", "role": "assistant", "content": [{"type": "output_text", "text": "FINAL"}]}]}
        self.assertEqual(d.extract_visible(response), ("FINAL", False))

    def test_scope_gate_does_not_fabricate_provider_clearance(self):
        with tempfile.TemporaryDirectory() as root:
            _, manifest, _ = bundle_at(root)
            auth = authorization(manifest)
            auth.update(policy_warning_active=True, provider_response_reported=False)
            d.check_execution_gates(auth, gate(manifest), manifest)
            with self.assertRaises(ValueError):
                d.check_execution_gates({"inference_authorized": False}, gate(manifest), manifest)
            for field in ("scope_review_passed", "prior_flagged_requests_excluded", "no_broad_resume", "current_user_authorization_source", "frozen_roster_sha256", "risk_review_receipt_sha256"):
                changed = dict(auth)
                changed.pop(field)
                with self.assertRaises(ValueError):
                    d.check_execution_gates(changed, gate(manifest), manifest)

    def test_development_authorization_is_separate_and_non_circular(self):
        with tempfile.TemporaryDirectory() as root:
            _, manifest, _ = bundle_at(root)
            d.check_execution_gates(authorization(manifest, True), None, manifest, development=True)
            with self.assertRaises(ValueError):
                d.check_execution_gates(authorization(manifest, True), None, manifest)
            with self.assertRaises(ValueError):
                d.check_execution_gates(authorization(manifest), None, manifest)
            broken = gate(manifest)
            broken["dispatcher_sha256"] = "e" * 64
            with self.assertRaises(ValueError):
                d.check_execution_gates(authorization(manifest), broken, manifest)

    def test_actual_review_receipts_are_hashed_and_exactly_bound(self):
        with tempfile.TemporaryDirectory() as root:
            _, manifest, _ = bundle_at(root)
            receipt = {"scope_review_passed": True, "prior_flagged_requests_excluded": True,
                       "reviewed_bundles": [{"protocol_id": manifest["protocol_id"], "model": manifest["model"],
                           "frozen_roster_sha256": manifest["source_roster_sha256"],
                           "frozen_protocol_sha256": manifest["frozen_protocol_sha256"], "case_count": 3,
                           "task_ids": ["B01", "B03"]}]}
            path = Path(root) / "review.json"
            path.write_bytes(d.canonical(receipt))
            auth = authorization(manifest)
            auth["reviewed_input_receipt_sha256"] = auth["risk_review_receipt_sha256"] = d.sha(path.read_bytes())
            self.assertEqual(d.verify_review_receipts(auth, manifest, path, path)["reviewed_input_receipt_sha256"], d.sha(path.read_bytes()))
            with self.assertRaises(ValueError):
                d.verify_review_receipts(auth, manifest, None, path)
            with self.assertRaises(ValueError):
                d.verify_review_receipts(dict(auth, risk_review_receipt_sha256="f" * 64), manifest, path, path)
            for field, wrong in (("model", "other-model"), ("case_count", 2), ("frozen_roster_sha256", "0" * 64), ("protocol_id", "wrong-protocol")):
                changed = copy.deepcopy(receipt)
                changed["reviewed_bundles"][0][field] = wrong
                path.write_bytes(d.canonical(changed))
                auth["reviewed_input_receipt_sha256"] = auth["risk_review_receipt_sha256"] = d.sha(path.read_bytes())
                with self.assertRaisesRegex(ValueError, "exact case roster"):
                    d.verify_review_receipts(auth, manifest, path, path)

    def test_receipt_failures_precede_any_private_identity_read(self):
        with tempfile.TemporaryDirectory() as root:
            result, manifest, _ = bundle_at(root)
            auth = authorization(manifest, True)
            authfile = Path(root) / "scoped_auth.json"
            authfile.write_bytes(d.canonical(auth))
            args = argparse.Namespace(command="run-development", bundle=result["bundle"], bundle_sha256=result["bundle_sha256"],
                output=str(Path(root) / "out"), run_id="fixture_dev", workers=4,
                authorization=str(authfile), authorization_sha256=d.sha(authfile.read_bytes()),
                reviewed_input_receipt=None, risk_review_receipt=None)
            with mock.patch.object(d.Path, "home", side_effect=AssertionError("Credentials must not be touched")):
                with self.assertRaisesRegex(ValueError, "Actual input and risk"):
                    d.launch(args)
            self.assertFalse(Path(args.output).exists())

    def test_cost_guard_and_scope_do_not_auto_expand(self):
        with tempfile.TemporaryDirectory() as root:
            _, manifest, _ = bundle_at(root)
            for change in ({"estimated_max_run_cost_usd": 114}, {"spending_guard_usd": 500}, {"allowed_tasks": ["B01"]}, {"allowed_models": ["gpt-6.1-sol"]}):
                with self.assertRaises(ValueError):
                    d.check_execution_gates(dict(authorization(manifest), **change), gate(manifest), manifest)

    def test_real_landlock_worker_has_no_repository_access_and_no_network(self):
        with tempfile.TemporaryDirectory() as root:
            result, manifest, _ = bundle_at(root)
            output = Path(root) / "out"
            args = argparse.Namespace(command="dry-run", bundle=result["bundle"], bundle_sha256=result["bundle_sha256"], output=str(output), run_id="synthetic", workers=4)
            # The child has a fixed synthetic transport. No credentials supplied.
            with mock.patch.dict(os.environ, {"OPENAI_API_KEY": "UNREAD_SYNTHETIC_SECRET"}):
                summary = d.launch(args)
            self.assertEqual(summary["new_inference_calls"], 0)
            self.assertEqual(summary["saved"], 3)
            isolation = json.loads((output / "isolation_receipt.json").read_text())
            self.assertTrue(isolation["repository_read_probe_denied"])
            self.assertGreaterEqual(isolation["abi"], 1)
            lock = json.loads((output / "predictions_lock.json").read_text())
            self.assertFalse(lock["scoring_performed"])
            self.assertEqual(lock["frozen_protocol_sha256"], manifest["frozen_protocol_sha256"])
            for artifact in output.iterdir():
                self.assertNotIn(b"UNREAD_SYNTHETIC_SECRET", artifact.read_bytes())
                self.assertNotIn(b"synthetic-dry-run-identifier", artifact.read_bytes())

    def test_pinned_bundle_rejects_edit_extra_file_and_symlink(self):
        with tempfile.TemporaryDirectory() as root:
            result, _, _ = bundle_at(root)
            bundle = Path(result["bundle"])
            bundle.chmod(0o755)
            (bundle / "gold.json").write_text("invented gold")
            with self.assertRaises(ValueError):
                d.load_bundle(bundle, result["bundle_sha256"])
            (bundle / "gold.json").unlink()
            (bundle / "requests.jsonl").chmod(0o644)
            (bundle / "requests.jsonl").write_text("tampered")
            with self.assertRaises(ValueError):
                d.load_bundle(bundle, result["bundle_sha256"])

    def test_all_error_kinds_are_locked_without_retry_and_identifier_stays_private(self):
        with tempfile.TemporaryDirectory() as root:
            _, manifest, rows = bundle_at(root, count=5)
            output = Path(root) / "out"
            output.mkdir()
            outgoing = []
            replies = [reply(), reply("", "incomplete", incomplete_details={"reason": "max_output_tokens"}), reply(""), (500, b'{"error":"fixture"}'), ValueError("fixture")]
            def transport(body):
                self.assertTrue((output / f"case_{len(outgoing):05d}.dispatch_receipt.json").exists())
                outgoing.append(body)
                value = replies[len(outgoing) - 1]
                if isinstance(value, Exception):
                    raise value
                return value
            summary = d.run_cases(manifest, rows, output, "fixture_run", "PRIVATE_TEST_IDENTIFIER", transport, workers=1)
            self.assertEqual(len(outgoing), 5)
            self.assertEqual(summary["truncations"], 1)
            self.assertEqual(summary["empty_finals"], 4)
            self.assertEqual(summary["transport_or_response_errors"], 2)
            lock = json.loads((output / "predictions_lock.json").read_text())
            self.assertEqual([r["terminal_status"] for r in lock["rows"]], ["completed", "truncated", "empty_final", "http_error", "transport_error"])
            for i, body in enumerate(outgoing):
                submitted = json.loads(body)
                self.assertEqual(submitted.pop("safety_identifier"), "PRIVATE_TEST_IDENTIFIER")
                self.assertEqual(d.sha(d.canonical(submitted)), rows[i]["payload_sha256"])
                request = json.loads((output / lock["rows"][i]["request_path"]).read_text())
                self.assertEqual(request["actual_submitted_payload_sha256"], d.sha(body))
            for artifact in output.iterdir():
                self.assertNotIn(b"PRIVATE_TEST_IDENTIFIER", artifact.read_bytes())

    def test_model_not_found_access_error_stops_but_ordinary_404_does_not(self):
        self.assertTrue(d.stop_for_provider_error(404, b'{"error":{"code":"model_not_found"}}', "http_error"))
        self.assertTrue(d.stop_for_provider_error(404, b'{"error":{"type":"access_denied"}}', "http_error"))
        self.assertFalse(d.stop_for_provider_error(404, b'{"error":{"code":"resource_not_found"}}', "http_error"))
        with tempfile.TemporaryDirectory() as root:
            _, manifest, rows = bundle_at(root, count=3)
            output = Path(root) / "out"
            output.mkdir()
            calls = []
            def transport(body):
                calls.append(body)
                return 404, b'{"error":{"code":"model_not_found"}}'
            summary = d.run_cases(manifest, rows, output, "fixture_run", "PRIVATE", transport, workers=1)
            self.assertEqual(len(calls), 1)
            self.assertEqual(summary["not_dispatched"], 2)

    def test_actual_completed_development_outputs_are_verified(self):
        with tempfile.TemporaryDirectory() as root:
            _, manifest, rows = bundle_at(root, count=3)
            output = Path(root) / "dev"
            output.mkdir()
            d.run_cases(manifest, rows, output, "fixture_development", "PRIVATE", lambda _: reply(), workers=1)
            lock_path = output / "predictions_lock.json"
            review = gate(manifest)
            review.update(development_evidence_sha256=d.sha(lock_path.read_bytes()), development_protocol_id=manifest["protocol_id"],
                development_protocol_sha256=manifest["frozen_protocol_sha256"], development_roster_sha256=manifest["source_roster_sha256"],
                development_request_file_sha256=manifest["requests_sha256"], development_case_count=3)
            self.assertEqual(d.verify_development_evidence(review, manifest, lock_path), d.sha(lock_path.read_bytes()))
            with self.assertRaisesRegex(ValueError, "Actual completed"):
                d.verify_development_evidence(review, manifest, None)
            with self.assertRaises(ValueError):
                d.verify_development_evidence(dict(review, development_evidence_sha256="d" * 64), manifest, lock_path)
            with self.assertRaisesRegex(ValueError, "Wrong development"):
                d.verify_development_evidence(dict(review, development_protocol_id="wrong_dev"), manifest, lock_path)
            with self.assertRaises(ValueError):
                d.verify_development_evidence(dict(review, development_case_count=2), manifest, lock_path)
            artifact = output / "case_00000.response.json"
            artifact.chmod(0o644)
            artifact.write_bytes(b'{"tampered":true}')
            with self.assertRaises(ValueError):
                d.verify_development_evidence(review, manifest, lock_path)

    def test_policy_error_stops_future_calls_and_preserves_inflight(self):
        with tempfile.TemporaryDirectory() as root:
            _, manifest, rows = bundle_at(root, count=7)
            output = Path(root) / "out"
            output.mkdir()
            barrier = threading.Barrier(2)
            calls = []
            def transport(body):
                i = len(calls)
                calls.append(body)
                barrier.wait(timeout=5)
                if i == 0:
                    return 403, b'{"error":{"code":"bio_policy"}}'
                time.sleep(.1)
                return reply()
            summary = d.run_cases(manifest, rows, output, "fixture_run", "PRIVATE", transport, workers=2)
            self.assertEqual(len(calls), 2)
            self.assertEqual(summary["not_dispatched"], 5)
            self.assertTrue(summary["stopped_after_provider_policy_or_access_error"])
            lock = json.loads((output / "predictions_lock.json").read_text())
            self.assertEqual(len(lock["rows"]), 7)
            self.assertEqual(lock["new_inference_calls"], 2)

    def test_model_identity_mismatch_is_an_invalid_saved_response(self):
        with tempfile.TemporaryDirectory() as root:
            _, manifest, rows = bundle_at(root, count=1)
            output = Path(root) / "out"
            output.mkdir()
            d.run_cases(manifest, rows, output, "fixture", "PRIVATE", lambda _: reply(model="other"))
            lock = json.loads((output / "predictions_lock.json").read_text())
            self.assertEqual(lock["rows"][0]["terminal_status"], "response_error")
            self.assertEqual((output / "case_00000.final.txt").read_text(), "")

    def test_live_global_hold_refused_before_credentials_or_output(self):
        with tempfile.TemporaryDirectory() as root:
            result, _, _ = bundle_at(root)
            authfile = Path(root) / "held.json"
            authfile.write_text(json.dumps({"inference_authorized": False, "policy_warning_active": True}))
            gatefile = Path(root) / "gate.json"
            gatefile.write_text("{}")
            args = argparse.Namespace(command="run", bundle=result["bundle"], bundle_sha256=result["bundle_sha256"], output=str(Path(root) / "out"), run_id="forbidden", workers=4,
                authorization=str(authfile), authorization_sha256=d.sha(authfile.read_bytes()), development_gate=str(gatefile), development_gate_sha256=d.sha(gatefile.read_bytes()))
            with self.assertRaises(ValueError):
                d.launch(args)
            self.assertFalse(Path(args.output).exists())


if __name__ == "__main__":
    unittest.main()
