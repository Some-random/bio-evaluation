# EC_number_0062

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **C** — 2.7.2.3

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | reasoning-supported | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MSLSNKLAITDVDLKDKRVLIRVDFNVPLDADKKITNNQRIVGALPTIKYAIENGAKAVVLMSHLGRPDGKANPKYSLKPVATELEKLLSKSVIFAENCVGKETEEIVNKATGGQVILLENLRFHAEEEGSSKDAEGKKVKADKEKVEEFRKGLTALGDVYINDAFGTAHRAHSSMVGVDLPQKASGFLVKKELEYFAKALESPQRPFLAILGGAKVSDKIQLIDNLLPKVNSLIITGAMAFTFKKTLENVKIGNSLFDEAGSKIVGDIVEKAKKNNVKIVLPVDYVTADKFAADAKTGYATDADGIPDGYMGLDVGEKSVELYKKTIAEAKTILWNGPPGVFELEPFANATKKTLDAAVAAAQSGSIVIIGGGDTATVAAKYGAEAKLSHVSTGGGASLELLEGKVLPGVDALSSK

[Multiple Choices]
A. 2.7.1.39
B. 2.1.1.348
C. 2.7.2.3
D. 6.3.5.1
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

> The exact sequence matches the UniProt entry annotated as phosphoglycerate kinase, EC 2.7.2.3, with the reaction of 3-phosphoglycerate and ATP also assigned that EC number. The annotation is transferred by similarity from UniProtKB:P00560, so this supports the key but is not direct experimental evidence for this particular protein.

Cited evidence: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 417-aa sequence has an overall pattern consistent with the phosphoglycerate kinase family, including a conserved glycine-rich region near the C-terminus (`...SIVIIGGGDTATV...`). That family assignment supports EC 2.7.2.3 and distinguishes it from the unrelated methyltransferase and ligase choices, as well as the distinct kinase in A.

**Missing item-specific fact**

> No external item-specific fact is necessary for a defensible family-level inference from the sequence, though confirming the exact annotation would ordinarily rely on sequence-family or database analysis.

**Reason**

> The sequence provides meaningful family-level evidence for phosphoglycerate kinase rather than requiring memorization of this exact protein's database entry. The inference is not equivalent to direct experimental verification of its reaction.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> The sequence supports the phosphoglycerate kinase family, and the listed EC number for that enzyme is 2.7.2.3.

### Important caveats

- The UniProt EC and catalytic-activity annotations cite transfer by similarity from P00560 (ECO:0000250), not direct experimental evidence for this exact sequence.
- The reviewer-only evidence matches the supplied sequence, but the author's source snapshot is unknown.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "EC_number_0062",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as phosphoglycerate kinase, EC 2.7.2.3, with the reaction of 3-phosphoglycerate and ATP also assigned that EC number. The annotation is transferred by similarity from UniProtKB:P00560, so this supports the key but is not direct experimental evidence for this particular protein.",
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H4"
    ]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 417-aa sequence has an overall pattern consistent with the phosphoglycerate kinase family, including a conserved glycine-rich region near the C-terminus (`...SIVIIGGGDTATV...`). That family assignment supports EC 2.7.2.3 and distinguishes it from the unrelated methyltransferase and ligase choices, as well as the distinct kinase in A.",
    "missing_item_specific_fact": "No external item-specific fact is necessary for a defensible family-level inference from the sequence, though confirming the exact annotation would ordinarily rely on sequence-family or database analysis.",
    "reason": "The sequence provides meaningful family-level evidence for phosphoglycerate kinase rather than requiring memorization of this exact protein's database entry. The inference is not equivalent to direct experimental verification of its reaction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence supports the phosphoglycerate kinase family, and the listed EC number for that enzyme is 2.7.2.3."
  },
  "important_caveats": [
    "The UniProt EC and catalytic-activity annotations cite transfer by similarity from P00560 (ECO:0000250), not direct experimental evidence for this exact sequence.",
    "The reviewer-only evidence matches the supplied sequence, but the author's source snapshot is unknown."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `A0A7G5KET3`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 18. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7G5KET3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:35.568831+00:00.  

```json
"A0A7G5KET3"
```

Source SHA-256: `79f801166dc030cf4959c0881b37cd1bd39704c428283cc65f9c68002c1fbb5b`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7G5KET3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:35.568831+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P00560","source":"UniProtKB"}],"value":"2.7.2.3"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"RU000532","source":"RuleBase"}],"value":"Phosphoglycerate kinase"}}}
```

Source SHA-256: `79f801166dc030cf4959c0881b37cd1bd39704c428283cc65f9c68002c1fbb5b`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7G5KET3.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:35.568831+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.7.2.3","evidences":[{"evidenceCode":"ECO:0000250","id":"P00560","source":"UniProtKB"}],"name":"(2R)-3-phosphoglycerate + ATP = (2R)-3-phospho-glyceroyl phosphate + ADP","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:14801"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:57604"},{"database":"ChEBI","id":"CHEBI:58272"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `79f801166dc030cf4959c0881b37cd1bd39704c428283cc65f9c68002c1fbb5b`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7G5KET3?format=txt&versions=18)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 18 / 1.  
**Retrieved:** 2026-11-02T04:25:37.377118+00:00.  

```text
DE   RecName: Full=Phosphoglycerate kinase {ECO:0000255|RuleBase:RU000532};
DE            EC=2.7.2.3 {ECO:0000250|UniProtKB:P00560};
```

Source SHA-256: `b429698fb3b322f2fc43bbd8bc72a321c4e8bcf2772d689c13b699dd201233ec`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7G5KET3?format=txt&versions=18)  
**Locator:** `lines 43-47`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 18 / 1.  
**Retrieved:** 2026-11-02T04:25:37.377118+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=(2R)-3-phosphoglycerate + ATP = (2R)-3-phospho-glyceroyl
CC         phosphate + ADP; Xref=Rhea:RHEA:14801, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:57604, ChEBI:CHEBI:58272, ChEBI:CHEBI:456216; EC=2.7.2.3;
CC         Evidence={ECO:0000250|UniProtKB:P00560};
```

Source SHA-256: `b429698fb3b322f2fc43bbd8bc72a321c4e8bcf2772d689c13b699dd201233ec`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json) (zero-based source row 62). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
