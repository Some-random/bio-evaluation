# EC_number_0024

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **D** — 5.1.1.25

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | invalid_review |

**Paired comparison:** not comparable: one or both reviews invalid or missing. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MIVVVIADKEFYGWAESVPYARYDESISTSTKQIKALFCDRSFTRKMELSELINTLPAGAARNALDCAMWDLQAKQSTRPVAEILSKTSITSICAHTLSIDTPKAMQEAVLAMNSPPLVKVKLDKQDIIARMTAIANAAPHSQFIVDANEDWCFRDLEENVEALKALNVVLIEQPLPAGEDEQLINFTSPIPLCADESCHTENDLPYLQGRYQVVNIKLDKTGGLTQACSLASKAQKMGFDIMLGCMVGSSLAMAPASLLASQARYVDLDGPLLVLKDRKHHFTYADGQMSPLQSCLWGGAHNSERFFVDRLQLQ

[Multiple Choices]
A. 5.1.1.24
B. 3.5.2.6
C. 2.7.11.11
D. 5.1.1.25
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

> The exact sequence matches UniProt entry P0DXZ2, annotated as EC 5.1.1.25. Its catalytic-activity annotation identifies the reaction as N-acetyl-D-glutamate = N-acetyl-L-glutamate and cites experimental evidence (ECO:0000269, PubMed 36690779).

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices include two racemase EC numbers, but the sequence alone does not establish the specific substrate whose racemization defines the exact EC number. Broad enzyme-class clues do not resolve that distinction.


**Missing item-specific fact**

> The protein's experimentally established catalytic reaction, specifically that it racemizes N-acetyl-D-glutamate.


**Reason**

> The key is supported by sequence-matched, cited annotation, but that protein-specific functional fact is absent from the question input. Recognizing the sequence or recalling its annotation would be lookup or memorization, not reasoning from supplied evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> From the supplied sequence alone, the two racemase choices cannot be distinguished by the substrate-specific fact needed to assign the exact EC number; the reviewer-only evidence supports D.


### Important caveats

