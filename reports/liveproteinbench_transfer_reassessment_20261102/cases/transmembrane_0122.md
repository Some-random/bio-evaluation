# transmembrane_0122

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0122.txt)

**Task:** `transmembrane`  
**Expected answer:** **D** — 29..49; 60..80; 117..137; 158..178; 179..199

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSIIGSFPPGGPRVEVQETRVQTDRVLTIPNILSMARLAGVPLFLWLILRPEFGGPQSDGWALLVLALSGVSDYLDGKLARRWNQISSLGRLLDPAADRLYILSTLVGLTWREILPLWLTLVLLAREAMLLVMVGILRRHGYPPPQVNFLGKAATFNLMYAFPLLLLSDGSGWIASLAAVFGWAFAGWGTTLYWWAGVLYVVQVRRLVRADVAAD

[Multiple Choices]
A. 179..199; 357..377
B. 29..49; 60..80; 158..178; 179..199
C. 29..49; 62..77; 117..137; 158..178; 179..199
D. 29..49; 60..80; 117..137; 158..178; 179..199
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

> The sequence-matched UniProt records annotate all five spans listed in D as transmembrane helices, supporting the key. The annotations carry computational evidence code ECO:0000255, so they support the prediction but do not establish experimental confirmation.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains several hydrophobic stretches characteristic of membrane-spanning helices. In particular, 117..137 is strongly hydrophobic and distinguishes D from B, while 60..80 captures a longer, more typical helix-length interval than C's shorter 62..77 segment. The final two listed intervals are also present in the alternatives that include them.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and transferable knowledge about hydrophobic membrane helices provide a meaningful basis for preferring D among these options, although they do not independently establish exact boundaries or guarantee the predicted topology.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The nearby alternative boundary for the 60-region is a source of uncertainty, but the longer interval in D is more consistent with a typical membrane-spanning helix, and the sequence supports the additional span that distinguishes D from B.


### Important caveats

