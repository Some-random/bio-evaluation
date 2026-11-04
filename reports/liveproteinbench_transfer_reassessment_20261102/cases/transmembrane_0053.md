# transmembrane_0053

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0053.txt)

**Task:** `transmembrane`  
**Expected answer:** **D** — 51..77; 132..157

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MDGSHCKVIAPLLTERHQRMVTKDGHSTLQMDGAQTGLAYLRDAWGILMDMRWRWMMLVFSASFVIHWLVFAVLWYILAEMNGDLGLDHDAPPENHTICVKYITSFTAAFSFSLETQLTIGYGTMFPSGDCPSAIALLAIQMLLGLMLEAFITGAFVAKIARPKNRAFSIRFTDLAVVAHIDGKPNLIFQVANTRPSPLTNVRVSAVLYQERENGKLYQTSVDFHLDGISSEECPFFIFPLTYYHSIIPSSPLATLLQHENPPHFELVVFLSAMQEGTGETCQRRTSYLPSEIMLHHCFASLLARGSKGEYQIKMENFDKTTPEFQTPLVSKSPNRTDLDIHINGQSIDNFQISETGLTE

[Multiple Choices]
A. 17..53; 58..88; 94..129; 138..164; 181..218; 223..258; 269..297
B. 132..157
C. 48..80; 132..157
D. 51..77; 132..157
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

> The matched historical UniProt record annotates both 51..77 and 132..157 as transmembrane helices, supporting choice D. These annotations are transferred by similarity to another protein, not direct experimental evidence for this sequence.

