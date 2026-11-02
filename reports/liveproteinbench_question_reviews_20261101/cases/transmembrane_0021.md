# transmembrane_0021

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **B** — 9..45; 50..80; 86..121; 130..156; 173..210; 215..250; 261..289

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MCNVSQDSCNIDSRLDSLFPPTLYIFVMVIGFPTNCLSLWAAFVQVRQKNELGVYLLNLSISDLLYIATLPPWVNYFLHQDNWIHGPESCKLFGFILYTNIYISIGFLSCISVDRYLAVAHPLKFAKVRRVKTAAVVSAVVWAIEIGANSAPLFHNELFEDRFNHTFCFEKYPMEDWVAQMNLYRVFVGFLFPWVLMLFCYQGILRAVKTNVSTEREEKAKIKRLALSLIAILLFCFAPYHLILLSRSVVYLGQPCDCTFEENIFTAYHVSLALTSLNCVADPILYCLANEGARSEVTRGLAPLMKFFSASRPNMDSFARSVTLDTPWSSRRAAAPSPRSWSLCGQTGGRGRRSRVRRRRDCKC

[Multiple Choices]
A. 50..80; 86..121; 130..156; 173..210; 215..250; 261..289
B. 9..45; 50..80; 86..121; 130..156; 173..210; 215..250; 261..289
C. 9..45; 54..80; 86..121; 130..156; 173..210; 215..250; 261..289
D. 305..325
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

> The exact sequence matches the historical UniProt entry, whose annotated transmembrane segments correspond to choice B. These annotations are transferred by similarity from another UniProt entry (ECO:0000250), so they support the key as database annotation, not as direct experimental mapping for this sequence.

