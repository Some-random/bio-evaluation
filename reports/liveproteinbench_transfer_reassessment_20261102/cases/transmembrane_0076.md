# transmembrane_0076

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0076.txt)

**Task:** `transmembrane`  
**Expected answer:** **C** — 5..25; 72..92; 111..131; 149..169; 177..197; 222..242; 267..287; 298..318

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MLHSASVIFLSLSVLAAVGVWGPFVRDGGFDAMDAVVARHPSTGIPGLQHYPEFDRGLMSIVAFNLSAVNSIAYCFMMQFLANVAVIPVILCTEDSSAAPGSWVRYSTIWGLLSQLGTSAVIYPLYAMSFIRQSSREPSQTRQPMSDMALILNMAMGYALPAAITLNVLHSSLNMQIWGILAFTVYPICMKLMARIIKVFTGFRKFPTRSRHQSIPTLRYAVAGGVALQGHLWYLGTELGIFKGHTPSLSAEKMDSEGGARLVLRFLQVDYAITFLAMLLLAWHELIYHRILPAWRALGGLIIGWILVGPGATLAAAWYLRSRFIMAPGKRKKRYGD

[Multiple Choices]
A. 5..25; 72..92; 111..131; 151..170; 177..197; 222..242; 267..287; 298..318
B. 227..249
C. 5..25; 72..92; 111..131; 149..169; 177..197; 222..242; 267..287; 298..318
D. 72..92; 111..131; 149..169; 177..197; 222..242; 267..287; 298..318
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

> The sequence-matched UniProt annotation lists the eight transmembrane segments in choice C. These annotations carry computational evidence code ECO:0000255, so they support the key as database predictions, not as direct experimental measurements.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains multiple strongly hydrophobic stretches consistent with the listed transmembrane helices, which can distinguish the multi-helix choices from B and the omitted-helix choice D. But the sequence and transferable knowledge do not reliably distinguish A from C: their only difference is a small shift in the boundaries of one hydrophobic stretch.


**Missing item-specific fact**

> The exact predicted boundary annotation for that helix (149..169 versus 151..170) is needed to select between A and C.


**Reason**

> General sequence-based reasoning supports the overall multi-pass topology, but the choices require an exact boundary that is not uniquely determined by the supplied sequence. Selecting the keyed alternative requires the target-specific boundary annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> A and C differ only by a small boundary shift for one otherwise strongly hydrophobic segment. Both are plausible transmembrane spans from the sequence; the question supplies no boundary convention that resolves the difference.


### Important caveats

