# EC_number_0096

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **A** — 3.2.1.8

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MVSFTTLLAGFVAVTGVLSAPTETVEVVDVEKRQTIGPGTGFNNGYYYSYWNDGHSGVTYTNGAGGSFSVNWANSGNFVGGKGWNPGSSSRVINFSGSYNPNGNSYLSVYGWSKNPLIEYYIVENFGTYNPSTGTTKLGEVTSDGSVYDIYRTQRVNQPSIIGTATFYQYWSVRRNHAPAARSRLRTTSNAWRNLGLTLGTLDYQIIAVEGYFSSGNANINVS

[Multiple Choices]
A. 3.2.1.8
B. 3.2.1.20
C. 1.1.1.1
D. 5.1.1.25
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

> The sequence matches the UniProt entry for this protein. Its catalytic activity is annotated as endohydrolysis of beta-D-xylosidic linkages in xylans, corresponding to EC 3.2.1.8; the annotation cites experimental evidence. The annotation supports choice A, though the evidence excerpt does not independently reproduce the primary study.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has a secretion signal and features compatible with a fungal carbohydrate-active enzyme, but those broad clues do not establish xylan as the substrate or distinguish EC 3.2.1.8 from another glycosidase such as choice B.


**Missing item-specific fact**

> The protein's specific xylan-hydrolysis activity, established by a protein-specific annotation or experiment, is needed to select EC 3.2.1.8.


**Reason**

> The supplied sequence and choices alone do not provide a sufficiently specific substrate or reaction clue. The supporting catalytic-activity annotation is reviewer-only, not information supplied to the evaluated model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer-only sequence-matched catalytic-activity evidence supports choice A; no other listed EC is supported by the supplied evidence.


### Important caveats

