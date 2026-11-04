# EC_number_0056

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0056.txt)

**Task:** `EC_number`  
**Expected answer:** **A** — 5.1.1.24

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MDGKVQVLDFIKINPAGNITILIDNFDIYDKNIPKLSEEIMKETNLYAEQVGFIKEKHLQMMGGEFCGNASRSFASLLAFRDKDFSEQKNYSITCSGESEVLDVDVRTDGAKNKFLAKIKMPKFISLEEISIDEYKLGLVRFSGISHFIFNIKENKETSFENIIDLVKKYLSNEDYSAFGIMFFDKDNLSMKPYVYVKELESGIYENSCASGTTALGYYLKKYKNLDRAKVVQPNGWLEYIIENDEMYIDGPVEIVAEGKVYI

[Multiple Choices]
A. 5.1.1.24
B. 5.1.1.25
C. 4.3.3.9
D. 5.3.1.16
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

> The sequence-matched UniProt entry assigns EC 5.1.1.24 and describes the reaction L-histidine = D-histidine, citing experimental evidence (ECO:0000269). The archived entry also records this assignment. The cited study was not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Sequence features might suggest a cofactor-independent racemase and thus help distinguish racemase choices from unrelated reaction classes. But that alone does not establish histidine rather than another amino-acid substrate.


**Missing item-specific fact**

> Whether this exact protein catalyzes histidine racemization rather than the alternative racemase reaction; the supplied input gives no substrate assay or established substrate-specific family signature.


**Reason**

> The key distinction between the offered racemase alternatives is substrate specificity. No concrete transferable feature in the supplied sequence is established here as distinguishing those substrates, so the supported choice depends on protein-specific functional evidence or its annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched functional annotation supports A; the supplied evidence does not support another offered choice.


### Important caveats

