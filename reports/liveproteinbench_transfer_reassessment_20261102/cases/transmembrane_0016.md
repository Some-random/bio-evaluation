# transmembrane_0016

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0016.txt)

**Task:** `transmembrane`  
**Expected answer:** **A** — 13..35

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MASEIYRRLPMELPAQHLLASLALVGALLSVGYLLLRPAKYQLPLPPGPRGLPIIGNLHQAPKEKAWEVYKQWSDRYGPIMSVNNGGMITIIVSSHEVVKNFLEKNNAVFSSRPQLLVLERALYGFTTPALPYGEKWLKHRALRGAVLKPAMAVRYRGLQDLESKQLLRDLLYSEDFTQCMRRQAASLFLGIAYGNRFPEETPEIIDIDQAVAQLGGISESMFQGTGMLREFFPVLKYFPGYDKFLKQLDDVGERLANIYVRRFRDGLSTPAWNWAKEYSKRPEAQGMGELELSFCIGSTYQASLTPYEILRIILLAAICHPEEKARLQKEIDLVVGKDNLPGWEHKDRIQFVQAFIYEALRWHAFSPLGAPRAVSRDIEYKGYFIPKGATLVLNQWAMDHDENVYDNPFTFRPQRWIDNPDLPHVIFGFGLRGCPGQHLARDHLFINTARLFWAFNFGNAYENGKKVELDLDELMQPRGGGSAFNQVPSFKASVIIRSSERRQIVENEWDAVEKDEQKILAEAMPLPE

[Multiple Choices]
A. 13..35
B. 12..39
C. 26..46
D. 13..35; 796..814
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

> The sequence-matched UniProt annotation identifies a helical transmembrane region at 13..35. Its ECO:0000255 evidence indicates computational support, not necessarily experimental confirmation.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a prominent N-terminal hydrophobic stretch, consistent with a membrane-spanning helix. Among the choices, 13..35 gives a plausible helix-length segment around that stretch; 12..39 extends farther into acidic/charged and proline-containing flanks, 26..46 misses much of the hydrophobic region, and D includes positions beyond the 529-residue sequence.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The hydrophobic sequence pattern and ordinary expectations for transmembrane-helix length provide a transferable basis for preferring A. The exact boundary is inherently prediction-dependent, but distinguishing A from the offered alternatives does not require knowing this protein's recorded annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> A and B overlap the same N-terminal hydrophobic region, but B is longer and includes less suitable flanking residues, making A the more defensible offered segment.


### Important caveats