Citations as saved: [H4](#evidence-h4), [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has multiple hydrophobic stretches consistent with a multi-pass membrane protein, and the segment around residues 54–80 is notably hydrophobic. This supports a broad membrane-spanning interpretation but does not establish the exact annotated boundaries.


**Missing item-specific fact**

> The specific transmembrane boundary annotation for this protein or a homolog, particularly whether the second segment is annotated as 50–80 or 54–80.


**Reason**

> General sequence reasoning supports identifying likely membrane-spanning regions, but the choices require precise boundaries. Distinguishing B from C depends on a protein-specific boundary assignment not supplied in the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> B matches the cited annotation, while C starts the second segment at the strongly hydrophobic portion of the same stretch. The sequence alone does not uniquely determine whether residues 50–53 belong to the predicted transmembrane interval.


### Important caveats

- The historical entry matches the supplied sequence, but the actual source snapshot used by the author is unknown.
- The cited transmembrane annotations are similarity-based transfers, not evidence of direct experimental boundary determination for this sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has multiple hydrophobic stretches consistent with a multi-pass membrane protein, and the segment around residues 54–80 is notably hydrophobic. This supports a broad membrane-spanning interpretation but does not establish the exact annotated boundaries.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific transmembrane boundary annotation for this protein or a homolog, particularly whether the second segment is annotated as 50–80 or 54–80.",
    "reason": "General sequence reasoning supports identifying likely membrane-spanning regions, but the choices require precise boundaries. Distinguishing B from C depends on a protein-specific boundary assignment not supplied in the question."
  },
  "case_id": "transmembrane_0021",
  "expected_answer_check": {
    "evidence_ids": [
      "H4",
      "H6",
      "H8",
      "H10",
      "H12",
      "H14",
      "H16"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the historical UniProt entry, whose annotated transmembrane segments correspond to choice B. These annotations are transferred by similarity from another UniProt entry (ECO:0000250), so they support the key as database annotation, not as direct experimental mapping for this sequence."
  },
  "important_caveats": [
    "The historical entry matches the supplied sequence, but the actual source snapshot used by the author is unknown.",
    "The cited transmembrane annotations are similarity-based transfers, not evidence of direct experimental boundary determination for this sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "B matches the cited annotation, while C starts the second segment at the strongly hydrophobic portion of the same stretch. The sequence alone does not uniquely determine whether residues 50–53 belong to the predicted transmembrane interval."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0021",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the historical UniProt entry, whose annotated transmembrane segments correspond to choice B. These annotations are transferred by similarity from another UniProt entry (ECO:0000250), so they support the key as database annotation, not as direct experimental mapping for this sequence.",
    "evidence_ids": ["H4", "H6", "H8", "H10", "H12", "H14", "H16"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has multiple hydrophobic stretches consistent with a multi-pass membrane protein, and the segment around residues 54–80 is notably hydrophobic. This supports a broad membrane-spanning interpretation but does not establish the exact annotated boundaries.",
    "missing_item_specific_fact": "The specific transmembrane boundary annotation for this protein or a homolog, particularly whether the second segment is annotated as 50–80 or 54–80.",
    "reason": "General sequence reasoning supports identifying likely membrane-spanning regions, but the choices require precise boundaries. Distinguishing B from C depends on a protein-specific boundary assignment not supplied in the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "B matches the cited annotation, while C starts the second segment at the strongly hydrophobic portion of the same stretch. The sequence alone does not uniquely determine whether residues 50–53 belong to the predicted transmembrane interval."
  },
  "important_caveats": [
    "The historical entry matches the supplied sequence, but the actual source snapshot used by the author is unknown.",
    "The cited transmembrane annotations are similarity-based transfers, not evidence of direct experimental boundary determination for this sequence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for A0A4W3GG95 (GPR4_CALMI, ghost shark GPCR) lists exactly seven transmembrane helices at 9..45, 50..80, 86..121, 130..156, 173..210, 215..250, and 261..289, matching option B precisely. The sequence in the question matches the UniProt entry (SHA-256 confirmed). However, all TM annotations carry evidence code ECO:0000250 (similarity transfer from A0A6I8PUB9), indicating computational inference rather than direct experimental determination for this specific protein.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [H4](#evidence-h4), [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Recognizing the protein as a 7-TM GPCR eliminates option D (single 21-residue segment) and option A (only 6 TM segments). However, distinguishing B from C requires resolving whether TM2 begins at position 50 (N-E-L-G) or 54 (V-Y-L-L). Positions 50-51 are Asn and Glu—clearly hydrophilic/charged residues atypical of a TM helix core—while position 54 onward (VYLLNLSISDLLYIATLPPWVNYFLHQ) is substantially more hydrophobic. A pure hydrophobicity analysis would arguably favor option C (TM2 starting at 54). The specific 4-residue boundary at TM2's N-terminus cannot be reliably resolved by general biological reasoning.


**Missing item-specific fact**

> The exact TM2 start position (50 vs 54) for this particular GPR4 ortholog, as determined by the similarity-transfer annotation from A0A6I8PUB9. No experimental structure or mutagenesis data for this specific boundary is provided.


**Reason**

> While the 7-TM GPCR topology narrows choices to B or C, the critical distinction (TM2 start at 50 vs 54) is a 4-residue boundary difference. Hydrophobicity analysis of residues 50-53 (N, E, L, G) actually slightly disfavors their inclusion in a TM helix, making C arguably more defensible by sequence reasoning. Resolving B over C depends on the specific database annotation boundary, which is an item-specific external fact not derivable from general principles.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> Options B and C differ only in TM2's start position (50 vs 54). Residues 50-51 (Asn, Glu) are hydrophilic and atypical for a TM helix interior, giving a hydrophobicity-based argument for option C. Conversely, GPCR TM helices can include polar residues at their loop-adjacent ends, and the annotation supports B. The 4-residue boundary falls within the typical uncertainty of any TM prediction method, making both B and C defensible without access to the specific database annotation.


### Important caveats

- All seven TM annotations are ECO:0000250 (similarity transfer from A0A6I8PUB9), not experimental evidence for this specific ghost shark GPR4.
- The reviewer-only UniProt evidence confirms the sequence match and annotation but was not available to the evaluated model.
- The B-vs-C distinction (TM2 start at 50 vs 54) is within the typical ±5-residue uncertainty of computational TM prediction tools.
- Option A (missing TM1) and D (single short C-terminal segment) are clearly eliminable by general GPCR knowledge, but the question's discriminating difficulty lies entirely in the B-vs-C boundary.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Recognizing the protein as a 7-TM GPCR eliminates option D (single 21-residue segment) and option A (only 6 TM segments). However, distinguishing B from C requires resolving whether TM2 begins at position 50 (N-E-L-G) or 54 (V-Y-L-L). Positions 50-51 are Asn and Glu—clearly hydrophilic/charged residues atypical of a TM helix core—while position 54 onward (VYLLNLSISDLLYIATLPPWVNYFLHQ) is substantially more hydrophobic. A pure hydrophobicity analysis would arguably favor option C (TM2 starting at 54). The specific 4-residue boundary at TM2's N-terminus cannot be reliably resolved by general biological reasoning.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact TM2 start position (50 vs 54) for this particular GPR4 ortholog, as determined by the similarity-transfer annotation from A0A6I8PUB9. No experimental structure or mutagenesis data for this specific boundary is provided.",
    "reason": "While the 7-TM GPCR topology narrows choices to B or C, the critical distinction (TM2 start at 50 vs 54) is a 4-residue boundary difference. Hydrophobicity analysis of residues 50-53 (N, E, L, G) actually slightly disfavors their inclusion in a TM helix, making C arguably more defensible by sequence reasoning. Resolving B over C depends on the specific database annotation boundary, which is an item-specific external fact not derivable from general principles."
  },
  "case_id": "transmembrane_0021",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C8",
      "C10",
      "C12",
      "C14",
      "C16",
      "C18",
      "H4",
      "H6",
      "H8",
      "H10",
      "H12",
      "H14",
      "H16"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for A0A4W3GG95 (GPR4_CALMI, ghost shark GPCR) lists exactly seven transmembrane helices at 9..45, 50..80, 86..121, 130..156, 173..210, 215..250, and 261..289, matching option B precisely. The sequence in the question matches the UniProt entry (SHA-256 confirmed). However, all TM annotations carry evidence code ECO:0000250 (similarity transfer from A0A6I8PUB9), indicating computational inference rather than direct experimental determination for this specific protein."
  },
  "important_caveats": [
    "All seven TM annotations are ECO:0000250 (similarity transfer from A0A6I8PUB9), not experimental evidence for this specific ghost shark GPR4.",
    "The reviewer-only UniProt evidence confirms the sequence match and annotation but was not available to the evaluated model.",
    "The B-vs-C distinction (TM2 start at 50 vs 54) is within the typical ±5-residue uncertainty of computational TM prediction tools.",
    "Option A (missing TM1) and D (single short C-terminal segment) are clearly eliminable by general GPCR knowledge, but the question's discriminating difficulty lies entirely in the B-vs-C boundary."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "Options B and C differ only in TM2's start position (50 vs 54). Residues 50-51 (Asn, Glu) are hydrophilic and atypical for a TM helix interior, giving a hydrophobicity-based argument for option C. Conversely, GPCR TM helices can include polar residues at their loop-adjacent ends, and the annotation supports B. The 4-residue boundary falls within the typical uncertainty of any TM prediction method, making both B and C defensible without access to the specific database annotation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0021",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for A0A4W3GG95 (GPR4_CALMI, ghost shark GPCR) lists exactly seven transmembrane helices at 9..45, 50..80, 86..121, 130..156, 173..210, 215..250, and 261..289, matching option B precisely. The sequence in the question matches the UniProt entry (SHA-256 confirmed). However, all TM annotations carry evidence code ECO:0000250 (similarity transfer from A0A6I8PUB9), indicating computational inference rather than direct experimental determination for this specific protein.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "H4", "H6", "H8", "H10", "H12", "H14", "H16"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Recognizing the protein as a 7-TM GPCR eliminates option D (single 21-residue segment) and option A (only 6 TM segments). However, distinguishing B from C requires resolving whether TM2 begins at position 50 (N-E-L-G) or 54 (V-Y-L-L). Positions 50-51 are Asn and Glu—clearly hydrophilic/charged residues atypical of a TM helix core—while position 54 onward (VYLLNLSISDLLYIATLPPWVNYFLHQ) is substantially more hydrophobic. A pure hydrophobicity analysis would arguably favor option C (TM2 starting at 54). The specific 4-residue boundary at TM2's N-terminus cannot be reliably resolved by general biological reasoning.",
    "missing_item_specific_fact": "The exact TM2 start position (50 vs 54) for this particular GPR4 ortholog, as determined by the similarity-transfer annotation from A0A6I8PUB9. No experimental structure or mutagenesis data for this specific boundary is provided.",
    "reason": "While the 7-TM GPCR topology narrows choices to B or C, the critical distinction (TM2 start at 50 vs 54) is a 4-residue boundary difference. Hydrophobicity analysis of residues 50-53 (N, E, L, G) actually slightly disfavors their inclusion in a TM helix, making C arguably more defensible by sequence reasoning. Resolving B over C depends on the specific database annotation boundary, which is an item-specific external fact not derivable from general principles."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "Options B and C differ only in TM2's start position (50 vs 54). Residues 50-51 (Asn, Glu) are hydrophilic and atypical for a TM helix interior, giving a hydrophobicity-based argument for option C. Conversely, GPCR TM helices can include polar residues at their loop-adjacent ends, and the annotation supports B. The 4-residue boundary falls within the typical uncertainty of any TM prediction method, making both B and C defensible without access to the specific database annotation."
  },
  "important_caveats": [
    "All seven TM annotations are ECO:0000250 (similarity transfer from A0A6I8PUB9), not experimental evidence for this specific ghost shark GPR4.",
    "The reviewer-only UniProt evidence confirms the sequence match and annotation but was not available to the evaluated model.",
    "The B-vs-C distinction (TM2 start at 50 vs 54) is within the typical ±5-residue uncertainty of computational TM prediction tools.",
    "Option A (missing TM1) and D (single short C-terminal segment) are clearly eliminable by general GPCR knowledge, but the question's discriminating difficulty lies entirely in the B-vs-C boundary."
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

**Accession:** `A0A4W3GG95` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 30. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:47.202623+00:00.  

```json
{"description":"Helical; Name=1","evidences":[{"evidenceCode":"ECO:0000250","id":"A0A6I8PUB9","source":"UniProtKB"}],"location":{"end":{"modifier":"EXACT","value":45},"start":{"modifier":"EXACT","value":9}},"type":"Transmembrane"}
```

Source SHA-256: `a92b2a2611b3e831e67c290051c3b607ae4d71a21502ae38da2c507908426245`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:47.202623+00:00.  

```json
{"description":"Helical; Name=2","evidences":[{"evidenceCode":"ECO:0000250","id":"A0A6I8PUB9","source":"UniProtKB"}],"location":{"end":{"modifier":"EXACT","value":80},"start":{"modifier":"EXACT","value":50}},"type":"Transmembrane"}
```

Source SHA-256: `a92b2a2611b3e831e67c290051c3b607ae4d71a21502ae38da2c507908426245`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:47.202623+00:00.  

```json
{"description":"Helical; Name=3","evidences":[{"evidenceCode":"ECO:0000250","id":"A0A6I8PUB9","source":"UniProtKB"}],"location":{"end":{"modifier":"EXACT","value":121},"start":{"modifier":"EXACT","value":86}},"type":"Transmembrane"}
```

Source SHA-256: `a92b2a2611b3e831e67c290051c3b607ae4d71a21502ae38da2c507908426245`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json)  
**Locator:** `/features/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:47.202623+00:00.  

```json
{"description":"Helical; Name=4","evidences":[{"evidenceCode":"ECO:0000250","id":"A0A6I8PUB9","source":"UniProtKB"}],"location":{"end":{"modifier":"EXACT","value":156},"start":{"modifier":"EXACT","value":130}},"type":"Transmembrane"}
```

Source SHA-256: `a92b2a2611b3e831e67c290051c3b607ae4d71a21502ae38da2c507908426245`.

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json)  
**Locator:** `/features/10`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:47.202623+00:00.  

```json
{"description":"Helical; Name=5","evidences":[{"evidenceCode":"ECO:0000250","id":"A0A6I8PUB9","source":"UniProtKB"}],"location":{"end":{"modifier":"EXACT","value":210},"start":{"modifier":"EXACT","value":173}},"type":"Transmembrane"}
```

Source SHA-256: `a92b2a2611b3e831e67c290051c3b607ae4d71a21502ae38da2c507908426245`.

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json)  
**Locator:** `/features/12`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:47.202623+00:00.  

```json
{"description":"Helical; Name=6","evidences":[{"evidenceCode":"ECO:0000250","id":"A0A6I8PUB9","source":"UniProtKB"}],"location":{"end":{"modifier":"EXACT","value":250},"start":{"modifier":"EXACT","value":215}},"type":"Transmembrane"}
```

Source SHA-256: `a92b2a2611b3e831e67c290051c3b607ae4d71a21502ae38da2c507908426245`.

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json)  
**Locator:** `/features/14`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:47.202623+00:00.  

```json
{"description":"Helical; Name=7","evidences":[{"evidenceCode":"ECO:0000250","id":"A0A6I8PUB9","source":"UniProtKB"}],"location":{"end":{"modifier":"EXACT","value":289},"start":{"modifier":"EXACT","value":261}},"type":"Transmembrane"}
```

Source SHA-256: `a92b2a2611b3e831e67c290051c3b607ae4d71a21502ae38da2c507908426245`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A4W3GG95?format=txt&versions=30)  
**Locator:** `lines 92-94`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 1.  
**Retrieved:** 2026-11-01T06:27:31.027017+00:00.  

```text
FT   TRANSMEM        9..45
FT                   /note="Helical; Name=1"
FT                   /evidence="ECO:0000250|UniProtKB:A0A6I8PUB9"
```

Source SHA-256: `2de235f5ecdbc32faad1779acf9f8307edf330e58265fd2df418707701078865`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A4W3GG95?format=txt&versions=30)  
**Locator:** `lines 98-100`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 1.  
**Retrieved:** 2026-11-01T06:27:31.027017+00:00.  

```text
FT   TRANSMEM        50..80
FT                   /note="Helical; Name=2"
FT                   /evidence="ECO:0000250|UniProtKB:A0A6I8PUB9"
```

Source SHA-256: `2de235f5ecdbc32faad1779acf9f8307edf330e58265fd2df418707701078865`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A4W3GG95?format=txt&versions=30)  
**Locator:** `lines 104-106`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 1.  
**Retrieved:** 2026-11-01T06:27:31.027017+00:00.  

```text
FT   TRANSMEM        86..121
FT                   /note="Helical; Name=3"
FT                   /evidence="ECO:0000250|UniProtKB:A0A6I8PUB9"
```

Source SHA-256: `2de235f5ecdbc32faad1779acf9f8307edf330e58265fd2df418707701078865`.

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A4W3GG95?format=txt&versions=30)  
**Locator:** `lines 110-112`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 1.  
**Retrieved:** 2026-11-01T06:27:31.027017+00:00.  

```text
FT   TRANSMEM        130..156
FT                   /note="Helical; Name=4"
FT                   /evidence="ECO:0000250|UniProtKB:A0A6I8PUB9"
```

Source SHA-256: `2de235f5ecdbc32faad1779acf9f8307edf330e58265fd2df418707701078865`.

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A4W3GG95?format=txt&versions=30)  
**Locator:** `lines 116-118`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 1.  
**Retrieved:** 2026-11-01T06:27:31.027017+00:00.  

```text
FT   TRANSMEM        173..210
FT                   /note="Helical; Name=5"
FT                   /evidence="ECO:0000250|UniProtKB:A0A6I8PUB9"
```

Source SHA-256: `2de235f5ecdbc32faad1779acf9f8307edf330e58265fd2df418707701078865`.

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A4W3GG95?format=txt&versions=30)  
**Locator:** `lines 122-124`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 1.  
**Retrieved:** 2026-11-01T06:27:31.027017+00:00.  

```text
FT   TRANSMEM        215..250
FT                   /note="Helical; Name=6"
FT                   /evidence="ECO:0000250|UniProtKB:A0A6I8PUB9"
```

Source SHA-256: `2de235f5ecdbc32faad1779acf9f8307edf330e58265fd2df418707701078865`.

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A4W3GG95?format=txt&versions=30)  
**Locator:** `lines 128-130`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 1.  
**Retrieved:** 2026-11-01T06:27:31.027017+00:00.  

```text
FT   TRANSMEM        261..289
FT                   /note="Helical; Name=7"
FT                   /evidence="ECO:0000250|UniProtKB:A0A6I8PUB9"
```

Source SHA-256: `2de235f5ecdbc32faad1779acf9f8307edf330e58265fd2df418707701078865`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 21. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
