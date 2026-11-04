# EC_number_0025

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0025.txt)

**Task:** `EC_number`  
**Expected answer:** **D** — 1.2.1.101

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MPSHTFNPQAGYDLAVDRNLGLGEIFYNRAQKSHQAIAVCDGGAVLTYGQLHAKAYRLAQELSQWLRLTEKPVGIVVQHGMADVVAQMAVIYAGGSCAPMDPTLPDNQIQGRLKRLDAVCVLTDQANRHRDLGADVLCIDDFDIADLAPEDTLYPVATNLEHCAYLIHTSGTTAEPKAVQIAARSILHVAFYAPLEPVYDTDVVAHANNSSFDVSLFDIWVPLLRGAQIAVINKAVLLDPPMMAREIDRLGITVMATTTAVLNLAAFIYPKAFAKLRLVTIGGEAANVAAIRIILKNGPPAMLFNAYGPTECCVFCLAHQITPADVEHGSIGVSIGKPVGRTITYIAGDEGGESDQGELWIGGPGVSPGYFRQPEKNLAAFSDLGEAMTSLENPVRFYRTGDIVRRRPNGALEYVGRRDHQVKVRGFRIELEAVEAGLLKTGLFSDAVAMRIEMPQNGAGSILAAYVVPTDVSKPPTMDEALESAKSILPHYMVPQLELVPRLPLNRHLKVDRKQLAELFGRRWEDVSPAQPENASQDVRSALVSLWATVLASPLSTYGDDDDFLHLGGTSLQAAMLINQIRHKFDIEVSLLTLYDNTTLGALTSIIKQRLSGQSETLHNEKDSWVADSEIADDLSCPLDRPIDWCRDTEGRVFLTGGTGFVGAFLLADLLHMPQTSQVRCLVRATDAAVGQERLRAALDKYGLWEDGFADKLVAIAGLLEDDYLGMGREQFEEAASWASVVFHLGARVNYAQPYSLHRASNTLGTRNMVRFACAGRTKAIHYVSSIGCFGPTGSILGTTSVREDEPLLPHITALPYDHGYAQSQWVADALLRRLMDRGFPIAIYRPGFIVGHSQTGACNPDDFLSRLIDACREIGCYPQLPNQRKEFVPVDYVNAAILHIAASPASLGHAYHIVPPTRAVSIDMDNSMALVDRAGNSPMRPVSYKEWVERLAATSPKRLLPLQPMLAERVKDGLTRWELYENMPVYETTNTARALQNYPGGLQFPVLDTSLMKRYLDFLEAKG

[Multiple Choices]
A. 1.1.1.336
B. 2.7.8.43
C. 4.1.1.128
D. 1.2.1.101
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence.. The inputs provided by the user for this task include:

* Protein Sequence: The amino acid sequence of the protein.
* Multiple Choices: Candidate answers for the protein-related question.

Please think step-by-step about this problem:
1. Analyze the protein sequence carefully.
2. Consider the biological context and function.
3. Evaluate each multiple-choice option.
4. Provide your reasoning process.
5. Finally, give your answer.

