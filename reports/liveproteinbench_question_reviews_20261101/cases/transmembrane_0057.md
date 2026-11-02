# transmembrane_0057

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **B** — 30..50; 62..82; 108..128; 144..164; 186..206; 327..347; 357..377

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTQLPYLLDRRGGALAAPATAWGDMMLNRALFSVALLSSVGSAWVVLSYACIKELRSYRHQLILGLAISDLLMSLNFMFSAGWNVAGGDLALEESRTACSVNGFLTQVFVVQTDWWILVIAIATYIILGNFKTQSQFIQTHVWIPWVGPWVLSIIIAAICHGVLGYGYIGGWCWLTSDLMRLLINFIPRWLIVIAIALIYIRLYMIVRKARKWDIEGVSPDPGDDMADTSVILMSVGKKDRERQGSGVLVSRDVSVSFGRKGSTAPTFVTMVTTSGAGDSREAISSCSAREEGSRARTVNVNSSRSLSLGMRQPLNAAQLKRIAKKMMVYPVAYAIIWACPTAIRIYQGTTGSRAPLWITIVDKSCIVIQGLVDAVVYGLNERAWQGWRDHIRRIIYKNEGGRIIG

[Multiple Choices]
A. 139..159; 176..196; 247..267; 272..292; 297..317
B. 30..50; 62..82; 108..128; 144..164; 186..206; 327..347; 357..377
C. 30..50; 62..82; 108..128; 144..164; 186..206; 327..347
D. 30..50; 62..82; 108..128; 144..164; 186..206; 328..343; 357..377
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

