# EC_number_0177

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **D** — 5.3.3.21

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | invalid_review |

**Paired comparison:** not comparable: one or both reviews invalid or missing. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSGVTTVEYRGRVAVITICNERKLNALDLHGYYELSERMREVATHDEVYVTLLTAKGRFFSAGADVSTIRDPPTTGEDDSGIADGGRRQWLQSFVAFNLNITQAFYSHPKILVVGLNGPVVGLSAALVSFADFIYATPSTFLLTPFSSLGLVAEGGASRALVQRLGVSKANEALLMSRRVPADELLQTGFVNKVFTELKGAKDDDVRFKELVLAEIDDKLGDHLVGDSLIGIKELIRRPEIDVLEGQNAREVFAGLGRFMSGVPQREFLKLASGEKRHKL

[Multiple Choices]
A. 5.3.1.16
B. 3.1.26.3
C. 3.4.21.90
D. 5.3.3.21
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

> The exact sequence matches a UniProtKB/Swiss-Prot entry annotated as delta(3,5)-delta(2,4)-dienoyl-CoA isomerase, EC 5.3.3.21, supporting choice D. The catalytic-activity annotation is transferred from another UniProt entry; the supplied evidence does not establish a direct experimental assay of this exact protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone does not provide a concrete, reliable argument that distinguishes this specific dienoyl-CoA isomerase EC number from the alternatives. Identifying the protein family by sequence could guide a prediction, but the exact reaction classification is not established by the supplied context.


**Missing item-specific fact**

> The protein's identity/function as delta(3,5)-delta(2,4)-dienoyl-CoA isomerase, or a sufficiently informative homolog annotation linking it to EC 5.3.3.21.


**Reason**

> Choosing D depends on protein-specific functional information absent from the prompt, obtainable through annotation lookup or functional characterization rather than general reasoning from the sequence and choices alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched database annotation supports D; the evidence provided does not support another listed EC number as an alternative.


### Important caveats

