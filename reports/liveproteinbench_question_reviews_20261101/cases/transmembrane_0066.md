# transmembrane_0066

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **B** — 27..47; 82..102; 109..129; 136..156; 173..193; 209..229; 333..353; 361..381; 395..415; 427..447; 460..480

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MDTAPDHREPQEQGESRKWYEMTASEFYVYVVAFMCGVSMMMSVNAVFSAPAYIMTYYRYAMQDPEAVPLYTNFWNNVMTYYNLIGIVTSLIMEPLTLLSWFRRIPIKVRLLGGLVILIVEIIVLMVVPARGTSEAGAVATICCTGFIGGFGKSIFESTAYGMFGAFPSSFTSTMMGGVGMSGVLTSLLQIIVKAALPDSYEGVKKQSKIYYGLDVGIQGMTFVALILLRFNSFAQNYFGDLGAVKSKVDAGKLSAEALCHTDEHPTHDKEGRNSSSGKEVPALGEVQTAAAKSEGPDAVEESSWPHEVEGPTSNEILVATAIFSTLRRVKWMFVACAFNFLITLFLFPGIAVGMFPDSKWFSTIAVFIFNVFDVLGRFSPSLKLMWPRSYKQRWIIVAASFARVIFVPLLLLHSYHYIPGEAYGYVMEVIFGFSNGYVGSMALVLGPQSKGIDNDGKRFVAGTLMGISILVGGTIGTVLSIMTQTIRERH

[Multiple Choices]
A. 27..47; 82..102; 109..129; 136..156; 173..193; 209..229; 333..353; 361..381; 395..415; 460..480
B. 27..47; 82..102; 109..129; 136..156; 173..193; 209..229; 333..353; 361..381; 395..415; 427..447; 460..480
C. 27..47; 80..106; 109..129; 136..156; 173..193; 209..229; 333..353; 361..381; 395..415; 427..447; 460..480
D. 157..177; 412..432; 448..468; 478..498; 516..536; 545..565; 789..809; 986..1006; 1013..1033; 1037..1057; 1080..1100; 1114..1134
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

