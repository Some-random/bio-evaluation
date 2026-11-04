# transmembrane_0049

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0049.txt)

**Task:** `transmembrane`  
**Expected answer:** **B** — 35..55; 68..88; 99..119; 139..159

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MADFPGKVSTQTSSQEPQRSFAISSSVDMGFIKSIPGILLIAEIVVGLLVWTLIASTPHYLIPALGWVLFVSITLWLLSIALLVILLLSLHQRLPSVPWPLVLLVFYSVAALLYLTAFLANAATVPGGYYQGHLGASAFFGIVETLLYTASSYFAYLGWRGEGQNAAGSTVPV

[Multiple Choices]
A. 35..55; 99..119; 139..159
B. 35..55; 68..88; 99..119; 139..159
C. 35..55
D. 35..55; 63..83; 99..119; 139..159
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

> The matched UniProt record annotates four helical transmembrane regions at 35..55, 68..88, 99..119, and 139..159, matching B. These annotations carry computational evidence code ECO:0000255, so they support the key as database annotation, not as independent experimental confirmation.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has four conspicuously hydrophobic stretches, consistent with a small multipass membrane protein. Their lengths and hydrophobic composition support the four-helix choices B and D, while A omits one such stretch and C omits several. The second stretch has a particularly hydrophobic core around 68..88; the proline near the start of D's 63..83 interval makes B a plausible better boundary estimate.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable knowledge about transmembrane helices and hydrophobic sequence patterns meaningfully distinguishes the four-span options from those listing fewer spans. However, the sequence alone does not sharply establish the precise boundaries of the second interval.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> Both options include the same four apparent hydrophobic spans, and the proposed second intervals overlap substantially. Since the task asks for a segment that crosses the membrane without defining a boundary convention, 63..83 could plausibly identify the same crossing helix as 68..88, despite B being the better-supported boundary estimate.


### Important caveats

