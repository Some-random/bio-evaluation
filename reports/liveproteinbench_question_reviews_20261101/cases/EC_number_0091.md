# EC_number_0091

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **A** — 2.4.1.392

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MNRSDAYGYFRNQGREYVITTPRTPARWFNYLFNDTYYTEISQTGQGDSVAFRPHNRTLTRGFRYFYLKDLETGGTWSPLYQPLKTEPEAYECIHSLGTTEIRSVSQEIASSIHVFVPRAGQQEIWTVTLTNTGVKPRSLSLFTAFSLENGGVMGSKCQFDQESQILSSYSFPYHVTYGQKAGCDDHTNVVYVYPDYPADSYDCSQRAFFGGDDIYELPAAVQKGRCSGGQAEAENPLGALQQTITLEPGEQAVRHFVVGCASSLEEIRSSKAELAAKGYAVLLQETEDYWEGITGMFRVETPDDDVNAFMNIWLKKQIVMQTRTNRMSSYCPVRNQLQDALGYALVDPAGAAEYMISVLQGQERSGFIQQWIMTDGSPPKNLCLLKHTDGPVWLIICITALLNQCGDTELLQRQVGFKGSSDSATIYQHLLLAADYMAGETGAHGLCLMGDGDWNDPINGPGRLGRGESAWNTMALVYAIQALIPFCEQLGDTENAEQLNTVARRLADAVNRICWDGGWYVAGFDDDGTPFGTAQDEEGKLFLNTQTWAIMSGIASGERLDQCLAAIDSLDTPFGPRLLEPPFSGWNPKWGRISLKLAGTTENGSVYCHASMFKAFADCIAGRGSEAWQTISRTLPTNPDNPPGQNGQVPIFVPNYYFGLADSPNFGKSSHHVSTGTVGWMLWTTLEYALGIRATANGLKIDPCIPADWPEYTVERKYRSASYRIHVLNPSGISRGTVKVTVDGEAWMAAALPYEAGREYQVTVQLEQ

[Multiple Choices]
A. 2.4.1.392
B. 2.4.1.259
C. 2.1.1.392
D. 1.2.1.46
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

> The exact sequence matches a UniProt entry annotated as EC 2.4.1.392, with catalytic-activity annotations linked to experimental evidence (ECO:0000269) and PubMed 35947916. The cited reaction is consistent with a glycoside phosphorylase. The paper itself was not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The EC prefixes make some choices broadly distinguishable by reaction type, but they do not establish the precise substrate specificity needed to choose between the two transferase-class options.


**Missing item-specific fact**

> The protein's specific experimentally characterized activity as 3-O-beta-D-glucopyranosyl-beta-D-glucuronide phosphorylase, corresponding to EC 2.4.1.392.


**Reason**

> The sequence alone does not provide a sufficiently discriminating argument for this exact four-digit EC assignment. Selecting A over the closely related EC 2.4.1.259 requires protein-specific functional annotation or equivalent external evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer-only evidence supports A for the sequence-matched protein; no evidence supports another listed choice.


### Important caveats

