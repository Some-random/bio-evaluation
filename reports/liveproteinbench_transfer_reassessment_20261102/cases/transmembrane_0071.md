# transmembrane_0071

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0071.txt)

**Task:** `transmembrane`  
**Expected answer:** **A** — 38..58; 73..93; 124..144; 156..176; 182..202; 244..264

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTTLDLTARSDRGRVYWLLADCWNIVRRGLTHYQRQPVNIAWQLGFPILSVLLYGYVFGSAMKVPGGGDYKDFLMPGMFVMTMAFGFINTATLVVYDSTKGVIDRFRSMPMASSAVVAGRGVTDLITACAELAIMMLTAFAMGWRPDGGLGFLGAFGLLLWLRFALIWIGVWLGLLVPNPEAAGGLFAVAFPLTMISSIMVAPQLMPDWLGWVAMWNPISSTAAATRELFGTPVGGDTWVEQHALLMAGVWPVILTLVFLPLAVRRFKKLSR

[Multiple Choices]
A. 38..58; 73..93; 124..144; 156..176; 182..202; 244..264
B. 38..58; 73..93; 123..147; 156..176; 182..202; 244..264
C. 35..55
D. 38..58; 73..93; 124..144; 156..176; 244..264
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

> The sequence-matched historical UniProt record lists all six transmembrane regions in choice A. These are computational annotations (ECO:0000255), not evidence of experimental determination.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has multiple strongly hydrophobic stretches consistent with a multipass membrane protein, supporting the overall set of six regions in A or B. But transferable hydropathy and membrane-protein knowledge do not meaningfully distinguish the nearly identical proposed boundaries for one region.


**Missing item-specific fact**

> The exact annotated boundary convention or predicted coordinates for the region listed as 124..144 in A versus 123..147 in B.


**Reason**

> General biological reasoning supports the broad transmembrane topology, but choosing between A and B as exact coordinate lists requires the specific boundary annotation or prediction that is not supplied in the original input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> A and B identify the same set of hydrophobic membrane-spanning regions, with only a small boundary difference for one segment. Both are defensible as transmembrane-region predictions from the sequence.


### Important caveats

