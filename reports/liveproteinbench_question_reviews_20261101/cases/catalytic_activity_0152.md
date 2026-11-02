# catalytic_activity_0152

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **B** — Hydrolysis of terminal, non-reducing (1-&gt;4)-linked alpha-D-glucose residues with release of alpha-D-glucose.

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MPPLGVLLLLVALGHSTQGHRPLPIRKAHKFDWWERGNFYQIYPRSFKDSDGDGIGDLKGITQTIDYLKTIGIDGVWLSPIFKSPMNDFGYDISDFYAIQEEYGTMEDFEELAAKCASIGLKLILDFVPNHSSDEHEHFRLSEEGIEPYKDYYIWHSGVLDANGTRHPPSNWISVFRGSAWQWSDKRQQYYLHQFQKKQPDLNYRNPALVEEMKNVMRFWLNKGIAGFRIDALPYLFESEEVDGHYRDEPLSGQATDDPDNPAYLTHTETKDQPETYDMVHQWRQVVDEYTARDNFTRIILTEAYTAVQNMTRFYGTPAAPGAQIPFNFQLITLLTVNSTGRDFVNAVQSWTRAMPSGAIANWVLGNHDNSRIASRLGVARADLYNIALQTLPGIAVTYYGEEIAMVDQWISWNDTIDPAACNADPATYELYSRDPVRTPFQWSNGTNAGFSNASRTWLPVADGYRELNVAAQLAAPRSHLKTFMQLTAYRKRRLLAEGNFVLRTVGRDLVMYKRSVPGVGYVVVALNFGPEPATLPVASQFPGTGEHWLKVIASSLQAQPQAGTWINTRLYKLAPDSGIVLERLTGRNDLMT

[Multiple Choices]
A. (S,S)-drim-8-en-11-yl diphosphate + D-mannitol = sporulositol A + diphosphate
B. Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues with release of alpha-D-glucose.
C. O-succinyl-L-homoserine + L-cysteine = L,L-cystathionine + succinate + H(+)
D. pyrrolizixenacetamide + H2O = 3-amino-5,6,7,7a-tetrahydro-1H-pyrrolizin-1-one + acetate + H(+)
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

> The supplied sequence exactly matches the Anopheles gambiae salivary alpha-glucosidase record, which assigns EC 3.2.1.20 and the reaction in choice B. The annotation cites experimental evidence (ECO:0000269) and a functional study; the historical record also contains the matching reaction annotation.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has an N-terminal hydrophobic signal-like region, consistent with a secreted protein, but that does not distinguish the specific catalytic reaction in choice B from the alternatives.


**Missing item-specific fact**

> The protein-specific identification as salivary alpha-glucosidase, or direct functional evidence for its catalytic activity, is absent from the input.


**Reason**

> The exact reaction is supported by sequence-matched external annotation and cited experimental evidence, but the sequence and choices alone provide no sufficiently specific biological argument for identifying that reaction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched activity annotation supports choice B; the supplied evidence does not support another listed reaction.


### Important caveats

