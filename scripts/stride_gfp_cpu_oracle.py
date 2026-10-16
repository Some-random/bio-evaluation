"""CPU-only pinned native SaProt GFP oracle with exact trained-state audit."""
from __future__ import annotations

import argparse
import contextlib
import hashlib
import importlib.metadata
import importlib.util
import json
import os
from pathlib import Path
import platform
import sys

ROOT = Path(__file__).resolve().parents[1]
NATIVE_SOURCE = "sources/stride__scripts__eval__score_fluorescence.py"
NATIVE_SHA256 = "ae06c6f200d81ad6b7f764921fba17379076d2e6413cae781cc3bbffd3ed9ad2"
RUNTIME_FILE = "reports/stride_gfp_oracle_runtime.json"
AUDIT_FILE = "reports/stride_gfp_oracle_state_restoration.json"
BASE_DIRECTORY = "models/proxy_generation_native/saprot_base"
ADAPTER_DIRECTORY = "models/proxy_generation_native/saprot_fluorescence_adapter"
EXPECTED_CORE = {"torch": "2.6.0+cpu", "transformers": "4.44.2", "peft": "0.12.0", "accelerate": "0.34.2",
    "numpy": "1.26.4", "huggingface-hub": "0.25.2", "tokenizers": "0.19.1", "safetensors": "0.4.5"}
_CONFIGURED = False


def file_sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b""): h.update(block)
    return h.hexdigest()


def digest(value): return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def save(path, value):
    path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n"); temporary.replace(path)


def package_inventory():
    return sorted([{"name": d.metadata["Name"], "version": d.version} for d in importlib.metadata.distributions()], key=lambda d: d["name"].lower())


def configure_cpu():
    global _CONFIGURED
    if Path(sys.prefix).resolve() != (ROOT / ".venv-oracles").resolve():
        raise ValueError("Use only the isolated .venv-oracles interpreter; active environments are not oracle runtimes")
    for name, version in EXPECTED_CORE.items():
        if importlib.metadata.version(name) != version: raise ValueError("Pinned CPU dependency changed: " + name)
    # Local to this oracle process; no global environment or serving changes.
    os.environ["HF_HUB_OFFLINE"] = "1"; os.environ["TRANSFORMERS_OFFLINE"] = "1"
    os.environ["CUDA_VISIBLE_DEVICES"] = ""
    import torch
    if torch.__version__ != EXPECTED_CORE["torch"] or torch.version.cuda is not None:
        raise ValueError("Oracle requires the official CPU-only torch build")
    if not _CONFIGURED:
        torch.set_num_threads(8); torch.set_num_interop_threads(1); torch.manual_seed(42)
        _CONFIGURED = True
    return torch


def critical_package_files():
    import torch, transformers, peft, numpy, tokenizers
    files = [torch.__file__, transformers.__file__, peft.__file__, numpy.__file__, tokenizers.__file__]
    packages = {name: Path(module.__file__).parent for name, module in [("torch", torch), ("transformers", transformers), ("peft", peft)]}
    names = {"torch": ["serialization.py"], "transformers": ["modeling_utils.py", "models/esm/modeling_esm.py", "models/esm/tokenization_esm.py"],
        "peft": ["peft_model.py", "utils/save_and_load.py", "utils/other.py", "tuners/lora/layer.py"]}
    files += [str(packages[name] / relative) for name, relatives in names.items() for relative in relatives]
    return {str(Path(path).relative_to(ROOT)): file_sha(path) for path in files}


def freeze_runtime():
    torch = configure_cpu()
    report = {"environment": ".venv-oracles", "python_executable": str(Path(sys.executable).relative_to(ROOT)),
        "python_version": platform.python_version(), "platform": platform.platform(), "packages": package_inventory(),
        "core_versions": EXPECTED_CORE, "critical_installed_files_sha256": critical_package_files(),
        "torch_cuda_build": torch.version.cuda, "device": "cpu", "dtype": "float32", "torch_num_threads": 8, "torch_num_interop_threads": 1,
        "native_scorer_source": NATIVE_SOURCE, "native_scorer_sha256": NATIVE_SHA256,
        "weights_only_loading": True, "network_during_model_load_or_scoring": False,
        "benchmark_forwards_performed": 0, "active_environments_modified": False,
        "numeric_qualification": "CPU FP32 native architecture/preprocessing; different hardware and pinned library versions from unpinned author historical runtime. No byte-identical GPU score claim."}
    path = ROOT / RUNTIME_FILE
    if path.exists() and json.loads(path.read_text()) != report: raise ValueError("Runtime already frozen; refuse replacement")
    save(path, report)
    freeze = "\n".join(row["name"] + "==" + row["version"] for row in report["packages"]) + "\n"
    (ROOT / "reports/stride_gfp_oracle_packages.lock.txt").write_text(freeze)
    return report


