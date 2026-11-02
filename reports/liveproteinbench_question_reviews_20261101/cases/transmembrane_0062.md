# transmembrane_0062

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **A** — 27..47; 78..98; 108..128; 136..156; 173..193; 209..229; 337..357; 366..386; 400..420; 432..452; 465..485

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSSHTSTPNHASAAPPRKWYDMTSAEFYVYVVAFMCGISMLMPINAVFSAPSYMLQYYLYATKDPNHVPQMTNFWSNVMTYYNLIGLVTGLVMEPLTLLKSFRKIPMLVRLLGGLCILIVEIIVLMAVPARGTTEGGAVATMCIAGFIGGLGKSIFESTVYGMFGAFPPSFTSIMMGGVGISGVLTSLIQIIVKAALPDTYEGVKKQSYIYYSLDVGIQAATFIALIMMRFNSFAQLHFGDLGGVKSKVDAGSLAGAGENVREPGAEATELEQYTEPAIGQIQEKNAEAHKDDPLVDREHSDDVDEHGDALRAVEGPTSNEILRATSIISVLRSIKWMFVSCAFVFVVTLFLFPGIATGMFPESKWFATVAVFIFNCCDVLGRVAPALRFMWPRSYNQRWIIVAASFARVIFVPLLLLYSYHYIPSEAYGYVIMVIFGFSSGYVASMSLTLGPQSKGIDNDGKRFVAGTLMGISILVGGTIGTVLSIMTQTIREKY

[Multiple Choices]
A. 27..47; 78..98; 108..128; 136..156; 173..193; 209..229; 337..357; 366..386; 400..420; 432..452; 465..485
B. 93..113; 163..183; 382..402; 425..445; 764..784
C. 27..47; 78..98; 108..128; 136..156; 173..193; 209..229; 337..357; 400..420; 432..452; 465..485
D. 27..47; 78..98; 108..128; 136..156; 173..193; 209..229; 337..357; 366..386; 400..420; 436..447; 465..485
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

