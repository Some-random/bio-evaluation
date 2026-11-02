# GO_molecular_function_0015

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **A** — exo-alpha-sialidase activity

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MEPSKLFTISDNATFAPGPVINVADKKTFRTCFRILVLSVQAVTLILVIVNLGELVRMINDQGLSNQLSSITDKIRESANMIASAVGVMNQVIHGVTVSLPLQIEGNQNQLLSTLATICTSKKQVSNCSTNIPLVNDLRFINGINKFIIEDYATHDFSIGHPLNMPSFIPTATSPNGCTRIPSFSLGKTHWCYTHNVINANCKDHTSSNQYVSMGILVQTASGYPMFKTLKIQYLSDGLNRKSCSIATVPDGCAMYCYISTQLETDDYAGSSPPTQKLTLLFYNDTVTERTISPSGLEGNWATLVPGVGSGIYFENKLIFPAYGGVLPNSTLGVKSAREFFRPVNPYNPCSGPQQDLDQRALRSYFPSYFSNRRVQSAFLVCAWNQILVTNCELVVPSNNQTLMGAEGRVLLINNRLLYYQRSTSWWPYELLYEISFTFTNSGQSSVNMSWIPIYSFTRPGSGNCSGENVCPTACVSGVYLDPWPLTPYSHQSGINRNFYFTGALLNSSTTRVNPTLYVSALNNLKVLAPYGTQGLFASYTTTTCFQDTGDASVYCVYIMELASNIVGEFQILPVLTRLTIT

[Multiple Choices]
A. exo-alpha-sialidase activity
B. ribosome binding
C. zinc ion transmembrane transporter activity
D. misfolded protein binding
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Molecular Function Prediction, which is to predict the fundamental activity of a protein at the molecular level, as defined by the Gene Ontology (GO) 'Molecular Function' branch. This describes the elemental tasks a protein performs, such as catalysis, transport, or binding to specific molecules. Based on the protein's amino acid sequence, you are to select the option that best describes its primary molecular function.. The inputs provided by the user for this task include:

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

> The sequence matches the UniProt entry for mumps virus hemagglutinin-neuraminidase, whose annotated catalytic activity is hydrolysis of terminal sialic acid linkages (EC 3.2.1.18), corresponding to exo-alpha-sialidase activity. The cited UniProt functional and catalytic annotations are transferred by similarity, not direct experimental evidence for this exact protein.

Cited evidence: [C1](#evidence-c1), [C4](#evidence-c4), [C7](#evidence-c7), [C8](#evidence-c8), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic segment and overall sequence are consistent with a membrane-associated viral glycoprotein, making ribosome binding and zinc transport less plausible. But those broad features do not specifically establish sialidase catalysis over other membrane-protein functions.

**Missing item-specific fact**

> The specific assignment of this sequence to a hemagglutinin-neuraminidase with sialidase activity, or equivalent protein-specific functional/domain annotation, is absent from the prompt.

**Reason**

> Choosing A requires the specific functional identity or a reliable recognition of its protein-specific catalytic features; general sequence and biological reasoning alone do not establish that activity.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> Among the listed choices, exo-alpha-sialidase activity is supported for this protein. Its additional receptor-binding role is not one of the options.

### Important caveats

- The sequence match is exact, but the retrieved functional evidence is primarily similarity-based rather than direct experimental evidence for this sequence.
- The exact source snapshot used by the author is unknown.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "GO_molecular_function_0015",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry for mumps virus hemagglutinin-neuraminidase, whose annotated catalytic activity is hydrolysis of terminal sialic acid linkages (EC 3.2.1.18), corresponding to exo-alpha-sialidase activity. The cited UniProt functional and catalytic annotations are transferred by similarity, not direct experimental evidence for this exact protein.",
    "evidence_ids": [
      "C1",
      "C4",
      "C7",
      "C8",
      "H4",
      "H5"
    ]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment and overall sequence are consistent with a membrane-associated viral glycoprotein, making ribosome binding and zinc transport less plausible. But those broad features do not specifically establish sialidase catalysis over other membrane-protein functions.",
    "missing_item_specific_fact": "The specific assignment of this sequence to a hemagglutinin-neuraminidase with sialidase activity, or equivalent protein-specific functional/domain annotation, is absent from the prompt.",
    "reason": "Choosing A requires the specific functional identity or a reliable recognition of its protein-specific catalytic features; general sequence and biological reasoning alone do not establish that activity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, exo-alpha-sialidase activity is supported for this protein. Its additional receptor-binding role is not one of the options."
  },
  "important_caveats": [
    "The sequence match is exact, but the retrieved functional evidence is primarily similarity-based rather than direct experimental evidence for this sequence.",
    "The exact source snapshot used by the author is unknown."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `Q5SC51`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 105. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC51.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:29.846842+00:00.  

```json
"Q5SC51"
```

Source SHA-256: `84cb4071f2488c26b98cb3a00a95cf7fafbb3f15b4205e39b2029f487b04b1c3`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC51.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:29.846842+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9WAF5","source":"UniProtKB"}],"value":"3.2.1.18"}],"fullName":{"value":"Hemagglutinin-neuraminidase"}}}
```

Source SHA-256: `84cb4071f2488c26b98cb3a00a95cf7fafbb3f15b4205e39b2029f487b04b1c3`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC51.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:29.846842+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.1.18","evidences":[{"evidenceCode":"ECO:0000250","id":"Q9WAF5","source":"UniProtKB"}],"name":"Hydrolysis of alpha-(2->3)-, alpha-(2->6)-, alpha-(2->8)- glycosidic linkages of terminal sialic acid residues in oligosaccharides, glycoproteins, glycolipids, colominic acid and synthetic substrates."}}
```

Source SHA-256: `84cb4071f2488c26b98cb3a00a95cf7fafbb3f15b4205e39b2029f487b04b1c3`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC51.json)  
**Locator:** `/uniProtKBCrossReferences/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:29.846842+00:00.  

```json
{"database":"GO","id":"GO:0004308","properties":[{"key":"GoTerm","value":"F:exo-alpha-sialidase activity"},{"key":"GoEvidenceType","value":"ISS:UniProtKB"}]}
```

Source SHA-256: `84cb4071f2488c26b98cb3a00a95cf7fafbb3f15b4205e39b2029f487b04b1c3`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC51?format=txt&versions=105)  
**Locator:** `lines 51-56`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 105 / 1.  
**Retrieved:** 2026-11-02T04:31:32.054381+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Hydrolysis of alpha-(2->3)-, alpha-(2->6)-, alpha-
CC         (2->8)- glycosidic linkages of terminal sialic acid residues in
CC         oligosaccharides, glycoproteins, glycolipids, colominic acid and
CC         synthetic substrates.; EC=3.2.1.18;
CC         Evidence={ECO:0000250|UniProtKB:Q9WAF5};
```

Source SHA-256: `8bf1ba1afc5634387cc3311f78ac6fc61cefd51f3d1e338d340ea041cd46beeb`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC51?format=txt&versions=105)  
**Locator:** `lines 82-82`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 105 / 1.  
**Retrieved:** 2026-11-02T04:31:32.054381+00:00.  

```text
DR   GO; GO:0004308; F:exo-alpha-sialidase activity; IEA:UniProtKB-EC.
```

Source SHA-256: `8bf1ba1afc5634387cc3311f78ac6fc61cefd51f3d1e338d340ea041cd46beeb`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json) (zero-based source row 15). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
