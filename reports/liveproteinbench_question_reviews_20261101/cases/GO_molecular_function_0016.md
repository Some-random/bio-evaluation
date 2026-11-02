# GO_molecular_function_0016

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **D** — beta-lactamase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKLLKILSLVCLSISIGACAEHSMSRAKTSTIPQVNNSIIDQNVQALFNEISADAVFVTYDGQNIKKYGTHLDRAKTAYIPASTFKIANALIGLENHKATSTEIFKWDGKPRFFKAWDKDFTLGEAMQASTVPVYQELARRIGPSLMQSELQRIGYGNMQIGTEVDQFWLKGPLTITPIQEVKFVYDLAQGQLPFKPEVQQQVKEMLYVERRGENRLYAKSGWGMAVDPQVGWYVGFVEKADGQVVAFALNMQMKAGDDIALRKQLSLDVLDKLGVFHYL

[Multiple Choices]
A. mRNA binding
B. beta-glucuronidase activity
C. oxidoreductase activity, acting on NAD(P)H
D. beta-lactamase activity
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

> The supplied sequence matches the historical OXA-58 record, which reports beta-lactam hydrolysis and beta-lactamase activity with experimental evidence. This supports choice D.

Citations as saved: [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the characteristic STFK motif of class D beta-lactamases, along with a YGN motif; these sequence features support beta-lactamase activity over the listed binding, glucuronidase, and NAD(P)H-dependent oxidoreductase alternatives.


**Missing item-specific fact**

> No item-specific annotation is necessary for the broad distinction if the characteristic motifs are recognized; exact OXA-58 identity and experimentally documented substrate activity are not supplied.


**Reason**

> The sequence provides recognizable enzyme-family evidence that meaningfully favors beta-lactamase activity. The reviewer-only database evidence supports the key but is not needed as input to this inference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The listed alternatives describe distinct functions, and the sequence motifs support beta-lactamase activity.


### Important caveats

- The historical UniProt record and experimental evidence support this exact sequence; this does not imply that every listed substrate is hydrolyzed equally or in every biological context.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the characteristic STFK motif of class D beta-lactamases, along with a YGN motif; these sequence features support beta-lactamase activity over the listed binding, glucuronidase, and NAD(P)H-dependent oxidoreductase alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No item-specific annotation is necessary for the broad distinction if the characteristic motifs are recognized; exact OXA-58 identity and experimentally documented substrate activity are not supplied.",
    "reason": "The sequence provides recognizable enzyme-family evidence that meaningfully favors beta-lactamase activity. The reviewer-only database evidence supports the key but is not needed as input to this inference."
  },
  "case_id": "GO_molecular_function_0016",
  "expected_answer_check": {
    "evidence_ids": [
      "H5",
      "H6",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches the historical OXA-58 record, which reports beta-lactam hydrolysis and beta-lactamase activity with experimental evidence. This supports choice D."
  },
  "important_caveats": [
    "The historical UniProt record and experimental evidence support this exact sequence; this does not imply that every listed substrate is hydrolyzed equally or in every biological context."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The listed alternatives describe distinct functions, and the sequence motifs support beta-lactamase activity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0016",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches the historical OXA-58 record, which reports beta-lactam hydrolysis and beta-lactamase activity with experimental evidence. This supports choice D.",
    "evidence_ids": ["H5", "H6", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the characteristic STFK motif of class D beta-lactamases, along with a YGN motif; these sequence features support beta-lactamase activity over the listed binding, glucuronidase, and NAD(P)H-dependent oxidoreductase alternatives.",
    "missing_item_specific_fact": "No item-specific annotation is necessary for the broad distinction if the characteristic motifs are recognized; exact OXA-58 identity and experimentally documented substrate activity are not supplied.",
    "reason": "The sequence provides recognizable enzyme-family evidence that meaningfully favors beta-lactamase activity. The reviewer-only database evidence supports the key but is not needed as input to this inference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The listed alternatives describe distinct functions, and the sequence motifs support beta-lactamase activity."
  },
  "important_caveats": [
    "The historical UniProt record and experimental evidence support this exact sequence; this does not imply that every listed substrate is hydrolyzed equally or in every biological context."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt Q2TR58 (Beta-lactamase OXA-58, Acinetobacter baumannii) with exact sequence comparison. The entry carries GO:0008800 (beta-lactamase activity) annotated with EXP:UniProtKB evidence, supported by experimental data from PubMed:15616297, PubMed:26459904, and PubMed:26701320, including X-ray crystallography (PDB: 5BOH, 4Y0O, 4Y0T, 4Y0U). The EC number 3.5.2.6 and the function comment ('Class D beta-lactamase… Acts via hydrolysis of the beta-lactam ring') confirm the molecular function. Multiple experimental references establish this as experimentally verified, not merely computational inference.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [H1](#evidence-h1), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the STFK motif (…HKATSTEIFKWDGK…, approximately residues 83-86), which is the hallmark active-site motif of class D (OXA-type) serine beta-lactamases. The N-terminal hydrophobic stretch (MKLLKILSLVCLSISIGACAE) is a recognizable signal peptide consistent with a periplasmic enzyme. The total length (~280 aa) is consistent with beta-lactamases. The other options can be excluded by general knowledge: beta-glucuronidases are ~600+ aa with distinct catalytic motifs; NAD(P)H oxidoreductases require a Rossmann-fold GxGxxG dinucleotide-binding motif absent here; mRNA-binding proteins display RGG, KH, or RRM domains not present in this sequence. The STFK motif is a textbook-level identifier for class D beta-lactamases that a knowledgeable biologist could recognize from the raw sequence.


**Missing item-specific fact**

> None critical. Recognition of the STFK motif and exclusion of other options relies on general knowledge of enzyme-family signatures rather than a protein-specific database lookup.


**Reason**

> The sequence itself provides identifiable structural motifs (STFK active-site signature, signal peptide, appropriate size) that allow a biologist with general knowledge of enzyme families to select beta-lactamase activity and exclude the three distractors without needing to look up this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractors are clearly wrong: mRNA-binding proteins have RNA-recognition motifs absent here; beta-glucuronidases are much larger (~600+ aa) glycosidases; NAD(P)H oxidoreductases require Rossmann-fold motifs not present. The STFK motif and overall architecture point unambiguously to a serine beta-lactamase.


### Important caveats

- The STFK motif recognition requires specific knowledge of class D beta-lactamase families; a model without this domain knowledge might struggle, but this is legitimate expert biological reasoning, not item-specific memorization.
- The UniProt annotation evidence is experimental (EXP) with multiple independent publications and crystal structures, providing strong support for the key.
- The sequence-match is exact (SHA-256 identical) between the benchmark input and both current and historical UniProt entries.
- The GO term GO:0008800 in the ontology exactly matches option D text, confirming terminological alignment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the STFK motif (…HKATSTEIFKWDGK…, approximately residues 83-86), which is the hallmark active-site motif of class D (OXA-type) serine beta-lactamases. The N-terminal hydrophobic stretch (MKLLKILSLVCLSISIGACAE) is a recognizable signal peptide consistent with a periplasmic enzyme. The total length (~280 aa) is consistent with beta-lactamases. The other options can be excluded by general knowledge: beta-glucuronidases are ~600+ aa with distinct catalytic motifs; NAD(P)H oxidoreductases require a Rossmann-fold GxGxxG dinucleotide-binding motif absent here; mRNA-binding proteins display RGG, KH, or RRM domains not present in this sequence. The STFK motif is a textbook-level identifier for class D beta-lactamases that a knowledgeable biologist could recognize from the raw sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. Recognition of the STFK motif and exclusion of other options relies on general knowledge of enzyme-family signatures rather than a protein-specific database lookup.",
    "reason": "The sequence itself provides identifiable structural motifs (STFK active-site signature, signal peptide, appropriate size) that allow a biologist with general knowledge of enzyme families to select beta-lactamase activity and exclude the three distractors without needing to look up this specific protein's database entry."
  },
  "case_id": "GO_molecular_function_0016",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C9",
      "C10",
      "C11",
      "H1",
      "H5",
      "H6",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q2TR58 (Beta-lactamase OXA-58, Acinetobacter baumannii) with exact sequence comparison. The entry carries GO:0008800 (beta-lactamase activity) annotated with EXP:UniProtKB evidence, supported by experimental data from PubMed:15616297, PubMed:26459904, and PubMed:26701320, including X-ray crystallography (PDB: 5BOH, 4Y0O, 4Y0T, 4Y0U). The EC number 3.5.2.6 and the function comment ('Class D beta-lactamase… Acts via hydrolysis of the beta-lactam ring') confirm the molecular function. Multiple experimental references establish this as experimentally verified, not merely computational inference."
  },
  "important_caveats": [
    "The STFK motif recognition requires specific knowledge of class D beta-lactamase families; a model without this domain knowledge might struggle, but this is legitimate expert biological reasoning, not item-specific memorization.",
    "The UniProt annotation evidence is experimental (EXP) with multiple independent publications and crystal structures, providing strong support for the key.",
    "The sequence-match is exact (SHA-256 identical) between the benchmark input and both current and historical UniProt entries.",
    "The GO term GO:0008800 in the ontology exactly matches option D text, confirming terminological alignment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors are clearly wrong: mRNA-binding proteins have RNA-recognition motifs absent here; beta-glucuronidases are much larger (~600+ aa) glycosidases; NAD(P)H oxidoreductases require Rossmann-fold motifs not present. The STFK motif and overall architecture point unambiguously to a serine beta-lactamase."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0016",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q2TR58 (Beta-lactamase OXA-58, Acinetobacter baumannii) with exact sequence comparison. The entry carries GO:0008800 (beta-lactamase activity) annotated with EXP:UniProtKB evidence, supported by experimental data from PubMed:15616297, PubMed:26459904, and PubMed:26701320, including X-ray crystallography (PDB: 5BOH, 4Y0O, 4Y0T, 4Y0U). The EC number 3.5.2.6 and the function comment ('Class D beta-lactamase… Acts via hydrolysis of the beta-lactam ring') confirm the molecular function. Multiple experimental references establish this as experimentally verified, not merely computational inference.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C9", "C10", "C11", "H1", "H5", "H6", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the STFK motif (…HKATSTEIFKWDGK…, approximately residues 83-86), which is the hallmark active-site motif of class D (OXA-type) serine beta-lactamases. The N-terminal hydrophobic stretch (MKLLKILSLVCLSISIGACAE) is a recognizable signal peptide consistent with a periplasmic enzyme. The total length (~280 aa) is consistent with beta-lactamases. The other options can be excluded by general knowledge: beta-glucuronidases are ~600+ aa with distinct catalytic motifs; NAD(P)H oxidoreductases require a Rossmann-fold GxGxxG dinucleotide-binding motif absent here; mRNA-binding proteins display RGG, KH, or RRM domains not present in this sequence. The STFK motif is a textbook-level identifier for class D beta-lactamases that a knowledgeable biologist could recognize from the raw sequence.",
    "missing_item_specific_fact": "None critical. Recognition of the STFK motif and exclusion of other options relies on general knowledge of enzyme-family signatures rather than a protein-specific database lookup.",
    "reason": "The sequence itself provides identifiable structural motifs (STFK active-site signature, signal peptide, appropriate size) that allow a biologist with general knowledge of enzyme families to select beta-lactamase activity and exclude the three distractors without needing to look up this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors are clearly wrong: mRNA-binding proteins have RNA-recognition motifs absent here; beta-glucuronidases are much larger (~600+ aa) glycosidases; NAD(P)H oxidoreductases require Rossmann-fold motifs not present. The STFK motif and overall architecture point unambiguously to a serine beta-lactamase."
  },
  "important_caveats": [
    "The STFK motif recognition requires specific knowledge of class D beta-lactamase families; a model without this domain knowledge might struggle, but this is legitimate expert biological reasoning, not item-specific memorization.",
    "The UniProt annotation evidence is experimental (EXP) with multiple independent publications and crystal structures, providing strong support for the key.",
    "The sequence-match is exact (SHA-256 identical) between the benchmark input and both current and historical UniProt entries.",
    "The GO term GO:0008800 in the ontology exactly matches option D text, confirming terminological alignment."
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
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

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
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:39.664161+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"15616297","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"26459904","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"26701320","source":"PubMed"}],"value":"Class D beta-lactamase which confers resistance to the beta-lactam antibiotics, including penicillins and oxacillin, and moderate resistance to carbapenems such as imipenem; in the DH10B strain of E.coli (PubMed:15616297). Acts via hydrolysis of the beta-lactam ring (PubMed:15616297, PubMed:26459904, PubMed:26701320). Has benzylpenicillin-, oxacillin-, cephalothin- and imipenem-hydrolyzing activities (PubMed:15616297, PubMed:26459904, PubMed:26701320)"}]}
```

Source SHA-256: `90800739268b3a91a720a2ca6b56cd2e1f1fdaaa169bc64ee8999ea5771dcb35`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TR58.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:39.664161+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.5.2.6","evidences":[{"evidenceCode":"ECO:0000269","id":"15616297","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"26459904","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"26701320","source":"PubMed"}],"name":"a beta-lactam + H2O = a substituted beta-amino acid","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:20401"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:35627"},{"database":"ChEBI","id":"CHEBI:140347"}]}}
```

