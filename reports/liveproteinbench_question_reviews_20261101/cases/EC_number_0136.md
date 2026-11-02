# EC_number_0136

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **D** — 2.1.1.5

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MEVNQKWNWDTKPILVKCGGFSSQLAKNVTEKVDGDPLWGSRFDATNPEAVIQTHLDFLRNGADIILTNTYQSSVEGFVKYLGVTRERGVELIQKSVQLAKQAKEQYLSEIGSEAESALPLIMGSIGPYGAYLHDGSEYTGNYADKMSKEELRAWHKTRIEICLAAGVDGLALETLPCLMEAEAVTELVLDNFPDAKFWVSLQCMDEKHMASGENFAEAALSLWRLVQSRKAENRLLGIGLNCVNPLFVTPLLSSLTKVAGSDRIPLVVYSNRGEIYDVEQGDWTGTGEEVVKFVPEWIQLGVRIVGGCCRVYPTDVLAIRKYVDGLNIKP

[Multiple Choices]
A. 2.1.1.393
B. 2.7.8.43
C. 2.1.1.395
D. 2.1.1.5
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

> The exact matched sequence is annotated as betaine-homocysteine S-methyltransferase with EC 2.1.1.5, and its annotated reaction is consistent with that EC. The annotation is transferred by similarity from UniProtKB Q93088, rather than shown here as direct experimental evidence for this sequence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone does not provide a clear, general biological argument that distinguishes EC 2.1.1.5 from the other specific EC choices.


**Missing item-specific fact**

> The protein's identity and catalytic activity as betaine-homocysteine S-methyltransferase, or an equivalent protein-specific functional annotation.


**Reason**

> Choosing the exact EC requires knowing the function assigned to this particular protein; recognizing the sequence or recalling its database entry would be lookup or memorization, not reasoning from the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched-sequence annotation supports choice D; the supplied evidence does not support another listed option.


### Important caveats

