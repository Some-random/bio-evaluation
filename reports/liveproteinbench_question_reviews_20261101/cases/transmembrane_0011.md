# transmembrane_0011

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **B** — 139..159; 191..211; 251..271; 280..300; 321..341

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MASGQMAPSLLRRPITFVSSCPPALRSFGALCPPTGSTDLIGGTGRDILIAAAPARRAPLHATLPLLRSLHTSPAPQLSASHQHQAQQQQQQTKQPQQPYDPQQDQVPSTSTASSSKPAADPVYNLPNAVSVARLVSGPLIGYWLVQGHYEAATLALAVSGASDWLDGWLARRLGASSVFGSYLDPLADKVLIGCVAAALLMNGAMPGWVAGVVVGRDVLLVAGSFVFRLRGFGWRWPGAAAFFRTVDTSAAAAGAATGAANGVASGGGGGGEGVSFMRPLLISKANTVLQLLLLGGYLLRGMDGGAGLQLLLPGGGGEELIMGLELATAATTVASGLAYGTMAVQGKLFK

[Multiple Choices]
A. 139..159; 191..211; 251..271; 280..300; 322..338
B. 139..159; 191..211; 251..271; 280..300; 321..341
C. 6..29
D. 139..159; 191..211; 251..271; 280..300
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

> The exact sequence matches a UniProt entry whose archived and current annotations list all five transmembrane regions in choice B. These annotations have computational evidence code ECO:0000255, so they support the predicted regions but are not evidence of experimental validation.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains several hydrophobic stretches consistent with membrane-spanning helices, including a hydrophobic C-terminal segment. This supports predicting a final transmembrane region, but does not confidently determine its exact boundaries.


**Missing item-specific fact**

> The specific predicted endpoint annotation that places the final helix at 321..341 rather than 322..338.


**Reason**

> Distinguishing choices B and A requires exact boundary placement for a particular protein. The sequence supports a membrane-spanning helix in that region, but general hydrophobicity reasoning does not uniquely establish those precise coordinates.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Both choices identify the same four regions and a final hydrophobic segment; they differ only slightly in the final segment's boundaries. The supplied sequence alone does not clearly resolve that boundary difference.


### Important caveats

