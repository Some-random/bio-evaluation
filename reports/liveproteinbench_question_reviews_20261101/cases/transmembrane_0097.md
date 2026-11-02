# transmembrane_0097

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **B** — 371..391; 409..429; 444..464; 472..492; 531..551; 564..586; 596..618

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKQNPAKTARMWIIICLLFVLGQATDNDRDFKMCGKWLHGIAPQNLEYDLKTGCERIEISANESTLSIQGRITAKCTQSSSIQLDSNPHQNQSHFCVFWEPLLDLLIVEVNGKNHTLCKPNGLQGTCCTDLSQGVQDNAHMYGIVNGSVKGDIITGDLKGNYIFDGAHINCKEKFCDEARLKPRGANMIEEVVMRFNAKGRVDLPCAQGTVIEMDEEFTGHNFTVPAPRFVDANTIPSVYIPSSLRSVSRRKSKVVCTYYKNKTLFERGPSKSALLDDIVGLSVENETIRNLIEPVKIRFHHRPFAPDSSGRCVSWDTKQDNEVNWKDDGCDTVKINEEQTECHCNHLTYFAILVQVEQKSTVRHLKALTFITAVGCAVSLVSCLVLFYWLCKRRRGKKNQISLVHRGLVVAIFLLCLFFILTGILANVANETVCQLTGSLLHYGLLSTLCWMAMEVFHTFLLVRKVFNSPLPIWIFYLMGFGFPFLLVSILLSVGDIYGERKIKPSDDVNNPYRMCWMTEGDKSQLAHYIINIGLLAVVVSSGLVMLFLVVREIRNRPDWKKIHVAFLSIWGLTCLYGTTWALGFLDFGPFSEVTLFLFCIINSLQGFFLMLRYYALERMKKKDVSSSDGSSSGSSKQHMLQTNEKS

[Multiple Choices]
A. 32..52; 730..750; 795..815; 845..865; 1111..1131
B. 371..391; 409..429; 444..464; 472..492; 531..551; 564..586; 596..618
C. 371..391; 409..429; 472..492; 531..551; 564..586; 596..618
D. 371..391; 409..431; 444..464; 472..492; 531..551; 564..586; 596..618
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

> The sequence matches the historical UniProt record, whose annotations list all seven transmembrane segments in choice B. These are computational annotations (ECO:0000255), not evidence of direct experimental measurement of the boundaries.

