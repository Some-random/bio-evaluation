# transmembrane_0067

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **A** — 27..47; 82..102; 109..129; 136..156; 173..193; 209..229; 333..353; 361..381; 395..415; 427..447; 460..480

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MDTAPDHREPQEQGESRKWYEMTASEFYVYVVAFMCGVSMMMPVNAVFSAPAYIMTYYRYAMQDPEAVPLYTNFWNNVMTYYNLIGIVTSLIMEPLTLLSWFRRIPMKVRLLGGLVILIVEIIVLMVVPARGTSEAGAVATICCTGFIGGFGKSIFESTTYGMFGAFPSSFTSTMMGGVGMSGVLTSLLQIIVKAALPDSYEGVKKQSKIYYGLDVGIQGMTFVALILLRFNSFAQNYFGDLGAVKSKVDAGKLSAEALCHTDEHPTHDKEGRNSSSGKEVPALGEVQTAAAKSEGPDAVEESSWPHEVEGPTSNEILVATAIFSTLRRVKWMFVACAFNFLITLFLFPGIAVGMFPDSKWFSTIAVFIFNVFDVLGRFSPSLKLMWPRSYKQRWIIVAASFARVIFVPLLLLHSYHYIPGEAYGYVMEVIFGFSNGYVGSMALVLGPQSKGIDNDGKRFVAGTLMGISILVGGTIGTVLSIMTQTIRATY

[Multiple Choices]
A. 27..47; 82..102; 109..129; 136..156; 173..193; 209..229; 333..353; 361..381; 395..415; 427..447; 460..480
B. 70..90; 96..116
C. 27..47; 82..102; 104..127; 136..156; 173..193; 209..229; 333..353; 361..381; 395..415; 427..447; 460..480
D. 27..47; 82..102; 109..129; 136..156; 173..193; 209..229; 361..381; 395..415; 427..447; 460..480
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

