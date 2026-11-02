# transmembrane_0059

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **B** — 17..37; 48..68; 94..114; 129..149; 176..196; 295..315; 322..342

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MQPFGDAWSQRHLAGVVLAGSVLSIVGSLYMILGFFFLRECRSFRHKLILGLAVSDLLLALNFFIPSLSMVTGREISSPWNEGFCSANGFLMQLFFAQIDVWQISIALITLLMLSGPSMVLKWIRENVWAVWLFPWLVSLIAAFFAFGFWDYANVGGFCWLGSRNIRLYFNYIPRWIIILVCLVIYIAVYRLILHARRRANIQKTYRGRASDRAPPQPVTTTAPATNPESEKVNPDEISSGNGSSSLDTSRSGSSTGFTQTVHDPAVAGQIQTAAERAQEEAEQQKQVRKIAIQMISYPLAYAVLWAIPTIVMIIQVARGGEGVSIHVEGLAKMLLVFNGFVDAHVYGFNERTAMGWRQRIRPAAQEDDEEAAGTSGGVHEVVSRPEPTLKNPNVWQQNMV

[Multiple Choices]
A. 17..37; 48..68; 94..114; 134..154; 176..196; 295..315; 322..342
B. 17..37; 48..68; 94..114; 129..149; 176..196; 295..315; 322..342
C. 28..48; 59..79; 106..126
D. 48..68; 94..114; 129..149; 176..196; 295..315; 322..342
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

> The sequence exactly matches the UniProt record, whose historical and current annotations include all seven transmembrane spans listed in B, including 129..149. These are computational annotations (ECO:0000255), not evidence of direct experimental measurement.

