# transmembrane_0033

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **A** — 14..34; 78..98; 114..134; 137..157; 162..182; 193..213; 235..255; 328..348; 380..400; 471..491

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MWSLDPSQKEVLRFAVSCRILTLMLQALFNIIIPDHHADAFSPPRLASSCSVDQLVEGLLGGLSRWDAEHFLFIAEHGYLYEHNFAFFPGFPLALLMGTELLRPLQGLLSQRSCLLVSVALLNFLFSVLAAVTLHDLGCLVLGCPRQAFYAAMLFCLSPANVFLAAGYSEALFAFLTFSAMGQLERGRSWASGLLFALATGVRSNGLVSVGFLLHAQCRGFFSSLVVLNPLKPLFKLMASLCLSVLTVSLPFALFQYYAYTQFCLPGSAHSVPEPLVQLAVDKGYRITGGNEPPWCSWGLPLVYSYIQDVYWNVGFLRYYELRQVPNFLLATPVAVLVVWAAWTYVTTHPWLCLTLGLRRSKDSKKTLEKPHPGFLSPKVFVYLVHAAGLLLFGSLCMHVQVLTRLLCSSTPVVYWFPAHLLQNQEPLLRSVDTVPEKLLEKNSPPGQKAPRNCIMKLLYNWRACSPVTRCILGYFLTYWLLGLLLHCNFLPWT

[Multiple Choices]
A. 14..34; 78..98; 114..134; 137..157; 162..182; 193..213; 235..255; 328..348; 380..400; 471..491
B. 14..34; 78..98; 114..134; 162..182; 193..213; 235..255; 328..348; 380..400; 471..491
C. 41..61
D. 14..34; 78..98; 114..134; 137..157; 158..178; 193..213; 235..255; 328..348; 380..400; 471..491
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

> The sequence matches the cited 494-aa UniProt record, whose transmembrane annotations match Choice A's coordinates. These are computational annotations (ECO:0000255), not direct experimental measurements of each boundary.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C20](#evidence-c20), [C22](#evidence-c22), [C24](#evidence-c24).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains multiple hydrophobic stretches consistent with membrane-spanning helices, which supports a multi-pass membrane protein and disfavors the isolated 41..61 option. But general hydrophobicity does not establish the exact boundaries that distinguish A from D.


**Missing item-specific fact**

> The protein-specific transmembrane assignments and boundary convention, or equivalent predictor results for this sequence, are needed to choose among the near-identical coordinate sets.


**Reason**

> The input supports a broad transmembrane prediction, but the exact placement of helix boundaries—including the 158..161 versus 162..182 distinction—is not reliably determined from general biological reasoning alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> A is supported by the cited annotation. Without a specified annotation source or boundary convention, D's shifted boundary for the neighboring hydrophobic segment is also a plausible prediction; sequence-based boundary estimates can differ by several residues.


### Important caveats

