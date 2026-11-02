# pathway_0038

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **A** — Secondary metabolite biosynthesis

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSDQNDKKVEIIVFPYHGQGHMNTMLQFAKRIAWKNAKVTIATTLSTTNKMKSKVENAWGTSITLDSIYDDSDESQIKFMDRMARFEAAAASSLSKLLVQKKEEADNKVLLVYDGNLPWALDIAHEHGVRGAAFFPQSCATVATYYSLYQETQGKELETELPAVFPPLELIQRNVPNVFGLKFPEAVVAKNGKEYSPFVLFVLRQCINLEKADLLLFNQFDKLVEPGEVLQWMSKIFNVKTIGPTLPSSYIDKRIKDDVDYGFHAFNLDNNSCINWLNSKPARSVIYIAFGSSVHYSVEQMTEIAEALKSQPNNFLWAVRETEQKKLPEDFVQQTSEKGLMLSWCPQLDVLVHESISCFVTHCGWNSITEALSFGVPMLSVPQFLDQPVDAHFVEQVWGAGITVKRSEDGLVTRDEIVRCLEVLNNGEKAEEIKANVARWKVLAKEALDEGGSSDKHIDEIIEWVSSF

[Multiple Choices]
A. Secondary metabolite biosynthesis
B. L-threonine from L-aspartate: step 4/5. .
C. 7,8-dihydrofolate from 2-amino-4-hydroxy-6-hydroxymethyl-7,8-dihydropteridine diphosphate and 4-aminobenzoate: step 1/2. .
D. NAD(+) from nicotinamide D-ribonucleotide: step 1/1. .
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Pathway Prediction, which is to predict the primary metabolic or signaling pathway in which a given protein functions. Biological pathways are series of chemical reactions occurring within a cell that are essential for life. Based on the protein's amino acid sequence, you should identify the most relevant pathway from the given options.. The inputs provided by the user for this task include:

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

> The exact sequence matches a UniProt entry annotated as UDP-glucosyl transferase 74CD1 from Saponaria officinalis, with the pathway listed as secondary metabolite biosynthesis; terpenoid biosynthesis. The annotation cites a publication whose stated scope includes function and pathway. This supports choice A, while remaining an annotation based on that cited work rather than independently verified evidence here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may suggest a plant UDP-dependent glycosyltransferase, but that enzyme-family inference does not establish the particular metabolic pathway in which this protein functions.


**Missing item-specific fact**

> The protein's identity and experimentally characterized pathway role—UDP-glucosyl transferase 74CD1 involved in secondary-metabolite/terpenoid biosynthesis—are not supplied in the question.


**Reason**

> Distinguishing A from the specific primary-metabolism alternatives requires protein-specific functional or pathway information absent from the sequence context and choices. Recognizing the sequence or retrieving its annotation would be lookup, not reasoning from supplied evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched annotation supports A. The other options name specific pathway reactions not supported for this protein by the supplied information or the matched annotation.


### Important caveats

