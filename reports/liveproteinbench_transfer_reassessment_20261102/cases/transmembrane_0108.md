# transmembrane_0108

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0108.txt)

**Task:** `transmembrane`  
**Expected answer:** **D** — 58..78; 89..109; 122..142; 146..166; 192..212; 216..236; 266..286; 300..320; 326..346; 352..372; 405..425; 431..451

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MEDDDFSIKDKKENYETCSTETISSYISINEKCQLIEKDINDDNHENPYMIFNKISSSLIAMLQGVEVLCNLSIIYLLKDNYHLHPASLSIVMCFIKIPWSIKLVWAVISDNYPIFGYRRKYYLLLGSFLCILSLICLGLITHNNLFITILLLFIYFFGSSLCNVIGEAQVVESNRNCSINSSARNVSLFFAFRKLSFAIMSYLSGYLLLLISKKHIFLIGSFLPICVFTSGFFIIEKRNYTKSSIKDQIKCIYSIIKLSYLKNFIIFIFIMMSTPSCGNTLFFYITNELKFSPNLLGKMAMFQSLASFISIISYMLFFTKIDIRKLLLYSTIIITPFCLLPLVVIKKVNYFLFIPNTLFFITDTVLIEFIAEFQTMPILVLCSRLIPEGFESTIYSLLLSSNNFASIISSFLSSLLTYSLNITSTNFTNLPYMIIICCLTNIIPIFFLYILPNHSQKKNLQHSNSHTQKYYSYPSTDYISSQKSDSSEITKFSADMQIDDITLE

[Multiple Choices]
A. 58..78; 89..109; 122..142; 146..166; 192..212; 216..236; 266..286; 300..320; 326..346; 405..425; 431..451
B. 58..78; 89..109; 122..142; 146..166; 192..212; 216..236; 266..286; 300..320; 326..346; 352..372; 400..427; 431..451
C. 27..47; 78..98; 108..128; 136..156; 173..193; 209..229; 337..357; 366..386; 400..420; 432..452; 465..485
D. 58..78; 89..109; 122..142; 146..166; 192..212; 216..236; 266..286; 300..320; 326..346; 352..372; 405..425; 431..451
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

