# transmembrane_0132

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0132.txt)

**Task:** `transmembrane`  
**Expected answer:** **B** — 24..44; 63..83; 84..104; 151..171; 173..193

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSEPNVRASFADNRRPLSKTKGQLLNMPPVITTALYTAFPVIFLLDKVLAFLTWTNDDPYTNFIAIAIYIMVVKYWTVVACTVLPTIIALGTCASLWFLKTTIDDLRSETAPPTIEEIIDTLINMQARFSYIVEPFSYFGSLSGSDYFNLGFSLIAITPCYIWLMTRIFTVRSFLLVFGVAWLSFHSSWSVATRHLLWRSIVIRKILTFTTGLKFSLVDKNIELTVLNDFQISNVGTGKTVEFHILQNQRRWLGVGWSNTLLPFERGPFTTEDLEKSWDSLESFQFPEITQATCRWRWLDANWKTDDSFAPGEGWIYYNNSWEEPSNTDSLTRFTRTKRWKRRALVIVEDDGTT

[Multiple Choices]
A. 24..44; 84..104; 151..171; 173..193
B. 24..44; 63..83; 84..104; 151..171; 173..193
C. 58..78
D. 27..44; 63..83; 84..104; 151..171; 173..193
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

> The sequence-matched historical UniProt record annotates all five intervals in B as helical transmembrane regions. These are computational annotations (ECO:0000255), so they support the expected answer as a database prediction, not as direct experimental validation.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains several hydrophobic stretches consistent with membrane-spanning helices. In particular, residues 63–83 are strongly hydrophobic, making B and D meaningfully more plausible than A, which omits that segment, or C, which gives only a partial interval. This is transferable hydropathy and membrane-protein reasoning, not reliance on the target's recorded annotation.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and choices provide a credible basis to identify the multi-pass pattern and distinguish the main alternatives. Transferable sequence-based inference supports the listed regions, although it does not establish exact helix boundaries with certainty.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> B and D differ in the N-terminal boundary of the first region: 24 versus 27. The shorter 27–44 interval is also a plausible membrane-spanning segment, and the question does not specify a boundary convention or required precision. B matches the cited annotation, but the wording alone does not clearly rule out D.


### Important caveats

