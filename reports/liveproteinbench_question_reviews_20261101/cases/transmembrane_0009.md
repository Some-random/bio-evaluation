# transmembrane_0009

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **D** — 14..34; 47..67; 72..92; 121..141; 161..181

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTSHHSWYRYSINPFVLMGLVALFLAATANLTFFEKAMAVYPVSDNLGFIISMAVAVMGAMLLIVVLLSYRYVLKPVLILLLIMGAVTSYFTDTYGTVYDTTMLQNAMQTDQAESKDLMNLAFFVRIIGLGVLPSVLVAVAKVNYPTWGKGLIQRAMTWGVSLVLLLVPIGLFSSQYASFFRVHKPVRFYINPITPIYSVGKLASIEYKKATAPTDTIYHAKDAVQTTKPSERKPRLVVFVVGETARADHVQFNGYGRETFPQLAKVDGLANFSQVTSCGTSTAYSVPCMFSYLGQDDYDVDTAKYQENVLDTLDRLGVGILWRDNNSDSKGVMDKLPATQYFDYKSATNNTICNTNPYNECRDVGMLVGLDDYVSANNGKDMLIMLHQMGNHGPAYFKRYDEQFAKFTPVCEGNELAKCEHQSLINAYDNALLATDDFIAKSIDWLKTHEANYDVAMLYVSDHGESLGENGVYLHGMPNAFAPKEQRAVPAFFWSNNTTFKPTASDTVLTHDAITPTLLKLFDVTAGKVKDRAAFIQ

[Multiple Choices]
A. 14..34; 47..67; 72..92; 121..141
B. 30..50; 62..82; 108..128; 144..164; 186..206; 327..347; 357..377
C. 14..34; 47..67; 72..92; 122..141; 161..181
D. 14..34; 47..67; 72..92; 121..141; 161..181
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

> The sequence-matched UniProt entry annotates all five regions in D as transmembrane helices, including in the historical record. These annotations are computational (ECO:0000255), not direct experimental confirmation of the boundaries.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has several conspicuously hydrophobic stretches, supporting the broad inference that its N-terminal region contains membrane-spanning helices.


**Missing item-specific fact**

> Distinguishing the exact annotated coordinates—especially the 121 versus 122 start and the inclusion of the 161–181 segment—requires protein-specific boundary annotations or an equivalent prediction not supplied in the question.


**Reason**

> General sequence inspection supports broad hydrophobic segments but does not reliably establish exact residue boundaries. The supplied sequence alone does not provide a decisive basis for the one-residue boundary distinction between C and D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> C and D differ only in whether the fourth segment begins at residue 122 or 121. Both describe essentially the same hydrophobic span; the supplied input gives no clear biological basis for preferring that one-residue boundary.


### Important caveats

