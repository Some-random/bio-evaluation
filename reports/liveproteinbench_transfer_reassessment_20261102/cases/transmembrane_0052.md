# transmembrane_0052

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0052.txt)

**Task:** `transmembrane`  
**Expected answer:** **B** — 227..249

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MEILRLAQSKKNIISLNMDLERDMQRIDEANQELLLKIQEKESEVQRLEHEITQTGDPAEDEEWEKENYTVMEREQALQELEEETARLERKNETLVHSISELQRKLTRKSQKIVRCEQGDLERTPEESKVKLQLLESSCADQEKELGKIMEDYVFVSQLCEDQALCIKKYQEALKRIEEELETGYLEREVSKVLSMDSEREKTVSLNEKDGFISNGALRFSKRIFRSLLFSTLFFIRLLGYLIFHLSFINPDLLVNALPKILSRDVLWKLRCFLFPSLTLETEDMLPH

[Multiple Choices]
A. 230..251
B. 227..249
C. 227..249; 334..355
D. 1404..1424
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

> The sequence-matched UniProt annotation identifies residues 227–249 as a helical transmembrane region. Its ECO:0000255 evidence code indicates computational support, not experimental demonstration.

Citations as saved: [C5](#evidence-c5), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a conspicuous hydrophobic C-terminal segment, consistent with a membrane-spanning helix. That feature supports the overlapping ranges A and B, while C adds a region beyond the 288-residue sequence and D is also out of range. B is a plausible boundary choice: it ends before the following polar/proline-rich sequence, whereas A extends farther into it.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable knowledge about hydrophobic membrane helices meaningfully identifies the relevant region and rules against C and D. It does not make the exact boundaries certain, since A and B overlap substantially.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Both ranges cover the same hydrophobic helix and are plausible approximate transmembrane spans. The sequence favors B's C-terminal boundary, but the question provides no boundary convention that decisively excludes A.


### Important caveats

- The cited annotation is computational, not experimental evidence.
- Transmembrane-region boundaries can be approximate; the sequence supports the helix more strongly than an exact residue-level boundary.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a conspicuous hydrophobic C-terminal segment, consistent with a membrane-spanning helix. That feature supports the overlapping ranges A and B, while C adds a region beyond the 288-residue sequence and D is also out of range. B is a plausible boundary choice: it ends before the following polar/proline-rich sequence, whereas A extends farther into it.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge about hydrophobic membrane helices meaningfully identifies the relevant region and rules against C and D. It does not make the exact boundaries certain, since A and B overlap substantially."
  },
  "case_id": "transmembrane_0052",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies residues 227–249 as a helical transmembrane region. Its ECO:0000255 evidence code indicates computational support, not experimental demonstration."
  },
  "important_caveats": [
    "The cited annotation is computational, not experimental evidence.",
    "Transmembrane-region boundaries can be approximate; the sequence supports the helix more strongly than an exact residue-level boundary."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Both ranges cover the same hydrophobic helix and are plausible approximate transmembrane spans. The sequence favors B's C-terminal boundary, but the question provides no boundary convention that decisively excludes A."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0052",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies residues 227–249 as a helical transmembrane region. Its ECO:0000255 evidence code indicates computational support, not experimental demonstration.",
    "evidence_ids": ["C5", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a conspicuous hydrophobic C-terminal segment, consistent with a membrane-spanning helix. That feature supports the overlapping ranges A and B, while C adds a region beyond the 288-residue sequence and D is also out of range. B is a plausible boundary choice: it ends before the following polar/proline-rich sequence, whereas A extends farther into it.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge about hydrophobic membrane helices meaningfully identifies the relevant region and rules against C and D. It does not make the exact boundaries certain, since A and B overlap substantially."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Both ranges cover the same hydrophobic helix and are plausible approximate transmembrane spans. The sequence favors B's C-terminal boundary, but the question provides no boundary convention that decisively excludes A."
  },
  "important_caveats": [
    "The cited annotation is computational, not experimental evidence.",
    "Transmembrane-region boundaries can be approximate; the sequence supports the helix more strongly than an exact residue-level boundary."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for this protein (D3ZNV2, TMC5A_RAT, 288 aa) explicitly annotates a single transmembrane helix at positions 227..249 (evidence C5, H2), matching the expected answer B exactly. The evidence code ECO:0000255 indicates this is an inference-by-similarity annotation, not experimental, but the sequence region 227-249 (SLLFSTLFFIRLLGYLIFHLSFI) is consistent with a hydrophobic α-helical TM segment of 23 residues. No contradicting evidence is present.

Citations as saved: [C5](#evidence-c5), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Options C (334..355) and D (1404..1424) are immediately eliminated because the protein is only 288 residues long. The real distinction is between A (230..251) and B (227..249). The hydrophobic core is identifiable from the sequence: positions ~227-249 contain the stretch SLLFSTLFFIRLLGYLIFHLSFI, a predominantly hydrophobic 23-residue segment consistent with a single-pass TM α-helix. Option A extends to position 251, which includes Asn (polar) at 250 and Pro at 251. Proline is a well-known helix breaker that is virtually never found within a TM α-helix; its inclusion in option A is a strong argument against it. Option B ends on Ile (hydrophobic) and starts on Ser (small, commonly tolerated at TM helix boundaries). The 'ST' motif at positions 231-232 within option B is a minor polar interruption but is well-documented in TM helices (e.g., GPCRs, many single-pass receptors) and does not invalidate the helix. General TM-helix composition rules (avoid Pro, prefer hydrophobic termini, ~20-25 residues) meaningfully favor B over A.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The elimination of C and D requires only a length check. The A-vs-B distinction relies on transferable knowledge: Proline is a helix breaker excluded from TM segments, and the hydrophobicity profile of the sequence is directly readable. No target-specific database lookup is necessary to prefer B over A.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> C and D are impossible given the 288-residue protein length. Between A and B, the inclusion of Pro at position 251 in option A is a clear violation of TM helix composition rules, making B the clearly superior choice. The 'ST' in B's middle is a minor concern but well within accepted TM helix composition.


### Important caveats

- The UniProt annotation uses evidence code ECO:0000255 (inferred by similarity), meaning the 227..249 boundary is a computational/annotation prediction rather than an experimentally determined boundary. Exact TM boundaries can vary by a few residues depending on the prediction method.
- The distinction between A and B is only 3 residues at each end; in practice, different TM prediction tools might give slightly different boundaries. However, the Pro exclusion principle provides a clear qualitative argument favoring B.
- The reviewer-only accession (D3ZNV2) and organism identity were not available to the evaluated model; the reasoning above relies solely on the sequence and general biology.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Options C (334..355) and D (1404..1424) are immediately eliminated because the protein is only 288 residues long. The real distinction is between A (230..251) and B (227..249). The hydrophobic core is identifiable from the sequence: positions ~227-249 contain the stretch SLLFSTLFFIRLLGYLIFHLSFI, a predominantly hydrophobic 23-residue segment consistent with a single-pass TM α-helix. Option A extends to position 251, which includes Asn (polar) at 250 and Pro at 251. Proline is a well-known helix breaker that is virtually never found within a TM α-helix; its inclusion in option A is a strong argument against it. Option B ends on Ile (hydrophobic) and starts on Ser (small, commonly tolerated at TM helix boundaries). The 'ST' motif at positions 231-232 within option B is a minor polar interruption but is well-documented in TM helices (e.g., GPCRs, many single-pass receptors) and does not invalidate the helix. General TM-helix composition rules (avoid Pro, prefer hydrophobic termini, ~20-25 residues) meaningfully favor B over A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The elimination of C and D requires only a length check. The A-vs-B distinction relies on transferable knowledge: Proline is a helix breaker excluded from TM segments, and the hydrophobicity profile of the sequence is directly readable. No target-specific database lookup is necessary to prefer B over A."
  },
  "case_id": "transmembrane_0052",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for this protein (D3ZNV2, TMC5A_RAT, 288 aa) explicitly annotates a single transmembrane helix at positions 227..249 (evidence C5, H2), matching the expected answer B exactly. The evidence code ECO:0000255 indicates this is an inference-by-similarity annotation, not experimental, but the sequence region 227-249 (SLLFSTLFFIRLLGYLIFHLSFI) is consistent with a hydrophobic α-helical TM segment of 23 residues. No contradicting evidence is present."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (inferred by similarity), meaning the 227..249 boundary is a computational/annotation prediction rather than an experimentally determined boundary. Exact TM boundaries can vary by a few residues depending on the prediction method.",
    "The distinction between A and B is only 3 residues at each end; in practice, different TM prediction tools might give slightly different boundaries. However, the Pro exclusion principle provides a clear qualitative argument favoring B.",
    "The reviewer-only accession (D3ZNV2) and organism identity were not available to the evaluated model; the reasoning above relies solely on the sequence and general biology."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "C and D are impossible given the 288-residue protein length. Between A and B, the inclusion of Pro at position 251 in option A is a clear violation of TM helix composition rules, making B the clearly superior choice. The 'ST' in B's middle is a minor concern but well within accepted TM helix composition."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0052",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for this protein (D3ZNV2, TMC5A_RAT, 288 aa) explicitly annotates a single transmembrane helix at positions 227..249 (evidence C5, H2), matching the expected answer B exactly. The evidence code ECO:0000255 indicates this is an inference-by-similarity annotation, not experimental, but the sequence region 227-249 (SLLFSTLFFIRLLGYLIFHLSFI) is consistent with a hydrophobic α-helical TM segment of 23 residues. No contradicting evidence is present.",
    "evidence_ids": ["C5", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Options C (334..355) and D (1404..1424) are immediately eliminated because the protein is only 288 residues long. The real distinction is between A (230..251) and B (227..249). The hydrophobic core is identifiable from the sequence: positions ~227-249 contain the stretch SLLFSTLFFIRLLGYLIFHLSFI, a predominantly hydrophobic 23-residue segment consistent with a single-pass TM α-helix. Option A extends to position 251, which includes Asn (polar) at 250 and Pro at 251. Proline is a well-known helix breaker that is virtually never found within a TM α-helix; its inclusion in option A is a strong argument against it. Option B ends on Ile (hydrophobic) and starts on Ser (small, commonly tolerated at TM helix boundaries). The 'ST' motif at positions 231-232 within option B is a minor polar interruption but is well-documented in TM helices (e.g., GPCRs, many single-pass receptors) and does not invalidate the helix. General TM-helix composition rules (avoid Pro, prefer hydrophobic termini, ~20-25 residues) meaningfully favor B over A.",
    "missing_item_specific_fact": "",
    "reason": "The elimination of C and D requires only a length check. The A-vs-B distinction relies on transferable knowledge: Proline is a helix breaker excluded from TM segments, and the hydrophobicity profile of the sequence is directly readable. No target-specific database lookup is necessary to prefer B over A."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "C and D are impossible given the 288-residue protein length. Between A and B, the inclusion of Pro at position 251 in option A is a clear violation of TM helix composition rules, making B the clearly superior choice. The 'ST' in B's middle is a minor concern but well within accepted TM helix composition."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (inferred by similarity), meaning the 227..249 boundary is a computational/annotation prediction rather than an experimentally determined boundary. Exact TM boundaries can vary by a few residues depending on the prediction method.",
    "The distinction between A and B is only 3 residues at each end; in practice, different TM prediction tools might give slightly different boundaries. However, the Pro exclusion principle provides a clear qualitative argument favoring B.",
    "The reviewer-only accession (D3ZNV2) and organism identity were not available to the evaluated model; the reasoning above relies solely on the sequence and general biology."
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
  "benchmark_sequence_length": 288,
  "benchmark_sequence_sha256": "4b889ff0121995f352547fa895c5d5dbb10d9586f727e4a6225c501fc4bba60e",
  "current_entry_audit": {
    "entryVersion": 79,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2022-05-25",
    "sequenceVersion": 3
  },
  "current_record_sha256": "29374169b9ac851b080d82af3408767d5388d739d0142cd3d417d041e6810675",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 288,
  "current_source_sequence_sha256": "4b889ff0121995f352547fa895c5d5dbb10d9586f727e4a6225c501fc4bba60e",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 77,
      "exact_sequence_comparison": "matched",
      "sequence_version": 3
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "D3ZNV2",
  "selected_historical_entry_version": 77,
  "selected_historical_record_sha256": "5760c372bfd312c618c77199dec0871bf8d8b8bd127d6e6a8614fec3b04057fb",
  "selected_historical_source_sequence_length": 288,
  "selected_historical_source_sequence_sha256": "4b889ff0121995f352547fa895c5d5dbb10d9586f727e4a6225c501fc4bba60e",
  "selected_historical_version": {
    "accession": "D3ZNV2",
    "database": "Swiss-Prot",
    "entryVersion": 77,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "TMC5A_RAT",
    "sequenceVersion": 3
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3ZNV2.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"D3ZNV2\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:27:45.198803+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "29374169b9ac851b080d82af3408767d5388d739d0142cd3d417d041e6810675",
  "url": "https://rest.uniprot.org/uniprotkb/D3ZNV2.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3ZNV2.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":79,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2022-05-25\",\"sequenceVersion\":3}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:27:45.198803+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "29374169b9ac851b080d82af3408767d5388d739d0142cd3d417d041e6810675",
  "url": "https://rest.uniprot.org/uniprotkb/D3ZNV2.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3ZNV2.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Rat\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Euteleostomi\",\"Mammalia\",\"Eutheria\",\"Euarchontoglires\",\"Glires\",\"Rodentia\",\"Myomorpha\",\"Muroidea\",\"Muridae\",\"Murinae\",\"Rattus\"],\"scientificName\":\"Rattus norvegicus\",\"taxonId\":10116}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:27:45.198803+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "29374169b9ac851b080d82af3408767d5388d739d0142cd3d417d041e6810675",
  "url": "https://rest.uniprot.org/uniprotkb/D3ZNV2.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3ZNV2.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"value\":\"Transmembrane and coiled-coil domain-containing protein 5A\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:27:45.198803+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "29374169b9ac851b080d82af3408767d5388d739d0142cd3d417d041e6810675",
  "url": "https://rest.uniprot.org/uniprotkb/D3ZNV2.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3ZNV2.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":249},\"start\":{\"modifier\":\"EXACT\",\"value\":227}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:27:45.198803+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "29374169b9ac851b080d82af3408767d5388d739d0142cd3d417d041e6810675",
  "url": "https://rest.uniprot.org/uniprotkb/D3ZNV2.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3ZNV2?format=txt&versions=77)

```json
{
  "entry_version": 77,
  "evidence_id": "H1",
  "excerpt": "ID   TMC5A_RAT               Reviewed;         288 AA.\nAC   D3ZNV2; A0A8I6A3G0;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   25-MAY-2022, sequence version 3.\nDT   28-JAN-2026, entry version 77.\nDE   RecName: Full=Transmembrane and coiled-coil domain-containing protein 5A;\nGN   Name=Tmco5a; Synonyms=Tmco5;\nOS   Rattus norvegicus (Rat).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;\nOC   Eutheria; Euarchontoglires; Glires; Rodentia; Myomorpha; Muroidea; Muridae;\nOC   Murinae; Rattus.\nOX   NCBI_TaxID=10116;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:48.423993+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 3,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5760c372bfd312c618c77199dec0871bf8d8b8bd127d6e6a8614fec3b04057fb",
  "url": "https://rest.uniprot.org/unisave/D3ZNV2?format=txt&versions=77"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3ZNV2?format=txt&versions=77)

```json
{
  "entry_version": 77,
  "evidence_id": "H2",
  "excerpt": "FT   TRANSMEM        227..249\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:48.423993+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 3,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 111-113",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5760c372bfd312c618c77199dec0871bf8d8b8bd127d6e6a8614fec3b04057fb",
  "url": "https://rest.uniprot.org/unisave/D3ZNV2?format=txt&versions=77"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 52. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
