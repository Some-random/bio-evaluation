# active_site_0074

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0074.txt)

**Task:** `active_site`  
**Expected answer:** **C** — Position 93 (Proton donor)

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
A. Position 365 (For beta-ketoacyl synthase 1 activity)
B. Position 127 (Nucleophile)
C. Position 93 (Proton donor)
D. Position 27 (Proton acceptor)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Active Site Prediction, which is to identify the key amino acid residues that form the active site of an enzyme. The active site is the specific region on the enzyme where a substrate binds and the chemical reaction is catalyzed. Based on the full protein sequence provided, you must select the option that correctly lists the amino acid residues (by their type and position) that constitute the enzyme's catalytic center.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt record annotates position 93 as a proton donor. This annotation is transferred by similarity (ECO:0000250), not presented as direct experimental evidence for this protein.

Citations as saved: [C5](#evidence-c5), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 214-residue sequence is consistent with a compact FMN-dependent phosphopantothenoylcysteine decarboxylase family protein. Transferable family knowledge supports a catalytic proton-donor role for a conserved histidine; position 93 is His. This favors C over the proposed beta-ketoacyl synthase activity at a position beyond the sequence, a proton-acceptor claim at a leucine position, or a nucleophile claim for the cysteine at 127.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level recognition and conserved catalytic-residue patterns provide a credible, probabilistic way to distinguish C among these choices. The sequence alone does not prove the annotation, and the inference is not independent experimental validation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only C is supported among the offered choices. The source also annotates another proton donor at position 178, but that position is not an offered option.


### Important caveats

- The supporting annotation is similarity-based; it should not be characterized as experimentally established for this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 214-residue sequence is consistent with a compact FMN-dependent phosphopantothenoylcysteine decarboxylase family protein. Transferable family knowledge supports a catalytic proton-donor role for a conserved histidine; position 93 is His. This favors C over the proposed beta-ketoacyl synthase activity at a position beyond the sequence, a proton-acceptor claim at a leucine position, or a nucleophile claim for the cysteine at 127.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition and conserved catalytic-residue patterns provide a credible, probabilistic way to distinguish C among these choices. The sequence alone does not prove the annotation, and the inference is not independent experimental validation."
  },
  "case_id": "active_site_0074",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates position 93 as a proton donor. This annotation is transferred by similarity (ECO:0000250), not presented as direct experimental evidence for this protein."
  },
  "important_caveats": [
    "The supporting annotation is similarity-based; it should not be characterized as experimentally established for this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only C is supported among the offered choices. The source also annotates another proton donor at position 178, but that position is not an offered option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0074",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates position 93 as a proton donor. This annotation is transferred by similarity (ECO:0000250), not presented as direct experimental evidence for this protein.",
    "evidence_ids": ["C5", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 214-residue sequence is consistent with a compact FMN-dependent phosphopantothenoylcysteine decarboxylase family protein. Transferable family knowledge supports a catalytic proton-donor role for a conserved histidine; position 93 is His. This favors C over the proposed beta-ketoacyl synthase activity at a position beyond the sequence, a proton-acceptor claim at a leucine position, or a nucleophile claim for the cysteine at 127.",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition and conserved catalytic-residue patterns provide a credible, probabilistic way to distinguish C among these choices. The sequence alone does not prove the annotation, and the inference is not independent experimental validation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only C is supported among the offered choices. The source also annotates another proton donor at position 178, but that position is not an offered option."
  },
  "important_caveats": [
    "The supporting annotation is similarity-based; it should not be characterized as experimentally established for this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry C6TA59 (HAL3B_SOYBN, Phosphopantothenoylcysteine decarboxylase, EC 4.1.1.36) annotates position 93 as 'Active site – Proton donor' (evidence ECO:0000250, similarity transfer from Q9SWE5, the characterized yeast PPCDC). The sequence at position 93 is Histidine, consistent with the proton-donor role in FMN-dependent decarboxylases. The annotation is computational inference by similarity rather than direct experimental evidence for this specific protein, but it is internally consistent with the PPCDC family mechanism. Option C matches the annotation exactly.

Citations as saved: [C5](#evidence-c5), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Several layers of transferable knowledge allow a knowledgeable model to narrow the choices. (1) Option A (position 365) is trivially eliminated because the protein is only 214 residues long, and 'beta-ketoacyl synthase 1 activity' is functionally irrelevant. (2) Option D (position 27, proton acceptor) is eliminated because residue 27 is Leucine, which has no ionizable side chain and cannot act as a proton acceptor. (3) The sequence contains the conserved 'CHCF' motif (positions 42–45) and the overall length/composition are hallmarks of the FMN-dependent phosphopantothenoylcysteine decarboxylase (PPCDC) family. Members of this family (e.g., yeast PPCDC/HAL3) catalyze decarboxylation via FMN-mediated electron/proton transfer, not via nucleophilic attack by a cysteine. Histidine is the canonical proton-donor/acceptor in such mechanisms. (4) Position 93 is Histidine (H), fitting the proton-donor role perfectly. Position 127 is Cysteine (C), which could serve as a nucleophile in cysteine proteases or phosphatases, but the FMN-dependent decarboxylase mechanism does not rely on nucleophilic catalysis. Thus, family-level mechanism knowledge (FMN-dependent decarboxylase → proton transfer → Histidine proton donor) meaningfully distinguishes C from B, while A and D are eliminated by sequence-length and chemical-logic arguments.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The model can eliminate A (out of range) and D (Leucine cannot be a proton acceptor) from the sequence alone. The B-vs-C distinction rests on recognizing the protein as an FMN-dependent decarboxylase (via the CHCF motif and family-level features) and applying the well-known mechanism of this family: proton transfer catalysis with Histidine as the proton donor, not nucleophilic catalysis by Cysteine. This is legitimate transferable knowledge about the PPCDC/FMN-dependent enzyme family, not a lookup of this exact protein's database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option A is eliminated by sequence length (214 aa < 365). Option D is eliminated by chemistry (Leucine has no ionizable side chain). Between B and C, the FMN-dependent decarboxylase mechanism favors proton transfer (His) over nucleophilic catalysis (Cys), making C the uniquely defensible choice. The UniProt entry also annotates position 178 as a second proton donor, but that residue is not offered as an option, so no ambiguity is introduced among the presented choices.


### Important caveats

- The active-site annotation at position 93 carries evidence code ECO:0000250 (inferred by similarity to Q9SWE5), meaning it is a computational transfer rather than direct experimental evidence for this specific soybean protein.
- The UniProt entry annotates two proton-donor active sites (93 and 178); only position 93 is offered among the choices, so the question is not ambiguous in practice but is incomplete relative to the full annotation.
- The question stem asks for residues 'by their type and position' but the options provide only position and functional role, not the amino-acid identity; the model must read the sequence to determine the residue type at each position.
- The reviewer-only accession (C6TA59) and organism identity were not available to the evaluated model; the reasoning above relies only on sequence features and family-level knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Several layers of transferable knowledge allow a knowledgeable model to narrow the choices. (1) Option A (position 365) is trivially eliminated because the protein is only 214 residues long, and 'beta-ketoacyl synthase 1 activity' is functionally irrelevant. (2) Option D (position 27, proton acceptor) is eliminated because residue 27 is Leucine, which has no ionizable side chain and cannot act as a proton acceptor. (3) The sequence contains the conserved 'CHCF' motif (positions 42–45) and the overall length/composition are hallmarks of the FMN-dependent phosphopantothenoylcysteine decarboxylase (PPCDC) family. Members of this family (e.g., yeast PPCDC/HAL3) catalyze decarboxylation via FMN-mediated electron/proton transfer, not via nucleophilic attack by a cysteine. Histidine is the canonical proton-donor/acceptor in such mechanisms. (4) Position 93 is Histidine (H), fitting the proton-donor role perfectly. Position 127 is Cysteine (C), which could serve as a nucleophile in cysteine proteases or phosphatases, but the FMN-dependent decarboxylase mechanism does not rely on nucleophilic catalysis. Thus, family-level mechanism knowledge (FMN-dependent decarboxylase → proton transfer → Histidine proton donor) meaningfully distinguishes C from B, while A and D are eliminated by sequence-length and chemical-logic arguments.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The model can eliminate A (out of range) and D (Leucine cannot be a proton acceptor) from the sequence alone. The B-vs-C distinction rests on recognizing the protein as an FMN-dependent decarboxylase (via the CHCF motif and family-level features) and applying the well-known mechanism of this family: proton transfer catalysis with Histidine as the proton donor, not nucleophilic catalysis by Cysteine. This is legitimate transferable knowledge about the PPCDC/FMN-dependent enzyme family, not a lookup of this exact protein's database record."
  },
  "case_id": "active_site_0074",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry C6TA59 (HAL3B_SOYBN, Phosphopantothenoylcysteine decarboxylase, EC 4.1.1.36) annotates position 93 as 'Active site – Proton donor' (evidence ECO:0000250, similarity transfer from Q9SWE5, the characterized yeast PPCDC). The sequence at position 93 is Histidine, consistent with the proton-donor role in FMN-dependent decarboxylases. The annotation is computational inference by similarity rather than direct experimental evidence for this specific protein, but it is internally consistent with the PPCDC family mechanism. Option C matches the annotation exactly."
  },
  "important_caveats": [
    "The active-site annotation at position 93 carries evidence code ECO:0000250 (inferred by similarity to Q9SWE5), meaning it is a computational transfer rather than direct experimental evidence for this specific soybean protein.",
    "The UniProt entry annotates two proton-donor active sites (93 and 178); only position 93 is offered among the choices, so the question is not ambiguous in practice but is incomplete relative to the full annotation.",
    "The question stem asks for residues 'by their type and position' but the options provide only position and functional role, not the amino-acid identity; the model must read the sequence to determine the residue type at each position.",
    "The reviewer-only accession (C6TA59) and organism identity were not available to the evaluated model; the reasoning above relies only on sequence features and family-level knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option A is eliminated by sequence length (214 aa < 365). Option D is eliminated by chemistry (Leucine has no ionizable side chain). Between B and C, the FMN-dependent decarboxylase mechanism favors proton transfer (His) over nucleophilic catalysis (Cys), making C the uniquely defensible choice. The UniProt entry also annotates position 178 as a second proton donor, but that residue is not offered as an option, so no ambiguity is introduced among the presented choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0074",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry C6TA59 (HAL3B_SOYBN, Phosphopantothenoylcysteine decarboxylase, EC 4.1.1.36) annotates position 93 as 'Active site – Proton donor' (evidence ECO:0000250, similarity transfer from Q9SWE5, the characterized yeast PPCDC). The sequence at position 93 is Histidine, consistent with the proton-donor role in FMN-dependent decarboxylases. The annotation is computational inference by similarity rather than direct experimental evidence for this specific protein, but it is internally consistent with the PPCDC family mechanism. Option C matches the annotation exactly.",
    "evidence_ids": ["C5", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Several layers of transferable knowledge allow a knowledgeable model to narrow the choices. (1) Option A (position 365) is trivially eliminated because the protein is only 214 residues long, and 'beta-ketoacyl synthase 1 activity' is functionally irrelevant. (2) Option D (position 27, proton acceptor) is eliminated because residue 27 is Leucine, which has no ionizable side chain and cannot act as a proton acceptor. (3) The sequence contains the conserved 'CHCF' motif (positions 42–45) and the overall length/composition are hallmarks of the FMN-dependent phosphopantothenoylcysteine decarboxylase (PPCDC) family. Members of this family (e.g., yeast PPCDC/HAL3) catalyze decarboxylation via FMN-mediated electron/proton transfer, not via nucleophilic attack by a cysteine. Histidine is the canonical proton-donor/acceptor in such mechanisms. (4) Position 93 is Histidine (H), fitting the proton-donor role perfectly. Position 127 is Cysteine (C), which could serve as a nucleophile in cysteine proteases or phosphatases, but the FMN-dependent decarboxylase mechanism does not rely on nucleophilic catalysis. Thus, family-level mechanism knowledge (FMN-dependent decarboxylase → proton transfer → Histidine proton donor) meaningfully distinguishes C from B, while A and D are eliminated by sequence-length and chemical-logic arguments.",
    "missing_item_specific_fact": "",
    "reason": "The model can eliminate A (out of range) and D (Leucine cannot be a proton acceptor) from the sequence alone. The B-vs-C distinction rests on recognizing the protein as an FMN-dependent decarboxylase (via the CHCF motif and family-level features) and applying the well-known mechanism of this family: proton transfer catalysis with Histidine as the proton donor, not nucleophilic catalysis by Cysteine. This is legitimate transferable knowledge about the PPCDC/FMN-dependent enzyme family, not a lookup of this exact protein's database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option A is eliminated by sequence length (214 aa < 365). Option D is eliminated by chemistry (Leucine has no ionizable side chain). Between B and C, the FMN-dependent decarboxylase mechanism favors proton transfer (His) over nucleophilic catalysis (Cys), making C the uniquely defensible choice. The UniProt entry also annotates position 178 as a second proton donor, but that residue is not offered as an option, so no ambiguity is introduced among the presented choices."
  },
  "important_caveats": [
    "The active-site annotation at position 93 carries evidence code ECO:0000250 (inferred by similarity to Q9SWE5), meaning it is a computational transfer rather than direct experimental evidence for this specific soybean protein.",
    "The UniProt entry annotates two proton-donor active sites (93 and 178); only position 93 is offered among the choices, so the question is not ambiguous in practice but is incomplete relative to the full annotation.",
    "The question stem asks for residues 'by their type and position' but the options provide only position and functional role, not the amino-acid identity; the model must read the sequence to determine the residue type at each position.",
    "The reviewer-only accession (C6TA59) and organism identity were not available to the evaluated model; the reasoning above relies only on sequence features and family-level knowledge."
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
  "excerpt": "{\"description\":\"Proton donor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":93},\"start\":{\"modifier\":\"EXACT\",\"value\":93}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:27:35.244012+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f24a50395840d689b2bca6503bac71363002becd9e9b0e170ac85361993f2a0",
  "url": "https://rest.uniprot.org/uniprotkb/C6TA59.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6TA59.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Proton donor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":178},\"start\":{\"modifier\":\"EXACT\",\"value\":178}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:27:35.244012+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f24a50395840d689b2bca6503bac71363002becd9e9b0e170ac85361993f2a0",
  "url": "https://rest.uniprot.org/uniprotkb/C6TA59.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6TA59.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58210\",\"name\":\"FMN\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":33},\"start\":{\"modifier\":\"EXACT\",\"value\":31}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:27:35.244012+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f24a50395840d689b2bca6503bac71363002becd9e9b0e170ac85361993f2a0",
  "url": "https://rest.uniprot.org/uniprotkb/C6TA59.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6TA59.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58210\",\"name\":\"FMN\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":58},\"start\":{\"modifier\":\"EXACT\",\"value\":56}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:27:35.244012+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f24a50395840d689b2bca6503bac71363002becd9e9b0e170ac85361993f2a0",
  "url": "https://rest.uniprot.org/uniprotkb/C6TA59.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6TA59.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58210\",\"name\":\"FMN\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":112},\"start\":{\"modifier\":\"EXACT\",\"value\":109}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:27:35.244012+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f24a50395840d689b2bca6503bac71363002becd9e9b0e170ac85361993f2a0",
  "url": "https://rest.uniprot.org/uniprotkb/C6TA59.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6TA59.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58210\",\"name\":\"FMN\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":143},\"start\":{\"modifier\":\"EXACT\",\"value\":143}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:27:35.244012+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f24a50395840d689b2bca6503bac71363002becd9e9b0e170ac85361993f2a0",
  "url": "https://rest.uniprot.org/uniprotkb/C6TA59.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6TA59.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:59458\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:59458\",\"name\":\"N-[(R)-4-phosphopantothenoyl]-L-cysteine\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":145},\"start\":{\"modifier\":\"EXACT\",\"value\":145}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:27:35.244012+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f24a50395840d689b2bca6503bac71363002becd9e9b0e170ac85361993f2a0",
  "url": "https://rest.uniprot.org/uniprotkb/C6TA59.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6TA59.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:59458\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:59458\",\"name\":\"N-[(R)-4-phosphopantothenoyl]-L-cysteine\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":175},\"start\":{\"modifier\":\"EXACT\",\"value\":175}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:27:35.244012+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f24a50395840d689b2bca6503bac71363002becd9e9b0e170ac85361993f2a0",
  "url": "https://rest.uniprot.org/uniprotkb/C6TA59.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6TA59.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:59458\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:59458\",\"name\":\"N-[(R)-4-phosphopantothenoyl]-L-cysteine\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":177},\"start\":{\"modifier\":\"EXACT\",\"value\":177}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-02T04:27:35.244012+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f24a50395840d689b2bca6503bac71363002becd9e9b0e170ac85361993f2a0",
  "url": "https://rest.uniprot.org/uniprotkb/C6TA59.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6TA59.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:59458\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:59458\",\"name\":\"N-[(R)-4-phosphopantothenoyl]-L-cysteine\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":186},\"start\":{\"modifier\":\"EXACT\",\"value\":186}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-02T04:27:35.244012+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f24a50395840d689b2bca6503bac71363002becd9e9b0e170ac85361993f2a0",
  "url": "https://rest.uniprot.org/uniprotkb/C6TA59.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6TA59.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"description\":\"Important for catalytic activity\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":178},\"start\":{\"modifier\":\"EXACT\",\"value\":178}},\"type\":\"Site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/11",
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
  "excerpt": "FT   ACT_SITE        93\nFT                   /note=\"Proton donor\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SWE5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:37.263279+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 146-148",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9ba69ef0f337ff2a30393964c793af5f757c0c52e62614aa37894bfe6ab8f68d",
  "url": "https://rest.uniprot.org/unisave/C6TA59?format=txt&versions=84"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6TA59?format=txt&versions=84)