> The supplied sequence exactly matches the UniProt entry for this protein, whose historical and current records annotate the eleven intervals listed in B as transmembrane helices. The annotations cite ECO:0000255, indicating computational evidence rather than direct experimental confirmation of these boundaries.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11), [H12](#evidence-h12), [H13](#evidence-h13).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has multiple hydrophobic stretches consistent with a multipass membrane protein, and hydropathy can support broad transmembrane-region predictions. It does not reliably establish the precise boundaries needed to choose B over the near-identical, boundary-shifted C.


**Missing item-specific fact**

> The protein-specific predicted or annotated transmembrane intervals, including the exact boundary convention for the 82..102 versus 80..106 region.


**Reason**

> The sequence provides biological grounds for predicting membrane-spanning helices, but selecting the listed exact intervals—especially between B and C—depends on protein-specific boundary assignments not supplied in the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> Both choices include the same predicted helices except that C gives a longer, shifted interval at 80..106 instead of 82..102. Transmembrane boundaries can be uncertain, and the sequence alone does not unambiguously resolve that difference.


### Important caveats

- The evidence supports B as the annotated answer, but the cited UniProt transmembrane features are computationally supported, not established here as experimentally measured boundaries.
- The reviewer-only accession and annotations were not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has multiple hydrophobic stretches consistent with a multipass membrane protein, and hydropathy can support broad transmembrane-region predictions. It does not reliably establish the precise boundaries needed to choose B over the near-identical, boundary-shifted C.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific predicted or annotated transmembrane intervals, including the exact boundary convention for the 82..102 versus 80..106 region.",
    "reason": "The sequence provides biological grounds for predicting membrane-spanning helices, but selecting the listed exact intervals—especially between B and C—depends on protein-specific boundary assignments not supplied in the question."
  },
  "case_id": "transmembrane_0066",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9",
      "H10",
      "H11",
      "H12",
      "H13"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry for this protein, whose historical and current records annotate the eleven intervals listed in B as transmembrane helices. The annotations cite ECO:0000255, indicating computational evidence rather than direct experimental confirmation of these boundaries."
  },
  "important_caveats": [
    "The evidence supports B as the annotated answer, but the cited UniProt transmembrane features are computationally supported, not established here as experimentally measured boundaries.",
    "The reviewer-only accession and annotations were not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "Both choices include the same predicted helices except that C gives a longer, shifted interval at 80..106 instead of 82..102. Transmembrane boundaries can be uncertain, and the sequence alone does not unambiguously resolve that difference."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0066",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry for this protein, whose historical and current records annotate the eleven intervals listed in B as transmembrane helices. The annotations cite ECO:0000255, indicating computational evidence rather than direct experimental confirmation of these boundaries.",
    "evidence_ids": ["H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "H11", "H12", "H13"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has multiple hydrophobic stretches consistent with a multipass membrane protein, and hydropathy can support broad transmembrane-region predictions. It does not reliably establish the precise boundaries needed to choose B over the near-identical, boundary-shifted C.",
    "missing_item_specific_fact": "The protein-specific predicted or annotated transmembrane intervals, including the exact boundary convention for the 82..102 versus 80..106 region.",
    "reason": "The sequence provides biological grounds for predicting membrane-spanning helices, but selecting the listed exact intervals—especially between B and C—depends on protein-specific boundary assignments not supplied in the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "Both choices include the same predicted helices except that C gives a longer, shifted interval at 80..106 instead of 82..102. Transmembrane boundaries can be uncertain, and the sequence alone does not unambiguously resolve that difference."
  },
  "important_caveats": [
    "The evidence supports B as the annotated answer, but the cited UniProt transmembrane features are computationally supported, not established here as experimentally measured boundaries.",
    "The reviewer-only accession and annotations were not provided to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry O76269 (Nucleoside transporter 1.2, Leishmania donovani, 491 AA, sequence matched) annotates exactly 11 transmembrane helices at 27-47, 82-102, 109-129, 136-156, 173-193, 209-229, 333-353, 361-381, 395-415, 427-447, and 460-480, which matches Choice B precisely. All annotations carry evidence code ECO:0000255 (inferred by similarity), so these are computational predictions rather than experimental measurements, but they are the authoritative database annotation for this sequence.

Citations as saved: [C1](#evidence-c1), [C2](#evidence-c2), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [C13](#evidence-c13), [C14](#evidence-c14), [C15](#evidence-c15), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11), [H12](#evidence-h12), [H13](#evidence-h13).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Choice D is eliminated immediately because its positions (up to 1134) exceed the 491-residue sequence length. Choice C's second TM (80-106) includes residues R103 and R104 (charged arginines) and P106 (a helix-breaking proline) within the proposed membrane-spanning segment, which is energetically highly unfavorable for an alpha-helix embedded in a lipid bilayer; the 82-102 boundaries in B avoid these. Choice A omits the 427-447 segment, which contains a moderately hydrophobic stretch (VMEVIFGFSNGYVGSMALVLG) consistent with a TM helix; additionally, equilibrative nucleoside transporters (ENT family) are generally characterized as 11-TM proteins, providing family-level context for including this region. These are general biological arguments (charged-residue exclusion from TM helices, helix-breaking prolines, hydrophobicity windows, family topology) that meaningfully distinguish B from A, C, and D.


**Missing item-specific fact**

> The exact boundary residues (82 vs 80, 102 vs 106) depend on the specific prediction algorithm used by the annotator (ECO:0000255, similarity-based). A model without access to the particular tool's output might produce slightly shifted boundaries, though the R/R/P argument strongly disfavors the 80-106 range.


**Reason**

> Multiple concrete biological arguments from the sequence itself distinguish the options: D is eliminated by sequence length; C's TM2 boundary incorporates two arginines and a proline inside the helix, violating TM-helix energetics; A omits a hydrophobic segment that the ENT family topology predicts. These are general-knowledge arguments, not reliance on a single item-specific annotation lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While the exact TM boundaries are prediction-dependent (ECO:0000255), the four choices are sufficiently different that general biological reasoning (sequence length, charged-residue exclusion, helix-breaking residues, hydrophobicity, family topology) cleanly selects B. No other option survives scrutiny on multiple independent grounds.


### Important caveats

- All 11 TM annotations carry ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred from homologs, not experimentally determined boundaries. The exact start/end residues could differ under alternative prediction methods.
- The 427-447 region is only moderately hydrophobic (contains E, S, N, G, S, G); identifying it as a TM helix requires either family-level topology knowledge (ENT = 11 TM) or a permissive hydrophobicity threshold.
- The UniProt entry is flagged as a Fragment (491 AA), so the true full-length protein may have additional TM regions not represented here.
- Sequence-match confirmed: benchmark sequence SHA-256 matches both current (v69) and historical (v67) UniProt records for O76269.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Choice D is eliminated immediately because its positions (up to 1134) exceed the 491-residue sequence length. Choice C's second TM (80-106) includes residues R103 and R104 (charged arginines) and P106 (a helix-breaking proline) within the proposed membrane-spanning segment, which is energetically highly unfavorable for an alpha-helix embedded in a lipid bilayer; the 82-102 boundaries in B avoid these. Choice A omits the 427-447 segment, which contains a moderately hydrophobic stretch (VMEVIFGFSNGYVGSMALVLG) consistent with a TM helix; additionally, equilibrative nucleoside transporters (ENT family) are generally characterized as 11-TM proteins, providing family-level context for including this region. These are general biological arguments (charged-residue exclusion from TM helices, helix-breaking prolines, hydrophobicity windows, family topology) that meaningfully distinguish B from A, C, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact boundary residues (82 vs 80, 102 vs 106) depend on the specific prediction algorithm used by the annotator (ECO:0000255, similarity-based). A model without access to the particular tool's output might produce slightly shifted boundaries, though the R/R/P argument strongly disfavors the 80-106 range.",
    "reason": "Multiple concrete biological arguments from the sequence itself distinguish the options: D is eliminated by sequence length; C's TM2 boundary incorporates two arginines and a proline inside the helix, violating TM-helix energetics; A omits a hydrophobic segment that the ENT family topology predicts. These are general-knowledge arguments, not reliance on a single item-specific annotation lookup."
  },
  "case_id": "transmembrane_0066",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C2",
      "C3",
      "C4",
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
      "H3",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9",
      "H10",
      "H11",
      "H12",
      "H13"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry O76269 (Nucleoside transporter 1.2, Leishmania donovani, 491 AA, sequence matched) annotates exactly 11 transmembrane helices at 27-47, 82-102, 109-129, 136-156, 173-193, 209-229, 333-353, 361-381, 395-415, 427-447, and 460-480, which matches Choice B precisely. All annotations carry evidence code ECO:0000255 (inferred by similarity), so these are computational predictions rather than experimental measurements, but they are the authoritative database annotation for this sequence."
  },
  "important_caveats": [
    "All 11 TM annotations carry ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred from homologs, not experimentally determined boundaries. The exact start/end residues could differ under alternative prediction methods.",
    "The 427-447 region is only moderately hydrophobic (contains E, S, N, G, S, G); identifying it as a TM helix requires either family-level topology knowledge (ENT = 11 TM) or a permissive hydrophobicity threshold.",
    "The UniProt entry is flagged as a Fragment (491 AA), so the true full-length protein may have additional TM regions not represented here.",
    "Sequence-match confirmed: benchmark sequence SHA-256 matches both current (v69) and historical (v67) UniProt records for O76269."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the exact TM boundaries are prediction-dependent (ECO:0000255), the four choices are sufficiently different that general biological reasoning (sequence length, charged-residue exclusion, helix-breaking residues, hydrophobicity, family topology) cleanly selects B. No other option survives scrutiny on multiple independent grounds."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0066",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry O76269 (Nucleoside transporter 1.2, Leishmania donovani, 491 AA, sequence matched) annotates exactly 11 transmembrane helices at 27-47, 82-102, 109-129, 136-156, 173-193, 209-229, 333-353, 361-381, 395-415, 427-447, and 460-480, which matches Choice B precisely. All annotations carry evidence code ECO:0000255 (inferred by similarity), so these are computational predictions rather than experimental measurements, but they are the authoritative database annotation for this sequence.",
    "evidence_ids": ["C1","C2","C3","C4","C5","C6","C7","C8","C9","C10","C11","C12","C13","C14","C15","H3","H4","H5","H6","H7","H8","H9","H10","H11","H12","H13"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Choice D is eliminated immediately because its positions (up to 1134) exceed the 491-residue sequence length. Choice C's second TM (80-106) includes residues R103 and R104 (charged arginines) and P106 (a helix-breaking proline) within the proposed membrane-spanning segment, which is energetically highly unfavorable for an alpha-helix embedded in a lipid bilayer; the 82-102 boundaries in B avoid these. Choice A omits the 427-447 segment, which contains a moderately hydrophobic stretch (VMEVIFGFSNGYVGSMALVLG) consistent with a TM helix; additionally, equilibrative nucleoside transporters (ENT family) are generally characterized as 11-TM proteins, providing family-level context for including this region. These are general biological arguments (charged-residue exclusion from TM helices, helix-breaking prolines, hydrophobicity windows, family topology) that meaningfully distinguish B from A, C, and D.",
    "missing_item_specific_fact": "The exact boundary residues (82 vs 80, 102 vs 106) depend on the specific prediction algorithm used by the annotator (ECO:0000255, similarity-based). A model without access to the particular tool's output might produce slightly shifted boundaries, though the R/R/P argument strongly disfavors the 80-106 range.",
    "reason": "Multiple concrete biological arguments from the sequence itself distinguish the options: D is eliminated by sequence length; C's TM2 boundary incorporates two arginines and a proline inside the helix, violating TM-helix energetics; A omits a hydrophobic segment that the ENT family topology predicts. These are general-knowledge arguments, not reliance on a single item-specific annotation lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the exact TM boundaries are prediction-dependent (ECO:0000255), the four choices are sufficiently different that general biological reasoning (sequence length, charged-residue exclusion, helix-breaking residues, hydrophobicity, family topology) cleanly selects B. No other option survives scrutiny on multiple independent grounds."
  },
  "important_caveats": [
    "All 11 TM annotations carry ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred from homologs, not experimentally determined boundaries. The exact start/end residues could differ under alternative prediction methods.",
    "The 427-447 region is only moderately hydrophobic (contains E, S, N, G, S, G); identifying it as a TM helix requires either family-level topology knowledge (ENT = 11 TM) or a permissive hydrophobicity threshold.",
    "The UniProt entry is flagged as a Fragment (491 AA), so the true full-length protein may have additional TM regions not represented here.",
    "Sequence-match confirmed: benchmark sequence SHA-256 matches both current (v69) and historical (v67) UniProt records for O76269."
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

**Accession:** `O76269` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 67. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76269.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:16.869968+00:00.  

```json
"O76269"
```

Source SHA-256: `8f29244e052da5b7868c269faca3985b3271e53c25e144a81c4a059a7c67513f`.

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76269.json)  
**Locator:** `/entryAudit`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:16.869968+00:00.  

```json
{"entryVersion":69,"firstPublicDate":"2025-04-09","lastAnnotationUpdateDate":"2026-09-02","lastSequenceUpdateDate":"1998-11-01","sequenceVersion":1}
```

Source SHA-256: `8f29244e052da5b7868c269faca3985b3271e53c25e144a81c4a059a7c67513f`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76269.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:16.869968+00:00.  

```json
{"evidences":[{"evidenceCode":"ECO:0000312","id":"AAC32315.1","source":"EMBL"}],"lineage":["Eukaryota","Discoba","Euglenozoa","Kinetoplastea","Metakinetoplastina","Trypanosomatida","Trypanosomatidae","Leishmaniinae","Leishmania"],"scientificName":"Leishmania donovani","taxonId":5661}
```

Source SHA-256: `8f29244e052da5b7868c269faca3985b3271e53c25e144a81c4a059a7c67513f`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76269.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:16.869968+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"Ref.2","source":"Reference"}],"value":"Equilibrative nucleoside transporter 1.2"}}],"flag":"Fragment","recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"9707568","source":"PubMed"}],"value":"Nucleoside transporter 1.2"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"9707568","source":"PubMed"}],"value":"LdNT1.2"}]}}
```

Source SHA-256: `8f29244e052da5b7868c269faca3985b3271e53c25e144a81c4a059a7c67513f`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76269.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:16.869968+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":47},"start":{"modifier":"EXACT","value":27}},"type":"Transmembrane"}
```

