# OpenAI policy warning and evaluation status

Checked 14 October 2026, 12:17 PST (fixed UTC−8). The user pasted an email
warning about Prohibited Biological Use and possible additional enforcement
after seven calendar days without remediation. The authenticity, receipt time,
exact triggering requests, and current account-wide enforcement state cannot
be established from the pasted text alone.

## Evidence from this workspace

The P18 ProteinGym-LLM run sent native sequence-and-assay ranking requests.
Local records contain **43 HTTP 400 responses with code `bio_policy`**. Several
flagged assays request ranking for viral replication involving HIV, influenza
and Zika. The research benchmark context does not by itself establish provider
permission for every requested output. These blocks are consistent with the
email, but OpenAI must confirm whether these calls caused the notification.

There are 418 saved P18 case records: 43 provider policy errors, 373 transport
errors and two token-count failures. No completed P18 prediction was received
or saved. Five B01/LitQA2 responses completed in the separate LAB-Bench run;
they do not constitute a full category or suite evaluation. Transport failures
are distinct from policy blocks and cannot all be attributed to enforcement
using the available evidence.

Outputs, exact requests, timestamps, input hashes and API usage records remain
on disk. The warning has not deleted local data. Account enforcement could
withhold or reject new API outputs; a ChatGPT message-display issue would need
its exact notice to diagnose separately.

## Changes made

No active evaluation API workers remained at inspection. Future inference is
disabled in `configs/execution_authorization.json`, with an explicit policy
warning hold. The runner now stops queued submissions on a `bio_policy` or
identifier-blocked response. Do not retry flagged requests, disguise the
organism/objective, or change keys, user identifiers or providers to get the
flagged content through. Offline source inspection, scoring and incident
analysis can continue without further model calls. GitHub syncing remains
cancelled and its daily cron job remains disabled.

I should have stopped the batch and reviewed the scope when the first biological
policy blocks appeared. Continuing the broader batch was a mistake. No inference
will resume solely because the benchmark is public or because requests can be
submitted through a different route.

## Provider review

Use the appeal route in the verified notification, or OpenAI's official support
process, to request review and clarification of the permitted evaluation scope.
The local audit contains the relevant UTC/PST dates, requested model, error codes,
case identifiers and request hashes. Account/org identifiers should be supplied
through the support channel; do not put credentials into an appeal or chat.
The research purpose should be explained accurately, without declaring all flags
false positives or denying the pathogen-fitness content actually submitted.

Form-ready wording for the user to review and submit:

### Why the warning or deactivation should be reversed

> I am a PhD student at Stanford University advised by Professor Yejin Choi.
> I am conducting a computational study of language-model performance on published
> biological benchmarks, including ProteinGym-LLM and LAB-Bench. My goal is to
> evaluate biological prediction, question answering and explanation quality,
> and compare results with published baselines using the original evaluation
> protocols. This evaluation uses released benchmark data and does not include
> wet-lab experiments.
>
> Please review and lift the Prohibited Biological Use warning in light of
> this academic context and the corrective action taken.
> I have suspended all API evaluation calls, preserved the logs and added a stop
> on policy rejections. I would like to keep using OpenAI for the permitted parts
> of this research, with explicit guidance about the scope and safeguards required.

### Additional supporting context

> The model used was gpt-6-luna. Our audit found 43 `bio_policy` rejections in
> the ProteinGym-LLM run. These requests ranked existing protein variants by
> assay fitness; some assays measured viral replication involving HIV, influenza
> and Zika. These requests may explain the warning, although I would appreciate
> your confirmation. I understand that inclusion in a published benchmark does
> not automatically make every requested output permissible.
>
> All API evaluation calls remain paused. The runner now stops queued submissions
> following a policy rejection, and the request records and timestamps have been
> preserved for review. I can provide the benchmark task list, timestamps and
> request hashes through your support channel.
>
> To continue this research appropriately, I need clarification on four points:
>
> 1. Would adding a persistent `safety_identifier` for myself and restricting
>    execution to a reviewed, permitted task scope be sufficient to continue
>    through the standard API? What additional controls or approval are required?
>
> 2. Which benchmark task categories or requested outputs must be excluded?
>    Please distinguish restricted items from other biological prediction and
>    question-answering tasks that may remain permissible.
>
> 3. If Trusted Access is necessary, what verification route is available to a
>    university PhD student? I may not be able to make institution-wide enterprise
>    attestations or sign agreements on Stanford's behalf. Could a Stanford email,
>    project description and, if needed, adviser confirmation support individual
>    or lab-level review? If an institutional sponsor must apply, who should do so?
>
> 4. Does the current suspension address the warning, and what else is required
>    within the stated seven-day period? If this appeal is approved, please confirm
>    which research scope may resume and any continuing limits.

Include the OpenAI User ID and Organization ID if the form has not already
collected them. The user's academic affiliation and adviser were supplied by
the user; no authority to sign for Stanford or adviser sponsorship is asserted.

No appeal has been sent by the assistant.

The user subsequently reported submitting the appeal through the provider's
form. No provider response or confirmation of permitted scope has been reported.
The inference hold remains active; submission alone does not clear that hold.

## Interpretation of the email

A warning is not by itself proof of account deactivation. The email asks for
remediation within seven calendar days and warns of possible loss of access.
A `safety_identifier` is a stable pseudonymous identifier of the actual end user
so enforcement can be attributed appropriately; adding it does not authorize
restricted requests or resolve an existing warning. The password/2FA/key-rotation
advice is conditional on suspected unauthorized access. This workspace's known
traffic provides a plausible explanation, without excluding other account use.

References: [OpenAI safety classifiers](https://developers.openai.com/api/docs/guides/safety-checks),
[Usage policies](https://openai.com/policies/usage-policies/),
[Account warning guidance](https://help.openai.com/en/articles/10562178-why-did-i-receive-a-warning-about-my-account).

## Cost interpretation

The application ledger accounts for unknown transport outcomes at their reserved
maximum cost. Its near-$50 total is a conservative guard, not an observed bill.
Only five saved benchmark completions include confirmed usage, totaling about
$0.00188 at the recorded rates; compatibility probes are separate. The provider
usage dashboard is needed to establish the actual charge for unreceived or
interrupted requests. Do not report the ledger ceiling as money actually spent.
