# transmembrane_0080

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0080.txt)

**Task:** `transmembrane`  
**Expected answer:** **D** — 4..24; 81..101; 116..136; 158..178; 181..201; 228..248; 271..291; 309..329

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MLHLTPLIFLSLAMAAAVGVWGVFTWNGGFDEMDGIVASHQSTGILGLQHCPDLDRGLMSMVAFNLPVVGRNPIFPAGRRFMVQFLANVAVIPVILNTEGARAEPGSLVRYSTTWGLFSQMATSAVMCPLYGFWFVRQSGAKQTEGGTLRPLPPNKWVVPSSVLIGYGIPALLSFDPFQWGLDLQIRGILAFTLYPLCISLTARLMRKVSKKRGRSLSPEWNSTISYVAVGVVGMVSHLWYLGTGLTGYPLSGDAVSSVAGPTEVGRAAQLVLLFLQIDYVITFAAMLLLAWHELTRHQLVRSWRAAGTLAVGWLFLGPGATLAAAWALREQWLSRPRGVRGEIKQKPK

[Multiple Choices]
A. 14..34; 78..98; 114..134; 137..157; 162..182; 193..213; 235..255; 328..348; 380..400; 471..491
B. 4..24; 80..105; 116..136; 158..178; 181..201; 228..248; 271..291; 309..329
C. 81..101; 116..136; 158..178; 181..201; 228..248; 271..291; 309..329
D. 4..24; 81..101; 116..136; 158..178; 181..201; 228..248; 271..291; 309..329
```

<details>
<summary>Complete original system instructions</summary>

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

## Reviewer assessments

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt record annotates all eight regions in D as helical transmembrane regions. The evidence code is computational (ECO:0000255), so this supports the key as an annotation, not as direct experimental confirmation. The sequence also has a strongly hydrophobic N-terminal segment and multiple hydrophobic stretches consistent with membrane-spanning helices.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains an unmistakably hydrophobic N-terminal stretch around residues 4–24, which supports including that span and distinguishes D from C. Across the other choices, repeated hydrophobic stretches support the listed helices. D's 81–101 interval is a better span than B's longer 80–105 interval because that extension reaches into a more polar region; the hydrophobic-span pattern therefore gives a transferable basis for preferring D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model can use hydropathy and typical transmembrane-helix length to distinguish the choices without knowing this protein's recorded annotation. Exact boundaries remain predictions rather than guaranteed residue-level facts, but the alternatives include a clear N-terminal hydrophobic span and a longer, less plausible extension.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although predicted helix boundaries can be uncertain, D is better supported than B because B extends one candidate span into a more polar region; C omits the strongly hydrophobic N-terminal span.


### Important caveats

- The cited UniProt transmembrane annotations are computational, not direct experimental evidence.
- The reviewer-only source record matched the supplied sequence; its identity and annotations were not original model inputs.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains an unmistakably hydrophobic N-terminal stretch around residues 4–24, which supports including that span and distinguishes D from C. Across the other choices, repeated hydrophobic stretches support the listed helices. D's 81–101 interval is a better span than B's longer 80–105 interval because that extension reaches into a more polar region; the hydrophobic-span pattern therefore gives a transferable basis for preferring D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model can use hydropathy and typical transmembrane-helix length to distinguish the choices without knowing this protein's recorded annotation. Exact boundaries remain predictions rather than guaranteed residue-level facts, but the alternatives include a clear N-terminal hydrophobic span and a longer, less plausible extension."
  },
  "case_id": "transmembrane_0080",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9",
      "H10"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates all eight regions in D as helical transmembrane regions. The evidence code is computational (ECO:0000255), so this supports the key as an annotation, not as direct experimental confirmation. The sequence also has a strongly hydrophobic N-terminal segment and multiple hydrophobic stretches consistent with membrane-spanning helices."
  },
  "important_caveats": [
    "The cited UniProt transmembrane annotations are computational, not direct experimental evidence.",
    "The reviewer-only source record matched the supplied sequence; its identity and annotations were not original model inputs."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although predicted helix boundaries can be uncertain, D is better supported than B because B extends one candidate span into a more polar region; C omits the strongly hydrophobic N-terminal span."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0080",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates all eight regions in D as helical transmembrane regions. The evidence code is computational (ECO:0000255), so this supports the key as an annotation, not as direct experimental confirmation. The sequence also has a strongly hydrophobic N-terminal segment and multiple hydrophobic stretches consistent with membrane-spanning helices.",
    "evidence_ids": ["H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains an unmistakably hydrophobic N-terminal stretch around residues 4–24, which supports including that span and distinguishes D from C. Across the other choices, repeated hydrophobic stretches support the listed helices. D's 81–101 interval is a better span than B's longer 80–105 interval because that extension reaches into a more polar region; the hydrophobic-span pattern therefore gives a transferable basis for preferring D.",
    "missing_item_specific_fact": "",
    "reason": "A model can use hydropathy and typical transmembrane-helix length to distinguish the choices without knowing this protein's recorded annotation. Exact boundaries remain predictions rather than guaranteed residue-level facts, but the alternatives include a clear N-terminal hydrophobic span and a longer, less plausible extension."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although predicted helix boundaries can be uncertain, D is better supported than B because B extends one candidate span into a more polar region; C omits the strongly hydrophobic N-terminal span."
  },
  "important_caveats": [
    "The cited UniProt transmembrane annotations are computational, not direct experimental evidence.",
    "The reviewer-only source record matched the supplied sequence; its identity and annotations were not original model inputs."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P9WEG7 annotates exactly eight transmembrane helical regions at 4..24, 81..101, 116..136, 158..178, 181..201, 228..248, 271..291, and 309..329, matching option D precisely. The evidence code ECO:0000255 indicates these are computational predictions (by similarity), consistent with the task being a prediction exercise. The sequence match is confirmed (SHA-256 identical, 349 aa).

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model can distinguish D from the other options using standard TM prediction reasoning. (1) Option A is eliminated immediately because it lists regions at 380..400 and 471..491, which exceed the 349-residue protein length, and its other positions do not align with hydrophobic stretches. (2) Option C omits the N-terminal hydrophobic stretch at positions 4-24 (LHTPLIFLSLAMAAAVGVWGVFTW), which is a 21-residue segment dominated by Leu, Ile, Phe, Ala, Val, Met, and Trp — a textbook N-terminal TM helix that any hydrophobicity-based predictor would identify. (3) The critical B-vs-D distinction is the second TM boundary: B uses 80..105 (26 residues) while D uses 81..101 (21 residues). Residues 102-105 are E-P-G-S: Glu is polar, Pro is a helix breaker, Gly is conformationally flexible, and Ser is polar. None of these are compatible with a membrane-spanning alpha-helix. Standard TM helices are 18-25 residues; 21 fits well while 26 is at the upper extreme and the extra residues are clearly non-TM. A model applying hydropathy scales (e.g., Kyte-Doolittle) and helix-propensity knowledge would reject the E-P-G-S extension, favoring D. The remaining regions (116..136, 158..178, 181..201, 228..248, 271..291, 309..329) are shared across B, C, and D and correspond to identifiable hydrophobic segments in the sequence.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence itself provides sufficient information: the N-terminal hydrophobic stretch eliminates C, out-of-range positions eliminate A, and the polar/helix-breaking residues E-P-G-S at positions 102-105 eliminate B. Standard TM helix length (18-25 residues) and hydrophobicity criteria are transferable knowledge that distinguishes D from B. No exact database lookup of this specific protein's annotation is required.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While TM boundary assignments can have ±1-2 residue uncertainty in practice, the specific differences here are decisive: A has out-of-range positions, C omits an obvious N-terminal TM, and B extends a TM helix into four clearly incompatible residues (E-P-G-S). Only D is consistent with hydrophobicity, helix-propensity, and standard TM length.


### Important caveats

- The UniProt annotation uses evidence code ECO:0000255 (computational prediction by similarity), not experimental structure. The exact boundaries are predicted, not measured, so minor boundary shifts are possible in principle.
- The protein is a terpene cyclase (EC 5.4.99.-) from Aspergillus nomiae; its membrane association is inferred from sequence features and homology, not from resolved membrane-protein structures.
- The distinction between B and D rests on four residues (102-105). While the argument is strong, in a real-world prediction setting boundary uncertainty of a few residues is common; the multiple-choice format forces a discrete choice that is well-justified here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can distinguish D from the other options using standard TM prediction reasoning. (1) Option A is eliminated immediately because it lists regions at 380..400 and 471..491, which exceed the 349-residue protein length, and its other positions do not align with hydrophobic stretches. (2) Option C omits the N-terminal hydrophobic stretch at positions 4-24 (LHTPLIFLSLAMAAAVGVWGVFTW), which is a 21-residue segment dominated by Leu, Ile, Phe, Ala, Val, Met, and Trp — a textbook N-terminal TM helix that any hydrophobicity-based predictor would identify. (3) The critical B-vs-D distinction is the second TM boundary: B uses 80..105 (26 residues) while D uses 81..101 (21 residues). Residues 102-105 are E-P-G-S: Glu is polar, Pro is a helix breaker, Gly is conformationally flexible, and Ser is polar. None of these are compatible with a membrane-spanning alpha-helix. Standard TM helices are 18-25 residues; 21 fits well while 26 is at the upper extreme and the extra residues are clearly non-TM. A model applying hydropathy scales (e.g., Kyte-Doolittle) and helix-propensity knowledge would reject the E-P-G-S extension, favoring D. The remaining regions (116..136, 158..178, 181..201, 228..248, 271..291, 309..329) are shared across B, C, and D and correspond to identifiable hydrophobic segments in the sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence itself provides sufficient information: the N-terminal hydrophobic stretch eliminates C, out-of-range positions eliminate A, and the polar/helix-breaking residues E-P-G-S at positions 102-105 eliminate B. Standard TM helix length (18-25 residues) and hydrophobicity criteria are transferable knowledge that distinguishes D from B. No exact database lookup of this specific protein's annotation is required."
  },
  "case_id": "transmembrane_0080",
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
      "H3",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9",
      "H10"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P9WEG7 annotates exactly eight transmembrane helical regions at 4..24, 81..101, 116..136, 158..178, 181..201, 228..248, 271..291, and 309..329, matching option D precisely. The evidence code ECO:0000255 indicates these are computational predictions (by similarity), consistent with the task being a prediction exercise. The sequence match is confirmed (SHA-256 identical, 349 aa)."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (computational prediction by similarity), not experimental structure. The exact boundaries are predicted, not measured, so minor boundary shifts are possible in principle.",
    "The protein is a terpene cyclase (EC 5.4.99.-) from Aspergillus nomiae; its membrane association is inferred from sequence features and homology, not from resolved membrane-protein structures.",
    "The distinction between B and D rests on four residues (102-105). While the argument is strong, in a real-world prediction setting boundary uncertainty of a few residues is common; the multiple-choice format forces a discrete choice that is well-justified here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While TM boundary assignments can have ±1-2 residue uncertainty in practice, the specific differences here are decisive: A has out-of-range positions, C omits an obvious N-terminal TM, and B extends a TM helix into four clearly incompatible residues (E-P-G-S). Only D is consistent with hydrophobicity, helix-propensity, and standard TM length."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0080",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P9WEG7 annotates exactly eight transmembrane helical regions at 4..24, 81..101, 116..136, 158..178, 181..201, 228..248, 271..291, and 309..329, matching option D precisely. The evidence code ECO:0000255 indicates these are computational predictions (by similarity), consistent with the task being a prediction exercise. The sequence match is confirmed (SHA-256 identical, 349 aa).",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model can distinguish D from the other options using standard TM prediction reasoning. (1) Option A is eliminated immediately because it lists regions at 380..400 and 471..491, which exceed the 349-residue protein length, and its other positions do not align with hydrophobic stretches. (2) Option C omits the N-terminal hydrophobic stretch at positions 4-24 (LHTPLIFLSLAMAAAVGVWGVFTW), which is a 21-residue segment dominated by Leu, Ile, Phe, Ala, Val, Met, and Trp — a textbook N-terminal TM helix that any hydrophobicity-based predictor would identify. (3) The critical B-vs-D distinction is the second TM boundary: B uses 80..105 (26 residues) while D uses 81..101 (21 residues). Residues 102-105 are E-P-G-S: Glu is polar, Pro is a helix breaker, Gly is conformationally flexible, and Ser is polar. None of these are compatible with a membrane-spanning alpha-helix. Standard TM helices are 18-25 residues; 21 fits well while 26 is at the upper extreme and the extra residues are clearly non-TM. A model applying hydropathy scales (e.g., Kyte-Doolittle) and helix-propensity knowledge would reject the E-P-G-S extension, favoring D. The remaining regions (116..136, 158..178, 181..201, 228..248, 271..291, 309..329) are shared across B, C, and D and correspond to identifiable hydrophobic segments in the sequence.",
    "missing_item_specific_fact": "",
    "reason": "The sequence itself provides sufficient information: the N-terminal hydrophobic stretch eliminates C, out-of-range positions eliminate A, and the polar/helix-breaking residues E-P-G-S at positions 102-105 eliminate B. Standard TM helix length (18-25 residues) and hydrophobicity criteria are transferable knowledge that distinguishes D from B. No exact database lookup of this specific protein's annotation is required."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While TM boundary assignments can have ±1-2 residue uncertainty in practice, the specific differences here are decisive: A has out-of-range positions, C omits an obvious N-terminal TM, and B extends a TM helix into four clearly incompatible residues (E-P-G-S). Only D is consistent with hydrophobicity, helix-propensity, and standard TM length."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (computational prediction by similarity), not experimental structure. The exact boundaries are predicted, not measured, so minor boundary shifts are possible in principle.",
    "The protein is a terpene cyclase (EC 5.4.99.-) from Aspergillus nomiae; its membrane association is inferred from sequence features and homology, not from resolved membrane-protein structures.",
    "The distinction between B and D rests on four residues (102-105). While the argument is strong, in a real-world prediction setting boundary uncertainty of a few residues is common; the multiple-choice format forces a discrete choice that is well-justified here."
  ]
}
```

