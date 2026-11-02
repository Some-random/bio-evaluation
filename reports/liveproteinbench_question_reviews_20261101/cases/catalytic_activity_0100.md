# catalytic_activity_0100

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **B** — UDP-N-acetyl-alpha-D-glucosamine + 2 NAD(+) + H2O = UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + 2 NADH + 3 H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKDLKVAVVGLGYVGLPLAVEFGKKRTVVGFDINQGRIAELRQGIDSTLEVDAAELKEASELSFTFNLQDLQKCNVFIVTVPTPIDEHKQPDLTPLVKASESIGKVLKKGDIVIYESTVYPGATEEDCVPVLEKFSGLRFNEDFFAGYSPERINPGDKEHRVSSIKKVTSGSTPEIAELVDSLYREIITAGTHKASSIKVAEAAKVIENTQRDLNIALINELAIIFNRMGIDTEAVLKAAGTKWNFMPFRPGLVGGHCIGVDPYYLTHKAQSIGYHPEIILAGRRLNDGMGAYVVSQLVKAMLKRRIHVDGARVLLMGLTFKENCPDLRNTKVVDIVRELAEYNIQVDVFDPWVSAEDAMHEYGITPVGTPSHGAYDGIILAVAHSEFKNMGAENIRKLGKAEHVLYDLKYLLDEDKSDLRL

[Multiple Choices]
A. (R)-norprotosinomenine + S-adenosyl-L-methionine = (R)-6-O-methylnorprotosinomenine + S-adenosyl-L-homocysteine + H(+)
B. UDP-N-acetyl-alpha-D-glucosamine + 2 NAD(+) + H2O = UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + 2 NADH + 3 H(+)
C. cyclo(L-Trp-L-Trp) + 2 dimethylallyl diphosphate = cyclo(N(8)-(alpha,alpha-dimethylallyl)-L-Trp-6a-(alpha,alpha-dimethylallyl)-L-Trp) + 2 diphosphate
D. a 14alpha-hydroxymethyl steroid + reduced [NADPH--hemoprotein reductase] + O2 = a 14alpha-formyl steroid + oxidized [NADPH--hemoprotein reductase] + 2 H2O + H(+)
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

> The supplied sequence exactly matches the 422-aa UniProt entry annotated as UDP-N-acetyl-D-glucosamine 6-dehydrogenase. Its catalytic-activity annotation gives reaction B and cites experimental evidence (ECO:0000269; PubMed 18065759), though the primary paper was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a glycine-rich N-terminal motif consistent with a soluble NAD-dependent oxidoreductase. Among the choices, B is the NAD-dependent oxidation; A is a SAM-dependent methylation, C is a prenyltransferase reaction, and D is a cytochrome-P450 reaction. This gives a meaningful sequence-and-choice-based basis for preferring B.


**Missing item-specific fact**

> The exact native substrate and product are not established by the motif alone; identifying UDP-GlcNAc specifically would require stronger family/sequence identification or an external annotation.


**Reason**

> The alternatives differ in broad enzyme class and cofactor requirements, which provides useful grounds for discrimination from the sequence. The precise reaction is not derivable from the short motif alone, but the choices make the oxidoreductase match meaningfully distinguishable.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options describe substantially different reaction and enzyme classes; B is the one consistent with a soluble NAD-dependent oxidoreductase.


### Important caveats

