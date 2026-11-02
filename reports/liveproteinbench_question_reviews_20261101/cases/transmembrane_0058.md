# transmembrane_0058

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **D** — 100..120; 135..155; 182..202; 228..248; 263..283; 293..313; 329..349

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSGFVAGEEAVKSALSAATWIGAASPKYSHLVLSRVFNIYSEYIYANGFKLTRENLIEDFGTRPEDVDPFMKIFGGPNGIATYLTALPGLLPILPHPRNIPIIVPLFCVFTVMTSLAVGLRLWSRQKVAGGIRSFDWLALAGFGLTIIYGAVSVYHSKVSGPYQAFYDRTWDQMKENYKVYLVLTIMYPFIMGLIKISLLLFYYRVATLNYVQWAVYATGSLTIANSIAAIITHCLAFMPIDFWNHFLQSPFKFNSRTPMLVFGAVYILTDVAILIIPMPMVFQLKLYPREKVIAVIAFSLGGVACVASGFRIWAIDEFQNYSGKNSSGLMIDAWTMIELNLTLICASAPAIRALAIHYAPKILSTLPSAFSSSGATRGSKSAGSSGKSKTPESEKSMQVSQSPVIPKEVV

[Multiple Choices]
A. 5..25; 46..66; 74..94; 179..199; 239..259; 264..284; 296..316
B. 100..120; 135..155; 182..202; 263..283; 293..313; 329..349
C. 100..120; 135..155; 179..207; 228..248; 263..283; 293..313; 329..349
D. 100..120; 135..155; 182..202; 228..248; 263..283; 293..313; 329..349
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

> The exact sequence matches the UniProt record, whose seven annotated transmembrane helices correspond to choice D. The annotations are computationally evidenced (ECO:0000255), not presented here as experimental measurements.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has the repeated hydrophobic stretches expected of a seven-pass membrane protein. Their hydropathy and flanking more polar regions support the seven spans in D; the longer 179..207 range in C includes residues outside the strongest hydrophobic segment, and B omits a further plausible membrane span.


**Missing item-specific fact**

> The exact canonical residue boundaries are not supplied and cannot be known with certainty from general principles alone, but sequence hydropathy gives meaningful grounds to prefer D among these choices.


**Reason**

> This is a sequence-based prediction task, and the candidate intervals can be compared with the protein’s hydrophobic segments. The reviewer-only annotation corroborates the choice but is not needed as input to that biological argument.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> D is the best-supported complete set of spans; the alternatives either omit a plausible span or extend a candidate span into less hydrophobic flanking residues.


### Important caveats