- The current and archived database annotations match the supplied sequence, but the author's exact source snapshot is unknown.
- The EC annotation includes a computational ProRule basis, while the catalytic-activity annotation cites experimental evidence; these evidence types should not be conflated.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a secretion signal and features compatible with a fungal carbohydrate-active enzyme, but those broad clues do not establish xylan as the substrate or distinguish EC 3.2.1.8 from another glycosidase such as choice B.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's specific xylan-hydrolysis activity, established by a protein-specific annotation or experiment, is needed to select EC 3.2.1.8.",
    "reason": "The supplied sequence and choices alone do not provide a sufficiently specific substrate or reaction clue. The supporting catalytic-activity annotation is reviewer-only, not information supplied to the evaluated model."
  },
  "case_id": "EC_number_0096",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry for this protein. Its catalytic activity is annotated as endohydrolysis of beta-D-xylosidic linkages in xylans, corresponding to EC 3.2.1.8; the annotation cites experimental evidence. The annotation supports choice A, though the evidence excerpt does not independently reproduce the primary study."
  },
  "important_caveats": [
    "The current and archived database annotations match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The EC annotation includes a computational ProRule basis, while the catalytic-activity annotation cites experimental evidence; these evidence types should not be conflated."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only sequence-matched catalytic-activity evidence supports choice A; no other listed EC is supported by the supplied evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0096",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry for this protein. Its catalytic activity is annotated as endohydrolysis of beta-D-xylosidic linkages in xylans, corresponding to EC 3.2.1.8; the annotation cites experimental evidence. The annotation supports choice A, though the evidence excerpt does not independently reproduce the primary study.",
    "evidence_ids": ["C1", "C5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has a secretion signal and features compatible with a fungal carbohydrate-active enzyme, but those broad clues do not establish xylan as the substrate or distinguish EC 3.2.1.8 from another glycosidase such as choice B.",
    "missing_item_specific_fact": "The protein's specific xylan-hydrolysis activity, established by a protein-specific annotation or experiment, is needed to select EC 3.2.1.8.",
    "reason": "The supplied sequence and choices alone do not provide a sufficiently specific substrate or reaction clue. The supporting catalytic-activity annotation is reviewer-only, not information supplied to the evaluated model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only sequence-matched catalytic-activity evidence supports choice A; no other listed EC is supported by the supplied evidence."
  },
  "important_caveats": [
    "The current and archived database annotations match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The EC annotation includes a computational ProRule basis, while the catalytic-activity annotation cites experimental evidence; these evidence types should not be conflated."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProtKB entry Q9UVF9 (EIX_HYPRU) is annotated with EC 3.2.1.8 (endo-1,4-beta-xylanase). The EC assignment carries both a computational evidence code (ECO:0000255, PROSITE-ProRule PRU01097) and experimental confirmation (ECO:0000269, PubMed:16668223 — product characterization demonstrating endohydrolysis of (1→4)-β-D-xylosidic linkages in xylans). Multiple independent publications (PubMed 10517825, 16666504, 16668223) confirm xylanase activity. The benchmark sequence matches the UniProt entry exactly (SHA256 match confirmed).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H2](#evidence-h2), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The mature protein is approximately 185 amino acids (223 total minus ~38-residue signal peptide). This size is characteristic of GH11 endo-xylanases (~180–220 aa) but grossly inconsistent with EC 3.2.1.20 alpha-amylase (GH13), which is typically 400–500 residues. Options C (EC 1.1.1.1, alcohol dehydrogenase, oxidoreductase) and D (EC 5.1.1.25, amino acid racemase, isomerase) belong to entirely different EC classes and lack the hallmarks of glycoside hydrolases (e.g., no Rossmann-like NAD-binding motif for dehydrogenases, no PLP-binding residues for racemases). The small secreted fungal protein with a β-jelly-roll-like compact architecture and catalytic glutamate residues in a GPGTGFNNGYYYSY-type motif is consistent with GH11 xylanase rather than the large (β/α)₈ TIM-barrel alpha-amylase.


**Missing item-specific fact**

> Precise recognition of GH11-specific PROSITE-ProRule motifs (PRU01097) to confirm family assignment beyond the size-based elimination; however, the size argument alone provides a defensible biological distinction between GH11 xylanase and GH13 alpha-amylase.


**Reason**

> A model can eliminate C and D by recognizing the absence of oxidoreductase or isomerase catalytic machinery. Between A and B, the ~185-aa mature size is a strong biological discriminator: EC 3.2.1.20 alpha-amylases are consistently >400 aa, while GH11 xylanases are ~200 aa. This constitutes a concrete structural/biological argument rather than pure database lookup, though full family confirmation would benefit from motif-level pattern matching.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The size-based argument cleanly separates A (GH11 xylanase, ~185 aa) from B (GH13 alpha-amylase, ~450 aa). C and D are eliminated by EC class. No ambiguity in the correct answer.


### Important caveats

- The EC number assignment in UniProt carries a PROSITE-ProRule computational evidence code (ECO:0000255) for the EC field itself, but the catalytic activity comment is backed by experimental evidence (ECO:0000269, PubMed:16668223).
- The protein also functions as an elicitor (ethylene-inducing xylanase, EIX) with elicitation activity separable from xylanase activity (PubMed 10517825), but the EC number reflects the catalytic xylanase function.
- The size-based reasoning is robust for typical alpha-amylases but a model would need to be aware that no known EC 3.2.1.20 enzyme is as small as 185 aa.
- All reviewer-only evidence was absent from the evaluated model's input; the model must rely on sequence features and general biological knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The mature protein is approximately 185 amino acids (223 total minus ~38-residue signal peptide). This size is characteristic of GH11 endo-xylanases (~180–220 aa) but grossly inconsistent with EC 3.2.1.20 alpha-amylase (GH13), which is typically 400–500 residues. Options C (EC 1.1.1.1, alcohol dehydrogenase, oxidoreductase) and D (EC 5.1.1.25, amino acid racemase, isomerase) belong to entirely different EC classes and lack the hallmarks of glycoside hydrolases (e.g., no Rossmann-like NAD-binding motif for dehydrogenases, no PLP-binding residues for racemases). The small secreted fungal protein with a β-jelly-roll-like compact architecture and catalytic glutamate residues in a GPGTGFNNGYYYSY-type motif is consistent with GH11 xylanase rather than the large (β/α)₈ TIM-barrel alpha-amylase.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise recognition of GH11-specific PROSITE-ProRule motifs (PRU01097) to confirm family assignment beyond the size-based elimination; however, the size argument alone provides a defensible biological distinction between GH11 xylanase and GH13 alpha-amylase.",
    "reason": "A model can eliminate C and D by recognizing the absence of oxidoreductase or isomerase catalytic machinery. Between A and B, the ~185-aa mature size is a strong biological discriminator: EC 3.2.1.20 alpha-amylases are consistently >400 aa, while GH11 xylanases are ~200 aa. This constitutes a concrete structural/biological argument rather than pure database lookup, though full family confirmation would benefit from motif-level pattern matching."
  },
  "case_id": "EC_number_0096",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "H2",
      "H6"
    ],
    "judgment": "supported",
    "reason": "UniProtKB entry Q9UVF9 (EIX_HYPRU) is annotated with EC 3.2.1.8 (endo-1,4-beta-xylanase). The EC assignment carries both a computational evidence code (ECO:0000255, PROSITE-ProRule PRU01097) and experimental confirmation (ECO:0000269, PubMed:16668223 — product characterization demonstrating endohydrolysis of (1→4)-β-D-xylosidic linkages in xylans). Multiple independent publications (PubMed 10517825, 16666504, 16668223) confirm xylanase activity. The benchmark sequence matches the UniProt entry exactly (SHA256 match confirmed)."
  },
  "important_caveats": [
    "The EC number assignment in UniProt carries a PROSITE-ProRule computational evidence code (ECO:0000255) for the EC field itself, but the catalytic activity comment is backed by experimental evidence (ECO:0000269, PubMed:16668223).",
    "The protein also functions as an elicitor (ethylene-inducing xylanase, EIX) with elicitation activity separable from xylanase activity (PubMed 10517825), but the EC number reflects the catalytic xylanase function.",
    "The size-based reasoning is robust for typical alpha-amylases but a model would need to be aware that no known EC 3.2.1.20 enzyme is as small as 185 aa.",
    "All reviewer-only evidence was absent from the evaluated model's input; the model must rely on sequence features and general biological knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The size-based argument cleanly separates A (GH11 xylanase, ~185 aa) from B (GH13 alpha-amylase, ~450 aa). C and D are eliminated by EC class. No ambiguity in the correct answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0096",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProtKB entry Q9UVF9 (EIX_HYPRU) is annotated with EC 3.2.1.8 (endo-1,4-beta-xylanase). The EC assignment carries both a computational evidence code (ECO:0000255, PROSITE-ProRule PRU01097) and experimental confirmation (ECO:0000269, PubMed:16668223 — product characterization demonstrating endohydrolysis of (1→4)-β-D-xylosidic linkages in xylans). Multiple independent publications (PubMed 10517825, 16666504, 16668223) confirm xylanase activity. The benchmark sequence matches the UniProt entry exactly (SHA256 match confirmed).",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C8", "H2", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The mature protein is approximately 185 amino acids (223 total minus ~38-residue signal peptide). This size is characteristic of GH11 endo-xylanases (~180–220 aa) but grossly inconsistent with EC 3.2.1.20 alpha-amylase (GH13), which is typically 400–500 residues. Options C (EC 1.1.1.1, alcohol dehydrogenase, oxidoreductase) and D (EC 5.1.1.25, amino acid racemase, isomerase) belong to entirely different EC classes and lack the hallmarks of glycoside hydrolases (e.g., no Rossmann-like NAD-binding motif for dehydrogenases, no PLP-binding residues for racemases). The small secreted fungal protein with a β-jelly-roll-like compact architecture and catalytic glutamate residues in a GPGTGFNNGYYYSY-type motif is consistent with GH11 xylanase rather than the large (β/α)₈ TIM-barrel alpha-amylase.",
    "missing_item_specific_fact": "Precise recognition of GH11-specific PROSITE-ProRule motifs (PRU01097) to confirm family assignment beyond the size-based elimination; however, the size argument alone provides a defensible biological distinction between GH11 xylanase and GH13 alpha-amylase.",
    "reason": "A model can eliminate C and D by recognizing the absence of oxidoreductase or isomerase catalytic machinery. Between A and B, the ~185-aa mature size is a strong biological discriminator: EC 3.2.1.20 alpha-amylases are consistently >400 aa, while GH11 xylanases are ~200 aa. This constitutes a concrete structural/biological argument rather than pure database lookup, though full family confirmation would benefit from motif-level pattern matching."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The size-based argument cleanly separates A (GH11 xylanase, ~185 aa) from B (GH13 alpha-amylase, ~450 aa). C and D are eliminated by EC class. No ambiguity in the correct answer."
  },
  "important_caveats": [
    "The EC number assignment in UniProt carries a PROSITE-ProRule computational evidence code (ECO:0000255) for the EC field itself, but the catalytic activity comment is backed by experimental evidence (ECO:0000269, PubMed:16668223).",
    "The protein also functions as an elicitor (ethylene-inducing xylanase, EIX) with elicitation activity separable from xylanase activity (PubMed 10517825), but the EC number reflects the catalytic xylanase function.",
    "The size-based reasoning is robust for typical alpha-amylases but a model would need to be aware that no known EC 3.2.1.20 enzyme is as small as 185 aa.",
    "All reviewer-only evidence was absent from the evaluated model's input; the model must rely on sequence features and general biological knowledge."
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

**Accession:** `Q9UVF9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 91. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9UVF9.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.394840+00:00.  

```json
"Q9UVF9"
```

Source SHA-256: `fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9UVF9.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.394840+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"10517825","source":"PubMed"}],"value":"Endo-1,4-beta-xylanase EIX"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"16666504","source":"PubMed"}],"value":"Ethylene biosynthesis-inducing factor"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"16666504","source":"PubMed"}],"value":"EIF"}]}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01097","source":"PROSITE-ProRule"}],"value":"3.2.1.8"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"10517825","source":"PubMed"}],"value":"Ethylene-inducing xylanase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"10517825","source":"PubMed"}],"value":"EIX"}]}}
```

Source SHA-256: `fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9UVF9.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.394840+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.1.8","evidences":[{"evidenceCode":"ECO:0000269","id":"16668223","source":"PubMed"}],"name":"Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans."}}
```

Source SHA-256: `fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9UVF9.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.394840+00:00.  

