# transmembrane_0034

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **D** — 47..71; 139..171; 196..220; 421..450; 466..495; 500..536; 560..592; 613..631; 635..659; 667..695; 701..721

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MLPYVIATLGSAGSTCKASTCSNSTKDYCYSARIRSTVLQGLPFGGVPTVLALDFMCFLALLFVFSILRKVAWDYGRLALVTDADSIASALHSDNHDRYERLTSVSSSVDFDQRDNGFCSWLTAIFRIKDDEIRDKCGGDAVHYLSFQRHIIGLLVAVGVLSVGIVLPVNFSGDLLENNAYSFGRTTIANLNSGNNLLWLHTSFAFLYLLLTVYSMRRHTSKMRYKEDDLVKRTLFINGISKYAEPEKIKKHFEEAYANCTVLEARPCYDVARLMFLDAERRKAERGRIYFTNLQSKENTPSMINPKPCGHLCCCVIRGCEEVEAIEYYTKLEEKLKDDYKREKEKVNEKPLGMAFVTFHNETITAIILKDFNACKCQGCACRGEPRASSCSESLHVSNWTVSYAPDPQNIYWEHLSIRGFIWWIRCLVINVVLFILLFFLTTPAIIITTMDKFNVTKPVEYLNNPIITQFFPTLLLWCFSALLPTIVYYSAFFEAHWTRSGENRTTMHKCYTFLIFMVLLLPSLGLSSLDVFFRWLFDKKFLAEAAVRFECVFLPDNGAFFVNYVIASAFIGNAMDLLRIPGLLMYMIRLCLARSAAERRNVKRHQAYEFQFGAAYAWMMCVFTVVMTYSITCPIIVPFGLMYMLLKHLVDRYNLYYAYLPAKLDKKIHSGAVNQVVAAPILCLFWLLFFSTMRTGFLAPTSMFTFVVLVITIVICLCHVCFGHFKYLSAHNYKIEHTEVDTTESRQNGRPATNLPAPKSAKYIAQVLQDSSPEGEATESEEQGSQDEELITTDGMNDTDFQSCEDSLIENEIRQ

[Multiple Choices]
A. 47..71; 139..171; 196..220; 421..450; 466..495; 500..536; 613..631; 635..659; 667..695; 701..721
B. 47..71; 139..171; 196..220; 421..450; 466..495; 500..536; 560..592; 613..631; 635..659; 669..693; 701..721
C. 27..47; 78..98; 108..128; 136..156; 173..193; 209..229; 337..357; 366..386; 400..420; 432..452; 465..485
D. 47..71; 139..171; 196..220; 421..450; 466..495; 500..536; 560..592; 613..631; 635..659; 667..695; 701..721
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

> The sequence-matched UniProt record annotates the transmembrane regions as 47–71, 139–171, 196–220, 421–450, 466–495, 500–536, 560–592, 613–631, 635–659, 667–695, and 701–721, matching D. These annotations are supported by similarity evidence to Q3TWI9, not shown here to be direct experimental measurements for this chicken protein.