> The sequence matches the UniProt entry, whose transmembrane annotations correspond to all eleven intervals in A. The annotations carry computational evidence code ECO:0000255, so this supports the key as a database annotation, not as independently verified experimental boundaries.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [C13](#evidence-c13), [C14](#evidence-c14), [C15](#evidence-c15), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11), [H12](#evidence-h12), [H13](#evidence-h13), [H14](#evidence-h14).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has multiple strongly hydrophobic stretches of roughly membrane-helix length, including the region around 333–353, which supports a multi-pass membrane protein and argues against B and D. C adds a 104–127 interval that substantially overlaps its listed 109–129 helix; A instead represents the adjacent hydrophobic regions as separate spans.


**Missing item-specific fact**

> The exact annotated residue boundaries are not supplied; the database's specific boundary calls would be needed to reproduce those coordinates exactly.


**Reason**

> Despite uncertainty in precise boundaries from sequence alone, the hydrophobic pattern and the implausible omissions or overlap in the alternatives provide meaningful grounds to distinguish A.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> A is the best-supported option among those listed; the alternatives either omit evident hydrophobic spans or include a substantially overlapping extra interval.


### Important caveats

- The reviewer-only database annotation is computationally supported, not shown here to be experimentally established.
- The sequence matches both current and archived database records, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has multiple strongly hydrophobic stretches of roughly membrane-helix length, including the region around 333–353, which supports a multi-pass membrane protein and argues against B and D. C adds a 104–127 interval that substantially overlaps its listed 109–129 helix; A instead represents the adjacent hydrophobic regions as separate spans.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact annotated residue boundaries are not supplied; the database's specific boundary calls would be needed to reproduce those coordinates exactly.",
    "reason": "Despite uncertainty in precise boundaries from sequence alone, the hydrophobic pattern and the implausible omissions or overlap in the alternatives provide meaningful grounds to distinguish A."
  },
  "case_id": "transmembrane_0067",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
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
    "reason": "The sequence matches the UniProt entry, whose transmembrane annotations correspond to all eleven intervals in A. The annotations carry computational evidence code ECO:0000255, so this supports the key as a database annotation, not as independently verified experimental boundaries."
  },
  "important_caveats": [
    "The reviewer-only database annotation is computationally supported, not shown here to be experimentally established.",
    "The sequence matches both current and archived database records, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A is the best-supported option among those listed; the alternatives either omit evident hydrophobic spans or include a substantially overlapping extra interval."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0067",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry, whose transmembrane annotations correspond to all eleven intervals in A. The annotations carry computational evidence code ECO:0000255, so this supports the key as a database annotation, not as independently verified experimental boundaries.",
    "evidence_ids": ["C1", "C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "C14", "C15", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "H11", "H12", "H13", "H14"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has multiple strongly hydrophobic stretches of roughly membrane-helix length, including the region around 333–353, which supports a multi-pass membrane protein and argues against B and D. C adds a 104–127 interval that substantially overlaps its listed 109–129 helix; A instead represents the adjacent hydrophobic regions as separate spans.",
    "missing_item_specific_fact": "The exact annotated residue boundaries are not supplied; the database's specific boundary calls would be needed to reproduce those coordinates exactly.",
    "reason": "Despite uncertainty in precise boundaries from sequence alone, the hydrophobic pattern and the implausible omissions or overlap in the alternatives provide meaningful grounds to distinguish A."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A is the best-supported option among those listed; the alternatives either omit evident hydrophobic spans or include a substantially overlapping extra interval."
  },
  "important_caveats": [
    "The reviewer-only database annotation is computationally supported, not shown here to be experimentally established.",
    "The sequence matches both current and archived database records, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for O76343 (LdNT1.1, nucleoside transporter 1.1 from Leishmania donovani) lists exactly 11 transmembrane helices at positions 27..47, 82..102, 109..129, 136..156, 173..193, 209..229, 333..353, 361..381, 395..415, 427..447, 460..480, matching Choice A exactly. However, all annotations carry evidence code ECO:0000255 (by similarity), indicating computational prediction transferred from homologous proteins rather than experimental determination. The ENT (equilibrative nucleoside transporter) family is known to have 11 TM helices, consistent with this annotation.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [C13](#evidence-c13), [C14](#evidence-c14), [C15](#evidence-c15), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11), [H12](#evidence-h12), [H13](#evidence-h13), [H14](#evidence-h14).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One can reason that ENT-family nucleoside transporters have 11 TM helices, eliminating Choice B (only 2 TMs) and Choice D (only 10 TMs, missing 333..353). A hydrophobicity scan of the sequence could plausibly identify the 333..353 region as a TM helix, distinguishing A from D.


**Missing item-specific fact**

> The precise boundary of the third TM helix (109..129 in A vs 104..127 in C) cannot be reliably distinguished by general biological reasoning. A 21-residue vs 24-residue helix are both plausible TM lengths, and the 5-residue shift at the start and 2-residue shift at the end fall within the typical error margin of hydrophobicity-based TM prediction. Selecting the exact annotation boundary requires knowledge of the specific UniProt entry or running a particular prediction tool (e.g., Phobius, TMHMM) configured to produce those exact coordinates.


**Reason**

> While the 11-TM topology of ENT transporters is general knowledge that eliminates B and D, the critical distinction between A and C hinges on exact residue boundaries of one helix that are within prediction uncertainty. No general biological principle (helix length constraints, flanking residue preferences, etc.) cleanly resolves 109..129 over 104..127 without the specific annotation or a particular algorithm's output.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> The only difference between A and C is the third TM helix boundary (109..129 vs 104..127). Both represent plausible 21-24 residue hydrophobic helices. Without running a specific TM prediction algorithm or consulting the UniProt annotation, a careful sequence analysis could reasonably favor either boundary. The question asks for exact start/end positions, making this a precision-dependent choice that goes beyond general hydrophobicity reasoning.


### Important caveats

- All 11 TM annotations carry ECO:0000255 (by similarity), meaning they are computational predictions transferred from homologous proteins, not experimentally validated boundaries.
- The sequence-to-accession mapping (O76343) was inferred from reviewer-only metadata and was not provided to the evaluated model.
- The difference between A and C (5 residues at start, 2 at end of one helix) is within the typical ±5 residue uncertainty of TM prediction tools, making this a borderline distinction.
- The protein is 491 residues; the annotation was retrieved from both current (v72) and historical (v70) UniProt snapshots with matched sequences.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One can reason that ENT-family nucleoside transporters have 11 TM helices, eliminating Choice B (only 2 TMs) and Choice D (only 10 TMs, missing 333..353). A hydrophobicity scan of the sequence could plausibly identify the 333..353 region as a TM helix, distinguishing A from D.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The precise boundary of the third TM helix (109..129 in A vs 104..127 in C) cannot be reliably distinguished by general biological reasoning. A 21-residue vs 24-residue helix are both plausible TM lengths, and the 5-residue shift at the start and 2-residue shift at the end fall within the typical error margin of hydrophobicity-based TM prediction. Selecting the exact annotation boundary requires knowledge of the specific UniProt entry or running a particular prediction tool (e.g., Phobius, TMHMM) configured to produce those exact coordinates.",
    "reason": "While the 11-TM topology of ENT transporters is general knowledge that eliminates B and D, the critical distinction between A and C hinges on exact residue boundaries of one helix that are within prediction uncertainty. No general biological principle (helix length constraints, flanking residue preferences, etc.) cleanly resolves 109..129 over 104..127 without the specific annotation or a particular algorithm's output."
  },
  "case_id": "transmembrane_0067",
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
    "reason": "The UniProt annotation for O76343 (LdNT1.1, nucleoside transporter 1.1 from Leishmania donovani) lists exactly 11 transmembrane helices at positions 27..47, 82..102, 109..129, 136..156, 173..193, 209..229, 333..353, 361..381, 395..415, 427..447, 460..480, matching Choice A exactly. However, all annotations carry evidence code ECO:0000255 (by similarity), indicating computational prediction transferred from homologous proteins rather than experimental determination. The ENT (equilibrative nucleoside transporter) family is known to have 11 TM helices, consistent with this annotation."
  },
  "important_caveats": [
    "All 11 TM annotations carry ECO:0000255 (by similarity), meaning they are computational predictions transferred from homologous proteins, not experimentally validated boundaries.",
    "The sequence-to-accession mapping (O76343) was inferred from reviewer-only metadata and was not provided to the evaluated model.",
    "The difference between A and C (5 residues at start, 2 at end of one helix) is within the typical ±5 residue uncertainty of TM prediction tools, making this a borderline distinction.",
    "The protein is 491 residues; the annotation was retrieved from both current (v72) and historical (v70) UniProt snapshots with matched sequences."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "The only difference between A and C is the third TM helix boundary (109..129 vs 104..127). Both represent plausible 21-24 residue hydrophobic helices. Without running a specific TM prediction algorithm or consulting the UniProt annotation, a careful sequence analysis could reasonably favor either boundary. The question asks for exact start/end positions, making this a precision-dependent choice that goes beyond general hydrophobicity reasoning."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{"case_id":"transmembrane_0067","expected_answer_check":{"judgment":"supported","reason":"The UniProt annotation for O76343 (LdNT1.1, nucleoside transporter 1.1 from Leishmania donovani) lists exactly 11 transmembrane helices at positions 27..47, 82..102, 109..129, 136..156, 173..193, 209..229, 333..353, 361..381, 395..415, 427..447, 460..480, matching Choice A exactly. However, all annotations carry evidence code ECO:0000255 (by similarity), indicating computational prediction transferred from homologous proteins rather than experimental determination. The ENT (equilibrative nucleoside transporter) family is known to have 11 TM helices, consistent with this annotation.","evidence_ids":["C5","C6","C7","C8","C9","C10","C11","C12","C13","C14","C15","H4","H5","H6","H7","H8","H9","H10","H11","H12","H13","H14"]},"answerability_check":{"judgment":"lookup_or_memorization_dependent","discriminating_biological_argument":"One can reason that ENT-family nucleoside transporters have 11 TM helices, eliminating Choice B (only 2 TMs) and Choice D (only 10 TMs, missing 333..353). A hydrophobicity scan of the sequence could plausibly identify the 333..353 region as a TM helix, distinguishing A from D.","missing_item_specific_fact":"The precise boundary of the third TM helix (109..129 in A vs 104..127 in C) cannot be reliably distinguished by general biological reasoning. A 21-residue vs 24-residue helix are both plausible TM lengths, and the 5-residue shift at the start and 2-residue shift at the end fall within the typical error margin of hydrophobicity-based TM prediction. Selecting the exact annotation boundary requires knowledge of the specific UniProt entry or running a particular prediction tool (e.g., Phobius, TMHMM) configured to produce those exact coordinates.","reason":"While the 11-TM topology of ENT transporters is general knowledge that eliminates B and D, the critical distinction between A and C hinges on exact residue boundaries of one helix that are within prediction uncertainty. No general biological principle (helix length constraints, flanking residue preferences, etc.) cleanly resolves 109..129 over 104..127 without the specific annotation or a particular algorithm's output."},"question_ambiguity":{"multiple_defensible_options":["A","C"],"reason":"The only difference between A and C is the third TM helix boundary (109..129 vs 104..127). Both represent plausible 21-24 residue hydrophobic helices. Without running a specific TM prediction algorithm or consulting the UniProt annotation, a careful sequence analysis could reasonably favor either boundary. The question asks for exact start/end positions, making this a precision-dependent choice that goes beyond general hydrophobicity reasoning."},"important_caveats":["All 11 TM annotations carry ECO:0000255 (by similarity), meaning they are computational predictions transferred from homologous proteins, not experimentally validated boundaries.","The sequence-to-accession mapping (O76343) was inferred from reviewer-only metadata and was not provided to the evaluated model.","The difference between A and C (5 residues at start, 2 at end of one helix) is within the typical ±5 residue uncertainty of TM prediction tools, making this a borderline distinction.","The protein is 491 residues; the annotation was retrieved from both current (v72) and historical (v70) UniProt snapshots with matched sequences."]}
```

</details>

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `O76343` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 70. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76343.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:17.225994+00:00.  

```json
"O76343"
```

Source SHA-256: `97673b3b239eb17dcd7f09142ac967ab287203ab9d3569bb07bb1272089bf8f5`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76343.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:17.225994+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":47},"start":{"modifier":"EXACT","value":27}},"type":"Transmembrane"}
```

Source SHA-256: `97673b3b239eb17dcd7f09142ac967ab287203ab9d3569bb07bb1272089bf8f5`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76343.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:17.225994+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":102},"start":{"modifier":"EXACT","value":82}},"type":"Transmembrane"}
```

Source SHA-256: `97673b3b239eb17dcd7f09142ac967ab287203ab9d3569bb07bb1272089bf8f5`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76343.json)  
**Locator:** `/features/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:17.225994+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":129},"start":{"modifier":"EXACT","value":109}},"type":"Transmembrane"}
```

Source SHA-256: `97673b3b239eb17dcd7f09142ac967ab287203ab9d3569bb07bb1272089bf8f5`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76343.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:17.225994+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":156},"start":{"modifier":"EXACT","value":136}},"type":"Transmembrane"}
```

Source SHA-256: `97673b3b239eb17dcd7f09142ac967ab287203ab9d3569bb07bb1272089bf8f5`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76343.json)  
**Locator:** `/features/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:17.225994+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":193},"start":{"modifier":"EXACT","value":173}},"type":"Transmembrane"}
```