- The UniProt annotation cites experimental evidence, but the primary paper was not independently reviewed here.
- The author’s exact source snapshot is unknown; the historical entry available by the stated cutoff has the same sequence and reaction annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an N-terminal hydrophobic signal-like region, consistent with a secreted protein, but that does not distinguish the specific catalytic reaction in choice B from the alternatives.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as salivary alpha-glucosidase, or direct functional evidence for its catalytic activity, is absent from the input.",
    "reason": "The exact reaction is supported by sequence-matched external annotation and cited experimental evidence, but the sequence and choices alone provide no sufficiently specific biological argument for identifying that reaction."
  },
  "case_id": "catalytic_activity_0152",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the Anopheles gambiae salivary alpha-glucosidase record, which assigns EC 3.2.1.20 and the reaction in choice B. The annotation cites experimental evidence (ECO:0000269) and a functional study; the historical record also contains the matching reaction annotation."
  },
  "important_caveats": [
    "The UniProt annotation cites experimental evidence, but the primary paper was not independently reviewed here.",
    "The author’s exact source snapshot is unknown; the historical entry available by the stated cutoff has the same sequence and reaction annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched activity annotation supports choice B; the supplied evidence does not support another listed reaction."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0152",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the Anopheles gambiae salivary alpha-glucosidase record, which assigns EC 3.2.1.20 and the reaction in choice B. The annotation cites experimental evidence (ECO:0000269) and a functional study; the historical record also contains the matching reaction annotation.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has an N-terminal hydrophobic signal-like region, consistent with a secreted protein, but that does not distinguish the specific catalytic reaction in choice B from the alternatives.",
    "missing_item_specific_fact": "The protein-specific identification as salivary alpha-glucosidase, or direct functional evidence for its catalytic activity, is absent from the input.",
    "reason": "The exact reaction is supported by sequence-matched external annotation and cited experimental evidence, but the sequence and choices alone provide no sufficiently specific biological argument for identifying that reaction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched activity annotation supports choice B; the supplied evidence does not support another listed reaction."
  },
  "important_caveats": [
    "The UniProt annotation cites experimental evidence, but the primary paper was not independently reviewed here.",
    "The author’s exact source snapshot is unknown; the historical entry available by the stated cutoff has the same sequence and reaction annotation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q7PYT9 (MALT_ANOGA, Anopheles gambiae) annotates this 593-aa sequence as 'Salivary alpha-glucosidase' with EC 3.2.1.20. The catalytic activity comment explicitly states 'Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues with release of alpha-D-glucose,' matching Choice B verbatim. The evidence code is ECO:0000269 (PubMed:38428508, 2024), indicating experimental support from a structural/functional study of mosquito salivary alpha-glucosidases. Sequence match is exact (SHA256 identical, 593 AA).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has a hydrophobic N-terminal signal peptide (MPPLGVLLLLVALGHSTQ) suggesting a secreted protein, and its ~593-aa size is consistent with glycoside hydrolase family 31 (GH31) alpha-glucosidases. However, no unambiguous, general-knowledge-level motif in the sequence uniquely identifies this as an alpha-glucosidase with (1->4) linkage specificity rather than, e.g., a beta-glucosidase, alpha-amylase, or other glycosidase. The distractors (A: terpene cyclase; C: cystathionine gamma-synthase; D: amidase) are from entirely different enzyme classes, so identifying the protein as ANY glycosidase would eliminate three choices—but even that identification requires specialized GH31-family motif recognition (e.g., the DXXD nucleophile, conserved acid/base Glu, (β/α)8 barrel architecture) rather than general biological reasoning.


**Missing item-specific fact**

> The specific assignment of EC 3.2.1.20 (alpha-glucosidase, (1->4) alpha-D-glucosidic linkage, releasing alpha-D-glucose) to this particular Anopheles gambiae salivary protein requires either recognition of GH31-family-specific conserved motifs (specialized knowledge) or direct database lookup of the sequence. The precise linkage (1->4) and anomeric configuration (alpha) cannot be reliably inferred from the raw sequence through general enzymology reasoning alone.


**Reason**

> While the secreted nature and approximate size are weakly suggestive of a digestive glycosidase, distinguishing this as specifically an alpha-glucosidase (EC 3.2.1.20) with (1->4) alpha-linkage specificity from other glycosidase families (GH13 amylases, GH30, GH35, etc.) or other enzyme classes requires either specialized protein-family motif knowledge or database identification. The question provides no organism context, no structural data, and no active-site annotations. Selection of Choice B over the other options effectively depends on recognizing this exact sequence as the annotated salivary alpha-glucosidase.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choices A, C, and D describe reactions catalyzed by terpene cyclases, lyases, and amidases respectively—enzyme classes with entirely different folds, active-site architectures, and cofactor requirements. If the protein is identified as a glycoside hydrolase, B is the only viable option. Among the four choices, there is no genuine ambiguity once the enzyme class is determined; the difficulty lies in making that determination from sequence alone.


### Important caveats

- The UniProt annotation carries experimental evidence (ECO:0000269, PubMed:38428508, 2024), strengthening confidence in the expected answer.
- The accession Q7PYT9 was inferred by the reviewer from dataset metadata; it was not provided to the evaluated model. The model must work from the raw sequence alone.
- GH31 alpha-glucosidase identification from sequence requires recognizing conserved motifs (DXXD nucleophile, catalytic Glu, (β/α)8 barrel) that are not trivially identifiable without specialized glycoside-hydrolase-family knowledge.
- The 2024 PubMed reference post-dates many model training cutoffs; the specific functional characterization of this Anopheles gambiae enzyme may not be well-represented in training data.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a hydrophobic N-terminal signal peptide (MPPLGVLLLLVALGHSTQ) suggesting a secreted protein, and its ~593-aa size is consistent with glycoside hydrolase family 31 (GH31) alpha-glucosidases. However, no unambiguous, general-knowledge-level motif in the sequence uniquely identifies this as an alpha-glucosidase with (1->4) linkage specificity rather than, e.g., a beta-glucosidase, alpha-amylase, or other glycosidase. The distractors (A: terpene cyclase; C: cystathionine gamma-synthase; D: amidase) are from entirely different enzyme classes, so identifying the protein as ANY glycosidase would eliminate three choices—but even that identification requires specialized GH31-family motif recognition (e.g., the DXXD nucleophile, conserved acid/base Glu, (β/α)8 barrel architecture) rather than general biological reasoning.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific assignment of EC 3.2.1.20 (alpha-glucosidase, (1->4) alpha-D-glucosidic linkage, releasing alpha-D-glucose) to this particular Anopheles gambiae salivary protein requires either recognition of GH31-family-specific conserved motifs (specialized knowledge) or direct database lookup of the sequence. The precise linkage (1->4) and anomeric configuration (alpha) cannot be reliably inferred from the raw sequence through general enzymology reasoning alone.",
    "reason": "While the secreted nature and approximate size are weakly suggestive of a digestive glycosidase, distinguishing this as specifically an alpha-glucosidase (EC 3.2.1.20) with (1->4) alpha-linkage specificity from other glycosidase families (GH13 amylases, GH30, GH35, etc.) or other enzyme classes requires either specialized protein-family motif knowledge or database identification. The question provides no organism context, no structural data, and no active-site annotations. Selection of Choice B over the other options effectively depends on recognizing this exact sequence as the annotated salivary alpha-glucosidase."
  },
  "case_id": "catalytic_activity_0152",
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
    "reason": "The UniProt entry Q7PYT9 (MALT_ANOGA, Anopheles gambiae) annotates this 593-aa sequence as 'Salivary alpha-glucosidase' with EC 3.2.1.20. The catalytic activity comment explicitly states 'Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues with release of alpha-D-glucose,' matching Choice B verbatim. The evidence code is ECO:0000269 (PubMed:38428508, 2024), indicating experimental support from a structural/functional study of mosquito salivary alpha-glucosidases. Sequence match is exact (SHA256 identical, 593 AA)."
  },
  "important_caveats": [
    "The UniProt annotation carries experimental evidence (ECO:0000269, PubMed:38428508, 2024), strengthening confidence in the expected answer.",
    "The accession Q7PYT9 was inferred by the reviewer from dataset metadata; it was not provided to the evaluated model. The model must work from the raw sequence alone.",
    "GH31 alpha-glucosidase identification from sequence requires recognizing conserved motifs (DXXD nucleophile, catalytic Glu, (β/α)8 barrel) that are not trivially identifiable without specialized glycoside-hydrolase-family knowledge.",
    "The 2024 PubMed reference post-dates many model training cutoffs; the specific functional characterization of this Anopheles gambiae enzyme may not be well-represented in training data."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices A, C, and D describe reactions catalyzed by terpene cyclases, lyases, and amidases respectively—enzyme classes with entirely different folds, active-site architectures, and cofactor requirements. If the protein is identified as a glycoside hydrolase, B is the only viable option. Among the four choices, there is no genuine ambiguity once the enzyme class is determined; the difficulty lies in making that determination from sequence alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0152",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q7PYT9 (MALT_ANOGA, Anopheles gambiae) annotates this 593-aa sequence as 'Salivary alpha-glucosidase' with EC 3.2.1.20. The catalytic activity comment explicitly states 'Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues with release of alpha-D-glucose,' matching Choice B verbatim. The evidence code is ECO:0000269 (PubMed:38428508, 2024), indicating experimental support from a structural/functional study of mosquito salivary alpha-glucosidases. Sequence match is exact (SHA256 identical, 593 AA).",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has a hydrophobic N-terminal signal peptide (MPPLGVLLLLVALGHSTQ) suggesting a secreted protein, and its ~593-aa size is consistent with glycoside hydrolase family 31 (GH31) alpha-glucosidases. However, no unambiguous, general-knowledge-level motif in the sequence uniquely identifies this as an alpha-glucosidase with (1->4) linkage specificity rather than, e.g., a beta-glucosidase, alpha-amylase, or other glycosidase. The distractors (A: terpene cyclase; C: cystathionine gamma-synthase; D: amidase) are from entirely different enzyme classes, so identifying the protein as ANY glycosidase would eliminate three choices—but even that identification requires specialized GH31-family motif recognition (e.g., the DXXD nucleophile, conserved acid/base Glu, (β/α)8 barrel architecture) rather than general biological reasoning.",
    "missing_item_specific_fact": "The specific assignment of EC 3.2.1.20 (alpha-glucosidase, (1->4) alpha-D-glucosidic linkage, releasing alpha-D-glucose) to this particular Anopheles gambiae salivary protein requires either recognition of GH31-family-specific conserved motifs (specialized knowledge) or direct database lookup of the sequence. The precise linkage (1->4) and anomeric configuration (alpha) cannot be reliably inferred from the raw sequence through general enzymology reasoning alone.",
    "reason": "While the secreted nature and approximate size are weakly suggestive of a digestive glycosidase, distinguishing this as specifically an alpha-glucosidase (EC 3.2.1.20) with (1->4) alpha-linkage specificity from other glycosidase families (GH13 amylases, GH30, GH35, etc.) or other enzyme classes requires either specialized protein-family motif knowledge or database identification. The question provides no organism context, no structural data, and no active-site annotations. Selection of Choice B over the other options effectively depends on recognizing this exact sequence as the annotated salivary alpha-glucosidase."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices A, C, and D describe reactions catalyzed by terpene cyclases, lyases, and amidases respectively—enzyme classes with entirely different folds, active-site architectures, and cofactor requirements. If the protein is identified as a glycoside hydrolase, B is the only viable option. Among the four choices, there is no genuine ambiguity once the enzyme class is determined; the difficulty lies in making that determination from sequence alone."
  },
  "important_caveats": [
    "The UniProt annotation carries experimental evidence (ECO:0000269, PubMed:38428508, 2024), strengthening confidence in the expected answer.",
    "The accession Q7PYT9 was inferred by the reviewer from dataset metadata; it was not provided to the evaluated model. The model must work from the raw sequence alone.",
    "GH31 alpha-glucosidase identification from sequence requires recognizing conserved motifs (DXXD nucleophile, catalytic Glu, (β/α)8 barrel) that are not trivially identifiable without specialized glycoside-hydrolase-family knowledge.",
    "The 2024 PubMed reference post-dates many model training cutoffs; the specific functional characterization of this Anopheles gambiae enzyme may not be well-represented in training data."
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

**Accession:** `Q7PYT9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 132. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7PYT9.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:10.588074+00:00.  

```json
"Q7PYT9"
```

Source SHA-256: `b95ba5f84a3c800481a01173df1ae62cd4cae90bbd222bbb34ea446d40d2dc8d`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7PYT9.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:10.588074+00:00.  

```json
{"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38428508","source":"PubMed"}],"value":"3.2.1.20"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38428508","source":"PubMed"}],"value":"Salivary alpha-glucosidase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"38428508","source":"PubMed"}],"value":"AnGluc"}]}}
```

Source SHA-256: `b95ba5f84a3c800481a01173df1ae62cd4cae90bbd222bbb34ea446d40d2dc8d`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7PYT9.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:10.588074+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.1.20","evidences":[{"evidenceCode":"ECO:0000269","id":"38428508","source":"PubMed"}],"name":"Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues with release of alpha-D-glucose."}}
```

