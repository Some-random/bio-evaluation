# transmembrane_0100

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0100.txt)

**Task:** `transmembrane`  
**Expected answer:** **C** — 1..21; 31..51; 56..76; 77..97; 101..121; 128..148; 149..169; 182..202; 206..226; 321..341

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MFGFDNLILGVYLFNFLLILTATYTDIKERIIPHFVIILMLIVNLPIGYYFFGFDAITSFFATLILCLILGVGMGGGDVKMFTALSPLFAAETIYFVPKDISILIGLSALFAAIFPMTKILKNYWKDIIPSSAYLAMLIGIIVSITEIYSIGNTKTILWSYIILSIFISRKIPKYRIISNKLGYITPIYLIGFYLLNPAYFVSENVLISFFVYIGQLSLISLVIYALTGAEISSKKQISDLKEGDIIRDIVTIKENGEVTVENANILKRFKHMIYGEMGKLEGKSLMTDGEGLSDENLELLNKLQNEGKIGGELNVLTTYPFVPFVLVAYCVITLLNMGVINYLVG

[Multiple Choices]
A. 357..377; 397..419; 481..501; 506..526; 591..611; 619..639
B. 1..21; 33..56; 56..76; 77..97; 101..121; 128..148; 149..169; 182..202; 206..226; 321..341
C. 1..21; 31..51; 56..76; 77..97; 101..121; 128..148; 149..169; 182..202; 206..226; 321..341
D. 1..21; 31..51; 56..76; 101..121; 128..148; 149..169; 182..202; 206..226; 321..341
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

