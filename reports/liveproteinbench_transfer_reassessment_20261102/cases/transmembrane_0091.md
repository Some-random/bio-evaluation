# transmembrane_0091

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0091.txt)

**Task:** `transmembrane`  
**Expected answer:** **A** — 281..301

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MLVSDRDKLEDKALIPLDNIFHNGKGTLVQASVTSVEKEKTGGFVVLDNGEKLPFYVLVVATGSKWSGPVDFPSKPEDVTKWISEQRKKFKDAKNIVIAGGGSVGLELSGEIKDIWPEKSVTIVHSQKKLLNSVYPDKFRDRAAQAYRPRTKLVLDDQIPGELTPGATSVTTRNGKTITADLIVPAWGNKPNTALLSSLKDVLSPNGCVKIRDTFQTQAYPDIFALGDIIDVNEQKQAGKAQAHAGMVAANVLSYVQGQPLKQKYKGSYELIVITNGKNDGVGYFGVWWGIVIGGWLASLLKAKDLMLPATRVATGASK

[Multiple Choices]
A. 281..301
B. 277..300
C. 281..301; 597..617
D. 14..34
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

> The sequence-matched UniProt annotation identifies residues 281–301 as a helical transmembrane region. Its ECO:0000255 evidence indicates computational annotation, not direct experimental demonstration.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Residues 281–301 form a long, strongly hydrophobic stretch suitable for a membrane-spanning alpha helix. Option B includes several polar or charged residues before this hydrophobic stretch and truncates its end; D is not comparably hydrophobic, and C includes positions beyond the 319-residue sequence.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence itself contains a conspicuous membrane-compatible hydrophobic segment, and transferable knowledge about transmembrane helices meaningfully distinguishes A from the offered alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> A best matches the hydrophobic span; the alternatives either include non-hydrophobic residues, do not match the sequence length, or lack a comparable hydrophobic stretch.


### Important caveats

