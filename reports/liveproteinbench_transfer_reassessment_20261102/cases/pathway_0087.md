# pathway_0087

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0087.txt)

**Task:** `pathway`  
**Expected answer:** **C** — Amino-acid degradation. .

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MIVVVIADKEFYGWAESVPYARYDESISTSTKQIKALFCDRSFTRKMELSELINTLPAGAARNALDCAMWDLQAKQSTRPVAEILSKTSITSICAHTLSIDTPKAMQEAVLAMNSPPLVKVKLDKQDIIARMTAIANAAPHSQFIVDANEDWCFRDLEENVEALKALNVVLIEQPLPAGEDEQLINFTSPIPLCADESCHTENDLPYLQGRYQVVNIKLDKTGGLTQACSLASKAQKMGFDIMLGCMVGSSLAMAPASLLASQARYVDLDGPLLVLKDRKHHFTYADGQMSPLQSCLWGGAHNSERFFVDRLQLQ

[Multiple Choices]
A. tetrahydrofolate interconversion. .
B. chorismate biosynthesis
C. Amino-acid degradation. .
D. Metabolic intermediate biosynthesis
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Pathway Prediction, which is to predict the primary metabolic or signaling pathway in which a given protein functions. Biological pathways are series of chemical reactions occurring within a cell that are essential for life. Based on the protein's amino acid sequence, you should identify the most relevant pathway from the given options.. The inputs provided by the user for this task include:

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

> The sequence matches the annotated protein. UniProt identifies it as N-acetyl-D-glutamate racemase and assigns it to amino-acid degradation; the catalytic-activity annotation cites published evidence, and the cited study concerns a D-glutamate catabolic pathway. This supports choice C, though the pathway label itself is annotated with ECO:0000305 rather than presented here as a direct experimental measurement.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> The protein's substrate and catalytic activity—specifically, that it racemizes N-acetyl-D-glutamate in a D-glutamate catabolic pathway—are not supplied and are needed to identify amino-acid degradation over the offered alternatives.


**Reason**

> The sequence is a soluble enzyme-sized protein, but those general properties do not meaningfully distinguish amino-acid degradation from other metabolic pathways. No clear, diagnostic sequence feature or recognizable family relationship in the input establishes the relevant substrate or catabolic role. That distinction depends on the protein-specific activity annotation, not merely on transferable pathway knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the annotated racemase activity and catabolic pathway, amino-acid degradation is the fitting option. The other choices refer to different pathway classes; the broad wording of D does not make biosynthesis a defensible alternative here.


### Important caveats

