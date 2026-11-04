# active_site_0130

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0130.txt)

**Task:** `active_site`  
**Expected answer:** **A** — Position 170 (Nucleophile)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MVSTNAGGIASKQASSMAPNPGKATILALGHAFPQQLVMQDYVVDGFMRNTNCDDPELKEKLTRLCKTTTVKTRYVVMSEEILKSYPELAQEGQPTMKQRLDISNKAVTQMATEASLACVRSWGGALSEITHLVYVSSSEARFPGGDLHLARALGLSPDVRRVMLAFTGCSGGVAGLRVAKGLAESCPGARVLLATSETTIVGFRPPSPDRPYDLVGVALFGDGAGAAVVGADPTPVERPLFELHSALQRFLPDTDKTIDGRLTEEGIKFQLGRELPHIIEANVEAFCQKLMQEHPQAADKLTYGDMFWAVHPGGPAILTKMEGRLGLDGGKLRASRSALRDFGNASSNTIVYVLENMVEETRQRREEAAEEEDCEWGLILAFGPGITFEGILARNLQARARARD

[Multiple Choices]
A. Position 170 (Nucleophile)
B. Position 1978 (For beta-ketoacyl synthase 2 activity)
C. Position 2711 (For beta-ketoacyl synthase 2 activity)
D. Position 975 (Proton acceptor; for dehydratase activity)
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

> The sequence-matched UniProt record annotates residue 170 as the nucleophile. This is a similarity-based annotation, not direct experimental evidence in the supplied excerpts, but it is consistent with the conserved catalytic nucleophile of type III polyketide synthases.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The roughly 400-residue sequence and its conserved motifs are consistent with a type III polyketide synthase. Family-level knowledge identifies a conserved active-site cysteine that acts as the nucleophile; residue 170 is the corresponding candidate. The other choices refer to beta-ketoacyl synthase or dehydratase activities and give positions far beyond this sequence's 405 residues.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A transferable enzyme-family inference meaningfully distinguishes A from the offered alternatives; recalling this exact protein's database record is not necessary.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only A gives a plausible position and catalytic role for this sequence; the other positions exceed its length or describe unrelated activities.


### Important caveats

