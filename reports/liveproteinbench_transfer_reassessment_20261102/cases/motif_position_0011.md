# motif_position_0011

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/motif_position_0011.txt)

**Task:** `motif_position`  
**Expected answer:** **A** — 128..147

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MLPKVESEYLGLARSHGEQGHMPGNMQAPQFKMMDYSYDEDLDEMCPVCGDKVSGYHYGLLTCESCKGFFKRTVQNNKRYTCIENQSCQIDKTQRKRCPYCRFQKCLTVGMKLEAVRADRMRGGRNKFGPMYKRDRALKQQKKALIRANGLKLEAMTQVMQTVPADLTITSAIQNIHSASKGLPLSHHHHHHHHHHHHSSSSAGLPPADFDRSPFVTSPVSMAMPPHAGGLQGYQAYGHFQSRTIKSEYPDPYTSSPESLMGYPYVEAYAGGSPPSFPHLVVELLKCEPDEPQVQAKILAYLQQEQASRGKHEKLNTFGLMCKMADQTLFSIVEWARSSIFFRELKVDDQMKLLQNCWSELLILDHVFRQVMHAKEGSILLVTGQQVDYALIASQAGATLNNLLSHAQELVSKLRSLQLDQREFVCLKFLVLFSLDVKNLENFHLVESVQEQVNAALLDYVMCNYPQQTDKFGQLLLRLPEIRAISLQAEEYLYYKHLNGDVPCNNLLIEMLHAKRA

[Multiple Choices]
A. 128..147
B. 92..94
C. 6..14
D. 211..213
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Motif Position Prediction, which is to identify the specific positions of a conserved motif within a protein sequence. A motif is a short, recurring pattern in protein sequences that is often associated with a specific function or structure. Based on the provided protein sequence, you will need to determine the start and end positions of the motif.. The inputs provided by the user for this task include:

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

> The matched sequence is annotated with a motif at 128..147 named the FTZ-F1 box. This is a similarity-based annotation, not evidence of a direct experimental measurement of the motif boundaries.