> The sequence matches the cited UniProt record, whose annotated transmembrane intervals correspond exactly to Choice A. The helix features carry computational evidence code ECO:0000255, so this supports the key as an annotation-based prediction, not as direct experimental mapping of membrane boundaries.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C20](#evidence-c20), [C22](#evidence-c22), [C24](#evidence-c24), [C26](#evidence-c26).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has many strongly hydrophobic stretches, consistent with a multipass membrane protein, so general sequence reasoning can identify likely transmembrane helices in broad terms.


**Missing item-specific fact**

> Selecting the exact listed intervals requires protein-specific transmembrane boundary annotations or equivalent detailed topology predictions; generic hydropathy reasoning does not reliably distinguish the precise endpoints in these choices.


**Reason**

> The input provides sequence but no protein identity, topology annotation, or experimental boundary data. The near-identical choices differ in specific helix inclusion or endpoint placement, which is an item-specific fact rather than a conclusion established by general biological reasoning alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Under the supplied annotation coordinates, only Choice A lists all the annotated transmembrane intervals. Actual membrane boundaries can be less exact than annotation coordinates, but the choices do not establish another full set of equivalent intervals.


### Important caveats

- The supporting UniProt annotations are reviewer-only and were not available in the question input.
- The transmembrane annotations are computationally supported rather than shown here to be experimentally measured; the author’s original source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has many strongly hydrophobic stretches, consistent with a multipass membrane protein, so general sequence reasoning can identify likely transmembrane helices in broad terms.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Selecting the exact listed intervals requires protein-specific transmembrane boundary annotations or equivalent detailed topology predictions; generic hydropathy reasoning does not reliably distinguish the precise endpoints in these choices.",
    "reason": "The input provides sequence but no protein identity, topology annotation, or experimental boundary data. The near-identical choices differ in specific helix inclusion or endpoint placement, which is an item-specific fact rather than a conclusion established by general biological reasoning alone."
  },
  "case_id": "transmembrane_0062",
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
      "C26"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the cited UniProt record, whose annotated transmembrane intervals correspond exactly to Choice A. The helix features carry computational evidence code ECO:0000255, so this supports the key as an annotation-based prediction, not as direct experimental mapping of membrane boundaries."
  },
  "important_caveats": [
    "The supporting UniProt annotations are reviewer-only and were not available in the question input.",
    "The transmembrane annotations are computationally supported rather than shown here to be experimentally measured; the author’s original source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Under the supplied annotation coordinates, only Choice A lists all the annotated transmembrane intervals. Actual membrane boundaries can be less exact than annotation coordinates, but the choices do not establish another full set of equivalent intervals."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0062",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the cited UniProt record, whose annotated transmembrane intervals correspond exactly to Choice A. The helix features carry computational evidence code ECO:0000255, so this supports the key as an annotation-based prediction, not as direct experimental mapping of membrane boundaries.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "C20", "C22", "C24", "C26"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has many strongly hydrophobic stretches, consistent with a multipass membrane protein, so general sequence reasoning can identify likely transmembrane helices in broad terms.",
    "missing_item_specific_fact": "Selecting the exact listed intervals requires protein-specific transmembrane boundary annotations or equivalent detailed topology predictions; generic hydropathy reasoning does not reliably distinguish the precise endpoints in these choices.",
    "reason": "The input provides sequence but no protein identity, topology annotation, or experimental boundary data. The near-identical choices differ in specific helix inclusion or endpoint placement, which is an item-specific fact rather than a conclusion established by general biological reasoning alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Under the supplied annotation coordinates, only Choice A lists all the annotated transmembrane intervals. Actual membrane boundaries can be less exact than annotation coordinates, but the choices do not establish another full set of equivalent intervals."
  },
  "important_caveats": [
    "The supporting UniProt annotations are reviewer-only and were not available in the question input.",
    "The transmembrane annotations are computationally supported rather than shown here to be experimentally measured; the author’s original source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry J9UD11 (Adenosine transporter 1, CfAT1, from Crithidia fasciculata) annotates exactly 11 transmembrane helical regions at 27..47, 78..98, 108..128, 136..156, 173..193, 209..229, 337..357, 366..386, 400..420, 432..452, and 465..485, matching Choice A precisely. The evidence code ECO:0000255 indicates these are computational predictions by similarity, not experimentally determined boundaries, but the annotation is consistent and the sequence match is confirmed (SHA256 identical).

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C20](#evidence-c20), [C22](#evidence-c22), [C24](#evidence-c24), [C26](#evidence-c26), [H4](#evidence-h4), [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16), [H18](#evidence-h18), [H20](#evidence-h20), [H22](#evidence-h22), [H24](#evidence-h24).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Three independent biological arguments distinguish A from the distractors: (1) Equilibrative nucleoside transporters (ENT family) are well-established to possess 11 transmembrane domains; this eliminates B (only 5 TM regions) and C (only 10 TM regions). (2) Choice B includes region 764..784, which exceeds the 496-residue protein length, making it physically impossible. (3) Choice D replaces the 432..452 segment (21 residues) with 436..447 (12 residues); a 12-residue hydrophobic stretch is too short to span a ~30 Å lipid bilayer as an alpha-helix (which requires approximately 19–25 hydrophobic residues), eliminating D on basic membrane-biophysics grounds.


**Missing item-specific fact**

> None that is strictly required. The ENT 11-TM topology is general family-level knowledge, and the minimum TM-helix length is basic membrane biology. Exact boundary assignment at the residue level is algorithm-dependent, but the multiple-choice format allows elimination by the length argument.


**Reason**

> The question can be answered by combining general knowledge of ENT family topology (11 TMs), a sanity check against protein length, and the biophysical requirement that a TM helix needs ~20 hydrophobic residues. These are general biological arguments, not item-specific database lookups.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> B is eliminated by exceeding protein length and by having only 5 TMs. C is eliminated by having only 10 TMs (inconsistent with ENT topology). D is eliminated by containing a 12-residue segment too short for a TM helix. Only A satisfies all biological constraints simultaneously.


### Important caveats

- All 11 TM annotations carry evidence code ECO:0000255 (by similarity), meaning they are computational predictions transferred from a homolog, not experimentally validated boundaries. Exact residue-level boundaries are inherently approximate.
- The distinction between A and D (432..452 vs 436..447) relies on a minimum-length argument; a model performing a simple hydrophobicity scan might not cleanly resolve a 4-residue boundary shift without careful analysis.
- The protein is from Crithidia fasciculata, a trypanosomatid; its membrane composition and hydrophobicity thresholds may differ slightly from mammalian references, though this does not affect the qualitative 11-TM topology argument.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Three independent biological arguments distinguish A from the distractors: (1) Equilibrative nucleoside transporters (ENT family) are well-established to possess 11 transmembrane domains; this eliminates B (only 5 TM regions) and C (only 10 TM regions). (2) Choice B includes region 764..784, which exceeds the 496-residue protein length, making it physically impossible. (3) Choice D replaces the 432..452 segment (21 residues) with 436..447 (12 residues); a 12-residue hydrophobic stretch is too short to span a ~30 Å lipid bilayer as an alpha-helix (which requires approximately 19–25 hydrophobic residues), eliminating D on basic membrane-biophysics grounds.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None that is strictly required. The ENT 11-TM topology is general family-level knowledge, and the minimum TM-helix length is basic membrane biology. Exact boundary assignment at the residue level is algorithm-dependent, but the multiple-choice format allows elimination by the length argument.",
    "reason": "The question can be answered by combining general knowledge of ENT family topology (11 TMs), a sanity check against protein length, and the biophysical requirement that a TM helix needs ~20 hydrophobic residues. These are general biological arguments, not item-specific database lookups."
  },
  "case_id": "transmembrane_0062",
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
      "C26",
      "H4",
      "H6",
      "H8",
      "H10",
      "H12",
      "H14",
      "H16",
      "H18",
      "H20",
      "H22",
      "H24"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry J9UD11 (Adenosine transporter 1, CfAT1, from Crithidia fasciculata) annotates exactly 11 transmembrane helical regions at 27..47, 78..98, 108..128, 136..156, 173..193, 209..229, 337..357, 366..386, 400..420, 432..452, and 465..485, matching Choice A precisely. The evidence code ECO:0000255 indicates these are computational predictions by similarity, not experimentally determined boundaries, but the annotation is consistent and the sequence match is confirmed (SHA256 identical)."
  },
  "important_caveats": [
    "All 11 TM annotations carry evidence code ECO:0000255 (by similarity), meaning they are computational predictions transferred from a homolog, not experimentally validated boundaries. Exact residue-level boundaries are inherently approximate.",
    "The distinction between A and D (432..452 vs 436..447) relies on a minimum-length argument; a model performing a simple hydrophobicity scan might not cleanly resolve a 4-residue boundary shift without careful analysis.",
    "The protein is from Crithidia fasciculata, a trypanosomatid; its membrane composition and hydrophobicity thresholds may differ slightly from mammalian references, though this does not affect the qualitative 11-TM topology argument."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B is eliminated by exceeding protein length and by having only 5 TMs. C is eliminated by having only 10 TMs (inconsistent with ENT topology). D is eliminated by containing a 12-residue segment too short for a TM helix. Only A satisfies all biological constraints simultaneously."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0062",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry J9UD11 (Adenosine transporter 1, CfAT1, from Crithidia fasciculata) annotates exactly 11 transmembrane helical regions at 27..47, 78..98, 108..128, 136..156, 173..193, 209..229, 337..357, 366..386, 400..420, 432..452, and 465..485, matching Choice A precisely. The evidence code ECO:0000255 indicates these are computational predictions by similarity, not experimentally determined boundaries, but the annotation is consistent and the sequence match is confirmed (SHA256 identical).",
    "evidence_ids": ["C6","C8","C10","C12","C14","C16","C18","C20","C22","C24","C26","H4","H6","H8","H10","H12","H14","H16","H18","H20","H22","H24"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Three independent biological arguments distinguish A from the distractors: (1) Equilibrative nucleoside transporters (ENT family) are well-established to possess 11 transmembrane domains; this eliminates B (only 5 TM regions) and C (only 10 TM regions). (2) Choice B includes region 764..784, which exceeds the 496-residue protein length, making it physically impossible. (3) Choice D replaces the 432..452 segment (21 residues) with 436..447 (12 residues); a 12-residue hydrophobic stretch is too short to span a ~30 Å lipid bilayer as an alpha-helix (which requires approximately 19–25 hydrophobic residues), eliminating D on basic membrane-biophysics grounds.",
    "missing_item_specific_fact": "None that is strictly required. The ENT 11-TM topology is general family-level knowledge, and the minimum TM-helix length is basic membrane biology. Exact boundary assignment at the residue level is algorithm-dependent, but the multiple-choice format allows elimination by the length argument.",
    "reason": "The question can be answered by combining general knowledge of ENT family topology (11 TMs), a sanity check against protein length, and the biophysical requirement that a TM helix needs ~20 hydrophobic residues. These are general biological arguments, not item-specific database lookups."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B is eliminated by exceeding protein length and by having only 5 TMs. C is eliminated by having only 10 TMs (inconsistent with ENT topology). D is eliminated by containing a 12-residue segment too short for a TM helix. Only A satisfies all biological constraints simultaneously."
  },
  "important_caveats": [
    "All 11 TM annotations carry evidence code ECO:0000255 (by similarity), meaning they are computational predictions transferred from a homolog, not experimentally validated boundaries. Exact residue-level boundaries are inherently approximate.",
    "The distinction between A and D (432..452 vs 436..447) relies on a minimum-length argument; a model performing a simple hydrophobicity scan might not cleanly resolve a 4-residue boundary shift without careful analysis.",
    "The protein is from Crithidia fasciculata, a trypanosomatid; its membrane composition and hydrophobicity thresholds may differ slightly from mammalian references, though this does not affect the qualitative 11-TM topology argument."
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

**Accession:** `J9UD11` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 26. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9UD11.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:53.178363+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":47},"start":{"modifier":"EXACT","value":27}},"type":"Transmembrane"}
```

Source SHA-256: `b8a834408fc72a31b2ce6a3190a6f2a1e7030d828c3ec7442331408414d4777c`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9UD11.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:53.178363+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":98},"start":{"modifier":"EXACT","value":78}},"type":"Transmembrane"}
```

Source SHA-256: `b8a834408fc72a31b2ce6a3190a6f2a1e7030d828c3ec7442331408414d4777c`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9UD11.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:53.178363+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":128},"start":{"modifier":"EXACT","value":108}},"type":"Transmembrane"}
```

Source SHA-256: `b8a834408fc72a31b2ce6a3190a6f2a1e7030d828c3ec7442331408414d4777c`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9UD11.json)  
**Locator:** `/features/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:53.178363+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":156},"start":{"modifier":"EXACT","value":136}},"type":"Transmembrane"}
```

Source SHA-256: `b8a834408fc72a31b2ce6a3190a6f2a1e7030d828c3ec7442331408414d4777c`.

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9UD11.json)  
**Locator:** `/features/10`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:53.178363+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":193},"start":{"modifier":"EXACT","value":173}},"type":"Transmembrane"}
```

Source SHA-256: `b8a834408fc72a31b2ce6a3190a6f2a1e7030d828c3ec7442331408414d4777c`.

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9UD11.json)  
**Locator:** `/features/12`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:53.178363+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":229},"start":{"modifier":"EXACT","value":209}},"type":"Transmembrane"}
```

Source SHA-256: `b8a834408fc72a31b2ce6a3190a6f2a1e7030d828c3ec7442331408414d4777c`.

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9UD11.json)  
**Locator:** `/features/14`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:53.178363+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":357},"start":{"modifier":"EXACT","value":337}},"type":"Transmembrane"}
```

Source SHA-256: `b8a834408fc72a31b2ce6a3190a6f2a1e7030d828c3ec7442331408414d4777c`.

### Evidence C20

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9UD11.json)  
**Locator:** `/features/16`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:53.178363+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":386},"start":{"modifier":"EXACT","value":366}},"type":"Transmembrane"}
```

Source SHA-256: `b8a834408fc72a31b2ce6a3190a6f2a1e7030d828c3ec7442331408414d4777c`.

### Evidence C22

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9UD11.json)  
**Locator:** `/features/18`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:53.178363+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":420},"start":{"modifier":"EXACT","value":400}},"type":"Transmembrane"}
```

