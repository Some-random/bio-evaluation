# transmembrane_0018

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **B** — 27..47; 67..87; 100..120; 144..164; 202..222; 241..261; 274..294

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MGSNITSTSIIFLLTGVPGLEAFHTWISIPFCFLSVTALLGNSLILFATITQPSLHEPMYYFLSMLSATDLGLSISTLVTMLSIFWFNVREISFNACLSHMFFIKFFTVMESSVLLAMAFDRFVAVSNPLRYAMILTDSRIAQIGVASVIRGLLMLTPMVALLIRLSYCHSQVLHHSYCYHPDVMKLSCTDTRINSAVGLTAMFSTVGVDLLLILLSYVLIIRTVLSVASPEERKETFSTCVSHIVAFAIYYIPLISLSIVHRFGKQAPAYVHTMIANTYLLISPLMNPVIYSVKTKQIRRAVIKILHSKET

[Multiple Choices]
A. 27..47; 67..87; 100..120; 144..164; 202..222; 241..261
B. 27..47; 67..87; 100..120; 144..164; 202..222; 241..261; 274..294
C. 27..47; 67..87; 100..120; 144..164; 202..222; 241..265; 274..294
D. 9..29; 41..61; 84..104; 118..138; 153..173; 175..195; 202..222; 231..251
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

> The sequence-matched UniProt record annotates seven transmembrane helices at exactly the coordinates in B. These annotations use evidence code ECO:0000255, so they support the key as database annotation, not as independently established experimental measurements.