- The database evidence supports the annotation but describes catalytic activity transferred from a related UniProt entry; direct experimental validation for this exact protein is not shown.
- The source snapshot used by the question author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone does not provide a concrete, reliable argument that distinguishes this specific dienoyl-CoA isomerase EC number from the alternatives. Identifying the protein family by sequence could guide a prediction, but the exact reaction classification is not established by the supplied context.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's identity/function as delta(3,5)-delta(2,4)-dienoyl-CoA isomerase, or a sufficiently informative homolog annotation linking it to EC 5.3.3.21.",
    "reason": "Choosing D depends on protein-specific functional information absent from the prompt, obtainable through annotation lookup or functional characterization rather than general reasoning from the sequence and choices alone."
  },
  "case_id": "EC_number_0177",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProtKB/Swiss-Prot entry annotated as delta(3,5)-delta(2,4)-dienoyl-CoA isomerase, EC 5.3.3.21, supporting choice D. The catalytic-activity annotation is transferred from another UniProt entry; the supplied evidence does not establish a direct experimental assay of this exact protein."
  },
  "important_caveats": [
    "The database evidence supports the annotation but describes catalytic activity transferred from a related UniProt entry; direct experimental validation for this exact protein is not shown.",
    "The source snapshot used by the question author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched database annotation supports D; the evidence provided does not support another listed EC number as an alternative."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0177",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProtKB/Swiss-Prot entry annotated as delta(3,5)-delta(2,4)-dienoyl-CoA isomerase, EC 5.3.3.21, supporting choice D. The catalytic-activity annotation is transferred from another UniProt entry; the supplied evidence does not establish a direct experimental assay of this exact protein.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone does not provide a concrete, reliable argument that distinguishes this specific dienoyl-CoA isomerase EC number from the alternatives. Identifying the protein family by sequence could guide a prediction, but the exact reaction classification is not established by the supplied context.",
    "missing_item_specific_fact": "The protein's identity/function as delta(3,5)-delta(2,4)-dienoyl-CoA isomerase, or a sufficiently informative homolog annotation linking it to EC 5.3.3.21.",
    "reason": "Choosing D depends on protein-specific functional information absent from the prompt, obtainable through annotation lookup or functional characterization rather than general reasoning from the sequence and choices alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched database annotation supports D; the evidence provided does not support another listed EC number as an alternative."
  },
  "important_caveats": [
    "The database evidence supports the annotation but describes catalytic activity transferred from a related UniProt entry; direct experimental validation for this exact protein is not shown.",
    "The source snapshot used by the question author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `invalid_review`.

**This result is not a valid structured review.** Any saved labels below remain the model’s original values; they are excluded from label distributions and paired agreement. No field or option ID has been repaired.

**Validation errors:** `question_ambiguity:invalid_option_ids`.

### Expected-answer support: supported

> UniProt entry G4NCP4 (DCI1_PYRO7, 280 AA, sequence SHA256 matches the benchmark input) annotates the recommended name as 'Delta(3,5)-Delta(2,4)-dienoyl-CoA isomerase' with EC 5.3.3.21. The EC assignment carries evidence code ECO:0000305 (inferred by curator) citing PubMed 36774535, and the catalytic-activity comment cites ECO:0000250 (similarity to Q08558) with Rhea:RHEA:45240. The annotation is well-supported by sequence similarity to a characterized homolog and a 2023 functional study, though it is not direct experimental evidence on this exact protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4), [H1](#evidence-h1).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Options B (3.1.26.3, endoribonuclease) and C (3.4.21.90, serine endopeptidase) can be eliminated by general reasoning: the 280-residue sequence lacks a Ser-His-Asp catalytic triad, no RNase A-like catalytic His/Lys cluster, and no ribonuclease-fold motifs. However, distinguishing the two remaining isomerase choices—5.3.1.16 (intramolecular oxidoreductase, aldose-ketose type) from 5.3.3.21 (intramolecular oxidoreductase, transposing C=C bonds in dienoyl-CoA)—requires knowledge of the specific enoyl-CoA isomerase superfamily membership and the substrate class (dienoyl-CoA vs. sugar phosphate). No canonical, widely-recognized catalytic motif in the supplied sequence allows a model to assign the precise EC subclass 5.3.3 vs 5.3.1, let alone the terminal digit .21.


**Missing item-specific fact**

> The specific assignment of this Pyricularia oryzae protein to EC 5.3.3.21 (Delta(3,5)-Delta(2,4)-dienoyl-CoA isomerase) rests on sequence similarity to the characterized yeast homolog Q08558 and a 2023 functional study (PubMed 36774535). Without access to that annotation or prior knowledge of the DCI1/enoyl-CoA isomerase family, a model cannot derive the exact EC number from the raw sequence alone.


**Reason**

> Eliminating hydrolase options (B, C) is feasible by general reasoning, but the critical discrimination between the two isomerase options (A vs D) depends on recognizing the protein as a member of the enoyl-CoA isomerase family and knowing the specific EC subclass and number, which is an item-specific database annotation rather than a derivable sequence feature.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A (5.3.1.16)",
  "D (5.3.3.21)"
]
```

> Both A and D belong to EC class 5 (isomerases) subclass 5.3 (intramolecular oxidoreductases). From the raw 280-aa sequence alone, without the specific family annotation, a model cannot confidently distinguish the 5.3.1 (aldose-ketose isomerase) from the 5.3.3 (transposing C=C bonds) sub-subclass, making both A and D superficially defensible. The correct answer D is established only through database annotation and similarity-based inference.


### Important caveats

- The EC 5.3.3.21 annotation is based on similarity (ECO:0000250) to Q08558 and curator inference (ECO:0000305), not on direct experimental kinetics of this specific Pyricularia protein.
- EC 5.3.3.21 is a recently assigned, relatively obscure EC number (first public date 2025-06-18 for this entry), making it unlikely to be in standard textbook training data.
- The reviewer-only UniProt accession and annotation were absent from the evaluated model input; the model sees only the 280-aa sequence and four EC-number choices.
- Option A (5.3.1.16) may correspond to an obscure or possibly non-existent EC entry, which could serve as a weak distractor, but a model cannot verify EC-number validity from the question alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Options B (3.1.26.3, endoribonuclease) and C (3.4.21.90, serine endopeptidase) can be eliminated by general reasoning: the 280-residue sequence lacks a Ser-His-Asp catalytic triad, no RNase A-like catalytic His/Lys cluster, and no ribonuclease-fold motifs. However, distinguishing the two remaining isomerase choices—5.3.1.16 (intramolecular oxidoreductase, aldose-ketose type) from 5.3.3.21 (intramolecular oxidoreductase, transposing C=C bonds in dienoyl-CoA)—requires knowledge of the specific enoyl-CoA isomerase superfamily membership and the substrate class (dienoyl-CoA vs. sugar phosphate). No canonical, widely-recognized catalytic motif in the supplied sequence allows a model to assign the precise EC subclass 5.3.3 vs 5.3.1, let alone the terminal digit .21.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific assignment of this Pyricularia oryzae protein to EC 5.3.3.21 (Delta(3,5)-Delta(2,4)-dienoyl-CoA isomerase) rests on sequence similarity to the characterized yeast homolog Q08558 and a 2023 functional study (PubMed 36774535). Without access to that annotation or prior knowledge of the DCI1/enoyl-CoA isomerase family, a model cannot derive the exact EC number from the raw sequence alone.",
    "reason": "Eliminating hydrolase options (B, C) is feasible by general reasoning, but the critical discrimination between the two isomerase options (A vs D) depends on recognizing the protein as a member of the enoyl-CoA isomerase family and knowing the specific EC subclass and number, which is an item-specific database annotation rather than a derivable sequence feature."
  },
  "case_id": "EC_number_0177",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4",
      "H1"
    ],
    "judgment": "supported",
    "reason": "UniProt entry G4NCP4 (DCI1_PYRO7, 280 AA, sequence SHA256 matches the benchmark input) annotates the recommended name as 'Delta(3,5)-Delta(2,4)-dienoyl-CoA isomerase' with EC 5.3.3.21. The EC assignment carries evidence code ECO:0000305 (inferred by curator) citing PubMed 36774535, and the catalytic-activity comment cites ECO:0000250 (similarity to Q08558) with Rhea:RHEA:45240. The annotation is well-supported by sequence similarity to a characterized homolog and a 2023 functional study, though it is not direct experimental evidence on this exact protein."
  },
  "important_caveats": [
    "The EC 5.3.3.21 annotation is based on similarity (ECO:0000250) to Q08558 and curator inference (ECO:0000305), not on direct experimental kinetics of this specific Pyricularia protein.",
    "EC 5.3.3.21 is a recently assigned, relatively obscure EC number (first public date 2025-06-18 for this entry), making it unlikely to be in standard textbook training data.",
    "The reviewer-only UniProt accession and annotation were absent from the evaluated model input; the model sees only the 280-aa sequence and four EC-number choices.",
    "Option A (5.3.1.16) may correspond to an obscure or possibly non-existent EC entry, which could serve as a weak distractor, but a model cannot verify EC-number validity from the question alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A (5.3.1.16)",
      "D (5.3.3.21)"
    ],
    "reason": "Both A and D belong to EC class 5 (isomerases) subclass 5.3 (intramolecular oxidoreductases). From the raw 280-aa sequence alone, without the specific family annotation, a model cannot confidently distinguish the 5.3.1 (aldose-ketose isomerase) from the 5.3.3 (transposing C=C bonds) sub-subclass, making both A and D superficially defensible. The correct answer D is established only through database annotation and similarity-based inference."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0177",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry G4NCP4 (DCI1_PYRO7, 280 AA, sequence SHA256 matches the benchmark input) annotates the recommended name as 'Delta(3,5)-Delta(2,4)-dienoyl-CoA isomerase' with EC 5.3.3.21. The EC assignment carries evidence code ECO:0000305 (inferred by curator) citing PubMed 36774535, and the catalytic-activity comment cites ECO:0000250 (similarity to Q08558) with Rhea:RHEA:45240. The annotation is well-supported by sequence similarity to a characterized homolog and a 2023 functional study, though it is not direct experimental evidence on this exact protein.",
    "evidence_ids": ["C4", "C5", "H2", "H4", "H1"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Options B (3.1.26.3, endoribonuclease) and C (3.4.21.90, serine endopeptidase) can be eliminated by general reasoning: the 280-residue sequence lacks a Ser-His-Asp catalytic triad, no RNase A-like catalytic His/Lys cluster, and no ribonuclease-fold motifs. However, distinguishing the two remaining isomerase choices—5.3.1.16 (intramolecular oxidoreductase, aldose-ketose type) from 5.3.3.21 (intramolecular oxidoreductase, transposing C=C bonds in dienoyl-CoA)—requires knowledge of the specific enoyl-CoA isomerase superfamily membership and the substrate class (dienoyl-CoA vs. sugar phosphate). No canonical, widely-recognized catalytic motif in the supplied sequence allows a model to assign the precise EC subclass 5.3.3 vs 5.3.1, let alone the terminal digit .21.",
    "missing_item_specific_fact": "The specific assignment of this Pyricularia oryzae protein to EC 5.3.3.21 (Delta(3,5)-Delta(2,4)-dienoyl-CoA isomerase) rests on sequence similarity to the characterized yeast homolog Q08558 and a 2023 functional study (PubMed 36774535). Without access to that annotation or prior knowledge of the DCI1/enoyl-CoA isomerase family, a model cannot derive the exact EC number from the raw sequence alone.",
    "reason": "Eliminating hydrolase options (B, C) is feasible by general reasoning, but the critical discrimination between the two isomerase options (A vs D) depends on recognizing the protein as a member of the enoyl-CoA isomerase family and knowing the specific EC subclass and number, which is an item-specific database annotation rather than a derivable sequence feature."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A (5.3.1.16)", "D (5.3.3.21)"],
    "reason": "Both A and D belong to EC class 5 (isomerases) subclass 5.3 (intramolecular oxidoreductases). From the raw 280-aa sequence alone, without the specific family annotation, a model cannot confidently distinguish the 5.3.1 (aldose-ketose isomerase) from the 5.3.3 (transposing C=C bonds) sub-subclass, making both A and D superficially defensible. The correct answer D is established only through database annotation and similarity-based inference."
  },
  "important_caveats": [
    "The EC 5.3.3.21 annotation is based on similarity (ECO:0000250) to Q08558 and curator inference (ECO:0000305), not on direct experimental kinetics of this specific Pyricularia protein.",
    "EC 5.3.3.21 is a recently assigned, relatively obscure EC number (first public date 2025-06-18 for this entry), making it unlikely to be in standard textbook training data.",
    "The reviewer-only UniProt accession and annotation were absent from the evaluated model input; the model sees only the 280-aa sequence and four EC-number choices.",
    "Option A (5.3.1.16) may correspond to an obscure or possibly non-existent EC entry, which could serve as a weak distractor, but a model cannot verify EC-number validity from the question alone."
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

**Accession:** `G4NCP4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 50. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NCP4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:09.351845+00:00.  

