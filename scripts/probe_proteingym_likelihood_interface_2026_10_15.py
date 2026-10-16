"""At most two synthetic nonbiological teacher-forced loopback interface probes.

This is an interface audit, not benchmark authorization or a scoring protocol.
No model weights are loaded by this process; only the local CPU tokenizer.
"""
from __future__ import annotations

import base64
import datetime as dt
import hashlib
import importlib.metadata
import json
import math
from pathlib import Path
import sys
import time
import urllib.request

from transformers import AutoTokenizer

import run_local_labbench_eight_gpu as serving_helpers


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "sources/proteingym_likelihood_interface_2026-10-15"
MODEL = "Qwen/Qwen3.8-27B"
REVISION = "1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0"
ENDPOINT = "http://127.0.0.1:8026/v1"
VLLM = ROOT / ".venv-vllm/lib/python3.12/site-packages/vllm"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def save(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        raise FileExistsError(f"Refuse to overwrite audit artifact: {path}")
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def tokens(tok, text):
    result = tok(text, add_special_tokens=False, return_offsets_mapping=True)
    return {"text": text, "utf8_base64": base64.b64encode(text.encode()).decode(),
            "token_ids": result["input_ids"], "character_offsets": result["offset_mapping"],
            "single_token_decodes": [tok.decode([i], skip_special_tokens=False) for i in result["input_ids"]]}


def score_proof(response, ids, start, end, eos_index):
    assert len(response["choices"]) == 1
    choice = response["choices"][0]
    assert choice["prompt_token_ids"] == ids, "Server retokenized or modified supplied IDs"
    values = choice["prompt_logprobs"]
    assert len(values) == len(ids) and values[0] is None
    token_rows = []
    for i, (token_id, entry) in enumerate(zip(ids, values)):
        if i == 0:
            token_rows.append({"position": i, "token_id": token_id, "logprob": None})
            continue
        assert set(entry) == {str(token_id)}, "Unexpected top-N or missing actual token"
        lp = entry[str(token_id)]["logprob"]
        assert isinstance(lp, (int, float)) and math.isfinite(lp) and lp <= 0
        token_rows.append({"position": i, "token_id": token_id, **entry[str(token_id)]})
    suffix = [token_rows[i]["logprob"] for i in range(start, end)]
    complete = all(x is not None for x in suffix)
    return {
        "prompt_token_count": len(ids), "first_token_has_no_logprob": True,
        "actual_prompt_ids_match_cpu_tokenizer_or_supplied_ids": True,
        "selected_token_only_at_every_scored_position": True,
        "token_rows": token_rows, "target_token_start": start, "target_token_end_exclusive": end,
        "all_target_tokens_scored": complete,
        "target_sum_log_likelihood_if_all_scored": math.fsum(suffix) if complete else None,
        "sum_available_target_terms": math.fsum(x for x in suffix if x is not None),
        "explicit_eos_index": eos_index,
        "explicit_eos_logprob": token_rows[eos_index]["logprob"] if eos_index is not None else None,
        "generated_token_ids_ignored": choice.get("token_ids"),
        "generation_scores_used": False, "usage": response.get("usage"),
        "legacy_completion_logprobs": choice.get("logprobs"),
    }


def main() -> None:
    if OUT.exists():
        raise FileExistsError("Synthetic audit folder already exists; do not replay calls")
    OUT.mkdir(parents=True)
    settings = {"model": MODEL, "model_revision": REVISION, "gpu_ids": [5], "endpoint": ENDPOINT}
    serving = json.loads((ROOT / "configs/local_model.json").read_text())
    server = json.loads((ROOT / ".local/local_model_server.json").read_text())
    serving_helpers.validate_server_identity(server, settings, serving, serving_helpers.server_start_ticks(server["pid"]))
    assert serving["host"] == "127.0.0.1" and serving["port"] == 8026
    cmd = (Path(f"/proc/{server['pid']}/cmdline").read_bytes().decode().split("\0"))
    assert "--logprobs-mode" not in cmd, "Inspect any nondefault mode before scoring"
    assert str(ROOT / "models/Qwen3.8-27B") in cmd and MODEL in cmd
    if "--revision" in cmd:
        assert cmd[cmd.index("--revision") + 1] == REVISION
    save(OUT / "server_identity.json", {"record": server, "actual_start_ticks": serving_helpers.server_start_ticks(server["pid"]),
         "serving_file_sha256": sha((ROOT / "configs/local_model.json").read_bytes()),
         "command": cmd, "gpu0_touched": False, "new_server_started": False})
    installed = [
        "entrypoints/openai/completion/protocol.py", "entrypoints/openai/completion/serving.py",
        "entrypoints/generate/base/serving.py", "v1/worker/gpu_model_runner.py",
        "v1/worker/gpu/sample/prompt_logprob.py", "v1/sample/sampler.py", "config/model.py",
    ]
    receipts=[]
    for relative in installed:
        source = VLLM / relative
        data = source.read_bytes()
        dest = OUT / ("vllm__" + relative.replace("/", "__"))
        dest.write_bytes(data)
        receipts.append({"installed_file": str(source), "audit_copy": str(dest.relative_to(ROOT)),
                         "bytes": len(data), "sha256": sha(data)})
    tokenizer_paths = ["tokenizer.json", "tokenizer_config.json", "vocab.json", "merges.txt"]
    save(OUT / "source_receipts.json", {"installed_vllm_version": importlib.metadata.version("vllm"),
         "python": sys.version, "files": receipts,
         "tokenizer_files": [{"path": "models/Qwen3.8-27B/" + p, "sha256": sha((ROOT / "models/Qwen3.8-27B" / p).read_bytes())}
                             for p in tokenizer_paths]})
    tok = AutoTokenizer.from_pretrained(ROOT / "models/Qwen3.8-27B", local_files_only=True)
    ascii_text = "A toy clock reads 17:42."
    prefix, unicode_text = "score:\n", "café 🧩 Z\u0301"
    ascii_tokens, prefix_tokens, unicode_tokens = tokens(tok, ascii_text), tokens(tok, prefix), tokens(tok, unicode_text)
    merging_prefix, merging_target = "prefix: ", "painted cube"
    cpu = {
        "tokenizer_only_no_weights_loaded": True, "model": MODEL, "revision": REVISION,
        "bos_token": tok.bos_token, "bos_token_id": tok.bos_token_id,
        "eos_token": tok.eos_token, "eos_token_id": tok.eos_token_id, "vocabulary_size": len(tok),
        "automatic_special_tokens_added_for_ascii": tok.encode(ascii_text, add_special_tokens=True) != ascii_tokens["token_ids"],
        "ascii_no_prefix": ascii_tokens, "fixed_prefix": prefix_tokens, "unicode_target": unicode_tokens,
        "prefix_and_target_token_ids_equal_canonical_joint": prefix_tokens["token_ids"] + unicode_tokens["token_ids"] == tok.encode(prefix + unicode_text, add_special_tokens=False),
        "merging_counterexample": {"prefix": tokens(tok, merging_prefix), "target": tokens(tok, merging_target),
                                  "canonical_joint": tokens(tok, merging_prefix + merging_target),
                                  "separate_tokenization_equals_joint": tok.encode(merging_prefix, add_special_tokens=False) + tok.encode(merging_target, add_special_tokens=False) == tok.encode(merging_prefix + merging_target, add_special_tokens=False)},
    }
    save(OUT / "tokenizer_cpu_audit.json", cpu)
    cases = [
        {"case_id": "synthetic_ascii_no_prefix_no_eos", "prompt": ascii_text,
         "expected_ids": ascii_tokens["token_ids"], "target_start": 0, "target_end": len(ascii_tokens["token_ids"]), "eos_index": None},
        {"case_id": "synthetic_unicode_fixed_token_prefix_explicit_eos",
         "prompt": prefix_tokens["token_ids"] + unicode_tokens["token_ids"] + [tok.eos_token_id],
         "expected_ids": prefix_tokens["token_ids"] + unicode_tokens["token_ids"] + [tok.eos_token_id],
         "target_start": len(prefix_tokens["token_ids"]), "target_end": len(prefix_tokens["token_ids"]) + len(unicode_tokens["token_ids"]),
         "eos_index": len(prefix_tokens["token_ids"]) + len(unicode_tokens["token_ids"])},
    ]
    save(OUT / "synthetic_call_plan.json", {"created_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
         "authorization": "Root explicitly authorized1-2 tiny synthetic nonbiological interface calls on existingGPU5 loopback. No benchmark inputs, protocol approval or biological inference.",
         "cases": cases, "maximum_inference_requests": 2, "retries": 0})
    client = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    with client.open(ENDPOINT + "/models", timeout=10) as response:
        data = response.read()
    save(OUT / "models_identity.json", {"raw_utf8": data.decode(), "sha256": sha(data), "parsed": json.loads(data)})
    proofs=[]
    for case in cases:
        payload = {"model": MODEL, "prompt": case["prompt"], "max_tokens": 0, "echo": True,
                   "prompt_logprobs": 0, "n": 1, "stream": False, "add_special_tokens": False,
                   "return_token_ids": True, "return_tokens_as_token_ids": True,
                   "temperature": 0.0, "top_p": 1.0, "top_k": -1, "min_p": 0.0,
                   "frequency_penalty": 0.0, "presence_penalty": 0.0, "repetition_penalty": 1.0,
                   "seed": 42}
        wire = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).encode()
        save(OUT / (case["case_id"] + ".request.json"), {"payload": payload, "raw_utf8": wire.decode(),
             "wire_sha256": sha(wire), "endpoint": ENDPOINT + "/completions", "proxy_handler": {}})
        request = urllib.request.Request(ENDPOINT + "/completions", data=wire, headers={"Content-Type":"application/json"})
        start = time.monotonic()
        with client.open(request, timeout=180) as response:
            response_wire = response.read(); http_status=response.status; headers=dict(response.headers)
        elapsed = time.monotonic() - start
        parsed = json.loads(response_wire)
        save(OUT / (case["case_id"] + ".response.json"), {"http_status": http_status, "headers": headers,
             "elapsed_seconds": elapsed, "raw_base64": base64.b64encode(response_wire).decode(),
             "raw_utf8": response_wire.decode(), "wire_sha256": sha(response_wire), "wire_bytes": len(response_wire), "response": parsed})
        proof = score_proof(parsed, case["expected_ids"], case["target_start"], case["target_end"], case["eos_index"])
        proofs.append({"case_id": case["case_id"], "wire_bytes": len(response_wire), "elapsed_seconds": elapsed, **proof})
        save(OUT / (case["case_id"] + ".validation.json"), proofs[-1])
    save(OUT / "synthetic_proof_summary.json", {"synthetic_nonbiological_only": True, "benchmark_inputs_read": False,
         "inference_requests": len(proofs), "new_server_started": False, "no_proxy": True,
         "model": MODEL, "revision": REVISION, "gpu_ids": [5], "proofs": proofs})
    print(json.dumps({"folder": str(OUT.relative_to(ROOT)), "calls": len(proofs),
                      "proofs": [{"case_id": p["case_id"], "tokens": p["prompt_token_count"],
                                  "all_target_tokens_scored": p["all_target_tokens_scored"],
                                  "target_sum": p["target_sum_log_likelihood_if_all_scored"], "wire_bytes": p["wire_bytes"]}
                                 for p in proofs]}, indent=2))


if __name__ == "__main__":
    main()