- The supporting UniProt transmembrane features carry computational evidence codes, so they should not be described as experimentally established boundaries.
- The source sequence matches exactly, but the author's precise source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has the repeated hydrophobic stretches expected of a seven-pass membrane protein. Their hydropathy and flanking more polar regions support the seven spans in D; the longer 179..207 range in C includes residues outside the strongest hydrophobic segment, and B omits a further plausible membrane span.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact canonical residue boundaries are not supplied and cannot be known with certainty from general principles alone, but sequence hydropathy gives meaningful grounds to prefer D among these choices.",
    "reason": "This is a sequence-based prediction task, and the candidate intervals can be compared with the protein’s hydrophobic segments. The reviewer-only annotation corroborates the choice but is not needed as input to that biological argument."
  },
  "case_id": "transmembrane_0058",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C8",
      "C10",
      "C12",
      "C14",
      "C16",
      "C18"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt record, whose seven annotated transmembrane helices correspond to choice D. The annotations are computationally evidenced (ECO:0000255), not presented here as experimental measurements."
  },
  "important_caveats": [
    "The supporting UniProt transmembrane features carry computational evidence codes, so they should not be described as experimentally established boundaries.",
    "The source sequence matches exactly, but the author's precise source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is the best-supported complete set of spans; the alternatives either omit a plausible span or extend a candidate span into less hydrophobic flanking residues."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0058",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt record, whose seven annotated transmembrane helices correspond to choice D. The annotations are computationally evidenced (ECO:0000255), not presented here as experimental measurements.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has the repeated hydrophobic stretches expected of a seven-pass membrane protein. Their hydropathy and flanking more polar regions support the seven spans in D; the longer 179..207 range in C includes residues outside the strongest hydrophobic segment, and B omits a further plausible membrane span.",
    "missing_item_specific_fact": "The exact canonical residue boundaries are not supplied and cannot be known with certainty from general principles alone, but sequence hydropathy gives meaningful grounds to prefer D among these choices.",
    "reason": "This is a sequence-based prediction task, and the candidate intervals can be compared with the protein’s hydrophobic segments. The reviewer-only annotation corroborates the choice but is not needed as input to that biological argument."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is the best-supported complete set of spans; the alternatives either omit a plausible span or extend a candidate span into less hydrophobic flanking residues."
  },
  "important_caveats": [
    "The supporting UniProt transmembrane features carry computational evidence codes, so they should not be described as experimentally established boundaries.",
    "The source sequence matches exactly, but the author's precise source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (G1X9H9, entry version 34, sequence matched) lists exactly seven transmembrane helical regions at 100-120, 135-155, 182-202, 228-248, 263-283, 293-313, and 329-349, which matches option D precisely. The evidence code ECO:0000255 indicates these are computationally inferred by similarity (consistent with GPCR homology), not experimentally measured, but the annotation is internally consistent with the topological domain assignments (extracellular N-terminus 1-99, alternating cytoplasmic/extracellular loops). The protein is annotated as Receptor GIN3, a 7-TM GPCR, consistent with seven helical segments.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C5](#evidence-c5), [C7](#evidence-c7), [C9](#evidence-c9), [C11](#evidence-c11), [C13](#evidence-c13), [C15](#evidence-c15), [C17](#evidence-c17), [C19](#evidence-c19), [H4](#evidence-h4), [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Multiple reasoning steps distinguish the options: (1) The protein is a GPCR (7-TM receptor), so exactly 7 transmembrane helices are expected, eliminating option B which lists only 6. (2) The N-terminal ~100 residues contain charged/polar residues (e.g., positions 5-25 'VAGEEAVKSALSAATWIGAAS' contain E, E, K; positions 46-66 contain K, R, E, D, E), making them incompatible with membrane-spanning helices, eliminating option A which places three TMs in this region. (3) Between C and D, the key difference is TM3: option C gives 179-207 (29 residues) while D gives 182-202 (21 residues). GPCR transmembrane helices are typically 20-25 residues; a 29-residue helix is atypical. Additionally, the residues at 179-181 and 203-207 fall in the extracellular and cytoplasmic loops respectively (per topological domain logic), and a hydrophobicity scan of the sequence shows the contiguous hydrophobic core aligns better with 182-202 than the extended 179-207.


**Missing item-specific fact**

> The exact boundary residues (182 vs 179, 202 vs 207) are set by the UniProt similarity-based annotation (ECO:0000255). A model performing a slightly different hydrophobicity window analysis could plausibly extend the helix by 1-3 residues on either side. However, the options are fixed and the biological argument about typical GPCR helix length provides a defensible basis to prefer D over C.


**Reason**

> The elimination of A (non-hydrophobic N-terminal residues) and B (only 6 TMs for a GPCR) is straightforward from sequence and general knowledge. The C-vs-D distinction relies on typical GPCR TM helix length (~20-25 aa) and hydrophobicity boundaries, which is a valid biological reasoning argument, though the precision of the exact cut points is annotation-dependent.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C"
]
```

> Option C differs from D only in TM3 boundaries (179-207 vs 182-202). A model using a hydrophobicity window slightly wider than 21 residues could argue for C. The 29-residue helix in C is unusual for GPCRs but not impossible (some GPCR TMs extend into loops). However, the typical-length argument and the loop-residue character of positions 179-181/203-207 favor D, making C a less defensible but not absurd alternative.


### Important caveats

- All UniProt TM annotations carry ECO:0000255 (similarity), meaning they are computational predictions based on GPCR homology, not experimental measurements (e.g., crystallography or cryo-EM).
- The sequence is 411 AA and matches the UniProt entry exactly; numbering is canonical.
- The entry was first public in April 2025; the author's source snapshot date is unknown, but the sequence version (1) has not changed since 2011, so the annotation boundaries are unlikely to have shifted.
- Option A is clearly wrong (non-hydrophobic segments in the extracellular N-terminus); option B is clearly wrong (6 TMs for a 7-TM GPCR). The substantive discrimination is C vs D.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Multiple reasoning steps distinguish the options: (1) The protein is a GPCR (7-TM receptor), so exactly 7 transmembrane helices are expected, eliminating option B which lists only 6. (2) The N-terminal ~100 residues contain charged/polar residues (e.g., positions 5-25 'VAGEEAVKSALSAATWIGAAS' contain E, E, K; positions 46-66 contain K, R, E, D, E), making them incompatible with membrane-spanning helices, eliminating option A which places three TMs in this region. (3) Between C and D, the key difference is TM3: option C gives 179-207 (29 residues) while D gives 182-202 (21 residues). GPCR transmembrane helices are typically 20-25 residues; a 29-residue helix is atypical. Additionally, the residues at 179-181 and 203-207 fall in the extracellular and cytoplasmic loops respectively (per topological domain logic), and a hydrophobicity scan of the sequence shows the contiguous hydrophobic core aligns better with 182-202 than the extended 179-207.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact boundary residues (182 vs 179, 202 vs 207) are set by the UniProt similarity-based annotation (ECO:0000255). A model performing a slightly different hydrophobicity window analysis could plausibly extend the helix by 1-3 residues on either side. However, the options are fixed and the biological argument about typical GPCR helix length provides a defensible basis to prefer D over C.",
    "reason": "The elimination of A (non-hydrophobic N-terminal residues) and B (only 6 TMs for a GPCR) is straightforward from sequence and general knowledge. The C-vs-D distinction relies on typical GPCR TM helix length (~20-25 aa) and hydrophobicity boundaries, which is a valid biological reasoning argument, though the precision of the exact cut points is annotation-dependent."
  },
  "case_id": "transmembrane_0058",
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
      "C19",
      "H4",
      "H6",
      "H8",
      "H10",
      "H12",
      "H14",
      "H16"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (G1X9H9, entry version 34, sequence matched) lists exactly seven transmembrane helical regions at 100-120, 135-155, 182-202, 228-248, 263-283, 293-313, and 329-349, which matches option D precisely. The evidence code ECO:0000255 indicates these are computationally inferred by similarity (consistent with GPCR homology), not experimentally measured, but the annotation is internally consistent with the topological domain assignments (extracellular N-terminus 1-99, alternating cytoplasmic/extracellular loops). The protein is annotated as Receptor GIN3, a 7-TM GPCR, consistent with seven helical segments."
  },
  "important_caveats": [
    "All UniProt TM annotations carry ECO:0000255 (similarity), meaning they are computational predictions based on GPCR homology, not experimental measurements (e.g., crystallography or cryo-EM).",
    "The sequence is 411 AA and matches the UniProt entry exactly; numbering is canonical.",
    "The entry was first public in April 2025; the author's source snapshot date is unknown, but the sequence version (1) has not changed since 2011, so the annotation boundaries are unlikely to have shifted.",
    "Option A is clearly wrong (non-hydrophobic segments in the extracellular N-terminus); option B is clearly wrong (6 TMs for a 7-TM GPCR). The substantive discrimination is C vs D."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C"
    ],
    "reason": "Option C differs from D only in TM3 boundaries (179-207 vs 182-202). A model using a hydrophobicity window slightly wider than 21 residues could argue for C. The 29-residue helix in C is unusual for GPCRs but not impossible (some GPCR TMs extend into loops). However, the typical-length argument and the loop-residue character of positions 179-181/203-207 favor D, making C a less defensible but not absurd alternative."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{"case_id":"transmembrane_0058","expected_answer_check":{"judgment":"supported","reason":"The UniProt annotation (G1X9H9, entry version 34, sequence matched) lists exactly seven transmembrane helical regions at 100-120, 135-155, 182-202, 228-248, 263-283, 293-313, and 329-349, which matches option D precisely. The evidence code ECO:0000255 indicates these are computationally inferred by similarity (consistent with GPCR homology), not experimentally measured, but the annotation is internally consistent with the topological domain assignments (extracellular N-terminus 1-99, alternating cytoplasmic/extracellular loops). The protein is annotated as Receptor GIN3, a 7-TM GPCR, consistent with seven helical segments.","evidence_ids":["C6","C8","C10","C12","C14","C16","C18","C5","C7","C9","C11","C13","C15","C17","C19","H4","H6","H8","H10","H12","H14","H16"]},"answerability_check":{"judgment":"reasoning_supported","discriminating_biological_argument":"Multiple reasoning steps distinguish the options: (1) The protein is a GPCR (7-TM receptor), so exactly 7 transmembrane helices are expected, eliminating option B which lists only 6. (2) The N-terminal ~100 residues contain charged/polar residues (e.g., positions 5-25 'VAGEEAVKSALSAATWIGAAS' contain E, E, K; positions 46-66 contain K, R, E, D, E), making them incompatible with membrane-spanning helices, eliminating option A which places three TMs in this region. (3) Between C and D, the key difference is TM3: option C gives 179-207 (29 residues) while D gives 182-202 (21 residues). GPCR transmembrane helices are typically 20-25 residues; a 29-residue helix is atypical. Additionally, the residues at 179-181 and 203-207 fall in the extracellular and cytoplasmic loops respectively (per topological domain logic), and a hydrophobicity scan of the sequence shows the contiguous hydrophobic core aligns better with 182-202 than the extended 179-207.","missing_item_specific_fact":"The exact boundary residues (182 vs 179, 202 vs 207) are set by the UniProt similarity-based annotation (ECO:0000255). A model performing a slightly different hydrophobicity window analysis could plausibly extend the helix by 1-3 residues on either side. However, the options are fixed and the biological argument about typical GPCR helix length provides a defensible basis to prefer D over C.","reason":"The elimination of A (non-hydrophobic N-terminal residues) and B (only 6 TMs for a GPCR) is straightforward from sequence and general knowledge. The C-vs-D distinction relies on typical GPCR TM helix length (~20-25 aa) and hydrophobicity boundaries, which is a valid biological reasoning argument, though the precision of the exact cut points is annotation-dependent."},"question_ambiguity":{"multiple_defensible_options":["C"],"reason":"Option C differs from D only in TM3 boundaries (179-207 vs 182-202). A model using a hydrophobicity window slightly wider than 21 residues could argue for C. The 29-residue helix in C is unusual for GPCRs but not impossible (some GPCR TMs extend into loops). However, the typical-length argument and the loop-residue character of positions 179-181/203-207 favor D, making C a less defensible but not absurd alternative."},"important_caveats":["All UniProt TM annotations carry ECO:0000255 (similarity), meaning they are computational predictions based on GPCR homology, not experimental measurements (e.g., crystallography or cryo-EM).","The sequence is 411 AA and matches the UniProt entry exactly; numbering is canonical.","The entry was first public in April 2025; the author's source snapshot date is unknown, but the sequence version (1) has not changed since 2011, so the annotation boundaries are unlikely to have shifted.","Option A is clearly wrong (non-hydrophobic segments in the extracellular N-terminus); option B is clearly wrong (6 TMs for a 7-TM GPCR). The substantive discrimination is C vs D."]}
```

