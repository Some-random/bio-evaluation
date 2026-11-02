# GO_cellular_component_0086

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **A** — cell surface

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MLLNSKRGQVSIEMLILILAVLLSGTIFAAHMTKNTVSHDEISDVKKQTFKSFLGSVEGSTASSLPEKISEEDTSPEEDTIPEEDTSPEEDTIPEEDTIPEEDTSTEIPIGKNVKIYNLPIKEEKQNWFLDILNTALDRISAILDGFFSLFGLDLFNNDEIIPNILVKDFEGNRIPLSFDWERLSYTTDWFYAKEIEFTGDSSAKYSKLDLFRIFPIYSYSDTTFRITDLSYNLTYDVPPSTAKKTITITSNIPEGIKCKVTYKIGGILTGDYYTLEIDEKTSSNKYNNVNIAFE

[Multiple Choices]
A. cell surface
B. dendrite
C. axon cytoplasm
D. endoplasmic reticulum
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

> The exact sequence matches a UniProt entry annotated to the cell surface. The annotation is supported by transfer from a related protein (ECO:0000250), and the GO assignment is computational/inferred (ISS historically; IEA in the archived record), not direct experimental evidence. The entry also describes a probable minor pilin and annotates it as secreted and part of a fimbrium, consistent with cell-surface association.

Cited evidence: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic region and likely signal/anchor sequence are consistent with export or membrane association, but do not by themselves establish that the mature protein is cell-surface-associated rather than another listed location.

**Missing item-specific fact**

> Identifying this sequence as the probable minor pilin MMP0601 and knowing its transferred cell-surface annotation are protein-specific facts absent from the question.

**Reason**

> The sequence offers a broad localization clue, but distinguishing the keyed cell-surface assignment depends on protein identity/function and its annotation, not on a sufficiently specific general biological inference from the supplied input.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> The reviewer evidence supports cell surface among the listed choices. Other annotations for this protein include secreted and fimbrium, but those are not options.

### Important caveats

- The localization support is transferred/inferred rather than independently verified experimental evidence in the supplied excerpts.
- The sequence matches the current and archived UniProt records, but the author's exact source snapshot is unknown.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "GO_cellular_component_0086",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated to the cell surface. The annotation is supported by transfer from a related protein (ECO:0000250), and the GO assignment is computational/inferred (ISS historically; IEA in the archived record), not direct experimental evidence. The entry also describes a probable minor pilin and annotates it as secreted and part of a fimbrium, consistent with cell-surface association.",
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
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic region and likely signal/anchor sequence are consistent with export or membrane association, but do not by themselves establish that the mature protein is cell-surface-associated rather than another listed location.",
    "missing_item_specific_fact": "Identifying this sequence as the probable minor pilin MMP0601 and knowing its transferred cell-surface annotation are protein-specific facts absent from the question.",
    "reason": "The sequence offers a broad localization clue, but distinguishing the keyed cell-surface assignment depends on protein identity/function and its annotation, not on a sufficiently specific general biological inference from the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports cell surface among the listed choices. Other annotations for this protein include secreted and fimbrium, but those are not options."
  },
  "important_caveats": [
    "The localization support is transferred/inferred rather than independently verified experimental evidence in the supplied excerpts.",
    "The sequence matches the current and archived UniProt records, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `Q6LZM3`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 73. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LZM3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:38.071255+00:00.  

```json
"Q6LZM3"
```

Source SHA-256: `f65d8b6a81e43709b362bb1aff50762f04a31bac8e1a1b7b6ba493af5a50bfb2`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LZM3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:38.071255+00:00.  

```json
{"flag":"Precursor","recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Probable minor pilin MMP0601"}}}
```

Source SHA-256: `f65d8b6a81e43709b362bb1aff50762f04a31bac8e1a1b7b6ba493af5a50bfb2`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LZM3.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:38.071255+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q6LWM4","source":"UniProtKB"}],"id":"SL-0243","value":"Secreted"}},{"location":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q6LWM4","source":"UniProtKB"}],"id":"SL-0310","value":"Cell surface"}},{"location":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q6LWM4","source":"UniProtKB"}],"id":"SL-0113","value":"Fimbrium"}}]}
```

Source SHA-256: `f65d8b6a81e43709b362bb1aff50762f04a31bac8e1a1b7b6ba493af5a50bfb2`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LZM3.json)  
**Locator:** `/uniProtKBCrossReferences/12`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:38.071255+00:00.  

```json
{"database":"GO","id":"GO:0009986","properties":[{"key":"GoTerm","value":"C:cell surface"},{"key":"GoEvidenceType","value":"ISS:UniProtKB"}]}
```

Source SHA-256: `f65d8b6a81e43709b362bb1aff50762f04a31bac8e1a1b7b6ba493af5a50bfb2`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6LZM3?format=txt&versions=73)  
**Locator:** `lines 35-37`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 73 / 1.  
**Retrieved:** 2026-11-02T04:31:40.632602+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Secreted {ECO:0000250|UniProtKB:Q6LWM4}. Cell
CC       surface {ECO:0000250|UniProtKB:Q6LWM4}. Fimbrium
CC       {ECO:0000250|UniProtKB:Q6LWM4}.
```

Source SHA-256: `17589c2d3cb1884d286af6f6d4efa07afc0285ac6c6788da5a9fdf05c0f9061a`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6LZM3?format=txt&versions=73)  
**Locator:** `lines 64-64`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 73 / 1.  
**Retrieved:** 2026-11-02T04:31:40.632602+00:00.  

```text
DR   GO; GO:0009986; C:cell surface; IEA:UniProtKB-SubCell.
```

Source SHA-256: `17589c2d3cb1884d286af6f6d4efa07afc0285ac6c6788da5a9fdf05c0f9061a`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json) (zero-based source row 86). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
