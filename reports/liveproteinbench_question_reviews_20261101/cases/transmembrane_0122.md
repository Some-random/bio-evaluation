# transmembrane_0122

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **D** — 29..49; 60..80; 117..137; 158..178; 179..199

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSIIGSFPPGGPRVEVQETRVQTDRVLTIPNILSMARLAGVPLFLWLILRPEFGGPQSDGWALLVLALSGVSDYLDGKLARRWNQISSLGRLLDPAADRLYILSTLVGLTWREILPLWLTLVLLAREAMLLVMVGILRRHGYPPPQVNFLGKAATFNLMYAFPLLLLSDGSGWIASLAAVFGWAFAGWGTTLYWWAGVLYVVQVRRLVRADVAAD

[Multiple Choices]
A. 179..199; 357..377
B. 29..49; 60..80; 158..178; 179..199
C. 29..49; 62..77; 117..137; 158..178; 179..199
D. 29..49; 60..80; 117..137; 158..178; 179..199
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

> The sequence-matched UniProt annotation lists all five regions in choice D, both in the current entry and in a historical entry available by the stated cutoff. These are computational helical annotations (ECO:0000255), not evidence of experimental confirmation.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains hydrophobic stretches that make membrane-spanning helices plausible, but this does not reliably establish the complete set of regions or the specific boundaries needed to distinguish the options.


**Missing item-specific fact**

> The protein-specific predicted transmembrane annotation giving the five listed coordinates, especially the disputed 60..80 region and its boundaries.


**Reason**

> Choosing D requires protein-specific region assignments absent from the input. General hydropathy can motivate predictions but does not resolve these particular competing coordinates.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports D’s annotation. The sequence alone leaves uncertainty about some candidate regions and boundaries, but that uncertainty does not establish another option as equally supported.


### Important caveats

