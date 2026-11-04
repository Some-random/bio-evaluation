# transmembrane_0111

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0111.txt)

**Task:** `transmembrane`  
**Expected answer:** **D** — 42..64; 84..103; 110..131; 137..157; 177..195; 201..221; 242..261; 281..301; 313..331; 347..367; 417..438

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MIEKSNNPFLSIDPIVERTKSNGEGLPLLSEKTKKGFDFTQIVVYLVGLSDGLTHLASLAIYYLFKDYFRLTPYQVSLILMYPYIPFILKPVIALITDSFSIFGMRRKPYLFLFSLFQSLNFLALAFLNLSVIQASLILFFISLCASFCTTVAEALVVESSMGQTYSQGTNKVTEFIASKAIGSLSVAYFSGYFLEKMPREYIFIATSIFPLIISLSCLFLKEKEYSTNRNIFNQLSDLIKFINTPIFLGPFLYIFVYMSGPDYDDAFFFFCTNKLGFRPSFMGTLRLTYGIASLIGIIIYRVFLKNCSLRKTLIITTLVSFPIYISPIILTEHINKFLGISNELFVLSGGFLIEAITEIQLLPLFILTANICQPGLEASVFATILSVKNLGSLTKKGTSSFITYLMKIDSYNFDNLSLYILTCGFFLLFSLTLVPLLPNEEHIEKLKNKETSKG

[Multiple Choices]
A. 308..328; 344..364; 474..494; 533..553; 640..660; 670..690; 731..751; 771..791; 807..827; 851..871; 937..957; 1162..1182; 1209..1229; 1244..1264; 1306..1326; 1381..1401; 1422..1442; 1498..1518; 1532..1552; 1561..1581; 1633..1653; 1671..1691; 1722..1742
B. 42..64; 84..103; 110..131; 138..157; 177..195; 201..221; 242..261; 281..301; 313..331; 347..367; 417..438
C. 42..64; 84..103; 110..131; 137..157; 177..195; 201..221; 242..261; 281..301; 347..367; 417..438
D. 42..64; 84..103; 110..131; 137..157; 177..195; 201..221; 242..261; 281..301; 313..331; 347..367; 417..438
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

