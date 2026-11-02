# catalytic_activity_0030

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **C** — ATP + protein L-histidine = ADP + protein N-phospho-L-histidine.

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | reasoning-supported | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MKNRNPLIRKLLTQYFVTTGILLAFLVMIPLVIRFIAGTRTWYGTEPIYYILRFFADRWLFCVAIGALLIWFGTTIYYMTKAIGYLNETIQATTQLIEEPSKRITLSSHLIDVQEEMNQLREKSLQDQRAAKEAEQRKNDLIVYLAHDLRTPLTSVIGYLTLLKEEPQLSNAMRNRYTEIALQKAQRLELLISEFFEITRFNLTTIVLQTETTDLSLMLEQLTFEFLPLLEEKNLNWQLNLQKNVLATVDTEKIARVFDNLIRNAINYSYPDSPLLLELVESDSIHIRLTNRGKTIPEEMIGRLFEPFYRMDSSRATATSGTGLGLPIAKEILLASGGDISAESKDETIIFNVRLPKPANN

[Multiple Choices]
A. N-methyl-3-methoxytyramine + S-adenosyl-L-methionine = N,N-dimethyl-3-methoxytyramine + S-adenosyl-L-homocysteine + H(+)
B. L-homoserine + acetyl-CoA = O-acetyl-L-homoserine + CoA
C. ATP + protein L-histidine = ADP + protein N-phospho-L-histidine.
D. L-homocysteine + H2O = 2-oxobutanoate + hydrogen sulfide + NH4(+) + H(+)
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

> The exact sequence matches a VanSC sensor histidine protein kinase annotation, whose listed catalytic reaction is ATP-dependent phosphorylation of protein histidine, matching C. The annotation is transferred by similarity (ECO:0000250), not direct experimental evidence for this sequence; the cited structure establishes structural study but does not itself demonstrate the reaction.

Cited evidence: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an N-terminal membrane-sensor region with hydrophobic segments followed by a cytoplasmic histidine-kinase region. Sensor histidine kinases use ATP to autophosphorylate a protein histidine, which matches C; the other options describe unrelated methylation, acetylation, or amino-acid degradation reactions.

**Missing item-specific fact**

> No protein-specific annotation is necessary to distinguish these choices at the enzyme-class level, though identifying this exact VanSC protein or verifying its activity experimentally would require external information.

**Reason**

> The sequence architecture and general biochemistry of two-component sensor histidine kinases provide a meaningful basis for selecting C among these choices, rather than relying only on recognition of the exact sequence.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> The listed reactions correspond to distinct enzyme classes, and the sequence supports the sensor histidine-kinase class.

### Important caveats

- The reviewer-only UniProt catalytic-activity annotation is similarity-transferred; it is not direct evidence of an assay on this exact protein.
- The cited structural study concerns a protein fragment and weak ATP binding, not direct validation of the catalytic reaction.
- The author's exact source snapshot is unknown.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "catalytic_activity_0030",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a VanSC sensor histidine protein kinase annotation, whose listed catalytic reaction is ATP-dependent phosphorylation of protein histidine, matching C. The annotation is transferred by similarity (ECO:0000250), not direct experimental evidence for this sequence; the cited structure establishes structural study but does not itself demonstrate the reaction.",
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H4"
    ]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an N-terminal membrane-sensor region with hydrophobic segments followed by a cytoplasmic histidine-kinase region. Sensor histidine kinases use ATP to autophosphorylate a protein histidine, which matches C; the other options describe unrelated methylation, acetylation, or amino-acid degradation reactions.",
    "missing_item_specific_fact": "No protein-specific annotation is necessary to distinguish these choices at the enzyme-class level, though identifying this exact VanSC protein or verifying its activity experimentally would require external information.",
    "reason": "The sequence architecture and general biochemistry of two-component sensor histidine kinases provide a meaningful basis for selecting C among these choices, rather than relying only on recognition of the exact sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The listed reactions correspond to distinct enzyme classes, and the sequence supports the sensor histidine-kinase class."
  },
  "important_caveats": [
    "The reviewer-only UniProt catalytic-activity annotation is similarity-transferred; it is not direct evidence of an assay on this exact protein.",
    "The cited structural study concerns a protein fragment and weak ATP binding, not direct validation of the catalytic reaction.",
    "The author's exact source snapshot is unknown."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `Q9KJT3`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 116. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KJT3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:57.402699+00:00.  

```json
"Q9KJT3"
```

Source SHA-256: `ee33b15ec361df125314162e4a4f908af9fa7205027ed66a72d0e347dc4cb508`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KJT3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:57.402699+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Vancomycin histidine protein kinase"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Vancomycin resistance protein VanSC"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q06240","source":"UniProtKB"}],"value":"2.7.13.3"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Sensor protein VanSC"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"VanS"},{"evidences":[{"evidenceCode":"ECO:0000303","id":"36764524","source":"PubMed"}],"value":"VanSC"}]}}
```

Source SHA-256: `ee33b15ec361df125314162e4a4f908af9fa7205027ed66a72d0e347dc4cb508`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KJT3.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:57.402699+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.7.13.3","evidences":[{"evidenceCode":"ECO:0000250","id":"Q06240","source":"UniProtKB"}],"name":"ATP + protein L-histidine = ADP + protein N-phospho-L-histidine."}}
```

Source SHA-256: `ee33b15ec361df125314162e4a4f908af9fa7205027ed66a72d0e347dc4cb508`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KJT3.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:57.402699+00:00.  

```json
{"citation":{"authors":["Grasty K.C.","Guzik C.","D'Lauro E.J.","Padrick S.B.","Beld J.","Loll P.J."],"citationCrossReferences":[{"database":"PubMed","id":"36764524"},{"database":"DOI","id":"10.1016/j.jbc.2023.103001"}],"citationType":"journal article","firstPage":"103001","id":"36764524","journal":"J. Biol. Chem.","lastPage":"103001","publicationDate":"2023","title":"Structure of VanS from vancomycin-resistant enterococci: A sensor kinase with weak ATP binding.","volume":"299"},"evidences":[{"evidenceCode":"ECO:0007744","id":"8DX0","source":"PDB"}],"referenceNumber":3,"referencePositions":["X-RAY CRYSTALLOGRAPHY (1.45 ANGSTROMS) OF 208-361 IN COMPLEX WITH MG(2+)"]}
```

Source SHA-256: `ee33b15ec361df125314162e4a4f908af9fa7205027ed66a72d0e347dc4cb508`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KJT3?format=txt&versions=116)  
**Locator:** `lines 39-41`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 116 / 1.  
**Retrieved:** 2026-11-02T04:33:04.938411+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=ATP + protein L-histidine = ADP + protein N-phospho-L-
CC         histidine.; EC=2.7.13.3; Evidence={ECO:0000250|UniProtKB:Q06240};
```

Source SHA-256: `3a9c1fbae546e8df9a94d1ae1786bc246e118381f34915268ec1ab8d8786c6af`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json) (zero-based source row 30). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
