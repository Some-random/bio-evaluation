# catalytic_activity_0091

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **C** — L-arginyl-&#91;protein&#93; + 2-oxoglutarate + O2 = (3R)-3-hydroxy-L-arginyl-&#91;protein&#93; + succinate + CO2

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MDSEFLELTQLLPRWVDLENVVRGEVEARYILKRAADHLANLRSGGDSGAEETGYLVGALVDRNWERIHTGHFSQVPLVTRKIYAIACCFKIFFLLLESTSPAQKDACSEILDEAQLLGCMEDWSELKVALMDYLDKDGAVALNSAPLPTLEPLTRVTSNCDIPQLDAPSLEEFQTKCFEAGQPTLLLNTIQHWPALHKWLDLNYLLQVAGNRTVPIEIGSNYASDEWSQQLVKIRDFLSRQFGKEPSKAGQNIEYLAQHELFAQIPALKEDISIPDYCTISNEDTPGAVDIKAWLGPAGTVSPMHYDPKHNLLCQVFGSKRIILAAPADTDNLYPHDSEFLANTARIDAAQLDPETYPLVAKVKFYQLLLQPGDCLYMPPKWWHYVRSEAPSFSVSFWWE

[Multiple Choices]
A. Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.
B. L-methionine(in) = L-methionine(out)
C. L-arginyl-[protein] + 2-oxoglutarate + O2 = (3R)-3-hydroxy-L-arginyl-[protein] + succinate + CO2
D. a 5'-end (5'-triphosphoguanosine)-adenylyl-adenylyl-cytidylyl-adenosine in mRNA + 2 S-adenosyl-L-methionine = a 5'-end (N(7)-methyl 5'-triphosphoguanosine)-(2'-O-methyladenylyl)-adenylyl-cytidylyl-adenosine in mRNA + 2 S-adenosyl-L-homocysteine + H(+)
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

> The sequence exactly matches UniProt Q9W0M3, whose current and historical annotations assign the reaction in C. That assignment is transferred by similarity from UniProtKB:Q8N371 (ECO:0000250), so it supports the key as a computational annotation, not as direct experimental evidence for this sequence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a JmjC-like HxD...H catalytic motif consistent with a Fe(II)/2-oxoglutarate-dependent oxygenase. Of the choices, C is the oxygenase hydroxylation reaction; A is glycoside hydrolysis, B is transport, and D is SAM-dependent RNA methylation.


**Missing item-specific fact**

> The motif alone does not establish the precise arginyl-protein substrate or hydroxylation site; those details are supported by the protein-specific homology annotation rather than independently demonstrated in the supplied input.


**Reason**

> The sequence and choice set give a meaningful class-level basis to distinguish C from the alternatives, although the exact substrate specificity is not deducible from the motif alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, only C matches the sequence's JmjC/2-oxoglutarate oxygenase features.


### Important caveats

- The reviewer-only database record matches the supplied sequence, but the author’s exact source snapshot is unknown.
- The cited UniProt reaction assignment is transferred by similarity; the supplied evidence does not establish direct experimental validation for this sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a JmjC-like HxD...H catalytic motif consistent with a Fe(II)/2-oxoglutarate-dependent oxygenase. Of the choices, C is the oxygenase hydroxylation reaction; A is glycoside hydrolysis, B is transport, and D is SAM-dependent RNA methylation.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The motif alone does not establish the precise arginyl-protein substrate or hydroxylation site; those details are supported by the protein-specific homology annotation rather than independently demonstrated in the supplied input.",
    "reason": "The sequence and choice set give a meaningful class-level basis to distinguish C from the alternatives, although the exact substrate specificity is not deducible from the motif alone."
  },
  "case_id": "catalytic_activity_0091",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches UniProt Q9W0M3, whose current and historical annotations assign the reaction in C. That assignment is transferred by similarity from UniProtKB:Q8N371 (ECO:0000250), so it supports the key as a computational annotation, not as direct experimental evidence for this sequence."
  },
  "important_caveats": [
    "The reviewer-only database record matches the supplied sequence, but the author’s exact source snapshot is unknown.",
    "The cited UniProt reaction assignment is transferred by similarity; the supplied evidence does not establish direct experimental validation for this sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, only C matches the sequence's JmjC/2-oxoglutarate oxygenase features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0091",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches UniProt Q9W0M3, whose current and historical annotations assign the reaction in C. That assignment is transferred by similarity from UniProtKB:Q8N371 (ECO:0000250), so it supports the key as a computational annotation, not as direct experimental evidence for this sequence.",
    "evidence_ids": ["C1", "C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a JmjC-like HxD...H catalytic motif consistent with a Fe(II)/2-oxoglutarate-dependent oxygenase. Of the choices, C is the oxygenase hydroxylation reaction; A is glycoside hydrolysis, B is transport, and D is SAM-dependent RNA methylation.",
    "missing_item_specific_fact": "The motif alone does not establish the precise arginyl-protein substrate or hydroxylation site; those details are supported by the protein-specific homology annotation rather than independently demonstrated in the supplied input.",
    "reason": "The sequence and choice set give a meaningful class-level basis to distinguish C from the alternatives, although the exact substrate specificity is not deducible from the motif alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, only C matches the sequence's JmjC/2-oxoglutarate oxygenase features."
  },
  "important_caveats": [
    "The reviewer-only database record matches the supplied sequence, but the author’s exact source snapshot is unknown.",
    "The cited UniProt reaction assignment is transferred by similarity; the supplied evidence does not establish direct experimental validation for this sequence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt Q9W0M3 (KDM8_DROME, Jumonji C domain-containing protein 5 from Drosophila melanogaster) exactly (401 aa, SHA256 match). The UniProt catalytic activity annotation explicitly states: L-arginyl-&#91;protein&#93; + 2-oxoglutarate + O2 = (3R)-3-hydroxy-L-arginyl-&#91;protein&#93; + succinate + CO2 (EC 1.14.11.73), matching Choice C verbatim. However, the evidence code is ECO:0000250 (protein similarity), indicating the annotation is transferred from the human ortholog Q8N371 rather than established by direct experimentation on the Drosophila protein.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein contains a Jumonji C (JmjC) domain, identifiable by the conserved HxD/E…H facial triad for Fe(II) coordination and the characteristic ~150-residue fold. JmjC-domain proteins are a well-characterized superfamily of Fe(II)/2-oxoglutarate-dependent dioxygenases. Among the four choices, only Choice C involves 2-oxoglutarate and O2 as co-substrates, which is the hallmark mechanistic signature of JmjC-domain catalysis. Choices A (glycoside hydrolase), B (amino acid transporter), and D (mRNA capping methyltransferase) are mechanistically incompatible with a JmjC-domain dioxygenase. Thus, recognizing the JmjC domain from sequence and knowing its 2-OG/O2-dependent dioxygenase mechanism suffices to select C.


**Missing item-specific fact**

> The specific substrate being arginyl-&#91;protein&#93; (rather than a methylated lysine, which is the more common JmjC substrate) is a protein-specific fact about JMJD5/KDM8. However, since only one option uses 2-OG/O2, this specificity is not needed to distinguish among the given choices.


**Reason**

> The JmjC domain → 2-OG-dependent dioxygenase link is general biological knowledge that eliminates A, B, and D mechanistically. The correct answer is reachable without memorizing the exact UniProt entry for Q9W0M3.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent fundamentally different enzyme classes (hydrolase, transporter, dioxygenase, methyltransferase). A JmjC-domain protein is mechanistically incompatible with A, B, and D. No ambiguity in distinguishing the correct answer.


### Important caveats

- The UniProt catalytic activity annotation is based on protein similarity (ECO:0000250) to human JMJD5 (Q8N371), not direct experimental evidence on the Drosophila protein.
- The reviewer-only evidence was absent from the evaluated model input; the model must rely on sequence recognition and general biochemical knowledge.
- The specific arginine-hydroxylation activity (as opposed to the more typical lysine demethylation by other JmjC proteins) is a distinguishing feature of JMJD5/KDM8, but this specificity is not required to select the correct option among the four given.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein contains a Jumonji C (JmjC) domain, identifiable by the conserved HxD/E…H facial triad for Fe(II) coordination and the characteristic ~150-residue fold. JmjC-domain proteins are a well-characterized superfamily of Fe(II)/2-oxoglutarate-dependent dioxygenases. Among the four choices, only Choice C involves 2-oxoglutarate and O2 as co-substrates, which is the hallmark mechanistic signature of JmjC-domain catalysis. Choices A (glycoside hydrolase), B (amino acid transporter), and D (mRNA capping methyltransferase) are mechanistically incompatible with a JmjC-domain dioxygenase. Thus, recognizing the JmjC domain from sequence and knowing its 2-OG/O2-dependent dioxygenase mechanism suffices to select C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific substrate being arginyl-[protein] (rather than a methylated lysine, which is the more common JmjC substrate) is a protein-specific fact about JMJD5/KDM8. However, since only one option uses 2-OG/O2, this specificity is not needed to distinguish among the given choices.",
    "reason": "The JmjC domain → 2-OG-dependent dioxygenase link is general biological knowledge that eliminates A, B, and D mechanistically. The correct answer is reachable without memorizing the exact UniProt entry for Q9W0M3."
  },
  "case_id": "catalytic_activity_0091",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q9W0M3 (KDM8_DROME, Jumonji C domain-containing protein 5 from Drosophila melanogaster) exactly (401 aa, SHA256 match). The UniProt catalytic activity annotation explicitly states: L-arginyl-[protein] + 2-oxoglutarate + O2 = (3R)-3-hydroxy-L-arginyl-[protein] + succinate + CO2 (EC 1.14.11.73), matching Choice C verbatim. However, the evidence code is ECO:0000250 (protein similarity), indicating the annotation is transferred from the human ortholog Q8N371 rather than established by direct experimentation on the Drosophila protein."
  },
  "important_caveats": [
    "The UniProt catalytic activity annotation is based on protein similarity (ECO:0000250) to human JMJD5 (Q8N371), not direct experimental evidence on the Drosophila protein.",
    "The reviewer-only evidence was absent from the evaluated model input; the model must rely on sequence recognition and general biochemical knowledge.",
    "The specific arginine-hydroxylation activity (as opposed to the more typical lysine demethylation by other JmjC proteins) is a distinguishing feature of JMJD5/KDM8, but this specificity is not required to select the correct option among the four given."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent fundamentally different enzyme classes (hydrolase, transporter, dioxygenase, methyltransferase). A JmjC-domain protein is mechanistically incompatible with A, B, and D. No ambiguity in distinguishing the correct answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0091",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q9W0M3 (KDM8_DROME, Jumonji C domain-containing protein 5 from Drosophila melanogaster) exactly (401 aa, SHA256 match). The UniProt catalytic activity annotation explicitly states: L-arginyl-[protein] + 2-oxoglutarate + O2 = (3R)-3-hydroxy-L-arginyl-[protein] + succinate + CO2 (EC 1.14.11.73), matching Choice C verbatim. However, the evidence code is ECO:0000250 (protein similarity), indicating the annotation is transferred from the human ortholog Q8N371 rather than established by direct experimentation on the Drosophila protein.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein contains a Jumonji C (JmjC) domain, identifiable by the conserved HxD/E…H facial triad for Fe(II) coordination and the characteristic ~150-residue fold. JmjC-domain proteins are a well-characterized superfamily of Fe(II)/2-oxoglutarate-dependent dioxygenases. Among the four choices, only Choice C involves 2-oxoglutarate and O2 as co-substrates, which is the hallmark mechanistic signature of JmjC-domain catalysis. Choices A (glycoside hydrolase), B (amino acid transporter), and D (mRNA capping methyltransferase) are mechanistically incompatible with a JmjC-domain dioxygenase. Thus, recognizing the JmjC domain from sequence and knowing its 2-OG/O2-dependent dioxygenase mechanism suffices to select C.",
    "missing_item_specific_fact": "The specific substrate being arginyl-[protein] (rather than a methylated lysine, which is the more common JmjC substrate) is a protein-specific fact about JMJD5/KDM8. However, since only one option uses 2-OG/O2, this specificity is not needed to distinguish among the given choices.",
    "reason": "The JmjC domain → 2-OG-dependent dioxygenase link is general biological knowledge that eliminates A, B, and D mechanistically. The correct answer is reachable without memorizing the exact UniProt entry for Q9W0M3."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent fundamentally different enzyme classes (hydrolase, transporter, dioxygenase, methyltransferase). A JmjC-domain protein is mechanistically incompatible with A, B, and D. No ambiguity in distinguishing the correct answer."
  },
  "important_caveats": [
    "The UniProt catalytic activity annotation is based on protein similarity (ECO:0000250) to human JMJD5 (Q8N371), not direct experimental evidence on the Drosophila protein.",
    "The reviewer-only evidence was absent from the evaluated model input; the model must rely on sequence recognition and general biochemical knowledge.",
    "The specific arginine-hydroxylation activity (as opposed to the more typical lysine demethylation by other JmjC proteins) is a distinguishing feature of JMJD5/KDM8, but this specificity is not required to select the correct option among the four given."
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

**Accession:** `Q9W0M3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 170. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W0M3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:43.683489+00:00.  

```json
"Q9W0M3"
```

Source SHA-256: `1ea6b03bc8ddb55213f5b2d1a92a5f5660c411ba7d6b4ad94233da43076eafe1`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W0M3.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:43.683489+00:00.  

```json
{"commonName":"Fruit fly","evidences":[{"evidenceCode":"ECO:0000312","id":"UP000000803","source":"Proteomes"}],"lineage":["Eukaryota","Metazoa","Ecdysozoa","Arthropoda","Altocrustacea","Allotriocarida","Hexapoda","Insecta","Pterygota","Neoptera","Eumetabola","Endopterygota","Aparaglossata","Panorpida","Diptera","Brachycera","Muscomorpha","Ephydroidea","Drosophilidae","Drosophila","Sophophora"],"scientificName":"Drosophila melanogaster","taxonId":7227}
```

Source SHA-256: `1ea6b03bc8ddb55213f5b2d1a92a5f5660c411ba7d6b4ad94233da43076eafe1`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W0M3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:43.683489+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Lysine-specific demethylase 8"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8N371","source":"UniProtKB"}],"value":"1.14.11.73"},{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8N371","source":"UniProtKB"}],"value":"3.4.-.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Jumonji C domain-containing protein 5"}}}
```

Source SHA-256: `1ea6b03bc8ddb55213f5b2d1a92a5f5660c411ba7d6b4ad94233da43076eafe1`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W0M3.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:43.683489+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"1.14.11.73","evidences":[{"evidenceCode":"ECO:0000250","id":"Q8N371","source":"UniProtKB"}],"name":"L-arginyl-[protein] + 2-oxoglutarate + O2 = (3R)-3-hydroxy-L-arginyl-[protein] + succinate + CO2","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:56744"},{"database":"Rhea","id":"RHEA-COMP:10532"},{"database":"Rhea","id":"RHEA-COMP:14712"},{"database":"ChEBI","id":"CHEBI:15379"},{"database":"ChEBI","id":"CHEBI:16526"},{"database":"ChEBI","id":"CHEBI:16810"},{"database":"ChEBI","id":"CHEBI:29965"},{"database":"ChEBI","id":"CHEBI:30031"},{"database":"ChEBI","id":"CHEBI:78294"}]}}
```

Source SHA-256: `1ea6b03bc8ddb55213f5b2d1a92a5f5660c411ba7d6b4ad94233da43076eafe1`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W0M3?format=txt&versions=170)  
**Locator:** `lines 1-17`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 170 / 2.  
**Retrieved:** 2026-11-02T04:33:45.948211+00:00.  

```text
ID   KDM8_DROME              Reviewed;         401 AA.
AC   Q9W0M3; M9PDS1; Q86NX2;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   30-NOV-2010, sequence version 2.
DT   28-JAN-2026, entry version 170.
DE   RecName: Full=Jumonji C domain-containing protein 5 {ECO:0000305};
DE            EC=1.14.11.73 {ECO:0000250|UniProtKB:Q8N371};
DE            EC=3.4.-.- {ECO:0000250|UniProtKB:Q8N371};
DE   AltName: Full=Lysine-specific demethylase 8 {ECO:0000305};
GN   Name=JMJD5 {ECO:0000312|FlyBase:FBgn0035166};
GN   Synonyms=Kdm8 {ECO:0000312|FlyBase:FBgn0035166};
GN   ORFNames=CG13902 {ECO:0000312|FlyBase:FBgn0035166};
OS   Drosophila melanogaster (Fruit fly).
OC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;
OC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;
OC   Drosophilidae; Drosophila; Sophophora.
OX   NCBI_TaxID=7227 {ECO:0000312|Proteomes:UP000000803};
```

Source SHA-256: `45e70668e7a96138303d865036cba4c2edb7da0e5634453cb9fbab186acc3750`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W0M3?format=txt&versions=170)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 170 / 2.  
**Retrieved:** 2026-11-02T04:33:45.948211+00:00.  

```text
DE   RecName: Full=Jumonji C domain-containing protein 5 {ECO:0000305};
DE            EC=1.14.11.73 {ECO:0000250|UniProtKB:Q8N371};
DE            EC=3.4.-.- {ECO:0000250|UniProtKB:Q8N371};
DE   AltName: Full=Lysine-specific demethylase 8 {ECO:0000305};
```

Source SHA-256: `45e70668e7a96138303d865036cba4c2edb7da0e5634453cb9fbab186acc3750`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W0M3?format=txt&versions=170)  
**Locator:** `lines 100-106`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 170 / 2.  
**Retrieved:** 2026-11-02T04:33:45.948211+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-arginyl-[protein] + 2-oxoglutarate + O2 = (3R)-3-hydroxy-L-
CC         arginyl-[protein] + succinate + CO2; Xref=Rhea:RHEA:56744, Rhea:RHEA-
CC         COMP:10532, Rhea:RHEA-COMP:14712, ChEBI:CHEBI:15379,
CC         ChEBI:CHEBI:16526, ChEBI:CHEBI:16810, ChEBI:CHEBI:29965,
CC         ChEBI:CHEBI:30031, ChEBI:CHEBI:78294; EC=1.14.11.73;
CC         Evidence={ECO:0000250|UniProtKB:Q8N371};
```

Source SHA-256: `45e70668e7a96138303d865036cba4c2edb7da0e5634453cb9fbab186acc3750`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 91. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