Source SHA-256: `97673b3b239eb17dcd7f09142ac967ab287203ab9d3569bb07bb1272089bf8f5`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76343.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:17.225994+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":229},"start":{"modifier":"EXACT","value":209}},"type":"Transmembrane"}
```

Source SHA-256: `97673b3b239eb17dcd7f09142ac967ab287203ab9d3569bb07bb1272089bf8f5`.

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76343.json)  
**Locator:** `/features/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:17.225994+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":353},"start":{"modifier":"EXACT","value":333}},"type":"Transmembrane"}
```

Source SHA-256: `97673b3b239eb17dcd7f09142ac967ab287203ab9d3569bb07bb1272089bf8f5`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76343.json)  
**Locator:** `/features/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:17.225994+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":381},"start":{"modifier":"EXACT","value":361}},"type":"Transmembrane"}
```

Source SHA-256: `97673b3b239eb17dcd7f09142ac967ab287203ab9d3569bb07bb1272089bf8f5`.

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76343.json)  
**Locator:** `/features/9`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:17.225994+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":415},"start":{"modifier":"EXACT","value":395}},"type":"Transmembrane"}
```

Source SHA-256: `97673b3b239eb17dcd7f09142ac967ab287203ab9d3569bb07bb1272089bf8f5`.

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76343.json)  
**Locator:** `/features/10`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:17.225994+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":447},"start":{"modifier":"EXACT","value":427}},"type":"Transmembrane"}
```

Source SHA-256: `97673b3b239eb17dcd7f09142ac967ab287203ab9d3569bb07bb1272089bf8f5`.

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76343.json)  
**Locator:** `/features/11`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:17.225994+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":480},"start":{"modifier":"EXACT","value":460}},"type":"Transmembrane"}
```

