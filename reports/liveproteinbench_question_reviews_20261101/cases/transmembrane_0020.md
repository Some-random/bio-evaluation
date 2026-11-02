# transmembrane_0020

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **D** — 48..68; 83..103; 121..141; 145..165; 171..191; 203..223; 236..256; 269..289; 298..318; 336..356; 374..394; 403..423; 438..460; 516..536

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MQTATALEDSANAPSPAASSQGQFDREIVPIDTADAGNSTKRSPLKVALIMVALCCAVFLHALDNTIITTALPTITAAFDLDAAYTWIGSTYLLAVAASTMVWAKISDVFGRKPIILSANLCFFTGSLIAALSANFAMLIAARAIQGIGGAGVNVLANICVGDLFSQRKRGLYYGVIGGVWAVALSLGPVVGGSLTESISWRWCFYINLPLCAVVFVIIILLLDVKTPKTPFGKGIAAIDWVGAALSIGSTLMILLALSLGGQTEPWNSATVICLVVFGFIGWILCFSWEASLAKYPLLPVSIFKQIPTLAVLAACFIQSYAFVASAYYLPLYFQAVLGATPILSGVYLLPTAVSISISSTATGVYMRKTGQYLTPIYIGFVLQTLGYGLFIDLGPTANWAKIIVFQIIGGLGVGFNFQAPMVALQAFISPRELAMATSAYNFMRNVSGAISVVIGQTVFQNEMSKHQESLATILGPQLAAKLAGTGASASTDLIRSLPSPQRDVVHGVFANSMKSMWIMYTAFSAAALVVCPFLGKMVLREDHTETVTGLAAENAAREERLRQEKEKKDAKIRKCQVN

[Multiple Choices]
A. 48..68; 83..103; 121..141; 171..191; 203..223; 236..256; 269..289; 298..318; 336..356; 374..394; 403..423; 438..460; 516..536
B. 1..21
C. 48..68; 83..103; 121..141; 145..165; 171..191; 203..223; 236..256; 269..289; 298..318; 336..356; 374..394; 401..421; 438..460; 516..536
D. 48..68; 83..103; 121..141; 145..165; 171..191; 203..223; 236..256; 269..289; 298..318; 336..356; 374..394; 403..423; 438..460; 516..536
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

