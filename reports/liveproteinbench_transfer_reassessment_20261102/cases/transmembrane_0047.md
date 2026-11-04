# transmembrane_0047

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0047.txt)

**Task:** `transmembrane`  
**Expected answer:** **B** — 249..269; 302..322

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MQQTAALPKRLSCDRCYAQKLRCPRPSTNDDASCIRCLRQKVQCVYSTALPKGRPRAAVRACAAGAGATAGAPPITTTTTTAAPSSSDTAPPIFSTEDLASLTGLSTSGWLPDPTWEDSFCFLSSQVVPQPPPLDTTPPPRSLSASGLDNPENCVGRLSDLATRLHAVYQTTRALSDHPLITNAAFEAVTTLFNAPLSPPSAATTAATTNLRETFTSSRHLLETISHLLWATPNNNPSTAPAAAADETVIYHFTIACYSLLLLIYATLLTALHRDALTHTQPSLSTTTTTTGPDNNTSTWCSAPSLVELRLVLLFHMITYFLDRLQQMIRMYTAEFEKQASNSTTGRRPPTSGRWSEEVEEMMVVEEPWEREQHIPPPPPPTSSLGSISELETQARAALMQLRMSLVATRGGLVDN

[Multiple Choices]
A. 249..269
B. 249..269; 302..322
C. 14..34
D. 249..269; 304..319
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

> The sequence-matched UniProt entry annotates helical transmembrane regions at 249–269 and 302–322, matching choice B. These annotations are computational (ECO:0000255), so they support the key as a prediction but do not establish experimental validation.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains two candidate membrane-spanning hydrophobic helical stretches at the listed positions, each about 20 residues long—typical of transmembrane alpha helices. That makes B more plausible than A, which omits one stretch, or C, which points to the cysteine-rich N-terminus. D gives a shorter subrange of the second candidate rather than its likely full membrane-spanning span.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Hydropathy and expected transmembrane-helix length provide a transferable basis for distinguishing B among these choices. Exact boundaries remain less certain from sequence alone than the presence of the two candidate helices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although predicted helix boundaries can be uncertain, B offers the more plausible full-length spans; D's shorter second interval is less consistent with a complete membrane-crossing helix.


### Important caveats

