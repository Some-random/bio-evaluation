# catalytic_activity_0110

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **C** — daunorubicin(in) + ATP + H2O = daunorubicin(out) + ADP + phosphate + H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MADTAITVDGAEKRYGDKKALDGLDLRVARGTVHGVLGPNGAGKTTLVRVLSTLLRPDAGRIEVSGHDVVREAYAVRLRIGLLGQHAALDEELGGRQNLELFGRLHHLGARRARARADELLERFDLADTGRKTVRQYSGGMRRRLDLAASLITEPEVLFLDEPTTGLDPRGRAEVWDSVRSLVGGGTTVLLTTQYLEEADQLADRISVVDAGRVIAEGTADELKAETGGDRIDVVLREAGQLGAAVALLPLTGVTVDTDRRLLSAPVTDRMEALSGVVRALQEAGIEAEDVALRRPTLDEVFLHLTGDDRRVKEAA

[Multiple Choices]
A. pyrrolizixenacetamide + H2O = 3-amino-5,6,7,7a-tetrahydro-1H-pyrrolizin-1-one + acetate + H(+)
B. cyclo(N(8)-(alpha,alpha-dimethylallyl)-L-Trp-6a-(alpha,alpha-dimethylallyl)-L-Trp) + AH2 + O2 = okaramine C + A + H2O
C. daunorubicin(in) + ATP + H2O = daunorubicin(out) + ADP + phosphate + H(+)
D. cytidine(34) in elongator tRNA(Met) + acetyl-CoA + ATP + H2O = N(4)-acetylcytidine(34) in elongator tRNA(Met) + ADP + phosphate + CoA + H(+)
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

> The exact sequence matches UniProt entry P0DXU7, annotated as daunorubicin resistance ATP-binding protein DrrA3 (EC 7.6.2.2), with the catalytic reaction stated as daunorubicin efflux coupled to ATP hydrolysis. This supports choice C. The annotation cites a publication but carries curator-inference evidence, so it should not be taken as independently verified direct assay evidence here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence's P-loop-like ATP-binding motif can support an ATPase inference and may favor an ATP-driven transport reaction over the other listed reaction classes. It does not establish daunorubicin as this protein's specific transported substrate.


**Missing item-specific fact**

> The protein-specific identification and evidence connecting DrrA3 to daunorubicin efflux.


**Reason**

> Choosing the exact reaction requires knowing the transporter’s substrate or its protein-specific annotation; that fact is absent from the sequence and prompt. Inferring a broad ATP-dependent transport role does not establish the daunorubicin-specific reaction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The listed reactions represent distinct reaction classes, and the supporting annotation matches choice C. No other option is comparably supported by the evidence.


### Important caveats

