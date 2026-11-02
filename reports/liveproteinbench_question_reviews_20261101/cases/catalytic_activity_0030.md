# catalytic_activity_0030

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **C** — ATP + protein L-histidine = ADP + protein N-phospho-L-histidine.

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
A. N-methyl-3-methoxytyramine + S-adenosyl-L-methionine = N,N-dimethyl-3-methoxytyramine + S-adenosyl-L-homocysteine + H(+)
B. L-homoserine + acetyl-CoA = O-acetyl-L-homoserine + CoA
C. ATP + protein L-histidine = ADP + protein N-phospho-L-histidine.
D. L-homocysteine + H2O = 2-oxobutanoate + hydrogen sulfide + NH4(+) + H(+)
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

> The exact sequence matches a VanSC sensor histidine protein kinase annotation, whose listed catalytic reaction is ATP-dependent phosphorylation of protein histidine, matching C. The annotation is transferred by similarity (ECO:0000250), not direct experimental evidence for this sequence; the cited structure establishes structural study but does not itself demonstrate the reaction.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an N-terminal membrane-sensor region with hydrophobic segments followed by a cytoplasmic histidine-kinase region. Sensor histidine kinases use ATP to autophosphorylate a protein histidine, which matches C; the other options describe unrelated methylation, acetylation, or amino-acid degradation reactions.


**Missing item-specific fact**

> No protein-specific annotation is necessary to distinguish these choices at the enzyme-class level, though identifying this exact VanSC protein or verifying its activity experimentally would require external information.


**Reason**

> The sequence architecture and general biochemistry of two-component sensor histidine kinases provide a meaningful basis for selecting C among these choices, rather than relying only on recognition of the exact sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The listed reactions correspond to distinct enzyme classes, and the sequence supports the sensor histidine-kinase class.


### Important caveats

