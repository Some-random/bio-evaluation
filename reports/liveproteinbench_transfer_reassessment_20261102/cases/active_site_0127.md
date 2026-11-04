# active_site_0127

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0127.txt)

**Task:** `active_site`  
**Expected answer:** **C** — Position 156 (Acyl-thioester intermediate)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSVKKAGVLGATGSVGQRFILLLSKHPEFEIHALGASSRSAGKKYKDAASWKQTETLPETEQDIVVQECKPEGNFLECDVVFSGLDADVAGDIEKSFVEAGLAVVSNAKNYRREKDVPLVVPIVNPEHIDVVENKVKQAVSKGGKKPGFIICISNCSTAGLVAPLKPLVEKFGPIDALTTTTLQAISGAGFSPGVSGMDILDNIVPYISGEEDKLEWETKKILGGVNAEGTEFVPIPESEMKVSAQCNRVPVIDGHTECISLRFANRPAPSVEDVKQCLREYECAASKLGCHSAPKQTIHVLDQPDRPQPRLDRDRDSGYGVSVGRIREDSLLDFKMVVLSHNTIIGAAGAGILIAEILKAKNII

[Multiple Choices]
A. Position 1141 (Proton donor; for dehydratase activity 1)
B. Position 215 (Proton acceptor)
C. Position 156 (Acyl-thioester intermediate)
D. Position 308 (Proton acceptor)
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

> The sequence-matched UniProt records annotate residue 156 as the acyl-thioester intermediate site. This is computational PIRSR annotation, not direct experimental evidence for that residue, but it supports the keyed claim.