def verify_runtime(expected_sha=None):
    configure_cpu(); path = ROOT / RUNTIME_FILE
    if expected_sha and file_sha(path) != expected_sha: raise ValueError("Frozen oracle runtime record changed")
    record = json.loads(path.read_text())
    if package_inventory() != record["packages"] or critical_package_files() != record["critical_installed_files_sha256"]:
        raise ValueError("Actual isolated CPU package inventory/code changed")
    return record


def verify_assets(assets):
    found = {}
    for row in assets:
        path = ROOT / row["target"]
        if not path.resolve().is_relative_to((ROOT / "models/proxy_generation_native").resolve()): raise ValueError("Oracle asset escaped pinned local directory")
        if path.stat().st_size != row["bytes"] or file_sha(path) != row["sha256"]: raise ValueError("Pinned local oracle asset changed: " + row["target"])
        found[row["target"]] = row["sha256"]
    required = {BASE_DIRECTORY + "/" + name for name in ["config.json", "pytorch_model.bin", "vocab.txt", "tokenizer_config.json", "special_tokens_map.json"]}
    required |= {ADAPTER_DIRECTORY + "/" + name for name in ["adapter_config.json", "adapter_model.bin", "metadata.json"]}
    if set(found) != required or file_sha(ROOT / NATIVE_SOURCE) != NATIVE_SHA256: raise ValueError("Complete pinned oracle/source asset contract required")
    return found


@contextlib.contextmanager
def weights_only_cpu(torch):
    original = torch.load
    def restricted(*args, **kwargs):
        if kwargs.get("weights_only") is False: raise ValueError("Unrestricted pickle load forbidden")
        kwargs["weights_only"] = True; kwargs["map_location"] = "cpu"
        return original(*args, **kwargs)
    torch.load = restricted
    try: yield
    finally: torch.load = original


def compare_trained_tensors(saved, restored, torch):
    if not isinstance(saved, dict) or not saved or set(saved) != set(restored): raise ValueError("Trained adapter/classifier tensor keys missing or extra")
    classifier = [key for key in saved if ".classifier." in key]
    if len(classifier) != 4: raise ValueError("All four trained regression classifier tensors are required")
    result = {}
    for name in sorted(saved):
        before, after = saved[name], restored[name]
        if (not isinstance(before, torch.Tensor) or not isinstance(after, torch.Tensor)
                or before.shape != after.shape or after.dtype != torch.float32 or after.device.type != "cpu"
                or not torch.isfinite(before).all() or not torch.equal(before.to(dtype=torch.float32, device="cpu"), after)):
            raise ValueError("Trained tensor not exactly restored: " + name)
        expected = before.detach().to(dtype=torch.float32, device="cpu").contiguous()
        result[name] = {"shape": list(before.shape), "checkpoint_dtype": str(before.dtype), "runtime_dtype": str(after.dtype),
            "checkpoint_sha256": hashlib.sha256(before.detach().cpu().contiguous().numpy().tobytes()).hexdigest(),
            "expected_fp32_sha256": hashlib.sha256(expected.numpy().tobytes()).hexdigest(),
            "actual_fp32_sha256": hashlib.sha256(after.detach().cpu().contiguous().numpy().tobytes()).hexdigest(),
            "exact_equal_after_fp32_conversion": True}
    return result


def audit_active_routes(model, saved):
    """Establish trained active modules without running a model forward."""
    head = model.base_model.model.classifier
    if (getattr(head, "active_adapter", None) != "default" or getattr(head, "disable_adapters", True)
            or "default" not in getattr(head, "modules_to_save", {})):
        raise ValueError("Trained classifier modules_to_save.default is not the active forward head")
    if list(model.active_adapters) != ["default"]:
        raise ValueError("Unexpected globally active adapter")
    routes = {}
    mapped = set()
    for name, module in model.named_modules():
        if not hasattr(module, "lora_A"): continue
        if (getattr(module, "disable_adapters", True) or getattr(module, "merged", True)
                or list(module.active_adapters) != ["default"]
                or "default" not in module.lora_A or "default" not in module.lora_B):
            raise ValueError("A trained LoRA forward route is disabled, merged or selects a different adapter: " + name)
        keys = [name + ".lora_A.weight", name + ".lora_B.weight"]
        if not set(keys) <= set(saved): raise ValueError("Active LoRA module lacks matching pinned trained tensors")
        mapped.update(keys)
        routes[name] = {"active_adapters": ["default"], "disabled": False, "merged": False, "checkpoint_keys": keys}
    lora_keys = {name for name in saved if ".lora_A." in name or ".lora_B." in name}
    if not routes or mapped != lora_keys or len(routes) != 198:
        raise ValueError("Every one of396 trained LoRA tensors must map to198 active forward modules")
    if model.config.position_embedding_type != "rotary":
        raise ValueError("Unexpected positional embedding forward path")
    return {"classifier_forward_module": "base_model.model.classifier.modules_to_save.default",
        "inactive_classifier_original_module_used": False, "active_adapter": "default", "lora_module_count": len(routes),
        "all_trained_lora_keys_mapped_to_enabled_unmerged_modules": True, "lora_routes": routes,
        "base_load_missing_fields_qualification": "The base architecture initializes its classifier before the trained adapter restores the active modules_to_save.default classifier. The inactive original_module is not the selected head. Missing base contact-head tensors are unused by EsmForSequenceClassification; missing absolute position embeddings are unused with the verified rotary configuration."}