> The sequence-matched UniProt record annotates the transmembrane regions listed in D, including 145..165 and 403..423. These are computational annotations (ECO:0000255), not evidence of experimental determination of the exact boundaries.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [C13](#evidence-c13), [C14](#evidence-c14), [C15](#evidence-c15), [C16](#evidence-c16), [C17](#evidence-c17), [C18](#evidence-c18).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The long sequence contains many hydrophobic stretches and is consistent with a multi-pass membrane transporter, so broad transmembrane topology is inferable. That does not establish these precise coordinates or resolve the near-identical 401..421 versus 403..423 alternatives.


**Missing item-specific fact**

> The protein-specific transmembrane-region annotation, including whether to include 145..165 and the chosen endpoints around 403..423.


**Reason**

> The choices differ in specific predicted boundaries and inclusion of a particular helix. Those details are not uniquely determined by general membrane-protein reasoning from the sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> C and D differ only by a two-residue shift for one predicted helix. Both describe essentially the same hydrophobic segment as a likely membrane-spanning helix; the wording provides no boundary convention that makes those exact endpoints biologically distinct.


### Important caveats

- The supporting UniProt feature evidence is computational; it does not establish experimentally measured helix boundaries.
- The reviewer-only sequence-matched record supports D, but that annotation was not supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long sequence contains many hydrophobic stretches and is consistent with a multi-pass membrane transporter, so broad transmembrane topology is inferable. That does not establish these precise coordinates or resolve the near-identical 401..421 versus 403..423 alternatives.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific transmembrane-region annotation, including whether to include 145..165 and the chosen endpoints around 403..423.",
    "reason": "The choices differ in specific predicted boundaries and inclusion of a particular helix. Those details are not uniquely determined by general membrane-protein reasoning from the sequence."
  },
  "case_id": "transmembrane_0020",
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
      "C16",
      "C17",
      "C18"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the transmembrane regions listed in D, including 145..165 and 403..423. These are computational annotations (ECO:0000255), not evidence of experimental determination of the exact boundaries."
  },
  "important_caveats": [
    "The supporting UniProt feature evidence is computational; it does not establish experimentally measured helix boundaries.",
    "The reviewer-only sequence-matched record supports D, but that annotation was not supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "C and D differ only by a two-residue shift for one predicted helix. Both describe essentially the same hydrophobic segment as a likely membrane-spanning helix; the wording provides no boundary convention that makes those exact endpoints biologically distinct."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0020",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the transmembrane regions listed in D, including 145..165 and 403..423. These are computational annotations (ECO:0000255), not evidence of experimental determination of the exact boundaries.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "C14", "C15", "C16", "C17", "C18"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The long sequence contains many hydrophobic stretches and is consistent with a multi-pass membrane transporter, so broad transmembrane topology is inferable. That does not establish these precise coordinates or resolve the near-identical 401..421 versus 403..423 alternatives.",
    "missing_item_specific_fact": "The protein-specific transmembrane-region annotation, including whether to include 145..165 and the chosen endpoints around 403..423.",
    "reason": "The choices differ in specific predicted boundaries and inclusion of a particular helix. Those details are not uniquely determined by general membrane-protein reasoning from the sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "C and D differ only by a two-residue shift for one predicted helix. Both describe essentially the same hydrophobic segment as a likely membrane-spanning helix; the wording provides no boundary convention that makes those exact endpoints biologically distinct."
  },
  "important_caveats": [
    "The supporting UniProt feature evidence is computational; it does not establish experimentally measured helix boundaries.",
    "The reviewer-only sequence-matched record supports D, but that annotation was not supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> Option D (48..68; 83..103; 121..141; 145..165; 171..191; 203..223; 236..256; 269..289; 298..318; 336..356; 374..394; 403..423; 438..460; 516..536) exactly matches all 14 transmembrane helix annotations in UniProt entry A0A455ZIM6 (Swiss-Prot, PPZ2_METMF). Each region is confirmed by evidence IDs C5-C18 and H4-H17 with ECO:0000255 (inferred by similarity). The sequence match is exact (SHA-256 identical, 579 AA). Note the annotation is computational (ECO:0000255), not experimental.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [C13](#evidence-c13), [C14](#evidence-c14), [C15](#evidence-c15), [C16](#evidence-c16), [C17](#evidence-c17), [C18](#evidence-c18), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11), [H12](#evidence-h12), [H13](#evidence-h13), [H14](#evidence-h14), [H15](#evidence-h15), [H16](#evidence-h16), [H17](#evidence-h17).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A model could potentially identify the hydrophobic stretch at 145-165 (distinguishing A from C/D) by examining the sequence between TM helices at 121-141 and 171-191, and could identify that option B (1..21) is trivially wrong. However, the critical distinction between C and D is a 2-residue shift in the 12th TM boundary (401..421 vs 403..423). Both represent essentially the same hydrophobic helix; the exact start/end of a TM helix within a broad hydrophobic stretch is at the resolution limit of any sequence-based method and cannot be meaningfully resolved by general biological reasoning. Additionally, the precise boundaries of all 14 TM regions (e.g., whether TM1 starts at 48 vs 47, whether TM13 is 438..460 vs 437..459) are prediction-tool-dependent.


**Missing item-specific fact**

> The exact TM boundary assignments from the specific computational prediction pipeline used by UniProt (ECO:0000255, inferred by similarity). The 2-residue shift between options C and D at the 12th TM is indistinguishable by hydrophobicity analysis or general topology reasoning; it requires knowledge of the specific annotation or identical prediction tool output.


**Reason**

> While a skilled model could narrow the answer to C or D by identifying the 145-165 TM and rejecting A and B, the final C-vs-D distinction (401..421 vs 403..423) is a 2-residue boundary shift within a hydrophobic helix that no amount of general biological reasoning can resolve. It depends on the specific annotation entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> Options C and D differ by only 2 residues at one TM boundary (401..421 vs 403..423). Both describe the same 14-TM topology with nearly identical helix boundaries. In practice, any TM prediction tool could assign either boundary depending on the hydrophobicity threshold used. Without the exact annotation, both are equally defensible descriptions of the protein's membrane topology.


### Important caveats

- All TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred from homologous proteins, not experimentally determined boundaries.
- The annotation was first released in UniProtKB/Swiss-Prot on 2025-02-05; the author's source snapshot date is unknown but the sequence version (v1, dated 2019-06-05) matches.
- MFS transporters canonically have 12 TM helices; this entry annotates 14, which may reflect additional helices beyond the canonical MFS fold or a prediction artifact.
- The 2-residue boundary distinction between C and D is well within the typical ±3-5 residue uncertainty of TM prediction tools, making this a very fine-grained discrimination.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A model could potentially identify the hydrophobic stretch at 145-165 (distinguishing A from C/D) by examining the sequence between TM helices at 121-141 and 171-191, and could identify that option B (1..21) is trivially wrong. However, the critical distinction between C and D is a 2-residue shift in the 12th TM boundary (401..421 vs 403..423). Both represent essentially the same hydrophobic helix; the exact start/end of a TM helix within a broad hydrophobic stretch is at the resolution limit of any sequence-based method and cannot be meaningfully resolved by general biological reasoning. Additionally, the precise boundaries of all 14 TM regions (e.g., whether TM1 starts at 48 vs 47, whether TM13 is 438..460 vs 437..459) are prediction-tool-dependent.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact TM boundary assignments from the specific computational prediction pipeline used by UniProt (ECO:0000255, inferred by similarity). The 2-residue shift between options C and D at the 12th TM is indistinguishable by hydrophobicity analysis or general topology reasoning; it requires knowledge of the specific annotation or identical prediction tool output.",
    "reason": "While a skilled model could narrow the answer to C or D by identifying the 145-165 TM and rejecting A and B, the final C-vs-D distinction (401..421 vs 403..423) is a 2-residue boundary shift within a hydrophobic helix that no amount of general biological reasoning can resolve. It depends on the specific annotation entry."
  },
  "case_id": "transmembrane_0020",
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
      "C16",
      "C17",
      "C18",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9",
      "H10",
      "H11",
      "H12",
      "H13",
      "H14",
      "H15",
      "H16",
      "H17"
    ],
    "judgment": "supported",
    "reason": "Option D (48..68; 83..103; 121..141; 145..165; 171..191; 203..223; 236..256; 269..289; 298..318; 336..356; 374..394; 403..423; 438..460; 516..536) exactly matches all 14 transmembrane helix annotations in UniProt entry A0A455ZIM6 (Swiss-Prot, PPZ2_METMF). Each region is confirmed by evidence IDs C5-C18 and H4-H17 with ECO:0000255 (inferred by similarity). The sequence match is exact (SHA-256 identical, 579 AA). Note the annotation is computational (ECO:0000255), not experimental."
  },
  "important_caveats": [
    "All TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred from homologous proteins, not experimentally determined boundaries.",
    "The annotation was first released in UniProtKB/Swiss-Prot on 2025-02-05; the author's source snapshot date is unknown but the sequence version (v1, dated 2019-06-05) matches.",
    "MFS transporters canonically have 12 TM helices; this entry annotates 14, which may reflect additional helices beyond the canonical MFS fold or a prediction artifact.",
    "The 2-residue boundary distinction between C and D is well within the typical ±3-5 residue uncertainty of TM prediction tools, making this a very fine-grained discrimination."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "Options C and D differ by only 2 residues at one TM boundary (401..421 vs 403..423). Both describe the same 14-TM topology with nearly identical helix boundaries. In practice, any TM prediction tool could assign either boundary depending on the hydrophobicity threshold used. Without the exact annotation, both are equally defensible descriptions of the protein's membrane topology."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0020",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "Option D (48..68; 83..103; 121..141; 145..165; 171..191; 203..223; 236..256; 269..289; 298..318; 336..356; 374..394; 403..423; 438..460; 516..536) exactly matches all 14 transmembrane helix annotations in UniProt entry A0A455ZIM6 (Swiss-Prot, PPZ2_METMF). Each region is confirmed by evidence IDs C5-C18 and H4-H17 with ECO:0000255 (inferred by similarity). The sequence match is exact (SHA-256 identical, 579 AA). Note the annotation is computational (ECO:0000255), not experimental.",
    "evidence_ids": ["C5","C6","C7","C8","C9","C10","C11","C12","C13","C14","C15","C16","C17","C18","H4","H5","H6","H7","H8","H9","H10","H11","H12","H13","H14","H15","H16","H17"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A model could potentially identify the hydrophobic stretch at 145-165 (distinguishing A from C/D) by examining the sequence between TM helices at 121-141 and 171-191, and could identify that option B (1..21) is trivially wrong. However, the critical distinction between C and D is a 2-residue shift in the 12th TM boundary (401..421 vs 403..423). Both represent essentially the same hydrophobic helix; the exact start/end of a TM helix within a broad hydrophobic stretch is at the resolution limit of any sequence-based method and cannot be meaningfully resolved by general biological reasoning. Additionally, the precise boundaries of all 14 TM regions (e.g., whether TM1 starts at 48 vs 47, whether TM13 is 438..460 vs 437..459) are prediction-tool-dependent.",
    "missing_item_specific_fact": "The exact TM boundary assignments from the specific computational prediction pipeline used by UniProt (ECO:0000255, inferred by similarity). The 2-residue shift between options C and D at the 12th TM is indistinguishable by hydrophobicity analysis or general topology reasoning; it requires knowledge of the specific annotation or identical prediction tool output.",
    "reason": "While a skilled model could narrow the answer to C or D by identifying the 145-165 TM and rejecting A and B, the final C-vs-D distinction (401..421 vs 403..423) is a 2-residue boundary shift within a hydrophobic helix that no amount of general biological reasoning can resolve. It depends on the specific annotation entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "Options C and D differ by only 2 residues at one TM boundary (401..421 vs 403..423). Both describe the same 14-TM topology with nearly identical helix boundaries. In practice, any TM prediction tool could assign either boundary depending on the hydrophobicity threshold used. Without the exact annotation, both are equally defensible descriptions of the protein's membrane topology."
  },
  "important_caveats": [
    "All TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred from homologous proteins, not experimentally determined boundaries.",
    "The annotation was first released in UniProtKB/Swiss-Prot on 2025-02-05; the author's source snapshot date is unknown but the sequence version (v1, dated 2019-06-05) matches.",
    "MFS transporters canonically have 12 TM helices; this entry annotates 14, which may reflect additional helices beyond the canonical MFS fold or a prediction artifact.",
    "The 2-residue boundary distinction between C and D is well within the typical ±3-5 residue uncertainty of TM prediction tools, making this a very fine-grained discrimination."
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

**Accession:** `A0A455ZIM6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 20. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:13.201191+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":68},"start":{"modifier":"EXACT","value":48}},"type":"Transmembrane"}
```

Source SHA-256: `6f7707827365d1a1ffe9a48a865bb8667232a501e75af8734df730c3b24d6d20`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:13.201191+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":103},"start":{"modifier":"EXACT","value":83}},"type":"Transmembrane"}
```

Source SHA-256: `6f7707827365d1a1ffe9a48a865bb8667232a501e75af8734df730c3b24d6d20`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json)  
**Locator:** `/features/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:13.201191+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":141},"start":{"modifier":"EXACT","value":121}},"type":"Transmembrane"}
```

Source SHA-256: `6f7707827365d1a1ffe9a48a865bb8667232a501e75af8734df730c3b24d6d20`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:13.201191+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":165},"start":{"modifier":"EXACT","value":145}},"type":"Transmembrane"}
```

Source SHA-256: `6f7707827365d1a1ffe9a48a865bb8667232a501e75af8734df730c3b24d6d20`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json)  
**Locator:** `/features/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:13.201191+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":191},"start":{"modifier":"EXACT","value":171}},"type":"Transmembrane"}
```

Source SHA-256: `6f7707827365d1a1ffe9a48a865bb8667232a501e75af8734df730c3b24d6d20`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:13.201191+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":223},"start":{"modifier":"EXACT","value":203}},"type":"Transmembrane"}
```

Source SHA-256: `6f7707827365d1a1ffe9a48a865bb8667232a501e75af8734df730c3b24d6d20`.

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json)  
**Locator:** `/features/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:13.201191+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":256},"start":{"modifier":"EXACT","value":236}},"type":"Transmembrane"}
```

Source SHA-256: `6f7707827365d1a1ffe9a48a865bb8667232a501e75af8734df730c3b24d6d20`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json)  
**Locator:** `/features/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:13.201191+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":289},"start":{"modifier":"EXACT","value":269}},"type":"Transmembrane"}
```

Source SHA-256: `6f7707827365d1a1ffe9a48a865bb8667232a501e75af8734df730c3b24d6d20`.

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json)  
**Locator:** `/features/9`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:13.201191+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":318},"start":{"modifier":"EXACT","value":298}},"type":"Transmembrane"}
```

Source SHA-256: `6f7707827365d1a1ffe9a48a865bb8667232a501e75af8734df730c3b24d6d20`.

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json)  
**Locator:** `/features/10`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:13.201191+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":356},"start":{"modifier":"EXACT","value":336}},"type":"Transmembrane"}
```

Source SHA-256: `6f7707827365d1a1ffe9a48a865bb8667232a501e75af8734df730c3b24d6d20`.

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json)  
**Locator:** `/features/11`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:13.201191+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":394},"start":{"modifier":"EXACT","value":374}},"type":"Transmembrane"}
```

