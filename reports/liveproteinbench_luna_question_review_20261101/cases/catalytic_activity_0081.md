# catalytic_activity_0081

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **C** — L-homoserine + ATP = O-phospho-L-homoserine + ADP + H(+)

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MPARKYKIHVPCTSANIGPGFDVCGIALSLSLSLVVTIPSVSSGAEPLPKIIYTGLDSDNVPLSPYKNLLTRVALYVLRANGITTFPPGVTIEARNEIPFGRGLGSSGAAVIAGVLLGDLLGNLSLPKSRLLDFALMVERHPDNVTAALMGGFVGSYLRELSPEDMSAASIPLAEVLPEYPPDAGPDWGKSPPQPPHGIGHFVRFGWAKEIKAIAVSPRFELATAKARGVLPESYSRKDMIFNLQRLAVLTTALARSPPDPDLIYDAMGDRVHQPYRMTLIPGLPKILSTLTPTSHPGLLGICLSGAGPTILALATHNFEAIANEIERIFGDEQVLVDHKVLNIDEKGSWVEDITEA

[Multiple Choices]
A. O-phospho-L-seryl-[protein] + H2O = L-seryl-[protein] + phosphate
B. 3-O-beta-D-glucosyl-D-glucuronate + phosphate = aldehydo-D-glucuronate + alpha-D-glucose 1-phosphate
C. L-homoserine + ATP = O-phospho-L-homoserine + ADP + H(+)
D. dTMP + ATP = dTDP + ADP
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

> The supplied sequence exactly matches the UniProt entry annotated as homoserine kinase, with the listed reaction matching choice C. The reaction annotation is transferred by similarity from UniProtKB:P17423 (ECO:0000250), so it supports the key as a database-based functional assignment, not as direct experimental evidence for this sequence.

Cited evidence: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence could suggest an ATP-dependent enzyme, which may help distinguish kinase-type choices from the phosphatase or phosphorylase options. But that broad inference does not establish homoserine as the substrate rather than the alternative kinase substrate in choice D.

**Missing item-specific fact**

> The protein-specific assignment as homoserine kinase, including its substrate specificity for L-homoserine, is not supplied in the question.

**Reason**

> Choosing C over the other kinase option requires protein-specific functional annotation or equivalent external knowledge; general sequence-level kinase clues do not identify the precise reaction.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> The reaction choices are distinct, and the matched protein annotation specifically supports choice C.

### Important caveats

- The annotation evidence is transferred by similarity rather than presented as a direct experimental measurement of this protein's catalytic activity.
- Reviewer-only accession and annotation evidence establishes support for the key but was absent from the evaluated input.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "catalytic_activity_0081",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as homoserine kinase, with the listed reaction matching choice C. The reaction annotation is transferred by similarity from UniProtKB:P17423 (ECO:0000250), so it supports the key as a database-based functional assignment, not as direct experimental evidence for this sequence.",
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H4"
    ]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence could suggest an ATP-dependent enzyme, which may help distinguish kinase-type choices from the phosphatase or phosphorylase options. But that broad inference does not establish homoserine as the substrate rather than the alternative kinase substrate in choice D.",
    "missing_item_specific_fact": "The protein-specific assignment as homoserine kinase, including its substrate specificity for L-homoserine, is not supplied in the question.",
    "reason": "Choosing C over the other kinase option requires protein-specific functional annotation or equivalent external knowledge; general sequence-level kinase clues do not identify the precise reaction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reaction choices are distinct, and the matched protein annotation specifically supports choice C."
  },
  "important_caveats": [
    "The annotation evidence is transferred by similarity rather than presented as a direct experimental measurement of this protein's catalytic activity.",
    "Reviewer-only accession and annotation evidence establishes support for the key but was absent from the evaluated input."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `J9VU26`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 51. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VU26.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:11.100039+00:00.  

```json
"J9VU26"
```

Source SHA-256: `0e9afaf34be107a1ef4697a7739b7135416509845602d34b04e02d7fb3acefe1`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VU26.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:11.100039+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P17423","source":"UniProtKB"}],"value":"2.7.1.39"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Homoserine kinase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"HK"},{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"HSK"}]}}
```

Source SHA-256: `0e9afaf34be107a1ef4697a7739b7135416509845602d34b04e02d7fb3acefe1`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VU26.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:11.100039+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"P17423","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:13986"}}],"reaction":{"ecNumber":"2.7.1.39","evidences":[{"evidenceCode":"ECO:0000250","id":"P17423","source":"UniProtKB"}],"name":"L-homoserine + ATP = O-phospho-L-homoserine + ADP + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:13985"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:57476"},{"database":"ChEBI","id":"CHEBI:57590"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `0e9afaf34be107a1ef4697a7739b7135416509845602d34b04e02d7fb3acefe1`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VU26?format=txt&versions=51)  
**Locator:** `lines 1-17`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-01T06:28:15.320227+00:00.  

```text
ID   KHSE_CRYN9              Reviewed;         357 AA.
AC   J9VU26; B2MVI2;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   28-NOV-2012, sequence version 1.
DT   28-JAN-2026, entry version 51.
DE   RecName: Full=Homoserine kinase {ECO:0000305};
DE            Short=HK {ECO:0000305};
DE            Short=HSK {ECO:0000305};
DE            EC=2.7.1.39 {ECO:0000250|UniProtKB:P17423};
GN   Name=THR1 {ECO:0000303|PubMed:18757810};
GN   ORFNames=CNAG_04156 {ECO:0000312|EMBL:AFR96886.1};
OS   Cryptococcus neoformans (strain H99 / ATCC 208821 / CBS 10515 / FGSC 9487)
OS   (Cryptococcus neoformans var. grubii serotype A).
OC   Eukaryota; Fungi; Dikarya; Basidiomycota; Agaricomycotina; Tremellomycetes;
OC   Tremellales; Cryptococcaceae; Cryptococcus;
OC   Cryptococcus neoformans species complex.
OX   NCBI_TaxID=235443 {ECO:0000312|Proteomes:UP000010091};
```

Source SHA-256: `fc5fc0e459f5fad429e5682de28d956b045a7721e17c0769394b8a51086bfc87`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VU26?format=txt&versions=51)  
**Locator:** `lines 45-51`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-01T06:28:15.320227+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-homoserine + ATP = O-phospho-L-homoserine + ADP + H(+);
CC         Xref=Rhea:RHEA:13985, ChEBI:CHEBI:15378, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:57476, ChEBI:CHEBI:57590, ChEBI:CHEBI:456216;
CC         EC=2.7.1.39; Evidence={ECO:0000250|UniProtKB:P17423};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:13986;
CC         Evidence={ECO:0000250|UniProtKB:P17423};
```

Source SHA-256: `fc5fc0e459f5fad429e5682de28d956b045a7721e17c0769394b8a51086bfc87`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json) (zero-based source row 81). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
