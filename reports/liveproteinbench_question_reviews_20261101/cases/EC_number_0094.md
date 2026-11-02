# EC_number_0094

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **C** — 2.4.2.14

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MCGVLALILANQSSSAANDLHEALYVLQHRGQDAAGIATSTSSGHIHIRKKNGMAADVFQSGARLANLFGSMGIAHLRYPTAGGSANTEAQPFYVNSPYGICFAHNGNLINTVELRRYLDFEIHRHINSDSDSELMLNIFADELSETKKARVNTEDIFNGLSKMYQRCEGAWACTAMLAGFGVIGFRDAYGIRPLVMGSRPSSDGDGLDYMIASESIALDRLGFTNVRDIQPGEAVIVAKGAEPVFCQVAPRKSYTPDLFEYVYFARPDSVIDGISVYQSRQRMGRYLAARLLEVLGPEGIKEIDVVIPVPETSSPAAASVAHALNKPYCAGYIRNPYVFRTFIMPGQATRQKGVRRKLSAVKEEFKNRTILLVDDSIARGTTSREAISMAREAGVKKIIAACCSPEITYPHIYGIDLPSPHEMVAYERDNNDIAQNLGADRIVYQTLEDLQASCAEIARENDFQEPHTFENGVFSGQYVTPVPEGYFALLEKIRGTGRKEALDKSSKRL

[Multiple Choices]
A. 2.4.1.392
B. 1.14.15.37
C. 2.4.2.14
D. 4.4.1.11
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

> The exact sequence matches a UniProt entry annotated as phosphoribosylpyrophosphate amidotransferase FrzK, EC 2.4.2.14. The annotation cites experimental evidence, and the catalytic-activity annotation specifies the corresponding reaction.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a glutamine amidotransferase domain (including an N-terminal catalytic cysteine) coupled to a phosphoribosyltransferase domain. That combination supports a glutamine-dependent phosphoribosyl transfer reaction and distinguishes choice C from the unrelated oxidoreductase and lyase options and the other glycosyltransferase option.


**Missing item-specific fact**

> No essential item-specific fact is needed to distinguish these choices by the sequence-based functional inference, although direct reaction evidence would be needed to confirm the exact EC annotation independently.


**Reason**

> The sequence provides a concrete domain and catalytic-residue basis for inferring the enzyme class and selecting the matching listed EC number; this is more than remembering a database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence features support the phosphoribosyl amidotransferase option, while the other choices describe different enzyme classes.


### Important caveats

