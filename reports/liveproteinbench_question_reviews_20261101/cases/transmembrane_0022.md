# transmembrane_0022

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **B** — 12..32; 181..201; 220..240; 244..264; 285..305; 312..332; 346..366; 398..418

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MIIDLFQSKKLIISIIILILRISLFSCAEHLFFNNNFNFFNFSENNHAKVNELNIDTKYLYQGLRNINIYLALSALNGITKEKINDISQWNGYKTRNNDETNISNVVVTEWKQLNKKSFFLKNNNISNNDNLIKGMPNPYFINSLTEDINNINLYFNIRNDIKYGEIIYKGTYIPHIYNNIFLIFLISYMYWFCIKILFNGYIKGKYVAKEYILKISTLFIFFVILKISLIFLPAILSCIVCLILTFYFYSISMSPCKDIFYLFESTRIKKEPIGWIIIVYAESILIGNVIYNFLCPPKIIIIFIRYIQNDFLVKIICLTIILFISFLIFFLMISNIFPAKKAQNFVFSFTSSYLIVSCFAYFWNIFLLRFLNNTNIFQIEPIMFFSYTPKFVFNRQNMFALFMIFAMSILSIIFPRIKKLKQNIFDMKENIYDSDIDIGKASKNRYNIILNYFT

[Multiple Choices]
A. 12..32; 181..201; 220..240; 249..261; 285..305; 312..332; 346..366; 398..418
B. 12..32; 181..201; 220..240; 244..264; 285..305; 312..332; 346..366; 398..418
C. 6..26
D. 12..32; 181..201; 220..240; 285..305; 312..332; 346..366; 398..418
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

> The sequence-matched historical UniProt entry annotates the eight spans listed in B, including 244..264. These are computationally supported annotations (ECO:0000255), not evidence of experimental boundary measurement.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains multiple hydrophobic stretches consistent with transmembrane helices, but that general pattern does not establish the precise annotated boundaries or uniquely resolve the 244..264 interval versus the shorter 249..261 alternative.


**Missing item-specific fact**

> The protein-specific transmembrane annotation giving the span 244..264 and the remaining listed coordinates.


**Reason**

> Selecting B's exact coordinate set depends on protein-specific boundary annotations absent from the input. The sequence supports a multipass membrane-protein prediction, but does not independently establish those precise boundaries.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> B matches the sequence-matched annotated coordinate set. The shorter interval in A lies within the hydrophobic region but is not an equally supported complete membrane-spanning segment.


### Important caveats

