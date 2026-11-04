# transmembrane_0019

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0019.txt)

**Task:** `transmembrane`  
**Expected answer:** **C** — 1..21; 38..58; 72..92; 125..145; 154..174; 255..275; 284..304; 318..338; 348..368; 398..418; 427..447

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MGLFTDLVLYGIVLPALPFIMRNRFHIPNAELQHYTSGFLATYAGASVFFSVPAGWAASKLGSRQLFLGGLVFLFVATAIFAFSTSLALLVVSRLLQGMSTAVVWTAGLDMVQDTVDPSQIGVTIGTIFATISVGELAAPVLGGVLYERGGIAAVFAVSAVMLAIDLGLRGLVIDKKAAVKFESPCLIRSSAERSDHVASAPTVVEAQERTHEGTPLLPQDDDDDSDRYKIDRELGSIVQAIPLLYCFREPRLHLAMLLSFVQALFIGTFDATVPTEAESLFHFSSLQVGLVFIALMLPYFALGRLAGQAVDRFGTKAAATSGYAFLVPCLLLLGLPEKKLVSKEANVALFCTILALNGIGLAVVTSPGYVEAIDVTTKYQVANPGHFGENGPYAQLFGFSSLYFFTGLAVGPLLGGVLRAKFGYAVMGAVYAAISGVTAIVSFLFVGTRRGVCWG

[Multiple Choices]
A. 1..21; 72..92; 125..145; 154..174; 255..275; 284..304; 318..338; 348..368; 398..418; 427..447
B. 27..47; 82..102; 109..129; 136..156; 173..193; 209..229; 333..353; 361..381; 395..415; 427..447; 460..480
C. 1..21; 38..58; 72..92; 125..145; 154..174; 255..275; 284..304; 318..338; 348..368; 398..418; 427..447
D. 1..21; 38..58; 72..92; 125..145; 154..174; 255..275; 284..304; 318..338; 346..372; 398..418; 427..447
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

