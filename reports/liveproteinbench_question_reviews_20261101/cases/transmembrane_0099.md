# transmembrane_0099

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **D** — 483..503

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKAFSVTCLGFAVFSSSICVNINILQQIGYIKQQVRQLSYYSQSSSSYIVVKLLPNIQPTDNSCEFKSVTQYNKTLSNLLLPIAENINNIASPSPGSRRHKRFAGIAIGIAALGVATAAQVTAAVSLVQAQTNARAIAAMKNSIQATNRAIFEVKEGTQQLAIAVQAIQDHINTIMNTQLNNMTCQILDNQLATFLGLYLTELTTVFQPQLINPALSPISIQALRSLLGSMTPAVVQATLSTSISAAEILSAGLMEGQIVSVLLDEMQMIVKVNIPTIVTQSNALVIDFYSISSFINNQESIIQLPDRILEIGNEQWSYPAKNCKLTRHHIFCQYNEAERLSLESKLCLAGNISACVFSPIAGSYMRRFVALDGTIVANCRSLTCLCKSPSYPIYQPDHHAVTTIDLTACQTLSLDGLDFSIVSLSNITYAENLTISLSQTINTQPIDISTELSKVNASLQNAVKYIKESNHQLLSVSVNSKIGAIIVTALVLSILSIIISLLFCCWAYIATKEIRRINFKTNHINTISSSVDDLIRY

[Multiple Choices]
A. 278..286; 308..323
B. 483..507
C. 483..503; 567..591
D. 483..503
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

> The sequence-matched UniProt annotation places a helical transmembrane region at 483..503, matching choice D. This annotation is computationally supported (ECO:0000255), not presented as direct experimental evidence.

