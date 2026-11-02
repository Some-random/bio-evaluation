# transmembrane_0041

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **A** — 14..34; 42..62; 478..498; 508..528; 546..566; 581..601; 636..656; 669..689

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSPHNTCTLQITRALLSRLHILFHSALVASVFYYRFSNFSSGPAWALMTFAELTLAFIWALTQAFRWRPVVRAVFGPEEIDPAQLPGLDVFICTADPRKEPVMEVMNSVVSALALDYPAEKLAVYLSDDGGSPLTREVIREAAVFGKYWVGFCGKYNVKTRCPEAYFSSFCDGERVDHNQDYLNDELSVKSKFEAFKKYVQKASEDATKCIVVNDRPSCVEIIHDSKQNGEGEVKMPLLVYVAREKRPGFNHHAKAGAINTLLRVSGLLSNSPFFLVLDCDMYCNDPTSARQAMCFHLDPKLAPSLAFVQYPQIFYNTSKNDIYDGQARAAFKTKYQGMDGLRGPVMSGTGYFLKRKALYGKPHDQDELLREQPTKAFGSSKIFIASLGENTCVALKGLSKDELLQETQKLAACTYESNTLWGSEVGYSYDCLLESTYCGYLLHCKGWISVYLYPKKPCFLGCATVDMNDAMLQIMKWTSGLIGVGISKFSPFTYAMSRISIMQSLCYAYFAFSGLFAVFFLIYGVVLPYSLLQGVPLFPKAGDPWLLAFAGVFISSLLQHLYEVLSSGETVKAWWNEQRIWIIKSITACLFGLLDAMLNKIGVLKASFRLTNKAVDKQKLDKYEKGRFDFQGAQMFMVPLMILVVFNLVSFFGGLRRTVIHKNYEDMFAQLFLSLFILALSYPIMEEIVRKARKGRS

[Multiple Choices]
A. 14..34; 42..62; 478..498; 508..528; 546..566; 581..601; 636..656; 669..689
B. 42..62; 478..498; 508..528; 546..566; 581..601; 636..656; 669..689
C. 14..34; 42..62; 478..498; 508..528; 546..566; 581..601; 636..656; 664..692
D. 31..51; 112..132; 133..153; 179..199; 212..232; 350..370; 378..398; 406..426; 428..448; 475..495
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Transmembrane Region Prediction, which is to predict a region of the protein that spans across a cell membrane. These transmembrane domains are typically hydrophobic alpha-helices that anchor the protein within the lipid bilayer or form channels. Based on the provided amino acid sequence, you must select the option that correctly identifies the start and end positions of a segment that crosses the membrane.. The inputs provided by the user for this task include:

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

> The sequence matches the cited UniProt record, whose current and historical annotations list all eight regions in A. These are computational helical transmembrane annotations (ECO:0000255), not evidence of direct experimental measurement.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has multiple hydrophobic stretches of roughly membrane-spanning helix length, including the N-terminal stretch at 14..34 and a later one at 42..62; thus the sequence supports including 14..34, which distinguishes A from B. The C-terminal hydrophobic core also favors the narrower 669..689 interval over the longer 664..692 option.


**Missing item-specific fact**

> No protein-specific annotation or experimental result is required to make a defensible sequence-based distinction, although such information would be needed to establish exact boundaries experimentally.


**Reason**

> Hydropathy and typical transmembrane-helix length provide meaningful grounds for choosing A among the options. These support a prediction, not certainty about the precise endpoints or membrane topology.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> A is the best-supported choice from the hydrophobic segments and candidate boundaries. The exact endpoints remain predictive rather than experimentally established.


### Important caveats