Citations as saved: [H4](#evidence-h4), [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16), [H18](#evidence-h18), [H20](#evidence-h20), [H22](#evidence-h22), [H24](#evidence-h24).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains multiple hydrophobic stretches consistent with membrane-spanning helices, which supports the general prediction of many transmembrane regions.


**Missing item-specific fact**

> The exact annotated helix boundaries—especially whether the final listed helix is 667–695 or 669–693—are protein-specific coordinate information not supplied in the question.


**Reason**

> General hydropathy can identify plausible membrane-spanning regions but does not uniquely establish the precise listed boundaries. Distinguishing D from B requires the protein-specific annotation or an equivalent detailed analysis; recognizing or recalling the exact database entry would be lookup, not reasoning from the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> B and D differ only in the boundaries assigned to the same final hydrophobic helix. The broad description of a segment that crosses a membrane does not itself explain why the narrower 669–693 interval should be rejected as a crossing segment, although the matched annotation specifies 667–695.


### Important caveats

- The reviewer-only source sequence matches the supplied sequence; the author’s precise source snapshot is unknown.
- The cited transmembrane annotations carry similarity-based evidence, so they support the key as annotation but do not establish direct experimental verification for this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple hydrophobic stretches consistent with membrane-spanning helices, which supports the general prediction of many transmembrane regions.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact annotated helix boundaries—especially whether the final listed helix is 667–695 or 669–693—are protein-specific coordinate information not supplied in the question.",
    "reason": "General hydropathy can identify plausible membrane-spanning regions but does not uniquely establish the precise listed boundaries. Distinguishing D from B requires the protein-specific annotation or an equivalent detailed analysis; recognizing or recalling the exact database entry would be lookup, not reasoning from the supplied input."
  },
  "case_id": "transmembrane_0034",
  "expected_answer_check": {
    "evidence_ids": [
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
    "reason": "The sequence-matched UniProt record annotates the transmembrane regions as 47–71, 139–171, 196–220, 421–450, 466–495, 500–536, 560–592, 613–631, 635–659, 667–695, and 701–721, matching D. These annotations are supported by similarity evidence to Q3TWI9, not shown here to be direct experimental measurements for this chicken protein."
  },
  "important_caveats": [
    "The reviewer-only source sequence matches the supplied sequence; the author’s precise source snapshot is unknown.",
    "The cited transmembrane annotations carry similarity-based evidence, so they support the key as annotation but do not establish direct experimental verification for this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "B and D differ only in the boundaries assigned to the same final hydrophobic helix. The broad description of a segment that crosses a membrane does not itself explain why the narrower 669–693 interval should be rejected as a crossing segment, although the matched annotation specifies 667–695."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0034",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the transmembrane regions as 47–71, 139–171, 196–220, 421–450, 466–495, 500–536, 560–592, 613–631, 635–659, 667–695, and 701–721, matching D. These annotations are supported by similarity evidence to Q3TWI9, not shown here to be direct experimental measurements for this chicken protein.",
    "evidence_ids": ["H4", "H6", "H8", "H10", "H12", "H14", "H16", "H18", "H20", "H22", "H24"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains multiple hydrophobic stretches consistent with membrane-spanning helices, which supports the general prediction of many transmembrane regions.",
    "missing_item_specific_fact": "The exact annotated helix boundaries—especially whether the final listed helix is 667–695 or 669–693—are protein-specific coordinate information not supplied in the question.",
    "reason": "General hydropathy can identify plausible membrane-spanning regions but does not uniquely establish the precise listed boundaries. Distinguishing D from B requires the protein-specific annotation or an equivalent detailed analysis; recognizing or recalling the exact database entry would be lookup, not reasoning from the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "B and D differ only in the boundaries assigned to the same final hydrophobic helix. The broad description of a segment that crosses a membrane does not itself explain why the narrower 669–693 interval should be rejected as a crossing segment, although the matched annotation specifies 667–695."
  },
  "important_caveats": [
    "The reviewer-only source sequence matches the supplied sequence; the author’s precise source snapshot is unknown.",
    "The cited transmembrane annotations carry similarity-based evidence, so they support the key as annotation but do not establish direct experimental verification for this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> Choice D lists exactly 11 transmembrane helices (TM0–TM10) at positions 47..71, 139..171, 196..220, 421..450, 466..495, 500..536, 560..592, 613..631, 635..659, 667..695, 701..721, which match the UniProtKB annotation for A0A8V0ZB02 (TMEM63B_CHICK) residue-for-residue. The sequence in the question matches the UniProt entry exactly (SHA-256 confirmed). The annotation evidence codes are ECO:0000250 (similarity to human Q3TWI9), indicating computational transfer rather than direct experimental determination, but the annotation is the authoritative database record for this protein.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C20](#evidence-c20), [C22](#evidence-c22), [C24](#evidence-c24), [C26](#evidence-c26), [H4](#evidence-h4), [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16), [H18](#evidence-h18), [H20](#evidence-h20), [H22](#evidence-h22), [H24](#evidence-h24).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Choice C can be eliminated by general reasoning: it presents uniform 20-residue segments with a naive sliding-window topology that does not match the known 11-TM architecture of the TMEM63/OSCA family. Choice A is missing TM6 (560..592), which could in principle be identified as a hydrophobic stretch by sequence analysis. However, the critical distinction between B and D is a 2-residue boundary shift at TM9 (669..693 vs 667..695). This falls well within the ±2–3 residue uncertainty of any hydrophobicity-based TM predictor (TMHMM, Phobius, DeepTMHMM) and cannot be resolved by general biological reasoning about helix length, hydrophobicity, or topology. Selecting D over B requires knowledge of the specific annotation boundary from UniProt or the output of a particular prediction tool.


**Missing item-specific fact**

> The exact TM9 boundary assignment (667..695 vs 669..693) as recorded in the UniProt annotation for A0A8V0ZB02, which was derived by similarity transfer from human TMEM63B (Q3TWI9) and is not derivable from the sequence alone through general biological principles.


**Reason**

> While eliminating C and identifying the missing TM6 in A involves some reasoning about TM domain length and hydrophobicity, the final B-vs-D discrimination hinges on a 2-residue boundary difference at TM9 that is within the resolution limit of hydrophobicity prediction. This is an item-specific annotation fact, not a consequence of general biological knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> B and D differ only at TM9 boundaries (669..693 vs 667..695). A 2-residue shift at a TM helix boundary is within the typical uncertainty of hydrophobicity-based prediction and does not alter the topology or the number of membrane crossings. From a pure sequence-analysis standpoint, both assignments are biologically plausible. D is correct per the UniProt annotation, but the question wording ('correctly identifies the start and end positions') does not provide grounds to prefer 667 over 669 or 695 over 693 without referencing the specific annotation.


### Important caveats

- All 11 TM annotations carry evidence code ECO:0000250 (similarity to Q3TWI9), meaning they are computational transfers from the human ortholog, not experimentally validated boundaries for the chicken protein.
- The UniProt entry was first public on 2025-06-18; the author's source snapshot date is unknown, so the annotation available at question-construction time may differ.
- Choice A (10 segments, missing TM6) and Choice C (naive 20-residue scan) are clearly distinguishable from D by reasoning; the ambiguity is confined to the B-vs-D boundary.
- The sequence matches the UniProt entry exactly (SHA-256 verified), so coordinate numbering is consistent.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Choice C can be eliminated by general reasoning: it presents uniform 20-residue segments with a naive sliding-window topology that does not match the known 11-TM architecture of the TMEM63/OSCA family. Choice A is missing TM6 (560..592), which could in principle be identified as a hydrophobic stretch by sequence analysis. However, the critical distinction between B and D is a 2-residue boundary shift at TM9 (669..693 vs 667..695). This falls well within the ±2–3 residue uncertainty of any hydrophobicity-based TM predictor (TMHMM, Phobius, DeepTMHMM) and cannot be resolved by general biological reasoning about helix length, hydrophobicity, or topology. Selecting D over B requires knowledge of the specific annotation boundary from UniProt or the output of a particular prediction tool.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact TM9 boundary assignment (667..695 vs 669..693) as recorded in the UniProt annotation for A0A8V0ZB02, which was derived by similarity transfer from human TMEM63B (Q3TWI9) and is not derivable from the sequence alone through general biological principles.",
    "reason": "While eliminating C and identifying the missing TM6 in A involves some reasoning about TM domain length and hydrophobicity, the final B-vs-D discrimination hinges on a 2-residue boundary difference at TM9 that is within the resolution limit of hydrophobicity prediction. This is an item-specific annotation fact, not a consequence of general biological knowledge."
  },
  "case_id": "transmembrane_0034",
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
    "reason": "Choice D lists exactly 11 transmembrane helices (TM0–TM10) at positions 47..71, 139..171, 196..220, 421..450, 466..495, 500..536, 560..592, 613..631, 635..659, 667..695, 701..721, which match the UniProtKB annotation for A0A8V0ZB02 (TMEM63B_CHICK) residue-for-residue. The sequence in the question matches the UniProt entry exactly (SHA-256 confirmed). The annotation evidence codes are ECO:0000250 (similarity to human Q3TWI9), indicating computational transfer rather than direct experimental determination, but the annotation is the authoritative database record for this protein."
  },
  "important_caveats": [
    "All 11 TM annotations carry evidence code ECO:0000250 (similarity to Q3TWI9), meaning they are computational transfers from the human ortholog, not experimentally validated boundaries for the chicken protein.",
    "The UniProt entry was first public on 2025-06-18; the author's source snapshot date is unknown, so the annotation available at question-construction time may differ.",
    "Choice A (10 segments, missing TM6) and Choice C (naive 20-residue scan) are clearly distinguishable from D by reasoning; the ambiguity is confined to the B-vs-D boundary.",
    "The sequence matches the UniProt entry exactly (SHA-256 verified), so coordinate numbering is consistent."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "B and D differ only at TM9 boundaries (669..693 vs 667..695). A 2-residue shift at a TM helix boundary is within the typical uncertainty of hydrophobicity-based prediction and does not alter the topology or the number of membrane crossings. From a pure sequence-analysis standpoint, both assignments are biologically plausible. D is correct per the UniProt annotation, but the question wording ('correctly identifies the start and end positions') does not provide grounds to prefer 667 over 669 or 695 over 693 without referencing the specific annotation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0034",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "Choice D lists exactly 11 transmembrane helices (TM0–TM10) at positions 47..71, 139..171, 196..220, 421..450, 466..495, 500..536, 560..592, 613..631, 635..659, 667..695, 701..721, which match the UniProtKB annotation for A0A8V0ZB02 (TMEM63B_CHICK) residue-for-residue. The sequence in the question matches the UniProt entry exactly (SHA-256 confirmed). The annotation evidence codes are ECO:0000250 (similarity to human Q3TWI9), indicating computational transfer rather than direct experimental determination, but the annotation is the authoritative database record for this protein.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "C20", "C22", "C24", "C26", "H4", "H6", "H8", "H10", "H12", "H14", "H16", "H18", "H20", "H22", "H24"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Choice C can be eliminated by general reasoning: it presents uniform 20-residue segments with a naive sliding-window topology that does not match the known 11-TM architecture of the TMEM63/OSCA family. Choice A is missing TM6 (560..592), which could in principle be identified as a hydrophobic stretch by sequence analysis. However, the critical distinction between B and D is a 2-residue boundary shift at TM9 (669..693 vs 667..695). This falls well within the ±2–3 residue uncertainty of any hydrophobicity-based TM predictor (TMHMM, Phobius, DeepTMHMM) and cannot be resolved by general biological reasoning about helix length, hydrophobicity, or topology. Selecting D over B requires knowledge of the specific annotation boundary from UniProt or the output of a particular prediction tool.",
    "missing_item_specific_fact": "The exact TM9 boundary assignment (667..695 vs 669..693) as recorded in the UniProt annotation for A0A8V0ZB02, which was derived by similarity transfer from human TMEM63B (Q3TWI9) and is not derivable from the sequence alone through general biological principles.",
    "reason": "While eliminating C and identifying the missing TM6 in A involves some reasoning about TM domain length and hydrophobicity, the final B-vs-D discrimination hinges on a 2-residue boundary difference at TM9 that is within the resolution limit of hydrophobicity prediction. This is an item-specific annotation fact, not a consequence of general biological knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "B and D differ only at TM9 boundaries (669..693 vs 667..695). A 2-residue shift at a TM helix boundary is within the typical uncertainty of hydrophobicity-based prediction and does not alter the topology or the number of membrane crossings. From a pure sequence-analysis standpoint, both assignments are biologically plausible. D is correct per the UniProt annotation, but the question wording ('correctly identifies the start and end positions') does not provide grounds to prefer 667 over 669 or 695 over 693 without referencing the specific annotation."
  },
  "important_caveats": [
    "All 11 TM annotations carry evidence code ECO:0000250 (similarity to Q3TWI9), meaning they are computational transfers from the human ortholog, not experimentally validated boundaries for the chicken protein.",
    "The UniProt entry was first public on 2025-06-18; the author's source snapshot date is unknown, so the annotation available at question-construction time may differ.",
    "Choice A (10 segments, missing TM6) and Choice C (naive 20-residue scan) are clearly distinguishable from D by reasoning; the ambiguity is confined to the B-vs-D boundary.",
    "The sequence matches the UniProt entry exactly (SHA-256 verified), so coordinate numbering is consistent."
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

> Exact-match historical features annotate keyD, including667..695 with similarity evidence. OptionB narrows it to669..693;701..721 remains the final interval in both.

**Remaining uncertainty:** The source establishes the keyed coordinates but does not independently validate the narrowed alternative. The model calls the differing interval the final helix, although it is penultimate in the listed coordinate set.

Evidence checked: [H4](#evidence-h4), [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16), [H18](#evidence-h18), [H20](#evidence-h20), [H22](#evidence-h22), [H24](#evidence-h24).

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `A0A8V0ZB02` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 16. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:51.590118+00:00.  

```json
{"description":"Helical; Name=TM0","evidences":[{"evidenceCode":"ECO:0000250","id":"Q3TWI9","source":"UniProtKB"}],"location":{"end":{"modifier":"EXACT","value":71},"start":{"modifier":"EXACT","value":47}},"type":"Transmembrane"}
```

Source SHA-256: `2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:51.590118+00:00.  

```json
{"description":"Helical; Name=TM1","evidences":[{"evidenceCode":"ECO:0000250","id":"Q3TWI9","source":"UniProtKB"}],"location":{"end":{"modifier":"EXACT","value":171},"start":{"modifier":"EXACT","value":139}},"type":"Transmembrane"}
```

Source SHA-256: `2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:51.590118+00:00.  

```json
{"description":"Helical; Name=TM2","evidences":[{"evidenceCode":"ECO:0000250","id":"Q3TWI9","source":"UniProtKB"}],"location":{"end":{"modifier":"EXACT","value":220},"start":{"modifier":"EXACT","value":196}},"type":"Transmembrane"}
```

Source SHA-256: `2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)  
**Locator:** `/features/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:51.590118+00:00.  

```json
{"description":"Helical; Name=TM3","evidences":[{"evidenceCode":"ECO:0000250","id":"Q3TWI9","source":"UniProtKB"}],"location":{"end":{"modifier":"EXACT","value":450},"start":{"modifier":"EXACT","value":421}},"type":"Transmembrane"}
```

Source SHA-256: `2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74`.

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)  
**Locator:** `/features/10`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:51.590118+00:00.  

```json
{"description":"Helical; Name=TM4","evidences":[{"evidenceCode":"ECO:0000250","id":"Q3TWI9","source":"UniProtKB"}],"location":{"end":{"modifier":"EXACT","value":495},"start":{"modifier":"EXACT","value":466}},"type":"Transmembrane"}
```

Source SHA-256: `2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74`.

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)  
**Locator:** `/features/12`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:51.590118+00:00.  

```json
{"description":"Helical; Name=TM5","evidences":[{"evidenceCode":"ECO:0000250","id":"Q3TWI9","source":"UniProtKB"}],"location":{"end":{"modifier":"EXACT","value":536},"start":{"modifier":"EXACT","value":500}},"type":"Transmembrane"}
```

Source SHA-256: `2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74`.

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)  
**Locator:** `/features/14`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:51.590118+00:00.  

