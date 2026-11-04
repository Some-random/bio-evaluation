# EC_number_0105

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0105.txt)

**Task:** `EC_number`  
**Expected answer:** **D** — 2.3.1.322

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAPILQRISKTFIKPSSPTPESLRCYNLSSSDQMITSVYISLAFFYGSPGCESSRIRQQLDNSLSRTLVYYYPFAGRLVDNDHIDCNDQGVQFVEVRIHCPISAILKQTTSYAEDLVFPRGTSACHEDSLVVVQLNRFECGGVAIAVCISHKVADGSGAIAFINDWAATARVSSHIPSPLLVADSIFPHLDNSLPVPYNLSKNCVTRRFVFPAAEIEKLKSKAVESGLQQPTRVEVVTALLYQCALLASRSTNSGLSRPSVLIQAVNLRPFLVPPLPRNSVGNIFSINFSIIEVDSLEFPELAGRLRKAKLKFQNLSQEKLYYDSQMQELGECLKQLNTGNFDVYYCSSWCRFPVYDVDFGWGKPTWVCTVKSQIKDMIVLMDSPGDEIAAFVTLEEEKMSAFQHNELLLSFASLYSAK

[Multiple Choices]
A. 2.3.1.319
B. 1.14.11.53
C. 1.14.14.154
D. 2.3.1.322
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

> The sequence-matched record assigns EC 2.3.1.322 and reports the catalytic reaction rhazimol + acetyl-CoA = akuammiline + CoA + H(+), with ECO:0000269 evidence. This supports the key, though the cited experiment is not independently assessed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has the characteristic motifs of a BAHD-family acyltransferase, which makes the two EC 2.3.1 choices more plausible than the oxygenase choices. But both A and D are acyltransferase classifications; the family-level inference does not establish which specific reaction this protein catalyzes.


**Missing item-specific fact**

> Whether this particular enzyme catalyzes the rhazimol-to-akuammiline acetylation, rather than the reaction assigned to EC 2.3.1.319.


**Reason**

> Transferable sequence knowledge can narrow the choices to acyltransferases, but distinguishing A from D requires substrate- and product-specific functional knowledge not established by the sequence motifs alone. The reviewer-only reaction annotation supports D but was not part of the original input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied experimental annotation supports D; the fact that the original sequence does not meaningfully distinguish D from A is a limitation on answerability, not evidence that both EC numbers are correct.


### Important caveats