- The supplied source evidence is reviewer-only and was not part of the original model input.
- The cited database transmembrane annotations are computationally evidenced, not established here by direct experimental measurements.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has four conspicuously hydrophobic stretches, consistent with a small multipass membrane protein. Their lengths and hydrophobic composition support the four-helix choices B and D, while A omits one such stretch and C omits several. The second stretch has a particularly hydrophobic core around 68..88; the proline near the start of D's 63..83 interval makes B a plausible better boundary estimate.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge about transmembrane helices and hydrophobic sequence patterns meaningfully distinguishes the four-span options from those listing fewer spans. However, the sequence alone does not sharply establish the precise boundaries of the second interval."
  },
  "case_id": "transmembrane_0049",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C8",
      "C10",
      "C12"
    ],
    "judgment": "supported",
    "reason": "The matched UniProt record annotates four helical transmembrane regions at 35..55, 68..88, 99..119, and 139..159, matching B. These annotations carry computational evidence code ECO:0000255, so they support the key as database annotation, not as independent experimental confirmation."
  },
  "important_caveats": [
    "The supplied source evidence is reviewer-only and was not part of the original model input.",
    "The cited database transmembrane annotations are computationally evidenced, not established here by direct experimental measurements."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "Both options include the same four apparent hydrophobic spans, and the proposed second intervals overlap substantially. Since the task asks for a segment that crosses the membrane without defining a boundary convention, 63..83 could plausibly identify the same crossing helix as 68..88, despite B being the better-supported boundary estimate."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0049",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched UniProt record annotates four helical transmembrane regions at 35..55, 68..88, 99..119, and 139..159, matching B. These annotations carry computational evidence code ECO:0000255, so they support the key as database annotation, not as independent experimental confirmation.",
    "evidence_ids": ["C6", "C8", "C10", "C12"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has four conspicuously hydrophobic stretches, consistent with a small multipass membrane protein. Their lengths and hydrophobic composition support the four-helix choices B and D, while A omits one such stretch and C omits several. The second stretch has a particularly hydrophobic core around 68..88; the proline near the start of D's 63..83 interval makes B a plausible better boundary estimate.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge about transmembrane helices and hydrophobic sequence patterns meaningfully distinguishes the four-span options from those listing fewer spans. However, the sequence alone does not sharply establish the precise boundaries of the second interval."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "Both options include the same four apparent hydrophobic spans, and the proposed second intervals overlap substantially. Since the task asks for a segment that crosses the membrane without defining a boundary convention, 63..83 could plausibly identify the same crossing helix as 68..88, despite B being the better-supported boundary estimate."
  },
  "important_caveats": [
    "The supplied source evidence is reviewer-only and was not part of the original model input.",
    "The cited database transmembrane annotations are computationally evidenced, not established here by direct experimental measurements."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for A3KQ86 (Plasmolipin, Zebrafish) explicitly lists four transmembrane helices at 35..55, 68..88, 99..119, and 139..159, matching choice B exactly. The evidence codes are ECO:0000255 (predicted by similarity) and ECO:0000305 (inferred by curator), indicating computational/curator-based annotation rather than direct experimental determination, but the annotation is consistent with the hydrophobicity profile of the sequence. The topological domains (cytoplasmic 1-34, extracellular 56-67, cytoplasmic 89-98, extracellular 120-138, cytoplasmic 160-173) are internally consistent with a 4-TM topology.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [H3](#evidence-h3), [H5](#evidence-h5), [H7](#evidence-h7), [H9](#evidence-h9).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Two layers of transferable reasoning distinguish B from the alternatives. First, the number of TM segments: the 173-AA sequence contains four distinct hydrophobic stretches (~21 residues each) separated by short polar/charged loops, making a 4-TM topology clear and eliminating C (1 TM) and A (3 TMs, which omits the obvious hydrophobic region at ~68-88: VLFVSITLWLLSIALLVILLL). Second, B vs D differ only in the second TM boundary (68..88 vs 63..83). Position 63 is proline, a well-known alpha-helix breaker; TM helices virtually never initiate with proline. The residues 56-67 (STHYLIPALGW) contain serine, threonine, histidine, and tyrosine—polar residues characteristic of a short aqueous loop—while position 68 begins with valine, a canonical helix-forming hydrophobic residue. Additionally, plasmolipin-family proteins are a recognized 4-TM membrane protein family, providing family-level support for exactly four segments. The loop lengths implied by B (12, 10, 19 AA) are more typical of short extracellular/cytoplasmic loops than those implied by D (7, 15, 19 AA).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can identify four hydrophobic segments by hydropathy analysis, eliminate A and C, and then use the proline-helix-breaker rule at position 63 plus the polar composition of the 56-67 loop to favor 68..88 (B) over 63..83 (D). Family-level knowledge of 4-TM plasmolipin proteins further corroborates four segments. No fact specific to this exact protein beyond the sequence itself is required.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The proline at position 63 and the polar residues in the 56-67 stretch provide a clear, concrete sequence-based argument against D's 63..83 boundary. The four hydrophobic stretches are sufficiently distinct to rule out A and C. While exact TM boundaries can have ±1-2 residue uncertainty in practice, the offered choices differ by 5 residues, well within the range where the proline and loop-composition arguments discriminate.


### Important caveats

- The UniProt TM annotations use ECO:0000255 (similarity-based prediction), so they are computational predictions rather than experimentally determined boundaries. The exact residue-level boundaries could shift slightly with different prediction algorithms.
- The reviewer-only evidence confirms the sequence matches A3KQ86 (Plasmolipin, Danio rerio), but the evaluated model was not given the protein name or organism; the reasoning above relies only on the raw sequence and general biological knowledge.
- The third TM region (139..159: FFGIVETLLYTASSYFAYLGW) contains several polar residues (E, T, S, S, Y) and is the least hydrophobic of the four; a strict hydropathy threshold might question it, but all four answer choices include this segment, so it does not affect discrimination among options.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Two layers of transferable reasoning distinguish B from the alternatives. First, the number of TM segments: the 173-AA sequence contains four distinct hydrophobic stretches (~21 residues each) separated by short polar/charged loops, making a 4-TM topology clear and eliminating C (1 TM) and A (3 TMs, which omits the obvious hydrophobic region at ~68-88: VLFVSITLWLLSIALLVILLL). Second, B vs D differ only in the second TM boundary (68..88 vs 63..83). Position 63 is proline, a well-known alpha-helix breaker; TM helices virtually never initiate with proline. The residues 56-67 (STHYLIPALGW) contain serine, threonine, histidine, and tyrosine—polar residues characteristic of a short aqueous loop—while position 68 begins with valine, a canonical helix-forming hydrophobic residue. Additionally, plasmolipin-family proteins are a recognized 4-TM membrane protein family, providing family-level support for exactly four segments. The loop lengths implied by B (12, 10, 19 AA) are more typical of short extracellular/cytoplasmic loops than those implied by D (7, 15, 19 AA).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify four hydrophobic segments by hydropathy analysis, eliminate A and C, and then use the proline-helix-breaker rule at position 63 plus the polar composition of the 56-67 loop to favor 68..88 (B) over 63..83 (D). Family-level knowledge of 4-TM plasmolipin proteins further corroborates four segments. No fact specific to this exact protein beyond the sequence itself is required."
  },
  "case_id": "transmembrane_0049",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C8",
      "C10",
      "C12",
      "H3",
      "H5",
      "H7",
      "H9"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for A3KQ86 (Plasmolipin, Zebrafish) explicitly lists four transmembrane helices at 35..55, 68..88, 99..119, and 139..159, matching choice B exactly. The evidence codes are ECO:0000255 (predicted by similarity) and ECO:0000305 (inferred by curator), indicating computational/curator-based annotation rather than direct experimental determination, but the annotation is consistent with the hydrophobicity profile of the sequence. The topological domains (cytoplasmic 1-34, extracellular 56-67, cytoplasmic 89-98, extracellular 120-138, cytoplasmic 160-173) are internally consistent with a 4-TM topology."
  },
  "important_caveats": [
    "The UniProt TM annotations use ECO:0000255 (similarity-based prediction), so they are computational predictions rather than experimentally determined boundaries. The exact residue-level boundaries could shift slightly with different prediction algorithms.",
    "The reviewer-only evidence confirms the sequence matches A3KQ86 (Plasmolipin, Danio rerio), but the evaluated model was not given the protein name or organism; the reasoning above relies only on the raw sequence and general biological knowledge.",
    "The third TM region (139..159: FFGIVETLLYTASSYFAYLGW) contains several polar residues (E, T, S, S, Y) and is the least hydrophobic of the four; a strict hydropathy threshold might question it, but all four answer choices include this segment, so it does not affect discrimination among options."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The proline at position 63 and the polar residues in the 56-67 stretch provide a clear, concrete sequence-based argument against D's 63..83 boundary. The four hydrophobic stretches are sufficiently distinct to rule out A and C. While exact TM boundaries can have ±1-2 residue uncertainty in practice, the offered choices differ by 5 residues, well within the range where the proline and loop-composition arguments discriminate."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0049",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for A3KQ86 (Plasmolipin, Zebrafish) explicitly lists four transmembrane helices at 35..55, 68..88, 99..119, and 139..159, matching choice B exactly. The evidence codes are ECO:0000255 (predicted by similarity) and ECO:0000305 (inferred by curator), indicating computational/curator-based annotation rather than direct experimental determination, but the annotation is consistent with the hydrophobicity profile of the sequence. The topological domains (cytoplasmic 1-34, extracellular 56-67, cytoplasmic 89-98, extracellular 120-138, cytoplasmic 160-173) are internally consistent with a 4-TM topology.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "H3", "H5", "H7", "H9"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Two layers of transferable reasoning distinguish B from the alternatives. First, the number of TM segments: the 173-AA sequence contains four distinct hydrophobic stretches (~21 residues each) separated by short polar/charged loops, making a 4-TM topology clear and eliminating C (1 TM) and A (3 TMs, which omits the obvious hydrophobic region at ~68-88: VLFVSITLWLLSIALLVILLL). Second, B vs D differ only in the second TM boundary (68..88 vs 63..83). Position 63 is proline, a well-known alpha-helix breaker; TM helices virtually never initiate with proline. The residues 56-67 (STHYLIPALGW) contain serine, threonine, histidine, and tyrosine—polar residues characteristic of a short aqueous loop—while position 68 begins with valine, a canonical helix-forming hydrophobic residue. Additionally, plasmolipin-family proteins are a recognized 4-TM membrane protein family, providing family-level support for exactly four segments. The loop lengths implied by B (12, 10, 19 AA) are more typical of short extracellular/cytoplasmic loops than those implied by D (7, 15, 19 AA).",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify four hydrophobic segments by hydropathy analysis, eliminate A and C, and then use the proline-helix-breaker rule at position 63 plus the polar composition of the 56-67 loop to favor 68..88 (B) over 63..83 (D). Family-level knowledge of 4-TM plasmolipin proteins further corroborates four segments. No fact specific to this exact protein beyond the sequence itself is required."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The proline at position 63 and the polar residues in the 56-67 stretch provide a clear, concrete sequence-based argument against D's 63..83 boundary. The four hydrophobic stretches are sufficiently distinct to rule out A and C. While exact TM boundaries can have ±1-2 residue uncertainty in practice, the offered choices differ by 5 residues, well within the range where the proline and loop-composition arguments discriminate."
  },
  "important_caveats": [
    "The UniProt TM annotations use ECO:0000255 (similarity-based prediction), so they are computational predictions rather than experimentally determined boundaries. The exact residue-level boundaries could shift slightly with different prediction algorithms.",
    "The reviewer-only evidence confirms the sequence matches A3KQ86 (Plasmolipin, Danio rerio), but the evaluated model was not given the protein name or organism; the reasoning above relies only on the raw sequence and general biological knowledge.",
    "The third TM region (139..159: FFGIVETLLYTASSYFAYLGW) contains several polar residues (E, T, S, S, Y) and is the least hydrophobic of the four; a strict hydropathy threshold might question it, but all four answer choices include this segment, so it does not affect discrimination among options."
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
  "benchmark_sequence_length": 173,
  "benchmark_sequence_sha256": "41896d53c37932e1e171f9fcec9cd1931289884cdd217d271fb4438225cae35a",
  "current_entry_audit": {
    "entryVersion": 123,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2007-04-03",
    "sequenceVersion": 1
  },
  "current_record_sha256": "71db059b7d92b9cbb982c45261c2eacda70b05b9667017a735c6b72a71c6846e",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 173,
  "current_source_sequence_sha256": "41896d53c37932e1e171f9fcec9cd1931289884cdd217d271fb4438225cae35a",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 121,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A3KQ86",
  "selected_historical_entry_version": 121,
  "selected_historical_record_sha256": "a6866759886a22c2e64aae8941e7fe997c98c66a52079a88daaa7c18d3ddd601",
  "selected_historical_source_sequence_length": 173,
  "selected_historical_source_sequence_sha256": "41896d53c37932e1e171f9fcec9cd1931289884cdd217d271fb4438225cae35a",
  "selected_historical_version": {
    "accession": "A3KQ86",
    "database": "Swiss-Prot",
    "entryVersion": 121,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "PLLP_DANRE",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3KQ86.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A3KQ86\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:26:56.110007+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "71db059b7d92b9cbb982c45261c2eacda70b05b9667017a735c6b72a71c6846e",
  "url": "https://rest.uniprot.org/uniprotkb/A3KQ86.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3KQ86.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":123,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2007-04-03\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:26:56.110007+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "71db059b7d92b9cbb982c45261c2eacda70b05b9667017a735c6b72a71c6846e",
  "url": "https://rest.uniprot.org/uniprotkb/A3KQ86.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3KQ86.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Zebrafish\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Euteleostomi\",\"Actinopterygii\",\"Neopterygii\",\"Teleostei\",\"Ostariophysi\",\"Cypriniformes\",\"Danionidae\",\"Danioninae\",\"Danio\"],\"scientificName\":\"Danio rerio\",\"synonyms\":[\"Brachydanio rerio\"],\"taxonId\":7955}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:26:56.110007+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "71db059b7d92b9cbb982c45261c2eacda70b05b9667017a735c6b72a71c6846e",
  "url": "https://rest.uniprot.org/uniprotkb/A3KQ86.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3KQ86.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"value\":\"Plasma membrane proteolipid\"}}],\"recommendedName\":{\"fullName\":{\"value\":\"Plasmolipin\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:26:56.110007+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "71db059b7d92b9cbb982c45261c2eacda70b05b9667017a735c6b72a71c6846e",
  "url": "https://rest.uniprot.org/uniprotkb/A3KQ86.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3KQ86.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":34},\"start\":{\"modifier\":\"EXACT\",\"value\":1}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:26:56.110007+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "71db059b7d92b9cbb982c45261c2eacda70b05b9667017a735c6b72a71c6846e",
  "url": "https://rest.uniprot.org/uniprotkb/A3KQ86.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3KQ86.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":55},\"start\":{\"modifier\":\"EXACT\",\"value\":35}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:26:56.110007+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "71db059b7d92b9cbb982c45261c2eacda70b05b9667017a735c6b72a71c6846e",
  "url": "https://rest.uniprot.org/uniprotkb/A3KQ86.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3KQ86.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":67},\"start\":{\"modifier\":\"EXACT\",\"value\":56}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:26:56.110007+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "71db059b7d92b9cbb982c45261c2eacda70b05b9667017a735c6b72a71c6846e",
  "url": "https://rest.uniprot.org/uniprotkb/A3KQ86.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3KQ86.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":88},\"start\":{\"modifier\":\"EXACT\",\"value\":68}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:26:56.110007+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "71db059b7d92b9cbb982c45261c2eacda70b05b9667017a735c6b72a71c6846e",
  "url": "https://rest.uniprot.org/uniprotkb/A3KQ86.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3KQ86.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":98},\"start\":{\"modifier\":\"EXACT\",\"value\":89}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:26:56.110007+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "71db059b7d92b9cbb982c45261c2eacda70b05b9667017a735c6b72a71c6846e",
  "url": "https://rest.uniprot.org/uniprotkb/A3KQ86.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3KQ86.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":119},\"start\":{\"modifier\":\"EXACT\",\"value\":99}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:26:56.110007+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "71db059b7d92b9cbb982c45261c2eacda70b05b9667017a735c6b72a71c6846e",
  "url": "https://rest.uniprot.org/uniprotkb/A3KQ86.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3KQ86.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":138},\"start\":{\"modifier\":\"EXACT\",\"value\":120}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:26:56.110007+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "71db059b7d92b9cbb982c45261c2eacda70b05b9667017a735c6b72a71c6846e",
  "url": "https://rest.uniprot.org/uniprotkb/A3KQ86.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3KQ86.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":159},\"start\":{\"modifier\":\"EXACT\",\"value\":139}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:26:56.110007+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "71db059b7d92b9cbb982c45261c2eacda70b05b9667017a735c6b72a71c6846e",
  "url": "https://rest.uniprot.org/uniprotkb/A3KQ86.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3KQ86.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":173},\"start\":{\"modifier\":\"EXACT\",\"value\":160}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-02T04:26:56.110007+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "71db059b7d92b9cbb982c45261c2eacda70b05b9667017a735c6b72a71c6846e",
  "url": "https://rest.uniprot.org/uniprotkb/A3KQ86.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3KQ86?format=txt&versions=121)