- The supporting database annotation is computational, not direct experimental evidence.
- A transmembrane helix's exact boundary can be approximate; this supports the existence of the segment more strongly than the precise residue endpoints.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple strongly hydrophobic stretches consistent with the listed transmembrane helices, which can distinguish the multi-helix choices from B and the omitted-helix choice D. But the sequence and transferable knowledge do not reliably distinguish A from C: their only difference is a small shift in the boundaries of one hydrophobic stretch.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact predicted boundary annotation for that helix (149..169 versus 151..170) is needed to select between A and C.",
    "reason": "General sequence-based reasoning supports the overall multi-pass topology, but the choices require an exact boundary that is not uniquely determined by the supplied sequence. Selecting the keyed alternative requires the target-specific boundary annotation."
  },
  "case_id": "transmembrane_0076",
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
    "reason": "The sequence-matched UniProt annotation lists the eight transmembrane segments in choice C. These annotations carry computational evidence code ECO:0000255, so they support the key as database predictions, not as direct experimental measurements."
  },
  "important_caveats": [
    "The supporting database annotation is computational, not direct experimental evidence.",
    "A transmembrane helix's exact boundary can be approximate; this supports the existence of the segment more strongly than the precise residue endpoints."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "A and C differ only by a small boundary shift for one otherwise strongly hydrophobic segment. Both are plausible transmembrane spans from the sequence; the question supplies no boundary convention that resolves the difference."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0076",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation lists the eight transmembrane segments in choice C. These annotations carry computational evidence code ECO:0000255, so they support the key as database predictions, not as direct experimental measurements.",
    "evidence_ids": ["H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains multiple strongly hydrophobic stretches consistent with the listed transmembrane helices, which can distinguish the multi-helix choices from B and the omitted-helix choice D. But the sequence and transferable knowledge do not reliably distinguish A from C: their only difference is a small shift in the boundaries of one hydrophobic stretch.",
    "missing_item_specific_fact": "The exact predicted boundary annotation for that helix (149..169 versus 151..170) is needed to select between A and C.",
    "reason": "General sequence-based reasoning supports the overall multi-pass topology, but the choices require an exact boundary that is not uniquely determined by the supplied sequence. Selecting the keyed alternative requires the target-specific boundary annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "A and C differ only by a small boundary shift for one otherwise strongly hydrophobic segment. Both are plausible transmembrane spans from the sequence; the question supplies no boundary convention that resolves the difference."
  },
  "important_caveats": [
    "The supporting database annotation is computational, not direct experimental evidence.",
    "A transmembrane helix's exact boundary can be approximate; this supports the existence of the segment more strongly than the precise residue endpoints."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DXW1 annotates exactly eight transmembrane helical regions at 5..25, 72..92, 111..131, 149..169, 177..197, 222..242, 267..287, and 298..318 (evidence C5-C12, H3-H10), matching choice C precisely. All annotations carry evidence code ECO:0000255 (inferred by similarity), indicating computational prediction rather than experimental determination. The sequence match is confirmed (SHA-256 match, 337 AA).

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Choice B (single 23-residue segment) is eliminated because a multi-pass membrane protein requires multiple TM helices. Choice D omits the N-terminal 5..25 region (ASVIFLSLSVLAAVGVWGPF), which is strongly hydrophobic (rich in L, V, A, I) and consistent with a signal peptide or TM helix in membrane-associated terpene cyclases; excluding it contradicts basic hydropathy analysis. The critical distinction between A (151..170) and C (149..169) rests on a 2-residue shift. Residues 149(L) and 150(I) are strongly hydrophobic (hydropathy +3.8 and +4.5), while residue 170(S) is polar (hydropathy -0.8). A standard hydropathy-window analysis of this 21-residue segment therefore favors the window 149..169, which captures two additional hydrophobic residues at the N-terminus and excludes a polar serine at the C-terminus. This is a transferable principle of TM helix boundary assignment: maximize hydrophobic content within the predicted helix. The presence of a helix-breaking proline at position 160 within both windows does not change the relative ranking.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can eliminate B (too few helices) and D (missing obvious N-terminal hydrophobic TM) by general principles. The A-vs-C distinction, while subtle (2-residue shift), is addressable by hydropathy analysis: including L(149)+I(150) and excluding S(170) yields a more hydrophobic window, consistent with standard TM prediction methodology. This is a legitimate transferable inference, though the margin is small and within typical prediction-tool uncertainty.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> The difference between A and C is a 2-residue shift (151..170 vs 149..169). While hydropathy analysis mildly favors C, the margin is small and both windows contain a helix-breaking proline at position 160 and several polar residues. Different TM prediction tools or different windowing strategies could plausibly yield either boundary. The distinction is defensible but not decisive.


### Important caveats

- All eight TM annotations carry ECO:0000255 (inferred by similarity), meaning they are computational predictions based on homology, not experimental measurements. The exact boundaries depend on the prediction method and template used.
- The A-vs-C distinction (2-residue shift at the fourth TM) is within the typical uncertainty of sequence-based TM predictors. The hydropathy argument is valid but marginal.
- The protein is annotated as a terpene cyclase (EC 5.4.99.-) from Pyrenophora dematioidea involved in lanomycin biosynthesis; its membrane association and exact topology are inferred rather than experimentally confirmed.
- The UniProt entry was first public in February 2025; the author's source snapshot is unknown but the sequence matches the current and historical (entry version 2) records.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Choice B (single 23-residue segment) is eliminated because a multi-pass membrane protein requires multiple TM helices. Choice D omits the N-terminal 5..25 region (ASVIFLSLSVLAAVGVWGPF), which is strongly hydrophobic (rich in L, V, A, I) and consistent with a signal peptide or TM helix in membrane-associated terpene cyclases; excluding it contradicts basic hydropathy analysis. The critical distinction between A (151..170) and C (149..169) rests on a 2-residue shift. Residues 149(L) and 150(I) are strongly hydrophobic (hydropathy +3.8 and +4.5), while residue 170(S) is polar (hydropathy -0.8). A standard hydropathy-window analysis of this 21-residue segment therefore favors the window 149..169, which captures two additional hydrophobic residues at the N-terminus and excludes a polar serine at the C-terminus. This is a transferable principle of TM helix boundary assignment: maximize hydrophobic content within the predicted helix. The presence of a helix-breaking proline at position 160 within both windows does not change the relative ranking.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate B (too few helices) and D (missing obvious N-terminal hydrophobic TM) by general principles. The A-vs-C distinction, while subtle (2-residue shift), is addressable by hydropathy analysis: including L(149)+I(150) and excluding S(170) yields a more hydrophobic window, consistent with standard TM prediction methodology. This is a legitimate transferable inference, though the margin is small and within typical prediction-tool uncertainty."
  },
  "case_id": "transmembrane_0076",
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
    "reason": "The UniProt entry P0DXW1 annotates exactly eight transmembrane helical regions at 5..25, 72..92, 111..131, 149..169, 177..197, 222..242, 267..287, and 298..318 (evidence C5-C12, H3-H10), matching choice C precisely. All annotations carry evidence code ECO:0000255 (inferred by similarity), indicating computational prediction rather than experimental determination. The sequence match is confirmed (SHA-256 match, 337 AA)."
  },
  "important_caveats": [
    "All eight TM annotations carry ECO:0000255 (inferred by similarity), meaning they are computational predictions based on homology, not experimental measurements. The exact boundaries depend on the prediction method and template used.",
    "The A-vs-C distinction (2-residue shift at the fourth TM) is within the typical uncertainty of sequence-based TM predictors. The hydropathy argument is valid but marginal.",
    "The protein is annotated as a terpene cyclase (EC 5.4.99.-) from Pyrenophora dematioidea involved in lanomycin biosynthesis; its membrane association and exact topology are inferred rather than experimentally confirmed.",
    "The UniProt entry was first public in February 2025; the author's source snapshot is unknown but the sequence matches the current and historical (entry version 2) records."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "The difference between A and C is a 2-residue shift (151..170 vs 149..169). While hydropathy analysis mildly favors C, the margin is small and both windows contain a helix-breaking proline at position 160 and several polar residues. Different TM prediction tools or different windowing strategies could plausibly yield either boundary. The distinction is defensible but not decisive."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0076",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DXW1 annotates exactly eight transmembrane helical regions at 5..25, 72..92, 111..131, 149..169, 177..197, 222..242, 267..287, and 298..318 (evidence C5-C12, H3-H10), matching choice C precisely. All annotations carry evidence code ECO:0000255 (inferred by similarity), indicating computational prediction rather than experimental determination. The sequence match is confirmed (SHA-256 match, 337 AA).",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Choice B (single 23-residue segment) is eliminated because a multi-pass membrane protein requires multiple TM helices. Choice D omits the N-terminal 5..25 region (ASVIFLSLSVLAAVGVWGPF), which is strongly hydrophobic (rich in L, V, A, I) and consistent with a signal peptide or TM helix in membrane-associated terpene cyclases; excluding it contradicts basic hydropathy analysis. The critical distinction between A (151..170) and C (149..169) rests on a 2-residue shift. Residues 149(L) and 150(I) are strongly hydrophobic (hydropathy +3.8 and +4.5), while residue 170(S) is polar (hydropathy -0.8). A standard hydropathy-window analysis of this 21-residue segment therefore favors the window 149..169, which captures two additional hydrophobic residues at the N-terminus and excludes a polar serine at the C-terminus. This is a transferable principle of TM helix boundary assignment: maximize hydrophobic content within the predicted helix. The presence of a helix-breaking proline at position 160 within both windows does not change the relative ranking.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate B (too few helices) and D (missing obvious N-terminal hydrophobic TM) by general principles. The A-vs-C distinction, while subtle (2-residue shift), is addressable by hydropathy analysis: including L(149)+I(150) and excluding S(170) yields a more hydrophobic window, consistent with standard TM prediction methodology. This is a legitimate transferable inference, though the margin is small and within typical prediction-tool uncertainty."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "The difference between A and C is a 2-residue shift (151..170 vs 149..169). While hydropathy analysis mildly favors C, the margin is small and both windows contain a helix-breaking proline at position 160 and several polar residues. Different TM prediction tools or different windowing strategies could plausibly yield either boundary. The distinction is defensible but not decisive."
  },
  "important_caveats": [
    "All eight TM annotations carry ECO:0000255 (inferred by similarity), meaning they are computational predictions based on homology, not experimental measurements. The exact boundaries depend on the prediction method and template used.",
    "The A-vs-C distinction (2-residue shift at the fourth TM) is within the typical uncertainty of sequence-based TM predictors. The hydropathy argument is valid but marginal.",
    "The protein is annotated as a terpene cyclase (EC 5.4.99.-) from Pyrenophora dematioidea involved in lanomycin biosynthesis; its membrane association and exact topology are inferred rather than experimentally confirmed.",
    "The UniProt entry was first public in February 2025; the author's source snapshot is unknown but the sequence matches the current and historical (entry version 2) records."
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
  "benchmark_sequence_length": 337,
  "benchmark_sequence_sha256": "03195f3332d36bdd5e7387b1e3471a7b977448073f58c36a12eb518fcb748430",
  "current_entry_audit": {
    "entryVersion": 4,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-02-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "3f2ff3dca517c7cada001b0d9e2f2388aebcbab4f14d2d2a9a551d33f51517e8",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 337,
  "current_source_sequence_sha256": "03195f3332d36bdd5e7387b1e3471a7b977448073f58c36a12eb518fcb748430",
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
  "requested_accession": "P0DXW1",
  "selected_historical_entry_version": 2,
  "selected_historical_record_sha256": "db1acbf2ac66c5648de96f9c489a7a4f13b2cb19c91ff902f8cef92abf8b0704",
  "selected_historical_source_sequence_length": 337,
  "selected_historical_source_sequence_sha256": "03195f3332d36bdd5e7387b1e3471a7b977448073f58c36a12eb518fcb748430",
  "selected_historical_version": {
    "accession": "P0DXW1",
    "database": "Swiss-Prot",
    "entryVersion": 2,
    "firstRelease": "2025_02/2025_02",
    "firstReleaseDate": "23-Apr-2025",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "LAN5_PYRDE",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW1.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DXW1\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:16.733133+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3f2ff3dca517c7cada001b0d9e2f2388aebcbab4f14d2d2a9a551d33f51517e8",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXW1.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW1.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":4,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-02-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:16.733133+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3f2ff3dca517c7cada001b0d9e2f2388aebcbab4f14d2d2a9a551d33f51517e8",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXW1.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW1.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Helminthosporium dematioideum\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Dothideomycetes\",\"Pleosporomycetidae\",\"Pleosporales\",\"Pleosporineae\",\"Pleosporaceae\",\"Pyrenophora\"],\"scientificName\":\"Pyrenophora dematioidea\",\"taxonId\":139229}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:16.733133+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3f2ff3dca517c7cada001b0d9e2f2388aebcbab4f14d2d2a9a551d33f51517e8",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXW1.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW1.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33857369\",\"source\":\"PubMed\"}],\"value\":\"Lanomycin biosynthesis cluster protein 5\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"33857369\",\"source\":\"PubMed\"}],\"value\":\"5.4.99.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33857369\",\"source\":\"PubMed\"}],\"value\":\"Terpene cyclase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:16.733133+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3f2ff3dca517c7cada001b0d9e2f2388aebcbab4f14d2d2a9a551d33f51517e8",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXW1.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW1.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":25},\"start\":{\"modifier\":\"EXACT\",\"value\":5}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-01T06:25:16.733133+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3f2ff3dca517c7cada001b0d9e2f2388aebcbab4f14d2d2a9a551d33f51517e8",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXW1.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW1.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":92},\"start\":{\"modifier\":\"EXACT\",\"value\":72}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-01T06:25:16.733133+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3f2ff3dca517c7cada001b0d9e2f2388aebcbab4f14d2d2a9a551d33f51517e8",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXW1.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW1.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":131},\"start\":{\"modifier\":\"EXACT\",\"value\":111}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-01T06:25:16.733133+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3f2ff3dca517c7cada001b0d9e2f2388aebcbab4f14d2d2a9a551d33f51517e8",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXW1.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW1.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":169},\"start\":{\"modifier\":\"EXACT\",\"value\":149}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-01T06:25:16.733133+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3f2ff3dca517c7cada001b0d9e2f2388aebcbab4f14d2d2a9a551d33f51517e8",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXW1.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW1.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":197},\"start\":{\"modifier\":\"EXACT\",\"value\":177}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-01T06:25:16.733133+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3f2ff3dca517c7cada001b0d9e2f2388aebcbab4f14d2d2a9a551d33f51517e8",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXW1.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW1.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":242},\"start\":{\"modifier\":\"EXACT\",\"value\":222}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-01T06:25:16.733133+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3f2ff3dca517c7cada001b0d9e2f2388aebcbab4f14d2d2a9a551d33f51517e8",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXW1.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW1.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":287},\"start\":{\"modifier\":\"EXACT\",\"value\":267}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-01T06:25:16.733133+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3f2ff3dca517c7cada001b0d9e2f2388aebcbab4f14d2d2a9a551d33f51517e8",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXW1.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW1.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":318},\"start\":{\"modifier\":\"EXACT\",\"value\":298}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-01T06:25:16.733133+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3f2ff3dca517c7cada001b0d9e2f2388aebcbab4f14d2d2a9a551d33f51517e8",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXW1.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW1.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"citation\":{\"authors\":[\"Liu N.\",\"Abramyan E.D.\",\"Cheng W.\",\"Perlatti B.\",\"Harvey C.J.B.\",\"Bills G.F.\",\"Tang Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33857369\"},{\"database\":\"DOI\",\"id\":\"10.1021/jacs.1c01516\"}],\"citationType\":\"journal article\",\"firstPage\":\"6043\",\"id\":\"33857369\",\"journal\":\"J. Am. Chem. Soc.\",\"lastPage\":\"6047\",\"publicationDate\":\"2021\",\"title\":\"Targeted genome mining reveals the biosynthetic gene clusters of natural product CYP51 inhibitors.\",\"volume\":\"143\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"TTI-1096\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:25:16.733133+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3f2ff3dca517c7cada001b0d9e2f2388aebcbab4f14d2d2a9a551d33f51517e8",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXW1.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW1?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H1",
  "excerpt": "ID   LAN5_PYRDE              Reviewed;         337 AA.\nAC   P0DXW1;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-FEB-2025, sequence version 1.\nDT   09-APR-2025, entry version 2.\nDE   RecName: Full=Terpene cyclase {ECO:0000303|PubMed:33857369};\nDE            EC=5.4.99.- {ECO:0000305|PubMed:33857369};\nDE   AltName: Full=Lanomycin biosynthesis cluster protein 5 {ECO:0000303|PubMed:33857369};\nGN   Name=ORF5 {ECO:0000303|PubMed:33857369};\nOS   Pyrenophora dematioidea (Helminthosporium dematioideum).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Dothideomycetes;\nOC   Pleosporomycetidae; Pleosporales; Pleosporineae; Pleosporaceae;\nOC   Pyrenophora.\nOX   NCBI_TaxID=139229;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:24.266216+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "db1acbf2ac66c5648de96f9c489a7a4f13b2cb19c91ff902f8cef92abf8b0704",
  "url": "https://rest.uniprot.org/unisave/P0DXW1?format=txt&versions=2"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW1?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H2",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, AND PATHWAY.\nRC   STRAIN=TTI-1096;\nRX   PubMed=33857369; DOI=10.1021/jacs.1c01516;\nRA   Liu N., Abramyan E.D., Cheng W., Perlatti B., Harvey C.J.B., Bills G.F.,\nRA   Tang Y.;\nRT   \"Targeted genome mining reveals the biosynthetic gene clusters of natural\nRT   product CYP51 inhibitors.\";\nRL   J. Am. Chem. Soc. 143:6043-6047(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:24.266216+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 15-23",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "db1acbf2ac66c5648de96f9c489a7a4f13b2cb19c91ff902f8cef92abf8b0704",
  "url": "https://rest.uniprot.org/unisave/P0DXW1?format=txt&versions=2"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW1?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H3",
  "excerpt": "FT   TRANSMEM        5..25\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:24.266216+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 51-53",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "db1acbf2ac66c5648de96f9c489a7a4f13b2cb19c91ff902f8cef92abf8b0704",
  "url": "https://rest.uniprot.org/unisave/P0DXW1?format=txt&versions=2"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW1?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H4",
  "excerpt": "FT   TRANSMEM        72..92\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:24.266216+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 54-56",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "db1acbf2ac66c5648de96f9c489a7a4f13b2cb19c91ff902f8cef92abf8b0704",
  "url": "https://rest.uniprot.org/unisave/P0DXW1?format=txt&versions=2"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW1?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H5",
  "excerpt": "FT   TRANSMEM        111..131\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:24.266216+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 57-59",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "db1acbf2ac66c5648de96f9c489a7a4f13b2cb19c91ff902f8cef92abf8b0704",
  "url": "https://rest.uniprot.org/unisave/P0DXW1?format=txt&versions=2"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW1?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H6",
  "excerpt": "FT   TRANSMEM        149..169\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:24.266216+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 60-62",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "db1acbf2ac66c5648de96f9c489a7a4f13b2cb19c91ff902f8cef92abf8b0704",
  "url": "https://rest.uniprot.org/unisave/P0DXW1?format=txt&versions=2"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW1?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H7",
  "excerpt": "FT   TRANSMEM        177..197\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:24.266216+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 63-65",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "db1acbf2ac66c5648de96f9c489a7a4f13b2cb19c91ff902f8cef92abf8b0704",
  "url": "https://rest.uniprot.org/unisave/P0DXW1?format=txt&versions=2"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW1?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H8",
  "excerpt": "FT   TRANSMEM        222..242\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:24.266216+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 66-68",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "db1acbf2ac66c5648de96f9c489a7a4f13b2cb19c91ff902f8cef92abf8b0704",
  "url": "https://rest.uniprot.org/unisave/P0DXW1?format=txt&versions=2"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW1?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H9",
  "excerpt": "FT   TRANSMEM        267..287\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:24.266216+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 69-71",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "db1acbf2ac66c5648de96f9c489a7a4f13b2cb19c91ff902f8cef92abf8b0704",
  "url": "https://rest.uniprot.org/unisave/P0DXW1?format=txt&versions=2"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW1?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H10",
  "excerpt": "FT   TRANSMEM        298..318\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:24.266216+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 72-74",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "db1acbf2ac66c5648de96f9c489a7a4f13b2cb19c91ff902f8cef92abf8b0704",
  "url": "https://rest.uniprot.org/unisave/P0DXW1?format=txt&versions=2"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 76. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
