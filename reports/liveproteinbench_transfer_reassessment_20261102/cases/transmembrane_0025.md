# transmembrane_0025

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0025.txt)

**Task:** `transmembrane`  
**Expected answer:** **B** — 9..45; 50..80; 86..121; 130..156; 173..211; 216..251; 268..296

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSNFTPDACNVDSGLDSVLPPSLYALVFTLGLPANLLALWAAWLQVRKGRELGVYLLNLSLSDLLLICALPPWTDYYLRRDVWGYGPGACRLFGFVFYTNLYVGAAFLSCVSADRYLAVAHPLRFPGARPIRSAAAVSALIWMLELAANAPPLLGEAIHRDRYNHTFCYESYPLSGRGAALANVGRVLAGFLLPWGVMMLCYAGLLRALRGSASCEQRERRRVRRLALGLPCVALLCYGPYHALLLLRSLVFLVGGGSVDAGGGCALEERLFPAYHASLALATLNCLADPALYCLACPGARGEVAKVVGGVVAWAMGKERRAWGERGGNGRGCGEGEEVGMVELRGNGREFVV

[Multiple Choices]
A. 5..25
B. 9..45; 50..80; 86..121; 130..156; 173..211; 216..251; 268..296
C. 9..45; 50..80; 89..125; 130..156; 173..211; 216..251; 268..296
D. 9..45; 50..80; 86..121; 130..156; 173..211; 216..251
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

> The sequence-matched UniProt record annotates the seven transmembrane helices at the coordinates in choice B. The annotations cite experimental evidence (ECO:0000269) and the associated structural study, though the supplied excerpts do not independently validate that study's results.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is strongly characteristic of a seven-transmembrane GPCR: its hydrophobic stretches and alternating loops make the seven-helix choices much more credible than A or D. That family-level inference does not robustly distinguish B from C, which differ only in the boundaries assigned to the third helix.


**Missing item-specific fact**

> The exact boundary annotation for the third transmembrane helix in this protein is needed to choose between B and C.


**Reason**

> Transferable GPCR knowledge supports the overall topology, but the third-helix boundary shift is too small and ambiguous to select one interval confidently from sequence pattern alone. The exact annotated coordinates are a fact about this protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> B and C both describe the same apparent seven-helix topology and differ only by a few residues at the third helix's boundaries. Such close boundary choices are not clearly distinguished by the question's wording or by an unambiguous sequence feature.


### Important caveats

