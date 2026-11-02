# catalytic_activity_0180

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **D** — 1&#x27;-carboxy-chondrochloren A + FAD + 2 H(+) = chondrochloren A + FADH2 + CO2

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MNTQPLERALAAFREVLGTAHVSTDESARAAAETATFATTHRIPAIISPGSAAEVEACVRIAREHGVPLYPVSTGKNWGYGSRVPTSDGAIVLSLARMNRILDFNEELAYVAIEPGVTMRQLVAYLNDRGSRLMLSVTGSTPDSSVVGNICDRGFGAGVNAERIAHICNIEVVLPNGERLNTGFGRFPGAQTASIHRWGIGPQLDGLFTQSNLGIVTRMTIWLAPRPRHHEIFYFRLRDERRVEAVTDIIRDLKLQGLPRASVSLWNDYKLVSMKGQYPWQEAAGKTPLPEALLAKLRRAWGGAAWLGGGAILAASQDQIAAERAVIRKALHPHVDKLSFVGQRAARVARLLQRPVQRLTGFDLSEVVRAYEQSPHLGIPMERNIRSAYWRKKAPPPEQTDPDRDRCGAIWLAPAVPSTGKHVGTALRIVRERALAHAFEPGISVIFATERCANIVVALMYDRELPGEDGRAMACYQDIFDRLAAQGYLPYRLGIQSQSALPAAQSSYGTVVGALKRALDPDDILAPGRYDFRHEWPPADN