- The UniProt annotation is linked to experimental evidence, but the primary publication was not independently assessed.
- The exact author source snapshot is unknown, although the matched sequence and historical UniProt entry support the key.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The EC prefixes make some choices broadly distinguishable by reaction type, but they do not establish the precise substrate specificity needed to choose between the two transferase-class options.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's specific experimentally characterized activity as 3-O-beta-D-glucopyranosyl-beta-D-glucuronide phosphorylase, corresponding to EC 2.4.1.392.",
    "reason": "The sequence alone does not provide a sufficiently discriminating argument for this exact four-digit EC assignment. Selecting A over the closely related EC 2.4.1.259 requires protein-specific functional annotation or equivalent external evidence."
  },
  "case_id": "EC_number_0091",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as EC 2.4.1.392, with catalytic-activity annotations linked to experimental evidence (ECO:0000269) and PubMed 35947916. The cited reaction is consistent with a glycoside phosphorylase. The paper itself was not independently reviewed here."
  },
  "important_caveats": [
    "The UniProt annotation is linked to experimental evidence, but the primary publication was not independently assessed.",
    "The exact author source snapshot is unknown, although the matched sequence and historical UniProt entry support the key."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only evidence supports A for the sequence-matched protein; no evidence supports another listed choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0091",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as EC 2.4.1.392, with catalytic-activity annotations linked to experimental evidence (ECO:0000269) and PubMed 35947916. The cited reaction is consistent with a glycoside phosphorylase. The paper itself was not independently reviewed here.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The EC prefixes make some choices broadly distinguishable by reaction type, but they do not establish the precise substrate specificity needed to choose between the two transferase-class options.",
    "missing_item_specific_fact": "The protein's specific experimentally characterized activity as 3-O-beta-D-glucopyranosyl-beta-D-glucuronide phosphorylase, corresponding to EC 2.4.1.392.",
    "reason": "The sequence alone does not provide a sufficiently discriminating argument for this exact four-digit EC assignment. Selecting A over the closely related EC 2.4.1.259 requires protein-specific functional annotation or equivalent external evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only evidence supports A for the sequence-matched protein; no evidence supports another listed choice."
  },
  "important_caveats": [
    "The UniProt annotation is linked to experimental evidence, but the primary publication was not independently assessed.",
    "The exact author source snapshot is unknown, although the matched sequence and historical UniProt entry support the key."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A089MMR2 matches the supplied 769-aa sequence exactly (SHA256 confirmed). The entry is annotated as 3-O-beta-D-glucopyranosyl-beta-D-glucuronide phosphorylase with EC 2.4.1.392, supported by experimental evidence (ECO:0000269) from PubMed:35947916 (Isono et al., Biochem Biophys Res Commun 625:60-65, 2022). The catalytic reaction (3-O-beta-D-glucosyl-D-glucuronate + phosphate = aldehydo-D-glucuronate + alpha-D-glucose 1-phosphate) is consistent with EC 2.4.1.392. Historical entry version 38 (Swiss-Prot, released 2026-01-28) also confirms this annotation.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The first EC digit (1 vs 2) distinguishes oxidoreductase (D) from transferase (A, B, C), and the second digit (1 vs 4) distinguishes one-carbon transfer (C) from glycosyl transfer (A, B). A model with general knowledge of GH94-family sequence motifs might recognize sugar-phosphate chemistry and eliminate C and D. However, the critical distinction between A (2.4.1.392) and B (2.4.1.259) — both EC 2.4.1.xxx glycosyltransferases acting on glycosyl compounds — requires knowing the exact substrate specificity (3-O-beta-D-glucopyranosyl-beta-D-glucuronide for 392 vs whatever substrate 259 targets). This is an item-specific experimental finding from a 2022 paper, not derivable from general sequence features.


**Missing item-specific fact**

> The specific substrate identity (3-O-beta-D-glucopyranosyl-beta-D-glucuronide) and the precise EC assignment 2.4.1.392 vs 2.4.1.259, which were established experimentally in PubMed:35947916 and are not inferable from sequence motifs alone.


**Reason**

> While general biological reasoning can eliminate the oxidoreductase (D) and methyltransferase (C) options based on the presence of sugar-binding/phosphorylase-like sequence features, the choice between the two glycosyltransferase options (A and B) depends on the exact substrate specificity determined experimentally. EC 2.4.1.392 was assigned in 2022 based on in vitro characterization; no general sequence heuristic distinguishes it from other 2.4.1.xxx entries without memorizing this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Both A (2.4.1.392) and B (2.4.1.259) are glycosyltransferases acting on glycosyl compounds (EC 2.4.1.xxx). Without external knowledge of the specific substrate (3-O-beta-D-glucopyranosyl-beta-D-glucuronide), a model cannot reliably distinguish between these two EC numbers from sequence alone. C and D are more clearly eliminable as they belong to different EC subclasses (2.1.1 = one-carbon transfer; 1.2.1 = oxidoreductase).


### Important caveats

- The sequence match to UniProt A0A089MMR2 is exact (769 aa, SHA256 confirmed), and the EC annotation is backed by experimental evidence (ECO:0000269), so the key is scientifically valid.
- EC 2.4.1.392 was assigned in 2022; it is a very recent and specific annotation unlikely to be well-represented in model training data, increasing lookup dependence.
- The reviewer-only evidence establishes the key's validity but was not available to the evaluated model; the model must rely on sequence features and general knowledge.
- GH94 family membership (a glycoside phosphorylase family) could be recognized from sequence, which would support a phosphorylase-type EC number, but does not uniquely pinpoint 2.4.1.392 over other 2.4.1.xxx entries without substrate-specific knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The first EC digit (1 vs 2) distinguishes oxidoreductase (D) from transferase (A, B, C), and the second digit (1 vs 4) distinguishes one-carbon transfer (C) from glycosyl transfer (A, B). A model with general knowledge of GH94-family sequence motifs might recognize sugar-phosphate chemistry and eliminate C and D. However, the critical distinction between A (2.4.1.392) and B (2.4.1.259) — both EC 2.4.1.xxx glycosyltransferases acting on glycosyl compounds — requires knowing the exact substrate specificity (3-O-beta-D-glucopyranosyl-beta-D-glucuronide for 392 vs whatever substrate 259 targets). This is an item-specific experimental finding from a 2022 paper, not derivable from general sequence features.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate identity (3-O-beta-D-glucopyranosyl-beta-D-glucuronide) and the precise EC assignment 2.4.1.392 vs 2.4.1.259, which were established experimentally in PubMed:35947916 and are not inferable from sequence motifs alone.",
    "reason": "While general biological reasoning can eliminate the oxidoreductase (D) and methyltransferase (C) options based on the presence of sugar-binding/phosphorylase-like sequence features, the choice between the two glycosyltransferase options (A and B) depends on the exact substrate specificity determined experimentally. EC 2.4.1.392 was assigned in 2022 based on in vitro characterization; no general sequence heuristic distinguishes it from other 2.4.1.xxx entries without memorizing this specific protein's annotation."
  },
  "case_id": "EC_number_0091",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C7",
      "H1",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A089MMR2 matches the supplied 769-aa sequence exactly (SHA256 confirmed). The entry is annotated as 3-O-beta-D-glucopyranosyl-beta-D-glucuronide phosphorylase with EC 2.4.1.392, supported by experimental evidence (ECO:0000269) from PubMed:35947916 (Isono et al., Biochem Biophys Res Commun 625:60-65, 2022). The catalytic reaction (3-O-beta-D-glucosyl-D-glucuronate + phosphate = aldehydo-D-glucuronate + alpha-D-glucose 1-phosphate) is consistent with EC 2.4.1.392. Historical entry version 38 (Swiss-Prot, released 2026-01-28) also confirms this annotation."
  },
  "important_caveats": [
    "The sequence match to UniProt A0A089MMR2 is exact (769 aa, SHA256 confirmed), and the EC annotation is backed by experimental evidence (ECO:0000269), so the key is scientifically valid.",
    "EC 2.4.1.392 was assigned in 2022; it is a very recent and specific annotation unlikely to be well-represented in model training data, increasing lookup dependence.",
    "The reviewer-only evidence establishes the key's validity but was not available to the evaluated model; the model must rely on sequence features and general knowledge.",
    "GH94 family membership (a glycoside phosphorylase family) could be recognized from sequence, which would support a phosphorylase-type EC number, but does not uniquely pinpoint 2.4.1.392 over other 2.4.1.xxx entries without substrate-specific knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Both A (2.4.1.392) and B (2.4.1.259) are glycosyltransferases acting on glycosyl compounds (EC 2.4.1.xxx). Without external knowledge of the specific substrate (3-O-beta-D-glucopyranosyl-beta-D-glucuronide), a model cannot reliably distinguish between these two EC numbers from sequence alone. C and D are more clearly eliminable as they belong to different EC subclasses (2.1.1 = one-carbon transfer; 1.2.1 = oxidoreductase)."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0091",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A089MMR2 matches the supplied 769-aa sequence exactly (SHA256 confirmed). The entry is annotated as 3-O-beta-D-glucopyranosyl-beta-D-glucuronide phosphorylase with EC 2.4.1.392, supported by experimental evidence (ECO:0000269) from PubMed:35947916 (Isono et al., Biochem Biophys Res Commun 625:60-65, 2022). The catalytic reaction (3-O-beta-D-glucosyl-D-glucuronate + phosphate = aldehydo-D-glucuronate + alpha-D-glucose 1-phosphate) is consistent with EC 2.4.1.392. Historical entry version 38 (Swiss-Prot, released 2026-01-28) also confirms this annotation.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C7", "H1", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The first EC digit (1 vs 2) distinguishes oxidoreductase (D) from transferase (A, B, C), and the second digit (1 vs 4) distinguishes one-carbon transfer (C) from glycosyl transfer (A, B). A model with general knowledge of GH94-family sequence motifs might recognize sugar-phosphate chemistry and eliminate C and D. However, the critical distinction between A (2.4.1.392) and B (2.4.1.259) — both EC 2.4.1.xxx glycosyltransferases acting on glycosyl compounds — requires knowing the exact substrate specificity (3-O-beta-D-glucopyranosyl-beta-D-glucuronide for 392 vs whatever substrate 259 targets). This is an item-specific experimental finding from a 2022 paper, not derivable from general sequence features.",
    "missing_item_specific_fact": "The specific substrate identity (3-O-beta-D-glucopyranosyl-beta-D-glucuronide) and the precise EC assignment 2.4.1.392 vs 2.4.1.259, which were established experimentally in PubMed:35947916 and are not inferable from sequence motifs alone.",
    "reason": "While general biological reasoning can eliminate the oxidoreductase (D) and methyltransferase (C) options based on the presence of sugar-binding/phosphorylase-like sequence features, the choice between the two glycosyltransferase options (A and B) depends on the exact substrate specificity determined experimentally. EC 2.4.1.392 was assigned in 2022 based on in vitro characterization; no general sequence heuristic distinguishes it from other 2.4.1.xxx entries without memorizing this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Both A (2.4.1.392) and B (2.4.1.259) are glycosyltransferases acting on glycosyl compounds (EC 2.4.1.xxx). Without external knowledge of the specific substrate (3-O-beta-D-glucopyranosyl-beta-D-glucuronide), a model cannot reliably distinguish between these two EC numbers from sequence alone. C and D are more clearly eliminable as they belong to different EC subclasses (2.1.1 = one-carbon transfer; 1.2.1 = oxidoreductase)."
  },
  "important_caveats": [
    "The sequence match to UniProt A0A089MMR2 is exact (769 aa, SHA256 confirmed), and the EC annotation is backed by experimental evidence (ECO:0000269), so the key is scientifically valid.",
    "EC 2.4.1.392 was assigned in 2022; it is a very recent and specific annotation unlikely to be well-represented in model training data, increasing lookup dependence.",
    "The reviewer-only evidence establishes the key's validity but was not available to the evaluated model; the model must rely on sequence features and general knowledge.",
    "GH94 family membership (a glycoside phosphorylase family) could be recognized from sequence, which would support a phosphorylase-type EC number, but does not uniquely pinpoint 2.4.1.392 over other 2.4.1.xxx entries without substrate-specific knowledge."
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

**Accession:** `A0A089MMR2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 38. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A089MMR2.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:37.192125+00:00.  

```json
"A0A089MMR2"
```

Source SHA-256: `9c1354b8bfe0e59449355743dfc7334d0ba6fb5835c3df3570380eed27e91719`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A089MMR2.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:37.192125+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"35947916","source":"PubMed"}],"value":"2.4.1.392"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"35947916","source":"PubMed"}],"value":"3-O-beta-D-glucopyranosyl-beta-D-glucuronide phosphorylase"}}}
```

Source SHA-256: `9c1354b8bfe0e59449355743dfc7334d0ba6fb5835c3df3570380eed27e91719`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A089MMR2.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:37.192125+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.4.1.392","evidences":[{"evidenceCode":"ECO:0000269","id":"35947916","source":"PubMed"}],"name":"3-O-beta-D-glucosyl-D-glucuronate + phosphate = aldehydo-D-glucuronate + alpha-D-glucose 1-phosphate","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:78711"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:58601"},{"database":"ChEBI","id":"CHEBI:76826"},{"database":"ChEBI","id":"CHEBI:142686"}]}}
```

Source SHA-256: `9c1354b8bfe0e59449355743dfc7334d0ba6fb5835c3df3570380eed27e91719`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A089MMR2.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:37.192125+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.4.1.392","evidences":[{"evidenceCode":"ECO:0000269","id":"35947916","source":"PubMed"}],"name":"a 3-O-beta-D-glucosyl-beta-D-glucuronoside + phosphate = a beta-D-glucuronoside + alpha-D-glucose 1-phosphate","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:78699"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:58601"},{"database":"ChEBI","id":"CHEBI:83411"},{"database":"ChEBI","id":"CHEBI:229542"}]}}
```