- The reviewer-only source record matches the supplied sequence; its identity and annotations were not part of the original model input.
- Transmembrane helix boundaries can be convention-dependent, so support for the recorded coordinates does not make the nearby alternative biologically impossible.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is strongly characteristic of a seven-transmembrane GPCR: its hydrophobic stretches and alternating loops make the seven-helix choices much more credible than A or D. That family-level inference does not robustly distinguish B from C, which differ only in the boundaries assigned to the third helix.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact boundary annotation for the third transmembrane helix in this protein is needed to choose between B and C.",
    "reason": "Transferable GPCR knowledge supports the overall topology, but the third-helix boundary shift is too small and ambiguous to select one interval confidently from sequence pattern alone. The exact annotated coordinates are a fact about this protein."
  },
  "case_id": "transmembrane_0025",
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
    "reason": "The sequence-matched UniProt record annotates the seven transmembrane helices at the coordinates in choice B. The annotations cite experimental evidence (ECO:0000269) and the associated structural study, though the supplied excerpts do not independently validate that study's results."
  },
  "important_caveats": [
    "The reviewer-only source record matches the supplied sequence; its identity and annotations were not part of the original model input.",
    "Transmembrane helix boundaries can be convention-dependent, so support for the recorded coordinates does not make the nearby alternative biologically impossible."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "B and C both describe the same apparent seven-helix topology and differ only by a few residues at the third helix's boundaries. Such close boundary choices are not clearly distinguished by the question's wording or by an unambiguous sequence feature."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0025",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the seven transmembrane helices at the coordinates in choice B. The annotations cite experimental evidence (ECO:0000269) and the associated structural study, though the supplied excerpts do not independently validate that study's results.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is strongly characteristic of a seven-transmembrane GPCR: its hydrophobic stretches and alternating loops make the seven-helix choices much more credible than A or D. That family-level inference does not robustly distinguish B from C, which differ only in the boundaries assigned to the third helix.",
    "missing_item_specific_fact": "The exact boundary annotation for the third transmembrane helix in this protein is needed to choose between B and C.",
    "reason": "Transferable GPCR knowledge supports the overall topology, but the third-helix boundary shift is too small and ambiguous to select one interval confidently from sequence pattern alone. The exact annotated coordinates are a fact about this protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "B and C both describe the same apparent seven-helix topology and differ only by a few residues at the third helix's boundaries. Such close boundary choices are not clearly distinguished by the question's wording or by an unambiguous sequence feature."
  },
  "important_caveats": [
    "The reviewer-only source record matches the supplied sequence; its identity and annotations were not part of the original model input.",
    "Transmembrane helix boundaries can be convention-dependent, so support for the recorded coordinates does not make the nearby alternative biologically impossible."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A6I8PUB9 annotates exactly seven transmembrane helices at 9..45, 50..80, 86..121, 130..156, 173..211, 216..251, and 268..296, all with experimental evidence (ECO:0000269, cryo-EM structure from PubMed:39753131). This matches option B precisely.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is 353 residues with a pattern of seven long hydrophobic stretches separated by short polar/charged loops, consistent with a 7-TM GPCR. This eliminates A (single 21-residue segment) and D (only six TMs). The remaining distinction between B and C concerns TM3 boundaries (86..121 vs 89..125). In option C, TM3 would extend to residue 125, incorporating positions 122-125 (PLRF). Position 124 is arginine (R), a strongly charged residue that is thermodynamically unfavorable in the hydrophobic core of a transmembrane helix. In GPCRs, the cytoplasmic loop between TM3 and TM4 typically contains such charged residues (e.g., the conserved DRY motif region). Placing R within the TM helix contradicts the well-established principle that charged residues reside in aqueous loops. Additionally, the 5-residue extracellular loop (81-85: DVWGY) before TM3 is consistent with the short loops seen in GPCR crystal/cryo-EM structures, supporting a TM3 start near 86 rather than 89. The combination of 7-TM topology knowledge and the charged-residue-in-loop principle provides a credible transferable basis to select B over C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can apply GPCR 7-TM topology to eliminate A and D, then use the principle that charged residues (R at position 124) belong in cytoplasmic loops rather than TM helix interiors to reject C's extended TM3 boundary. The GPG segment at 86-88 is a short polar dip tolerable at a TM boundary in GPCR structures. These are transferable biophysical and structural principles learned from many GPCRs.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option A is clearly wrong (single short segment), D lacks the 7th TM, and C includes a charged arginine within TM3 which contradicts TM helix biophysics. B is the only option consistent with both 7-TM GPCR topology and hydrophobicity constraints.


### Important caveats

- The exact TM boundaries in the UniProt entry were determined by cryo-EM structure (experimental), so the precise residue-level boundaries (e.g., 86 vs 89 for TM3 start) may not be perfectly reproducible by hydropathy analysis alone.
- The GPG segment at positions 86-88 is a borderline case for TM inclusion; a model relying solely on hydrophobicity might exclude it, but the charged-residue argument for the C-terminal boundary (position 124) is more decisive.
- The reviewer-only evidence confirms the sequence matches the benchmark input exactly (SHA256 match), validating that the annotation applies to the supplied sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is 353 residues with a pattern of seven long hydrophobic stretches separated by short polar/charged loops, consistent with a 7-TM GPCR. This eliminates A (single 21-residue segment) and D (only six TMs). The remaining distinction between B and C concerns TM3 boundaries (86..121 vs 89..125). In option C, TM3 would extend to residue 125, incorporating positions 122-125 (PLRF). Position 124 is arginine (R), a strongly charged residue that is thermodynamically unfavorable in the hydrophobic core of a transmembrane helix. In GPCRs, the cytoplasmic loop between TM3 and TM4 typically contains such charged residues (e.g., the conserved DRY motif region). Placing R within the TM helix contradicts the well-established principle that charged residues reside in aqueous loops. Additionally, the 5-residue extracellular loop (81-85: DVWGY) before TM3 is consistent with the short loops seen in GPCR crystal/cryo-EM structures, supporting a TM3 start near 86 rather than 89. The combination of 7-TM topology knowledge and the charged-residue-in-loop principle provides a credible transferable basis to select B over C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can apply GPCR 7-TM topology to eliminate A and D, then use the principle that charged residues (R at position 124) belong in cytoplasmic loops rather than TM helix interiors to reject C's extended TM3 boundary. The GPG segment at 86-88 is a short polar dip tolerable at a TM boundary in GPCR structures. These are transferable biophysical and structural principles learned from many GPCRs."
  },
  "case_id": "transmembrane_0025",
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
    "reason": "The UniProt entry A0A6I8PUB9 annotates exactly seven transmembrane helices at 9..45, 50..80, 86..121, 130..156, 173..211, 216..251, and 268..296, all with experimental evidence (ECO:0000269, cryo-EM structure from PubMed:39753131). This matches option B precisely."
  },
  "important_caveats": [
    "The exact TM boundaries in the UniProt entry were determined by cryo-EM structure (experimental), so the precise residue-level boundaries (e.g., 86 vs 89 for TM3 start) may not be perfectly reproducible by hydropathy analysis alone.",
    "The GPG segment at positions 86-88 is a borderline case for TM inclusion; a model relying solely on hydrophobicity might exclude it, but the charged-residue argument for the C-terminal boundary (position 124) is more decisive.",
    "The reviewer-only evidence confirms the sequence matches the benchmark input exactly (SHA256 match), validating that the annotation applies to the supplied sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option A is clearly wrong (single short segment), D lacks the 7th TM, and C includes a charged arginine within TM3 which contradicts TM helix biophysics. B is the only option consistent with both 7-TM GPCR topology and hydrophobicity constraints."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0025",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A6I8PUB9 annotates exactly seven transmembrane helices at 9..45, 50..80, 86..121, 130..156, 173..211, 216..251, and 268..296, all with experimental evidence (ECO:0000269, cryo-EM structure from PubMed:39753131). This matches option B precisely.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is 353 residues with a pattern of seven long hydrophobic stretches separated by short polar/charged loops, consistent with a 7-TM GPCR. This eliminates A (single 21-residue segment) and D (only six TMs). The remaining distinction between B and C concerns TM3 boundaries (86..121 vs 89..125). In option C, TM3 would extend to residue 125, incorporating positions 122-125 (PLRF). Position 124 is arginine (R), a strongly charged residue that is thermodynamically unfavorable in the hydrophobic core of a transmembrane helix. In GPCRs, the cytoplasmic loop between TM3 and TM4 typically contains such charged residues (e.g., the conserved DRY motif region). Placing R within the TM helix contradicts the well-established principle that charged residues reside in aqueous loops. Additionally, the 5-residue extracellular loop (81-85: DVWGY) before TM3 is consistent with the short loops seen in GPCR crystal/cryo-EM structures, supporting a TM3 start near 86 rather than 89. The combination of 7-TM topology knowledge and the charged-residue-in-loop principle provides a credible transferable basis to select B over C.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can apply GPCR 7-TM topology to eliminate A and D, then use the principle that charged residues (R at position 124) belong in cytoplasmic loops rather than TM helix interiors to reject C's extended TM3 boundary. The GPG segment at 86-88 is a short polar dip tolerable at a TM boundary in GPCR structures. These are transferable biophysical and structural principles learned from many GPCRs."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option A is clearly wrong (single short segment), D lacks the 7th TM, and C includes a charged arginine within TM3 which contradicts TM helix biophysics. B is the only option consistent with both 7-TM GPCR topology and hydrophobicity constraints."
  },
  "important_caveats": [
    "The exact TM boundaries in the UniProt entry were determined by cryo-EM structure (experimental), so the precise residue-level boundaries (e.g., 86 vs 89 for TM3 start) may not be perfectly reproducible by hydropathy analysis alone.",
    "The GPG segment at positions 86-88 is a borderline case for TM inclusion; a model relying solely on hydrophobicity might exclude it, but the charged-residue argument for the C-terminal boundary (position 124) is more decisive.",
    "The reviewer-only evidence confirms the sequence matches the benchmark input exactly (SHA256 match), validating that the annotation applies to the supplied sequence."
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
  "benchmark_sequence_length": 353,
  "benchmark_sequence_sha256": "7093384a068f217cd38de58555a2ce625b886a7c15c3e1a032328261341f4f66",
  "current_entry_audit": {
    "entryVersion": 27,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2020-08-12",
    "sequenceVersion": 1
  },
  "current_record_sha256": "a744101e779b456c34c37646ab2aee926ca32698d73eef5421228a17149aa4e1",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 353,
  "current_source_sequence_sha256": "7093384a068f217cd38de58555a2ce625b886a7c15c3e1a032328261341f4f66",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 25,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A6I8PUB9",
  "selected_historical_entry_version": 25,
  "selected_historical_record_sha256": "57795ac8541e9349c417ffab8858e9955615bd1d0fd8bb5a206b1104334eba37",
  "selected_historical_source_sequence_length": 353,
  "selected_historical_source_sequence_sha256": "7093384a068f217cd38de58555a2ce625b886a7c15c3e1a032328261341f4f66",
  "selected_historical_version": {
    "accession": "A0A6I8PUB9",
    "database": "Swiss-Prot",
    "entryVersion": 25,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "GPR4_XENTR",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A6I8PUB9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:25:33.494326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a744101e779b456c34c37646ab2aee926ca32698d73eef5421228a17149aa4e1",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":27,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2020-08-12\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:25:33.494326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a744101e779b456c34c37646ab2aee926ca32698d73eef5421228a17149aa4e1",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Western clawed frog\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Euteleostomi\",\"Amphibia\",\"Batrachia\",\"Anura\",\"Pipoidea\",\"Pipidae\",\"Xenopodinae\",\"Xenopus\",\"Silurana\"],\"scientificName\":\"Xenopus tropicalis\",\"synonyms\":[\"Silurana tropicalis\"],\"taxonId\":8364}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:25:33.494326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a744101e779b456c34c37646ab2aee926ca32698d73eef5421228a17149aa4e1",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"value\":\"G protein-coupled receptor 4\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39753131\",\"source\":\"PubMed\"}],\"value\":\"XtGPR4\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:25:33.494326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a744101e779b456c34c37646ab2aee926ca32698d73eef5421228a17149aa4e1",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39753131\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":8},\"start\":{\"modifier\":\"EXACT\",\"value\":1}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:25:33.494326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a744101e779b456c34c37646ab2aee926ca32698d73eef5421228a17149aa4e1",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical; Name=1\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39753131\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":45},\"start\":{\"modifier\":\"EXACT\",\"value\":9}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:25:33.494326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a744101e779b456c34c37646ab2aee926ca32698d73eef5421228a17149aa4e1",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39753131\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":49},\"start\":{\"modifier\":\"EXACT\",\"value\":46}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:25:33.494326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a744101e779b456c34c37646ab2aee926ca32698d73eef5421228a17149aa4e1",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Helical; Name=2\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39753131\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":80},\"start\":{\"modifier\":\"EXACT\",\"value\":50}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:25:33.494326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a744101e779b456c34c37646ab2aee926ca32698d73eef5421228a17149aa4e1",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39753131\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":85},\"start\":{\"modifier\":\"EXACT\",\"value\":81}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:25:33.494326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a744101e779b456c34c37646ab2aee926ca32698d73eef5421228a17149aa4e1",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"Helical; Name=3\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39753131\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":121},\"start\":{\"modifier\":\"EXACT\",\"value\":86}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:25:33.494326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a744101e779b456c34c37646ab2aee926ca32698d73eef5421228a17149aa4e1",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39753131\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":129},\"start\":{\"modifier\":\"EXACT\",\"value\":122}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:25:33.494326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a744101e779b456c34c37646ab2aee926ca32698d73eef5421228a17149aa4e1",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"Helical; Name=4\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39753131\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":156},\"start\":{\"modifier\":\"EXACT\",\"value\":130}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:25:33.494326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a744101e779b456c34c37646ab2aee926ca32698d73eef5421228a17149aa4e1",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39753131\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":172},\"start\":{\"modifier\":\"EXACT\",\"value\":157}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-02T04:25:33.494326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a744101e779b456c34c37646ab2aee926ca32698d73eef5421228a17149aa4e1",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"description\":\"Helical; Name=5\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39753131\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":211},\"start\":{\"modifier\":\"EXACT\",\"value\":173}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-02T04:25:33.494326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a744101e779b456c34c37646ab2aee926ca32698d73eef5421228a17149aa4e1",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39753131\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":215},\"start\":{\"modifier\":\"EXACT\",\"value\":212}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/11",
  "retrieved_utc": "2026-11-02T04:25:33.494326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a744101e779b456c34c37646ab2aee926ca32698d73eef5421228a17149aa4e1",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json)

