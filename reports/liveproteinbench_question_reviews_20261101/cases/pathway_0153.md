# pathway_0153

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **A** — Cell wall biogenesis

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKKIAIIFGGNSPEYTVSLASATSAIEALQSSPYDYDLSLIGIAPDAMDWYLYTGELENIRQDTWLLDTKHKQKIQPLFEGNGFWLSEEQQTLVPDVLFPIMHGKYGEDGSIQGLFELMKLPYVGCGVAGSALCMNKWLLHQAAAAIGVQSAPTILLTNQANQQEQIEAFIQTHGFPVFFKPNEAGSSKGITKVTCVEEIASALKEAFTYCSAVLLQKNIAGVEIGCGILGNDSLTVGACDAISLVDGFFDFEEKYQLISAKITVPAPLPETIETKVKEQAQLLYRSLGLKGLARIDFFVTERGELYLNEINTMPGFTSHSRYPAMMAAVGLSYQELLQKLLVLAKEEVK

[Multiple Choices]
A. Cell wall biogenesis
B. Bacterial outer membrane biogenesis
C. LPS O-antigen biosynthesis. .
D. chorismate biosynthesis
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

> The exact sequence matches the VanC2 D-Ala-D-Ser ligase entry, whose pathway annotation is cell wall biogenesis/peptidoglycan biosynthesis. This pathway assignment is explicitly attributed to a HAMAP computational rule; the cited research concerns characterization of the ligase, rather than independently establishing the pathway in the supplied excerpt.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A ligase that supplies D-Ala-D-Ser for peptidoglycan precursor synthesis fits cell wall biogenesis, but the supplied input gives only an unannotated sequence and choices; it does not identify this protein's substrate or role.


**Missing item-specific fact**

> The sequence-specific identification as VanC2, a D-Ala-D-Ser ligase involved in peptidoglycan biosynthesis.


**Reason**

> The pathway distinction depends on recognizing or looking up this protein's specific enzymatic function. The choices alone and general sequence inspection do not establish that function.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched annotation specifically assigns cell wall biogenesis and peptidoglycan biosynthesis; the other choices are not supported by the supplied sequence-level information.


### Important caveats

