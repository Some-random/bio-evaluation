# transmembrane_0049

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **B** — 35..55; 68..88; 99..119; 139..159

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MADFPGKVSTQTSSQEPQRSFAISSSVDMGFIKSIPGILLIAEIVVGLLVWTLIASTPHYLIPALGWVLFVSITLWLLSIALLVILLLSLHQRLPSVPWPLVLLVFYSVAALLYLTAFLANAATVPGGYYQGHLGASAFFGIVETLLYTASSYFAYLGWRGEGQNAAGSTVPV

[Multiple Choices]
A. 35..55; 99..119; 139..159
B. 35..55; 68..88; 99..119; 139..159
C. 35..55
D. 35..55; 63..83; 99..119; 139..159
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

> The sequence exactly matches the historical UniProt record, which annotates transmembrane helices at 35–55, 68–88, 99–119, and 139–159—the intervals in B. The helix annotations carry computational evidence code ECO:0000255, so this supports the key as a database annotation, not as independently established experimental evidence.

Citations as saved: [H3](#evidence-h3), [H5](#evidence-h5), [H7](#evidence-h7), [H9](#evidence-h9).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains long hydrophobic stretches consistent with multiple membrane-spanning helices, including a particularly hydrophobic region around residues 63–88. That supports identifying the general region, but does not reliably establish its exact annotated boundaries.


**Missing item-specific fact**

> The protein-specific annotation locating the second helix at 68–88 rather than the also-hydrophobic 63–83 interval is not supplied in the question.


**Reason**

> The sequence permits broad transmembrane-region inference, but the choices test exact boundaries within a continuous hydrophobic stretch. General sequence reasoning does not clearly distinguish B from D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> Both choices include the same strongly hydrophobic second region but give different boundaries. The sequence alone does not unambiguously determine those precise endpoints.


### Important caveats

- Reviewer-only database evidence was not available to the evaluated model.
- The cited transmembrane annotations are computational; the supplied evidence does not independently verify the boundaries experimentally.
- The source record sequence matches the input, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains long hydrophobic stretches consistent with multiple membrane-spanning helices, including a particularly hydrophobic region around residues 63–88. That supports identifying the general region, but does not reliably establish its exact annotated boundaries.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific annotation locating the second helix at 68–88 rather than the also-hydrophobic 63–83 interval is not supplied in the question.",
    "reason": "The sequence permits broad transmembrane-region inference, but the choices test exact boundaries within a continuous hydrophobic stretch. General sequence reasoning does not clearly distinguish B from D."
  },
  "case_id": "transmembrane_0049",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H5",
      "H7",
      "H9"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches the historical UniProt record, which annotates transmembrane helices at 35–55, 68–88, 99–119, and 139–159—the intervals in B. The helix annotations carry computational evidence code ECO:0000255, so this supports the key as a database annotation, not as independently established experimental evidence."
  },
  "important_caveats": [
    "Reviewer-only database evidence was not available to the evaluated model.",
    "The cited transmembrane annotations are computational; the supplied evidence does not independently verify the boundaries experimentally.",
    "The source record sequence matches the input, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "Both choices include the same strongly hydrophobic second region but give different boundaries. The sequence alone does not unambiguously determine those precise endpoints."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0049",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches the historical UniProt record, which annotates transmembrane helices at 35–55, 68–88, 99–119, and 139–159—the intervals in B. The helix annotations carry computational evidence code ECO:0000255, so this supports the key as a database annotation, not as independently established experimental evidence.",
    "evidence_ids": ["H3", "H5", "H7", "H9"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains long hydrophobic stretches consistent with multiple membrane-spanning helices, including a particularly hydrophobic region around residues 63–88. That supports identifying the general region, but does not reliably establish its exact annotated boundaries.",
    "missing_item_specific_fact": "The protein-specific annotation locating the second helix at 68–88 rather than the also-hydrophobic 63–83 interval is not supplied in the question.",
    "reason": "The sequence permits broad transmembrane-region inference, but the choices test exact boundaries within a continuous hydrophobic stretch. General sequence reasoning does not clearly distinguish B from D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "Both choices include the same strongly hydrophobic second region but give different boundaries. The sequence alone does not unambiguously determine those precise endpoints."
  },
  "important_caveats": [
    "Reviewer-only database evidence was not available to the evaluated model.",
    "The cited transmembrane annotations are computational; the supplied evidence does not independently verify the boundaries experimentally.",
    "The source record sequence matches the input, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for A3KQ86 (Zebrafish Plasmolipin, 173 aa, sequence matched) lists exactly four helical transmembrane segments at 35..55, 68..88, 99..119, and 139..159, matching choice B precisely. The evidence code ECO:0000255 indicates these are inferred by similarity (computational), not experimentally determined, but the annotation is consistent with the sequence. Sequence-level hydrophobicity analysis also supports these boundaries: the 56-67 extracellular loop contains polar residues (S, T, H, Y) and helix-breaking residues (P at 58, P at 63, G at 66), making 68..88 a more plausible hydrophobic helix start than 63..83.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [H3](#evidence-h3), [H5](#evidence-h5), [H7](#evidence-h7), [H9](#evidence-h9).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The question can be addressed through hydrophobicity analysis of the sequence. (1) Counting long hydrophobic stretches (~20 residues) identifies four candidate TM helices, eliminating C (one TM) and A (three TMs, missing the second). (2) The critical distinction between B (68..88) and D (63..83) rests on the composition of residues 63-67: P(63), A(64), L(65), G(66), W(67). Proline and glycine are well-established alpha-helix breakers; their presence within a proposed 21-residue TM helix (63..83) is structurally implausible. Additionally, residues 56-62 (S, T, P, H, Y, L, I) are predominantly polar/charged, forming a clear extracellular loop. Starting the helix at 68 (V) yields a clean hydrophobic stretch VLFVSITLWLLSIALLVILL. The flanking polar/charged residues at 89-93 (S, L, H, Q, R) confirm the helix end at 88.


**Missing item-specific fact**

> None strictly required. The helix-breaking properties of proline and glycine, the hydrophobicity of the 68-88 stretch, and the polar character of the 56-67 loop are all general biochemical knowledge applicable to any sequence.


**Reason**

> A model with general knowledge of TM helix composition (hydrophobic residues, ~20-aa length, avoidance of helix breakers like Pro and Gly in the transmembrane core) can distinguish B from D by identifying P at 63 and G at 66 as incompatible with a TM helix, and can distinguish B from A and C by recognizing four distinct hydrophobic stretches. The exact residue-level boundaries require precision but are defensible from the sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While one might argue for slight boundary shifts (e.g., 67..88 vs 68..88), the choices are constructed so that only B matches both the correct number of TMs (four) and a helix composition free of internal helix-breaking residues. D is clearly weaker because it includes P and G within the helix. A and C omit TMs that are clearly hydrophobic in the sequence.


### Important caveats

- All four TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions from homology, not experimental measurements. The 'correct' answer reflects a database annotation, not experimentally validated topology.
- The UniProt entry was first public on 2025-02-05; the author's source snapshot date is unknown, though the sequence version (1) has been stable since 2007.
- The reviewer-only evidence (accession A3KQ86, UniProt annotations) was not available to the evaluated model; the model must reason from the raw sequence and general biology alone.
- Exact TM boundaries (e.g., whether the helix starts at 67 or 68) are inherently approximate in computational predictions; the question's multiple-choice format constrains the answer to the provided options.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The question can be addressed through hydrophobicity analysis of the sequence. (1) Counting long hydrophobic stretches (~20 residues) identifies four candidate TM helices, eliminating C (one TM) and A (three TMs, missing the second). (2) The critical distinction between B (68..88) and D (63..83) rests on the composition of residues 63-67: P(63), A(64), L(65), G(66), W(67). Proline and glycine are well-established alpha-helix breakers; their presence within a proposed 21-residue TM helix (63..83) is structurally implausible. Additionally, residues 56-62 (S, T, P, H, Y, L, I) are predominantly polar/charged, forming a clear extracellular loop. Starting the helix at 68 (V) yields a clean hydrophobic stretch VLFVSITLWLLSIALLVILL. The flanking polar/charged residues at 89-93 (S, L, H, Q, R) confirm the helix end at 88.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. The helix-breaking properties of proline and glycine, the hydrophobicity of the 68-88 stretch, and the polar character of the 56-67 loop are all general biochemical knowledge applicable to any sequence.",
    "reason": "A model with general knowledge of TM helix composition (hydrophobic residues, ~20-aa length, avoidance of helix breakers like Pro and Gly in the transmembrane core) can distinguish B from D by identifying P at 63 and G at 66 as incompatible with a TM helix, and can distinguish B from A and C by recognizing four distinct hydrophobic stretches. The exact residue-level boundaries require precision but are defensible from the sequence alone."
  },
  "case_id": "transmembrane_0049",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C8",
      "C10",
      "C12",
      "H3",
      "H5",
      "H7",
      "H9"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for A3KQ86 (Zebrafish Plasmolipin, 173 aa, sequence matched) lists exactly four helical transmembrane segments at 35..55, 68..88, 99..119, and 139..159, matching choice B precisely. The evidence code ECO:0000255 indicates these are inferred by similarity (computational), not experimentally determined, but the annotation is consistent with the sequence. Sequence-level hydrophobicity analysis also supports these boundaries: the 56-67 extracellular loop contains polar residues (S, T, H, Y) and helix-breaking residues (P at 58, P at 63, G at 66), making 68..88 a more plausible hydrophobic helix start than 63..83."
  },
  "important_caveats": [
    "All four TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions from homology, not experimental measurements. The 'correct' answer reflects a database annotation, not experimentally validated topology.",
    "The UniProt entry was first public on 2025-02-05; the author's source snapshot date is unknown, though the sequence version (1) has been stable since 2007.",
    "The reviewer-only evidence (accession A3KQ86, UniProt annotations) was not available to the evaluated model; the model must reason from the raw sequence and general biology alone.",
    "Exact TM boundaries (e.g., whether the helix starts at 67 or 68) are inherently approximate in computational predictions; the question's multiple-choice format constrains the answer to the provided options."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While one might argue for slight boundary shifts (e.g., 67..88 vs 68..88), the choices are constructed so that only B matches both the correct number of TMs (four) and a helix composition free of internal helix-breaking residues. D is clearly weaker because it includes P and G within the helix. A and C omit TMs that are clearly hydrophobic in the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0049",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for A3KQ86 (Zebrafish Plasmolipin, 173 aa, sequence matched) lists exactly four helical transmembrane segments at 35..55, 68..88, 99..119, and 139..159, matching choice B precisely. The evidence code ECO:0000255 indicates these are inferred by similarity (computational), not experimentally determined, but the annotation is consistent with the sequence. Sequence-level hydrophobicity analysis also supports these boundaries: the 56-67 extracellular loop contains polar residues (S, T, H, Y) and helix-breaking residues (P at 58, P at 63, G at 66), making 68..88 a more plausible hydrophobic helix start than 63..83.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "H3", "H5", "H7", "H9"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The question can be addressed through hydrophobicity analysis of the sequence. (1) Counting long hydrophobic stretches (~20 residues) identifies four candidate TM helices, eliminating C (one TM) and A (three TMs, missing the second). (2) The critical distinction between B (68..88) and D (63..83) rests on the composition of residues 63-67: P(63), A(64), L(65), G(66), W(67). Proline and glycine are well-established alpha-helix breakers; their presence within a proposed 21-residue TM helix (63..83) is structurally implausible. Additionally, residues 56-62 (S, T, P, H, Y, L, I) are predominantly polar/charged, forming a clear extracellular loop. Starting the helix at 68 (V) yields a clean hydrophobic stretch VLFVSITLWLLSIALLVILL. The flanking polar/charged residues at 89-93 (S, L, H, Q, R) confirm the helix end at 88.",
    "missing_item_specific_fact": "None strictly required. The helix-breaking properties of proline and glycine, the hydrophobicity of the 68-88 stretch, and the polar character of the 56-67 loop are all general biochemical knowledge applicable to any sequence.",
    "reason": "A model with general knowledge of TM helix composition (hydrophobic residues, ~20-aa length, avoidance of helix breakers like Pro and Gly in the transmembrane core) can distinguish B from D by identifying P at 63 and G at 66 as incompatible with a TM helix, and can distinguish B from A and C by recognizing four distinct hydrophobic stretches. The exact residue-level boundaries require precision but are defensible from the sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While one might argue for slight boundary shifts (e.g., 67..88 vs 68..88), the choices are constructed so that only B matches both the correct number of TMs (four) and a helix composition free of internal helix-breaking residues. D is clearly weaker because it includes P and G within the helix. A and C omit TMs that are clearly hydrophobic in the sequence."
  },
  "important_caveats": [
    "All four TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions from homology, not experimental measurements. The 'correct' answer reflects a database annotation, not experimentally validated topology.",
    "The UniProt entry was first public on 2025-02-05; the author's source snapshot date is unknown, though the sequence version (1) has been stable since 2007.",
    "The reviewer-only evidence (accession A3KQ86, UniProt annotations) was not available to the evaluated model; the model must reason from the raw sequence and general biology alone.",
    "Exact TM boundaries (e.g., whether the helix starts at 67 or 68) are inherently approximate in computational predictions; the question's multiple-choice format constrains the answer to the provided options."
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

**Accession:** `A3KQ86` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 121. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3KQ86.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:56.110007+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":55},"start":{"modifier":"EXACT","value":35}},"type":"Transmembrane"}
```

Source SHA-256: `71db059b7d92b9cbb982c45261c2eacda70b05b9667017a735c6b72a71c6846e`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3KQ86.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:56.110007+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":88},"start":{"modifier":"EXACT","value":68}},"type":"Transmembrane"}
```

Source SHA-256: `71db059b7d92b9cbb982c45261c2eacda70b05b9667017a735c6b72a71c6846e`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3KQ86.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:56.110007+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":119},"start":{"modifier":"EXACT","value":99}},"type":"Transmembrane"}
```

Source SHA-256: `71db059b7d92b9cbb982c45261c2eacda70b05b9667017a735c6b72a71c6846e`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3KQ86.json)  
**Locator:** `/features/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:56.110007+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":159},"start":{"modifier":"EXACT","value":139}},"type":"Transmembrane"}
```

Source SHA-256: `71db059b7d92b9cbb982c45261c2eacda70b05b9667017a735c6b72a71c6846e`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3KQ86?format=txt&versions=121)  
**Locator:** `lines 153-155`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 121 / 1.  
**Retrieved:** 2026-11-02T04:26:58.657829+00:00.  

```text
FT   TRANSMEM        35..55
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `a6866759886a22c2e64aae8941e7fe997c98c66a52079a88daaa7c18d3ddd601`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3KQ86?format=txt&versions=121)  
**Locator:** `lines 159-161`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 121 / 1.  
**Retrieved:** 2026-11-02T04:26:58.657829+00:00.  

```text
FT   TRANSMEM        68..88
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `a6866759886a22c2e64aae8941e7fe997c98c66a52079a88daaa7c18d3ddd601`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3KQ86?format=txt&versions=121)  
**Locator:** `lines 165-167`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 121 / 1.  
**Retrieved:** 2026-11-02T04:26:58.657829+00:00.  

```text
FT   TRANSMEM        99..119
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `a6866759886a22c2e64aae8941e7fe997c98c66a52079a88daaa7c18d3ddd601`.

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3KQ86?format=txt&versions=121)  
**Locator:** `lines 171-173`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 121 / 1.  
**Retrieved:** 2026-11-02T04:26:58.657829+00:00.  

```text
FT   TRANSMEM        139..159
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `a6866759886a22c2e64aae8941e7fe997c98c66a52079a88daaa7c18d3ddd601`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 49. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
