# EC_number_0091

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0091.txt)

**Task:** `EC_number`  
**Expected answer:** **A** — 2.4.1.392

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MNRSDAYGYFRNQGREYVITTPRTPARWFNYLFNDTYYTEISQTGQGDSVAFRPHNRTLTRGFRYFYLKDLETGGTWSPLYQPLKTEPEAYECIHSLGTTEIRSVSQEIASSIHVFVPRAGQQEIWTVTLTNTGVKPRSLSLFTAFSLENGGVMGSKCQFDQESQILSSYSFPYHVTYGQKAGCDDHTNVVYVYPDYPADSYDCSQRAFFGGDDIYELPAAVQKGRCSGGQAEAENPLGALQQTITLEPGEQAVRHFVVGCASSLEEIRSSKAELAAKGYAVLLQETEDYWEGITGMFRVETPDDDVNAFMNIWLKKQIVMQTRTNRMSSYCPVRNQLQDALGYALVDPAGAAEYMISVLQGQERSGFIQQWIMTDGSPPKNLCLLKHTDGPVWLIICITALLNQCGDTELLQRQVGFKGSSDSATIYQHLLLAADYMAGETGAHGLCLMGDGDWNDPINGPGRLGRGESAWNTMALVYAIQALIPFCEQLGDTENAEQLNTVARRLADAVNRICWDGGWYVAGFDDDGTPFGTAQDEEGKLFLNTQTWAIMSGIASGERLDQCLAAIDSLDTPFGPRLLEPPFSGWNPKWGRISLKLAGTTENGSVYCHASMFKAFADCIAGRGSEAWQTISRTLPTNPDNPPGQNGQVPIFVPNYYFGLADSPNFGKSSHHVSTGTVGWMLWTTLEYALGIRATANGLKIDPCIPADWPEYTVERKYRSASYRIHVLNPSGISRGTVKVTVDGEAWMAAALPYEAGREYQVTVQLEQ

[Multiple Choices]
A. 2.4.1.392
B. 2.4.1.259
C. 2.1.1.392
D. 1.2.1.46
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

> The sequence-matched UniProt record assigns EC 2.4.1.392 and links the catalytic activity to experimental evidence (ECO:0000269). The archived record also contains this assignment before the historical cutoff. This supports the key, while not independently validating the primary experiment.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with a large glycoside phosphorylase: transferable family-level knowledge can support a phosphorylase-type reaction and makes the two 2.4.1 choices more plausible than the methyltransferase or oxidoreductase choices. That broad inference does not establish the substrate specificity needed to distinguish EC 2.4.1.392 from EC 2.4.1.259.


**Missing item-specific fact**

> The exact enzyme's experimentally established substrate specificity or an independently established sequence-to-subfamily assignment that distinguishes the two 2.4.1 options.


**Reason**

> The sequence and general family knowledge provide a meaningful broad functional inference, but the offered choices include two glycosyltransferase-class EC numbers. The exact catalytic specificity needed to choose between them is not established by the original input alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> From the sequence and transferable family-level inference alone, both 2.4.1 choices remain plausible; the choices do not provide a basis to resolve their substrate-specific distinction.


### Important caveats

