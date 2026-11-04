# transmembrane_0075

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0075.txt)

**Task:** `transmembrane`  
**Expected answer:** **D** — 5..25; 81..101; 115..135; 151..171; 182..202; 229..249; 269..289; 305..325

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MPRPVSVVFVSLIIAAAVGVWGVFAWNGGFEELDAIVNRHPSTGIPGLNHFPSLDQGLMSMAAFNLPVVGREPLFAEGRHFMAQLLANVFAIPIVLLTEDFRAAPGSVARYSTSWGVFSQLATSAVMCPLYGVCFSRRSNPRRVAVLPGRSTWIVLISVLIGYGAPAMLIFDPFSWGLKPQIWGVLAFTVYPLYVCLTASLLLKTVSSKRGRASRSVQKDSDSNSSLHYVVAGIVGVAGHLSYIGFHLGEHTGTAATRPDRVAQLVLRFLQIDYVITFAAMLTLAWHELTHSGRISLKPWRVAGYLLLGWLFIGPGATLAAAWALRERWIRQDTQEEKKRKL

[Multiple Choices]
A. 27..47; 82..102; 109..129; 136..156; 173..193; 209..229; 333..353; 361..381; 395..415; 427..447; 460..480
B. 5..25; 81..101; 119..136; 151..171; 182..202; 229..249; 269..289; 305..325
C. 5..25; 81..101; 115..135; 151..171; 229..249; 269..289; 305..325
D. 5..25; 81..101; 115..135; 151..171; 182..202; 229..249; 269..289; 305..325
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

> The sequence-matched UniProt annotation lists the eight transmembrane segments in choice D. These annotations carry ECO:0000255, indicating computational evidence rather than direct experimental confirmation.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a series of strongly hydrophobic stretches of roughly membrane-spanning length, including the N-terminal segment and stretches around 81–101, 151–171, 182–202, 229–249, 269–289, and 305–325. The hydrophobicity and spacing make a multi-pass membrane-protein prediction credible and favor the eight-span patterns in B or D over C, which omits the strongly hydrophobic 182–202 stretch, and A, whose listed coordinates extend beyond the sequence.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable sequence and membrane-protein knowledge meaningfully narrows the choices and supports the multi-span prediction without requiring the exact protein record. However, sequence-based boundary prediction does not clearly distinguish the slightly shifted 119–136 segment in B from 115–135 in D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> B and D share the same predicted spans except for the boundary of one hydrophobic stretch: 119–136 versus 115–135. Both are plausible boundaries for a transmembrane helix, and the sequence alone does not establish the exact endpoints.


### Important caveats

