# catalytic_activity_0140

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **B** — Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MVSFSSLFVAACAAVTAFALPSELEKRAITTSQQGTSNGYFYSFWTNGGGSVSYNNGASGEYSVSWSNCGSFTSGKGWATGSSRNINFSGSFKPSGNAYLAVYGWTTSPLVEYYIMENYGDYNPGRSMTFKGTVTSDGSVYDIYTHQQVNQPSISGTATFEQYWSIRRTKRSSGTVTTANHFKAWASHGMYLGSHNYQIVSTEGYQSSGSSDITVS

[Multiple Choices]
A. UTP + H2O = UDP + phosphate + H(+)
B. Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.
C. guanosine(18) in tRNA + S-adenosyl-L-methionine = 2'-O-methylguanosine(18) in tRNA + S-adenosyl-L-homocysteine + H(+)
D. a 14alpha-formyl steroid + reduced [NADPH--hemoprotein reductase] + O2 = a Delta(14) steroid + formate + oxidized [NADPH--hemoprotein reductase] + H2O + 2 H(+)
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

> The exact supplied sequence matches a UniProt entry annotated as an endo-1,4-beta-xylanase with the reaction in choice B. The catalytic-activity annotation is supported by a PROSITE-ProRule computational assignment, not by experimental evidence shown here.

Cited evidence: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic segment is consistent with a secreted fungal protein, which makes an extracellular xylan hydrolase more plausible than the tRNA methyltransferase or steroid-metabolism options. But secretion and the sequence’s general character do not establish xylan as the substrate or identify the precise reaction.

**Missing item-specific fact**

> The protein-specific functional assignment linking this sequence to endo-1,4-beta-xylanase activity.

**Reason**

> The supplied sequence may support a broad enzyme-family inference, but distinguishing choice B’s specific substrate and bond requires a sequence-family/function annotation or equivalent protein-specific knowledge not provided in the question.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> The choices describe distinct reactions, and the matched protein annotation supports B; no other option is comparably supported by the supplied information.

### Important caveats

- The cited catalytic-activity assignment is computational (PROSITE-ProRule); the supplied evidence does not independently establish experimental validation.
- The sequence match is exact, but the author’s original source snapshot is unknown.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "catalytic_activity_0140",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence matches a UniProt entry annotated as an endo-1,4-beta-xylanase with the reaction in choice B. The catalytic-activity annotation is supported by a PROSITE-ProRule computational assignment, not by experimental evidence shown here.",
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a secreted fungal protein, which makes an extracellular xylan hydrolase more plausible than the tRNA methyltransferase or steroid-metabolism options. But secretion and the sequence’s general character do not establish xylan as the substrate or identify the precise reaction.",
    "missing_item_specific_fact": "The protein-specific functional assignment linking this sequence to endo-1,4-beta-xylanase activity.",
    "reason": "The supplied sequence may support a broad enzyme-family inference, but distinguishing choice B’s specific substrate and bond requires a sequence-family/function annotation or equivalent protein-specific knowledge not provided in the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe distinct reactions, and the matched protein annotation supports B; no other option is comparably supported by the supplied information."
  },
  "important_caveats": [
    "The cited catalytic-activity assignment is computational (PROSITE-ProRule); the supplied evidence does not independently establish experimental validation.",
    "The sequence match is exact, but the author’s original source snapshot is unknown."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `K9GHZ3`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 51. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/K9GHZ3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:58.976117+00:00.  

```json
"K9GHZ3"
```

Source SHA-256: `170b7f8687f590c7c152973565082d8026492fbc644d9dd85e58b3a122df0fde`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/K9GHZ3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:58.976117+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39718348","source":"PubMed"}],"value":"Endo-1,4-beta-xylanase EIX"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01097","source":"PROSITE-ProRule"}],"value":"3.2.1.8"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39718348","source":"PubMed"}],"value":"Ethylene-inducing xylanase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"39718348","source":"PubMed"}],"value":"EIX"}]}}
```

Source SHA-256: `170b7f8687f590c7c152973565082d8026492fbc644d9dd85e58b3a122df0fde`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/K9GHZ3.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:58.976117+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.1.8","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01097","source":"PROSITE-ProRule"}],"name":"Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans."}}
```

Source SHA-256: `170b7f8687f590c7c152973565082d8026492fbc644d9dd85e58b3a122df0fde`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/K9GHZ3?format=txt&versions=51)  
**Locator:** `lines 41-43`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-02T04:29:01.625551+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.;
CC         EC=3.2.1.8; Evidence={ECO:0000255|PROSITE-ProRule:PRU01097};
```

Source SHA-256: `c2648a20cf028f996aa5ec7b289a710072e22c44b057d60605b157f60e307ce3`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json) (zero-based source row 140). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
