# transmembrane_0090

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **D** — 478..498

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | reasoning-supported | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MGRDARRLPLLPFLLLLLAAAAGVAESATDAEAIHDLARSVPALGWDGDNVCGFEGVTCERGGAGKVTELNLADRGLSGTLPDSLSSLTSLTALQLQGNALTGAVPSLARMGSLARLALDGNAFTSLPPDFLHGLTSLQYLTMENLPLPPWPVPDAIANCSSLDTFSASNASISGPFPAVLATLVSLRNLRLSYNNLTGGLPPELSSLIAMESLQLNNQRSDDKLSGPIDVIASMKSLKLLWIQSNKFTGPIPDLNGTQLEAFNVRDNMLTGVVPPSLTGLMSLKNVSLSNNNFQGPKPAFAAIPGQDEDSGNGFCLNTPGPCSPLTTTLLQVAEGFGYPYELAKTWKGNDPCSPAWVGIVCTSSDVSMINLSRKNLSGRISPALANLTRLARLDLSNNNLTGVIPDVLTTLPSLTVLNVANNRLTGEVPKFKPSVNVLAQGNLFGQSSGSSGGGGGSDGDSSSSDSAGGGKSKPNTGMIIGIIVAVIILFACIALLVHHRKKKNVEKFRPVSTKTSPAESEMMKIQVVGANGISNGSSAFPTELYSHVSAANSSNISELFESHGMQLSVEVLLKATNNFSEDCILGRGGFGVVFKGNLNGKLVAVKRCDSGTMGTKGQEEFLAEIDVLRKVRHRHLVALLGYCTHGNERLLVYEYMSGGTLREHLCDLQQSGFIPLTWTQRMTIALDVARGIEYLHGLAQETFIHRDLKPSNILLDQDLRAKVSDFGLVKLAKDTDKSLMTRIAGTFGYLAPEYATTGKVTTKVDVYAYGVILMEMITGRKVLDDSLPDDETHLVTIFRRNILDKEKFRKFVDPTLELSAEGWTSLLEVADLARHCTAREPYQRPDMCHCVNRLSSLVDQWKPTNIDEDDYEGETSEMGLHQQLEKWRCDDFTISDSDTFGSFNVPRKYNG

[Multiple Choices]
A. 478..498; 128..147
B. 13..35
C. 481..501
D. 478..498
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

> The matched-sequence UniProt annotation places a helical transmembrane region at 478..498, agreeing with D. Its evidence code (ECO:0000255) indicates computational annotation, not direct experimental confirmation.

Cited evidence: [H4](#evidence-h4), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a pronounced hydrophobic stretch around 478..498, followed by the basic HHRKKK flank. D includes the hydrophobic stretch; C shifts the interval and includes the basic flank. The earlier hydrophobic N-terminus is consistent with a signal peptide, while the long extracellular region followed by this hydrophobic segment and a cytoplasmic kinase domain supports a C-terminal membrane anchor.

**Missing item-specific fact**

> No protein-specific annotation is needed to distinguish these choices from the sequence, although the exact annotated residue boundaries are not experimentally established by the input alone.

**Reason**

> The sequence and domain context provide a concrete basis for identifying the membrane-spanning segment and favor D over the shifted alternative.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> The prominent C-terminal hydrophobic interval and its flanking basic residues distinguish D from the shifted interval in C; the other choices do not identify that segment alone.

### Important caveats

- The supporting UniProt feature is computationally annotated; it should not be described as direct experimental evidence.
- Reviewer-only database evidence supports the key but was not available to the evaluated model.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "transmembrane_0090",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched-sequence UniProt annotation places a helical transmembrane region at 478..498, agreeing with D. Its evidence code (ECO:0000255) indicates computational annotation, not direct experimental confirmation.",
    "evidence_ids": [
      "H4",
      "C6"
    ]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a pronounced hydrophobic stretch around 478..498, followed by the basic HHRKKK flank. D includes the hydrophobic stretch; C shifts the interval and includes the basic flank. The earlier hydrophobic N-terminus is consistent with a signal peptide, while the long extracellular region followed by this hydrophobic segment and a cytoplasmic kinase domain supports a C-terminal membrane anchor.",
    "missing_item_specific_fact": "No protein-specific annotation is needed to distinguish these choices from the sequence, although the exact annotated residue boundaries are not experimentally established by the input alone.",
    "reason": "The sequence and domain context provide a concrete basis for identifying the membrane-spanning segment and favor D over the shifted alternative."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The prominent C-terminal hydrophobic interval and its flanking basic residues distinguish D from the shifted interval in C; the other choices do not identify that segment alone."
  },
  "important_caveats": [
    "The supporting UniProt feature is computationally annotated; it should not be described as direct experimental evidence.",
    "Reviewer-only database evidence supports the key but was not available to the evaluated model."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `Q2R560`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 23. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2R560.json)  
**Locator:** `/features/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:20.782611+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":498},"start":{"modifier":"EXACT","value":478}},"type":"Transmembrane"}
```

Source SHA-256: `6134946c5befacc9a9d4eee6c7262603fd779f3b8b073ce00fe2d5c0e1a621c4`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2R560?format=txt&versions=23)  
**Locator:** `lines 181-183`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 23 / 1.  
**Retrieved:** 2026-11-01T06:28:32.565844+00:00.  

```text
FT   TRANSMEM        478..498
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `8a1500792a74c38b22c2f5627966de80a760b1fed597a74e00b3d2510fcaa15a`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json) (zero-based source row 90). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