Source SHA-256: `6f7707827365d1a1ffe9a48a865bb8667232a501e75af8734df730c3b24d6d20`.

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json)  
**Locator:** `/features/12`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:13.201191+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":423},"start":{"modifier":"EXACT","value":403}},"type":"Transmembrane"}
```

Source SHA-256: `6f7707827365d1a1ffe9a48a865bb8667232a501e75af8734df730c3b24d6d20`.

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json)  
**Locator:** `/features/13`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:13.201191+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":460},"start":{"modifier":"EXACT","value":438}},"type":"Transmembrane"}
```

Source SHA-256: `6f7707827365d1a1ffe9a48a865bb8667232a501e75af8734df730c3b24d6d20`.

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json)  
**Locator:** `/features/14`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:13.201191+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":536},"start":{"modifier":"EXACT","value":516}},"type":"Transmembrane"}
```

Source SHA-256: `6f7707827365d1a1ffe9a48a865bb8667232a501e75af8734df730c3b24d6d20`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20)  
**Locator:** `lines 67-69`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 20 / 1.  
**Retrieved:** 2026-11-02T04:25:15.261809+00:00.  

```text
FT   TRANSMEM        48..68
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `05abb0d30f13abffa1cbfd065ad8e5fdc4d8e89d823d113602496d99dc707e15`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20)  
**Locator:** `lines 70-72`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 20 / 1.  
**Retrieved:** 2026-11-02T04:25:15.261809+00:00.  

