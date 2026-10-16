"""Synthetic-only archived-output locking and PathVQA metric accounting."""
import contextlib
import io
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
import prepare_pathvqa_native as preparation
import run_local_labbench_multimodal as runner
import score_local_pathvqa as scorer
from test_pathvqa_native import image_bytes


class LocalPathVQATests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.root=Path(self.tmp.name)
        self.folder=self.root/"results/runs/synthetic_pathvqa";self.folder.mkdir(parents=True)
        raw=image_bytes("red");self.cases=[];refs=[]
        for i,(answer,group) in enumerate([("alpha beta","OPEN"),("yes","CLOSED"),("yes","CLOSED"),("no","CLOSED")]):
            c=preparation.model_case(i,{"question":"Artificial image question?","image":{"bytes":raw}});self.cases.append(c)
            refs.append({"task":"V03","case_id":c["case_id"],"variant":c["variant"],"split":c["split"],"target_answer":answer,"answer_type":group,"image_sha256":preparation.sha(raw)})
        (self.root/"inputs.jsonl").write_text("".join(json.dumps(c)+"\n" for c in self.cases))
        self.refs=self.root/"refs.jsonl";self.refs.write_text("".join(json.dumps(c)+"\n" for c in refs))
        scorer.write_json(self.root/"review.json",{"approved_case_ids":[c["case_id"] for c in self.cases],"held_cases":[]})
        dependencies=["scripts/prepare_pathvqa_native.py","scripts/score_local_pathvqa.py",*[r["path"] for r in preparation.scoring_sources()]]
        for name in dependencies:
            target=self.root/name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(preparation.ROOT/name,target)
        self.cfg={"run_id":"synthetic_pathvqa","approved_task_ids":["V03"],"variant":preparation.VARIANT,
            "model":"synthetic-model","model_revision":"synthetic-revision","input_file":"inputs.jsonl","review_file":"review.json",
            "scorer_reference_file":"refs.jsonl","scorer_reference_sha256":scorer.file_digest(self.refs),
            "model_facing_fields":["released_question_text","released_original_image_bytes"],
            "generation":{"max_tokens":4096,"temperature":1.,"top_p":.95,"top_k":20,"seed":42,"n":1,"chat_template_kwargs":{"enable_thinking":True,"reasoning_effort":"medium"}},
            "frozen_files_sha256":{n:scorer.file_digest(self.root/n) for n in ["inputs.jsonl","review.json",*dependencies]}}
        scorer.write_json(self.folder/"run_manifest.json",{"configuration":self.cfg,"case_contract_sha256":scorer.digest(self.cases),"planned_cases":4})
        for i,text in enumerate(["alpha alpha","yes","no"]):
            case=self.cases[i];ident=scorer.digest([case["task"],case["variant"],case["case_id"]])+".json"
            scorer.write_json(self.folder/"requests"/ident,runner.request_record(case,self.cfg))
            response={"model":"synthetic-model","choices":[{"message":{"content":text},"finish_reason":"stop"}],"usage":{"prompt_tokens":1,"completion_tokens":1}}
            scorer.write_json(self.folder/"responses"/ident,{**{k:case[k] for k in ["task","case_id","variant","split"]},
                "model":"synthetic-model","model_revision":"synthetic-revision","request_sha256":scorer.digest(runner.payload_for(case,self.cfg)),
                "status":"completed","http_status":200,"response":response,"text":text,"finish_reason":"stop"})

    def score(self):
        with mock.patch.object(scorer,"ROOT",self.root),contextlib.redirect_stdout(io.StringIO()):return scorer.score(self.folder)

    def test_corrected_denominators_bug_diagnostic_and_mirror_scope(self):
        result=self.score()
        self.assertAlmostEqual(result["metrics"]["open_token_recall"],2/3)
        self.assertEqual(result["metrics"]["closed_accuracy_corrected"],1/3)
        self.assertEqual(result["separate_diagnostics"]["closed_bug_compatible_accuracy"],1/2)
        self.assertEqual(result["separate_diagnostics"]["closed_bug_compatible_omitted"],1)
        self.assertEqual(result["missing_or_failed_outputs"],1)
        self.assertFalse(result["full_native_test_inputs"])
        self.assertEqual(result["native_full_test_case_count"],6761)
        self.assertEqual(result["publisher_full_test_case_count"],6719)
        self.assertIsNone(result["explanation_support_score"])

    def test_predictions_locked_before_reading_labels_and_missing_slots_fixed(self):
        original=Path.read_bytes;reads=[]
        def read(p):
            if p==self.refs:
                self.assertTrue((self.folder/"scoring_output_lock.json").exists());reads.append(p)
            return original(p)
        with mock.patch.object(Path,"read_bytes",read):self.score()
        self.assertEqual(len(reads),1)
        case=self.cases[3];ident=scorer.digest([case["task"],case["variant"],case["case_id"]])+".json"
        scorer.write_json(self.folder/"requests"/ident,runner.request_record(case,self.cfg))
        with self.assertRaisesRegex(ValueError,"output lock changed"):self.score()

    def test_raw_output_and_source_changes_rejected(self):
        self.score();p=next((self.folder/"responses").glob("*.json"));p.write_text(p.read_text()+"\n")
        with self.assertRaisesRegex(ValueError,"output lock changed"):self.score()
        p=self.root/"scripts/prepare_pathvqa_native.py";p.write_text(p.read_text()+"\n")
        with self.assertRaisesRegex(ValueError,"Frozen file changed"):self.score()

    def test_reference_group_cannot_enter_prompt(self):
        c={**self.cases[0],"answer_type":"OPEN"}
        with self.assertRaises(ValueError):scorer.expected_payload(c,self.cfg)


if __name__=="__main__":unittest.main()
