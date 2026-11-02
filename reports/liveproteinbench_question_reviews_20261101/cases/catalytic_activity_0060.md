# catalytic_activity_0060

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **D** — a (3E,5Z)-dienoyl-CoA = a (2E,4E)-(5,6-saturated)-dienoyl-CoA

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSGVTTVEYRGRVAVITICNERKLNALDLHGYYELSERMREVATHDEVYVTLLTAKGRFFSAGADVSTIRDPPTTGEDDSGIADGGRRQWLQSFVAFNLNITQAFYSHPKILVVGLNGPVVGLSAALVSFADFIYATPSTFLLTPFSSLGLVAEGGASRALVQRLGVSKANEALLMSRRVPADELLQTGFVNKVFTELKGAKDDDVRFKELVLAEIDDKLGDHLVGDSLIGIKELIRRPEIDVLEGQNAREVFAGLGRFMSGVPQREFLKLASGEKRHKL

[Multiple Choices]
A. FMN + L-glutamine + ATP = 3-amino-1,5-dihydropyridine-2,6-dione + FMNH2 + AMP + diphosphate
B. spheroidene + 2 reduced [2Fe-2S]-[ferredoxin] + O2 + 2 H(+) = 2-hydroxyspheroidene + 2 oxidized [2Fe-2S]-[ferredoxin] + H2O
C. an alpha-D-Man-(1->2)-alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-[alpha-D-Man-(1->3)-alpha-D-Man-(1->6)]-beta-D-Man-(1->4)-beta-D-GlcNAc-(1->4)-alpha-D-GlcNAc-diphospho-di-trans,poly-cis-dolichol + a di-trans,poly-cis-dolichyl beta-D-mannosyl phosphate = an alpha-D-Man-(1->2)-alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-[alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-alpha-D-Man-(1->6)]-beta-D-Man-(1->4)-beta-D-GlcNAc-(1->4)-alpha-D-GlcNAc-diphospho-di-trans,poly-cis-dolichol + a di-trans,poly-cis-dolichyl phosphate + H(+)
D. a (3E,5Z)-dienoyl-CoA = a (2E,4E)-(5,6-saturated)-dienoyl-CoA
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

> The supplied sequence exactly matches the UniProt sequence annotated as delta(3,5)-delta(2,4)-dienoyl-CoA isomerase, whose catalytic reaction is choice D. The reaction annotation is transferred by similarity from UniProtKB:Q08558, so it supports the key but is not direct experimental evidence for this exact protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices describe very different enzyme reactions, but the input provides only a protein sequence and no biological context that identifies its substrate or reaction. No sufficiently specific catalytic signature in the supplied information distinguishes D.


**Missing item-specific fact**

> The sequence-specific functional annotation identifying this protein as a delta(3,5)-delta(2,4)-dienoyl-CoA isomerase is needed to select D.


**Reason**

> Choosing D depends on knowing or retrieving the protein-specific functional assignment; merely recognizing the sequence or invoking a general predictor would not make the answer reasoning-supported from the provided input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer-only annotation assigns the matched sequence the reaction stated in D; the other choices describe distinct transformations.


### Important caveats

