# transmembrane_0045

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0045.txt)

**Task:** `transmembrane`  
**Expected answer:** **C** — 113..133; 143..163; 166..186; 234..254; 275..295; 384..404; 413..433; 437..457; 473..493

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTALDTDTPTAGRSAPLISPGPVIPPPDFGPLDRAQGWAMTAIITALAAITRFLNLGSPTDAGTPIFDEKHYAPQAWQVLHNDGVEDNPGYGLVVHPPVGKQLIAIGEWLFGYNGLGWRFSGAVCGVIIVMLVTRIARRISRSTLVGAIAGLLIIADGVSFVSSRTALLDVFLVMFAVAAFACLMVDRDQVRERMYHAFLDGRIAETRWGTRLGVRWWRFGAGVLLGLACATKWSGLYFVLFFGVMTLVFDAIARKQYHVPHPWRGMLRRDLGPAAYVFGLIPFAVYLASYAPWFASETAVNRYEVGRSIGPDSILPIPDALRSLWHYTHAAYRFHSNLTNADGNHHPWESKPWTWPMSLRPVLYAIDNQDVPGCGAQSCVKAVMLVGTPAMWFIAVPVLGWALWRTVVRRDWRYGAVLVGYMAGFLPWFADIDRQMYFFYATVMAPFLVLAIALILGDILYKPNQNPERRTLGLLTVCFYVALVITNFAWMYPILTGLPISQTTWNLQIWLPSWR

[Multiple Choices]
A. 113..133; 143..163; 166..186; 234..254; 275..295; 382..407; 413..433; 437..457; 473..493
B. 6..26
C. 113..133; 143..163; 166..186; 234..254; 275..295; 384..404; 413..433; 437..457; 473..493
D. 113..133; 143..163; 166..186; 234..254; 275..295; 384..404; 413..433; 437..457
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

