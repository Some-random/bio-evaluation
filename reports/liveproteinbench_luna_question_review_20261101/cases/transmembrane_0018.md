# transmembrane_0018

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **B** — 27..47; 67..87; 100..120; 144..164; 202..222; 241..261; 274..294

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

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

## Luna’s full visible review

### Expected-answer support: supported

> The sequence-matched UniProt record annotates seven transmembrane helices at exactly the coordinates in B. These annotations use evidence code ECO:0000255, so they support the key as database annotation, not as independently established experimental measurements.

Cited evidence: [H3](#evidence-h3), [H5](#evidence-h5), [H7](#evidence-h7), [H9](#evidence-h9), [H11](#evidence-h11), [H13](#evidence-h13), [H15](#evidence-h15).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is strongly hydrophobic in multiple regions and is consistent with a multi-pass, likely seven-helix membrane protein, which supports the broad topology but not exact residue boundaries.

**Missing item-specific fact**

> The protein-specific transmembrane boundary annotations, especially the precise ends of the sixth and seventh helices, are absent from the input.

**Reason**

> Choosing exact coordinates requires an annotation or protein-specific prediction. Hydropathy can help identify likely helices, but does not uniquely establish the listed residue endpoints.

### Question ambiguity

**Multiple defensible options named by Luna:** B, C.

> B matches the database boundaries. C differs only by extending the sixth segment four residues, and membrane-helix boundaries can be approximate; the sequence and wording alone do not establish a uniquely exact physical endpoint.

### Important caveats

- Reviewer-only database evidence establishes support for the key but was not supplied to the evaluated model.
- The matching database helix annotations are computationally evidenced; they should not be described as experimental measurements.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "transmembrane_0018",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates seven transmembrane helices at exactly the coordinates in B. These annotations use evidence code ECO:0000255, so they support the key as database annotation, not as independently established experimental measurements.",
    "evidence_ids": [
      "H3",
      "H5",
      "H7",
      "H9",
      "H11",
      "H13",
      "H15"
    ]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is strongly hydrophobic in multiple regions and is consistent with a multi-pass, likely seven-helix membrane protein, which supports the broad topology but not exact residue boundaries.",
    "missing_item_specific_fact": "The protein-specific transmembrane boundary annotations, especially the precise ends of the sixth and seventh helices, are absent from the input.",
    "reason": "Choosing exact coordinates requires an annotation or protein-specific prediction. Hydropathy can help identify likely helices, but does not uniquely establish the listed residue endpoints."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "B matches the database boundaries. C differs only by extending the sixth segment four residues, and membrane-helix boundaries can be approximate; the sequence and wording alone do not establish a uniquely exact physical endpoint."
  },
  "important_caveats": [
    "Reviewer-only database evidence establishes support for the key but was not supplied to the evaluated model.",
    "The matching database helix annotations are computationally evidenced; they should not be described as experimental measurements."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `A0A3B3IT45`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 33. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

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

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json) (zero-based source row 18). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
