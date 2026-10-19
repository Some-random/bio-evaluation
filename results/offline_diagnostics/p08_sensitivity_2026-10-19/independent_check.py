"""Second implementation: counting ranks and direct pair-distance summation."""
from collections import Counter
import hashlib
import json
import math
from pathlib import Path
import statistics
import sys


def counting_ranks(values):
    counts = Counter(values)
    ranks = {}
    seen = 0
    for value in sorted(counts):
        ranks[value] = seen + (counts[value]+1)/2
        seen += counts[value]
    return [ranks[value] for value in values]


def verify(source, reference):
    rows = json.loads(source.read_bytes())
    expected = json.loads(reference.read_text())
    valid = [r for r in rows if r['prediction'] is not None]
    n, k = len(rows), len(valid)
    rank_x = counting_ranks([r['prediction'] for r in valid])
    rank_y_valid = counting_ranks([r['target'] for r in valid])
    rho = statistics.correlation(rank_x, rank_y_valid)
    full_b = [v-(n+1)/2 for v in counting_ranks([r['target'] for r in rows])]
    bv = [v for v,r in zip(full_b,rows) if r['prediction'] is not None]
    bm = [v for v,r in zip(full_b,rows) if r['prediction'] is None]
    base = sum((a-(k+1)/2)*b for a,b in zip(rank_x,bv))
    m=n-k
    numerator = base + (m*sum(abs(b) for b in bv)+(n-1)*sum(abs(b) for b in bm))/2
    pair_numerator = base + sum(abs(a-b) for a in bv for b in bm)/2
    pair_numerator += sum(abs(a-b) for i,a in enumerate(bm) for b in bm[:i])/2
    denominator = math.sqrt(sum(b*b for b in full_b)*sum((i-(n+1)/2)**2 for i in range(1,n+1)))
    checks = {'parsed_only_rho':rho,'rectangle_bound':numerator/denominator,
              'pairwise_bound':pair_numerator/denominator}
    comparisons = [expected['parsed_only_spearman_recomputed'],
                   expected['bounds']['rectangle']['correlation_upper'],
                   expected['bounds']['pairwise']['correlation_upper']]
    assert all(abs(a-b)<1e-14 for a,b in zip(checks.values(),comparisons))
    return {'algorithm':'counting ranks + statistics.correlation + direct pair enumeration',
            'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
            'independent_values':checks,'all_match_within':1e-14,'passed':True}


if __name__=='__main__':
    source,reference=map(Path,sys.argv[1:3]);result=verify(source,reference)
    output=Path(__file__).with_name('independent_validation.json')
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