> The exact sequence matches the source record, whose transmembrane annotations correspond to choice D. These annotations are computationally supported (ECO:0000255), not evidence of experimental validation; the historical record also contains the same spans.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [C13](#evidence-c13), [C14](#evidence-c14), [C15](#evidence-c15), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11), [H12](#evidence-h12), [H13](#evidence-h13).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has many long hydrophobic stretches characteristic of a multipass membrane protein. In particular, the hydrophobic stretch around residues 313–331 supports including that span, distinguishing choices B and D from C; the coordinates in A exceed the 455-residue sequence. The sequence supports the relevant helices without requiring knowledge of this exact protein's annotation.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable knowledge of membrane-helix hydrophobicity provides a meaningful way to rule out A and favor choices that include the hydrophobic 313–331 span. Sequence evidence alone does not reliably resolve the one-residue start-boundary difference between B and D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> B and D list the same spans except that B starts one span at residue 138 rather than 137. A one-residue boundary shift within a hydrophobic transmembrane helix is not reliably distinguishable from sequence alone, and either span plausibly crosses the membrane.


### Important caveats

- The matching source annotations are computational rather than experimentally validated.
- The exact historical source snapshot used by the author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has many long hydrophobic stretches characteristic of a multipass membrane protein. In particular, the hydrophobic stretch around residues 313–331 supports including that span, distinguishing choices B and D from C; the coordinates in A exceed the 455-residue sequence. The sequence supports the relevant helices without requiring knowledge of this exact protein's annotation.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of membrane-helix hydrophobicity provides a meaningful way to rule out A and favor choices that include the hydrophobic 313–331 span. Sequence evidence alone does not reliably resolve the one-residue start-boundary difference between B and D."
  },
  "case_id": "transmembrane_0111",
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
      "C13",
      "C14",
      "C15",
      "H3",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9",
      "H10",
      "H11",
      "H12",
      "H13"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the source record, whose transmembrane annotations correspond to choice D. These annotations are computationally supported (ECO:0000255), not evidence of experimental validation; the historical record also contains the same spans."
  },
  "important_caveats": [
    "The matching source annotations are computational rather than experimentally validated.",
    "The exact historical source snapshot used by the author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "B and D list the same spans except that B starts one span at residue 138 rather than 137. A one-residue boundary shift within a hydrophobic transmembrane helix is not reliably distinguishable from sequence alone, and either span plausibly crosses the membrane."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0111",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the source record, whose transmembrane annotations correspond to choice D. These annotations are computationally supported (ECO:0000255), not evidence of experimental validation; the historical record also contains the same spans.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "C14", "C15", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "H11", "H12", "H13"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has many long hydrophobic stretches characteristic of a multipass membrane protein. In particular, the hydrophobic stretch around residues 313–331 supports including that span, distinguishing choices B and D from C; the coordinates in A exceed the 455-residue sequence. The sequence supports the relevant helices without requiring knowledge of this exact protein's annotation.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of membrane-helix hydrophobicity provides a meaningful way to rule out A and favor choices that include the hydrophobic 313–331 span. Sequence evidence alone does not reliably resolve the one-residue start-boundary difference between B and D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "B and D list the same spans except that B starts one span at residue 138 rather than 137. A one-residue boundary shift within a hydrophobic transmembrane helix is not reliably distinguishable from sequence alone, and either span plausibly crosses the membrane."
  },
  "important_caveats": [
    "The matching source annotations are computational rather than experimentally validated.",
    "The exact historical source snapshot used by the author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q8IIK1 (Folate transporter 2, Plasmodium falciparum, 455 aa) annotates exactly 11 transmembrane helical segments at positions 42-64, 84-103, 110-131, 137-157, 177-195, 201-221, 242-261, 281-301, 313-331, 347-367, and 417-438, all with evidence code ECO:0000255 (by similarity/computational prediction). Choice D matches these annotations exactly. The sequence comparison confirms the benchmark sequence matches the UniProt entry.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [C13](#evidence-c13), [C14](#evidence-c14), [C15](#evidence-c15), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11), [H12](#evidence-h12), [H13](#evidence-h13).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Option A is eliminated because its positions (up to 1742) far exceed the 455-residue protein. Option C is eliminable by multi-pass transporter knowledge: a 455-aa membrane transporter with 10 other hydrophobic segments in MFS-like topology should have 11 TM segments, and the region 313-331 (TLIITTLVSFPIYISPIIL) sits between charged loop residues (K312, T332-E333-H334) consistent with a TM helix in a multi-pass transporter. However, the final distinction between B and D is a single-residue boundary: B has 138..157 while D has 137..157. Position 137 is L (KD=3.8) and 138 is I (KD=4.5); both are strongly hydrophobic. The preceding residue S(136) is only mildly polar (KD=-0.8). No general family rule, structural principle, or homolog comparison reliably determines whether a TM helix begins at L(137) or I(138). This single-residue boundary falls within the inherent uncertainty of all TM prediction methods and cannot be resolved by transferable knowledge of other proteins.


**Missing item-specific fact**

> The exact UniProt annotation boundary specifying that TM helix 4 starts at residue 137 rather than 138. This is a computational annotation (ECO:0000255) specific to this entry's prediction algorithm output, not derivable from general hydrophobicity or family-level principles.


**Reason**

> Options A and C can be eliminated by general reasoning (A: positions exceed protein length; C: missing a TM segment expected in a multi-pass transporter). However, the critical B vs D distinction is a single-residue difference at a TM helix boundary (137 vs 138), where both residues are strongly hydrophobic and the preceding 'polar' residue (Ser) is only mildly polar. No transferable biological principle or family-level knowledge meaningfully distinguishes these two one-residue-off boundaries. This requires the specific database annotation for this exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> B and D differ only by whether the fourth TM segment starts at residue 137 (Leu) or 138 (Ile). Both are hydrophobic residues, and the preceding Ser(136) is only mildly polar. Standard hydrophobicity analysis, window-based TM prediction, and family-level TM topology knowledge cannot reliably resolve a single-residue boundary at this position. Both choices are defensible from sequence analysis alone.


### Important caveats

- All 11 TM annotations carry evidence code ECO:0000255 (by similarity), meaning they are computational predictions, not experimentally determined boundaries.
- The annotations are from a Swiss-Prot entry first released in 2025; the underlying prediction algorithm and its boundary precision are not specified in the evidence.
- The 137 vs 138 distinction is within the typical ±1-2 residue uncertainty of TM prediction tools, making it an annotation artifact rather than a biologically meaningful distinction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Option A is eliminated because its positions (up to 1742) far exceed the 455-residue protein. Option C is eliminable by multi-pass transporter knowledge: a 455-aa membrane transporter with 10 other hydrophobic segments in MFS-like topology should have 11 TM segments, and the region 313-331 (TLIITTLVSFPIYISPIIL) sits between charged loop residues (K312, T332-E333-H334) consistent with a TM helix in a multi-pass transporter. However, the final distinction between B and D is a single-residue boundary: B has 138..157 while D has 137..157. Position 137 is L (KD=3.8) and 138 is I (KD=4.5); both are strongly hydrophobic. The preceding residue S(136) is only mildly polar (KD=-0.8). No general family rule, structural principle, or homolog comparison reliably determines whether a TM helix begins at L(137) or I(138). This single-residue boundary falls within the inherent uncertainty of all TM prediction methods and cannot be resolved by transferable knowledge of other proteins.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact UniProt annotation boundary specifying that TM helix 4 starts at residue 137 rather than 138. This is a computational annotation (ECO:0000255) specific to this entry's prediction algorithm output, not derivable from general hydrophobicity or family-level principles.",
    "reason": "Options A and C can be eliminated by general reasoning (A: positions exceed protein length; C: missing a TM segment expected in a multi-pass transporter). However, the critical B vs D distinction is a single-residue difference at a TM helix boundary (137 vs 138), where both residues are strongly hydrophobic and the preceding 'polar' residue (Ser) is only mildly polar. No transferable biological principle or family-level knowledge meaningfully distinguishes these two one-residue-off boundaries. This requires the specific database annotation for this exact protein."
  },
  "case_id": "transmembrane_0111",
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
      "C13",
      "C14",
      "C15",
      "H3",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9",
      "H10",
      "H11",
      "H12",
      "H13"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q8IIK1 (Folate transporter 2, Plasmodium falciparum, 455 aa) annotates exactly 11 transmembrane helical segments at positions 42-64, 84-103, 110-131, 137-157, 177-195, 201-221, 242-261, 281-301, 313-331, 347-367, and 417-438, all with evidence code ECO:0000255 (by similarity/computational prediction). Choice D matches these annotations exactly. The sequence comparison confirms the benchmark sequence matches the UniProt entry."
  },
  "important_caveats": [
    "All 11 TM annotations carry evidence code ECO:0000255 (by similarity), meaning they are computational predictions, not experimentally determined boundaries.",
    "The annotations are from a Swiss-Prot entry first released in 2025; the underlying prediction algorithm and its boundary precision are not specified in the evidence.",
    "The 137 vs 138 distinction is within the typical ±1-2 residue uncertainty of TM prediction tools, making it an annotation artifact rather than a biologically meaningful distinction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "B and D differ only by whether the fourth TM segment starts at residue 137 (Leu) or 138 (Ile). Both are hydrophobic residues, and the preceding Ser(136) is only mildly polar. Standard hydrophobicity analysis, window-based TM prediction, and family-level TM topology knowledge cannot reliably resolve a single-residue boundary at this position. Both choices are defensible from sequence analysis alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{"case_id":"transmembrane_0111","expected_answer_check":{"judgment":"supported","reason":"The UniProt entry Q8IIK1 (Folate transporter 2, Plasmodium falciparum, 455 aa) annotates exactly 11 transmembrane helical segments at positions 42-64, 84-103, 110-131, 137-157, 177-195, 201-221, 242-261, 281-301, 313-331, 347-367, and 417-438, all with evidence code ECO:0000255 (by similarity/computational prediction). Choice D matches these annotations exactly. The sequence comparison confirms the benchmark sequence matches the UniProt entry.","evidence_ids":["C5","C6","C7","C8","C9","C10","C11","C12","C13","C14","C15","H3","H4","H5","H6","H7","H8","H9","H10","H11","H12","H13"]},"answerability_check":{"judgment":"lookup_or_memorization_dependent","discriminating_biological_argument":"Option A is eliminated because its positions (up to 1742) far exceed the 455-residue protein. Option C is eliminable by multi-pass transporter knowledge: a 455-aa membrane transporter with 10 other hydrophobic segments in MFS-like topology should have 11 TM segments, and the region 313-331 (TLIITTLVSFPIYISPIIL) sits between charged loop residues (K312, T332-E333-H334) consistent with a TM helix in a multi-pass transporter. However, the final distinction between B and D is a single-residue boundary: B has 138..157 while D has 137..157. Position 137 is L (KD=3.8) and 138 is I (KD=4.5); both are strongly hydrophobic. The preceding residue S(136) is only mildly polar (KD=-0.8). No general family rule, structural principle, or homolog comparison reliably determines whether a TM helix begins at L(137) or I(138). This single-residue boundary falls within the inherent uncertainty of all TM prediction methods and cannot be resolved by transferable knowledge of other proteins.","missing_item_specific_fact":"The exact UniProt annotation boundary specifying that TM helix 4 starts at residue 137 rather than 138. This is a computational annotation (ECO:0000255) specific to this entry's prediction algorithm output, not derivable from general hydrophobicity or family-level principles.","reason":"Options A and C can be eliminated by general reasoning (A: positions exceed protein length; C: missing a TM segment expected in a multi-pass transporter). However, the critical B vs D distinction is a single-residue difference at a TM helix boundary (137 vs 138), where both residues are strongly hydrophobic and the preceding 'polar' residue (Ser) is only mildly polar. No transferable biological principle or family-level knowledge meaningfully distinguishes these two one-residue-off boundaries. This requires the specific database annotation for this exact protein."},"question_ambiguity":{"multiple_defensible_options":["B","D"],"reason":"B and D differ only by whether the fourth TM segment starts at residue 137 (Leu) or 138 (Ile). Both are hydrophobic residues, and the preceding Ser(136) is only mildly polar. Standard hydrophobicity analysis, window-based TM prediction, and family-level TM topology knowledge cannot reliably resolve a single-residue boundary at this position. Both choices are defensible from sequence analysis alone."},"important_caveats":["All 11 TM annotations carry evidence code ECO:0000255 (by similarity), meaning they are computational predictions, not experimentally determined boundaries.","The annotations are from a Swiss-Prot entry first released in 2025; the underlying prediction algorithm and its boundary precision are not specified in the evidence.","The 137 vs 138 distinction is within the typical ±1-2 residue uncertainty of TM prediction tools, making it an annotation artifact rather than a biologically meaningful distinction."]}
```

</details>

## Complete reviewer-only evidence and qualifications

These source excerpts were available to the reviewers. They were not included in the original benchmark-solving input.

**Source applicability:**

```json
{
  "actual_author_source_snapshot": "unknown",
  "benchmark_sequence_length": 455,
  "benchmark_sequence_sha256": "6872668a1169d79c41e0e3217c7a0afaf399201ad1db1edc0cc760ca366b5635",
  "current_entry_audit": {
    "entryVersion": 109,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2003-03-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 455,
  "current_source_sequence_sha256": "6872668a1169d79c41e0e3217c7a0afaf399201ad1db1edc0cc760ca366b5635",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 107,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q8IIK1",
  "selected_historical_entry_version": 107,
  "selected_historical_record_sha256": "c315cecd25012a01e06e0aefb68dd205d1cf053c48966bc36b4c33d3c6385707",
  "selected_historical_source_sequence_length": 455,
  "selected_historical_source_sequence_sha256": "6872668a1169d79c41e0e3217c7a0afaf399201ad1db1edc0cc760ca366b5635",
  "selected_historical_version": {
    "accession": "Q8IIK1",
    "database": "Swiss-Prot",
    "entryVersion": 107,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "FT2_PLAF7",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIK1.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q8IIK1\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:24.989052+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IIK1.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIK1.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":109,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2003-03-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:24.989052+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IIK1.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIK1.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000001450\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Aconoidasida\",\"Haemosporida\",\"Plasmodiidae\",\"Plasmodium\",\"Laverania\"],\"scientificName\":\"Plasmodium falciparum (isolate 3D7)\",\"taxonId\":36329}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:24.989052+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IIK1.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIK1.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"21998306\",\"source\":\"PubMed\"}],\"value\":\"Folate transporter 2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"21998306\",\"source\":\"PubMed\"}],\"value\":\"PfFT2\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:24.989052+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IIK1.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIK1.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":64},\"start\":{\"modifier\":\"EXACT\",\"value\":42}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-01T06:25:24.989052+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IIK1.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIK1.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":103},\"start\":{\"modifier\":\"EXACT\",\"value\":84}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-01T06:25:24.989052+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IIK1.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIK1.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":131},\"start\":{\"modifier\":\"EXACT\",\"value\":110}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-01T06:25:24.989052+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IIK1.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIK1.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":157},\"start\":{\"modifier\":\"EXACT\",\"value\":137}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-01T06:25:24.989052+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IIK1.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIK1.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":195},\"start\":{\"modifier\":\"EXACT\",\"value\":177}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-01T06:25:24.989052+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IIK1.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIK1.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":221},\"start\":{\"modifier\":\"EXACT\",\"value\":201}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-01T06:25:24.989052+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IIK1.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIK1.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":261},\"start\":{\"modifier\":\"EXACT\",\"value\":242}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-01T06:25:24.989052+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IIK1.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIK1.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":301},\"start\":{\"modifier\":\"EXACT\",\"value\":281}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-01T06:25:24.989052+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IIK1.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIK1.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":331},\"start\":{\"modifier\":\"EXACT\",\"value\":313}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-01T06:25:24.989052+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IIK1.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIK1.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":367},\"start\":{\"modifier\":\"EXACT\",\"value\":347}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-01T06:25:24.989052+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IIK1.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIK1.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":438},\"start\":{\"modifier\":\"EXACT\",\"value\":417}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/11",
  "retrieved_utc": "2026-11-01T06:25:24.989052+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IIK1.json"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIK1.json)

