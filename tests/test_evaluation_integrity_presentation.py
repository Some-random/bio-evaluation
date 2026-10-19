"""Synthetic presentation contract tests for a staged, display-only proposal."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('proposed_glance', ROOT / 'scripts/update_results_at_a_glance.py')
report = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(report)


def row(task, **overrides):
    value = {'task_id': task, 'task_name': 'Synthetic task', 'run_id': 'synthetic_' + task,
        'protocol_variant': 'SYNTHETIC', 'counts': {'planned': 10, 'completed': 10, 'parsed': 3, 'invalid_outputs': 7},
        'finish_reasons': {'length': 6, 'stop': 4}, 'metrics': {'accuracy': .2}, 'caveats': ['Existing caveat.'],
        'source_scores': 'results/runs/synthetic_' + task + '/scores.json',
        'source_completion': 'results/runs/synthetic_' + task + '/completion.json',
        'scores_sha256': 'frozen_native_score_hash', 'selected_published_reference': None,
        'completion_scope': 'completed_declared_run', 'dataset': None, 'native_split': None,
        'case_scope': 'synthetic_full', 'generation': {'max_tokens': 4096}}
    value.update(overrides)
    return value


def document(rows, diagnostics=None):
    return {'generated_at_utc': '2026-10-19T05:00:00+00:00', 'catalog_settings': 64,
        'completed_whole_declared_setting_ids': [r['task_id'] for r in rows],
        'completed_rows': rows, 'diagnostic_only_finished_runs': diagnostics or [],
        'P43': {'completed_components': [], 'whole_setting_complete': False},
        'P29_seed_only_offline_audit': None, 'blockers': [], 'warnings': [],
        'metadata_history_retention': {'preserved': True}}


class QualificationTests(unittest.TestCase):
    def test_reaction_audit_numbers_require_the_exact_audited_score(self):
        original = row('P16')
        self.assertNotIn('851', ' '.join(report.presentation_caveats(original)))
        audited = row('P16', scores_sha256='024501321eb30797df29401b256007ab6992881a6670027cb5232cce72d5972b')
        before = copy.deepcopy(audited)
        text = ' '.join(report.presentation_caveats(audited))
        self.assertIn('851 rejected nonempty answers', text)
        self.assertIn('correctness was not measured', text)
        self.assertEqual(audited, before)

    def test_retained_legacy_rows_are_qualified_without_mutation(self):
        doc = document([row('B07'), row('P01')]); before = copy.deepcopy(doc)
        text = report.render_markdown(doc)
        self.assertIn('3/10 final answers parsed', text)
        self.assertIn('6/10 outputs reached the output-token cap', text)
        self.assertIn('rejects 7/10 outputs', text)
        self.assertIn('Native coverage measures non-abstention', text)
        self.assertEqual(doc, before)
        self.assertIn('EVALUATION_INTEGRITY_AUDIT_2026-10-18.md', text)

    def test_medical_rows_explain_metric_predicates(self):
        text = report.render_markdown(document([row(task) for task in ['V01', 'V02', 'V03']]))
        self.assertEqual(text.count('CLOSED uses source substring Yes/No matching'), 3)
        self.assertIn('corrected CLOSED score fixes the denominator', text)
        self.assertIn('OPEN measures token recall', text)

    def test_pmcvqa_extraction_conditions_are_distinct(self):
        text = report.render_markdown(document([row('V05')]))
        self.assertIn('scores only the final character', text)
        self.assertIn('full-text choice matching is a separate adaptation', text)

    def test_description_parsed_is_not_usable_answer_count(self):
        text = report.render_markdown(document([row(task) for task in ['P23', 'P24', 'P25', 'P26']]))
        self.assertEqual(text.count('ROUGE measures lexical overlap'), 4)
        self.assertEqual(text.count('Parsed means a text record, even when empty'), 4)
        self.assertEqual(text.count('6/10 outputs reached the output-token cap'), 4)

    def test_diagnostic_row_shows_counts_and_keeps_null_and_denominator(self):
        diagnostic = row('P07', metrics={'spearman': None, 'spearman_parsed_only': .1})
        doc = document([], [diagnostic]); before = copy.deepcopy(doc)
        text = report.render_markdown(doc)
        self.assertIn('3/10 numeric final answers parsed', text)
        self.assertIn('6/10 outputs reached the output-token cap', text)
        self.assertIn('Full-test correlation is undefined', text)
        self.assertEqual(doc, before)
        self.assertIsNone(doc['diagnostic_only_finished_runs'][0]['metrics']['spearman'])

    def test_complete_future_regression_does_not_claim_undefined(self):
        future = row('P07', metrics={'spearman': .2}, counts={'planned': 10, 'parsed': 10}, finish_reasons={'stop': 10})
        self.assertNotIn('undefined', ' '.join(report.presentation_caveats(future)))

    def test_helper_is_idempotent_preserves_existing_caveats(self):
        value = row('B07'); first = report.presentation_caveats(value)
        self.assertEqual(first[0], 'Existing caveat.')
        self.assertEqual(first, report.presentation_caveats({**value, 'caveats': first}))
        self.assertEqual(value['caveats'], ['Existing caveat.'])

    def test_no_new_output_counts_are_invented(self):
        value = row('P23', counts={}, finish_reasons={})
        self.assertNotIn('/10', ' '.join(report.presentation_caveats(value)))
        self.assertEqual(report.presentation_caveats(row('B07', counts={})), ['Existing caveat.'])


if __name__ == '__main__':
    unittest.main()