Source SHA-256: `9c1354b8bfe0e59449355743dfc7334d0ba6fb5835c3df3570380eed27e91719`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A089MMR2.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:37.192125+00:00.  

```json
{"citation":{"authors":["Isono N.","Mizutani E.","Hayashida H.","Katsuzaki H.","Saburi W."],"citationCrossReferences":[{"database":"PubMed","id":"35947916"},{"database":"DOI","id":"10.1016/j.bbrc.2022.07.098"}],"citationType":"journal article","firstPage":"60","id":"35947916","journal":"Biochem. Biophys. Res. Commun.","lastPage":"65","publicationDate":"2022","title":"Functional characterization of a novel GH94 glycoside phosphorylase, 3-O-beta-d-glucopyranosyl beta-d-glucuronide phosphorylase, and implication of the metabolic pathway of acidic carbohydrates in Paenibacillus borealis.","volume":"625"},"referenceComments":[{"type":"STRAIN","value":"DSM 13188 / CCUG 43137 / CIP 107056 / KCTC 3805 / KK19"}],"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","SUBUNIT"]}
```

Source SHA-256: `9c1354b8bfe0e59449355743dfc7334d0ba6fb5835c3df3570380eed27e91719`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A089MMR2?format=txt&versions=38)  
**Locator:** `lines 1-12`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-01T06:27:15.632691+00:00.  