- The cited database annotations are computational, not experimental evidence.
- Sequence-based prediction does not guarantee that either region spans a membrane in vivo.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains two candidate membrane-spanning hydrophobic helical stretches at the listed positions, each about 20 residues long—typical of transmembrane alpha helices. That makes B more plausible than A, which omits one stretch, or C, which points to the cysteine-rich N-terminus. D gives a shorter subrange of the second candidate rather than its likely full membrane-spanning span.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Hydropathy and expected transmembrane-helix length provide a transferable basis for distinguishing B among these choices. Exact boundaries remain less certain from sequence alone than the presence of the two candidate helices."
  },
  "case_id": "transmembrane_0047",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates helical transmembrane regions at 249–269 and 302–322, matching choice B. These annotations are computational (ECO:0000255), so they support the key as a prediction but do not establish experimental validation."
  },
  "important_caveats": [
    "The cited database annotations are computational, not experimental evidence.",
    "Sequence-based prediction does not guarantee that either region spans a membrane in vivo."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although predicted helix boundaries can be uncertain, B offers the more plausible full-length spans; D's shorter second interval is less consistent with a complete membrane-crossing helix."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0047",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates helical transmembrane regions at 249–269 and 302–322, matching choice B. These annotations are computational (ECO:0000255), so they support the key as a prediction but do not establish experimental validation.",
    "evidence_ids": ["C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains two candidate membrane-spanning hydrophobic helical stretches at the listed positions, each about 20 residues long—typical of transmembrane alpha helices. That makes B more plausible than A, which omits one stretch, or C, which points to the cysteine-rich N-terminus. D gives a shorter subrange of the second candidate rather than its likely full membrane-spanning span.",
    "missing_item_specific_fact": "",
    "reason": "Hydropathy and expected transmembrane-helix length provide a transferable basis for distinguishing B among these choices. Exact boundaries remain less certain from sequence alone than the presence of the two candidate helices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although predicted helix boundaries can be uncertain, B offers the more plausible full-length spans; D's shorter second interval is less consistent with a complete membrane-crossing helix."
  },
  "important_caveats": [
    "The cited database annotations are computational, not experimental evidence.",
    "Sequence-based prediction does not guarantee that either region spans a membrane in vivo."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A2QQU8 annotates exactly two transmembrane helical regions: 249..269 and 302..322, both with evidence code ECO:0000255 (similarity/probability-based computational prediction). This matches option B precisely. The annotation is computational rather than experimental, but it is the recorded database fact that the expected answer reflects.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Several transferable principles allow meaningful discrimination among the four choices. (1) Option C (14..34: DRCYAQKLRCPRPSTNDDASC) is trivially eliminated because it is dominated by charged and polar residues (D, R, K, R, C, P, S, N, D) with no hydrophobic stretch—no TM helix can form here. (2) Option A vs B: The region around 249–269 (VIYHFTIACYSLLLLIYATLL) is an unambiguous hydrophobic alpha-helix candidate. A second hydrophobic stretch exists around 306–321 (LVLLFHMITYFL), flanked by mildly polar residues, consistent with a second TM helix. A model performing hydrophobicity scanning would plausibly identify two segments rather than one. (3) The critical B-vs-D discrimination rests on a well-established biophysical constraint: a lipid bilayer hydrophobic core is ~30 Å thick, requiring roughly 20 residues in an α-helix (1.5 Å/residue). Option D's second segment (304..319) is only 16 residues (≈24 Å), too short to span the bilayer, whereas option B's 21-residue segment (302..322) falls within the canonical 18–25-residue TM-helix range. This length criterion is textbook knowledge applicable to any membrane protein and directly distinguishes B from D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The length-of-TM-helix constraint (≥~20 residues to span the bilayer) is a fundamental, transferable biophysical principle that cleanly separates B (21-residue second helix) from D (16-residue, too short). Hydrophobicity analysis of the sequence supports identifying two hydrophobic stretches and eliminates C. While the second TM region is borderline in hydrophobicity (containing E, R, S, P), the combination of the length argument and the hydrophobic core LVLLFHMITYFL provides a credible basis for selecting B over A and D without needing to look up this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option C is clearly wrong (charged region). Option A is less defensible because a second hydrophobic stretch is identifiable by sequence scanning. Option D is undermined by the 16-residue length being below the minimum for bilayer spanning. Option B is the most defensible answer on both hydrophobicity and biophysical-length grounds.


### Important caveats

- The UniProt TM annotations carry evidence code ECO:0000255, indicating computational/similarity-based prediction rather than experimental determination.
- The second TM region (302–322) is borderline in hydrophobicity, containing polar/charged residues (S, A, P, E, R) alongside hydrophobic ones; a strict hydrophobicity threshold might not flag it, making A a partially defensible but weaker choice.
- The task prompt says 'a segment' (singular) but the options include multi-segment answers, creating minor wording ambiguity that does not change the correct answer.
- The reviewer-only evidence confirms sequence match (416 AA, SHA-256 identical) between the benchmark sequence and UniProt A2QQU8, so the annotation applies to this exact sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Several transferable principles allow meaningful discrimination among the four choices. (1) Option C (14..34: DRCYAQKLRCPRPSTNDDASC) is trivially eliminated because it is dominated by charged and polar residues (D, R, K, R, C, P, S, N, D) with no hydrophobic stretch—no TM helix can form here. (2) Option A vs B: The region around 249–269 (VIYHFTIACYSLLLLIYATLL) is an unambiguous hydrophobic alpha-helix candidate. A second hydrophobic stretch exists around 306–321 (LVLLFHMITYFL), flanked by mildly polar residues, consistent with a second TM helix. A model performing hydrophobicity scanning would plausibly identify two segments rather than one. (3) The critical B-vs-D discrimination rests on a well-established biophysical constraint: a lipid bilayer hydrophobic core is ~30 Å thick, requiring roughly 20 residues in an α-helix (1.5 Å/residue). Option D's second segment (304..319) is only 16 residues (≈24 Å), too short to span the bilayer, whereas option B's 21-residue segment (302..322) falls within the canonical 18–25-residue TM-helix range. This length criterion is textbook knowledge applicable to any membrane protein and directly distinguishes B from D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The length-of-TM-helix constraint (≥~20 residues to span the bilayer) is a fundamental, transferable biophysical principle that cleanly separates B (21-residue second helix) from D (16-residue, too short). Hydrophobicity analysis of the sequence supports identifying two hydrophobic stretches and eliminates C. While the second TM region is borderline in hydrophobicity (containing E, R, S, P), the combination of the length argument and the hydrophobic core LVLLFHMITYFL provides a credible basis for selecting B over A and D without needing to look up this specific protein's database entry."
  },
  "case_id": "transmembrane_0047",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A2QQU8 annotates exactly two transmembrane helical regions: 249..269 and 302..322, both with evidence code ECO:0000255 (similarity/probability-based computational prediction). This matches option B precisely. The annotation is computational rather than experimental, but it is the recorded database fact that the expected answer reflects."
  },
  "important_caveats": [
    "The UniProt TM annotations carry evidence code ECO:0000255, indicating computational/similarity-based prediction rather than experimental determination.",
    "The second TM region (302–322) is borderline in hydrophobicity, containing polar/charged residues (S, A, P, E, R) alongside hydrophobic ones; a strict hydrophobicity threshold might not flag it, making A a partially defensible but weaker choice.",
    "The task prompt says 'a segment' (singular) but the options include multi-segment answers, creating minor wording ambiguity that does not change the correct answer.",
    "The reviewer-only evidence confirms sequence match (416 AA, SHA-256 identical) between the benchmark sequence and UniProt A2QQU8, so the annotation applies to this exact sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C is clearly wrong (charged region). Option A is less defensible because a second hydrophobic stretch is identifiable by sequence scanning. Option D is undermined by the 16-residue length being below the minimum for bilayer spanning. Option B is the most defensible answer on both hydrophobicity and biophysical-length grounds."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0047",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A2QQU8 annotates exactly two transmembrane helical regions: 249..269 and 302..322, both with evidence code ECO:0000255 (similarity/probability-based computational prediction). This matches option B precisely. The annotation is computational rather than experimental, but it is the recorded database fact that the expected answer reflects.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Several transferable principles allow meaningful discrimination among the four choices. (1) Option C (14..34: DRCYAQKLRCPRPSTNDDASC) is trivially eliminated because it is dominated by charged and polar residues (D, R, K, R, C, P, S, N, D) with no hydrophobic stretch—no TM helix can form here. (2) Option A vs B: The region around 249–269 (VIYHFTIACYSLLLLIYATLL) is an unambiguous hydrophobic alpha-helix candidate. A second hydrophobic stretch exists around 306–321 (LVLLFHMITYFL), flanked by mildly polar residues, consistent with a second TM helix. A model performing hydrophobicity scanning would plausibly identify two segments rather than one. (3) The critical B-vs-D discrimination rests on a well-established biophysical constraint: a lipid bilayer hydrophobic core is ~30 Å thick, requiring roughly 20 residues in an α-helix (1.5 Å/residue). Option D's second segment (304..319) is only 16 residues (≈24 Å), too short to span the bilayer, whereas option B's 21-residue segment (302..322) falls within the canonical 18–25-residue TM-helix range. This length criterion is textbook knowledge applicable to any membrane protein and directly distinguishes B from D.",
    "missing_item_specific_fact": "",
    "reason": "The length-of-TM-helix constraint (≥~20 residues to span the bilayer) is a fundamental, transferable biophysical principle that cleanly separates B (21-residue second helix) from D (16-residue, too short). Hydrophobicity analysis of the sequence supports identifying two hydrophobic stretches and eliminates C. While the second TM region is borderline in hydrophobicity (containing E, R, S, P), the combination of the length argument and the hydrophobic core LVLLFHMITYFL provides a credible basis for selecting B over A and D without needing to look up this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C is clearly wrong (charged region). Option A is less defensible because a second hydrophobic stretch is identifiable by sequence scanning. Option D is undermined by the 16-residue length being below the minimum for bilayer spanning. Option B is the most defensible answer on both hydrophobicity and biophysical-length grounds."
  },
  "important_caveats": [
    "The UniProt TM annotations carry evidence code ECO:0000255, indicating computational/similarity-based prediction rather than experimental determination.",
    "The second TM region (302–322) is borderline in hydrophobicity, containing polar/charged residues (S, A, P, E, R) alongside hydrophobic ones; a strict hydrophobicity threshold might not flag it, making A a partially defensible but weaker choice.",
    "The task prompt says 'a segment' (singular) but the options include multi-segment answers, creating minor wording ambiguity that does not change the correct answer.",
    "The reviewer-only evidence confirms sequence match (416 AA, SHA-256 identical) between the benchmark sequence and UniProt A2QQU8, so the annotation applies to this exact sequence."
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
  "benchmark_sequence_length": 416,
  "benchmark_sequence_sha256": "ef7f0a641c909ab5a20bdd0e3049a677a6aa08cb311aa2a01ea9efecd2e34ffc",
  "current_entry_audit": {
    "entryVersion": 90,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2007-03-06",
    "sequenceVersion": 1
  },
  "current_record_sha256": "048c50007e74b0eaedcdeda2b2ba8f9654f5c7777a1f60d624cc567a63d1304d",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 416,
  "current_source_sequence_sha256": "ef7f0a641c909ab5a20bdd0e3049a677a6aa08cb311aa2a01ea9efecd2e34ffc",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 88,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A2QQU8",
  "selected_historical_entry_version": 88,
  "selected_historical_record_sha256": "8a15f0dda8a8cf133195a7f63b16d97c1e66a816907b2ecf92cfc388cd42b61a",
  "selected_historical_source_sequence_length": 416,
  "selected_historical_source_sequence_sha256": "ef7f0a641c909ab5a20bdd0e3049a677a6aa08cb311aa2a01ea9efecd2e34ffc",
  "selected_historical_version": {
    "accession": "A2QQU8",
    "database": "Swiss-Prot",
    "entryVersion": 88,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CAAR_ASPNC",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A2QQU8.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A2QQU8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:26:53.819868+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "048c50007e74b0eaedcdeda2b2ba8f9654f5c7777a1f60d624cc567a63d1304d",
  "url": "https://rest.uniprot.org/uniprotkb/A2QQU8.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A2QQU8.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":90,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2007-03-06\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:26:53.819868+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "048c50007e74b0eaedcdeda2b2ba8f9654f5c7777a1f60d624cc567a63d1304d",
  "url": "https://rest.uniprot.org/uniprotkb/A2QQU8.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A2QQU8.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Aspergillus\",\"Circumdati\"],\"scientificName\":\"Aspergillus niger (strain ATCC MYA-4892 / CBS 513.88 / FGSC A1513)\",\"taxonId\":425011}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:26:53.819868+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "048c50007e74b0eaedcdeda2b2ba8f9654f5c7777a1f60d624cc567a63d1304d",
  "url": "https://rest.uniprot.org/uniprotkb/A2QQU8.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A2QQU8.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"25044953\",\"source\":\"PubMed\"}],\"value\":\"Carlosic acid biosynthesis cluster regulator\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"25044953\",\"source\":\"PubMed\"}],\"value\":\"Transcription factor caaR\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:26:53.819868+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "048c50007e74b0eaedcdeda2b2ba8f9654f5c7777a1f60d624cc567a63d1304d",
  "url": "https://rest.uniprot.org/uniprotkb/A2QQU8.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A2QQU8.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":269},\"start\":{\"modifier\":\"EXACT\",\"value\":249}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:26:53.819868+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "048c50007e74b0eaedcdeda2b2ba8f9654f5c7777a1f60d624cc567a63d1304d",
  "url": "https://rest.uniprot.org/uniprotkb/A2QQU8.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A2QQU8.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":322},\"start\":{\"modifier\":\"EXACT\",\"value\":302}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:26:53.819868+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "048c50007e74b0eaedcdeda2b2ba8f9654f5c7777a1f60d624cc567a63d1304d",
  "url": "https://rest.uniprot.org/uniprotkb/A2QQU8.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A2QQU8.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Yang X.L.\",\"Awakawa T.\",\"Wakimoto T.\",\"Abe I.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"25044953\"},{\"database\":\"DOI\",\"id\":\"10.1002/cbic.201402172\"}],\"citationType\":\"journal article\",\"firstPage\":\"1578\",\"id\":\"25044953\",\"journal\":\"ChemBioChem\",\"lastPage\":\"1583\",\"publicationDate\":\"2014\",\"title\":\"Three acyltetronic acid derivatives: noncanonical cryptic polyketides from Aspergillus niger identified by genome mining.\",\"volume\":\"15\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:26:53.819868+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "048c50007e74b0eaedcdeda2b2ba8f9654f5c7777a1f60d624cc567a63d1304d",
  "url": "https://rest.uniprot.org/uniprotkb/A2QQU8.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A2QQU8?format=txt&versions=88)

