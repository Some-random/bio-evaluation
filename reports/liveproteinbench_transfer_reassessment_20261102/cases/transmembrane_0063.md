# transmembrane_0063

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0063.txt)

**Task:** `transmembrane`  
**Expected answer:** **D** — 58..78

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MPAREVYLKRPATRRQLEGICTRYDGQQRITQLDCEEGCSKRTQPPQRLNPRYKSPDLIHISFIIVLLCILSMTSSVVAQTTTGSSSSKAAATPILPRQTLPTTISLPPLNISHPVLQLALPPTSSLYLTFSICSLTSNATILPTVLISTSSPASFNLGSKPIRDASTGGIPTSSGGKGYNYKSGRNGATWGLKWSSGFGNWTLNGTSETQVHLLLGLGLGNDGSTLNTTGVGNGNVVVQMGASTSGPLHALSAVYPLLGDTTSTSALIFSPLLYSSPQPEPSYPNYTLPGAQLAFPDFSYSEPLNSSLSSNLTLIVVPTNASPTSTDLGNSICAINAASANSSVSGANNTILKSFQPEWMTVGDEQGFRSYWVLGDLAEQGNYTAWVSDDKGVLSQPAWFATKPAGFPCQLVMPNDVCPNLGYSAPLDANSTAVTSPSGATISPTSPIQTLPDDLLELIVQNLEAFSTSLLSHACGRDLFSHVSSCLDCYSAYRDWLCRIVVPQCGAANSTSGATVIETATSTSTSSGTFPTPSTVLRTPSSPRNPSLPIPAYSYYELLPCMSTCNRADRSCPVSMGIRCPKRKVNAAKSYAFVGDDHSYGDGSAAQGVAAQDRWGNRWCNG

[Multiple Choices]
A. 227..249
B. 59..78
C. 58..78; 431..451
D. 58..78
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

> The sequence-matched UniProt annotation identifies residues 58–78 as a helical transmembrane region. This supports the keyed coordinates, though the cited ECO:0000255 annotation is computational rather than direct experimental evidence.

