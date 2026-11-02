# EC_number_0082

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **B** — 2.3.1.312

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MQIKPPYLLFIGDATDKLSIKMAQSLADWRAELCVGELSVNGCTVSTGLNQCSICEAAKLGAKTFVLGFANSGGVLDKKWLPIISEAIENGMNIVSGLHDKLTNFDELVSLSQKHNTNLLDIRHPSTAFATGKGYKRKGKRLLTVGTDCSVGKMYTSLSLEKAMKEQNIDVDFRATGQCGILISGSGVAIDCVIADFISGAAESLSPDAEETHWDIIEGQGSLSHPAFAGVSLGLLHGSQPDALVICHALNRTHMRGLLHTSFPSIETTIELNIAAAKLTNPDVQVVGISVNTSSVSIEQGNEICERLSQTFGVPCVDPLRDGVDSIVANLC

[Multiple Choices]
A. 2.3.1.193
B. 2.3.1.312
C. 2.1.1.393
D. 5.2.1.8
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence.. The inputs provided by the user for this task include:

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

> The supplied sequence exactly matches the 332-aa UniProt entry annotated as EC 2.3.1.312. The annotation cites experimental evidence for acetyl-CoA-dependent acetylation of D-glutamate, and also reports activity with D-aspartate and D-glutamine.

Cited evidence: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may permit inference of an enzyme family or acetyltransferase-like activity, but the supplied input does not establish the specific substrate preference or complete EC classification needed to distinguish the options.

**Missing item-specific fact**

> The protein-specific experimentally characterized reaction and its EC assignment, namely D-amino-acid N-acetylation classified as EC 2.3.1.312.

**Reason**

> Choosing the precise EC number depends on protein-specific functional characterization or an external annotation; sequence-based general reasoning alone does not meaningfully resolve the relevant substrate-specific distinction.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> The matched sequence has direct cited annotation to option B; the evidence does not support another listed option.

### Important caveats

- The cited experimental evidence is represented here through UniProt annotations citing PubMed 36690779; the primary paper was not independently reviewed.
- The reviewer-only accession and annotation were not supplied to the evaluated model.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "EC_number_0082",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 332-aa UniProt entry annotated as EC 2.3.1.312. The annotation cites experimental evidence for acetyl-CoA-dependent acetylation of D-glutamate, and also reports activity with D-aspartate and D-glutamine.",
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C7",
      "H4",
      "H5",
      "H6"
    ]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may permit inference of an enzyme family or acetyltransferase-like activity, but the supplied input does not establish the specific substrate preference or complete EC classification needed to distinguish the options.",
    "missing_item_specific_fact": "The protein-specific experimentally characterized reaction and its EC assignment, namely D-amino-acid N-acetylation classified as EC 2.3.1.312.",
    "reason": "Choosing the precise EC number depends on protein-specific functional characterization or an external annotation; sequence-based general reasoning alone does not meaningfully resolve the relevant substrate-specific distinction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched sequence has direct cited annotation to option B; the evidence does not support another listed option."
  },
  "important_caveats": [
    "The cited experimental evidence is represented here through UniProt annotations citing PubMed 36690779; the primary paper was not independently reviewed.",
    "The reviewer-only accession and annotation were not supplied to the evaluated model."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `P0DXZ1`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 3. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ1.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:58.706491+00:00.  

```json
"P0DXZ1"
```

Source SHA-256: `aa2463d659dcce0272e4a1954d2f0e0ac1de2519b56334e15e5b9a8b29cffa17`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:58.706491+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"36690779","source":"PubMed"}],"value":"2.3.1.312"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"D-glutamate N-acetyltransferase"}}}
```

Source SHA-256: `aa2463d659dcce0272e4a1954d2f0e0ac1de2519b56334e15e5b9a8b29cffa17`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ1.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:58.706491+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"36690779","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:76496"}}],"reaction":{"ecNumber":"2.3.1.312","evidences":[{"evidenceCode":"ECO:0000269","id":"36690779","source":"PubMed"}],"name":"D-glutamate + acetyl-CoA = N-acetyl-D-glutamate + CoA + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:76495"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:29986"},{"database":"ChEBI","id":"CHEBI:57287"},{"database":"ChEBI","id":"CHEBI:57288"},{"database":"ChEBI","id":"CHEBI:195260"}]}}
```