> The sequence-matched UniProt entry annotates the eleven transmembrane intervals listed in choice C. These are computational annotations (ECO:0000255), not evidence of experimental measurement, but they support the key for this sequence.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [C13](#evidence-c13), [C14](#evidence-c14), [C15](#evidence-c15).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains repeated long hydrophobic stretches characteristic of transmembrane helices in a multi-pass transporter. Those features support the intervals in C and distinguish them from the many nonmatching intervals and out-of-range coordinate in B; in particular, the hydrophobic stretch around 38..58 supports including that interval, unlike A. The hydrophobic core also favors C's 348..368 interval over D's broader 346..372 range, which includes less hydrophobic flanks.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level knowledge of multi-pass transporters and transferable hydropathy patterns provide a concrete basis for selecting C from these alternatives. Sequence-based boundary estimates are not exact, but the offered alternatives differ in ways the sequence can meaningfully discriminate.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> C and D are close, but the hydrophobic core supports C's narrower interval; D extends beyond it into less hydrophobic flanks.


### Important caveats

- The supporting database annotations are computational rather than experimental.
- Exact transmembrane boundaries can be uncertain when inferred from sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains repeated long hydrophobic stretches characteristic of transmembrane helices in a multi-pass transporter. Those features support the intervals in C and distinguish them from the many nonmatching intervals and out-of-range coordinate in B; in particular, the hydrophobic stretch around 38..58 supports including that interval, unlike A. The hydrophobic core also favors C's 348..368 interval over D's broader 346..372 range, which includes less hydrophobic flanks.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level knowledge of multi-pass transporters and transferable hydropathy patterns provide a concrete basis for selecting C from these alternatives. Sequence-based boundary estimates are not exact, but the offered alternatives differ in ways the sequence can meaningfully discriminate."
  },
  "case_id": "transmembrane_0019",
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
      "C14",
      "C15"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates the eleven transmembrane intervals listed in choice C. These are computational annotations (ECO:0000255), not evidence of experimental measurement, but they support the key for this sequence."
  },
  "important_caveats": [
    "The supporting database annotations are computational rather than experimental.",
    "Exact transmembrane boundaries can be uncertain when inferred from sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "C and D are close, but the hydrophobic core supports C's narrower interval; D extends beyond it into less hydrophobic flanks."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0019",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates the eleven transmembrane intervals listed in choice C. These are computational annotations (ECO:0000255), not evidence of experimental measurement, but they support the key for this sequence.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "C14", "C15"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains repeated long hydrophobic stretches characteristic of transmembrane helices in a multi-pass transporter. Those features support the intervals in C and distinguish them from the many nonmatching intervals and out-of-range coordinate in B; in particular, the hydrophobic stretch around 38..58 supports including that interval, unlike A. The hydrophobic core also favors C's 348..368 interval over D's broader 346..372 range, which includes less hydrophobic flanks.",
    "missing_item_specific_fact": "",
    "reason": "Family-level knowledge of multi-pass transporters and transferable hydropathy patterns provide a concrete basis for selecting C from these alternatives. Sequence-based boundary estimates are not exact, but the offered alternatives differ in ways the sequence can meaningfully discriminate."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "C and D are close, but the hydrophobic core supports C's narrower interval; D extends beyond it into less hydrophobic flanks."
  },
  "important_caveats": [
    "The supporting database annotations are computational rather than experimental.",
    "Exact transmembrane boundaries can be uncertain when inferred from sequence alone."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A455ZIM5 (PPZB_METMF) annotates exactly 11 transmembrane helical regions at positions 1..21, 38..58, 72..92, 125..145, 154..174, 255..275, 284..304, 318..338, 348..368, 398..418, and 427..447, matching option C precisely. All annotations carry evidence code ECO:0000255 (similarity-based/computational inference), not experimental data, but the sequence match is confirmed (SHA-256 identical). The protein is identified as an MFS-type transporter (ppzB), a family with a canonical 12-TM-helix architecture (11 annotated here).

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [C13](#evidence-c13), [C14](#evidence-c14), [C15](#evidence-c15), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11), [H12](#evidence-h12), [H13](#evidence-h13).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Several transferable lines of reasoning distinguish C from the alternatives. (1) Eliminating B: Option B's proposed TM regions (e.g., 27..47 = IPNAELQHYTSGFLATYAGAS) contain multiple charged/polar residues (N, E, Q, H, R, S, T), which are strongly incompatible with a membrane-spanning alpha-helix. A basic hydrophobicity scan of the sequence shows the true hydrophobic stretches begin at residue 1 (MGLFTDLVLYGIVLPALPFIM), not at 27. B's numbering appears shifted by ~26 positions and does not correspond to actual hydrophobic segments. (2) Eliminating A: Option A omits the region 38..58 (GFLATYAGASVFFSVPAGWAA), which is moderately hydrophobic (F, L, A, V, F, F, V, A, G, W, A, A). More importantly, this protein exhibits the hallmark large hydrophilic cytoplasmic loop around residues 180–250 (KKAAVKFESPCLIRSSAERSDHVASAPTVVEAQERTHEGTPLLPQDDDDDSDRYKIDRELGSIVQAIPLLYCFREPRLH), characteristic of Major Facilitator Superfamily (MFS) transporters, which canonically possess 12 TM helices (6+6 topology). Option A provides only 10 TM regions, too few for the MFS fold. (3) Distinguishing C from D: The sole difference is one helix boundary—C gives 348..368 (21 residues) while D gives 346..372 (27 residues). Position 346 is Glutamate (E), a charged residue highly unfavorable in the hydrophobic membrane interior, and position 369 is Proline (P), a well-known helix-breaking residue. Standard TM-helix definitions (e.g., TMHMM, Phobius) typically exclude such residues from the TM segment. The 21-residue length in C is also more consistent with the canonical MFS TM-helix length (~20–22 residues) than the 27-residue span in D. These are general biophysical principles applicable to any membrane protein, not facts specific to this protein.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can use: (a) hydrophobicity analysis to reject B's polar 'TM' regions; (b) MFS-family topology knowledge (large cytoplasmic loop, ~12 TM helices) to reject A's 10-helix count; (c) general membrane biophysics (charged Glu and helix-breaking Pro are incompatible with TM helix interiors) to reject D's extended boundary. These are transferable principles learned from the broader membrane-protein literature, not annotations specific to this exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While the C-vs-D distinction is fine (only 2 residues on each side of one helix), the presence of a charged Glu (E346) and a helix-breaking Pro (P369) in D's extension provides a clear biophysical argument favoring C. No other pair of options is similarly ambiguous: A is missing an entire helix, and B's regions are grossly misaligned with hydrophobic stretches.


### Important caveats

- All UniProt TM annotations use evidence code ECO:0000255 (similarity-based/computational), not experimental structure or cross-linking data. The 'correct' answer reflects a computational prediction transferred by homology.
- The C-vs-D distinction (348..368 vs 346..372) is at the precision boundary where different TM prediction tools (TMHMM, Phobius, DeepTMHMM) may disagree. The biophysical argument against E and P in the TM core is strong but not absolute—some validated TM helices do contain buried charged residues or prolines.
- The MFS 12-TM-helix canonical count is a family-level expectation; this protein is annotated with 11, which is within the observed range for MFS members. The argument against A (10 helices) relies on the family expectation but is not an absolute rule.
- The reviewer-only UniProt accession and organism identity (Metarhizium majus, MFS-type transporter ppzB) were not available to the evaluated model; the reasoning above relies only on sequence-level features and family-level knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Several transferable lines of reasoning distinguish C from the alternatives. (1) Eliminating B: Option B's proposed TM regions (e.g., 27..47 = IPNAELQHYTSGFLATYAGAS) contain multiple charged/polar residues (N, E, Q, H, R, S, T), which are strongly incompatible with a membrane-spanning alpha-helix. A basic hydrophobicity scan of the sequence shows the true hydrophobic stretches begin at residue 1 (MGLFTDLVLYGIVLPALPFIM), not at 27. B's numbering appears shifted by ~26 positions and does not correspond to actual hydrophobic segments. (2) Eliminating A: Option A omits the region 38..58 (GFLATYAGASVFFSVPAGWAA), which is moderately hydrophobic (F, L, A, V, F, F, V, A, G, W, A, A). More importantly, this protein exhibits the hallmark large hydrophilic cytoplasmic loop around residues 180–250 (KKAAVKFESPCLIRSSAERSDHVASAPTVVEAQERTHEGTPLLPQDDDDDSDRYKIDRELGSIVQAIPLLYCFREPRLH), characteristic of Major Facilitator Superfamily (MFS) transporters, which canonically possess 12 TM helices (6+6 topology). Option A provides only 10 TM regions, too few for the MFS fold. (3) Distinguishing C from D: The sole difference is one helix boundary—C gives 348..368 (21 residues) while D gives 346..372 (27 residues). Position 346 is Glutamate (E), a charged residue highly unfavorable in the hydrophobic membrane interior, and position 369 is Proline (P), a well-known helix-breaking residue. Standard TM-helix definitions (e.g., TMHMM, Phobius) typically exclude such residues from the TM segment. The 21-residue length in C is also more consistent with the canonical MFS TM-helix length (~20–22 residues) than the 27-residue span in D. These are general biophysical principles applicable to any membrane protein, not facts specific to this protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use: (a) hydrophobicity analysis to reject B's polar 'TM' regions; (b) MFS-family topology knowledge (large cytoplasmic loop, ~12 TM helices) to reject A's 10-helix count; (c) general membrane biophysics (charged Glu and helix-breaking Pro are incompatible with TM helix interiors) to reject D's extended boundary. These are transferable principles learned from the broader membrane-protein literature, not annotations specific to this exact protein."
  },
  "case_id": "transmembrane_0019",
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
      "C14",
      "C15",
      "H3",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9",
      "H10",
      "H11",
      "H12",
      "H13"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A455ZIM5 (PPZB_METMF) annotates exactly 11 transmembrane helical regions at positions 1..21, 38..58, 72..92, 125..145, 154..174, 255..275, 284..304, 318..338, 348..368, 398..418, and 427..447, matching option C precisely. All annotations carry evidence code ECO:0000255 (similarity-based/computational inference), not experimental data, but the sequence match is confirmed (SHA-256 identical). The protein is identified as an MFS-type transporter (ppzB), a family with a canonical 12-TM-helix architecture (11 annotated here)."
  },
  "important_caveats": [
    "All UniProt TM annotations use evidence code ECO:0000255 (similarity-based/computational), not experimental structure or cross-linking data. The 'correct' answer reflects a computational prediction transferred by homology.",
    "The C-vs-D distinction (348..368 vs 346..372) is at the precision boundary where different TM prediction tools (TMHMM, Phobius, DeepTMHMM) may disagree. The biophysical argument against E and P in the TM core is strong but not absolute—some validated TM helices do contain buried charged residues or prolines.",
    "The MFS 12-TM-helix canonical count is a family-level expectation; this protein is annotated with 11, which is within the observed range for MFS members. The argument against A (10 helices) relies on the family expectation but is not an absolute rule.",
    "The reviewer-only UniProt accession and organism identity (Metarhizium majus, MFS-type transporter ppzB) were not available to the evaluated model; the reasoning above relies only on sequence-level features and family-level knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the C-vs-D distinction is fine (only 2 residues on each side of one helix), the presence of a charged Glu (E346) and a helix-breaking Pro (P369) in D's extension provides a clear biophysical argument favoring C. No other pair of options is similarly ambiguous: A is missing an entire helix, and B's regions are grossly misaligned with hydrophobic stretches."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0019",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A455ZIM5 (PPZB_METMF) annotates exactly 11 transmembrane helical regions at positions 1..21, 38..58, 72..92, 125..145, 154..174, 255..275, 284..304, 318..338, 348..368, 398..418, and 427..447, matching option C precisely. All annotations carry evidence code ECO:0000255 (similarity-based/computational inference), not experimental data, but the sequence match is confirmed (SHA-256 identical). The protein is identified as an MFS-type transporter (ppzB), a family with a canonical 12-TM-helix architecture (11 annotated here).",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "C14", "C15", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "H11", "H12", "H13"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Several transferable lines of reasoning distinguish C from the alternatives. (1) Eliminating B: Option B's proposed TM regions (e.g., 27..47 = IPNAELQHYTSGFLATYAGAS) contain multiple charged/polar residues (N, E, Q, H, R, S, T), which are strongly incompatible with a membrane-spanning alpha-helix. A basic hydrophobicity scan of the sequence shows the true hydrophobic stretches begin at residue 1 (MGLFTDLVLYGIVLPALPFIM), not at 27. B's numbering appears shifted by ~26 positions and does not correspond to actual hydrophobic segments. (2) Eliminating A: Option A omits the region 38..58 (GFLATYAGASVFFSVPAGWAA), which is moderately hydrophobic (F, L, A, V, F, F, V, A, G, W, A, A). More importantly, this protein exhibits the hallmark large hydrophilic cytoplasmic loop around residues 180–250 (KKAAVKFESPCLIRSSAERSDHVASAPTVVEAQERTHEGTPLLPQDDDDDSDRYKIDRELGSIVQAIPLLYCFREPRLH), characteristic of Major Facilitator Superfamily (MFS) transporters, which canonically possess 12 TM helices (6+6 topology). Option A provides only 10 TM regions, too few for the MFS fold. (3) Distinguishing C from D: The sole difference is one helix boundary—C gives 348..368 (21 residues) while D gives 346..372 (27 residues). Position 346 is Glutamate (E), a charged residue highly unfavorable in the hydrophobic membrane interior, and position 369 is Proline (P), a well-known helix-breaking residue. Standard TM-helix definitions (e.g., TMHMM, Phobius) typically exclude such residues from the TM segment. The 21-residue length in C is also more consistent with the canonical MFS TM-helix length (~20–22 residues) than the 27-residue span in D. These are general biophysical principles applicable to any membrane protein, not facts specific to this protein.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use: (a) hydrophobicity analysis to reject B's polar 'TM' regions; (b) MFS-family topology knowledge (large cytoplasmic loop, ~12 TM helices) to reject A's 10-helix count; (c) general membrane biophysics (charged Glu and helix-breaking Pro are incompatible with TM helix interiors) to reject D's extended boundary. These are transferable principles learned from the broader membrane-protein literature, not annotations specific to this exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the C-vs-D distinction is fine (only 2 residues on each side of one helix), the presence of a charged Glu (E346) and a helix-breaking Pro (P369) in D's extension provides a clear biophysical argument favoring C. No other pair of options is similarly ambiguous: A is missing an entire helix, and B's regions are grossly misaligned with hydrophobic stretches."
  },
  "important_caveats": [
    "All UniProt TM annotations use evidence code ECO:0000255 (similarity-based/computational), not experimental structure or cross-linking data. The 'correct' answer reflects a computational prediction transferred by homology.",
    "The C-vs-D distinction (348..368 vs 346..372) is at the precision boundary where different TM prediction tools (TMHMM, Phobius, DeepTMHMM) may disagree. The biophysical argument against E and P in the TM core is strong but not absolute—some validated TM helices do contain buried charged residues or prolines.",
    "The MFS 12-TM-helix canonical count is a family-level expectation; this protein is annotated with 11, which is within the observed range for MFS members. The argument against A (10 helices) relies on the family expectation but is not an absolute rule.",
    "The reviewer-only UniProt accession and organism identity (Metarhizium majus, MFS-type transporter ppzB) were not available to the evaluated model; the reasoning above relies only on sequence-level features and family-level knowledge."
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
  "benchmark_sequence_length": 456,
  "benchmark_sequence_sha256": "04f8c5e9e85da67b086773ba9238fcda3b1271a5894d0e923953e09ca0f0172f",
  "current_entry_audit": {
    "entryVersion": 18,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-01-28",
    "lastSequenceUpdateDate": "2019-06-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "6ca07c0a168a625bda1ae7ac7bf6169436a142dafb1eeff3ee0b50ba41ca0dfa",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 456,
  "current_source_sequence_sha256": "04f8c5e9e85da67b086773ba9238fcda3b1271a5894d0e923953e09ca0f0172f",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 18,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A455ZIM5",
  "selected_historical_entry_version": 18,
  "selected_historical_record_sha256": "23d1c6a0dd94bf4fb1bfb14ea0ccf66dde7fd98de0a1a6c3dc11a9bda856717c",
  "selected_historical_source_sequence_length": 456,
  "selected_historical_source_sequence_sha256": "04f8c5e9e85da67b086773ba9238fcda3b1271a5894d0e923953e09ca0f0172f",
  "selected_historical_version": {
    "accession": "A0A455ZIM5",
    "database": "Swiss-Prot",
    "entryVersion": 18,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "PPZB_METMF",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A455ZIM5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:25:12.764881+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6ca07c0a168a625bda1ae7ac7bf6169436a142dafb1eeff3ee0b50ba41ca0dfa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":18,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-01-28\",\"lastSequenceUpdateDate\":\"2019-06-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:25:12.764881+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6ca07c0a168a625bda1ae7ac7bf6169436a142dafb1eeff3ee0b50ba41ca0dfa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Hypocreomycetidae\",\"Hypocreales\",\"Clavicipitaceae\",\"Metarhizium\",\"Metarhizium majus\"],\"scientificName\":\"Metarhizium majus (strain ARSEF 297)\",\"taxonId\":1276143}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:25:12.764881+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6ca07c0a168a625bda1ae7ac7bf6169436a142dafb1eeff3ee0b50ba41ca0dfa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30452111\",\"source\":\"PubMed\"}],\"value\":\"Pyrrolopyrazine biosynthesis cluster protein B\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30452111\",\"source\":\"PubMed\"}],\"value\":\"MFS-type transporter ppzB\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:25:12.764881+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6ca07c0a168a625bda1ae7ac7bf6169436a142dafb1eeff3ee0b50ba41ca0dfa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":21},\"start\":{\"modifier\":\"EXACT\",\"value\":1}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:25:12.764881+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6ca07c0a168a625bda1ae7ac7bf6169436a142dafb1eeff3ee0b50ba41ca0dfa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":58},\"start\":{\"modifier\":\"EXACT\",\"value\":38}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:25:12.764881+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6ca07c0a168a625bda1ae7ac7bf6169436a142dafb1eeff3ee0b50ba41ca0dfa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":92},\"start\":{\"modifier\":\"EXACT\",\"value\":72}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:25:12.764881+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6ca07c0a168a625bda1ae7ac7bf6169436a142dafb1eeff3ee0b50ba41ca0dfa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":145},\"start\":{\"modifier\":\"EXACT\",\"value\":125}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:25:12.764881+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6ca07c0a168a625bda1ae7ac7bf6169436a142dafb1eeff3ee0b50ba41ca0dfa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":174},\"start\":{\"modifier\":\"EXACT\",\"value\":154}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:25:12.764881+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6ca07c0a168a625bda1ae7ac7bf6169436a142dafb1eeff3ee0b50ba41ca0dfa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":275},\"start\":{\"modifier\":\"EXACT\",\"value\":255}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:25:12.764881+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6ca07c0a168a625bda1ae7ac7bf6169436a142dafb1eeff3ee0b50ba41ca0dfa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":304},\"start\":{\"modifier\":\"EXACT\",\"value\":284}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:25:12.764881+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6ca07c0a168a625bda1ae7ac7bf6169436a142dafb1eeff3ee0b50ba41ca0dfa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":338},\"start\":{\"modifier\":\"EXACT\",\"value\":318}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:25:12.764881+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6ca07c0a168a625bda1ae7ac7bf6169436a142dafb1eeff3ee0b50ba41ca0dfa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":368},\"start\":{\"modifier\":\"EXACT\",\"value\":348}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-02T04:25:12.764881+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6ca07c0a168a625bda1ae7ac7bf6169436a142dafb1eeff3ee0b50ba41ca0dfa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":418},\"start\":{\"modifier\":\"EXACT\",\"value\":398}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-02T04:25:12.764881+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6ca07c0a168a625bda1ae7ac7bf6169436a142dafb1eeff3ee0b50ba41ca0dfa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":447},\"start\":{\"modifier\":\"EXACT\",\"value\":427}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/11",
  "retrieved_utc": "2026-11-02T04:25:12.764881+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6ca07c0a168a625bda1ae7ac7bf6169436a142dafb1eeff3ee0b50ba41ca0dfa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json)

