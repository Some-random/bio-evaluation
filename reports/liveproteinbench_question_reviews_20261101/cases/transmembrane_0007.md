# transmembrane_0007

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **B** — 65..85; 137..157; 158..178; 187..207; 216..236; 250..270; 334..354; 367..387; 392..412; 423..443; 455..475; 489..509

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MASSDSNAKLASQRLHSCAGGEESSGQCLEKQGAGARLRGWLAQLLPRADLPGARQKTPFNLNRYVLLLLYSIVVFTTGAVFYGWTALSAMIFKNDGFAYLCPKDASGVYVPDLRATQGKLYICDEQDAAVQKLYTMTFAVACLMSAGAGTLLDWLGPLWTELLGQLLNLVGWLFLAFSTVDRPLYYPALVFIGLGADASMLPTLCIRHLFPGSTGLIITILGSAASASFGIPLVLNTIVENHGVSVRDVSIGYCFFGPVLGVLVALLFMPRRGFALDDAGTIFREPDSGEGEGEAGPYALENGAQGGESQNAQETRRRKLLDPIVSSSFWTQFFSIRYFLIVLYFVVVSWATSYYQQAARRMFSEDVVSVIEVLLPLSFIPCILLGKVADVVGIIRVLFVMNTSGLLTYVFSFFKTDATGYLSACCFMVYMSLLTSQVYVYVEGTFSPNHFGKLIGISNLTGGLLSLVSNPLYENITVNRDNGDPLCIQIAMTALLCVQYVWIFILGFLKSGNSPLLNMDVKAKDDADAEKRADNAPGAEERTSAPSGSSSELAAVTVTPPQDSA

[Multiple Choices]
A. 65..85; 137..157; 187..207; 216..236; 250..270; 334..354; 367..387; 392..412; 423..443; 455..475; 489..509
B. 65..85; 137..157; 158..178; 187..207; 216..236; 250..270; 334..354; 367..387; 392..412; 423..443; 455..475; 489..509
C. 179..199; 357..377
D. 65..85; 137..157; 158..178; 185..206; 216..236; 250..270; 334..354; 367..387; 392..412; 423..443; 455..475; 489..509
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

> The sequence-matched historical UniProt entry annotates the listed transmembrane intervals, including 158..178 and 187..207, so it supports choice B. These annotations use ECO:0000255, indicating computational evidence rather than direct experimental confirmation.

