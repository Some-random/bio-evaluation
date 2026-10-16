"""Synthetic PMC clean-test exact prompt/scorer and activation/integrity tests."""
import ast
from collections import Counter
import contextlib
import copy
import io
import json
from pathlib import Path
import shutil
import sys
import tempfile
import types
import unittest
from unittest import mock
import zlib

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
import pmcvqa_clean_protocol as protocol
import prepare_pmcvqa_clean_native as preparation
import score_local_pmcvqa as scorer
import execute_local_pmcvqa as executor
import run_local_labbench_multimodal as runner


def jpeg():
    from PIL import Image
    stream=io.BytesIO();Image.new("RGB",(2,2),"red").save(stream,format="JPEG");return stream.getvalue()


def artificial(answer="Beta",label="B"):
    return {"Figure_path":"synthetic.jpg","Question":"Which artificial marker?","Answer":answer,"Answer_label":label,
        "Choice A":" A:Alpha","Choice B":" B:Beta","Choice C":" C:Gamma","Choice D":" D:Delta","Caption":"SCORER-FORBIDDEN-CAPTION"}


class ProtocolTests(unittest.TestCase):
    def test_native_test_prompt_ast_and_no_answer_caption_dependency(self):
        tree=ast.parse((protocol.SOURCE/"src__MedVInT_TD__Dataset__PMC_QA_Dataset.py").read_text())
        cls=next(n for n in tree.body if isinstance(n,ast.ClassDef));fn=next(n for n in cls.body if isinstance(n,ast.FunctionDef) and n.name=="__getitem__")
        branch=next(n for n in fn.body if isinstance(n,ast.If) and isinstance(n.test,ast.Compare) and isinstance(n.test.comparators[0],ast.Constant) and n.test.comparators[0].value=="Test")
        body=[n for n in branch.body if not isinstance(n,ast.Return)]
        code=compile(ast.fix_missing_locations(ast.Module(body=body,type_ignores=[])),"unchanged_source_TD_test_prompt","exec")
        row=artificial();choice=[row["Choice "+l] for l in "ABCD"]
        state={"self":types.SimpleNamespace(no_image=False,text_type="choice"),"sample":row,"Question":row["Question"],
               "Choice_A":choice[0],"Choice_B":choice[1],"Choice_C":choice[2],"Choice_D":choice[3],"choice_list":choice,
               "Anwser":row["Answer"],"image":"synthetic_image_placeholder"}
        exec(code,state)
        prompt,choices=protocol.native_prompt(row)
        self.assertEqual(prompt,state["item"]["input_ids"])
        self.assertEqual(choices,[state["item"]["Choice_"+l] for l in "ABCD"])
        case=protocol.model_case(0,row,jpeg());row["Answer"]="DIFFERENT SECRET";row["Answer_label"]="D";row["Caption"]="DIFFERENT CAPTION"
        self.assertEqual(protocol.model_case(0,row,jpeg()),case)
        self.assertEqual(set(case),{"task","case_id","variant","split","messages"})

    def test_source_ast_ties_allzero_and_last_character_are_preserved(self):
        fn=protocol.native_scorer();self.assertEqual(fn(["same","same"],"same"),0)
        self.assertIsNone(fn(["abc","def"],"xyz"))
        row=artificial();_,choices=protocol.native_prompt(row);ref={"native_choices":choices,**protocol.native_label(row,choices)}
        actual=protocol.score_text("B\n",ref)
        self.assertEqual(actual["native_final_character"],"\n");self.assertIsNone(actual["native_final_character_index"])
        self.assertEqual(actual["strict_final_label"],"B");self.assertEqual(actual["strict_final_label_correct"],1)
        self.assertEqual(actual["native_final_character_correct"],0)
        source=ast.parse((protocol.SOURCE/"src__MedVInT_TD__test.py").read_text())
        expression=next(n.value for n in ast.walk(source) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=="pred" for t in n.targets))
        result=eval(compile(ast.Expression(expression),"source_pred_extraction","eval"),{"generated_texts":["B\n"],"i":0})
        self.assertEqual(result,actual["native_final_character"])

    def test_missing_and_undefined_outputs_no_invented_choice(self):
        row=artificial();_,choices=protocol.native_prompt(row);ref={"native_choices":choices,**protocol.native_label(row,choices)}
        for text,completed in [(None,False),("",True),("\n",True)]:
            value=protocol.score_text(text,ref,completed)
            self.assertIsNone(value["native_final_character_index"])
            self.assertEqual(value["native_final_character_correct"],0)
        self.assertIsNone(protocol.strict_label("A or B"));self.assertEqual(protocol.strict_label("Explanation\nFinal answer: C"),"C")

    def test_image_preparation_waits_without_starting_another_acquisition(self):
        with tempfile.TemporaryDirectory() as tmp,mock.patch.object(preparation,"ROOT",Path(tmp)),mock.patch.object(preparation,"OUTPUT",Path(tmp)/"images"):
            with self.assertRaises(preparation.ImagesPending):preparation.image_records([artificial()])

    def test_original_image_crc_hash_and_bounded_range_are_checked(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);out=root/"output";src=root/"source";(out/"images").mkdir(parents=True);src.mkdir();raw=jpeg();(out/"images/synthetic.jpg").write_bytes(raw)
            protocol.save_json(root/"reports/pmcvqa_clean_image_acquisition.json",{"stage":"complete"})
            crc=zlib.crc32(raw)&0xffffffff;record={"image_name":"synthetic.jpg","sha256":protocol.file_sha(out/"images/synthetic.jpg"),"bytes":len(raw),"publisher_archive_member":"images/synthetic.jpg","publisher_zip_crc32":crc,"source_ranges":[{"start":100,"end":199,"bytes":100,"sha256":"f"*64}]}
            (src/"clean_image_acquisition.jsonl").write_text(json.dumps(record)+"\n")
            protocol.save_json(src/"selected_image_zip_metadata.json",{"synthetic.jpg":{"header_offset":100,"file_size":len(raw),"CRC":crc,"filename":"images/synthetic.jpg"}})
            with mock.patch.object(preparation,"ROOT",root),mock.patch.object(preparation,"OUTPUT",out),mock.patch.object(preparation,"SOURCE",src):
                self.assertEqual(len(preparation.image_records([artificial()])),1)
                (out/"images/synthetic.jpg").write_bytes(raw+b"changed")
                with self.assertRaisesRegex(ValueError,"ZIP identity inconsistent"):preparation.image_records([artificial()])

    def test_disabled_proposal_cannot_start_execution(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/"disabled.json";protocol.save_json(p,{"execution_authorized":False,"approved_task_ids":["V05"]})
            with mock.patch.object(executor.subprocess,"run") as dispatch:
                with self.assertRaisesRegex(ValueError,"not authorized"):executor.execute(p)
                dispatch.assert_not_called()

    def test_complete_image_binding_writes_exact_case_and_proposes_only_after_validation(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);out=root/"data";row=artificial();raw=jpeg();(out/"images").mkdir(parents=True);(out/"images/synthetic.jpg").write_bytes(raw)
            prompt,choices=protocol.native_prompt(row);ref={"task":"V05","case_id":"V05:clean2000:0000","variant":protocol.VARIANT,"split":"test_clean","native_choices":choices,**protocol.native_label(row,choices)}
            inputs=[{"case_id":ref["case_id"],"prompt":prompt}];report={"status":"waiting"}
            images=[{"image_name":"synthetic.jpg","sha256":__import__('hashlib').sha256(raw).hexdigest(),"path":str(out/"images/synthetic.jpg")}]
            with mock.patch.object(preparation,"ROOT",root),mock.patch.object(preparation,"OUTPUT",out),mock.patch.object(preparation,"REPORT",root/"report.json"),mock.patch.object(preparation,"contracts",return_value=([row],inputs,[ref],report)),mock.patch.object(preparation,"image_records",return_value=images),mock.patch.object(preparation,"propose",return_value="disabled_proposal") as propose:
                self.assertEqual(preparation.finalize(),"disabled_proposal");propose.assert_called_once()
                cases=list(map(json.loads,(out/"model_inputs.jsonl").read_text().splitlines()))
                self.assertEqual(cases,[protocol.model_case(0,row,raw)])
                bound=json.loads((out/"labels.jsonl").read_text());self.assertEqual(bound["image_sha256"],images[0]["sha256"])
                (out/"model_inputs.jsonl").write_text("changed\n")
                with self.assertRaisesRegex(ValueError,"complete model inputs changed"):preparation.finalize()
            with mock.patch.object(preparation,"contracts",return_value=([row],inputs,[ref],report)),mock.patch.object(preparation,"image_records",side_effect=preparation.ImagesPending("synthetic missing image")),mock.patch.object(preparation,"propose") as propose:
                with self.assertRaises(preparation.ImagesPending):preparation.finalize()
                propose.assert_not_called()


class OfflineScorerTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.root=Path(self.tmp.name)
        self.folder=self.root/"results/runs/synthetic";self.folder.mkdir(parents=True)
        self.cases=[];refs=[];contracts=[];raw=jpeg()
        for i,row in enumerate([artificial("Alpha","A"),artificial("Beta","B"),artificial("Gamma","D")]):
            case=protocol.model_case(i,row,raw);self.cases.append(case);prompt,choices=protocol.native_prompt(row)
            contracts.append({"case_id":case["case_id"],"prompt":prompt})
            refs.append({**{k:case[k] for k in ["task","case_id","variant","split"]},"native_choices":choices,
                **protocol.native_label(row,choices),"image_sha256":__import__('hashlib').sha256(raw).hexdigest()})
        for name,rows in [("inputs.jsonl",self.cases),("refs.jsonl",refs),("data/pmcvqa_clean_native/input_contracts.jsonl",contracts)]:
            p=self.root/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text("".join(json.dumps(r)+"\n" for r in rows))
        protocol.save_json(self.root/"review.json",{"reviewed":True,"approved_case_ids":[c["case_id"] for c in self.cases],"held_cases":[]})
        dependencies=["scripts/pmcvqa_clean_protocol.py","scripts/score_local_pmcvqa.py",*[r["path"] for r in protocol.native_sources()]]
        for name in dependencies:
            p=self.root/name;p.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(protocol.ROOT/name,p)
        self.cfg={"run_id":"synthetic","model":"synthetic-model","model_revision":"synthetic-revision","approved_task_ids":["V05"],"variant":protocol.VARIANT,
            "input_file":"inputs.jsonl","review_file":"review.json","scorer_reference_file":"refs.jsonl","scorer_reference_sha256":protocol.file_sha(self.root/"refs.jsonl"),
            "model_facing_fields":["source_TD_question_all_four_choices_prompt","original_JPEG_bytes"],"generation":copy.deepcopy(protocol.GENERATION),"paper_comparison":"Synthetic fixture only",
            "frozen_files_sha256":{name:protocol.file_sha(self.root/name) for name in ["inputs.jsonl","review.json","data/pmcvqa_clean_native/input_contracts.jsonl",*dependencies]}}
        protocol.save_json(self.folder/"run_manifest.json",{"configuration":self.cfg,"case_contract_sha256":protocol.digest(self.cases),"planned_cases":3,"solver_tools":[],"answer_keys_available_to_solver":False,"model_selection_on_test":False})
        for i,text in enumerate(["A","The answer is B\n"]):
            case=self.cases[i];identity=protocol.digest([case["task"],case["variant"],case["case_id"]])+".json"
            protocol.save_json(self.folder/"requests"/identity,runner.request_record(case,self.cfg))
            api={"model":"synthetic-model","choices":[{"message":{"content":text},"finish_reason":"stop"}],"usage":{"prompt_tokens":2,"completion_tokens":1}}
            protocol.save_json(self.folder/"responses"/identity,{**{k:case[k] for k in ["task","case_id","variant","split"]},"model":"synthetic-model","model_revision":"synthetic-revision",
                "request_sha256":protocol.digest(runner.payload_for(case,self.cfg)),"status":"completed","http_status":200,"response":api,"text":text,"finish_reason":"stop"})

    def score(self):
        with mock.patch.object(scorer,"ROOT",self.root),contextlib.redirect_stdout(io.StringIO()):return scorer.score(self.folder)

    def test_native_adapter_diagnostics_allcase_denominators_and_source_inconsistency(self):
        value=self.score();self.assertEqual(value["metrics"]["native_td_final_character_accuracy"],1/3)
        self.assertEqual(value["metrics"]["strict_final_label_accuracy"],2/3)
        self.assertEqual(value["planned"],3);self.assertEqual(value["completed"],2);self.assertEqual(value["missing_or_failed_outputs"],1)
        self.assertEqual(value["native_target_vs_released_label_mismatches"],1);self.assertEqual(value["native_undefined_mapping_count"],2)
        self.assertFalse(value["full_native_test_inputs"]);self.assertFalse(value["publisher_full_archive_sha256_verified"])

    def test_lock_before_labels_and_raw_mutation_rejected(self):
        ref=self.root/"refs.jsonl";read=Path.read_bytes;observed=[]
        def checked(path):
            if path==ref:self.assertTrue((self.folder/"scoring_output_lock.json").exists());observed.append(path)
            return read(path)
        with mock.patch.object(Path,"read_bytes",checked):self.score()
        self.assertEqual(len(observed),1)
        path=next((self.folder/"responses").glob("*.json"));path.write_text(path.read_text()+"\n")
        with self.assertRaisesRegex(ValueError,"raw output lock changed"):self.score()

    def test_reference_fields_cannot_enter_requests(self):
        bad={**self.cases[0],"Answer":"SECRET"}
        with self.assertRaises(ValueError):scorer.expected_payload(bad,self.cfg)


if __name__=="__main__":unittest.main()