```json
{
  "entry_version": 121,
  "evidence_id": "H1",
  "excerpt": "ID   PLLP_DANRE              Reviewed;         173 AA.\nAC   A3KQ86; F6NKZ5;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   03-APR-2007, sequence version 1.\nDT   28-JAN-2026, entry version 121.\nDE   RecName: Full=Plasmolipin;\nDE   AltName: Full=Plasma membrane proteolipid;\nGN   Name=pllp; ORFNames=si:dkey-73n10.4;\nOS   Danio rerio (Zebrafish) (Brachydanio rerio).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi;\nOC   Actinopterygii; Neopterygii; Teleostei; Ostariophysi; Cypriniformes;\nOC   Danionidae; Danioninae; Danio.\nOX   NCBI_TaxID=7955;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:58.657829+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a6866759886a22c2e64aae8941e7fe997c98c66a52079a88daaa7c18d3ddd601",
  "url": "https://rest.uniprot.org/unisave/A3KQ86?format=txt&versions=121"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3KQ86?format=txt&versions=121)

```json
{
  "entry_version": 121,
  "evidence_id": "H2",
  "excerpt": "FT   TOPO_DOM        1..34\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:58.657829+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 150-152",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a6866759886a22c2e64aae8941e7fe997c98c66a52079a88daaa7c18d3ddd601",
  "url": "https://rest.uniprot.org/unisave/A3KQ86?format=txt&versions=121"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3KQ86?format=txt&versions=121)

