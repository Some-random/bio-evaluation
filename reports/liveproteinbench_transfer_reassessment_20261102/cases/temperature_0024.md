# temperature_0024

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/temperature_0024.txt)

**Task:** `temperature`  
**Expected answer:** **C** — 37

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTHRRLLWALCVAALLGVVAAQAGDQQQMQPNEADALRKKWSAVEVVRDLGHIKKDLAKMIELEGAGALSQDELYFYYFRMHDFDNNNKLDGQEMMAAMFHTNHHEEDDEHDGKVPLIIPEQDIASYVDSVLRADKNQDGFISYPELRTSDLTNQI

[Multiple Choices]
A. 34-40
B. 22
C. 37
D. 29-44
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

> The sequence matches the annotated protein, and the historical UniProt entry reports an optimum temperature of 37°C with experimental evidence. This supports choice C as the exact optimum.

Citations as saved: [H6](#evidence-h6), [C5](#evidence-c5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic segment is consistent with a secreted protein, and general biology might suggest a mesophilic operating temperature. That gives only a broad expectation, not a reliable way to choose an exact optimum of 37°C over the other offered values or ranges.


**Missing item-specific fact**

> The experimentally measured optimum temperature for this particular protein.


**Reason**

> The sequence does not provide a clear transferable feature that determines the assay optimum. A general expectation of moderate temperature does not meaningfully distinguish 37°C from ranges that include 37°C or other plausible mesophilic values.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C",
  "D"
]
```

> If the options are interpreted as possible optimal-temperature ranges or values, 37°C falls within both 34–40 and 29–44 as well as matching the exact value in C. The prompt does not clarify whether the ranges are meant to be exclusive categories.


### Important caveats

- The sequence match and experimental annotation support the key, but that reviewer-only evidence was not part of the original input.
- The ambiguity concerns the overlapping option formats; the source annotation specifically reports an optimum of 37°C.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a secreted protein, and general biology might suggest a mesophilic operating temperature. That gives only a broad expectation, not a reliable way to choose an exact optimum of 37°C over the other offered values or ranges.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The experimentally measured optimum temperature for this particular protein.",
    "reason": "The sequence does not provide a clear transferable feature that determines the assay optimum. A general expectation of moderate temperature does not meaningfully distinguish 37°C from ranges that include 37°C or other plausible mesophilic values."
  },
  "case_id": "temperature_0024",
  "expected_answer_check": {
    "evidence_ids": [
      "H6",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the annotated protein, and the historical UniProt entry reports an optimum temperature of 37°C with experimental evidence. This supports choice C as the exact optimum."
  },
  "important_caveats": [
    "The sequence match and experimental annotation support the key, but that reviewer-only evidence was not part of the original input.",
    "The ambiguity concerns the overlapping option formats; the source annotation specifically reports an optimum of 37°C."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C",
      "D"
    ],
    "reason": "If the options are interpreted as possible optimal-temperature ranges or values, 37°C falls within both 34–40 and 29–44 as well as matching the exact value in C. The prompt does not clarify whether the ranges are meant to be exclusive categories."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "temperature_0024",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the annotated protein, and the historical UniProt entry reports an optimum temperature of 37°C with experimental evidence. This supports choice C as the exact optimum.",
    "evidence_ids": ["H6", "C5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a secreted protein, and general biology might suggest a mesophilic operating temperature. That gives only a broad expectation, not a reliable way to choose an exact optimum of 37°C over the other offered values or ranges.",
    "missing_item_specific_fact": "The experimentally measured optimum temperature for this particular protein.",
    "reason": "The sequence does not provide a clear transferable feature that determines the assay optimum. A general expectation of moderate temperature does not meaningfully distinguish 37°C from ranges that include 37°C or other plausible mesophilic values."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C", "D"],
    "reason": "If the options are interpreted as possible optimal-temperature ranges or values, 37°C falls within both 34–40 and 29–44 as well as matching the exact value in C. The prompt does not clarify whether the ranges are meant to be exclusive categories."
  },
  "important_caveats": [
    "The sequence match and experimental annotation support the key, but that reviewer-only evidence was not part of the original input.",
    "The ambiguity concerns the overlapping option formats; the source annotation specifically reports an optimum of 37°C."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (D4QD81, sequence matched) records an experimentally determined optimum temperature of 37°C (ECO:0000269, PubMed:22206819), with activity range 20-45°C. The benchmark sequence (156 AA) matches the source sequence exactly. Choice C (37) corresponds directly to the reported optimum temperature.

Citations as saved: [C5](#evidence-c5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Sequence composition analysis can rule out cold adaptation (B: 22°C) because the protein shows moderate charged-residue content, a signal peptide suggesting extracellular function, and EF-hand motifs with acidic residues—all inconsistent with psychrophilic adaptation. However, distinguishing 37°C (C) from the ranges 34-40°C (A) or 29-44°C (D) requires knowing the organism's ecological context: this is a tick (ectotherm) protein that functions during feeding on warm-blooded hosts, yielding an experimentally measured optimum at mammalian body temperature. The sequence alone reveals a secreted EF-hand protein of moderate stability but cannot identify the organism as a blood-feeding arthropod or specify the exact optimum versus a plausible range.


**Missing item-specific fact**

> The experimentally measured optimum temperature of exactly 37°C for this specific protein (Longistatin from Haemaphysalis longicornis), and the organism's identity as a tick that feeds on warm-blooded hosts—neither of which can be reliably inferred from the 156-residue sequence alone without database lookup.


**Reason**

> While composition analysis broadly places this protein in the 'moderate' thermal category (ruling out 22°C), the three remaining options (37, 34-40, 29-44) all represent moderate-temperature ranges. Selecting the precise value 37 over the ranges requires the specific experimental measurement recorded in the literature for this exact protein, or identification of the organism as a mammalian-host parasite—knowledge not derivable from sequence features alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C",
  "D"
]
```

