# transmembrane_0044

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0044.txt)

**Task:** `transmembrane`  
**Expected answer:** **D** — 3..23

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MELFFICGLVLFSTLSLISLFLLHNHSSARGYRLPPGRMGWPFIGESYEFLANGWKGYPEKFIFSRLAKYKPNQVFKTSILGEKVAVMCGATCNKFLFSNEGKLVNAWWPNSVNKIFPSSTQTSSKEEAKKMRKLLPTFFKPEALQRYIPIMDEIAIRHMEDEWEGKSKIEVFPLAKRYTFWLACRLFLSIDDPVHVAKFADPFNDIASGIISIPIDLPGTPFNRGIKASNVVRQELKTIIKQRKLDLSDNKASPTQDILSHMLLTPDEDGRYMNELDIADKILGLLIGGHDTASAACTFVVKFLAELPHIYDGVYKEQMEIAKSKKEGERLNWEDIQKMKYSWNVACEVMRLAPPLQGAFREALSDFMYAGFQIPKGWKLYWSANSTHRNPECFPEPEKFDPARFDGSGPAPYTYVPFGGGPRMCPGKEYARLEILVFMHNIVKRFKWEKLIPDETIVVNPMPTPAKGLPVRLRPHSKPVTVSA

[Multiple Choices]
A. 3..23; 423..447
B. 306..326; 333..353; 355..375; 466..486
C. 5..22
D. 3..23
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