- The supporting coordinate annotations are reviewer-only and were not supplied to the evaluated model.
- The annotation evidence is computational; it supports the database-defined answer, not experimentally established exact boundaries.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple hydrophobic stretches consistent with membrane-spanning helices, which supports a multi-pass membrane protein and disfavors the isolated 41..61 option. But general hydrophobicity does not establish the exact boundaries that distinguish A from D.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific transmembrane assignments and boundary convention, or equivalent predictor results for this sequence, are needed to choose among the near-identical coordinate sets.",
    "reason": "The input supports a broad transmembrane prediction, but the exact placement of helix boundaries—including the 158..161 versus 162..182 distinction—is not reliably determined from general biological reasoning alone."
  },
  "case_id": "transmembrane_0033",
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
      "C22",
      "C24"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the cited 494-aa UniProt record, whose transmembrane annotations match Choice A's coordinates. These are computational annotations (ECO:0000255), not direct experimental measurements of each boundary."
  },
  "important_caveats": [
    "The supporting coordinate annotations are reviewer-only and were not supplied to the evaluated model.",
    "The annotation evidence is computational; it supports the database-defined answer, not experimentally established exact boundaries."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "A is supported by the cited annotation. Without a specified annotation source or boundary convention, D's shifted boundary for the neighboring hydrophobic segment is also a plausible prediction; sequence-based boundary estimates can differ by several residues."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0033",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the cited 494-aa UniProt record, whose transmembrane annotations match Choice A's coordinates. These are computational annotations (ECO:0000255), not direct experimental measurements of each boundary.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "C20", "C22", "C24"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains multiple hydrophobic stretches consistent with membrane-spanning helices, which supports a multi-pass membrane protein and disfavors the isolated 41..61 option. But general hydrophobicity does not establish the exact boundaries that distinguish A from D.",
    "missing_item_specific_fact": "The protein-specific transmembrane assignments and boundary convention, or equivalent predictor results for this sequence, are needed to choose among the near-identical coordinate sets.",
    "reason": "The input supports a broad transmembrane prediction, but the exact placement of helix boundaries—including the 158..161 versus 162..182 distinction—is not reliably determined from general biological reasoning alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "A is supported by the cited annotation. Without a specified annotation source or boundary convention, D's shifted boundary for the neighboring hydrophobic segment is also a plausible prediction; sequence-based boundary estimates can differ by several residues."
  },
  "important_caveats": [
    "The supporting coordinate annotations are reviewer-only and were not supplied to the evaluated model.",
    "The annotation evidence is computational; it supports the database-defined answer, not experimentally established exact boundaries."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProtKB entry A0A8C2M425 (PIGV_CRIGR, Chinese hamster, 494 AA, sequence matched) annotates exactly ten transmembrane helical segments at 14..34, 78..98, 114..134, 137..157, 162..182, 193..213, 235..255, 328..348, 380..400, and 471..491, matching Choice A verbatim. The evidence codes are ECO:0000255 (transmembrane helix by similarity) for the TM segments and ECO:0000250 (similarity to human PIGV Q9NUD9) for the topological domains, so these are computational/similarity-based annotations rather than direct experimental measurements. Nonetheless, they constitute the canonical reference annotation and are consistent with the sequence.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C20](#evidence-c20), [C22](#evidence-c22), [C24](#evidence-c24), [H4](#evidence-h4), [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16), [H18](#evidence-h18), [H20](#evidence-h20), [H22](#evidence-h22).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Choice C (41..61) can be eliminated by noting this region lies in the lumenal loop between TM1 and TM2 and lacks a continuous hydrophobic stretch of ≥18 residues. The A-vs-D distinction (TM start at 162 vs 158) is partially accessible: residues 158-161 (S-P-A-N) include a polar Ser, a helix-breaking Pro, and a polar Asn, making 162 (Val) a more plausible TM helix start than 158. However, the critical A-vs-B distinction—whether 137..157 is a genuine TM helix—cannot be reliably resolved by sequence analysis alone. That 21-residue segment contains Pro145 and charged/polar residues R146 and Q147 in its middle, features strongly unfavorable for a standard α-helical TM segment. A hydrophobicity-based analysis would plausibly exclude this segment, favoring B. The annotation's inclusion of 137..157 as TM (by similarity to human PIGV) is an item-specific fact not derivable from general biological reasoning about the sequence.


**Missing item-specific fact**

> The specific annotation that 137..157 constitutes a transmembrane helix despite containing Pro145 and Arg146/Gln147, established by similarity to human PIGV (Q9NUD9) under evidence code ECO:0000255. Without this annotation, the unusual residue composition in the middle of this segment makes it genuinely ambiguous whether it qualifies as a TM helix.


**Reason**

> Eliminating C and partially distinguishing A from D can be done with general hydrophobicity reasoning. However, the decisive choice between A and B hinges on whether a 21-residue segment with a central Pro and charged residue qualifies as a TM helix—a determination that depends on the specific similarity-based annotation rather than generalizable sequence heuristics. A model performing standard hydropathy analysis would likely exclude 137..157 and select B.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> The segment 137..157 contains Pro145 and Arg146/Gln147, making its classification as a TM helix non-obvious from sequence alone. A defensible hydrophobicity-based analysis could exclude it, yielding B. The question stem says 'a segment that crosses the membrane' (singular) but all substantive choices list multiple segments; this is a minor wording inconsistency that does not create real ambiguity given the answer format.


### Important caveats

- All TM annotations carry evidence code ECO:0000255 (prediction by similarity), not experimental determination. The topological domain assignments are transferred from human PIGV (Q9NUD9) via ECO:0000250.
- The sequence is from Chinese hamster (Cricetulus griseus), not human; the annotation is based on similarity to the human ortholog, so exact boundary positions may differ slightly from experimental data.
- The question asks to identify 'a segment' but expects the full set of all TM regions; the singular/plural mismatch is a minor wording issue.
- The reviewer-only evidence was absent from the evaluated model's input; the model had only the raw 494-aa sequence and the four answer choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Choice C (41..61) can be eliminated by noting this region lies in the lumenal loop between TM1 and TM2 and lacks a continuous hydrophobic stretch of ≥18 residues. The A-vs-D distinction (TM start at 162 vs 158) is partially accessible: residues 158-161 (S-P-A-N) include a polar Ser, a helix-breaking Pro, and a polar Asn, making 162 (Val) a more plausible TM helix start than 158. However, the critical A-vs-B distinction—whether 137..157 is a genuine TM helix—cannot be reliably resolved by sequence analysis alone. That 21-residue segment contains Pro145 and charged/polar residues R146 and Q147 in its middle, features strongly unfavorable for a standard α-helical TM segment. A hydrophobicity-based analysis would plausibly exclude this segment, favoring B. The annotation's inclusion of 137..157 as TM (by similarity to human PIGV) is an item-specific fact not derivable from general biological reasoning about the sequence.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific annotation that 137..157 constitutes a transmembrane helix despite containing Pro145 and Arg146/Gln147, established by similarity to human PIGV (Q9NUD9) under evidence code ECO:0000255. Without this annotation, the unusual residue composition in the middle of this segment makes it genuinely ambiguous whether it qualifies as a TM helix.",
    "reason": "Eliminating C and partially distinguishing A from D can be done with general hydrophobicity reasoning. However, the decisive choice between A and B hinges on whether a 21-residue segment with a central Pro and charged residue qualifies as a TM helix—a determination that depends on the specific similarity-based annotation rather than generalizable sequence heuristics. A model performing standard hydropathy analysis would likely exclude 137..157 and select B."
  },
  "case_id": "transmembrane_0033",
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
      "C22",
      "C24",
      "H4",
      "H6",
      "H8",
      "H10",
      "H12",
      "H14",
      "H16",
      "H18",
      "H20",
      "H22"
    ],
    "judgment": "supported",
    "reason": "UniProtKB entry A0A8C2M425 (PIGV_CRIGR, Chinese hamster, 494 AA, sequence matched) annotates exactly ten transmembrane helical segments at 14..34, 78..98, 114..134, 137..157, 162..182, 193..213, 235..255, 328..348, 380..400, and 471..491, matching Choice A verbatim. The evidence codes are ECO:0000255 (transmembrane helix by similarity) for the TM segments and ECO:0000250 (similarity to human PIGV Q9NUD9) for the topological domains, so these are computational/similarity-based annotations rather than direct experimental measurements. Nonetheless, they constitute the canonical reference annotation and are consistent with the sequence."
  },
  "important_caveats": [
    "All TM annotations carry evidence code ECO:0000255 (prediction by similarity), not experimental determination. The topological domain assignments are transferred from human PIGV (Q9NUD9) via ECO:0000250.",
    "The sequence is from Chinese hamster (Cricetulus griseus), not human; the annotation is based on similarity to the human ortholog, so exact boundary positions may differ slightly from experimental data.",
    "The question asks to identify 'a segment' but expects the full set of all TM regions; the singular/plural mismatch is a minor wording issue.",
    "The reviewer-only evidence was absent from the evaluated model's input; the model had only the raw 494-aa sequence and the four answer choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "The segment 137..157 contains Pro145 and Arg146/Gln147, making its classification as a TM helix non-obvious from sequence alone. A defensible hydrophobicity-based analysis could exclude it, yielding B. The question stem says 'a segment that crosses the membrane' (singular) but all substantive choices list multiple segments; this is a minor wording inconsistency that does not create real ambiguity given the answer format."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0033",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProtKB entry A0A8C2M425 (PIGV_CRIGR, Chinese hamster, 494 AA, sequence matched) annotates exactly ten transmembrane helical segments at 14..34, 78..98, 114..134, 137..157, 162..182, 193..213, 235..255, 328..348, 380..400, and 471..491, matching Choice A verbatim. The evidence codes are ECO:0000255 (transmembrane helix by similarity) for the TM segments and ECO:0000250 (similarity to human PIGV Q9NUD9) for the topological domains, so these are computational/similarity-based annotations rather than direct experimental measurements. Nonetheless, they constitute the canonical reference annotation and are consistent with the sequence.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "C20", "C22", "C24", "H4", "H6", "H8", "H10", "H12", "H14", "H16", "H18", "H20", "H22"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Choice C (41..61) can be eliminated by noting this region lies in the lumenal loop between TM1 and TM2 and lacks a continuous hydrophobic stretch of ≥18 residues. The A-vs-D distinction (TM start at 162 vs 158) is partially accessible: residues 158-161 (S-P-A-N) include a polar Ser, a helix-breaking Pro, and a polar Asn, making 162 (Val) a more plausible TM helix start than 158. However, the critical A-vs-B distinction—whether 137..157 is a genuine TM helix—cannot be reliably resolved by sequence analysis alone. That 21-residue segment contains Pro145 and charged/polar residues R146 and Q147 in its middle, features strongly unfavorable for a standard α-helical TM segment. A hydrophobicity-based analysis would plausibly exclude this segment, favoring B. The annotation's inclusion of 137..157 as TM (by similarity to human PIGV) is an item-specific fact not derivable from general biological reasoning about the sequence.",
    "missing_item_specific_fact": "The specific annotation that 137..157 constitutes a transmembrane helix despite containing Pro145 and Arg146/Gln147, established by similarity to human PIGV (Q9NUD9) under evidence code ECO:0000255. Without this annotation, the unusual residue composition in the middle of this segment makes it genuinely ambiguous whether it qualifies as a TM helix.",
    "reason": "Eliminating C and partially distinguishing A from D can be done with general hydrophobicity reasoning. However, the decisive choice between A and B hinges on whether a 21-residue segment with a central Pro and charged residue qualifies as a TM helix—a determination that depends on the specific similarity-based annotation rather than generalizable sequence heuristics. A model performing standard hydropathy analysis would likely exclude 137..157 and select B."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "The segment 137..157 contains Pro145 and Arg146/Gln147, making its classification as a TM helix non-obvious from sequence alone. A defensible hydrophobicity-based analysis could exclude it, yielding B. The question stem says 'a segment that crosses the membrane' (singular) but all substantive choices list multiple segments; this is a minor wording inconsistency that does not create real ambiguity given the answer format."
  },
  "important_caveats": [
    "All TM annotations carry evidence code ECO:0000255 (prediction by similarity), not experimental determination. The topological domain assignments are transferred from human PIGV (Q9NUD9) via ECO:0000250.",
    "The sequence is from Chinese hamster (Cricetulus griseus), not human; the annotation is based on similarity to the human ortholog, so exact boundary positions may differ slightly from experimental data.",
    "The question asks to identify 'a segment' but expects the full set of all TM regions; the singular/plural mismatch is a minor wording issue.",
    "The reviewer-only evidence was absent from the evaluated model's input; the model had only the raw 494-aa sequence and the four answer choices."
  ]
}
```

</details>

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

### Source check 1

**Check:** `boundary_alternative_not_independently_validated`.

> Cited computational Transmembrane features match keyA including162..182. OptionD replaces that interval with158..178.

**Remaining uncertainty:** The alternative boundary is not annotated by the cited source. Its biological plausibility and the question wording remain separate from the factual annotation match.

Evidence checked: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C20](#evidence-c20), [C22](#evidence-c22), [C24](#evidence-c24).

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `A0A8C2M425` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 19. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:57.236271+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":34},"start":{"modifier":"EXACT","value":14}},"type":"Transmembrane"}
```