- The cited transmembrane annotations are computational rather than direct experimental evidence.
- The historical source sequence matches the supplied sequence; the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains several hydrophobic stretches consistent with membrane-spanning helices. In particular, residues 63–83 are strongly hydrophobic, making B and D meaningfully more plausible than A, which omits that segment, or C, which gives only a partial interval. This is transferable hydropathy and membrane-protein reasoning, not reliance on the target's recorded annotation.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and choices provide a credible basis to identify the multi-pass pattern and distinguish the main alternatives. Transferable sequence-based inference supports the listed regions, although it does not establish exact helix boundaries with certainty."
  },
  "case_id": "transmembrane_0132",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H4",
      "H5",
      "H6",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record annotates all five intervals in B as helical transmembrane regions. These are computational annotations (ECO:0000255), so they support the expected answer as a database prediction, not as direct experimental validation."
  },
  "important_caveats": [
    "The cited transmembrane annotations are computational rather than direct experimental evidence.",
    "The historical source sequence matches the supplied sequence; the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "B and D differ in the N-terminal boundary of the first region: 24 versus 27. The shorter 27–44 interval is also a plausible membrane-spanning segment, and the question does not specify a boundary convention or required precision. B matches the cited annotation, but the wording alone does not clearly rule out D."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0132",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record annotates all five intervals in B as helical transmembrane regions. These are computational annotations (ECO:0000255), so they support the expected answer as a database prediction, not as direct experimental validation.",
    "evidence_ids": ["H3", "H4", "H5", "H6", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains several hydrophobic stretches consistent with membrane-spanning helices. In particular, residues 63–83 are strongly hydrophobic, making B and D meaningfully more plausible than A, which omits that segment, or C, which gives only a partial interval. This is transferable hydropathy and membrane-protein reasoning, not reliance on the target's recorded annotation.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and choices provide a credible basis to identify the multi-pass pattern and distinguish the main alternatives. Transferable sequence-based inference supports the listed regions, although it does not establish exact helix boundaries with certainty."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "B and D differ in the N-terminal boundary of the first region: 24 versus 27. The shorter 27–44 interval is also a plausible membrane-spanning segment, and the question does not specify a boundary convention or required precision. B matches the cited annotation, but the wording alone does not clearly rule out D."
  },
  "important_caveats": [
    "The cited transmembrane annotations are computational rather than direct experimental evidence.",
    "The historical source sequence matches the supplied sequence; the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry W1QHP2 (PEX32_OGAPD) annotates exactly five transmembrane helical regions: 24..44, 63..83, 84..104, 151..171, and 173..193, matching choice B precisely. However, all five annotations carry evidence code ECO:0000255 (automatic annotation from predicted data), meaning these are computational predictions rather than experimentally validated measurements. The annotation supports B as the recorded database answer, but the underlying evidence is algorithmic prediction, not direct experimental confirmation of membrane topology.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Several layers of transferable reasoning narrow the choices. (1) Choice C (a single TM at 58..78) is easily eliminated: the 354-residue sequence contains multiple long hydrophobic stretches (e.g., positions 63-83 FIAIAIYIMVVKYWTVVACTV, positions 173-193 SFLLVFGVAWLSFHSSWSVAT) characteristic of a multi-pass membrane protein, not a single-pass one. (2) The distinction between A (four TMs, omitting 63..83) and B (five TMs, including 63..83) is well-supported by hydropathy analysis: the 21-residue stretch at 63-83 is predominantly hydrophobic (F, I, A, I, A, I, Y, I, M, V, V, W, V, V, A, V) and of canonical TM-helix length (~20-25 residues). Any standard sliding-window hydrophobicity analysis or TM-prediction heuristic (e.g., Kyte-Doolittle, TMHMM-style logic) would flag this as a TM helix, making A clearly incomplete. (3) The B vs D distinction (first TM starting at 24 vs 27) is finer. Positions 24-26 are L, L, N. Two leucines are strongly hydrophobic; the single asparagine is polar but tolerable within a TM helix. Starting at 24 yields a 21-residue helix (24-44), closer to the canonical ~20-25 residue TM length, whereas starting at 27 yields only 18 residues (27-44), on the short side for a stable TM helix. Standard TM-prediction practice favors the longer hydrophobic segment, giving a modest but real preference for start=24. This is a probabilistic preference rather than a certainty, but it meaningfully distinguishes B from D using general TM-helix length principles learned from many membrane proteins.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The primary reasoning task—recognizing this as a multi-pass membrane protein and identifying the hydrophobic stretch at 63..83 as a TM helix—is strongly supported by general hydrophobicity analysis and TM-helix length rules transferable from many other membrane proteins. The finer boundary question (24 vs 27) is harder but still has a credible basis in standard TM-helix length preferences (21 vs 18 residues), giving a probabilistic edge to B. No target-specific database lookup is strictly necessary to reach B over A or C, and the B-over-D preference, while subtle, rests on general TM-length heuristics.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> The first TM boundary at position 24 (B) vs 27 (D) is a fine-grained annotation boundary. Positions 24-26 (L, L, N) contain two hydrophobic leucines and one polar asparagine; different TM-prediction algorithms or hydropathy thresholds could reasonably include or exclude these residues. Both 21-residue (24-44) and 18-residue (27-44) helices fall within the broad range of observed TM lengths. The preference for B rests on the general tendency toward longer hydrophobic segments, but D is not clearly wrong from sequence alone.


### Important caveats

- All five TM annotations in UniProt carry evidence code ECO:0000255 (automatic/computational prediction), not experimental validation. The 'correct' answer reflects a prediction algorithm's output, not confirmed membrane topology.
- The reviewer-only evidence confirms the sequence matches UniProt W1QHP2 (PEX32_OGAPD, Ogataea parapolymorpha), but this accession and organism identity were not provided to the evaluated model.
- The B vs D boundary distinction (start at 24 vs 27) is genuinely fine-grained; the preference for B relies on a general length heuristic rather than a definitive sequence feature.
- The protein is annotated as a peroxisomal membrane protein (PEX32), which is consistent with multiple TM helices, but the peroxisomal membrane context was not given in the original prompt.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Several layers of transferable reasoning narrow the choices. (1) Choice C (a single TM at 58..78) is easily eliminated: the 354-residue sequence contains multiple long hydrophobic stretches (e.g., positions 63-83 FIAIAIYIMVVKYWTVVACTV, positions 173-193 SFLLVFGVAWLSFHSSWSVAT) characteristic of a multi-pass membrane protein, not a single-pass one. (2) The distinction between A (four TMs, omitting 63..83) and B (five TMs, including 63..83) is well-supported by hydropathy analysis: the 21-residue stretch at 63-83 is predominantly hydrophobic (F, I, A, I, A, I, Y, I, M, V, V, W, V, V, A, V) and of canonical TM-helix length (~20-25 residues). Any standard sliding-window hydrophobicity analysis or TM-prediction heuristic (e.g., Kyte-Doolittle, TMHMM-style logic) would flag this as a TM helix, making A clearly incomplete. (3) The B vs D distinction (first TM starting at 24 vs 27) is finer. Positions 24-26 are L, L, N. Two leucines are strongly hydrophobic; the single asparagine is polar but tolerable within a TM helix. Starting at 24 yields a 21-residue helix (24-44), closer to the canonical ~20-25 residue TM length, whereas starting at 27 yields only 18 residues (27-44), on the short side for a stable TM helix. Standard TM-prediction practice favors the longer hydrophobic segment, giving a modest but real preference for start=24. This is a probabilistic preference rather than a certainty, but it meaningfully distinguishes B from D using general TM-helix length principles learned from many membrane proteins.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The primary reasoning task—recognizing this as a multi-pass membrane protein and identifying the hydrophobic stretch at 63..83 as a TM helix—is strongly supported by general hydrophobicity analysis and TM-helix length rules transferable from many other membrane proteins. The finer boundary question (24 vs 27) is harder but still has a credible basis in standard TM-helix length preferences (21 vs 18 residues), giving a probabilistic edge to B. No target-specific database lookup is strictly necessary to reach B over A or C, and the B-over-D preference, while subtle, rests on general TM-length heuristics."
  },
  "case_id": "transmembrane_0132",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "H3",
      "H4",
      "H5",
      "H6",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry W1QHP2 (PEX32_OGAPD) annotates exactly five transmembrane helical regions: 24..44, 63..83, 84..104, 151..171, and 173..193, matching choice B precisely. However, all five annotations carry evidence code ECO:0000255 (automatic annotation from predicted data), meaning these are computational predictions rather than experimentally validated measurements. The annotation supports B as the recorded database answer, but the underlying evidence is algorithmic prediction, not direct experimental confirmation of membrane topology."
  },
  "important_caveats": [
    "All five TM annotations in UniProt carry evidence code ECO:0000255 (automatic/computational prediction), not experimental validation. The 'correct' answer reflects a prediction algorithm's output, not confirmed membrane topology.",
    "The reviewer-only evidence confirms the sequence matches UniProt W1QHP2 (PEX32_OGAPD, Ogataea parapolymorpha), but this accession and organism identity were not provided to the evaluated model.",
    "The B vs D boundary distinction (start at 24 vs 27) is genuinely fine-grained; the preference for B relies on a general length heuristic rather than a definitive sequence feature.",
    "The protein is annotated as a peroxisomal membrane protein (PEX32), which is consistent with multiple TM helices, but the peroxisomal membrane context was not given in the original prompt."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "The first TM boundary at position 24 (B) vs 27 (D) is a fine-grained annotation boundary. Positions 24-26 (L, L, N) contain two hydrophobic leucines and one polar asparagine; different TM-prediction algorithms or hydropathy thresholds could reasonably include or exclude these residues. Both 21-residue (24-44) and 18-residue (27-44) helices fall within the broad range of observed TM lengths. The preference for B rests on the general tendency toward longer hydrophobic segments, but D is not clearly wrong from sequence alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0132",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry W1QHP2 (PEX32_OGAPD) annotates exactly five transmembrane helical regions: 24..44, 63..83, 84..104, 151..171, and 173..193, matching choice B precisely. However, all five annotations carry evidence code ECO:0000255 (automatic annotation from predicted data), meaning these are computational predictions rather than experimentally validated measurements. The annotation supports B as the recorded database answer, but the underlying evidence is algorithmic prediction, not direct experimental confirmation of membrane topology.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "H3", "H4", "H5", "H6", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Several layers of transferable reasoning narrow the choices. (1) Choice C (a single TM at 58..78) is easily eliminated: the 354-residue sequence contains multiple long hydrophobic stretches (e.g., positions 63-83 FIAIAIYIMVVKYWTVVACTV, positions 173-193 SFLLVFGVAWLSFHSSWSVAT) characteristic of a multi-pass membrane protein, not a single-pass one. (2) The distinction between A (four TMs, omitting 63..83) and B (five TMs, including 63..83) is well-supported by hydropathy analysis: the 21-residue stretch at 63-83 is predominantly hydrophobic (F, I, A, I, A, I, Y, I, M, V, V, W, V, V, A, V) and of canonical TM-helix length (~20-25 residues). Any standard sliding-window hydrophobicity analysis or TM-prediction heuristic (e.g., Kyte-Doolittle, TMHMM-style logic) would flag this as a TM helix, making A clearly incomplete. (3) The B vs D distinction (first TM starting at 24 vs 27) is finer. Positions 24-26 are L, L, N. Two leucines are strongly hydrophobic; the single asparagine is polar but tolerable within a TM helix. Starting at 24 yields a 21-residue helix (24-44), closer to the canonical ~20-25 residue TM length, whereas starting at 27 yields only 18 residues (27-44), on the short side for a stable TM helix. Standard TM-prediction practice favors the longer hydrophobic segment, giving a modest but real preference for start=24. This is a probabilistic preference rather than a certainty, but it meaningfully distinguishes B from D using general TM-helix length principles learned from many membrane proteins.",
    "missing_item_specific_fact": "",
    "reason": "The primary reasoning task—recognizing this as a multi-pass membrane protein and identifying the hydrophobic stretch at 63..83 as a TM helix—is strongly supported by general hydrophobicity analysis and TM-helix length rules transferable from many other membrane proteins. The finer boundary question (24 vs 27) is harder but still has a credible basis in standard TM-helix length preferences (21 vs 18 residues), giving a probabilistic edge to B. No target-specific database lookup is strictly necessary to reach B over A or C, and the B-over-D preference, while subtle, rests on general TM-length heuristics."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "The first TM boundary at position 24 (B) vs 27 (D) is a fine-grained annotation boundary. Positions 24-26 (L, L, N) contain two hydrophobic leucines and one polar asparagine; different TM-prediction algorithms or hydropathy thresholds could reasonably include or exclude these residues. Both 21-residue (24-44) and 18-residue (27-44) helices fall within the broad range of observed TM lengths. The preference for B rests on the general tendency toward longer hydrophobic segments, but D is not clearly wrong from sequence alone."
  },
  "important_caveats": [
    "All five TM annotations in UniProt carry evidence code ECO:0000255 (automatic/computational prediction), not experimental validation. The 'correct' answer reflects a prediction algorithm's output, not confirmed membrane topology.",
    "The reviewer-only evidence confirms the sequence matches UniProt W1QHP2 (PEX32_OGAPD, Ogataea parapolymorpha), but this accession and organism identity were not provided to the evaluated model.",
    "The B vs D boundary distinction (start at 24 vs 27) is genuinely fine-grained; the preference for B relies on a general length heuristic rather than a definitive sequence feature.",
    "The protein is annotated as a peroxisomal membrane protein (PEX32), which is consistent with multiple TM helices, but the peroxisomal membrane context was not given in the original prompt."
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
  "benchmark_sequence_length": 354,
  "benchmark_sequence_sha256": "abe0e7534f8e5a7590c0c44dd5ef1187e54178fee63a913ef3b3fc143ae42ee1",
  "current_entry_audit": {
    "entryVersion": 40,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2014-03-19",
    "sequenceVersion": 1
  },
  "current_record_sha256": "496aea11aa2b41aaa21a1680c1288b30d7312fd99c41cdd11ef292e508959dcd",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 354,
  "current_source_sequence_sha256": "abe0e7534f8e5a7590c0c44dd5ef1187e54178fee63a913ef3b3fc143ae42ee1",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 38,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "W1QHP2",
  "selected_historical_entry_version": 38,
  "selected_historical_record_sha256": "95f12c3e5266dcfc076c0bab33c3d654a00f2c142918715c03c5fb98c2acd8be",
  "selected_historical_source_sequence_length": 354,
  "selected_historical_source_sequence_sha256": "abe0e7534f8e5a7590c0c44dd5ef1187e54178fee63a913ef3b3fc143ae42ee1",
  "selected_historical_version": {
    "accession": "W1QHP2",
    "database": "Swiss-Prot",
    "entryVersion": 38,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "PEX32_OGAPD",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QHP2.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"W1QHP2\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:30.706856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "496aea11aa2b41aaa21a1680c1288b30d7312fd99c41cdd11ef292e508959dcd",
  "url": "https://rest.uniprot.org/uniprotkb/W1QHP2.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QHP2.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":40,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2014-03-19\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:30.706856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "496aea11aa2b41aaa21a1680c1288b30d7312fd99c41cdd11ef292e508959dcd",
  "url": "https://rest.uniprot.org/uniprotkb/W1QHP2.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QHP2.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Yeast\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Saccharomycotina\",\"Pichiomycetes\",\"Pichiales\",\"Pichiaceae\",\"Ogataea\"],\"scientificName\":\"Ogataea parapolymorpha (strain ATCC 26012 / BCRC 20466 / JCM 22074 / NRRL Y-7560 / DL-1)\",\"synonyms\":[\"Hansenula polymorpha\"],\"taxonId\":871575}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:30.706856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "496aea11aa2b41aaa21a1680c1288b30d7312fd99c41cdd11ef292e508959dcd",
  "url": "https://rest.uniprot.org/uniprotkb/W1QHP2.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QHP2.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Peroxin-32\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32665322\",\"source\":\"PubMed\"}],\"value\":\"Peroxisomal membrane protein PEX32\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:30.706856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "496aea11aa2b41aaa21a1680c1288b30d7312fd99c41cdd11ef292e508959dcd",
  "url": "https://rest.uniprot.org/uniprotkb/W1QHP2.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QHP2.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":44},\"start\":{\"modifier\":\"EXACT\",\"value\":24}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-01T06:25:30.706856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "496aea11aa2b41aaa21a1680c1288b30d7312fd99c41cdd11ef292e508959dcd",
  "url": "https://rest.uniprot.org/uniprotkb/W1QHP2.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QHP2.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":83},\"start\":{\"modifier\":\"EXACT\",\"value\":63}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-01T06:25:30.706856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "496aea11aa2b41aaa21a1680c1288b30d7312fd99c41cdd11ef292e508959dcd",
  "url": "https://rest.uniprot.org/uniprotkb/W1QHP2.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QHP2.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":104},\"start\":{\"modifier\":\"EXACT\",\"value\":84}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-01T06:25:30.706856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "496aea11aa2b41aaa21a1680c1288b30d7312fd99c41cdd11ef292e508959dcd",
  "url": "https://rest.uniprot.org/uniprotkb/W1QHP2.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QHP2.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":171},\"start\":{\"modifier\":\"EXACT\",\"value\":151}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-01T06:25:30.706856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "496aea11aa2b41aaa21a1680c1288b30d7312fd99c41cdd11ef292e508959dcd",
  "url": "https://rest.uniprot.org/uniprotkb/W1QHP2.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QHP2.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":193},\"start\":{\"modifier\":\"EXACT\",\"value\":173}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-01T06:25:30.706856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "496aea11aa2b41aaa21a1680c1288b30d7312fd99c41cdd11ef292e508959dcd",
  "url": "https://rest.uniprot.org/uniprotkb/W1QHP2.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QHP2.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Wu F.\",\"de Boer R.\",\"Krikken A.M.\",\"Aksit A.\",\"Bordin N.\",\"Devos D.P.\",\"van der Klei I.J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"32665322\"},{\"database\":\"DOI\",\"id\":\"10.1242/jcs.246983\"}],\"citationType\":\"journal article\",\"firstPage\":\"0\",\"id\":\"32665322\",\"journal\":\"J. Cell Sci.\",\"lastPage\":\"0\",\"publicationDate\":\"2020\",\"title\":\"Pex24 and Pex32 are required to tether peroxisomes to the ER for organelle biogenesis, positioning and segregation in yeast.\",\"volume\":\"133\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:25:30.706856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "496aea11aa2b41aaa21a1680c1288b30d7312fd99c41cdd11ef292e508959dcd",
  "url": "https://rest.uniprot.org/uniprotkb/W1QHP2.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QHP2?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H1",
  "excerpt": "ID   PEX32_OGAPD             Reviewed;         354 AA.\nAC   W1QHP2;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   19-MAR-2014, sequence version 1.\nDT   28-JAN-2026, entry version 38.\nDE   RecName: Full=Peroxisomal membrane protein PEX32 {ECO:0000303|PubMed:32665322};\nDE   AltName: Full=Peroxin-32 {ECO:0000305};\nGN   Name=PEX32 {ECO:0000303|PubMed:32665322}; ORFNames=HPODL_04641;\nOS   Ogataea parapolymorpha (strain ATCC 26012 / BCRC 20466 / JCM 22074 / NRRL\nOS   Y-7560 / DL-1) (Yeast) (Hansenula polymorpha).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Saccharomycotina; Pichiomycetes;\nOC   Pichiales; Pichiaceae; Ogataea.\nOX   NCBI_TaxID=871575;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:55.253871+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "95f12c3e5266dcfc076c0bab33c3d654a00f2c142918715c03c5fb98c2acd8be",
  "url": "https://rest.uniprot.org/unisave/W1QHP2?format=txt&versions=38"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QHP2?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, DISRUPTION PHENOTYPE, AND SUBCELLULAR LOCATION.\nRX   PubMed=32665322; DOI=10.1242/jcs.246983;\nRA   Wu F., de Boer R., Krikken A.M., Aksit A., Bordin N., Devos D.P.,\nRA   van der Klei I.J.;\nRT   \"Pex24 and Pex32 are required to tether peroxisomes to the ER for organelle\nRT   biogenesis, positioning and segregation in yeast.\";\nRL   J. Cell Sci. 133:0-0(2020).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:55.253871+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 24-31",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "95f12c3e5266dcfc076c0bab33c3d654a00f2c142918715c03c5fb98c2acd8be",
  "url": "https://rest.uniprot.org/unisave/W1QHP2?format=txt&versions=38"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QHP2?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H3",
  "excerpt": "FT   TRANSMEM        24..44\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:55.253871+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 80-82",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "95f12c3e5266dcfc076c0bab33c3d654a00f2c142918715c03c5fb98c2acd8be",
  "url": "https://rest.uniprot.org/unisave/W1QHP2?format=txt&versions=38"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QHP2?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H4",
  "excerpt": "FT   TRANSMEM        63..83\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:55.253871+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 83-85",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "95f12c3e5266dcfc076c0bab33c3d654a00f2c142918715c03c5fb98c2acd8be",
  "url": "https://rest.uniprot.org/unisave/W1QHP2?format=txt&versions=38"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QHP2?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H5",
  "excerpt": "FT   TRANSMEM        84..104\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:55.253871+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 86-88",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "95f12c3e5266dcfc076c0bab33c3d654a00f2c142918715c03c5fb98c2acd8be",
  "url": "https://rest.uniprot.org/unisave/W1QHP2?format=txt&versions=38"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QHP2?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H6",
  "excerpt": "FT   TRANSMEM        151..171\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:55.253871+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 89-91",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "95f12c3e5266dcfc076c0bab33c3d654a00f2c142918715c03c5fb98c2acd8be",
  "url": "https://rest.uniprot.org/unisave/W1QHP2?format=txt&versions=38"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QHP2?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H7",
  "excerpt": "FT   TRANSMEM        173..193\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:55.253871+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 92-94",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "95f12c3e5266dcfc076c0bab33c3d654a00f2c142918715c03c5fb98c2acd8be",
  "url": "https://rest.uniprot.org/unisave/W1QHP2?format=txt&versions=38"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 132. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