Source SHA-256: `b95ba5f84a3c800481a01173df1ae62cd4cae90bbd222bbb34ea446d40d2dc8d`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7PYT9.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:10.588074+00:00.  

```json
{"citation":{"authors":["Williams A.E.","Gittis A.G.","Botello K.","Cruz P.","Martin-Martin I.","Valenzuela Leon P.C.","Sumner B.","Bonilla B.","Calvo E."],"citationCrossReferences":[{"database":"PubMed","id":"38428508"},{"database":"DOI","id":"10.1016/j.ibmb.2024.104097"}],"citationType":"journal article","firstPage":"104097","id":"38428508","journal":"Insect Biochem. Mol. Biol.","lastPage":"104097","publicationDate":"2024","title":"Structural and functional comparisons of salivary alpha-glucosidases from the mosquito vectors Aedes aegypti, Anopheles gambiae, and Culex quinquefasciatus.","volume":"167"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":4,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","SUBCELLULAR LOCATION","TISSUE SPECIFICITY"]}
```

Source SHA-256: `b95ba5f84a3c800481a01173df1ae62cd4cae90bbd222bbb34ea446d40d2dc8d`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7PYT9?format=txt&versions=132)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 132 / 3.  
**Retrieved:** 2026-11-01T06:42:03.279027+00:00.  

