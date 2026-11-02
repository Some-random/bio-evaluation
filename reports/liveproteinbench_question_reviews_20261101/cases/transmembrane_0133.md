# transmembrane_0133

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **B** — 139..159; 176..196; 247..267; 272..292; 297..317

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MESMVNNLWSSWDTLSQATASTGGDMDAASVASKQSPQESKMAASSMIWSSFSEPQKTPPTKRASSSFFDDMFTSSKDHSTTLTDKMFERFLSMALPTTTTQDGEELQSILERIEMQKSRPQLSLNVMSKNAIQLLSRLSVPFVLIDQVIIIFSWSKPLYTLTFLNVATLLILKPILLLSLPFFYTCFEIIVPAYMKRHPPDKHTILQNRNPIPAEGPSVSHVDVPRPVPELSREFVLNSTDLQNHMLLYVMSYDFVTSLIVKYLYFKDENITIFIFVALLTSGTLLTLFGAQVLSAMLPFIKVTLSVGLWAATIAMHPNYRSTLLDMLYSEDTRLRLLMMSNRLELWLNKELNLREQKEVKETEIFELQHLDPETHNWQLICFSSDPYPANSHARLNNLPLLGTLHLSQVKPPEGWKFVDVETAVNTRSVDGWLLDLTPEGWIKENFLNETMDIDEDEKWCYDLVTKFSYQAGLTTNEKKTRGEVRRRRWIRYCVRDIWDEDDQMEETVAHRRNKSMESSNSLHPVKSIDSVDG

[Multiple Choices]
A. 281..301
B. 139..159; 176..196; 247..267; 272..292; 297..317
C. 135..157; 176..196; 247..267; 272..292; 297..317
D. 139..159; 176..196; 247..267; 297..317
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

> The exact supplied sequence matches the UniProt record, whose transmembrane annotations give all five ranges in choice B. These are computational annotations (ECO:0000255), not experimental demonstrations.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Several hydrophobic stretches support the general inference that the protein has multiple membrane-spanning helices, but sequence hydropathy alone does not establish the precise annotated boundaries.


**Missing item-specific fact**

> The protein-specific predicted transmembrane ranges, especially the boundary choice distinguishing B from C, are not provided in the question.


**Reason**

> Selecting the exact coordinate set depends on the protein-specific annotation or an equivalent prediction; recognizing hydrophobic segments does not resolve the close boundary alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> B matches the cited annotation, but C shifts the first predicted span's boundaries only slightly. Such boundary variation is biologically plausible from the sequence alone, which does not specify a unique exact boundary.


### Important caveats

