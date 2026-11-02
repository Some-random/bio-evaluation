# catalytic_activity_0055

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **A** — N(6),N(6)-dimethyl-L-lysyl(9)-&#91;histone H3&#93; + 2 2-oxoglutarate + 2 O2 = L-lysyl(9)-&#91;histone H3&#93; + 2 formaldehyde + 2 succinate + 2 CO2

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSQKELAALVATRTSRKRTISSTSFSISTRTDPKSIIEIHIFNDSLPIKRACCEVENPTLKAEQRVQQEEESLGQVPPLTEEEQQRHDEFRNSGSIFLQDLPCFKLQQAQPIAGSSPIPKCRECRRRNLATTEGEPSSVSDVYCRFYEFRRLQFNENGELCVVGFPNPYSEPSPEDIAIWQPDKNTPPTSGYMDIQVCRYILLHAGDQFCYIWHQEAEALSLHQNTDGTIAWKKAVKGTREICDVCDTTLFNYHWTCRKCGFGVCLDCVKDRKEGLRLRRAENAAQKGCDEYHWLLCSDPSGPQEHVLTELMLTQIIAGDALNVLGRLLHEVRTLWQVPQVCGCLLSKQAIEDAQSKEVIQDMIKESQLKQHTSYSSLASEQKVHQQQRLDQLHATKLEFARELGVDYVPGRVWTKETLGKDPITTAFDNLKHINFLRKGLAGLRRFLPPRTMTFAYSTQLAPGVPHEFLCDGRLLRLTDAMHPDNRVLFQEVWKCGQPVMISEVARSLNLDLWHPQAFCRDFGDKPNDLINCLNGNLVPNQPMRHFWEGFQCMTKRLPDAYGKPMLLKLKDWPPGDDFAEILPTRFADLMKGLPMPEYTLRTGNLNIASCLPKMFVPPDLGPKMYNAYGSALHPDKGTTNLHLDISDAVNIMVYVGIPQDGDTRPQMAATQKAIEIGGCDYITRARCQSPDVLPGALWHIFPARDADKIRDLLNRVTLEKGFRLEPDHDPIHDQNWYLDDKLRARLFKEYGVEGHPIVQCLGDAVFIPAGAPHQVQNLHNCIKVAEDFVSPENITHCYHLTHEFRRLSHSHTNHEDKLQIKNIIYHAIKDCCTILTRAVDERLNAELTKLNAD

[Multiple Choices]
A. N(6),N(6)-dimethyl-L-lysyl(9)-[histone H3] + 2 2-oxoglutarate + 2 O2 = L-lysyl(9)-[histone H3] + 2 formaldehyde + 2 succinate + 2 CO2
B. 3-desmethyl okaramine B + S-adenosyl-L-methionine = okaramine B + S-adenosyl-L-homocysteine + H(+)
C. ATP + H2O + xenobioticSide 1 = ADP + phosphate + xenobioticSide 2.
D. O-phospho-L-seryl-[protein] + H2O = L-seryl-[protein] + phosphate
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

> The sequence matches the Drosophila KDM3 entry, whose UniProt annotation assigns the reaction in choice A. That catalytic-activity annotation is transferred by similarity from Q9Y4C1, so it supports A as an annotation-based inference rather than establishing direct experimental evidence for this exact protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices describe different chemistries, and recognizing a 2-oxoglutarate-dependent demethylase would favor A over the methyltransferase, ATP-hydrolysis, and phosphatase options. But the sequence and choices alone do not establish this protein's specific histone H3 Lys9 substrate reaction.


**Missing item-specific fact**

> The protein-specific KDM3 functional annotation, including its assigned histone H3 Lys9 demethylation reaction, is needed to select A with confidence.


**Reason**

> The evidence supporting the key depends on a sequence-matched database annotation transferred from a homolog; that annotation was not supplied in the question. Inferring a broad enzyme class from sequence motifs would not by itself establish the precise substrate and reaction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied annotation supports A, and the choices describe distinct reaction types; no alternative is supported by the available evidence.


### Important caveats

