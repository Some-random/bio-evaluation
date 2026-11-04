# transmembrane_0050

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0050.txt)

**Task:** `transmembrane`  
**Expected answer:** **A** — 39..59; 94..114; 117..137; 148..168; 177..197; 217..237; 365..385; 405..425; 433..453; 461..481; 488..508; 528..548

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKDSRGKRRCLAFLKGLRLKTDPNLPGAKQKTPFNISRFWLLVIIVIYTATSACIYFDWSAIRNLLLTVGKYKHLNVGDYPDITLSPQYKRINSLYPITLAIHFTMSVFCGFLYDHIGPKFTAIIGQMCNIMSWVFLSIDSTTVDTTFLSFVFLGLGADTAFIPILTISNLYPDASTFILTVVGAAASLSYAVPATLNFICRRYPSTPFPYICYGYIFLILVPCLLVATFLLPLMPFKGLDYYIERDQSRRSGAEGDAHRGRRGDPKMVTSQTNDEVDVEMQPFENAQSEASKGRSGNGSNTPSTRGNTPNGGKQTRGKTTSESNRSSKGEGSAIQGVEEEDQATNSSKGVNEEDSDFHRKSISLFFKVLLSYPSICIIVYFILFNISTVFYGMVTDTYFSYDRSIINIINILMPISCIPCIIFGRFINRYGSAIIIILMNAFSALMHLTALIKHRAAGLVSAFLYMCVTSIYTSQIYCFIQNSFPSVVFGKLLGFASLCGGLFSLLCEKLYDQIVSKDGASIDPTNVVLLLVIAFILMFLPLTVLYFRKYERSIEDLHQEVAMSQSSGRA

[Multiple Choices]
A. 39..59; 94..114; 117..137; 148..168; 177..197; 217..237; 365..385; 405..425; 433..453; 461..481; 488..508; 528..548
B. 9..29; 41..61; 84..104; 118..138; 153..173; 175..195; 202..222; 231..251
C. 41..61; 94..114; 117..137; 148..168; 177..197; 217..237; 365..385; 405..425; 433..453; 461..481; 488..508; 528..548
D. 39..59; 94..114; 117..137; 148..168; 177..197; 217..237; 365..385; 405..425; 433..453; 461..481; 488..508
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