> The sequence-matched UniProt record annotates the ten regions in choice C as transmembrane helices. These annotations are computational (ECO:0000255), so they support the key but are not experimental confirmation.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [C13](#evidence-c13), [C14](#evidence-c14).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has many long, strongly hydrophobic stretches, consistent with a multi-pass membrane protein. This supports the shared predicted spans and favors including the hydrophobic 77–97 region over choice D, which omits it. Between B and C, 31–51 is a better hydrophobic-span candidate than 33–56: the latter extends through Asp55, while the sequence includes hydrophobic residues at 31–32. This is a transferable hydropathy-based inference, not proof of exact boundaries.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence provides meaningful evidence for the multi-pass topology and favors C's segmentation, though hydropathy alone cannot establish every boundary with annotation-level precision.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> B and C share the same predicted spans except for the first disputed segment: both coordinate ranges overlap a strongly hydrophobic stretch capable of spanning a membrane. The sequence favors C, particularly because B includes Asp55, but the exact helix boundaries are not uniquely determined by the sequence.


### Important caveats

- The supporting database annotations are computational rather than experimentally established in the supplied evidence.
- Exact transmembrane boundaries can be uncertain even when the presence of a membrane-spanning helix is strongly supported.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has many long, strongly hydrophobic stretches, consistent with a multi-pass membrane protein. This supports the shared predicted spans and favors including the hydrophobic 77–97 region over choice D, which omits it. Between B and C, 31–51 is a better hydrophobic-span candidate than 33–56: the latter extends through Asp55, while the sequence includes hydrophobic residues at 31–32. This is a transferable hydropathy-based inference, not proof of exact boundaries.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence provides meaningful evidence for the multi-pass topology and favors C's segmentation, though hydropathy alone cannot establish every boundary with annotation-level precision."
  },
  "case_id": "transmembrane_0100",
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
      "C14"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the ten regions in choice C as transmembrane helices. These annotations are computational (ECO:0000255), so they support the key but are not experimental confirmation."
  },
  "important_caveats": [
    "The supporting database annotations are computational rather than experimentally established in the supplied evidence.",
    "Exact transmembrane boundaries can be uncertain even when the presence of a membrane-spanning helix is strongly supported."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "B and C share the same predicted spans except for the first disputed segment: both coordinate ranges overlap a strongly hydrophobic stretch capable of spanning a membrane. The sequence favors C, particularly because B includes Asp55, but the exact helix boundaries are not uniquely determined by the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0100",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the ten regions in choice C as transmembrane helices. These annotations are computational (ECO:0000255), so they support the key but are not experimental confirmation.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "C14"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has many long, strongly hydrophobic stretches, consistent with a multi-pass membrane protein. This supports the shared predicted spans and favors including the hydrophobic 77–97 region over choice D, which omits it. Between B and C, 31–51 is a better hydrophobic-span candidate than 33–56: the latter extends through Asp55, while the sequence includes hydrophobic residues at 31–32. This is a transferable hydropathy-based inference, not proof of exact boundaries.",
    "missing_item_specific_fact": "",
    "reason": "The sequence provides meaningful evidence for the multi-pass topology and favors C's segmentation, though hydropathy alone cannot establish every boundary with annotation-level precision."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "B and C share the same predicted spans except for the first disputed segment: both coordinate ranges overlap a strongly hydrophobic stretch capable of spanning a membrane. The sequence favors C, particularly because B includes Asp55, but the exact helix boundaries are not uniquely determined by the sequence."
  },
  "important_caveats": [
    "The supporting database annotations are computational rather than experimentally established in the supplied evidence.",
    "Exact transmembrane boundaries can be uncertain even when the presence of a membrane-spanning helix is strongly supported."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for Q6M0N8 (Prepilin peptidase EppA, 346 AA) lists exactly 10 transmembrane helices at positions 1..21, 31..51, 56..76, 77..97, 101..121, 128..148, 149..169, 182..202, 206..226, and 321..341, matching choice C precisely. The evidence code ECO:0000255 indicates these are inferred by similarity (computational annotation), not experimentally determined, but the annotation is consistent and matches the expected answer exactly.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [C13](#evidence-c13), [C14](#evidence-c14), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11), [H12](#evidence-h12), [H13](#evidence-h13).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Choice A is immediately eliminated because all listed positions (357-639) exceed the 346-residue protein length. Between B and C, the key difference is the second segment: B lists 33..56 while C lists 31..51. In B, segments 33..56 and 56..76 overlap at position 56, which is structurally inconsistent with discrete TM helices separated by loops. In C, 31..51 and 56..76 are cleanly separated by a short loop (52-55: FFGF), and position 31 (Ile) is more hydrophobic than position 33 (Pro, a helix breaker), making 31 a more natural helix start. Between C and D, the difference is inclusion of 77..97. Prepilin peptidases (type IV prepilin peptidase family, e.g., PilD homologs) are well-characterized multi-pass membrane proteins with approximately 10 TM helices. The 77..97 segment is 21 residues (appropriate TM length), flanked by two clear TM helices (56..76 and 101..121), and while somewhat polar, contains sufficient hydrophobic residues (V, M, F, L, F, A, I, F, V) to potentially span the bilayer. Excluding it would leave a 24-residue gap between adjacent TM segments, which is atypical for closely packed multi-pass membrane proteins. Family-level knowledge that prepilin peptidases have ~10 TM segments supports including this borderline helix, favoring C (10 segments) over D (9 segments).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence itself plus family knowledge of prepilin peptidase topology (approximately 10 TM helices, regular helix spacing, avoidance of helix overlap) provides a credible inference chain that distinguishes C from the alternatives. The overlap argument eliminates B, the length argument eliminates A, and family-level TM count plus spacing regularity supports C over D. The 77..97 segment is borderline in hydrophobicity, introducing some uncertainty, but the structural context and family analogy provide a defensible probabilistic argument.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> The 77..97 segment has notably polar character (D, K, S, P, E, T, Y among 21 residues), making its classification as a TM helix borderline. A model relying purely on hydrophobicity thresholds might reasonably exclude it and select D. The argument for including it relies on family-level TM count expectations and spacing regularity, which is a probabilistic inference rather than a definitive sequence-based call. However, the overlap elimination of B and the length elimination of A are unambiguous.


### Important caveats

- The UniProt TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational/homology-based rather than experimentally determined.
- The 77..97 segment has average hydropathy well below typical TM helix thresholds, making its inclusion genuinely borderline from pure sequence analysis.
- The overlap in choice B (segments 33..56 and 56..76 sharing position 56) is a strong structural argument against B that does not require target-specific knowledge.
- Prepilin peptidase family topology knowledge (approximately 10 TM helices) is the primary transferable basis for distinguishing C from D.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Choice A is immediately eliminated because all listed positions (357-639) exceed the 346-residue protein length. Between B and C, the key difference is the second segment: B lists 33..56 while C lists 31..51. In B, segments 33..56 and 56..76 overlap at position 56, which is structurally inconsistent with discrete TM helices separated by loops. In C, 31..51 and 56..76 are cleanly separated by a short loop (52-55: FFGF), and position 31 (Ile) is more hydrophobic than position 33 (Pro, a helix breaker), making 31 a more natural helix start. Between C and D, the difference is inclusion of 77..97. Prepilin peptidases (type IV prepilin peptidase family, e.g., PilD homologs) are well-characterized multi-pass membrane proteins with approximately 10 TM helices. The 77..97 segment is 21 residues (appropriate TM length), flanked by two clear TM helices (56..76 and 101..121), and while somewhat polar, contains sufficient hydrophobic residues (V, M, F, L, F, A, I, F, V) to potentially span the bilayer. Excluding it would leave a 24-residue gap between adjacent TM segments, which is atypical for closely packed multi-pass membrane proteins. Family-level knowledge that prepilin peptidases have ~10 TM segments supports including this borderline helix, favoring C (10 segments) over D (9 segments).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence itself plus family knowledge of prepilin peptidase topology (approximately 10 TM helices, regular helix spacing, avoidance of helix overlap) provides a credible inference chain that distinguishes C from the alternatives. The overlap argument eliminates B, the length argument eliminates A, and family-level TM count plus spacing regularity supports C over D. The 77..97 segment is borderline in hydrophobicity, introducing some uncertainty, but the structural context and family analogy provide a defensible probabilistic argument."
  },
  "case_id": "transmembrane_0100",
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
    "reason": "The UniProt annotation for Q6M0N8 (Prepilin peptidase EppA, 346 AA) lists exactly 10 transmembrane helices at positions 1..21, 31..51, 56..76, 77..97, 101..121, 128..148, 149..169, 182..202, 206..226, and 321..341, matching choice C precisely. The evidence code ECO:0000255 indicates these are inferred by similarity (computational annotation), not experimentally determined, but the annotation is consistent and matches the expected answer exactly."
  },
  "important_caveats": [
    "The UniProt TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational/homology-based rather than experimentally determined.",
    "The 77..97 segment has average hydropathy well below typical TM helix thresholds, making its inclusion genuinely borderline from pure sequence analysis.",
    "The overlap in choice B (segments 33..56 and 56..76 sharing position 56) is a strong structural argument against B that does not require target-specific knowledge.",
    "Prepilin peptidase family topology knowledge (approximately 10 TM helices) is the primary transferable basis for distinguishing C from D."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "The 77..97 segment has notably polar character (D, K, S, P, E, T, Y among 21 residues), making its classification as a TM helix borderline. A model relying purely on hydrophobicity thresholds might reasonably exclude it and select D. The argument for including it relies on family-level TM count expectations and spacing regularity, which is a probabilistic inference rather than a definitive sequence-based call. However, the overlap elimination of B and the length elimination of A are unambiguous."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{"case_id":"transmembrane_0100","expected_answer_check":{"judgment":"supported","reason":"The UniProt annotation for Q6M0N8 (Prepilin peptidase EppA, 346 AA) lists exactly 10 transmembrane helices at positions 1..21, 31..51, 56..76, 77..97, 101..121, 128..148, 149..169, 182..202, 206..226, and 321..341, matching choice C precisely. The evidence code ECO:0000255 indicates these are inferred by similarity (computational annotation), not experimentally determined, but the annotation is consistent and matches the expected answer exactly.","evidence_ids":["C5","C6","C7","C8","C9","C10","C11","C12","C13","C14","H4","H5","H6","H7","H8","H9","H10","H11","H12","H13"]},"answerability_check":{"judgment":"reasoning_supported","discriminating_biological_argument":"Choice A is immediately eliminated because all listed positions (357-639) exceed the 346-residue protein length. Between B and C, the key difference is the second segment: B lists 33..56 while C lists 31..51. In B, segments 33..56 and 56..76 overlap at position 56, which is structurally inconsistent with discrete TM helices separated by loops. In C, 31..51 and 56..76 are cleanly separated by a short loop (52-55: FFGF), and position 31 (Ile) is more hydrophobic than position 33 (Pro, a helix breaker), making 31 a more natural helix start. Between C and D, the difference is inclusion of 77..97. Prepilin peptidases (type IV prepilin peptidase family, e.g., PilD homologs) are well-characterized multi-pass membrane proteins with approximately 10 TM helices. The 77..97 segment is 21 residues (appropriate TM length), flanked by two clear TM helices (56..76 and 101..121), and while somewhat polar, contains sufficient hydrophobic residues (V, M, F, L, F, A, I, F, V) to potentially span the bilayer. Excluding it would leave a 24-residue gap between adjacent TM segments, which is atypical for closely packed multi-pass membrane proteins. Family-level knowledge that prepilin peptidases have ~10 TM segments supports including this borderline helix, favoring C (10 segments) over D (9 segments).","missing_item_specific_fact":"","reason":"The sequence itself plus family knowledge of prepilin peptidase topology (approximately 10 TM helices, regular helix spacing, avoidance of helix overlap) provides a credible inference chain that distinguishes C from the alternatives. The overlap argument eliminates B, the length argument eliminates A, and family-level TM count plus spacing regularity supports C over D. The 77..97 segment is borderline in hydrophobicity, introducing some uncertainty, but the structural context and family analogy provide a defensible probabilistic argument."},"question_ambiguity":{"multiple_defensible_options":["C","D"],"reason":"The 77..97 segment has notably polar character (D, K, S, P, E, T, Y among 21 residues), making its classification as a TM helix borderline. A model relying purely on hydrophobicity thresholds might reasonably exclude it and select D. The argument for including it relies on family-level TM count expectations and spacing regularity, which is a probabilistic inference rather than a definitive sequence-based call. However, the overlap elimination of B and the length elimination of A are unambiguous."},"important_caveats":["The UniProt TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational/homology-based rather than experimentally determined.","The 77..97 segment has average hydropathy well below typical TM helix thresholds, making its inclusion genuinely borderline from pure sequence analysis.","The overlap in choice B (segments 33..56 and 56..76 sharing position 56) is a strong structural argument against B that does not require target-specific knowledge.","Prepilin peptidase family topology knowledge (approximately 10 TM helices) is the primary transferable basis for distinguishing C from D."]}
```

</details>

## Complete reviewer-only evidence and qualifications

These source excerpts were available to the reviewers. They were not included in the original benchmark-solving input.

**Source applicability:**

```json
{
  "actual_author_source_snapshot": "unknown",
  "benchmark_sequence_length": 346,
  "benchmark_sequence_sha256": "02492f034a0c05024df5aaf34285525a00d9c31d340f6cc1dc3359d761712204",
  "current_entry_audit": {
    "entryVersion": 83,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2004-07-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "7a4af27303c7c5267346a50d5911ef3e3a55003fa5cc3be434c4311406e03db3",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 346,
  "current_source_sequence_sha256": "02492f034a0c05024df5aaf34285525a00d9c31d340f6cc1dc3359d761712204",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 82,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q6M0N8",
  "selected_historical_entry_version": 82,
  "selected_historical_record_sha256": "db360aef5d1ea6667df242a1cc2d0cea06cc60f4f37e16fbd6c154d182306232",
  "selected_historical_source_sequence_length": 346,
  "selected_historical_source_sequence_sha256": "02492f034a0c05024df5aaf34285525a00d9c31d340f6cc1dc3359d761712204",
  "selected_historical_version": {
    "accession": "Q6M0N8",
    "database": "Swiss-Prot",
    "entryVersion": 82,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "EPPA_METMP",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6M0N8.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q6M0N8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:31:42.105570+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7a4af27303c7c5267346a50d5911ef3e3a55003fa5cc3be434c4311406e03db3",
  "url": "https://rest.uniprot.org/uniprotkb/Q6M0N8.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6M0N8.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":83,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2004-07-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:31:42.105570+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7a4af27303c7c5267346a50d5911ef3e3a55003fa5cc3be434c4311406e03db3",
  "url": "https://rest.uniprot.org/uniprotkb/Q6M0N8.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6M0N8.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Archaea\",\"Methanobacteriati\",\"Methanobacteriota\",\"Methanomada group\",\"Methanococci\",\"Methanococcales\",\"Methanococcaceae\",\"Methanococcus\"],\"scientificName\":\"Methanococcus maripaludis (strain DSM 14266 / JCM 13030 / NBRC 101832 / S2 / LL)\",\"taxonId\":267377}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:31:42.105570+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7a4af27303c7c5267346a50d5911ef3e3a55003fa5cc3be434c4311406e03db3",
  "url": "https://rest.uniprot.org/uniprotkb/Q6M0N8.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6M0N8.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"17114255\",\"source\":\"PubMed\"}],\"value\":\"Euryarchaeal type IV prepilin peptidase\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"17114255\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"25569238\",\"source\":\"PubMed\"}],\"value\":\"3.4.-.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"17114255\",\"source\":\"PubMed\"}],\"value\":\"Prepilin peptidase EppA\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:31:42.105570+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7a4af27303c7c5267346a50d5911ef3e3a55003fa5cc3be434c4311406e03db3",
  "url": "https://rest.uniprot.org/uniprotkb/Q6M0N8.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6M0N8.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":21},\"start\":{\"modifier\":\"EXACT\",\"value\":1}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:31:42.105570+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7a4af27303c7c5267346a50d5911ef3e3a55003fa5cc3be434c4311406e03db3",
  "url": "https://rest.uniprot.org/uniprotkb/Q6M0N8.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6M0N8.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":51},\"start\":{\"modifier\":\"EXACT\",\"value\":31}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:31:42.105570+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7a4af27303c7c5267346a50d5911ef3e3a55003fa5cc3be434c4311406e03db3",
  "url": "https://rest.uniprot.org/uniprotkb/Q6M0N8.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6M0N8.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":76},\"start\":{\"modifier\":\"EXACT\",\"value\":56}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:31:42.105570+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7a4af27303c7c5267346a50d5911ef3e3a55003fa5cc3be434c4311406e03db3",
  "url": "https://rest.uniprot.org/uniprotkb/Q6M0N8.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6M0N8.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":97},\"start\":{\"modifier\":\"EXACT\",\"value\":77}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:31:42.105570+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7a4af27303c7c5267346a50d5911ef3e3a55003fa5cc3be434c4311406e03db3",
  "url": "https://rest.uniprot.org/uniprotkb/Q6M0N8.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6M0N8.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":121},\"start\":{\"modifier\":\"EXACT\",\"value\":101}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:31:42.105570+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7a4af27303c7c5267346a50d5911ef3e3a55003fa5cc3be434c4311406e03db3",
  "url": "https://rest.uniprot.org/uniprotkb/Q6M0N8.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6M0N8.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":148},\"start\":{\"modifier\":\"EXACT\",\"value\":128}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:31:42.105570+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7a4af27303c7c5267346a50d5911ef3e3a55003fa5cc3be434c4311406e03db3",
  "url": "https://rest.uniprot.org/uniprotkb/Q6M0N8.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6M0N8.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":169},\"start\":{\"modifier\":\"EXACT\",\"value\":149}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:31:42.105570+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7a4af27303c7c5267346a50d5911ef3e3a55003fa5cc3be434c4311406e03db3",
  "url": "https://rest.uniprot.org/uniprotkb/Q6M0N8.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6M0N8.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":202},\"start\":{\"modifier\":\"EXACT\",\"value\":182}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:31:42.105570+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7a4af27303c7c5267346a50d5911ef3e3a55003fa5cc3be434c4311406e03db3",
  "url": "https://rest.uniprot.org/uniprotkb/Q6M0N8.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6M0N8.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":226},\"start\":{\"modifier\":\"EXACT\",\"value\":206}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-02T04:31:42.105570+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7a4af27303c7c5267346a50d5911ef3e3a55003fa5cc3be434c4311406e03db3",
  "url": "https://rest.uniprot.org/uniprotkb/Q6M0N8.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6M0N8.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":341},\"start\":{\"modifier\":\"EXACT\",\"value\":321}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-02T04:31:42.105570+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7a4af27303c7c5267346a50d5911ef3e3a55003fa5cc3be434c4311406e03db3",
  "url": "https://rest.uniprot.org/uniprotkb/Q6M0N8.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6M0N8.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"citation\":{\"authors\":[\"Szabo Z.\",\"Stahl A.O.\",\"Albers S.V.\",\"Kissinger J.C.\",\"Driessen A.J.\",\"Pohlschroeder M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"17114255\"},{\"database\":\"DOI\",\"id\":\"10.1128/jb.01547-06\"}],\"citationType\":\"journal article\",\"firstPage\":\"772\",\"id\":\"17114255\",\"journal\":\"J. Bacteriol.\",\"lastPage\":\"778\",\"publicationDate\":\"2007\",\"title\":\"Identification of diverse archaeal proteins with class III signal peptides cleaved by distinct archaeal prepilin peptidases.\",\"volume\":\"189\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"DSM 14266 / JCM 13030 / NBRC 101832 / S2 / LL\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION AS A PEPTIDASE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:31:42.105570+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7a4af27303c7c5267346a50d5911ef3e3a55003fa5cc3be434c4311406e03db3",
  "url": "https://rest.uniprot.org/uniprotkb/Q6M0N8.json"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6M0N8.json)

