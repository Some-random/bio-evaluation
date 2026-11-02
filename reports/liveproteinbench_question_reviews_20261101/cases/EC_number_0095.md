# EC_number_0095

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **B** — 1.14.18.1

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MGDSSELNVRRSVRDLQAEYDRGNRKPLEDLIRAWKGIQELPPDDKRSFFILGGYHGEPFDYRNAVDALPPDDIYTYWGGWCNHGNVLFPTWHRIYILKLEEALQSIVPGVTLPFWDETSEETVKKGIPDVLTREYFELDGENIKNPLYSYTLPLSLSDNVPGDNKAYEKPAGYETVRYPLSGLVGTPEARAATAKHNAKYPNPIENTQLLNKNIIAWLHGSGKDEEGPTTTDPNPKGRGVKWMYEKCLSAPNYTVFSNTTSAGQWNLDHPAKSVVALEQPHNDVHLAVGGFDIPGQGESGQVADANGDMGENNTAALDPIFFFHHCNVDRMFWLWQKQNGFINKLEVITGYYGTNSSDSQGPTPGIPPGTPLDLNTPLNPFIKDEFGNPFTSMDCINIEEQLGYTYGPGSLDEVPKPEPITGGSTKKLTVRGINRGLFDGSFVIRAYASVPDAQGQLTEYYLGDHAVLSRRNVVKCANCLTHLEVIAHFPLDTLSADLVDKAEYWITIQHRGHSKRMKVDKDTGQSEKALLAQRAELPEKLKYSISVTD

[Multiple Choices]
A. 1.14.19.80
B. 1.14.18.1
C. 1.97.1.14
D. 1.1.1.138
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

> The supplied sequence exactly matches the UniProt entry for tyrosinase HcTyr2, annotated EC 1.14.18.1. The annotation cites experimental evidence for tyrosinase catalytic reactions, including oxidation of L-tyrosine and L-DOPA.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a soluble-enzyme architecture and a pattern of histidines consistent with the conserved copper-binding sites of type-3 copper tyrosinases. That family-level evidence favors tyrosinase over the listed dehydrogenase and other oxidoreductase alternatives.


**Missing item-specific fact**

> No external item-specific fact is strictly necessary to distinguish the options at the family level, although a database annotation or assay would provide stronger confirmation of the exact catalytic activity.


**Reason**

> Sequence features support a recognizable copper-dependent tyrosinase family assignment, which is a meaningful biological basis for selecting the tyrosinase EC option rather than merely recalling the exact sequence's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence's tyrosinase-family features distinguish the keyed option from the listed alternatives.


### Important caveats

