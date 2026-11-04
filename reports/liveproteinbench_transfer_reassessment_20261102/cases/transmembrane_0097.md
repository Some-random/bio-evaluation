# transmembrane_0097

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0097.txt)

**Task:** `transmembrane`  
**Expected answer:** **B** — 371..391; 409..429; 444..464; 472..492; 531..551; 564..586; 596..618

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKQNPAKTARMWIIICLLFVLGQATDNDRDFKMCGKWLHGIAPQNLEYDLKTGCERIEISANESTLSIQGRITAKCTQSSSIQLDSNPHQNQSHFCVFWEPLLDLLIVEVNGKNHTLCKPNGLQGTCCTDLSQGVQDNAHMYGIVNGSVKGDIITGDLKGNYIFDGAHINCKEKFCDEARLKPRGANMIEEVVMRFNAKGRVDLPCAQGTVIEMDEEFTGHNFTVPAPRFVDANTIPSVYIPSSLRSVSRRKSKVVCTYYKNKTLFERGPSKSALLDDIVGLSVENETIRNLIEPVKIRFHHRPFAPDSSGRCVSWDTKQDNEVNWKDDGCDTVKINEEQTECHCNHLTYFAILVQVEQKSTVRHLKALTFITAVGCAVSLVSCLVLFYWLCKRRRGKKNQISLVHRGLVVAIFLLCLFFILTGILANVANETVCQLTGSLLHYGLLSTLCWMAMEVFHTFLLVRKVFNSPLPIWIFYLMGFGFPFLLVSILLSVGDIYGERKIKPSDDVNNPYRMCWMTEGDKSQLAHYIINIGLLAVVVSSGLVMLFLVVREIRNRPDWKKIHVAFLSIWGLTCLYGTTWALGFLDFGPFSEVTLFLFCIINSLQGFFLMLRYYALERMKKKDVSSSDGSSSGSSKQHMLQTNEKS

[Multiple Choices]
A. 32..52; 730..750; 795..815; 845..865; 1111..1131
B. 371..391; 409..429; 444..464; 472..492; 531..551; 564..586; 596..618
C. 371..391; 409..429; 472..492; 531..551; 564..586; 596..618
D. 371..391; 409..431; 444..464; 472..492; 531..551; 564..586; 596..618
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Transmembrane Region Prediction, which is to predict a region of the protein that spans across a cell membrane. These transmembrane domains are typically hydrophobic alpha-helices that anchor the protein within the lipid bilayer or form channels. Based on the provided amino acid sequence, you must select the option that correctly identifies the start and end positions of a segment that crosses the membrane.. The inputs provided by the user for this task include:

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

> The sequence exactly matches the cited source sequence, whose annotations list seven transmembrane helices at the positions in B. These annotations support the key, though their evidence code is computational (ECO:0000255), not direct experimental evidence.

