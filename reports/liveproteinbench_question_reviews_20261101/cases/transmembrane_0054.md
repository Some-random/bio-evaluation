# transmembrane_0054

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **D** — 17..53; 58..88; 94..129; 138..164; 181..218; 223..258; 269..297

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MASLRGSETMCNITTSCNVDSNIDQFFQPTLYIIVIVLGFPTNCMALWAAYMQVKQKNELGIYLMNLSIADLLYITTLPLWIDYFVHHDNWIHGQVSCKLFGFIFYTNIYVSIAFLCCISVDRYLAVAHPLKFAKVRRVKTALLVSAIVWLTEIVANSAPLFHDELFQDRFNHTFCFEKYPMEPWVAGMNLYRTFLGFLAPWGIMLAAYRGILRAVRGNVSTERQEKAKIKRLALSLILIVLLCFAPYHVLLLWRSVLFLINPCDCGGEENLFGAYHVTLALTSLNCVADPILYCFVNEGARHDVGRALATLLGLFQRGKSPETLMGASITVETPLAVKKPDFYSEVKTNAYKNDIEVLKDECLQMTILSVKK

[Multiple Choices]
A. 17..53; 94..129; 138..164; 181..218; 223..258; 269..297
B. 3..23
C. 17..53; 58..88; 94..129; 135..160; 181..218; 223..258; 269..297
D. 17..53; 58..88; 94..129; 138..164; 181..218; 223..258; 269..297
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

> The supplied sequence matches the historical UniProt sequence, whose annotation lists the seven transmembrane regions exactly as in D. Those annotations cite a publication and cryo-EM structures, providing stronger support than sequence prediction alone.

