# transmembrane_0115

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0115.txt)

**Task:** `transmembrane`  
**Expected answer:** **A** — 604..624

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKANRIWCFFAWRMVVRASFLKEMDSIFVSAIRQNVQHTHSALLAKLKEPPDPDDENSWLCRISKKYDACGSREYSDKGLKGTYCPEDFCCSKTACFYGSCGSWCHDNWALCSSSIIYHDEYSYGKCNCKRFQENCDVNAICVHANREDGGAYCQCKEGYWGDGKSCKIDFCQLQPCGAGTCTRTDEGYKCDCPETHKLIVVEDKETCKAKPDFCAEEPCGPPSMVENCVNTDDSYECVCKQGYEVRNGRCEEIDLCADKPCGPDEGVHECVTERQPKLRYRCTCKAGFDLTTLPDGVSQKCLKNFCYEEPCGTRDLVESCKSKAYGYSCLCAAGAMVQVINGKEKCIKADLCRNDPCGPETAVIQCYSHGTSYRCLCKAGYTEVFVNGKSSCQKGDPCTLNMCGGNEAVQECTTDGTAYGCTCKPGYSIAIKHGQKFCNPEEECASHCGSAAAVKSCEILDSGGYQCTCNPGYVMRYSDYVKGCVEGNQCSLNPCGEQEAVQRCIPEGDTYDCECNPGFVKRVLPDGNFICADPASCVGNPCGSSDAVDACIAGTSTYTCRCKDGYTPQSIGSKLQCLPESTDQTDFDSKHKPEDNKGRYSKGTIALVVVGCVALLGIIAGGISYARNRGGERDDEDLAPPPRSTRERRLSSMGEGFENASWASSVSMIPSAPAPPPSGGIWS

[Multiple Choices]
A. 604..624
B. 20..39
C. 605..624
D. 604..624; 543..567
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

> The sequence-matched UniProt records annotate residues 604–624 as a helical transmembrane region. The annotation is computational (ECO:0000255), not evidence of experimental determination, but it supports the key.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The C-terminal hydrophobic stretch, following a long cysteine-rich region, is a credible membrane-anchor inference and distinguishes this region from the N-terminal hydrophobic signal-like segment and the nonhydrophobic region in D's extra span.


**Missing item-specific fact**

> The precise annotated start boundary—604 rather than 605—is not meaningfully resolved by the transferable sequence-level inference.


**Reason**

> Transferable knowledge identifies the likely C-terminal membrane span, but choices A and C differ by only one residue. Distinguishing those exact boundaries requires an item-specific boundary annotation or equivalent prediction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> Both choices identify essentially the same strongly hydrophobic C-terminal span; the supplied sequence alone does not meaningfully establish whether its start is residue 604 or 605.


### Important caveats

