# transmembrane_0132

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **B** — 24..44; 63..83; 84..104; 151..171; 173..193

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSEPNVRASFADNRRPLSKTKGQLLNMPPVITTALYTAFPVIFLLDKVLAFLTWTNDDPYTNFIAIAIYIMVVKYWTVVACTVLPTIIALGTCASLWFLKTTIDDLRSETAPPTIEEIIDTLINMQARFSYIVEPFSYFGSLSGSDYFNLGFSLIAITPCYIWLMTRIFTVRSFLLVFGVAWLSFHSSWSVATRHLLWRSIVIRKILTFTTGLKFSLVDKNIELTVLNDFQISNVGTGKTVEFHILQNQRRWLGVGWSNTLLPFERGPFTTEDLEKSWDSLESFQFPEITQATCRWRWLDANWKTDDSFAPGEGWIYYNNSWEEPSNTDSLTRFTRTKRWKRRALVIVEDDGTT

[Multiple Choices]
A. 24..44; 84..104; 151..171; 173..193
B. 24..44; 63..83; 84..104; 151..171; 173..193
C. 58..78
D. 27..44; 63..83; 84..104; 151..171; 173..193
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

> The exact matched sequence has UniProt transmembrane annotations at all five ranges in B, both in the current record and the archived historical record. These annotations carry ECO:0000255, indicating computational evidence rather than experimental validation.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains strongly hydrophobic stretches consistent with membrane-spanning helices, including the region around 63–104 and later hydrophobic segments. This supports a multi-pass membrane-protein interpretation but does not establish the exact annotated boundaries.


**Missing item-specific fact**

> The sequence alone does not specify the protein-specific transmembrane annotations or their precise residue boundaries; in particular, it does not resolve the 24-versus-27 start in the first candidate segment.


**Reason**

> Choosing the exact range set in B depends on the item-specific annotation or a prediction giving specific boundaries, not merely on general membrane-protein reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> B matches the supplied database annotation, but D differs only by starting the first candidate segment at residue 27. The sequence does not clearly determine that precise boundary, so D remains plausible from the provided input.


### Important caveats