- The cited historical UniProt record matches the supplied sequence, but the author's exact source snapshot is unknown.
- The transmembrane features carry computational evidence; this supports the key as an annotation, not as experimentally verified boundaries.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple hydrophobic stretches consistent with transmembrane helices, but that general pattern does not establish the precise annotated boundaries or uniquely resolve the 244..264 interval versus the shorter 249..261 alternative.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific transmembrane annotation giving the span 244..264 and the remaining listed coordinates.",
    "reason": "Selecting B's exact coordinate set depends on protein-specific boundary annotations absent from the input. The sequence supports a multipass membrane-protein prediction, but does not independently establish those precise boundaries."
  },
  "case_id": "transmembrane_0022",
  "expected_answer_check": {
    "evidence_ids": [
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
    "reason": "The sequence-matched historical UniProt entry annotates the eight spans listed in B, including 244..264. These are computationally supported annotations (ECO:0000255), not evidence of experimental boundary measurement."
  },
  "important_caveats": [
    "The cited historical UniProt record matches the supplied sequence, but the author's exact source snapshot is unknown.",
    "The transmembrane features carry computational evidence; this supports the key as an annotation, not as experimentally verified boundaries."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B matches the sequence-matched annotated coordinate set. The shorter interval in A lies within the hydrophobic region but is not an equally supported complete membrane-spanning segment."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0022",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt entry annotates the eight spans listed in B, including 244..264. These are computationally supported annotations (ECO:0000255), not evidence of experimental boundary measurement.",
    "evidence_ids": ["H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains multiple hydrophobic stretches consistent with transmembrane helices, but that general pattern does not establish the precise annotated boundaries or uniquely resolve the 244..264 interval versus the shorter 249..261 alternative.",
    "missing_item_specific_fact": "The protein-specific transmembrane annotation giving the span 244..264 and the remaining listed coordinates.",
    "reason": "Selecting B's exact coordinate set depends on protein-specific boundary annotations absent from the input. The sequence supports a multipass membrane-protein prediction, but does not independently establish those precise boundaries."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B matches the sequence-matched annotated coordinate set. The shorter interval in A lies within the hydrophobic region but is not an equally supported complete membrane-spanning segment."
  },
  "important_caveats": [
    "The cited historical UniProt record matches the supplied sequence, but the author's exact source snapshot is unknown.",
    "The transmembrane features carry computational evidence; this supports the key as an annotation, not as experimentally verified boundaries."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A509AKT6 (PBS54_PLABA, sequence SHA256 matched) annotates exactly eight transmembrane helical regions at 12..32, 181..201, 220..240, 244..264, 285..305, 312..332, 346..366, and 398..418, matching option B precisely. The evidence code is ECO:0000255 (inferred by similarity), so this is a computational annotation rather than experimental data, but it is the authoritative reference annotation for this entry.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Distinguishing A from B is partly reasoning-supported: option A lists the fourth TM as 249..261 (13 residues), which is too short to span the ~30 Å hydrophobic core of a lipid bilayer (typically ≥18–20 residues needed), whereas B's 244..264 (21 residues) meets the length requirement. Option C (6..26) is clearly wrong because the N-terminal 1–10 residues include charged KK at positions 9–10 and the annotated TM starts at 12. However, the critical B-vs-D distinction (whether 244..264 is a TM helix at all) is not cleanly resolvable by general reasoning.


**Missing item-specific fact**

> The region 244..264 (ILTFYFYSISMSPCKDIFYLF) has an average hydrophobicity notably lower than the other seven annotated TM segments (~1.1 vs ~2.2 on a Kyte-Doolittle-like scale) and contains a proline (helix breaker) plus a lysine and aspartate (charged) in its middle. Whether this borderline segment qualifies as a TM helix depends on the specific prediction method and similarity-based annotation used, not on a clear-cut hydrophobicity threshold that general reasoning would resolve unambiguously.


**Reason**

> The B-vs-D choice hinges on the inclusion of a borderline hydrophobic segment that contains charged residues and a proline. General hydrophobicity analysis could reasonably go either way. The definitive answer comes from the UniProt similarity-based annotation (ECO:0000255), making this lookup-dependent for the key distinction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> Option D omits the 244..264 region. Because that segment contains K, D, and P residues that are atypical for a TM helix and has lower hydrophobicity than the other seven segments, a model applying a strict hydrophobicity window or helix-propensity filter could reasonably exclude it, making D a defensible alternative. The annotation includes it, but the sequence itself does not make inclusion unambiguous.


### Important caveats

- All eight TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning the 'ground truth' is itself a computational prediction, not experimental data (e.g., crystallography or cryo-EM).
- The UniProt entry was first public in February 2025; the author's source snapshot date is unknown, though the sequence version has not changed since 2019.
- The functional characterization reference (PubMed 37774810) addresses Pbs54's role in gamete fertilization and subcellular location but does not appear to provide experimental TM topology; the TM boundaries are purely annotation-derived.
- Option A's 249..261 (13 residues) is defensibly wrong on length grounds, and option C (6..26) is clearly wrong, so the real discrimination is B vs D.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Distinguishing A from B is partly reasoning-supported: option A lists the fourth TM as 249..261 (13 residues), which is too short to span the ~30 Å hydrophobic core of a lipid bilayer (typically ≥18–20 residues needed), whereas B's 244..264 (21 residues) meets the length requirement. Option C (6..26) is clearly wrong because the N-terminal 1–10 residues include charged KK at positions 9–10 and the annotated TM starts at 12. However, the critical B-vs-D distinction (whether 244..264 is a TM helix at all) is not cleanly resolvable by general reasoning.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The region 244..264 (ILTFYFYSISMSPCKDIFYLF) has an average hydrophobicity notably lower than the other seven annotated TM segments (~1.1 vs ~2.2 on a Kyte-Doolittle-like scale) and contains a proline (helix breaker) plus a lysine and aspartate (charged) in its middle. Whether this borderline segment qualifies as a TM helix depends on the specific prediction method and similarity-based annotation used, not on a clear-cut hydrophobicity threshold that general reasoning would resolve unambiguously.",
    "reason": "The B-vs-D choice hinges on the inclusion of a borderline hydrophobic segment that contains charged residues and a proline. General hydrophobicity analysis could reasonably go either way. The definitive answer comes from the UniProt similarity-based annotation (ECO:0000255), making this lookup-dependent for the key distinction."
  },
  "case_id": "transmembrane_0022",
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
    "reason": "The UniProt entry A0A509AKT6 (PBS54_PLABA, sequence SHA256 matched) annotates exactly eight transmembrane helical regions at 12..32, 181..201, 220..240, 244..264, 285..305, 312..332, 346..366, and 398..418, matching option B precisely. The evidence code is ECO:0000255 (inferred by similarity), so this is a computational annotation rather than experimental data, but it is the authoritative reference annotation for this entry."
  },
  "important_caveats": [
    "All eight TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning the 'ground truth' is itself a computational prediction, not experimental data (e.g., crystallography or cryo-EM).",
    "The UniProt entry was first public in February 2025; the author's source snapshot date is unknown, though the sequence version has not changed since 2019.",
    "The functional characterization reference (PubMed 37774810) addresses Pbs54's role in gamete fertilization and subcellular location but does not appear to provide experimental TM topology; the TM boundaries are purely annotation-derived.",
    "Option A's 249..261 (13 residues) is defensibly wrong on length grounds, and option C (6..26) is clearly wrong, so the real discrimination is B vs D."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "Option D omits the 244..264 region. Because that segment contains K, D, and P residues that are atypical for a TM helix and has lower hydrophobicity than the other seven segments, a model applying a strict hydrophobicity window or helix-propensity filter could reasonably exclude it, making D a defensible alternative. The annotation includes it, but the sequence itself does not make inclusion unambiguous."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0022",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A509AKT6 (PBS54_PLABA, sequence SHA256 matched) annotates exactly eight transmembrane helical regions at 12..32, 181..201, 220..240, 244..264, 285..305, 312..332, 346..366, and 398..418, matching option B precisely. The evidence code is ECO:0000255 (inferred by similarity), so this is a computational annotation rather than experimental data, but it is the authoritative reference annotation for this entry.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Distinguishing A from B is partly reasoning-supported: option A lists the fourth TM as 249..261 (13 residues), which is too short to span the ~30 Å hydrophobic core of a lipid bilayer (typically ≥18–20 residues needed), whereas B's 244..264 (21 residues) meets the length requirement. Option C (6..26) is clearly wrong because the N-terminal 1–10 residues include charged KK at positions 9–10 and the annotated TM starts at 12. However, the critical B-vs-D distinction (whether 244..264 is a TM helix at all) is not cleanly resolvable by general reasoning.",
    "missing_item_specific_fact": "The region 244..264 (ILTFYFYSISMSPCKDIFYLF) has an average hydrophobicity notably lower than the other seven annotated TM segments (~1.1 vs ~2.2 on a Kyte-Doolittle-like scale) and contains a proline (helix breaker) plus a lysine and aspartate (charged) in its middle. Whether this borderline segment qualifies as a TM helix depends on the specific prediction method and similarity-based annotation used, not on a clear-cut hydrophobicity threshold that general reasoning would resolve unambiguously.",
    "reason": "The B-vs-D choice hinges on the inclusion of a borderline hydrophobic segment that contains charged residues and a proline. General hydrophobicity analysis could reasonably go either way. The definitive answer comes from the UniProt similarity-based annotation (ECO:0000255), making this lookup-dependent for the key distinction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "Option D omits the 244..264 region. Because that segment contains K, D, and P residues that are atypical for a TM helix and has lower hydrophobicity than the other seven segments, a model applying a strict hydrophobicity window or helix-propensity filter could reasonably exclude it, making D a defensible alternative. The annotation includes it, but the sequence itself does not make inclusion unambiguous."
  },
  "important_caveats": [
    "All eight TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning the 'ground truth' is itself a computational prediction, not experimental data (e.g., crystallography or cryo-EM).",
    "The UniProt entry was first public in February 2025; the author's source snapshot date is unknown, though the sequence version has not changed since 2019.",
    "The functional characterization reference (PubMed 37774810) addresses Pbs54's role in gamete fertilization and subcellular location but does not appear to provide experimental TM topology; the TM boundaries are purely annotation-derived.",
    "Option A's 249..261 (13 residues) is defensibly wrong on length grounds, and option C (6..26) is clearly wrong, so the real discrimination is B vs D."
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

**Accession:** `A0A509AKT6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 19. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AKT6.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:23.898557+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":32},"start":{"modifier":"EXACT","value":12}},"type":"Transmembrane"}
```

Source SHA-256: `5f12f41d692d932165f3b4e32653a23e5a692f941e64b936309ea1b6a4bbad25`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AKT6.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:23.898557+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":201},"start":{"modifier":"EXACT","value":181}},"type":"Transmembrane"}
```

Source SHA-256: `5f12f41d692d932165f3b4e32653a23e5a692f941e64b936309ea1b6a4bbad25`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AKT6.json)  
**Locator:** `/features/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:23.898557+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":240},"start":{"modifier":"EXACT","value":220}},"type":"Transmembrane"}
```

Source SHA-256: `5f12f41d692d932165f3b4e32653a23e5a692f941e64b936309ea1b6a4bbad25`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AKT6.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:23.898557+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":264},"start":{"modifier":"EXACT","value":244}},"type":"Transmembrane"}
```

Source SHA-256: `5f12f41d692d932165f3b4e32653a23e5a692f941e64b936309ea1b6a4bbad25`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AKT6.json)  
**Locator:** `/features/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:23.898557+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":305},"start":{"modifier":"EXACT","value":285}},"type":"Transmembrane"}
```

Source SHA-256: `5f12f41d692d932165f3b4e32653a23e5a692f941e64b936309ea1b6a4bbad25`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AKT6.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:23.898557+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":332},"start":{"modifier":"EXACT","value":312}},"type":"Transmembrane"}
```

Source SHA-256: `5f12f41d692d932165f3b4e32653a23e5a692f941e64b936309ea1b6a4bbad25`.

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AKT6.json)  
**Locator:** `/features/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:23.898557+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":366},"start":{"modifier":"EXACT","value":346}},"type":"Transmembrane"}
```

Source SHA-256: `5f12f41d692d932165f3b4e32653a23e5a692f941e64b936309ea1b6a4bbad25`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AKT6.json)  
**Locator:** `/features/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:23.898557+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":418},"start":{"modifier":"EXACT","value":398}},"type":"Transmembrane"}
```

Source SHA-256: `5f12f41d692d932165f3b4e32653a23e5a692f941e64b936309ea1b6a4bbad25`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AKT6?format=txt&versions=19)  
**Locator:** `lines 82-84`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:25:27.030552+00:00.  

```text
FT   TRANSMEM        12..32
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `6d40908ee73c41ed5a2c9670ef889cabc4ff6bd15769a8b8824958da5cb4a8f5`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AKT6?format=txt&versions=19)  
**Locator:** `lines 85-87`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:25:27.030552+00:00.  