Citations as saved: [H5](#evidence-h5), [H7](#evidence-h7), [H9](#evidence-h9), [H11](#evidence-h11), [H13](#evidence-h13), [H15](#evidence-h15), [H17](#evidence-h17).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a long extracellular region followed by a cluster of seven membrane-length hydrophobic segments, characteristic of a seven-transmembrane GPCR. Those segments distinguish B from C, which omits one, and from A, whose listed positions do not match the seven-helix cluster. The strong hydrophobic spans support B's boundaries over D's extension of one helix into the following basic, non-hydrophobic loop.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level knowledge of GPCR architecture and recognizable hydrophobic spans in the supplied sequence meaningfully distinguish the offered choices without needing the exact protein's database record. Predicted helix boundaries can be approximate, so sequence-based reasoning does not independently establish experimental topology at every residue.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> B best matches the seven hydrophobic spans; the alternatives either omit a span, extend a span into a charged loop, or list unrelated positions.


### Important caveats

- The cited transmembrane annotations are computational predictions, not direct experimental measurements.
- Exact transmembrane boundaries may vary among prediction methods.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a long extracellular region followed by a cluster of seven membrane-length hydrophobic segments, characteristic of a seven-transmembrane GPCR. Those segments distinguish B from C, which omits one, and from A, whose listed positions do not match the seven-helix cluster. The strong hydrophobic spans support B's boundaries over D's extension of one helix into the following basic, non-hydrophobic loop.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level knowledge of GPCR architecture and recognizable hydrophobic spans in the supplied sequence meaningfully distinguish the offered choices without needing the exact protein's database record. Predicted helix boundaries can be approximate, so sequence-based reasoning does not independently establish experimental topology at every residue."
  },
  "case_id": "transmembrane_0097",
  "expected_answer_check": {
    "evidence_ids": [
      "H5",
      "H7",
      "H9",
      "H11",
      "H13",
      "H15",
      "H17"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches the cited source sequence, whose annotations list seven transmembrane helices at the positions in B. These annotations support the key, though their evidence code is computational (ECO:0000255), not direct experimental evidence."
  },
  "important_caveats": [
    "The cited transmembrane annotations are computational predictions, not direct experimental measurements.",
    "Exact transmembrane boundaries may vary among prediction methods."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B best matches the seven hydrophobic spans; the alternatives either omit a span, extend a span into a charged loop, or list unrelated positions."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0097",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches the cited source sequence, whose annotations list seven transmembrane helices at the positions in B. These annotations support the key, though their evidence code is computational (ECO:0000255), not direct experimental evidence.",
    "evidence_ids": ["H5", "H7", "H9", "H11", "H13", "H15", "H17"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a long extracellular region followed by a cluster of seven membrane-length hydrophobic segments, characteristic of a seven-transmembrane GPCR. Those segments distinguish B from C, which omits one, and from A, whose listed positions do not match the seven-helix cluster. The strong hydrophobic spans support B's boundaries over D's extension of one helix into the following basic, non-hydrophobic loop.",
    "missing_item_specific_fact": "",
    "reason": "Family-level knowledge of GPCR architecture and recognizable hydrophobic spans in the supplied sequence meaningfully distinguish the offered choices without needing the exact protein's database record. Predicted helix boundaries can be approximate, so sequence-based reasoning does not independently establish experimental topology at every residue."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B best matches the seven hydrophobic spans; the alternatives either omit a span, extend a span into a charged loop, or list unrelated positions."
  },
  "important_caveats": [
    "The cited transmembrane annotations are computational predictions, not direct experimental measurements.",
    "Exact transmembrane boundaries may vary among prediction methods."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for Q59I63 (ADGRG1/GPR56, Zebrafish) lists exactly seven transmembrane helical segments at 371-391, 409-429, 444-464, 472-492, 531-551, 564-586, and 596-618, matching Choice B precisely. The topological domains (extracellular 25-370, cytoplasmic 392-408, extracellular 430-443, etc.) are consistent with a canonical 7-TM GPCR topology. All TM annotations carry evidence code ECO:0000255 (similarity-based/procurable), indicating computational transfer rather than experimental structure, but they are the current database annotations.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C5](#evidence-c5), [C7](#evidence-c7), [C9](#evidence-c9), [C11](#evidence-c11), [C13](#evidence-c13), [C15](#evidence-c15), [C17](#evidence-c17), [H5](#evidence-h5), [H7](#evidence-h7), [H9](#evidence-h9), [H11](#evidence-h11), [H13](#evidence-h13), [H15](#evidence-h15), [H17](#evidence-h17).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Choice A is trivially eliminated because its positions (730, 795, 845, 1111) exceed the 648-residue protein length. Choices B, C, and D all place TM helices in the C-terminal ~250 residues, consistent with the large N-terminal extracellular domain of an adhesion GPCR. The decisive transferable-knowledge step is recognizing the canonical seven-transmembrane-helix architecture of all GPCRs (rhodopsin, beta-adrenergic receptor, and hundreds of solved GPCR structures). This eliminates Choice C, which lists only six TM segments. The remaining B-vs-D distinction is a two-residue difference in TM2 (ending at 429 vs 431). In GPCRs, the extracellular loop 2 (ECL2) between TM2 and TM3 is a short hydrophilic segment that typically contains a conserved cysteine forming a disulfide bond with TM3. A model examining the input sequence at positions 430-431 can assess whether those residues are hydrophobic (extending the helix, favoring D) or hydrophilic/polar (beginning the extracellular loop, favoring B). The alternating TM/loop topology of GPCRs provides a structural framework for identifying the helix-to-loop transition, making this a legitimate sequence-analysis reasoning task rather than a memorization task.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The 7-TM GPCR architecture is a well-established, broadly transferable fact from hundreds of GPCR structures and family-level knowledge. It decisively eliminates A (out-of-range positions) and C (only 6 TMs). The B-vs-D distinction, while fine-grained (2 residues), is answerable by examining hydrophobicity at positions 430-431 in the provided sequence and applying the GPCR topology principle that extracellular loops begin with hydrophilic residues. No fact unique to this exact protein's annotation is strictly necessary.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> A is eliminated by exceeding protein length; C is eliminated by having only 6 TM helices (GPCRs have 7). The B-vs-D difference is only two residues (429 vs 431) in TM2. If residues 430-431 were borderline hydrophobic, both could be argued, but the GPCR extracellular-loop topology (hydrophilic residues, conserved ECL2 cysteine) provides a clear structural rationale for B. No other pair of options is genuinely defensible.


### Important caveats

- All UniProt TM annotations carry evidence code ECO:0000255 (similarity-based/procurable), meaning they are computational predictions transferred from homology, not experimentally determined boundaries. The exact helix termini could shift by 1-2 residues with different prediction algorithms.
- The B-vs-D distinction (2 residues in one of seven helices) is extremely fine-grained. A model relying on approximate hydropathy windows might not reliably resolve this boundary without careful residue-level analysis.
- The protein is an adhesion GPCR (ADGRG1/GPR56) with a large N-terminal extracellular domain (residues 25-370) followed by the 7-TM domain (371-618) and a short cytoplasmic tail (619-648). This architecture is consistent with the adhesion GPCR subfamily but the question does not require identifying the subfamily explicitly.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Choice A is trivially eliminated because its positions (730, 795, 845, 1111) exceed the 648-residue protein length. Choices B, C, and D all place TM helices in the C-terminal ~250 residues, consistent with the large N-terminal extracellular domain of an adhesion GPCR. The decisive transferable-knowledge step is recognizing the canonical seven-transmembrane-helix architecture of all GPCRs (rhodopsin, beta-adrenergic receptor, and hundreds of solved GPCR structures). This eliminates Choice C, which lists only six TM segments. The remaining B-vs-D distinction is a two-residue difference in TM2 (ending at 429 vs 431). In GPCRs, the extracellular loop 2 (ECL2) between TM2 and TM3 is a short hydrophilic segment that typically contains a conserved cysteine forming a disulfide bond with TM3. A model examining the input sequence at positions 430-431 can assess whether those residues are hydrophobic (extending the helix, favoring D) or hydrophilic/polar (beginning the extracellular loop, favoring B). The alternating TM/loop topology of GPCRs provides a structural framework for identifying the helix-to-loop transition, making this a legitimate sequence-analysis reasoning task rather than a memorization task.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The 7-TM GPCR architecture is a well-established, broadly transferable fact from hundreds of GPCR structures and family-level knowledge. It decisively eliminates A (out-of-range positions) and C (only 6 TMs). The B-vs-D distinction, while fine-grained (2 residues), is answerable by examining hydrophobicity at positions 430-431 in the provided sequence and applying the GPCR topology principle that extracellular loops begin with hydrophilic residues. No fact unique to this exact protein's annotation is strictly necessary."
  },
  "case_id": "transmembrane_0097",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C8",
      "C10",
      "C12",
      "C14",
      "C16",
      "C18",
      "C5",
      "C7",
      "C9",
      "C11",
      "C13",
      "C15",
      "C17",
      "H5",
      "H7",
      "H9",
      "H11",
      "H13",
      "H15",
      "H17"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for Q59I63 (ADGRG1/GPR56, Zebrafish) lists exactly seven transmembrane helical segments at 371-391, 409-429, 444-464, 472-492, 531-551, 564-586, and 596-618, matching Choice B precisely. The topological domains (extracellular 25-370, cytoplasmic 392-408, extracellular 430-443, etc.) are consistent with a canonical 7-TM GPCR topology. All TM annotations carry evidence code ECO:0000255 (similarity-based/procurable), indicating computational transfer rather than experimental structure, but they are the current database annotations."
  },
  "important_caveats": [
    "All UniProt TM annotations carry evidence code ECO:0000255 (similarity-based/procurable), meaning they are computational predictions transferred from homology, not experimentally determined boundaries. The exact helix termini could shift by 1-2 residues with different prediction algorithms.",
    "The B-vs-D distinction (2 residues in one of seven helices) is extremely fine-grained. A model relying on approximate hydropathy windows might not reliably resolve this boundary without careful residue-level analysis.",
    "The protein is an adhesion GPCR (ADGRG1/GPR56) with a large N-terminal extracellular domain (residues 25-370) followed by the 7-TM domain (371-618) and a short cytoplasmic tail (619-648). This architecture is consistent with the adhesion GPCR subfamily but the question does not require identifying the subfamily explicitly."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A is eliminated by exceeding protein length; C is eliminated by having only 6 TM helices (GPCRs have 7). The B-vs-D difference is only two residues (429 vs 431) in TM2. If residues 430-431 were borderline hydrophobic, both could be argued, but the GPCR extracellular-loop topology (hydrophilic residues, conserved ECL2 cysteine) provides a clear structural rationale for B. No other pair of options is genuinely defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0097",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for Q59I63 (ADGRG1/GPR56, Zebrafish) lists exactly seven transmembrane helical segments at 371-391, 409-429, 444-464, 472-492, 531-551, 564-586, and 596-618, matching Choice B precisely. The topological domains (extracellular 25-370, cytoplasmic 392-408, extracellular 430-443, etc.) are consistent with a canonical 7-TM GPCR topology. All TM annotations carry evidence code ECO:0000255 (similarity-based/procurable), indicating computational transfer rather than experimental structure, but they are the current database annotations.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "C5", "C7", "C9", "C11", "C13", "C15", "C17", "H5", "H7", "H9", "H11", "H13", "H15", "H17"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Choice A is trivially eliminated because its positions (730, 795, 845, 1111) exceed the 648-residue protein length. Choices B, C, and D all place TM helices in the C-terminal ~250 residues, consistent with the large N-terminal extracellular domain of an adhesion GPCR. The decisive transferable-knowledge step is recognizing the canonical seven-transmembrane-helix architecture of all GPCRs (rhodopsin, beta-adrenergic receptor, and hundreds of solved GPCR structures). This eliminates Choice C, which lists only six TM segments. The remaining B-vs-D distinction is a two-residue difference in TM2 (ending at 429 vs 431). In GPCRs, the extracellular loop 2 (ECL2) between TM2 and TM3 is a short hydrophilic segment that typically contains a conserved cysteine forming a disulfide bond with TM3. A model examining the input sequence at positions 430-431 can assess whether those residues are hydrophobic (extending the helix, favoring D) or hydrophilic/polar (beginning the extracellular loop, favoring B). The alternating TM/loop topology of GPCRs provides a structural framework for identifying the helix-to-loop transition, making this a legitimate sequence-analysis reasoning task rather than a memorization task.",
    "missing_item_specific_fact": "",
    "reason": "The 7-TM GPCR architecture is a well-established, broadly transferable fact from hundreds of GPCR structures and family-level knowledge. It decisively eliminates A (out-of-range positions) and C (only 6 TMs). The B-vs-D distinction, while fine-grained (2 residues), is answerable by examining hydrophobicity at positions 430-431 in the provided sequence and applying the GPCR topology principle that extracellular loops begin with hydrophilic residues. No fact unique to this exact protein's annotation is strictly necessary."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A is eliminated by exceeding protein length; C is eliminated by having only 6 TM helices (GPCRs have 7). The B-vs-D difference is only two residues (429 vs 431) in TM2. If residues 430-431 were borderline hydrophobic, both could be argued, but the GPCR extracellular-loop topology (hydrophilic residues, conserved ECL2 cysteine) provides a clear structural rationale for B. No other pair of options is genuinely defensible."
  },
  "important_caveats": [
    "All UniProt TM annotations carry evidence code ECO:0000255 (similarity-based/procurable), meaning they are computational predictions transferred from homology, not experimentally determined boundaries. The exact helix termini could shift by 1-2 residues with different prediction algorithms.",
    "The B-vs-D distinction (2 residues in one of seven helices) is extremely fine-grained. A model relying on approximate hydropathy windows might not reliably resolve this boundary without careful residue-level analysis.",
    "The protein is an adhesion GPCR (ADGRG1/GPR56) with a large N-terminal extracellular domain (residues 25-370) followed by the 7-TM domain (371-618) and a short cytoplasmic tail (619-648). This architecture is consistent with the adhesion GPCR subfamily but the question does not require identifying the subfamily explicitly."
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
  "benchmark_sequence_length": 648,
  "benchmark_sequence_sha256": "0aeb6f4623306585d8f08066b919f9b296ac122794d0737052b31610ace39de4",
  "current_entry_audit": {
    "entryVersion": 121,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-06-18",
    "sequenceVersion": 2
  },
  "current_record_sha256": "a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 648,
  "current_source_sequence_sha256": "0aeb6f4623306585d8f08066b919f9b296ac122794d0737052b31610ace39de4",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 119,
      "exact_sequence_comparison": "matched",
      "sequence_version": 2
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q59I63",
  "selected_historical_entry_version": 119,
  "selected_historical_record_sha256": "b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0",
  "selected_historical_source_sequence_length": 648,
  "selected_historical_source_sequence_sha256": "0aeb6f4623306585d8f08066b919f9b296ac122794d0737052b31610ace39de4",
  "selected_historical_version": {
    "accession": "Q59I63",
    "database": "Swiss-Prot",
    "entryVersion": 119,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "AGRG1_DANRE",
    "sequenceVersion": 2
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q59I63\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:31:01.992326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe",
  "url": "https://rest.uniprot.org/uniprotkb/Q59I63.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":121,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-06-18\",\"sequenceVersion\":2}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:31:01.992326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe",
  "url": "https://rest.uniprot.org/uniprotkb/Q59I63.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Zebrafish\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Euteleostomi\",\"Actinopterygii\",\"Neopterygii\",\"Teleostei\",\"Ostariophysi\",\"Cypriniformes\",\"Danionidae\",\"Danioninae\",\"Danio\"],\"scientificName\":\"Danio rerio\",\"synonyms\":[\"Brachydanio rerio\"],\"taxonId\":7955}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:31:01.992326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe",
  "url": "https://rest.uniprot.org/uniprotkb/Q59I63.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"25607772\",\"source\":\"PubMed\"}],\"value\":\"G protein-coupled receptor 56\"}}],\"contains\":[{\"alternativeNames\":[{\"fullName\":{\"value\":\"ADGRG1 N-terminal fragment\"},\"shortNames\":[{\"value\":\"ADGRG1 NT\"}]}],\"recommendedName\":{\"fullName\":{\"value\":\"Adhesion G protein-coupled receptor G1, N-terminal fragment\"}}},{\"alternativeNames\":[{\"fullName\":{\"value\":\"ADGRG1 C-terminal fragment\"},\"shortNames\":[{\"value\":\"ADGRG1 CT\"}]}],\"recommendedName\":{\"fullName\":{\"value\":\"Adhesion G protein-coupled receptor G1, C-terminal fragment\"}}}],\"flag\":\"Precursor\",\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Adhesion G protein-coupled receptor G1\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:31:01.992326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe",
  "url": "https://rest.uniprot.org/uniprotkb/Q59I63.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":370},\"start\":{\"modifier\":\"EXACT\",\"value\":25}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:31:01.992326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe",
  "url": "https://rest.uniprot.org/uniprotkb/Q59I63.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":391},\"start\":{\"modifier\":\"EXACT\",\"value\":371}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:31:01.992326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe",
  "url": "https://rest.uniprot.org/uniprotkb/Q59I63.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":408},\"start\":{\"modifier\":\"EXACT\",\"value\":392}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:31:01.992326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe",
  "url": "https://rest.uniprot.org/uniprotkb/Q59I63.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":429},\"start\":{\"modifier\":\"EXACT\",\"value\":409}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:31:01.992326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe",
  "url": "https://rest.uniprot.org/uniprotkb/Q59I63.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":443},\"start\":{\"modifier\":\"EXACT\",\"value\":430}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:31:01.992326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe",
  "url": "https://rest.uniprot.org/uniprotkb/Q59I63.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":464},\"start\":{\"modifier\":\"EXACT\",\"value\":444}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-02T04:31:01.992326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe",
  "url": "https://rest.uniprot.org/uniprotkb/Q59I63.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":471},\"start\":{\"modifier\":\"EXACT\",\"value\":465}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-02T04:31:01.992326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe",
  "url": "https://rest.uniprot.org/uniprotkb/Q59I63.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":492},\"start\":{\"modifier\":\"EXACT\",\"value\":472}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/11",
  "retrieved_utc": "2026-11-02T04:31:01.992326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe",
  "url": "https://rest.uniprot.org/uniprotkb/Q59I63.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":530},\"start\":{\"modifier\":\"EXACT\",\"value\":493}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/12",
  "retrieved_utc": "2026-11-02T04:31:01.992326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe",
  "url": "https://rest.uniprot.org/uniprotkb/Q59I63.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":551},\"start\":{\"modifier\":\"EXACT\",\"value\":531}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/13",
  "retrieved_utc": "2026-11-02T04:31:01.992326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe",
  "url": "https://rest.uniprot.org/uniprotkb/Q59I63.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":563},\"start\":{\"modifier\":\"EXACT\",\"value\":552}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/14",
  "retrieved_utc": "2026-11-02T04:31:01.992326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe",
  "url": "https://rest.uniprot.org/uniprotkb/Q59I63.json"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)

