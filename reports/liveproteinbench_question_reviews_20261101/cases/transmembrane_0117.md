# transmembrane_0117

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **B** — 31..51; 82..102; 112..132; 138..158; 179..199; 211..231; 353..373; 381..401; 409..429; 437..457; 478..498

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTTSSDSAMVNHTPSPWYKFGFKSFAEFNTYVTFVFLGMSIMMVASAVTSAPDFLTRYYVYATGDPDAVAETPLFWNNANTFYNAGTYVLQVLTELFSLTPFMRRIPLSVRLFVGLGIPFAELLLIIIVPAATIKSQHGAIAVIMVVACVGGFSKALCDSCTNALVGPFPTKFMNGAQWGLTVIALLMSIIQIILKVSMGTSFHDILTMSRIYFGICIGIQLFAIFELAILRFNPFAQKYIAEYRAGAQRNAQNNESTLEETAPSMNEPAAGDIADLPATVDDKERALNEEEGDEVRAVTSEEFHVKRGAVLTATGDADKMVDLDQTGNITSTEQLLRASAASVFKRVYPMLVCVFLIYFTSLLTFPGVFFLVSTTSGWYMTVIVTLFNAGDFISRMVLMFRPLRPSPKVVVAGTLGRLIIIPFLVLCVRGIIRGEALPYVLITLLGLTNGYFGCMACIHCPRTTTLRYAGERSLAAMLSGISIMLGLCFGSNLSLAITLTH

[Multiple Choices]
A. 61..81; 91..111; 169..189; 192..212; 276..296; 317..337; 789..809; 830..850; 908..928; 929..949; 1033..1053; 1058..1078
B. 31..51; 82..102; 112..132; 138..158; 179..199; 211..231; 353..373; 381..401; 409..429; 437..457; 478..498
C. 31..51; 82..102; 112..132; 138..158; 179..199; 211..231; 353..373; 381..401; 409..429; 437..457
D. 31..51; 82..102; 112..132; 138..158; 179..199; 211..231; 353..373; 384..405; 409..429; 437..457; 478..498
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

