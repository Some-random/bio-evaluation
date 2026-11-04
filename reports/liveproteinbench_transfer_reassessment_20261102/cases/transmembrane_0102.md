# transmembrane_0102

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0102.txt)

**Task:** `transmembrane`  
**Expected answer:** **D** — 27..47; 59..81; 96..116; 138..158; 204..224; 246..266; 270..290

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MVNFTHVSEFVLLGFQGGPGMQAMLFLIFLILYGIAVVGNLGMIVIIWVDAHLHTPMYAFLQSLSLLDICYSSTIAPRALANSMQEDHTISFGGCAAQFFFLSLFGITEAFLLAAMAYDRFIAICNPLLYSVSMSHQVCVLLISGSYLWGVVNAIAQTTMTFRLPFCGSNEINDFFCDVPPLLSLSCSDTFINQLVLLGLCGSIIVSTFLIVLVSYIYIISTILRIPTMQGCQKAFSTCASHLTGVCLFFGTVFFMYAQPSAIFFMEQSKIVSIFYTMVIPMLNPLIYSLRNKEVKQALRRSMQKLSL

[Multiple Choices]
A. 27..47; 96..116; 138..158; 204..224; 246..266; 270..290
B. 27..47; 59..81; 96..116; 138..158; 204..224; 246..266; 275..292
C. 35..55
D. 27..47; 59..81; 96..116; 138..158; 204..224; 246..266; 270..290
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

> The sequence-matched UniProt annotations identify all seven transmembrane helices at the coordinates in D. These annotations carry ECO:0000255, indicating computational evidence, rather than establishing experimental confirmation.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has the characteristic pattern of a seven-pass, helix-rich membrane protein: repeated roughly 20-residue hydrophobic stretches separated by loops. That transferable pattern favors D's complete set over C's single segment and A's omission of the strong hydrophobic stretch at 59..81. The final hydrophobic stretch is followed by a more polar, charged tail, favoring D's 270..290 interval over B's shifted interval.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The alternatives can be meaningfully distinguished from sequence hydrophobicity and general knowledge of seven-transmembrane proteins; the exact database annotation is not necessary to make that inference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although B contains most of the final hydrophobic segment, its interval starts well inside that stretch and extends beyond it; the sequence pattern favors D's boundaries.


### Important caveats