Citations as saved: [H4](#evidence-h4), [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains successive strongly hydrophobic stretches separated by more polar or charged regions, consistent with a multi-pass membrane protein. The candidate set’s seven-span pattern fits this sequence; around the disputed span, 129..149 better captures the hydrophobic segment than the shifted 134..154 option, which extends into more polar residues.


**Missing item-specific fact**

> The exact curated transmembrane coordinates are not given, but sequence hydropathy and the pattern of separated hydrophobic segments provide meaningful grounds to distinguish the choices. The database annotation is useful confirmation, not information supplied to the model.


**Reason**

> This is a sequence-based prediction task with a recognizable multi-pass hydrophobic pattern. The evidence supports an inference from the input rather than requiring recognition of the exact protein or recall of its database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives omit or shift spans in ways that fit the sequence less well; no competing option is comparably supported by the supplied sequence.


### Important caveats

- The supporting database transmembrane features are computationally annotated, not established here as experimental measurements.
- The historical record sequence matches the supplied sequence, but the author’s exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains successive strongly hydrophobic stretches separated by more polar or charged regions, consistent with a multi-pass membrane protein. The candidate set’s seven-span pattern fits this sequence; around the disputed span, 129..149 better captures the hydrophobic segment than the shifted 134..154 option, which extends into more polar residues.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact curated transmembrane coordinates are not given, but sequence hydropathy and the pattern of separated hydrophobic segments provide meaningful grounds to distinguish the choices. The database annotation is useful confirmation, not information supplied to the model.",
    "reason": "This is a sequence-based prediction task with a recognizable multi-pass hydrophobic pattern. The evidence supports an inference from the input rather than requiring recognition of the exact protein or recall of its database entry."
  },
  "case_id": "transmembrane_0059",
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
    "reason": "The sequence exactly matches the UniProt record, whose historical and current annotations include all seven transmembrane spans listed in B, including 129..149. These are computational annotations (ECO:0000255), not evidence of direct experimental measurement."
  },
  "important_caveats": [
    "The supporting database transmembrane features are computationally annotated, not established here as experimental measurements.",
    "The historical record sequence matches the supplied sequence, but the author’s exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives omit or shift spans in ways that fit the sequence less well; no competing option is comparably supported by the supplied sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0059",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches the UniProt record, whose historical and current annotations include all seven transmembrane spans listed in B, including 129..149. These are computational annotations (ECO:0000255), not evidence of direct experimental measurement.",
    "evidence_ids": ["H4", "H6", "H8", "H10", "H12", "H14", "H16"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains successive strongly hydrophobic stretches separated by more polar or charged regions, consistent with a multi-pass membrane protein. The candidate set’s seven-span pattern fits this sequence; around the disputed span, 129..149 better captures the hydrophobic segment than the shifted 134..154 option, which extends into more polar residues.",
    "missing_item_specific_fact": "The exact curated transmembrane coordinates are not given, but sequence hydropathy and the pattern of separated hydrophobic segments provide meaningful grounds to distinguish the choices. The database annotation is useful confirmation, not information supplied to the model.",
    "reason": "This is a sequence-based prediction task with a recognizable multi-pass hydrophobic pattern. The evidence supports an inference from the input rather than requiring recognition of the exact protein or recall of its database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives omit or shift spans in ways that fit the sequence less well; no competing option is comparably supported by the supplied sequence."
  },
  "important_caveats": [
    "The supporting database transmembrane features are computationally annotated, not established here as experimental measurements.",
    "The historical record sequence matches the supplied sequence, but the author’s exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry G1XJN1 (Ascaroside receptor GPR3, Arthrobotrys oligospora) annotates exactly seven transmembrane helices at 17-37, 48-68, 94-114, 129-149, 176-196, 295-315, and 322-342, matching option B precisely. Both the current entry (v48) and the historical entry (v46) confirm these coordinates. The sequence in the question matches the UniProt sequence (SHA-256 identical, 401 AA). However, all TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning these are computational predictions from homology to known GPCR architectures, not experimentally determined boundaries.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [H4](#evidence-h4), [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> General GPCR knowledge eliminates C (only 3 TM segments) and D (6 segments, missing TM1) since a canonical GPCR requires 7 TM helices. For the A-vs-B distinction (TM4 at 129-149 vs 134-154), a partial hydrophobicity argument exists: residues 129-133 (W-A-V-W-L) are hydrophobic and favor B's earlier start, while residues 150-154 include D and N (hydrophilic) that favor B's earlier end. However, this is a 5-residue shift within a 21-residue helix, well within the boundary uncertainty of any hydrophobicity-based predictor.


**Missing item-specific fact**

> The exact TM4 boundary (129-149 vs 134-154) is a specific output of the UniProt similarity-based prediction (ECO:0000255), not an experimentally determined value. Distinguishing A from B with confidence requires knowing the particular annotation or prediction-tool output rather than applying general biological principles, since both boundaries fall within the plausible hydrophobic stretch.


**Reason**

> While GPCR topology reasoning (7 TM segments) eliminates C and D, the critical A-vs-B discrimination hinges on a 5-residue boundary shift in TM4. The residues at the contested positions (WAVWL at 129-133; WDYAN at 150-154) provide weak hydrophobicity hints favoring B, but TM helix boundaries in GPCRs are inherently fuzzy and commonly include aromatic and even polar residues at their edges. The 'correct' boundaries are themselves computational predictions (ECO:0000255), so the question effectively asks the model to reproduce a specific annotation output rather than derive a biologically certain answer.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Options A and B differ only in TM4 (134-154 vs 129-149). Both are plausible 21-residue hydrophobic segments. The 5-residue shift falls within the typical boundary uncertainty of TM prediction tools. Without the specific database annotation, a competent hydrophobicity analysis could reasonably assign TM4 to either range, making A a defensible alternative.


### Important caveats

- All seven TM annotations carry evidence code ECO:0000255 (similarity inference), meaning even the 'correct' boundaries are computational predictions, not experimental measurements.
- The UniProt entry was first public in April 2025; the author's source snapshot is unknown, though the sequence and annotations are stable (sequence version 1 unchanged since 2011).
- The reviewer-only evidence confirms the annotation but was not available to the evaluated model; the model must reason from sequence alone.
- Option C (3 segments) and D (6 segments) are clearly wrong for a GPCR, making the effective discrimination a binary A-vs-B choice on a single boundary.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "General GPCR knowledge eliminates C (only 3 TM segments) and D (6 segments, missing TM1) since a canonical GPCR requires 7 TM helices. For the A-vs-B distinction (TM4 at 129-149 vs 134-154), a partial hydrophobicity argument exists: residues 129-133 (W-A-V-W-L) are hydrophobic and favor B's earlier start, while residues 150-154 include D and N (hydrophilic) that favor B's earlier end. However, this is a 5-residue shift within a 21-residue helix, well within the boundary uncertainty of any hydrophobicity-based predictor.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact TM4 boundary (129-149 vs 134-154) is a specific output of the UniProt similarity-based prediction (ECO:0000255), not an experimentally determined value. Distinguishing A from B with confidence requires knowing the particular annotation or prediction-tool output rather than applying general biological principles, since both boundaries fall within the plausible hydrophobic stretch.",
    "reason": "While GPCR topology reasoning (7 TM segments) eliminates C and D, the critical A-vs-B discrimination hinges on a 5-residue boundary shift in TM4. The residues at the contested positions (WAVWL at 129-133; WDYAN at 150-154) provide weak hydrophobicity hints favoring B, but TM helix boundaries in GPCRs are inherently fuzzy and commonly include aromatic and even polar residues at their edges. The 'correct' boundaries are themselves computational predictions (ECO:0000255), so the question effectively asks the model to reproduce a specific annotation output rather than derive a biologically certain answer."
  },
  "case_id": "transmembrane_0059",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C8",
      "C10",
      "C12",
      "C14",
      "C16",
      "C18",
      "H4",
      "H6",
      "H8",
      "H10",
      "H12",
      "H14",
      "H16"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry G1XJN1 (Ascaroside receptor GPR3, Arthrobotrys oligospora) annotates exactly seven transmembrane helices at 17-37, 48-68, 94-114, 129-149, 176-196, 295-315, and 322-342, matching option B precisely. Both the current entry (v48) and the historical entry (v46) confirm these coordinates. The sequence in the question matches the UniProt sequence (SHA-256 identical, 401 AA). However, all TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning these are computational predictions from homology to known GPCR architectures, not experimentally determined boundaries."
  },
  "important_caveats": [
    "All seven TM annotations carry evidence code ECO:0000255 (similarity inference), meaning even the 'correct' boundaries are computational predictions, not experimental measurements.",
    "The UniProt entry was first public in April 2025; the author's source snapshot is unknown, though the sequence and annotations are stable (sequence version 1 unchanged since 2011).",
    "The reviewer-only evidence confirms the annotation but was not available to the evaluated model; the model must reason from sequence alone.",
    "Option C (3 segments) and D (6 segments) are clearly wrong for a GPCR, making the effective discrimination a binary A-vs-B choice on a single boundary."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Options A and B differ only in TM4 (134-154 vs 129-149). Both are plausible 21-residue hydrophobic segments. The 5-residue shift falls within the typical boundary uncertainty of TM prediction tools. Without the specific database annotation, a competent hydrophobicity analysis could reasonably assign TM4 to either range, making A a defensible alternative."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0059",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry G1XJN1 (Ascaroside receptor GPR3, Arthrobotrys oligospora) annotates exactly seven transmembrane helices at 17-37, 48-68, 94-114, 129-149, 176-196, 295-315, and 322-342, matching option B precisely. Both the current entry (v48) and the historical entry (v46) confirm these coordinates. The sequence in the question matches the UniProt sequence (SHA-256 identical, 401 AA). However, all TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning these are computational predictions from homology to known GPCR architectures, not experimentally determined boundaries.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "H4", "H6", "H8", "H10", "H12", "H14", "H16"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "General GPCR knowledge eliminates C (only 3 TM segments) and D (6 segments, missing TM1) since a canonical GPCR requires 7 TM helices. For the A-vs-B distinction (TM4 at 129-149 vs 134-154), a partial hydrophobicity argument exists: residues 129-133 (W-A-V-W-L) are hydrophobic and favor B's earlier start, while residues 150-154 include D and N (hydrophilic) that favor B's earlier end. However, this is a 5-residue shift within a 21-residue helix, well within the boundary uncertainty of any hydrophobicity-based predictor.",
    "missing_item_specific_fact": "The exact TM4 boundary (129-149 vs 134-154) is a specific output of the UniProt similarity-based prediction (ECO:0000255), not an experimentally determined value. Distinguishing A from B with confidence requires knowing the particular annotation or prediction-tool output rather than applying general biological principles, since both boundaries fall within the plausible hydrophobic stretch.",
    "reason": "While GPCR topology reasoning (7 TM segments) eliminates C and D, the critical A-vs-B discrimination hinges on a 5-residue boundary shift in TM4. The residues at the contested positions (WAVWL at 129-133; WDYAN at 150-154) provide weak hydrophobicity hints favoring B, but TM helix boundaries in GPCRs are inherently fuzzy and commonly include aromatic and even polar residues at their edges. The 'correct' boundaries are themselves computational predictions (ECO:0000255), so the question effectively asks the model to reproduce a specific annotation output rather than derive a biologically certain answer."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Options A and B differ only in TM4 (134-154 vs 129-149). Both are plausible 21-residue hydrophobic segments. The 5-residue shift falls within the typical boundary uncertainty of TM prediction tools. Without the specific database annotation, a competent hydrophobicity analysis could reasonably assign TM4 to either range, making A a defensible alternative."
  },
  "important_caveats": [
    "All seven TM annotations carry evidence code ECO:0000255 (similarity inference), meaning even the 'correct' boundaries are computational predictions, not experimental measurements.",
    "The UniProt entry was first public in April 2025; the author's source snapshot is unknown, though the sequence and annotations are stable (sequence version 1 unchanged since 2011).",
    "The reviewer-only evidence confirms the annotation but was not available to the evaluated model; the model must reason from sequence alone.",
    "Option C (3 segments) and D (6 segments) are clearly wrong for a GPCR, making the effective discrimination a binary A-vs-B choice on a single boundary."
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

**Accession:** `G1XJN1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 46. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1XJN1.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:05.818783+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":37},"start":{"modifier":"EXACT","value":17}},"type":"Transmembrane"}
```

Source SHA-256: `d1cb02451e5c1d2640cfcdf6c12c2a6a6f5853805bd439c3031dde0eea563a37`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1XJN1.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:05.818783+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":68},"start":{"modifier":"EXACT","value":48}},"type":"Transmembrane"}
```

Source SHA-256: `d1cb02451e5c1d2640cfcdf6c12c2a6a6f5853805bd439c3031dde0eea563a37`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1XJN1.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:05.818783+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":114},"start":{"modifier":"EXACT","value":94}},"type":"Transmembrane"}
```

Source SHA-256: `d1cb02451e5c1d2640cfcdf6c12c2a6a6f5853805bd439c3031dde0eea563a37`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1XJN1.json)  
**Locator:** `/features/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:05.818783+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":149},"start":{"modifier":"EXACT","value":129}},"type":"Transmembrane"}
```