- The reviewer-only UniProt accession and annotations were not supplied to the evaluated model.
- The UniProt catalytic-activity annotation cites experimental evidence, but the cited study was not independently validated here; the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a glycine-rich N-terminal motif consistent with a soluble NAD-dependent oxidoreductase. Among the choices, B is the NAD-dependent oxidation; A is a SAM-dependent methylation, C is a prenyltransferase reaction, and D is a cytochrome-P450 reaction. This gives a meaningful sequence-and-choice-based basis for preferring B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact native substrate and product are not established by the motif alone; identifying UDP-GlcNAc specifically would require stronger family/sequence identification or an external annotation.",
    "reason": "The alternatives differ in broad enzyme class and cofactor requirements, which provides useful grounds for discrimination from the sequence. The precise reaction is not derivable from the short motif alone, but the choices make the oxidoreductase match meaningfully distinguishable."
  },
  "case_id": "catalytic_activity_0100",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 422-aa UniProt entry annotated as UDP-N-acetyl-D-glucosamine 6-dehydrogenase. Its catalytic-activity annotation gives reaction B and cites experimental evidence (ECO:0000269; PubMed 18065759), though the primary paper was not independently reviewed here."
  },
  "important_caveats": [
    "The reviewer-only UniProt accession and annotations were not supplied to the evaluated model.",
    "The UniProt catalytic-activity annotation cites experimental evidence, but the cited study was not independently validated here; the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options describe substantially different reaction and enzyme classes; B is the one consistent with a soluble NAD-dependent oxidoreductase."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0100",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 422-aa UniProt entry annotated as UDP-N-acetyl-D-glucosamine 6-dehydrogenase. Its catalytic-activity annotation gives reaction B and cites experimental evidence (ECO:0000269; PubMed 18065759), though the primary paper was not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a glycine-rich N-terminal motif consistent with a soluble NAD-dependent oxidoreductase. Among the choices, B is the NAD-dependent oxidation; A is a SAM-dependent methylation, C is a prenyltransferase reaction, and D is a cytochrome-P450 reaction. This gives a meaningful sequence-and-choice-based basis for preferring B.",
    "missing_item_specific_fact": "The exact native substrate and product are not established by the motif alone; identifying UDP-GlcNAc specifically would require stronger family/sequence identification or an external annotation.",
    "reason": "The alternatives differ in broad enzyme class and cofactor requirements, which provides useful grounds for discrimination from the sequence. The precise reaction is not derivable from the short motif alone, but the choices make the oxidoreductase match meaningfully distinguishable."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options describe substantially different reaction and enzyme classes; B is the one consistent with a soluble NAD-dependent oxidoreductase."
  },
  "important_caveats": [
    "The reviewer-only UniProt accession and annotations were not supplied to the evaluated model.",
    "The UniProt catalytic-activity annotation cites experimental evidence, but the cited study was not independently validated here; the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The benchmark sequence (422 aa, SHA256 matched) corresponds to UniProt Q9RHD7 (WBPO_PSEAI), experimentally characterized as UDP-N-acetyl-D-glucosamine 6-dehydrogenase (EC 1.1.1.136). The catalytic activity annotation (ECO:0000269, PubMed:18065759, a 2008 J. Biol. Chem. experimental study) states exactly: UDP-N-acetyl-alpha-D-glucosamine + 2 NAD(+) + H2O = UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + 2 NADH + 3 H(+), which is identical to Choice B.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal region contains a clear GxGxxG Rossmann fold motif (GLGYVGLPL, positions ~10-16), strongly indicating an NAD/NADP-binding oxidoreductase. This eliminates Choice A (SAM-dependent methyltransferase, which uses a distinct β-sheet fold without a Rossmann motif) and Choice C (prenyltransferase, which requires a DDxxD Mg2+-binding motif absent from the sequence). Choice D (cytochrome P450) is eliminated because the sequence lacks the highly conserved P450 heme-binding motif (FxxGxxxCxG with the axial Cys ligand); P450s do not possess a Rossmann fold themselves. With A, C, and D eliminated by cofactor/structural motif incompatibility, B (the only NAD-dependent dehydrogenase option) remains.


**Missing item-specific fact**

> None strictly required for elimination-based reasoning at the enzyme-class level. However, confirming that the specific substrate is UDP-GlcNAc (rather than another NAD-dependent dehydrogenase substrate) would require family/substrate-specific knowledge beyond generic motif recognition.


**Reason**

> The four choices span four distinct enzyme classes (methyltransferase, NAD-dehydrogenase, prenyltransferase, P450). Recognizing the Rossmann fold and the absence of P450 heme-binding, DDxxD, and SAM-binding motifs provides a concrete, general-knowledge-based elimination pathway that distinguishes B from the other three options without requiring memorization of this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent mechanistically and structurally distinct enzyme classes. The presence of a Rossmann fold and absence of P450, prenyltransferase, and methyltransferase signature motifs makes only B consistent with the sequence features.


### Important caveats

- The reasoning path relies on recognizing a GxGxxG motif and eliminating options by motif absence; it does not positively confirm the UDP-sugar substrate specificity from sequence alone.
- The experimental evidence (ECO:0000269, PubMed:18065759) is reviewer-only and was not available to the evaluated model.
- The Rossmann fold identification is based on a canonical GxGxxG pattern (GLGYVGLPL); some variation in motif recognition could affect model performance.
- Sequence identity to Q9RHD7 is confirmed by SHA256 match, but the annotation was established experimentally on the P. aeruginosa PAK strain (serotype O6).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal region contains a clear GxGxxG Rossmann fold motif (GLGYVGLPL, positions ~10-16), strongly indicating an NAD/NADP-binding oxidoreductase. This eliminates Choice A (SAM-dependent methyltransferase, which uses a distinct β-sheet fold without a Rossmann motif) and Choice C (prenyltransferase, which requires a DDxxD Mg2+-binding motif absent from the sequence). Choice D (cytochrome P450) is eliminated because the sequence lacks the highly conserved P450 heme-binding motif (FxxGxxxCxG with the axial Cys ligand); P450s do not possess a Rossmann fold themselves. With A, C, and D eliminated by cofactor/structural motif incompatibility, B (the only NAD-dependent dehydrogenase option) remains.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required for elimination-based reasoning at the enzyme-class level. However, confirming that the specific substrate is UDP-GlcNAc (rather than another NAD-dependent dehydrogenase substrate) would require family/substrate-specific knowledge beyond generic motif recognition.",
    "reason": "The four choices span four distinct enzyme classes (methyltransferase, NAD-dehydrogenase, prenyltransferase, P450). Recognizing the Rossmann fold and the absence of P450 heme-binding, DDxxD, and SAM-binding motifs provides a concrete, general-knowledge-based elimination pathway that distinguishes B from the other three options without requiring memorization of this specific protein's database entry."
  },
  "case_id": "catalytic_activity_0100",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H2",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The benchmark sequence (422 aa, SHA256 matched) corresponds to UniProt Q9RHD7 (WBPO_PSEAI), experimentally characterized as UDP-N-acetyl-D-glucosamine 6-dehydrogenase (EC 1.1.1.136). The catalytic activity annotation (ECO:0000269, PubMed:18065759, a 2008 J. Biol. Chem. experimental study) states exactly: UDP-N-acetyl-alpha-D-glucosamine + 2 NAD(+) + H2O = UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + 2 NADH + 3 H(+), which is identical to Choice B."
  },
  "important_caveats": [
    "The reasoning path relies on recognizing a GxGxxG motif and eliminating options by motif absence; it does not positively confirm the UDP-sugar substrate specificity from sequence alone.",
    "The experimental evidence (ECO:0000269, PubMed:18065759) is reviewer-only and was not available to the evaluated model.",
    "The Rossmann fold identification is based on a canonical GxGxxG pattern (GLGYVGLPL); some variation in motif recognition could affect model performance.",
    "Sequence identity to Q9RHD7 is confirmed by SHA256 match, but the annotation was established experimentally on the P. aeruginosa PAK strain (serotype O6)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent mechanistically and structurally distinct enzyme classes. The presence of a Rossmann fold and absence of P450, prenyltransferase, and methyltransferase signature motifs makes only B consistent with the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0100",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The benchmark sequence (422 aa, SHA256 matched) corresponds to UniProt Q9RHD7 (WBPO_PSEAI), experimentally characterized as UDP-N-acetyl-D-glucosamine 6-dehydrogenase (EC 1.1.1.136). The catalytic activity annotation (ECO:0000269, PubMed:18065759, a 2008 J. Biol. Chem. experimental study) states exactly: UDP-N-acetyl-alpha-D-glucosamine + 2 NAD(+) + H2O = UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + 2 NADH + 3 H(+), which is identical to Choice B.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H2", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal region contains a clear GxGxxG Rossmann fold motif (GLGYVGLPL, positions ~10-16), strongly indicating an NAD/NADP-binding oxidoreductase. This eliminates Choice A (SAM-dependent methyltransferase, which uses a distinct β-sheet fold without a Rossmann motif) and Choice C (prenyltransferase, which requires a DDxxD Mg2+-binding motif absent from the sequence). Choice D (cytochrome P450) is eliminated because the sequence lacks the highly conserved P450 heme-binding motif (FxxGxxxCxG with the axial Cys ligand); P450s do not possess a Rossmann fold themselves. With A, C, and D eliminated by cofactor/structural motif incompatibility, B (the only NAD-dependent dehydrogenase option) remains.",
    "missing_item_specific_fact": "None strictly required for elimination-based reasoning at the enzyme-class level. However, confirming that the specific substrate is UDP-GlcNAc (rather than another NAD-dependent dehydrogenase substrate) would require family/substrate-specific knowledge beyond generic motif recognition.",
    "reason": "The four choices span four distinct enzyme classes (methyltransferase, NAD-dehydrogenase, prenyltransferase, P450). Recognizing the Rossmann fold and the absence of P450 heme-binding, DDxxD, and SAM-binding motifs provides a concrete, general-knowledge-based elimination pathway that distinguishes B from the other three options without requiring memorization of this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent mechanistically and structurally distinct enzyme classes. The presence of a Rossmann fold and absence of P450, prenyltransferase, and methyltransferase signature motifs makes only B consistent with the sequence features."
  },
  "important_caveats": [
    "The reasoning path relies on recognizing a GxGxxG motif and eliminating options by motif absence; it does not positively confirm the UDP-sugar substrate specificity from sequence alone.",
    "The experimental evidence (ECO:0000269, PubMed:18065759) is reviewer-only and was not available to the evaluated model.",
    "The Rossmann fold identification is based on a canonical GxGxxG pattern (GLGYVGLPL); some variation in motif recognition could affect model performance.",
    "Sequence identity to Q9RHD7 is confirmed by SHA256 match, but the annotation was established experimentally on the P. aeruginosa PAK strain (serotype O6)."
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

**Accession:** `Q9RHD7` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 111. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:27.130209+00:00.  

```json
"Q9RHD7"
```

Source SHA-256: `9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:27.130209+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"18065759","source":"PubMed"}],"value":"1.1.1.136"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"UDP-N-acetyl-D-glucosamine 6-dehydrogenase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"UDP-GlcNAc 6-dehydrogenase"}]}}
```

Source SHA-256: `9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:27.130209+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"18065759","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:13326"}}],"reaction":{"ecNumber":"1.1.1.136","evidences":[{"evidenceCode":"ECO:0000269","id":"18065759","source":"PubMed"}],"name":"UDP-N-acetyl-alpha-D-glucosamine + 2 NAD(+) + H2O = UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + 2 NADH + 3 H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:13325"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57540"},{"database":"ChEBI","id":"CHEBI:57705"},{"database":"ChEBI","id":"CHEBI:57945"},{"database":"ChEBI","id":"CHEBI:65040"}]}}
```

Source SHA-256: `9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)  
**Locator:** `/references/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:27.130209+00:00.  

```json
{"citation":{"authors":["Miller W.L.","Matewish M.J.","McNally D.J.","Ishiyama N.","Anderson E.M.","Brewer D.","Brisson J.R.","Berghuis A.M.","Lam J.S."],"citationCrossReferences":[{"database":"PubMed","id":"18065759"},{"database":"DOI","id":"10.1074/jbc.m708894200"}],"citationType":"journal article","firstPage":"3507","id":"18065759","journal":"J. Biol. Chem.","lastPage":"3518","publicationDate":"2008","title":"Flagellin glycosylation in Pseudomonas aeruginosa PAK requires the O-antigen biosynthesis enzyme WbpO.","volume":"283"},"referenceComments":[{"type":"STRAIN","value":"PAK / Serotype O6"}],"referenceNumber":5,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","ACTIVITY REGULATION","BIOPHYSICOCHEMICAL PROPERTIES","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 111 / 1.  
**Retrieved:** 2026-11-01T06:28:50.339116+00:00.  

```text
DE   RecName: Full=UDP-N-acetyl-D-glucosamine 6-dehydrogenase {ECO:0000305};
DE            Short=UDP-GlcNAc 6-dehydrogenase {ECO:0000305};
DE            EC=1.1.1.136 {ECO:0000269|PubMed:18065759};
```

Source SHA-256: `f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111)  
**Locator:** `lines 47-56`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 111 / 1.  
**Retrieved:** 2026-11-01T06:28:50.339116+00:00.  

