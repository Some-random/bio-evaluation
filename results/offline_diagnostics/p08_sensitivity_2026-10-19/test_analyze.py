"""Mathematical and format checks using synthetic values, never test outcomes."""
import itertools
import math
import random
import unittest

from analyze import absolute_cross_sum, finite_imputation_bounds, midranks, spearman
from format_rules import classify, native_number


class SyntheticChecks(unittest.TestCase):
    def test_native_number_contract(self):
        for text, expected in [('Answer: -1.5',-1.5),(' 2e-3 ',.002),('+0',0),('.5',.5)]:
            self.assertEqual(native_number(text),expected)
        for text in ['−1.5','**1.2**','1.2 or 1.3','nan','1e999','about 2',None]:
            self.assertIsNone(native_number(text))

    def test_reference_free_categories(self):
        for text, finish, category in [
            ('−2.34','stop','unicode_minus_only_scalar'),
            ('**-2.3**','stop','whole_final_scalar_wrapper'),
            ('I cannot calculate this; a guess is 0.0.','stop','abstention_or_insufficient_information'),
            ('Approximately 0.2','stop','qualified_estimate_or_uncertainty'),
            ('','length','truncated_invalid'),('', 'stop','empty_final'),
            ('Answer: 1.4','stop','native_scalar')]:
            self.assertEqual(classify(text,finish)['category'],category)

    def test_midrank_ties_and_monotone_direction(self):
        self.assertEqual(midranks([3,1,1,2]),[4,1.5,1.5,3])
        self.assertAlmostEqual(spearman([3,1,1,2],[30,10,10,20]),1)
        self.assertAlmostEqual(spearman([3,1,1,2],[-30,-10,-10,-20]),-1)
        self.assertIsNone(spearman([1,1],[0,1]))

    def test_cross_sum_matches_direct_pair_enumeration(self):
        a,b=[1,1,4,9],[-2,1,5]
        self.assertEqual(absolute_cross_sum(a,b),sum(abs(x-y) for x in a for y in b))

    def test_midrank_pair_covariance_identity_with_ties(self):
        rng=random.Random(19)
        for _ in range(100):
            x=[rng.randrange(4) for _ in range(8)]
            y=[rng.randrange(5) for _ in range(8)]
            a,b=midranks(x),midranks(y);mean=(len(x)+1)/2
            dot=sum((p-mean)*(q-mean) for p,q in zip(a,b))
            pair=sum(((x[i]>x[j])-(x[i]<x[j]))*(b[i]-b[j])/2
                     for i in range(len(x)) for j in range(i))
            self.assertEqual(dot,pair)

    def test_universal_bounds_exhaustive_completions_including_ties(self):
        rng=random.Random(29);checked=0
        for _ in range(100):
            n=6;pred=[rng.randrange(3) for _ in range(4)]+[None,None]
            if len(set(pred[:4]))<2:continue
            targets=[rng.randrange(4) for _ in range(n)]
            if len(set(targets))<2:continue
            bounds=finite_imputation_bounds(pred,targets)
            # Covers below/above accepted values, intervening positions and ties.
            for completion in itertools.product([-1,0,.5,1,1.5,2,3],repeat=2):
                corr=spearman(pred[:4]+list(completion),targets)
                for method in ['rectangle','pairwise']:
                    self.assertLessEqual(corr,bounds[method]['correlation_upper']+1e-12)
                checked+=1
        self.assertGreater(checked,4000)

    def test_nontrivial_negative_bounds_for_every_completion(self):
        pred=[7,6,5,4,3,2,1,None]
        targets=list(range(8))
        bounds=finite_imputation_bounds(pred,targets)
        for method in ['rectangle','pairwise']:
            self.assertLess(bounds[method]['correlation_upper'],0)
        for value in [-1,0,.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,8]:
            correlation=spearman(pred[:-1]+[value],targets)
            for method in ['rectangle','pairwise']:
                self.assertLessEqual(correlation,bounds[method]['correlation_upper']+1e-12)

    def test_positive_numerator_does_not_misuse_denominator_upper(self):
        bounds=finite_imputation_bounds([0,1,None],[0,1,2])
        self.assertEqual(bounds['rectangle']['correlation_upper'],1)

    def test_no_missing_agrees_with_exact_spearman_when_untied(self):
        p=[4,3,2,1];y=[1,2,3,4]
        bounds=finite_imputation_bounds(p,y)
        self.assertEqual(bounds['rectangle']['correlation_upper'],spearman(p,y))
        self.assertEqual(bounds['pairwise']['correlation_upper'],spearman(p,y))


if __name__=='__main__':unittest.main()
