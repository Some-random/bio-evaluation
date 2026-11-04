# temperature_0012

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/temperature_0012.txt)

**Task:** `temperature`  
**Expected answer:** **D** — 42

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MEKQVQMPEVELNSDHKMPLVGFGTCIPDPIPPLEELATIFLEVIKVGYRHFDTASCYGTEEALGKAVAQAIESGLVNGREEFFITSKLWVEDADQDLILPALKKTLGNLGLDYLDLYLIHMPLRLRQGAEMFKYTKEDFLPFDIKGTWKAMEECSKLGLCKSIGVSNYSCEKLSKLLENATILPAVNQVEMNVVWKQSKLLPFCKEKNIHVSAWSPLLSYGSIWSQNAVMENTVLVDIAASKSKTVAQVALRWIYEQGASFIMRTFNKERMYQNVQIFDWELTQEELDQIQQIPQRRSNLAEAFVHPEGPIKSVEELWDGDL

[Multiple Choices]
A. 29
B. 77
C. 50
D. 42
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

> The exact sequence matches the UniProt record, which reports an optimum temperature of 42°C with experimental evidence (ECO:0000269). This supports choice D, though the underlying study was not independently reviewed here.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> The measured optimum temperature of this protein is 42°C.


**Reason**

> Sequence composition and general knowledge about enzymes may make an extreme value such as 77°C less plausible, but provide no meaningful basis for distinguishing 42°C from the other moderate-temperature choices. The reported optimum is a target-specific measurement.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options are distinct numerical temperatures, and the supplied reviewer evidence reports a specific optimum of 42°C.


### Important caveats

- An enzyme's measured optimum temperature is not identical to a broad thermal-adaptation category, although the choices here are numerical temperatures.
- The database annotation cites experimental evidence, but the primary study was not independently assessed.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The measured optimum temperature of this protein is 42°C.",
    "reason": "Sequence composition and general knowledge about enzymes may make an extreme value such as 77°C less plausible, but provide no meaningful basis for distinguishing 42°C from the other moderate-temperature choices. The reported optimum is a target-specific measurement."
  },
  "case_id": "temperature_0012",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt record, which reports an optimum temperature of 42°C with experimental evidence (ECO:0000269). This supports choice D, though the underlying study was not independently reviewed here."
  },
  "important_caveats": [
    "An enzyme's measured optimum temperature is not identical to a broad thermal-adaptation category, although the choices here are numerical temperatures.",
    "The database annotation cites experimental evidence, but the primary study was not independently assessed."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options are distinct numerical temperatures, and the supplied reviewer evidence reports a specific optimum of 42°C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "temperature_0012",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt record, which reports an optimum temperature of 42°C with experimental evidence (ECO:0000269). This supports choice D, though the underlying study was not independently reviewed here.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "The measured optimum temperature of this protein is 42°C.",
    "reason": "Sequence composition and general knowledge about enzymes may make an extreme value such as 77°C less plausible, but provide no meaningful basis for distinguishing 42°C from the other moderate-temperature choices. The reported optimum is a target-specific measurement."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options are distinct numerical temperatures, and the supplied reviewer evidence reports a specific optimum of 42°C."
  },
  "important_caveats": [
    "An enzyme's measured optimum temperature is not identical to a broad thermal-adaptation category, although the choices here are numerical temperatures.",
    "The database annotation cites experimental evidence, but the primary study was not independently assessed."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A9E7S5B9) for this exact sequence explicitly states 'Optimum temperature is 42 degrees Celsius' with experimental evidence code ECO:0000269 from PubMed:36349266. The sequence matches exactly (SHA-256 confirmed). The answer D (42) is directly supported by the experimental biophysical characterization.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A knowledgeable model could eliminate 77°C (hyperthermophilic, typical of archaea in hydrothermal vents) and 50°C (thermophilic bacteria/archaea) because the sequence shows features of a eukaryotic short-chain dehydrogenase/reductase (SDR) family enzyme with a Rossmann-fold N-terminus and plant-like composition, making extreme-temperature adaptation implausible. However, distinguishing 29°C from 42°C requires the specific experimental optimum-temperature measurement for this exact enzyme. Both values fall within the mesophilic range typical of plant enzymes. General knowledge of SDR family members or tropical plant enzymes does not reliably predict whether a particular plant reductase has a 29°C or 42°C optimum; the difference is within normal experimental variation for mesophilic proteins and is not encoded by a clear, transferable sequence signature.