> The matched sequence has UniProt annotations for all 12 regions in choice A. These are helical transmembrane annotations with computational evidence code ECO:0000255, so they support the key as a computational prediction, not as direct experimental confirmation.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [C13](#evidence-c13), [C14](#evidence-c14), [C15](#evidence-c15), [C16](#evidence-c16).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple long, strongly hydrophobic stretches, consistent with a multipass membrane protein. In the first candidate region, the hydrophobic run begins at F39 immediately after R38; that charged-to-hydrophobic boundary favors A's 39..59 over C's shifted 41..61. The repeated hydrophobic segments also support the multipass pattern represented in A, unlike B's substantially different positions or D's omission of a late segment.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable knowledge about membrane-spanning helices and hydropathy gives a concrete basis to prefer A among the listed patterns. The exact helix boundaries remain predictions from sequence, and the near-identical alternative C makes the first boundary less certain.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> A and C differ only by a two-residue shift in the first proposed helix. Both intervals lie within the same strongly hydrophobic stretch, and sequence alone does not establish a uniquely exact boundary for a membrane helix.


### Important caveats

- The supplied evidence supports computationally annotated regions; it does not establish that each boundary was experimentally measured.
- Transmembrane helix boundaries can be approximate, especially when adjacent intervals are both strongly hydrophobic.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple long, strongly hydrophobic stretches, consistent with a multipass membrane protein. In the first candidate region, the hydrophobic run begins at F39 immediately after R38; that charged-to-hydrophobic boundary favors A's 39..59 over C's shifted 41..61. The repeated hydrophobic segments also support the multipass pattern represented in A, unlike B's substantially different positions or D's omission of a late segment.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge about membrane-spanning helices and hydropathy gives a concrete basis to prefer A among the listed patterns. The exact helix boundaries remain predictions from sequence, and the near-identical alternative C makes the first boundary less certain."
  },
  "case_id": "transmembrane_0050",
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
      "C16"
    ],
    "judgment": "supported",
    "reason": "The matched sequence has UniProt annotations for all 12 regions in choice A. These are helical transmembrane annotations with computational evidence code ECO:0000255, so they support the key as a computational prediction, not as direct experimental confirmation."
  },
  "important_caveats": [
    "The supplied evidence supports computationally annotated regions; it does not establish that each boundary was experimentally measured.",
    "Transmembrane helix boundaries can be approximate, especially when adjacent intervals are both strongly hydrophobic."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "A and C differ only by a two-residue shift in the first proposed helix. Both intervals lie within the same strongly hydrophobic stretch, and sequence alone does not establish a uniquely exact boundary for a membrane helix."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0050",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence has UniProt annotations for all 12 regions in choice A. These are helical transmembrane annotations with computational evidence code ECO:0000255, so they support the key as a computational prediction, not as direct experimental confirmation.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "C14", "C15", "C16"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple long, strongly hydrophobic stretches, consistent with a multipass membrane protein. In the first candidate region, the hydrophobic run begins at F39 immediately after R38; that charged-to-hydrophobic boundary favors A's 39..59 over C's shifted 41..61. The repeated hydrophobic segments also support the multipass pattern represented in A, unlike B's substantially different positions or D's omission of a late segment.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge about membrane-spanning helices and hydropathy gives a concrete basis to prefer A among the listed patterns. The exact helix boundaries remain predictions from sequence, and the near-identical alternative C makes the first boundary less certain."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "A and C differ only by a two-residue shift in the first proposed helix. Both intervals lie within the same strongly hydrophobic stretch, and sequence alone does not establish a uniquely exact boundary for a membrane helix."
  },
  "important_caveats": [
    "The supplied evidence supports computationally annotated regions; it does not establish that each boundary was experimentally measured.",
    "Transmembrane helix boundaries can be approximate, especially when adjacent intervals are both strongly hydrophobic."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A5K9W3 (Cationic amino acid transporter 8, Plasmodium vivax) records exactly 12 transmembrane helical regions: 39..59, 94..114, 117..137, 148..168, 177..197, 217..237, 365..385, 405..425, 433..453, 461..481, 488..508, 528..548. These match Choice A exactly. The sequence SHA256 matches the benchmark input. Note that all annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred by homology rather than experimentally verified, but they are the recorded database annotation for this entry.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [C13](#evidence-c13), [C14](#evidence-c14), [C15](#evidence-c15), [C16](#evidence-c16), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11), [H12](#evidence-h12), [H13](#evidence-h13), [H14](#evidence-h14).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Three transferable lines of reasoning distinguish A from the alternatives: (1) Family-level topology: Amino acid transporters in the APC superfamily (LAT, CAT, ApiAT families) characteristically possess 12 transmembrane helices arranged in two inverted 6-TM repeats. This eliminates B (only 8 TMs confined to the N-terminal ~250 residues, with no TM regions in the C-terminal half despite obvious hydrophobic stretches there). (2) Hydrophobicity boundary analysis: The segment 528..548 (VVL LVI AFILMFLPLTVLYF) is strongly hydrophobic, flanked by charged/polar residues (N527 before, R549 after), making it an unambiguous TM helix. Choice D omits this region and is therefore incomplete. (3) Boundary residue logic for the first TM: Position 38 is Arg (charged, a natural TM boundary), position 39 is Phe (hydrophobic, start of helix), position 59 is Trp (hydrophobic, end of helix), and position 60 is Ser (polar). Choice A's 39..59 respects these boundaries, whereas Choice C's 41..61 excludes two clearly hydrophobic residues (F39, W40) and includes two polar/small residues (S60, A61), which contradicts standard TM boundary assignment principles. Together, these arguments based on sequence hydrophobicity, flanking residue polarity, and family-level 12-TM topology of amino acid transporters allow a knowledgeable model to select A.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The combination of (a) recognizing the 12-TM topology expected for amino acid transporters from family knowledge, (b) performing hydrophobicity analysis on the provided sequence to identify all 12 TM segments including the C-terminal ones, and (c) applying standard boundary-residue logic (charged/polar residues flanking hydrophobic helices) provides a concrete, transferable basis for selecting A over B, C, and D. No fact specific to this exact protein record beyond what is derivable from the sequence itself and general transporter biology is required.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The differences among choices are substantive: B has a completely different TM set (8 TMs in N-terminal half only), D omits a clearly hydrophobic C-terminal TM (528..548), and C shifts the first TM boundary by 2 residues in a way that contradicts flanking-residue polarity logic. While the 2-residue shift between A and C is small, the charged Arg at position 38 and polar Ser at position 60 provide clear justification for the 39..59 boundaries, making A the more defensible choice.


### Important caveats

- All 12 TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred by homology, not experimentally validated helix positions. Exact boundary positions (±1-2 residues) are inherently uncertain for predicted TMs.
- The distinction between A and C (39..59 vs 41..61) relies on boundary-residue logic applied to a 2-residue shift; different prediction tools might assign slightly different boundaries. However, among the four offered choices, A is the most internally consistent.
- The protein is identified as Plasmodium vivax ApiAT8 (A5K9W3) in UniProt, but this identity was not provided to the evaluated model and was not needed for the reasoning.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Three transferable lines of reasoning distinguish A from the alternatives: (1) Family-level topology: Amino acid transporters in the APC superfamily (LAT, CAT, ApiAT families) characteristically possess 12 transmembrane helices arranged in two inverted 6-TM repeats. This eliminates B (only 8 TMs confined to the N-terminal ~250 residues, with no TM regions in the C-terminal half despite obvious hydrophobic stretches there). (2) Hydrophobicity boundary analysis: The segment 528..548 (VVL LVI AFILMFLPLTVLYF) is strongly hydrophobic, flanked by charged/polar residues (N527 before, R549 after), making it an unambiguous TM helix. Choice D omits this region and is therefore incomplete. (3) Boundary residue logic for the first TM: Position 38 is Arg (charged, a natural TM boundary), position 39 is Phe (hydrophobic, start of helix), position 59 is Trp (hydrophobic, end of helix), and position 60 is Ser (polar). Choice A's 39..59 respects these boundaries, whereas Choice C's 41..61 excludes two clearly hydrophobic residues (F39, W40) and includes two polar/small residues (S60, A61), which contradicts standard TM boundary assignment principles. Together, these arguments based on sequence hydrophobicity, flanking residue polarity, and family-level 12-TM topology of amino acid transporters allow a knowledgeable model to select A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The combination of (a) recognizing the 12-TM topology expected for amino acid transporters from family knowledge, (b) performing hydrophobicity analysis on the provided sequence to identify all 12 TM segments including the C-terminal ones, and (c) applying standard boundary-residue logic (charged/polar residues flanking hydrophobic helices) provides a concrete, transferable basis for selecting A over B, C, and D. No fact specific to this exact protein record beyond what is derivable from the sequence itself and general transporter biology is required."
  },
  "case_id": "transmembrane_0050",
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
      "C16",
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
      "H13",
      "H14"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A5K9W3 (Cationic amino acid transporter 8, Plasmodium vivax) records exactly 12 transmembrane helical regions: 39..59, 94..114, 117..137, 148..168, 177..197, 217..237, 365..385, 405..425, 433..453, 461..481, 488..508, 528..548. These match Choice A exactly. The sequence SHA256 matches the benchmark input. Note that all annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred by homology rather than experimentally verified, but they are the recorded database annotation for this entry."
  },
  "important_caveats": [
    "All 12 TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred by homology, not experimentally validated helix positions. Exact boundary positions (±1-2 residues) are inherently uncertain for predicted TMs.",
    "The distinction between A and C (39..59 vs 41..61) relies on boundary-residue logic applied to a 2-residue shift; different prediction tools might assign slightly different boundaries. However, among the four offered choices, A is the most internally consistent.",
    "The protein is identified as Plasmodium vivax ApiAT8 (A5K9W3) in UniProt, but this identity was not provided to the evaluated model and was not needed for the reasoning."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The differences among choices are substantive: B has a completely different TM set (8 TMs in N-terminal half only), D omits a clearly hydrophobic C-terminal TM (528..548), and C shifts the first TM boundary by 2 residues in a way that contradicts flanking-residue polarity logic. While the 2-residue shift between A and C is small, the charged Arg at position 38 and polar Ser at position 60 provide clear justification for the 39..59 boundaries, making A the more defensible choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0050",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A5K9W3 (Cationic amino acid transporter 8, Plasmodium vivax) records exactly 12 transmembrane helical regions: 39..59, 94..114, 117..137, 148..168, 177..197, 217..237, 365..385, 405..425, 433..453, 461..481, 488..508, 528..548. These match Choice A exactly. The sequence SHA256 matches the benchmark input. Note that all annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred by homology rather than experimentally verified, but they are the recorded database annotation for this entry.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "C14", "C15", "C16", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "H11", "H12", "H13", "H14"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Three transferable lines of reasoning distinguish A from the alternatives: (1) Family-level topology: Amino acid transporters in the APC superfamily (LAT, CAT, ApiAT families) characteristically possess 12 transmembrane helices arranged in two inverted 6-TM repeats. This eliminates B (only 8 TMs confined to the N-terminal ~250 residues, with no TM regions in the C-terminal half despite obvious hydrophobic stretches there). (2) Hydrophobicity boundary analysis: The segment 528..548 (VVL LVI AFILMFLPLTVLYF) is strongly hydrophobic, flanked by charged/polar residues (N527 before, R549 after), making it an unambiguous TM helix. Choice D omits this region and is therefore incomplete. (3) Boundary residue logic for the first TM: Position 38 is Arg (charged, a natural TM boundary), position 39 is Phe (hydrophobic, start of helix), position 59 is Trp (hydrophobic, end of helix), and position 60 is Ser (polar). Choice A's 39..59 respects these boundaries, whereas Choice C's 41..61 excludes two clearly hydrophobic residues (F39, W40) and includes two polar/small residues (S60, A61), which contradicts standard TM boundary assignment principles. Together, these arguments based on sequence hydrophobicity, flanking residue polarity, and family-level 12-TM topology of amino acid transporters allow a knowledgeable model to select A.",
    "missing_item_specific_fact": "",
    "reason": "The combination of (a) recognizing the 12-TM topology expected for amino acid transporters from family knowledge, (b) performing hydrophobicity analysis on the provided sequence to identify all 12 TM segments including the C-terminal ones, and (c) applying standard boundary-residue logic (charged/polar residues flanking hydrophobic helices) provides a concrete, transferable basis for selecting A over B, C, and D. No fact specific to this exact protein record beyond what is derivable from the sequence itself and general transporter biology is required."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The differences among choices are substantive: B has a completely different TM set (8 TMs in N-terminal half only), D omits a clearly hydrophobic C-terminal TM (528..548), and C shifts the first TM boundary by 2 residues in a way that contradicts flanking-residue polarity logic. While the 2-residue shift between A and C is small, the charged Arg at position 38 and polar Ser at position 60 provide clear justification for the 39..59 boundaries, making A the more defensible choice."
  },
  "important_caveats": [
    "All 12 TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred by homology, not experimentally validated helix positions. Exact boundary positions (±1-2 residues) are inherently uncertain for predicted TMs.",
    "The distinction between A and C (39..59 vs 41..61) relies on boundary-residue logic applied to a 2-residue shift; different prediction tools might assign slightly different boundaries. However, among the four offered choices, A is the most internally consistent.",
    "The protein is identified as Plasmodium vivax ApiAT8 (A5K9W3) in UniProt, but this identity was not provided to the evaluated model and was not needed for the reasoning."
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
  "benchmark_sequence_length": 571,
  "benchmark_sequence_sha256": "a7c2b0bec62f4a9189c515f87b771d40fcc353c1911613979f9b3acbd6355174",
  "current_entry_audit": {
    "entryVersion": 71,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2007-07-10",
    "sequenceVersion": 1
  },
  "current_record_sha256": "4f0bdab5e9e7326eb9b6a761a41895f5bb4b5b9bae7c92cfc419fe755650b7a7",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 571,
  "current_source_sequence_sha256": "a7c2b0bec62f4a9189c515f87b771d40fcc353c1911613979f9b3acbd6355174",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 70,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A5K9W3",
  "selected_historical_entry_version": 70,
  "selected_historical_record_sha256": "5fa55f18851f98378363667b0094890e54d37ee80e9a4c1b8d3f1f7eec1b9221",
  "selected_historical_source_sequence_length": 571,
  "selected_historical_source_sequence_sha256": "a7c2b0bec62f4a9189c515f87b771d40fcc353c1911613979f9b3acbd6355174",
  "selected_historical_version": {
    "accession": "A5K9W3",
    "database": "Swiss-Prot",
    "entryVersion": 70,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "AT8_PLAVS",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K9W3.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A5K9W3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:27:03.679737+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f0bdab5e9e7326eb9b6a761a41895f5bb4b5b9bae7c92cfc419fe755650b7a7",
  "url": "https://rest.uniprot.org/uniprotkb/A5K9W3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K9W3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":71,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2007-07-10\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:27:03.679737+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f0bdab5e9e7326eb9b6a761a41895f5bb4b5b9bae7c92cfc419fe755650b7a7",
  "url": "https://rest.uniprot.org/uniprotkb/A5K9W3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K9W3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000008333\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Aconoidasida\",\"Haemosporida\",\"Plasmodiidae\",\"Plasmodium\",\"Plasmodium\"],\"scientificName\":\"Plasmodium vivax (strain Salvador I)\",\"taxonId\":126793}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:27:03.679737+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f0bdab5e9e7326eb9b6a761a41895f5bb4b5b9bae7c92cfc419fe755650b7a7",
  "url": "https://rest.uniprot.org/uniprotkb/A5K9W3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K9W3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39905186\",\"source\":\"PubMed\"}],\"value\":\"Apicomplexan amino acid transporter 8\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39905186\",\"source\":\"PubMed\"}],\"value\":\"PvApiAT8\"}]},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39905186\",\"source\":\"PubMed\"}],\"value\":\"Novel putative transporter 1\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Cationic amino acid transporter 8\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:27:03.679737+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f0bdab5e9e7326eb9b6a761a41895f5bb4b5b9bae7c92cfc419fe755650b7a7",
  "url": "https://rest.uniprot.org/uniprotkb/A5K9W3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K9W3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":59},\"start\":{\"modifier\":\"EXACT\",\"value\":39}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:27:03.679737+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f0bdab5e9e7326eb9b6a761a41895f5bb4b5b9bae7c92cfc419fe755650b7a7",
  "url": "https://rest.uniprot.org/uniprotkb/A5K9W3.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K9W3.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":114},\"start\":{\"modifier\":\"EXACT\",\"value\":94}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:27:03.679737+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f0bdab5e9e7326eb9b6a761a41895f5bb4b5b9bae7c92cfc419fe755650b7a7",
  "url": "https://rest.uniprot.org/uniprotkb/A5K9W3.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K9W3.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":137},\"start\":{\"modifier\":\"EXACT\",\"value\":117}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:27:03.679737+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f0bdab5e9e7326eb9b6a761a41895f5bb4b5b9bae7c92cfc419fe755650b7a7",
  "url": "https://rest.uniprot.org/uniprotkb/A5K9W3.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K9W3.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":168},\"start\":{\"modifier\":\"EXACT\",\"value\":148}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:27:03.679737+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f0bdab5e9e7326eb9b6a761a41895f5bb4b5b9bae7c92cfc419fe755650b7a7",
  "url": "https://rest.uniprot.org/uniprotkb/A5K9W3.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K9W3.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":197},\"start\":{\"modifier\":\"EXACT\",\"value\":177}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:27:03.679737+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f0bdab5e9e7326eb9b6a761a41895f5bb4b5b9bae7c92cfc419fe755650b7a7",
  "url": "https://rest.uniprot.org/uniprotkb/A5K9W3.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K9W3.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":237},\"start\":{\"modifier\":\"EXACT\",\"value\":217}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:27:03.679737+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f0bdab5e9e7326eb9b6a761a41895f5bb4b5b9bae7c92cfc419fe755650b7a7",
  "url": "https://rest.uniprot.org/uniprotkb/A5K9W3.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K9W3.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":385},\"start\":{\"modifier\":\"EXACT\",\"value\":365}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:27:03.679737+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f0bdab5e9e7326eb9b6a761a41895f5bb4b5b9bae7c92cfc419fe755650b7a7",
  "url": "https://rest.uniprot.org/uniprotkb/A5K9W3.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K9W3.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":425},\"start\":{\"modifier\":\"EXACT\",\"value\":405}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:27:03.679737+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f0bdab5e9e7326eb9b6a761a41895f5bb4b5b9bae7c92cfc419fe755650b7a7",
  "url": "https://rest.uniprot.org/uniprotkb/A5K9W3.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K9W3.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":453},\"start\":{\"modifier\":\"EXACT\",\"value\":433}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-02T04:27:03.679737+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f0bdab5e9e7326eb9b6a761a41895f5bb4b5b9bae7c92cfc419fe755650b7a7",
  "url": "https://rest.uniprot.org/uniprotkb/A5K9W3.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K9W3.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":481},\"start\":{\"modifier\":\"EXACT\",\"value\":461}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-02T04:27:03.679737+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f0bdab5e9e7326eb9b6a761a41895f5bb4b5b9bae7c92cfc419fe755650b7a7",
  "url": "https://rest.uniprot.org/uniprotkb/A5K9W3.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K9W3.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":508},\"start\":{\"modifier\":\"EXACT\",\"value\":488}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/11",
  "retrieved_utc": "2026-11-02T04:27:03.679737+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f0bdab5e9e7326eb9b6a761a41895f5bb4b5b9bae7c92cfc419fe755650b7a7",
  "url": "https://rest.uniprot.org/uniprotkb/A5K9W3.json"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K9W3.json)

