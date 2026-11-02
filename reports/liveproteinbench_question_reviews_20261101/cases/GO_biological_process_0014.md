# GO_biological_process_0014

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **C** — isoleucine biosynthetic process

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MATSSIRSRALGLSRRARFETTRLPFIGRRYKSDETLNRISSKITQPKSQGASQAMLYATGLTEEDMSKAQVGISSVWFEGNPCNMHLNDLSGIVRDSVLRAGLVPMRFNSVGVSDGISMGTAGMRYSLQSRELIADGIETVMNAQWYDANISLPGCDKNMPGVLMAMGRTNRPSIMVYGGSIKPGCSAKGQKLDLVSAFQSYGQFITGQIDETERFDIIRNACPGKGACGGMYTANTLATAIETMGMTVPGSSSCPADDPKKLVECENIGEVVKNMLREEIKPRDVMTRQAFENAMIVVNVLGGSTNAVLHLIAIADSVGIKLTIDDFQAVSDKTPFLADLKPSGKYLMNDLYSIGGTPALLKYLLKEGLIDGSGITVTGKTMKENVASWPDFPADQDIIQPLSNPIKPSGHLQILRGSLAPGGSVGKITGKEGLRFEGTAKCYDYEDAFIESLERGEIKKGEKTVVIIRYEGPKGGPGMPEMLKPSAAIMGAGLGQDVALLTDGRFSGGSHGFLIGHIVPEAMEGGPIALARDGDRIVIDAEEKVVDLDVPTEELDARRKQWKAPPLRYQKGTLKKYCALVSDASHGCVTDGPI

[Multiple Choices]
A. surfactant secretion
B. regulation of inflammatory response
C. isoleucine biosynthetic process
D. cellular response to peptidoglycan
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Biological Process Prediction, which is to predict the primary biological process a given protein participates in, as defined by the Gene Ontology (GO) 'Biological Process' branch. A biological process is a series of molecular events that accomplishes a larger biological program, such as cell division or signal transduction. Based on the provided protein sequence, you must select the option that best describes the overall biological objective to which the protein contributes.. The inputs provided by the user for this task include:

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

> The exact sequence match is annotated as dihydroxy-acid dehydratase, and its pathway annotation places it in L-isoleucine biosynthesis. The support is primarily by similarity/inference rather than direct experimental validation of the isoleucine-biosynthesis role.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Once identified as dihydroxy-acid dehydratase, its role in branched-chain amino-acid biosynthesis supports choice C; however, the supplied sequence and choices alone do not establish that enzyme identity through a clear, general biological clue.


**Missing item-specific fact**

> The protein-specific functional identification as dihydroxy-acid dehydratase and its pathway role in isoleucine biosynthesis, ordinarily obtained from an annotation or sequence-homology/domain analysis.


**Reason**

> The sequence is the only biological input, with no organism, pathway context, or functional annotation. Inferring the precise pathway requires identifying this particular enzyme; generic sequence properties do not distinguish the choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The annotation also places this enzyme in valine biosynthesis, but valine biosynthesis is not an option. Of the listed choices, isoleucine biosynthesis is the supported match.


### Important caveats