</details>

## Complete reviewer-only evidence and qualifications

These source excerpts were available to the reviewers. They were not included in the original benchmark-solving input.

**Source applicability:**

```json
{
  "actual_author_source_snapshot": "unknown",
  "benchmark_sequence_length": 349,
  "benchmark_sequence_sha256": "81e62647611dee5222b170056638bacd813b9736ff263a1893b00f2e83d6464a",
  "current_entry_audit": {
    "entryVersion": 4,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-02-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "cc0cb3cc56cbc60432581eb408108dc2d2be5bfdc4ea3d2699b2708dcea8ab8b",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 349,
  "current_source_sequence_sha256": "81e62647611dee5222b170056638bacd813b9736ff263a1893b00f2e83d6464a",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 2,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "P9WEG7",
  "selected_historical_entry_version": 2,
  "selected_historical_record_sha256": "20bc0e67398f5d9ca5428fba937ca2d4cf4546b725019108174063d3acb20d32",
  "selected_historical_source_sequence_length": 349,
  "selected_historical_source_sequence_sha256": "81e62647611dee5222b170056638bacd813b9736ff263a1893b00f2e83d6464a",
  "selected_historical_version": {
    "accession": "P9WEG7",
    "database": "Swiss-Prot",
    "entryVersion": 2,
    "firstRelease": "2025_02/2025_02",
    "firstReleaseDate": "23-Apr-2025",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "RSTN5_ASPN3",
    "sequenceVersion": 1
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG7.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P9WEG7\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:30:17.512806+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "cc0cb3cc56cbc60432581eb408108dc2d2be5bfdc4ea3d2699b2708dcea8ab8b",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG7.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG7.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":4,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-02-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:30:17.512806+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "cc0cb3cc56cbc60432581eb408108dc2d2be5bfdc4ea3d2699b2708dcea8ab8b",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG7.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG7.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Aspergillus\",\"Circumdati\"],\"scientificName\":\"Aspergillus nomiae NRRL (strain ATCC 15546 / NRRL 13137 / CBS 260.88 / M93)\",\"taxonId\":1509407}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:30:17.512806+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "cc0cb3cc56cbc60432581eb408108dc2d2be5bfdc4ea3d2699b2708dcea8ab8b",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG7.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG7.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33857369\",\"source\":\"PubMed\"}],\"value\":\"Restricticin biosynthesis cluster protein 5\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"33857369\",\"source\":\"PubMed\"}],\"value\":\"5.4.99.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33857369\",\"source\":\"PubMed\"}],\"value\":\"Terpene cyclase rstn5\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:30:17.512806+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "cc0cb3cc56cbc60432581eb408108dc2d2be5bfdc4ea3d2699b2708dcea8ab8b",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG7.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG7.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":24},\"start\":{\"modifier\":\"EXACT\",\"value\":4}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:30:17.512806+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "cc0cb3cc56cbc60432581eb408108dc2d2be5bfdc4ea3d2699b2708dcea8ab8b",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG7.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG7.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":101},\"start\":{\"modifier\":\"EXACT\",\"value\":81}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:30:17.512806+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "cc0cb3cc56cbc60432581eb408108dc2d2be5bfdc4ea3d2699b2708dcea8ab8b",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG7.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG7.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":136},\"start\":{\"modifier\":\"EXACT\",\"value\":116}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:30:17.512806+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "cc0cb3cc56cbc60432581eb408108dc2d2be5bfdc4ea3d2699b2708dcea8ab8b",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG7.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG7.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":178},\"start\":{\"modifier\":\"EXACT\",\"value\":158}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:30:17.512806+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "cc0cb3cc56cbc60432581eb408108dc2d2be5bfdc4ea3d2699b2708dcea8ab8b",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG7.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG7.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":201},\"start\":{\"modifier\":\"EXACT\",\"value\":181}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:30:17.512806+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "cc0cb3cc56cbc60432581eb408108dc2d2be5bfdc4ea3d2699b2708dcea8ab8b",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG7.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG7.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":248},\"start\":{\"modifier\":\"EXACT\",\"value\":228}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:30:17.512806+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "cc0cb3cc56cbc60432581eb408108dc2d2be5bfdc4ea3d2699b2708dcea8ab8b",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG7.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG7.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":291},\"start\":{\"modifier\":\"EXACT\",\"value\":271}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:30:17.512806+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "cc0cb3cc56cbc60432581eb408108dc2d2be5bfdc4ea3d2699b2708dcea8ab8b",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG7.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG7.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":329},\"start\":{\"modifier\":\"EXACT\",\"value\":309}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:30:17.512806+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "cc0cb3cc56cbc60432581eb408108dc2d2be5bfdc4ea3d2699b2708dcea8ab8b",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG7.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG7.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"citation\":{\"authors\":[\"Liu N.\",\"Abramyan E.D.\",\"Cheng W.\",\"Perlatti B.\",\"Harvey C.J.B.\",\"Bills G.F.\",\"Tang Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33857369\"},{\"database\":\"DOI\",\"id\":\"10.1021/jacs.1c01516\"}],\"citationType\":\"journal article\",\"firstPage\":\"6043\",\"id\":\"33857369\",\"journal\":\"J. Am. Chem. Soc.\",\"lastPage\":\"6047\",\"publicationDate\":\"2021\",\"title\":\"Targeted genome mining reveals the biosynthetic gene clusters of natural product CYP51 inhibitors.\",\"volume\":\"143\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:30:17.512806+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "cc0cb3cc56cbc60432581eb408108dc2d2be5bfdc4ea3d2699b2708dcea8ab8b",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG7.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEG7?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H1",
  "excerpt": "ID   RSTN5_ASPN3             Reviewed;         349 AA.\nAC   P9WEG7;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-FEB-2025, sequence version 1.\nDT   09-APR-2025, entry version 2.\nDE   RecName: Full=Terpene cyclase rstn5 {ECO:0000303|PubMed:33857369};\nDE            EC=5.4.99.- {ECO:0000305|PubMed:33857369};\nDE   AltName: Full=Restricticin biosynthesis cluster protein 5 {ECO:0000303|PubMed:33857369};\nGN   Name=rstn5 {ECO:0000303|PubMed:33857369};\nOS   Aspergillus nomiae NRRL (strain ATCC 15546 / NRRL 13137 / CBS 260.88 /\nOS   M93).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;\nOC   Aspergillus subgen. Circumdati.\nOX   NCBI_TaxID=1509407;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:21.947384+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "20bc0e67398f5d9ca5428fba937ca2d4cf4546b725019108174063d3acb20d32",
  "url": "https://rest.uniprot.org/unisave/P9WEG7?format=txt&versions=2"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEG7?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, AND PATHWAY.\nRX   PubMed=33857369; DOI=10.1021/jacs.1c01516;\nRA   Liu N., Abramyan E.D., Cheng W., Perlatti B., Harvey C.J.B., Bills G.F.,\nRA   Tang Y.;\nRT   \"Targeted genome mining reveals the biosynthetic gene clusters of natural\nRT   product CYP51 inhibitors.\";\nRL   J. Am. Chem. Soc. 143:6043-6047(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:21.947384+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 24-31",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "20bc0e67398f5d9ca5428fba937ca2d4cf4546b725019108174063d3acb20d32",
  "url": "https://rest.uniprot.org/unisave/P9WEG7?format=txt&versions=2"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEG7?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H3",
  "excerpt": "FT   TRANSMEM        4..24\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:21.947384+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 66-68",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "20bc0e67398f5d9ca5428fba937ca2d4cf4546b725019108174063d3acb20d32",
  "url": "https://rest.uniprot.org/unisave/P9WEG7?format=txt&versions=2"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEG7?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H4",
  "excerpt": "FT   TRANSMEM        81..101\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:21.947384+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 69-71",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "20bc0e67398f5d9ca5428fba937ca2d4cf4546b725019108174063d3acb20d32",
  "url": "https://rest.uniprot.org/unisave/P9WEG7?format=txt&versions=2"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEG7?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H5",
  "excerpt": "FT   TRANSMEM        116..136\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:21.947384+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 72-74",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "20bc0e67398f5d9ca5428fba937ca2d4cf4546b725019108174063d3acb20d32",
  "url": "https://rest.uniprot.org/unisave/P9WEG7?format=txt&versions=2"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEG7?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H6",
  "excerpt": "FT   TRANSMEM        158..178\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:21.947384+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 75-77",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "20bc0e67398f5d9ca5428fba937ca2d4cf4546b725019108174063d3acb20d32",
  "url": "https://rest.uniprot.org/unisave/P9WEG7?format=txt&versions=2"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEG7?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H7",
  "excerpt": "FT   TRANSMEM        181..201\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:21.947384+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 78-80",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "20bc0e67398f5d9ca5428fba937ca2d4cf4546b725019108174063d3acb20d32",
  "url": "https://rest.uniprot.org/unisave/P9WEG7?format=txt&versions=2"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEG7?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H8",
  "excerpt": "FT   TRANSMEM        228..248\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:21.947384+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 81-83",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "20bc0e67398f5d9ca5428fba937ca2d4cf4546b725019108174063d3acb20d32",
  "url": "https://rest.uniprot.org/unisave/P9WEG7?format=txt&versions=2"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEG7?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H9",
  "excerpt": "FT   TRANSMEM        271..291\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:21.947384+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 84-86",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "20bc0e67398f5d9ca5428fba937ca2d4cf4546b725019108174063d3acb20d32",
  "url": "https://rest.uniprot.org/unisave/P9WEG7?format=txt&versions=2"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEG7?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H10",
  "excerpt": "FT   TRANSMEM        309..329\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:21.947384+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 87-89",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "20bc0e67398f5d9ca5428fba937ca2d4cf4546b725019108174063d3acb20d32",
  "url": "https://rest.uniprot.org/unisave/P9WEG7?format=txt&versions=2"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 80. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
