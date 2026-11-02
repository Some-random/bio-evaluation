# catalytic_activity_0056

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **D** — L-methionine + H2O = methanethiol + 2-oxobutanoate + NH4(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MIAVNSRNSLNADMTSLHPETLMVHGGMKGLTEAGVHVPAIDLSTTNPVNDVATGGDSYEWLATGHTLKDGDSAVYQRLWQPGVARFETALAGLEHAEEAVAFATGMAAMTAALLAAVSAGTPHIVAVRPLYGGSDHLLETGLLGTTVTWAKEADIASAIQDDTGLVIVETPANPSLDLVDLDSVVSAAGNVPVLVDNTFCTPVLQQPISHGAALVLHSATKYLGGHGDAMGGIIATNADWAMRLRQVRAITGALLHPMGAYLLHRGLRTLAVRMRAAQTTAGELAERLDAHPAISVVHYPGLKGQDPRGLLGRQMSGGGAMIAMELAGGFDAARSFVEHCNLVVHAVSLGGADTLIQHPASLTHRPVAATAKPGDGLIRLSVGLEHVDDLADDLIAALDASRAAA

[Multiple Choices]
A. L-galactose + NAD(+) = L-galactono-1,5-lactone + NADH + H(+)
B. 3-desmethyl okaramine B + S-adenosyl-L-methionine = okaramine B + S-adenosyl-L-homocysteine + H(+)
C. AH2 + 2 S-adenosyl-L-methionine = 2 5'-deoxyadenosin-5'-yl radical + 2 L-methionine + A + 2 H(+)
D. L-methionine + H2O = methanethiol + 2-oxobutanoate + NH4(+)
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

> The exact sequence matches the annotated L-methionine gamma-lyase, and the entry reports the reaction in choice D with experimental evidence codes citing two publications. This supports D for this sequence, though the primary papers were not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 406-aa sequence is consistent with a PLP-dependent amino-acid lyase. Among the choices, D is the amino-acid cleavage reaction; A is an NAD-dependent oxidation, B a SAM-dependent methyl transfer, and C a radical-SAM reaction. Those alternatives imply distinct enzyme classes and characteristic cofactor-related sequence features, so the choices provide a meaningful class-level distinction.


**Missing item-specific fact**

> Exact substrate specificity and experimentally established activity are protein-specific facts not supplied explicitly; they would be needed to establish D as the documented reaction rather than a sequence-based prediction.


**Reason**

> The strongly contrasting reaction classes and sequence context allow a defensible biological inference for D without needing to recall this exact protein's database entry. That inference is not equivalent to experimental confirmation of its substrate specificity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer evidence supports D among the listed reactions. The annotation also reports homocysteine desulfhydration, but that reaction is not one of the choices.


### Important caveats

- The sequence match and database annotation establish applicability to this sequence, but the cited experimental publications were not independently assessed.
- The author’s exact source snapshot is unknown; the matched historical and current records support the reaction while preserving that qualification.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 406-aa sequence is consistent with a PLP-dependent amino-acid lyase. Among the choices, D is the amino-acid cleavage reaction; A is an NAD-dependent oxidation, B a SAM-dependent methyl transfer, and C a radical-SAM reaction. Those alternatives imply distinct enzyme classes and characteristic cofactor-related sequence features, so the choices provide a meaningful class-level distinction.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Exact substrate specificity and experimentally established activity are protein-specific facts not supplied explicitly; they would be needed to establish D as the documented reaction rather than a sequence-based prediction.",
    "reason": "The strongly contrasting reaction classes and sequence context allow a defensible biological inference for D without needing to recall this exact protein's database entry. That inference is not equivalent to experimental confirmation of its substrate specificity."
  },
  "case_id": "catalytic_activity_0056",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the annotated L-methionine gamma-lyase, and the entry reports the reaction in choice D with experimental evidence codes citing two publications. This supports D for this sequence, though the primary papers were not independently reviewed here."
  },
  "important_caveats": [
    "The sequence match and database annotation establish applicability to this sequence, but the cited experimental publications were not independently assessed.",
    "The author’s exact source snapshot is unknown; the matched historical and current records support the reaction while preserving that qualification."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports D among the listed reactions. The annotation also reports homocysteine desulfhydration, but that reaction is not one of the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0056",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the annotated L-methionine gamma-lyase, and the entry reports the reaction in choice D with experimental evidence codes citing two publications. This supports D for this sequence, though the primary papers were not independently reviewed here.",
    "evidence_ids": ["C4", "C5", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 406-aa sequence is consistent with a PLP-dependent amino-acid lyase. Among the choices, D is the amino-acid cleavage reaction; A is an NAD-dependent oxidation, B a SAM-dependent methyl transfer, and C a radical-SAM reaction. Those alternatives imply distinct enzyme classes and characteristic cofactor-related sequence features, so the choices provide a meaningful class-level distinction.",
    "missing_item_specific_fact": "Exact substrate specificity and experimentally established activity are protein-specific facts not supplied explicitly; they would be needed to establish D as the documented reaction rather than a sequence-based prediction.",
    "reason": "The strongly contrasting reaction classes and sequence context allow a defensible biological inference for D without needing to recall this exact protein's database entry. That inference is not equivalent to experimental confirmation of its substrate specificity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports D among the listed reactions. The annotation also reports homocysteine desulfhydration, but that reaction is not one of the choices."
  },
  "important_caveats": [
    "The sequence match and database annotation establish applicability to this sequence, but the cited experimental publications were not independently assessed.",
    "The author’s exact source snapshot is unknown; the matched historical and current records support the reaction while preserving that qualification."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt entry A0A2H1K3G9 (MEGL_BREAU) exactly (406 aa, SHA-256 matched). The entry is annotated as L-methionine gamma-lyase (EC 4.4.1.11) with experimental evidence (ECO:0000269, PubMed:9726878 and PubMed:30940696). The catalytic activity comment states verbatim: 'L-methionine + H2O = methanethiol + 2-oxobutanoate + NH4(+)', which is identical to Choice D. The annotation is backed by purification/characterization studies, not mere computational inference.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [C8](#evidence-c8), [H1](#evidence-h1), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> None robustly available from the sequence alone. The four choices represent four very different enzyme classes (NAD-dependent oxidoreductase, SAM-dependent methyltransferase, radical SAM enzyme, PLP-dependent gamma-lyase). The 406-aa sequence lacks a Rossmann fold pattern (eliminating A), lacks the CX3CX2C radical SAM motif (eliminating C), and lacks a clear SAM-binding methyltransferase motif (eliminating B). However, the positive identification as a PLP-dependent gamma-lyase requires recognizing the specific sequence as MEGL from Brevibacterium or identifying conserved fold-type II PLP motifs, which is not feasible from general biological reasoning on this raw sequence.


**Missing item-specific fact**

> The specific identity of this protein as L-methionine gamma-lyase (MEGL) from Brevibacterium aurantiacum, which is a database annotation fact. Without recognizing this exact sequence or its fold-type II PLP structural context, the model cannot positively assign the gamma-lyase reaction.


**Reason**

> Eliminating options A, B, and C by absence of motifs is weak and unreliable for a raw sequence. Positively identifying the enzyme as a PLP gamma-lyase with methionine specificity requires either database lookup of this exact sequence or memorization of MEGL's sequence/structure. The sequence does not contain a universally recognized, easily identifiable motif that would allow a model to reason from general biology to the specific catalytic reaction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent distinct enzyme classes and reactions. Only one (D) corresponds to the annotated activity. The enzyme's secondary activity (homocysteine desulfhydrase, EC 4.4.1.2) is not among the choices, so no ambiguity arises from that.


### Important caveats

- The reviewer-only evidence confirms the key is correct, but this confirmation was not available to the evaluated model.
- The enzyme also catalyzes homocysteine desulfhydrase activity (EC 4.4.1.2), but this reaction is not offered as a distractor, so it does not affect answerability.
- The sequence is 406 aa with no signal peptide or domain boundaries provided, making de novo identification of the fold type extremely difficult without structural or database context.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "None robustly available from the sequence alone. The four choices represent four very different enzyme classes (NAD-dependent oxidoreductase, SAM-dependent methyltransferase, radical SAM enzyme, PLP-dependent gamma-lyase). The 406-aa sequence lacks a Rossmann fold pattern (eliminating A), lacks the CX3CX2C radical SAM motif (eliminating C), and lacks a clear SAM-binding methyltransferase motif (eliminating B). However, the positive identification as a PLP-dependent gamma-lyase requires recognizing the specific sequence as MEGL from Brevibacterium or identifying conserved fold-type II PLP motifs, which is not feasible from general biological reasoning on this raw sequence.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identity of this protein as L-methionine gamma-lyase (MEGL) from Brevibacterium aurantiacum, which is a database annotation fact. Without recognizing this exact sequence or its fold-type II PLP structural context, the model cannot positively assign the gamma-lyase reaction.",
    "reason": "Eliminating options A, B, and C by absence of motifs is weak and unreliable for a raw sequence. Positively identifying the enzyme as a PLP gamma-lyase with methionine specificity requires either database lookup of this exact sequence or memorization of MEGL's sequence/structure. The sequence does not contain a universally recognized, easily identifiable motif that would allow a model to reason from general biology to the specific catalytic reaction."
  },
  "case_id": "catalytic_activity_0056",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C7",
      "C8",
      "H1",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt entry A0A2H1K3G9 (MEGL_BREAU) exactly (406 aa, SHA-256 matched). The entry is annotated as L-methionine gamma-lyase (EC 4.4.1.11) with experimental evidence (ECO:0000269, PubMed:9726878 and PubMed:30940696). The catalytic activity comment states verbatim: 'L-methionine + H2O = methanethiol + 2-oxobutanoate + NH4(+)', which is identical to Choice D. The annotation is backed by purification/characterization studies, not mere computational inference."
  },
  "important_caveats": [
    "The reviewer-only evidence confirms the key is correct, but this confirmation was not available to the evaluated model.",
    "The enzyme also catalyzes homocysteine desulfhydrase activity (EC 4.4.1.2), but this reaction is not offered as a distractor, so it does not affect answerability.",
    "The sequence is 406 aa with no signal peptide or domain boundaries provided, making de novo identification of the fold type extremely difficult without structural or database context."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent distinct enzyme classes and reactions. Only one (D) corresponds to the annotated activity. The enzyme's secondary activity (homocysteine desulfhydrase, EC 4.4.1.2) is not among the choices, so no ambiguity arises from that."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0056",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt entry A0A2H1K3G9 (MEGL_BREAU) exactly (406 aa, SHA-256 matched). The entry is annotated as L-methionine gamma-lyase (EC 4.4.1.11) with experimental evidence (ECO:0000269, PubMed:9726878 and PubMed:30940696). The catalytic activity comment states verbatim: 'L-methionine + H2O = methanethiol + 2-oxobutanoate + NH4(+)', which is identical to Choice D. The annotation is backed by purification/characterization studies, not mere computational inference.",
    "evidence_ids": ["C1", "C4", "C5", "C7", "C8", "H1", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "None robustly available from the sequence alone. The four choices represent four very different enzyme classes (NAD-dependent oxidoreductase, SAM-dependent methyltransferase, radical SAM enzyme, PLP-dependent gamma-lyase). The 406-aa sequence lacks a Rossmann fold pattern (eliminating A), lacks the CX3CX2C radical SAM motif (eliminating C), and lacks a clear SAM-binding methyltransferase motif (eliminating B). However, the positive identification as a PLP-dependent gamma-lyase requires recognizing the specific sequence as MEGL from Brevibacterium or identifying conserved fold-type II PLP motifs, which is not feasible from general biological reasoning on this raw sequence.",
    "missing_item_specific_fact": "The specific identity of this protein as L-methionine gamma-lyase (MEGL) from Brevibacterium aurantiacum, which is a database annotation fact. Without recognizing this exact sequence or its fold-type II PLP structural context, the model cannot positively assign the gamma-lyase reaction.",
    "reason": "Eliminating options A, B, and C by absence of motifs is weak and unreliable for a raw sequence. Positively identifying the enzyme as a PLP gamma-lyase with methionine specificity requires either database lookup of this exact sequence or memorization of MEGL's sequence/structure. The sequence does not contain a universally recognized, easily identifiable motif that would allow a model to reason from general biology to the specific catalytic reaction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent distinct enzyme classes and reactions. Only one (D) corresponds to the annotated activity. The enzyme's secondary activity (homocysteine desulfhydrase, EC 4.4.1.2) is not among the choices, so no ambiguity arises from that."
  },
  "important_caveats": [
    "The reviewer-only evidence confirms the key is correct, but this confirmation was not available to the evaluated model.",
    "The enzyme also catalyzes homocysteine desulfhydrase activity (EC 4.4.1.2), but this reaction is not offered as a distractor, so it does not affect answerability.",
    "The sequence is 406 aa with no signal peptide or domain boundaries provided, making de novo identification of the fold type extremely difficult without structural or database context."
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

**Accession:** `A0A2H1K3G9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 32. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:44.554855+00:00.  

```json
"A0A2H1K3G9"
```

Source SHA-256: `a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:44.554855+00:00.  

```json
{"alternativeNames":[{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"30940696","source":"PubMed"}],"value":"4.4.1.2"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30940696","source":"PubMed"}],"value":"Homocysteine desulfhydrase"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30940696","source":"PubMed"}],"value":"MGL-BL929"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"30940696","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"9726878","source":"PubMed"}],"value":"4.4.1.11"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30940696","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"9726878","source":"PubMed"}],"value":"L-methionine gamma-lyase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"30940696","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"9726878","source":"PubMed"}],"value":"MGL"}]}}
```

Source SHA-256: `a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:44.554855+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"30940696","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:23801"}}],"reaction":{"ecNumber":"4.4.1.11","evidences":[{"evidenceCode":"ECO:0000269","id":"30940696","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"9726878","source":"PubMed"}],"name":"L-methionine + H2O = methanethiol + 2-oxobutanoate + NH4(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:23800"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:16007"},{"database":"ChEBI","id":"CHEBI:16763"},{"database":"ChEBI","id":"CHEBI:28938"},{"database":"ChEBI","id":"CHEBI:57844"}]}}
```

Source SHA-256: `a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:44.554855+00:00.  

```json
{"citation":{"authors":["Dias B.","Weimer B."],"citationCrossReferences":[{"database":"PubMed","id":"9726878"},{"database":"DOI","id":"10.1128/aem.64.9.3327-3331.1998"}],"citationType":"journal article","firstPage":"3327","id":"9726878","journal":"Appl. Environ. Microbiol.","lastPage":"3331","publicationDate":"1998","title":"Purification and characterization of L-methionine gamma-lyase from brevibacterium linens BL2.","volume":"64"},"referenceComments":[{"type":"STRAIN","value":"BL2"}],"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","COFACTOR","SUBSTRATE SPECIFICITY","BIOPHYSICOCHEMICAL PROPERTIES","ACTIVITY REGULATION","SUBUNIT"]}
```

Source SHA-256: `a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:44.554855+00:00.  

```json
{"citation":{"authors":["Machover D.","Rossi L.","Hamelin J.","Desterke C.","Goldschmidt E.","Chadefaux-Vekemans B.","Bonnarme P.","Briozzo P.","Kopecny D.","Pierige F.","Magnani M.","Mollicone R.","Haghighi-Rad F.","Gaston-Mathe Y.","Dairou J.","Boucheix C.","Saffroy R."],"citationCrossReferences":[{"database":"PubMed","id":"30940696"},{"database":"DOI","id":"10.1124/jpet.119.256537"}],"citationType":"journal article","firstPage":"489","id":"30940696","journal":"J. Pharmacol. Exp. Ther.","lastPage":"502","publicationDate":"2019","title":"Effects in Cancer Cells of the Recombinant L-Methionine Gamma-Lyase from Brevibacterium aurantiacum. Encapsulation in Human Erythrocytes for Sustained L-Methionine Elimination.","volume":"369"},"referenceComments":[{"type":"STRAIN","value":"ATCC 9175 / DSM 20426 / JCM 2590 / NBRC 12171 / NCDO 739 / NCIMB 8546 / KC"}],"referenceNumber":3,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","COFACTOR","SUBSTRATE SPECIFICITY","BIOPHYSICOCHEMICAL PROPERTIES","SUBUNIT","BIOTECHNOLOGY"]}
```

Source SHA-256: `a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32)  
**Locator:** `lines 1-19`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-01T06:27:25.782043+00:00.  

```text
ID   MEGL_BREAU              Reviewed;         406 AA.
AC   A0A2H1K3G9;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   31-JAN-2018, sequence version 1.
DT   28-JAN-2026, entry version 32.
DE   RecName: Full=L-methionine gamma-lyase {ECO:0000303|PubMed:30940696, ECO:0000303|PubMed:9726878};
DE            Short=MGL {ECO:0000303|PubMed:30940696, ECO:0000303|PubMed:9726878};
DE            EC=4.4.1.11 {ECO:0000269|PubMed:30940696, ECO:0000269|PubMed:9726878};
DE   AltName: Full=Homocysteine desulfhydrase {ECO:0000303|PubMed:30940696};
DE            EC=4.4.1.2 {ECO:0000269|PubMed:30940696};
DE   AltName: Full=MGL-BL929 {ECO:0000303|PubMed:30940696};
GN   ORFNames=BAUR9175_03070 {ECO:0000312|EMBL:SMX94104.1},
GN   BAUR920_03040 {ECO:0000312|EMBL:SMX97377.1},
GN   BAURA63_02933 {ECO:0000312|EMBL:SMX94451.1},
GN   BAURA86_00394 {ECO:0000312|EMBL:SMX72154.1};
OS   Brevibacterium aurantiacum.
OC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Micrococcales;
OC   Brevibacteriaceae; Brevibacterium.
OX   NCBI_TaxID=273384;
```

Source SHA-256: `9f8f2097c25cd1b2756007ac83a5f1a172b3bde4aa3f977e22144a88c5ee6f0b`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32)  
**Locator:** `lines 60-66`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-01T06:27:25.782043+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-methionine + H2O = methanethiol + 2-oxobutanoate + NH4(+);
CC         Xref=Rhea:RHEA:23800, ChEBI:CHEBI:15377, ChEBI:CHEBI:16007,
CC         ChEBI:CHEBI:16763, ChEBI:CHEBI:28938, ChEBI:CHEBI:57844; EC=4.4.1.11;
CC         Evidence={ECO:0000269|PubMed:30940696, ECO:0000269|PubMed:9726878};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:23801;
CC         Evidence={ECO:0000269|PubMed:30940696};
```

Source SHA-256: `9f8f2097c25cd1b2756007ac83a5f1a172b3bde4aa3f977e22144a88c5ee6f0b`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 56. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