- The source supports the key for the sequence-matched protein, but the evaluated model did not receive the reviewer-only annotations.
- The cited source excerpts indicate published evidence for catalytic activity and pathway annotation; they do not provide the underlying experimental details.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's substrate and catalytic activity—specifically, that it racemizes N-acetyl-D-glutamate in a D-glutamate catabolic pathway—are not supplied and are needed to identify amino-acid degradation over the offered alternatives.",
    "reason": "The sequence is a soluble enzyme-sized protein, but those general properties do not meaningfully distinguish amino-acid degradation from other metabolic pathways. No clear, diagnostic sequence feature or recognizable family relationship in the input establishes the relevant substrate or catabolic role. That distinction depends on the protein-specific activity annotation, not merely on transferable pathway knowledge."
  },
  "case_id": "pathway_0087",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the annotated protein. UniProt identifies it as N-acetyl-D-glutamate racemase and assigns it to amino-acid degradation; the catalytic-activity annotation cites published evidence, and the cited study concerns a D-glutamate catabolic pathway. This supports choice C, though the pathway label itself is annotated with ECO:0000305 rather than presented here as a direct experimental measurement."
  },
  "important_caveats": [
    "The source supports the key for the sequence-matched protein, but the evaluated model did not receive the reviewer-only annotations.",
    "The cited source excerpts indicate published evidence for catalytic activity and pathway annotation; they do not provide the underlying experimental details."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the annotated racemase activity and catabolic pathway, amino-acid degradation is the fitting option. The other choices refer to different pathway classes; the broad wording of D does not make biosynthesis a defensible alternative here."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0087",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the annotated protein. UniProt identifies it as N-acetyl-D-glutamate racemase and assigns it to amino-acid degradation; the catalytic-activity annotation cites published evidence, and the cited study concerns a D-glutamate catabolic pathway. This supports choice C, though the pathway label itself is annotated with ECO:0000305 rather than presented here as a direct experimental measurement.",
    "evidence_ids": ["C4", "C5", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "The protein's substrate and catalytic activity—specifically, that it racemizes N-acetyl-D-glutamate in a D-glutamate catabolic pathway—are not supplied and are needed to identify amino-acid degradation over the offered alternatives.",
    "reason": "The sequence is a soluble enzyme-sized protein, but those general properties do not meaningfully distinguish amino-acid degradation from other metabolic pathways. No clear, diagnostic sequence feature or recognizable family relationship in the input establishes the relevant substrate or catabolic role. That distinction depends on the protein-specific activity annotation, not merely on transferable pathway knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the annotated racemase activity and catabolic pathway, amino-acid degradation is the fitting option. The other choices refer to different pathway classes; the broad wording of D does not make biosynthesis a defensible alternative here."
  },
  "important_caveats": [
    "The source supports the key for the sequence-matched protein, but the evaluated model did not receive the reviewer-only annotations.",
    "The cited source excerpts indicate published evidence for catalytic activity and pathway annotation; they do not provide the underlying experimental details."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (P0DXZ2) explicitly annotates the pathway as 'Amino-acid degradation' (evidence C5, H3, ECO:0000305|PubMed:36690779). The protein is N-acetyl-D-glutamate racemase (EC 5.1.1.25), which catalyzes the racemization of N-acetyl-D-glutamate as a key step in a novel D-glutamate catabolic pathway described in the 2023 ISME J. paper. This is unambiguously amino-acid degradation.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C4](#evidence-c4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> The specific substrate identity (N-acetyl-D-glutamate) and the catabolic (degradation) context of the pathway containing this racemase. Without knowing that this enzyme participates in D-glutamate catabolism, one cannot distinguish 'amino-acid degradation' (C) from 'metabolic intermediate biosynthesis' (D). The sequence provides no recognizable motifs for amino-acid catabolism, and the enzyme belongs to a novel family (EC 5.1.1.25, described in 2023) with no well-established family-level pathway association that would transfer from other proteins.


**Reason**

> The 315-residue sequence lacks obvious motifs for folate metabolism (eliminating A by general knowledge), shikimate/chorismate pathway enzymes (eliminating B), or any well-characterized amino-acid catabolic enzyme family. The protein is a novel racemase (EC 5.1.1.25) from a 2023 publication describing a previously unknown D-glutamate catabolic pathway in marine Proteobacteria. Racemases in general are associated with both biosynthetic and catabolic pathways (e.g., alanine racemase in peptidoglycan synthesis vs. amino-acid catabolism), so knowing it is a racemase does not resolve C vs. D. The specific assignment to 'amino-acid degradation' depends on knowing this enzyme's role in the D-glutamate catabolic pathway, a fact specific to this protein's annotation rather than derivable from sequence features or general enzyme-family knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> From the sequence alone, without pathway-specific knowledge, a racemase acting on an acylated amino-acid derivative could plausibly be categorized under either 'amino-acid degradation' (C) or 'metabolic intermediate biosynthesis' (D), since N-acetyl-glutamate is both an amino-acid derivative and a metabolic intermediate. The correct assignment to degradation requires knowing the catabolic direction of the pathway, which is not encoded in the sequence.


### Important caveats

- The protein is a novel enzyme (EC 5.1.1.25) described in a 2023 ISME J. paper, making it unlikely to be well-represented in training corpora for general pattern recognition.
- The UniProt annotation is based on experimental evidence (ECO:0000269, PubMed:36690779) including catalytic activity and disruption phenotype, confirming the catabolic role.
- Options A and B are clearly eliminable by general knowledge (no folate-binding or chorismate-synthase motifs present), but the C/D distinction requires pathway-specific knowledge not derivable from the sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate identity (N-acetyl-D-glutamate) and the catabolic (degradation) context of the pathway containing this racemase. Without knowing that this enzyme participates in D-glutamate catabolism, one cannot distinguish 'amino-acid degradation' (C) from 'metabolic intermediate biosynthesis' (D). The sequence provides no recognizable motifs for amino-acid catabolism, and the enzyme belongs to a novel family (EC 5.1.1.25, described in 2023) with no well-established family-level pathway association that would transfer from other proteins.",
    "reason": "The 315-residue sequence lacks obvious motifs for folate metabolism (eliminating A by general knowledge), shikimate/chorismate pathway enzymes (eliminating B), or any well-characterized amino-acid catabolic enzyme family. The protein is a novel racemase (EC 5.1.1.25) from a 2023 publication describing a previously unknown D-glutamate catabolic pathway in marine Proteobacteria. Racemases in general are associated with both biosynthetic and catabolic pathways (e.g., alanine racemase in peptidoglycan synthesis vs. amino-acid catabolism), so knowing it is a racemase does not resolve C vs. D. The specific assignment to 'amino-acid degradation' depends on knowing this enzyme's role in the D-glutamate catabolic pathway, a fact specific to this protein's annotation rather than derivable from sequence features or general enzyme-family knowledge."
  },
  "case_id": "pathway_0087",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (P0DXZ2) explicitly annotates the pathway as 'Amino-acid degradation' (evidence C5, H3, ECO:0000305|PubMed:36690779). The protein is N-acetyl-D-glutamate racemase (EC 5.1.1.25), which catalyzes the racemization of N-acetyl-D-glutamate as a key step in a novel D-glutamate catabolic pathway described in the 2023 ISME J. paper. This is unambiguously amino-acid degradation."
  },
  "important_caveats": [
    "The protein is a novel enzyme (EC 5.1.1.25) described in a 2023 ISME J. paper, making it unlikely to be well-represented in training corpora for general pattern recognition.",
    "The UniProt annotation is based on experimental evidence (ECO:0000269, PubMed:36690779) including catalytic activity and disruption phenotype, confirming the catabolic role.",
    "Options A and B are clearly eliminable by general knowledge (no folate-binding or chorismate-synthase motifs present), but the C/D distinction requires pathway-specific knowledge not derivable from the sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "From the sequence alone, without pathway-specific knowledge, a racemase acting on an acylated amino-acid derivative could plausibly be categorized under either 'amino-acid degradation' (C) or 'metabolic intermediate biosynthesis' (D), since N-acetyl-glutamate is both an amino-acid derivative and a metabolic intermediate. The correct assignment to degradation requires knowing the catabolic direction of the pathway, which is not encoded in the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0087",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (P0DXZ2) explicitly annotates the pathway as 'Amino-acid degradation' (evidence C5, H3, ECO:0000305|PubMed:36690779). The protein is N-acetyl-D-glutamate racemase (EC 5.1.1.25), which catalyzes the racemization of N-acetyl-D-glutamate as a key step in a novel D-glutamate catabolic pathway described in the 2023 ISME J. paper. This is unambiguously amino-acid degradation.",
    "evidence_ids": ["C5", "H3", "C4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "The specific substrate identity (N-acetyl-D-glutamate) and the catabolic (degradation) context of the pathway containing this racemase. Without knowing that this enzyme participates in D-glutamate catabolism, one cannot distinguish 'amino-acid degradation' (C) from 'metabolic intermediate biosynthesis' (D). The sequence provides no recognizable motifs for amino-acid catabolism, and the enzyme belongs to a novel family (EC 5.1.1.25, described in 2023) with no well-established family-level pathway association that would transfer from other proteins.",
    "reason": "The 315-residue sequence lacks obvious motifs for folate metabolism (eliminating A by general knowledge), shikimate/chorismate pathway enzymes (eliminating B), or any well-characterized amino-acid catabolic enzyme family. The protein is a novel racemase (EC 5.1.1.25) from a 2023 publication describing a previously unknown D-glutamate catabolic pathway in marine Proteobacteria. Racemases in general are associated with both biosynthetic and catabolic pathways (e.g., alanine racemase in peptidoglycan synthesis vs. amino-acid catabolism), so knowing it is a racemase does not resolve C vs. D. The specific assignment to 'amino-acid degradation' depends on knowing this enzyme's role in the D-glutamate catabolic pathway, a fact specific to this protein's annotation rather than derivable from sequence features or general enzyme-family knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "From the sequence alone, without pathway-specific knowledge, a racemase acting on an acylated amino-acid derivative could plausibly be categorized under either 'amino-acid degradation' (C) or 'metabolic intermediate biosynthesis' (D), since N-acetyl-glutamate is both an amino-acid derivative and a metabolic intermediate. The correct assignment to degradation requires knowing the catabolic direction of the pathway, which is not encoded in the sequence."
  },
  "important_caveats": [
    "The protein is a novel enzyme (EC 5.1.1.25) described in a 2023 ISME J. paper, making it unlikely to be well-represented in training corpora for general pattern recognition.",
    "The UniProt annotation is based on experimental evidence (ECO:0000269, PubMed:36690779) including catalytic activity and disruption phenotype, confirming the catabolic role.",
    "Options A and B are clearly eliminable by general knowledge (no folate-binding or chorismate-synthase motifs present), but the C/D distinction requires pathway-specific knowledge not derivable from the sequence."
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
  "benchmark_sequence_length": 315,
  "benchmark_sequence_sha256": "0d1eb3735d239531b3217901b0448f4b6bbb8ed844687491961a764ee0e557df",
  "current_entry_audit": {
    "entryVersion": 5,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-04-09",
    "sequenceVersion": 1
  },
  "current_record_sha256": "ce4ce37f5eba503f3ded1200adaf39a2c1cec4022ddf9b32af66f9212c2586ea",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 315,
  "current_source_sequence_sha256": "0d1eb3735d239531b3217901b0448f4b6bbb8ed844687491961a764ee0e557df",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 3,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "P0DXZ2",
  "selected_historical_entry_version": 3,
  "selected_historical_record_sha256": "e4cce17ff5162859998568df20b58b36b0722c6040f9c24adb62cf5a2aed600d",
  "selected_historical_source_sequence_length": 315,
  "selected_historical_source_sequence_sha256": "0d1eb3735d239531b3217901b0448f4b6bbb8ed844687491961a764ee0e557df",
  "selected_historical_version": {
    "accession": "P0DXZ2",
    "database": "Swiss-Prot",
    "entryVersion": 3,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DGCA_PSEAS",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ2.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DXZ2\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:09.095372+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ce4ce37f5eba503f3ded1200adaf39a2c1cec4022ddf9b32af66f9212c2586ea",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXZ2.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ2.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":5,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-04-09\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:09.095372+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ce4ce37f5eba503f3ded1200adaf39a2c1cec4022ddf9b32af66f9212c2586ea",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXZ2.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ2.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Alteromonadales\",\"Pseudoalteromonadaceae\",\"Pseudoalteromonas\"],\"scientificName\":\"Pseudoalteromonas sp\",\"taxonId\":53249}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:09.095372+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ce4ce37f5eba503f3ded1200adaf39a2c1cec4022ddf9b32af66f9212c2586ea",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXZ2.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ2.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36690779\",\"source\":\"PubMed\"}],\"value\":\"5.1.1.25\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36690779\",\"source\":\"PubMed\"}],\"value\":\"N-acetyl-D-glutamate racemase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36690779\",\"source\":\"PubMed\"}],\"value\":\"N-acetyl-D-Glu racemase\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:09.095372+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ce4ce37f5eba503f3ded1200adaf39a2c1cec4022ddf9b32af66f9212c2586ea",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXZ2.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ2.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"36690779\",\"source\":\"PubMed\"}],\"value\":\"Amino-acid degradation\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-01T06:25:09.095372+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ce4ce37f5eba503f3ded1200adaf39a2c1cec4022ddf9b32af66f9212c2586ea",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXZ2.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ2.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Yu Y.\",\"Wang P.\",\"Cao H.Y.\",\"Teng Z.J.\",\"Zhu Y.\",\"Wang M.\",\"McMinn A.\",\"Chen Y.\",\"Xiang H.\",\"Zhang Y.Z.\",\"Chen X.L.\",\"Zhang Y.Q.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"36690779\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41396-023-01364-6\"}],\"citationType\":\"journal article\",\"firstPage\":\"537\",\"id\":\"36690779\",\"journal\":\"ISME J.\",\"lastPage\":\"548\",\"publicationDate\":\"2023\",\"title\":\"Novel D-glutamate catabolic pathway in marine Proteobacteria and halophilic archaea.\",\"volume\":\"17\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"CF6-2\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"INDUCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:25:09.095372+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ce4ce37f5eba503f3ded1200adaf39a2c1cec4022ddf9b32af66f9212c2586ea",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXZ2.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ2?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H1",
  "excerpt": "ID   DGCA_PSEAS              Reviewed;         315 AA.\nAC   P0DXZ2;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   09-APR-2025, sequence version 1.\nDT   28-JAN-2026, entry version 3.\nDE   RecName: Full=N-acetyl-D-glutamate racemase {ECO:0000303|PubMed:36690779};\nDE            Short=N-acetyl-D-Glu racemase {ECO:0000303|PubMed:36690779};\nDE            EC=5.1.1.25 {ECO:0000269|PubMed:36690779};\nGN   Name=dgcA {ECO:0000303|PubMed:36690779};\nOS   Pseudoalteromonas sp.\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Alteromonadales; Pseudoalteromonadaceae; Pseudoalteromonas.\nOX   NCBI_TaxID=53249;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:41:59.066573+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e4cce17ff5162859998568df20b58b36b0722c6040f9c24adb62cf5a2aed600d",
  "url": "https://rest.uniprot.org/unisave/P0DXZ2?format=txt&versions=3"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ2?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H2",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, CATALYTIC ACTIVITY, INDUCTION,\nRP   AND DISRUPTION PHENOTYPE.\nRC   STRAIN=CF6-2;\nRX   PubMed=36690779; DOI=10.1038/s41396-023-01364-6;\nRA   Yu Y., Wang P., Cao H.Y., Teng Z.J., Zhu Y., Wang M., McMinn A., Chen Y.,\nRA   Xiang H., Zhang Y.Z., Chen X.L., Zhang Y.Q.;\nRT   \"Novel D-glutamate catabolic pathway in marine Proteobacteria and\nRT   halophilic archaea.\";\nRL   ISME J. 17:537-548(2023).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:41:59.066573+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 14-23",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e4cce17ff5162859998568df20b58b36b0722c6040f9c24adb62cf5a2aed600d",
  "url": "https://rest.uniprot.org/unisave/P0DXZ2?format=txt&versions=3"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ2?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Amino-acid degradation. {ECO:0000305|PubMed:36690779}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:41:59.066573+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 41-41",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e4cce17ff5162859998568df20b58b36b0722c6040f9c24adb62cf5a2aed600d",
  "url": "https://rest.uniprot.org/unisave/P0DXZ2?format=txt&versions=3"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 87. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