- The cited active-site annotation is transferred by similarity from another UniProt entry; the supplied evidence does not establish direct experimental verification for this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The roughly 400-residue sequence and its conserved motifs are consistent with a type III polyketide synthase. Family-level knowledge identifies a conserved active-site cysteine that acts as the nucleophile; residue 170 is the corresponding candidate. The other choices refer to beta-ketoacyl synthase or dehydratase activities and give positions far beyond this sequence's 405 residues.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A transferable enzyme-family inference meaningfully distinguishes A from the offered alternatives; recalling this exact protein's database record is not necessary."
  },
  "case_id": "active_site_0130",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates residue 170 as the nucleophile. This is a similarity-based annotation, not direct experimental evidence in the supplied excerpts, but it is consistent with the conserved catalytic nucleophile of type III polyketide synthases."
  },
  "important_caveats": [
    "The cited active-site annotation is transferred by similarity from another UniProt entry; the supplied evidence does not establish direct experimental verification for this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only A gives a plausible position and catalytic role for this sequence; the other positions exceed its length or describe unrelated activities."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0130",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates residue 170 as the nucleophile. This is a similarity-based annotation, not direct experimental evidence in the supplied excerpts, but it is consistent with the conserved catalytic nucleophile of type III polyketide synthases.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The roughly 400-residue sequence and its conserved motifs are consistent with a type III polyketide synthase. Family-level knowledge identifies a conserved active-site cysteine that acts as the nucleophile; residue 170 is the corresponding candidate. The other choices refer to beta-ketoacyl synthase or dehydratase activities and give positions far beyond this sequence's 405 residues.",
    "missing_item_specific_fact": "",
    "reason": "A transferable enzyme-family inference meaningfully distinguishes A from the offered alternatives; recalling this exact protein's database record is not necessary."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only A gives a plausible position and catalytic role for this sequence; the other positions exceed its length or describe unrelated activities."
  },
  "important_caveats": [
    "The cited active-site annotation is transferred by similarity from another UniProt entry; the supplied evidence does not establish direct experimental verification for this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q8H305 (Type III polyketide synthase 10 / OsPKS10, rice) annotates position 170 as an active-site nucleophile (Cys), with evidence code ECO:0000250 (by similarity to Q94FV7). The supplied 405-residue sequence indeed has Cys at position 170 (within the conserved 'GCSGG' motif at ~168-172), which is the catalytic nucleophile in Type III PKS enzymes. The other options reference positions 1978, 2711, and 975, all far exceeding the 405-residue sequence length, making them physically impossible for this protein.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Three independent lines of transferable reasoning distinguish option A: (1) The supplied sequence is 405 amino acids long. Options B (position 1978), C (position 2711), and D (position 975) all cite residue numbers far exceeding the sequence length, making them trivially eliminable from the input alone. (2) The sequence contains the hallmark conserved motifs of Type III polyketide synthases (chalcone synthase family): the 'GCSGG' motif around positions 168-172 (catalytic Cys nucleophile), the 'FGDGAGAAVV' motif (~221-230), and the 'GPG' motif near the C-terminus. These motifs are shared across hundreds of characterized Type III PKS enzymes (CHS, stilbene synthase, acridone synthase, etc.), and the catalytic Cys in the 'GCGSTG/GCSGG' motif is a well-known, transferable feature of this enzyme family. (3) The overall domain architecture (single ~400-residue chain with these motifs) is diagnostic of Type III PKS rather than the multi-domain Type I PKS or fatty-acid synthase systems that would have active sites at positions in the thousands.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can eliminate B, C, and D purely from the sequence length (405 AA), and confirm A by recognizing the conserved Type III PKS catalytic Cys motif 'GCSGG' at position 170, a pattern learned from the entire chalcone synthase / Type III PKS enzyme family. No memorization of this specific protein's database entry is required.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B, C, and D reference residue positions (1978, 2711, 975) that exceed the 405-residue sequence length, so they are unambiguously invalid. Only option A references a position within the sequence and matches the conserved catalytic motif.


### Important caveats

- The UniProt annotation for the active site at position 170 carries evidence code ECO:0000250 (inferred by similarity to Q94FV7), not direct experimental evidence for this specific protein. However, the catalytic Cys in the GCSGG motif is a well-established, experimentally validated feature across the Type III PKS family.
- The protein is annotated as OsPKS10 (formerly OsPKS2) from Oryza sativa; the alternative name OsPKS2 appears in UniProt but the recommended name is OsPKS10.
- The distractor options (B, C, D) appear to reference positions from a much larger multi-domain protein (possibly a Type I PKS or fatty-acid synthase), making them trivially eliminable by sequence-length check alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Three independent lines of transferable reasoning distinguish option A: (1) The supplied sequence is 405 amino acids long. Options B (position 1978), C (position 2711), and D (position 975) all cite residue numbers far exceeding the sequence length, making them trivially eliminable from the input alone. (2) The sequence contains the hallmark conserved motifs of Type III polyketide synthases (chalcone synthase family): the 'GCSGG' motif around positions 168-172 (catalytic Cys nucleophile), the 'FGDGAGAAVV' motif (~221-230), and the 'GPG' motif near the C-terminus. These motifs are shared across hundreds of characterized Type III PKS enzymes (CHS, stilbene synthase, acridone synthase, etc.), and the catalytic Cys in the 'GCGSTG/GCSGG' motif is a well-known, transferable feature of this enzyme family. (3) The overall domain architecture (single ~400-residue chain with these motifs) is diagnostic of Type III PKS rather than the multi-domain Type I PKS or fatty-acid synthase systems that would have active sites at positions in the thousands.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate B, C, and D purely from the sequence length (405 AA), and confirm A by recognizing the conserved Type III PKS catalytic Cys motif 'GCSGG' at position 170, a pattern learned from the entire chalcone synthase / Type III PKS enzyme family. No memorization of this specific protein's database entry is required."
  },
  "case_id": "active_site_0130",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q8H305 (Type III polyketide synthase 10 / OsPKS10, rice) annotates position 170 as an active-site nucleophile (Cys), with evidence code ECO:0000250 (by similarity to Q94FV7). The supplied 405-residue sequence indeed has Cys at position 170 (within the conserved 'GCSGG' motif at ~168-172), which is the catalytic nucleophile in Type III PKS enzymes. The other options reference positions 1978, 2711, and 975, all far exceeding the 405-residue sequence length, making them physically impossible for this protein."
  },
  "important_caveats": [
    "The UniProt annotation for the active site at position 170 carries evidence code ECO:0000250 (inferred by similarity to Q94FV7), not direct experimental evidence for this specific protein. However, the catalytic Cys in the GCSGG motif is a well-established, experimentally validated feature across the Type III PKS family.",
    "The protein is annotated as OsPKS10 (formerly OsPKS2) from Oryza sativa; the alternative name OsPKS2 appears in UniProt but the recommended name is OsPKS10.",
    "The distractor options (B, C, D) appear to reference positions from a much larger multi-domain protein (possibly a Type I PKS or fatty-acid synthase), making them trivially eliminable by sequence-length check alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B, C, and D reference residue positions (1978, 2711, 975) that exceed the 405-residue sequence length, so they are unambiguously invalid. Only option A references a position within the sequence and matches the conserved catalytic motif."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0130",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q8H305 (Type III polyketide synthase 10 / OsPKS10, rice) annotates position 170 as an active-site nucleophile (Cys), with evidence code ECO:0000250 (by similarity to Q94FV7). The supplied 405-residue sequence indeed has Cys at position 170 (within the conserved 'GCSGG' motif at ~168-172), which is the catalytic nucleophile in Type III PKS enzymes. The other options reference positions 1978, 2711, and 975, all far exceeding the 405-residue sequence length, making them physically impossible for this protein.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Three independent lines of transferable reasoning distinguish option A: (1) The supplied sequence is 405 amino acids long. Options B (position 1978), C (position 2711), and D (position 975) all cite residue numbers far exceeding the sequence length, making them trivially eliminable from the input alone. (2) The sequence contains the hallmark conserved motifs of Type III polyketide synthases (chalcone synthase family): the 'GCSGG' motif around positions 168-172 (catalytic Cys nucleophile), the 'FGDGAGAAVV' motif (~221-230), and the 'GPG' motif near the C-terminus. These motifs are shared across hundreds of characterized Type III PKS enzymes (CHS, stilbene synthase, acridone synthase, etc.), and the catalytic Cys in the 'GCGSTG/GCSGG' motif is a well-known, transferable feature of this enzyme family. (3) The overall domain architecture (single ~400-residue chain with these motifs) is diagnostic of Type III PKS rather than the multi-domain Type I PKS or fatty-acid synthase systems that would have active sites at positions in the thousands.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate B, C, and D purely from the sequence length (405 AA), and confirm A by recognizing the conserved Type III PKS catalytic Cys motif 'GCSGG' at position 170, a pattern learned from the entire chalcone synthase / Type III PKS enzyme family. No memorization of this specific protein's database entry is required."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B, C, and D reference residue positions (1978, 2711, 975) that exceed the 405-residue sequence length, so they are unambiguously invalid. Only option A references a position within the sequence and matches the conserved catalytic motif."
  },
  "important_caveats": [
    "The UniProt annotation for the active site at position 170 carries evidence code ECO:0000250 (inferred by similarity to Q94FV7), not direct experimental evidence for this specific protein. However, the catalytic Cys in the GCSGG motif is a well-established, experimentally validated feature across the Type III PKS family.",
    "The protein is annotated as OsPKS10 (formerly OsPKS2) from Oryza sativa; the alternative name OsPKS2 appears in UniProt but the recommended name is OsPKS10.",
    "The distractor options (B, C, D) appear to reference positions from a much larger multi-domain protein (possibly a Type I PKS or fatty-acid synthase), making them trivially eliminable by sequence-length check alone."
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
  "benchmark_sequence_length": 405,
  "benchmark_sequence_sha256": "8a56cfb606e4fe50f8190fb2e20628feacd1ddf83ddaf17985ab255c0e083848",
  "current_entry_audit": {
    "entryVersion": 133,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2003-03-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "725c43792b5cff8298b1771be62e5326ec303acf22c3a36d81c4c5bf4079ff65",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 405,
  "current_source_sequence_sha256": "8a56cfb606e4fe50f8190fb2e20628feacd1ddf83ddaf17985ab255c0e083848",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 131,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q8H305",
  "selected_historical_entry_version": 131,
  "selected_historical_record_sha256": "087e3fd396545934ba1c15f147eb9357fac43fedfd73e6e5d9a9e98b77653b37",
  "selected_historical_source_sequence_length": 405,
  "selected_historical_source_sequence_sha256": "8a56cfb606e4fe50f8190fb2e20628feacd1ddf83ddaf17985ab255c0e083848",
  "selected_historical_version": {
    "accession": "Q8H305",
    "database": "Swiss-Prot",
    "entryVersion": 131,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "PKS10_ORYSJ",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8H305.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q8H305\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:31:57.631660+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "725c43792b5cff8298b1771be62e5326ec303acf22c3a36d81c4c5bf4079ff65",
  "url": "https://rest.uniprot.org/uniprotkb/Q8H305.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8H305.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":133,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2003-03-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:31:57.631660+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "725c43792b5cff8298b1771be62e5326ec303acf22c3a36d81c4c5bf4079ff65",
  "url": "https://rest.uniprot.org/uniprotkb/Q8H305.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8H305.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Rice\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"Liliopsida\",\"Poales\",\"Poaceae\",\"BOP clade\",\"Oryzoideae\",\"Oryzeae\",\"Oryzinae\",\"Oryza\",\"Oryza sativa\"],\"scientificName\":\"Oryza sativa subsp. japonica\",\"taxonId\":39947}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:31:57.631660+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "725c43792b5cff8298b1771be62e5326ec303acf22c3a36d81c4c5bf4079ff65",
  "url": "https://rest.uniprot.org/uniprotkb/Q8H305.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8H305.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"28783252\",\"source\":\"PubMed\"}],\"value\":\"Type III polyketide synthase 2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"28783252\",\"source\":\"PubMed\"}],\"value\":\"OsPKS2\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"28783252\",\"source\":\"PubMed\"}],\"value\":\"2.3.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"27878652\",\"source\":\"PubMed\"}],\"value\":\"Type III polyketide synthase 10\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"27878652\",\"source\":\"PubMed\"}],\"value\":\"OsPKS10\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:31:57.631660+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "725c43792b5cff8298b1771be62e5326ec303acf22c3a36d81c4c5bf4079ff65",
  "url": "https://rest.uniprot.org/uniprotkb/Q8H305.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8H305.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Nucleophile\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q94FV7\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":170},\"start\":{\"modifier\":\"EXACT\",\"value\":170}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:31:57.631660+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "725c43792b5cff8298b1771be62e5326ec303acf22c3a36d81c4c5bf4079ff65",
  "url": "https://rest.uniprot.org/uniprotkb/Q8H305.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8H305.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhu X.\",\"Yu J.\",\"Shi J.\",\"Tohge T.\",\"Fernie A.R.\",\"Meir S.\",\"Aharoni A.\",\"Xu D.\",\"Zhang D.\",\"Liang W.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"28783252\"},{\"database\":\"DOI\",\"id\":\"10.1111/jipb.12574\"}],\"citationType\":\"journal article\",\"firstPage\":\"612\",\"id\":\"28783252\",\"journal\":\"J. Integr. Plant Biol.\",\"lastPage\":\"628\",\"publicationDate\":\"2017\",\"title\":\"The polyketide synthase OsPKS2 is essential for pollen exine and Ubisch body patterning in rice.\",\"volume\":\"59\"},\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"DEVELOPMENTAL STAGE\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:31:57.631660+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "725c43792b5cff8298b1771be62e5326ec303acf22c3a36d81c4c5bf4079ff65",
  "url": "https://rest.uniprot.org/uniprotkb/Q8H305.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8H305.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Hu L.\",\"He H.\",\"Zhu C.\",\"Peng X.\",\"Fu J.\",\"He X.\",\"Chen X.\",\"Ouyang L.\",\"Bian J.\",\"Liu S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"27878652\"},{\"database\":\"DOI\",\"id\":\"10.1007/s10265-016-0871-7\"}],\"citationType\":\"journal article\",\"firstPage\":\"95\",\"id\":\"27878652\",\"journal\":\"J. Plant Res.\",\"lastPage\":\"105\",\"publicationDate\":\"2017\",\"title\":\"Genome-wide identification and phylogenetic analysis of the chalcone synthase gene family in rice.\",\"volume\":\"130\"},\"referenceNumber\":5,\"referencePositions\":[\"GENE FAMILY\",\"NOMENCLATURE\",\"TISSUE SPECIFICITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-02T04:31:57.631660+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "725c43792b5cff8298b1771be62e5326ec303acf22c3a36d81c4c5bf4079ff65",
  "url": "https://rest.uniprot.org/uniprotkb/Q8H305.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8H305?format=txt&versions=131)

```json
{
  "entry_version": 131,
  "evidence_id": "H1",
  "excerpt": "ID   PKS10_ORYSJ             Reviewed;         405 AA.\nAC   Q8H305; A0A5S6RAJ2; Q0D710;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAR-2003, sequence version 1.\nDT   28-JAN-2026, entry version 131.\nDE   RecName: Full=Type III polyketide synthase 10 {ECO:0000303|PubMed:27878652};\nDE            Short=OsPKS10 {ECO:0000303|PubMed:27878652};\nDE            EC=2.3.1.- {ECO:0000269|PubMed:28783252};\nDE   AltName: Full=Type III polyketide synthase 2 {ECO:0000303|PubMed:28783252};\nDE            Short=OsPKS2 {ECO:0000303|PubMed:28783252};\nGN   Name=PKS10 {ECO:0000303|PubMed:27878652};\nGN   Synonyms=PKS2 {ECO:0000303|PubMed:28783252};\nGN   OrderedLocusNames=Os07g0411300 {ECO:0000312|EMBL:BAT01127.1},\nGN   LOC_Os07g22850 {ECO:0000305};\nOS   Oryza sativa subsp. japonica (Rice).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; Liliopsida; Poales; Poaceae; BOP clade;\nOC   Oryzoideae; Oryzeae; Oryzinae; Oryza; Oryza sativa.\nOX   NCBI_TaxID=39947;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:02.084503+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-19",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "087e3fd396545934ba1c15f147eb9357fac43fedfd73e6e5d9a9e98b77653b37",
  "url": "https://rest.uniprot.org/unisave/Q8H305?format=txt&versions=131"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8H305?format=txt&versions=131)

```json
{
  "entry_version": 131,
  "evidence_id": "H2",
  "excerpt": "RN   [4]\nRP   FUNCTION, CATALYTIC ACTIVITY, DEVELOPMENTAL STAGE, AND DISRUPTION\nRP   PHENOTYPE.\nRX   PubMed=28783252; DOI=10.1111/jipb.12574;\nRA   Zhu X., Yu J., Shi J., Tohge T., Fernie A.R., Meir S., Aharoni A., Xu D.,\nRA   Zhang D., Liang W.;\nRT   \"The polyketide synthase OsPKS2 is essential for pollen exine and Ubisch\nRT   body patterning in rice.\";\nRL   J. Integr. Plant Biol. 59:612-628(2017).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:02.084503+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 45-53",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "087e3fd396545934ba1c15f147eb9357fac43fedfd73e6e5d9a9e98b77653b37",
  "url": "https://rest.uniprot.org/unisave/Q8H305?format=txt&versions=131"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8H305?format=txt&versions=131)

```json
{
  "entry_version": 131,
  "evidence_id": "H3",
  "excerpt": "RN   [5]\nRP   GENE FAMILY, NOMENCLATURE, AND TISSUE SPECIFICITY.\nRX   PubMed=27878652; DOI=10.1007/s10265-016-0871-7;\nRA   Hu L., He H., Zhu C., Peng X., Fu J., He X., Chen X., Ouyang L., Bian J.,\nRA   Liu S.;\nRT   \"Genome-wide identification and phylogenetic analysis of the chalcone\nRT   synthase gene family in rice.\";\nRL   J. Plant Res. 130:95-105(2017).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:02.084503+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 54-61",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "087e3fd396545934ba1c15f147eb9357fac43fedfd73e6e5d9a9e98b77653b37",
  "url": "https://rest.uniprot.org/unisave/Q8H305?format=txt&versions=131"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8H305?format=txt&versions=131)

```json
{
  "entry_version": 131,
  "evidence_id": "H4",
  "excerpt": "FT   ACT_SITE        170\nFT                   /note=\"Nucleophile\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q94FV7\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:02.084503+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 162-164",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "087e3fd396545934ba1c15f147eb9357fac43fedfd73e6e5d9a9e98b77653b37",
  "url": "https://rest.uniprot.org/unisave/Q8H305?format=txt&versions=131"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 130. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