- The cited UniProt features are computational annotations, not direct experimental validation.
- The reviewer-only accession and annotation evidence were not supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has multiple hydrophobic stretches of roughly membrane-spanning helix length, including the N-terminal stretch at 14..34 and a later one at 42..62; thus the sequence supports including 14..34, which distinguishes A from B. The C-terminal hydrophobic core also favors the narrower 669..689 interval over the longer 664..692 option.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No protein-specific annotation or experimental result is required to make a defensible sequence-based distinction, although such information would be needed to establish exact boundaries experimentally.",
    "reason": "Hydropathy and typical transmembrane-helix length provide meaningful grounds for choosing A among the options. These support a prediction, not certainty about the precise endpoints or membrane topology."
  },
  "case_id": "transmembrane_0041",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "C10",
      "C11",
      "C12",
      "H3",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9",
      "H10"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the cited UniProt record, whose current and historical annotations list all eight regions in A. These are computational helical transmembrane annotations (ECO:0000255), not evidence of direct experimental measurement."
  },
  "important_caveats": [
    "The cited UniProt features are computational annotations, not direct experimental validation.",
    "The reviewer-only accession and annotation evidence were not supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A is the best-supported choice from the hydrophobic segments and candidate boundaries. The exact endpoints remain predictive rather than experimentally established."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0041",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the cited UniProt record, whose current and historical annotations list all eight regions in A. These are computational helical transmembrane annotations (ECO:0000255), not evidence of direct experimental measurement.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has multiple hydrophobic stretches of roughly membrane-spanning helix length, including the N-terminal stretch at 14..34 and a later one at 42..62; thus the sequence supports including 14..34, which distinguishes A from B. The C-terminal hydrophobic core also favors the narrower 669..689 interval over the longer 664..692 option.",
    "missing_item_specific_fact": "No protein-specific annotation or experimental result is required to make a defensible sequence-based distinction, although such information would be needed to establish exact boundaries experimentally.",
    "reason": "Hydropathy and typical transmembrane-helix length provide meaningful grounds for choosing A among the options. These support a prediction, not certainty about the precise endpoints or membrane topology."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A is the best-supported choice from the hydrophobic segments and candidate boundaries. The exact endpoints remain predictive rather than experimentally established."
  },
  "important_caveats": [
    "The cited UniProt features are computational annotations, not direct experimental validation.",
    "The reviewer-only accession and annotation evidence were not supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0AAW1HA02 (CSL1_SAPOF, Quillaic acid 3-O-glycosyltransferase CSL1 from Saponaria officinalis) annotates exactly 8 helical transmembrane regions at 14..34, 42..62, 478..498, 508..528, 546..566, 581..601, 636..656, and 669..689, matching Choice A precisely. The benchmark sequence SHA256 matches the UniProt sequence. All annotations carry evidence code ECO:0000255 (inferred by similarity), confirming these are computational predictions rather than experimental measurements.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A model can eliminate D (regions at 31..51, 112..132, etc. do not correspond to the actual TM topology of this CSL protein) and can argue for including the N-terminal hydrophobic stretch at ~14..34 (eliminating B), since residues 14-34 contain a clear hydrophobic segment (LQITRALLSRLHILFHSALVASVF). However, the critical A-vs-C distinction—whether the last TM spans 669..689 or 664..692—cannot be resolved by general hydrophobicity reasoning; it is a 5-residue boundary shift on each end that depends on the specific prediction algorithm's window size and threshold.


**Missing item-specific fact**

> The exact TM boundary predictions from the specific tool that generated the UniProt annotation (ECO:0000255, similarity-based inference). The 5-residue boundary differences between A and C (664 vs 669 start; 692 vs 689 end) are algorithm-specific outputs not derivable from first-principles hydrophobicity analysis.


**Reason**

> While broad TM identification and elimination of D are possible by reasoning, the precise boundary positions (especially the A-vs-C distinction) depend on the output of a particular prediction algorithm. The ECO:0000255 evidence code confirms these are computational predictions, not experimentally determined boundaries. Selecting A over C requires knowing the exact tool output, making this lookup-dependent at the level of precision the question demands.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> Choices A and C differ only in the last TM boundary (669..689 vs 664..692). A hydrophobicity analysis with a slightly wider window or lower threshold could plausibly yield the 664..692 boundaries. Without the specific prediction tool, both boundaries are within the range of reasonable hydrophobic helix predictions for this C-terminal region. Choice B is also close to A (merely omits the first TM), though the 14..34 region is clearly hydrophobic enough to favor its inclusion.


### Important caveats

- All TM annotations carry ECO:0000255 (inferred by similarity), meaning they are computational predictions, not experimental measurements. Exact boundaries are prediction-tool-dependent.
- The UniProt entry was first public on 2025-06-18; the benchmark was constructed from this or a closely contemporaneous annotation. The prediction tool used is not specified in the annotation.
- The protein is a CSL (cellulose synthase-like) family member, which typically has 8 TM domains—a family-level expectation that supports the 8-region answer but does not fix exact boundaries.
- Sequence match between benchmark input and UniProt entry is confirmed (SHA256 identical, 698 residues).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A model can eliminate D (regions at 31..51, 112..132, etc. do not correspond to the actual TM topology of this CSL protein) and can argue for including the N-terminal hydrophobic stretch at ~14..34 (eliminating B), since residues 14-34 contain a clear hydrophobic segment (LQITRALLSRLHILFHSALVASVF). However, the critical A-vs-C distinction—whether the last TM spans 669..689 or 664..692—cannot be resolved by general hydrophobicity reasoning; it is a 5-residue boundary shift on each end that depends on the specific prediction algorithm's window size and threshold.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact TM boundary predictions from the specific tool that generated the UniProt annotation (ECO:0000255, similarity-based inference). The 5-residue boundary differences between A and C (664 vs 669 start; 692 vs 689 end) are algorithm-specific outputs not derivable from first-principles hydrophobicity analysis.",
    "reason": "While broad TM identification and elimination of D are possible by reasoning, the precise boundary positions (especially the A-vs-C distinction) depend on the output of a particular prediction algorithm. The ECO:0000255 evidence code confirms these are computational predictions, not experimentally determined boundaries. Selecting A over C requires knowing the exact tool output, making this lookup-dependent at the level of precision the question demands."
  },
  "case_id": "transmembrane_0041",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "C10",
      "C11",
      "C12",
      "H3",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9",
      "H10"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0AAW1HA02 (CSL1_SAPOF, Quillaic acid 3-O-glycosyltransferase CSL1 from Saponaria officinalis) annotates exactly 8 helical transmembrane regions at 14..34, 42..62, 478..498, 508..528, 546..566, 581..601, 636..656, and 669..689, matching Choice A precisely. The benchmark sequence SHA256 matches the UniProt sequence. All annotations carry evidence code ECO:0000255 (inferred by similarity), confirming these are computational predictions rather than experimental measurements."
  },
  "important_caveats": [
    "All TM annotations carry ECO:0000255 (inferred by similarity), meaning they are computational predictions, not experimental measurements. Exact boundaries are prediction-tool-dependent.",
    "The UniProt entry was first public on 2025-06-18; the benchmark was constructed from this or a closely contemporaneous annotation. The prediction tool used is not specified in the annotation.",
    "The protein is a CSL (cellulose synthase-like) family member, which typically has 8 TM domains—a family-level expectation that supports the 8-region answer but does not fix exact boundaries.",
    "Sequence match between benchmark input and UniProt entry is confirmed (SHA256 identical, 698 residues)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "Choices A and C differ only in the last TM boundary (669..689 vs 664..692). A hydrophobicity analysis with a slightly wider window or lower threshold could plausibly yield the 664..692 boundaries. Without the specific prediction tool, both boundaries are within the range of reasonable hydrophobic helix predictions for this C-terminal region. Choice B is also close to A (merely omits the first TM), though the 14..34 region is clearly hydrophobic enough to favor its inclusion."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0041",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0AAW1HA02 (CSL1_SAPOF, Quillaic acid 3-O-glycosyltransferase CSL1 from Saponaria officinalis) annotates exactly 8 helical transmembrane regions at 14..34, 42..62, 478..498, 508..528, 546..566, 581..601, 636..656, and 669..689, matching Choice A precisely. The benchmark sequence SHA256 matches the UniProt sequence. All annotations carry evidence code ECO:0000255 (inferred by similarity), confirming these are computational predictions rather than experimental measurements.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A model can eliminate D (regions at 31..51, 112..132, etc. do not correspond to the actual TM topology of this CSL protein) and can argue for including the N-terminal hydrophobic stretch at ~14..34 (eliminating B), since residues 14-34 contain a clear hydrophobic segment (LQITRALLSRLHILFHSALVASVF). However, the critical A-vs-C distinction—whether the last TM spans 669..689 or 664..692—cannot be resolved by general hydrophobicity reasoning; it is a 5-residue boundary shift on each end that depends on the specific prediction algorithm's window size and threshold.",
    "missing_item_specific_fact": "The exact TM boundary predictions from the specific tool that generated the UniProt annotation (ECO:0000255, similarity-based inference). The 5-residue boundary differences between A and C (664 vs 669 start; 692 vs 689 end) are algorithm-specific outputs not derivable from first-principles hydrophobicity analysis.",
    "reason": "While broad TM identification and elimination of D are possible by reasoning, the precise boundary positions (especially the A-vs-C distinction) depend on the output of a particular prediction algorithm. The ECO:0000255 evidence code confirms these are computational predictions, not experimentally determined boundaries. Selecting A over C requires knowing the exact tool output, making this lookup-dependent at the level of precision the question demands."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "Choices A and C differ only in the last TM boundary (669..689 vs 664..692). A hydrophobicity analysis with a slightly wider window or lower threshold could plausibly yield the 664..692 boundaries. Without the specific prediction tool, both boundaries are within the range of reasonable hydrophobic helix predictions for this C-terminal region. Choice B is also close to A (merely omits the first TM), though the 14..34 region is clearly hydrophobic enough to favor its inclusion."
  },
  "important_caveats": [
    "All TM annotations carry ECO:0000255 (inferred by similarity), meaning they are computational predictions, not experimental measurements. Exact boundaries are prediction-tool-dependent.",
    "The UniProt entry was first public on 2025-06-18; the benchmark was constructed from this or a closely contemporaneous annotation. The prediction tool used is not specified in the annotation.",
    "The protein is a CSL (cellulose synthase-like) family member, which typically has 8 TM domains—a family-level expectation that supports the 8-region answer but does not fix exact boundaries.",
    "Sequence match between benchmark input and UniProt entry is confirmed (SHA256 identical, 698 residues)."
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

**Accession:** `A0AAW1HA02` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 5. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1HA02.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:29.725144+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":34},"start":{"modifier":"EXACT","value":14}},"type":"Transmembrane"}
```

Source SHA-256: `ced1a85f4bd178ca3a21351af4130064faa92db4910f1c839491e60a08e4daf9`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1HA02.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:29.725144+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":62},"start":{"modifier":"EXACT","value":42}},"type":"Transmembrane"}
```

Source SHA-256: `ced1a85f4bd178ca3a21351af4130064faa92db4910f1c839491e60a08e4daf9`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1HA02.json)  
**Locator:** `/features/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:29.725144+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":498},"start":{"modifier":"EXACT","value":478}},"type":"Transmembrane"}
```

