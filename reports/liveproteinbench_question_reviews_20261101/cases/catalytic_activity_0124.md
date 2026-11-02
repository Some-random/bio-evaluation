# catalytic_activity_0124

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **C** — (E)-cinnamyl alcohol + NADP(+) = (E)-cinnamaldehyde + NADPH + H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAKSPEVEHPVKAFGWAARDPSGVLSPFNFSRRATGEHDVQFKVLYCGICHSDLHMIKNEWGFTKYPIVPGHEIVGVVTEVGSKVEKFKVGDKVGVGCLVGSCRKCDMCSDDLENYCPGQILTYSAAYTDGTTTYGGYSNLMVSDEHFVICWPENLPMDIGAPLLCAGITTYSPLRYFGLDKPGTHVGVVGLGGLGHVAVKFAKAFGAKVTVISTSESKKQEAIEKLGADAFLVSRDPEQMQGAAGSMDGIIDTVSAVHPVLPLVNLLKSQGKLIMVGAPEKPLELPVFPLLAGRRIIAGSAIGGLKETQEMIDFAAKNNILPDVELVPMDYVNTAMERLLKADVKYRFVIDIGNTLKSA

[Multiple Choices]
A. an alpha-D-Man-(1->2)-alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-[alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-[alpha-D-Man-(1->6)]-alpha-D-Man-(1->6)]-beta-D-Man-(1->4)-beta-D-GlcNAc-(1->4)-alpha-D-GlcNAc-diphospho-di-trans,poly-cis-dolichol + a di-trans,poly-cis-dolichyl beta-D-mannosyl phosphate = an alpha-D-Man-(1->2)-alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-[alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-[alpha-D-Man-(1->2)-alpha-D-Man-(1->6)]-alpha-D-Man-(1->6)]-beta-D-Man-(1->4)-beta-D-GlcNAc-(1->4)-alpha-D-GlcNAc-diphospho-di-trans,poly-cis-dolichol + a di-trans,poly-cis-dolichyl phosphate + H(+)
B. dimethylamine + NADPH + O2 + H(+) = methylamine + formaldehyde + NADP(+) + H2O
C. (E)-cinnamyl alcohol + NADP(+) = (E)-cinnamaldehyde + NADPH + H(+)
D. (1S,4S)-4-[(4-hydroxyphenyl)methyl]-2,5-diazaspiro[bicyclo[3.2.1]octane-6,1'-cyclohexan]-4'-one + S-adenosyl-L-methionine = (1S,4S)-4-[(4-hydroxyphenyl)methyl]-2-methyl-2,5-diazaspiro[bicyclo[3.2.1]octane-6,1'-cyclohexan]-4'-one + S-adenosyl-L-homocysteine + H(+)
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

> The supplied sequence exactly matches the annotated protein. UniProt assigns it EC 1.1.1.195 and records the reaction in choice C with experimental-evidence code ECO:0000269, citing PubMed 26715562. The archived entry also contains this annotation.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has cysteine-rich metal-binding-like motifs and glycine-rich regions consistent with a zinc-dependent, NAD(P)-linked alcohol dehydrogenase. That enzyme-class evidence points to choice C, the only alcohol-to-aldehyde dehydrogenation, rather than the glycosyl transfer, amine oxidation, or SAM-dependent methylation in the other choices.


**Missing item-specific fact**

> The sequence alone does not establish the enzyme's exact preference for cinnamyl alcohol; that substrate-specific assignment is supported by the annotation and cited experimental evidence, but is not necessary to distinguish the broad reaction classes in these choices.


**Reason**

> The choices differ in reaction class, and sequence features provide a concrete basis for identifying an alcohol dehydrogenase. Exact substrate specificity is less directly inferable, but the options allow the enzyme-class inference to meaningfully distinguish C.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choice C is the only option consistent with an NAD(P)-linked alcohol dehydrogenase. The annotation describes the same reaction equation.


### Important caveats

- The sequence match is exact in both the current and archived UniProt records; the author’s precise source snapshot is unknown.
- The cited annotation marks the reaction as experimentally supported, but the primary paper was not independently reviewed here.
- The annotation gives the physiological direction as right-to-left; choice C states the same reaction equation in the opposite direction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has cysteine-rich metal-binding-like motifs and glycine-rich regions consistent with a zinc-dependent, NAD(P)-linked alcohol dehydrogenase. That enzyme-class evidence points to choice C, the only alcohol-to-aldehyde dehydrogenation, rather than the glycosyl transfer, amine oxidation, or SAM-dependent methylation in the other choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The sequence alone does not establish the enzyme's exact preference for cinnamyl alcohol; that substrate-specific assignment is supported by the annotation and cited experimental evidence, but is not necessary to distinguish the broad reaction classes in these choices.",
    "reason": "The choices differ in reaction class, and sequence features provide a concrete basis for identifying an alcohol dehydrogenase. Exact substrate specificity is less directly inferable, but the options allow the enzyme-class inference to meaningfully distinguish C."
  },
  "case_id": "catalytic_activity_0124",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the annotated protein. UniProt assigns it EC 1.1.1.195 and records the reaction in choice C with experimental-evidence code ECO:0000269, citing PubMed 26715562. The archived entry also contains this annotation."
  },
  "important_caveats": [
    "The sequence match is exact in both the current and archived UniProt records; the author’s precise source snapshot is unknown.",
    "The cited annotation marks the reaction as experimentally supported, but the primary paper was not independently reviewed here.",
    "The annotation gives the physiological direction as right-to-left; choice C states the same reaction equation in the opposite direction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice C is the only option consistent with an NAD(P)-linked alcohol dehydrogenase. The annotation describes the same reaction equation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0124",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the annotated protein. UniProt assigns it EC 1.1.1.195 and records the reaction in choice C with experimental-evidence code ECO:0000269, citing PubMed 26715562. The archived entry also contains this annotation.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has cysteine-rich metal-binding-like motifs and glycine-rich regions consistent with a zinc-dependent, NAD(P)-linked alcohol dehydrogenase. That enzyme-class evidence points to choice C, the only alcohol-to-aldehyde dehydrogenation, rather than the glycosyl transfer, amine oxidation, or SAM-dependent methylation in the other choices.",
    "missing_item_specific_fact": "The sequence alone does not establish the enzyme's exact preference for cinnamyl alcohol; that substrate-specific assignment is supported by the annotation and cited experimental evidence, but is not necessary to distinguish the broad reaction classes in these choices.",
    "reason": "The choices differ in reaction class, and sequence features provide a concrete basis for identifying an alcohol dehydrogenase. Exact substrate specificity is less directly inferable, but the options allow the enzyme-class inference to meaningfully distinguish C."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice C is the only option consistent with an NAD(P)-linked alcohol dehydrogenase. The annotation describes the same reaction equation."
  },
  "important_caveats": [
    "The sequence match is exact in both the current and archived UniProt records; the author’s precise source snapshot is unknown.",
    "The cited annotation marks the reaction as experimentally supported, but the primary paper was not independently reviewed here.",
    "The annotation gives the physiological direction as right-to-left; choice C states the same reaction equation in the opposite direction."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein sequence exactly matches UniProt entry A0A0U4AHM6 (CAD2_RAUSE, Cinnamyl alcohol dehydrogenase 2 from Rauvolfia serpentina, EC 1.1.1.195). The catalytic activity is annotated as '(E)-cinnamyl alcohol + NADP(+) = (E)-cinnamaldehyde + NADPH + H(+)' with experimental evidence (ECO:0000269, PubMed:26715562). This matches Choice C verbatim. The physiological direction is noted as right-to-left (reduction), but the EC-standard reaction equation as written in Choice C is the annotated reaction.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable features of a medium-chain alcohol dehydrogenase/reductase (MDR): a Rossmann-fold nucleotide-binding motif (GxGxxG pattern visible in 'GSKVEKFKVGDKVGVG'), and a zinc-binding cysteine cluster ('CDMCSDD') characteristic of catalytic zinc sites in alcohol dehydrogenases. These oxidoreductase/dehydrogenase features clearly distinguish the protein from a glycosyltransferase (Choice A, which would show different fold motifs), a cytochrome P450 monooxygenase (Choice B, which would contain the FxxGxxxCxG heme-binding motif), or a SAM-dependent methyltransferase (Choice D, which would show V/IxGxG SAM-binding motifs). Since C is the only oxidoreductase/dehydrogenase among the four choices, identifying the enzyme class from sequence architecture is sufficient to select C.


**Missing item-specific fact**

> The specific substrate identity (cinnamyl alcohol vs. other alcohols) is not directly derivable from sequence motifs alone; however, this specificity is not needed to distinguish C from A, B, and D, which belong to entirely different enzyme classes.


**Reason**

> The sequence-level evidence (Rossmann fold, zinc-binding cysteines, overall MDR-family architecture) provides a concrete biological argument to classify this as an NAD(P)-dependent dehydrogenase, eliminating the transferase, monooxygenase, and methyltransferase distractors. The specific substrate (cinnamyl alcohol) is not independently derivable from sequence, but the question's distractor design makes class-level reasoning sufficient.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices span four distinct enzyme classes (glycosyltransferase, monooxygenase, oxidoreductase/dehydrogenase, methyltransferase). The sequence's structural motifs (Rossmann fold, zinc-binding cysteines) unambiguously point to the dehydrogenase class, making C the only defensible choice. No other option's enzyme class is supported by the sequence features.


### Important caveats

- The physiological direction of the reaction in vivo is right-to-left (reduction of cinnamaldehyde to cinnamyl alcohol), as noted in the UniProt annotation, but the EC-standard reaction equation written in Choice C (oxidation direction) is the formally annotated catalytic activity.
- The specific substrate specificity for cinnamyl alcohol (as opposed to other alcohols) relies on experimental characterization (PubMed:26715562) and is not independently derivable from sequence motifs alone; however, this does not affect answerability given the distractor design.
- The evidence code ECO:0000269 confirms experimental (not purely computational) support for the catalytic activity annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable features of a medium-chain alcohol dehydrogenase/reductase (MDR): a Rossmann-fold nucleotide-binding motif (GxGxxG pattern visible in 'GSKVEKFKVGDKVGVG'), and a zinc-binding cysteine cluster ('CDMCSDD') characteristic of catalytic zinc sites in alcohol dehydrogenases. These oxidoreductase/dehydrogenase features clearly distinguish the protein from a glycosyltransferase (Choice A, which would show different fold motifs), a cytochrome P450 monooxygenase (Choice B, which would contain the FxxGxxxCxG heme-binding motif), or a SAM-dependent methyltransferase (Choice D, which would show V/IxGxG SAM-binding motifs). Since C is the only oxidoreductase/dehydrogenase among the four choices, identifying the enzyme class from sequence architecture is sufficient to select C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific substrate identity (cinnamyl alcohol vs. other alcohols) is not directly derivable from sequence motifs alone; however, this specificity is not needed to distinguish C from A, B, and D, which belong to entirely different enzyme classes.",
    "reason": "The sequence-level evidence (Rossmann fold, zinc-binding cysteines, overall MDR-family architecture) provides a concrete biological argument to classify this as an NAD(P)-dependent dehydrogenase, eliminating the transferase, monooxygenase, and methyltransferase distractors. The specific substrate (cinnamyl alcohol) is not independently derivable from sequence, but the question's distractor design makes class-level reasoning sufficient."
  },
  "case_id": "catalytic_activity_0124",
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
    "reason": "The protein sequence exactly matches UniProt entry A0A0U4AHM6 (CAD2_RAUSE, Cinnamyl alcohol dehydrogenase 2 from Rauvolfia serpentina, EC 1.1.1.195). The catalytic activity is annotated as '(E)-cinnamyl alcohol + NADP(+) = (E)-cinnamaldehyde + NADPH + H(+)' with experimental evidence (ECO:0000269, PubMed:26715562). This matches Choice C verbatim. The physiological direction is noted as right-to-left (reduction), but the EC-standard reaction equation as written in Choice C is the annotated reaction."
  },
  "important_caveats": [
    "The physiological direction of the reaction in vivo is right-to-left (reduction of cinnamaldehyde to cinnamyl alcohol), as noted in the UniProt annotation, but the EC-standard reaction equation written in Choice C (oxidation direction) is the formally annotated catalytic activity.",
    "The specific substrate specificity for cinnamyl alcohol (as opposed to other alcohols) relies on experimental characterization (PubMed:26715562) and is not independently derivable from sequence motifs alone; however, this does not affect answerability given the distractor design.",
    "The evidence code ECO:0000269 confirms experimental (not purely computational) support for the catalytic activity annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span four distinct enzyme classes (glycosyltransferase, monooxygenase, oxidoreductase/dehydrogenase, methyltransferase). The sequence's structural motifs (Rossmann fold, zinc-binding cysteines) unambiguously point to the dehydrogenase class, making C the only defensible choice. No other option's enzyme class is supported by the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0124",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein sequence exactly matches UniProt entry A0A0U4AHM6 (CAD2_RAUSE, Cinnamyl alcohol dehydrogenase 2 from Rauvolfia serpentina, EC 1.1.1.195). The catalytic activity is annotated as '(E)-cinnamyl alcohol + NADP(+) = (E)-cinnamaldehyde + NADPH + H(+)' with experimental evidence (ECO:0000269, PubMed:26715562). This matches Choice C verbatim. The physiological direction is noted as right-to-left (reduction), but the EC-standard reaction equation as written in Choice C is the annotated reaction.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable features of a medium-chain alcohol dehydrogenase/reductase (MDR): a Rossmann-fold nucleotide-binding motif (GxGxxG pattern visible in 'GSKVEKFKVGDKVGVG'), and a zinc-binding cysteine cluster ('CDMCSDD') characteristic of catalytic zinc sites in alcohol dehydrogenases. These oxidoreductase/dehydrogenase features clearly distinguish the protein from a glycosyltransferase (Choice A, which would show different fold motifs), a cytochrome P450 monooxygenase (Choice B, which would contain the FxxGxxxCxG heme-binding motif), or a SAM-dependent methyltransferase (Choice D, which would show V/IxGxG SAM-binding motifs). Since C is the only oxidoreductase/dehydrogenase among the four choices, identifying the enzyme class from sequence architecture is sufficient to select C.",
    "missing_item_specific_fact": "The specific substrate identity (cinnamyl alcohol vs. other alcohols) is not directly derivable from sequence motifs alone; however, this specificity is not needed to distinguish C from A, B, and D, which belong to entirely different enzyme classes.",
    "reason": "The sequence-level evidence (Rossmann fold, zinc-binding cysteines, overall MDR-family architecture) provides a concrete biological argument to classify this as an NAD(P)-dependent dehydrogenase, eliminating the transferase, monooxygenase, and methyltransferase distractors. The specific substrate (cinnamyl alcohol) is not independently derivable from sequence, but the question's distractor design makes class-level reasoning sufficient."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span four distinct enzyme classes (glycosyltransferase, monooxygenase, oxidoreductase/dehydrogenase, methyltransferase). The sequence's structural motifs (Rossmann fold, zinc-binding cysteines) unambiguously point to the dehydrogenase class, making C the only defensible choice. No other option's enzyme class is supported by the sequence features."
  },
  "important_caveats": [
    "The physiological direction of the reaction in vivo is right-to-left (reduction of cinnamaldehyde to cinnamyl alcohol), as noted in the UniProt annotation, but the EC-standard reaction equation written in Choice C (oxidation direction) is the formally annotated catalytic activity.",
    "The specific substrate specificity for cinnamyl alcohol (as opposed to other alcohols) relies on experimental characterization (PubMed:26715562) and is not independently derivable from sequence motifs alone; however, this does not affect answerability given the distractor design.",
    "The evidence code ECO:0000269 confirms experimental (not purely computational) support for the catalytic activity annotation."
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

**Accession:** `A0A0U4AHM6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 27. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U4AHM6.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:23.084054+00:00.  

```json
"A0A0U4AHM6"
```

Source SHA-256: `729526cd490e7835c63bf23151cfac76f61e2eee15d3331fc705b3c325c26d70`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U4AHM6.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:23.084054+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"26715562","source":"PubMed"}],"value":"Protein RR6"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"26715562","source":"PubMed"}],"value":"RsRR6"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"26715562","source":"PubMed"}],"value":"1.1.1.195"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"26715562","source":"PubMed"}],"value":"Cinnamyl alcohol dehydrogenase 2"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"26715562","source":"PubMed"}],"value":"RsCAD2"}]}}
```

Source SHA-256: `729526cd490e7835c63bf23151cfac76f61e2eee15d3331fc705b3c325c26d70`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U4AHM6.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:23.084054+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"right-to-left","evidences":[{"evidenceCode":"ECO:0000269","id":"26715562","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:10394"}}],"reaction":{"ecNumber":"1.1.1.195","evidences":[{"evidenceCode":"ECO:0000269","id":"26715562","source":"PubMed"}],"name":"(E)-cinnamyl alcohol + NADP(+) = (E)-cinnamaldehyde + NADPH + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:10392"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:16731"},{"database":"ChEBI","id":"CHEBI:33227"},{"database":"ChEBI","id":"CHEBI:57783"},{"database":"ChEBI","id":"CHEBI:58349"}]}}
```

Source SHA-256: `729526cd490e7835c63bf23151cfac76f61e2eee15d3331fc705b3c325c26d70`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U4AHM6.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:23.084054+00:00.  

```json
{"citation":{"authors":["Geissler M.","Burghard M.","Volk J.","Staniek A.","Warzecha H."],"citationCrossReferences":[{"database":"PubMed","id":"26715562"},{"database":"DOI","id":"10.1007/s00425-015-2446-6"}],"citationType":"journal article","firstPage":"813","id":"26715562","journal":"Planta","lastPage":"824","publicationDate":"2016","title":"A novel cinnamyl alcohol dehydrogenase (CAD)-like reductase contributes to the structural diversity of monoterpenoid indole alkaloids in Rauvolfia.","volume":"243"},"evidences":[{"evidenceCode":"ECO:0000312","id":"ALW82980.1","source":"EMBL"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","PROTEIN SEQUENCE OF 43-53 AND 66-77","FUNCTION","CATALYTIC ACTIVITY","TISSUE SPECIFICITY"]}
```

Source SHA-256: `729526cd490e7835c63bf23151cfac76f61e2eee15d3331fc705b3c325c26d70`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U4AHM6?format=txt&versions=27)  
**Locator:** `lines 6-10`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 27 / 1.  
**Retrieved:** 2026-11-02T04:24:26.964793+00:00.  

```text
DE   RecName: Full=Cinnamyl alcohol dehydrogenase 2 {ECO:0000303|PubMed:26715562};
DE            Short=RsCAD2 {ECO:0000303|PubMed:26715562};
DE            EC=1.1.1.195 {ECO:0000269|PubMed:26715562};
DE   AltName: Full=Protein RR6 {ECO:0000303|PubMed:26715562};
DE            Short=RsRR6 {ECO:0000303|PubMed:26715562};
```

Source SHA-256: `e85fa680b6b0f4b7eb19749997dc2e80edd7537f4e965d90637174bac9c0e458`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U4AHM6?format=txt&versions=27)  
**Locator:** `lines 19-26`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 27 / 1.  
**Retrieved:** 2026-11-02T04:24:26.964793+00:00.  

```text
RN   [1] {ECO:0000312|EMBL:ALW82980.1}
RP   NUCLEOTIDE SEQUENCE [MRNA], PROTEIN SEQUENCE OF 43-53 AND 66-77, FUNCTION,
RP   CATALYTIC ACTIVITY, AND TISSUE SPECIFICITY.
RX   PubMed=26715562; DOI=10.1007/s00425-015-2446-6;
RA   Geissler M., Burghard M., Volk J., Staniek A., Warzecha H.;
RT   "A novel cinnamyl alcohol dehydrogenase (CAD)-like reductase contributes to
RT   the structural diversity of monoterpenoid indole alkaloids in Rauvolfia.";
RL   Planta 243:813-824(2016).
```

Source SHA-256: `e85fa680b6b0f4b7eb19749997dc2e80edd7537f4e965d90637174bac9c0e458`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U4AHM6?format=txt&versions=27)  
**Locator:** `lines 29-35`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 27 / 1.  
**Retrieved:** 2026-11-02T04:24:26.964793+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=(E)-cinnamyl alcohol + NADP(+) = (E)-cinnamaldehyde + NADPH +
CC         H(+); Xref=Rhea:RHEA:10392, ChEBI:CHEBI:15378, ChEBI:CHEBI:16731,
CC         ChEBI:CHEBI:33227, ChEBI:CHEBI:57783, ChEBI:CHEBI:58349;
CC         EC=1.1.1.195; Evidence={ECO:0000269|PubMed:26715562};
CC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:10394;
CC         Evidence={ECO:0000269|PubMed:26715562};
```

Source SHA-256: `e85fa680b6b0f4b7eb19749997dc2e80edd7537f4e965d90637174bac9c0e458`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 124. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
