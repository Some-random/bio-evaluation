# catalytic_activity_0193

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **D** — a beta-lactam + H2O = a substituted beta-amino acid

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MRVLALSAVFLVASIIGMPAVAKEWQENKSWNAHFTEHKSQGVVVLWNENKQQGFTNNLKRANQAFLPASTFKIPNSLIALDLGVVKDEHQVFKWDGQTRDIATWNRDHNLITAMKYSVVPVYQEFARQIGEARMSKMLHAFDYGNEDISGNVDSFWLDGGIRISATEQISFLRKLYHNKLHVSERSQRIVKQAMLTEANGDYIIRAKTGYSTRIEPKIGWWVGWVELDDNVWFFAMNMDMPTSDGLGLRQAITKEVLKQEKIIP

[Multiple Choices]
A. 3-oxocapnine + NADPH + H(+) = capnine + NADP(+)
B. Hydrolysis of terminal non-reducing alpha-L-arabinofuranoside residues in alpha-L-arabinosides.
C. L-arabinitol + NAD(+) = L-xylulose + NADH + H(+)
D. a beta-lactam + H2O = a substituted beta-amino acid
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

> The exact sequence matches the OXA-48 beta-lactamase entry, whose annotated catalytic reaction is beta-lactam hydrolysis to a substituted beta-amino acid. The annotation cites experimental evidence, although the underlying papers were not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H7](#evidence-h7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence includes a hydrophobic N-terminal region consistent with export, but that alone does not identify its catalytic reaction or distinguish beta-lactam hydrolysis from the other listed activities.


**Missing item-specific fact**

> The sequence's identity as OXA-48, a class D beta-lactamase, and its beta-lactam hydrolysis activity are not supplied in the question.


**Reason**

> Selecting D depends on identifying this particular protein or obtaining its functional annotation; exact sequence recognition or recalling a database entry is lookup or memorization, not a biological argument provided by the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched annotation supports D, and no supplied evidence supports another listed reaction.


### Important caveats

- The reviewer-only evidence was not available to the evaluated model.
- The exact sequence match and historical annotation support applicability, but the primary experimental studies were not independently examined.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence includes a hydrophobic N-terminal region consistent with export, but that alone does not identify its catalytic reaction or distinguish beta-lactam hydrolysis from the other listed activities.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence's identity as OXA-48, a class D beta-lactamase, and its beta-lactam hydrolysis activity are not supplied in the question.",
    "reason": "Selecting D depends on identifying this particular protein or obtaining its functional annotation; exact sequence recognition or recalling a database entry is lookup or memorization, not a biological argument provided by the input."
  },
  "case_id": "catalytic_activity_0193",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the OXA-48 beta-lactamase entry, whose annotated catalytic reaction is beta-lactam hydrolysis to a substituted beta-amino acid. The annotation cites experimental evidence, although the underlying papers were not independently reviewed here."
  },
  "important_caveats": [
    "The reviewer-only evidence was not available to the evaluated model.",
    "The exact sequence match and historical annotation support applicability, but the primary experimental studies were not independently examined."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation supports D, and no supplied evidence supports another listed reaction."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0193",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the OXA-48 beta-lactamase entry, whose annotated catalytic reaction is beta-lactam hydrolysis to a substituted beta-amino acid. The annotation cites experimental evidence, although the underlying papers were not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence includes a hydrophobic N-terminal region consistent with export, but that alone does not identify its catalytic reaction or distinguish beta-lactam hydrolysis from the other listed activities.",
    "missing_item_specific_fact": "The sequence's identity as OXA-48, a class D beta-lactamase, and its beta-lactam hydrolysis activity are not supplied in the question.",
    "reason": "Selecting D depends on identifying this particular protein or obtaining its functional annotation; exact sequence recognition or recalling a database entry is lookup or memorization, not a biological argument provided by the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation supports D, and no supplied evidence supports another listed reaction."
  },
  "important_caveats": [
    "The reviewer-only evidence was not available to the evaluated model.",
    "The exact sequence match and historical annotation support applicability, but the primary experimental studies were not independently examined."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt Q6XEC0 (Beta-lactamase OXA-48, EC 3.5.2.6) exactly (265 aa, sequence SHA256 identical). The catalytic activity 'a beta-lactam + H2O = a substituted beta-amino acid' is annotated with multiple experimental evidence codes (ECO:0000269) from four independent publications (PubMed:14693513, 19477418, 27073009, 38161376) including X-ray crystallography (PDB: 3HBR, 5HAP, 5HAQ, 7O5N, 7O9N) and functional assays. The Rhea cross-reference RHEA:20401 confirms the reaction. The expected answer D is directly and experimentally supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [H2](#evidence-h2), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the S-x-x-K active-site motif (S70-T-F-K73, visible as 'PASTFKIP' in the sequence) and the KTG motif (K208-T209-G210, visible as 'AKTGY'), both hallmarks of class D serine beta-lactamases (oxacillinases). Additionally, the N-terminal hydrophobic stretch (MRVLALSAVFLVASIIGMPAVA) is a classic bacterial signal peptide consistent with periplasmic localization of beta-lactamases. These motifs are general, textbook-level features of class D beta-lactamases and are incompatible with the other choices: (A) an NADPH-dependent reductase would require a Rossmann-fold GxGxxG motif absent here; (B) a glycosidase would show different catalytic residue arrangements; (C) an NAD+-dependent dehydrogenase would also require a Rossmann fold. Recognizing S-x-x-K and KTG as class D beta-lactamase signatures and linking them to beta-lactam hydrolysis is standard enzymological knowledge.


**Missing item-specific fact**

> None critical. The model does not need to know this is specifically OXA-48; identifying the class D beta-lactamase fold from S-x-x-K and KTG motifs suffices to select D over the other three mechanistically distinct options.


**Reason**

> The S-x-x-K and KTG motifs are well-established, general structural signatures of class D beta-lactamases taught in standard biochemistry and microbiology. Their presence in the sequence, combined with the signal peptide and absence of Rossmann-fold or glycosidase motifs, provides a concrete biological argument distinguishing D from A, B, and C without requiring memorization of this particular protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The S-x-x-K and KTG motifs are highly specific to class D beta-lactamases. The other three choices involve fundamentally different enzyme classes (NADPH reductase, glycosidase, NAD+ dehydrogenase) with incompatible structural requirements. No alternative choice is defensible given the sequence features.


### Important caveats

- The S-x-x-K motif identification requires the model to correctly locate the motif within the 265-residue sequence and recognize it as a class D beta-lactamase signature rather than a coincidental S-x-x-K pattern; however, the co-occurrence with KTG and the signal peptide strongly reinforces the identification.
- The UniProt annotation for EC 3.5.2.6 carries both RuleBase (computational, ECO:0000255) and experimental (ECO:0000269) evidence; the experimental support from crystallography and functional assays is robust.
- The reviewer evidence is from the current (2026) UniProt snapshot; the author's source snapshot is unknown, but the sequence has been unchanged since 2004 (sequence version 1), so the annotation is stable.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the S-x-x-K active-site motif (S70-T-F-K73, visible as 'PASTFKIP' in the sequence) and the KTG motif (K208-T209-G210, visible as 'AKTGY'), both hallmarks of class D serine beta-lactamases (oxacillinases). Additionally, the N-terminal hydrophobic stretch (MRVLALSAVFLVASIIGMPAVA) is a classic bacterial signal peptide consistent with periplasmic localization of beta-lactamases. These motifs are general, textbook-level features of class D beta-lactamases and are incompatible with the other choices: (A) an NADPH-dependent reductase would require a Rossmann-fold GxGxxG motif absent here; (B) a glycosidase would show different catalytic residue arrangements; (C) an NAD+-dependent dehydrogenase would also require a Rossmann fold. Recognizing S-x-x-K and KTG as class D beta-lactamase signatures and linking them to beta-lactam hydrolysis is standard enzymological knowledge.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The model does not need to know this is specifically OXA-48; identifying the class D beta-lactamase fold from S-x-x-K and KTG motifs suffices to select D over the other three mechanistically distinct options.",
    "reason": "The S-x-x-K and KTG motifs are well-established, general structural signatures of class D beta-lactamases taught in standard biochemistry and microbiology. Their presence in the sequence, combined with the signal peptide and absence of Rossmann-fold or glycosidase motifs, provides a concrete biological argument distinguishing D from A, B, and C without requiring memorization of this particular protein's database entry."
  },
  "case_id": "catalytic_activity_0193",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "H2",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q6XEC0 (Beta-lactamase OXA-48, EC 3.5.2.6) exactly (265 aa, sequence SHA256 identical). The catalytic activity 'a beta-lactam + H2O = a substituted beta-amino acid' is annotated with multiple experimental evidence codes (ECO:0000269) from four independent publications (PubMed:14693513, 19477418, 27073009, 38161376) including X-ray crystallography (PDB: 3HBR, 5HAP, 5HAQ, 7O5N, 7O9N) and functional assays. The Rhea cross-reference RHEA:20401 confirms the reaction. The expected answer D is directly and experimentally supported."
  },
  "important_caveats": [
    "The S-x-x-K motif identification requires the model to correctly locate the motif within the 265-residue sequence and recognize it as a class D beta-lactamase signature rather than a coincidental S-x-x-K pattern; however, the co-occurrence with KTG and the signal peptide strongly reinforces the identification.",
    "The UniProt annotation for EC 3.5.2.6 carries both RuleBase (computational, ECO:0000255) and experimental (ECO:0000269) evidence; the experimental support from crystallography and functional assays is robust.",
    "The reviewer evidence is from the current (2026) UniProt snapshot; the author's source snapshot is unknown, but the sequence has been unchanged since 2004 (sequence version 1), so the annotation is stable."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The S-x-x-K and KTG motifs are highly specific to class D beta-lactamases. The other three choices involve fundamentally different enzyme classes (NADPH reductase, glycosidase, NAD+ dehydrogenase) with incompatible structural requirements. No alternative choice is defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0193",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q6XEC0 (Beta-lactamase OXA-48, EC 3.5.2.6) exactly (265 aa, sequence SHA256 identical). The catalytic activity 'a beta-lactam + H2O = a substituted beta-amino acid' is annotated with multiple experimental evidence codes (ECO:0000269) from four independent publications (PubMed:14693513, 19477418, 27073009, 38161376) including X-ray crystallography (PDB: 3HBR, 5HAP, 5HAQ, 7O5N, 7O9N) and functional assays. The Rhea cross-reference RHEA:20401 confirms the reaction. The expected answer D is directly and experimentally supported.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C8", "C9", "H2", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the S-x-x-K active-site motif (S70-T-F-K73, visible as 'PASTFKIP' in the sequence) and the KTG motif (K208-T209-G210, visible as 'AKTGY'), both hallmarks of class D serine beta-lactamases (oxacillinases). Additionally, the N-terminal hydrophobic stretch (MRVLALSAVFLVASIIGMPAVA) is a classic bacterial signal peptide consistent with periplasmic localization of beta-lactamases. These motifs are general, textbook-level features of class D beta-lactamases and are incompatible with the other choices: (A) an NADPH-dependent reductase would require a Rossmann-fold GxGxxG motif absent here; (B) a glycosidase would show different catalytic residue arrangements; (C) an NAD+-dependent dehydrogenase would also require a Rossmann fold. Recognizing S-x-x-K and KTG as class D beta-lactamase signatures and linking them to beta-lactam hydrolysis is standard enzymological knowledge.",
    "missing_item_specific_fact": "None critical. The model does not need to know this is specifically OXA-48; identifying the class D beta-lactamase fold from S-x-x-K and KTG motifs suffices to select D over the other three mechanistically distinct options.",
    "reason": "The S-x-x-K and KTG motifs are well-established, general structural signatures of class D beta-lactamases taught in standard biochemistry and microbiology. Their presence in the sequence, combined with the signal peptide and absence of Rossmann-fold or glycosidase motifs, provides a concrete biological argument distinguishing D from A, B, and C without requiring memorization of this particular protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The S-x-x-K and KTG motifs are highly specific to class D beta-lactamases. The other three choices involve fundamentally different enzyme classes (NADPH reductase, glycosidase, NAD+ dehydrogenase) with incompatible structural requirements. No alternative choice is defensible given the sequence features."
  },
  "important_caveats": [
    "The S-x-x-K motif identification requires the model to correctly locate the motif within the 265-residue sequence and recognize it as a class D beta-lactamase signature rather than a coincidental S-x-x-K pattern; however, the co-occurrence with KTG and the signal peptide strongly reinforces the identification.",
    "The UniProt annotation for EC 3.5.2.6 carries both RuleBase (computational, ECO:0000255) and experimental (ECO:0000269) evidence; the experimental support from crystallography and functional assays is robust.",
    "The reviewer evidence is from the current (2026) UniProt snapshot; the author's source snapshot is unknown, but the sequence has been unchanged since 2004 (sequence version 1), so the annotation is stable."
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

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6XEC0.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:45.821901+00:00.  

```json
"Q6XEC0"
```

Source SHA-256: `7a7b0d77f1f923e008e8fc5048255b02d3f9e2d1a0d4b680f7c01328fb477d33`.

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
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:45.821901+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.5.2.6","evidences":[{"evidenceCode":"ECO:0000269","id":"14693513","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"19477418","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"27073009","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38161376","source":"PubMed"}],"name":"a beta-lactam + H2O = a substituted beta-amino acid","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:20401"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:35627"},{"database":"ChEBI","id":"CHEBI:140347"}]}}
```

Source SHA-256: `7a7b0d77f1f923e008e8fc5048255b02d3f9e2d1a0d4b680f7c01328fb477d33`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6XEC0.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:45.821901+00:00.  

```json
{"citation":{"authors":["Poirel L.","Heritier C.","Tolun V.","Nordmann P."],"citationCrossReferences":[{"database":"PubMed","id":"14693513"},{"database":"DOI","id":"10.1128/aac.48.1.15-22.2004"}],"citationType":"journal article","firstPage":"15","id":"14693513","journal":"Antimicrob. Agents Chemother.","lastPage":"22","publicationDate":"2004","title":"Emergence of oxacillinase-mediated resistance to imipenem in Klebsiella pneumoniae.","volume":"48"},"evidences":[{"evidenceCode":"ECO:0000312","id":"AAP70012.1","source":"EMBL"}],"referenceComments":[{"evidences":[{"evidenceCode":"ECO:0000312","id":"AAP70012.1","source":"EMBL"}],"type":"STRAIN","value":"11978"}],"referenceNumber":4,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","ACTIVITY REGULATION","INDUCTION"]}
```

Source SHA-256: `7a7b0d77f1f923e008e8fc5048255b02d3f9e2d1a0d4b680f7c01328fb477d33`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6XEC0.json)  
**Locator:** `/references/11`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:45.821901+00:00.  

```json
{"citation":{"authors":["Docquier J.D.","Calderone V.","De Luca F.","Benvenuti M.","Giuliani F.","Bellucci L.","Tafi A.","Nordmann P.","Botta M.","Rossolini G.M.","Mangani S."],"citationCrossReferences":[{"database":"PubMed","id":"19477418"},{"database":"DOI","id":"10.1016/j.chembiol.2009.04.010"}],"citationType":"journal article","firstPage":"540","id":"19477418","journal":"Chem. Biol.","lastPage":"547","publicationDate":"2009","title":"Crystal structure of the OXA-48 beta-lactamase reveals mechanistic diversity among class D carbapenemases.","volume":"16"},"evidences":[{"evidenceCode":"ECO:0007744","id":"3HBR","source":"PDB"}],"referenceNumber":12,"referencePositions":["X-RAY CRYSTALLOGRAPHY (1.90 ANGSTROMS)","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","CARBOXYLATION AT LYS-73"]}
```

Source SHA-256: `7a7b0d77f1f923e008e8fc5048255b02d3f9e2d1a0d4b680f7c01328fb477d33`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6XEC0.json)  
**Locator:** `/references/14`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:45.821901+00:00.  

```json
{"citation":{"authors":["Stojanoski V.","Adamski C.J.","Hu L.","Mehta S.C.","Sankaran B.","Zwart P.","Prasad B.V.","Palzkill T."],"citationCrossReferences":[{"database":"PubMed","id":"27073009"},{"database":"DOI","id":"10.1021/acs.biochem.6b00056"}],"citationType":"journal article","firstPage":"2479","id":"27073009","journal":"Biochemistry","lastPage":"2490","publicationDate":"2016","title":"Removal of the Side Chain at the Active-Site Serine by a Glycine Substitution Increases the Stability of a Wide Range of Serine beta-Lactamases by Relieving Steric Strain.","volume":"55"},"evidences":[{"evidenceCode":"ECO:0007744","id":"5HAP","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"5HAQ","source":"PDB"}],"referenceNumber":15,"referencePositions":["X-RAY CRYSTALLOGRAPHY (1.89 ANGSTROMS) OF 25-265 OF MUTANTS ALA-70 AND GLY-70","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","MUTAGENESIS OF SER-70"]}
```

Source SHA-256: `7a7b0d77f1f923e008e8fc5048255b02d3f9e2d1a0d4b680f7c01328fb477d33`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6XEC0.json)  
**Locator:** `/references/19`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:45.821901+00:00.  

```json
{"citation":{"authors":["Zhou Q.","Catalan P.","Bell H.","Baumann P.","Cooke R.","Evans R.","Yang J.","Zhang Z.","Zappala D.","Zhang Y.","Blackburn G.M.","He Y.","Jin Y."],"citationCrossReferences":[{"database":"PubMed","id":"38161376"},{"database":"DOI","id":"10.1021/acscentsci.3c00609"}],"citationType":"journal article","firstPage":"2339","id":"38161376","journal":"ACS Cent. Sci.","lastPage":"2349","publicationDate":"2023","title":"An Ion-Pair Induced Intermediate Complex Captured in Class D Carbapenemase Reveals Chloride Ion as a Janus Effector Modulating Activity.","volume":"9"},"evidences":[{"evidenceCode":"ECO:0007744","id":"7O5N","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7O9N","source":"PDB"}],"referenceNumber":20,"referencePositions":["X-RAY CRYSTALLOGRAPHY (1.53 ANGSTROMS) OF 23-265 IN APO FORM AND IN COMPLEXES WITH IMIPENEM INHIBITOR AND CHLORIDE; BROMIDE; IODIDE; BICARBONATE AND OF MUTANTS ALA-185/ALA-186/ALA-206 AND ALA-250 IN COMPLEXES WITH CHLORIDE AND BROMIDE","FUNCTION","CATALYTIC ACTIVITY","ACTIVITY REGULATION"]}
```

Source SHA-256: `7a7b0d77f1f923e008e8fc5048255b02d3f9e2d1a0d4b680f7c01328fb477d33`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6XEC0?format=txt&versions=136)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 136 / 1.  
**Retrieved:** 2026-11-02T04:31:51.921802+00:00.  

```text
DE   RecName: Full=Beta-lactamase OXA-48 {ECO:0000255|RuleBase:RU361140, ECO:0000303|PubMed:14693513};
DE            EC=3.5.2.6 {ECO:0000255|RuleBase:RU361140, ECO:0000269|PubMed:14693513, ECO:0000269|PubMed:19477418, ECO:0000269|PubMed:27073009, ECO:0000269|PubMed:38161376};
DE   Flags: Precursor;
```

Source SHA-256: `748d62da6dbda55945d3952c2004e283e2a5bc809be9fd394e2b1d0eff688b3a`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6XEC0?format=txt&versions=136)  
**Locator:** `lines 221-226`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 136 / 1.  
**Retrieved:** 2026-11-02T04:31:51.921802+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=a beta-lactam + H2O = a substituted beta-amino acid;
CC         Xref=Rhea:RHEA:20401, ChEBI:CHEBI:15377, ChEBI:CHEBI:35627,
CC         ChEBI:CHEBI:140347; EC=3.5.2.6;
CC         Evidence={ECO:0000269|PubMed:14693513, ECO:0000269|PubMed:19477418,
CC         ECO:0000269|PubMed:27073009, ECO:0000269|PubMed:38161376};
```

Source SHA-256: `748d62da6dbda55945d3952c2004e283e2a5bc809be9fd394e2b1d0eff688b3a`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 193. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