Citations as saved: [C11](#evidence-c11), [H10](#evidence-h10).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has the characteristic C4 zinc-finger region of a nuclear-receptor DNA-binding domain, followed downstream by the region where the FTZ-F1/NR5A family box occurs. Transferable knowledge of nuclear-receptor and FTZ-F1-family architecture makes the 20-residue interval at 128..147 a credible choice; the other options do not fit that expected motif placement or length.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Although the prompt does not name the motif, the sequence and offered coordinates permit a meaningful family-level inference without knowing this exact protein's recorded annotation. This is a probabilistic inference, not a guarantee of the annotated boundaries.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The motif is not explicitly named, but the sequence's recognizable nuclear-receptor architecture and the answer choices make A the defensible family-level match.


### Important caveats

- The database motif annotation is supported by similarity to another UniProt entry; the supplied evidence does not establish experimental validation of these exact boundaries.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has the characteristic C4 zinc-finger region of a nuclear-receptor DNA-binding domain, followed downstream by the region where the FTZ-F1/NR5A family box occurs. Transferable knowledge of nuclear-receptor and FTZ-F1-family architecture makes the 20-residue interval at 128..147 a credible choice; the other options do not fit that expected motif placement or length.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Although the prompt does not name the motif, the sequence and offered coordinates permit a meaningful family-level inference without knowing this exact protein's recorded annotation. This is a probabilistic inference, not a guarantee of the annotated boundaries."
  },
  "case_id": "motif_position_0011",
  "expected_answer_check": {
    "evidence_ids": [
      "C11",
      "H10"
    ],
    "judgment": "supported",
    "reason": "The matched sequence is annotated with a motif at 128..147 named the FTZ-F1 box. This is a similarity-based annotation, not evidence of a direct experimental measurement of the motif boundaries."
  },
  "important_caveats": [
    "The database motif annotation is supported by similarity to another UniProt entry; the supplied evidence does not establish experimental validation of these exact boundaries."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The motif is not explicitly named, but the sequence's recognizable nuclear-receptor architecture and the answer choices make A the defensible family-level match."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "motif_position_0011",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence is annotated with a motif at 128..147 named the FTZ-F1 box. This is a similarity-based annotation, not evidence of a direct experimental measurement of the motif boundaries.",
    "evidence_ids": ["C11", "H10"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has the characteristic C4 zinc-finger region of a nuclear-receptor DNA-binding domain, followed downstream by the region where the FTZ-F1/NR5A family box occurs. Transferable knowledge of nuclear-receptor and FTZ-F1-family architecture makes the 20-residue interval at 128..147 a credible choice; the other options do not fit that expected motif placement or length.",
    "missing_item_specific_fact": "",
    "reason": "Although the prompt does not name the motif, the sequence and offered coordinates permit a meaningful family-level inference without knowing this exact protein's recorded annotation. This is a probabilistic inference, not a guarantee of the annotated boundaries."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The motif is not explicitly named, but the sequence's recognizable nuclear-receptor architecture and the answer choices make A the defensible family-level match."
  },
  "important_caveats": [
    "The database motif annotation is supported by similarity to another UniProt entry; the supplied evidence does not establish experimental validation of these exact boundaries."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (evidence C11, H10) explicitly labels positions 128..147 as the 'FTZ-F1 box' Motif (feature type: Motif), with evidence code ECO:0000250 (similarity to human NR5A2/O00482). This is a computational annotation transferred by family similarity rather than experimentally validated for this exact zebrafish protein, but it is the sole feature typed as 'Motif' in the entry. The sequence at 128-147 (FGP MYKRDRALKQQKKALIR) contains the characteristic RDR and KK elements of the FTZ-F1 box consensus.

Citations as saved: [C11](#evidence-c11), [H10](#evidence-h10).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein sequence contains two clearly recognizable C4-type nuclear receptor zinc finger domains (C-x2-C-x13-C-x2-C patterns at approximately positions 46-66 and 82-101), identifying it as a nuclear receptor. Among NR5A family members (SF-1/NR5A1, LRH-1/NR5A2), a conserved ~20-residue 'FTZ-F1 box' motif is well-known to reside in the hinge region between the DNA-binding domain (zinc fingers) and the ligand-binding domain. Option A (128..147, 20 residues) is the only choice located in this hinge region and of appropriate motif length. The sequence there (FGP MYKRDRALKQQKKALIR) contains the diagnostic RDR and KK elements of the FTZ-F1 box consensus. Options B (92..94) and D (211..213) are only 3 residues — far too short to constitute a 'conserved motif' — and fall within the zinc finger and disordered regions respectively. Option C (6..14) is in the N-terminal A/B domain, which is not a site of a named conserved motif in this family. Thus, family-level knowledge of NR5A hinge-region architecture and the FTZ-F1 box consensus meaningfully distinguishes A from the other choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model familiar with nuclear receptor biology and the NR5A family can recognize the zinc finger domains, infer the hinge-region location, recall that NR5A proteins carry a ~20-residue FTZ-F1 box motif between DBD and LBD, and match the sequence features (RDR, KK) at 128-147. The 3-residue alternatives (B, D) are implausibly short for a 'conserved motif,' and C is in the wrong structural context. This is transferable family knowledge, not a lookup of this protein's specific annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The question asks for 'a conserved motif' without naming it, but among the four choices only A is both of appropriate motif length (20 residues) and located in the structurally correct hinge region of a nuclear receptor. The 3-residue options (B, D) are not credible 'motifs,' and C is in the poorly conserved N-terminal domain. No other option is defensible.


### Important caveats

- The FTZ-F1 box annotation is based on similarity transfer (ECO:0000250) from human NR5A2 (O00482), not direct experimental validation on this zebrafish protein.
- The question does not name the motif, relying on the model to infer which conserved motif is being asked about from context and the answer choices.
- The protein sequence includes a His-tag (HHHHHHHHHHHHH) and SSSS linker around positions 187-204, indicating this is a recombinant construct sequence; numbering is based on the canonical entry coordinates.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein sequence contains two clearly recognizable C4-type nuclear receptor zinc finger domains (C-x2-C-x13-C-x2-C patterns at approximately positions 46-66 and 82-101), identifying it as a nuclear receptor. Among NR5A family members (SF-1/NR5A1, LRH-1/NR5A2), a conserved ~20-residue 'FTZ-F1 box' motif is well-known to reside in the hinge region between the DNA-binding domain (zinc fingers) and the ligand-binding domain. Option A (128..147, 20 residues) is the only choice located in this hinge region and of appropriate motif length. The sequence there (FGP MYKRDRALKQQKKALIR) contains the diagnostic RDR and KK elements of the FTZ-F1 box consensus. Options B (92..94) and D (211..213) are only 3 residues — far too short to constitute a 'conserved motif' — and fall within the zinc finger and disordered regions respectively. Option C (6..14) is in the N-terminal A/B domain, which is not a site of a named conserved motif in this family. Thus, family-level knowledge of NR5A hinge-region architecture and the FTZ-F1 box consensus meaningfully distinguishes A from the other choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model familiar with nuclear receptor biology and the NR5A family can recognize the zinc finger domains, infer the hinge-region location, recall that NR5A proteins carry a ~20-residue FTZ-F1 box motif between DBD and LBD, and match the sequence features (RDR, KK) at 128-147. The 3-residue alternatives (B, D) are implausibly short for a 'conserved motif,' and C is in the wrong structural context. This is transferable family knowledge, not a lookup of this protein's specific annotation."
  },
  "case_id": "motif_position_0011",
  "expected_answer_check": {
    "evidence_ids": [
      "C11",
      "H10"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C11, H10) explicitly labels positions 128..147 as the 'FTZ-F1 box' Motif (feature type: Motif), with evidence code ECO:0000250 (similarity to human NR5A2/O00482). This is a computational annotation transferred by family similarity rather than experimentally validated for this exact zebrafish protein, but it is the sole feature typed as 'Motif' in the entry. The sequence at 128-147 (FGP MYKRDRALKQQKKALIR) contains the characteristic RDR and KK elements of the FTZ-F1 box consensus."
  },
  "important_caveats": [
    "The FTZ-F1 box annotation is based on similarity transfer (ECO:0000250) from human NR5A2 (O00482), not direct experimental validation on this zebrafish protein.",
    "The question does not name the motif, relying on the model to infer which conserved motif is being asked about from context and the answer choices.",
    "The protein sequence includes a His-tag (HHHHHHHHHHHHH) and SSSS linker around positions 187-204, indicating this is a recombinant construct sequence; numbering is based on the canonical entry coordinates."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The question asks for 'a conserved motif' without naming it, but among the four choices only A is both of appropriate motif length (20 residues) and located in the structurally correct hinge region of a nuclear receptor. The 3-residue options (B, D) are not credible 'motifs,' and C is in the poorly conserved N-terminal domain. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "motif_position_0011",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C11, H10) explicitly labels positions 128..147 as the 'FTZ-F1 box' Motif (feature type: Motif), with evidence code ECO:0000250 (similarity to human NR5A2/O00482). This is a computational annotation transferred by family similarity rather than experimentally validated for this exact zebrafish protein, but it is the sole feature typed as 'Motif' in the entry. The sequence at 128-147 (FGP MYKRDRALKQQKKALIR) contains the characteristic RDR and KK elements of the FTZ-F1 box consensus.",
    "evidence_ids": ["C11", "H10"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein sequence contains two clearly recognizable C4-type nuclear receptor zinc finger domains (C-x2-C-x13-C-x2-C patterns at approximately positions 46-66 and 82-101), identifying it as a nuclear receptor. Among NR5A family members (SF-1/NR5A1, LRH-1/NR5A2), a conserved ~20-residue 'FTZ-F1 box' motif is well-known to reside in the hinge region between the DNA-binding domain (zinc fingers) and the ligand-binding domain. Option A (128..147, 20 residues) is the only choice located in this hinge region and of appropriate motif length. The sequence there (FGP MYKRDRALKQQKKALIR) contains the diagnostic RDR and KK elements of the FTZ-F1 box consensus. Options B (92..94) and D (211..213) are only 3 residues — far too short to constitute a 'conserved motif' — and fall within the zinc finger and disordered regions respectively. Option C (6..14) is in the N-terminal A/B domain, which is not a site of a named conserved motif in this family. Thus, family-level knowledge of NR5A hinge-region architecture and the FTZ-F1 box consensus meaningfully distinguishes A from the other choices.",
    "missing_item_specific_fact": "",
    "reason": "A model familiar with nuclear receptor biology and the NR5A family can recognize the zinc finger domains, infer the hinge-region location, recall that NR5A proteins carry a ~20-residue FTZ-F1 box motif between DBD and LBD, and match the sequence features (RDR, KK) at 128-147. The 3-residue alternatives (B, D) are implausibly short for a 'conserved motif,' and C is in the wrong structural context. This is transferable family knowledge, not a lookup of this protein's specific annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The question asks for 'a conserved motif' without naming it, but among the four choices only A is both of appropriate motif length (20 residues) and located in the structurally correct hinge region of a nuclear receptor. The 3-residue options (B, D) are not credible 'motifs,' and C is in the poorly conserved N-terminal domain. No other option is defensible."
  },
  "important_caveats": [
    "The FTZ-F1 box annotation is based on similarity transfer (ECO:0000250) from human NR5A2 (O00482), not direct experimental validation on this zebrafish protein.",
    "The question does not name the motif, relying on the model to infer which conserved motif is being asked about from context and the answer choices.",
    "The protein sequence includes a His-tag (HHHHHHHHHHHHH) and SSSS linker around positions 187-204, indicating this is a recombinant construct sequence; numbering is based on the canonical entry coordinates."
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
  "benchmark_sequence_length": 517,
  "benchmark_sequence_sha256": "b7c785e3944855ed1e7aa9faa32091cc02df77098be954cc64b2cd3e8976bce9",
  "current_entry_audit": {
    "entryVersion": 184,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2001-12-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "d44c7f7cfbc5ec1817e4243a16d89625902bfbce478c41a8825d7a9540940b60",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 517,
  "current_source_sequence_sha256": "b7c785e3944855ed1e7aa9faa32091cc02df77098be954cc64b2cd3e8976bce9",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 182,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q90YL6",
  "selected_historical_entry_version": 182,
  "selected_historical_record_sha256": "a4d164dbcc6a2a9361980ddd54854f2823cbd7222b59caaa941115286c3e2d39",
  "selected_historical_source_sequence_length": 517,
  "selected_historical_source_sequence_sha256": "b7c785e3944855ed1e7aa9faa32091cc02df77098be954cc64b2cd3e8976bce9",
  "selected_historical_version": {
    "accession": "Q90YL6",
    "database": "Swiss-Prot",
    "entryVersion": 182,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "NR5A2_DANRE",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q90YL6.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q90YL6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:32:31.842408+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d44c7f7cfbc5ec1817e4243a16d89625902bfbce478c41a8825d7a9540940b60",
  "url": "https://rest.uniprot.org/uniprotkb/Q90YL6.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q90YL6.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":184,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2001-12-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:32:31.842408+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d44c7f7cfbc5ec1817e4243a16d89625902bfbce478c41a8825d7a9540940b60",
  "url": "https://rest.uniprot.org/uniprotkb/Q90YL6.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q90YL6.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Zebrafish\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Euteleostomi\",\"Actinopterygii\",\"Neopterygii\",\"Teleostei\",\"Ostariophysi\",\"Cypriniformes\",\"Danionidae\",\"Danioninae\",\"Danio\"],\"scientificName\":\"Danio rerio\",\"synonyms\":[\"Brachydanio rerio\"],\"taxonId\":7955}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:32:31.842408+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d44c7f7cfbc5ec1817e4243a16d89625902bfbce478c41a8825d7a9540940b60",
  "url": "https://rest.uniprot.org/uniprotkb/Q90YL6.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q90YL6.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"9178748\",\"source\":\"PubMed\"}],\"value\":\"FTZ-F1 homolog\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"9178748\",\"source\":\"PubMed\"}],\"value\":\"zFF1\"}]},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"28642062\",\"source\":\"PubMed\"}],\"value\":\"Liver receptor homolog 1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"28642062\",\"source\":\"PubMed\"}],\"value\":\"LRH-1\"}]}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Nuclear receptor subfamily 5 group A member 2\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:32:31.842408+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d44c7f7cfbc5ec1817e4243a16d89625902bfbce478c41a8825d7a9540940b60",
  "url": "https://rest.uniprot.org/uniprotkb/Q90YL6.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q90YL6.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"NR LBD\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01189\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":515},\"start\":{\"modifier\":\"EXACT\",\"value\":276}},\"type\":\"Domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:32:31.842408+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d44c7f7cfbc5ec1817e4243a16d89625902bfbce478c41a8825d7a9540940b60",
  "url": "https://rest.uniprot.org/uniprotkb/Q90YL6.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q90YL6.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"NR C4-type\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00407\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":66},\"start\":{\"modifier\":\"EXACT\",\"value\":46}},\"type\":\"Zinc finger\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:32:31.842408+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d44c7f7cfbc5ec1817e4243a16d89625902bfbce478c41a8825d7a9540940b60",
  "url": "https://rest.uniprot.org/uniprotkb/Q90YL6.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q90YL6.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"NR C4-type\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00407\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":101},\"start\":{\"modifier\":\"EXACT\",\"value\":82}},\"type\":\"Zinc finger\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:32:31.842408+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d44c7f7cfbc5ec1817e4243a16d89625902bfbce478c41a8825d7a9540940b60",
  "url": "https://rest.uniprot.org/uniprotkb/Q90YL6.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q90YL6.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"C-terminal extension (CTE)\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O00482\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":127},\"start\":{\"modifier\":\"EXACT\",\"value\":112}},\"type\":\"Region\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:32:31.842408+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d44c7f7cfbc5ec1817e4243a16d89625902bfbce478c41a8825d7a9540940b60",
  "url": "https://rest.uniprot.org/uniprotkb/Q90YL6.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q90YL6.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Disordered\",\"evidences\":[{\"evidenceCode\":\"ECO:0000256\",\"id\":\"MobiDB-lite\",\"source\":\"SAM\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":211},\"start\":{\"modifier\":\"EXACT\",\"value\":182}},\"type\":\"Region\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:32:31.842408+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d44c7f7cfbc5ec1817e4243a16d89625902bfbce478c41a8825d7a9540940b60",
  "url": "https://rest.uniprot.org/uniprotkb/Q90YL6.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q90YL6.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"AF-2\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01189\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":515},\"start\":{\"modifier\":\"EXACT\",\"value\":504}},\"type\":\"Region\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:32:31.842408+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d44c7f7cfbc5ec1817e4243a16d89625902bfbce478c41a8825d7a9540940b60",
  "url": "https://rest.uniprot.org/uniprotkb/Q90YL6.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q90YL6.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"FTZ-F1 box\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O00482\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":147},\"start\":{\"modifier\":\"EXACT\",\"value\":128}},\"type\":\"Motif\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:32:31.842408+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d44c7f7cfbc5ec1817e4243a16d89625902bfbce478c41a8825d7a9540940b60",
  "url": "https://rest.uniprot.org/uniprotkb/Q90YL6.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q90YL6.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"citation\":{\"authors\":[\"Liu D.\",\"Le Drean Y.\",\"Ekker M.\",\"Xiong F.\",\"Hew C.L.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"9178748\"},{\"database\":\"DOI\",\"id\":\"10.1210/mend.11.7.9947\"}],\"citationType\":\"journal article\",\"firstPage\":\"877\",\"id\":\"9178748\",\"journal\":\"Mol. Endocrinol.\",\"lastPage\":\"890\",\"publicationDate\":\"1997\",\"title\":\"Teleost FTZ-F1 homolog and its splicing variant determine the expression of the salmon gonadotropin IIbeta subunit gene.\",\"volume\":\"11\"},\"referenceNumber\":4,\"referencePositions\":[\"ALTERNATIVE SPLICING\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:32:31.842408+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d44c7f7cfbc5ec1817e4243a16d89625902bfbce478c41a8825d7a9540940b60",
  "url": "https://rest.uniprot.org/uniprotkb/Q90YL6.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q90YL6.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhai G.\",\"Song J.\",\"Shu T.\",\"Yan J.\",\"Jin X.\",\"He J.\",\"Yin Z.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"28642062\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.jgg.2017.03.006\"}],\"citationType\":\"journal article\",\"firstPage\":\"307\",\"id\":\"28642062\",\"journal\":\"J. Genet. Genomics\",\"lastPage\":\"317\",\"publicationDate\":\"2017\",\"title\":\"LRH-1 senses signaling from phosphatidylcholine to regulate the expansion growth of digestive organs via synergy with Wnt/beta-catenin signaling in zebrafish.\",\"volume\":\"44\"},\"referenceNumber\":9,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/8",
  "retrieved_utc": "2026-11-02T04:32:31.842408+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d44c7f7cfbc5ec1817e4243a16d89625902bfbce478c41a8825d7a9540940b60",
  "url": "https://rest.uniprot.org/uniprotkb/Q90YL6.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q90YL6?format=txt&versions=182)

```json
{
  "entry_version": 182,
  "evidence_id": "H1",
  "excerpt": "ID   NR5A2_DANRE             Reviewed;         517 AA.\nAC   Q90YL6; A0A0R4IW70; A0A8M3AXL9; A0A8N7XJG3; B3DJL1;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-DEC-2001, sequence version 1.\nDT   28-JAN-2026, entry version 182.\nDE   RecName: Full=Nuclear receptor subfamily 5 group A member 2 {ECO:0000305};\nDE   AltName: Full=FTZ-F1 homolog {ECO:0000303|PubMed:9178748};\nDE            Short=zFF1 {ECO:0000303|PubMed:9178748};\nDE   AltName: Full=Liver receptor homolog 1 {ECO:0000303|PubMed:28642062};\nDE            Short=LRH-1 {ECO:0000303|PubMed:28642062};\nGN   Name=nr5a2 {ECO:0000312|ZFIN:ZDB-GENE-990415-79};\nGN   Synonyms=ff1a {ECO:0000303|PubMed:9178748};\nOS   Danio rerio (Zebrafish) (Brachydanio rerio).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi;\nOC   Actinopterygii; Neopterygii; Teleostei; Ostariophysi; Cypriniformes;\nOC   Danionidae; Danioninae; Danio.\nOX   NCBI_TaxID=7955;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:34.883642+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a4d164dbcc6a2a9361980ddd54854f2823cbd7222b59caaa941115286c3e2d39",
  "url": "https://rest.uniprot.org/unisave/Q90YL6?format=txt&versions=182"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q90YL6?format=txt&versions=182)

```json
{
  "entry_version": 182,
  "evidence_id": "H2",
  "excerpt": "RN   [4]\nRP   ALTERNATIVE SPLICING.\nRX   PubMed=9178748; DOI=10.1210/mend.11.7.9947;\nRA   Liu D., Le Drean Y., Ekker M., Xiong F., Hew C.L.;\nRT   \"Teleost FTZ-F1 homolog and its splicing variant determine the expression\nRT   of the salmon gonadotropin IIbeta subunit gene.\";\nRL   Mol. Endocrinol. 11:877-890(1997).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:34.883642+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 64-70",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a4d164dbcc6a2a9361980ddd54854f2823cbd7222b59caaa941115286c3e2d39",
  "url": "https://rest.uniprot.org/unisave/Q90YL6?format=txt&versions=182"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q90YL6?format=txt&versions=182)

```json
{
  "entry_version": 182,
  "evidence_id": "H3",
  "excerpt": "RN   [9]\nRP   FUNCTION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=28642062; DOI=10.1016/j.jgg.2017.03.006;\nRA   Zhai G., Song J., Shu T., Yan J., Jin X., He J., Yin Z.;\nRT   \"LRH-1 senses signaling from phosphatidylcholine to regulate the expansion\nRT   growth of digestive organs via synergy with Wnt/beta-catenin signaling in\nRT   zebrafish.\";\nRL   J. Genet. Genomics 44:307-317(2017).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:34.883642+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 103-110",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a4d164dbcc6a2a9361980ddd54854f2823cbd7222b59caaa941115286c3e2d39",
  "url": "https://rest.uniprot.org/unisave/Q90YL6?format=txt&versions=182"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q90YL6?format=txt&versions=182)

```json
{
  "entry_version": 182,
  "evidence_id": "H4",
  "excerpt": "FT   DOMAIN          276..515\nFT                   /note=\"NR LBD\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01189\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:34.883642+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 246-248",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a4d164dbcc6a2a9361980ddd54854f2823cbd7222b59caaa941115286c3e2d39",
  "url": "https://rest.uniprot.org/unisave/Q90YL6?format=txt&versions=182"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q90YL6?format=txt&versions=182)

```json
{
  "entry_version": 182,
  "evidence_id": "H5",
  "excerpt": "FT   ZN_FING         46..66\nFT                   /note=\"NR C4-type\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00407\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:34.883642+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 252-254",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a4d164dbcc6a2a9361980ddd54854f2823cbd7222b59caaa941115286c3e2d39",
  "url": "https://rest.uniprot.org/unisave/Q90YL6?format=txt&versions=182"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q90YL6?format=txt&versions=182)

```json
{
  "entry_version": 182,
  "evidence_id": "H6",
  "excerpt": "FT   ZN_FING         82..101\nFT                   /note=\"NR C4-type\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00407\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:34.883642+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 255-257",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a4d164dbcc6a2a9361980ddd54854f2823cbd7222b59caaa941115286c3e2d39",
  "url": "https://rest.uniprot.org/unisave/Q90YL6?format=txt&versions=182"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q90YL6?format=txt&versions=182)

```json
{
  "entry_version": 182,
  "evidence_id": "H7",
  "excerpt": "FT   REGION          112..127\nFT                   /note=\"C-terminal extension (CTE)\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:O00482\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:34.883642+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 258-260",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a4d164dbcc6a2a9361980ddd54854f2823cbd7222b59caaa941115286c3e2d39",
  "url": "https://rest.uniprot.org/unisave/Q90YL6?format=txt&versions=182"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q90YL6?format=txt&versions=182)

```json
{
  "entry_version": 182,
  "evidence_id": "H8",
  "excerpt": "FT   REGION          182..211\nFT                   /note=\"Disordered\"\nFT                   /evidence=\"ECO:0000256|SAM:MobiDB-lite\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:34.883642+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 261-263",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a4d164dbcc6a2a9361980ddd54854f2823cbd7222b59caaa941115286c3e2d39",
  "url": "https://rest.uniprot.org/unisave/Q90YL6?format=txt&versions=182"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q90YL6?format=txt&versions=182)

```json
{
  "entry_version": 182,
  "evidence_id": "H9",
  "excerpt": "FT   REGION          504..515\nFT                   /note=\"AF-2\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01189\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:34.883642+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 264-266",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a4d164dbcc6a2a9361980ddd54854f2823cbd7222b59caaa941115286c3e2d39",
  "url": "https://rest.uniprot.org/unisave/Q90YL6?format=txt&versions=182"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q90YL6?format=txt&versions=182)

```json
{
  "entry_version": 182,
  "evidence_id": "H10",
  "excerpt": "FT   MOTIF           128..147\nFT                   /note=\"FTZ-F1 box\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:O00482\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:34.883642+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 267-269",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a4d164dbcc6a2a9361980ddd54854f2823cbd7222b59caaa941115286c3e2d39",
  "url": "https://rest.uniprot.org/unisave/Q90YL6?format=txt&versions=182"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/motif_position.json), zero-based source row 11. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