```json
{"description":"Helical; Name=TM6","evidences":[{"evidenceCode":"ECO:0000250","id":"Q3TWI9","source":"UniProtKB"}],"location":{"end":{"modifier":"EXACT","value":592},"start":{"modifier":"EXACT","value":560}},"type":"Transmembrane"}
```

Source SHA-256: `2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74`.

### Evidence C20

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)  
**Locator:** `/features/16`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:51.590118+00:00.  

```json
{"description":"Helical; Name=TM7","evidences":[{"evidenceCode":"ECO:0000250","id":"Q3TWI9","source":"UniProtKB"}],"location":{"end":{"modifier":"EXACT","value":631},"start":{"modifier":"EXACT","value":613}},"type":"Transmembrane"}
```

Source SHA-256: `2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74`.

### Evidence C22

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)  
**Locator:** `/features/18`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:51.590118+00:00.  

```json
{"description":"Helical; Name=TM8","evidences":[{"evidenceCode":"ECO:0000250","id":"Q3TWI9","source":"UniProtKB"}],"location":{"end":{"modifier":"EXACT","value":659},"start":{"modifier":"EXACT","value":635}},"type":"Transmembrane"}
```

Source SHA-256: `2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74`.

### Evidence C24

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)  
**Locator:** `/features/20`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:51.590118+00:00.  

