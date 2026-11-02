# EC_number_0130

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **B** — 1.1.1.195

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAKSPEVEHPVKAFGWAARDPSGVLSPFNFSRRATGEHDVQFKVLYCGICHSDLHMIKNEWGFTKYPIVPGHEIVGVVTEVGSKVEKFKVGDKVGVGCLVGSCRKCDMCSDDLENYCPGQILTYSAAYTDGTTTYGGYSNLMVSDEHFVICWPENLPMDIGAPLLCAGITTYSPLRYFGLDKPGTHVGVVGLGGLGHVAVKFAKAFGAKVTVISTSESKKQEAIEKLGADAFLVSRDPEQMQGAAGSMDGIIDTVSAVHPVLPLVNLLKSQGKLIMVGAPEKPLELPVFPLLAGRRIIAGSAIGGLKETQEMIDFAAKNNILPDVELVPMDYVNTAMERLLKADVKYRFVIDIGNTLKSA

[Multiple Choices]
A. 1.1.1.122
B. 1.1.1.195
C. 3.2.1.20
D. 3.1.3.16
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

> The exact sequence matches the UniProt entry annotated EC 1.1.1.195, with experimental-evidence codes and a cited catalytic reaction for that EC. This supports choice B for the supplied protein, though the cited primary study was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Sequence motifs may suggest a zinc-dependent alcohol dehydrogenase and distinguish an oxidoreductase from the hydrolase choices, but they do not establish the specific substrate reaction needed to distinguish EC 1.1.1.195 from EC 1.1.1.122.


**Missing item-specific fact**

> The protein-specific catalytic activity and its EC annotation, particularly the substrate specificity distinguishing the two oxidoreductase options, are not supplied.


**Reason**

> The complete four-part EC number depends on protein-specific function not established by the sequence and choices alone; matching or recalling the database entry would be lookup or memorization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer-only sequence-matched evidence supports B. The input itself does not resolve the exact EC number, but no alternative is supported by the supplied evidence.


### Important caveats

