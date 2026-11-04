# transmembrane_0057

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0057.txt)

**Task:** `transmembrane`  
**Expected answer:** **B** — 30..50; 62..82; 108..128; 144..164; 186..206; 327..347; 357..377

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTQLPYLLDRRGGALAAPATAWGDMMLNRALFSVALLSSVGSAWVVLSYACIKELRSYRHQLILGLAISDLLMSLNFMFSAGWNVAGGDLALEESRTACSVNGFLTQVFVVQTDWWILVIAIATYIILGNFKTQSQFIQTHVWIPWVGPWVLSIIIAAICHGVLGYGYIGGWCWLTSDLMRLLINFIPRWLIVIAIALIYIRLYMIVRKARKWDIEGVSPDPGDDMADTSVILMSVGKKDRERQGSGVLVSRDVSVSFGRKGSTAPTFVTMVTTSGAGDSREAISSCSAREEGSRARTVNVNSSRSLSLGMRQPLNAAQLKRIAKKMMVYPVAYAIIWACPTAIRIYQGTTGSRAPLWITIVDKSCIVIQGLVDAVVYGLNERAWQGWRDHIRRIIYKNEGGRIIG

[Multiple Choices]
A. 139..159; 176..196; 247..267; 272..292; 297..317
B. 30..50; 62..82; 108..128; 144..164; 186..206; 327..347; 357..377
C. 30..50; 62..82; 108..128; 144..164; 186..206; 327..347
D. 30..50; 62..82; 108..128; 144..164; 186..206; 328..343; 357..377
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

> The exact sequence matches UniProt records annotating all seven regions listed in B as transmembrane helices. The annotations are computationally supported (ECO:0000255), not direct experimental evidence of membrane crossing.