- The database annotation cites a 2024 publication as experimental evidence, but that publication was not independently assessed.
- The exact author source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Sequence features might suggest a cofactor-independent racemase and thus help distinguish racemase choices from unrelated reaction classes. But that alone does not establish histidine rather than another amino-acid substrate.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Whether this exact protein catalyzes histidine racemization rather than the alternative racemase reaction; the supplied input gives no substrate assay or established substrate-specific family signature.",
    "reason": "The key distinction between the offered racemase alternatives is substrate specificity. No concrete transferable feature in the supplied sequence is established here as distinguishing those substrates, so the supported choice depends on protein-specific functional evidence or its annotation."
  },
  "case_id": "EC_number_0056",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry assigns EC 5.1.1.24 and describes the reaction L-histidine = D-histidine, citing experimental evidence (ECO:0000269). The archived entry also records this assignment. The cited study was not independently reviewed here."
  },
  "important_caveats": [
    "The database annotation cites a 2024 publication as experimental evidence, but that publication was not independently assessed.",
    "The exact author source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched functional annotation supports A; the supplied evidence does not support another offered choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0056",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry assigns EC 5.1.1.24 and describes the reaction L-histidine = D-histidine, citing experimental evidence (ECO:0000269). The archived entry also records this assignment. The cited study was not independently reviewed here.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Sequence features might suggest a cofactor-independent racemase and thus help distinguish racemase choices from unrelated reaction classes. But that alone does not establish histidine rather than another amino-acid substrate.",
    "missing_item_specific_fact": "Whether this exact protein catalyzes histidine racemization rather than the alternative racemase reaction; the supplied input gives no substrate assay or established substrate-specific family signature.",
    "reason": "The key distinction between the offered racemase alternatives is substrate specificity. No concrete transferable feature in the supplied sequence is established here as distinguishing those substrates, so the supported choice depends on protein-specific functional evidence or its annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched functional annotation supports A; the supplied evidence does not support another offered choice."
  },
  "important_caveats": [
    "The database annotation cites a 2024 publication as experimental evidence, but that publication was not independently assessed.",
    "The exact author source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry D5RFM4 (HISR_FUSN2) is annotated as 'Histidine racemase' with EC 5.1.1.24, supported by experimental evidence (ECO:0000269, PubMed 39424140, J. Biol. Chem. 2024). The catalytic activity is L-histidine = D-histidine. The benchmark sequence matches the UniProt sequence exactly (SHA256 confirmed). The expected answer A (5.1.1.24) is fully supported by experimental characterization.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> The specific substrate identity (histidine) and the fact that this is a cofactor-independent racemase with a novel fold/mechanism, as characterized experimentally in 2024 (PubMed 39424140). The sequence lacks PLP-binding motifs (e.g., TxxxD, conserved Lys for Schiff base) shared by the well-studied PLP-dependent amino acid racemases (alanine, glutamate, serine racemases), so family-level transfer from those enzymes does not apply. Distinguishing 5.1.1.24 (histidine racemase) from 5.1.1.25 (another amino acid racemase, if it exists) requires knowing which specific amino acid is the substrate, which cannot be inferred from the 263-aa sequence alone. Distinguishing the racemase class (5.1.1) from a lyase (4.3.3.9) or intramolecular oxidoreductase (5.3.1.16) also lacks a clear sequence-based discriminator for this novel, cofactor-independent enzyme.


**Reason**

> This is a novel enzyme (first characterized 2024) that is cofactor-independent, meaning it does not share the well-known PLP-binding motifs that allow family-level inference to other amino acid racemases. The 263-aa sequence provides no obvious active-site signature that would allow a knowledgeable model to determine (a) the EC class (racemase vs. lyase vs. intramolecular oxidoreductase), or (b) the specific substrate (histidine vs. another amino acid for 5.1.1.24 vs. 5.1.1.25). General knowledge of PLP-dependent racemases, lyases, or isomerases does not transfer meaningfully to this cofactor-independent, structurally novel enzyme. The assignment of EC 5.1.1.24 to this exact sequence depends on the experimental characterization reported in the 2024 paper.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The experimental evidence unambiguously assigns EC 5.1.1.24. Option B (5.1.1.25) may not correspond to a well-established or existing EC entry, and options C (4.3.3.9, a lyase) and D (5.3.1.16, an intramolecular oxidoreductase) represent fundamentally different reaction types not supported by the experimental data. No genuine ambiguity exists in the correct answer.


### Important caveats

- The enzyme was only characterized experimentally in 2024 (PubMed 39424140), making it a very recent annotation that would not be in training data from earlier periods.
- The cofactor-independent mechanism means standard sequence-based heuristics for amino acid racemases (PLP-binding motifs) are inapplicable.
- EC 5.1.1.25 may not be a valid or well-established EC number, potentially making it a fabricated distractor rather than a genuine alternative.
- The reviewer-only source evidence confirms sequence match and experimental support, but these were not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate identity (histidine) and the fact that this is a cofactor-independent racemase with a novel fold/mechanism, as characterized experimentally in 2024 (PubMed 39424140). The sequence lacks PLP-binding motifs (e.g., TxxxD, conserved Lys for Schiff base) shared by the well-studied PLP-dependent amino acid racemases (alanine, glutamate, serine racemases), so family-level transfer from those enzymes does not apply. Distinguishing 5.1.1.24 (histidine racemase) from 5.1.1.25 (another amino acid racemase, if it exists) requires knowing which specific amino acid is the substrate, which cannot be inferred from the 263-aa sequence alone. Distinguishing the racemase class (5.1.1) from a lyase (4.3.3.9) or intramolecular oxidoreductase (5.3.1.16) also lacks a clear sequence-based discriminator for this novel, cofactor-independent enzyme.",
    "reason": "This is a novel enzyme (first characterized 2024) that is cofactor-independent, meaning it does not share the well-known PLP-binding motifs that allow family-level inference to other amino acid racemases. The 263-aa sequence provides no obvious active-site signature that would allow a knowledgeable model to determine (a) the EC class (racemase vs. lyase vs. intramolecular oxidoreductase), or (b) the specific substrate (histidine vs. another amino acid for 5.1.1.24 vs. 5.1.1.25). General knowledge of PLP-dependent racemases, lyases, or isomerases does not transfer meaningfully to this cofactor-independent, structurally novel enzyme. The assignment of EC 5.1.1.24 to this exact sequence depends on the experimental characterization reported in the 2024 paper."
  },
  "case_id": "EC_number_0056",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry D5RFM4 (HISR_FUSN2) is annotated as 'Histidine racemase' with EC 5.1.1.24, supported by experimental evidence (ECO:0000269, PubMed 39424140, J. Biol. Chem. 2024). The catalytic activity is L-histidine = D-histidine. The benchmark sequence matches the UniProt sequence exactly (SHA256 confirmed). The expected answer A (5.1.1.24) is fully supported by experimental characterization."
  },
  "important_caveats": [
    "The enzyme was only characterized experimentally in 2024 (PubMed 39424140), making it a very recent annotation that would not be in training data from earlier periods.",
    "The cofactor-independent mechanism means standard sequence-based heuristics for amino acid racemases (PLP-binding motifs) are inapplicable.",
    "EC 5.1.1.25 may not be a valid or well-established EC number, potentially making it a fabricated distractor rather than a genuine alternative.",
    "The reviewer-only source evidence confirms sequence match and experimental support, but these were not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The experimental evidence unambiguously assigns EC 5.1.1.24. Option B (5.1.1.25) may not correspond to a well-established or existing EC entry, and options C (4.3.3.9, a lyase) and D (5.3.1.16, an intramolecular oxidoreductase) represent fundamentally different reaction types not supported by the experimental data. No genuine ambiguity exists in the correct answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0056",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry D5RFM4 (HISR_FUSN2) is annotated as 'Histidine racemase' with EC 5.1.1.24, supported by experimental evidence (ECO:0000269, PubMed 39424140, J. Biol. Chem. 2024). The catalytic activity is L-histidine = D-histidine. The benchmark sequence matches the UniProt sequence exactly (SHA256 confirmed). The expected answer A (5.1.1.24) is fully supported by experimental characterization.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "The specific substrate identity (histidine) and the fact that this is a cofactor-independent racemase with a novel fold/mechanism, as characterized experimentally in 2024 (PubMed 39424140). The sequence lacks PLP-binding motifs (e.g., TxxxD, conserved Lys for Schiff base) shared by the well-studied PLP-dependent amino acid racemases (alanine, glutamate, serine racemases), so family-level transfer from those enzymes does not apply. Distinguishing 5.1.1.24 (histidine racemase) from 5.1.1.25 (another amino acid racemase, if it exists) requires knowing which specific amino acid is the substrate, which cannot be inferred from the 263-aa sequence alone. Distinguishing the racemase class (5.1.1) from a lyase (4.3.3.9) or intramolecular oxidoreductase (5.3.1.16) also lacks a clear sequence-based discriminator for this novel, cofactor-independent enzyme.",
    "reason": "This is a novel enzyme (first characterized 2024) that is cofactor-independent, meaning it does not share the well-known PLP-binding motifs that allow family-level inference to other amino acid racemases. The 263-aa sequence provides no obvious active-site signature that would allow a knowledgeable model to determine (a) the EC class (racemase vs. lyase vs. intramolecular oxidoreductase), or (b) the specific substrate (histidine vs. another amino acid for 5.1.1.24 vs. 5.1.1.25). General knowledge of PLP-dependent racemases, lyases, or isomerases does not transfer meaningfully to this cofactor-independent, structurally novel enzyme. The assignment of EC 5.1.1.24 to this exact sequence depends on the experimental characterization reported in the 2024 paper."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The experimental evidence unambiguously assigns EC 5.1.1.24. Option B (5.1.1.25) may not correspond to a well-established or existing EC entry, and options C (4.3.3.9, a lyase) and D (5.3.1.16, an intramolecular oxidoreductase) represent fundamentally different reaction types not supported by the experimental data. No genuine ambiguity exists in the correct answer."
  },
  "important_caveats": [
    "The enzyme was only characterized experimentally in 2024 (PubMed 39424140), making it a very recent annotation that would not be in training data from earlier periods.",
    "The cofactor-independent mechanism means standard sequence-based heuristics for amino acid racemases (PLP-binding motifs) are inapplicable.",
    "EC 5.1.1.25 may not be a valid or well-established EC number, potentially making it a fabricated distractor rather than a genuine alternative.",
    "The reviewer-only source evidence confirms sequence match and experimental support, but these were not available to the evaluated model."
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
  "benchmark_sequence_length": 263,
  "benchmark_sequence_sha256": "c3c062f84cb504706da4f93fc7c25a17790dd9bc3a42419a61e2a9462719a5f8",
  "current_entry_audit": {
    "entryVersion": 34,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2010-07-13",
    "sequenceVersion": 1
  },
  "current_record_sha256": "9d534f1baac31e4cc070d3002eca79de8e3da489ec484522b9820ff39ad10ecd",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 263,
  "current_source_sequence_sha256": "c3c062f84cb504706da4f93fc7c25a17790dd9bc3a42419a61e2a9462719a5f8",
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
  "requested_accession": "D5RFM4",
  "selected_historical_entry_version": 32,
  "selected_historical_record_sha256": "b43d619ca52111b53572f98986c14dc86b988a025a0364b36dd5b2547453e3cc",
  "selected_historical_source_sequence_length": 263,
  "selected_historical_source_sequence_sha256": "c3c062f84cb504706da4f93fc7c25a17790dd9bc3a42419a61e2a9462719a5f8",
  "selected_historical_version": {
    "accession": "D5RFM4",
    "database": "Swiss-Prot",
    "entryVersion": 32,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "HISR_FUSN2",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D5RFM4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"D5RFM4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:27:49.723120+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9d534f1baac31e4cc070d3002eca79de8e3da489ec484522b9820ff39ad10ecd",
  "url": "https://rest.uniprot.org/uniprotkb/D5RFM4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D5RFM4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":34,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2010-07-13\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:27:49.723120+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9d534f1baac31e4cc070d3002eca79de8e3da489ec484522b9820ff39ad10ecd",
  "url": "https://rest.uniprot.org/uniprotkb/D5RFM4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D5RFM4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Fusobacteriati\",\"Fusobacteriota\",\"Fusobacteriia\",\"Fusobacteriales\",\"Fusobacteriaceae\",\"Fusobacterium\"],\"scientificName\":\"Fusobacterium nucleatum subsp. nucleatum (strain ATCC 23726 / VPI 4351)\",\"taxonId\":525283}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:27:49.723120+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9d534f1baac31e4cc070d3002eca79de8e3da489ec484522b9820ff39ad10ecd",
  "url": "https://rest.uniprot.org/uniprotkb/D5RFM4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D5RFM4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39424140\",\"source\":\"PubMed\"}],\"value\":\"5.1.1.24\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39424140\",\"source\":\"PubMed\"}],\"value\":\"Histidine racemase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:27:49.723120+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9d534f1baac31e4cc070d3002eca79de8e3da489ec484522b9820ff39ad10ecd",
  "url": "https://rest.uniprot.org/uniprotkb/D5RFM4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D5RFM4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"5.1.1.24\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39424140\",\"source\":\"PubMed\"}],\"name\":\"L-histidine = D-histidine\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:59188\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57595\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:142967\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:27:49.723120+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9d534f1baac31e4cc070d3002eca79de8e3da489ec484522b9820ff39ad10ecd",
  "url": "https://rest.uniprot.org/uniprotkb/D5RFM4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D5RFM4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Lamer T.\",\"Chen P.\",\"Venter M.J.\",\"van Belkum M.J.\",\"Wijewardane A.\",\"Wu C.\",\"Lemieux M.J.\",\"Vederas J.C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39424140\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.jbc.2024.107896\"}],\"citationType\":\"journal article\",\"firstPage\":\"107896\",\"id\":\"39424140\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"107896\",\"publicationDate\":\"2024\",\"title\":\"Discovery, characterization, and structure of a cofactor-independent histidine racemase from the oral pathogen Fusobacterium nucleatum.\",\"volume\":\"300\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC 23726 / VPI 4351\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:27:49.723120+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9d534f1baac31e4cc070d3002eca79de8e3da489ec484522b9820ff39ad10ecd",
  "url": "https://rest.uniprot.org/uniprotkb/D5RFM4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D5RFM4?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H1",
  "excerpt": "ID   HISR_FUSN2              Reviewed;         263 AA.\nAC   D5RFM4;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   13-JUL-2010, sequence version 1.\nDT   28-JAN-2026, entry version 32.\nDE   RecName: Full=Histidine racemase {ECO:0000303|PubMed:39424140};\nDE            EC=5.1.1.24 {ECO:0000269|PubMed:39424140};\nGN   Name=hisR {ECO:0000303|PubMed:39424140};\nGN   ORFNames=HMPREF0397_2009 {ECO:0000312|EMBL:EFG94488.1};\nOS   Fusobacterium nucleatum subsp. nucleatum (strain ATCC 23726 / VPI 4351).\nOC   Bacteria; Fusobacteriati; Fusobacteriota; Fusobacteriia; Fusobacteriales;\nOC   Fusobacteriaceae; Fusobacterium.\nOX   NCBI_TaxID=525283;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:51.450216+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b43d619ca52111b53572f98986c14dc86b988a025a0364b36dd5b2547453e3cc",
  "url": "https://rest.uniprot.org/unisave/D5RFM4?format=txt&versions=32"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D5RFM4?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Histidine racemase {ECO:0000303|PubMed:39424140};\nDE            EC=5.1.1.24 {ECO:0000269|PubMed:39424140};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:51.450216+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b43d619ca52111b53572f98986c14dc86b988a025a0364b36dd5b2547453e3cc",
  "url": "https://rest.uniprot.org/unisave/D5RFM4?format=txt&versions=32"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D5RFM4?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND DISRUPTION\nRP   PHENOTYPE.\nRC   STRAIN=ATCC 23726 / VPI 4351;\nRX   PubMed=39424140; DOI=10.1016/j.jbc.2024.107896;\nRA   Lamer T., Chen P., Venter M.J., van Belkum M.J., Wijewardane A., Wu C.,\nRA   Lemieux M.J., Vederas J.C.;\nRT   \"Discovery, characterization, and structure of a cofactor-independent\nRT   histidine racemase from the oral pathogen Fusobacterium nucleatum.\";\nRL   J. Biol. Chem. 300:107896-107896(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:51.450216+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 28-37",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b43d619ca52111b53572f98986c14dc86b988a025a0364b36dd5b2547453e3cc",
  "url": "https://rest.uniprot.org/unisave/D5RFM4?format=txt&versions=32"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D5RFM4?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-histidine = D-histidine; Xref=Rhea:RHEA:59188,\nCC         ChEBI:CHEBI:57595, ChEBI:CHEBI:142967; EC=5.1.1.24;\nCC         Evidence={ECO:0000269|PubMed:39424140};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:51.450216+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 42-45",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b43d619ca52111b53572f98986c14dc86b988a025a0364b36dd5b2547453e3cc",
  "url": "https://rest.uniprot.org/unisave/D5RFM4?format=txt&versions=32"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 56. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