**Missing item-specific fact**

> The experimentally determined optimum temperature of 42°C for Rhazimal reductase 2 (AsRHR2) from Alstonia scholaris, measured in the 2022 study by Wang et al. (PubMed:36349266). This specific biophysical measurement for this exact protein is not derivable from sequence composition or family-level generalization.


**Reason**

> While 77 and 50 can be eliminated via family/organism-level reasoning (eukaryotic plant SDR enzyme), the remaining choice between 29 and 42 requires the specific experimental optimum-temperature measurement for this protein. No transferable sequence feature or family-level pattern reliably distinguishes a 29°C from a 42°C mesophilic optimum in plant dehydrogenases.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> Both 29°C and 42°C are plausible mesophilic optima for a plant SDR enzyme. Without the specific experimental measurement, a model relying on general plant-enzyme knowledge could reasonably select either value. The system prompt mentions categories like 'cold-adapted, moderate, heat-adapted' but the options are specific temperatures, making the 29-vs-42 distinction effectively a lookup.


### Important caveats

- The UniProt temperature annotation (42°C) is based on a single experimental study (PubMed:36349266, 2022) with evidence code ECO:0000269 (experimental). It represents one measured optimum, not a broad consensus.
- The protein is identified as Rhazimal reductase 2 (AsRHR2) from Alstonia scholaris (Dogbane), a tropical plant. The organism identity was not provided to the evaluated model.
- The question format presents specific temperatures rather than qualitative categories, which increases the precision required and makes sequence-based prediction more challenging.
- The SDR family is found across all thermal ranges, so family membership alone does not narrow the temperature to a specific value within the mesophilic range.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model could eliminate 77°C (hyperthermophilic, typical of archaea in hydrothermal vents) and 50°C (thermophilic bacteria/archaea) because the sequence shows features of a eukaryotic short-chain dehydrogenase/reductase (SDR) family enzyme with a Rossmann-fold N-terminus and plant-like composition, making extreme-temperature adaptation implausible. However, distinguishing 29°C from 42°C requires the specific experimental optimum-temperature measurement for this exact enzyme. Both values fall within the mesophilic range typical of plant enzymes. General knowledge of SDR family members or tropical plant enzymes does not reliably predict whether a particular plant reductase has a 29°C or 42°C optimum; the difference is within normal experimental variation for mesophilic proteins and is not encoded by a clear, transferable sequence signature.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The experimentally determined optimum temperature of 42°C for Rhazimal reductase 2 (AsRHR2) from Alstonia scholaris, measured in the 2022 study by Wang et al. (PubMed:36349266). This specific biophysical measurement for this exact protein is not derivable from sequence composition or family-level generalization.",
    "reason": "While 77 and 50 can be eliminated via family/organism-level reasoning (eukaryotic plant SDR enzyme), the remaining choice between 29 and 42 requires the specific experimental optimum-temperature measurement for this protein. No transferable sequence feature or family-level pattern reliably distinguishes a 29°C from a 42°C mesophilic optimum in plant dehydrogenases."
  },
  "case_id": "temperature_0012",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A9E7S5B9) for this exact sequence explicitly states 'Optimum temperature is 42 degrees Celsius' with experimental evidence code ECO:0000269 from PubMed:36349266. The sequence matches exactly (SHA-256 confirmed). The answer D (42) is directly supported by the experimental biophysical characterization."
  },
  "important_caveats": [
    "The UniProt temperature annotation (42°C) is based on a single experimental study (PubMed:36349266, 2022) with evidence code ECO:0000269 (experimental). It represents one measured optimum, not a broad consensus.",
    "The protein is identified as Rhazimal reductase 2 (AsRHR2) from Alstonia scholaris (Dogbane), a tropical plant. The organism identity was not provided to the evaluated model.",
    "The question format presents specific temperatures rather than qualitative categories, which increases the precision required and makes sequence-based prediction more challenging.",
    "The SDR family is found across all thermal ranges, so family membership alone does not narrow the temperature to a specific value within the mesophilic range."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "Both 29°C and 42°C are plausible mesophilic optima for a plant SDR enzyme. Without the specific experimental measurement, a model relying on general plant-enzyme knowledge could reasonably select either value. The system prompt mentions categories like 'cold-adapted, moderate, heat-adapted' but the options are specific temperatures, making the 29-vs-42 distinction effectively a lookup."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "temperature_0012",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A9E7S5B9) for this exact sequence explicitly states 'Optimum temperature is 42 degrees Celsius' with experimental evidence code ECO:0000269 from PubMed:36349266. The sequence matches exactly (SHA-256 confirmed). The answer D (42) is directly supported by the experimental biophysical characterization.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A knowledgeable model could eliminate 77°C (hyperthermophilic, typical of archaea in hydrothermal vents) and 50°C (thermophilic bacteria/archaea) because the sequence shows features of a eukaryotic short-chain dehydrogenase/reductase (SDR) family enzyme with a Rossmann-fold N-terminus and plant-like composition, making extreme-temperature adaptation implausible. However, distinguishing 29°C from 42°C requires the specific experimental optimum-temperature measurement for this exact enzyme. Both values fall within the mesophilic range typical of plant enzymes. General knowledge of SDR family members or tropical plant enzymes does not reliably predict whether a particular plant reductase has a 29°C or 42°C optimum; the difference is within normal experimental variation for mesophilic proteins and is not encoded by a clear, transferable sequence signature.",
    "missing_item_specific_fact": "The experimentally determined optimum temperature of 42°C for Rhazimal reductase 2 (AsRHR2) from Alstonia scholaris, measured in the 2022 study by Wang et al. (PubMed:36349266). This specific biophysical measurement for this exact protein is not derivable from sequence composition or family-level generalization.",
    "reason": "While 77 and 50 can be eliminated via family/organism-level reasoning (eukaryotic plant SDR enzyme), the remaining choice between 29 and 42 requires the specific experimental optimum-temperature measurement for this protein. No transferable sequence feature or family-level pattern reliably distinguishes a 29°C from a 42°C mesophilic optimum in plant dehydrogenases."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "Both 29°C and 42°C are plausible mesophilic optima for a plant SDR enzyme. Without the specific experimental measurement, a model relying on general plant-enzyme knowledge could reasonably select either value. The system prompt mentions categories like 'cold-adapted, moderate, heat-adapted' but the options are specific temperatures, making the 29-vs-42 distinction effectively a lookup."
  },
  "important_caveats": [
    "The UniProt temperature annotation (42°C) is based on a single experimental study (PubMed:36349266, 2022) with evidence code ECO:0000269 (experimental). It represents one measured optimum, not a broad consensus.",
    "The protein is identified as Rhazimal reductase 2 (AsRHR2) from Alstonia scholaris (Dogbane), a tropical plant. The organism identity was not provided to the evaluated model.",
    "The question format presents specific temperatures rather than qualitative categories, which increases the precision required and makes sequence-based prediction more challenging.",
    "The SDR family is found across all thermal ranges, so family membership alone does not narrow the temperature to a specific value within the mesophilic range."
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
  "benchmark_sequence_length": 323,
  "benchmark_sequence_sha256": "a52baf3a827949bb9338e7931607670fa3ba5ddced33d4a29afc239fba6099af",
  "current_entry_audit": {
    "entryVersion": 14,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2023-05-03",
    "sequenceVersion": 1
  },
  "current_record_sha256": "1c08163802b289b90c328d14948f43d22b2f958ae0fc9ab7cce8f8e6c8cfdb11",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 323,
  "current_source_sequence_sha256": "a52baf3a827949bb9338e7931607670fa3ba5ddced33d4a29afc239fba6099af",
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
  "requested_accession": "A0A9E7S5B9",
  "selected_historical_entry_version": 13,
  "selected_historical_record_sha256": "e4dda31c04daf5f332a19bce2a18fad48f65a392722189ae93f6d3e440e89922",
  "selected_historical_source_sequence_length": 323,
  "selected_historical_source_sequence_sha256": "a52baf3a827949bb9338e7931607670fa3ba5ddced33d4a29afc239fba6099af",
  "selected_historical_version": {
    "accession": "A0A9E7S5B9",
    "database": "Swiss-Prot",
    "entryVersion": 13,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "RHR2_ALSSC",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S5B9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A9E7S5B9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:54.300761+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c08163802b289b90c328d14948f43d22b2f958ae0fc9ab7cce8f8e6c8cfdb11",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S5B9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S5B9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":14,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2023-05-03\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:54.300761+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c08163802b289b90c328d14948f43d22b2f958ae0fc9ab7cce8f8e6c8cfdb11",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S5B9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S5B9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Dogbane\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Apocynaceae\",\"Rauvolfioideae\",\"Alstonieae\",\"Alstonia\"],\"scientificName\":\"Alstonia scholaris\",\"synonyms\":[\"Echites scholaris\"],\"taxonId\":52822}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:54.300761+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c08163802b289b90c328d14948f43d22b2f958ae0fc9ab7cce8f8e6c8cfdb11",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S5B9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S5B9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"value\":\"1.1.1.440\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"value\":\"Rhazimal reductase 2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"value\":\"AsRHR2\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:54.300761+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c08163802b289b90c328d14948f43d22b2f958ae0fc9ab7cce8f8e6c8cfdb11",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S5B9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S5B9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"BIOPHYSICOCHEMICAL PROPERTIES\",\"phDependence\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"value\":\"Optimum pH is 7-8.\"}]},\"temperatureDependence\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"value\":\"Optimum temperature is 42 degrees Celsius.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-01T06:24:54.300761+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c08163802b289b90c328d14948f43d22b2f958ae0fc9ab7cce8f8e6c8cfdb11",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S5B9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S5B9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Wang Z.\",\"Xiao Y.\",\"Wu S.\",\"Chen J.\",\"Li A.\",\"Tatsis E.C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"36349266\"},{\"database\":\"DOI\",\"id\":\"10.1039/d2sc03612f\"}],\"citationType\":\"journal article\",\"firstPage\":\"12389\",\"id\":\"36349266\",\"journal\":\"Chem. Sci.\",\"lastPage\":\"12395\",\"publicationDate\":\"2022\",\"title\":\"Deciphering and reprogramming the cyclization regioselectivity in bifurcation of indole alkaloid biosynthesis.\",\"volume\":\"13\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"URS65386.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:24:54.300761+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1c08163802b289b90c328d14948f43d22b2f958ae0fc9ab7cce8f8e6c8cfdb11",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S5B9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S5B9?format=txt&versions=13)

```json
{
  "entry_version": 13,
  "evidence_id": "H1",
  "excerpt": "ID   RHR2_ALSSC              Reviewed;         323 AA.\nAC   A0A9E7S5B9;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   03-MAY-2023, sequence version 1.\nDT   28-JAN-2026, entry version 13.\nDE   RecName: Full=Rhazimal reductase 2 {ECO:0000303|PubMed:36349266};\nDE            Short=AsRHR2 {ECO:0000303|PubMed:36349266};\nDE            EC=1.1.1.440 {ECO:0000269|PubMed:36349266};\nGN   Name=RHR2 {ECO:0000303|PubMed:36349266};\nOS   Alstonia scholaris (Dogbane) (Echites scholaris).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Alstonieae;\nOC   Alstonia.\nOX   NCBI_TaxID=52822;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:37.410633+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e4dda31c04daf5f332a19bce2a18fad48f65a392722189ae93f6d3e440e89922",
  "url": "https://rest.uniprot.org/unisave/A0A9E7S5B9?format=txt&versions=13"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S5B9?format=txt&versions=13)

```json
{
  "entry_version": 13,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:URS65386.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, PATHWAY, AND\nRP   BIOPHYSICOCHEMICAL PROPERTIES.\nRX   PubMed=36349266; DOI=10.1039/d2sc03612f;\nRA   Wang Z., Xiao Y., Wu S., Chen J., Li A., Tatsis E.C.;\nRT   \"Deciphering and reprogramming the cyclization regioselectivity in\nRT   bifurcation of indole alkaloid biosynthesis.\";\nRL   Chem. Sci. 13:12389-12395(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:37.410633+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 16-23",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e4dda31c04daf5f332a19bce2a18fad48f65a392722189ae93f6d3e440e89922",
  "url": "https://rest.uniprot.org/unisave/A0A9E7S5B9?format=txt&versions=13"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S5B9?format=txt&versions=13)

```json
{
  "entry_version": 13,
  "evidence_id": "H3",
  "excerpt": "CC   -!- BIOPHYSICOCHEMICAL PROPERTIES:\nCC       pH dependence:\nCC         Optimum pH is 7-8. {ECO:0000269|PubMed:36349266};\nCC       Temperature dependence:\nCC         Optimum temperature is 42 degrees Celsius.\nCC         {ECO:0000269|PubMed:36349266};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:37.410633+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 37-42",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e4dda31c04daf5f332a19bce2a18fad48f65a392722189ae93f6d3e440e89922",
  "url": "https://rest.uniprot.org/unisave/A0A9E7S5B9?format=txt&versions=13"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/temperature.json), zero-based source row 12. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
