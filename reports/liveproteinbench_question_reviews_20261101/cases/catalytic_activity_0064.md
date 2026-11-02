# catalytic_activity_0064

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **A** — rhazimol + NADP(+) = rhazimal + NADPH + 2 H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MEKQVQMPEVELNSDHKMPLVGFGTCIPDPIPPLEELATIFLEVIKVGYRHFDTASCYGTEEALGKAVAQAIESGLVNGREEFFITSKLWVEDADQDLILPALKKTLGNLGLDYLDLYLIHMPLRLRQGAEMFKYTKEDFLPFDIKGTWKAMEECSKLGLCKSIGVSNYSCEKLSKLLENATILPAVNQVEMNVVWKQSKLLPFCKEKNIHVSAWSPLLSYGSIWSQNAVMENTVLVDIAASKSKTVAQVALRWIYEQGASFIMRTFNKERMYQNVQIFDWELTQEELDQIQQIPQRRSNLAEAFVHPEGPIKSVEELWDGDL

[Multiple Choices]
A. rhazimol + NADP(+) = rhazimal + NADPH + 2 H(+)
B. N-methylmescaline + S-adenosyl-L-methionine = N,N-dimethylmescaline + S-adenosyl-L-homocysteine + H(+)
C. 12-deshydroxyl okaramine E + 2 reduced [NADPH--hemoprotein reductase] + 2 O2 = 3-desmethyl okaramine B + 2 oxidized [NADPH--hemoprotein reductase] + 2 H2O + 2 H(+)
D. deacetylisoipecoside + S-adenosyl-L-methionine = 7-O-methyldeacetylisoipecoside + S-adenosyl-L-homocysteine + H(+)
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