- The supporting database feature is computationally annotated; it does not by itself establish experimental verification.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Residues 281–301 form a long, strongly hydrophobic stretch suitable for a membrane-spanning alpha helix. Option B includes several polar or charged residues before this hydrophobic stretch and truncates its end; D is not comparably hydrophobic, and C includes positions beyond the 319-residue sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence itself contains a conspicuous membrane-compatible hydrophobic segment, and transferable knowledge about transmembrane helices meaningfully distinguishes A from the offered alternatives."
  },
  "case_id": "transmembrane_0091",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies residues 281–301 as a helical transmembrane region. Its ECO:0000255 evidence indicates computational annotation, not direct experimental demonstration."
  },
  "important_caveats": [
    "The supporting database feature is computationally annotated; it does not by itself establish experimental verification."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A best matches the hydrophobic span; the alternatives either include non-hydrophobic residues, do not match the sequence length, or lack a comparable hydrophobic stretch."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0091",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies residues 281–301 as a helical transmembrane region. Its ECO:0000255 evidence indicates computational annotation, not direct experimental demonstration.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Residues 281–301 form a long, strongly hydrophobic stretch suitable for a membrane-spanning alpha helix. Option B includes several polar or charged residues before this hydrophobic stretch and truncates its end; D is not comparably hydrophobic, and C includes positions beyond the 319-residue sequence.",
    "missing_item_specific_fact": "",
    "reason": "The sequence itself contains a conspicuous membrane-compatible hydrophobic segment, and transferable knowledge about transmembrane helices meaningfully distinguishes A from the offered alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A best matches the hydrophobic span; the alternatives either include non-hydrophobic residues, do not match the sequence length, or lack a comparable hydrophobic stretch."
  },
  "important_caveats": [
    "The supporting database feature is computationally annotated; it does not by itself establish experimental verification."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (evidence C5, H3) records a transmembrane helical region at exactly 281..301, matching choice A. The evidence code is ECO:0000255 (inferred by similarity to a related protein), so this is a computational/transfer annotation rather than direct experimental verification. However, the sequence at positions 281-301 (GVGYFGVWWGIVIGGWLASLL) is a hydrophobic stretch with aromatic residues (Y, F, W, W) at the boundaries and hydrophobic residues (V, I, L, A) in the core, consistent with a single-pass TM alpha-helix. The annotation is supported by the sequence itself.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Option C is eliminated immediately because positions 597-617 exceed the 319-residue protein length. Option D (14..34) contains multiple charged and polar residues (D, N, H, K, Q, S, T) and lacks the sustained hydrophobicity required for a TM helix. The critical distinction is between A (281..301) and B (277..300). Positions 277-280 encode G-K-N-D: three of these (K, N, D) are polar or charged, which are incompatible with the hydrophobic interior of a lipid bilayer-spanning helix. Starting the TM segment at 281 (G) or 282 (V) avoids these residues and captures the hydrophobic core VGYFGVWWGIVIGGWLASLL, which has a Kyte-Doolittle-like hydrophobic profile with aromatic residues (Y, F, W, W) positioned at the expected lipid-water interface. A model applying standard hydropathy analysis or recognizing the canonical TM helix signature (hydrophobic core flanked by aromatic residues) would exclude the GKND extension and select 281-301 over 277-300.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The hydrophobicity pattern of the sequence, combined with general knowledge of TM helix composition (hydrophobic core, aromatic interfacial residues, exclusion of charged residues from the bilayer-spanning region), provides a concrete basis for selecting A over B and D. Option C is trivially excluded by protein length. No fact specific to this exact protein beyond the supplied sequence is needed.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The charged residues K, N, D at positions 278-280 clearly break the hydrophobic stretch, making B (277..300) less defensible than A (281..301). Option D lacks hydrophobicity entirely, and C references nonexistent positions. Among the four choices, A is the only one consistent with standard TM helix criteria.


### Important caveats

- The UniProt TM annotation carries evidence code ECO:0000255 (inferred by similarity), meaning it was transferred from a related protein rather than directly predicted or experimentally determined for this sequence.
- The exact boundary residues (281 vs 282, 300 vs 301) are somewhat method-dependent; however, among the offered choices, the hydrophobicity argument clearly favors A over B.
- The protein is annotated as a FAD-dependent oxidoreductase (WD40 protein), and the single predicted TM helix likely serves as a membrane anchor rather than a channel.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Option C is eliminated immediately because positions 597-617 exceed the 319-residue protein length. Option D (14..34) contains multiple charged and polar residues (D, N, H, K, Q, S, T) and lacks the sustained hydrophobicity required for a TM helix. The critical distinction is between A (281..301) and B (277..300). Positions 277-280 encode G-K-N-D: three of these (K, N, D) are polar or charged, which are incompatible with the hydrophobic interior of a lipid bilayer-spanning helix. Starting the TM segment at 281 (G) or 282 (V) avoids these residues and captures the hydrophobic core VGYFGVWWGIVIGGWLASLL, which has a Kyte-Doolittle-like hydrophobic profile with aromatic residues (Y, F, W, W) positioned at the expected lipid-water interface. A model applying standard hydropathy analysis or recognizing the canonical TM helix signature (hydrophobic core flanked by aromatic residues) would exclude the GKND extension and select 281-301 over 277-300.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The hydrophobicity pattern of the sequence, combined with general knowledge of TM helix composition (hydrophobic core, aromatic interfacial residues, exclusion of charged residues from the bilayer-spanning region), provides a concrete basis for selecting A over B and D. Option C is trivially excluded by protein length. No fact specific to this exact protein beyond the supplied sequence is needed."
  },
  "case_id": "transmembrane_0091",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C5, H3) records a transmembrane helical region at exactly 281..301, matching choice A. The evidence code is ECO:0000255 (inferred by similarity to a related protein), so this is a computational/transfer annotation rather than direct experimental verification. However, the sequence at positions 281-301 (GVGYFGVWWGIVIGGWLASLL) is a hydrophobic stretch with aromatic residues (Y, F, W, W) at the boundaries and hydrophobic residues (V, I, L, A) in the core, consistent with a single-pass TM alpha-helix. The annotation is supported by the sequence itself."
  },
  "important_caveats": [
    "The UniProt TM annotation carries evidence code ECO:0000255 (inferred by similarity), meaning it was transferred from a related protein rather than directly predicted or experimentally determined for this sequence.",
    "The exact boundary residues (281 vs 282, 300 vs 301) are somewhat method-dependent; however, among the offered choices, the hydrophobicity argument clearly favors A over B.",
    "The protein is annotated as a FAD-dependent oxidoreductase (WD40 protein), and the single predicted TM helix likely serves as a membrane anchor rather than a channel."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The charged residues K, N, D at positions 278-280 clearly break the hydrophobic stretch, making B (277..300) less defensible than A (281..301). Option D lacks hydrophobicity entirely, and C references nonexistent positions. Among the four choices, A is the only one consistent with standard TM helix criteria."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0091",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C5, H3) records a transmembrane helical region at exactly 281..301, matching choice A. The evidence code is ECO:0000255 (inferred by similarity to a related protein), so this is a computational/transfer annotation rather than direct experimental verification. However, the sequence at positions 281-301 (GVGYFGVWWGIVIGGWLASLL) is a hydrophobic stretch with aromatic residues (Y, F, W, W) at the boundaries and hydrophobic residues (V, I, L, A) in the core, consistent with a single-pass TM alpha-helix. The annotation is supported by the sequence itself.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Option C is eliminated immediately because positions 597-617 exceed the 319-residue protein length. Option D (14..34) contains multiple charged and polar residues (D, N, H, K, Q, S, T) and lacks the sustained hydrophobicity required for a TM helix. The critical distinction is between A (281..301) and B (277..300). Positions 277-280 encode G-K-N-D: three of these (K, N, D) are polar or charged, which are incompatible with the hydrophobic interior of a lipid bilayer-spanning helix. Starting the TM segment at 281 (G) or 282 (V) avoids these residues and captures the hydrophobic core VGYFGVWWGIVIGGWLASLL, which has a Kyte-Doolittle-like hydrophobic profile with aromatic residues (Y, F, W, W) positioned at the expected lipid-water interface. A model applying standard hydropathy analysis or recognizing the canonical TM helix signature (hydrophobic core flanked by aromatic residues) would exclude the GKND extension and select 281-301 over 277-300.",
    "missing_item_specific_fact": "",
    "reason": "The hydrophobicity pattern of the sequence, combined with general knowledge of TM helix composition (hydrophobic core, aromatic interfacial residues, exclusion of charged residues from the bilayer-spanning region), provides a concrete basis for selecting A over B and D. Option C is trivially excluded by protein length. No fact specific to this exact protein beyond the supplied sequence is needed."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The charged residues K, N, D at positions 278-280 clearly break the hydrophobic stretch, making B (277..300) less defensible than A (281..301). Option D lacks hydrophobicity entirely, and C references nonexistent positions. Among the four choices, A is the only one consistent with standard TM helix criteria."
  },
  "important_caveats": [
    "The UniProt TM annotation carries evidence code ECO:0000255 (inferred by similarity), meaning it was transferred from a related protein rather than directly predicted or experimentally determined for this sequence.",
    "The exact boundary residues (281 vs 282, 300 vs 301) are somewhat method-dependent; however, among the offered choices, the hydrophobicity argument clearly favors A over B.",
    "The protein is annotated as a FAD-dependent oxidoreductase (WD40 protein), and the single predicted TM helix likely serves as a membrane anchor rather than a channel."
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
  "benchmark_sequence_length": 319,
  "benchmark_sequence_sha256": "7b558093635631e4d5e8123647a5ede975af25a57bd534eb6ff0360099de9539",
  "current_entry_audit": {
    "entryVersion": 66,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2006-01-24",
    "sequenceVersion": 1
  },
  "current_record_sha256": "beb3cfe391db72fc8866ae9445a0714bbe0a44d8c8a6074dc27c3819e066bff4",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 319,
  "current_source_sequence_sha256": "7b558093635631e4d5e8123647a5ede975af25a57bd534eb6ff0360099de9539",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 64,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q2RBS5",
  "selected_historical_entry_version": 64,
  "selected_historical_record_sha256": "da35682d80cb6cef63c8793b0377fbe770f2acb9c2e203caa3a8ca7d0a0e8f97",
  "selected_historical_source_sequence_length": 319,
  "selected_historical_source_sequence_sha256": "7b558093635631e4d5e8123647a5ede975af25a57bd534eb6ff0360099de9539",
  "selected_historical_version": {
    "accession": "Q2RBS5",
    "database": "Swiss-Prot",
    "entryVersion": 64,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "FD30_FLAVE",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2RBS5.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q2RBS5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:30:38.073015+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "beb3cfe391db72fc8866ae9445a0714bbe0a44d8c8a6074dc27c3819e066bff4",
  "url": "https://rest.uniprot.org/uniprotkb/Q2RBS5.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2RBS5.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":66,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2006-01-24\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:30:38.073015+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "beb3cfe391db72fc8866ae9445a0714bbe0a44d8c8a6074dc27c3819e066bff4",
  "url": "https://rest.uniprot.org/uniprotkb/Q2RBS5.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2RBS5.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Agaricus velutipes\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Basidiomycota\",\"Agaricomycotina\",\"Agaricomycetes\",\"Agaricomycetidae\",\"Agaricales\",\"Marasmiineae\",\"Physalacriaceae\",\"Flammulina\"],\"scientificName\":\"Flammulina velutipes\",\"taxonId\":38945}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:30:38.073015+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "beb3cfe391db72fc8866ae9445a0714bbe0a44d8c8a6074dc27c3819e066bff4",
  "url": "https://rest.uniprot.org/uniprotkb/Q2RBS5.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2RBS5.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32273873\",\"source\":\"PubMed\"}],\"value\":\"Fruiting body differentiation protein 30\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9BRQ8\",\"source\":\"UniProtKB\"}],\"value\":\"1.6.5.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"FAD-dependent oxidoreductase FVFD30\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:30:38.073015+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "beb3cfe391db72fc8866ae9445a0714bbe0a44d8c8a6074dc27c3819e066bff4",
  "url": "https://rest.uniprot.org/uniprotkb/Q2RBS5.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2RBS5.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":301},\"start\":{\"modifier\":\"EXACT\",\"value\":281}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:30:38.073015+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "beb3cfe391db72fc8866ae9445a0714bbe0a44d8c8a6074dc27c3819e066bff4",
  "url": "https://rest.uniprot.org/uniprotkb/Q2RBS5.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2RBS5.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Wu T.\",\"Zhang Z.\",\"Hu C.\",\"Zhang L.\",\"Wei S.\",\"Li S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"32273873\"},{\"database\":\"DOI\",\"id\":\"10.3389/fmicb.2020.00498\"}],\"citationType\":\"journal article\",\"firstPage\":\"498\",\"id\":\"32273873\",\"journal\":\"Front. Microbiol.\",\"lastPage\":\"498\",\"publicationDate\":\"2020\",\"title\":\"A WD40 Protein Encoding Gene Fvcpc2 Positively Regulates Mushroom Development and Yield in Flammulina velutipes.\",\"volume\":\"11\"},\"referenceNumber\":2,\"referencePositions\":[\"INDUCTION\",\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:30:38.073015+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "beb3cfe391db72fc8866ae9445a0714bbe0a44d8c8a6074dc27c3819e066bff4",
  "url": "https://rest.uniprot.org/uniprotkb/Q2RBS5.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2RBS5?format=txt&versions=64)

```json
{
  "entry_version": 64,
  "evidence_id": "H1",
  "excerpt": "ID   FD30_FLAVE              Reviewed;         319 AA.\nAC   Q2RBS5;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   24-JAN-2006, sequence version 1.\nDT   28-JAN-2026, entry version 64.\nDE   RecName: Full=FAD-dependent oxidoreductase FVFD30 {ECO:0000305};\nDE            EC=1.6.5.- {ECO:0000250|UniProtKB:Q9BRQ8};\nDE   AltName: Full=Fruiting body differentiation protein 30 {ECO:0000303|PubMed:32273873};\nGN   Name=FVFD30 {ECO:0000303|PubMed:32273873};\nOS   Flammulina velutipes (Agaricus velutipes).\nOC   Eukaryota; Fungi; Dikarya; Basidiomycota; Agaricomycotina; Agaricomycetes;\nOC   Agaricomycetidae; Agaricales; Marasmiineae; Physalacriaceae; Flammulina.\nOX   NCBI_TaxID=38945;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:40.650534+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "da35682d80cb6cef63c8793b0377fbe770f2acb9c2e203caa3a8ca7d0a0e8f97",
  "url": "https://rest.uniprot.org/unisave/Q2RBS5?format=txt&versions=64"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2RBS5?format=txt&versions=64)

```json
{
  "entry_version": 64,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   INDUCTION, AND FUNCTION.\nRX   PubMed=32273873; DOI=10.3389/fmicb.2020.00498;\nRA   Wu T., Zhang Z., Hu C., Zhang L., Wei S., Li S.;\nRT   \"A WD40 Protein Encoding Gene Fvcpc2 Positively Regulates Mushroom\nRT   Development and Yield in Flammulina velutipes.\";\nRL   Front. Microbiol. 11:498-498(2020).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:40.650534+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 21-27",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "da35682d80cb6cef63c8793b0377fbe770f2acb9c2e203caa3a8ca7d0a0e8f97",
  "url": "https://rest.uniprot.org/unisave/Q2RBS5?format=txt&versions=64"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2RBS5?format=txt&versions=64)

```json
{
  "entry_version": 64,
  "evidence_id": "H3",
  "excerpt": "FT   TRANSMEM        281..301\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:40.650534+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 63-65",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "da35682d80cb6cef63c8793b0377fbe770f2acb9c2e203caa3a8ca7d0a0e8f97",
  "url": "https://rest.uniprot.org/unisave/Q2RBS5?format=txt&versions=64"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 91. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
