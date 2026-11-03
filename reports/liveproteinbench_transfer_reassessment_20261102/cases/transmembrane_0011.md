# transmembrane_0011: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/transmembrane_0011.txt)

**Task:** `transmembrane`  
**Author key, unchanged:** **B** — 139..159; 191..211; 251..271; 280..300; 321..341

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | usable output (valid_review) |
| after | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

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
<summary>Complete original system instructions</summary>

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

## Four saved visible reviews

## Before: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

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

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

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

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched historical UniProt record annotates all five spans in choice B. These annotations support the key, but their ECO:0000255 evidence is computational rather than experimental.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains several hydrophobic regions consistent with membrane-spanning helices, and transferable knowledge can support a multi-pass membrane-protein interpretation. But choices A and B differ only in the endpoints of the same overlapping final candidate helix; hydrophobicity and typical helix length do not uniquely establish those exact boundaries.


**Missing item-specific fact**

> The target-specific annotation or measurement fixing the final helix boundaries at 321..341 rather than 322..338.


**Reason**

> General sequence and membrane-protein knowledge can identify the likely spans, but it does not meaningfully resolve the small endpoint difference between A and B. Selecting the recorded coordinates requires an exact boundary annotation or measurement for this protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Both choices include the same four spans and overlapping versions of the final candidate helix. The supplied sequence does not establish a unique sharp boundary between the two proposed ranges.


### Important caveats