- The organism and accession were not supplied to the evaluated model; the sequence match and associated annotations are reviewer-only evidence.
- The pathway annotation is computationally supported by HAMAP. The cited literature is described as experimentally characterizing VanC2 ligase, but its detailed findings were not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A ligase that supplies D-Ala-D-Ser for peptidoglycan precursor synthesis fits cell wall biogenesis, but the supplied input gives only an unannotated sequence and choices; it does not identify this protein's substrate or role.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence-specific identification as VanC2, a D-Ala-D-Ser ligase involved in peptidoglycan biosynthesis.",
    "reason": "The pathway distinction depends on recognizing or looking up this protein's specific enzymatic function. The choices alone and general sequence inspection do not establish that function."
  },
  "case_id": "pathway_0153",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the VanC2 D-Ala-D-Ser ligase entry, whose pathway annotation is cell wall biogenesis/peptidoglycan biosynthesis. This pathway assignment is explicitly attributed to a HAMAP computational rule; the cited research concerns characterization of the ligase, rather than independently establishing the pathway in the supplied excerpt."
  },
  "important_caveats": [
    "The organism and accession were not supplied to the evaluated model; the sequence match and associated annotations are reviewer-only evidence.",
    "The pathway annotation is computationally supported by HAMAP. The cited literature is described as experimentally characterizing VanC2 ligase, but its detailed findings were not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched annotation specifically assigns cell wall biogenesis and peptidoglycan biosynthesis; the other choices are not supported by the supplied sequence-level information."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0153",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the VanC2 D-Ala-D-Ser ligase entry, whose pathway annotation is cell wall biogenesis/peptidoglycan biosynthesis. This pathway assignment is explicitly attributed to a HAMAP computational rule; the cited research concerns characterization of the ligase, rather than independently establishing the pathway in the supplied excerpt.",
    "evidence_ids": ["C4", "C5", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A ligase that supplies D-Ala-D-Ser for peptidoglycan precursor synthesis fits cell wall biogenesis, but the supplied input gives only an unannotated sequence and choices; it does not identify this protein's substrate or role.",
    "missing_item_specific_fact": "The sequence-specific identification as VanC2, a D-Ala-D-Ser ligase involved in peptidoglycan biosynthesis.",
    "reason": "The pathway distinction depends on recognizing or looking up this protein's specific enzymatic function. The choices alone and general sequence inspection do not establish that function."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched annotation specifically assigns cell wall biogenesis and peptidoglycan biosynthesis; the other choices are not supported by the supplied sequence-level information."
  },
  "important_caveats": [
    "The organism and accession were not supplied to the evaluated model; the sequence match and associated annotations are reviewer-only evidence.",
    "The pathway annotation is computationally supported by HAMAP. The cited literature is described as experimentally characterizing VanC2 ligase, but its detailed findings were not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q47720 (VanC2, D-alanine--D-serine ligase, EC 6.3.2.35) carries the PATHWAY annotation 'Cell wall biogenesis; peptidoglycan biosynthesis' (C5, H4). The protein's catalytic function as a D-Ala-D-Ser ligase is experimentally confirmed by PubMed 9294159 and 9545431 (C6, C7, H2, H3). The pathway assignment (HAMAP rule MF_00047) is a computational inference from protein family membership, but it is consistent with the experimentally verified function: D-Ala-D-Ser ligase participates in peptidoglycan precursor synthesis, a core step of cell wall biogenesis. The expected answer 'Cell wall biogenesis' matches the UniProt pathway annotation directly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The ~350-residue sequence contains features consistent with the D-alanine:D-alanine ligase (Ddl) / Van ligase superfamily, including a P-loop-like 'GCGVAG' motif region characteristic of ATP-binding ligases in peptidoglycan biosynthesis. Ddl and its Van homologs are well-known, textbook enzymes in peptidoglycan (cell wall) biosynthesis. A model with general knowledge of peptidoglycan biosynthesis can recognize ligase-type features and associate D-Ala ligase activity with peptidoglycan precursor assembly, leading to 'cell wall biogenesis.' The distractors (outer membrane biogenesis via Lol/BAM, LPS O-antigen via glycosyltransferases, chorismate biosynthesis via shikimate-pathway enzymes) involve mechanistically distinct enzyme classes unrelated to D-Ala ligases.


**Missing item-specific fact**

> None critical. Recognizing the specific VanC2 identity (D-Ala-D-Ser vs. D-Ala-D-Ala ligase) requires item-specific knowledge, but this distinction does not alter the pathway assignment, since both Ddl and Van ligases function in peptidoglycan biosynthesis / cell wall biogenesis.


**Reason**

> The Ddl/Van ligase superfamily is a well-characterized class in peptidoglycan biosynthesis. Sequence-level recognition of ligase-type motifs and the ~350-aa architecture is within the scope of general biochemical knowledge. The four choices span mechanistically distinct pathways, so identifying the enzyme as a D-Ala-type ligase suffices to select 'cell wall biogenesis' without memorizing the exact UniProt annotation for this particular protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent mechanistically distinct pathways. A D-Ala ligase (whether Ddl or Van-type) is unambiguously part of peptidoglycan biosynthesis (cell wall biogenesis). Outer membrane biogenesis (Lol/BAM machinery), LPS O-antigen biosynthesis (glycosyltransferases, polymerases), and chorismate biosynthesis (shikimate pathway enzymes such as DAHP synthase, shikimate kinase, EPSP synthase) do not involve D-Ala ligases. No alternative choice is defensible.


### Important caveats

- The pathway annotation in UniProt is assigned via HAMAP rule MF_00047 (ECO:0000255, computational/protein-family inference), not a direct experimental pathway measurement. However, the underlying catalytic function is experimentally confirmed.
- Recognizing the Ddl/Van fold from a raw 350-aa sequence without structural context is non-trivial; a model may rely on pattern-matching to known ligase motifs rather than de novo fold prediction.
- The protein is from Enterococcus casseliflavus (a Gram-positive organism). The 'cell wall biogenesis' label is appropriate for peptidoglycan synthesis in this context. The distractor 'bacterial outer membrane biogenesis' is particularly inapplicable to a Gram-positive organism, which lacks an outer membrane, though the question does not state the organism.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The ~350-residue sequence contains features consistent with the D-alanine:D-alanine ligase (Ddl) / Van ligase superfamily, including a P-loop-like 'GCGVAG' motif region characteristic of ATP-binding ligases in peptidoglycan biosynthesis. Ddl and its Van homologs are well-known, textbook enzymes in peptidoglycan (cell wall) biosynthesis. A model with general knowledge of peptidoglycan biosynthesis can recognize ligase-type features and associate D-Ala ligase activity with peptidoglycan precursor assembly, leading to 'cell wall biogenesis.' The distractors (outer membrane biogenesis via Lol/BAM, LPS O-antigen via glycosyltransferases, chorismate biosynthesis via shikimate-pathway enzymes) involve mechanistically distinct enzyme classes unrelated to D-Ala ligases.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. Recognizing the specific VanC2 identity (D-Ala-D-Ser vs. D-Ala-D-Ala ligase) requires item-specific knowledge, but this distinction does not alter the pathway assignment, since both Ddl and Van ligases function in peptidoglycan biosynthesis / cell wall biogenesis.",
    "reason": "The Ddl/Van ligase superfamily is a well-characterized class in peptidoglycan biosynthesis. Sequence-level recognition of ligase-type motifs and the ~350-aa architecture is within the scope of general biochemical knowledge. The four choices span mechanistically distinct pathways, so identifying the enzyme as a D-Ala-type ligase suffices to select 'cell wall biogenesis' without memorizing the exact UniProt annotation for this particular protein."
  },
  "case_id": "pathway_0153",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q47720 (VanC2, D-alanine--D-serine ligase, EC 6.3.2.35) carries the PATHWAY annotation 'Cell wall biogenesis; peptidoglycan biosynthesis' (C5, H4). The protein's catalytic function as a D-Ala-D-Ser ligase is experimentally confirmed by PubMed 9294159 and 9545431 (C6, C7, H2, H3). The pathway assignment (HAMAP rule MF_00047) is a computational inference from protein family membership, but it is consistent with the experimentally verified function: D-Ala-D-Ser ligase participates in peptidoglycan precursor synthesis, a core step of cell wall biogenesis. The expected answer 'Cell wall biogenesis' matches the UniProt pathway annotation directly."
  },
  "important_caveats": [
    "The pathway annotation in UniProt is assigned via HAMAP rule MF_00047 (ECO:0000255, computational/protein-family inference), not a direct experimental pathway measurement. However, the underlying catalytic function is experimentally confirmed.",
    "Recognizing the Ddl/Van fold from a raw 350-aa sequence without structural context is non-trivial; a model may rely on pattern-matching to known ligase motifs rather than de novo fold prediction.",
    "The protein is from Enterococcus casseliflavus (a Gram-positive organism). The 'cell wall biogenesis' label is appropriate for peptidoglycan synthesis in this context. The distractor 'bacterial outer membrane biogenesis' is particularly inapplicable to a Gram-positive organism, which lacks an outer membrane, though the question does not state the organism."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent mechanistically distinct pathways. A D-Ala ligase (whether Ddl or Van-type) is unambiguously part of peptidoglycan biosynthesis (cell wall biogenesis). Outer membrane biogenesis (Lol/BAM machinery), LPS O-antigen biosynthesis (glycosyltransferases, polymerases), and chorismate biosynthesis (shikimate pathway enzymes such as DAHP synthase, shikimate kinase, EPSP synthase) do not involve D-Ala ligases. No alternative choice is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0153",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q47720 (VanC2, D-alanine--D-serine ligase, EC 6.3.2.35) carries the PATHWAY annotation 'Cell wall biogenesis; peptidoglycan biosynthesis' (C5, H4). The protein's catalytic function as a D-Ala-D-Ser ligase is experimentally confirmed by PubMed 9294159 and 9545431 (C6, C7, H2, H3). The pathway assignment (HAMAP rule MF_00047) is a computational inference from protein family membership, but it is consistent with the experimentally verified function: D-Ala-D-Ser ligase participates in peptidoglycan precursor synthesis, a core step of cell wall biogenesis. The expected answer 'Cell wall biogenesis' matches the UniProt pathway annotation directly.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The ~350-residue sequence contains features consistent with the D-alanine:D-alanine ligase (Ddl) / Van ligase superfamily, including a P-loop-like 'GCGVAG' motif region characteristic of ATP-binding ligases in peptidoglycan biosynthesis. Ddl and its Van homologs are well-known, textbook enzymes in peptidoglycan (cell wall) biosynthesis. A model with general knowledge of peptidoglycan biosynthesis can recognize ligase-type features and associate D-Ala ligase activity with peptidoglycan precursor assembly, leading to 'cell wall biogenesis.' The distractors (outer membrane biogenesis via Lol/BAM, LPS O-antigen via glycosyltransferases, chorismate biosynthesis via shikimate-pathway enzymes) involve mechanistically distinct enzyme classes unrelated to D-Ala ligases.",
    "missing_item_specific_fact": "None critical. Recognizing the specific VanC2 identity (D-Ala-D-Ser vs. D-Ala-D-Ala ligase) requires item-specific knowledge, but this distinction does not alter the pathway assignment, since both Ddl and Van ligases function in peptidoglycan biosynthesis / cell wall biogenesis.",
    "reason": "The Ddl/Van ligase superfamily is a well-characterized class in peptidoglycan biosynthesis. Sequence-level recognition of ligase-type motifs and the ~350-aa architecture is within the scope of general biochemical knowledge. The four choices span mechanistically distinct pathways, so identifying the enzyme as a D-Ala-type ligase suffices to select 'cell wall biogenesis' without memorizing the exact UniProt annotation for this particular protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent mechanistically distinct pathways. A D-Ala ligase (whether Ddl or Van-type) is unambiguously part of peptidoglycan biosynthesis (cell wall biogenesis). Outer membrane biogenesis (Lol/BAM machinery), LPS O-antigen biosynthesis (glycosyltransferases, polymerases), and chorismate biosynthesis (shikimate pathway enzymes such as DAHP synthase, shikimate kinase, EPSP synthase) do not involve D-Ala ligases. No alternative choice is defensible."
  },
  "important_caveats": [
    "The pathway annotation in UniProt is assigned via HAMAP rule MF_00047 (ECO:0000255, computational/protein-family inference), not a direct experimental pathway measurement. However, the underlying catalytic function is experimentally confirmed.",
    "Recognizing the Ddl/Van fold from a raw 350-aa sequence without structural context is non-trivial; a model may rely on pattern-matching to known ligase motifs rather than de novo fold prediction.",
    "The protein is from Enterococcus casseliflavus (a Gram-positive organism). The 'cell wall biogenesis' label is appropriate for peptidoglycan synthesis in this context. The distractor 'bacterial outer membrane biogenesis' is particularly inapplicable to a Gram-positive organism, which lacks an outer membrane, though the question does not state the organism."
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

**Accession:** `Q47720` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 147. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q47720.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:46.048238+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_00047","source":"HAMAP-Rule"}],"value":"D-alanine--D-serine ligase"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"VanC2 ligase"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"9294159","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"9545431","source":"PubMed"}],"value":"6.3.2.35"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"9294159","source":"PubMed"},{"evidenceCode":"ECO:0000305"}],"value":"Vancomycin C-type resistance protein VanC2"}}}
```

Source SHA-256: `06db9d8bdf71a60d46c0d76bf8119766f2c979bd548827237a9036af1752f4cd`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q47720.json)  
**Locator:** `/comments/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:46.048238+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_00047","source":"HAMAP-Rule"}],"value":"Cell wall biogenesis; peptidoglycan biosynthesis"}]}
```

Source SHA-256: `06db9d8bdf71a60d46c0d76bf8119766f2c979bd548827237a9036af1752f4cd`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q47720.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:46.048238+00:00.  

```json
{"citation":{"authors":["Park I.S.","Lin C.H.","Walsh C.T."],"citationCrossReferences":[{"database":"PubMed","id":"9294159"},{"database":"DOI","id":"10.1073/pnas.94.19.10040"}],"citationType":"journal article","firstPage":"10040","id":"9294159","journal":"Proc. Natl. Acad. Sci. U.S.A.","lastPage":"10044","publicationDate":"1997","title":"Bacterial resistance to vancomycin: overproduction, purification, and characterization of VanC2 from Enterococcus casseliflavus as a D-Ala-D-Ser ligase.","volume":"94"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceComments":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"9294159","source":"PubMed"}],"type":"STRAIN","value":"ATCC 25788"}],"referenceNumber":4,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","ACTIVITY REGULATION","SUBUNIT"]}
```

Source SHA-256: `06db9d8bdf71a60d46c0d76bf8119766f2c979bd548827237a9036af1752f4cd`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q47720.json)  
**Locator:** `/references/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:46.048238+00:00.  

