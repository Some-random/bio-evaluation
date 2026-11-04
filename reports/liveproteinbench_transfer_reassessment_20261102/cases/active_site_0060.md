# active_site_0060

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0060.txt)

**Task:** `active_site`  
**Expected answer:** **B** — Position 200 (Proton acceptor)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MLNDYLQWEKFILRGVEFPTRYRVDGDEVEITPSSRLYVSGMGGSGVVGDLIRDFSIVWNWDVEVTVVKDYFLRARDGLLIAVSYSGNTVETLYSVEYAKKRRIPTVAITTGGKLAQMGVPTIIIPKASAPRAALPQMLTAALHVVRKVYGIPIEIPEALEPPNDPLIHKLMEDFQKRPTIVAPETMRGVAYRVKNEFNENAKIEPSVEILPEAHHNWIEGSERPIVALTSPHIPREHQERVKATLEILGGTLYVVEMSTRGVLTFLREVGVASIKLAESRGVNPLATPRIEALKRRLQ

[Multiple Choices]
A. Position 315 (For beta-ketoacyl synthase activity)
B. Position 200 (Proton acceptor)
C. Position 4681 (Proton acceptor; for dehydratase activity 2)
D. Position 5963 (For beta-ketoacyl synthase 4 activity)
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

> The sequence-matched UniProt annotation identifies position 200 as a proton acceptor. Its evidence is transferred by similarity, rather than direct experimental evidence for this exact protein.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The supplied sequence is 299 residues long, so positions 315, 4681, and 5963 in options A, C, and D are outside the protein. B is the only positionally possible choice; its proton-acceptor role is plausible for an enzyme active site, though not established by sequence length alone.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence length eliminates the other options without needing the exact protein's database annotation. This supports choosing B among the offered alternatives, while leaving the precise catalytic assignment less certain from the original input alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only B gives a position within the supplied sequence.


### Important caveats

- The supporting annotation is based on similarity transfer, not direct experimental evidence for this exact sequence.
- The question asks about active-site residues plural, but each option gives only one position; the keyed option may not describe the complete catalytic center.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The supplied sequence is 299 residues long, so positions 315, 4681, and 5963 in options A, C, and D are outside the protein. B is the only positionally possible choice; its proton-acceptor role is plausible for an enzyme active site, though not established by sequence length alone.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence length eliminates the other options without needing the exact protein's database annotation. This supports choosing B among the offered alternatives, while leaving the precise catalytic assignment less certain from the original input alone."
  },
  "case_id": "active_site_0060",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies position 200 as a proton acceptor. Its evidence is transferred by similarity, rather than direct experimental evidence for this exact protein."
  },
  "important_caveats": [
    "The supporting annotation is based on similarity transfer, not direct experimental evidence for this exact sequence.",
    "The question asks about active-site residues plural, but each option gives only one position; the keyed option may not describe the complete catalytic center."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only B gives a position within the supplied sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0060",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies position 200 as a proton acceptor. Its evidence is transferred by similarity, rather than direct experimental evidence for this exact protein.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The supplied sequence is 299 residues long, so positions 315, 4681, and 5963 in options A, C, and D are outside the protein. B is the only positionally possible choice; its proton-acceptor role is plausible for an enzyme active site, though not established by sequence length alone.",
    "missing_item_specific_fact": "",
    "reason": "The sequence length eliminates the other options without needing the exact protein's database annotation. This supports choosing B among the offered alternatives, while leaving the precise catalytic assignment less certain from the original input alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only B gives a position within the supplied sequence."
  },
  "important_caveats": [
    "The supporting annotation is based on similarity transfer, not direct experimental evidence for this exact sequence.",
    "The question asks about active-site residues plural, but each option gives only one position; the keyed option may not describe the complete catalytic center."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A3MTR6) annotates position 200 as 'Proton acceptor' active site (evidence code ECO:0000250, transferred by similarity from Q8ZWV0). The protein is a bifunctional phosphoglucose/phosphomannose isomerase (EC 5.3.1.8/5.3.1.9), whose catalytic mechanism involves proton transfer. The annotation is computational inference by similarity rather than direct experimental determination, but it is consistent with the known GPI/PMI catalytic mechanism and the sequence length (299 aa) places position 200 within the protein. The expected answer B matches the database annotation.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein sequence is only 299 amino acids long. Options A (position 315), C (position 4681), and D (position 5963) all reference residue positions that exceed the protein's length, making them physically impossible. Furthermore, the functional descriptions in those options ('beta-ketoacyl synthase activity', 'dehydratase activity 2', 'beta-ketoacyl synthase 4 activity') correspond to catalytic domains of large multi-domain fatty acid synthase complexes, not a small ~300-residue isomerase. The sequence contains the characteristic 'SGMGGSGVVGDL' motif near position 44-55, diagnostic of the TIM-barrel fold of phosphoglucose isomerase, whose catalytic mechanism involves a proton acceptor (typically a Glu or Lys in the active site). Only option B (position 200, proton acceptor) is both within the protein's length and mechanistically consistent with the identified enzyme family.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model can eliminate options A, C, and D purely by noting that their referenced positions (315, 4681, 5963) exceed the 299-residue sequence length, and that their described functions (beta-ketoacyl synthase, dehydratase) belong to entirely different enzyme classes. The remaining option B (position 200, proton acceptor) is the only physically possible and mechanistically coherent choice for a phosphoglucose isomerase. This requires only basic sequence-length reasoning and general knowledge of enzyme families, not memorization of this protein's specific annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only option B references a position within the 299-amino-acid sequence and describes a function consistent with the protein's family. The other three options are eliminated by sequence-length impossibility and functional mismatch.


