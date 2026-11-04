# temperature_0033

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/temperature_0033.txt)

**Task:** `temperature`  
**Expected answer:** **B** — 30

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAISPEVEHPNKAFGFAARDPSGLLSPFNFSRRATGEHDVQFKVLYCGICHSDLHMIKNEWGFTKYPIVPGHEIVGVVTEVGSKVEKFKVGDKVGVGCLVGSCRKCDMCSQDLENYCPDQILTYSATYTDGTTTYGGYSSLMVADEHFVIRWPENLPMDIGAPLLCAGITTYSPLRHFGLDKPGTHVGIVGLGGLGHVAVKFAKAFGAKVTVISTSEGKKQEAVEKLGADAFLVSRDPEQMQAAAATLDGIIDTVSAVHPILPLVNLLKSQGKLIMVGAPEKPIELPVFPLLLGRKIVAGSAIGGLKETQDMIDFAAKHNILPDVELIPMDYVNTAMERLLKADVKYRFVIDICNTLKSA

[Multiple Choices]
A. 50
B. 30
C. 54
D. 64
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

> The matched sequence record reports an optimum temperature of 30 °C with experimental evidence (ECO:0000269), supporting choice B.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with an ordinary soluble globular enzyme and shows no obvious membrane or other extreme-environment signature. As a probabilistic prior, ordinary enzymes are more likely to have moderate-temperature activity than optima of 50–64 °C, making 30 the best fit among these choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> That transferable biological prior can meaningfully favor 30 over the substantially higher alternatives, though sequence alone does not establish an exact optimum and the inference is not strong proof.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied choices are distinct, and the sequence-matched experimental annotation supports 30 °C.


### Important caveats