Citations as saved: [H3](#evidence-h3), [H5](#evidence-h5), [H7](#evidence-h7), [H9](#evidence-h9), [H11](#evidence-h11), [H13](#evidence-h13), [H15](#evidence-h15).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is strongly hydrophobic in multiple regions and is consistent with a multi-pass, likely seven-helix membrane protein, which supports the broad topology but not exact residue boundaries.


**Missing item-specific fact**

> The protein-specific transmembrane boundary annotations, especially the precise ends of the sixth and seventh helices, are absent from the input.


**Reason**

> Choosing exact coordinates requires an annotation or protein-specific prediction. Hydropathy can help identify likely helices, but does not uniquely establish the listed residue endpoints.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> B matches the database boundaries. C differs only by extending the sixth segment four residues, and membrane-helix boundaries can be approximate; the sequence and wording alone do not establish a uniquely exact physical endpoint.


### Important caveats

- Reviewer-only database evidence establishes support for the key but was not supplied to the evaluated model.
- The matching database helix annotations are computationally evidenced; they should not be described as experimental measurements.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is strongly hydrophobic in multiple regions and is consistent with a multi-pass, likely seven-helix membrane protein, which supports the broad topology but not exact residue boundaries.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific transmembrane boundary annotations, especially the precise ends of the sixth and seventh helices, are absent from the input.",
    "reason": "Choosing exact coordinates requires an annotation or protein-specific prediction. Hydropathy can help identify likely helices, but does not uniquely establish the listed residue endpoints."
  },
  "case_id": "transmembrane_0018",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H5",
      "H7",
      "H9",
      "H11",
      "H13",
      "H15"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates seven transmembrane helices at exactly the coordinates in B. These annotations use evidence code ECO:0000255, so they support the key as database annotation, not as independently established experimental measurements."
  },
  "important_caveats": [
    "Reviewer-only database evidence establishes support for the key but was not supplied to the evaluated model.",
    "The matching database helix annotations are computationally evidenced; they should not be described as experimental measurements."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "B matches the database boundaries. C differs only by extending the sixth segment four residues, and membrane-helix boundaries can be approximate; the sequence and wording alone do not establish a uniquely exact physical endpoint."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0018",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates seven transmembrane helices at exactly the coordinates in B. These annotations use evidence code ECO:0000255, so they support the key as database annotation, not as independently established experimental measurements.",
    "evidence_ids": ["H3", "H5", "H7", "H9", "H11", "H13", "H15"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is strongly hydrophobic in multiple regions and is consistent with a multi-pass, likely seven-helix membrane protein, which supports the broad topology but not exact residue boundaries.",
    "missing_item_specific_fact": "The protein-specific transmembrane boundary annotations, especially the precise ends of the sixth and seventh helices, are absent from the input.",
    "reason": "Choosing exact coordinates requires an annotation or protein-specific prediction. Hydropathy can help identify likely helices, but does not uniquely establish the listed residue endpoints."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "B matches the database boundaries. C differs only by extending the sixth segment four residues, and membrane-helix boundaries can be approximate; the sequence and wording alone do not establish a uniquely exact physical endpoint."
  },
  "important_caveats": [
    "Reviewer-only database evidence establishes support for the key but was not supplied to the evaluated model.",
    "The matching database helix annotations are computationally evidenced; they should not be described as experimental measurements."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> Option B (27..47; 67..87; 100..120; 144..164; 202..222; 241..261; 274..294) matches exactly the seven transmembrane helix annotations in UniProt entry A0A3B3IT45 (OR51C1_HUMAN), confirmed in both the current entry (v35) and the historical archived entry (v33). The evidence code ECO:0000255 (by similarity) indicates these are computational predictions transferred by homology rather than experimentally determined boundaries, but the annotation is internally consistent and the sequence match is exact (SHA-256 confirmed).

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [H3](#evidence-h3), [H5](#evidence-h5), [H7](#evidence-h7), [H9](#evidence-h9), [H11](#evidence-h11), [H13](#evidence-h13), [H15](#evidence-h15).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> General knowledge that olfactory receptors are 7-transmembrane GPCRs meaningfully eliminates Option A (only 6 TMs) and Option D (8 TMs with entirely different boundaries). This is a legitimate reasoning step. However, the critical distinction between Option B (TM6: 241..261) and Option C (TM6: 241..265) is a 4-residue boundary difference within a single helix, which falls within the normal uncertainty range of hydrophobicity-based TM prediction and cannot be reliably resolved from the sequence alone without knowing the specific annotation.


**Missing item-specific fact**

> The exact C-terminal boundary of TM6 (residue 261 vs. 265) as recorded in the UniProt annotation. Both boundaries are plausible hydrophobic stretches; the UniProt annotation uses ECO:0000255 (by similarity), meaning this is a transferred computational prediction rather than an experimentally determined endpoint. Distinguishing 261 from 265 requires knowledge of which specific prediction method or homology template was used.


**Reason**

> While the 7-TM GPCR topology of olfactory receptors is general biological knowledge that eliminates A and D, the final B-vs-C distinction hinges on a 4-residue boundary in TM6 that is within the noise of TM prediction. A hydrophobicity scan of the supplied sequence would not clearly favor one boundary over the other. Selecting B over C effectively requires knowing the exact UniProt annotation, making the question lookup-dependent at the decisive step.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> Options B and C differ only in the TM6 endpoint (261 vs. 265), a 4-residue difference well within the typical ±5-residue uncertainty of computational TM helix boundary prediction. Both represent reasonable hydrophobic segments. The annotation evidence code (ECO:0000255, by similarity) confirms these are transferred predictions, not experimental measurements, so neither boundary is uniquely 'correct' from first principles. A model performing its own hydrophobicity analysis could plausibly arrive at either endpoint.


### Important caveats

- All transmembrane annotations carry evidence code ECO:0000255 (predicted by similarity), not experimental evidence. The exact boundaries are computational predictions transferred from homologous proteins.
- The UniProt entry was first publicly released on 2025-02-05 (Swiss-Prot), so the annotation predates the benchmark construction but the author's exact source snapshot is unknown.
- The 7-TM GPCR topology of olfactory receptors is well-established general biology and provides a valid reasoning basis to eliminate Options A and D.
- The B-vs-C ambiguity (4 residues) is at the margin of what any prediction tool can reliably resolve; this does not make the question defective per se, but it weakens the reasoning-only path to the unique correct answer.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "General knowledge that olfactory receptors are 7-transmembrane GPCRs meaningfully eliminates Option A (only 6 TMs) and Option D (8 TMs with entirely different boundaries). This is a legitimate reasoning step. However, the critical distinction between Option B (TM6: 241..261) and Option C (TM6: 241..265) is a 4-residue boundary difference within a single helix, which falls within the normal uncertainty range of hydrophobicity-based TM prediction and cannot be reliably resolved from the sequence alone without knowing the specific annotation.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact C-terminal boundary of TM6 (residue 261 vs. 265) as recorded in the UniProt annotation. Both boundaries are plausible hydrophobic stretches; the UniProt annotation uses ECO:0000255 (by similarity), meaning this is a transferred computational prediction rather than an experimentally determined endpoint. Distinguishing 261 from 265 requires knowledge of which specific prediction method or homology template was used.",
    "reason": "While the 7-TM GPCR topology of olfactory receptors is general biological knowledge that eliminates A and D, the final B-vs-C distinction hinges on a 4-residue boundary in TM6 that is within the noise of TM prediction. A hydrophobicity scan of the supplied sequence would not clearly favor one boundary over the other. Selecting B over C effectively requires knowing the exact UniProt annotation, making the question lookup-dependent at the decisive step."
  },
  "case_id": "transmembrane_0018",
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
    "reason": "Option B (27..47; 67..87; 100..120; 144..164; 202..222; 241..261; 274..294) matches exactly the seven transmembrane helix annotations in UniProt entry A0A3B3IT45 (OR51C1_HUMAN), confirmed in both the current entry (v35) and the historical archived entry (v33). The evidence code ECO:0000255 (by similarity) indicates these are computational predictions transferred by homology rather than experimentally determined boundaries, but the annotation is internally consistent and the sequence match is exact (SHA-256 confirmed)."
  },
  "important_caveats": [
    "All transmembrane annotations carry evidence code ECO:0000255 (predicted by similarity), not experimental evidence. The exact boundaries are computational predictions transferred from homologous proteins.",
    "The UniProt entry was first publicly released on 2025-02-05 (Swiss-Prot), so the annotation predates the benchmark construction but the author's exact source snapshot is unknown.",
    "The 7-TM GPCR topology of olfactory receptors is well-established general biology and provides a valid reasoning basis to eliminate Options A and D.",
    "The B-vs-C ambiguity (4 residues) is at the margin of what any prediction tool can reliably resolve; this does not make the question defective per se, but it weakens the reasoning-only path to the unique correct answer."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "Options B and C differ only in the TM6 endpoint (261 vs. 265), a 4-residue difference well within the typical ±5-residue uncertainty of computational TM helix boundary prediction. Both represent reasonable hydrophobic segments. The annotation evidence code (ECO:0000255, by similarity) confirms these are transferred predictions, not experimental measurements, so neither boundary is uniquely 'correct' from first principles. A model performing its own hydrophobicity analysis could plausibly arrive at either endpoint."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0018",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "Option B (27..47; 67..87; 100..120; 144..164; 202..222; 241..261; 274..294) matches exactly the seven transmembrane helix annotations in UniProt entry A0A3B3IT45 (OR51C1_HUMAN), confirmed in both the current entry (v35) and the historical archived entry (v33). The evidence code ECO:0000255 (by similarity) indicates these are computational predictions transferred by homology rather than experimentally determined boundaries, but the annotation is internally consistent and the sequence match is exact (SHA-256 confirmed).",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "H3", "H5", "H7", "H9", "H11", "H13", "H15"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "General knowledge that olfactory receptors are 7-transmembrane GPCRs meaningfully eliminates Option A (only 6 TMs) and Option D (8 TMs with entirely different boundaries). This is a legitimate reasoning step. However, the critical distinction between Option B (TM6: 241..261) and Option C (TM6: 241..265) is a 4-residue boundary difference within a single helix, which falls within the normal uncertainty range of hydrophobicity-based TM prediction and cannot be reliably resolved from the sequence alone without knowing the specific annotation.",
    "missing_item_specific_fact": "The exact C-terminal boundary of TM6 (residue 261 vs. 265) as recorded in the UniProt annotation. Both boundaries are plausible hydrophobic stretches; the UniProt annotation uses ECO:0000255 (by similarity), meaning this is a transferred computational prediction rather than an experimentally determined endpoint. Distinguishing 261 from 265 requires knowledge of which specific prediction method or homology template was used.",
    "reason": "While the 7-TM GPCR topology of olfactory receptors is general biological knowledge that eliminates A and D, the final B-vs-C distinction hinges on a 4-residue boundary in TM6 that is within the noise of TM prediction. A hydrophobicity scan of the supplied sequence would not clearly favor one boundary over the other. Selecting B over C effectively requires knowing the exact UniProt annotation, making the question lookup-dependent at the decisive step."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "Options B and C differ only in the TM6 endpoint (261 vs. 265), a 4-residue difference well within the typical ±5-residue uncertainty of computational TM helix boundary prediction. Both represent reasonable hydrophobic segments. The annotation evidence code (ECO:0000255, by similarity) confirms these are transferred predictions, not experimental measurements, so neither boundary is uniquely 'correct' from first principles. A model performing its own hydrophobicity analysis could plausibly arrive at either endpoint."
  },
  "important_caveats": [
    "All transmembrane annotations carry evidence code ECO:0000255 (predicted by similarity), not experimental evidence. The exact boundaries are computational predictions transferred from homologous proteins.",
    "The UniProt entry was first publicly released on 2025-02-05 (Swiss-Prot), so the annotation predates the benchmark construction but the author's exact source snapshot is unknown.",
    "The 7-TM GPCR topology of olfactory receptors is well-established general biology and provides a valid reasoning basis to eliminate Options A and D.",
    "The B-vs-C ambiguity (4 residues) is at the margin of what any prediction tool can reliably resolve; this does not make the question defective per se, but it weakens the reasoning-only path to the unique correct answer."
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

**Accession:** `A0A3B3IT45` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 33. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:02.741232+00:00.  

```json
{"description":"Helical; Name=1","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":47},"start":{"modifier":"EXACT","value":27}},"type":"Transmembrane"}
```

Source SHA-256: `413edf0d30a632c4d35f0ee6c062c8bf9f27b4551b6e1a829cb403d5b8de10f5`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:02.741232+00:00.  

```json
{"description":"Helical; Name=2","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":87},"start":{"modifier":"EXACT","value":67}},"type":"Transmembrane"}
```

Source SHA-256: `413edf0d30a632c4d35f0ee6c062c8bf9f27b4551b6e1a829cb403d5b8de10f5`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:02.741232+00:00.  

```json
{"description":"Helical; Name=3","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":120},"start":{"modifier":"EXACT","value":100}},"type":"Transmembrane"}
```

Source SHA-256: `413edf0d30a632c4d35f0ee6c062c8bf9f27b4551b6e1a829cb403d5b8de10f5`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json)  
**Locator:** `/features/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:02.741232+00:00.  

```json
{"description":"Helical; Name=4","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":164},"start":{"modifier":"EXACT","value":144}},"type":"Transmembrane"}
```

Source SHA-256: `413edf0d30a632c4d35f0ee6c062c8bf9f27b4551b6e1a829cb403d5b8de10f5`.

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json)  
**Locator:** `/features/10`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:02.741232+00:00.  

```json
{"description":"Helical; Name=5","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":222},"start":{"modifier":"EXACT","value":202}},"type":"Transmembrane"}
```

Source SHA-256: `413edf0d30a632c4d35f0ee6c062c8bf9f27b4551b6e1a829cb403d5b8de10f5`.

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json)  
**Locator:** `/features/12`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:02.741232+00:00.  

```json
{"description":"Helical; Name=6","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":261},"start":{"modifier":"EXACT","value":241}},"type":"Transmembrane"}
```

Source SHA-256: `413edf0d30a632c4d35f0ee6c062c8bf9f27b4551b6e1a829cb403d5b8de10f5`.

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json)  
**Locator:** `/features/14`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:02.741232+00:00.  

```json
{"description":"Helical; Name=7","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":294},"start":{"modifier":"EXACT","value":274}},"type":"Transmembrane"}
```

Source SHA-256: `413edf0d30a632c4d35f0ee6c062c8bf9f27b4551b6e1a829cb403d5b8de10f5`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A3B3IT45?format=txt&versions=33)  
**Locator:** `lines 107-109`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 33 / 1.  
**Retrieved:** 2026-11-02T04:25:05.547773+00:00.  

```text
FT   TRANSMEM        27..47
FT                   /note="Helical; Name=1"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `baa83bf26c0bb6c7471ba5998d88f9308542ba6a5a9c7c12ad2235d34b22e1f3`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A3B3IT45?format=txt&versions=33)  
**Locator:** `lines 113-115`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 33 / 1.  
**Retrieved:** 2026-11-02T04:25:05.547773+00:00.  

