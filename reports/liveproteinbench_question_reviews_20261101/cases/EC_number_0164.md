# EC_number_0164

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **A** — 5.1.3.45

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MMSRYEELRKELPAQPKVWLITGVAGFIGSNLLETLLKLDQKVVGLDNFATGHQRNLDEVRSLVSEKQWSNFKFIQGDIRNLDDCNNACAGVDYVLHQAALGSVPRSINDPITSNATNIDGFLNMLIAARDAKVQSFTYAASSSTYGDHPGLPKVEDTIGKPLSPYAVTKYVNELYADVFSRCYGFSTIGLRYFNVFGRRQDPNGAYAAVIPKWTSSMIQGDDVYINGDGETSRDFCYIENTVQANLLAATAGLDARNQVYNIAVGGRTSLNQLFFALRDGLAENGVSYHREPVYRDFREGDVRHSLADISKAAKLLGYAPKYDVSAGVALAMPWYIMFLK

[Multiple Choices]
A. 5.1.3.45
B. 5.1.3.14
C. 5.1.1.25
D. 2.1.2.1
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

> The supplied sequence exactly matches the UniProt entry, which assigns EC 5.1.3.45 and cites experimental evidence for the corresponding UDP-sugar epimerization reaction. The record also carries an experimentally supported EC 5.1.3.7 activity, but that option is not listed.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may suggest an enzyme with epimerase-like features, but general sequence reasoning does not establish the precise substrate specificity needed to select EC 5.1.3.45 over other detailed EC assignments.


**Missing item-specific fact**

> The enzyme's experimentally characterized substrate and reaction, or an equivalent protein-specific functional annotation, is absent from the question.


**Reason**

> Selecting the exact four-part EC number depends on protein-specific catalytic specificity not supplied in the sequence prompt; recognizing the sequence or recalling its database annotation would be lookup or memorization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, only A is supported by the matched entry's experimentally evidenced EC annotation. The entry also has EC 5.1.3.7, but it is not among the choices.


### Important caveats