Source SHA-256: `90800739268b3a91a720a2ca6b56cd2e1f1fdaaa169bc64ee8999ea5771dcb35`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TR58.json)  
**Locator:** `/uniProtKBCrossReferences/72`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:39.664161+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000269","id":"15616297","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"26459904","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"26701320","source":"PubMed"}],"id":"GO:0008800","properties":[{"key":"GoTerm","value":"F:beta-lactamase activity"},{"key":"GoEvidenceType","value":"EXP:UniProtKB"}]}
```

Source SHA-256: `90800739268b3a91a720a2ca6b56cd2e1f1fdaaa169bc64ee8999ea5771dcb35`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TR58.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:39.664161+00:00.  

```json
{"citation":{"authors":["Poirel L.","Marque S.","Heritier C.","Segonds C.","Chabanon G.","Nordmann P."],"citationCrossReferences":[{"database":"PubMed","id":"15616297"},{"database":"DOI","id":"10.1128/aac.49.1.202-208.2005"}],"citationType":"journal article","firstPage":"202","id":"15616297","journal":"Antimicrob. Agents Chemother.","lastPage":"208","publicationDate":"2005","title":"OXA-58, a novel class D {beta}-lactamase involved in resistance to carbapenems in Acinetobacter baumannii.","volume":"49"},"evidences":[{"evidenceCode":"ECO:0000312","id":"AAW57529.1","source":"EMBL"}],"referenceComments":[{"evidences":[{"evidenceCode":"ECO:0000312","id":"AAW57529.1","source":"EMBL"}],"type":"STRAIN","value":"MAD"}],"referenceNumber":2,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES"]}
```

Source SHA-256: `90800739268b3a91a720a2ca6b56cd2e1f1fdaaa169bc64ee8999ea5771dcb35`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TR58.json)  
**Locator:** `/references/22`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:39.664161+00:00.  

```json
{"citation":{"authors":["Saino H.","Sugiyabu T.","Ueno G.","Yamamoto M.","Ishii Y.","Miyano M."],"citationCrossReferences":[{"database":"PubMed","id":"26701320"},{"database":"DOI","id":"10.1371/journal.pone.0145869"}],"citationType":"journal article","firstPage":"e0145869","id":"26701320","journal":"PLoS ONE","lastPage":"e0145869","publicationDate":"2015","title":"Crystal Structure of OXA-58 with the Substrate-Binding Cleft in a Closed State: Insights into the Mobility and Stability of the OXA-58 Structure.","volume":"10"},"evidences":[{"evidenceCode":"ECO:0007744","id":"5BOH","source":"PDB"}],"referenceNumber":23,"referencePositions":["X-RAY CRYSTALLOGRAPHY (1.80 ANGSTROMS) OF 44-280","FUNCTION","CATALYTIC ACTIVITY","ACTIVITY REGULATION","CARBOXYLATION AT LYS-86","MUTAGENESIS OF SER-83 AND TRP-169"]}
```

Source SHA-256: `90800739268b3a91a720a2ca6b56cd2e1f1fdaaa169bc64ee8999ea5771dcb35`.

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TR58.json)  
**Locator:** `/references/23`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:39.664161+00:00.  

```json
{"citation":{"authors":["Pratap S.","Katiki M.","Gill P.","Kumar P.","Golemi-Kotra D."],"citationCrossReferences":[{"database":"PubMed","id":"26459904"},{"database":"DOI","id":"10.1128/aac.01393-15"}],"citationType":"journal article","firstPage":"75","id":"26459904","journal":"Antimicrob. Agents Chemother.","lastPage":"86","publicationDate":"2016","title":"Active-Site Plasticity Is Essential to Carbapenem Hydrolysis by OXA-58 Class D beta-Lactamase of Acinetobacter baumannii.","volume":"60"},"evidences":[{"evidenceCode":"ECO:0007744","id":"4Y0O","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"4Y0T","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"4Y0U","source":"PDB"}],"referenceNumber":24,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.30 ANGSTROMS) IN APO FORM AND IN COMPLEXES WITH CARBAPENEM ANALOGS","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","CARBOXYLATION AT LYS-86","MUTAGENESIS OF PHE-113; PHE-114 AND MET-225"]}
```

Source SHA-256: `90800739268b3a91a720a2ca6b56cd2e1f1fdaaa169bc64ee8999ea5771dcb35`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2TR58?format=txt&versions=133)  
**Locator:** `lines 1-30`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 133 / 1.  
**Retrieved:** 2026-11-02T04:30:42.289456+00:00.  

```text
ID   OXA58_ACIBA             Reviewed;         280 AA.
AC   Q2TR58; A5H882;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   24-JAN-2006, sequence version 1.
DT   28-JAN-2026, entry version 133.
DE   RecName: Full=Beta-lactamase OXA-58 {ECO:0000255|RuleBase:RU361140, ECO:0000303|PubMed:15616297};
DE            EC=3.5.2.6 {ECO:0000255|RuleBase:RU361140, ECO:0000269|PubMed:15616297, ECO:0000269|PubMed:26459904, ECO:0000269|PubMed:26701320};
DE   Flags: Precursor;
GN   Name=OXA-58 {ECO:0000303|PubMed:15616297};
GN   Synonyms=bla-oxa-58 {ECO:0000312|EMBL:ABU97485.1},
GN   bla-oxa58 {ECO:0000312|EMBL:ABQ23512.2},
GN   blaOXA-58 {ECO:0000312|EMBL:AAW57529.1};
GN   ORFNames=EKS29_04300 {ECO:0000312|EMBL:RTY12892.1},
GN   GSE42_20550 {ECO:0000312|EMBL:MYM80302.1},
GN   H0529_21805 {ECO:0000312|EMBL:QOJ62286.1},
GN   P9867_019230 {ECO:0000312|EMBL:MEC5498499.1},
GN   P9867_20895 {ECO:0000312|EMBL:MDK4883960.1};
OS   Acinetobacter baumannii.
OG   Plasmid pA2445 {ECO:0000312|EMBL:AGC51039.1},
OG   Plasmid pABIR {ECO:0000312|EMBL:ACB05799.1},
OG   Plasmid pABNA1 {ECO:0000312|EMBL:ACT98250.1},
OG   Plasmid pABNA2 {ECO:0000312|EMBL:ACT98258.1},
OG   Plasmid pAC1633-1 {ECO:0000312|EMBL:QOJ62286.1},
OG   Plasmid pOUR {ECO:0000312|EMBL:ABQ23503.1},
OG   Plasmid pWA3 {ECO:0000312|EMBL:AFF18250.1}, and
OG   Plasmid pWH8144 {ECO:0000312|EMBL:AFH57370.1}.
OC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;
OC   Moraxellales; Moraxellaceae; Acinetobacter;
OC   Acinetobacter calcoaceticus/baumannii complex.
OX   NCBI_TaxID=470 {ECO:0000312|EMBL:AAW57529.1};
```

Source SHA-256: `866adbe4a25883d784b4da01795f3c6d0f8328c05c58ea698350889ad138c921`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2TR58?format=txt&versions=133)  
**Locator:** `lines 257-265`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 133 / 1.  
**Retrieved:** 2026-11-02T04:30:42.289456+00:00.  

```text
CC   -!- FUNCTION: Class D beta-lactamase which confers resistance to the beta-
CC       lactam antibiotics, including penicillins and oxacillin, and moderate
CC       resistance to carbapenems such as imipenem; in the DH10B strain of
CC       E.coli (PubMed:15616297). Acts via hydrolysis of the beta-lactam ring
CC       (PubMed:15616297, PubMed:26459904, PubMed:26701320). Has
CC       benzylpenicillin-, oxacillin-, cephalothin- and imipenem-hydrolyzing
CC       activities (PubMed:15616297, PubMed:26459904, PubMed:26701320).
CC       {ECO:0000269|PubMed:15616297, ECO:0000269|PubMed:26459904,
CC       ECO:0000269|PubMed:26701320}.
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

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2TR58?format=txt&versions=133)  
**Locator:** `lines 429-429`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 133 / 1.  
**Retrieved:** 2026-11-02T04:30:42.289456+00:00.  

```text
DR   GO; GO:0008800; F:beta-lactamase activity; IEA:UniProtKB-EC.
```

Source SHA-256: `866adbe4a25883d784b4da01795f3c6d0f8328c05c58ea698350889ad138c921`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 16. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
