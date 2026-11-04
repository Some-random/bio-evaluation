# transmembrane_0021

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0021.txt)

**Task:** `transmembrane`  
**Expected answer:** **B** — 9..45; 50..80; 86..121; 130..156; 173..210; 215..250; 261..289

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MCNVSQDSCNIDSRLDSLFPPTLYIFVMVIGFPTNCLSLWAAFVQVRQKNELGVYLLNLSISDLLYIATLPPWVNYFLHQDNWIHGPESCKLFGFILYTNIYISIGFLSCISVDRYLAVAHPLKFAKVRRVKTAAVVSAVVWAIEIGANSAPLFHNELFEDRFNHTFCFEKYPMEDWVAQMNLYRVFVGFLFPWVLMLFCYQGILRAVKTNVSTEREEKAKIKRLALSLIAILLFCFAPYHLILLSRSVVYLGQPCDCTFEENIFTAYHVSLALTSLNCVADPILYCLANEGARSEVTRGLAPLMKFFSASRPNMDSFARSVTLDTPWSSRRAAAPSPRSWSLCGQTGGRGRRSRVRRRRDCKC

[Multiple Choices]
A. 50..80; 86..121; 130..156; 173..210; 215..250; 261..289
B. 9..45; 50..80; 86..121; 130..156; 173..210; 215..250; 261..289
C. 9..45; 54..80; 86..121; 130..156; 173..210; 215..250; 261..289
D. 305..325
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

> The sequence-matched historical UniProt record annotates all seven listed intervals in B as transmembrane regions. These annotations are transferred by similarity from another protein (ECO:0000250), so they support the key as a database annotation but are not direct experimental validation of every boundary.