- The sequence match and reaction annotation are reviewer-only information, not facts supplied to the evaluated model.
- The UniProt reaction annotation cites a 2024 paper and is marked with ECO:0000305; the cited study was not independently assessed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence's P-loop-like ATP-binding motif can support an ATPase inference and may favor an ATP-driven transport reaction over the other listed reaction classes. It does not establish daunorubicin as this protein's specific transported substrate.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification and evidence connecting DrrA3 to daunorubicin efflux.",
    "reason": "Choosing the exact reaction requires knowing the transporter’s substrate or its protein-specific annotation; that fact is absent from the sequence and prompt. Inferring a broad ATP-dependent transport role does not establish the daunorubicin-specific reaction."
  },
  "case_id": "catalytic_activity_0110",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt entry P0DXU7, annotated as daunorubicin resistance ATP-binding protein DrrA3 (EC 7.6.2.2), with the catalytic reaction stated as daunorubicin efflux coupled to ATP hydrolysis. This supports choice C. The annotation cites a publication but carries curator-inference evidence, so it should not be taken as independently verified direct assay evidence here."
  },
  "important_caveats": [
    "The sequence match and reaction annotation are reviewer-only information, not facts supplied to the evaluated model.",
    "The UniProt reaction annotation cites a 2024 paper and is marked with ECO:0000305; the cited study was not independently assessed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The listed reactions represent distinct reaction classes, and the supporting annotation matches choice C. No other option is comparably supported by the evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0110",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt entry P0DXU7, annotated as daunorubicin resistance ATP-binding protein DrrA3 (EC 7.6.2.2), with the catalytic reaction stated as daunorubicin efflux coupled to ATP hydrolysis. This supports choice C. The annotation cites a publication but carries curator-inference evidence, so it should not be taken as independently verified direct assay evidence here.",
    "evidence_ids": ["C1", "C4", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence's P-loop-like ATP-binding motif can support an ATPase inference and may favor an ATP-driven transport reaction over the other listed reaction classes. It does not establish daunorubicin as this protein's specific transported substrate.",
    "missing_item_specific_fact": "The protein-specific identification and evidence connecting DrrA3 to daunorubicin efflux.",
    "reason": "Choosing the exact reaction requires knowing the transporter’s substrate or its protein-specific annotation; that fact is absent from the sequence and prompt. Inferring a broad ATP-dependent transport role does not establish the daunorubicin-specific reaction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The listed reactions represent distinct reaction classes, and the supporting annotation matches choice C. No other option is comparably supported by the evidence."
  },
  "important_caveats": [
    "The sequence match and reaction annotation are reviewer-only information, not facts supplied to the evaluated model.",
    "The UniProt reaction annotation cites a 2024 paper and is marked with ECO:0000305; the cited study was not independently assessed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein sequence (316 AA) matches UniProt P0DXU7 (DrrA3, Daunorubicin resistance ATP-binding protein) exactly. The UniProt entry annotates EC 7.6.2.2 with catalytic activity 'daunorubicin(in) + ATP + H2O = daunorubicin(out) + ADP + phosphate + H(+)', matching Choice C verbatim. Evidence code ECO:0000305 (inferred by similarity) references PubMed:39375957, a 2024 experimental study on daunorubicin efflux by ABC transporters in Streptomyces coeruleorubidus. The annotation is computational inference by similarity rather than direct experimental characterization of this specific protein, but is grounded in experimental context.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a canonical Walker A motif (GPGAGKTTL at ~positions 40-48) and a Walker B motif (LLDEPTTGL at ~positions 170-178), which are hallmark signatures of ABC-type nucleotide-binding domains. Among the four choices, only Choice C describes an ABC transporter-mediated efflux reaction (substrate translocation coupled to ATP hydrolysis). Choices A (hydrolase), B (oxidase/monooxygenase), and D (acetyltransferase) involve entirely different enzyme classes lacking ABC motifs. A model with knowledge of ABC transporter domain architecture can eliminate A, B, and D based on the recognizable P-loop and Walker B signatures, leaving C as the only mechanistically consistent option.


**Missing item-specific fact**

> The specific substrate identity (daunorubicin vs. other ABC transporter substrates) cannot be determined from sequence alone. However, this is not needed because C is the sole ABC transporter reaction among the four choices.


**Reason**

> The ABC transporter signature (Walker A + Walker B motifs) is identifiable from the primary sequence using general biochemical knowledge. Since only one of the four options represents an ABC transporter reaction, the model can select the correct answer without needing to memorize the specific protein identity or its exact substrate. The reasoning path from motif recognition to enzyme class to matching reaction is concrete and defensible.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent four distinct enzyme classes (hydrolase, oxidase, ABC transporter, acetyltransferase). The ABC transporter motifs in the sequence unambiguously point to Choice C. No other option is mechanistically consistent with the observed domain architecture.


### Important caveats

- The UniProt annotation uses ECO:0000305 (inferred by similarity), meaning the daunorubicin-specific substrate assignment is based on homology to characterized DrrA-like transporters rather than direct in vitro characterization of this exact protein.
- The entry was first published in February 2025 (entry P0DXU7), making it a relatively recent annotation.
- The specific substrate 'daunorubicin' cannot be deduced from sequence motifs alone; the answer relies on C being the only ABC transporter option, not on substrate specificity prediction.
- All reviewer evidence is sequence-matched (SHA256 identical) to the benchmark input, confirming applicability.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a canonical Walker A motif (GPGAGKTTL at ~positions 40-48) and a Walker B motif (LLDEPTTGL at ~positions 170-178), which are hallmark signatures of ABC-type nucleotide-binding domains. Among the four choices, only Choice C describes an ABC transporter-mediated efflux reaction (substrate translocation coupled to ATP hydrolysis). Choices A (hydrolase), B (oxidase/monooxygenase), and D (acetyltransferase) involve entirely different enzyme classes lacking ABC motifs. A model with knowledge of ABC transporter domain architecture can eliminate A, B, and D based on the recognizable P-loop and Walker B signatures, leaving C as the only mechanistically consistent option.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific substrate identity (daunorubicin vs. other ABC transporter substrates) cannot be determined from sequence alone. However, this is not needed because C is the sole ABC transporter reaction among the four choices.",
    "reason": "The ABC transporter signature (Walker A + Walker B motifs) is identifiable from the primary sequence using general biochemical knowledge. Since only one of the four options represents an ABC transporter reaction, the model can select the correct answer without needing to memorize the specific protein identity or its exact substrate. The reasoning path from motif recognition to enzyme class to matching reaction is concrete and defensible."
  },
  "case_id": "catalytic_activity_0110",
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
    "reason": "The protein sequence (316 AA) matches UniProt P0DXU7 (DrrA3, Daunorubicin resistance ATP-binding protein) exactly. The UniProt entry annotates EC 7.6.2.2 with catalytic activity 'daunorubicin(in) + ATP + H2O = daunorubicin(out) + ADP + phosphate + H(+)', matching Choice C verbatim. Evidence code ECO:0000305 (inferred by similarity) references PubMed:39375957, a 2024 experimental study on daunorubicin efflux by ABC transporters in Streptomyces coeruleorubidus. The annotation is computational inference by similarity rather than direct experimental characterization of this specific protein, but is grounded in experimental context."
  },
  "important_caveats": [
    "The UniProt annotation uses ECO:0000305 (inferred by similarity), meaning the daunorubicin-specific substrate assignment is based on homology to characterized DrrA-like transporters rather than direct in vitro characterization of this exact protein.",
    "The entry was first published in February 2025 (entry P0DXU7), making it a relatively recent annotation.",
    "The specific substrate 'daunorubicin' cannot be deduced from sequence motifs alone; the answer relies on C being the only ABC transporter option, not on substrate specificity prediction.",
    "All reviewer evidence is sequence-matched (SHA256 identical) to the benchmark input, confirming applicability."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent four distinct enzyme classes (hydrolase, oxidase, ABC transporter, acetyltransferase). The ABC transporter motifs in the sequence unambiguously point to Choice C. No other option is mechanistically consistent with the observed domain architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0110",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein sequence (316 AA) matches UniProt P0DXU7 (DrrA3, Daunorubicin resistance ATP-binding protein) exactly. The UniProt entry annotates EC 7.6.2.2 with catalytic activity 'daunorubicin(in) + ATP + H2O = daunorubicin(out) + ADP + phosphate + H(+)', matching Choice C verbatim. Evidence code ECO:0000305 (inferred by similarity) references PubMed:39375957, a 2024 experimental study on daunorubicin efflux by ABC transporters in Streptomyces coeruleorubidus. The annotation is computational inference by similarity rather than direct experimental characterization of this specific protein, but is grounded in experimental context.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a canonical Walker A motif (GPGAGKTTL at ~positions 40-48) and a Walker B motif (LLDEPTTGL at ~positions 170-178), which are hallmark signatures of ABC-type nucleotide-binding domains. Among the four choices, only Choice C describes an ABC transporter-mediated efflux reaction (substrate translocation coupled to ATP hydrolysis). Choices A (hydrolase), B (oxidase/monooxygenase), and D (acetyltransferase) involve entirely different enzyme classes lacking ABC motifs. A model with knowledge of ABC transporter domain architecture can eliminate A, B, and D based on the recognizable P-loop and Walker B signatures, leaving C as the only mechanistically consistent option.",
    "missing_item_specific_fact": "The specific substrate identity (daunorubicin vs. other ABC transporter substrates) cannot be determined from sequence alone. However, this is not needed because C is the sole ABC transporter reaction among the four choices.",
    "reason": "The ABC transporter signature (Walker A + Walker B motifs) is identifiable from the primary sequence using general biochemical knowledge. Since only one of the four options represents an ABC transporter reaction, the model can select the correct answer without needing to memorize the specific protein identity or its exact substrate. The reasoning path from motif recognition to enzyme class to matching reaction is concrete and defensible."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent four distinct enzyme classes (hydrolase, oxidase, ABC transporter, acetyltransferase). The ABC transporter motifs in the sequence unambiguously point to Choice C. No other option is mechanistically consistent with the observed domain architecture."
  },
  "important_caveats": [
    "The UniProt annotation uses ECO:0000305 (inferred by similarity), meaning the daunorubicin-specific substrate assignment is based on homology to characterized DrrA-like transporters rather than direct in vitro characterization of this exact protein.",
    "The entry was first published in February 2025 (entry P0DXU7), making it a relatively recent annotation.",
    "The specific substrate 'daunorubicin' cannot be deduced from sequence motifs alone; the answer relies on C being the only ABC transporter option, not on substrate specificity prediction.",
    "All reviewer evidence is sequence-matched (SHA256 identical) to the benchmark input, confirming applicability."
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

**Accession:** `P0DXU7` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 4. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU7.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:39.757107+00:00.  

```json
"P0DXU7"
```

Source SHA-256: `e4ecbe95569eb6174ea1ce5042f5eb78567e393cf608a2fde3f152bb86370540`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU7.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:39.757107+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"39375957","source":"PubMed"}],"value":"7.6.2.2"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Daunorubicin resistance ATP-binding protein DrrA3"}}}
```

Source SHA-256: `e4ecbe95569eb6174ea1ce5042f5eb78567e393cf608a2fde3f152bb86370540`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU7.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:39.757107+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"39375957","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:33148"}}],"reaction":{"ecNumber":"7.6.2.2","evidences":[{"evidenceCode":"ECO:0000305","id":"39375957","source":"PubMed"}],"name":"daunorubicin(in) + ATP + H2O = daunorubicin(out) + ADP + phosphate + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:33147"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:64677"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `e4ecbe95569eb6174ea1ce5042f5eb78567e393cf608a2fde3f152bb86370540`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU7.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:39.757107+00:00.  

```json
{"citation":{"authors":["Dong J.","Ning J.","Tian Y.","Li H.","Chen H.","Guan W."],"citationCrossReferences":[{"database":"PubMed","id":"39375957"},{"database":"DOI","id":"10.1111/1751-7915.70023"}],"citationType":"journal article","firstPage":"e70023","id":"39375957","journal":"Microb. Biotechnol.","lastPage":"e70023","publicationDate":"2024","title":"The involvement of multiple ABC transporters in daunorubicin efflux in Streptomyces coeruleorubidus.","volume":"17"},"referenceNumber":2,"referencePositions":["FUNCTION IN DAUNORUBICIN EFFLUX","INDUCTION","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `e4ecbe95569eb6174ea1ce5042f5eb78567e393cf608a2fde3f152bb86370540`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU7?format=txt&versions=4)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:44.049376+00:00.  

```text
ID   DRRA3_STRC4             Reviewed;         316 AA.
AC   P0DXU7;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-FEB-2025, sequence version 1.
DT   28-JAN-2026, entry version 4.
DE   RecName: Full=Daunorubicin resistance ATP-binding protein DrrA3 {ECO:0000305};
DE            EC=7.6.2.2 {ECO:0000305|PubMed:39375957};
GN   Name=drrA3 {ECO:0000303|PubMed:39375957};
GN   ORFNames=R5U08_20725 {ECO:0000312|EMBL:WOT36399.1};
OS   Streptomyces coeruleorubidus.
OC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Kitasatosporales;
OC   Streptomycetaceae; Streptomyces.
OX   NCBI_TaxID=116188;
```

Source SHA-256: `42d20297633a41a19682385e9a7ca80ef7478fe940d29e171258f49592f4cbc9`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU7?format=txt&versions=4)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:44.049376+00:00.  

```text
DE   RecName: Full=Daunorubicin resistance ATP-binding protein DrrA3 {ECO:0000305};
DE            EC=7.6.2.2 {ECO:0000305|PubMed:39375957};
```

Source SHA-256: `42d20297633a41a19682385e9a7ca80ef7478fe940d29e171258f49592f4cbc9`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU7?format=txt&versions=4)  
**Locator:** `lines 19-25`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:44.049376+00:00.  

