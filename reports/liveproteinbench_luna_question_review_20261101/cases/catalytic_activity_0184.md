# catalytic_activity_0184

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **D** — (2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate + H2O

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | reasoning-supported | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MATSSIRSRALGLSRRARFETTRLPFIGRRYKSDETLNRISSKITQPKSQGASQAMLYATGLTEEDMSKAQVGISSVWFEGNPCNMHLNDLSGIVRDSVLRAGLVPMRFNSVGVSDGISMGTAGMRYSLQSRELIADGIETVMNAQWYDANISLPGCDKNMPGVLMAMGRTNRPSIMVYGGSIKPGCSAKGQKLDLVSAFQSYGQFITGQIDETERFDIIRNACPGKGACGGMYTANTLATAIETMGMTVPGSSSCPADDPKKLVECENIGEVVKNMLREEIKPRDVMTRQAFENAMIVVNVLGGSTNAVLHLIAIADSVGIKLTIDDFQAVSDKTPFLADLKPSGKYLMNDLYSIGGTPALLKYLLKEGLIDGSGITVTGKTMKENVASWPDFPADQDIIQPLSNPIKPSGHLQILRGSLAPGGSVGKITGKEGLRFEGTAKCYDYEDAFIESLERGEIKKGEKTVVIIRYEGPKGGPGMPEMLKPSAAIMGAGLGQDVALLTDGRFSGGSHGFLIGHIVPEAMEGGPIALARDGDRIVIDAEEKVVDLDVPTEELDARRKQWKAPPLRYQKGTLKKYCALVSDASHGCVTDGPI

[Multiple Choices]
A. 4-methylnorajmaline + S-adenosyl-L-methionine = 4-methylajmaline + S-adenosyl-L-homocysteine + H(+)
B. okaramine C + 2 reduced [NADPH--hemoprotein reductase] + 2 O2 = okaramine A + 2 oxidized [NADPH--hemoprotein reductase] + 4 H2O + 2 H(+)
C. (19E)-geissoschizine + reduced [NADPH--hemoprotein reductase] + O2 = rhazimal + oxidized [NADPH--hemoprotein reductase] + 2 H2O + H(+)
D. (2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate + H2O
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

> The supplied sequence exactly matches the reviewed UniProt entry annotated as mitochondrial dihydroxy-acid dehydratase (EC 4.2.1.9), and that entry lists the reaction in choice D. The catalytic-activity annotation is transferred from homologs (ECO:0000250), so this supports D as an annotation-based inference, not as direct experimental verification of this exact protein.

Cited evidence: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The long sequence has an N-terminal region consistent with mitochondrial targeting and a cysteine-containing architecture consistent with the iron-sulfur-dependent IlvD/dihydroxy-acid dehydratase family. That family-level inference favors D over the SAM-dependent methylation in A and the P450-type oxidations in B and C, which would require different catalytic machinery.

**Missing item-specific fact**

> No specific database accession or experimentally established activity is supplied; identifying the enzyme family from sequence features is the relevant inference.

**Reason**

> The choices describe substantially different enzyme classes, and sequence family features provide a biological basis to favor the DHAD reaction. This supports family-level discrimination, though the exact substrate reaction is not independently demonstrated by the input alone.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> The options represent distinct transformations, and the sequence-based DHAD-family inference supports D rather than the methylation or oxidative reactions.

### Important caveats

- The reviewer-only UniProt record matches the sequence, but the exact source snapshot used by the question author is unknown.
- The listed catalytic activity is supported by transfer from homolog annotations; the supplied evidence does not establish direct experimental measurement of this protein's activity.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "catalytic_activity_0184",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed UniProt entry annotated as mitochondrial dihydroxy-acid dehydratase (EC 4.2.1.9), and that entry lists the reaction in choice D. The catalytic-activity annotation is transferred from homologs (ECO:0000250), so this supports D as an annotation-based inference, not as direct experimental verification of this exact protein.",
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The long sequence has an N-terminal region consistent with mitochondrial targeting and a cysteine-containing architecture consistent with the iron-sulfur-dependent IlvD/dihydroxy-acid dehydratase family. That family-level inference favors D over the SAM-dependent methylation in A and the P450-type oxidations in B and C, which would require different catalytic machinery.",
    "missing_item_specific_fact": "No specific database accession or experimentally established activity is supplied; identifying the enzyme family from sequence features is the relevant inference.",
    "reason": "The choices describe substantially different enzyme classes, and sequence family features provide a biological basis to favor the DHAD reaction. This supports family-level discrimination, though the exact substrate reaction is not independently demonstrated by the input alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options represent distinct transformations, and the sequence-based DHAD-family inference supports D rather than the methylation or oxidative reactions."
  },
  "important_caveats": [
    "The reviewer-only UniProt record matches the sequence, but the exact source snapshot used by the question author is unknown.",
    "The listed catalytic activity is supported by transfer from homolog annotations; the supplied evidence does not establish direct experimental measurement of this protein's activity."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `A0A0F7TWW9`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 30. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F7TWW9.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:01.826200+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39511739","source":"PubMed"}],"value":"Aspterric acid biosynthesis cluster protein D"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"39511739","source":"PubMed"}],"value":"4.2.1.9"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39511739","source":"PubMed"}],"value":"Dihydroxy-acid dehydratase pbrD, mitochondrial"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"39511739","source":"PubMed"}],"value":"DHAD astD"}]}}
```

Source SHA-256: `9c9db7d008b685b5073a404f2df8618925830622276ec1c773349e5fd3829400`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F7TWW9.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:01.826200+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"Q0CPG9","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:24810"}}],"reaction":{"ecNumber":"4.2.1.9","evidences":[{"evidenceCode":"ECO:0000250","id":"Q0CPG9","source":"UniProtKB"}],"name":"(2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate + H2O","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:24809"},{"database":"ChEBI","id":"CHEBI:11851"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:49072"}]}}
```

Source SHA-256: `9c9db7d008b685b5073a404f2df8618925830622276ec1c773349e5fd3829400`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F7TWW9?format=txt&versions=30)  
**Locator:** `lines 44-50`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 2.  
**Retrieved:** 2026-11-02T04:24:04.510512+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=(2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate
CC         + H2O; Xref=Rhea:RHEA:24809, ChEBI:CHEBI:11851, ChEBI:CHEBI:15377,
CC         ChEBI:CHEBI:49072; EC=4.2.1.9;
CC         Evidence={ECO:0000250|UniProtKB:Q0CPG9};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:24810;
CC         Evidence={ECO:0000250|UniProtKB:Q0CPG9};
```

Source SHA-256: `5c8dba2f186ec2f5c49e223d9e4d0a5408127c4f67b41ce2f7a9d3d700501ce5`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json) (zero-based source row 184). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