```json
"G4NCP4"
```

Source SHA-256: `18e48cf8abf1a98581d94e658f5c733af10a67b9ab523abb9b4c1242569dd85d`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NCP4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:09.351845+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q08558","source":"UniProtKB"}],"value":"Peroxisomal di-isomerase DCI1"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"36774535","source":"PubMed"}],"value":"5.3.3.21"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"36774535","source":"PubMed"}],"value":"Delta(3,5)-Delta(2,4)-dienoyl-CoA isomerase"}}}
```

Source SHA-256: `18e48cf8abf1a98581d94e658f5c733af10a67b9ab523abb9b4c1242569dd85d`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NCP4.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:09.351845+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"Q08558","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:45241"}}],"reaction":{"ecNumber":"5.3.3.21","evidences":[{"evidenceCode":"ECO:0000250","id":"Q08558","source":"UniProtKB"}],"name":"a (3E,5Z)-dienoyl-CoA = a (2E,4E)-(5,6-saturated)-dienoyl-CoA","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:45240"},{"database":"ChEBI","id":"CHEBI:85110"},{"database":"ChEBI","id":"CHEBI:85111"}]}}
```

Source SHA-256: `18e48cf8abf1a98581d94e658f5c733af10a67b9ab523abb9b4c1242569dd85d`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4NCP4?format=txt&versions=50)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 50 / 1.  
**Retrieved:** 2026-11-01T06:28:06.213875+00:00.  