```json
{
  "evidence_id": "C16",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":586},\"start\":{\"modifier\":\"EXACT\",\"value\":564}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/15",
  "retrieved_utc": "2026-11-02T04:31:01.992326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe",
  "url": "https://rest.uniprot.org/uniprotkb/Q59I63.json"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)

```json
{
  "evidence_id": "C17",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":595},\"start\":{\"modifier\":\"EXACT\",\"value\":587}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/16",
  "retrieved_utc": "2026-11-02T04:31:01.992326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe",
  "url": "https://rest.uniprot.org/uniprotkb/Q59I63.json"
}
```

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)

```json
{
  "evidence_id": "C18",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":618},\"start\":{\"modifier\":\"EXACT\",\"value\":596}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/17",
  "retrieved_utc": "2026-11-02T04:31:01.992326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe",
  "url": "https://rest.uniprot.org/uniprotkb/Q59I63.json"
}
```

### Evidence C19

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)

```json
{
  "evidence_id": "C19",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":648},\"start\":{\"modifier\":\"EXACT\",\"value\":619}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/18",
  "retrieved_utc": "2026-11-02T04:31:01.992326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe",
  "url": "https://rest.uniprot.org/uniprotkb/Q59I63.json"
}
```

### Evidence C20

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)

```json
{
  "evidence_id": "C20",
  "excerpt": "{\"citation\":{\"authors\":[\"Ackerman S.D.\",\"Garcia C.\",\"Piao X.\",\"Gutmann D.H.\",\"Monk K.R.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"25607772\"},{\"database\":\"DOI\",\"id\":\"10.1038/ncomms7122\"}],\"citationType\":\"journal article\",\"firstPage\":\"6122\",\"id\":\"25607772\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"6122\",\"publicationDate\":\"2015\",\"title\":\"The adhesion GPCR Gpr56 regulates oligodendrocyte development via interactions with Galpha12/13 and RhoA.\",\"volume\":\"6\"},\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"DEVELOPMENTAL STAGE\",\"DISRUPTION PHENOTYPE\",\"MUTAGENESIS OF 325-ASN-TRP-326\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:31:01.992326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe",
  "url": "https://rest.uniprot.org/uniprotkb/Q59I63.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)

```json
{
  "entry_version": 119,
  "evidence_id": "H1",
  "excerpt": "ID   AGRG1_DANRE             Reviewed;         648 AA.\nAC   Q59I63; A0A0R4IXA8; A0A8M2BDY6; F1QZM9;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-JUN-2025, sequence version 2.\nDT   28-JAN-2026, entry version 119.\nDE   RecName: Full=Adhesion G-protein coupled receptor G1 {ECO:0000305};\nDE   AltName: Full=G-protein coupled receptor 56 {ECO:0000303|PubMed:25607772};\nDE   Contains:\nDE     RecName: Full=Adhesion G-protein coupled receptor G1, N-terminal fragment;\nDE     AltName: Full=ADGRG1 N-terminal fragment;\nDE              Short=ADGRG1 NT;\nDE   Contains:\nDE     RecName: Full=Adhesion G-protein coupled receptor G1, C-terminal fragment;\nDE     AltName: Full=ADGRG1 C-terminal fragment;\nDE              Short=ADGRG1 CT;\nDE   Flags: Precursor;\nGN   Name=adgrg1 {ECO:0000303|PubMed:29367382,\nGN   ECO:0000312|ZFIN:ZDB-GENE-030131-3671};\nGN   Synonyms=gpr56 {ECO:0000303|PubMed:25607772};\nOS   Danio rerio (Zebrafish) (Brachydanio rerio).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi;\nOC   Actinopterygii; Neopterygii; Teleostei; Ostariophysi; Cypriniformes;\nOC   Danionidae; Danioninae; Danio.\nOX   NCBI_TaxID=7955;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:04.584714+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-24",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0",
  "url": "https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)

```json
{
  "entry_version": 119,
  "evidence_id": "H2",
  "excerpt": "RN   [3]\nRP   FUNCTION, DEVELOPMENTAL STAGE, DISRUPTION PHENOTYPE, AND MUTAGENESIS OF\nRP   325-ASN-TRP-326.\nRX   PubMed=25607772; DOI=10.1038/ncomms7122;\nRA   Ackerman S.D., Garcia C., Piao X., Gutmann D.H., Monk K.R.;\nRT   \"The adhesion GPCR Gpr56 regulates oligodendrocyte development via\nRT   interactions with Galpha12/13 and RhoA.\";\nRL   Nat. Commun. 6:6122-6122(2015).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:04.584714+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 70-77",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0",
  "url": "https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)

```json
{
  "entry_version": 119,
  "evidence_id": "H3",
  "excerpt": "RN   [4]\nRP   FUNCTION.\nRX   PubMed=29367382; DOI=10.1084/jem.20161714;\nRA   Ackerman S.D., Luo R., Poitelon Y., Mogha A., Harty B.L., D'Rozario M.,\nRA   Sanchez N.E., Lakkaraju A.K.K., Gamble P., Li J., Qu J., MacEwan M.R.,\nRA   Ray W.Z., Aguzzi A., Feltri M.L., Piao X., Monk K.R.;\nRT   \"GPR56/ADGRG1 regulates development and maintenance of peripheral myelin.\";\nRL   J. Exp. Med. 215:941-961(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:04.584714+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 78-85",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0",
  "url": "https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)

```json
{
  "entry_version": 119,
  "evidence_id": "H4",
  "excerpt": "FT   TOPO_DOM        25..370\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:04.584714+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 211-213",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0",
  "url": "https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)

```json
{
  "entry_version": 119,
  "evidence_id": "H5",
  "excerpt": "FT   TRANSMEM        371..391\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:04.584714+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 214-216",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0",
  "url": "https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)

```json
{
  "entry_version": 119,
  "evidence_id": "H6",
  "excerpt": "FT   TOPO_DOM        392..408\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:04.584714+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 217-219",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0",
  "url": "https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)

```json
{
  "entry_version": 119,
  "evidence_id": "H7",
  "excerpt": "FT   TRANSMEM        409..429\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:04.584714+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 220-222",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0",
  "url": "https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)

```json
{
  "entry_version": 119,
  "evidence_id": "H8",
  "excerpt": "FT   TOPO_DOM        430..443\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:04.584714+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 223-225",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0",
  "url": "https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)

```json
{
  "entry_version": 119,
  "evidence_id": "H9",
  "excerpt": "FT   TRANSMEM        444..464\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:04.584714+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 226-228",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0",
  "url": "https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)

```json
{
  "entry_version": 119,
  "evidence_id": "H10",
  "excerpt": "FT   TOPO_DOM        465..471\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:04.584714+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 229-231",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0",
  "url": "https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)

```json
{
  "entry_version": 119,
  "evidence_id": "H11",
  "excerpt": "FT   TRANSMEM        472..492\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:04.584714+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 232-234",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0",
  "url": "https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)

```json
{
  "entry_version": 119,
  "evidence_id": "H12",
  "excerpt": "FT   TOPO_DOM        493..530\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:04.584714+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 235-237",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0",
  "url": "https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)

```json
{
  "entry_version": 119,
  "evidence_id": "H13",
  "excerpt": "FT   TRANSMEM        531..551\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:04.584714+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 238-240",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0",
  "url": "https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)

```json
{
  "entry_version": 119,
  "evidence_id": "H14",
  "excerpt": "FT   TOPO_DOM        552..563\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:04.584714+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 241-243",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0",
  "url": "https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119"
}
```

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)

```json
{
  "entry_version": 119,
  "evidence_id": "H15",
  "excerpt": "FT   TRANSMEM        564..586\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:04.584714+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 244-246",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0",
  "url": "https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119"
}
```

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)

```json
{
  "entry_version": 119,
  "evidence_id": "H16",
  "excerpt": "FT   TOPO_DOM        587..595\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:04.584714+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 247-249",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0",
  "url": "https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119"
}
```

### Evidence H17

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)

```json
{
  "entry_version": 119,
  "evidence_id": "H17",
  "excerpt": "FT   TRANSMEM        596..618\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:04.584714+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 250-252",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0",
  "url": "https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119"
}
```

### Evidence H18

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)

```json
{
  "entry_version": 119,
  "evidence_id": "H18",
  "excerpt": "FT   TOPO_DOM        619..648\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:04.584714+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 253-255",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0",
  "url": "https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 97. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