> The sequence-matched UniProt record lists all nine transmembrane intervals in choice C. These annotations carry computational evidence code ECO:0000255, so they support the key as database predictions, not as independently established experimental measurements.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [C13](#evidence-c13).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has multiple strongly hydrophobic regions, allowing a transferable sequence-based inference of a multipass membrane protein and making the single short interval in B implausible. But A and C differ only in the boundaries assigned to the same hydrophobic helix; sequence hydropathy supports the region without robustly selecting one exact endpoint convention.


**Missing item-specific fact**

> The exact predicted boundary annotation for the helix represented as 384..404 in C versus 382..407 in A.


**Reason**

> Transferable sequence features identify the membrane-spanning regions broadly, but do not meaningfully resolve the near-identical boundary alternatives A and C. Selecting the keyed coordinate set requires an exact prediction or annotation for this protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> Both options include the same set of predicted helices and assign slightly different limits to the same hydrophobic region. The question gives no boundary convention that makes the narrower or wider interval uniquely correct as a segment crossing the membrane.


### Important caveats

- The source annotations are computationally evidenced; the supplied evidence does not establish experimental validation of each interval.
- The source sequence matches the supplied sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has multiple strongly hydrophobic regions, allowing a transferable sequence-based inference of a multipass membrane protein and making the single short interval in B implausible. But A and C differ only in the boundaries assigned to the same hydrophobic helix; sequence hydropathy supports the region without robustly selecting one exact endpoint convention.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact predicted boundary annotation for the helix represented as 384..404 in C versus 382..407 in A.",
    "reason": "Transferable sequence features identify the membrane-spanning regions broadly, but do not meaningfully resolve the near-identical boundary alternatives A and C. Selecting the keyed coordinate set requires an exact prediction or annotation for this protein."
  },
  "case_id": "transmembrane_0045",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "C10",
      "C11",
      "C12",
      "C13"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record lists all nine transmembrane intervals in choice C. These annotations carry computational evidence code ECO:0000255, so they support the key as database predictions, not as independently established experimental measurements."
  },
  "important_caveats": [
    "The source annotations are computationally evidenced; the supplied evidence does not establish experimental validation of each interval.",
    "The source sequence matches the supplied sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "Both options include the same set of predicted helices and assign slightly different limits to the same hydrophobic region. The question gives no boundary convention that makes the narrower or wider interval uniquely correct as a segment crossing the membrane."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0045",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record lists all nine transmembrane intervals in choice C. These annotations carry computational evidence code ECO:0000255, so they support the key as database predictions, not as independently established experimental measurements.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has multiple strongly hydrophobic regions, allowing a transferable sequence-based inference of a multipass membrane protein and making the single short interval in B implausible. But A and C differ only in the boundaries assigned to the same hydrophobic helix; sequence hydropathy supports the region without robustly selecting one exact endpoint convention.",
    "missing_item_specific_fact": "The exact predicted boundary annotation for the helix represented as 384..404 in C versus 382..407 in A.",
    "reason": "Transferable sequence features identify the membrane-spanning regions broadly, but do not meaningfully resolve the near-identical boundary alternatives A and C. Selecting the keyed coordinate set requires an exact prediction or annotation for this protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "Both options include the same set of predicted helices and assign slightly different limits to the same hydrophobic region. The question gives no boundary convention that makes the narrower or wider interval uniquely correct as a segment crossing the membrane."
  },
  "important_caveats": [
    "The source annotations are computationally evidenced; the supplied evidence does not establish experimental validation of each interval.",
    "The source sequence matches the supplied sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (A0R3E8) lists exactly nine transmembrane helices at 113..133, 143..163, 166..186, 234..254, 275..295, 384..404, 413..433, 437..457, and 473..493, matching option C precisely. However, all annotations carry evidence code ECO:0000255 (by similarity), indicating computational inference rather than experimental determination. The sequence itself supports these boundaries: each region is a hydrophobic stretch of ~21 residues consistent with a TM alpha-helix.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [C13](#evidence-c13), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The options differ in three ways: (1) B (6..26) is trivially eliminated as the N-terminal region contains polar/charged residues (D, T, P, A, G, R, S, A, P, L, I, S, P, G, P, V, I, P, P, P, D) with no hydrophobic stretch. (2) A vs C: the 6th TM region is 382..407 (A) vs 384..404 (C). Position 382 is K (charged) and positions 406-407 are R and T (polar), while 384..404 contains only hydrophobic residues (V, M, L, V, G, T, P, A, M, W, F, I, A, V, P, V, L, G, W, A, L). Standard TM prediction excludes charged residues from helix boundaries, favoring 384..404. (3) C vs D: region 473..493 (L, G, L, L, T, V, C, F, Y, V, A, L, V, I, T, N, F, A, W, M, Y) is a 21-residue hydrophobic stretch well within the canonical TM helix length range (18-25 residues) and should be included. A model applying hydropathy scoring and TM helix length criteria can distinguish all options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The distinctions between options rely on standard, transferable TM prediction principles: excluding charged residues (K, R) from helix boundaries, requiring ~20-25 hydrophobic residues for a TM helix, and including all qualifying hydrophobic stretches. These are general biophysical principles applicable to any membrane protein, not specific to this protein's database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The differences between options are resolvable by standard hydropathy analysis. Option A's inclusion of charged K(382) and R(406) in the TM boundary is clearly suboptimal. Option D's exclusion of the hydrophobic 473..493 stretch contradicts the obvious presence of a TM-length hydrophobic segment. Option B is trivially wrong. Option C is the only choice consistent with standard TM prediction criteria.


### Important caveats

- All UniProt TM annotations carry ECO:0000255 (by similarity), meaning they are computational predictions transferred from homologs, not experimentally validated boundaries.
- The boundary precision (384 vs 382, 404 vs 407) is within the typical ±2-3 residue uncertainty of TM prediction tools, but the inclusion of a charged lysine (K382) in option A makes it clearly inferior by standard criteria.
- The protein is a polyprenol-phosphate-mannose protein mannosyltransferase from Mycolicibacterium smegmatis, a multi-pass membrane enzyme with 9 predicted TM helices, consistent with its enzymatic function requiring membrane anchoring.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The options differ in three ways: (1) B (6..26) is trivially eliminated as the N-terminal region contains polar/charged residues (D, T, P, A, G, R, S, A, P, L, I, S, P, G, P, V, I, P, P, P, D) with no hydrophobic stretch. (2) A vs C: the 6th TM region is 382..407 (A) vs 384..404 (C). Position 382 is K (charged) and positions 406-407 are R and T (polar), while 384..404 contains only hydrophobic residues (V, M, L, V, G, T, P, A, M, W, F, I, A, V, P, V, L, G, W, A, L). Standard TM prediction excludes charged residues from helix boundaries, favoring 384..404. (3) C vs D: region 473..493 (L, G, L, L, T, V, C, F, Y, V, A, L, V, I, T, N, F, A, W, M, Y) is a 21-residue hydrophobic stretch well within the canonical TM helix length range (18-25 residues) and should be included. A model applying hydropathy scoring and TM helix length criteria can distinguish all options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The distinctions between options rely on standard, transferable TM prediction principles: excluding charged residues (K, R) from helix boundaries, requiring ~20-25 hydrophobic residues for a TM helix, and including all qualifying hydrophobic stretches. These are general biophysical principles applicable to any membrane protein, not specific to this protein's database record."
  },
  "case_id": "transmembrane_0045",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "C10",
      "C11",
      "C12",
      "C13",
      "H3",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9",
      "H10",
      "H11"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (A0R3E8) lists exactly nine transmembrane helices at 113..133, 143..163, 166..186, 234..254, 275..295, 384..404, 413..433, 437..457, and 473..493, matching option C precisely. However, all annotations carry evidence code ECO:0000255 (by similarity), indicating computational inference rather than experimental determination. The sequence itself supports these boundaries: each region is a hydrophobic stretch of ~21 residues consistent with a TM alpha-helix."
  },
  "important_caveats": [
    "All UniProt TM annotations carry ECO:0000255 (by similarity), meaning they are computational predictions transferred from homologs, not experimentally validated boundaries.",
    "The boundary precision (384 vs 382, 404 vs 407) is within the typical ±2-3 residue uncertainty of TM prediction tools, but the inclusion of a charged lysine (K382) in option A makes it clearly inferior by standard criteria.",
    "The protein is a polyprenol-phosphate-mannose protein mannosyltransferase from Mycolicibacterium smegmatis, a multi-pass membrane enzyme with 9 predicted TM helices, consistent with its enzymatic function requiring membrane anchoring."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The differences between options are resolvable by standard hydropathy analysis. Option A's inclusion of charged K(382) and R(406) in the TM boundary is clearly suboptimal. Option D's exclusion of the hydrophobic 473..493 stretch contradicts the obvious presence of a TM-length hydrophobic segment. Option B is trivially wrong. Option C is the only choice consistent with standard TM prediction criteria."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0045",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (A0R3E8) lists exactly nine transmembrane helices at 113..133, 143..163, 166..186, 234..254, 275..295, 384..404, 413..433, 437..457, and 473..493, matching option C precisely. However, all annotations carry evidence code ECO:0000255 (by similarity), indicating computational inference rather than experimental determination. The sequence itself supports these boundaries: each region is a hydrophobic stretch of ~21 residues consistent with a TM alpha-helix.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "H11"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The options differ in three ways: (1) B (6..26) is trivially eliminated as the N-terminal region contains polar/charged residues (D, T, P, A, G, R, S, A, P, L, I, S, P, G, P, V, I, P, P, P, D) with no hydrophobic stretch. (2) A vs C: the 6th TM region is 382..407 (A) vs 384..404 (C). Position 382 is K (charged) and positions 406-407 are R and T (polar), while 384..404 contains only hydrophobic residues (V, M, L, V, G, T, P, A, M, W, F, I, A, V, P, V, L, G, W, A, L). Standard TM prediction excludes charged residues from helix boundaries, favoring 384..404. (3) C vs D: region 473..493 (L, G, L, L, T, V, C, F, Y, V, A, L, V, I, T, N, F, A, W, M, Y) is a 21-residue hydrophobic stretch well within the canonical TM helix length range (18-25 residues) and should be included. A model applying hydropathy scoring and TM helix length criteria can distinguish all options.",
    "missing_item_specific_fact": "",
    "reason": "The distinctions between options rely on standard, transferable TM prediction principles: excluding charged residues (K, R) from helix boundaries, requiring ~20-25 hydrophobic residues for a TM helix, and including all qualifying hydrophobic stretches. These are general biophysical principles applicable to any membrane protein, not specific to this protein's database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The differences between options are resolvable by standard hydropathy analysis. Option A's inclusion of charged K(382) and R(406) in the TM boundary is clearly suboptimal. Option D's exclusion of the hydrophobic 473..493 stretch contradicts the obvious presence of a TM-length hydrophobic segment. Option B is trivially wrong. Option C is the only choice consistent with standard TM prediction criteria."
  },
  "important_caveats": [
    "All UniProt TM annotations carry ECO:0000255 (by similarity), meaning they are computational predictions transferred from homologs, not experimentally validated boundaries.",
    "The boundary precision (384 vs 382, 404 vs 407) is within the typical ±2-3 residue uncertainty of TM prediction tools, but the inclusion of a charged lysine (K382) in option A makes it clearly inferior by standard criteria.",
    "The protein is a polyprenol-phosphate-mannose protein mannosyltransferase from Mycolicibacterium smegmatis, a multi-pass membrane enzyme with 9 predicted TM helices, consistent with its enzymatic function requiring membrane anchoring."
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
  "benchmark_sequence_length": 516,
  "benchmark_sequence_sha256": "283fcdf8941135b9c8b4851bf735e03f92c71bebe99b9f17b27ab97279f6a1a0",
  "current_entry_audit": {
    "entryVersion": 116,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2007-01-09",
    "sequenceVersion": 1
  },
  "current_record_sha256": "7460bfadb65f50b4073bc118af38399e6b1513a5f5a97e209de8bb6435c7ac44",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 516,
  "current_source_sequence_sha256": "283fcdf8941135b9c8b4851bf735e03f92c71bebe99b9f17b27ab97279f6a1a0",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 114,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0R3E8",
  "selected_historical_entry_version": 114,
  "selected_historical_record_sha256": "4c32d7463b098ec708cba16ef0ffc8465a4a08c5c9abc6fb7d70933bd38435a7",
  "selected_historical_source_sequence_length": 516,
  "selected_historical_source_sequence_sha256": "283fcdf8941135b9c8b4851bf735e03f92c71bebe99b9f17b27ab97279f6a1a0",
  "selected_historical_version": {
    "accession": "A0R3E8",
    "database": "Swiss-Prot",
    "entryVersion": 114,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "PMT_MYCS2",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0R3E8.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0R3E8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:26:45.822179+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7460bfadb65f50b4073bc118af38399e6b1513a5f5a97e209de8bb6435c7ac44",
  "url": "https://rest.uniprot.org/uniprotkb/A0R3E8.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0R3E8.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":116,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2007-01-09\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:26:45.822179+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7460bfadb65f50b4073bc118af38399e6b1513a5f5a97e209de8bb6435c7ac44",
  "url": "https://rest.uniprot.org/uniprotkb/A0R3E8.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0R3E8.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Mycobacterium smegmatis\",\"lineage\":[\"Bacteria\",\"Bacillati\",\"Actinomycetota\",\"Actinomycetes\",\"Mycobacteriales\",\"Mycobacteriaceae\",\"Mycolicibacterium\"],\"scientificName\":\"Mycolicibacterium smegmatis (strain ATCC 700084 / mc(2)155)\",\"taxonId\":246196}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:26:45.822179+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7460bfadb65f50b4073bc118af38399e6b1513a5f5a97e209de8bb6435c7ac44",
  "url": "https://rest.uniprot.org/uniprotkb/A0R3E8.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0R3E8.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"23550160\",\"source\":\"PubMed\"}],\"value\":\"Protein O-mannosyltransferase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"23550160\",\"source\":\"PubMed\"}],\"value\":\"PMT\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"23550160\",\"source\":\"PubMed\"}],\"value\":\"2.4.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Polyprenol-phosphate-mannose--protein mannosyltransferase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:26:45.822179+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7460bfadb65f50b4073bc118af38399e6b1513a5f5a97e209de8bb6435c7ac44",
  "url": "https://rest.uniprot.org/uniprotkb/A0R3E8.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0R3E8.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":133},\"start\":{\"modifier\":\"EXACT\",\"value\":113}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:26:45.822179+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7460bfadb65f50b4073bc118af38399e6b1513a5f5a97e209de8bb6435c7ac44",
  "url": "https://rest.uniprot.org/uniprotkb/A0R3E8.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0R3E8.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":163},\"start\":{\"modifier\":\"EXACT\",\"value\":143}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:26:45.822179+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7460bfadb65f50b4073bc118af38399e6b1513a5f5a97e209de8bb6435c7ac44",
  "url": "https://rest.uniprot.org/uniprotkb/A0R3E8.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0R3E8.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":186},\"start\":{\"modifier\":\"EXACT\",\"value\":166}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:26:45.822179+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7460bfadb65f50b4073bc118af38399e6b1513a5f5a97e209de8bb6435c7ac44",
  "url": "https://rest.uniprot.org/uniprotkb/A0R3E8.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0R3E8.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":254},\"start\":{\"modifier\":\"EXACT\",\"value\":234}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:26:45.822179+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7460bfadb65f50b4073bc118af38399e6b1513a5f5a97e209de8bb6435c7ac44",
  "url": "https://rest.uniprot.org/uniprotkb/A0R3E8.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0R3E8.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":295},\"start\":{\"modifier\":\"EXACT\",\"value\":275}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:26:45.822179+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7460bfadb65f50b4073bc118af38399e6b1513a5f5a97e209de8bb6435c7ac44",
  "url": "https://rest.uniprot.org/uniprotkb/A0R3E8.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0R3E8.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":404},\"start\":{\"modifier\":\"EXACT\",\"value\":384}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:26:45.822179+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7460bfadb65f50b4073bc118af38399e6b1513a5f5a97e209de8bb6435c7ac44",
  "url": "https://rest.uniprot.org/uniprotkb/A0R3E8.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0R3E8.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":433},\"start\":{\"modifier\":\"EXACT\",\"value\":413}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:26:45.822179+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7460bfadb65f50b4073bc118af38399e6b1513a5f5a97e209de8bb6435c7ac44",
  "url": "https://rest.uniprot.org/uniprotkb/A0R3E8.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0R3E8.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":457},\"start\":{\"modifier\":\"EXACT\",\"value\":437}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:26:45.822179+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7460bfadb65f50b4073bc118af38399e6b1513a5f5a97e209de8bb6435c7ac44",
  "url": "https://rest.uniprot.org/uniprotkb/A0R3E8.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0R3E8.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":493},\"start\":{\"modifier\":\"EXACT\",\"value\":473}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-02T04:26:45.822179+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7460bfadb65f50b4073bc118af38399e6b1513a5f5a97e209de8bb6435c7ac44",
  "url": "https://rest.uniprot.org/uniprotkb/A0R3E8.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0R3E8.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"citation\":{\"authors\":[\"Liu C.F.\",\"Tonini L.\",\"Malaga W.\",\"Beau M.\",\"Stella A.\",\"Bouyssie D.\",\"Jackson M.C.\",\"Nigou J.\",\"Puzo G.\",\"Guilhot C.\",\"Burlet-Schiltz O.\",\"Riviere M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"23550160\"},{\"database\":\"DOI\",\"id\":\"10.1073/pnas.1219704110\"}],\"citationType\":\"journal article\",\"firstPage\":\"6560\",\"id\":\"23550160\",\"journal\":\"Proc. Natl. Acad. Sci. U.S.A.\",\"lastPage\":\"6565\",\"publicationDate\":\"2013\",\"title\":\"Bacterial protein-O-mannosylating enzyme is crucial for virulence of Mycobacterium tuberculosis.\",\"volume\":\"110\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC 700084 / mc(2)155\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"PATHWAY\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:26:45.822179+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7460bfadb65f50b4073bc118af38399e6b1513a5f5a97e209de8bb6435c7ac44",
  "url": "https://rest.uniprot.org/uniprotkb/A0R3E8.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0R3E8?format=txt&versions=114)

