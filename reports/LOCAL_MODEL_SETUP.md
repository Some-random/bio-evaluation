# Local Qwen3.8-27B checkpoint and server

**Complete and ready**, verified 14 October 2026 at 9:03 PM PST (fixed UTC-8).

The selected model is `Qwen/Qwen3.8-27B`, revision
`1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0`, original BF16 weights,
Apache 2.0, with the native vision tower retained.

## Complete checkpoint

Directory: `/data/rustfs1/dongweij/bio-evaluation/models/Qwen3.8-27B`.
All 32 files in the pinned source repository are present:

- 18 weight shards, totaling 55,563,006,776 bytes, each matched to its official SHA-256.
- 14 supporting files, including configuration, tokenizer, processors, index,
  chat template, license and README, each matched to its pinned source digest.
- Total source-file size: **55,586,114,863 bytes (55.59 GB)**.

[Complete verification ledger](local_model_complete_verification.json),
[weight verification](local_model_weight_verification.json), and
[supporting-file verification](local_model_repository_verification.json)
contain the file names, sizes and hashes. The repository manifest is saved under
`sources/local_model/1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0/`.

The final shard was completed with resumable aria2 through direct HTTPS to
Qwen's publisher repository on ModelScope's China CDN. Its pinned SHA-256 is
identical to the Hugging Face copy. The unstable SOCKS proxy was excluded only
for that download process. No global network settings or SSH connections changed.

## Running server

The server is ready at `http://127.0.0.1:8026/v1`. It is bound only to loopback.
`GET /health` returned 200, and `/v1/models` advertises `Qwen/Qwen3.8-27B`
with a 262,144-token context limit.

The active configuration uses **one H200, physical GPU 5**, tensor parallelism 1,
65% requested GPU memory utilization, and at most four concurrent sequences.
The observed GPU worker uses GPU 5 only; its post-check memory use was 84,712 MiB.
Vision remains enabled, with no weight quantization, extra drafter, context
extension or solver tools. Native generation defaults are retained; future
scored runs must separately freeze their decoding settings.

Fixed synthetic checks passed: exact `READY` text, arithmetic through the
reasoning interface, and identifying a solid blue image. These establish basic
serving operation, not biological benchmark accuracy or explanation validity.
See [server validation](local_model_server_validation.json),
[synthetic check results](local_model_capability_smoke.json), and the
[live deployment record](local_model_deployment.json).

The isolated runtime is Python 3.12.15, vLLM 0.31.0, PyTorch 2.13.0+cu132,
Transformers 5.17.0, Ninja 1.13.2 and the installed CUDA 13.0 compiler. The
launcher includes its environment's executables on PATH; a real FlashInfer
sampling kernel compiled and passed. Current model, framework, compiler and
CUDA driver caches are directed to the project data disk. OpenAI keys are not
read or needed.

## Operation

From `/data/rustfs1/dongweij/bio-evaluation`:

```bash
cat reports/local_model_deployment.json
```

The current server is already running. Its identity is in
`.local/local_model_server.json`; do not start a duplicate server.
`python3 scripts/local_vllm.py download` validates and reuses the completed local
manifest. `scripts/bootstrap_local_model.py` performs full setup when a server
is absent, reusing prior official weight hashes only if the files are unchanged.
A synthetic-client failure leaves a healthy server available for diagnosis.
Process records are under `.local/`; diagnostic logs are under
`logs/local_model/`. Old failed-transfer/startup logs are retained and do not
indicate that the current checkpoint is incomplete.

The initial startup encountered changing free memory on GPU 4, then an executable
PATH issue, and an unsupported empty `tools` field in the test client. The active
GPU allocation, launcher and client were corrected. The current status is `ready`.
The larger eight-GPU Flash-Next proposal remains archived and was not downloaded.

## Evaluation scope

No Qwen biological benchmark cases have been dispatched. The local task
allowlist remains empty; the OpenAI inference hold and flagged-task restrictions
remain active. Before scientific execution, freeze the permitted scope,
protocols, inputs, inference settings and scorers. Preserve native sequences,
images, structures and representations, sealed labels, and interpretation tables.
Public-benchmark pretraining exposure remains unknown.

Sources: [Qwen model card](https://huggingface.co/Qwen/Qwen3.8-27B),
[publisher ModelScope repository](https://modelscope.cn/models/Qwen/Qwen3.8-27B),
[vLLM recipe](https://recipes.vllm.ai/Qwen/Qwen3.8-27B).
