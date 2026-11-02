# EC_number_0104

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **B** — 2.7.13.3

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKNRNPLIRKLLTQYFVTTGILLAFLVMIPLVIRFIAGTRTWYGTEPIYYILRFFADRWLFCVAIGALLIWFGTTIYYMTKAIGYLNETIQATTQLIEEPSKRITLSSHLIDVQEEMNQLREKSLQDQRAAKEAEQRKNDLIVYLAHDLRTPLTSVIGYLTLLKEEPQLSNAMRNRYTEIALQKAQRLELLISEFFEITRFNLTTIVLQTETTDLSLMLEQLTFEFLPLLEEKNLNWQLNLQKNVLATVDTEKIARVFDNLIRNAINYSYPDSPLLLELVESDSIHIRLTNRGKTIPEEMIGRLFEPFYRMDSSRATATSGTGLGLPIAKEILLASGGDISAESKDETIIFNVRLPKPANN

[Multiple Choices]
A. 2.7.11.1
B. 2.7.13.3
C. 3.6.1.74
D. 1.1.1.1
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence.. The inputs provided by the user for this task include:

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

> The supplied sequence exactly matches the UniProt entry annotated as a VanS sensor histidine protein kinase with EC 2.7.13.3. The annotation and catalytic-activity assignment are transferred by similarity (ECO:0000250), not direct experimental evidence for this exact protein, so the key is supported as a curated inference rather than established here by a protein-specific assay.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an N-terminal multi-pass membrane region followed by a cytoplasmic kinase domain with features characteristic of a two-component sensor histidine kinase, including a histidine-phosphotransfer region and a histidine-kinase ATPase domain. This architecture supports EC 2.7.13.3 over the serine/threonine kinase, hydrolase, and dehydrogenase alternatives.


**Missing item-specific fact**

> Direct experimental confirmation of this particular protein's catalytic activity is not supplied; the benchmark input provides only sequence.


**Reason**

> The sequence and choices provide a meaningful family-level biological distinction for a histidine kinase. The precise UniProt annotation is external, but recognizing the sequence or recalling its database entry is not necessary to make the classification.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The membrane-associated sensor kinase architecture supports the histidine kinase option; the other choices classify different reaction types.


### Important caveats