> The sequence-matched archived UniProt entry annotates all 12 regions listed in D as transmembrane helices, matching the key exactly. These annotations carry ECO:0000255 computational evidence, so they support the key as a database prediction, not as direct experimental confirmation.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11), [H12](#evidence-h12), [H13](#evidence-h13), [H14](#evidence-h14).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The input sequence has repeated hydrophobic stretches characteristic of a multipass membrane protein. In particular, the stretch around 352–372 is strongly hydrophobic, supporting its inclusion and distinguishing D from A; the other listed regions likewise align with hydrophobic-rich segments. For the final helix, the shorter 405–425 interval better fits the hydrophobic core than B's broader 400–427 interval, which adds less hydrophobic flanks. These transferable sequence-based principles meaningfully favor D, though exact helix boundaries can be uncertain.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can use hydropathy and the pattern of repeated membrane-spanning helices in the supplied sequence to distinguish the choices without knowing this protein's recorded annotation. The exact boundaries are less certain than identifying the helices, but the choices differ in ways that sequence features can inform.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives are not equally defensible as complete lists: A omits a hydrophobic segment, C differs substantially from the repeated hydrophobic pattern, and B includes a broader interval around the final predicted helix. Boundary uncertainty is a caveat, but does not make another entire option comparably supported.


### Important caveats

- The source annotations are computationally supported predictions, not direct experimental verification of every membrane-spanning boundary.
- The sequence-matched source supports the key, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The input sequence has repeated hydrophobic stretches characteristic of a multipass membrane protein. In particular, the stretch around 352–372 is strongly hydrophobic, supporting its inclusion and distinguishing D from A; the other listed regions likewise align with hydrophobic-rich segments. For the final helix, the shorter 405–425 interval better fits the hydrophobic core than B's broader 400–427 interval, which adds less hydrophobic flanks. These transferable sequence-based principles meaningfully favor D, though exact helix boundaries can be uncertain.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use hydropathy and the pattern of repeated membrane-spanning helices in the supplied sequence to distinguish the choices without knowing this protein's recorded annotation. The exact boundaries are less certain than identifying the helices, but the choices differ in ways that sequence features can inform."
  },
  "case_id": "transmembrane_0108",
  "expected_answer_check": {
    "evidence_ids": [
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
      "H13",
      "H14"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched archived UniProt entry annotates all 12 regions listed in D as transmembrane helices, matching the key exactly. These annotations carry ECO:0000255 computational evidence, so they support the key as a database prediction, not as direct experimental confirmation."
  },
  "important_caveats": [
    "The source annotations are computationally supported predictions, not direct experimental verification of every membrane-spanning boundary.",
    "The sequence-matched source supports the key, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives are not equally defensible as complete lists: A omits a hydrophobic segment, C differs substantially from the repeated hydrophobic pattern, and B includes a broader interval around the final predicted helix. Boundary uncertainty is a caveat, but does not make another entire option comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0108",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched archived UniProt entry annotates all 12 regions listed in D as transmembrane helices, matching the key exactly. These annotations carry ECO:0000255 computational evidence, so they support the key as a database prediction, not as direct experimental confirmation.",
    "evidence_ids": ["H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "H11", "H12", "H13", "H14"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The input sequence has repeated hydrophobic stretches characteristic of a multipass membrane protein. In particular, the stretch around 352–372 is strongly hydrophobic, supporting its inclusion and distinguishing D from A; the other listed regions likewise align with hydrophobic-rich segments. For the final helix, the shorter 405–425 interval better fits the hydrophobic core than B's broader 400–427 interval, which adds less hydrophobic flanks. These transferable sequence-based principles meaningfully favor D, though exact helix boundaries can be uncertain.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use hydropathy and the pattern of repeated membrane-spanning helices in the supplied sequence to distinguish the choices without knowing this protein's recorded annotation. The exact boundaries are less certain than identifying the helices, but the choices differ in ways that sequence features can inform."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives are not equally defensible as complete lists: A omits a hydrophobic segment, C differs substantially from the repeated hydrophobic pattern, and B includes a broader interval around the final predicted helix. Boundary uncertainty is a caveat, but does not make another entire option comparably supported."
  },
  "important_caveats": [
    "The source annotations are computationally supported predictions, not direct experimental verification of every membrane-spanning boundary.",
    "The sequence-matched source supports the key, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q8IBB7 (Folate transporter 1, PfFT1) annotates exactly 12 transmembrane helical segments at positions 58..78, 89..109, 122..142, 146..166, 192..212, 216..236, 266..286, 300..320, 326..346, 352..372, 405..425, and 431..451, which matches Option D precisely. However, all 12 annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred from homologous proteins, not experimentally determined boundaries. The sequence in the benchmark matches the UniProt sequence exactly (505 AA, SHA256 confirmed).

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [C13](#evidence-c13), [C14](#evidence-c14), [C15](#evidence-c15), [C16](#evidence-c16).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein sequence exhibits the hallmarks of a Major Facilitator Superfamily (MFS) transporter: ~500 residues, highly hydrophobic stretches distributed across the sequence, and the characteristic alternating hydrophobic/hydrophilic pattern. MFS transporters are well-known to possess exactly 12 transmembrane helices in a 6+6 topology, which is a robust family-level feature learned from hundreds of characterized MFS members (e.g., LacY, GlpT, EmrB). This eliminates Option A (11 segments) and Option C (11 segments with shifted positions). Between Options B and D, the sole difference is the boundary of one helix: B lists 400..427 (28 residues) while D lists 405..425 (21 residues). Standard alpha-helical TM segments span approximately 19-25 residues to cross the ~30 Å lipid bilayer; a 28-residue helix is atypically long, while 21 residues is squarely in the canonical range. Additionally, examining the sequence at positions 400-404 reveals residues less hydrophobic than the core helix, making the 405 start more consistent with a true hydrophobic boundary. These are transferable principles from TM-helix biophysics and MFS-family knowledge, not facts unique to this protein.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can apply MFS 12-TM topology to eliminate A and C, and use standard TM helix length constraints (~20-25 residues) plus hydrophobicity inspection to prefer 405..425 over 400..427, arriving at D. The argument is probabilistic rather than certain for the exact boundary, but it meaningfully distinguishes the offered alternatives using family-level and biophysical knowledge learned from other proteins.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and C are eliminated by the 12-TM MFS topology. Option B's 400..427 (28-residue) helix is disfavored by standard TM helix length norms. Option D is the only set consistent with both the 12-helix count and typical helix lengths. The remaining boundary uncertainties (e.g., ±2-3 residues on any helix) are not reflected in the offered alternatives, so no two options are equally defensible.


### Important caveats

- All 12 UniProt TM annotations are ECO:0000255 (computational inference by similarity), not experimental measurements. The exact boundaries are algorithm-dependent predictions.
- The question stem says 'a segment' (singular) but all options list 11-12 segments; the intended task is clearly to select the complete correct set.
- The 400..427 vs 405..425 distinction is subtle and relies on general TM-length heuristics; a model performing precise hydropathy profiling would arrive at the same conclusion but with less certainty than the 12-TM topology argument.
- The reviewer-only evidence confirms the sequence matches UniProt Q8IBB7 exactly, but the model was not given the protein name, organism, or family annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein sequence exhibits the hallmarks of a Major Facilitator Superfamily (MFS) transporter: ~500 residues, highly hydrophobic stretches distributed across the sequence, and the characteristic alternating hydrophobic/hydrophilic pattern. MFS transporters are well-known to possess exactly 12 transmembrane helices in a 6+6 topology, which is a robust family-level feature learned from hundreds of characterized MFS members (e.g., LacY, GlpT, EmrB). This eliminates Option A (11 segments) and Option C (11 segments with shifted positions). Between Options B and D, the sole difference is the boundary of one helix: B lists 400..427 (28 residues) while D lists 405..425 (21 residues). Standard alpha-helical TM segments span approximately 19-25 residues to cross the ~30 Å lipid bilayer; a 28-residue helix is atypically long, while 21 residues is squarely in the canonical range. Additionally, examining the sequence at positions 400-404 reveals residues less hydrophobic than the core helix, making the 405 start more consistent with a true hydrophobic boundary. These are transferable principles from TM-helix biophysics and MFS-family knowledge, not facts unique to this protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can apply MFS 12-TM topology to eliminate A and C, and use standard TM helix length constraints (~20-25 residues) plus hydrophobicity inspection to prefer 405..425 over 400..427, arriving at D. The argument is probabilistic rather than certain for the exact boundary, but it meaningfully distinguishes the offered alternatives using family-level and biophysical knowledge learned from other proteins."
  },
  "case_id": "transmembrane_0108",
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
      "C16"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q8IBB7 (Folate transporter 1, PfFT1) annotates exactly 12 transmembrane helical segments at positions 58..78, 89..109, 122..142, 146..166, 192..212, 216..236, 266..286, 300..320, 326..346, 352..372, 405..425, and 431..451, which matches Option D precisely. However, all 12 annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred from homologous proteins, not experimentally determined boundaries. The sequence in the benchmark matches the UniProt sequence exactly (505 AA, SHA256 confirmed)."
  },
  "important_caveats": [
    "All 12 UniProt TM annotations are ECO:0000255 (computational inference by similarity), not experimental measurements. The exact boundaries are algorithm-dependent predictions.",
    "The question stem says 'a segment' (singular) but all options list 11-12 segments; the intended task is clearly to select the complete correct set.",
    "The 400..427 vs 405..425 distinction is subtle and relies on general TM-length heuristics; a model performing precise hydropathy profiling would arrive at the same conclusion but with less certainty than the 12-TM topology argument.",
    "The reviewer-only evidence confirms the sequence matches UniProt Q8IBB7 exactly, but the model was not given the protein name, organism, or family annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and C are eliminated by the 12-TM MFS topology. Option B's 400..427 (28-residue) helix is disfavored by standard TM helix length norms. Option D is the only set consistent with both the 12-helix count and typical helix lengths. The remaining boundary uncertainties (e.g., ±2-3 residues on any helix) are not reflected in the offered alternatives, so no two options are equally defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0108",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q8IBB7 (Folate transporter 1, PfFT1) annotates exactly 12 transmembrane helical segments at positions 58..78, 89..109, 122..142, 146..166, 192..212, 216..236, 266..286, 300..320, 326..346, 352..372, 405..425, and 431..451, which matches Option D precisely. However, all 12 annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred from homologous proteins, not experimentally determined boundaries. The sequence in the benchmark matches the UniProt sequence exactly (505 AA, SHA256 confirmed).",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "C14", "C15", "C16"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein sequence exhibits the hallmarks of a Major Facilitator Superfamily (MFS) transporter: ~500 residues, highly hydrophobic stretches distributed across the sequence, and the characteristic alternating hydrophobic/hydrophilic pattern. MFS transporters are well-known to possess exactly 12 transmembrane helices in a 6+6 topology, which is a robust family-level feature learned from hundreds of characterized MFS members (e.g., LacY, GlpT, EmrB). This eliminates Option A (11 segments) and Option C (11 segments with shifted positions). Between Options B and D, the sole difference is the boundary of one helix: B lists 400..427 (28 residues) while D lists 405..425 (21 residues). Standard alpha-helical TM segments span approximately 19-25 residues to cross the ~30 Å lipid bilayer; a 28-residue helix is atypically long, while 21 residues is squarely in the canonical range. Additionally, examining the sequence at positions 400-404 reveals residues less hydrophobic than the core helix, making the 405 start more consistent with a true hydrophobic boundary. These are transferable principles from TM-helix biophysics and MFS-family knowledge, not facts unique to this protein.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can apply MFS 12-TM topology to eliminate A and C, and use standard TM helix length constraints (~20-25 residues) plus hydrophobicity inspection to prefer 405..425 over 400..427, arriving at D. The argument is probabilistic rather than certain for the exact boundary, but it meaningfully distinguishes the offered alternatives using family-level and biophysical knowledge learned from other proteins."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and C are eliminated by the 12-TM MFS topology. Option B's 400..427 (28-residue) helix is disfavored by standard TM helix length norms. Option D is the only set consistent with both the 12-helix count and typical helix lengths. The remaining boundary uncertainties (e.g., ±2-3 residues on any helix) are not reflected in the offered alternatives, so no two options are equally defensible."
  },
  "important_caveats": [
    "All 12 UniProt TM annotations are ECO:0000255 (computational inference by similarity), not experimental measurements. The exact boundaries are algorithm-dependent predictions.",
    "The question stem says 'a segment' (singular) but all options list 11-12 segments; the intended task is clearly to select the complete correct set.",
    "The 400..427 vs 405..425 distinction is subtle and relies on general TM-length heuristics; a model performing precise hydropathy profiling would arrive at the same conclusion but with less certainty than the 12-TM topology argument.",
    "The reviewer-only evidence confirms the sequence matches UniProt Q8IBB7 exactly, but the model was not given the protein name, organism, or family annotation."
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
  "benchmark_sequence_length": 505,
  "benchmark_sequence_sha256": "c119806f4af8df36d96a0b3132aa84ccec0f7513a38b42c3ceb1495fb192ffc3",
  "current_entry_audit": {
    "entryVersion": 100,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2003-03-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "f181b4dbb2ac2ea55eb60db5ac65720a1ffcd9dd3096b131edc4a79c0f2331cd",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 505,
  "current_source_sequence_sha256": "c119806f4af8df36d96a0b3132aa84ccec0f7513a38b42c3ceb1495fb192ffc3",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 98,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q8IBB7",
  "selected_historical_entry_version": 98,
  "selected_historical_record_sha256": "23128f941b579a9921cbe78a9e91da7734842a0f3c2311d1bf182aed647224f0",
  "selected_historical_source_sequence_length": 505,
  "selected_historical_source_sequence_sha256": "c119806f4af8df36d96a0b3132aa84ccec0f7513a38b42c3ceb1495fb192ffc3",
  "selected_historical_version": {
    "accession": "Q8IBB7",
    "database": "Swiss-Prot",
    "entryVersion": 98,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "FT1_PLAF7",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBB7.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q8IBB7\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:32:06.455529+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f181b4dbb2ac2ea55eb60db5ac65720a1ffcd9dd3096b131edc4a79c0f2331cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IBB7.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBB7.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":100,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2003-03-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:32:06.455529+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f181b4dbb2ac2ea55eb60db5ac65720a1ffcd9dd3096b131edc4a79c0f2331cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IBB7.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBB7.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000001450\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Aconoidasida\",\"Haemosporida\",\"Plasmodiidae\",\"Plasmodium\",\"Laverania\"],\"scientificName\":\"Plasmodium falciparum (isolate 3D7)\",\"taxonId\":36329}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:32:06.455529+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f181b4dbb2ac2ea55eb60db5ac65720a1ffcd9dd3096b131edc4a79c0f2331cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IBB7.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBB7.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"21998306\",\"source\":\"PubMed\"}],\"value\":\"Folate transporter 1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"21998306\",\"source\":\"PubMed\"}],\"value\":\"PfFT1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:32:06.455529+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f181b4dbb2ac2ea55eb60db5ac65720a1ffcd9dd3096b131edc4a79c0f2331cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IBB7.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBB7.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":78},\"start\":{\"modifier\":\"EXACT\",\"value\":58}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:32:06.455529+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f181b4dbb2ac2ea55eb60db5ac65720a1ffcd9dd3096b131edc4a79c0f2331cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IBB7.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBB7.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":109},\"start\":{\"modifier\":\"EXACT\",\"value\":89}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:32:06.455529+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f181b4dbb2ac2ea55eb60db5ac65720a1ffcd9dd3096b131edc4a79c0f2331cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IBB7.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBB7.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":142},\"start\":{\"modifier\":\"EXACT\",\"value\":122}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:32:06.455529+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f181b4dbb2ac2ea55eb60db5ac65720a1ffcd9dd3096b131edc4a79c0f2331cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IBB7.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBB7.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":166},\"start\":{\"modifier\":\"EXACT\",\"value\":146}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:32:06.455529+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f181b4dbb2ac2ea55eb60db5ac65720a1ffcd9dd3096b131edc4a79c0f2331cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IBB7.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBB7.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":212},\"start\":{\"modifier\":\"EXACT\",\"value\":192}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:32:06.455529+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f181b4dbb2ac2ea55eb60db5ac65720a1ffcd9dd3096b131edc4a79c0f2331cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IBB7.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBB7.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":236},\"start\":{\"modifier\":\"EXACT\",\"value\":216}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:32:06.455529+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f181b4dbb2ac2ea55eb60db5ac65720a1ffcd9dd3096b131edc4a79c0f2331cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IBB7.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBB7.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":286},\"start\":{\"modifier\":\"EXACT\",\"value\":266}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:32:06.455529+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f181b4dbb2ac2ea55eb60db5ac65720a1ffcd9dd3096b131edc4a79c0f2331cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IBB7.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBB7.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":320},\"start\":{\"modifier\":\"EXACT\",\"value\":300}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:32:06.455529+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f181b4dbb2ac2ea55eb60db5ac65720a1ffcd9dd3096b131edc4a79c0f2331cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IBB7.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBB7.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":346},\"start\":{\"modifier\":\"EXACT\",\"value\":326}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-02T04:32:06.455529+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f181b4dbb2ac2ea55eb60db5ac65720a1ffcd9dd3096b131edc4a79c0f2331cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IBB7.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBB7.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":372},\"start\":{\"modifier\":\"EXACT\",\"value\":352}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-02T04:32:06.455529+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f181b4dbb2ac2ea55eb60db5ac65720a1ffcd9dd3096b131edc4a79c0f2331cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IBB7.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBB7.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":425},\"start\":{\"modifier\":\"EXACT\",\"value\":405}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/11",
  "retrieved_utc": "2026-11-02T04:32:06.455529+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f181b4dbb2ac2ea55eb60db5ac65720a1ffcd9dd3096b131edc4a79c0f2331cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IBB7.json"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBB7.json)

