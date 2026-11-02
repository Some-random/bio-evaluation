# EC_number_0196

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **D** — 3.5.2.6

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKLLKILSLVCLSISIGACAEHSMSRAKTSTIPQVNNSIIDQNVQALFNEISADAVFVTYDGQNIKKYGTHLDRAKTAYIPASTFKIANALIGLENHKATSTEIFKWDGKPRFFKAWDKDFTLGEAMQASTVPVYQELARRIGPSLMQSELQRIGYGNMQIGTEVDQFWLKGPLTITPIQEVKFVYDLAQGQLPFKPEVQQQVKEMLYVERRGENRLYAKSGWGMAVDPQVGWYVGFVEKADGQVVAFALNMQMKAGDDIALRKQLSLDVLDKLGVFHYL

[Multiple Choices]
A. 3.6.1.5
B. 5.1.3.45
C. 4.1.1.36
D. 3.5.2.6
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

> The exact supplied sequence matches the UniProt OXA-58 entry. Its EC 3.5.2.6 annotation is supported by cited experimental evidence, and the entry specifies beta-lactam hydrolysis as the catalytic reaction.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may suggest a bacterial exported enzyme, but that does not establish its specific substrate reaction or distinguish EC 3.5.2.6 from the other listed EC numbers.


**Missing item-specific fact**

> The protein's identity and catalytic activity as OXA-58 beta-lactamase, or equivalent protein-specific functional evidence, are not supplied in the question.


**Reason**

> Choosing the correct EC requires protein-specific functional knowledge not established by the sequence context and choices alone; identifying the exact sequence from memory would be lookup or memorization, not reasoning from the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence assigns the matched protein to EC 3.5.2.6; no evidence supports another listed option.


### Important caveats

