import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from score_vqamed2019_native import normalize, reference_alternatives


class NativeReferenceContractTests(unittest.TestCase):
    def test_alternatives_and_optional_parts_from_organizer_contract(self):
        answers = reference_alternatives("an (illustrative) finding#other answer")
        self.assertEqual(answers, {"an finding", "an illustrative finding", "other answer"})

    def test_strictness_does_not_credit_substring_or_reasoning(self):
        answers = reference_alternatives("yes")
        self.assertNotIn(normalize("yes or no"), answers)
        self.assertNotIn(normalize("My explanation suggests yes"), answers)
        self.assertNotIn(normalize(""), answers)

    def test_native_punctuation_case_and_word_spacing_only(self):
        self.assertEqual(normalize(" AXIAL,  PLANE! "), "axial plane")
        self.assertNotEqual(normalize("a plane"), normalize("plane"))

    def test_nested_optional_syntax_requires_explicit_review(self):
        with self.assertRaises(ValueError):
            reference_alternatives("a (nested (optional)) answer")


if __name__ == "__main__":
    unittest.main()
