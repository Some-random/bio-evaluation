# transmembrane_0012

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **D** — 287..307

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | reasoning-supported | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MTLPILLGWFLTLCSSHIVRSCLQCDQVIRYVHEDFLSTVKGIRVRDQIELKKIIDHAYTNYRETSKLLSGVIDPTTLYRARTEYQSEFKRHWKEDRTNSLQWDLITIVEKGKRILQKHLEIFIAEGLCPNKCGLLYQRVMNCTSCQYGLFTCLSAKPPLDCGEHHLEADEGEEVVLDCFLSWHTLVVGQTEYHYSWHPGETNVLFDGEYEELVVTKESKIVLNQLSVSEEGSYRCLLKDQKGTALSRTFFQLEVKPFPSTSPRQVVTLPSLPLGYENTPYSLQKSSFLTVLILLTVLSITGSLIIIEYLRKSLKRQEEARGRDSRTAGDIELNTE

[Multiple Choices]
A. 27..47; 59..79; 109..129; 142..162; 168..188; 225..245
B. 291..304
C. 287..307; 298..318
D. 287..307
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

> The sequence-matched UniProt annotation identifies residues 287–307 as a helical transmembrane region. The cited evidence code indicates computational evidence, not experimental validation.

Cited evidence: [C5](#evidence-c5), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a continuous, strongly hydrophobic C-terminal stretch consistent with a single membrane-spanning helix. The 287–307 interval captures that span; 291–304 is a short subset, while 298–318 extends beyond the hydrophobic segment into the less suitable tail.

**Missing item-specific fact**

> No additional item-specific fact is needed to distinguish the plausible membrane-spanning interval from the listed alternatives, though exact boundary conventions can vary.

**Reason**

> The hydrophobic segment and the contrasting lengths and endpoints in the choices provide a concrete sequence-based basis for selecting D. The database annotation corroborates the answer but is not the only basis for it.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> Choice C includes the 287–307 interval but also proposes a second overlapping span extending past the hydrophobic region; it is not as defensible as D as a complete answer.

### Important caveats

- The supporting UniProt feature is computationally evidenced (ECO:0000255), not an experimentally established boundary.
- The historical and current source sequences match the supplied sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "transmembrane_0012",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies residues 287–307 as a helical transmembrane region. The cited evidence code indicates computational evidence, not experimental validation.",
    "evidence_ids": [
      "C5",
      "H2"
    ]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a continuous, strongly hydrophobic C-terminal stretch consistent with a single membrane-spanning helix. The 287–307 interval captures that span; 291–304 is a short subset, while 298–318 extends beyond the hydrophobic segment into the less suitable tail.",
    "missing_item_specific_fact": "No additional item-specific fact is needed to distinguish the plausible membrane-spanning interval from the listed alternatives, though exact boundary conventions can vary.",
    "reason": "The hydrophobic segment and the contrasting lengths and endpoints in the choices provide a concrete sequence-based basis for selecting D. The database annotation corroborates the answer but is not the only basis for it."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice C includes the 287–307 interval but also proposes a second overlapping span extending past the hydrophobic region; it is not as defensible as D as a complete answer."
  },
  "important_caveats": [
    "The supporting UniProt feature is computationally evidenced (ECO:0000255), not an experimentally established boundary.",
    "The historical and current source sequences match the supplied sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `A0A2R8QHQ6`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 30. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2R8QHQ6.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:50.294214+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":307},"start":{"modifier":"EXACT","value":287}},"type":"Transmembrane"}
```

Source SHA-256: `1f080979fe7048e78f2edfaa03e82a529e0dcfffb47df84982e5f47bec07c233`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2R8QHQ6?format=txt&versions=30)  
**Locator:** `lines 132-134`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 1.  
**Retrieved:** 2026-11-02T04:24:52.546075+00:00.  

```text
FT   TRANSMEM        287..307
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `98dd15dd75468aa1c87c8374da8af70b6254d13862c620694aed67db56c75e75`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json) (zero-based source row 12). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
