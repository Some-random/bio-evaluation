"""Verify the explicitly authorized GitHub publication destination."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

REPOSITORY = "Some-random/bio-evaluation"
POLICY_PATH = "configs/publication_destination.json"


def verify_repository_metadata(repository, root):
    raw = (Path(root) / POLICY_PATH).read_bytes()
    policy = json.loads(raw)
    if policy.get("repository") != REPOSITORY or policy.get("visibility") not in {"private", "public"}:
        raise RuntimeError("Unexpected publication destination policy")
    if policy.get("publication_authorized") is not True:
        raise RuntimeError("Publication destination is not explicitly authorized")
    if policy["visibility"] == "public":
        authorization = policy.get("user_authorization", {})
        if (authorization.get("quote") != "prepare everytying publicly"
                or not authorization.get("recorded_at_utc")):
            raise RuntimeError("Public publication requires the recorded user instruction")
    if repository.get("full_name") != REPOSITORY or type(repository.get("private")) is not bool:
        raise RuntimeError("GitHub repository identity or visibility was not verified")
    observed = "private" if repository["private"] else "public"
    if observed != policy["visibility"] or repository.get("visibility", observed) != observed:
        raise RuntimeError("GitHub visibility differs from the authorized destination")
    if repository.get("permissions", {}).get("push") is not True:
        raise RuntimeError("Current GitHub credentials lack push permission")
    return {"repository": REPOSITORY, "private": repository["private"],
        "visibility": observed, "push_permission": True, "publication_authorized": True,
        "destination_policy": POLICY_PATH,
        "destination_policy_sha256": hashlib.sha256(raw).hexdigest(),
        "verified_at_utc": datetime.now(timezone.utc).isoformat()}