- The reviewer-only UniProt evidence matches the sequence and cites experimental evidence, but the primary paper was not independently reviewed here.
- The exact author data-source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a soluble-enzyme architecture and a pattern of histidines consistent with the conserved copper-binding sites of type-3 copper tyrosinases. That family-level evidence favors tyrosinase over the listed dehydrogenase and other oxidoreductase alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No external item-specific fact is strictly necessary to distinguish the options at the family level, although a database annotation or assay would provide stronger confirmation of the exact catalytic activity.",
    "reason": "Sequence features support a recognizable copper-dependent tyrosinase family assignment, which is a meaningful biological basis for selecting the tyrosinase EC option rather than merely recalling the exact sequence's database entry."
  },
  "case_id": "EC_number_0095",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry for tyrosinase HcTyr2, annotated EC 1.14.18.1. The annotation cites experimental evidence for tyrosinase catalytic reactions, including oxidation of L-tyrosine and L-DOPA."
  },
  "important_caveats": [
    "The reviewer-only UniProt evidence matches the sequence and cites experimental evidence, but the primary paper was not independently reviewed here.",
    "The exact author data-source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence's tyrosinase-family features distinguish the keyed option from the listed alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0095",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry for tyrosinase HcTyr2, annotated EC 1.14.18.1. The annotation cites experimental evidence for tyrosinase catalytic reactions, including oxidation of L-tyrosine and L-DOPA.",
    "evidence_ids": ["C1", "C4", "C5", "H4", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a soluble-enzyme architecture and a pattern of histidines consistent with the conserved copper-binding sites of type-3 copper tyrosinases. That family-level evidence favors tyrosinase over the listed dehydrogenase and other oxidoreductase alternatives.",
    "missing_item_specific_fact": "No external item-specific fact is strictly necessary to distinguish the options at the family level, although a database annotation or assay would provide stronger confirmation of the exact catalytic activity.",
    "reason": "Sequence features support a recognizable copper-dependent tyrosinase family assignment, which is a meaningful biological basis for selecting the tyrosinase EC option rather than merely recalling the exact sequence's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence's tyrosinase-family features distinguish the keyed option from the listed alternatives."
  },
  "important_caveats": [
    "The reviewer-only UniProt evidence matches the sequence and cites experimental evidence, but the primary paper was not independently reviewed here.",
    "The exact author data-source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The reviewer evidence confirms the sequence (SHA256 match) corresponds to UniProt entry A0A261GVB1 (TYR2_HAHS4), annotated as Tyrosinase HcTyr2 with EC 1.14.18.1. The annotation carries experimental evidence (ECO:0000269, PubMed:39382070, a 2024 FEBS Open Bio paper characterizing bacterial tyrosinases from Hahella sp. CCB-MM4). The catalytic activities listed (L-tyrosine + O2 → L-dopaquinone + H2O; 2 L-tyrosine + O2 → 2 L-dopa; 2 L-dopa + O2 → 2 L-dopaquinone + 2 H2O) are consistent with EC 1.14.18.1 (monophenol monooxygenase/tyrosinase). The answer is supported by experimental evidence, not merely computational inference.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Partial reasoning is possible: the sequence contains conserved histidine-rich motifs (HHC at ~position 230, CNCLTH at ~position 430) suggestive of a binuclear copper site characteristic of the tyrosinase superfamily. The absence of a P450 heme-binding motif (FxxGxxxCxG) argues against EC 1.14.19.80, and the absence of a Rossmann-fold NAD-binding motif (GxGxxG) argues against EC 1.1.1.138. However, these negative observations alone do not positively identify EC 1.14.18.1 over other copper-dependent oxidoreductases or rule out EC 1.97.1.14 without knowing the specific substrate (monophenol/tyrosine) and reaction mechanism.


**Missing item-specific fact**

> The exact mapping of the tyrosinase enzyme family to EC 1.14.18.1 (as opposed to other EC 1.14 or 1.97 entries) is a database/classification fact. Additionally, distinguishing EC 1.14.18.1 from EC 1.97.1.14 by sequence alone requires knowing the specific substrate specificity (monophenol vs. other substrates) and the ascorbate/reduced-pteridine electron-donor classification criterion for subclass 1.14.18, which is not derivable from the sequence without external knowledge.


**Reason**

> While the copper-binding motifs provide a weak positive signal toward a tyrosinase-like enzyme, the final step of assigning the precise 4-digit EC number (1.14.18.1) from the family-level identification is a memorization/database-lookup task. The distractors are not all trivially eliminable by general sequence heuristics alone; in particular, EC 1.97.1.14 cannot be excluded without knowing its specific substrate and mechanism.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the experimental annotation, EC 1.14.18.1 is the correct answer. The distractors (P450, dehydrogenase, and a different oxidoreductase class) are mechanistically distinct from a copper-dependent tyrosinase, so the answer is unambiguous once the protein is correctly identified.


### Important caveats

- The annotation evidence (PubMed:39382070, 2024) postdates many training cutoffs; a model trained on earlier data may not have encountered this specific entry.
- The sequence match is exact (SHA256 confirmed), so the reviewer evidence applies directly to the benchmark sequence.
- The EC 1.14.18 subclass definition ('with ascorbate or a reduced pteridine as one donor') is a classification convention that is not self-evident from the catalytic reaction alone and requires knowledge of the EC nomenclature rules.
- The reviewer-only evidence was not available to the evaluated model; the model must rely solely on the 550-residue sequence and four EC choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Partial reasoning is possible: the sequence contains conserved histidine-rich motifs (HHC at ~position 230, CNCLTH at ~position 430) suggestive of a binuclear copper site characteristic of the tyrosinase superfamily. The absence of a P450 heme-binding motif (FxxGxxxCxG) argues against EC 1.14.19.80, and the absence of a Rossmann-fold NAD-binding motif (GxGxxG) argues against EC 1.1.1.138. However, these negative observations alone do not positively identify EC 1.14.18.1 over other copper-dependent oxidoreductases or rule out EC 1.97.1.14 without knowing the specific substrate (monophenol/tyrosine) and reaction mechanism.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact mapping of the tyrosinase enzyme family to EC 1.14.18.1 (as opposed to other EC 1.14 or 1.97 entries) is a database/classification fact. Additionally, distinguishing EC 1.14.18.1 from EC 1.97.1.14 by sequence alone requires knowing the specific substrate specificity (monophenol vs. other substrates) and the ascorbate/reduced-pteridine electron-donor classification criterion for subclass 1.14.18, which is not derivable from the sequence without external knowledge.",
    "reason": "While the copper-binding motifs provide a weak positive signal toward a tyrosinase-like enzyme, the final step of assigning the precise 4-digit EC number (1.14.18.1) from the family-level identification is a memorization/database-lookup task. The distractors are not all trivially eliminable by general sequence heuristics alone; in particular, EC 1.97.1.14 cannot be excluded without knowing its specific substrate and mechanism."
  },
  "case_id": "EC_number_0095",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "H1",
      "H2",
      "H4",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The reviewer evidence confirms the sequence (SHA256 match) corresponds to UniProt entry A0A261GVB1 (TYR2_HAHS4), annotated as Tyrosinase HcTyr2 with EC 1.14.18.1. The annotation carries experimental evidence (ECO:0000269, PubMed:39382070, a 2024 FEBS Open Bio paper characterizing bacterial tyrosinases from Hahella sp. CCB-MM4). The catalytic activities listed (L-tyrosine + O2 → L-dopaquinone + H2O; 2 L-tyrosine + O2 → 2 L-dopa; 2 L-dopa + O2 → 2 L-dopaquinone + 2 H2O) are consistent with EC 1.14.18.1 (monophenol monooxygenase/tyrosinase). The answer is supported by experimental evidence, not merely computational inference."
  },
  "important_caveats": [
    "The annotation evidence (PubMed:39382070, 2024) postdates many training cutoffs; a model trained on earlier data may not have encountered this specific entry.",
    "The sequence match is exact (SHA256 confirmed), so the reviewer evidence applies directly to the benchmark sequence.",
    "The EC 1.14.18 subclass definition ('with ascorbate or a reduced pteridine as one donor') is a classification convention that is not self-evident from the catalytic reaction alone and requires knowledge of the EC nomenclature rules.",
    "The reviewer-only evidence was not available to the evaluated model; the model must rely solely on the 550-residue sequence and four EC choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the experimental annotation, EC 1.14.18.1 is the correct answer. The distractors (P450, dehydrogenase, and a different oxidoreductase class) are mechanistically distinct from a copper-dependent tyrosinase, so the answer is unambiguous once the protein is correctly identified."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0095",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The reviewer evidence confirms the sequence (SHA256 match) corresponds to UniProt entry A0A261GVB1 (TYR2_HAHS4), annotated as Tyrosinase HcTyr2 with EC 1.14.18.1. The annotation carries experimental evidence (ECO:0000269, PubMed:39382070, a 2024 FEBS Open Bio paper characterizing bacterial tyrosinases from Hahella sp. CCB-MM4). The catalytic activities listed (L-tyrosine + O2 → L-dopaquinone + H2O; 2 L-tyrosine + O2 → 2 L-dopa; 2 L-dopa + O2 → 2 L-dopaquinone + 2 H2O) are consistent with EC 1.14.18.1 (monophenol monooxygenase/tyrosinase). The answer is supported by experimental evidence, not merely computational inference.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C7", "C8", "H1", "H2", "H4", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Partial reasoning is possible: the sequence contains conserved histidine-rich motifs (HHC at ~position 230, CNCLTH at ~position 430) suggestive of a binuclear copper site characteristic of the tyrosinase superfamily. The absence of a P450 heme-binding motif (FxxGxxxCxG) argues against EC 1.14.19.80, and the absence of a Rossmann-fold NAD-binding motif (GxGxxG) argues against EC 1.1.1.138. However, these negative observations alone do not positively identify EC 1.14.18.1 over other copper-dependent oxidoreductases or rule out EC 1.97.1.14 without knowing the specific substrate (monophenol/tyrosine) and reaction mechanism.",
    "missing_item_specific_fact": "The exact mapping of the tyrosinase enzyme family to EC 1.14.18.1 (as opposed to other EC 1.14 or 1.97 entries) is a database/classification fact. Additionally, distinguishing EC 1.14.18.1 from EC 1.97.1.14 by sequence alone requires knowing the specific substrate specificity (monophenol vs. other substrates) and the ascorbate/reduced-pteridine electron-donor classification criterion for subclass 1.14.18, which is not derivable from the sequence without external knowledge.",
    "reason": "While the copper-binding motifs provide a weak positive signal toward a tyrosinase-like enzyme, the final step of assigning the precise 4-digit EC number (1.14.18.1) from the family-level identification is a memorization/database-lookup task. The distractors are not all trivially eliminable by general sequence heuristics alone; in particular, EC 1.97.1.14 cannot be excluded without knowing its specific substrate and mechanism."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the experimental annotation, EC 1.14.18.1 is the correct answer. The distractors (P450, dehydrogenase, and a different oxidoreductase class) are mechanistically distinct from a copper-dependent tyrosinase, so the answer is unambiguous once the protein is correctly identified."
  },
  "important_caveats": [
    "The annotation evidence (PubMed:39382070, 2024) postdates many training cutoffs; a model trained on earlier data may not have encountered this specific entry.",
    "The sequence match is exact (SHA256 confirmed), so the reviewer evidence applies directly to the benchmark sequence.",
    "The EC 1.14.18 subclass definition ('with ascorbate or a reduced pteridine as one donor') is a classification convention that is not self-evident from the catalytic reaction alone and requires knowledge of the EC nomenclature rules.",
    "The reviewer-only evidence was not available to the evaluated model; the model must rely solely on the 550-residue sequence and four EC choices."
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

**Accession:** `A0A261GVB1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 18. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A261GVB1.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:44.082570+00:00.  

```json
"A0A261GVB1"
```

Source SHA-256: `09d130bfdce053511ac8c67319a6b3e3b5ffbca8bcd3153677567a716e079201`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A261GVB1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:44.082570+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39382070","source":"PubMed"}],"value":"1.14.18.1"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39382070","source":"PubMed"}],"value":"Tyrosinase HcTyr2"}}}
```

Source SHA-256: `09d130bfdce053511ac8c67319a6b3e3b5ffbca8bcd3153677567a716e079201`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A261GVB1.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:44.082570+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"1.14.18.1","evidences":[{"evidenceCode":"ECO:0000269","id":"39382070","source":"PubMed"}],"name":"L-tyrosine + O2 = L-dopaquinone + H2O","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:18117"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15379"},{"database":"ChEBI","id":"CHEBI:57924"},{"database":"ChEBI","id":"CHEBI:58315"}]}}
```

Source SHA-256: `09d130bfdce053511ac8c67319a6b3e3b5ffbca8bcd3153677567a716e079201`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A261GVB1.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:44.082570+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"evidences":[{"evidenceCode":"ECO:0000269","id":"39382070","source":"PubMed"}],"name":"2 L-tyrosine + O2 = 2 L-dopa","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:34283"},{"database":"ChEBI","id":"CHEBI:15379"},{"database":"ChEBI","id":"CHEBI:57504"},{"database":"ChEBI","id":"CHEBI:58315"}]}}
```

Source SHA-256: `09d130bfdce053511ac8c67319a6b3e3b5ffbca8bcd3153677567a716e079201`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A261GVB1.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:44.082570+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"1.14.18.1","evidences":[{"evidenceCode":"ECO:0000269","id":"39382070","source":"PubMed"}],"name":"2 L-dopa + O2 = 2 L-dopaquinone + 2 H2O","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:34287"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15379"},{"database":"ChEBI","id":"CHEBI:57504"},{"database":"ChEBI","id":"CHEBI:57924"}]}}
```

Source SHA-256: `09d130bfdce053511ac8c67319a6b3e3b5ffbca8bcd3153677567a716e079201`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A261GVB1.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:44.082570+00:00.  

```json
{"citation":{"authors":["de Almeida Santos G.","Englund A.N.B.","Dalleywater E.L.","Roehr A.K."],"citationCrossReferences":[{"database":"PubMed","id":"39382070"},{"database":"DOI","id":"10.1002/2211-5463.13906"}],"citationType":"journal article","firstPage":"0","id":"39382070","journal":"FEBS Open Bio","lastPage":"0","publicationDate":"2024","title":"Characterization of two bacterial tyrosinases from the halophilic bacterium Hahella sp. CCB MM4 relevant for phenolic compounds oxidation in wetlands.","volume":"0"},"referenceComments":[{"type":"STRAIN","value":"CCB-MM4"}],"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","COFACTOR","BIOPHYSICOCHEMICAL PROPERTIES","DOMAIN","MUTAGENESIS OF 426-THR--ASP-550"]}
```

Source SHA-256: `09d130bfdce053511ac8c67319a6b3e3b5ffbca8bcd3153677567a716e079201`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A261GVB1?format=txt&versions=18)  
**Locator:** `lines 1-12`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 18 / 1.  
**Retrieved:** 2026-11-01T06:27:24.733923+00:00.  

```text
ID   TYR2_HAHS4              Reviewed;         550 AA.
AC   A0A261GVB1;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   20-DEC-2017, sequence version 1.
DT   28-JAN-2026, entry version 18.
DE   RecName: Full=Tyrosinase HcTyr2 {ECO:0000303|PubMed:39382070};
DE            EC=1.14.18.1 {ECO:0000269|PubMed:39382070};
GN   ORFNames=BTA51_03560 {ECO:0000312|EMBL:OZG75462.1};
OS   Hahella sp. (strain CCB-MM4).
OC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;
OC   Oceanospirillales; Hahellaceae; Hahella.
OX   NCBI_TaxID=1926491;
```

Source SHA-256: `4c794a3cbf945cd4e479d9430b2d9c1e3d32924055d9812812fc36602c8f48b9`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A261GVB1?format=txt&versions=18)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 18 / 1.  
**Retrieved:** 2026-11-01T06:27:24.733923+00:00.  

```text
DE   RecName: Full=Tyrosinase HcTyr2 {ECO:0000303|PubMed:39382070};
DE            EC=1.14.18.1 {ECO:0000269|PubMed:39382070};
```

Source SHA-256: `4c794a3cbf945cd4e479d9430b2d9c1e3d32924055d9812812fc36602c8f48b9`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A261GVB1?format=txt&versions=18)  
**Locator:** `lines 37-41`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 18 / 1.  
**Retrieved:** 2026-11-01T06:27:24.733923+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-tyrosine + O2 = L-dopaquinone + H2O; Xref=Rhea:RHEA:18117,
CC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15379, ChEBI:CHEBI:57924,
CC         ChEBI:CHEBI:58315; EC=1.14.18.1;
CC         Evidence={ECO:0000269|PubMed:39382070};
```

