# motif_position_0044

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/motif_position_0044.txt)

**Task:** `motif_position`  
**Expected answer:** **C** — 216..220

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MADSNLNEPVIIQATRLDTSILPRNIFSQSYLLYVIAQGTDVGNVANKANEAGQGAYDAQVKNDEQDVELADHDARIAANTKAINILEVRLTTAEGKIVVLRSDVDYLLDEVIDIQAHLVTVDQRLDGVESDVSDIKSDYVSKTVTESQSLASPLDVKTSYSVDGIQVVGARQTGWTAATGTPLLGSFNANQSYTVGTTYTQSEVAALATGLEQARQRILALETALRLHGLID

[Multiple Choices]
A. 128..147
B. 380..383
C. 216..220
D. 184..247
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

> The sequence-matched UniProt entry annotates a basic-cluster motif at 216..220, supporting choice C. This annotation is transferred by similarity from another protein, not direct experimental evidence for this protein.

Citations as saved: [C18](#evidence-c18).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 216..220 segment is RQRIL, a short region containing two arginines and thus a plausible basic motif. Among the choices, A is a longer mixed/acidic segment, B lies outside the 233-residue sequence, and D is an unusually broad interval. General knowledge that short basic clusters can function as motifs makes C a meaningful, though not certain, inference.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The prompt does not name the motif, which limits certainty, but the sequence composition and candidate intervals provide a transferable basis for favoring the short basic segment at C.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The motif is not explicitly identified, but the offered alternatives make C the plausible short basic motif; no other listed interval is comparably supported.


### Important caveats

- The supporting annotation is similarity-based and does not establish direct experimental validation of this motif in the supplied protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 216..220 segment is RQRIL, a short region containing two arginines and thus a plausible basic motif. Among the choices, A is a longer mixed/acidic segment, B lies outside the 233-residue sequence, and D is an unusually broad interval. General knowledge that short basic clusters can function as motifs makes C a meaningful, though not certain, inference.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The prompt does not name the motif, which limits certainty, but the sequence composition and candidate intervals provide a transferable basis for favoring the short basic segment at C."
  },
  "case_id": "motif_position_0044",
  "expected_answer_check": {
    "evidence_ids": [
      "C18"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates a basic-cluster motif at 216..220, supporting choice C. This annotation is transferred by similarity from another protein, not direct experimental evidence for this protein."
  },
  "important_caveats": [
    "The supporting annotation is similarity-based and does not establish direct experimental validation of this motif in the supplied protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The motif is not explicitly identified, but the offered alternatives make C the plausible short basic motif; no other listed interval is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "motif_position_0044",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates a basic-cluster motif at 216..220, supporting choice C. This annotation is transferred by similarity from another protein, not direct experimental evidence for this protein.",
    "evidence_ids": ["C18"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 216..220 segment is RQRIL, a short region containing two arginines and thus a plausible basic motif. Among the choices, A is a longer mixed/acidic segment, B lies outside the 233-residue sequence, and D is an unusually broad interval. General knowledge that short basic clusters can function as motifs makes C a meaningful, though not certain, inference.",
    "missing_item_specific_fact": "",
    "reason": "The prompt does not name the motif, which limits certainty, but the sequence composition and candidate intervals provide a transferable basis for favoring the short basic segment at C."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The motif is not explicitly identified, but the offered alternatives make C the plausible short basic motif; no other listed interval is comparably supported."
  },
  "important_caveats": [
    "The supporting annotation is similarity-based and does not establish direct experimental validation of this motif in the supplied protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for Q9AYZ3 records a 'Basic cluster' motif at positions 216..220 (evidence C18/H16), matching the expected answer C exactly. The annotation is type 'Motif' with evidence code ECO:0000250 (transferred by similarity to P35837, P22 gp26). The sequence at positions 216-220 is RQRIL, which contains two arginines consistent with a basic cluster. The annotation is computationally transferred rather than experimentally verified for this specific protein, but it is the recorded database entry that the question targets.

Citations as saved: [C18](#evidence-c18), [H16](#evidence-h16).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Options B (380..383) and D (184..247) are immediately eliminated because the protein is only 233 residues long, making those positions physically impossible. Between A (128..147, 20 residues) and C (216..220, 5 residues): (1) The task definition states a motif is 'a short, recurring pattern.' A 20-residue span is more characteristic of a domain or region than a motif, whereas a 5-residue span fits the standard motif definition. (2) In phage tail needle proteins (the family including P22 gp26 and HK620 gp26), a conserved basic cluster at the C-terminal tip of the inverted coiled coil is a well-known functional feature involved in host interaction or DNA packaging. The sequence at 216-220 (RQRIL) shows a concentration of basic residues (R, R) at the C-terminal end of the inverted coiled coil (annotated region 175-233), consistent with this family-level pattern. (3) The 128-147 region lies within the trimerization coiled coil (heptad repeats span 61-139) and shows no distinctive short motif pattern—it is a continuation of the helical coiled coil with scattered acidic residues. Thus, family knowledge of tail needle proteins plus the motif-length criterion distinguishes C from A.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can eliminate B and D by sequence length, apply the 'short pattern' motif definition to disfavour the 20-residue option A, and use family-level knowledge of phage tail needle proteins (basic cluster at the C-terminal tip) to identify C. The sequence itself (RQRIL at 216-220) visibly shows the basic residue concentration. This is a defensible probabilistic inference from transferable knowledge, not requiring memorization of this exact protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B and D are physically impossible (beyond the 233-aa sequence). Option A (20 residues) conflicts with the stated definition of a motif as 'short.' Option C (5 residues, basic cluster at C-terminal tip) is the only choice consistent with both the motif length definition and the known family-level feature of tail needle proteins. No genuine ambiguity among the offered alternatives.


### Important caveats

- The 'Basic cluster' annotation at 216..220 is transferred by similarity to P35837 (P22 gp26) with evidence code ECO:0000250; it has not been independently experimentally validated for HK620 gp26 specifically.
- The question does not specify which motif to identify; the answer relies on recognizing that only one option qualifies as a 'short motif' with a recognizable pattern.
- The reviewer-only evidence confirms sequence match (233 aa, SHA256 identical) between the benchmark sequence and the UniProt entry.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Options B (380..383) and D (184..247) are immediately eliminated because the protein is only 233 residues long, making those positions physically impossible. Between A (128..147, 20 residues) and C (216..220, 5 residues): (1) The task definition states a motif is 'a short, recurring pattern.' A 20-residue span is more characteristic of a domain or region than a motif, whereas a 5-residue span fits the standard motif definition. (2) In phage tail needle proteins (the family including P22 gp26 and HK620 gp26), a conserved basic cluster at the C-terminal tip of the inverted coiled coil is a well-known functional feature involved in host interaction or DNA packaging. The sequence at 216-220 (RQRIL) shows a concentration of basic residues (R, R) at the C-terminal end of the inverted coiled coil (annotated region 175-233), consistent with this family-level pattern. (3) The 128-147 region lies within the trimerization coiled coil (heptad repeats span 61-139) and shows no distinctive short motif pattern—it is a continuation of the helical coiled coil with scattered acidic residues. Thus, family knowledge of tail needle proteins plus the motif-length criterion distinguishes C from A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate B and D by sequence length, apply the 'short pattern' motif definition to disfavour the 20-residue option A, and use family-level knowledge of phage tail needle proteins (basic cluster at the C-terminal tip) to identify C. The sequence itself (RQRIL at 216-220) visibly shows the basic residue concentration. This is a defensible probabilistic inference from transferable knowledge, not requiring memorization of this exact protein's annotation."
  },
  "case_id": "motif_position_0044",
  "expected_answer_check": {
    "evidence_ids": [
      "C18",
      "H16"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for Q9AYZ3 records a 'Basic cluster' motif at positions 216..220 (evidence C18/H16), matching the expected answer C exactly. The annotation is type 'Motif' with evidence code ECO:0000250 (transferred by similarity to P35837, P22 gp26). The sequence at positions 216-220 is RQRIL, which contains two arginines consistent with a basic cluster. The annotation is computationally transferred rather than experimentally verified for this specific protein, but it is the recorded database entry that the question targets."
  },
  "important_caveats": [
    "The 'Basic cluster' annotation at 216..220 is transferred by similarity to P35837 (P22 gp26) with evidence code ECO:0000250; it has not been independently experimentally validated for HK620 gp26 specifically.",
    "The question does not specify which motif to identify; the answer relies on recognizing that only one option qualifies as a 'short motif' with a recognizable pattern.",
    "The reviewer-only evidence confirms sequence match (233 aa, SHA256 identical) between the benchmark sequence and the UniProt entry."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and D are physically impossible (beyond the 233-aa sequence). Option A (20 residues) conflicts with the stated definition of a motif as 'short.' Option C (5 residues, basic cluster at C-terminal tip) is the only choice consistent with both the motif length definition and the known family-level feature of tail needle proteins. No genuine ambiguity among the offered alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "motif_position_0044",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for Q9AYZ3 records a 'Basic cluster' motif at positions 216..220 (evidence C18/H16), matching the expected answer C exactly. The annotation is type 'Motif' with evidence code ECO:0000250 (transferred by similarity to P35837, P22 gp26). The sequence at positions 216-220 is RQRIL, which contains two arginines consistent with a basic cluster. The annotation is computationally transferred rather than experimentally verified for this specific protein, but it is the recorded database entry that the question targets.",
    "evidence_ids": ["C18", "H16"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Options B (380..383) and D (184..247) are immediately eliminated because the protein is only 233 residues long, making those positions physically impossible. Between A (128..147, 20 residues) and C (216..220, 5 residues): (1) The task definition states a motif is 'a short, recurring pattern.' A 20-residue span is more characteristic of a domain or region than a motif, whereas a 5-residue span fits the standard motif definition. (2) In phage tail needle proteins (the family including P22 gp26 and HK620 gp26), a conserved basic cluster at the C-terminal tip of the inverted coiled coil is a well-known functional feature involved in host interaction or DNA packaging. The sequence at 216-220 (RQRIL) shows a concentration of basic residues (R, R) at the C-terminal end of the inverted coiled coil (annotated region 175-233), consistent with this family-level pattern. (3) The 128-147 region lies within the trimerization coiled coil (heptad repeats span 61-139) and shows no distinctive short motif pattern—it is a continuation of the helical coiled coil with scattered acidic residues. Thus, family knowledge of tail needle proteins plus the motif-length criterion distinguishes C from A.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate B and D by sequence length, apply the 'short pattern' motif definition to disfavour the 20-residue option A, and use family-level knowledge of phage tail needle proteins (basic cluster at the C-terminal tip) to identify C. The sequence itself (RQRIL at 216-220) visibly shows the basic residue concentration. This is a defensible probabilistic inference from transferable knowledge, not requiring memorization of this exact protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and D are physically impossible (beyond the 233-aa sequence). Option A (20 residues) conflicts with the stated definition of a motif as 'short.' Option C (5 residues, basic cluster at C-terminal tip) is the only choice consistent with both the motif length definition and the known family-level feature of tail needle proteins. No genuine ambiguity among the offered alternatives."
  },
  "important_caveats": [
    "The 'Basic cluster' annotation at 216..220 is transferred by similarity to P35837 (P22 gp26) with evidence code ECO:0000250; it has not been independently experimentally validated for HK620 gp26 specifically.",
    "The question does not specify which motif to identify; the answer relies on recognizing that only one option qualifies as a 'short motif' with a recognizable pattern.",
    "The reviewer-only evidence confirms sequence match (233 aa, SHA256 identical) between the benchmark sequence and the UniProt entry."
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
  "benchmark_sequence_length": 233,
  "benchmark_sequence_sha256": "78db8ada1420f81704a86e1f73974048e944125986dc900a91e5f22c32a6fa6c",
  "current_entry_audit": {
    "entryVersion": 84,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2001-06-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "fb98ac90c263a168880dbbd0ac49fe332e0529f262c4f40ba939c785038eda08",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 233,
  "current_source_sequence_sha256": "78db8ada1420f81704a86e1f73974048e944125986dc900a91e5f22c32a6fa6c",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 83,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9AYZ3",
  "selected_historical_entry_version": 83,
  "selected_historical_record_sha256": "0f5b04df4f6c180ff20dad87e3929d5b22b173869433f4330e3aceb11b69188b",
  "selected_historical_source_sequence_length": 233,
  "selected_historical_source_sequence_sha256": "78db8ada1420f81704a86e1f73974048e944125986dc900a91e5f22c32a6fa6c",
  "selected_historical_version": {
    "accession": "Q9AYZ3",
    "database": "Swiss-Prot",
    "entryVersion": 83,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "NEEDL_BPHK6",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9AYZ3.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9AYZ3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:32:41.135549+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fb98ac90c263a168880dbbd0ac49fe332e0529f262c4f40ba939c785038eda08",
  "url": "https://rest.uniprot.org/uniprotkb/Q9AYZ3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9AYZ3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":84,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2001-06-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:32:41.135549+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fb98ac90c263a168880dbbd0ac49fe332e0529f262c4f40ba939c785038eda08",
  "url": "https://rest.uniprot.org/uniprotkb/Q9AYZ3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9AYZ3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Bacteriophage HK620\",\"lineage\":[\"Viruses\",\"Duplodnaviria\",\"Heunggongvirae\",\"Uroviricota\",\"Caudoviricetes\",\"Caudoviricetes incertae sedis\",\"Lederbergvirus\",\"Lederbergvirus HK620\"],\"scientificName\":\"Enterobacteria phage HK620\",\"taxonId\":155148}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:32:41.135549+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fb98ac90c263a168880dbbd0ac49fe332e0529f262c4f40ba939c785038eda08",
  "url": "https://rest.uniprot.org/uniprotkb/Q9AYZ3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9AYZ3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"value\":\"Head completion protein\"}},{\"fullName\":{\"value\":\"Packaged DNA stabilization protein\"}},{\"fullName\":{\"value\":\"Tail accessory factor gp26\"}}],\"recommendedName\":{\"fullName\":{\"value\":\"Tail needle protein gp26\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:32:41.135549+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fb98ac90c263a168880dbbd0ac49fe332e0529f262c4f40ba939c785038eda08",
  "url": "https://rest.uniprot.org/uniprotkb/Q9AYZ3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9AYZ3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Trimerization heptad repeat 1\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P35837\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":67},\"start\":{\"modifier\":\"EXACT\",\"value\":61}},\"type\":\"Repeat\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:32:41.135549+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fb98ac90c263a168880dbbd0ac49fe332e0529f262c4f40ba939c785038eda08",
  "url": "https://rest.uniprot.org/uniprotkb/Q9AYZ3.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9AYZ3.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Trimerization heptad repeat 2\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P35837\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":76},\"start\":{\"modifier\":\"EXACT\",\"value\":70}},\"type\":\"Repeat\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:32:41.135549+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fb98ac90c263a168880dbbd0ac49fe332e0529f262c4f40ba939c785038eda08",
  "url": "https://rest.uniprot.org/uniprotkb/Q9AYZ3.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9AYZ3.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Trimerization heptad repeat 3\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P35837\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":83},\"start\":{\"modifier\":\"EXACT\",\"value\":77}},\"type\":\"Repeat\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:32:41.135549+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fb98ac90c263a168880dbbd0ac49fe332e0529f262c4f40ba939c785038eda08",
  "url": "https://rest.uniprot.org/uniprotkb/Q9AYZ3.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9AYZ3.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Trimerization heptad repeat 4\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P35837\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":90},\"start\":{\"modifier\":\"EXACT\",\"value\":84}},\"type\":\"Repeat\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:32:41.135549+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fb98ac90c263a168880dbbd0ac49fe332e0529f262c4f40ba939c785038eda08",
  "url": "https://rest.uniprot.org/uniprotkb/Q9AYZ3.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9AYZ3.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Trimerization heptad repeat 5\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P35837\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":97},\"start\":{\"modifier\":\"EXACT\",\"value\":91}},\"type\":\"Repeat\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:32:41.135549+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fb98ac90c263a168880dbbd0ac49fe332e0529f262c4f40ba939c785038eda08",
  "url": "https://rest.uniprot.org/uniprotkb/Q9AYZ3.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9AYZ3.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"Trimerization heptad repeat 6\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P35837\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":104},\"start\":{\"modifier\":\"EXACT\",\"value\":98}},\"type\":\"Repeat\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:32:41.135549+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fb98ac90c263a168880dbbd0ac49fe332e0529f262c4f40ba939c785038eda08",
  "url": "https://rest.uniprot.org/uniprotkb/Q9AYZ3.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9AYZ3.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"Trimerization heptad repeat 7\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P35837\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":111},\"start\":{\"modifier\":\"EXACT\",\"value\":105}},\"type\":\"Repeat\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:32:41.135549+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fb98ac90c263a168880dbbd0ac49fe332e0529f262c4f40ba939c785038eda08",
  "url": "https://rest.uniprot.org/uniprotkb/Q9AYZ3.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9AYZ3.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"Trimerization heptad repeat 8\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P35837\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":118},\"start\":{\"modifier\":\"EXACT\",\"value\":112}},\"type\":\"Repeat\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:32:41.135549+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fb98ac90c263a168880dbbd0ac49fe332e0529f262c4f40ba939c785038eda08",
  "url": "https://rest.uniprot.org/uniprotkb/Q9AYZ3.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9AYZ3.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"Trimerization heptad repeat 9\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P35837\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":125},\"start\":{\"modifier\":\"EXACT\",\"value\":119}},\"type\":\"Repeat\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-02T04:32:41.135549+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fb98ac90c263a168880dbbd0ac49fe332e0529f262c4f40ba939c785038eda08",
  "url": "https://rest.uniprot.org/uniprotkb/Q9AYZ3.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9AYZ3.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"description\":\"Trimerization heptad repeat 10\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P35837\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":132},\"start\":{\"modifier\":\"EXACT\",\"value\":126}},\"type\":\"Repeat\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-02T04:32:41.135549+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fb98ac90c263a168880dbbd0ac49fe332e0529f262c4f40ba939c785038eda08",
  "url": "https://rest.uniprot.org/uniprotkb/Q9AYZ3.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9AYZ3.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"description\":\"Trimerization heptad repeat 11\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P35837\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":139},\"start\":{\"modifier\":\"EXACT\",\"value\":133}},\"type\":\"Repeat\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/11",
  "retrieved_utc": "2026-11-02T04:32:41.135549+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fb98ac90c263a168880dbbd0ac49fe332e0529f262c4f40ba939c785038eda08",
  "url": "https://rest.uniprot.org/uniprotkb/Q9AYZ3.json"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9AYZ3.json)