- The matched UniProt record reports both EC 5.1.3.45 and EC 5.1.3.7 for distinct reactions; A is supported but is not the enzyme's only annotated activity.
- Reviewer-only database evidence supports the key but was not available to the evaluated model, and the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may suggest an enzyme with epimerase-like features, but general sequence reasoning does not establish the precise substrate specificity needed to select EC 5.1.3.45 over other detailed EC assignments.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The enzyme's experimentally characterized substrate and reaction, or an equivalent protein-specific functional annotation, is absent from the question.",
    "reason": "Selecting the exact four-part EC number depends on protein-specific catalytic specificity not supplied in the sequence prompt; recognizing the sequence or recalling its database annotation would be lookup or memorization."
  },
  "case_id": "EC_number_0164",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry, which assigns EC 5.1.3.45 and cites experimental evidence for the corresponding UDP-sugar epimerization reaction. The record also carries an experimentally supported EC 5.1.3.7 activity, but that option is not listed."
  },
  "important_caveats": [
    "The matched UniProt record reports both EC 5.1.3.45 and EC 5.1.3.7 for distinct reactions; A is supported but is not the enzyme's only annotated activity.",
    "Reviewer-only database evidence supports the key but was not available to the evaluated model, and the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, only A is supported by the matched entry's experimentally evidenced EC annotation. The entry also has EC 5.1.3.7, but it is not among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0164",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry, which assigns EC 5.1.3.45 and cites experimental evidence for the corresponding UDP-sugar epimerization reaction. The record also carries an experimentally supported EC 5.1.3.7 activity, but that option is not listed.",
    "evidence_ids": ["C1", "C4", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may suggest an enzyme with epimerase-like features, but general sequence reasoning does not establish the precise substrate specificity needed to select EC 5.1.3.45 over other detailed EC assignments.",
    "missing_item_specific_fact": "The enzyme's experimentally characterized substrate and reaction, or an equivalent protein-specific functional annotation, is absent from the question.",
    "reason": "Selecting the exact four-part EC number depends on protein-specific catalytic specificity not supplied in the sequence prompt; recognizing the sequence or recalling its database annotation would be lookup or memorization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, only A is supported by the matched entry's experimentally evidenced EC annotation. The entry also has EC 5.1.3.7, but it is not among the choices."
  },
  "important_caveats": [
    "The matched UniProt record reports both EC 5.1.3.45 and EC 5.1.3.7 for distinct reactions; A is supported but is not the enzyme's only annotated activity.",
    "Reviewer-only database evidence supports the key but was not available to the evaluated model, and the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q8KN66 (WbpP, Pseudomonas aeruginosa, sequence matched exactly) lists EC 5.1.3.45 as the recommended EC number for 'UDP-N-acetyl-alpha-D-glucosaminouronate 4-epimerase,' supported by experimental evidence (ECO:0000269, PubMed:18065759). The catalytic reaction UDP-2-acetamido-2-deoxy-alpha-D-glucuronate = UDP-2-acetamido-2-deoxy-alpha-D-galacturonate is confirmed. The protein also carries EC 5.1.3.7 as an alternative name, but that number is not among the choices, so it does not contradict the key.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C9](#evidence-c9), [H1](#evidence-h1), [H2](#evidence-h2), [H9](#evidence-h9).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The NAD-binding Rossmann-fold motif (GVAGFIGSN) is present, which is consistent with NAD-dependent UDP-sugar 4-epimerases (EC 5.1.3.x) and helps rule out 2.1.2.1 (PLP-dependent glycine hydroxymethyltransferase) and 5.1.1.25 (radical-SAM lysine 2,3-aminomutase). However, distinguishing 5.1.3.45 (UDP-GlcNAcA 4-epimerase) from 5.1.3.14 (a different UDP-sugar epimerase subtype) requires knowing this specific enzyme's substrate preference for the uronate (GlcNAcA) rather than the amino-sugar (GlcNAc), which is a protein-specific experimental fact not encoded in generalizable sequence motifs.


**Missing item-specific fact**

> The specific substrate selectivity of WbpP for UDP-GlcNAcA (EC 5.1.3.45) versus other UDP-hexose/hexuronic acid substrates (e.g., UDP-GlcNAc for EC 5.1.3.7, or the substrate of EC 5.1.3.14), established only by experimental characterization (PubMed:18065759).


**Reason**

> While the NAD-binding motif narrows the EC class to 5.1.3.x, the final 4th digit (45 vs 14) depends on the experimentally determined substrate specificity of this particular enzyme, which is not derivable from sequence motifs shared across the UDP-sugar epimerase superfamily.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The protein carries both EC 5.1.3.45 and EC 5.1.3.7, but 5.1.3.7 is not among the choices. Among the four options, only A (5.1.3.45) matches the recommended annotation. B (5.1.3.14), C (5.1.1.25), and D (2.1.2.1) correspond to mechanistically and functionally distinct enzymes, so no ambiguity exists within the provided option set.


### Important caveats

- The UniProt entry lists EC 5.1.3.7 as an alternative activity (UDP-GlcNAc C4 epimerase) with experimental support from three independent publications. If 5.1.3.7 had been an option, the question would be ambiguous.
- The recommended EC 5.1.3.45 was assigned in 2008 (PubMed:18065759), later than the original 5.1.3.7 characterization. The author source snapshot date is unknown; if constructed before 2008, the annotation history could differ.
- Sequence identity is confirmed (SHA-256 match to Q8KN66, 341 aa), so the annotation applies to the exact protein in the question.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The NAD-binding Rossmann-fold motif (GVAGFIGSN) is present, which is consistent with NAD-dependent UDP-sugar 4-epimerases (EC 5.1.3.x) and helps rule out 2.1.2.1 (PLP-dependent glycine hydroxymethyltransferase) and 5.1.1.25 (radical-SAM lysine 2,3-aminomutase). However, distinguishing 5.1.3.45 (UDP-GlcNAcA 4-epimerase) from 5.1.3.14 (a different UDP-sugar epimerase subtype) requires knowing this specific enzyme's substrate preference for the uronate (GlcNAcA) rather than the amino-sugar (GlcNAc), which is a protein-specific experimental fact not encoded in generalizable sequence motifs.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate selectivity of WbpP for UDP-GlcNAcA (EC 5.1.3.45) versus other UDP-hexose/hexuronic acid substrates (e.g., UDP-GlcNAc for EC 5.1.3.7, or the substrate of EC 5.1.3.14), established only by experimental characterization (PubMed:18065759).",
    "reason": "While the NAD-binding motif narrows the EC class to 5.1.3.x, the final 4th digit (45 vs 14) depends on the experimentally determined substrate specificity of this particular enzyme, which is not derivable from sequence motifs shared across the UDP-sugar epimerase superfamily."
  },
  "case_id": "EC_number_0164",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C9",
      "H1",
      "H2",
      "H9"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q8KN66 (WbpP, Pseudomonas aeruginosa, sequence matched exactly) lists EC 5.1.3.45 as the recommended EC number for 'UDP-N-acetyl-alpha-D-glucosaminouronate 4-epimerase,' supported by experimental evidence (ECO:0000269, PubMed:18065759). The catalytic reaction UDP-2-acetamido-2-deoxy-alpha-D-glucuronate = UDP-2-acetamido-2-deoxy-alpha-D-galacturonate is confirmed. The protein also carries EC 5.1.3.7 as an alternative name, but that number is not among the choices, so it does not contradict the key."
  },
  "important_caveats": [
    "The UniProt entry lists EC 5.1.3.7 as an alternative activity (UDP-GlcNAc C4 epimerase) with experimental support from three independent publications. If 5.1.3.7 had been an option, the question would be ambiguous.",
    "The recommended EC 5.1.3.45 was assigned in 2008 (PubMed:18065759), later than the original 5.1.3.7 characterization. The author source snapshot date is unknown; if constructed before 2008, the annotation history could differ.",
    "Sequence identity is confirmed (SHA-256 match to Q8KN66, 341 aa), so the annotation applies to the exact protein in the question."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein carries both EC 5.1.3.45 and EC 5.1.3.7, but 5.1.3.7 is not among the choices. Among the four options, only A (5.1.3.45) matches the recommended annotation. B (5.1.3.14), C (5.1.1.25), and D (2.1.2.1) correspond to mechanistically and functionally distinct enzymes, so no ambiguity exists within the provided option set."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0164",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q8KN66 (WbpP, Pseudomonas aeruginosa, sequence matched exactly) lists EC 5.1.3.45 as the recommended EC number for 'UDP-N-acetyl-alpha-D-glucosaminouronate 4-epimerase,' supported by experimental evidence (ECO:0000269, PubMed:18065759). The catalytic reaction UDP-2-acetamido-2-deoxy-alpha-D-glucuronate = UDP-2-acetamido-2-deoxy-alpha-D-galacturonate is confirmed. The protein also carries EC 5.1.3.7 as an alternative name, but that number is not among the choices, so it does not contradict the key.",
    "evidence_ids": ["C4", "C5", "C9", "H1", "H2", "H9"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The NAD-binding Rossmann-fold motif (GVAGFIGSN) is present, which is consistent with NAD-dependent UDP-sugar 4-epimerases (EC 5.1.3.x) and helps rule out 2.1.2.1 (PLP-dependent glycine hydroxymethyltransferase) and 5.1.1.25 (radical-SAM lysine 2,3-aminomutase). However, distinguishing 5.1.3.45 (UDP-GlcNAcA 4-epimerase) from 5.1.3.14 (a different UDP-sugar epimerase subtype) requires knowing this specific enzyme's substrate preference for the uronate (GlcNAcA) rather than the amino-sugar (GlcNAc), which is a protein-specific experimental fact not encoded in generalizable sequence motifs.",
    "missing_item_specific_fact": "The specific substrate selectivity of WbpP for UDP-GlcNAcA (EC 5.1.3.45) versus other UDP-hexose/hexuronic acid substrates (e.g., UDP-GlcNAc for EC 5.1.3.7, or the substrate of EC 5.1.3.14), established only by experimental characterization (PubMed:18065759).",
    "reason": "While the NAD-binding motif narrows the EC class to 5.1.3.x, the final 4th digit (45 vs 14) depends on the experimentally determined substrate specificity of this particular enzyme, which is not derivable from sequence motifs shared across the UDP-sugar epimerase superfamily."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein carries both EC 5.1.3.45 and EC 5.1.3.7, but 5.1.3.7 is not among the choices. Among the four options, only A (5.1.3.45) matches the recommended annotation. B (5.1.3.14), C (5.1.1.25), and D (2.1.2.1) correspond to mechanistically and functionally distinct enzymes, so no ambiguity exists within the provided option set."
  },
  "important_caveats": [
    "The UniProt entry lists EC 5.1.3.7 as an alternative activity (UDP-GlcNAc C4 epimerase) with experimental support from three independent publications. If 5.1.3.7 had been an option, the question would be ambiguous.",
    "The recommended EC 5.1.3.45 was assigned in 2008 (PubMed:18065759), later than the original 5.1.3.7 characterization. The author source snapshot date is unknown; if constructed before 2008, the annotation history could differ.",
    "Sequence identity is confirmed (SHA-256 match to Q8KN66, 341 aa), so the annotation applies to the exact protein in the question."
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

**Accession:** `Q8KN66` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 87. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8KN66.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:25.367428+00:00.  

```json
"Q8KN66"
```

Source SHA-256: `f67b2500389a81025c9be1998ba5bdf0c0e6d0d7f2971007bc6e11f741355b05`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8KN66.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:25.367428+00:00.  

```json
{"alternativeNames":[{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"10747995","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"15016816","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"15752069","source":"PubMed"}],"value":"5.1.3.7"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"15752069","source":"PubMed"}],"value":"UDP-N-acetylglucosamine C4 epimerase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"10747995","source":"PubMed"}],"value":"UDP-GlcNAc C4 epimerase"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"18065759","source":"PubMed"}],"value":"5.1.3.45"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"UDP-N-acetyl-alpha-D-glucosaminouronate 4-epimerase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"UDP-GlcNAcA 4-epimerase"}]}}
```

Source SHA-256: `f67b2500389a81025c9be1998ba5bdf0c0e6d0d7f2971007bc6e11f741355b05`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8KN66.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:25.367428+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"18065759","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:81512"}}],"reaction":{"ecNumber":"5.1.3.45","evidences":[{"evidenceCode":"ECO:0000269","id":"18065759","source":"PubMed"}],"name":"UDP-2-acetamido-2-deoxy-alpha-D-glucuronate = UDP-2-acetamido-2-deoxy-alpha-D-galacturonate","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:81511"},{"database":"ChEBI","id":"CHEBI:65040"},{"database":"ChEBI","id":"CHEBI:231899"}]}}
```

Source SHA-256: `f67b2500389a81025c9be1998ba5bdf0c0e6d0d7f2971007bc6e11f741355b05`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8KN66.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:25.367428+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"5.1.3.7","evidences":[{"evidenceCode":"ECO:0000269","id":"10747995","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"15016816","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"15752069","source":"PubMed"}],"name":"UDP-N-acetyl-alpha-D-glucosamine = UDP-N-acetyl-alpha-D-galactosamine","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:20517"},{"database":"ChEBI","id":"CHEBI:57705"},{"database":"ChEBI","id":"CHEBI:67138"}]}}
```