- The source record matches the supplied sequence, and its EC assignment cites experimental evidence, but the underlying study was not independently reviewed.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has the characteristic motifs of a BAHD-family acyltransferase, which makes the two EC 2.3.1 choices more plausible than the oxygenase choices. But both A and D are acyltransferase classifications; the family-level inference does not establish which specific reaction this protein catalyzes.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Whether this particular enzyme catalyzes the rhazimol-to-akuammiline acetylation, rather than the reaction assigned to EC 2.3.1.319.",
    "reason": "Transferable sequence knowledge can narrow the choices to acyltransferases, but distinguishing A from D requires substrate- and product-specific functional knowledge not established by the sequence motifs alone. The reviewer-only reaction annotation supports D but was not part of the original input."
  },
  "case_id": "EC_number_0105",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched record assigns EC 2.3.1.322 and reports the catalytic reaction rhazimol + acetyl-CoA = akuammiline + CoA + H(+), with ECO:0000269 evidence. This supports the key, though the cited experiment is not independently assessed here."
  },
  "important_caveats": [
    "The source record matches the supplied sequence, and its EC assignment cites experimental evidence, but the underlying study was not independently reviewed."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied experimental annotation supports D; the fact that the original sequence does not meaningfully distinguish D from A is a limitation on answerability, not evidence that both EC numbers are correct."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0105",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched record assigns EC 2.3.1.322 and reports the catalytic reaction rhazimol + acetyl-CoA = akuammiline + CoA + H(+), with ECO:0000269 evidence. This supports the key, though the cited experiment is not independently assessed here.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has the characteristic motifs of a BAHD-family acyltransferase, which makes the two EC 2.3.1 choices more plausible than the oxygenase choices. But both A and D are acyltransferase classifications; the family-level inference does not establish which specific reaction this protein catalyzes.",
    "missing_item_specific_fact": "Whether this particular enzyme catalyzes the rhazimol-to-akuammiline acetylation, rather than the reaction assigned to EC 2.3.1.319.",
    "reason": "Transferable sequence knowledge can narrow the choices to acyltransferases, but distinguishing A from D requires substrate- and product-specific functional knowledge not established by the sequence motifs alone. The reviewer-only reaction annotation supports D but was not part of the original input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied experimental annotation supports D; the fact that the original sequence does not meaningfully distinguish D from A is a limitation on answerability, not evidence that both EC numbers are correct."
  },
  "important_caveats": [
    "The source record matches the supplied sequence, and its EC assignment cites experimental evidence, but the underlying study was not independently reviewed."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt Swiss-Prot entry A0A9E7S5E3 (Akuammiline synthase 1, AsAKS1) is annotated with EC 2.3.1.322, supported by experimental evidence (ECO:0000269, PubMed:36349266). The catalytic reaction rhazimol + acetyl-CoA = akuammiline + CoA + H(+) confirms the acyltransferase classification. The sequence matches the benchmark input exactly (419 AA, SHA-256 matched).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A knowledgeable model can partially narrow the field: the absence of the canonical P450 heme-binding motif (FxxGxxxCxG with the axial Cys) argues against option C (1.14.14.154, a cytochrome P450), and the absence of the 2-His-1-carboxylate facial triad (HxD/E...H spaced ~100-200 residues) typical of 2-oxoglutarate-dependent dioxygenases argues against option B (1.14.11.53). The protein length (~419 AA) and the plant Apocynaceae context are consistent with BAHD acyltransferases (EC 2.3.1.x), which are well-known participants in monoterpene indole alkaloid (MIA) biosynthesis in this family. However, both remaining options A (2.3.1.319) and D (2.3.1.322) are acyltransferases in the same 3-digit class. Distinguishing between two specific 4-digit EC numbers within 2.3.1.3xx requires knowing the exact substrate and reaction (here, rhazimol + acetyl-CoA → akuammiline), which is a protein-specific experimental finding published in 2022 and not derivable from sequence motifs, family membership, or general BAHD acyltransferase biochemistry alone.


**Missing item-specific fact**

> The specific substrate identity (rhazimol) and the resulting 4-digit EC assignment 2.3.1.322, established experimentally in 2022 (Wang et al., Chem. Sci. 13:12389-12395). Without this, a model cannot distinguish 2.3.1.319 from 2.3.1.322, as both are acyltransferases potentially active on MIA-pathway intermediates in Apocynaceae.


**Reason**

> While transferable knowledge about BAHD acyltransferase family features and the absence of P450/dioxygenase motifs can eliminate options B and C, the final distinction between options A and D (both EC 2.3.1.3xx acyltransferases) requires the specific substrate-reaction annotation of this exact protein, which is not encoded in recognizable sequence motifs and was determined by 2022 experimental work.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> Both A (2.3.1.319) and D (2.3.1.322) are acyltransferases. Without the specific substrate annotation, a model that correctly identifies the protein as a BAHD-family acyltransferase active in Apocynaceae MIA biosynthesis cannot definitively choose between these two 4-digit EC numbers based on sequence features alone.


### Important caveats

- The EC 2.3.1.322 assignment is recent (2022) and based on a single experimental study; the 2.3.1.319 entry's identity and substrate were not independently verified in this review.
- The reviewer-only evidence confirms sequence identity and annotation but was not available to the evaluated model.
- The BAHD motifs (DPxxD, HxxxD) are present in degenerate form in the sequence but are not unambiguously identifiable without prior family knowledge, making even the broad class assignment somewhat dependent on learned patterns from other BAHD enzymes.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can partially narrow the field: the absence of the canonical P450 heme-binding motif (FxxGxxxCxG with the axial Cys) argues against option C (1.14.14.154, a cytochrome P450), and the absence of the 2-His-1-carboxylate facial triad (HxD/E...H spaced ~100-200 residues) typical of 2-oxoglutarate-dependent dioxygenases argues against option B (1.14.11.53). The protein length (~419 AA) and the plant Apocynaceae context are consistent with BAHD acyltransferases (EC 2.3.1.x), which are well-known participants in monoterpene indole alkaloid (MIA) biosynthesis in this family. However, both remaining options A (2.3.1.319) and D (2.3.1.322) are acyltransferases in the same 3-digit class. Distinguishing between two specific 4-digit EC numbers within 2.3.1.3xx requires knowing the exact substrate and reaction (here, rhazimol + acetyl-CoA → akuammiline), which is a protein-specific experimental finding published in 2022 and not derivable from sequence motifs, family membership, or general BAHD acyltransferase biochemistry alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate identity (rhazimol) and the resulting 4-digit EC assignment 2.3.1.322, established experimentally in 2022 (Wang et al., Chem. Sci. 13:12389-12395). Without this, a model cannot distinguish 2.3.1.319 from 2.3.1.322, as both are acyltransferases potentially active on MIA-pathway intermediates in Apocynaceae.",
    "reason": "While transferable knowledge about BAHD acyltransferase family features and the absence of P450/dioxygenase motifs can eliminate options B and C, the final distinction between options A and D (both EC 2.3.1.3xx acyltransferases) requires the specific substrate-reaction annotation of this exact protein, which is not encoded in recognizable sequence motifs and was determined by 2022 experimental work."
  },
  "case_id": "EC_number_0105",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt Swiss-Prot entry A0A9E7S5E3 (Akuammiline synthase 1, AsAKS1) is annotated with EC 2.3.1.322, supported by experimental evidence (ECO:0000269, PubMed:36349266). The catalytic reaction rhazimol + acetyl-CoA = akuammiline + CoA + H(+) confirms the acyltransferase classification. The sequence matches the benchmark input exactly (419 AA, SHA-256 matched)."
  },
  "important_caveats": [
    "The EC 2.3.1.322 assignment is recent (2022) and based on a single experimental study; the 2.3.1.319 entry's identity and substrate were not independently verified in this review.",
    "The reviewer-only evidence confirms sequence identity and annotation but was not available to the evaluated model.",
    "The BAHD motifs (DPxxD, HxxxD) are present in degenerate form in the sequence but are not unambiguously identifiable without prior family knowledge, making even the broad class assignment somewhat dependent on learned patterns from other BAHD enzymes."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "Both A (2.3.1.319) and D (2.3.1.322) are acyltransferases. Without the specific substrate annotation, a model that correctly identifies the protein as a BAHD-family acyltransferase active in Apocynaceae MIA biosynthesis cannot definitively choose between these two 4-digit EC numbers based on sequence features alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0105",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt Swiss-Prot entry A0A9E7S5E3 (Akuammiline synthase 1, AsAKS1) is annotated with EC 2.3.1.322, supported by experimental evidence (ECO:0000269, PubMed:36349266). The catalytic reaction rhazimol + acetyl-CoA = akuammiline + CoA + H(+) confirms the acyltransferase classification. The sequence matches the benchmark input exactly (419 AA, SHA-256 matched).",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A knowledgeable model can partially narrow the field: the absence of the canonical P450 heme-binding motif (FxxGxxxCxG with the axial Cys) argues against option C (1.14.14.154, a cytochrome P450), and the absence of the 2-His-1-carboxylate facial triad (HxD/E...H spaced ~100-200 residues) typical of 2-oxoglutarate-dependent dioxygenases argues against option B (1.14.11.53). The protein length (~419 AA) and the plant Apocynaceae context are consistent with BAHD acyltransferases (EC 2.3.1.x), which are well-known participants in monoterpene indole alkaloid (MIA) biosynthesis in this family. However, both remaining options A (2.3.1.319) and D (2.3.1.322) are acyltransferases in the same 3-digit class. Distinguishing between two specific 4-digit EC numbers within 2.3.1.3xx requires knowing the exact substrate and reaction (here, rhazimol + acetyl-CoA → akuammiline), which is a protein-specific experimental finding published in 2022 and not derivable from sequence motifs, family membership, or general BAHD acyltransferase biochemistry alone.",
    "missing_item_specific_fact": "The specific substrate identity (rhazimol) and the resulting 4-digit EC assignment 2.3.1.322, established experimentally in 2022 (Wang et al., Chem. Sci. 13:12389-12395). Without this, a model cannot distinguish 2.3.1.319 from 2.3.1.322, as both are acyltransferases potentially active on MIA-pathway intermediates in Apocynaceae.",
    "reason": "While transferable knowledge about BAHD acyltransferase family features and the absence of P450/dioxygenase motifs can eliminate options B and C, the final distinction between options A and D (both EC 2.3.1.3xx acyltransferases) requires the specific substrate-reaction annotation of this exact protein, which is not encoded in recognizable sequence motifs and was determined by 2022 experimental work."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "Both A (2.3.1.319) and D (2.3.1.322) are acyltransferases. Without the specific substrate annotation, a model that correctly identifies the protein as a BAHD-family acyltransferase active in Apocynaceae MIA biosynthesis cannot definitively choose between these two 4-digit EC numbers based on sequence features alone."
  },
  "important_caveats": [
    "The EC 2.3.1.322 assignment is recent (2022) and based on a single experimental study; the 2.3.1.319 entry's identity and substrate were not independently verified in this review.",
    "The reviewer-only evidence confirms sequence identity and annotation but was not available to the evaluated model.",
    "The BAHD motifs (DPxxD, HxxxD) are present in degenerate form in the sequence but are not unambiguously identifiable without prior family knowledge, making even the broad class assignment somewhat dependent on learned patterns from other BAHD enzymes."
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
  "benchmark_sequence_length": 419,
  "benchmark_sequence_sha256": "4d53f81259ad6ebf110d3f0389144aaa3ab73e2a4032a10a17048eaa8c40b8bf",
  "current_entry_audit": {
    "entryVersion": 15,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2023-05-03",
    "sequenceVersion": 1
  },
  "current_record_sha256": "dccc1e1f78f84ddf8a52309526ec78e3e0e822b2e5e5620c9b28bd1314fc2e3d",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 419,
  "current_source_sequence_sha256": "4d53f81259ad6ebf110d3f0389144aaa3ab73e2a4032a10a17048eaa8c40b8bf",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 13,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A9E7S5E3",
  "selected_historical_entry_version": 13,
  "selected_historical_record_sha256": "1462d014137043d064b721b692e151871424684911f566849eb4da04580f0a54",
  "selected_historical_source_sequence_length": 419,
  "selected_historical_source_sequence_sha256": "4d53f81259ad6ebf110d3f0389144aaa3ab73e2a4032a10a17048eaa8c40b8bf",
  "selected_historical_version": {
    "accession": "A0A9E7S5E3",
    "database": "Swiss-Prot",
    "entryVersion": 13,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "AKS1_ALSSC",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S5E3.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A9E7S5E3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:54.493793+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dccc1e1f78f84ddf8a52309526ec78e3e0e822b2e5e5620c9b28bd1314fc2e3d",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S5E3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S5E3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":15,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2023-05-03\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:54.493793+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dccc1e1f78f84ddf8a52309526ec78e3e0e822b2e5e5620c9b28bd1314fc2e3d",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S5E3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S5E3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Dogbane\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Apocynaceae\",\"Rauvolfioideae\",\"Alstonieae\",\"Alstonia\"],\"scientificName\":\"Alstonia scholaris\",\"synonyms\":[\"Echites scholaris\"],\"taxonId\":52822}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:54.493793+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dccc1e1f78f84ddf8a52309526ec78e3e0e822b2e5e5620c9b28bd1314fc2e3d",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S5E3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S5E3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"value\":\"2.3.1.322\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"value\":\"Akuammiline synthase 1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"value\":\"AsAKS1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:54.493793+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dccc1e1f78f84ddf8a52309526ec78e3e0e822b2e5e5620c9b28bd1314fc2e3d",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S5E3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S5E3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:79624\"}}],\"reaction\":{\"ecNumber\":\"2.3.1.322\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"name\":\"rhazimol + acetyl-CoA = akuammiline + CoA + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:79623\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57287\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57288\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:141879\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:230474\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:24:54.493793+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dccc1e1f78f84ddf8a52309526ec78e3e0e822b2e5e5620c9b28bd1314fc2e3d",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S5E3.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S5E3.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Wang Z.\",\"Xiao Y.\",\"Wu S.\",\"Chen J.\",\"Li A.\",\"Tatsis E.C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"36349266\"},{\"database\":\"DOI\",\"id\":\"10.1039/d2sc03612f\"}],\"citationType\":\"journal article\",\"firstPage\":\"12389\",\"id\":\"36349266\",\"journal\":\"Chem. Sci.\",\"lastPage\":\"12395\",\"publicationDate\":\"2022\",\"title\":\"Deciphering and reprogramming the cyclization regioselectivity in bifurcation of indole alkaloid biosynthesis.\",\"volume\":\"13\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"URS65387.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:24:54.493793+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dccc1e1f78f84ddf8a52309526ec78e3e0e822b2e5e5620c9b28bd1314fc2e3d",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S5E3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S5E3?format=txt&versions=13)

```json
{
  "entry_version": 13,
  "evidence_id": "H1",
  "excerpt": "ID   AKS1_ALSSC              Reviewed;         419 AA.\nAC   A0A9E7S5E3;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   03-MAY-2023, sequence version 1.\nDT   28-JAN-2026, entry version 13.\nDE   RecName: Full=Akuammiline synthase 1 {ECO:0000303|PubMed:36349266};\nDE            Short=AsAKS1 {ECO:0000303|PubMed:36349266};\nDE            EC=2.3.1.322 {ECO:0000269|PubMed:36349266};\nGN   Name=AKS1 {ECO:0000303|PubMed:36349266};\nGN   Synonyms=BAHD3 {ECO:0000303|PubMed:36349266};\nOS   Alstonia scholaris (Dogbane) (Echites scholaris).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Alstonieae;\nOC   Alstonia.\nOX   NCBI_TaxID=52822;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:37.651074+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1462d014137043d064b721b692e151871424684911f566849eb4da04580f0a54",
  "url": "https://rest.uniprot.org/unisave/A0A9E7S5E3?format=txt&versions=13"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S5E3?format=txt&versions=13)

```json
{
  "entry_version": 13,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Akuammiline synthase 1 {ECO:0000303|PubMed:36349266};\nDE            Short=AsAKS1 {ECO:0000303|PubMed:36349266};\nDE            EC=2.3.1.322 {ECO:0000269|PubMed:36349266};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:37.651074+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1462d014137043d064b721b692e151871424684911f566849eb4da04580f0a54",
  "url": "https://rest.uniprot.org/unisave/A0A9E7S5E3?format=txt&versions=13"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S5E3?format=txt&versions=13)

```json
{
  "entry_version": 13,
  "evidence_id": "H3",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:URS65387.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, PATHWAY, AND\nRP   BIOPHYSICOCHEMICAL PROPERTIES.\nRX   PubMed=36349266; DOI=10.1039/d2sc03612f;\nRA   Wang Z., Xiao Y., Wu S., Chen J., Li A., Tatsis E.C.;\nRT   \"Deciphering and reprogramming the cyclization regioselectivity in\nRT   bifurcation of indole alkaloid biosynthesis.\";\nRL   Chem. Sci. 13:12389-12395(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:37.651074+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 17-24",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1462d014137043d064b721b692e151871424684911f566849eb4da04580f0a54",
  "url": "https://rest.uniprot.org/unisave/A0A9E7S5E3?format=txt&versions=13"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S5E3?format=txt&versions=13)

```json
{
  "entry_version": 13,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=rhazimol + acetyl-CoA = akuammiline + CoA + H(+);\nCC         Xref=Rhea:RHEA:79623, ChEBI:CHEBI:15378, ChEBI:CHEBI:57287,\nCC         ChEBI:CHEBI:57288, ChEBI:CHEBI:141879, ChEBI:CHEBI:230474;\nCC         EC=2.3.1.322; Evidence={ECO:0000269|PubMed:36349266};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:79624;\nCC         Evidence={ECO:0000269|PubMed:36349266};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:37.651074+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 31-37",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1462d014137043d064b721b692e151871424684911f566849eb4da04580f0a54",
  "url": "https://rest.uniprot.org/unisave/A0A9E7S5E3?format=txt&versions=13"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 105. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