```text
ID   DCI1_PYRO7              Reviewed;         280 AA.
AC   G4NCP4;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   14-DEC-2011, sequence version 1.
DT   28-JAN-2026, entry version 50.
DE   RecName: Full=Delta(3,5)-Delta(2,4)-dienoyl-CoA isomerase {ECO:0000303|PubMed:36774535};
DE            EC=5.3.3.21 {ECO:0000305|PubMed:36774535};
DE   AltName: Full=Peroxisomal di-isomerase DCI1 {ECO:0000250|UniProtKB:Q08558};
GN   Name=DCI1 {ECO:0000303|PubMed:36774535}; ORFNames=MGG_00359;
OS   Pyricularia oryzae (strain 70-15 / ATCC MYA-4617 / FGSC 8958) (Rice blast
OS   fungus) (Magnaporthe oryzae).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;
OC   Sordariomycetidae; Magnaporthales; Pyriculariaceae; Pyricularia.
OX   NCBI_TaxID=242507;
```

Source SHA-256: `b3af8253bb3b622f3d6088c53ac0e4fee82efbfd91d58cde994f260c9162d6d7`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4NCP4?format=txt&versions=50)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 50 / 1.  
**Retrieved:** 2026-11-01T06:28:06.213875+00:00.  

```text
DE   RecName: Full=Delta(3,5)-Delta(2,4)-dienoyl-CoA isomerase {ECO:0000303|PubMed:36774535};
DE            EC=5.3.3.21 {ECO:0000305|PubMed:36774535};
DE   AltName: Full=Peroxisomal di-isomerase DCI1 {ECO:0000250|UniProtKB:Q08558};
```

Source SHA-256: `b3af8253bb3b622f3d6088c53ac0e4fee82efbfd91d58cde994f260c9162d6d7`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4NCP4?format=txt&versions=50)  
**Locator:** `lines 41-46`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 50 / 1.  
**Retrieved:** 2026-11-01T06:28:06.213875+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=a (3E,5Z)-dienoyl-CoA = a (2E,4E)-(5,6-saturated)-dienoyl-CoA;
CC         Xref=Rhea:RHEA:45240, ChEBI:CHEBI:85110, ChEBI:CHEBI:85111;
CC         EC=5.3.3.21; Evidence={ECO:0000250|UniProtKB:Q08558};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:45241;
CC         Evidence={ECO:0000250|UniProtKB:Q08558};
```

Source SHA-256: `b3af8253bb3b622f3d6088c53ac0e4fee82efbfd91d58cde994f260c9162d6d7`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 177. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
