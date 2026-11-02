# transmembrane_0112

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **C** — 5..25; 46..66; 74..94; 179..199; 239..259; 264..284; 296..316

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MWLSTFLALLIFVECVIVVYIPAYIESKLSKIKKNRFFNMENFENIASGAILALAFLHMLPEVIILSNKKNMNLYYIFILVLVSVTFLNITDILYDHHFESTFDVNCTLACENSNNQIKNINDKEITTNYIDIKSNEVIDLELKAMDTNINNNNNNNNNNKTDPCKTNIFFEIFKSNSFFIVLSLFIHSFIEGLLMGSLKDKNAIIIVGLSMLAHKWAECLIVYKNVVNKIENPLLASIYAWSFILSLPLGVFIAIFSFPSNEFVEIIFSSIACGFFLYLSFNMTKEIKITKSNKHFISFSYFLGVGGMSTLMILFNSFESNNII

[Multiple Choices]
A. 5..25; 46..66; 179..199; 239..259; 264..284; 296..316
B. 4..24
C. 5..25; 46..66; 74..94; 179..199; 239..259; 264..284; 296..316
D. 5..25; 44..68; 74..94; 179..199; 239..259; 264..284; 296..316
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

> The sequence-matched UniProt record annotates all six regions listed in choice C as transmembrane helices. These are computationally evidenced annotations (ECO:0000255), not direct experimental confirmation.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Hydrophobic stretches in the sequence support several membrane-spanning helices, including the additional region represented in C and D but omitted in A. However, broad hydropathy does not establish whether the first helix should be delimited as 46..66 or 44..68.


**Missing item-specific fact**

> The exact predicted or annotated boundaries for this particular protein, especially the choice between 46..66 and 44..68.


**Reason**

> Sequence-based reasoning supports the general multi-pass membrane-protein interpretation, but the options require exact region boundaries that cannot be reliably distinguished from the supplied sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> Both choices include the same apparent membrane-spanning stretches, and 44..68 extends the 46..66 hydrophobic core into flanking residues. The question gives no boundary tolerance or criterion for exact endpoints.


### Important caveats

