# transmembrane_0072

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **C** — 27..47; 59..79; 109..129; 142..162; 168..188; 225..245

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTAYALTDSWTMTRRELARWARQPVQLVVNLVFPVMLLLMFGYLIGGGRGVNGEYRDYLIPGMLALTMAFGLEGTMIAVTRDLDKGVIDRFRSMPMADGAVLVGRSAADMLQSAMALVVLIGVGAALGWRVHGGPVAFLGAVGLLLLFRFAMLWIGIYLALVAGKPEMVQAVQILVWPIGFLSNALALPDTMPGWLGTVVEWNPMSHTATAVRDLFGTPGAESGHVGAALVWPLALLAVFFPLAVRRFGRLSR

[Multiple Choices]
A. 29..44; 59..79; 109..129; 142..162; 168..188; 225..245
B. 27..47; 59..79; 109..129; 168..188; 225..245
C. 27..47; 59..79; 109..129; 142..162; 168..188; 225..245
D. 17..40
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

> The sequence-matched UniProt record annotates all six regions in C as helical transmembrane segments. The evidence code is computational (ECO:0000255), so this supports the predicted annotations, not experimental confirmation.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains several suitably long, strongly hydrophobic stretches consistent with membrane-spanning helices. In particular, the hydrophobic stretch around 142–162 supports the segment omitted by B, while 27–47 is a more plausible full-length helix than A’s shorter 29–44 interval.


**Missing item-specific fact**

> The exact database annotation is not supplied; precise residue boundaries remain predictive rather than experimentally established by the input.


**Reason**

> Sequence hydrophobicity and expected transmembrane-helix length provide meaningful grounds to favor C among the choices, although they do not establish exact boundaries with certainty.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options differ in a way that favors the full-length hydrophobic span in C; A’s shorter interval and B’s omission of a strongly hydrophobic span are less plausible.


### Important caveats