> The sequence matches the referenced UniProt entry, whose annotation lists all seven regions in choice B as transmembrane helices. These are computational annotations (ECO:0000255), not evidence of direct experimental determination of the boundaries.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [H4](#evidence-h4), [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains hydrophobic stretches consistent with membrane-spanning helices, including near the C-terminus. That supports the general prediction of membrane regions but does not establish their exact residue boundaries.


**Missing item-specific fact**

> The protein-specific transmembrane-region assignments and precise boundaries, particularly the choice between the full 327..347 interval and the shortened 328..343 interval.


**Reason**

> Selecting the exact listed coordinates depends on protein-specific annotation or a prediction beyond what general membrane-protein knowledge establishes. The reviewer-only UniProt evidence supports the key but was not supplied to the evaluated model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence supports hydrophobic membrane-spanning regions, but it does not independently validate exact endpoints. Among the choices, B is supported by the matched annotation; the other options omit or truncate candidate regions.


### Important caveats

- The supplied evidence identifies the regions as computationally annotated helical transmembrane segments, not experimentally established boundaries.
- The author’s source snapshot is unknown, though the matching sequence occurs in both the historical and current UniProt records.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hydrophobic stretches consistent with membrane-spanning helices, including near the C-terminus. That supports the general prediction of membrane regions but does not establish their exact residue boundaries.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific transmembrane-region assignments and precise boundaries, particularly the choice between the full 327..347 interval and the shortened 328..343 interval.",
    "reason": "Selecting the exact listed coordinates depends on protein-specific annotation or a prediction beyond what general membrane-protein knowledge establishes. The reviewer-only UniProt evidence supports the key but was not supplied to the evaluated model."
  },
  "case_id": "transmembrane_0057",
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
    "reason": "The sequence matches the referenced UniProt entry, whose annotation lists all seven regions in choice B as transmembrane helices. These are computational annotations (ECO:0000255), not evidence of direct experimental determination of the boundaries."
  },
  "important_caveats": [
    "The supplied evidence identifies the regions as computationally annotated helical transmembrane segments, not experimentally established boundaries.",
    "The author’s source snapshot is unknown, though the matching sequence occurs in both the historical and current UniProt records."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence supports hydrophobic membrane-spanning regions, but it does not independently validate exact endpoints. Among the choices, B is supported by the matched annotation; the other options omit or truncate candidate regions."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0057",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the referenced UniProt entry, whose annotation lists all seven regions in choice B as transmembrane helices. These are computational annotations (ECO:0000255), not evidence of direct experimental determination of the boundaries.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "H4", "H6", "H8", "H10", "H12", "H14", "H16"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains hydrophobic stretches consistent with membrane-spanning helices, including near the C-terminus. That supports the general prediction of membrane regions but does not establish their exact residue boundaries.",
    "missing_item_specific_fact": "The protein-specific transmembrane-region assignments and precise boundaries, particularly the choice between the full 327..347 interval and the shortened 328..343 interval.",
    "reason": "Selecting the exact listed coordinates depends on protein-specific annotation or a prediction beyond what general membrane-protein knowledge establishes. The reviewer-only UniProt evidence supports the key but was not supplied to the evaluated model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence supports hydrophobic membrane-spanning regions, but it does not independently validate exact endpoints. Among the choices, B is supported by the matched annotation; the other options omit or truncate candidate regions."
  },
  "important_caveats": [
    "The supplied evidence identifies the regions as computationally annotated helical transmembrane segments, not experimentally established boundaries.",
    "The author’s source snapshot is unknown, though the matching sequence occurs in both the historical and current UniProt records."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for G1X9E2 (Ascaroside receptor GPR2, a GPCR from Arthrobotrys oligospora) lists exactly 7 transmembrane helices at positions 30..50, 62..82, 108..128, 144..164, 186..206, 327..347, and 357..377, matching option B precisely. However, all TM annotations carry evidence code ECO:0000255 ('By similarity'), indicating computational prediction rather than experimental determination. The 7-TM topology is consistent with the protein's classification as a GPCR (supported by PubMed:38649409 functional study). The sequence match is confirmed (SHA256 identical, 406 AA).

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C4](#evidence-c4), [H4](#evidence-h4), [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein is a GPCR (7-TM receptor). Option C lists only 6 TM regions, violating GPCR topology. Option A's positions (139..159, 176..196, 247..267, 272..292, 297..317) do not correspond to hydrophobic stretches in the sequence and are inconsistent with GPCR architecture. The critical B-vs-D distinction concerns TM6: option D gives 328..343 (16 residues ≈ 24 Å helix length), which is too short to span the ~30 Å hydrophobic core of a lipid bilayer in an α-helical conformation (requires ≥20 residues). Option B's 327..347 (21 residues ≈ 31.5 Å) is consistent with canonical TM helix length. Additionally, the hydrophobicity profile around positions 344–347 remains sufficiently hydrophobic to include those residues in the TM segment.


**Missing item-specific fact**

> The exact boundary residue (327 vs 328, 347 vs 343) is determined by a specific computational predictor (ECO:0000255). A model without access to the exact prediction tool output must rely on hydrophobicity judgment and helix-length reasoning, which strongly but not absolutely favors 21 over 16 residues.


**Reason**

> General GPCR knowledge (7 TM helices) eliminates C. Hydrophobicity pattern analysis eliminates A. The B-vs-D distinction is addressable via helix-length biophysics (16 residues is marginal/too short for membrane spanning), though the exact boundary is somewhat predictor-dependent. Overall, reasoning provides meaningful grounds to select B.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While the exact TM boundary (327 vs 328, 347 vs 343) is somewhat arbitrary from a prediction standpoint, the 16-residue option (D) is biophysically implausible for a membrane-spanning helix, making B the clearly more defensible choice. No other option is equally defensible.


### Important caveats

- All UniProt TM annotations use evidence code ECO:0000255 (By similarity/computational prediction), not experimental structural data. Exact boundaries reflect a specific prediction algorithm's output.
- The protein was identified as GPR2 (Ascaroside receptor) via a 2024 Nature Microbiology paper (PubMed:38649409) demonstrating GPCR function, supporting the 7-TM topology assignment.
- The distinction between B and D (TM6: 327..347 vs 328..343) is a 5-residue boundary difference; while the 16-residue helix in D is biophysically marginal, a very aggressive TM predictor might output shorter boundaries. The reasoning argument (helix length) is strong but not mathematically airtight.
- Option A's positions appear to be a distractor with no correspondence to actual hydrophobic TM stretches in the sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein is a GPCR (7-TM receptor). Option C lists only 6 TM regions, violating GPCR topology. Option A's positions (139..159, 176..196, 247..267, 272..292, 297..317) do not correspond to hydrophobic stretches in the sequence and are inconsistent with GPCR architecture. The critical B-vs-D distinction concerns TM6: option D gives 328..343 (16 residues ≈ 24 Å helix length), which is too short to span the ~30 Å hydrophobic core of a lipid bilayer in an α-helical conformation (requires ≥20 residues). Option B's 327..347 (21 residues ≈ 31.5 Å) is consistent with canonical TM helix length. Additionally, the hydrophobicity profile around positions 344–347 remains sufficiently hydrophobic to include those residues in the TM segment.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact boundary residue (327 vs 328, 347 vs 343) is determined by a specific computational predictor (ECO:0000255). A model without access to the exact prediction tool output must rely on hydrophobicity judgment and helix-length reasoning, which strongly but not absolutely favors 21 over 16 residues.",
    "reason": "General GPCR knowledge (7 TM helices) eliminates C. Hydrophobicity pattern analysis eliminates A. The B-vs-D distinction is addressable via helix-length biophysics (16 residues is marginal/too short for membrane spanning), though the exact boundary is somewhat predictor-dependent. Overall, reasoning provides meaningful grounds to select B."
  },
  "case_id": "transmembrane_0057",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C8",
      "C10",
      "C12",
      "C14",
      "C16",
      "C18",
      "C4",
      "H4",
      "H6",
      "H8",
      "H10",
      "H12",
      "H14",
      "H16",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for G1X9E2 (Ascaroside receptor GPR2, a GPCR from Arthrobotrys oligospora) lists exactly 7 transmembrane helices at positions 30..50, 62..82, 108..128, 144..164, 186..206, 327..347, and 357..377, matching option B precisely. However, all TM annotations carry evidence code ECO:0000255 ('By similarity'), indicating computational prediction rather than experimental determination. The 7-TM topology is consistent with the protein's classification as a GPCR (supported by PubMed:38649409 functional study). The sequence match is confirmed (SHA256 identical, 406 AA)."
  },
  "important_caveats": [
    "All UniProt TM annotations use evidence code ECO:0000255 (By similarity/computational prediction), not experimental structural data. Exact boundaries reflect a specific prediction algorithm's output.",
    "The protein was identified as GPR2 (Ascaroside receptor) via a 2024 Nature Microbiology paper (PubMed:38649409) demonstrating GPCR function, supporting the 7-TM topology assignment.",
    "The distinction between B and D (TM6: 327..347 vs 328..343) is a 5-residue boundary difference; while the 16-residue helix in D is biophysically marginal, a very aggressive TM predictor might output shorter boundaries. The reasoning argument (helix length) is strong but not mathematically airtight.",
    "Option A's positions appear to be a distractor with no correspondence to actual hydrophobic TM stretches in the sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the exact TM boundary (327 vs 328, 347 vs 343) is somewhat arbitrary from a prediction standpoint, the 16-residue option (D) is biophysically implausible for a membrane-spanning helix, making B the clearly more defensible choice. No other option is equally defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0057",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for G1X9E2 (Ascaroside receptor GPR2, a GPCR from Arthrobotrys oligospora) lists exactly 7 transmembrane helices at positions 30..50, 62..82, 108..128, 144..164, 186..206, 327..347, and 357..377, matching option B precisely. However, all TM annotations carry evidence code ECO:0000255 ('By similarity'), indicating computational prediction rather than experimental determination. The 7-TM topology is consistent with the protein's classification as a GPCR (supported by PubMed:38649409 functional study). The sequence match is confirmed (SHA256 identical, 406 AA).",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "C4", "H4", "H6", "H8", "H10", "H12", "H14", "H16", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein is a GPCR (7-TM receptor). Option C lists only 6 TM regions, violating GPCR topology. Option A's positions (139..159, 176..196, 247..267, 272..292, 297..317) do not correspond to hydrophobic stretches in the sequence and are inconsistent with GPCR architecture. The critical B-vs-D distinction concerns TM6: option D gives 328..343 (16 residues ≈ 24 Å helix length), which is too short to span the ~30 Å hydrophobic core of a lipid bilayer in an α-helical conformation (requires ≥20 residues). Option B's 327..347 (21 residues ≈ 31.5 Å) is consistent with canonical TM helix length. Additionally, the hydrophobicity profile around positions 344–347 remains sufficiently hydrophobic to include those residues in the TM segment.",
    "missing_item_specific_fact": "The exact boundary residue (327 vs 328, 347 vs 343) is determined by a specific computational predictor (ECO:0000255). A model without access to the exact prediction tool output must rely on hydrophobicity judgment and helix-length reasoning, which strongly but not absolutely favors 21 over 16 residues.",
    "reason": "General GPCR knowledge (7 TM helices) eliminates C. Hydrophobicity pattern analysis eliminates A. The B-vs-D distinction is addressable via helix-length biophysics (16 residues is marginal/too short for membrane spanning), though the exact boundary is somewhat predictor-dependent. Overall, reasoning provides meaningful grounds to select B."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the exact TM boundary (327 vs 328, 347 vs 343) is somewhat arbitrary from a prediction standpoint, the 16-residue option (D) is biophysically implausible for a membrane-spanning helix, making B the clearly more defensible choice. No other option is equally defensible."
  },
  "important_caveats": [
    "All UniProt TM annotations use evidence code ECO:0000255 (By similarity/computational prediction), not experimental structural data. Exact boundaries reflect a specific prediction algorithm's output.",
    "The protein was identified as GPR2 (Ascaroside receptor) via a 2024 Nature Microbiology paper (PubMed:38649409) demonstrating GPCR function, supporting the 7-TM topology assignment.",
    "The distinction between B and D (TM6: 327..347 vs 328..343) is a 5-residue boundary difference; while the 16-residue helix in D is biophysically marginal, a very aggressive TM predictor might output shorter boundaries. The reasoning argument (helix length) is strong but not mathematically airtight.",
    "Option A's positions appear to be a distractor with no correspondence to actual hydrophobic TM stretches in the sequence."
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

**Accession:** `G1X9E2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 45. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:30.739464+00:00.  

```json
{"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Ascaroside receptor GPR2"}}}
```

Source SHA-256: `d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:30.739464+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":50},"start":{"modifier":"EXACT","value":30}},"type":"Transmembrane"}
```

Source SHA-256: `d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:30.739464+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":82},"start":{"modifier":"EXACT","value":62}},"type":"Transmembrane"}
```

Source SHA-256: `d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:30.739464+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":128},"start":{"modifier":"EXACT","value":108}},"type":"Transmembrane"}
```

Source SHA-256: `d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)  
**Locator:** `/features/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:30.739464+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":164},"start":{"modifier":"EXACT","value":144}},"type":"Transmembrane"}
```

