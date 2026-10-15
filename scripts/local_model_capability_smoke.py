"""Fixed synthetic text, reasoning-interface and vision checks on loopback only."""
import base64
import hashlib
import io
import json
from pathlib import Path
import time
import urllib.request

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]


def main():
    settings = json.loads((ROOT / "configs/local_model.json").read_text())
    if settings["host"] != "127.0.0.1":
        raise SystemExit("Synthetic checks require loopback serving.")
    client = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    endpoint = f'http://127.0.0.1:{settings["port"]}/v1/chat/completions'
    png = io.BytesIO()
    Image.new("RGB", (128, 128), (0, 0, 255)).save(png, format="PNG")
    image_bytes = png.getvalue()
    image_url = "data:image/png;base64," + base64.b64encode(image_bytes).decode()
    cases = [
        ("text", "Reply exactly READY.", {"enable_thinking": False}, 16, "ready"),
        ("reasoning_interface", "What is 12 + 7? Reply with only the number.",
         {"enable_thinking": True, "reasoning_effort": "low"}, 512, "19"),
        ("vision", [
            {"type": "text", "text": "What color fills this image? Reply with one color word."},
            {"type": "image_url", "image_url": {"url": image_url}},
        ], {"enable_thinking": False}, 32, "blue"),
    ]
    records = []
    for name, content, template, budget, expected in cases:
        payload = {"model": settings["model"], "messages": [{"role": "user", "content": content}],
                   "max_tokens": budget, "temperature": 0,
                   "chat_template_kwargs": template}
        request = urllib.request.Request(endpoint, json.dumps(payload).encode(),
                                         {"Content-Type": "application/json"})
        start = time.monotonic()
        with client.open(request, timeout=300) as response:
            value = json.load(response)
        choice = value["choices"][0]
        message = choice["message"]
        text = message.get("content") or ""
        reasoning = message.get("reasoning") or message.get("reasoning_content") or ""
        record = {"check": name, "expected": expected, "text": text,
                  "passed": text.strip().lower().rstrip(".") == expected,
                  "finish_reason": choice.get("finish_reason"), "usage": value.get("usage"),
                  "latency_seconds": round(time.monotonic() - start, 3),
                  "chat_template_kwargs": template, "max_tokens": budget,
                  "reasoning_characters": len(reasoning)}
        if name == "vision":
            record["synthetic_image"] = {"size": [128, 128], "RGB": [0, 0, 255],
                                         "png_sha256": hashlib.sha256(image_bytes).hexdigest()}
        records.append(record)
        print(json.dumps(record), flush=True)
    result = {"model": settings["model"], "revision": settings["revision"],
              "gpu_ids": settings["gpu_ids"], "benchmark_cases_dispatched": 0,
              "scope": "synthetic checks only; not evidence of biological benchmark performance",
              "all_passed": all(r["passed"] for r in records), "checks": records}
    (ROOT / "reports/local_model_capability_smoke.json").write_text(json.dumps(result, indent=2) + "\n")
    if not result["all_passed"]:
        raise SystemExit("One or more synthetic checks failed; see the saved report.")


if __name__ == "__main__":
    main()