```text
FT   TRANSMEM        83..103
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `05abb0d30f13abffa1cbfd065ad8e5fdc4d8e89d823d113602496d99dc707e15`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20)  
**Locator:** `lines 73-75`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 20 / 1.  
**Retrieved:** 2026-11-02T04:25:15.261809+00:00.  

```text
FT   TRANSMEM        121..141
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `05abb0d30f13abffa1cbfd065ad8e5fdc4d8e89d823d113602496d99dc707e15`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20)  
**Locator:** `lines 76-78`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 20 / 1.  
**Retrieved:** 2026-11-02T04:25:15.261809+00:00.  

```text
FT   TRANSMEM        145..165
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `05abb0d30f13abffa1cbfd065ad8e5fdc4d8e89d823d113602496d99dc707e15`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20)  
**Locator:** `lines 79-81`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 20 / 1.  
**Retrieved:** 2026-11-02T04:25:15.261809+00:00.  

```text
FT   TRANSMEM        171..191
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `05abb0d30f13abffa1cbfd065ad8e5fdc4d8e89d823d113602496d99dc707e15`.

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20)  
**Locator:** `lines 82-84`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 20 / 1.  
**Retrieved:** 2026-11-02T04:25:15.261809+00:00.  

```text
FT   TRANSMEM        203..223
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `05abb0d30f13abffa1cbfd065ad8e5fdc4d8e89d823d113602496d99dc707e15`.

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20)  
**Locator:** `lines 85-87`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 20 / 1.  
**Retrieved:** 2026-11-02T04:25:15.261809+00:00.  

```text
FT   TRANSMEM        236..256
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `05abb0d30f13abffa1cbfd065ad8e5fdc4d8e89d823d113602496d99dc707e15`.

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20)  
**Locator:** `lines 88-90`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 20 / 1.  
**Retrieved:** 2026-11-02T04:25:15.261809+00:00.  