- The supporting database annotations are computationally evidenced, not shown here to be experimentally validated.
- The evidence is sequence-matched, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a series of strongly hydrophobic stretches of roughly membrane-spanning length, including the N-terminal segment and stretches around 81–101, 151–171, 182–202, 229–249, 269–289, and 305–325. The hydrophobicity and spacing make a multi-pass membrane-protein prediction credible and favor the eight-span patterns in B or D over C, which omits the strongly hydrophobic 182–202 stretch, and A, whose listed coordinates extend beyond the sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable sequence and membrane-protein knowledge meaningfully narrows the choices and supports the multi-span prediction without requiring the exact protein record. However, sequence-based boundary prediction does not clearly distinguish the slightly shifted 119–136 segment in B from 115–135 in D."
  },
  "case_id": "transmembrane_0075",
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
    "reason": "The sequence-matched UniProt annotation lists the eight transmembrane segments in choice D. These annotations carry ECO:0000255, indicating computational evidence rather than direct experimental confirmation."
  },
  "important_caveats": [
    "The supporting database annotations are computationally evidenced, not shown here to be experimentally validated.",
    "The evidence is sequence-matched, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "B and D share the same predicted spans except for the boundary of one hydrophobic stretch: 119–136 versus 115–135. Both are plausible boundaries for a transmembrane helix, and the sequence alone does not establish the exact endpoints."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0075",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation lists the eight transmembrane segments in choice D. These annotations carry ECO:0000255, indicating computational evidence rather than direct experimental confirmation.",
    "evidence_ids": ["H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a series of strongly hydrophobic stretches of roughly membrane-spanning length, including the N-terminal segment and stretches around 81–101, 151–171, 182–202, 229–249, 269–289, and 305–325. The hydrophobicity and spacing make a multi-pass membrane-protein prediction credible and favor the eight-span patterns in B or D over C, which omits the strongly hydrophobic 182–202 stretch, and A, whose listed coordinates extend beyond the sequence.",
    "missing_item_specific_fact": "",
    "reason": "Transferable sequence and membrane-protein knowledge meaningfully narrows the choices and supports the multi-span prediction without requiring the exact protein record. However, sequence-based boundary prediction does not clearly distinguish the slightly shifted 119–136 segment in B from 115–135 in D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "B and D share the same predicted spans except for the boundary of one hydrophobic stretch: 119–136 versus 115–135. Both are plausible boundaries for a transmembrane helix, and the sequence alone does not establish the exact endpoints."
  },
  "important_caveats": [
    "The supporting database annotations are computationally evidenced, not shown here to be experimentally validated.",
    "The evidence is sequence-matched, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DXW0 (Terpene cyclase resF, Aspergillus sclerotiorum) annotates exactly 8 transmembrane helical regions: 5-25, 81-101, 115-135, 151-171, 182-202, 229-249, 269-289, 305-325. These match option D precisely. However, all eight annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions based on sequence similarity rather than experimentally validated boundaries. The sequence is confirmed as a 342-residue match to the benchmark input.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Option A is trivially eliminated because its listed positions (e.g., 333-353, 361-381, 395-415, 427-447, 460-480) exceed the 342-residue protein length. The remaining three options (B, C, D) differ only in subtle ways: B shifts the third TM boundary from 115-135 to 119-136 (a 4-residue N-terminal shift in a moderately hydrophobic region SWGVFSQLATSAVMCPLYGVC vs FSQLATSAVMCPLYGVCFS, with near-identical average hydropathy ~1.1-1.3); C omits the TM at 182-202 (QIWGVLAFTVYPLYVCLTASL, average hydropathy ~1.5, borderline for TM prediction). General hydrophobicity analysis, terpene-cyclase family knowledge, or multi-pass membrane protein topology principles cannot definitively resolve whether the third helix starts at residue 115 or 119, nor whether the moderately hydrophobic segment at 182-202 should be counted as a TM helix. These are computational similarity-based predictions (ECO:0000255) whose exact boundaries depend on the specific prediction algorithm and similarity template used, not on a transferable biological principle.


**Missing item-specific fact**

> The specific set of 8 TM regions with exact boundaries (particularly the inclusion of 182-202 and the precise N-terminal boundary at 115 rather than 119 for the third helix) as recorded in this protein's UniProt annotation. No general family-level rule or hydrophobicity threshold uniquely determines these boundaries among the offered choices.


**Reason**

> While a knowledgeable model can eliminate option A (positions exceed protein length) and can broadly identify hydrophobic stretches, the fine distinctions between options B, C, and D—whether a moderately hydrophobic 21-residue segment at 182-202 qualifies as TM, and whether the third helix boundary is 115-135 or 119-136—cannot be resolved by transferable knowledge of terpene cyclases, membrane protein families, or hydrophobicity principles. These boundaries are algorithm-specific computational predictions (ECO:0000255), and different prediction tools would plausibly produce slightly different boundaries. Distinguishing the correct option requires knowing this particular protein's recorded annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C",
  "D"
]
```

> Options B, C, and D all describe plausible sets of TM regions for this protein. B differs from D only by a 4-residue shift in one helix boundary (119-136 vs 115-135), and C differs by omitting one moderately hydrophobic TM region (182-202). Without the specific annotation, a careful hydrophobicity analysis could reasonably produce any of these three sets, making them all defensible from sequence alone.


### Important caveats

- All TM annotations are ECO:0000255 (inferred by similarity), i.e., computational predictions, not experimental measurements. Exact boundaries are algorithm-dependent.
- The protein is a terpene cyclase (EC 5.4.99.-) from Aspergillus sclerotiorum, but the specific TM topology for this particular cyclase is not a well-established family-level feature that would override the need for this protein's specific annotation.
- Option A is unambiguously wrong due to positions exceeding the 342-residue sequence length, providing one clear elimination but leaving three close alternatives.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Option A is trivially eliminated because its listed positions (e.g., 333-353, 361-381, 395-415, 427-447, 460-480) exceed the 342-residue protein length. The remaining three options (B, C, D) differ only in subtle ways: B shifts the third TM boundary from 115-135 to 119-136 (a 4-residue N-terminal shift in a moderately hydrophobic region SWGVFSQLATSAVMCPLYGVC vs FSQLATSAVMCPLYGVCFS, with near-identical average hydropathy ~1.1-1.3); C omits the TM at 182-202 (QIWGVLAFTVYPLYVCLTASL, average hydropathy ~1.5, borderline for TM prediction). General hydrophobicity analysis, terpene-cyclase family knowledge, or multi-pass membrane protein topology principles cannot definitively resolve whether the third helix starts at residue 115 or 119, nor whether the moderately hydrophobic segment at 182-202 should be counted as a TM helix. These are computational similarity-based predictions (ECO:0000255) whose exact boundaries depend on the specific prediction algorithm and similarity template used, not on a transferable biological principle.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific set of 8 TM regions with exact boundaries (particularly the inclusion of 182-202 and the precise N-terminal boundary at 115 rather than 119 for the third helix) as recorded in this protein's UniProt annotation. No general family-level rule or hydrophobicity threshold uniquely determines these boundaries among the offered choices.",
    "reason": "While a knowledgeable model can eliminate option A (positions exceed protein length) and can broadly identify hydrophobic stretches, the fine distinctions between options B, C, and D—whether a moderately hydrophobic 21-residue segment at 182-202 qualifies as TM, and whether the third helix boundary is 115-135 or 119-136—cannot be resolved by transferable knowledge of terpene cyclases, membrane protein families, or hydrophobicity principles. These boundaries are algorithm-specific computational predictions (ECO:0000255), and different prediction tools would plausibly produce slightly different boundaries. Distinguishing the correct option requires knowing this particular protein's recorded annotation."
  },
  "case_id": "transmembrane_0075",
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
    "reason": "The UniProt entry P0DXW0 (Terpene cyclase resF, Aspergillus sclerotiorum) annotates exactly 8 transmembrane helical regions: 5-25, 81-101, 115-135, 151-171, 182-202, 229-249, 269-289, 305-325. These match option D precisely. However, all eight annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions based on sequence similarity rather than experimentally validated boundaries. The sequence is confirmed as a 342-residue match to the benchmark input."
  },
  "important_caveats": [
    "All TM annotations are ECO:0000255 (inferred by similarity), i.e., computational predictions, not experimental measurements. Exact boundaries are algorithm-dependent.",
    "The protein is a terpene cyclase (EC 5.4.99.-) from Aspergillus sclerotiorum, but the specific TM topology for this particular cyclase is not a well-established family-level feature that would override the need for this protein's specific annotation.",
    "Option A is unambiguously wrong due to positions exceeding the 342-residue sequence length, providing one clear elimination but leaving three close alternatives."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C",
      "D"
    ],
    "reason": "Options B, C, and D all describe plausible sets of TM regions for this protein. B differs from D only by a 4-residue shift in one helix boundary (119-136 vs 115-135), and C differs by omitting one moderately hydrophobic TM region (182-202). Without the specific annotation, a careful hydrophobicity analysis could reasonably produce any of these three sets, making them all defensible from sequence alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{"case_id":"transmembrane_0075","expected_answer_check":{"judgment":"supported","reason":"The UniProt entry P0DXW0 (Terpene cyclase resF, Aspergillus sclerotiorum) annotates exactly 8 transmembrane helical regions: 5-25, 81-101, 115-135, 151-171, 182-202, 229-249, 269-289, 305-325. These match option D precisely. However, all eight annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions based on sequence similarity rather than experimentally validated boundaries. The sequence is confirmed as a 342-residue match to the benchmark input.","evidence_ids":["C5","C6","C7","C8","C9","C10","C11","C12","H3","H4","H5","H6","H7","H8","H9","H10"]},"answerability_check":{"judgment":"lookup_or_memorization_dependent","discriminating_biological_argument":"Option A is trivially eliminated because its listed positions (e.g., 333-353, 361-381, 395-415, 427-447, 460-480) exceed the 342-residue protein length. The remaining three options (B, C, D) differ only in subtle ways: B shifts the third TM boundary from 115-135 to 119-136 (a 4-residue N-terminal shift in a moderately hydrophobic region SWGVFSQLATSAVMCPLYGVC vs FSQLATSAVMCPLYGVCFS, with near-identical average hydropathy ~1.1-1.3); C omits the TM at 182-202 (QIWGVLAFTVYPLYVCLTASL, average hydropathy ~1.5, borderline for TM prediction). General hydrophobicity analysis, terpene-cyclase family knowledge, or multi-pass membrane protein topology principles cannot definitively resolve whether the third helix starts at residue 115 or 119, nor whether the moderately hydrophobic segment at 182-202 should be counted as a TM helix. These are computational similarity-based predictions (ECO:0000255) whose exact boundaries depend on the specific prediction algorithm and similarity template used, not on a transferable biological principle.","missing_item_specific_fact":"The specific set of 8 TM regions with exact boundaries (particularly the inclusion of 182-202 and the precise N-terminal boundary at 115 rather than 119 for the third helix) as recorded in this protein's UniProt annotation. No general family-level rule or hydrophobicity threshold uniquely determines these boundaries among the offered choices.","reason":"While a knowledgeable model can eliminate option A (positions exceed protein length) and can broadly identify hydrophobic stretches, the fine distinctions between options B, C, and D—whether a moderately hydrophobic 21-residue segment at 182-202 qualifies as TM, and whether the third helix boundary is 115-135 or 119-136—cannot be resolved by transferable knowledge of terpene cyclases, membrane protein families, or hydrophobicity principles. These boundaries are algorithm-specific computational predictions (ECO:0000255), and different prediction tools would plausibly produce slightly different boundaries. Distinguishing the correct option requires knowing this particular protein's recorded annotation."},"question_ambiguity":{"multiple_defensible_options":["B","C","D"],"reason":"Options B, C, and D all describe plausible sets of TM regions for this protein. B differs from D only by a 4-residue shift in one helix boundary (119-136 vs 115-135), and C differs by omitting one moderately hydrophobic TM region (182-202). Without the specific annotation, a careful hydrophobicity analysis could reasonably produce any of these three sets, making them all defensible from sequence alone."},"important_caveats":["All TM annotations are ECO:0000255 (inferred by similarity), i.e., computational predictions, not experimental measurements. Exact boundaries are algorithm-dependent.","The protein is a terpene cyclase (EC 5.4.99.-) from Aspergillus sclerotiorum, but the specific TM topology for this particular cyclase is not a well-established family-level feature that would override the need for this protein's specific annotation.","Option A is unambiguously wrong due to positions exceeding the 342-residue sequence length, providing one clear elimination but leaving three close alternatives."]}
```

</details>

## Complete reviewer-only evidence and qualifications

These source excerpts were available to the reviewers. They were not included in the original benchmark-solving input.

**Source applicability:**

```json
{
  "actual_author_source_snapshot": "unknown",
  "benchmark_sequence_length": 342,
  "benchmark_sequence_sha256": "ed325be2f8ee79598c0abcb873dca733c54a3c7abec00f6bf398603cd44c5b21",
  "current_entry_audit": {
    "entryVersion": 4,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-02-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "20826975e15383c7e7ed9a18e9833743bdc1e763a65798dcc5e4dbb145fcc991",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 342,
  "current_source_sequence_sha256": "ed325be2f8ee79598c0abcb873dca733c54a3c7abec00f6bf398603cd44c5b21",
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
  "requested_accession": "P0DXW0",
  "selected_historical_entry_version": 2,
  "selected_historical_record_sha256": "4ee0148ff929a45fee99461aa9272fe9ea0eed8e9ecc9ee53739e76044ec61c4",
  "selected_historical_source_sequence_length": 342,
  "selected_historical_source_sequence_sha256": "ed325be2f8ee79598c0abcb873dca733c54a3c7abec00f6bf398603cd44c5b21",
  "selected_historical_version": {
    "accession": "P0DXW0",
    "database": "Swiss-Prot",
    "entryVersion": 2,
    "firstRelease": "2025_02/2025_02",
    "firstReleaseDate": "23-Apr-2025",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "RESF_ASPSL",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW0.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DXW0\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:29:50.537709+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "20826975e15383c7e7ed9a18e9833743bdc1e763a65798dcc5e4dbb145fcc991",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXW0.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW0.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":4,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-02-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:29:50.537709+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "20826975e15383c7e7ed9a18e9833743bdc1e763a65798dcc5e4dbb145fcc991",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXW0.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW0.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Aspergillus\",\"Circumdati\"],\"scientificName\":\"Aspergillus sclerotiorum\",\"taxonId\":138282}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:29:50.537709+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "20826975e15383c7e7ed9a18e9833743bdc1e763a65798dcc5e4dbb145fcc991",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXW0.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW0.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39105744\",\"source\":\"PubMed\"}],\"value\":\"Restricticin biosynthesis cluster protein F\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"39105744\",\"source\":\"PubMed\"}],\"value\":\"5.4.99.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39105744\",\"source\":\"PubMed\"}],\"value\":\"Terpene cyclase resF\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:29:50.537709+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "20826975e15383c7e7ed9a18e9833743bdc1e763a65798dcc5e4dbb145fcc991",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXW0.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW0.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":25},\"start\":{\"modifier\":\"EXACT\",\"value\":5}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:29:50.537709+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "20826975e15383c7e7ed9a18e9833743bdc1e763a65798dcc5e4dbb145fcc991",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXW0.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW0.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":101},\"start\":{\"modifier\":\"EXACT\",\"value\":81}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:29:50.537709+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "20826975e15383c7e7ed9a18e9833743bdc1e763a65798dcc5e4dbb145fcc991",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXW0.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW0.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":135},\"start\":{\"modifier\":\"EXACT\",\"value\":115}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:29:50.537709+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "20826975e15383c7e7ed9a18e9833743bdc1e763a65798dcc5e4dbb145fcc991",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXW0.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW0.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":171},\"start\":{\"modifier\":\"EXACT\",\"value\":151}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:29:50.537709+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "20826975e15383c7e7ed9a18e9833743bdc1e763a65798dcc5e4dbb145fcc991",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXW0.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW0.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":202},\"start\":{\"modifier\":\"EXACT\",\"value\":182}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:29:50.537709+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "20826975e15383c7e7ed9a18e9833743bdc1e763a65798dcc5e4dbb145fcc991",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXW0.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW0.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":249},\"start\":{\"modifier\":\"EXACT\",\"value\":229}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:29:50.537709+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "20826975e15383c7e7ed9a18e9833743bdc1e763a65798dcc5e4dbb145fcc991",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXW0.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW0.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":289},\"start\":{\"modifier\":\"EXACT\",\"value\":269}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:29:50.537709+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "20826975e15383c7e7ed9a18e9833743bdc1e763a65798dcc5e4dbb145fcc991",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXW0.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW0.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":325},\"start\":{\"modifier\":\"EXACT\",\"value\":305}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:29:50.537709+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "20826975e15383c7e7ed9a18e9833743bdc1e763a65798dcc5e4dbb145fcc991",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXW0.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW0.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"citation\":{\"authors\":[\"Lu Y.\",\"Li Y.\",\"Dou M.\",\"Liu D.\",\"Lin W.\",\"Fan A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39105744\"},{\"database\":\"DOI\",\"id\":\"10.1021/acs.jafc.4c04244\"}],\"citationType\":\"journal article\",\"firstPage\":\"18520\",\"id\":\"39105744\",\"journal\":\"J. Agric. Food Chem.\",\"lastPage\":\"18527\",\"publicationDate\":\"2024\",\"title\":\"Discovery of a hybrid molecule with phytotoxic activity by genome mining, heterologous expression, and OSMAC strategy.\",\"volume\":\"72\"},\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:29:50.537709+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "20826975e15383c7e7ed9a18e9833743bdc1e763a65798dcc5e4dbb145fcc991",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXW0.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW0?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H1",
  "excerpt": "ID   RESF_ASPSL              Reviewed;         342 AA.\nAC   P0DXW0;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-FEB-2025, sequence version 1.\nDT   09-APR-2025, entry version 2.\nDE   RecName: Full=Terpene cyclase resF {ECO:0000303|PubMed:39105744};\nDE            EC=5.4.99.- {ECO:0000305|PubMed:39105744};\nDE   AltName: Full=Restricticin biosynthesis cluster protein F {ECO:0000303|PubMed:39105744};\nGN   Name=resF {ECO:0000303|PubMed:39105744};\nOS   Aspergillus sclerotiorum.\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;\nOC   Aspergillus subgen. Circumdati.\nOX   NCBI_TaxID=138282;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:54.246056+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4ee0148ff929a45fee99461aa9272fe9ea0eed8e9ecc9ee53739e76044ec61c4",
  "url": "https://rest.uniprot.org/unisave/P0DXW0?format=txt&versions=2"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW0?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H2",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, AND PATHWAY.\nRX   PubMed=39105744; DOI=10.1021/acs.jafc.4c04244;\nRA   Lu Y., Li Y., Dou M., Liu D., Lin W., Fan A.;\nRT   \"Discovery of a hybrid molecule with phytotoxic activity by genome mining,\nRT   heterologous expression, and OSMAC strategy.\";\nRL   J. Agric. Food Chem. 72:18520-18527(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:54.246056+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 15-21",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4ee0148ff929a45fee99461aa9272fe9ea0eed8e9ecc9ee53739e76044ec61c4",
  "url": "https://rest.uniprot.org/unisave/P0DXW0?format=txt&versions=2"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW0?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H3",
  "excerpt": "FT   TRANSMEM        5..25\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:54.246056+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 53-55",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4ee0148ff929a45fee99461aa9272fe9ea0eed8e9ecc9ee53739e76044ec61c4",
  "url": "https://rest.uniprot.org/unisave/P0DXW0?format=txt&versions=2"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW0?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H4",
  "excerpt": "FT   TRANSMEM        81..101\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:54.246056+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 56-58",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4ee0148ff929a45fee99461aa9272fe9ea0eed8e9ecc9ee53739e76044ec61c4",
  "url": "https://rest.uniprot.org/unisave/P0DXW0?format=txt&versions=2"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW0?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H5",
  "excerpt": "FT   TRANSMEM        115..135\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:54.246056+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 59-61",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4ee0148ff929a45fee99461aa9272fe9ea0eed8e9ecc9ee53739e76044ec61c4",
  "url": "https://rest.uniprot.org/unisave/P0DXW0?format=txt&versions=2"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW0?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H6",
  "excerpt": "FT   TRANSMEM        151..171\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:54.246056+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 62-64",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4ee0148ff929a45fee99461aa9272fe9ea0eed8e9ecc9ee53739e76044ec61c4",
  "url": "https://rest.uniprot.org/unisave/P0DXW0?format=txt&versions=2"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW0?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H7",
  "excerpt": "FT   TRANSMEM        182..202\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:54.246056+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 65-67",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4ee0148ff929a45fee99461aa9272fe9ea0eed8e9ecc9ee53739e76044ec61c4",
  "url": "https://rest.uniprot.org/unisave/P0DXW0?format=txt&versions=2"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW0?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H8",
  "excerpt": "FT   TRANSMEM        229..249\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:54.246056+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 68-70",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4ee0148ff929a45fee99461aa9272fe9ea0eed8e9ecc9ee53739e76044ec61c4",
  "url": "https://rest.uniprot.org/unisave/P0DXW0?format=txt&versions=2"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW0?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H9",
  "excerpt": "FT   TRANSMEM        269..289\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:54.246056+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 71-73",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4ee0148ff929a45fee99461aa9272fe9ea0eed8e9ecc9ee53739e76044ec61c4",
  "url": "https://rest.uniprot.org/unisave/P0DXW0?format=txt&versions=2"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW0?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H10",
  "excerpt": "FT   TRANSMEM        305..325\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:54.246056+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 74-76",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4ee0148ff929a45fee99461aa9272fe9ea0eed8e9ecc9ee53739e76044ec61c4",
  "url": "https://rest.uniprot.org/unisave/P0DXW0?format=txt&versions=2"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 75. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
