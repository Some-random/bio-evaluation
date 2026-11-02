# pathway_0023

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **C** — Amino-acid biosynthesis

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAVSSCARAFPSFECRSDAEFSGGIPRHDIPNSGKASILSHGSSVHGLSSLIYRFPPNFVRQLSIKARRNCSNIGVAQVVAASWSNNNSSPDFTPVAKAVDAAAAAAAAIAPVDTTVVNEDVALVENETCNDQNVQFDSLPSMKYASFLNSDGSVAIHAGERLGRGIVTDAITTPVVNTSAYFFNKTSELIDFKEKRRASFEYGRYGNPTTVVLEEKISALEGAESTLLMASGMCASTVMLLALVPAGGHIVTTTDCYRKTRIFIETILPKMGITATVIDPADVGALELALNQKKVNLFFTESPTNPFLRCVDIELVSKLCHEKGALVCIDGTFATPLNQKALALGADLVLHSATKFLGGHNDVLAGCISGPLKLVSEIRNLHHILGGALNPNAAYLIIRGMKTLHLRVQQQNSTALRMAEILEAHPKVRHVYYPGLQSHPEHHIAKKQMTGFGGVVSFEVDGDLLTTAKFVDALKIPYIAPSFGGCESIVDQPAIMSYWDLSQSDRAKYGIMDNLVRFSFGVEDFDDLKADILQALDSI

[Multiple Choices]
A. spheroidene biosynthesis. .
B. Lipid metabolism
C. Amino-acid biosynthesis
D. Cell wall biogenesis
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Pathway Prediction, which is to predict the primary metabolic or signaling pathway in which a given protein functions. Biological pathways are series of chemical reactions occurring within a cell that are essential for life. Based on the protein's amino acid sequence, you should identify the most relevant pathway from the given options.. The inputs provided by the user for this task include:

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

> The exact supplied sequence matches the tobacco chloroplastic cystathionine gamma-synthase 1 entry. Its pathway annotation places it in amino-acid biosynthesis, specifically de novo L-methionine biosynthesis; the annotation cites experimental evidence and a study of the enzyme's function and catalytic activity.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with a chloroplast-targeted enzyme, but that context does not by itself distinguish amino-acid biosynthesis from the other offered pathways. The specific cystathionine gamma-synthase function is not stated in the input.


**Missing item-specific fact**

> The protein's identity and experimentally supported function as cystathionine gamma-synthase, which links it to methionine and amino-acid biosynthesis.


**Reason**

> Choosing C depends on identifying this particular protein or knowing its specific enzyme function. That protein-specific fact is absent from the sequence prompt; recognizing the sequence from an external database would be lookup or memorization, not reasoning from supplied context alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched annotation supports amino-acid biosynthesis, and the choices do not present another pathway supported by the supplied evidence.


### Important caveats