Source SHA-256: `d1cb02451e5c1d2640cfcdf6c12c2a6a6f5853805bd439c3031dde0eea563a37`.

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1XJN1.json)  
**Locator:** `/features/10`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:05.818783+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":196},"start":{"modifier":"EXACT","value":176}},"type":"Transmembrane"}
```

Source SHA-256: `d1cb02451e5c1d2640cfcdf6c12c2a6a6f5853805bd439c3031dde0eea563a37`.

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1XJN1.json)  
**Locator:** `/features/12`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:05.818783+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":315},"start":{"modifier":"EXACT","value":295}},"type":"Transmembrane"}
```

Source SHA-256: `d1cb02451e5c1d2640cfcdf6c12c2a6a6f5853805bd439c3031dde0eea563a37`.

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1XJN1.json)  
**Locator:** `/features/14`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:05.818783+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":342},"start":{"modifier":"EXACT","value":322}},"type":"Transmembrane"}
```

Source SHA-256: `d1cb02451e5c1d2640cfcdf6c12c2a6a6f5853805bd439c3031dde0eea563a37`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1XJN1?format=txt&versions=46)  
**Locator:** `lines 99-101`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 46 / 1.  
**Retrieved:** 2026-11-01T06:28:00.513965+00:00.  

```text
FT   TRANSMEM        17..37
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `3c78ac63e30f9e6fea6d4c3a7ddd8ee59ee45f0a9c5a7225b00c7055bec78804`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1XJN1?format=txt&versions=46)  
**Locator:** `lines 105-107`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 46 / 1.  
**Retrieved:** 2026-11-01T06:28:00.513965+00:00.  

