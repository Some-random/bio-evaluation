# temperature_0019

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/temperature_0019.txt)

**Task:** `temperature`  
**Expected answer:** **A** — 35.0

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKTFAPLLATLLLAGFGSALQWWEHGNFYQVYPRSFKDSDGNGIGDLDGVTEKLQYLKDVGMDGIWLSPIFASPMADFGYDISDFYNIQGEYGDLAAFERLSAKCKELGLRLILDFVPNHTSNQHEYFKKSVQKEDPYTNYYVWHPGVTNEDGTKSPPSNWISVFRGSAWEWNEDRQEYYLHQFLKEQPDLNYRDPALVEEMKNVLKFWLNKGVSGFRIDAVPYLFESVEVENRYVDEPLSRATDDAENPAYLIHNQTMDQPETYDMIYQWRAVLDEFTAKDNQTRIMMTEGYTSIPNVMKFFGEGEQNGAQIPFNFQMISNLRKTSTAADFARYANLWLDNLPAGRRSNWVLGNHDNNRIGSRLGEAKIDLYNIALQTLPDIAVTYYGEEIGMVDQPIPFNETVDPAGLRAGPDDYTLYSRDPARTPMQWNSDKNAGFSSADKTWLPVATNYKQLNVKAQDAAQKSHLKLFKRLTTYRKRQILTHGDLDLRTTDSNLVLYKRKVDKVGYVVVVLNFSDEPQSLAAIKQQFPGADDRLQVVASSKLVTIKDNKWINVADTELPGESAIVLQKLWGPNPVVVYEA

[Multiple Choices]
A. 35.0
B. 32
C. 66
D. 49
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

> The sequence-matched UniProt record reports an optimum temperature of 35.0 °C, with experimental evidence attributed to PubMed 25746591, supporting choice A. The cited annotation is evidence about the measured optimum, not merely a computational prediction; the underlying study was not independently reviewed here.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic segment is consistent with a signal peptide, and transferable knowledge about secreted enzymes from organisms living in moderate environments could favor temperatures in the low-to-mid 30s over 49 or 66 °C. That general inference does not meaningfully distinguish 35 from 32 °C.


**Missing item-specific fact**

> The measured temperature optimum of this particular protein, reported as 35.0 °C.


**Reason**

> The sequence may support a broad moderate-temperature expectation, but the offered choices include two close values that such a general expectation cannot reliably resolve. Selecting 35 rather than 32 requires a protein-specific measurement or equivalent exact annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> From the supplied sequence alone, both 35.0 and 32 °C are plausible low-to-mid-30s optima; the question gives no context or transferable feature that separates them. The cited measurement supports A, but that fact was not in the original input.


### Important caveats

