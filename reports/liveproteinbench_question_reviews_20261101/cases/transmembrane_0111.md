# transmembrane_0111

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **D** — 42..64; 84..103; 110..131; 137..157; 177..195; 201..221; 242..261; 281..301; 313..331; 347..367; 417..438

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MIEKSNNPFLSIDPIVERTKSNGEGLPLLSEKTKKGFDFTQIVVYLVGLSDGLTHLASLAIYYLFKDYFRLTPYQVSLILMYPYIPFILKPVIALITDSFSIFGMRRKPYLFLFSLFQSLNFLALAFLNLSVIQASLILFFISLCASFCTTVAEALVVESSMGQTYSQGTNKVTEFIASKAIGSLSVAYFSGYFLEKMPREYIFIATSIFPLIISLSCLFLKEKEYSTNRNIFNQLSDLIKFINTPIFLGPFLYIFVYMSGPDYDDAFFFFCTNKLGFRPSFMGTLRLTYGIASLIGIIIYRVFLKNCSLRKTLIITTLVSFPIYISPIILTEHINKFLGISNELFVLSGGFLIEAITEIQLLPLFILTANICQPGLEASVFATILSVKNLGSLTKKGTSSFITYLMKIDSYNFDNLSLYILTCGFFLLFSLTLVPLLPNEEHIEKLKNKETSKG

[Multiple Choices]
A. 308..328; 344..364; 474..494; 533..553; 640..660; 670..690; 731..751; 771..791; 807..827; 851..871; 937..957; 1162..1182; 1209..1229; 1244..1264; 1306..1326; 1381..1401; 1422..1442; 1498..1518; 1532..1552; 1561..1581; 1633..1653; 1671..1691; 1722..1742
B. 42..64; 84..103; 110..131; 138..157; 177..195; 201..221; 242..261; 281..301; 313..331; 347..367; 417..438
C. 42..64; 84..103; 110..131; 137..157; 177..195; 201..221; 242..261; 281..301; 347..367; 417..438
D. 42..64; 84..103; 110..131; 137..157; 177..195; 201..221; 242..261; 281..301; 313..331; 347..367; 417..438
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