Citations as saved: [H5](#evidence-h5), [H7](#evidence-h7), [H9](#evidence-h9), [H11](#evidence-h11), [H13](#evidence-h13), [H15](#evidence-h15), [H17](#evidence-h17).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence's hydrophobic stretches support identifying a multi-pass membrane region and can distinguish it from the clearly mismatched option A, but do not establish the exact boundaries needed to choose between the near-identical options.


**Missing item-specific fact**

> The particular transmembrane boundary annotations for this protein, especially whether the helix is labeled 409..429 or 409..431.


**Reason**

> The input gives a sequence but no boundary convention or protein-specific topology annotation. General hydrophobicity reasoning can locate likely helices, but cannot robustly resolve the precise coordinates that distinguish the remaining choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> B and D list the same regions except that D extends one predicted helix by two residues, 409..431 rather than 409..429. Without a stated boundary convention, both ranges can reasonably describe the same membrane-spanning helix.


### Important caveats

- The supporting annotation applies to the exact supplied sequence, but its evidence code indicates computational annotation rather than direct experimental determination.
- The reviewer-only database evidence supports the key; it was not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence's hydrophobic stretches support identifying a multi-pass membrane region and can distinguish it from the clearly mismatched option A, but do not establish the exact boundaries needed to choose between the near-identical options.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The particular transmembrane boundary annotations for this protein, especially whether the helix is labeled 409..429 or 409..431.",
    "reason": "The input gives a sequence but no boundary convention or protein-specific topology annotation. General hydrophobicity reasoning can locate likely helices, but cannot robustly resolve the precise coordinates that distinguish the remaining choices."
  },
  "case_id": "transmembrane_0097",
  "expected_answer_check": {
    "evidence_ids": [
      "H5",
      "H7",
      "H9",
      "H11",
      "H13",
      "H15",
      "H17"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the historical UniProt record, whose annotations list all seven transmembrane segments in choice B. These are computational annotations (ECO:0000255), not evidence of direct experimental measurement of the boundaries."
  },
  "important_caveats": [
    "The supporting annotation applies to the exact supplied sequence, but its evidence code indicates computational annotation rather than direct experimental determination.",
    "The reviewer-only database evidence supports the key; it was not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "B and D list the same regions except that D extends one predicted helix by two residues, 409..431 rather than 409..429. Without a stated boundary convention, both ranges can reasonably describe the same membrane-spanning helix."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0097",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the historical UniProt record, whose annotations list all seven transmembrane segments in choice B. These are computational annotations (ECO:0000255), not evidence of direct experimental measurement of the boundaries.",
    "evidence_ids": ["H5", "H7", "H9", "H11", "H13", "H15", "H17"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence's hydrophobic stretches support identifying a multi-pass membrane region and can distinguish it from the clearly mismatched option A, but do not establish the exact boundaries needed to choose between the near-identical options.",
    "missing_item_specific_fact": "The particular transmembrane boundary annotations for this protein, especially whether the helix is labeled 409..429 or 409..431.",
    "reason": "The input gives a sequence but no boundary convention or protein-specific topology annotation. General hydrophobicity reasoning can locate likely helices, but cannot robustly resolve the precise coordinates that distinguish the remaining choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "B and D list the same regions except that D extends one predicted helix by two residues, 409..431 rather than 409..429. Without a stated boundary convention, both ranges can reasonably describe the same membrane-spanning helix."
  },
  "important_caveats": [
    "The supporting annotation applies to the exact supplied sequence, but its evidence code indicates computational annotation rather than direct experimental determination.",
    "The reviewer-only database evidence supports the key; it was not provided to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for Q59I63 (Zebrafish ADGRG1/GPR56, sequence matched, 648 AA) lists exactly seven transmembrane helices at 371-391, 409-429, 444-464, 472-492, 531-551, 564-586, and 596-618, matching option B precisely. However, all TM annotations carry evidence code ECO:0000255 (By similarity), indicating computational prediction by similarity to other GPCRs rather than direct experimental determination. The annotation is consistent with the expected answer but is of predicted, not experimentally validated, status.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [H5](#evidence-h5), [H7](#evidence-h7), [H9](#evidence-h9), [H11](#evidence-h11), [H13](#evidence-h13), [H15](#evidence-h15), [H17](#evidence-h17).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> General GPCR biology (seven TM helices in the 7-TM bundle) eliminates option C (only six TMs) and option A (positions 730-1131 exceed the 648-residue protein length). This framework reasoning is sound. However, the critical distinction between B and D is a 2-residue difference in TM2's C-terminal boundary (ends at 429 vs 431). Both 21- and 23-residue helices fall within the normal GPCR TM length range (~19-26 residues). Distinguishing the exact boundary requires either the specific UniProt annotation or a residue-level hydropathy analysis precise enough to classify positions 430-431 as hydrophilic (extracellular loop) versus hydrophobic (TM extension), which is at the limit of reliable sequence-based inference.


**Missing item-specific fact**

> The exact residue identities at positions 430-431 and their hydrophobicity classification, or equivalently the specific database annotation boundary (TM2 = 409-429 vs 409-431), which determines whether the answer is B or D.


**Reason**

> While the 7-TM GPCR architecture and the general location of the TM bundle in the C-terminal ~250 residues are reasoning-accessible, the final B-vs-D discrimination hinges on a 2-residue boundary that is annotation-dependent. A careful hydropathy scan of the provided sequence might in principle resolve it, but the margin is too narrow for confident general-knowledge reasoning, and the correct boundary matches the specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> Options B and D differ only in whether TM2 ends at residue 429 or 431 (a 2-residue shift). Both lengths (21 vs 23 residues) are within the normal range for a GPCR transmembrane helix. Without the specific annotation or a definitive structural/experimental boundary, both boundaries are biologically plausible. The question wording ('correctly identifies the start and end positions') implies a single exact answer, but the 2-residue TM boundary is inherently fuzzy in prediction practice.


### Important caveats

- All seven TM annotations carry ECO:0000255 (By similarity), meaning they are computational predictions transferred from homologous GPCRs, not experimentally determined boundaries.
- The UniProt entry was first publicly released 2025-06-18 (sequence version 2); the author's source snapshot is unknown, but the sequence matches the current and historical (v119) records.
- Option A is trivially eliminable (positions exceed the 648-residue protein length), serving as a very easy distractor.
- Option C is eliminable by the well-known 7-TM GPCR architecture, making the effective discrimination a B-vs-D choice.
- The 2-residue boundary difference between B and D is within the typical uncertainty of TM prediction tools and does not reflect a functionally significant distinction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "General GPCR biology (seven TM helices in the 7-TM bundle) eliminates option C (only six TMs) and option A (positions 730-1131 exceed the 648-residue protein length). This framework reasoning is sound. However, the critical distinction between B and D is a 2-residue difference in TM2's C-terminal boundary (ends at 429 vs 431). Both 21- and 23-residue helices fall within the normal GPCR TM length range (~19-26 residues). Distinguishing the exact boundary requires either the specific UniProt annotation or a residue-level hydropathy analysis precise enough to classify positions 430-431 as hydrophilic (extracellular loop) versus hydrophobic (TM extension), which is at the limit of reliable sequence-based inference.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact residue identities at positions 430-431 and their hydrophobicity classification, or equivalently the specific database annotation boundary (TM2 = 409-429 vs 409-431), which determines whether the answer is B or D.",
    "reason": "While the 7-TM GPCR architecture and the general location of the TM bundle in the C-terminal ~250 residues are reasoning-accessible, the final B-vs-D discrimination hinges on a 2-residue boundary that is annotation-dependent. A careful hydropathy scan of the provided sequence might in principle resolve it, but the margin is too narrow for confident general-knowledge reasoning, and the correct boundary matches the specific UniProt entry."
  },
  "case_id": "transmembrane_0097",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C8",
      "C10",
      "C12",
      "C14",
      "C16",
      "C18",
      "H5",
      "H7",
      "H9",
      "H11",
      "H13",
      "H15",
      "H17"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for Q59I63 (Zebrafish ADGRG1/GPR56, sequence matched, 648 AA) lists exactly seven transmembrane helices at 371-391, 409-429, 444-464, 472-492, 531-551, 564-586, and 596-618, matching option B precisely. However, all TM annotations carry evidence code ECO:0000255 (By similarity), indicating computational prediction by similarity to other GPCRs rather than direct experimental determination. The annotation is consistent with the expected answer but is of predicted, not experimentally validated, status."
  },
  "important_caveats": [
    "All seven TM annotations carry ECO:0000255 (By similarity), meaning they are computational predictions transferred from homologous GPCRs, not experimentally determined boundaries.",
    "The UniProt entry was first publicly released 2025-06-18 (sequence version 2); the author's source snapshot is unknown, but the sequence matches the current and historical (v119) records.",
    "Option A is trivially eliminable (positions exceed the 648-residue protein length), serving as a very easy distractor.",
    "Option C is eliminable by the well-known 7-TM GPCR architecture, making the effective discrimination a B-vs-D choice.",
    "The 2-residue boundary difference between B and D is within the typical uncertainty of TM prediction tools and does not reflect a functionally significant distinction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "Options B and D differ only in whether TM2 ends at residue 429 or 431 (a 2-residue shift). Both lengths (21 vs 23 residues) are within the normal range for a GPCR transmembrane helix. Without the specific annotation or a definitive structural/experimental boundary, both boundaries are biologically plausible. The question wording ('correctly identifies the start and end positions') implies a single exact answer, but the 2-residue TM boundary is inherently fuzzy in prediction practice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0097",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for Q59I63 (Zebrafish ADGRG1/GPR56, sequence matched, 648 AA) lists exactly seven transmembrane helices at 371-391, 409-429, 444-464, 472-492, 531-551, 564-586, and 596-618, matching option B precisely. However, all TM annotations carry evidence code ECO:0000255 (By similarity), indicating computational prediction by similarity to other GPCRs rather than direct experimental determination. The annotation is consistent with the expected answer but is of predicted, not experimentally validated, status.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "H5", "H7", "H9", "H11", "H13", "H15", "H17"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "General GPCR biology (seven TM helices in the 7-TM bundle) eliminates option C (only six TMs) and option A (positions 730-1131 exceed the 648-residue protein length). This framework reasoning is sound. However, the critical distinction between B and D is a 2-residue difference in TM2's C-terminal boundary (ends at 429 vs 431). Both 21- and 23-residue helices fall within the normal GPCR TM length range (~19-26 residues). Distinguishing the exact boundary requires either the specific UniProt annotation or a residue-level hydropathy analysis precise enough to classify positions 430-431 as hydrophilic (extracellular loop) versus hydrophobic (TM extension), which is at the limit of reliable sequence-based inference.",
    "missing_item_specific_fact": "The exact residue identities at positions 430-431 and their hydrophobicity classification, or equivalently the specific database annotation boundary (TM2 = 409-429 vs 409-431), which determines whether the answer is B or D.",
    "reason": "While the 7-TM GPCR architecture and the general location of the TM bundle in the C-terminal ~250 residues are reasoning-accessible, the final B-vs-D discrimination hinges on a 2-residue boundary that is annotation-dependent. A careful hydropathy scan of the provided sequence might in principle resolve it, but the margin is too narrow for confident general-knowledge reasoning, and the correct boundary matches the specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "Options B and D differ only in whether TM2 ends at residue 429 or 431 (a 2-residue shift). Both lengths (21 vs 23 residues) are within the normal range for a GPCR transmembrane helix. Without the specific annotation or a definitive structural/experimental boundary, both boundaries are biologically plausible. The question wording ('correctly identifies the start and end positions') implies a single exact answer, but the 2-residue TM boundary is inherently fuzzy in prediction practice."
  },
  "important_caveats": [
    "All seven TM annotations carry ECO:0000255 (By similarity), meaning they are computational predictions transferred from homologous GPCRs, not experimentally determined boundaries.",
    "The UniProt entry was first publicly released 2025-06-18 (sequence version 2); the author's source snapshot is unknown, but the sequence matches the current and historical (v119) records.",
    "Option A is trivially eliminable (positions exceed the 648-residue protein length), serving as a very easy distractor.",
    "Option C is eliminable by the well-known 7-TM GPCR architecture, making the effective discrimination a B-vs-D choice.",
    "The 2-residue boundary difference between B and D is within the typical uncertainty of TM prediction tools and does not reflect a functionally significant distinction."
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

**Accession:** `Q59I63` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 119. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)  
**Locator:** `/features/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:01.992326+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":391},"start":{"modifier":"EXACT","value":371}},"type":"Transmembrane"}
```

Source SHA-256: `a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)  
**Locator:** `/features/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:01.992326+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":429},"start":{"modifier":"EXACT","value":409}},"type":"Transmembrane"}
```

Source SHA-256: `a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)  
**Locator:** `/features/9`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:01.992326+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":464},"start":{"modifier":"EXACT","value":444}},"type":"Transmembrane"}
```

Source SHA-256: `a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)  
**Locator:** `/features/11`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:01.992326+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":492},"start":{"modifier":"EXACT","value":472}},"type":"Transmembrane"}
```

Source SHA-256: `a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe`.

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)  
**Locator:** `/features/13`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:01.992326+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":551},"start":{"modifier":"EXACT","value":531}},"type":"Transmembrane"}
```

