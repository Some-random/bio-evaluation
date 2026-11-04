# transmembrane_0081

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0081.txt)

**Task:** `transmembrane`  
**Expected answer:** **B** — 53..71

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MNVPTAPTPNKHLNIPDLRFEKVFKKALHRELAPSSSLSRKAGVITKVVVRDVLLMPLLQSFVLSLALMGVKEWLSYIRLKGRTLGDRIRQRLFPI

[Multiple Choices]
A. 53..72
B. 53..71
C. 53..71; 395..420
D. 4..24; 81..101; 116..136; 158..178; 181..201; 228..248; 271..291; 309..329
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

> The sequence-matched UniProt annotation places a helical transmembrane region at 53..71. This is a computational annotation (ECO:0000255), not experimental evidence.

Citations as saved: [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Residues 53..71 form a strongly hydrophobic stretch, while residue 72 is lysine, a plausible charged boundary marker. This makes B a credible choice over the much longer alternatives and favors it over A, which includes the lysine.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence itself supports a membrane-spanning hydrophobic helix and gives a transferable basis for locating its likely boundary. The precise endpoint remains less certain than the existence of the helix.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> The options differ only by whether the boundary lysine at 72 is included. Given ordinary uncertainty in defining transmembrane-region endpoints, either interval could describe a segment that spans the membrane, although B is better supported as the hydrophobic core.


### Important caveats

- The supplied evidence supports a computationally annotated feature; it does not establish experimental validation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Residues 53..71 form a strongly hydrophobic stretch, while residue 72 is lysine, a plausible charged boundary marker. This makes B a credible choice over the much longer alternatives and favors it over A, which includes the lysine.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence itself supports a membrane-spanning hydrophobic helix and gives a transferable basis for locating its likely boundary. The precise endpoint remains less certain than the existence of the helix."
  },
  "case_id": "transmembrane_0081",
  "expected_answer_check": {
    "evidence_ids": [
      "H2"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation places a helical transmembrane region at 53..71. This is a computational annotation (ECO:0000255), not experimental evidence."
  },
  "important_caveats": [
    "The supplied evidence supports a computationally annotated feature; it does not establish experimental validation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "The options differ only by whether the boundary lysine at 72 is included. Given ordinary uncertainty in defining transmembrane-region endpoints, either interval could describe a segment that spans the membrane, although B is better supported as the hydrophobic core."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0081",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation places a helical transmembrane region at 53..71. This is a computational annotation (ECO:0000255), not experimental evidence.",
    "evidence_ids": ["H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Residues 53..71 form a strongly hydrophobic stretch, while residue 72 is lysine, a plausible charged boundary marker. This makes B a credible choice over the much longer alternatives and favors it over A, which includes the lysine.",
    "missing_item_specific_fact": "",
    "reason": "The sequence itself supports a membrane-spanning hydrophobic helix and gives a transferable basis for locating its likely boundary. The precise endpoint remains less certain than the existence of the helix."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "The options differ only by whether the boundary lysine at 72 is included. Given ordinary uncertainty in defining transmembrane-region endpoints, either interval could describe a segment that spans the membrane, although B is better supported as the hydrophobic core."
  },
  "important_caveats": [
    "The supplied evidence supports a computationally annotated feature; it does not establish experimental validation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (evidence C5, H2) records a single transmembrane helix at 53..71 with evidence code ECO:0000255 (inferred from similarity / ProRule computational annotation). The sequence at positions 53-71 (VLLMPLLQSFVLSLALMGV) is predominantly hydrophobic and 19 residues long, consistent with a single-pass TM helix. Position 72 is Lys (K), a charged residue that would be energetically unfavorable in the lipid bilayer core, supporting its exclusion. The annotation is computational rather than experimental, but the sequence itself independently supports the 53..71 boundary.

Citations as saved: [C5](#evidence-c5), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein is only 96 residues long, immediately eliminating options C (which references positions 395-420) and D (which lists eight TM segments spanning well beyond 96 residues). Between A (53..72) and B (53..71), the critical distinction is position 72: Lysine (K), a positively charged residue. A well-established principle in membrane protein biology is that charged residues (K, R, D, E) are excluded from the hydrophobic core of transmembrane helices because their burial in the lipid bilayer is energetically prohibitive. The hydrophobic stretch VLLMPLLQSFVLSLALMGV (positions 53-71) naturally terminates at V(71), and K(72) marks the transition to the cytosolic/extramembrane region. Standard TM helix prediction conventions (as in ProRule, TMHMM, Phobius) exclude such flanking charged residues from the helix definition. This is a transferable principle applicable to all single-pass TM proteins, not specific to this protein.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The distinction between A and B rests on the universally recognized rule that charged residues are excluded from TM helix cores, combined with reading the sequence to identify K at position 72. Options C and D are eliminated by the protein's total length (96 aa). No protein-specific annotation or memorization is needed.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While A and B differ by only one residue, the presence of a charged Lysine at position 72 provides a clear and standard biological rationale for excluding it from the TM helix. No other option is defensible: C and D reference positions beyond the 96-residue protein length.


### Important caveats

- The UniProt annotation uses evidence code ECO:0000255 (inferred from similarity / ProRule), meaning the TM assignment is computational rather than experimentally validated.
- The protein is annotated as 'Uncharacterized protein YFR035W-A' from S. cerevisiae; its function and membrane topology have not been experimentally confirmed.
- The distinction between 53..71 and 53..72 is a one-residue boundary judgment; some prediction tools might include or exclude the flanking K depending on their scoring thresholds, though the standard convention excludes it.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein is only 96 residues long, immediately eliminating options C (which references positions 395-420) and D (which lists eight TM segments spanning well beyond 96 residues). Between A (53..72) and B (53..71), the critical distinction is position 72: Lysine (K), a positively charged residue. A well-established principle in membrane protein biology is that charged residues (K, R, D, E) are excluded from the hydrophobic core of transmembrane helices because their burial in the lipid bilayer is energetically prohibitive. The hydrophobic stretch VLLMPLLQSFVLSLALMGV (positions 53-71) naturally terminates at V(71), and K(72) marks the transition to the cytosolic/extramembrane region. Standard TM helix prediction conventions (as in ProRule, TMHMM, Phobius) exclude such flanking charged residues from the helix definition. This is a transferable principle applicable to all single-pass TM proteins, not specific to this protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The distinction between A and B rests on the universally recognized rule that charged residues are excluded from TM helix cores, combined with reading the sequence to identify K at position 72. Options C and D are eliminated by the protein's total length (96 aa). No protein-specific annotation or memorization is needed."
  },
  "case_id": "transmembrane_0081",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C5, H2) records a single transmembrane helix at 53..71 with evidence code ECO:0000255 (inferred from similarity / ProRule computational annotation). The sequence at positions 53-71 (VLLMPLLQSFVLSLALMGV) is predominantly hydrophobic and 19 residues long, consistent with a single-pass TM helix. Position 72 is Lys (K), a charged residue that would be energetically unfavorable in the lipid bilayer core, supporting its exclusion. The annotation is computational rather than experimental, but the sequence itself independently supports the 53..71 boundary."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (inferred from similarity / ProRule), meaning the TM assignment is computational rather than experimentally validated.",
    "The protein is annotated as 'Uncharacterized protein YFR035W-A' from S. cerevisiae; its function and membrane topology have not been experimentally confirmed.",
    "The distinction between 53..71 and 53..72 is a one-residue boundary judgment; some prediction tools might include or exclude the flanking K depending on their scoring thresholds, though the standard convention excludes it."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While A and B differ by only one residue, the presence of a charged Lysine at position 72 provides a clear and standard biological rationale for excluding it from the TM helix. No other option is defensible: C and D reference positions beyond the 96-residue protein length."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0081",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C5, H2) records a single transmembrane helix at 53..71 with evidence code ECO:0000255 (inferred from similarity / ProRule computational annotation). The sequence at positions 53-71 (VLLMPLLQSFVLSLALMGV) is predominantly hydrophobic and 19 residues long, consistent with a single-pass TM helix. Position 72 is Lys (K), a charged residue that would be energetically unfavorable in the lipid bilayer core, supporting its exclusion. The annotation is computational rather than experimental, but the sequence itself independently supports the 53..71 boundary.",
    "evidence_ids": ["C5", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein is only 96 residues long, immediately eliminating options C (which references positions 395-420) and D (which lists eight TM segments spanning well beyond 96 residues). Between A (53..72) and B (53..71), the critical distinction is position 72: Lysine (K), a positively charged residue. A well-established principle in membrane protein biology is that charged residues (K, R, D, E) are excluded from the hydrophobic core of transmembrane helices because their burial in the lipid bilayer is energetically prohibitive. The hydrophobic stretch VLLMPLLQSFVLSLALMGV (positions 53-71) naturally terminates at V(71), and K(72) marks the transition to the cytosolic/extramembrane region. Standard TM helix prediction conventions (as in ProRule, TMHMM, Phobius) exclude such flanking charged residues from the helix definition. This is a transferable principle applicable to all single-pass TM proteins, not specific to this protein.",
    "missing_item_specific_fact": "",
    "reason": "The distinction between A and B rests on the universally recognized rule that charged residues are excluded from TM helix cores, combined with reading the sequence to identify K at position 72. Options C and D are eliminated by the protein's total length (96 aa). No protein-specific annotation or memorization is needed."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While A and B differ by only one residue, the presence of a charged Lysine at position 72 provides a clear and standard biological rationale for excluding it from the TM helix. No other option is defensible: C and D reference positions beyond the 96-residue protein length."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (inferred from similarity / ProRule), meaning the TM assignment is computational rather than experimentally validated.",
    "The protein is annotated as 'Uncharacterized protein YFR035W-A' from S. cerevisiae; its function and membrane topology have not been experimentally confirmed.",
    "The distinction between 53..71 and 53..72 is a one-residue boundary judgment; some prediction tools might include or exclude the flanking K depending on their scoring thresholds, though the standard convention excludes it."
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
  "benchmark_sequence_length": 96,
  "benchmark_sequence_sha256": "af9deaca53f1b7ad13d02bb00fcd3d88f84d31a2a38d6646a9176bba432113f6",
  "current_entry_audit": {
    "entryVersion": 5,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2025-02-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "334d652c31aa94671f71985d47556af600c64ebfe50ff82f67cec6a6220cb69c",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 96,
  "current_source_sequence_sha256": "af9deaca53f1b7ad13d02bb00fcd3d88f84d31a2a38d6646a9176bba432113f6",
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
  "requested_accession": "P9WEJ4",
  "selected_historical_entry_version": 4,
  "selected_historical_record_sha256": "620602a41d8671c8701df46a7d19236b30cfbea35740e43343f9e3862130e866",
  "selected_historical_source_sequence_length": 96,
  "selected_historical_source_sequence_sha256": "af9deaca53f1b7ad13d02bb00fcd3d88f84d31a2a38d6646a9176bba432113f6",
  "selected_historical_version": {
    "accession": "P9WEJ4",
    "database": "Swiss-Prot",
    "entryVersion": 4,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "YF035_YEAST",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEJ4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P9WEJ4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:30:19.580713+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "334d652c31aa94671f71985d47556af600c64ebfe50ff82f67cec6a6220cb69c",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEJ4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEJ4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":5,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2025-02-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:30:19.580713+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "334d652c31aa94671f71985d47556af600c64ebfe50ff82f67cec6a6220cb69c",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEJ4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEJ4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Baker's yeast\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Saccharomycotina\",\"Saccharomycetes\",\"Saccharomycetales\",\"Saccharomycetaceae\",\"Saccharomyces\"],\"scientificName\":\"Saccharomyces cerevisiae (strain ATCC 204508 / S288c)\",\"taxonId\":559292}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:30:19.580713+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "334d652c31aa94671f71985d47556af600c64ebfe50ff82f67cec6a6220cb69c",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEJ4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEJ4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Uncharacterized protein YFR035W-A\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:30:19.580713+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "334d652c31aa94671f71985d47556af600c64ebfe50ff82f67cec6a6220cb69c",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEJ4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEJ4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":71},\"start\":{\"modifier\":\"EXACT\",\"value\":53}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:30:19.580713+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "334d652c31aa94671f71985d47556af600c64ebfe50ff82f67cec6a6220cb69c",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEJ4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEJ4?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H1",
  "excerpt": "ID   YF035_YEAST             Reviewed;          96 AA.\nAC   P9WEJ4; A0AAT9JB48;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-FEB-2025, sequence version 1.\nDT   28-JAN-2026, entry version 4.\nDE   RecName: Full=Uncharacterized protein YFR035W-A {ECO:0000305};\nGN   OrderedLocusNames=YFR035W-A {ECO:0000312|SGD:S000350095};\nOS   Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Saccharomycotina; Saccharomycetes;\nOC   Saccharomycetales; Saccharomycetaceae; Saccharomyces.\nOX   NCBI_TaxID=559292;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:21.235682+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-11",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "620602a41d8671c8701df46a7d19236b30cfbea35740e43343f9e3862130e866",
  "url": "https://rest.uniprot.org/unisave/P9WEJ4?format=txt&versions=4"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEJ4?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H2",
  "excerpt": "FT   TRANSMEM        53..71\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:21.235682+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 71-73",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "620602a41d8671c8701df46a7d19236b30cfbea35740e43343f9e3862130e866",
  "url": "https://rest.uniprot.org/unisave/P9WEJ4?format=txt&versions=4"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 81. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