- The reviewer-only annotation matches the supplied sequence, but its transmembrane evidence is computational, not experimental.
- Exact segment boundaries can be uncertain from sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains several suitably long, strongly hydrophobic stretches consistent with membrane-spanning helices. In particular, the hydrophobic stretch around 142–162 supports the segment omitted by B, while 27–47 is a more plausible full-length helix than A’s shorter 29–44 interval.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact database annotation is not supplied; precise residue boundaries remain predictive rather than experimentally established by the input.",
    "reason": "Sequence hydrophobicity and expected transmembrane-helix length provide meaningful grounds to favor C among the choices, although they do not establish exact boundaries with certainty."
  },
  "case_id": "transmembrane_0072",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "C10"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates all six regions in C as helical transmembrane segments. The evidence code is computational (ECO:0000255), so this supports the predicted annotations, not experimental confirmation."
  },
  "important_caveats": [
    "The reviewer-only annotation matches the supplied sequence, but its transmembrane evidence is computational, not experimental.",
    "Exact segment boundaries can be uncertain from sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options differ in a way that favors the full-length hydrophobic span in C; A’s shorter interval and B’s omission of a strongly hydrophobic span are less plausible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0072",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates all six regions in C as helical transmembrane segments. The evidence code is computational (ECO:0000255), so this supports the predicted annotations, not experimental confirmation.",
    "evidence_ids": ["H3", "H4", "H5", "H6", "H7", "H8", "C5", "C6", "C7", "C8", "C9", "C10"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains several suitably long, strongly hydrophobic stretches consistent with membrane-spanning helices. In particular, the hydrophobic stretch around 142–162 supports the segment omitted by B, while 27–47 is a more plausible full-length helix than A’s shorter 29–44 interval.",
    "missing_item_specific_fact": "The exact database annotation is not supplied; precise residue boundaries remain predictive rather than experimentally established by the input.",
    "reason": "Sequence hydrophobicity and expected transmembrane-helix length provide meaningful grounds to favor C among the choices, although they do not establish exact boundaries with certainty."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options differ in a way that favors the full-length hydrophobic span in C; A’s shorter interval and B’s omission of a strongly hydrophobic span are less plausible."
  },
  "important_caveats": [
    "The reviewer-only annotation matches the supplied sequence, but its transmembrane evidence is computational, not experimental.",
    "Exact segment boundaries can be uncertain from sequence alone."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> Choice C (27..47; 59..79; 109..129; 142..162; 168..188; 225..245) exactly matches all six transmembrane helix annotations in UniProt entry P0DXU8 (DrrB3, Daunorubicin resistance ABC transporter permease). The sequence in the question matches the UniProt sequence (SHA-256 confirmed). However, the annotation evidence code is ECO:0000255 (inferred by rule/similarity), meaning these are computational predictions rather than experimentally determined boundaries. The key is supported as the canonical database annotation.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Two key distinctions can be reasoned from the sequence itself: (1) Choice B omits the 142..162 region, which is a 21-residue segment (VGLLLLFRFAMLWIGIYLALV) dominated by hydrophobic residues (L, F, A, M, W, I, V) — a textbook TM helix candidate that any hydrophobicity-based analysis would flag. (2) Choice A uses 29..44 (16 residues) for the first TM, whereas C uses 27..47 (21 residues). A 21-residue α-helix (~31.5 Å) is more physically appropriate for spanning a ~30 Å hydrophobic membrane core than a 16-residue helix (~24 Å), which would be borderline too short. Choice D (single TM at 17..40) is clearly incompatible with a multi-pass ABC permease. These biological arguments meaningfully favor C over A, B, and D.


**Missing item-specific fact**

> The exact boundary positions (e.g., start at 27 vs 28 vs 29; end at 47 vs 44 vs 45) are determined by the specific prediction algorithm used in the UniProt annotation (ECO:0000255, rule-based). A model performing independent hydrophobicity analysis might assign slightly different boundaries (e.g., 28..46 or 27..45), though the 21-residue span and the inclusion of 142..162 are well-supported by the sequence.


**Reason**

> The presence/absence of the 142..162 TM helix and the physical requirement for ~20+ residue hydrophobic helices to span a membrane provide genuine biological reasoning to eliminate B and A respectively. D is trivially eliminated. The exact boundary positions (27 vs 29, 47 vs 44) are somewhat algorithm-dependent, but the 21-residue length is more defensible than 16 residues for membrane spanning, giving a concrete physical argument favoring C.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While the exact first-TM boundaries (27..47 vs 29..44) are borderline, the 16-residue helix in A is physically marginal for membrane spanning, and the omission of the clearly hydrophobic 142..162 region in B is a substantive error. D is clearly wrong. C is the most defensible choice. No other option is equally well-supported.


### Important caveats

- The UniProt TM annotations carry evidence code ECO:0000255 (inferred by rule/similarity), meaning they are computational predictions, not experimental measurements. The 'correct' boundaries reflect a specific prediction algorithm's output.
- The reviewer-only evidence confirms the sequence matches P0DXU8 exactly (SHA-256 match), but the model was not given the accession or annotation — it must work from the raw sequence.
- The exact boundary positions (e.g., 27 vs 29 for the first TM start) are somewhat arbitrary and algorithm-dependent; a reasonable alternative predictor might shift boundaries by 1-2 residues without changing the biological interpretation.
- The protein is annotated as an ABC transporter permease (DrrB3), which typically has multiple TM helices, consistent with 6 TMs rather than 5 (B) or 1 (D).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Two key distinctions can be reasoned from the sequence itself: (1) Choice B omits the 142..162 region, which is a 21-residue segment (VGLLLLFRFAMLWIGIYLALV) dominated by hydrophobic residues (L, F, A, M, W, I, V) — a textbook TM helix candidate that any hydrophobicity-based analysis would flag. (2) Choice A uses 29..44 (16 residues) for the first TM, whereas C uses 27..47 (21 residues). A 21-residue α-helix (~31.5 Å) is more physically appropriate for spanning a ~30 Å hydrophobic membrane core than a 16-residue helix (~24 Å), which would be borderline too short. Choice D (single TM at 17..40) is clearly incompatible with a multi-pass ABC permease. These biological arguments meaningfully favor C over A, B, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact boundary positions (e.g., start at 27 vs 28 vs 29; end at 47 vs 44 vs 45) are determined by the specific prediction algorithm used in the UniProt annotation (ECO:0000255, rule-based). A model performing independent hydrophobicity analysis might assign slightly different boundaries (e.g., 28..46 or 27..45), though the 21-residue span and the inclusion of 142..162 are well-supported by the sequence.",
    "reason": "The presence/absence of the 142..162 TM helix and the physical requirement for ~20+ residue hydrophobic helices to span a membrane provide genuine biological reasoning to eliminate B and A respectively. D is trivially eliminated. The exact boundary positions (27 vs 29, 47 vs 44) are somewhat algorithm-dependent, but the 21-residue length is more defensible than 16 residues for membrane spanning, giving a concrete physical argument favoring C."
  },
  "case_id": "transmembrane_0072",
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
    "reason": "Choice C (27..47; 59..79; 109..129; 142..162; 168..188; 225..245) exactly matches all six transmembrane helix annotations in UniProt entry P0DXU8 (DrrB3, Daunorubicin resistance ABC transporter permease). The sequence in the question matches the UniProt sequence (SHA-256 confirmed). However, the annotation evidence code is ECO:0000255 (inferred by rule/similarity), meaning these are computational predictions rather than experimentally determined boundaries. The key is supported as the canonical database annotation."
  },
  "important_caveats": [
    "The UniProt TM annotations carry evidence code ECO:0000255 (inferred by rule/similarity), meaning they are computational predictions, not experimental measurements. The 'correct' boundaries reflect a specific prediction algorithm's output.",
    "The reviewer-only evidence confirms the sequence matches P0DXU8 exactly (SHA-256 match), but the model was not given the accession or annotation — it must work from the raw sequence.",
    "The exact boundary positions (e.g., 27 vs 29 for the first TM start) are somewhat arbitrary and algorithm-dependent; a reasonable alternative predictor might shift boundaries by 1-2 residues without changing the biological interpretation.",
    "The protein is annotated as an ABC transporter permease (DrrB3), which typically has multiple TM helices, consistent with 6 TMs rather than 5 (B) or 1 (D)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the exact first-TM boundaries (27..47 vs 29..44) are borderline, the 16-residue helix in A is physically marginal for membrane spanning, and the omission of the clearly hydrophobic 142..162 region in B is a substantive error. D is clearly wrong. C is the most defensible choice. No other option is equally well-supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0072",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "Choice C (27..47; 59..79; 109..129; 142..162; 168..188; 225..245) exactly matches all six transmembrane helix annotations in UniProt entry P0DXU8 (DrrB3, Daunorubicin resistance ABC transporter permease). The sequence in the question matches the UniProt sequence (SHA-256 confirmed). However, the annotation evidence code is ECO:0000255 (inferred by rule/similarity), meaning these are computational predictions rather than experimentally determined boundaries. The key is supported as the canonical database annotation.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "H3", "H4", "H5", "H6", "H7", "H8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Two key distinctions can be reasoned from the sequence itself: (1) Choice B omits the 142..162 region, which is a 21-residue segment (VGLLLLFRFAMLWIGIYLALV) dominated by hydrophobic residues (L, F, A, M, W, I, V) — a textbook TM helix candidate that any hydrophobicity-based analysis would flag. (2) Choice A uses 29..44 (16 residues) for the first TM, whereas C uses 27..47 (21 residues). A 21-residue α-helix (~31.5 Å) is more physically appropriate for spanning a ~30 Å hydrophobic membrane core than a 16-residue helix (~24 Å), which would be borderline too short. Choice D (single TM at 17..40) is clearly incompatible with a multi-pass ABC permease. These biological arguments meaningfully favor C over A, B, and D.",
    "missing_item_specific_fact": "The exact boundary positions (e.g., start at 27 vs 28 vs 29; end at 47 vs 44 vs 45) are determined by the specific prediction algorithm used in the UniProt annotation (ECO:0000255, rule-based). A model performing independent hydrophobicity analysis might assign slightly different boundaries (e.g., 28..46 or 27..45), though the 21-residue span and the inclusion of 142..162 are well-supported by the sequence.",
    "reason": "The presence/absence of the 142..162 TM helix and the physical requirement for ~20+ residue hydrophobic helices to span a membrane provide genuine biological reasoning to eliminate B and A respectively. D is trivially eliminated. The exact boundary positions (27 vs 29, 47 vs 44) are somewhat algorithm-dependent, but the 21-residue length is more defensible than 16 residues for membrane spanning, giving a concrete physical argument favoring C."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the exact first-TM boundaries (27..47 vs 29..44) are borderline, the 16-residue helix in A is physically marginal for membrane spanning, and the omission of the clearly hydrophobic 142..162 region in B is a substantive error. D is clearly wrong. C is the most defensible choice. No other option is equally well-supported."
  },
  "important_caveats": [
    "The UniProt TM annotations carry evidence code ECO:0000255 (inferred by rule/similarity), meaning they are computational predictions, not experimental measurements. The 'correct' boundaries reflect a specific prediction algorithm's output.",
    "The reviewer-only evidence confirms the sequence matches P0DXU8 exactly (SHA-256 match), but the model was not given the accession or annotation — it must work from the raw sequence.",
    "The exact boundary positions (e.g., 27 vs 29 for the first TM start) are somewhat arbitrary and algorithm-dependent; a reasonable alternative predictor might shift boundaries by 1-2 residues without changing the biological interpretation.",
    "The protein is annotated as an ABC transporter permease (DrrB3), which typically has multiple TM helices, consistent with 6 TMs rather than 5 (B) or 1 (D)."
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

**Accession:** `P0DXU8` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 4. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU8.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:15.602104+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":47},"start":{"modifier":"EXACT","value":27}},"type":"Transmembrane"}
```

Source SHA-256: `c44dd25653843feda280457e5b2e85251c777e88151bb6df35b17c700c0142ca`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU8.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:15.602104+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":79},"start":{"modifier":"EXACT","value":59}},"type":"Transmembrane"}
```

Source SHA-256: `c44dd25653843feda280457e5b2e85251c777e88151bb6df35b17c700c0142ca`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU8.json)  
**Locator:** `/features/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:15.602104+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":129},"start":{"modifier":"EXACT","value":109}},"type":"Transmembrane"}
```

