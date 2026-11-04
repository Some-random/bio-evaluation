# temperature_0007

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/temperature_0007.txt)

**Task:** `temperature`  
**Expected answer:** **B** — 25

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MIAVNSRNSLNADMTSLHPETLMVHGGMKGLTEAGVHVPAIDLSTTNPVNDVATGGDSYEWLATGHTLKDGDSAVYQRLWQPGVARFETALAGLEHAEEAVAFATGMAAMTAALLAAVSAGTPHIVAVRPLYGGSDHLLETGLLGTTVTWAKEADIASAIQDDTGLVIVETPANPSLDLVDLDSVVSAAGNVPVLVDNTFCTPVLQQPISHGAALVLHSATKYLGGHGDAMGGIIATNADWAMRLRQVRAITGALLHPMGAYLLHRGLRTLAVRMRAAQTTAGELAERLDAHPAISVVHYPGLKGQDPRGLLGRQMSGGGAMIAMELAGGFDAARSFVEHCNLVVHAVSLGGADTLIQHPASLTHRPVAATAKPGDGLIRLSVGLEHVDDLADDLIAALDASRAAA

[Multiple Choices]
A. 30
B. 25
C. 31
D. 41-53
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

> The sequence matches the reviewed record, which reports an optimum temperature of 25 °C with experimental evidence. This supports choice B for the property asked.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Sequence or enzyme-family knowledge could support a broad expectation of moderate-temperature function and make 41–53 less likely. But that does not meaningfully distinguish an optimum of 25 °C from 30 or 31 °C.


**Missing item-specific fact**

> The measured optimum temperature for this exact protein is needed to distinguish 25 °C from the nearby numerical choices.


**Reason**

> The key is supported by a target-specific experimental annotation, but the sequence and transferable biological patterns do not resolve the close alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices are distinct numerical values, and the supplied reviewer evidence reports 25 °C as the optimum; it does not establish multiple correct values.


### Important caveats

- The experimental temperature annotation is reviewer-only and was not part of the original inputs.
- The evidence supports the reported optimum; it does not make the exact value inferable from sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Sequence or enzyme-family knowledge could support a broad expectation of moderate-temperature function and make 41–53 less likely. But that does not meaningfully distinguish an optimum of 25 °C from 30 or 31 °C.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The measured optimum temperature for this exact protein is needed to distinguish 25 °C from the nearby numerical choices.",
    "reason": "The key is supported by a target-specific experimental annotation, but the sequence and transferable biological patterns do not resolve the close alternatives."
  },
  "case_id": "temperature_0007",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the reviewed record, which reports an optimum temperature of 25 °C with experimental evidence. This supports choice B for the property asked."
  },
  "important_caveats": [
    "The experimental temperature annotation is reviewer-only and was not part of the original inputs.",
    "The evidence supports the reported optimum; it does not make the exact value inferable from sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices are distinct numerical values, and the supplied reviewer evidence reports 25 °C as the optimum; it does not establish multiple correct values."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "temperature_0007",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the reviewed record, which reports an optimum temperature of 25 °C with experimental evidence. This supports choice B for the property asked.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Sequence or enzyme-family knowledge could support a broad expectation of moderate-temperature function and make 41–53 less likely. But that does not meaningfully distinguish an optimum of 25 °C from 30 or 31 °C.",
    "missing_item_specific_fact": "The measured optimum temperature for this exact protein is needed to distinguish 25 °C from the nearby numerical choices.",
    "reason": "The key is supported by a target-specific experimental annotation, but the sequence and transferable biological patterns do not resolve the close alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices are distinct numerical values, and the supplied reviewer evidence reports 25 °C as the optimum; it does not establish multiple correct values."
  },
  "important_caveats": [
    "The experimental temperature annotation is reviewer-only and was not part of the original inputs.",
    "The evidence supports the reported optimum; it does not make the exact value inferable from sequence alone."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A2H1K3G9, L-methionine gamma-lyase from Brevibacterium aurantiacum) explicitly states under BIOPHYSICOCHEMICAL PROPERTIES: 'Optimum temperature is 25 degrees Celsius. Is active between 5 and 50 degrees Celsius.' This is an experimentally determined value (ECO:0000269, PubMed:9726878, Dias & Weimer 1998). The expected answer of 25°C is directly supported by primary experimental evidence.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One could argue from sequence composition that this PLP-dependent enzyme (Class I aminotransferase family) lacks thermophilic signatures (excess salt bridges, high proline content, reduced thermolabile residues), which would reasonably rule out option D (41-53°C). However, distinguishing among the three remaining mesophilic options—25, 30, and 31°C—requires the specific experimental measurement. No established sequence-composition principle, family-level inference, or transferable biological knowledge can meaningfully separate a 25°C optimum from a 30°C or 31°C optimum. These values fall within the same mesophilic range and do not correspond to any known amino acid signature threshold. The organism identity (Brevibacterium aurantiacum, a dairy-associated mesophile) is not provided in the input, and even if recognized, the specific 25°C value is a single experimental data point from one publication.


