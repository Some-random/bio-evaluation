# transmembrane_0011

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0011.txt)

**Task:** `transmembrane`  
**Expected answer:** **B** — 139..159; 191..211; 251..271; 280..300; 321..341

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MASGQMAPSLLRRPITFVSSCPPALRSFGALCPPTGSTDLIGGTGRDILIAAAPARRAPLHATLPLLRSLHTSPAPQLSASHQHQAQQQQQQTKQPQQPYDPQQDQVPSTSTASSSKPAADPVYNLPNAVSVARLVSGPLIGYWLVQGHYEAATLALAVSGASDWLDGWLARRLGASSVFGSYLDPLADKVLIGCVAAALLMNGAMPGWVAGVVVGRDVLLVAGSFVFRLRGFGWRWPGAAAFFRTVDTSAAAAGAATGAANGVASGGGGGGEGVSFMRPLLISKANTVLQLLLLGGYLLRGMDGGAGLQLLLPGGGGEELIMGLELATAATTVASGLAYGTMAVQGKLFK

[Multiple Choices]
A. 139..159; 191..211; 251..271; 280..300; 322..338
B. 139..159; 191..211; 251..271; 280..300; 321..341
C. 6..29
D. 139..159; 191..211; 251..271; 280..300
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

> The sequence-matched historical UniProt record annotates all five spans in choice B. These annotations support the key, but their ECO:0000255 evidence is computational rather than experimental.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains several hydrophobic regions consistent with membrane-spanning helices, and transferable knowledge can support a multi-pass membrane-protein interpretation. But choices A and B differ only in the endpoints of the same overlapping final candidate helix; hydrophobicity and typical helix length do not uniquely establish those exact boundaries.


**Missing item-specific fact**

> The target-specific annotation or measurement fixing the final helix boundaries at 321..341 rather than 322..338.


**Reason**

> General sequence and membrane-protein knowledge can identify the likely spans, but it does not meaningfully resolve the small endpoint difference between A and B. Selecting the recorded coordinates requires an exact boundary annotation or measurement for this protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Both choices include the same four spans and overlapping versions of the final candidate helix. The supplied sequence does not establish a unique sharp boundary between the two proposed ranges.


### Important caveats