- The cited database features are computational predictions, not direct experimental confirmation.
- The historical record matches the supplied sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains several hydrophobic regions consistent with membrane-spanning helices, and transferable knowledge can support a multi-pass membrane-protein interpretation. But choices A and B differ only in the endpoints of the same overlapping final candidate helix; hydrophobicity and typical helix length do not uniquely establish those exact boundaries.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The target-specific annotation or measurement fixing the final helix boundaries at 321..341 rather than 322..338.",
    "reason": "General sequence and membrane-protein knowledge can identify the likely spans, but it does not meaningfully resolve the small endpoint difference between A and B. Selecting the recorded coordinates requires an exact boundary annotation or measurement for this protein."
  },
  "case_id": "transmembrane_0011",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H4",
      "H5",
      "H6",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record annotates all five spans in choice B. These annotations support the key, but their ECO:0000255 evidence is computational rather than experimental."
  },
  "important_caveats": [
    "The cited database features are computational predictions, not direct experimental confirmation.",
    "The historical record matches the supplied sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Both choices include the same four spans and overlapping versions of the final candidate helix. The supplied sequence does not establish a unique sharp boundary between the two proposed ranges."
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
    "reason": "The sequence-matched historical UniProt record annotates all five spans in choice B. These annotations support the key, but their ECO:0000255 evidence is computational rather than experimental.",
    "evidence_ids": ["H3", "H4", "H5", "H6", "H7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains several hydrophobic regions consistent with membrane-spanning helices, and transferable knowledge can support a multi-pass membrane-protein interpretation. But choices A and B differ only in the endpoints of the same overlapping final candidate helix; hydrophobicity and typical helix length do not uniquely establish those exact boundaries.",
    "missing_item_specific_fact": "The target-specific annotation or measurement fixing the final helix boundaries at 321..341 rather than 322..338.",
    "reason": "General sequence and membrane-protein knowledge can identify the likely spans, but it does not meaningfully resolve the small endpoint difference between A and B. Selecting the recorded coordinates requires an exact boundary annotation or measurement for this protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Both choices include the same four spans and overlapping versions of the final candidate helix. The supplied sequence does not establish a unique sharp boundary between the two proposed ranges."
  },
  "important_caveats": [
    "The cited database features are computational predictions, not direct experimental confirmation.",
    "The historical record matches the supplied sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for A0A2K3D1C8 lists exactly five transmembrane helical segments at 139-159, 191-211, 251-271, 280-300, and 321-341 (all ECO:0000255, by similarity). Choice B matches these coordinates precisely. The annotations are computational predictions transferred by similarity, not experimental determinations, but they are the recorded source annotation.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Option C (6..29) can be eliminated because the N-terminal region contains charged residues (R, R, R) and lacks the continuous hydrophobic stretch required for a TM helix. The 4-vs-5 TM question (D vs A/B) is borderline: the region around 321-341 has partial hydrophobic character (L, I, M, L, L, A, A, A, V, A, L, A) but also contains E, T, S, G, Y, G, making TM classification uncertain. The critical A-vs-B distinction (322..338 vs 321..341) is a 2-3 residue boundary shift. A weak biophysical argument exists: TM helices typically require ~19-20+ residues to span the ~30 Å hydrophobic core, so 17 residues (option A) falls below the typical minimum while 21 residues (option B) is within range. However, this argument is undermined by the poor overall hydrophobicity of the region—neither 17 nor 21 residues in this sequence constitutes a convincing TM helix by standard hydropathy criteria. The exact boundary is essentially an artifact of the specific prediction algorithm (Phobius/TMpred-type) used to generate the annotation.


**Missing item-specific fact**

> The exact start/end coordinates (321 vs 322; 338 vs 341) of the fifth transmembrane helix as assigned by the specific computational algorithm used in the UniProt annotation. The sequence in this region is too borderline for hydropathy analysis to reliably resolve a 2-3 residue boundary difference.


**Reason**

> The A-vs-B distinction hinges on a 2-3 residue boundary in a region with marginal hydrophobicity. While the 'minimum ~20 residues for a TM helix' principle provides a weak probabilistic preference for B (21 residues) over A (17 residues), the poor hydrophobicity of the region (containing E, T, S, Y, multiple G) means the TM classification itself is uncertain, making the length argument unreliable. The exact boundary is algorithm-specific and cannot be confidently resolved from the sequence alone. A model would need to recall the specific UniProt annotation coordinates.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B",
  "D"
]
```

> D (4 TM regions) is defensible because the fifth region (321-341) has poor hydrophobicity and could be rejected by strict criteria. A (322..338) is defensible because 17 residues, while short, is not impossible for a TM helix, and the region's hydrophobic core arguably ends around position 338. B is supported by the annotation and the 21-residue length argument, but the margin over A is small.


### Important caveats

- All five TM annotations carry evidence code ECO:0000255 (by similarity), meaning they are computational predictions transferred from related proteins, not experimentally validated.
- The fifth TM region (321-341) has the weakest hydrophobic character of the five annotated segments, making its classification and boundaries the most uncertain.
- The distinction between options A and B (322..338 vs 321..341) is within the typical ±2-3 residue uncertainty of TM prediction algorithms.
- The protein is annotated as a cardiolipin synthase (CMP-forming, EC 2.7.8.41) from Chlamydomonas, a membrane enzyme, but this identity was not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Option C (6..29) can be eliminated because the N-terminal region contains charged residues (R, R, R) and lacks the continuous hydrophobic stretch required for a TM helix. The 4-vs-5 TM question (D vs A/B) is borderline: the region around 321-341 has partial hydrophobic character (L, I, M, L, L, A, A, A, V, A, L, A) but also contains E, T, S, G, Y, G, making TM classification uncertain. The critical A-vs-B distinction (322..338 vs 321..341) is a 2-3 residue boundary shift. A weak biophysical argument exists: TM helices typically require ~19-20+ residues to span the ~30 Å hydrophobic core, so 17 residues (option A) falls below the typical minimum while 21 residues (option B) is within range. However, this argument is undermined by the poor overall hydrophobicity of the region—neither 17 nor 21 residues in this sequence constitutes a convincing TM helix by standard hydropathy criteria. The exact boundary is essentially an artifact of the specific prediction algorithm (Phobius/TMpred-type) used to generate the annotation.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact start/end coordinates (321 vs 322; 338 vs 341) of the fifth transmembrane helix as assigned by the specific computational algorithm used in the UniProt annotation. The sequence in this region is too borderline for hydropathy analysis to reliably resolve a 2-3 residue boundary difference.",
    "reason": "The A-vs-B distinction hinges on a 2-3 residue boundary in a region with marginal hydrophobicity. While the 'minimum ~20 residues for a TM helix' principle provides a weak probabilistic preference for B (21 residues) over A (17 residues), the poor hydrophobicity of the region (containing E, T, S, Y, multiple G) means the TM classification itself is uncertain, making the length argument unreliable. The exact boundary is algorithm-specific and cannot be confidently resolved from the sequence alone. A model would need to recall the specific UniProt annotation coordinates."
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
    "reason": "The UniProt annotation for A0A2K3D1C8 lists exactly five transmembrane helical segments at 139-159, 191-211, 251-271, 280-300, and 321-341 (all ECO:0000255, by similarity). Choice B matches these coordinates precisely. The annotations are computational predictions transferred by similarity, not experimental determinations, but they are the recorded source annotation."
  },
  "important_caveats": [
    "All five TM annotations carry evidence code ECO:0000255 (by similarity), meaning they are computational predictions transferred from related proteins, not experimentally validated.",
    "The fifth TM region (321-341) has the weakest hydrophobic character of the five annotated segments, making its classification and boundaries the most uncertain.",
    "The distinction between options A and B (322..338 vs 321..341) is within the typical ±2-3 residue uncertainty of TM prediction algorithms.",
    "The protein is annotated as a cardiolipin synthase (CMP-forming, EC 2.7.8.41) from Chlamydomonas, a membrane enzyme, but this identity was not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B",
      "D"
    ],
    "reason": "D (4 TM regions) is defensible because the fifth region (321-341) has poor hydrophobicity and could be rejected by strict criteria. A (322..338) is defensible because 17 residues, while short, is not impossible for a TM helix, and the region's hydrophobic core arguably ends around position 338. B is supported by the annotation and the 21-residue length argument, but the margin over A is small."
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
    "reason": "The UniProt annotation for A0A2K3D1C8 lists exactly five transmembrane helical segments at 139-159, 191-211, 251-271, 280-300, and 321-341 (all ECO:0000255, by similarity). Choice B matches these coordinates precisely. The annotations are computational predictions transferred by similarity, not experimental determinations, but they are the recorded source annotation.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "H3", "H4", "H5", "H6", "H7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Option C (6..29) can be eliminated because the N-terminal region contains charged residues (R, R, R) and lacks the continuous hydrophobic stretch required for a TM helix. The 4-vs-5 TM question (D vs A/B) is borderline: the region around 321-341 has partial hydrophobic character (L, I, M, L, L, A, A, A, V, A, L, A) but also contains E, T, S, G, Y, G, making TM classification uncertain. The critical A-vs-B distinction (322..338 vs 321..341) is a 2-3 residue boundary shift. A weak biophysical argument exists: TM helices typically require ~19-20+ residues to span the ~30 Å hydrophobic core, so 17 residues (option A) falls below the typical minimum while 21 residues (option B) is within range. However, this argument is undermined by the poor overall hydrophobicity of the region—neither 17 nor 21 residues in this sequence constitutes a convincing TM helix by standard hydropathy criteria. The exact boundary is essentially an artifact of the specific prediction algorithm (Phobius/TMpred-type) used to generate the annotation.",
    "missing_item_specific_fact": "The exact start/end coordinates (321 vs 322; 338 vs 341) of the fifth transmembrane helix as assigned by the specific computational algorithm used in the UniProt annotation. The sequence in this region is too borderline for hydropathy analysis to reliably resolve a 2-3 residue boundary difference.",
    "reason": "The A-vs-B distinction hinges on a 2-3 residue boundary in a region with marginal hydrophobicity. While the 'minimum ~20 residues for a TM helix' principle provides a weak probabilistic preference for B (21 residues) over A (17 residues), the poor hydrophobicity of the region (containing E, T, S, Y, multiple G) means the TM classification itself is uncertain, making the length argument unreliable. The exact boundary is algorithm-specific and cannot be confidently resolved from the sequence alone. A model would need to recall the specific UniProt annotation coordinates."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B", "D"],
    "reason": "D (4 TM regions) is defensible because the fifth region (321-341) has poor hydrophobicity and could be rejected by strict criteria. A (322..338) is defensible because 17 residues, while short, is not impossible for a TM helix, and the region's hydrophobic core arguably ends around position 338. B is supported by the annotation and the 21-residue length argument, but the margin over A is small."
  },
  "important_caveats": [
    "All five TM annotations carry evidence code ECO:0000255 (by similarity), meaning they are computational predictions transferred from related proteins, not experimentally validated.",
    "The fifth TM region (321-341) has the weakest hydrophobic character of the five annotated segments, making its classification and boundaries the most uncertain.",
    "The distinction between options A and B (322..338 vs 321..341) is within the typical ±2-3 residue uncertainty of TM prediction algorithms.",
    "The protein is annotated as a cardiolipin synthase (CMP-forming, EC 2.7.8.41) from Chlamydomonas, a membrane enzyme, but this identity was not provided to the evaluated model."
  ]
}
```

</details>

## Existing project source checks of the old Luna review only

These unchanged notes concern the earlier Luna claims. They do not validate either new review or the old Qwen review. No new scientific adjudication was performed.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Complete reviewer-only evidence and qualifications

All excerpts supplied in the original and revised reviewer user message follow. This material was not available to the original evaluated model. Accession identity came from dataset image-path metadata. Source support and transferable discrimination are separate judgments.

**Applicability metadata, unchanged:**

```json
{
  "requested_accession": "A0A2K3D1C8",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "d5caa566c264b21e72ce662ef50949e75c0df2a96713facfc4330fbd74359ca1",
  "benchmark_sequence_length": 351,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 33,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2018-03-28",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "26e9b73e0d86ca30bf42039424c27469e24cd0f504b95de4718d0e72ea3a9a16",
  "current_source_sequence_sha256": "d5caa566c264b21e72ce662ef50949e75c0df2a96713facfc4330fbd74359ca1",
  "current_source_sequence_length": 351,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 31,
  "selected_historical_version": {
    "accession": "A0A2K3D1C8",
    "database": "Swiss-Prot",
    "entryVersion": 31,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CRLS1_CHLRE",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "59f1e23ac2c4d5a40557e3d481dab63f297277a1a4b73ab6748fe911f7d4716c",
  "selected_historical_source_sequence_sha256": "d5caa566c264b21e72ce662ef50949e75c0df2a96713facfc4330fbd74359ca1",
  "selected_historical_source_sequence_length": 351,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 31,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "actual_author_source_snapshot": "unknown",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed."
}
```

**Qualifications, unchanged:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json",
  "source_sha256": "26e9b73e0d86ca30bf42039424c27469e24cd0f504b95de4718d0e72ea3a9a16",
  "retrieved_utc": "2026-11-02T04:24:48.321314+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"A0A2K3D1C8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json",
  "source_sha256": "26e9b73e0d86ca30bf42039424c27469e24cd0f504b95de4718d0e72ea3a9a16",
  "retrieved_utc": "2026-11-02T04:24:48.321314+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":33,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2018-03-28\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json",
  "source_sha256": "26e9b73e0d86ca30bf42039424c27469e24cd0f504b95de4718d0e72ea3a9a16",
  "retrieved_utc": "2026-11-02T04:24:48.321314+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Chlamydomonas smithii\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000006906\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Chlorophyta\",\"core chlorophytes\",\"Chlorophyceae\",\"CS clade\",\"Chlamydomonadales\",\"Chlamydomonadaceae\",\"Chlamydomonas\"],\"scientificName\":\"Chlamydomonas reinhardtii\",\"taxonId\":3055}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json",
  "source_sha256": "26e9b73e0d86ca30bf42039424c27469e24cd0f504b95de4718d0e72ea3a9a16",
  "retrieved_utc": "2026-11-02T04:24:48.321314+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"26793177\",\"source\":\"PubMed\"}],\"value\":\"2.7.8.41\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Cardiolipin synthase (CMP-forming)\"},\"shortNames\":[{\"value\":\"CLS\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json",
  "source_sha256": "26e9b73e0d86ca30bf42039424c27469e24cd0f504b95de4718d0e72ea3a9a16",
  "retrieved_utc": "2026-11-02T04:24:48.321314+00:00",
  "json_pointer": "/features/2",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":159},\"start\":{\"modifier\":\"EXACT\",\"value\":139}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json",
  "source_sha256": "26e9b73e0d86ca30bf42039424c27469e24cd0f504b95de4718d0e72ea3a9a16",
  "retrieved_utc": "2026-11-02T04:24:48.321314+00:00",
  "json_pointer": "/features/3",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":211},\"start\":{\"modifier\":\"EXACT\",\"value\":191}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json",
  "source_sha256": "26e9b73e0d86ca30bf42039424c27469e24cd0f504b95de4718d0e72ea3a9a16",
  "retrieved_utc": "2026-11-02T04:24:48.321314+00:00",
  "json_pointer": "/features/4",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":271},\"start\":{\"modifier\":\"EXACT\",\"value\":251}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json",
  "source_sha256": "26e9b73e0d86ca30bf42039424c27469e24cd0f504b95de4718d0e72ea3a9a16",
  "retrieved_utc": "2026-11-02T04:24:48.321314+00:00",
  "json_pointer": "/features/5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":300},\"start\":{\"modifier\":\"EXACT\",\"value\":280}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json",
  "source_sha256": "26e9b73e0d86ca30bf42039424c27469e24cd0f504b95de4718d0e72ea3a9a16",
  "retrieved_utc": "2026-11-02T04:24:48.321314+00:00",
  "json_pointer": "/features/6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":341},\"start\":{\"modifier\":\"EXACT\",\"value\":321}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json)

