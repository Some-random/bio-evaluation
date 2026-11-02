# catalytic_activity_0139

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **B** — norajmaline + S-adenosyl-L-methionine = ajmaline + S-adenosyl-L-homocysteine + H(+)

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | reasoning-supported | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MAEKQQAVTEFYNNTSPRGAWEFLLGDHLHEGFYDPGTTATISGSQAAAARMIDEALRFANIYDDPSKKPKNMLDIGCGVGGTCVHVAKQYGIQCKGITLSPEEVKCAQGIAKAQGLEEKVSFDVGDALNLPYKDGTFDLVLTIECIEHVQDKEKFIREMIRVAAPGAPIVILSYAHRNLSPSAESLKPDEKKVLKKICDNLALSCLCSSADFVRWLTQLPAEDIKTADWTQNTSPFFPLLMKETFTWKGFTSLLMKGGWTAIKELLALRMMSKAADDGLLKFVAITCRKSK

[Multiple Choices]
A. O-succinyl-L-homoserine + L-cysteine = L,L-cystathionine + succinate + H(+)
B. norajmaline + S-adenosyl-L-methionine = ajmaline + S-adenosyl-L-homocysteine + H(+)
C. 4-hydroxylaminobenzoate + H2O + H(+) = 3,4-dihydroxybenzoate + NH4(+)
D. a 14alpha-methyl steroid + reduced [NADPH--hemoprotein reductase] + O2 = a 14alpha-hydroxymethyl steroid + oxidized [NADPH--hemoprotein reductase] + H2O + H(+)
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

> The supplied sequence exactly matches the reviewed Rauvolfia serpentina protein annotated as norajmaline N-methyltransferase. Its catalytic-activity annotation gives reaction B and cites experimental evidence (ECO:0000269); the historical entry also matches the sequence. The cited studies are not independently evaluated here.

Cited evidence: [C4](#evidence-c4), [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a glycine-rich region, DIGCGVGGTC, consistent with a SAM-binding methyltransferase motif. Of the choices, B alone is a SAM-dependent methyl transfer; the others describe transsulfuration, aromatic hydroxylamine deamination, and P450 oxidation.

**Missing item-specific fact**

> The motif and choices support the methyltransferase reaction class, but the specific substrate pair—norajmaline and ajmaline—and the exact N-methylation require protein-specific functional knowledge.

**Reason**

> A sequence-based motif argument meaningfully distinguishes the only SAM-dependent methylation choice from the other catalytic classes, although it does not independently establish the precise substrate specificity.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> The choices describe distinct reaction classes, and the sequence supports a SAM-dependent methyltransferase rather than the alternatives.

### Important caveats

- Reviewer-only database evidence was not supplied to the evaluated model and is used only to assess whether the key is supported.
- The historical and current database entries match the supplied sequence, but the author's exact source snapshot is unknown.
- The cited experimental evidence codes support the annotation; the underlying primary studies were not independently reviewed.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "catalytic_activity_0139",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed Rauvolfia serpentina protein annotated as norajmaline N-methyltransferase. Its catalytic-activity annotation gives reaction B and cites experimental evidence (ECO:0000269); the historical entry also matches the sequence. The cited studies are not independently evaluated here.",
    "evidence_ids": [
      "C4",
      "C5",
      "H5"
    ]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a glycine-rich region, DIGCGVGGTC, consistent with a SAM-binding methyltransferase motif. Of the choices, B alone is a SAM-dependent methyl transfer; the others describe transsulfuration, aromatic hydroxylamine deamination, and P450 oxidation.",
    "missing_item_specific_fact": "The motif and choices support the methyltransferase reaction class, but the specific substrate pair—norajmaline and ajmaline—and the exact N-methylation require protein-specific functional knowledge.",
    "reason": "A sequence-based motif argument meaningfully distinguishes the only SAM-dependent methylation choice from the other catalytic classes, although it does not independently establish the precise substrate specificity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe distinct reaction classes, and the sequence supports a SAM-dependent methyltransferase rather than the alternatives."
  },
  "important_caveats": [
    "Reviewer-only database evidence was not supplied to the evaluated model and is used only to assess whether the key is supported.",
    "The historical and current database entries match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The cited experimental evidence codes support the annotation; the underlying primary studies were not independently reviewed."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `A0A075D6M1`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 36. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D6M1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:36.783284+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"AHH02781.1","source":"EMBL"}],"value":"Gamma-tocopherol-like methyltransferase NNMT"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38212296","source":"PubMed"}],"value":"2.1.1.392"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"27122470","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"38212296","source":"PubMed"}],"value":"Norajmaline N-methyltransferase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"27122470","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"38212296","source":"PubMed"}],"value":"RsNNMT"}]}}
```

Source SHA-256: `3bb9ffb2ae03473556ed523492c0744d518e1d741d7bd4b3a3fc9dc695f623a9`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D6M1.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:36.783284+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"27122470","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38212296","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:79600"}}],"reaction":{"ecNumber":"2.1.1.392","evidences":[{"evidenceCode":"ECO:0000269","id":"27122470","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38212296","source":"PubMed"}],"name":"norajmaline + S-adenosyl-L-methionine = ajmaline + S-adenosyl-L-homocysteine + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:79599"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57856"},{"database":"ChEBI","id":"CHEBI:58567"},{"database":"ChEBI","id":"CHEBI:59789"},{"database":"ChEBI","id":"CHEBI:77618"}]}}
```

Source SHA-256: `3bb9ffb2ae03473556ed523492c0744d518e1d741d7bd4b3a3fc9dc695f623a9`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D6M1?format=txt&versions=36)  
**Locator:** `lines 51-58`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 36 / 1.  
**Retrieved:** 2026-11-01T06:27:15.852655+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=norajmaline + S-adenosyl-L-methionine = ajmaline + S-adenosyl-
CC         L-homocysteine + H(+); Xref=Rhea:RHEA:79599, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:57856, ChEBI:CHEBI:58567, ChEBI:CHEBI:59789,
CC         ChEBI:CHEBI:77618; EC=2.1.1.392;
CC         Evidence={ECO:0000269|PubMed:27122470, ECO:0000269|PubMed:38212296};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:79600;
CC         Evidence={ECO:0000269|PubMed:27122470, ECO:0000269|PubMed:38212296};
```

Source SHA-256: `ea487ae2513c784ecb9c3536d3436f3ff3869372e436c3eb33f2b9b462f39efa`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json) (zero-based source row 139). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
