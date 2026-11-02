# transmembrane_0013

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **C** — 29..49; 66..86; 98..118; 141..163; 196..216; 237..257; 270..290

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MEVSNMTTVTVFILLGLSNNPQVQALLFVLFLVIYLLTLLGNLLMVLVISTDSHLCTPMYFFLRQLSFLDAFYSSIIVPKLLENLLSKGETISFLECFTQISLVIFSGATEACLLSVMAYDRFQAMCHPLLYVVIINRRVCAGLVGASWAIGMGTGLINTLLLAQQHFCGPNVIHSFACELPPVLLLTCSDPCASIVSILTTMSVLGLGTLVLLLGSYSCIIMTALRINSATGRSKIFSTCSSHFLVVTIFYTSGVLRYMIPASGSALEQVLSVQYSVITPLLNPLIYSLKSQEVKVALRRMLARKSRLPL

[Multiple Choices]
A. 278..286; 308..323
B. 32..52; 66..86; 98..118; 141..163; 196..216; 237..257; 270..290
C. 29..49; 66..86; 98..118; 141..163; 196..216; 237..257; 270..290
D. 29..49; 66..86; 98..118; 196..216; 237..257; 270..290
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

> The exact sequence matches the UniProt record, whose historical and current annotations list the seven transmembrane regions in choice C. The transmembrane annotations carry evidence code ECO:0000255, indicating computational annotation rather than, on this evidence, experimental validation.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [H3](#evidence-h3), [H5](#evidence-h5), [H7](#evidence-h7), [H9](#evidence-h9), [H11](#evidence-h11), [H13](#evidence-h13), [H15](#evidence-h15).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has the repeated hydrophobic segments expected of a seven-transmembrane receptor, which supports the shared overall pattern in choices B and C. It does not decisively establish whether the first segment begins at residue 29 or 32.


**Missing item-specific fact**

> The precise annotated boundary for the first transmembrane helix, 29 rather than 32, is needed to select C over B.


**Reason**

> General sequence reasoning supports the broad locations of the helices, but the near-identical B and C options differ only by a three-residue boundary shift within the same hydrophobic region. Choosing between them depends on a protein-specific boundary annotation or prediction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> Both choices identify the same seven broadly hydrophobic segments; their only difference is whether the first begins at residue 32 or 29, a boundary not clearly distinguishable from the supplied sequence alone.


### Important caveats

- The reviewer-only UniProt evidence matches the supplied sequence, but the author’s exact source snapshot is unknown.
- The cited transmembrane annotations are computationally evidenced; this support does not establish experimental measurement of the helix boundaries.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has the repeated hydrophobic segments expected of a seven-transmembrane receptor, which supports the shared overall pattern in choices B and C. It does not decisively establish whether the first segment begins at residue 29 or 32.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The precise annotated boundary for the first transmembrane helix, 29 rather than 32, is needed to select C over B.",
    "reason": "General sequence reasoning supports the broad locations of the helices, but the near-identical B and C options differ only by a three-residue boundary shift within the same hydrophobic region. Choosing between them depends on a protein-specific boundary annotation or prediction."
  },
  "case_id": "transmembrane_0013",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C8",
      "C10",
      "C12",
      "C14",
      "C16",
      "C18",
      "H3",
      "H5",
      "H7",
      "H9",
      "H11",
      "H13",
      "H15"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt record, whose historical and current annotations list the seven transmembrane regions in choice C. The transmembrane annotations carry evidence code ECO:0000255, indicating computational annotation rather than, on this evidence, experimental validation."
  },
  "important_caveats": [
    "The reviewer-only UniProt evidence matches the supplied sequence, but the author’s exact source snapshot is unknown.",
    "The cited transmembrane annotations are computationally evidenced; this support does not establish experimental measurement of the helix boundaries."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "Both choices identify the same seven broadly hydrophobic segments; their only difference is whether the first begins at residue 32 or 29, a boundary not clearly distinguishable from the supplied sequence alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0013",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt record, whose historical and current annotations list the seven transmembrane regions in choice C. The transmembrane annotations carry evidence code ECO:0000255, indicating computational annotation rather than, on this evidence, experimental validation.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "H3", "H5", "H7", "H9", "H11", "H13", "H15"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has the repeated hydrophobic segments expected of a seven-transmembrane receptor, which supports the shared overall pattern in choices B and C. It does not decisively establish whether the first segment begins at residue 29 or 32.",
    "missing_item_specific_fact": "The precise annotated boundary for the first transmembrane helix, 29 rather than 32, is needed to select C over B.",
    "reason": "General sequence reasoning supports the broad locations of the helices, but the near-identical B and C options differ only by a three-residue boundary shift within the same hydrophobic region. Choosing between them depends on a protein-specific boundary annotation or prediction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "Both choices identify the same seven broadly hydrophobic segments; their only difference is whether the first begins at residue 32 or 29, a boundary not clearly distinguishable from the supplied sequence alone."
  },
  "important_caveats": [
    "The reviewer-only UniProt evidence matches the supplied sequence, but the author’s exact source snapshot is unknown.",
    "The cited transmembrane annotations are computationally evidenced; this support does not establish experimental measurement of the helix boundaries."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> Choice C (29..49; 66..86; 98..118; 141..163; 196..216; 237..257; 270..290) matches the UniProt annotation for A0A2R8YED5 (Olfactory receptor 5BS1) exactly across all seven transmembrane helices. The evidence codes are ECO:0000255 (inferred by similarity), meaning these are computational annotations transferred by homology, not experimentally determined boundaries. Nevertheless, they are the canonical database annotation for this sequence, and the sequence SHA-256 matches the benchmark input.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [H3](#evidence-h3), [H5](#evidence-h5), [H7](#evidence-h7), [H9](#evidence-h9), [H11](#evidence-h11), [H13](#evidence-h13), [H15](#evidence-h15).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein is 311 residues with multiple long hydrophobic stretches, consistent with a seven-transmembrane GPCR. Olfactory receptors are canonical 7-TM GPCRs, so a model with general GPCR knowledge can eliminate A (only 2 segments) and D (only 6 segments, missing TM4 at 141..163). Between B and C, the sole difference is whether TM1 begins at residue 29 (V-L-F) or 32 (L). Positions 29–31 (V, L, F) are strongly hydrophobic and form part of the continuous hydrophobic helix core VLFLVIYLLTLLGNLLMVLVI; the preceding residues at 25–27 (A, L, L) are more ambiguous. A standard hydropathy-window analysis (e.g., Kyte-Doolittle with a 19–21 residue window) would naturally extend the TM1 helix to include VLF at position 29, favoring C. The N-terminal extracellular segment (1–28) contains polar/charged residues (S, N, N, P, Q, V, Q) that break the hydrophobic stretch before position 29, supporting a TM1 start at 29 rather than 32.


**Missing item-specific fact**

> None strictly required. The B-vs-C distinction rests on a 3-residue boundary that is resolvable by hydrophobicity analysis, though the margin is thin. The exact annotation (ECO:0000255, inferred by similarity) confirms C but is not the only path to it.


**Reason**

> The major structural reasoning (7-TM GPCR topology) eliminates A and D. The B-vs-C distinction, while narrow, can be addressed by standard hydropathy analysis: the hydrophobic residues VLF at 29–31 belong to the TM1 helix core, and the polar residues in the N-terminal region (positions ~19–28) mark the extracellular boundary. This provides a concrete, if thin, biological argument for C over B without requiring memorization of a specific database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> B and C differ only in the TM1 start position (32 vs 29, a 3-residue shift). Both boundaries are within the hydrophobic N-terminal region, and different hydropathy algorithms or window sizes could yield either boundary. C is slightly better supported because V(29), L(30), F(31) are hydrophobic and the preceding residues (A25, L26, L27, F28) are more ambiguous, but a model choosing B would not be unreasonable. The annotation evidence (ECO:0000255) is computational, not experimental, so neither boundary is experimentally fixed.


### Important caveats

- All seven TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred from homologous proteins, not experimentally validated boundaries.
- The B-vs-C distinction (3 residues in TM1) is at the threshold of what hydropathy analysis can reliably resolve; different algorithms and parameter choices could shift this boundary.
- The UniProt entry was first released 2025-02-05 and has undergone annotation updates; the historical snapshot used by the benchmark author is unknown.
- The reviewer-only evidence confirms sequence identity (SHA-256 match) but the evaluated model had no access to the UniProt annotation or accession.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein is 311 residues with multiple long hydrophobic stretches, consistent with a seven-transmembrane GPCR. Olfactory receptors are canonical 7-TM GPCRs, so a model with general GPCR knowledge can eliminate A (only 2 segments) and D (only 6 segments, missing TM4 at 141..163). Between B and C, the sole difference is whether TM1 begins at residue 29 (V-L-F) or 32 (L). Positions 29–31 (V, L, F) are strongly hydrophobic and form part of the continuous hydrophobic helix core VLFLVIYLLTLLGNLLMVLVI; the preceding residues at 25–27 (A, L, L) are more ambiguous. A standard hydropathy-window analysis (e.g., Kyte-Doolittle with a 19–21 residue window) would naturally extend the TM1 helix to include VLF at position 29, favoring C. The N-terminal extracellular segment (1–28) contains polar/charged residues (S, N, N, P, Q, V, Q) that break the hydrophobic stretch before position 29, supporting a TM1 start at 29 rather than 32.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. The B-vs-C distinction rests on a 3-residue boundary that is resolvable by hydrophobicity analysis, though the margin is thin. The exact annotation (ECO:0000255, inferred by similarity) confirms C but is not the only path to it.",
    "reason": "The major structural reasoning (7-TM GPCR topology) eliminates A and D. The B-vs-C distinction, while narrow, can be addressed by standard hydropathy analysis: the hydrophobic residues VLF at 29–31 belong to the TM1 helix core, and the polar residues in the N-terminal region (positions ~19–28) mark the extracellular boundary. This provides a concrete, if thin, biological argument for C over B without requiring memorization of a specific database entry."
  },
  "case_id": "transmembrane_0013",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C8",
      "C10",
      "C12",
      "C14",
      "C16",
      "C18",
      "H3",
      "H5",
      "H7",
      "H9",
      "H11",
      "H13",
      "H15"
    ],
    "judgment": "supported",
    "reason": "Choice C (29..49; 66..86; 98..118; 141..163; 196..216; 237..257; 270..290) matches the UniProt annotation for A0A2R8YED5 (Olfactory receptor 5BS1) exactly across all seven transmembrane helices. The evidence codes are ECO:0000255 (inferred by similarity), meaning these are computational annotations transferred by homology, not experimentally determined boundaries. Nevertheless, they are the canonical database annotation for this sequence, and the sequence SHA-256 matches the benchmark input."
  },
  "important_caveats": [
    "All seven TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred from homologous proteins, not experimentally validated boundaries.",
    "The B-vs-C distinction (3 residues in TM1) is at the threshold of what hydropathy analysis can reliably resolve; different algorithms and parameter choices could shift this boundary.",
    "The UniProt entry was first released 2025-02-05 and has undergone annotation updates; the historical snapshot used by the benchmark author is unknown.",
    "The reviewer-only evidence confirms sequence identity (SHA-256 match) but the evaluated model had no access to the UniProt annotation or accession."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "B and C differ only in the TM1 start position (32 vs 29, a 3-residue shift). Both boundaries are within the hydrophobic N-terminal region, and different hydropathy algorithms or window sizes could yield either boundary. C is slightly better supported because V(29), L(30), F(31) are hydrophobic and the preceding residues (A25, L26, L27, F28) are more ambiguous, but a model choosing B would not be unreasonable. The annotation evidence (ECO:0000255) is computational, not experimental, so neither boundary is experimentally fixed."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0013",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "Choice C (29..49; 66..86; 98..118; 141..163; 196..216; 237..257; 270..290) matches the UniProt annotation for A0A2R8YED5 (Olfactory receptor 5BS1) exactly across all seven transmembrane helices. The evidence codes are ECO:0000255 (inferred by similarity), meaning these are computational annotations transferred by homology, not experimentally determined boundaries. Nevertheless, they are the canonical database annotation for this sequence, and the sequence SHA-256 matches the benchmark input.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "H3", "H5", "H7", "H9", "H11", "H13", "H15"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein is 311 residues with multiple long hydrophobic stretches, consistent with a seven-transmembrane GPCR. Olfactory receptors are canonical 7-TM GPCRs, so a model with general GPCR knowledge can eliminate A (only 2 segments) and D (only 6 segments, missing TM4 at 141..163). Between B and C, the sole difference is whether TM1 begins at residue 29 (V-L-F) or 32 (L). Positions 29–31 (V, L, F) are strongly hydrophobic and form part of the continuous hydrophobic helix core VLFLVIYLLTLLGNLLMVLVI; the preceding residues at 25–27 (A, L, L) are more ambiguous. A standard hydropathy-window analysis (e.g., Kyte-Doolittle with a 19–21 residue window) would naturally extend the TM1 helix to include VLF at position 29, favoring C. The N-terminal extracellular segment (1–28) contains polar/charged residues (S, N, N, P, Q, V, Q) that break the hydrophobic stretch before position 29, supporting a TM1 start at 29 rather than 32.",
    "missing_item_specific_fact": "None strictly required. The B-vs-C distinction rests on a 3-residue boundary that is resolvable by hydrophobicity analysis, though the margin is thin. The exact annotation (ECO:0000255, inferred by similarity) confirms C but is not the only path to it.",
    "reason": "The major structural reasoning (7-TM GPCR topology) eliminates A and D. The B-vs-C distinction, while narrow, can be addressed by standard hydropathy analysis: the hydrophobic residues VLF at 29–31 belong to the TM1 helix core, and the polar residues in the N-terminal region (positions ~19–28) mark the extracellular boundary. This provides a concrete, if thin, biological argument for C over B without requiring memorization of a specific database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "B and C differ only in the TM1 start position (32 vs 29, a 3-residue shift). Both boundaries are within the hydrophobic N-terminal region, and different hydropathy algorithms or window sizes could yield either boundary. C is slightly better supported because V(29), L(30), F(31) are hydrophobic and the preceding residues (A25, L26, L27, F28) are more ambiguous, but a model choosing B would not be unreasonable. The annotation evidence (ECO:0000255) is computational, not experimental, so neither boundary is experimentally fixed."
  },
  "important_caveats": [
    "All seven TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred from homologous proteins, not experimentally validated boundaries.",
    "The B-vs-C distinction (3 residues in TM1) is at the threshold of what hydropathy analysis can reliably resolve; different algorithms and parameter choices could shift this boundary.",
    "The UniProt entry was first released 2025-02-05 and has undergone annotation updates; the historical snapshot used by the benchmark author is unknown.",
    "The reviewer-only evidence confirms sequence identity (SHA-256 match) but the evaluated model had no access to the UniProt annotation or accession."
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

**Accession:** `A0A2R8YED5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 28. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:45.255114+00:00.  

```json
{"description":"Helical; Name=1","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":49},"start":{"modifier":"EXACT","value":29}},"type":"Transmembrane"}
```

Source SHA-256: `d0a68a9d870084d5a8a25b212bcab1f8fc22e1d9dc23ed81cdab2f3f4f4889f2`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:45.255114+00:00.  

```json
{"description":"Helical; Name=2","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":86},"start":{"modifier":"EXACT","value":66}},"type":"Transmembrane"}
```

Source SHA-256: `d0a68a9d870084d5a8a25b212bcab1f8fc22e1d9dc23ed81cdab2f3f4f4889f2`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:45.255114+00:00.  

```json
{"description":"Helical; Name=3","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":118},"start":{"modifier":"EXACT","value":98}},"type":"Transmembrane"}
```

Source SHA-256: `d0a68a9d870084d5a8a25b212bcab1f8fc22e1d9dc23ed81cdab2f3f4f4889f2`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json)  
**Locator:** `/features/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:45.255114+00:00.  