Citations as saved: [H3](#evidence-h3), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has two prominent hydrophobic stretches, around 51..77 and 132..157, separated by a region consistent with the pore-loop architecture of a two-transmembrane-helix potassium channel. Transferable knowledge of this channel-family architecture supports D over A, which proposes many spans, and B, which omits the first span. Compared with C, D gives the tighter interval for the first helix; the extra residues in C extend toward flanking sequence, including an acidic residue at the C-terminal edge.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and family-level pattern provide a credible basis for selecting the two membrane-spanning helices. Exact boundaries remain less certain from sequence alone, but the alternatives meaningfully favor D's tighter first interval.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> C is close to D, but its wider first interval includes flanking residues; the sequence supports the tighter hydrophobic helix interval in D.


### Important caveats

- The supporting database annotations are similarity-based rather than direct experimental measurements for this protein.
- Membrane-helix boundaries can vary somewhat with annotation or prediction method.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has two prominent hydrophobic stretches, around 51..77 and 132..157, separated by a region consistent with the pore-loop architecture of a two-transmembrane-helix potassium channel. Transferable knowledge of this channel-family architecture supports D over A, which proposes many spans, and B, which omits the first span. Compared with C, D gives the tighter interval for the first helix; the extra residues in C extend toward flanking sequence, including an acidic residue at the C-terminal edge.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and family-level pattern provide a credible basis for selecting the two membrane-spanning helices. Exact boundaries remain less certain from sequence alone, but the alternatives meaningfully favor D's tighter first interval."
  },
  "case_id": "transmembrane_0053",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The matched historical UniProt record annotates both 51..77 and 132..157 as transmembrane helices, supporting choice D. These annotations are transferred by similarity to another protein, not direct experimental evidence for this sequence."
  },
  "important_caveats": [
    "The supporting database annotations are similarity-based rather than direct experimental measurements for this protein.",
    "Membrane-helix boundaries can vary somewhat with annotation or prediction method."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "C is close to D, but its wider first interval includes flanking residues; the sequence supports the tighter hydrophobic helix interval in D."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0053",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched historical UniProt record annotates both 51..77 and 132..157 as transmembrane helices, supporting choice D. These annotations are transferred by similarity to another protein, not direct experimental evidence for this sequence.",
    "evidence_ids": ["H3", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has two prominent hydrophobic stretches, around 51..77 and 132..157, separated by a region consistent with the pore-loop architecture of a two-transmembrane-helix potassium channel. Transferable knowledge of this channel-family architecture supports D over A, which proposes many spans, and B, which omits the first span. Compared with C, D gives the tighter interval for the first helix; the extra residues in C extend toward flanking sequence, including an acidic residue at the C-terminal edge.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and family-level pattern provide a credible basis for selecting the two membrane-spanning helices. Exact boundaries remain less certain from sequence alone, but the alternatives meaningfully favor D's tighter first interval."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "C is close to D, but its wider first interval includes flanking residues; the sequence supports the tighter hydrophobic helix interval in D."
  },
  "important_caveats": [
    "The supporting database annotations are similarity-based rather than direct experimental measurements for this protein.",
    "Membrane-helix boundaries can vary somewhat with annotation or prediction method."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (evidence C6, C10, H3, H7) explicitly records Transmembrane helices at 51-77 (M1) and 132-157 (M2), matching answer D exactly. The evidence codes are ECO:0000250 (similarity-based transfer from human Kir2.1, P49655), indicating computational annotation by homology rather than direct experimental determination. Nevertheless, the Kir channel 2-TM + P-loop topology is well-established, and the annotated boundaries are consistent with the hydrophobic core of the sequence. The expected answer is supported by the supplied evidence.

Citations as saved: [C6](#evidence-c6), [C10](#evidence-c10), [H3](#evidence-h3), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Multiple transferable inferences narrow the choices. (1) Kir channels (inward rectifier K+ channels) have a canonical 2-TM + P-loop topology, not the 7-TM GPCR fold; this eliminates option A, which lists seven TM segments. (2) A Kir channel must have two TM helices (M1 and M2), so option B (only 132..157) is incomplete. (3) The distinction between C (48..80) and D (51..77) for the M1 boundary can be resolved by hydrophobicity analysis of the supplied sequence: position 50 is Asp (D, charged) and position 80 is Glu (E, charged). Standard TM helix boundary rules place the start at the first hydrophobic residue after a charged residue and the end at the last hydrophobic residue before a charged residue. Starting at M51 (hydrophobic) and ending at I77 (hydrophobic) respects these boundaries, whereas C includes the charged D50 and E80 within the TM segment. Additionally, Kir M1 helices are known from the family (e.g., Kir2.1, Kir1.1) to be relatively short (~25-27 residues) and tilted, consistent with a 27-residue helix (51-77) rather than a 33-residue helix (48-80). The M2 region (132-157) is shared by C and D, so the only discriminating feature is the M1 boundary, which the hydrophobicity criterion resolves.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence itself contains charged residues (D50, E80) at the boundaries that distinguish C from D under standard TM helix prediction rules. Kir channel family topology knowledge (2 TM + P-loop, short tilted M1) eliminates A and B. No target-specific annotation beyond general Kir channel biology and hydrophobicity principles is needed to reach D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While the M1 boundary is somewhat approximate in TM prediction generally, the presence of charged residues at positions 50 (D) and 80 (E) provides a clear hydrophobicity-based rationale for choosing D (51-77) over C (48-80). The other options (A: wrong topology, B: incomplete) are clearly eliminable. No genuine ambiguity remains among the offered choices.


### Important caveats

- The UniProt TM annotations are based on similarity transfer (ECO:0000250 from P49655, human Kir2.1), not direct experimental structure determination of this bovine Kir7.1 protein.
- TM helix boundaries are inherently approximate; different prediction tools may shift boundaries by a few residues. The distinction between C and D (3-residue shift at each end) is within the typical uncertainty of TM prediction, but the charged-residue argument provides a principled basis for preferring D.
- The reviewer-only evidence identifies this as Bos taurus Kir7.1 (E1BN00), but this identification was not available to the evaluated model; the reasoning above relies only on sequence-level hydrophobicity analysis and general Kir channel family knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Multiple transferable inferences narrow the choices. (1) Kir channels (inward rectifier K+ channels) have a canonical 2-TM + P-loop topology, not the 7-TM GPCR fold; this eliminates option A, which lists seven TM segments. (2) A Kir channel must have two TM helices (M1 and M2), so option B (only 132..157) is incomplete. (3) The distinction between C (48..80) and D (51..77) for the M1 boundary can be resolved by hydrophobicity analysis of the supplied sequence: position 50 is Asp (D, charged) and position 80 is Glu (E, charged). Standard TM helix boundary rules place the start at the first hydrophobic residue after a charged residue and the end at the last hydrophobic residue before a charged residue. Starting at M51 (hydrophobic) and ending at I77 (hydrophobic) respects these boundaries, whereas C includes the charged D50 and E80 within the TM segment. Additionally, Kir M1 helices are known from the family (e.g., Kir2.1, Kir1.1) to be relatively short (~25-27 residues) and tilted, consistent with a 27-residue helix (51-77) rather than a 33-residue helix (48-80). The M2 region (132-157) is shared by C and D, so the only discriminating feature is the M1 boundary, which the hydrophobicity criterion resolves.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence itself contains charged residues (D50, E80) at the boundaries that distinguish C from D under standard TM helix prediction rules. Kir channel family topology knowledge (2 TM + P-loop, short tilted M1) eliminates A and B. No target-specific annotation beyond general Kir channel biology and hydrophobicity principles is needed to reach D."
  },
  "case_id": "transmembrane_0053",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C10",
      "H3",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C6, C10, H3, H7) explicitly records Transmembrane helices at 51-77 (M1) and 132-157 (M2), matching answer D exactly. The evidence codes are ECO:0000250 (similarity-based transfer from human Kir2.1, P49655), indicating computational annotation by homology rather than direct experimental determination. Nevertheless, the Kir channel 2-TM + P-loop topology is well-established, and the annotated boundaries are consistent with the hydrophobic core of the sequence. The expected answer is supported by the supplied evidence."
  },
  "important_caveats": [
    "The UniProt TM annotations are based on similarity transfer (ECO:0000250 from P49655, human Kir2.1), not direct experimental structure determination of this bovine Kir7.1 protein.",
    "TM helix boundaries are inherently approximate; different prediction tools may shift boundaries by a few residues. The distinction between C and D (3-residue shift at each end) is within the typical uncertainty of TM prediction, but the charged-residue argument provides a principled basis for preferring D.",
    "The reviewer-only evidence identifies this as Bos taurus Kir7.1 (E1BN00), but this identification was not available to the evaluated model; the reasoning above relies only on sequence-level hydrophobicity analysis and general Kir channel family knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the M1 boundary is somewhat approximate in TM prediction generally, the presence of charged residues at positions 50 (D) and 80 (E) provides a clear hydrophobicity-based rationale for choosing D (51-77) over C (48-80). The other options (A: wrong topology, B: incomplete) are clearly eliminable. No genuine ambiguity remains among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0053",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C6, C10, H3, H7) explicitly records Transmembrane helices at 51-77 (M1) and 132-157 (M2), matching answer D exactly. The evidence codes are ECO:0000250 (similarity-based transfer from human Kir2.1, P49655), indicating computational annotation by homology rather than direct experimental determination. Nevertheless, the Kir channel 2-TM + P-loop topology is well-established, and the annotated boundaries are consistent with the hydrophobic core of the sequence. The expected answer is supported by the supplied evidence.",
    "evidence_ids": ["C6", "C10", "H3", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Multiple transferable inferences narrow the choices. (1) Kir channels (inward rectifier K+ channels) have a canonical 2-TM + P-loop topology, not the 7-TM GPCR fold; this eliminates option A, which lists seven TM segments. (2) A Kir channel must have two TM helices (M1 and M2), so option B (only 132..157) is incomplete. (3) The distinction between C (48..80) and D (51..77) for the M1 boundary can be resolved by hydrophobicity analysis of the supplied sequence: position 50 is Asp (D, charged) and position 80 is Glu (E, charged). Standard TM helix boundary rules place the start at the first hydrophobic residue after a charged residue and the end at the last hydrophobic residue before a charged residue. Starting at M51 (hydrophobic) and ending at I77 (hydrophobic) respects these boundaries, whereas C includes the charged D50 and E80 within the TM segment. Additionally, Kir M1 helices are known from the family (e.g., Kir2.1, Kir1.1) to be relatively short (~25-27 residues) and tilted, consistent with a 27-residue helix (51-77) rather than a 33-residue helix (48-80). The M2 region (132-157) is shared by C and D, so the only discriminating feature is the M1 boundary, which the hydrophobicity criterion resolves.",
    "missing_item_specific_fact": "",
    "reason": "The sequence itself contains charged residues (D50, E80) at the boundaries that distinguish C from D under standard TM helix prediction rules. Kir channel family topology knowledge (2 TM + P-loop, short tilted M1) eliminates A and B. No target-specific annotation beyond general Kir channel biology and hydrophobicity principles is needed to reach D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the M1 boundary is somewhat approximate in TM prediction generally, the presence of charged residues at positions 50 (D) and 80 (E) provides a clear hydrophobicity-based rationale for choosing D (51-77) over C (48-80). The other options (A: wrong topology, B: incomplete) are clearly eliminable. No genuine ambiguity remains among the offered choices."
  },
  "important_caveats": [
    "The UniProt TM annotations are based on similarity transfer (ECO:0000250 from P49655, human Kir2.1), not direct experimental structure determination of this bovine Kir7.1 protein.",
    "TM helix boundaries are inherently approximate; different prediction tools may shift boundaries by a few residues. The distinction between C and D (3-residue shift at each end) is within the typical uncertainty of TM prediction, but the charged-residue argument provides a principled basis for preferring D.",
    "The reviewer-only evidence identifies this as Bos taurus Kir7.1 (E1BN00), but this identification was not available to the evaluated model; the reasoning above relies only on sequence-level hydrophobicity analysis and general Kir channel family knowledge."
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
  "benchmark_sequence_length": 360,
  "benchmark_sequence_sha256": "feb9d6140c91f297df4e1b3bf9a9bd39d203ad60b8fd9106c95f00ca1a7abda5",
  "current_entry_audit": {
    "entryVersion": 87,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2010-11-02",
    "sequenceVersion": 1
  },
  "current_record_sha256": "7246b2eb4549dfb47f31cd992990356778022560a9d7b5e49262f934a1c773a8",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 360,
  "current_source_sequence_sha256": "feb9d6140c91f297df4e1b3bf9a9bd39d203ad60b8fd9106c95f00ca1a7abda5",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 85,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "E1BN00",
  "selected_historical_entry_version": 85,
  "selected_historical_record_sha256": "4b9086c0d9c9ac0bc55162776e962e7edd043bea19b585c2259e8c880bcc5a3a",
  "selected_historical_source_sequence_length": 360,
  "selected_historical_source_sequence_sha256": "feb9d6140c91f297df4e1b3bf9a9bd39d203ad60b8fd9106c95f00ca1a7abda5",
  "selected_historical_version": {
    "accession": "E1BN00",
    "database": "Swiss-Prot",
    "entryVersion": 85,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "KCJ13_BOVIN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E1BN00.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"E1BN00\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:28:00.720540+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7246b2eb4549dfb47f31cd992990356778022560a9d7b5e49262f934a1c773a8",
  "url": "https://rest.uniprot.org/uniprotkb/E1BN00.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E1BN00.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":87,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2010-11-02\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:28:00.720540+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7246b2eb4549dfb47f31cd992990356778022560a9d7b5e49262f934a1c773a8",
  "url": "https://rest.uniprot.org/uniprotkb/E1BN00.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E1BN00.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Bovine\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Euteleostomi\",\"Mammalia\",\"Eutheria\",\"Laurasiatheria\",\"Artiodactyla\",\"Ruminantia\",\"Pecora\",\"Bovidae\",\"Bovinae\",\"Bos\"],\"scientificName\":\"Bos taurus\",\"taxonId\":9913}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:28:00.720540+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7246b2eb4549dfb47f31cd992990356778022560a9d7b5e49262f934a1c773a8",
  "url": "https://rest.uniprot.org/uniprotkb/E1BN00.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E1BN00.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O60928\",\"source\":\"UniProtKB\"}],\"value\":\"Inward rectifier K(+) channel Kir7.1\"}},{\"fullName\":{\"value\":\"Potassium channel, inwardly rectifying subfamily J member 13\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O60928\",\"source\":\"UniProtKB\"}],\"value\":\"Inward rectifier potassium channel 13\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:28:00.720540+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7246b2eb4549dfb47f31cd992990356778022560a9d7b5e49262f934a1c773a8",
  "url": "https://rest.uniprot.org/uniprotkb/E1BN00.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E1BN00.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":50},\"start\":{\"modifier\":\"EXACT\",\"value\":1}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:28:00.720540+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7246b2eb4549dfb47f31cd992990356778022560a9d7b5e49262f934a1c773a8",
  "url": "https://rest.uniprot.org/uniprotkb/E1BN00.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E1BN00.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical; Name=M1\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P49655\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":77},\"start\":{\"modifier\":\"EXACT\",\"value\":51}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:28:00.720540+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7246b2eb4549dfb47f31cd992990356778022560a9d7b5e49262f934a1c773a8",
  "url": "https://rest.uniprot.org/uniprotkb/E1BN00.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E1BN00.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":105},\"start\":{\"modifier\":\"EXACT\",\"value\":78}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:28:00.720540+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7246b2eb4549dfb47f31cd992990356778022560a9d7b5e49262f934a1c773a8",
  "url": "https://rest.uniprot.org/uniprotkb/E1BN00.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E1BN00.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Helical; Pore-forming\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P49655\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":122},\"start\":{\"modifier\":\"EXACT\",\"value\":106}},\"type\":\"Intramembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:28:00.720540+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7246b2eb4549dfb47f31cd992990356778022560a9d7b5e49262f934a1c773a8",
  "url": "https://rest.uniprot.org/uniprotkb/E1BN00.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E1BN00.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":131},\"start\":{\"modifier\":\"EXACT\",\"value\":123}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:28:00.720540+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7246b2eb4549dfb47f31cd992990356778022560a9d7b5e49262f934a1c773a8",
  "url": "https://rest.uniprot.org/uniprotkb/E1BN00.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E1BN00.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"Helical; Name=M2\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P49655\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":157},\"start\":{\"modifier\":\"EXACT\",\"value\":132}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:28:00.720540+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7246b2eb4549dfb47f31cd992990356778022560a9d7b5e49262f934a1c773a8",
  "url": "https://rest.uniprot.org/uniprotkb/E1BN00.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E1BN00.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":360},\"start\":{\"modifier\":\"EXACT\",\"value\":158}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:28:00.720540+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7246b2eb4549dfb47f31cd992990356778022560a9d7b5e49262f934a1c773a8",
  "url": "https://rest.uniprot.org/uniprotkb/E1BN00.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E1BN00?format=txt&versions=85)