Source SHA-256: `97673b3b239eb17dcd7f09142ac967ab287203ab9d3569bb07bb1272089bf8f5`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76343?format=txt&versions=70)  
**Locator:** `lines 114-116`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 70 / 1.  
**Retrieved:** 2026-11-02T04:29:19.110797+00:00.  

```text
FT   TRANSMEM        27..47
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `dc801be211759dda113a5721795889a659944693db48804af91b6fcc1dd93c4c`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76343?format=txt&versions=70)  
**Locator:** `lines 117-119`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 70 / 1.  
**Retrieved:** 2026-11-02T04:29:19.110797+00:00.  

```text
FT   TRANSMEM        82..102
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `dc801be211759dda113a5721795889a659944693db48804af91b6fcc1dd93c4c`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76343?format=txt&versions=70)  
**Locator:** `lines 120-122`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 70 / 1.  
**Retrieved:** 2026-11-02T04:29:19.110797+00:00.  

```text
FT   TRANSMEM        109..129
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `dc801be211759dda113a5721795889a659944693db48804af91b6fcc1dd93c4c`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76343?format=txt&versions=70)  
**Locator:** `lines 123-125`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 70 / 1.  
**Retrieved:** 2026-11-02T04:29:19.110797+00:00.  

```text
FT   TRANSMEM        136..156
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `dc801be211759dda113a5721795889a659944693db48804af91b6fcc1dd93c4c`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76343?format=txt&versions=70)  
**Locator:** `lines 126-128`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 70 / 1.  
**Retrieved:** 2026-11-02T04:29:19.110797+00:00.  