> The sequence matches the 455-aa UniProt entry, whose annotated transmembrane segments correspond to choice D. These features carry ECO:0000255, indicating computational annotation rather than direct experimental confirmation.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [C13](#evidence-c13), [C14](#evidence-c14), [C15](#evidence-c15).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has multiple strongly hydrophobic stretches consistent with membrane-spanning helices, including the regions represented in the choices. That supports identifying likely helices, but does not reliably determine every exact endpoint.


**Missing item-specific fact**

> The protein-specific transmembrane annotation, especially the exact boundary at 137 versus 138 and the inclusion of 313..331, is not supplied in the question.


**Reason**

> Choosing the complete set and its precise residue boundaries depends on protein-specific annotation or prediction. General hydropathy reasoning can support the broad regions but cannot robustly distinguish the one-residue boundary difference between B and D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> B and D differ only in whether the fourth segment starts at residue 138 or 137; both are plausible boundaries for a hydrophobic helix from sequence inspection. The database annotation supports D, but the input does not provide enough to establish that exact one-residue distinction.


### Important caveats

- The supporting UniProt transmembrane features are computationally annotated (ECO:0000255), not demonstrated here to be experimentally measured.
- Reviewer-only database evidence supports the key but was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has multiple strongly hydrophobic stretches consistent with membrane-spanning helices, including the regions represented in the choices. That supports identifying likely helices, but does not reliably determine every exact endpoint.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific transmembrane annotation, especially the exact boundary at 137 versus 138 and the inclusion of 313..331, is not supplied in the question.",
    "reason": "Choosing the complete set and its precise residue boundaries depends on protein-specific annotation or prediction. General hydropathy reasoning can support the broad regions but cannot robustly distinguish the one-residue boundary difference between B and D."
  },
  "case_id": "transmembrane_0111",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
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
      "C15"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the 455-aa UniProt entry, whose annotated transmembrane segments correspond to choice D. These features carry ECO:0000255, indicating computational annotation rather than direct experimental confirmation."
  },
  "important_caveats": [
    "The supporting UniProt transmembrane features are computationally annotated (ECO:0000255), not demonstrated here to be experimentally measured.",
    "Reviewer-only database evidence supports the key but was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "B and D differ only in whether the fourth segment starts at residue 138 or 137; both are plausible boundaries for a hydrophobic helix from sequence inspection. The database annotation supports D, but the input does not provide enough to establish that exact one-residue distinction."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0111",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the 455-aa UniProt entry, whose annotated transmembrane segments correspond to choice D. These features carry ECO:0000255, indicating computational annotation rather than direct experimental confirmation.",
    "evidence_ids": ["C1", "C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "C14", "C15"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has multiple strongly hydrophobic stretches consistent with membrane-spanning helices, including the regions represented in the choices. That supports identifying likely helices, but does not reliably determine every exact endpoint.",
    "missing_item_specific_fact": "The protein-specific transmembrane annotation, especially the exact boundary at 137 versus 138 and the inclusion of 313..331, is not supplied in the question.",
    "reason": "Choosing the complete set and its precise residue boundaries depends on protein-specific annotation or prediction. General hydropathy reasoning can support the broad regions but cannot robustly distinguish the one-residue boundary difference between B and D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "B and D differ only in whether the fourth segment starts at residue 138 or 137; both are plausible boundaries for a hydrophobic helix from sequence inspection. The database annotation supports D, but the input does not provide enough to establish that exact one-residue distinction."
  },
  "important_caveats": [
    "The supporting UniProt transmembrane features are computationally annotated (ECO:0000255), not demonstrated here to be experimentally measured.",
    "Reviewer-only database evidence supports the key but was not available to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q8IIK1 (Folate transporter 2, PfFT2, Plasmodium falciparum) annotates exactly 11 transmembrane helices at positions 42..64, 84..103, 110..131, 137..157, 177..195, 201..221, 242..261, 281..301, 313..331, 347..367, 417..438, which matches option D precisely. The sequence length (455 AA) and sequence SHA match the supplied sequence. However, all annotations carry evidence code ECO:0000255 (by similarity), meaning they are computational predictions by homology rather than experimentally determined boundaries.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [C13](#evidence-c13), [C14](#evidence-c14), [C15](#evidence-c15), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11), [H12](#evidence-h12), [H13](#evidence-h13).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Option A is eliminable by noting positions exceed the 455-residue protein length. A general hydrophobicity scan can identify the approximate locations of ~10-11 TM segments. However, the critical distinctions among B, C, and D are: (1) B vs D differ by a single-residue boundary (137 vs 138 at the start of the 4th TM helix, where position 137 is Leu and 138 is Ile — both hydrophobic); (2) C vs D differ by inclusion/exclusion of the 313..331 region, which contains mixed hydrophobic (L,I,I,L,V,F,I,Y,I,I,L) and polar/proline residues (T,T,T,S,P,S,P), making it a genuinely borderline segment. No general biological principle definitively resolves a one-residue helix boundary or whether this mixed-composition segment qualifies as TM.


**Missing item-specific fact**

> The exact boundary of the 4th TM helix (whether position 137-L or 138-I is the first residue) and the decision to include the borderline 313-331 segment as a TM helix depend on the specific prediction algorithm (UniProt's homology-based annotation, ECO:0000255). These are annotation-specific outputs not derivable from general hydrophobicity reasoning.


**Reason**

> While a trained biologist could narrow from four options to two or three using hydrophobicity analysis and the known ~11-TM topology of MFS-family transporters, the final discrimination between B and D (single-residue boundary) and between C and D (borderline TM inclusion) requires knowledge of the specific computational annotation rather than general biological reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> Options B and D differ only at the start of the 4th TM helix (138..157 vs 137..157). Position 137 is Leucine (hydrophobic) and position 138 is Isoleucine (hydrophobic). A hydrophobicity-based analysis could reasonably include or exclude either boundary. Option C is also arguably defensible as a 'conservative' prediction that excludes the borderline 313-331 region containing multiple polar/proline residues. Only option A is clearly eliminable.


### Important caveats

- All UniProt TM annotations carry ECO:0000255 (by similarity), indicating computational homology-based predictions rather than experimental structural determination.
- The single-residue boundary difference between B and D (137 vs 138) is within the typical ±1-2 residue uncertainty of TM prediction algorithms and cannot be resolved by reasoning.
- The 313-331 region contains P, S, T, T, T residues interspersed with hydrophobic residues, making its classification as TM algorithm-dependent.
- The UniProt entry was first publicly released 2025-02-05; the historical annotation at entry version 107 (released 2026-01-28) is identical to the current version regarding TM features.
- Option A appears to be a distractor drawn from a different (much longer) protein or contains positions exceeding the 455-residue sequence length.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Option A is eliminable by noting positions exceed the 455-residue protein length. A general hydrophobicity scan can identify the approximate locations of ~10-11 TM segments. However, the critical distinctions among B, C, and D are: (1) B vs D differ by a single-residue boundary (137 vs 138 at the start of the 4th TM helix, where position 137 is Leu and 138 is Ile — both hydrophobic); (2) C vs D differ by inclusion/exclusion of the 313..331 region, which contains mixed hydrophobic (L,I,I,L,V,F,I,Y,I,I,L) and polar/proline residues (T,T,T,S,P,S,P), making it a genuinely borderline segment. No general biological principle definitively resolves a one-residue helix boundary or whether this mixed-composition segment qualifies as TM.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact boundary of the 4th TM helix (whether position 137-L or 138-I is the first residue) and the decision to include the borderline 313-331 segment as a TM helix depend on the specific prediction algorithm (UniProt's homology-based annotation, ECO:0000255). These are annotation-specific outputs not derivable from general hydrophobicity reasoning.",
    "reason": "While a trained biologist could narrow from four options to two or three using hydrophobicity analysis and the known ~11-TM topology of MFS-family transporters, the final discrimination between B and D (single-residue boundary) and between C and D (borderline TM inclusion) requires knowledge of the specific computational annotation rather than general biological reasoning."
  },
  "case_id": "transmembrane_0111",
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
    "reason": "The UniProt entry Q8IIK1 (Folate transporter 2, PfFT2, Plasmodium falciparum) annotates exactly 11 transmembrane helices at positions 42..64, 84..103, 110..131, 137..157, 177..195, 201..221, 242..261, 281..301, 313..331, 347..367, 417..438, which matches option D precisely. The sequence length (455 AA) and sequence SHA match the supplied sequence. However, all annotations carry evidence code ECO:0000255 (by similarity), meaning they are computational predictions by homology rather than experimentally determined boundaries."
  },
  "important_caveats": [
    "All UniProt TM annotations carry ECO:0000255 (by similarity), indicating computational homology-based predictions rather than experimental structural determination.",
    "The single-residue boundary difference between B and D (137 vs 138) is within the typical ±1-2 residue uncertainty of TM prediction algorithms and cannot be resolved by reasoning.",
    "The 313-331 region contains P, S, T, T, T residues interspersed with hydrophobic residues, making its classification as TM algorithm-dependent.",
    "The UniProt entry was first publicly released 2025-02-05; the historical annotation at entry version 107 (released 2026-01-28) is identical to the current version regarding TM features.",
    "Option A appears to be a distractor drawn from a different (much longer) protein or contains positions exceeding the 455-residue sequence length."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "Options B and D differ only at the start of the 4th TM helix (138..157 vs 137..157). Position 137 is Leucine (hydrophobic) and position 138 is Isoleucine (hydrophobic). A hydrophobicity-based analysis could reasonably include or exclude either boundary. Option C is also arguably defensible as a 'conservative' prediction that excludes the borderline 313-331 region containing multiple polar/proline residues. Only option A is clearly eliminable."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0111",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q8IIK1 (Folate transporter 2, PfFT2, Plasmodium falciparum) annotates exactly 11 transmembrane helices at positions 42..64, 84..103, 110..131, 137..157, 177..195, 201..221, 242..261, 281..301, 313..331, 347..367, 417..438, which matches option D precisely. The sequence length (455 AA) and sequence SHA match the supplied sequence. However, all annotations carry evidence code ECO:0000255 (by similarity), meaning they are computational predictions by homology rather than experimentally determined boundaries.",
    "evidence_ids": ["C5","C6","C7","C8","C9","C10","C11","C12","C13","C14","C15","H3","H4","H5","H6","H7","H8","H9","H10","H11","H12","H13"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Option A is eliminable by noting positions exceed the 455-residue protein length. A general hydrophobicity scan can identify the approximate locations of ~10-11 TM segments. However, the critical distinctions among B, C, and D are: (1) B vs D differ by a single-residue boundary (137 vs 138 at the start of the 4th TM helix, where position 137 is Leu and 138 is Ile — both hydrophobic); (2) C vs D differ by inclusion/exclusion of the 313..331 region, which contains mixed hydrophobic (L,I,I,L,V,F,I,Y,I,I,L) and polar/proline residues (T,T,T,S,P,S,P), making it a genuinely borderline segment. No general biological principle definitively resolves a one-residue helix boundary or whether this mixed-composition segment qualifies as TM.",
    "missing_item_specific_fact": "The exact boundary of the 4th TM helix (whether position 137-L or 138-I is the first residue) and the decision to include the borderline 313-331 segment as a TM helix depend on the specific prediction algorithm (UniProt's homology-based annotation, ECO:0000255). These are annotation-specific outputs not derivable from general hydrophobicity reasoning.",
    "reason": "While a trained biologist could narrow from four options to two or three using hydrophobicity analysis and the known ~11-TM topology of MFS-family transporters, the final discrimination between B and D (single-residue boundary) and between C and D (borderline TM inclusion) requires knowledge of the specific computational annotation rather than general biological reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "Options B and D differ only at the start of the 4th TM helix (138..157 vs 137..157). Position 137 is Leucine (hydrophobic) and position 138 is Isoleucine (hydrophobic). A hydrophobicity-based analysis could reasonably include or exclude either boundary. Option C is also arguably defensible as a 'conservative' prediction that excludes the borderline 313-331 region containing multiple polar/proline residues. Only option A is clearly eliminable."
  },
  "important_caveats": [
    "All UniProt TM annotations carry ECO:0000255 (by similarity), indicating computational homology-based predictions rather than experimental structural determination.",
    "The single-residue boundary difference between B and D (137 vs 138) is within the typical ±1-2 residue uncertainty of TM prediction algorithms and cannot be resolved by reasoning.",
    "The 313-331 region contains P, S, T, T, T residues interspersed with hydrophobic residues, making its classification as TM algorithm-dependent.",
    "The UniProt entry was first publicly released 2025-02-05; the historical annotation at entry version 107 (released 2026-01-28) is identical to the current version regarding TM features.",
    "Option A appears to be a distractor drawn from a different (much longer) protein or contains positions exceeding the 455-residue sequence length."
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

**Accession:** `Q8IIK1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 107. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIK1.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:24.989052+00:00.  

```json
"Q8IIK1"
```

Source SHA-256: `8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIK1.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:24.989052+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":64},"start":{"modifier":"EXACT","value":42}},"type":"Transmembrane"}
```

Source SHA-256: `8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIK1.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:24.989052+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":103},"start":{"modifier":"EXACT","value":84}},"type":"Transmembrane"}
```

Source SHA-256: `8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIK1.json)  
**Locator:** `/features/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:24.989052+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":131},"start":{"modifier":"EXACT","value":110}},"type":"Transmembrane"}
```

Source SHA-256: `8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIK1.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:24.989052+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":157},"start":{"modifier":"EXACT","value":137}},"type":"Transmembrane"}
```

Source SHA-256: `8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIK1.json)  
**Locator:** `/features/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:24.989052+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":195},"start":{"modifier":"EXACT","value":177}},"type":"Transmembrane"}
```

Source SHA-256: `8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIK1.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:24.989052+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":221},"start":{"modifier":"EXACT","value":201}},"type":"Transmembrane"}
```

Source SHA-256: `8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940`.

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIK1.json)  
**Locator:** `/features/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:24.989052+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":261},"start":{"modifier":"EXACT","value":242}},"type":"Transmembrane"}
```

Source SHA-256: `8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIK1.json)  
**Locator:** `/features/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:24.989052+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":301},"start":{"modifier":"EXACT","value":281}},"type":"Transmembrane"}
```

Source SHA-256: `8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940`.

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIK1.json)  
**Locator:** `/features/9`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:24.989052+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":331},"start":{"modifier":"EXACT","value":313}},"type":"Transmembrane"}
```

Source SHA-256: `8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940`.

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIK1.json)  
**Locator:** `/features/10`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:24.989052+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":367},"start":{"modifier":"EXACT","value":347}},"type":"Transmembrane"}
```

Source SHA-256: `8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940`.

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIK1.json)  
**Locator:** `/features/11`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:24.989052+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":438},"start":{"modifier":"EXACT","value":417}},"type":"Transmembrane"}
```

Source SHA-256: `8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107)  
**Locator:** `lines 98-100`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 107 / 1.  
**Retrieved:** 2026-11-01T06:28:40.005689+00:00.  