- The sequence match and pathway annotation come from reviewer-only sources and were not available to the evaluated model.
- The exact author data-source snapshot is unknown; a historical record available by the stated cutoff carries the same pathway annotation.
- The annotation cites experimental evidence, but the underlying paper was not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may suggest a plant UDP-dependent glycosyltransferase, but that enzyme-family inference does not establish the particular metabolic pathway in which this protein functions.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's identity and experimentally characterized pathway role—UDP-glucosyl transferase 74CD1 involved in secondary-metabolite/terpenoid biosynthesis—are not supplied in the question.",
    "reason": "Distinguishing A from the specific primary-metabolism alternatives requires protein-specific functional or pathway information absent from the sequence context and choices. Recognizing the sequence or retrieving its annotation would be lookup, not reasoning from supplied evidence."
  },
  "case_id": "pathway_0038",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as UDP-glucosyl transferase 74CD1 from Saponaria officinalis, with the pathway listed as secondary metabolite biosynthesis; terpenoid biosynthesis. The annotation cites a publication whose stated scope includes function and pathway. This supports choice A, while remaining an annotation based on that cited work rather than independently verified evidence here."
  },
  "important_caveats": [
    "The sequence match and pathway annotation come from reviewer-only sources and were not available to the evaluated model.",
    "The exact author data-source snapshot is unknown; a historical record available by the stated cutoff carries the same pathway annotation.",
    "The annotation cites experimental evidence, but the underlying paper was not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched annotation supports A. The other options name specific pathway reactions not supported for this protein by the supplied information or the matched annotation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0038",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as UDP-glucosyl transferase 74CD1 from Saponaria officinalis, with the pathway listed as secondary metabolite biosynthesis; terpenoid biosynthesis. The annotation cites a publication whose stated scope includes function and pathway. This supports choice A, while remaining an annotation based on that cited work rather than independently verified evidence here.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may suggest a plant UDP-dependent glycosyltransferase, but that enzyme-family inference does not establish the particular metabolic pathway in which this protein functions.",
    "missing_item_specific_fact": "The protein's identity and experimentally characterized pathway role—UDP-glucosyl transferase 74CD1 involved in secondary-metabolite/terpenoid biosynthesis—are not supplied in the question.",
    "reason": "Distinguishing A from the specific primary-metabolism alternatives requires protein-specific functional or pathway information absent from the sequence context and choices. Recognizing the sequence or retrieving its annotation would be lookup, not reasoning from supplied evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched annotation supports A. The other options name specific pathway reactions not supported for this protein by the supplied information or the matched annotation."
  },
  "important_caveats": [
    "The sequence match and pathway annotation come from reviewer-only sources and were not available to the evaluated model.",
    "The exact author data-source snapshot is unknown; a historical record available by the stated cutoff carries the same pathway annotation.",
    "The annotation cites experimental evidence, but the underlying paper was not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt annotation (C5, H3) explicitly assigns this protein (UDP-glucosyl transferase 74CD1, SoUGT74CD1, EC 2.4.1.-) to 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with experimental evidence (ECO:0000269, PubMed:39043959, Nat. Chem. Biol. 2025). The protein is a plant UGT involved in saponin (triterpenoid) glycosylation in Saponaria officinalis, which is a secondary metabolite pathway. The sequence matches the benchmark input exactly.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the PSPG (Plant Secondary Product Glycosyltransferase) motif, a well-known ~44-residue conserved signature of plant UGTs (visible in the region 'PQSCATVATYYSLYQETQGKELETELPAVFPPLELIQRNVPNVFGLKFPEAVVAKNGKEYSPFVLFVLRQCINLEKADLLLFNQFDKLVEPGEVLQWMSKIFNVKTIGPTLPSSYIDKRIKDDVDYGFHAFNLDNNSCINWLNSKPARSVIYIAFGSSVHYSVEQ'). Once identified as a plant UGT, general plant biochemistry knowledge establishes that these enzymes glycosylate secondary metabolites (triterpenoids/saponins, flavonoids, etc.), not primary metabolic intermediates. The three distractors (threonine biosynthesis, folate biosynthesis, NAD+ biosynthesis) involve entirely different enzyme classes (threonine synthase, dihydropteroate synthase, NAD synthetase) that would not possess a PSPG motif or UDP-sugar binding architecture.


**Missing item-specific fact**

> None critical. The PSPG motif is a general, widely-taught feature of plant UGTs. Exact substrate specificity (saponin vs. flavonoid glycosylation) would require the PubMed:39043959 study, but the pathway-level assignment to 'Secondary metabolite biosynthesis' follows from UGT identity alone.


**Reason**

> A model with general plant biochemistry knowledge can recognize the PSPG motif in the sequence, infer plant UGT identity, and eliminate the three primary-metabolism distractors because they involve unrelated enzyme classes. The reasoning chain (PSPG motif → plant UGT → secondary metabolite glycosylation) is a standard biological inference, not an item-specific lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Distractors B (threonine biosynthesis), C (folate biosynthesis), and D (NAD+ biosynthesis) each specify a single-step reaction catalyzed by a well-defined enzyme class (threonine synthase, dihydropteroate synthase, NAD synthetase) that bears no structural or mechanistic resemblance to a plant UGT. Only option A is compatible with a UDP-glycosyltransferase.


### Important caveats

- The PSPG motif recognition from raw sequence without alignment tools is non-trivial but is standard plant biochemistry knowledge; the motif region is visually distinctive in the 468-aa sequence.
- The UniProt annotation is supported by experimental evidence (ECO:0000269) from a 2025 Nat. Chem. Biol. paper characterizing saponin biosynthesis in soapwort, not merely by computational transfer.
- The specific sub-pathway is 'terpenoid biosynthesis' (saponin glycosylation); the answer choice 'Secondary metabolite biosynthesis' is the broader UniProt pathway heading, which is accurate.
- Reviewer-only evidence was absent from the evaluated model input; the reasoning assessment relies solely on what a model could extract from the sequence and general biological knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the PSPG (Plant Secondary Product Glycosyltransferase) motif, a well-known ~44-residue conserved signature of plant UGTs (visible in the region 'PQSCATVATYYSLYQETQGKELETELPAVFPPLELIQRNVPNVFGLKFPEAVVAKNGKEYSPFVLFVLRQCINLEKADLLLFNQFDKLVEPGEVLQWMSKIFNVKTIGPTLPSSYIDKRIKDDVDYGFHAFNLDNNSCINWLNSKPARSVIYIAFGSSVHYSVEQ'). Once identified as a plant UGT, general plant biochemistry knowledge establishes that these enzymes glycosylate secondary metabolites (triterpenoids/saponins, flavonoids, etc.), not primary metabolic intermediates. The three distractors (threonine biosynthesis, folate biosynthesis, NAD+ biosynthesis) involve entirely different enzyme classes (threonine synthase, dihydropteroate synthase, NAD synthetase) that would not possess a PSPG motif or UDP-sugar binding architecture.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The PSPG motif is a general, widely-taught feature of plant UGTs. Exact substrate specificity (saponin vs. flavonoid glycosylation) would require the PubMed:39043959 study, but the pathway-level assignment to 'Secondary metabolite biosynthesis' follows from UGT identity alone.",
    "reason": "A model with general plant biochemistry knowledge can recognize the PSPG motif in the sequence, infer plant UGT identity, and eliminate the three primary-metabolism distractors because they involve unrelated enzyme classes. The reasoning chain (PSPG motif → plant UGT → secondary metabolite glycosylation) is a standard biological inference, not an item-specific lookup."
  },
  "case_id": "pathway_0038",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt annotation (C5, H3) explicitly assigns this protein (UDP-glucosyl transferase 74CD1, SoUGT74CD1, EC 2.4.1.-) to 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with experimental evidence (ECO:0000269, PubMed:39043959, Nat. Chem. Biol. 2025). The protein is a plant UGT involved in saponin (triterpenoid) glycosylation in Saponaria officinalis, which is a secondary metabolite pathway. The sequence matches the benchmark input exactly."
  },
  "important_caveats": [
    "The PSPG motif recognition from raw sequence without alignment tools is non-trivial but is standard plant biochemistry knowledge; the motif region is visually distinctive in the 468-aa sequence.",
    "The UniProt annotation is supported by experimental evidence (ECO:0000269) from a 2025 Nat. Chem. Biol. paper characterizing saponin biosynthesis in soapwort, not merely by computational transfer.",
    "The specific sub-pathway is 'terpenoid biosynthesis' (saponin glycosylation); the answer choice 'Secondary metabolite biosynthesis' is the broader UniProt pathway heading, which is accurate.",
    "Reviewer-only evidence was absent from the evaluated model input; the reasoning assessment relies solely on what a model could extract from the sequence and general biological knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Distractors B (threonine biosynthesis), C (folate biosynthesis), and D (NAD+ biosynthesis) each specify a single-step reaction catalyzed by a well-defined enzyme class (threonine synthase, dihydropteroate synthase, NAD synthetase) that bears no structural or mechanistic resemblance to a plant UGT. Only option A is compatible with a UDP-glycosyltransferase."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0038",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt annotation (C5, H3) explicitly assigns this protein (UDP-glucosyl transferase 74CD1, SoUGT74CD1, EC 2.4.1.-) to 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with experimental evidence (ECO:0000269, PubMed:39043959, Nat. Chem. Biol. 2025). The protein is a plant UGT involved in saponin (triterpenoid) glycosylation in Saponaria officinalis, which is a secondary metabolite pathway. The sequence matches the benchmark input exactly.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the PSPG (Plant Secondary Product Glycosyltransferase) motif, a well-known ~44-residue conserved signature of plant UGTs (visible in the region 'PQSCATVATYYSLYQETQGKELETELPAVFPPLELIQRNVPNVFGLKFPEAVVAKNGKEYSPFVLFVLRQCINLEKADLLLFNQFDKLVEPGEVLQWMSKIFNVKTIGPTLPSSYIDKRIKDDVDYGFHAFNLDNNSCINWLNSKPARSVIYIAFGSSVHYSVEQ'). Once identified as a plant UGT, general plant biochemistry knowledge establishes that these enzymes glycosylate secondary metabolites (triterpenoids/saponins, flavonoids, etc.), not primary metabolic intermediates. The three distractors (threonine biosynthesis, folate biosynthesis, NAD+ biosynthesis) involve entirely different enzyme classes (threonine synthase, dihydropteroate synthase, NAD synthetase) that would not possess a PSPG motif or UDP-sugar binding architecture.",
    "missing_item_specific_fact": "None critical. The PSPG motif is a general, widely-taught feature of plant UGTs. Exact substrate specificity (saponin vs. flavonoid glycosylation) would require the PubMed:39043959 study, but the pathway-level assignment to 'Secondary metabolite biosynthesis' follows from UGT identity alone.",
    "reason": "A model with general plant biochemistry knowledge can recognize the PSPG motif in the sequence, infer plant UGT identity, and eliminate the three primary-metabolism distractors because they involve unrelated enzyme classes. The reasoning chain (PSPG motif → plant UGT → secondary metabolite glycosylation) is a standard biological inference, not an item-specific lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Distractors B (threonine biosynthesis), C (folate biosynthesis), and D (NAD+ biosynthesis) each specify a single-step reaction catalyzed by a well-defined enzyme class (threonine synthase, dihydropteroate synthase, NAD synthetase) that bears no structural or mechanistic resemblance to a plant UGT. Only option A is compatible with a UDP-glycosyltransferase."
  },
  "important_caveats": [
    "The PSPG motif recognition from raw sequence without alignment tools is non-trivial but is standard plant biochemistry knowledge; the motif region is visually distinctive in the 468-aa sequence.",
    "The UniProt annotation is supported by experimental evidence (ECO:0000269) from a 2025 Nat. Chem. Biol. paper characterizing saponin biosynthesis in soapwort, not merely by computational transfer.",
    "The specific sub-pathway is 'terpenoid biosynthesis' (saponin glycosylation); the answer choice 'Secondary metabolite biosynthesis' is the broader UniProt pathway heading, which is accurate.",
    "Reviewer-only evidence was absent from the evaluated model input; the reasoning assessment relies solely on what a model could extract from the sequence and general biological knowledge."
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

**Accession:** `A0AAW1M2U7` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 5. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1M2U7.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:41.867838+00:00.  

```json
"A0AAW1M2U7"
```

Source SHA-256: `9e83ecfae642612e0a9d04119aef39a3020c2e00cb00661e9ca5632043218b90`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1M2U7.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:41.867838+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39043959","source":"PubMed"}],"value":"2.4.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39043959","source":"PubMed"}],"value":"UDP-glucosyl transferase 74CD1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"39043959","source":"PubMed"}],"value":"SoUGT74CD1"}]}}
```

Source SHA-256: `9e83ecfae642612e0a9d04119aef39a3020c2e00cb00661e9ca5632043218b90`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1M2U7.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:41.867838+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39043959","source":"PubMed"}],"value":"Secondary metabolite biosynthesis; terpenoid biosynthesis"}]}
```