- The supporting database features are computational predictions, not independently verified experimental measurements.
- The reviewer-only accession and annotation were not supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains several hydrophobic stretches consistent with membrane-spanning helices, including a hydrophobic C-terminal segment. This supports predicting a final transmembrane region, but does not confidently determine its exact boundaries.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific predicted endpoint annotation that places the final helix at 321..341 rather than 322..338.",
    "reason": "Distinguishing choices B and A requires exact boundary placement for a particular protein. The sequence supports a membrane-spanning helix in that region, but general hydrophobicity reasoning does not uniquely establish those precise coordinates."
  },
  "case_id": "transmembrane_0011",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H4",
      "H5",
      "H6",
      "H7",
      "C5",
      "C6",
      "C7",
      "C8",
      "C9"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry whose archived and current annotations list all five transmembrane regions in choice B. These annotations have computational evidence code ECO:0000255, so they support the predicted regions but are not evidence of experimental validation."
  },
  "important_caveats": [
    "The supporting database features are computational predictions, not independently verified experimental measurements.",
    "The reviewer-only accession and annotation were not supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Both choices identify the same four regions and a final hydrophobic segment; they differ only slightly in the final segment's boundaries. The supplied sequence alone does not clearly resolve that boundary difference."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0011",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry whose archived and current annotations list all five transmembrane regions in choice B. These annotations have computational evidence code ECO:0000255, so they support the predicted regions but are not evidence of experimental validation.",
    "evidence_ids": ["H3", "H4", "H5", "H6", "H7", "C5", "C6", "C7", "C8", "C9"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains several hydrophobic stretches consistent with membrane-spanning helices, including a hydrophobic C-terminal segment. This supports predicting a final transmembrane region, but does not confidently determine its exact boundaries.",
    "missing_item_specific_fact": "The specific predicted endpoint annotation that places the final helix at 321..341 rather than 322..338.",
    "reason": "Distinguishing choices B and A requires exact boundary placement for a particular protein. The sequence supports a membrane-spanning helix in that region, but general hydrophobicity reasoning does not uniquely establish those precise coordinates."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Both choices identify the same four regions and a final hydrophobic segment; they differ only slightly in the final segment's boundaries. The supplied sequence alone does not clearly resolve that boundary difference."
  },
  "important_caveats": [
    "The supporting database features are computational predictions, not independently verified experimental measurements.",
    "The reviewer-only accession and annotation were not supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A2K3D1C8 (CRLS1_CHLRE, Cardiolipin synthase CMP-forming from Chlamydomonas reinhardtii) annotates exactly five transmembrane helical regions at 139..159, 191..211, 251..271, 280..300, and 321..341, matching option B precisely. The sequence SHA256 matches between the benchmark input and the source entry. However, all five annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred from homologs, not experimentally determined boundaries.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Option C (6..29) can be eliminated by noting that residues 6-29 (APSLLRRPITFVSSCPPALRSFGA) contain multiple charged and polar residues (R, R, P, S, C, P, R, S) incompatible with a TM helix. However, distinguishing A from B (boundary 322..338 vs 321..341) and B from D (presence/absence of the 5th TM) cannot be resolved by general biological reasoning from the sequence.


**Missing item-specific fact**

> The exact TM boundary assignment (321 vs 322 start; 341 vs 338 end) for the fifth helix is an arbitrary annotation choice not derivable from sequence properties. Additionally, the region 251..271 (AAAAGAATGAANGVASGGGGGG) is overwhelmingly polar (mostly Ala, Gly, Asn, Thr, Ser) and would NOT be predicted as TM by hydrophobicity analysis; its annotation rests entirely on homology transfer (ECO:0000255). The region 321..341 (LIMGLELATAATTVASGLAYG) is also only weakly hydrophobic. A model relying on sequence-based reasoning would likely miss several annotated TMs and could not resolve the 1-3 residue boundary differences between A and B.


**Reason**

> The annotated TM regions are not identifiable by standard hydrophobicity criteria from the sequence alone; they are homology-based predictions. The critical A-vs-B distinction (321..341 vs 322..338) is a 1-3 residue boundary difference within a weakly hydrophobic segment, which no general biological principle can resolve. The B-vs-D distinction (whether the weakly hydrophobic C-terminal region constitutes a TM) is likewise protein-specific. Selection of the correct answer requires knowledge of this particular entry's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B",
  "D"
]
```

> Option A (322..338) and B (321..341) differ by only 1 residue at the N-terminal boundary and 3 at the C-terminal boundary within a segment that is only weakly hydrophobic; neither boundary is clearly more correct from sequence alone. Option D (omitting the 5th TM entirely) is also defensible because the region 321-341 contains multiple polar residues (E, T, T, S, G, Y, G) and is not a canonical hydrophobic TM helix. Only option C is clearly wrong.


### Important caveats

- All five TM annotations carry ECO:0000255 (inferred by similarity), meaning they are computational predictions from homology, not experimental measurements. The exact boundaries are therefore somewhat arbitrary within the prediction.
- The region annotated as TM at 251..271 is overwhelmingly polar (Ala/Gly-rich with Asn, Thr, Ser) and would not be identified as TM by standard hydrophobicity-based predictors, making the question dependent on the specific homology-based annotation rather than sequence properties.
- The sequence match is confirmed (SHA256 identical), so the annotations do apply to the supplied sequence.
- The historical annotation (entry version 31) and current annotation (version 33) both contain the same five TM regions, so the answer key is stable across versions.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Option C (6..29) can be eliminated by noting that residues 6-29 (APSLLRRPITFVSSCPPALRSFGA) contain multiple charged and polar residues (R, R, P, S, C, P, R, S) incompatible with a TM helix. However, distinguishing A from B (boundary 322..338 vs 321..341) and B from D (presence/absence of the 5th TM) cannot be resolved by general biological reasoning from the sequence.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact TM boundary assignment (321 vs 322 start; 341 vs 338 end) for the fifth helix is an arbitrary annotation choice not derivable from sequence properties. Additionally, the region 251..271 (AAAAGAATGAANGVASGGGGGG) is overwhelmingly polar (mostly Ala, Gly, Asn, Thr, Ser) and would NOT be predicted as TM by hydrophobicity analysis; its annotation rests entirely on homology transfer (ECO:0000255). The region 321..341 (LIMGLELATAATTVASGLAYG) is also only weakly hydrophobic. A model relying on sequence-based reasoning would likely miss several annotated TMs and could not resolve the 1-3 residue boundary differences between A and B.",
    "reason": "The annotated TM regions are not identifiable by standard hydrophobicity criteria from the sequence alone; they are homology-based predictions. The critical A-vs-B distinction (321..341 vs 322..338) is a 1-3 residue boundary difference within a weakly hydrophobic segment, which no general biological principle can resolve. The B-vs-D distinction (whether the weakly hydrophobic C-terminal region constitutes a TM) is likewise protein-specific. Selection of the correct answer requires knowledge of this particular entry's annotation."
  },
  "case_id": "transmembrane_0011",
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
    "reason": "The UniProt entry A0A2K3D1C8 (CRLS1_CHLRE, Cardiolipin synthase CMP-forming from Chlamydomonas reinhardtii) annotates exactly five transmembrane helical regions at 139..159, 191..211, 251..271, 280..300, and 321..341, matching option B precisely. The sequence SHA256 matches between the benchmark input and the source entry. However, all five annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred from homologs, not experimentally determined boundaries."
  },
  "important_caveats": [
    "All five TM annotations carry ECO:0000255 (inferred by similarity), meaning they are computational predictions from homology, not experimental measurements. The exact boundaries are therefore somewhat arbitrary within the prediction.",
    "The region annotated as TM at 251..271 is overwhelmingly polar (Ala/Gly-rich with Asn, Thr, Ser) and would not be identified as TM by standard hydrophobicity-based predictors, making the question dependent on the specific homology-based annotation rather than sequence properties.",
    "The sequence match is confirmed (SHA256 identical), so the annotations do apply to the supplied sequence.",
    "The historical annotation (entry version 31) and current annotation (version 33) both contain the same five TM regions, so the answer key is stable across versions."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B",
      "D"
    ],
    "reason": "Option A (322..338) and B (321..341) differ by only 1 residue at the N-terminal boundary and 3 at the C-terminal boundary within a segment that is only weakly hydrophobic; neither boundary is clearly more correct from sequence alone. Option D (omitting the 5th TM entirely) is also defensible because the region 321-341 contains multiple polar residues (E, T, T, S, G, Y, G) and is not a canonical hydrophobic TM helix. Only option C is clearly wrong."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0011",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A2K3D1C8 (CRLS1_CHLRE, Cardiolipin synthase CMP-forming from Chlamydomonas reinhardtii) annotates exactly five transmembrane helical regions at 139..159, 191..211, 251..271, 280..300, and 321..341, matching option B precisely. The sequence SHA256 matches between the benchmark input and the source entry. However, all five annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred from homologs, not experimentally determined boundaries.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "H3", "H4", "H5", "H6", "H7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Option C (6..29) can be eliminated by noting that residues 6-29 (APSLLRRPITFVSSCPPALRSFGA) contain multiple charged and polar residues (R, R, P, S, C, P, R, S) incompatible with a TM helix. However, distinguishing A from B (boundary 322..338 vs 321..341) and B from D (presence/absence of the 5th TM) cannot be resolved by general biological reasoning from the sequence.",
    "missing_item_specific_fact": "The exact TM boundary assignment (321 vs 322 start; 341 vs 338 end) for the fifth helix is an arbitrary annotation choice not derivable from sequence properties. Additionally, the region 251..271 (AAAAGAATGAANGVASGGGGGG) is overwhelmingly polar (mostly Ala, Gly, Asn, Thr, Ser) and would NOT be predicted as TM by hydrophobicity analysis; its annotation rests entirely on homology transfer (ECO:0000255). The region 321..341 (LIMGLELATAATTVASGLAYG) is also only weakly hydrophobic. A model relying on sequence-based reasoning would likely miss several annotated TMs and could not resolve the 1-3 residue boundary differences between A and B.",
    "reason": "The annotated TM regions are not identifiable by standard hydrophobicity criteria from the sequence alone; they are homology-based predictions. The critical A-vs-B distinction (321..341 vs 322..338) is a 1-3 residue boundary difference within a weakly hydrophobic segment, which no general biological principle can resolve. The B-vs-D distinction (whether the weakly hydrophobic C-terminal region constitutes a TM) is likewise protein-specific. Selection of the correct answer requires knowledge of this particular entry's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B", "D"],
    "reason": "Option A (322..338) and B (321..341) differ by only 1 residue at the N-terminal boundary and 3 at the C-terminal boundary within a segment that is only weakly hydrophobic; neither boundary is clearly more correct from sequence alone. Option D (omitting the 5th TM entirely) is also defensible because the region 321-341 contains multiple polar residues (E, T, T, S, G, Y, G) and is not a canonical hydrophobic TM helix. Only option C is clearly wrong."
  },
  "important_caveats": [
    "All five TM annotations carry ECO:0000255 (inferred by similarity), meaning they are computational predictions from homology, not experimental measurements. The exact boundaries are therefore somewhat arbitrary within the prediction.",
    "The region annotated as TM at 251..271 is overwhelmingly polar (Ala/Gly-rich with Asn, Thr, Ser) and would not be identified as TM by standard hydrophobicity-based predictors, making the question dependent on the specific homology-based annotation rather than sequence properties.",
    "The sequence match is confirmed (SHA256 identical), so the annotations do apply to the supplied sequence.",
    "The historical annotation (entry version 31) and current annotation (version 33) both contain the same five TM regions, so the answer key is stable across versions."
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

**Accession:** `A0A2K3D1C8` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 31. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:48.321314+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":159},"start":{"modifier":"EXACT","value":139}},"type":"Transmembrane"}
```

Source SHA-256: `26e9b73e0d86ca30bf42039424c27469e24cd0f504b95de4718d0e72ea3a9a16`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json)  
**Locator:** `/features/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:48.321314+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":211},"start":{"modifier":"EXACT","value":191}},"type":"Transmembrane"}
```

