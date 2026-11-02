# GO_molecular_function_0034

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **D** — type 1 parathyroid hormone receptor binding

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | reasoning-supported | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MMSANTVAKVMIIMLAVCLLTQTDGKPVRKRAVSEIQLMHNLGKHLASMERMQWLRRKLQDMHNFVSLGVQMAARDGSHQKPTKKEENVLVDGNPKSLGEGDKADVDVLVKSKSQ

[Multiple Choices]
A. nicotinamide phosphoribosyltransferase activity
B. phosphatase activity
C. glycolipid mannosyltransferase activity
D. type 1 parathyroid hormone receptor binding
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

> The exact sequence matches the mouse parathyroid hormone precursor. UniProt describes it as binding and activating PTH1R by similarity and annotates type 1 parathyroid hormone receptor binding. That GO annotation is computationally transferred, not direct experimental evidence for this exact sequence in the excerpts.

Cited evidence: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C10](#evidence-c10), [H5](#evidence-h5), [H10](#evidence-h10).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is short and begins with a strongly hydrophobic signal-peptide-like region, consistent with a secreted peptide precursor. It lacks an evident enzyme-sized architecture or recognizable catalytic motif, making the three enzyme activities less plausible than a receptor-binding peptide hormone.

**Missing item-specific fact**

> The sequence alone does not establish the specific receptor target, PTH1R; that exact binding annotation is supported here by protein-specific database information and transfer by similarity.

**Reason**

> Sequence architecture gives meaningful grounds to favor a secreted peptide ligand over the enzyme choices, although identifying the exact receptor interaction requires item-specific evidence.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> Among the listed choices, D is the only one consistent with the sequence's likely secreted peptide-precursor architecture.

### Important caveats

- The sequence match identifies a mouse PTH precursor, but recognizing that exact identity is not itself sequence-based reasoning.
- The supplied GO receptor-binding annotation uses ISO evidence, and the functional description characterizes receptor binding as by similarity; the excerpts do not provide direct experimental evidence for that interaction in this exact protein.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "GO_molecular_function_0034",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the mouse parathyroid hormone precursor. UniProt describes it as binding and activating PTH1R by similarity and annotates type 1 parathyroid hormone receptor binding. That GO annotation is computationally transferred, not direct experimental evidence for this exact sequence in the excerpts.",
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C10",
      "H5",
      "H10"
    ]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is short and begins with a strongly hydrophobic signal-peptide-like region, consistent with a secreted peptide precursor. It lacks an evident enzyme-sized architecture or recognizable catalytic motif, making the three enzyme activities less plausible than a receptor-binding peptide hormone.",
    "missing_item_specific_fact": "The sequence alone does not establish the specific receptor target, PTH1R; that exact binding annotation is supported here by protein-specific database information and transfer by similarity.",
    "reason": "Sequence architecture gives meaningful grounds to favor a secreted peptide ligand over the enzyme choices, although identifying the exact receptor interaction requires item-specific evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, D is the only one consistent with the sequence's likely secreted peptide-precursor architecture."
  },
  "important_caveats": [
    "The sequence match identifies a mouse PTH precursor, but recognizing that exact identity is not itself sequence-based reasoning.",
    "The supplied GO receptor-binding annotation uses ISO evidence, and the functional description characterizes receptor binding as by similarity; the excerpts do not provide direct experimental evidence for that interaction in this exact protein."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `Q9Z0L6`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 187. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9Z0L6.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:53.362529+00:00.  

```json
"Q9Z0L6"
```

Source SHA-256: `a5fb53dfa148e6d67354819a91204340e628f1ef95f869f6284a224f75d168f4`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9Z0L6.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:53.362529+00:00.  

```json
{"flag":"Precursor","recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"12370121","source":"PubMed"}],"value":"Parathyroid hormone"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"12370121","source":"PubMed"}],"value":"PTH"}]}}
```

Source SHA-256: `a5fb53dfa148e6d67354819a91204340e628f1ef95f869f6284a224f75d168f4`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9Z0L6.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:53.362529+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P01270","source":"UniProtKB"},{"evidenceCode":"ECO:0000269","id":"11606467","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"17975671","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"19968565","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"36862513","source":"PubMed"}],"value":"Peptide hormone secreted by parathyroid chief cells that acts as a primary endocrine regulator of extracellular calcium and phosphate homeostasis, acting primarily on bone and kidney to maintain serum calcium levels within a narrow range (PubMed:11606467, PubMed:19968565). Acts by binding and activating the G protein-coupled receptor PTH1R, engaging the receptor to activate G(s)-mediated cAMP/PKA signaling (By similarity). In bone, acts indirectly on osteoclasts by binding PTH1R on cells of the osteoblast/osteocyte lineage, where it increases expression of TNFSF11/RANKL and decreases expression of TNFRSF11B/OPG, thereby raising the RANKL/OPG ratio and stimulating osteoclast differentiation and bone resorption (By similarity). Stimulates also [1-14C]-2-deoxy-D-glucose (2DG) transport and glycogen synthesis in osteoblastic cells (By similarity). In distal renal tubule cells, stimulates active Ca(2+) reabsorption via the adenylyl cyclase-cAMP-protein kinase A (PKA) pathway leading to the phosphorylation and activation of the calcium selective cation channel TRPV5 (By similarity). Acting on PTH1R in proximal renal tubule cells, decreases reabsorption of filtered phosphate by reducing apical abundance of SLC34A1, through a mechanism involving PTH1R-activated PKC-mediated phosphorylation of the scaffold NHERF1, causing dissociation of the NHERF1-SLC34A1 complex and subsequent clathrin-mediated endocytosis and lysosomal degradation of the cotransporter (PubMed:17975671). Activates also transcription of CYP27B1 (25-hydroxyvitamin D3 1-alpha-hydroxylase) through a cAMP/PKA/SIK2-SIK3/CRTC2 axis, thereby increasing renal synthesis of the active vitamin D metabolite 1,25-dihydroxyvitamin D(3) (PubMed:36862513)"}]}
```

Source SHA-256: `a5fb53dfa148e6d67354819a91204340e628f1ef95f869f6284a224f75d168f4`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9Z0L6.json)  
**Locator:** `/uniProtKBCrossReferences/38`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:53.362529+00:00.  

```json
{"database":"GO","id":"GO:0031857","properties":[{"key":"GoTerm","value":"F:type 1 parathyroid hormone receptor binding"},{"key":"GoEvidenceType","value":"ISO:GO_Central"}]}
```

Source SHA-256: `a5fb53dfa148e6d67354819a91204340e628f1ef95f869f6284a224f75d168f4`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9Z0L6?format=txt&versions=187)  
**Locator:** `lines 112-118`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 187 / 1.  
**Retrieved:** 2026-11-02T04:33:56.766069+00:00.  

```text
CC   -!- FUNCTION: Parathyroid hormone elevates calcium level by dissolving the
CC       salts in bone and preventing their renal excretion (PubMed:11606467,
CC       PubMed:19968565). Acts by binding to its receptor, PTH1R, activating G
CC       protein-coupled receptor signaling (By similarity). Stimulates [1-14C]-
CC       2-deoxy-D-glucose (2DG) transport and glycogen synthesis in
CC       osteoblastic cells (By similarity). {ECO:0000250|UniProtKB:P01270,
CC       ECO:0000269|PubMed:11606467, ECO:0000269|PubMed:19968565}.
```

Source SHA-256: `3be318ad34c791fc0b4cbd4154921c3154a5a243619b25f61225e6948241545e`.

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9Z0L6?format=txt&versions=187)  
**Locator:** `lines 179-179`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 187 / 1.  
**Retrieved:** 2026-11-02T04:33:56.766069+00:00.  

```text
DR   GO; GO:0031857; F:type 1 parathyroid hormone receptor binding; ISO:GO_Central.
```

Source SHA-256: `3be318ad34c791fc0b4cbd4154921c3154a5a243619b25f61225e6948241545e`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json) (zero-based source row 34). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
