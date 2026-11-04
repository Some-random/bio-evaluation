# transmembrane_0092

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0092.txt)

**Task:** `transmembrane`  
**Expected answer:** **D** — 6..26; 300..320; 337..357; 373..393; 416..436; 439..459

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MGLTDIFLNLLLFVYPAVFIIYQIILYEISARKQINQEALKYSNLPVLSIIVPIKNEEISVIQGLLDNLSNLIWDKKKLEIIIVSDDNEDYFTKIINTVKVPKDLTVYFYRREKKLGYKSGALQYGFEKATGDLILTIDVDSRLPPNALINAYEKMQSNTCDAIVFQWNGYSSNQYSTLAKGMVVSTLFASKALFEGKEKLKLKIYPVGSGTMFSREALRVVNGWDYRLVQDDLEIGTRLIYNGKNVCASGIPIYVEVPDNFYSFYVQQTRWAMGSAEVLRNRLKYIIKSKISFTQRMDLIIYLLQYTPVIVTFFISTLLSLMLPFRIGHDPLNSPALLFWLVSLGLYASLLLSLALKLGLNLKDSLMGIGRLTAFTVSISPFIVFNFFKGLLKSGNTYVITPKGTVKKTNKLLRIIAIIGVFGLLYLLSSILYIYEGYYVTGIWLLYYSSAYLYTMLLYYKEL

[Multiple Choices]
A. 6..26; 300..320; 337..357; 372..388; 416..436; 439..459
B. 6..26; 337..357; 373..393; 416..436; 439..459
C. 1..21
D. 6..26; 300..320; 337..357; 373..393; 416..436; 439..459
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

> The sequence-matched historical UniProt entry annotates all six intervals in D as transmembrane helices. The annotations use ECO:0000255, indicating computational evidence rather than establishing experimental verification, but they support the keyed intervals for this sequence.

