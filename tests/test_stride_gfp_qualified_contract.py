import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location('stride_gfp_contract', Path(__file__).parents[1] / 'scripts/stride_gfp_qualified_contract.py')
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)


def row(i, sequence='ACEE', score=2.0, **kwargs):
    return {'sample_index': i, 'final_text': '{"protein": "'+sequence+'"}',
            'reasoning_text': 'synthetic fixture', 'oracle_score': score,
            'finish_reason': 'stop', **kwargs}


class TestStrideGfpContract(unittest.TestCase):
    def test_source_parser_channel_reconstruction_and_no_reasoning_answer_fallback(self):
        separate = c.parse_channels('{"protein":"ACDE"}', 'synthetic fixture')
        combined = c.parse_channels('<think>synthetic fixture</think>{"protein":"ACDE"}', None)
        assert separate['protein'] == combined['protein'] == 'ACDE'
        assert not c.parse_channels('', '{"protein":"ACDE"}')['valid_format']
        assert not c.parse_channels('```json\n{"protein":"ACDE"}\n```', 'x')['valid_format']
        assert not c.parse_channels('{"protein":"ACDE"}', None)['valid_format']


    def test_endpoint_budget_distinguishes_hamming_and_indels_without_trace_claim(self):
        assert c.validate_endpoint('ACDE', 'ACEE', 'replace_only')['eligible']
        assert not c.validate_endpoint('ACDE', 'ACDDE', 'replace_only')['eligible']
        assert c.validate_endpoint('ACDE', 'ACDDE', 'full_atomic')['eligible']
        assert not c.validate_endpoint('ACDE', 'WWWW', 'full_atomic')['eligible']
        assert not c.validate_endpoint('ACDE', 'ACDE', 'replace_only')['eligible']
        assert not c.validate_endpoint('ACDE', 'acde', 'full_atomic')['eligible']
        assert c.validate_endpoint('ACDE', 'ACEE', 'replace_only')['trajectory_correctness'] == 'unassessed'


    def test_fixed_denominator_preserves_duplicates_and_invalids(self):
        samples = [row(0), row(1), row(2, 'ACDE'), row(3, 'ACZE')]
        got = c.summarize('ACDE', 'replace_only', samples, 1.0, 4)
        assert got['qualified_oracle_success'] == 0.5
        assert got['improved_samples'] == 2
        assert got['unique_improved_sequences'] == 1
        assert got['improved_sequence_uniqueness'] == 0.5
        assert got['invalid_generation_or_endpoint_count'] == 2
        assert got['native_novelty'] is None


    def test_missing_oracle_is_not_imputed_as_biological_failure(self):
        got = c.summarize('ACDE', 'replace_only', [row(0, score=None)], 1.0, 1)
        assert got['qualified_oracle_success'] is None
        assert got['improved_sequence_uniqueness'] is None
        assert not got['scoring_complete']


    def test_slot_identity_and_complete_coverage_required(self):
        with self.assertRaises(ValueError):
            c.summarize('ACDE', 'replace_only', [row(0)], 1.0, 2)
        with self.assertRaises(ValueError):
            c.summarize('ACDE', 'replace_only', [row(0), row(0)], 1.0, 2)


    def test_generation_error_remains_failure_even_if_text_and_score_exist(self):
        got = c.summarize('ACDE', 'replace_only', [row(0, generation_error='transport failed')], 1.0, 1)
        assert got['qualified_oracle_success'] == 0.0
        assert got['invalid_reasons'] == {'generation_error': 1}
        assert got['improved_sequence_uniqueness'] is None


    def test_strict_improvement_no_score_rounding_and_native_novelty_stays_null(self):
        got = c.summarize('ACDE', 'replace_only', [row(0, score=1.0)], 1.0, 1)
        assert got['qualified_oracle_success'] == 0.0
        assert got['native_novelty'] is None

if __name__ == "__main__":
    unittest.main()