Source SHA-256: `8f29244e052da5b7868c269faca3985b3271e53c25e144a81c4a059a7c67513f`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76269.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:16.869968+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":102},"start":{"modifier":"EXACT","value":82}},"type":"Transmembrane"}
```

Source SHA-256: `8f29244e052da5b7868c269faca3985b3271e53c25e144a81c4a059a7c67513f`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76269.json)  
**Locator:** `/features/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:16.869968+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":129},"start":{"modifier":"EXACT","value":109}},"type":"Transmembrane"}
```

Source SHA-256: `8f29244e052da5b7868c269faca3985b3271e53c25e144a81c4a059a7c67513f`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76269.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:16.869968+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":156},"start":{"modifier":"EXACT","value":136}},"type":"Transmembrane"}
```

Source SHA-256: `8f29244e052da5b7868c269faca3985b3271e53c25e144a81c4a059a7c67513f`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76269.json)  
**Locator:** `/features/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:16.869968+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":193},"start":{"modifier":"EXACT","value":173}},"type":"Transmembrane"}
```

Source SHA-256: `8f29244e052da5b7868c269faca3985b3271e53c25e144a81c4a059a7c67513f`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76269.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:16.869968+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":229},"start":{"modifier":"EXACT","value":209}},"type":"Transmembrane"}
```

Source SHA-256: `8f29244e052da5b7868c269faca3985b3271e53c25e144a81c4a059a7c67513f`.

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76269.json)  
**Locator:** `/features/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:16.869968+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":353},"start":{"modifier":"EXACT","value":333}},"type":"Transmembrane"}
```

Source SHA-256: `8f29244e052da5b7868c269faca3985b3271e53c25e144a81c4a059a7c67513f`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76269.json)  
**Locator:** `/features/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:16.869968+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":381},"start":{"modifier":"EXACT","value":361}},"type":"Transmembrane"}
```

Source SHA-256: `8f29244e052da5b7868c269faca3985b3271e53c25e144a81c4a059a7c67513f`.

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76269.json)  
**Locator:** `/features/9`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:16.869968+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":415},"start":{"modifier":"EXACT","value":395}},"type":"Transmembrane"}
```