```json
{
  "evidence_id": "C16",
  "excerpt": "{\"description\":\"Helical; Name=6\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39753131\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":251},\"start\":{\"modifier\":\"EXACT\",\"value\":216}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/12",
  "retrieved_utc": "2026-11-02T04:25:33.494326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a744101e779b456c34c37646ab2aee926ca32698d73eef5421228a17149aa4e1",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json)

```json
{
  "evidence_id": "C17",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39753131\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":267},\"start\":{\"modifier\":\"EXACT\",\"value\":252}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/13",
  "retrieved_utc": "2026-11-02T04:25:33.494326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a744101e779b456c34c37646ab2aee926ca32698d73eef5421228a17149aa4e1",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json"
}
```

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json)

```json
{
  "evidence_id": "C18",
  "excerpt": "{\"description\":\"Helical; Name=7\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39753131\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":296},\"start\":{\"modifier\":\"EXACT\",\"value\":268}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/14",
  "retrieved_utc": "2026-11-02T04:25:33.494326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a744101e779b456c34c37646ab2aee926ca32698d73eef5421228a17149aa4e1",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json"
}
```

### Evidence C19

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json)

```json
{
  "evidence_id": "C19",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39753131\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":353},\"start\":{\"modifier\":\"EXACT\",\"value\":297}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/15",
  "retrieved_utc": "2026-11-02T04:25:33.494326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a744101e779b456c34c37646ab2aee926ca32698d73eef5421228a17149aa4e1",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json"
}
```

### Evidence C20

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json)

```json
{
  "evidence_id": "C20",
  "excerpt": "{\"citation\":{\"authors\":[\"Wen X.\",\"Shang P.\",\"Chen H.\",\"Guo L.\",\"Rong N.\",\"Jiang X.\",\"Li X.\",\"Liu J.\",\"Yang G.\",\"Zhang J.\",\"Zhu K.\",\"Meng Q.\",\"He X.\",\"Wang Z.\",\"Liu Z.\",\"Cheng H.\",\"Zheng Y.\",\"Zhang B.\",\"Pang J.\",\"Liu Z.\",\"Xiao P.\",\"Chen Y.\",\"Liu L.\",\"Luo F.\",\"Yu X.\",\"Yi F.\",\"Zhang P.\",\"Yang F.\",\"Deng C.\",\"Sun J.P.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39753131\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.cell.2024.12.001\"}],\"citationType\":\"journal article\",\"firstPage\":\"653\",\"id\":\"39753131\",\"journal\":\"Cell\",\"lastPage\":\"670\",\"publicationDate\":\"2025\",\"title\":\"Evolutionary study and structural basis of proton sensing by Mus GPR4 and Xenopus GPR4.\",\"volume\":\"188\"},\"referenceNumber\":2,\"referencePositions\":[\"STRUCTURE BY ELECTRON MICROSCOPY\",\"DISULFIDE BONDS\",\"FUNCTION\",\"ACTIVITY REGULATION\",\"DOMAIN\",\"MUTAGENESIS OF GLU-51; VAL-119; PRO-122; LEU-123; HIS-159; HIS-165; SER-171; TYR-172; SER-214 AND HIS-276\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:25:33.494326+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a744101e779b456c34c37646ab2aee926ca32698d73eef5421228a17149aa4e1",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6I8PUB9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25)

