# EC_number_0033

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **C** — 2.3.1.318

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | invalid_review |

**Paired comparison:** not comparable: one or both reviews invalid or missing. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTQPCIISVAITGSLPRKRDNPAVPITVSEQVESTQAAFEAGATLVHLHVRNDDETPSSEPDRFARVLEGIRKHAPGIITQVSTGGRSGAGRERGGMLSLRPDMASLATGSVNFPTRVYDNPPDLVDWLAAEMKAYAIKPEIEAFDLSMIFQAVAMQQAGKIDGALHIQFVMGIKNAMPVDREVLAFYVHTLRRLAPDATWTGAGIGRDQLTMARWSLELGGHCRTGLEDNVRLDKQTLAPSNAALVSQVAALCEEYGRPVATVAQARALLGLPSMEIDGRSPW

[Multiple Choices]
A. 2.3.1.193
B. 6.3.5.1
C. 2.3.1.318
D. 4.3.1.24
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

> The exact sequence matches the UniProt entry annotated as 3-oxoadipate:acetyl-CoA acetyltransferase, EC 2.3.1.318. Its catalytic-activity annotation assigns the reaction 3-oxoadipate + acetyl-CoA = acetoacetate + succinyl-CoA and cites experimental evidence (ECO:0000269, PubMed:24240508).

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is compatible with an enzyme, but the supplied sequence and choices do not establish its precise substrate specificity or reaction. Distinguishing the listed EC numbers requires identifying the protein's specific catalytic function.


**Missing item-specific fact**

> The sequence-specific functional annotation or experimental evidence identifying this protein's catalyzed reaction as 3-oxoadipate:acetyl-CoA acetyltransferase.


**Reason**

> The supporting reaction annotation is reviewer-only and was not provided in the question. General sequence reasoning alone does not meaningfully select this exact EC number over the alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices specify different EC numbers, and the sequence-matched annotation supports C; no evidence here supports another listed option.


### Important caveats