```json
{"citation":{"authors":["Healy V.L.","Park I.S.","Walsh C.T."],"citationCrossReferences":[{"database":"PubMed","id":"9545431"},{"database":"DOI","id":"10.1016/s1074-5521(98)90633-0"}],"citationType":"journal article","firstPage":"197","id":"9545431","journal":"Chem. Biol.","lastPage":"207","publicationDate":"1998","title":"Active-site mutants of the VanC2 D-alanyl-D-serine ligase, characteristic of one vancomycin-resistant bacterial phenotype, revert towards wild-type D-alanyl-D-alanine ligases.","volume":"5"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":5,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","MUTAGENESIS OF PHE-250 AND ARG-322"]}
```

Source SHA-256: `06db9d8bdf71a60d46c0d76bf8119766f2c979bd548827237a9036af1752f4cd`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q47720?format=txt&versions=147)  
**Locator:** `lines 1-18`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 147 / 1.  
**Retrieved:** 2026-11-02T04:30:51.643943+00:00.  

```text
ID   VANC2_ENTCA             Reviewed;         350 AA.
AC   Q47720;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-NOV-1996, sequence version 1.
DT   28-JAN-2026, entry version 147.
DE   RecName: Full=Vancomycin C-type resistance protein VanC2 {ECO:0000303|PubMed:9294159, ECO:0000305};
DE            EC=6.3.2.35 {ECO:0000269|PubMed:9294159, ECO:0000269|PubMed:9545431};
DE   AltName: Full=D-alanine--D-serine ligase {ECO:0000255|HAMAP-Rule:MF_00047};
DE   AltName: Full=VanC2 ligase {ECO:0000305};
GN   Name=vanC2 {ECO:0000303|PubMed:9294159, ECO:0000303|PubMed:9545431,
GN   ECO:0000312|EMBL:ABX79432.1};
GN   Synonyms=ddl {ECO:0000255|HAMAP-Rule:MF_00047},
GN   vanC-2 {ECO:0000312|EMBL:AAA60990.1};
GN   ORFNames=P7I34_04740 {ECO:0000312|EMBL:MDT2981959.1};
OS   Enterococcus casseliflavus (Enterococcus flavescens).
OC   Bacteria; Bacillati; Bacillota; Bacilli; Lactobacillales; Enterococcaceae;
OC   Enterococcus.
OX   NCBI_TaxID=37734 {ECO:0000312|EMBL:AAA60990.1};
```