### Important caveats

- The active site annotation at position 200 carries evidence code ECO:0000250 (similarity transfer from Q8ZWV0), meaning it is computational inference rather than direct experimental determination for this specific protein.
- Option A (position 315) is only 16 residues beyond the protein's C-terminus, so a model that miscounts by a small margin might not immediately eliminate it, though the functional description (beta-ketoacyl synthase) still clearly mismatches.
- The reviewer-only UniProt accession and organism identity were not provided to the evaluated model; the reasoning relies solely on sequence length and family-level motifs visible in the input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein sequence is only 299 amino acids long. Options A (position 315), C (position 4681), and D (position 5963) all reference residue positions that exceed the protein's length, making them physically impossible. Furthermore, the functional descriptions in those options ('beta-ketoacyl synthase activity', 'dehydratase activity 2', 'beta-ketoacyl synthase 4 activity') correspond to catalytic domains of large multi-domain fatty acid synthase complexes, not a small ~300-residue isomerase. The sequence contains the characteristic 'SGMGGSGVVGDL' motif near position 44-55, diagnostic of the TIM-barrel fold of phosphoglucose isomerase, whose catalytic mechanism involves a proton acceptor (typically a Glu or Lys in the active site). Only option B (position 200, proton acceptor) is both within the protein's length and mechanistically consistent with the identified enzyme family.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model can eliminate options A, C, and D purely by noting that their referenced positions (315, 4681, 5963) exceed the 299-residue sequence length, and that their described functions (beta-ketoacyl synthase, dehydratase) belong to entirely different enzyme classes. The remaining option B (position 200, proton acceptor) is the only physically possible and mechanistically coherent choice for a phosphoglucose isomerase. This requires only basic sequence-length reasoning and general knowledge of enzyme families, not memorization of this protein's specific annotation."
  },
  "case_id": "active_site_0060",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A3MTR6) annotates position 200 as 'Proton acceptor' active site (evidence code ECO:0000250, transferred by similarity from Q8ZWV0). The protein is a bifunctional phosphoglucose/phosphomannose isomerase (EC 5.3.1.8/5.3.1.9), whose catalytic mechanism involves proton transfer. The annotation is computational inference by similarity rather than direct experimental determination, but it is consistent with the known GPI/PMI catalytic mechanism and the sequence length (299 aa) places position 200 within the protein. The expected answer B matches the database annotation."
  },
  "important_caveats": [
    "The active site annotation at position 200 carries evidence code ECO:0000250 (similarity transfer from Q8ZWV0), meaning it is computational inference rather than direct experimental determination for this specific protein.",
    "Option A (position 315) is only 16 residues beyond the protein's C-terminus, so a model that miscounts by a small margin might not immediately eliminate it, though the functional description (beta-ketoacyl synthase) still clearly mismatches.",
    "The reviewer-only UniProt accession and organism identity were not provided to the evaluated model; the reasoning relies solely on sequence length and family-level motifs visible in the input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option B references a position within the 299-amino-acid sequence and describes a function consistent with the protein's family. The other three options are eliminated by sequence-length impossibility and functional mismatch."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0060",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A3MTR6) annotates position 200 as 'Proton acceptor' active site (evidence code ECO:0000250, transferred by similarity from Q8ZWV0). The protein is a bifunctional phosphoglucose/phosphomannose isomerase (EC 5.3.1.8/5.3.1.9), whose catalytic mechanism involves proton transfer. The annotation is computational inference by similarity rather than direct experimental determination, but it is consistent with the known GPI/PMI catalytic mechanism and the sequence length (299 aa) places position 200 within the protein. The expected answer B matches the database annotation.",
    "evidence_ids": ["C5", "H3", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein sequence is only 299 amino acids long. Options A (position 315), C (position 4681), and D (position 5963) all reference residue positions that exceed the protein's length, making them physically impossible. Furthermore, the functional descriptions in those options ('beta-ketoacyl synthase activity', 'dehydratase activity 2', 'beta-ketoacyl synthase 4 activity') correspond to catalytic domains of large multi-domain fatty acid synthase complexes, not a small ~300-residue isomerase. The sequence contains the characteristic 'SGMGGSGVVGDL' motif near position 44-55, diagnostic of the TIM-barrel fold of phosphoglucose isomerase, whose catalytic mechanism involves a proton acceptor (typically a Glu or Lys in the active site). Only option B (position 200, proton acceptor) is both within the protein's length and mechanistically consistent with the identified enzyme family.",
    "missing_item_specific_fact": "",
    "reason": "A model can eliminate options A, C, and D purely by noting that their referenced positions (315, 4681, 5963) exceed the 299-residue sequence length, and that their described functions (beta-ketoacyl synthase, dehydratase) belong to entirely different enzyme classes. The remaining option B (position 200, proton acceptor) is the only physically possible and mechanistically coherent choice for a phosphoglucose isomerase. This requires only basic sequence-length reasoning and general knowledge of enzyme families, not memorization of this protein's specific annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option B references a position within the 299-amino-acid sequence and describes a function consistent with the protein's family. The other three options are eliminated by sequence-length impossibility and functional mismatch."
  },
  "important_caveats": [
    "The active site annotation at position 200 carries evidence code ECO:0000250 (similarity transfer from Q8ZWV0), meaning it is computational inference rather than direct experimental determination for this specific protein.",
    "Option A (position 315) is only 16 residues beyond the protein's C-terminus, so a model that miscounts by a small margin might not immediately eliminate it, though the functional description (beta-ketoacyl synthase) still clearly mismatches.",
    "The reviewer-only UniProt accession and organism identity were not provided to the evaluated model; the reasoning relies solely on sequence length and family-level motifs visible in the input."
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
  "benchmark_sequence_length": 299,
  "benchmark_sequence_sha256": "c1fe40d32c9a8ace25b121d1ae83f544553f7aee96a73eb13f919f4b78b80f91",
  "current_entry_audit": {
    "entryVersion": 75,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2007-04-03",
    "sequenceVersion": 1
  },
  "current_record_sha256": "ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 299,
  "current_source_sequence_sha256": "c1fe40d32c9a8ace25b121d1ae83f544553f7aee96a73eb13f919f4b78b80f91",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 74,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A3MTR6",
  "selected_historical_entry_version": 74,
  "selected_historical_record_sha256": "9c472af706932a5c4dae44d3e7eaa83f12d4956caae5979ddee1e4be573d0761",
  "selected_historical_source_sequence_length": 299,
  "selected_historical_source_sequence_sha256": "c1fe40d32c9a8ace25b121d1ae83f544553f7aee96a73eb13f919f4b78b80f91",
  "selected_historical_version": {
    "accession": "A3MTR6",
    "database": "Swiss-Prot",
    "entryVersion": 74,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "PGMI_PYRCJ",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A3MTR6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:26:58.786987+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3",
  "url": "https://rest.uniprot.org/uniprotkb/A3MTR6.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":75,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2007-04-03\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:26:58.786987+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3",
  "url": "https://rest.uniprot.org/uniprotkb/A3MTR6.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Archaea\",\"Thermoproteota\",\"Thermoprotei\",\"Thermoproteales\",\"Thermoproteaceae\",\"Pyrobaculum\"],\"scientificName\":\"Pyrobaculum calidifontis (strain DSM 21063 / JCM 11548 / VA1)\",\"taxonId\":410359}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:26:58.786987+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3",
  "url": "https://rest.uniprot.org/uniprotkb/A3MTR6.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39208883\",\"source\":\"PubMed\"}],\"value\":\"Glucose-6-phosphate isomerase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"GPI\"}]},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Mannose-6-phosphate isomerase\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39208883\",\"source\":\"PubMed\"}],\"value\":\"5.3.1.8\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39208883\",\"source\":\"PubMed\"}],\"value\":\"5.3.1.9\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39208883\",\"source\":\"PubMed\"}],\"value\":\"Bifunctional phosphoglucose/phosphomannose isomerase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Bifunctional PGI/PMI\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:26:58.786987+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3",
  "url": "https://rest.uniprot.org/uniprotkb/A3MTR6.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Proton acceptor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8ZWV0\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":200},\"start\":{\"modifier\":\"EXACT\",\"value\":200}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:26:58.786987+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3",
  "url": "https://rest.uniprot.org/uniprotkb/A3MTR6.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Proton donor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8ZWV0\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":216},\"start\":{\"modifier\":\"EXACT\",\"value\":216}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:26:58.786987+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3",
  "url": "https://rest.uniprot.org/uniprotkb/A3MTR6.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Proton acceptor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8ZWV0\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":295},\"start\":{\"modifier\":\"EXACT\",\"value\":295}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:26:58.786987+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3",
  "url": "https://rest.uniprot.org/uniprotkb/A3MTR6.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8ZWV0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:61527\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:61527\",\"name\":\"D-fructose 6-phosphate\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":44},\"start\":{\"modifier\":\"EXACT\",\"value\":44}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:26:58.786987+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3",
  "url": "https://rest.uniprot.org/uniprotkb/A3MTR6.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8ZWV0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:61527\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:61527\",\"name\":\"D-fructose 6-phosphate\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":45},\"start\":{\"modifier\":\"EXACT\",\"value\":45}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:26:58.786987+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3",
  "url": "https://rest.uniprot.org/uniprotkb/A3MTR6.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8ZWV0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:61527\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:61527\",\"name\":\"D-fructose 6-phosphate\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":84},\"start\":{\"modifier\":\"EXACT\",\"value\":84}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:26:58.786987+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3",
  "url": "https://rest.uniprot.org/uniprotkb/A3MTR6.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8ZWV0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:61527\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:61527\",\"name\":\"D-fructose 6-phosphate\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":86},\"start\":{\"modifier\":\"EXACT\",\"value\":86}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:26:58.786987+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3",
  "url": "https://rest.uniprot.org/uniprotkb/A3MTR6.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8ZWV0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:61527\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:61527\",\"name\":\"D-fructose 6-phosphate\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":89},\"start\":{\"modifier\":\"EXACT\",\"value\":89}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-02T04:26:58.786987+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3",
  "url": "https://rest.uniprot.org/uniprotkb/A3MTR6.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8ZWV0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:61527\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:61527\",\"name\":\"D-fructose 6-phosphate\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":132},\"start\":{\"modifier\":\"EXACT\",\"value\":132}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-02T04:26:58.786987+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3",
  "url": "https://rest.uniprot.org/uniprotkb/A3MTR6.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8ZWV0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:61527\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:61527\",\"name\":\"D-fructose 6-phosphate\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":216},\"start\":{\"modifier\":\"EXACT\",\"value\":216}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/11",
  "retrieved_utc": "2026-11-02T04:26:58.786987+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3",
  "url": "https://rest.uniprot.org/uniprotkb/A3MTR6.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8ZWV0\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:61527\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:61527\",\"name\":\"D-fructose 6-phosphate\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":295},\"start\":{\"modifier\":\"EXACT\",\"value\":295}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/12",
  "retrieved_utc": "2026-11-02T04:26:58.786987+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3",
  "url": "https://rest.uniprot.org/uniprotkb/A3MTR6.json"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)