Source SHA-256: `4c794a3cbf945cd4e479d9430b2d9c1e3d32924055d9812812fc36602c8f48b9`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A261GVB1?format=txt&versions=18)  
**Locator:** `lines 42-45`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 18 / 1.  
**Retrieved:** 2026-11-01T06:27:24.733923+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=2 L-tyrosine + O2 = 2 L-dopa; Xref=Rhea:RHEA:34283,
CC         ChEBI:CHEBI:15379, ChEBI:CHEBI:57504, ChEBI:CHEBI:58315;
CC         Evidence={ECO:0000269|PubMed:39382070};
```

Source SHA-256: `4c794a3cbf945cd4e479d9430b2d9c1e3d32924055d9812812fc36602c8f48b9`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A261GVB1?format=txt&versions=18)  
**Locator:** `lines 46-50`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 18 / 1.  
**Retrieved:** 2026-11-01T06:27:24.733923+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=2 L-dopa + O2 = 2 L-dopaquinone + 2 H2O; Xref=Rhea:RHEA:34287,
CC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15379, ChEBI:CHEBI:57504,
CC         ChEBI:CHEBI:57924; EC=1.14.18.1;
CC         Evidence={ECO:0000269|PubMed:39382070};
```

Source SHA-256: `4c794a3cbf945cd4e479d9430b2d9c1e3d32924055d9812812fc36602c8f48b9`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 95. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
