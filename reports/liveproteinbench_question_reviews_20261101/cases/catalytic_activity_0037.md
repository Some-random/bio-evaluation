# catalytic_activity_0037

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **A** — 3-amino-5,6,7,7a-tetrahydro-1H-pyrrolizin-1-one + AH2 = 3-amino-tetrahydro-1H-pyrrolizin-1-ol + A

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTRKSILVTGASSGLGYAAVQKLAENGFYVFAAVREIRGMFSNIKNIKELKLDLANEQSIEELFIYIEATQKDYPLWGLVNNAGICVPSPLELLREFDLRQQLDTNVIGQLLVTQFALPFIRKSKGRIINITSGLGSIAVPYLGAYSIAQFAKMAFTDVLRRELKHSGVTVSVVQPGAIYTPIWDKFLVTGQEILDNSLDEKRKIYERSFIEFLKASQIGVNSVKTTRNDFAKVILDIFKAEIPETHYYVGDDAKNFSNKSKILTVTEIDEWFDLQSPTESEFKKI

[Multiple Choices]
A. 3-amino-5,6,7,7a-tetrahydro-1H-pyrrolizin-1-one + AH2 = 3-amino-tetrahydro-1H-pyrrolizin-1-ol + A
B. O-phospho-L-seryl-[protein] + H2O = L-seryl-[protein] + phosphate
C. dopamine + S-adenosyl-L-methionine = 4-methoxytyramine + S-adenosyl-L-homocysteine + H(+)
D. L-ornithine = L-proline + NH4(+)
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

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied sequence exactly matches the historical and current UniProt sequence annotated as a 3-amino-tetrahydro-pyrrolizinone reductase. Its catalytic-activity annotation gives reaction A and cites experimental evidence (ECO:0000269, PubMed 39428351).

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal glycine-rich sequence is compatible with an oxidoreductase, which could help distinguish reaction A from the phosphatase, methyltransferase, and ornithine-to-proline alternatives. It does not establish the particular pyrrolizinone substrate or reaction.


**Missing item-specific fact**

> The protein-specific catalytic annotation or experimental finding that this enzyme reduces 3-amino-5,6,7,7a-tetrahydro-1H-pyrrolizin-1-one.


**Reason**

> The sequence may suggest a broad enzyme class, but identifying the exact substrate and product requires a protein-specific fact absent from the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched catalytic annotation supports A; the other choices describe different reaction types.


### Important caveats