Citations as saved: [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a strongly hydrophobic N-terminal stretch and multiple later hydrophobic stretches, separated by more polar regions—a familiar pattern for a multi-pass membrane protein. Hydropathy and typical membrane-helix lengths favor the six-helix set in D: it includes the hydrophobic region around 300..320 and uses a 21-residue interval at 373..393, whereas B omits the former and A gives a notably shorter interval for the latter. This is a transferable sequence-pattern inference, not proof of exact boundaries.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The offered intervals can be compared with recognizable hydrophobic segments in the supplied sequence, so distinguishing the choices does not require knowing this protein's database record. Exact helix boundaries remain predictions from sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> A differs from D by giving a shorter interval for one hydrophobic stretch, but the longer, typical-length interval in D is the more plausible full transmembrane helix. Boundary uncertainty does not make A equally defensible here.


### Important caveats

- The reviewer-only annotation is computational, not experimental evidence.
- The historical entry's sequence matches the supplied sequence; the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a strongly hydrophobic N-terminal stretch and multiple later hydrophobic stretches, separated by more polar regions—a familiar pattern for a multi-pass membrane protein. Hydropathy and typical membrane-helix lengths favor the six-helix set in D: it includes the hydrophobic region around 300..320 and uses a 21-residue interval at 373..393, whereas B omits the former and A gives a notably shorter interval for the latter. This is a transferable sequence-pattern inference, not proof of exact boundaries.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The offered intervals can be compared with recognizable hydrophobic segments in the supplied sequence, so distinguishing the choices does not require knowing this protein's database record. Exact helix boundaries remain predictions from sequence alone."
  },
  "case_id": "transmembrane_0092",
  "expected_answer_check": {
    "evidence_ids": [
      "H2",
      "H3",
      "H4",
      "H5",
      "H6",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt entry annotates all six intervals in D as transmembrane helices. The annotations use ECO:0000255, indicating computational evidence rather than establishing experimental verification, but they support the keyed intervals for this sequence."
  },
  "important_caveats": [
    "The reviewer-only annotation is computational, not experimental evidence.",
    "The historical entry's sequence matches the supplied sequence; the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A differs from D by giving a shorter interval for one hydrophobic stretch, but the longer, typical-length interval in D is the more plausible full transmembrane helix. Boundary uncertainty does not make A equally defensible here."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0092",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt entry annotates all six intervals in D as transmembrane helices. The annotations use ECO:0000255, indicating computational evidence rather than establishing experimental verification, but they support the keyed intervals for this sequence.",
    "evidence_ids": ["H2", "H3", "H4", "H5", "H6", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a strongly hydrophobic N-terminal stretch and multiple later hydrophobic stretches, separated by more polar regions—a familiar pattern for a multi-pass membrane protein. Hydropathy and typical membrane-helix lengths favor the six-helix set in D: it includes the hydrophobic region around 300..320 and uses a 21-residue interval at 373..393, whereas B omits the former and A gives a notably shorter interval for the latter. This is a transferable sequence-pattern inference, not proof of exact boundaries.",
    "missing_item_specific_fact": "",
    "reason": "The offered intervals can be compared with recognizable hydrophobic segments in the supplied sequence, so distinguishing the choices does not require knowing this protein's database record. Exact helix boundaries remain predictions from sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A differs from D by giving a shorter interval for one hydrophobic stretch, but the longer, typical-length interval in D is the more plausible full transmembrane helix. Boundary uncertainty does not make A equally defensible here."
  },
  "important_caveats": [
    "The reviewer-only annotation is computational, not experimental evidence.",
    "The historical entry's sequence matches the supplied sequence; the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for Q4J8Q7 (Y1499_SULAC, Sulfolobus acidocaldarius) lists exactly six transmembrane helical segments at 6..26, 300..320, 337..357, 373..393, 416..436, and 439..459, matching option D verbatim. All six annotations carry evidence code ECO:0000255 (inferred by similarity), so they are computational predictions rather than experimentally determined boundaries. The sequence matches the benchmark input exactly (464 residues, SHA-256 confirmed). The annotation is consistent with the hydrophobic stretches visible in the C-terminal region of the supplied sequence.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The C-terminal ~180 residues of this 464-aa protein contain multiple consecutive hydrophobic stretches separated by short polar loops, a hallmark of a multi-pass membrane protein. Hydropathy analysis of the sequence identifies six such stretches: (1) residues 6–26 (IFLNLLLFVYPAVFIIYQIIL), a clear N-terminal TM helix; (2) residues ~300–320 (IIYLLQYTPVIVTFFISTLL), a moderately hydrophobic segment; (3) residues ~337–357 (PALLFWLVSLGLYASLLLSLA); (4) residues ~373–393 (LTAFTVSISPFIVFNFFKGLL); (5) residues ~416–436 (NKLLRIIAIIGVFGLLYLLS); (6) residues ~439–459 (ILYIYEGYYVTGIWLLYYSSA). Option C (single 21-residue helix at 1..21) is eliminated immediately. Option B omits the 300..320 helix; a hydropathy scan reveals a hydrophobic cluster in that window (L, I, I, Y, L, L, V, I, V, F, F, I, L, L), so a model performing standard hydrophobicity profiling should detect it. The A-vs-D distinction hinges on the fourth helix boundary: A gives 372..388 (17 residues) while D gives 373..393 (21 residues). Two transferable arguments favor D: (a) canonical TM α-helices spanning a lipid bilayer are typically 18–25 residues, making a 17-residue segment (A) short and a 21-residue segment (D) more typical; (b) position 372 is glycine, which is uncommon at the helix core start and more characteristic of a loop/boundary residue, whereas position 373 is leucine, a standard helix-forming residue. These family-level and biophysical regularities learned from many membrane proteins provide a defensible, if not airtight, basis for preferring D over A.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model can identify the overall multi-pass topology (six TM segments) from the hydrophobic pattern in the C-terminal region, eliminating C and B. The A-vs-D boundary difference (372..388 vs 373..393) is subtle, but the helix-length norm (18–25 residues) and the glycine-vs-leucine start-residue argument provide a concrete, transferable biological rationale for choosing D. The annotation is computational (ECO:0000255), so the 'correct' boundaries themselves are algorithm-dependent, but the question's choices are sufficiently separated that transferable knowledge meaningfully narrows the answer.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> Options A and D differ only in the fourth TM helix boundary: 372..388 (17 residues) vs 373..393 (21 residues). Both windows overlap substantially and contain a mix of hydrophobic and mildly polar residues. The 5-residue extension in D includes K(390), a charged residue unusual inside a TM helix, which could argue for the shorter A boundary. Conversely, the 21-residue length of D is more typical for a bilayer-spanning helix. Without the exact annotation, a careful hydropathy analysis could plausibly land on either boundary, making both A and D defensible.


### Important caveats

- All six UniProt TM annotations carry ECO:0000255 (inferred by similarity), meaning they are computational predictions, not experimentally verified boundaries. The 'correct' answer reflects a specific prediction algorithm's output.
- The A-vs-D distinction (372..388 vs 373..393) is within the typical ±3–5 residue uncertainty of TM prediction tools, so the boundary difference is not a sharply defined biological fact.
- The protein is from Sulfolobus acidocaldarius (Archaea); membrane composition and helix-length norms may differ slightly from bacterial/eukaryotic references, though the general hydrophobic-helix principle applies.
- The reviewer-only UniProt accession and organism identity were not available to the evaluated model; the reasoning above relies only on the supplied sequence and general membrane-protein knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The C-terminal ~180 residues of this 464-aa protein contain multiple consecutive hydrophobic stretches separated by short polar loops, a hallmark of a multi-pass membrane protein. Hydropathy analysis of the sequence identifies six such stretches: (1) residues 6–26 (IFLNLLLFVYPAVFIIYQIIL), a clear N-terminal TM helix; (2) residues ~300–320 (IIYLLQYTPVIVTFFISTLL), a moderately hydrophobic segment; (3) residues ~337–357 (PALLFWLVSLGLYASLLLSLA); (4) residues ~373–393 (LTAFTVSISPFIVFNFFKGLL); (5) residues ~416–436 (NKLLRIIAIIGVFGLLYLLS); (6) residues ~439–459 (ILYIYEGYYVTGIWLLYYSSA). Option C (single 21-residue helix at 1..21) is eliminated immediately. Option B omits the 300..320 helix; a hydropathy scan reveals a hydrophobic cluster in that window (L, I, I, Y, L, L, V, I, V, F, F, I, L, L), so a model performing standard hydrophobicity profiling should detect it. The A-vs-D distinction hinges on the fourth helix boundary: A gives 372..388 (17 residues) while D gives 373..393 (21 residues). Two transferable arguments favor D: (a) canonical TM α-helices spanning a lipid bilayer are typically 18–25 residues, making a 17-residue segment (A) short and a 21-residue segment (D) more typical; (b) position 372 is glycine, which is uncommon at the helix core start and more characteristic of a loop/boundary residue, whereas position 373 is leucine, a standard helix-forming residue. These family-level and biophysical regularities learned from many membrane proteins provide a defensible, if not airtight, basis for preferring D over A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model can identify the overall multi-pass topology (six TM segments) from the hydrophobic pattern in the C-terminal region, eliminating C and B. The A-vs-D boundary difference (372..388 vs 373..393) is subtle, but the helix-length norm (18–25 residues) and the glycine-vs-leucine start-residue argument provide a concrete, transferable biological rationale for choosing D. The annotation is computational (ECO:0000255), so the 'correct' boundaries themselves are algorithm-dependent, but the question's choices are sufficiently separated that transferable knowledge meaningfully narrows the answer."
  },
  "case_id": "transmembrane_0092",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "C10",
      "H2",
      "H3",
      "H4",
      "H5",
      "H6",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for Q4J8Q7 (Y1499_SULAC, Sulfolobus acidocaldarius) lists exactly six transmembrane helical segments at 6..26, 300..320, 337..357, 373..393, 416..436, and 439..459, matching option D verbatim. All six annotations carry evidence code ECO:0000255 (inferred by similarity), so they are computational predictions rather than experimentally determined boundaries. The sequence matches the benchmark input exactly (464 residues, SHA-256 confirmed). The annotation is consistent with the hydrophobic stretches visible in the C-terminal region of the supplied sequence."
  },
  "important_caveats": [
    "All six UniProt TM annotations carry ECO:0000255 (inferred by similarity), meaning they are computational predictions, not experimentally verified boundaries. The 'correct' answer reflects a specific prediction algorithm's output.",
    "The A-vs-D distinction (372..388 vs 373..393) is within the typical ±3–5 residue uncertainty of TM prediction tools, so the boundary difference is not a sharply defined biological fact.",
    "The protein is from Sulfolobus acidocaldarius (Archaea); membrane composition and helix-length norms may differ slightly from bacterial/eukaryotic references, though the general hydrophobic-helix principle applies.",
    "The reviewer-only UniProt accession and organism identity were not available to the evaluated model; the reasoning above relies only on the supplied sequence and general membrane-protein knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "Options A and D differ only in the fourth TM helix boundary: 372..388 (17 residues) vs 373..393 (21 residues). Both windows overlap substantially and contain a mix of hydrophobic and mildly polar residues. The 5-residue extension in D includes K(390), a charged residue unusual inside a TM helix, which could argue for the shorter A boundary. Conversely, the 21-residue length of D is more typical for a bilayer-spanning helix. Without the exact annotation, a careful hydropathy analysis could plausibly land on either boundary, making both A and D defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0092",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for Q4J8Q7 (Y1499_SULAC, Sulfolobus acidocaldarius) lists exactly six transmembrane helical segments at 6..26, 300..320, 337..357, 373..393, 416..436, and 439..459, matching option D verbatim. All six annotations carry evidence code ECO:0000255 (inferred by similarity), so they are computational predictions rather than experimentally determined boundaries. The sequence matches the benchmark input exactly (464 residues, SHA-256 confirmed). The annotation is consistent with the hydrophobic stretches visible in the C-terminal region of the supplied sequence.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "H2", "H3", "H4", "H5", "H6", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The C-terminal ~180 residues of this 464-aa protein contain multiple consecutive hydrophobic stretches separated by short polar loops, a hallmark of a multi-pass membrane protein. Hydropathy analysis of the sequence identifies six such stretches: (1) residues 6–26 (IFLNLLLFVYPAVFIIYQIIL), a clear N-terminal TM helix; (2) residues ~300–320 (IIYLLQYTPVIVTFFISTLL), a moderately hydrophobic segment; (3) residues ~337–357 (PALLFWLVSLGLYASLLLSLA); (4) residues ~373–393 (LTAFTVSISPFIVFNFFKGLL); (5) residues ~416–436 (NKLLRIIAIIGVFGLLYLLS); (6) residues ~439–459 (ILYIYEGYYVTGIWLLYYSSA). Option C (single 21-residue helix at 1..21) is eliminated immediately. Option B omits the 300..320 helix; a hydropathy scan reveals a hydrophobic cluster in that window (L, I, I, Y, L, L, V, I, V, F, F, I, L, L), so a model performing standard hydrophobicity profiling should detect it. The A-vs-D distinction hinges on the fourth helix boundary: A gives 372..388 (17 residues) while D gives 373..393 (21 residues). Two transferable arguments favor D: (a) canonical TM α-helices spanning a lipid bilayer are typically 18–25 residues, making a 17-residue segment (A) short and a 21-residue segment (D) more typical; (b) position 372 is glycine, which is uncommon at the helix core start and more characteristic of a loop/boundary residue, whereas position 373 is leucine, a standard helix-forming residue. These family-level and biophysical regularities learned from many membrane proteins provide a defensible, if not airtight, basis for preferring D over A.",
    "missing_item_specific_fact": "",
    "reason": "A model can identify the overall multi-pass topology (six TM segments) from the hydrophobic pattern in the C-terminal region, eliminating C and B. The A-vs-D boundary difference (372..388 vs 373..393) is subtle, but the helix-length norm (18–25 residues) and the glycine-vs-leucine start-residue argument provide a concrete, transferable biological rationale for choosing D. The annotation is computational (ECO:0000255), so the 'correct' boundaries themselves are algorithm-dependent, but the question's choices are sufficiently separated that transferable knowledge meaningfully narrows the answer."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "Options A and D differ only in the fourth TM helix boundary: 372..388 (17 residues) vs 373..393 (21 residues). Both windows overlap substantially and contain a mix of hydrophobic and mildly polar residues. The 5-residue extension in D includes K(390), a charged residue unusual inside a TM helix, which could argue for the shorter A boundary. Conversely, the 21-residue length of D is more typical for a bilayer-spanning helix. Without the exact annotation, a careful hydropathy analysis could plausibly land on either boundary, making both A and D defensible."
  },
  "important_caveats": [
    "All six UniProt TM annotations carry ECO:0000255 (inferred by similarity), meaning they are computational predictions, not experimentally verified boundaries. The 'correct' answer reflects a specific prediction algorithm's output.",
    "The A-vs-D distinction (372..388 vs 373..393) is within the typical ±3–5 residue uncertainty of TM prediction tools, so the boundary difference is not a sharply defined biological fact.",
    "The protein is from Sulfolobus acidocaldarius (Archaea); membrane composition and helix-length norms may differ slightly from bacterial/eukaryotic references, though the general hydrophobic-helix principle applies.",
    "The reviewer-only UniProt accession and organism identity were not available to the evaluated model; the reasoning above relies only on the supplied sequence and general membrane-protein knowledge."
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
  "benchmark_sequence_length": 464,
  "benchmark_sequence_sha256": "72c1798b49bae9f57c5f8f2af2190336eda2aa84ac1f7c439509152b3e010ed3",
  "current_entry_audit": {
    "entryVersion": 85,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2005-08-02",
    "sequenceVersion": 1
  },
  "current_record_sha256": "3e85eec2dfbc367c39396a2802767d7bd8d7eecdc2ad5665df5f0b909ffd12ee",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 464,
  "current_source_sequence_sha256": "72c1798b49bae9f57c5f8f2af2190336eda2aa84ac1f7c439509152b3e010ed3",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 83,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q4J8Q7",
  "selected_historical_entry_version": 83,
  "selected_historical_record_sha256": "77a0391d87d26f83f55657f76a4009b13d967514999d8b969ae7fda3d19b4120",
  "selected_historical_source_sequence_length": 464,
  "selected_historical_source_sequence_sha256": "72c1798b49bae9f57c5f8f2af2190336eda2aa84ac1f7c439509152b3e010ed3",
  "selected_historical_version": {
    "accession": "Q4J8Q7",
    "database": "Swiss-Prot",
    "entryVersion": 83,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "Y1499_SULAC",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4J8Q7.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q4J8Q7\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:30:48.833149+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3e85eec2dfbc367c39396a2802767d7bd8d7eecdc2ad5665df5f0b909ffd12ee",
  "url": "https://rest.uniprot.org/uniprotkb/Q4J8Q7.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4J8Q7.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":85,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2005-08-02\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:30:48.833149+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3e85eec2dfbc367c39396a2802767d7bd8d7eecdc2ad5665df5f0b909ffd12ee",
  "url": "https://rest.uniprot.org/uniprotkb/Q4J8Q7.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4J8Q7.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Archaea\",\"Thermoproteota\",\"Thermoprotei\",\"Sulfolobales\",\"Sulfolobaceae\",\"Sulfolobus\"],\"scientificName\":\"Sulfolobus acidocaldarius (strain ATCC 33909 / DSM 639 / JCM 8929 / NBRC 15157 / NCIMB 11770)\",\"taxonId\":330779}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:30:48.833149+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3e85eec2dfbc367c39396a2802767d7bd8d7eecdc2ad5665df5f0b909ffd12ee",
  "url": "https://rest.uniprot.org/uniprotkb/Q4J8Q7.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4J8Q7.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"value\":\"2.4.-.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Probable glycosyltransferase Saci_1499\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:30:48.833149+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3e85eec2dfbc367c39396a2802767d7bd8d7eecdc2ad5665df5f0b909ffd12ee",
  "url": "https://rest.uniprot.org/uniprotkb/Q4J8Q7.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4J8Q7.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":26},\"start\":{\"modifier\":\"EXACT\",\"value\":6}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:30:48.833149+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3e85eec2dfbc367c39396a2802767d7bd8d7eecdc2ad5665df5f0b909ffd12ee",
  "url": "https://rest.uniprot.org/uniprotkb/Q4J8Q7.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4J8Q7.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":320},\"start\":{\"modifier\":\"EXACT\",\"value\":300}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:30:48.833149+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3e85eec2dfbc367c39396a2802767d7bd8d7eecdc2ad5665df5f0b909ffd12ee",
  "url": "https://rest.uniprot.org/uniprotkb/Q4J8Q7.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4J8Q7.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":357},\"start\":{\"modifier\":\"EXACT\",\"value\":337}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:30:48.833149+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3e85eec2dfbc367c39396a2802767d7bd8d7eecdc2ad5665df5f0b909ffd12ee",
  "url": "https://rest.uniprot.org/uniprotkb/Q4J8Q7.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4J8Q7.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":393},\"start\":{\"modifier\":\"EXACT\",\"value\":373}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:30:48.833149+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3e85eec2dfbc367c39396a2802767d7bd8d7eecdc2ad5665df5f0b909ffd12ee",
  "url": "https://rest.uniprot.org/uniprotkb/Q4J8Q7.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4J8Q7.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":436},\"start\":{\"modifier\":\"EXACT\",\"value\":416}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:30:48.833149+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3e85eec2dfbc367c39396a2802767d7bd8d7eecdc2ad5665df5f0b909ffd12ee",
  "url": "https://rest.uniprot.org/uniprotkb/Q4J8Q7.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4J8Q7.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":459},\"start\":{\"modifier\":\"EXACT\",\"value\":439}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:30:48.833149+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3e85eec2dfbc367c39396a2802767d7bd8d7eecdc2ad5665df5f0b909ffd12ee",
  "url": "https://rest.uniprot.org/uniprotkb/Q4J8Q7.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4J8Q7?format=txt&versions=83)

