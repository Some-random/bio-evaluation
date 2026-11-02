# transmembrane_0030

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **D** — 8..28

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MDLLQRAGLVVGLWVTYHILLGTYNVFFHPLRRFPGPRLAAATQLVNVYYIIRGINCKYLYELHEKYGDVVRTGPNELSFRTASAIRTIYGGNPGPDDTFHKNMIANIQETGDSDNLFFATGQQHNRYRRLIMPVFAERTIQGQGPMMQEYCSQLIQGLRNRCGRGYFPTQDGVVDIVPWTHFIISDILSHMLFGSGMNCLLNGDYHPWVMAGYKALIESTYIEAAHRLRPYHRILEYLLIPTRLRDGFRVHSAVSREKLQARSKEAEPYQFSLPSFTSESLSEQELFDNINVIATAAGETTSSALSAIMYYLTANPAAYDKAVTEVRQAFSNEAEITAASSASLPYLKAVIREAFRIRPTIPVGLHRLTPKGGREIDGKWVPAGTWISVANLAACRTSSHWKEAGRFIPERWLGDPEFASDNRDTSVPYSIGVRNCIGMSHANTQLRLILSRLLWNFDFEACPGNADPYDYLEYGTWQVEPLKLRVVDIRGQPK

[Multiple Choices]
A. 8..28; 709..733
B. 5..30
C. 35..55
D. 8..28
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

> The sequence-matched UniProt records annotate residues 8–28 as a transmembrane helix. The annotation is computational (ECO:0000255), so it supports the expected database annotation but is not evidence of experimental confirmation.

Cited evidence: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminus has a strongly hydrophobic stretch around residues 8–28, making it much more plausible as a membrane-spanning helix than residues 35–55. The flanking charged and polar residues also make 5–30 a less precise estimate.

**Missing item-specific fact**

> Selecting the exact annotated endpoints 8 and 28, rather than a slightly expanded interval such as 5–30, requires an item-specific boundary annotation or prediction not supplied in the question.

**Reason**

> Sequence composition supports the location of a likely transmembrane helix, but does not establish exact residue boundaries with enough specificity to distinguish the closely overlapping choices.

### Question ambiguity

**Multiple defensible options named by Luna:** B, D.

> D gives the more plausible hydrophobic core, but B includes that core and the question does not define whether endpoints must match a particular annotation convention; a spanning segment can be reported with flanking residues.

### Important caveats

- The supporting annotation is computational, not experimental.
- The reviewer-only database evidence was not supplied to the evaluated model.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "transmembrane_0030",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt records annotate residues 8–28 as a transmembrane helix. The annotation is computational (ECO:0000255), so it supports the expected database annotation but is not evidence of experimental confirmation.",
    "evidence_ids": [
      "C5",
      "H3"
    ]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminus has a strongly hydrophobic stretch around residues 8–28, making it much more plausible as a membrane-spanning helix than residues 35–55. The flanking charged and polar residues also make 5–30 a less precise estimate.",
    "missing_item_specific_fact": "Selecting the exact annotated endpoints 8 and 28, rather than a slightly expanded interval such as 5–30, requires an item-specific boundary annotation or prediction not supplied in the question.",
    "reason": "Sequence composition supports the location of a likely transmembrane helix, but does not establish exact residue boundaries with enough specificity to distinguish the closely overlapping choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "D gives the more plausible hydrophobic core, but B includes that core and the question does not define whether endpoints must match a particular annotation convention; a spanning segment can be reported with flanking residues."
  },
  "important_caveats": [
    "The supporting annotation is computational, not experimental.",
    "The reviewer-only database evidence was not supplied to the evaluated model."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `A0A7T8F1I4`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 18. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1I4.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:44.613598+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":28},"start":{"modifier":"EXACT","value":8}},"type":"Transmembrane"}
```

Source SHA-256: `a450aa333c0480566d67fc577725d57e8ffabeeea7f1c8ff429be621fd79b04b`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1I4?format=txt&versions=18)  
**Locator:** `lines 105-107`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 18 / 1.  
**Retrieved:** 2026-11-02T04:25:47.051386+00:00.  

```text
FT   TRANSMEM        8..28
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `9364b021301c1c0c3fb659db92b723838ee62210edc6aa3fb3422781d6bcadb6`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json) (zero-based source row 30). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