- The supporting database features are computationally evidenced annotations, not evidence of experimental measurement.
- The current and historical database records match the supplied sequence; the actual source snapshot used by the author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Hydrophobic stretches in the sequence support several membrane-spanning helices, including the additional region represented in C and D but omitted in A. However, broad hydropathy does not establish whether the first helix should be delimited as 46..66 or 44..68.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact predicted or annotated boundaries for this particular protein, especially the choice between 46..66 and 44..68.",
    "reason": "Sequence-based reasoning supports the general multi-pass membrane-protein interpretation, but the options require exact region boundaries that cannot be reliably distinguished from the supplied sequence alone."
  },
  "case_id": "transmembrane_0112",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "C10",
      "C11",
      "H3",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates all six regions listed in choice C as transmembrane helices. These are computationally evidenced annotations (ECO:0000255), not direct experimental confirmation."
  },
  "important_caveats": [
    "The supporting database features are computationally evidenced annotations, not evidence of experimental measurement.",
    "The current and historical database records match the supplied sequence; the actual source snapshot used by the author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "Both choices include the same apparent membrane-spanning stretches, and 44..68 extends the 46..66 hydrophobic core into flanking residues. The question gives no boundary tolerance or criterion for exact endpoints."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0112",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates all six regions listed in choice C as transmembrane helices. These are computationally evidenced annotations (ECO:0000255), not direct experimental confirmation.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "C11", "H3", "H4", "H5", "H6", "H7", "H8", "H9"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Hydrophobic stretches in the sequence support several membrane-spanning helices, including the additional region represented in C and D but omitted in A. However, broad hydropathy does not establish whether the first helix should be delimited as 46..66 or 44..68.",
    "missing_item_specific_fact": "The exact predicted or annotated boundaries for this particular protein, especially the choice between 46..66 and 44..68.",
    "reason": "Sequence-based reasoning supports the general multi-pass membrane-protein interpretation, but the options require exact region boundaries that cannot be reliably distinguished from the supplied sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "Both choices include the same apparent membrane-spanning stretches, and 44..68 extends the 46..66 hydrophobic core into flanking residues. The question gives no boundary tolerance or criterion for exact endpoints."
  },
  "important_caveats": [
    "The supporting database features are computationally evidenced annotations, not evidence of experimental measurement.",
    "The current and historical database records match the supplied sequence; the actual source snapshot used by the author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for Q8IJI1 (ZIPCO_PLAF7) lists exactly seven transmembrane helical regions at positions 5..25, 46..66, 74..94, 179..199, 239..259, 264..284, and 296..316, matching Choice C precisely. The sequence SHA256 matches between the benchmark input and the UniProt entry. However, all annotations carry evidence code ECO:0000255 (inferred by similarity/prorule), indicating computational prediction transferred from homologs rather than experimental determination.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The C vs D distinction is resolvable by hydrophobicity: D's second region (44..68) includes E44 and N45 at the N-terminus and S67, N68 at the C-terminus—charged/polar residues that destabilize a TM helix—whereas C's 46..66 (IASGAILALAFLHMLPEVIIL) begins and ends with hydrophobic residues. The A vs C distinction (presence of 74..94) is arguable: the segment LYYIFILVLVSVTFLNITDI has a hydrophobic core (YYIFILVLV, mean KD ~3.8) flanked by polar residues, giving an average hydrophobicity (~+1.7) above the bilayer threshold, and ZIP-domain transporters characteristically contain 7–8 TM helices, making omission of a seventh region biologically implausible for this protein family.


**Missing item-specific fact**

> The exact boundary assignments (e.g., whether the second TM starts at 46 vs 45, or the third spans 74..94 vs 73..93) depend on the specific prediction algorithm (prorule/similar) used by the annotator. A model using a different hydrophobicity window or threshold might shift boundaries by 1–2 residues, though this would not change the overall region count or the C-vs-D discrimination.


**Reason**

> The primary discriminations (C vs D by boundary hydrophobicity; A vs C by expected ZIP-domain topology of 7 TM helices) are addressable through general membrane-biophysics reasoning and protein-family knowledge. The exact residue-level boundaries are somewhat algorithm-dependent but do not prevent distinguishing the four options.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choice B is clearly wrong (single region, wrong start). Choice D is distinguishable from C by the inclusion of polar residues (E, N, S, N) in the second TM boundary. Choice A omits a region that has sufficient hydrophobic character and is expected for a 7-TM ZIP transporter. No two options are equally defensible given standard membrane-protein reasoning.


### Important caveats

- All seven TM annotations are ECO:0000255 (inferred by similarity/prorule), i.e., computational predictions transferred from homologs, not experimental measurements (no crystal structure or cross-linking data cited for this protein).
- The 74..94 region is borderline in hydrophobicity (avg KD ~+1.7 with embedded polar residues S, T, N, T, D); a strict hydrophobicity-window predictor might miss it, making the A-vs-C discrimination less clean than the C-vs-D discrimination.
- The UniProt entry was first public on 2025-06-18; the author source snapshot is unknown, though the sequence version 2 has been stable since 2009.
- Exact TM boundaries in prorule/similar annotations can vary by ±1–2 residues across prediction tools; the question rewards matching one specific algorithm's output.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The C vs D distinction is resolvable by hydrophobicity: D's second region (44..68) includes E44 and N45 at the N-terminus and S67, N68 at the C-terminus—charged/polar residues that destabilize a TM helix—whereas C's 46..66 (IASGAILALAFLHMLPEVIIL) begins and ends with hydrophobic residues. The A vs C distinction (presence of 74..94) is arguable: the segment LYYIFILVLVSVTFLNITDI has a hydrophobic core (YYIFILVLV, mean KD ~3.8) flanked by polar residues, giving an average hydrophobicity (~+1.7) above the bilayer threshold, and ZIP-domain transporters characteristically contain 7–8 TM helices, making omission of a seventh region biologically implausible for this protein family.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact boundary assignments (e.g., whether the second TM starts at 46 vs 45, or the third spans 74..94 vs 73..93) depend on the specific prediction algorithm (prorule/similar) used by the annotator. A model using a different hydrophobicity window or threshold might shift boundaries by 1–2 residues, though this would not change the overall region count or the C-vs-D discrimination.",
    "reason": "The primary discriminations (C vs D by boundary hydrophobicity; A vs C by expected ZIP-domain topology of 7 TM helices) are addressable through general membrane-biophysics reasoning and protein-family knowledge. The exact residue-level boundaries are somewhat algorithm-dependent but do not prevent distinguishing the four options."
  },
  "case_id": "transmembrane_0112",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "C10",
      "C11",
      "H3",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for Q8IJI1 (ZIPCO_PLAF7) lists exactly seven transmembrane helical regions at positions 5..25, 46..66, 74..94, 179..199, 239..259, 264..284, and 296..316, matching Choice C precisely. The sequence SHA256 matches between the benchmark input and the UniProt entry. However, all annotations carry evidence code ECO:0000255 (inferred by similarity/prorule), indicating computational prediction transferred from homologs rather than experimental determination."
  },
  "important_caveats": [
    "All seven TM annotations are ECO:0000255 (inferred by similarity/prorule), i.e., computational predictions transferred from homologs, not experimental measurements (no crystal structure or cross-linking data cited for this protein).",
    "The 74..94 region is borderline in hydrophobicity (avg KD ~+1.7 with embedded polar residues S, T, N, T, D); a strict hydrophobicity-window predictor might miss it, making the A-vs-C discrimination less clean than the C-vs-D discrimination.",
    "The UniProt entry was first public on 2025-06-18; the author source snapshot is unknown, though the sequence version 2 has been stable since 2009.",
    "Exact TM boundaries in prorule/similar annotations can vary by ±1–2 residues across prediction tools; the question rewards matching one specific algorithm's output."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice B is clearly wrong (single region, wrong start). Choice D is distinguishable from C by the inclusion of polar residues (E, N, S, N) in the second TM boundary. Choice A omits a region that has sufficient hydrophobic character and is expected for a 7-TM ZIP transporter. No two options are equally defensible given standard membrane-protein reasoning."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0112",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for Q8IJI1 (ZIPCO_PLAF7) lists exactly seven transmembrane helical regions at positions 5..25, 46..66, 74..94, 179..199, 239..259, 264..284, and 296..316, matching Choice C precisely. The sequence SHA256 matches between the benchmark input and the UniProt entry. However, all annotations carry evidence code ECO:0000255 (inferred by similarity/prorule), indicating computational prediction transferred from homologs rather than experimental determination.",
    "evidence_ids": ["C5","C6","C7","C8","C9","C10","C11","H3","H4","H5","H6","H7","H8","H9"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The C vs D distinction is resolvable by hydrophobicity: D's second region (44..68) includes E44 and N45 at the N-terminus and S67, N68 at the C-terminus—charged/polar residues that destabilize a TM helix—whereas C's 46..66 (IASGAILALAFLHMLPEVIIL) begins and ends with hydrophobic residues. The A vs C distinction (presence of 74..94) is arguable: the segment LYYIFILVLVSVTFLNITDI has a hydrophobic core (YYIFILVLV, mean KD ~3.8) flanked by polar residues, giving an average hydrophobicity (~+1.7) above the bilayer threshold, and ZIP-domain transporters characteristically contain 7–8 TM helices, making omission of a seventh region biologically implausible for this protein family.",
    "missing_item_specific_fact": "The exact boundary assignments (e.g., whether the second TM starts at 46 vs 45, or the third spans 74..94 vs 73..93) depend on the specific prediction algorithm (prorule/similar) used by the annotator. A model using a different hydrophobicity window or threshold might shift boundaries by 1–2 residues, though this would not change the overall region count or the C-vs-D discrimination.",
    "reason": "The primary discriminations (C vs D by boundary hydrophobicity; A vs C by expected ZIP-domain topology of 7 TM helices) are addressable through general membrane-biophysics reasoning and protein-family knowledge. The exact residue-level boundaries are somewhat algorithm-dependent but do not prevent distinguishing the four options."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice B is clearly wrong (single region, wrong start). Choice D is distinguishable from C by the inclusion of polar residues (E, N, S, N) in the second TM boundary. Choice A omits a region that has sufficient hydrophobic character and is expected for a 7-TM ZIP transporter. No two options are equally defensible given standard membrane-protein reasoning."
  },
  "important_caveats": [
    "All seven TM annotations are ECO:0000255 (inferred by similarity/prorule), i.e., computational predictions transferred from homologs, not experimental measurements (no crystal structure or cross-linking data cited for this protein).",
    "The 74..94 region is borderline in hydrophobicity (avg KD ~+1.7 with embedded polar residues S, T, N, T, D); a strict hydrophobicity-window predictor might miss it, making the A-vs-C discrimination less clean than the C-vs-D discrimination.",
    "The UniProt entry was first public on 2025-06-18; the author source snapshot is unknown, though the sequence version 2 has been stable since 2009.",
    "Exact TM boundaries in prorule/similar annotations can vary by ±1–2 residues across prediction tools; the question rewards matching one specific algorithm's output."
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

**Accession:** `Q8IJI1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 99. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IJI1.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:13.245159+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":25},"start":{"modifier":"EXACT","value":5}},"type":"Transmembrane"}
```

Source SHA-256: `98ec602d5ce9074cc044866398ff14a3b6a28ea7f4a3afc0eb6d37bd83fd5f25`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IJI1.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:13.245159+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":66},"start":{"modifier":"EXACT","value":46}},"type":"Transmembrane"}
```

Source SHA-256: `98ec602d5ce9074cc044866398ff14a3b6a28ea7f4a3afc0eb6d37bd83fd5f25`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IJI1.json)  
**Locator:** `/features/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:13.245159+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":94},"start":{"modifier":"EXACT","value":74}},"type":"Transmembrane"}
```

Source SHA-256: `98ec602d5ce9074cc044866398ff14a3b6a28ea7f4a3afc0eb6d37bd83fd5f25`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IJI1.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:13.245159+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":199},"start":{"modifier":"EXACT","value":179}},"type":"Transmembrane"}
```

Source SHA-256: `98ec602d5ce9074cc044866398ff14a3b6a28ea7f4a3afc0eb6d37bd83fd5f25`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IJI1.json)  
**Locator:** `/features/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:13.245159+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":259},"start":{"modifier":"EXACT","value":239}},"type":"Transmembrane"}
```

Source SHA-256: `98ec602d5ce9074cc044866398ff14a3b6a28ea7f4a3afc0eb6d37bd83fd5f25`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IJI1.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:13.245159+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":284},"start":{"modifier":"EXACT","value":264}},"type":"Transmembrane"}
```

Source SHA-256: `98ec602d5ce9074cc044866398ff14a3b6a28ea7f4a3afc0eb6d37bd83fd5f25`.

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IJI1.json)  
**Locator:** `/features/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:13.245159+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":316},"start":{"modifier":"EXACT","value":296}},"type":"Transmembrane"}
```

Source SHA-256: `98ec602d5ce9074cc044866398ff14a3b6a28ea7f4a3afc0eb6d37bd83fd5f25`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IJI1?format=txt&versions=99)  
**Locator:** `lines 87-89`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 99 / 2.  
**Retrieved:** 2026-11-02T04:32:15.953075+00:00.  

```text
FT   TRANSMEM        5..25
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `a185b20a7b70bc0a98ff98aba7bf611816a4de98cce29ce98fad70203aaa6f76`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IJI1?format=txt&versions=99)  
**Locator:** `lines 90-92`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 99 / 2.  
**Retrieved:** 2026-11-02T04:32:15.953075+00:00.  