- The reviewer evidence matches the supplied sequence, including a historical entry available by the stated cutoff.
- The isoleucine-pathway assignment is annotated by similarity/inference; the cited experimental evidence concerns aspterric-acid biosynthesis and self-resistance, not direct experimental verification of the isoleucine role.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Once identified as dihydroxy-acid dehydratase, its role in branched-chain amino-acid biosynthesis supports choice C; however, the supplied sequence and choices alone do not establish that enzyme identity through a clear, general biological clue.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional identification as dihydroxy-acid dehydratase and its pathway role in isoleucine biosynthesis, ordinarily obtained from an annotation or sequence-homology/domain analysis.",
    "reason": "The sequence is the only biological input, with no organism, pathway context, or functional annotation. Inferring the precise pathway requires identifying this particular enzyme; generic sequence properties do not distinguish the choices."
  },
  "case_id": "GO_biological_process_0014",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H4",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The exact sequence match is annotated as dihydroxy-acid dehydratase, and its pathway annotation places it in L-isoleucine biosynthesis. The support is primarily by similarity/inference rather than direct experimental validation of the isoleucine-biosynthesis role."
  },
  "important_caveats": [
    "The reviewer evidence matches the supplied sequence, including a historical entry available by the stated cutoff.",
    "The isoleucine-pathway assignment is annotated by similarity/inference; the cited experimental evidence concerns aspterric-acid biosynthesis and self-resistance, not direct experimental verification of the isoleucine role."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The annotation also places this enzyme in valine biosynthesis, but valine biosynthesis is not an option. Of the listed choices, isoleucine biosynthesis is the supported match."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0014",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence match is annotated as dihydroxy-acid dehydratase, and its pathway annotation places it in L-isoleucine biosynthesis. The support is primarily by similarity/inference rather than direct experimental validation of the isoleucine-biosynthesis role.",
    "evidence_ids": ["C1", "C5", "C6", "H4", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Once identified as dihydroxy-acid dehydratase, its role in branched-chain amino-acid biosynthesis supports choice C; however, the supplied sequence and choices alone do not establish that enzyme identity through a clear, general biological clue.",
    "missing_item_specific_fact": "The protein-specific functional identification as dihydroxy-acid dehydratase and its pathway role in isoleucine biosynthesis, ordinarily obtained from an annotation or sequence-homology/domain analysis.",
    "reason": "The sequence is the only biological input, with no organism, pathway context, or functional annotation. Inferring the precise pathway requires identifying this particular enzyme; generic sequence properties do not distinguish the choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The annotation also places this enzyme in valine biosynthesis, but valine biosynthesis is not an option. Of the listed choices, isoleucine biosynthesis is the supported match."
  },
  "important_caveats": [
    "The reviewer evidence matches the supplied sequence, including a historical entry available by the stated cutoff.",
    "The isoleucine-pathway assignment is annotated by similarity/inference; the cited experimental evidence concerns aspterric-acid biosynthesis and self-resistance, not direct experimental verification of the isoleucine role."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein is annotated as Dihydroxy-acid dehydratase (DHAD, EC 4.2.1.9) from Penicillium brasilianum. UniProt explicitly assigns GO:0009097 (isoleucine biosynthetic process) via UniPathway, and the PATHWAY comment states 'Amino-acid biosynthesis; L-isoleucine biosynthesis; L-isoleucine from 2-oxobutanoate: step 3/4' (By similarity to Q0CPG9). The FUNCTION comment confirms catalysis of 2,3-dihydroxy-3-methylvalerate → 2-oxo-3-methylvalerate, the penultimate precursor to L-isoleucine. Experimental evidence (PubMed:39511739) supports the enzyme's DHAD catalytic activity within the aspterric acid cluster; the specific isoleucine-pathway assignment is by similarity. The GO annotation is IEA (inferred from electronic annotation via UniPathway), which is computational rather than direct experimental, but is consistent with the enzyme's known substrate specificity.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein is from Penicillium (a fungus). Options A (surfactant secretion, GO:0160069), B (regulation of inflammatory response, GO:0050727), and D (cellular response to peptidoglycan, GO:0071224) are all animal-specific processes: surfactant secretion is a vertebrate lung process, inflammatory response is an animal immune process, and peptidoglycan recognition is an innate immune response in animals. None of these biological processes exist in fungi. Option C (isoleucine biosynthetic process) is a universal metabolic pathway present in all organisms including fungi. The protein sequence (~596 aa) is consistent with a metabolic enzyme (dehydratase) rather than a signaling or secretion protein. A model with general biological knowledge can eliminate A, B, D as incompatible with a fungal metabolic enzyme and select C as the only plausible metabolic biosynthetic pathway.


**Missing item-specific fact**

> None critical. Precise identification of the enzyme as DHAD (EC 4.2.1.9) from sequence motifs would strengthen the answer, but is not strictly necessary given the organism-process incompatibility argument.


**Reason**

> The distractors are all animal immune/secretory processes that are biologically incompatible with a fungal protein. The only option representing a metabolic biosynthetic pathway (present in fungi) is C. This provides a concrete biological reasoning chain from the sequence (fungal metabolic enzyme) and the choices (three animal-specific processes vs. one universal metabolic pathway) that distinguishes the answer without requiring memorization of this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the enzyme also participates in valine biosynthesis (shared BCAA pathway enzyme), 'L-valine biosynthetic process' is not among the options. The protein's primary literature role is in the aspterric acid biosynthesis cluster, but that term is also not an option. Among the four given choices, only C is biologically plausible for a fungal metabolic enzyme, leaving no ambiguity.


### Important caveats

- The isoleucine-pathway GO annotation is IEA (UniPathway inference) and the pathway comment is 'By similarity' to Q0CPG9, not direct experimental assignment for this specific protein. The experimental evidence (PubMed:39511739) supports DHAD catalytic activity in the aspterric acid cluster context.
- The protein's primary described biological role in the literature is as 'Aspterric acid biosynthesis cluster protein D' conferring self-resistance; its role in isoleucine biosynthesis is a secondary/shared enzymatic function.
- The reviewer identified the accession (A0A0F7TWW9) from dataset metadata; this was not available to the evaluated model.
- The sequence matches the UniProt entry exactly (SHA-256 confirmed) at both current and historical (v30) snapshots.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein is from Penicillium (a fungus). Options A (surfactant secretion, GO:0160069), B (regulation of inflammatory response, GO:0050727), and D (cellular response to peptidoglycan, GO:0071224) are all animal-specific processes: surfactant secretion is a vertebrate lung process, inflammatory response is an animal immune process, and peptidoglycan recognition is an innate immune response in animals. None of these biological processes exist in fungi. Option C (isoleucine biosynthetic process) is a universal metabolic pathway present in all organisms including fungi. The protein sequence (~596 aa) is consistent with a metabolic enzyme (dehydratase) rather than a signaling or secretion protein. A model with general biological knowledge can eliminate A, B, D as incompatible with a fungal metabolic enzyme and select C as the only plausible metabolic biosynthetic pathway.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. Precise identification of the enzyme as DHAD (EC 4.2.1.9) from sequence motifs would strengthen the answer, but is not strictly necessary given the organism-process incompatibility argument.",
    "reason": "The distractors are all animal immune/secretory processes that are biologically incompatible with a fungal protein. The only option representing a metabolic biosynthetic pathway (present in fungi) is C. This provides a concrete biological reasoning chain from the sequence (fungal metabolic enzyme) and the choices (three animal-specific processes vs. one universal metabolic pathway) that distinguishes the answer without requiring memorization of this specific protein's database entry."
  },
  "case_id": "GO_biological_process_0014",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H3",
      "H4",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The protein is annotated as Dihydroxy-acid dehydratase (DHAD, EC 4.2.1.9) from Penicillium brasilianum. UniProt explicitly assigns GO:0009097 (isoleucine biosynthetic process) via UniPathway, and the PATHWAY comment states 'Amino-acid biosynthesis; L-isoleucine biosynthesis; L-isoleucine from 2-oxobutanoate: step 3/4' (By similarity to Q0CPG9). The FUNCTION comment confirms catalysis of 2,3-dihydroxy-3-methylvalerate → 2-oxo-3-methylvalerate, the penultimate precursor to L-isoleucine. Experimental evidence (PubMed:39511739) supports the enzyme's DHAD catalytic activity within the aspterric acid cluster; the specific isoleucine-pathway assignment is by similarity. The GO annotation is IEA (inferred from electronic annotation via UniPathway), which is computational rather than direct experimental, but is consistent with the enzyme's known substrate specificity."
  },
  "important_caveats": [
    "The isoleucine-pathway GO annotation is IEA (UniPathway inference) and the pathway comment is 'By similarity' to Q0CPG9, not direct experimental assignment for this specific protein. The experimental evidence (PubMed:39511739) supports DHAD catalytic activity in the aspterric acid cluster context.",
    "The protein's primary described biological role in the literature is as 'Aspterric acid biosynthesis cluster protein D' conferring self-resistance; its role in isoleucine biosynthesis is a secondary/shared enzymatic function.",
    "The reviewer identified the accession (A0A0F7TWW9) from dataset metadata; this was not available to the evaluated model.",
    "The sequence matches the UniProt entry exactly (SHA-256 confirmed) at both current and historical (v30) snapshots."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the enzyme also participates in valine biosynthesis (shared BCAA pathway enzyme), 'L-valine biosynthetic process' is not among the options. The protein's primary literature role is in the aspterric acid biosynthesis cluster, but that term is also not an option. Among the four given choices, only C is biologically plausible for a fungal metabolic enzyme, leaving no ambiguity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0014",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein is annotated as Dihydroxy-acid dehydratase (DHAD, EC 4.2.1.9) from Penicillium brasilianum. UniProt explicitly assigns GO:0009097 (isoleucine biosynthetic process) via UniPathway, and the PATHWAY comment states 'Amino-acid biosynthesis; L-isoleucine biosynthesis; L-isoleucine from 2-oxobutanoate: step 3/4' (By similarity to Q0CPG9). The FUNCTION comment confirms catalysis of 2,3-dihydroxy-3-methylvalerate → 2-oxo-3-methylvalerate, the penultimate precursor to L-isoleucine. Experimental evidence (PubMed:39511739) supports the enzyme's DHAD catalytic activity within the aspterric acid cluster; the specific isoleucine-pathway assignment is by similarity. The GO annotation is IEA (inferred from electronic annotation via UniPathway), which is computational rather than direct experimental, but is consistent with the enzyme's known substrate specificity.",
    "evidence_ids": ["C4", "C5", "C6", "H3", "H4", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein is from Penicillium (a fungus). Options A (surfactant secretion, GO:0160069), B (regulation of inflammatory response, GO:0050727), and D (cellular response to peptidoglycan, GO:0071224) are all animal-specific processes: surfactant secretion is a vertebrate lung process, inflammatory response is an animal immune process, and peptidoglycan recognition is an innate immune response in animals. None of these biological processes exist in fungi. Option C (isoleucine biosynthetic process) is a universal metabolic pathway present in all organisms including fungi. The protein sequence (~596 aa) is consistent with a metabolic enzyme (dehydratase) rather than a signaling or secretion protein. A model with general biological knowledge can eliminate A, B, D as incompatible with a fungal metabolic enzyme and select C as the only plausible metabolic biosynthetic pathway.",
    "missing_item_specific_fact": "None critical. Precise identification of the enzyme as DHAD (EC 4.2.1.9) from sequence motifs would strengthen the answer, but is not strictly necessary given the organism-process incompatibility argument.",
    "reason": "The distractors are all animal immune/secretory processes that are biologically incompatible with a fungal protein. The only option representing a metabolic biosynthetic pathway (present in fungi) is C. This provides a concrete biological reasoning chain from the sequence (fungal metabolic enzyme) and the choices (three animal-specific processes vs. one universal metabolic pathway) that distinguishes the answer without requiring memorization of this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the enzyme also participates in valine biosynthesis (shared BCAA pathway enzyme), 'L-valine biosynthetic process' is not among the options. The protein's primary literature role is in the aspterric acid biosynthesis cluster, but that term is also not an option. Among the four given choices, only C is biologically plausible for a fungal metabolic enzyme, leaving no ambiguity."
  },
  "important_caveats": [
    "The isoleucine-pathway GO annotation is IEA (UniPathway inference) and the pathway comment is 'By similarity' to Q0CPG9, not direct experimental assignment for this specific protein. The experimental evidence (PubMed:39511739) supports DHAD catalytic activity in the aspterric acid cluster context.",
    "The protein's primary described biological role in the literature is as 'Aspterric acid biosynthesis cluster protein D' conferring self-resistance; its role in isoleucine biosynthesis is a secondary/shared enzymatic function.",
    "The reviewer identified the accession (A0A0F7TWW9) from dataset metadata; this was not available to the evaluated model.",
    "The sequence matches the UniProt entry exactly (SHA-256 confirmed) at both current and historical (v30) snapshots."
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

**Accession:** `A0A0F7TWW9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 30. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F7TWW9.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:01.826200+00:00.  

```json
"A0A0F7TWW9"
```

Source SHA-256: `9c9db7d008b685b5073a404f2df8618925830622276ec1c773349e5fd3829400`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F7TWW9.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:01.826200+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39511739","source":"PubMed"}],"value":"Aspterric acid biosynthesis cluster protein D"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"39511739","source":"PubMed"}],"value":"4.2.1.9"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39511739","source":"PubMed"}],"value":"Dihydroxy-acid dehydratase pbrD, mitochondrial"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"39511739","source":"PubMed"}],"value":"DHAD astD"}]}}
```

Source SHA-256: `9c9db7d008b685b5073a404f2df8618925830622276ec1c773349e5fd3829400`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F7TWW9.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:01.826200+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q0CPG9","source":"UniProtKB"},{"evidenceCode":"ECO:0000269","id":"39511739","source":"PubMed"}],"value":"Dihydroxyacid dehydratase; part of the gene cluster that mediates the biosynthesis of the sesquiterpenoid aspterric acid (AA), an inhibitor of dihydroxy-acid dehydratase (DHAD) effective as an herbicide (PubMed:39511739). Performs the third step in the common pathway leading to biosynthesis of branched-chain amino acids (By similarity). Catalyzes the dehydration of (2R,3R)-2,3-dihydroxy-3-methylpentanoate (2,3-dihydroxy-3-methylvalerate) into 2-oxo-3-methylpentanoate (2-oxo-3-methylvalerate) and of (2R)-2,3-dihydroxy-3-methylbutanoate (2,3-dihydroxyisovalerate) into 2-oxo-3-methylbutanoate (2-oxoisovalerate), the penultimate precursor to L-isoleucine and L-valine, respectively (By similarity). PbrD confers self-resistance in the presence of the dihydroxyacid dehydratase inhibitor aspterric acid (AA) produced by the ast cluster (PubMed:39511739)"}]}
```

Source SHA-256: `9c9db7d008b685b5073a404f2df8618925830622276ec1c773349e5fd3829400`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F7TWW9.json)  
**Locator:** `/comments/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:01.826200+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q0CPG9","source":"UniProtKB"}],"value":"Amino-acid biosynthesis; L-isoleucine biosynthesis; L-isoleucine from 2-oxobutanoate: step 3/4"}]}
```

Source SHA-256: `9c9db7d008b685b5073a404f2df8618925830622276ec1c773349e5fd3829400`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F7TWW9?format=txt&versions=30)  
**Locator:** `lines 30-43`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 2.  
**Retrieved:** 2026-11-02T04:24:04.510512+00:00.  

```text
CC   -!- FUNCTION: Dihydroxyacid dehydratase; part of the gene cluster that
CC       mediates the biosynthesis of the sesquiterpenoid aspterric acid (AA),
CC       an inhibitor of dihydroxy-acid dehydratase (DHAD) effective as an
CC       herbicide (PubMed:39511739). Performs the third step in the common
CC       pathway leading to biosynthesis of branched-chain amino acids (By
CC       similarity). Catalyzes the dehydration of (2R,3R)-2,3-dihydroxy-3-
CC       methylpentanoate (2,3-dihydroxy-3-methylvalerate) into 2-oxo-3-
CC       methylpentanoate (2-oxo-3-methylvalerate) and of (2R)-2,3-dihydroxy-3-
CC       methylbutanoate (2,3-dihydroxyisovalerate) into 2-oxo-3-methylbutanoate
CC       (2-oxoisovalerate), the penultimate precursor to L-isoleucine and L-
CC       valine, respectively (By similarity). PbrD confers self-resistance in
CC       the presence of the dihydroxyacid dehydratase inhibitor aspterric acid
CC       (AA) produced by the ast cluster (PubMed:39511739).
CC       {ECO:0000250|UniProtKB:Q0CPG9, ECO:0000269|PubMed:39511739}.
```

Source SHA-256: `5c8dba2f186ec2f5c49e223d9e4d0a5408127c4f67b41ce2f7a9d3d700501ce5`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F7TWW9?format=txt&versions=30)  
**Locator:** `lines 69-71`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 2.  
**Retrieved:** 2026-11-02T04:24:04.510512+00:00.  

```text
CC   -!- PATHWAY: Amino-acid biosynthesis; L-isoleucine biosynthesis; L-
CC       isoleucine from 2-oxobutanoate: step 3/4.
CC       {ECO:0000250|UniProtKB:Q0CPG9}.
```

Source SHA-256: `5c8dba2f186ec2f5c49e223d9e4d0a5408127c4f67b41ce2f7a9d3d700501ce5`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F7TWW9?format=txt&versions=30)  
**Locator:** `lines 94-94`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 2.  
**Retrieved:** 2026-11-02T04:24:04.510512+00:00.  

```text
DR   GO; GO:0009097; P:isoleucine biosynthetic process; IEA:UniProtKB-UniPathway.
```

Source SHA-256: `5c8dba2f186ec2f5c49e223d9e4d0a5408127c4f67b41ce2f7a9d3d700501ce5`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 14. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