```json
{
  "entry_version": 84,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        178\nFT                   /note=\"Proton donor\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SWE5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:37.263279+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 149-151",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9ba69ef0f337ff2a30393964c793af5f757c0c52e62614aa37894bfe6ab8f68d",
  "url": "https://rest.uniprot.org/unisave/C6TA59?format=txt&versions=84"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6TA59?format=txt&versions=84)

```json
{
  "entry_version": 84,
  "evidence_id": "H4",
  "excerpt": "FT   BINDING         31..33\nFT                   /ligand=\"FMN\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58210\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SWE5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:37.263279+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 152-155",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9ba69ef0f337ff2a30393964c793af5f757c0c52e62614aa37894bfe6ab8f68d",
  "url": "https://rest.uniprot.org/unisave/C6TA59?format=txt&versions=84"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6TA59?format=txt&versions=84)

```json
{
  "entry_version": 84,
  "evidence_id": "H5",
  "excerpt": "FT   BINDING         56..58\nFT                   /ligand=\"FMN\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58210\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SWE5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:37.263279+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 156-159",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9ba69ef0f337ff2a30393964c793af5f757c0c52e62614aa37894bfe6ab8f68d",
  "url": "https://rest.uniprot.org/unisave/C6TA59?format=txt&versions=84"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6TA59?format=txt&versions=84)

```json
{
  "entry_version": 84,
  "evidence_id": "H6",
  "excerpt": "FT   BINDING         109..112\nFT                   /ligand=\"FMN\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58210\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SWE5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:37.263279+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 160-163",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9ba69ef0f337ff2a30393964c793af5f757c0c52e62614aa37894bfe6ab8f68d",
  "url": "https://rest.uniprot.org/unisave/C6TA59?format=txt&versions=84"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6TA59?format=txt&versions=84)

