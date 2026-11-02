# EC_number_0171

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **B** — 1.2.1.11

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSPRPQIKVGVLGATGTVGQRFIELLAAHPYFALHALGASSRSAGQQYARVVRWKLPSPIPDAVRHMVVHECRPDAPGFAECGVVFSGLDADVAGDIENAFRAADLVVYSNAKNYRRDPLCPLIVPLVNPSHLSIIPYQREQLGLKKGYIVTNANCSTTGIVVPLAALEKAFGPLDTVIVTTLQAISGAGYPGVSSLDIMDNVVPLISGEEDKIEWETNKILGGVTPDNKAFDLHAPKQINVSATCTRVPVIDGHTGCVSVKFARSPPPSVAEVENAFREYTCDAQHLGVPSAPAQAIVVHDAPDRPQPRLDKNLHNGACVSVGRIRECPVFDIKFVCLIDNVRLGAATSSIINAEIAVEKGLIQ

[Multiple Choices]
A. 1.2.1.46
B. 1.2.1.11
C. 1.1.1.336
D. 5.3.1.8
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

> The supplied sequence exactly matches the UniProt entry for a fungal aspartate-semialdehyde dehydrogenase, annotated EC 1.2.1.11. The annotation cites experimental evidence for the catalytic activity and reaction.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Sequence features may suggest a nucleotide-binding oxidoreductase and help disfavor the isomerase option, but those broad clues do not establish this protein’s substrate-specific catalytic activity or uniquely distinguish the exact EC number.


**Missing item-specific fact**

> The protein-specific identification as aspartate-semialdehyde dehydrogenase, supported here by curated annotation and cited catalytic-activity evidence.


**Reason**

> The sequence is supplied, but no biological context or functional evidence is provided that establishes its precise substrate and reaction. Recalling or retrieving this exact protein’s annotation would distinguish the choices; generic sequence heuristics alone do not.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports one EC assignment for the matched protein, but the sequence-only input does not provide enough function-specific evidence to distinguish that assignment reliably from the alternatives.


### Important caveats