- The UniProt annotation cites experimental evidence for the catalytic activity, but the primary paper was not independently assessed.
- Reviewer-only accession and annotation information supports the key; it was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Sequence motifs may suggest a zinc-dependent alcohol dehydrogenase and distinguish an oxidoreductase from the hydrolase choices, but they do not establish the specific substrate reaction needed to distinguish EC 1.1.1.195 from EC 1.1.1.122.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific catalytic activity and its EC annotation, particularly the substrate specificity distinguishing the two oxidoreductase options, are not supplied.",
    "reason": "The complete four-part EC number depends on protein-specific function not established by the sequence and choices alone; matching or recalling the database entry would be lookup or memorization."
  },
  "case_id": "EC_number_0130",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated EC 1.1.1.195, with experimental-evidence codes and a cited catalytic reaction for that EC. This supports choice B for the supplied protein, though the cited primary study was not independently reviewed here."
  },
  "important_caveats": [
    "The UniProt annotation cites experimental evidence for the catalytic activity, but the primary paper was not independently assessed.",
    "Reviewer-only accession and annotation information supports the key; it was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only sequence-matched evidence supports B. The input itself does not resolve the exact EC number, but no alternative is supported by the supplied evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0130",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated EC 1.1.1.195, with experimental-evidence codes and a cited catalytic reaction for that EC. This supports choice B for the supplied protein, though the cited primary study was not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Sequence motifs may suggest a zinc-dependent alcohol dehydrogenase and distinguish an oxidoreductase from the hydrolase choices, but they do not establish the specific substrate reaction needed to distinguish EC 1.1.1.195 from EC 1.1.1.122.",
    "missing_item_specific_fact": "The protein-specific catalytic activity and its EC annotation, particularly the substrate specificity distinguishing the two oxidoreductase options, are not supplied.",
    "reason": "The complete four-part EC number depends on protein-specific function not established by the sequence and choices alone; matching or recalling the database entry would be lookup or memorization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only sequence-matched evidence supports B. The input itself does not resolve the exact EC number, but no alternative is supported by the supplied evidence."
  },
  "important_caveats": [
    "The UniProt annotation cites experimental evidence for the catalytic activity, but the primary paper was not independently assessed.",
    "Reviewer-only accession and annotation information supports the key; it was not available to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A0U4AHM6 (CAD2_RAUSE) matches the benchmark sequence exactly (360 AA, SHA256 confirmed). The EC number 1.1.1.195 (cinnamyl alcohol dehydrogenase) is annotated with evidence code ECO:0000269 (experimental evidence) from PubMed:26715562 (Geissler et al., Planta 2016), which reports catalytic activity for (E)-cinnamyl alcohol + NADP(+) → (E)-cinnamaldehyde + NADPH + H(+). This is a well-supported experimental annotation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains zinc-dependent alcohol dehydrogenase motifs (e.g., the Cys/His-containing region 'GICHSDLHM') and a length (~360 AA) consistent with the zinc-ADH superfamily, which allows elimination of hydrolase options C (3.2.1.20, glycosidase) and D (3.1.3.16, phosphatase). However, distinguishing 1.1.1.195 (cinnamyl-alcohol dehydrogenase) from 1.1.1.122 (L-iditol 2-dehydrogenase) requires knowing the specific substrate-binding pocket architecture and active-site residues that confer selectivity for the aromatic cinnamyl alcohol versus the alditol iditol. These substrate-specificity determinants are not reliably identifiable from primary sequence alone without structural or functional data.


**Missing item-specific fact**

> The specific active-site residue configuration and substrate-binding pocket geometry that distinguishes cinnamyl-alcohol dehydrogenase (1.1.1.195) from L-iditol 2-dehydrogenase (1.1.1.122), both of which belong to the same zinc-dependent ADH family and share the same 3-digit EC class (1.1.1).


**Reason**

> While the oxidoreductase class (1.1.1) can be inferred from ADH-like motifs, the 4th-digit distinction between 122 and 195 depends on substrate specificity that is not derivable from sequence features alone. A model would need to recognize this exact protein as CAD2 from Rauvolfia serpentina or perform a database homology search, making this a lookup/memorization task for the critical A-vs-B choice.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Options A (1.1.1.122) and B (1.1.1.195) are both zinc-dependent alcohol dehydrogenases in the same 3-digit class. From sequence alone, a knowledgeable model could correctly assign the enzyme to class 1.1.1 but would struggle to justify the specific 4th-digit assignment without database lookup or structural knowledge of the substrate-binding site. Options C and D (hydrolases) are clearly eliminable.


### Important caveats

- The ECO:0000269 evidence code indicates the EC assignment is experimentally determined, not merely inferred by similarity.
- The sequence is from Rauvolfia serpentina, a plant rich in monoterpenoid indole alkaloids; the CAD-like enzyme (RsRR6) has a dual role in lignin biosynthesis and alkaloid metabolism, but the EC annotation 1.1.1.195 refers specifically to its cinnamyl-alcohol dehydrogenase activity.
- The reviewer-only evidence was unavailable to the evaluated model; the model must reason from sequence alone.
- The entry was first publicly released in 2025-06-18; the author data-construction date is unknown, so the model may or may not have encountered this entry during training.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains zinc-dependent alcohol dehydrogenase motifs (e.g., the Cys/His-containing region 'GICHSDLHM') and a length (~360 AA) consistent with the zinc-ADH superfamily, which allows elimination of hydrolase options C (3.2.1.20, glycosidase) and D (3.1.3.16, phosphatase). However, distinguishing 1.1.1.195 (cinnamyl-alcohol dehydrogenase) from 1.1.1.122 (L-iditol 2-dehydrogenase) requires knowing the specific substrate-binding pocket architecture and active-site residues that confer selectivity for the aromatic cinnamyl alcohol versus the alditol iditol. These substrate-specificity determinants are not reliably identifiable from primary sequence alone without structural or functional data.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific active-site residue configuration and substrate-binding pocket geometry that distinguishes cinnamyl-alcohol dehydrogenase (1.1.1.195) from L-iditol 2-dehydrogenase (1.1.1.122), both of which belong to the same zinc-dependent ADH family and share the same 3-digit EC class (1.1.1).",
    "reason": "While the oxidoreductase class (1.1.1) can be inferred from ADH-like motifs, the 4th-digit distinction between 122 and 195 depends on substrate specificity that is not derivable from sequence features alone. A model would need to recognize this exact protein as CAD2 from Rauvolfia serpentina or perform a database homology search, making this a lookup/memorization task for the critical A-vs-B choice."
  },
  "case_id": "EC_number_0130",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A0U4AHM6 (CAD2_RAUSE) matches the benchmark sequence exactly (360 AA, SHA256 confirmed). The EC number 1.1.1.195 (cinnamyl alcohol dehydrogenase) is annotated with evidence code ECO:0000269 (experimental evidence) from PubMed:26715562 (Geissler et al., Planta 2016), which reports catalytic activity for (E)-cinnamyl alcohol + NADP(+) → (E)-cinnamaldehyde + NADPH + H(+). This is a well-supported experimental annotation."
  },
  "important_caveats": [
    "The ECO:0000269 evidence code indicates the EC assignment is experimentally determined, not merely inferred by similarity.",
    "The sequence is from Rauvolfia serpentina, a plant rich in monoterpenoid indole alkaloids; the CAD-like enzyme (RsRR6) has a dual role in lignin biosynthesis and alkaloid metabolism, but the EC annotation 1.1.1.195 refers specifically to its cinnamyl-alcohol dehydrogenase activity.",
    "The reviewer-only evidence was unavailable to the evaluated model; the model must reason from sequence alone.",
    "The entry was first publicly released in 2025-06-18; the author data-construction date is unknown, so the model may or may not have encountered this entry during training."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Options A (1.1.1.122) and B (1.1.1.195) are both zinc-dependent alcohol dehydrogenases in the same 3-digit class. From sequence alone, a knowledgeable model could correctly assign the enzyme to class 1.1.1 but would struggle to justify the specific 4th-digit assignment without database lookup or structural knowledge of the substrate-binding site. Options C and D (hydrolases) are clearly eliminable."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0130",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A0U4AHM6 (CAD2_RAUSE) matches the benchmark sequence exactly (360 AA, SHA256 confirmed). The EC number 1.1.1.195 (cinnamyl alcohol dehydrogenase) is annotated with evidence code ECO:0000269 (experimental evidence) from PubMed:26715562 (Geissler et al., Planta 2016), which reports catalytic activity for (E)-cinnamyl alcohol + NADP(+) → (E)-cinnamaldehyde + NADPH + H(+). This is a well-supported experimental annotation.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains zinc-dependent alcohol dehydrogenase motifs (e.g., the Cys/His-containing region 'GICHSDLHM') and a length (~360 AA) consistent with the zinc-ADH superfamily, which allows elimination of hydrolase options C (3.2.1.20, glycosidase) and D (3.1.3.16, phosphatase). However, distinguishing 1.1.1.195 (cinnamyl-alcohol dehydrogenase) from 1.1.1.122 (L-iditol 2-dehydrogenase) requires knowing the specific substrate-binding pocket architecture and active-site residues that confer selectivity for the aromatic cinnamyl alcohol versus the alditol iditol. These substrate-specificity determinants are not reliably identifiable from primary sequence alone without structural or functional data.",
    "missing_item_specific_fact": "The specific active-site residue configuration and substrate-binding pocket geometry that distinguishes cinnamyl-alcohol dehydrogenase (1.1.1.195) from L-iditol 2-dehydrogenase (1.1.1.122), both of which belong to the same zinc-dependent ADH family and share the same 3-digit EC class (1.1.1).",
    "reason": "While the oxidoreductase class (1.1.1) can be inferred from ADH-like motifs, the 4th-digit distinction between 122 and 195 depends on substrate specificity that is not derivable from sequence features alone. A model would need to recognize this exact protein as CAD2 from Rauvolfia serpentina or perform a database homology search, making this a lookup/memorization task for the critical A-vs-B choice."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Options A (1.1.1.122) and B (1.1.1.195) are both zinc-dependent alcohol dehydrogenases in the same 3-digit class. From sequence alone, a knowledgeable model could correctly assign the enzyme to class 1.1.1 but would struggle to justify the specific 4th-digit assignment without database lookup or structural knowledge of the substrate-binding site. Options C and D (hydrolases) are clearly eliminable."
  },
  "important_caveats": [
    "The ECO:0000269 evidence code indicates the EC assignment is experimentally determined, not merely inferred by similarity.",
    "The sequence is from Rauvolfia serpentina, a plant rich in monoterpenoid indole alkaloids; the CAD-like enzyme (RsRR6) has a dual role in lignin biosynthesis and alkaloid metabolism, but the EC annotation 1.1.1.195 refers specifically to its cinnamyl-alcohol dehydrogenase activity.",
    "The reviewer-only evidence was unavailable to the evaluated model; the model must reason from sequence alone.",
    "The entry was first publicly released in 2025-06-18; the author data-construction date is unknown, so the model may or may not have encountered this entry during training."
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

**Accession:** `A0A0U4AHM6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 27. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U4AHM6.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:23.084054+00:00.  

```json
"A0A0U4AHM6"
```

Source SHA-256: `729526cd490e7835c63bf23151cfac76f61e2eee15d3331fc705b3c325c26d70`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U4AHM6.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:23.084054+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"26715562","source":"PubMed"}],"value":"Protein RR6"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"26715562","source":"PubMed"}],"value":"RsRR6"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"26715562","source":"PubMed"}],"value":"1.1.1.195"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"26715562","source":"PubMed"}],"value":"Cinnamyl alcohol dehydrogenase 2"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"26715562","source":"PubMed"}],"value":"RsCAD2"}]}}
```

Source SHA-256: `729526cd490e7835c63bf23151cfac76f61e2eee15d3331fc705b3c325c26d70`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U4AHM6.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:23.084054+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"right-to-left","evidences":[{"evidenceCode":"ECO:0000269","id":"26715562","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:10394"}}],"reaction":{"ecNumber":"1.1.1.195","evidences":[{"evidenceCode":"ECO:0000269","id":"26715562","source":"PubMed"}],"name":"(E)-cinnamyl alcohol + NADP(+) = (E)-cinnamaldehyde + NADPH + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:10392"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:16731"},{"database":"ChEBI","id":"CHEBI:33227"},{"database":"ChEBI","id":"CHEBI:57783"},{"database":"ChEBI","id":"CHEBI:58349"}]}}
```

Source SHA-256: `729526cd490e7835c63bf23151cfac76f61e2eee15d3331fc705b3c325c26d70`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U4AHM6.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:23.084054+00:00.  

```json
{"citation":{"authors":["Geissler M.","Burghard M.","Volk J.","Staniek A.","Warzecha H."],"citationCrossReferences":[{"database":"PubMed","id":"26715562"},{"database":"DOI","id":"10.1007/s00425-015-2446-6"}],"citationType":"journal article","firstPage":"813","id":"26715562","journal":"Planta","lastPage":"824","publicationDate":"2016","title":"A novel cinnamyl alcohol dehydrogenase (CAD)-like reductase contributes to the structural diversity of monoterpenoid indole alkaloids in Rauvolfia.","volume":"243"},"evidences":[{"evidenceCode":"ECO:0000312","id":"ALW82980.1","source":"EMBL"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","PROTEIN SEQUENCE OF 43-53 AND 66-77","FUNCTION","CATALYTIC ACTIVITY","TISSUE SPECIFICITY"]}
```

Source SHA-256: `729526cd490e7835c63bf23151cfac76f61e2eee15d3331fc705b3c325c26d70`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U4AHM6?format=txt&versions=27)  
**Locator:** `lines 6-10`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 27 / 1.  
**Retrieved:** 2026-11-02T04:24:26.964793+00:00.  

```text
DE   RecName: Full=Cinnamyl alcohol dehydrogenase 2 {ECO:0000303|PubMed:26715562};
DE            Short=RsCAD2 {ECO:0000303|PubMed:26715562};
DE            EC=1.1.1.195 {ECO:0000269|PubMed:26715562};
DE   AltName: Full=Protein RR6 {ECO:0000303|PubMed:26715562};
DE            Short=RsRR6 {ECO:0000303|PubMed:26715562};
```

Source SHA-256: `e85fa680b6b0f4b7eb19749997dc2e80edd7537f4e965d90637174bac9c0e458`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U4AHM6?format=txt&versions=27)  
**Locator:** `lines 29-35`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 27 / 1.  
**Retrieved:** 2026-11-02T04:24:26.964793+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=(E)-cinnamyl alcohol + NADP(+) = (E)-cinnamaldehyde + NADPH +
CC         H(+); Xref=Rhea:RHEA:10392, ChEBI:CHEBI:15378, ChEBI:CHEBI:16731,
CC         ChEBI:CHEBI:33227, ChEBI:CHEBI:57783, ChEBI:CHEBI:58349;
CC         EC=1.1.1.195; Evidence={ECO:0000269|PubMed:26715562};
CC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:10394;
CC         Evidence={ECO:0000269|PubMed:26715562};
```

Source SHA-256: `e85fa680b6b0f4b7eb19749997dc2e80edd7537f4e965d90637174bac9c0e458`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 130. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