```text
FT   TRANSMEM        269..289
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `05abb0d30f13abffa1cbfd065ad8e5fdc4d8e89d823d113602496d99dc707e15`.

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20)  
**Locator:** `lines 91-93`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 20 / 1.  
**Retrieved:** 2026-11-02T04:25:15.261809+00:00.  

```text
FT   TRANSMEM        298..318
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `05abb0d30f13abffa1cbfd065ad8e5fdc4d8e89d823d113602496d99dc707e15`.

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20)  
**Locator:** `lines 94-96`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 20 / 1.  
**Retrieved:** 2026-11-02T04:25:15.261809+00:00.  

```text
FT   TRANSMEM        336..356
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `05abb0d30f13abffa1cbfd065ad8e5fdc4d8e89d823d113602496d99dc707e15`.

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20)  
**Locator:** `lines 97-99`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 20 / 1.  
**Retrieved:** 2026-11-02T04:25:15.261809+00:00.  

```text
FT   TRANSMEM        374..394
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `05abb0d30f13abffa1cbfd065ad8e5fdc4d8e89d823d113602496d99dc707e15`.

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20)  
**Locator:** `lines 100-102`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 20 / 1.  
**Retrieved:** 2026-11-02T04:25:15.261809+00:00.  

```text
FT   TRANSMEM        403..423
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `05abb0d30f13abffa1cbfd065ad8e5fdc4d8e89d823d113602496d99dc707e15`.

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20)  
**Locator:** `lines 103-105`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 20 / 1.  
**Retrieved:** 2026-11-02T04:25:15.261809+00:00.  

```text
FT   TRANSMEM        438..460
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `05abb0d30f13abffa1cbfd065ad8e5fdc4d8e89d823d113602496d99dc707e15`.

### Evidence H17

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20)  
**Locator:** `lines 106-108`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 20 / 1.  
**Retrieved:** 2026-11-02T04:25:15.261809+00:00.  

```text
FT   TRANSMEM        516..536
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `05abb0d30f13abffa1cbfd065ad8e5fdc4d8e89d823d113602496d99dc707e15`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 20. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