```json
{"description":"Helical; Name=TM9","evidences":[{"evidenceCode":"ECO:0000250","id":"Q3TWI9","source":"UniProtKB"}],"location":{"end":{"modifier":"EXACT","value":695},"start":{"modifier":"EXACT","value":667}},"type":"Transmembrane"}
```

Source SHA-256: `2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74`.

### Evidence C26

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8V0ZB02.json)  
**Locator:** `/features/22`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:51.590118+00:00.  

```json
{"description":"Helical; Name=TM10","evidences":[{"evidenceCode":"ECO:0000250","id":"Q3TWI9","source":"UniProtKB"}],"location":{"end":{"modifier":"EXACT","value":721},"start":{"modifier":"EXACT","value":701}},"type":"Transmembrane"}
```

Source SHA-256: `2a70bd6be844793f85a89646f4b0890123b0430bff08bb408f761d9ee7d44c74`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)  
**Locator:** `lines 137-139`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 16 / 1.  
**Retrieved:** 2026-11-01T06:27:36.055628+00:00.  

```text
FT   TRANSMEM        47..71
FT                   /note="Helical; Name=TM0"
FT                   /evidence="ECO:0000250|UniProtKB:Q3TWI9"
```

Source SHA-256: `098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)  
**Locator:** `lines 143-145`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 16 / 1.  
**Retrieved:** 2026-11-01T06:27:36.055628+00:00.  

```text
FT   TRANSMEM        139..171
FT                   /note="Helical; Name=TM1"
FT                   /evidence="ECO:0000250|UniProtKB:Q3TWI9"
```

Source SHA-256: `098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)  
**Locator:** `lines 149-151`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 16 / 1.  
**Retrieved:** 2026-11-01T06:27:36.055628+00:00.  