Source SHA-256: `ced1a85f4bd178ca3a21351af4130064faa92db4910f1c839491e60a08e4daf9`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1HA02.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:29.725144+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":528},"start":{"modifier":"EXACT","value":508}},"type":"Transmembrane"}
```

Source SHA-256: `ced1a85f4bd178ca3a21351af4130064faa92db4910f1c839491e60a08e4daf9`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1HA02.json)  
**Locator:** `/features/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:29.725144+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":566},"start":{"modifier":"EXACT","value":546}},"type":"Transmembrane"}
```

Source SHA-256: `ced1a85f4bd178ca3a21351af4130064faa92db4910f1c839491e60a08e4daf9`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1HA02.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:29.725144+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":601},"start":{"modifier":"EXACT","value":581}},"type":"Transmembrane"}
```

Source SHA-256: `ced1a85f4bd178ca3a21351af4130064faa92db4910f1c839491e60a08e4daf9`.

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1HA02.json)  
**Locator:** `/features/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:29.725144+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":656},"start":{"modifier":"EXACT","value":636}},"type":"Transmembrane"}
```

Source SHA-256: `ced1a85f4bd178ca3a21351af4130064faa92db4910f1c839491e60a08e4daf9`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1HA02.json)  
**Locator:** `/features/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:29.725144+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":689},"start":{"modifier":"EXACT","value":669}},"type":"Transmembrane"}
```