- The cited evidence code indicates experimental support in the database annotation, but the primary paper was not independently reviewed here.
- The exact author source snapshot is unknown; the matched historical record already contains the catalytic-activity annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal glycine-rich sequence is compatible with an oxidoreductase, which could help distinguish reaction A from the phosphatase, methyltransferase, and ornithine-to-proline alternatives. It does not establish the particular pyrrolizinone substrate or reaction.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific catalytic annotation or experimental finding that this enzyme reduces 3-amino-5,6,7,7a-tetrahydro-1H-pyrrolizin-1-one.",
    "reason": "The sequence may suggest a broad enzyme class, but identifying the exact substrate and product requires a protein-specific fact absent from the question."
  },
  "case_id": "catalytic_activity_0037",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the historical and current UniProt sequence annotated as a 3-amino-tetrahydro-pyrrolizinone reductase. Its catalytic-activity annotation gives reaction A and cites experimental evidence (ECO:0000269, PubMed 39428351)."
  },
  "important_caveats": [
    "The cited evidence code indicates experimental support in the database annotation, but the primary paper was not independently reviewed here.",
    "The exact author source snapshot is unknown; the matched historical record already contains the catalytic-activity annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched catalytic annotation supports A; the other choices describe different reaction types."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0037",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the historical and current UniProt sequence annotated as a 3-amino-tetrahydro-pyrrolizinone reductase. Its catalytic-activity annotation gives reaction A and cites experimental evidence (ECO:0000269, PubMed 39428351).",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal glycine-rich sequence is compatible with an oxidoreductase, which could help distinguish reaction A from the phosphatase, methyltransferase, and ornithine-to-proline alternatives. It does not establish the particular pyrrolizinone substrate or reaction.",
    "missing_item_specific_fact": "The protein-specific catalytic annotation or experimental finding that this enzyme reduces 3-amino-5,6,7,7a-tetrahydro-1H-pyrrolizin-1-one.",
    "reason": "The sequence may suggest a broad enzyme class, but identifying the exact substrate and product requires a protein-specific fact absent from the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched catalytic annotation supports A; the other choices describe different reaction types."
  },
  "important_caveats": [
    "The cited evidence code indicates experimental support in the database annotation, but the primary paper was not independently reviewed here.",
    "The exact author source snapshot is unknown; the matched historical record already contains the catalytic-activity annotation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A2G0QDN4 (XHPD_XENHO) for this exact 286-aa sequence (SHA256 match confirmed) is annotated as '3-amino-tetrahydro-pyrrolizinone reductase' (EC 1.1.-.-) with the catalytic reaction '3-amino-5,6,7,7a-tetrahydro-1H-pyrrolizin-1-one + AH2 = 3-amino-tetrahydro-1H-pyrrolizin-1-ol + A' (RHEA:83311), supported by experimental evidence (ECO:0000269, PubMed:39428351, Angew. Chem. Int. Ed. 2024). The annotation matches Choice A verbatim.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal region contains the canonical SDR (short-chain dehydrogenase/reductase) Rossmann-fold motif 'TGASSGLGY' (TGxxxGxG pattern), and the C-terminal region contains a 'DDAKN' variant of the DDxxD motif, together with a YxxxK-like catalytic tetrad region ('YYVGDDAKN'). These are hallmarks of the SDR family (EC 1.1.1.-/1.1.-.-), which catalyzes NAD(P)H-dependent (AH2) oxidoreductions. Among the four choices, only A is an EC 1.1.-.- reduction using AH2. Choice B is a serine phosphatase (EC 3.1.3.16, no SDR motifs expected), Choice C is a catechol-O-methyltransferase (EC 2.1.1.6, requires SAM-binding motif absent here), and Choice D is a flavin-dependent oxidase (EC 1.4.3.4, uses O2 not AH2). The SDR family features thus meaningfully eliminate B, C, and D.


**Missing item-specific fact**

> The specific obscure substrate (3-amino-5,6,7,7a-tetrahydro-1H-pyrrolizin-1-one, a pyrrolizwilline-pathway intermediate in Xenorhabdus hominickii) cannot be deduced from sequence alone. However, the multiple-choice format only requires selecting among four given reactions, and EC-class reasoning suffices to isolate A.


**Reason**

> A trained biologist can identify SDR-family sequence signatures (TGASSGLGY Rossmann motif, DDxxD C-terminal motif, catalytic tetrad) to assign the enzyme to EC 1.1.-.-, then match the only AH2-dependent oxidoreductase among the choices. This is a concrete, generalizable argument from sequence features to enzyme class, not mere memorization of a database entry. The specific substrate name is obscure, but the question structure (four options) makes EC-class elimination sufficient.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices span four distinct enzyme classes (oxidoreductase EC 1.1, phosphatase EC 3.1, methyltransferase EC 2.1, flavin oxidase EC 1.4). The SDR-like sequence features unambiguously point to EC 1.1.-.- with NAD(P)H (AH2) cofactor, which only Choice A satisfies. No other option is defensible given the sequence evidence.


### Important caveats

- The specific substrate (pyrrolizinone alkaloid intermediate) is extremely obscure and identifiable only through the 2024 Bode lab publication (PubMed:39428351); no sequence-based method would name it de novo.
- The EC number is incomplete (1.1.-.-), indicating the full four-digit classification is not yet assigned, though the reaction is experimentally confirmed.
- The SDR family is very large (>10,000 members); the motifs confirm the family and EC class but not the specific substrate without pathway context.
- All reviewer evidence is UniProt annotation (experimental, ECO:0000269); the primary paper was not independently retrieved for this audit.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal region contains the canonical SDR (short-chain dehydrogenase/reductase) Rossmann-fold motif 'TGASSGLGY' (TGxxxGxG pattern), and the C-terminal region contains a 'DDAKN' variant of the DDxxD motif, together with a YxxxK-like catalytic tetrad region ('YYVGDDAKN'). These are hallmarks of the SDR family (EC 1.1.1.-/1.1.-.-), which catalyzes NAD(P)H-dependent (AH2) oxidoreductions. Among the four choices, only A is an EC 1.1.-.- reduction using AH2. Choice B is a serine phosphatase (EC 3.1.3.16, no SDR motifs expected), Choice C is a catechol-O-methyltransferase (EC 2.1.1.6, requires SAM-binding motif absent here), and Choice D is a flavin-dependent oxidase (EC 1.4.3.4, uses O2 not AH2). The SDR family features thus meaningfully eliminate B, C, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific obscure substrate (3-amino-5,6,7,7a-tetrahydro-1H-pyrrolizin-1-one, a pyrrolizwilline-pathway intermediate in Xenorhabdus hominickii) cannot be deduced from sequence alone. However, the multiple-choice format only requires selecting among four given reactions, and EC-class reasoning suffices to isolate A.",
    "reason": "A trained biologist can identify SDR-family sequence signatures (TGASSGLGY Rossmann motif, DDxxD C-terminal motif, catalytic tetrad) to assign the enzyme to EC 1.1.-.-, then match the only AH2-dependent oxidoreductase among the choices. This is a concrete, generalizable argument from sequence features to enzyme class, not mere memorization of a database entry. The specific substrate name is obscure, but the question structure (four options) makes EC-class elimination sufficient."
  },
  "case_id": "catalytic_activity_0037",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A2G0QDN4 (XHPD_XENHO) for this exact 286-aa sequence (SHA256 match confirmed) is annotated as '3-amino-tetrahydro-pyrrolizinone reductase' (EC 1.1.-.-) with the catalytic reaction '3-amino-5,6,7,7a-tetrahydro-1H-pyrrolizin-1-one + AH2 = 3-amino-tetrahydro-1H-pyrrolizin-1-ol + A' (RHEA:83311), supported by experimental evidence (ECO:0000269, PubMed:39428351, Angew. Chem. Int. Ed. 2024). The annotation matches Choice A verbatim."
  },
  "important_caveats": [
    "The specific substrate (pyrrolizinone alkaloid intermediate) is extremely obscure and identifiable only through the 2024 Bode lab publication (PubMed:39428351); no sequence-based method would name it de novo.",
    "The EC number is incomplete (1.1.-.-), indicating the full four-digit classification is not yet assigned, though the reaction is experimentally confirmed.",
    "The SDR family is very large (>10,000 members); the motifs confirm the family and EC class but not the specific substrate without pathway context.",
    "All reviewer evidence is UniProt annotation (experimental, ECO:0000269); the primary paper was not independently retrieved for this audit."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span four distinct enzyme classes (oxidoreductase EC 1.1, phosphatase EC 3.1, methyltransferase EC 2.1, flavin oxidase EC 1.4). The SDR-like sequence features unambiguously point to EC 1.1.-.- with NAD(P)H (AH2) cofactor, which only Choice A satisfies. No other option is defensible given the sequence evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0037",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A2G0QDN4 (XHPD_XENHO) for this exact 286-aa sequence (SHA256 match confirmed) is annotated as '3-amino-tetrahydro-pyrrolizinone reductase' (EC 1.1.-.-) with the catalytic reaction '3-amino-5,6,7,7a-tetrahydro-1H-pyrrolizin-1-one + AH2 = 3-amino-tetrahydro-1H-pyrrolizin-1-ol + A' (RHEA:83311), supported by experimental evidence (ECO:0000269, PubMed:39428351, Angew. Chem. Int. Ed. 2024). The annotation matches Choice A verbatim.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal region contains the canonical SDR (short-chain dehydrogenase/reductase) Rossmann-fold motif 'TGASSGLGY' (TGxxxGxG pattern), and the C-terminal region contains a 'DDAKN' variant of the DDxxD motif, together with a YxxxK-like catalytic tetrad region ('YYVGDDAKN'). These are hallmarks of the SDR family (EC 1.1.1.-/1.1.-.-), which catalyzes NAD(P)H-dependent (AH2) oxidoreductions. Among the four choices, only A is an EC 1.1.-.- reduction using AH2. Choice B is a serine phosphatase (EC 3.1.3.16, no SDR motifs expected), Choice C is a catechol-O-methyltransferase (EC 2.1.1.6, requires SAM-binding motif absent here), and Choice D is a flavin-dependent oxidase (EC 1.4.3.4, uses O2 not AH2). The SDR family features thus meaningfully eliminate B, C, and D.",
    "missing_item_specific_fact": "The specific obscure substrate (3-amino-5,6,7,7a-tetrahydro-1H-pyrrolizin-1-one, a pyrrolizwilline-pathway intermediate in Xenorhabdus hominickii) cannot be deduced from sequence alone. However, the multiple-choice format only requires selecting among four given reactions, and EC-class reasoning suffices to isolate A.",
    "reason": "A trained biologist can identify SDR-family sequence signatures (TGASSGLGY Rossmann motif, DDxxD C-terminal motif, catalytic tetrad) to assign the enzyme to EC 1.1.-.-, then match the only AH2-dependent oxidoreductase among the choices. This is a concrete, generalizable argument from sequence features to enzyme class, not mere memorization of a database entry. The specific substrate name is obscure, but the question structure (four options) makes EC-class elimination sufficient."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span four distinct enzyme classes (oxidoreductase EC 1.1, phosphatase EC 3.1, methyltransferase EC 2.1, flavin oxidase EC 1.4). The SDR-like sequence features unambiguously point to EC 1.1.-.- with NAD(P)H (AH2) cofactor, which only Choice A satisfies. No other option is defensible given the sequence evidence."
  },
  "important_caveats": [
    "The specific substrate (pyrrolizinone alkaloid intermediate) is extremely obscure and identifiable only through the 2024 Bode lab publication (PubMed:39428351); no sequence-based method would name it de novo.",
    "The EC number is incomplete (1.1.-.-), indicating the full four-digit classification is not yet assigned, though the reaction is experimentally confirmed.",
    "The SDR family is very large (>10,000 members); the motifs confirm the family and EC class but not the specific substrate without pathway context.",
    "All reviewer evidence is UniProt annotation (experimental, ECO:0000269); the primary paper was not independently retrieved for this audit."
  ]
}
```

</details>

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `A0A2G0QDN4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 28. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2G0QDN4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:47.620054+00:00.  