```text
FT   TRANSMEM        42..64
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `c315cecd25012a01e06e0aefb68dd205d1cf053c48966bc36b4c33d3c6385707`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107)  
**Locator:** `lines 101-103`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 107 / 1.  
**Retrieved:** 2026-11-01T06:28:40.005689+00:00.  

```text
FT   TRANSMEM        84..103
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `c315cecd25012a01e06e0aefb68dd205d1cf053c48966bc36b4c33d3c6385707`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107)  
**Locator:** `lines 104-106`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 107 / 1.  
**Retrieved:** 2026-11-01T06:28:40.005689+00:00.  

```text
FT   TRANSMEM        110..131
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `c315cecd25012a01e06e0aefb68dd205d1cf053c48966bc36b4c33d3c6385707`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107)  
**Locator:** `lines 107-109`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 107 / 1.  
**Retrieved:** 2026-11-01T06:28:40.005689+00:00.  

```text
FT   TRANSMEM        137..157
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `c315cecd25012a01e06e0aefb68dd205d1cf053c48966bc36b4c33d3c6385707`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107)  
**Locator:** `lines 110-112`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 107 / 1.  
**Retrieved:** 2026-11-01T06:28:40.005689+00:00.  

```text
FT   TRANSMEM        177..195
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `c315cecd25012a01e06e0aefb68dd205d1cf053c48966bc36b4c33d3c6385707`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107)  
**Locator:** `lines 113-115`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 107 / 1.  
**Retrieved:** 2026-11-01T06:28:40.005689+00:00.  

```text
FT   TRANSMEM        201..221
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `c315cecd25012a01e06e0aefb68dd205d1cf053c48966bc36b4c33d3c6385707`.

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107)  
**Locator:** `lines 116-118`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 107 / 1.  
**Retrieved:** 2026-11-01T06:28:40.005689+00:00.  

