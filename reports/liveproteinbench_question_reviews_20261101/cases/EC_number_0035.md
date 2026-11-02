# EC_number_0035

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **C** — 2.1.1.392

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAEKQQAVTEFYNNTSPRGAWEFLLGDHLHEGFYDPGTTATISGSQAAAARMIDEALRFANIYDDPSKKPKNMLDIGCGVGGTCVHVAKQYGIQCKGITLSPEEVKCAQGIAKAQGLEEKVSFDVGDALNLPYKDGTFDLVLTIECIEHVQDKEKFIREMIRVAAPGAPIVILSYAHRNLSPSAESLKPDEKKVLKKICDNLALSCLCSSADFVRWLTQLPAEDIKTADWTQNTSPFFPLLMKETFTWKGFTSLLMKGGWTAIKELLALRMMSKAADDGLLKFVAITCRKSK

[Multiple Choices]
A. 2.1.1.395
B. 2.1.1.27
C. 2.1.1.392
D. 1.3.1.36
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

> The supplied sequence exactly matches the reviewed UniProt sequence for this protein. Its EC 2.1.1.392 annotation is linked to evidence-coded catalytic activity for methylating norajmaline and 4-methylnorajmaline; the cited evidence code is experimental, though the underlying papers were not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may support a broad inference of methyltransferase activity, and EC 1.3.1.36 is a different enzyme class. But that does not distinguish the closely related methyltransferase options by their specific substrate and reaction.


**Missing item-specific fact**

> The protein-specific catalytic activity—especially its methylation of norajmaline to ajmaline, which identifies EC 2.1.1.392—is not supplied in the question and requires a specific annotation or experimental result.


**Reason**

> Choosing the exact EC number depends on protein-specific substrate specificity, not a general sequence-level argument available from the provided input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer-only evidence supports C for the matched sequence. The sequence-only input does not reveal the exact substrate specificity, but that limitation concerns answerability rather than evidence that another option is correct.


### Important caveats