- The cited database features are computational predictions, not direct experimental confirmation.
- The historical record matches the supplied sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains several hydrophobic regions consistent with membrane-spanning helices, and transferable knowledge can support a multi-pass membrane-protein interpretation. But choices A and B differ only in the endpoints of the same overlapping final candidate helix; hydrophobicity and typical helix length do not uniquely establish those exact boundaries.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The target-specific annotation or measurement fixing the final helix boundaries at 321..341 rather than 322..338.",
    "reason": "General sequence and membrane-protein knowledge can identify the likely spans, but it does not meaningfully resolve the small endpoint difference between A and B. Selecting the recorded coordinates requires an exact boundary annotation or measurement for this protein."
  },
  "case_id": "transmembrane_0011",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H4",
      "H5",
      "H6",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record annotates all five spans in choice B. These annotations support the key, but their ECO:0000255 evidence is computational rather than experimental."
  },
  "important_caveats": [
    "The cited database features are computational predictions, not direct experimental confirmation.",
    "The historical record matches the supplied sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Both choices include the same four spans and overlapping versions of the final candidate helix. The supplied sequence does not establish a unique sharp boundary between the two proposed ranges."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0011",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record annotates all five spans in choice B. These annotations support the key, but their ECO:0000255 evidence is computational rather than experimental.",
    "evidence_ids": ["H3", "H4", "H5", "H6", "H7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains several hydrophobic regions consistent with membrane-spanning helices, and transferable knowledge can support a multi-pass membrane-protein interpretation. But choices A and B differ only in the endpoints of the same overlapping final candidate helix; hydrophobicity and typical helix length do not uniquely establish those exact boundaries.",
    "missing_item_specific_fact": "The target-specific annotation or measurement fixing the final helix boundaries at 321..341 rather than 322..338.",
    "reason": "General sequence and membrane-protein knowledge can identify the likely spans, but it does not meaningfully resolve the small endpoint difference between A and B. Selecting the recorded coordinates requires an exact boundary annotation or measurement for this protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Both choices include the same four spans and overlapping versions of the final candidate helix. The supplied sequence does not establish a unique sharp boundary between the two proposed ranges."
  },
  "important_caveats": [
    "The cited database features are computational predictions, not direct experimental confirmation.",
    "The historical record matches the supplied sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for A0A2K3D1C8 lists exactly five transmembrane helical segments at 139-159, 191-211, 251-271, 280-300, and 321-341 (all ECO:0000255, by similarity). Choice B matches these coordinates precisely. The annotations are computational predictions transferred by similarity, not experimental determinations, but they are the recorded source annotation.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Option C (6..29) can be eliminated because the N-terminal region contains charged residues (R, R, R) and lacks the continuous hydrophobic stretch required for a TM helix. The 4-vs-5 TM question (D vs A/B) is borderline: the region around 321-341 has partial hydrophobic character (L, I, M, L, L, A, A, A, V, A, L, A) but also contains E, T, S, G, Y, G, making TM classification uncertain. The critical A-vs-B distinction (322..338 vs 321..341) is a 2-3 residue boundary shift. A weak biophysical argument exists: TM helices typically require ~19-20+ residues to span the ~30 Å hydrophobic core, so 17 residues (option A) falls below the typical minimum while 21 residues (option B) is within range. However, this argument is undermined by the poor overall hydrophobicity of the region—neither 17 nor 21 residues in this sequence constitutes a convincing TM helix by standard hydropathy criteria. The exact boundary is essentially an artifact of the specific prediction algorithm (Phobius/TMpred-type) used to generate the annotation.


**Missing item-specific fact**

> The exact start/end coordinates (321 vs 322; 338 vs 341) of the fifth transmembrane helix as assigned by the specific computational algorithm used in the UniProt annotation. The sequence in this region is too borderline for hydropathy analysis to reliably resolve a 2-3 residue boundary difference.


**Reason**

> The A-vs-B distinction hinges on a 2-3 residue boundary in a region with marginal hydrophobicity. While the 'minimum ~20 residues for a TM helix' principle provides a weak probabilistic preference for B (21 residues) over A (17 residues), the poor hydrophobicity of the region (containing E, T, S, Y, multiple G) means the TM classification itself is uncertain, making the length argument unreliable. The exact boundary is algorithm-specific and cannot be confidently resolved from the sequence alone. A model would need to recall the specific UniProt annotation coordinates.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B",
  "D"
]
```

> D (4 TM regions) is defensible because the fifth region (321-341) has poor hydrophobicity and could be rejected by strict criteria. A (322..338) is defensible because 17 residues, while short, is not impossible for a TM helix, and the region's hydrophobic core arguably ends around position 338. B is supported by the annotation and the 21-residue length argument, but the margin over A is small.


### Important caveats

- All five TM annotations carry evidence code ECO:0000255 (by similarity), meaning they are computational predictions transferred from related proteins, not experimentally validated.
- The fifth TM region (321-341) has the weakest hydrophobic character of the five annotated segments, making its classification and boundaries the most uncertain.
- The distinction between options A and B (322..338 vs 321..341) is within the typical ±2-3 residue uncertainty of TM prediction algorithms.
- The protein is annotated as a cardiolipin synthase (CMP-forming, EC 2.7.8.41) from Chlamydomonas, a membrane enzyme, but this identity was not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Option C (6..29) can be eliminated because the N-terminal region contains charged residues (R, R, R) and lacks the continuous hydrophobic stretch required for a TM helix. The 4-vs-5 TM question (D vs A/B) is borderline: the region around 321-341 has partial hydrophobic character (L, I, M, L, L, A, A, A, V, A, L, A) but also contains E, T, S, G, Y, G, making TM classification uncertain. The critical A-vs-B distinction (322..338 vs 321..341) is a 2-3 residue boundary shift. A weak biophysical argument exists: TM helices typically require ~19-20+ residues to span the ~30 Å hydrophobic core, so 17 residues (option A) falls below the typical minimum while 21 residues (option B) is within range. However, this argument is undermined by the poor overall hydrophobicity of the region—neither 17 nor 21 residues in this sequence constitutes a convincing TM helix by standard hydropathy criteria. The exact boundary is essentially an artifact of the specific prediction algorithm (Phobius/TMpred-type) used to generate the annotation.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact start/end coordinates (321 vs 322; 338 vs 341) of the fifth transmembrane helix as assigned by the specific computational algorithm used in the UniProt annotation. The sequence in this region is too borderline for hydropathy analysis to reliably resolve a 2-3 residue boundary difference.",
    "reason": "The A-vs-B distinction hinges on a 2-3 residue boundary in a region with marginal hydrophobicity. While the 'minimum ~20 residues for a TM helix' principle provides a weak probabilistic preference for B (21 residues) over A (17 residues), the poor hydrophobicity of the region (containing E, T, S, Y, multiple G) means the TM classification itself is uncertain, making the length argument unreliable. The exact boundary is algorithm-specific and cannot be confidently resolved from the sequence alone. A model would need to recall the specific UniProt annotation coordinates."
  },
  "case_id": "transmembrane_0011",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "H3",
      "H4",
      "H5",
      "H6",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for A0A2K3D1C8 lists exactly five transmembrane helical segments at 139-159, 191-211, 251-271, 280-300, and 321-341 (all ECO:0000255, by similarity). Choice B matches these coordinates precisely. The annotations are computational predictions transferred by similarity, not experimental determinations, but they are the recorded source annotation."
  },
  "important_caveats": [
    "All five TM annotations carry evidence code ECO:0000255 (by similarity), meaning they are computational predictions transferred from related proteins, not experimentally validated.",
    "The fifth TM region (321-341) has the weakest hydrophobic character of the five annotated segments, making its classification and boundaries the most uncertain.",
    "The distinction between options A and B (322..338 vs 321..341) is within the typical ±2-3 residue uncertainty of TM prediction algorithms.",
    "The protein is annotated as a cardiolipin synthase (CMP-forming, EC 2.7.8.41) from Chlamydomonas, a membrane enzyme, but this identity was not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B",
      "D"
    ],
    "reason": "D (4 TM regions) is defensible because the fifth region (321-341) has poor hydrophobicity and could be rejected by strict criteria. A (322..338) is defensible because 17 residues, while short, is not impossible for a TM helix, and the region's hydrophobic core arguably ends around position 338. B is supported by the annotation and the 21-residue length argument, but the margin over A is small."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0011",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for A0A2K3D1C8 lists exactly five transmembrane helical segments at 139-159, 191-211, 251-271, 280-300, and 321-341 (all ECO:0000255, by similarity). Choice B matches these coordinates precisely. The annotations are computational predictions transferred by similarity, not experimental determinations, but they are the recorded source annotation.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "H3", "H4", "H5", "H6", "H7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Option C (6..29) can be eliminated because the N-terminal region contains charged residues (R, R, R) and lacks the continuous hydrophobic stretch required for a TM helix. The 4-vs-5 TM question (D vs A/B) is borderline: the region around 321-341 has partial hydrophobic character (L, I, M, L, L, A, A, A, V, A, L, A) but also contains E, T, S, G, Y, G, making TM classification uncertain. The critical A-vs-B distinction (322..338 vs 321..341) is a 2-3 residue boundary shift. A weak biophysical argument exists: TM helices typically require ~19-20+ residues to span the ~30 Å hydrophobic core, so 17 residues (option A) falls below the typical minimum while 21 residues (option B) is within range. However, this argument is undermined by the poor overall hydrophobicity of the region—neither 17 nor 21 residues in this sequence constitutes a convincing TM helix by standard hydropathy criteria. The exact boundary is essentially an artifact of the specific prediction algorithm (Phobius/TMpred-type) used to generate the annotation.",
    "missing_item_specific_fact": "The exact start/end coordinates (321 vs 322; 338 vs 341) of the fifth transmembrane helix as assigned by the specific computational algorithm used in the UniProt annotation. The sequence in this region is too borderline for hydropathy analysis to reliably resolve a 2-3 residue boundary difference.",
    "reason": "The A-vs-B distinction hinges on a 2-3 residue boundary in a region with marginal hydrophobicity. While the 'minimum ~20 residues for a TM helix' principle provides a weak probabilistic preference for B (21 residues) over A (17 residues), the poor hydrophobicity of the region (containing E, T, S, Y, multiple G) means the TM classification itself is uncertain, making the length argument unreliable. The exact boundary is algorithm-specific and cannot be confidently resolved from the sequence alone. A model would need to recall the specific UniProt annotation coordinates."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B", "D"],
    "reason": "D (4 TM regions) is defensible because the fifth region (321-341) has poor hydrophobicity and could be rejected by strict criteria. A (322..338) is defensible because 17 residues, while short, is not impossible for a TM helix, and the region's hydrophobic core arguably ends around position 338. B is supported by the annotation and the 21-residue length argument, but the margin over A is small."
  },
  "important_caveats": [
    "All five TM annotations carry evidence code ECO:0000255 (by similarity), meaning they are computational predictions transferred from related proteins, not experimentally validated.",
    "The fifth TM region (321-341) has the weakest hydrophobic character of the five annotated segments, making its classification and boundaries the most uncertain.",
    "The distinction between options A and B (322..338 vs 321..341) is within the typical ±2-3 residue uncertainty of TM prediction algorithms.",
    "The protein is annotated as a cardiolipin synthase (CMP-forming, EC 2.7.8.41) from Chlamydomonas, a membrane enzyme, but this identity was not provided to the evaluated model."
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
  "benchmark_sequence_length": 351,
  "benchmark_sequence_sha256": "d5caa566c264b21e72ce662ef50949e75c0df2a96713facfc4330fbd74359ca1",
  "current_entry_audit": {
    "entryVersion": 33,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2018-03-28",
    "sequenceVersion": 1
  },
  "current_record_sha256": "26e9b73e0d86ca30bf42039424c27469e24cd0f504b95de4718d0e72ea3a9a16",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 351,
  "current_source_sequence_sha256": "d5caa566c264b21e72ce662ef50949e75c0df2a96713facfc4330fbd74359ca1",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 31,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A2K3D1C8",
  "selected_historical_entry_version": 31,
  "selected_historical_record_sha256": "59f1e23ac2c4d5a40557e3d481dab63f297277a1a4b73ab6748fe911f7d4716c",
  "selected_historical_source_sequence_length": 351,
  "selected_historical_source_sequence_sha256": "d5caa566c264b21e72ce662ef50949e75c0df2a96713facfc4330fbd74359ca1",
  "selected_historical_version": {
    "accession": "A0A2K3D1C8",
    "database": "Swiss-Prot",
    "entryVersion": 31,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CRLS1_CHLRE",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A2K3D1C8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:48.321314+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "26e9b73e0d86ca30bf42039424c27469e24cd0f504b95de4718d0e72ea3a9a16",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":33,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2018-03-28\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:48.321314+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "26e9b73e0d86ca30bf42039424c27469e24cd0f504b95de4718d0e72ea3a9a16",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Chlamydomonas smithii\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000006906\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Chlorophyta\",\"core chlorophytes\",\"Chlorophyceae\",\"CS clade\",\"Chlamydomonadales\",\"Chlamydomonadaceae\",\"Chlamydomonas\"],\"scientificName\":\"Chlamydomonas reinhardtii\",\"taxonId\":3055}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:48.321314+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "26e9b73e0d86ca30bf42039424c27469e24cd0f504b95de4718d0e72ea3a9a16",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"26793177\",\"source\":\"PubMed\"}],\"value\":\"2.7.8.41\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Cardiolipin synthase (CMP-forming)\"},\"shortNames\":[{\"value\":\"CLS\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:48.321314+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "26e9b73e0d86ca30bf42039424c27469e24cd0f504b95de4718d0e72ea3a9a16",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":159},\"start\":{\"modifier\":\"EXACT\",\"value\":139}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:24:48.321314+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "26e9b73e0d86ca30bf42039424c27469e24cd0f504b95de4718d0e72ea3a9a16",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":211},\"start\":{\"modifier\":\"EXACT\",\"value\":191}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:24:48.321314+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "26e9b73e0d86ca30bf42039424c27469e24cd0f504b95de4718d0e72ea3a9a16",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":271},\"start\":{\"modifier\":\"EXACT\",\"value\":251}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:24:48.321314+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "26e9b73e0d86ca30bf42039424c27469e24cd0f504b95de4718d0e72ea3a9a16",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":300},\"start\":{\"modifier\":\"EXACT\",\"value\":280}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:24:48.321314+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "26e9b73e0d86ca30bf42039424c27469e24cd0f504b95de4718d0e72ea3a9a16",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":341},\"start\":{\"modifier\":\"EXACT\",\"value\":321}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:24:48.321314+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "26e9b73e0d86ca30bf42039424c27469e24cd0f504b95de4718d0e72ea3a9a16",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Hung C.H.\",\"Kobayashi K.\",\"Wada H.\",\"Nakamura Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"26793177\"},{\"database\":\"DOI\",\"id\":\"10.3389/fmicb.2015.01542\"}],\"citationType\":\"journal article\",\"firstPage\":\"1542\",\"id\":\"26793177\",\"journal\":\"Front. Microbiol.\",\"lastPage\":\"1542\",\"publicationDate\":\"2015\",\"title\":\"Functional Specificity of Cardiolipin Synthase Revealed by the Identification of a Cardiolipin Synthase CrCLS1 in Chlamydomonas reinhardtii.\",\"volume\":\"6\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:24:48.321314+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "26e9b73e0d86ca30bf42039424c27469e24cd0f504b95de4718d0e72ea3a9a16",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2K3D1C8.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H1",
  "excerpt": "ID   CRLS1_CHLRE             Reviewed;         351 AA.\nAC   A0A2K3D1C8;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   28-MAR-2018, sequence version 1.\nDT   28-JAN-2026, entry version 31.\nDE   RecName: Full=Cardiolipin synthase (CMP-forming) {ECO:0000305};\nDE            Short=CLS;\nDE            EC=2.7.8.41 {ECO:0000305|PubMed:26793177};\nDE   Flags: Precursor;\nGN   ORFNames=CHLRE_13g604700v5 {ECO:0000312|EMBL:PNW74341.1};\nOS   Chlamydomonas reinhardtii (Chlamydomonas smithii).\nOC   Eukaryota; Viridiplantae; Chlorophyta; core chlorophytes; Chlorophyceae;\nOC   CS clade; Chlamydomonadales; Chlamydomonadaceae; Chlamydomonas.\nOX   NCBI_TaxID=3055 {ECO:0000312|Proteomes:UP000006906};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:52.248527+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "59f1e23ac2c4d5a40557e3d481dab63f297277a1a4b73ab6748fe911f7d4716c",
  "url": "https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, AND CATALYTIC ACTIVITY.\nRX   PubMed=26793177; DOI=10.3389/fmicb.2015.01542;\nRA   Hung C.H., Kobayashi K., Wada H., Nakamura Y.;\nRT   \"Functional Specificity of Cardiolipin Synthase Revealed by the\nRT   Identification of a Cardiolipin Synthase CrCLS1 in Chlamydomonas\nRT   reinhardtii.\";\nRL   Front. Microbiol. 6:1542-1542(2015).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:52.248527+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 43-50",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "59f1e23ac2c4d5a40557e3d481dab63f297277a1a4b73ab6748fe911f7d4716c",
  "url": "https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H3",
  "excerpt": "FT   TRANSMEM        139..159\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:52.248527+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 118-120",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "59f1e23ac2c4d5a40557e3d481dab63f297277a1a4b73ab6748fe911f7d4716c",
  "url": "https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H4",
  "excerpt": "FT   TRANSMEM        191..211\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:52.248527+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 121-123",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "59f1e23ac2c4d5a40557e3d481dab63f297277a1a4b73ab6748fe911f7d4716c",
  "url": "https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H5",
  "excerpt": "FT   TRANSMEM        251..271\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:52.248527+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 124-126",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "59f1e23ac2c4d5a40557e3d481dab63f297277a1a4b73ab6748fe911f7d4716c",
  "url": "https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H6",
  "excerpt": "FT   TRANSMEM        280..300\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:52.248527+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 127-129",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "59f1e23ac2c4d5a40557e3d481dab63f297277a1a4b73ab6748fe911f7d4716c",
  "url": "https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H7",
  "excerpt": "FT   TRANSMEM        321..341\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:52.248527+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 130-132",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "59f1e23ac2c4d5a40557e3d481dab63f297277a1a4b73ab6748fe911f7d4716c",
  "url": "https://rest.uniprot.org/unisave/A0A2K3D1C8?format=txt&versions=31"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 11. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