</details>

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `G1X9H9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 34. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9H9.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:32.260197+00:00.  

```json
{"description":"Extracellular","evidences":[{"evidenceCode":"ECO:0000305"}],"location":{"end":{"modifier":"EXACT","value":99},"start":{"modifier":"EXACT","value":1}},"type":"Topological domain"}
```

Source SHA-256: `94b96505af2850513697c650eceb67c2c454b1c96127f985a05f0bd52970b66a`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9H9.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:32.260197+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":120},"start":{"modifier":"EXACT","value":100}},"type":"Transmembrane"}
```

Source SHA-256: `94b96505af2850513697c650eceb67c2c454b1c96127f985a05f0bd52970b66a`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9H9.json)  
**Locator:** `/features/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:32.260197+00:00.  

```json
{"description":"Cytoplasmic","evidences":[{"evidenceCode":"ECO:0000305"}],"location":{"end":{"modifier":"EXACT","value":134},"start":{"modifier":"EXACT","value":121}},"type":"Topological domain"}
```

Source SHA-256: `94b96505af2850513697c650eceb67c2c454b1c96127f985a05f0bd52970b66a`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9H9.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:32.260197+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":155},"start":{"modifier":"EXACT","value":135}},"type":"Transmembrane"}
```

Source SHA-256: `94b96505af2850513697c650eceb67c2c454b1c96127f985a05f0bd52970b66a`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9H9.json)  
**Locator:** `/features/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:32.260197+00:00.  

```json
{"description":"Extracellular","evidences":[{"evidenceCode":"ECO:0000305"}],"location":{"end":{"modifier":"EXACT","value":181},"start":{"modifier":"EXACT","value":156}},"type":"Topological domain"}
```

Source SHA-256: `94b96505af2850513697c650eceb67c2c454b1c96127f985a05f0bd52970b66a`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9H9.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:32.260197+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":202},"start":{"modifier":"EXACT","value":182}},"type":"Transmembrane"}
```