- The supporting database spans are computationally annotated, not shown here to be experimentally mapped.
- Exact transmembrane boundaries can be uncertain from sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains several hydrophobic stretches characteristic of membrane-spanning helices. In particular, 117..137 is strongly hydrophobic and distinguishes D from B, while 60..80 captures a longer, more typical helix-length interval than C's shorter 62..77 segment. The final two listed intervals are also present in the alternatives that include them.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and transferable knowledge about hydrophobic membrane helices provide a meaningful basis for preferring D among these options, although they do not independently establish exact boundaries or guarantee the predicted topology."
  },
  "case_id": "transmembrane_0122",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt records annotate all five spans listed in D as transmembrane helices, supporting the key. The annotations carry computational evidence code ECO:0000255, so they support the prediction but do not establish experimental confirmation."
  },
  "important_caveats": [
    "The supporting database spans are computationally annotated, not shown here to be experimentally mapped.",
    "Exact transmembrane boundaries can be uncertain from sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The nearby alternative boundary for the 60-region is a source of uncertainty, but the longer interval in D is more consistent with a typical membrane-spanning helix, and the sequence supports the additional span that distinguishes D from B."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0122",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt records annotate all five spans listed in D as transmembrane helices, supporting the key. The annotations carry computational evidence code ECO:0000255, so they support the prediction but do not establish experimental confirmation.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains several hydrophobic stretches characteristic of membrane-spanning helices. In particular, 117..137 is strongly hydrophobic and distinguishes D from B, while 60..80 captures a longer, more typical helix-length interval than C's shorter 62..77 segment. The final two listed intervals are also present in the alternatives that include them.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and transferable knowledge about hydrophobic membrane helices provide a meaningful basis for preferring D among these options, although they do not independently establish exact boundaries or guarantee the predicted topology."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The nearby alternative boundary for the 60-region is a source of uncertainty, but the longer interval in D is more consistent with a typical membrane-spanning helix, and the sequence supports the additional span that distinguishes D from B."
  },
  "important_caveats": [
    "The supporting database spans are computationally annotated, not shown here to be experimentally mapped.",
    "Exact transmembrane boundaries can be uncertain from sequence alone."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for Q9KZP3 (Cardiolipin synthase, CMP-forming) lists exactly five transmembrane helical segments at 29..49, 60..80, 117..137, 158..178, and 179..199, matching option D precisely. However, all five annotations carry evidence code ECO:0000255 (inferred by similarity/computational prediction), not experimental evidence. The answer is supported by the database annotation, though the underlying evidence is computational rather than experimentally validated.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Option A is immediately eliminated because position 357 exceeds the 215-residue protein length. Option B (four TM segments) is eliminated because the region 117-137 (LWLTLLVLLAREAMLLVMVGIL) is strongly hydrophobic (L, W, L, L, V, L, L, A, M, L, L, V, M, V, I, L) and should be recognized as a TM helix by any hydrophobicity analysis, making omission unjustifiable. The critical distinction between C and D is the second segment: C proposes 62-77 (16 residues: ALLVLALSGVSDYLDG) while D proposes 60-80 (21 residues: GWALLVLALSGVSDYLDGKLA). A general biophysical principle states that alpha-helical TM segments require approximately 18-25 residues to span the ~30 Å hydrophobic core of the lipid bilayer. A 16-residue segment is below this threshold and would not span the membrane, while a 21-residue segment falls within the expected range. This length criterion, learned from the general principle of membrane-spanning helix geometry applicable to all membrane proteins, meaningfully eliminates C and selects D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence itself provides sufficient information: (1) out-of-range position eliminates A, (2) the clearly hydrophobic 117-137 stretch eliminates B, and (3) the universal biophysical requirement that TM helices be ~18-25 residues long eliminates the 16-residue 62-77 option in C. These are general principles of membrane protein biophysics transferable across all membrane proteins, not facts specific to this exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options are sufficiently distinct: A has an impossible position, B omits a clearly hydrophobic segment, C uses a too-short segment, and D satisfies all criteria. No two options are equally defensible given the sequence and general TM helix length requirements.


### Important caveats

- All five UniProt TM annotations carry ECO:0000255 (computational/similarity-based inference), not experimental evidence. The exact boundaries may differ from experimental determination.
- The 60-80 region is relatively mixed in hydrophobicity (contains D, K, S, G residues), making it the weakest TM candidate among the five. A strict hydrophobicity threshold might exclude it, but the annotation includes it.
- The reviewer-only evidence (UniProt accession, organism, protein name) was not available to the evaluated model; the reasoning above relies only on the sequence and general biophysical principles.
- The 29-49 region is also borderline in hydrophobicity, containing P, N, S, R, G residues interspersed with hydrophobic ones, but is included in the annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Option A is immediately eliminated because position 357 exceeds the 215-residue protein length. Option B (four TM segments) is eliminated because the region 117-137 (LWLTLLVLLAREAMLLVMVGIL) is strongly hydrophobic (L, W, L, L, V, L, L, A, M, L, L, V, M, V, I, L) and should be recognized as a TM helix by any hydrophobicity analysis, making omission unjustifiable. The critical distinction between C and D is the second segment: C proposes 62-77 (16 residues: ALLVLALSGVSDYLDG) while D proposes 60-80 (21 residues: GWALLVLALSGVSDYLDGKLA). A general biophysical principle states that alpha-helical TM segments require approximately 18-25 residues to span the ~30 Å hydrophobic core of the lipid bilayer. A 16-residue segment is below this threshold and would not span the membrane, while a 21-residue segment falls within the expected range. This length criterion, learned from the general principle of membrane-spanning helix geometry applicable to all membrane proteins, meaningfully eliminates C and selects D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence itself provides sufficient information: (1) out-of-range position eliminates A, (2) the clearly hydrophobic 117-137 stretch eliminates B, and (3) the universal biophysical requirement that TM helices be ~18-25 residues long eliminates the 16-residue 62-77 option in C. These are general principles of membrane protein biophysics transferable across all membrane proteins, not facts specific to this exact protein."
  },
  "case_id": "transmembrane_0122",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for Q9KZP3 (Cardiolipin synthase, CMP-forming) lists exactly five transmembrane helical segments at 29..49, 60..80, 117..137, 158..178, and 179..199, matching option D precisely. However, all five annotations carry evidence code ECO:0000255 (inferred by similarity/computational prediction), not experimental evidence. The answer is supported by the database annotation, though the underlying evidence is computational rather than experimentally validated."
  },
  "important_caveats": [
    "All five UniProt TM annotations carry ECO:0000255 (computational/similarity-based inference), not experimental evidence. The exact boundaries may differ from experimental determination.",
    "The 60-80 region is relatively mixed in hydrophobicity (contains D, K, S, G residues), making it the weakest TM candidate among the five. A strict hydrophobicity threshold might exclude it, but the annotation includes it.",
    "The reviewer-only evidence (UniProt accession, organism, protein name) was not available to the evaluated model; the reasoning above relies only on the sequence and general biophysical principles.",
    "The 29-49 region is also borderline in hydrophobicity, containing P, N, S, R, G residues interspersed with hydrophobic ones, but is included in the annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are sufficiently distinct: A has an impossible position, B omits a clearly hydrophobic segment, C uses a too-short segment, and D satisfies all criteria. No two options are equally defensible given the sequence and general TM helix length requirements."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0122",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for Q9KZP3 (Cardiolipin synthase, CMP-forming) lists exactly five transmembrane helical segments at 29..49, 60..80, 117..137, 158..178, and 179..199, matching option D precisely. However, all five annotations carry evidence code ECO:0000255 (inferred by similarity/computational prediction), not experimental evidence. The answer is supported by the database annotation, though the underlying evidence is computational rather than experimentally validated.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "H4", "H5", "H6", "H7", "H8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Option A is immediately eliminated because position 357 exceeds the 215-residue protein length. Option B (four TM segments) is eliminated because the region 117-137 (LWLTLLVLLAREAMLLVMVGIL) is strongly hydrophobic (L, W, L, L, V, L, L, A, M, L, L, V, M, V, I, L) and should be recognized as a TM helix by any hydrophobicity analysis, making omission unjustifiable. The critical distinction between C and D is the second segment: C proposes 62-77 (16 residues: ALLVLALSGVSDYLDG) while D proposes 60-80 (21 residues: GWALLVLALSGVSDYLDGKLA). A general biophysical principle states that alpha-helical TM segments require approximately 18-25 residues to span the ~30 Å hydrophobic core of the lipid bilayer. A 16-residue segment is below this threshold and would not span the membrane, while a 21-residue segment falls within the expected range. This length criterion, learned from the general principle of membrane-spanning helix geometry applicable to all membrane proteins, meaningfully eliminates C and selects D.",
    "missing_item_specific_fact": "",
    "reason": "The sequence itself provides sufficient information: (1) out-of-range position eliminates A, (2) the clearly hydrophobic 117-137 stretch eliminates B, and (3) the universal biophysical requirement that TM helices be ~18-25 residues long eliminates the 16-residue 62-77 option in C. These are general principles of membrane protein biophysics transferable across all membrane proteins, not facts specific to this exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are sufficiently distinct: A has an impossible position, B omits a clearly hydrophobic segment, C uses a too-short segment, and D satisfies all criteria. No two options are equally defensible given the sequence and general TM helix length requirements."
  },
  "important_caveats": [
    "All five UniProt TM annotations carry ECO:0000255 (computational/similarity-based inference), not experimental evidence. The exact boundaries may differ from experimental determination.",
    "The 60-80 region is relatively mixed in hydrophobicity (contains D, K, S, G residues), making it the weakest TM candidate among the five. A strict hydrophobicity threshold might exclude it, but the annotation includes it.",
    "The reviewer-only evidence (UniProt accession, organism, protein name) was not available to the evaluated model; the reasoning above relies only on the sequence and general biophysical principles.",
    "The 29-49 region is also borderline in hydrophobicity, containing P, N, S, R, G residues interspersed with hydrophobic ones, but is included in the annotation."
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
  "benchmark_sequence_length": 215,
  "benchmark_sequence_sha256": "4d7ff8f97540a27b3e75118f82df28e82087f33a3652f781a7c4f3611ee726bb",
  "current_entry_audit": {
    "entryVersion": 120,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2000-10-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "19159a513ac84423a492087d8961c46891339eef5cec5a9d995ec98e1cfe717c",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 215,
  "current_source_sequence_sha256": "4d7ff8f97540a27b3e75118f82df28e82087f33a3652f781a7c4f3611ee726bb",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 118,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9KZP3",
  "selected_historical_entry_version": 118,
  "selected_historical_record_sha256": "40068827609c34109c814e2d2c856e36a3bec9b7c2775a90bbcc5f7a21726d79",
  "selected_historical_source_sequence_length": 215,
  "selected_historical_source_sequence_sha256": "4d7ff8f97540a27b3e75118f82df28e82087f33a3652f781a7c4f3611ee726bb",
  "selected_historical_version": {
    "accession": "Q9KZP3",
    "database": "Swiss-Prot",
    "entryVersion": 118,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CRLS1_STRCO",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KZP3.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9KZP3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:27.611577+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "19159a513ac84423a492087d8961c46891339eef5cec5a9d995ec98e1cfe717c",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KZP3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KZP3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":120,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2000-10-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:27.611577+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "19159a513ac84423a492087d8961c46891339eef5cec5a9d995ec98e1cfe717c",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KZP3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KZP3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000001973\",\"source\":\"Proteomes\"}],\"lineage\":[\"Bacteria\",\"Bacillati\",\"Actinomycetota\",\"Actinomycetes\",\"Kitasatosporales\",\"Streptomycetaceae\",\"Streptomyces\",\"Streptomyces albidoflavus group\"],\"scientificName\":\"Streptomyces coelicolor (strain ATCC BAA-471 / A3(2) / M145)\",\"taxonId\":100226}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:27.611577+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "19159a513ac84423a492087d8961c46891339eef5cec5a9d995ec98e1cfe717c",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KZP3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KZP3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"19439403\",\"source\":\"PubMed\"}],\"value\":\"2.7.8.41\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Cardiolipin synthase (CMP-forming)\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"CLS\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:27.611577+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "19159a513ac84423a492087d8961c46891339eef5cec5a9d995ec98e1cfe717c",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KZP3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KZP3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":49},\"start\":{\"modifier\":\"EXACT\",\"value\":29}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-01T06:25:27.611577+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "19159a513ac84423a492087d8961c46891339eef5cec5a9d995ec98e1cfe717c",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KZP3.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KZP3.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":80},\"start\":{\"modifier\":\"EXACT\",\"value\":60}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-01T06:25:27.611577+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "19159a513ac84423a492087d8961c46891339eef5cec5a9d995ec98e1cfe717c",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KZP3.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KZP3.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":137},\"start\":{\"modifier\":\"EXACT\",\"value\":117}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-01T06:25:27.611577+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "19159a513ac84423a492087d8961c46891339eef5cec5a9d995ec98e1cfe717c",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KZP3.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KZP3.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":178},\"start\":{\"modifier\":\"EXACT\",\"value\":158}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-01T06:25:27.611577+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "19159a513ac84423a492087d8961c46891339eef5cec5a9d995ec98e1cfe717c",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KZP3.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KZP3.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":199},\"start\":{\"modifier\":\"EXACT\",\"value\":179}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-01T06:25:27.611577+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "19159a513ac84423a492087d8961c46891339eef5cec5a9d995ec98e1cfe717c",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KZP3.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KZP3.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Sandoval-Calderon M.\",\"Geiger O.\",\"Guan Z.\",\"Barona-Gomez F.\",\"Sohlenkamp C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"19439403\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m109.006072\"}],\"citationType\":\"journal article\",\"firstPage\":\"17383\",\"id\":\"19439403\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"17390\",\"publicationDate\":\"2009\",\"title\":\"A eukaryote-like cardiolipin synthase is present in Streptomyces coelicolor and in most actinobacteria.\",\"volume\":\"284\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:25:27.611577+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "19159a513ac84423a492087d8961c46891339eef5cec5a9d995ec98e1cfe717c",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KZP3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118)

