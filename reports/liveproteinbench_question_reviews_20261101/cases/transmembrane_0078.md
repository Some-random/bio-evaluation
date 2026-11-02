# transmembrane_0078

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **D** — 3..23

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MDKISIIPIVGVALSLAIILQLGRTYWRLRHIPGPFPACITNFQRVGWVKTKRAHLILQDMHKKYGEVVRIGPNMVSFSNPEVIPTVYPARSGFPKGDFYVTLRPYTRGGGALHAVFNTTEEDLHKQIKSPIAPMFTPANTPSFEGLVDEVLTCIHEKLDENFIANSEIFNLGQWLQYFAFDVMGTMTFSKRYGFLDTGKDVGRMLGTIVDFMRDAAPMTQIPWLDWALRKNRIGDSIQRLFGKTASLGILGFVGKAIKERQELLSKGDFKVSDEKSGRKDFLTRFIELQQNDPKIPPWAPTAWTFSNVIAGSDSVGSLMRTTMFNLLVYPHTLEKLHDELRSAGVSRPYPKWSEIRNLLYLDACVQEGARMHPPFALPFERVVPAGGITILGYYLPGGTVVGGSPYVVNRHRETFGRDAEFWRPERWLESDEGHKRKLEQGVLTFGAGRRVCLGKHVGILEIKKLISFLVLNYDIRVVNPEKFELENSWFFFQRGLYATIRKRPDAVAVKNQQV

[Multiple Choices]
A. 3..23; 635..655
B. 5..27
C. 3..18
D. 3..23
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

> The sequence matches the cited UniProt entry, which annotates residues 3–23 as a helical transmembrane region. The annotation is computational (ECO:0000255), not presented here as experimental evidence.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The strong N-terminal hydrophobic stretch around residues 4–23 supports a membrane-spanning helix; the much later interval in A is outside this 515-residue protein, and C truncates the hydrophobic stretch.


**Missing item-specific fact**

> Choosing the exact annotated boundaries 3–23 rather than the overlapping 5–27 requires a boundary convention or protein-specific annotation not supplied in the question.


**Reason**

> Sequence hydropathy identifies the likely N-terminal transmembrane region, but its fuzzy boundaries do not robustly settle the close choice between D and B.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> Both intervals overlap the N-terminal hydrophobic helix; residues near the C-terminal boundary, including aromatic residues, can plausibly be included as membrane-interface or helix-boundary residues.


### Important caveats

