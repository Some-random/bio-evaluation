import importlib.util
from pathlib import Path
import unittest

spec=importlib.util.spec_from_file_location("scoring",Path(__file__).resolve().parents[1]/"scripts/score_results.py")
scoring=importlib.util.module_from_spec(spec);spec.loader.exec_module(scoring)


class NativeScoringTests(unittest.TestCase):
    def test_lab_parser_tagged_bare_and_invalid_answers(self):
        self.assertEqual(scoring.lab_answer("Reasoning. [ANSWER]C[/ANSWER]",5),"C")
        self.assertEqual(scoring.lab_answer("D",5),"D")
        self.assertIsNone(scoring.lab_answer("The protein is soluble.",5))
        self.assertIsNone(scoring.lab_answer("[ANSWER]Z[/ANSWER]",5))

    def test_pg_direction_ties_and_source_grouping(self):
        prompt=scoring.module("test_pg",scoring.ROOT/"sources/pg__src__prompt.py")
        self.assertAlmostEqual(prompt.score_ranking(["M01","M02","M03"],["M01","M02","M03"],
            [("a","A",3),("b","B",2),("c","C",1)]),1)
        self.assertEqual(prompt.spearman([1,2,3],[2,2,2]),0)
        agg=scoring.module("test_agg",scoring.ROOT/"sources/pg__src__aggregate.py")
        meta={"a":{"uniprot_id":"p1","function":"Activity"},
              "b":{"uniprot_id":"p1","function":"Activity"},
              "c":{"uniprot_id":"p2","function":"Binding"}}
        self.assertEqual(agg.macro_from_assay_rho({"a":1,"b":1,"c":-1},meta)[0],0)


if __name__=="__main__":unittest.main()