```json
"A0A2G0QDN4"
```

Source SHA-256: `5510f043b076696b57f87efa7739b48cfedb1b8f19f87a14fd6d5a4d3624e099`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2G0QDN4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:47.620054+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39428351","source":"PubMed"}],"value":"1.1.-.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305","id":"39428351","source":"PubMed"}],"value":"3-amino-tetrahydro-pyrrolizinone reductase"}}}
```

Source SHA-256: `5510f043b076696b57f87efa7739b48cfedb1b8f19f87a14fd6d5a4d3624e099`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2G0QDN4.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:47.620054+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"39428351","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:83312"}}],"reaction":{"evidences":[{"evidenceCode":"ECO:0000269","id":"39428351","source":"PubMed"}],"name":"3-amino-5,6,7,7a-tetrahydro-1H-pyrrolizin-1-one + AH2 = 3-amino-tetrahydro-1H-pyrrolizin-1-ol + A","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:83311"},{"database":"ChEBI","id":"CHEBI:13193"},{"database":"ChEBI","id":"CHEBI:17499"},{"database":"ChEBI","id":"CHEBI:232462"},{"database":"ChEBI","id":"CHEBI:232512"}]}}
```

Source SHA-256: `5510f043b076696b57f87efa7739b48cfedb1b8f19f87a14fd6d5a4d3624e099`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2G0QDN4.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:47.620054+00:00.  