- The UniProt annotation is sequence-matched, and its EC assignment cites experimental evidence; the cited primary papers were not independently reviewed here.
- The annotation’s historical snapshot is known, but the author’s exact source snapshot is not.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Sequence features may suggest a nucleotide-binding oxidoreductase and help disfavor the isomerase option, but those broad clues do not establish this protein’s substrate-specific catalytic activity or uniquely distinguish the exact EC number.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as aspartate-semialdehyde dehydrogenase, supported here by curated annotation and cited catalytic-activity evidence.",
    "reason": "The sequence is supplied, but no biological context or functional evidence is provided that establishes its precise substrate and reaction. Recalling or retrieving this exact protein’s annotation would distinguish the choices; generic sequence heuristics alone do not."
  },
  "case_id": "EC_number_0171",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry for a fungal aspartate-semialdehyde dehydrogenase, annotated EC 1.2.1.11. The annotation cites experimental evidence for the catalytic activity and reaction."
  },
  "important_caveats": [
    "The UniProt annotation is sequence-matched, and its EC assignment cites experimental evidence; the cited primary papers were not independently reviewed here.",
    "The annotation’s historical snapshot is known, but the author’s exact source snapshot is not."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports one EC assignment for the matched protein, but the sequence-only input does not provide enough function-specific evidence to distinguish that assignment reliably from the alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0171",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry for a fungal aspartate-semialdehyde dehydrogenase, annotated EC 1.2.1.11. The annotation cites experimental evidence for the catalytic activity and reaction.",
    "evidence_ids": ["C1", "C4", "C5", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Sequence features may suggest a nucleotide-binding oxidoreductase and help disfavor the isomerase option, but those broad clues do not establish this protein’s substrate-specific catalytic activity or uniquely distinguish the exact EC number.",
    "missing_item_specific_fact": "The protein-specific identification as aspartate-semialdehyde dehydrogenase, supported here by curated annotation and cited catalytic-activity evidence.",
    "reason": "The sequence is supplied, but no biological context or functional evidence is provided that establishes its precise substrate and reaction. Recalling or retrieving this exact protein’s annotation would distinguish the choices; generic sequence heuristics alone do not."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports one EC assignment for the matched protein, but the sequence-only input does not provide enough function-specific evidence to distinguish that assignment reliably from the alternatives."
  },
  "important_caveats": [
    "The UniProt annotation is sequence-matched, and its EC assignment cites experimental evidence; the cited primary papers were not independently reviewed here.",
    "The annotation’s historical snapshot is known, but the author’s exact source snapshot is not."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q5KPK7 (sequence SHA256 match confirmed) annotates this protein as Aspartate-semialdehyde dehydrogenase with EC 1.2.1.11, supported by experimental evidence (ECO:0000269) from PubMed:26527262 (X-ray crystallography, PDB:5CEF) and PubMed:29608391 (functional/inhibitor studies). The catalytic reaction (L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-L-aspartate + NADPH + H(+)) is confirmed by Rhea:RHEA:24284.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H5](#evidence-h5), [C7](#evidence-c7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The Rossmann-fold motif (GVLGATGTVGQ) and catalytic cysteine residues suggest an NAD(P)-dependent aldehyde/oxo oxidoreductase (EC class 1.2), which helps eliminate option C (EC 1.1, acting on CH-OH group) and option D (EC 5.3, isomerase). However, distinguishing EC 1.2.1.11 (aspartate-semialdehyde dehydrogenase) from EC 1.2.1.46 (general aldehyde dehydrogenase, NADP+) requires recognizing specific substrate-binding residues for the aspartate-semialdehyde/phosphate moiety, which is not derivable from general biological reasoning about the sequence.


**Missing item-specific fact**

> The specific substrate-binding pocket architecture and active-site residues that distinguish aspartate-semialdehyde dehydrogenase (EC 1.2.1.11) from a general NADP+-dependent aldehyde dehydrogenase (EC 1.2.1.46) are not identifiable from the raw sequence without either recognizing this exact protein family or consulting a database annotation.


**Reason**

> While general oxidoreductase class (EC 1.2 vs 1.1 vs 5.3) can be partially inferred from the Rossmann fold and catalytic Cys mechanism, the critical distinction between the two EC 1.2.1.x options (A: 1.2.1.46 vs B: 1.2.1.11) depends on item-specific knowledge of ASADH's substrate specificity and active-site geometry that is not apparent from sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options C (1.1.1.336) and D (5.3.1.8) are in entirely different EC top-level classes and are inconsistent with the observed Rossmann fold and catalytic cysteine mechanism. Options A and B are both EC 1.2.1.x aldehyde dehydrogenases, but only B matches the experimental annotation. No ambiguity in the correct answer, though A is a plausible distractor.


### Important caveats

- The UniProt annotation carries experimental evidence codes (ECO:0000269) from two independent publications including X-ray crystallography, strengthening confidence in the EC assignment.
- The identity origin (accession Q5KPK7) was inferred mechanically from dataset metadata and was not provided to the evaluated model; the model must work from sequence alone.
- EC 1.2.1.46 (option A) is a legitimate aldehyde dehydrogenase (NADP+) and shares the same EC top-level class, making it a structurally and mechanistically close distractor that is difficult to exclude without specific ASADH knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The Rossmann-fold motif (GVLGATGTVGQ) and catalytic cysteine residues suggest an NAD(P)-dependent aldehyde/oxo oxidoreductase (EC class 1.2), which helps eliminate option C (EC 1.1, acting on CH-OH group) and option D (EC 5.3, isomerase). However, distinguishing EC 1.2.1.11 (aspartate-semialdehyde dehydrogenase) from EC 1.2.1.46 (general aldehyde dehydrogenase, NADP+) requires recognizing specific substrate-binding residues for the aspartate-semialdehyde/phosphate moiety, which is not derivable from general biological reasoning about the sequence.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate-binding pocket architecture and active-site residues that distinguish aspartate-semialdehyde dehydrogenase (EC 1.2.1.11) from a general NADP+-dependent aldehyde dehydrogenase (EC 1.2.1.46) are not identifiable from the raw sequence without either recognizing this exact protein family or consulting a database annotation.",
    "reason": "While general oxidoreductase class (EC 1.2 vs 1.1 vs 5.3) can be partially inferred from the Rossmann fold and catalytic Cys mechanism, the critical distinction between the two EC 1.2.1.x options (A: 1.2.1.46 vs B: 1.2.1.11) depends on item-specific knowledge of ASADH's substrate specificity and active-site geometry that is not apparent from sequence alone."
  },
  "case_id": "EC_number_0171",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H5",
      "C7"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q5KPK7 (sequence SHA256 match confirmed) annotates this protein as Aspartate-semialdehyde dehydrogenase with EC 1.2.1.11, supported by experimental evidence (ECO:0000269) from PubMed:26527262 (X-ray crystallography, PDB:5CEF) and PubMed:29608391 (functional/inhibitor studies). The catalytic reaction (L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-L-aspartate + NADPH + H(+)) is confirmed by Rhea:RHEA:24284."
  },
  "important_caveats": [
    "The UniProt annotation carries experimental evidence codes (ECO:0000269) from two independent publications including X-ray crystallography, strengthening confidence in the EC assignment.",
    "The identity origin (accession Q5KPK7) was inferred mechanically from dataset metadata and was not provided to the evaluated model; the model must work from sequence alone.",
    "EC 1.2.1.46 (option A) is a legitimate aldehyde dehydrogenase (NADP+) and shares the same EC top-level class, making it a structurally and mechanistically close distractor that is difficult to exclude without specific ASADH knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C (1.1.1.336) and D (5.3.1.8) are in entirely different EC top-level classes and are inconsistent with the observed Rossmann fold and catalytic cysteine mechanism. Options A and B are both EC 1.2.1.x aldehyde dehydrogenases, but only B matches the experimental annotation. No ambiguity in the correct answer, though A is a plausible distractor."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0171",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q5KPK7 (sequence SHA256 match confirmed) annotates this protein as Aspartate-semialdehyde dehydrogenase with EC 1.2.1.11, supported by experimental evidence (ECO:0000269) from PubMed:26527262 (X-ray crystallography, PDB:5CEF) and PubMed:29608391 (functional/inhibitor studies). The catalytic reaction (L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-L-aspartate + NADPH + H(+)) is confirmed by Rhea:RHEA:24284.",
    "evidence_ids": ["C4", "C5", "H2", "H5", "C7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The Rossmann-fold motif (GVLGATGTVGQ) and catalytic cysteine residues suggest an NAD(P)-dependent aldehyde/oxo oxidoreductase (EC class 1.2), which helps eliminate option C (EC 1.1, acting on CH-OH group) and option D (EC 5.3, isomerase). However, distinguishing EC 1.2.1.11 (aspartate-semialdehyde dehydrogenase) from EC 1.2.1.46 (general aldehyde dehydrogenase, NADP+) requires recognizing specific substrate-binding residues for the aspartate-semialdehyde/phosphate moiety, which is not derivable from general biological reasoning about the sequence.",
    "missing_item_specific_fact": "The specific substrate-binding pocket architecture and active-site residues that distinguish aspartate-semialdehyde dehydrogenase (EC 1.2.1.11) from a general NADP+-dependent aldehyde dehydrogenase (EC 1.2.1.46) are not identifiable from the raw sequence without either recognizing this exact protein family or consulting a database annotation.",
    "reason": "While general oxidoreductase class (EC 1.2 vs 1.1 vs 5.3) can be partially inferred from the Rossmann fold and catalytic Cys mechanism, the critical distinction between the two EC 1.2.1.x options (A: 1.2.1.46 vs B: 1.2.1.11) depends on item-specific knowledge of ASADH's substrate specificity and active-site geometry that is not apparent from sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C (1.1.1.336) and D (5.3.1.8) are in entirely different EC top-level classes and are inconsistent with the observed Rossmann fold and catalytic cysteine mechanism. Options A and B are both EC 1.2.1.x aldehyde dehydrogenases, but only B matches the experimental annotation. No ambiguity in the correct answer, though A is a plausible distractor."
  },
  "important_caveats": [
    "The UniProt annotation carries experimental evidence codes (ECO:0000269) from two independent publications including X-ray crystallography, strengthening confidence in the EC assignment.",
    "The identity origin (accession Q5KPK7) was inferred mechanically from dataset metadata and was not provided to the evaluated model; the model must work from sequence alone.",
    "EC 1.2.1.46 (option A) is a legitimate aldehyde dehydrogenase (NADP+) and shares the same EC top-level class, making it a structurally and mechanistically close distractor that is difficult to exclude without specific ASADH knowledge."
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

**Accession:** `Q5KPK7` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 121. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5KPK7.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:24.745599+00:00.  

```json
"Q5KPK7"
```

Source SHA-256: `6e1b51beba0452942e5c6cb2774ea67654b44f73f1d91b259ec7240bea1d2e67`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5KPK7.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:24.745599+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"26527262","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"29608391","source":"PubMed"}],"value":"1.2.1.11"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Aspartate-semialdehyde dehydrogenase"}}}
```

Source SHA-256: `6e1b51beba0452942e5c6cb2774ea67654b44f73f1d91b259ec7240bea1d2e67`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5KPK7.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:24.745599+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"right-to-left","evidences":[{"evidenceCode":"ECO:0000269","id":"26527262","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"29608391","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:24286"}}],"reaction":{"ecNumber":"1.2.1.11","evidences":[{"evidenceCode":"ECO:0000269","id":"26527262","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"29608391","source":"PubMed"}],"name":"L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-L-aspartate + NADPH + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:24284"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:57535"},{"database":"ChEBI","id":"CHEBI:57783"},{"database":"ChEBI","id":"CHEBI:58349"},{"database":"ChEBI","id":"CHEBI:537519"}]}}
```

