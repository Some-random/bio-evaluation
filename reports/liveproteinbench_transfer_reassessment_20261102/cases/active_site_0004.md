# active_site_0004

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0004.txt)

**Task:** `active_site`  
**Expected answer:** **B** — Position 21 (Proton acceptor)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAIKLIVGLANPGAEYAATRHNAGAWYVDLLAERLRAPLREEPKFFGYTSRITLEGEDVRLLVPTTFMNLSGKAVGAMASFYRIQPDEILVAHDELDLPPGVAKFKLGGGHGGHNGLKDIISKLGNNPNFHRLRVGIGHPGDKNKVVGFVLGKPPVSEQKLIDEAIDEAARCTELWFKEGLAKATSRLHTFKAQ

[Multiple Choices]
A. Position 4261 (For beta-ketoacyl synthase 3 activity)
B. Position 21 (Proton acceptor)
C. Position 355 (For beta-ketoacyl synthase activity)
D. Position 318 (O-(5'-phospho-DNA)-tyrosine intermediate)
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

> The sequence-matched UniProt annotation identifies position 21 as the proton acceptor, supporting choice B. This is a HAMAP-rule computational annotation, not experimental evidence.

Citations as saved: [C5](#evidence-c5), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 194-residue sequence has the characteristic context of a bacterial peptidyl-tRNA hydrolase, and position 21 is histidine. Transferable family knowledge associates the conserved N-terminal histidine with the proton-accepting catalytic role, distinguishing B from the beta-ketoacyl synthase and DNA-tyrosine-intermediate alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference from the sequence and conserved catalytic features meaningfully favors B without requiring recall of this exact protein's database record. The precise annotation is computationally assigned, so the inference is not equivalent to direct experimental confirmation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, only B is consistent with the sequence's peptidyl-tRNA hydrolase family features and its conserved catalytic histidine.


### Important caveats

- The supporting source annotation is based on the HAMAP rule; the supplied evidence does not establish experimental validation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 194-residue sequence has the characteristic context of a bacterial peptidyl-tRNA hydrolase, and position 21 is histidine. Transferable family knowledge associates the conserved N-terminal histidine with the proton-accepting catalytic role, distinguishing B from the beta-ketoacyl synthase and DNA-tyrosine-intermediate alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence and conserved catalytic features meaningfully favors B without requiring recall of this exact protein's database record. The precise annotation is computationally assigned, so the inference is not equivalent to direct experimental confirmation."
  },
  "case_id": "active_site_0004",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies position 21 as the proton acceptor, supporting choice B. This is a HAMAP-rule computational annotation, not experimental evidence."
  },
  "important_caveats": [
    "The supporting source annotation is based on the HAMAP rule; the supplied evidence does not establish experimental validation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, only B is consistent with the sequence's peptidyl-tRNA hydrolase family features and its conserved catalytic histidine."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0004",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies position 21 as the proton acceptor, supporting choice B. This is a HAMAP-rule computational annotation, not experimental evidence.",
    "evidence_ids": ["C5", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 194-residue sequence has the characteristic context of a bacterial peptidyl-tRNA hydrolase, and position 21 is histidine. Transferable family knowledge associates the conserved N-terminal histidine with the proton-accepting catalytic role, distinguishing B from the beta-ketoacyl synthase and DNA-tyrosine-intermediate alternatives.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence and conserved catalytic features meaningfully favors B without requiring recall of this exact protein's database record. The precise annotation is computationally assigned, so the inference is not equivalent to direct experimental confirmation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, only B is consistent with the sequence's peptidyl-tRNA hydrolase family features and its conserved catalytic histidine."
  },
  "important_caveats": [
    "The supporting source annotation is based on the HAMAP rule; the supplied evidence does not establish experimental validation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A0F6B281) annotates position 21 as an active site 'Proton acceptor' (evidence codes C5, H2), matching the expected answer exactly. The annotation derives from HAMAP-Rule MF_00083 (ECO:0000255), which is a computational/family-transfer annotation rather than direct experimental evidence on this specific protein. However, the His21 proton-acceptor role is consistent with the well-characterized peptidyl-tRNA hydrolase (Pth, EC 3.1.1.29) family mechanism involving a His-Glu catalytic dyad. The residue at position 21 in the supplied sequence is indeed Histidine (H), confirming internal consistency.

Citations as saved: [C5](#evidence-c5), [H2](#evidence-h2), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The supplied protein sequence is 194 amino acids long (verifiable by direct counting of the input). Options A (position 4261), C (position 355), and D (position 318) all reference residue positions that exceed the protein's length and therefore cannot correspond to any amino acid in this enzyme. Only option B (position 21) falls within the valid range. This arithmetic elimination alone uniquely identifies B. Additionally, position 21 corresponds to Histidine (H) in the sequence, and a His acting as a 'Proton acceptor' is a widely observed catalytic motif in small hydrolases and transferases (e.g., serine proteases, Pth family), making the functional description biologically plausible. The wrong-answer descriptions (beta-ketoacyl synthase, phospho-DNA-tyrosine intermediate) belong to entirely unrelated enzyme families, further supporting their exclusion.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can eliminate options A, C, and D by noting their positions exceed the 194-residue sequence length—a check requiring only arithmetic on the provided input. The remaining option B (His21, proton acceptor) is consistent with general catalytic-mechanism knowledge of small hydrolases and the Pth family. No target-specific database lookup is necessary to distinguish the choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only one option (B) references a residue position within the 194-amino-acid sequence. The other three options cite positions (318, 355, 4261) that are physically impossible for this protein, leaving no ambiguity.


### Important caveats

- The active-site annotation is based on HAMAP-Rule (computational family transfer, ECO:0000255), not direct experimental validation on this specific Salmonella Pth protein.
- The question is trivially solvable by position-range arithmetic alone, which limits its value as a test of genuine active-site prediction reasoning.
- The wrong-answer descriptions (beta-ketoacyl synthase, phospho-DNA-tyrosine intermediate) appear to be drawn from unrelated enzyme entries and do not correspond to any annotation in this protein's record.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The supplied protein sequence is 194 amino acids long (verifiable by direct counting of the input). Options A (position 4261), C (position 355), and D (position 318) all reference residue positions that exceed the protein's length and therefore cannot correspond to any amino acid in this enzyme. Only option B (position 21) falls within the valid range. This arithmetic elimination alone uniquely identifies B. Additionally, position 21 corresponds to Histidine (H) in the sequence, and a His acting as a 'Proton acceptor' is a widely observed catalytic motif in small hydrolases and transferases (e.g., serine proteases, Pth family), making the functional description biologically plausible. The wrong-answer descriptions (beta-ketoacyl synthase, phospho-DNA-tyrosine intermediate) belong to entirely unrelated enzyme families, further supporting their exclusion.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate options A, C, and D by noting their positions exceed the 194-residue sequence length—a check requiring only arithmetic on the provided input. The remaining option B (His21, proton acceptor) is consistent with general catalytic-mechanism knowledge of small hydrolases and the Pth family. No target-specific database lookup is necessary to distinguish the choices."
  },
  "case_id": "active_site_0004",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H2",
      "C4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A0F6B281) annotates position 21 as an active site 'Proton acceptor' (evidence codes C5, H2), matching the expected answer exactly. The annotation derives from HAMAP-Rule MF_00083 (ECO:0000255), which is a computational/family-transfer annotation rather than direct experimental evidence on this specific protein. However, the His21 proton-acceptor role is consistent with the well-characterized peptidyl-tRNA hydrolase (Pth, EC 3.1.1.29) family mechanism involving a His-Glu catalytic dyad. The residue at position 21 in the supplied sequence is indeed Histidine (H), confirming internal consistency."
  },
  "important_caveats": [
    "The active-site annotation is based on HAMAP-Rule (computational family transfer, ECO:0000255), not direct experimental validation on this specific Salmonella Pth protein.",
    "The question is trivially solvable by position-range arithmetic alone, which limits its value as a test of genuine active-site prediction reasoning.",
    "The wrong-answer descriptions (beta-ketoacyl synthase, phospho-DNA-tyrosine intermediate) appear to be drawn from unrelated enzyme entries and do not correspond to any annotation in this protein's record."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only one option (B) references a residue position within the 194-amino-acid sequence. The other three options cite positions (318, 355, 4261) that are physically impossible for this protein, leaving no ambiguity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0004",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A0F6B281) annotates position 21 as an active site 'Proton acceptor' (evidence codes C5, H2), matching the expected answer exactly. The annotation derives from HAMAP-Rule MF_00083 (ECO:0000255), which is a computational/family-transfer annotation rather than direct experimental evidence on this specific protein. However, the His21 proton-acceptor role is consistent with the well-characterized peptidyl-tRNA hydrolase (Pth, EC 3.1.1.29) family mechanism involving a His-Glu catalytic dyad. The residue at position 21 in the supplied sequence is indeed Histidine (H), confirming internal consistency.",
    "evidence_ids": ["C5", "H2", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The supplied protein sequence is 194 amino acids long (verifiable by direct counting of the input). Options A (position 4261), C (position 355), and D (position 318) all reference residue positions that exceed the protein's length and therefore cannot correspond to any amino acid in this enzyme. Only option B (position 21) falls within the valid range. This arithmetic elimination alone uniquely identifies B. Additionally, position 21 corresponds to Histidine (H) in the sequence, and a His acting as a 'Proton acceptor' is a widely observed catalytic motif in small hydrolases and transferases (e.g., serine proteases, Pth family), making the functional description biologically plausible. The wrong-answer descriptions (beta-ketoacyl synthase, phospho-DNA-tyrosine intermediate) belong to entirely unrelated enzyme families, further supporting their exclusion.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate options A, C, and D by noting their positions exceed the 194-residue sequence length—a check requiring only arithmetic on the provided input. The remaining option B (His21, proton acceptor) is consistent with general catalytic-mechanism knowledge of small hydrolases and the Pth family. No target-specific database lookup is necessary to distinguish the choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only one option (B) references a residue position within the 194-amino-acid sequence. The other three options cite positions (318, 355, 4261) that are physically impossible for this protein, leaving no ambiguity."
  },
  "important_caveats": [
    "The active-site annotation is based on HAMAP-Rule (computational family transfer, ECO:0000255), not direct experimental validation on this specific Salmonella Pth protein.",
    "The question is trivially solvable by position-range arithmetic alone, which limits its value as a test of genuine active-site prediction reasoning.",
    "The wrong-answer descriptions (beta-ketoacyl synthase, phospho-DNA-tyrosine intermediate) appear to be drawn from unrelated enzyme entries and do not correspond to any annotation in this protein's record."
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
  "benchmark_sequence_length": 194,
  "benchmark_sequence_sha256": "00656498a6b609ca797c42fc5a57fa47e1fcc3afb2d96e5c70eb6cd51566269c",
  "current_entry_audit": {
    "entryVersion": 43,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2015-06-24",
    "sequenceVersion": 1
  },
  "current_record_sha256": "99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 194,
  "current_source_sequence_sha256": "00656498a6b609ca797c42fc5a57fa47e1fcc3afb2d96e5c70eb6cd51566269c",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 42,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A0F6B281",
  "selected_historical_entry_version": 42,
  "selected_historical_record_sha256": "60b2125307db6a1a0373bc7d2279f21c78a94c37b3be59796a932c5d6fc020f9",
  "selected_historical_source_sequence_length": 194,
  "selected_historical_source_sequence_sha256": "00656498a6b609ca797c42fc5a57fa47e1fcc3afb2d96e5c70eb6cd51566269c",
  "selected_historical_version": {
    "accession": "A0A0F6B281",
    "database": "Swiss-Prot",
    "entryVersion": 42,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "PTH_SALT1",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A0F6B281\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:01.196338+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F6B281.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":43,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2015-06-24\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:01.196338+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F6B281.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Enterobacterales\",\"Enterobacteriaceae\",\"Salmonella\"],\"scientificName\":\"Salmonella typhimurium (strain 14028s / SGSC 2262)\",\"taxonId\":588858}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:01.196338+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F6B281.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_00083\",\"source\":\"HAMAP-Rule\"}],\"value\":\"3.1.1.29\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_00083\",\"source\":\"HAMAP-Rule\"}],\"value\":\"Peptidyl-tRNA hydrolase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_00083\",\"source\":\"HAMAP-Rule\"}],\"value\":\"Pth\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:01.196338+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F6B281.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Proton acceptor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_00083\",\"source\":\"HAMAP-Rule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":21},\"start\":{\"modifier\":\"EXACT\",\"value\":21}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:24:01.196338+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F6B281.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_00083\",\"source\":\"HAMAP-Rule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:17843\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:17843\",\"name\":\"tRNA\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":16},\"start\":{\"modifier\":\"EXACT\",\"value\":16}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:24:01.196338+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F6B281.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_00083\",\"source\":\"HAMAP-Rule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:17843\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:17843\",\"name\":\"tRNA\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":67},\"start\":{\"modifier\":\"EXACT\",\"value\":67}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:24:01.196338+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F6B281.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_00083\",\"source\":\"HAMAP-Rule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:17843\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:17843\",\"name\":\"tRNA\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":69},\"start\":{\"modifier\":\"EXACT\",\"value\":69}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:24:01.196338+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F6B281.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_00083\",\"source\":\"HAMAP-Rule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:17843\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:17843\",\"name\":\"tRNA\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":115},\"start\":{\"modifier\":\"EXACT\",\"value\":115}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:24:01.196338+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F6B281.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"Discriminates between blocked and unblocked aminoacyl-tRNA\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_00083\",\"source\":\"HAMAP-Rule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":11},\"start\":{\"modifier\":\"EXACT\",\"value\":11}},\"type\":\"Site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:24:01.196338+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F6B281.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"Stabilizes the basic form of H active site to accept a proton\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_00083\",\"source\":\"HAMAP-Rule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":94},\"start\":{\"modifier\":\"EXACT\",\"value\":94}},\"type\":\"Site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:24:01.196338+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F6B281.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42)

