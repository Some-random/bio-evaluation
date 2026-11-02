# GO_cellular_component_0060

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **A** — cell surface

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | reasoning-supported | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MSNRGQLSIEMVILVLAVLVSGSYVALDLSKGAFETTAVNDVQESSYCGFTPDFGATSIDKALVKLTTGIININPNAAVTNNEFNATYTNTTDNTVVTYSLDNVHPNLIKNYADGTIVKVPLNETWKNFTASNIILRMKSDYVCTINGENVSMESNCFEITAPLGSDSFDFQMSAGTGAGQYYLRLVDQEVTIEFSLE

[Multiple Choices]
A. cell surface
B. mitochondrial [2Fe-2S] assembly complex
C. ATP-binding cassette (ABC) transporter complex
D. egg chorion
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Cellular Component Prediction, which is to predict the primary Cellular Component where a protein is located, according to the Gene Ontology (GO) framework. A protein's location within a cell (e.g., Nucleus, Mitochondria, Cytoplasm) is critical for its function and is often determined by specific targeting signals in its amino acid sequence. Based on the provided sequence, you must identify the most likely compartment where the protein resides.. The inputs provided by the user for this task include:

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

> The exact sequence matches a UniProt record annotated as a probable minor pilin, with cell-surface localization and a cell-surface GO annotation. The localization is supported by transferred or computational annotation, not direct experimental evidence in the supplied excerpts.

Cited evidence: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal hydrophobic leader followed by a largely non-multipass globular region is compatible with an exported pilin rather than an ABC transporter component; the sequence also lacks an obvious ATP-binding domain. This supports a cell-surface-associated protein over the listed complex options.

**Missing item-specific fact**

> A protein-specific identification as a minor pilin would strengthen the inference that it is surface-associated; the sequence alone does not establish direct experimental localization.

**Reason**

> The sequence architecture provides a meaningful biological basis for choosing the surface-associated option among these choices, though it predicts export/pilin-like character more directly than it proves cell-surface attachment.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> The signal-peptide/pilin-like architecture favors cell-surface association over the listed alternatives. Secreted localization is also annotated, but it is not a separate choice.

### Important caveats

- The current and historical UniProt sequence matches support applicability to this exact sequence.
- The cited localization evidence is transferred by similarity, and the GO cell-surface annotation is computational; the excerpts do not establish experimental validation.
- The exact author source snapshot is unknown.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "GO_cellular_component_0060",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt record annotated as a probable minor pilin, with cell-surface localization and a cell-surface GO annotation. The localization is supported by transferred or computational annotation, not direct experimental evidence in the supplied excerpts.",
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H2",
      "H3"
    ]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal hydrophobic leader followed by a largely non-multipass globular region is compatible with an exported pilin rather than an ABC transporter component; the sequence also lacks an obvious ATP-binding domain. This supports a cell-surface-associated protein over the listed complex options.",
    "missing_item_specific_fact": "A protein-specific identification as a minor pilin would strengthen the inference that it is surface-associated; the sequence alone does not establish direct experimental localization.",
    "reason": "The sequence architecture provides a meaningful biological basis for choosing the surface-associated option among these choices, though it predicts export/pilin-like character more directly than it proves cell-surface attachment."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The signal-peptide/pilin-like architecture favors cell-surface association over the listed alternatives. Secreted localization is also annotated, but it is not a separate choice."
  },
  "important_caveats": [
    "The current and historical UniProt sequence matches support applicability to this exact sequence.",
    "The cited localization evidence is transferred by similarity, and the GO cell-surface annotation is computational; the excerpts do not establish experimental validation.",
    "The exact author source snapshot is unknown."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `Q6LZC0`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 75. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LZC0.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:36.716902+00:00.  

```json
"Q6LZC0"
```

Source SHA-256: `3db999749abf6c20699452461ca055eda952536b51b4b243a842e55072268151`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LZC0.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:36.716902+00:00.  

```json
{"flag":"Precursor","recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Probable minor pilin MMP0709"}}}
```

Source SHA-256: `3db999749abf6c20699452461ca055eda952536b51b4b243a842e55072268151`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LZC0.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:36.716902+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q6LWM4","source":"UniProtKB"}],"id":"SL-0243","value":"Secreted"}},{"location":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q6LWM4","source":"UniProtKB"}],"id":"SL-0310","value":"Cell surface"}},{"location":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q6LWM4","source":"UniProtKB"}],"id":"SL-0113","value":"Fimbrium"}}]}
```

Source SHA-256: `3db999749abf6c20699452461ca055eda952536b51b4b243a842e55072268151`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LZC0.json)  
**Locator:** `/uniProtKBCrossReferences/12`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:36.716902+00:00.  

```json
{"database":"GO","id":"GO:0009986","properties":[{"key":"GoTerm","value":"C:cell surface"},{"key":"GoEvidenceType","value":"ISS:UniProtKB"}]}
```

Source SHA-256: `3db999749abf6c20699452461ca055eda952536b51b4b243a842e55072268151`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6LZC0?format=txt&versions=75)  
**Locator:** `lines 35-37`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 75 / 1.  
**Retrieved:** 2026-11-02T04:31:40.518419+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Secreted {ECO:0000250|UniProtKB:Q6LWM4}. Cell
CC       surface {ECO:0000250|UniProtKB:Q6LWM4}. Fimbrium
CC       {ECO:0000250|UniProtKB:Q6LWM4}.
```

Source SHA-256: `61362a31ad043a1d4de7160cee8e25e0f26f8c0cb1765bb8133df45d8e8d5e54`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6LZC0?format=txt&versions=75)  
**Locator:** `lines 64-64`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 75 / 1.  
**Retrieved:** 2026-11-02T04:31:40.518419+00:00.  

```text
DR   GO; GO:0009986; C:cell surface; IEA:UniProtKB-SubCell.
```

Source SHA-256: `61362a31ad043a1d4de7160cee8e25e0f26f8c0cb1765bb8133df45d8e8d5e54`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json) (zero-based source row 60). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