```json
{
  "entry_version": 84,
  "evidence_id": "H7",
  "excerpt": "FT   BINDING         143\nFT                   /ligand=\"FMN\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58210\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SWE5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:37.263279+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 164-167",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9ba69ef0f337ff2a30393964c793af5f757c0c52e62614aa37894bfe6ab8f68d",
  "url": "https://rest.uniprot.org/unisave/C6TA59?format=txt&versions=84"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6TA59?format=txt&versions=84)

```json
{
  "entry_version": 84,
  "evidence_id": "H8",
  "excerpt": "FT   BINDING         145\nFT                   /ligand=\"N-[(R)-4-phosphopantothenoyl]-L-cysteine\"\nFT                   /ligand_id=\"ChEBI:CHEBI:59458\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SWE5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:37.263279+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 168-171",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9ba69ef0f337ff2a30393964c793af5f757c0c52e62614aa37894bfe6ab8f68d",
  "url": "https://rest.uniprot.org/unisave/C6TA59?format=txt&versions=84"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6TA59?format=txt&versions=84)

```json
{
  "entry_version": 84,
  "evidence_id": "H9",
  "excerpt": "FT   BINDING         175\nFT                   /ligand=\"N-[(R)-4-phosphopantothenoyl]-L-cysteine\"\nFT                   /ligand_id=\"ChEBI:CHEBI:59458\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SWE5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:37.263279+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 172-175",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9ba69ef0f337ff2a30393964c793af5f757c0c52e62614aa37894bfe6ab8f68d",
  "url": "https://rest.uniprot.org/unisave/C6TA59?format=txt&versions=84"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6TA59?format=txt&versions=84)

```json
{
  "entry_version": 84,
  "evidence_id": "H10",
  "excerpt": "FT   BINDING         177\nFT                   /ligand=\"N-[(R)-4-phosphopantothenoyl]-L-cysteine\"\nFT                   /ligand_id=\"ChEBI:CHEBI:59458\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SWE5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:37.263279+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 176-179",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9ba69ef0f337ff2a30393964c793af5f757c0c52e62614aa37894bfe6ab8f68d",
  "url": "https://rest.uniprot.org/unisave/C6TA59?format=txt&versions=84"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6TA59?format=txt&versions=84)

```json
{
  "entry_version": 84,
  "evidence_id": "H11",
  "excerpt": "FT   BINDING         186\nFT                   /ligand=\"N-[(R)-4-phosphopantothenoyl]-L-cysteine\"\nFT                   /ligand_id=\"ChEBI:CHEBI:59458\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SWE5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:37.263279+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 180-183",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9ba69ef0f337ff2a30393964c793af5f757c0c52e62614aa37894bfe6ab8f68d",
  "url": "https://rest.uniprot.org/unisave/C6TA59?format=txt&versions=84"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6TA59?format=txt&versions=84)

```json
{
  "entry_version": 84,
  "evidence_id": "H12",
  "excerpt": "FT   SITE            178\nFT                   /note=\"Important for catalytic activity\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9SWE5\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:37.263279+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 184-186",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9ba69ef0f337ff2a30393964c793af5f757c0c52e62614aa37894bfe6ab8f68d",
  "url": "https://rest.uniprot.org/unisave/C6TA59?format=txt&versions=84"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 74. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