```json
{
  "evidence_id": "C16",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":451},\"start\":{\"modifier\":\"EXACT\",\"value\":431}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/12",
  "retrieved_utc": "2026-11-02T04:32:06.455529+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f181b4dbb2ac2ea55eb60db5ac65720a1ffcd9dd3096b131edc4a79c0f2331cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IBB7.json"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBB7.json)

```json
{
  "evidence_id": "C17",
  "excerpt": "{\"citation\":{\"authors\":[\"Salcedo-Sora J.E.\",\"Ochong E.\",\"Beveridge S.\",\"Johnson D.\",\"Nzila A.\",\"Biagini G.A.\",\"Stocks P.A.\",\"O'Neill P.M.\",\"Krishna S.\",\"Bray P.G.\",\"Ward S.A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"21998306\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m111.286054\"}],\"citationType\":\"journal article\",\"firstPage\":\"44659\",\"id\":\"21998306\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"44668\",\"publicationDate\":\"2011\",\"title\":\"The molecular basis of folate salvage in Plasmodium falciparum: characterization of two folate transporters.\",\"volume\":\"286\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"TRANSPORTER ACTIVITY\",\"ACTIVITY REGULATION\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:32:06.455529+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f181b4dbb2ac2ea55eb60db5ac65720a1ffcd9dd3096b131edc4a79c0f2331cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IBB7.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98)

```json
{
  "entry_version": 98,
  "evidence_id": "H1",
  "excerpt": "ID   FT1_PLAF7               Reviewed;         505 AA.\nAC   Q8IBB7;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAR-2003, sequence version 1.\nDT   28-JAN-2026, entry version 98.\nDE   RecName: Full=Folate transporter 1 {ECO:0000303|PubMed:21998306};\nDE            Short=PfFT1 {ECO:0000303|PubMed:21998306};\nGN   ORFNames=PF3D7_0828600 {ECO:0000312|EMBL:CAD51089.1};\nOS   Plasmodium falciparum (isolate 3D7).\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;\nOC   Plasmodiidae; Plasmodium; Plasmodium (Laverania).\nOX   NCBI_TaxID=36329 {ECO:0000312|Proteomes:UP000001450};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:10.640562+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "23128f941b579a9921cbe78a9e91da7734842a0f3c2311d1bf182aed647224f0",
  "url": "https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98)

```json
{
  "entry_version": 98,
  "evidence_id": "H2",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, TRANSPORTER ACTIVITY, ACTIVITY REGULATION, AND SUBCELLULAR\nRP   LOCATION.\nRX   PubMed=21998306; DOI=10.1074/jbc.m111.286054;\nRA   Salcedo-Sora J.E., Ochong E., Beveridge S., Johnson D., Nzila A.,\nRA   Biagini G.A., Stocks P.A., O'Neill P.M., Krishna S., Bray P.G., Ward S.A.;\nRT   \"The molecular basis of folate salvage in Plasmodium falciparum:\nRT   characterization of two folate transporters.\";\nRL   J. Biol. Chem. 286:44659-44668(2011).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:10.640562+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 47-55",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "23128f941b579a9921cbe78a9e91da7734842a0f3c2311d1bf182aed647224f0",
  "url": "https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98)

```json
{
  "entry_version": 98,
  "evidence_id": "H3",
  "excerpt": "FT   TRANSMEM        58..78\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:10.640562+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 110-112",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "23128f941b579a9921cbe78a9e91da7734842a0f3c2311d1bf182aed647224f0",
  "url": "https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98)

```json
{
  "entry_version": 98,
  "evidence_id": "H4",
  "excerpt": "FT   TRANSMEM        89..109\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:10.640562+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 113-115",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "23128f941b579a9921cbe78a9e91da7734842a0f3c2311d1bf182aed647224f0",
  "url": "https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98)

```json
{
  "entry_version": 98,
  "evidence_id": "H5",
  "excerpt": "FT   TRANSMEM        122..142\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:10.640562+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 116-118",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "23128f941b579a9921cbe78a9e91da7734842a0f3c2311d1bf182aed647224f0",
  "url": "https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98)

```json
{
  "entry_version": 98,
  "evidence_id": "H6",
  "excerpt": "FT   TRANSMEM        146..166\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:10.640562+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 119-121",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "23128f941b579a9921cbe78a9e91da7734842a0f3c2311d1bf182aed647224f0",
  "url": "https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98)

```json
{
  "entry_version": 98,
  "evidence_id": "H7",
  "excerpt": "FT   TRANSMEM        192..212\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:10.640562+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 122-124",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "23128f941b579a9921cbe78a9e91da7734842a0f3c2311d1bf182aed647224f0",
  "url": "https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98)

```json
{
  "entry_version": 98,
  "evidence_id": "H8",
  "excerpt": "FT   TRANSMEM        216..236\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:10.640562+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 125-127",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "23128f941b579a9921cbe78a9e91da7734842a0f3c2311d1bf182aed647224f0",
  "url": "https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98)

```json
{
  "entry_version": 98,
  "evidence_id": "H9",
  "excerpt": "FT   TRANSMEM        266..286\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:10.640562+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 128-130",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "23128f941b579a9921cbe78a9e91da7734842a0f3c2311d1bf182aed647224f0",
  "url": "https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98)

```json
{
  "entry_version": 98,
  "evidence_id": "H10",
  "excerpt": "FT   TRANSMEM        300..320\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:10.640562+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 131-133",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "23128f941b579a9921cbe78a9e91da7734842a0f3c2311d1bf182aed647224f0",
  "url": "https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98)

```json
{
  "entry_version": 98,
  "evidence_id": "H11",
  "excerpt": "FT   TRANSMEM        326..346\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:10.640562+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 134-136",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "23128f941b579a9921cbe78a9e91da7734842a0f3c2311d1bf182aed647224f0",
  "url": "https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98)

```json
{
  "entry_version": 98,
  "evidence_id": "H12",
  "excerpt": "FT   TRANSMEM        352..372\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:10.640562+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 137-139",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "23128f941b579a9921cbe78a9e91da7734842a0f3c2311d1bf182aed647224f0",
  "url": "https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98)

```json
{
  "entry_version": 98,
  "evidence_id": "H13",
  "excerpt": "FT   TRANSMEM        405..425\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:10.640562+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 140-142",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "23128f941b579a9921cbe78a9e91da7734842a0f3c2311d1bf182aed647224f0",
  "url": "https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98)

```json
{
  "entry_version": 98,
  "evidence_id": "H14",
  "excerpt": "FT   TRANSMEM        431..451\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:10.640562+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 143-145",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "23128f941b579a9921cbe78a9e91da7734842a0f3c2311d1bf182aed647224f0",
  "url": "https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 108. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
