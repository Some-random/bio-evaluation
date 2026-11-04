# EC_number_0017

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0017.txt)

**Task:** `EC_number`  
**Expected answer:** **A** — 1.97.1.14

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MGSKETKNTSRRDFLIKGAGAAALGAGAFAISQVPLLEKLASANEDTVKDLLPFPELIESDEIIIRMQNDVRRALKKPLNEIQWIMVIDLKKCVGCSSCTVACVSENVLPPGVVYRPVIEEEIGTFPNVTKKFTPRPCMQCEHPPCTKVCPIGATYKSEDGIVAIDYDKCIGCRYCITACPYGARTFDWGEYHTENTPEIMQYEKEPNYEYGVERVREKKNSPIGNARKCHFCKHRLHKGMLSMCVTTCIGRATYIGDKNDPESLVAELIASPRVMRLKEELGTEPNVYYLT

[Multiple Choices]
A. 1.97.1.14
B. 1.97.1.13
C. 2.5.1.76
D. 2.7.1.52
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

> The sequence-matched UniProt record assigns EC 1.97.1.14 to this protein and links that assignment to a cited characterization of the selenate reductase complex. Its catalytic-activity annotation also gives the reaction and the same EC number. This supports the key, though the excerpts report database annotations and citations rather than the experimental details themselves.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has multiple cysteine-rich regions consistent with iron-sulfur centers and an N-terminal hydrophobic segment, supporting recognition as a membrane-associated respiratory electron-transfer subunit. A solver recognizing the broader SrdB-like family from related proteins could infer association with a selenate-reductase system, favoring A over the unrelated enzyme classes and the alternative EC. This is a family-level, probabilistic inference, not proof of the exact reaction from these features alone.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable recognition of the respiratory selenate-reductase subunit family provides a meaningful basis for preferring A. The sequence features are not uniquely diagnostic by themselves, so confidence in the exact EC assignment is limited.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No second option is identified as comparably defensible from the supplied choices.


### Important caveats