```text
ID   BGBGP_PAEBO             Reviewed;         769 AA.
AC   A0A089MMR2;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   26-NOV-2014, sequence version 1.
DT   28-JAN-2026, entry version 38.
DE   RecName: Full=3-O-beta-D-glucopyranosyl-beta-D-glucuronide phosphorylase {ECO:0000303|PubMed:35947916};
DE            EC=2.4.1.392 {ECO:0000269|PubMed:35947916};
GN   ORFNames=PBOR_13355 {ECO:0000312|EMBL:AIQ57809.1};
OS   Paenibacillus borealis.
OC   Bacteria; Bacillati; Bacillota; Bacilli; Bacillales; Paenibacillaceae;
OC   Paenibacillus.
OX   NCBI_TaxID=160799;
```

Source SHA-256: `abf8108925ffb7b150428b7a1aa52e27f87e1ad71c64967596cc5207ae75a348`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A089MMR2?format=txt&versions=38)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-01T06:27:15.632691+00:00.  

```text
DE   RecName: Full=3-O-beta-D-glucopyranosyl-beta-D-glucuronide phosphorylase {ECO:0000303|PubMed:35947916};
DE            EC=2.4.1.392 {ECO:0000269|PubMed:35947916};
```

Source SHA-256: `abf8108925ffb7b150428b7a1aa52e27f87e1ad71c64967596cc5207ae75a348`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A089MMR2?format=txt&versions=38)  
**Locator:** `lines 41-46`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-01T06:27:15.632691+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=3-O-beta-D-glucosyl-D-glucuronate + phosphate = aldehydo-D-
CC         glucuronate + alpha-D-glucose 1-phosphate; Xref=Rhea:RHEA:78711,
CC         ChEBI:CHEBI:43474, ChEBI:CHEBI:58601, ChEBI:CHEBI:76826,
CC         ChEBI:CHEBI:142686; EC=2.4.1.392;
CC         Evidence={ECO:0000269|PubMed:35947916};
```

Source SHA-256: `abf8108925ffb7b150428b7a1aa52e27f87e1ad71c64967596cc5207ae75a348`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A089MMR2?format=txt&versions=38)  
**Locator:** `lines 47-52`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-01T06:27:15.632691+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=a 3-O-beta-D-glucosyl-beta-D-glucuronoside + phosphate = a
CC         beta-D-glucuronoside + alpha-D-glucose 1-phosphate;
CC         Xref=Rhea:RHEA:78699, ChEBI:CHEBI:43474, ChEBI:CHEBI:58601,
CC         ChEBI:CHEBI:83411, ChEBI:CHEBI:229542; EC=2.4.1.392;
CC         Evidence={ECO:0000269|PubMed:35947916};
```

Source SHA-256: `abf8108925ffb7b150428b7a1aa52e27f87e1ad71c64967596cc5207ae75a348`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 91. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