Citations as saved: [C5](#evidence-c5), [H8](#evidence-h8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a conserved cysteine-rich motif around position 156, consistent with the catalytic nucleophile of an aspartate-semialdehyde-dehydrogenase-like enzyme. In this enzyme family, the catalytic cysteine forms a covalent acyl-thioester intermediate, supporting choice C over the proton-acceptor alternatives. The sequence also lets the solver count the residue position; choice A is incompatible with the sequence length.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level catalytic mechanism and the sequence motif provide a credible transferable basis for distinguishing the acyl-thioester role from the offered proton-acceptor roles. The exact annotation is not required to make that inference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, the catalytic-cysteine acyl-thioester role is meaningfully distinguished; the other listed positions and roles are not supported by the sequence-family inference.


### Important caveats

- The supporting database annotation is computationally transferred by a family rule, rather than being direct experimental validation of residue 156.
- The reviewer-only sequence-matched source evidence was not part of the original model input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a conserved cysteine-rich motif around position 156, consistent with the catalytic nucleophile of an aspartate-semialdehyde-dehydrogenase-like enzyme. In this enzyme family, the catalytic cysteine forms a covalent acyl-thioester intermediate, supporting choice C over the proton-acceptor alternatives. The sequence also lets the solver count the residue position; choice A is incompatible with the sequence length.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level catalytic mechanism and the sequence motif provide a credible transferable basis for distinguishing the acyl-thioester role from the offered proton-acceptor roles. The exact annotation is not required to make that inference."
  },
  "case_id": "active_site_0127",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H8"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt records annotate residue 156 as the acyl-thioester intermediate site. This is computational PIRSR annotation, not direct experimental evidence for that residue, but it supports the keyed claim."
  },
  "important_caveats": [
    "The supporting database annotation is computationally transferred by a family rule, rather than being direct experimental validation of residue 156.",
    "The reviewer-only sequence-matched source evidence was not part of the original model input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, the catalytic-cysteine acyl-thioester role is meaningfully distinguished; the other listed positions and roles are not supported by the sequence-family inference."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0127",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt records annotate residue 156 as the acyl-thioester intermediate site. This is computational PIRSR annotation, not direct experimental evidence for that residue, but it supports the keyed claim.",
    "evidence_ids": ["C5", "H8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a conserved cysteine-rich motif around position 156, consistent with the catalytic nucleophile of an aspartate-semialdehyde-dehydrogenase-like enzyme. In this enzyme family, the catalytic cysteine forms a covalent acyl-thioester intermediate, supporting choice C over the proton-acceptor alternatives. The sequence also lets the solver count the residue position; choice A is incompatible with the sequence length.",
    "missing_item_specific_fact": "",
    "reason": "Family-level catalytic mechanism and the sequence motif provide a credible transferable basis for distinguishing the acyl-thioester role from the offered proton-acceptor roles. The exact annotation is not required to make that inference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, the catalytic-cysteine acyl-thioester role is meaningfully distinguished; the other listed positions and roles are not supported by the sequence-family inference."
  },
  "important_caveats": [
    "The supporting database annotation is computationally transferred by a family rule, rather than being direct experimental validation of residue 156.",
    "The reviewer-only sequence-matched source evidence was not part of the original model input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q5ALM0 (Aspartate-semialdehyde dehydrogenase, Candida albicans) annotates position 156 as 'Acyl-thioester intermediate' active site (evidence code ECO:0000255, PIRSR000148-1). The residue at position 156 in the provided sequence is C (Cysteine), which is mechanistically consistent with thioester intermediate formation in the ASADH family. Although the evidence code indicates similarity-based annotation transfer from the PIRSR pattern rather than direct experimental proof for this specific protein, the catalytic cysteine-thioester mechanism is well-established experimentally across the ASADH family (EC 1.2.1.11). The annotation is scientifically supported.

Citations as saved: [C5](#evidence-c5), [H8](#evidence-h8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model can distinguish the answer through multiple independent reasoning steps: (1) Option A (position 1141) is immediately eliminated because the protein is only 365 residues long. (2) The N-terminal motif 'GVLGATGSVG' (positions 7-16) is a classic Rossmann-fold NAD(P)+-binding motif (GxGxxG), identifying this as a dehydrogenase. (3) Checking the actual amino acid at each candidate position: position 156 is C (Cysteine), position 215 is L (Leucine), position 308 is P (Proline). (4) Leucine and Proline cannot function as proton acceptors (they lack ionizable side chains), immediately eliminating options B and D on basic amino-acid chemistry grounds. (5) Cysteine at position 156, embedded in the conserved 'CISNC' motif (positions 152-156), is the hallmark catalytic residue of ASADH-family enzymes that forms the acyl-thioester intermediate. This family-level conserved motif, combined with the Rossmann fold and the requirement for a thiol nucleophile, makes C the only biochemically plausible answer.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The question is answerable through general biochemistry: (a) eliminating impossible positions, (b) reading the actual residue identity at each candidate position from the sequence, and (c) applying knowledge that only cysteine can form a thioester and that leucine/proline cannot act as proton acceptors. The conserved 'CISNC' motif in ASADH homologs (e.g., E. coli ASADH catalytic Cys135 in an equivalent context) provides family-level transferable knowledge. No protein-specific memorization is required.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only option C is biochemically plausible. Position 1141 exceeds the protein length (eliminates A). Position 215 is Leucine and position 308 is Proline—neither can serve as a proton acceptor (eliminates B and D). Position 156 is Cysteine, the only residue among the options capable of forming a thioester intermediate.


### Important caveats

- The UniProt annotation uses evidence code ECO:0000255 (similarity to PIRSR000148-1), meaning the active-site assignment is based on pattern matching to the ASADH family rather than direct experimental mutagenesis of this specific Candida albicans protein. However, the mechanism is well-established across the family.
- The reviewer-only evidence confirms the sequence matches Q5ALM0 (365 AA, sequence version 1), but the evaluated model was not given the protein name or accession—identification must come from sequence features.
- The question's distractors are effectively self-eliminating through basic amino-acid chemistry (Leu and Pro cannot be proton acceptors; position 1141 is out of range), making the question easier than a typical active-site prediction task.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can distinguish the answer through multiple independent reasoning steps: (1) Option A (position 1141) is immediately eliminated because the protein is only 365 residues long. (2) The N-terminal motif 'GVLGATGSVG' (positions 7-16) is a classic Rossmann-fold NAD(P)+-binding motif (GxGxxG), identifying this as a dehydrogenase. (3) Checking the actual amino acid at each candidate position: position 156 is C (Cysteine), position 215 is L (Leucine), position 308 is P (Proline). (4) Leucine and Proline cannot function as proton acceptors (they lack ionizable side chains), immediately eliminating options B and D on basic amino-acid chemistry grounds. (5) Cysteine at position 156, embedded in the conserved 'CISNC' motif (positions 152-156), is the hallmark catalytic residue of ASADH-family enzymes that forms the acyl-thioester intermediate. This family-level conserved motif, combined with the Rossmann fold and the requirement for a thiol nucleophile, makes C the only biochemically plausible answer.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The question is answerable through general biochemistry: (a) eliminating impossible positions, (b) reading the actual residue identity at each candidate position from the sequence, and (c) applying knowledge that only cysteine can form a thioester and that leucine/proline cannot act as proton acceptors. The conserved 'CISNC' motif in ASADH homologs (e.g., E. coli ASADH catalytic Cys135 in an equivalent context) provides family-level transferable knowledge. No protein-specific memorization is required."
  },
  "case_id": "active_site_0127",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H8"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q5ALM0 (Aspartate-semialdehyde dehydrogenase, Candida albicans) annotates position 156 as 'Acyl-thioester intermediate' active site (evidence code ECO:0000255, PIRSR000148-1). The residue at position 156 in the provided sequence is C (Cysteine), which is mechanistically consistent with thioester intermediate formation in the ASADH family. Although the evidence code indicates similarity-based annotation transfer from the PIRSR pattern rather than direct experimental proof for this specific protein, the catalytic cysteine-thioester mechanism is well-established experimentally across the ASADH family (EC 1.2.1.11). The annotation is scientifically supported."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (similarity to PIRSR000148-1), meaning the active-site assignment is based on pattern matching to the ASADH family rather than direct experimental mutagenesis of this specific Candida albicans protein. However, the mechanism is well-established across the family.",
    "The reviewer-only evidence confirms the sequence matches Q5ALM0 (365 AA, sequence version 1), but the evaluated model was not given the protein name or accession—identification must come from sequence features.",
    "The question's distractors are effectively self-eliminating through basic amino-acid chemistry (Leu and Pro cannot be proton acceptors; position 1141 is out of range), making the question easier than a typical active-site prediction task."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option C is biochemically plausible. Position 1141 exceeds the protein length (eliminates A). Position 215 is Leucine and position 308 is Proline—neither can serve as a proton acceptor (eliminates B and D). Position 156 is Cysteine, the only residue among the options capable of forming a thioester intermediate."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0127",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q5ALM0 (Aspartate-semialdehyde dehydrogenase, Candida albicans) annotates position 156 as 'Acyl-thioester intermediate' active site (evidence code ECO:0000255, PIRSR000148-1). The residue at position 156 in the provided sequence is C (Cysteine), which is mechanistically consistent with thioester intermediate formation in the ASADH family. Although the evidence code indicates similarity-based annotation transfer from the PIRSR pattern rather than direct experimental proof for this specific protein, the catalytic cysteine-thioester mechanism is well-established experimentally across the ASADH family (EC 1.2.1.11). The annotation is scientifically supported.",
    "evidence_ids": ["C5", "H8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model can distinguish the answer through multiple independent reasoning steps: (1) Option A (position 1141) is immediately eliminated because the protein is only 365 residues long. (2) The N-terminal motif 'GVLGATGSVG' (positions 7-16) is a classic Rossmann-fold NAD(P)+-binding motif (GxGxxG), identifying this as a dehydrogenase. (3) Checking the actual amino acid at each candidate position: position 156 is C (Cysteine), position 215 is L (Leucine), position 308 is P (Proline). (4) Leucine and Proline cannot function as proton acceptors (they lack ionizable side chains), immediately eliminating options B and D on basic amino-acid chemistry grounds. (5) Cysteine at position 156, embedded in the conserved 'CISNC' motif (positions 152-156), is the hallmark catalytic residue of ASADH-family enzymes that forms the acyl-thioester intermediate. This family-level conserved motif, combined with the Rossmann fold and the requirement for a thiol nucleophile, makes C the only biochemically plausible answer.",
    "missing_item_specific_fact": "",
    "reason": "The question is answerable through general biochemistry: (a) eliminating impossible positions, (b) reading the actual residue identity at each candidate position from the sequence, and (c) applying knowledge that only cysteine can form a thioester and that leucine/proline cannot act as proton acceptors. The conserved 'CISNC' motif in ASADH homologs (e.g., E. coli ASADH catalytic Cys135 in an equivalent context) provides family-level transferable knowledge. No protein-specific memorization is required."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option C is biochemically plausible. Position 1141 exceeds the protein length (eliminates A). Position 215 is Leucine and position 308 is Proline—neither can serve as a proton acceptor (eliminates B and D). Position 156 is Cysteine, the only residue among the options capable of forming a thioester intermediate."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (similarity to PIRSR000148-1), meaning the active-site assignment is based on pattern matching to the ASADH family rather than direct experimental mutagenesis of this specific Candida albicans protein. However, the mechanism is well-established across the family.",
    "The reviewer-only evidence confirms the sequence matches Q5ALM0 (365 AA, sequence version 1), but the evaluated model was not given the protein name or accession—identification must come from sequence features.",
    "The question's distractors are effectively self-eliminating through basic amino-acid chemistry (Leu and Pro cannot be proton acceptors; position 1141 is out of range), making the question easier than a typical active-site prediction task."
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
  "benchmark_sequence_length": 365,
  "benchmark_sequence_sha256": "6addf96ce62cae01385fdd88f8e959e42e783ffb39b551e1fdaa9f5898f59f56",
  "current_entry_audit": {
    "entryVersion": 147,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2005-04-26",
    "sequenceVersion": 1
  },
  "current_record_sha256": "8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 365,
  "current_source_sequence_sha256": "6addf96ce62cae01385fdd88f8e959e42e783ffb39b551e1fdaa9f5898f59f56",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 145,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q5ALM0",
  "selected_historical_entry_version": 145,
  "selected_historical_record_sha256": "ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d",
  "selected_historical_source_sequence_length": 365,
  "selected_historical_source_sequence_sha256": "6addf96ce62cae01385fdd88f8e959e42e783ffb39b551e1fdaa9f5898f59f56",
  "selected_historical_version": {
    "accession": "Q5ALM0",
    "database": "Swiss-Prot",
    "entryVersion": 145,
    "firstRelease": "2025_03/2025_03",
    "firstReleaseDate": "18-Jun-2025",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DHAS_CANAL",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q5ALM0\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:31:05.955388+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f",
  "url": "https://rest.uniprot.org/uniprotkb/Q5ALM0.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":147,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2005-04-26\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:31:05.955388+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f",
  "url": "https://rest.uniprot.org/uniprotkb/Q5ALM0.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Yeast\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000559\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Saccharomycotina\",\"Pichiomycetes\",\"Debaryomycetaceae\",\"Candida/Lodderomyces clade\",\"Candida\"],\"scientificName\":\"Candida albicans (strain SC5314 / ATCC MYA-2876)\",\"taxonId\":237561}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:31:05.955388+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f",
  "url": "https://rest.uniprot.org/uniprotkb/Q5ALM0.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"17419877\",\"source\":\"PubMed\"}],\"value\":\"CaASADH\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20124701\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29608391\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"32383780\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"34469014\",\"source\":\"PubMed\"}],\"value\":\"1.2.1.11\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Aspartate-semialdehyde dehydrogenase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:31:05.955388+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f",
  "url": "https://rest.uniprot.org/uniprotkb/Q5ALM0.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Acyl-thioester intermediate\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PIRSR000148-1\",\"source\":\"PIRSR\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":156},\"start\":{\"modifier\":\"EXACT\",\"value\":156}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:31:05.955388+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f",
  "url": "https://rest.uniprot.org/uniprotkb/Q5ALM0.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Proton acceptor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PIRSR000148-1\",\"source\":\"PIRSR\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":256},\"start\":{\"modifier\":\"EXACT\",\"value\":256}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:31:05.955388+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f",
  "url": "https://rest.uniprot.org/uniprotkb/Q5ALM0.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24025428\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"3HSK\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":12},\"start\":{\"modifier\":\"EXACT\",\"value\":12}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:31:05.955388+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f",
  "url": "https://rest.uniprot.org/uniprotkb/Q5ALM0.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24025428\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"3HSK\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":13},\"start\":{\"modifier\":\"EXACT\",\"value\":13}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:31:05.955388+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f",
  "url": "https://rest.uniprot.org/uniprotkb/Q5ALM0.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24025428\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"3HSK\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":14},\"start\":{\"modifier\":\"EXACT\",\"value\":14}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:31:05.955388+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f",
  "url": "https://rest.uniprot.org/uniprotkb/Q5ALM0.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A179UL48\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":15},\"start\":{\"modifier\":\"EXACT\",\"value\":15}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:31:05.955388+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f",
  "url": "https://rest.uniprot.org/uniprotkb/Q5ALM0.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24025428\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"3HSK\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":37},\"start\":{\"modifier\":\"EXACT\",\"value\":37}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:31:05.955388+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f",
  "url": "https://rest.uniprot.org/uniprotkb/Q5ALM0.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24025428\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"3HSK\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":40},\"start\":{\"modifier\":\"EXACT\",\"value\":40}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:31:05.955388+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f",
  "url": "https://rest.uniprot.org/uniprotkb/Q5ALM0.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A080WMA9\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":85},\"start\":{\"modifier\":\"EXACT\",\"value\":85}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-02T04:31:05.955388+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f",
  "url": "https://rest.uniprot.org/uniprotkb/Q5ALM0.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A080WMA9\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":86},\"start\":{\"modifier\":\"EXACT\",\"value\":86}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-02T04:31:05.955388+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f",
  "url": "https://rest.uniprot.org/uniprotkb/Q5ALM0.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A080WMA9\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":188},\"start\":{\"modifier\":\"EXACT\",\"value\":188}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/11",
  "retrieved_utc": "2026-11-02T04:31:05.955388+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f",
  "url": "https://rest.uniprot.org/uniprotkb/Q5ALM0.json"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)

