"""Extract independent hash-pinned CPU runtimes inside the continuation job."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import posixpath
import subprocess
import tarfile
import zipfile


def sha(path):
    result = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(8 * 1024 * 1024), b""):
            result.update(chunk)
    return result.hexdigest()


def extract(record, target):
    if sha(record["path"]) != record["sha256"]:
        raise ValueError("CPU archive digest mismatch")
    target.mkdir(parents=True, exist_ok=True)
    with tarfile.open(record["path"]) as archive:
        for member in archive.getmembers():
            relative = PurePosixPath(member.name)
            if relative.is_absolute() or ".." in relative.parts or not (member.isfile() or member.isdir() or member.issym() or member.islnk()):
                raise ValueError("Unsafe CPU archive member")
            if member.issym() or member.islnk():
                link = member.linkname
                resolved = posixpath.normpath(posixpath.join(str(relative.parent), link) if member.issym() else link)
                if link.startswith("/") or resolved == ".." or resolved.startswith("../"):
                    raise ValueError("CPU archive link escapes its runtime")
        archive.extractall(target)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--config-sha256", required=True)
    parser.add_argument("--runtime-dir", type=Path, required=True)
    args = parser.parse_args()
    if sha(args.config) != args.config_sha256:
        raise ValueError("Continuation startup config changed")
    config = json.loads(args.config.read_text())
    runtime = args.runtime_dir.resolve()
    if not os.environ.get("SLURM_JOB_ID") or os.environ.get("SLURM_JOB_GPUS") or not runtime.name.startswith("bio-eval-continuation-") or any(runtime.iterdir()):
        raise ValueError("A fresh isolated CPU-only Slurm runtime is required")
    for name, expected in config["files_sha256"].items():
        if sha(name) != expected:
            raise ValueError("Pinned continuation code or receipt changed")
    extract(config["archive"], runtime)
    site = runtime / "python/lib/python3.10/site-packages"
    for wheel in config["wheels"]:
        if sha(wheel["path"]) != wheel["sha256"]:
            raise ValueError("CPU wheel digest mismatch")
        with zipfile.ZipFile(wheel["path"]) as archive:
            for name in archive.namelist():
                relative = PurePosixPath(name)
                if relative.is_absolute() or ".." in relative.parts or any(part.endswith(".data") for part in relative.parts):
                    raise ValueError("Unsupported CPU wheel layout")
            archive.extractall(site)
    extract(config["scorer"]["archive"], runtime / "scorer")
    if sha(runtime / "scorer" / config["scorer"]["launcher_relative"]) != config["scorer"]["launcher_sha256"]:
        raise ValueError("Portable scorer launcher digest mismatch")
    python = runtime / "python/bin/python3.10"
    env = dict(os.environ, PYTHONNOUSERSITE="1", PYTHONDONTWRITEBYTECODE="1", CUDA_VISIBLE_DEVICES="",
        OMP_NUM_THREADS="1", MKL_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1")
    for name in ("PYTHONHOME", "PYTHONPATH", "VIRTUAL_ENV", "OPENAI_API_KEY", "ANTHROPIC_API_KEY", "HF_TOKEN", "HUGGING_FACE_HUB_TOKEN"):
        env.pop(name, None)
    env["PATH"] = str(runtime / "python/bin") + os.pathsep + env.get("PATH", "")
    subprocess.run([str(python), "-c", "import json,yaml; print(json.dumps({'python':'3.10','yaml':yaml.__version__,'cpu_only':True}))"], env=env, check=True)
    coordinator = config["coordinator_script"]
    os.execve(str(python), [str(python), "-u", coordinator, "--config", str(args.config), "--runtime-dir", str(runtime)], env)


if __name__ == "__main__":
    main()