```json
{
  "evidence_id": "C16",
  "excerpt": "{\"description\":\"Interaction with tail hub protein\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P35837\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":50},\"start\":{\"modifier\":\"EXACT\",\"value\":2}},\"type\":\"Region\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/12",
  "retrieved_utc": "2026-11-02T04:32:41.135549+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fb98ac90c263a168880dbbd0ac49fe332e0529f262c4f40ba939c785038eda08",
  "url": "https://rest.uniprot.org/uniprotkb/Q9AYZ3.json"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9AYZ3.json)

```json
{
  "evidence_id": "C17",
  "excerpt": "{\"description\":\"Inverted coiled coil\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"19482036\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":233},\"start\":{\"modifier\":\"EXACT\",\"value\":175}},\"type\":\"Region\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/13",
  "retrieved_utc": "2026-11-02T04:32:41.135549+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fb98ac90c263a168880dbbd0ac49fe332e0529f262c4f40ba939c785038eda08",
  "url": "https://rest.uniprot.org/uniprotkb/Q9AYZ3.json"
}
```

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9AYZ3.json)

```json
{
  "evidence_id": "C18",
  "excerpt": "{\"description\":\"Basic cluster\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P35837\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":220},\"start\":{\"modifier\":\"EXACT\",\"value\":216}},\"type\":\"Motif\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/15",
  "retrieved_utc": "2026-11-02T04:32:41.135549+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fb98ac90c263a168880dbbd0ac49fe332e0529f262c4f40ba939c785038eda08",
  "url": "https://rest.uniprot.org/uniprotkb/Q9AYZ3.json"
}
```

### Evidence C19

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9AYZ3.json)

```json
{
  "evidence_id": "C19",
  "excerpt": "{\"citation\":{\"authors\":[\"Bhardwaj A.\",\"Walker-Kopp N.\",\"Casjens S.R.\",\"Cingolani G.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"19482036\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.jmb.2009.05.069\"}],\"citationType\":\"journal article\",\"firstPage\":\"227\",\"id\":\"19482036\",\"journal\":\"J. Mol. Biol.\",\"lastPage\":\"245\",\"publicationDate\":\"2009\",\"title\":\"An evolutionarily conserved family of virion tail needles related to bacteriophage P22 gp26: correlation between structural stability and length of the alpha-helical trimeric coiled coil.\",\"volume\":\"391\"},\"referenceNumber\":2,\"referencePositions\":[\"DOMAIN\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:32:41.135549+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fb98ac90c263a168880dbbd0ac49fe332e0529f262c4f40ba939c785038eda08",
  "url": "https://rest.uniprot.org/uniprotkb/Q9AYZ3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9AYZ3?format=txt&versions=83)

```json
{
  "entry_version": 83,
  "evidence_id": "H1",
  "excerpt": "ID   NEEDL_BPHK6             Reviewed;         233 AA.\nAC   Q9AYZ3;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-JUN-2001, sequence version 1.\nDT   28-JAN-2026, entry version 83.\nDE   RecName: Full=Tail needle protein gp26;\nDE   AltName: Full=Head completion protein;\nDE   AltName: Full=Packaged DNA stabilization protein;\nDE   AltName: Full=Tail accessory factor gp26;\nGN   Name=26;\nOS   Enterobacteria phage HK620 (Bacteriophage HK620).\nOC   Viruses; Duplodnaviria; Heunggongvirae; Uroviricota; Caudoviricetes;\nOC   Lederbergvirus; Lederbergvirus HK620.\nOX   NCBI_TaxID=155148;\nOH   NCBI_TaxID=562; Escherichia coli.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:46.941025+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0f5b04df4f6c180ff20dad87e3929d5b22b173869433f4330e3aceb11b69188b",
  "url": "https://rest.uniprot.org/unisave/Q9AYZ3?format=txt&versions=83"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9AYZ3?format=txt&versions=83)

```json
{
  "entry_version": 83,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   DOMAIN, AND SUBUNIT.\nRX   PubMed=19482036; DOI=10.1016/j.jmb.2009.05.069;\nRA   Bhardwaj A., Walker-Kopp N., Casjens S.R., Cingolani G.;\nRT   \"An evolutionarily conserved family of virion tail needles related to\nRT   bacteriophage P22 gp26: correlation between structural stability and length\nRT   of the alpha-helical trimeric coiled coil.\";\nRL   J. Mol. Biol. 391:227-245(2009).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:46.941025+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 23-30",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0f5b04df4f6c180ff20dad87e3929d5b22b173869433f4330e3aceb11b69188b",
  "url": "https://rest.uniprot.org/unisave/Q9AYZ3?format=txt&versions=83"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9AYZ3?format=txt&versions=83)

```json
{
  "entry_version": 83,
  "evidence_id": "H3",
  "excerpt": "FT   REPEAT          61..67\nFT                   /note=\"Trimerization heptad repeat 1\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P35837\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:46.941025+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 96-98",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0f5b04df4f6c180ff20dad87e3929d5b22b173869433f4330e3aceb11b69188b",
  "url": "https://rest.uniprot.org/unisave/Q9AYZ3?format=txt&versions=83"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9AYZ3?format=txt&versions=83)

```json
{
  "entry_version": 83,
  "evidence_id": "H4",
  "excerpt": "FT   REPEAT          70..76\nFT                   /note=\"Trimerization heptad repeat 2\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P35837\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:46.941025+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 99-101",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0f5b04df4f6c180ff20dad87e3929d5b22b173869433f4330e3aceb11b69188b",
  "url": "https://rest.uniprot.org/unisave/Q9AYZ3?format=txt&versions=83"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9AYZ3?format=txt&versions=83)

```json
{
  "entry_version": 83,
  "evidence_id": "H5",
  "excerpt": "FT   REPEAT          77..83\nFT                   /note=\"Trimerization heptad repeat 3\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P35837\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:46.941025+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 102-104",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0f5b04df4f6c180ff20dad87e3929d5b22b173869433f4330e3aceb11b69188b",
  "url": "https://rest.uniprot.org/unisave/Q9AYZ3?format=txt&versions=83"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9AYZ3?format=txt&versions=83)

```json
{
  "entry_version": 83,
  "evidence_id": "H6",
  "excerpt": "FT   REPEAT          84..90\nFT                   /note=\"Trimerization heptad repeat 4\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P35837\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:46.941025+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 105-107",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0f5b04df4f6c180ff20dad87e3929d5b22b173869433f4330e3aceb11b69188b",
  "url": "https://rest.uniprot.org/unisave/Q9AYZ3?format=txt&versions=83"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9AYZ3?format=txt&versions=83)

```json
{
  "entry_version": 83,
  "evidence_id": "H7",
  "excerpt": "FT   REPEAT          91..97\nFT                   /note=\"Trimerization heptad repeat 5\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P35837\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:46.941025+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 108-110",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0f5b04df4f6c180ff20dad87e3929d5b22b173869433f4330e3aceb11b69188b",
  "url": "https://rest.uniprot.org/unisave/Q9AYZ3?format=txt&versions=83"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9AYZ3?format=txt&versions=83)

```json
{
  "entry_version": 83,
  "evidence_id": "H8",
  "excerpt": "FT   REPEAT          98..104\nFT                   /note=\"Trimerization heptad repeat 6\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P35837\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:46.941025+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 111-113",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0f5b04df4f6c180ff20dad87e3929d5b22b173869433f4330e3aceb11b69188b",
  "url": "https://rest.uniprot.org/unisave/Q9AYZ3?format=txt&versions=83"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9AYZ3?format=txt&versions=83)

```json
{
  "entry_version": 83,
  "evidence_id": "H9",
  "excerpt": "FT   REPEAT          105..111\nFT                   /note=\"Trimerization heptad repeat 7\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P35837\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:46.941025+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 114-116",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0f5b04df4f6c180ff20dad87e3929d5b22b173869433f4330e3aceb11b69188b",
  "url": "https://rest.uniprot.org/unisave/Q9AYZ3?format=txt&versions=83"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9AYZ3?format=txt&versions=83)

```json
{
  "entry_version": 83,
  "evidence_id": "H10",
  "excerpt": "FT   REPEAT          112..118\nFT                   /note=\"Trimerization heptad repeat 8\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P35837\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:46.941025+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 117-119",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0f5b04df4f6c180ff20dad87e3929d5b22b173869433f4330e3aceb11b69188b",
  "url": "https://rest.uniprot.org/unisave/Q9AYZ3?format=txt&versions=83"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9AYZ3?format=txt&versions=83)

```json
{
  "entry_version": 83,
  "evidence_id": "H11",
  "excerpt": "FT   REPEAT          119..125\nFT                   /note=\"Trimerization heptad repeat 9\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P35837\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:46.941025+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 120-122",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0f5b04df4f6c180ff20dad87e3929d5b22b173869433f4330e3aceb11b69188b",
  "url": "https://rest.uniprot.org/unisave/Q9AYZ3?format=txt&versions=83"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9AYZ3?format=txt&versions=83)

```json
{
  "entry_version": 83,
  "evidence_id": "H12",
  "excerpt": "FT   REPEAT          126..132\nFT                   /note=\"Trimerization heptad repeat 10\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P35837\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:46.941025+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 123-125",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0f5b04df4f6c180ff20dad87e3929d5b22b173869433f4330e3aceb11b69188b",
  "url": "https://rest.uniprot.org/unisave/Q9AYZ3?format=txt&versions=83"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9AYZ3?format=txt&versions=83)

```json
{
  "entry_version": 83,
  "evidence_id": "H13",
  "excerpt": "FT   REPEAT          133..139\nFT                   /note=\"Trimerization heptad repeat 11\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P35837\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:46.941025+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 126-128",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0f5b04df4f6c180ff20dad87e3929d5b22b173869433f4330e3aceb11b69188b",
  "url": "https://rest.uniprot.org/unisave/Q9AYZ3?format=txt&versions=83"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9AYZ3?format=txt&versions=83)

```json
{
  "entry_version": 83,
  "evidence_id": "H14",
  "excerpt": "FT   REGION          2..50\nFT                   /note=\"Interaction with tail hub protein\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P35837\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:46.941025+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 129-131",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0f5b04df4f6c180ff20dad87e3929d5b22b173869433f4330e3aceb11b69188b",
  "url": "https://rest.uniprot.org/unisave/Q9AYZ3?format=txt&versions=83"
}
```

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9AYZ3?format=txt&versions=83)

```json
{
  "entry_version": 83,
  "evidence_id": "H15",
  "excerpt": "FT   REGION          175..233\nFT                   /note=\"Inverted coiled coil\"\nFT                   /evidence=\"ECO:0000269|PubMed:19482036\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:46.941025+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 132-134",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0f5b04df4f6c180ff20dad87e3929d5b22b173869433f4330e3aceb11b69188b",
  "url": "https://rest.uniprot.org/unisave/Q9AYZ3?format=txt&versions=83"
}
```

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9AYZ3?format=txt&versions=83)

```json
{
  "entry_version": 83,
  "evidence_id": "H16",
  "excerpt": "FT   MOTIF           216..220\nFT                   /note=\"Basic cluster\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P35837\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:46.941025+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 137-139",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0f5b04df4f6c180ff20dad87e3929d5b22b173869433f4330e3aceb11b69188b",
  "url": "https://rest.uniprot.org/unisave/Q9AYZ3?format=txt&versions=83"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/motif_position.json), zero-based source row 44. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