```json
{
  "evidence_id": "C16",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A179UL48\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":343},\"start\":{\"modifier\":\"EXACT\",\"value\":343}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/12",
  "retrieved_utc": "2026-11-02T04:31:05.955388+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f",
  "url": "https://rest.uniprot.org/uniprotkb/Q5ALM0.json"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)

```json
{
  "evidence_id": "C17",
  "excerpt": "{\"citation\":{\"authors\":[\"van het Hoog M.\",\"Rast T.J.\",\"Martchenko M.\",\"Grindle S.\",\"Dignard D.\",\"Hogues H.\",\"Cuomo C.\",\"Berriman M.\",\"Scherer S.\",\"Magee B.B.\",\"Whiteway M.\",\"Chibana H.\",\"Nantel A.\",\"Magee P.T.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"17419877\"},{\"database\":\"DOI\",\"id\":\"10.1186/gb-2007-8-4-r52\"}],\"citationType\":\"journal article\",\"firstPage\":\"RESEARCH52.1\",\"id\":\"17419877\",\"journal\":\"Genome Biol.\",\"lastPage\":\"RESEARCH52.12\",\"publicationDate\":\"2007\",\"title\":\"Assembly of the Candida albicans genome into sixteen supercontigs aligned on the eight chromosomes.\",\"volume\":\"8\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000559\",\"source\":\"Proteomes\"}],\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000559\",\"source\":\"Proteomes\"}],\"type\":\"STRAIN\",\"value\":\"SC5314 / ATCC MYA-2876\"}],\"referenceNumber\":2,\"referencePositions\":[\"GENOME REANNOTATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:31:05.955388+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f",
  "url": "https://rest.uniprot.org/uniprotkb/Q5ALM0.json"
}
```

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)

```json
{
  "evidence_id": "C18",
  "excerpt": "{\"citation\":{\"authors\":[\"Muzzey D.\",\"Schwartz K.\",\"Weissman J.S.\",\"Sherlock G.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"24025428\"},{\"database\":\"DOI\",\"id\":\"10.1186/gb-2013-14-9-r97\"}],\"citationType\":\"journal article\",\"firstPage\":\"RESEARCH97.1\",\"id\":\"24025428\",\"journal\":\"Genome Biol.\",\"lastPage\":\"RESEARCH97.14\",\"publicationDate\":\"2013\",\"title\":\"Assembly of a phased diploid Candida albicans genome facilitates allele-specific measurements and provides a simple model for repeat and indel structure.\",\"volume\":\"14\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000559\",\"source\":\"Proteomes\"}],\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000559\",\"source\":\"Proteomes\"}],\"type\":\"STRAIN\",\"value\":\"SC5314 / ATCC MYA-2876\"}],\"referenceNumber\":3,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [LARGE SCALE GENOMIC DNA]\",\"GENOME REANNOTATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:31:05.955388+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f",
  "url": "https://rest.uniprot.org/uniprotkb/Q5ALM0.json"
}
```

### Evidence C19

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)

```json
{
  "evidence_id": "C19",
  "excerpt": "{\"citation\":{\"authors\":[\"Dahal G.P.\",\"Viola R.E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"29608391\"},{\"database\":\"DOI\",\"id\":\"10.1177/2472555218767844\"}],\"citationType\":\"journal article\",\"firstPage\":\"520\",\"id\":\"29608391\",\"journal\":\"SLAS Discovery\",\"lastPage\":\"531\",\"publicationDate\":\"2018\",\"title\":\"A Fragment Library Screening Approach to Identify Selective Inhibitors against an Essential Fungal Enzyme.\",\"volume\":\"23\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":5,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-02T04:31:05.955388+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f",
  "url": "https://rest.uniprot.org/uniprotkb/Q5ALM0.json"
}
```

### Evidence C20

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)

```json
{
  "evidence_id": "C20",
  "excerpt": "{\"citation\":{\"authors\":[\"Dahal G.P.\",\"Launder D.\",\"McKeone K.M.M.\",\"Hunter J.P.\",\"Conti H.R.\",\"Viola R.E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"32383780\"},{\"database\":\"DOI\",\"id\":\"10.1002/ddr.21682\"}],\"citationType\":\"journal article\",\"firstPage\":\"736\",\"id\":\"32383780\",\"journal\":\"Drug Dev. Res.\",\"lastPage\":\"744\",\"publicationDate\":\"2020\",\"title\":\"Aspartate semialdehyde dehydrogenase inhibition suppresses the growth of the pathogenic fungus Candida albicans.\",\"volume\":\"81\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":6,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/5",
  "retrieved_utc": "2026-11-02T04:31:05.955388+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f",
  "url": "https://rest.uniprot.org/uniprotkb/Q5ALM0.json"
}
```

### Evidence C21

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)

```json
{
  "evidence_id": "C21",
  "excerpt": "{\"citation\":{\"authors\":[\"Friday S.N.\",\"Cheng D.W.\",\"Zagler S.G.\",\"Zanella B.S.\",\"Dietz J.D.\",\"Calbat C.N.\",\"Roach L.T.\",\"Bagnal C.\",\"Faile I.S.\",\"Halkides C.J.\",\"Viola R.E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"34469014\"},{\"database\":\"DOI\",\"id\":\"10.1002/ddr.21875\"}],\"citationType\":\"journal article\",\"firstPage\":\"447\",\"id\":\"34469014\",\"journal\":\"Drug Dev. Res.\",\"lastPage\":\"460\",\"publicationDate\":\"2022\",\"title\":\"Design and testing of selective inactivators against an antifungal enzyme target.\",\"volume\":\"83\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":7,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/6",
  "retrieved_utc": "2026-11-02T04:31:05.955388+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f",
  "url": "https://rest.uniprot.org/uniprotkb/Q5ALM0.json"
}
```

### Evidence C22

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)

```json
{
  "evidence_id": "C22",
  "excerpt": "{\"citation\":{\"authors\":[\"Arachea B.T.\",\"Liu X.\",\"Pavlovsky A.G.\",\"Viola R.E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"20124701\"},{\"database\":\"DOI\",\"id\":\"10.1107/s0907444909052834\"}],\"citationType\":\"journal article\",\"firstPage\":\"205\",\"id\":\"20124701\",\"journal\":\"Acta Crystallogr. D\",\"lastPage\":\"212\",\"publicationDate\":\"2010\",\"title\":\"Expansion of the aspartate beta-semialdehyde dehydrogenase family: the first structure of a fungal ortholog.\",\"volume\":\"66\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"3HSK\",\"source\":\"PDB\"}],\"referenceNumber\":8,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.20 ANGSTROMS) IN COMPLEX WITH NADP(+)\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/7",
  "retrieved_utc": "2026-11-02T04:31:05.955388+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f",
  "url": "https://rest.uniprot.org/uniprotkb/Q5ALM0.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)

```json
{
  "entry_version": 145,
  "evidence_id": "H1",
  "excerpt": "ID   DHAS_CANAL              Reviewed;         365 AA.\nAC   Q5ALM0;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   26-APR-2005, sequence version 1.\nDT   18-JUN-2025, entry version 145.\nDE   RecName: Full=Aspartate-semialdehyde dehydrogenase {ECO:0000305};\nDE            EC=1.2.1.11 {ECO:0000269|PubMed:20124701, ECO:0000269|PubMed:29608391, ECO:0000269|PubMed:32383780, ECO:0000269|PubMed:34469014};\nDE   AltName: Full=CaASADH {ECO:0000303|PubMed:17419877};\nGN   Name=HOM2 {ECO:0000303|PubMed:17419877};\nGN   OrderedLocusNames=CAALFM_C202370CA {ECO:0000312|EMBL:AOW27277.1},\nGN   orf19.9132 {ECO:0000312|CGD:CAL0000179646};\nOS   Candida albicans (strain SC5314 / ATCC MYA-2876) (Yeast).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Saccharomycotina; Pichiomycetes;\nOC   Debaryomycetaceae; Candida/Lodderomyces clade; Candida.\nOX   NCBI_TaxID=237561 {ECO:0000312|Proteomes:UP000000559};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:09.278811+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d",
  "url": "https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)

```json
{
  "entry_version": 145,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000312|Proteomes:UP000000559}\nRP   GENOME REANNOTATION.\nRC   STRAIN=SC5314 / ATCC MYA-2876 {ECO:0000312|Proteomes:UP000000559};\nRX   PubMed=17419877; DOI=10.1186/gb-2007-8-4-r52;\nRA   van het Hoog M., Rast T.J., Martchenko M., Grindle S., Dignard D.,\nRA   Hogues H., Cuomo C., Berriman M., Scherer S., Magee B.B., Whiteway M.,\nRA   Chibana H., Nantel A., Magee P.T.;\nRT   \"Assembly of the Candida albicans genome into sixteen supercontigs aligned\nRT   on the eight chromosomes.\";\nRL   Genome Biol. 8:RESEARCH52.1-RESEARCH52.12(2007).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:09.278811+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 25-34",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d",
  "url": "https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)

```json
{
  "entry_version": 145,
  "evidence_id": "H3",
  "excerpt": "RN   [3] {ECO:0000312|Proteomes:UP000000559}\nRP   NUCLEOTIDE SEQUENCE [LARGE SCALE GENOMIC DNA], AND GENOME REANNOTATION.\nRC   STRAIN=SC5314 / ATCC MYA-2876 {ECO:0000312|Proteomes:UP000000559};\nRX   PubMed=24025428; DOI=10.1186/gb-2013-14-9-r97;\nRA   Muzzey D., Schwartz K., Weissman J.S., Sherlock G.;\nRT   \"Assembly of a phased diploid Candida albicans genome facilitates allele-\nRT   specific measurements and provides a simple model for repeat and indel\nRT   structure.\";\nRL   Genome Biol. 14:RESEARCH97.1-RESEARCH97.14(2013).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:09.278811+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 35-43",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d",
  "url": "https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)

```json
{
  "entry_version": 145,
  "evidence_id": "H4",
  "excerpt": "RN   [5] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, AND ACTIVITY REGULATION.\nRX   PubMed=29608391; DOI=10.1177/2472555218767844;\nRA   Dahal G.P., Viola R.E.;\nRT   \"A Fragment Library Screening Approach to Identify Selective Inhibitors\nRT   against an Essential Fungal Enzyme.\";\nRL   SLAS Discovery 23:520-531(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:09.278811+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 51-57",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d",
  "url": "https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)

```json
{
  "entry_version": 145,
  "evidence_id": "H5",
  "excerpt": "RN   [6] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, AND DISRUPTION\nRP   PHENOTYPE.\nRX   PubMed=32383780; DOI=10.1002/ddr.21682;\nRA   Dahal G.P., Launder D., McKeone K.M.M., Hunter J.P., Conti H.R.,\nRA   Viola R.E.;\nRT   \"Aspartate semialdehyde dehydrogenase inhibition suppresses the growth of\nRT   the pathogenic fungus Candida albicans.\";\nRL   Drug Dev. Res. 81:736-744(2020).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:09.278811+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 58-66",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d",
  "url": "https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)

```json
{
  "entry_version": 145,
  "evidence_id": "H6",
  "excerpt": "RN   [7] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, AND ACTIVITY REGULATION.\nRX   PubMed=34469014; DOI=10.1002/ddr.21875;\nRA   Friday S.N., Cheng D.W., Zagler S.G., Zanella B.S., Dietz J.D.,\nRA   Calbat C.N., Roach L.T., Bagnal C., Faile I.S., Halkides C.J., Viola R.E.;\nRT   \"Design and testing of selective inactivators against an antifungal enzyme\nRT   target.\";\nRL   Drug Dev. Res. 83:447-460(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:09.278811+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 67-74",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d",
  "url": "https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)

```json
{
  "entry_version": 145,
  "evidence_id": "H7",
  "excerpt": "RN   [8] {ECO:0007744|PDB:3HSK}\nRP   X-RAY CRYSTALLOGRAPHY (2.20 ANGSTROMS) IN COMPLEX WITH NADP(+), FUNCTION,\nRP   CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, AND SUBUNIT.\nRX   PubMed=20124701; DOI=10.1107/s0907444909052834;\nRA   Arachea B.T., Liu X., Pavlovsky A.G., Viola R.E.;\nRT   \"Expansion of the aspartate beta-semialdehyde dehydrogenase family: the\nRT   first structure of a fungal ortholog.\";\nRL   Acta Crystallogr. D 66:205-212(2010).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:09.278811+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 75-82",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d",
  "url": "https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)

```json
{
  "entry_version": 145,
  "evidence_id": "H8",
  "excerpt": "FT   ACT_SITE        156\nFT                   /note=\"Acyl-thioester intermediate\"\nFT                   /evidence=\"ECO:0000255|PIRSR:PIRSR000148-1\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:09.278811+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 194-196",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d",
  "url": "https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)

```json
{
  "entry_version": 145,
  "evidence_id": "H9",
  "excerpt": "FT   ACT_SITE        256\nFT                   /note=\"Proton acceptor\"\nFT                   /evidence=\"ECO:0000255|PIRSR:PIRSR000148-1\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:09.278811+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 197-199",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d",
  "url": "https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)

```json
{
  "entry_version": 145,
  "evidence_id": "H10",
  "excerpt": "FT   BINDING         12\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000269|PubMed:24025428,\nFT                   ECO:0007744|PDB:3HSK\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:09.278811+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 200-204",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d",
  "url": "https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)

```json
{
  "entry_version": 145,
  "evidence_id": "H11",
  "excerpt": "FT   BINDING         13\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000269|PubMed:24025428,\nFT                   ECO:0007744|PDB:3HSK\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:09.278811+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 205-209",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d",
  "url": "https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)

```json
{
  "entry_version": 145,
  "evidence_id": "H12",
  "excerpt": "FT   BINDING         14\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000269|PubMed:24025428,\nFT                   ECO:0007744|PDB:3HSK\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:09.278811+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 210-214",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d",
  "url": "https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)

```json
{
  "entry_version": 145,
  "evidence_id": "H13",
  "excerpt": "FT   BINDING         15\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:A0A179UL48\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:09.278811+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 215-218",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d",
  "url": "https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)

```json
{
  "entry_version": 145,
  "evidence_id": "H14",
  "excerpt": "FT   BINDING         37\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000269|PubMed:24025428,\nFT                   ECO:0007744|PDB:3HSK\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:09.278811+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 219-223",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d",
  "url": "https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145"
}
```

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)

```json
{
  "entry_version": 145,
  "evidence_id": "H15",
  "excerpt": "FT   BINDING         40\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000269|PubMed:24025428,\nFT                   ECO:0007744|PDB:3HSK\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:09.278811+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 224-228",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d",
  "url": "https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145"
}
```

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)

```json
{
  "entry_version": 145,
  "evidence_id": "H16",
  "excerpt": "FT   BINDING         85\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:A0A080WMA9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:09.278811+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 229-232",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d",
  "url": "https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145"
}
```

### Evidence H17

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)

```json
{
  "entry_version": 145,
  "evidence_id": "H17",
  "excerpt": "FT   BINDING         86\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:A0A080WMA9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:09.278811+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 233-236",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d",
  "url": "https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145"
}
```

### Evidence H18

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)

```json
{
  "entry_version": 145,
  "evidence_id": "H18",
  "excerpt": "FT   BINDING         188\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:A0A080WMA9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:09.278811+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 237-240",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d",
  "url": "https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145"
}
```

### Evidence H19

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)

```json
{
  "entry_version": 145,
  "evidence_id": "H19",
  "excerpt": "FT   BINDING         343\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:A0A179UL48\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:09.278811+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 241-244",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d",
  "url": "https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 127. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