```json
{
  "evidence_id": "C16",
  "excerpt": "{\"citation\":{\"authors\":[\"Nair D.B.\",\"Jarrell K.F.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"25569238\"},{\"database\":\"DOI\",\"id\":\"10.3390/life5010085\"}],\"citationType\":\"journal article\",\"firstPage\":\"85\",\"id\":\"25569238\",\"journal\":\"Life\",\"lastPage\":\"101\",\"publicationDate\":\"2015\",\"title\":\"Pilin Processing Follows a Different Temporal Route than That of Archaellins in Methanococcus maripaludis.\",\"volume\":\"5\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"DSM 14266 / JCM 13030 / NBRC 101832 / S2 / LL\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION AS A PEPTIDASE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:31:42.105570+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7a4af27303c7c5267346a50d5911ef3e3a55003fa5cc3be434c4311406e03db3",
  "url": "https://rest.uniprot.org/uniprotkb/Q6M0N8.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6M0N8?format=txt&versions=82)

```json
{
  "entry_version": 82,
  "evidence_id": "H1",
  "excerpt": "ID   EPPA_METMP              Reviewed;         346 AA.\nAC   Q6M0N8;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-JUL-2004, sequence version 1.\nDT   28-JAN-2026, entry version 82.\nDE   RecName: Full=Prepilin peptidase EppA {ECO:0000303|PubMed:17114255};\nDE            EC=3.4.-.- {ECO:0000269|PubMed:17114255, ECO:0000269|PubMed:25569238};\nDE   AltName: Full=Euryarchaeal type IV prepilin peptidase {ECO:0000303|PubMed:17114255};\nGN   Name=eppA {ECO:0000303|PubMed:17114255};\nGN   OrderedLocusNames=MMP0232 {ECO:0000312|EMBL:CAF29788.1};\nOS   Methanococcus maripaludis (strain DSM 14266 / JCM 13030 / NBRC 101832 / S2\nOS   / LL).\nOC   Archaea; Methanobacteriati; Methanobacteriota; Methanomada group;\nOC   Methanococci; Methanococcales; Methanococcaceae; Methanococcus.\nOX   NCBI_TaxID=267377;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:46.039212+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "db360aef5d1ea6667df242a1cc2d0cea06cc60f4f37e16fbd6c154d182306232",
  "url": "https://rest.uniprot.org/unisave/Q6M0N8?format=txt&versions=82"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6M0N8?format=txt&versions=82)