Citations as saved: [H4](#evidence-h4), [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has several strong hydrophobic stretches, including two near the C-terminus around the candidate regions 327..347 and 357..377. These are consistent with membrane-spanning helices; the long intervening region is comparatively nonhydrophobic. Thus B includes both plausible C-terminal spans, whereas C omits one and D gives a notably shortened interval for the first. Hydrophobic-segment recognition and the common multi-pass architecture of receptors provide transferable grounds for choosing B.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence itself supplies a meaningful hydrophobicity-based distinction among the choices; exact target-specific database recall is not necessary. Boundaries are predictions rather than experimentally established here.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives differ in whether they include the second C-terminal hydrophobic span and in the coverage of the preceding span; the sequence supports the two full intervals in B.


### Important caveats

- The cited UniProt transmembrane features are computationally supported annotations, not experimental measurements.
- The current and historical records match the supplied sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has several strong hydrophobic stretches, including two near the C-terminus around the candidate regions 327..347 and 357..377. These are consistent with membrane-spanning helices; the long intervening region is comparatively nonhydrophobic. Thus B includes both plausible C-terminal spans, whereas C omits one and D gives a notably shortened interval for the first. Hydrophobic-segment recognition and the common multi-pass architecture of receptors provide transferable grounds for choosing B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence itself supplies a meaningful hydrophobicity-based distinction among the choices; exact target-specific database recall is not necessary. Boundaries are predictions rather than experimentally established here."
  },
  "case_id": "transmembrane_0057",
  "expected_answer_check": {
    "evidence_ids": [
      "H4",
      "H6",
      "H8",
      "H10",
      "H12",
      "H14",
      "H16"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt records annotating all seven regions listed in B as transmembrane helices. The annotations are computationally supported (ECO:0000255), not direct experimental evidence of membrane crossing."
  },
  "important_caveats": [
    "The cited UniProt transmembrane features are computationally supported annotations, not experimental measurements.",
    "The current and historical records match the supplied sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives differ in whether they include the second C-terminal hydrophobic span and in the coverage of the preceding span; the sequence supports the two full intervals in B."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0057",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt records annotating all seven regions listed in B as transmembrane helices. The annotations are computationally supported (ECO:0000255), not direct experimental evidence of membrane crossing.",
    "evidence_ids": ["H4", "H6", "H8", "H10", "H12", "H14", "H16"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has several strong hydrophobic stretches, including two near the C-terminus around the candidate regions 327..347 and 357..377. These are consistent with membrane-spanning helices; the long intervening region is comparatively nonhydrophobic. Thus B includes both plausible C-terminal spans, whereas C omits one and D gives a notably shortened interval for the first. Hydrophobic-segment recognition and the common multi-pass architecture of receptors provide transferable grounds for choosing B.",
    "missing_item_specific_fact": "",
    "reason": "The sequence itself supplies a meaningful hydrophobicity-based distinction among the choices; exact target-specific database recall is not necessary. Boundaries are predictions rather than experimentally established here."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives differ in whether they include the second C-terminal hydrophobic span and in the coverage of the preceding span; the sequence supports the two full intervals in B."
  },
  "important_caveats": [
    "The cited UniProt transmembrane features are computationally supported annotations, not experimental measurements.",
    "The current and historical records match the supplied sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for G1X9E2 (Ascaroside receptor GPR2) lists exactly 7 transmembrane helices at positions 30..50, 62..82, 108..128, 144..164, 186..206, 327..347, and 357..377, matching option B exactly. The evidence codes are ECO:0000255 (by similarity), indicating computational/predicted annotations based on homology rather than experimental determination. However, the annotation is internally consistent with the sequence topology (alternating extracellular/cytoplasmic loops) and the 7TM GPCR architecture. The sequence match is confirmed (SHA256 identical, 406 AA).

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [H4](#evidence-h4), [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> This protein exhibits the hallmark architecture of a 7-transmembrane GPCR: multiple hydrophobic stretches of ~20 residues separated by hydrophilic loops, including a characteristically long third intracellular loop (~120 residues). The 7TM GPCR topology is among the most well-established facts in structural biology, learned from hundreds of characterized GPCRs. This eliminates option A (only 5 TM segments) and option C (only 6 TM segments). Distinguishing B from D requires knowledge that an alpha-helix must be at least ~19-21 residues to span the ~30 Å hydrophobic core of a lipid bilayer (at 1.5 Å/residue rise). Option D's sixth TM segment (328..343) is only 16 residues—physically too short to traverse the membrane—while option B's 327..347 (21 residues) is the standard length. The hydrophobic stretch around positions 327-347 in the sequence (containing residues like Y, P, V, A, Y, A, I, I, W, A, C, P, T, A, I, R, I, Y, Q, G, T) is clearly identifiable as a ~20+ residue hydrophobic segment, supporting the 21-residue assignment over the 16-residue one.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can apply the universally recognized 7TM GPCR architecture to eliminate options A and C, and apply the biophysical minimum helix length (~20 residues) for membrane spanning to eliminate option D's implausibly short 16-residue segment. These are well-established, transferable principles from hundreds of characterized GPCRs and basic membrane biophysics, not facts specific to this exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options are well-separated: A has 5 TMs (wrong count for GPCR), C has 6 TMs (wrong count), D has a 16-residue helix (physically too short), leaving B as the only option with 7 TMs of appropriate length. The biophysical constraint on minimum helix length clearly distinguishes B from D.


### Important caveats

- The UniProt transmembrane annotations carry evidence code ECO:0000255 (by similarity), meaning they are computational predictions based on homology to known GPCRs, not experimental measurements.
- The protein identity (Ascaroside receptor GPR2, a GPCR) was determined by reviewer-only UniProt lookup and was not provided to the evaluated model; however, the 7TM architecture is inferable from the sequence pattern itself.
- The long intracellular loop (positions 207-326, ~120 residues) is characteristic of GPCRs and helps confirm the 7TM topology from sequence alone.
- Option A's positions (139..159, etc.) appear to be deliberate ~5-residue shifts of the true TM positions, serving as a positional-shift distractor.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "This protein exhibits the hallmark architecture of a 7-transmembrane GPCR: multiple hydrophobic stretches of ~20 residues separated by hydrophilic loops, including a characteristically long third intracellular loop (~120 residues). The 7TM GPCR topology is among the most well-established facts in structural biology, learned from hundreds of characterized GPCRs. This eliminates option A (only 5 TM segments) and option C (only 6 TM segments). Distinguishing B from D requires knowledge that an alpha-helix must be at least ~19-21 residues to span the ~30 Å hydrophobic core of a lipid bilayer (at 1.5 Å/residue rise). Option D's sixth TM segment (328..343) is only 16 residues—physically too short to traverse the membrane—while option B's 327..347 (21 residues) is the standard length. The hydrophobic stretch around positions 327-347 in the sequence (containing residues like Y, P, V, A, Y, A, I, I, W, A, C, P, T, A, I, R, I, Y, Q, G, T) is clearly identifiable as a ~20+ residue hydrophobic segment, supporting the 21-residue assignment over the 16-residue one.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can apply the universally recognized 7TM GPCR architecture to eliminate options A and C, and apply the biophysical minimum helix length (~20 residues) for membrane spanning to eliminate option D's implausibly short 16-residue segment. These are well-established, transferable principles from hundreds of characterized GPCRs and basic membrane biophysics, not facts specific to this exact protein."
  },
  "case_id": "transmembrane_0057",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C8",
      "C10",
      "C12",
      "C14",
      "C16",
      "C18",
      "H4",
      "H6",
      "H8",
      "H10",
      "H12",
      "H14",
      "H16"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for G1X9E2 (Ascaroside receptor GPR2) lists exactly 7 transmembrane helices at positions 30..50, 62..82, 108..128, 144..164, 186..206, 327..347, and 357..377, matching option B exactly. The evidence codes are ECO:0000255 (by similarity), indicating computational/predicted annotations based on homology rather than experimental determination. However, the annotation is internally consistent with the sequence topology (alternating extracellular/cytoplasmic loops) and the 7TM GPCR architecture. The sequence match is confirmed (SHA256 identical, 406 AA)."
  },
  "important_caveats": [
    "The UniProt transmembrane annotations carry evidence code ECO:0000255 (by similarity), meaning they are computational predictions based on homology to known GPCRs, not experimental measurements.",
    "The protein identity (Ascaroside receptor GPR2, a GPCR) was determined by reviewer-only UniProt lookup and was not provided to the evaluated model; however, the 7TM architecture is inferable from the sequence pattern itself.",
    "The long intracellular loop (positions 207-326, ~120 residues) is characteristic of GPCRs and helps confirm the 7TM topology from sequence alone.",
    "Option A's positions (139..159, etc.) appear to be deliberate ~5-residue shifts of the true TM positions, serving as a positional-shift distractor."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options are well-separated: A has 5 TMs (wrong count for GPCR), C has 6 TMs (wrong count), D has a 16-residue helix (physically too short), leaving B as the only option with 7 TMs of appropriate length. The biophysical constraint on minimum helix length clearly distinguishes B from D."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0057",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for G1X9E2 (Ascaroside receptor GPR2) lists exactly 7 transmembrane helices at positions 30..50, 62..82, 108..128, 144..164, 186..206, 327..347, and 357..377, matching option B exactly. The evidence codes are ECO:0000255 (by similarity), indicating computational/predicted annotations based on homology rather than experimental determination. However, the annotation is internally consistent with the sequence topology (alternating extracellular/cytoplasmic loops) and the 7TM GPCR architecture. The sequence match is confirmed (SHA256 identical, 406 AA).",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "H4", "H6", "H8", "H10", "H12", "H14", "H16"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "This protein exhibits the hallmark architecture of a 7-transmembrane GPCR: multiple hydrophobic stretches of ~20 residues separated by hydrophilic loops, including a characteristically long third intracellular loop (~120 residues). The 7TM GPCR topology is among the most well-established facts in structural biology, learned from hundreds of characterized GPCRs. This eliminates option A (only 5 TM segments) and option C (only 6 TM segments). Distinguishing B from D requires knowledge that an alpha-helix must be at least ~19-21 residues to span the ~30 Å hydrophobic core of a lipid bilayer (at 1.5 Å/residue rise). Option D's sixth TM segment (328..343) is only 16 residues—physically too short to traverse the membrane—while option B's 327..347 (21 residues) is the standard length. The hydrophobic stretch around positions 327-347 in the sequence (containing residues like Y, P, V, A, Y, A, I, I, W, A, C, P, T, A, I, R, I, Y, Q, G, T) is clearly identifiable as a ~20+ residue hydrophobic segment, supporting the 21-residue assignment over the 16-residue one.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can apply the universally recognized 7TM GPCR architecture to eliminate options A and C, and apply the biophysical minimum helix length (~20 residues) for membrane spanning to eliminate option D's implausibly short 16-residue segment. These are well-established, transferable principles from hundreds of characterized GPCRs and basic membrane biophysics, not facts specific to this exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options are well-separated: A has 5 TMs (wrong count for GPCR), C has 6 TMs (wrong count), D has a 16-residue helix (physically too short), leaving B as the only option with 7 TMs of appropriate length. The biophysical constraint on minimum helix length clearly distinguishes B from D."
  },
  "important_caveats": [
    "The UniProt transmembrane annotations carry evidence code ECO:0000255 (by similarity), meaning they are computational predictions based on homology to known GPCRs, not experimental measurements.",
    "The protein identity (Ascaroside receptor GPR2, a GPCR) was determined by reviewer-only UniProt lookup and was not provided to the evaluated model; however, the 7TM architecture is inferable from the sequence pattern itself.",
    "The long intracellular loop (positions 207-326, ~120 residues) is characteristic of GPCRs and helps confirm the 7TM topology from sequence alone.",
    "Option A's positions (139..159, etc.) appear to be deliberate ~5-residue shifts of the true TM positions, serving as a positional-shift distractor."
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
  "benchmark_sequence_length": 406,
  "benchmark_sequence_sha256": "4e764ad5fe8865d73836f34a410857326f248f960936c909cff720a56696f0f3",
  "current_entry_audit": {
    "entryVersion": 47,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2011-11-16",
    "sequenceVersion": 1
  },
  "current_record_sha256": "d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 406,
  "current_source_sequence_sha256": "4e764ad5fe8865d73836f34a410857326f248f960936c909cff720a56696f0f3",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 45,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "G1X9E2",
  "selected_historical_entry_version": 45,
  "selected_historical_record_sha256": "e35d509b45ea64e3eac1fedae5691280c0fa8c7205a8651df542bc73ee054a3f",
  "selected_historical_source_sequence_length": 406,
  "selected_historical_source_sequence_sha256": "4e764ad5fe8865d73836f34a410857326f248f960936c909cff720a56696f0f3",
  "selected_historical_version": {
    "accession": "G1X9E2",
    "database": "Swiss-Prot",
    "entryVersion": 45,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "GPR2_ARTOA",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"G1X9E2\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:28:30.739464+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f",
  "url": "https://rest.uniprot.org/uniprotkb/G1X9E2.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":47,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2011-11-16\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:28:30.739464+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f",
  "url": "https://rest.uniprot.org/uniprotkb/G1X9E2.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Nematode-trapping fungus\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000008784\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Orbiliomycetes\",\"Orbiliales\",\"Orbiliaceae\",\"Orbilia\",\"Orbilia oligospora\"],\"scientificName\":\"Arthrobotrys oligospora (strain ATCC 24927 / CBS 115.81 / DSM 1491)\",\"synonyms\":[\"Didymozoophaga oligospora\"],\"taxonId\":756982}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:28:30.739464+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f",
  "url": "https://rest.uniprot.org/uniprotkb/G1X9E2.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Ascaroside receptor GPR2\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:28:30.739464+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f",
  "url": "https://rest.uniprot.org/uniprotkb/G1X9E2.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":29},\"start\":{\"modifier\":\"EXACT\",\"value\":1}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:28:30.739464+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f",
  "url": "https://rest.uniprot.org/uniprotkb/G1X9E2.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":50},\"start\":{\"modifier\":\"EXACT\",\"value\":30}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:28:30.739464+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f",
  "url": "https://rest.uniprot.org/uniprotkb/G1X9E2.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":61},\"start\":{\"modifier\":\"EXACT\",\"value\":51}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:28:30.739464+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f",
  "url": "https://rest.uniprot.org/uniprotkb/G1X9E2.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":82},\"start\":{\"modifier\":\"EXACT\",\"value\":62}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:28:30.739464+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f",
  "url": "https://rest.uniprot.org/uniprotkb/G1X9E2.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":107},\"start\":{\"modifier\":\"EXACT\",\"value\":83}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:28:30.739464+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f",
  "url": "https://rest.uniprot.org/uniprotkb/G1X9E2.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":128},\"start\":{\"modifier\":\"EXACT\",\"value\":108}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:28:30.739464+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f",
  "url": "https://rest.uniprot.org/uniprotkb/G1X9E2.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":143},\"start\":{\"modifier\":\"EXACT\",\"value\":129}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:28:30.739464+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f",
  "url": "https://rest.uniprot.org/uniprotkb/G1X9E2.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":164},\"start\":{\"modifier\":\"EXACT\",\"value\":144}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:28:30.739464+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f",
  "url": "https://rest.uniprot.org/uniprotkb/G1X9E2.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":185},\"start\":{\"modifier\":\"EXACT\",\"value\":165}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-02T04:28:30.739464+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f",
  "url": "https://rest.uniprot.org/uniprotkb/G1X9E2.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":206},\"start\":{\"modifier\":\"EXACT\",\"value\":186}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-02T04:28:30.739464+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f",
  "url": "https://rest.uniprot.org/uniprotkb/G1X9E2.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":326},\"start\":{\"modifier\":\"EXACT\",\"value\":207}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/11",
  "retrieved_utc": "2026-11-02T04:28:30.739464+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f",
  "url": "https://rest.uniprot.org/uniprotkb/G1X9E2.json"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)