Source SHA-256: `8f29244e052da5b7868c269faca3985b3271e53c25e144a81c4a059a7c67513f`.

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76269.json)  
**Locator:** `/features/10`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:16.869968+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":447},"start":{"modifier":"EXACT","value":427}},"type":"Transmembrane"}
```

Source SHA-256: `8f29244e052da5b7868c269faca3985b3271e53c25e144a81c4a059a7c67513f`.

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O76269.json)  
**Locator:** `/features/11`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:16.869968+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":480},"start":{"modifier":"EXACT","value":460}},"type":"Transmembrane"}
```

Source SHA-256: `8f29244e052da5b7868c269faca3985b3271e53c25e144a81c4a059a7c67513f`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76269?format=txt&versions=67)  
**Locator:** `lines 101-103`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 67 / 1.  
**Retrieved:** 2026-11-02T04:29:18.847742+00:00.  

```text
FT   TRANSMEM        27..47
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `c46d1d02153bfb053b483070158a9f044f1d5ebc437f236b62fb741bcb5237e7`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76269?format=txt&versions=67)  
**Locator:** `lines 104-106`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 67 / 1.  
**Retrieved:** 2026-11-02T04:29:18.847742+00:00.  

```text
FT   TRANSMEM        82..102
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `c46d1d02153bfb053b483070158a9f044f1d5ebc437f236b62fb741bcb5237e7`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76269?format=txt&versions=67)  
**Locator:** `lines 107-109`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 67 / 1.  
**Retrieved:** 2026-11-02T04:29:18.847742+00:00.  