Source SHA-256: `4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:57.236271+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":98},"start":{"modifier":"EXACT","value":78}},"type":"Transmembrane"}
```

Source SHA-256: `4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:57.236271+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":134},"start":{"modifier":"EXACT","value":114}},"type":"Transmembrane"}
```

Source SHA-256: `4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)  
**Locator:** `/features/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:57.236271+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":157},"start":{"modifier":"EXACT","value":137}},"type":"Transmembrane"}
```

Source SHA-256: `4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa`.

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)  
**Locator:** `/features/10`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:57.236271+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":182},"start":{"modifier":"EXACT","value":162}},"type":"Transmembrane"}
```

Source SHA-256: `4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa`.

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)  
**Locator:** `/features/12`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:57.236271+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":213},"start":{"modifier":"EXACT","value":193}},"type":"Transmembrane"}
```

Source SHA-256: `4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa`.

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)  
**Locator:** `/features/14`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:57.236271+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":255},"start":{"modifier":"EXACT","value":235}},"type":"Transmembrane"}
```

Source SHA-256: `4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa`.

### Evidence C20

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)  
**Locator:** `/features/16`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:57.236271+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":348},"start":{"modifier":"EXACT","value":328}},"type":"Transmembrane"}
```

Source SHA-256: `4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa`.

### Evidence C22

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)  
**Locator:** `/features/18`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:57.236271+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":400},"start":{"modifier":"EXACT","value":380}},"type":"Transmembrane"}
```