```json
{
  "entry_version": 121,
  "evidence_id": "H3",
  "excerpt": "FT   TRANSMEM        35..55\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:58.657829+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 153-155",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a6866759886a22c2e64aae8941e7fe997c98c66a52079a88daaa7c18d3ddd601",
  "url": "https://rest.uniprot.org/unisave/A3KQ86?format=txt&versions=121"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3KQ86?format=txt&versions=121)

```json
{
  "entry_version": 121,
  "evidence_id": "H4",
  "excerpt": "FT   TOPO_DOM        56..67\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:58.657829+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 156-158",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a6866759886a22c2e64aae8941e7fe997c98c66a52079a88daaa7c18d3ddd601",
  "url": "https://rest.uniprot.org/unisave/A3KQ86?format=txt&versions=121"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3KQ86?format=txt&versions=121)

```json
{
  "entry_version": 121,
  "evidence_id": "H5",
  "excerpt": "FT   TRANSMEM        68..88\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:58.657829+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 159-161",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a6866759886a22c2e64aae8941e7fe997c98c66a52079a88daaa7c18d3ddd601",
  "url": "https://rest.uniprot.org/unisave/A3KQ86?format=txt&versions=121"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3KQ86?format=txt&versions=121)

```json
{
  "entry_version": 121,
  "evidence_id": "H6",
  "excerpt": "FT   TOPO_DOM        89..98\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:58.657829+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 162-164",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a6866759886a22c2e64aae8941e7fe997c98c66a52079a88daaa7c18d3ddd601",
  "url": "https://rest.uniprot.org/unisave/A3KQ86?format=txt&versions=121"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3KQ86?format=txt&versions=121)