```text
FT   TRANSMEM        109..129
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `c46d1d02153bfb053b483070158a9f044f1d5ebc437f236b62fb741bcb5237e7`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76269?format=txt&versions=67)  
**Locator:** `lines 110-112`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 67 / 1.  
**Retrieved:** 2026-11-02T04:29:18.847742+00:00.  

```text
FT   TRANSMEM        136..156
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `c46d1d02153bfb053b483070158a9f044f1d5ebc437f236b62fb741bcb5237e7`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76269?format=txt&versions=67)  
**Locator:** `lines 113-115`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 67 / 1.  
**Retrieved:** 2026-11-02T04:29:18.847742+00:00.  

```text
FT   TRANSMEM        173..193
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `c46d1d02153bfb053b483070158a9f044f1d5ebc437f236b62fb741bcb5237e7`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76269?format=txt&versions=67)  
**Locator:** `lines 116-118`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 67 / 1.  
**Retrieved:** 2026-11-02T04:29:18.847742+00:00.  

```text
FT   TRANSMEM        209..229
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `c46d1d02153bfb053b483070158a9f044f1d5ebc437f236b62fb741bcb5237e7`.

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76269?format=txt&versions=67)  
**Locator:** `lines 119-121`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 67 / 1.  
**Retrieved:** 2026-11-02T04:29:18.847742+00:00.  

