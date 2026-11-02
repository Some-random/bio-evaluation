# EC_number_0146

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
MSSASTPTAPYLEDLVRNSLDQNLPWVVQKYGGTSVGKSLDNITKIVGSYIDNGSKVAIVCSARSTQTKSLGTTNLLLQASREALQPAMSSSGDGRSGSMSGTATPFYPKRVGSGFFGKDQSTSMTSSVSSLSQLESQLGRSGSPSPFQSSSSRSPPRSPATPSQDSSISQEPAFHATVDLIKKGHLEAARASLKGGPLRDELEEEIERDCESLRSFLYAAQIIDEISPRSQDSIVGTGERLACKIVAAALRDRGVDSELVVLDNIVDASMSAASEAVSVDAGDQGVAQLGQEFYDQLSFRLGERLRECGQRVPVVTGYFGPVPGSLLAQIGRGYTDLCAALCAVGLKASELQVWKEVDGIFTADPRKVPSARLVPIITPDEAAELTYYGSEVIHPFTMEQVIRARIPIRIKNVENPSGAGTVIYPDVGFPRGLDTEPPKAERIVEGVDERMPTAVTIKDEIIVLNIHSNRKTLSHGFLARIFGTLDRAGVVVDLISTSEVHVSMAMQDFLNRKRLERLVKDLEKIGEVTVSKDMAILSLVGRNMRNAIGSAGLMFASLARAMINIEMISQGASEINISCVIENKDAIKALNVIHESCLSYPRSPATEMAGLQLQ

[Multiple Choices]
A. 2.7.2.4
B. 2.7.1.52
C. 1.14.14.126
D. 1.1.1.136
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

> The supplied sequence exactly matches the UniProt entry annotated as aspartokinase, EC 2.7.2.4, and the matching historical record retains that annotation. The reaction annotation assigns phosphorylation of L-aspartate to this EC number, but its evidence is transferred by similarity from UniProtKB:P10869 rather than direct experimental evidence for this sequence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may permit family-level recognition, but the input provides no organism, functional annotation, reaction context, or established catalytic-site interpretation that independently identifies the precise substrate and reaction required for EC 2.7.2.4.


**Missing item-specific fact**

> The protein-specific aspartokinase function and its L-aspartate phosphorylation reaction, supplied by the external annotation or by prior knowledge of this sequence or a close homolog.


**Reason**

> Choosing the complete EC number depends on knowing or retrieving the protein-specific catalytic function; recognizing the sequence or invoking a predictor does not itself provide reasoning from the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched sequence annotation supports option A; the other choices classify different reaction types, and the evidence supplies no comparable support for them.


### Important caveats