def load_oracle(assets, runtime_sha=None, expected_audit_sha=None):
    runtime = verify_runtime(runtime_sha); asset_hashes = verify_assets(assets); torch = configure_cpu()
    spec = importlib.util.spec_from_file_location("p42_pinned_native_fluorescence", ROOT / NATIVE_SOURCE)
    native = importlib.util.module_from_spec(spec); spec.loader.exec_module(native)
    # Execute the pinned author's native loader with existing local paths.
    # OFFLINE flags prohibit network fallback; no model copies are written.
    with weights_only_cpu(torch):
        saved = torch.load(ROOT / ADAPTER_DIRECTORY / "adapter_model.bin", weights_only=True, map_location="cpu")
        tokenizer, model = native.load_model(str(ROOT / BASE_DIRECTORY), str(ROOT / ADAPTER_DIRECTORY),
            str(ROOT / ".local/stride_gfp_oracle_cache"), torch.device("cpu"))
    model.to(device="cpu", dtype=torch.float32); model.eval(); model.requires_grad_(False)
    from peft import get_peft_model_state_dict
    restored = get_peft_model_state_dict(model, adapter_name="default")
    tensors = compare_trained_tensors(saved, restored, torch)
    if len(tensors) != 400: raise ValueError("Unexpected trained adapter tensor count")
    routes = audit_active_routes(model, saved)
    if model.config.num_labels != 1 or model.config.problem_type != "regression" or model.training:
        raise ValueError("Oracle regression/eval configuration changed")
    if any(parameter.device.type != "cpu" or parameter.dtype != torch.float32 for parameter in model.parameters()):
        raise ValueError("All oracle parameters must remain FP32 CPU")
    audit = {"assets_sha256": asset_hashes, "runtime_record_sha256": file_sha(ROOT / RUNTIME_FILE),
        "native_scorer_sha256": NATIVE_SHA256, "weights_only_cpu_load": True, "trained_state_tensor_count": len(tensors),
        "trained_classifier_tensor_count": 4, "all_trained_tensors_exactly_restored": True,
        "active_classifier": "base_model.model.classifier.modules_to_save.default", "active_adapter": "default",
        "active_forward_routes": routes,
        "classification_head_randomness_used_for_scoring": False, "all_parameters_fp32_cpu": True,
        "evaluation_mode": True, "gradients_disabled": True, "benchmark_forward_count": 0, "tensors": tensors,
        "qualification": runtime["numeric_qualification"]}
    if expected_audit_sha:
        path = ROOT / AUDIT_FILE
        if file_sha(path) != expected_audit_sha or json.loads(path.read_text()) != audit: raise ValueError("Actual trained-state restoration differs from frozen audit")
    return NativeOracle(tokenizer, model, native, torch), audit


class NativeOracle:
    def __init__(self, tokenizer, model, native, torch): self.tokenizer, self.model, self.native, self.torch = tokenizer, model, native, torch
    def predict(self, sequences):
        if not sequences or any(not isinstance(sequence, str) or not sequence or "#" in sequence for sequence in sequences): raise ValueError("Require complete raw eligible amino-acid sequences")
        # Original function supplies AA# masking, EsmTokenizer padding/truncation
        # max1024, eval-mode logits, no_grad and float32 CPU scalar extraction.
        with self.torch.no_grad(): return self.native.predict_batch(sequences, self.tokenizer, self.model, self.torch.device("cpu"))


def main():
    parser = argparse.ArgumentParser(description=__doc__); parser.add_argument("--freeze-runtime", action="store_true")
    parser.add_argument("--audit-restoration", action="store_true"); parser.add_argument("--proposal", default="configs/stride_gfp_qualified_p42.proposed.json")
    args = parser.parse_args()
    if args.freeze_runtime: freeze_runtime(); print(json.dumps({"runtime_file": RUNTIME_FILE, "sha256": file_sha(ROOT / RUNTIME_FILE), "benchmark_forwards": 0}))
    elif args.audit_restoration:
        proposal = json.loads((ROOT / args.proposal).read_text()); _, audit = load_oracle(proposal["oracle"]["assets"])
        path = ROOT / AUDIT_FILE
        if path.exists() and json.loads(path.read_text()) != audit: raise ValueError("Restoration audit already frozen")
        save(path, audit); print(json.dumps({"audit_file": AUDIT_FILE, "sha256": file_sha(path), "trained_tensors": 400, "benchmark_forwards": 0}))
    else: parser.error("Choose only runtime freeze or no-forward restoration audit")


if __name__ == "__main__": main()