```json
{
  "entry_version": 85,
  "evidence_id": "H1",
  "excerpt": "ID   KCJ13_BOVIN             Reviewed;         360 AA.\nAC   E1BN00;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   02-NOV-2010, sequence version 1.\nDT   28-JAN-2026, entry version 85.\nDE   RecName: Full=Inward rectifier potassium channel 13 {ECO:0000250|UniProtKB:O60928};\nDE   AltName: Full=Inward rectifier K(+) channel Kir7.1 {ECO:0000250|UniProtKB:O60928};\nDE   AltName: Full=Potassium channel, inwardly rectifying subfamily J member 13;\nGN   Name=KCNJ13;\nOS   Bos taurus (Bovine).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;\nOC   Eutheria; Laurasiatheria; Artiodactyla; Ruminantia; Pecora; Bovidae;\nOC   Bovinae; Bos.\nOX   NCBI_TaxID=9913;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:05.462686+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4b9086c0d9c9ac0bc55162776e962e7edd043bea19b585c2259e8c880bcc5a3a",
  "url": "https://rest.uniprot.org/unisave/E1BN00?format=txt&versions=85"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E1BN00?format=txt&versions=85)

```json
{
  "entry_version": 85,
  "evidence_id": "H2",
  "excerpt": "FT   TOPO_DOM        1..50\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:05.462686+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 119-121",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4b9086c0d9c9ac0bc55162776e962e7edd043bea19b585c2259e8c880bcc5a3a",
  "url": "https://rest.uniprot.org/unisave/E1BN00?format=txt&versions=85"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E1BN00?format=txt&versions=85)