Source SHA-256: `94b96505af2850513697c650eceb67c2c454b1c96127f985a05f0bd52970b66a`.

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9H9.json)  
**Locator:** `/features/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:32.260197+00:00.  

```json
{"description":"Cytoplasmic","evidences":[{"evidenceCode":"ECO:0000305"}],"location":{"end":{"modifier":"EXACT","value":227},"start":{"modifier":"EXACT","value":203}},"type":"Topological domain"}
```

Source SHA-256: `94b96505af2850513697c650eceb67c2c454b1c96127f985a05f0bd52970b66a`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9H9.json)  
**Locator:** `/features/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:32.260197+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":248},"start":{"modifier":"EXACT","value":228}},"type":"Transmembrane"}
```

Source SHA-256: `94b96505af2850513697c650eceb67c2c454b1c96127f985a05f0bd52970b66a`.

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9H9.json)  
**Locator:** `/features/9`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:32.260197+00:00.  

```json
{"description":"Extracellular","evidences":[{"evidenceCode":"ECO:0000305"}],"location":{"end":{"modifier":"EXACT","value":262},"start":{"modifier":"EXACT","value":249}},"type":"Topological domain"}
```

Source SHA-256: `94b96505af2850513697c650eceb67c2c454b1c96127f985a05f0bd52970b66a`.

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9H9.json)  
**Locator:** `/features/10`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:32.260197+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":283},"start":{"modifier":"EXACT","value":263}},"type":"Transmembrane"}
```