- The supporting database feature is computationally evidenced; it should not be described as experimentally established.
- Predicted transmembrane boundaries can vary by a few residues.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a prominent N-terminal hydrophobic stretch, consistent with a membrane-spanning helix. Among the choices, 13..35 gives a plausible helix-length segment around that stretch; 12..39 extends farther into acidic/charged and proline-containing flanks, 26..46 misses much of the hydrophobic region, and D includes positions beyond the 529-residue sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The hydrophobic sequence pattern and ordinary expectations for transmembrane-helix length provide a transferable basis for preferring A. The exact boundary is inherently prediction-dependent, but distinguishing A from the offered alternatives does not require knowing this protein's recorded annotation."
  },
  "case_id": "transmembrane_0016",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies a helical transmembrane region at 13..35. Its ECO:0000255 evidence indicates computational support, not necessarily experimental confirmation."
  },
  "important_caveats": [
    "The supporting database feature is computationally evidenced; it should not be described as experimentally established.",
    "Predicted transmembrane boundaries can vary by a few residues."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A and B overlap the same N-terminal hydrophobic region, but B is longer and includes less suitable flanking residues, making A the more defensible offered segment."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0016",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies a helical transmembrane region at 13..35. Its ECO:0000255 evidence indicates computational support, not necessarily experimental confirmation.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a prominent N-terminal hydrophobic stretch, consistent with a membrane-spanning helix. Among the choices, 13..35 gives a plausible helix-length segment around that stretch; 12..39 extends farther into acidic/charged and proline-containing flanks, 26..46 misses much of the hydrophobic region, and D includes positions beyond the 529-residue sequence.",
    "missing_item_specific_fact": "",
    "reason": "The hydrophobic sequence pattern and ordinary expectations for transmembrane-helix length provide a transferable basis for preferring A. The exact boundary is inherently prediction-dependent, but distinguishing A from the offered alternatives does not require knowing this protein's recorded annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A and B overlap the same N-terminal hydrophobic region, but B is longer and includes less suitable flanking residues, making A the more defensible offered segment."
  },
  "important_caveats": [
    "The supporting database feature is computationally evidenced; it should not be described as experimentally established.",
    "Predicted transmembrane boundaries can vary by a few residues."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (C5, H3) records a transmembrane helix at positions 13..35 with evidence code ECO:0000255 (by similarity/computational). The sequence at 13-35 (LPAQHLLASLALVGALLSVGYLL) is a ~23-residue predominantly hydrophobic stretch consistent with a TM helix. This is a Cytochrome P450 monooxygenase (okaD), which characteristically carries an N-terminal TM anchor. The annotation is computational (by similarity), not experimentally validated, but the hydrophobic pattern in the sequence is consistent with the annotation. The protein is 529 residues long, so option D's second segment (796..814) is impossible.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Several transferable features distinguish option A from the alternatives: (1) Cytochrome P450 enzymes are a well-known family that characteristically possess an N-terminal transmembrane anchor helix; this is a family-level regularity learned from many P450s. (2) The N-terminal region 13-35 is the most hydrophobic contiguous stretch in the first ~50 residues (L, A, V, L, L, A, L, L, V, L, L dominate), with a length of ~23 residues appropriate for a single-pass TM helix. (3) Option B (12..39) extends into charged/polar residues E(12) and R(37),P(38),A(39), which are incompatible with a lipid-embedded helix. (4) Option C (26..46) begins with G and extends into highly polar residues (K, Y, Q, L, P, L), clearly not a TM segment. (5) Option D includes positions 796..814, but the protein is only 529 residues long, making it physically impossible. Thus, hydrophobicity analysis of the sequence combined with P450 family knowledge and basic arithmetic on protein length meaningfully selects A.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The hydrophobicity pattern at 13-35 is directly readable from the supplied sequence. P450 N-terminal TM anchors are a well-established family feature. The elimination of D by protein length, C by excessive polarity, and B by charged residues at the boundaries are all achievable from the input sequence plus general biochemistry and family knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option D is eliminated by protein length (529 < 796). Option C is eliminated by inclusion of multiple polar/charged residues incompatible with a TM helix. Option B is disfavored by extension into charged residues (E at 12, R at 37). Option A is the only choice whose boundaries align with a clean hydrophobic core of appropriate TM length. No ambiguity among the offered choices.


### Important caveats

- The UniProt annotation uses evidence code ECO:0000255 (by similarity), indicating a computational prediction rather than experimental validation.
- The exact boundaries (13 vs 12, 35 vs 36) of TM helices can vary slightly between predictors; however, the offered choices are spaced far enough apart that hydrophobicity analysis clearly favors 13-35.
- The reviewer-only evidence confirms the sequence matches the benchmark (SHA-256 match) and the annotation is present in both current and historical entry versions.
- The protein is annotated as a Cytochrome P450 monooxygenase (okaD) from Penicillium ochrochloron, but this identity was not provided to the evaluated model; the P450 family inference must come from sequence features (heme-binding motifs visible later in the sequence) or general pattern recognition.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Several transferable features distinguish option A from the alternatives: (1) Cytochrome P450 enzymes are a well-known family that characteristically possess an N-terminal transmembrane anchor helix; this is a family-level regularity learned from many P450s. (2) The N-terminal region 13-35 is the most hydrophobic contiguous stretch in the first ~50 residues (L, A, V, L, L, A, L, L, V, L, L dominate), with a length of ~23 residues appropriate for a single-pass TM helix. (3) Option B (12..39) extends into charged/polar residues E(12) and R(37),P(38),A(39), which are incompatible with a lipid-embedded helix. (4) Option C (26..46) begins with G and extends into highly polar residues (K, Y, Q, L, P, L), clearly not a TM segment. (5) Option D includes positions 796..814, but the protein is only 529 residues long, making it physically impossible. Thus, hydrophobicity analysis of the sequence combined with P450 family knowledge and basic arithmetic on protein length meaningfully selects A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The hydrophobicity pattern at 13-35 is directly readable from the supplied sequence. P450 N-terminal TM anchors are a well-established family feature. The elimination of D by protein length, C by excessive polarity, and B by charged residues at the boundaries are all achievable from the input sequence plus general biochemistry and family knowledge."
  },
  "case_id": "transmembrane_0016",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C4"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H3) records a transmembrane helix at positions 13..35 with evidence code ECO:0000255 (by similarity/computational). The sequence at 13-35 (LPAQHLLASLALVGALLSVGYLL) is a ~23-residue predominantly hydrophobic stretch consistent with a TM helix. This is a Cytochrome P450 monooxygenase (okaD), which characteristically carries an N-terminal TM anchor. The annotation is computational (by similarity), not experimentally validated, but the hydrophobic pattern in the sequence is consistent with the annotation. The protein is 529 residues long, so option D's second segment (796..814) is impossible."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (by similarity), indicating a computational prediction rather than experimental validation.",
    "The exact boundaries (13 vs 12, 35 vs 36) of TM helices can vary slightly between predictors; however, the offered choices are spaced far enough apart that hydrophobicity analysis clearly favors 13-35.",
    "The reviewer-only evidence confirms the sequence matches the benchmark (SHA-256 match) and the annotation is present in both current and historical entry versions.",
    "The protein is annotated as a Cytochrome P450 monooxygenase (okaD) from Penicillium ochrochloron, but this identity was not provided to the evaluated model; the P450 family inference must come from sequence features (heme-binding motifs visible later in the sequence) or general pattern recognition."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option D is eliminated by protein length (529 < 796). Option C is eliminated by inclusion of multiple polar/charged residues incompatible with a TM helix. Option B is disfavored by extension into charged residues (E at 12, R at 37). Option A is the only choice whose boundaries align with a clean hydrophobic core of appropriate TM length. No ambiguity among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0016",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H3) records a transmembrane helix at positions 13..35 with evidence code ECO:0000255 (by similarity/computational). The sequence at 13-35 (LPAQHLLASLALVGALLSVGYLL) is a ~23-residue predominantly hydrophobic stretch consistent with a TM helix. This is a Cytochrome P450 monooxygenase (okaD), which characteristically carries an N-terminal TM anchor. The annotation is computational (by similarity), not experimentally validated, but the hydrophobic pattern in the sequence is consistent with the annotation. The protein is 529 residues long, so option D's second segment (796..814) is impossible.",
    "evidence_ids": ["C5", "H3", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Several transferable features distinguish option A from the alternatives: (1) Cytochrome P450 enzymes are a well-known family that characteristically possess an N-terminal transmembrane anchor helix; this is a family-level regularity learned from many P450s. (2) The N-terminal region 13-35 is the most hydrophobic contiguous stretch in the first ~50 residues (L, A, V, L, L, A, L, L, V, L, L dominate), with a length of ~23 residues appropriate for a single-pass TM helix. (3) Option B (12..39) extends into charged/polar residues E(12) and R(37),P(38),A(39), which are incompatible with a lipid-embedded helix. (4) Option C (26..46) begins with G and extends into highly polar residues (K, Y, Q, L, P, L), clearly not a TM segment. (5) Option D includes positions 796..814, but the protein is only 529 residues long, making it physically impossible. Thus, hydrophobicity analysis of the sequence combined with P450 family knowledge and basic arithmetic on protein length meaningfully selects A.",
    "missing_item_specific_fact": "",
    "reason": "The hydrophobicity pattern at 13-35 is directly readable from the supplied sequence. P450 N-terminal TM anchors are a well-established family feature. The elimination of D by protein length, C by excessive polarity, and B by charged residues at the boundaries are all achievable from the input sequence plus general biochemistry and family knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option D is eliminated by protein length (529 < 796). Option C is eliminated by inclusion of multiple polar/charged residues incompatible with a TM helix. Option B is disfavored by extension into charged residues (E at 12, R at 37). Option A is the only choice whose boundaries align with a clean hydrophobic core of appropriate TM length. No ambiguity among the offered choices."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (by similarity), indicating a computational prediction rather than experimental validation.",
    "The exact boundaries (13 vs 12, 35 vs 36) of TM helices can vary slightly between predictors; however, the offered choices are spaced far enough apart that hydrophobicity analysis clearly favors 13-35.",
    "The reviewer-only evidence confirms the sequence matches the benchmark (SHA-256 match) and the annotation is present in both current and historical entry versions.",
    "The protein is annotated as a Cytochrome P450 monooxygenase (okaD) from Penicillium ochrochloron, but this identity was not provided to the evaluated model; the P450 family inference must come from sequence features (heme-binding motifs visible later in the sequence) or general pattern recognition."
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
  "benchmark_sequence_length": 529,
  "benchmark_sequence_sha256": "99280cdea8196dec317d2f18830c1825fab94ad5dea0f68ec9b853bab5214ffd",
  "current_entry_audit": {
    "entryVersion": 24,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2018-10-10",
    "sequenceVersion": 1
  },
  "current_record_sha256": "40a05d7310f4d79d3d8cc83398d816d9e515e9003ac315147b668ca6050d9c84",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 529,
  "current_source_sequence_sha256": "99280cdea8196dec317d2f18830c1825fab94ad5dea0f68ec9b853bab5214ffd",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 23,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A2Z5U6I9",
  "selected_historical_entry_version": 23,
  "selected_historical_record_sha256": "325b1f9f1545fcf13c71c1f0abd0af2223be88dff7649f9a3b61a997d58cc16f",
  "selected_historical_source_sequence_length": 529,
  "selected_historical_source_sequence_sha256": "99280cdea8196dec317d2f18830c1825fab94ad5dea0f68ec9b853bab5214ffd",
  "selected_historical_version": {
    "accession": "A0A2Z5U6I9",
    "database": "Swiss-Prot",
    "entryVersion": 23,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "OKAD_PENOH",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5U6I9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A2Z5U6I9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:54.111891+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40a05d7310f4d79d3d8cc83398d816d9e515e9003ac315147b668ca6050d9c84",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2Z5U6I9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5U6I9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":24,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2018-10-10\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:54.111891+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40a05d7310f4d79d3d8cc83398d816d9e515e9003ac315147b668ca6050d9c84",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2Z5U6I9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5U6I9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Penicillium\"],\"scientificName\":\"Penicillium ochrochloron\",\"taxonId\":69780}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:54.111891+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40a05d7310f4d79d3d8cc83398d816d9e515e9003ac315147b668ca6050d9c84",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2Z5U6I9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5U6I9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"28631282\",\"source\":\"PubMed\"}],\"value\":\"Okaramines biosynthesis cluster protein D\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"28631282\",\"source\":\"PubMed\"}],\"value\":\"1.14.99.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"28631282\",\"source\":\"PubMed\"}],\"value\":\"Cytochrome P450 monooxygenase okaD\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:54.111891+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40a05d7310f4d79d3d8cc83398d816d9e515e9003ac315147b668ca6050d9c84",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2Z5U6I9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5U6I9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":35},\"start\":{\"modifier\":\"EXACT\",\"value\":13}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:24:54.111891+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40a05d7310f4d79d3d8cc83398d816d9e515e9003ac315147b668ca6050d9c84",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2Z5U6I9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5U6I9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Lai C.Y.\",\"Lo I.W.\",\"Hewage R.T.\",\"Chen Y.C.\",\"Chen C.T.\",\"Lee C.F.\",\"Lin S.\",\"Tang M.C.\",\"Lin H.C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"28631282\"},{\"database\":\"DOI\",\"id\":\"10.1002/anie.201705501\"}],\"citationType\":\"journal article\",\"firstPage\":\"9478\",\"id\":\"28631282\",\"journal\":\"Angew. Chem. Int. Ed.\",\"lastPage\":\"9482\",\"publicationDate\":\"2017\",\"title\":\"Biosynthesis of Complex Indole Alkaloids: Elucidation of the Concise Pathway of Okaramines.\",\"volume\":\"56\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:24:54.111891+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40a05d7310f4d79d3d8cc83398d816d9e515e9003ac315147b668ca6050d9c84",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2Z5U6I9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2Z5U6I9?format=txt&versions=23)

```json
{
  "entry_version": 23,
  "evidence_id": "H1",
  "excerpt": "ID   OKAD_PENOH              Reviewed;         529 AA.\nAC   A0A2Z5U6I9;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   10-OCT-2018, sequence version 1.\nDT   28-JAN-2026, entry version 23.\nDE   RecName: Full=Cytochrome P450 monooxygenase okaD {ECO:0000303|PubMed:28631282};\nDE            EC=1.14.99.- {ECO:0000269|PubMed:28631282};\nDE   AltName: Full=Okaramines biosynthesis cluster protein D {ECO:0000303|PubMed:28631282};\nGN   Name=okaD {ECO:0000303|PubMed:28631282};\nOS   Penicillium ochrochloron.\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Penicillium.\nOX   NCBI_TaxID=69780;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:57.209412+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "325b1f9f1545fcf13c71c1f0abd0af2223be88dff7649f9a3b61a997d58cc16f",
  "url": "https://rest.uniprot.org/unisave/A0A2Z5U6I9?format=txt&versions=23"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2Z5U6I9?format=txt&versions=23)

```json
{
  "entry_version": 23,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, DISRUPTION PHENOTYPE, CATALYTIC ACTIVITY, AND PATHWAY.\nRX   PubMed=28631282; DOI=10.1002/anie.201705501;\nRA   Lai C.Y., Lo I.W., Hewage R.T., Chen Y.C., Chen C.T., Lee C.F., Lin S.,\nRA   Tang M.C., Lin H.C.;\nRT   \"Biosynthesis of Complex Indole Alkaloids: Elucidation of the Concise\nRT   Pathway of Okaramines.\";\nRL   Angew. Chem. Int. Ed. 56:9478-9482(2017).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:57.209412+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 24-31",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "325b1f9f1545fcf13c71c1f0abd0af2223be88dff7649f9a3b61a997d58cc16f",
  "url": "https://rest.uniprot.org/unisave/A0A2Z5U6I9?format=txt&versions=23"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2Z5U6I9?format=txt&versions=23)

```json
{
  "entry_version": 23,
  "evidence_id": "H3",
  "excerpt": "FT   TRANSMEM        13..35\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:57.209412+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 111-113",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "325b1f9f1545fcf13c71c1f0abd0af2223be88dff7649f9a3b61a997d58cc16f",
  "url": "https://rest.uniprot.org/unisave/A0A2Z5U6I9?format=txt&versions=23"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 16. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