```json
{
  "entry_version": 82,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION AS A PEPTIDASE.\nRC   STRAIN=DSM 14266 / JCM 13030 / NBRC 101832 / S2 / LL;\nRX   PubMed=17114255; DOI=10.1128/jb.01547-06;\nRA   Szabo Z., Stahl A.O., Albers S.V., Kissinger J.C., Driessen A.J.,\nRA   Pohlschroeder M.;\nRT   \"Identification of diverse archaeal proteins with class III signal peptides\nRT   cleaved by distinct archaeal prepilin peptidases.\";\nRL   J. Bacteriol. 189:772-778(2007).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:46.039212+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 29-37",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "db360aef5d1ea6667df242a1cc2d0cea06cc60f4f37e16fbd6c154d182306232",
  "url": "https://rest.uniprot.org/unisave/Q6M0N8?format=txt&versions=82"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6M0N8?format=txt&versions=82)

```json
{
  "entry_version": 82,
  "evidence_id": "H3",
  "excerpt": "RN   [3]\nRP   FUNCTION AS A PEPTIDASE.\nRC   STRAIN=DSM 14266 / JCM 13030 / NBRC 101832 / S2 / LL;\nRX   PubMed=25569238; DOI=10.3390/life5010085;\nRA   Nair D.B., Jarrell K.F.;\nRT   \"Pilin Processing Follows a Different Temporal Route than That of\nRT   Archaellins in Methanococcus maripaludis.\";\nRL   Life 5:85-101(2015).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:46.039212+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 38-45",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "db360aef5d1ea6667df242a1cc2d0cea06cc60f4f37e16fbd6c154d182306232",
  "url": "https://rest.uniprot.org/unisave/Q6M0N8?format=txt&versions=82"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6M0N8?format=txt&versions=82)