- The catalytic-activity evidence is transferred by similarity from UniProtKB:Q08558 (ECO:0000250), rather than shown here as a direct experimental measurement on this protein.
- The current and historical UniProt records match the supplied sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices describe very different enzyme reactions, but the input provides only a protein sequence and no biological context that identifies its substrate or reaction. No sufficiently specific catalytic signature in the supplied information distinguishes D.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence-specific functional annotation identifying this protein as a delta(3,5)-delta(2,4)-dienoyl-CoA isomerase is needed to select D.",
    "reason": "Choosing D depends on knowing or retrieving the protein-specific functional assignment; merely recognizing the sequence or invoking a general predictor would not make the answer reasoning-supported from the provided input."
  },
  "case_id": "catalytic_activity_0060",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt sequence annotated as delta(3,5)-delta(2,4)-dienoyl-CoA isomerase, whose catalytic reaction is choice D. The reaction annotation is transferred by similarity from UniProtKB:Q08558, so it supports the key but is not direct experimental evidence for this exact protein."
  },
  "important_caveats": [
    "The catalytic-activity evidence is transferred by similarity from UniProtKB:Q08558 (ECO:0000250), rather than shown here as a direct experimental measurement on this protein.",
    "The current and historical UniProt records match the supplied sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only annotation assigns the matched sequence the reaction stated in D; the other choices describe distinct transformations."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0060",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt sequence annotated as delta(3,5)-delta(2,4)-dienoyl-CoA isomerase, whose catalytic reaction is choice D. The reaction annotation is transferred by similarity from UniProtKB:Q08558, so it supports the key but is not direct experimental evidence for this exact protein.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices describe very different enzyme reactions, but the input provides only a protein sequence and no biological context that identifies its substrate or reaction. No sufficiently specific catalytic signature in the supplied information distinguishes D.",
    "missing_item_specific_fact": "The sequence-specific functional annotation identifying this protein as a delta(3,5)-delta(2,4)-dienoyl-CoA isomerase is needed to select D.",
    "reason": "Choosing D depends on knowing or retrieving the protein-specific functional assignment; merely recognizing the sequence or invoking a general predictor would not make the answer reasoning-supported from the provided input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only annotation assigns the matched sequence the reaction stated in D; the other choices describe distinct transformations."
  },
  "important_caveats": [
    "The catalytic-activity evidence is transferred by similarity from UniProtKB:Q08558 (ECO:0000250), rather than shown here as a direct experimental measurement on this protein.",
    "The current and historical UniProt records match the supplied sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied 280-AA sequence matches UniProtKB entry G4NCP4 (DCI1_PYRO7) exactly. The entry's catalytic activity annotation (C5, H4) explicitly states 'a (3E,5Z)-dienoyl-CoA = a (2E,4E)-(5,6-saturated)-dienoyl-CoA' (EC 5.3.3.21, Rhea:RHEA:45240), which is verbatim Choice D. The EC assignment carries ECO:0000305 (inferred from sequence similarity to yeast Q08558) and is further supported by PubMed:36774535 for the FUNCTION annotation. The reaction annotation itself is transferred by similarity (ECO:0000250), but the protein identity and family assignment are well-established.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One could weakly argue by elimination: the 280-AA compact size is atypical for a glycosyltransferase (C, usually >350 AA), lacks recognizable Fe-S cluster Cys motifs (B), and lacks a Rossmann-fold FMN-binding motif (A). The small size and hydrophobic character are broadly consistent with a crotonase-fold isomerase. However, this elimination reasoning is weak and does not positively identify the specific dienoyl-CoA isomerase subfamily within the large and diverse crotonase superfamily.


**Missing item-specific fact**

> Positive identification of this sequence as a Delta(3,5)-Delta(2,4)-dienoyl-CoA isomerase (DCI1 family) requires either recognizing the exact sequence, knowing the specific structural motifs of the DCI1 subfamily, or accessing a database annotation. The 280-AA sequence does not contain a unique, unambiguous motif that a general biologist could use to assign it specifically to EC 5.3.3.21 rather than another crotonase-like enzyme.


**Reason**

> While the four choices span very different enzyme classes (FMN oxidoreductase, Fe-S oxygenase, glycosyltransferase, isomerase), allowing some weak elimination by size and absence of cofactor motifs, positive identification of the dienoyl-CoA isomerase activity from a 280-AA fungal sequence without database access depends on recognizing the DCI1/crotonase subfamily. This is an item-specific annotation lookup rather than a derivable reasoning chain.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent fundamentally different enzyme classes and reaction types. There is no genuine ambiguity: either the sequence is identified as a dienoyl-CoA isomerase (D) or it is not. No two choices are defensible simultaneously.


### Important caveats

- The catalytic activity annotation in UniProtKB is transferred by similarity (ECO:0000250 from Q08558, yeast DCI1), not from direct experimental kinetics on this fungal protein. The protein name and EC assignment are supported by PubMed:36774535 (functional characterization in P. oryzae).
- The accession G4NCP4 was inferred from dataset metadata by the reviewer and was not provided to the evaluated model.
- The sequence is a 280-residue fungal protein; its compact size and general hydrophobicity are consistent with the crotonase fold but do not uniquely specify the dienoyl-CoA isomerase subfamily.
- The entry was first publicly released 2025-06-18; the historical version at the benchmark cutoff (v50, released 2026-01-28) contains the same annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One could weakly argue by elimination: the 280-AA compact size is atypical for a glycosyltransferase (C, usually >350 AA), lacks recognizable Fe-S cluster Cys motifs (B), and lacks a Rossmann-fold FMN-binding motif (A). The small size and hydrophobic character are broadly consistent with a crotonase-fold isomerase. However, this elimination reasoning is weak and does not positively identify the specific dienoyl-CoA isomerase subfamily within the large and diverse crotonase superfamily.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Positive identification of this sequence as a Delta(3,5)-Delta(2,4)-dienoyl-CoA isomerase (DCI1 family) requires either recognizing the exact sequence, knowing the specific structural motifs of the DCI1 subfamily, or accessing a database annotation. The 280-AA sequence does not contain a unique, unambiguous motif that a general biologist could use to assign it specifically to EC 5.3.3.21 rather than another crotonase-like enzyme.",
    "reason": "While the four choices span very different enzyme classes (FMN oxidoreductase, Fe-S oxygenase, glycosyltransferase, isomerase), allowing some weak elimination by size and absence of cofactor motifs, positive identification of the dienoyl-CoA isomerase activity from a 280-AA fungal sequence without database access depends on recognizing the DCI1/crotonase subfamily. This is an item-specific annotation lookup rather than a derivable reasoning chain."
  },
  "case_id": "catalytic_activity_0060",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied 280-AA sequence matches UniProtKB entry G4NCP4 (DCI1_PYRO7) exactly. The entry's catalytic activity annotation (C5, H4) explicitly states 'a (3E,5Z)-dienoyl-CoA = a (2E,4E)-(5,6-saturated)-dienoyl-CoA' (EC 5.3.3.21, Rhea:RHEA:45240), which is verbatim Choice D. The EC assignment carries ECO:0000305 (inferred from sequence similarity to yeast Q08558) and is further supported by PubMed:36774535 for the FUNCTION annotation. The reaction annotation itself is transferred by similarity (ECO:0000250), but the protein identity and family assignment are well-established."
  },
  "important_caveats": [
    "The catalytic activity annotation in UniProtKB is transferred by similarity (ECO:0000250 from Q08558, yeast DCI1), not from direct experimental kinetics on this fungal protein. The protein name and EC assignment are supported by PubMed:36774535 (functional characterization in P. oryzae).",
    "The accession G4NCP4 was inferred from dataset metadata by the reviewer and was not provided to the evaluated model.",
    "The sequence is a 280-residue fungal protein; its compact size and general hydrophobicity are consistent with the crotonase fold but do not uniquely specify the dienoyl-CoA isomerase subfamily.",
    "The entry was first publicly released 2025-06-18; the historical version at the benchmark cutoff (v50, released 2026-01-28) contains the same annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent fundamentally different enzyme classes and reaction types. There is no genuine ambiguity: either the sequence is identified as a dienoyl-CoA isomerase (D) or it is not. No two choices are defensible simultaneously."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0060",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied 280-AA sequence matches UniProtKB entry G4NCP4 (DCI1_PYRO7) exactly. The entry's catalytic activity annotation (C5, H4) explicitly states 'a (3E,5Z)-dienoyl-CoA = a (2E,4E)-(5,6-saturated)-dienoyl-CoA' (EC 5.3.3.21, Rhea:RHEA:45240), which is verbatim Choice D. The EC assignment carries ECO:0000305 (inferred from sequence similarity to yeast Q08558) and is further supported by PubMed:36774535 for the FUNCTION annotation. The reaction annotation itself is transferred by similarity (ECO:0000250), but the protein identity and family assignment are well-established.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One could weakly argue by elimination: the 280-AA compact size is atypical for a glycosyltransferase (C, usually >350 AA), lacks recognizable Fe-S cluster Cys motifs (B), and lacks a Rossmann-fold FMN-binding motif (A). The small size and hydrophobic character are broadly consistent with a crotonase-fold isomerase. However, this elimination reasoning is weak and does not positively identify the specific dienoyl-CoA isomerase subfamily within the large and diverse crotonase superfamily.",
    "missing_item_specific_fact": "Positive identification of this sequence as a Delta(3,5)-Delta(2,4)-dienoyl-CoA isomerase (DCI1 family) requires either recognizing the exact sequence, knowing the specific structural motifs of the DCI1 subfamily, or accessing a database annotation. The 280-AA sequence does not contain a unique, unambiguous motif that a general biologist could use to assign it specifically to EC 5.3.3.21 rather than another crotonase-like enzyme.",
    "reason": "While the four choices span very different enzyme classes (FMN oxidoreductase, Fe-S oxygenase, glycosyltransferase, isomerase), allowing some weak elimination by size and absence of cofactor motifs, positive identification of the dienoyl-CoA isomerase activity from a 280-AA fungal sequence without database access depends on recognizing the DCI1/crotonase subfamily. This is an item-specific annotation lookup rather than a derivable reasoning chain."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent fundamentally different enzyme classes and reaction types. There is no genuine ambiguity: either the sequence is identified as a dienoyl-CoA isomerase (D) or it is not. No two choices are defensible simultaneously."
  },
  "important_caveats": [
    "The catalytic activity annotation in UniProtKB is transferred by similarity (ECO:0000250 from Q08558, yeast DCI1), not from direct experimental kinetics on this fungal protein. The protein name and EC assignment are supported by PubMed:36774535 (functional characterization in P. oryzae).",
    "The accession G4NCP4 was inferred from dataset metadata by the reviewer and was not provided to the evaluated model.",
    "The sequence is a 280-residue fungal protein; its compact size and general hydrophobicity are consistent with the crotonase fold but do not uniquely specify the dienoyl-CoA isomerase subfamily.",
    "The entry was first publicly released 2025-06-18; the historical version at the benchmark cutoff (v50, released 2026-01-28) contains the same annotation."
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

**Accession:** `G4NCP4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 50. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NCP4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:09.351845+00:00.  

```json
"G4NCP4"
```

Source SHA-256: `18e48cf8abf1a98581d94e658f5c733af10a67b9ab523abb9b4c1242569dd85d`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NCP4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:09.351845+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q08558","source":"UniProtKB"}],"value":"Peroxisomal di-isomerase DCI1"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"36774535","source":"PubMed"}],"value":"5.3.3.21"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"36774535","source":"PubMed"}],"value":"Delta(3,5)-Delta(2,4)-dienoyl-CoA isomerase"}}}
```

Source SHA-256: `18e48cf8abf1a98581d94e658f5c733af10a67b9ab523abb9b4c1242569dd85d`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NCP4.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:09.351845+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"Q08558","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:45241"}}],"reaction":{"ecNumber":"5.3.3.21","evidences":[{"evidenceCode":"ECO:0000250","id":"Q08558","source":"UniProtKB"}],"name":"a (3E,5Z)-dienoyl-CoA = a (2E,4E)-(5,6-saturated)-dienoyl-CoA","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:45240"},{"database":"ChEBI","id":"CHEBI:85110"},{"database":"ChEBI","id":"CHEBI:85111"}]}}
```

Source SHA-256: `18e48cf8abf1a98581d94e658f5c733af10a67b9ab523abb9b4c1242569dd85d`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4NCP4?format=txt&versions=50)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 50 / 1.  
**Retrieved:** 2026-11-01T06:28:06.213875+00:00.  

```text
ID   DCI1_PYRO7              Reviewed;         280 AA.
AC   G4NCP4;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   14-DEC-2011, sequence version 1.
DT   28-JAN-2026, entry version 50.
DE   RecName: Full=Delta(3,5)-Delta(2,4)-dienoyl-CoA isomerase {ECO:0000303|PubMed:36774535};
DE            EC=5.3.3.21 {ECO:0000305|PubMed:36774535};
DE   AltName: Full=Peroxisomal di-isomerase DCI1 {ECO:0000250|UniProtKB:Q08558};
GN   Name=DCI1 {ECO:0000303|PubMed:36774535}; ORFNames=MGG_00359;
OS   Pyricularia oryzae (strain 70-15 / ATCC MYA-4617 / FGSC 8958) (Rice blast
OS   fungus) (Magnaporthe oryzae).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;
OC   Sordariomycetidae; Magnaporthales; Pyriculariaceae; Pyricularia.
OX   NCBI_TaxID=242507;
```

Source SHA-256: `b3af8253bb3b622f3d6088c53ac0e4fee82efbfd91d58cde994f260c9162d6d7`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4NCP4?format=txt&versions=50)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 50 / 1.  
**Retrieved:** 2026-11-01T06:28:06.213875+00:00.  

```text
DE   RecName: Full=Delta(3,5)-Delta(2,4)-dienoyl-CoA isomerase {ECO:0000303|PubMed:36774535};
DE            EC=5.3.3.21 {ECO:0000305|PubMed:36774535};
DE   AltName: Full=Peroxisomal di-isomerase DCI1 {ECO:0000250|UniProtKB:Q08558};
```

Source SHA-256: `b3af8253bb3b622f3d6088c53ac0e4fee82efbfd91d58cde994f260c9162d6d7`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4NCP4?format=txt&versions=50)  
**Locator:** `lines 41-46`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 50 / 1.  
**Retrieved:** 2026-11-01T06:28:06.213875+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=a (3E,5Z)-dienoyl-CoA = a (2E,4E)-(5,6-saturated)-dienoyl-CoA;
CC         Xref=Rhea:RHEA:45240, ChEBI:CHEBI:85110, ChEBI:CHEBI:85111;
CC         EC=5.3.3.21; Evidence={ECO:0000250|UniProtKB:Q08558};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:45241;
CC         Evidence={ECO:0000250|UniProtKB:Q08558};
```

Source SHA-256: `b3af8253bb3b622f3d6088c53ac0e4fee82efbfd91d58cde994f260c9162d6d7`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 60. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
