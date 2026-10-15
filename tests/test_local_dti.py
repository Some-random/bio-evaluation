"""Synthetic-only likelihood, metric, graph and frozen-input tests."""
import copy
import contextlib
import io
import importlib.util
import json
import math
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import local_dti_common as common
import local_dti_identity as identity
import local_dti_run as runner
import local_dti_score as scorer


def response(sampled="No", logyes=math.log(.08), logno=math.log(.02)):
    token = common.LABELS[sampled]
    return {"model": common.MODEL, "choices": [{"message": {"role": "assistant", "content": sampled, "reasoning": None},
        "token_ids": [token], "finish_reason": "length", "logprobs": {"content": [{"token": "token_id:" + str(token),
            "logprob": logyes if sampled == "Yes" else logno,
            "top_logprobs": [{"token": "token_id:9175", "logprob": logyes}, {"token": "token_id:2665", "logprob": logno}]}]}}],
        "prompt_token_ids":common.CLOSED_THINKING_SUFFIX,
        "usage": {"prompt_tokens":len(common.CLOSED_THINKING_SUFFIX),"completion_tokens": 1, "completion_tokens_details": {"reasoning_tokens": 0}}}


class DTITests(unittest.TestCase):
    def test_score_uses_both_loglikelihoods_not_sampled_label(self):
        value = common.extract_score(response(sampled="No"))
        self.assertAlmostEqual(value["positive_score"], .8)
        self.assertAlmostEqual(value["raw_pair_probability_mass"], .1)
        self.assertEqual(value["sampled_label"], "No")
        low = common.conditional_probability(-1000., -1001.)
        self.assertAlmostEqual(low["positive_score"], 1 / (1 + math.exp(-1)))

    def test_missing_candidate_or_unbounded_output_rejected(self):
        missing = response();missing["choices"][0]["logprobs"]["content"][0]["top_logprobs"].pop()
        with self.assertRaises(ValueError):common.extract_score(missing)
        thought = response();thought["choices"][0]["message"]["reasoning"] = "extra"
        with self.assertRaises(ValueError):common.extract_score(thought)
        wrong = response();wrong["choices"][0]["token_ids"] = [17]
        with self.assertRaises(ValueError):common.extract_score(wrong)
        channel = response();channel["prompt_token_ids"] = [1]*7
        with self.assertRaisesRegex(ValueError,"channel audit"):common.extract_score(channel)
        for yes,no in [(float("nan"),-1.),(.5,-1.),(0.,0.)]:
            with self.assertRaises(ValueError):common.conditional_probability(yes,no)

    def test_exact_output_adapter_prevents_budget_variants_or_label_fields(self):
        settings = {"approved_task_ids": ["P43"], "model": common.MODEL, "model_revision": common.REVISION,
                    "variant": common.VARIANT, "generation": copy.deepcopy(common.GENERATION)}
        case = {"task": "P43", "case_id": "synthetic:0", "variant": common.VARIANT, "split": "synthetic",
                "messages": [{"role": "user", "content": "Artificial input only"}]}
        self.assertEqual(common.payload_for(case, settings)["max_tokens"], 1)
        leaked = {**case, "target": 1}
        with self.assertRaises(ValueError):common.payload_for(leaked, settings)
        settings["generation"]["chat_template_kwargs"]["enable_thinking"] = True
        with self.assertRaises(ValueError):common.payload_for(case, settings)

    def test_auroc_ap_ties_and_constant_valid_scores(self):
        result = scorer.binary_metrics([0,1,0,1], [.5,.5,.1,.9])
        self.assertAlmostEqual(result["auroc"], .875)
        self.assertAlmostEqual(result["auprc"], 5/6)
        flat = scorer.binary_metrics([0,1], [.5,.5])
        self.assertEqual(flat["auroc"], .5);self.assertEqual(flat["auprc"], .5)
        self.assertIsNone(scorer.binary_metrics([0,0], [.2,.8])["auroc"])
        with self.assertRaises(ValueError):scorer.binary_metrics([0,1], [.5,None])

    def test_graph_identity_preserves_components_and_stereochemistry(self):
        self.assertEqual(identity.canonical("CCO"), identity.canonical("OCC"))
        self.assertNotEqual(identity.canonical("[Na+].[Cl-]"), identity.canonical("[Cl-]"))
        self.assertNotEqual(identity.canonical("N[C@H](C)O"), identity.canonical("N[C@@H](C)O"))

    def test_runner_refuses_unapproved_and_never_reads_reference_bytes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp);(root/"configs").mkdir()
            config = {"execution_authorized": False}
            p = root/"config.json";p.write_text(json.dumps(config))
            (root/"configs/local_model.json").write_text(json.dumps({"benchmark_inference_authorized": True,
                "approved_task_ids": ["P43"], "model": common.MODEL, "revision": common.REVISION}))
            with mock.patch.object(runner,"ROOT",root):
                with self.assertRaisesRegex(ValueError,"authorization"):runner.read_config(p)
            case = {"task":"P43","case_id":"human:fixture","variant":common.VARIANT,"split":"fixture",
                    "messages":[{"role":"user","content":"Synthetic only"}]}
            (root/"inputs.jsonl").write_text(json.dumps(case)+"\n")
            (root/"review.json").write_text(json.dumps({"reviewed":True,"dataset":"human","approved_case_ids":["human:fixture"],"held_cases":[]}))
            (root/"server.json").write_text("{}")
            config = {"execution_authorized":True,"concurrency":1,"dataset":"human","input_file":"inputs.jsonl",
                "review_file":"review.json","server_state_file":"server.json","scorer_reference_file":"FORBIDDEN_REFS",
                "frozen_files_sha256":{name:"hash" for name in ["FORBIDDEN_REFS","inputs.jsonl","review.json","scripts/local_dti_common.py","scripts/local_dti_run.py","scripts/local_dti_score.py"]},"approved_task_ids":["P43"],"model":common.MODEL,
                "model_revision":common.REVISION,"generation":common.GENERATION,"variant":common.VARIANT}
            p.write_text(json.dumps(config))
            def safe_hash(path):
                if path.name == "FORBIDDEN_REFS":raise AssertionError("gold file read")
                return "hash"
            with mock.patch.object(runner,"ROOT",root),mock.patch.object(runner,"validate_server"),mock.patch.object(runner,"file_digest",side_effect=safe_hash):
                settings,cases,server=runner.read_config(p)
            self.assertEqual(len(cases),1)

    def test_offline_missing_score_and_raw_output_lock(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            cases=[{"task":"P43","case_id":"human:"+str(i),"variant":common.VARIANT,"split":"synthetic", "messages":[{"role":"user","content":"Artificial"+str(i)}]} for i in range(4)]
            (root/"inputs.jsonl").write_text("".join(json.dumps(r)+"\n" for r in cases))
            review={"reviewed":True,"dataset":"human","approved_case_ids":[r["case_id"] for r in cases],"held_cases":[]}
            (root/"review.json").write_text(json.dumps(review))
            refs=[{"task":"P43","case_id":r["case_id"],"dataset":"human","target_binary":i%2} for i,r in enumerate(cases)]
            (root/"refs.jsonl").write_text("".join(json.dumps(r)+"\n" for r in refs))
            settings={"run_id":"synthetic","dataset":"human","approved_task_ids":["P43"],"model":common.MODEL,"model_revision":common.REVISION,"variant":common.VARIANT,
                "generation":common.GENERATION,"input_file":"inputs.jsonl","review_file":"review.json","scorer_reference_file":"refs.jsonl",
                "scorer_reference_sha256":common.file_digest(root/"refs.jsonl"),"frozen_files_sha256":{"inputs.jsonl":common.file_digest(root/"inputs.jsonl")}}
            folder=root/"run";(folder/"requests").mkdir(parents=True);(folder/"responses").mkdir()
            (folder/"run_manifest.json").write_text(json.dumps({"configuration":settings,"case_contract_sha256":common.digest(cases)}))
            for i,case in enumerate(cases[:2]):
                payload=common.payload_for(case,settings);h=common.digest(payload);ident=common.digest(["P43",common.VARIANT,case["case_id"]])
                raw=response(sampled="Yes" if i else "No",logyes=math.log(.08 if i else .02),logno=math.log(.02 if i else .08))
                (folder/"requests"/(ident+".json")).write_text(json.dumps({"payload":payload,"request_sha256":h}))
                rec={**case,"model":common.MODEL,"model_revision":common.REVISION,"request_sha256":h,"status":"completed","score":common.extract_score(raw),"response":raw,"text":raw["choices"][0]["message"]["content"],"finish_reason":"length"}
                (folder/"responses"/(ident+".json")).write_text(json.dumps(rec))
            with mock.patch.object(scorer,"ROOT",root),contextlib.redirect_stdout(io.StringIO()):
                result=scorer.score(folder)
            self.assertIsNone(result["metrics"]["auroc"])
            self.assertEqual(result["metrics"]["auroc_completed_only"],1.)
            self.assertEqual(result["missing_or_failed_outputs"],2)
            p=next((folder/"responses").glob("*.json"));rec=json.loads(p.read_text());rec["score"]["positive_score"]=.5;p.write_text(json.dumps(rec))
            with mock.patch.object(scorer,"ROOT",root),contextlib.redirect_stdout(io.StringIO()):
                with self.assertRaisesRegex(ValueError,"output lock"):scorer.score(folder)


if __name__ == "__main__":unittest.main()