```text
FT   TRANSMEM        196..220
FT                   /note="Helical; Name=TM2"
FT                   /evidence="ECO:0000250|UniProtKB:Q3TWI9"
```

Source SHA-256: `098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704`.

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)  
**Locator:** `lines 155-157`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 16 / 1.  
**Retrieved:** 2026-11-01T06:27:36.055628+00:00.  

```text
FT   TRANSMEM        421..450
FT                   /note="Helical; Name=TM3"
FT                   /evidence="ECO:0000250|UniProtKB:Q3TWI9"
```

Source SHA-256: `098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704`.

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)  
**Locator:** `lines 161-163`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 16 / 1.  
**Retrieved:** 2026-11-01T06:27:36.055628+00:00.  

```text
FT   TRANSMEM        466..495
FT                   /note="Helical; Name=TM4"
FT                   /evidence="ECO:0000250|UniProtKB:Q3TWI9"
```

Source SHA-256: `098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704`.

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)  
**Locator:** `lines 167-169`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 16 / 1.  
**Retrieved:** 2026-11-01T06:27:36.055628+00:00.  

```text
FT   TRANSMEM        500..536
FT                   /note="Helical; Name=TM5"
FT                   /evidence="ECO:0000250|UniProtKB:Q3TWI9"
```

Source SHA-256: `098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704`.

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)  
**Locator:** `lines 173-175`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 16 / 1.  
**Retrieved:** 2026-11-01T06:27:36.055628+00:00.  

