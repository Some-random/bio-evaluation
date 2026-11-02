# EC_number_0009

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **A** — 2.7.2.4

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSQSPTNVPRSYNSVLDLKLASPTNSASGATGGWIVQKFGGTSVGKFPENIVDNIVKVYSQTNRVAVVCSARSSQTKSEGTTSRLLRSADLAENDKDYQPLLNAIEEDHVTNAERIQSEEIKQELIKDTKQEIEHVRELLHACQIIGEISPRSLDSIMAVGEKLSCLFMTALMKDHGLNAVYINLQDVIPLSYDFQKGFDDSFYQFLSQEIGKRVLQCDKEREGEEDVIPVLTGYFGVVPGGLLNGVGRGYTDLCAALAAVALQADELQIWKEVDGIFTADPRKVPNARLLDSVTPEEAAELTYYGSEVIHPFTMEQVIRAKIPIRIKNVENPTGKGTIIYPDNIGRRGEATPPHPPAAFEQLAMSSLLQRKRSATAITAKQDIVVINIHSNKKTLSHGFLAHVFTTLDKYKLVVDLISTSEVHVSMALSIQSDQESQLKHALVDLRKMGTVDVTKKMTIVSLVGKQMVNFIGIAGNMFKVLADEKINIEMISQGANEINISAVINEKDTIRALKSIHAKLLEGGSAIGDSSAVDTRLEALKLS

[Multiple Choices]
A. 2.7.2.4
B. 2.7.1.39
C. 2.7.1.52
D. 2.1.1.348
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

> The exact supplied sequence matches the Candida albicans UniProt entry annotated as aspartokinase, EC 2.7.2.4, for the reaction converting L-aspartate and ATP to 4-phospho-L-aspartate and ADP. The annotation is transferred by similarity from UniProtKB:P10869, not shown here as direct experimental evidence for this protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may support a broad kinase-family inference, but that does not establish the specific substrate and reaction needed to distinguish EC 2.7.2.4 from other kinase options.


**Missing item-specific fact**

> The protein-specific functional annotation or evidence that this enzyme catalyzes aspartate phosphorylation to 4-phospho-L-aspartate is not supplied in the question.


**Reason**

> Choosing the complete EC number depends on protein-specific substrate and reaction information absent from the sequence prompt; recognizing the exact sequence or recalling its database entry would be lookup or memorization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched annotation supports option A. The prompt alone does not establish the exact EC, but that is missing information rather than evidence that another listed option is equally supported.


### Important caveats