Citations as saved: [H4](#evidence-h4), [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The strongly hydrophobic stretches and seven-helix GPCR-like pattern support a seven-transmembrane protein and distinguish the seven-helix choices from D, and from A's omission of the first helix. But B and C differ only in the start of the second interval. The sequence has a polar NELG stretch before the more hydrophobic portion, so general hydropathy does not meaningfully establish that the interval should start at 50 rather than 54.


**Missing item-specific fact**

> A reliable boundary assignment for the second transmembrane helix in this protein or a sufficiently close homolog is needed to choose between the 50 and 54 starts.


**Reason**

> Transferable GPCR and hydropathy knowledge supports the overall topology, but does not resolve the close boundary choice that distinguishes the keyed option B from C. The evidence favoring B is a similarity-transferred annotation, a target-specific boundary fact not supplied in the original input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> Both options include the same seven predicted helices and differ only in whether the second interval begins at 50 or 54. Given the polar residues preceding its hydrophobic core and the lack of an experimentally established boundary in the supplied input, either boundary convention is defensible.


### Important caveats

- The supplied sequence matches the historical and current UniProt sequence, but the cited transmembrane annotations are similarity-based rather than direct experimental measurements.
- The exact endpoints of predicted transmembrane helices can depend on annotation convention; the source annotation supports B without independently proving that its boundaries are uniquely correct.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The strongly hydrophobic stretches and seven-helix GPCR-like pattern support a seven-transmembrane protein and distinguish the seven-helix choices from D, and from A's omission of the first helix. But B and C differ only in the start of the second interval. The sequence has a polar NELG stretch before the more hydrophobic portion, so general hydropathy does not meaningfully establish that the interval should start at 50 rather than 54.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "A reliable boundary assignment for the second transmembrane helix in this protein or a sufficiently close homolog is needed to choose between the 50 and 54 starts.",
    "reason": "Transferable GPCR and hydropathy knowledge supports the overall topology, but does not resolve the close boundary choice that distinguishes the keyed option B from C. The evidence favoring B is a similarity-transferred annotation, a target-specific boundary fact not supplied in the original input."
  },
  "case_id": "transmembrane_0021",
  "expected_answer_check": {
    "evidence_ids": [
      "H4",
      "H6",
      "H8",
      "H10",
      "H12",
      "H14",
      "H16"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record annotates all seven listed intervals in B as transmembrane regions. These annotations are transferred by similarity from another protein (ECO:0000250), so they support the key as a database annotation but are not direct experimental validation of every boundary."
  },
  "important_caveats": [
    "The supplied sequence matches the historical and current UniProt sequence, but the cited transmembrane annotations are similarity-based rather than direct experimental measurements.",
    "The exact endpoints of predicted transmembrane helices can depend on annotation convention; the source annotation supports B without independently proving that its boundaries are uniquely correct."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "Both options include the same seven predicted helices and differ only in whether the second interval begins at 50 or 54. Given the polar residues preceding its hydrophobic core and the lack of an experimentally established boundary in the supplied input, either boundary convention is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0021",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record annotates all seven listed intervals in B as transmembrane regions. These annotations are transferred by similarity from another protein (ECO:0000250), so they support the key as a database annotation but are not direct experimental validation of every boundary.",
    "evidence_ids": ["H4", "H6", "H8", "H10", "H12", "H14", "H16"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The strongly hydrophobic stretches and seven-helix GPCR-like pattern support a seven-transmembrane protein and distinguish the seven-helix choices from D, and from A's omission of the first helix. But B and C differ only in the start of the second interval. The sequence has a polar NELG stretch before the more hydrophobic portion, so general hydropathy does not meaningfully establish that the interval should start at 50 rather than 54.",
    "missing_item_specific_fact": "A reliable boundary assignment for the second transmembrane helix in this protein or a sufficiently close homolog is needed to choose between the 50 and 54 starts.",
    "reason": "Transferable GPCR and hydropathy knowledge supports the overall topology, but does not resolve the close boundary choice that distinguishes the keyed option B from C. The evidence favoring B is a similarity-transferred annotation, a target-specific boundary fact not supplied in the original input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "Both options include the same seven predicted helices and differ only in whether the second interval begins at 50 or 54. Given the polar residues preceding its hydrophobic core and the lack of an experimentally established boundary in the supplied input, either boundary convention is defensible."
  },
  "important_caveats": [
    "The supplied sequence matches the historical and current UniProt sequence, but the cited transmembrane annotations are similarity-based rather than direct experimental measurements.",
    "The exact endpoints of predicted transmembrane helices can depend on annotation convention; the source annotation supports B without independently proving that its boundaries are uniquely correct."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for A0A4W3GG95 (GPR4_CALMI, ghost shark GPCR) lists exactly seven transmembrane helices at 9..45, 50..80, 86..121, 130..156, 173..210, 215..250, and 261..289, which matches option B verbatim. The evidence codes are ECO:0000250 (similarity to A0A6I8PUB9), indicating computational transfer rather than direct experimental determination, but the annotation is consistent with the sequence being a canonical 7-TM GPCR.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [H4](#evidence-h4), [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence (364 aa) contains seven long hydrophobic stretches (~20-37 residues) in a pattern characteristic of a 7-transmembrane GPCR. The N-terminal region (positions 9-45: 'LYIFVMVIGFPTNCLSLWAAFVQVRQKNELGVYLLNLSISDLLYIATLPPWVNYFL') is strongly hydrophobic, confirming TM1 exists and eliminating option A (which omits it). Option D (a single 21-residue segment at 305-325) is inconsistent with any multi-pass membrane protein topology. The remaining seven-helix pattern (TM1 through TM7) matches both B and C. The 4-residue difference in TM2 start (50 vs 54) is within the typical boundary uncertainty of hydrophobicity-based TM prediction; GPCR TM helices commonly include a few polar residues at their edges, and the short 4-residue cytoplasmic loop (46-49) between TM1 and TM2 is consistent with the compact first loop seen in many GPCRs. A model applying GPCR topology knowledge and hydrophobicity analysis would identify the seven-region answer and select B as the most complete annotation, though C is a close alternative.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable knowledge of GPCR 7-TM architecture, hydrophobicity-based TM helix identification, and the characteristic short loops between helices allows a knowledgeable model to eliminate D (single short segment) and A (missing clearly hydrophobic TM1), and to identify the seven-region pattern. The B vs C distinction (TM2 start at 50 vs 54) is a 4-residue boundary difference well within the resolution of standard TM prediction tools; GPCR-specific knowledge that TM helix boundaries often include edge polar residues supports B. The overall inference is a defensible probabilistic generalization from GPCR family knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> Options B and C differ only in the start position of TM2 (50 vs 54). Residues 50-53 (N, E, L, G) include polar/charged amino acids that a simple hydrophobicity predictor might exclude from the helix, favoring C. However, GPCR structural conventions and the UniProt annotation place the boundary at 50, favoring B. The 4-residue difference is within the typical ±3-5 residue uncertainty of TM boundary predictions, making both options defensible without the exact database annotation.


### Important caveats

- All UniProt TM annotations carry evidence code ECO:0000250 (similarity to A0A6I8PUB9), meaning they are computational transfers, not direct experimental measurements of this specific protein.
- The B vs C distinction (TM2 start 50 vs 54) is a 4-residue boundary issue that is at the edge of what hydrophobicity analysis can reliably resolve; a model might reasonably choose C based on the polar N/E residues at positions 50-51.
- The reviewer-only evidence confirms the sequence matches the benchmark (SHA256 match), but the accession and organism identity were not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence (364 aa) contains seven long hydrophobic stretches (~20-37 residues) in a pattern characteristic of a 7-transmembrane GPCR. The N-terminal region (positions 9-45: 'LYIFVMVIGFPTNCLSLWAAFVQVRQKNELGVYLLNLSISDLLYIATLPPWVNYFL') is strongly hydrophobic, confirming TM1 exists and eliminating option A (which omits it). Option D (a single 21-residue segment at 305-325) is inconsistent with any multi-pass membrane protein topology. The remaining seven-helix pattern (TM1 through TM7) matches both B and C. The 4-residue difference in TM2 start (50 vs 54) is within the typical boundary uncertainty of hydrophobicity-based TM prediction; GPCR TM helices commonly include a few polar residues at their edges, and the short 4-residue cytoplasmic loop (46-49) between TM1 and TM2 is consistent with the compact first loop seen in many GPCRs. A model applying GPCR topology knowledge and hydrophobicity analysis would identify the seven-region answer and select B as the most complete annotation, though C is a close alternative.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of GPCR 7-TM architecture, hydrophobicity-based TM helix identification, and the characteristic short loops between helices allows a knowledgeable model to eliminate D (single short segment) and A (missing clearly hydrophobic TM1), and to identify the seven-region pattern. The B vs C distinction (TM2 start at 50 vs 54) is a 4-residue boundary difference well within the resolution of standard TM prediction tools; GPCR-specific knowledge that TM helix boundaries often include edge polar residues supports B. The overall inference is a defensible probabilistic generalization from GPCR family knowledge."
  },
  "case_id": "transmembrane_0021",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C8",
      "C10",
      "C12",
      "C14",
      "C16",
      "C18",
      "H4",
      "H6",
      "H8",
      "H10",
      "H12",
      "H14",
      "H16"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for A0A4W3GG95 (GPR4_CALMI, ghost shark GPCR) lists exactly seven transmembrane helices at 9..45, 50..80, 86..121, 130..156, 173..210, 215..250, and 261..289, which matches option B verbatim. The evidence codes are ECO:0000250 (similarity to A0A6I8PUB9), indicating computational transfer rather than direct experimental determination, but the annotation is consistent with the sequence being a canonical 7-TM GPCR."
  },
  "important_caveats": [
    "All UniProt TM annotations carry evidence code ECO:0000250 (similarity to A0A6I8PUB9), meaning they are computational transfers, not direct experimental measurements of this specific protein.",
    "The B vs C distinction (TM2 start 50 vs 54) is a 4-residue boundary issue that is at the edge of what hydrophobicity analysis can reliably resolve; a model might reasonably choose C based on the polar N/E residues at positions 50-51.",
    "The reviewer-only evidence confirms the sequence matches the benchmark (SHA256 match), but the accession and organism identity were not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "Options B and C differ only in the start position of TM2 (50 vs 54). Residues 50-53 (N, E, L, G) include polar/charged amino acids that a simple hydrophobicity predictor might exclude from the helix, favoring C. However, GPCR structural conventions and the UniProt annotation place the boundary at 50, favoring B. The 4-residue difference is within the typical ±3-5 residue uncertainty of TM boundary predictions, making both options defensible without the exact database annotation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0021",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for A0A4W3GG95 (GPR4_CALMI, ghost shark GPCR) lists exactly seven transmembrane helices at 9..45, 50..80, 86..121, 130..156, 173..210, 215..250, and 261..289, which matches option B verbatim. The evidence codes are ECO:0000250 (similarity to A0A6I8PUB9), indicating computational transfer rather than direct experimental determination, but the annotation is consistent with the sequence being a canonical 7-TM GPCR.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "H4", "H6", "H8", "H10", "H12", "H14", "H16"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence (364 aa) contains seven long hydrophobic stretches (~20-37 residues) in a pattern characteristic of a 7-transmembrane GPCR. The N-terminal region (positions 9-45: 'LYIFVMVIGFPTNCLSLWAAFVQVRQKNELGVYLLNLSISDLLYIATLPPWVNYFL') is strongly hydrophobic, confirming TM1 exists and eliminating option A (which omits it). Option D (a single 21-residue segment at 305-325) is inconsistent with any multi-pass membrane protein topology. The remaining seven-helix pattern (TM1 through TM7) matches both B and C. The 4-residue difference in TM2 start (50 vs 54) is within the typical boundary uncertainty of hydrophobicity-based TM prediction; GPCR TM helices commonly include a few polar residues at their edges, and the short 4-residue cytoplasmic loop (46-49) between TM1 and TM2 is consistent with the compact first loop seen in many GPCRs. A model applying GPCR topology knowledge and hydrophobicity analysis would identify the seven-region answer and select B as the most complete annotation, though C is a close alternative.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of GPCR 7-TM architecture, hydrophobicity-based TM helix identification, and the characteristic short loops between helices allows a knowledgeable model to eliminate D (single short segment) and A (missing clearly hydrophobic TM1), and to identify the seven-region pattern. The B vs C distinction (TM2 start at 50 vs 54) is a 4-residue boundary difference well within the resolution of standard TM prediction tools; GPCR-specific knowledge that TM helix boundaries often include edge polar residues supports B. The overall inference is a defensible probabilistic generalization from GPCR family knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "Options B and C differ only in the start position of TM2 (50 vs 54). Residues 50-53 (N, E, L, G) include polar/charged amino acids that a simple hydrophobicity predictor might exclude from the helix, favoring C. However, GPCR structural conventions and the UniProt annotation place the boundary at 50, favoring B. The 4-residue difference is within the typical ±3-5 residue uncertainty of TM boundary predictions, making both options defensible without the exact database annotation."
  },
  "important_caveats": [
    "All UniProt TM annotations carry evidence code ECO:0000250 (similarity to A0A6I8PUB9), meaning they are computational transfers, not direct experimental measurements of this specific protein.",
    "The B vs C distinction (TM2 start 50 vs 54) is a 4-residue boundary issue that is at the edge of what hydrophobicity analysis can reliably resolve; a model might reasonably choose C based on the polar N/E residues at positions 50-51.",
    "The reviewer-only evidence confirms the sequence matches the benchmark (SHA256 match), but the accession and organism identity were not available to the evaluated model."
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
  "benchmark_sequence_length": 364,
  "benchmark_sequence_sha256": "88f0ec3e6dea24c8c4b72e89d3e6620b7b87a9adc05a94bbbf04f8d014910ea7",
  "current_entry_audit": {
    "entryVersion": 32,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2019-09-18",
    "sequenceVersion": 1
  },
  "current_record_sha256": "a92b2a2611b3e831e67c290051c3b607ae4d71a21502ae38da2c507908426245",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 364,
  "current_source_sequence_sha256": "88f0ec3e6dea24c8c4b72e89d3e6620b7b87a9adc05a94bbbf04f8d014910ea7",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 30,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A4W3GG95",
  "selected_historical_entry_version": 30,
  "selected_historical_record_sha256": "2de235f5ecdbc32faad1779acf9f8307edf330e58265fd2df418707701078865",
  "selected_historical_source_sequence_length": 364,
  "selected_historical_source_sequence_sha256": "88f0ec3e6dea24c8c4b72e89d3e6620b7b87a9adc05a94bbbf04f8d014910ea7",
  "selected_historical_version": {
    "accession": "A0A4W3GG95",
    "database": "Swiss-Prot",
    "entryVersion": 30,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "GPR4_CALMI",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A4W3GG95\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:47.202623+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a92b2a2611b3e831e67c290051c3b607ae4d71a21502ae38da2c507908426245",
  "url": "https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":32,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2019-09-18\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:47.202623+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a92b2a2611b3e831e67c290051c3b607ae4d71a21502ae38da2c507908426245",
  "url": "https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Ghost shark\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Chondrichthyes\",\"Holocephali\",\"Chimaeriformes\",\"Callorhinchidae\",\"Callorhinchus\"],\"scientificName\":\"Callorhinchus milii\",\"taxonId\":7868}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:47.202623+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a92b2a2611b3e831e67c290051c3b607ae4d71a21502ae38da2c507908426245",
  "url": "https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"G protein-coupled receptor 4\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39753131\",\"source\":\"PubMed\"}],\"value\":\"cmGPR4\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:47.202623+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a92b2a2611b3e831e67c290051c3b607ae4d71a21502ae38da2c507908426245",
  "url": "https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A6I8PUB9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":8},\"start\":{\"modifier\":\"EXACT\",\"value\":1}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-01T06:24:47.202623+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a92b2a2611b3e831e67c290051c3b607ae4d71a21502ae38da2c507908426245",
  "url": "https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical; Name=1\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A6I8PUB9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":45},\"start\":{\"modifier\":\"EXACT\",\"value\":9}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-01T06:24:47.202623+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a92b2a2611b3e831e67c290051c3b607ae4d71a21502ae38da2c507908426245",
  "url": "https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A6I8PUB9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":49},\"start\":{\"modifier\":\"EXACT\",\"value\":46}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-01T06:24:47.202623+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a92b2a2611b3e831e67c290051c3b607ae4d71a21502ae38da2c507908426245",
  "url": "https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Helical; Name=2\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A6I8PUB9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":80},\"start\":{\"modifier\":\"EXACT\",\"value\":50}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-01T06:24:47.202623+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a92b2a2611b3e831e67c290051c3b607ae4d71a21502ae38da2c507908426245",
  "url": "https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A6I8PUB9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":85},\"start\":{\"modifier\":\"EXACT\",\"value\":81}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-01T06:24:47.202623+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a92b2a2611b3e831e67c290051c3b607ae4d71a21502ae38da2c507908426245",
  "url": "https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"Helical; Name=3\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A6I8PUB9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":121},\"start\":{\"modifier\":\"EXACT\",\"value\":86}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-01T06:24:47.202623+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a92b2a2611b3e831e67c290051c3b607ae4d71a21502ae38da2c507908426245",
  "url": "https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A6I8PUB9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":129},\"start\":{\"modifier\":\"EXACT\",\"value\":122}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-01T06:24:47.202623+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a92b2a2611b3e831e67c290051c3b607ae4d71a21502ae38da2c507908426245",
  "url": "https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"Helical; Name=4\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A6I8PUB9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":156},\"start\":{\"modifier\":\"EXACT\",\"value\":130}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-01T06:24:47.202623+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a92b2a2611b3e831e67c290051c3b607ae4d71a21502ae38da2c507908426245",
  "url": "https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A6I8PUB9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":172},\"start\":{\"modifier\":\"EXACT\",\"value\":157}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-01T06:24:47.202623+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a92b2a2611b3e831e67c290051c3b607ae4d71a21502ae38da2c507908426245",
  "url": "https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"description\":\"Helical; Name=5\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A6I8PUB9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":210},\"start\":{\"modifier\":\"EXACT\",\"value\":173}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-01T06:24:47.202623+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a92b2a2611b3e831e67c290051c3b607ae4d71a21502ae38da2c507908426245",
  "url": "https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A6I8PUB9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":214},\"start\":{\"modifier\":\"EXACT\",\"value\":211}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/11",
  "retrieved_utc": "2026-11-01T06:24:47.202623+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a92b2a2611b3e831e67c290051c3b607ae4d71a21502ae38da2c507908426245",
  "url": "https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json)