- The experimental temperature annotation is reviewer-only evidence, not information available in the original input.
- The sequence-based inference is probabilistic; the original input gives no organism, habitat, or measured temperature.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with an ordinary soluble globular enzyme and shows no obvious membrane or other extreme-environment signature. As a probabilistic prior, ordinary enzymes are more likely to have moderate-temperature activity than optima of 50–64 °C, making 30 the best fit among these choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "That transferable biological prior can meaningfully favor 30 over the substantially higher alternatives, though sequence alone does not establish an exact optimum and the inference is not strong proof."
  },
  "case_id": "temperature_0033",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The matched sequence record reports an optimum temperature of 30 °C with experimental evidence (ECO:0000269), supporting choice B."
  },
  "important_caveats": [
    "The experimental temperature annotation is reviewer-only evidence, not information available in the original input.",
    "The sequence-based inference is probabilistic; the original input gives no organism, habitat, or measured temperature."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied choices are distinct, and the sequence-matched experimental annotation supports 30 °C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "temperature_0033",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence record reports an optimum temperature of 30 °C with experimental evidence (ECO:0000269), supporting choice B.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with an ordinary soluble globular enzyme and shows no obvious membrane or other extreme-environment signature. As a probabilistic prior, ordinary enzymes are more likely to have moderate-temperature activity than optima of 50–64 °C, making 30 the best fit among these choices.",
    "missing_item_specific_fact": "",
    "reason": "That transferable biological prior can meaningfully favor 30 over the substantially higher alternatives, though sequence alone does not establish an exact optimum and the inference is not strong proof."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied choices are distinct, and the sequence-matched experimental annotation supports 30 °C."
  },
  "important_caveats": [
    "The experimental temperature annotation is reviewer-only evidence, not information available in the original input.",
    "The sequence-based inference is probabilistic; the original input gives no organism, habitat, or measured temperature."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (P0DXJ3, Vomilenine reductase from Rauvolfia serpentina) explicitly states 'Optimum temperature is 30 degrees Celsius' with experimental evidence (ECO:0000269|PubMed:11937349). The sequence in the question matches the canonical entry (360 AA, SHA256 match). The expected answer B (30) is directly supported by experimental measurement.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The choices partition into one mesophilic option (30°C) versus three thermophilic options (50, 54, 64°C). Several sequence features distinguish mesophilic from thermophilic adaptation: (1) The sequence contains approximately 6-7 cysteine residues (~1.7-2% Cys content), including a Cys-rich zinc-binding motif (GICHSDLH...GCLVGSCRKCDMCSQDLENYCPDQILTYSATY). Thermophilic proteins strongly minimize cysteine because free thiols and disulfide bonds are destabilizing at 50-64°C; thermophilic enzymes typically have <1% Cys. (2) The enzyme belongs to the medium-chain dehydrogenase/reductase (MDR) family based on structural motifs (GxxGxxG-like Rossmann fold segments, catalytic Zn-binding Cys cluster), and plant MDR enzymes are overwhelmingly mesophilic. (3) The overall amino acid composition lacks the hallmarks of thermophilic adaptation: no extreme enrichment of charged residues for salt-bridge networks, presence of flexible Gly/Ser/Thr-rich loops, and moderate hydrophobicity. These features collectively argue against 50, 54, or 64°C and support the mesophilic 30°C answer.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can use well-established sequence-composition rules (Cys content, charge distribution, hydrophobicity patterns) learned from thermophilic vs. mesophilic protein families to exclude the three thermophilic options. The multiple cysteines and plant-reductase family context provide a concrete, transferable basis for selecting the mesophilic answer without needing this protein's specific UniProt annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices clearly separate one mesophilic temperature (30°C) from three thermophilic temperatures (50, 54, 64°C). The sequence features (multiple Cys, plant enzyme family, moderate composition) unambiguously favor the mesophilic option. No two choices are equally defensible given the sequence evidence.


### Important caveats

- Distinguishing 30°C from other mesophilic temperatures (e.g., 37°C or 25°C) would be far harder from sequence alone, but the offered choices do not require that finer resolution.
- The Cys-content argument is probabilistic: some thermophilic proteins do retain a few cysteines, but the density here (~2%) is atypical for proteins functioning at 50-64°C.
- The reviewer-only evidence confirms the experimental optimum is exactly 30°C, but the model's inference from sequence features to 'mesophilic' is the transferable reasoning path, not recall of this specific annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices partition into one mesophilic option (30°C) versus three thermophilic options (50, 54, 64°C). Several sequence features distinguish mesophilic from thermophilic adaptation: (1) The sequence contains approximately 6-7 cysteine residues (~1.7-2% Cys content), including a Cys-rich zinc-binding motif (GICHSDLH...GCLVGSCRKCDMCSQDLENYCPDQILTYSATY). Thermophilic proteins strongly minimize cysteine because free thiols and disulfide bonds are destabilizing at 50-64°C; thermophilic enzymes typically have <1% Cys. (2) The enzyme belongs to the medium-chain dehydrogenase/reductase (MDR) family based on structural motifs (GxxGxxG-like Rossmann fold segments, catalytic Zn-binding Cys cluster), and plant MDR enzymes are overwhelmingly mesophilic. (3) The overall amino acid composition lacks the hallmarks of thermophilic adaptation: no extreme enrichment of charged residues for salt-bridge networks, presence of flexible Gly/Ser/Thr-rich loops, and moderate hydrophobicity. These features collectively argue against 50, 54, or 64°C and support the mesophilic 30°C answer.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use well-established sequence-composition rules (Cys content, charge distribution, hydrophobicity patterns) learned from thermophilic vs. mesophilic protein families to exclude the three thermophilic options. The multiple cysteines and plant-reductase family context provide a concrete, transferable basis for selecting the mesophilic answer without needing this protein's specific UniProt annotation."
  },
  "case_id": "temperature_0033",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (P0DXJ3, Vomilenine reductase from Rauvolfia serpentina) explicitly states 'Optimum temperature is 30 degrees Celsius' with experimental evidence (ECO:0000269|PubMed:11937349). The sequence in the question matches the canonical entry (360 AA, SHA256 match). The expected answer B (30) is directly supported by experimental measurement."
  },
  "important_caveats": [
    "Distinguishing 30°C from other mesophilic temperatures (e.g., 37°C or 25°C) would be far harder from sequence alone, but the offered choices do not require that finer resolution.",
    "The Cys-content argument is probabilistic: some thermophilic proteins do retain a few cysteines, but the density here (~2%) is atypical for proteins functioning at 50-64°C.",
    "The reviewer-only evidence confirms the experimental optimum is exactly 30°C, but the model's inference from sequence features to 'mesophilic' is the transferable reasoning path, not recall of this specific annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices clearly separate one mesophilic temperature (30°C) from three thermophilic temperatures (50, 54, 64°C). The sequence features (multiple Cys, plant enzyme family, moderate composition) unambiguously favor the mesophilic option. No two choices are equally defensible given the sequence evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "temperature_0033",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (P0DXJ3, Vomilenine reductase from Rauvolfia serpentina) explicitly states 'Optimum temperature is 30 degrees Celsius' with experimental evidence (ECO:0000269|PubMed:11937349). The sequence in the question matches the canonical entry (360 AA, SHA256 match). The expected answer B (30) is directly supported by experimental measurement.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The choices partition into one mesophilic option (30°C) versus three thermophilic options (50, 54, 64°C). Several sequence features distinguish mesophilic from thermophilic adaptation: (1) The sequence contains approximately 6-7 cysteine residues (~1.7-2% Cys content), including a Cys-rich zinc-binding motif (GICHSDLH...GCLVGSCRKCDMCSQDLENYCPDQILTYSATY). Thermophilic proteins strongly minimize cysteine because free thiols and disulfide bonds are destabilizing at 50-64°C; thermophilic enzymes typically have <1% Cys. (2) The enzyme belongs to the medium-chain dehydrogenase/reductase (MDR) family based on structural motifs (GxxGxxG-like Rossmann fold segments, catalytic Zn-binding Cys cluster), and plant MDR enzymes are overwhelmingly mesophilic. (3) The overall amino acid composition lacks the hallmarks of thermophilic adaptation: no extreme enrichment of charged residues for salt-bridge networks, presence of flexible Gly/Ser/Thr-rich loops, and moderate hydrophobicity. These features collectively argue against 50, 54, or 64°C and support the mesophilic 30°C answer.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use well-established sequence-composition rules (Cys content, charge distribution, hydrophobicity patterns) learned from thermophilic vs. mesophilic protein families to exclude the three thermophilic options. The multiple cysteines and plant-reductase family context provide a concrete, transferable basis for selecting the mesophilic answer without needing this protein's specific UniProt annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices clearly separate one mesophilic temperature (30°C) from three thermophilic temperatures (50, 54, 64°C). The sequence features (multiple Cys, plant enzyme family, moderate composition) unambiguously favor the mesophilic option. No two choices are equally defensible given the sequence evidence."
  },
  "important_caveats": [
    "Distinguishing 30°C from other mesophilic temperatures (e.g., 37°C or 25°C) would be far harder from sequence alone, but the offered choices do not require that finer resolution.",
    "The Cys-content argument is probabilistic: some thermophilic proteins do retain a few cysteines, but the density here (~2%) is atypical for proteins functioning at 50-64°C.",
    "The reviewer-only evidence confirms the experimental optimum is exactly 30°C, but the model's inference from sequence features to 'mesophilic' is the transferable reasoning path, not recall of this specific annotation."
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
  "benchmark_sequence_length": 360,
  "benchmark_sequence_sha256": "1933079f07120bf5b2fe0ecc1f607c3e5acf58131be2f829cf6de54cffcec9ac",
  "current_entry_audit": {
    "entryVersion": 4,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-06-18",
    "sequenceVersion": 1
  },
  "current_record_sha256": "ccaaad5822ec39e44590c5e16beeccbdfcd7c83e7419ffbefc67e80e7443eae6",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 360,
  "current_source_sequence_sha256": "1933079f07120bf5b2fe0ecc1f607c3e5acf58131be2f829cf6de54cffcec9ac",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 2,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "P0DXJ3",
  "selected_historical_entry_version": 2,
  "selected_historical_record_sha256": "8bdcf60482b99bb425a940f66a98a33c2804e893e02173cd72679e1dd8c51d20",
  "selected_historical_source_sequence_length": 360,
  "selected_historical_source_sequence_sha256": "1933079f07120bf5b2fe0ecc1f607c3e5acf58131be2f829cf6de54cffcec9ac",
  "selected_historical_version": {
    "accession": "P0DXJ3",
    "database": "Swiss-Prot",
    "entryVersion": 2,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "VOR1_RAUSE",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ3.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DXJ3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:29:30.487363+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ccaaad5822ec39e44590c5e16beeccbdfcd7c83e7419ffbefc67e80e7443eae6",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":4,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-06-18\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:29:30.487363+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ccaaad5822ec39e44590c5e16beeccbdfcd7c83e7419ffbefc67e80e7443eae6",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Serpentine wood\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Apocynaceae\",\"Rauvolfioideae\",\"Vinceae\",\"Rauvolfiinae\",\"Rauvolfia\"],\"scientificName\":\"Rauvolfia serpentina\",\"synonyms\":[\"Ophioxylon serpentinum\"],\"taxonId\":4060}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:29:30.487363+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ccaaad5822ec39e44590c5e16beeccbdfcd7c83e7419ffbefc67e80e7443eae6",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"CAD2-homolog protein\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"Protein RR6-2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"RsRR6-2\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"11937349\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"1.5.1.32\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"Vomilenine reductase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"RsVR\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:29:30.487363+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ccaaad5822ec39e44590c5e16beeccbdfcd7c83e7419ffbefc67e80e7443eae6",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"BIOPHYSICOCHEMICAL PROPERTIES\",\"kineticParameters\":{\"michaelisConstants\":[{\"constant\":41.6,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"substrate\":\"vomilenine\",\"unit\":\"uM\"}],\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"kcat is 1.7 sec(-1) with vomilenine as substrate.\"}]}},\"phDependence\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"11937349\",\"source\":\"PubMed\"}],\"value\":\"Optimum pH is 5.7-6.2.\"}]},\"temperatureDependence\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"11937349\",\"source\":\"PubMed\"}],\"value\":\"Optimum temperature is 30 degrees Celsius.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-02T04:29:30.487363+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ccaaad5822ec39e44590c5e16beeccbdfcd7c83e7419ffbefc67e80e7443eae6",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ3.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ3.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Guo J.\",\"Gao D.\",\"Lian J.\",\"Qu Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38212296\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-024-44797-z\"}],\"citationType\":\"journal article\",\"firstPage\":\"457\",\"id\":\"38212296\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"457\",\"publicationDate\":\"2024\",\"title\":\"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.\",\"volume\":\"15\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"WKU61927.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\",\"TISSUE SPECIFICITY\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:29:30.487363+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ccaaad5822ec39e44590c5e16beeccbdfcd7c83e7419ffbefc67e80e7443eae6",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ3.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ3.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"von Schumann G.\",\"Gao S.\",\"Stoeckigt J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"11937349\"},{\"database\":\"DOI\",\"id\":\"10.1016/s0968-0896(01)00435-7\"}],\"citationType\":\"journal article\",\"firstPage\":\"1913\",\"id\":\"11937349\",\"journal\":\"Bioorg. Med. Chem.\",\"lastPage\":\"1918\",\"publicationDate\":\"2002\",\"title\":\"Vomilenine reductase--a novel enzyme catalyzing a crucial step in the biosynthesis of the therapeutically applied antiarrhythmic alkaloid ajmaline.\",\"volume\":\"10\"},\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\",\"ACTIVITY REGULATION\",\"TISSUE SPECIFICITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:29:30.487363+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ccaaad5822ec39e44590c5e16beeccbdfcd7c83e7419ffbefc67e80e7443eae6",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ3?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H1",
  "excerpt": "ID   VOR1_RAUSE              Reviewed;         360 AA.\nAC   P0DXJ3;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-JUN-2025, sequence version 1.\nDT   28-JAN-2026, entry version 2.\nDE   RecName: Full=Vomilenine reductase {ECO:0000305|PubMed:38212296};\nDE            Short=RsVR {ECO:0000305|PubMed:38212296};\nDE            EC=1.5.1.32 {ECO:0000269|PubMed:11937349, ECO:0000269|PubMed:38212296};\nDE   AltName: Full=CAD2-homolog protein {ECO:0000303|PubMed:38212296};\nDE   AltName: Full=Protein RR6-2 {ECO:0000303|PubMed:38212296};\nDE            Short=RsRR6-2 {ECO:0000303|PubMed:38212296};\nGN   Name=VR {ECO:0000305|PubMed:38212296};\nGN   Synonyms=RR6-2 {ECO:0000303|PubMed:38212296};\nOS   Rauvolfia serpentina (Serpentine wood) (Ophioxylon serpentinum).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Vinceae;\nOC   Rauvolfiinae; Rauvolfia.\nOX   NCBI_TaxID=4060;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:34.682731+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-19",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8bdcf60482b99bb425a940f66a98a33c2804e893e02173cd72679e1dd8c51d20",
  "url": "https://rest.uniprot.org/unisave/P0DXJ3?format=txt&versions=2"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ3?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:WKU61927.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, TISSUE SPECIFICITY, AND\nRP   BIOTECHNOLOGY.\nRX   PubMed=38212296; DOI=10.1038/s41467-024-44797-z;\nRA   Guo J., Gao D., Lian J., Qu Y.;\nRT   \"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.\";\nRL   Nat. Commun. 15:457-457(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:34.682731+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 20-27",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8bdcf60482b99bb425a940f66a98a33c2804e893e02173cd72679e1dd8c51d20",
  "url": "https://rest.uniprot.org/unisave/P0DXJ3?format=txt&versions=2"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ3?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H3",
  "excerpt": "RN   [3]\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY,\nRP   ACTIVITY REGULATION, AND TISSUE SPECIFICITY.\nRX   PubMed=11937349; DOI=10.1016/s0968-0896(01)00435-7;\nRA   von Schumann G., Gao S., Stoeckigt J.;\nRT   \"Vomilenine reductase--a novel enzyme catalyzing a crucial step in the\nRT   biosynthesis of the therapeutically applied antiarrhythmic alkaloid\nRT   ajmaline.\";\nRL   Bioorg. Med. Chem. 10:1913-1918(2002).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:34.682731+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 35-43",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8bdcf60482b99bb425a940f66a98a33c2804e893e02173cd72679e1dd8c51d20",
  "url": "https://rest.uniprot.org/unisave/P0DXJ3?format=txt&versions=2"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ3?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H4",
  "excerpt": "CC   -!- BIOPHYSICOCHEMICAL PROPERTIES:\nCC       Kinetic parameters:\nCC         KM=41.6 uM for vomilenine {ECO:0000269|PubMed:38212296};\nCC         Note=kcat is 1.7 sec(-1) with vomilenine as substrate.\nCC         {ECO:0000269|PubMed:38212296};\nCC       pH dependence:\nCC         Optimum pH is 5.7-6.2. {ECO:0000269|PubMed:11937349};\nCC       Temperature dependence:\nCC         Optimum temperature is 30 degrees Celsius.\nCC         {ECO:0000269|PubMed:11937349};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:34.682731+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 64-73",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8bdcf60482b99bb425a940f66a98a33c2804e893e02173cd72679e1dd8c51d20",
  "url": "https://rest.uniprot.org/unisave/P0DXJ3?format=txt&versions=2"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/temperature.json), zero-based source row 33. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