Source SHA-256: `b8a834408fc72a31b2ce6a3190a6f2a1e7030d828c3ec7442331408414d4777c`.

### Evidence C24

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9UD11.json)  
**Locator:** `/features/20`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:53.178363+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":452},"start":{"modifier":"EXACT","value":432}},"type":"Transmembrane"}
```

Source SHA-256: `b8a834408fc72a31b2ce6a3190a6f2a1e7030d828c3ec7442331408414d4777c`.

### Evidence C26

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9UD11.json)  
**Locator:** `/features/22`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:53.178363+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":485},"start":{"modifier":"EXACT","value":465}},"type":"Transmembrane"}
```

Source SHA-256: `b8a834408fc72a31b2ce6a3190a6f2a1e7030d828c3ec7442331408414d4777c`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26)  
**Locator:** `lines 63-65`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 1.  
**Retrieved:** 2026-11-02T04:28:56.181587+00:00.  

```text
FT   TRANSMEM        27..47
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `52f5c9978ed3814d8396e7feee320cd18c812e512a57459050eeb591ed24b7a6`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26)  
**Locator:** `lines 69-71`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 1.  
**Retrieved:** 2026-11-02T04:28:56.181587+00:00.  

```text
FT   TRANSMEM        78..98
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `52f5c9978ed3814d8396e7feee320cd18c812e512a57459050eeb591ed24b7a6`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26)  
**Locator:** `lines 75-77`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 1.  
**Retrieved:** 2026-11-02T04:28:56.181587+00:00.  

