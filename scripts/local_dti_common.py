"""Frozen, input-only first-token likelihood protocol for the local DTI adapter."""
import hashlib
import json
import math
from pathlib import Path
import re
import urllib.error
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
MODEL = "Qwen/Qwen3.8-27B"
REVISION = "1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0"
LABELS = {"Yes": 9175, "No": 2665}
CLOSED_THINKING_SUFFIX = [248045, 74455, 198, 248068, 271, 248069, 271]
VARIANT = "QWEN_DTI_FIRST_TOKEN_CONDITIONAL_YES_NO_LIKELIHOOD"
GENERATION = {"max_tokens": 1, "temperature": 1.0, "top_p": 1.0, "top_k": -1, "min_p": 0.0,
              "n": 1, "seed": 42, "chat_template_kwargs": {"enable_thinking": False},
              "allowed_token_ids": [9175, 2665], "logprobs": True, "top_logprobs": 2,
              "logprob_token_ids": [9175, 2665], "return_tokens_as_token_ids": True, "return_token_ids": True}


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def file_digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")
    temporary.chmod(0o600)
    temporary.replace(path)


def validate_endpoint(endpoint, server):
    url = urllib.parse.urlsplit(endpoint)
    if (url.scheme != "http" or url.hostname != "127.0.0.1" or url.port != server.get("port", 8026)
            or url.path != "/v1" or url.query or url.fragment or url.username or url.password):
        raise ValueError("Endpoint differs from the pinned loopback server identity")


def validate_server(server, settings):
    if server["model"] != MODEL or server["revision"] != REVISION or settings["model"] != MODEL or settings["model_revision"] != REVISION:
        raise ValueError("Model/checkpoint differs from the frozen protocol")
    ticks = Path(f"/proc/{server['pid']}/stat").read_text().split()[21]
    if ticks != server["proc_start_ticks"]:
        raise ValueError("Server PID identity changed")
    validate_endpoint(settings["endpoint"], server)


def call(endpoint, payload=None, timeout=180):
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    request = urllib.request.Request(endpoint, data=json.dumps(payload, ensure_ascii=False).encode() if payload is not None else None,
                                     headers={"Content-Type": "application/json"})
    try:
        with opener.open(request, timeout=timeout) as response:
            return response.status, json.load(response)
    except urllib.error.HTTPError as error:
        return error.code, {"error": {"type": "HTTPError"}}
    except (urllib.error.URLError, OSError, TimeoutError, ValueError) as error:
        return 0, {"error": {"type": type(error).__name__}}


def payload_for(case, settings):
    if settings["generation"] != GENERATION:
        raise ValueError("Likelihood settings changed; no alternate budget/sampling protocol")
    if settings["approved_task_ids"] != ["P43"] or settings["model"] != MODEL or settings["model_revision"] != REVISION:
        raise ValueError("Task/model outside this fixed adapter")
    if set(case) != {"task", "case_id", "variant", "split", "messages"}:
        raise ValueError("Unexpected input field; scorer labels cannot be dispatched")
    if case["task"] != "P43" or case["variant"] != VARIANT or settings["variant"] != VARIANT:
        raise ValueError("Protocol identity mismatch")
    if len(case["messages"]) != 1 or set(case["messages"][0]) != {"role", "content"}:
        raise ValueError("Require exactly one original input string")
    message = case["messages"][0]
    if message["role"] != "user" or not isinstance(message["content"], str):
        raise ValueError("Unexpected input modality")
    return {"model": MODEL, "messages": case["messages"], **GENERATION}


def conditional_probability(logp_yes, logp_no):
    if not all(isinstance(x, (int, float)) and math.isfinite(x) and x <= 1e-5 for x in [logp_yes, logp_no]):
        raise ValueError("Require finite raw log-probabilities, not logits or hard labels")
    maximum = max(logp_yes, logp_no)
    yes, no = math.exp(logp_yes - maximum), math.exp(logp_no - maximum)
    score = yes / (yes + no)
    mass = math.exp(logp_yes) + math.exp(logp_no)
    if mass > 1.00005:
        raise ValueError("Two raw token probabilities exceed total vocabulary mass")
    return {"positive_score": score, "negative_score": 1.0 - score,
            "logprob_yes": logp_yes, "logprob_no": logp_no,
            "raw_pair_probability_mass": mass,
            "log_odds_yes_no": logp_yes - logp_no}


def extract_score(response):
    if response.get("model") != MODEL or len(response.get("choices", [])) != 1:
        raise ValueError("Response model/count mismatch")
    choice = response["choices"][0]
    tokens = choice.get("token_ids")
    if not isinstance(tokens, list) or len(tokens) != 1 or tokens[0] not in LABELS.values():
        raise ValueError("Expected exactly one allowed token ID")
    entries = choice.get("logprobs", {}).get("content")
    if not isinstance(entries, list) or len(entries) != 1:
        raise ValueError("Expected first generated token logprobs")
    candidates = {}
    for item in entries[0].get("top_logprobs", []):
        match = re.fullmatch(r"token_id:([0-9]+)", item.get("token", ""))
        if match is None:
            raise ValueError("Require explicit token-ID logprob identity")
        token = int(match.group(1))
        if token in candidates:
            raise ValueError("Duplicate candidate logprob")
        candidates[token] = item["logprob"]
    if set(candidates) != set(LABELS.values()):
        raise ValueError("Both fixed label logprobs must be available; no inferred missing value")
    expected_token = "token_id:" + str(tokens[0])
    if entries[0].get("token") != expected_token:
        raise ValueError("Sampled token provenance mismatch")
    sampled_logprob = entries[0].get("logprob")
    if not isinstance(sampled_logprob, (float, int)) or not math.isclose(sampled_logprob, candidates[tokens[0]], rel_tol=1e-6, abs_tol=1e-6):
        raise ValueError("Sampled/candidate raw logprobs disagree")
    message = choice.get("message", {})
    expected_text = next(label for label, token in LABELS.items() if token == tokens[0])
    if (message.get("role") != "assistant" or message.get("content") != expected_text or message.get("reasoning")
            or message.get("reasoning_content") or message.get("tool_calls") or message.get("function_call") or message.get("refusal")):
        raise ValueError("Unexpected generated content or reasoning")
    usage = response.get("usage", {})
    if usage.get("completion_tokens") != 1 or usage.get("completion_tokens_details", {}).get("reasoning_tokens") != 0:
        raise ValueError("Output violates one-token/no-thinking protocol")
    if choice.get("finish_reason") != "length":
        raise ValueError("Expected fixed one-token budget finish")
    prompt_ids = response.get("prompt_token_ids")
    if (not isinstance(prompt_ids, list) or not all(isinstance(t, int) for t in prompt_ids)
            or prompt_ids[-len(CLOSED_THINKING_SUFFIX):] != CLOSED_THINKING_SUFFIX
            or usage.get("prompt_tokens") != len(prompt_ids)):
        raise ValueError("Prompt token/channel audit failed; require pinned closed-thinking suffix")
    result = conditional_probability(candidates[LABELS["Yes"]], candidates[LABELS["No"]])
    result.update(sampled_token_id=tokens[0], sampled_label=expected_text,
                  prompt_token_ids_sha256=digest(prompt_ids), prompt_token_count=len(prompt_ids), reasoning_tokens=0,
                  system_fingerprint=response.get("system_fingerprint"),
                  score_basis="Both raw FIRST-token conditional log-likelihoods; sampled label is not the ranking score")
    return result