```json
{"description":"Helical; Name=4","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":163},"start":{"modifier":"EXACT","value":141}},"type":"Transmembrane"}
```

Source SHA-256: `d0a68a9d870084d5a8a25b212bcab1f8fc22e1d9dc23ed81cdab2f3f4f4889f2`.

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json)  
**Locator:** `/features/10`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:45.255114+00:00.  

```json
{"description":"Helical; Name=5","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":216},"start":{"modifier":"EXACT","value":196}},"type":"Transmembrane"}
```

Source SHA-256: `d0a68a9d870084d5a8a25b212bcab1f8fc22e1d9dc23ed81cdab2f3f4f4889f2`.

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json)  
**Locator:** `/features/12`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:45.255114+00:00.  

```json
{"description":"Helical; Name=6","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":257},"start":{"modifier":"EXACT","value":237}},"type":"Transmembrane"}
```

Source SHA-256: `d0a68a9d870084d5a8a25b212bcab1f8fc22e1d9dc23ed81cdab2f3f4f4889f2`.

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json)  
**Locator:** `/features/14`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:45.255114+00:00.  

```json
{"description":"Helical; Name=7","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":290},"start":{"modifier":"EXACT","value":270}},"type":"Transmembrane"}
```

Source SHA-256: `d0a68a9d870084d5a8a25b212bcab1f8fc22e1d9dc23ed81cdab2f3f4f4889f2`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28)  
**Locator:** `lines 138-140`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 28 / 1.  
**Retrieved:** 2026-11-01T06:27:26.314292+00:00.  