> The supplied sequence exactly matches the UniProt entry annotated with the reaction in choice A. That catalytic-activity annotation cites experimental evidence (ECO:0000269; PubMed:36349266), although the primary paper was not independently reviewed here.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C6](#evidence-c6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may support identifying a broad enzyme class, which could help distinguish an oxidoreductase from methyltransferases or an oxygenase. It does not, from the supplied information alone, establish the particular alkaloid substrate and product named in choice A.


**Missing item-specific fact**

> The protein-specific functional annotation or experimental identification of this sequence as catalyzing the rhazimol/rhazimal reaction.


**Reason**

> Selecting the exact reaction requires substrate-specific knowledge not supplied by the sequence context or question. Recognizing the exact protein or retrieving its annotation would be lookup, not reasoning from the provided input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices describe distinct reaction types, and the matched annotation supports choice A.


### Important caveats

- The sequence match and functional annotation are reviewer-only evidence and were not supplied to the evaluated model.
- UniProt records the physiological direction as right-to-left; this does not contradict the reaction equation stated in choice A.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may support identifying a broad enzyme class, which could help distinguish an oxidoreductase from methyltransferases or an oxygenase. It does not, from the supplied information alone, establish the particular alkaloid substrate and product named in choice A.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental identification of this sequence as catalyzing the rhazimol/rhazimal reaction.",
    "reason": "Selecting the exact reaction requires substrate-specific knowledge not supplied by the sequence context or question. Recognizing the exact protein or retrieving its annotation would be lookup, not reasoning from the provided input."
  },
  "case_id": "catalytic_activity_0064",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated with the reaction in choice A. That catalytic-activity annotation cites experimental evidence (ECO:0000269; PubMed:36349266), although the primary paper was not independently reviewed here."
  },
  "important_caveats": [
    "The sequence match and functional annotation are reviewer-only evidence and were not supplied to the evaluated model.",
    "UniProt records the physiological direction as right-to-left; this does not contradict the reaction equation stated in choice A."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe distinct reaction types, and the matched annotation supports choice A."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0064",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated with the reaction in choice A. That catalytic-activity annotation cites experimental evidence (ECO:0000269; PubMed:36349266), although the primary paper was not independently reviewed here.",
    "evidence_ids": ["C5", "H4", "C6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may support identifying a broad enzyme class, which could help distinguish an oxidoreductase from methyltransferases or an oxygenase. It does not, from the supplied information alone, establish the particular alkaloid substrate and product named in choice A.",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental identification of this sequence as catalyzing the rhazimol/rhazimal reaction.",
    "reason": "Selecting the exact reaction requires substrate-specific knowledge not supplied by the sequence context or question. Recognizing the exact protein or retrieving its annotation would be lookup, not reasoning from the provided input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe distinct reaction types, and the matched annotation supports choice A."
  },
  "important_caveats": [
    "The sequence match and functional annotation are reviewer-only evidence and were not supplied to the evaluated model.",
    "UniProt records the physiological direction as right-to-left; this does not contradict the reaction equation stated in choice A."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein sequence (323 aa) matches UniProt entry A0A9E7S5B9 (Rhazimal reductase 2, AsRHR2, EC 1.1.1.440) with exact sequence identity in both current and historical records. The catalytic activity is annotated as 'rhazimol + NADP(+) = rhazimal + NADPH + 2 H(+)' with experimental evidence code ECO:0000269 (inferred from direct assay) from PubMed:36349266 (Wang et al., Chem. Sci. 2022). The expected answer text matches the annotation verbatim.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The four choices represent three distinct enzyme classes: (A) NADP-dependent dehydrogenase/reductase, (B and D) SAM-dependent methyltransferases, and (C) a cytochrome P450 monooxygenase (hemoprotein reductase). The 323-aa sequence length is incompatible with a P450 (typically 500+ aa with a conserved heme-ligating Cys in the FxxGxxxCxG motif, absent here). The sequence lacks the canonical SAM-binding motifs and the fold architecture expected of methyltransferases (eliminating B and D). The sequence length, composition, and presence of NAD(P)-binding-like GxxxG patterns are consistent with a short-chain dehydrogenase/reductase (SDR) family oxidoreductase, making A the only option matching the enzyme class. Elimination of the three non-oxidoreductase choices provides meaningful grounds to select A.


**Missing item-specific fact**

> The specific substrate names 'rhazimol' and 'rhazimal' (specialized monoterpenoid indole alkaloids from Alstonia scholaris) cannot be deduced from sequence alone; however, since only one option is an NADP-dependent oxidoreductase reaction, the specific substrate identity is not required to distinguish the correct choice from the distractors at the enzyme-class level.


**Reason**

> While the exact substrate (rhazimol) is an item-specific fact, the question is answerable by recognizing that the sequence encodes an oxidoreductase rather than a methyltransferase or P450. The length constraint (323 aa vs. ~500+ for P450), absence of heme-binding motifs, and absence of SAM-binding architecture allow elimination of B, C, and D through general enzymology knowledge. Only option A is an NADP-dependent dehydrogenase/reductase reaction, matching the inferred enzyme class.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span three clearly distinct enzyme classes (oxidoreductase, methyltransferase ×2, P450). Given the sequence features, only the oxidoreductase option (A) is consistent with the protein's inferred family. No ambiguity exists among the choices at the enzyme-class level.


### Important caveats

- The physiological direction of the enzyme is right-to-left (reduction of rhazimal to rhazimol), but the reaction is written in the standard EC oxidation direction as annotated in UniProt. This is conventional and does not affect correctness.
- Specific substrate identification (rhazimol/rhazimal) requires database lookup or prior knowledge of Alstonia scholaris alkaloid biosynthesis; the reasoning argument operates at the enzyme-class level.
- The sequence does not display the most canonical SDR motif (TGxxxGG) prominently, so positive identification as an SDR is less certain than the negative elimination of P450 and methyltransferase classes.
- All reviewer evidence is from UniProt annotation with experimental evidence codes; the primary paper (PubMed:36349266) was not independently validated in this audit.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The four choices represent three distinct enzyme classes: (A) NADP-dependent dehydrogenase/reductase, (B and D) SAM-dependent methyltransferases, and (C) a cytochrome P450 monooxygenase (hemoprotein reductase). The 323-aa sequence length is incompatible with a P450 (typically 500+ aa with a conserved heme-ligating Cys in the FxxGxxxCxG motif, absent here). The sequence lacks the canonical SAM-binding motifs and the fold architecture expected of methyltransferases (eliminating B and D). The sequence length, composition, and presence of NAD(P)-binding-like GxxxG patterns are consistent with a short-chain dehydrogenase/reductase (SDR) family oxidoreductase, making A the only option matching the enzyme class. Elimination of the three non-oxidoreductase choices provides meaningful grounds to select A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific substrate names 'rhazimol' and 'rhazimal' (specialized monoterpenoid indole alkaloids from Alstonia scholaris) cannot be deduced from sequence alone; however, since only one option is an NADP-dependent oxidoreductase reaction, the specific substrate identity is not required to distinguish the correct choice from the distractors at the enzyme-class level.",
    "reason": "While the exact substrate (rhazimol) is an item-specific fact, the question is answerable by recognizing that the sequence encodes an oxidoreductase rather than a methyltransferase or P450. The length constraint (323 aa vs. ~500+ for P450), absence of heme-binding motifs, and absence of SAM-binding architecture allow elimination of B, C, and D through general enzymology knowledge. Only option A is an NADP-dependent dehydrogenase/reductase reaction, matching the inferred enzyme class."
  },
  "case_id": "catalytic_activity_0064",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The protein sequence (323 aa) matches UniProt entry A0A9E7S5B9 (Rhazimal reductase 2, AsRHR2, EC 1.1.1.440) with exact sequence identity in both current and historical records. The catalytic activity is annotated as 'rhazimol + NADP(+) = rhazimal + NADPH + 2 H(+)' with experimental evidence code ECO:0000269 (inferred from direct assay) from PubMed:36349266 (Wang et al., Chem. Sci. 2022). The expected answer text matches the annotation verbatim."
  },
  "important_caveats": [
    "The physiological direction of the enzyme is right-to-left (reduction of rhazimal to rhazimol), but the reaction is written in the standard EC oxidation direction as annotated in UniProt. This is conventional and does not affect correctness.",
    "Specific substrate identification (rhazimol/rhazimal) requires database lookup or prior knowledge of Alstonia scholaris alkaloid biosynthesis; the reasoning argument operates at the enzyme-class level.",
    "The sequence does not display the most canonical SDR motif (TGxxxGG) prominently, so positive identification as an SDR is less certain than the negative elimination of P450 and methyltransferase classes.",
    "All reviewer evidence is from UniProt annotation with experimental evidence codes; the primary paper (PubMed:36349266) was not independently validated in this audit."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three clearly distinct enzyme classes (oxidoreductase, methyltransferase ×2, P450). Given the sequence features, only the oxidoreductase option (A) is consistent with the protein's inferred family. No ambiguity exists among the choices at the enzyme-class level."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0064",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein sequence (323 aa) matches UniProt entry A0A9E7S5B9 (Rhazimal reductase 2, AsRHR2, EC 1.1.1.440) with exact sequence identity in both current and historical records. The catalytic activity is annotated as 'rhazimol + NADP(+) = rhazimal + NADPH + 2 H(+)' with experimental evidence code ECO:0000269 (inferred from direct assay) from PubMed:36349266 (Wang et al., Chem. Sci. 2022). The expected answer text matches the annotation verbatim.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The four choices represent three distinct enzyme classes: (A) NADP-dependent dehydrogenase/reductase, (B and D) SAM-dependent methyltransferases, and (C) a cytochrome P450 monooxygenase (hemoprotein reductase). The 323-aa sequence length is incompatible with a P450 (typically 500+ aa with a conserved heme-ligating Cys in the FxxGxxxCxG motif, absent here). The sequence lacks the canonical SAM-binding motifs and the fold architecture expected of methyltransferases (eliminating B and D). The sequence length, composition, and presence of NAD(P)-binding-like GxxxG patterns are consistent with a short-chain dehydrogenase/reductase (SDR) family oxidoreductase, making A the only option matching the enzyme class. Elimination of the three non-oxidoreductase choices provides meaningful grounds to select A.",
    "missing_item_specific_fact": "The specific substrate names 'rhazimol' and 'rhazimal' (specialized monoterpenoid indole alkaloids from Alstonia scholaris) cannot be deduced from sequence alone; however, since only one option is an NADP-dependent oxidoreductase reaction, the specific substrate identity is not required to distinguish the correct choice from the distractors at the enzyme-class level.",
    "reason": "While the exact substrate (rhazimol) is an item-specific fact, the question is answerable by recognizing that the sequence encodes an oxidoreductase rather than a methyltransferase or P450. The length constraint (323 aa vs. ~500+ for P450), absence of heme-binding motifs, and absence of SAM-binding architecture allow elimination of B, C, and D through general enzymology knowledge. Only option A is an NADP-dependent dehydrogenase/reductase reaction, matching the inferred enzyme class."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three clearly distinct enzyme classes (oxidoreductase, methyltransferase ×2, P450). Given the sequence features, only the oxidoreductase option (A) is consistent with the protein's inferred family. No ambiguity exists among the choices at the enzyme-class level."
  },
  "important_caveats": [
    "The physiological direction of the enzyme is right-to-left (reduction of rhazimal to rhazimol), but the reaction is written in the standard EC oxidation direction as annotated in UniProt. This is conventional and does not affect correctness.",
    "Specific substrate identification (rhazimol/rhazimal) requires database lookup or prior knowledge of Alstonia scholaris alkaloid biosynthesis; the reasoning argument operates at the enzyme-class level.",
    "The sequence does not display the most canonical SDR motif (TGxxxGG) prominently, so positive identification as an SDR is less certain than the negative elimination of P450 and methyltransferase classes.",
    "All reviewer evidence is from UniProt annotation with experimental evidence codes; the primary paper (PubMed:36349266) was not independently validated in this audit."
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

**Accession:** `A0A9E7S5B9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 13. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S5B9.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:54.300761+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"36349266","source":"PubMed"}],"value":"1.1.1.440"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"36349266","source":"PubMed"}],"value":"Rhazimal reductase 2"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"36349266","source":"PubMed"}],"value":"AsRHR2"}]}}
```

Source SHA-256: `1c08163802b289b90c328d14948f43d22b2f958ae0fc9ab7cce8f8e6c8cfdb11`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S5B9.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:54.300761+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"right-to-left","evidences":[{"evidenceCode":"ECO:0000269","id":"36349266","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:79617"}}],"reaction":{"ecNumber":"1.1.1.440","evidences":[{"evidenceCode":"ECO:0000269","id":"36349266","source":"PubMed"}],"name":"rhazimol + NADP(+) = rhazimal + NADPH + 2 H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:79615"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57783"},{"database":"ChEBI","id":"CHEBI:58349"},{"database":"ChEBI","id":"CHEBI:230473"},{"database":"ChEBI","id":"CHEBI:230474"}]}}
```

Source SHA-256: `1c08163802b289b90c328d14948f43d22b2f958ae0fc9ab7cce8f8e6c8cfdb11`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S5B9.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:54.300761+00:00.  

```json
{"citation":{"authors":["Wang Z.","Xiao Y.","Wu S.","Chen J.","Li A.","Tatsis E.C."],"citationCrossReferences":[{"database":"PubMed","id":"36349266"},{"database":"DOI","id":"10.1039/d2sc03612f"}],"citationType":"journal article","firstPage":"12389","id":"36349266","journal":"Chem. Sci.","lastPage":"12395","publicationDate":"2022","title":"Deciphering and reprogramming the cyclization regioselectivity in bifurcation of indole alkaloid biosynthesis.","volume":"13"},"evidences":[{"evidenceCode":"ECO:0000312","id":"URS65386.1","source":"EMBL"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","CATALYTIC ACTIVITY","PATHWAY","BIOPHYSICOCHEMICAL PROPERTIES"]}
```

Source SHA-256: `1c08163802b289b90c328d14948f43d22b2f958ae0fc9ab7cce8f8e6c8cfdb11`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S5B9?format=txt&versions=13)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 13 / 1.  
**Retrieved:** 2026-11-01T06:27:37.410633+00:00.  

```text
DE   RecName: Full=Rhazimal reductase 2 {ECO:0000303|PubMed:36349266};
DE            Short=AsRHR2 {ECO:0000303|PubMed:36349266};
DE            EC=1.1.1.440 {ECO:0000269|PubMed:36349266};
```

Source SHA-256: `e4dda31c04daf5f332a19bce2a18fad48f65a392722189ae93f6d3e440e89922`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S5B9?format=txt&versions=13)  
**Locator:** `lines 16-23`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 13 / 1.  
**Retrieved:** 2026-11-01T06:27:37.410633+00:00.  

```text
RN   [1] {ECO:0000312|EMBL:URS65386.1}
RP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, PATHWAY, AND
RP   BIOPHYSICOCHEMICAL PROPERTIES.
RX   PubMed=36349266; DOI=10.1039/d2sc03612f;
RA   Wang Z., Xiao Y., Wu S., Chen J., Li A., Tatsis E.C.;
RT   "Deciphering and reprogramming the cyclization regioselectivity in
RT   bifurcation of indole alkaloid biosynthesis.";
RL   Chem. Sci. 13:12389-12395(2022).
```

Source SHA-256: `e4dda31c04daf5f332a19bce2a18fad48f65a392722189ae93f6d3e440e89922`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S5B9?format=txt&versions=13)  
**Locator:** `lines 30-36`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 13 / 1.  
**Retrieved:** 2026-11-01T06:27:37.410633+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=rhazimol + NADP(+) = rhazimal + NADPH + 2 H(+);
CC         Xref=Rhea:RHEA:79615, ChEBI:CHEBI:15378, ChEBI:CHEBI:57783,
CC         ChEBI:CHEBI:58349, ChEBI:CHEBI:230473, ChEBI:CHEBI:230474;
CC         EC=1.1.1.440; Evidence={ECO:0000269|PubMed:36349266};
CC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:79617;
CC         Evidence={ECO:0000269|PubMed:36349266};
```

Source SHA-256: `e4dda31c04daf5f332a19bce2a18fad48f65a392722189ae93f6d3e440e89922`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 64. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