```text
DE   RecName: Full=Salivary alpha-glucosidase {ECO:0000303|PubMed:38428508};
DE            Short=AnGluc {ECO:0000303|PubMed:38428508};
DE            EC=3.2.1.20 {ECO:0000269|PubMed:38428508};
DE   Flags: Precursor;
```

Source SHA-256: `de59e19c2630176f429b35ceca36f772399cba06a5d924df213abc4f4cd0c052`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7PYT9?format=txt&versions=132)  
**Locator:** `lines 60-69`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 132 / 3.  
**Retrieved:** 2026-11-01T06:42:03.279027+00:00.  

```text
RN   [4] {ECO:0000305}
RP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, SUBCELLULAR
RP   LOCATION, AND TISSUE SPECIFICITY.
RX   PubMed=38428508; DOI=10.1016/j.ibmb.2024.104097;
RA   Williams A.E., Gittis A.G., Botello K., Cruz P., Martin-Martin I.,
RA   Valenzuela Leon P.C., Sumner B., Bonilla B., Calvo E.;
RT   "Structural and functional comparisons of salivary alpha-glucosidases from
RT   the mosquito vectors Aedes aegypti, Anopheles gambiae, and Culex
RT   quinquefasciatus.";
RL   Insect Biochem. Mol. Biol. 167:104097-104097(2024).
```

Source SHA-256: `de59e19c2630176f429b35ceca36f772399cba06a5d924df213abc4f4cd0c052`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7PYT9?format=txt&versions=132)  
**Locator:** `lines 74-77`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 132 / 3.  
**Retrieved:** 2026-11-01T06:42:03.279027+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-
CC         glucose residues with release of alpha-D-glucose.; EC=3.2.1.20;
CC         Evidence={ECO:0000269|PubMed:38428508};
```

Source SHA-256: `de59e19c2630176f429b35ceca36f772399cba06a5d924df213abc4f4cd0c052`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 152. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