Source SHA-256: `9e83ecfae642612e0a9d04119aef39a3020c2e00cb00661e9ca5632043218b90`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1M2U7.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:41.867838+00:00.  

```json
{"citation":{"authors":["Jo S.","El-Demerdash A.","Owen C.","Srivastava V.","Wu D.","Kikuchi S.","Reed J.","Hodgson H.","Harkess A.","Shu S.","Plott C.","Jenkins J.","Williams M.","Boston L.-B.","Lacchini E.","Qu T.","Goossens A.","Grimwood J.","Schmutz J.","Leebens-Mack J.","Osbourn A."],"citationCrossReferences":[{"database":"PubMed","id":"39043959"},{"database":"DOI","id":"10.1038/s41589-024-01681-7"}],"citationType":"journal article","firstPage":"215","id":"39043959","journal":"Nat. Chem. Biol.","lastPage":"226","publicationDate":"2025","title":"Unlocking saponin biosynthesis in soapwort.","volume":"21"},"evidences":[{"evidenceCode":"ECO:0000312","id":"WWM48152.1","source":"EMBL"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","CATALYTIC ACTIVITY","TISSUE SPECIFICITY","PATHWAY","BIOTECHNOLOGY"]}
```

Source SHA-256: `9e83ecfae642612e0a9d04119aef39a3020c2e00cb00661e9ca5632043218b90`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1M2U7?format=txt&versions=5)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:45.433800+00:00.  

