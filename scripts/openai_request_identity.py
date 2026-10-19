"""Stable end-user identity for OpenAI requests; contains no credentials."""
from __future__ import annotations

import json
from pathlib import Path
import re


DEFAULT_IDENTITY_FILE = Path.home() / ".config/openai/request_identity.json"


def load_safety_identifier(path=DEFAULT_IDENTITY_FILE):
    data = json.loads(Path(path).read_text())
    value = data.get("safety_identifier")
    if data.get("schema_version") != 1 or not isinstance(value, str):
        raise ValueError("A configured stable end-user safety identifier is required")
    if re.fullmatch(r"[A-Za-z0-9_-]{1,128}", value) is None:
        raise ValueError("Invalid safety identifier")
    return value


def with_safety_identifier(payload, identifier):
    """Copy a payload without allowing a caller to switch end-user identities."""
    if not isinstance(identifier, str) or re.fullmatch(r"[A-Za-z0-9_-]{1,128}", identifier) is None:
        raise ValueError("Invalid safety identifier")
    existing = payload.get("safety_identifier")
    if existing is not None and existing != identifier:
        raise ValueError("Request attempts to change the configured end-user identity")
    return {**payload, "safety_identifier": identifier}
