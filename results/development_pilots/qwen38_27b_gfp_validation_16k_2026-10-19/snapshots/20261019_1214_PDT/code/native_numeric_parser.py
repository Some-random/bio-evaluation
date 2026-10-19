"""Exact P07 numerical parser snapshot; no references or scoring are loaded."""
import math
import re

def parse_number(text):
    match = re.fullmatch(r"\s*(?:Answer\s*:\s*)?([+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?)\s*", text or "", re.IGNORECASE)
    if not match:
        return None
    value = float(match.group(1))
    return value if math.isfinite(value) else None