- The reviewer-only source annotation applies to the exact sequence, including a historical UniProt record.
- The cited EC assignment is similarity-transferred; the supplied evidence does not independently establish experimental validation for this protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may support a broad kinase-family inference, but that does not establish the specific substrate and reaction needed to distinguish EC 2.7.2.4 from other kinase options.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional annotation or evidence that this enzyme catalyzes aspartate phosphorylation to 4-phospho-L-aspartate is not supplied in the question.",
    "reason": "Choosing the complete EC number depends on protein-specific substrate and reaction information absent from the sequence prompt; recognizing the exact sequence or recalling its database entry would be lookup or memorization."
  },
  "case_id": "EC_number_0009",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the Candida albicans UniProt entry annotated as aspartokinase, EC 2.7.2.4, for the reaction converting L-aspartate and ATP to 4-phospho-L-aspartate and ADP. The annotation is transferred by similarity from UniProtKB:P10869, not shown here as direct experimental evidence for this protein."
  },
  "important_caveats": [
    "The reviewer-only source annotation applies to the exact sequence, including a historical UniProt record.",
    "The cited EC assignment is similarity-transferred; the supplied evidence does not independently establish experimental validation for this protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched annotation supports option A. The prompt alone does not establish the exact EC, but that is missing information rather than evidence that another listed option is equally supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0009",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the Candida albicans UniProt entry annotated as aspartokinase, EC 2.7.2.4, for the reaction converting L-aspartate and ATP to 4-phospho-L-aspartate and ADP. The annotation is transferred by similarity from UniProtKB:P10869, not shown here as direct experimental evidence for this protein.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may support a broad kinase-family inference, but that does not establish the specific substrate and reaction needed to distinguish EC 2.7.2.4 from other kinase options.",
    "missing_item_specific_fact": "The protein-specific functional annotation or evidence that this enzyme catalyzes aspartate phosphorylation to 4-phospho-L-aspartate is not supplied in the question.",
    "reason": "Choosing the complete EC number depends on protein-specific substrate and reaction information absent from the sequence prompt; recognizing the exact sequence or recalling its database entry would be lookup or memorization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched annotation supports option A. The prompt alone does not establish the exact EC, but that is missing information rather than evidence that another listed option is equally supported."
  },
  "important_caveats": [
    "The reviewer-only source annotation applies to the exact sequence, including a historical UniProt record.",
    "The cited EC assignment is similarity-transferred; the supplied evidence does not independently establish experimental validation for this protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied 544-aa sequence matches UniProt A0A1D8PMB8 (HOM3, Candida albicans) exactly (SHA256 confirmed). The current and historical (v39) UniProt entries annotate this protein as Aspartokinase, EC 2.7.2.4, with catalytic activity L-aspartate + ATP → 4-phospho-L-aspartate + ADP (Rhea:RHEA:23776/23777). The annotation evidence code is ECO:0000250 (inferred by similarity to P10869, the S. cerevisiae Hom3 aspartokinase), so this is a computational/similarity-based annotation rather than direct experimental verification. Nonetheless, the sequence match is exact, the protein is identified as HOM3 (the well-characterised fungal aspartokinase), and the annotation is consistent with the amino acid kinase family architecture visible in the sequence (P-loop 'GGTSVG' near position 50). The expected answer EC 2.7.2.4 is supported by the database annotation, with the caveat that the underlying evidence is similarity-based.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal region contains a P-loop / Walker-A motif 'GGTSVGKF' (approx. residues 50–57), characteristic of the amino acid kinase (AAK) superfamily. AAK-family enzymes transfer phosphate to a carboxyl group of their amino-acid substrate, placing them in EC subclass 2.7.2 (phosphotransferases with carboxyl group as acceptor). The four choices span three different EC subclasses: 2.7.2.4 (carboxyl-group acceptor, AAK family), 2.7.1.39 and 2.7.1.52 (alcohol-group acceptor kinases, subclass 2.7.1), and 2.1.1.348 (methyltransferase, subclass 2.1.1). Recognising the P-loop as a kinase motif eliminates D (methyltransferase). Recognising the specific P-loop context and overall domain architecture as amino acid kinase–like, and knowing that AAK enzymes phosphorylate carboxyl groups (not hydroxyl groups), places the enzyme in EC 2.7.2.x rather than 2.7.1.x, eliminating B and C. Only A (2.7.2.4) remains. The overall length (~544 aa) is also consistent with fungal/eukaryotic aspartokinases (Hom3-type, ~500–550 aa) rather than the shorter bacterial aspartokinases (~400 aa), further supporting the AAK assignment.


**Missing item-specific fact**

> None that is strictly indispensable. The reasoning chain (P-loop → kinase; AAK-family P-loop signature → carboxyl-group phosphorylation → EC 2.7.2.x) is grounded in general enzymology and protein-family knowledge. Distinguishing the exact 4th digit (2.7.2.4 vs. 2.7.2.8 NAG-kinase vs. 2.7.2.11 homoserine kinase) would require more specific knowledge, but the answer set contains only one 2.7.2.x option, so that distinction is not needed.


**Reason**

> A defensible biological reasoning chain exists: identify the P-loop to call the protein a kinase, recognise the amino acid kinase family signature to assign carboxyl-group phosphorylation (EC 2.7.2.x), and eliminate the 2.7.1.x and 2.1.1.x distractors. This does not require memorising a specific UniProt entry; it relies on general knowledge of kinase motif biology and EC classification logic. The question is therefore reasoning-supported, though it demands familiarity with the AAK superfamily's sequence signatures.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices occupy three distinct EC subclasses (2.7.2, 2.7.1, 2.1.1), so the subclass-level reasoning (carboxyl vs. alcohol vs. methyl transfer) cleanly isolates option A. No other option is in the 2.7.2.x subclass, so there is no ambiguity among the given choices once the AAK assignment is made.


### Important caveats

- The UniProt annotation for EC 2.7.2.4 carries evidence code ECO:0000250 (inferred by similarity to P10869, S. cerevisiae Hom3), not direct experimental validation. The annotation is a computational transfer, though it is highly plausible given the exact sequence match to a well-studied ortholog.
- The P-loop motif 'GGTSVG' is suggestive but not absolutely exclusive to the amino acid kinase superfamily; the reasoning also relies on the broader domain architecture and the EC-classification logic (carboxyl vs. alcohol acceptor).
- The reviewer-only evidence (accession A0A1D8PMB8, organism, annotation) was not available to the evaluated model; the reasoning assessment above is based solely on the sequence and the four choices as presented to the model.
- The first-publication date of the UniProt entry is 2025-02-05 and the historical Swiss-Prot version (v39) was released 2025-06-18. If the benchmark was constructed before that date, the annotation may not have been publicly available at authoring time, though the sequence itself (from 2017) would have been.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal region contains a P-loop / Walker-A motif 'GGTSVGKF' (approx. residues 50–57), characteristic of the amino acid kinase (AAK) superfamily. AAK-family enzymes transfer phosphate to a carboxyl group of their amino-acid substrate, placing them in EC subclass 2.7.2 (phosphotransferases with carboxyl group as acceptor). The four choices span three different EC subclasses: 2.7.2.4 (carboxyl-group acceptor, AAK family), 2.7.1.39 and 2.7.1.52 (alcohol-group acceptor kinases, subclass 2.7.1), and 2.1.1.348 (methyltransferase, subclass 2.1.1). Recognising the P-loop as a kinase motif eliminates D (methyltransferase). Recognising the specific P-loop context and overall domain architecture as amino acid kinase–like, and knowing that AAK enzymes phosphorylate carboxyl groups (not hydroxyl groups), places the enzyme in EC 2.7.2.x rather than 2.7.1.x, eliminating B and C. Only A (2.7.2.4) remains. The overall length (~544 aa) is also consistent with fungal/eukaryotic aspartokinases (Hom3-type, ~500–550 aa) rather than the shorter bacterial aspartokinases (~400 aa), further supporting the AAK assignment.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None that is strictly indispensable. The reasoning chain (P-loop → kinase; AAK-family P-loop signature → carboxyl-group phosphorylation → EC 2.7.2.x) is grounded in general enzymology and protein-family knowledge. Distinguishing the exact 4th digit (2.7.2.4 vs. 2.7.2.8 NAG-kinase vs. 2.7.2.11 homoserine kinase) would require more specific knowledge, but the answer set contains only one 2.7.2.x option, so that distinction is not needed.",
    "reason": "A defensible biological reasoning chain exists: identify the P-loop to call the protein a kinase, recognise the amino acid kinase family signature to assign carboxyl-group phosphorylation (EC 2.7.2.x), and eliminate the 2.7.1.x and 2.1.1.x distractors. This does not require memorising a specific UniProt entry; it relies on general knowledge of kinase motif biology and EC classification logic. The question is therefore reasoning-supported, though it demands familiarity with the AAK superfamily's sequence signatures."
  },
  "case_id": "EC_number_0009",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The supplied 544-aa sequence matches UniProt A0A1D8PMB8 (HOM3, Candida albicans) exactly (SHA256 confirmed). The current and historical (v39) UniProt entries annotate this protein as Aspartokinase, EC 2.7.2.4, with catalytic activity L-aspartate + ATP → 4-phospho-L-aspartate + ADP (Rhea:RHEA:23776/23777). The annotation evidence code is ECO:0000250 (inferred by similarity to P10869, the S. cerevisiae Hom3 aspartokinase), so this is a computational/similarity-based annotation rather than direct experimental verification. Nonetheless, the sequence match is exact, the protein is identified as HOM3 (the well-characterised fungal aspartokinase), and the annotation is consistent with the amino acid kinase family architecture visible in the sequence (P-loop 'GGTSVG' near position 50). The expected answer EC 2.7.2.4 is supported by the database annotation, with the caveat that the underlying evidence is similarity-based."
  },
  "important_caveats": [
    "The UniProt annotation for EC 2.7.2.4 carries evidence code ECO:0000250 (inferred by similarity to P10869, S. cerevisiae Hom3), not direct experimental validation. The annotation is a computational transfer, though it is highly plausible given the exact sequence match to a well-studied ortholog.",
    "The P-loop motif 'GGTSVG' is suggestive but not absolutely exclusive to the amino acid kinase superfamily; the reasoning also relies on the broader domain architecture and the EC-classification logic (carboxyl vs. alcohol acceptor).",
    "The reviewer-only evidence (accession A0A1D8PMB8, organism, annotation) was not available to the evaluated model; the reasoning assessment above is based solely on the sequence and the four choices as presented to the model.",
    "The first-publication date of the UniProt entry is 2025-02-05 and the historical Swiss-Prot version (v39) was released 2025-06-18. If the benchmark was constructed before that date, the annotation may not have been publicly available at authoring time, though the sequence itself (from 2017) would have been."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices occupy three distinct EC subclasses (2.7.2, 2.7.1, 2.1.1), so the subclass-level reasoning (carboxyl vs. alcohol vs. methyl transfer) cleanly isolates option A. No other option is in the 2.7.2.x subclass, so there is no ambiguity among the given choices once the AAK assignment is made."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0009",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied 544-aa sequence matches UniProt A0A1D8PMB8 (HOM3, Candida albicans) exactly (SHA256 confirmed). The current and historical (v39) UniProt entries annotate this protein as Aspartokinase, EC 2.7.2.4, with catalytic activity L-aspartate + ATP → 4-phospho-L-aspartate + ADP (Rhea:RHEA:23776/23777). The annotation evidence code is ECO:0000250 (inferred by similarity to P10869, the S. cerevisiae Hom3 aspartokinase), so this is a computational/similarity-based annotation rather than direct experimental verification. Nonetheless, the sequence match is exact, the protein is identified as HOM3 (the well-characterised fungal aspartokinase), and the annotation is consistent with the amino acid kinase family architecture visible in the sequence (P-loop 'GGTSVG' near position 50). The expected answer EC 2.7.2.4 is supported by the database annotation, with the caveat that the underlying evidence is similarity-based.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal region contains a P-loop / Walker-A motif 'GGTSVGKF' (approx. residues 50–57), characteristic of the amino acid kinase (AAK) superfamily. AAK-family enzymes transfer phosphate to a carboxyl group of their amino-acid substrate, placing them in EC subclass 2.7.2 (phosphotransferases with carboxyl group as acceptor). The four choices span three different EC subclasses: 2.7.2.4 (carboxyl-group acceptor, AAK family), 2.7.1.39 and 2.7.1.52 (alcohol-group acceptor kinases, subclass 2.7.1), and 2.1.1.348 (methyltransferase, subclass 2.1.1). Recognising the P-loop as a kinase motif eliminates D (methyltransferase). Recognising the specific P-loop context and overall domain architecture as amino acid kinase–like, and knowing that AAK enzymes phosphorylate carboxyl groups (not hydroxyl groups), places the enzyme in EC 2.7.2.x rather than 2.7.1.x, eliminating B and C. Only A (2.7.2.4) remains. The overall length (~544 aa) is also consistent with fungal/eukaryotic aspartokinases (Hom3-type, ~500–550 aa) rather than the shorter bacterial aspartokinases (~400 aa), further supporting the AAK assignment.",
    "missing_item_specific_fact": "None that is strictly indispensable. The reasoning chain (P-loop → kinase; AAK-family P-loop signature → carboxyl-group phosphorylation → EC 2.7.2.x) is grounded in general enzymology and protein-family knowledge. Distinguishing the exact 4th digit (2.7.2.4 vs. 2.7.2.8 NAG-kinase vs. 2.7.2.11 homoserine kinase) would require more specific knowledge, but the answer set contains only one 2.7.2.x option, so that distinction is not needed.",
    "reason": "A defensible biological reasoning chain exists: identify the P-loop to call the protein a kinase, recognise the amino acid kinase family signature to assign carboxyl-group phosphorylation (EC 2.7.2.x), and eliminate the 2.7.1.x and 2.1.1.x distractors. This does not require memorising a specific UniProt entry; it relies on general knowledge of kinase motif biology and EC classification logic. The question is therefore reasoning-supported, though it demands familiarity with the AAK superfamily's sequence signatures."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices occupy three distinct EC subclasses (2.7.2, 2.7.1, 2.1.1), so the subclass-level reasoning (carboxyl vs. alcohol vs. methyl transfer) cleanly isolates option A. No other option is in the 2.7.2.x subclass, so there is no ambiguity among the given choices once the AAK assignment is made."
  },
  "important_caveats": [
    "The UniProt annotation for EC 2.7.2.4 carries evidence code ECO:0000250 (inferred by similarity to P10869, S. cerevisiae Hom3), not direct experimental validation. The annotation is a computational transfer, though it is highly plausible given the exact sequence match to a well-studied ortholog.",
    "The P-loop motif 'GGTSVG' is suggestive but not absolutely exclusive to the amino acid kinase superfamily; the reasoning also relies on the broader domain architecture and the EC-classification logic (carboxyl vs. alcohol acceptor).",
    "The reviewer-only evidence (accession A0A1D8PMB8, organism, annotation) was not available to the evaluated model; the reasoning assessment above is based solely on the sequence and the four choices as presented to the model.",
    "The first-publication date of the UniProt entry is 2025-02-05 and the historical Swiss-Prot version (v39) was released 2025-06-18. If the benchmark was constructed before that date, the annotation may not have been publicly available at authoring time, though the sequence itself (from 2017) would have been."
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

**Accession:** `A0A1D8PMB8` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 39. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:32.794689+00:00.  

```json
"A0A1D8PMB8"
```

Source SHA-256: `7c688e4eaabc3e4781e5ade84edef7517de0ae1c9eaf84cba6bd0311b17eacc2`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:32.794689+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P10869","source":"UniProtKB"}],"value":"2.7.2.4"}],"fullName":{"value":"Aspartokinase"}}}
```

Source SHA-256: `7c688e4eaabc3e4781e5ade84edef7517de0ae1c9eaf84cba6bd0311b17eacc2`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:32.794689+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"P10869","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:23777"}}],"reaction":{"ecNumber":"2.7.2.4","evidences":[{"evidenceCode":"ECO:0000250","id":"P10869","source":"UniProtKB"}],"name":"L-aspartate + ATP = 4-phospho-L-aspartate + ADP","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:23776"},{"database":"ChEBI","id":"CHEBI:29991"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:57535"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `7c688e4eaabc3e4781e5ade84edef7517de0ae1c9eaf84cba6bd0311b17eacc2`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1D8PMB8?format=txt&versions=39)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 39 / 1.  
**Retrieved:** 2026-11-02T04:24:35.627360+00:00.  

```text
ID   AK_CANAL                Reviewed;         544 AA.
AC   A0A1D8PMB8;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   18-JAN-2017, sequence version 1.
DT   18-JUN-2025, entry version 39.
DE   RecName: Full=Aspartokinase;
DE            EC=2.7.2.4 {ECO:0000250|UniProtKB:P10869};
GN   Name=HOM3 {ECO:0000312|CGD:CAL0000181037};
GN   OrderedLocusNames=CAALFM_C405540WA {ECO:0000312|EMBL:AOW29286.1},
GN   orf19.8820 {ECO:0000312|CGD:CAL0000181037};
OS   Candida albicans (strain SC5314 / ATCC MYA-2876) (Yeast).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Saccharomycotina; Pichiomycetes;
OC   Debaryomycetaceae; Candida/Lodderomyces clade; Candida.
OX   NCBI_TaxID=237561 {ECO:0000312|Proteomes:UP000000559};
```

Source SHA-256: `25e1c2e406fb09fd648127e1e60780d1244490e7b9ae80cba023db5b2b691f93`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1D8PMB8?format=txt&versions=39)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 39 / 1.  
**Retrieved:** 2026-11-02T04:24:35.627360+00:00.  

```text
DE   RecName: Full=Aspartokinase;
DE            EC=2.7.2.4 {ECO:0000250|UniProtKB:P10869};
```

Source SHA-256: `25e1c2e406fb09fd648127e1e60780d1244490e7b9ae80cba023db5b2b691f93`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1D8PMB8?format=txt&versions=39)  
**Locator:** `lines 63-69`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 39 / 1.  
**Retrieved:** 2026-11-02T04:24:35.627360+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-aspartate + ATP = 4-phospho-L-aspartate + ADP;
CC         Xref=Rhea:RHEA:23776, ChEBI:CHEBI:29991, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:57535, ChEBI:CHEBI:456216; EC=2.7.2.4;
CC         Evidence={ECO:0000250|UniProtKB:P10869};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:23777;
CC         Evidence={ECO:0000250|UniProtKB:P10869};
```

Source SHA-256: `25e1c2e406fb09fd648127e1e60780d1244490e7b9ae80cba023db5b2b691f93`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 9. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