```text
RN   [5]
RP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, BIOPHYSICOCHEMICAL
RP   PROPERTIES, AND DISRUPTION PHENOTYPE.
RC   STRAIN=PAK / Serotype O6;
RX   PubMed=18065759; DOI=10.1074/jbc.m708894200;
RA   Miller W.L., Matewish M.J., McNally D.J., Ishiyama N., Anderson E.M.,
RA   Brewer D., Brisson J.R., Berghuis A.M., Lam J.S.;
RT   "Flagellin glycosylation in Pseudomonas aeruginosa PAK requires the O-
RT   antigen biosynthesis enzyme WbpO.";
RL   J. Biol. Chem. 283:3507-3518(2008).
```

Source SHA-256: `f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111)  
**Locator:** `lines 67-75`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 111 / 1.  
**Retrieved:** 2026-11-01T06:28:50.339116+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=UDP-N-acetyl-alpha-D-glucosamine + 2 NAD(+) + H2O = UDP-2-
CC         acetamido-2-deoxy-alpha-D-glucuronate + 2 NADH + 3 H(+);
CC         Xref=Rhea:RHEA:13325, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:57540, ChEBI:CHEBI:57705, ChEBI:CHEBI:57945,
CC         ChEBI:CHEBI:65040; EC=1.1.1.136;
CC         Evidence={ECO:0000269|PubMed:18065759};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:13326;
CC         Evidence={ECO:0000269|PubMed:18065759};
```

Source SHA-256: `f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 100. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
