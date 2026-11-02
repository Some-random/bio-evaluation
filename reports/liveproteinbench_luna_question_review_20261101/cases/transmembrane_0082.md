# transmembrane_0082

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **A** — 14..34

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MAVYSYYPIDMVLLAHLIGIIYLIIILGTLVMLFS

[Multiple Choices]
A. 14..34
B. 14..34; 385..410
C. 16..34
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

## Luna’s full visible review

### Expected-answer support: supported

> The sequence-matched UniProt annotation gives a transmembrane helix at 14..34, supporting the key. Its ECO:0000255 evidence code indicates computational support, not experimental confirmation.

Cited evidence: [C5](#evidence-c5), [H2](#evidence-h2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has a strong hydrophobic stretch consistent with a membrane-spanning helix, which distinguishes the single-span choices from the implausible multi-span choices. But sequence composition alone does not reliably establish whether its exact N-terminal boundary is 14 or 16.

**Missing item-specific fact**

> The protein-specific transmembrane boundary annotation or prediction specifying 14..34 rather than 16..34.

**Reason**

> Identifying the general membrane-spanning region is biologically reasonable from the sequence, but choosing between the closely overlapping coordinates requires a protein-specific boundary call not supplied in the question.

### Question ambiguity

**Multiple defensible options named by Luna:** A, C.

> Both options describe the same strongly hydrophobic segment and differ only by two residues at its N-terminal boundary; the input does not give a rule or evidence that resolves that precise boundary.

### Important caveats

- The reviewer-only annotation applies to the exact supplied sequence, but it is computationally supported and should not be presented as experimental validation.
- The source snapshot used by the benchmark author is unknown.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "transmembrane_0082",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation gives a transmembrane helix at 14..34, supporting the key. Its ECO:0000255 evidence code indicates computational support, not experimental confirmation.",
    "evidence_ids": [
      "C5",
      "H2"
    ]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has a strong hydrophobic stretch consistent with a membrane-spanning helix, which distinguishes the single-span choices from the implausible multi-span choices. But sequence composition alone does not reliably establish whether its exact N-terminal boundary is 14 or 16.",
    "missing_item_specific_fact": "The protein-specific transmembrane boundary annotation or prediction specifying 14..34 rather than 16..34.",
    "reason": "Identifying the general membrane-spanning region is biologically reasonable from the sequence, but choosing between the closely overlapping coordinates requires a protein-specific boundary call not supplied in the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "Both options describe the same strongly hydrophobic segment and differ only by two residues at its N-terminal boundary; the input does not give a rule or evidence that resolves that precise boundary."
  },
  "important_caveats": [
    "The reviewer-only annotation applies to the exact supplied sequence, but it is computationally supported and should not be presented as experimental validation.",
    "The source snapshot used by the benchmark author is unknown."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `P9WEJ6`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 3. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEJ6.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:18.932651+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":34},"start":{"modifier":"EXACT","value":14}},"type":"Transmembrane"}
```

Source SHA-256: `93a966297fce68bace2aba191c1ce96de572405f36dcec82cd2e1abd71c74475`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEJ6?format=txt&versions=3)  
**Locator:** `lines 96-98`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-01T06:28:28.375865+00:00.  

```text
FT   TRANSMEM        14..34
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `2b9116a361e289851a454b5ec0e6b4749004d2d6afc18e6ac189e5457a8359fd`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json) (zero-based source row 82). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
