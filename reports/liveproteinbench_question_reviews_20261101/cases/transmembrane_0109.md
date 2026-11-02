# transmembrane_0109

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **D** — 357..377; 397..419; 481..501; 506..526; 591..611; 619..639

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MRSFYNKCFTNKLISAHSLFCQHVSTLKNNKKECFEDVKRSNRISDEFYSSFLYHSYIENLKSTKEYVYFIYLQDIYYNINIFKNKGRLYISNNGLCNDKLKDNNNNNNINSNNFGNSYNAYTKKKSFYHSFNDLNEAKEIRKKRKNEKSEKNIVEYLLCNIINPNENYHIQNIYNHNLNNNVSIEIHKKNDSVMYHYNNEKKTKTSKMTTDIKLKQINNVYIKYVPYKNKIITLACPNKYYPTLYRYFSSHTNKKEDAEENDKNKNININNVDNRYKEDFMYGCENKNDSEKHKKTTNNNFGDEFEKLKVKELDKILNKLEMLYDNKNNKMNINVKILGYIFKNFLLKNKELKRKIFCSLFFLLCSKMAIIYTPILLSTFIENVNLQKSLSNNIDIYSTNKSSVLLLCAYVFSRVLSSTMNELRNSVFSNISQKISTFVSKLFFYKIHNLNLTYILSKKNGELSFIFNRGCKSITNLLNVMVFQIIPIIIEFILYLYILTYKIHYTVSLVTCFNMFLYVLFTTLITKRRTIIRKHMNKAEQNTFNIFLDSIQNVEQVKYYTNEIHELKKFIKEQKKYEKEAINVQKSLSFLNFGQQIILNTNLFLCMYLTYLNIANDIFPFSYLILVNTLLFQLAMPLNMFGTIYRETKLSLVDIESMIKILVKKIKSPDYGNQMLIKNGNIKFENVYFKYPLNEDINGLEQNYQAKEKDPNIINNINNINNINNINNINNINSINNIYTFESNVKNISSTNMITSSINKLKKWYLDKVKDNKKNVQYNNNDVKKTNPNITKNLNKEIKENINTHLKNHKIINNSPNYNNNNYLFQNFTCNIENGEKVAIIGKSGSGKSSLIKLLLKFYEVNSGNIYIDNKNIDDIDLYTLRKNISVVPQDTILFNNTISYNIKYGNFQCTDKQMIQASIKAELHDKIMKMENKYDTIVGERGTKLSIGEKQRICIARCFLKDSKIIVLDEHASNLDNENKKAIEKALTKLCMGKTTFIITHVMENLKHMDKIIFFCGKNIYVGSHKNLMDDNHFYREYYDSKNNKML

[Multiple Choices]
A. 357..377; 397..419; 481..501; 506..526; 619..639
B. 358..373; 397..419; 481..501; 506..526; 591..611; 619..639
C. 337..357
D. 357..377; 397..419; 481..501; 506..526; 591..611; 619..639
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

> The sequence matches the UniProt record, whose historical and current annotations list all six transmembrane regions in choice D. These are computational annotations based on PROSITE-ProRule, not experimental measurements.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has hydrophobic stretches consistent with multiple membrane-spanning helices, so their approximate locations can be inferred. That does not establish the exact annotated boundaries or uniquely resolve the narrower first interval in choice B.


**Missing item-specific fact**

> The protein-specific transmembrane-region annotations, particularly the exact boundaries and whether the 591..611 region is included.


**Reason**