Source SHA-256: `f67b2500389a81025c9be1998ba5bdf0c0e6d0d7f2971007bc6e11f741355b05`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8KN66.json)  
**Locator:** `/references/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:25.367428+00:00.  

```json
{"citation":{"authors":["Miller W.L.","Matewish M.J.","McNally D.J.","Ishiyama N.","Anderson E.M.","Brewer D.","Brisson J.R.","Berghuis A.M.","Lam J.S."],"citationCrossReferences":[{"database":"PubMed","id":"18065759"},{"database":"DOI","id":"10.1074/jbc.m708894200"}],"citationType":"journal article","firstPage":"3507","id":"18065759","journal":"J. Biol. Chem.","lastPage":"3518","publicationDate":"2008","title":"Flagellin glycosylation in Pseudomonas aeruginosa PAK requires the O-antigen biosynthesis enzyme WbpO.","volume":"283"},"referenceComments":[{"type":"STRAIN","value":"PAK / Serotype O6"}],"referenceNumber":5,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `f67b2500389a81025c9be1998ba5bdf0c0e6d0d7f2971007bc6e11f741355b05`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 87 / 1.  
**Retrieved:** 2026-11-01T06:28:41.451179+00:00.  

```text
ID   WBPP_PSEAI              Reviewed;         341 AA.
AC   Q8KN66; Q9RHD6;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-OCT-2002, sequence version 1.
DT   28-JAN-2026, entry version 87.
DE   RecName: Full=UDP-N-acetyl-alpha-D-glucosaminouronate 4-epimerase {ECO:0000305};
DE            Short=UDP-GlcNAcA 4-epimerase {ECO:0000305};
DE            EC=5.1.3.45 {ECO:0000269|PubMed:18065759};
DE   AltName: Full=UDP-N-acetylglucosamine C4 epimerase {ECO:0000303|PubMed:15752069};
DE            Short=UDP-GlcNAc C4 epimerase {ECO:0000303|PubMed:10747995};
DE            EC=5.1.3.7 {ECO:0000269|PubMed:10747995, ECO:0000269|PubMed:15016816, ECO:0000269|PubMed:15752069};
GN   Name=wbpP {ECO:0000303|PubMed:10627048, ECO:0000303|PubMed:12057956};
OS   Pseudomonas aeruginosa.
OC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;
OC   Pseudomonadales; Pseudomonadaceae; Pseudomonas.
OX   NCBI_TaxID=287;
```

Source SHA-256: `d549ed0cf621d2667a5b18f1c61cab90f3244af9d4301b29345d83da21267e72`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87)  
**Locator:** `lines 6-11`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 87 / 1.  
**Retrieved:** 2026-11-01T06:28:41.451179+00:00.  