```json
{
  "entry_version": 83,
  "evidence_id": "H1",
  "excerpt": "ID   Y1499_SULAC             Reviewed;         464 AA.\nAC   Q4J8Q7;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   02-AUG-2005, sequence version 1.\nDT   28-JAN-2026, entry version 83.\nDE   RecName: Full=Probable glycosyltransferase Saci_1499 {ECO:0000305};\nDE            EC=2.4.-.-;\nGN   OrderedLocusNames=Saci_1499 {ECO:0000312|EMBL:AAY80820.1};\nOS   Sulfolobus acidocaldarius (strain ATCC 33909 / DSM 639 / JCM 8929 / NBRC\nOS   15157 / NCIMB 11770).\nOC   Archaea; Thermoproteota; Thermoprotei; Sulfolobales; Sulfolobaceae;\nOC   Sulfolobus.\nOX   NCBI_TaxID=330779;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:51.056852+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "77a0391d87d26f83f55657f76a4009b13d967514999d8b969ae7fda3d19b4120",
  "url": "https://rest.uniprot.org/unisave/Q4J8Q7?format=txt&versions=83"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4J8Q7?format=txt&versions=83)

```json
{
  "entry_version": 83,
  "evidence_id": "H2",
  "excerpt": "FT   TRANSMEM        6..26\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:51.056852+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 73-75",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "77a0391d87d26f83f55657f76a4009b13d967514999d8b969ae7fda3d19b4120",
  "url": "https://rest.uniprot.org/unisave/Q4J8Q7?format=txt&versions=83"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4J8Q7?format=txt&versions=83)