> The sequence supports a multi-pass membrane-protein interpretation, but selecting the precise set of coordinate intervals depends on protein-specific annotation or prediction not supplied in the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B"
]
```

> Choice B includes the same six candidate regions as D except that its first interval is narrower. Because membrane-helix boundaries are not intrinsically sharp, that interval could represent a predicted core, although D matches the cited annotation.


### Important caveats

- The supporting annotations are computational and do not establish experimental membrane-spanning boundaries.
- The annotation evidence matches the supplied sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has hydrophobic stretches consistent with multiple membrane-spanning helices, so their approximate locations can be inferred. That does not establish the exact annotated boundaries or uniquely resolve the narrower first interval in choice B.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific transmembrane-region annotations, particularly the exact boundaries and whether the 591..611 region is included.",
    "reason": "The sequence supports a multi-pass membrane-protein interpretation, but selecting the precise set of coordinate intervals depends on protein-specific annotation or prediction not supplied in the question."
  },
  "case_id": "transmembrane_0109",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the UniProt record, whose historical and current annotations list all six transmembrane regions in choice D. These are computational annotations based on PROSITE-ProRule, not experimental measurements."
  },
  "important_caveats": [
    "The supporting annotations are computational and do not establish experimental membrane-spanning boundaries.",
    "The annotation evidence matches the supplied sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B"
    ],
    "reason": "Choice B includes the same six candidate regions as D except that its first interval is narrower. Because membrane-helix boundaries are not intrinsically sharp, that interval could represent a predicted core, although D matches the cited annotation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0109",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the UniProt record, whose historical and current annotations list all six transmembrane regions in choice D. These are computational annotations based on PROSITE-ProRule, not experimental measurements.",
    "evidence_ids": ["H3", "H4", "H5", "H6", "H7", "H8"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has hydrophobic stretches consistent with multiple membrane-spanning helices, so their approximate locations can be inferred. That does not establish the exact annotated boundaries or uniquely resolve the narrower first interval in choice B.",
    "missing_item_specific_fact": "The protein-specific transmembrane-region annotations, particularly the exact boundaries and whether the 591..611 region is included.",
    "reason": "The sequence supports a multi-pass membrane-protein interpretation, but selecting the precise set of coordinate intervals depends on protein-specific annotation or prediction not supplied in the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B"],
    "reason": "Choice B includes the same six candidate regions as D except that its first interval is narrower. Because membrane-helix boundaries are not intrinsically sharp, that interval could represent a predicted core, although D matches the cited annotation."
  },
  "important_caveats": [
    "The supporting annotations are computational and do not establish experimental membrane-spanning boundaries.",
    "The annotation evidence matches the supplied sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> All six transmembrane regions in Choice D (357..377; 397..419; 481..501; 506..526; 591..611; 619..639) exactly match the UniProt annotations for Q8IDH9 (PfATM1). The annotations are computationally predicted (ECO:0000255, PROSITE-ProRule PRU00441), not experimentally determined, but they are the canonical database annotation for this entry. The sequence in the question matches the UniProt sequence (SHA-256 confirmed).

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein is an ABC transporter (ATM1/PfABCB6), whose transmembrane domain canonically contains six α-helical TM segments. This eliminates Choice C (a single TM region) and Choice A (only five TMs, missing 591..611). Between B and D, the first TM in B spans 358..373 (16 residues), which is below the ~20-residue minimum generally required for a hydrophobic α-helix to traverse the ~30 Å lipid-bilayer core, whereas D's 357..377 (21 residues) is consistent with a standard TM helix. These two arguments (6-TM ABC architecture and minimum helix length) provide concrete biological reasoning to select D.


**Missing item-specific fact**

> None strictly required. The precise single-residue boundaries (357 vs 358, 377 vs 373) fall within the inherent uncertainty of TM prediction algorithms, but the 16-vs-21-residue length difference is large enough for a general hydrophobicity-span argument to apply.


**Reason**

> General knowledge of ABC transporter topology (six TMs) and the biophysical requirement of ~20 hydrophobic residues per membrane-spanning helix provide defensible grounds to eliminate A, B, and C without recalling the specific UniProt entry. The remaining choice D is consistent with both constraints.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choice C is clearly wrong (single short TM for an ABC transporter). Choice A omits a TM region inconsistent with ABC transporter architecture. Choice B's 16-residue first TM is notably short for membrane spanning. Only D satisfies both the 6-TM requirement and the ~20-residue helix-length criterion.


### Important caveats

- The UniProt transmembrane annotations are computationally predicted (PROSITE-ProRule PRU00441), not experimentally validated by crystallography or cryo-EM.
- The exact single-residue boundaries of TM helices carry inherent uncertainty even among prediction tools; the question's distractors exploit this, but the 16-vs-21-residue gap in the B/D comparison is large enough to reason about.
- The protein is from Plasmodium falciparum (ATM1/PfABCB6), an ABC transporter involved in Fe-S cluster biogenesis; its 6-TM architecture is a family-level property, not an experimentally confirmed topology for this specific protein.
- The reviewer-only UniProt evidence was not available to the evaluated model; the reasoning above relies on general biological knowledge accessible to a trained biologist.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein is an ABC transporter (ATM1/PfABCB6), whose transmembrane domain canonically contains six α-helical TM segments. This eliminates Choice C (a single TM region) and Choice A (only five TMs, missing 591..611). Between B and D, the first TM in B spans 358..373 (16 residues), which is below the ~20-residue minimum generally required for a hydrophobic α-helix to traverse the ~30 Å lipid-bilayer core, whereas D's 357..377 (21 residues) is consistent with a standard TM helix. These two arguments (6-TM ABC architecture and minimum helix length) provide concrete biological reasoning to select D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. The precise single-residue boundaries (357 vs 358, 377 vs 373) fall within the inherent uncertainty of TM prediction algorithms, but the 16-vs-21-residue length difference is large enough for a general hydrophobicity-span argument to apply.",
    "reason": "General knowledge of ABC transporter topology (six TMs) and the biophysical requirement of ~20 hydrophobic residues per membrane-spanning helix provide defensible grounds to eliminate A, B, and C without recalling the specific UniProt entry. The remaining choice D is consistent with both constraints."
  },
  "case_id": "transmembrane_0109",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "C10",
      "H3",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8"
    ],
    "judgment": "supported",
    "reason": "All six transmembrane regions in Choice D (357..377; 397..419; 481..501; 506..526; 591..611; 619..639) exactly match the UniProt annotations for Q8IDH9 (PfATM1). The annotations are computationally predicted (ECO:0000255, PROSITE-ProRule PRU00441), not experimentally determined, but they are the canonical database annotation for this entry. The sequence in the question matches the UniProt sequence (SHA-256 confirmed)."
  },
  "important_caveats": [
    "The UniProt transmembrane annotations are computationally predicted (PROSITE-ProRule PRU00441), not experimentally validated by crystallography or cryo-EM.",
    "The exact single-residue boundaries of TM helices carry inherent uncertainty even among prediction tools; the question's distractors exploit this, but the 16-vs-21-residue gap in the B/D comparison is large enough to reason about.",
    "The protein is from Plasmodium falciparum (ATM1/PfABCB6), an ABC transporter involved in Fe-S cluster biogenesis; its 6-TM architecture is a family-level property, not an experimentally confirmed topology for this specific protein.",
    "The reviewer-only UniProt evidence was not available to the evaluated model; the reasoning above relies on general biological knowledge accessible to a trained biologist."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice C is clearly wrong (single short TM for an ABC transporter). Choice A omits a TM region inconsistent with ABC transporter architecture. Choice B's 16-residue first TM is notably short for membrane spanning. Only D satisfies both the 6-TM requirement and the ~20-residue helix-length criterion."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0109",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "All six transmembrane regions in Choice D (357..377; 397..419; 481..501; 506..526; 591..611; 619..639) exactly match the UniProt annotations for Q8IDH9 (PfATM1). The annotations are computationally predicted (ECO:0000255, PROSITE-ProRule PRU00441), not experimentally determined, but they are the canonical database annotation for this entry. The sequence in the question matches the UniProt sequence (SHA-256 confirmed).",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "H3", "H4", "H5", "H6", "H7", "H8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein is an ABC transporter (ATM1/PfABCB6), whose transmembrane domain canonically contains six α-helical TM segments. This eliminates Choice C (a single TM region) and Choice A (only five TMs, missing 591..611). Between B and D, the first TM in B spans 358..373 (16 residues), which is below the ~20-residue minimum generally required for a hydrophobic α-helix to traverse the ~30 Å lipid-bilayer core, whereas D's 357..377 (21 residues) is consistent with a standard TM helix. These two arguments (6-TM ABC architecture and minimum helix length) provide concrete biological reasoning to select D.",
    "missing_item_specific_fact": "None strictly required. The precise single-residue boundaries (357 vs 358, 377 vs 373) fall within the inherent uncertainty of TM prediction algorithms, but the 16-vs-21-residue length difference is large enough for a general hydrophobicity-span argument to apply.",
    "reason": "General knowledge of ABC transporter topology (six TMs) and the biophysical requirement of ~20 hydrophobic residues per membrane-spanning helix provide defensible grounds to eliminate A, B, and C without recalling the specific UniProt entry. The remaining choice D is consistent with both constraints."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice C is clearly wrong (single short TM for an ABC transporter). Choice A omits a TM region inconsistent with ABC transporter architecture. Choice B's 16-residue first TM is notably short for membrane spanning. Only D satisfies both the 6-TM requirement and the ~20-residue helix-length criterion."
  },
  "important_caveats": [
    "The UniProt transmembrane annotations are computationally predicted (PROSITE-ProRule PRU00441), not experimentally validated by crystallography or cryo-EM.",
    "The exact single-residue boundaries of TM helices carry inherent uncertainty even among prediction tools; the question's distractors exploit this, but the 16-vs-21-residue gap in the B/D comparison is large enough to reason about.",
    "The protein is from Plasmodium falciparum (ATM1/PfABCB6), an ABC transporter involved in Fe-S cluster biogenesis; its 6-TM architecture is a family-level property, not an experimentally confirmed topology for this specific protein.",
    "The reviewer-only UniProt evidence was not available to the evaluated model; the reasoning above relies on general biological knowledge accessible to a trained biologist."
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

**Accession:** `Q8IDH9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 148. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IDH9.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:08.625514+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"},{"evidenceCode":"ECO:0000255","id":"PRU00441","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":377},"start":{"modifier":"EXACT","value":357}},"type":"Transmembrane"}
```

Source SHA-256: `e8f2bda44f575e480dae54a87949611a9f660eeebc858da9b702318946aeef67`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IDH9.json)  
**Locator:** `/features/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:08.625514+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"},{"evidenceCode":"ECO:0000255","id":"PRU00441","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":419},"start":{"modifier":"EXACT","value":397}},"type":"Transmembrane"}
```

Source SHA-256: `e8f2bda44f575e480dae54a87949611a9f660eeebc858da9b702318946aeef67`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IDH9.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:08.625514+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"},{"evidenceCode":"ECO:0000255","id":"PRU00441","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":501},"start":{"modifier":"EXACT","value":481}},"type":"Transmembrane"}
```