```text
FT   TRANSMEM        560..592
FT                   /note="Helical; Name=TM6"
FT                   /evidence="ECO:0000250|UniProtKB:Q3TWI9"
```

Source SHA-256: `098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704`.

### Evidence H18

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)  
**Locator:** `lines 179-181`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 16 / 1.  
**Retrieved:** 2026-11-01T06:27:36.055628+00:00.  

```text
FT   TRANSMEM        613..631
FT                   /note="Helical; Name=TM7"
FT                   /evidence="ECO:0000250|UniProtKB:Q3TWI9"
```

Source SHA-256: `098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704`.

### Evidence H20

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)  
**Locator:** `lines 185-187`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 16 / 1.  
**Retrieved:** 2026-11-01T06:27:36.055628+00:00.  

```text
FT   TRANSMEM        635..659
FT                   /note="Helical; Name=TM8"
FT                   /evidence="ECO:0000250|UniProtKB:Q3TWI9"
```

Source SHA-256: `098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704`.

### Evidence H22

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)  
**Locator:** `lines 191-193`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 16 / 1.  
**Retrieved:** 2026-11-01T06:27:36.055628+00:00.  

```text
FT   TRANSMEM        667..695
FT                   /note="Helical; Name=TM9"
FT                   /evidence="ECO:0000250|UniProtKB:Q3TWI9"
```

Source SHA-256: `098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704`.

### Evidence H24

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8V0ZB02?format=txt&versions=16)  
**Locator:** `lines 197-199`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 16 / 1.  
**Retrieved:** 2026-11-01T06:27:36.055628+00:00.  

```text
FT   TRANSMEM        701..721
FT                   /note="Helical; Name=TM10"
FT                   /evidence="ECO:0000250|UniProtKB:Q3TWI9"
```

Source SHA-256: `098fa8177aa78ced176ae350c71e2c32a9c01620a23e7c5f32ac21455a5f8704`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 34. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