- The sequence match is exact to the database record, but the cited catalytic-activity evidence is by similarity to Q9Y4C1, not direct experimental evidence for this Drosophila protein.
- The author's source snapshot is unknown; both the historical and current matched records contain the A annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices describe different chemistries, and recognizing a 2-oxoglutarate-dependent demethylase would favor A over the methyltransferase, ATP-hydrolysis, and phosphatase options. But the sequence and choices alone do not establish this protein's specific histone H3 Lys9 substrate reaction.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific KDM3 functional annotation, including its assigned histone H3 Lys9 demethylation reaction, is needed to select A with confidence.",
    "reason": "The evidence supporting the key depends on a sequence-matched database annotation transferred from a homolog; that annotation was not supplied in the question. Inferring a broad enzyme class from sequence motifs would not by itself establish the precise substrate and reaction."
  },
  "case_id": "catalytic_activity_0055",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the Drosophila KDM3 entry, whose UniProt annotation assigns the reaction in choice A. That catalytic-activity annotation is transferred by similarity from Q9Y4C1, so it supports A as an annotation-based inference rather than establishing direct experimental evidence for this exact protein."
  },
  "important_caveats": [
    "The sequence match is exact to the database record, but the cited catalytic-activity evidence is by similarity to Q9Y4C1, not direct experimental evidence for this Drosophila protein.",
    "The author's source snapshot is unknown; both the historical and current matched records contain the A annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied annotation supports A, and the choices describe distinct reaction types; no alternative is supported by the available evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0055",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the Drosophila KDM3 entry, whose UniProt annotation assigns the reaction in choice A. That catalytic-activity annotation is transferred by similarity from Q9Y4C1, so it supports A as an annotation-based inference rather than establishing direct experimental evidence for this exact protein.",
    "evidence_ids": ["C1", "C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices describe different chemistries, and recognizing a 2-oxoglutarate-dependent demethylase would favor A over the methyltransferase, ATP-hydrolysis, and phosphatase options. But the sequence and choices alone do not establish this protein's specific histone H3 Lys9 substrate reaction.",
    "missing_item_specific_fact": "The protein-specific KDM3 functional annotation, including its assigned histone H3 Lys9 demethylation reaction, is needed to select A with confidence.",
    "reason": "The evidence supporting the key depends on a sequence-matched database annotation transferred from a homolog; that annotation was not supplied in the question. Inferring a broad enzyme class from sequence motifs would not by itself establish the precise substrate and reaction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied annotation supports A, and the choices describe distinct reaction types; no alternative is supported by the available evidence."
  },
  "important_caveats": [
    "The sequence match is exact to the database record, but the cited catalytic-activity evidence is by similarity to Q9Y4C1, not direct experimental evidence for this Drosophila protein.",
    "The author's source snapshot is unknown; both the historical and current matched records contain the A annotation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt Q9VHC5 (KDM3_DROME, 854 aa, Drosophila melanogaster Lysine-specific demethylase 3, EC 1.14.11.65). The catalytic activity annotation (C5, H3) states exactly: 'N(6),N(6)-dimethyl-L-lysyl(9)-&#91;histone H3&#93; + 2 2-oxoglutarate + 2 O2 = L-lysyl(9)-&#91;histone H3&#93; + 2 formaldehyde + 2 succinate + 2 CO2', which is identical to Choice A. Note the evidence code is ECO:0000250 (transferred by similarity from human KDM3A, Q9Y4C1), so this is database-inferred rather than directly experimentally validated for the Drosophila protein, but the annotation is consistent and unambiguous.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the JmjC (Jumonji C) domain signature: the 'WHQE' motif and the H-x-H / H-x-E-H spacing pattern characteristic of Fe(II)-coordinating JmjC-domain histone demethylases. JmjC enzymes use 2-oxoglutarate as co-substrate and produce formaldehyde as a byproduct of oxidative demethylation. Among the four choices, only A describes a 2-oxoglutarate/O2-dependent oxidative demethylation producing formaldehyde and succinate. Choice B is a SAM-dependent methyltransferase (okaramine biosynthesis), C is an ATP-dependent xenobiotic transporter, and D is a serine phosphatase—none of which involve JmjC-domain chemistry. Recognizing the JmjC domain motif and its associated 2-OG/formaldehyde chemistry constitutes general biological knowledge.


**Missing item-specific fact**

> The precise histone target (H3K9 vs H3K4 vs H3K36) and methylation state (me2 vs me3) would require specific knowledge of the KDM3 family, but this is unnecessary to answer the question because only one option (A) represents a JmjC-type reaction at all.


**Reason**

> The JmjC domain signature (WHQE, H-x-H motifs) is a well-characterized biological motif recognizable from sequence. The 2-oxoglutarate/formaldehyde chemistry is the hallmark of JmjC demethylases. Since three of the four choices represent entirely different enzyme classes (methyltransferase, transporter, phosphatase), recognizing the JmjC domain is sufficient to select A without item-specific lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only Choice A describes a JmjC-type oxidative demethylase reaction. The other three options (SAM-dependent methyltransferase, ATP-dependent transporter, phosphatase) are mechanistically incompatible with a JmjC-domain protein. No ambiguity exists among the choices.


### Important caveats

- The UniProt annotation uses evidence code ECO:0000250 (similarity to human KDM3A Q9Y4C1), meaning the catalytic activity is transferred by orthology rather than directly demonstrated for the Drosophila protein.
- The specific substrate target (H3K9me2) and the exact demethylation state are inferred from the human ortholog; direct biochemical characterization of Drosophila Kdm3 on H3K9 specifically was not independently confirmed in the retrieved evidence.
- The reviewer-only accession (Q9VHC5) was inferred from dataset metadata and was not provided to the evaluated model; the model must work from the raw sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the JmjC (Jumonji C) domain signature: the 'WHQE' motif and the H-x-H / H-x-E-H spacing pattern characteristic of Fe(II)-coordinating JmjC-domain histone demethylases. JmjC enzymes use 2-oxoglutarate as co-substrate and produce formaldehyde as a byproduct of oxidative demethylation. Among the four choices, only A describes a 2-oxoglutarate/O2-dependent oxidative demethylation producing formaldehyde and succinate. Choice B is a SAM-dependent methyltransferase (okaramine biosynthesis), C is an ATP-dependent xenobiotic transporter, and D is a serine phosphatase—none of which involve JmjC-domain chemistry. Recognizing the JmjC domain motif and its associated 2-OG/formaldehyde chemistry constitutes general biological knowledge.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The precise histone target (H3K9 vs H3K4 vs H3K36) and methylation state (me2 vs me3) would require specific knowledge of the KDM3 family, but this is unnecessary to answer the question because only one option (A) represents a JmjC-type reaction at all.",
    "reason": "The JmjC domain signature (WHQE, H-x-H motifs) is a well-characterized biological motif recognizable from sequence. The 2-oxoglutarate/formaldehyde chemistry is the hallmark of JmjC demethylases. Since three of the four choices represent entirely different enzyme classes (methyltransferase, transporter, phosphatase), recognizing the JmjC domain is sufficient to select A without item-specific lookup."
  },
  "case_id": "catalytic_activity_0055",
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
    "reason": "The sequence matches UniProt Q9VHC5 (KDM3_DROME, 854 aa, Drosophila melanogaster Lysine-specific demethylase 3, EC 1.14.11.65). The catalytic activity annotation (C5, H3) states exactly: 'N(6),N(6)-dimethyl-L-lysyl(9)-[histone H3] + 2 2-oxoglutarate + 2 O2 = L-lysyl(9)-[histone H3] + 2 formaldehyde + 2 succinate + 2 CO2', which is identical to Choice A. Note the evidence code is ECO:0000250 (transferred by similarity from human KDM3A, Q9Y4C1), so this is database-inferred rather than directly experimentally validated for the Drosophila protein, but the annotation is consistent and unambiguous."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000250 (similarity to human KDM3A Q9Y4C1), meaning the catalytic activity is transferred by orthology rather than directly demonstrated for the Drosophila protein.",
    "The specific substrate target (H3K9me2) and the exact demethylation state are inferred from the human ortholog; direct biochemical characterization of Drosophila Kdm3 on H3K9 specifically was not independently confirmed in the retrieved evidence.",
    "The reviewer-only accession (Q9VHC5) was inferred from dataset metadata and was not provided to the evaluated model; the model must work from the raw sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only Choice A describes a JmjC-type oxidative demethylase reaction. The other three options (SAM-dependent methyltransferase, ATP-dependent transporter, phosphatase) are mechanistically incompatible with a JmjC-domain protein. No ambiguity exists among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0055",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q9VHC5 (KDM3_DROME, 854 aa, Drosophila melanogaster Lysine-specific demethylase 3, EC 1.14.11.65). The catalytic activity annotation (C5, H3) states exactly: 'N(6),N(6)-dimethyl-L-lysyl(9)-[histone H3] + 2 2-oxoglutarate + 2 O2 = L-lysyl(9)-[histone H3] + 2 formaldehyde + 2 succinate + 2 CO2', which is identical to Choice A. Note the evidence code is ECO:0000250 (transferred by similarity from human KDM3A, Q9Y4C1), so this is database-inferred rather than directly experimentally validated for the Drosophila protein, but the annotation is consistent and unambiguous.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the JmjC (Jumonji C) domain signature: the 'WHQE' motif and the H-x-H / H-x-E-H spacing pattern characteristic of Fe(II)-coordinating JmjC-domain histone demethylases. JmjC enzymes use 2-oxoglutarate as co-substrate and produce formaldehyde as a byproduct of oxidative demethylation. Among the four choices, only A describes a 2-oxoglutarate/O2-dependent oxidative demethylation producing formaldehyde and succinate. Choice B is a SAM-dependent methyltransferase (okaramine biosynthesis), C is an ATP-dependent xenobiotic transporter, and D is a serine phosphatase—none of which involve JmjC-domain chemistry. Recognizing the JmjC domain motif and its associated 2-OG/formaldehyde chemistry constitutes general biological knowledge.",
    "missing_item_specific_fact": "The precise histone target (H3K9 vs H3K4 vs H3K36) and methylation state (me2 vs me3) would require specific knowledge of the KDM3 family, but this is unnecessary to answer the question because only one option (A) represents a JmjC-type reaction at all.",
    "reason": "The JmjC domain signature (WHQE, H-x-H motifs) is a well-characterized biological motif recognizable from sequence. The 2-oxoglutarate/formaldehyde chemistry is the hallmark of JmjC demethylases. Since three of the four choices represent entirely different enzyme classes (methyltransferase, transporter, phosphatase), recognizing the JmjC domain is sufficient to select A without item-specific lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only Choice A describes a JmjC-type oxidative demethylase reaction. The other three options (SAM-dependent methyltransferase, ATP-dependent transporter, phosphatase) are mechanistically incompatible with a JmjC-domain protein. No ambiguity exists among the choices."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000250 (similarity to human KDM3A Q9Y4C1), meaning the catalytic activity is transferred by orthology rather than directly demonstrated for the Drosophila protein.",
    "The specific substrate target (H3K9me2) and the exact demethylation state are inferred from the human ortholog; direct biochemical characterization of Drosophila Kdm3 on H3K9 specifically was not independently confirmed in the retrieved evidence.",
    "The reviewer-only accession (Q9VHC5) was inferred from dataset metadata and was not provided to the evaluated model; the model must work from the raw sequence alone."
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

**Accession:** `Q9VHC5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 180. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VHC5.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:18.636093+00:00.  

```json
"Q9VHC5"
```

Source SHA-256: `988cd450ac6d94115d3a0a907f3be7bea9fa1fb8ec7323334e09bde36a991b80`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VHC5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:18.636093+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9Y4C1","source":"UniProtKB"}],"value":"1.14.11.65"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"FBgn0037703","source":"FlyBase"}],"value":"Lysine-specific demethylase 3"}}}
```

Source SHA-256: `988cd450ac6d94115d3a0a907f3be7bea9fa1fb8ec7323334e09bde36a991b80`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VHC5.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:18.636093+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"1.14.11.65","evidences":[{"evidenceCode":"ECO:0000250","id":"Q9Y4C1","source":"UniProtKB"}],"name":"N(6),N(6)-dimethyl-L-lysyl(9)-[histone H3] + 2 2-oxoglutarate + 2 O2 = L-lysyl(9)-[histone H3] + 2 formaldehyde + 2 succinate + 2 CO2","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:60188"},{"database":"Rhea","id":"RHEA-COMP:15541"},{"database":"Rhea","id":"RHEA-COMP:15546"},{"database":"ChEBI","id":"CHEBI:15379"},{"database":"ChEBI","id":"CHEBI:16526"},{"database":"ChEBI","id":"CHEBI:16810"},{"database":"ChEBI","id":"CHEBI:16842"},{"database":"ChEBI","id":"CHEBI:29969"},{"database":"ChEBI","id":"CHEBI:30031"},{"database":"ChEBI","id":"CHEBI:61976"}]}}
```

Source SHA-256: `988cd450ac6d94115d3a0a907f3be7bea9fa1fb8ec7323334e09bde36a991b80`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VHC5?format=txt&versions=180)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 180 / 1.  
**Retrieved:** 2026-11-02T04:33:24.066442+00:00.  

```text
ID   KDM3_DROME              Reviewed;         854 AA.
AC   Q9VHC5;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-MAY-2000, sequence version 1.
DT   28-JAN-2026, entry version 180.
DE   RecName: Full=Lysine-specific demethylase 3 {ECO:0000312|FlyBase:FBgn0037703};
DE            EC=1.14.11.65 {ECO:0000250|UniProtKB:Q9Y4C1};
GN   Name=Kdm3 {ECO:0000312|FlyBase:FBgn0037703};
GN   Synonyms=JHDM2 {ECO:0000312|FlyBase:FBgn0037703};
GN   ORFNames=CG8165 {ECO:0000312|FlyBase:FBgn0037703};
OS   Drosophila melanogaster (Fruit fly).
OC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;
OC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;
OC   Drosophilidae; Drosophila; Sophophora.
OX   NCBI_TaxID=7227 {ECO:0000312|Proteomes:UP000000803};
```

Source SHA-256: `f5da474d2b6eef609a1e0f06b8a3e0427dad5c78083068d262116ce5e8a89bbd`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VHC5?format=txt&versions=180)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 180 / 1.  
**Retrieved:** 2026-11-02T04:33:24.066442+00:00.  

```text
DE   RecName: Full=Lysine-specific demethylase 3 {ECO:0000312|FlyBase:FBgn0037703};
DE            EC=1.14.11.65 {ECO:0000250|UniProtKB:Q9Y4C1};
```

Source SHA-256: `f5da474d2b6eef609a1e0f06b8a3e0427dad5c78083068d262116ce5e8a89bbd`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VHC5?format=txt&versions=180)  
**Locator:** `lines 122-129`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 180 / 1.  
**Retrieved:** 2026-11-02T04:33:24.066442+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=N(6),N(6)-dimethyl-L-lysyl(9)-[histone H3] + 2 2-oxoglutarate
CC         + 2 O2 = L-lysyl(9)-[histone H3] + 2 formaldehyde + 2 succinate + 2
CC         CO2; Xref=Rhea:RHEA:60188, Rhea:RHEA-COMP:15541, Rhea:RHEA-
CC         COMP:15546, ChEBI:CHEBI:15379, ChEBI:CHEBI:16526, ChEBI:CHEBI:16810,
CC         ChEBI:CHEBI:16842, ChEBI:CHEBI:29969, ChEBI:CHEBI:30031,
CC         ChEBI:CHEBI:61976; EC=1.14.11.65;
CC         Evidence={ECO:0000250|UniProtKB:Q9Y4C1};
```

Source SHA-256: `f5da474d2b6eef609a1e0f06b8a3e0427dad5c78083068d262116ce5e8a89bbd`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 55. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