```json
{
  "entry_version": 118,
  "evidence_id": "H1",
  "excerpt": "ID   CRLS1_STRCO             Reviewed;         215 AA.\nAC   Q9KZP3;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-OCT-2000, sequence version 1.\nDT   28-JAN-2026, entry version 118.\nDE   RecName: Full=Cardiolipin synthase (CMP-forming) {ECO:0000305};\nDE            Short=CLS {ECO:0000305};\nDE            EC=2.7.8.41 {ECO:0000305|PubMed:19439403};\nGN   Name=clsA {ECO:0000303|PubMed:22409773};\nGN   OrderedLocusNames=SCO1389 {ECO:0000312|EMBL:CAB88885.1};\nGN   ORFNames=SC1A8A.09c {ECO:0000312|EMBL:CAB88885.1};\nOS   Streptomyces coelicolor (strain ATCC BAA-471 / A3(2) / M145).\nOC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Kitasatosporales;\nOC   Streptomycetaceae; Streptomyces; Streptomyces albidoflavus group.\nOX   NCBI_TaxID=100226 {ECO:0000312|Proteomes:UP000001973};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:47.509754+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "40068827609c34109c814e2d2c856e36a3bec9b7c2775a90bbcc5f7a21726d79",
  "url": "https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118)

```json
{
  "entry_version": 118,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, COFACTOR, BIOPHYSICOCHEMICAL PROPERTIES, AND\nRP   SUBCELLULAR LOCATION.\nRX   PubMed=19439403; DOI=10.1074/jbc.m109.006072;\nRA   Sandoval-Calderon M., Geiger O., Guan Z., Barona-Gomez F., Sohlenkamp C.;\nRT   \"A eukaryote-like cardiolipin synthase is present in Streptomyces\nRT   coelicolor and in most actinobacteria.\";\nRL   J. Biol. Chem. 284:17383-17390(2009).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:47.509754+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 31-38",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "40068827609c34109c814e2d2c856e36a3bec9b7c2775a90bbcc5f7a21726d79",
  "url": "https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118)

```json
{
  "entry_version": 118,
  "evidence_id": "H3",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=22409773; DOI=10.1111/j.1365-2958.2012.08018.x;\nRA   Jyothikumar V., Klanbut K., Tiong J., Roxburgh J.S., Hunter I.S.,\nRA   Smith T.K., Herron P.R.;\nRT   \"Cardiolipin synthase is required for Streptomyces coelicolor\nRT   morphogenesis.\";\nRL   Mol. Microbiol. 84:181-197(2012).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:47.509754+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 39-46",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "40068827609c34109c814e2d2c856e36a3bec9b7c2775a90bbcc5f7a21726d79",
  "url": "https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118)

```json
{
  "entry_version": 118,
  "evidence_id": "H4",
  "excerpt": "FT   TRANSMEM        29..49\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:47.509754+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 118-120",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "40068827609c34109c814e2d2c856e36a3bec9b7c2775a90bbcc5f7a21726d79",
  "url": "https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118)

```json
{
  "entry_version": 118,
  "evidence_id": "H5",
  "excerpt": "FT   TRANSMEM        60..80\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:47.509754+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 121-123",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "40068827609c34109c814e2d2c856e36a3bec9b7c2775a90bbcc5f7a21726d79",
  "url": "https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118)

```json
{
  "entry_version": 118,
  "evidence_id": "H6",
  "excerpt": "FT   TRANSMEM        117..137\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:47.509754+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 124-126",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "40068827609c34109c814e2d2c856e36a3bec9b7c2775a90bbcc5f7a21726d79",
  "url": "https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118)

```json
{
  "entry_version": 118,
  "evidence_id": "H7",
  "excerpt": "FT   TRANSMEM        158..178\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:47.509754+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 127-129",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "40068827609c34109c814e2d2c856e36a3bec9b7c2775a90bbcc5f7a21726d79",
  "url": "https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118)

```json
{
  "entry_version": 118,
  "evidence_id": "H8",
  "excerpt": "FT   TRANSMEM        179..199\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:47.509754+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 130-132",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "40068827609c34109c814e2d2c856e36a3bec9b7c2775a90bbcc5f7a21726d79",
  "url": "https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 122. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