- The UniProt annotation cites experimental evidence, but the cited primary paper was not independently reviewed here.
- The actual author source snapshot is unknown; the reviewer-only historical record and current record both match the supplied sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is compatible with an enzyme, but the supplied sequence and choices do not establish its precise substrate specificity or reaction. Distinguishing the listed EC numbers requires identifying the protein's specific catalytic function.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence-specific functional annotation or experimental evidence identifying this protein's catalyzed reaction as 3-oxoadipate:acetyl-CoA acetyltransferase.",
    "reason": "The supporting reaction annotation is reviewer-only and was not provided in the question. General sequence reasoning alone does not meaningfully select this exact EC number over the alternatives."
  },
  "case_id": "EC_number_0033",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as 3-oxoadipate:acetyl-CoA acetyltransferase, EC 2.3.1.318. Its catalytic-activity annotation assigns the reaction 3-oxoadipate + acetyl-CoA = acetoacetate + succinyl-CoA and cites experimental evidence (ECO:0000269, PubMed:24240508)."
  },
  "important_caveats": [
    "The UniProt annotation cites experimental evidence, but the cited primary paper was not independently reviewed here.",
    "The actual author source snapshot is unknown; the reviewer-only historical record and current record both match the supplied sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices specify different EC numbers, and the sequence-matched annotation supports C; no evidence here supports another listed option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0033",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as 3-oxoadipate:acetyl-CoA acetyltransferase, EC 2.3.1.318. Its catalytic-activity annotation assigns the reaction 3-oxoadipate + acetyl-CoA = acetoacetate + succinyl-CoA and cites experimental evidence (ECO:0000269, PubMed:24240508).",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is compatible with an enzyme, but the supplied sequence and choices do not establish its precise substrate specificity or reaction. Distinguishing the listed EC numbers requires identifying the protein's specific catalytic function.",
    "missing_item_specific_fact": "The sequence-specific functional annotation or experimental evidence identifying this protein's catalyzed reaction as 3-oxoadipate:acetyl-CoA acetyltransferase.",
    "reason": "The supporting reaction annotation is reviewer-only and was not provided in the question. General sequence reasoning alone does not meaningfully select this exact EC number over the alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices specify different EC numbers, and the sequence-matched annotation supports C; no evidence here supports another listed option."
  },
  "important_caveats": [
    "The UniProt annotation cites experimental evidence, but the cited primary paper was not independently reviewed here.",
    "The actual author source snapshot is unknown; the reviewer-only historical record and current record both match the supplied sequence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `invalid_review`.

**This result is not a valid structured review.** Any saved labels below remain the model’s original values; they are excluded from label distributions and paired agreement. No field or option ID has been repaired.

**Validation errors:** `question_ambiguity:invalid_option_ids`.

### Expected-answer support: supported

> The supplied 284-aa sequence exactly matches UniProt Q0KAA1 (3OXCE_CUPNH) from Cupriavidus necator H16. The EC 2.3.1.318 annotation (3-oxoadipate:acetyl-CoA acetyltransferase) is backed by experimental evidence (ECO:0000269, in vitro assay) from PubMed 24240508 (Bastard et al., Nat. Chem. Biol. 2014). The catalytic reaction (3-oxoadipate + acetyl-CoA → acetoacetate + succinyl-CoA) is confirmed with Rhea and ChEBI cross-references. Sequence match is confirmed in both current (v89) and historical (v87) snapshots.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Two distractors (6.3.5.1, a ligase/glutamine synthetase; 4.3.1.24, a C-N lyase) can be eliminated by recognizing the wrong enzyme class and inconsistent protein size (glutamine synthetase is ~460+ aa in bacteria vs. 284 aa here). However, the remaining contest is between EC 2.3.1.193 and EC 2.3.1.318, both acyltransferases. Distinguishing between two specific acyltransferase EC numbers from a 284-aa sequence requires knowledge of the precise substrate specificity (3-oxoadipate + acetyl-CoA → acetoacetate + succinyl-CoA) determined experimentally in 2014. No general sequence motif or family-level reasoning separates these two EC numbers.


**Missing item-specific fact**

> The specific substrate specificity of this enzyme (3-oxoadipate:acetyl-CoA acetyltransferase) was established only by in vitro experimentation (PubMed 24240508, 2014). Without knowing which acyltransferase subfamily this protein belongs to and its exact reaction, one cannot distinguish EC 2.3.1.193 from EC 2.3.1.318 by sequence reasoning alone.


**Reason**

> While class-level elimination (ligase, lyase) is feasible, the critical discrimination between two acyltransferase EC numbers depends on an item-specific experimental fact (the exact substrates/products of this recently characterized enzyme) that is not inferable from general sequence features or motifs.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A (2.3.1.193)",
  "C (2.3.1.318)"
]
```

> Both are acyltransferases. Without prior knowledge of the specific reaction catalyzed by this 284-aa protein, a model cannot distinguish between these two EC numbers from sequence alone. The other two options (6.3.5.1, 4.3.1.24) are eliminable by class and size, but the A-vs-C contest is not resolvable by general reasoning.


### Important caveats

- EC 2.3.1.318 was assigned relatively recently (2014 experimental characterization; UniProt entry first public 2025-02-05), making it unlikely to be widely represented in training data.
- The identity of EC 2.3.1.193 could not be independently verified from the supplied evidence; its exact name and substrate are not provided, limiting the ability to assess whether any subtle sequence distinction exists.
- The reviewer-only evidence confirms the key but was not available to the evaluated model.
- The sequence-to-function mapping for this enzyme was established by heterologous expression and in vitro assay, not by sequence homology alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Two distractors (6.3.5.1, a ligase/glutamine synthetase; 4.3.1.24, a C-N lyase) can be eliminated by recognizing the wrong enzyme class and inconsistent protein size (glutamine synthetase is ~460+ aa in bacteria vs. 284 aa here). However, the remaining contest is between EC 2.3.1.193 and EC 2.3.1.318, both acyltransferases. Distinguishing between two specific acyltransferase EC numbers from a 284-aa sequence requires knowledge of the precise substrate specificity (3-oxoadipate + acetyl-CoA → acetoacetate + succinyl-CoA) determined experimentally in 2014. No general sequence motif or family-level reasoning separates these two EC numbers.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate specificity of this enzyme (3-oxoadipate:acetyl-CoA acetyltransferase) was established only by in vitro experimentation (PubMed 24240508, 2014). Without knowing which acyltransferase subfamily this protein belongs to and its exact reaction, one cannot distinguish EC 2.3.1.193 from EC 2.3.1.318 by sequence reasoning alone.",
    "reason": "While class-level elimination (ligase, lyase) is feasible, the critical discrimination between two acyltransferase EC numbers depends on an item-specific experimental fact (the exact substrates/products of this recently characterized enzyme) that is not inferable from general sequence features or motifs."
  },
  "case_id": "EC_number_0033",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied 284-aa sequence exactly matches UniProt Q0KAA1 (3OXCE_CUPNH) from Cupriavidus necator H16. The EC 2.3.1.318 annotation (3-oxoadipate:acetyl-CoA acetyltransferase) is backed by experimental evidence (ECO:0000269, in vitro assay) from PubMed 24240508 (Bastard et al., Nat. Chem. Biol. 2014). The catalytic reaction (3-oxoadipate + acetyl-CoA → acetoacetate + succinyl-CoA) is confirmed with Rhea and ChEBI cross-references. Sequence match is confirmed in both current (v89) and historical (v87) snapshots."
  },
  "important_caveats": [
    "EC 2.3.1.318 was assigned relatively recently (2014 experimental characterization; UniProt entry first public 2025-02-05), making it unlikely to be widely represented in training data.",
    "The identity of EC 2.3.1.193 could not be independently verified from the supplied evidence; its exact name and substrate are not provided, limiting the ability to assess whether any subtle sequence distinction exists.",
    "The reviewer-only evidence confirms the key but was not available to the evaluated model.",
    "The sequence-to-function mapping for this enzyme was established by heterologous expression and in vitro assay, not by sequence homology alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A (2.3.1.193)",
      "C (2.3.1.318)"
    ],
    "reason": "Both are acyltransferases. Without prior knowledge of the specific reaction catalyzed by this 284-aa protein, a model cannot distinguish between these two EC numbers from sequence alone. The other two options (6.3.5.1, 4.3.1.24) are eliminable by class and size, but the A-vs-C contest is not resolvable by general reasoning."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0033",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied 284-aa sequence exactly matches UniProt Q0KAA1 (3OXCE_CUPNH) from Cupriavidus necator H16. The EC 2.3.1.318 annotation (3-oxoadipate:acetyl-CoA acetyltransferase) is backed by experimental evidence (ECO:0000269, in vitro assay) from PubMed 24240508 (Bastard et al., Nat. Chem. Biol. 2014). The catalytic reaction (3-oxoadipate + acetyl-CoA → acetoacetate + succinyl-CoA) is confirmed with Rhea and ChEBI cross-references. Sequence match is confirmed in both current (v89) and historical (v87) snapshots.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Two distractors (6.3.5.1, a ligase/glutamine synthetase; 4.3.1.24, a C-N lyase) can be eliminated by recognizing the wrong enzyme class and inconsistent protein size (glutamine synthetase is ~460+ aa in bacteria vs. 284 aa here). However, the remaining contest is between EC 2.3.1.193 and EC 2.3.1.318, both acyltransferases. Distinguishing between two specific acyltransferase EC numbers from a 284-aa sequence requires knowledge of the precise substrate specificity (3-oxoadipate + acetyl-CoA → acetoacetate + succinyl-CoA) determined experimentally in 2014. No general sequence motif or family-level reasoning separates these two EC numbers.",
    "missing_item_specific_fact": "The specific substrate specificity of this enzyme (3-oxoadipate:acetyl-CoA acetyltransferase) was established only by in vitro experimentation (PubMed 24240508, 2014). Without knowing which acyltransferase subfamily this protein belongs to and its exact reaction, one cannot distinguish EC 2.3.1.193 from EC 2.3.1.318 by sequence reasoning alone.",
    "reason": "While class-level elimination (ligase, lyase) is feasible, the critical discrimination between two acyltransferase EC numbers depends on an item-specific experimental fact (the exact substrates/products of this recently characterized enzyme) that is not inferable from general sequence features or motifs."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A (2.3.1.193)", "C (2.3.1.318)"],
    "reason": "Both are acyltransferases. Without prior knowledge of the specific reaction catalyzed by this 284-aa protein, a model cannot distinguish between these two EC numbers from sequence alone. The other two options (6.3.5.1, 4.3.1.24) are eliminable by class and size, but the A-vs-C contest is not resolvable by general reasoning."
  },
  "important_caveats": [
    "EC 2.3.1.318 was assigned relatively recently (2014 experimental characterization; UniProt entry first public 2025-02-05), making it unlikely to be widely represented in training data.",
    "The identity of EC 2.3.1.193 could not be independently verified from the supplied evidence; its exact name and substrate are not provided, limiting the ability to assess whether any subtle sequence distinction exists.",
    "The reviewer-only evidence confirms the key but was not available to the evaluated model.",
    "The sequence-to-function mapping for this enzyme was established by heterologous expression and in vitro assay, not by sequence homology alone."
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

**Accession:** `Q0KAA1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 87. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0KAA1.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:26.682394+00:00.  