Source SHA-256: `c44dd25653843feda280457e5b2e85251c777e88151bb6df35b17c700c0142ca`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU8.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:15.602104+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":162},"start":{"modifier":"EXACT","value":142}},"type":"Transmembrane"}
```

Source SHA-256: `c44dd25653843feda280457e5b2e85251c777e88151bb6df35b17c700c0142ca`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU8.json)  
**Locator:** `/features/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:15.602104+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":188},"start":{"modifier":"EXACT","value":168}},"type":"Transmembrane"}
```

Source SHA-256: `c44dd25653843feda280457e5b2e85251c777e88151bb6df35b17c700c0142ca`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU8.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:15.602104+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":245},"start":{"modifier":"EXACT","value":225}},"type":"Transmembrane"}
```

Source SHA-256: `c44dd25653843feda280457e5b2e85251c777e88151bb6df35b17c700c0142ca`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU8?format=txt&versions=4)  
**Locator:** `lines 74-76`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-01T06:28:21.104799+00:00.  

```text
FT   TRANSMEM        27..47
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `eacc14042885f4a9bee71583e3725efd2169f7b227d732287e6adf264663178e`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU8?format=txt&versions=4)  
**Locator:** `lines 77-79`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-01T06:28:21.104799+00:00.  

```text
FT   TRANSMEM        59..79
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `eacc14042885f4a9bee71583e3725efd2169f7b227d732287e6adf264663178e`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU8?format=txt&versions=4)  
**Locator:** `lines 80-82`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-01T06:28:21.104799+00:00.  

```text
FT   TRANSMEM        109..129
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `eacc14042885f4a9bee71583e3725efd2169f7b227d732287e6adf264663178e`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU8?format=txt&versions=4)  
**Locator:** `lines 83-85`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-01T06:28:21.104799+00:00.  

```text
FT   TRANSMEM        142..162
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `eacc14042885f4a9bee71583e3725efd2169f7b227d732287e6adf264663178e`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU8?format=txt&versions=4)  
**Locator:** `lines 86-88`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-01T06:28:21.104799+00:00.  

```text
FT   TRANSMEM        168..188
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `eacc14042885f4a9bee71583e3725efd2169f7b227d732287e6adf264663178e`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU8?format=txt&versions=4)  
**Locator:** `lines 89-91`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-01T06:28:21.104799+00:00.  

```text
FT   TRANSMEM        225..245
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `eacc14042885f4a9bee71583e3725efd2169f7b227d732287e6adf264663178e`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 72. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
