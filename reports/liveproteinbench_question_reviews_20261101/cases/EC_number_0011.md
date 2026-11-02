# EC_number_0011

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **A** — 3.2.1.37

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAPLITNIYTADPSAHVFNGKLYIYPSHDRETDIQFNDNGDQYDMADYHVFSLDSLDPPSEVTDHGVVLKVEDIPWVSKQLWAPDAATKDGKYYLYFPARDKEGIFRIGVAVSDKPEGPFTPDPEPIKGSYSIDPAVFVDDDGSAYMYFGGLWGGQLQCYQKGNNIFDAEWSGPKEPSGSGAKALGPRVAKLTDDMRQFAEEVREIVILAPETGEPLAADDHDRRFFEAAWMHKYNGKYYFSYSTGDTHYLVYAVGDSPYGPFTYGGRILEPVLGWTTHHSIVEFQGRWWLFHHDCELSKGVDHLRSVKVKEIWYDKDGKIVTEKPE

[Multiple Choices]
A. 3.2.1.37
B. 3.2.1.18
C. 2.7.1.39
D. 2.7.2.4
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

> The exact sequence matches the UniProt entry annotated with EC 3.2.1.37 for beta-xylosidase activity. The annotation cites experimental evidence (ECO:0000269) and specifies hydrolysis of beta-D-xylans. The entry also records a second activity, EC 3.2.1.55, which is not among the choices.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may support a broad enzyme-family or hydrolase inference, but that does not establish the precise substrate specificity needed to distinguish EC 3.2.1.37 from other hydrolase options.


**Missing item-specific fact**

> The protein's experimentally characterized beta-xylosidase activity, including hydrolysis of beta-D-xylans, is needed to select EC 3.2.1.37.


**Reason**

> The input supplies only a sequence and options. Assigning this specific EC number depends on protein-specific functional annotation or experimental substrate characterization absent from the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched protein is also annotated with EC 3.2.1.55, but that activity is not listed; among the provided options, only A matches a documented activity.


### Important caveats