Source SHA-256: `26e9b73e0d86ca30bf42039424c27469e24cd0f504b95de4718d0e72ea3a9a16`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:48.321314+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":271},"start":{"modifier":"EXACT","value":251}},"type":"Transmembrane"}
```

Source SHA-256: `26e9b73e0d86ca30bf42039424c27469e24cd0f504b95de4718d0e72ea3a9a16`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json)  
**Locator:** `/features/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:48.321314+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":300},"start":{"modifier":"EXACT","value":280}},"type":"Transmembrane"}
```

Source SHA-256: `26e9b73e0d86ca30bf42039424c27469e24cd0f504b95de4718d0e72ea3a9a16`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:48.321314+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":341},"start":{"modifier":"EXACT","value":321}},"type":"Transmembrane"}
```

Source SHA-256: `26e9b73e0d86ca30bf42039424c27469e24cd0f504b95de4718d0e72ea3a9a16`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31)  
**Locator:** `lines 118-120`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 31 / 1.  
**Retrieved:** 2026-11-02T04:24:52.248527+00:00.  

```text
FT   TRANSMEM        139..159
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `59f1e23ac2c4d5a40557e3d481dab63f297277a1a4b73ab6748fe911f7d4716c`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31)  
**Locator:** `lines 121-123`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 31 / 1.  
**Retrieved:** 2026-11-02T04:24:52.248527+00:00.  

```text
FT   TRANSMEM        191..211
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `59f1e23ac2c4d5a40557e3d481dab63f297277a1a4b73ab6748fe911f7d4716c`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31)  
**Locator:** `lines 124-126`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 31 / 1.  
**Retrieved:** 2026-11-02T04:24:52.248527+00:00.  

```text
FT   TRANSMEM        251..271
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `59f1e23ac2c4d5a40557e3d481dab63f297277a1a4b73ab6748fe911f7d4716c`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31)  
**Locator:** `lines 127-129`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 31 / 1.  
**Retrieved:** 2026-11-02T04:24:52.248527+00:00.  

```text
FT   TRANSMEM        280..300
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `59f1e23ac2c4d5a40557e3d481dab63f297277a1a4b73ab6748fe911f7d4716c`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31)  
**Locator:** `lines 130-132`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 31 / 1.  
**Retrieved:** 2026-11-02T04:24:52.248527+00:00.  

```text
FT   TRANSMEM        321..341
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `59f1e23ac2c4d5a40557e3d481dab63f297277a1a4b73ab6748fe911f7d4716c`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 11. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