```json
{
  "evidence_id": "C16",
  "excerpt": "{\"citation\":{\"authors\":[\"Berry D.\",\"Mace W.\",\"Rehner S.A.\",\"Grage K.\",\"Dijkwel P.P.\",\"Young C.A.\",\"Scott B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30452111\"},{\"database\":\"DOI\",\"id\":\"10.1111/1462-2920.14483\"}],\"citationType\":\"journal article\",\"firstPage\":\"928\",\"id\":\"30452111\",\"journal\":\"Environ. Microbiol.\",\"lastPage\":\"939\",\"publicationDate\":\"2019\",\"title\":\"Orthologous peramine and pyrrolopyrazine-producing biosynthetic gene clusters in Metarhizium rileyi, Metarhizium majus and Cladonia grayi.\",\"volume\":\"21\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ARSEF 297\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:25:12.764881+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6ca07c0a168a625bda1ae7ac7bf6169436a142dafb1eeff3ee0b50ba41ca0dfa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM5.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18)

```json
{
  "entry_version": 18,
  "evidence_id": "H1",
  "excerpt": "ID   PPZB_METMF              Reviewed;         456 AA.\nAC   A0A455ZIM5;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-JUN-2019, sequence version 1.\nDT   28-JAN-2026, entry version 18.\nDE   RecName: Full=MFS-type transporter ppzB {ECO:0000303|PubMed:30452111};\nDE   AltName: Full=Pyrrolopyrazine biosynthesis cluster protein B {ECO:0000303|PubMed:30452111};\nGN   Name=ppzB;\nOS   Metarhizium majus (strain ARSEF 297).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Hypocreomycetidae; Hypocreales; Clavicipitaceae; Metarhizium;\nOC   Metarhizium majus.\nOX   NCBI_TaxID=1276143;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:16.028134+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "23d1c6a0dd94bf4fb1bfb14ea0ccf66dde7fd98de0a1a6c3dc11a9bda856717c",
  "url": "https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18)

```json
{
  "entry_version": 18,
  "evidence_id": "H2",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, AND PATHWAY.\nRC   STRAIN=ARSEF 297;\nRX   PubMed=30452111; DOI=10.1111/1462-2920.14483;\nRA   Berry D., Mace W., Rehner S.A., Grage K., Dijkwel P.P., Young C.A.,\nRA   Scott B.;\nRT   \"Orthologous peramine and pyrrolopyrazine-producing biosynthetic gene\nRT   clusters in Metarhizium rileyi, Metarhizium majus and Cladonia grayi.\";\nRL   Environ. Microbiol. 21:928-939(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:16.028134+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 14-22",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "23d1c6a0dd94bf4fb1bfb14ea0ccf66dde7fd98de0a1a6c3dc11a9bda856717c",
  "url": "https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18)

```json
{
  "entry_version": 18,
  "evidence_id": "H3",
  "excerpt": "FT   TRANSMEM        1..21\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:16.028134+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 65-67",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "23d1c6a0dd94bf4fb1bfb14ea0ccf66dde7fd98de0a1a6c3dc11a9bda856717c",
  "url": "https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18)

```json
{
  "entry_version": 18,
  "evidence_id": "H4",
  "excerpt": "FT   TRANSMEM        38..58\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:16.028134+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 68-70",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "23d1c6a0dd94bf4fb1bfb14ea0ccf66dde7fd98de0a1a6c3dc11a9bda856717c",
  "url": "https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18)

```json
{
  "entry_version": 18,
  "evidence_id": "H5",
  "excerpt": "FT   TRANSMEM        72..92\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:16.028134+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 71-73",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "23d1c6a0dd94bf4fb1bfb14ea0ccf66dde7fd98de0a1a6c3dc11a9bda856717c",
  "url": "https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18)

```json
{
  "entry_version": 18,
  "evidence_id": "H6",
  "excerpt": "FT   TRANSMEM        125..145\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:16.028134+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 74-76",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "23d1c6a0dd94bf4fb1bfb14ea0ccf66dde7fd98de0a1a6c3dc11a9bda856717c",
  "url": "https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18)

```json
{
  "entry_version": 18,
  "evidence_id": "H7",
  "excerpt": "FT   TRANSMEM        154..174\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:16.028134+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 77-79",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "23d1c6a0dd94bf4fb1bfb14ea0ccf66dde7fd98de0a1a6c3dc11a9bda856717c",
  "url": "https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18)

```json
{
  "entry_version": 18,
  "evidence_id": "H8",
  "excerpt": "FT   TRANSMEM        255..275\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:16.028134+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 80-82",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "23d1c6a0dd94bf4fb1bfb14ea0ccf66dde7fd98de0a1a6c3dc11a9bda856717c",
  "url": "https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18)

```json
{
  "entry_version": 18,
  "evidence_id": "H9",
  "excerpt": "FT   TRANSMEM        284..304\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:16.028134+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 83-85",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "23d1c6a0dd94bf4fb1bfb14ea0ccf66dde7fd98de0a1a6c3dc11a9bda856717c",
  "url": "https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18)

```json
{
  "entry_version": 18,
  "evidence_id": "H10",
  "excerpt": "FT   TRANSMEM        318..338\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:16.028134+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 86-88",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "23d1c6a0dd94bf4fb1bfb14ea0ccf66dde7fd98de0a1a6c3dc11a9bda856717c",
  "url": "https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18)

```json
{
  "entry_version": 18,
  "evidence_id": "H11",
  "excerpt": "FT   TRANSMEM        348..368\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:16.028134+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 89-91",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "23d1c6a0dd94bf4fb1bfb14ea0ccf66dde7fd98de0a1a6c3dc11a9bda856717c",
  "url": "https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18)

```json
{
  "entry_version": 18,
  "evidence_id": "H12",
  "excerpt": "FT   TRANSMEM        398..418\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:16.028134+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 92-94",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "23d1c6a0dd94bf4fb1bfb14ea0ccf66dde7fd98de0a1a6c3dc11a9bda856717c",
  "url": "https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18)

```json
{
  "entry_version": 18,
  "evidence_id": "H13",
  "excerpt": "FT   TRANSMEM        427..447\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:16.028134+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 95-97",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "23d1c6a0dd94bf4fb1bfb14ea0ccf66dde7fd98de0a1a6c3dc11a9bda856717c",
  "url": "https://rest.uniprot.org/unisave/A0A455ZIM5?format=txt&versions=18"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 19. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