```json
{
  "evidence_id": "C16",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":548},\"start\":{\"modifier\":\"EXACT\",\"value\":528}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/12",
  "retrieved_utc": "2026-11-02T04:27:03.679737+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f0bdab5e9e7326eb9b6a761a41895f5bb4b5b9bae7c92cfc419fe755650b7a7",
  "url": "https://rest.uniprot.org/uniprotkb/A5K9W3.json"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K9W3.json)

```json
{
  "evidence_id": "C17",
  "excerpt": "{\"citation\":{\"authors\":[\"Lee W.J.\",\"Mazigo E.\",\"Han J.H.\",\"Cha S.H.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39905186\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41598-025-88746-2\"}],\"citationType\":\"journal article\",\"firstPage\":\"4234\",\"id\":\"39905186\",\"journal\":\"Sci. Rep.\",\"lastPage\":\"4234\",\"publicationDate\":\"2025\",\"title\":\"Characteristics of Plasmodium vivax apicomplexan amino acid transporter 8 (PvApiAT8) in the cationic amino acid transport.\",\"volume\":\"15\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"TRANSPORTER ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:27:03.679737+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f0bdab5e9e7326eb9b6a761a41895f5bb4b5b9bae7c92cfc419fe755650b7a7",
  "url": "https://rest.uniprot.org/uniprotkb/A5K9W3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K9W3?format=txt&versions=70)

```json
{
  "entry_version": 70,
  "evidence_id": "H1",
  "excerpt": "ID   AT8_PLAVS               Reviewed;         571 AA.\nAC   A5K9W3;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   10-JUL-2007, sequence version 1.\nDT   28-JAN-2026, entry version 70.\nDE   RecName: Full=Cationic amino acid transporter 8 {ECO:0000305};\nDE   AltName: Full=Apicomplexan amino acid transporter 8 {ECO:0000303|PubMed:39905186};\nDE            Short=PvApiAT8 {ECO:0000303|PubMed:39905186};\nDE   AltName: Full=Novel putative transporter 1 {ECO:0000303|PubMed:39905186};\nGN   Name=NPT1 {ECO:0000303|PubMed:39905186}; Synonyms=ApiAT8 {ECO:0000305};\nGN   ORFNames=PVX_081515 {ECO:0000312|EMBL:EDL43851.1};\nOS   Plasmodium vivax (strain Salvador I).\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;\nOC   Plasmodiidae; Plasmodium; Plasmodium (Plasmodium).\nOX   NCBI_TaxID=126793 {ECO:0000312|Proteomes:UP000008333};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:11.338974+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5fa55f18851f98378363667b0094890e54d37ee80e9a4c1b8d3f1f7eec1b9221",
  "url": "https://rest.uniprot.org/unisave/A5K9W3?format=txt&versions=70"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K9W3?format=txt&versions=70)

```json
{
  "entry_version": 70,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, TRANSPORTER ACTIVITY, AND BIOPHYSICOCHEMICAL PROPERTIES.\nRX   PubMed=39905186; DOI=10.1038/s41598-025-88746-2;\nRA   Lee W.J., Mazigo E., Han J.H., Cha S.H.;\nRT   \"Characteristics of Plasmodium vivax apicomplexan amino acid transporter 8\nRT   (PvApiAT8) in the cationic amino acid transport.\";\nRL   Sci. Rep. 15:4234-4234(2025).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:11.338974+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 31-37",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5fa55f18851f98378363667b0094890e54d37ee80e9a4c1b8d3f1f7eec1b9221",
  "url": "https://rest.uniprot.org/unisave/A5K9W3?format=txt&versions=70"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K9W3?format=txt&versions=70)

```json
{
  "entry_version": 70,
  "evidence_id": "H3",
  "excerpt": "FT   TRANSMEM        39..59\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:11.338974+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 83-85",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5fa55f18851f98378363667b0094890e54d37ee80e9a4c1b8d3f1f7eec1b9221",
  "url": "https://rest.uniprot.org/unisave/A5K9W3?format=txt&versions=70"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K9W3?format=txt&versions=70)

```json
{
  "entry_version": 70,
  "evidence_id": "H4",
  "excerpt": "FT   TRANSMEM        94..114\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:11.338974+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 86-88",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5fa55f18851f98378363667b0094890e54d37ee80e9a4c1b8d3f1f7eec1b9221",
  "url": "https://rest.uniprot.org/unisave/A5K9W3?format=txt&versions=70"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K9W3?format=txt&versions=70)

```json
{
  "entry_version": 70,
  "evidence_id": "H5",
  "excerpt": "FT   TRANSMEM        117..137\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:11.338974+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 89-91",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5fa55f18851f98378363667b0094890e54d37ee80e9a4c1b8d3f1f7eec1b9221",
  "url": "https://rest.uniprot.org/unisave/A5K9W3?format=txt&versions=70"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K9W3?format=txt&versions=70)

```json
{
  "entry_version": 70,
  "evidence_id": "H6",
  "excerpt": "FT   TRANSMEM        148..168\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:11.338974+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 92-94",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5fa55f18851f98378363667b0094890e54d37ee80e9a4c1b8d3f1f7eec1b9221",
  "url": "https://rest.uniprot.org/unisave/A5K9W3?format=txt&versions=70"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K9W3?format=txt&versions=70)

```json
{
  "entry_version": 70,
  "evidence_id": "H7",
  "excerpt": "FT   TRANSMEM        177..197\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:11.338974+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 95-97",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5fa55f18851f98378363667b0094890e54d37ee80e9a4c1b8d3f1f7eec1b9221",
  "url": "https://rest.uniprot.org/unisave/A5K9W3?format=txt&versions=70"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K9W3?format=txt&versions=70)

```json
{
  "entry_version": 70,
  "evidence_id": "H8",
  "excerpt": "FT   TRANSMEM        217..237\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:11.338974+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 98-100",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5fa55f18851f98378363667b0094890e54d37ee80e9a4c1b8d3f1f7eec1b9221",
  "url": "https://rest.uniprot.org/unisave/A5K9W3?format=txt&versions=70"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K9W3?format=txt&versions=70)

```json
{
  "entry_version": 70,
  "evidence_id": "H9",
  "excerpt": "FT   TRANSMEM        365..385\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:11.338974+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 101-103",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5fa55f18851f98378363667b0094890e54d37ee80e9a4c1b8d3f1f7eec1b9221",
  "url": "https://rest.uniprot.org/unisave/A5K9W3?format=txt&versions=70"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K9W3?format=txt&versions=70)

```json
{
  "entry_version": 70,
  "evidence_id": "H10",
  "excerpt": "FT   TRANSMEM        405..425\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:11.338974+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 104-106",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5fa55f18851f98378363667b0094890e54d37ee80e9a4c1b8d3f1f7eec1b9221",
  "url": "https://rest.uniprot.org/unisave/A5K9W3?format=txt&versions=70"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K9W3?format=txt&versions=70)

```json
{
  "entry_version": 70,
  "evidence_id": "H11",
  "excerpt": "FT   TRANSMEM        433..453\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:11.338974+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 107-109",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5fa55f18851f98378363667b0094890e54d37ee80e9a4c1b8d3f1f7eec1b9221",
  "url": "https://rest.uniprot.org/unisave/A5K9W3?format=txt&versions=70"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K9W3?format=txt&versions=70)

```json
{
  "entry_version": 70,
  "evidence_id": "H12",
  "excerpt": "FT   TRANSMEM        461..481\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:11.338974+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 110-112",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5fa55f18851f98378363667b0094890e54d37ee80e9a4c1b8d3f1f7eec1b9221",
  "url": "https://rest.uniprot.org/unisave/A5K9W3?format=txt&versions=70"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K9W3?format=txt&versions=70)

```json
{
  "entry_version": 70,
  "evidence_id": "H13",
  "excerpt": "FT   TRANSMEM        488..508\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:11.338974+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 113-115",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5fa55f18851f98378363667b0094890e54d37ee80e9a4c1b8d3f1f7eec1b9221",
  "url": "https://rest.uniprot.org/unisave/A5K9W3?format=txt&versions=70"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K9W3?format=txt&versions=70)

```json
{
  "entry_version": 70,
  "evidence_id": "H14",
  "excerpt": "FT   TRANSMEM        528..548\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:11.338974+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 116-118",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5fa55f18851f98378363667b0094890e54d37ee80e9a4c1b8d3f1f7eec1b9221",
  "url": "https://rest.uniprot.org/unisave/A5K9W3?format=txt&versions=70"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 50. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
