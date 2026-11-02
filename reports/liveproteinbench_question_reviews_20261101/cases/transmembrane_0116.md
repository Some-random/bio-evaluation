# transmembrane_0116

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **C** — 26..46

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MLGELIFLLRSLHGFLASSGPIGAALAWLISFKPILFAFLLLLLLLSNWLVKQEHNLAPSPPQEEAETTTAPEVHPKNNVKNKEELEKINACFALQDKVLERLMFSEMKLKALENQVFVIWNKINRRRWSSRQRNFSRRRHRSRRHDSTFSTLSKCTTVTPTECD

[Multiple Choices]
A. 26..46; 764..789
B. 31..42
C. 26..46
D. 9..29; 2201..2221; 2238..2258; 2267..2287; 2296..2316; 2352..2372; 2386..2406
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

> The supplied sequence exactly matches the UniProt record, which annotates residues 26–46 as a helical transmembrane region. The annotation is computationally supported (ECO:0000255), not presented as experimental evidence.

Citations as saved: [C5](#evidence-c5), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a long, predominantly hydrophobic N-terminal region, consistent with a membrane-spanning helix. Of the in-range choices, 26–46 has a plausible span length; 31–42 is only a short subset, while the other choices include coordinates beyond this 165-residue sequence.


**Missing item-specific fact**

> The precise annotated boundaries 26 and 46 are protein-specific; sequence hydropathy alone does not establish those exact endpoints with certainty.


**Reason**

> The sequence and options provide a meaningful basis for selecting the plausible full-length membrane-spanning segment, even though the exact boundaries are not uniquely proven by general reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only choice C gives a plausible complete region within the sequence. B is a shorter subset, and A and D include out-of-range coordinates.


### Important caveats

- The supporting annotation is computational and does not establish experimental confirmation.
- The exact source snapshot used by the author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a long, predominantly hydrophobic N-terminal region, consistent with a membrane-spanning helix. Of the in-range choices, 26–46 has a plausible span length; 31–42 is only a short subset, while the other choices include coordinates beyond this 165-residue sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The precise annotated boundaries 26 and 46 are protein-specific; sequence hydropathy alone does not establish those exact endpoints with certainty.",
    "reason": "The sequence and options provide a meaningful basis for selecting the plausible full-length membrane-spanning segment, even though the exact boundaries are not uniquely proven by general reasoning."
  },
  "case_id": "transmembrane_0116",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt record, which annotates residues 26–46 as a helical transmembrane region. The annotation is computationally supported (ECO:0000255), not presented as experimental evidence."
  },
  "important_caveats": [
    "The supporting annotation is computational and does not establish experimental confirmation.",
    "The exact source snapshot used by the author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only choice C gives a plausible complete region within the sequence. B is a shorter subset, and A and D include out-of-range coordinates."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0116",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt record, which annotates residues 26–46 as a helical transmembrane region. The annotation is computationally supported (ECO:0000255), not presented as experimental evidence.",
    "evidence_ids": ["C5", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a long, predominantly hydrophobic N-terminal region, consistent with a membrane-spanning helix. Of the in-range choices, 26–46 has a plausible span length; 31–42 is only a short subset, while the other choices include coordinates beyond this 165-residue sequence.",
    "missing_item_specific_fact": "The precise annotated boundaries 26 and 46 are protein-specific; sequence hydropathy alone does not establish those exact endpoints with certainty.",
    "reason": "The sequence and options provide a meaningful basis for selecting the plausible full-length membrane-spanning segment, even though the exact boundaries are not uniquely proven by general reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only choice C gives a plausible complete region within the sequence. B is a shorter subset, and A and D include out-of-range coordinates."
  },
  "important_caveats": [
    "The supporting annotation is computational and does not establish experimental confirmation.",
    "The exact source snapshot used by the author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q9CPU3 (TEX46_MOUSE, 165 AA) annotates a transmembrane helical region at positions 26..46 (evidence C5, H2). The sequence at positions 26-46 (AALAWLISFKPILFAFLLLLLL) is predominantly hydrophobic and 21 residues long, consistent with a single-pass TM helix. The evidence code ECO:0000255 indicates computational/curator inference rather than experimental determination, but the annotation is present and the sequence context supports it.

Citations as saved: [C5](#evidence-c5), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein is only 165 residues long, so options A (references position 764) and D (references positions 2201-2406) are immediately eliminated as impossible. Between B (31-42, 12 residues) and C (26-46, 21 residues), the well-established biological constraint that a transmembrane alpha-helix requires approximately 20 residues to span the ~30 Å hydrophobic core of the lipid bilayer eliminates B as too short. The hydrophobic stretch in the N-terminal region of the sequence (positions ~26-46, rich in A, L, W, I, F) with a length of 21 residues is the only option satisfying both the hydrophobicity and length criteria for a TM helix.


**Missing item-specific fact**

> None critical. The exact boundary residues (why 26 vs 25, why 46 vs 47) could benefit from the annotation, but the provided options make the distinction resolvable by the ~20-residue TM helix length rule.


**Reason**

> Eliminating A and D requires only checking sequence length (165 AA). Distinguishing B from C requires the general biological knowledge that TM helices need ~20 residues, which is standard textbook knowledge. The hydrophobic character of the 26-46 stretch is visible from the sequence itself. No protein-specific experimental measurement or obscure annotation is needed.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and D are definitively eliminated by the 165-residue sequence length. Option B (12 residues) is too short for a TM helix by general biological principles. Only C satisfies both the hydrophobicity and length requirements. No ambiguity remains among the choices.


### Important caveats

- The UniProt annotation uses evidence code ECO:0000255 (inferred by sequence analysis/computational), not experimental determination. The TM assignment is a prediction, not an experimentally validated topology.
- The protein is annotated as a 'Precursor' (C4), so the mature form could differ, but this does not affect the TM region prediction within the given 165-residue sequence.
- The region 26-46 contains a few non-ideal TM residues (S32, K34, P35), but the overall hydrophobic character and length are consistent with a TM helix as annotated.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein is only 165 residues long, so options A (references position 764) and D (references positions 2201-2406) are immediately eliminated as impossible. Between B (31-42, 12 residues) and C (26-46, 21 residues), the well-established biological constraint that a transmembrane alpha-helix requires approximately 20 residues to span the ~30 Å hydrophobic core of the lipid bilayer eliminates B as too short. The hydrophobic stretch in the N-terminal region of the sequence (positions ~26-46, rich in A, L, W, I, F) with a length of 21 residues is the only option satisfying both the hydrophobicity and length criteria for a TM helix.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The exact boundary residues (why 26 vs 25, why 46 vs 47) could benefit from the annotation, but the provided options make the distinction resolvable by the ~20-residue TM helix length rule.",
    "reason": "Eliminating A and D requires only checking sequence length (165 AA). Distinguishing B from C requires the general biological knowledge that TM helices need ~20 residues, which is standard textbook knowledge. The hydrophobic character of the 26-46 stretch is visible from the sequence itself. No protein-specific experimental measurement or obscure annotation is needed."
  },
  "case_id": "transmembrane_0116",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H2"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q9CPU3 (TEX46_MOUSE, 165 AA) annotates a transmembrane helical region at positions 26..46 (evidence C5, H2). The sequence at positions 26-46 (AALAWLISFKPILFAFLLLLLL) is predominantly hydrophobic and 21 residues long, consistent with a single-pass TM helix. The evidence code ECO:0000255 indicates computational/curator inference rather than experimental determination, but the annotation is present and the sequence context supports it."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (inferred by sequence analysis/computational), not experimental determination. The TM assignment is a prediction, not an experimentally validated topology.",
    "The protein is annotated as a 'Precursor' (C4), so the mature form could differ, but this does not affect the TM region prediction within the given 165-residue sequence.",
    "The region 26-46 contains a few non-ideal TM residues (S32, K34, P35), but the overall hydrophobic character and length are consistent with a TM helix as annotated."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and D are definitively eliminated by the 165-residue sequence length. Option B (12 residues) is too short for a TM helix by general biological principles. Only C satisfies both the hydrophobicity and length requirements. No ambiguity remains among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0116",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q9CPU3 (TEX46_MOUSE, 165 AA) annotates a transmembrane helical region at positions 26..46 (evidence C5, H2). The sequence at positions 26-46 (AALAWLISFKPILFAFLLLLLL) is predominantly hydrophobic and 21 residues long, consistent with a single-pass TM helix. The evidence code ECO:0000255 indicates computational/curator inference rather than experimental determination, but the annotation is present and the sequence context supports it.",
    "evidence_ids": ["C5", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein is only 165 residues long, so options A (references position 764) and D (references positions 2201-2406) are immediately eliminated as impossible. Between B (31-42, 12 residues) and C (26-46, 21 residues), the well-established biological constraint that a transmembrane alpha-helix requires approximately 20 residues to span the ~30 Å hydrophobic core of the lipid bilayer eliminates B as too short. The hydrophobic stretch in the N-terminal region of the sequence (positions ~26-46, rich in A, L, W, I, F) with a length of 21 residues is the only option satisfying both the hydrophobicity and length criteria for a TM helix.",
    "missing_item_specific_fact": "None critical. The exact boundary residues (why 26 vs 25, why 46 vs 47) could benefit from the annotation, but the provided options make the distinction resolvable by the ~20-residue TM helix length rule.",
    "reason": "Eliminating A and D requires only checking sequence length (165 AA). Distinguishing B from C requires the general biological knowledge that TM helices need ~20 residues, which is standard textbook knowledge. The hydrophobic character of the 26-46 stretch is visible from the sequence itself. No protein-specific experimental measurement or obscure annotation is needed."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and D are definitively eliminated by the 165-residue sequence length. Option B (12 residues) is too short for a TM helix by general biological principles. Only C satisfies both the hydrophobicity and length requirements. No ambiguity remains among the choices."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (inferred by sequence analysis/computational), not experimental determination. The TM assignment is a prediction, not an experimentally validated topology.",
    "The protein is annotated as a 'Precursor' (C4), so the mature form could differ, but this does not affect the TM region prediction within the given 165-residue sequence.",
    "The region 26-46 contains a few non-ideal TM residues (S32, K34, P35), but the overall hydrophobic character and length are consistent with a TM helix as annotated."
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

**Accession:** `Q9CPU3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 138. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9CPU3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:41.992470+00:00.  

```json
{"flag":"Precursor","recommendedName":{"fullName":{"value":"Testis expressed 46"}}}
```

Source SHA-256: `99cc363802abde6fdab0470811cc356e245be073343a2e13f8809aa18306cf3a`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9CPU3.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:41.992470+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":46},"start":{"modifier":"EXACT","value":26}},"type":"Transmembrane"}
```

Source SHA-256: `99cc363802abde6fdab0470811cc356e245be073343a2e13f8809aa18306cf3a`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9CPU3?format=txt&versions=138)  
**Locator:** `lines 139-141`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 138 / 1.  
**Retrieved:** 2026-11-02T04:32:46.624739+00:00.  

```text
FT   TRANSMEM        26..46
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `d1133d1c732f294e96a2ddbd82458e2e88c2a4f72fc869dbdba86c1d279c012d`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 116. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