> Options A (34-40), C (37), and D (29-44) all describe moderate-temperature adaptation. Without the specific experimental datum, a model reasoning from composition alone could plausibly select any of these as 'moderate' thermal adaptation. The ranges A and D overlap with 37°C. Only the precise experimental measurement (optimum = 37°C) uniquely selects C.


### Important caveats

- The optimum temperature (37°C) is experimentally determined (ECO:0000269) but the active range (20-45°C) does not exactly match any offered range option, making the question's range choices (A, D) imprecise representations of the actual data.
- The question format mixes single values (B, C) and ranges (A, D) as options for 'thermal adaptation category,' which is an unusual presentation that may confuse the expected response type.
- The organism identity (Haemaphysalis longicornis, bush tick) is reviewer-only and not derivable from the sequence without database lookup; this ecological context is what makes 37°C the natural optimum.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Sequence composition analysis can rule out cold adaptation (B: 22°C) because the protein shows moderate charged-residue content, a signal peptide suggesting extracellular function, and EF-hand motifs with acidic residues—all inconsistent with psychrophilic adaptation. However, distinguishing 37°C (C) from the ranges 34-40°C (A) or 29-44°C (D) requires knowing the organism's ecological context: this is a tick (ectotherm) protein that functions during feeding on warm-blooded hosts, yielding an experimentally measured optimum at mammalian body temperature. The sequence alone reveals a secreted EF-hand protein of moderate stability but cannot identify the organism as a blood-feeding arthropod or specify the exact optimum versus a plausible range.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The experimentally measured optimum temperature of exactly 37°C for this specific protein (Longistatin from Haemaphysalis longicornis), and the organism's identity as a tick that feeds on warm-blooded hosts—neither of which can be reliably inferred from the 156-residue sequence alone without database lookup.",
    "reason": "While composition analysis broadly places this protein in the 'moderate' thermal category (ruling out 22°C), the three remaining options (37, 34-40, 29-44) all represent moderate-temperature ranges. Selecting the precise value 37 over the ranges requires the specific experimental measurement recorded in the literature for this exact protein, or identification of the organism as a mammalian-host parasite—knowledge not derivable from sequence features alone."
  },
  "case_id": "temperature_0024",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (D4QD81, sequence matched) records an experimentally determined optimum temperature of 37°C (ECO:0000269, PubMed:22206819), with activity range 20-45°C. The benchmark sequence (156 AA) matches the source sequence exactly. Choice C (37) corresponds directly to the reported optimum temperature."
  },
  "important_caveats": [
    "The optimum temperature (37°C) is experimentally determined (ECO:0000269) but the active range (20-45°C) does not exactly match any offered range option, making the question's range choices (A, D) imprecise representations of the actual data.",
    "The question format mixes single values (B, C) and ranges (A, D) as options for 'thermal adaptation category,' which is an unusual presentation that may confuse the expected response type.",
    "The organism identity (Haemaphysalis longicornis, bush tick) is reviewer-only and not derivable from the sequence without database lookup; this ecological context is what makes 37°C the natural optimum."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C",
      "D"
    ],
    "reason": "Options A (34-40), C (37), and D (29-44) all describe moderate-temperature adaptation. Without the specific experimental datum, a model reasoning from composition alone could plausibly select any of these as 'moderate' thermal adaptation. The ranges A and D overlap with 37°C. Only the precise experimental measurement (optimum = 37°C) uniquely selects C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "temperature_0024",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (D4QD81, sequence matched) records an experimentally determined optimum temperature of 37°C (ECO:0000269, PubMed:22206819), with activity range 20-45°C. The benchmark sequence (156 AA) matches the source sequence exactly. Choice C (37) corresponds directly to the reported optimum temperature.",
    "evidence_ids": ["C5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Sequence composition analysis can rule out cold adaptation (B: 22°C) because the protein shows moderate charged-residue content, a signal peptide suggesting extracellular function, and EF-hand motifs with acidic residues—all inconsistent with psychrophilic adaptation. However, distinguishing 37°C (C) from the ranges 34-40°C (A) or 29-44°C (D) requires knowing the organism's ecological context: this is a tick (ectotherm) protein that functions during feeding on warm-blooded hosts, yielding an experimentally measured optimum at mammalian body temperature. The sequence alone reveals a secreted EF-hand protein of moderate stability but cannot identify the organism as a blood-feeding arthropod or specify the exact optimum versus a plausible range.",
    "missing_item_specific_fact": "The experimentally measured optimum temperature of exactly 37°C for this specific protein (Longistatin from Haemaphysalis longicornis), and the organism's identity as a tick that feeds on warm-blooded hosts—neither of which can be reliably inferred from the 156-residue sequence alone without database lookup.",
    "reason": "While composition analysis broadly places this protein in the 'moderate' thermal category (ruling out 22°C), the three remaining options (37, 34-40, 29-44) all represent moderate-temperature ranges. Selecting the precise value 37 over the ranges requires the specific experimental measurement recorded in the literature for this exact protein, or identification of the organism as a mammalian-host parasite—knowledge not derivable from sequence features alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C", "D"],
    "reason": "Options A (34-40), C (37), and D (29-44) all describe moderate-temperature adaptation. Without the specific experimental datum, a model reasoning from composition alone could plausibly select any of these as 'moderate' thermal adaptation. The ranges A and D overlap with 37°C. Only the precise experimental measurement (optimum = 37°C) uniquely selects C."
  },
  "important_caveats": [
    "The optimum temperature (37°C) is experimentally determined (ECO:0000269) but the active range (20-45°C) does not exactly match any offered range option, making the question's range choices (A, D) imprecise representations of the actual data.",
    "The question format mixes single values (B, C) and ranges (A, D) as options for 'thermal adaptation category,' which is an unusual presentation that may confuse the expected response type.",
    "The organism identity (Haemaphysalis longicornis, bush tick) is reviewer-only and not derivable from the sequence without database lookup; this ecological context is what makes 37°C the natural optimum."
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
  "benchmark_sequence_length": 156,
  "benchmark_sequence_sha256": "b49da4c85afbae35dc43277360770712180ee44911013a8d16fcb6c5a4bf35a3",
  "current_entry_audit": {
    "entryVersion": 32,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2010-06-15",
    "sequenceVersion": 1
  },
  "current_record_sha256": "27d5a24c10550956afab284439c23ad93d6c94ed57b9a87ce791ea4e4597d0dd",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 156,
  "current_source_sequence_sha256": "b49da4c85afbae35dc43277360770712180ee44911013a8d16fcb6c5a4bf35a3",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 31,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "D4QD81",
  "selected_historical_entry_version": 31,
  "selected_historical_record_sha256": "33d72b54de397540314c319d5d65281dcef13ef22f478476c602e399ba6c861a",
  "selected_historical_source_sequence_length": 156,
  "selected_historical_source_sequence_sha256": "b49da4c85afbae35dc43277360770712180ee44911013a8d16fcb6c5a4bf35a3",
  "selected_historical_version": {
    "accession": "D4QD81",
    "database": "Swiss-Prot",
    "entryVersion": 31,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "LONG_HAELO",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D4QD81.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"D4QD81\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:05.409363+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "27d5a24c10550956afab284439c23ad93d6c94ed57b9a87ce791ea4e4597d0dd",
  "url": "https://rest.uniprot.org/uniprotkb/D4QD81.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D4QD81.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":32,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2010-06-15\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:05.409363+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "27d5a24c10550956afab284439c23ad93d6c94ed57b9a87ce791ea4e4597d0dd",
  "url": "https://rest.uniprot.org/uniprotkb/D4QD81.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D4QD81.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Bush tick\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"BAI99729.1\",\"source\":\"EMBL\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Chelicerata\",\"Arachnida\",\"Acari\",\"Parasitiformes\",\"Ixodida\",\"Ixodoidea\",\"Ixodidae\",\"Haemaphysalinae\",\"Haemaphysalis\"],\"scientificName\":\"Haemaphysalis longicornis\",\"taxonId\":44386}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:05.409363+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "27d5a24c10550956afab284439c23ad93d6c94ed57b9a87ce791ea4e4597d0dd",
  "url": "https://rest.uniprot.org/uniprotkb/D4QD81.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D4QD81.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"22206819\",\"source\":\"PubMed\"}],\"value\":\"3.4.21.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"19968997\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"21423674\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"21925150\",\"source\":\"PubMed\"}],\"value\":\"Longistatin\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:05.409363+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "27d5a24c10550956afab284439c23ad93d6c94ed57b9a87ce791ea4e4597d0dd",
  "url": "https://rest.uniprot.org/uniprotkb/D4QD81.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D4QD81.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"BIOPHYSICOCHEMICAL PROPERTIES\",\"phDependence\":{\"texts\":[{\"value\":\"Optimum pH is 7.0.\"}]},\"temperatureDependence\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"22206819\",\"source\":\"PubMed\"}],\"value\":\"Optimum temperature is 37 degrees Celsius. Active from 20 to 45 degrees Celsius.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-01T06:25:05.409363+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "27d5a24c10550956afab284439c23ad93d6c94ed57b9a87ce791ea4e4597d0dd",
  "url": "https://rest.uniprot.org/uniprotkb/D4QD81.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D4QD81.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Anisuzzaman X.\",\"Islam M.K.\",\"Miyoshi T.\",\"Alim M.A.\",\"Hatta T.\",\"Yamaji K.\",\"Matsumoto Y.\",\"Fujisaki K.\",\"Tsuji N.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"19968997\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.ijpara.2009.11.004\"}],\"citationType\":\"journal article\",\"firstPage\":\"721\",\"id\":\"19968997\",\"journal\":\"Int. J. Parasitol.\",\"lastPage\":\"729\",\"publicationDate\":\"2010\",\"title\":\"Longistatin, a novel EF-hand protein from the ixodid tick Haemaphysalis longicornis, is required for acquisition of host blood-meals.\",\"volume\":\"40\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"BAI99729.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"SUBCELLULAR LOCATION\",\"TISSUE SPECIFICITY\",\"DEVELOPMENTAL STAGE\",\"INDUCTION BY BLOOD FEEDING\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:25:05.409363+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "27d5a24c10550956afab284439c23ad93d6c94ed57b9a87ce791ea4e4597d0dd",
  "url": "https://rest.uniprot.org/uniprotkb/D4QD81.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D4QD81.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Anisuzzaman X.\",\"Khyrul Islam M.\",\"Abdul Alim M.\",\"Miyoshi T.\",\"Hatta T.\",\"Yamaji K.\",\"Matsumoto Y.\",\"Fujisaki K.\",\"Tsuji N.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"21925150\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.bbrc.2011.09.009\"}],\"citationType\":\"journal article\",\"firstPage\":\"599\",\"id\":\"21925150\",\"journal\":\"Biochem. Biophys. Res. Commun.\",\"lastPage\":\"604\",\"publicationDate\":\"2011\",\"title\":\"Longistatin, a novel plasminogen activator from vector ticks, is resistant to plasminogen activator inhibitor-1.\",\"volume\":\"413\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"ACTIVITY REGULATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:25:05.409363+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "27d5a24c10550956afab284439c23ad93d6c94ed57b9a87ce791ea4e4597d0dd",
  "url": "https://rest.uniprot.org/uniprotkb/D4QD81.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D4QD81.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Anisuzzaman X.\",\"Islam M.K.\",\"Alim M.A.\",\"Miyoshi T.\",\"Hatta T.\",\"Yamaji K.\",\"Matsumoto Y.\",\"Fujisaki K.\",\"Tsuji N.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"21423674\"},{\"database\":\"DOI\",\"id\":\"10.1371/journal.ppat.1001312\"}],\"citationType\":\"journal article\",\"firstPage\":\"e1001312\",\"id\":\"21423674\",\"journal\":\"PLoS Pathog.\",\"lastPage\":\"e1001312\",\"publicationDate\":\"2011\",\"title\":\"Longistatin, a plasminogen activator, is key to the availability of blood-meals for ixodid ticks.\",\"volume\":\"7\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"INTERACTION WITH HOST FIBRIN\",\"TISSUE SPECIFICITY\",\"INDUCTION BY BLOOD FEEDING\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-01T06:25:05.409363+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "27d5a24c10550956afab284439c23ad93d6c94ed57b9a87ce791ea4e4597d0dd",
  "url": "https://rest.uniprot.org/uniprotkb/D4QD81.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D4QD81.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Anisuzzaman X.\",\"Islam M.K.\",\"Alim M.A.\",\"Miyoshi T.\",\"Hatta T.\",\"Yamaji K.\",\"Matsumoto Y.\",\"Fujisaki K.\",\"Tsuji N.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"22206819\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.molbiopara.2011.12.002\"}],\"citationType\":\"journal article\",\"firstPage\":\"45\",\"id\":\"22206819\",\"journal\":\"Mol. Biochem. Parasitol.\",\"lastPage\":\"53\",\"publicationDate\":\"2012\",\"title\":\"Longistatin is an unconventional serine protease and induces protective immunity against tick infestation.\",\"volume\":\"182\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"TISSUE SPECIFICITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-01T06:25:05.409363+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "27d5a24c10550956afab284439c23ad93d6c94ed57b9a87ce791ea4e4597d0dd",
  "url": "https://rest.uniprot.org/uniprotkb/D4QD81.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D4QD81?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H1",
  "excerpt": "ID   LONG_HAELO              Reviewed;         156 AA.\nAC   D4QD81;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   15-JUN-2010, sequence version 1.\nDT   28-JAN-2026, entry version 31.\nDE   RecName: Full=Longistatin {ECO:0000303|PubMed:19968997, ECO:0000303|PubMed:21423674, ECO:0000303|PubMed:21925150};\nDE            EC=3.4.21.- {ECO:0000269|PubMed:22206819};\nDE   Flags: Precursor;\nGN   Name=A01M12 {ECO:0000312|EMBL:BAI99729.1};\nOS   Haemaphysalis longicornis (Bush tick).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Chelicerata; Arachnida; Acari;\nOC   Parasitiformes; Ixodida; Ixodoidea; Ixodidae; Haemaphysalinae;\nOC   Haemaphysalis.\nOX   NCBI_TaxID=44386 {ECO:0000312|EMBL:BAI99729.1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:00.036900+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "33d72b54de397540314c319d5d65281dcef13ef22f478476c602e399ba6c861a",
  "url": "https://rest.uniprot.org/unisave/D4QD81?format=txt&versions=31"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D4QD81?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:BAI99729.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, SUBCELLULAR LOCATION, TISSUE\nRP   SPECIFICITY, DEVELOPMENTAL STAGE, AND INDUCTION BY BLOOD FEEDING.\nRX   PubMed=19968997; DOI=10.1016/j.ijpara.2009.11.004;\nRA   Anisuzzaman X., Islam M.K., Miyoshi T., Alim M.A., Hatta T., Yamaji K.,\nRA   Matsumoto Y., Fujisaki K., Tsuji N.;\nRT   \"Longistatin, a novel EF-hand protein from the ixodid tick Haemaphysalis\nRT   longicornis, is required for acquisition of host blood-meals.\";\nRL   Int. J. Parasitol. 40:721-729(2010).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:00.036900+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 15-23",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "33d72b54de397540314c319d5d65281dcef13ef22f478476c602e399ba6c861a",
  "url": "https://rest.uniprot.org/unisave/D4QD81?format=txt&versions=31"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D4QD81?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H3",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, AND ACTIVITY REGULATION.\nRX   PubMed=21925150; DOI=10.1016/j.bbrc.2011.09.009;\nRA   Anisuzzaman X., Khyrul Islam M., Abdul Alim M., Miyoshi T., Hatta T.,\nRA   Yamaji K., Matsumoto Y., Fujisaki K., Tsuji N.;\nRT   \"Longistatin, a novel plasminogen activator from vector ticks, is resistant\nRT   to plasminogen activator inhibitor-1.\";\nRL   Biochem. Biophys. Res. Commun. 413:599-604(2011).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:00.036900+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 24-31",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "33d72b54de397540314c319d5d65281dcef13ef22f478476c602e399ba6c861a",
  "url": "https://rest.uniprot.org/unisave/D4QD81?format=txt&versions=31"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D4QD81?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H4",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, INTERACTION WITH HOST FIBRIN, TISSUE SPECIFICITY, INDUCTION BY\nRP   BLOOD FEEDING, AND DISRUPTION PHENOTYPE.\nRX   PubMed=21423674; DOI=10.1371/journal.ppat.1001312;\nRA   Anisuzzaman X., Islam M.K., Alim M.A., Miyoshi T., Hatta T., Yamaji K.,\nRA   Matsumoto Y., Fujisaki K., Tsuji N.;\nRT   \"Longistatin, a plasminogen activator, is key to the availability of blood-\nRT   meals for ixodid ticks.\";\nRL   PLoS Pathog. 7:e1001312-e1001312(2011).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:00.036900+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 32-40",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "33d72b54de397540314c319d5d65281dcef13ef22f478476c602e399ba6c861a",
  "url": "https://rest.uniprot.org/unisave/D4QD81?format=txt&versions=31"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D4QD81?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H5",
  "excerpt": "RN   [4] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, BIOPHYSICOCHEMICAL\nRP   PROPERTIES, AND TISSUE SPECIFICITY.\nRX   PubMed=22206819; DOI=10.1016/j.molbiopara.2011.12.002;\nRA   Anisuzzaman X., Islam M.K., Alim M.A., Miyoshi T., Hatta T., Yamaji K.,\nRA   Matsumoto Y., Fujisaki K., Tsuji N.;\nRT   \"Longistatin is an unconventional serine protease and induces protective\nRT   immunity against tick infestation.\";\nRL   Mol. Biochem. Parasitol. 182:45-53(2012).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:00.036900+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 41-49",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "33d72b54de397540314c319d5d65281dcef13ef22f478476c602e399ba6c861a",
  "url": "https://rest.uniprot.org/unisave/D4QD81?format=txt&versions=31"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D4QD81?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H6",
  "excerpt": "CC   -!- BIOPHYSICOCHEMICAL PROPERTIES:\nCC       pH dependence:\nCC         Optimum pH is 7.0.;\nCC       Temperature dependence:\nCC         Optimum temperature is 37 degrees Celsius. Active from 20 to 45\nCC         degrees Celsius. {ECO:0000269|PubMed:22206819};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:00.036900+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 91-96",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "33d72b54de397540314c319d5d65281dcef13ef22f478476c602e399ba6c861a",
  "url": "https://rest.uniprot.org/unisave/D4QD81?format=txt&versions=31"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/temperature.json), zero-based source row 24. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