```json
{
  "entry_version": 88,
  "evidence_id": "H1",
  "excerpt": "ID   CAAR_ASPNC              Reviewed;         416 AA.\nAC   A2QQU8;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   06-MAR-2007, sequence version 1.\nDT   28-JAN-2026, entry version 88.\nDE   RecName: Full=Transcription factor caaR {ECO:0000303|PubMed:25044953};\nDE   AltName: Full=Carlosic acid biosynthesis cluster regulator {ECO:0000303|PubMed:25044953};\nGN   Name=caaR {ECO:0000303|PubMed:25044953}; ORFNames=An08g03770;\nOS   Aspergillus niger (strain ATCC MYA-4892 / CBS 513.88 / FGSC A1513).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;\nOC   Aspergillus subgen. Circumdati.\nOX   NCBI_TaxID=425011;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:00.244329+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8a15f0dda8a8cf133195a7f63b16d97c1e66a816907b2ecf92cfc388cd42b61a",
  "url": "https://rest.uniprot.org/unisave/A2QQU8?format=txt&versions=88"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A2QQU8?format=txt&versions=88)

```json
{
  "entry_version": 88,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION.\nRX   PubMed=25044953; DOI=10.1002/cbic.201402172;\nRA   Yang X.L., Awakawa T., Wakimoto T., Abe I.;\nRT   \"Three acyltetronic acid derivatives: noncanonical cryptic polyketides from\nRT   Aspergillus niger identified by genome mining.\";\nRL   ChemBioChem 15:1578-1583(2014).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:00.244329+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 35-41",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8a15f0dda8a8cf133195a7f63b16d97c1e66a816907b2ecf92cfc388cd42b61a",
  "url": "https://rest.uniprot.org/unisave/A2QQU8?format=txt&versions=88"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A2QQU8?format=txt&versions=88)

```json
{
  "entry_version": 88,
  "evidence_id": "H3",
  "excerpt": "FT   TRANSMEM        249..269\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:00.244329+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 81-83",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8a15f0dda8a8cf133195a7f63b16d97c1e66a816907b2ecf92cfc388cd42b61a",
  "url": "https://rest.uniprot.org/unisave/A2QQU8?format=txt&versions=88"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A2QQU8?format=txt&versions=88)

```json
{
  "entry_version": 88,
  "evidence_id": "H4",
  "excerpt": "FT   TRANSMEM        302..322\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:00.244329+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 84-86",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8a15f0dda8a8cf133195a7f63b16d97c1e66a816907b2ecf92cfc388cd42b61a",
  "url": "https://rest.uniprot.org/unisave/A2QQU8?format=txt&versions=88"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 47. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