Citations as saved: [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11), [H12](#evidence-h12), [H13](#evidence-h13), [H14](#evidence-h14), [H15](#evidence-h15).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has multiple hydrophobic stretches consistent with membrane-spanning helices, including a likely segment around 158..178, which helps distinguish choices that omit it. But sequence hydrophobicity alone does not reliably resolve the exact endpoints of closely overlapping candidate intervals.


**Missing item-specific fact**

> A protein-specific transmembrane annotation or other evidence establishing the precise helix boundaries, especially whether the interval is 187..207 or 185..206.


**Reason**

> Broad sequence features support a multi-pass membrane protein, but the choice between B and D depends on precise, item-specific boundaries that are not established by general biological reasoning from the supplied sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> Choices B and D include nearly the same candidate helix, with boundaries shifted by only a few residues. Both intervals could plausibly represent the same membrane-spanning region based on sequence-level evidence, even though the cited annotation matches B.


### Important caveats

- Reviewer-only database evidence supports the expected answer but was not supplied to the evaluated model.
- The cited transmembrane annotations are computational, not direct experimental measurements.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has multiple hydrophobic stretches consistent with membrane-spanning helices, including a likely segment around 158..178, which helps distinguish choices that omit it. But sequence hydrophobicity alone does not reliably resolve the exact endpoints of closely overlapping candidate intervals.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "A protein-specific transmembrane annotation or other evidence establishing the precise helix boundaries, especially whether the interval is 187..207 or 185..206.",
    "reason": "Broad sequence features support a multi-pass membrane protein, but the choice between B and D depends on precise, item-specific boundaries that are not established by general biological reasoning from the supplied sequence."
  },
  "case_id": "transmembrane_0007",
  "expected_answer_check": {
    "evidence_ids": [
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9",
      "H10",
      "H11",
      "H12",
      "H13",
      "H14",
      "H15"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt entry annotates the listed transmembrane intervals, including 158..178 and 187..207, so it supports choice B. These annotations use ECO:0000255, indicating computational evidence rather than direct experimental confirmation."
  },
  "important_caveats": [
    "Reviewer-only database evidence supports the expected answer but was not supplied to the evaluated model.",
    "The cited transmembrane annotations are computational, not direct experimental measurements."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "Choices B and D include nearly the same candidate helix, with boundaries shifted by only a few residues. Both intervals could plausibly represent the same membrane-spanning region based on sequence-level evidence, even though the cited annotation matches B."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0007",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt entry annotates the listed transmembrane intervals, including 158..178 and 187..207, so it supports choice B. These annotations use ECO:0000255, indicating computational evidence rather than direct experimental confirmation.",
    "evidence_ids": ["H4", "H5", "H6", "H7", "H8", "H9", "H10", "H11", "H12", "H13", "H14", "H15"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has multiple hydrophobic stretches consistent with membrane-spanning helices, including a likely segment around 158..178, which helps distinguish choices that omit it. But sequence hydrophobicity alone does not reliably resolve the exact endpoints of closely overlapping candidate intervals.",
    "missing_item_specific_fact": "A protein-specific transmembrane annotation or other evidence establishing the precise helix boundaries, especially whether the interval is 187..207 or 185..206.",
    "reason": "Broad sequence features support a multi-pass membrane protein, but the choice between B and D depends on precise, item-specific boundaries that are not established by general biological reasoning from the supplied sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "Choices B and D include nearly the same candidate helix, with boundaries shifted by only a few residues. Both intervals could plausibly represent the same membrane-spanning region based on sequence-level evidence, even though the cited annotation matches B."
  },
  "important_caveats": [
    "Reviewer-only database evidence supports the expected answer but was not supplied to the evaluated model.",
    "The cited transmembrane annotations are computational, not direct experimental measurements."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProtKB/Swiss-Prot entry A0A125YQS6 (TgApiAT6-1, amino acid transporter 6-1 from Toxoplasma gondii) annotates exactly 12 transmembrane helical regions at 65..85, 137..157, 158..178, 187..207, 216..236, 250..270, 334..354, 367..387, 392..412, 423..443, 455..475, and 489..509, matching option B exactly. The sequence SHA256 matches the benchmark input. However, all TM annotations carry evidence code ECO:0000255 (inferred by similarity), indicating computational annotation rather than experimental determination.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [C13](#evidence-c13), [C14](#evidence-c14), [C15](#evidence-c15), [C16](#evidence-c16), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11), [H12](#evidence-h12), [H13](#evidence-h13), [H14](#evidence-h14), [H15](#evidence-h15).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Option C (only 2 TM regions) can be eliminated by reasoning: a 566-residue amino acid transporter of the ApiAT family is expected to have approximately 12 TM helices, not 2. Option A (missing 158..178) might be partially addressable by noting a hydrophobic stretch in that region, but distinguishing it as a separate helix from the adjacent 137..157 helix is ambiguous. The critical distinction between B (187..207) and D (185..206) involves a 2-residue boundary shift that cannot be resolved by general hydrophobicity reasoning—it depends on the specific computational annotation boundary.


**Missing item-specific fact**

> The exact 1-2 residue boundary precision of the TM helix at positions 185-207 vs 187-209, and the definitive assignment of 158..178 as a separate helix from 137..157, are determined by the UniProt computational annotation (ECO:0000255) rather than by a general biological principle. Distinguishing B from D requires knowing the precise annotation boundary.


**Reason**

> While general biological knowledge (transporter topology, hydrophobic helix length ~20 residues, ApiAT family ~12 TM) can eliminate C and provide approximate regions, the precise boundaries distinguishing B from D (2-residue shift at one helix) and B from A (inclusion/exclusion of one helix) are annotation-specific facts. The ECO:0000255 evidence code confirms these are computational predictions, not experimentally determined boundaries, making the exact values database-specific.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> The distinction between B (187..207) and D (185..206) involves a 2-residue boundary shift. Without the specific annotation, both boundaries could be argued as reasonable hydrophobic helix termini by sequence inspection. Similarly, A vs B hinges on whether 158..178 constitutes a separate helix or is contiguous with 137..157, which is not unambiguously resolvable by general reasoning.


### Important caveats

- All TM annotations carry ECO:0000255 (inferred by similarity), meaning they are computational predictions, not experimental measurements. The 'correct' boundaries reflect a specific prediction algorithm's output.
- The sequence match is confirmed (SHA256 identical), and the entry is reviewed Swiss-Prot, but the TM boundaries themselves are not experimentally validated.
- Option C is an obvious distractor (2 TM regions for a 12-TM transporter) and does not meaningfully test knowledge.
- The reviewer-only evidence confirms the key but was not available to the evaluated model; the model must rely on sequence analysis or memorization of this specific annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Option C (only 2 TM regions) can be eliminated by reasoning: a 566-residue amino acid transporter of the ApiAT family is expected to have approximately 12 TM helices, not 2. Option A (missing 158..178) might be partially addressable by noting a hydrophobic stretch in that region, but distinguishing it as a separate helix from the adjacent 137..157 helix is ambiguous. The critical distinction between B (187..207) and D (185..206) involves a 2-residue boundary shift that cannot be resolved by general hydrophobicity reasoning—it depends on the specific computational annotation boundary.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact 1-2 residue boundary precision of the TM helix at positions 185-207 vs 187-209, and the definitive assignment of 158..178 as a separate helix from 137..157, are determined by the UniProt computational annotation (ECO:0000255) rather than by a general biological principle. Distinguishing B from D requires knowing the precise annotation boundary.",
    "reason": "While general biological knowledge (transporter topology, hydrophobic helix length ~20 residues, ApiAT family ~12 TM) can eliminate C and provide approximate regions, the precise boundaries distinguishing B from D (2-residue shift at one helix) and B from A (inclusion/exclusion of one helix) are annotation-specific facts. The ECO:0000255 evidence code confirms these are computational predictions, not experimentally determined boundaries, making the exact values database-specific."
  },
  "case_id": "transmembrane_0007",
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
      "C13",
      "C14",
      "C15",
      "C16",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9",
      "H10",
      "H11",
      "H12",
      "H13",
      "H14",
      "H15"
    ],
    "judgment": "supported",
    "reason": "The UniProtKB/Swiss-Prot entry A0A125YQS6 (TgApiAT6-1, amino acid transporter 6-1 from Toxoplasma gondii) annotates exactly 12 transmembrane helical regions at 65..85, 137..157, 158..178, 187..207, 216..236, 250..270, 334..354, 367..387, 392..412, 423..443, 455..475, and 489..509, matching option B exactly. The sequence SHA256 matches the benchmark input. However, all TM annotations carry evidence code ECO:0000255 (inferred by similarity), indicating computational annotation rather than experimental determination."
  },
  "important_caveats": [
    "All TM annotations carry ECO:0000255 (inferred by similarity), meaning they are computational predictions, not experimental measurements. The 'correct' boundaries reflect a specific prediction algorithm's output.",
    "The sequence match is confirmed (SHA256 identical), and the entry is reviewed Swiss-Prot, but the TM boundaries themselves are not experimentally validated.",
    "Option C is an obvious distractor (2 TM regions for a 12-TM transporter) and does not meaningfully test knowledge.",
    "The reviewer-only evidence confirms the key but was not available to the evaluated model; the model must rely on sequence analysis or memorization of this specific annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "The distinction between B (187..207) and D (185..206) involves a 2-residue boundary shift. Without the specific annotation, both boundaries could be argued as reasonable hydrophobic helix termini by sequence inspection. Similarly, A vs B hinges on whether 158..178 constitutes a separate helix or is contiguous with 137..157, which is not unambiguously resolvable by general reasoning."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0007",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProtKB/Swiss-Prot entry A0A125YQS6 (TgApiAT6-1, amino acid transporter 6-1 from Toxoplasma gondii) annotates exactly 12 transmembrane helical regions at 65..85, 137..157, 158..178, 187..207, 216..236, 250..270, 334..354, 367..387, 392..412, 423..443, 455..475, and 489..509, matching option B exactly. The sequence SHA256 matches the benchmark input. However, all TM annotations carry evidence code ECO:0000255 (inferred by similarity), indicating computational annotation rather than experimental determination.",
    "evidence_ids": ["C5","C6","C7","C8","C9","C10","C11","C12","C13","C14","C15","C16","H4","H5","H6","H7","H8","H9","H10","H11","H12","H13","H14","H15"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Option C (only 2 TM regions) can be eliminated by reasoning: a 566-residue amino acid transporter of the ApiAT family is expected to have approximately 12 TM helices, not 2. Option A (missing 158..178) might be partially addressable by noting a hydrophobic stretch in that region, but distinguishing it as a separate helix from the adjacent 137..157 helix is ambiguous. The critical distinction between B (187..207) and D (185..206) involves a 2-residue boundary shift that cannot be resolved by general hydrophobicity reasoning—it depends on the specific computational annotation boundary.",
    "missing_item_specific_fact": "The exact 1-2 residue boundary precision of the TM helix at positions 185-207 vs 187-209, and the definitive assignment of 158..178 as a separate helix from 137..157, are determined by the UniProt computational annotation (ECO:0000255) rather than by a general biological principle. Distinguishing B from D requires knowing the precise annotation boundary.",
    "reason": "While general biological knowledge (transporter topology, hydrophobic helix length ~20 residues, ApiAT family ~12 TM) can eliminate C and provide approximate regions, the precise boundaries distinguishing B from D (2-residue shift at one helix) and B from A (inclusion/exclusion of one helix) are annotation-specific facts. The ECO:0000255 evidence code confirms these are computational predictions, not experimentally determined boundaries, making the exact values database-specific."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "The distinction between B (187..207) and D (185..206) involves a 2-residue boundary shift. Without the specific annotation, both boundaries could be argued as reasonable hydrophobic helix termini by sequence inspection. Similarly, A vs B hinges on whether 158..178 constitutes a separate helix or is contiguous with 137..157, which is not unambiguously resolvable by general reasoning."
  },
  "important_caveats": [
    "All TM annotations carry ECO:0000255 (inferred by similarity), meaning they are computational predictions, not experimental measurements. The 'correct' boundaries reflect a specific prediction algorithm's output.",
    "The sequence match is confirmed (SHA256 identical), and the entry is reviewed Swiss-Prot, but the TM boundaries themselves are not experimentally validated.",
    "Option C is an obvious distractor (2 TM regions for a 12-TM transporter) and does not meaningfully test knowledge.",
    "The reviewer-only evidence confirms the key but was not available to the evaluated model; the model must rely on sequence analysis or memorization of this specific annotation."
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

**Accession:** `A0A125YQS6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 32. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YQS6.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:25.310365+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":85},"start":{"modifier":"EXACT","value":65}},"type":"Transmembrane"}
```

Source SHA-256: `fe45df740c1133045fa704bf8db7ed1e22b8af4077b4407e44e9e271dc51f39f`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YQS6.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:25.310365+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":157},"start":{"modifier":"EXACT","value":137}},"type":"Transmembrane"}
```

Source SHA-256: `fe45df740c1133045fa704bf8db7ed1e22b8af4077b4407e44e9e271dc51f39f`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YQS6.json)  
**Locator:** `/features/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:25.310365+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":178},"start":{"modifier":"EXACT","value":158}},"type":"Transmembrane"}
```

Source SHA-256: `fe45df740c1133045fa704bf8db7ed1e22b8af4077b4407e44e9e271dc51f39f`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YQS6.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:25.310365+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":207},"start":{"modifier":"EXACT","value":187}},"type":"Transmembrane"}
```

Source SHA-256: `fe45df740c1133045fa704bf8db7ed1e22b8af4077b4407e44e9e271dc51f39f`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YQS6.json)  
**Locator:** `/features/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:25.310365+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":236},"start":{"modifier":"EXACT","value":216}},"type":"Transmembrane"}
```

Source SHA-256: `fe45df740c1133045fa704bf8db7ed1e22b8af4077b4407e44e9e271dc51f39f`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YQS6.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:25.310365+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":270},"start":{"modifier":"EXACT","value":250}},"type":"Transmembrane"}
```

Source SHA-256: `fe45df740c1133045fa704bf8db7ed1e22b8af4077b4407e44e9e271dc51f39f`.

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YQS6.json)  
**Locator:** `/features/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:25.310365+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":354},"start":{"modifier":"EXACT","value":334}},"type":"Transmembrane"}
```

Source SHA-256: `fe45df740c1133045fa704bf8db7ed1e22b8af4077b4407e44e9e271dc51f39f`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YQS6.json)  
**Locator:** `/features/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:25.310365+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":387},"start":{"modifier":"EXACT","value":367}},"type":"Transmembrane"}
```

Source SHA-256: `fe45df740c1133045fa704bf8db7ed1e22b8af4077b4407e44e9e271dc51f39f`.

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YQS6.json)  
**Locator:** `/features/9`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:25.310365+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":412},"start":{"modifier":"EXACT","value":392}},"type":"Transmembrane"}
```

Source SHA-256: `fe45df740c1133045fa704bf8db7ed1e22b8af4077b4407e44e9e271dc51f39f`.

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YQS6.json)  
**Locator:** `/features/10`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:25.310365+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":443},"start":{"modifier":"EXACT","value":423}},"type":"Transmembrane"}
```

Source SHA-256: `fe45df740c1133045fa704bf8db7ed1e22b8af4077b4407e44e9e271dc51f39f`.

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YQS6.json)  
**Locator:** `/features/11`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:25.310365+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":475},"start":{"modifier":"EXACT","value":455}},"type":"Transmembrane"}
```

Source SHA-256: `fe45df740c1133045fa704bf8db7ed1e22b8af4077b4407e44e9e271dc51f39f`.

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A125YQS6.json)  
**Locator:** `/features/12`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:25.310365+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":509},"start":{"modifier":"EXACT","value":489}},"type":"Transmembrane"}
```

Source SHA-256: `fe45df740c1133045fa704bf8db7ed1e22b8af4077b4407e44e9e271dc51f39f`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A125YQS6?format=txt&versions=32)  
**Locator:** `lines 114-116`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-02T04:24:28.654244+00:00.  

```text
FT   TRANSMEM        65..85
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `d1f59d0960a176349ecfb71f807306e5811e320840d2d34cbe7fbcebeb965659`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A125YQS6?format=txt&versions=32)  
**Locator:** `lines 117-119`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-02T04:24:28.654244+00:00.  

