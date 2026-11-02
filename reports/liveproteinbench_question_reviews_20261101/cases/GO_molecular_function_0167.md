# GO_molecular_function_0167

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **B** — phosphorelay sensor kinase activity

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
A. nucleoside transmembrane transporter activity
B. phosphorelay sensor kinase activity
C. histone H3K9me/H3K9me2 demethylase activity
D. protein dimerization activity
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Molecular Function Prediction, which is to predict the fundamental activity of a protein at the molecular level, as defined by the Gene Ontology (GO) 'Molecular Function' branch. This describes the elemental tasks a protein performs, such as catalysis, transport, or binding to specific molecules. Based on the protein's amino acid sequence, you are to select the option that best describes its primary molecular function.. The inputs provided by the user for this task include:

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

> The exact sequence matches the VanSC sensor protein entry, which is annotated as a VanS sensor histidine kinase and with phosphorelay sensor kinase activity. The catalytic reaction annotation is transferred by similarity, so this supports the key but is not direct experimental proof of activity for this sequence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H3](#evidence-h3), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an N-terminal hydrophobic membrane-spanning region followed by a substantial cytoplasmic region with a histidine-kinase-like catalytic architecture, consistent with a membrane sensor kinase. This distinguishes B from a nucleoside transporter, which would be expected to have a transporter-like multi-pass membrane architecture, and from the eukaryotic histone demethylase option.


**Missing item-specific fact**

> No specific external fact is necessary for the broad distinction among these choices; identifying this exact VanS protein would require item-specific annotation or prior knowledge, but the sequence features support B without that identification.


**Reason**

> The sequence and options provide meaningful architectural evidence for a membrane-associated sensor histidine kinase. The reviewer-only annotation corroborates that inference but is not information supplied to the original model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence architecture strongly favors a sensor histidine kinase over the listed alternatives.


### Important caveats

- The sequence-matched UniProt catalytic activity evidence is transferred from a homolog; the supplied evidence does not establish a direct biochemical assay of this exact protein.
- The phosphorelay sensor kinase GO annotation is computational (InterPro IEA), not experimental.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an N-terminal hydrophobic membrane-spanning region followed by a substantial cytoplasmic region with a histidine-kinase-like catalytic architecture, consistent with a membrane sensor kinase. This distinguishes B from a nucleoside transporter, which would be expected to have a transporter-like multi-pass membrane architecture, and from the eukaryotic histone demethylase option.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No specific external fact is necessary for the broad distinction among these choices; identifying this exact VanS protein would require item-specific annotation or prior knowledge, but the sequence features support B without that identification.",
    "reason": "The sequence and options provide meaningful architectural evidence for a membrane-associated sensor histidine kinase. The reviewer-only annotation corroborates that inference but is not information supplied to the original model."
  },
  "case_id": "GO_molecular_function_0167",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C7",
      "H3",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the VanSC sensor protein entry, which is annotated as a VanS sensor histidine kinase and with phosphorelay sensor kinase activity. The catalytic reaction annotation is transferred by similarity, so this supports the key but is not direct experimental proof of activity for this sequence."
  },
  "important_caveats": [
    "The sequence-matched UniProt catalytic activity evidence is transferred from a homolog; the supplied evidence does not establish a direct biochemical assay of this exact protein.",
    "The phosphorelay sensor kinase GO annotation is computational (InterPro IEA), not experimental."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence architecture strongly favors a sensor histidine kinase over the listed alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0167",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the VanSC sensor protein entry, which is annotated as a VanS sensor histidine kinase and with phosphorelay sensor kinase activity. The catalytic reaction annotation is transferred by similarity, so this supports the key but is not direct experimental proof of activity for this sequence.",
    "evidence_ids": ["C1", "C4", "C5", "C7", "H3", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an N-terminal hydrophobic membrane-spanning region followed by a substantial cytoplasmic region with a histidine-kinase-like catalytic architecture, consistent with a membrane sensor kinase. This distinguishes B from a nucleoside transporter, which would be expected to have a transporter-like multi-pass membrane architecture, and from the eukaryotic histone demethylase option.",
    "missing_item_specific_fact": "No specific external fact is necessary for the broad distinction among these choices; identifying this exact VanS protein would require item-specific annotation or prior knowledge, but the sequence features support B without that identification.",
    "reason": "The sequence and options provide meaningful architectural evidence for a membrane-associated sensor histidine kinase. The reviewer-only annotation corroborates that inference but is not information supplied to the original model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence architecture strongly favors a sensor histidine kinase over the listed alternatives."
  },
  "important_caveats": [
    "The sequence-matched UniProt catalytic activity evidence is transferred from a homolog; the supplied evidence does not establish a direct biochemical assay of this exact protein.",
    "The phosphorelay sensor kinase GO annotation is computational (InterPro IEA), not experimental."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt Q9KJT3 (Sensor protein VanSC from Enterococcus gallinarum) is annotated with GO:0000155 'phosphorelay sensor kinase activity' (IEA:InterPro, C7) and GO:0004673 'protein histidine kinase activity' (ISS, C8). The EC number 2.7.13.3 (histidine kinase) and catalytic reaction 'ATP + protein L-histidine = ADP + protein N-phospho-L-histidine' (C5/H3) confirm the kinase activity. The protein name 'Sensor protein VanSC' (C4) and the GO term definition (GO1: 'Catalysis of the phosphorylation of a histidine residue in response to detection of an extracellular signal...to initiate a change in cell state') directly match option B. The X-ray structure of residues 208-361 (C9/H2) confirms the kinase domain fold. Evidence is primarily computational (IEA/ISS), but the annotation is consistent and well-established for this two-component system protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [C8](#evidence-c8), [GO1](#evidence-go1), [H3](#evidence-h3), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits the canonical two-component system sensor kinase architecture: (1) N-terminal region (~residues 1-200) contains multiple hydrophobic stretches consistent with transmembrane helices forming a sensor domain; (2) a conserved histidine in the 'H-box' region (AHDLRTPL, ~residue 210) serving as the phosphorylation site; (3) C-terminal region (~residues 200-361) contains recognizable histidine kinase ATP-binding motifs (GK in 'GKTIPE', GT/GR in 'GTGLGLPIAKEILLASGG') characteristic of the HATPase_c domain. This TM-sensor + kinase-domain combination is the hallmark of a two-component phosphorelay sensor kinase. Option A (nucleoside transporter) is excluded by the absence of nucleoside-binding motifs and presence of kinase motifs. Option C (H3K9 demethylase) is excluded as a bacterial protein lacking any JmjC/Fe(II)-2OG dioxygenase domain. Option D (dimerization) is a secondary structural property, not the primary catalytic molecular function.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence architecture provides concrete, recognizable domain features (transmembrane sensor region + conserved His phosphorylation site + ATP-binding kinase motifs) that a model trained on general molecular biology can identify as diagnostic of a two-component sensor kinase. The distractors are eliminable through domain logic: no nucleoside transporter motifs, no eukaryotic demethylase domain, and dimerization is not a primary catalytic function. This is a well-known protein family (two-component systems) with conserved architectural signatures.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The primary molecular function of a two-component sensor kinase is unambiguously the phosphorelay sensor kinase activity (GO:0000155). While sensor kinases do dimerize (making D a true but secondary property), the question asks for 'primary molecular function,' and the catalytic kinase activity is the defining function. The other options (A, C) are clearly incompatible with the sequence.


### Important caveats

- The GO:0000155 annotation carries evidence code IEA:InterPro (computational inference from domain match), not direct experimental validation of phosphorelay activity for this specific protein.
- The EC assignment (2.7.13.3) is transferred by similarity (ECO:0000250) from Q06240 (VanS from Enterococcus faecium), not independently measured for Q9KJT3.
- The X-ray structure (PDB 8DX0) covers only residues 208-361 (kinase domain) and confirms the fold but does not directly demonstrate phosphorelay activity.
- The protein dimerization activity (D) is technically true for sensor kinases but is not their primary molecular function as defined by GO.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits the canonical two-component system sensor kinase architecture: (1) N-terminal region (~residues 1-200) contains multiple hydrophobic stretches consistent with transmembrane helices forming a sensor domain; (2) a conserved histidine in the 'H-box' region (AHDLRTPL, ~residue 210) serving as the phosphorylation site; (3) C-terminal region (~residues 200-361) contains recognizable histidine kinase ATP-binding motifs (GK in 'GKTIPE', GT/GR in 'GTGLGLPIAKEILLASGG') characteristic of the HATPase_c domain. This TM-sensor + kinase-domain combination is the hallmark of a two-component phosphorelay sensor kinase. Option A (nucleoside transporter) is excluded by the absence of nucleoside-binding motifs and presence of kinase motifs. Option C (H3K9 demethylase) is excluded as a bacterial protein lacking any JmjC/Fe(II)-2OG dioxygenase domain. Option D (dimerization) is a secondary structural property, not the primary catalytic molecular function.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence architecture provides concrete, recognizable domain features (transmembrane sensor region + conserved His phosphorylation site + ATP-binding kinase motifs) that a model trained on general molecular biology can identify as diagnostic of a two-component sensor kinase. The distractors are eliminable through domain logic: no nucleoside transporter motifs, no eukaryotic demethylase domain, and dimerization is not a primary catalytic function. This is a well-known protein family (two-component systems) with conserved architectural signatures."
  },
  "case_id": "GO_molecular_function_0167",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "C8",
      "GO1",
      "H3",
      "H7"
    ],
    "judgment": "supported",
    "reason": "UniProt Q9KJT3 (Sensor protein VanSC from Enterococcus gallinarum) is annotated with GO:0000155 'phosphorelay sensor kinase activity' (IEA:InterPro, C7) and GO:0004673 'protein histidine kinase activity' (ISS, C8). The EC number 2.7.13.3 (histidine kinase) and catalytic reaction 'ATP + protein L-histidine = ADP + protein N-phospho-L-histidine' (C5/H3) confirm the kinase activity. The protein name 'Sensor protein VanSC' (C4) and the GO term definition (GO1: 'Catalysis of the phosphorylation of a histidine residue in response to detection of an extracellular signal...to initiate a change in cell state') directly match option B. The X-ray structure of residues 208-361 (C9/H2) confirms the kinase domain fold. Evidence is primarily computational (IEA/ISS), but the annotation is consistent and well-established for this two-component system protein."
  },
  "important_caveats": [
    "The GO:0000155 annotation carries evidence code IEA:InterPro (computational inference from domain match), not direct experimental validation of phosphorelay activity for this specific protein.",
    "The EC assignment (2.7.13.3) is transferred by similarity (ECO:0000250) from Q06240 (VanS from Enterococcus faecium), not independently measured for Q9KJT3.",
    "The X-ray structure (PDB 8DX0) covers only residues 208-361 (kinase domain) and confirms the fold but does not directly demonstrate phosphorelay activity.",
    "The protein dimerization activity (D) is technically true for sensor kinases but is not their primary molecular function as defined by GO."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The primary molecular function of a two-component sensor kinase is unambiguously the phosphorelay sensor kinase activity (GO:0000155). While sensor kinases do dimerize (making D a true but secondary property), the question asks for 'primary molecular function,' and the catalytic kinase activity is the defining function. The other options (A, C) are clearly incompatible with the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0167",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt Q9KJT3 (Sensor protein VanSC from Enterococcus gallinarum) is annotated with GO:0000155 'phosphorelay sensor kinase activity' (IEA:InterPro, C7) and GO:0004673 'protein histidine kinase activity' (ISS, C8). The EC number 2.7.13.3 (histidine kinase) and catalytic reaction 'ATP + protein L-histidine = ADP + protein N-phospho-L-histidine' (C5/H3) confirm the kinase activity. The protein name 'Sensor protein VanSC' (C4) and the GO term definition (GO1: 'Catalysis of the phosphorylation of a histidine residue in response to detection of an extracellular signal...to initiate a change in cell state') directly match option B. The X-ray structure of residues 208-361 (C9/H2) confirms the kinase domain fold. Evidence is primarily computational (IEA/ISS), but the annotation is consistent and well-established for this two-component system protein.",
    "evidence_ids": ["C4", "C5", "C7", "C8", "GO1", "H3", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits the canonical two-component system sensor kinase architecture: (1) N-terminal region (~residues 1-200) contains multiple hydrophobic stretches consistent with transmembrane helices forming a sensor domain; (2) a conserved histidine in the 'H-box' region (AHDLRTPL, ~residue 210) serving as the phosphorylation site; (3) C-terminal region (~residues 200-361) contains recognizable histidine kinase ATP-binding motifs (GK in 'GKTIPE', GT/GR in 'GTGLGLPIAKEILLASGG') characteristic of the HATPase_c domain. This TM-sensor + kinase-domain combination is the hallmark of a two-component phosphorelay sensor kinase. Option A (nucleoside transporter) is excluded by the absence of nucleoside-binding motifs and presence of kinase motifs. Option C (H3K9 demethylase) is excluded as a bacterial protein lacking any JmjC/Fe(II)-2OG dioxygenase domain. Option D (dimerization) is a secondary structural property, not the primary catalytic molecular function.",
    "missing_item_specific_fact": "",
    "reason": "The sequence architecture provides concrete, recognizable domain features (transmembrane sensor region + conserved His phosphorylation site + ATP-binding kinase motifs) that a model trained on general molecular biology can identify as diagnostic of a two-component sensor kinase. The distractors are eliminable through domain logic: no nucleoside transporter motifs, no eukaryotic demethylase domain, and dimerization is not a primary catalytic function. This is a well-known protein family (two-component systems) with conserved architectural signatures."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The primary molecular function of a two-component sensor kinase is unambiguously the phosphorelay sensor kinase activity (GO:0000155). While sensor kinases do dimerize (making D a true but secondary property), the question asks for 'primary molecular function,' and the catalytic kinase activity is the defining function. The other options (A, C) are clearly incompatible with the sequence."
  },
  "important_caveats": [
    "The GO:0000155 annotation carries evidence code IEA:InterPro (computational inference from domain match), not direct experimental validation of phosphorelay activity for this specific protein.",
    "The EC assignment (2.7.13.3) is transferred by similarity (ECO:0000250) from Q06240 (VanS from Enterococcus faecium), not independently measured for Q9KJT3.",
    "The X-ray structure (PDB 8DX0) covers only residues 208-361 (kinase domain) and confirms the fold but does not directly demonstrate phosphorelay activity.",
    "The protein dimerization activity (D) is technically true for sensor kinases but is not their primary molecular function as defined by GO."
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
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

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

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KJT3.json)  
**Locator:** `/uniProtKBCrossReferences/9`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:57.402699+00:00.  

```json
{"database":"GO","id":"GO:0000155","properties":[{"key":"GoTerm","value":"F:phosphorelay sensor kinase activity"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `ee33b15ec361df125314162e4a4f908af9fa7205027ed66a72d0e347dc4cb508`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KJT3.json)  
**Locator:** `/uniProtKBCrossReferences/10`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:57.402699+00:00.  

```json
{"database":"GO","id":"GO:0004673","properties":[{"key":"GoTerm","value":"F:protein histidine kinase activity"},{"key":"GoEvidenceType","value":"ISS:UniProtKB"}]}
```

Source SHA-256: `ee33b15ec361df125314162e4a4f908af9fa7205027ed66a72d0e347dc4cb508`.

### Evidence C9

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

### Evidence H3

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

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KJT3?format=txt&versions=116)  
**Locator:** `lines 64-64`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 116 / 1.  
**Retrieved:** 2026-11-02T04:33:04.938411+00:00.  

```text
DR   GO; GO:0000155; F:phosphorelay sensor kinase activity; IEA:InterPro.
```

Source SHA-256: `3a9c1fbae546e8df9a94d1ae1786bc246e118381f34915268ec1ab8d8786c6af`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 1549-1560`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0000155
name: phosphorelay sensor kinase activity
namespace: molecular_function
def: "Catalysis of the phosphorylation of a histidine residue in response to detection of an extracellular signal such as a chemical ligand or change in environment, to initiate a change in cell state or activity. The two-component sensor is a histidine kinase that autophosphorylates a histidine residue in its active site. The phosphate is then transferred to an aspartate residue in a downstream response regulator, to trigger a response." [GOC:bf, GOC:mcc, PMID:10966457, PMID:20223701, PMID:31386843, PMID:9191038]
synonym: "two-component sensor activity" NARROW []
synonym: "two-component sensor molecule" NARROW []
synonym: "two-component system sensor activity" NARROW []
is_a: GO:0004673 ! protein histidine kinase activity
is_a: GO:0140299 ! molecular sensor activity
property_value: skos:broadMatch EC:2.7.13.3

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 167. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