```text
FT   TRANSMEM        29..49
FT                   /note="Helical; Name=1"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `cca1844e232709cdf49594e55779c1f7550585001e53d4c1927ed8cbc4f14327`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28)  
**Locator:** `lines 144-146`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 28 / 1.  
**Retrieved:** 2026-11-01T06:27:26.314292+00:00.  

```text
FT   TRANSMEM        66..86
FT                   /note="Helical; Name=2"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `cca1844e232709cdf49594e55779c1f7550585001e53d4c1927ed8cbc4f14327`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28)  
**Locator:** `lines 150-152`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 28 / 1.  
**Retrieved:** 2026-11-01T06:27:26.314292+00:00.  

```text
FT   TRANSMEM        98..118
FT                   /note="Helical; Name=3"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `cca1844e232709cdf49594e55779c1f7550585001e53d4c1927ed8cbc4f14327`.

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28)  
**Locator:** `lines 156-158`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 28 / 1.  
**Retrieved:** 2026-11-01T06:27:26.314292+00:00.  

```text
FT   TRANSMEM        141..163
FT                   /note="Helical; Name=4"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `cca1844e232709cdf49594e55779c1f7550585001e53d4c1927ed8cbc4f14327`.

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28)  
**Locator:** `lines 162-164`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 28 / 1.  
**Retrieved:** 2026-11-01T06:27:26.314292+00:00.  

```text
FT   TRANSMEM        196..216
FT                   /note="Helical; Name=5"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `cca1844e232709cdf49594e55779c1f7550585001e53d4c1927ed8cbc4f14327`.

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28)  
**Locator:** `lines 168-170`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 28 / 1.  
**Retrieved:** 2026-11-01T06:27:26.314292+00:00.  

```text
FT   TRANSMEM        237..257
FT                   /note="Helical; Name=6"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `cca1844e232709cdf49594e55779c1f7550585001e53d4c1927ed8cbc4f14327`.

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28)  
**Locator:** `lines 174-176`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 28 / 1.  
**Retrieved:** 2026-11-01T06:27:26.314292+00:00.  

```text
FT   TRANSMEM        270..290
FT                   /note="Helical; Name=7"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `cca1844e232709cdf49594e55779c1f7550585001e53d4c1927ed8cbc4f14327`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 13. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