```json
{
  "entry_version": 114,
  "evidence_id": "H1",
  "excerpt": "ID   PMT_MYCS2               Reviewed;         516 AA.\nAC   A0R3E8; I7GFC3;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   09-JAN-2007, sequence version 1.\nDT   28-JAN-2026, entry version 114.\nDE   RecName: Full=Polyprenol-phosphate-mannose--protein mannosyltransferase {ECO:0000305};\nDE            EC=2.4.1.- {ECO:0000305|PubMed:23550160};\nDE   AltName: Full=Protein O-mannosyltransferase {ECO:0000303|PubMed:23550160};\nDE            Short=PMT {ECO:0000303|PubMed:23550160};\nGN   OrderedLocusNames=MSMEG_5447 {ECO:0000312|EMBL:ABK72177.1},\nGN   MSMEI_5297 {ECO:0000312|EMBL:AFP41739.1};\nOS   Mycolicibacterium smegmatis (strain ATCC 700084 / mc(2)155) (Mycobacterium\nOS   smegmatis).\nOC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Mycobacteriales;\nOC   Mycobacteriaceae; Mycolicibacterium.\nOX   NCBI_TaxID=246196;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:48.840229+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4c32d7463b098ec708cba16ef0ffc8465a4a08c5c9abc6fb7d70933bd38435a7",
  "url": "https://rest.uniprot.org/unisave/A0R3E8?format=txt&versions=114"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0R3E8?format=txt&versions=114)

```json
{
  "entry_version": 114,
  "evidence_id": "H2",
  "excerpt": "RN   [4]\nRP   FUNCTION, PATHWAY, AND DISRUPTION PHENOTYPE.\nRC   STRAIN=ATCC 700084 / mc(2)155;\nRX   PubMed=23550160; DOI=10.1073/pnas.1219704110;\nRA   Liu C.F., Tonini L., Malaga W., Beau M., Stella A., Bouyssie D.,\nRA   Jackson M.C., Nigou J., Puzo G., Guilhot C., Burlet-Schiltz O., Riviere M.;\nRT   \"Bacterial protein-O-mannosylating enzyme is crucial for virulence of\nRT   Mycobacterium tuberculosis.\";\nRL   Proc. Natl. Acad. Sci. U.S.A. 110:6560-6565(2013).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:48.840229+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 41-49",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4c32d7463b098ec708cba16ef0ffc8465a4a08c5c9abc6fb7d70933bd38435a7",
  "url": "https://rest.uniprot.org/unisave/A0R3E8?format=txt&versions=114"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0R3E8?format=txt&versions=114)

