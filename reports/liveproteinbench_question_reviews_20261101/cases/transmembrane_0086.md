# transmembrane_0086

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **D** — 306..326; 333..353; 355..375; 466..486

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MATTLTPTQRYAAGALLALALRQAQIHQSVLLGAHHHHDDDDEEQGRTSTSSGGGGGSSSSSSNSGAGADADLWTHDSHGLLRPVFRFLEIDPKAWSGLEETAASSEAKHHIGAFLRIIFEEDGESSSDRSVQELALAKGVDVMVMSLGNDSEVGNTIKGGDQDALPSSSGTDKSPGESSHDDQLGINKLTLDDIPANNHRKMALLFALLSACVADKPVSQEEEDRKSTRFRKGYDARHRVALRLLSTWLDVKWIKMEAIEVMVACSAMAAAKEQEQSQESASPKSKWEKWKRGGIIGAAALTGGALLAITGGLAAPAIAAGFGALAPTLGTLVPVIGASGFAAMATAAGSVAGSVAVAASFGAAGAGLTGSKMARRIGSVKEFEFKPIGENHNQGRLAVGILISGFAFDEDDFCRPWEGWQDNLERYILQWESKHIIAVSTAIQDWLTSRLAMELMKQGAMRTVLSGLLAAFAWPATLLAATDFIDSKWSVAIDRSDKAGKMLAEVLLKGLQGNRPVTLIGFSLGARVIFKCLQELALSSDNEGLVERVVLLGAPVSVKGERWEAARKMVAGRFVNVYSTDDWILGVTFRASLLTQGLAGIQAIDVPGVENVDVTELVDGHSSYLSAAQQILEHLELNTYYPVFVPLSAANEETDGTVAQ