Source SHA-256: `6e1b51beba0452942e5c6cb2774ea67654b44f73f1d91b259ec7240bea1d2e67`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5KPK7.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:24.745599+00:00.  

```json
{"citation":{"authors":["Dahal G.","Viola R.E."],"citationCrossReferences":[{"database":"PubMed","id":"26527262"},{"database":"DOI","id":"10.1107/s2053230x15017495"}],"citationType":"journal article","firstPage":"1365","id":"26527262","journal":"Acta Crystallogr. F Struct. Biol. Commun.","lastPage":"1371","publicationDate":"2015","title":"Structure of a fungal form of aspartate semialdehyde dehydrogenase from Cryptococcus neoformans.","volume":"71"},"evidences":[{"evidenceCode":"ECO:0007744","id":"5CEF","source":"PDB"}],"referenceNumber":4,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.60 ANGSTROMS)","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","PATHWAY","SUBUNIT"]}
```

Source SHA-256: `6e1b51beba0452942e5c6cb2774ea67654b44f73f1d91b259ec7240bea1d2e67`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5KPK7?format=txt&versions=121)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 121 / 1.  
**Retrieved:** 2026-11-02T04:31:27.262588+00:00.  

```text
DE   RecName: Full=Aspartate-semialdehyde dehydrogenase {ECO:0000305};
DE            EC=1.2.1.11 {ECO:0000269|PubMed:26527262, ECO:0000269|PubMed:29608391};
```

Source SHA-256: `117184b77b1c1a6b186665d7a7a3070affc905fd69df2a927a14fb0e3ceb88c4`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5KPK7?format=txt&versions=121)  
**Locator:** `lines 61-68`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 121 / 1.  
**Retrieved:** 2026-11-02T04:31:27.262588+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-
CC         L-aspartate + NADPH + H(+); Xref=Rhea:RHEA:24284, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:43474, ChEBI:CHEBI:57535, ChEBI:CHEBI:57783,
CC         ChEBI:CHEBI:58349, ChEBI:CHEBI:537519; EC=1.2.1.11;
CC         Evidence={ECO:0000269|PubMed:26527262, ECO:0000269|PubMed:29608391};
CC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:24286;
CC         Evidence={ECO:0000269|PubMed:26527262, ECO:0000269|PubMed:29608391};
```

Source SHA-256: `117184b77b1c1a6b186665d7a7a3070affc905fd69df2a927a14fb0e3ceb88c4`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 171. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