Provide your response in the following format:
1. reasoning: [Your detailed reasoning here]
2. answer: Your final answer, which should be "A", "B", "C" or "D".
```

</details>

## Reviewer assessments

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The matched UniProt record assigns EC 1.2.1.101 and gives the corresponding tyrosinal-to-tyrosine reaction. The annotation cites experimental evidence (ECO:0000269); this supports D, though the cited paper was not independently reviewed here.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 1024-aa sequence has the scale and apparent multidomain character expected of a noncanonical NRPS, with adenylation-like and NAD(P)-dependent reductive features. Transferable knowledge of such enzymes makes an amino-acid-related redox/activation function—and thus D, an EC 1.2 oxidoreductase—more plausible than the offered phosphotransferase, decarboxylase, or different oxidoreductase choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family/domain-level sequence inference meaningfully favors D among these choices. It does not establish the exact substrate or the full EC suffix from first principles, but the alternatives do not require that finer discrimination to select the best-supported option.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered option is comparably supported by the sequence-level family/domain inference.


### Important caveats

- The experimental support is reported through a cited UniProt annotation; the primary study was not independently assessed.
- The exact reaction and EC suffix are more specific than what the sequence-only inference alone establishes.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 1024-aa sequence has the scale and apparent multidomain character expected of a noncanonical NRPS, with adenylation-like and NAD(P)-dependent reductive features. Transferable knowledge of such enzymes makes an amino-acid-related redox/activation function—and thus D, an EC 1.2 oxidoreductase—more plausible than the offered phosphotransferase, decarboxylase, or different oxidoreductase choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family/domain-level sequence inference meaningfully favors D among these choices. It does not establish the exact substrate or the full EC suffix from first principles, but the alternatives do not require that finer discrimination to select the best-supported option."
  },
  "case_id": "EC_number_0025",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The matched UniProt record assigns EC 1.2.1.101 and gives the corresponding tyrosinal-to-tyrosine reaction. The annotation cites experimental evidence (ECO:0000269); this supports D, though the cited paper was not independently reviewed here."
  },
  "important_caveats": [
    "The experimental support is reported through a cited UniProt annotation; the primary study was not independently assessed.",
    "The exact reaction and EC suffix are more specific than what the sequence-only inference alone establishes."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option is comparably supported by the sequence-level family/domain inference."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0025",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched UniProt record assigns EC 1.2.1.101 and gives the corresponding tyrosinal-to-tyrosine reaction. The annotation cites experimental evidence (ECO:0000269); this supports D, though the cited paper was not independently reviewed here.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 1024-aa sequence has the scale and apparent multidomain character expected of a noncanonical NRPS, with adenylation-like and NAD(P)-dependent reductive features. Transferable knowledge of such enzymes makes an amino-acid-related redox/activation function—and thus D, an EC 1.2 oxidoreductase—more plausible than the offered phosphotransferase, decarboxylase, or different oxidoreductase choices.",
    "missing_item_specific_fact": "",
    "reason": "Family/domain-level sequence inference meaningfully favors D among these choices. It does not establish the exact substrate or the full EC suffix from first principles, but the alternatives do not require that finer discrimination to select the best-supported option."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option is comparably supported by the sequence-level family/domain inference."
  },
  "important_caveats": [
    "The experimental support is reported through a cited UniProt annotation; the primary study was not independently assessed.",
    "The exact reaction and EC suffix are more specific than what the sequence-only inference alone establishes."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A7T8F1L4 (FRZA_CLASX) annotates EC 1.2.1.101 with experimental evidence (ECO:0000269, PubMed:33372776). The catalytic reaction L-tyrosinal + AMP + diphosphate + NADP(+) = L-tyrosine + ATP + NADPH + H(+) is confirmed. The benchmark sequence (1024 aa) matches the source sequence exactly. The annotation is based on a published experimental study (Zhang et al., JACS 2021), not merely computational prediction.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a clear Rossmann-fold NAD(P)-binding motif (GGTGFVGAFLL) and a catalytic Cys in the canonical aldehyde-dehydrogenase context (GGSCAPMDPT, the 'Cys-Gly' pair). These two features together are hallmarks of the aldehyde dehydrogenase superfamily (EC 1.2.1), distinguishing it from alcohol dehydrogenases (EC 1.1.1, which typically use a catalytic Zn2+ rather than a Cys thiohemiacetal mechanism) and from transferases (EC 2.x) or lyases (EC 4.x) that lack Rossmann folds entirely. Additionally, the C-terminal region displays NRPS adenylation-domain motifs (GHSQTG, GCFGPTGS, GHSQTGACNPDD) characteristic of non-canonical NRPS enzymes, consistent with an amino-acid-activating dehydrogenase. Among the four options, only D (1.2.1.101) falls in the 1.2.1 subclass; A (1.1.1.336) requires a Zn-dependent alcohol-oxidation mechanism incompatible with the observed catalytic Cys; B (2.7.8.43) and C (4.1.1.128) belong to entirely different EC top-level classes (transferase, lyase) and would not present a Rossmann fold or aldehyde-dehydrogenase catalytic Cys. Thus family-level knowledge of aldehyde dehydrogenases and NRPS enzymes meaningfully eliminates A, B, and C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The four options span three different EC top-level classes (1, 2, 4) and two different EC second-level classes within EC 1 (1.1 vs 1.2). Transferable knowledge of the aldehyde dehydrogenase catalytic Cys mechanism, Rossmann-fold NADP+ binding, and NRPS adenylation-domain motifs is sufficient to select D over the other three options without needing to recall this protein's specific database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options occupy distinct EC classes and subclasses. The catalytic Cys in a GSC context and the Rossmann-fold motif cleanly separate EC 1.2.1 from EC 1.1.1, EC 2.7.8, and EC 4.1.1. No two options are mechanistically interchangeable.


### Important caveats

- The 4th digit (101) specifies the L-tyrosinal/L-tyrosine substrate; this level of precision is not independently derivable from sequence alone, but the question only requires selecting among four options where only one falls in the 1.2.1 subclass.
- The protein is a non-canonical NRPS with a fused adenylation-like domain and aldehyde dehydrogenase domain; recognizing the hybrid architecture relies on familiarity with natural-product biosynthesis enzymes.
- The UniProt annotation carries experimental evidence (ECO:0000269) from a 2021 JACS publication, lending strong support to the key.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a clear Rossmann-fold NAD(P)-binding motif (GGTGFVGAFLL) and a catalytic Cys in the canonical aldehyde-dehydrogenase context (GGSCAPMDPT, the 'Cys-Gly' pair). These two features together are hallmarks of the aldehyde dehydrogenase superfamily (EC 1.2.1), distinguishing it from alcohol dehydrogenases (EC 1.1.1, which typically use a catalytic Zn2+ rather than a Cys thiohemiacetal mechanism) and from transferases (EC 2.x) or lyases (EC 4.x) that lack Rossmann folds entirely. Additionally, the C-terminal region displays NRPS adenylation-domain motifs (GHSQTG, GCFGPTGS, GHSQTGACNPDD) characteristic of non-canonical NRPS enzymes, consistent with an amino-acid-activating dehydrogenase. Among the four options, only D (1.2.1.101) falls in the 1.2.1 subclass; A (1.1.1.336) requires a Zn-dependent alcohol-oxidation mechanism incompatible with the observed catalytic Cys; B (2.7.8.43) and C (4.1.1.128) belong to entirely different EC top-level classes (transferase, lyase) and would not present a Rossmann fold or aldehyde-dehydrogenase catalytic Cys. Thus family-level knowledge of aldehyde dehydrogenases and NRPS enzymes meaningfully eliminates A, B, and C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The four options span three different EC top-level classes (1, 2, 4) and two different EC second-level classes within EC 1 (1.1 vs 1.2). Transferable knowledge of the aldehyde dehydrogenase catalytic Cys mechanism, Rossmann-fold NADP+ binding, and NRPS adenylation-domain motifs is sufficient to select D over the other three options without needing to recall this protein's specific database record."
  },
  "case_id": "EC_number_0025",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A7T8F1L4 (FRZA_CLASX) annotates EC 1.2.1.101 with experimental evidence (ECO:0000269, PubMed:33372776). The catalytic reaction L-tyrosinal + AMP + diphosphate + NADP(+) = L-tyrosine + ATP + NADPH + H(+) is confirmed. The benchmark sequence (1024 aa) matches the source sequence exactly. The annotation is based on a published experimental study (Zhang et al., JACS 2021), not merely computational prediction."
  },
  "important_caveats": [
    "The 4th digit (101) specifies the L-tyrosinal/L-tyrosine substrate; this level of precision is not independently derivable from sequence alone, but the question only requires selecting among four options where only one falls in the 1.2.1 subclass.",
    "The protein is a non-canonical NRPS with a fused adenylation-like domain and aldehyde dehydrogenase domain; recognizing the hybrid architecture relies on familiarity with natural-product biosynthesis enzymes.",
    "The UniProt annotation carries experimental evidence (ECO:0000269) from a 2021 JACS publication, lending strong support to the key."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options occupy distinct EC classes and subclasses. The catalytic Cys in a GSC context and the Rossmann-fold motif cleanly separate EC 1.2.1 from EC 1.1.1, EC 2.7.8, and EC 4.1.1. No two options are mechanistically interchangeable."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0025",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A7T8F1L4 (FRZA_CLASX) annotates EC 1.2.1.101 with experimental evidence (ECO:0000269, PubMed:33372776). The catalytic reaction L-tyrosinal + AMP + diphosphate + NADP(+) = L-tyrosine + ATP + NADPH + H(+) is confirmed. The benchmark sequence (1024 aa) matches the source sequence exactly. The annotation is based on a published experimental study (Zhang et al., JACS 2021), not merely computational prediction.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a clear Rossmann-fold NAD(P)-binding motif (GGTGFVGAFLL) and a catalytic Cys in the canonical aldehyde-dehydrogenase context (GGSCAPMDPT, the 'Cys-Gly' pair). These two features together are hallmarks of the aldehyde dehydrogenase superfamily (EC 1.2.1), distinguishing it from alcohol dehydrogenases (EC 1.1.1, which typically use a catalytic Zn2+ rather than a Cys thiohemiacetal mechanism) and from transferases (EC 2.x) or lyases (EC 4.x) that lack Rossmann folds entirely. Additionally, the C-terminal region displays NRPS adenylation-domain motifs (GHSQTG, GCFGPTGS, GHSQTGACNPDD) characteristic of non-canonical NRPS enzymes, consistent with an amino-acid-activating dehydrogenase. Among the four options, only D (1.2.1.101) falls in the 1.2.1 subclass; A (1.1.1.336) requires a Zn-dependent alcohol-oxidation mechanism incompatible with the observed catalytic Cys; B (2.7.8.43) and C (4.1.1.128) belong to entirely different EC top-level classes (transferase, lyase) and would not present a Rossmann fold or aldehyde-dehydrogenase catalytic Cys. Thus family-level knowledge of aldehyde dehydrogenases and NRPS enzymes meaningfully eliminates A, B, and C.",
    "missing_item_specific_fact": "",
    "reason": "The four options span three different EC top-level classes (1, 2, 4) and two different EC second-level classes within EC 1 (1.1 vs 1.2). Transferable knowledge of the aldehyde dehydrogenase catalytic Cys mechanism, Rossmann-fold NADP+ binding, and NRPS adenylation-domain motifs is sufficient to select D over the other three options without needing to recall this protein's specific database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options occupy distinct EC classes and subclasses. The catalytic Cys in a GSC context and the Rossmann-fold motif cleanly separate EC 1.2.1 from EC 1.1.1, EC 2.7.8, and EC 4.1.1. No two options are mechanistically interchangeable."
  },
  "important_caveats": [
    "The 4th digit (101) specifies the L-tyrosinal/L-tyrosine substrate; this level of precision is not independently derivable from sequence alone, but the question only requires selecting among four options where only one falls in the 1.2.1 subclass.",
    "The protein is a non-canonical NRPS with a fused adenylation-like domain and aldehyde dehydrogenase domain; recognizing the hybrid architecture relies on familiarity with natural-product biosynthesis enzymes.",
    "The UniProt annotation carries experimental evidence (ECO:0000269) from a 2021 JACS publication, lending strong support to the key."
  ]
}
```

