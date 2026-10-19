"""Frozen, tool-free Responses evaluations with resumability and a shared cost guard."""
import argparse
import concurrent.futures as cf
import datetime as dt
import fcntl
import hashlib
import json
import os
from pathlib import Path
import sqlite3
import threading
import time

import requests

from openai_request_identity import load_safety_identifier, with_safety_identifier

ROOT = Path(__file__).resolve().parents[1]
PST = dt.timezone(dt.timedelta(hours=-8))
MODEL = "gpt-6-luna"


def encoded(value):
    return json.dumps(value, ensure_ascii=False, separators=(",", ":")).encode()


def digest(value):
    return hashlib.sha256(encoded(value)).hexdigest()


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_bytes(encoded(value) + b"\n")
    temporary.chmod(0o600)
    temporary.replace(path)


def usage_cost(usage):
    count = usage["input_tokens"]
    details = usage.get("input_tokens_details") or {}
    cached, writes = details.get("cached_tokens", 0), details.get("cache_write_tokens", 0)
    rate = 2 if count > 272000 else 1
    return (max(0, count - cached - writes) * .10 * rate + cached * .01 * rate
            + writes * .125 * rate + usage["output_tokens"] * .50 * (1.5 if count > 272000 else 1)) / 1e6


class Ledger:
    def __init__(self, path, cap=50):
        self.path, self.cap = path, cap
        path.parent.mkdir(parents=True, exist_ok=True)
        with self.connect() as db:
            db.execute("CREATE TABLE IF NOT EXISTS calls (id TEXT PRIMARY KEY, upper REAL, charge REAL, state TEXT)")

    def connect(self):
        return sqlite3.connect(self.path, timeout=60, isolation_level="IMMEDIATE")

    def reserve(self, identity, upper):
        with self.connect() as db:
            db.execute("BEGIN IMMEDIATE")
            if db.execute("SELECT 1 FROM calls WHERE id=?", (identity,)).fetchone():
                return False
            total = db.execute("SELECT COALESCE(SUM(COALESCE(charge, upper)),0) FROM calls").fetchone()[0]
            if total + upper > self.cap:
                return False
            db.execute("INSERT INTO calls VALUES (?,?,NULL,'reserved')", (identity, upper))
            return True

    def finish(self, identity, charge, state):
        with self.connect() as db:
            db.execute("UPDATE calls SET charge=?,state=? WHERE id=?", (charge, state, identity))

    def summary(self):
        with self.connect() as db:
            rows = db.execute("SELECT state,COUNT(*),SUM(COALESCE(charge,upper)) FROM calls GROUP BY state").fetchall()
        return {"accounted_usd":sum(x[2] for x in rows), "cap_usd":self.cap,
                "states":{x[0]:x[1] for x in rows}}


class Client:
    def __init__(self, key):
        self.key = key
        self.local = threading.local()

    def post(self, endpoint, payload):
        if not hasattr(self.local, "session"):
            self.local.session = requests.Session()
            self.local.session.headers.update({"Authorization":"Bearer " + self.key})
        try:
            response = self.local.session.post("https://api.openai.com/v1/" + endpoint,
                json=payload, timeout=(20, 900))
            value = response.json()
            # An error message can echo credential fragments; keep safe codes only.
            if response.status_code != 200:
                error = value.get("error") or {}
                value = {"error":{"type":error.get("type"), "code":error.get("code")}}
            return response.status_code, value
        except (requests.RequestException, ValueError) as exc:
            self.local.session.close()
            del self.local.session
            return 0, {"error":{"type":type(exc).__name__}}