```text
FT   TRANSMEM        333..353
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `c46d1d02153bfb053b483070158a9f044f1d5ebc437f236b62fb741bcb5237e7`.

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76269?format=txt&versions=67)  
**Locator:** `lines 122-124`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 67 / 1.  
**Retrieved:** 2026-11-02T04:29:18.847742+00:00.  

```text
FT   TRANSMEM        361..381
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `c46d1d02153bfb053b483070158a9f044f1d5ebc437f236b62fb741bcb5237e7`.

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76269?format=txt&versions=67)  
**Locator:** `lines 125-127`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 67 / 1.  
**Retrieved:** 2026-11-02T04:29:18.847742+00:00.  

```text
FT   TRANSMEM        395..415
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `c46d1d02153bfb053b483070158a9f044f1d5ebc437f236b62fb741bcb5237e7`.

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76269?format=txt&versions=67)  
**Locator:** `lines 128-130`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 67 / 1.  
**Retrieved:** 2026-11-02T04:29:18.847742+00:00.  

```text
FT   TRANSMEM        427..447
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `c46d1d02153bfb053b483070158a9f044f1d5ebc437f236b62fb741bcb5237e7`.

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O76269?format=txt&versions=67)  
**Locator:** `lines 131-133`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 67 / 1.  
**Retrieved:** 2026-11-02T04:29:18.847742+00:00.  

```text
FT   TRANSMEM        460..480
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `c46d1d02153bfb053b483070158a9f044f1d5ebc437f236b62fb741bcb5237e7`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 66. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
