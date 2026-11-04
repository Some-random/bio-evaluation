# temperature_0018

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/temperature_0018.txt)

**Task:** `temperature`  
**Expected answer:** **A** — 37

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKKRCLITGGAGFIGSHLAEELVKRGHPVTIVDNFYKGKSKYHEELTGNIPIIPISILDKNSMHELVNQHDVVFHLAAILGVKTTMEKSIELIETNFDGTRNILQAALKGKKKVIFASTSEVYGKGTPPFSEDDDRLYGATSKIRWSYAICKTLEETLCLGYALQGLPVTIVRYFNIYGPRAKDGPYAGVIPRFIRAALQGDDLLVYGDGKQTRCFTYVSDAVEATIAAMDEKVNGEIINIGSEDEKSIQEVAQDIHQLTHSSSKIVHVPFEKVYPHGFEEIPNRKPDVTKLKEMCQFHPNVSWEQGLKETIQWFREIEND

[Multiple Choices]
A. 37
B. 79
C. 44-49
D. 38-50
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

> The sequence-matched UniProt record reports an optimum temperature of 37 °C, citing experimental evidence (ECO:0000269). This supports choice A for the measured optimum.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> The experimentally measured temperature optimum for this exact enzyme, reported as 37 °C, is not provided in the original input.


**Reason**

> Sequence composition and general knowledge of protein thermal adaptation may inform a broad prediction, but they do not meaningfully distinguish an optimum of 37 °C from the nearby higher-temperature ranges offered here. The exact assay optimum is a target-specific empirical fact.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices have inconsistent precision, but the source reports a specific measured optimum of 37 °C, corresponding to A.


### Important caveats