- Reviewer-only evidence supports the key but was absent from the evaluated input.
- The supplied evidence supports a computational database annotation, not an independently verified experimental boundary.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The strong N-terminal hydrophobic stretch around residues 4–23 supports a membrane-spanning helix; the much later interval in A is outside this 515-residue protein, and C truncates the hydrophobic stretch.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Choosing the exact annotated boundaries 3–23 rather than the overlapping 5–27 requires a boundary convention or protein-specific annotation not supplied in the question.",
    "reason": "Sequence hydropathy identifies the likely N-terminal transmembrane region, but its fuzzy boundaries do not robustly settle the close choice between D and B."
  },
  "case_id": "transmembrane_0078",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the cited UniProt entry, which annotates residues 3–23 as a helical transmembrane region. The annotation is computational (ECO:0000255), not presented here as experimental evidence."
  },
  "important_caveats": [
    "Reviewer-only evidence supports the key but was absent from the evaluated input.",
    "The supplied evidence supports a computational database annotation, not an independently verified experimental boundary."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "Both intervals overlap the N-terminal hydrophobic helix; residues near the C-terminal boundary, including aromatic residues, can plausibly be included as membrane-interface or helix-boundary residues."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0078",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the cited UniProt entry, which annotates residues 3–23 as a helical transmembrane region. The annotation is computational (ECO:0000255), not presented here as experimental evidence.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The strong N-terminal hydrophobic stretch around residues 4–23 supports a membrane-spanning helix; the much later interval in A is outside this 515-residue protein, and C truncates the hydrophobic stretch.",
    "missing_item_specific_fact": "Choosing the exact annotated boundaries 3–23 rather than the overlapping 5–27 requires a boundary convention or protein-specific annotation not supplied in the question.",
    "reason": "Sequence hydropathy identifies the likely N-terminal transmembrane region, but its fuzzy boundaries do not robustly settle the close choice between D and B."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "Both intervals overlap the N-terminal hydrophobic helix; residues near the C-terminal boundary, including aromatic residues, can plausibly be included as membrane-interface or helix-boundary residues."
  },
  "important_caveats": [
    "Reviewer-only evidence supports the key but was absent from the evaluated input.",
    "The supplied evidence supports a computational database annotation, not an independently verified experimental boundary."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt annotation (evidence C5, H3) explicitly annotates a transmembrane helix at positions 3..23 with note 'Helical'. The sequence at positions 3-23 (KISIIPIVGVALSLAIILQLG) is predominantly hydrophobic, consistent with a TM helix. However, the evidence code is ECO:0000255 (inferred by similarity), meaning this is a computational annotation rather than experimental determination. The sequence match is confirmed (SHA256 identical).

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C1](#evidence-c1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Option A is eliminated because position 635..655 exceeds the 515-residue protein length. Option B (5..27) includes polar/aromatic residues R(24), T(25), Y(26), W(27) that disrupt the hydrophobic stretch, making it an implausible TM boundary. Between C (3..18, 16 residues) and D (3..23, 21 residues): a transmembrane alpha-helix requires approximately 20 residues (at ~1.5 Å/residue rise) to span the ~30 Å hydrophobic core of the lipid bilayer. The hydrophobic stretch KISIIPIVGVALSLAIILQLG extends through position 23, with the core hydrophobicity (I, V, A, L, S) persisting past position 18. Sixteen residues (option C) is too short for a complete TM helix, while 21 residues (option D) is within the typical 18-25 range.


**Missing item-specific fact**

> None critical. The exact endpoint (23 vs 20 or 22) involves some algorithmic boundary-determination judgment, but the broad biological reasoning (helix length requirement, hydrophobic stretch extent) meaningfully distinguishes D from C.


**Reason**

> A model can eliminate A (out of range) and B (polar residues at boundary) by simple sequence inspection, then use the well-established requirement that TM helices need ~20 residues to span the membrane to prefer D (21 residues) over C (16 residues). The hydrophobic character of positions 19-23 (I, L, Q, L, G) supports extension beyond 18.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C"
]
```

> Option C (3..18) represents a defensible but short TM prediction. The Q at position 21 is a polar residue that could argue for ending the helix earlier. However, the 16-residue length of C falls below the minimum needed to span the bilayer, and L(22)/G(23) are compatible with TM helix interiors, making D the stronger choice by biological reasoning.


### Important caveats

- The UniProt annotation uses ECO:0000255 (inferred by similarity), meaning the 3..23 boundary is a computational prediction, not an experimental measurement.
- The exact TM helix boundary (e.g., 20 vs 22 vs 23) is inherently algorithm-dependent; the question tests the correct annotation rather than an experimentally validated value.
- Option A's second range (635..655) is trivially impossible for a 515-residue protein, serving as a distractor.
- The annotation was first public in April 2025; the author's source snapshot is unknown but the sequence matches across all checked versions.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Option A is eliminated because position 635..655 exceeds the 515-residue protein length. Option B (5..27) includes polar/aromatic residues R(24), T(25), Y(26), W(27) that disrupt the hydrophobic stretch, making it an implausible TM boundary. Between C (3..18, 16 residues) and D (3..23, 21 residues): a transmembrane alpha-helix requires approximately 20 residues (at ~1.5 Å/residue rise) to span the ~30 Å hydrophobic core of the lipid bilayer. The hydrophobic stretch KISIIPIVGVALSLAIILQLG extends through position 23, with the core hydrophobicity (I, V, A, L, S) persisting past position 18. Sixteen residues (option C) is too short for a complete TM helix, while 21 residues (option D) is within the typical 18-25 range.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The exact endpoint (23 vs 20 or 22) involves some algorithmic boundary-determination judgment, but the broad biological reasoning (helix length requirement, hydrophobic stretch extent) meaningfully distinguishes D from C.",
    "reason": "A model can eliminate A (out of range) and B (polar residues at boundary) by simple sequence inspection, then use the well-established requirement that TM helices need ~20 residues to span the membrane to prefer D (21 residues) over C (16 residues). The hydrophobic character of positions 19-23 (I, L, Q, L, G) supports extension beyond 18."
  },
  "case_id": "transmembrane_0078",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C1"
    ],
    "judgment": "supported",
    "reason": "UniProt annotation (evidence C5, H3) explicitly annotates a transmembrane helix at positions 3..23 with note 'Helical'. The sequence at positions 3-23 (KISIIPIVGVALSLAIILQLG) is predominantly hydrophobic, consistent with a TM helix. However, the evidence code is ECO:0000255 (inferred by similarity), meaning this is a computational annotation rather than experimental determination. The sequence match is confirmed (SHA256 identical)."
  },
  "important_caveats": [
    "The UniProt annotation uses ECO:0000255 (inferred by similarity), meaning the 3..23 boundary is a computational prediction, not an experimental measurement.",
    "The exact TM helix boundary (e.g., 20 vs 22 vs 23) is inherently algorithm-dependent; the question tests the correct annotation rather than an experimentally validated value.",
    "Option A's second range (635..655) is trivially impossible for a 515-residue protein, serving as a distractor.",
    "The annotation was first public in April 2025; the author's source snapshot is unknown but the sequence matches across all checked versions."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C"
    ],
    "reason": "Option C (3..18) represents a defensible but short TM prediction. The Q at position 21 is a polar residue that could argue for ending the helix earlier. However, the 16-residue length of C falls below the minimum needed to span the bilayer, and L(22)/G(23) are compatible with TM helix interiors, making D the stronger choice by biological reasoning."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0078",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt annotation (evidence C5, H3) explicitly annotates a transmembrane helix at positions 3..23 with note 'Helical'. The sequence at positions 3-23 (KISIIPIVGVALSLAIILQLG) is predominantly hydrophobic, consistent with a TM helix. However, the evidence code is ECO:0000255 (inferred by similarity), meaning this is a computational annotation rather than experimental determination. The sequence match is confirmed (SHA256 identical).",
    "evidence_ids": ["C5", "H3", "C1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Option A is eliminated because position 635..655 exceeds the 515-residue protein length. Option B (5..27) includes polar/aromatic residues R(24), T(25), Y(26), W(27) that disrupt the hydrophobic stretch, making it an implausible TM boundary. Between C (3..18, 16 residues) and D (3..23, 21 residues): a transmembrane alpha-helix requires approximately 20 residues (at ~1.5 Å/residue rise) to span the ~30 Å hydrophobic core of the lipid bilayer. The hydrophobic stretch KISIIPIVGVALSLAIILQLG extends through position 23, with the core hydrophobicity (I, V, A, L, S) persisting past position 18. Sixteen residues (option C) is too short for a complete TM helix, while 21 residues (option D) is within the typical 18-25 range.",
    "missing_item_specific_fact": "None critical. The exact endpoint (23 vs 20 or 22) involves some algorithmic boundary-determination judgment, but the broad biological reasoning (helix length requirement, hydrophobic stretch extent) meaningfully distinguishes D from C.",
    "reason": "A model can eliminate A (out of range) and B (polar residues at boundary) by simple sequence inspection, then use the well-established requirement that TM helices need ~20 residues to span the membrane to prefer D (21 residues) over C (16 residues). The hydrophobic character of positions 19-23 (I, L, Q, L, G) supports extension beyond 18."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C"],
    "reason": "Option C (3..18) represents a defensible but short TM prediction. The Q at position 21 is a polar residue that could argue for ending the helix earlier. However, the 16-residue length of C falls below the minimum needed to span the bilayer, and L(22)/G(23) are compatible with TM helix interiors, making D the stronger choice by biological reasoning."
  },
  "important_caveats": [
    "The UniProt annotation uses ECO:0000255 (inferred by similarity), meaning the 3..23 boundary is a computational prediction, not an experimental measurement.",
    "The exact TM helix boundary (e.g., 20 vs 22 vs 23) is inherently algorithm-dependent; the question tests the correct annotation rather than an experimentally validated value.",
    "Option A's second range (635..655) is trivially impossible for a 515-residue protein, serving as a distractor.",
    "The annotation was first public in April 2025; the author's source snapshot is unknown but the sequence matches across all checked versions."
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

**Accession:** `P9WEG0` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 3. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG0.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:13.096452+00:00.  

```json
"P9WEG0"
```

Source SHA-256: `a6e6527f5d1306f7f6b07d9ae1a2faeb4bf00fa63555cc612e053eae8f17e600`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG0.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:13.096452+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":23},"start":{"modifier":"EXACT","value":3}},"type":"Transmembrane"}
```

Source SHA-256: `a6e6527f5d1306f7f6b07d9ae1a2faeb4bf00fa63555cc612e053eae8f17e600`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEG0?format=txt&versions=3)  
**Locator:** `lines 96-98`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-02T04:30:18.350529+00:00.  

```text
FT   TRANSMEM        3..23
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `3b311182ec72cd21034e97a0da2e7b1c6f9097ddf71e067e2d78b84e2753fac2`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 78. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