Citations as saved: [H4](#evidence-h4), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a roughly 21-residue hydrophobic stretch at the coordinates given by B and D, consistent with a membrane-spanning alpha helix. The region offered by A is not comparably hydrophobic, and C additionally proposes a second segment that is not a similarly convincing membrane-spanning stretch.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A standard transferable sequence-based feature—an extended hydrophobic stretch of membrane-spanning length—meaningfully distinguishes the 58–78 region from the alternatives. This supports the region, but cannot distinguish between B and D because they give identical coordinates.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> B and D are identical answers, so both are defensible and the wording provides no basis to select one over the other.


### Important caveats

- The supplied source annotations support the coordinates but do not establish direct experimental validation.
- Option C includes the supported 58–78 segment as well as an additional candidate, so it is not equivalent to the single-region answer.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a roughly 21-residue hydrophobic stretch at the coordinates given by B and D, consistent with a membrane-spanning alpha helix. The region offered by A is not comparably hydrophobic, and C additionally proposes a second segment that is not a similarly convincing membrane-spanning stretch.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A standard transferable sequence-based feature—an extended hydrophobic stretch of membrane-spanning length—meaningfully distinguishes the 58–78 region from the alternatives. This supports the region, but cannot distinguish between B and D because they give identical coordinates."
  },
  "case_id": "transmembrane_0063",
  "expected_answer_check": {
    "evidence_ids": [
      "H4",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies residues 58–78 as a helical transmembrane region. This supports the keyed coordinates, though the cited ECO:0000255 annotation is computational rather than direct experimental evidence."
  },
  "important_caveats": [
    "The supplied source annotations support the coordinates but do not establish direct experimental validation.",
    "Option C includes the supported 58–78 segment as well as an additional candidate, so it is not equivalent to the single-region answer."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "B and D are identical answers, so both are defensible and the wording provides no basis to select one over the other."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0063",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies residues 58–78 as a helical transmembrane region. This supports the keyed coordinates, though the cited ECO:0000255 annotation is computational rather than direct experimental evidence.",
    "evidence_ids": ["H4", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a roughly 21-residue hydrophobic stretch at the coordinates given by B and D, consistent with a membrane-spanning alpha helix. The region offered by A is not comparably hydrophobic, and C additionally proposes a second segment that is not a similarly convincing membrane-spanning stretch.",
    "missing_item_specific_fact": "",
    "reason": "A standard transferable sequence-based feature—an extended hydrophobic stretch of membrane-spanning length—meaningfully distinguishes the 58–78 region from the alternatives. This supports the region, but cannot distinguish between B and D because they give identical coordinates."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "B and D are identical answers, so both are defensible and the wording provides no basis to select one over the other."
  },
  "important_caveats": [
    "The supplied source annotations support the coordinates but do not establish direct experimental validation.",
    "Option C includes the supported 58–78 segment as well as an additional candidate, so it is not equivalent to the single-region answer."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (evidence code ECO:0000255, by similarity) records a single transmembrane helix at positions 58..78, with extracellular domain 1..57 and cytoplasmic domain 79..623. This directly supports choice D (58..78). The annotation is computational (by similarity) rather than experimentally determined, but it is the recorded annotation for this entry. The sequence at positions 58-78 (LIHISFIIVLLCILSMTSSVV) is a hydrophobic stretch bounded by Asp(57) on the N-terminal side and polar residues (A, Q, T, T, T, G, S...) on the C-terminal side, consistent with a single-pass TM helix.

Citations as saved: [C6](#evidence-c6), [H4](#evidence-h4), [C5](#evidence-c5), [C7](#evidence-c7), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A model can perform hydrophobicity analysis on the provided sequence. The region around positions 55-80 shows a clear hydrophobic stretch: position 56 is Pro (helix breaker), position 57 is Asp (charged, incompatible with TM), positions 58-78 are dominated by Leu, Ile, Phe, Val, Met (strongly hydrophobic), and position 79 onward transitions to Ala, Gln, Thr, Gly, Ser (polar). This identifies 58..78 as the TM helix. Choice A (227..249: LNTTGVGNGNVVVQMGASTSGPL) is clearly not hydrophobic. Choice C adds a second TM at 431..451 (NSTAVTSPSGATISPTSPIQTL), which is rich in polar/charged residues (Asn, Ser, Thr, Gln) and cannot be a TM helix. The distinction between B (59..78) and D (58..78) rests on whether position 58 (Leu, highly hydrophobic) belongs in the TM segment: since position 57 is Asp (charged) and position 58 is Leu (hydrophobic), the hydrophobic stretch begins at 58, making D the better answer. The question also asks for 'a segment' (singular), which disfavors C listing two regions.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The hydrophobicity profile of the sequence, combined with standard knowledge that TM helices are hydrophobic alpha-helices of ~20 residues bounded by polar/charged residues, allows elimination of A and C outright and a defensible preference for D over B based on the identity of residue 58 (Leu, hydrophobic) versus 57 (Asp, charged). This is a standard sequence-based inference applicable to any protein, not a lookup of this protein's specific annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> The distinction between B (59..78) and D (58..78) is a single-residue boundary difference. While hydrophobicity analysis favors including Leu(58) in the TM segment, some TM prediction algorithms or manual annotations might trim the boundary by one residue. However, the presence of charged Asp at 57 and the strongly hydrophobic Leu at 58 make D the more defensible choice. This is a minor boundary ambiguity rather than a fundamental ambiguity, as the hydrophobicity argument clearly supports 58 as the start.


### Important caveats

- The UniProt TM annotation uses evidence code ECO:0000255 (by similarity), indicating computational inference rather than experimental determination.
- The distinction between choices B and D is a one-residue boundary issue; while the hydrophobicity argument favors D, this is a fine-grained distinction that some predictors might resolve differently.
- The protein is annotated as a stretch-activated cation channel (MID1) with a single TM helix and a large cytoplasmic domain, consistent with the single-TM answer.
- The reviewer-only evidence confirms sequence match (SHA-256 identical) between the benchmark sequence and the UniProt entry.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A model can perform hydrophobicity analysis on the provided sequence. The region around positions 55-80 shows a clear hydrophobic stretch: position 56 is Pro (helix breaker), position 57 is Asp (charged, incompatible with TM), positions 58-78 are dominated by Leu, Ile, Phe, Val, Met (strongly hydrophobic), and position 79 onward transitions to Ala, Gln, Thr, Gly, Ser (polar). This identifies 58..78 as the TM helix. Choice A (227..249: LNTTGVGNGNVVVQMGASTSGPL) is clearly not hydrophobic. Choice C adds a second TM at 431..451 (NSTAVTSPSGATISPTSPIQTL), which is rich in polar/charged residues (Asn, Ser, Thr, Gln) and cannot be a TM helix. The distinction between B (59..78) and D (58..78) rests on whether position 58 (Leu, highly hydrophobic) belongs in the TM segment: since position 57 is Asp (charged) and position 58 is Leu (hydrophobic), the hydrophobic stretch begins at 58, making D the better answer. The question also asks for 'a segment' (singular), which disfavors C listing two regions.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The hydrophobicity profile of the sequence, combined with standard knowledge that TM helices are hydrophobic alpha-helices of ~20 residues bounded by polar/charged residues, allows elimination of A and C outright and a defensible preference for D over B based on the identity of residue 58 (Leu, hydrophobic) versus 57 (Asp, charged). This is a standard sequence-based inference applicable to any protein, not a lookup of this protein's specific annotation."
  },
  "case_id": "transmembrane_0063",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "H4",
      "C5",
      "C7",
      "H3",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence code ECO:0000255, by similarity) records a single transmembrane helix at positions 58..78, with extracellular domain 1..57 and cytoplasmic domain 79..623. This directly supports choice D (58..78). The annotation is computational (by similarity) rather than experimentally determined, but it is the recorded annotation for this entry. The sequence at positions 58-78 (LIHISFIIVLLCILSMTSSVV) is a hydrophobic stretch bounded by Asp(57) on the N-terminal side and polar residues (A, Q, T, T, T, G, S...) on the C-terminal side, consistent with a single-pass TM helix."
  },
  "important_caveats": [
    "The UniProt TM annotation uses evidence code ECO:0000255 (by similarity), indicating computational inference rather than experimental determination.",
    "The distinction between choices B and D is a one-residue boundary issue; while the hydrophobicity argument favors D, this is a fine-grained distinction that some predictors might resolve differently.",
    "The protein is annotated as a stretch-activated cation channel (MID1) with a single TM helix and a large cytoplasmic domain, consistent with the single-TM answer.",
    "The reviewer-only evidence confirms sequence match (SHA-256 identical) between the benchmark sequence and the UniProt entry."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "The distinction between B (59..78) and D (58..78) is a single-residue boundary difference. While hydrophobicity analysis favors including Leu(58) in the TM segment, some TM prediction algorithms or manual annotations might trim the boundary by one residue. However, the presence of charged Asp at 57 and the strongly hydrophobic Leu at 58 make D the more defensible choice. This is a minor boundary ambiguity rather than a fundamental ambiguity, as the hydrophobicity argument clearly supports 58 as the start."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0063",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence code ECO:0000255, by similarity) records a single transmembrane helix at positions 58..78, with extracellular domain 1..57 and cytoplasmic domain 79..623. This directly supports choice D (58..78). The annotation is computational (by similarity) rather than experimentally determined, but it is the recorded annotation for this entry. The sequence at positions 58-78 (LIHISFIIVLLCILSMTSSVV) is a hydrophobic stretch bounded by Asp(57) on the N-terminal side and polar residues (A, Q, T, T, T, G, S...) on the C-terminal side, consistent with a single-pass TM helix.",
    "evidence_ids": ["C6", "H4", "C5", "C7", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A model can perform hydrophobicity analysis on the provided sequence. The region around positions 55-80 shows a clear hydrophobic stretch: position 56 is Pro (helix breaker), position 57 is Asp (charged, incompatible with TM), positions 58-78 are dominated by Leu, Ile, Phe, Val, Met (strongly hydrophobic), and position 79 onward transitions to Ala, Gln, Thr, Gly, Ser (polar). This identifies 58..78 as the TM helix. Choice A (227..249: LNTTGVGNGNVVVQMGASTSGPL) is clearly not hydrophobic. Choice C adds a second TM at 431..451 (NSTAVTSPSGATISPTSPIQTL), which is rich in polar/charged residues (Asn, Ser, Thr, Gln) and cannot be a TM helix. The distinction between B (59..78) and D (58..78) rests on whether position 58 (Leu, highly hydrophobic) belongs in the TM segment: since position 57 is Asp (charged) and position 58 is Leu (hydrophobic), the hydrophobic stretch begins at 58, making D the better answer. The question also asks for 'a segment' (singular), which disfavors C listing two regions.",
    "missing_item_specific_fact": "",
    "reason": "The hydrophobicity profile of the sequence, combined with standard knowledge that TM helices are hydrophobic alpha-helices of ~20 residues bounded by polar/charged residues, allows elimination of A and C outright and a defensible preference for D over B based on the identity of residue 58 (Leu, hydrophobic) versus 57 (Asp, charged). This is a standard sequence-based inference applicable to any protein, not a lookup of this protein's specific annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "The distinction between B (59..78) and D (58..78) is a single-residue boundary difference. While hydrophobicity analysis favors including Leu(58) in the TM segment, some TM prediction algorithms or manual annotations might trim the boundary by one residue. However, the presence of charged Asp at 57 and the strongly hydrophobic Leu at 58 make D the more defensible choice. This is a minor boundary ambiguity rather than a fundamental ambiguity, as the hydrophobicity argument clearly supports 58 as the start."
  },
  "important_caveats": [
    "The UniProt TM annotation uses evidence code ECO:0000255 (by similarity), indicating computational inference rather than experimental determination.",
    "The distinction between choices B and D is a one-residue boundary issue; while the hydrophobicity argument favors D, this is a fine-grained distinction that some predictors might resolve differently.",
    "The protein is annotated as a stretch-activated cation channel (MID1) with a single TM helix and a large cytoplasmic domain, consistent with the single-TM answer.",
    "The reviewer-only evidence confirms sequence match (SHA-256 identical) between the benchmark sequence and the UniProt entry."
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
  "benchmark_sequence_length": 623,
  "benchmark_sequence_sha256": "3579d1a1040ea01e21c17e5edbd32710bf365c4f46ce4aef54d0eb0255558685",
  "current_entry_audit": {
    "entryVersion": 44,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2013-11-13",
    "sequenceVersion": 2
  },
  "current_record_sha256": "7eb86781b1aba624db3eae2dbb2fdef8a485dda8d568205f7f3827ebe928f923",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 623,
  "current_source_sequence_sha256": "3579d1a1040ea01e21c17e5edbd32710bf365c4f46ce4aef54d0eb0255558685",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 42,
      "exact_sequence_comparison": "matched",
      "sequence_version": 2
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "J9VIL4",
  "selected_historical_entry_version": 42,
  "selected_historical_record_sha256": "c1d506108a574b5a95ba76e4cb46c67370d560b8e22b21bb5ef44affca09647a",
  "selected_historical_source_sequence_length": 623,
  "selected_historical_source_sequence_sha256": "3579d1a1040ea01e21c17e5edbd32710bf365c4f46ce4aef54d0eb0255558685",
  "selected_historical_version": {
    "accession": "J9VIL4",
    "database": "Swiss-Prot",
    "entryVersion": 42,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MID1_CRYN9",
    "sequenceVersion": 2
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VIL4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"J9VIL4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:28:54.584597+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7eb86781b1aba624db3eae2dbb2fdef8a485dda8d568205f7f3827ebe928f923",
  "url": "https://rest.uniprot.org/uniprotkb/J9VIL4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VIL4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":44,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2013-11-13\",\"sequenceVersion\":2}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:28:54.584597+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7eb86781b1aba624db3eae2dbb2fdef8a485dda8d568205f7f3827ebe928f923",
  "url": "https://rest.uniprot.org/uniprotkb/J9VIL4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VIL4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Cryptococcus neoformans var. grubii serotype A\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000010091\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Basidiomycota\",\"Agaricomycotina\",\"Tremellomycetes\",\"Tremellales\",\"Cryptococcaceae\",\"Cryptococcus\",\"Cryptococcus neoformans species complex\"],\"scientificName\":\"Cryptococcus neoformans (strain H99 / ATCC 208821 / CBS 10515 / FGSC 9487)\",\"taxonId\":235443}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:28:54.584597+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7eb86781b1aba624db3eae2dbb2fdef8a485dda8d568205f7f3827ebe928f923",
  "url": "https://rest.uniprot.org/uniprotkb/J9VIL4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VIL4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Stretch-activated cation channel MID1\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:28:54.584597+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7eb86781b1aba624db3eae2dbb2fdef8a485dda8d568205f7f3827ebe928f923",
  "url": "https://rest.uniprot.org/uniprotkb/J9VIL4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VIL4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":57},\"start\":{\"modifier\":\"EXACT\",\"value\":1}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:28:54.584597+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7eb86781b1aba624db3eae2dbb2fdef8a485dda8d568205f7f3827ebe928f923",
  "url": "https://rest.uniprot.org/uniprotkb/J9VIL4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VIL4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":78},\"start\":{\"modifier\":\"EXACT\",\"value\":58}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:28:54.584597+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7eb86781b1aba624db3eae2dbb2fdef8a485dda8d568205f7f3827ebe928f923",
  "url": "https://rest.uniprot.org/uniprotkb/J9VIL4.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VIL4.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":623},\"start\":{\"modifier\":\"EXACT\",\"value\":79}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:28:54.584597+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7eb86781b1aba624db3eae2dbb2fdef8a485dda8d568205f7f3827ebe928f923",
  "url": "https://rest.uniprot.org/uniprotkb/J9VIL4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VIL4?format=txt&versions=42)

```json
{
  "entry_version": 42,
  "evidence_id": "H1",
  "excerpt": "ID   MID1_CRYN9              Reviewed;         623 AA.\nAC   J9VIL4;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   13-NOV-2013, sequence version 2.\nDT   28-JAN-2026, entry version 42.\nDE   RecName: Full=Stretch-activated cation channel MID1 {ECO:0000305};\nGN   Name=MID1 {ECO:0000303|PubMed:20123986};\nGN   ORFNames=CNAG_03751 {ECO:0000312|EMBL:AFR93256.2};\nOS   Cryptococcus neoformans (strain H99 / ATCC 208821 / CBS 10515 / FGSC 9487)\nOS   (Cryptococcus neoformans var. grubii serotype A).\nOC   Eukaryota; Fungi; Dikarya; Basidiomycota; Agaricomycotina; Tremellomycetes;\nOC   Tremellales; Cryptococcaceae; Cryptococcus;\nOC   Cryptococcus neoformans species complex.\nOX   NCBI_TaxID=235443 {ECO:0000312|Proteomes:UP000010091};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:56.856231+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c1d506108a574b5a95ba76e4cb46c67370d560b8e22b21bb5ef44affca09647a",
  "url": "https://rest.uniprot.org/unisave/J9VIL4?format=txt&versions=42"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VIL4?format=txt&versions=42)

```json
{
  "entry_version": 42,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, SUBUNIT, IDENTIFICATION IN A COMPLEX WITH CCH1, SUBCELLULAR\nRP   LOCATION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=20123986; DOI=10.1074/jbc.m109.056218;\nRA   Hong M.P., Vu K., Bautos J., Gelli A.;\nRT   \"Cch1 restores intracellular Ca2+ in fungal cells during endoplasmic\nRT   reticulum stress.\";\nRL   J. Biol. Chem. 285:10951-10958(2010).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:56.856231+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 34-41",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c1d506108a574b5a95ba76e4cb46c67370d560b8e22b21bb5ef44affca09647a",
  "url": "https://rest.uniprot.org/unisave/J9VIL4?format=txt&versions=42"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VIL4?format=txt&versions=42)

```json
{
  "entry_version": 42,
  "evidence_id": "H3",
  "excerpt": "FT   TOPO_DOM        1..57\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:56.856231+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 106-108",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c1d506108a574b5a95ba76e4cb46c67370d560b8e22b21bb5ef44affca09647a",
  "url": "https://rest.uniprot.org/unisave/J9VIL4?format=txt&versions=42"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VIL4?format=txt&versions=42)

```json
{
  "entry_version": 42,
  "evidence_id": "H4",
  "excerpt": "FT   TRANSMEM        58..78\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:56.856231+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 109-111",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c1d506108a574b5a95ba76e4cb46c67370d560b8e22b21bb5ef44affca09647a",
  "url": "https://rest.uniprot.org/unisave/J9VIL4?format=txt&versions=42"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VIL4?format=txt&versions=42)

```json
{
  "entry_version": 42,
  "evidence_id": "H5",
  "excerpt": "FT   TOPO_DOM        79..623\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:56.856231+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 112-114",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c1d506108a574b5a95ba76e4cb46c67370d560b8e22b21bb5ef44affca09647a",
  "url": "https://rest.uniprot.org/unisave/J9VIL4?format=txt&versions=42"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 63. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