Source SHA-256: `7cd95341b40880e3967efdffddc7f3a25c7982d99fb2b3f1cf21db004390d78a`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q47720?format=txt&versions=147)  
**Locator:** `lines 42-51`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 147 / 1.  
**Retrieved:** 2026-11-02T04:30:51.643943+00:00.  

```text
RN   [4] {ECO:0000305}
RP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, ACTIVITY
RP   REGULATION, AND SUBUNIT.
RC   STRAIN=ATCC 25788 {ECO:0000303|PubMed:9294159};
RX   PubMed=9294159; DOI=10.1073/pnas.94.19.10040;
RA   Park I.S., Lin C.H., Walsh C.T.;
RT   "Bacterial resistance to vancomycin: overproduction, purification, and
RT   characterization of VanC2 from Enterococcus casseliflavus as a D-Ala-D-Ser
RT   ligase.";
RL   Proc. Natl. Acad. Sci. U.S.A. 94:10040-10044(1997).
```

Source SHA-256: `7cd95341b40880e3967efdffddc7f3a25c7982d99fb2b3f1cf21db004390d78a`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q47720?format=txt&versions=147)  
**Locator:** `lines 52-60`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 147 / 1.  
**Retrieved:** 2026-11-02T04:30:51.643943+00:00.  

```text
RN   [5] {ECO:0000305}
RP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND
RP   MUTAGENESIS OF PHE-250 AND ARG-322.
RX   PubMed=9545431; DOI=10.1016/s1074-5521(98)90633-0;
RA   Healy V.L., Park I.S., Walsh C.T.;
RT   "Active-site mutants of the VanC2 D-alanyl-D-serine ligase, characteristic
RT   of one vancomycin-resistant bacterial phenotype, revert towards wild-type
RT   D-alanyl-D-alanine ligases.";
RL   Chem. Biol. 5:197-207(1998).
```

Source SHA-256: `7cd95341b40880e3967efdffddc7f3a25c7982d99fb2b3f1cf21db004390d78a`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q47720?format=txt&versions=147)  
**Locator:** `lines 108-109`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 147 / 1.  
**Retrieved:** 2026-11-02T04:30:51.643943+00:00.  

```text
CC   -!- PATHWAY: Cell wall biogenesis; peptidoglycan biosynthesis.
CC       {ECO:0000255|HAMAP-Rule:MF_00047}.
```

Source SHA-256: `7cd95341b40880e3967efdffddc7f3a25c7982d99fb2b3f1cf21db004390d78a`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 153. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