[Multiple Choices]
A. 30..50; 62..82; 108..128; 144..164; 186..206; 327..347; 357..377
B. 306..326; 333..353; 466..486
C. 306..326; 333..353; 356..372; 466..486
D. 306..326; 333..353; 355..375; 466..486
```

<details>
<summary>Original system instructions, verbatim</summary>

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

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt annotation lists transmembrane regions 306..326, 333..353, 355..375, and 466..486, matching choice D. These are computationally supported annotations (ECO:0000255), not evidence here of experimental boundary measurements.

Citations as saved: [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Hydrophobic sequence stretches support the general inference that membrane-spanning helices occur in these regions, but they do not uniquely establish the precise annotated boundaries, especially for the highly hydrophobic region represented as 355..375 in D versus 356..372 in C.


**Missing item-specific fact**

> The protein-specific transmembrane feature annotations, including their exact start and end coordinates, are not supplied in the question.


**Reason**

> Choosing the exact listed coordinates depends on protein-specific boundary assignments absent from the input; sequence hydropathy can support a prediction but does not distinguish these near-nested boundaries reliably.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> Both choices include the same other listed regions, and the 356..372 segment in C is a hydrophobic subset of D's 355..375 region. The question does not specify that coordinates must match a particular annotation source or boundary convention.


### Important caveats

- The supporting UniProt evidence is computationally annotated and applies to the exact supplied sequence; it does not establish experimental validation of each boundary.
- The reviewer-only accession and database annotations were not supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Hydrophobic sequence stretches support the general inference that membrane-spanning helices occur in these regions, but they do not uniquely establish the precise annotated boundaries, especially for the highly hydrophobic region represented as 355..375 in D versus 356..372 in C.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific transmembrane feature annotations, including their exact start and end coordinates, are not supplied in the question.",
    "reason": "Choosing the exact listed coordinates depends on protein-specific boundary assignments absent from the input; sequence hydropathy can support a prediction but does not distinguish these near-nested boundaries reliably."
  },
  "case_id": "transmembrane_0086",
  "expected_answer_check": {
    "evidence_ids": [
      "H4",
      "H5",
      "H6",
      "H7",
      "C5",
      "C6",
      "C7",
      "C8"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation lists transmembrane regions 306..326, 333..353, 355..375, and 466..486, matching choice D. These are computationally supported annotations (ECO:0000255), not evidence here of experimental boundary measurements."
  },
  "important_caveats": [
    "The supporting UniProt evidence is computationally annotated and applies to the exact supplied sequence; it does not establish experimental validation of each boundary.",
    "The reviewer-only accession and database annotations were not supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "Both choices include the same other listed regions, and the 356..372 segment in C is a hydrophobic subset of D's 355..375 region. The question does not specify that coordinates must match a particular annotation source or boundary convention."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0086",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation lists transmembrane regions 306..326, 333..353, 355..375, and 466..486, matching choice D. These are computationally supported annotations (ECO:0000255), not evidence here of experimental boundary measurements.",
    "evidence_ids": ["H4", "H5", "H6", "H7", "C5", "C6", "C7", "C8"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Hydrophobic sequence stretches support the general inference that membrane-spanning helices occur in these regions, but they do not uniquely establish the precise annotated boundaries, especially for the highly hydrophobic region represented as 355..375 in D versus 356..372 in C.",
    "missing_item_specific_fact": "The protein-specific transmembrane feature annotations, including their exact start and end coordinates, are not supplied in the question.",
    "reason": "Choosing the exact listed coordinates depends on protein-specific boundary assignments absent from the input; sequence hydropathy can support a prediction but does not distinguish these near-nested boundaries reliably."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "Both choices include the same other listed regions, and the 356..372 segment in C is a hydrophobic subset of D's 355..375 region. The question does not specify that coordinates must match a particular annotation source or boundary convention."
  },
  "important_caveats": [
    "The supporting UniProt evidence is computationally annotated and applies to the exact supplied sequence; it does not establish experimental validation of each boundary.",
    "The reviewer-only accession and database annotations were not supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q10SS2 (STS1_ORYSJ, sequence matched by SHA-256) annotates exactly four transmembrane helical regions: 306-326, 333-353, 355-375, and 466-486, all with evidence code ECO:0000255 (inferred by similarity). This matches option D precisely. The annotation is computational (not experimentally determined), but it is the authoritative database annotation for this sequence.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The broad structure can be reasoned: the N-terminal ~290 residues are dominated by charged/polar residues (D, E, K, R, S, G, N, Q), making option A (7 TMs at positions 30-206) clearly implausible. The C-terminal region (~300-500) contains hydrophobic stretches consistent with multi-pass membrane topology, and a fourth hydrophobic segment near 466-486 is identifiable. This eliminates A and B. However, the critical C-vs-D distinction (third TM as 356-372 vs 355-375) involves only 1-3 residue boundary differences within a region that is itself only marginally hydrophobic (both segments contain multiple Ser, Gly, Thr, and even Lys at position 373).


**Missing item-specific fact**

> The exact boundary positions as output by the specific TM prediction algorithm (e.g., TMHMM, Phobius, or similar) used to generate the UniProt annotation. Distinguishing 355-375 from 356-372 requires knowing the precise algorithm parameters and scoring, not just general hydrophobicity reasoning. The region contains charged K(373) and multiple polar residues, making the exact start/end assignment algorithm-dependent.


**Reason**

> While the overall membrane topology (4 TMs in the C-terminal half, not 7 in the N-terminal half) is reasoning-accessible, the decisive C-vs-D discrimination hinges on 1-3 residue boundary precision that falls within the noise of any general hydrophobicity window analysis. The region is not a canonical strongly-hydrophobic TM helix; it is a borderline computational prediction. Selecting the exact boundaries requires knowledge of which prediction tool and parameters produced the annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> The third TM region in both C (356-372, 17 residues) and D (355-375, 21 residues) spans a segment with mixed hydrophobicity including Ser, Gly, Thr, and Lys. A 17-residue helix is at the short end of typical TM helices (usually 18-25), which mildly favors D's 21 residues, but this is not a decisive biological argument given the borderline nature of this particular segment. The 1-residue start difference (S355 vs V356) and 3-residue end difference (S372 vs A375) are within the typical ±2-3 residue uncertainty of TM boundary prediction.


### Important caveats

- All four TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions, not experimentally validated membrane insertions.
- The sequence identity is confirmed (SHA-256 match), so the annotation applies to the exact sequence provided.
- Option A (7 TMs in the N-terminal hydrophilic region) is clearly wrong and serves as an easy distractor.
- Option B (only 3 TMs, missing the 355-375 region) is distinguishable from C/D by recognizing the hydrophobic stretch around 355-375, though this stretch is itself borderline.
- The UniProt entry was first public on 2025-04-09; the author's source snapshot date is unknown but the sequence has been unchanged since 2006.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The broad structure can be reasoned: the N-terminal ~290 residues are dominated by charged/polar residues (D, E, K, R, S, G, N, Q), making option A (7 TMs at positions 30-206) clearly implausible. The C-terminal region (~300-500) contains hydrophobic stretches consistent with multi-pass membrane topology, and a fourth hydrophobic segment near 466-486 is identifiable. This eliminates A and B. However, the critical C-vs-D distinction (third TM as 356-372 vs 355-375) involves only 1-3 residue boundary differences within a region that is itself only marginally hydrophobic (both segments contain multiple Ser, Gly, Thr, and even Lys at position 373).",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact boundary positions as output by the specific TM prediction algorithm (e.g., TMHMM, Phobius, or similar) used to generate the UniProt annotation. Distinguishing 355-375 from 356-372 requires knowing the precise algorithm parameters and scoring, not just general hydrophobicity reasoning. The region contains charged K(373) and multiple polar residues, making the exact start/end assignment algorithm-dependent.",
    "reason": "While the overall membrane topology (4 TMs in the C-terminal half, not 7 in the N-terminal half) is reasoning-accessible, the decisive C-vs-D discrimination hinges on 1-3 residue boundary precision that falls within the noise of any general hydrophobicity window analysis. The region is not a canonical strongly-hydrophobic TM helix; it is a borderline computational prediction. Selecting the exact boundaries requires knowledge of which prediction tool and parameters produced the annotation."
  },
  "case_id": "transmembrane_0086",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "H4",
      "H5",
      "H6",
      "H7"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q10SS2 (STS1_ORYSJ, sequence matched by SHA-256) annotates exactly four transmembrane helical regions: 306-326, 333-353, 355-375, and 466-486, all with evidence code ECO:0000255 (inferred by similarity). This matches option D precisely. The annotation is computational (not experimentally determined), but it is the authoritative database annotation for this sequence."
  },
  "important_caveats": [
    "All four TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions, not experimentally validated membrane insertions.",
    "The sequence identity is confirmed (SHA-256 match), so the annotation applies to the exact sequence provided.",
    "Option A (7 TMs in the N-terminal hydrophilic region) is clearly wrong and serves as an easy distractor.",
    "Option B (only 3 TMs, missing the 355-375 region) is distinguishable from C/D by recognizing the hydrophobic stretch around 355-375, though this stretch is itself borderline.",
    "The UniProt entry was first public on 2025-04-09; the author's source snapshot date is unknown but the sequence has been unchanged since 2006."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "The third TM region in both C (356-372, 17 residues) and D (355-375, 21 residues) spans a segment with mixed hydrophobicity including Ser, Gly, Thr, and Lys. A 17-residue helix is at the short end of typical TM helices (usually 18-25), which mildly favors D's 21 residues, but this is not a decisive biological argument given the borderline nature of this particular segment. The 1-residue start difference (S355 vs V356) and 3-residue end difference (S372 vs A375) are within the typical ±2-3 residue uncertainty of TM boundary prediction."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0086",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q10SS2 (STS1_ORYSJ, sequence matched by SHA-256) annotates exactly four transmembrane helical regions: 306-326, 333-353, 355-375, and 466-486, all with evidence code ECO:0000255 (inferred by similarity). This matches option D precisely. The annotation is computational (not experimentally determined), but it is the authoritative database annotation for this sequence.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "H4", "H5", "H6", "H7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The broad structure can be reasoned: the N-terminal ~290 residues are dominated by charged/polar residues (D, E, K, R, S, G, N, Q), making option A (7 TMs at positions 30-206) clearly implausible. The C-terminal region (~300-500) contains hydrophobic stretches consistent with multi-pass membrane topology, and a fourth hydrophobic segment near 466-486 is identifiable. This eliminates A and B. However, the critical C-vs-D distinction (third TM as 356-372 vs 355-375) involves only 1-3 residue boundary differences within a region that is itself only marginally hydrophobic (both segments contain multiple Ser, Gly, Thr, and even Lys at position 373).",
    "missing_item_specific_fact": "The exact boundary positions as output by the specific TM prediction algorithm (e.g., TMHMM, Phobius, or similar) used to generate the UniProt annotation. Distinguishing 355-375 from 356-372 requires knowing the precise algorithm parameters and scoring, not just general hydrophobicity reasoning. The region contains charged K(373) and multiple polar residues, making the exact start/end assignment algorithm-dependent.",
    "reason": "While the overall membrane topology (4 TMs in the C-terminal half, not 7 in the N-terminal half) is reasoning-accessible, the decisive C-vs-D discrimination hinges on 1-3 residue boundary precision that falls within the noise of any general hydrophobicity window analysis. The region is not a canonical strongly-hydrophobic TM helix; it is a borderline computational prediction. Selecting the exact boundaries requires knowledge of which prediction tool and parameters produced the annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "The third TM region in both C (356-372, 17 residues) and D (355-375, 21 residues) spans a segment with mixed hydrophobicity including Ser, Gly, Thr, and Lys. A 17-residue helix is at the short end of typical TM helices (usually 18-25), which mildly favors D's 21 residues, but this is not a decisive biological argument given the borderline nature of this particular segment. The 1-residue start difference (S355 vs V356) and 3-residue end difference (S372 vs A375) are within the typical ±2-3 residue uncertainty of TM boundary prediction."
  },
  "important_caveats": [
    "All four TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions, not experimentally validated membrane insertions.",
    "The sequence identity is confirmed (SHA-256 match), so the annotation applies to the exact sequence provided.",
    "Option A (7 TMs in the N-terminal hydrophilic region) is clearly wrong and serves as an easy distractor.",
    "Option B (only 3 TMs, missing the 355-375 region) is distinguishable from C/D by recognizing the hydrophobic stretch around 355-375, though this stretch is itself borderline.",
    "The UniProt entry was first public on 2025-04-09; the author's source snapshot date is unknown but the sequence has been unchanged since 2006."
  ]
}
```

