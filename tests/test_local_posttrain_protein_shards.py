"""Synthetic exact union, label-free shards, once-global scoring and failure tests."""
import copy
import base64
import inspect
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
import local_posttrain_protein_shards as common
import aggregate_local_posttrain_protein_shards as aggregation
import execute_local_posttrain_protein_shard as executor
import run_local_labbench_eight_gpu as expanded_runner
import run_local_labbench_multimodal as frozen_runner
from run_local_labbench_multimodal import request_record


class ExpandedRunnerCompatibilityTests(unittest.TestCase):
    def test_frozen_runner_hash_and_payload_records_are_byte_equivalent(self):
        project=Path(__file__).resolve().parents[1]
        self.assertEqual(common.file_sha(project/common.RUNNER),common.RUNNER_SHA256)
        for name in ["digest","validate_content","supplied_fields_for","payload_for","request_record"]:
            self.assertEqual(inspect.getsource(getattr(expanded_runner,name)),
                             inspect.getsource(getattr(frozen_runner,name)))
        settings={"model":"synthetic-model","approved_task_ids":["P29"],"variant":"synthetic",
            "model_facing_fields":["synthetic_context"],"generation":{"max_tokens":4096,"temperature":1.,
                "top_p":.95,"top_k":20,"seed":42,"n":1,"chat_template_kwargs":{"enable_thinking":True,"reasoning_effort":"medium"}}}
        contents=["Synthetic text only; no biological case.",
            [{"type":"text","text":"Synthetic image context."},
             {"type":"image_url","image_url":{"url":"data:image/png;base64,"+base64.b64encode(b"\x89PNG\r\n\x1a\nsynthetic").decode()}}]]
        for content in contents:
            case={"task":"P29","case_id":"synthetic:compatibility","variant":"synthetic","split":"synthetic",
                  "messages":[{"role":"user","content":content}]}
            for name in ["payload_for","request_record"]:
                old=getattr(frozen_runner,name)(case,settings);new=getattr(expanded_runner,name)(case,settings)
                self.assertEqual(json.dumps(old,ensure_ascii=False).encode(),json.dumps(new,ensure_ascii=False).encode())


class ShardTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.root=Path(self.tmp.name)
        patch=mock.patch.object(common,"ROOT",self.root);patch.start();self.addCleanup(patch.stop)
        for name,value in [("SHARD_SIZE",2),("FULL_INPUT","full_inputs.jsonl"),("FULL_REVIEW","full_review.json"),("FULL_CONFIG","full_config.json")]:
            patch=mock.patch.object(common,name,value,create=True);patch.start();self.addCleanup(patch.stop)
        patch=mock.patch.dict(common.protocol.SPLITS,{"ood":("ood-test",4,"synthetic")});patch.start();self.addCleanup(patch.stop)
        self.cases=[{"task":"P29","case_id":"P29:synthetic:"+str(i),"variant":common.protocol.VARIANT,"split":"synthetic",
            "messages":[{"role":"user","content":"Synthetic allowed input context GO:9999999; no annotation target."}]} for i in range(4)]
        self.write_lines(common.FULL_INPUT,self.cases);common.save(self.root/common.FULL_REVIEW,{"reviewed":True,"approved_case_ids":[c["case_id"] for c in self.cases],"held_cases":[]})
        self.refs=self.root/"refs.jsonl";self.refs.write_text("SCORER_ONLY_SENTINEL\n")
        (self.root/common.RUNNER).parent.mkdir(parents=True,exist_ok=True);(self.root/common.RUNNER).write_text("synthetic fixed runner fixture\n")
        base={"model":"synthetic-model","model_revision":"synthetic-revision","checkpoint_precision":"synthetic_float32","concurrency":4,
            "generation":{"max_tokens":4096,"temperature":1.,"top_p":.95,"top_k":20,"seed":42,"n":1,"chat_template_kwargs":{"enable_thinking":True,"reasoning_effort":"medium"}}}
        common.save(self.root/"base.json",base)
        frozen={name:common.file_sha(self.root/name) for name in [common.FULL_INPUT,common.FULL_REVIEW,common.RUNNER]}
        self.full={**base,"native_split":"ood","run_id":"synthetic_full","approved_task_ids":["P29"],"variant":common.protocol.VARIANT,
            "input_file":common.FULL_INPUT,"review_file":common.FULL_REVIEW,"scorer_reference_file":"refs.jsonl","scorer_reference_sha256":common.file_sha(self.refs),
            "model_facing_fields":["synthetic_input"],"prompt_policy":"synthetic allowed input only","frozen_files_sha256":frozen,
            "full_test_case_count":4,"shard_count":2,"shard_size":2,"aggregate_only":True,"generator_execution_allowed":False,
            "endpoint":"aggregate-only://offline","incomplete_output_policy":"synthetic all-case failures retained"}
        self.shards=[];entries=[]
        for index in range(2):
            group=self.cases[index*2:(index+1)*2];inp=f"shard{index}.jsonl";review=f"review{index}.json"
            self.write_lines(inp,group);common.save(self.root/review,{"reviewed":True,"approved_case_ids":[c["case_id"] for c in group],"held_cases":[]})
            gpu,port=common.REPLICAS[index]
            cfg={**self.full,"run_id":"synthetic_shard"+str(index),"execution_authorized":False,"input_review_complete":True,
                "aggregate_only":False,"generator_execution_allowed":True,"case_scope":"task_shard_only","input_file":inp,"review_file":review,
                "gpu_ids":[gpu],"endpoint":f"http://127.0.0.1:{port}/v1","shard_index":index,"global_shard_index":index,"source_start_index":index*2,"source_stop_index":index*2+2,
                "aggregate_config_file":common.FULL_CONFIG,"full_input_file":common.FULL_INPUT,"full_input_sha256":common.file_sha(self.root/common.FULL_INPUT),
                "full_review_file":common.FULL_REVIEW,"full_review_sha256":common.file_sha(self.root/common.FULL_REVIEW),"runner":common.RUNNER,
                "shard_plan_file":common.PLAN_FILE,"frozen_files_sha256":{**frozen,inp:common.file_sha(self.root/inp),review:common.file_sha(self.root/review)}}
            path=f"config{index}.json";common.save(self.root/path,cfg);self.shards.append(cfg)
            entries.append({"config_file":path,"config_sha256":common.file_sha(self.root/path),"run_id":cfg["run_id"],"shard_index":index,"cases":2,"gpu_ids":[gpu],"endpoint":cfg["endpoint"]})
        self.full["shard_configs"]=entries;common.save(self.root/common.FULL_CONFIG,self.full)
        self.plan={"global_shard_start_index":0,"aggregate_config_file":common.FULL_CONFIG,"aggregate_config_sha256":common.file_sha(self.root/common.FULL_CONFIG),
            "source_recipe_file":"base.json","source_recipe_sha256":common.file_sha(self.root/"base.json"),"shards":entries,"aggregate_run_id":"synthetic_full",
            "incomplete_output_policy":self.full["incomplete_output_policy"],"global_metric_policy":"Synthetic once-global metric, no shard averaging"}
        common.save(self.root/common.PLAN_FILE,self.plan);self.plan_sha=common.file_sha(self.root/common.PLAN_FILE)
        common.save(self.root/common.APPROVAL_FILE,{"execution_authorized":True,"approved_task_ids":["P29"],"model":base["model"],"model_revision":base["model_revision"],
            "generation_sha256":common.digest(base["generation"]),"plan_sha256":self.plan_sha,"approved_config_sha256":{e["config_file"]:e["config_sha256"] for e in entries},"incomplete_output_policy":self.full["incomplete_output_policy"]})
        for index,cfg in enumerate(self.shards):self.emit_shard(index)

    def write_lines(self,name,rows):
        p=self.root/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text("".join(json.dumps(r)+"\n" for r in rows))

    def emit_shard(self,index,missing_last=False,generation_code=0):
        cfg=self.shards[index];entry=self.plan["shards"][index];cases=self.cases[index*2:(index+1)*2];folder=self.root/"results/runs"/cfg["run_id"];folder.mkdir(parents=True,exist_ok=True)
        gpu,port=common.REPLICAS[index];manifest={"configuration":cfg,"configuration_sha256":entry["config_sha256"],"case_contract_sha256":common.digest(cases),"planned_cases":len(cases),
            "runner_sha256":cfg["frozen_files_sha256"][common.RUNNER],"solver_tools":[],"answer_keys_available_to_solver":False,"model_selection_on_test":False,
            "server":{"gpu_ids":[gpu],"model":cfg["model"],"revision":cfg["model_revision"],"pid":123,"proc_start_ticks":"456","port":port},
            "serving_configuration":{"host":"127.0.0.1","port":port,"gpu_ids":[gpu],"model":cfg["model"],"revision":cfg["model_revision"]}}
        common.save(folder/"run_manifest.json",manifest)
        for case in cases[:-1] if missing_last else cases:
            identity=common.digest([case["task"],case["variant"],case["case_id"]])+".json";req=request_record(case,cfg)
            common.save(folder/"requests"/identity,req)
            common.save(folder/"responses"/identity,{**{k:case[k] for k in ["task","case_id","variant","split"]},"model":cfg["model"],"model_revision":cfg["model_revision"],
                "request_sha256":req["request_sha256"],"status":"completed","http_status":200,"text":"GO:0000002","finish_reason":"stop",
                "response":{"model":cfg["model"],"choices":[{"message":{"role":"assistant","reasoning":"GO:0000001","content":"GO:0000002"},"finish_reason":"stop"}]}})
        audit,_=common.audit_raw(folder,cases,cfg,entry["config_sha256"]);common.save(folder/"scores.json",audit)
        done={"generation_exit_code":generation_code,"scoring_exit_code":0,"raw_audit_exit_code":0,"configuration_sha256":entry["config_sha256"],"execution_approval":common.approval_for(self.root/entry["config_file"],cfg),**common.metadata(cfg)}
        for name in ["run_manifest.json","scores.json","scoring_output_lock.json"]:done[name.replace(".json","")+"_sha256"]=common.file_sha(folder/name)
        common.save(folder/"completion.json",done)

    def fake_global(self,full):
        folder=self.root/"results/runs"/full["run_id"]
        self.assertTrue((folder/"scoring_output_lock.json").exists())
        # Only this mocked global stage may touch the scorer-side sentinel.
        self.assertEqual(self.refs.read_text(),"SCORER_ONLY_SENTINEL\n")
        lock=json.loads((folder/"scoring_output_lock.json").read_text());available=sum(v is not None for k,v in lock["files_sha256"].items() if k.startswith("responses/"))
        summary={"planned":4,"completed":available,"case_scope":"full_synthetic_test" if available==4 else "INCOMPLETE_allcase_penalty",
            "generation_completeness":"complete" if available==4 else "incomplete_with_all_eligible_failures_retained",
            "metrics":{"native_augmented_F1":.37}}
        common.save(folder/"scores.json",summary);return 0

    def test_single_global_call_exact_union_and_idempotent_artifact_hash(self):
        with mock.patch.object(aggregation,"run_native_scorer",side_effect=self.fake_global) as metric:
            result=aggregation.aggregate(self.plan,self.plan_sha);self.assertEqual(metric.call_count,1)
            self.assertEqual(aggregation.aggregate(self.plan,self.plan_sha),result);self.assertEqual(metric.call_count,1)
        self.assertEqual(result["generation_exit_code"],0);self.assertEqual(result["evaluation_status"],"complete")
        summary=json.loads((self.root/"results/runs/synthetic_full/scores.json").read_text());self.assertEqual(summary["native_global_metric_call_count"],1)
        self.assertTrue(summary["full_test_id_union_validation"]["union_matches_full_test_ids"])
        self.assertEqual(summary["metrics"]["native_augmented_F1"],.37)

    def test_all_shards_must_be_terminal_before_any_global_scorer(self):
        (self.root/"results/runs/synthetic_shard1/completion.json").unlink()
        with mock.patch.object(aggregation,"run_native_scorer") as metric:
            with self.assertRaises(aggregation.Pending):aggregation.aggregate(self.plan,self.plan_sha)
            metric.assert_not_called()

    def test_missing_output_is_retained_incomplete_not_success_subset(self):
        folder=self.root/"results/runs/synthetic_shard1"
        # Replace only this synthetic fixture before terminal locking exists.
        shutil=__import__('shutil');shutil.rmtree(folder);self.emit_shard(1,missing_last=True,generation_code=1)
        with mock.patch.object(aggregation,"run_native_scorer",side_effect=self.fake_global):result=aggregation.aggregate(self.plan,self.plan_sha)
        summary=json.loads((self.root/"results/runs/synthetic_full/scores.json").read_text())
        self.assertEqual(result["generation_exit_code"],1);self.assertEqual(result["scoring_exit_code"],0)
        self.assertEqual(summary["planned"],4);self.assertEqual(summary["completed"],3)
        self.assertEqual(summary["case_scope"],"INCOMPLETE_allcase_penalty")
        self.assertTrue(result["full_test_id_union_validation"]["complete"])

    def test_locked_missing_slot_cannot_appear_later(self):
        folder=self.root/"results/runs/synthetic_shard1";__import__('shutil').rmtree(folder);self.emit_shard(1,missing_last=True,generation_code=1)
        case=self.cases[-1];ident=common.digest([case["task"],case["variant"],case["case_id"]])+".json";common.save(folder/"requests"/ident,request_record(case,self.shards[1]))
        with self.assertRaisesRegex(ValueError,"lock changed"):aggregation.validate_plan(self.plan)

    def test_exact_order_duplicate_or_prompt_changes_rejected(self):
        for groups in [[self.cases[2:],self.cases[:2]],[self.cases[:2],self.cases[:2]],[self.cases[:2],self.cases[2:-1]]]:
            with self.assertRaises(ValueError):common.ordered_union(self.cases,groups)
        changed=copy.deepcopy(self.cases);changed[0]["messages"][0]["content"]="different"
        with self.assertRaises(ValueError):common.ordered_union(self.cases,[changed])

    def test_approval_gate_rejects_without_dispatch_and_recipe_hash_bound(self):
        path=self.root/common.APPROVAL_FILE;approval=json.loads(path.read_text());approval["execution_authorized"]=False;common.save(path,approval)
        with mock.patch.object(executor.subprocess,"run") as dispatch:
            with self.assertRaisesRegex(ValueError,"execution approval"):executor.execute(self.root/"config0.json")
            dispatch.assert_not_called()

    def test_shard_stage_never_reads_references_or_computes_native_metrics(self):
        read=Path.read_bytes
        def reject(path):
            if path==self.refs:raise AssertionError("gold read by shard audit")
            return read(path)
        with mock.patch.object(Path,"read_bytes",reject),mock.patch.object(common.protocol,"score_prediction",side_effect=AssertionError("native metric called by shard")):
            full,cases,sources,union=aggregation.validate_plan(self.plan)
        self.assertEqual(len(cases),4);self.assertEqual(len(sources),2)

    def test_raw_metric_and_completed_aggregate_tampering_blocked(self):
        with mock.patch.object(aggregation,"run_native_scorer",side_effect=self.fake_global):aggregation.aggregate(self.plan,self.plan_sha)
        p=self.root/"results/runs/synthetic_full/scores.json";p.write_text(p.read_text()+"\n")
        with self.assertRaisesRegex(ValueError,"Completed aggregate artifact hash changed"):aggregation.aggregate(self.plan,self.plan_sha)


if __name__=="__main__":unittest.main()