- The database annotation cites experimental evidence, but the primary papers were not independently retrieved or validated.
- The exact author data-source snapshot is unknown, although the sequence matches both the current and retrieved historical UniProt records.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may support a broad inference of methyltransferase activity, and EC 1.3.1.36 is a different enzyme class. But that does not distinguish the closely related methyltransferase options by their specific substrate and reaction.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific catalytic activity—especially its methylation of norajmaline to ajmaline, which identifies EC 2.1.1.392—is not supplied in the question and requires a specific annotation or experimental result.",
    "reason": "Choosing the exact EC number depends on protein-specific substrate specificity, not a general sequence-level argument available from the provided input."
  },
  "case_id": "EC_number_0035",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed UniProt sequence for this protein. Its EC 2.1.1.392 annotation is linked to evidence-coded catalytic activity for methylating norajmaline and 4-methylnorajmaline; the cited evidence code is experimental, though the underlying papers were not independently reviewed here."
  },
  "important_caveats": [
    "The database annotation cites experimental evidence, but the primary papers were not independently retrieved or validated.",
    "The exact author data-source snapshot is unknown, although the sequence matches both the current and retrieved historical UniProt records."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only evidence supports C for the matched sequence. The sequence-only input does not reveal the exact substrate specificity, but that limitation concerns answerability rather than evidence that another option is correct."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0035",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed UniProt sequence for this protein. Its EC 2.1.1.392 annotation is linked to evidence-coded catalytic activity for methylating norajmaline and 4-methylnorajmaline; the cited evidence code is experimental, though the underlying papers were not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may support a broad inference of methyltransferase activity, and EC 1.3.1.36 is a different enzyme class. But that does not distinguish the closely related methyltransferase options by their specific substrate and reaction.",
    "missing_item_specific_fact": "The protein-specific catalytic activity—especially its methylation of norajmaline to ajmaline, which identifies EC 2.1.1.392—is not supplied in the question and requires a specific annotation or experimental result.",
    "reason": "Choosing the exact EC number depends on protein-specific substrate specificity, not a general sequence-level argument available from the provided input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only evidence supports C for the matched sequence. The sequence-only input does not reveal the exact substrate specificity, but that limitation concerns answerability rather than evidence that another option is correct."
  },
  "important_caveats": [
    "The database annotation cites experimental evidence, but the primary papers were not independently retrieved or validated.",
    "The exact author data-source snapshot is unknown, although the sequence matches both the current and retrieved historical UniProt records."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A075D6M1 (NNMT_RAUSE) confirms this 292-aa sequence from Rauvolfia serpentina is Norajmaline N-methyltransferase with EC 2.1.1.392. The EC assignment is backed by experimental evidence (ECO:0000269) from PubMed 27122470 (Cazares-Flores et al., Plant J. 2016) and PubMed 38212296 (Guo et al., Nat. Commun. 2024), documenting the catalytic reaction: norajmaline + SAM → ajmaline + SAH + H+. Sequence match is exact (SHA-256 identical). The expected answer C (2.1.1.392) is correct.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [C8](#evidence-c8), [H1](#evidence-h1), [H2](#evidence-h2), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> From the sequence, one can reasonably identify a SAM-dependent methyltransferase fold (Rossmann-like motifs including 'GCGVGGTC', 'VLT', and the conserved catalytic region), which supports EC class 2.1.1.- (N-methyltransferases) and eliminates D (1.3.1.36, an oxidoreductase). However, distinguishing the 4th digit — 392 vs 395 vs 27 — requires knowing the exact substrate specificity (norajmaline vs other alkaloid substrates). The EC 4th digit is an arbitrary catalog identifier for a specific enzyme–substrate pair, not derivable from general sequence motifs.


**Missing item-specific fact**

> The specific substrate identity (norajmaline → ajmaline N-methylation) and the precise active-site residues that confer selectivity for norajmaline over other potential N-methyltransferase substrates. This is an experimentally determined fact (PubMed 27122470, 38212296) not inferable from the raw sequence without database lookup or memorization of this specific entry.


**Reason**

> While the methyltransferase fold narrows the answer to EC 2.1.1.-, the three methyltransferase options (2.1.1.392, 2.1.1.395, 2.1.1.27) differ only in their arbitrary 4th-digit catalog number, which encodes the exact substrate. No general biological rule or sequence heuristic distinguishes 'norajmaline N-methyltransferase' from 'another N-methyltransferase' at the 4th-digit level. Selection requires item-specific knowledge of this protein's experimentally characterized substrate specificity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> D (1.3.1.36, oxidoreductase) is clearly eliminable by recognizing the methyltransferase fold. Among A, B, and C (all 2.1.1.-), only C is correct per experimental evidence, but the question does not provide enough sequence-level information to reason between them. The ambiguity is not in the correctness of the key but in the absence of reasoning grounds to distinguish the three methyltransferase options.


### Important caveats

- The UniProt annotation was first released in Swiss-Prot on 2025-06-18; the EC assignment relies on 2016 and 2024 experimental papers. The benchmark author's source snapshot is unknown.
- EC 4th-digit numbers (392, 395, 27) are essentially catalog identifiers for specific enzyme-substrate pairs; no general biological rule maps sequence motifs to a specific 4th digit.
- The sequence alone does not reveal the organism (Rauvolfia serpentina) or the gene name (NNMT), both of which would be needed for contextual inference about ajmaline biosynthesis.
- Distractor D (1.3.1.36, oxidoreductase) is a trivially eliminable option given the clear methyltransferase fold, reducing effective discrimination to a three-way choice among N-methyltransferases that require substrate-specific knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "From the sequence, one can reasonably identify a SAM-dependent methyltransferase fold (Rossmann-like motifs including 'GCGVGGTC', 'VLT', and the conserved catalytic region), which supports EC class 2.1.1.- (N-methyltransferases) and eliminates D (1.3.1.36, an oxidoreductase). However, distinguishing the 4th digit — 392 vs 395 vs 27 — requires knowing the exact substrate specificity (norajmaline vs other alkaloid substrates). The EC 4th digit is an arbitrary catalog identifier for a specific enzyme–substrate pair, not derivable from general sequence motifs.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate identity (norajmaline → ajmaline N-methylation) and the precise active-site residues that confer selectivity for norajmaline over other potential N-methyltransferase substrates. This is an experimentally determined fact (PubMed 27122470, 38212296) not inferable from the raw sequence without database lookup or memorization of this specific entry.",
    "reason": "While the methyltransferase fold narrows the answer to EC 2.1.1.-, the three methyltransferase options (2.1.1.392, 2.1.1.395, 2.1.1.27) differ only in their arbitrary 4th-digit catalog number, which encodes the exact substrate. No general biological rule or sequence heuristic distinguishes 'norajmaline N-methyltransferase' from 'another N-methyltransferase' at the 4th-digit level. Selection requires item-specific knowledge of this protein's experimentally characterized substrate specificity."
  },
  "case_id": "EC_number_0035",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "C8",
      "H1",
      "H2",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A075D6M1 (NNMT_RAUSE) confirms this 292-aa sequence from Rauvolfia serpentina is Norajmaline N-methyltransferase with EC 2.1.1.392. The EC assignment is backed by experimental evidence (ECO:0000269) from PubMed 27122470 (Cazares-Flores et al., Plant J. 2016) and PubMed 38212296 (Guo et al., Nat. Commun. 2024), documenting the catalytic reaction: norajmaline + SAM → ajmaline + SAH + H+. Sequence match is exact (SHA-256 identical). The expected answer C (2.1.1.392) is correct."
  },
  "important_caveats": [
    "The UniProt annotation was first released in Swiss-Prot on 2025-06-18; the EC assignment relies on 2016 and 2024 experimental papers. The benchmark author's source snapshot is unknown.",
    "EC 4th-digit numbers (392, 395, 27) are essentially catalog identifiers for specific enzyme-substrate pairs; no general biological rule maps sequence motifs to a specific 4th digit.",
    "The sequence alone does not reveal the organism (Rauvolfia serpentina) or the gene name (NNMT), both of which would be needed for contextual inference about ajmaline biosynthesis.",
    "Distractor D (1.3.1.36, oxidoreductase) is a trivially eliminable option given the clear methyltransferase fold, reducing effective discrimination to a three-way choice among N-methyltransferases that require substrate-specific knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D (1.3.1.36, oxidoreductase) is clearly eliminable by recognizing the methyltransferase fold. Among A, B, and C (all 2.1.1.-), only C is correct per experimental evidence, but the question does not provide enough sequence-level information to reason between them. The ambiguity is not in the correctness of the key but in the absence of reasoning grounds to distinguish the three methyltransferase options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0035",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A075D6M1 (NNMT_RAUSE) confirms this 292-aa sequence from Rauvolfia serpentina is Norajmaline N-methyltransferase with EC 2.1.1.392. The EC assignment is backed by experimental evidence (ECO:0000269) from PubMed 27122470 (Cazares-Flores et al., Plant J. 2016) and PubMed 38212296 (Guo et al., Nat. Commun. 2024), documenting the catalytic reaction: norajmaline + SAM → ajmaline + SAH + H+. Sequence match is exact (SHA-256 identical). The expected answer C (2.1.1.392) is correct.",
    "evidence_ids": ["C4", "C5", "C7", "C8", "H1", "H2", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "From the sequence, one can reasonably identify a SAM-dependent methyltransferase fold (Rossmann-like motifs including 'GCGVGGTC', 'VLT', and the conserved catalytic region), which supports EC class 2.1.1.- (N-methyltransferases) and eliminates D (1.3.1.36, an oxidoreductase). However, distinguishing the 4th digit — 392 vs 395 vs 27 — requires knowing the exact substrate specificity (norajmaline vs other alkaloid substrates). The EC 4th digit is an arbitrary catalog identifier for a specific enzyme–substrate pair, not derivable from general sequence motifs.",
    "missing_item_specific_fact": "The specific substrate identity (norajmaline → ajmaline N-methylation) and the precise active-site residues that confer selectivity for norajmaline over other potential N-methyltransferase substrates. This is an experimentally determined fact (PubMed 27122470, 38212296) not inferable from the raw sequence without database lookup or memorization of this specific entry.",
    "reason": "While the methyltransferase fold narrows the answer to EC 2.1.1.-, the three methyltransferase options (2.1.1.392, 2.1.1.395, 2.1.1.27) differ only in their arbitrary 4th-digit catalog number, which encodes the exact substrate. No general biological rule or sequence heuristic distinguishes 'norajmaline N-methyltransferase' from 'another N-methyltransferase' at the 4th-digit level. Selection requires item-specific knowledge of this protein's experimentally characterized substrate specificity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D (1.3.1.36, oxidoreductase) is clearly eliminable by recognizing the methyltransferase fold. Among A, B, and C (all 2.1.1.-), only C is correct per experimental evidence, but the question does not provide enough sequence-level information to reason between them. The ambiguity is not in the correctness of the key but in the absence of reasoning grounds to distinguish the three methyltransferase options."
  },
  "important_caveats": [
    "The UniProt annotation was first released in Swiss-Prot on 2025-06-18; the EC assignment relies on 2016 and 2024 experimental papers. The benchmark author's source snapshot is unknown.",
    "EC 4th-digit numbers (392, 395, 27) are essentially catalog identifiers for specific enzyme-substrate pairs; no general biological rule maps sequence motifs to a specific 4th digit.",
    "The sequence alone does not reveal the organism (Rauvolfia serpentina) or the gene name (NNMT), both of which would be needed for contextual inference about ajmaline biosynthesis.",
    "Distractor D (1.3.1.36, oxidoreductase) is a trivially eliminable option given the clear methyltransferase fold, reducing effective discrimination to a three-way choice among N-methyltransferases that require substrate-specific knowledge."
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

**Accession:** `A0A075D6M1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 36. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D6M1.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:36.783284+00:00.  

```json
"A0A075D6M1"
```

Source SHA-256: `3bb9ffb2ae03473556ed523492c0744d518e1d741d7bd4b3a3fc9dc695f623a9`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D6M1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:36.783284+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"AHH02781.1","source":"EMBL"}],"value":"Gamma-tocopherol-like methyltransferase NNMT"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38212296","source":"PubMed"}],"value":"2.1.1.392"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"27122470","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"38212296","source":"PubMed"}],"value":"Norajmaline N-methyltransferase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"27122470","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"38212296","source":"PubMed"}],"value":"RsNNMT"}]}}
```

Source SHA-256: `3bb9ffb2ae03473556ed523492c0744d518e1d741d7bd4b3a3fc9dc695f623a9`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D6M1.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:36.783284+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"27122470","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38212296","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:79600"}}],"reaction":{"ecNumber":"2.1.1.392","evidences":[{"evidenceCode":"ECO:0000269","id":"27122470","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38212296","source":"PubMed"}],"name":"norajmaline + S-adenosyl-L-methionine = ajmaline + S-adenosyl-L-homocysteine + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:79599"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57856"},{"database":"ChEBI","id":"CHEBI:58567"},{"database":"ChEBI","id":"CHEBI:59789"},{"database":"ChEBI","id":"CHEBI:77618"}]}}
```

Source SHA-256: `3bb9ffb2ae03473556ed523492c0744d518e1d741d7bd4b3a3fc9dc695f623a9`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D6M1.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:36.783284+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"27122470","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:79604"}}],"reaction":{"ecNumber":"2.1.1.392","evidences":[{"evidenceCode":"ECO:0000269","id":"27122470","source":"PubMed"}],"name":"4-methylnorajmaline + S-adenosyl-L-methionine = 4-methylajmaline + S-adenosyl-L-homocysteine + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:79603"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57856"},{"database":"ChEBI","id":"CHEBI:59789"},{"database":"ChEBI","id":"CHEBI:230509"},{"database":"ChEBI","id":"CHEBI:230510"}]}}
```

Source SHA-256: `3bb9ffb2ae03473556ed523492c0744d518e1d741d7bd4b3a3fc9dc695f623a9`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D6M1.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:36.783284+00:00.  

```json
{"citation":{"authors":["Cazares-Flores P.","Levac D.","De Luca V."],"citationCrossReferences":[{"database":"PubMed","id":"27122470"},{"database":"DOI","id":"10.1111/tpj.13186"}],"citationType":"journal article","firstPage":"335","id":"27122470","journal":"Plant J.","lastPage":"342","publicationDate":"2016","title":"Rauvolfia serpentina N-methyltransferases involved in ajmaline and Nbeta -methylajmaline biosynthesis belong to a gene family derived from gamma-tocopherol C-methyltransferase.","volume":"87"},"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","PATHWAY","TISSUE SPECIFICITY"]}
```

Source SHA-256: `3bb9ffb2ae03473556ed523492c0744d518e1d741d7bd4b3a3fc9dc695f623a9`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D6M1.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:36.783284+00:00.  

```json
{"citation":{"authors":["Guo J.","Gao D.","Lian J.","Qu Y."],"citationCrossReferences":[{"database":"PubMed","id":"38212296"},{"database":"DOI","id":"10.1038/s41467-024-44797-z"}],"citationType":"journal article","firstPage":"457","id":"38212296","journal":"Nat. Commun.","lastPage":"457","publicationDate":"2024","title":"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.","volume":"15"},"referenceNumber":3,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","PATHWAY","TISSUE SPECIFICITY","BIOTECHNOLOGY"]}
```

Source SHA-256: `3bb9ffb2ae03473556ed523492c0744d518e1d741d7bd4b3a3fc9dc695f623a9`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D6M1?format=txt&versions=36)  
**Locator:** `lines 1-17`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 36 / 1.  
**Retrieved:** 2026-11-01T06:27:15.852655+00:00.  