- The annotation is supported by sequence-matched database records, but the cited evidence is similarity-based, not direct experimental validation of this particular protein.
- The author's exact data-source snapshot is unknown, although the sequence-matched historical record also contains the EC annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may permit family-level recognition, but the input provides no organism, functional annotation, reaction context, or established catalytic-site interpretation that independently identifies the precise substrate and reaction required for EC 2.7.2.4.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific aspartokinase function and its L-aspartate phosphorylation reaction, supplied by the external annotation or by prior knowledge of this sequence or a close homolog.",
    "reason": "Choosing the complete EC number depends on knowing or retrieving the protein-specific catalytic function; recognizing the sequence or invoking a predictor does not itself provide reasoning from the supplied input."
  },
  "case_id": "EC_number_0146",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as aspartokinase, EC 2.7.2.4, and the matching historical record retains that annotation. The reaction annotation assigns phosphorylation of L-aspartate to this EC number, but its evidence is transferred by similarity from UniProtKB:P10869 rather than direct experimental evidence for this sequence."
  },
  "important_caveats": [
    "The annotation is supported by sequence-matched database records, but the cited evidence is similarity-based, not direct experimental validation of this particular protein.",
    "The author's exact data-source snapshot is unknown, although the sequence-matched historical record also contains the EC annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched sequence annotation supports option A; the other choices classify different reaction types, and the evidence supplies no comparable support for them."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0146",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as aspartokinase, EC 2.7.2.4, and the matching historical record retains that annotation. The reaction annotation assigns phosphorylation of L-aspartate to this EC number, but its evidence is transferred by similarity from UniProtKB:P10869 rather than direct experimental evidence for this sequence.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may permit family-level recognition, but the input provides no organism, functional annotation, reaction context, or established catalytic-site interpretation that independently identifies the precise substrate and reaction required for EC 2.7.2.4.",
    "missing_item_specific_fact": "The protein-specific aspartokinase function and its L-aspartate phosphorylation reaction, supplied by the external annotation or by prior knowledge of this sequence or a close homolog.",
    "reason": "Choosing the complete EC number depends on knowing or retrieving the protein-specific catalytic function; recognizing the sequence or invoking a predictor does not itself provide reasoning from the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched sequence annotation supports option A; the other choices classify different reaction types, and the evidence supplies no comparable support for them."
  },
  "important_caveats": [
    "The annotation is supported by sequence-matched database records, but the cited evidence is similarity-based, not direct experimental validation of this particular protein.",
    "The author's exact data-source snapshot is unknown, although the sequence-matched historical record also contains the EC annotation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry J9VS37 (AK_CRYN9, Cryptococcus neoformans HOM3) assigns EC 2.7.2.4 (Aspartokinase) with evidence code ECO:0000250 (inferred by similarity to P10869). The catalytic reaction L-aspartate + ATP → 4-phospho-L-aspartate + ADP is annotated. A functional reference (PubMed:18757810, Kingsbury & McCusker 2008) documents threonine biosynthetic gene essentiality in C. neoformans, providing experimental context. The benchmark sequence matches the UniProt entry exactly (615 AA, SHA256 confirmed). The EC assignment is a database annotation (similarity-based) supported by pathway-level experimental evidence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal region contains a clear P-loop / Walker A motif (GGTSVGKSLDN), identifying the protein as an ATP-binding kinase (EC 2.7.x.x), which eliminates options C (1.14.14.126, cytochrome P450 oxidoreductase) and D (1.1.1.136, hydroxysteroid dehydrogenase oxidoreductase). To distinguish A (2.7.2.4 aspartokinase) from B (2.7.1.52 threonine kinase), the sequence exhibits a bifunctional domain architecture: a kinase domain (P-loop, ATP-binding) followed by a Rossmann-fold-like region (e.g., 'IVGTGERLACK' resembling a dehydrogenase nucleotide-binding motif). This kinase-plus-dehydrogenase architecture is the hallmark of fungal aspartokinase–homoserine dehydrogenase (AK-HSD) bifunctional enzymes (e.g., HOM3 in yeast), which catalyze the first committed step of threonine biosynthesis. Threonine kinase (2.7.1.52) is a monofunctional enzyme without a fused dehydrogenase domain, making the observed architecture inconsistent with option B.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The P-loop motif is directly readable from the sequence and eliminates the two oxidoreductase distractors. The bifunctional kinase-dehydrogenase architecture, also discernible from domain-level sequence features, is a well-established biological signature of fungal aspartokinase-homoserine dehydrogenase and distinguishes EC 2.7.2.4 from the monofunctional threonine kinase (2.7.1.52). This constitutes a concrete, general biological argument rather than a lookup of a specific database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options C and D are oxidoreductases, clearly incompatible with the P-loop kinase signature. Option B (threonine kinase) is the closest distractor but is inconsistent with the bifunctional domain architecture evident in the sequence. Option A is the most defensible answer given the combined kinase + dehydrogenase architecture.


### Important caveats

- The EC 2.7.2.4 assignment in UniProt carries evidence code ECO:0000250 (inferred by similarity to P10869), not direct experimental measurement on this specific C. neoformans protein. The PubMed:18757810 reference provides pathway-level functional evidence (gene essentiality in threonine biosynthesis) but may not constitute direct enzyme-activity assay on this exact sequence.
- The bifunctional AK-HSD architecture argument is a general biological inference from domain organization; it does not constitute proof that the kinase domain specifically phosphorylates aspartate's carboxyl group rather than some other substrate.
- The reviewer-only UniProt accession and annotation were absent from the evaluated model input; the reasoning argument relies solely on sequence-observable features.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal region contains a clear P-loop / Walker A motif (GGTSVGKSLDN), identifying the protein as an ATP-binding kinase (EC 2.7.x.x), which eliminates options C (1.14.14.126, cytochrome P450 oxidoreductase) and D (1.1.1.136, hydroxysteroid dehydrogenase oxidoreductase). To distinguish A (2.7.2.4 aspartokinase) from B (2.7.1.52 threonine kinase), the sequence exhibits a bifunctional domain architecture: a kinase domain (P-loop, ATP-binding) followed by a Rossmann-fold-like region (e.g., 'IVGTGERLACK' resembling a dehydrogenase nucleotide-binding motif). This kinase-plus-dehydrogenase architecture is the hallmark of fungal aspartokinase–homoserine dehydrogenase (AK-HSD) bifunctional enzymes (e.g., HOM3 in yeast), which catalyze the first committed step of threonine biosynthesis. Threonine kinase (2.7.1.52) is a monofunctional enzyme without a fused dehydrogenase domain, making the observed architecture inconsistent with option B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The P-loop motif is directly readable from the sequence and eliminates the two oxidoreductase distractors. The bifunctional kinase-dehydrogenase architecture, also discernible from domain-level sequence features, is a well-established biological signature of fungal aspartokinase-homoserine dehydrogenase and distinguishes EC 2.7.2.4 from the monofunctional threonine kinase (2.7.1.52). This constitutes a concrete, general biological argument rather than a lookup of a specific database entry."
  },
  "case_id": "EC_number_0146",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry J9VS37 (AK_CRYN9, Cryptococcus neoformans HOM3) assigns EC 2.7.2.4 (Aspartokinase) with evidence code ECO:0000250 (inferred by similarity to P10869). The catalytic reaction L-aspartate + ATP → 4-phospho-L-aspartate + ADP is annotated. A functional reference (PubMed:18757810, Kingsbury & McCusker 2008) documents threonine biosynthetic gene essentiality in C. neoformans, providing experimental context. The benchmark sequence matches the UniProt entry exactly (615 AA, SHA256 confirmed). The EC assignment is a database annotation (similarity-based) supported by pathway-level experimental evidence."
  },
  "important_caveats": [
    "The EC 2.7.2.4 assignment in UniProt carries evidence code ECO:0000250 (inferred by similarity to P10869), not direct experimental measurement on this specific C. neoformans protein. The PubMed:18757810 reference provides pathway-level functional evidence (gene essentiality in threonine biosynthesis) but may not constitute direct enzyme-activity assay on this exact sequence.",
    "The bifunctional AK-HSD architecture argument is a general biological inference from domain organization; it does not constitute proof that the kinase domain specifically phosphorylates aspartate's carboxyl group rather than some other substrate.",
    "The reviewer-only UniProt accession and annotation were absent from the evaluated model input; the reasoning argument relies solely on sequence-observable features."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are oxidoreductases, clearly incompatible with the P-loop kinase signature. Option B (threonine kinase) is the closest distractor but is inconsistent with the bifunctional domain architecture evident in the sequence. Option A is the most defensible answer given the combined kinase + dehydrogenase architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0146",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry J9VS37 (AK_CRYN9, Cryptococcus neoformans HOM3) assigns EC 2.7.2.4 (Aspartokinase) with evidence code ECO:0000250 (inferred by similarity to P10869). The catalytic reaction L-aspartate + ATP → 4-phospho-L-aspartate + ADP is annotated. A functional reference (PubMed:18757810, Kingsbury & McCusker 2008) documents threonine biosynthetic gene essentiality in C. neoformans, providing experimental context. The benchmark sequence matches the UniProt entry exactly (615 AA, SHA256 confirmed). The EC assignment is a database annotation (similarity-based) supported by pathway-level experimental evidence.",
    "evidence_ids": ["C4", "C5", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal region contains a clear P-loop / Walker A motif (GGTSVGKSLDN), identifying the protein as an ATP-binding kinase (EC 2.7.x.x), which eliminates options C (1.14.14.126, cytochrome P450 oxidoreductase) and D (1.1.1.136, hydroxysteroid dehydrogenase oxidoreductase). To distinguish A (2.7.2.4 aspartokinase) from B (2.7.1.52 threonine kinase), the sequence exhibits a bifunctional domain architecture: a kinase domain (P-loop, ATP-binding) followed by a Rossmann-fold-like region (e.g., 'IVGTGERLACK' resembling a dehydrogenase nucleotide-binding motif). This kinase-plus-dehydrogenase architecture is the hallmark of fungal aspartokinase–homoserine dehydrogenase (AK-HSD) bifunctional enzymes (e.g., HOM3 in yeast), which catalyze the first committed step of threonine biosynthesis. Threonine kinase (2.7.1.52) is a monofunctional enzyme without a fused dehydrogenase domain, making the observed architecture inconsistent with option B.",
    "missing_item_specific_fact": "",
    "reason": "The P-loop motif is directly readable from the sequence and eliminates the two oxidoreductase distractors. The bifunctional kinase-dehydrogenase architecture, also discernible from domain-level sequence features, is a well-established biological signature of fungal aspartokinase-homoserine dehydrogenase and distinguishes EC 2.7.2.4 from the monofunctional threonine kinase (2.7.1.52). This constitutes a concrete, general biological argument rather than a lookup of a specific database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are oxidoreductases, clearly incompatible with the P-loop kinase signature. Option B (threonine kinase) is the closest distractor but is inconsistent with the bifunctional domain architecture evident in the sequence. Option A is the most defensible answer given the combined kinase + dehydrogenase architecture."
  },
  "important_caveats": [
    "The EC 2.7.2.4 assignment in UniProt carries evidence code ECO:0000250 (inferred by similarity to P10869), not direct experimental measurement on this specific C. neoformans protein. The PubMed:18757810 reference provides pathway-level functional evidence (gene essentiality in threonine biosynthesis) but may not constitute direct enzyme-activity assay on this exact sequence.",
    "The bifunctional AK-HSD architecture argument is a general biological inference from domain organization; it does not constitute proof that the kinase domain specifically phosphorylates aspartate's carboxyl group rather than some other substrate.",
    "The reviewer-only UniProt accession and annotation were absent from the evaluated model input; the reasoning argument relies solely on sequence-observable features."
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

**Accession:** `J9VS37` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 66. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VS37.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:11.359613+00:00.  

```json
"J9VS37"
```

Source SHA-256: `bb5b363535dd2685880902011b1b4759259d3d6916624b8c598839c37e11adcb`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VS37.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:11.359613+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P10869","source":"UniProtKB"}],"value":"2.7.2.4"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Aspartokinase"}}}
```

Source SHA-256: `bb5b363535dd2685880902011b1b4759259d3d6916624b8c598839c37e11adcb`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VS37.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:11.359613+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"P10869","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:23777"}}],"reaction":{"ecNumber":"2.7.2.4","evidences":[{"evidenceCode":"ECO:0000250","id":"P10869","source":"UniProtKB"}],"name":"L-aspartate + ATP = 4-phospho-L-aspartate + ADP","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:23776"},{"database":"ChEBI","id":"CHEBI:29991"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:57535"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `bb5b363535dd2685880902011b1b4759259d3d6916624b8c598839c37e11adcb`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VS37?format=txt&versions=66)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 66 / 1.  
**Retrieved:** 2026-11-01T06:28:11.138363+00:00.  

```text
ID   AK_CRYN9                Reviewed;         615 AA.
AC   J9VS37;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   28-NOV-2012, sequence version 1.
DT   28-JAN-2026, entry version 66.
DE   RecName: Full=Aspartokinase {ECO:0000305};
DE            EC=2.7.2.4 {ECO:0000250|UniProtKB:P10869};
GN   Name=HOM3 {ECO:0000303|PubMed:18757810};
GN   ORFNames=CNAG_04347 {ECO:0000312|EMBL:AFR97078.1};
OS   Cryptococcus neoformans (strain H99 / ATCC 208821 / CBS 10515 / FGSC 9487)
OS   (Cryptococcus neoformans var. grubii serotype A).
OC   Eukaryota; Fungi; Dikarya; Basidiomycota; Agaricomycotina; Tremellomycetes;
OC   Tremellales; Cryptococcaceae; Cryptococcus;
OC   Cryptococcus neoformans species complex.
OX   NCBI_TaxID=235443 {ECO:0000312|Proteomes:UP000010091};
```

Source SHA-256: `77de37c68978830aedf52fdbf53e7f43de3832b6c42ac70c5cda5101f729cb49`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VS37?format=txt&versions=66)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 66 / 1.  
**Retrieved:** 2026-11-01T06:28:11.138363+00:00.  

```text
DE   RecName: Full=Aspartokinase {ECO:0000305};
DE            EC=2.7.2.4 {ECO:0000250|UniProtKB:P10869};
```

Source SHA-256: `77de37c68978830aedf52fdbf53e7f43de3832b6c42ac70c5cda5101f729cb49`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VS37?format=txt&versions=66)  
**Locator:** `lines 35-40`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 66 / 1.  
**Retrieved:** 2026-11-01T06:28:11.138363+00:00.  

```text
RN   [2] {ECO:0000305}
RP   FUNCTION, PATHWAY, AND DISRUPTION PHENOTYPE.
RX   PubMed=18757810; DOI=10.1099/mic.0.2008/019729-0;
RA   Kingsbury J.M., McCusker J.H.;
RT   "Threonine biosynthetic genes are essential in Cryptococcus neoformans.";
RL   Microbiology 154:2767-2775(2008).
```

Source SHA-256: `77de37c68978830aedf52fdbf53e7f43de3832b6c42ac70c5cda5101f729cb49`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VS37?format=txt&versions=66)  
**Locator:** `lines 45-51`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 66 / 1.  
**Retrieved:** 2026-11-01T06:28:11.138363+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-aspartate + ATP = 4-phospho-L-aspartate + ADP;
CC         Xref=Rhea:RHEA:23776, ChEBI:CHEBI:29991, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:57535, ChEBI:CHEBI:456216; EC=2.7.2.4;
CC         Evidence={ECO:0000250|UniProtKB:P10869};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:23777;
CC         Evidence={ECO:0000250|UniProtKB:P10869};
```

Source SHA-256: `77de37c68978830aedf52fdbf53e7f43de3832b6c42ac70c5cda5101f729cb49`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 146. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