- The reviewer-only evidence matches the supplied sequence, but the author's exact source snapshot is unknown.
- The cited experimental evidence is retained in the database annotation; the primary study was not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may support a broad enzyme-family or hydrolase inference, but that does not establish the precise substrate specificity needed to distinguish EC 3.2.1.37 from other hydrolase options.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's experimentally characterized beta-xylosidase activity, including hydrolysis of beta-D-xylans, is needed to select EC 3.2.1.37.",
    "reason": "The input supplies only a sequence and options. Assigning this specific EC number depends on protein-specific functional annotation or experimental substrate characterization absent from the question."
  },
  "case_id": "EC_number_0011",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated with EC 3.2.1.37 for beta-xylosidase activity. The annotation cites experimental evidence (ECO:0000269) and specifies hydrolysis of beta-D-xylans. The entry also records a second activity, EC 3.2.1.55, which is not among the choices."
  },
  "important_caveats": [
    "The reviewer-only evidence matches the supplied sequence, but the author's exact source snapshot is unknown.",
    "The cited experimental evidence is retained in the database annotation; the primary study was not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched protein is also annotated with EC 3.2.1.55, but that activity is not listed; among the provided options, only A matches a documented activity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0011",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated with EC 3.2.1.37 for beta-xylosidase activity. The annotation cites experimental evidence (ECO:0000269) and specifies hydrolysis of beta-D-xylans. The entry also records a second activity, EC 3.2.1.55, which is not among the choices.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may support a broad enzyme-family or hydrolase inference, but that does not establish the precise substrate specificity needed to distinguish EC 3.2.1.37 from other hydrolase options.",
    "missing_item_specific_fact": "The protein's experimentally characterized beta-xylosidase activity, including hydrolysis of beta-D-xylans, is needed to select EC 3.2.1.37.",
    "reason": "The input supplies only a sequence and options. Assigning this specific EC number depends on protein-specific functional annotation or experimental substrate characterization absent from the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched protein is also annotated with EC 3.2.1.55, but that activity is not listed; among the provided options, only A matches a documented activity."
  },
  "important_caveats": [
    "The reviewer-only evidence matches the supplied sequence, but the author's exact source snapshot is unknown.",
    "The cited experimental evidence is retained in the database annotation; the primary study was not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry V9TNS0 (XY43A_HUMIN, sequence matched) is annotated with EC 3.2.1.37 (beta-xylosidase) supported by experimental evidence (ECO:0000269, PubMed:24262572). The catalytic activity comment confirms hydrolysis of (1→4)-beta-D-xylans to remove successive D-xylose residues from non-reducing termini. The protein also carries EC 3.2.1.55 (alpha-L-arabinofuranosidase), but this is not among the answer choices.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One can reason away options C (2.7.1.39, adenosine kinase) and D (2.7.2.4, creatine kinase) because the sequence lacks kinase signature motifs (Walker A/B, glycine-rich ATP-binding loops, phosphotransfer catalytic residues). However, distinguishing between the two glycosidase options (A: 3.2.1.37 vs B: 3.2.1.18) from sequence alone requires knowing the specific GH family assignment (GH43) and the exact substrate specificity of the active site, which is not reliably determinable from primary sequence without structural or database knowledge.


**Missing item-specific fact**

> The specific substrate specificity (beta-xylosidase vs. the enzyme denoted by EC 3.2.1.18) of this particular GH43 enzyme, and the fact that this protein's primary annotated activity is EC 3.2.1.37 rather than another glycosidase EC number. This requires knowledge of the GH43 family's catalytic mechanism and the specific residue configuration determining xylose vs. other sugar release.


**Reason**

> While the hydrolase-vs-transferase distinction (eliminating C and D) is somewhat reasoning-accessible from the absence of kinase motifs, the critical distinction between glycosidase EC numbers A and B depends on knowing the precise catalytic mechanism and substrate specificity encoded in the 3D active-site architecture. No general sequence heuristic reliably distinguishes 3.2.1.37 from other glycosidase EC numbers without family-level database knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the protein is bifunctional (EC 3.2.1.37 and EC 3.2.1.55), only 3.2.1.37 appears among the choices. Option B (3.2.1.18) is a different EC number not assigned to this protein. Options C and D are unrelated transferases. Among the four choices, only A matches the experimental annotation, so no ambiguity exists within the given option set.


### Important caveats

- The protein is annotated with two EC numbers (3.2.1.37 and 3.2.1.55) per experimental evidence; the question implicitly selects the 'primary' activity by making 3.2.1.55 absent from the choices.
- EC 3.2.1.18: its validity and assignment as a current EC number could not be independently confirmed from the supplied evidence; if it is obsolete or unassigned, option B is a trivially eliminable distractor, further reducing reasoning difficulty.
- The sequence-match is confirmed (SHA-256 identical) between the benchmark input and UniProt V9TNS0, ensuring the annotation applies to the exact sequence provided.
- The reviewer-only UniProt annotation was not available to the evaluated model; the model must rely solely on the 327-aa sequence and general biological knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One can reason away options C (2.7.1.39, adenosine kinase) and D (2.7.2.4, creatine kinase) because the sequence lacks kinase signature motifs (Walker A/B, glycine-rich ATP-binding loops, phosphotransfer catalytic residues). However, distinguishing between the two glycosidase options (A: 3.2.1.37 vs B: 3.2.1.18) from sequence alone requires knowing the specific GH family assignment (GH43) and the exact substrate specificity of the active site, which is not reliably determinable from primary sequence without structural or database knowledge.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate specificity (beta-xylosidase vs. the enzyme denoted by EC 3.2.1.18) of this particular GH43 enzyme, and the fact that this protein's primary annotated activity is EC 3.2.1.37 rather than another glycosidase EC number. This requires knowledge of the GH43 family's catalytic mechanism and the specific residue configuration determining xylose vs. other sugar release.",
    "reason": "While the hydrolase-vs-transferase distinction (eliminating C and D) is somewhat reasoning-accessible from the absence of kinase motifs, the critical distinction between glycosidase EC numbers A and B depends on knowing the precise catalytic mechanism and substrate specificity encoded in the 3D active-site architecture. No general sequence heuristic reliably distinguishes 3.2.1.37 from other glycosidase EC numbers without family-level database knowledge."
  },
  "case_id": "EC_number_0011",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry V9TNS0 (XY43A_HUMIN, sequence matched) is annotated with EC 3.2.1.37 (beta-xylosidase) supported by experimental evidence (ECO:0000269, PubMed:24262572). The catalytic activity comment confirms hydrolysis of (1→4)-beta-D-xylans to remove successive D-xylose residues from non-reducing termini. The protein also carries EC 3.2.1.55 (alpha-L-arabinofuranosidase), but this is not among the answer choices."
  },
  "important_caveats": [
    "The protein is annotated with two EC numbers (3.2.1.37 and 3.2.1.55) per experimental evidence; the question implicitly selects the 'primary' activity by making 3.2.1.55 absent from the choices.",
    "EC 3.2.1.18: its validity and assignment as a current EC number could not be independently confirmed from the supplied evidence; if it is obsolete or unassigned, option B is a trivially eliminable distractor, further reducing reasoning difficulty.",
    "The sequence-match is confirmed (SHA-256 identical) between the benchmark input and UniProt V9TNS0, ensuring the annotation applies to the exact sequence provided.",
    "The reviewer-only UniProt annotation was not available to the evaluated model; the model must rely solely on the 327-aa sequence and general biological knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the protein is bifunctional (EC 3.2.1.37 and EC 3.2.1.55), only 3.2.1.37 appears among the choices. Option B (3.2.1.18) is a different EC number not assigned to this protein. Options C and D are unrelated transferases. Among the four choices, only A matches the experimental annotation, so no ambiguity exists within the given option set."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0011",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry V9TNS0 (XY43A_HUMIN, sequence matched) is annotated with EC 3.2.1.37 (beta-xylosidase) supported by experimental evidence (ECO:0000269, PubMed:24262572). The catalytic activity comment confirms hydrolysis of (1→4)-beta-D-xylans to remove successive D-xylose residues from non-reducing termini. The protein also carries EC 3.2.1.55 (alpha-L-arabinofuranosidase), but this is not among the answer choices.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One can reason away options C (2.7.1.39, adenosine kinase) and D (2.7.2.4, creatine kinase) because the sequence lacks kinase signature motifs (Walker A/B, glycine-rich ATP-binding loops, phosphotransfer catalytic residues). However, distinguishing between the two glycosidase options (A: 3.2.1.37 vs B: 3.2.1.18) from sequence alone requires knowing the specific GH family assignment (GH43) and the exact substrate specificity of the active site, which is not reliably determinable from primary sequence without structural or database knowledge.",
    "missing_item_specific_fact": "The specific substrate specificity (beta-xylosidase vs. the enzyme denoted by EC 3.2.1.18) of this particular GH43 enzyme, and the fact that this protein's primary annotated activity is EC 3.2.1.37 rather than another glycosidase EC number. This requires knowledge of the GH43 family's catalytic mechanism and the specific residue configuration determining xylose vs. other sugar release.",
    "reason": "While the hydrolase-vs-transferase distinction (eliminating C and D) is somewhat reasoning-accessible from the absence of kinase motifs, the critical distinction between glycosidase EC numbers A and B depends on knowing the precise catalytic mechanism and substrate specificity encoded in the 3D active-site architecture. No general sequence heuristic reliably distinguishes 3.2.1.37 from other glycosidase EC numbers without family-level database knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the protein is bifunctional (EC 3.2.1.37 and EC 3.2.1.55), only 3.2.1.37 appears among the choices. Option B (3.2.1.18) is a different EC number not assigned to this protein. Options C and D are unrelated transferases. Among the four choices, only A matches the experimental annotation, so no ambiguity exists within the given option set."
  },
  "important_caveats": [
    "The protein is annotated with two EC numbers (3.2.1.37 and 3.2.1.55) per experimental evidence; the question implicitly selects the 'primary' activity by making 3.2.1.55 absent from the choices.",
    "EC 3.2.1.18: its validity and assignment as a current EC number could not be independently confirmed from the supplied evidence; if it is obsolete or unassigned, option B is a trivially eliminable distractor, further reducing reasoning difficulty.",
    "The sequence-match is confirmed (SHA-256 identical) between the benchmark input and UniProt V9TNS0, ensuring the annotation applies to the exact sequence provided.",
    "The reviewer-only UniProt annotation was not available to the evaluated model; the model must rely solely on the 327-aa sequence and general biological knowledge."
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

**Accession:** `V9TNS0` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 21. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TNS0.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.909204+00:00.  

```json
"V9TNS0"
```

Source SHA-256: `4161e2957710d391f76f21ebe451652d828870a93127025ad04961d04b1d3c73`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TNS0.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.909204+00:00.  

```json
{"includes":[{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"24262572","source":"PubMed"}],"value":"1,4-beta-D-xylan xylohydrolase"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"24262572","source":"PubMed"}],"value":"Xylan 1,4-beta-xylosidase"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"24262572","source":"PubMed"}],"value":"3.2.1.37"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"24262572","source":"PubMed"}],"value":"Beta-xylosidase"}}},{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"24262572","source":"PubMed"}],"value":"3.2.1.55"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"24262572","source":"PubMed"}],"value":"Alpha-L-arabinofuranosidase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"24262572","source":"PubMed"}],"value":"Arabinosidase"}]}}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"24262572","source":"PubMed"}],"value":"Xylosidase/arabinosidase 43A"}}}
```

Source SHA-256: `4161e2957710d391f76f21ebe451652d828870a93127025ad04961d04b1d3c73`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TNS0.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.909204+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.1.37","evidences":[{"evidenceCode":"ECO:0000269","id":"24262572","source":"PubMed"}],"name":"Hydrolysis of (1->4)-beta-D-xylans, to remove successive D-xylose residues from the non-reducing termini."}}
```

Source SHA-256: `4161e2957710d391f76f21ebe451652d828870a93127025ad04961d04b1d3c73`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TNS0.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.909204+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.1.55","evidences":[{"evidenceCode":"ECO:0000269","id":"24262572","source":"PubMed"}],"name":"Hydrolysis of terminal non-reducing alpha-L-arabinofuranoside residues in alpha-L-arabinosides."}}
```

Source SHA-256: `4161e2957710d391f76f21ebe451652d828870a93127025ad04961d04b1d3c73`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/V9TNS0?format=txt&versions=21)  
**Locator:** `lines 6-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 21 / 1.  
**Retrieved:** 2026-11-01T06:28:51.766326+00:00.  

```text
DE   RecName: Full=Xylosidase/arabinosidase 43A {ECO:0000303|PubMed:24262572};
DE   Includes:
DE     RecName: Full=Beta-xylosidase {ECO:0000303|PubMed:24262572};
DE              EC=3.2.1.37 {ECO:0000269|PubMed:24262572};
DE     AltName: Full=1,4-beta-D-xylan xylohydrolase {ECO:0000303|PubMed:24262572};
DE     AltName: Full=Xylan 1,4-beta-xylosidase {ECO:0000303|PubMed:24262572};
DE   Includes:
DE     RecName: Full=Alpha-L-arabinofuranosidase {ECO:0000303|PubMed:24262572};
DE              Short=Arabinosidase {ECO:0000303|PubMed:24262572};
DE              EC=3.2.1.55 {ECO:0000269|PubMed:24262572};
```

Source SHA-256: `9e4bf9e42b116a4202b7fa35da7f1678719e0062361cb3f723d101ecbaf0326f`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/V9TNS0?format=txt&versions=21)  
**Locator:** `lines 46-49`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 21 / 1.  
**Retrieved:** 2026-11-01T06:28:51.766326+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Hydrolysis of (1->4)-beta-D-xylans, to remove successive D-
CC         xylose residues from the non-reducing termini.; EC=3.2.1.37;
CC         Evidence={ECO:0000269|PubMed:24262572};
```

Source SHA-256: `9e4bf9e42b116a4202b7fa35da7f1678719e0062361cb3f723d101ecbaf0326f`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/V9TNS0?format=txt&versions=21)  
**Locator:** `lines 50-53`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 21 / 1.  
**Retrieved:** 2026-11-01T06:28:51.766326+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Hydrolysis of terminal non-reducing alpha-L-arabinofuranoside
CC         residues in alpha-L-arabinosides.; EC=3.2.1.55;
CC         Evidence={ECO:0000269|PubMed:24262572};
```

Source SHA-256: `9e4bf9e42b116a4202b7fa35da7f1678719e0062361cb3f723d101ecbaf0326f`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 11. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