> The sequence matches the UniProt entry, whose annotated transmembrane regions match all 11 intervals in B. These span annotations are primarily computational (ECO:0000255), so they support the key as an annotation-based answer but are not, by themselves, experimental validation of every boundary.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C20](#evidence-c20), [C22](#evidence-c22), [C24](#evidence-c24), [C26](#evidence-c26).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has multiple strongly hydrophobic stretches consistent with a multi-pass membrane protein, including the C-terminal region omitted by C. This supports the broad pattern of transmembrane helices, but does not reliably establish the exact listed boundaries.


**Missing item-specific fact**

> The precise annotated boundaries for this particular protein, especially the distinction between 381..401 and the closely overlapping 384..405 interval, are not supplied in the question.


**Reason**

> General sequence reasoning can identify likely membrane-spanning stretches, but the options require exact residue intervals. Choosing the keyed set depends on protein-specific boundary annotations or a sufficiently calibrated predictor, not merely on broad hydrophobicity reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> B matches the cited annotation. However, B's 381..401 and D's 384..405 intervals substantially overlap the same hydrophobic segment, and the question gives no boundary convention that would make such a small shift biologically unambiguous.


### Important caveats

- The reviewer-only database identity and annotations were not supplied to the evaluated model.
- Database transmembrane features here are computational annotations; the cited topology evidence does not independently establish every helix boundary experimentally.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has multiple strongly hydrophobic stretches consistent with a multi-pass membrane protein, including the C-terminal region omitted by C. This supports the broad pattern of transmembrane helices, but does not reliably establish the exact listed boundaries.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The precise annotated boundaries for this particular protein, especially the distinction between 381..401 and the closely overlapping 384..405 interval, are not supplied in the question.",
    "reason": "General sequence reasoning can identify likely membrane-spanning stretches, but the options require exact residue intervals. Choosing the keyed set depends on protein-specific boundary annotations or a sufficiently calibrated predictor, not merely on broad hydrophobicity reasoning."
  },
  "case_id": "transmembrane_0117",
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
    "reason": "The sequence matches the UniProt entry, whose annotated transmembrane regions match all 11 intervals in B. These span annotations are primarily computational (ECO:0000255), so they support the key as an annotation-based answer but are not, by themselves, experimental validation of every boundary."
  },
  "important_caveats": [
    "The reviewer-only database identity and annotations were not supplied to the evaluated model.",
    "Database transmembrane features here are computational annotations; the cited topology evidence does not independently establish every helix boundary experimentally."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "B matches the cited annotation. However, B's 381..401 and D's 384..405 intervals substantially overlap the same hydrophobic segment, and the question gives no boundary convention that would make such a small shift biologically unambiguous."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0117",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry, whose annotated transmembrane regions match all 11 intervals in B. These span annotations are primarily computational (ECO:0000255), so they support the key as an annotation-based answer but are not, by themselves, experimental validation of every boundary.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "C20", "C22", "C24", "C26"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has multiple strongly hydrophobic stretches consistent with a multi-pass membrane protein, including the C-terminal region omitted by C. This supports the broad pattern of transmembrane helices, but does not reliably establish the exact listed boundaries.",
    "missing_item_specific_fact": "The precise annotated boundaries for this particular protein, especially the distinction between 381..401 and the closely overlapping 384..405 interval, are not supplied in the question.",
    "reason": "General sequence reasoning can identify likely membrane-spanning stretches, but the options require exact residue intervals. Choosing the keyed set depends on protein-specific boundary annotations or a sufficiently calibrated predictor, not merely on broad hydrophobicity reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "B matches the cited annotation. However, B's 381..401 and D's 384..405 intervals substantially overlap the same hydrophobic segment, and the question gives no boundary convention that would make such a small shift biologically unambiguous."
  },
  "important_caveats": [
    "The reviewer-only database identity and annotations were not supplied to the evaluated model.",
    "Database transmembrane features here are computational annotations; the cited topology evidence does not independently establish every helix boundary experimentally."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9GTP4 (Crithidia fasciculata Nucleoside transporter 2, CfNT2) annotates exactly 11 transmembrane helices at positions 31-51, 82-102, 112-132, 138-158, 179-199, 211-231, 353-373, 381-401, 409-429, 437-457, and 478-498, matching Choice B exactly. The sequence in the question (502 aa) matches the UniProt sequence (sha256 confirmed). TM boundaries carry evidence code ECO:0000255 (computational/PROSITE pattern-based prediction), while intervening topological domains are supported by experimental mutagenesis data (PubMed:20037157). The key is consistent with the database annotation.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C20](#evidence-c20), [C22](#evidence-c22), [C24](#evidence-c24), [C26](#evidence-c26), [H5](#evidence-h5), [H7](#evidence-h7), [H9](#evidence-h9), [H11](#evidence-h11), [H13](#evidence-h13), [H15](#evidence-h15), [H17](#evidence-h17), [H19](#evidence-h19), [H21](#evidence-h21), [H23](#evidence-h23), [H25](#evidence-h25).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Choice A can be eliminated by noting positions 789, 830, 908, 929, 1033, 1058 exceed the 502-residue protein length. General ENT-family knowledge (equilibrative nucleoside transporters typically have 11 TM helices) could help eliminate Choice C (only 10 TMs). However, the critical B-vs-D distinction—whether TM8 spans 381-401 or 384-405 (a 3-residue shift)—cannot be resolved by general hydrophobicity reasoning; the region contains a mix of hydrophobic and polar residues whose exact helix boundaries depend on the specific prediction algorithm (PROSITE PS50250 pattern matching, ECO:0000255).


**Missing item-specific fact**

> The precise start/end coordinates of TM8 (381-401 vs 384-405) as determined by the specific computational prediction method used in the UniProt annotation. No general biological principle or simple hydrophobicity analysis distinguishes a 21-residue helix starting at 381 from one starting at 384 in this particular sequence context.


**Reason**

> While A is trivially eliminable and C is weakly eliminable via ENT-family topology knowledge, the decisive B-vs-D distinction requires knowledge of the exact algorithmic boundaries assigned to this protein's TM helices. This is an item-specific annotation fact, not derivable from general transmembrane biology.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> Both B and D contain 11 TM segments with nearly identical boundaries. The only difference is TM8 (381-401 in B vs 384-405 in D), a 3-residue shift that falls within the typical uncertainty of hydrophobicity-based TM prediction. Without access to the specific prediction algorithm's output, both boundaries are plausible for a helix in this region. The sequence in the 381-405 window contains sufficient hydrophobic character to support either boundary assignment.


### Important caveats

- All TM boundary annotations carry ECO:0000255 (computational prediction via PROSITE pattern), not experimental determination of helix boundaries. The experimental evidence (PubMed:20037157) supports the overall topology (number of TMs, inside/outside orientation) but not the exact residue-level start/end of each helix.
- Choice A is clearly invalid (positions exceed protein length), serving as an easy distractor.
- The UniProt entry was first released in 2025-02-05; the author's source snapshot is unknown, though the sequence has been unchanged since 2001-03-01.
- The ENT family generally has 11 TM helices, which provides weak reasoning support for choosing an 11-TM answer (B or D) over C (10 TMs).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Choice A can be eliminated by noting positions 789, 830, 908, 929, 1033, 1058 exceed the 502-residue protein length. General ENT-family knowledge (equilibrative nucleoside transporters typically have 11 TM helices) could help eliminate Choice C (only 10 TMs). However, the critical B-vs-D distinction—whether TM8 spans 381-401 or 384-405 (a 3-residue shift)—cannot be resolved by general hydrophobicity reasoning; the region contains a mix of hydrophobic and polar residues whose exact helix boundaries depend on the specific prediction algorithm (PROSITE PS50250 pattern matching, ECO:0000255).",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The precise start/end coordinates of TM8 (381-401 vs 384-405) as determined by the specific computational prediction method used in the UniProt annotation. No general biological principle or simple hydrophobicity analysis distinguishes a 21-residue helix starting at 381 from one starting at 384 in this particular sequence context.",
    "reason": "While A is trivially eliminable and C is weakly eliminable via ENT-family topology knowledge, the decisive B-vs-D distinction requires knowledge of the exact algorithmic boundaries assigned to this protein's TM helices. This is an item-specific annotation fact, not derivable from general transmembrane biology."
  },
  "case_id": "transmembrane_0117",
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
      "H5",
      "H7",
      "H9",
      "H11",
      "H13",
      "H15",
      "H17",
      "H19",
      "H21",
      "H23",
      "H25"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q9GTP4 (Crithidia fasciculata Nucleoside transporter 2, CfNT2) annotates exactly 11 transmembrane helices at positions 31-51, 82-102, 112-132, 138-158, 179-199, 211-231, 353-373, 381-401, 409-429, 437-457, and 478-498, matching Choice B exactly. The sequence in the question (502 aa) matches the UniProt sequence (sha256 confirmed). TM boundaries carry evidence code ECO:0000255 (computational/PROSITE pattern-based prediction), while intervening topological domains are supported by experimental mutagenesis data (PubMed:20037157). The key is consistent with the database annotation."
  },
  "important_caveats": [
    "All TM boundary annotations carry ECO:0000255 (computational prediction via PROSITE pattern), not experimental determination of helix boundaries. The experimental evidence (PubMed:20037157) supports the overall topology (number of TMs, inside/outside orientation) but not the exact residue-level start/end of each helix.",
    "Choice A is clearly invalid (positions exceed protein length), serving as an easy distractor.",
    "The UniProt entry was first released in 2025-02-05; the author's source snapshot is unknown, though the sequence has been unchanged since 2001-03-01.",
    "The ENT family generally has 11 TM helices, which provides weak reasoning support for choosing an 11-TM answer (B or D) over C (10 TMs)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "Both B and D contain 11 TM segments with nearly identical boundaries. The only difference is TM8 (381-401 in B vs 384-405 in D), a 3-residue shift that falls within the typical uncertainty of hydrophobicity-based TM prediction. Without access to the specific prediction algorithm's output, both boundaries are plausible for a helix in this region. The sequence in the 381-405 window contains sufficient hydrophobic character to support either boundary assignment."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0117",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9GTP4 (Crithidia fasciculata Nucleoside transporter 2, CfNT2) annotates exactly 11 transmembrane helices at positions 31-51, 82-102, 112-132, 138-158, 179-199, 211-231, 353-373, 381-401, 409-429, 437-457, and 478-498, matching Choice B exactly. The sequence in the question (502 aa) matches the UniProt sequence (sha256 confirmed). TM boundaries carry evidence code ECO:0000255 (computational/PROSITE pattern-based prediction), while intervening topological domains are supported by experimental mutagenesis data (PubMed:20037157). The key is consistent with the database annotation.",
    "evidence_ids": ["C6","C8","C10","C12","C14","C16","C18","C20","C22","C24","C26","H5","H7","H9","H11","H13","H15","H17","H19","H21","H23","H25"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Choice A can be eliminated by noting positions 789, 830, 908, 929, 1033, 1058 exceed the 502-residue protein length. General ENT-family knowledge (equilibrative nucleoside transporters typically have 11 TM helices) could help eliminate Choice C (only 10 TMs). However, the critical B-vs-D distinction—whether TM8 spans 381-401 or 384-405 (a 3-residue shift)—cannot be resolved by general hydrophobicity reasoning; the region contains a mix of hydrophobic and polar residues whose exact helix boundaries depend on the specific prediction algorithm (PROSITE PS50250 pattern matching, ECO:0000255).",
    "missing_item_specific_fact": "The precise start/end coordinates of TM8 (381-401 vs 384-405) as determined by the specific computational prediction method used in the UniProt annotation. No general biological principle or simple hydrophobicity analysis distinguishes a 21-residue helix starting at 381 from one starting at 384 in this particular sequence context.",
    "reason": "While A is trivially eliminable and C is weakly eliminable via ENT-family topology knowledge, the decisive B-vs-D distinction requires knowledge of the exact algorithmic boundaries assigned to this protein's TM helices. This is an item-specific annotation fact, not derivable from general transmembrane biology."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "Both B and D contain 11 TM segments with nearly identical boundaries. The only difference is TM8 (381-401 in B vs 384-405 in D), a 3-residue shift that falls within the typical uncertainty of hydrophobicity-based TM prediction. Without access to the specific prediction algorithm's output, both boundaries are plausible for a helix in this region. The sequence in the 381-405 window contains sufficient hydrophobic character to support either boundary assignment."
  },
  "important_caveats": [
    "All TM boundary annotations carry ECO:0000255 (computational prediction via PROSITE pattern), not experimental determination of helix boundaries. The experimental evidence (PubMed:20037157) supports the overall topology (number of TMs, inside/outside orientation) but not the exact residue-level start/end of each helix.",
    "Choice A is clearly invalid (positions exceed protein length), serving as an easy distractor.",
    "The UniProt entry was first released in 2025-02-05; the author's source snapshot is unknown, though the sequence has been unchanged since 2001-03-01.",
    "The ENT family generally has 11 TM helices, which provides weak reasoning support for choosing an 11-TM answer (B or D) over C (10 TMs)."
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

> Cited computational Transmembrane features match keyB381..401; original optionD substitutes384..405, as the model states.

**Remaining uncertainty:** These annotations establish the database interval but do not demonstrate that the alternative interval is equally valid under the wording.

Evidence checked: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C20](#evidence-c20), [C22](#evidence-c22), [C24](#evidence-c24), [C26](#evidence-c26).

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `Q9GTP4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 55. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:48.296419+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":51},"start":{"modifier":"EXACT","value":31}},"type":"Transmembrane"}
```

Source SHA-256: `3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:48.296419+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":102},"start":{"modifier":"EXACT","value":82}},"type":"Transmembrane"}
```

Source SHA-256: `3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:48.296419+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":132},"start":{"modifier":"EXACT","value":112}},"type":"Transmembrane"}
```

Source SHA-256: `3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)  
**Locator:** `/features/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:48.296419+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":158},"start":{"modifier":"EXACT","value":138}},"type":"Transmembrane"}
```

Source SHA-256: `3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73`.

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)  
**Locator:** `/features/10`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:48.296419+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":199},"start":{"modifier":"EXACT","value":179}},"type":"Transmembrane"}
```

Source SHA-256: `3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73`.

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)  
**Locator:** `/features/12`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:48.296419+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":231},"start":{"modifier":"EXACT","value":211}},"type":"Transmembrane"}
```

Source SHA-256: `3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73`.

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)  
**Locator:** `/features/14`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:48.296419+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":373},"start":{"modifier":"EXACT","value":353}},"type":"Transmembrane"}
```

Source SHA-256: `3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73`.

### Evidence C20

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)  
**Locator:** `/features/16`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:48.296419+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":401},"start":{"modifier":"EXACT","value":381}},"type":"Transmembrane"}
```

Source SHA-256: `3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73`.

### Evidence C22

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)  
**Locator:** `/features/18`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:48.296419+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":429},"start":{"modifier":"EXACT","value":409}},"type":"Transmembrane"}
```