- The EC and catalytic-activity annotations cite evidence transferred from Q93088 (ECO:0000250); the excerpts do not establish direct experimental characterization of the Drosophila sequence.
- The sequence matches both the current UniProt entry and the historical sequence-version record, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone does not provide a clear, general biological argument that distinguishes EC 2.1.1.5 from the other specific EC choices.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's identity and catalytic activity as betaine-homocysteine S-methyltransferase, or an equivalent protein-specific functional annotation.",
    "reason": "Choosing the exact EC requires knowing the function assigned to this particular protein; recognizing the sequence or recalling its database entry would be lookup or memorization, not reasoning from the supplied input."
  },
  "case_id": "EC_number_0136",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact matched sequence is annotated as betaine-homocysteine S-methyltransferase with EC 2.1.1.5, and its annotated reaction is consistent with that EC. The annotation is transferred by similarity from UniProtKB Q93088, rather than shown here as direct experimental evidence for this sequence."
  },
  "important_caveats": [
    "The EC and catalytic-activity annotations cite evidence transferred from Q93088 (ECO:0000250); the excerpts do not establish direct experimental characterization of the Drosophila sequence.",
    "The sequence matches both the current UniProt entry and the historical sequence-version record, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched-sequence annotation supports choice D; the supplied evidence does not support another listed option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0136",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact matched sequence is annotated as betaine-homocysteine S-methyltransferase with EC 2.1.1.5, and its annotated reaction is consistent with that EC. The annotation is transferred by similarity from UniProtKB Q93088, rather than shown here as direct experimental evidence for this sequence.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone does not provide a clear, general biological argument that distinguishes EC 2.1.1.5 from the other specific EC choices.",
    "missing_item_specific_fact": "The protein's identity and catalytic activity as betaine-homocysteine S-methyltransferase, or an equivalent protein-specific functional annotation.",
    "reason": "Choosing the exact EC requires knowing the function assigned to this particular protein; recognizing the sequence or recalling its database entry would be lookup or memorization, not reasoning from the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched-sequence annotation supports choice D; the supplied evidence does not support another listed option."
  },
  "important_caveats": [
    "The EC and catalytic-activity annotations cite evidence transferred from Q93088 (ECO:0000250); the excerpts do not establish direct experimental characterization of the Drosophila sequence.",
    "The sequence matches both the current UniProt entry and the historical sequence-version record, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The benchmark sequence matches UniProt entry Q9VJ31 (BHMT_DROME, Drosophila melanogaster) exactly (SHA-256 confirmed). The UniProt annotation assigns EC 2.1.1.5 (Betaine-homocysteine S-methyltransferase) with catalytic activity L-homocysteine + glycine betaine = N,N-dimethylglycine + L-methionine. The evidence code is ECO:0000250 (similarity-based inference from human BHMT Q93088), not direct experimental characterization of the Drosophila protein, but the annotation is consistent and the sequence identity is confirmed.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One could note the zinc-binding motif (Cys-Gly in 'CGGFSSQ') and ~331-aa length, which are consistent with BHMT (a rare zinc-dependent, non-SAM methyltransferase). This might weakly favor a methyltransferase over the phosphotransferase option B. However, distinguishing EC 2.1.1.5 from the other two methyltransferase options (2.1.1.393 and 2.1.1.395) requires knowing the specific reactions these obscure EC numbers catalyze, which is not derivable from general sequence reasoning.


**Missing item-specific fact**

> The specific chemical reactions catalyzed by EC 2.1.1.393 and EC 2.1.1.395, and the structural/sequence signatures that would exclude them in favor of BHMT (EC 2.1.1.5), are not available from the sequence alone. Recognition of this as BHMT or knowledge of what the distractor EC numbers represent is required.


**Reason**

> The question presents three methyltransferase EC numbers (A, C, D) and one phosphotransferase (B). While B can be eliminated by noting the absence of phosphotransferase motifs, distinguishing among three methyltransferases requires either recognizing the specific protein from its sequence (memorization) or knowing the exact reactions of the obscure EC numbers 2.1.1.393 and 2.1.1.395 (lookup). General biological reasoning about methyltransferase families does not resolve the choice among these three specific sub-subclass entries.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The annotation unambiguously assigns EC 2.1.1.5 to this sequence. Option B (phosphotransferase, EC 2.7) is clearly in a different EC class. Options A and C are methyltransferases but correspond to different specific reactions. There is one correct answer per the database annotation; the difficulty lies in the model's ability to identify it, not in genuine ambiguity.


### Important caveats

- The EC annotation carries evidence code ECO:0000250 (similarity-based transfer from human BHMT Q93088), not direct experimental validation of the Drosophila protein's catalytic activity.
- The UniProt entry was first publicly released on 2025-02-05; the benchmark construction date is unknown, but the sequence has been unchanged since 2000-05-01.
- EC 2.1.1.393 and 2.1.1.395 are highly specific and obscure EC numbers; without looking up their definitions, a model cannot rule them out by reasoning from the sequence alone.
- The reviewer-only evidence (accession Q9VJ31) was not available to the evaluated model; the model must work from the raw sequence and the four EC-number choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One could note the zinc-binding motif (Cys-Gly in 'CGGFSSQ') and ~331-aa length, which are consistent with BHMT (a rare zinc-dependent, non-SAM methyltransferase). This might weakly favor a methyltransferase over the phosphotransferase option B. However, distinguishing EC 2.1.1.5 from the other two methyltransferase options (2.1.1.393 and 2.1.1.395) requires knowing the specific reactions these obscure EC numbers catalyze, which is not derivable from general sequence reasoning.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific chemical reactions catalyzed by EC 2.1.1.393 and EC 2.1.1.395, and the structural/sequence signatures that would exclude them in favor of BHMT (EC 2.1.1.5), are not available from the sequence alone. Recognition of this as BHMT or knowledge of what the distractor EC numbers represent is required.",
    "reason": "The question presents three methyltransferase EC numbers (A, C, D) and one phosphotransferase (B). While B can be eliminated by noting the absence of phosphotransferase motifs, distinguishing among three methyltransferases requires either recognizing the specific protein from its sequence (memorization) or knowing the exact reactions of the obscure EC numbers 2.1.1.393 and 2.1.1.395 (lookup). General biological reasoning about methyltransferase families does not resolve the choice among these three specific sub-subclass entries."
  },
  "case_id": "EC_number_0136",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The benchmark sequence matches UniProt entry Q9VJ31 (BHMT_DROME, Drosophila melanogaster) exactly (SHA-256 confirmed). The UniProt annotation assigns EC 2.1.1.5 (Betaine-homocysteine S-methyltransferase) with catalytic activity L-homocysteine + glycine betaine = N,N-dimethylglycine + L-methionine. The evidence code is ECO:0000250 (similarity-based inference from human BHMT Q93088), not direct experimental characterization of the Drosophila protein, but the annotation is consistent and the sequence identity is confirmed."
  },
  "important_caveats": [
    "The EC annotation carries evidence code ECO:0000250 (similarity-based transfer from human BHMT Q93088), not direct experimental validation of the Drosophila protein's catalytic activity.",
    "The UniProt entry was first publicly released on 2025-02-05; the benchmark construction date is unknown, but the sequence has been unchanged since 2000-05-01.",
    "EC 2.1.1.393 and 2.1.1.395 are highly specific and obscure EC numbers; without looking up their definitions, a model cannot rule them out by reasoning from the sequence alone.",
    "The reviewer-only evidence (accession Q9VJ31) was not available to the evaluated model; the model must work from the raw sequence and the four EC-number choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The annotation unambiguously assigns EC 2.1.1.5 to this sequence. Option B (phosphotransferase, EC 2.7) is clearly in a different EC class. Options A and C are methyltransferases but correspond to different specific reactions. There is one correct answer per the database annotation; the difficulty lies in the model's ability to identify it, not in genuine ambiguity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0136",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The benchmark sequence matches UniProt entry Q9VJ31 (BHMT_DROME, Drosophila melanogaster) exactly (SHA-256 confirmed). The UniProt annotation assigns EC 2.1.1.5 (Betaine-homocysteine S-methyltransferase) with catalytic activity L-homocysteine + glycine betaine = N,N-dimethylglycine + L-methionine. The evidence code is ECO:0000250 (similarity-based inference from human BHMT Q93088), not direct experimental characterization of the Drosophila protein, but the annotation is consistent and the sequence identity is confirmed.",
    "evidence_ids": ["C4", "C5", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One could note the zinc-binding motif (Cys-Gly in 'CGGFSSQ') and ~331-aa length, which are consistent with BHMT (a rare zinc-dependent, non-SAM methyltransferase). This might weakly favor a methyltransferase over the phosphotransferase option B. However, distinguishing EC 2.1.1.5 from the other two methyltransferase options (2.1.1.393 and 2.1.1.395) requires knowing the specific reactions these obscure EC numbers catalyze, which is not derivable from general sequence reasoning.",
    "missing_item_specific_fact": "The specific chemical reactions catalyzed by EC 2.1.1.393 and EC 2.1.1.395, and the structural/sequence signatures that would exclude them in favor of BHMT (EC 2.1.1.5), are not available from the sequence alone. Recognition of this as BHMT or knowledge of what the distractor EC numbers represent is required.",
    "reason": "The question presents three methyltransferase EC numbers (A, C, D) and one phosphotransferase (B). While B can be eliminated by noting the absence of phosphotransferase motifs, distinguishing among three methyltransferases requires either recognizing the specific protein from its sequence (memorization) or knowing the exact reactions of the obscure EC numbers 2.1.1.393 and 2.1.1.395 (lookup). General biological reasoning about methyltransferase families does not resolve the choice among these three specific sub-subclass entries."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The annotation unambiguously assigns EC 2.1.1.5 to this sequence. Option B (phosphotransferase, EC 2.7) is clearly in a different EC class. Options A and C are methyltransferases but correspond to different specific reactions. There is one correct answer per the database annotation; the difficulty lies in the model's ability to identify it, not in genuine ambiguity."
  },
  "important_caveats": [
    "The EC annotation carries evidence code ECO:0000250 (similarity-based transfer from human BHMT Q93088), not direct experimental validation of the Drosophila protein's catalytic activity.",
    "The UniProt entry was first publicly released on 2025-02-05; the benchmark construction date is unknown, but the sequence has been unchanged since 2000-05-01.",
    "EC 2.1.1.393 and 2.1.1.395 are highly specific and obscure EC numbers; without looking up their definitions, a model cannot rule them out by reasoning from the sequence alone.",
    "The reviewer-only evidence (accession Q9VJ31) was not available to the evaluated model; the model must work from the raw sequence and the four EC-number choices."
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

**Accession:** `Q9VJ31` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 179. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ31.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:22.549548+00:00.  

```json
"Q9VJ31"
```

Source SHA-256: `d9e7ae75552fc6f8c0b82b0818c27c06ccc38e4edbafe213c0d1073bb6cc0f26`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ31.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:22.549548+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q93088","source":"UniProtKB"}],"value":"2.1.1.5"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"FBgn0032727","source":"FlyBase"}],"value":"Betaine-homocysteine S-methyltransferase"}}}
```

Source SHA-256: `d9e7ae75552fc6f8c0b82b0818c27c06ccc38e4edbafe213c0d1073bb6cc0f26`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ31.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:22.549548+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"Q93088","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:22337"}}],"reaction":{"ecNumber":"2.1.1.5","evidences":[{"evidenceCode":"ECO:0000250","id":"Q93088","source":"UniProtKB"}],"name":"L-homocysteine + glycine betaine = N,N-dimethylglycine + L-methionine","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:22336"},{"database":"ChEBI","id":"CHEBI:17750"},{"database":"ChEBI","id":"CHEBI:57844"},{"database":"ChEBI","id":"CHEBI:58199"},{"database":"ChEBI","id":"CHEBI:58251"}]}}
```

Source SHA-256: `d9e7ae75552fc6f8c0b82b0818c27c06ccc38e4edbafe213c0d1073bb6cc0f26`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VJ31?format=txt&versions=179)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 179 / 1.  
**Retrieved:** 2026-11-02T04:33:24.773902+00:00.  

```text
ID   BHMT_DROME              Reviewed;         331 AA.
AC   Q9VJ31;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-MAY-2000, sequence version 1.
DT   28-JAN-2026, entry version 179.
DE   RecName: Full=Betaine-homocysteine S-methyltransferase {ECO:0000312|FlyBase:FBgn0032727};
DE            EC=2.1.1.5 {ECO:0000250|UniProtKB:Q93088};
GN   Name=Bhmt {ECO:0000312|FlyBase:FBgn0032727};
GN   ORFNames=CG10623 {ECO:0000312|FlyBase:FBgn0032727};
OS   Drosophila melanogaster (Fruit fly).
OC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;
OC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;
OC   Drosophilidae; Drosophila; Sophophora.
OX   NCBI_TaxID=7227 {ECO:0000312|Proteomes:UP000000803};
```

Source SHA-256: `0137a301084f29c9ad250967ed17fe809b86d9f9bf9482cf841c048eb041de62`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VJ31?format=txt&versions=179)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 179 / 1.  
**Retrieved:** 2026-11-02T04:33:24.773902+00:00.  

```text
DE   RecName: Full=Betaine-homocysteine S-methyltransferase {ECO:0000312|FlyBase:FBgn0032727};
DE            EC=2.1.1.5 {ECO:0000250|UniProtKB:Q93088};
```

Source SHA-256: `0137a301084f29c9ad250967ed17fe809b86d9f9bf9482cf841c048eb041de62`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VJ31?format=txt&versions=179)  
**Locator:** `lines 109-115`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 179 / 1.  
**Retrieved:** 2026-11-02T04:33:24.773902+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-homocysteine + glycine betaine = N,N-dimethylglycine + L-
CC         methionine; Xref=Rhea:RHEA:22336, ChEBI:CHEBI:17750,
CC         ChEBI:CHEBI:57844, ChEBI:CHEBI:58199, ChEBI:CHEBI:58251; EC=2.1.1.5;
CC         Evidence={ECO:0000250|UniProtKB:Q93088};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:22337;
CC         Evidence={ECO:0000250|UniProtKB:Q93088};
```

Source SHA-256: `0137a301084f29c9ad250967ed17fe809b86d9f9bf9482cf841c048eb041de62`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 136. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