```json
{
  "entry_version": 82,
  "evidence_id": "H4",
  "excerpt": "FT   TRANSMEM        1..21\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:46.039212+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 87-89",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "db360aef5d1ea6667df242a1cc2d0cea06cc60f4f37e16fbd6c154d182306232",
  "url": "https://rest.uniprot.org/unisave/Q6M0N8?format=txt&versions=82"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6M0N8?format=txt&versions=82)

```json
{
  "entry_version": 82,
  "evidence_id": "H5",
  "excerpt": "FT   TRANSMEM        31..51\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:46.039212+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 90-92",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "db360aef5d1ea6667df242a1cc2d0cea06cc60f4f37e16fbd6c154d182306232",
  "url": "https://rest.uniprot.org/unisave/Q6M0N8?format=txt&versions=82"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6M0N8?format=txt&versions=82)

```json
{
  "entry_version": 82,
  "evidence_id": "H6",
  "excerpt": "FT   TRANSMEM        56..76\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:46.039212+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 93-95",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "db360aef5d1ea6667df242a1cc2d0cea06cc60f4f37e16fbd6c154d182306232",
  "url": "https://rest.uniprot.org/unisave/Q6M0N8?format=txt&versions=82"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6M0N8?format=txt&versions=82)

```json
{
  "entry_version": 82,
  "evidence_id": "H7",
  "excerpt": "FT   TRANSMEM        77..97\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:46.039212+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 96-98",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "db360aef5d1ea6667df242a1cc2d0cea06cc60f4f37e16fbd6c154d182306232",
  "url": "https://rest.uniprot.org/unisave/Q6M0N8?format=txt&versions=82"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6M0N8?format=txt&versions=82)