Source SHA-256: `d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f`.

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)  
**Locator:** `/features/10`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:30.739464+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":206},"start":{"modifier":"EXACT","value":186}},"type":"Transmembrane"}
```

Source SHA-256: `d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f`.

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)  
**Locator:** `/features/12`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:30.739464+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":347},"start":{"modifier":"EXACT","value":327}},"type":"Transmembrane"}
```

Source SHA-256: `d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f`.

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)  
**Locator:** `/features/14`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:30.739464+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":377},"start":{"modifier":"EXACT","value":357}},"type":"Transmembrane"}
```

Source SHA-256: `d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45)  
**Locator:** `lines 25-34`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 45 / 1.  
**Retrieved:** 2026-11-02T04:28:32.723564+00:00.  

```text
RN   [2] {ECO:0000305}
RP   FUNCTION, INTERACTION WITH GPA2 AND GPR3, SUBCELLULAR LOCATION, INDUCTION,
RP   AND DISRUPTION PHENOTYPE.
RC   STRAIN=TWF154 {ECO:0000303|PubMed:38649409};
RX   PubMed=38649409; DOI=10.1038/s41564-024-01679-w;
RA   Kuo C.Y., Tay R.J., Lin H.C., Juan S.C., Vidal-Diez de Ulzurrun G.,
RA   Chang Y.C., Hoki J., Schroeder F.C., Hsueh Y.P.;
RT   "The nematode-trapping fungus Arthrobotrys oligospora detects prey
RT   pheromones via G protein-coupled receptors.";
RL   Nat. Microbiol. 9:1738-1751(2024).
```