```json
{
  "evidence_id": "C16",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":347},\"start\":{\"modifier\":\"EXACT\",\"value\":327}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/12",
  "retrieved_utc": "2026-11-02T04:28:30.739464+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f",
  "url": "https://rest.uniprot.org/uniprotkb/G1X9E2.json"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)

```json
{
  "evidence_id": "C17",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":356},\"start\":{\"modifier\":\"EXACT\",\"value\":348}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/13",
  "retrieved_utc": "2026-11-02T04:28:30.739464+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f",
  "url": "https://rest.uniprot.org/uniprotkb/G1X9E2.json"
}
```

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)

```json
{
  "evidence_id": "C18",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":377},\"start\":{\"modifier\":\"EXACT\",\"value\":357}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/14",
  "retrieved_utc": "2026-11-02T04:28:30.739464+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f",
  "url": "https://rest.uniprot.org/uniprotkb/G1X9E2.json"
}
```

### Evidence C19

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)

```json
{
  "evidence_id": "C19",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":406},\"start\":{\"modifier\":\"EXACT\",\"value\":378}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/15",
  "retrieved_utc": "2026-11-02T04:28:30.739464+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f",
  "url": "https://rest.uniprot.org/uniprotkb/G1X9E2.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45)

```json
{
  "entry_version": 45,
  "evidence_id": "H1",
  "excerpt": "ID   GPR2_ARTOA              Reviewed;         406 AA.\nAC   G1X9E2;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   16-NOV-2011, sequence version 1.\nDT   28-JAN-2026, entry version 45.\nDE   RecName: Full=Ascaroside receptor GPR2 {ECO:0000305};\nGN   Name=GPR2 {ECO:0000303|PubMed:38649409};\nGN   ORFNames=AOL_s00076g249 {ECO:0000312|EMBL:EGX50174.1};\nOS   Arthrobotrys oligospora (strain ATCC 24927 / CBS 115.81 / DSM 1491)\nOS   (Nematode-trapping fungus) (Didymozoophaga oligospora).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Orbiliomycetes;\nOC   Orbiliales; Orbiliaceae; Orbilia; Orbilia oligospora.\nOX   NCBI_TaxID=756982 {ECO:0000312|Proteomes:UP000008784};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:32.723564+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e35d509b45ea64e3eac1fedae5691280c0fa8c7205a8651df542bc73ee054a3f",
  "url": "https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45)

```json
{
  "entry_version": 45,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, INTERACTION WITH GPA2 AND GPR3, SUBCELLULAR LOCATION, INDUCTION,\nRP   AND DISRUPTION PHENOTYPE.\nRC   STRAIN=TWF154 {ECO:0000303|PubMed:38649409};\nRX   PubMed=38649409; DOI=10.1038/s41564-024-01679-w;\nRA   Kuo C.Y., Tay R.J., Lin H.C., Juan S.C., Vidal-Diez de Ulzurrun G.,\nRA   Chang Y.C., Hoki J., Schroeder F.C., Hsueh Y.P.;\nRT   \"The nematode-trapping fungus Arthrobotrys oligospora detects prey\nRT   pheromones via G protein-coupled receptors.\";\nRL   Nat. Microbiol. 9:1738-1751(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:32.723564+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 25-34",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e35d509b45ea64e3eac1fedae5691280c0fa8c7205a8651df542bc73ee054a3f",
  "url": "https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45)

```json
{
  "entry_version": 45,
  "evidence_id": "H3",
  "excerpt": "FT   TOPO_DOM        1..29\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:32.723564+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 94-96",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e35d509b45ea64e3eac1fedae5691280c0fa8c7205a8651df542bc73ee054a3f",
  "url": "https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45)

```json
{
  "entry_version": 45,
  "evidence_id": "H4",
  "excerpt": "FT   TRANSMEM        30..50\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:32.723564+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 97-99",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e35d509b45ea64e3eac1fedae5691280c0fa8c7205a8651df542bc73ee054a3f",
  "url": "https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45)

```json
{
  "entry_version": 45,
  "evidence_id": "H5",
  "excerpt": "FT   TOPO_DOM        51..61\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:32.723564+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 100-102",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e35d509b45ea64e3eac1fedae5691280c0fa8c7205a8651df542bc73ee054a3f",
  "url": "https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45)

```json
{
  "entry_version": 45,
  "evidence_id": "H6",
  "excerpt": "FT   TRANSMEM        62..82\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:32.723564+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 103-105",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e35d509b45ea64e3eac1fedae5691280c0fa8c7205a8651df542bc73ee054a3f",
  "url": "https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45)

```json
{
  "entry_version": 45,
  "evidence_id": "H7",
  "excerpt": "FT   TOPO_DOM        83..107\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:32.723564+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 106-108",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e35d509b45ea64e3eac1fedae5691280c0fa8c7205a8651df542bc73ee054a3f",
  "url": "https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45)

```json
{
  "entry_version": 45,
  "evidence_id": "H8",
  "excerpt": "FT   TRANSMEM        108..128\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:32.723564+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 109-111",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e35d509b45ea64e3eac1fedae5691280c0fa8c7205a8651df542bc73ee054a3f",
  "url": "https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45)

```json
{
  "entry_version": 45,
  "evidence_id": "H9",
  "excerpt": "FT   TOPO_DOM        129..143\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:32.723564+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 112-114",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e35d509b45ea64e3eac1fedae5691280c0fa8c7205a8651df542bc73ee054a3f",
  "url": "https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45)

```json
{
  "entry_version": 45,
  "evidence_id": "H10",
  "excerpt": "FT   TRANSMEM        144..164\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:32.723564+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 115-117",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e35d509b45ea64e3eac1fedae5691280c0fa8c7205a8651df542bc73ee054a3f",
  "url": "https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45)

```json
{
  "entry_version": 45,
  "evidence_id": "H11",
  "excerpt": "FT   TOPO_DOM        165..185\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:32.723564+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 118-120",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e35d509b45ea64e3eac1fedae5691280c0fa8c7205a8651df542bc73ee054a3f",
  "url": "https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45)

```json
{
  "entry_version": 45,
  "evidence_id": "H12",
  "excerpt": "FT   TRANSMEM        186..206\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:32.723564+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 121-123",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e35d509b45ea64e3eac1fedae5691280c0fa8c7205a8651df542bc73ee054a3f",
  "url": "https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45)

```json
{
  "entry_version": 45,
  "evidence_id": "H13",
  "excerpt": "FT   TOPO_DOM        207..326\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:32.723564+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 124-126",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e35d509b45ea64e3eac1fedae5691280c0fa8c7205a8651df542bc73ee054a3f",
  "url": "https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45)

```json
{
  "entry_version": 45,
  "evidence_id": "H14",
  "excerpt": "FT   TRANSMEM        327..347\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:32.723564+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 127-129",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e35d509b45ea64e3eac1fedae5691280c0fa8c7205a8651df542bc73ee054a3f",
  "url": "https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45"
}
```

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45)

```json
{
  "entry_version": 45,
  "evidence_id": "H15",
  "excerpt": "FT   TOPO_DOM        348..356\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:32.723564+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 130-132",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e35d509b45ea64e3eac1fedae5691280c0fa8c7205a8651df542bc73ee054a3f",
  "url": "https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45"
}
```

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45)

```json
{
  "entry_version": 45,
  "evidence_id": "H16",
  "excerpt": "FT   TRANSMEM        357..377\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:32.723564+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 133-135",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e35d509b45ea64e3eac1fedae5691280c0fa8c7205a8651df542bc73ee054a3f",
  "url": "https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45"
}
```

### Evidence H17

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45)

```json
{
  "entry_version": 45,
  "evidence_id": "H17",
  "excerpt": "FT   TOPO_DOM        378..406\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:32.723564+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 136-138",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e35d509b45ea64e3eac1fedae5691280c0fa8c7205a8651df542bc73ee054a3f",
  "url": "https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 57. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