```json
{
  "entry_version": 83,
  "evidence_id": "H3",
  "excerpt": "FT   TRANSMEM        300..320\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:51.056852+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 76-78",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "77a0391d87d26f83f55657f76a4009b13d967514999d8b969ae7fda3d19b4120",
  "url": "https://rest.uniprot.org/unisave/Q4J8Q7?format=txt&versions=83"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4J8Q7?format=txt&versions=83)

```json
{
  "entry_version": 83,
  "evidence_id": "H4",
  "excerpt": "FT   TRANSMEM        337..357\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:51.056852+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 79-81",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "77a0391d87d26f83f55657f76a4009b13d967514999d8b969ae7fda3d19b4120",
  "url": "https://rest.uniprot.org/unisave/Q4J8Q7?format=txt&versions=83"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4J8Q7?format=txt&versions=83)

```json
{
  "entry_version": 83,
  "evidence_id": "H5",
  "excerpt": "FT   TRANSMEM        373..393\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:51.056852+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 82-84",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "77a0391d87d26f83f55657f76a4009b13d967514999d8b969ae7fda3d19b4120",
  "url": "https://rest.uniprot.org/unisave/Q4J8Q7?format=txt&versions=83"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4J8Q7?format=txt&versions=83)

```json
{
  "entry_version": 83,
  "evidence_id": "H6",
  "excerpt": "FT   TRANSMEM        416..436\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:51.056852+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 85-87",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "77a0391d87d26f83f55657f76a4009b13d967514999d8b969ae7fda3d19b4120",
  "url": "https://rest.uniprot.org/unisave/Q4J8Q7?format=txt&versions=83"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4J8Q7?format=txt&versions=83)

```json
{
  "entry_version": 83,
  "evidence_id": "H7",
  "excerpt": "FT   TRANSMEM        439..459\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:51.056852+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 88-90",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "77a0391d87d26f83f55657f76a4009b13d967514999d8b969ae7fda3d19b4120",
  "url": "https://rest.uniprot.org/unisave/Q4J8Q7?format=txt&versions=83"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 92. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