</details>

## Complete reviewer-only evidence and qualifications

These source excerpts were available to the reviewers. They were not included in the original benchmark-solving input.

**Source applicability:**

```json
{
  "actual_author_source_snapshot": "unknown",
  "benchmark_sequence_length": 1024,
  "benchmark_sequence_sha256": "78903b102e2259d837b80ac44bcf15e6ae1534722167cff1a23d530bb0db74e0",
  "current_entry_audit": {
    "entryVersion": 20,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2021-06-02",
    "sequenceVersion": 1
  },
  "current_record_sha256": "4cf4e4af61e7d91300bdd1c46dcd31d2e7126d4631315e40df3061127135d0fb",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 1024,
  "current_source_sequence_sha256": "78903b102e2259d837b80ac44bcf15e6ae1534722167cff1a23d530bb0db74e0",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 18,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A7T8F1L4",
  "selected_historical_entry_version": 18,
  "selected_historical_record_sha256": "dc244e3d4206d7a97707ec88200b44521e519f3504ebcf6f0cd7d074b3fd2c4b",
  "selected_historical_source_sequence_length": 1024,
  "selected_historical_source_sequence_sha256": "78903b102e2259d837b80ac44bcf15e6ae1534722167cff1a23d530bb0db74e0",
  "selected_historical_version": {
    "accession": "A0A7T8F1L4",
    "database": "Swiss-Prot",
    "entryVersion": 18,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "FRZA_CLASX",
    "sequenceVersion": 1
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1L4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A7T8F1L4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:25:48.509506+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4cf4e4af61e7d91300bdd1c46dcd31d2e7126d4631315e40df3061127135d0fb",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1L4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1L4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":20,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2021-06-02\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:25:48.509506+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4cf4e4af61e7d91300bdd1c46dcd31d2e7126d4631315e40df3061127135d0fb",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1L4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1L4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Hypocreomycetidae\",\"Hypocreales\",\"Hypocreaceae\",\"Cladobotryum\"],\"scientificName\":\"Cladobotryum sp\",\"taxonId\":2040732}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:25:48.509506+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4cf4e4af61e7d91300bdd1c46dcd31d2e7126d4631315e40df3061127135d0fb",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1L4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1L4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"FR901483 biosynthesis cluster protein A\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"1.2.1.101\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"Non-canonical nonribosomal peptide synthetase FrzA\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:25:48.509506+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4cf4e4af61e7d91300bdd1c46dcd31d2e7126d4631315e40df3061127135d0fb",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1L4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1L4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"right-to-left\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:57414\"}}],\"reaction\":{\"ecNumber\":\"1.2.1.101\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"name\":\"L-tyrosinal + AMP + diphosphate + NADP(+) = L-tyrosine + ATP + NADPH + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:57412\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33019\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57783\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58315\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:141668\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456215\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:25:48.509506+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4cf4e4af61e7d91300bdd1c46dcd31d2e7126d4631315e40df3061127135d0fb",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1L4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1L4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhang Z.\",\"Tamura Y.\",\"Tang M.\",\"Qiao T.\",\"Sato M.\",\"Otsu Y.\",\"Sasamura S.\",\"Taniguchi M.\",\"Watanabe K.\",\"Tang Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33372776\"},{\"database\":\"DOI\",\"id\":\"10.1021/jacs.0c12352\"}],\"citationType\":\"journal article\",\"firstPage\":\"132\",\"id\":\"33372776\",\"journal\":\"J. Am. Chem. Soc.\",\"lastPage\":\"136\",\"publicationDate\":\"2021\",\"title\":\"Biosynthesis of the Immunosuppressant (-)-FR901483.\",\"volume\":\"143\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"11231\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:25:48.509506+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4cf4e4af61e7d91300bdd1c46dcd31d2e7126d4631315e40df3061127135d0fb",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1L4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1L4?format=txt&versions=18)

```json
{
  "entry_version": 18,
  "evidence_id": "H1",
  "excerpt": "ID   FRZA_CLASX              Reviewed;        1024 AA.\nAC   A0A7T8F1L4;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   02-JUN-2021, sequence version 1.\nDT   28-JAN-2026, entry version 18.\nDE   RecName: Full=Non-canonical nonribosomal peptide synthetase FrzA {ECO:0000303|PubMed:33372776};\nDE            EC=1.2.1.101 {ECO:0000269|PubMed:33372776};\nDE   AltName: Full=FR901483 biosynthesis cluster protein A {ECO:0000303|PubMed:33372776};\nGN   Name=FrzA {ECO:0000303|PubMed:33372776};\nOS   Cladobotryum sp.\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Hypocreomycetidae; Hypocreales; Hypocreaceae; Cladobotryum.\nOX   NCBI_TaxID=2040732;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:50.375049+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dc244e3d4206d7a97707ec88200b44521e519f3504ebcf6f0cd7d074b3fd2c4b",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1L4?format=txt&versions=18"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1L4?format=txt&versions=18)

```json
{
  "entry_version": 18,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Non-canonical nonribosomal peptide synthetase FrzA {ECO:0000303|PubMed:33372776};\nDE            EC=1.2.1.101 {ECO:0000269|PubMed:33372776};\nDE   AltName: Full=FR901483 biosynthesis cluster protein A {ECO:0000303|PubMed:33372776};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:50.375049+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dc244e3d4206d7a97707ec88200b44521e519f3504ebcf6f0cd7d074b3fd2c4b",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1L4?format=txt&versions=18"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1L4?format=txt&versions=18)

```json
{
  "entry_version": 18,
  "evidence_id": "H3",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, CATALYTIC ACTIVITY, AND\nRP   PATHWAY.\nRC   STRAIN=11231;\nRX   PubMed=33372776; DOI=10.1021/jacs.0c12352;\nRA   Zhang Z., Tamura Y., Tang M., Qiao T., Sato M., Otsu Y., Sasamura S.,\nRA   Taniguchi M., Watanabe K., Tang Y.;\nRT   \"Biosynthesis of the Immunosuppressant (-)-FR901483.\";\nRL   J. Am. Chem. Soc. 143:132-136(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:50.375049+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 14-22",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dc244e3d4206d7a97707ec88200b44521e519f3504ebcf6f0cd7d074b3fd2c4b",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1L4?format=txt&versions=18"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1L4?format=txt&versions=18)

```json
{
  "entry_version": 18,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-tyrosinal + AMP + diphosphate + NADP(+) = L-tyrosine + ATP +\nCC         NADPH + H(+); Xref=Rhea:RHEA:57412, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:30616, ChEBI:CHEBI:33019, ChEBI:CHEBI:57783,\nCC         ChEBI:CHEBI:58315, ChEBI:CHEBI:58349, ChEBI:CHEBI:141668,\nCC         ChEBI:CHEBI:456215; EC=1.2.1.101;\nCC         Evidence={ECO:0000269|PubMed:33372776};\nCC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:57414;\nCC         Evidence={ECO:0000269|PubMed:33372776};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:50.375049+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 53-61",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dc244e3d4206d7a97707ec88200b44521e519f3504ebcf6f0cd7d074b3fd2c4b",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1L4?format=txt&versions=18"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 25. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