- An experimentally reported enzyme optimum is not necessarily identical to the broader thermal-adaptation category described in the prompt.
- The reported optimum applies to the cited experimental measurement and conditions.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The experimentally measured temperature optimum for this exact enzyme, reported as 37 °C, is not provided in the original input.",
    "reason": "Sequence composition and general knowledge of protein thermal adaptation may inform a broad prediction, but they do not meaningfully distinguish an optimum of 37 °C from the nearby higher-temperature ranges offered here. The exact assay optimum is a target-specific empirical fact."
  },
  "case_id": "temperature_0018",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports an optimum temperature of 37 °C, citing experimental evidence (ECO:0000269). This supports choice A for the measured optimum."
  },
  "important_caveats": [
    "An experimentally reported enzyme optimum is not necessarily identical to the broader thermal-adaptation category described in the prompt.",
    "The reported optimum applies to the cited experimental measurement and conditions."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices have inconsistent precision, but the source reports a specific measured optimum of 37 °C, corresponding to A."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "temperature_0018",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports an optimum temperature of 37 °C, citing experimental evidence (ECO:0000269). This supports choice A for the measured optimum.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "The experimentally measured temperature optimum for this exact enzyme, reported as 37 °C, is not provided in the original input.",
    "reason": "Sequence composition and general knowledge of protein thermal adaptation may inform a broad prediction, but they do not meaningfully distinguish an optimum of 37 °C from the nearby higher-temperature ranges offered here. The exact assay optimum is a target-specific empirical fact."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices have inconsistent precision, but the source reports a specific measured optimum of 37 °C, corresponding to A."
  },
  "important_caveats": [
    "An experimentally reported enzyme optimum is not necessarily identical to the broader thermal-adaptation category described in the prompt.",
    "The reported optimum applies to the cited experimental measurement and conditions."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A7GKX7 records the optimum temperature as 37 degrees Celsius, determined experimentally (ECO:0000269, PubMed:20529859). The sequence matches the benchmark sequence (321 AA, sha256 match). The author's expected answer of A (37) is directly supported by the experimental annotation.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains an N-terminal GGAGFIGSH motif diagnostic of the PLP-dependent decarboxylase superfamily, a family overwhelmingly populated by mesophilic enzymes. The amino acid composition shows no thermophilic adaptations: no extreme enrichment of charged residues for salt-bridge networks, no depletion of thermolabile residues (Asn, Gln are present in normal mesophilic proportions), no shortened loops or increased proline content. This completely mesophilic profile argues against B (79°C, hyperthermophilic) and C (44-49°C, thermophilic). For the A vs D distinction: the 38-50°C range implies at least mild thermotolerance, which in characterized enzymes is typically accompanied by detectable sequence signatures (increased ionic interactions, reduced thermolabile residues, hydrophobic core tightening). The complete absence of any such features supports the 'standard' mesophilic optimum of 37°C rather than an elevated range. The PLP-dependent decarboxylase family's predominant mesophilic character provides family-level transferable knowledge favoring 37°C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence's family membership (PLP-dependent decarboxylase, recognizable by the GGAGFIGSH motif) and its complete lack of thermophilic sequence adaptations provide a transferable, family-level argument for the standard mesophilic optimum of 37°C over the elevated 38-50°C range. While the 37 vs 38 boundary is extremely fine, the 38-50 range as a whole (encompassing 44-50°C) is inconsistent with the observed mesophilic sequence profile. B and C are clearly excluded. The argument is probabilistic but grounded in family-level biology and sequence composition principles.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> The boundary between A (37) and D (38-50) is only 1°C. Many mesophilic enzymes have optima in the 37-40°C range and sequence features cannot reliably distinguish 37 from 38. Additionally, option C (44-49) is a strict subset of D (38-50), creating a logical overlap in the answer choices that could confuse a model. However, for a protein with no thermophilic adaptations whatsoever, the 'standard mesophilic = 37°C' heuristic provides a defensible preference for A.


### Important caveats

- The 38-50°C range (option D) encompasses the 44-49°C range (option C), creating a logical subset overlap in the answer choices.
- The distinction between 37°C and 38°C is below the resolution of sequence-based thermal prediction; the argument for A relies on the broader 38-50 range being inconsistent with the mesophilic sequence profile.
- The organism (Bacillus cytotoxicus) is the most thermotolerant member of the B. cereus group, which could tempt a model toward higher temperature answers if the organism were known, but this information is absent from the model input.
- The experimental determination (37°C) is from a single study (PubMed:20529859); no independent replication is noted in the evidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains an N-terminal GGAGFIGSH motif diagnostic of the PLP-dependent decarboxylase superfamily, a family overwhelmingly populated by mesophilic enzymes. The amino acid composition shows no thermophilic adaptations: no extreme enrichment of charged residues for salt-bridge networks, no depletion of thermolabile residues (Asn, Gln are present in normal mesophilic proportions), no shortened loops or increased proline content. This completely mesophilic profile argues against B (79°C, hyperthermophilic) and C (44-49°C, thermophilic). For the A vs D distinction: the 38-50°C range implies at least mild thermotolerance, which in characterized enzymes is typically accompanied by detectable sequence signatures (increased ionic interactions, reduced thermolabile residues, hydrophobic core tightening). The complete absence of any such features supports the 'standard' mesophilic optimum of 37°C rather than an elevated range. The PLP-dependent decarboxylase family's predominant mesophilic character provides family-level transferable knowledge favoring 37°C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence's family membership (PLP-dependent decarboxylase, recognizable by the GGAGFIGSH motif) and its complete lack of thermophilic sequence adaptations provide a transferable, family-level argument for the standard mesophilic optimum of 37°C over the elevated 38-50°C range. While the 37 vs 38 boundary is extremely fine, the 38-50 range as a whole (encompassing 44-50°C) is inconsistent with the observed mesophilic sequence profile. B and C are clearly excluded. The argument is probabilistic but grounded in family-level biology and sequence composition principles."
  },
  "case_id": "temperature_0018",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A7GKX7 records the optimum temperature as 37 degrees Celsius, determined experimentally (ECO:0000269, PubMed:20529859). The sequence matches the benchmark sequence (321 AA, sha256 match). The author's expected answer of A (37) is directly supported by the experimental annotation."
  },
  "important_caveats": [
    "The 38-50°C range (option D) encompasses the 44-49°C range (option C), creating a logical subset overlap in the answer choices.",
    "The distinction between 37°C and 38°C is below the resolution of sequence-based thermal prediction; the argument for A relies on the broader 38-50 range being inconsistent with the mesophilic sequence profile.",
    "The organism (Bacillus cytotoxicus) is the most thermotolerant member of the B. cereus group, which could tempt a model toward higher temperature answers if the organism were known, but this information is absent from the model input.",
    "The experimental determination (37°C) is from a single study (PubMed:20529859); no independent replication is noted in the evidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "The boundary between A (37) and D (38-50) is only 1°C. Many mesophilic enzymes have optima in the 37-40°C range and sequence features cannot reliably distinguish 37 from 38. Additionally, option C (44-49) is a strict subset of D (38-50), creating a logical overlap in the answer choices that could confuse a model. However, for a protein with no thermophilic adaptations whatsoever, the 'standard mesophilic = 37°C' heuristic provides a defensible preference for A."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "temperature_0018",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A7GKX7 records the optimum temperature as 37 degrees Celsius, determined experimentally (ECO:0000269, PubMed:20529859). The sequence matches the benchmark sequence (321 AA, sha256 match). The author's expected answer of A (37) is directly supported by the experimental annotation.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains an N-terminal GGAGFIGSH motif diagnostic of the PLP-dependent decarboxylase superfamily, a family overwhelmingly populated by mesophilic enzymes. The amino acid composition shows no thermophilic adaptations: no extreme enrichment of charged residues for salt-bridge networks, no depletion of thermolabile residues (Asn, Gln are present in normal mesophilic proportions), no shortened loops or increased proline content. This completely mesophilic profile argues against B (79°C, hyperthermophilic) and C (44-49°C, thermophilic). For the A vs D distinction: the 38-50°C range implies at least mild thermotolerance, which in characterized enzymes is typically accompanied by detectable sequence signatures (increased ionic interactions, reduced thermolabile residues, hydrophobic core tightening). The complete absence of any such features supports the 'standard' mesophilic optimum of 37°C rather than an elevated range. The PLP-dependent decarboxylase family's predominant mesophilic character provides family-level transferable knowledge favoring 37°C.",
    "missing_item_specific_fact": "",
    "reason": "The sequence's family membership (PLP-dependent decarboxylase, recognizable by the GGAGFIGSH motif) and its complete lack of thermophilic sequence adaptations provide a transferable, family-level argument for the standard mesophilic optimum of 37°C over the elevated 38-50°C range. While the 37 vs 38 boundary is extremely fine, the 38-50 range as a whole (encompassing 44-50°C) is inconsistent with the observed mesophilic sequence profile. B and C are clearly excluded. The argument is probabilistic but grounded in family-level biology and sequence composition principles."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "The boundary between A (37) and D (38-50) is only 1°C. Many mesophilic enzymes have optima in the 37-40°C range and sequence features cannot reliably distinguish 37 from 38. Additionally, option C (44-49) is a strict subset of D (38-50), creating a logical overlap in the answer choices that could confuse a model. However, for a protein with no thermophilic adaptations whatsoever, the 'standard mesophilic = 37°C' heuristic provides a defensible preference for A."
  },
  "important_caveats": [
    "The 38-50°C range (option D) encompasses the 44-49°C range (option C), creating a logical subset overlap in the answer choices.",
    "The distinction between 37°C and 38°C is below the resolution of sequence-based thermal prediction; the argument for A relies on the broader 38-50 range being inconsistent with the mesophilic sequence profile.",
    "The organism (Bacillus cytotoxicus) is the most thermotolerant member of the B. cereus group, which could tempt a model toward higher temperature answers if the organism were known, but this information is absent from the model input.",
    "The experimental determination (37°C) is from a single study (PubMed:20529859); no independent replication is noted in the evidence."
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
  "benchmark_sequence_length": 321,
  "benchmark_sequence_sha256": "4c5f6d841731f9123f3dbb4943a6017c6602477e2820756b25be4ef0e94f0333",
  "current_entry_audit": {
    "entryVersion": 96,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2007-09-11",
    "sequenceVersion": 1
  },
  "current_record_sha256": "e37b9430cdb758a34827140a4468b1360af7ce820a7d40f214a2160c678d65be",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 321,
  "current_source_sequence_sha256": "4c5f6d841731f9123f3dbb4943a6017c6602477e2820756b25be4ef0e94f0333",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 94,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A7GKX7",
  "selected_historical_entry_version": 94,
  "selected_historical_record_sha256": "3e6a7818add6ff28d4f35cd226e812162be4e132f88da510bdff71af66aa4fea",
  "selected_historical_source_sequence_length": 321,
  "selected_historical_source_sequence_sha256": "4c5f6d841731f9123f3dbb4943a6017c6602477e2820756b25be4ef0e94f0333",
  "selected_historical_version": {
    "accession": "A7GKX7",
    "database": "Swiss-Prot",
    "entryVersion": 94,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "UXNAS_BACCN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX7.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A7GKX7\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:00.082856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e37b9430cdb758a34827140a4468b1360af7ce820a7d40f214a2160c678d65be",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX7.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX7.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":96,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2007-09-11\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:00.082856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e37b9430cdb758a34827140a4468b1360af7ce820a7d40f214a2160c678d65be",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX7.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX7.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Bacillati\",\"Bacillota\",\"Bacilli\",\"Caryophanales\",\"Bacillaceae\",\"Bacillus\",\"Bacillus cereus group\"],\"scientificName\":\"Bacillus cytotoxicus (strain DSM 22905 / CIP 110041 / 391-98 / NVH 391-98)\",\"taxonId\":315749}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:00.082856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e37b9430cdb758a34827140a4468b1360af7ce820a7d40f214a2160c678d65be",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX7.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX7.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20529859\",\"source\":\"PubMed\"}],\"value\":\"UDP-XylNAc synthase\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20529859\",\"source\":\"PubMed\"}],\"value\":\"4.1.1.128\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"UDP-N-acetyl-alpha-D-glucosaminuronate decarboxylase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20529859\",\"source\":\"PubMed\"}],\"value\":\"UDP-GlcNAcA decarboxylase\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:00.082856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e37b9430cdb758a34827140a4468b1360af7ce820a7d40f214a2160c678d65be",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX7.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX7.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"BIOPHYSICOCHEMICAL PROPERTIES\",\"kineticParameters\":{\"michaelisConstants\":[{\"constant\":67.0,\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20529859\",\"source\":\"PubMed\"}],\"substrate\":\"UDP-GlcNAcA\",\"unit\":\"uM\"}],\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20529859\",\"source\":\"PubMed\"}],\"value\":\"kcat is 0.47 sec(-1).\"}]}},\"phDependence\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20529859\",\"source\":\"PubMed\"}],\"value\":\"Optimum pH is 8.2 (PubMed:20529859). No activity is observed below pH 4 (PubMed:20529859).\"}]},\"temperatureDependence\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20529859\",\"source\":\"PubMed\"}],\"value\":\"Optimum temperature is 37 degrees Celsius.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-01T06:25:00.082856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e37b9430cdb758a34827140a4468b1360af7ce820a7d40f214a2160c678d65be",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX7.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX7.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Gu X.\",\"Glushka J.\",\"Lee S.G.\",\"Bar-Peled M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"20529859\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m110.125872\"}],\"citationType\":\"journal article\",\"firstPage\":\"24825\",\"id\":\"20529859\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"24833\",\"publicationDate\":\"2010\",\"title\":\"Biosynthesis of a new UDP-sugar, UDP-2-acetamido-2-deoxyxylose, in the human pathogen Bacillus cereus subspecies cytotoxis NVH 391-98.\",\"volume\":\"285\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"ADE43880.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"DSM 22905 / CIP 110041 / 391-98 / NVH 391-98\"}],\"referenceNumber\":2,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"ACTIVITY REGULATION\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:25:00.082856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e37b9430cdb758a34827140a4468b1360af7ce820a7d40f214a2160c678d65be",
  "url": "https://rest.uniprot.org/uniprotkb/A7GKX7.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94)

```json
{
  "entry_version": 94,
  "evidence_id": "H1",
  "excerpt": "ID   UXNAS_BACCN             Reviewed;         321 AA.\nAC   A7GKX7;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   11-SEP-2007, sequence version 1.\nDT   28-JAN-2026, entry version 94.\nDE   RecName: Full=UDP-N-acetyl-alpha-D-glucosaminuronate decarboxylase {ECO:0000305};\nDE            Short=UDP-GlcNAcA decarboxylase {ECO:0000303|PubMed:20529859};\nDE            EC=4.1.1.128 {ECO:0000269|PubMed:20529859};\nDE   AltName: Full=UDP-XylNAc synthase {ECO:0000303|PubMed:20529859};\nGN   Name=UXNAcS {ECO:0000303|PubMed:20529859};\nGN   OrderedLocusNames=Bcer98_0430 {ECO:0000312|EMBL:ABS20785.1};\nOS   Bacillus cytotoxicus (strain DSM 22905 / CIP 110041 / 391-98 / NVH 391-98).\nOC   Bacteria; Bacillati; Bacillota; Bacilli; Bacillales; Bacillaceae; Bacillus;\nOC   Bacillus cereus group.\nOX   NCBI_TaxID=315749;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:51.337169+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3e6a7818add6ff28d4f35cd226e812162be4e132f88da510bdff71af66aa4fea",
  "url": "https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94)

```json
{
  "entry_version": 94,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000312|EMBL:ADE43880.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, CATALYTIC ACTIVITY, COFACTOR,\nRP   ACTIVITY REGULATION, BIOPHYSICOCHEMICAL PROPERTIES, AND SUBUNIT.\nRC   STRAIN=DSM 22905 / CIP 110041 / 391-98 / NVH 391-98;\nRX   PubMed=20529859; DOI=10.1074/jbc.m110.125872;\nRA   Gu X., Glushka J., Lee S.G., Bar-Peled M.;\nRT   \"Biosynthesis of a new UDP-sugar, UDP-2-acetamido-2-deoxyxylose, in the\nRT   human pathogen Bacillus cereus subspecies cytotoxis NVH 391-98.\";\nRL   J. Biol. Chem. 285:24825-24833(2010).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:51.337169+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 27-35",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3e6a7818add6ff28d4f35cd226e812162be4e132f88da510bdff71af66aa4fea",
  "url": "https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94)

```json
{
  "entry_version": 94,
  "evidence_id": "H3",
  "excerpt": "CC   -!- BIOPHYSICOCHEMICAL PROPERTIES:\nCC       Kinetic parameters:\nCC         KM=67 uM for UDP-GlcNAcA {ECO:0000269|PubMed:20529859};\nCC         Note=kcat is 0.47 sec(-1). {ECO:0000269|PubMed:20529859};\nCC       pH dependence:\nCC         Optimum pH is 8.2 (PubMed:20529859). No activity is observed below pH\nCC         4 (PubMed:20529859). {ECO:0000269|PubMed:20529859};\nCC       Temperature dependence:\nCC         Optimum temperature is 37 degrees Celsius.\nCC         {ECO:0000269|PubMed:20529859};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:51.337169+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 57-66",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3e6a7818add6ff28d4f35cd226e812162be4e132f88da510bdff71af66aa4fea",
  "url": "https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/temperature.json), zero-based source row 18. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