Citations as saved: [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a conspicuous hydrophobic C-terminal stretch consistent with a membrane-spanning helix, distinguishing it from the other distant candidate regions.


**Missing item-specific fact**

> The exact annotated boundary, especially whether the region ends at 503 or extends to 507, is not uniquely established by general hydropathy reasoning.


**Reason**

> Sequence reasoning supports the location of a membrane-spanning helix, but selecting the precise annotated endpoint requires a protein-specific boundary annotation or comparable item-specific evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> Both choices include the strongly hydrophobic segment at 483 onward. The additional residues in B could be treated as part of an extended membrane-associated region, while the supplied evidence annotates the core helix as ending at 503.


### Important caveats

- The reviewer-only annotation matches the supplied sequence; the actual source snapshot used by the author is unknown.
- The cited transmembrane annotation is computationally evidenced, not independently validated here by primary experimental data.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a conspicuous hydrophobic C-terminal stretch consistent with a membrane-spanning helix, distinguishing it from the other distant candidate regions.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact annotated boundary, especially whether the region ends at 503 or extends to 507, is not uniquely established by general hydropathy reasoning.",
    "reason": "Sequence reasoning supports the location of a membrane-spanning helix, but selecting the precise annotated endpoint requires a protein-specific boundary annotation or comparable item-specific evidence."
  },
  "case_id": "transmembrane_0099",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation places a helical transmembrane region at 483..503, matching choice D. This annotation is computationally supported (ECO:0000255), not presented as direct experimental evidence."
  },
  "important_caveats": [
    "The reviewer-only annotation matches the supplied sequence; the actual source snapshot used by the author is unknown.",
    "The cited transmembrane annotation is computationally evidenced, not independently validated here by primary experimental data."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "Both choices include the strongly hydrophobic segment at 483 onward. The additional residues in B could be treated as part of an extended membrane-associated region, while the supplied evidence annotates the core helix as ending at 503."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0099",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation places a helical transmembrane region at 483..503, matching choice D. This annotation is computationally supported (ECO:0000255), not presented as direct experimental evidence.",
    "evidence_ids": ["C6", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a conspicuous hydrophobic C-terminal stretch consistent with a membrane-spanning helix, distinguishing it from the other distant candidate regions.",
    "missing_item_specific_fact": "The exact annotated boundary, especially whether the region ends at 503 or extends to 507, is not uniquely established by general hydropathy reasoning.",
    "reason": "Sequence reasoning supports the location of a membrane-spanning helix, but selecting the precise annotated endpoint requires a protein-specific boundary annotation or comparable item-specific evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "Both choices include the strongly hydrophobic segment at 483 onward. The additional residues in B could be treated as part of an extended membrane-associated region, while the supplied evidence annotates the core helix as ending at 503."
  },
  "important_caveats": [
    "The reviewer-only annotation matches the supplied sequence; the actual source snapshot used by the author is unknown.",
    "The cited transmembrane annotation is computationally evidenced, not independently validated here by primary experimental data."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q5SC53 (Mumps virus Fusion glycoprotein F0, 538 AA) annotates a single transmembrane helix at positions 483..503 (evidence code ECO:0000255, homology/proximity inference), flanked by an extracellular topological domain (20..482) and a cytoplasmic domain (504..538). This is consistent with the well-established single-pass type I membrane topology of paramyxovirus class I fusion glycoproteins. The sequence match is confirmed (SHA-256 identical). The annotation is computational/homology-based rather than directly experimental, but it is a standard, well-supported annotation for this protein family.

Citations as saved: [C6](#evidence-c6), [H3](#evidence-h3), [C5](#evidence-c5), [C7](#evidence-c7), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A model can reason from the sequence that (1) option A references positions (278-286, 308-323) in the large extracellular domain where the sequence is not hydrophobic, and (2) option C references positions 567-591 which exceed the protein length of 538 residues, so both are clearly eliminable. The remaining critical choice is between B (483..507) and D (483..503). The hydrophobic stretch in the C-terminal region is identifiable, but the exact C-terminal boundary of the TM helix at residue 503 versus 507 cannot be definitively resolved from sequence alone: residues 504-507 (C, C, W, A) are also hydrophobic, and the aromatic Trp at ~506 could plausibly be part of the membrane-water interface. Distinguishing 21-residue vs 25-residue TM helix boundaries depends on the specific annotation convention for this protein.


**Missing item-specific fact**

> The precise C-terminal boundary of the transmembrane helix (residue 503 vs 507) as annotated in UniProt for this specific Mumps virus F protein entry, which is a protein-specific annotation boundary not derivable from general hydrophobicity analysis alone.


**Reason**

> While general sequence reasoning eliminates options A and C, the decisive distinction between B (483..507) and D (483..503) requires knowledge of the exact annotation boundary. Both 21- and 25-residue TM helices are within the normal range for class I fusion proteins, and the sequence around 503-507 (FLCCWA) does not provide a clear-cut hydrophobicity cutoff. The answer depends on the specific UniProt annotation rather than a generalizable biological principle.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> From sequence analysis alone, both 483..503 (21 residues) and 483..507 (25 residues) are plausible TM helix boundaries. The residues at 504-507 (C, C, W, A) are hydrophobic, and Trp is a classic membrane-interface residue. Without the specific annotation, a knowledgeable model could reasonably select B. However, option C is definitively eliminable (positions beyond protein length) and A is eliminable (non-hydrophobic extracellular region).


### Important caveats

- The UniProt TM annotation uses evidence code ECO:0000255 (similarity/proximity), meaning it is inferred by homology to related paramyxovirus F proteins rather than from direct experimental measurement of this specific strain's TM boundaries.
- The sequence is from a vaccine strain (L-Zagreb) of Mumps virus genotype N; TM boundaries in paramyxovirus F proteins are generally well-conserved across strains.
- Option C's second segment (567..591) references positions beyond the 538-residue protein, making it trivially eliminable regardless of biological reasoning.
- The author key (D) matches the current UniProt annotation exactly, but the annotation is computational/homology-based, not experimentally determined for this specific protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A model can reason from the sequence that (1) option A references positions (278-286, 308-323) in the large extracellular domain where the sequence is not hydrophobic, and (2) option C references positions 567-591 which exceed the protein length of 538 residues, so both are clearly eliminable. The remaining critical choice is between B (483..507) and D (483..503). The hydrophobic stretch in the C-terminal region is identifiable, but the exact C-terminal boundary of the TM helix at residue 503 versus 507 cannot be definitively resolved from sequence alone: residues 504-507 (C, C, W, A) are also hydrophobic, and the aromatic Trp at ~506 could plausibly be part of the membrane-water interface. Distinguishing 21-residue vs 25-residue TM helix boundaries depends on the specific annotation convention for this protein.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The precise C-terminal boundary of the transmembrane helix (residue 503 vs 507) as annotated in UniProt for this specific Mumps virus F protein entry, which is a protein-specific annotation boundary not derivable from general hydrophobicity analysis alone.",
    "reason": "While general sequence reasoning eliminates options A and C, the decisive distinction between B (483..507) and D (483..503) requires knowledge of the exact annotation boundary. Both 21- and 25-residue TM helices are within the normal range for class I fusion proteins, and the sequence around 503-507 (FLCCWA) does not provide a clear-cut hydrophobicity cutoff. The answer depends on the specific UniProt annotation rather than a generalizable biological principle."
  },
  "case_id": "transmembrane_0099",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "H3",
      "C5",
      "C7",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q5SC53 (Mumps virus Fusion glycoprotein F0, 538 AA) annotates a single transmembrane helix at positions 483..503 (evidence code ECO:0000255, homology/proximity inference), flanked by an extracellular topological domain (20..482) and a cytoplasmic domain (504..538). This is consistent with the well-established single-pass type I membrane topology of paramyxovirus class I fusion glycoproteins. The sequence match is confirmed (SHA-256 identical). The annotation is computational/homology-based rather than directly experimental, but it is a standard, well-supported annotation for this protein family."
  },
  "important_caveats": [
    "The UniProt TM annotation uses evidence code ECO:0000255 (similarity/proximity), meaning it is inferred by homology to related paramyxovirus F proteins rather than from direct experimental measurement of this specific strain's TM boundaries.",
    "The sequence is from a vaccine strain (L-Zagreb) of Mumps virus genotype N; TM boundaries in paramyxovirus F proteins are generally well-conserved across strains.",
    "Option C's second segment (567..591) references positions beyond the 538-residue protein, making it trivially eliminable regardless of biological reasoning.",
    "The author key (D) matches the current UniProt annotation exactly, but the annotation is computational/homology-based, not experimentally determined for this specific protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "From sequence analysis alone, both 483..503 (21 residues) and 483..507 (25 residues) are plausible TM helix boundaries. The residues at 504-507 (C, C, W, A) are hydrophobic, and Trp is a classic membrane-interface residue. Without the specific annotation, a knowledgeable model could reasonably select B. However, option C is definitively eliminable (positions beyond protein length) and A is eliminable (non-hydrophobic extracellular region)."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0099",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q5SC53 (Mumps virus Fusion glycoprotein F0, 538 AA) annotates a single transmembrane helix at positions 483..503 (evidence code ECO:0000255, homology/proximity inference), flanked by an extracellular topological domain (20..482) and a cytoplasmic domain (504..538). This is consistent with the well-established single-pass type I membrane topology of paramyxovirus class I fusion glycoproteins. The sequence match is confirmed (SHA-256 identical). The annotation is computational/homology-based rather than directly experimental, but it is a standard, well-supported annotation for this protein family.",
    "evidence_ids": ["C6", "H3", "C5", "C7", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A model can reason from the sequence that (1) option A references positions (278-286, 308-323) in the large extracellular domain where the sequence is not hydrophobic, and (2) option C references positions 567-591 which exceed the protein length of 538 residues, so both are clearly eliminable. The remaining critical choice is between B (483..507) and D (483..503). The hydrophobic stretch in the C-terminal region is identifiable, but the exact C-terminal boundary of the TM helix at residue 503 versus 507 cannot be definitively resolved from sequence alone: residues 504-507 (C, C, W, A) are also hydrophobic, and the aromatic Trp at ~506 could plausibly be part of the membrane-water interface. Distinguishing 21-residue vs 25-residue TM helix boundaries depends on the specific annotation convention for this protein.",
    "missing_item_specific_fact": "The precise C-terminal boundary of the transmembrane helix (residue 503 vs 507) as annotated in UniProt for this specific Mumps virus F protein entry, which is a protein-specific annotation boundary not derivable from general hydrophobicity analysis alone.",
    "reason": "While general sequence reasoning eliminates options A and C, the decisive distinction between B (483..507) and D (483..503) requires knowledge of the exact annotation boundary. Both 21- and 25-residue TM helices are within the normal range for class I fusion proteins, and the sequence around 503-507 (FLCCWA) does not provide a clear-cut hydrophobicity cutoff. The answer depends on the specific UniProt annotation rather than a generalizable biological principle."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "From sequence analysis alone, both 483..503 (21 residues) and 483..507 (25 residues) are plausible TM helix boundaries. The residues at 504-507 (C, C, W, A) are hydrophobic, and Trp is a classic membrane-interface residue. Without the specific annotation, a knowledgeable model could reasonably select B. However, option C is definitively eliminable (positions beyond protein length) and A is eliminable (non-hydrophobic extracellular region)."
  },
  "important_caveats": [
    "The UniProt TM annotation uses evidence code ECO:0000255 (similarity/proximity), meaning it is inferred by homology to related paramyxovirus F proteins rather than from direct experimental measurement of this specific strain's TM boundaries.",
    "The sequence is from a vaccine strain (L-Zagreb) of Mumps virus genotype N; TM boundaries in paramyxovirus F proteins are generally well-conserved across strains.",
    "Option C's second segment (567..591) references positions beyond the 538-residue protein, making it trivially eliminable regardless of biological reasoning.",
    "The author key (D) matches the current UniProt annotation exactly, but the annotation is computational/homology-based, not experimentally determined for this specific protein."
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

**Accession:** `Q5SC53` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 80. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC53.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:22.414761+00:00.  

```json
{"description":"Extracellular","evidences":[{"evidenceCode":"ECO:0000250"}],"location":{"end":{"modifier":"EXACT","value":482},"start":{"modifier":"EXACT","value":20}},"type":"Topological domain"}
```

Source SHA-256: `72eeca0dc4f0e1b54320c79e260ae9238e7fcefb733b978db81bae5e0d233fa9`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC53.json)  
**Locator:** `/features/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:22.414761+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":503},"start":{"modifier":"EXACT","value":483}},"type":"Transmembrane"}
```

Source SHA-256: `72eeca0dc4f0e1b54320c79e260ae9238e7fcefb733b978db81bae5e0d233fa9`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC53.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:22.414761+00:00.  

```json
{"description":"Cytoplasmic","evidences":[{"evidenceCode":"ECO:0000250"}],"location":{"end":{"modifier":"EXACT","value":538},"start":{"modifier":"EXACT","value":504}},"type":"Topological domain"}
```

Source SHA-256: `72eeca0dc4f0e1b54320c79e260ae9238e7fcefb733b978db81bae5e0d233fa9`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC53?format=txt&versions=80)  
**Locator:** `lines 124-126`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 80 / 1.  
**Retrieved:** 2026-11-01T06:28:38.619336+00:00.  

```text
FT   TOPO_DOM        20..482
FT                   /note="Extracellular"
FT                   /evidence="ECO:0000250"
```

Source SHA-256: `afb9ab9d6093f040c16474e49b884836fed8582e6d2cecfa0264668dfd09db66`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC53?format=txt&versions=80)  
**Locator:** `lines 127-129`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 80 / 1.  
**Retrieved:** 2026-11-01T06:28:38.619336+00:00.  

```text
FT   TRANSMEM        483..503
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `afb9ab9d6093f040c16474e49b884836fed8582e6d2cecfa0264668dfd09db66`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC53?format=txt&versions=80)  
**Locator:** `lines 130-132`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 80 / 1.  
**Retrieved:** 2026-11-01T06:28:38.619336+00:00.  

```text
FT   TOPO_DOM        504..538
FT                   /note="Cytoplasmic"
FT                   /evidence="ECO:0000250"
```

Source SHA-256: `afb9ab9d6093f040c16474e49b884836fed8582e6d2cecfa0264668dfd09db66`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 99. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