```json
{
  "entry_version": 114,
  "evidence_id": "H3",
  "excerpt": "FT   TRANSMEM        113..133\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:48.840229+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 108-110",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4c32d7463b098ec708cba16ef0ffc8465a4a08c5c9abc6fb7d70933bd38435a7",
  "url": "https://rest.uniprot.org/unisave/A0R3E8?format=txt&versions=114"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0R3E8?format=txt&versions=114)

```json
{
  "entry_version": 114,
  "evidence_id": "H4",
  "excerpt": "FT   TRANSMEM        143..163\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:48.840229+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 111-113",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4c32d7463b098ec708cba16ef0ffc8465a4a08c5c9abc6fb7d70933bd38435a7",
  "url": "https://rest.uniprot.org/unisave/A0R3E8?format=txt&versions=114"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0R3E8?format=txt&versions=114)

```json
{
  "entry_version": 114,
  "evidence_id": "H5",
  "excerpt": "FT   TRANSMEM        166..186\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:48.840229+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 114-116",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4c32d7463b098ec708cba16ef0ffc8465a4a08c5c9abc6fb7d70933bd38435a7",
  "url": "https://rest.uniprot.org/unisave/A0R3E8?format=txt&versions=114"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0R3E8?format=txt&versions=114)

```json
{
  "entry_version": 114,
  "evidence_id": "H6",
  "excerpt": "FT   TRANSMEM        234..254\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:48.840229+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 117-119",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4c32d7463b098ec708cba16ef0ffc8465a4a08c5c9abc6fb7d70933bd38435a7",
  "url": "https://rest.uniprot.org/unisave/A0R3E8?format=txt&versions=114"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0R3E8?format=txt&versions=114)

