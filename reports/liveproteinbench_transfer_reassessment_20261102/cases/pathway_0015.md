# pathway_0015

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0015.txt)

**Task:** `pathway`  
**Expected answer:** **B** — Cofactor biosynthesis

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAGSEPVSAEGESMAVDAAPRKPRILLAASGSVAAVKFANLCHCFSEWADVRAVSSSGSLHFIDRASMPKDVILYTDEDEWSSWKKLGDSVLHIELRKWADIMVIAPLSANTLGKIAGGLCDNLLTCIVRAWDYSKPFFVAPAMNTLMWNNPFTERHFISIDELGISLIPPVTKRLACGDYGNGAMAEPSTIYSTVRLFYESKAQQGRAVVTLR

[Multiple Choices]
A. L-threonine from L-aspartate: step 1/5. .
B. Cofactor biosynthesis
C. Glycolipid biosynthesis
D. L-cystathionine from O-succinyl-L-homoserine: step 1/1. .
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

> The matching sequence is annotated as phosphopantothenoylcysteine decarboxylase, with a pathway annotation placing it in coenzyme A biosynthesis, which falls under option B. The annotation is transferred by similarity (ECO:0000250), so it supports the key but is not direct experimental evidence for this exact protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 214-residue sequence can plausibly be recognized by its distributed sequence similarity as belonging to the phosphopantothenoylcysteine decarboxylase/Hal3 family. Transferable knowledge of that enzyme family links it to coenzyme A cofactor biosynthesis, distinguishing option B from the amino-acid biosynthesis steps and glycolipid biosynthesis. This is a family-level inference, not recall of this protein's database record.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level sequence inference provides a meaningful basis for choosing the broad cofactor-biosynthesis option among these alternatives, although sequence-only identification may be uncertain.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives describe distinct pathway categories, and the family-level inference supports cofactor biosynthesis.


### Important caveats