- The annotation supports the key but is computational rather than direct experimental evidence.
- The reviewer-only source matches the supplied sequence; its accession and annotation were not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Several hydrophobic stretches support the general inference that the protein has multiple membrane-spanning helices, but sequence hydropathy alone does not establish the precise annotated boundaries.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific predicted transmembrane ranges, especially the boundary choice distinguishing B from C, are not provided in the question.",
    "reason": "Selecting the exact coordinate set depends on the protein-specific annotation or an equivalent prediction; recognizing hydrophobic segments does not resolve the close boundary alternatives."
  },
  "case_id": "transmembrane_0133",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H4",
      "H5",
      "H6",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt record, whose transmembrane annotations give all five ranges in choice B. These are computational annotations (ECO:0000255), not experimental demonstrations."
  },
  "important_caveats": [
    "The annotation supports the key but is computational rather than direct experimental evidence.",
    "The reviewer-only source matches the supplied sequence; its accession and annotation were not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "B matches the cited annotation, but C shifts the first predicted span's boundaries only slightly. Such boundary variation is biologically plausible from the sequence alone, which does not specify a unique exact boundary."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0133",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt record, whose transmembrane annotations give all five ranges in choice B. These are computational annotations (ECO:0000255), not experimental demonstrations.",
    "evidence_ids": ["H3", "H4", "H5", "H6", "H7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Several hydrophobic stretches support the general inference that the protein has multiple membrane-spanning helices, but sequence hydropathy alone does not establish the precise annotated boundaries.",
    "missing_item_specific_fact": "The protein-specific predicted transmembrane ranges, especially the boundary choice distinguishing B from C, are not provided in the question.",
    "reason": "Selecting the exact coordinate set depends on the protein-specific annotation or an equivalent prediction; recognizing hydrophobic segments does not resolve the close boundary alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "B matches the cited annotation, but C shifts the first predicted span's boundaries only slightly. Such boundary variation is biologically plausible from the sequence alone, which does not specify a unique exact boundary."
  },
  "important_caveats": [
    "The annotation supports the key but is computational rather than direct experimental evidence.",
    "The reviewer-only source matches the supplied sequence; its accession and annotation were not available to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> Option B (139..159; 176..196; 247..267; 272..292; 297..317) matches the UniProtKB annotation for W1QL91 (PEX29_OGAPD) exactly across all five transmembrane helical segments. The annotation evidence code is ECO:0000255 (by similarity), indicating a computational/inference-based assignment rather than direct experimental determination, but it is the canonical database annotation and is consistent with the protein being a multi-pass peroxisomal membrane protein.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> General reasoning can establish that PEX29 is a multi-pass membrane protein and can identify approximate hydrophobic stretches of ~20 residues. However, distinguishing B from C (first TM at 139..159 vs 135..157, a 4-residue boundary shift) requires precise per-residue hydrophobicity scoring that is essentially what a TM prediction algorithm performs. Distinguishing B from D (whether 272..292 is a separate TM or merged with 247..267) hinges on whether a 4-residue intervening loop (268-271) is sufficient to split two adjacent hydrophobic stretches—a borderline judgment that depends on the specific prediction tool's parameters rather than a clear biological principle.


**Missing item-specific fact**

> The exact hydrophobicity scores at boundary residues (e.g., positions 135-138 and 158-159 for the first TM; positions 268-271 for the loop between TM3 and TM4) that determine whether the algorithm splits or merges segments. The UniProt annotation (ECO:0000255, by similarity) reflects a specific prediction tool's output, and the exact boundaries are tool-dependent rather than derivable from general biological knowledge.


**Reason**

> While a skilled analyst can identify the general pattern of multiple hydrophobic segments, the precise start/end positions (139 vs 135) and the decision to treat a 4-residue loop as separating two TMs (272-292) versus merging them depend on specific hydrophobicity calculations equivalent to running a TM prediction tool. These are not resolvable by general biological reasoning alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> The distinction between B and D rests on whether the 4-residue segment (positions 268-271) between TM regions 247-267 and 272-292 constitutes a genuine loop or is too short to separate two helices. Some TM prediction approaches would merge these into a single ~46-residue helix, while UniProt lists them separately. Without running the specific predictor used for annotation, both B and D are defensible from a pure hydrophobicity standpoint, though B matches the database annotation.


### Important caveats

- All transmembrane annotations carry evidence code ECO:0000255 (by similarity), meaning they are computational predictions transferred by homology, not experimentally validated topologies.
- The protein is from Ogataea parapolymorpha (yeast); the peroxisomal membrane localization is supported by PubMed:32665322 (subcellular location), but the exact TM boundaries are not experimentally determined.
- The reviewer-only UniProt evidence was not available to the evaluated model; the model must rely solely on the provided sequence and choices.
- Option A (281..301) is clearly wrong as it does not correspond to any annotated TM region and is too short (21 residues) to represent the full multi-pass topology.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "General reasoning can establish that PEX29 is a multi-pass membrane protein and can identify approximate hydrophobic stretches of ~20 residues. However, distinguishing B from C (first TM at 139..159 vs 135..157, a 4-residue boundary shift) requires precise per-residue hydrophobicity scoring that is essentially what a TM prediction algorithm performs. Distinguishing B from D (whether 272..292 is a separate TM or merged with 247..267) hinges on whether a 4-residue intervening loop (268-271) is sufficient to split two adjacent hydrophobic stretches—a borderline judgment that depends on the specific prediction tool's parameters rather than a clear biological principle.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact hydrophobicity scores at boundary residues (e.g., positions 135-138 and 158-159 for the first TM; positions 268-271 for the loop between TM3 and TM4) that determine whether the algorithm splits or merges segments. The UniProt annotation (ECO:0000255, by similarity) reflects a specific prediction tool's output, and the exact boundaries are tool-dependent rather than derivable from general biological knowledge.",
    "reason": "While a skilled analyst can identify the general pattern of multiple hydrophobic segments, the precise start/end positions (139 vs 135) and the decision to treat a 4-residue loop as separating two TMs (272-292) versus merging them depend on specific hydrophobicity calculations equivalent to running a TM prediction tool. These are not resolvable by general biological reasoning alone."
  },
  "case_id": "transmembrane_0133",
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
    "reason": "Option B (139..159; 176..196; 247..267; 272..292; 297..317) matches the UniProtKB annotation for W1QL91 (PEX29_OGAPD) exactly across all five transmembrane helical segments. The annotation evidence code is ECO:0000255 (by similarity), indicating a computational/inference-based assignment rather than direct experimental determination, but it is the canonical database annotation and is consistent with the protein being a multi-pass peroxisomal membrane protein."
  },
  "important_caveats": [
    "All transmembrane annotations carry evidence code ECO:0000255 (by similarity), meaning they are computational predictions transferred by homology, not experimentally validated topologies.",
    "The protein is from Ogataea parapolymorpha (yeast); the peroxisomal membrane localization is supported by PubMed:32665322 (subcellular location), but the exact TM boundaries are not experimentally determined.",
    "The reviewer-only UniProt evidence was not available to the evaluated model; the model must rely solely on the provided sequence and choices.",
    "Option A (281..301) is clearly wrong as it does not correspond to any annotated TM region and is too short (21 residues) to represent the full multi-pass topology."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "The distinction between B and D rests on whether the 4-residue segment (positions 268-271) between TM regions 247-267 and 272-292 constitutes a genuine loop or is too short to separate two helices. Some TM prediction approaches would merge these into a single ~46-residue helix, while UniProt lists them separately. Without running the specific predictor used for annotation, both B and D are defensible from a pure hydrophobicity standpoint, though B matches the database annotation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0133",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "Option B (139..159; 176..196; 247..267; 272..292; 297..317) matches the UniProtKB annotation for W1QL91 (PEX29_OGAPD) exactly across all five transmembrane helical segments. The annotation evidence code is ECO:0000255 (by similarity), indicating a computational/inference-based assignment rather than direct experimental determination, but it is the canonical database annotation and is consistent with the protein being a multi-pass peroxisomal membrane protein.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "H3", "H4", "H5", "H6", "H7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "General reasoning can establish that PEX29 is a multi-pass membrane protein and can identify approximate hydrophobic stretches of ~20 residues. However, distinguishing B from C (first TM at 139..159 vs 135..157, a 4-residue boundary shift) requires precise per-residue hydrophobicity scoring that is essentially what a TM prediction algorithm performs. Distinguishing B from D (whether 272..292 is a separate TM or merged with 247..267) hinges on whether a 4-residue intervening loop (268-271) is sufficient to split two adjacent hydrophobic stretches—a borderline judgment that depends on the specific prediction tool's parameters rather than a clear biological principle.",
    "missing_item_specific_fact": "The exact hydrophobicity scores at boundary residues (e.g., positions 135-138 and 158-159 for the first TM; positions 268-271 for the loop between TM3 and TM4) that determine whether the algorithm splits or merges segments. The UniProt annotation (ECO:0000255, by similarity) reflects a specific prediction tool's output, and the exact boundaries are tool-dependent rather than derivable from general biological knowledge.",
    "reason": "While a skilled analyst can identify the general pattern of multiple hydrophobic segments, the precise start/end positions (139 vs 135) and the decision to treat a 4-residue loop as separating two TMs (272-292) versus merging them depend on specific hydrophobicity calculations equivalent to running a TM prediction tool. These are not resolvable by general biological reasoning alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "The distinction between B and D rests on whether the 4-residue segment (positions 268-271) between TM regions 247-267 and 272-292 constitutes a genuine loop or is too short to separate two helices. Some TM prediction approaches would merge these into a single ~46-residue helix, while UniProt lists them separately. Without running the specific predictor used for annotation, both B and D are defensible from a pure hydrophobicity standpoint, though B matches the database annotation."
  },
  "important_caveats": [
    "All transmembrane annotations carry evidence code ECO:0000255 (by similarity), meaning they are computational predictions transferred by homology, not experimentally validated topologies.",
    "The protein is from Ogataea parapolymorpha (yeast); the peroxisomal membrane localization is supported by PubMed:32665322 (subcellular location), but the exact TM boundaries are not experimentally determined.",
    "The reviewer-only UniProt evidence was not available to the evaluated model; the model must rely solely on the provided sequence and choices.",
    "Option A (281..301) is clearly wrong as it does not correspond to any annotated TM region and is too short (21 residues) to represent the full multi-pass topology."
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

**Accession:** `W1QL91` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 41. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QL91.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:34:09.919107+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":159},"start":{"modifier":"EXACT","value":139}},"type":"Transmembrane"}
```

Source SHA-256: `82521092a67ef997abdc31799f3577764b26227f0c47f2c09c813128fc009f23`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QL91.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:34:09.919107+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":196},"start":{"modifier":"EXACT","value":176}},"type":"Transmembrane"}
```

Source SHA-256: `82521092a67ef997abdc31799f3577764b26227f0c47f2c09c813128fc009f23`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QL91.json)  
**Locator:** `/features/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:34:09.919107+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":267},"start":{"modifier":"EXACT","value":247}},"type":"Transmembrane"}
```