Citations as saved: [H4](#evidence-h4), [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has several hydrophobic stretches consistent with membrane-spanning helices, including 58–88, which rules against A and B. Around the fourth span, the basic-rich sequence preceding the hydrophobic stretch supports D over C, which extends into that basic region and truncates the span.


**Missing item-specific fact**

> No item-specific fact is necessary for a meaningful sequence-based choice, though an experimental structure or annotation would better establish exact helix boundaries.


**Reason**

> The sequence and choices provide a biological basis for distinguishing D. Exact transmembrane boundaries can be uncertain from sequence alone, but the competing ranges differ in ways that hydrophobicity and the charged loop help resolve.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The endpoints are predictions rather than inherently sharp boundaries, but the sequence features and listed ranges support D as the best choice.


### Important caveats

- The reviewer-only UniProt evidence supports the key but was not supplied to the evaluated model.
- The cited annotation is tied to a matched sequence and cites publication and structural evidence; the exact author-side source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has several hydrophobic stretches consistent with membrane-spanning helices, including 58–88, which rules against A and B. Around the fourth span, the basic-rich sequence preceding the hydrophobic stretch supports D over C, which extends into that basic region and truncates the span.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No item-specific fact is necessary for a meaningful sequence-based choice, though an experimental structure or annotation would better establish exact helix boundaries.",
    "reason": "The sequence and choices provide a biological basis for distinguishing D. Exact transmembrane boundaries can be uncertain from sequence alone, but the competing ranges differ in ways that hydrophobicity and the charged loop help resolve."
  },
  "case_id": "transmembrane_0054",
  "expected_answer_check": {
    "evidence_ids": [
      "H4",
      "H6",
      "H8",
      "H10",
      "H12",
      "H14",
      "H16"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches the historical UniProt sequence, whose annotation lists the seven transmembrane regions exactly as in D. Those annotations cite a publication and cryo-EM structures, providing stronger support than sequence prediction alone."
  },
  "important_caveats": [
    "The reviewer-only UniProt evidence supports the key but was not supplied to the evaluated model.",
    "The cited annotation is tied to a matched sequence and cites publication and structural evidence; the exact author-side source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The endpoints are predictions rather than inherently sharp boundaries, but the sequence features and listed ranges support D as the best choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0054",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches the historical UniProt sequence, whose annotation lists the seven transmembrane regions exactly as in D. Those annotations cite a publication and cryo-EM structures, providing stronger support than sequence prediction alone.",
    "evidence_ids": ["H4", "H6", "H8", "H10", "H12", "H14", "H16"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has several hydrophobic stretches consistent with membrane-spanning helices, including 58–88, which rules against A and B. Around the fourth span, the basic-rich sequence preceding the hydrophobic stretch supports D over C, which extends into that basic region and truncates the span.",
    "missing_item_specific_fact": "No item-specific fact is necessary for a meaningful sequence-based choice, though an experimental structure or annotation would better establish exact helix boundaries.",
    "reason": "The sequence and choices provide a biological basis for distinguishing D. Exact transmembrane boundaries can be uncertain from sequence alone, but the competing ranges differ in ways that hydrophobicity and the charged loop help resolve."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The endpoints are predictions rather than inherently sharp boundaries, but the sequence features and listed ranges support D as the best choice."
  },
  "important_caveats": [
    "The reviewer-only UniProt evidence supports the key but was not supplied to the evaluated model.",
    "The cited annotation is tied to a matched sequence and cites publication and structural evidence; the exact author-side source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry E7FEL0 (Zebrafish GPR4) annotates exactly seven transmembrane helices at positions 17-53, 58-88, 94-129, 138-164, 181-218, 223-258, and 269-297, matching option D precisely. These annotations carry experimental evidence codes (ECO:0000269 from PubMed:39799123 and ECO:0007744 from PDB structures 8ZFZ and 9J31, a 3.05 Å cryo-EM structure of the activated GPR4-Gs complex), constituting structural experimental determination rather than mere computational prediction.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C20](#evidence-c20), [H4](#evidence-h4), [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> General GPCR knowledge (7-TM topology) and the positive-inside rule (favoring K135 and R137 in the cytoplasmic loop rather than within TM4) can eliminate options A (only 6 TM regions) and B (single 21-residue segment), and weakly favor D over C. However, the C-vs-D distinction hinges on a 3-residue boundary (TM4 start at 135 vs 138), where hydrophobicity scores for K(-3.9), V(4.2), R(-4.5) are mixed and a sliding-window predictor could reasonably place the boundary at either position. The positive-inside rule is a statistical tendency (~60-70%), not a hard rule, and R138 itself (the first residue in D's TM4) is also charged, weakening the argument.


**Missing item-specific fact**

> The exact cryo-EM-determined boundary of TM4 (residue 138 vs 135) as resolved in PDB structures 8ZFZ/9J31. No sequence-based hydrophobicity heuristic or general topological rule can definitively resolve a 3-residue boundary difference in a region with mixed hydrophobicity.


**Reason**

> While recognizing 7 TM domains and applying the positive-inside rule narrows choices from four to two, the final C-vs-D discrimination depends on the precise structural annotation from cryo-EM data not derivable from sequence alone. The 3-residue shift in TM4 start is within the uncertainty of any hydrophobicity-based prediction method.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although C and D differ by only 3 residues in TM4 start, the positive-inside rule provides a mild but not definitive preference for D. No other option pair is equally defensible: A omits an obvious 31-residue hydrophobic helix (TM2), and B is a trivially short single segment. The question wording ('correctly identifies the start and end positions') implies a single exact answer, which aligns with the structural annotation.


### Important caveats

- The TM boundaries are from a 2025 cryo-EM structure (Nat. Commun. 16:605), which postdates the benchmark sequence's original 2011 submission. The author's source snapshot is unknown; if constructed before mid-2025, the annotation basis may have been computational (e.g., a TM prediction tool) rather than experimental.
- The reviewer-only UniProt accession (E7FEL0) was inferred from dataset metadata and was not provided to the evaluated model; the model must work from sequence alone.
- The positive-inside rule argument for D over C is suggestive but not conclusive; a model applying rigorous hydrophobicity windowing could plausibly select C.
- The sequence matches the canonical UniProt entry exactly (SHA-256 confirmed), so numbering is unambiguous.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "General GPCR knowledge (7-TM topology) and the positive-inside rule (favoring K135 and R137 in the cytoplasmic loop rather than within TM4) can eliminate options A (only 6 TM regions) and B (single 21-residue segment), and weakly favor D over C. However, the C-vs-D distinction hinges on a 3-residue boundary (TM4 start at 135 vs 138), where hydrophobicity scores for K(-3.9), V(4.2), R(-4.5) are mixed and a sliding-window predictor could reasonably place the boundary at either position. The positive-inside rule is a statistical tendency (~60-70%), not a hard rule, and R138 itself (the first residue in D's TM4) is also charged, weakening the argument.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact cryo-EM-determined boundary of TM4 (residue 138 vs 135) as resolved in PDB structures 8ZFZ/9J31. No sequence-based hydrophobicity heuristic or general topological rule can definitively resolve a 3-residue boundary difference in a region with mixed hydrophobicity.",
    "reason": "While recognizing 7 TM domains and applying the positive-inside rule narrows choices from four to two, the final C-vs-D discrimination depends on the precise structural annotation from cryo-EM data not derivable from sequence alone. The 3-residue shift in TM4 start is within the uncertainty of any hydrophobicity-based prediction method."
  },
  "case_id": "transmembrane_0054",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C8",
      "C10",
      "C12",
      "C14",
      "C16",
      "C18",
      "C20",
      "H4",
      "H6",
      "H8",
      "H10",
      "H12",
      "H14",
      "H16"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry E7FEL0 (Zebrafish GPR4) annotates exactly seven transmembrane helices at positions 17-53, 58-88, 94-129, 138-164, 181-218, 223-258, and 269-297, matching option D precisely. These annotations carry experimental evidence codes (ECO:0000269 from PubMed:39799123 and ECO:0007744 from PDB structures 8ZFZ and 9J31, a 3.05 Å cryo-EM structure of the activated GPR4-Gs complex), constituting structural experimental determination rather than mere computational prediction."
  },
  "important_caveats": [
    "The TM boundaries are from a 2025 cryo-EM structure (Nat. Commun. 16:605), which postdates the benchmark sequence's original 2011 submission. The author's source snapshot is unknown; if constructed before mid-2025, the annotation basis may have been computational (e.g., a TM prediction tool) rather than experimental.",
    "The reviewer-only UniProt accession (E7FEL0) was inferred from dataset metadata and was not provided to the evaluated model; the model must work from sequence alone.",
    "The positive-inside rule argument for D over C is suggestive but not conclusive; a model applying rigorous hydrophobicity windowing could plausibly select C.",
    "The sequence matches the canonical UniProt entry exactly (SHA-256 confirmed), so numbering is unambiguous."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although C and D differ by only 3 residues in TM4 start, the positive-inside rule provides a mild but not definitive preference for D. No other option pair is equally defensible: A omits an obvious 31-residue hydrophobic helix (TM2), and B is a trivially short single segment. The question wording ('correctly identifies the start and end positions') implies a single exact answer, which aligns with the structural annotation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0054",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry E7FEL0 (Zebrafish GPR4) annotates exactly seven transmembrane helices at positions 17-53, 58-88, 94-129, 138-164, 181-218, 223-258, and 269-297, matching option D precisely. These annotations carry experimental evidence codes (ECO:0000269 from PubMed:39799123 and ECO:0007744 from PDB structures 8ZFZ and 9J31, a 3.05 Å cryo-EM structure of the activated GPR4-Gs complex), constituting structural experimental determination rather than mere computational prediction.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "C20", "H4", "H6", "H8", "H10", "H12", "H14", "H16"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "General GPCR knowledge (7-TM topology) and the positive-inside rule (favoring K135 and R137 in the cytoplasmic loop rather than within TM4) can eliminate options A (only 6 TM regions) and B (single 21-residue segment), and weakly favor D over C. However, the C-vs-D distinction hinges on a 3-residue boundary (TM4 start at 135 vs 138), where hydrophobicity scores for K(-3.9), V(4.2), R(-4.5) are mixed and a sliding-window predictor could reasonably place the boundary at either position. The positive-inside rule is a statistical tendency (~60-70%), not a hard rule, and R138 itself (the first residue in D's TM4) is also charged, weakening the argument.",
    "missing_item_specific_fact": "The exact cryo-EM-determined boundary of TM4 (residue 138 vs 135) as resolved in PDB structures 8ZFZ/9J31. No sequence-based hydrophobicity heuristic or general topological rule can definitively resolve a 3-residue boundary difference in a region with mixed hydrophobicity.",
    "reason": "While recognizing 7 TM domains and applying the positive-inside rule narrows choices from four to two, the final C-vs-D discrimination depends on the precise structural annotation from cryo-EM data not derivable from sequence alone. The 3-residue shift in TM4 start is within the uncertainty of any hydrophobicity-based prediction method."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although C and D differ by only 3 residues in TM4 start, the positive-inside rule provides a mild but not definitive preference for D. No other option pair is equally defensible: A omits an obvious 31-residue hydrophobic helix (TM2), and B is a trivially short single segment. The question wording ('correctly identifies the start and end positions') implies a single exact answer, which aligns with the structural annotation."
  },
  "important_caveats": [
    "The TM boundaries are from a 2025 cryo-EM structure (Nat. Commun. 16:605), which postdates the benchmark sequence's original 2011 submission. The author's source snapshot is unknown; if constructed before mid-2025, the annotation basis may have been computational (e.g., a TM prediction tool) rather than experimental.",
    "The reviewer-only UniProt accession (E7FEL0) was inferred from dataset metadata and was not provided to the evaluated model; the model must work from sequence alone.",
    "The positive-inside rule argument for D over C is suggestive but not conclusive; a model applying rigorous hydrophobicity windowing could plausibly select C.",
    "The sequence matches the canonical UniProt entry exactly (SHA-256 confirmed), so numbering is unambiguous."
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

**Accession:** `E7FEL0` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 99. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FEL0.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:01.793515+00:00.  

```json
{"description":"Helical; Name=1","evidences":[{"evidenceCode":"ECO:0000269","id":"39799123","source":"PubMed"},{"evidenceCode":"ECO:0007744","id":"8ZFZ","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"9J31","source":"PDB"}],"location":{"end":{"modifier":"EXACT","value":53},"start":{"modifier":"EXACT","value":17}},"type":"Transmembrane"}
```

Source SHA-256: `36f6ec0f1f41e3c4a3ba2109b2d762f3c0f2e896b891b1172156f642628c0dd4`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FEL0.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:01.793515+00:00.  

```json
{"description":"Helical; Name=2","evidences":[{"evidenceCode":"ECO:0000269","id":"39799123","source":"PubMed"},{"evidenceCode":"ECO:0007744","id":"8ZFZ","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"9J31","source":"PDB"}],"location":{"end":{"modifier":"EXACT","value":88},"start":{"modifier":"EXACT","value":58}},"type":"Transmembrane"}
```

Source SHA-256: `36f6ec0f1f41e3c4a3ba2109b2d762f3c0f2e896b891b1172156f642628c0dd4`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FEL0.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:01.793515+00:00.  

```json
{"description":"Helical; Name=3","evidences":[{"evidenceCode":"ECO:0000269","id":"39799123","source":"PubMed"},{"evidenceCode":"ECO:0007744","id":"8ZFZ","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"9J31","source":"PDB"}],"location":{"end":{"modifier":"EXACT","value":129},"start":{"modifier":"EXACT","value":94}},"type":"Transmembrane"}
```

Source SHA-256: `36f6ec0f1f41e3c4a3ba2109b2d762f3c0f2e896b891b1172156f642628c0dd4`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FEL0.json)  
**Locator:** `/features/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:01.793515+00:00.  

```json
{"description":"Helical; Name=4","evidences":[{"evidenceCode":"ECO:0000269","id":"39799123","source":"PubMed"},{"evidenceCode":"ECO:0007744","id":"8ZFZ","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"9J31","source":"PDB"}],"location":{"end":{"modifier":"EXACT","value":164},"start":{"modifier":"EXACT","value":138}},"type":"Transmembrane"}
```

Source SHA-256: `36f6ec0f1f41e3c4a3ba2109b2d762f3c0f2e896b891b1172156f642628c0dd4`.

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FEL0.json)  
**Locator:** `/features/10`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:01.793515+00:00.  

```json
{"description":"Helical; Name=5","evidences":[{"evidenceCode":"ECO:0000269","id":"39799123","source":"PubMed"},{"evidenceCode":"ECO:0007744","id":"8ZFZ","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"9J31","source":"PDB"}],"location":{"end":{"modifier":"EXACT","value":218},"start":{"modifier":"EXACT","value":181}},"type":"Transmembrane"}
```

Source SHA-256: `36f6ec0f1f41e3c4a3ba2109b2d762f3c0f2e896b891b1172156f642628c0dd4`.

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FEL0.json)  
**Locator:** `/features/12`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:01.793515+00:00.  

```json
{"description":"Helical; Name=6","evidences":[{"evidenceCode":"ECO:0000269","id":"39799123","source":"PubMed"},{"evidenceCode":"ECO:0007744","id":"8ZFZ","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"9J31","source":"PDB"}],"location":{"end":{"modifier":"EXACT","value":258},"start":{"modifier":"EXACT","value":223}},"type":"Transmembrane"}
```

Source SHA-256: `36f6ec0f1f41e3c4a3ba2109b2d762f3c0f2e896b891b1172156f642628c0dd4`.

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FEL0.json)  
**Locator:** `/features/14`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:01.793515+00:00.  

```json
{"description":"Helical; Name=7","evidences":[{"evidenceCode":"ECO:0000269","id":"39799123","source":"PubMed"},{"evidenceCode":"ECO:0007744","id":"8ZFZ","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"9J31","source":"PDB"}],"location":{"end":{"modifier":"EXACT","value":297},"start":{"modifier":"EXACT","value":269}},"type":"Transmembrane"}
```

Source SHA-256: `36f6ec0f1f41e3c4a3ba2109b2d762f3c0f2e896b891b1172156f642628c0dd4`.

### Evidence C20

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FEL0.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:01.793515+00:00.  

```json
{"citation":{"authors":["Ma Y.","Wang Y.","Tang M.","Weng Y.","Chen Y.","Xu Y.","An S.","Wu Y.","Zhao S.","Xu H.","Li D.","Liu M.","Lu W.","Ru H.","Song G."],"citationCrossReferences":[{"database":"PubMed","id":"39799123"},{"database":"DOI","id":"10.1038/s41467-025-55901-2"}],"citationType":"journal article","firstPage":"605","id":"39799123","journal":"Nat. Commun.","lastPage":"605","publicationDate":"2025","title":"Cryo-EM structure of an activated GPR4-Gs signaling complex.","volume":"16"},"evidences":[{"evidenceCode":"ECO:0007744","id":"8ZFZ","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"9J31","source":"PDB"}],"referenceNumber":2,"referencePositions":["STRUCTURE BY ELECTRON MICROSCOPY (3.05 ANGSTROMS) OF 2-360 IN COMPLEX WITH GNAS","FUNCTION","MUTAGENESIS OF GLN-53; ASN-58; GLU-59; ASP-71; HIS-87; ASP-89; TYR-106; TYR-110; ARG-123; ARG-137; 164-ASP-GLU-165; HIS-173; GLU-178; ASN-219; GLU-226; TYR-248; TYR-276; HIS-277; ASP-290 AND GLU-299"]}
```

Source SHA-256: `36f6ec0f1f41e3c4a3ba2109b2d762f3c0f2e896b891b1172156f642628c0dd4`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FEL0?format=txt&versions=99)  
**Locator:** `lines 148-151`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 99 / 1.  
**Retrieved:** 2026-11-02T04:28:05.185174+00:00.  

```text
FT   TRANSMEM        17..53
FT                   /note="Helical; Name=1"
FT                   /evidence="ECO:0000269|PubMed:39799123,
FT                   ECO:0007744|PDB:8ZFZ, ECO:0007744|PDB:9J31"
```

Source SHA-256: `77459f384ab3083be302beb8cb4cd600b88183275fff5fbc110a53c59c8454b1`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FEL0?format=txt&versions=99)  
**Locator:** `lines 156-159`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 99 / 1.  
**Retrieved:** 2026-11-02T04:28:05.185174+00:00.  

```text
FT   TRANSMEM        58..88
FT                   /note="Helical; Name=2"
FT                   /evidence="ECO:0000269|PubMed:39799123,
FT                   ECO:0007744|PDB:8ZFZ, ECO:0007744|PDB:9J31"
```

Source SHA-256: `77459f384ab3083be302beb8cb4cd600b88183275fff5fbc110a53c59c8454b1`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FEL0?format=txt&versions=99)  
**Locator:** `lines 164-167`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 99 / 1.  
**Retrieved:** 2026-11-02T04:28:05.185174+00:00.  

```text
FT   TRANSMEM        94..129
FT                   /note="Helical; Name=3"
FT                   /evidence="ECO:0000269|PubMed:39799123,
FT                   ECO:0007744|PDB:8ZFZ, ECO:0007744|PDB:9J31"
```

Source SHA-256: `77459f384ab3083be302beb8cb4cd600b88183275fff5fbc110a53c59c8454b1`.

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FEL0?format=txt&versions=99)  
**Locator:** `lines 172-175`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 99 / 1.  
**Retrieved:** 2026-11-02T04:28:05.185174+00:00.  

```text
FT   TRANSMEM        138..164
FT                   /note="Helical; Name=4"
FT                   /evidence="ECO:0000269|PubMed:39799123,
FT                   ECO:0007744|PDB:8ZFZ, ECO:0007744|PDB:9J31"
```

Source SHA-256: `77459f384ab3083be302beb8cb4cd600b88183275fff5fbc110a53c59c8454b1`.

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FEL0?format=txt&versions=99)  
**Locator:** `lines 180-183`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 99 / 1.  
**Retrieved:** 2026-11-02T04:28:05.185174+00:00.  

```text
FT   TRANSMEM        181..218
FT                   /note="Helical; Name=5"
FT                   /evidence="ECO:0000269|PubMed:39799123,
FT                   ECO:0007744|PDB:8ZFZ, ECO:0007744|PDB:9J31"
```

Source SHA-256: `77459f384ab3083be302beb8cb4cd600b88183275fff5fbc110a53c59c8454b1`.

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FEL0?format=txt&versions=99)  
**Locator:** `lines 188-191`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 99 / 1.  
**Retrieved:** 2026-11-02T04:28:05.185174+00:00.  

```text
FT   TRANSMEM        223..258
FT                   /note="Helical; Name=6"
FT                   /evidence="ECO:0000269|PubMed:39799123,
FT                   ECO:0007744|PDB:8ZFZ, ECO:0007744|PDB:9J31"
```

Source SHA-256: `77459f384ab3083be302beb8cb4cd600b88183275fff5fbc110a53c59c8454b1`.

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FEL0?format=txt&versions=99)  
**Locator:** `lines 196-199`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 99 / 1.  
**Retrieved:** 2026-11-02T04:28:05.185174+00:00.  

```text
FT   TRANSMEM        269..297
FT                   /note="Helical; Name=7"
FT                   /evidence="ECO:0000269|PubMed:39799123,
FT                   ECO:0007744|PDB:8ZFZ, ECO:0007744|PDB:9J31"
```

Source SHA-256: `77459f384ab3083be302beb8cb4cd600b88183275fff5fbc110a53c59c8454b1`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 54. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