```json
{
  "entry_version": 82,
  "evidence_id": "H8",
  "excerpt": "FT   TRANSMEM        101..121\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:46.039212+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 99-101",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "db360aef5d1ea6667df242a1cc2d0cea06cc60f4f37e16fbd6c154d182306232",
  "url": "https://rest.uniprot.org/unisave/Q6M0N8?format=txt&versions=82"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6M0N8?format=txt&versions=82)

```json
{
  "entry_version": 82,
  "evidence_id": "H9",
  "excerpt": "FT   TRANSMEM        128..148\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:46.039212+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 102-104",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "db360aef5d1ea6667df242a1cc2d0cea06cc60f4f37e16fbd6c154d182306232",
  "url": "https://rest.uniprot.org/unisave/Q6M0N8?format=txt&versions=82"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6M0N8?format=txt&versions=82)

```json
{
  "entry_version": 82,
  "evidence_id": "H10",
  "excerpt": "FT   TRANSMEM        149..169\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:46.039212+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 105-107",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "db360aef5d1ea6667df242a1cc2d0cea06cc60f4f37e16fbd6c154d182306232",
  "url": "https://rest.uniprot.org/unisave/Q6M0N8?format=txt&versions=82"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6M0N8?format=txt&versions=82)

```json
{
  "entry_version": 82,
  "evidence_id": "H11",
  "excerpt": "FT   TRANSMEM        182..202\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:46.039212+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 108-110",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "db360aef5d1ea6667df242a1cc2d0cea06cc60f4f37e16fbd6c154d182306232",
  "url": "https://rest.uniprot.org/unisave/Q6M0N8?format=txt&versions=82"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6M0N8?format=txt&versions=82)

```json
{
  "entry_version": 82,
  "evidence_id": "H12",
  "excerpt": "FT   TRANSMEM        206..226\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:46.039212+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 111-113",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "db360aef5d1ea6667df242a1cc2d0cea06cc60f4f37e16fbd6c154d182306232",
  "url": "https://rest.uniprot.org/unisave/Q6M0N8?format=txt&versions=82"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6M0N8?format=txt&versions=82)

```json
{
  "entry_version": 82,
  "evidence_id": "H13",
  "excerpt": "FT   TRANSMEM        321..341\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:46.039212+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 114-116",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "db360aef5d1ea6667df242a1cc2d0cea06cc60f4f37e16fbd6c154d182306232",
  "url": "https://rest.uniprot.org/unisave/Q6M0N8?format=txt&versions=82"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 100. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