Source SHA-256: `82521092a67ef997abdc31799f3577764b26227f0c47f2c09c813128fc009f23`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QL91.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:34:09.919107+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":292},"start":{"modifier":"EXACT","value":272}},"type":"Transmembrane"}
```

Source SHA-256: `82521092a67ef997abdc31799f3577764b26227f0c47f2c09c813128fc009f23`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QL91.json)  
**Locator:** `/features/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:34:09.919107+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":317},"start":{"modifier":"EXACT","value":297}},"type":"Transmembrane"}
```

Source SHA-256: `82521092a67ef997abdc31799f3577764b26227f0c47f2c09c813128fc009f23`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QL91?format=txt&versions=41)  
**Locator:** `lines 84-86`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 41 / 1.  
**Retrieved:** 2026-11-02T04:34:13.232116+00:00.  

```text
FT   TRANSMEM        139..159
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `2b59cad336a5f0f970c7aa6c93d04cd1ad5885189ae5de312c6383b733a569b7`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QL91?format=txt&versions=41)  
**Locator:** `lines 87-89`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 41 / 1.  
**Retrieved:** 2026-11-02T04:34:13.232116+00:00.  

```text
FT   TRANSMEM        176..196
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `2b59cad336a5f0f970c7aa6c93d04cd1ad5885189ae5de312c6383b733a569b7`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QL91?format=txt&versions=41)  
**Locator:** `lines 90-92`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 41 / 1.  
**Retrieved:** 2026-11-02T04:34:13.232116+00:00.  

```text
FT   TRANSMEM        247..267
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `2b59cad336a5f0f970c7aa6c93d04cd1ad5885189ae5de312c6383b733a569b7`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QL91?format=txt&versions=41)  
**Locator:** `lines 93-95`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 41 / 1.  
**Retrieved:** 2026-11-02T04:34:13.232116+00:00.  

```text
FT   TRANSMEM        272..292
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `2b59cad336a5f0f970c7aa6c93d04cd1ad5885189ae5de312c6383b733a569b7`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QL91?format=txt&versions=41)  
**Locator:** `lines 96-98`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 41 / 1.  
**Retrieved:** 2026-11-02T04:34:13.232116+00:00.  

```text
FT   TRANSMEM        297..317
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `2b59cad336a5f0f970c7aa6c93d04cd1ad5885189ae5de312c6383b733a569b7`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 133. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