```text
ID   NNMT_RAUSE              Reviewed;         292 AA.
AC   A0A075D6M1;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   29-OCT-2014, sequence version 1.
DT   28-JAN-2026, entry version 36.
DE   RecName: Full=Norajmaline N-methyltransferase {ECO:0000303|PubMed:27122470, ECO:0000303|PubMed:38212296};
DE            Short=RsNNMT {ECO:0000303|PubMed:27122470, ECO:0000303|PubMed:38212296};
DE            EC=2.1.1.392 {ECO:0000269|PubMed:38212296};
DE   AltName: Full=Gamma-tocopherol-like methyltransferase NNMT {ECO:0000312|EMBL:AHH02781.1};
GN   Name=NNMT {ECO:0000303|PubMed:38212296};
GN   Synonyms=Rs9447 {ECO:0000312|EMBL:AHH02781.1};
OS   Rauvolfia serpentina (Serpentine wood) (Ophioxylon serpentinum).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Vinceae;
OC   Rauvolfiinae; Rauvolfia.
OX   NCBI_TaxID=4060;
```

Source SHA-256: `ea487ae2513c784ecb9c3536d3436f3ff3869372e436c3eb33f2b9b462f39efa`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D6M1?format=txt&versions=36)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 36 / 1.  
**Retrieved:** 2026-11-01T06:27:15.852655+00:00.  