```text
FT   TRANSMEM        108..128
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `52f5c9978ed3814d8396e7feee320cd18c812e512a57459050eeb591ed24b7a6`.

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26)  
**Locator:** `lines 81-83`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 1.  
**Retrieved:** 2026-11-02T04:28:56.181587+00:00.  

```text
FT   TRANSMEM        136..156
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `52f5c9978ed3814d8396e7feee320cd18c812e512a57459050eeb591ed24b7a6`.

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26)  
**Locator:** `lines 87-89`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 1.  
**Retrieved:** 2026-11-02T04:28:56.181587+00:00.  

```text
FT   TRANSMEM        173..193
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `52f5c9978ed3814d8396e7feee320cd18c812e512a57459050eeb591ed24b7a6`.

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26)  
**Locator:** `lines 93-95`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 1.  
**Retrieved:** 2026-11-02T04:28:56.181587+00:00.  

```text
FT   TRANSMEM        209..229
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `52f5c9978ed3814d8396e7feee320cd18c812e512a57459050eeb591ed24b7a6`.

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26)  
**Locator:** `lines 99-101`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 1.  
**Retrieved:** 2026-11-02T04:28:56.181587+00:00.  

```text
FT   TRANSMEM        337..357
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `52f5c9978ed3814d8396e7feee320cd18c812e512a57459050eeb591ed24b7a6`.

### Evidence H18

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26)  
**Locator:** `lines 105-107`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 1.  
**Retrieved:** 2026-11-02T04:28:56.181587+00:00.  

```text
FT   TRANSMEM        366..386
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `52f5c9978ed3814d8396e7feee320cd18c812e512a57459050eeb591ed24b7a6`.

### Evidence H20

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26)  
**Locator:** `lines 111-113`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 1.  
**Retrieved:** 2026-11-02T04:28:56.181587+00:00.  

```text
FT   TRANSMEM        400..420
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `52f5c9978ed3814d8396e7feee320cd18c812e512a57459050eeb591ed24b7a6`.

### Evidence H22

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26)  
**Locator:** `lines 117-119`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 1.  
**Retrieved:** 2026-11-02T04:28:56.181587+00:00.  

```text
FT   TRANSMEM        432..452
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `52f5c9978ed3814d8396e7feee320cd18c812e512a57459050eeb591ed24b7a6`.

### Evidence H24

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26)  
**Locator:** `lines 123-125`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 1.  
**Retrieved:** 2026-11-02T04:28:56.181587+00:00.  

```text
FT   TRANSMEM        465..485
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `52f5c9978ed3814d8396e7feee320cd18c812e512a57459050eeb591ed24b7a6`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 62. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
