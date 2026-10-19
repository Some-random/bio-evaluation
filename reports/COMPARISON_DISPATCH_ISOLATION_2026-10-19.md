# OpenAI comparison dispatch isolation

Checked 2026-10-19T14:15:27.576606-07:00 (America/Los_Angeles). This is a zero-network validation record, not a benchmark result.

The [dispatcher](../scripts/run_isolated_openai_comparison.py) was frozen at SHA-256 `c8184228dcdf78bd9e5c837631882c004f211a195af70535431a1230d3ad1ae8`. All **19 dispatcher tests** and **20 scoring tests** passed, including the persistent dispatcher-to-scorer integration check. The integration accepted normally completed, truncated, empty-final, HTTP-error, transport-error and refused outputs while treating only the usable completion as a delivered answer.

## Actual filesystem isolation

A fresh subprocess ran the frozen dispatcher under **Linux Landlock ABI 4**. Its attempt to read a synthetic probe inside this evaluation repository, outside the minimal bundle/output, raised `PermissionError`. The worker then processed three artificial questions using its fixed local synthetic transport. No remote transport, private identity or API credentials were used; new inference calls were **zero**.

The kernel receipt is preserved in the [structured report](COMPARISON_DISPATCH_ISOLATION_2026-10-19.json). Its original file SHA-256 was `215e2c73eacf2b301307228f53c82ebbd337cab148d62821283ee53c846f6533`. The synthetic output lock SHA-256 was `569cde203b11bf25b2da5337282383e0c14d8711fc0ea11653b49236c8badec6`. Temporary synthetic files were removed after these records were captured.

The worker can read its minimal frozen bundle, its own output directory, and explicitly allowed interpreter/system TLS/DNS resources. It cannot read the repository's scorer references, Qwen outputs, reports, home credentials or unrelated temporary files. The process receives no inherited API-key environment variable. A private runtime pipe is closed before the filesystem restriction takes effect.

## Request and scoring separation

Preparation reads only the dedicated `payload_without_private_safety_identifier` field for model content. The exact ordered roster pins every case's canonical payload hash. Only one fresh user text message is accepted. Assistant/system/developer history, tools, previous responses, conversation references, added payload fields, alternate budgets and unsupported sampling parameters are rejected. The only added model-facing runtime field is the existing stable private `safety_identifier`.

Immediately before transport, the dispatcher revalidates the payload and fsyncs its actual serialized body hash. The public request artifact contains the frozen body without the private identifier value, plus the actual-wire hash. Raw response bytes, HTTP status, request/response IDs, usage, final text and terminal status are retained. The dispatcher extracts assistant `output_text` only; reasoning summaries never become answers.

The tested invariance rule permutes separate gold labels and changes Qwen predictions/correctness metadata after choices are frozen. Outgoing model payload bytes and hashes stay unchanged. Changing the actual question/choice order instead fails its frozen payload pin.

Concurrency defaults to four independent requests, with a maximum of eight. There are no automatic retries or selective resumption. A policy/access failure, including parsed `model_not_found` or access-denied errors on HTTP404, stops future submissions while preserving in-flight returns and records for cases not dispatched. A complete immutable prediction lock is required before the scorer opens reference artifacts.

## Actual authorization receipts

Both `run` and `run-development` require actual `--reviewed-input-receipt` and `--risk-review-receipt` files. Their bytes are hashed against scoped authorization **before private identity or key access**. Each must report a passed scope review with prior flagged requests excluded and bind the exact model, protocol, roster/protocol hashes, task IDs and case count. Missing files, bogus hashes and mismatched scope fail closed.

For benchmark execution, `--development-evidence` must point to the actual sealed completed development lock. Before credentials are accessed, the dispatcher hashes the lock and each actual request, raw response and final-text artifact. It checks the reviewed model, development protocol/request/roster hashes, frozen code, complete case count, task coverage and actual HTTP200 nonempty completed outputs without truncations or refusals. The task-specific review still determines whether the delivered answer satisfies its declared format; these checks do not score biological labels.

The new reviewed comparison uses its own explicit narrow authorization; the historical warning/appeal facts and global disabled authorization are unchanged. Development uses a separate delivery-only protocol. Benchmark dispatch additionally requires a reviewed successful development gate bound to the frozen code/protocol, the same model/task coverage and the 4,096-token medium-reasoning condition. Every run requires a reviewed estimate within the initial $50 spending guard and cannot automatically start another model or stage.

## What these records do not establish

SHA-256 pins verify agreement with trusted reviewed artifacts. They are **not digital signatures, independent provider approval or proof against an operator who can rewrite both the authorization and review artifacts**. The outbound hash records transport handoff, not a provider-signed receipt. Landlock restricts filesystem access; the fixed API endpoint and no-tools request contract restrict the implemented network path.

These checks establish pipeline separation and artifact integrity under the stated execution code. They do not establish biological accuracy, representative delivery reliability, absence of public-benchmark training exposure, or equal internal reasoning compute between models. This validation itself made no live calls; any later development or benchmark execution has separate runtime evidence.