[Multiple Choices]
A. a 5'-end triphospho-ribonucleoside in mRNA + H2O = a 5'-end diphospho-ribonucleoside in mRNA + phosphate + H(+)
B. cyclo(L-Trp-L-Trp) + 2 dimethylallyl diphosphate = cyclo(N(8)-(alpha,alpha-dimethylallyl)-L-Trp-6a-(alpha,alpha-dimethylallyl)-L-Trp) + 2 diphosphate
C. (2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate + H2O
D. 1'-carboxy-chondrochloren A + FAD + 2 H(+) = chondrochloren A + FADH2 + CO2
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

> The supplied sequence exactly matches the historical and current UniProt sequence for CndG. Its catalytic-activity annotation gives choice D and cites ECO:0000269 (experimental evidence) linked to PubMed 20080978. The cited study itself was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices describe distinct, highly specific reactions. The sequence alone offers no clear general biological argument identifying this enzyme as the decarboxylase acting on 1'-carboxy-chondrochloren; assigning D requires protein-specific functional knowledge.


**Missing item-specific fact**

> The protein's identity or experimentally characterized catalytic activity as 1'-carboxy-chondrochloren decarboxylase.


**Reason**

> The reviewer-only annotation supports D but was not supplied to the evaluated model. Recognizing the sequence or relying on an unspecified predictor would not make the answer reasoning-supported.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched-sequence catalytic-activity annotation specifically supports D; the other options describe different reactions.


### Important caveats

- The sequence match establishes applicability of the cited annotation to this sequence, not independent verification of the primary study.
- The annotation’s experimental evidence code and cited paper support the key, but the paper was not comprehensively retrieved or independently validated.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices describe distinct, highly specific reactions. The sequence alone offers no clear general biological argument identifying this enzyme as the decarboxylase acting on 1'-carboxy-chondrochloren; assigning D requires protein-specific functional knowledge.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's identity or experimentally characterized catalytic activity as 1'-carboxy-chondrochloren decarboxylase.",
    "reason": "The reviewer-only annotation supports D but was not supplied to the evaluated model. Recognizing the sequence or relying on an unspecified predictor would not make the answer reasoning-supported."
  },
  "case_id": "catalytic_activity_0180",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the historical and current UniProt sequence for CndG. Its catalytic-activity annotation gives choice D and cites ECO:0000269 (experimental evidence) linked to PubMed 20080978. The cited study itself was not independently reviewed here."
  },
  "important_caveats": [
    "The sequence match establishes applicability of the cited annotation to this sequence, not independent verification of the primary study.",
    "The annotation’s experimental evidence code and cited paper support the key, but the paper was not comprehensively retrieved or independently validated."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched-sequence catalytic-activity annotation specifically supports D; the other options describe different reactions."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0180",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the historical and current UniProt sequence for CndG. Its catalytic-activity annotation gives choice D and cites ECO:0000269 (experimental evidence) linked to PubMed 20080978. The cited study itself was not independently reviewed here.",
    "evidence_ids": ["C1", "C5", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices describe distinct, highly specific reactions. The sequence alone offers no clear general biological argument identifying this enzyme as the decarboxylase acting on 1'-carboxy-chondrochloren; assigning D requires protein-specific functional knowledge.",
    "missing_item_specific_fact": "The protein's identity or experimentally characterized catalytic activity as 1'-carboxy-chondrochloren decarboxylase.",
    "reason": "The reviewer-only annotation supports D but was not supplied to the evaluated model. Recognizing the sequence or relying on an unspecified predictor would not make the answer reasoning-supported."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched-sequence catalytic-activity annotation specifically supports D; the other options describe different reactions."
  },
  "important_caveats": [
    "The sequence match establishes applicability of the cited annotation to this sequence, not independent verification of the primary study.",
    "The annotation’s experimental evidence code and cited paper support the key, but the paper was not comprehensively retrieved or independently validated."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProtKB entry B9ZUK6 (sequence-matched, 541 AA) explicitly annotates the catalytic activity as '1'-carboxy-chondrochloren A + FAD + 2 H(+) = chondrochloren A + FADH2 + CO2' (EC 4.1.1.129) with experimental evidence (ECO:0000269, PubMed:20080978, JBC 2010). The protein is named '1'-carboxy-chondrochloren decarboxylase' / 'Oxidative decarboxylase CndG' from Chondromyces crocatus. The expected answer matches the annotated reaction verbatim.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a possible FAD-binding region (STGKNWGYGSRV near the N-terminus), which could weakly suggest FAD involvement and thus disfavor choices A, B, and C. However, this is at best a very weak heuristic and does not uniquely identify the reaction. The specific substrate '1'-carboxy-chondrochloren A' is an extremely niche natural-product intermediate in the chondrochloren biosynthetic pathway of Chondromyces crocatus. No general biological reasoning from a 541-aa sequence can deduce that this particular protein oxidatively decarboxylates this particular styryl intermediate.


**Missing item-specific fact**

> The specific identity of this protein as CndG (oxidative decarboxylase) in the chondrochloren biosynthetic gene cluster of Chondromyces crocatus, and the experimental characterization (PubMed:20080978) demonstrating its FAD-dependent oxidative decarboxylation of 1'-carboxy-chondrochloren A.


**Reason**

> Selecting answer D requires knowing the specific database annotation of this protein. The reaction involves a highly specialized natural-product intermediate (chondrochloren A) that cannot be inferred from general enzymology or sequence motifs. While a trained model might recognize the sequence as CndG and recall its annotation, this constitutes memorization of a database entry rather than biological reasoning from the sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices describe mechanistically distinct enzyme classes (triphosphatase, prenyltransferase, dehydratase, oxidative decarboxylase). Given the experimental annotation, only D is correct. The choices are well-separated and do not create genuine ambiguity.


### Important caveats

- The annotation evidence is experimental (ECO:0000269 from a JBC paper), not merely computational prediction.
- The sequence is an exact match (SHA256) to UniProt B9ZUK6 in both current and historical (entry v61) snapshots.
- The FAD-binding region in the sequence is suggestive but insufficient to uniquely determine the specific substrate and reaction; it merely narrows the class of enzymes.
- The chondrochloren pathway is known from a single myxobacterium (Chondromyces crocatus); this is not a broadly conserved or textbook pathway.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a possible FAD-binding region (STGKNWGYGSRV near the N-terminus), which could weakly suggest FAD involvement and thus disfavor choices A, B, and C. However, this is at best a very weak heuristic and does not uniquely identify the reaction. The specific substrate '1'-carboxy-chondrochloren A' is an extremely niche natural-product intermediate in the chondrochloren biosynthetic pathway of Chondromyces crocatus. No general biological reasoning from a 541-aa sequence can deduce that this particular protein oxidatively decarboxylates this particular styryl intermediate.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identity of this protein as CndG (oxidative decarboxylase) in the chondrochloren biosynthetic gene cluster of Chondromyces crocatus, and the experimental characterization (PubMed:20080978) demonstrating its FAD-dependent oxidative decarboxylation of 1'-carboxy-chondrochloren A.",
    "reason": "Selecting answer D requires knowing the specific database annotation of this protein. The reaction involves a highly specialized natural-product intermediate (chondrochloren A) that cannot be inferred from general enzymology or sequence motifs. While a trained model might recognize the sequence as CndG and recall its annotation, this constitutes memorization of a database entry rather than biological reasoning from the sequence."
  },
  "case_id": "catalytic_activity_0180",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProtKB entry B9ZUK6 (sequence-matched, 541 AA) explicitly annotates the catalytic activity as '1'-carboxy-chondrochloren A + FAD + 2 H(+) = chondrochloren A + FADH2 + CO2' (EC 4.1.1.129) with experimental evidence (ECO:0000269, PubMed:20080978, JBC 2010). The protein is named '1'-carboxy-chondrochloren decarboxylase' / 'Oxidative decarboxylase CndG' from Chondromyces crocatus. The expected answer matches the annotated reaction verbatim."
  },
  "important_caveats": [
    "The annotation evidence is experimental (ECO:0000269 from a JBC paper), not merely computational prediction.",
    "The sequence is an exact match (SHA256) to UniProt B9ZUK6 in both current and historical (entry v61) snapshots.",
    "The FAD-binding region in the sequence is suggestive but insufficient to uniquely determine the specific substrate and reaction; it merely narrows the class of enzymes.",
    "The chondrochloren pathway is known from a single myxobacterium (Chondromyces crocatus); this is not a broadly conserved or textbook pathway."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices describe mechanistically distinct enzyme classes (triphosphatase, prenyltransferase, dehydratase, oxidative decarboxylase). Given the experimental annotation, only D is correct. The choices are well-separated and do not create genuine ambiguity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0180",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProtKB entry B9ZUK6 (sequence-matched, 541 AA) explicitly annotates the catalytic activity as '1'-carboxy-chondrochloren A + FAD + 2 H(+) = chondrochloren A + FADH2 + CO2' (EC 4.1.1.129) with experimental evidence (ECO:0000269, PubMed:20080978, JBC 2010). The protein is named '1'-carboxy-chondrochloren decarboxylase' / 'Oxidative decarboxylase CndG' from Chondromyces crocatus. The expected answer matches the annotated reaction verbatim.",
    "evidence_ids": ["C4", "C5", "C7", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a possible FAD-binding region (STGKNWGYGSRV near the N-terminus), which could weakly suggest FAD involvement and thus disfavor choices A, B, and C. However, this is at best a very weak heuristic and does not uniquely identify the reaction. The specific substrate '1'-carboxy-chondrochloren A' is an extremely niche natural-product intermediate in the chondrochloren biosynthetic pathway of Chondromyces crocatus. No general biological reasoning from a 541-aa sequence can deduce that this particular protein oxidatively decarboxylates this particular styryl intermediate.",
    "missing_item_specific_fact": "The specific identity of this protein as CndG (oxidative decarboxylase) in the chondrochloren biosynthetic gene cluster of Chondromyces crocatus, and the experimental characterization (PubMed:20080978) demonstrating its FAD-dependent oxidative decarboxylation of 1'-carboxy-chondrochloren A.",
    "reason": "Selecting answer D requires knowing the specific database annotation of this protein. The reaction involves a highly specialized natural-product intermediate (chondrochloren A) that cannot be inferred from general enzymology or sequence motifs. While a trained model might recognize the sequence as CndG and recall its annotation, this constitutes memorization of a database entry rather than biological reasoning from the sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices describe mechanistically distinct enzyme classes (triphosphatase, prenyltransferase, dehydratase, oxidative decarboxylase). Given the experimental annotation, only D is correct. The choices are well-separated and do not create genuine ambiguity."
  },
  "important_caveats": [
    "The annotation evidence is experimental (ECO:0000269 from a JBC paper), not merely computational prediction.",
    "The sequence is an exact match (SHA256) to UniProt B9ZUK6 in both current and historical (entry v61) snapshots.",
    "The FAD-binding region in the sequence is suggestive but insufficient to uniquely determine the specific substrate and reaction; it merely narrows the class of enzymes.",
    "The chondrochloren pathway is known from a single myxobacterium (Chondromyces crocatus); this is not a broadly conserved or textbook pathway."
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

**Accession:** `B9ZUK6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 61. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B9ZUK6.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:01.455195+00:00.  

```json
"B9ZUK6"
```

Source SHA-256: `37544f80df2e40e3cc30dce0bb90b3ac4b0740813f4bd2d7136af35a8395ee56`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B9ZUK6.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:01.455195+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"20080978","source":"PubMed"}],"value":"Oxidative decarboxylase CndG"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"20080978","source":"PubMed"}],"value":"4.1.1.129"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"1'-carboxy-chondrochloren decarboxylase"}}}
```

Source SHA-256: `37544f80df2e40e3cc30dce0bb90b3ac4b0740813f4bd2d7136af35a8395ee56`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B9ZUK6.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:01.455195+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"20080978","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:81492"}}],"reaction":{"ecNumber":"4.1.1.129","evidences":[{"evidenceCode":"ECO:0000269","id":"20080978","source":"PubMed"}],"name":"1'-carboxy-chondrochloren A + FAD + 2 H(+) = chondrochloren A + FADH2 + CO2","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:81491"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:16526"},{"database":"ChEBI","id":"CHEBI:57692"},{"database":"ChEBI","id":"CHEBI:58307"},{"database":"ChEBI","id":"CHEBI:132426"},{"database":"ChEBI","id":"CHEBI:231889"}]}}
```

Source SHA-256: `37544f80df2e40e3cc30dce0bb90b3ac4b0740813f4bd2d7136af35a8395ee56`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B9ZUK6.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:01.455195+00:00.  

```json
{"citation":{"authors":["Rachid S.","Revermann O.","Dauth C.","Kazmaier U.","Mueller R."],"citationCrossReferences":[{"database":"PubMed","id":"20080978"},{"database":"DOI","id":"10.1074/jbc.m109.079707"}],"citationType":"journal article","firstPage":"12482","id":"20080978","journal":"J. Biol. Chem.","lastPage":"12489","publicationDate":"2010","title":"Characterization of a novel type of oxidative decarboxylase involved in the biosynthesis of the styryl moiety of chondrochloren from an acylated tyrosine.","volume":"285"},"referenceComments":[{"type":"STRAIN","value":"DSM 14714 / JCM 12616 / Cm c5"}],"referenceNumber":3,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","ACTIVITY REGULATION","BIOPHYSICOCHEMICAL PROPERTIES","PATHWAY","MASS SPECTROMETRY","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `37544f80df2e40e3cc30dce0bb90b3ac4b0740813f4bd2d7136af35a8395ee56`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B9ZUK6?format=txt&versions=61)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 61 / 1.  
**Retrieved:** 2026-11-01T06:27:55.921419+00:00.  

```text
DE   RecName: Full=1'-carboxy-chondrochloren decarboxylase {ECO:0000305};
DE            EC=4.1.1.129 {ECO:0000269|PubMed:20080978};
DE   AltName: Full=Oxidative decarboxylase CndG {ECO:0000303|PubMed:20080978};
```

Source SHA-256: `f7851bd61d2f3d639ee8c9ce615c1e642a5adf7540b13dac4f8a2badafe3d4de`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B9ZUK6?format=txt&versions=61)  
**Locator:** `lines 30-39`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 61 / 1.  
**Retrieved:** 2026-11-01T06:27:55.921419+00:00.  