Source SHA-256: `aa2463d659dcce0272e4a1954d2f0e0ac1de2519b56334e15e5b9a8b29cffa17`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ1.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:58.706491+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.3.1.312","evidences":[{"evidenceCode":"ECO:0000269","id":"36690779","source":"PubMed"}],"name":"D-aspartate + acetyl-CoA = N-acetyl-D-aspartate + CoA + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:76551"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:29990"},{"database":"ChEBI","id":"CHEBI:57287"},{"database":"ChEBI","id":"CHEBI:57288"},{"database":"ChEBI","id":"CHEBI:195274"}]}}
```

Source SHA-256: `aa2463d659dcce0272e4a1954d2f0e0ac1de2519b56334e15e5b9a8b29cffa17`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ1.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:58.706491+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.3.1.312","evidences":[{"evidenceCode":"ECO:0000269","id":"36690779","source":"PubMed"}],"name":"D-glutamine + acetyl-CoA = N-acetyl-D-glutamine + CoA + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:76547"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57287"},{"database":"ChEBI","id":"CHEBI:57288"},{"database":"ChEBI","id":"CHEBI:58000"},{"database":"ChEBI","id":"CHEBI:143880"}]}}
```

Source SHA-256: `aa2463d659dcce0272e4a1954d2f0e0ac1de2519b56334e15e5b9a8b29cffa17`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ1?format=txt&versions=3)  
**Locator:** `lines 31-37`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-02T04:30:00.858326+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=D-glutamate + acetyl-CoA = N-acetyl-D-glutamate + CoA + H(+);
CC         Xref=Rhea:RHEA:76495, ChEBI:CHEBI:15378, ChEBI:CHEBI:29986,
CC         ChEBI:CHEBI:57287, ChEBI:CHEBI:57288, ChEBI:CHEBI:195260;
CC         EC=2.3.1.312; Evidence={ECO:0000269|PubMed:36690779};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:76496;
CC         Evidence={ECO:0000269|PubMed:36690779};
```

Source SHA-256: `f028fea1879dfe3aaa57742281e0eecbec1a2030f44e9354a914347ae6b4be60`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ1?format=txt&versions=3)  
**Locator:** `lines 38-42`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-02T04:30:00.858326+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=D-aspartate + acetyl-CoA = N-acetyl-D-aspartate + CoA + H(+);
CC         Xref=Rhea:RHEA:76551, ChEBI:CHEBI:15378, ChEBI:CHEBI:29990,
CC         ChEBI:CHEBI:57287, ChEBI:CHEBI:57288, ChEBI:CHEBI:195274;
CC         EC=2.3.1.312; Evidence={ECO:0000269|PubMed:36690779};
```

Source SHA-256: `f028fea1879dfe3aaa57742281e0eecbec1a2030f44e9354a914347ae6b4be60`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ1?format=txt&versions=3)  
**Locator:** `lines 43-47`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-02T04:30:00.858326+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=D-glutamine + acetyl-CoA = N-acetyl-D-glutamine + CoA + H(+);
CC         Xref=Rhea:RHEA:76547, ChEBI:CHEBI:15378, ChEBI:CHEBI:57287,
CC         ChEBI:CHEBI:57288, ChEBI:CHEBI:58000, ChEBI:CHEBI:143880;
CC         EC=2.3.1.312; Evidence={ECO:0000269|PubMed:36690779};
```

Source SHA-256: `f028fea1879dfe3aaa57742281e0eecbec1a2030f44e9354a914347ae6b4be60`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json) (zero-based source row 82). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