```json
{
  "entry_version": 85,
  "evidence_id": "H3",
  "excerpt": "FT   TRANSMEM        51..77\nFT                   /note=\"Helical; Name=M1\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P49655\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:05.462686+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 122-124",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4b9086c0d9c9ac0bc55162776e962e7edd043bea19b585c2259e8c880bcc5a3a",
  "url": "https://rest.uniprot.org/unisave/E1BN00?format=txt&versions=85"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E1BN00?format=txt&versions=85)

```json
{
  "entry_version": 85,
  "evidence_id": "H4",
  "excerpt": "FT   TOPO_DOM        78..105\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:05.462686+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 125-127",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4b9086c0d9c9ac0bc55162776e962e7edd043bea19b585c2259e8c880bcc5a3a",
  "url": "https://rest.uniprot.org/unisave/E1BN00?format=txt&versions=85"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E1BN00?format=txt&versions=85)

```json
{
  "entry_version": 85,
  "evidence_id": "H5",
  "excerpt": "FT   INTRAMEM        106..122\nFT                   /note=\"Helical; Pore-forming\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P49655\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:05.462686+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 128-130",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4b9086c0d9c9ac0bc55162776e962e7edd043bea19b585c2259e8c880bcc5a3a",
  "url": "https://rest.uniprot.org/unisave/E1BN00?format=txt&versions=85"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E1BN00?format=txt&versions=85)

```json
{
  "entry_version": 85,
  "evidence_id": "H6",
  "excerpt": "FT   TOPO_DOM        123..131\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:05.462686+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 131-133",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4b9086c0d9c9ac0bc55162776e962e7edd043bea19b585c2259e8c880bcc5a3a",
  "url": "https://rest.uniprot.org/unisave/E1BN00?format=txt&versions=85"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E1BN00?format=txt&versions=85)

```json
{
  "entry_version": 85,
  "evidence_id": "H7",
  "excerpt": "FT   TRANSMEM        132..157\nFT                   /note=\"Helical; Name=M2\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P49655\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:05.462686+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 134-136",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4b9086c0d9c9ac0bc55162776e962e7edd043bea19b585c2259e8c880bcc5a3a",
  "url": "https://rest.uniprot.org/unisave/E1BN00?format=txt&versions=85"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E1BN00?format=txt&versions=85)

```json
{
  "entry_version": 85,
  "evidence_id": "H8",
  "excerpt": "FT   TOPO_DOM        158..360\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:05.462686+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 137-139",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4b9086c0d9c9ac0bc55162776e962e7edd043bea19b585c2259e8c880bcc5a3a",
  "url": "https://rest.uniprot.org/unisave/E1BN00?format=txt&versions=85"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 53. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
