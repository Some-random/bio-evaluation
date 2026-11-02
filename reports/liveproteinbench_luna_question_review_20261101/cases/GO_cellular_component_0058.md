# GO_cellular_component_0058

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **B** — plasma membrane

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | reasoning-supported | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MCNVSQDSCNIDSRLDSLFPPTLYIFVMVIGFPTNCLSLWAAFVQVRQKNELGVYLLNLSISDLLYIATLPPWVNYFLHQDNWIHGPESCKLFGFILYTNIYISIGFLSCISVDRYLAVAHPLKFAKVRRVKTAAVVSAVVWAIEIGANSAPLFHNELFEDRFNHTFCFEKYPMEDWVAQMNLYRVFVGFLFPWVLMLFCYQGILRAVKTNVSTEREEKAKIKRLALSLIAILLFCFAPYHLILLSRSVVYLGQPCDCTFEENIFTAYHVSLALTSLNCVADPILYCLANEGARSEVTRGLAPLMKFFSASRPNMDSFARSVTLDTPWSSRRAAAPSPRSWSLCGQTGGRGRRSRVRRRRDCKC

[Multiple Choices]
A. fungal-type cell wall
B. plasma membrane
C. nucleolus
D. chromosome
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

> The exact sequence match is annotated as a multipass cell-membrane protein, with a plasma-membrane GO annotation. The location evidence is computational or transferred by similarity rather than direct experimental evidence for this protein.

Cited evidence: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has multiple long hydrophobic segments consistent with a multipass membrane protein and a GPCR-like architecture. That strongly favors a membrane location over the fungal cell wall, nucleolus, or chromosome; a cell-surface receptor is plausibly at the plasma membrane.

**Missing item-specific fact**

> No protein-specific annotation is strictly necessary to distinguish these choices, although such annotation supports the plasma-membrane assignment.

**Reason**

> The sequence provides meaningful biological grounds for choosing B over the clearly incompatible cell-wall and nuclear options. The database evidence is corroborative, not the only basis for the choice.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> Among the listed choices, the plasma membrane is the only one consistent with the sequence's multipass receptor-like architecture.

### Important caveats

- The reviewed subcellular-location annotation is transferred from another UniProt protein, and the multipass topology annotation is computational; neither alone establishes direct experimental localization of this exact protein.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "GO_cellular_component_0058",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence match is annotated as a multipass cell-membrane protein, with a plasma-membrane GO annotation. The location evidence is computational or transferred by similarity rather than direct experimental evidence for this protein.",
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has multiple long hydrophobic segments consistent with a multipass membrane protein and a GPCR-like architecture. That strongly favors a membrane location over the fungal cell wall, nucleolus, or chromosome; a cell-surface receptor is plausibly at the plasma membrane.",
    "missing_item_specific_fact": "No protein-specific annotation is strictly necessary to distinguish these choices, although such annotation supports the plasma-membrane assignment.",
    "reason": "The sequence provides meaningful biological grounds for choosing B over the clearly incompatible cell-wall and nuclear options. The database evidence is corroborative, not the only basis for the choice."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the plasma membrane is the only one consistent with the sequence's multipass receptor-like architecture."
  },
  "important_caveats": [
    "The reviewed subcellular-location annotation is transferred from another UniProt protein, and the multipass topology annotation is computational; neither alone establishes direct experimental localization of this exact protein."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `A0A4W3GG95`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 30. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:47.202623+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000250","id":"P46093","source":"UniProtKB"}],"id":"SL-0039","value":"Cell membrane"},"topology":{"evidences":[{"evidenceCode":"ECO:0000255"}],"id":"SL-9909","value":"Multi-pass membrane protein"}}]}
```

Source SHA-256: `a92b2a2611b3e831e67c290051c3b607ae4d71a21502ae38da2c507908426245`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json)  
**Locator:** `/uniProtKBCrossReferences/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:47.202623+00:00.  

```json
{"database":"GO","id":"GO:0005886","properties":[{"key":"GoTerm","value":"C:plasma membrane"},{"key":"GoEvidenceType","value":"ISS:UniProtKB"}]}
```

Source SHA-256: `a92b2a2611b3e831e67c290051c3b607ae4d71a21502ae38da2c507908426245`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A4W3GG95?format=txt&versions=30)  
**Locator:** `lines 46-47`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 1.  
**Retrieved:** 2026-11-01T06:27:31.027017+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000250|UniProtKB:P46093};
CC       Multi-pass membrane protein {ECO:0000255}.
```

Source SHA-256: `2de235f5ecdbc32faad1779acf9f8307edf330e58265fd2df418707701078865`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A4W3GG95?format=txt&versions=30)  
**Locator:** `lines 64-64`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 1.  
**Retrieved:** 2026-11-01T06:27:31.027017+00:00.  

```text
DR   GO; GO:0005886; C:plasma membrane; IEA:UniProtKB-SubCell.
```

Source SHA-256: `2de235f5ecdbc32faad1779acf9f8307edf330e58265fd2df418707701078865`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json) (zero-based source row 58). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