- The source annotations are computational rather than experimentally established.
- Transmembrane-region boundaries can be prediction- or annotation-dependent, and nearby endpoints may both describe the same membrane-spanning helix.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has multiple strongly hydrophobic stretches consistent with a multipass membrane protein, supporting the overall set of six regions in A or B. But transferable hydropathy and membrane-protein knowledge do not meaningfully distinguish the nearly identical proposed boundaries for one region.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact annotated boundary convention or predicted coordinates for the region listed as 124..144 in A versus 123..147 in B.",
    "reason": "General biological reasoning supports the broad transmembrane topology, but choosing between A and B as exact coordinate lists requires the specific boundary annotation or prediction that is not supplied in the original input."
  },
  "case_id": "transmembrane_0071",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record lists all six transmembrane regions in choice A. These are computational annotations (ECO:0000255), not evidence of experimental determination."
  },
  "important_caveats": [
    "The source annotations are computational rather than experimentally established.",
    "Transmembrane-region boundaries can be prediction- or annotation-dependent, and nearby endpoints may both describe the same membrane-spanning helix."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "A and B identify the same set of hydrophobic membrane-spanning regions, with only a small boundary difference for one segment. Both are defensible as transmembrane-region predictions from the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0071",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record lists all six transmembrane regions in choice A. These are computational annotations (ECO:0000255), not evidence of experimental determination.",
    "evidence_ids": ["H3", "H4", "H5", "H6", "H7", "H8"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has multiple strongly hydrophobic stretches consistent with a multipass membrane protein, supporting the overall set of six regions in A or B. But transferable hydropathy and membrane-protein knowledge do not meaningfully distinguish the nearly identical proposed boundaries for one region.",
    "missing_item_specific_fact": "The exact annotated boundary convention or predicted coordinates for the region listed as 124..144 in A versus 123..147 in B.",
    "reason": "General biological reasoning supports the broad transmembrane topology, but choosing between A and B as exact coordinate lists requires the specific boundary annotation or prediction that is not supplied in the original input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "A and B identify the same set of hydrophobic membrane-spanning regions, with only a small boundary difference for one segment. Both are defensible as transmembrane-region predictions from the sequence."
  },
  "important_caveats": [
    "The source annotations are computational rather than experimentally established.",
    "Transmembrane-region boundaries can be prediction- or annotation-dependent, and nearby endpoints may both describe the same membrane-spanning helix."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DXU6 (DRRB2_STRC4, Daunorubicin resistance ABC transporter permease protein DrrB2, 272 AA) annotates exactly six transmembrane helical segments at 38..58, 73..93, 124..144, 156..176, 182..202, and 244..264, matching choice A precisely. All annotations carry evidence code ECO:0000255 (inferred by similarity), so they represent computational/transfer-based predictions rather than direct experimental measurement. The sequence in the benchmark matches the UniProt record (SHA-256 identical, 272 AA).

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Two layers of transferable knowledge narrow the choices. (1) Family-level topology: the sequence length (~272 AA), the overall hydrophobic pattern, and the domain architecture are consistent with an ABC transporter permease (transmembrane domain), which canonically contains six TM helices arranged in two pseudo-symmetric three-helix bundles. This eliminates C (single TM) and D (five TM segments, missing 182..202). (2) Hydrophobicity boundary analysis to distinguish A from B: the third TM region in B is 123..147, which extends the helix to include residues R(145), P(146), D(147) at the C-terminal end. Arginine (charged), proline (helix-breaking), and aspartate (charged) are strongly incompatible with a lipid-embedded alpha-helix; standard TM prediction rules (e.g., GRAVY, Kyte-Doolittle windows) would exclude these positions from a TM segment. Choice A's boundary of 124..144 ends at Trp(144), a residue commonly found at the membrane-water interface, which is biologically consistent. Starting at position 124 (Asp) vs 123 (Thr) is marginal, but the C-terminal extension in B is the decisive discriminator. A model performing a straightforward hydrophobicity scan would flag the R-P-D triplet as non-TM and select A over B.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The ABC-permease six-helix topology is a well-established family feature transferable across hundreds of characterized ABC transporters. The hydrophobicity incompatibility of Arg/Pro/Asp with a TM helix is a universal biophysical principle. Together these distinguish A from B, C, and D without requiring the specific UniProt annotation for P0DXU6.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choice C (1 TM) and D (5 TM) are eliminated by the canonical six-helix ABC permease topology. Choice B is eliminated because its third TM segment (123..147) includes R, P, D residues that violate basic TM helix compatibility. Only choice A remains as a defensible answer. The boundary differences between A and B (124 vs 123, 144 vs 147) are small, but the inclusion of three clearly non-TM residues in B provides a clear discriminator.


### Important caveats

- All UniProt TM annotations for this entry carry evidence code ECO:0000255 (inferred by similarity), meaning the boundaries are computational predictions transferred from homologous proteins, not experimentally determined positions.
- The exact residue-level boundaries (e.g., 124 vs 123) are within the typical uncertainty of TM prediction tools; the question tests qualitative hydrophobicity reasoning rather than sub-residue precision.
- The identity of the protein (ABC permease, Streptomyces coeruleorubidus) was not given to the model; family recognition must be inferred from sequence features and length.
- The reviewer-only UniProt accession and organism information were not part of the model's original input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Two layers of transferable knowledge narrow the choices. (1) Family-level topology: the sequence length (~272 AA), the overall hydrophobic pattern, and the domain architecture are consistent with an ABC transporter permease (transmembrane domain), which canonically contains six TM helices arranged in two pseudo-symmetric three-helix bundles. This eliminates C (single TM) and D (five TM segments, missing 182..202). (2) Hydrophobicity boundary analysis to distinguish A from B: the third TM region in B is 123..147, which extends the helix to include residues R(145), P(146), D(147) at the C-terminal end. Arginine (charged), proline (helix-breaking), and aspartate (charged) are strongly incompatible with a lipid-embedded alpha-helix; standard TM prediction rules (e.g., GRAVY, Kyte-Doolittle windows) would exclude these positions from a TM segment. Choice A's boundary of 124..144 ends at Trp(144), a residue commonly found at the membrane-water interface, which is biologically consistent. Starting at position 124 (Asp) vs 123 (Thr) is marginal, but the C-terminal extension in B is the decisive discriminator. A model performing a straightforward hydrophobicity scan would flag the R-P-D triplet as non-TM and select A over B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The ABC-permease six-helix topology is a well-established family feature transferable across hundreds of characterized ABC transporters. The hydrophobicity incompatibility of Arg/Pro/Asp with a TM helix is a universal biophysical principle. Together these distinguish A from B, C, and D without requiring the specific UniProt annotation for P0DXU6."
  },
  "case_id": "transmembrane_0071",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "C10",
      "H3",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DXU6 (DRRB2_STRC4, Daunorubicin resistance ABC transporter permease protein DrrB2, 272 AA) annotates exactly six transmembrane helical segments at 38..58, 73..93, 124..144, 156..176, 182..202, and 244..264, matching choice A precisely. All annotations carry evidence code ECO:0000255 (inferred by similarity), so they represent computational/transfer-based predictions rather than direct experimental measurement. The sequence in the benchmark matches the UniProt record (SHA-256 identical, 272 AA)."
  },
  "important_caveats": [
    "All UniProt TM annotations for this entry carry evidence code ECO:0000255 (inferred by similarity), meaning the boundaries are computational predictions transferred from homologous proteins, not experimentally determined positions.",
    "The exact residue-level boundaries (e.g., 124 vs 123) are within the typical uncertainty of TM prediction tools; the question tests qualitative hydrophobicity reasoning rather than sub-residue precision.",
    "The identity of the protein (ABC permease, Streptomyces coeruleorubidus) was not given to the model; family recognition must be inferred from sequence features and length.",
    "The reviewer-only UniProt accession and organism information were not part of the model's original input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice C (1 TM) and D (5 TM) are eliminated by the canonical six-helix ABC permease topology. Choice B is eliminated because its third TM segment (123..147) includes R, P, D residues that violate basic TM helix compatibility. Only choice A remains as a defensible answer. The boundary differences between A and B (124 vs 123, 144 vs 147) are small, but the inclusion of three clearly non-TM residues in B provides a clear discriminator."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0071",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DXU6 (DRRB2_STRC4, Daunorubicin resistance ABC transporter permease protein DrrB2, 272 AA) annotates exactly six transmembrane helical segments at 38..58, 73..93, 124..144, 156..176, 182..202, and 244..264, matching choice A precisely. All annotations carry evidence code ECO:0000255 (inferred by similarity), so they represent computational/transfer-based predictions rather than direct experimental measurement. The sequence in the benchmark matches the UniProt record (SHA-256 identical, 272 AA).",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "H3", "H4", "H5", "H6", "H7", "H8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Two layers of transferable knowledge narrow the choices. (1) Family-level topology: the sequence length (~272 AA), the overall hydrophobic pattern, and the domain architecture are consistent with an ABC transporter permease (transmembrane domain), which canonically contains six TM helices arranged in two pseudo-symmetric three-helix bundles. This eliminates C (single TM) and D (five TM segments, missing 182..202). (2) Hydrophobicity boundary analysis to distinguish A from B: the third TM region in B is 123..147, which extends the helix to include residues R(145), P(146), D(147) at the C-terminal end. Arginine (charged), proline (helix-breaking), and aspartate (charged) are strongly incompatible with a lipid-embedded alpha-helix; standard TM prediction rules (e.g., GRAVY, Kyte-Doolittle windows) would exclude these positions from a TM segment. Choice A's boundary of 124..144 ends at Trp(144), a residue commonly found at the membrane-water interface, which is biologically consistent. Starting at position 124 (Asp) vs 123 (Thr) is marginal, but the C-terminal extension in B is the decisive discriminator. A model performing a straightforward hydrophobicity scan would flag the R-P-D triplet as non-TM and select A over B.",
    "missing_item_specific_fact": "",
    "reason": "The ABC-permease six-helix topology is a well-established family feature transferable across hundreds of characterized ABC transporters. The hydrophobicity incompatibility of Arg/Pro/Asp with a TM helix is a universal biophysical principle. Together these distinguish A from B, C, and D without requiring the specific UniProt annotation for P0DXU6."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice C (1 TM) and D (5 TM) are eliminated by the canonical six-helix ABC permease topology. Choice B is eliminated because its third TM segment (123..147) includes R, P, D residues that violate basic TM helix compatibility. Only choice A remains as a defensible answer. The boundary differences between A and B (124 vs 123, 144 vs 147) are small, but the inclusion of three clearly non-TM residues in B provides a clear discriminator."
  },
  "important_caveats": [
    "All UniProt TM annotations for this entry carry evidence code ECO:0000255 (inferred by similarity), meaning the boundaries are computational predictions transferred from homologous proteins, not experimentally determined positions.",
    "The exact residue-level boundaries (e.g., 124 vs 123) are within the typical uncertainty of TM prediction tools; the question tests qualitative hydrophobicity reasoning rather than sub-residue precision.",
    "The identity of the protein (ABC permease, Streptomyces coeruleorubidus) was not given to the model; family recognition must be inferred from sequence features and length.",
    "The reviewer-only UniProt accession and organism information were not part of the model's original input."
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
  "benchmark_sequence_length": 272,
  "benchmark_sequence_sha256": "59e638eb8cf60b05352d61e55cf16844ce8b914c1394940c66e4190daaf561d9",
  "current_entry_audit": {
    "entryVersion": 6,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-02-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "4e7d0b296d64a4ffb645956bc9763e367bd0533eedf73ba35b4dc16bd7421217",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 272,
  "current_source_sequence_sha256": "59e638eb8cf60b05352d61e55cf16844ce8b914c1394940c66e4190daaf561d9",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 4,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "P0DXU6",
  "selected_historical_entry_version": 4,
  "selected_historical_record_sha256": "372a99e71818628749a5230f6a3ea50eb4a3ab3f801909ad5a5e951310594fb7",
  "selected_historical_source_sequence_length": 272,
  "selected_historical_source_sequence_sha256": "59e638eb8cf60b05352d61e55cf16844ce8b914c1394940c66e4190daaf561d9",
  "selected_historical_version": {
    "accession": "P0DXU6",
    "database": "Swiss-Prot",
    "entryVersion": 4,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DRRB2_STRC4",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU6.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DXU6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:29:39.151534+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4e7d0b296d64a4ffb645956bc9763e367bd0533eedf73ba35b4dc16bd7421217",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU6.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU6.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":6,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-02-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:29:39.151534+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4e7d0b296d64a4ffb645956bc9763e367bd0533eedf73ba35b4dc16bd7421217",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU6.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU6.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Bacillati\",\"Actinomycetota\",\"Actinomycetes\",\"Kitasatosporales\",\"Streptomycetaceae\",\"Streptomyces\"],\"scientificName\":\"Streptomyces coeruleorubidus\",\"taxonId\":116188}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:29:39.151534+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4e7d0b296d64a4ffb645956bc9763e367bd0533eedf73ba35b4dc16bd7421217",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU6.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU6.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Daunorubicin resistance ABC transporter permease protein DrrB2\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:29:39.151534+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4e7d0b296d64a4ffb645956bc9763e367bd0533eedf73ba35b4dc16bd7421217",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU6.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU6.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":58},\"start\":{\"modifier\":\"EXACT\",\"value\":38}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:29:39.151534+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4e7d0b296d64a4ffb645956bc9763e367bd0533eedf73ba35b4dc16bd7421217",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU6.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU6.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":93},\"start\":{\"modifier\":\"EXACT\",\"value\":73}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:29:39.151534+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4e7d0b296d64a4ffb645956bc9763e367bd0533eedf73ba35b4dc16bd7421217",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU6.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU6.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":144},\"start\":{\"modifier\":\"EXACT\",\"value\":124}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:29:39.151534+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4e7d0b296d64a4ffb645956bc9763e367bd0533eedf73ba35b4dc16bd7421217",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU6.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU6.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":176},\"start\":{\"modifier\":\"EXACT\",\"value\":156}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:29:39.151534+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4e7d0b296d64a4ffb645956bc9763e367bd0533eedf73ba35b4dc16bd7421217",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU6.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU6.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":202},\"start\":{\"modifier\":\"EXACT\",\"value\":182}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:29:39.151534+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4e7d0b296d64a4ffb645956bc9763e367bd0533eedf73ba35b4dc16bd7421217",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU6.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU6.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":264},\"start\":{\"modifier\":\"EXACT\",\"value\":244}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:29:39.151534+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4e7d0b296d64a4ffb645956bc9763e367bd0533eedf73ba35b4dc16bd7421217",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU6.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU6?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H1",
  "excerpt": "ID   DRRB2_STRC4             Reviewed;         272 AA.\nAC   P0DXU6;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-FEB-2025, sequence version 1.\nDT   28-JAN-2026, entry version 4.\nDE   RecName: Full=Daunorubicin resistance ABC transporter permease protein DrrB2 {ECO:0000305};\nGN   Name=drrB2 {ECO:0000303|PubMed:39375957};\nGN   ORFNames=R5U08_15990 {ECO:0000312|EMBL:WOT35540.1};\nOS   Streptomyces coeruleorubidus.\nOC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Kitasatosporales;\nOC   Streptomycetaceae; Streptomyces.\nOX   NCBI_TaxID=116188;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:40.921406+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "372a99e71818628749a5230f6a3ea50eb4a3ab3f801909ad5a5e951310594fb7",
  "url": "https://rest.uniprot.org/unisave/P0DXU6?format=txt&versions=4"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU6?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION IN DAUNORUBICIN EFFLUX, INDUCTION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=39375957; DOI=10.1111/1751-7915.70023;\nRA   Dong J., Ning J., Tian Y., Li H., Chen H., Guan W.;\nRT   \"The involvement of multiple ABC transporters in daunorubicin efflux in\nRT   Streptomyces coeruleorubidus.\";\nRL   Microb. Biotechnol. 17:e70023-e70023(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:40.921406+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 18-24",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "372a99e71818628749a5230f6a3ea50eb4a3ab3f801909ad5a5e951310594fb7",
  "url": "https://rest.uniprot.org/unisave/P0DXU6?format=txt&versions=4"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU6?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H3",
  "excerpt": "FT   TRANSMEM        38..58\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:40.921406+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 73-75",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "372a99e71818628749a5230f6a3ea50eb4a3ab3f801909ad5a5e951310594fb7",
  "url": "https://rest.uniprot.org/unisave/P0DXU6?format=txt&versions=4"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU6?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H4",
  "excerpt": "FT   TRANSMEM        73..93\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:40.921406+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 76-78",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "372a99e71818628749a5230f6a3ea50eb4a3ab3f801909ad5a5e951310594fb7",
  "url": "https://rest.uniprot.org/unisave/P0DXU6?format=txt&versions=4"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU6?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H5",
  "excerpt": "FT   TRANSMEM        124..144\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:40.921406+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 79-81",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "372a99e71818628749a5230f6a3ea50eb4a3ab3f801909ad5a5e951310594fb7",
  "url": "https://rest.uniprot.org/unisave/P0DXU6?format=txt&versions=4"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU6?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H6",
  "excerpt": "FT   TRANSMEM        156..176\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:40.921406+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 82-84",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "372a99e71818628749a5230f6a3ea50eb4a3ab3f801909ad5a5e951310594fb7",
  "url": "https://rest.uniprot.org/unisave/P0DXU6?format=txt&versions=4"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU6?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H7",
  "excerpt": "FT   TRANSMEM        182..202\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:40.921406+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 85-87",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "372a99e71818628749a5230f6a3ea50eb4a3ab3f801909ad5a5e951310594fb7",
  "url": "https://rest.uniprot.org/unisave/P0DXU6?format=txt&versions=4"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU6?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H8",
  "excerpt": "FT   TRANSMEM        244..264\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:40.921406+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 88-90",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "372a99e71818628749a5230f6a3ea50eb4a3ab3f801909ad5a5e951310594fb7",
  "url": "https://rest.uniprot.org/unisave/P0DXU6?format=txt&versions=4"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 71. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