```json
{
  "evidence_id": "C10",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json",
  "source_sha256": "26e9b73e0d86ca30bf42039424c27469e24cd0f504b95de4718d0e72ea3a9a16",
  "retrieved_utc": "2026-11-02T04:24:48.321314+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Hung C.H.\",\"Kobayashi K.\",\"Wada H.\",\"Nakamura Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"26793177\"},{\"database\":\"DOI\",\"id\":\"10.3389/fmicb.2015.01542\"}],\"citationType\":\"journal article\",\"firstPage\":\"1542\",\"id\":\"26793177\",\"journal\":\"Front. Microbiol.\",\"lastPage\":\"1542\",\"publicationDate\":\"2015\",\"title\":\"Functional Specificity of Cardiolipin Synthase Revealed by the Identification of a Cardiolipin Synthase CrCLS1 in Chlamydomonas reinhardtii.\",\"volume\":\"6\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31",
  "source_sha256": "59f1e23ac2c4d5a40557e3d481dab63f297277a1a4b73ab6748fe911f7d4716c",
  "retrieved_utc": "2026-11-02T04:24:52.248527+00:00",
  "source_locator": "lines 1-14",
  "excerpt": "ID   CRLS1_CHLRE             Reviewed;         351 AA.\nAC   A0A2K3D1C8;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   28-MAR-2018, sequence version 1.\nDT   28-JAN-2026, entry version 31.\nDE   RecName: Full=Cardiolipin synthase (CMP-forming) {ECO:0000305};\nDE            Short=CLS;\nDE            EC=2.7.8.41 {ECO:0000305|PubMed:26793177};\nDE   Flags: Precursor;\nGN   ORFNames=CHLRE_13g604700v5 {ECO:0000312|EMBL:PNW74341.1};\nOS   Chlamydomonas reinhardtii (Chlamydomonas smithii).\nOC   Eukaryota; Viridiplantae; Chlorophyta; core chlorophytes; Chlorophyceae;\nOC   CS clade; Chlamydomonadales; Chlamydomonadaceae; Chlamydomonas.\nOX   NCBI_TaxID=3055 {ECO:0000312|Proteomes:UP000006906};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 31,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31",
  "source_sha256": "59f1e23ac2c4d5a40557e3d481dab63f297277a1a4b73ab6748fe911f7d4716c",
  "retrieved_utc": "2026-11-02T04:24:52.248527+00:00",
  "source_locator": "lines 43-50",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, AND CATALYTIC ACTIVITY.\nRX   PubMed=26793177; DOI=10.3389/fmicb.2015.01542;\nRA   Hung C.H., Kobayashi K., Wada H., Nakamura Y.;\nRT   \"Functional Specificity of Cardiolipin Synthase Revealed by the\nRT   Identification of a Cardiolipin Synthase CrCLS1 in Chlamydomonas\nRT   reinhardtii.\";\nRL   Front. Microbiol. 6:1542-1542(2015).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 31,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31",
  "source_sha256": "59f1e23ac2c4d5a40557e3d481dab63f297277a1a4b73ab6748fe911f7d4716c",
  "retrieved_utc": "2026-11-02T04:24:52.248527+00:00",
  "source_locator": "lines 118-120",
  "excerpt": "FT   TRANSMEM        139..159\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 31,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31",
  "source_sha256": "59f1e23ac2c4d5a40557e3d481dab63f297277a1a4b73ab6748fe911f7d4716c",
  "retrieved_utc": "2026-11-02T04:24:52.248527+00:00",
  "source_locator": "lines 121-123",
  "excerpt": "FT   TRANSMEM        191..211\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 31,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31",
  "source_sha256": "59f1e23ac2c4d5a40557e3d481dab63f297277a1a4b73ab6748fe911f7d4716c",
  "retrieved_utc": "2026-11-02T04:24:52.248527+00:00",
  "source_locator": "lines 124-126",
  "excerpt": "FT   TRANSMEM        251..271\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 31,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31",
  "source_sha256": "59f1e23ac2c4d5a40557e3d481dab63f297277a1a4b73ab6748fe911f7d4716c",
  "retrieved_utc": "2026-11-02T04:24:52.248527+00:00",
  "source_locator": "lines 127-129",
  "excerpt": "FT   TRANSMEM        280..300\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 31,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31)

```json
{
  "evidence_id": "H7",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31",
  "source_sha256": "59f1e23ac2c4d5a40557e3d481dab63f297277a1a4b73ab6748fe911f7d4716c",
  "retrieved_utc": "2026-11-02T04:24:52.248527+00:00",
  "source_locator": "lines 130-132",
  "excerpt": "FT   TRANSMEM        321..341\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 31,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 11. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