```text
DE   RecName: Full=Norajmaline N-methyltransferase {ECO:0000303|PubMed:27122470, ECO:0000303|PubMed:38212296};
DE            Short=RsNNMT {ECO:0000303|PubMed:27122470, ECO:0000303|PubMed:38212296};
DE            EC=2.1.1.392 {ECO:0000269|PubMed:38212296};
DE   AltName: Full=Gamma-tocopherol-like methyltransferase NNMT {ECO:0000312|EMBL:AHH02781.1};
```

Source SHA-256: `ea487ae2513c784ecb9c3536d3436f3ff3869372e436c3eb33f2b9b462f39efa`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D6M1?format=txt&versions=36)  
**Locator:** `lines 51-58`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 36 / 1.  
**Retrieved:** 2026-11-01T06:27:15.852655+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=norajmaline + S-adenosyl-L-methionine = ajmaline + S-adenosyl-
CC         L-homocysteine + H(+); Xref=Rhea:RHEA:79599, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:57856, ChEBI:CHEBI:58567, ChEBI:CHEBI:59789,
CC         ChEBI:CHEBI:77618; EC=2.1.1.392;
CC         Evidence={ECO:0000269|PubMed:27122470, ECO:0000269|PubMed:38212296};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:79600;
CC         Evidence={ECO:0000269|PubMed:27122470, ECO:0000269|PubMed:38212296};
```

Source SHA-256: `ea487ae2513c784ecb9c3536d3436f3ff3869372e436c3eb33f2b9b462f39efa`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D6M1?format=txt&versions=36)  
**Locator:** `lines 59-66`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 36 / 1.  
**Retrieved:** 2026-11-01T06:27:15.852655+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=4-methylnorajmaline + S-adenosyl-L-methionine = 4-
CC         methylajmaline + S-adenosyl-L-homocysteine + H(+);
CC         Xref=Rhea:RHEA:79603, ChEBI:CHEBI:15378, ChEBI:CHEBI:57856,
CC         ChEBI:CHEBI:59789, ChEBI:CHEBI:230509, ChEBI:CHEBI:230510;
CC         EC=2.1.1.392; Evidence={ECO:0000269|PubMed:27122470};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:79604;
CC         Evidence={ECO:0000269|PubMed:27122470};
```

Source SHA-256: `ea487ae2513c784ecb9c3536d3436f3ff3869372e436c3eb33f2b9b462f39efa`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 35. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