Source SHA-256: `e35d509b45ea64e3eac1fedae5691280c0fa8c7205a8651df542bc73ee054a3f`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45)  
**Locator:** `lines 97-99`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 45 / 1.  
**Retrieved:** 2026-11-02T04:28:32.723564+00:00.  

```text
FT   TRANSMEM        30..50
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `e35d509b45ea64e3eac1fedae5691280c0fa8c7205a8651df542bc73ee054a3f`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45)  
**Locator:** `lines 103-105`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 45 / 1.  
**Retrieved:** 2026-11-02T04:28:32.723564+00:00.  

```text
FT   TRANSMEM        62..82
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `e35d509b45ea64e3eac1fedae5691280c0fa8c7205a8651df542bc73ee054a3f`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45)  
**Locator:** `lines 109-111`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 45 / 1.  
**Retrieved:** 2026-11-02T04:28:32.723564+00:00.  

```text
FT   TRANSMEM        108..128
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `e35d509b45ea64e3eac1fedae5691280c0fa8c7205a8651df542bc73ee054a3f`.

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45)  
**Locator:** `lines 115-117`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 45 / 1.  
**Retrieved:** 2026-11-02T04:28:32.723564+00:00.  

```text
FT   TRANSMEM        144..164
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `e35d509b45ea64e3eac1fedae5691280c0fa8c7205a8651df542bc73ee054a3f`.

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45)  
**Locator:** `lines 121-123`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 45 / 1.  
**Retrieved:** 2026-11-02T04:28:32.723564+00:00.  

```text
FT   TRANSMEM        186..206
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `e35d509b45ea64e3eac1fedae5691280c0fa8c7205a8651df542bc73ee054a3f`.

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45)  
**Locator:** `lines 127-129`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 45 / 1.  
**Retrieved:** 2026-11-02T04:28:32.723564+00:00.  

```text
FT   TRANSMEM        327..347
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `e35d509b45ea64e3eac1fedae5691280c0fa8c7205a8651df542bc73ee054a3f`.

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45)  
**Locator:** `lines 133-135`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 45 / 1.  
**Retrieved:** 2026-11-02T04:28:32.723564+00:00.  

```text
FT   TRANSMEM        357..377
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `e35d509b45ea64e3eac1fedae5691280c0fa8c7205a8651df542bc73ee054a3f`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 57. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