- The annotation cites experimental evidence, but the cited primary study was not independently reviewed here.
- The sequence match and source identity are established by reviewer-only evidence and were not supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices include two racemase EC numbers, but the sequence alone does not establish the specific substrate whose racemization defines the exact EC number. Broad enzyme-class clues do not resolve that distinction.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's experimentally established catalytic reaction, specifically that it racemizes N-acetyl-D-glutamate.",
    "reason": "The key is supported by sequence-matched, cited annotation, but that protein-specific functional fact is absent from the question input. Recognizing the sequence or recalling its annotation would be lookup or memorization, not reasoning from supplied evidence."
  },
  "case_id": "EC_number_0024",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt entry P0DXZ2, annotated as EC 5.1.1.25. Its catalytic-activity annotation identifies the reaction as N-acetyl-D-glutamate = N-acetyl-L-glutamate and cites experimental evidence (ECO:0000269, PubMed 36690779)."
  },
  "important_caveats": [
    "The annotation cites experimental evidence, but the cited primary study was not independently reviewed here.",
    "The sequence match and source identity are established by reviewer-only evidence and were not supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "From the supplied sequence alone, the two racemase choices cannot be distinguished by the substrate-specific fact needed to assign the exact EC number; the reviewer-only evidence supports D."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0024",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt entry P0DXZ2, annotated as EC 5.1.1.25. Its catalytic-activity annotation identifies the reaction as N-acetyl-D-glutamate = N-acetyl-L-glutamate and cites experimental evidence (ECO:0000269, PubMed 36690779).",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices include two racemase EC numbers, but the sequence alone does not establish the specific substrate whose racemization defines the exact EC number. Broad enzyme-class clues do not resolve that distinction.",
    "missing_item_specific_fact": "The protein's experimentally established catalytic reaction, specifically that it racemizes N-acetyl-D-glutamate.",
    "reason": "The key is supported by sequence-matched, cited annotation, but that protein-specific functional fact is absent from the question input. Recognizing the sequence or recalling its annotation would be lookup or memorization, not reasoning from supplied evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "From the supplied sequence alone, the two racemase choices cannot be distinguished by the substrate-specific fact needed to assign the exact EC number; the reviewer-only evidence supports D."
  },
  "important_caveats": [
    "The annotation cites experimental evidence, but the cited primary study was not independently reviewed here.",
    "The sequence match and source identity are established by reviewer-only evidence and were not supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `invalid_review`.

**This result is not a valid structured review.** Any saved labels below remain the model’s original values; they are excluded from label distributions and paired agreement. No field or option ID has been repaired.

**Validation errors:** `question_ambiguity:invalid_option_ids`.

### Expected-answer support: supported

> The UniProt entry P0DXZ2 (sequence matched exactly, 315 aa) annotates this protein as N-acetyl-D-glutamate racemase with EC 5.1.1.25, supported by experimental evidence (ECO:0000269, PubMed 36690779, ISME J. 2023). The catalytic activity (N-acetyl-D-glutamate = N-acetyl-L-glutamate, Rhea:RHEA:76499) is confirmed by the primary literature. The historical archived entry (entry version 3, released 2026-01) also carries the same EC annotation.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence displays features consistent with a glutamate-racemase-like fold (a conserved cysteine pair, ~315 aa length, overall architecture), which can narrow the answer to the 5.1.1.x sub-subclass (racemases acting on amino acids and derivatives). This eliminates B (3.5.2.6, beta-lactamase, a hydrolase) and C (2.7.11.11, a kinase, a transferase) as clearly wrong EC classes. However, distinguishing 5.1.1.24 (a closely related racemase in the same sub-subclass) from 5.1.1.25 (N-acetyl-D-glutamate racemase) requires knowing the specific substrate tested experimentally. EC 5.1.1.25 was assigned only in 2023 based on in vitro characterization of a novel marine D-glutamate catabolic pathway; no general sequence motif or fold feature distinguishes 5.1.1.24 from 5.1.1.25 that a model could apply from first principles.


**Missing item-specific fact**

> The specific substrate identity (N-acetyl-D-glutamate vs. the substrate of EC 5.1.1.24) and the experimental characterization from PubMed 36690779 that assigned EC 5.1.1.25 to this particular protein. Without knowing what 5.1.1.24 catalyzes and how its active site differs from 5.1.1.25, the final one-digit distinction cannot be reasoned from the sequence alone.


**Reason**

> While the broader class (5.1.1.x, amino-acid racemase) is inferable from fold-level features, the precise 4th-digit assignment (24 vs 25) depends on an item-specific experimental fact: the substrate specificity determined in the 2023 ISME J. study. This is a newly characterized enzyme (UniProt entry created 2025), so the distinction is not embedded in well-known catalytic-residue rules that a model could apply generically.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A (5.1.1.24)",
  "D (5.1.1.25)"
]
```

> Both A and D fall within EC 5.1.1.x (racemases acting on amino acids and derivatives). Without external knowledge of the specific substrate for 5.1.1.24 versus 5.1.1.25, a model relying solely on sequence-level reasoning could reasonably consider either as a plausible racemase acting on an amino-acid derivative. B and C are clearly eliminable by EC class.


### Important caveats

- EC 5.1.1.25 was assigned very recently (2023 publication, 2025 UniProt entry), so training-data exposure to this annotation is uncertain and may vary by model.
- The reviewer-only UniProt annotation confirms the key but was not available to the evaluated model; the model must rely on its internal knowledge or sequence reasoning.
- The identity of EC 5.1.1.24 was not independently verified in this audit; if it does not exist or is a placeholder, option A would be trivially eliminable, changing the answerability assessment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence displays features consistent with a glutamate-racemase-like fold (a conserved cysteine pair, ~315 aa length, overall architecture), which can narrow the answer to the 5.1.1.x sub-subclass (racemases acting on amino acids and derivatives). This eliminates B (3.5.2.6, beta-lactamase, a hydrolase) and C (2.7.11.11, a kinase, a transferase) as clearly wrong EC classes. However, distinguishing 5.1.1.24 (a closely related racemase in the same sub-subclass) from 5.1.1.25 (N-acetyl-D-glutamate racemase) requires knowing the specific substrate tested experimentally. EC 5.1.1.25 was assigned only in 2023 based on in vitro characterization of a novel marine D-glutamate catabolic pathway; no general sequence motif or fold feature distinguishes 5.1.1.24 from 5.1.1.25 that a model could apply from first principles.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate identity (N-acetyl-D-glutamate vs. the substrate of EC 5.1.1.24) and the experimental characterization from PubMed 36690779 that assigned EC 5.1.1.25 to this particular protein. Without knowing what 5.1.1.24 catalyzes and how its active site differs from 5.1.1.25, the final one-digit distinction cannot be reasoned from the sequence alone.",
    "reason": "While the broader class (5.1.1.x, amino-acid racemase) is inferable from fold-level features, the precise 4th-digit assignment (24 vs 25) depends on an item-specific experimental fact: the substrate specificity determined in the 2023 ISME J. study. This is a newly characterized enzyme (UniProt entry created 2025), so the distinction is not embedded in well-known catalytic-residue rules that a model could apply generically."
  },
  "case_id": "EC_number_0024",
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
    "reason": "The UniProt entry P0DXZ2 (sequence matched exactly, 315 aa) annotates this protein as N-acetyl-D-glutamate racemase with EC 5.1.1.25, supported by experimental evidence (ECO:0000269, PubMed 36690779, ISME J. 2023). The catalytic activity (N-acetyl-D-glutamate = N-acetyl-L-glutamate, Rhea:RHEA:76499) is confirmed by the primary literature. The historical archived entry (entry version 3, released 2026-01) also carries the same EC annotation."
  },
  "important_caveats": [
    "EC 5.1.1.25 was assigned very recently (2023 publication, 2025 UniProt entry), so training-data exposure to this annotation is uncertain and may vary by model.",
    "The reviewer-only UniProt annotation confirms the key but was not available to the evaluated model; the model must rely on its internal knowledge or sequence reasoning.",
    "The identity of EC 5.1.1.24 was not independently verified in this audit; if it does not exist or is a placeholder, option A would be trivially eliminable, changing the answerability assessment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A (5.1.1.24)",
      "D (5.1.1.25)"
    ],
    "reason": "Both A and D fall within EC 5.1.1.x (racemases acting on amino acids and derivatives). Without external knowledge of the specific substrate for 5.1.1.24 versus 5.1.1.25, a model relying solely on sequence-level reasoning could reasonably consider either as a plausible racemase acting on an amino-acid derivative. B and C are clearly eliminable by EC class."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0024",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DXZ2 (sequence matched exactly, 315 aa) annotates this protein as N-acetyl-D-glutamate racemase with EC 5.1.1.25, supported by experimental evidence (ECO:0000269, PubMed 36690779, ISME J. 2023). The catalytic activity (N-acetyl-D-glutamate = N-acetyl-L-glutamate, Rhea:RHEA:76499) is confirmed by the primary literature. The historical archived entry (entry version 3, released 2026-01) also carries the same EC annotation.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence displays features consistent with a glutamate-racemase-like fold (a conserved cysteine pair, ~315 aa length, overall architecture), which can narrow the answer to the 5.1.1.x sub-subclass (racemases acting on amino acids and derivatives). This eliminates B (3.5.2.6, beta-lactamase, a hydrolase) and C (2.7.11.11, a kinase, a transferase) as clearly wrong EC classes. However, distinguishing 5.1.1.24 (a closely related racemase in the same sub-subclass) from 5.1.1.25 (N-acetyl-D-glutamate racemase) requires knowing the specific substrate tested experimentally. EC 5.1.1.25 was assigned only in 2023 based on in vitro characterization of a novel marine D-glutamate catabolic pathway; no general sequence motif or fold feature distinguishes 5.1.1.24 from 5.1.1.25 that a model could apply from first principles.",
    "missing_item_specific_fact": "The specific substrate identity (N-acetyl-D-glutamate vs. the substrate of EC 5.1.1.24) and the experimental characterization from PubMed 36690779 that assigned EC 5.1.1.25 to this particular protein. Without knowing what 5.1.1.24 catalyzes and how its active site differs from 5.1.1.25, the final one-digit distinction cannot be reasoned from the sequence alone.",
    "reason": "While the broader class (5.1.1.x, amino-acid racemase) is inferable from fold-level features, the precise 4th-digit assignment (24 vs 25) depends on an item-specific experimental fact: the substrate specificity determined in the 2023 ISME J. study. This is a newly characterized enzyme (UniProt entry created 2025), so the distinction is not embedded in well-known catalytic-residue rules that a model could apply generically."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A (5.1.1.24)", "D (5.1.1.25)"],
    "reason": "Both A and D fall within EC 5.1.1.x (racemases acting on amino acids and derivatives). Without external knowledge of the specific substrate for 5.1.1.24 versus 5.1.1.25, a model relying solely on sequence-level reasoning could reasonably consider either as a plausible racemase acting on an amino-acid derivative. B and C are clearly eliminable by EC class."
  },
  "important_caveats": [
    "EC 5.1.1.25 was assigned very recently (2023 publication, 2025 UniProt entry), so training-data exposure to this annotation is uncertain and may vary by model.",
    "The reviewer-only UniProt annotation confirms the key but was not available to the evaluated model; the model must rely on its internal knowledge or sequence reasoning.",
    "The identity of EC 5.1.1.24 was not independently verified in this audit; if it does not exist or is a placeholder, option A would be trivially eliminable, changing the answerability assessment."
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

**Accession:** `P0DXZ2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 3. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ2.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:09.095372+00:00.  