```text
FT   TRANSMEM        181..201
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `6d40908ee73c41ed5a2c9670ef889cabc4ff6bd15769a8b8824958da5cb4a8f5`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AKT6?format=txt&versions=19)  
**Locator:** `lines 88-90`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:25:27.030552+00:00.  

```text
FT   TRANSMEM        220..240
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `6d40908ee73c41ed5a2c9670ef889cabc4ff6bd15769a8b8824958da5cb4a8f5`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AKT6?format=txt&versions=19)  
**Locator:** `lines 91-93`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:25:27.030552+00:00.  

```text
FT   TRANSMEM        244..264
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `6d40908ee73c41ed5a2c9670ef889cabc4ff6bd15769a8b8824958da5cb4a8f5`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AKT6?format=txt&versions=19)  
**Locator:** `lines 94-96`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:25:27.030552+00:00.  

```text
FT   TRANSMEM        285..305
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `6d40908ee73c41ed5a2c9670ef889cabc4ff6bd15769a8b8824958da5cb4a8f5`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AKT6?format=txt&versions=19)  
**Locator:** `lines 97-99`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:25:27.030552+00:00.  

```text
FT   TRANSMEM        312..332
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `6d40908ee73c41ed5a2c9670ef889cabc4ff6bd15769a8b8824958da5cb4a8f5`.

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AKT6?format=txt&versions=19)  
**Locator:** `lines 100-102`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:25:27.030552+00:00.  

```text
FT   TRANSMEM        346..366
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `6d40908ee73c41ed5a2c9670ef889cabc4ff6bd15769a8b8824958da5cb4a8f5`.

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AKT6?format=txt&versions=19)  
**Locator:** `lines 103-105`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:25:27.030552+00:00.  

```text
FT   TRANSMEM        398..418
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `6d40908ee73c41ed5a2c9670ef889cabc4ff6bd15769a8b8824958da5cb4a8f5`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 22. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