- The supporting UniProt evidence is reviewer-only and was not available to the evaluated model.
- The EC annotation includes both a computational RuleBase attribution and citations with experimental evidence codes; the annotation alone should not be treated as wholly experimental.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may suggest a bacterial exported enzyme, but that does not establish its specific substrate reaction or distinguish EC 3.5.2.6 from the other listed EC numbers.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's identity and catalytic activity as OXA-58 beta-lactamase, or equivalent protein-specific functional evidence, are not supplied in the question.",
    "reason": "Choosing the correct EC requires protein-specific functional knowledge not established by the sequence context and choices alone; identifying the exact sequence from memory would be lookup or memorization, not reasoning from the input."
  },
  "case_id": "EC_number_0196",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt OXA-58 entry. Its EC 3.5.2.6 annotation is supported by cited experimental evidence, and the entry specifies beta-lactam hydrolysis as the catalytic reaction."
  },
  "important_caveats": [
    "The supporting UniProt evidence is reviewer-only and was not available to the evaluated model.",
    "The EC annotation includes both a computational RuleBase attribution and citations with experimental evidence codes; the annotation alone should not be treated as wholly experimental."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence assigns the matched protein to EC 3.5.2.6; no evidence supports another listed option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0196",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt OXA-58 entry. Its EC 3.5.2.6 annotation is supported by cited experimental evidence, and the entry specifies beta-lactam hydrolysis as the catalytic reaction.",
    "evidence_ids": ["C1", "C4", "C5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may suggest a bacterial exported enzyme, but that does not establish its specific substrate reaction or distinguish EC 3.5.2.6 from the other listed EC numbers.",
    "missing_item_specific_fact": "The protein's identity and catalytic activity as OXA-58 beta-lactamase, or equivalent protein-specific functional evidence, are not supplied in the question.",
    "reason": "Choosing the correct EC requires protein-specific functional knowledge not established by the sequence context and choices alone; identifying the exact sequence from memory would be lookup or memorization, not reasoning from the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence assigns the matched protein to EC 3.5.2.6; no evidence supports another listed option."
  },
  "important_caveats": [
    "The supporting UniProt evidence is reviewer-only and was not available to the evaluated model.",
    "The EC annotation includes both a computational RuleBase attribution and citations with experimental evidence codes; the annotation alone should not be treated as wholly experimental."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence exactly matches UniProt Q2TR58 (Beta-lactamase OXA-58, Acinetobacter baumannii, 280 aa). The EC 3.5.2.6 annotation is backed by multiple experimental evidence codes (ECO:0000269 from PubMed:15616297, PubMed:26459904, PubMed:26701320), X-ray crystallography structures (5BOH, 4Y0O, 4Y0T, 4Y0U), mutagenesis studies, and catalytic activity assays. The catalytic reaction (a beta-lactam + H2O = a substituted beta-amino acid) is well-characterized experimentally.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the S-x-x-K catalytic motif (STFK at ~positions 83-86), which is the hallmark active-site signature of serine beta-lactamases. This motif is a well-established general biological fact about the beta-lactamase fold. The overall ~280-residue length with an N-terminal signal peptide is consistent with a secreted/periplasmic beta-lactamase. The C-terminal region contains 'KSGWG', consistent with the KSG motif of class D (OXA-type) beta-lactamases. None of the other EC classes (phosphodiesterase 3.6.1.5, epimerase 5.1.3.45, decarboxylase 4.1.1.36) employ an S-x-x-K serine nucleophile mechanism, so the motif discriminates D from A, B, and C using general enzyme-mechanism knowledge.


**Missing item-specific fact**

> None critical. The S-x-x-K motif identification and its association with beta-lactamase activity (EC 3.5.2.6) are general biochemical knowledge, not item-specific database lookups.


**Reason**

> A model with knowledge of enzyme active-site motifs can identify STFK as the S-x-x-K serine nucleophile motif, recognize the overall architecture as consistent with beta-lactamases, and eliminate the other three EC classes (phosphodiesterase, epimerase, decarboxylase) because they do not use serine nucleophilic catalysis. This constitutes general biological reasoning rather than memorization of a specific database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The S-x-x-K motif unambiguously points to a serine hydrolase acting on a beta-lactam ring (EC 3.5.2.6). The other three options represent mechanistically distinct enzyme classes (phosphodiesterase, epimerase, decarboxylase) that are incompatible with the identified active-site architecture. No ambiguity in distinguishing the correct answer.


### Important caveats

- The EC number annotation includes both RuleBase (computational) and experimental (PubMed) evidence codes; the experimental evidence (crystal structures, mutagenesis, catalytic assays) provides strong independent support.
- The sequence is a precursor (signal peptide present); the mature enzyme numbering differs from precursor numbering, but this does not affect the EC assignment.
- All reviewer evidence is from the current or archived UniProt snapshot; the author's exact source snapshot is unknown but sequence match is confirmed across versions.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the S-x-x-K catalytic motif (STFK at ~positions 83-86), which is the hallmark active-site signature of serine beta-lactamases. This motif is a well-established general biological fact about the beta-lactamase fold. The overall ~280-residue length with an N-terminal signal peptide is consistent with a secreted/periplasmic beta-lactamase. The C-terminal region contains 'KSGWG', consistent with the KSG motif of class D (OXA-type) beta-lactamases. None of the other EC classes (phosphodiesterase 3.6.1.5, epimerase 5.1.3.45, decarboxylase 4.1.1.36) employ an S-x-x-K serine nucleophile mechanism, so the motif discriminates D from A, B, and C using general enzyme-mechanism knowledge.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The S-x-x-K motif identification and its association with beta-lactamase activity (EC 3.5.2.6) are general biochemical knowledge, not item-specific database lookups.",
    "reason": "A model with knowledge of enzyme active-site motifs can identify STFK as the S-x-x-K serine nucleophile motif, recognize the overall architecture as consistent with beta-lactamases, and eliminate the other three EC classes (phosphodiesterase, epimerase, decarboxylase) because they do not use serine nucleophilic catalysis. This constitutes general biological reasoning rather than memorization of a specific database entry."
  },
  "case_id": "EC_number_0196",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "H2",
      "H3",
      "H4",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches UniProt Q2TR58 (Beta-lactamase OXA-58, Acinetobacter baumannii, 280 aa). The EC 3.5.2.6 annotation is backed by multiple experimental evidence codes (ECO:0000269 from PubMed:15616297, PubMed:26459904, PubMed:26701320), X-ray crystallography structures (5BOH, 4Y0O, 4Y0T, 4Y0U), mutagenesis studies, and catalytic activity assays. The catalytic reaction (a beta-lactam + H2O = a substituted beta-amino acid) is well-characterized experimentally."
  },
  "important_caveats": [
    "The EC number annotation includes both RuleBase (computational) and experimental (PubMed) evidence codes; the experimental evidence (crystal structures, mutagenesis, catalytic assays) provides strong independent support.",
    "The sequence is a precursor (signal peptide present); the mature enzyme numbering differs from precursor numbering, but this does not affect the EC assignment.",
    "All reviewer evidence is from the current or archived UniProt snapshot; the author's exact source snapshot is unknown but sequence match is confirmed across versions."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The S-x-x-K motif unambiguously points to a serine hydrolase acting on a beta-lactam ring (EC 3.5.2.6). The other three options represent mechanistically distinct enzyme classes (phosphodiesterase, epimerase, decarboxylase) that are incompatible with the identified active-site architecture. No ambiguity in distinguishing the correct answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0196",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches UniProt Q2TR58 (Beta-lactamase OXA-58, Acinetobacter baumannii, 280 aa). The EC 3.5.2.6 annotation is backed by multiple experimental evidence codes (ECO:0000269 from PubMed:15616297, PubMed:26459904, PubMed:26701320), X-ray crystallography structures (5BOH, 4Y0O, 4Y0T, 4Y0U), mutagenesis studies, and catalytic activity assays. The catalytic reaction (a beta-lactam + H2O = a substituted beta-amino acid) is well-characterized experimentally.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C8", "H2", "H3", "H4", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the S-x-x-K catalytic motif (STFK at ~positions 83-86), which is the hallmark active-site signature of serine beta-lactamases. This motif is a well-established general biological fact about the beta-lactamase fold. The overall ~280-residue length with an N-terminal signal peptide is consistent with a secreted/periplasmic beta-lactamase. The C-terminal region contains 'KSGWG', consistent with the KSG motif of class D (OXA-type) beta-lactamases. None of the other EC classes (phosphodiesterase 3.6.1.5, epimerase 5.1.3.45, decarboxylase 4.1.1.36) employ an S-x-x-K serine nucleophile mechanism, so the motif discriminates D from A, B, and C using general enzyme-mechanism knowledge.",
    "missing_item_specific_fact": "None critical. The S-x-x-K motif identification and its association with beta-lactamase activity (EC 3.5.2.6) are general biochemical knowledge, not item-specific database lookups.",
    "reason": "A model with knowledge of enzyme active-site motifs can identify STFK as the S-x-x-K serine nucleophile motif, recognize the overall architecture as consistent with beta-lactamases, and eliminate the other three EC classes (phosphodiesterase, epimerase, decarboxylase) because they do not use serine nucleophilic catalysis. This constitutes general biological reasoning rather than memorization of a specific database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The S-x-x-K motif unambiguously points to a serine hydrolase acting on a beta-lactam ring (EC 3.5.2.6). The other three options represent mechanistically distinct enzyme classes (phosphodiesterase, epimerase, decarboxylase) that are incompatible with the identified active-site architecture. No ambiguity in distinguishing the correct answer."
  },
  "important_caveats": [
    "The EC number annotation includes both RuleBase (computational) and experimental (PubMed) evidence codes; the experimental evidence (crystal structures, mutagenesis, catalytic assays) provides strong independent support.",
    "The sequence is a precursor (signal peptide present); the mature enzyme numbering differs from precursor numbering, but this does not affect the EC assignment.",
    "All reviewer evidence is from the current or archived UniProt snapshot; the author's exact source snapshot is unknown but sequence match is confirmed across versions."
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

**Accession:** `Q2TR58` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 133. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TR58.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:39.664161+00:00.  

```json
"Q2TR58"
```

Source SHA-256: `90800739268b3a91a720a2ca6b56cd2e1f1fdaaa169bc64ee8999ea5771dcb35`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TR58.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:39.664161+00:00.  

```json
{"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"RU361140","source":"RuleBase"},{"evidenceCode":"ECO:0000269","id":"15616297","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"26459904","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"26701320","source":"PubMed"}],"value":"3.5.2.6"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"RU361140","source":"RuleBase"},{"evidenceCode":"ECO:0000303","id":"15616297","source":"PubMed"}],"value":"Beta-lactamase OXA-58"}}}
```

Source SHA-256: `90800739268b3a91a720a2ca6b56cd2e1f1fdaaa169bc64ee8999ea5771dcb35`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TR58.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:39.664161+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.5.2.6","evidences":[{"evidenceCode":"ECO:0000269","id":"15616297","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"26459904","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"26701320","source":"PubMed"}],"name":"a beta-lactam + H2O = a substituted beta-amino acid","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:20401"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:35627"},{"database":"ChEBI","id":"CHEBI:140347"}]}}
```

Source SHA-256: `90800739268b3a91a720a2ca6b56cd2e1f1fdaaa169bc64ee8999ea5771dcb35`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TR58.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:39.664161+00:00.  

```json
{"citation":{"authors":["Poirel L.","Marque S.","Heritier C.","Segonds C.","Chabanon G.","Nordmann P."],"citationCrossReferences":[{"database":"PubMed","id":"15616297"},{"database":"DOI","id":"10.1128/aac.49.1.202-208.2005"}],"citationType":"journal article","firstPage":"202","id":"15616297","journal":"Antimicrob. Agents Chemother.","lastPage":"208","publicationDate":"2005","title":"OXA-58, a novel class D {beta}-lactamase involved in resistance to carbapenems in Acinetobacter baumannii.","volume":"49"},"evidences":[{"evidenceCode":"ECO:0000312","id":"AAW57529.1","source":"EMBL"}],"referenceComments":[{"evidences":[{"evidenceCode":"ECO:0000312","id":"AAW57529.1","source":"EMBL"}],"type":"STRAIN","value":"MAD"}],"referenceNumber":2,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES"]}
```

Source SHA-256: `90800739268b3a91a720a2ca6b56cd2e1f1fdaaa169bc64ee8999ea5771dcb35`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TR58.json)  
**Locator:** `/references/22`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:39.664161+00:00.  

```json
{"citation":{"authors":["Saino H.","Sugiyabu T.","Ueno G.","Yamamoto M.","Ishii Y.","Miyano M."],"citationCrossReferences":[{"database":"PubMed","id":"26701320"},{"database":"DOI","id":"10.1371/journal.pone.0145869"}],"citationType":"journal article","firstPage":"e0145869","id":"26701320","journal":"PLoS ONE","lastPage":"e0145869","publicationDate":"2015","title":"Crystal Structure of OXA-58 with the Substrate-Binding Cleft in a Closed State: Insights into the Mobility and Stability of the OXA-58 Structure.","volume":"10"},"evidences":[{"evidenceCode":"ECO:0007744","id":"5BOH","source":"PDB"}],"referenceNumber":23,"referencePositions":["X-RAY CRYSTALLOGRAPHY (1.80 ANGSTROMS) OF 44-280","FUNCTION","CATALYTIC ACTIVITY","ACTIVITY REGULATION","CARBOXYLATION AT LYS-86","MUTAGENESIS OF SER-83 AND TRP-169"]}
```

Source SHA-256: `90800739268b3a91a720a2ca6b56cd2e1f1fdaaa169bc64ee8999ea5771dcb35`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TR58.json)  
**Locator:** `/references/23`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:39.664161+00:00.  

```json
{"citation":{"authors":["Pratap S.","Katiki M.","Gill P.","Kumar P.","Golemi-Kotra D."],"citationCrossReferences":[{"database":"PubMed","id":"26459904"},{"database":"DOI","id":"10.1128/aac.01393-15"}],"citationType":"journal article","firstPage":"75","id":"26459904","journal":"Antimicrob. Agents Chemother.","lastPage":"86","publicationDate":"2016","title":"Active-Site Plasticity Is Essential to Carbapenem Hydrolysis by OXA-58 Class D beta-Lactamase of Acinetobacter baumannii.","volume":"60"},"evidences":[{"evidenceCode":"ECO:0007744","id":"4Y0O","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"4Y0T","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"4Y0U","source":"PDB"}],"referenceNumber":24,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.30 ANGSTROMS) IN APO FORM AND IN COMPLEXES WITH CARBAPENEM ANALOGS","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","CARBOXYLATION AT LYS-86","MUTAGENESIS OF PHE-113; PHE-114 AND MET-225"]}
```

Source SHA-256: `90800739268b3a91a720a2ca6b56cd2e1f1fdaaa169bc64ee8999ea5771dcb35`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2TR58?format=txt&versions=133)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 133 / 1.  
**Retrieved:** 2026-11-02T04:30:42.289456+00:00.  

```text
DE   RecName: Full=Beta-lactamase OXA-58 {ECO:0000255|RuleBase:RU361140, ECO:0000303|PubMed:15616297};
DE            EC=3.5.2.6 {ECO:0000255|RuleBase:RU361140, ECO:0000269|PubMed:15616297, ECO:0000269|PubMed:26459904, ECO:0000269|PubMed:26701320};
DE   Flags: Precursor;
```

Source SHA-256: `866adbe4a25883d784b4da01795f3c6d0f8328c05c58ea698350889ad138c921`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2TR58?format=txt&versions=133)  
**Locator:** `lines 39-47`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 133 / 1.  
**Retrieved:** 2026-11-02T04:30:42.289456+00:00.  

```text
RN   [2] {ECO:0000312|EMBL:AAW57529.1}
RP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, CATALYTIC ACTIVITY, AND
RP   BIOPHYSICOCHEMICAL PROPERTIES.
RC   STRAIN=MAD {ECO:0000312|EMBL:AAW57529.1};
RX   PubMed=15616297; DOI=10.1128/aac.49.1.202-208.2005;
RA   Poirel L., Marque S., Heritier C., Segonds C., Chabanon G., Nordmann P.;
RT   "OXA-58, a novel class D {beta}-lactamase involved in resistance to
RT   carbapenems in Acinetobacter baumannii.";
RL   Antimicrob. Agents Chemother. 49:202-208(2005).
```

Source SHA-256: `866adbe4a25883d784b4da01795f3c6d0f8328c05c58ea698350889ad138c921`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2TR58?format=txt&versions=133)  
**Locator:** `lines 227-235`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 133 / 1.  
**Retrieved:** 2026-11-02T04:30:42.289456+00:00.  

```text
RN   [23] {ECO:0007744|PDB:5BOH}
RP   X-RAY CRYSTALLOGRAPHY (1.80 ANGSTROMS) OF 44-280, FUNCTION, CATALYTIC
RP   ACTIVITY, ACTIVITY REGULATION, CARBOXYLATION AT LYS-86, AND MUTAGENESIS OF
RP   SER-83 AND TRP-169.
RX   PubMed=26701320; DOI=10.1371/journal.pone.0145869;
RA   Saino H., Sugiyabu T., Ueno G., Yamamoto M., Ishii Y., Miyano M.;
RT   "Crystal Structure of OXA-58 with the Substrate-Binding Cleft in a Closed
RT   State: Insights into the Mobility and Stability of the OXA-58 Structure.";
RL   PLoS ONE 10:e0145869-e0145869(2015).
```

Source SHA-256: `866adbe4a25883d784b4da01795f3c6d0f8328c05c58ea698350889ad138c921`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2TR58?format=txt&versions=133)  
**Locator:** `lines 236-245`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 133 / 1.  
**Retrieved:** 2026-11-02T04:30:42.289456+00:00.  

```text
RN   [24] {ECO:0007744|PDB:4Y0O, ECO:0007744|PDB:4Y0T, ECO:0007744|PDB:4Y0U}
RP   X-RAY CRYSTALLOGRAPHY (2.30 ANGSTROMS) IN APO FORM AND IN COMPLEXES WITH
RP   CARBAPENEM ANALOGS, FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL
RP   PROPERTIES, CARBOXYLATION AT LYS-86, AND MUTAGENESIS OF PHE-113; PHE-114
RP   AND MET-225.
RX   PubMed=26459904; DOI=10.1128/aac.01393-15;
RA   Pratap S., Katiki M., Gill P., Kumar P., Golemi-Kotra D.;
RT   "Active-Site Plasticity Is Essential to Carbapenem Hydrolysis by OXA-58
RT   Class D beta-Lactamase of Acinetobacter baumannii.";
RL   Antimicrob. Agents Chemother. 60:75-86(2016).
```

Source SHA-256: `866adbe4a25883d784b4da01795f3c6d0f8328c05c58ea698350889ad138c921`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2TR58?format=txt&versions=133)  
**Locator:** `lines 266-271`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 133 / 1.  
**Retrieved:** 2026-11-02T04:30:42.289456+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=a beta-lactam + H2O = a substituted beta-amino acid;
CC         Xref=Rhea:RHEA:20401, ChEBI:CHEBI:15377, ChEBI:CHEBI:35627,
CC         ChEBI:CHEBI:140347; EC=3.5.2.6;
CC         Evidence={ECO:0000269|PubMed:15616297, ECO:0000269|PubMed:26459904,
CC         ECO:0000269|PubMed:26701320};
```

Source SHA-256: `866adbe4a25883d784b4da01795f3c6d0f8328c05c58ea698350889ad138c921`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 196. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