```text
FT   TRANSMEM        137..157
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `d1f59d0960a176349ecfb71f807306e5811e320840d2d34cbe7fbcebeb965659`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A125YQS6?format=txt&versions=32)  
**Locator:** `lines 120-122`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-02T04:24:28.654244+00:00.  

```text
FT   TRANSMEM        158..178
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `d1f59d0960a176349ecfb71f807306e5811e320840d2d34cbe7fbcebeb965659`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A125YQS6?format=txt&versions=32)  
**Locator:** `lines 123-125`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-02T04:24:28.654244+00:00.  

```text
FT   TRANSMEM        187..207
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `d1f59d0960a176349ecfb71f807306e5811e320840d2d34cbe7fbcebeb965659`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A125YQS6?format=txt&versions=32)  
**Locator:** `lines 126-128`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-02T04:24:28.654244+00:00.  

```text
FT   TRANSMEM        216..236
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `d1f59d0960a176349ecfb71f807306e5811e320840d2d34cbe7fbcebeb965659`.

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A125YQS6?format=txt&versions=32)  
**Locator:** `lines 129-131`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-02T04:24:28.654244+00:00.  

```text
FT   TRANSMEM        250..270
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `d1f59d0960a176349ecfb71f807306e5811e320840d2d34cbe7fbcebeb965659`.

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A125YQS6?format=txt&versions=32)  
**Locator:** `lines 132-134`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-02T04:24:28.654244+00:00.  

```text
FT   TRANSMEM        334..354
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `d1f59d0960a176349ecfb71f807306e5811e320840d2d34cbe7fbcebeb965659`.

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A125YQS6?format=txt&versions=32)  
**Locator:** `lines 135-137`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-02T04:24:28.654244+00:00.  