- The reviewer-only UniProt evidence matches the supplied sequence, but the exact source snapshot used by the author is unknown.
- The cited structural evidence concerns residues 215–538 and does not experimentally establish the N-terminal transmembrane boundaries.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has several conspicuously hydrophobic stretches, supporting the broad inference that its N-terminal region contains membrane-spanning helices.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Distinguishing the exact annotated coordinates—especially the 121 versus 122 start and the inclusion of the 161–181 segment—requires protein-specific boundary annotations or an equivalent prediction not supplied in the question.",
    "reason": "General sequence inspection supports broad hydrophobic segments but does not reliably establish exact residue boundaries. The supplied sequence alone does not provide a decisive basis for the one-residue boundary distinction between C and D."
  },
  "case_id": "transmembrane_0009",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "H3",
      "H4",
      "H5",
      "H6",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates all five regions in D as transmembrane helices, including in the historical record. These annotations are computational (ECO:0000255), not direct experimental confirmation of the boundaries."
  },
  "important_caveats": [
    "The reviewer-only UniProt evidence matches the supplied sequence, but the exact source snapshot used by the author is unknown.",
    "The cited structural evidence concerns residues 215–538 and does not experimentally establish the N-terminal transmembrane boundaries."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "C and D differ only in whether the fourth segment begins at residue 122 or 121. Both describe essentially the same hydrophobic span; the supplied input gives no clear biological basis for preferring that one-residue boundary."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0009",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates all five regions in D as transmembrane helices, including in the historical record. These annotations are computational (ECO:0000255), not direct experimental confirmation of the boundaries.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "H3", "H4", "H5", "H6", "H7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has several conspicuously hydrophobic stretches, supporting the broad inference that its N-terminal region contains membrane-spanning helices.",
    "missing_item_specific_fact": "Distinguishing the exact annotated coordinates—especially the 121 versus 122 start and the inclusion of the 161–181 segment—requires protein-specific boundary annotations or an equivalent prediction not supplied in the question.",
    "reason": "General sequence inspection supports broad hydrophobic segments but does not reliably establish exact residue boundaries. The supplied sequence alone does not provide a decisive basis for the one-residue boundary distinction between C and D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "C and D differ only in whether the fourth segment begins at residue 122 or 121. Both describe essentially the same hydrophobic span; the supplied input gives no clear biological basis for preferring that one-residue boundary."
  },
  "important_caveats": [
    "The reviewer-only UniProt evidence matches the supplied sequence, but the exact source snapshot used by the author is unknown.",
    "The cited structural evidence concerns residues 215–538 and does not experimentally establish the N-terminal transmembrane boundaries."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A1C3NEV1 (MCR-2, E. coli) annotates exactly five transmembrane helical regions at 14..34, 47..67, 72..92, 121..141, and 161..181 (evidence_ids C5-C9, H3-H7), matching choice D precisely. The sequence matches the benchmark input. However, the evidence code is ECO:0000255 (by similarity), indicating these are computational predictions transferred by homology, not experimentally determined boundaries. The X-ray crystallography data (PDB 6A7W) covers only residues 215-538, so the TM regions are not directly validated experimentally.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A model can identify approximately five hydrophobic stretches of ~20 residues (distinguishing D from A which omits the fifth TM at 161-181, and from B which has entirely wrong positions). However, the critical distinction between D (121..141) and C (122..141) hinges on a single-residue boundary: position 121 is Leucine (hydrophobic) and position 122 is Alanine (also hydrophobic). Both are clearly hydrophobic residues, and no general biological principle definitively determines whether a TM helix boundary falls at 121 or 122. The weak argument that position 120 is Asparagine (polar) so the helix 'starts' at 121 is within the noise of any TM prediction algorithm.


**Missing item-specific fact**

> The exact residue-level boundary output of the specific prediction algorithm (or homology transfer) used to generate the UniProt annotation, which determines whether the fourth TM helix starts at residue 121 or 122. This is an item-specific computational prediction artifact not derivable from general biology.


**Reason**

> While the number of TM regions (~5) and their approximate locations can be inferred from hydrophobicity analysis, the precise single-residue boundary distinguishing the correct answer D from the closest distractor C (121 vs 122) cannot be resolved by biological reasoning. Both L and A are hydrophobic; the boundary is an algorithmic artifact of the prediction method used for annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> The only difference between C and D is whether the fourth TM helix starts at 121 (L) or 122 (A). Both residues are hydrophobic and either could reasonably be considered the start of a TM helix. Without knowing the specific prediction algorithm's output, both boundaries are defensible from a hydrophobicity standpoint. The annotation evidence code (ECO:0000255, by similarity) confirms these are computational predictions, not experimental measurements.


### Important caveats

- All TM annotations carry evidence code ECO:0000255 (by similarity), meaning they are computational predictions transferred from homologous proteins, not experimentally determined boundaries.
- The X-ray structure (PDB 6A7W) covers residues 215-538 only; the TM regions (all <215) are not covered by experimental structural data.
- The distinction between choices C and D is a single-residue boundary difference (121 vs 122) that falls within the uncertainty of any TM prediction method.
- The reviewer-only UniProt accession was inferred from dataset metadata and was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A model can identify approximately five hydrophobic stretches of ~20 residues (distinguishing D from A which omits the fifth TM at 161-181, and from B which has entirely wrong positions). However, the critical distinction between D (121..141) and C (122..141) hinges on a single-residue boundary: position 121 is Leucine (hydrophobic) and position 122 is Alanine (also hydrophobic). Both are clearly hydrophobic residues, and no general biological principle definitively determines whether a TM helix boundary falls at 121 or 122. The weak argument that position 120 is Asparagine (polar) so the helix 'starts' at 121 is within the noise of any TM prediction algorithm.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact residue-level boundary output of the specific prediction algorithm (or homology transfer) used to generate the UniProt annotation, which determines whether the fourth TM helix starts at residue 121 or 122. This is an item-specific computational prediction artifact not derivable from general biology.",
    "reason": "While the number of TM regions (~5) and their approximate locations can be inferred from hydrophobicity analysis, the precise single-residue boundary distinguishing the correct answer D from the closest distractor C (121 vs 122) cannot be resolved by biological reasoning. Both L and A are hydrophobic; the boundary is an algorithmic artifact of the prediction method used for annotation."
  },
  "case_id": "transmembrane_0009",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "H3",
      "H4",
      "H5",
      "H6",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A1C3NEV1 (MCR-2, E. coli) annotates exactly five transmembrane helical regions at 14..34, 47..67, 72..92, 121..141, and 161..181 (evidence_ids C5-C9, H3-H7), matching choice D precisely. The sequence matches the benchmark input. However, the evidence code is ECO:0000255 (by similarity), indicating these are computational predictions transferred by homology, not experimentally determined boundaries. The X-ray crystallography data (PDB 6A7W) covers only residues 215-538, so the TM regions are not directly validated experimentally."
  },
  "important_caveats": [
    "All TM annotations carry evidence code ECO:0000255 (by similarity), meaning they are computational predictions transferred from homologous proteins, not experimentally determined boundaries.",
    "The X-ray structure (PDB 6A7W) covers residues 215-538 only; the TM regions (all <215) are not covered by experimental structural data.",
    "The distinction between choices C and D is a single-residue boundary difference (121 vs 122) that falls within the uncertainty of any TM prediction method.",
    "The reviewer-only UniProt accession was inferred from dataset metadata and was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "The only difference between C and D is whether the fourth TM helix starts at 121 (L) or 122 (A). Both residues are hydrophobic and either could reasonably be considered the start of a TM helix. Without knowing the specific prediction algorithm's output, both boundaries are defensible from a hydrophobicity standpoint. The annotation evidence code (ECO:0000255, by similarity) confirms these are computational predictions, not experimental measurements."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0009",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A1C3NEV1 (MCR-2, E. coli) annotates exactly five transmembrane helical regions at 14..34, 47..67, 72..92, 121..141, and 161..181 (evidence_ids C5-C9, H3-H7), matching choice D precisely. The sequence matches the benchmark input. However, the evidence code is ECO:0000255 (by similarity), indicating these are computational predictions transferred by homology, not experimentally determined boundaries. The X-ray crystallography data (PDB 6A7W) covers only residues 215-538, so the TM regions are not directly validated experimentally.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "H3", "H4", "H5", "H6", "H7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A model can identify approximately five hydrophobic stretches of ~20 residues (distinguishing D from A which omits the fifth TM at 161-181, and from B which has entirely wrong positions). However, the critical distinction between D (121..141) and C (122..141) hinges on a single-residue boundary: position 121 is Leucine (hydrophobic) and position 122 is Alanine (also hydrophobic). Both are clearly hydrophobic residues, and no general biological principle definitively determines whether a TM helix boundary falls at 121 or 122. The weak argument that position 120 is Asparagine (polar) so the helix 'starts' at 121 is within the noise of any TM prediction algorithm.",
    "missing_item_specific_fact": "The exact residue-level boundary output of the specific prediction algorithm (or homology transfer) used to generate the UniProt annotation, which determines whether the fourth TM helix starts at residue 121 or 122. This is an item-specific computational prediction artifact not derivable from general biology.",
    "reason": "While the number of TM regions (~5) and their approximate locations can be inferred from hydrophobicity analysis, the precise single-residue boundary distinguishing the correct answer D from the closest distractor C (121 vs 122) cannot be resolved by biological reasoning. Both L and A are hydrophobic; the boundary is an algorithmic artifact of the prediction method used for annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "The only difference between C and D is whether the fourth TM helix starts at 121 (L) or 122 (A). Both residues are hydrophobic and either could reasonably be considered the start of a TM helix. Without knowing the specific prediction algorithm's output, both boundaries are defensible from a hydrophobicity standpoint. The annotation evidence code (ECO:0000255, by similarity) confirms these are computational predictions, not experimental measurements."
  },
  "important_caveats": [
    "All TM annotations carry evidence code ECO:0000255 (by similarity), meaning they are computational predictions transferred from homologous proteins, not experimentally determined boundaries.",
    "The X-ray structure (PDB 6A7W) covers residues 215-538 only; the TM regions (all <215) are not covered by experimental structural data.",
    "The distinction between choices C and D is a single-residue boundary difference (121 vs 122) that falls within the uncertainty of any TM prediction method.",
    "The reviewer-only UniProt accession was inferred from dataset metadata and was not available to the evaluated model."
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

**Accession:** `A0A1C3NEV1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 38. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:32.663314+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":34},"start":{"modifier":"EXACT","value":14}},"type":"Transmembrane"}
```

Source SHA-256: `919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:32.663314+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":67},"start":{"modifier":"EXACT","value":47}},"type":"Transmembrane"}
```

Source SHA-256: `919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json)  
**Locator:** `/features/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:32.663314+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":92},"start":{"modifier":"EXACT","value":72}},"type":"Transmembrane"}
```

Source SHA-256: `919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:32.663314+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":141},"start":{"modifier":"EXACT","value":121}},"type":"Transmembrane"}
```

Source SHA-256: `919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json)  
**Locator:** `/features/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:32.663314+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":181},"start":{"modifier":"EXACT","value":161}},"type":"Transmembrane"}
```

Source SHA-256: `919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38)  
**Locator:** `lines 133-135`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:24:35.172422+00:00.  

```text
FT   TRANSMEM        14..34
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `d75fc4c8bc738f05806f3af9945e4dc68a9d390599953db777a2ada2b9fa9923`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38)  
**Locator:** `lines 136-138`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:24:35.172422+00:00.  

```text
FT   TRANSMEM        47..67
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `d75fc4c8bc738f05806f3af9945e4dc68a9d390599953db777a2ada2b9fa9923`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38)  
**Locator:** `lines 139-141`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:24:35.172422+00:00.  

```text
FT   TRANSMEM        72..92
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `d75fc4c8bc738f05806f3af9945e4dc68a9d390599953db777a2ada2b9fa9923`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38)  
**Locator:** `lines 142-144`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:24:35.172422+00:00.  

```text
FT   TRANSMEM        121..141
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `d75fc4c8bc738f05806f3af9945e4dc68a9d390599953db777a2ada2b9fa9923`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38)  
**Locator:** `lines 145-147`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:24:35.172422+00:00.  

```text
FT   TRANSMEM        161..181
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `d75fc4c8bc738f05806f3af9945e4dc68a9d390599953db777a2ada2b9fa9923`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 9. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