Source SHA-256: `e8f2bda44f575e480dae54a87949611a9f660eeebc858da9b702318946aeef67`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IDH9.json)  
**Locator:** `/features/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:08.625514+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"},{"evidenceCode":"ECO:0000255","id":"PRU00441","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":526},"start":{"modifier":"EXACT","value":506}},"type":"Transmembrane"}
```

Source SHA-256: `e8f2bda44f575e480dae54a87949611a9f660eeebc858da9b702318946aeef67`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IDH9.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:08.625514+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"},{"evidenceCode":"ECO:0000255","id":"PRU00441","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":611},"start":{"modifier":"EXACT","value":591}},"type":"Transmembrane"}
```

Source SHA-256: `e8f2bda44f575e480dae54a87949611a9f660eeebc858da9b702318946aeef67`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IDH9.json)  
**Locator:** `/features/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:08.625514+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"},{"evidenceCode":"ECO:0000255","id":"PRU00441","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":639},"start":{"modifier":"EXACT","value":619}},"type":"Transmembrane"}
```

Source SHA-256: `e8f2bda44f575e480dae54a87949611a9f660eeebc858da9b702318946aeef67`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IDH9?format=txt&versions=148)  
**Locator:** `lines 155-158`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 148 / 1.  
**Retrieved:** 2026-11-02T04:32:10.963943+00:00.  

```text
FT   TRANSMEM        357..377
FT                   /note="Helical"
FT                   /evidence="ECO:0000255, ECO:0000255|PROSITE-
FT                   ProRule:PRU00441"
```

Source SHA-256: `ecc9fb1303c91e20ea222fee968f93a70954dff7b257572b63e18f4fe50795bb`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IDH9?format=txt&versions=148)  
**Locator:** `lines 159-162`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 148 / 1.  
**Retrieved:** 2026-11-02T04:32:10.963943+00:00.  

```text
FT   TRANSMEM        397..419
FT                   /note="Helical"
FT                   /evidence="ECO:0000255, ECO:0000255|PROSITE-
FT                   ProRule:PRU00441"
```

Source SHA-256: `ecc9fb1303c91e20ea222fee968f93a70954dff7b257572b63e18f4fe50795bb`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IDH9?format=txt&versions=148)  
**Locator:** `lines 163-166`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 148 / 1.  
**Retrieved:** 2026-11-02T04:32:10.963943+00:00.  

```text
FT   TRANSMEM        481..501
FT                   /note="Helical"
FT                   /evidence="ECO:0000255, ECO:0000255|PROSITE-
FT                   ProRule:PRU00441"
```

Source SHA-256: `ecc9fb1303c91e20ea222fee968f93a70954dff7b257572b63e18f4fe50795bb`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IDH9?format=txt&versions=148)  
**Locator:** `lines 167-170`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 148 / 1.  
**Retrieved:** 2026-11-02T04:32:10.963943+00:00.  

```text
FT   TRANSMEM        506..526
FT                   /note="Helical"
FT                   /evidence="ECO:0000255, ECO:0000255|PROSITE-
FT                   ProRule:PRU00441"
```

Source SHA-256: `ecc9fb1303c91e20ea222fee968f93a70954dff7b257572b63e18f4fe50795bb`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IDH9?format=txt&versions=148)  
**Locator:** `lines 171-174`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 148 / 1.  
**Retrieved:** 2026-11-02T04:32:10.963943+00:00.  

```text
FT   TRANSMEM        591..611
FT                   /note="Helical"
FT                   /evidence="ECO:0000255, ECO:0000255|PROSITE-
FT                   ProRule:PRU00441"
```

Source SHA-256: `ecc9fb1303c91e20ea222fee968f93a70954dff7b257572b63e18f4fe50795bb`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IDH9?format=txt&versions=148)  
**Locator:** `lines 175-178`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 148 / 1.  
**Retrieved:** 2026-11-02T04:32:10.963943+00:00.  

```text
FT   TRANSMEM        619..639
FT                   /note="Helical"
FT                   /evidence="ECO:0000255, ECO:0000255|PROSITE-
FT                   ProRule:PRU00441"
```

Source SHA-256: `ecc9fb1303c91e20ea222fee968f93a70954dff7b257572b63e18f4fe50795bb`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 109. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