- The sequence match establishes that the reviewer-only annotation concerns the supplied sequence; the accession and annotation were not provided to the evaluated model.
- The cited transmembrane features are computationally supported annotations, not direct experimental measurements.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains strongly hydrophobic stretches consistent with membrane-spanning helices, including the region around 63–104 and later hydrophobic segments. This supports a multi-pass membrane-protein interpretation but does not establish the exact annotated boundaries.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence alone does not specify the protein-specific transmembrane annotations or their precise residue boundaries; in particular, it does not resolve the 24-versus-27 start in the first candidate segment.",
    "reason": "Choosing the exact range set in B depends on the item-specific annotation or a prediction giving specific boundaries, not merely on general membrane-protein reasoning."
  },
  "case_id": "transmembrane_0132",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "H3",
      "H4",
      "H5",
      "H6",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The exact matched sequence has UniProt transmembrane annotations at all five ranges in B, both in the current record and the archived historical record. These annotations carry ECO:0000255, indicating computational evidence rather than experimental validation."
  },
  "important_caveats": [
    "The sequence match establishes that the reviewer-only annotation concerns the supplied sequence; the accession and annotation were not provided to the evaluated model.",
    "The cited transmembrane features are computationally supported annotations, not direct experimental measurements."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "B matches the supplied database annotation, but D differs only by starting the first candidate segment at residue 27. The sequence does not clearly determine that precise boundary, so D remains plausible from the provided input."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0132",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact matched sequence has UniProt transmembrane annotations at all five ranges in B, both in the current record and the archived historical record. These annotations carry ECO:0000255, indicating computational evidence rather than experimental validation.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "H3", "H4", "H5", "H6", "H7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains strongly hydrophobic stretches consistent with membrane-spanning helices, including the region around 63–104 and later hydrophobic segments. This supports a multi-pass membrane-protein interpretation but does not establish the exact annotated boundaries.",
    "missing_item_specific_fact": "The sequence alone does not specify the protein-specific transmembrane annotations or their precise residue boundaries; in particular, it does not resolve the 24-versus-27 start in the first candidate segment.",
    "reason": "Choosing the exact range set in B depends on the item-specific annotation or a prediction giving specific boundaries, not merely on general membrane-protein reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "B matches the supplied database annotation, but D differs only by starting the first candidate segment at residue 27. The sequence does not clearly determine that precise boundary, so D remains plausible from the provided input."
  },
  "important_caveats": [
    "The sequence match establishes that the reviewer-only annotation concerns the supplied sequence; the accession and annotation were not provided to the evaluated model.",
    "The cited transmembrane features are computationally supported annotations, not direct experimental measurements."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry W1QHP2 (PEX32_OGAPD) annotates exactly five transmembrane helical segments at 24..44, 63..83, 84..104, 151..171, and 173..193, matching Choice B precisely. The sequence in the question matches the database sequence (SHA-256 confirmed). However, all five annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred from a homolog rather than experimentally determined boundaries.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A model can reasonably eliminate Choice C (a single 21-residue segment ignores the multiple hydrophobic stretches) and Choice A (positions 63-83, FIAIAIYIMVVKYWTVVACTV, are strongly hydrophobic and clearly TM-like, so omitting them is indefensible). These two eliminations are reasoning-supported. However, the critical B-vs-D distinction hinges on whether the first TM helix begins at residue 24 (L-L-N) or 27 (M-P-P). Positions 24-25 are leucines (hydrophobic) while 26 is asparagine (polar); positions 28-29 are prolines (helix-breaking) within both candidate boundaries. No general biological principle uniquely resolves a 3-residue boundary shift in a proline-containing helix. The 'correct' boundary is set by whichever similarity-based prediction tool generated the ECO:0000255 annotation, not by a sequence-intrinsic rule.


**Missing item-specific fact**

> The exact start position (24 vs 27) of the first transmembrane helix as determined by the specific computational prediction algorithm used to generate the UniProt annotation. This is an algorithm-parameter-dependent boundary that cannot be uniquely derived from the sequence using general hydrophobicity principles.


**Reason**

> While the overall five-TM topology and the inclusion of 63..83 are identifiable from hydrophobicity analysis, the precise boundary of the first TM (24 vs 27) is a tool-specific prediction artifact. The ECO:0000255 evidence code confirms these are similarity-transferred predictions, not experimental measurements. Distinguishing B from D requires knowing the exact output of the prediction method, making the question partly lookup-dependent.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> Choices B and D differ only in the start of the first TM (24 vs 27). The three residues in question (L-L-N at 24-26) contain two strongly hydrophobic leucines followed by a polar asparagine. A reasonable hydrophobicity-window analysis could place the boundary at either position. Both 24..44 and 27..44 describe plausible 21-residue hydrophobic helices given the surrounding sequence context.


### Important caveats

- All five TM annotations carry ECO:0000255 (inferred by similarity), so the boundaries are computational predictions, not experimental determinations. The 'correct' boundaries reflect a specific prediction tool's output.
- The UniProt entry was first publicly released on 2025-02-05 (entry version 38 archived at 2026-01-28). The author's source snapshot is unknown but the sequence and annotations are stable (sequence version 1 unchanged since 2014).
- The identity of the protein (PEX32, a peroxisomal membrane protein tethering peroxisomes to the ER) was not provided in the question input; the model must work from the raw sequence alone.
- The B-vs-A distinction (inclusion of 63..83) is more robustly reasoning-supported than the B-vs-D distinction (24 vs 27 boundary).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A model can reasonably eliminate Choice C (a single 21-residue segment ignores the multiple hydrophobic stretches) and Choice A (positions 63-83, FIAIAIYIMVVKYWTVVACTV, are strongly hydrophobic and clearly TM-like, so omitting them is indefensible). These two eliminations are reasoning-supported. However, the critical B-vs-D distinction hinges on whether the first TM helix begins at residue 24 (L-L-N) or 27 (M-P-P). Positions 24-25 are leucines (hydrophobic) while 26 is asparagine (polar); positions 28-29 are prolines (helix-breaking) within both candidate boundaries. No general biological principle uniquely resolves a 3-residue boundary shift in a proline-containing helix. The 'correct' boundary is set by whichever similarity-based prediction tool generated the ECO:0000255 annotation, not by a sequence-intrinsic rule.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact start position (24 vs 27) of the first transmembrane helix as determined by the specific computational prediction algorithm used to generate the UniProt annotation. This is an algorithm-parameter-dependent boundary that cannot be uniquely derived from the sequence using general hydrophobicity principles.",
    "reason": "While the overall five-TM topology and the inclusion of 63..83 are identifiable from hydrophobicity analysis, the precise boundary of the first TM (24 vs 27) is a tool-specific prediction artifact. The ECO:0000255 evidence code confirms these are similarity-transferred predictions, not experimental measurements. Distinguishing B from D requires knowing the exact output of the prediction method, making the question partly lookup-dependent."
  },
  "case_id": "transmembrane_0132",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "H3",
      "H4",
      "H5",
      "H6",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry W1QHP2 (PEX32_OGAPD) annotates exactly five transmembrane helical segments at 24..44, 63..83, 84..104, 151..171, and 173..193, matching Choice B precisely. The sequence in the question matches the database sequence (SHA-256 confirmed). However, all five annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred from a homolog rather than experimentally determined boundaries."
  },
  "important_caveats": [
    "All five TM annotations carry ECO:0000255 (inferred by similarity), so the boundaries are computational predictions, not experimental determinations. The 'correct' boundaries reflect a specific prediction tool's output.",
    "The UniProt entry was first publicly released on 2025-02-05 (entry version 38 archived at 2026-01-28). The author's source snapshot is unknown but the sequence and annotations are stable (sequence version 1 unchanged since 2014).",
    "The identity of the protein (PEX32, a peroxisomal membrane protein tethering peroxisomes to the ER) was not provided in the question input; the model must work from the raw sequence alone.",
    "The B-vs-A distinction (inclusion of 63..83) is more robustly reasoning-supported than the B-vs-D distinction (24 vs 27 boundary)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "Choices B and D differ only in the start of the first TM (24 vs 27). The three residues in question (L-L-N at 24-26) contain two strongly hydrophobic leucines followed by a polar asparagine. A reasonable hydrophobicity-window analysis could place the boundary at either position. Both 24..44 and 27..44 describe plausible 21-residue hydrophobic helices given the surrounding sequence context."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0132",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry W1QHP2 (PEX32_OGAPD) annotates exactly five transmembrane helical segments at 24..44, 63..83, 84..104, 151..171, and 173..193, matching Choice B precisely. The sequence in the question matches the database sequence (SHA-256 confirmed). However, all five annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred from a homolog rather than experimentally determined boundaries.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "H3", "H4", "H5", "H6", "H7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A model can reasonably eliminate Choice C (a single 21-residue segment ignores the multiple hydrophobic stretches) and Choice A (positions 63-83, FIAIAIYIMVVKYWTVVACTV, are strongly hydrophobic and clearly TM-like, so omitting them is indefensible). These two eliminations are reasoning-supported. However, the critical B-vs-D distinction hinges on whether the first TM helix begins at residue 24 (L-L-N) or 27 (M-P-P). Positions 24-25 are leucines (hydrophobic) while 26 is asparagine (polar); positions 28-29 are prolines (helix-breaking) within both candidate boundaries. No general biological principle uniquely resolves a 3-residue boundary shift in a proline-containing helix. The 'correct' boundary is set by whichever similarity-based prediction tool generated the ECO:0000255 annotation, not by a sequence-intrinsic rule.",
    "missing_item_specific_fact": "The exact start position (24 vs 27) of the first transmembrane helix as determined by the specific computational prediction algorithm used to generate the UniProt annotation. This is an algorithm-parameter-dependent boundary that cannot be uniquely derived from the sequence using general hydrophobicity principles.",
    "reason": "While the overall five-TM topology and the inclusion of 63..83 are identifiable from hydrophobicity analysis, the precise boundary of the first TM (24 vs 27) is a tool-specific prediction artifact. The ECO:0000255 evidence code confirms these are similarity-transferred predictions, not experimental measurements. Distinguishing B from D requires knowing the exact output of the prediction method, making the question partly lookup-dependent."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "Choices B and D differ only in the start of the first TM (24 vs 27). The three residues in question (L-L-N at 24-26) contain two strongly hydrophobic leucines followed by a polar asparagine. A reasonable hydrophobicity-window analysis could place the boundary at either position. Both 24..44 and 27..44 describe plausible 21-residue hydrophobic helices given the surrounding sequence context."
  },
  "important_caveats": [
    "All five TM annotations carry ECO:0000255 (inferred by similarity), so the boundaries are computational predictions, not experimental determinations. The 'correct' boundaries reflect a specific prediction tool's output.",
    "The UniProt entry was first publicly released on 2025-02-05 (entry version 38 archived at 2026-01-28). The author's source snapshot is unknown but the sequence and annotations are stable (sequence version 1 unchanged since 2014).",
    "The identity of the protein (PEX32, a peroxisomal membrane protein tethering peroxisomes to the ER) was not provided in the question input; the model must work from the raw sequence alone.",
    "The B-vs-A distinction (inclusion of 63..83) is more robustly reasoning-supported than the B-vs-D distinction (24 vs 27 boundary)."
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

**Accession:** `W1QHP2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 38. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QHP2.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:30.706856+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":44},"start":{"modifier":"EXACT","value":24}},"type":"Transmembrane"}
```

Source SHA-256: `496aea11aa2b41aaa21a1680c1288b30d7312fd99c41cdd11ef292e508959dcd`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QHP2.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:30.706856+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":83},"start":{"modifier":"EXACT","value":63}},"type":"Transmembrane"}
```

Source SHA-256: `496aea11aa2b41aaa21a1680c1288b30d7312fd99c41cdd11ef292e508959dcd`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QHP2.json)  
**Locator:** `/features/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:30.706856+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":104},"start":{"modifier":"EXACT","value":84}},"type":"Transmembrane"}
```

Source SHA-256: `496aea11aa2b41aaa21a1680c1288b30d7312fd99c41cdd11ef292e508959dcd`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QHP2.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:30.706856+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":171},"start":{"modifier":"EXACT","value":151}},"type":"Transmembrane"}
```

Source SHA-256: `496aea11aa2b41aaa21a1680c1288b30d7312fd99c41cdd11ef292e508959dcd`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QHP2.json)  
**Locator:** `/features/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:30.706856+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":193},"start":{"modifier":"EXACT","value":173}},"type":"Transmembrane"}
```