Source SHA-256: `ced1a85f4bd178ca3a21351af4130064faa92db4910f1c839491e60a08e4daf9`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1HA02?format=txt&versions=5)  
**Locator:** `lines 94-96`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:31.462058+00:00.  

```text
FT   TRANSMEM        14..34
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `e565ff77eec1b44dd5ee2a404680772ba99cc36e620917e40ca47a72ffd020f9`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1HA02?format=txt&versions=5)  
**Locator:** `lines 97-99`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:31.462058+00:00.  

```text
FT   TRANSMEM        42..62
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `e565ff77eec1b44dd5ee2a404680772ba99cc36e620917e40ca47a72ffd020f9`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1HA02?format=txt&versions=5)  
**Locator:** `lines 100-102`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:31.462058+00:00.  

```text
FT   TRANSMEM        478..498
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `e565ff77eec1b44dd5ee2a404680772ba99cc36e620917e40ca47a72ffd020f9`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1HA02?format=txt&versions=5)  
**Locator:** `lines 103-105`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:31.462058+00:00.  

```text
FT   TRANSMEM        508..528
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `e565ff77eec1b44dd5ee2a404680772ba99cc36e620917e40ca47a72ffd020f9`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1HA02?format=txt&versions=5)  
**Locator:** `lines 106-108`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:31.462058+00:00.  

```text
FT   TRANSMEM        546..566
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `e565ff77eec1b44dd5ee2a404680772ba99cc36e620917e40ca47a72ffd020f9`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1HA02?format=txt&versions=5)  
**Locator:** `lines 109-111`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:31.462058+00:00.  

```text
FT   TRANSMEM        581..601
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `e565ff77eec1b44dd5ee2a404680772ba99cc36e620917e40ca47a72ffd020f9`.

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1HA02?format=txt&versions=5)  
**Locator:** `lines 112-114`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:31.462058+00:00.  

```text
FT   TRANSMEM        636..656
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `e565ff77eec1b44dd5ee2a404680772ba99cc36e620917e40ca47a72ffd020f9`.

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1HA02?format=txt&versions=5)  
**Locator:** `lines 115-117`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:31.462058+00:00.  

```text
FT   TRANSMEM        669..689
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `e565ff77eec1b44dd5ee2a404680772ba99cc36e620917e40ca47a72ffd020f9`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 41. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