Source SHA-256: `a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe`.

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)  
**Locator:** `/features/15`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:01.992326+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":586},"start":{"modifier":"EXACT","value":564}},"type":"Transmembrane"}
```

Source SHA-256: `a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe`.

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)  
**Locator:** `/features/17`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:01.992326+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":618},"start":{"modifier":"EXACT","value":596}},"type":"Transmembrane"}
```

Source SHA-256: `a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)  
**Locator:** `lines 214-216`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 119 / 2.  
**Retrieved:** 2026-11-02T04:31:04.584714+00:00.  

```text
FT   TRANSMEM        371..391
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)  
**Locator:** `lines 220-222`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 119 / 2.  
**Retrieved:** 2026-11-02T04:31:04.584714+00:00.  

```text
FT   TRANSMEM        409..429
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0`.

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)  
**Locator:** `lines 226-228`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 119 / 2.  
**Retrieved:** 2026-11-02T04:31:04.584714+00:00.  

```text
FT   TRANSMEM        444..464
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0`.

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)  
**Locator:** `lines 232-234`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 119 / 2.  
**Retrieved:** 2026-11-02T04:31:04.584714+00:00.  

```text
FT   TRANSMEM        472..492
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0`.

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)  
**Locator:** `lines 238-240`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 119 / 2.  
**Retrieved:** 2026-11-02T04:31:04.584714+00:00.  

```text
FT   TRANSMEM        531..551
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0`.

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)  
**Locator:** `lines 244-246`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 119 / 2.  
**Retrieved:** 2026-11-02T04:31:04.584714+00:00.  

```text
FT   TRANSMEM        564..586
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0`.

### Evidence H17

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)  
**Locator:** `lines 250-252`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 119 / 2.  
**Retrieved:** 2026-11-02T04:31:04.584714+00:00.  

```text
FT   TRANSMEM        596..618
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 97. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
