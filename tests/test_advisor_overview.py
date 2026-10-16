"""Presentation contracts using synthetic examples and catalog metadata only."""
import copy
import html
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("advisor_overview", ROOT / "scripts/update_grouped_evaluation_reports.py")
render = importlib.util.module_from_spec(spec)
spec.loader.exec_module(render)


class AdvisorOverviewTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.reports = Path(self.temp.name)
        self.data = json.loads((ROOT / "reports/TASK_HIERARCHY_DATA.json").read_text())
        self.original = copy.deepcopy(self.data)
        (self.reports / "QWEN_TASK_FEASIBILITY.json").write_bytes(
            (ROOT / "reports/QWEN_TASK_FEASIBILITY.json").read_bytes())
        good = {"examples": [{"task_id": "B04", "case_id": "synthetic-main", "main_example": True,
            "question_and_options_exact": "Question: Which synthetic value is smaller?\n\nOptions:\n(A) 1\n(B) 2",
            "local_score_record": {"correct": True, "answer": "A"},
            "native_gold": {"target_choice": "A"}, "images": [],
            "model_reasoning_text_exact": "Synthetic reasoning.\n\nOne is smaller than two.",
            "assistant_final_text_exact": "[ANSWER]A[/ANSWER]",
            "main_answer": "The synthetic answer is one.",
            "dataset_result": {"accuracy": 1.0, "correct": 1, "total": 1}},
            {"task_id": "B05", "case_id": "synthetic-extra",
             "question_and_options_exact": "Question: Another synthetic question?\n\nOptions:\n(A) Yes",
             "local_score_record": {"correct": True, "answer": "A"}, "native_gold": {"target_choice": "A"},
             "images": [], "model_reasoning_text_exact": "Additional full reasoning.",
             "assistant_final_text_exact": "Additional final answer.",
             "dataset_result": {"accuracy": 1.0, "correct": 1, "total": 1}}]}
        tools = {"cases": [{"title": "Synthetic structural task", "dataset": "Synthetic dataset",
            "input": "An artificial sequence", "input_sequence": "AAAA", "input_sequence_length": 4,
            "required_output": "Numerical 3D coordinates", "why_text_answer_is_insufficient": "Prose supplies no coordinates.",
            "tool_route": "A structure predictor and comparison", "source_url": "https://example.invalid/synthetic"},
            {"title": "Synthetic stability question", "dataset": "Synthetic stability dataset", "main_example": True,
             "input": "Original and changed artificial sequences", "input_sequences": {
                 "wild_type": {"case_id": "synthetic-wt", "sequence": "AAAAAQ", "length": 6}},
             "plain_question": "Is the synthetic variant more stable?", "plain_answer": "Synthetic reference value.",
             "experimental_reference": {"mutant_ddg_exp": 0.5},
             "result_scope": "Synthetic fixture, not a measurement.",
             "required_output": "A single stability number", "why_text_answer_is_insufficient": "The number needs computation.",
             "tool_route": "Embeddings, sampling and calculation", "source_url": "https://example.invalid/reference",
             "case_source_url": "https://example.invalid/testcases",
             "paper_url": "https://example.invalid/paper"}]}
        (self.reports / "ADVISOR_GOOD_EXAMPLES.json").write_text(json.dumps(good))
        (self.reports / "TOOL_REQUIRED_CASES.json").write_text(json.dumps(tools))

    def tearDown(self):
        self.temp.cleanup()

    def overview(self):
        with patch.object(render, "REPORTS", self.reports):
            return render.overview(self.data)

    def test_task_map_and_examples_are_visible_without_expanding_categories(self):
        output = self.overview()
        before_details = output.split("<details>", 1)[0]
        self.assertIn("## Task map", before_details)
        self.assertIn("## Worked examples", before_details)
        self.assertIn("The synthetic answer is one.", before_details)
        self.assertIn("+0.50 kcal/mol", before_details)
        self.assertIn("AAAAA**Q**", before_details)
        self.assertIn("What is BioEmu?", before_details)
        self.assertIn("Evaluation dataset:", before_details)
        self.assertIn("LAB-Bench FigQA", before_details)
        self.assertIn("BioEmu folding-free-energy benchmark", before_details)
        self.assertNotIn("This illustrates a published tool workflow", before_details)
        self.assertNotIn("not a measured Qwen failure", before_details)
        self.assertIn("WORKED_EXAMPLES.md", before_details)
        self.assertNotIn("Additional final answer.", before_details)
        self.assertNotIn("Numerical 3D coordinates", before_details)
        self.assertNotIn("Synthetic reasoning.", before_details)
        self.assertEqual(before_details.count("### Good result:"), 1)
        self.assertEqual(before_details.count("### Tool-use challenge:"), 1)
        self.assertEqual(output.count("<summary><h2>"), 8)
        self.assertEqual(output.count("<details>"), 9)

    def test_map_counts_task_families_instead_of_datasets_or_cases(self):
        output = self.overview().split("## Worked examples", 1)[0]
        self.assertIn("Number of task families", output)
        self.assertIn("not datasets or individual test questions", output)
        rows = [line.split("|") for line in output.splitlines() if line.startswith("| ")]
        counts = [int(row[2].strip()) for row in rows if row[2].strip().isdigit()]
        self.assertEqual(counts, [5, 5, 4, 1, 6, 5, 2, 6])
        self.assertEqual(sum(counts), 34)

    def test_companion_keeps_full_reasoning_and_additional_examples(self):
        with patch.object(render, "REPORTS", self.reports):
            output = render.worked_examples()
        for text in ["Synthetic reasoning.", "One is smaller than two.", "Additional full reasoning.",
                     "Additional final answer.", "Numerical 3D coordinates", "A single stability number"]:
            self.assertIn(text, output)
        self.assertIn("not measured Qwen failures", output)

    def test_every_dataset_is_preserved_without_run_bookkeeping(self):
        output = self.overview()
        for group in self.data["groups"]:
            self.assertIn(render.cell(group["dataset"]), output, group["id"])
        for phrase in ["Run status", "Running or queued", "trajectories uploaded", "finished runs",
                       "runnable with the current setup", "Status / what's missing", "heartbeat"]:
            self.assertNotIn(phrase, output)
        self.assertIn("Input / required computation", output)
        self.assertEqual(self.data, self.original)

    def test_pacific_timezone_observes_summer_and_winter_without_changing_source(self):
        self.assertEqual(render.pacific_time("2026-10-16T13:49:27+00:00"), "2026-10-16 06:49 PDT")
        self.assertEqual(render.pacific_time("2026-01-16T13:49:27Z"), "2026-01-16 05:49 PST")
        with self.assertRaises(ValueError):
            render.pacific_time("2026-10-16T13:49:27")

    def test_saved_reasoning_is_escaped_and_keeps_paragraphs(self):
        value = "First step.  \n\nLiteral <tag> & text."
        lines = render.quoted_record(value)
        self.assertEqual(lines[1], ">")
        recovered = "\n".join(line[2:] if line.startswith("> ") else "" for line in lines)
        self.assertEqual(html.unescape(recovered), value)

    def test_visual_requirements_distinguish_figures_from_tables(self):
        group = {"id": "synthetic", "inputInterface": "fallback"}
        self.assertIn("figure image", render.scientific_requirements(group, {"taskId": "B04"}))
        self.assertIn("table image", render.scientific_requirements(group, {"taskId": "B05"}))


if __name__ == "__main__":
    unittest.main()