```json
{"citation":{"authors":["Effert J.","Westphalen M.","Calderari A.","Shi Y.M.","Elamri I.","Najah S.","Gruen P.","Li Y.","Gruez A.","Weissman K.J.","Bode H.B."],"citationCrossReferences":[{"database":"PubMed","id":"39428351"},{"database":"DOI","id":"10.1002/anie.202411258"}],"citationType":"journal article","firstPage":"e202411258","id":"39428351","journal":"Angew. Chem. Int. Ed.","lastPage":"e202411258","publicationDate":"2024","title":"Pyrrolizwilline, a unique bacterial alkaloid assembled by a nonribosomal peptide synthetase and non-enzymatic dimerization.","volume":"63"},"referenceComments":[{"type":"STRAIN","value":"DSM 17903 / CIP 109072 / KE01"}],"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY"]}
```

Source SHA-256: `5510f043b076696b57f87efa7739b48cfedb1b8f19f87a14fd6d5a4d3624e099`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2G0QDN4?format=txt&versions=28)  
**Locator:** `lines 1-12`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 28 / 1.  
**Retrieved:** 2026-11-02T04:24:49.959850+00:00.  

```text
ID   XHPD_XENHO              Reviewed;         286 AA.
AC   A0A2G0QDN4;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   31-JAN-2018, sequence version 1.
DT   28-JAN-2026, entry version 28.
DE   RecName: Full=3-amino-tetrahydro-pyrrolizinone reductase {ECO:0000305|PubMed:39428351};
DE            EC=1.1.-.- {ECO:0000269|PubMed:39428351};
GN   Name=xhpD; ORFNames=Xhom_00313 {ECO:0000312|EMBL:PHM57347.1};
OS   Xenorhabdus hominickii.
OC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;
OC   Enterobacterales; Morganellaceae; Xenorhabdus.
OX   NCBI_TaxID=351679;
```