```json
{
  "entry_version": 42,
  "evidence_id": "H1",
  "excerpt": "ID   PTH_SALT1               Reviewed;         194 AA.\nAC   A0A0F6B281;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   24-JUN-2015, sequence version 1.\nDT   28-JAN-2026, entry version 42.\nDE   RecName: Full=Peptidyl-tRNA hydrolase {ECO:0000255|HAMAP-Rule:MF_00083};\nDE            Short=Pth {ECO:0000255|HAMAP-Rule:MF_00083};\nDE            EC=3.1.1.29 {ECO:0000255|HAMAP-Rule:MF_00083};\nGN   Name=pth {ECO:0000255|HAMAP-Rule:MF_00083, ECO:0000312|EMBL:ACY88619.1};\nGN   OrderedLocusNames=STM14_2156 {ECO:0000312|EMBL:ACY88619.1};\nOS   Salmonella typhimurium (strain 14028s / SGSC 2262).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Enterobacterales; Enterobacteriaceae; Salmonella.\nOX   NCBI_TaxID=588858;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:05.242925+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "60b2125307db6a1a0373bc7d2279f21c78a94c37b3be59796a932c5d6fc020f9",
  "url": "https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42)

```json
{
  "entry_version": 42,
  "evidence_id": "H2",
  "excerpt": "FT   ACT_SITE        21\nFT                   /note=\"Proton acceptor\"\nFT                   /evidence=\"ECO:0000255|HAMAP-Rule:MF_00083\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:05.242925+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 106-108",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "60b2125307db6a1a0373bc7d2279f21c78a94c37b3be59796a932c5d6fc020f9",
  "url": "https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42)

```json
{
  "entry_version": 42,
  "evidence_id": "H3",
  "excerpt": "FT   BINDING         16\nFT                   /ligand=\"tRNA\"\nFT                   /ligand_id=\"ChEBI:CHEBI:17843\"\nFT                   /evidence=\"ECO:0000255|HAMAP-Rule:MF_00083\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:05.242925+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 109-112",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "60b2125307db6a1a0373bc7d2279f21c78a94c37b3be59796a932c5d6fc020f9",
  "url": "https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42)

```json
{
  "entry_version": 42,
  "evidence_id": "H4",
  "excerpt": "FT   BINDING         67\nFT                   /ligand=\"tRNA\"\nFT                   /ligand_id=\"ChEBI:CHEBI:17843\"\nFT                   /evidence=\"ECO:0000255|HAMAP-Rule:MF_00083\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:05.242925+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 113-116",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "60b2125307db6a1a0373bc7d2279f21c78a94c37b3be59796a932c5d6fc020f9",
  "url": "https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42)

```json
{
  "entry_version": 42,
  "evidence_id": "H5",
  "excerpt": "FT   BINDING         69\nFT                   /ligand=\"tRNA\"\nFT                   /ligand_id=\"ChEBI:CHEBI:17843\"\nFT                   /evidence=\"ECO:0000255|HAMAP-Rule:MF_00083\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:05.242925+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 117-120",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "60b2125307db6a1a0373bc7d2279f21c78a94c37b3be59796a932c5d6fc020f9",
  "url": "https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42)

```json
{
  "entry_version": 42,
  "evidence_id": "H6",
  "excerpt": "FT   BINDING         115\nFT                   /ligand=\"tRNA\"\nFT                   /ligand_id=\"ChEBI:CHEBI:17843\"\nFT                   /evidence=\"ECO:0000255|HAMAP-Rule:MF_00083\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:05.242925+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 121-124",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "60b2125307db6a1a0373bc7d2279f21c78a94c37b3be59796a932c5d6fc020f9",
  "url": "https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42)

```json
{
  "entry_version": 42,
  "evidence_id": "H7",
  "excerpt": "FT   SITE            11\nFT                   /note=\"Discriminates between blocked and unblocked\nFT                   aminoacyl-tRNA\"\nFT                   /evidence=\"ECO:0000255|HAMAP-Rule:MF_00083\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:05.242925+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 125-128",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "60b2125307db6a1a0373bc7d2279f21c78a94c37b3be59796a932c5d6fc020f9",
  "url": "https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42)

```json
{
  "entry_version": 42,
  "evidence_id": "H8",
  "excerpt": "FT   SITE            94\nFT                   /note=\"Stabilizes the basic form of H active site to accept\nFT                   a proton\"\nFT                   /evidence=\"ECO:0000255|HAMAP-Rule:MF_00083\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:05.242925+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 129-132",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "60b2125307db6a1a0373bc7d2279f21c78a94c37b3be59796a932c5d6fc020f9",
  "url": "https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 4. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