Source SHA-256: `4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa`.

### Evidence C24

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)  
**Locator:** `/features/20`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:57.236271+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":491},"start":{"modifier":"EXACT","value":471}},"type":"Transmembrane"}
```

Source SHA-256: `4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)  
**Locator:** `lines 124-126`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:26:00.136470+00:00.  

```text
FT   TRANSMEM        14..34
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)  
**Locator:** `lines 130-132`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:26:00.136470+00:00.  

```text
FT   TRANSMEM        78..98
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)  
**Locator:** `lines 136-138`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:26:00.136470+00:00.  

```text
FT   TRANSMEM        114..134
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef`.

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)  
**Locator:** `lines 142-144`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:26:00.136470+00:00.  

```text
FT   TRANSMEM        137..157
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef`.

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)  
**Locator:** `lines 148-150`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:26:00.136470+00:00.  

```text
FT   TRANSMEM        162..182
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef`.

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)  
**Locator:** `lines 154-156`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:26:00.136470+00:00.  

```text
FT   TRANSMEM        193..213
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef`.

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)  
**Locator:** `lines 160-162`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:26:00.136470+00:00.  

```text
FT   TRANSMEM        235..255
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef`.

### Evidence H18

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)  
**Locator:** `lines 166-168`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:26:00.136470+00:00.  

```text
FT   TRANSMEM        328..348
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef`.

### Evidence H20

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)  
**Locator:** `lines 172-174`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:26:00.136470+00:00.  

```text
FT   TRANSMEM        380..400
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef`.

### Evidence H22

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)  
**Locator:** `lines 178-180`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:26:00.136470+00:00.  

```text
FT   TRANSMEM        471..491
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 33. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