```json
{
  "evidence_id": "C16",
  "excerpt": "{\"citation\":{\"authors\":[\"Maqsood A.\",\"Shakir N.A.\",\"Aslam M.\",\"Rahman M.\",\"Rashid N.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39208883\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.ijbiomac.2024.135127\"}],\"citationType\":\"journal article\",\"firstPage\":\"135127\",\"id\":\"39208883\",\"journal\":\"Int. J. Biol. Macromol.\",\"lastPage\":\"135127\",\"publicationDate\":\"2024\",\"title\":\"Structural and functional investigations of Pcal_0606, a bifunctional phosphoglucose/phosphomannose isomerase from Pyrobaculum calidifontis.\",\"volume\":\"279\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"DSM 21063 / JCM 11548 / VA1\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:26:58.786987+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3",
  "url": "https://rest.uniprot.org/uniprotkb/A3MTR6.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H1",
  "excerpt": "ID   PGMI_PYRCJ              Reviewed;         299 AA.\nAC   A3MTR6;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   03-APR-2007, sequence version 1.\nDT   28-JAN-2026, entry version 74.\nDE   RecName: Full=Bifunctional phosphoglucose/phosphomannose isomerase {ECO:0000303|PubMed:39208883};\nDE            Short=Bifunctional PGI/PMI {ECO:0000305};\nDE            EC=5.3.1.8 {ECO:0000269|PubMed:39208883};\nDE            EC=5.3.1.9 {ECO:0000269|PubMed:39208883};\nDE   AltName: Full=Glucose-6-phosphate isomerase {ECO:0000303|PubMed:39208883};\nDE            Short=GPI {ECO:0000305};\nDE   AltName: Full=Mannose-6-phosphate isomerase {ECO:0000305};\nGN   OrderedLocusNames=Pcal_0606 {ECO:0000312|EMBL:ABO08033.1};\nOS   Pyrobaculum calidifontis (strain DSM 21063 / JCM 11548 / VA1).\nOC   Archaea; Thermoproteota; Thermoprotei; Thermoproteales; Thermoproteaceae;\nOC   Pyrobaculum.\nOX   NCBI_TaxID=410359;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:04.156488+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9c472af706932a5c4dae44d3e7eaa83f12d4956caae5979ddee1e4be573d0761",
  "url": "https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, BIOPHYSICOCHEMICAL\nRP   PROPERTIES, AND SUBUNIT.\nRC   STRAIN=DSM 21063 / JCM 11548 / VA1;\nRX   PubMed=39208883; DOI=10.1016/j.ijbiomac.2024.135127;\nRA   Maqsood A., Shakir N.A., Aslam M., Rahman M., Rashid N.;\nRT   \"Structural and functional investigations of Pcal_0606, a bifunctional\nRT   phosphoglucose/phosphomannose isomerase from Pyrobaculum calidifontis.\";\nRL   Int. J. Biol. Macromol. 279:135127-135127(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:04.156488+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 28-36",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9c472af706932a5c4dae44d3e7eaa83f12d4956caae5979ddee1e4be573d0761",
  "url": "https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        200\nFT                   /note=\"Proton acceptor\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8ZWV0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:04.156488+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 119-121",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9c472af706932a5c4dae44d3e7eaa83f12d4956caae5979ddee1e4be573d0761",
  "url": "https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H4",
  "excerpt": "FT   ACT_SITE        216\nFT                   /note=\"Proton donor\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8ZWV0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:04.156488+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 122-124",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9c472af706932a5c4dae44d3e7eaa83f12d4956caae5979ddee1e4be573d0761",
  "url": "https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H5",
  "excerpt": "FT   ACT_SITE        295\nFT                   /note=\"Proton acceptor\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8ZWV0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:04.156488+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 125-127",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9c472af706932a5c4dae44d3e7eaa83f12d4956caae5979ddee1e4be573d0761",
  "url": "https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H6",
  "excerpt": "FT   BINDING         44\nFT                   /ligand=\"D-fructose 6-phosphate\"\nFT                   /ligand_id=\"ChEBI:CHEBI:61527\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8ZWV0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:04.156488+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 128-131",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9c472af706932a5c4dae44d3e7eaa83f12d4956caae5979ddee1e4be573d0761",
  "url": "https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H7",
  "excerpt": "FT   BINDING         45\nFT                   /ligand=\"D-fructose 6-phosphate\"\nFT                   /ligand_id=\"ChEBI:CHEBI:61527\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8ZWV0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:04.156488+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 132-135",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9c472af706932a5c4dae44d3e7eaa83f12d4956caae5979ddee1e4be573d0761",
  "url": "https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H8",
  "excerpt": "FT   BINDING         84\nFT                   /ligand=\"D-fructose 6-phosphate\"\nFT                   /ligand_id=\"ChEBI:CHEBI:61527\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8ZWV0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:04.156488+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 136-139",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9c472af706932a5c4dae44d3e7eaa83f12d4956caae5979ddee1e4be573d0761",
  "url": "https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H9",
  "excerpt": "FT   BINDING         86\nFT                   /ligand=\"D-fructose 6-phosphate\"\nFT                   /ligand_id=\"ChEBI:CHEBI:61527\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8ZWV0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:04.156488+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 140-143",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9c472af706932a5c4dae44d3e7eaa83f12d4956caae5979ddee1e4be573d0761",
  "url": "https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H10",
  "excerpt": "FT   BINDING         89\nFT                   /ligand=\"D-fructose 6-phosphate\"\nFT                   /ligand_id=\"ChEBI:CHEBI:61527\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8ZWV0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:04.156488+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 144-147",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9c472af706932a5c4dae44d3e7eaa83f12d4956caae5979ddee1e4be573d0761",
  "url": "https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H11",
  "excerpt": "FT   BINDING         132\nFT                   /ligand=\"D-fructose 6-phosphate\"\nFT                   /ligand_id=\"ChEBI:CHEBI:61527\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8ZWV0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:04.156488+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 148-151",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9c472af706932a5c4dae44d3e7eaa83f12d4956caae5979ddee1e4be573d0761",
  "url": "https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H12",
  "excerpt": "FT   BINDING         216\nFT                   /ligand=\"D-fructose 6-phosphate\"\nFT                   /ligand_id=\"ChEBI:CHEBI:61527\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8ZWV0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:04.156488+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 152-155",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9c472af706932a5c4dae44d3e7eaa83f12d4956caae5979ddee1e4be573d0761",
  "url": "https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H13",
  "excerpt": "FT   BINDING         295\nFT                   /ligand=\"D-fructose 6-phosphate\"\nFT                   /ligand_id=\"ChEBI:CHEBI:61527\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8ZWV0\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:04.156488+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 156-159",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9c472af706932a5c4dae44d3e7eaa83f12d4956caae5979ddee1e4be573d0761",
  "url": "https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 60. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