Source SHA-256: `3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73`.

### Evidence C24

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)  
**Locator:** `/features/20`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:48.296419+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":457},"start":{"modifier":"EXACT","value":437}},"type":"Transmembrane"}
```

Source SHA-256: `3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73`.

### Evidence C26

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)  
**Locator:** `/features/22`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:48.296419+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":498},"start":{"modifier":"EXACT","value":478}},"type":"Transmembrane"}
```

Source SHA-256: `3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)  
**Locator:** `lines 86-88`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 55 / 1.  
**Retrieved:** 2026-11-02T04:32:52.675125+00:00.  

```text
FT   TRANSMEM        31..51
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)  
**Locator:** `lines 92-94`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 55 / 1.  
**Retrieved:** 2026-11-02T04:32:52.675125+00:00.  

```text
FT   TRANSMEM        82..102
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8`.

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)  
**Locator:** `lines 98-100`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 55 / 1.  
**Retrieved:** 2026-11-02T04:32:52.675125+00:00.  

```text
FT   TRANSMEM        112..132
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8`.

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)  
**Locator:** `lines 104-106`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 55 / 1.  
**Retrieved:** 2026-11-02T04:32:52.675125+00:00.  

```text
FT   TRANSMEM        138..158
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8`.

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)  
**Locator:** `lines 110-112`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 55 / 1.  
**Retrieved:** 2026-11-02T04:32:52.675125+00:00.  