```text
DE   RecName: Full=UDP-N-acetyl-alpha-D-glucosaminouronate 4-epimerase {ECO:0000305};
DE            Short=UDP-GlcNAcA 4-epimerase {ECO:0000305};
DE            EC=5.1.3.45 {ECO:0000269|PubMed:18065759};
DE   AltName: Full=UDP-N-acetylglucosamine C4 epimerase {ECO:0000303|PubMed:15752069};
DE            Short=UDP-GlcNAc C4 epimerase {ECO:0000303|PubMed:10747995};
DE            EC=5.1.3.7 {ECO:0000269|PubMed:10747995, ECO:0000269|PubMed:15016816, ECO:0000269|PubMed:15752069};
```

Source SHA-256: `d549ed0cf621d2667a5b18f1c61cab90f3244af9d4301b29345d83da21267e72`.

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87)  
**Locator:** `lines 85-91`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 87 / 1.  
**Retrieved:** 2026-11-01T06:28:41.451179+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=UDP-2-acetamido-2-deoxy-alpha-D-glucuronate = UDP-2-acetamido-
CC         2-deoxy-alpha-D-galacturonate; Xref=Rhea:RHEA:81511,
CC         ChEBI:CHEBI:65040, ChEBI:CHEBI:231899; EC=5.1.3.45;
CC         Evidence={ECO:0000269|PubMed:18065759};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81512;
CC         Evidence={ECO:0000269|PubMed:18065759};
```

Source SHA-256: `d549ed0cf621d2667a5b18f1c61cab90f3244af9d4301b29345d83da21267e72`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 164. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