Source SHA-256: `496aea11aa2b41aaa21a1680c1288b30d7312fd99c41cdd11ef292e508959dcd`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QHP2?format=txt&versions=38)  
**Locator:** `lines 80-82`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-01T06:28:55.253871+00:00.  

```text
FT   TRANSMEM        24..44
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `95f12c3e5266dcfc076c0bab33c3d654a00f2c142918715c03c5fb98c2acd8be`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QHP2?format=txt&versions=38)  
**Locator:** `lines 83-85`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-01T06:28:55.253871+00:00.  

```text
FT   TRANSMEM        63..83
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `95f12c3e5266dcfc076c0bab33c3d654a00f2c142918715c03c5fb98c2acd8be`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QHP2?format=txt&versions=38)  
**Locator:** `lines 86-88`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-01T06:28:55.253871+00:00.  

```text
FT   TRANSMEM        84..104
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `95f12c3e5266dcfc076c0bab33c3d654a00f2c142918715c03c5fb98c2acd8be`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QHP2?format=txt&versions=38)  
**Locator:** `lines 89-91`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-01T06:28:55.253871+00:00.  

```text
FT   TRANSMEM        151..171
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `95f12c3e5266dcfc076c0bab33c3d654a00f2c142918715c03c5fb98c2acd8be`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QHP2?format=txt&versions=38)  
**Locator:** `lines 92-94`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-01T06:28:55.253871+00:00.  

```text
FT   TRANSMEM        173..193
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `95f12c3e5266dcfc076c0bab33c3d654a00f2c142918715c03c5fb98c2acd8be`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 132. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