```json
"Q0KAA1"
```

Source SHA-256: `c8f71ccfa4b417ca33bf6e9e7b333cdb179beaa73d1bbbba6e6d86bbeaaac140`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0KAA1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:26.682394+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"3-oxoadipate cleavage enzyme"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"24240508","source":"PubMed"}],"value":"BKACE_378"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"24240508","source":"PubMed"}],"value":"2.3.1.318"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"3-oxoadipate:acetyl-CoA acetyltransferase"}}}
```

Source SHA-256: `c8f71ccfa4b417ca33bf6e9e7b333cdb179beaa73d1bbbba6e6d86bbeaaac140`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0KAA1.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:26.682394+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.3.1.318","evidences":[{"evidenceCode":"ECO:0000269","id":"24240508","source":"PubMed"}],"name":"3-oxoadipate + acetyl-CoA = acetoacetate + succinyl-CoA","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:79651"},{"database":"ChEBI","id":"CHEBI:13705"},{"database":"ChEBI","id":"CHEBI:15775"},{"database":"ChEBI","id":"CHEBI:57288"},{"database":"ChEBI","id":"CHEBI:57292"}]}}
```

Source SHA-256: `c8f71ccfa4b417ca33bf6e9e7b333cdb179beaa73d1bbbba6e6d86bbeaaac140`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0KAA1.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:26.682394+00:00.  