> The matched sequence has a strongly hydrophobic N-terminal stretch at residues 3–23, consistent with a membrane-spanning helix. UniProt annotates this exact span as a helical signal-anchor transmembrane region, with computational evidence (ECO:0000255), rather than direct experimental evidence.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Residues 3–23 form a continuous, strongly hydrophobic N-terminal stretch of typical transmembrane-helix length, which meaningfully favors D over the internal segments in B. The sequence’s long globular remainder is also consistent with a single N-terminal signal-anchor. D gives the full plausible span, whereas C is a shorter subset.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The hydrophobic sequence pattern and general knowledge of membrane-spanning helices provide a credible basis for selecting the N-terminal region without knowing this protein’s database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C"
]
```

> The 5–22 segment in C is a highly hydrophobic subset of the same likely membrane-spanning helix and could itself be described as crossing the membrane. The sequence supports D as the fuller span, but the question does not specify that the entire span or exact boundaries must be identified.


### Important caveats

- The source annotation is computational, not direct experimental evidence.
- The exact boundaries of a transmembrane helix are not uniquely determined by sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Residues 3–23 form a continuous, strongly hydrophobic N-terminal stretch of typical transmembrane-helix length, which meaningfully favors D over the internal segments in B. The sequence’s long globular remainder is also consistent with a single N-terminal signal-anchor. D gives the full plausible span, whereas C is a shorter subset.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The hydrophobic sequence pattern and general knowledge of membrane-spanning helices provide a credible basis for selecting the N-terminal region without knowing this protein’s database annotation."
  },
  "case_id": "transmembrane_0044",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The matched sequence has a strongly hydrophobic N-terminal stretch at residues 3–23, consistent with a membrane-spanning helix. UniProt annotates this exact span as a helical signal-anchor transmembrane region, with computational evidence (ECO:0000255), rather than direct experimental evidence."
  },
  "important_caveats": [
    "The source annotation is computational, not direct experimental evidence.",
    "The exact boundaries of a transmembrane helix are not uniquely determined by sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C"
    ],
    "reason": "The 5–22 segment in C is a highly hydrophobic subset of the same likely membrane-spanning helix and could itself be described as crossing the membrane. The sequence supports D as the fuller span, but the question does not specify that the entire span or exact boundaries must be identified."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0044",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence has a strongly hydrophobic N-terminal stretch at residues 3–23, consistent with a membrane-spanning helix. UniProt annotates this exact span as a helical signal-anchor transmembrane region, with computational evidence (ECO:0000255), rather than direct experimental evidence.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Residues 3–23 form a continuous, strongly hydrophobic N-terminal stretch of typical transmembrane-helix length, which meaningfully favors D over the internal segments in B. The sequence’s long globular remainder is also consistent with a single N-terminal signal-anchor. D gives the full plausible span, whereas C is a shorter subset.",
    "missing_item_specific_fact": "",
    "reason": "The hydrophobic sequence pattern and general knowledge of membrane-spanning helices provide a credible basis for selecting the N-terminal region without knowing this protein’s database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C"],
    "reason": "The 5–22 segment in C is a highly hydrophobic subset of the same likely membrane-spanning helix and could itself be described as crossing the membrane. The sequence supports D as the fuller span, but the question does not specify that the entire span or exact boundaries must be identified."
  },
  "important_caveats": [
    "The source annotation is computational, not direct experimental evidence.",
    "The exact boundaries of a transmembrane helix are not uniquely determined by sequence alone."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (evidence C5, H3) explicitly annotates a transmembrane helix at positions 3..23, described as 'Helical; Signal-anchor for type II membrane protein' (evidence code ECO:0000255, similarity-based). The sequence at positions 3-23 (LFFICGLVLFSTLSLISLFLL) is predominantly hydrophobic (Leu, Phe, Ile, Val), consistent with a transmembrane helix. The annotation is computational/similarity-based rather than experimentally validated, but it is the recorded annotation supporting choice D.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the CYP450 heme-binding signature 'CGATCNK' (~positions 80-86) and is ~485 AA, identifying it as a plant microsomal CYP450. Transferable knowledge from other CYP450 proteins establishes that plant microsomal CYPs (unlike mitochondrial CYPs) have a single N-terminal transmembrane signal-anchor (type II membrane topology), not multiple TM helices. This immediately disfavors option B (four TM regions) and the second region in option A. The N-terminal sequence MELFFICGLVLFSTLSLISLFLLH is clearly hydrophobic from L3 through L23, with H24 breaking the hydrophobic stretch, supporting boundaries 3..23 over 5..22. The C-terminal region (residues ~420-485) contains charged/polar residues (K, E, R, H, S, N) inconsistent with a TM helix, ruling out 423..447 in option A and 466..486 in option B. The middle region is the globular catalytic domain of CYP450s, not membrane-spanning. Thus family-level CYP450 knowledge plus hydrophobicity analysis of the sequence meaningfully distinguishes D from all alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model recognizing the CYP450 fold from the heme-binding motif and knowing that plant microsomal CYPs possess a single N-terminal TM anchor can eliminate multi-TM options (B) and the spurious second TM in A. Hydrophobicity analysis of the N-terminal 25 residues identifies the hydrophobic core as L3-L23 (H24 terminates the stretch), distinguishing D from C (5..22). No fact specific to this exact protein beyond family-level CYP450 biology and sequence hydrophobicity is required.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option D (3..23) is the most defensible: the hydrophobic segment clearly begins at L3 (first hydrophobic residue after Met-Glu) and ends at L23 (H24 breaks the hydrophobicity). Option C (5..22) truncates two hydrophobic residues at each end. Options A and B include regions that are not hydrophobic. No genuine ambiguity exists among the choices.


### Important caveats

- The UniProt TM annotation uses evidence code ECO:0000255 (similarity), meaning it is a computational/transfer annotation rather than direct experimental evidence.
- The distinction between C (5..22) and D (3..23) relies on hydrophobicity boundary judgment; while L3 and F4 are hydrophobic and L23 is hydrophobic, the exact TM boundaries are inherently approximate. However, the sequence clearly supports 3..23 as the full hydrophobic stretch.
- The protein identity (CYP716A378, Saponaria officinalis) was not provided to the evaluated model; the CYP450 identification must come from recognizing the heme-binding motif in the sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the CYP450 heme-binding signature 'CGATCNK' (~positions 80-86) and is ~485 AA, identifying it as a plant microsomal CYP450. Transferable knowledge from other CYP450 proteins establishes that plant microsomal CYPs (unlike mitochondrial CYPs) have a single N-terminal transmembrane signal-anchor (type II membrane topology), not multiple TM helices. This immediately disfavors option B (four TM regions) and the second region in option A. The N-terminal sequence MELFFICGLVLFSTLSLISLFLLH is clearly hydrophobic from L3 through L23, with H24 breaking the hydrophobic stretch, supporting boundaries 3..23 over 5..22. The C-terminal region (residues ~420-485) contains charged/polar residues (K, E, R, H, S, N) inconsistent with a TM helix, ruling out 423..447 in option A and 466..486 in option B. The middle region is the globular catalytic domain of CYP450s, not membrane-spanning. Thus family-level CYP450 knowledge plus hydrophobicity analysis of the sequence meaningfully distinguishes D from all alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model recognizing the CYP450 fold from the heme-binding motif and knowing that plant microsomal CYPs possess a single N-terminal TM anchor can eliminate multi-TM options (B) and the spurious second TM in A. Hydrophobicity analysis of the N-terminal 25 residues identifies the hydrophobic core as L3-L23 (H24 terminates the stretch), distinguishing D from C (5..22). No fact specific to this exact protein beyond family-level CYP450 biology and sequence hydrophobicity is required."
  },
  "case_id": "transmembrane_0044",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C5, H3) explicitly annotates a transmembrane helix at positions 3..23, described as 'Helical; Signal-anchor for type II membrane protein' (evidence code ECO:0000255, similarity-based). The sequence at positions 3-23 (LFFICGLVLFSTLSLISLFLL) is predominantly hydrophobic (Leu, Phe, Ile, Val), consistent with a transmembrane helix. The annotation is computational/similarity-based rather than experimentally validated, but it is the recorded annotation supporting choice D."
  },
  "important_caveats": [
    "The UniProt TM annotation uses evidence code ECO:0000255 (similarity), meaning it is a computational/transfer annotation rather than direct experimental evidence.",
    "The distinction between C (5..22) and D (3..23) relies on hydrophobicity boundary judgment; while L3 and F4 are hydrophobic and L23 is hydrophobic, the exact TM boundaries are inherently approximate. However, the sequence clearly supports 3..23 as the full hydrophobic stretch.",
    "The protein identity (CYP716A378, Saponaria officinalis) was not provided to the evaluated model; the CYP450 identification must come from recognizing the heme-binding motif in the sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option D (3..23) is the most defensible: the hydrophobic segment clearly begins at L3 (first hydrophobic residue after Met-Glu) and ends at L23 (H24 breaks the hydrophobicity). Option C (5..22) truncates two hydrophobic residues at each end. Options A and B include regions that are not hydrophobic. No genuine ambiguity exists among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0044",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C5, H3) explicitly annotates a transmembrane helix at positions 3..23, described as 'Helical; Signal-anchor for type II membrane protein' (evidence code ECO:0000255, similarity-based). The sequence at positions 3-23 (LFFICGLVLFSTLSLISLFLL) is predominantly hydrophobic (Leu, Phe, Ile, Val), consistent with a transmembrane helix. The annotation is computational/similarity-based rather than experimentally validated, but it is the recorded annotation supporting choice D.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the CYP450 heme-binding signature 'CGATCNK' (~positions 80-86) and is ~485 AA, identifying it as a plant microsomal CYP450. Transferable knowledge from other CYP450 proteins establishes that plant microsomal CYPs (unlike mitochondrial CYPs) have a single N-terminal transmembrane signal-anchor (type II membrane topology), not multiple TM helices. This immediately disfavors option B (four TM regions) and the second region in option A. The N-terminal sequence MELFFICGLVLFSTLSLISLFLLH is clearly hydrophobic from L3 through L23, with H24 breaking the hydrophobic stretch, supporting boundaries 3..23 over 5..22. The C-terminal region (residues ~420-485) contains charged/polar residues (K, E, R, H, S, N) inconsistent with a TM helix, ruling out 423..447 in option A and 466..486 in option B. The middle region is the globular catalytic domain of CYP450s, not membrane-spanning. Thus family-level CYP450 knowledge plus hydrophobicity analysis of the sequence meaningfully distinguishes D from all alternatives.",
    "missing_item_specific_fact": "",
    "reason": "A model recognizing the CYP450 fold from the heme-binding motif and knowing that plant microsomal CYPs possess a single N-terminal TM anchor can eliminate multi-TM options (B) and the spurious second TM in A. Hydrophobicity analysis of the N-terminal 25 residues identifies the hydrophobic core as L3-L23 (H24 terminates the stretch), distinguishing D from C (5..22). No fact specific to this exact protein beyond family-level CYP450 biology and sequence hydrophobicity is required."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option D (3..23) is the most defensible: the hydrophobic segment clearly begins at L3 (first hydrophobic residue after Met-Glu) and ends at L23 (H24 breaks the hydrophobicity). Option C (5..22) truncates two hydrophobic residues at each end. Options A and B include regions that are not hydrophobic. No genuine ambiguity exists among the choices."
  },
  "important_caveats": [
    "The UniProt TM annotation uses evidence code ECO:0000255 (similarity), meaning it is a computational/transfer annotation rather than direct experimental evidence.",
    "The distinction between C (5..22) and D (3..23) relies on hydrophobicity boundary judgment; while L3 and F4 are hydrophobic and L23 is hydrophobic, the exact TM boundaries are inherently approximate. However, the sequence clearly supports 3..23 as the full hydrophobic stretch.",
    "The protein identity (CYP716A378, Saponaria officinalis) was not provided to the evaluated model; the CYP450 identification must come from recognizing the heme-binding motif in the sequence."
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
  "benchmark_sequence_length": 485,
  "benchmark_sequence_sha256": "c4bff1f7e639d9ca658ce7a8d1b4bea128f38e1d86d04bfb0390444eed1c9e39",
  "current_entry_audit": {
    "entryVersion": 6,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2024-11-27",
    "sequenceVersion": 1
  },
  "current_record_sha256": "3395db4e25f9768c60ce7cac240774ed32dd3f474abfda702e2c591ef35e9a76",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 485,
  "current_source_sequence_sha256": "c4bff1f7e639d9ca658ce7a8d1b4bea128f38e1d86d04bfb0390444eed1c9e39",
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
  "requested_accession": "A0AAW1NEA3",
  "selected_historical_entry_version": 5,
  "selected_historical_record_sha256": "8601238c4d3910ff611c06a4f863e8c633074e9e3c66a978a480c31233a972f5",
  "selected_historical_source_sequence_length": 485,
  "selected_historical_source_sequence_sha256": "c4bff1f7e639d9ca658ce7a8d1b4bea128f38e1d86d04bfb0390444eed1c9e39",
  "selected_historical_version": {
    "accession": "A0AAW1NEA3",
    "database": "Swiss-Prot",
    "entryVersion": 5,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "C7168_SAPOF",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1NEA3.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0AAW1NEA3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:55.776537+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3395db4e25f9768c60ce7cac240774ed32dd3f474abfda702e2c591ef35e9a76",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1NEA3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1NEA3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":6,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2024-11-27\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:55.776537+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3395db4e25f9768c60ce7cac240774ed32dd3f474abfda702e2c591ef35e9a76",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1NEA3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1NEA3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Common soapwort\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"Caryophyllales\",\"Caryophyllaceae\",\"Caryophylleae\",\"Saponaria\"],\"scientificName\":\"Saponaria officinalis\",\"synonyms\":[\"Lychnis saponaria\"],\"taxonId\":3572}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:55.776537+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3395db4e25f9768c60ce7cac240774ed32dd3f474abfda702e2c591ef35e9a76",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1NEA3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1NEA3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"Cytochrome P450 716A378\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"SoCYP716A378\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"1.14.14.126\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Beta-amyrin 28-monooxygenase CYP716A378\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:55.776537+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3395db4e25f9768c60ce7cac240774ed32dd3f474abfda702e2c591ef35e9a76",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1NEA3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1NEA3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical; Signal-anchor for type II membrane protein\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":23},\"start\":{\"modifier\":\"EXACT\",\"value\":3}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-01T06:24:55.776537+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3395db4e25f9768c60ce7cac240774ed32dd3f474abfda702e2c591ef35e9a76",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1NEA3.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1NEA3.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Jo S.\",\"El-Demerdash A.\",\"Owen C.\",\"Srivastava V.\",\"Wu D.\",\"Kikuchi S.\",\"Reed J.\",\"Hodgson H.\",\"Harkess A.\",\"Shu S.\",\"Plott C.\",\"Jenkins J.\",\"Williams M.\",\"Boston L.-B.\",\"Lacchini E.\",\"Qu T.\",\"Goossens A.\",\"Grimwood J.\",\"Schmutz J.\",\"Leebens-Mack J.\",\"Osbourn A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39043959\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41589-024-01681-7\"}],\"citationType\":\"journal article\",\"firstPage\":\"215\",\"id\":\"39043959\",\"journal\":\"Nat. Chem. Biol.\",\"lastPage\":\"226\",\"publicationDate\":\"2025\",\"title\":\"Unlocking saponin biosynthesis in soapwort.\",\"volume\":\"21\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"WWM48148.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"TISSUE SPECIFICITY\",\"PATHWAY\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:24:55.776537+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3395db4e25f9768c60ce7cac240774ed32dd3f474abfda702e2c591ef35e9a76",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1NEA3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1NEA3?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H1",
  "excerpt": "ID   C7168_SAPOF             Reviewed;         485 AA.\nAC   A0AAW1NEA3;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   27-NOV-2024, sequence version 1.\nDT   28-JAN-2026, entry version 5.\nDE   RecName: Full=Beta-amyrin 28-monooxygenase CYP716A378 {ECO:0000305};\nDE            EC=1.14.14.126 {ECO:0000269|PubMed:39043959};\nDE   AltName: Full=Cytochrome P450 716A378 {ECO:0000303|PubMed:39043959};\nDE            Short=SoCYP716A378 {ECO:0000303|PubMed:39043959};\nGN   Name=CYP716A378 {ECO:0000303|PubMed:39043959};\nGN   Synonyms=Saoffv11003497m {ECO:0000303|PubMed:39043959};\nGN   ORFNames=RND81_01G137900 {ECO:0000312|EMBL:KAK9757076.1};\nOS   Saponaria officinalis (Common soapwort) (Lychnis saponaria).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   Caryophyllales; Caryophyllaceae; Caryophylleae; Saponaria.\nOX   NCBI_TaxID=3572;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:40.561544+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8601238c4d3910ff611c06a4f863e8c633074e9e3c66a978a480c31233a972f5",
  "url": "https://rest.uniprot.org/unisave/A0AAW1NEA3?format=txt&versions=5"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1NEA3?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:WWM48148.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, TISSUE\nRP   SPECIFICITY, PATHWAY, AND BIOTECHNOLOGY.\nRX   PubMed=39043959; DOI=10.1038/s41589-024-01681-7;\nRA   Jo S., El-Demerdash A., Owen C., Srivastava V., Wu D., Kikuchi S., Reed J.,\nRA   Hodgson H., Harkess A., Shu S., Plott C., Jenkins J., Williams M.,\nRA   Boston L.-B., Lacchini E., Qu T., Goossens A., Grimwood J., Schmutz J.,\nRA   Leebens-Mack J., Osbourn A.;\nRT   \"Unlocking saponin biosynthesis in soapwort.\";\nRL   Nat. Chem. Biol. 21:215-226(2025).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:40.561544+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 18-27",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8601238c4d3910ff611c06a4f863e8c633074e9e3c66a978a480c31233a972f5",
  "url": "https://rest.uniprot.org/unisave/A0AAW1NEA3?format=txt&versions=5"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1NEA3?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H3",
  "excerpt": "FT   TRANSMEM        3..23\nFT                   /note=\"Helical; Signal-anchor for type II membrane protein\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:40.561544+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 107-109",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8601238c4d3910ff611c06a4f863e8c633074e9e3c66a978a480c31233a972f5",
  "url": "https://rest.uniprot.org/unisave/A0AAW1NEA3?format=txt&versions=5"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 44. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
