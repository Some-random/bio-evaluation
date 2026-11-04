# temperature_0002

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/temperature_0002.txt)

**Task:** `temperature`  
**Expected answer:** **B** — 35

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
A. 36
B. 35
C. 29-38
D. 69
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Thermal Adaptation Prediction, which is to predict the thermal adaptation category of a protein. This relates to the optimal temperature range in which the protein is stable and functional (e.g., cold-adapted, moderate temperature-adapted, or heat-adapted). This property is encoded by subtle patterns in the amino acid sequence that affect the protein's structural stability, such as amino acid composition and the potential for internal bonds. Based on the provided sequence, you must classify the protein into its most likely thermal category.. The inputs provided by the user for this task include:

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

> The sequence-matched source reports an experimentally supported optimum temperature of 35°C for the reverse phosphorolytic activity, matching choice B. This supports the key for that assay, though it is not necessarily a general measurement of thermal stability or adaptation.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may support a broad prediction of a moderate-temperature enzyme, but transferable family or sequence knowledge does not meaningfully distinguish an exact optimum of 35°C from 36°C. The 69°C option is much less consistent with that broad prediction, but that does not identify choice B over the nearby alternative.


**Missing item-specific fact**

> The measured optimum temperature for this exact protein in the specified reaction; the supplied sequence and choices do not provide it.


**Reason**

> Choosing the exact keyed value depends on a target-specific measurement rather than a transferable inference that separates 35°C from 36°C.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> The task describes thermal-category prediction, while the choices mix exact temperatures with a range. Since 35°C lies within 29–38°C, both B and C are defensible if the requested answer is a temperature range or category; B is the supported choice if an exact measured optimum is intended.


### Important caveats