- The reviewer-only evidence matches the supplied sequence, but the author's exact source snapshot is unknown.
- The reported optimum is an experimental annotation attributed to a cited publication; that publication was not independently assessed.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a signal peptide, and transferable knowledge about secreted enzymes from organisms living in moderate environments could favor temperatures in the low-to-mid 30s over 49 or 66 °C. That general inference does not meaningfully distinguish 35 from 32 °C.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The measured temperature optimum of this particular protein, reported as 35.0 °C.",
    "reason": "The sequence may support a broad moderate-temperature expectation, but the offered choices include two close values that such a general expectation cannot reliably resolve. Selecting 35 rather than 32 requires a protein-specific measurement or equivalent exact annotation."
  },
  "case_id": "temperature_0019",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports an optimum temperature of 35.0 °C, with experimental evidence attributed to PubMed 25746591, supporting choice A. The cited annotation is evidence about the measured optimum, not merely a computational prediction; the underlying study was not independently reviewed here."
  },
  "important_caveats": [
    "The reviewer-only evidence matches the supplied sequence, but the author's exact source snapshot is unknown.",
    "The reported optimum is an experimental annotation attributed to a cited publication; that publication was not independently assessed."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "From the supplied sequence alone, both 35.0 and 32 °C are plausible low-to-mid-30s optima; the question gives no context or transferable feature that separates them. The cited measurement supports A, but that fact was not in the original input."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "temperature_0019",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports an optimum temperature of 35.0 °C, with experimental evidence attributed to PubMed 25746591, supporting choice A. The cited annotation is evidence about the measured optimum, not merely a computational prediction; the underlying study was not independently reviewed here.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a signal peptide, and transferable knowledge about secreted enzymes from organisms living in moderate environments could favor temperatures in the low-to-mid 30s over 49 or 66 °C. That general inference does not meaningfully distinguish 35 from 32 °C.",
    "missing_item_specific_fact": "The measured temperature optimum of this particular protein, reported as 35.0 °C.",
    "reason": "The sequence may support a broad moderate-temperature expectation, but the offered choices include two close values that such a general expectation cannot reliably resolve. Selecting 35 rather than 32 requires a protein-specific measurement or equivalent exact annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "From the supplied sequence alone, both 35.0 and 32 °C are plausible low-to-mid-30s optima; the question gives no context or transferable feature that separates them. The cited measurement supports A, but that fact was not in the original input."
  },
  "important_caveats": [
    "The reviewer-only evidence matches the supplied sequence, but the author's exact source snapshot is unknown.",
    "The reported optimum is an experimental annotation attributed to a cited publication; that publication was not independently assessed."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry B0XAA1 (Salivary alpha-glucosidase from Culex quinquefasciatus) explicitly states 'Optimum temperature is 35.0 degrees Celsius' based on experimental evidence (ECO:0000269, PubMed:25746591). The benchmark sequence matches the source sequence exactly (SHA256 confirmed). The answer 35.0 is a directly reported experimental measurement.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A model could reasonably eliminate C (66°C) and D (49°C) by recognizing the sequence as a secreted glycosidase (signal peptide, GH31-like architecture) from an ectothermic organism, where optimal temperatures cluster around 25-40°C. However, distinguishing A (35.0) from B (32) requires the specific experimental measurement for this exact protein. No sequence composition feature, family-level property of alpha-glucosidases, or general biological principle reliably predicts a 3°C difference in optimal temperature between two otherwise similar mesophilic enzymes. Both 32 and 35 fall squarely within the expected range for insect salivary enzymes.


**Missing item-specific fact**

> The experimentally determined optimum temperature of 35.0°C for this specific Culex quinquefasciatus salivary alpha-glucosidase (PubMed:25746591), which cannot be inferred from sequence composition or family-level properties to distinguish it from 32°C.


**Reason**

> While family and organism-level knowledge eliminates the thermophilic options (66, 49), the critical distinction between 35.0 and 32 requires the specific experimental measurement recorded for this protein. No transferable sequence feature or biological principle predicts whether an insect alpha-glucosidase has a 32°C versus 35°C optimum.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Both 35.0°C and 32°C fall within the normal operating range for insect salivary enzymes and cannot be distinguished by any known sequence-based or family-level criterion. A knowledgeable model recognizing this as a mesophilic insect glycosidase would find both A and B equally plausible without the specific experimental datum.


### Important caveats

- The system message describes the task as predicting a 'thermal adaptation category' but the answer choices are specific numerical temperatures, creating a mismatch between the stated task and the actual question format.
- The formatting of '35.0' (with decimal) versus integers '32', '66', '49' may serve as a meta-clue but is not a biological argument.
- The experimental optimum of 35°C was measured for the recombinant protein (PubMed:25746591); the native protein's in vivo operating temperature may differ.
- The protein is active from 30 to 60°C, meaning 35°C is the peak but the enzyme functions across a broad range; the question asks for optimum specifically.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A model could reasonably eliminate C (66°C) and D (49°C) by recognizing the sequence as a secreted glycosidase (signal peptide, GH31-like architecture) from an ectothermic organism, where optimal temperatures cluster around 25-40°C. However, distinguishing A (35.0) from B (32) requires the specific experimental measurement for this exact protein. No sequence composition feature, family-level property of alpha-glucosidases, or general biological principle reliably predicts a 3°C difference in optimal temperature between two otherwise similar mesophilic enzymes. Both 32 and 35 fall squarely within the expected range for insect salivary enzymes.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The experimentally determined optimum temperature of 35.0°C for this specific Culex quinquefasciatus salivary alpha-glucosidase (PubMed:25746591), which cannot be inferred from sequence composition or family-level properties to distinguish it from 32°C.",
    "reason": "While family and organism-level knowledge eliminates the thermophilic options (66, 49), the critical distinction between 35.0 and 32 requires the specific experimental measurement recorded for this protein. No transferable sequence feature or biological principle predicts whether an insect alpha-glucosidase has a 32°C versus 35°C optimum."
  },
  "case_id": "temperature_0019",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry B0XAA1 (Salivary alpha-glucosidase from Culex quinquefasciatus) explicitly states 'Optimum temperature is 35.0 degrees Celsius' based on experimental evidence (ECO:0000269, PubMed:25746591). The benchmark sequence matches the source sequence exactly (SHA256 confirmed). The answer 35.0 is a directly reported experimental measurement."
  },
  "important_caveats": [
    "The system message describes the task as predicting a 'thermal adaptation category' but the answer choices are specific numerical temperatures, creating a mismatch between the stated task and the actual question format.",
    "The formatting of '35.0' (with decimal) versus integers '32', '66', '49' may serve as a meta-clue but is not a biological argument.",
    "The experimental optimum of 35°C was measured for the recombinant protein (PubMed:25746591); the native protein's in vivo operating temperature may differ.",
    "The protein is active from 30 to 60°C, meaning 35°C is the peak but the enzyme functions across a broad range; the question asks for optimum specifically."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Both 35.0°C and 32°C fall within the normal operating range for insect salivary enzymes and cannot be distinguished by any known sequence-based or family-level criterion. A knowledgeable model recognizing this as a mesophilic insect glycosidase would find both A and B equally plausible without the specific experimental datum."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "temperature_0019",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry B0XAA1 (Salivary alpha-glucosidase from Culex quinquefasciatus) explicitly states 'Optimum temperature is 35.0 degrees Celsius' based on experimental evidence (ECO:0000269, PubMed:25746591). The benchmark sequence matches the source sequence exactly (SHA256 confirmed). The answer 35.0 is a directly reported experimental measurement.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A model could reasonably eliminate C (66°C) and D (49°C) by recognizing the sequence as a secreted glycosidase (signal peptide, GH31-like architecture) from an ectothermic organism, where optimal temperatures cluster around 25-40°C. However, distinguishing A (35.0) from B (32) requires the specific experimental measurement for this exact protein. No sequence composition feature, family-level property of alpha-glucosidases, or general biological principle reliably predicts a 3°C difference in optimal temperature between two otherwise similar mesophilic enzymes. Both 32 and 35 fall squarely within the expected range for insect salivary enzymes.",
    "missing_item_specific_fact": "The experimentally determined optimum temperature of 35.0°C for this specific Culex quinquefasciatus salivary alpha-glucosidase (PubMed:25746591), which cannot be inferred from sequence composition or family-level properties to distinguish it from 32°C.",
    "reason": "While family and organism-level knowledge eliminates the thermophilic options (66, 49), the critical distinction between 35.0 and 32 requires the specific experimental measurement recorded for this protein. No transferable sequence feature or biological principle predicts whether an insect alpha-glucosidase has a 32°C versus 35°C optimum."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Both 35.0°C and 32°C fall within the normal operating range for insect salivary enzymes and cannot be distinguished by any known sequence-based or family-level criterion. A knowledgeable model recognizing this as a mesophilic insect glycosidase would find both A and B equally plausible without the specific experimental datum."
  },
  "important_caveats": [
    "The system message describes the task as predicting a 'thermal adaptation category' but the answer choices are specific numerical temperatures, creating a mismatch between the stated task and the actual question format.",
    "The formatting of '35.0' (with decimal) versus integers '32', '66', '49' may serve as a meta-clue but is not a biological argument.",
    "The experimental optimum of 35°C was measured for the recombinant protein (PubMed:25746591); the native protein's in vivo operating temperature may differ.",
    "The protein is active from 30 to 60°C, meaning 35°C is the peak but the enzyme functions across a broad range; the question asks for optimum specifically."
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
  "benchmark_sequence_length": 584,
  "benchmark_sequence_sha256": "29d6b8000e7795f6bbd083f2568cece3ab8850588bc2d1c4dda913580b5b41a1",
  "current_entry_audit": {
    "entryVersion": 94,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2008-04-08",
    "sequenceVersion": 1
  },
  "current_record_sha256": "9afccd0935d9c913183f609d3d8afcc2196f79187f5d0532d2ba6ed0e5048c10",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 584,
  "current_source_sequence_sha256": "29d6b8000e7795f6bbd083f2568cece3ab8850588bc2d1c4dda913580b5b41a1",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 92,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "B0XAA1",
  "selected_historical_entry_version": 92,
  "selected_historical_record_sha256": "5fda9ac6361a740657451da46434a8060a2e37043092db9553e846bf116af583",
  "selected_historical_source_sequence_length": 584,
  "selected_historical_source_sequence_sha256": "29d6b8000e7795f6bbd083f2568cece3ab8850588bc2d1c4dda913580b5b41a1",
  "selected_historical_version": {
    "accession": "B0XAA1",
    "database": "Swiss-Prot",
    "entryVersion": 92,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MALT_CULQU",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0XAA1.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"B0XAA1\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:27:15.565561+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9afccd0935d9c913183f609d3d8afcc2196f79187f5d0532d2ba6ed0e5048c10",
  "url": "https://rest.uniprot.org/uniprotkb/B0XAA1.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0XAA1.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":94,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2008-04-08\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:27:15.565561+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9afccd0935d9c913183f609d3d8afcc2196f79187f5d0532d2ba6ed0e5048c10",
  "url": "https://rest.uniprot.org/uniprotkb/B0XAA1.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0XAA1.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Southern house mosquito\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Aparaglossata\",\"Panorpida\",\"Diptera\",\"Nematocera\",\"Culicoidea\",\"Culicidae\",\"Culicinae\",\"Culicini\",\"Culex\",\"Culex\"],\"scientificName\":\"Culex quinquefasciatus\",\"synonyms\":[\"Culex pungens\"],\"taxonId\":7176}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:27:15.565561+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9afccd0935d9c913183f609d3d8afcc2196f79187f5d0532d2ba6ed0e5048c10",
  "url": "https://rest.uniprot.org/uniprotkb/B0XAA1.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0XAA1.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"25746591\",\"source\":\"PubMed\"}],\"value\":\"CQMalI\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"25746591\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38428508\",\"source\":\"PubMed\"}],\"value\":\"3.2.1.20\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38428508\",\"source\":\"PubMed\"}],\"value\":\"Salivary alpha-glucosidase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38428508\",\"source\":\"PubMed\"}],\"value\":\"CxGluc\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:27:15.565561+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9afccd0935d9c913183f609d3d8afcc2196f79187f5d0532d2ba6ed0e5048c10",
  "url": "https://rest.uniprot.org/uniprotkb/B0XAA1.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0XAA1.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"BIOPHYSICOCHEMICAL PROPERTIES\",\"kineticParameters\":{\"michaelisConstants\":[{\"constant\":41.1,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38428508\",\"source\":\"PubMed\"}],\"substrate\":\"sucrose\",\"unit\":\"mM\"},{\"constant\":7.74,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"25746591\",\"source\":\"PubMed\"}],\"substrate\":\"sucrose\",\"unit\":\"mM\"},{\"constant\":35.7,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"25746591\",\"source\":\"PubMed\"}],\"substrate\":\"maltose\",\"unit\":\"mM\"},{\"constant\":2.18,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"25746591\",\"source\":\"PubMed\"}],\"substrate\":\"maltotriose\",\"unit\":\"mM\"},{\"constant\":4.21,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"25746591\",\"source\":\"PubMed\"}],\"substrate\":\"maltotetraose\",\"unit\":\"mM\"},{\"constant\":3.9,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"25746591\",\"source\":\"PubMed\"}],\"substrate\":\"p-nitrophenyl-alpha-d-glucoside\",\"unit\":\"mM\"}],\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"25746591\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38428508\",\"source\":\"PubMed\"}],\"value\":\"kcat is 45.0 min(-1) with sucrose as substrate (PubMed:38428508). kcat is 329 sec(-1) with sucrose as substrate (PubMed:25746591). kcat is 84 sec(-1) with maltose as substrate (PubMed:25746591). kcat is 320 sec(-1) with maltotriose as substrate (PubMed:25746591). kcat is 146 sec(-1) with maltotetraose as substrate (PubMed:25746591). kcat is 45 sec(-1) with p-nitrophenyl-alpha-d-glucoside as substrate (PubMed:25746591).\"}]}},\"phDependence\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"25746591\",\"source\":\"PubMed\"}],\"value\":\"Optimum pH is 5.5 (PubMed:25746591). Active from pH 3.0 to 8.0 (PubMed:25746591).\"}]},\"temperatureDependence\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"25746591\",\"source\":\"PubMed\"}],\"value\":\"Optimum temperature is 35.0 degrees Celsius (PubMed:25746591). Active from 30 to 60 degrees Celsius (PubMed:25746591).\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:27:15.565561+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9afccd0935d9c913183f609d3d8afcc2196f79187f5d0532d2ba6ed0e5048c10",
  "url": "https://rest.uniprot.org/uniprotkb/B0XAA1.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0XAA1.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Suthangkornkul R.\",\"Sirichaiyakul P.\",\"Sungvornyothin S.\",\"Thepouyporn A.\",\"Svasti J.\",\"Arthan D.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"25746591\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.pep.2015.02.018\"}],\"citationType\":\"journal article\",\"firstPage\":\"145\",\"id\":\"25746591\",\"journal\":\"Protein Expr. Purif.\",\"lastPage\":\"150\",\"publicationDate\":\"2015\",\"title\":\"Functional expression and molecular characterization of Culex quinquefasciatus salivary alpha-glucosidase (MalI).\",\"volume\":\"110\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"GLYCOSYLATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:27:15.565561+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9afccd0935d9c913183f609d3d8afcc2196f79187f5d0532d2ba6ed0e5048c10",
  "url": "https://rest.uniprot.org/uniprotkb/B0XAA1.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0XAA1.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Williams A.E.\",\"Gittis A.G.\",\"Botello K.\",\"Cruz P.\",\"Martin-Martin I.\",\"Valenzuela Leon P.C.\",\"Sumner B.\",\"Bonilla B.\",\"Calvo E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38428508\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.ibmb.2024.104097\"}],\"citationType\":\"journal article\",\"firstPage\":\"104097\",\"id\":\"38428508\",\"journal\":\"Insect Biochem. Mol. Biol.\",\"lastPage\":\"104097\",\"publicationDate\":\"2024\",\"title\":\"Structural and functional comparisons of salivary alpha-glucosidases from the mosquito vectors Aedes aegypti, Anopheles gambiae, and Culex quinquefasciatus.\",\"volume\":\"167\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBCELLULAR LOCATION\",\"TISSUE SPECIFICITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:27:15.565561+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9afccd0935d9c913183f609d3d8afcc2196f79187f5d0532d2ba6ed0e5048c10",
  "url": "https://rest.uniprot.org/uniprotkb/B0XAA1.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0XAA1?format=txt&versions=92)

```json
{
  "entry_version": 92,
  "evidence_id": "H1",
  "excerpt": "ID   MALT_CULQU              Reviewed;         584 AA.\nAC   B0XAA1;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   08-APR-2008, sequence version 1.\nDT   28-JAN-2026, entry version 92.\nDE   RecName: Full=Salivary alpha-glucosidase {ECO:0000303|PubMed:38428508};\nDE            Short=CxGluc {ECO:0000303|PubMed:38428508};\nDE            EC=3.2.1.20 {ECO:0000269|PubMed:25746591, ECO:0000269|PubMed:38428508};\nDE   AltName: Full=CQMalI {ECO:0000303|PubMed:25746591};\nDE   Flags: Precursor;\nGN   Name=MAL1 {ECO:0000303|PubMed:25746591};\nGN   ORFNames=CpipJ_CPIJ016362 {ECO:0000312|EMBL:EDS43598.1};\nOS   Culex quinquefasciatus (Southern house mosquito) (Culex pungens).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Diptera; Nematocera; Culicoidea; Culicidae;\nOC   Culicinae; Culicini; Culex; Culex.\nOX   NCBI_TaxID=7176;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:18.547256+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5fda9ac6361a740657451da46434a8060a2e37043092db9553e846bf116af583",
  "url": "https://rest.uniprot.org/unisave/B0XAA1?format=txt&versions=92"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0XAA1?format=txt&versions=92)

```json
{
  "entry_version": 92,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, BIOPHYSICOCHEMICAL\nRP   PROPERTIES, AND GLYCOSYLATION.\nRX   PubMed=25746591; DOI=10.1016/j.pep.2015.02.018;\nRA   Suthangkornkul R., Sirichaiyakul P., Sungvornyothin S., Thepouyporn A.,\nRA   Svasti J., Arthan D.;\nRT   \"Functional expression and molecular characterization of Culex\nRT   quinquefasciatus salivary alpha-glucosidase (MalI).\";\nRL   Protein Expr. Purif. 110:145-150(2015).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:18.547256+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 32-40",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5fda9ac6361a740657451da46434a8060a2e37043092db9553e846bf116af583",
  "url": "https://rest.uniprot.org/unisave/B0XAA1?format=txt&versions=92"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0XAA1?format=txt&versions=92)

```json
{
  "entry_version": 92,
  "evidence_id": "H3",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, SUBCELLULAR\nRP   LOCATION, AND TISSUE SPECIFICITY.\nRX   PubMed=38428508; DOI=10.1016/j.ibmb.2024.104097;\nRA   Williams A.E., Gittis A.G., Botello K., Cruz P., Martin-Martin I.,\nRA   Valenzuela Leon P.C., Sumner B., Bonilla B., Calvo E.;\nRT   \"Structural and functional comparisons of salivary alpha-glucosidases from\nRT   the mosquito vectors Aedes aegypti, Anopheles gambiae, and Culex\nRT   quinquefasciatus.\";\nRL   Insect Biochem. Mol. Biol. 167:104097-104097(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:18.547256+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 41-50",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5fda9ac6361a740657451da46434a8060a2e37043092db9553e846bf116af583",
  "url": "https://rest.uniprot.org/unisave/B0XAA1?format=txt&versions=92"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0XAA1?format=txt&versions=92)

```json
{
  "entry_version": 92,
  "evidence_id": "H4",
  "excerpt": "CC   -!- BIOPHYSICOCHEMICAL PROPERTIES:\nCC       Kinetic parameters:\nCC         KM=41.1 mM for sucrose {ECO:0000269|PubMed:38428508};\nCC         KM=7.74 mM for sucrose {ECO:0000269|PubMed:25746591};\nCC         KM=35.7 mM for maltose {ECO:0000269|PubMed:25746591};\nCC         KM=2.18 mM for maltotriose {ECO:0000269|PubMed:25746591};\nCC         KM=4.21 mM for maltotetraose {ECO:0000269|PubMed:25746591};\nCC         KM=3.9 mM for p-nitrophenyl-alpha-d-glucoside\nCC         {ECO:0000269|PubMed:25746591};\nCC         Note=kcat is 45.0 min(-1) with sucrose as substrate\nCC         (PubMed:38428508). kcat is 329 sec(-1) with sucrose as substrate\nCC         (PubMed:25746591). kcat is 84 sec(-1) with maltose as substrate\nCC         (PubMed:25746591). kcat is 320 sec(-1) with maltotriose as substrate\nCC         (PubMed:25746591). kcat is 146 sec(-1) with maltotetraose as\nCC         substrate (PubMed:25746591). kcat is 45 sec(-1) with p-nitrophenyl-\nCC         alpha-d-glucoside as substrate (PubMed:25746591).\nCC         {ECO:0000269|PubMed:25746591, ECO:0000269|PubMed:38428508};\nCC       pH dependence:\nCC         Optimum pH is 5.5 (PubMed:25746591). Active from pH 3.0 to 8.0\nCC         (PubMed:25746591). {ECO:0000269|PubMed:25746591};\nCC       Temperature dependence:\nCC         Optimum temperature is 35.0 degrees Celsius (PubMed:25746591). Active\nCC         from 30 to 60 degrees Celsius (PubMed:25746591).\nCC         {ECO:0000269|PubMed:25746591};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:18.547256+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 62-85",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5fda9ac6361a740657451da46434a8060a2e37043092db9553e846bf116af583",
  "url": "https://rest.uniprot.org/unisave/B0XAA1?format=txt&versions=92"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/temperature.json), zero-based source row 19. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