```json
{
  "entry_version": 114,
  "evidence_id": "H7",
  "excerpt": "FT   TRANSMEM        275..295\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:48.840229+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 120-122",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4c32d7463b098ec708cba16ef0ffc8465a4a08c5c9abc6fb7d70933bd38435a7",
  "url": "https://rest.uniprot.org/unisave/A0R3E8?format=txt&versions=114"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0R3E8?format=txt&versions=114)

```json
{
  "entry_version": 114,
  "evidence_id": "H8",
  "excerpt": "FT   TRANSMEM        384..404\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:48.840229+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 123-125",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4c32d7463b098ec708cba16ef0ffc8465a4a08c5c9abc6fb7d70933bd38435a7",
  "url": "https://rest.uniprot.org/unisave/A0R3E8?format=txt&versions=114"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0R3E8?format=txt&versions=114)

```json
{
  "entry_version": 114,
  "evidence_id": "H9",
  "excerpt": "FT   TRANSMEM        413..433\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:48.840229+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 126-128",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4c32d7463b098ec708cba16ef0ffc8465a4a08c5c9abc6fb7d70933bd38435a7",
  "url": "https://rest.uniprot.org/unisave/A0R3E8?format=txt&versions=114"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0R3E8?format=txt&versions=114)

```json
{
  "entry_version": 114,
  "evidence_id": "H10",
  "excerpt": "FT   TRANSMEM        437..457\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:48.840229+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 129-131",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4c32d7463b098ec708cba16ef0ffc8465a4a08c5c9abc6fb7d70933bd38435a7",
  "url": "https://rest.uniprot.org/unisave/A0R3E8?format=txt&versions=114"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0R3E8?format=txt&versions=114)

```json
{
  "entry_version": 114,
  "evidence_id": "H11",
  "excerpt": "FT   TRANSMEM        473..493\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:48.840229+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 132-134",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4c32d7463b098ec708cba16ef0ffc8465a4a08c5c9abc6fb7d70933bd38435a7",
  "url": "https://rest.uniprot.org/unisave/A0R3E8?format=txt&versions=114"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 45. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