- The reported optimum is specifically for reverse phosphorolytic activity; it should not be treated as a direct measurement of the protein's full stability range or thermal adaptation category.
- The reviewer-only source is sequence-matched, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may support a broad prediction of a moderate-temperature enzyme, but transferable family or sequence knowledge does not meaningfully distinguish an exact optimum of 35°C from 36°C. The 69°C option is much less consistent with that broad prediction, but that does not identify choice B over the nearby alternative.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The measured optimum temperature for this exact protein in the specified reaction; the supplied sequence and choices do not provide it.",
    "reason": "Choosing the exact keyed value depends on a target-specific measurement rather than a transferable inference that separates 35°C from 36°C."
  },
  "case_id": "temperature_0002",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched source reports an experimentally supported optimum temperature of 35°C for the reverse phosphorolytic activity, matching choice B. This supports the key for that assay, though it is not necessarily a general measurement of thermal stability or adaptation."
  },
  "important_caveats": [
    "The reported optimum is specifically for reverse phosphorolytic activity; it should not be treated as a direct measurement of the protein's full stability range or thermal adaptation category.",
    "The reviewer-only source is sequence-matched, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "The task describes thermal-category prediction, while the choices mix exact temperatures with a range. Since 35°C lies within 29–38°C, both B and C are defensible if the requested answer is a temperature range or category; B is the supported choice if an exact measured optimum is intended."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "temperature_0002",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched source reports an experimentally supported optimum temperature of 35°C for the reverse phosphorolytic activity, matching choice B. This supports the key for that assay, though it is not necessarily a general measurement of thermal stability or adaptation.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may support a broad prediction of a moderate-temperature enzyme, but transferable family or sequence knowledge does not meaningfully distinguish an exact optimum of 35°C from 36°C. The 69°C option is much less consistent with that broad prediction, but that does not identify choice B over the nearby alternative.",
    "missing_item_specific_fact": "The measured optimum temperature for this exact protein in the specified reaction; the supplied sequence and choices do not provide it.",
    "reason": "Choosing the exact keyed value depends on a target-specific measurement rather than a transferable inference that separates 35°C from 36°C."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "The task describes thermal-category prediction, while the choices mix exact temperatures with a range. Since 35°C lies within 29–38°C, both B and C are defensible if the requested answer is a temperature range or category; B is the supported choice if an exact measured optimum is intended."
  },
  "important_caveats": [
    "The reported optimum is specifically for reverse phosphorolytic activity; it should not be treated as a direct measurement of the protein's full stability range or thermal adaptation category.",
    "The reviewer-only source is sequence-matched, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A089MMR2) for this exact protein (3-O-beta-D-glucopyranosyl-beta-D-glucuronide phosphorylase from Paenibacillus borealis) reports an experimentally determined optimum temperature of 35°C (ECO:0000269, PubMed:35947916). The sequence matches exactly (SHA256 confirmed). Choice B (35) directly corresponds to this measured value.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A knowledgeable model can eliminate D (69°C) as thermophilic: the sequence lacks hallmark thermophilic adaptations (elevated charged residues, high proline, reduced thermolabile residues). It can also recognize the protein as a mesophilic GH94-family phosphorylase based on sequence features. However, distinguishing 35°C from 36°C from amino acid sequence alone is not achievable through any known transferable biological principle. No sequence motif, composition bias, or family-level regularity correlates with a 1°C difference in optimum temperature. Similarly, choosing between a single value (35) and a range (29-38) requires knowing the specific experimental measurement format reported for this protein.


**Missing item-specific fact**

> The exact experimentally measured optimum temperature (35°C) for this specific protein from Paenibacillus borealis, as reported in PubMed:35947916. No sequence-derived feature distinguishes 35°C from 36°C optimum.


**Reason**

> While the broad thermal category (mesophilic vs. thermophilic) is inferable from sequence composition and family knowledge, the specific numerical distinction between 35 and 36 (and between a point value and a range) requires the exact experimental annotation for this protein. No transferable knowledge from other proteins or general biology provides a meaningful basis for choosing 35 over 36.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B",
  "C"
]
```

> From sequence alone, a model can only determine the protein is mesophilic. All three options A (36), B (35), and C (29-38) are within the mesophilic range and cannot be reliably distinguished from one another based on amino acid composition or structural principles. The 1°C difference between 35 and 36 has no known sequence correlate. Option C (29-38) as a range also encompasses the correct value and is arguably a valid description of the functional temperature window (the protein retains >90% activity at 30°C).


### Important caveats

- The optimum temperature (35°C) was measured for the reverse phosphorolytic activity specifically; forward activity may differ.
- The protein retains >90% activity after 1 hour at 30°C, which could support interpreting the functional range as broader than a single point value.
- The organism name 'Paenibacillus borealis' (suggesting northern/cold habitat) is not provided to the model in the original input; only the raw sequence is given.
- The distinction between 35 and 36 is within typical experimental error for enzyme optimum temperature measurements.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can eliminate D (69°C) as thermophilic: the sequence lacks hallmark thermophilic adaptations (elevated charged residues, high proline, reduced thermolabile residues). It can also recognize the protein as a mesophilic GH94-family phosphorylase based on sequence features. However, distinguishing 35°C from 36°C from amino acid sequence alone is not achievable through any known transferable biological principle. No sequence motif, composition bias, or family-level regularity correlates with a 1°C difference in optimum temperature. Similarly, choosing between a single value (35) and a range (29-38) requires knowing the specific experimental measurement format reported for this protein.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact experimentally measured optimum temperature (35°C) for this specific protein from Paenibacillus borealis, as reported in PubMed:35947916. No sequence-derived feature distinguishes 35°C from 36°C optimum.",
    "reason": "While the broad thermal category (mesophilic vs. thermophilic) is inferable from sequence composition and family knowledge, the specific numerical distinction between 35 and 36 (and between a point value and a range) requires the exact experimental annotation for this protein. No transferable knowledge from other proteins or general biology provides a meaningful basis for choosing 35 over 36."
  },
  "case_id": "temperature_0002",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A089MMR2) for this exact protein (3-O-beta-D-glucopyranosyl-beta-D-glucuronide phosphorylase from Paenibacillus borealis) reports an experimentally determined optimum temperature of 35°C (ECO:0000269, PubMed:35947916). The sequence matches exactly (SHA256 confirmed). Choice B (35) directly corresponds to this measured value."
  },
  "important_caveats": [
    "The optimum temperature (35°C) was measured for the reverse phosphorolytic activity specifically; forward activity may differ.",
    "The protein retains >90% activity after 1 hour at 30°C, which could support interpreting the functional range as broader than a single point value.",
    "The organism name 'Paenibacillus borealis' (suggesting northern/cold habitat) is not provided to the model in the original input; only the raw sequence is given.",
    "The distinction between 35 and 36 is within typical experimental error for enzyme optimum temperature measurements."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B",
      "C"
    ],
    "reason": "From sequence alone, a model can only determine the protein is mesophilic. All three options A (36), B (35), and C (29-38) are within the mesophilic range and cannot be reliably distinguished from one another based on amino acid composition or structural principles. The 1°C difference between 35 and 36 has no known sequence correlate. Option C (29-38) as a range also encompasses the correct value and is arguably a valid description of the functional temperature window (the protein retains >90% activity at 30°C)."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "temperature_0002",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A089MMR2) for this exact protein (3-O-beta-D-glucopyranosyl-beta-D-glucuronide phosphorylase from Paenibacillus borealis) reports an experimentally determined optimum temperature of 35°C (ECO:0000269, PubMed:35947916). The sequence matches exactly (SHA256 confirmed). Choice B (35) directly corresponds to this measured value.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A knowledgeable model can eliminate D (69°C) as thermophilic: the sequence lacks hallmark thermophilic adaptations (elevated charged residues, high proline, reduced thermolabile residues). It can also recognize the protein as a mesophilic GH94-family phosphorylase based on sequence features. However, distinguishing 35°C from 36°C from amino acid sequence alone is not achievable through any known transferable biological principle. No sequence motif, composition bias, or family-level regularity correlates with a 1°C difference in optimum temperature. Similarly, choosing between a single value (35) and a range (29-38) requires knowing the specific experimental measurement format reported for this protein.",
    "missing_item_specific_fact": "The exact experimentally measured optimum temperature (35°C) for this specific protein from Paenibacillus borealis, as reported in PubMed:35947916. No sequence-derived feature distinguishes 35°C from 36°C optimum.",
    "reason": "While the broad thermal category (mesophilic vs. thermophilic) is inferable from sequence composition and family knowledge, the specific numerical distinction between 35 and 36 (and between a point value and a range) requires the exact experimental annotation for this protein. No transferable knowledge from other proteins or general biology provides a meaningful basis for choosing 35 over 36."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B", "C"],
    "reason": "From sequence alone, a model can only determine the protein is mesophilic. All three options A (36), B (35), and C (29-38) are within the mesophilic range and cannot be reliably distinguished from one another based on amino acid composition or structural principles. The 1°C difference between 35 and 36 has no known sequence correlate. Option C (29-38) as a range also encompasses the correct value and is arguably a valid description of the functional temperature window (the protein retains >90% activity at 30°C)."
  },
  "important_caveats": [
    "The optimum temperature (35°C) was measured for the reverse phosphorolytic activity specifically; forward activity may differ.",
    "The protein retains >90% activity after 1 hour at 30°C, which could support interpreting the functional range as broader than a single point value.",
    "The organism name 'Paenibacillus borealis' (suggesting northern/cold habitat) is not provided to the model in the original input; only the raw sequence is given.",
    "The distinction between 35 and 36 is within typical experimental error for enzyme optimum temperature measurements."
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
  "excerpt": "{\"commentType\":\"BIOPHYSICOCHEMICAL PROPERTIES\",\"kineticParameters\":{\"michaelisConstants\":[{\"constant\":7.89,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35947916\",\"source\":\"PubMed\"}],\"substrate\":\"3-O-beta-D-glucosyl-D-glucuronate\",\"unit\":\"mM\"},{\"constant\":1.52,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35947916\",\"source\":\"PubMed\"}],\"substrate\":\"phosphate\",\"unit\":\"mM\"},{\"constant\":1.57,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35947916\",\"source\":\"PubMed\"}],\"substrate\":\"alpha-D-glucose 1-phosphate\",\"unit\":\"mM\"},{\"constant\":11.7,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35947916\",\"source\":\"PubMed\"}],\"substrate\":\"D-glucuronic acid\",\"unit\":\"mM\"},{\"constant\":3.02,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35947916\",\"source\":\"PubMed\"}],\"substrate\":\"p-nitrophenyl-beta-D-glucuronide\",\"unit\":\"mM\"}],\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35947916\",\"source\":\"PubMed\"}],\"value\":\"kcat is 102 sec(-1) with O-beta-D-glucosyl-D-glucuronate as substrate (PubMed:35947916). kcat is 156 sec(-1) with alpha-D-glucose 1-phosphate as substrate (PubMed:35947916). kcat is 351 sec(-1) with D-glucuronic acid as substrate (PubMed:35947916). kcat is 433 sec(-1) with p-nitrophenyl-beta-D-glucuronide as substrate (PubMed:35947916).\"}]}},\"phDependence\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35947916\",\"source\":\"PubMed\"}],\"value\":\"Optimum pH is 6.9 (for the reverse phosphorolytic activity) (PubMed:35947916). Stable between pH 6.6 and 8.8 at 4 degrees Celsius for 24 hours (PubMed:35947916).\"}]},\"temperatureDependence\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35947916\",\"source\":\"PubMed\"}],\"value\":\"Optimum temperature is 35 degrees Celsius (for the reverse phosphorolytic activity) (PubMed:35947916). Retains more than 90% of its original activity after incubation at 30 degrees Celsius for 1 hour (PubMed:35947916).\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
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

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A089MMR2?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H3",
  "excerpt": "CC   -!- BIOPHYSICOCHEMICAL PROPERTIES:\nCC       Kinetic parameters:\nCC         KM=7.89 mM for 3-O-beta-D-glucosyl-D-glucuronate\nCC         {ECO:0000269|PubMed:35947916};\nCC         KM=1.52 mM for phosphate {ECO:0000269|PubMed:35947916};\nCC         KM=1.57 mM for alpha-D-glucose 1-phosphate\nCC         {ECO:0000269|PubMed:35947916};\nCC         KM=11.7 mM for D-glucuronic acid {ECO:0000269|PubMed:35947916};\nCC         KM=3.02 mM for p-nitrophenyl-beta-D-glucuronide\nCC         {ECO:0000269|PubMed:35947916};\nCC         Note=kcat is 102 sec(-1) with O-beta-D-glucosyl-D-glucuronate as\nCC         substrate (PubMed:35947916). kcat is 156 sec(-1) with alpha-D-glucose\nCC         1-phosphate as substrate (PubMed:35947916). kcat is 351 sec(-1) with\nCC         D-glucuronic acid as substrate (PubMed:35947916). kcat is 433 sec(-1)\nCC         with p-nitrophenyl-beta-D-glucuronide as substrate (PubMed:35947916).\nCC         {ECO:0000269|PubMed:35947916};\nCC       pH dependence:\nCC         Optimum pH is 6.9 (for the reverse phosphorolytic activity)\nCC         (PubMed:35947916). Stable between pH 6.6 and 8.8 at 4 degrees Celsius\nCC         for 24 hours (PubMed:35947916). {ECO:0000269|PubMed:35947916};\nCC       Temperature dependence:\nCC         Optimum temperature is 35 degrees Celsius (for the reverse\nCC         phosphorolytic activity) (PubMed:35947916). Retains more than 90% of\nCC         its original activity after incubation at 30 degrees Celsius for 1\nCC         hour (PubMed:35947916). {ECO:0000269|PubMed:35947916};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:15.632691+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 53-77",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "abf8108925ffb7b150428b7a1aa52e27f87e1ad71c64967596cc5207ae75a348",
  "url": "https://rest.uniprot.org/unisave/A0A089MMR2?format=txt&versions=38"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/temperature.json), zero-based source row 2. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