- The pathway annotation is similarity-based rather than evidence of direct experimental characterization of this exact protein.
- The source record matches the supplied sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 214-residue sequence can plausibly be recognized by its distributed sequence similarity as belonging to the phosphopantothenoylcysteine decarboxylase/Hal3 family. Transferable knowledge of that enzyme family links it to coenzyme A cofactor biosynthesis, distinguishing option B from the amino-acid biosynthesis steps and glycolipid biosynthesis. This is a family-level inference, not recall of this protein's database record.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference provides a meaningful basis for choosing the broad cofactor-biosynthesis option among these alternatives, although sequence-only identification may be uncertain."
  },
  "case_id": "pathway_0015",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The matching sequence is annotated as phosphopantothenoylcysteine decarboxylase, with a pathway annotation placing it in coenzyme A biosynthesis, which falls under option B. The annotation is transferred by similarity (ECO:0000250), so it supports the key but is not direct experimental evidence for this exact protein."
  },
  "important_caveats": [
    "The pathway annotation is similarity-based rather than evidence of direct experimental characterization of this exact protein.",
    "The source record matches the supplied sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives describe distinct pathway categories, and the family-level inference supports cofactor biosynthesis."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0015",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matching sequence is annotated as phosphopantothenoylcysteine decarboxylase, with a pathway annotation placing it in coenzyme A biosynthesis, which falls under option B. The annotation is transferred by similarity (ECO:0000250), so it supports the key but is not direct experimental evidence for this exact protein.",
    "evidence_ids": ["C4", "C5", "H1", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 214-residue sequence can plausibly be recognized by its distributed sequence similarity as belonging to the phosphopantothenoylcysteine decarboxylase/Hal3 family. Transferable knowledge of that enzyme family links it to coenzyme A cofactor biosynthesis, distinguishing option B from the amino-acid biosynthesis steps and glycolipid biosynthesis. This is a family-level inference, not recall of this protein's database record.",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference provides a meaningful basis for choosing the broad cofactor-biosynthesis option among these alternatives, although sequence-only identification may be uncertain."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives describe distinct pathway categories, and the family-level inference supports cofactor biosynthesis."
  },
  "important_caveats": [
    "The pathway annotation is similarity-based rather than evidence of direct experimental characterization of this exact protein.",
    "The source record matches the supplied sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry C6TA59 (HAL3B_SOYBN) explicitly annotates the pathway as 'Cofactor biosynthesis; coenzyme A biosynthesis; CoA from (R)-pantothenate: step 3/5' (evidence IDs C5, H2). The protein is named Phosphopantothenoylcysteine decarboxylase (PPCDC, EC 4.1.1.36). Choice B ('Cofactor biosynthesis') directly matches this annotation. The evidence code is ECO:0000250 (similarity to Q9SWE5), so the pathway assignment is computationally inferred rather than experimentally demonstrated for this exact protein, but it is a well-supported and standard annotation for the PPCDC family.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 214-amino-acid length is a strong discriminator. PPCDC family members are characteristically small (~200–250 aa). In contrast, aspartate kinase (option A, threonine biosynthesis step 1) is typically 800+ aa with ACT regulatory domains; cystathionine gamma-synthase (option D) is a PLP-dependent enzyme of ~400+ aa with conserved PLP-binding lysine motifs; glycolipid biosynthesis enzymes (option C) are glycosyltransferases or related enzymes typically 300–500+ aa with PSPG or GT-B motifs. The sequence contains a 'CHCF' motif (residues ~47–50) and additional conserved cysteines (e.g., 'LACGDYG' near the C-terminus), which are hallmarks of the PPCDC/radical SAM-like decarboxylase superfamily where a conserved Cys forms a thiyl radical for decarboxylation. The sequence lacks ACT domains, PLP-binding motifs, and glycosyltransferase signatures. A knowledgeable model recognizing the small size, the conserved Cys-rich motifs, and the absence of features diagnostic of the other three enzyme classes could credibly assign this to the PPCDC family and thus to cofactor (CoA) biosynthesis.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable knowledge about the PPCDC family (small size, conserved Cys motifs for radical chemistry, absence of ACT/PLP/glycosyltransferase domains) combined with the known sizes and motifs of the enzymes in the other three pathways provides a concrete, credible inference that distinguishes choice B from A, C, and D without requiring recall of this exact UniProt record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent structurally and functionally distinct enzyme classes with well-separated size ranges and sequence motifs. The 214-aa length and Cys-rich motifs point clearly toward PPCDC/cofactor biosynthesis and away from the much larger or mechanistically different enzymes in options A, C, and D.


### Important caveats

- The UniProt pathway annotation carries evidence code ECO:0000250 (similarity to Q9SWE5), meaning it is computationally inferred by homology rather than directly experimentally validated for this soybean protein.
- The protein was originally named 'Halotolerance protein 3b' (GmHAL3b) based on expression studies; the PPCDC enzymatic activity is assigned by similarity, not by direct assay in this reference.
- The sequence-match to C6TA59 is confirmed (SHA-256 match), and the entry has been in Swiss-Prot since 2025-04-09; the benchmark author's exact source snapshot is unknown but the sequence is identical across versions.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 214-amino-acid length is a strong discriminator. PPCDC family members are characteristically small (~200–250 aa). In contrast, aspartate kinase (option A, threonine biosynthesis step 1) is typically 800+ aa with ACT regulatory domains; cystathionine gamma-synthase (option D) is a PLP-dependent enzyme of ~400+ aa with conserved PLP-binding lysine motifs; glycolipid biosynthesis enzymes (option C) are glycosyltransferases or related enzymes typically 300–500+ aa with PSPG or GT-B motifs. The sequence contains a 'CHCF' motif (residues ~47–50) and additional conserved cysteines (e.g., 'LACGDYG' near the C-terminus), which are hallmarks of the PPCDC/radical SAM-like decarboxylase superfamily where a conserved Cys forms a thiyl radical for decarboxylation. The sequence lacks ACT domains, PLP-binding motifs, and glycosyltransferase signatures. A knowledgeable model recognizing the small size, the conserved Cys-rich motifs, and the absence of features diagnostic of the other three enzyme classes could credibly assign this to the PPCDC family and thus to cofactor (CoA) biosynthesis.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge about the PPCDC family (small size, conserved Cys motifs for radical chemistry, absence of ACT/PLP/glycosyltransferase domains) combined with the known sizes and motifs of the enzymes in the other three pathways provides a concrete, credible inference that distinguishes choice B from A, C, and D without requiring recall of this exact UniProt record."
  },
  "case_id": "pathway_0015",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry C6TA59 (HAL3B_SOYBN) explicitly annotates the pathway as 'Cofactor biosynthesis; coenzyme A biosynthesis; CoA from (R)-pantothenate: step 3/5' (evidence IDs C5, H2). The protein is named Phosphopantothenoylcysteine decarboxylase (PPCDC, EC 4.1.1.36). Choice B ('Cofactor biosynthesis') directly matches this annotation. The evidence code is ECO:0000250 (similarity to Q9SWE5), so the pathway assignment is computationally inferred rather than experimentally demonstrated for this exact protein, but it is a well-supported and standard annotation for the PPCDC family."
  },
  "important_caveats": [
    "The UniProt pathway annotation carries evidence code ECO:0000250 (similarity to Q9SWE5), meaning it is computationally inferred by homology rather than directly experimentally validated for this soybean protein.",
    "The protein was originally named 'Halotolerance protein 3b' (GmHAL3b) based on expression studies; the PPCDC enzymatic activity is assigned by similarity, not by direct assay in this reference.",
    "The sequence-match to C6TA59 is confirmed (SHA-256 match), and the entry has been in Swiss-Prot since 2025-04-09; the benchmark author's exact source snapshot is unknown but the sequence is identical across versions."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent structurally and functionally distinct enzyme classes with well-separated size ranges and sequence motifs. The 214-aa length and Cys-rich motifs point clearly toward PPCDC/cofactor biosynthesis and away from the much larger or mechanistically different enzymes in options A, C, and D."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0015",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry C6TA59 (HAL3B_SOYBN) explicitly annotates the pathway as 'Cofactor biosynthesis; coenzyme A biosynthesis; CoA from (R)-pantothenate: step 3/5' (evidence IDs C5, H2). The protein is named Phosphopantothenoylcysteine decarboxylase (PPCDC, EC 4.1.1.36). Choice B ('Cofactor biosynthesis') directly matches this annotation. The evidence code is ECO:0000250 (similarity to Q9SWE5), so the pathway assignment is computationally inferred rather than experimentally demonstrated for this exact protein, but it is a well-supported and standard annotation for the PPCDC family.",
    "evidence_ids": ["C4", "C5", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 214-amino-acid length is a strong discriminator. PPCDC family members are characteristically small (~200–250 aa). In contrast, aspartate kinase (option A, threonine biosynthesis step 1) is typically 800+ aa with ACT regulatory domains; cystathionine gamma-synthase (option D) is a PLP-dependent enzyme of ~400+ aa with conserved PLP-binding lysine motifs; glycolipid biosynthesis enzymes (option C) are glycosyltransferases or related enzymes typically 300–500+ aa with PSPG or GT-B motifs. The sequence contains a 'CHCF' motif (residues ~47–50) and additional conserved cysteines (e.g., 'LACGDYG' near the C-terminus), which are hallmarks of the PPCDC/radical SAM-like decarboxylase superfamily where a conserved Cys forms a thiyl radical for decarboxylation. The sequence lacks ACT domains, PLP-binding motifs, and glycosyltransferase signatures. A knowledgeable model recognizing the small size, the conserved Cys-rich motifs, and the absence of features diagnostic of the other three enzyme classes could credibly assign this to the PPCDC family and thus to cofactor (CoA) biosynthesis.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge about the PPCDC family (small size, conserved Cys motifs for radical chemistry, absence of ACT/PLP/glycosyltransferase domains) combined with the known sizes and motifs of the enzymes in the other three pathways provides a concrete, credible inference that distinguishes choice B from A, C, and D without requiring recall of this exact UniProt record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent structurally and functionally distinct enzyme classes with well-separated size ranges and sequence motifs. The 214-aa length and Cys-rich motifs point clearly toward PPCDC/cofactor biosynthesis and away from the much larger or mechanistically different enzymes in options A, C, and D."
  },
  "important_caveats": [
    "The UniProt pathway annotation carries evidence code ECO:0000250 (similarity to Q9SWE5), meaning it is computationally inferred by homology rather than directly experimentally validated for this soybean protein.",
    "The protein was originally named 'Halotolerance protein 3b' (GmHAL3b) based on expression studies; the PPCDC enzymatic activity is assigned by similarity, not by direct assay in this reference.",
    "The sequence-match to C6TA59 is confirmed (SHA-256 match), and the entry has been in Swiss-Prot since 2025-04-09; the benchmark author's exact source snapshot is unknown but the sequence is identical across versions."
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
  "benchmark_sequence_length": 214,
  "benchmark_sequence_sha256": "dcaceed6f1d468598241beac0d585a8eb9ed9cdd0b98d0e7be38e1ae1801b687",
  "current_entry_audit": {
    "entryVersion": 86,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2009-09-22",
    "sequenceVersion": 1
  },
  "current_record_sha256": "4f24a50395840d689b2bca6503bac71363002becd9e9b0e170ac85361993f2a0",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 214,
  "current_source_sequence_sha256": "dcaceed6f1d468598241beac0d585a8eb9ed9cdd0b98d0e7be38e1ae1801b687",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 84,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "C6TA59",
  "selected_historical_entry_version": 84,
  "selected_historical_record_sha256": "9ba69ef0f337ff2a30393964c793af5f757c0c52e62614aa37894bfe6ab8f68d",
  "selected_historical_source_sequence_length": 214,
  "selected_historical_source_sequence_sha256": "dcaceed6f1d468598241beac0d585a8eb9ed9cdd0b98d0e7be38e1ae1801b687",
  "selected_historical_version": {
    "accession": "C6TA59",
    "database": "Swiss-Prot",
    "entryVersion": 84,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "HAL3B_SOYBN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6TA59.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"C6TA59\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:27:35.244012+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f24a50395840d689b2bca6503bac71363002becd9e9b0e170ac85361993f2a0",
  "url": "https://rest.uniprot.org/uniprotkb/C6TA59.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6TA59.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":86,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2009-09-22\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:27:35.244012+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f24a50395840d689b2bca6503bac71363002becd9e9b0e170ac85361993f2a0",
  "url": "https://rest.uniprot.org/uniprotkb/C6TA59.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6TA59.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Soybean\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"rosids\",\"fabids\",\"Fabales\",\"Fabaceae\",\"Papilionoideae\",\"50 kb inversion clade\",\"NPAAA clade\",\"indigoferoid/millettioid clade\",\"Phaseoleae\",\"Glycine\",\"Glycine subgen. Soja\"],\"scientificName\":\"Glycine max\",\"synonyms\":[\"Glycine hispida\"],\"taxonId\":3847}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:27:35.244012+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f24a50395840d689b2bca6503bac71363002becd9e9b0e170ac85361993f2a0",
  "url": "https://rest.uniprot.org/uniprotkb/C6TA59.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6TA59.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"Ref.3\",\"source\":\"Reference\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"Ref.4\",\"source\":\"Reference\"}],\"value\":\"Halotolerance protein 3b\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"Ref.3\",\"source\":\"Reference\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"Ref.4\",\"source\":\"Reference\"}],\"value\":\"GmHAL3b\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"value\":\"4.1.1.36\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Phosphopantothenoylcysteine decarboxylase HAL3b\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"PPCDC\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:27:35.244012+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f24a50395840d689b2bca6503bac71363002becd9e9b0e170ac85361993f2a0",
  "url": "https://rest.uniprot.org/uniprotkb/C6TA59.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6TA59.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"value\":\"Cofactor biosynthesis; coenzyme A biosynthesis; CoA from (R)-pantothenate: step 3/5\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:27:35.244012+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f24a50395840d689b2bca6503bac71363002becd9e9b0e170ac85361993f2a0",
  "url": "https://rest.uniprot.org/uniprotkb/C6TA59.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6TA59?format=txt&versions=84)

```json
{
  "entry_version": 84,
  "evidence_id": "H1",
  "excerpt": "ID   HAL3B_SOYBN             Reviewed;         214 AA.\nAC   C6TA59;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   22-SEP-2009, sequence version 1.\nDT   28-JAN-2026, entry version 84.\nDE   RecName: Full=Phosphopantothenoylcysteine decarboxylase HAL3b {ECO:0000305};\nDE            Short=PPCDC {ECO:0000305};\nDE            EC=4.1.1.36 {ECO:0000250|UniProtKB:Q9SWE5};\nDE   AltName: Full=Halotolerance protein 3b {ECO:0000303|Ref.3, ECO:0000303|Ref.4};\nDE            Short=GmHAL3b {ECO:0000303|Ref.3, ECO:0000303|Ref.4};\nGN   Name=HAL3B {ECO:0000303|Ref.3, ECO:0000303|Ref.4};\nGN   OrderedLocusNames=Glyma07g082800 {ECO:0000312|EMBL:KRH48322.1};\nOS   Glycine max (Soybean) (Glycine hispida).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   rosids; fabids; Fabales; Fabaceae; Papilionoideae; 50 kb inversion clade;\nOC   NPAAA clade; indigoferoid/millettioid clade; Phaseoleae; Glycine;\nOC   Glycine subgen. Soja.\nOX   NCBI_TaxID=3847;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:37.263279+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-19",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9ba69ef0f337ff2a30393964c793af5f757c0c52e62614aa37894bfe6ab8f68d",
  "url": "https://rest.uniprot.org/unisave/C6TA59?format=txt&versions=84"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6TA59?format=txt&versions=84)

```json
{
  "entry_version": 84,
  "evidence_id": "H2",
  "excerpt": "CC   -!- PATHWAY: Cofactor biosynthesis; coenzyme A biosynthesis; CoA from (R)-\nCC       pantothenate: step 3/5. {ECO:0000250|UniProtKB:Q9SWE5}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:37.263279+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 73-74",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9ba69ef0f337ff2a30393964c793af5f757c0c52e62614aa37894bfe6ab8f68d",
  "url": "https://rest.uniprot.org/unisave/C6TA59?format=txt&versions=84"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 15. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