</details>

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `Q10SS2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 121. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q10SS2.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:29.234158+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":326},"start":{"modifier":"EXACT","value":306}},"type":"Transmembrane"}
```

Source SHA-256: `0a6a8d6a3c909a1dbd7c765a1a1d325767f551df7a3b5795f41c6d5c449c4e27`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q10SS2.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:29.234158+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":353},"start":{"modifier":"EXACT","value":333}},"type":"Transmembrane"}
```

Source SHA-256: `0a6a8d6a3c909a1dbd7c765a1a1d325767f551df7a3b5795f41c6d5c449c4e27`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q10SS2.json)  
**Locator:** `/features/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:29.234158+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":375},"start":{"modifier":"EXACT","value":355}},"type":"Transmembrane"}
```

Source SHA-256: `0a6a8d6a3c909a1dbd7c765a1a1d325767f551df7a3b5795f41c6d5c449c4e27`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q10SS2.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:29.234158+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":486},"start":{"modifier":"EXACT","value":466}},"type":"Transmembrane"}
```

Source SHA-256: `0a6a8d6a3c909a1dbd7c765a1a1d325767f551df7a3b5795f41c6d5c449c4e27`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q10SS2?format=txt&versions=121)  
**Locator:** `lines 178-180`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 121 / 1.  
**Retrieved:** 2026-11-02T04:30:34.944114+00:00.  

```text
FT   TRANSMEM        306..326
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `acc4e547beb155cdd1e60fb276d5cc6296693b0794b6f3a69d9c2d66a4f46eda`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q10SS2?format=txt&versions=121)  
**Locator:** `lines 181-183`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 121 / 1.  
**Retrieved:** 2026-11-02T04:30:34.944114+00:00.  

```text
FT   TRANSMEM        333..353
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `acc4e547beb155cdd1e60fb276d5cc6296693b0794b6f3a69d9c2d66a4f46eda`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q10SS2?format=txt&versions=121)  
**Locator:** `lines 184-186`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 121 / 1.  
**Retrieved:** 2026-11-02T04:30:34.944114+00:00.  

```text
FT   TRANSMEM        355..375
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `acc4e547beb155cdd1e60fb276d5cc6296693b0794b6f3a69d9c2d66a4f46eda`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q10SS2?format=txt&versions=121)  
**Locator:** `lines 187-189`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 121 / 1.  
**Retrieved:** 2026-11-02T04:30:34.944114+00:00.  

```text
FT   TRANSMEM        466..486
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `acc4e547beb155cdd1e60fb276d5cc6296693b0794b6f3a69d9c2d66a4f46eda`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 86. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
