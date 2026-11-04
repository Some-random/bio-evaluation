# temperature_0011

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/temperature_0011.txt)

**Task:** `temperature`  
**Expected answer:** **C** — 37

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MEKQVQIPEIELNSGHKMPLVGFGTCVPDPIPPLEELAGIFLEAIKVGYRHFDTASSYGTEEALGRAVAQAIETGLVNGREEFFISSKLWCEDADLDLILPALKKTLGNMGLDYLDLSMIHMPVRVRKGAEMFNYTKEDLLPFDIQGTWKAMEECNKLGLAKSIGVSNYSCEKLTKLLENATVPPAVNQVEMNVVWQQRKLLPFCKEKNIHVTAWSPLLSYGAVWGSNAVMENPILVEIAASKNKTVAQVALRWIYEQGASFIMRTFNKDRMFENVQIFDWELTKEELDKIQKIPQRRGTLGEDFIHPEGPIKSVEDLWDGDL

[Multiple Choices]
A. 60
B. 74
C. 37
D. 62
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

> The sequence-matched UniProt record reports an optimum temperature of 37 °C with experimental evidence (ECO:0000269), matching choice C. This is database-reported experimental evidence, though the cited study was not independently reviewed here.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a soluble globular enzyme rather than a membrane protein, and shows no conspicuous indication of an extreme-temperature adaptation. Transferable biological knowledge gives an ordinary mesophilic enzyme a stronger prior than a protein with an optimum of 60–74 °C, so 37 is meaningfully favored among these choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> This supports a probabilistic distinction between the mesophilic choice and the three high-temperature choices, not an exact prediction of 37 °C. The sequence alone does not establish the measured optimum, and the inference is limited by the absence of source-organism or assay context.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices are distinct numerical temperatures, and the sequence-matched experimental annotation supports 37 °C.


### Important caveats