```json
{"citation":{"authors":["Furman-Matarasso N.","Cohen E.","Du Q.","Chejanovsky N.","Hanania U.","Avni A."],"citationCrossReferences":[{"database":"PubMed","id":"10517825"},{"database":"DOI","id":"10.1104/pp.121.2.345"}],"citationType":"journal article","firstPage":"345","id":"10517825","journal":"Plant Physiol.","lastPage":"351","publicationDate":"1999","title":"A point mutation in the ethylene-inducing xylanase elicitor inhibits the beta-1-4-endoxylanase activity but not the elicitation activity.","volume":"121"},"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","SUBCELLULAR LOCATION","MUTAGENESIS OF GLU-86 AND GLU-177"]}
```

Source SHA-256: `fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9UVF9.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.394840+00:00.  

```json
{"citation":{"authors":["Fuchs Y.","Saxena A.","Gamble H.R.","Anderson J.D."],"citationCrossReferences":[{"database":"PubMed","id":"16666504"},{"database":"DOI","id":"10.1104/pp.89.1.138"}],"citationType":"journal article","firstPage":"138","id":"16666504","journal":"Plant Physiol.","lastPage":"143","publicationDate":"1989","title":"Ethylene biosynthesis-inducing protein from cellulysin is an endoxylanase.","volume":"89"},"referenceNumber":2,"referencePositions":["FUNCTION"]}
```

Source SHA-256: `fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9UVF9.json)  
**Locator:** `/references/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.394840+00:00.  

```json
{"citation":{"authors":["Dean J.F.","Gross K.C.","Anderson J.D."],"citationCrossReferences":[{"database":"PubMed","id":"16668223"},{"database":"DOI","id":"10.1104/pp.96.2.571"}],"citationType":"journal article","firstPage":"571","id":"16668223","journal":"Plant Physiol.","lastPage":"576","publicationDate":"1991","title":"Ethylene Biosynthesis-Inducing Xylanase: III. Product Characterization.","volume":"96"},"referenceNumber":5,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES"]}
```

Source SHA-256: `fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91)  
**Locator:** `lines 6-12`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 91 / 1.  
**Retrieved:** 2026-11-01T06:28:50.576003+00:00.  

```text
DE   RecName: Full=Ethylene-inducing xylanase {ECO:0000303|PubMed:10517825};
DE            Short=EIX {ECO:0000303|PubMed:10517825};
DE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};
DE   AltName: Full=Endo-1,4-beta-xylanase EIX {ECO:0000303|PubMed:10517825};
DE   AltName: Full=Ethylene biosynthesis-inducing factor {ECO:0000303|PubMed:16666504};
DE            Short=EIF {ECO:0000303|PubMed:16666504};
DE   Flags: Precursor;
```

Source SHA-256: `58405d88f8ea2ef78dd2cc137a7fa2fd8d879e249b7706495d0b0eeb486f7eac`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91)  
**Locator:** `lines 156-158`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 91 / 1.  
**Retrieved:** 2026-11-01T06:28:50.576003+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.;
CC         EC=3.2.1.8; Evidence={ECO:0000269|PubMed:16668223};
```

Source SHA-256: `58405d88f8ea2ef78dd2cc137a7fa2fd8d879e249b7706495d0b0eeb486f7eac`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 96. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