```json
{
  "evidence_id": "C16",
  "excerpt": "{\"description\":\"Helical; Name=6\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A6I8PUB9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":250},\"start\":{\"modifier\":\"EXACT\",\"value\":215}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/12",
  "retrieved_utc": "2026-11-01T06:24:47.202623+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a92b2a2611b3e831e67c290051c3b607ae4d71a21502ae38da2c507908426245",
  "url": "https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json)

```json
{
  "evidence_id": "C17",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A6I8PUB9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":260},\"start\":{\"modifier\":\"EXACT\",\"value\":251}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/13",
  "retrieved_utc": "2026-11-01T06:24:47.202623+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a92b2a2611b3e831e67c290051c3b607ae4d71a21502ae38da2c507908426245",
  "url": "https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json"
}
```

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json)

```json
{
  "evidence_id": "C18",
  "excerpt": "{\"description\":\"Helical; Name=7\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A6I8PUB9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":289},\"start\":{\"modifier\":\"EXACT\",\"value\":261}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/14",
  "retrieved_utc": "2026-11-01T06:24:47.202623+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a92b2a2611b3e831e67c290051c3b607ae4d71a21502ae38da2c507908426245",
  "url": "https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json"
}
```

### Evidence C19

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json)

```json
{
  "evidence_id": "C19",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A6I8PUB9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":364},\"start\":{\"modifier\":\"EXACT\",\"value\":290}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/15",
  "retrieved_utc": "2026-11-01T06:24:47.202623+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a92b2a2611b3e831e67c290051c3b607ae4d71a21502ae38da2c507908426245",
  "url": "https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json"
}
```

### Evidence C20

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json)

```json
{
  "evidence_id": "C20",
  "excerpt": "{\"citation\":{\"authors\":[\"Wen X.\",\"Shang P.\",\"Chen H.\",\"Guo L.\",\"Rong N.\",\"Jiang X.\",\"Li X.\",\"Liu J.\",\"Yang G.\",\"Zhang J.\",\"Zhu K.\",\"Meng Q.\",\"He X.\",\"Wang Z.\",\"Liu Z.\",\"Cheng H.\",\"Zheng Y.\",\"Zhang B.\",\"Pang J.\",\"Liu Z.\",\"Xiao P.\",\"Chen Y.\",\"Liu L.\",\"Luo F.\",\"Yu X.\",\"Yi F.\",\"Zhang P.\",\"Yang F.\",\"Deng C.\",\"Sun J.P.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39753131\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.cell.2024.12.001\"}],\"citationType\":\"journal article\",\"firstPage\":\"653\",\"id\":\"39753131\",\"journal\":\"Cell\",\"lastPage\":\"670\",\"publicationDate\":\"2025\",\"title\":\"Evolutionary study and structural basis of proton sensing by Mus GPR4 and Xenopus GPR4.\",\"volume\":\"188\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"MUTAGENESIS OF GLU-51; VAL-119; PRO-122 AND LEU-123\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:24:47.202623+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a92b2a2611b3e831e67c290051c3b607ae4d71a21502ae38da2c507908426245",
  "url": "https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A4W3GG95?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H1",
  "excerpt": "ID   GPR4_CALMI              Reviewed;         364 AA.\nAC   A0A4W3GG95;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-SEP-2019, sequence version 1.\nDT   28-JAN-2026, entry version 30.\nDE   RecName: Full=G-protein coupled receptor 4 {ECO:0000305};\nDE            Short=cmGPR4 {ECO:0000303|PubMed:39753131};\nGN   Name=gpr4 {ECO:0000303|PubMed:39753131};\nOS   Callorhinchus milii (Ghost shark).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Chondrichthyes;\nOC   Holocephali; Chimaeriformes; Callorhinchidae; Callorhinchus.\nOX   NCBI_TaxID=7868;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.027017+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2de235f5ecdbc32faad1779acf9f8307edf330e58265fd2df418707701078865",
  "url": "https://rest.uniprot.org/unisave/A0A4W3GG95?format=txt&versions=30"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A4W3GG95?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, AND MUTAGENESIS OF GLU-51; VAL-119; PRO-122 AND LEU-123.\nRX   PubMed=39753131; DOI=10.1016/j.cell.2024.12.001;\nRA   Wen X., Shang P., Chen H., Guo L., Rong N., Jiang X., Li X., Liu J.,\nRA   Yang G., Zhang J., Zhu K., Meng Q., He X., Wang Z., Liu Z., Cheng H.,\nRA   Zheng Y., Zhang B., Pang J., Liu Z., Xiao P., Chen Y., Liu L., Luo F.,\nRA   Yu X., Yi F., Zhang P., Yang F., Deng C., Sun J.P.;\nRT   \"Evolutionary study and structural basis of proton sensing by Mus GPR4 and\nRT   Xenopus GPR4.\";\nRL   Cell 188:653-670(2025).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.027017+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 21-30",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2de235f5ecdbc32faad1779acf9f8307edf330e58265fd2df418707701078865",
  "url": "https://rest.uniprot.org/unisave/A0A4W3GG95?format=txt&versions=30"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A4W3GG95?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H3",
  "excerpt": "FT   TOPO_DOM        1..8\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:A0A6I8PUB9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.027017+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 89-91",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2de235f5ecdbc32faad1779acf9f8307edf330e58265fd2df418707701078865",
  "url": "https://rest.uniprot.org/unisave/A0A4W3GG95?format=txt&versions=30"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A4W3GG95?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H4",
  "excerpt": "FT   TRANSMEM        9..45\nFT                   /note=\"Helical; Name=1\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:A0A6I8PUB9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.027017+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 92-94",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2de235f5ecdbc32faad1779acf9f8307edf330e58265fd2df418707701078865",
  "url": "https://rest.uniprot.org/unisave/A0A4W3GG95?format=txt&versions=30"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A4W3GG95?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H5",
  "excerpt": "FT   TOPO_DOM        46..49\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:A0A6I8PUB9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.027017+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 95-97",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2de235f5ecdbc32faad1779acf9f8307edf330e58265fd2df418707701078865",
  "url": "https://rest.uniprot.org/unisave/A0A4W3GG95?format=txt&versions=30"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A4W3GG95?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H6",
  "excerpt": "FT   TRANSMEM        50..80\nFT                   /note=\"Helical; Name=2\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:A0A6I8PUB9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.027017+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 98-100",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2de235f5ecdbc32faad1779acf9f8307edf330e58265fd2df418707701078865",
  "url": "https://rest.uniprot.org/unisave/A0A4W3GG95?format=txt&versions=30"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A4W3GG95?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H7",
  "excerpt": "FT   TOPO_DOM        81..85\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:A0A6I8PUB9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.027017+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 101-103",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2de235f5ecdbc32faad1779acf9f8307edf330e58265fd2df418707701078865",
  "url": "https://rest.uniprot.org/unisave/A0A4W3GG95?format=txt&versions=30"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A4W3GG95?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H8",
  "excerpt": "FT   TRANSMEM        86..121\nFT                   /note=\"Helical; Name=3\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:A0A6I8PUB9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.027017+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 104-106",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2de235f5ecdbc32faad1779acf9f8307edf330e58265fd2df418707701078865",
  "url": "https://rest.uniprot.org/unisave/A0A4W3GG95?format=txt&versions=30"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A4W3GG95?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H9",
  "excerpt": "FT   TOPO_DOM        122..129\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:A0A6I8PUB9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.027017+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 107-109",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2de235f5ecdbc32faad1779acf9f8307edf330e58265fd2df418707701078865",
  "url": "https://rest.uniprot.org/unisave/A0A4W3GG95?format=txt&versions=30"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A4W3GG95?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H10",
  "excerpt": "FT   TRANSMEM        130..156\nFT                   /note=\"Helical; Name=4\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:A0A6I8PUB9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.027017+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 110-112",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2de235f5ecdbc32faad1779acf9f8307edf330e58265fd2df418707701078865",
  "url": "https://rest.uniprot.org/unisave/A0A4W3GG95?format=txt&versions=30"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A4W3GG95?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H11",
  "excerpt": "FT   TOPO_DOM        157..172\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:A0A6I8PUB9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.027017+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 113-115",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2de235f5ecdbc32faad1779acf9f8307edf330e58265fd2df418707701078865",
  "url": "https://rest.uniprot.org/unisave/A0A4W3GG95?format=txt&versions=30"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A4W3GG95?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H12",
  "excerpt": "FT   TRANSMEM        173..210\nFT                   /note=\"Helical; Name=5\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:A0A6I8PUB9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.027017+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 116-118",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2de235f5ecdbc32faad1779acf9f8307edf330e58265fd2df418707701078865",
  "url": "https://rest.uniprot.org/unisave/A0A4W3GG95?format=txt&versions=30"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A4W3GG95?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H13",
  "excerpt": "FT   TOPO_DOM        211..214\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:A0A6I8PUB9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.027017+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 119-121",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2de235f5ecdbc32faad1779acf9f8307edf330e58265fd2df418707701078865",
  "url": "https://rest.uniprot.org/unisave/A0A4W3GG95?format=txt&versions=30"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A4W3GG95?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H14",
  "excerpt": "FT   TRANSMEM        215..250\nFT                   /note=\"Helical; Name=6\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:A0A6I8PUB9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.027017+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 122-124",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2de235f5ecdbc32faad1779acf9f8307edf330e58265fd2df418707701078865",
  "url": "https://rest.uniprot.org/unisave/A0A4W3GG95?format=txt&versions=30"
}
```

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A4W3GG95?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H15",
  "excerpt": "FT   TOPO_DOM        251..260\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:A0A6I8PUB9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.027017+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 125-127",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2de235f5ecdbc32faad1779acf9f8307edf330e58265fd2df418707701078865",
  "url": "https://rest.uniprot.org/unisave/A0A4W3GG95?format=txt&versions=30"
}
```

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A4W3GG95?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H16",
  "excerpt": "FT   TRANSMEM        261..289\nFT                   /note=\"Helical; Name=7\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:A0A6I8PUB9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.027017+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 128-130",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2de235f5ecdbc32faad1779acf9f8307edf330e58265fd2df418707701078865",
  "url": "https://rest.uniprot.org/unisave/A0A4W3GG95?format=txt&versions=30"
}
```

### Evidence H17

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A4W3GG95?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H17",
  "excerpt": "FT   TOPO_DOM        290..364\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:A0A6I8PUB9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.027017+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 131-133",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2de235f5ecdbc32faad1779acf9f8307edf330e58265fd2df418707701078865",
  "url": "https://rest.uniprot.org/unisave/A0A4W3GG95?format=txt&versions=30"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 21. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
