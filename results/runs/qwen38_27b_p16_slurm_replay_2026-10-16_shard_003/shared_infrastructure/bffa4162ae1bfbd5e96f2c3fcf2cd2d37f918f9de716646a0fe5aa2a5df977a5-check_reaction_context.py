"""CPU tokenizer-only proof that every complete P16 input fits without truncation."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def input_ids(encoded):
    values = encoded["input_ids"] if hasattr(encoded, "keys") else encoded
    if values and isinstance(values[0], list):
        if len(values) != 1:
            raise ValueError("Expected one tokenized chat")
        values = values[0]
    if any(type(value) is not int for value in values):
        raise ValueError("Unexpected tokenizer return schema")
    return values


def check():
    from transformers import AutoTokenizer
    folder = ROOT / "data/catalog_reaction/P16"
    largest, max_bytes, rows, min_seq, max_seq = None, 0, 0, 10**8, 0
    with (folder / "model_inputs.jsonl").open() as handle:
        for line in handle:
            row = json.loads(line); rows += 1
            size = len(row["prompt"].encode())
            seqsize = len(row["fields"]["sequence"].encode())
            min_seq, max_seq = min(min_seq, seqsize), max(max_seq, seqsize)
            if size > max_bytes:
                max_bytes, largest = size, row
    if rows != 5651:
        raise ValueError("Native complete test count changed")
    tokenizer = AutoTokenizer.from_pretrained(str(ROOT / "models/Qwen3.8-27B"), local_files_only=True)
    if type(tokenizer).__name__ != "Qwen2Tokenizer":
        raise ValueError("Recheck byte-level bound for changed tokenizer")
    def count(content):
        return len(input_ids(tokenizer.apply_chat_template([{"role": "user", "content": content}],
            tokenize=True, add_generation_prompt=True, enable_thinking=True, reasoning_effort="medium")))
    actual, empty = count(largest["prompt"]), count("")
    class_tokens = len(tokenizer.encode((folder / "class_context.txt").read_text(), add_special_tokens=False))
    conservative = max_bytes + 1024 + 4096
    if not (class_tokens < actual and actual + 4096 < 262144 and conservative < 262144 and empty < 1024):
        raise ValueError("Complete input/output context bound failed")
    report = {"task_id": "P16", "model": "Qwen/Qwen3.8-27B",
              "model_revision": "1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0", "tokenizer_class": type(tokenizer).__name__,
              "cases_checked_for_input_byte_length": rows, "full_class_context_tokens": class_tokens,
              "largest_input_by_bytes": {"case_id": largest["case_id"], "utf8_bytes": max_bytes,
                    "actual_chat_template_tokens_without_truncation": actual}, "empty_user_chat_template_tokens": empty,
              "source_sequence_bytes": {"min": min_seq, "max": max_seq},
              "all_case_conservative_input_plus_output_token_bound": conservative,
              "bound_basis": "Max complete input UTF8bytes +1024fixed-chat/control reserve +4096output. Pinned byte-level Qwen2 BPE tokencount cannot exceed raw bytecount; actual complete longest-byte prompt also tokenized with no truncation.",
              "model_context_limit": 262144, "frozen_output_tokens": 4096,
              "fits_without_any_input_truncation": True, "inference_dispatched": 0}
    (ROOT / "reports/catalog_reaction_context_validation.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report))
    return report


if __name__ == "__main__":
    check()