- The supporting database annotation cites experimental evidence, but the reviewer-only sources were not available to the evaluated model.
- The sequence match establishes applicability of the retrieved annotation to this sequence; it does not establish what source or annotation was available to the question author.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a chloroplast-targeted enzyme, but that context does not by itself distinguish amino-acid biosynthesis from the other offered pathways. The specific cystathionine gamma-synthase function is not stated in the input.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's identity and experimentally supported function as cystathionine gamma-synthase, which links it to methionine and amino-acid biosynthesis.",
    "reason": "Choosing C depends on identifying this particular protein or knowing its specific enzyme function. That protein-specific fact is absent from the sequence prompt; recognizing the sequence from an external database would be lookup or memorization, not reasoning from supplied context alone."
  },
  "case_id": "pathway_0023",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the tobacco chloroplastic cystathionine gamma-synthase 1 entry. Its pathway annotation places it in amino-acid biosynthesis, specifically de novo L-methionine biosynthesis; the annotation cites experimental evidence and a study of the enzyme's function and catalytic activity."
  },
  "important_caveats": [
    "The supporting database annotation cites experimental evidence, but the reviewer-only sources were not available to the evaluated model.",
    "The sequence match establishes applicability of the retrieved annotation to this sequence; it does not establish what source or annotation was available to the question author."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation supports amino-acid biosynthesis, and the choices do not present another pathway supported by the supplied evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0023",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the tobacco chloroplastic cystathionine gamma-synthase 1 entry. Its pathway annotation places it in amino-acid biosynthesis, specifically de novo L-methionine biosynthesis; the annotation cites experimental evidence and a study of the enzyme's function and catalytic activity.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with a chloroplast-targeted enzyme, but that context does not by itself distinguish amino-acid biosynthesis from the other offered pathways. The specific cystathionine gamma-synthase function is not stated in the input.",
    "missing_item_specific_fact": "The protein's identity and experimentally supported function as cystathionine gamma-synthase, which links it to methionine and amino-acid biosynthesis.",
    "reason": "Choosing C depends on identifying this particular protein or knowing its specific enzyme function. That protein-specific fact is absent from the sequence prompt; recognizing the sequence from an external database would be lookup or memorization, not reasoning from supplied context alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation supports amino-acid biosynthesis, and the choices do not present another pathway supported by the supplied evidence."
  },
  "important_caveats": [
    "The supporting database annotation cites experimental evidence, but the reviewer-only sources were not available to the evaluated model.",
    "The sequence match establishes applicability of the retrieved annotation to this sequence; it does not establish what source or annotation was available to the question author."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9ZPL5 identifies the sequence as Cystathionine gamma-synthase 1, chloroplastic (EC 2.5.1.160) from Nicotiana tabacum. The pathway annotation explicitly states 'Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway; L-cystathionine from O-succinyl-L-homoserine: step 1/1' with experimental evidence (ECO:0000269, PubMed:10595588). The sequence matches exactly (SHA-256 confirmed). Choice C 'Amino-acid biosynthesis' is directly supported by the curated annotation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal region (MAVSSCARAFPSFECRSDAEFSGGIPRHDIPNSGKASILSHGSSVHGLSSLIYRFPPNFVRQLSIKARRNCSNIGVAQVVAASWSNNNSSPDFTPVAKAVDAAAAAAAAIAPVDTTVVNEDVALVENETCNDQNVQFDSLPSMKYASFLNSDGSVAIHAGERLGRGIVTDAITTPVVNTSAYFFNKTSELIDFKEKRRASFEYGRYGNPTTVVLEEKISALEGAESTLLMASGMCASTVMLLALVPAGGHIVTTTDCYRKTRIFIETILPKMGITATVIDPADVGALELALNQKKVNLFFTESPTNPFLRCVDIELVSKLCHEKGALVCIDGTFATPLNQKALALGADLVLHSATKFLGGHNDVLAGCISGPLKLVSEIRNLHHILGGALNPNAAYLIIRGMKTLHLRVQQQNSTALRMAEILEAHPKVRHVYYPGLQSHPEHHIAKKQMTGFGGVVSFEVDGDLLTTAKFVDALKIPYIAPSFGGCESIVDQPAIMSYWDLSQSDRAKYGIMDNLVRFSFGVEDFDDLKADILQALDSI) shows a chloroplast transit peptide (serine/threonine-rich, arginine-containing N-terminus with cleavage-site motifs), indicating a plastid-localized enzyme. The sequence length (~540 aa) and composition are consistent with a PLP-dependent enzyme of the aminotransferase/cystathionine gamma-synthase fold. The motif 'GGALNPNAAYLIIRGMKTLHLRVQQQ' contains a lysine in a context reminiscent of the PLP-binding lysine found in Class I aminotransferase-fold enzymes. PLP-dependent enzymes are overwhelmingly associated with amino-acid metabolism. Among the four options: (A) spheroidene biosynthesis is a bacterial carotenoid pathway, implausible for a plant chloroplast protein; (D) cell wall biogenesis involves glycosyltransferases/cellulose synthases with entirely different sequence features; (B) lipid metabolism enzymes (acyl-CoA synthetases, desaturases, lipases) do not use PLP cofactors and have different folds. The combination of chloroplast targeting, PLP-enzyme fold features, and elimination of the other three options provides a defensible biological argument pointing to amino-acid biosynthesis.


**Missing item-specific fact**

> Precise identification of the specific enzyme (cystathionine gamma-synthase) and its exact reaction (O-succinyl-L-homoserine → L-cystathionine) requires database lookup or expert knowledge of this particular protein. However, the question asks for the pathway class, not the specific enzyme, and the four options are sufficiently distinct that general reasoning about PLP-enzyme biology and organelle targeting can discriminate.


**Reason**

> The four pathway options span fundamentally different biochemical enzyme classes. A model recognizing the PLP-enzyme fold signature, chloroplast transit peptide, and absence of glycosyltransferase/lipid-metabolism/carotenoid-synthase features can eliminate three options through general biological knowledge. The reasoning does not require memorizing this specific protein's entry, though precise enzyme identification would.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent very different pathway classes with distinct enzyme types. Spheroidene biosynthesis (bacterial carotenoid pathway), cell wall biogenesis (glycosyltransferases), and lipid metabolism (acyl-CoA enzymes, desaturases) are all inconsistent with the observed sequence features. Only amino-acid biosynthesis aligns with a PLP-dependent chloroplast enzyme.


### Important caveats

- The reviewer evidence confirms the annotation with experimental evidence (ECO:0000269, PubMed:10595588), but this evidence was not available to the evaluated model.
- The sequence matches the UniProt entry exactly (SHA-256 confirmed for both current and historical versions).
- The entry was first public in June 2025 and integrated into Swiss-Prot in January 2026; the author's source snapshot date is unknown, but the historical version 110 (released Jan 2026) already contains the full pathway annotation.
- While the pathway-level answer is reasoning-supported, identifying the specific enzyme as cystathionine gamma-synthase (rather than, say, a serine acetyltransferase or another PLP enzyme in amino acid metabolism) would require more specialized knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal region (MAVSSCARAFPSFECRSDAEFSGGIPRHDIPNSGKASILSHGSSVHGLSSLIYRFPPNFVRQLSIKARRNCSNIGVAQVVAASWSNNNSSPDFTPVAKAVDAAAAAAAAIAPVDTTVVNEDVALVENETCNDQNVQFDSLPSMKYASFLNSDGSVAIHAGERLGRGIVTDAITTPVVNTSAYFFNKTSELIDFKEKRRASFEYGRYGNPTTVVLEEKISALEGAESTLLMASGMCASTVMLLALVPAGGHIVTTTDCYRKTRIFIETILPKMGITATVIDPADVGALELALNQKKVNLFFTESPTNPFLRCVDIELVSKLCHEKGALVCIDGTFATPLNQKALALGADLVLHSATKFLGGHNDVLAGCISGPLKLVSEIRNLHHILGGALNPNAAYLIIRGMKTLHLRVQQQNSTALRMAEILEAHPKVRHVYYPGLQSHPEHHIAKKQMTGFGGVVSFEVDGDLLTTAKFVDALKIPYIAPSFGGCESIVDQPAIMSYWDLSQSDRAKYGIMDNLVRFSFGVEDFDDLKADILQALDSI) shows a chloroplast transit peptide (serine/threonine-rich, arginine-containing N-terminus with cleavage-site motifs), indicating a plastid-localized enzyme. The sequence length (~540 aa) and composition are consistent with a PLP-dependent enzyme of the aminotransferase/cystathionine gamma-synthase fold. The motif 'GGALNPNAAYLIIRGMKTLHLRVQQQ' contains a lysine in a context reminiscent of the PLP-binding lysine found in Class I aminotransferase-fold enzymes. PLP-dependent enzymes are overwhelmingly associated with amino-acid metabolism. Among the four options: (A) spheroidene biosynthesis is a bacterial carotenoid pathway, implausible for a plant chloroplast protein; (D) cell wall biogenesis involves glycosyltransferases/cellulose synthases with entirely different sequence features; (B) lipid metabolism enzymes (acyl-CoA synthetases, desaturases, lipases) do not use PLP cofactors and have different folds. The combination of chloroplast targeting, PLP-enzyme fold features, and elimination of the other three options provides a defensible biological argument pointing to amino-acid biosynthesis.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise identification of the specific enzyme (cystathionine gamma-synthase) and its exact reaction (O-succinyl-L-homoserine → L-cystathionine) requires database lookup or expert knowledge of this particular protein. However, the question asks for the pathway class, not the specific enzyme, and the four options are sufficiently distinct that general reasoning about PLP-enzyme biology and organelle targeting can discriminate.",
    "reason": "The four pathway options span fundamentally different biochemical enzyme classes. A model recognizing the PLP-enzyme fold signature, chloroplast transit peptide, and absence of glycosyltransferase/lipid-metabolism/carotenoid-synthase features can eliminate three options through general biological knowledge. The reasoning does not require memorizing this specific protein's entry, though precise enzyme identification would."
  },
  "case_id": "pathway_0023",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q9ZPL5 identifies the sequence as Cystathionine gamma-synthase 1, chloroplastic (EC 2.5.1.160) from Nicotiana tabacum. The pathway annotation explicitly states 'Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway; L-cystathionine from O-succinyl-L-homoserine: step 1/1' with experimental evidence (ECO:0000269, PubMed:10595588). The sequence matches exactly (SHA-256 confirmed). Choice C 'Amino-acid biosynthesis' is directly supported by the curated annotation."
  },
  "important_caveats": [
    "The reviewer evidence confirms the annotation with experimental evidence (ECO:0000269, PubMed:10595588), but this evidence was not available to the evaluated model.",
    "The sequence matches the UniProt entry exactly (SHA-256 confirmed for both current and historical versions).",
    "The entry was first public in June 2025 and integrated into Swiss-Prot in January 2026; the author's source snapshot date is unknown, but the historical version 110 (released Jan 2026) already contains the full pathway annotation.",
    "While the pathway-level answer is reasoning-supported, identifying the specific enzyme as cystathionine gamma-synthase (rather than, say, a serine acetyltransferase or another PLP enzyme in amino acid metabolism) would require more specialized knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent very different pathway classes with distinct enzyme types. Spheroidene biosynthesis (bacterial carotenoid pathway), cell wall biogenesis (glycosyltransferases), and lipid metabolism (acyl-CoA enzymes, desaturases) are all inconsistent with the observed sequence features. Only amino-acid biosynthesis aligns with a PLP-dependent chloroplast enzyme."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0023",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9ZPL5 identifies the sequence as Cystathionine gamma-synthase 1, chloroplastic (EC 2.5.1.160) from Nicotiana tabacum. The pathway annotation explicitly states 'Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway; L-cystathionine from O-succinyl-L-homoserine: step 1/1' with experimental evidence (ECO:0000269, PubMed:10595588). The sequence matches exactly (SHA-256 confirmed). Choice C 'Amino-acid biosynthesis' is directly supported by the curated annotation.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal region (MAVSSCARAFPSFECRSDAEFSGGIPRHDIPNSGKASILSHGSSVHGLSSLIYRFPPNFVRQLSIKARRNCSNIGVAQVVAASWSNNNSSPDFTPVAKAVDAAAAAAAAIAPVDTTVVNEDVALVENETCNDQNVQFDSLPSMKYASFLNSDGSVAIHAGERLGRGIVTDAITTPVVNTSAYFFNKTSELIDFKEKRRASFEYGRYGNPTTVVLEEKISALEGAESTLLMASGMCASTVMLLALVPAGGHIVTTTDCYRKTRIFIETILPKMGITATVIDPADVGALELALNQKKVNLFFTESPTNPFLRCVDIELVSKLCHEKGALVCIDGTFATPLNQKALALGADLVLHSATKFLGGHNDVLAGCISGPLKLVSEIRNLHHILGGALNPNAAYLIIRGMKTLHLRVQQQNSTALRMAEILEAHPKVRHVYYPGLQSHPEHHIAKKQMTGFGGVVSFEVDGDLLTTAKFVDALKIPYIAPSFGGCESIVDQPAIMSYWDLSQSDRAKYGIMDNLVRFSFGVEDFDDLKADILQALDSI) shows a chloroplast transit peptide (serine/threonine-rich, arginine-containing N-terminus with cleavage-site motifs), indicating a plastid-localized enzyme. The sequence length (~540 aa) and composition are consistent with a PLP-dependent enzyme of the aminotransferase/cystathionine gamma-synthase fold. The motif 'GGALNPNAAYLIIRGMKTLHLRVQQQ' contains a lysine in a context reminiscent of the PLP-binding lysine found in Class I aminotransferase-fold enzymes. PLP-dependent enzymes are overwhelmingly associated with amino-acid metabolism. Among the four options: (A) spheroidene biosynthesis is a bacterial carotenoid pathway, implausible for a plant chloroplast protein; (D) cell wall biogenesis involves glycosyltransferases/cellulose synthases with entirely different sequence features; (B) lipid metabolism enzymes (acyl-CoA synthetases, desaturases, lipases) do not use PLP cofactors and have different folds. The combination of chloroplast targeting, PLP-enzyme fold features, and elimination of the other three options provides a defensible biological argument pointing to amino-acid biosynthesis.",
    "missing_item_specific_fact": "Precise identification of the specific enzyme (cystathionine gamma-synthase) and its exact reaction (O-succinyl-L-homoserine → L-cystathionine) requires database lookup or expert knowledge of this particular protein. However, the question asks for the pathway class, not the specific enzyme, and the four options are sufficiently distinct that general reasoning about PLP-enzyme biology and organelle targeting can discriminate.",
    "reason": "The four pathway options span fundamentally different biochemical enzyme classes. A model recognizing the PLP-enzyme fold signature, chloroplast transit peptide, and absence of glycosyltransferase/lipid-metabolism/carotenoid-synthase features can eliminate three options through general biological knowledge. The reasoning does not require memorizing this specific protein's entry, though precise enzyme identification would."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent very different pathway classes with distinct enzyme types. Spheroidene biosynthesis (bacterial carotenoid pathway), cell wall biogenesis (glycosyltransferases), and lipid metabolism (acyl-CoA enzymes, desaturases) are all inconsistent with the observed sequence features. Only amino-acid biosynthesis aligns with a PLP-dependent chloroplast enzyme."
  },
  "important_caveats": [
    "The reviewer evidence confirms the annotation with experimental evidence (ECO:0000269, PubMed:10595588), but this evidence was not available to the evaluated model.",
    "The sequence matches the UniProt entry exactly (SHA-256 confirmed for both current and historical versions).",
    "The entry was first public in June 2025 and integrated into Swiss-Prot in January 2026; the author's source snapshot date is unknown, but the historical version 110 (released Jan 2026) already contains the full pathway annotation.",
    "While the pathway-level answer is reasoning-supported, identifying the specific enzyme as cystathionine gamma-synthase (rather than, say, a serine acetyltransferase or another PLP enzyme in amino acid metabolism) would require more specialized knowledge."
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

**Accession:** `Q9ZPL5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 110. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZPL5.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:56.568005+00:00.  

```json
"Q9ZPL5"
```

Source SHA-256: `eba20b71fa68300db26e07dbef891aceaac0dafd788c516e4e6cd7e6d24a0088`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZPL5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:56.568005+00:00.  

```json
{"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"10595588","source":"PubMed"}],"value":"2.5.1.160"}],"fullName":{"value":"Cystathionine gamma-synthase 1, chloroplastic"}}}
```

Source SHA-256: `eba20b71fa68300db26e07dbef891aceaac0dafd788c516e4e6cd7e6d24a0088`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZPL5.json)  
**Locator:** `/comments/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:56.568005+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"10595588","source":"PubMed"}],"value":"Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway; L-cystathionine from O-succinyl-L-homoserine: step 1/1"}]}
```

Source SHA-256: `eba20b71fa68300db26e07dbef891aceaac0dafd788c516e4e6cd7e6d24a0088`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZPL5.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:56.568005+00:00.  

```json
{"citation":{"authors":["Clausen T.","Wahl M.C.","Messerschmidt A.","Huber R.","Fuhrmann J.C.","Laber B.","Streber W.","Steegborn C."],"citationCrossReferences":[{"database":"PubMed","id":"10595588"},{"database":"DOI","id":"10.1515/bc.1999.157"}],"citationType":"journal article","firstPage":"1237","id":"10595588","journal":"Biol. Chem.","lastPage":"1242","publicationDate":"1999","title":"Cloning, purification and characterisation of cystathionine gamma-synthase from Nicotiana tabacum.","volume":"380"},"referenceNumber":3,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA] OF 97-540","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","ACTIVITY REGULATION"]}
```

Source SHA-256: `eba20b71fa68300db26e07dbef891aceaac0dafd788c516e4e6cd7e6d24a0088`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZPL5?format=txt&versions=110)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 110 / 2.  
**Retrieved:** 2026-11-02T04:34:02.156603+00:00.  

```text
ID   CGS1_TOBAC              Reviewed;         540 AA.
AC   Q9ZPL5; W8SGH6;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   18-JUN-2025, sequence version 2.
DT   28-JAN-2026, entry version 110.
DE   RecName: Full=Cystathionine gamma-synthase 1, chloroplastic;
DE            EC=2.5.1.160 {ECO:0000269|PubMed:10595588};
DE   Flags: Precursor;
GN   Name=CGS1 {ECO:0000305}; ORFNames=LOC107822634;
OS   Nicotiana tabacum (Common tobacco).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   asterids; lamiids; Solanales; Solanaceae; Nicotianoideae; Nicotianeae;
OC   Nicotiana.
OX   NCBI_TaxID=4097;
```

Source SHA-256: `3437ba65b4e8147dfa9317dbc3f6f4d938558890b29fbadf232e8d98ba79ca89`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZPL5?format=txt&versions=110)  
**Locator:** `lines 29-37`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 110 / 2.  
**Retrieved:** 2026-11-02T04:34:02.156603+00:00.  

```text
RN   [3]
RP   NUCLEOTIDE SEQUENCE [MRNA] OF 97-540, FUNCTION, CATALYTIC ACTIVITY,
RP   BIOPHYSICOCHEMICAL PROPERTIES, AND ACTIVITY REGULATION.
RX   PubMed=10595588; DOI=10.1515/bc.1999.157;
RA   Clausen T., Wahl M.C., Messerschmidt A., Huber R., Fuhrmann J.C., Laber B.,
RA   Streber W., Steegborn C.;
RT   "Cloning, purification and characterisation of cystathionine gamma-synthase
RT   from Nicotiana tabacum.";
RL   Biol. Chem. 380:1237-1242(1999).
```

Source SHA-256: `3437ba65b4e8147dfa9317dbc3f6f4d938558890b29fbadf232e8d98ba79ca89`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZPL5?format=txt&versions=110)  
**Locator:** `lines 81-83`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 110 / 2.  
**Retrieved:** 2026-11-02T04:34:02.156603+00:00.  

```text
CC   -!- PATHWAY: Amino-acid biosynthesis; L-methionine biosynthesis via de novo
CC       pathway; L-cystathionine from O-succinyl-L-homoserine: step 1/1.
CC       {ECO:0000269|PubMed:10595588}.
```

Source SHA-256: `3437ba65b4e8147dfa9317dbc3f6f4d938558890b29fbadf232e8d98ba79ca89`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 23. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
