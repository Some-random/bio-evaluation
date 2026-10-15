"""Synthetic-only all-three-test identity, likelihood metric and tamper tests."""
import contextlib
import copy
import io
import json
import math
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
import local_dti_common as common
import local_dti_score as scorer
import local_dti_aggregate as aggregate


def response(probability):
    # Synthetic observations, never biological benchmark data or inference.
    yes,no=math.log(probability*.1),math.log((1-probability)*.1)
    return {"model":common.MODEL,"choices":[{"message":{"role":"assistant","content":"No","reasoning":None},
        "token_ids":[2665],"finish_reason":"length","logprobs":{"content":[{"token":"token_id:2665","logprob":no,
            "top_logprobs":[{"token":"token_id:9175","logprob":yes},{"token":"token_id:2665","logprob":no}]}]}}],
        "prompt_token_ids":common.CLOSED_THINKING_SUFFIX,
        "usage":{"prompt_tokens":len(common.CLOSED_THINKING_SUFFIX),"completion_tokens":1,"completion_tokens_details":{"reasoning_tokens":0}}}


class AggregateTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name);self.configs={};self.folders={}
        for path in ["configs","scripts"]:(self.root/path).mkdir()
        (self.root/aggregate.RUNNER).write_text("synthetic runner fixture\n")
        original=[{"task":"P43","dataset":dataset,"case_id":f"{dataset}:synthetic:{i}","prompt":f"Artificial instruction {dataset} {i}"}
                  for dataset in ["bindingdb","biosnap","human"] for i in range(2)]
        self.original=original
        src=self.root/aggregate.SOURCE_INPUT;src.parent.mkdir(parents=True)
        src.write_text("".join(json.dumps(r)+"\n" for r in original))
        refs=[{"task":"P43","dataset":r["dataset"],"case_id":r["case_id"],"target_binary":i%2} for i,r in enumerate(original)]
        (self.root/"refs.jsonl").write_text("".join(json.dumps(r)+"\n" for r in refs))
        pins={}
        # Dataset results differ deliberately: perfect, reversed and tied.
        probabilities={"human":[.1,.9],"biosnap":[.9,.1],"bindingdb":[.5,.5]}
        for dataset in ["human","biosnap","bindingdb"]:
            cases=[{"task":"P43","case_id":r["case_id"],"variant":common.VARIANT,
                "split":"official_BioT5_export_"+dataset+"_test","messages":[{"role":"user","content":r["prompt"]}]}
                for r in original if r["dataset"]==dataset]
            inp=f"{dataset}.jsonl";review=f"{dataset}.review.json"
            (self.root/inp).write_text("".join(json.dumps(c)+"\n" for c in cases))
            common.write_json(self.root/review,{"reviewed":True,"dataset":dataset,"held_cases":[],"approved_case_ids":[c["case_id"] for c in cases]})
            cfg={"run_id":"synthetic_"+dataset,"dataset":dataset,"approved_task_ids":["P43"],"execution_authorized":True,
                 "model":common.MODEL,"model_revision":common.REVISION,"generation":copy.deepcopy(common.GENERATION),"variant":common.VARIANT,
                 "input_file":inp,"review_file":review,"source_input_sha256":common.file_digest(src),
                 "scorer_reference_file":"refs.jsonl","scorer_reference_sha256":common.file_digest(self.root/"refs.jsonl"),
                 "frozen_files_sha256":{name:common.file_digest(self.root/name) for name in [inp,review,aggregate.RUNNER]},
                 "gpu_ids":[6],"endpoint":"http://127.0.0.1:8027/v1"}
            config_path=self.root/f"configs/local_dti_{dataset}.json";common.write_json(config_path,cfg)
            pins[dataset]=common.file_digest(config_path);self.configs[dataset]=cfg
            folder=self.root/"results/runs"/cfg["run_id"];self.folders[dataset]=folder
            (folder/"requests").mkdir(parents=True);(folder/"responses").mkdir()
            common.write_json(folder/"run_manifest.json",{"configuration":cfg,"configuration_sha256":pins[dataset],
                "case_contract_sha256":common.digest(cases),"planned_cases":2,"runner_sha256":cfg["frozen_files_sha256"][aggregate.RUNNER],
                "solver_tools":[],"answer_keys_available_to_solver":False,"model_selection_on_test":False,
                "server":{"model":common.MODEL,"revision":common.REVISION,"gpu_ids":[6],"port":8027,"pid":123,"proc_start_ticks":"456"}})
            for i,case in enumerate(cases):
                payload=common.payload_for(case,cfg);ident=common.digest(["P43",common.VARIANT,case["case_id"]])+".json"
                common.write_json(folder/"requests"/ident,{**{k:case[k] for k in ["task","case_id","variant","split"]},
                    "payload":payload,"request_sha256":common.digest(payload),"dataset":dataset,
                    "supplied_fields":["source_definition","full_SELFIES","complete_protein_sequence"]})
                raw=response(probabilities[dataset][i])
                common.write_json(folder/"responses"/ident,{**case,"model":common.MODEL,"model_revision":common.REVISION,
                    "request_sha256":common.digest(payload),"status":"completed","http_status":200,"response":raw,
                    "score":common.extract_score(raw),"text":"No","finish_reason":"length"})
            with mock.patch.object(scorer,"ROOT",self.root),contextlib.redirect_stdout(io.StringIO()):scorer.score(folder)
            common.write_json(folder/"completion.json",{"generation_exit_code":0,"scoring_exit_code":0,"finished_at_utc":"synthetic"})
        for name,value in [("ROOT",self.root),("CONFIGS",pins),("COUNTS",{d:2 for d in pins})]:
            patch=mock.patch.object(aggregate,name,value);patch.start();self.addCleanup(patch.stop)

    def test_all_three_native_metrics_remain_separate_and_ordered(self):
        result=aggregate.aggregate();self.assertEqual(result["scoring_exit_code"],0)
        folder=self.root/"results/runs"/aggregate.RUN_ID
        scores=json.loads((folder/"scores.json").read_text())
        self.assertEqual(scores["planned"],6);self.assertEqual(scores["completed"],6)
        self.assertEqual(scores["metrics"]["human"],{"auroc":1.,"auprc":1.})
        self.assertEqual(scores["metrics"]["biosnap"],{"auroc":0.,"auprc":.5})
        self.assertEqual(scores["metrics"]["bindingdb"],{"auroc":.5,"auprc":.5})
        self.assertNotIn("auroc",scores["metrics"])
        self.assertTrue(scores["full_test_id_union_validation"]["union_matches_full_test_ids"])
        archived=json.loads((folder/"case_inputs.json").read_text())
        self.assertEqual([r["case_id"] for r in archived],[r["case_id"] for r in self.original])
        self.assertTrue(all(set(r)=={"task","case_id","variant","split","messages"} for r in archived))
        self.assertEqual(aggregate.aggregate(),result)

    def test_any_pending_prevents_completion(self):
        (self.folders["biosnap"]/"completion.json").unlink()
        with self.assertRaises(aggregate.Pending):aggregate.aggregate()
        self.assertFalse((self.root/"results/runs"/aggregate.RUN_ID/"completion.json").exists())

    def test_failure_blocks_even_with_another_dataset_pending(self):
        (self.folders["human"]/"completion.json").unlink()
        common.write_json(self.folders["bindingdb"]/"completion.json",{"generation_exit_code":1,"scoring_exit_code":0})
        with self.assertRaisesRegex(ValueError,"Failed dataset"):aggregate.aggregate()

    def test_source_order_missing_duplicate_and_extra_are_rejected(self):
        self.assertTrue(aggregate.ordered_union(self.original,self.original)["complete"])
        for broken in [list(reversed(self.original)),self.original[:-1],self.original+[self.original[0]]]:
            with self.assertRaisesRegex(ValueError,"ordered case IDs"):aggregate.ordered_union(self.original,broken)

    def test_summary_metric_tampering_cannot_pass_raw_recomputation(self):
        path=self.folders["human"]/"scores.json";summary=json.loads(path.read_text())
        summary["metrics"]["auroc"]=.5;common.write_json(path,summary)
        with self.assertRaisesRegex(ValueError,"independent raw-score recomputation"):aggregate.aggregate()

    def test_raw_response_hash_tampering_and_config_changes_are_rejected(self):
        path=next((self.folders["human"]/"responses").glob("*.json"))
        path.write_text(path.read_text()+"\n")
        with self.assertRaisesRegex(ValueError,"raw-output lock"):aggregate.aggregate()
        # Whitespace-only change to final config also invalidates its reviewed pin.
        cfg=self.root/"configs/local_dti_human.json";cfg.write_text(cfg.read_text()+"\n")
        with self.assertRaisesRegex(ValueError,"reviewed config changed"):aggregate.aggregate()

    def test_completed_score_artifact_is_immutable(self):
        aggregate.aggregate();folder=self.root/"results/runs"/aggregate.RUN_ID
        path=folder/"scores.json";path.write_text(path.read_text()+"\n")
        with self.assertRaisesRegex(ValueError,"Completed aggregate artifact hash changed"):aggregate.aggregate()

    def test_completed_aggregate_copy_raw_is_immutable(self):
        # Force copy fallback so this tests aggregate raw protection independently
        # of the source lock (a hard link would mutate the source as well).
        with mock.patch.object(aggregate.os,"link",side_effect=OSError("synthetic cross-device")):aggregate.aggregate()
        folder=self.root/"results/runs"/aggregate.RUN_ID
        path=next((folder/"responses").glob("*.json"));path.write_text(path.read_text()+"\n")
        with self.assertRaisesRegex(ValueError,"Completed aggregate raw artifact changed"):aggregate.aggregate()

    def test_full_input_archive_tampering_is_rejected(self):
        aggregate.aggregate();folder=self.root/"results/runs"/aggregate.RUN_ID
        path=folder/"case_inputs.json";rows=json.loads(path.read_text());rows.reverse();common.write_json(path,rows)
        with self.assertRaisesRegex(ValueError,"Archived full ordered input cases changed"):aggregate.aggregate()


if __name__=="__main__":unittest.main()