```text
FT   TRANSMEM        173..193
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `dc801be211759dda113a5721795889a659944693db48804af91b6fcc1dd93c4c`.

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76343?format=txt&versions=70)  
**Locator:** `lines 129-131`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 70 / 1.  
**Retrieved:** 2026-11-02T04:29:19.110797+00:00.  

```text
FT   TRANSMEM        209..229
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `dc801be211759dda113a5721795889a659944693db48804af91b6fcc1dd93c4c`.

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76343?format=txt&versions=70)  
**Locator:** `lines 132-134`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 70 / 1.  
**Retrieved:** 2026-11-02T04:29:19.110797+00:00.  

```text
FT   TRANSMEM        333..353
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `dc801be211759dda113a5721795889a659944693db48804af91b6fcc1dd93c4c`.

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76343?format=txt&versions=70)  
**Locator:** `lines 135-137`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 70 / 1.  
**Retrieved:** 2026-11-02T04:29:19.110797+00:00.  

```text
FT   TRANSMEM        361..381
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `dc801be211759dda113a5721795889a659944693db48804af91b6fcc1dd93c4c`.

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76343?format=txt&versions=70)  
**Locator:** `lines 138-140`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 70 / 1.  
**Retrieved:** 2026-11-02T04:29:19.110797+00:00.  

```text
FT   TRANSMEM        395..415
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `dc801be211759dda113a5721795889a659944693db48804af91b6fcc1dd93c4c`.

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76343?format=txt&versions=70)  
**Locator:** `lines 141-143`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 70 / 1.  
**Retrieved:** 2026-11-02T04:29:19.110797+00:00.  

```text
FT   TRANSMEM        427..447
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `dc801be211759dda113a5721795889a659944693db48804af91b6fcc1dd93c4c`.

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76343?format=txt&versions=70)  
**Locator:** `lines 144-146`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 70 / 1.  
**Retrieved:** 2026-11-02T04:29:19.110797+00:00.  

```text
FT   TRANSMEM        460..480
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `dc801be211759dda113a5721795889a659944693db48804af91b6fcc1dd93c4c`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 67. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
