# active_site_0129

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `active_site`  
**Author expected answer:** **D** — Position 70 (Acyl-ester intermediate)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MRVLALSAVFLVASIIGMPAVAKEWQENKSWNAHFTEHKSQGVVVLWNENKQQGFTNNLKRANQAFLPASTFKIPNSLIALDLGVVKDEHQVFKWDGQTRDIATWNRDHNLITAMKYSVVPVYQEFARQIGEARMSKMLHAFDYGNEDISGNVDSFWLDGGIRISATEQISFLRKLYHNKLHVSERSQRIVKQAMLTEANGDYIIRAKTGYSTRIEPKIGWWVGWVELDDNVWFFAMNMDMPTSDGLGLRQAITKEVLKQEKIIP

[Multiple Choices]
A. Position 177 (Proton donor)
B. Position 180 (For beta-ketoacyl synthase activity)
C. Position 2711 (For beta-ketoacyl synthase 2 activity)
D. Position 70 (Acyl-ester intermediate)
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Active Site Prediction, which is to identify the key amino acid residues that form the active site of an enzyme. The active site is the specific region on the enzyme where a substrate binds and the chemical reaction is catalyzed. Based on the full protein sequence provided, you must select the option that correctly lists the amino acid residues (by their type and position) that constitute the enzyme's catalytic center.. The inputs provided by the user for this task include:

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

> The exact sequence matches the OXA-48 beta-lactamase sequence, and UniProt annotates canonical position 70 as the acyl-ester-intermediate active-site residue, with literature- and structure-linked evidence. This supports choice D.