Source SHA-256: `94b96505af2850513697c650eceb67c2c454b1c96127f985a05f0bd52970b66a`.

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9H9.json)  
**Locator:** `/features/11`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:32.260197+00:00.  

```json
{"description":"Cytoplasmic","evidences":[{"evidenceCode":"ECO:0000305"}],"location":{"end":{"modifier":"EXACT","value":292},"start":{"modifier":"EXACT","value":284}},"type":"Topological domain"}
```

Source SHA-256: `94b96505af2850513697c650eceb67c2c454b1c96127f985a05f0bd52970b66a`.

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9H9.json)  
**Locator:** `/features/12`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:32.260197+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":313},"start":{"modifier":"EXACT","value":293}},"type":"Transmembrane"}
```

Source SHA-256: `94b96505af2850513697c650eceb67c2c454b1c96127f985a05f0bd52970b66a`.

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9H9.json)  
**Locator:** `/features/13`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:32.260197+00:00.  

```json
{"description":"Extracellular","evidences":[{"evidenceCode":"ECO:0000305"}],"location":{"end":{"modifier":"EXACT","value":328},"start":{"modifier":"EXACT","value":314}},"type":"Topological domain"}
```

Source SHA-256: `94b96505af2850513697c650eceb67c2c454b1c96127f985a05f0bd52970b66a`.

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9H9.json)  
**Locator:** `/features/14`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:32.260197+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":349},"start":{"modifier":"EXACT","value":329}},"type":"Transmembrane"}
```