- The supplied source supports D with computational transmembrane annotations, not direct experimental evidence.
- Reviewer-only source identity and annotations were not original model inputs and are not used as the basis for the transferability judgment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has the characteristic pattern of a seven-pass, helix-rich membrane protein: repeated roughly 20-residue hydrophobic stretches separated by loops. That transferable pattern favors D's complete set over C's single segment and A's omission of the strong hydrophobic stretch at 59..81. The final hydrophobic stretch is followed by a more polar, charged tail, favoring D's 270..290 interval over B's shifted interval.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The alternatives can be meaningfully distinguished from sequence hydrophobicity and general knowledge of seven-transmembrane proteins; the exact database annotation is not necessary to make that inference."
  },
  "case_id": "transmembrane_0102",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C8",
      "C10",
      "C12",
      "C14",
      "C16",
      "C18"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotations identify all seven transmembrane helices at the coordinates in D. These annotations carry ECO:0000255, indicating computational evidence, rather than establishing experimental confirmation."
  },
  "important_caveats": [
    "The supplied source supports D with computational transmembrane annotations, not direct experimental evidence.",
    "Reviewer-only source identity and annotations were not original model inputs and are not used as the basis for the transferability judgment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although B contains most of the final hydrophobic segment, its interval starts well inside that stretch and extends beyond it; the sequence pattern favors D's boundaries."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0102",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotations identify all seven transmembrane helices at the coordinates in D. These annotations carry ECO:0000255, indicating computational evidence, rather than establishing experimental confirmation.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has the characteristic pattern of a seven-pass, helix-rich membrane protein: repeated roughly 20-residue hydrophobic stretches separated by loops. That transferable pattern favors D's complete set over C's single segment and A's omission of the strong hydrophobic stretch at 59..81. The final hydrophobic stretch is followed by a more polar, charged tail, favoring D's 270..290 interval over B's shifted interval.",
    "missing_item_specific_fact": "",
    "reason": "The alternatives can be meaningfully distinguished from sequence hydrophobicity and general knowledge of seven-transmembrane proteins; the exact database annotation is not necessary to make that inference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although B contains most of the final hydrophobic segment, its interval starts well inside that stretch and extends beyond it; the sequence pattern favors D's boundaries."
  },
  "important_caveats": [
    "The supplied source supports D with computational transmembrane annotations, not direct experimental evidence.",
    "Reviewer-only source identity and annotations were not original model inputs and are not used as the basis for the transferability judgment."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for Q6UXT6 (OR9H1, human olfactory receptor) lists exactly seven transmembrane helices at 27-47, 59-81, 96-116, 138-158, 204-224, 246-266, and 270-290, matching option D precisely. The evidence codes are ECO:0000255 (predicted by similarity/prorule), indicating computational annotation transferred from GPCR family knowledge rather than experimental determination, but the coordinates are consistent across both the current entry and the historical archived version.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [H3](#evidence-h3), [H5](#evidence-h5), [H7](#evidence-h7), [H9](#evidence-h9), [H11](#evidence-h11), [H13](#evidence-h13), [H15](#evidence-h15).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is ~308 aa with multiple hydrophobic stretches, consistent with the 7-transmembrane GPCR superfamily (olfactory receptors). Recognizing the GPCR fold (7TM topology) eliminates option C (single TM) and option A (only 6 TMs, missing the TM2 region at ~59-81). Distinguishing D from B relies on two transferable GPCR structural principles: (1) The NPxxY motif (N286-P287-L288-I289-Y290) is a highly conserved GPCR hallmark anchoring the C-terminal end of TM7 at the tyrosine, making TM7 ending at position 290 (as in D) far more consistent with GPCR topology than ending at 292 (as in B, which extends 2 residues past the conserved tyrosine). (2) TM helices spanning the ~30 Å hydrophobic core require approximately 19-22 residues; the 270-290 segment (21 residues) is a standard TM7 length, while 275-292 (18 residues) is at the short end and would not comfortably span the bilayer. These are general GPCR structural principles learned from hundreds of other GPCR structures, not specific to this protein.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can use GPCR family recognition (7TM topology from sequence length and hydrophobic pattern), the conserved NPxxY motif at the TM7 C-terminus, and the minimum helix length for membrane spanning to select D over A, B, and C without recalling the specific UniProt annotation for OR9H1.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option C is trivially wrong (single TM for a 7TM GPCR). Option A omits TM2, inconsistent with GPCR topology. Option B shifts TM7 boundaries in a way that conflicts with the NPxxY motif and minimum helix length. Option D is the only choice consistent with all GPCR structural constraints.


### Important caveats

- The UniProt TM annotations carry ECO:0000255 (predicted by similarity), meaning they are computational transfers from GPCR family models rather than experimental measurements. The boundaries are therefore model-dependent, though well-established for the GPCR family.
- The distinction between D and B (TM7: 270-290 vs 275-292) is subtle and relies on the NPxxY motif and helix-length heuristics; a purely hydrophobicity-window-based approach might produce slightly different boundaries, but the NPxxY anchor strongly favors D.
- The reviewer-only evidence confirms the sequence matches Q6UXT6 (OR9H1_HUMAN), but this identification was not available to the evaluated model; the reasoning relies on recognizing the GPCR fold from the sequence itself.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is ~308 aa with multiple hydrophobic stretches, consistent with the 7-transmembrane GPCR superfamily (olfactory receptors). Recognizing the GPCR fold (7TM topology) eliminates option C (single TM) and option A (only 6 TMs, missing the TM2 region at ~59-81). Distinguishing D from B relies on two transferable GPCR structural principles: (1) The NPxxY motif (N286-P287-L288-I289-Y290) is a highly conserved GPCR hallmark anchoring the C-terminal end of TM7 at the tyrosine, making TM7 ending at position 290 (as in D) far more consistent with GPCR topology than ending at 292 (as in B, which extends 2 residues past the conserved tyrosine). (2) TM helices spanning the ~30 Å hydrophobic core require approximately 19-22 residues; the 270-290 segment (21 residues) is a standard TM7 length, while 275-292 (18 residues) is at the short end and would not comfortably span the bilayer. These are general GPCR structural principles learned from hundreds of other GPCR structures, not specific to this protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use GPCR family recognition (7TM topology from sequence length and hydrophobic pattern), the conserved NPxxY motif at the TM7 C-terminus, and the minimum helix length for membrane spanning to select D over A, B, and C without recalling the specific UniProt annotation for OR9H1."
  },
  "case_id": "transmembrane_0102",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C8",
      "C10",
      "C12",
      "C14",
      "C16",
      "C18",
      "H3",
      "H5",
      "H7",
      "H9",
      "H11",
      "H13",
      "H15"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for Q6UXT6 (OR9H1, human olfactory receptor) lists exactly seven transmembrane helices at 27-47, 59-81, 96-116, 138-158, 204-224, 246-266, and 270-290, matching option D precisely. The evidence codes are ECO:0000255 (predicted by similarity/prorule), indicating computational annotation transferred from GPCR family knowledge rather than experimental determination, but the coordinates are consistent across both the current entry and the historical archived version."
  },
  "important_caveats": [
    "The UniProt TM annotations carry ECO:0000255 (predicted by similarity), meaning they are computational transfers from GPCR family models rather than experimental measurements. The boundaries are therefore model-dependent, though well-established for the GPCR family.",
    "The distinction between D and B (TM7: 270-290 vs 275-292) is subtle and relies on the NPxxY motif and helix-length heuristics; a purely hydrophobicity-window-based approach might produce slightly different boundaries, but the NPxxY anchor strongly favors D.",
    "The reviewer-only evidence confirms the sequence matches Q6UXT6 (OR9H1_HUMAN), but this identification was not available to the evaluated model; the reasoning relies on recognizing the GPCR fold from the sequence itself."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C is trivially wrong (single TM for a 7TM GPCR). Option A omits TM2, inconsistent with GPCR topology. Option B shifts TM7 boundaries in a way that conflicts with the NPxxY motif and minimum helix length. Option D is the only choice consistent with all GPCR structural constraints."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0102",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for Q6UXT6 (OR9H1, human olfactory receptor) lists exactly seven transmembrane helices at 27-47, 59-81, 96-116, 138-158, 204-224, 246-266, and 270-290, matching option D precisely. The evidence codes are ECO:0000255 (predicted by similarity/prorule), indicating computational annotation transferred from GPCR family knowledge rather than experimental determination, but the coordinates are consistent across both the current entry and the historical archived version.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "H3", "H5", "H7", "H9", "H11", "H13", "H15"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is ~308 aa with multiple hydrophobic stretches, consistent with the 7-transmembrane GPCR superfamily (olfactory receptors). Recognizing the GPCR fold (7TM topology) eliminates option C (single TM) and option A (only 6 TMs, missing the TM2 region at ~59-81). Distinguishing D from B relies on two transferable GPCR structural principles: (1) The NPxxY motif (N286-P287-L288-I289-Y290) is a highly conserved GPCR hallmark anchoring the C-terminal end of TM7 at the tyrosine, making TM7 ending at position 290 (as in D) far more consistent with GPCR topology than ending at 292 (as in B, which extends 2 residues past the conserved tyrosine). (2) TM helices spanning the ~30 Å hydrophobic core require approximately 19-22 residues; the 270-290 segment (21 residues) is a standard TM7 length, while 275-292 (18 residues) is at the short end and would not comfortably span the bilayer. These are general GPCR structural principles learned from hundreds of other GPCR structures, not specific to this protein.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use GPCR family recognition (7TM topology from sequence length and hydrophobic pattern), the conserved NPxxY motif at the TM7 C-terminus, and the minimum helix length for membrane spanning to select D over A, B, and C without recalling the specific UniProt annotation for OR9H1."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C is trivially wrong (single TM for a 7TM GPCR). Option A omits TM2, inconsistent with GPCR topology. Option B shifts TM7 boundaries in a way that conflicts with the NPxxY motif and minimum helix length. Option D is the only choice consistent with all GPCR structural constraints."
  },
  "important_caveats": [
    "The UniProt TM annotations carry ECO:0000255 (predicted by similarity), meaning they are computational transfers from GPCR family models rather than experimental measurements. The boundaries are therefore model-dependent, though well-established for the GPCR family.",
    "The distinction between D and B (TM7: 270-290 vs 275-292) is subtle and relies on the NPxxY motif and helix-length heuristics; a purely hydrophobicity-window-based approach might produce slightly different boundaries, but the NPxxY anchor strongly favors D.",
    "The reviewer-only evidence confirms the sequence matches Q6UXT6 (OR9H1_HUMAN), but this identification was not available to the evaluated model; the reasoning relies on recognizing the GPCR fold from the sequence itself."
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
  "benchmark_sequence_length": 308,
  "benchmark_sequence_sha256": "bd1ae21d4d6b2155ee292802de80ed9a0a9be76bd414045d979fdca2cb4a9e30",
  "current_entry_audit": {
    "entryVersion": 108,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2004-07-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "d761824ae03c221d019ed712f82a29f42f3f5f479f6233c26b23ed7827f111d1",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 308,
  "current_source_sequence_sha256": "bd1ae21d4d6b2155ee292802de80ed9a0a9be76bd414045d979fdca2cb4a9e30",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 106,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q6UXT6",
  "selected_historical_entry_version": 106,
  "selected_historical_record_sha256": "072cef681e411cc08becb56d888ebce42ad8a93eca1ca016afab23f858b5896a",
  "selected_historical_source_sequence_length": 308,
  "selected_historical_source_sequence_sha256": "bd1ae21d4d6b2155ee292802de80ed9a0a9be76bd414045d979fdca2cb4a9e30",
  "selected_historical_version": {
    "accession": "Q6UXT6",
    "database": "Swiss-Prot",
    "entryVersion": 106,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "OR9H1_HUMAN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6UXT6.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q6UXT6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:31:45.136978+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d761824ae03c221d019ed712f82a29f42f3f5f479f6233c26b23ed7827f111d1",
  "url": "https://rest.uniprot.org/uniprotkb/Q6UXT6.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6UXT6.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":108,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2004-07-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:31:45.136978+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d761824ae03c221d019ed712f82a29f42f3f5f479f6233c26b23ed7827f111d1",
  "url": "https://rest.uniprot.org/uniprotkb/Q6UXT6.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6UXT6.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Human\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Euteleostomi\",\"Mammalia\",\"Eutheria\",\"Euarchontoglires\",\"Primates\",\"Haplorrhini\",\"Catarrhini\",\"Hominidae\",\"Homo\"],\"scientificName\":\"Homo sapiens\",\"taxonId\":9606}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:31:45.136978+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d761824ae03c221d019ed712f82a29f42f3f5f479f6233c26b23ed7827f111d1",
  "url": "https://rest.uniprot.org/uniprotkb/Q6UXT6.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6UXT6.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"value\":\"Olfactory receptor family 9 subfamily H member 1\"}}],\"recommendedName\":{\"fullName\":{\"value\":\"Olfactory receptor OR9H1\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:31:45.136978+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d761824ae03c221d019ed712f82a29f42f3f5f479f6233c26b23ed7827f111d1",
  "url": "https://rest.uniprot.org/uniprotkb/Q6UXT6.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6UXT6.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":26},\"start\":{\"modifier\":\"EXACT\",\"value\":1}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:31:45.136978+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d761824ae03c221d019ed712f82a29f42f3f5f479f6233c26b23ed7827f111d1",
  "url": "https://rest.uniprot.org/uniprotkb/Q6UXT6.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6UXT6.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical; Name=1\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":47},\"start\":{\"modifier\":\"EXACT\",\"value\":27}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:31:45.136978+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d761824ae03c221d019ed712f82a29f42f3f5f479f6233c26b23ed7827f111d1",
  "url": "https://rest.uniprot.org/uniprotkb/Q6UXT6.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6UXT6.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":58},\"start\":{\"modifier\":\"EXACT\",\"value\":48}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:31:45.136978+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d761824ae03c221d019ed712f82a29f42f3f5f479f6233c26b23ed7827f111d1",
  "url": "https://rest.uniprot.org/uniprotkb/Q6UXT6.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6UXT6.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Helical; Name=2\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":81},\"start\":{\"modifier\":\"EXACT\",\"value\":59}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:31:45.136978+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d761824ae03c221d019ed712f82a29f42f3f5f479f6233c26b23ed7827f111d1",
  "url": "https://rest.uniprot.org/uniprotkb/Q6UXT6.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6UXT6.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":95},\"start\":{\"modifier\":\"EXACT\",\"value\":82}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:31:45.136978+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d761824ae03c221d019ed712f82a29f42f3f5f479f6233c26b23ed7827f111d1",
  "url": "https://rest.uniprot.org/uniprotkb/Q6UXT6.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6UXT6.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"Helical; Name=3\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":116},\"start\":{\"modifier\":\"EXACT\",\"value\":96}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:31:45.136978+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d761824ae03c221d019ed712f82a29f42f3f5f479f6233c26b23ed7827f111d1",
  "url": "https://rest.uniprot.org/uniprotkb/Q6UXT6.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6UXT6.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":137},\"start\":{\"modifier\":\"EXACT\",\"value\":117}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:31:45.136978+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d761824ae03c221d019ed712f82a29f42f3f5f479f6233c26b23ed7827f111d1",
  "url": "https://rest.uniprot.org/uniprotkb/Q6UXT6.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6UXT6.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"Helical; Name=4\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":158},\"start\":{\"modifier\":\"EXACT\",\"value\":138}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:31:45.136978+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d761824ae03c221d019ed712f82a29f42f3f5f479f6233c26b23ed7827f111d1",
  "url": "https://rest.uniprot.org/uniprotkb/Q6UXT6.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6UXT6.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":203},\"start\":{\"modifier\":\"EXACT\",\"value\":159}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-02T04:31:45.136978+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d761824ae03c221d019ed712f82a29f42f3f5f479f6233c26b23ed7827f111d1",
  "url": "https://rest.uniprot.org/uniprotkb/Q6UXT6.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6UXT6.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"description\":\"Helical; Name=5\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":224},\"start\":{\"modifier\":\"EXACT\",\"value\":204}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-02T04:31:45.136978+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d761824ae03c221d019ed712f82a29f42f3f5f479f6233c26b23ed7827f111d1",
  "url": "https://rest.uniprot.org/uniprotkb/Q6UXT6.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6UXT6.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":245},\"start\":{\"modifier\":\"EXACT\",\"value\":225}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/11",
  "retrieved_utc": "2026-11-02T04:31:45.136978+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d761824ae03c221d019ed712f82a29f42f3f5f479f6233c26b23ed7827f111d1",
  "url": "https://rest.uniprot.org/uniprotkb/Q6UXT6.json"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6UXT6.json)