```text
FT   TRANSMEM        179..199
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8`.

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)  
**Locator:** `lines 116-118`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 55 / 1.  
**Retrieved:** 2026-11-02T04:32:52.675125+00:00.  

```text
FT   TRANSMEM        211..231
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8`.

### Evidence H17

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)  
**Locator:** `lines 122-124`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 55 / 1.  
**Retrieved:** 2026-11-02T04:32:52.675125+00:00.  

```text
FT   TRANSMEM        353..373
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8`.

### Evidence H19

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)  
**Locator:** `lines 128-130`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 55 / 1.  
**Retrieved:** 2026-11-02T04:32:52.675125+00:00.  

```text
FT   TRANSMEM        381..401
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8`.

### Evidence H21

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)  
**Locator:** `lines 134-136`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 55 / 1.  
**Retrieved:** 2026-11-02T04:32:52.675125+00:00.  

```text
FT   TRANSMEM        409..429
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8`.

### Evidence H23

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)  
**Locator:** `lines 140-142`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 55 / 1.  
**Retrieved:** 2026-11-02T04:32:52.675125+00:00.  

```text
FT   TRANSMEM        437..457
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8`.

### Evidence H25

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)  
**Locator:** `lines 146-148`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 55 / 1.  
**Retrieved:** 2026-11-02T04:32:52.675125+00:00.  

```text
FT   TRANSMEM        478..498
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 117. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