```json
{"citation":{"authors":["Bastard K.","Smith A.A.","Vergne-Vaxelaire C.","Perret A.","Zaparucha A.","De Melo-Minardi R.","Mariage A.","Boutard M.","Debard A.","Lechaplais C.","Pelle C.","Pellouin V.","Perchat N.","Petit J.L.","Kreimeyer A.","Medigue C.","Weissenbach J.","Artiguenave F.","De Berardinis V.","Vallenet D.","Salanoubat M."],"citationCrossReferences":[{"database":"PubMed","id":"24240508"},{"database":"DOI","id":"10.1038/nchembio.1387"}],"citationType":"journal article","firstPage":"42","id":"24240508","journal":"Nat. Chem. Biol.","lastPage":"49","publicationDate":"2014","title":"Revealing the hidden functional diversity of an enzyme family.","volume":"10"},"referenceNumber":3,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES"]}
```

Source SHA-256: `c8f71ccfa4b417ca33bf6e9e7b333cdb179beaa73d1bbbba6e6d86bbeaaac140`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0KAA1?format=txt&versions=87)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 87 / 1.  
**Retrieved:** 2026-11-02T04:30:29.925890+00:00.  

```text
ID   3OXCE_CUPNH             Reviewed;         284 AA.
AC   Q0KAA1;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   03-OCT-2006, sequence version 1.
DT   28-JAN-2026, entry version 87.
DE   RecName: Full=3-oxoadipate:acetyl-CoA acetyltransferase {ECO:0000305};
DE            EC=2.3.1.318 {ECO:0000269|PubMed:24240508};
DE   AltName: Full=3-oxoadipate cleavage enzyme {ECO:0000305};
DE   AltName: Full=BKACE_378 {ECO:0000303|PubMed:24240508};
GN   OrderedLocusNames=H16_A1969 {ECO:0000312|EMBL:CAJ93070.1};
GN   ORFNames=E6A55_10065 {ECO:0000312|EMBL:QCC00902.1};
OS   Cupriavidus necator (strain ATCC 17699 / DSM 428 / KCTC 22496 / NCIMB 10442
OS   / H16 / Stanier 337) (Ralstonia eutropha).
OC   Bacteria; Pseudomonadati; Pseudomonadota; Betaproteobacteria;
OC   Burkholderiales; Burkholderiaceae; Cupriavidus.
OX   NCBI_TaxID=381666;
```