```text
RN   [2]
RP   FUNCTION IN DAUNORUBICIN EFFLUX, INDUCTION, AND DISRUPTION PHENOTYPE.
RX   PubMed=39375957; DOI=10.1111/1751-7915.70023;
RA   Dong J., Ning J., Tian Y., Li H., Chen H., Guan W.;
RT   "The involvement of multiple ABC transporters in daunorubicin efflux in
RT   Streptomyces coeruleorubidus.";
RL   Microb. Biotechnol. 17:e70023-e70023(2024).
```

Source SHA-256: `42d20297633a41a19682385e9a7ca80ef7478fe940d29e171258f49592f4cbc9`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU7?format=txt&versions=4)  
**Locator:** `lines 33-40`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:44.049376+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=daunorubicin(in) + ATP + H2O = daunorubicin(out) + ADP +
CC         phosphate + H(+); Xref=Rhea:RHEA:33147, ChEBI:CHEBI:15377,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:30616, ChEBI:CHEBI:43474,
CC         ChEBI:CHEBI:64677, ChEBI:CHEBI:456216; EC=7.6.2.2;
CC         Evidence={ECO:0000305|PubMed:39375957};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:33148;
CC         Evidence={ECO:0000305|PubMed:39375957};
```

Source SHA-256: `42d20297633a41a19682385e9a7ca80ef7478fe940d29e171258f49592f4cbc9`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 110. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
