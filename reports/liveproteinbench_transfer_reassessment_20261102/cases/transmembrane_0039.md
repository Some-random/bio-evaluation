# transmembrane_0039

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0039.txt)

**Task:** `transmembrane`  
**Expected answer:** **D** — 28..48; 59..79; 106..126

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MDFYRILVICIHVYTRLVFAPLKKDLKLLRLISLCIPIIRPFSFLIYPPPKSFSPLNSILPSILPIIPFAISSSLLFSYTFHVFYRFLFQPLLSVPYANSKQTNCLLVASFVYLPYRSPLPVVIEIMVQRYL

[Multiple Choices]
A. 28..48; 59..79
B. 1..21
C. 28..48; 63..81; 106..126
D. 28..48; 59..79; 106..126
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

> The sequence-matched UniProt record annotates transmembrane regions at 28–48, 59–79, and 106–126, matching D. These are computational annotations (ECO:0000255), not evidence of experimental validation.

Citations as saved: [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Transferable knowledge that membrane-spanning helices are usually long, hydrophobic stretches supports identifying the three candidate regions around 28–48, 59–81, and 106–126. In particular, the hydrophobic C-terminal stretch distinguishes choices with a third span (C or D) from A and B. D is a reasonable sequence-based choice because its second interval includes the hydrophobic residues at 59–60 and ends before the more polar continuation; however, the exact boundary is uncertain.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence supplies a credible hydropathy-based inference without needing the target's annotation. The evidence does not, however, make the close boundary choice between C and D certain.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> Both intervals 59–79 and 63–81 cover a plausible hydrophobic membrane-spanning segment, and the sequence alone does not establish its exact endpoints. Both choices also include the plausible 106–126 span.


### Important caveats

- The reviewer evidence matches the supplied sequence, but the author's exact source snapshot is unknown.
- The cited transmembrane annotations are computational rather than experimental.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Transferable knowledge that membrane-spanning helices are usually long, hydrophobic stretches supports identifying the three candidate regions around 28–48, 59–81, and 106–126. In particular, the hydrophobic C-terminal stretch distinguishes choices with a third span (C or D) from A and B. D is a reasonable sequence-based choice because its second interval includes the hydrophobic residues at 59–60 and ends before the more polar continuation; however, the exact boundary is uncertain.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence supplies a credible hydropathy-based inference without needing the target's annotation. The evidence does not, however, make the close boundary choice between C and D certain."
  },
  "case_id": "transmembrane_0039",
  "expected_answer_check": {
    "evidence_ids": [
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates transmembrane regions at 28–48, 59–79, and 106–126, matching D. These are computational annotations (ECO:0000255), not evidence of experimental validation."
  },
  "important_caveats": [
    "The reviewer evidence matches the supplied sequence, but the author's exact source snapshot is unknown.",
    "The cited transmembrane annotations are computational rather than experimental."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "Both intervals 59–79 and 63–81 cover a plausible hydrophobic membrane-spanning segment, and the sequence alone does not establish its exact endpoints. Both choices also include the plausible 106–126 span."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0039",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates transmembrane regions at 28–48, 59–79, and 106–126, matching D. These are computational annotations (ECO:0000255), not evidence of experimental validation.",
    "evidence_ids": ["H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Transferable knowledge that membrane-spanning helices are usually long, hydrophobic stretches supports identifying the three candidate regions around 28–48, 59–81, and 106–126. In particular, the hydrophobic C-terminal stretch distinguishes choices with a third span (C or D) from A and B. D is a reasonable sequence-based choice because its second interval includes the hydrophobic residues at 59–60 and ends before the more polar continuation; however, the exact boundary is uncertain.",
    "missing_item_specific_fact": "",
    "reason": "The sequence supplies a credible hydropathy-based inference without needing the target's annotation. The evidence does not, however, make the close boundary choice between C and D certain."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "Both intervals 59–79 and 63–81 cover a plausible hydrophobic membrane-spanning segment, and the sequence alone does not establish its exact endpoints. Both choices also include the plausible 106–126 span."
  },
  "important_caveats": [
    "The reviewer evidence matches the supplied sequence, but the author's exact source snapshot is unknown.",
    "The cited transmembrane annotations are computational rather than experimental."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry for this sequence (A0AAN2H888, Schizosaccharomyces pombe protein SPCC1840.13) annotates exactly three transmembrane helical regions at 28-48, 59-79, and 106-126, matching option D precisely. The evidence code ECO:0000255 indicates computational prediction (not experimental), but the annotation directly supports the expected answer.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model can perform hydrophobicity analysis on the 132-residue sequence. Three regions (28-48, 59-79, 106-126) show elevated hydrophobicity (average Kyte-Doolittle ~+1.1 to +1.4) compared to the N-terminal region 1-21 (which contains D, R, H, T — charged/polar residues that disqualify it as TM, eliminating B). The spacing pattern (TM-loop-TM-loop-TM) with loops of ~11 and ~27 residues is consistent with a 3-TM small membrane protein. All three candidate regions have comparable moderate hydrophobicity, making the identification of three stretches (rather than two) a defensible inference from the sequence pattern. The distinction between C (63-81) and D (59-79) for the second TM is minor (4-residue boundary shift) and both are hydrophobically similar, but 59-79 captures the full hydrophobic stretch starting at I59. The key discriminator between A and D is recognizing the third hydrophobic stretch at 106-126, which has comparable hydrophobicity to the other two regions despite containing R and E.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The hydrophobicity profile of the sequence provides a transferable basis for identifying three regions of elevated hydrophobicity with appropriate TM-like spacing. While region 106-126 is borderline (contains R117 and E125), its overall hydrophobicity is comparable to the other two regions, and the three-stretch pattern in a 132-AA protein is recognizable from general TM prediction principles learned from other membrane proteins.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> Region 106-126 (LLVASFVYLPYRSPLPVVIEI) contains a charged arginine at position 117 and a glutamate at position 125, plus three prolines. A model applying strict TM criteria (no charged residues in the core, few prolines) might reasonably exclude this region and select A (only 2 TM regions). However, its overall hydrophobicity is comparable to the other two annotated regions, making D also defensible. The boundary difference between C and D (59-79 vs 63-81) is minor and both are hydrophobically plausible.


### Important caveats

- All three TM annotations carry evidence code ECO:0000255 (computational analysis), not experimental data. The boundaries reflect a specific prediction algorithm's output.
- The protein is annotated as 'Uncharacterized' with no known function, so biological context cannot independently validate the TM topology.
- The third TM region (106-126) is borderline by standard hydrophobicity criteria due to internal charged residues; its inclusion depends on the specific prediction threshold used.
- The distinction between options C and D involves only a 4-residue boundary shift in the second TM region, which is within the typical uncertainty of computational TM predictions.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can perform hydrophobicity analysis on the 132-residue sequence. Three regions (28-48, 59-79, 106-126) show elevated hydrophobicity (average Kyte-Doolittle ~+1.1 to +1.4) compared to the N-terminal region 1-21 (which contains D, R, H, T — charged/polar residues that disqualify it as TM, eliminating B). The spacing pattern (TM-loop-TM-loop-TM) with loops of ~11 and ~27 residues is consistent with a 3-TM small membrane protein. All three candidate regions have comparable moderate hydrophobicity, making the identification of three stretches (rather than two) a defensible inference from the sequence pattern. The distinction between C (63-81) and D (59-79) for the second TM is minor (4-residue boundary shift) and both are hydrophobically similar, but 59-79 captures the full hydrophobic stretch starting at I59. The key discriminator between A and D is recognizing the third hydrophobic stretch at 106-126, which has comparable hydrophobicity to the other two regions despite containing R and E.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The hydrophobicity profile of the sequence provides a transferable basis for identifying three regions of elevated hydrophobicity with appropriate TM-like spacing. While region 106-126 is borderline (contains R117 and E125), its overall hydrophobicity is comparable to the other two regions, and the three-stretch pattern in a 132-AA protein is recognizable from general TM prediction principles learned from other membrane proteins."
  },
  "case_id": "transmembrane_0039",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry for this sequence (A0AAN2H888, Schizosaccharomyces pombe protein SPCC1840.13) annotates exactly three transmembrane helical regions at 28-48, 59-79, and 106-126, matching option D precisely. The evidence code ECO:0000255 indicates computational prediction (not experimental), but the annotation directly supports the expected answer."
  },
  "important_caveats": [
    "All three TM annotations carry evidence code ECO:0000255 (computational analysis), not experimental data. The boundaries reflect a specific prediction algorithm's output.",
    "The protein is annotated as 'Uncharacterized' with no known function, so biological context cannot independently validate the TM topology.",
    "The third TM region (106-126) is borderline by standard hydrophobicity criteria due to internal charged residues; its inclusion depends on the specific prediction threshold used.",
    "The distinction between options C and D involves only a 4-residue boundary shift in the second TM region, which is within the typical uncertainty of computational TM predictions."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "Region 106-126 (LLVASFVYLPYRSPLPVVIEI) contains a charged arginine at position 117 and a glutamate at position 125, plus three prolines. A model applying strict TM criteria (no charged residues in the core, few prolines) might reasonably exclude this region and select A (only 2 TM regions). However, its overall hydrophobicity is comparable to the other two annotated regions, making D also defensible. The boundary difference between C and D (59-79 vs 63-81) is minor and both are hydrophobically plausible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0039",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry for this sequence (A0AAN2H888, Schizosaccharomyces pombe protein SPCC1840.13) annotates exactly three transmembrane helical regions at 28-48, 59-79, and 106-126, matching option D precisely. The evidence code ECO:0000255 indicates computational prediction (not experimental), but the annotation directly supports the expected answer.",
    "evidence_ids": ["C5", "C6", "C7", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model can perform hydrophobicity analysis on the 132-residue sequence. Three regions (28-48, 59-79, 106-126) show elevated hydrophobicity (average Kyte-Doolittle ~+1.1 to +1.4) compared to the N-terminal region 1-21 (which contains D, R, H, T — charged/polar residues that disqualify it as TM, eliminating B). The spacing pattern (TM-loop-TM-loop-TM) with loops of ~11 and ~27 residues is consistent with a 3-TM small membrane protein. All three candidate regions have comparable moderate hydrophobicity, making the identification of three stretches (rather than two) a defensible inference from the sequence pattern. The distinction between C (63-81) and D (59-79) for the second TM is minor (4-residue boundary shift) and both are hydrophobically similar, but 59-79 captures the full hydrophobic stretch starting at I59. The key discriminator between A and D is recognizing the third hydrophobic stretch at 106-126, which has comparable hydrophobicity to the other two regions despite containing R and E.",
    "missing_item_specific_fact": "",
    "reason": "The hydrophobicity profile of the sequence provides a transferable basis for identifying three regions of elevated hydrophobicity with appropriate TM-like spacing. While region 106-126 is borderline (contains R117 and E125), its overall hydrophobicity is comparable to the other two regions, and the three-stretch pattern in a 132-AA protein is recognizable from general TM prediction principles learned from other membrane proteins."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "Region 106-126 (LLVASFVYLPYRSPLPVVIEI) contains a charged arginine at position 117 and a glutamate at position 125, plus three prolines. A model applying strict TM criteria (no charged residues in the core, few prolines) might reasonably exclude this region and select A (only 2 TM regions). However, its overall hydrophobicity is comparable to the other two annotated regions, making D also defensible. The boundary difference between C and D (59-79 vs 63-81) is minor and both are hydrophobically plausible."
  },
  "important_caveats": [
    "All three TM annotations carry evidence code ECO:0000255 (computational analysis), not experimental data. The boundaries reflect a specific prediction algorithm's output.",
    "The protein is annotated as 'Uncharacterized' with no known function, so biological context cannot independently validate the TM topology.",
    "The third TM region (106-126) is borderline by standard hydrophobicity criteria due to internal charged residues; its inclusion depends on the specific prediction threshold used.",
    "The distinction between options C and D involves only a 4-residue boundary shift in the second TM region, which is within the typical uncertainty of computational TM predictions."
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
  "benchmark_sequence_length": 132,
  "benchmark_sequence_sha256": "519f14e72ae9755d32e43cc6ea1077031f23f1105fff5c8446d2e5156527f08f",
  "current_entry_audit": {
    "entryVersion": 6,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2024-10-02",
    "sequenceVersion": 1
  },
  "current_record_sha256": "dfe5241448e321f0663c9cfb8b4bae6fb06ac8d1923749d24757cdf8e7c7462b",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 132,
  "current_source_sequence_sha256": "519f14e72ae9755d32e43cc6ea1077031f23f1105fff5c8446d2e5156527f08f",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 5,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0AAN2H888",
  "selected_historical_entry_version": 5,
  "selected_historical_record_sha256": "6b6f26f79f92127cfcc4099a0210bb1df7b1178d8b385d3a6ee22f9c5b19080e",
  "selected_historical_source_sequence_length": 132,
  "selected_historical_source_sequence_sha256": "519f14e72ae9755d32e43cc6ea1077031f23f1105fff5c8446d2e5156527f08f",
  "selected_historical_version": {
    "accession": "A0AAN2H888",
    "database": "Swiss-Prot",
    "entryVersion": 5,
    "firstRelease": "2025_03/2025_03",
    "firstReleaseDate": "18-Jun-2025",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "YQJD_SCHPO",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAN2H888.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0AAN2H888\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:26:26.578336+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dfe5241448e321f0663c9cfb8b4bae6fb06ac8d1923749d24757cdf8e7c7462b",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAN2H888.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAN2H888.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":6,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2024-10-02\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:26:26.578336+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dfe5241448e321f0663c9cfb8b4bae6fb06ac8d1923749d24757cdf8e7c7462b",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAN2H888.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAN2H888.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Fission yeast\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Taphrinomycotina\",\"Schizosaccharomycetes\",\"Schizosaccharomycetales\",\"Schizosaccharomycetaceae\",\"Schizosaccharomyces\"],\"scientificName\":\"Schizosaccharomyces pombe (strain 972 / ATCC 24843)\",\"taxonId\":284812}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:26:26.578336+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dfe5241448e321f0663c9cfb8b4bae6fb06ac8d1923749d24757cdf8e7c7462b",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAN2H888.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAN2H888.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Uncharacterized protein SPCC1840.13\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:26:26.578336+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dfe5241448e321f0663c9cfb8b4bae6fb06ac8d1923749d24757cdf8e7c7462b",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAN2H888.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAN2H888.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":48},\"start\":{\"modifier\":\"EXACT\",\"value\":28}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:26:26.578336+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dfe5241448e321f0663c9cfb8b4bae6fb06ac8d1923749d24757cdf8e7c7462b",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAN2H888.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAN2H888.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":79},\"start\":{\"modifier\":\"EXACT\",\"value\":59}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:26:26.578336+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dfe5241448e321f0663c9cfb8b4bae6fb06ac8d1923749d24757cdf8e7c7462b",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAN2H888.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAN2H888.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":126},\"start\":{\"modifier\":\"EXACT\",\"value\":106}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:26:26.578336+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dfe5241448e321f0663c9cfb8b4bae6fb06ac8d1923749d24757cdf8e7c7462b",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAN2H888.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAN2H888?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H1",
  "excerpt": "ID   YQJD_SCHPO              Reviewed;         132 AA.\nAC   A0AAN2H888;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   02-OCT-2024, sequence version 1.\nDT   18-JUN-2025, entry version 5.\nDE   RecName: Full=Uncharacterized protein SPCC1840.13 {ECO:0000305};\nGN   ORFNames=SPCC1840.13 {ECO:0000312|PomBase:SPCC1840.13};\nOS   Schizosaccharomyces pombe (strain 972 / ATCC 24843) (Fission yeast).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Taphrinomycotina;\nOC   Schizosaccharomycetes; Schizosaccharomycetales; Schizosaccharomycetaceae;\nOC   Schizosaccharomyces.\nOX   NCBI_TaxID=284812;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:32.614740+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6b6f26f79f92127cfcc4099a0210bb1df7b1178d8b385d3a6ee22f9c5b19080e",
  "url": "https://rest.uniprot.org/unisave/A0AAN2H888?format=txt&versions=5"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAN2H888?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H2",
  "excerpt": "FT   TRANSMEM        28..48\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:32.614740+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 65-67",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6b6f26f79f92127cfcc4099a0210bb1df7b1178d8b385d3a6ee22f9c5b19080e",
  "url": "https://rest.uniprot.org/unisave/A0AAN2H888?format=txt&versions=5"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAN2H888?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H3",
  "excerpt": "FT   TRANSMEM        59..79\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:32.614740+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 68-70",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6b6f26f79f92127cfcc4099a0210bb1df7b1178d8b385d3a6ee22f9c5b19080e",
  "url": "https://rest.uniprot.org/unisave/A0AAN2H888?format=txt&versions=5"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAN2H888?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H4",
  "excerpt": "FT   TRANSMEM        106..126\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:32.614740+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 71-73",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6b6f26f79f92127cfcc4099a0210bb1df7b1178d8b385d3a6ee22f9c5b19080e",
  "url": "https://rest.uniprot.org/unisave/A0AAN2H888?format=txt&versions=5"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 39. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