```json
{
  "entry_version": 25,
  "evidence_id": "H1",
  "excerpt": "ID   GPR4_XENTR              Reviewed;         353 AA.\nAC   A0A6I8PUB9;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   12-AUG-2020, sequence version 1.\nDT   28-JAN-2026, entry version 25.\nDE   RecName: Full=G-protein coupled receptor 4;\nDE            Short=XtGPR4 {ECO:0000303|PubMed:39753131};\nGN   Name=gpr4;\nOS   Xenopus tropicalis (Western clawed frog) (Silurana tropicalis).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Amphibia;\nOC   Batrachia; Anura; Pipoidea; Pipidae; Xenopodinae; Xenopus; Silurana.\nOX   NCBI_TaxID=8364;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:39.964772+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "57795ac8541e9349c417ffab8858e9955615bd1d0fd8bb5a206b1104334eba37",
  "url": "https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25)

```json
{
  "entry_version": 25,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   STRUCTURE BY ELECTRON MICROSCOPY, DISULFIDE BONDS, FUNCTION, ACTIVITY\nRP   REGULATION, DOMAIN, AND MUTAGENESIS OF GLU-51; VAL-119; PRO-122; LEU-123;\nRP   HIS-159; HIS-165; SER-171; TYR-172; SER-214 AND HIS-276.\nRX   PubMed=39753131; DOI=10.1016/j.cell.2024.12.001;\nRA   Wen X., Shang P., Chen H., Guo L., Rong N., Jiang X., Li X., Liu J.,\nRA   Yang G., Zhang J., Zhu K., Meng Q., He X., Wang Z., Liu Z., Cheng H.,\nRA   Zheng Y., Zhang B., Pang J., Liu Z., Xiao P., Chen Y., Liu L., Luo F.,\nRA   Yu X., Yi F., Zhang P., Yang F., Deng C., Sun J.P.;\nRT   \"Evolutionary study and structural basis of proton sensing by Mus GPR4 and\nRT   Xenopus GPR4.\";\nRL   Cell 188:653-670(2025).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:39.964772+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 27-38",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "57795ac8541e9349c417ffab8858e9955615bd1d0fd8bb5a206b1104334eba37",
  "url": "https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25)

```json
{
  "entry_version": 25,
  "evidence_id": "H3",
  "excerpt": "FT   TOPO_DOM        1..8\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000269|PubMed:39753131\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:39.964772+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 139-141",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "57795ac8541e9349c417ffab8858e9955615bd1d0fd8bb5a206b1104334eba37",
  "url": "https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25)

```json
{
  "entry_version": 25,
  "evidence_id": "H4",
  "excerpt": "FT   TRANSMEM        9..45\nFT                   /note=\"Helical; Name=1\"\nFT                   /evidence=\"ECO:0000269|PubMed:39753131\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:39.964772+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 142-144",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "57795ac8541e9349c417ffab8858e9955615bd1d0fd8bb5a206b1104334eba37",
  "url": "https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25)

```json
{
  "entry_version": 25,
  "evidence_id": "H5",
  "excerpt": "FT   TOPO_DOM        46..49\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000269|PubMed:39753131\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:39.964772+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 145-147",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "57795ac8541e9349c417ffab8858e9955615bd1d0fd8bb5a206b1104334eba37",
  "url": "https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25)

```json
{
  "entry_version": 25,
  "evidence_id": "H6",
  "excerpt": "FT   TRANSMEM        50..80\nFT                   /note=\"Helical; Name=2\"\nFT                   /evidence=\"ECO:0000269|PubMed:39753131\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:39.964772+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 148-150",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "57795ac8541e9349c417ffab8858e9955615bd1d0fd8bb5a206b1104334eba37",
  "url": "https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25)

```json
{
  "entry_version": 25,
  "evidence_id": "H7",
  "excerpt": "FT   TOPO_DOM        81..85\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000269|PubMed:39753131\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:39.964772+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 151-153",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "57795ac8541e9349c417ffab8858e9955615bd1d0fd8bb5a206b1104334eba37",
  "url": "https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25)

```json
{
  "entry_version": 25,
  "evidence_id": "H8",
  "excerpt": "FT   TRANSMEM        86..121\nFT                   /note=\"Helical; Name=3\"\nFT                   /evidence=\"ECO:0000269|PubMed:39753131\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:39.964772+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 154-156",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "57795ac8541e9349c417ffab8858e9955615bd1d0fd8bb5a206b1104334eba37",
  "url": "https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25)

```json
{
  "entry_version": 25,
  "evidence_id": "H9",
  "excerpt": "FT   TOPO_DOM        122..129\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000269|PubMed:39753131\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:39.964772+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 157-159",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "57795ac8541e9349c417ffab8858e9955615bd1d0fd8bb5a206b1104334eba37",
  "url": "https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25)

```json
{
  "entry_version": 25,
  "evidence_id": "H10",
  "excerpt": "FT   TRANSMEM        130..156\nFT                   /note=\"Helical; Name=4\"\nFT                   /evidence=\"ECO:0000269|PubMed:39753131\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:39.964772+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 160-162",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "57795ac8541e9349c417ffab8858e9955615bd1d0fd8bb5a206b1104334eba37",
  "url": "https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25)

```json
{
  "entry_version": 25,
  "evidence_id": "H11",
  "excerpt": "FT   TOPO_DOM        157..172\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000269|PubMed:39753131\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:39.964772+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 163-165",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "57795ac8541e9349c417ffab8858e9955615bd1d0fd8bb5a206b1104334eba37",
  "url": "https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25)

```json
{
  "entry_version": 25,
  "evidence_id": "H12",
  "excerpt": "FT   TRANSMEM        173..211\nFT                   /note=\"Helical; Name=5\"\nFT                   /evidence=\"ECO:0000269|PubMed:39753131\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:39.964772+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 166-168",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "57795ac8541e9349c417ffab8858e9955615bd1d0fd8bb5a206b1104334eba37",
  "url": "https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25)

```json
{
  "entry_version": 25,
  "evidence_id": "H13",
  "excerpt": "FT   TOPO_DOM        212..215\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000269|PubMed:39753131\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:39.964772+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 169-171",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "57795ac8541e9349c417ffab8858e9955615bd1d0fd8bb5a206b1104334eba37",
  "url": "https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25)

```json
{
  "entry_version": 25,
  "evidence_id": "H14",
  "excerpt": "FT   TRANSMEM        216..251\nFT                   /note=\"Helical; Name=6\"\nFT                   /evidence=\"ECO:0000269|PubMed:39753131\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:39.964772+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 172-174",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "57795ac8541e9349c417ffab8858e9955615bd1d0fd8bb5a206b1104334eba37",
  "url": "https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25"
}
```

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25)

```json
{
  "entry_version": 25,
  "evidence_id": "H15",
  "excerpt": "FT   TOPO_DOM        252..267\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000269|PubMed:39753131\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:39.964772+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 175-177",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "57795ac8541e9349c417ffab8858e9955615bd1d0fd8bb5a206b1104334eba37",
  "url": "https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25"
}
```

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25)

```json
{
  "entry_version": 25,
  "evidence_id": "H16",
  "excerpt": "FT   TRANSMEM        268..296\nFT                   /note=\"Helical; Name=7\"\nFT                   /evidence=\"ECO:0000269|PubMed:39753131\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:39.964772+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 178-180",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "57795ac8541e9349c417ffab8858e9955615bd1d0fd8bb5a206b1104334eba37",
  "url": "https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25"
}
```

### Evidence H17

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25)

```json
{
  "entry_version": 25,
  "evidence_id": "H17",
  "excerpt": "FT   TOPO_DOM        297..353\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000269|PubMed:39753131\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:39.964772+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 181-183",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "57795ac8541e9349c417ffab8858e9955615bd1d0fd8bb5a206b1104334eba37",
  "url": "https://rest.uniprot.org/unisave/A0A6I8PUB9?format=txt&versions=25"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 25. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