Source SHA-256: `e9a43167d987f4d30c210cf3857bc305e9fa0ec071e154f20f0d529315825c29`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2G0QDN4?format=txt&versions=28)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 28 / 1.  
**Retrieved:** 2026-11-02T04:24:49.959850+00:00.  

```text
DE   RecName: Full=3-amino-tetrahydro-pyrrolizinone reductase {ECO:0000305|PubMed:39428351};
DE            EC=1.1.-.- {ECO:0000269|PubMed:39428351};
```

Source SHA-256: `e9a43167d987f4d30c210cf3857bc305e9fa0ec071e154f20f0d529315825c29`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2G0QDN4?format=txt&versions=28)  
**Locator:** `lines 23-31`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 28 / 1.  
**Retrieved:** 2026-11-02T04:24:49.959850+00:00.  

```text
RN   [2]
RP   FUNCTION, AND CATALYTIC ACTIVITY.
RC   STRAIN=DSM 17903 / CIP 109072 / KE01;
RX   PubMed=39428351; DOI=10.1002/anie.202411258;
RA   Effert J., Westphalen M., Calderari A., Shi Y.M., Elamri I., Najah S.,
RA   Gruen P., Li Y., Gruez A., Weissman K.J., Bode H.B.;
RT   "Pyrrolizwilline, a unique bacterial alkaloid assembled by a nonribosomal
RT   peptide synthetase and non-enzymatic dimerization.";
RL   Angew. Chem. Int. Ed. 63:e202411258-e202411258(2024).
```

Source SHA-256: `e9a43167d987f4d30c210cf3857bc305e9fa0ec071e154f20f0d529315825c29`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2G0QDN4?format=txt&versions=28)  
**Locator:** `lines 36-42`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 28 / 1.  
**Retrieved:** 2026-11-02T04:24:49.959850+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=3-amino-5,6,7,7a-tetrahydro-1H-pyrrolizin-1-one + AH2 = 3-
CC         amino-tetrahydro-1H-pyrrolizin-1-ol + A; Xref=Rhea:RHEA:83311,
CC         ChEBI:CHEBI:13193, ChEBI:CHEBI:17499, ChEBI:CHEBI:232462,
CC         ChEBI:CHEBI:232512; Evidence={ECO:0000269|PubMed:39428351};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:83312;
CC         Evidence={ECO:0000269|PubMed:39428351};
```

Source SHA-256: `e9a43167d987f4d30c210cf3857bc305e9fa0ec071e154f20f0d529315825c29`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 37. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