- The cited EC activity is associated with the selenate-reductase complex; the annotated subunit is described as an electron-transport subunit, not necessarily a standalone catalyst.
- Reviewer-only source annotations support the key but were not available as input to the evaluated solver.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has multiple cysteine-rich regions consistent with iron-sulfur centers and an N-terminal hydrophobic segment, supporting recognition as a membrane-associated respiratory electron-transfer subunit. A solver recognizing the broader SrdB-like family from related proteins could infer association with a selenate-reductase system, favoring A over the unrelated enzyme classes and the alternative EC. This is a family-level, probabilistic inference, not proof of the exact reaction from these features alone.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable recognition of the respiratory selenate-reductase subunit family provides a meaningful basis for preferring A. The sequence features are not uniquely diagnostic by themselves, so confidence in the exact EC assignment is limited."
  },
  "case_id": "EC_number_0017",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 1.97.1.14 to this protein and links that assignment to a cited characterization of the selenate reductase complex. Its catalytic-activity annotation also gives the reaction and the same EC number. This supports the key, though the excerpts report database annotations and citations rather than the experimental details themselves."
  },
  "important_caveats": [
    "The cited EC activity is associated with the selenate-reductase complex; the annotated subunit is described as an electron-transport subunit, not necessarily a standalone catalyst.",
    "Reviewer-only source annotations support the key but were not available as input to the evaluated solver."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No second option is identified as comparably defensible from the supplied choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0017",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 1.97.1.14 to this protein and links that assignment to a cited characterization of the selenate reductase complex. Its catalytic-activity annotation also gives the reaction and the same EC number. This supports the key, though the excerpts report database annotations and citations rather than the experimental details themselves.",
    "evidence_ids": ["C4", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has multiple cysteine-rich regions consistent with iron-sulfur centers and an N-terminal hydrophobic segment, supporting recognition as a membrane-associated respiratory electron-transfer subunit. A solver recognizing the broader SrdB-like family from related proteins could infer association with a selenate-reductase system, favoring A over the unrelated enzyme classes and the alternative EC. This is a family-level, probabilistic inference, not proof of the exact reaction from these features alone.",
    "missing_item_specific_fact": "",
    "reason": "Transferable recognition of the respiratory selenate-reductase subunit family provides a meaningful basis for preferring A. The sequence features are not uniquely diagnostic by themselves, so confidence in the exact EC assignment is limited."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No second option is identified as comparably defensible from the supplied choices."
  },
  "important_caveats": [
    "The cited EC activity is associated with the selenate-reductase complex; the annotated subunit is described as an electron-transport subunit, not necessarily a standalone catalyst.",
    "Reviewer-only source annotations support the key but were not available as input to the evaluated solver."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A0A8X5N4, SRDB_MESS1) annotates this 292-aa protein as 'Selenate reductase subunit B' with EC 1.97.1.14, supported by experimental evidence (ECO:0000305, PubMed:21357486) describing the srdBCA operon encoding the respiratory selenate reductase complex. The catalytic activity is selenite + quinone + H2O = selenate + quinol. The sequence matches the benchmark input exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple iron-sulfur cluster binding motifs: a &#91;2Fe-2S&#93;-type region (CVGCSSCTVACVSE), a &#91;4Fe-4S&#93;-type region (CIGCRYCITACPY), and a C-H-F-C/4Fe-4S region (CHFCKHRLHKGMLSMCVTTCIGRATY). An N-terminal signal peptide (MGSKETKNTSRRDFLIKGAGAAALGAGAFAISQVPLLEK) indicates membrane association. These features are hallmarks of an electron-transport subunit of a respiratory oxidoreductase complex, which immediately eliminates C (2.5.1.76, an alkyl/aryl transferase) and D (2.7.1.52, a phosphotransferase) because neither class uses Fe-S clusters or membrane-associated electron transport. Both A (1.97.1.14) and B (1.97.1.13) fall within EC 1.97.1.x (oxidoreductases acting on other nitrogenous compounds), so the Fe-S/signal-peptide evidence narrows to this sub-subclass but does not fully separate A from B. The specific Fe-S cluster architecture—three distinct Cys-rich clusters in a ~292-aa subunit with a Sec-type signal peptide—is characteristic of the SrdB-type electron transport subunit found in selenate-reducing Bacillus/related organisms, a family-level pattern learned from homologous respiratory reductase complexes (e.g., perchlorate/chlorate reductase electron transport subunits share Fe-S motifs but differ in cluster count, spacing, and accessory motifs). The particular Cys spacing and the C-H-F-C motif in the third cluster align with selenate reductase subunit B rather than the alternative in EC 1.97.1.13. This is a probabilistic family-level inference, not a certainty, but it meaningfully favors A over B.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The Fe-S cluster motifs and signal peptide provide a strong, transferable inference eliminating the two transferase options (C, D). The specific Fe-S cluster architecture and overall domain organization are consistent with the selenate reductase subunit B family, giving a credible (if not airtight) basis to prefer A over B. The A-vs-B distinction is the hardest part and relies on family-level pattern recognition rather than a single unambiguous sequence signature, but it does not require memorizing this exact protein's database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Both A (1.97.1.14) and B (1.97.1.13) belong to the same EC sub-subclass (oxidoreductases acting on other nitrogenous compounds as acceptors) and would both plausibly use an Fe-S-containing electron transport subunit. Without prior knowledge of which specific reductase complex this subunit belongs to, a model could reasonably hesitate between these two choices. The discrimination relies on subtle family-level sequence patterns rather than a single decisive feature.


### Important caveats

- The EC 1.97.1.13 option's exact identity and whether it is a well-established, distinct EC entry was not independently verified; if it is a rarely used or deprecated number, the effective choice set is smaller.
- The Fe-S cluster motifs and signal peptide are necessary but not fully sufficient to distinguish 1.97.1.14 from 1.97.1.13; the inference is probabilistic and family-level.
- The UniProt annotation carries evidence code ECO:0000305 (inferred from related experimental work on the srdBCA operon), not direct purification and kinetics of this isolated subunit alone.
- The reviewer-only evidence (accession A0A0A8X5N4, organism Mesobacillus selenatarsenatis) was not available to the evaluated model; the reasoning above uses only the sequence and general biological knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple iron-sulfur cluster binding motifs: a [2Fe-2S]-type region (CVGCSSCTVACVSE), a [4Fe-4S]-type region (CIGCRYCITACPY), and a C-H-F-C/4Fe-4S region (CHFCKHRLHKGMLSMCVTTCIGRATY). An N-terminal signal peptide (MGSKETKNTSRRDFLIKGAGAAALGAGAFAISQVPLLEK) indicates membrane association. These features are hallmarks of an electron-transport subunit of a respiratory oxidoreductase complex, which immediately eliminates C (2.5.1.76, an alkyl/aryl transferase) and D (2.7.1.52, a phosphotransferase) because neither class uses Fe-S clusters or membrane-associated electron transport. Both A (1.97.1.14) and B (1.97.1.13) fall within EC 1.97.1.x (oxidoreductases acting on other nitrogenous compounds), so the Fe-S/signal-peptide evidence narrows to this sub-subclass but does not fully separate A from B. The specific Fe-S cluster architecture—three distinct Cys-rich clusters in a ~292-aa subunit with a Sec-type signal peptide—is characteristic of the SrdB-type electron transport subunit found in selenate-reducing Bacillus/related organisms, a family-level pattern learned from homologous respiratory reductase complexes (e.g., perchlorate/chlorate reductase electron transport subunits share Fe-S motifs but differ in cluster count, spacing, and accessory motifs). The particular Cys spacing and the C-H-F-C motif in the third cluster align with selenate reductase subunit B rather than the alternative in EC 1.97.1.13. This is a probabilistic family-level inference, not a certainty, but it meaningfully favors A over B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The Fe-S cluster motifs and signal peptide provide a strong, transferable inference eliminating the two transferase options (C, D). The specific Fe-S cluster architecture and overall domain organization are consistent with the selenate reductase subunit B family, giving a credible (if not airtight) basis to prefer A over B. The A-vs-B distinction is the hardest part and relies on family-level pattern recognition rather than a single unambiguous sequence signature, but it does not require memorizing this exact protein's database record."
  },
  "case_id": "EC_number_0017",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A0A8X5N4, SRDB_MESS1) annotates this 292-aa protein as 'Selenate reductase subunit B' with EC 1.97.1.14, supported by experimental evidence (ECO:0000305, PubMed:21357486) describing the srdBCA operon encoding the respiratory selenate reductase complex. The catalytic activity is selenite + quinone + H2O = selenate + quinol. The sequence matches the benchmark input exactly."
  },
  "important_caveats": [
    "The EC 1.97.1.13 option's exact identity and whether it is a well-established, distinct EC entry was not independently verified; if it is a rarely used or deprecated number, the effective choice set is smaller.",
    "The Fe-S cluster motifs and signal peptide are necessary but not fully sufficient to distinguish 1.97.1.14 from 1.97.1.13; the inference is probabilistic and family-level.",
    "The UniProt annotation carries evidence code ECO:0000305 (inferred from related experimental work on the srdBCA operon), not direct purification and kinetics of this isolated subunit alone.",
    "The reviewer-only evidence (accession A0A0A8X5N4, organism Mesobacillus selenatarsenatis) was not available to the evaluated model; the reasoning above uses only the sequence and general biological knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Both A (1.97.1.14) and B (1.97.1.13) belong to the same EC sub-subclass (oxidoreductases acting on other nitrogenous compounds as acceptors) and would both plausibly use an Fe-S-containing electron transport subunit. Without prior knowledge of which specific reductase complex this subunit belongs to, a model could reasonably hesitate between these two choices. The discrimination relies on subtle family-level sequence patterns rather than a single decisive feature."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0017",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A0A8X5N4, SRDB_MESS1) annotates this 292-aa protein as 'Selenate reductase subunit B' with EC 1.97.1.14, supported by experimental evidence (ECO:0000305, PubMed:21357486) describing the srdBCA operon encoding the respiratory selenate reductase complex. The catalytic activity is selenite + quinone + H2O = selenate + quinol. The sequence matches the benchmark input exactly.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple iron-sulfur cluster binding motifs: a [2Fe-2S]-type region (CVGCSSCTVACVSE), a [4Fe-4S]-type region (CIGCRYCITACPY), and a C-H-F-C/4Fe-4S region (CHFCKHRLHKGMLSMCVTTCIGRATY). An N-terminal signal peptide (MGSKETKNTSRRDFLIKGAGAAALGAGAFAISQVPLLEK) indicates membrane association. These features are hallmarks of an electron-transport subunit of a respiratory oxidoreductase complex, which immediately eliminates C (2.5.1.76, an alkyl/aryl transferase) and D (2.7.1.52, a phosphotransferase) because neither class uses Fe-S clusters or membrane-associated electron transport. Both A (1.97.1.14) and B (1.97.1.13) fall within EC 1.97.1.x (oxidoreductases acting on other nitrogenous compounds), so the Fe-S/signal-peptide evidence narrows to this sub-subclass but does not fully separate A from B. The specific Fe-S cluster architecture—three distinct Cys-rich clusters in a ~292-aa subunit with a Sec-type signal peptide—is characteristic of the SrdB-type electron transport subunit found in selenate-reducing Bacillus/related organisms, a family-level pattern learned from homologous respiratory reductase complexes (e.g., perchlorate/chlorate reductase electron transport subunits share Fe-S motifs but differ in cluster count, spacing, and accessory motifs). The particular Cys spacing and the C-H-F-C motif in the third cluster align with selenate reductase subunit B rather than the alternative in EC 1.97.1.13. This is a probabilistic family-level inference, not a certainty, but it meaningfully favors A over B.",
    "missing_item_specific_fact": "",
    "reason": "The Fe-S cluster motifs and signal peptide provide a strong, transferable inference eliminating the two transferase options (C, D). The specific Fe-S cluster architecture and overall domain organization are consistent with the selenate reductase subunit B family, giving a credible (if not airtight) basis to prefer A over B. The A-vs-B distinction is the hardest part and relies on family-level pattern recognition rather than a single unambiguous sequence signature, but it does not require memorizing this exact protein's database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Both A (1.97.1.14) and B (1.97.1.13) belong to the same EC sub-subclass (oxidoreductases acting on other nitrogenous compounds as acceptors) and would both plausibly use an Fe-S-containing electron transport subunit. Without prior knowledge of which specific reductase complex this subunit belongs to, a model could reasonably hesitate between these two choices. The discrimination relies on subtle family-level sequence patterns rather than a single decisive feature."
  },
  "important_caveats": [
    "The EC 1.97.1.13 option's exact identity and whether it is a well-established, distinct EC entry was not independently verified; if it is a rarely used or deprecated number, the effective choice set is smaller.",
    "The Fe-S cluster motifs and signal peptide are necessary but not fully sufficient to distinguish 1.97.1.14 from 1.97.1.13; the inference is probabilistic and family-level.",
    "The UniProt annotation carries evidence code ECO:0000305 (inferred from related experimental work on the srdBCA operon), not direct purification and kinetics of this isolated subunit alone.",
    "The reviewer-only evidence (accession A0A0A8X5N4, organism Mesobacillus selenatarsenatis) was not available to the evaluated model; the reasoning above uses only the sequence and general biological knowledge."
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
  "benchmark_sequence_length": 292,
  "benchmark_sequence_sha256": "235529ed4cdd4907b4cde6312a1c0e5dd237655b162eef3a5632d65e9b7cec97",
  "current_entry_audit": {
    "entryVersion": 30,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2015-03-04",
    "sequenceVersion": 1
  },
  "current_record_sha256": "ad4296ea74491ed50535947ea88c00f59f9264d4b7e02a26604d154b65d36999",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 292,
  "current_source_sequence_sha256": "235529ed4cdd4907b4cde6312a1c0e5dd237655b162eef3a5632d65e9b7cec97",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 28,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A0A8X5N4",
  "selected_historical_entry_version": 28,
  "selected_historical_record_sha256": "d0917601898661906f576d07a10b60378261919ac0854faebd606db893a6272d",
  "selected_historical_source_sequence_length": 292,
  "selected_historical_source_sequence_sha256": "235529ed4cdd4907b4cde6312a1c0e5dd237655b162eef3a5632d65e9b7cec97",
  "selected_historical_version": {
    "accession": "A0A0A8X5N4",
    "database": "Swiss-Prot",
    "entryVersion": 28,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "SRDB_MESS1",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X5N4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A0A8X5N4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:23:58.709600+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ad4296ea74491ed50535947ea88c00f59f9264d4b7e02a26604d154b65d36999",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0A8X5N4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X5N4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":30,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2015-03-04\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:23:58.709600+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ad4296ea74491ed50535947ea88c00f59f9264d4b7e02a26604d154b65d36999",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0A8X5N4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X5N4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Bacillati\",\"Bacillota\",\"Bacilli\",\"Caryophanales\",\"Bacillaceae\",\"Mesobacillus\"],\"scientificName\":\"Mesobacillus selenatarsenatis (strain DSM 18680 / JCM 14380 / FERM P-15431 / SF-1)\",\"taxonId\":1321606}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:23:58.709600+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ad4296ea74491ed50535947ea88c00f59f9264d4b7e02a26604d154b65d36999",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0A8X5N4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X5N4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Selenate reductase electron transport subunit\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"21357486\",\"source\":\"PubMed\"}],\"value\":\"1.97.1.14\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Selenate reductase subunit B\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:23:58.709600+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ad4296ea74491ed50535947ea88c00f59f9264d4b7e02a26604d154b65d36999",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0A8X5N4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X5N4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"1.97.1.14\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"21357486\",\"source\":\"PubMed\"}],\"name\":\"selenite + a quinone + H2O = selenate + a quinol\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:51636\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15075\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:18212\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:24646\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:132124\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:23:58.709600+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ad4296ea74491ed50535947ea88c00f59f9264d4b7e02a26604d154b65d36999",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0A8X5N4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X5N4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Kuroda M.\",\"Yamashita M.\",\"Miwa E.\",\"Imao K.\",\"Fujimoto N.\",\"Ono H.\",\"Nagano K.\",\"Sei K.\",\"Ike M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"21357486\"},{\"database\":\"DOI\",\"id\":\"10.1128/jb.01197-10\"}],\"citationType\":\"journal article\",\"firstPage\":\"2141\",\"id\":\"21357486\",\"journal\":\"J. Bacteriol.\",\"lastPage\":\"2148\",\"publicationDate\":\"2011\",\"title\":\"Molecular cloning and characterization of the srdBCA operon, encoding the respiratory selenate reductase complex, from the selenate-reducing bacterium Bacillus selenatarsenatis SF-1.\",\"volume\":\"193\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"BAJ83592.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"DSM 18680 / JCM 14380 / FERM P-15431 / SF-1\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION AS A SELENATE REDUCTASE\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:23:58.709600+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ad4296ea74491ed50535947ea88c00f59f9264d4b7e02a26604d154b65d36999",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0A8X5N4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X5N4?format=txt&versions=28)

```json
{
  "entry_version": 28,
  "evidence_id": "H1",
  "excerpt": "ID   SRDB_MESS1              Reviewed;         292 AA.\nAC   A0A0A8X5N4; E9RFC9;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   04-MAR-2015, sequence version 1.\nDT   28-JAN-2026, entry version 28.\nDE   RecName: Full=Selenate reductase subunit B {ECO:0000305};\nDE            EC=1.97.1.14 {ECO:0000305|PubMed:21357486};\nDE   AltName: Full=Selenate reductase electron transport subunit {ECO:0000305};\nDE   Flags: Precursor;\nGN   Name=srdB {ECO:0000303|PubMed:21357486};\nGN   ORFNames=SAMD00020551_1550 {ECO:0000312|EMBL:GAM13406.1};\nOS   Mesobacillus selenatarsenatis (strain DSM 18680 / JCM 14380 / FERM P-15431\nOS   / SF-1).\nOC   Bacteria; Bacillati; Bacillota; Bacilli; Bacillales; Bacillaceae;\nOC   Mesobacillus.\nOX   NCBI_TaxID=1321606;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:01.544310+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d0917601898661906f576d07a10b60378261919ac0854faebd606db893a6272d",
  "url": "https://rest.uniprot.org/unisave/A0A0A8X5N4?format=txt&versions=28"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X5N4?format=txt&versions=28)

```json
{
  "entry_version": 28,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Selenate reductase subunit B {ECO:0000305};\nDE            EC=1.97.1.14 {ECO:0000305|PubMed:21357486};\nDE   AltName: Full=Selenate reductase electron transport subunit {ECO:0000305};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:01.544310+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-9",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d0917601898661906f576d07a10b60378261919ac0854faebd606db893a6272d",
  "url": "https://rest.uniprot.org/unisave/A0A0A8X5N4?format=txt&versions=28"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X5N4?format=txt&versions=28)

```json
{
  "entry_version": 28,
  "evidence_id": "H3",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:BAJ83592.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION AS A SELENATE REDUCTASE, AND\nRP   SUBUNIT.\nRC   STRAIN=DSM 18680 / JCM 14380 / FERM P-15431 / SF-1;\nRX   PubMed=21357486; DOI=10.1128/jb.01197-10;\nRA   Kuroda M., Yamashita M., Miwa E., Imao K., Fujimoto N., Ono H., Nagano K.,\nRA   Sei K., Ike M.;\nRT   \"Molecular cloning and characterization of the srdBCA operon, encoding the\nRT   respiratory selenate reductase complex, from the selenate-reducing\nRT   bacterium Bacillus selenatarsenatis SF-1.\";\nRL   J. Bacteriol. 193:2141-2148(2011).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:01.544310+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 17-27",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d0917601898661906f576d07a10b60378261919ac0854faebd606db893a6272d",
  "url": "https://rest.uniprot.org/unisave/A0A0A8X5N4?format=txt&versions=28"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X5N4?format=txt&versions=28)

```json
{
  "entry_version": 28,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=selenite + a quinone + H2O = selenate + a quinol;\nCC         Xref=Rhea:RHEA:51636, ChEBI:CHEBI:15075, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:18212, ChEBI:CHEBI:24646, ChEBI:CHEBI:132124;\nCC         EC=1.97.1.14; Evidence={ECO:0000305|PubMed:21357486};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:01.544310+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 42-46",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d0917601898661906f576d07a10b60378261919ac0854faebd606db893a6272d",
  "url": "https://rest.uniprot.org/unisave/A0A0A8X5N4?format=txt&versions=28"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 17. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
