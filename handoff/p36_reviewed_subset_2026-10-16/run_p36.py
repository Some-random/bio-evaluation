"""Hash-gated n=1 runner. Preparation alone cannot authorize dispatch."""
import argparse
import concurrent.futures
from datetime import datetime, timezone
import fcntl
import json
from pathlib import Path
import urllib.error
import urllib.parse
import urllib.request

from p36_contract import ROOT, digest, file_digest, payload, validate_cases, write_json


def execute(config_path, authorization_path, endpoint, run_dir):
    run_dir.mkdir(parents=True, exist_ok=True)
    with (run_dir / ".runner.lock").open("a") as handle:
        fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        return execute_locked(config_path, authorization_path, endpoint, run_dir)


def execute_locked(config_path, authorization_path, endpoint, run_dir):
    config = json.loads(config_path.read_text())
    approval = json.loads(authorization_path.read_text())
    if approval.get("execution_authorized") is not True or approval.get("configuration_sha256") != file_digest(config_path):
        raise ValueError("Require a separate exact-config execution approval")
    if approval.get("endpoint") != endpoint or approval.get("run_directory") != str(run_dir.resolve()):
        raise ValueError("Endpoint/run directory differs from exact execution approval")
    parsed_endpoint = urllib.parse.urlparse(endpoint)
    if parsed_endpoint.scheme != "http" or parsed_endpoint.hostname not in {"localhost", "127.0.0.1", "::1"}:
        raise ValueError("Only a separately approved local HTTP vLLM endpoint is permitted")
    if parsed_endpoint.path.rstrip("/") != "/v1" or parsed_endpoint.username or parsed_endpoint.password:
        raise ValueError("Unexpected endpoint")
    cases, _ = validate_cases(config)
    run_dir.mkdir(parents=True, exist_ok=True)
    manifest = {"configuration": config, "configuration_sha256": file_digest(config_path),
                "approval_sha256": file_digest(authorization_path), "endpoint": endpoint,
                "case_contract_sha256": digest(cases)}
    manifest_path = run_dir / "run_manifest.json"
    if manifest_path.exists() and json.loads(manifest_path.read_text()) != manifest:
        raise ValueError("Existing run differs from frozen condition")
    write_json(manifest_path, manifest)
    for name in ["requests", "responses"]:
        (run_dir / name).mkdir(exist_ok=True)

    def one(case):
        identity = digest([case["task"], case["variant"], case["case_id"]])
        request_path = run_dir / "requests" / (identity + ".json")
        response_path = run_dir / "responses" / (identity + ".json")
        body = payload(case, config)
        request_hash = digest(body)
        if response_path.exists():
            response = json.loads(response_path.read_text())
            if response.get("request_sha256") != request_hash:
                raise ValueError("Existing response request mismatch")
            return response["status"]
        if request_path.exists():
            # A previous request may have consumed a generation. Never regenerate it.
            return "ambiguous_prior_dispatch_held_no_retry"
        record = {"task": "P36", "case_id": case["case_id"], "variant": case["variant"],
                  "model": config["model"], "model_revision": config["model_revision"],
                  "request_sha256": request_hash,
                  "created_at_utc": datetime.now(timezone.utc).isoformat()}
        write_json(request_path, {**record, "payload": body})
        req = urllib.request.Request(endpoint.rstrip("/") + "/chat/completions",
                                     data=json.dumps(body).encode(), headers={"Content-Type": "application/json"})
        response = {**record}
        try:
            with urllib.request.urlopen(req, timeout=7200) as handle:
                raw = handle.read().decode()
                response.update(http_status=handle.status, raw_response_body=raw)
            decoded = json.loads(raw)
            choices = decoded["choices"]
            if len(choices) != 1 or not isinstance(choices[0]["message"].get("content"), str):
                raise ValueError("Require one final-content string")
            response.update(status="completed", response=decoded, text=choices[0]["message"]["content"],
                            finish_reason=choices[0].get("finish_reason"))
        except urllib.error.HTTPError as error:
            response.update(status="http_error_no_retry", http_status=error.code,
                            raw_response_body=error.read().decode(errors="replace"))
        except Exception as error:
            response.update(status="error_or_unknown_completion_no_retry", error=type(error).__name__ + ": " + str(error))
        response["saved_at_utc"] = datetime.now(timezone.utc).isoformat()
        write_json(response_path, response)
        return response["status"]

    with concurrent.futures.ThreadPoolExecutor(max_workers=config["concurrency"]) as pool:
        statuses = list(pool.map(one, cases))
    write_json(run_dir / "dispatch_summary.json", {"planned": len(cases),
               "statuses": {value: statuses.count(value) for value in sorted(set(statuses))},
               "resampling_or_retries": False})


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=ROOT / "proposed_config.json")
    parser.add_argument("--authorization", type=Path, required=True)
    parser.add_argument("--endpoint", required=True)
    parser.add_argument("--run-dir", type=Path, required=True)
    args = parser.parse_args()
    execute(args.config, args.authorization, args.endpoint, args.run_dir)
