"""Three fixed, benign connectivity checks; never dispatch benchmark data."""
from __future__ import annotations

import argparse
from datetime import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import time
import urllib.error
import urllib.request
from zoneinfo import ZoneInfo

from openai_request_identity import load_safety_identifier, with_safety_identifier


CASES = (
    ("connectivity", "Reply with exactly: OK", "OK"),
    ("arithmetic", "What is 2 + 2? Reply with the number only.", "4"),
    ("basic_terminology", "What does DNA stand for? Reply with the expanded name only.", "deoxyribonucleic acid"),
)


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        raise RuntimeError("Redirect refused")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    private = Path.home() / ".config/openai"
    parser.add_argument("--key-file", type=Path, default=private / "api_key")
    parser.add_argument("--identity-file", type=Path, default=private / "request_identity.json")
    parser.add_argument("--output", type=Path, default=private / "last_safety_identifier_test.json")
    args = parser.parse_args()
    identifier = load_safety_identifier(args.identity_file)
    key = args.key_file.read_text().strip()
    opener = urllib.request.build_opener(NoRedirect)
    rows = []
    for name, prompt, expected in CASES:
        payload = with_safety_identifier({"model": "gpt-6-luna", "input": prompt,
            "reasoning": {"effort": "none"}, "max_output_tokens": 64,
            "service_tier": "default", "store": False}, identifier)
        request = urllib.request.Request("https://api.openai.com/v1/responses",
            data=json.dumps(payload).encode(), method="POST",
            headers={"Authorization": "Bearer " + key, "Content-Type": "application/json"})
        started = time.monotonic()
        row = {"case": name, "prompt": prompt, "safety_identifier_sha256": hashlib.sha256(identifier.encode()).hexdigest()}
        try:
            with opener.open(request, timeout=45) as response:
                result = json.load(response)
                row.update(http_status=response.status, request_id=response.headers.get("x-request-id"))
            output = "".join(content.get("text", "") for item in result.get("output", [])
                for content in item.get("content", []) if content.get("type") == "output_text")
            row.update(status=result.get("status"), output=output.replace(key, "[REDACTED]"),
                model=result.get("model"), usage=result.get("usage"),
                passed=result.get("status") == "completed" and output.strip().lower() == expected.lower())
        except urllib.error.HTTPError as exc:
            try:
                error = json.loads(exc.read()).get("error", {})
            except (ValueError, OSError):
                error = {}
            row.update(passed=False, http_status=exc.code,
                error_code=error.get("code") if re.fullmatch(r"[A-Za-z0-9_-]{1,80}", str(error.get("code", ""))) else None)
        except Exception as exc:
            row.update(passed=False, error_type=type(exc).__name__)
        row["elapsed_seconds"] = round(time.monotonic() - started, 3)
        rows.append(row)
        if row.get("http_status") != 200:
            break  # No identifier changes or retries after a provider rejection.
    report = {"tested_at_pacific": datetime.now(ZoneInfo("America/Los_Angeles")).isoformat(),
        "kind": "BENIGN_SAFETY_IDENTIFIER_CONNECTIVITY_TEST", "cases": rows,
        "all_passed": len(rows) == len(CASES) and all(row["passed"] for row in rows),
        "one_stable_identifier_for_all_requests": True, "identifier_rotations": 0,
        "retries": 0, "benchmark_requests_dispatched": 0}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fd = os.open(args.output, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w") as handle:
        json.dump(report, handle, indent=2)
        handle.write("\n")
    print(json.dumps(report))


if __name__ == "__main__":
    main()