```text
FT   TRANSMEM        367..387
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `d1f59d0960a176349ecfb71f807306e5811e320840d2d34cbe7fbcebeb965659`.

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A125YQS6?format=txt&versions=32)  
**Locator:** `lines 138-140`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-02T04:24:28.654244+00:00.  

```text
FT   TRANSMEM        392..412
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `d1f59d0960a176349ecfb71f807306e5811e320840d2d34cbe7fbcebeb965659`.

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A125YQS6?format=txt&versions=32)  
**Locator:** `lines 141-143`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-02T04:24:28.654244+00:00.  

```text
FT   TRANSMEM        423..443
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `d1f59d0960a176349ecfb71f807306e5811e320840d2d34cbe7fbcebeb965659`.

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A125YQS6?format=txt&versions=32)  
**Locator:** `lines 144-146`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-02T04:24:28.654244+00:00.  

```text
FT   TRANSMEM        455..475
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `d1f59d0960a176349ecfb71f807306e5811e320840d2d34cbe7fbcebeb965659`.

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A125YQS6?format=txt&versions=32)  
**Locator:** `lines 147-149`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-02T04:24:28.654244+00:00.  

```text
FT   TRANSMEM        489..509
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `d1f59d0960a176349ecfb71f807306e5811e320840d2d34cbe7fbcebeb965659`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 7. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