- The supporting UniProt annotations are reviewer-only and were not part of the original input.
- The matched database annotation cites experimental evidence, but the primary paper was not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a glutamine amidotransferase domain (including an N-terminal catalytic cysteine) coupled to a phosphoribosyltransferase domain. That combination supports a glutamine-dependent phosphoribosyl transfer reaction and distinguishes choice C from the unrelated oxidoreductase and lyase options and the other glycosyltransferase option.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No essential item-specific fact is needed to distinguish these choices by the sequence-based functional inference, although direct reaction evidence would be needed to confirm the exact EC annotation independently.",
    "reason": "The sequence provides a concrete domain and catalytic-residue basis for inferring the enzyme class and selecting the matching listed EC number; this is more than remembering a database entry."
  },
  "case_id": "EC_number_0094",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as phosphoribosylpyrophosphate amidotransferase FrzK, EC 2.4.2.14. The annotation cites experimental evidence, and the catalytic-activity annotation specifies the corresponding reaction."
  },
  "important_caveats": [
    "The supporting UniProt annotations are reviewer-only and were not part of the original input.",
    "The matched database annotation cites experimental evidence, but the primary paper was not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence features support the phosphoribosyl amidotransferase option, while the other choices describe different enzyme classes."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0094",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as phosphoribosylpyrophosphate amidotransferase FrzK, EC 2.4.2.14. The annotation cites experimental evidence, and the catalytic-activity annotation specifies the corresponding reaction.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a glutamine amidotransferase domain (including an N-terminal catalytic cysteine) coupled to a phosphoribosyltransferase domain. That combination supports a glutamine-dependent phosphoribosyl transfer reaction and distinguishes choice C from the unrelated oxidoreductase and lyase options and the other glycosyltransferase option.",
    "missing_item_specific_fact": "No essential item-specific fact is needed to distinguish these choices by the sequence-based functional inference, although direct reaction evidence would be needed to confirm the exact EC annotation independently.",
    "reason": "The sequence provides a concrete domain and catalytic-residue basis for inferring the enzyme class and selecting the matching listed EC number; this is more than remembering a database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence features support the phosphoribosyl amidotransferase option, while the other choices describe different enzyme classes."
  },
  "important_caveats": [
    "The supporting UniProt annotations are reviewer-only and were not part of the original input.",
    "The matched database annotation cites experimental evidence, but the primary paper was not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A7T8J1U7 (FRZK_CLASX) annotates this 510-aa protein with EC 2.4.2.14 (phosphoribosylpyrophosphate amidotransferase FrzK), supported by experimental evidence (ECO:0000269, PubMed:33372776, JACS 2021). The catalytic reaction (5-phospho-beta-D-ribosylamine + L-glutamate + diphosphate = 5-phospho-alpha-D-ribose 1-diphosphate + L-glutamine + H2O) confirms the EC assignment. Sequence match is exact in both current (v18) and historical (v16) records.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal region contains a recognizable class I glutamine amidotransferase (GAT) catalytic triad motif (Cys in 'CFAH', His in 'IHRH', Asp in 'FADE'), and the C-terminal region displays the conserved PRPP-binding motif 'GIDLPSPHE' characteristic of phosphoribosylpyrophosphate amidotransferases. These features identify the enzyme as an EC 2.4.2.x amidotransferase. The other options belong to entirely different EC classes: 2.4.1.392 (O-glycosyltransferase, no GT-A/GT-B fold features present), 1.14.15.37 (copper monooxygenase, no type-1/type-2 copper His clusters), and 4.4.1.11 (PLP-dependent cystathionine gamma-lyase, no PLP-binding lysine motif). Since C is the only option in the 2.4.2.x family, recognizing the amidotransferase fold is sufficient to select it.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The glutamine amidotransferase catalytic triad (Cys-His-Asp) and the PRPP-binding 'GIDLPSPHE' motif are well-established enzyme-architecture signatures in biochemistry. A model with general enzyme-structure knowledge can identify the fold and eliminate the three options from unrelated EC classes. The specificity of 2.4.2.14 versus other 2.4.2.x sub-numbers is not tested here because no other 2.4.2.x option is offered.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractors (glycosyltransferase, copper monooxygenase, PLP-dependent lyase) lack any sequence features consistent with their assigned EC classes for this protein. Only EC 2.4.2.14 matches the observed amidotransferase fold and PRPP-binding domain.


### Important caveats

- The protein is a specialized variant (FrzK) of PRPP amidotransferase involved in FR901483 biosynthesis rather than canonical de novo purine biosynthesis; however, the EC number and fold are identical to the canonical enzyme.
- Recognition of the GAT catalytic triad from linear sequence requires familiarity with the fold architecture; the residues are brought together by tertiary structure, not a simple linear motif.
- The UniProt annotation carries experimental evidence (ECO:0000269) from the 2021 JACS paper, lending strong support to the EC assignment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal region contains a recognizable class I glutamine amidotransferase (GAT) catalytic triad motif (Cys in 'CFAH', His in 'IHRH', Asp in 'FADE'), and the C-terminal region displays the conserved PRPP-binding motif 'GIDLPSPHE' characteristic of phosphoribosylpyrophosphate amidotransferases. These features identify the enzyme as an EC 2.4.2.x amidotransferase. The other options belong to entirely different EC classes: 2.4.1.392 (O-glycosyltransferase, no GT-A/GT-B fold features present), 1.14.15.37 (copper monooxygenase, no type-1/type-2 copper His clusters), and 4.4.1.11 (PLP-dependent cystathionine gamma-lyase, no PLP-binding lysine motif). Since C is the only option in the 2.4.2.x family, recognizing the amidotransferase fold is sufficient to select it.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The glutamine amidotransferase catalytic triad (Cys-His-Asp) and the PRPP-binding 'GIDLPSPHE' motif are well-established enzyme-architecture signatures in biochemistry. A model with general enzyme-structure knowledge can identify the fold and eliminate the three options from unrelated EC classes. The specificity of 2.4.2.14 versus other 2.4.2.x sub-numbers is not tested here because no other 2.4.2.x option is offered."
  },
  "case_id": "EC_number_0094",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A7T8J1U7 (FRZK_CLASX) annotates this 510-aa protein with EC 2.4.2.14 (phosphoribosylpyrophosphate amidotransferase FrzK), supported by experimental evidence (ECO:0000269, PubMed:33372776, JACS 2021). The catalytic reaction (5-phospho-beta-D-ribosylamine + L-glutamate + diphosphate = 5-phospho-alpha-D-ribose 1-diphosphate + L-glutamine + H2O) confirms the EC assignment. Sequence match is exact in both current (v18) and historical (v16) records."
  },
  "important_caveats": [
    "The protein is a specialized variant (FrzK) of PRPP amidotransferase involved in FR901483 biosynthesis rather than canonical de novo purine biosynthesis; however, the EC number and fold are identical to the canonical enzyme.",
    "Recognition of the GAT catalytic triad from linear sequence requires familiarity with the fold architecture; the residues are brought together by tertiary structure, not a simple linear motif.",
    "The UniProt annotation carries experimental evidence (ECO:0000269) from the 2021 JACS paper, lending strong support to the EC assignment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (glycosyltransferase, copper monooxygenase, PLP-dependent lyase) lack any sequence features consistent with their assigned EC classes for this protein. Only EC 2.4.2.14 matches the observed amidotransferase fold and PRPP-binding domain."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0094",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A7T8J1U7 (FRZK_CLASX) annotates this 510-aa protein with EC 2.4.2.14 (phosphoribosylpyrophosphate amidotransferase FrzK), supported by experimental evidence (ECO:0000269, PubMed:33372776, JACS 2021). The catalytic reaction (5-phospho-beta-D-ribosylamine + L-glutamate + diphosphate = 5-phospho-alpha-D-ribose 1-diphosphate + L-glutamine + H2O) confirms the EC assignment. Sequence match is exact in both current (v18) and historical (v16) records.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal region contains a recognizable class I glutamine amidotransferase (GAT) catalytic triad motif (Cys in 'CFAH', His in 'IHRH', Asp in 'FADE'), and the C-terminal region displays the conserved PRPP-binding motif 'GIDLPSPHE' characteristic of phosphoribosylpyrophosphate amidotransferases. These features identify the enzyme as an EC 2.4.2.x amidotransferase. The other options belong to entirely different EC classes: 2.4.1.392 (O-glycosyltransferase, no GT-A/GT-B fold features present), 1.14.15.37 (copper monooxygenase, no type-1/type-2 copper His clusters), and 4.4.1.11 (PLP-dependent cystathionine gamma-lyase, no PLP-binding lysine motif). Since C is the only option in the 2.4.2.x family, recognizing the amidotransferase fold is sufficient to select it.",
    "missing_item_specific_fact": "",
    "reason": "The glutamine amidotransferase catalytic triad (Cys-His-Asp) and the PRPP-binding 'GIDLPSPHE' motif are well-established enzyme-architecture signatures in biochemistry. A model with general enzyme-structure knowledge can identify the fold and eliminate the three options from unrelated EC classes. The specificity of 2.4.2.14 versus other 2.4.2.x sub-numbers is not tested here because no other 2.4.2.x option is offered."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (glycosyltransferase, copper monooxygenase, PLP-dependent lyase) lack any sequence features consistent with their assigned EC classes for this protein. Only EC 2.4.2.14 matches the observed amidotransferase fold and PRPP-binding domain."
  },
  "important_caveats": [
    "The protein is a specialized variant (FrzK) of PRPP amidotransferase involved in FR901483 biosynthesis rather than canonical de novo purine biosynthesis; however, the EC number and fold are identical to the canonical enzyme.",
    "Recognition of the GAT catalytic triad from linear sequence requires familiarity with the fold architecture; the residues are brought together by tertiary structure, not a simple linear motif.",
    "The UniProt annotation carries experimental evidence (ECO:0000269) from the 2021 JACS paper, lending strong support to the EC assignment."
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

**Accession:** `A0A7T8J1U7` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 16. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:51.826168+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33372776","source":"PubMed"}],"value":"FR901483 biosynthesis clusters protein K"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33372776","source":"PubMed"}],"value":"Glutamine phosphoribosylpyrophosphate amidotransferase"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"33372776","source":"PubMed"}],"value":"2.4.2.14"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33372776","source":"PubMed"}],"value":"Phosphoribosylpyrophosphate amidotransferase FrzK"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"33372776","source":"PubMed"}],"value":"ATase FrzK"}]}}
```

Source SHA-256: `56665e1cd9e3380e3faeac05a356479129623641a0ef275c9308eeccf948063d`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:51.826168+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"right-to-left","evidences":[{"evidenceCode":"ECO:0000305","id":"33372776","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:14907"}}],"reaction":{"ecNumber":"2.4.2.14","evidences":[{"evidenceCode":"ECO:0000305","id":"33372776","source":"PubMed"}],"name":"5-phospho-beta-D-ribosylamine + L-glutamate + diphosphate = 5-phospho-alpha-D-ribose 1-diphosphate + L-glutamine + H2O","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:14905"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:29985"},{"database":"ChEBI","id":"CHEBI:33019"},{"database":"ChEBI","id":"CHEBI:58017"},{"database":"ChEBI","id":"CHEBI:58359"},{"database":"ChEBI","id":"CHEBI:58681"}]}}
```