Citations as saved: [C5](#evidence-c5), [H10](#evidence-h10), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The supplied sequence contains the class D beta-lactamase catalytic SxxK motif at positions 70–73 (STFK). The motif serine is the nucleophile that forms the acyl-enzyme ester intermediate, distinguishing position 70 from the unrelated beta-ketoacyl-synthase choices and the out-of-range position 2711.


**Missing item-specific fact**

> No essential external fact is needed to distinguish the listed choices from the sequence motif and biological context. Independent experimental confirmation of the precise annotation would be protein-specific, but is not required for this choice.


**Reason**

> The sequence provides a recognizable catalytic motif and the relevant residue position; this is a concrete family-based biological inference, not merely identification of a database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options identify distinct residues or activities, and the sequence motif supports the Ser70 acyl-intermediate choice. The wording refers to residues plural while each option gives one residue, but this does not create a competing defensible option.


### Important caveats

- The supporting UniProt annotations are reviewer-only evidence, not information provided to the evaluated model.
- The sequence matches the canonical precursor sequence; the active-site position is stated in canonical coordinates.
- The annotation includes computational and literature/PDB-linked evidence; the excerpts do not independently validate every cited primary study.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The supplied sequence contains the class D beta-lactamase catalytic SxxK motif at positions 70–73 (STFK). The motif serine is the nucleophile that forms the acyl-enzyme ester intermediate, distinguishing position 70 from the unrelated beta-ketoacyl-synthase choices and the out-of-range position 2711.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No essential external fact is needed to distinguish the listed choices from the sequence motif and biological context. Independent experimental confirmation of the precise annotation would be protein-specific, but is not required for this choice.",
    "reason": "The sequence provides a recognizable catalytic motif and the relevant residue position; this is a concrete family-based biological inference, not merely identification of a database entry."
  },
  "case_id": "active_site_0129",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H10",
      "C4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the OXA-48 beta-lactamase sequence, and UniProt annotates canonical position 70 as the acyl-ester-intermediate active-site residue, with literature- and structure-linked evidence. This supports choice D."
  },
  "important_caveats": [
    "The supporting UniProt annotations are reviewer-only evidence, not information provided to the evaluated model.",
    "The sequence matches the canonical precursor sequence; the active-site position is stated in canonical coordinates.",
    "The annotation includes computational and literature/PDB-linked evidence; the excerpts do not independently validate every cited primary study."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options identify distinct residues or activities, and the sequence motif supports the Ser70 acyl-intermediate choice. The wording refers to residues plural while each option gives one residue, but this does not create a competing defensible option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0129",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the OXA-48 beta-lactamase sequence, and UniProt annotates canonical position 70 as the acyl-ester-intermediate active-site residue, with literature- and structure-linked evidence. This supports choice D.",
    "evidence_ids": ["C5", "H10", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The supplied sequence contains the class D beta-lactamase catalytic SxxK motif at positions 70–73 (STFK). The motif serine is the nucleophile that forms the acyl-enzyme ester intermediate, distinguishing position 70 from the unrelated beta-ketoacyl-synthase choices and the out-of-range position 2711.",
    "missing_item_specific_fact": "No essential external fact is needed to distinguish the listed choices from the sequence motif and biological context. Independent experimental confirmation of the precise annotation would be protein-specific, but is not required for this choice.",
    "reason": "The sequence provides a recognizable catalytic motif and the relevant residue position; this is a concrete family-based biological inference, not merely identification of a database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options identify distinct residues or activities, and the sequence motif supports the Ser70 acyl-intermediate choice. The wording refers to residues plural while each option gives one residue, but this does not create a competing defensible option."
  },
  "important_caveats": [
    "The supporting UniProt annotations are reviewer-only evidence, not information provided to the evaluated model.",
    "The sequence matches the canonical precursor sequence; the active-site position is stated in canonical coordinates.",
    "The annotation includes computational and literature/PDB-linked evidence; the excerpts do not independently validate every cited primary study."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q6XEC0 (OXA-48 beta-lactamase, Klebsiella pneumoniae) annotates position 70 as an Active site with description 'Acyl-ester intermediate', supported by multiple PDB crystal structures (4WMC, 5FAQ, 5FAS, 6P97-6P99, 6P9C, 6V1O) and experimental PubMed references. The supplied sequence matches the entry exactly (265 AA, identical SHA256). Position 70 in the sequence is Serine (S), consistent with the catalytic serine of class D beta-lactamases forming the acyl-enzyme intermediate.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H10](#evidence-h10), [H11](#evidence-h11), [C14](#evidence-c14), [C15](#evidence-c15).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the well-known STFK motif (Ser-Thr-Phe-Lys) at positions 69-73, which is the canonical active-site signature of class D serine beta-lactamases. A student with general enzyme-mechanism knowledge can scan the sequence, identify this motif, and deduce that the serine at position 70 is the nucleophilic residue forming the acyl-ester intermediate. Additionally, distractors are eliminable by basic reasoning: option C cites position 2711 in a 265-residue protein (physically impossible), and options B and C invoke 'beta-ketoacyl synthase' which is an entirely different enzyme class with a different catalytic mechanism (cysteine nucleophile in a different fold).


**Missing item-specific fact**

> None critical. While knowing the exact protein identity (OXA-48) would confirm the answer, the STFK motif recognition and elimination of impossible/irrelevant distractors provide sufficient reasoning grounds.


**Reason**

> The STFK motif is a textbook catalytic signature in serine beta-lactamases. Identifying it in the raw sequence and knowing the serine forms the acyl-enzyme intermediate constitutes general biochemical reasoning. The distractors are further eliminable by sequence-length logic (position 2711 > 265) and enzyme-class mismatch (beta-ketoacyl synthase vs. beta-lactamase).


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only option D is defensible. Option C is physically impossible (position 2711 exceeds the 265-residue length). Options B and C reference beta-ketoacyl synthase, an unrelated enzyme class. Option A (position 177, proton donor) does not correspond to the primary catalytic residue; while some residues in beta-lactamases assist proton transfer, the defining catalytic nucleophile is Ser70.


### Important caveats

- The question does not explicitly identify the protein as a beta-lactamase; the solver must infer enzyme class from sequence motifs (STFK) or prior knowledge.
- The UniProt annotation for the ACT_SITE feature combines a PIRSR computational prediction (ECO:0000255) with multiple experimental X-ray crystallography confirmations (ECO:0007744, ECO:0000269), so the final annotation is experimentally validated.
- The reviewer-only evidence confirms the sequence match and annotation but was not available to the evaluated model; the model must rely on sequence analysis alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the well-known STFK motif (Ser-Thr-Phe-Lys) at positions 69-73, which is the canonical active-site signature of class D serine beta-lactamases. A student with general enzyme-mechanism knowledge can scan the sequence, identify this motif, and deduce that the serine at position 70 is the nucleophilic residue forming the acyl-ester intermediate. Additionally, distractors are eliminable by basic reasoning: option C cites position 2711 in a 265-residue protein (physically impossible), and options B and C invoke 'beta-ketoacyl synthase' which is an entirely different enzyme class with a different catalytic mechanism (cysteine nucleophile in a different fold).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. While knowing the exact protein identity (OXA-48) would confirm the answer, the STFK motif recognition and elimination of impossible/irrelevant distractors provide sufficient reasoning grounds.",
    "reason": "The STFK motif is a textbook catalytic signature in serine beta-lactamases. Identifying it in the raw sequence and knowing the serine forms the acyl-enzyme intermediate constitutes general biochemical reasoning. The distractors are further eliminable by sequence-length logic (position 2711 > 265) and enzyme-class mismatch (beta-ketoacyl synthase vs. beta-lactamase)."
  },
  "case_id": "active_site_0129",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H10",
      "H11",
      "C14",
      "C15"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q6XEC0 (OXA-48 beta-lactamase, Klebsiella pneumoniae) annotates position 70 as an Active site with description 'Acyl-ester intermediate', supported by multiple PDB crystal structures (4WMC, 5FAQ, 5FAS, 6P97-6P99, 6P9C, 6V1O) and experimental PubMed references. The supplied sequence matches the entry exactly (265 AA, identical SHA256). Position 70 in the sequence is Serine (S), consistent with the catalytic serine of class D beta-lactamases forming the acyl-enzyme intermediate."
  },
  "important_caveats": [
    "The question does not explicitly identify the protein as a beta-lactamase; the solver must infer enzyme class from sequence motifs (STFK) or prior knowledge.",
    "The UniProt annotation for the ACT_SITE feature combines a PIRSR computational prediction (ECO:0000255) with multiple experimental X-ray crystallography confirmations (ECO:0007744, ECO:0000269), so the final annotation is experimentally validated.",
    "The reviewer-only evidence confirms the sequence match and annotation but was not available to the evaluated model; the model must rely on sequence analysis alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option D is defensible. Option C is physically impossible (position 2711 exceeds the 265-residue length). Options B and C reference beta-ketoacyl synthase, an unrelated enzyme class. Option A (position 177, proton donor) does not correspond to the primary catalytic residue; while some residues in beta-lactamases assist proton transfer, the defining catalytic nucleophile is Ser70."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0129",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q6XEC0 (OXA-48 beta-lactamase, Klebsiella pneumoniae) annotates position 70 as an Active site with description 'Acyl-ester intermediate', supported by multiple PDB crystal structures (4WMC, 5FAQ, 5FAS, 6P97-6P99, 6P9C, 6V1O) and experimental PubMed references. The supplied sequence matches the entry exactly (265 AA, identical SHA256). Position 70 in the sequence is Serine (S), consistent with the catalytic serine of class D beta-lactamases forming the acyl-enzyme intermediate.",
    "evidence_ids": ["C5", "C6", "H10", "H11", "C14", "C15"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the well-known STFK motif (Ser-Thr-Phe-Lys) at positions 69-73, which is the canonical active-site signature of class D serine beta-lactamases. A student with general enzyme-mechanism knowledge can scan the sequence, identify this motif, and deduce that the serine at position 70 is the nucleophilic residue forming the acyl-ester intermediate. Additionally, distractors are eliminable by basic reasoning: option C cites position 2711 in a 265-residue protein (physically impossible), and options B and C invoke 'beta-ketoacyl synthase' which is an entirely different enzyme class with a different catalytic mechanism (cysteine nucleophile in a different fold).",
    "missing_item_specific_fact": "None critical. While knowing the exact protein identity (OXA-48) would confirm the answer, the STFK motif recognition and elimination of impossible/irrelevant distractors provide sufficient reasoning grounds.",
    "reason": "The STFK motif is a textbook catalytic signature in serine beta-lactamases. Identifying it in the raw sequence and knowing the serine forms the acyl-enzyme intermediate constitutes general biochemical reasoning. The distractors are further eliminable by sequence-length logic (position 2711 > 265) and enzyme-class mismatch (beta-ketoacyl synthase vs. beta-lactamase)."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option D is defensible. Option C is physically impossible (position 2711 exceeds the 265-residue length). Options B and C reference beta-ketoacyl synthase, an unrelated enzyme class. Option A (position 177, proton donor) does not correspond to the primary catalytic residue; while some residues in beta-lactamases assist proton transfer, the defining catalytic nucleophile is Ser70."
  },
  "important_caveats": [
    "The question does not explicitly identify the protein as a beta-lactamase; the solver must infer enzyme class from sequence motifs (STFK) or prior knowledge.",
    "The UniProt annotation for the ACT_SITE feature combines a PIRSR computational prediction (ECO:0000255) with multiple experimental X-ray crystallography confirmations (ECO:0007744, ECO:0000269), so the final annotation is experimentally validated.",
    "The reviewer-only evidence confirms the sequence match and annotation but was not available to the evaluated model; the model must rely on sequence analysis alone."
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

**Accession:** `Q6XEC0` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 136. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6XEC0.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:45.821901+00:00.  

```json
{"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"RU361140","source":"RuleBase"},{"evidenceCode":"ECO:0000269","id":"14693513","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"19477418","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"27073009","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38161376","source":"PubMed"}],"value":"3.5.2.6"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"RU361140","source":"RuleBase"},{"evidenceCode":"ECO:0000303","id":"14693513","source":"PubMed"}],"value":"Beta-lactamase OXA-48"}}}
```

Source SHA-256: `7a7b0d77f1f923e008e8fc5048255b02d3f9e2d1a0d4b680f7c01328fb477d33`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6XEC0.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:45.821901+00:00.  

```json
{"description":"Acyl-ester intermediate","evidences":[{"evidenceCode":"ECO:0000255","id":"PIRSR602137-50","source":"PIRSR"},{"evidenceCode":"ECO:0000269","id":"25406838","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"26731698","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"31358584","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"32150407","source":"PubMed"},{"evidenceCode":"ECO:0007744","id":"4WMC","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"5FAQ","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"5FAS","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"6P97","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"6P98","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"6P99","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"6P9C","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"6V1O","source":"PDB"}],"location":{"end":{"modifier":"EXACT","value":70},"start":{"modifier":"EXACT","value":70}},"type":"Active site"}
```

Source SHA-256: `7a7b0d77f1f923e008e8fc5048255b02d3f9e2d1a0d4b680f7c01328fb477d33`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6XEC0.json)  
**Locator:** `/features/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:45.821901+00:00.  

```json
{"description":"","evidences":[{"evidenceCode":"ECO:0000250","id":"Q8RLA6","source":"UniProtKB"}],"featureCrossReferences":[{"database":"ChEBI","id":"CHEBI:35627"}],"ligand":{"id":"ChEBI:CHEBI:35627","name":"a beta-lactam"},"location":{"end":{"modifier":"EXACT","value":70},"start":{"modifier":"EXACT","value":70}},"type":"Binding site"}
```

Source SHA-256: `7a7b0d77f1f923e008e8fc5048255b02d3f9e2d1a0d4b680f7c01328fb477d33`.

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6XEC0.json)  
**Locator:** `/references/14`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:45.821901+00:00.  

```json
{"citation":{"authors":["Stojanoski V.","Adamski C.J.","Hu L.","Mehta S.C.","Sankaran B.","Zwart P.","Prasad B.V.","Palzkill T."],"citationCrossReferences":[{"database":"PubMed","id":"27073009"},{"database":"DOI","id":"10.1021/acs.biochem.6b00056"}],"citationType":"journal article","firstPage":"2479","id":"27073009","journal":"Biochemistry","lastPage":"2490","publicationDate":"2016","title":"Removal of the Side Chain at the Active-Site Serine by a Glycine Substitution Increases the Stability of a Wide Range of Serine beta-Lactamases by Relieving Steric Strain.","volume":"55"},"evidences":[{"evidenceCode":"ECO:0007744","id":"5HAP","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"5HAQ","source":"PDB"}],"referenceNumber":15,"referencePositions":["X-RAY CRYSTALLOGRAPHY (1.89 ANGSTROMS) OF 25-265 OF MUTANTS ALA-70 AND GLY-70","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","MUTAGENESIS OF SER-70"]}
```

Source SHA-256: `7a7b0d77f1f923e008e8fc5048255b02d3f9e2d1a0d4b680f7c01328fb477d33`.

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6XEC0.json)  
**Locator:** `/references/17`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:45.821901+00:00.  

```json
{"citation":{"authors":["Smith C.A.","Stewart N.K.","Toth M.","Vakulenko S.B."],"citationCrossReferences":[{"database":"PubMed","id":"31358584"},{"database":"DOI","id":"10.1128/aac.01202-19"}],"citationType":"journal article","firstPage":"e01202","id":"31358584","journal":"Antimicrob. Agents Chemother.","lastPage":"e01219","publicationDate":"2019","title":"Structural Insights into the Mechanism of Carbapenemase Activity of the OXA-48 beta-Lactamase.","volume":"63"},"evidences":[{"evidenceCode":"ECO:0007744","id":"6P96","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"6P97","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"6P98","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"6P99","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"6P9C","source":"PDB"}],"referenceNumber":18,"referencePositions":["X-RAY CRYSTALLOGRAPHY (1.60 ANGSTROMS) IN COMPLEXES WITH CARBAPENEM SUBSTRATES","SUBUNIT","ACTIVE SITE"]}
```

Source SHA-256: `7a7b0d77f1f923e008e8fc5048255b02d3f9e2d1a0d4b680f7c01328fb477d33`.

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6XEC0?format=txt&versions=136)  
**Locator:** `lines 616-624`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 136 / 1.  
**Retrieved:** 2026-11-02T04:31:51.921802+00:00.  

```text
FT   ACT_SITE        70
FT                   /note="Acyl-ester intermediate"
FT                   /evidence="ECO:0000255|PIRSR:PIRSR602137-50,
FT                   ECO:0000269|PubMed:25406838, ECO:0000269|PubMed:26731698,
FT                   ECO:0000269|PubMed:31358584, ECO:0000269|PubMed:32150407,
FT                   ECO:0007744|PDB:4WMC, ECO:0007744|PDB:5FAQ,
FT                   ECO:0007744|PDB:5FAS, ECO:0007744|PDB:6P97,
FT                   ECO:0007744|PDB:6P98, ECO:0007744|PDB:6P99,
FT                   ECO:0007744|PDB:6P9C, ECO:0007744|PDB:6V1O"
```

Source SHA-256: `748d62da6dbda55945d3952c2004e283e2a5bc809be9fd394e2b1d0eff688b3a`.

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6XEC0?format=txt&versions=136)  
**Locator:** `lines 625-628`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 136 / 1.  
**Retrieved:** 2026-11-02T04:31:51.921802+00:00.  

```text
FT   BINDING         70
FT                   /ligand="a beta-lactam"
FT                   /ligand_id="ChEBI:CHEBI:35627"
FT                   /evidence="ECO:0000250|UniProtKB:Q8RLA6"
```

Source SHA-256: `748d62da6dbda55945d3952c2004e283e2a5bc809be9fd394e2b1d0eff688b3a`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 129. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