```text
FT   TRANSMEM        67..87
FT                   /note="Helical; Name=2"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `baa83bf26c0bb6c7471ba5998d88f9308542ba6a5a9c7c12ad2235d34b22e1f3`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A3B3IT45?format=txt&versions=33)  
**Locator:** `lines 119-121`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 33 / 1.  
**Retrieved:** 2026-11-02T04:25:05.547773+00:00.  

```text
FT   TRANSMEM        100..120
FT                   /note="Helical; Name=3"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `baa83bf26c0bb6c7471ba5998d88f9308542ba6a5a9c7c12ad2235d34b22e1f3`.

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A3B3IT45?format=txt&versions=33)  
**Locator:** `lines 125-127`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 33 / 1.  
**Retrieved:** 2026-11-02T04:25:05.547773+00:00.  

```text
FT   TRANSMEM        144..164
FT                   /note="Helical; Name=4"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `baa83bf26c0bb6c7471ba5998d88f9308542ba6a5a9c7c12ad2235d34b22e1f3`.

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A3B3IT45?format=txt&versions=33)  
**Locator:** `lines 131-133`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 33 / 1.  
**Retrieved:** 2026-11-02T04:25:05.547773+00:00.  

```text
FT   TRANSMEM        202..222
FT                   /note="Helical; Name=5"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `baa83bf26c0bb6c7471ba5998d88f9308542ba6a5a9c7c12ad2235d34b22e1f3`.

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A3B3IT45?format=txt&versions=33)  
**Locator:** `lines 137-139`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 33 / 1.  
**Retrieved:** 2026-11-02T04:25:05.547773+00:00.  

```text
FT   TRANSMEM        241..261
FT                   /note="Helical; Name=6"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `baa83bf26c0bb6c7471ba5998d88f9308542ba6a5a9c7c12ad2235d34b22e1f3`.

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A3B3IT45?format=txt&versions=33)  
**Locator:** `lines 143-145`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 33 / 1.  
**Retrieved:** 2026-11-02T04:25:05.547773+00:00.  

```text
FT   TRANSMEM        274..294
FT                   /note="Helical; Name=7"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `baa83bf26c0bb6c7471ba5998d88f9308542ba6a5a9c7c12ad2235d34b22e1f3`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 18. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