- The cited transmembrane features are computational annotations, not reported experimental measurements.
- The historical record has a sequence match, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hydrophobic stretches that make membrane-spanning helices plausible, but this does not reliably establish the complete set of regions or the specific boundaries needed to distinguish the options.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific predicted transmembrane annotation giving the five listed coordinates, especially the disputed 60..80 region and its boundaries.",
    "reason": "Choosing D requires protein-specific region assignments absent from the input. General hydropathy can motivate predictions but does not resolve these particular competing coordinates."
  },
  "case_id": "transmembrane_0122",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation lists all five regions in choice D, both in the current entry and in a historical entry available by the stated cutoff. These are computational helical annotations (ECO:0000255), not evidence of experimental confirmation."
  },
  "important_caveats": [
    "The cited transmembrane features are computational annotations, not reported experimental measurements.",
    "The historical record has a sequence match, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports D’s annotation. The sequence alone leaves uncertainty about some candidate regions and boundaries, but that uncertainty does not establish another option as equally supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0122",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation lists all five regions in choice D, both in the current entry and in a historical entry available by the stated cutoff. These are computational helical annotations (ECO:0000255), not evidence of experimental confirmation.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "H4", "H5", "H6", "H7", "H8"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains hydrophobic stretches that make membrane-spanning helices plausible, but this does not reliably establish the complete set of regions or the specific boundaries needed to distinguish the options.",
    "missing_item_specific_fact": "The protein-specific predicted transmembrane annotation giving the five listed coordinates, especially the disputed 60..80 region and its boundaries.",
    "reason": "Choosing D requires protein-specific region assignments absent from the input. General hydropathy can motivate predictions but does not resolve these particular competing coordinates."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports D’s annotation. The sequence alone leaves uncertainty about some candidate regions and boundaries, but that uncertainty does not establish another option as equally supported."
  },
  "important_caveats": [
    "The cited transmembrane features are computational annotations, not reported experimental measurements.",
    "The historical record has a sequence match, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q9KZP3 (Cardiolipin synthase, CRLS1_STRCO, 215 AA) annotates exactly five transmembrane helical regions: 29..49, 60..80, 117..137, 158..178, and 179..199, matching option D precisely. The annotation uses evidence code ECO:0000255 (similarity/computational prediction), not experimental determination, but the sequence match is confirmed and the annotation is consistent across current (v120) and historical (v118) snapshots.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Option A is eliminated by arithmetic (position 357 exceeds the 215-residue protein). Option B omits the 117..137 segment (LWLTLVLLAREAMLLVMVGIL), which is a strongly hydrophobic stretch that any hydrophobicity-window scan would flag as a TM helix, so its absence is detectable by general reasoning. The C-vs-D distinction (62..77 vs 60..80) is fine-grained but addressable: a 16-residue segment (62-77) is below the ~20-residue minimum typically required for a TM α-helix to span the lipid bilayer, whereas 60-80 (21 residues) meets that threshold. Additionally, Trp at position 61 is a canonical aromatic interfacial TM anchor residue, supporting its inclusion in the helix boundary. These general biophysical principles provide a defensible argument for D over C.


**Missing item-specific fact**

> The exact boundary (60 vs 62, 80 vs 77) is somewhat algorithm-dependent; the UniProt annotation is a computational prediction (ECO:0000255) rather than an experimentally determined boundary. However, the length and W-anchor arguments provide reasonable biological grounds without needing to memorize this specific entry.


**Reason**

> Three of four options can be eliminated or disfavored through general biological reasoning: A by out-of-range positions, B by missing an obviously hydrophobic TM segment, and C by insufficient helix length for membrane spanning. The C-vs-D boundary is fine-grained but the ~20-residue TM helix requirement and the interfacial Trp provide a concrete, general-knowledge-based argument favoring D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> The 62..77 vs 60..80 boundary is a fine-grained distinction. The 62-77 segment (16 residues) is borderline short for a TM helix but contains a hydrophobic core; the 60-80 segment adds G(60), W(61) at the N-terminus and K(78), L(79), A(80) at the C-terminus, introducing a charged Lys. A strict hydrophobicity scan might truncate the helix at 77 to exclude K(78). However, the length argument and Trp anchoring provide a reasonable basis to prefer D, making C a defensible-but-weak distractor rather than a truly equivalent alternative.


### Important caveats

- All five TM annotations carry evidence code ECO:0000255 (predicted by similarity/protein analysis), not experimental structural or spectroscopic evidence. The exact boundaries are computational predictions.
- The UniProt entry was first public in 2025-02-05; the author's source snapshot is unknown but the sequence and annotation are stable (sequence version 1 since 2000).
- The reviewer-only accession Q9KZP3 was inferred from dataset metadata and was not provided to the evaluated model; the model must work from the raw sequence alone.
- Option A (357..377) is trivially eliminable and serves as a low-effort distractor.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Option A is eliminated by arithmetic (position 357 exceeds the 215-residue protein). Option B omits the 117..137 segment (LWLTLVLLAREAMLLVMVGIL), which is a strongly hydrophobic stretch that any hydrophobicity-window scan would flag as a TM helix, so its absence is detectable by general reasoning. The C-vs-D distinction (62..77 vs 60..80) is fine-grained but addressable: a 16-residue segment (62-77) is below the ~20-residue minimum typically required for a TM α-helix to span the lipid bilayer, whereas 60-80 (21 residues) meets that threshold. Additionally, Trp at position 61 is a canonical aromatic interfacial TM anchor residue, supporting its inclusion in the helix boundary. These general biophysical principles provide a defensible argument for D over C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact boundary (60 vs 62, 80 vs 77) is somewhat algorithm-dependent; the UniProt annotation is a computational prediction (ECO:0000255) rather than an experimentally determined boundary. However, the length and W-anchor arguments provide reasonable biological grounds without needing to memorize this specific entry.",
    "reason": "Three of four options can be eliminated or disfavored through general biological reasoning: A by out-of-range positions, B by missing an obviously hydrophobic TM segment, and C by insufficient helix length for membrane spanning. The C-vs-D boundary is fine-grained but the ~20-residue TM helix requirement and the interfacial Trp provide a concrete, general-knowledge-based argument favoring D."
  },
  "case_id": "transmembrane_0122",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q9KZP3 (Cardiolipin synthase, CRLS1_STRCO, 215 AA) annotates exactly five transmembrane helical regions: 29..49, 60..80, 117..137, 158..178, and 179..199, matching option D precisely. The annotation uses evidence code ECO:0000255 (similarity/computational prediction), not experimental determination, but the sequence match is confirmed and the annotation is consistent across current (v120) and historical (v118) snapshots."
  },
  "important_caveats": [
    "All five TM annotations carry evidence code ECO:0000255 (predicted by similarity/protein analysis), not experimental structural or spectroscopic evidence. The exact boundaries are computational predictions.",
    "The UniProt entry was first public in 2025-02-05; the author's source snapshot is unknown but the sequence and annotation are stable (sequence version 1 since 2000).",
    "The reviewer-only accession Q9KZP3 was inferred from dataset metadata and was not provided to the evaluated model; the model must work from the raw sequence alone.",
    "Option A (357..377) is trivially eliminable and serves as a low-effort distractor."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "The 62..77 vs 60..80 boundary is a fine-grained distinction. The 62-77 segment (16 residues) is borderline short for a TM helix but contains a hydrophobic core; the 60-80 segment adds G(60), W(61) at the N-terminus and K(78), L(79), A(80) at the C-terminus, introducing a charged Lys. A strict hydrophobicity scan might truncate the helix at 77 to exclude K(78). However, the length argument and Trp anchoring provide a reasonable basis to prefer D, making C a defensible-but-weak distractor rather than a truly equivalent alternative."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0122",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q9KZP3 (Cardiolipin synthase, CRLS1_STRCO, 215 AA) annotates exactly five transmembrane helical regions: 29..49, 60..80, 117..137, 158..178, and 179..199, matching option D precisely. The annotation uses evidence code ECO:0000255 (similarity/computational prediction), not experimental determination, but the sequence match is confirmed and the annotation is consistent across current (v120) and historical (v118) snapshots.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "H4", "H5", "H6", "H7", "H8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Option A is eliminated by arithmetic (position 357 exceeds the 215-residue protein). Option B omits the 117..137 segment (LWLTLVLLAREAMLLVMVGIL), which is a strongly hydrophobic stretch that any hydrophobicity-window scan would flag as a TM helix, so its absence is detectable by general reasoning. The C-vs-D distinction (62..77 vs 60..80) is fine-grained but addressable: a 16-residue segment (62-77) is below the ~20-residue minimum typically required for a TM α-helix to span the lipid bilayer, whereas 60-80 (21 residues) meets that threshold. Additionally, Trp at position 61 is a canonical aromatic interfacial TM anchor residue, supporting its inclusion in the helix boundary. These general biophysical principles provide a defensible argument for D over C.",
    "missing_item_specific_fact": "The exact boundary (60 vs 62, 80 vs 77) is somewhat algorithm-dependent; the UniProt annotation is a computational prediction (ECO:0000255) rather than an experimentally determined boundary. However, the length and W-anchor arguments provide reasonable biological grounds without needing to memorize this specific entry.",
    "reason": "Three of four options can be eliminated or disfavored through general biological reasoning: A by out-of-range positions, B by missing an obviously hydrophobic TM segment, and C by insufficient helix length for membrane spanning. The C-vs-D boundary is fine-grained but the ~20-residue TM helix requirement and the interfacial Trp provide a concrete, general-knowledge-based argument favoring D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "The 62..77 vs 60..80 boundary is a fine-grained distinction. The 62-77 segment (16 residues) is borderline short for a TM helix but contains a hydrophobic core; the 60-80 segment adds G(60), W(61) at the N-terminus and K(78), L(79), A(80) at the C-terminus, introducing a charged Lys. A strict hydrophobicity scan might truncate the helix at 77 to exclude K(78). However, the length argument and Trp anchoring provide a reasonable basis to prefer D, making C a defensible-but-weak distractor rather than a truly equivalent alternative."
  },
  "important_caveats": [
    "All five TM annotations carry evidence code ECO:0000255 (predicted by similarity/protein analysis), not experimental structural or spectroscopic evidence. The exact boundaries are computational predictions.",
    "The UniProt entry was first public in 2025-02-05; the author's source snapshot is unknown but the sequence and annotation are stable (sequence version 1 since 2000).",
    "The reviewer-only accession Q9KZP3 was inferred from dataset metadata and was not provided to the evaluated model; the model must work from the raw sequence alone.",
    "Option A (357..377) is trivially eliminable and serves as a low-effort distractor."
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

**Accession:** `Q9KZP3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 118. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KZP3.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:27.611577+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":49},"start":{"modifier":"EXACT","value":29}},"type":"Transmembrane"}
```

Source SHA-256: `19159a513ac84423a492087d8961c46891339eef5cec5a9d995ec98e1cfe717c`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KZP3.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:27.611577+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":80},"start":{"modifier":"EXACT","value":60}},"type":"Transmembrane"}
```

Source SHA-256: `19159a513ac84423a492087d8961c46891339eef5cec5a9d995ec98e1cfe717c`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KZP3.json)  
**Locator:** `/features/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:27.611577+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":137},"start":{"modifier":"EXACT","value":117}},"type":"Transmembrane"}
```

Source SHA-256: `19159a513ac84423a492087d8961c46891339eef5cec5a9d995ec98e1cfe717c`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KZP3.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:27.611577+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":178},"start":{"modifier":"EXACT","value":158}},"type":"Transmembrane"}
```

Source SHA-256: `19159a513ac84423a492087d8961c46891339eef5cec5a9d995ec98e1cfe717c`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KZP3.json)  
**Locator:** `/features/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:27.611577+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":199},"start":{"modifier":"EXACT","value":179}},"type":"Transmembrane"}
```