Source SHA-256: `56665e1cd9e3380e3faeac05a356479129623641a0ef275c9308eeccf948063d`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:51.826168+00:00.  

```json
{"citation":{"authors":["Zhang Z.","Tamura Y.","Tang M.","Qiao T.","Sato M.","Otsu Y.","Sasamura S.","Taniguchi M.","Watanabe K.","Tang Y."],"citationCrossReferences":[{"database":"PubMed","id":"33372776"},{"database":"DOI","id":"10.1021/jacs.0c12352"}],"citationType":"journal article","firstPage":"132","id":"33372776","journal":"J. Am. Chem. Soc.","lastPage":"136","publicationDate":"2021","title":"Biosynthesis of the Immunosuppressant (-)-FR901483.","volume":"143"},"referenceComments":[{"type":"STRAIN","value":"11231"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","FUNCTION"]}
```

Source SHA-256: `56665e1cd9e3380e3faeac05a356479129623641a0ef275c9308eeccf948063d`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8J1U7?format=txt&versions=16)  
**Locator:** `lines 6-10`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 16 / 1.  
**Retrieved:** 2026-11-02T04:25:55.036238+00:00.  

```text
DE   RecName: Full=Phosphoribosylpyrophosphate amidotransferase FrzK {ECO:0000303|PubMed:33372776};
DE            Short=ATase FrzK {ECO:0000303|PubMed:33372776};
DE            EC=2.4.2.14 {ECO:0000269|PubMed:33372776};
DE   AltName: Full=FR901483 biosynthesis clusters protein K {ECO:0000303|PubMed:33372776};
DE   AltName: Full=Glutamine phosphoribosylpyrophosphate amidotransferase {ECO:0000303|PubMed:33372776};
```

Source SHA-256: `578ee5dbb88bc40f60a644a1dc0fae09acdb5d05f79fe55109621fabea2329a5`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8J1U7?format=txt&versions=16)  
**Locator:** `lines 35-43`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 16 / 1.  
**Retrieved:** 2026-11-02T04:25:55.036238+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=5-phospho-beta-D-ribosylamine + L-glutamate + diphosphate = 5-
CC         phospho-alpha-D-ribose 1-diphosphate + L-glutamine + H2O;
CC         Xref=Rhea:RHEA:14905, ChEBI:CHEBI:15377, ChEBI:CHEBI:29985,
CC         ChEBI:CHEBI:33019, ChEBI:CHEBI:58017, ChEBI:CHEBI:58359,
CC         ChEBI:CHEBI:58681; EC=2.4.2.14;
CC         Evidence={ECO:0000305|PubMed:33372776};
CC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:14907;
CC         Evidence={ECO:0000305|PubMed:33372776};
```

Source SHA-256: `578ee5dbb88bc40f60a644a1dc0fae09acdb5d05f79fe55109621fabea2329a5`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 94. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