```text
FT   TRANSMEM        242..261
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `c315cecd25012a01e06e0aefb68dd205d1cf053c48966bc36b4c33d3c6385707`.

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107)  
**Locator:** `lines 119-121`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 107 / 1.  
**Retrieved:** 2026-11-01T06:28:40.005689+00:00.  

```text
FT   TRANSMEM        281..301
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `c315cecd25012a01e06e0aefb68dd205d1cf053c48966bc36b4c33d3c6385707`.

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107)  
**Locator:** `lines 122-124`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 107 / 1.  
**Retrieved:** 2026-11-01T06:28:40.005689+00:00.  

```text
FT   TRANSMEM        313..331
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `c315cecd25012a01e06e0aefb68dd205d1cf053c48966bc36b4c33d3c6385707`.

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107)  
**Locator:** `lines 125-127`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 107 / 1.  
**Retrieved:** 2026-11-01T06:28:40.005689+00:00.  

```text
FT   TRANSMEM        347..367
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `c315cecd25012a01e06e0aefb68dd205d1cf053c48966bc36b4c33d3c6385707`.

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107)  
**Locator:** `lines 128-130`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 107 / 1.  
**Retrieved:** 2026-11-01T06:28:40.005689+00:00.  

```text
FT   TRANSMEM        417..438
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `c315cecd25012a01e06e0aefb68dd205d1cf053c48966bc36b4c33d3c6385707`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 111. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