```text
FT   TRANSMEM        48..68
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `3c78ac63e30f9e6fea6d4c3a7ddd8ee59ee45f0a9c5a7225b00c7055bec78804`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1XJN1?format=txt&versions=46)  
**Locator:** `lines 111-113`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 46 / 1.  
**Retrieved:** 2026-11-01T06:28:00.513965+00:00.  

```text
FT   TRANSMEM        94..114
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `3c78ac63e30f9e6fea6d4c3a7ddd8ee59ee45f0a9c5a7225b00c7055bec78804`.

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1XJN1?format=txt&versions=46)  
**Locator:** `lines 117-119`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 46 / 1.  
**Retrieved:** 2026-11-01T06:28:00.513965+00:00.  

```text
FT   TRANSMEM        129..149
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `3c78ac63e30f9e6fea6d4c3a7ddd8ee59ee45f0a9c5a7225b00c7055bec78804`.

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1XJN1?format=txt&versions=46)  
**Locator:** `lines 123-125`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 46 / 1.  
**Retrieved:** 2026-11-01T06:28:00.513965+00:00.  

```text
FT   TRANSMEM        176..196
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `3c78ac63e30f9e6fea6d4c3a7ddd8ee59ee45f0a9c5a7225b00c7055bec78804`.

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1XJN1?format=txt&versions=46)  
**Locator:** `lines 129-131`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 46 / 1.  
**Retrieved:** 2026-11-01T06:28:00.513965+00:00.  

```text
FT   TRANSMEM        295..315
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `3c78ac63e30f9e6fea6d4c3a7ddd8ee59ee45f0a9c5a7225b00c7055bec78804`.

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1XJN1?format=txt&versions=46)  
**Locator:** `lines 135-137`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 46 / 1.  
**Retrieved:** 2026-11-01T06:28:00.513965+00:00.  

```text
FT   TRANSMEM        322..342
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `3c78ac63e30f9e6fea6d4c3a7ddd8ee59ee45f0a9c5a7225b00c7055bec78804`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 59. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