- Reviewer-only annotation supports the answer key but was not part of the original model input.
- The database annotation cites experimental evidence, but the primary paper was not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a large glycoside phosphorylase: transferable family-level knowledge can support a phosphorylase-type reaction and makes the two 2.4.1 choices more plausible than the methyltransferase or oxidoreductase choices. That broad inference does not establish the substrate specificity needed to distinguish EC 2.4.1.392 from EC 2.4.1.259.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact enzyme's experimentally established substrate specificity or an independently established sequence-to-subfamily assignment that distinguishes the two 2.4.1 options.",
    "reason": "The sequence and general family knowledge provide a meaningful broad functional inference, but the offered choices include two glycosyltransferase-class EC numbers. The exact catalytic specificity needed to choose between them is not established by the original input alone."
  },
  "case_id": "EC_number_0091",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 2.4.1.392 and links the catalytic activity to experimental evidence (ECO:0000269). The archived record also contains this assignment before the historical cutoff. This supports the key, while not independently validating the primary experiment."
  },
  "important_caveats": [
    "Reviewer-only annotation supports the answer key but was not part of the original model input.",
    "The database annotation cites experimental evidence, but the primary paper was not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "From the sequence and transferable family-level inference alone, both 2.4.1 choices remain plausible; the choices do not provide a basis to resolve their substrate-specific distinction."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0091",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 2.4.1.392 and links the catalytic activity to experimental evidence (ECO:0000269). The archived record also contains this assignment before the historical cutoff. This supports the key, while not independently validating the primary experiment.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with a large glycoside phosphorylase: transferable family-level knowledge can support a phosphorylase-type reaction and makes the two 2.4.1 choices more plausible than the methyltransferase or oxidoreductase choices. That broad inference does not establish the substrate specificity needed to distinguish EC 2.4.1.392 from EC 2.4.1.259.",
    "missing_item_specific_fact": "The exact enzyme's experimentally established substrate specificity or an independently established sequence-to-subfamily assignment that distinguishes the two 2.4.1 options.",
    "reason": "The sequence and general family knowledge provide a meaningful broad functional inference, but the offered choices include two glycosyltransferase-class EC numbers. The exact catalytic specificity needed to choose between them is not established by the original input alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "From the sequence and transferable family-level inference alone, both 2.4.1 choices remain plausible; the choices do not provide a basis to resolve their substrate-specific distinction."
  },
  "important_caveats": [
    "Reviewer-only annotation supports the answer key but was not part of the original model input.",
    "The database annotation cites experimental evidence, but the primary paper was not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The expected answer EC 2.4.1.392 (3-O-beta-D-glucopyranosyl-beta-D-glucuronide phosphorylase) is supported by experimental evidence (ECO:0000269, PubMed:35947916) in the UniProt annotation for the matched sequence (A0A089MMR2, Paenibacillus borealis). The catalytic activity is phosphorolysis of 3-O-beta-D-glucosyl-D-glucuronate by phosphate, confirmed by two Rhea reactions (RHEA:78711 and RHEA:78699). The evidence code ECO:0000269 indicates direct experimental determination.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A knowledgeable model can eliminate C (EC 2.1.1.392, a methyltransferase) and D (EC 1.2.1.46, an oxidoreductase) by recognizing the protein as belonging to the GH94 glycoside phosphorylase family, which is a transferase (EC 2) acting on glycosyl groups (EC 2.4), not a one-carbon transferase (EC 2.1) or an oxidoreductase (EC 1). However, distinguishing A (2.4.1.392) from B (2.4.1.259) requires knowing the exact 4th-digit substrate specificity. Both are 2.4.1.x hexosyltransferases/phosphorylases. EC 2.4.1.392 was assigned in 2022 specifically for glucuronide-containing substrates, a very recently characterized and narrow activity. No well-established sequence signature in GH94 family members reliably predicts glucuronide specificity over other sugar substrates at the level of the 4th EC digit. The active-site residues accommodating the glucuronic acid carboxylate are not a conserved, transferable motif across GH94 that would allow a model to predict this specific substrate without prior knowledge of this enzyme's experimental characterization.


**Missing item-specific fact**

> The experimentally determined substrate specificity of this exact protein (3-O-beta-D-glucopyranosyl-beta-D-glucuronide phosphorylase, EC 2.4.1.392) as characterized in PubMed:35947916 (2022). The 4th EC digit distinguishing 392 from 259 encodes a specific substrate reaction that is not predictable from GH94 family membership or general sequence features.


**Reason**

> While the first three EC digits (2.4.1) can be inferred from family-level knowledge (GH94 glycoside phosphorylase → transferase, glycosyltransferase, hexosyltransferase), the 4th digit (392 vs 259) encodes a specific substrate reaction determined experimentally in 2022. No transferable sequence feature or family-level pattern reliably distinguishes glucuronide specificity (392) from whatever substrate EC 2.4.1.259 represents. The A vs B distinction requires knowledge of this protein's specific experimental characterization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> EC 2.4.1.392 is unambiguously supported by experimental evidence for this sequence. EC 2.4.1.259 is a different reaction. Options C and D are clearly wrong enzyme classes. No genuine ambiguity exists in the correct answer.


### Important caveats

- The 4th EC digit distinction (392 vs 259) is the critical challenge; first three digits are inferable from family knowledge.
- EC 2.4.1.392 was assigned in 2022 (PubMed:35947916), making it a very recent annotation that may not be well-represented in training data.
- The reviewer-only evidence confirms the sequence matches A0A089MMR2 (Paenibacillus borealis, 769 aa) with experimental evidence code ECO:0000269.
- The identity of EC 2.4.1.259's specific substrate was not independently verified; it is assumed to be a valid but different hexosyltransferase reaction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can eliminate C (EC 2.1.1.392, a methyltransferase) and D (EC 1.2.1.46, an oxidoreductase) by recognizing the protein as belonging to the GH94 glycoside phosphorylase family, which is a transferase (EC 2) acting on glycosyl groups (EC 2.4), not a one-carbon transferase (EC 2.1) or an oxidoreductase (EC 1). However, distinguishing A (2.4.1.392) from B (2.4.1.259) requires knowing the exact 4th-digit substrate specificity. Both are 2.4.1.x hexosyltransferases/phosphorylases. EC 2.4.1.392 was assigned in 2022 specifically for glucuronide-containing substrates, a very recently characterized and narrow activity. No well-established sequence signature in GH94 family members reliably predicts glucuronide specificity over other sugar substrates at the level of the 4th EC digit. The active-site residues accommodating the glucuronic acid carboxylate are not a conserved, transferable motif across GH94 that would allow a model to predict this specific substrate without prior knowledge of this enzyme's experimental characterization.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The experimentally determined substrate specificity of this exact protein (3-O-beta-D-glucopyranosyl-beta-D-glucuronide phosphorylase, EC 2.4.1.392) as characterized in PubMed:35947916 (2022). The 4th EC digit distinguishing 392 from 259 encodes a specific substrate reaction that is not predictable from GH94 family membership or general sequence features.",
    "reason": "While the first three EC digits (2.4.1) can be inferred from family-level knowledge (GH94 glycoside phosphorylase → transferase, glycosyltransferase, hexosyltransferase), the 4th digit (392 vs 259) encodes a specific substrate reaction determined experimentally in 2022. No transferable sequence feature or family-level pattern reliably distinguishes glucuronide specificity (392) from whatever substrate EC 2.4.1.259 represents. The A vs B distinction requires knowledge of this protein's specific experimental characterization."
  },
  "case_id": "EC_number_0091",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The expected answer EC 2.4.1.392 (3-O-beta-D-glucopyranosyl-beta-D-glucuronide phosphorylase) is supported by experimental evidence (ECO:0000269, PubMed:35947916) in the UniProt annotation for the matched sequence (A0A089MMR2, Paenibacillus borealis). The catalytic activity is phosphorolysis of 3-O-beta-D-glucosyl-D-glucuronate by phosphate, confirmed by two Rhea reactions (RHEA:78711 and RHEA:78699). The evidence code ECO:0000269 indicates direct experimental determination."
  },
  "important_caveats": [
    "The 4th EC digit distinction (392 vs 259) is the critical challenge; first three digits are inferable from family knowledge.",
    "EC 2.4.1.392 was assigned in 2022 (PubMed:35947916), making it a very recent annotation that may not be well-represented in training data.",
    "The reviewer-only evidence confirms the sequence matches A0A089MMR2 (Paenibacillus borealis, 769 aa) with experimental evidence code ECO:0000269.",
    "The identity of EC 2.4.1.259's specific substrate was not independently verified; it is assumed to be a valid but different hexosyltransferase reaction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "EC 2.4.1.392 is unambiguously supported by experimental evidence for this sequence. EC 2.4.1.259 is a different reaction. Options C and D are clearly wrong enzyme classes. No genuine ambiguity exists in the correct answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0091",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The expected answer EC 2.4.1.392 (3-O-beta-D-glucopyranosyl-beta-D-glucuronide phosphorylase) is supported by experimental evidence (ECO:0000269, PubMed:35947916) in the UniProt annotation for the matched sequence (A0A089MMR2, Paenibacillus borealis). The catalytic activity is phosphorolysis of 3-O-beta-D-glucosyl-D-glucuronate by phosphate, confirmed by two Rhea reactions (RHEA:78711 and RHEA:78699). The evidence code ECO:0000269 indicates direct experimental determination.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A knowledgeable model can eliminate C (EC 2.1.1.392, a methyltransferase) and D (EC 1.2.1.46, an oxidoreductase) by recognizing the protein as belonging to the GH94 glycoside phosphorylase family, which is a transferase (EC 2) acting on glycosyl groups (EC 2.4), not a one-carbon transferase (EC 2.1) or an oxidoreductase (EC 1). However, distinguishing A (2.4.1.392) from B (2.4.1.259) requires knowing the exact 4th-digit substrate specificity. Both are 2.4.1.x hexosyltransferases/phosphorylases. EC 2.4.1.392 was assigned in 2022 specifically for glucuronide-containing substrates, a very recently characterized and narrow activity. No well-established sequence signature in GH94 family members reliably predicts glucuronide specificity over other sugar substrates at the level of the 4th EC digit. The active-site residues accommodating the glucuronic acid carboxylate are not a conserved, transferable motif across GH94 that would allow a model to predict this specific substrate without prior knowledge of this enzyme's experimental characterization.",
    "missing_item_specific_fact": "The experimentally determined substrate specificity of this exact protein (3-O-beta-D-glucopyranosyl-beta-D-glucuronide phosphorylase, EC 2.4.1.392) as characterized in PubMed:35947916 (2022). The 4th EC digit distinguishing 392 from 259 encodes a specific substrate reaction that is not predictable from GH94 family membership or general sequence features.",
    "reason": "While the first three EC digits (2.4.1) can be inferred from family-level knowledge (GH94 glycoside phosphorylase → transferase, glycosyltransferase, hexosyltransferase), the 4th digit (392 vs 259) encodes a specific substrate reaction determined experimentally in 2022. No transferable sequence feature or family-level pattern reliably distinguishes glucuronide specificity (392) from whatever substrate EC 2.4.1.259 represents. The A vs B distinction requires knowledge of this protein's specific experimental characterization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "EC 2.4.1.392 is unambiguously supported by experimental evidence for this sequence. EC 2.4.1.259 is a different reaction. Options C and D are clearly wrong enzyme classes. No genuine ambiguity exists in the correct answer."
  },
  "important_caveats": [
    "The 4th EC digit distinction (392 vs 259) is the critical challenge; first three digits are inferable from family knowledge.",
    "EC 2.4.1.392 was assigned in 2022 (PubMed:35947916), making it a very recent annotation that may not be well-represented in training data.",
    "The reviewer-only evidence confirms the sequence matches A0A089MMR2 (Paenibacillus borealis, 769 aa) with experimental evidence code ECO:0000269.",
    "The identity of EC 2.4.1.259's specific substrate was not independently verified; it is assumed to be a valid but different hexosyltransferase reaction."
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
  "benchmark_sequence_length": 769,
  "benchmark_sequence_sha256": "40a4249be74e7afcec5840e732edfa8379c2c5142a4cd41cbb1026a8b9c257e7",
  "current_entry_audit": {
    "entryVersion": 40,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2014-11-26",
    "sequenceVersion": 1
  },
  "current_record_sha256": "9c1354b8bfe0e59449355743dfc7334d0ba6fb5835c3df3570380eed27e91719",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 769,
  "current_source_sequence_sha256": "40a4249be74e7afcec5840e732edfa8379c2c5142a4cd41cbb1026a8b9c257e7",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 38,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A089MMR2",
  "selected_historical_entry_version": 38,
  "selected_historical_record_sha256": "abf8108925ffb7b150428b7a1aa52e27f87e1ad71c64967596cc5207ae75a348",
  "selected_historical_source_sequence_length": 769,
  "selected_historical_source_sequence_sha256": "40a4249be74e7afcec5840e732edfa8379c2c5142a4cd41cbb1026a8b9c257e7",
  "selected_historical_version": {
    "accession": "A0A089MMR2",
    "database": "Swiss-Prot",
    "entryVersion": 38,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "BGBGP_PAEBO",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A089MMR2.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A089MMR2\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:37.192125+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9c1354b8bfe0e59449355743dfc7334d0ba6fb5835c3df3570380eed27e91719",
  "url": "https://rest.uniprot.org/uniprotkb/A0A089MMR2.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A089MMR2.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":40,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2014-11-26\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:37.192125+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9c1354b8bfe0e59449355743dfc7334d0ba6fb5835c3df3570380eed27e91719",
  "url": "https://rest.uniprot.org/uniprotkb/A0A089MMR2.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A089MMR2.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Bacillati\",\"Bacillota\",\"Bacilli\",\"Caryophanales\",\"Paenibacillaceae\",\"Paenibacillus\"],\"scientificName\":\"Paenibacillus borealis\",\"taxonId\":160799}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:37.192125+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9c1354b8bfe0e59449355743dfc7334d0ba6fb5835c3df3570380eed27e91719",
  "url": "https://rest.uniprot.org/uniprotkb/A0A089MMR2.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A089MMR2.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35947916\",\"source\":\"PubMed\"}],\"value\":\"2.4.1.392\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"35947916\",\"source\":\"PubMed\"}],\"value\":\"3-O-beta-D-glucopyranosyl-beta-D-glucuronide phosphorylase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:37.192125+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9c1354b8bfe0e59449355743dfc7334d0ba6fb5835c3df3570380eed27e91719",
  "url": "https://rest.uniprot.org/uniprotkb/A0A089MMR2.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A089MMR2.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"2.4.1.392\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35947916\",\"source\":\"PubMed\"}],\"name\":\"3-O-beta-D-glucosyl-D-glucuronate + phosphate = aldehydo-D-glucuronate + alpha-D-glucose 1-phosphate\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:78711\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:43474\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58601\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:76826\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:142686\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:24:37.192125+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9c1354b8bfe0e59449355743dfc7334d0ba6fb5835c3df3570380eed27e91719",
  "url": "https://rest.uniprot.org/uniprotkb/A0A089MMR2.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A089MMR2.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"2.4.1.392\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35947916\",\"source\":\"PubMed\"}],\"name\":\"a 3-O-beta-D-glucosyl-beta-D-glucuronoside + phosphate = a beta-D-glucuronoside + alpha-D-glucose 1-phosphate\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:78699\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:43474\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58601\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:83411\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:229542\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-01T06:24:37.192125+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9c1354b8bfe0e59449355743dfc7334d0ba6fb5835c3df3570380eed27e91719",
  "url": "https://rest.uniprot.org/uniprotkb/A0A089MMR2.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A089MMR2.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Isono N.\",\"Mizutani E.\",\"Hayashida H.\",\"Katsuzaki H.\",\"Saburi W.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"35947916\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.bbrc.2022.07.098\"}],\"citationType\":\"journal article\",\"firstPage\":\"60\",\"id\":\"35947916\",\"journal\":\"Biochem. Biophys. Res. Commun.\",\"lastPage\":\"65\",\"publicationDate\":\"2022\",\"title\":\"Functional characterization of a novel GH94 glycoside phosphorylase, 3-O-beta-d-glucopyranosyl beta-d-glucuronide phosphorylase, and implication of the metabolic pathway of acidic carbohydrates in Paenibacillus borealis.\",\"volume\":\"625\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"DSM 13188 / CCUG 43137 / CIP 107056 / KCTC 3805 / KK19\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:24:37.192125+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9c1354b8bfe0e59449355743dfc7334d0ba6fb5835c3df3570380eed27e91719",
  "url": "https://rest.uniprot.org/uniprotkb/A0A089MMR2.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A089MMR2?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H1",
  "excerpt": "ID   BGBGP_PAEBO             Reviewed;         769 AA.\nAC   A0A089MMR2;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   26-NOV-2014, sequence version 1.\nDT   28-JAN-2026, entry version 38.\nDE   RecName: Full=3-O-beta-D-glucopyranosyl-beta-D-glucuronide phosphorylase {ECO:0000303|PubMed:35947916};\nDE            EC=2.4.1.392 {ECO:0000269|PubMed:35947916};\nGN   ORFNames=PBOR_13355 {ECO:0000312|EMBL:AIQ57809.1};\nOS   Paenibacillus borealis.\nOC   Bacteria; Bacillati; Bacillota; Bacilli; Bacillales; Paenibacillaceae;\nOC   Paenibacillus.\nOX   NCBI_TaxID=160799;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:15.632691+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "abf8108925ffb7b150428b7a1aa52e27f87e1ad71c64967596cc5207ae75a348",
  "url": "https://rest.uniprot.org/unisave/A0A089MMR2?format=txt&versions=38"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A089MMR2?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=3-O-beta-D-glucopyranosyl-beta-D-glucuronide phosphorylase {ECO:0000303|PubMed:35947916};\nDE            EC=2.4.1.392 {ECO:0000269|PubMed:35947916};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:15.632691+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "abf8108925ffb7b150428b7a1aa52e27f87e1ad71c64967596cc5207ae75a348",
  "url": "https://rest.uniprot.org/unisave/A0A089MMR2?format=txt&versions=38"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A089MMR2?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND SUBUNIT.\nRC   STRAIN=DSM 13188 / CCUG 43137 / CIP 107056 / KCTC 3805 / KK19;\nRX   PubMed=35947916; DOI=10.1016/j.bbrc.2022.07.098;\nRA   Isono N., Mizutani E., Hayashida H., Katsuzaki H., Saburi W.;\nRT   \"Functional characterization of a novel GH94 glycoside phosphorylase, 3-O-\nRT   beta-d-glucopyranosyl beta-d-glucuronide phosphorylase, and implication of\nRT   the metabolic pathway of acidic carbohydrates in Paenibacillus borealis.\";\nRL   Biochem. Biophys. Res. Commun. 625:60-65(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:15.632691+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 19-27",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "abf8108925ffb7b150428b7a1aa52e27f87e1ad71c64967596cc5207ae75a348",
  "url": "https://rest.uniprot.org/unisave/A0A089MMR2?format=txt&versions=38"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A089MMR2?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=3-O-beta-D-glucosyl-D-glucuronate + phosphate = aldehydo-D-\nCC         glucuronate + alpha-D-glucose 1-phosphate; Xref=Rhea:RHEA:78711,\nCC         ChEBI:CHEBI:43474, ChEBI:CHEBI:58601, ChEBI:CHEBI:76826,\nCC         ChEBI:CHEBI:142686; EC=2.4.1.392;\nCC         Evidence={ECO:0000269|PubMed:35947916};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:15.632691+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 41-46",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "abf8108925ffb7b150428b7a1aa52e27f87e1ad71c64967596cc5207ae75a348",
  "url": "https://rest.uniprot.org/unisave/A0A089MMR2?format=txt&versions=38"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A089MMR2?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=a 3-O-beta-D-glucosyl-beta-D-glucuronoside + phosphate = a\nCC         beta-D-glucuronoside + alpha-D-glucose 1-phosphate;\nCC         Xref=Rhea:RHEA:78699, ChEBI:CHEBI:43474, ChEBI:CHEBI:58601,\nCC         ChEBI:CHEBI:83411, ChEBI:CHEBI:229542; EC=2.4.1.392;\nCC         Evidence={ECO:0000269|PubMed:35947916};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:15.632691+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 47-52",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "abf8108925ffb7b150428b7a1aa52e27f87e1ad71c64967596cc5207ae75a348",
  "url": "https://rest.uniprot.org/unisave/A0A089MMR2?format=txt&versions=38"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 91. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