```json
{
  "entry_version": 121,
  "evidence_id": "H7",
  "excerpt": "FT   TRANSMEM        99..119\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:58.657829+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 165-167",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a6866759886a22c2e64aae8941e7fe997c98c66a52079a88daaa7c18d3ddd601",
  "url": "https://rest.uniprot.org/unisave/A3KQ86?format=txt&versions=121"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3KQ86?format=txt&versions=121)

```json
{
  "entry_version": 121,
  "evidence_id": "H8",
  "excerpt": "FT   TOPO_DOM        120..138\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:58.657829+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 168-170",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a6866759886a22c2e64aae8941e7fe997c98c66a52079a88daaa7c18d3ddd601",
  "url": "https://rest.uniprot.org/unisave/A3KQ86?format=txt&versions=121"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3KQ86?format=txt&versions=121)

```json
{
  "entry_version": 121,
  "evidence_id": "H9",
  "excerpt": "FT   TRANSMEM        139..159\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:58.657829+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 171-173",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a6866759886a22c2e64aae8941e7fe997c98c66a52079a88daaa7c18d3ddd601",
  "url": "https://rest.uniprot.org/unisave/A3KQ86?format=txt&versions=121"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3KQ86?format=txt&versions=121)

```json
{
  "entry_version": 121,
  "evidence_id": "H10",
  "excerpt": "FT   TOPO_DOM        160..173\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:58.657829+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 174-176",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a6866759886a22c2e64aae8941e7fe997c98c66a52079a88daaa7c18d3ddd601",
  "url": "https://rest.uniprot.org/unisave/A3KQ86?format=txt&versions=121"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 49. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
