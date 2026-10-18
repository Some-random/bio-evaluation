"""Bounded HTTP producer queue; GPU scheduling belongs to vLLM.

Only dispatch order changes. Every original case/payload is still supplied by
the frozen native runner, and no case is claimed before a worker selects it.
"""
from __future__ import annotations

from collections import Counter, deque
import concurrent.futures
import threading


class QueueError(RuntimeError):
    pass


def queue_limit(endpoint):
    limit = endpoint.get("queue_limit")
    if (type(limit) is not int or not 1 <= limit <= 512
            or endpoint.get("max_inflight") != limit
            or endpoint.get("scheduler_policy") != "vllm_native_bounded_queue"):
        raise QueueError("A bounded native queue_limit/max_inflight contract is required")
    return limit


class NativeTaskQueue:
    """One shared iterator per run; fair across tasks, then runs within a task."""

    def __init__(self, runs, endpoints):
        self.runs = list(runs)
        self.pending = [iter(state.pending()) for state in self.runs]
        self.heads, self.exhausted = {}, set()
        self.mutex = threading.Lock()
        grouped = {}
        for index, state in enumerate(self.runs):
            grouped.setdefault(state.entry["task_id"], deque()).append(index)
            budget = state.settings["generation"]["max_tokens"]
            if type(budget) is not int or budget != 4096:
                raise QueueError("The unchanged frozen 4096-token generation budget is required")
            count = max(state.prompt_tokens.values(), default=0)
            if not any(endpoint["max_model_len"] >= state.entry["minimum_context_tokens"]
                       and count + budget <= endpoint["max_model_len"] for endpoint in endpoints):
                raise QueueError("A selected run lacks an endpoint covering its complete frozen context")
        self.tasks = deque(grouped)
        self.groups = grouped
        self.selected_by_task, self.selected_by_run = Counter(), Counter()

    def take(self, endpoint, stopped):
        # Transport workers bound outstanding requests. No fractional memory
        # weights, queue tickets or waiting for one long prompt occur here.
        with self.mutex:
            if stopped.is_set():
                return None
            for _ in range(len(self.tasks)):
                task = self.tasks[0]
                self.tasks.rotate(-1)
                group = self.groups[task]
                for _ in range(len(group)):
                    index = group[0]
                    group.rotate(-1)
                    state = self.runs[index]
                    if index in self.exhausted or endpoint["max_model_len"] < state.entry["minimum_context_tokens"]:
                        continue
                    if index not in self.heads:
                        try:
                            self.heads[index] = next(self.pending[index])
                        except StopIteration:
                            self.exhausted.add(index)
                            continue
                    case, name = self.heads[index]
                    budget = state.settings["generation"]["max_tokens"]
                    if state.prompt_tokens[case["case_id"]] + budget > endpoint["max_model_len"]:
                        # A larger declared endpoint can consume this same head;
                        # this endpoint immediately considers another runnable task.
                        continue
                    del self.heads[index]
                    self.selected_by_task[task] += 1
                    self.selected_by_run[state.entry["run_id"]] += 1
                    return state, case, name
            return None

    def snapshot(self):
        with self.mutex:
            return {"scheduler_policy": "vllm_native_bounded_queue",
                    "fairness": "task_round_robin_then_run_round_robin",
                    "selected_by_task": dict(self.selected_by_task),
                    "selected_by_run": dict(self.selected_by_run),
                    "exhausted_runs": len(self.exhausted), "retained_heads": len(self.heads)}


def drive_bounded_queue(queue, endpoints, stopped, dispatch, after_case):
    """Keep each server's bounded native queue supplied; drain calls on pause."""
    limits = {endpoint["endpoint_id"]: queue_limit(endpoint) for endpoint in endpoints}
    active, peaks, errors = Counter(), Counter(), []
    mutex = threading.Lock()

    def worker(endpoint):
        identity = endpoint["endpoint_id"]
        while not stopped.is_set():
            selected = queue.take(endpoint, stopped)
            if selected is None:
                return
            state, case, name = selected
            with mutex:
                active[identity] += 1
                peaks[identity] = max(peaks[identity], active[identity])
            try:
                dispatch(state, case, name, endpoint, stopped)
            except Exception as error:
                # Retain the existing claim/request for independent audit.
                # Every other already-active call still runs to completion.
                stopped.set()
                with mutex:
                    errors.append(type(error).__name__)
            finally:
                with mutex:
                    active[identity] -= 1
                try:
                    after_case(state)
                except Exception as error:
                    stopped.set()
                    with mutex:
                        errors.append(type(error).__name__)

    with concurrent.futures.ThreadPoolExecutor(max_workers=sum(limits.values())) as pool:
        futures = [pool.submit(worker, endpoint) for endpoint in endpoints
                   for _ in range(limits[endpoint["endpoint_id"]])]
        for future in futures:
            future.result()
    return {**queue.snapshot(), "queue_limits": limits,
            "peak_outstanding_requests": dict(peaks), "active_calls_at_return": dict(active),
            "infrastructure_error_types": errors}