```json
{
  "evidence_id": "C16",
  "excerpt": "{\"citation\":{\"authors\":[\"Salcedo-Sora J.E.\",\"Ochong E.\",\"Beveridge S.\",\"Johnson D.\",\"Nzila A.\",\"Biagini G.A.\",\"Stocks P.A.\",\"O'Neill P.M.\",\"Krishna S.\",\"Bray P.G.\",\"Ward S.A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"21998306\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m111.286054\"}],\"citationType\":\"journal article\",\"firstPage\":\"44659\",\"id\":\"21998306\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"44668\",\"publicationDate\":\"2011\",\"title\":\"The molecular basis of folate salvage in Plasmodium falciparum: characterization of two folate transporters.\",\"volume\":\"286\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"TRANSPORTER ACTIVITY\",\"ACTIVITY REGULATION\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:25:24.989052+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IIK1.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107)

```json
{
  "entry_version": 107,
  "evidence_id": "H1",
  "excerpt": "ID   FT2_PLAF7               Reviewed;         455 AA.\nAC   Q8IIK1;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAR-2003, sequence version 1.\nDT   28-JAN-2026, entry version 107.\nDE   RecName: Full=Folate transporter 2 {ECO:0000303|PubMed:21998306};\nDE            Short=PfFT2 {ECO:0000303|PubMed:21998306};\nGN   ORFNames=PF3D7_1116500 {ECO:0000312|EMBL:CZT98826.1};\nOS   Plasmodium falciparum (isolate 3D7).\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;\nOC   Plasmodiidae; Plasmodium; Plasmodium (Laverania).\nOX   NCBI_TaxID=36329 {ECO:0000312|Proteomes:UP000001450};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:40.005689+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c315cecd25012a01e06e0aefb68dd205d1cf053c48966bc36b4c33d3c6385707",
  "url": "https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107)

```json
{
  "entry_version": 107,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, TRANSPORTER ACTIVITY, ACTIVITY REGULATION, AND SUBCELLULAR\nRP   LOCATION.\nRX   PubMed=21998306; DOI=10.1074/jbc.m111.286054;\nRA   Salcedo-Sora J.E., Ochong E., Beveridge S., Johnson D., Nzila A.,\nRA   Biagini G.A., Stocks P.A., O'Neill P.M., Krishna S., Bray P.G., Ward S.A.;\nRT   \"The molecular basis of folate salvage in Plasmodium falciparum:\nRT   characterization of two folate transporters.\";\nRL   J. Biol. Chem. 286:44659-44668(2011).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:40.005689+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 27-35",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c315cecd25012a01e06e0aefb68dd205d1cf053c48966bc36b4c33d3c6385707",
  "url": "https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107)

```json
{
  "entry_version": 107,
  "evidence_id": "H3",
  "excerpt": "FT   TRANSMEM        42..64\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:40.005689+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 98-100",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c315cecd25012a01e06e0aefb68dd205d1cf053c48966bc36b4c33d3c6385707",
  "url": "https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107)

```json
{
  "entry_version": 107,
  "evidence_id": "H4",
  "excerpt": "FT   TRANSMEM        84..103\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:40.005689+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 101-103",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c315cecd25012a01e06e0aefb68dd205d1cf053c48966bc36b4c33d3c6385707",
  "url": "https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107)

```json
{
  "entry_version": 107,
  "evidence_id": "H5",
  "excerpt": "FT   TRANSMEM        110..131\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:40.005689+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 104-106",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c315cecd25012a01e06e0aefb68dd205d1cf053c48966bc36b4c33d3c6385707",
  "url": "https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107)

```json
{
  "entry_version": 107,
  "evidence_id": "H6",
  "excerpt": "FT   TRANSMEM        137..157\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:40.005689+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 107-109",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c315cecd25012a01e06e0aefb68dd205d1cf053c48966bc36b4c33d3c6385707",
  "url": "https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107)

```json
{
  "entry_version": 107,
  "evidence_id": "H7",
  "excerpt": "FT   TRANSMEM        177..195\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:40.005689+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 110-112",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c315cecd25012a01e06e0aefb68dd205d1cf053c48966bc36b4c33d3c6385707",
  "url": "https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107)

```json
{
  "entry_version": 107,
  "evidence_id": "H8",
  "excerpt": "FT   TRANSMEM        201..221\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:40.005689+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 113-115",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c315cecd25012a01e06e0aefb68dd205d1cf053c48966bc36b4c33d3c6385707",
  "url": "https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107)

```json
{
  "entry_version": 107,
  "evidence_id": "H9",
  "excerpt": "FT   TRANSMEM        242..261\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:40.005689+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 116-118",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c315cecd25012a01e06e0aefb68dd205d1cf053c48966bc36b4c33d3c6385707",
  "url": "https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107)

```json
{
  "entry_version": 107,
  "evidence_id": "H10",
  "excerpt": "FT   TRANSMEM        281..301\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:40.005689+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 119-121",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c315cecd25012a01e06e0aefb68dd205d1cf053c48966bc36b4c33d3c6385707",
  "url": "https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107)

```json
{
  "entry_version": 107,
  "evidence_id": "H11",
  "excerpt": "FT   TRANSMEM        313..331\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:40.005689+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 122-124",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c315cecd25012a01e06e0aefb68dd205d1cf053c48966bc36b4c33d3c6385707",
  "url": "https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107)

```json
{
  "entry_version": 107,
  "evidence_id": "H12",
  "excerpt": "FT   TRANSMEM        347..367\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:40.005689+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 125-127",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c315cecd25012a01e06e0aefb68dd205d1cf053c48966bc36b4c33d3c6385707",
  "url": "https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107)

```json
{
  "entry_version": 107,
  "evidence_id": "H13",
  "excerpt": "FT   TRANSMEM        417..438\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:40.005689+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 128-130",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c315cecd25012a01e06e0aefb68dd205d1cf053c48966bc36b4c33d3c6385707",
  "url": "https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 111. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