- The supporting transmembrane annotation is computational, not experimental.
- Reviewer-only evidence establishes support for the key but was not part of the original model input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The C-terminal hydrophobic stretch, following a long cysteine-rich region, is a credible membrane-anchor inference and distinguishes this region from the N-terminal hydrophobic signal-like segment and the nonhydrophobic region in D's extra span.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The precise annotated start boundary—604 rather than 605—is not meaningfully resolved by the transferable sequence-level inference.",
    "reason": "Transferable knowledge identifies the likely C-terminal membrane span, but choices A and C differ by only one residue. Distinguishing those exact boundaries requires an item-specific boundary annotation or equivalent prediction."
  },
  "case_id": "transmembrane_0115",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt records annotate residues 604–624 as a helical transmembrane region. The annotation is computational (ECO:0000255), not evidence of experimental determination, but it supports the key."
  },
  "important_caveats": [
    "The supporting transmembrane annotation is computational, not experimental.",
    "Reviewer-only evidence establishes support for the key but was not part of the original model input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "Both choices identify essentially the same strongly hydrophobic C-terminal span; the supplied sequence alone does not meaningfully establish whether its start is residue 604 or 605."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0115",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt records annotate residues 604–624 as a helical transmembrane region. The annotation is computational (ECO:0000255), not evidence of experimental determination, but it supports the key.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The C-terminal hydrophobic stretch, following a long cysteine-rich region, is a credible membrane-anchor inference and distinguishes this region from the N-terminal hydrophobic signal-like segment and the nonhydrophobic region in D's extra span.",
    "missing_item_specific_fact": "The precise annotated start boundary—604 rather than 605—is not meaningfully resolved by the transferable sequence-level inference.",
    "reason": "Transferable knowledge identifies the likely C-terminal membrane span, but choices A and C differ by only one residue. Distinguishing those exact boundaries requires an item-specific boundary annotation or equivalent prediction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "Both choices identify essentially the same strongly hydrophobic C-terminal span; the supplied sequence alone does not meaningfully establish whether its start is residue 604 or 605."
  },
  "important_caveats": [
    "The supporting transmembrane annotation is computational, not experimental.",
    "Reviewer-only evidence establishes support for the key but was not part of the original model input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (evidence C5, H3) explicitly states TRANSMEM 604..624, Helical, with evidence code ECO:0000255 (computational/similarity-based prediction). Option A (604..624) matches this annotation exactly. The sequence segment at positions 604-624 (GTIALVVVGCVALLGIIAGGI) is a 21-residue hydrophobic stretch consistent with a single-pass transmembrane helix.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Options B and D can be eliminated by sequence analysis: position 20-39 falls in the signal peptide/N-terminal region containing charged residues (K, E, D, R, Q) incompatible with a TM helix, and position 543-567 lies within the EGF-like domain region rich in cysteines and charged residues, clearly not hydrophobic. The remaining distinction is A (604..624) vs C (605..624), a one-residue difference. The sequence context around the TM region is ...K-S-G-T-I-A-L-V-V-V-G-C-V-A-L-L-G-I-I-A-G-G-I-S-Y-A-R... The residues preceding the hydrophobic stretch (K, S) are clearly polar/charged, while G at position 604 is small and uncharged, sitting at the boundary of the hydrophobic segment. Standard hydrophobicity-window analysis (e.g., 19-21 residue sliding window) would include this G as part of the hydrophobic peak since it is flanked by K/S on one side and T/I on the other, and G is commonly incorporated at TM helix boundaries. Starting the helix at T (option C) would place a polar residue at the helix start, which is less typical. Thus, transferable knowledge of TM helix boundary conventions and hydrophobicity analysis slightly favors including G, supporting option A over C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The hydrophobic stretch is clearly identifiable in the C-terminal region. Options B and D are eliminable by recognizing signal-peptide and EGF-domain sequence features. The A-vs-C distinction is a one-residue boundary question, but hydrophobicity analysis and TM helix boundary conventions (small uncharged residues at helix termini) provide a defensible, if probabilistic, basis for including G at position 604.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> The one-residue difference between 604..624 (A) and 605..624 (C) represents a genuinely fuzzy TM helix boundary. Both 20- and 21-residue helices are within the normal range. The G/T boundary is ambiguous by standard hydrophobicity criteria. While the G is slightly more defensible as a helix boundary residue, a model could reasonably argue either boundary.


### Important caveats

- The UniProt annotation uses evidence code ECO:0000255 (computational/similarity-based), not direct experimental verification of the TM boundary.
- The A-vs-C distinction is a single-residue boundary question; the reasoning argument is probabilistic rather than definitive.
- The protein is a Toxoplasma gondii micronemal protein (MIC8) with multiple EGF-like domains; the single TM helix near the C-terminus is consistent with its role as a membrane-anchored escorter protein.
- Option D's second region (543..567) falls squarely in the EGF-like domain repeat region and is clearly not a TM helix, making D eliminable.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Options B and D can be eliminated by sequence analysis: position 20-39 falls in the signal peptide/N-terminal region containing charged residues (K, E, D, R, Q) incompatible with a TM helix, and position 543-567 lies within the EGF-like domain region rich in cysteines and charged residues, clearly not hydrophobic. The remaining distinction is A (604..624) vs C (605..624), a one-residue difference. The sequence context around the TM region is ...K-S-G-T-I-A-L-V-V-V-G-C-V-A-L-L-G-I-I-A-G-G-I-S-Y-A-R... The residues preceding the hydrophobic stretch (K, S) are clearly polar/charged, while G at position 604 is small and uncharged, sitting at the boundary of the hydrophobic segment. Standard hydrophobicity-window analysis (e.g., 19-21 residue sliding window) would include this G as part of the hydrophobic peak since it is flanked by K/S on one side and T/I on the other, and G is commonly incorporated at TM helix boundaries. Starting the helix at T (option C) would place a polar residue at the helix start, which is less typical. Thus, transferable knowledge of TM helix boundary conventions and hydrophobicity analysis slightly favors including G, supporting option A over C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The hydrophobic stretch is clearly identifiable in the C-terminal region. Options B and D are eliminable by recognizing signal-peptide and EGF-domain sequence features. The A-vs-C distinction is a one-residue boundary question, but hydrophobicity analysis and TM helix boundary conventions (small uncharged residues at helix termini) provide a defensible, if probabilistic, basis for including G at position 604."
  },
  "case_id": "transmembrane_0115",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C5, H3) explicitly states TRANSMEM 604..624, Helical, with evidence code ECO:0000255 (computational/similarity-based prediction). Option A (604..624) matches this annotation exactly. The sequence segment at positions 604-624 (GTIALVVVGCVALLGIIAGGI) is a 21-residue hydrophobic stretch consistent with a single-pass transmembrane helix."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (computational/similarity-based), not direct experimental verification of the TM boundary.",
    "The A-vs-C distinction is a single-residue boundary question; the reasoning argument is probabilistic rather than definitive.",
    "The protein is a Toxoplasma gondii micronemal protein (MIC8) with multiple EGF-like domains; the single TM helix near the C-terminus is consistent with its role as a membrane-anchored escorter protein.",
    "Option D's second region (543..567) falls squarely in the EGF-like domain repeat region and is clearly not a TM helix, making D eliminable."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "The one-residue difference between 604..624 (A) and 605..624 (C) represents a genuinely fuzzy TM helix boundary. Both 20- and 21-residue helices are within the normal range. The G/T boundary is ambiguous by standard hydrophobicity criteria. While the G is slightly more defensible as a helix boundary residue, a model could reasonably argue either boundary."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0115",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C5, H3) explicitly states TRANSMEM 604..624, Helical, with evidence code ECO:0000255 (computational/similarity-based prediction). Option A (604..624) matches this annotation exactly. The sequence segment at positions 604-624 (GTIALVVVGCVALLGIIAGGI) is a 21-residue hydrophobic stretch consistent with a single-pass transmembrane helix.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Options B and D can be eliminated by sequence analysis: position 20-39 falls in the signal peptide/N-terminal region containing charged residues (K, E, D, R, Q) incompatible with a TM helix, and position 543-567 lies within the EGF-like domain region rich in cysteines and charged residues, clearly not hydrophobic. The remaining distinction is A (604..624) vs C (605..624), a one-residue difference. The sequence context around the TM region is ...K-S-G-T-I-A-L-V-V-V-G-C-V-A-L-L-G-I-I-A-G-G-I-S-Y-A-R... The residues preceding the hydrophobic stretch (K, S) are clearly polar/charged, while G at position 604 is small and uncharged, sitting at the boundary of the hydrophobic segment. Standard hydrophobicity-window analysis (e.g., 19-21 residue sliding window) would include this G as part of the hydrophobic peak since it is flanked by K/S on one side and T/I on the other, and G is commonly incorporated at TM helix boundaries. Starting the helix at T (option C) would place a polar residue at the helix start, which is less typical. Thus, transferable knowledge of TM helix boundary conventions and hydrophobicity analysis slightly favors including G, supporting option A over C.",
    "missing_item_specific_fact": "",
    "reason": "The hydrophobic stretch is clearly identifiable in the C-terminal region. Options B and D are eliminable by recognizing signal-peptide and EGF-domain sequence features. The A-vs-C distinction is a one-residue boundary question, but hydrophobicity analysis and TM helix boundary conventions (small uncharged residues at helix termini) provide a defensible, if probabilistic, basis for including G at position 604."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "The one-residue difference between 604..624 (A) and 605..624 (C) represents a genuinely fuzzy TM helix boundary. Both 20- and 21-residue helices are within the normal range. The G/T boundary is ambiguous by standard hydrophobicity criteria. While the G is slightly more defensible as a helix boundary residue, a model could reasonably argue either boundary."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (computational/similarity-based), not direct experimental verification of the TM boundary.",
    "The A-vs-C distinction is a single-residue boundary question; the reasoning argument is probabilistic rather than definitive.",
    "The protein is a Toxoplasma gondii micronemal protein (MIC8) with multiple EGF-like domains; the single TM helix near the C-terminus is consistent with its role as a membrane-anchored escorter protein.",
    "Option D's second region (543..567) falls squarely in the EGF-like domain repeat region and is clearly not a TM helix, making D eliminable."
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
  "benchmark_sequence_length": 684,
  "benchmark_sequence_sha256": "b06f78ad156d49575dc708492a79dfb5aca4e4016331191d7f59e8147aee63ba",
  "current_entry_audit": {
    "entryVersion": 105,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2001-06-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "1e26d02d811092d5350aec3cf5656bbd901e1bcb12f8e7f35f889b6548fa730c",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 684,
  "current_source_sequence_sha256": "b06f78ad156d49575dc708492a79dfb5aca4e4016331191d7f59e8147aee63ba",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 104,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9BIM7",
  "selected_historical_entry_version": 104,
  "selected_historical_record_sha256": "8c1cdfe300fe0b7fd1b3d88242ec8673bd6601c370229c09fb7966b89d227666",
  "selected_historical_source_sequence_length": 684,
  "selected_historical_source_sequence_sha256": "b06f78ad156d49575dc708492a79dfb5aca4e4016331191d7f59e8147aee63ba",
  "selected_historical_version": {
    "accession": "Q9BIM7",
    "database": "Swiss-Prot",
    "entryVersion": 104,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "MIC8_TOXGO",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9BIM7.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9BIM7\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:32:41.847892+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1e26d02d811092d5350aec3cf5656bbd901e1bcb12f8e7f35f889b6548fa730c",
  "url": "https://rest.uniprot.org/uniprotkb/Q9BIM7.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9BIM7.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":105,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2001-06-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:32:41.847892+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1e26d02d811092d5350aec3cf5656bbd901e1bcb12f8e7f35f889b6548fa730c",
  "url": "https://rest.uniprot.org/uniprotkb/Q9BIM7.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9BIM7.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAK19757.1\",\"source\":\"EMBL\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Conoidasida\",\"Coccidia\",\"Eucoccidiorida\",\"Eimeriorina\",\"Sarcocystidae\",\"Toxoplasma\"],\"scientificName\":\"Toxoplasma gondii\",\"taxonId\":5811}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:32:41.847892+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1e26d02d811092d5350aec3cf5656bbd901e1bcb12f8e7f35f889b6548fa730c",
  "url": "https://rest.uniprot.org/uniprotkb/Q9BIM7.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9BIM7.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"KAF4638404.1\",\"source\":\"EMBL\"}],\"value\":\"Microneme protein MIC8\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Micronemal protein 8\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"11861763\",\"source\":\"PubMed\"}],\"value\":\"TgMIC8\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:32:41.847892+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1e26d02d811092d5350aec3cf5656bbd901e1bcb12f8e7f35f889b6548fa730c",
  "url": "https://rest.uniprot.org/uniprotkb/Q9BIM7.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9BIM7.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":624},\"start\":{\"modifier\":\"EXACT\",\"value\":604}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:32:41.847892+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1e26d02d811092d5350aec3cf5656bbd901e1bcb12f8e7f35f889b6548fa730c",
  "url": "https://rest.uniprot.org/uniprotkb/Q9BIM7.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9BIM7.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Meissner M.\",\"Reiss M.\",\"Viebig N.\",\"Carruthers V.B.\",\"Toursel C.\",\"Tomavo S.\",\"Ajioka J.W.\",\"Soldati D.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"11861763\"},{\"database\":\"DOI\",\"id\":\"10.1242/jcs.115.3.563\"}],\"citationType\":\"journal article\",\"firstPage\":\"563\",\"id\":\"11861763\",\"journal\":\"J. Cell Sci.\",\"lastPage\":\"574\",\"publicationDate\":\"2002\",\"title\":\"A family of transmembrane microneme proteins of Toxoplasma gondii contain EGF-like domains and function as escorters.\",\"volume\":\"115\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":5,\"referencePositions\":[\"SUBCELLULAR LOCATION\",\"DEVELOPMENTAL STAGE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-02T04:32:41.847892+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1e26d02d811092d5350aec3cf5656bbd901e1bcb12f8e7f35f889b6548fa730c",
  "url": "https://rest.uniprot.org/uniprotkb/Q9BIM7.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9BIM7?format=txt&versions=104)

```json
{
  "entry_version": 104,
  "evidence_id": "H1",
  "excerpt": "ID   MIC8_TOXGO              Reviewed;         684 AA.\nAC   Q9BIM7; S7WHE3;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-JUN-2001, sequence version 1.\nDT   28-JAN-2026, entry version 104.\nDE   RecName: Full=Micronemal protein 8 {ECO:0000305};\nDE            Short=TgMIC8 {ECO:0000303|PubMed:11861763};\nDE   AltName: Full=Microneme protein MIC8 {ECO:0000312|EMBL:KAF4638404.1};\nDE   Flags: Precursor;\nGN   Name=MIC8 {ECO:0000312|EMBL:AAK19757.1};\nGN   ORFNames=TGRH88_060120 {ECO:0000312|EMBL:KAF4638404.1};\nOS   Toxoplasma gondii.\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Conoidasida; Coccidia;\nOC   Eucoccidiorida; Eimeriorina; Sarcocystidae; Toxoplasma.\nOX   NCBI_TaxID=5811 {ECO:0000312|EMBL:AAK19757.1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:43.749643+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8c1cdfe300fe0b7fd1b3d88242ec8673bd6601c370229c09fb7966b89d227666",
  "url": "https://rest.uniprot.org/unisave/Q9BIM7?format=txt&versions=104"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9BIM7?format=txt&versions=104)

```json
{
  "entry_version": 104,
  "evidence_id": "H2",
  "excerpt": "RN   [5] {ECO:0000305}\nRP   SUBCELLULAR LOCATION, AND DEVELOPMENTAL STAGE.\nRX   PubMed=11861763; DOI=10.1242/jcs.115.3.563;\nRA   Meissner M., Reiss M., Viebig N., Carruthers V.B., Toursel C., Tomavo S.,\nRA   Ajioka J.W., Soldati D.;\nRT   \"A family of transmembrane microneme proteins of Toxoplasma gondii contain\nRT   EGF-like domains and function as escorters.\";\nRL   J. Cell Sci. 115:563-574(2002).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:43.749643+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 42-49",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8c1cdfe300fe0b7fd1b3d88242ec8673bd6601c370229c09fb7966b89d227666",
  "url": "https://rest.uniprot.org/unisave/Q9BIM7?format=txt&versions=104"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9BIM7?format=txt&versions=104)

```json
{
  "entry_version": 104,
  "evidence_id": "H3",
  "excerpt": "FT   TRANSMEM        604..624\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:43.749643+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 142-144",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8c1cdfe300fe0b7fd1b3d88242ec8673bd6601c370229c09fb7966b89d227666",
  "url": "https://rest.uniprot.org/unisave/Q9BIM7?format=txt&versions=104"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 115. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