```text
FT   TRANSMEM        46..66
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `a185b20a7b70bc0a98ff98aba7bf611816a4de98cce29ce98fad70203aaa6f76`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IJI1?format=txt&versions=99)  
**Locator:** `lines 93-95`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 99 / 2.  
**Retrieved:** 2026-11-02T04:32:15.953075+00:00.  

```text
FT   TRANSMEM        74..94
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `a185b20a7b70bc0a98ff98aba7bf611816a4de98cce29ce98fad70203aaa6f76`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IJI1?format=txt&versions=99)  
**Locator:** `lines 96-98`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 99 / 2.  
**Retrieved:** 2026-11-02T04:32:15.953075+00:00.  

```text
FT   TRANSMEM        179..199
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `a185b20a7b70bc0a98ff98aba7bf611816a4de98cce29ce98fad70203aaa6f76`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IJI1?format=txt&versions=99)  
**Locator:** `lines 99-101`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 99 / 2.  
**Retrieved:** 2026-11-02T04:32:15.953075+00:00.  

```text
FT   TRANSMEM        239..259
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `a185b20a7b70bc0a98ff98aba7bf611816a4de98cce29ce98fad70203aaa6f76`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IJI1?format=txt&versions=99)  
**Locator:** `lines 102-104`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 99 / 2.  
**Retrieved:** 2026-11-02T04:32:15.953075+00:00.  

```text
FT   TRANSMEM        264..284
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `a185b20a7b70bc0a98ff98aba7bf611816a4de98cce29ce98fad70203aaa6f76`.

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IJI1?format=txt&versions=99)  
**Locator:** `lines 105-107`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 99 / 2.  
**Retrieved:** 2026-11-02T04:32:15.953075+00:00.  

```text
FT   TRANSMEM        296..316
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `a185b20a7b70bc0a98ff98aba7bf611816a4de98cce29ce98fad70203aaa6f76`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 112. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