- The reported optimum is an assay-dependent property and does not by itself fully characterize the protein's thermal stability or adaptation.
- The reviewer-only evidence was not part of the original input and is used only to assess support for the key.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a soluble globular enzyme rather than a membrane protein, and shows no conspicuous indication of an extreme-temperature adaptation. Transferable biological knowledge gives an ordinary mesophilic enzyme a stronger prior than a protein with an optimum of 60–74 °C, so 37 is meaningfully favored among these choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "This supports a probabilistic distinction between the mesophilic choice and the three high-temperature choices, not an exact prediction of 37 °C. The sequence alone does not establish the measured optimum, and the inference is limited by the absence of source-organism or assay context."
  },
  "case_id": "temperature_0011",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports an optimum temperature of 37 °C with experimental evidence (ECO:0000269), matching choice C. This is database-reported experimental evidence, though the cited study was not independently reviewed here."
  },
  "important_caveats": [
    "The reported optimum is an assay-dependent property and does not by itself fully characterize the protein's thermal stability or adaptation.",
    "The reviewer-only evidence was not part of the original input and is used only to assess support for the key."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices are distinct numerical temperatures, and the sequence-matched experimental annotation supports 37 °C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "temperature_0011",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports an optimum temperature of 37 °C with experimental evidence (ECO:0000269), matching choice C. This is database-reported experimental evidence, though the cited study was not independently reviewed here.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a soluble globular enzyme rather than a membrane protein, and shows no conspicuous indication of an extreme-temperature adaptation. Transferable biological knowledge gives an ordinary mesophilic enzyme a stronger prior than a protein with an optimum of 60–74 °C, so 37 is meaningfully favored among these choices.",
    "missing_item_specific_fact": "",
    "reason": "This supports a probabilistic distinction between the mesophilic choice and the three high-temperature choices, not an exact prediction of 37 °C. The sequence alone does not establish the measured optimum, and the inference is limited by the absence of source-organism or assay context."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices are distinct numerical temperatures, and the sequence-matched experimental annotation supports 37 °C."
  },
  "important_caveats": [
    "The reported optimum is an assay-dependent property and does not by itself fully characterize the protein's thermal stability or adaptation.",
    "The reviewer-only evidence was not part of the original input and is used only to assess support for the key."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A9E7S518 (Rhazimal reductase 1 from Alstonia scholaris) contains an experimentally determined annotation (ECO:0000269, PubMed:36349266) stating 'Optimum temperature is 37 degrees Celsius.' The benchmark sequence matches the source sequence (SHA256 confirmed). The expected answer of 37°C is directly supported by experimental evidence.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Among the four choices (37, 60, 62, 74°C), only 37°C falls in the mesophilic range; the other three are thermophilic or hyperthermophilic. Transferable knowledge tells us that thermophilic proteins exhibit distinctive sequence signatures: markedly elevated charged-residue content (especially K, E, R forming salt bridges), increased hydrophobic packing, depletion of thermolabile residues (Cys, Gln, Asn), and increased Pro content. Examining this 323-residue sequence, the amino acid composition is moderate—there is a normal complement of Cys (e.g., 'GFGTC'), no extreme enrichment of charged residues, and no pronounced hydrophobic-core compression typical of thermophiles. The sequence is consistent with a mesophilic enzyme (short-chain dehydrogenase/reductase fold suggested by the N-terminal GxxGxxG-like motif). Since the majority of characterized proteins are mesophilic and this sequence lacks thermophilic signatures, the mesophilic option (37°C) is the only defensible choice among the four. This is a family-level and composition-based inference learned from many thermophilic vs. mesophilic proteins, not a lookup of this protein's specific record.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The key distinction among the offered alternatives is mesophilic (37°C) vs. thermophilic (60, 62, 74°C). A knowledgeable model can use general principles of thermal adaptation (charged-residue enrichment, salt-bridge density, thermolabile-residue depletion in thermophiles) applied to the sequence composition, plus the prior that most proteins are mesophilic, to select 37°C as the only mesophilic option. This does not require recalling the specific experimental measurement for this exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span a clear categorical divide: one mesophilic temperature (37°C) versus three thermophilic/hyperthermophilic temperatures (60, 62, 74°C). Given the absence of thermophilic sequence signatures, 37°C is the uniquely defensible choice. There is no ambiguity among the alternatives for a model applying standard thermal-adaptation reasoning.


### Important caveats

- The experimental optimum of 37°C for a plant enzyme (Alstonia scholaris) is slightly above the typical 25-30°C range for many plant enzymes, but it remains firmly mesophilic and is the only mesophilic option among the choices.
- Distinguishing 60°C from 62°C from sequence alone would be essentially impossible without experimental data; however, this distinction is irrelevant since the correct answer is the mesophilic option.
- The reviewer-only UniProt annotation (experimental, PubMed:36349266) was not available to the evaluated model; the reasoning_supported judgment relies solely on transferable sequence-composition knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Among the four choices (37, 60, 62, 74°C), only 37°C falls in the mesophilic range; the other three are thermophilic or hyperthermophilic. Transferable knowledge tells us that thermophilic proteins exhibit distinctive sequence signatures: markedly elevated charged-residue content (especially K, E, R forming salt bridges), increased hydrophobic packing, depletion of thermolabile residues (Cys, Gln, Asn), and increased Pro content. Examining this 323-residue sequence, the amino acid composition is moderate—there is a normal complement of Cys (e.g., 'GFGTC'), no extreme enrichment of charged residues, and no pronounced hydrophobic-core compression typical of thermophiles. The sequence is consistent with a mesophilic enzyme (short-chain dehydrogenase/reductase fold suggested by the N-terminal GxxGxxG-like motif). Since the majority of characterized proteins are mesophilic and this sequence lacks thermophilic signatures, the mesophilic option (37°C) is the only defensible choice among the four. This is a family-level and composition-based inference learned from many thermophilic vs. mesophilic proteins, not a lookup of this protein's specific record.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The key distinction among the offered alternatives is mesophilic (37°C) vs. thermophilic (60, 62, 74°C). A knowledgeable model can use general principles of thermal adaptation (charged-residue enrichment, salt-bridge density, thermolabile-residue depletion in thermophiles) applied to the sequence composition, plus the prior that most proteins are mesophilic, to select 37°C as the only mesophilic option. This does not require recalling the specific experimental measurement for this exact protein."
  },
  "case_id": "temperature_0011",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A9E7S518 (Rhazimal reductase 1 from Alstonia scholaris) contains an experimentally determined annotation (ECO:0000269, PubMed:36349266) stating 'Optimum temperature is 37 degrees Celsius.' The benchmark sequence matches the source sequence (SHA256 confirmed). The expected answer of 37°C is directly supported by experimental evidence."
  },
  "important_caveats": [
    "The experimental optimum of 37°C for a plant enzyme (Alstonia scholaris) is slightly above the typical 25-30°C range for many plant enzymes, but it remains firmly mesophilic and is the only mesophilic option among the choices.",
    "Distinguishing 60°C from 62°C from sequence alone would be essentially impossible without experimental data; however, this distinction is irrelevant since the correct answer is the mesophilic option.",
    "The reviewer-only UniProt annotation (experimental, PubMed:36349266) was not available to the evaluated model; the reasoning_supported judgment relies solely on transferable sequence-composition knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span a clear categorical divide: one mesophilic temperature (37°C) versus three thermophilic/hyperthermophilic temperatures (60, 62, 74°C). Given the absence of thermophilic sequence signatures, 37°C is the uniquely defensible choice. There is no ambiguity among the alternatives for a model applying standard thermal-adaptation reasoning."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "temperature_0011",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A9E7S518 (Rhazimal reductase 1 from Alstonia scholaris) contains an experimentally determined annotation (ECO:0000269, PubMed:36349266) stating 'Optimum temperature is 37 degrees Celsius.' The benchmark sequence matches the source sequence (SHA256 confirmed). The expected answer of 37°C is directly supported by experimental evidence.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Among the four choices (37, 60, 62, 74°C), only 37°C falls in the mesophilic range; the other three are thermophilic or hyperthermophilic. Transferable knowledge tells us that thermophilic proteins exhibit distinctive sequence signatures: markedly elevated charged-residue content (especially K, E, R forming salt bridges), increased hydrophobic packing, depletion of thermolabile residues (Cys, Gln, Asn), and increased Pro content. Examining this 323-residue sequence, the amino acid composition is moderate—there is a normal complement of Cys (e.g., 'GFGTC'), no extreme enrichment of charged residues, and no pronounced hydrophobic-core compression typical of thermophiles. The sequence is consistent with a mesophilic enzyme (short-chain dehydrogenase/reductase fold suggested by the N-terminal GxxGxxG-like motif). Since the majority of characterized proteins are mesophilic and this sequence lacks thermophilic signatures, the mesophilic option (37°C) is the only defensible choice among the four. This is a family-level and composition-based inference learned from many thermophilic vs. mesophilic proteins, not a lookup of this protein's specific record.",
    "missing_item_specific_fact": "",
    "reason": "The key distinction among the offered alternatives is mesophilic (37°C) vs. thermophilic (60, 62, 74°C). A knowledgeable model can use general principles of thermal adaptation (charged-residue enrichment, salt-bridge density, thermolabile-residue depletion in thermophiles) applied to the sequence composition, plus the prior that most proteins are mesophilic, to select 37°C as the only mesophilic option. This does not require recalling the specific experimental measurement for this exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span a clear categorical divide: one mesophilic temperature (37°C) versus three thermophilic/hyperthermophilic temperatures (60, 62, 74°C). Given the absence of thermophilic sequence signatures, 37°C is the uniquely defensible choice. There is no ambiguity among the alternatives for a model applying standard thermal-adaptation reasoning."
  },
  "important_caveats": [
    "The experimental optimum of 37°C for a plant enzyme (Alstonia scholaris) is slightly above the typical 25-30°C range for many plant enzymes, but it remains firmly mesophilic and is the only mesophilic option among the choices.",
    "Distinguishing 60°C from 62°C from sequence alone would be essentially impossible without experimental data; however, this distinction is irrelevant since the correct answer is the mesophilic option.",
    "The reviewer-only UniProt annotation (experimental, PubMed:36349266) was not available to the evaluated model; the reasoning_supported judgment relies solely on transferable sequence-composition knowledge."
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
  "benchmark_sequence_sha256": "016d2556a5540f503b5f5d1c251aaf15f9f522ff3142edec17aaac977d884675",
  "current_entry_audit": {
    "entryVersion": 13,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2023-05-03",
    "sequenceVersion": 1
  },
  "current_record_sha256": "48100f49c79084f47d85a13a08484c59c6d716f4326ce301e0bac7ab49997534",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 323,
  "current_source_sequence_sha256": "016d2556a5540f503b5f5d1c251aaf15f9f522ff3142edec17aaac977d884675",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 12,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A9E7S518",
  "selected_historical_entry_version": 12,
  "selected_historical_record_sha256": "9e7eab76338f130e203ce1b1b78446aa08ea74e562c2d55ca9d31f37f8958320",
  "selected_historical_source_sequence_length": 323,
  "selected_historical_source_sequence_sha256": "016d2556a5540f503b5f5d1c251aaf15f9f522ff3142edec17aaac977d884675",
  "selected_historical_version": {
    "accession": "A0A9E7S518",
    "database": "Swiss-Prot",
    "entryVersion": 12,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "RHR1_ALSSC",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S518.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A9E7S518\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:26:12.223906+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48100f49c79084f47d85a13a08484c59c6d716f4326ce301e0bac7ab49997534",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S518.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S518.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":13,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2023-05-03\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:26:12.223906+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48100f49c79084f47d85a13a08484c59c6d716f4326ce301e0bac7ab49997534",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S518.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S518.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Dogbane\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Apocynaceae\",\"Rauvolfioideae\",\"Alstonieae\",\"Alstonia\"],\"scientificName\":\"Alstonia scholaris\",\"synonyms\":[\"Echites scholaris\"],\"taxonId\":52822}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:26:12.223906+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48100f49c79084f47d85a13a08484c59c6d716f4326ce301e0bac7ab49997534",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S518.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S518.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"value\":\"1.1.1.440\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"value\":\"Rhazimal reductase 1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"value\":\"AsRHR1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:26:12.223906+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48100f49c79084f47d85a13a08484c59c6d716f4326ce301e0bac7ab49997534",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S518.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S518.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"BIOPHYSICOCHEMICAL PROPERTIES\",\"phDependence\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"value\":\"Optimum pH is 7-8.\"}]},\"temperatureDependence\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"value\":\"Optimum temperature is 37 degrees Celsius.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:26:12.223906+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48100f49c79084f47d85a13a08484c59c6d716f4326ce301e0bac7ab49997534",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S518.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S518.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Wang Z.\",\"Xiao Y.\",\"Wu S.\",\"Chen J.\",\"Li A.\",\"Tatsis E.C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"36349266\"},{\"database\":\"DOI\",\"id\":\"10.1039/d2sc03612f\"}],\"citationType\":\"journal article\",\"firstPage\":\"12389\",\"id\":\"36349266\",\"journal\":\"Chem. Sci.\",\"lastPage\":\"12395\",\"publicationDate\":\"2022\",\"title\":\"Deciphering and reprogramming the cyclization regioselectivity in bifurcation of indole alkaloid biosynthesis.\",\"volume\":\"13\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"URS65385.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:26:12.223906+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48100f49c79084f47d85a13a08484c59c6d716f4326ce301e0bac7ab49997534",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S518.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S518?format=txt&versions=12)

```json
{
  "entry_version": 12,
  "evidence_id": "H1",
  "excerpt": "ID   RHR1_ALSSC              Reviewed;         323 AA.\nAC   A0A9E7S518;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   03-MAY-2023, sequence version 1.\nDT   28-JAN-2026, entry version 12.\nDE   RecName: Full=Rhazimal reductase 1 {ECO:0000303|PubMed:36349266};\nDE            Short=AsRHR1 {ECO:0000303|PubMed:36349266};\nDE            EC=1.1.1.440 {ECO:0000269|PubMed:36349266};\nGN   Name=RHR1 {ECO:0000303|PubMed:36349266};\nOS   Alstonia scholaris (Dogbane) (Echites scholaris).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Alstonieae;\nOC   Alstonia.\nOX   NCBI_TaxID=52822;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:14.092631+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9e7eab76338f130e203ce1b1b78446aa08ea74e562c2d55ca9d31f37f8958320",
  "url": "https://rest.uniprot.org/unisave/A0A9E7S518?format=txt&versions=12"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S518?format=txt&versions=12)

```json
{
  "entry_version": 12,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:URS65385.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, PATHWAY, AND\nRP   BIOPHYSICOCHEMICAL PROPERTIES.\nRX   PubMed=36349266; DOI=10.1039/d2sc03612f;\nRA   Wang Z., Xiao Y., Wu S., Chen J., Li A., Tatsis E.C.;\nRT   \"Deciphering and reprogramming the cyclization regioselectivity in\nRT   bifurcation of indole alkaloid biosynthesis.\";\nRL   Chem. Sci. 13:12389-12395(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:14.092631+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 16-23",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9e7eab76338f130e203ce1b1b78446aa08ea74e562c2d55ca9d31f37f8958320",
  "url": "https://rest.uniprot.org/unisave/A0A9E7S518?format=txt&versions=12"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S518?format=txt&versions=12)

```json
{
  "entry_version": 12,
  "evidence_id": "H3",
  "excerpt": "CC   -!- BIOPHYSICOCHEMICAL PROPERTIES:\nCC       pH dependence:\nCC         Optimum pH is 7-8. {ECO:0000269|PubMed:36349266};\nCC       Temperature dependence:\nCC         Optimum temperature is 37 degrees Celsius.\nCC         {ECO:0000269|PubMed:36349266};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:14.092631+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 37-42",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9e7eab76338f130e203ce1b1b78446aa08ea74e562c2d55ca9d31f37f8958320",
  "url": "https://rest.uniprot.org/unisave/A0A9E7S518?format=txt&versions=12"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/temperature.json), zero-based source row 11. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