```json
"P0DXZ2"
```

Source SHA-256: `ce4ce37f5eba503f3ded1200adaf39a2c1cec4022ddf9b32af66f9212c2586ea`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ2.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:09.095372+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"36690779","source":"PubMed"}],"value":"5.1.1.25"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"36690779","source":"PubMed"}],"value":"N-acetyl-D-glutamate racemase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"36690779","source":"PubMed"}],"value":"N-acetyl-D-Glu racemase"}]}}
```

Source SHA-256: `ce4ce37f5eba503f3ded1200adaf39a2c1cec4022ddf9b32af66f9212c2586ea`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ2.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:09.095372+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"36690779","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:76500"}}],"reaction":{"ecNumber":"5.1.1.25","evidences":[{"evidenceCode":"ECO:0000269","id":"36690779","source":"PubMed"}],"name":"N-acetyl-D-glutamate = N-acetyl-L-glutamate","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:76499"},{"database":"ChEBI","id":"CHEBI:44337"},{"database":"ChEBI","id":"CHEBI:195260"}]}}
```

Source SHA-256: `ce4ce37f5eba503f3ded1200adaf39a2c1cec4022ddf9b32af66f9212c2586ea`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ2.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:09.095372+00:00.  

```json
{"citation":{"authors":["Yu Y.","Wang P.","Cao H.Y.","Teng Z.J.","Zhu Y.","Wang M.","McMinn A.","Chen Y.","Xiang H.","Zhang Y.Z.","Chen X.L.","Zhang Y.Q."],"citationCrossReferences":[{"database":"PubMed","id":"36690779"},{"database":"DOI","id":"10.1038/s41396-023-01364-6"}],"citationType":"journal article","firstPage":"537","id":"36690779","journal":"ISME J.","lastPage":"548","publicationDate":"2023","title":"Novel D-glutamate catabolic pathway in marine Proteobacteria and halophilic archaea.","volume":"17"},"referenceComments":[{"type":"STRAIN","value":"CF6-2"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","FUNCTION","CATALYTIC ACTIVITY","INDUCTION","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `ce4ce37f5eba503f3ded1200adaf39a2c1cec4022ddf9b32af66f9212c2586ea`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ2?format=txt&versions=3)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-01T06:41:59.066573+00:00.  

```text
ID   DGCA_PSEAS              Reviewed;         315 AA.
AC   P0DXZ2;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   09-APR-2025, sequence version 1.
DT   28-JAN-2026, entry version 3.
DE   RecName: Full=N-acetyl-D-glutamate racemase {ECO:0000303|PubMed:36690779};
DE            Short=N-acetyl-D-Glu racemase {ECO:0000303|PubMed:36690779};
DE            EC=5.1.1.25 {ECO:0000269|PubMed:36690779};
GN   Name=dgcA {ECO:0000303|PubMed:36690779};
OS   Pseudoalteromonas sp.
OC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;
OC   Alteromonadales; Pseudoalteromonadaceae; Pseudoalteromonas.
OX   NCBI_TaxID=53249;
```

Source SHA-256: `e4cce17ff5162859998568df20b58b36b0722c6040f9c24adb62cf5a2aed600d`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ2?format=txt&versions=3)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-01T06:41:59.066573+00:00.  

```text
DE   RecName: Full=N-acetyl-D-glutamate racemase {ECO:0000303|PubMed:36690779};
DE            Short=N-acetyl-D-Glu racemase {ECO:0000303|PubMed:36690779};
DE            EC=5.1.1.25 {ECO:0000269|PubMed:36690779};
```

Source SHA-256: `e4cce17ff5162859998568df20b58b36b0722c6040f9c24adb62cf5a2aed600d`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ2?format=txt&versions=3)  
**Locator:** `lines 14-23`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-01T06:41:59.066573+00:00.  

```text
RN   [1]
RP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, CATALYTIC ACTIVITY, INDUCTION,
RP   AND DISRUPTION PHENOTYPE.
RC   STRAIN=CF6-2;
RX   PubMed=36690779; DOI=10.1038/s41396-023-01364-6;
RA   Yu Y., Wang P., Cao H.Y., Teng Z.J., Zhu Y., Wang M., McMinn A., Chen Y.,
RA   Xiang H., Zhang Y.Z., Chen X.L., Zhang Y.Q.;
RT   "Novel D-glutamate catabolic pathway in marine Proteobacteria and
RT   halophilic archaea.";
RL   ISME J. 17:537-548(2023).
```

Source SHA-256: `e4cce17ff5162859998568df20b58b36b0722c6040f9c24adb62cf5a2aed600d`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ2?format=txt&versions=3)  
**Locator:** `lines 31-36`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-01T06:41:59.066573+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=N-acetyl-D-glutamate = N-acetyl-L-glutamate;
CC         Xref=Rhea:RHEA:76499, ChEBI:CHEBI:44337, ChEBI:CHEBI:195260;
CC         EC=5.1.1.25; Evidence={ECO:0000269|PubMed:36690779};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:76500;
CC         Evidence={ECO:0000269|PubMed:36690779};
```

Source SHA-256: `e4cce17ff5162859998568df20b58b36b0722c6040f9c24adb62cf5a2aed600d`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 24. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
