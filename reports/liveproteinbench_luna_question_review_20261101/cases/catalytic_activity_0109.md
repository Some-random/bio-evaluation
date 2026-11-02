# catalytic_activity_0109

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **C** — Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues with release of alpha-D-glucose.

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MKTFAPLLATLLLAGFGSALQWWEHGNFYQVYPRSFKDSDGNGIGDLDGVTEKLQYLKDVGMDGIWLSPIFASPMADFGYDISDFYNIQGEYGDLAAFERLSAKCKELGLRLILDFVPNHTSNQHEYFKKSVQKEDPYTNYYVWHPGVTNEDGTKSPPSNWISVFRGSAWEWNEDRQEYYLHQFLKEQPDLNYRDPALVEEMKNVLKFWLNKGVSGFRIDAVPYLFESVEVENRYVDEPLSRATDDAENPAYLIHNQTMDQPETYDMIYQWRAVLDEFTAKDNQTRIMMTEGYTSIPNVMKFFGEGEQNGAQIPFNFQMISNLRKTSTAADFARYANLWLDNLPAGRRSNWVLGNHDNNRIGSRLGEAKIDLYNIALQTLPDIAVTYYGEEIGMVDQPIPFNETVDPAGLRAGPDDYTLYSRDPARTPMQWNSDKNAGFSSADKTWLPVATNYKQLNVKAQDAAQKSHLKLFKRLTTYRKRQILTHGDLDLRTTDSNLVLYKRKVDKVGYVVVVLNFSDEPQSLAAIKQQFPGADDRLQVVASSKLVTIKDNKWINVADTELPGESAIVLQKLWGPNPVVVYEA

[Multiple Choices]
A. N-methyl-4-hydroxy-3,5-dimethoxyphenethylamine + S-adenosyl-L-methionine = N,N-dimethyl-4-hydroxy-3,5-dimethoxyphenethylamine + S-adenosyl-L-homocysteine + H(+)
B. AH2 + 2 S-adenosyl-L-methionine = 2 5'-deoxyadenosin-5'-yl radical + 2 L-methionine + A + 2 H(+)
C. Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues with release of alpha-D-glucose.
D. beta-nicotinamide D-ribonucleotide + ATP + H(+) = diphosphate + NAD(+)
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

> The exact sequence matches UniProt entry B0XAA1, annotated as salivary alpha-glucosidase with the reaction in choice C. The catalytic-activity annotation carries experimental evidence codes linked to two publications, though those studies were not independently reviewed here.

Cited evidence: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal signal peptide is consistent with a secreted protein and makes the cytosolic-enzyme alternatives less plausible, but it does not establish the enzyme's substrate specificity or exact reaction.

**Missing item-specific fact**

> The supplied input does not provide this protein's experimentally established alpha-glucosidase activity or an identification linking it to that catalytic annotation.

**Reason**

> Selecting the precise hydrolysis reaction requires protein-specific functional knowledge or a reliable family/annotation match. General sequence context alone does not establish hydrolysis of terminal alpha-D-glucose residues.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> The choices describe distinct enzyme activities, and the sequence-matched annotation supports C.

### Important caveats

- The cited database evidence is reviewer-only and was not available to the evaluated model.
- The UniProt annotation cites experimental evidence, but the underlying papers were not independently assessed.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "catalytic_activity_0109",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt entry B0XAA1, annotated as salivary alpha-glucosidase with the reaction in choice C. The catalytic-activity annotation carries experimental evidence codes linked to two publications, though those studies were not independently reviewed here.",
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H5"
    ]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal signal peptide is consistent with a secreted protein and makes the cytosolic-enzyme alternatives less plausible, but it does not establish the enzyme's substrate specificity or exact reaction.",
    "missing_item_specific_fact": "The supplied input does not provide this protein's experimentally established alpha-glucosidase activity or an identification linking it to that catalytic annotation.",
    "reason": "Selecting the precise hydrolysis reaction requires protein-specific functional knowledge or a reliable family/annotation match. General sequence context alone does not establish hydrolysis of terminal alpha-D-glucose residues."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe distinct enzyme activities, and the sequence-matched annotation supports C."
  },
  "important_caveats": [
    "The cited database evidence is reviewer-only and was not available to the evaluated model.",
    "The UniProt annotation cites experimental evidence, but the underlying papers were not independently assessed."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `B0XAA1`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 92. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0XAA1.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:15.565561+00:00.  

```json
"B0XAA1"
```

Source SHA-256: `9afccd0935d9c913183f609d3d8afcc2196f79187f5d0532d2ba6ed0e5048c10`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0XAA1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:15.565561+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"25746591","source":"PubMed"}],"value":"CQMalI"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"25746591","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38428508","source":"PubMed"}],"value":"3.2.1.20"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38428508","source":"PubMed"}],"value":"Salivary alpha-glucosidase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"38428508","source":"PubMed"}],"value":"CxGluc"}]}}
```

Source SHA-256: `9afccd0935d9c913183f609d3d8afcc2196f79187f5d0532d2ba6ed0e5048c10`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0XAA1.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:15.565561+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.1.20","evidences":[{"evidenceCode":"ECO:0000269","id":"25746591","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38428508","source":"PubMed"}],"name":"Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues with release of alpha-D-glucose."}}
```

Source SHA-256: `9afccd0935d9c913183f609d3d8afcc2196f79187f5d0532d2ba6ed0e5048c10`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0XAA1?format=txt&versions=92)  
**Locator:** `lines 56-59`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 92 / 1.  
**Retrieved:** 2026-11-02T04:27:18.547256+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-
CC         glucose residues with release of alpha-D-glucose.; EC=3.2.1.20;
CC         Evidence={ECO:0000269|PubMed:25746591, ECO:0000269|PubMed:38428508};
```

Source SHA-256: `5fda9ac6361a740657451da46434a8060a2e37043092db9553e846bf116af583`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json) (zero-based source row 109). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