```json
{
  "evidence_id": "C16",
  "excerpt": "{\"description\":\"Helical; Name=6\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":266},\"start\":{\"modifier\":\"EXACT\",\"value\":246}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/12",
  "retrieved_utc": "2026-11-02T04:31:45.136978+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d761824ae03c221d019ed712f82a29f42f3f5f479f6233c26b23ed7827f111d1",
  "url": "https://rest.uniprot.org/uniprotkb/Q6UXT6.json"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6UXT6.json)

```json
{
  "evidence_id": "C17",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":269},\"start\":{\"modifier\":\"EXACT\",\"value\":267}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/13",
  "retrieved_utc": "2026-11-02T04:31:45.136978+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d761824ae03c221d019ed712f82a29f42f3f5f479f6233c26b23ed7827f111d1",
  "url": "https://rest.uniprot.org/uniprotkb/Q6UXT6.json"
}
```

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6UXT6.json)

```json
{
  "evidence_id": "C18",
  "excerpt": "{\"description\":\"Helical; Name=7\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":290},\"start\":{\"modifier\":\"EXACT\",\"value\":270}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/14",
  "retrieved_utc": "2026-11-02T04:31:45.136978+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d761824ae03c221d019ed712f82a29f42f3f5f479f6233c26b23ed7827f111d1",
  "url": "https://rest.uniprot.org/uniprotkb/Q6UXT6.json"
}
```

### Evidence C19

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6UXT6.json)

```json
{
  "evidence_id": "C19",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":308},\"start\":{\"modifier\":\"EXACT\",\"value\":291}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/15",
  "retrieved_utc": "2026-11-02T04:31:45.136978+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d761824ae03c221d019ed712f82a29f42f3f5f479f6233c26b23ed7827f111d1",
  "url": "https://rest.uniprot.org/uniprotkb/Q6UXT6.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6UXT6?format=txt&versions=106)

```json
{
  "entry_version": 106,
  "evidence_id": "H1",
  "excerpt": "ID   OR9H1_HUMAN             Reviewed;         308 AA.\nAC   Q6UXT6;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-JUL-2004, sequence version 1.\nDT   28-JAN-2026, entry version 106.\nDE   RecName: Full=Olfactory receptor OR9H1;\nDE   AltName: Full=Olfactory receptor family 9 subfamily H member 1;\nGN   Name=OR9H1 {ECO:0000312|HGNC:HGNC:15038};\nGN   Synonyms=OR9H1P {ECO:0000312|HGNC:HGNC:15038}; ORFNames=UNQ9373;\nOS   Homo sapiens (Human).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;\nOC   Eutheria; Euarchontoglires; Primates; Haplorrhini; Catarrhini; Hominidae;\nOC   Homo.\nOX   NCBI_TaxID=9606;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:47.614110+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "072cef681e411cc08becb56d888ebce42ad8a93eca1ca016afab23f858b5896a",
  "url": "https://rest.uniprot.org/unisave/Q6UXT6?format=txt&versions=106"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6UXT6?format=txt&versions=106)

```json
{
  "entry_version": 106,
  "evidence_id": "H2",
  "excerpt": "FT   TOPO_DOM        1..26\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:47.614110+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 118-120",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "072cef681e411cc08becb56d888ebce42ad8a93eca1ca016afab23f858b5896a",
  "url": "https://rest.uniprot.org/unisave/Q6UXT6?format=txt&versions=106"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6UXT6?format=txt&versions=106)

```json
{
  "entry_version": 106,
  "evidence_id": "H3",
  "excerpt": "FT   TRANSMEM        27..47\nFT                   /note=\"Helical; Name=1\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:47.614110+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 121-123",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "072cef681e411cc08becb56d888ebce42ad8a93eca1ca016afab23f858b5896a",
  "url": "https://rest.uniprot.org/unisave/Q6UXT6?format=txt&versions=106"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6UXT6?format=txt&versions=106)

```json
{
  "entry_version": 106,
  "evidence_id": "H4",
  "excerpt": "FT   TOPO_DOM        48..58\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:47.614110+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 124-126",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "072cef681e411cc08becb56d888ebce42ad8a93eca1ca016afab23f858b5896a",
  "url": "https://rest.uniprot.org/unisave/Q6UXT6?format=txt&versions=106"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6UXT6?format=txt&versions=106)

```json
{
  "entry_version": 106,
  "evidence_id": "H5",
  "excerpt": "FT   TRANSMEM        59..81\nFT                   /note=\"Helical; Name=2\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:47.614110+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 127-129",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "072cef681e411cc08becb56d888ebce42ad8a93eca1ca016afab23f858b5896a",
  "url": "https://rest.uniprot.org/unisave/Q6UXT6?format=txt&versions=106"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6UXT6?format=txt&versions=106)

```json
{
  "entry_version": 106,
  "evidence_id": "H6",
  "excerpt": "FT   TOPO_DOM        82..95\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:47.614110+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 130-132",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "072cef681e411cc08becb56d888ebce42ad8a93eca1ca016afab23f858b5896a",
  "url": "https://rest.uniprot.org/unisave/Q6UXT6?format=txt&versions=106"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6UXT6?format=txt&versions=106)

```json
{
  "entry_version": 106,
  "evidence_id": "H7",
  "excerpt": "FT   TRANSMEM        96..116\nFT                   /note=\"Helical; Name=3\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:47.614110+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 133-135",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "072cef681e411cc08becb56d888ebce42ad8a93eca1ca016afab23f858b5896a",
  "url": "https://rest.uniprot.org/unisave/Q6UXT6?format=txt&versions=106"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6UXT6?format=txt&versions=106)

```json
{
  "entry_version": 106,
  "evidence_id": "H8",
  "excerpt": "FT   TOPO_DOM        117..137\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:47.614110+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 136-138",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "072cef681e411cc08becb56d888ebce42ad8a93eca1ca016afab23f858b5896a",
  "url": "https://rest.uniprot.org/unisave/Q6UXT6?format=txt&versions=106"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6UXT6?format=txt&versions=106)

```json
{
  "entry_version": 106,
  "evidence_id": "H9",
  "excerpt": "FT   TRANSMEM        138..158\nFT                   /note=\"Helical; Name=4\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:47.614110+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 139-141",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "072cef681e411cc08becb56d888ebce42ad8a93eca1ca016afab23f858b5896a",
  "url": "https://rest.uniprot.org/unisave/Q6UXT6?format=txt&versions=106"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6UXT6?format=txt&versions=106)

```json
{
  "entry_version": 106,
  "evidence_id": "H10",
  "excerpt": "FT   TOPO_DOM        159..203\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:47.614110+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 142-144",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "072cef681e411cc08becb56d888ebce42ad8a93eca1ca016afab23f858b5896a",
  "url": "https://rest.uniprot.org/unisave/Q6UXT6?format=txt&versions=106"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6UXT6?format=txt&versions=106)

```json
{
  "entry_version": 106,
  "evidence_id": "H11",
  "excerpt": "FT   TRANSMEM        204..224\nFT                   /note=\"Helical; Name=5\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:47.614110+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 145-147",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "072cef681e411cc08becb56d888ebce42ad8a93eca1ca016afab23f858b5896a",
  "url": "https://rest.uniprot.org/unisave/Q6UXT6?format=txt&versions=106"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6UXT6?format=txt&versions=106)

```json
{
  "entry_version": 106,
  "evidence_id": "H12",
  "excerpt": "FT   TOPO_DOM        225..245\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:47.614110+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 148-150",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "072cef681e411cc08becb56d888ebce42ad8a93eca1ca016afab23f858b5896a",
  "url": "https://rest.uniprot.org/unisave/Q6UXT6?format=txt&versions=106"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6UXT6?format=txt&versions=106)

```json
{
  "entry_version": 106,
  "evidence_id": "H13",
  "excerpt": "FT   TRANSMEM        246..266\nFT                   /note=\"Helical; Name=6\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:47.614110+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 151-153",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "072cef681e411cc08becb56d888ebce42ad8a93eca1ca016afab23f858b5896a",
  "url": "https://rest.uniprot.org/unisave/Q6UXT6?format=txt&versions=106"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6UXT6?format=txt&versions=106)

```json
{
  "entry_version": 106,
  "evidence_id": "H14",
  "excerpt": "FT   TOPO_DOM        267..269\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:47.614110+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 154-156",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "072cef681e411cc08becb56d888ebce42ad8a93eca1ca016afab23f858b5896a",
  "url": "https://rest.uniprot.org/unisave/Q6UXT6?format=txt&versions=106"
}
```

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6UXT6?format=txt&versions=106)

```json
{
  "entry_version": 106,
  "evidence_id": "H15",
  "excerpt": "FT   TRANSMEM        270..290\nFT                   /note=\"Helical; Name=7\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:47.614110+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 157-159",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "072cef681e411cc08becb56d888ebce42ad8a93eca1ca016afab23f858b5896a",
  "url": "https://rest.uniprot.org/unisave/Q6UXT6?format=txt&versions=106"
}
```

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6UXT6?format=txt&versions=106)

```json
{
  "entry_version": 106,
  "evidence_id": "H16",
  "excerpt": "FT   TOPO_DOM        291..308\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:47.614110+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 160-162",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "072cef681e411cc08becb56d888ebce42ad8a93eca1ca016afab23f858b5896a",
  "url": "https://rest.uniprot.org/unisave/Q6UXT6?format=txt&versions=106"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 102. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