Source SHA-256: `6f05fdb130e65dbd4fe594e672961fa4042d9e020ec6cf0253a116bc497dc13e`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0KAA1?format=txt&versions=87)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 87 / 1.  
**Retrieved:** 2026-11-02T04:30:29.925890+00:00.  

```text
DE   RecName: Full=3-oxoadipate:acetyl-CoA acetyltransferase {ECO:0000305};
DE            EC=2.3.1.318 {ECO:0000269|PubMed:24240508};
DE   AltName: Full=3-oxoadipate cleavage enzyme {ECO:0000305};
DE   AltName: Full=BKACE_378 {ECO:0000303|PubMed:24240508};
```

Source SHA-256: `6f05fdb130e65dbd4fe594e672961fa4042d9e020ec6cf0253a116bc497dc13e`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0KAA1?format=txt&versions=87)  
**Locator:** `lines 34-43`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 87 / 1.  
**Retrieved:** 2026-11-02T04:30:29.925890+00:00.  

```text
RN   [3]
RP   FUNCTION, CATALYTIC ACTIVITY, AND BIOPHYSICOCHEMICAL PROPERTIES.
RX   PubMed=24240508; DOI=10.1038/nchembio.1387;
RA   Bastard K., Smith A.A., Vergne-Vaxelaire C., Perret A., Zaparucha A.,
RA   De Melo-Minardi R., Mariage A., Boutard M., Debard A., Lechaplais C.,
RA   Pelle C., Pellouin V., Perchat N., Petit J.L., Kreimeyer A., Medigue C.,
RA   Weissenbach J., Artiguenave F., De Berardinis V., Vallenet D.,
RA   Salanoubat M.;
RT   "Revealing the hidden functional diversity of an enzyme family.";
RL   Nat. Chem. Biol. 10:42-49(2014).
```

Source SHA-256: `6f05fdb130e65dbd4fe594e672961fa4042d9e020ec6cf0253a116bc497dc13e`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0KAA1?format=txt&versions=87)  
**Locator:** `lines 49-53`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 87 / 1.  
**Retrieved:** 2026-11-02T04:30:29.925890+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=3-oxoadipate + acetyl-CoA = acetoacetate + succinyl-CoA;
CC         Xref=Rhea:RHEA:79651, ChEBI:CHEBI:13705, ChEBI:CHEBI:15775,
CC         ChEBI:CHEBI:57288, ChEBI:CHEBI:57292; EC=2.3.1.318;
CC         Evidence={ECO:0000269|PubMed:24240508};
```

Source SHA-256: `6f05fdb130e65dbd4fe594e672961fa4042d9e020ec6cf0253a116bc497dc13e`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 33. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