- The matching database entry's EC assignment is similarity-transferred and should not be represented as direct experimental verification for this exact sequence.
- The annotation supports the author's key, but does not establish that the original question source used that annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an N-terminal multi-pass membrane region followed by a cytoplasmic kinase domain with features characteristic of a two-component sensor histidine kinase, including a histidine-phosphotransfer region and a histidine-kinase ATPase domain. This architecture supports EC 2.7.13.3 over the serine/threonine kinase, hydrolase, and dehydrogenase alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Direct experimental confirmation of this particular protein's catalytic activity is not supplied; the benchmark input provides only sequence.",
    "reason": "The sequence and choices provide a meaningful family-level biological distinction for a histidine kinase. The precise UniProt annotation is external, but recognizing the sequence or recalling its database entry is not necessary to make the classification."
  },
  "case_id": "EC_number_0104",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as a VanS sensor histidine protein kinase with EC 2.7.13.3. The annotation and catalytic-activity assignment are transferred by similarity (ECO:0000250), not direct experimental evidence for this exact protein, so the key is supported as a curated inference rather than established here by a protein-specific assay."
  },
  "important_caveats": [
    "The matching database entry's EC assignment is similarity-transferred and should not be represented as direct experimental verification for this exact sequence.",
    "The annotation supports the author's key, but does not establish that the original question source used that annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The membrane-associated sensor kinase architecture supports the histidine kinase option; the other choices classify different reaction types."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0104",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as a VanS sensor histidine protein kinase with EC 2.7.13.3. The annotation and catalytic-activity assignment are transferred by similarity (ECO:0000250), not direct experimental evidence for this exact protein, so the key is supported as a curated inference rather than established here by a protein-specific assay.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an N-terminal multi-pass membrane region followed by a cytoplasmic kinase domain with features characteristic of a two-component sensor histidine kinase, including a histidine-phosphotransfer region and a histidine-kinase ATPase domain. This architecture supports EC 2.7.13.3 over the serine/threonine kinase, hydrolase, and dehydrogenase alternatives.",
    "missing_item_specific_fact": "Direct experimental confirmation of this particular protein's catalytic activity is not supplied; the benchmark input provides only sequence.",
    "reason": "The sequence and choices provide a meaningful family-level biological distinction for a histidine kinase. The precise UniProt annotation is external, but recognizing the sequence or recalling its database entry is not necessary to make the classification."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The membrane-associated sensor kinase architecture supports the histidine kinase option; the other choices classify different reaction types."
  },
  "important_caveats": [
    "The matching database entry's EC assignment is similarity-transferred and should not be represented as direct experimental verification for this exact sequence.",
    "The annotation supports the author's key, but does not establish that the original question source used that annotation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q9KJT3 (sequence matched exactly, 361 aa) annotates this protein as Sensor protein VanSC / Vancomycin histidine protein kinase with EC 2.7.13.3. The catalytic activity (ATP + protein L-histidine → ADP + protein N-phospho-L-histidine) is consistent with a histidine kinase. The EC assignment carries evidence code ECO:0000250 (inferred by similarity from Q06240, a well-characterized VanS homolog), and a 1.45 Å crystal structure of the kinase domain (PDB 8DX0, residues 208-361, in complex with Mg²⁺) supports the kinase domain architecture. While the EC assignment is transferred by similarity rather than from direct enzymatic assay on this specific protein, the structural and homology evidence makes the annotation well-supported.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits a multi-transmembrane N-terminal sensor domain (several hydrophobic stretches in residues ~1-180) followed by a cytoplasmic kinase domain (~residues 208-361) containing a putative conserved phosphotransferable histidine in the context 'LIVYLAHDLRT' and a G-box-like motif 'GGDISAESKDE'. This two-component sensor histidine kinase architecture (TM sensor + His-kinase domain) is a hallmark of EC 2.7.13.x (protein-histidine kinases). It is incompatible with EC 1.1.1.1 (alcohol dehydrogenase, a soluble NAD⁺-dependent oxidoreductase with no TM helices or kinase motifs), EC 3.6.1.74 (a hydrolase acting on acid anhydrides, lacking kinase catalytic machinery), and EC 2.7.11.1 (cAMP-dependent protein kinase, a soluble serine/threonine kinase with a bilobal kinase fold containing VAIK/HRD/DFG motifs and no transmembrane sensor domain). Among the four options, only 2.7.13.3 matches the observed two-component sensor kinase architecture.


**Missing item-specific fact**

> None critical. The specific sub-number 2.7.13.3 vs. other histidine kinase EC numbers is not independently derivable from sequence alone, but since only one histidine kinase option (2.7.13.3) is offered, the reasoning suffices to select it.


**Reason**

> The transmembrane sensor + kinase domain architecture, the conserved His phosphotransfer site, and the absence of features characteristic of serine/threonine kinases, oxidoreductases, or hydrolases provide concrete biological reasoning to select 2.7.13.3 over the three distractors without needing to recall the specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span three distinct enzyme classes (oxidoreductase 1.1.1.1, hydrolase 3.6.1.74, transferase 2.7.x). Within transferases, the two options (2.7.11.1 serine/threonine kinase vs. 2.7.13.3 histidine kinase) are distinguishable by the two-component sensor kinase architecture and conserved His motif visible in the sequence. No ambiguity among the provided choices.


### Important caveats

- The EC 2.7.13.3 annotation is transferred by similarity (ECO:0000250) from Q06240 rather than from a direct enzymatic assay on Q9KJT3 itself; the crystal structure (PDB 8DX0) confirms the kinase domain fold but the paper title notes 'weak ATP binding,' so full catalytic characterization on this specific protein may be limited.
- The conserved His identification in the sequence is based on pattern recognition of the H-box motif; without structural alignment confirmation, the exact phosphotransferable His position is inferred.
- The EC sub-number specificity (2.7.13.3 vs. 2.7.13.1 or 2.7.13.2) cannot be resolved from sequence alone, but this does not affect answerability since only one histidine kinase option is presented.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits a multi-transmembrane N-terminal sensor domain (several hydrophobic stretches in residues ~1-180) followed by a cytoplasmic kinase domain (~residues 208-361) containing a putative conserved phosphotransferable histidine in the context 'LIVYLAHDLRT' and a G-box-like motif 'GGDISAESKDE'. This two-component sensor histidine kinase architecture (TM sensor + His-kinase domain) is a hallmark of EC 2.7.13.x (protein-histidine kinases). It is incompatible with EC 1.1.1.1 (alcohol dehydrogenase, a soluble NAD⁺-dependent oxidoreductase with no TM helices or kinase motifs), EC 3.6.1.74 (a hydrolase acting on acid anhydrides, lacking kinase catalytic machinery), and EC 2.7.11.1 (cAMP-dependent protein kinase, a soluble serine/threonine kinase with a bilobal kinase fold containing VAIK/HRD/DFG motifs and no transmembrane sensor domain). Among the four options, only 2.7.13.3 matches the observed two-component sensor kinase architecture.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The specific sub-number 2.7.13.3 vs. other histidine kinase EC numbers is not independently derivable from sequence alone, but since only one histidine kinase option (2.7.13.3) is offered, the reasoning suffices to select it.",
    "reason": "The transmembrane sensor + kinase domain architecture, the conserved His phosphotransfer site, and the absence of features characteristic of serine/threonine kinases, oxidoreductases, or hydrolases provide concrete biological reasoning to select 2.7.13.3 over the three distractors without needing to recall the specific UniProt entry."
  },
  "case_id": "EC_number_0104",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q9KJT3 (sequence matched exactly, 361 aa) annotates this protein as Sensor protein VanSC / Vancomycin histidine protein kinase with EC 2.7.13.3. The catalytic activity (ATP + protein L-histidine → ADP + protein N-phospho-L-histidine) is consistent with a histidine kinase. The EC assignment carries evidence code ECO:0000250 (inferred by similarity from Q06240, a well-characterized VanS homolog), and a 1.45 Å crystal structure of the kinase domain (PDB 8DX0, residues 208-361, in complex with Mg²⁺) supports the kinase domain architecture. While the EC assignment is transferred by similarity rather than from direct enzymatic assay on this specific protein, the structural and homology evidence makes the annotation well-supported."
  },
  "important_caveats": [
    "The EC 2.7.13.3 annotation is transferred by similarity (ECO:0000250) from Q06240 rather than from a direct enzymatic assay on Q9KJT3 itself; the crystal structure (PDB 8DX0) confirms the kinase domain fold but the paper title notes 'weak ATP binding,' so full catalytic characterization on this specific protein may be limited.",
    "The conserved His identification in the sequence is based on pattern recognition of the H-box motif; without structural alignment confirmation, the exact phosphotransferable His position is inferred.",
    "The EC sub-number specificity (2.7.13.3 vs. 2.7.13.1 or 2.7.13.2) cannot be resolved from sequence alone, but this does not affect answerability since only one histidine kinase option is presented."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three distinct enzyme classes (oxidoreductase 1.1.1.1, hydrolase 3.6.1.74, transferase 2.7.x). Within transferases, the two options (2.7.11.1 serine/threonine kinase vs. 2.7.13.3 histidine kinase) are distinguishable by the two-component sensor kinase architecture and conserved His motif visible in the sequence. No ambiguity among the provided choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0104",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q9KJT3 (sequence matched exactly, 361 aa) annotates this protein as Sensor protein VanSC / Vancomycin histidine protein kinase with EC 2.7.13.3. The catalytic activity (ATP + protein L-histidine → ADP + protein N-phospho-L-histidine) is consistent with a histidine kinase. The EC assignment carries evidence code ECO:0000250 (inferred by similarity from Q06240, a well-characterized VanS homolog), and a 1.45 Å crystal structure of the kinase domain (PDB 8DX0, residues 208-361, in complex with Mg²⁺) supports the kinase domain architecture. While the EC assignment is transferred by similarity rather than from direct enzymatic assay on this specific protein, the structural and homology evidence makes the annotation well-supported.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits a multi-transmembrane N-terminal sensor domain (several hydrophobic stretches in residues ~1-180) followed by a cytoplasmic kinase domain (~residues 208-361) containing a putative conserved phosphotransferable histidine in the context 'LIVYLAHDLRT' and a G-box-like motif 'GGDISAESKDE'. This two-component sensor histidine kinase architecture (TM sensor + His-kinase domain) is a hallmark of EC 2.7.13.x (protein-histidine kinases). It is incompatible with EC 1.1.1.1 (alcohol dehydrogenase, a soluble NAD⁺-dependent oxidoreductase with no TM helices or kinase motifs), EC 3.6.1.74 (a hydrolase acting on acid anhydrides, lacking kinase catalytic machinery), and EC 2.7.11.1 (cAMP-dependent protein kinase, a soluble serine/threonine kinase with a bilobal kinase fold containing VAIK/HRD/DFG motifs and no transmembrane sensor domain). Among the four options, only 2.7.13.3 matches the observed two-component sensor kinase architecture.",
    "missing_item_specific_fact": "None critical. The specific sub-number 2.7.13.3 vs. other histidine kinase EC numbers is not independently derivable from sequence alone, but since only one histidine kinase option (2.7.13.3) is offered, the reasoning suffices to select it.",
    "reason": "The transmembrane sensor + kinase domain architecture, the conserved His phosphotransfer site, and the absence of features characteristic of serine/threonine kinases, oxidoreductases, or hydrolases provide concrete biological reasoning to select 2.7.13.3 over the three distractors without needing to recall the specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three distinct enzyme classes (oxidoreductase 1.1.1.1, hydrolase 3.6.1.74, transferase 2.7.x). Within transferases, the two options (2.7.11.1 serine/threonine kinase vs. 2.7.13.3 histidine kinase) are distinguishable by the two-component sensor kinase architecture and conserved His motif visible in the sequence. No ambiguity among the provided choices."
  },
  "important_caveats": [
    "The EC 2.7.13.3 annotation is transferred by similarity (ECO:0000250) from Q06240 rather than from a direct enzymatic assay on Q9KJT3 itself; the crystal structure (PDB 8DX0) confirms the kinase domain fold but the paper title notes 'weak ATP binding,' so full catalytic characterization on this specific protein may be limited.",
    "The conserved His identification in the sequence is based on pattern recognition of the H-box motif; without structural alignment confirmation, the exact phosphotransferable His position is inferred.",
    "The EC sub-number specificity (2.7.13.3 vs. 2.7.13.1 or 2.7.13.2) cannot be resolved from sequence alone, but this does not affect answerability since only one histidine kinase option is presented."
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

**Accession:** `Q9KJT3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 116. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KJT3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:57.402699+00:00.  

```json
"Q9KJT3"
```

Source SHA-256: `ee33b15ec361df125314162e4a4f908af9fa7205027ed66a72d0e347dc4cb508`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KJT3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:57.402699+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Vancomycin histidine protein kinase"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Vancomycin resistance protein VanSC"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q06240","source":"UniProtKB"}],"value":"2.7.13.3"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Sensor protein VanSC"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"VanS"},{"evidences":[{"evidenceCode":"ECO:0000303","id":"36764524","source":"PubMed"}],"value":"VanSC"}]}}
```

Source SHA-256: `ee33b15ec361df125314162e4a4f908af9fa7205027ed66a72d0e347dc4cb508`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KJT3.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:57.402699+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.7.13.3","evidences":[{"evidenceCode":"ECO:0000250","id":"Q06240","source":"UniProtKB"}],"name":"ATP + protein L-histidine = ADP + protein N-phospho-L-histidine."}}
```

Source SHA-256: `ee33b15ec361df125314162e4a4f908af9fa7205027ed66a72d0e347dc4cb508`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KJT3.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:57.402699+00:00.  

```json
{"citation":{"authors":["Grasty K.C.","Guzik C.","D'Lauro E.J.","Padrick S.B.","Beld J.","Loll P.J."],"citationCrossReferences":[{"database":"PubMed","id":"36764524"},{"database":"DOI","id":"10.1016/j.jbc.2023.103001"}],"citationType":"journal article","firstPage":"103001","id":"36764524","journal":"J. Biol. Chem.","lastPage":"103001","publicationDate":"2023","title":"Structure of VanS from vancomycin-resistant enterococci: A sensor kinase with weak ATP binding.","volume":"299"},"evidences":[{"evidenceCode":"ECO:0007744","id":"8DX0","source":"PDB"}],"referenceNumber":3,"referencePositions":["X-RAY CRYSTALLOGRAPHY (1.45 ANGSTROMS) OF 208-361 IN COMPLEX WITH MG(2+)"]}
```

Source SHA-256: `ee33b15ec361df125314162e4a4f908af9fa7205027ed66a72d0e347dc4cb508`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KJT3?format=txt&versions=116)  
**Locator:** `lines 6-11`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 116 / 1.  
**Retrieved:** 2026-11-02T04:33:04.938411+00:00.  

```text
DE   RecName: Full=Sensor protein VanSC {ECO:0000305};
DE            Short=VanS {ECO:0000305};
DE            Short=VanSC {ECO:0000303|PubMed:36764524};
DE            EC=2.7.13.3 {ECO:0000250|UniProtKB:Q06240};
DE   AltName: Full=Vancomycin histidine protein kinase {ECO:0000305};
DE   AltName: Full=Vancomycin resistance protein VanSC {ECO:0000305};
```

Source SHA-256: `3a9c1fbae546e8df9a94d1ae1786bc246e118381f34915268ec1ab8d8786c6af`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KJT3?format=txt&versions=116)  
**Locator:** `lines 32-38`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 116 / 1.  
**Retrieved:** 2026-11-02T04:33:04.938411+00:00.  

```text
RN   [3] {ECO:0007744|PDB:8DX0}
RP   X-RAY CRYSTALLOGRAPHY (1.45 ANGSTROMS) OF 208-361 IN COMPLEX WITH MG(2+).
RX   PubMed=36764524; DOI=10.1016/j.jbc.2023.103001;
RA   Grasty K.C., Guzik C., D'Lauro E.J., Padrick S.B., Beld J., Loll P.J.;
RT   "Structure of VanS from vancomycin-resistant enterococci: A sensor kinase
RT   with weak ATP binding.";
RL   J. Biol. Chem. 299:103001-103001(2023).
```

Source SHA-256: `3a9c1fbae546e8df9a94d1ae1786bc246e118381f34915268ec1ab8d8786c6af`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KJT3?format=txt&versions=116)  
**Locator:** `lines 39-41`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 116 / 1.  
**Retrieved:** 2026-11-02T04:33:04.938411+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=ATP + protein L-histidine = ADP + protein N-phospho-L-
CC         histidine.; EC=2.7.13.3; Evidence={ECO:0000250|UniProtKB:Q06240};
```

Source SHA-256: `3a9c1fbae546e8df9a94d1ae1786bc246e118381f34915268ec1ab8d8786c6af`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 104. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