```text
ID   GT741_SAPOF             Reviewed;         468 AA.
AC   A0AAW1M2U7;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   27-NOV-2024, sequence version 1.
DT   28-JAN-2026, entry version 5.
DE   RecName: Full=UDP-glucosyl transferase 74CD1 {ECO:0000303|PubMed:39043959};
DE            Short=SoUGT74CD1 {ECO:0000303|PubMed:39043959};
DE            EC=2.4.1.- {ECO:0000269|PubMed:39043959};
GN   Name=UGT74CD1 {ECO:0000303|PubMed:39043959};
GN   Synonyms=Saoffv11011728m {ECO:0000303|PubMed:39043959};
GN   ORFNames=RND81_03G023500 {ECO:0000312|EMBL:KAK9740266.1};
OS   Saponaria officinalis (Common soapwort) (Lychnis saponaria).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   Caryophyllales; Caryophyllaceae; Caryophylleae; Saponaria.
OX   NCBI_TaxID=3572;
```

Source SHA-256: `6fb7981b56d64ad94695deca153a07b58aaf5f39453d0b61b923eef58aac0a67`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1M2U7?format=txt&versions=5)  
**Locator:** `lines 17-26`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:45.433800+00:00.  

```text
RN   [1] {ECO:0000312|EMBL:WWM48152.1}
RP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, TISSUE
RP   SPECIFICITY, PATHWAY, AND BIOTECHNOLOGY.
RX   PubMed=39043959; DOI=10.1038/s41589-024-01681-7;
RA   Jo S., El-Demerdash A., Owen C., Srivastava V., Wu D., Kikuchi S., Reed J.,
RA   Hodgson H., Harkess A., Shu S., Plott C., Jenkins J., Williams M.,
RA   Boston L.-B., Lacchini E., Qu T., Goossens A., Grimwood J., Schmutz J.,
RA   Leebens-Mack J., Osbourn A.;
RT   "Unlocking saponin biosynthesis in soapwort.";
RL   Nat. Chem. Biol. 21:215-226(2025).
```

Source SHA-256: `6fb7981b56d64ad94695deca153a07b58aaf5f39453d0b61b923eef58aac0a67`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1M2U7?format=txt&versions=5)  
**Locator:** `lines 52-53`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:45.433800+00:00.  

```text
CC   -!- PATHWAY: Secondary metabolite biosynthesis; terpenoid biosynthesis.
CC       {ECO:0000269|PubMed:39043959}.
```

Source SHA-256: `6fb7981b56d64ad94695deca153a07b58aaf5f39453d0b61b923eef58aac0a67`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 38. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