```text
RN   [3]
RP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, BIOPHYSICOCHEMICAL
RP   PROPERTIES, PATHWAY, MASS SPECTROMETRY, AND DISRUPTION PHENOTYPE.
RC   STRAIN=DSM 14714 / JCM 12616 / Cm c5;
RX   PubMed=20080978; DOI=10.1074/jbc.m109.079707;
RA   Rachid S., Revermann O., Dauth C., Kazmaier U., Mueller R.;
RT   "Characterization of a novel type of oxidative decarboxylase involved in
RT   the biosynthesis of the styryl moiety of chondrochloren from an acylated
RT   tyrosine.";
RL   J. Biol. Chem. 285:12482-12489(2010).
```

Source SHA-256: `f7851bd61d2f3d639ee8c9ce615c1e642a5adf7540b13dac4f8a2badafe3d4de`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B9ZUK6?format=txt&versions=61)  
**Locator:** `lines 48-55`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 61 / 1.  
**Retrieved:** 2026-11-01T06:27:55.921419+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=1'-carboxy-chondrochloren A + FAD + 2 H(+) = chondrochloren A
CC         + FADH2 + CO2; Xref=Rhea:RHEA:81491, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:16526, ChEBI:CHEBI:57692, ChEBI:CHEBI:58307,
CC         ChEBI:CHEBI:132426, ChEBI:CHEBI:231889; EC=4.1.1.129;
CC         Evidence={ECO:0000269|PubMed:20080978};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81492;
CC         Evidence={ECO:0000269|PubMed:20080978};
```

Source SHA-256: `f7851bd61d2f3d639ee8c9ce615c1e642a5adf7540b13dac4f8a2badafe3d4de`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 180. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