**Missing item-specific fact**

> The experimentally determined optimal temperature of 25°C for this exact L-methionine gamma-lyase (from Dias & Weimer, 1998, PubMed:9726878), which is a single measurement that cannot be distinguished from 30°C or 31°C by any sequence-based or family-level reasoning.


**Reason**

> While sequence features can plausibly rule out the thermophilic option D (41-53°C), the three remaining options (25, 30, 31) are all within the narrow mesophilic range and are indistinguishable by any known transferable biological principle. The correct answer depends on a specific experimental measurement for this exact protein, not on a generalizable pattern.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B",
  "C"
]
```

> Options A (30), B (25), and C (31) all represent mesophilic temperatures that are consistent with the sequence composition of this PLP-dependent enzyme. No sequence-based criterion or family-level knowledge can reliably distinguish among these three values. Only option D (41-53°C) is clearly distinguishable as thermophilic based on the absence of thermophilic sequence signatures.


### Important caveats

- The original input provides only the protein sequence; organism name, taxonomy, and ecological context are not given to the evaluated model.
- The 25°C optimum is a single experimental measurement from one 1998 paper; the enzyme is active between 5-50°C, so the 'optimum' is a peak of a broad activity curve.
- The question format asks for a specific temperature number rather than a broad category (cold/moderate/hot), making the distinction between 25, 30, and 31 essentially a precision requirement that exceeds what sequence-based inference can provide.
- The system prompt describes the task as predicting a 'thermal adaptation category' (cold/moderate/heat), but the options are specific numbers, creating a mismatch between the described task and the actual question format.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One could argue from sequence composition that this PLP-dependent enzyme (Class I aminotransferase family) lacks thermophilic signatures (excess salt bridges, high proline content, reduced thermolabile residues), which would reasonably rule out option D (41-53°C). However, distinguishing among the three remaining mesophilic options—25, 30, and 31°C—requires the specific experimental measurement. No established sequence-composition principle, family-level inference, or transferable biological knowledge can meaningfully separate a 25°C optimum from a 30°C or 31°C optimum. These values fall within the same mesophilic range and do not correspond to any known amino acid signature threshold. The organism identity (Brevibacterium aurantiacum, a dairy-associated mesophile) is not provided in the input, and even if recognized, the specific 25°C value is a single experimental data point from one publication.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The experimentally determined optimal temperature of 25°C for this exact L-methionine gamma-lyase (from Dias & Weimer, 1998, PubMed:9726878), which is a single measurement that cannot be distinguished from 30°C or 31°C by any sequence-based or family-level reasoning.",
    "reason": "While sequence features can plausibly rule out the thermophilic option D (41-53°C), the three remaining options (25, 30, 31) are all within the narrow mesophilic range and are indistinguishable by any known transferable biological principle. The correct answer depends on a specific experimental measurement for this exact protein, not on a generalizable pattern."
  },
  "case_id": "temperature_0007",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A2H1K3G9, L-methionine gamma-lyase from Brevibacterium aurantiacum) explicitly states under BIOPHYSICOCHEMICAL PROPERTIES: 'Optimum temperature is 25 degrees Celsius. Is active between 5 and 50 degrees Celsius.' This is an experimentally determined value (ECO:0000269, PubMed:9726878, Dias & Weimer 1998). The expected answer of 25°C is directly supported by primary experimental evidence."
  },
  "important_caveats": [
    "The original input provides only the protein sequence; organism name, taxonomy, and ecological context are not given to the evaluated model.",
    "The 25°C optimum is a single experimental measurement from one 1998 paper; the enzyme is active between 5-50°C, so the 'optimum' is a peak of a broad activity curve.",
    "The question format asks for a specific temperature number rather than a broad category (cold/moderate/hot), making the distinction between 25, 30, and 31 essentially a precision requirement that exceeds what sequence-based inference can provide.",
    "The system prompt describes the task as predicting a 'thermal adaptation category' (cold/moderate/heat), but the options are specific numbers, creating a mismatch between the described task and the actual question format."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B",
      "C"
    ],
    "reason": "Options A (30), B (25), and C (31) all represent mesophilic temperatures that are consistent with the sequence composition of this PLP-dependent enzyme. No sequence-based criterion or family-level knowledge can reliably distinguish among these three values. Only option D (41-53°C) is clearly distinguishable as thermophilic based on the absence of thermophilic sequence signatures."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "temperature_0007",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A2H1K3G9, L-methionine gamma-lyase from Brevibacterium aurantiacum) explicitly states under BIOPHYSICOCHEMICAL PROPERTIES: 'Optimum temperature is 25 degrees Celsius. Is active between 5 and 50 degrees Celsius.' This is an experimentally determined value (ECO:0000269, PubMed:9726878, Dias & Weimer 1998). The expected answer of 25°C is directly supported by primary experimental evidence.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One could argue from sequence composition that this PLP-dependent enzyme (Class I aminotransferase family) lacks thermophilic signatures (excess salt bridges, high proline content, reduced thermolabile residues), which would reasonably rule out option D (41-53°C). However, distinguishing among the three remaining mesophilic options—25, 30, and 31°C—requires the specific experimental measurement. No established sequence-composition principle, family-level inference, or transferable biological knowledge can meaningfully separate a 25°C optimum from a 30°C or 31°C optimum. These values fall within the same mesophilic range and do not correspond to any known amino acid signature threshold. The organism identity (Brevibacterium aurantiacum, a dairy-associated mesophile) is not provided in the input, and even if recognized, the specific 25°C value is a single experimental data point from one publication.",
    "missing_item_specific_fact": "The experimentally determined optimal temperature of 25°C for this exact L-methionine gamma-lyase (from Dias & Weimer, 1998, PubMed:9726878), which is a single measurement that cannot be distinguished from 30°C or 31°C by any sequence-based or family-level reasoning.",
    "reason": "While sequence features can plausibly rule out the thermophilic option D (41-53°C), the three remaining options (25, 30, 31) are all within the narrow mesophilic range and are indistinguishable by any known transferable biological principle. The correct answer depends on a specific experimental measurement for this exact protein, not on a generalizable pattern."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B", "C"],
    "reason": "Options A (30), B (25), and C (31) all represent mesophilic temperatures that are consistent with the sequence composition of this PLP-dependent enzyme. No sequence-based criterion or family-level knowledge can reliably distinguish among these three values. Only option D (41-53°C) is clearly distinguishable as thermophilic based on the absence of thermophilic sequence signatures."
  },
  "important_caveats": [
    "The original input provides only the protein sequence; organism name, taxonomy, and ecological context are not given to the evaluated model.",
    "The 25°C optimum is a single experimental measurement from one 1998 paper; the enzyme is active between 5-50°C, so the 'optimum' is a peak of a broad activity curve.",
    "The question format asks for a specific temperature number rather than a broad category (cold/moderate/hot), making the distinction between 25, 30, and 31 essentially a precision requirement that exceeds what sequence-based inference can provide.",
    "The system prompt describes the task as predicting a 'thermal adaptation category' (cold/moderate/heat), but the options are specific numbers, creating a mismatch between the described task and the actual question format."
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
  "benchmark_sequence_length": 406,
  "benchmark_sequence_sha256": "435ffd3b8e0f97253809f6299a192824acbc91b3f9ba8e80c96d087a48e0a9a8",
  "current_entry_audit": {
    "entryVersion": 34,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2018-01-31",
    "sequenceVersion": 1
  },
  "current_record_sha256": "a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 406,
  "current_source_sequence_sha256": "435ffd3b8e0f97253809f6299a192824acbc91b3f9ba8e80c96d087a48e0a9a8",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 32,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A2H1K3G9",
  "selected_historical_entry_version": 32,
  "selected_historical_record_sha256": "9f8f2097c25cd1b2756007ac83a5f1a172b3bde4aa3f977e22144a88c5ee6f0b",
  "selected_historical_source_sequence_length": 406,
  "selected_historical_source_sequence_sha256": "435ffd3b8e0f97253809f6299a192824acbc91b3f9ba8e80c96d087a48e0a9a8",
  "selected_historical_version": {
    "accession": "A0A2H1K3G9",
    "database": "Swiss-Prot",
    "entryVersion": 32,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MEGL_BREAU",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A2H1K3G9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:44.554855+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":34,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2018-01-31\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:44.554855+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Bacillati\",\"Actinomycetota\",\"Actinomycetes\",\"Micrococcales\",\"Brevibacteriaceae\",\"Brevibacterium\"],\"scientificName\":\"Brevibacterium aurantiacum\",\"taxonId\":273384}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:44.554855+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30940696\",\"source\":\"PubMed\"}],\"value\":\"4.4.1.2\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30940696\",\"source\":\"PubMed\"}],\"value\":\"Homocysteine desulfhydrase\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30940696\",\"source\":\"PubMed\"}],\"value\":\"MGL-BL929\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30940696\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"9726878\",\"source\":\"PubMed\"}],\"value\":\"4.4.1.11\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30940696\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"9726878\",\"source\":\"PubMed\"}],\"value\":\"L-methionine gamma-lyase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30940696\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"9726878\",\"source\":\"PubMed\"}],\"value\":\"MGL\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:44.554855+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"BIOPHYSICOCHEMICAL PROPERTIES\",\"kineticParameters\":{\"maximumVelocities\":[{\"enzyme\":\"enzyme with L-methionine as substrate\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"9726878\",\"source\":\"PubMed\"}],\"unit\":\"umol/min/mg\",\"velocity\":7.0}],\"michaelisConstants\":[{\"constant\":6.12,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"9726878\",\"source\":\"PubMed\"}],\"substrate\":\"L-methionine\",\"unit\":\"mM\"},{\"constant\":6.83,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30940696\",\"source\":\"PubMed\"}],\"substrate\":\"L-methionine\",\"unit\":\"mM\"},{\"constant\":0.94,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30940696\",\"source\":\"PubMed\"}],\"substrate\":\"L-homocysteine\",\"unit\":\"mM\"}],\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30940696\",\"source\":\"PubMed\"}],\"value\":\"kcat is 15.51 sec(-1) with L-methionine as substrate. kcat is 72.44 sec(-1) with L-homocysteine as substrate.\"}]}},\"phDependence\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"9726878\",\"source\":\"PubMed\"}],\"value\":\"Optimum pH is 7.5. Is stable at pHs ranging from 6.0 to 8.0 for 24 hours.\"}]},\"temperatureDependence\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"9726878\",\"source\":\"PubMed\"}],\"value\":\"Optimum temperature is 25 degrees Celsius. Is active between 5 and 50 degrees Celsius.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/5",
  "retrieved_utc": "2026-11-01T06:24:44.554855+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Dias B.\",\"Weimer B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"9726878\"},{\"database\":\"DOI\",\"id\":\"10.1128/aem.64.9.3327-3331.1998\"}],\"citationType\":\"journal article\",\"firstPage\":\"3327\",\"id\":\"9726878\",\"journal\":\"Appl. Environ. Microbiol.\",\"lastPage\":\"3331\",\"publicationDate\":\"1998\",\"title\":\"Purification and characterization of L-methionine gamma-lyase from brevibacterium linens BL2.\",\"volume\":\"64\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"BL2\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"SUBSTRATE SPECIFICITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"ACTIVITY REGULATION\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:24:44.554855+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Machover D.\",\"Rossi L.\",\"Hamelin J.\",\"Desterke C.\",\"Goldschmidt E.\",\"Chadefaux-Vekemans B.\",\"Bonnarme P.\",\"Briozzo P.\",\"Kopecny D.\",\"Pierige F.\",\"Magnani M.\",\"Mollicone R.\",\"Haghighi-Rad F.\",\"Gaston-Mathe Y.\",\"Dairou J.\",\"Boucheix C.\",\"Saffroy R.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30940696\"},{\"database\":\"DOI\",\"id\":\"10.1124/jpet.119.256537\"}],\"citationType\":\"journal article\",\"firstPage\":\"489\",\"id\":\"30940696\",\"journal\":\"J. Pharmacol. Exp. Ther.\",\"lastPage\":\"502\",\"publicationDate\":\"2019\",\"title\":\"Effects in Cancer Cells of the Recombinant L-Methionine Gamma-Lyase from Brevibacterium aurantiacum. Encapsulation in Human Erythrocytes for Sustained L-Methionine Elimination.\",\"volume\":\"369\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC 9175 / DSM 20426 / JCM 2590 / NBRC 12171 / NCDO 739 / NCIMB 8546 / KC\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"SUBSTRATE SPECIFICITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBUNIT\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-01T06:24:44.554855+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H1",
  "excerpt": "ID   MEGL_BREAU              Reviewed;         406 AA.\nAC   A0A2H1K3G9;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   31-JAN-2018, sequence version 1.\nDT   28-JAN-2026, entry version 32.\nDE   RecName: Full=L-methionine gamma-lyase {ECO:0000303|PubMed:30940696, ECO:0000303|PubMed:9726878};\nDE            Short=MGL {ECO:0000303|PubMed:30940696, ECO:0000303|PubMed:9726878};\nDE            EC=4.4.1.11 {ECO:0000269|PubMed:30940696, ECO:0000269|PubMed:9726878};\nDE   AltName: Full=Homocysteine desulfhydrase {ECO:0000303|PubMed:30940696};\nDE            EC=4.4.1.2 {ECO:0000269|PubMed:30940696};\nDE   AltName: Full=MGL-BL929 {ECO:0000303|PubMed:30940696};\nGN   ORFNames=BAUR9175_03070 {ECO:0000312|EMBL:SMX94104.1},\nGN   BAUR920_03040 {ECO:0000312|EMBL:SMX97377.1},\nGN   BAURA63_02933 {ECO:0000312|EMBL:SMX94451.1},\nGN   BAURA86_00394 {ECO:0000312|EMBL:SMX72154.1};\nOS   Brevibacterium aurantiacum.\nOC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Micrococcales;\nOC   Brevibacteriaceae; Brevibacterium.\nOX   NCBI_TaxID=273384;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:25.782043+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-19",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9f8f2097c25cd1b2756007ac83a5f1a172b3bde4aa3f977e22144a88c5ee6f0b",
  "url": "https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, COFACTOR, SUBSTRATE SPECIFICITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, ACTIVITY REGULATION, AND SUBUNIT.\nRC   STRAIN=BL2;\nRX   PubMed=9726878; DOI=10.1128/aem.64.9.3327-3331.1998;\nRA   Dias B., Weimer B.;\nRT   \"Purification and characterization of L-methionine gamma-lyase from\nRT   brevibacterium linens BL2.\";\nRL   Appl. Environ. Microbiol. 64:3327-3331(1998).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:25.782043+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 27-35",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9f8f2097c25cd1b2756007ac83a5f1a172b3bde4aa3f977e22144a88c5ee6f0b",
  "url": "https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H3",
  "excerpt": "RN   [3]\nRP   FUNCTION, CATALYTIC ACTIVITY, COFACTOR, SUBSTRATE SPECIFICITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, SUBUNIT, AND BIOTECHNOLOGY.\nRC   STRAIN=ATCC 9175 / DSM 20426 / JCM 2590 / NBRC 12171 / NCDO 739 / NCIMB\nRC   8546 / KC;\nRX   PubMed=30940696; DOI=10.1124/jpet.119.256537;\nRA   Machover D., Rossi L., Hamelin J., Desterke C., Goldschmidt E.,\nRA   Chadefaux-Vekemans B., Bonnarme P., Briozzo P., Kopecny D., Pierige F.,\nRA   Magnani M., Mollicone R., Haghighi-Rad F., Gaston-Mathe Y., Dairou J.,\nRA   Boucheix C., Saffroy R.;\nRT   \"Effects in Cancer Cells of the Recombinant L-Methionine Gamma-Lyase from\nRT   Brevibacterium aurantiacum. Encapsulation in Human Erythrocytes for\nRT   Sustained L-Methionine Elimination.\";\nRL   J. Pharmacol. Exp. Ther. 369:489-502(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:25.782043+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 36-49",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9f8f2097c25cd1b2756007ac83a5f1a172b3bde4aa3f977e22144a88c5ee6f0b",
  "url": "https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H4",
  "excerpt": "CC   -!- BIOPHYSICOCHEMICAL PROPERTIES:\nCC       Kinetic parameters:\nCC         KM=6.12 mM for L-methionine {ECO:0000269|PubMed:9726878};\nCC         KM=6.83 mM for L-methionine {ECO:0000269|PubMed:30940696};\nCC         KM=0.94 mM for L-homocysteine {ECO:0000269|PubMed:30940696};\nCC         Vmax=7.0 umol/min/mg enzyme with L-methionine as substrate\nCC         {ECO:0000269|PubMed:9726878};\nCC         Note=kcat is 15.51 sec(-1) with L-methionine as substrate. kcat is\nCC         72.44 sec(-1) with L-homocysteine as substrate.\nCC         {ECO:0000269|PubMed:30940696};\nCC       pH dependence:\nCC         Optimum pH is 7.5. Is stable at pHs ranging from 6.0 to 8.0 for 24\nCC         hours. {ECO:0000269|PubMed:9726878};\nCC       Temperature dependence:\nCC         Optimum temperature is 25 degrees Celsius. Is active between 5 and 50\nCC         degrees Celsius. {ECO:0000269|PubMed:9726878};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:25.782043+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 81-96",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9f8f2097c25cd1b2756007ac83a5f1a172b3bde4aa3f977e22144a88c5ee6f0b",
  "url": "https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/temperature.json), zero-based source row 7. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