def payload_for(case):
    if "DRAFT" in case["variant"]:
        raise ValueError("Unreviewed protocol cannot be executed")
    if case.get("payload"):
        payload = dict(case["payload"])
        if payload.get("model") != MODEL or payload.get("tools"):
            raise ValueError("Only the frozen model and tool-free inputs are authorized")
    else:
        payload = {"model":MODEL, "input":[{"role":"user", "content":case["prompt"]}],
                   "reasoning":{"effort":"max" if case["task"] == "P18" else "medium"},
                   "max_output_tokens":128000 if case["task"] == "P18" else 4096,
                   "store":False, "tools":[]}
        if case.get("system"):
            payload["input"].insert(0, {"role":"system", "content":case["system"]})
    return payload


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inputs", required=True)
    parser.add_argument("--tasks", nargs="+")
    parser.add_argument("--run", required=True)
    parser.add_argument("--key-file")
    parser.add_argument("--identity-file", type=Path, default=Path.home() / ".config/openai/request_identity.json")
    parser.add_argument("--concurrency", type=int, default=8)
    args = parser.parse_args()
    auth = json.loads((ROOT / "configs/execution_authorization.json").read_text())
    if auth.get("policy_warning_active"):
        raise SystemExit("Policy warning hold is active. No API calls are permitted pending review.")
    if not auth.get("inference_authorized") or auth["model"] != MODEL:
        raise SystemExit("Inference is not authorized for this model.")
    safety_identifier = load_safety_identifier(args.identity_file)
    key = os.environ.get("OPENAI_API_KEY") or (Path(args.key_file).read_text().strip() if args.key_file else None)
    if not key or "\n" in key:
        raise SystemExit("A runtime API credential is required.")
    path = Path(args.inputs)
    cases = [json.loads(line) for line in path.read_text().splitlines() if line]
    if args.tasks:
        cases = [c for c in cases if c["task"] in args.tasks]
    if not cases:
        raise SystemExit("No eligible cases.")
    if len({(c["task"],c["case_id"],c["variant"]) for c in cases}) != len(cases):
        raise SystemExit("Duplicate case identities.")
    for case in cases:
        payload_for(case)
    folder = ROOT / "results/runs" / args.run
    folder.mkdir(parents=True, exist_ok=True)
    lock = (folder / "worker.lock").open("a")
    try:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        raise SystemExit("This run already has an active worker.")
    fixed = {"model":MODEL, "planned_cases":len(cases), "case_contract_sha256":digest(cases),
             "safety_identifier":safety_identifier,
             "tools":[], "input_file_sha256":hashlib.sha256(path.read_bytes()).hexdigest(),
             "protocols":sorted({c["variant"] for c in cases}),
             "model_selection_on_test":False, "global_guard_usd":auth["initial_agent_spending_guard_usd"]}
    manifest = folder / "run_manifest.json"
    if manifest.exists() and json.loads(manifest.read_text()) != fixed:
        raise SystemExit("Frozen run manifest differs; use a distinct run ID.")
    write_json(manifest, fixed)
    ledger = Ledger(ROOT / "results/api_spend.sqlite", auth["initial_agent_spending_guard_usd"])
    client = Client(key)
    permanent = threading.Event()

    def execute(case):
        identity = digest([args.run,case["task"],case["variant"],case["case_id"]])
        output_path = folder / "responses" / (identity + ".json")
        if output_path.exists():
            previous = json.loads(output_path.read_text())
            if previous.get("status") != "token_count_failed" or previous.get("token_count_attempt",1) >= 2:
                return "cached"
        else:
            previous = {}
        if permanent.is_set():
            return "provider_blocked"
        payload = with_safety_identifier(payload_for(case), safety_identifier)
        request_hash = digest(payload)
        write_json(folder / "requests" / (identity + ".json"),
                   {"task":case["task"],"case_id":case["case_id"],"variant":case["variant"],
                    "split":case["split"],"request_sha256":request_hash,"payload":payload,
                    "supplied_fields":sorted(case.get("fields",{}))})
        count_payload = {k:v for k,v in payload.items() if k in {"model","input","instructions","tools","text"}}
        count_status, count_response = client.post("responses/input_tokens", count_payload)
        if count_status in [0,429,500,502,503,504]:
            time.sleep(2)
            count_status, count_response = client.post("responses/input_tokens", count_payload)
        tokens = count_response.get("input_tokens")
        if count_status != 200 or not isinstance(tokens, int):
            write_json(output_path,{"task":case["task"],"case_id":case["case_id"],"variant":case["variant"],
                         "split":case["split"],"status":"token_count_failed","http_status":count_status,
                         "error":count_response.get("error"),"request_sha256":request_hash,
                         "token_count_attempt":previous.get("token_count_attempt",0)+1})
            if count_status in [401,403,404]: permanent.set()
            return "token_count_failed"
        if tokens + payload["max_output_tokens"] > 1050000:
            return "context_overflow"
        upper = (tokens * .125 * (2 if tokens > 272000 else 1)
                 + payload["max_output_tokens"] * .50 * (1.5 if tokens > 272000 else 1)) / 1e6
        for attempt in range(2):
            call_id = identity + ":" + str(attempt)
            if not ledger.reserve(call_id, upper):
                if attempt == 0:
                    with ledger.connect() as db:
                        older = db.execute("SELECT upper,charge,state FROM calls WHERE id=?",(call_id,)).fetchone()
                    if older is not None:
                        if older[2] == "reserved":
                            ledger.finish(call_id,older[0],"interrupted_unknown_charge")
                        continue
                return "budget_or_existing_reservation"
            started = time.time()
            status, response = client.post("responses", payload)
            usage = response.get("usage")
            cost = usage_cost(usage) if usage else upper if status == 0 or status == 200 else 0
            ledger.finish(call_id, cost, "completed" if status == 200 else "error")
            record = {"task":case["task"],"case_id":case["case_id"],"variant":case["variant"],
                      "split":case["split"], "request_sha256":request_hash,"http_status":status,
                      "exact_input_tokens":tokens, "response":response, "cost_usd":cost,
                      "attempt":attempt,"elapsed_seconds":round(time.time()-started,2),
                      "checked_at_pst":dt.datetime.now(PST).isoformat()}
            if status == 200:
                record["status"] = response.get("status","unknown")
                if response.get("model") != MODEL:
                    record["status"] = "model_identity_mismatch"
                record["text"] = "".join(c.get("text","") for item in response.get("output",[])
                                           for c in item.get("content",[]) if c.get("type") == "output_text")
            else:
                record["status"] = "transport_error" if status == 0 else "provider_error"
            write_json(folder / "attempts" / (identity + "." + str(attempt) + ".json"), record)
            if status == 200 or status not in [0,429,500,502,503,504] or attempt == 1:
                write_json(output_path, record)
                if status in [401,403,404] or response.get("error",{}).get("code") in {"insufficient_quota","bio_policy","identifier_blocked"}:
                    permanent.set()
                return record["status"]
            time.sleep(2 * (attempt + 1))

    counts = {}
    started = time.time()
    with cf.ThreadPoolExecutor(max_workers=args.concurrency) as pool:
        futures = [pool.submit(execute,c) for c in cases]
        for i,future in enumerate(cf.as_completed(futures), 1):
            try: status = future.result()
            except Exception:
                status = "worker_exception"
                permanent.set()
            counts[status] = counts.get(status,0) + 1
            if i % 10 == 0 or i == len(cases):
                progress = {"run":args.run,"finished":i,"planned":len(cases),"statuses":counts,
                            "elapsed_seconds":round(time.time()-started),"spend":ledger.summary()}
                write_json(folder / "progress.json", progress)
                print(json.dumps(progress), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
