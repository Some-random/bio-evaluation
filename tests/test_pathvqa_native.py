"""Synthetic question/image identity, source metric and known scorer-bug tests."""
import ast
import base64
from collections import defaultdict
import copy
import inspect
import io
from pathlib import Path
import sys
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
import prepare_pathvqa_native as pathvqa


def image_bytes(color):
    from PIL import Image
    b=io.BytesIO();Image.new("RGB",(2,2),color).save(b,format="PNG");return b.getvalue()


class PathVQATests(unittest.TestCase):
    def test_full_question_and_image_preserved_without_label_fields(self):
        raw=image_bytes("red");row={"question":"Artificial test question ?","image":{"bytes":raw},"answer":"SECRET"}
        case=pathvqa.model_case(0,row)
        self.assertEqual(case["messages"][0]["content"][0]["text"],row["question"])
        url=case["messages"][0]["content"][1]["image_url"]["url"]
        self.assertEqual(base64.b64decode(url.split(",",1)[1]),raw)
        row["answer"]="CHANGED SECRET";row["answer_type"]="CLOSED"
        self.assertEqual(pathvqa.model_case(0,row),case)
        self.assertEqual(set(case),{"task","case_id","variant","split","messages"})
        with self.assertRaises(ValueError):pathvqa.model_case(0,{"question":"X","image":{"bytes":b""}})

    def test_identity_proves_cleanup_but_discloses_duplicate_and_ambiguity(self):
        original=[{"img_id":image,"sentf":{"pvqa":["Question  A ?","Question  A ?"]},
                   "labelf":{"pvqa":[{"Answer":1},{"Answer":1}]}} for image in ["synthetic_a","synthetic_b"]]
        mirror=[{"question":"question a?","answer":"answer","image":{"bytes":image_bytes(c)}} for c in ["red","blue"]]
        result=pathvqa.source_identity(original,mirror)
        self.assertEqual(result["original_test_question_count"],4)
        self.assertEqual(result["removed_exact_triplet_duplicates"],2)
        self.assertTrue(result["full_normalized_deduplicated_question_answer_multiset_match"])
        self.assertEqual(result["source_image_group_candidate_counts"],{2:2})
        self.assertFalse(result["original_per_image_byte_identity_verified"])
        wrong=copy.deepcopy(mirror);wrong[0]["question"]="changed"
        with self.assertRaisesRegex(ValueError,"multiset differs"):pathvqa.source_identity(original,wrong)

    def test_open_metric_uses_actual_pinned_source_token_counting(self):
        # Source function counts repeated candidate tokens in true positives;
        # this intentionally differs from ordinary multiset token recall.
        scores=pathvqa.score_answer("alpha alpha","alpha beta","OPEN")
        self.assertAlmostEqual(scores["open_token_recall"],2/3)
        self.assertEqual(pathvqa.score_answer("","alpha beta","OPEN")["open_token_recall"],0)

    def test_closed_bug_is_checked_against_unchanged_official_ast_branch(self):
        code=ast.parse((pathvqa.SOURCE/"llava_v1_run_eval_pvqa.py").read_text())
        function=next(n for n in code.body if isinstance(n,ast.FunctionDef) and n.name=="evaluate")
        loop=next(n for n in function.body if isinstance(n,ast.For))
        branch=next(n for n in loop.body if isinstance(n,ast.If) and isinstance(n.test,ast.Compare) and
                    isinstance(n.test.left,ast.Subscript) and isinstance(n.test.left.value,ast.Name) and n.test.left.value.id=="gt_item")
        closed_branch=branch.orelse[0]
        reference_code=compile(ast.fix_missing_locations(ast.Module(body=closed_branch.body,type_ignores=[])),"official_closed_branch","exec")
        for prediction,gold in [("yes","yes"),("no","yes"),("","no"),("yes and no","no")]:
            state={"closed_scores":defaultdict(list),"pred_item":{"question_id":0},"pred_value":prediction,"gt_value":gold}
            exec(reference_code,state)
            actual=pathvqa.score_answer(prediction,gold,"CLOSED")
            self.assertEqual(actual["closed_bug_compatible_denominator"],len(state["closed_scores"]["hit"]))
            self.assertEqual(actual["closed_bug_compatible_numerator"],sum(state["closed_scores"]["hit"]))
        self.assertEqual(pathvqa.score_answer("yes and no","no","CLOSED")["closed_strict_exact_hit"],0)

    def test_group_denominators_and_missing_outputs_are_explicit(self):
        examples=[("yes","yes"),("no","yes"),("","no")]
        rows=[{"answer_type":"CLOSED","native_scores":pathvqa.score_answer(pred,gold,"CLOSED")} for pred,gold in examples]
        rows.append({"answer_type":"OPEN","native_scores":pathvqa.score_answer("","alpha","OPEN")})
        metrics=pathvqa.metrics_for(rows)
        self.assertEqual(metrics["closed_accuracy_corrected"],1/3)
        self.assertEqual(metrics["closed_bug_compatible_accuracy"],1/2)
        self.assertEqual(metrics["closed_bug_compatible_omitted"],1)
        self.assertEqual(metrics["closed_corrected_denominator"],3)
        self.assertEqual(metrics["open_token_recall"],0)
        self.assertNotIn("overall_accuracy",metrics)

    def test_official_open_cli_arity_blocker_and_source_blob_verification(self):
        sources=pathvqa.scoring_sources();self.assertEqual(len(sources),4)
        self.assertTrue(all(s["publisher_digest_verified"] for s in sources))
        _,module=pathvqa.native_modules()
        self.assertEqual(len(inspect.signature(module.calculate_appearance_with_normalization).parameters),3)
        tree=ast.parse((pathvqa.SOURCE/"llava_v1_run_eval_pvqa.py").read_text())
        calls=[n for n in ast.walk(tree) if isinstance(n,ast.Call) and isinstance(n.func,ast.Name) and n.func.id=="calculate_appearance_with_normalization"]
        self.assertEqual([len(n.args) for n in calls],[2])


if __name__=="__main__":unittest.main()
