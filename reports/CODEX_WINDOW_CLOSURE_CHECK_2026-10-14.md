# App-window closure: available evidence

Checked 2026-10-14T20:11:47.214312-08:00 (PST, fixed UTC-8).
The user reports that the Codex/ChatGPT app window itself closed. The exact app,
client OS/version and closure timestamp have been requested and are unconfirmed.

## Confirmed on the remote Linux host

- The existing Codex server processes are alive. The active executable is the
  installed app-server daemon release 0.162.1.
- The local-model setup worker (PID 328177) and existing download parent
  (PID 323516) are alive. The setup worker is independently detached and waiting
  for that download; no duplicate worker was launched for this investigation.
- Sixteen of eighteen Qwen3.8-27B weight shards are complete, totaling
  50,062,050,088 bytes. Full-model serving has not started. A live process alone
  does not establish current download throughput.
- The Codex process cgroup reports zero memory-limit, OOM and OOM-kill events;
  its memory maximum is unlimited. Its process-limit event counter is zero.
- The recent kernel journal query found no matching OOM, killed-process,
  segmentation-fault, watchdog or Codex entries. The host remains on the same
  boot, with about 22.9 days of uptime.
- Remote app-server logs contain MCP transport HTTP 502 errors, most recently
  at 2026-10-14 15:59 PST. These do not establish an app-window crash cause.
- A daemon updater exists and checks/packages updates periodically. Its recorded
  forced shutdown events were on October 9, most recently 14:11 PST; the reviewed
  October 14 update events do not record a forced daemon restart. This is not
  evidence that a current desktop window was closed by a watchdog.

## Limits and next evidence

These are remote Linux observations. They do not inspect the user's desktop
app crash reports, OS termination records, or client-side security software.
No available evidence establishes an account-policy action, intentional blocking,
or a watchdog as the cause of the reported window closure. Such a cause is not
ruled out by remote process survival.

For a Mac client, inspect the app logs for the closure timestamp. Official
OpenAI documentation lists `~/Library/Logs/com.openai.codex/YYYY/MM/DD`.
A corresponding OS crash report's exception and termination-reason fields would
help distinguish an application fault from an OS/watchdog termination. Retain
those records before making changes. No security, watchdog, updater, SSH or app
configuration was changed during this investigation.

Source: [official OpenAI troubleshooting documentation](https://learn.chatgpt.com/docs/reference/troubleshooting).