- The reviewer-only UniProt catalytic-activity annotation is similarity-transferred; it is not direct evidence of an assay on this exact protein.
- The cited structural study concerns a protein fragment and weak ATP binding, not direct validation of the catalytic reaction.
- The author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an N-terminal membrane-sensor region with hydrophobic segments followed by a cytoplasmic histidine-kinase region. Sensor histidine kinases use ATP to autophosphorylate a protein histidine, which matches C; the other options describe unrelated methylation, acetylation, or amino-acid degradation reactions.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No protein-specific annotation is necessary to distinguish these choices at the enzyme-class level, though identifying this exact VanSC protein or verifying its activity experimentally would require external information.",
    "reason": "The sequence architecture and general biochemistry of two-component sensor histidine kinases provide a meaningful basis for selecting C among these choices, rather than relying only on recognition of the exact sequence."
  },
  "case_id": "catalytic_activity_0030",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a VanSC sensor histidine protein kinase annotation, whose listed catalytic reaction is ATP-dependent phosphorylation of protein histidine, matching C. The annotation is transferred by similarity (ECO:0000250), not direct experimental evidence for this sequence; the cited structure establishes structural study but does not itself demonstrate the reaction."
  },
  "important_caveats": [
    "The reviewer-only UniProt catalytic-activity annotation is similarity-transferred; it is not direct evidence of an assay on this exact protein.",
    "The cited structural study concerns a protein fragment and weak ATP binding, not direct validation of the catalytic reaction.",
    "The author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The listed reactions correspond to distinct enzyme classes, and the sequence supports the sensor histidine-kinase class."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0030",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a VanSC sensor histidine protein kinase annotation, whose listed catalytic reaction is ATP-dependent phosphorylation of protein histidine, matching C. The annotation is transferred by similarity (ECO:0000250), not direct experimental evidence for this sequence; the cited structure establishes structural study but does not itself demonstrate the reaction.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an N-terminal membrane-sensor region with hydrophobic segments followed by a cytoplasmic histidine-kinase region. Sensor histidine kinases use ATP to autophosphorylate a protein histidine, which matches C; the other options describe unrelated methylation, acetylation, or amino-acid degradation reactions.",
    "missing_item_specific_fact": "No protein-specific annotation is necessary to distinguish these choices at the enzyme-class level, though identifying this exact VanSC protein or verifying its activity experimentally would require external information.",
    "reason": "The sequence architecture and general biochemistry of two-component sensor histidine kinases provide a meaningful basis for selecting C among these choices, rather than relying only on recognition of the exact sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The listed reactions correspond to distinct enzyme classes, and the sequence supports the sensor histidine-kinase class."
  },
  "important_caveats": [
    "The reviewer-only UniProt catalytic-activity annotation is similarity-transferred; it is not direct evidence of an assay on this exact protein.",
    "The cited structural study concerns a protein fragment and weak ATP binding, not direct validation of the catalytic reaction.",
    "The author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence (361 aa, SHA256 match confirmed) corresponds to UniProt Q9KJT3 (VANSC_ENTGA), annotated as Sensor protein VanSC / Vancomycin histidine protein kinase, EC 2.7.13.3. The catalytic activity comment (C5, H4) explicitly states 'ATP + protein L-histidine = ADP + protein N-phospho-L-histidine,' matching choice C exactly. The evidence code is ECO:0000250 (inferred by similarity from Q06240), so the annotation is by similarity transfer rather than direct experimental assay of this specific protein; however, the protein is named 'histidine protein kinase,' a crystal structure (PDB 8DX0) of VanS from vancomycin-resistant enterococci exists, and the domain architecture is consistent with histidine kinase function.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 361-aa sequence displays the canonical two-component sensor histidine kinase architecture: (1) an N-terminal hydrophobic transmembrane sensor region (~residues 1-50), (2) a linker/HAMP-like region, and (3) a C-terminal kinase domain containing the conserved H-box (phosphorylatable His in 'HLIDVQEEMNQLREKSLQDQRAAKEAEQRKNDLIVYLAHDLRT'), the conserved N-box, and the ATP-binding G-box with the diagnostic 'GK' motif ('GKTIPEEMIGRLFEPFYRMDSSRATATSGTGLGLPIAKEILLASGGDISAESKDETIIFNVRLPKPANN'). This H-box + G-box + transmembrane-sensor architecture is the hallmark of histidine kinases (EC 2.7.13.x) and is structurally incompatible with an O-methyltransferase (A), an acetyltransferase (B), or a cystathionine lyase (D), none of which possess transmembrane sensor domains or conserved His-phosphorylation/ATP-binding kinase motifs.


**Missing item-specific fact**

> None critical. The domain architecture is recognizable from general knowledge of histidine kinase motifs. The specific identity as VanSC (vs. any other sensor kinase) is not required to select the correct reaction, since all sensor histidine kinases catalyze the same core reaction (ATP + protein L-his → ADP + protein N-phospho-L-his).


**Reason**

> A biologist familiar with two-component signaling systems can identify the histidine kinase fold from the conserved H-box, G-box (GK), and transmembrane sensor architecture visible in the raw sequence, without needing to look up the specific UniProt entry. The four choices span entirely different enzyme classes (methyltransferase, acetyltransferase, kinase, lyase), making the domain-architecture argument sufficient to discriminate.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent mutually exclusive enzyme classes (O-methyltransferase, acetyltransferase, histidine kinase, cystathionine lyase). The histidine kinase domain architecture is distinctive and clearly incompatible with the other three. No ambiguity among choices.


### Important caveats

- The UniProt catalytic activity annotation carries evidence code ECO:0000250 (inferred by similarity from Q06240, the VanS from Enterococcus faecium), not direct experimental measurement of Q9KJT3's catalytic rate. However, the protein name, domain architecture, and published crystal structure (PDB 8DX0) of VanS strongly corroborate histidine kinase function.
- The EC 2.7.13.3 assignment is for a specific histidine kinase subclass; the general histidine kinase reaction (EC 2.7.13.1) is also catalyzed by this class of enzymes, but choice C's wording matches the database annotation exactly.
- The reviewed evidence is reviewer-only and was not available to the evaluated model; the model must rely on sequence-derived domain recognition.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 361-aa sequence displays the canonical two-component sensor histidine kinase architecture: (1) an N-terminal hydrophobic transmembrane sensor region (~residues 1-50), (2) a linker/HAMP-like region, and (3) a C-terminal kinase domain containing the conserved H-box (phosphorylatable His in 'HLIDVQEEMNQLREKSLQDQRAAKEAEQRKNDLIVYLAHDLRT'), the conserved N-box, and the ATP-binding G-box with the diagnostic 'GK' motif ('GKTIPEEMIGRLFEPFYRMDSSRATATSGTGLGLPIAKEILLASGGDISAESKDETIIFNVRLPKPANN'). This H-box + G-box + transmembrane-sensor architecture is the hallmark of histidine kinases (EC 2.7.13.x) and is structurally incompatible with an O-methyltransferase (A), an acetyltransferase (B), or a cystathionine lyase (D), none of which possess transmembrane sensor domains or conserved His-phosphorylation/ATP-binding kinase motifs.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The domain architecture is recognizable from general knowledge of histidine kinase motifs. The specific identity as VanSC (vs. any other sensor kinase) is not required to select the correct reaction, since all sensor histidine kinases catalyze the same core reaction (ATP + protein L-his → ADP + protein N-phospho-L-his).",
    "reason": "A biologist familiar with two-component signaling systems can identify the histidine kinase fold from the conserved H-box, G-box (GK), and transmembrane sensor architecture visible in the raw sequence, without needing to look up the specific UniProt entry. The four choices span entirely different enzyme classes (methyltransferase, acetyltransferase, kinase, lyase), making the domain-architecture argument sufficient to discriminate."
  },
  "case_id": "catalytic_activity_0030",
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
    "reason": "The sequence (361 aa, SHA256 match confirmed) corresponds to UniProt Q9KJT3 (VANSC_ENTGA), annotated as Sensor protein VanSC / Vancomycin histidine protein kinase, EC 2.7.13.3. The catalytic activity comment (C5, H4) explicitly states 'ATP + protein L-histidine = ADP + protein N-phospho-L-histidine,' matching choice C exactly. The evidence code is ECO:0000250 (inferred by similarity from Q06240), so the annotation is by similarity transfer rather than direct experimental assay of this specific protein; however, the protein is named 'histidine protein kinase,' a crystal structure (PDB 8DX0) of VanS from vancomycin-resistant enterococci exists, and the domain architecture is consistent with histidine kinase function."
  },
  "important_caveats": [
    "The UniProt catalytic activity annotation carries evidence code ECO:0000250 (inferred by similarity from Q06240, the VanS from Enterococcus faecium), not direct experimental measurement of Q9KJT3's catalytic rate. However, the protein name, domain architecture, and published crystal structure (PDB 8DX0) of VanS strongly corroborate histidine kinase function.",
    "The EC 2.7.13.3 assignment is for a specific histidine kinase subclass; the general histidine kinase reaction (EC 2.7.13.1) is also catalyzed by this class of enzymes, but choice C's wording matches the database annotation exactly.",
    "The reviewed evidence is reviewer-only and was not available to the evaluated model; the model must rely on sequence-derived domain recognition."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent mutually exclusive enzyme classes (O-methyltransferase, acetyltransferase, histidine kinase, cystathionine lyase). The histidine kinase domain architecture is distinctive and clearly incompatible with the other three. No ambiguity among choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0030",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence (361 aa, SHA256 match confirmed) corresponds to UniProt Q9KJT3 (VANSC_ENTGA), annotated as Sensor protein VanSC / Vancomycin histidine protein kinase, EC 2.7.13.3. The catalytic activity comment (C5, H4) explicitly states 'ATP + protein L-histidine = ADP + protein N-phospho-L-histidine,' matching choice C exactly. The evidence code is ECO:0000250 (inferred by similarity from Q06240), so the annotation is by similarity transfer rather than direct experimental assay of this specific protein; however, the protein is named 'histidine protein kinase,' a crystal structure (PDB 8DX0) of VanS from vancomycin-resistant enterococci exists, and the domain architecture is consistent with histidine kinase function.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 361-aa sequence displays the canonical two-component sensor histidine kinase architecture: (1) an N-terminal hydrophobic transmembrane sensor region (~residues 1-50), (2) a linker/HAMP-like region, and (3) a C-terminal kinase domain containing the conserved H-box (phosphorylatable His in 'HLIDVQEEMNQLREKSLQDQRAAKEAEQRKNDLIVYLAHDLRT'), the conserved N-box, and the ATP-binding G-box with the diagnostic 'GK' motif ('GKTIPEEMIGRLFEPFYRMDSSRATATSGTGLGLPIAKEILLASGGDISAESKDETIIFNVRLPKPANN'). This H-box + G-box + transmembrane-sensor architecture is the hallmark of histidine kinases (EC 2.7.13.x) and is structurally incompatible with an O-methyltransferase (A), an acetyltransferase (B), or a cystathionine lyase (D), none of which possess transmembrane sensor domains or conserved His-phosphorylation/ATP-binding kinase motifs.",
    "missing_item_specific_fact": "None critical. The domain architecture is recognizable from general knowledge of histidine kinase motifs. The specific identity as VanSC (vs. any other sensor kinase) is not required to select the correct reaction, since all sensor histidine kinases catalyze the same core reaction (ATP + protein L-his → ADP + protein N-phospho-L-his).",
    "reason": "A biologist familiar with two-component signaling systems can identify the histidine kinase fold from the conserved H-box, G-box (GK), and transmembrane sensor architecture visible in the raw sequence, without needing to look up the specific UniProt entry. The four choices span entirely different enzyme classes (methyltransferase, acetyltransferase, kinase, lyase), making the domain-architecture argument sufficient to discriminate."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent mutually exclusive enzyme classes (O-methyltransferase, acetyltransferase, histidine kinase, cystathionine lyase). The histidine kinase domain architecture is distinctive and clearly incompatible with the other three. No ambiguity among choices."
  },
  "important_caveats": [
    "The UniProt catalytic activity annotation carries evidence code ECO:0000250 (inferred by similarity from Q06240, the VanS from Enterococcus faecium), not direct experimental measurement of Q9KJT3's catalytic rate. However, the protein name, domain architecture, and published crystal structure (PDB 8DX0) of VanS strongly corroborate histidine kinase function.",
    "The EC 2.7.13.3 assignment is for a specific histidine kinase subclass; the general histidine kinase reaction (EC 2.7.13.1) is also catalyzed by this class of enzymes, but choice C's wording matches the database annotation exactly.",
    "The reviewed evidence is reviewer-only and was not available to the evaluated model; the model must rely on sequence-derived domain recognition."
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

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KJT3?format=txt&versions=116)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 116 / 1.  
**Retrieved:** 2026-11-02T04:33:04.938411+00:00.  

```text
ID   VANSC_ENTGA             Reviewed;         361 AA.
AC   Q9KJT3;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-OCT-2000, sequence version 1.
DT   28-JAN-2026, entry version 116.
DE   RecName: Full=Sensor protein VanSC {ECO:0000305};
DE            Short=VanS {ECO:0000305};
DE            Short=VanSC {ECO:0000303|PubMed:36764524};
DE            EC=2.7.13.3 {ECO:0000250|UniProtKB:Q06240};
DE   AltName: Full=Vancomycin histidine protein kinase {ECO:0000305};
DE   AltName: Full=Vancomycin resistance protein VanSC {ECO:0000305};
GN   Name=vanSc {ECO:0000312|EMBL:AAF86642.1};
OS   Enterococcus gallinarum.
OC   Bacteria; Bacillati; Bacillota; Bacilli; Lactobacillales; Enterococcaceae;
OC   Enterococcus.
OX   NCBI_TaxID=1353 {ECO:0000312|EMBL:AAF86642.1};
```

Source SHA-256: `3a9c1fbae546e8df9a94d1ae1786bc246e118381f34915268ec1ab8d8786c6af`.

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

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 30. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