Source SHA-256: `94b96505af2850513697c650eceb67c2c454b1c96127f985a05f0bd52970b66a`.

### Evidence C19

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9H9.json)  
**Locator:** `/features/15`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:32.260197+00:00.  

```json
{"description":"Cytoplasmic","evidences":[{"evidenceCode":"ECO:0000305"}],"location":{"end":{"modifier":"EXACT","value":411},"start":{"modifier":"EXACT","value":350}},"type":"Topological domain"}
```

Source SHA-256: `94b96505af2850513697c650eceb67c2c454b1c96127f985a05f0bd52970b66a`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9H9?format=txt&versions=34)  
**Locator:** `lines 82-84`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 34 / 1.  
**Retrieved:** 2026-11-02T04:28:34.047987+00:00.  

```text
FT   TRANSMEM        100..120
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `4373765a04c53d8ca0885d8905393dedb927e54af65644fad7cdc7e4abd3a154`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9H9?format=txt&versions=34)  
**Locator:** `lines 88-90`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 34 / 1.  
**Retrieved:** 2026-11-02T04:28:34.047987+00:00.  

```text
FT   TRANSMEM        135..155
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `4373765a04c53d8ca0885d8905393dedb927e54af65644fad7cdc7e4abd3a154`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9H9?format=txt&versions=34)  
**Locator:** `lines 94-96`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 34 / 1.  
**Retrieved:** 2026-11-02T04:28:34.047987+00:00.  

```text
FT   TRANSMEM        182..202
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `4373765a04c53d8ca0885d8905393dedb927e54af65644fad7cdc7e4abd3a154`.

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9H9?format=txt&versions=34)  
**Locator:** `lines 100-102`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 34 / 1.  
**Retrieved:** 2026-11-02T04:28:34.047987+00:00.  

```text
FT   TRANSMEM        228..248
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `4373765a04c53d8ca0885d8905393dedb927e54af65644fad7cdc7e4abd3a154`.

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9H9?format=txt&versions=34)  
**Locator:** `lines 106-108`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 34 / 1.  
**Retrieved:** 2026-11-02T04:28:34.047987+00:00.  

```text
FT   TRANSMEM        263..283
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `4373765a04c53d8ca0885d8905393dedb927e54af65644fad7cdc7e4abd3a154`.

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9H9?format=txt&versions=34)  
**Locator:** `lines 112-114`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 34 / 1.  
**Retrieved:** 2026-11-02T04:28:34.047987+00:00.  

```text
FT   TRANSMEM        293..313
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `4373765a04c53d8ca0885d8905393dedb927e54af65644fad7cdc7e4abd3a154`.

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9H9?format=txt&versions=34)  
**Locator:** `lines 118-120`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 34 / 1.  
**Retrieved:** 2026-11-02T04:28:34.047987+00:00.  

```text
FT   TRANSMEM        329..349
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `4373765a04c53d8ca0885d8905393dedb927e54af65644fad7cdc7e4abd3a154`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 58. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