Source SHA-256: `19159a513ac84423a492087d8961c46891339eef5cec5a9d995ec98e1cfe717c`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118)  
**Locator:** `lines 118-120`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 118 / 1.  
**Retrieved:** 2026-11-01T06:28:47.509754+00:00.  

```text
FT   TRANSMEM        29..49
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `40068827609c34109c814e2d2c856e36a3bec9b7c2775a90bbcc5f7a21726d79`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118)  
**Locator:** `lines 121-123`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 118 / 1.  
**Retrieved:** 2026-11-01T06:28:47.509754+00:00.  

```text
FT   TRANSMEM        60..80
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `40068827609c34109c814e2d2c856e36a3bec9b7c2775a90bbcc5f7a21726d79`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118)  
**Locator:** `lines 124-126`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 118 / 1.  
**Retrieved:** 2026-11-01T06:28:47.509754+00:00.  

```text
FT   TRANSMEM        117..137
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `40068827609c34109c814e2d2c856e36a3bec9b7c2775a90bbcc5f7a21726d79`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118)  
**Locator:** `lines 127-129`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 118 / 1.  
**Retrieved:** 2026-11-01T06:28:47.509754+00:00.  

```text
FT   TRANSMEM        158..178
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `40068827609c34109c814e2d2c856e36a3bec9b7c2775a90bbcc5f7a21726d79`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118)  
**Locator:** `lines 130-132`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 118 / 1.  
**Retrieved:** 2026-11-01T06:28:47.509754+00:00.  

```text
FT   TRANSMEM        179..199
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `40068827609c34109c814e2d2c856e36a3bec9b7c2775a90bbcc5f7a21726d79`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 122. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
