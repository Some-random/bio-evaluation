# transmembrane_0035

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0035.txt)

**Task:** `transmembrane`  
**Expected answer:** **A** — 4..24

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MATPQFSCLLPAFFLLVVFLFLLIKELRRYKSPKTTQKLPPGPPMLPIIGNLHQMASSLPHQNLKKLADKYGPLMHLKLGEISAVAVSSPRLAKEVLQTRGLAFADRPQSVVAKLMLHNCLGVTFSRYGDYWRQLRQIFAMELLSSKSVQSFSTIMEDELFAMVKSIESEAGRPIILADKLISYLYATLSRATLGRVCKGKETLIEVTGETLALSGAQSLEDIFPSVKIFAYLNPLRPKVRKLFNRIDGVLEDIINQQEKKLLSARVDNDQLQPEENDMLSVLLKLRNGKDSKVQVTNNDIKAIIFELFLAGTVGSSTTVEWAMSEMMKNPKVMEKAQHEVREVLKGKKRICQSDIQKLSYLKLVVKETLRLHPPAPLLFPRECRGQCEVDGYTIPAKAMVMVNCWALGRDPEHWIEADKFEPERFKNSSIDFIGNHFEYIPFGAGRRICPGISFGATNVELLLAALLYHFDWELAGGMHPKDLDMLELFGPGCTRKNPLSVIPSICIPSHDDN

[Multiple Choices]
A. 4..24
B. 6..24
C. 4..24; 232..250
D. 14..34; 78..98; 114..134; 137..157; 162..182; 193..213; 235..255; 328..348; 380..400; 471..491
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

> The exact matched sequence has a UniProt transmembrane annotation at 4..24, matching choice A. Its evidence code is computational (ECO:0000255), so this supports the expected answer as an annotation, not as direct experimental confirmation.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a conspicuous hydrophobic stretch near its N-terminus, followed by a much less hydrophobic, enzyme-like region. General knowledge that membrane-anchored proteins commonly use an N-terminal hydrophobic helix makes the 4..24 / 6..24 region a credible membrane-spanning segment; it also argues against choice C's additional internal segment and choice D's many proposed spans.


**Missing item-specific fact**

> The precise predicted start boundary needed to choose uniquely between 4..24 and 6..24 is not established by the sequence pattern alone.


**Reason**

> Transferable sequence knowledge meaningfully identifies the N-terminal membrane-spanning region among the alternatives. It does not resolve the two nearly overlapping boundary variants.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Both intervals cover the same N-terminal hydrophobic stretch, and the wording asks for a segment that crosses the membrane rather than for a specific prediction convention or exact boundary. The input does not clearly rule out 6..24 as a spanning segment.


### Important caveats

- The supporting database feature is computationally inferred, not experimental evidence.
- The exact residue boundaries remain less certain from sequence inspection than the presence of the N-terminal hydrophobic segment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a conspicuous hydrophobic stretch near its N-terminus, followed by a much less hydrophobic, enzyme-like region. General knowledge that membrane-anchored proteins commonly use an N-terminal hydrophobic helix makes the 4..24 / 6..24 region a credible membrane-spanning segment; it also argues against choice C's additional internal segment and choice D's many proposed spans.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The precise predicted start boundary needed to choose uniquely between 4..24 and 6..24 is not established by the sequence pattern alone.",
    "reason": "Transferable sequence knowledge meaningfully identifies the N-terminal membrane-spanning region among the alternatives. It does not resolve the two nearly overlapping boundary variants."
  },
  "case_id": "transmembrane_0035",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact matched sequence has a UniProt transmembrane annotation at 4..24, matching choice A. Its evidence code is computational (ECO:0000255), so this supports the expected answer as an annotation, not as direct experimental confirmation."
  },
  "important_caveats": [
    "The supporting database feature is computationally inferred, not experimental evidence.",
    "The exact residue boundaries remain less certain from sequence inspection than the presence of the N-terminal hydrophobic segment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Both intervals cover the same N-terminal hydrophobic stretch, and the wording asks for a segment that crosses the membrane rather than for a specific prediction convention or exact boundary. The input does not clearly rule out 6..24 as a spanning segment."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0035",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact matched sequence has a UniProt transmembrane annotation at 4..24, matching choice A. Its evidence code is computational (ECO:0000255), so this supports the expected answer as an annotation, not as direct experimental confirmation.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a conspicuous hydrophobic stretch near its N-terminus, followed by a much less hydrophobic, enzyme-like region. General knowledge that membrane-anchored proteins commonly use an N-terminal hydrophobic helix makes the 4..24 / 6..24 region a credible membrane-spanning segment; it also argues against choice C's additional internal segment and choice D's many proposed spans.",
    "missing_item_specific_fact": "The precise predicted start boundary needed to choose uniquely between 4..24 and 6..24 is not established by the sequence pattern alone.",
    "reason": "Transferable sequence knowledge meaningfully identifies the N-terminal membrane-spanning region among the alternatives. It does not resolve the two nearly overlapping boundary variants."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Both intervals cover the same N-terminal hydrophobic stretch, and the wording asks for a segment that crosses the membrane rather than for a specific prediction convention or exact boundary. The input does not clearly rule out 6..24 as a spanning segment."
  },
  "important_caveats": [
    "The supporting database feature is computationally inferred, not experimental evidence.",
    "The exact residue boundaries remain less certain from sequence inspection than the presence of the N-terminal hydrophobic segment."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (evidence code ECO:0000255, pro-rule-based computational prediction) explicitly annotates a single transmembrane helical region at positions 4..24, matching choice A exactly. The annotation is computational (prorule) rather than experimental, but it is the recorded annotation for this sequence. The N-terminal hydrophobic stretch (LLPAFFLLVVFLFLLI, ~positions 9-22) is consistent with a single-pass membrane anchor typical of plant microsomal cytochrome P450 enzymes.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable cytochrome P450 heme-binding motif (FGAGRRICPGIS near position 400) and the overall architecture of a soluble catalytic domain preceded by a short N-terminal hydrophobic stretch (LLPAFFLLVVFLFLLI). Knowledge from the P450 superfamily (learned from many characterized P450s) establishes that microsomal P450s, including plant P450s, possess a single N-terminal transmembrane anchor helix and a soluble catalytic domain. This family-level inference strongly disfavors option D (ten TM regions, characteristic of multi-pass channels/GPCRs) and option C (two TM regions, inconsistent with P450 topology). The N-terminal hydrophobic segment is clearly visible in the raw sequence, and its length (~21 residues from position 4 to 24) is appropriate for a single-pass TM helix. The distinction between A (4..24) and B (6..24) is a minor boundary question (2 residues: P-Q at positions 4-5); Pro at position 4 is moderately hydrophobic and TM predictions commonly include a few edge residues before the strongly hydrophobic core, making A defensible.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level knowledge of cytochrome P450 topology (single N-terminal TM anchor + soluble catalytic domain) meaningfully eliminates options C and D. The visible N-terminal hydrophobic stretch supports a single TM region. The A-vs-B boundary distinction is within the typical ±2-3 residue uncertainty of TM prediction, but including the moderately hydrophobic Pro at position 4 is consistent with standard TM helix boundary conventions, making A the more defensible choice among the offered alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> The difference between A (4..24) and B (6..24) is only two residues at the N-terminal edge (P-Q). Both describe a single N-terminal transmembrane helix of appropriate length for a P450 anchor. Hydrophobicity analysis of the raw sequence could reasonably place the TM boundary at either position, as P (hydropathy -1.6) and Q (-3.5) are at the interface between the signal-anchor region and the cytoplasmic/luminal flanking sequence. The annotation (prorule) chose 4, but a model relying on hydrophobicity alone might select 6 where the strongly hydrophobic F begins.


### Important caveats

- The transmembrane annotation carries evidence code ECO:0000255 (prorule-based computational prediction), not experimental data. No experimental validation of the TM topology is cited.
- The protein identity (Alstonine synthase / Cytochrome P450 AS from Alstonia scholaris) was not provided to the evaluated model; the P450 family recognition must come from sequence motifs in the provided sequence.
- The A-vs-B boundary distinction (positions 4 vs 6) is within the typical uncertainty of TM prediction algorithms and represents a genuine ambiguity in the multiple-choice design.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable cytochrome P450 heme-binding motif (FGAGRRICPGIS near position 400) and the overall architecture of a soluble catalytic domain preceded by a short N-terminal hydrophobic stretch (LLPAFFLLVVFLFLLI). Knowledge from the P450 superfamily (learned from many characterized P450s) establishes that microsomal P450s, including plant P450s, possess a single N-terminal transmembrane anchor helix and a soluble catalytic domain. This family-level inference strongly disfavors option D (ten TM regions, characteristic of multi-pass channels/GPCRs) and option C (two TM regions, inconsistent with P450 topology). The N-terminal hydrophobic segment is clearly visible in the raw sequence, and its length (~21 residues from position 4 to 24) is appropriate for a single-pass TM helix. The distinction between A (4..24) and B (6..24) is a minor boundary question (2 residues: P-Q at positions 4-5); Pro at position 4 is moderately hydrophobic and TM predictions commonly include a few edge residues before the strongly hydrophobic core, making A defensible.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level knowledge of cytochrome P450 topology (single N-terminal TM anchor + soluble catalytic domain) meaningfully eliminates options C and D. The visible N-terminal hydrophobic stretch supports a single TM region. The A-vs-B boundary distinction is within the typical ±2-3 residue uncertainty of TM prediction, but including the moderately hydrophobic Pro at position 4 is consistent with standard TM helix boundary conventions, making A the more defensible choice among the offered alternatives."
  },
  "case_id": "transmembrane_0035",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence code ECO:0000255, pro-rule-based computational prediction) explicitly annotates a single transmembrane helical region at positions 4..24, matching choice A exactly. The annotation is computational (prorule) rather than experimental, but it is the recorded annotation for this sequence. The N-terminal hydrophobic stretch (LLPAFFLLVVFLFLLI, ~positions 9-22) is consistent with a single-pass membrane anchor typical of plant microsomal cytochrome P450 enzymes."
  },
  "important_caveats": [
    "The transmembrane annotation carries evidence code ECO:0000255 (prorule-based computational prediction), not experimental data. No experimental validation of the TM topology is cited.",
    "The protein identity (Alstonine synthase / Cytochrome P450 AS from Alstonia scholaris) was not provided to the evaluated model; the P450 family recognition must come from sequence motifs in the provided sequence.",
    "The A-vs-B boundary distinction (positions 4 vs 6) is within the typical uncertainty of TM prediction algorithms and represents a genuine ambiguity in the multiple-choice design."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "The difference between A (4..24) and B (6..24) is only two residues at the N-terminal edge (P-Q). Both describe a single N-terminal transmembrane helix of appropriate length for a P450 anchor. Hydrophobicity analysis of the raw sequence could reasonably place the TM boundary at either position, as P (hydropathy -1.6) and Q (-3.5) are at the interface between the signal-anchor region and the cytoplasmic/luminal flanking sequence. The annotation (prorule) chose 4, but a model relying on hydrophobicity alone might select 6 where the strongly hydrophobic F begins."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0035",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence code ECO:0000255, pro-rule-based computational prediction) explicitly annotates a single transmembrane helical region at positions 4..24, matching choice A exactly. The annotation is computational (prorule) rather than experimental, but it is the recorded annotation for this sequence. The N-terminal hydrophobic stretch (LLPAFFLLVVFLFLLI, ~positions 9-22) is consistent with a single-pass membrane anchor typical of plant microsomal cytochrome P450 enzymes.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable cytochrome P450 heme-binding motif (FGAGRRICPGIS near position 400) and the overall architecture of a soluble catalytic domain preceded by a short N-terminal hydrophobic stretch (LLPAFFLLVVFLFLLI). Knowledge from the P450 superfamily (learned from many characterized P450s) establishes that microsomal P450s, including plant P450s, possess a single N-terminal transmembrane anchor helix and a soluble catalytic domain. This family-level inference strongly disfavors option D (ten TM regions, characteristic of multi-pass channels/GPCRs) and option C (two TM regions, inconsistent with P450 topology). The N-terminal hydrophobic segment is clearly visible in the raw sequence, and its length (~21 residues from position 4 to 24) is appropriate for a single-pass TM helix. The distinction between A (4..24) and B (6..24) is a minor boundary question (2 residues: P-Q at positions 4-5); Pro at position 4 is moderately hydrophobic and TM predictions commonly include a few edge residues before the strongly hydrophobic core, making A defensible.",
    "missing_item_specific_fact": "",
    "reason": "Family-level knowledge of cytochrome P450 topology (single N-terminal TM anchor + soluble catalytic domain) meaningfully eliminates options C and D. The visible N-terminal hydrophobic stretch supports a single TM region. The A-vs-B boundary distinction is within the typical ±2-3 residue uncertainty of TM prediction, but including the moderately hydrophobic Pro at position 4 is consistent with standard TM helix boundary conventions, making A the more defensible choice among the offered alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "The difference between A (4..24) and B (6..24) is only two residues at the N-terminal edge (P-Q). Both describe a single N-terminal transmembrane helix of appropriate length for a P450 anchor. Hydrophobicity analysis of the raw sequence could reasonably place the TM boundary at either position, as P (hydropathy -1.6) and Q (-3.5) are at the interface between the signal-anchor region and the cytoplasmic/luminal flanking sequence. The annotation (prorule) chose 4, but a model relying on hydrophobicity alone might select 6 where the strongly hydrophobic F begins."
  },
  "important_caveats": [
    "The transmembrane annotation carries evidence code ECO:0000255 (prorule-based computational prediction), not experimental data. No experimental validation of the TM topology is cited.",
    "The protein identity (Alstonine synthase / Cytochrome P450 AS from Alstonia scholaris) was not provided to the evaluated model; the P450 family recognition must come from sequence motifs in the provided sequence.",
    "The A-vs-B boundary distinction (positions 4 vs 6) is within the typical uncertainty of TM prediction algorithms and represents a genuine ambiguity in the multiple-choice design."
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
  "benchmark_sequence_length": 514,
  "benchmark_sequence_sha256": "f8a5be35733d188ee2bee1b5df23d995bfe0c9c4a31237aa6a8988f9038cf055",
  "current_entry_audit": {
    "entryVersion": 14,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2023-05-03",
    "sequenceVersion": 1
  },
  "current_record_sha256": "59fe739ed168944070cd38e29550519331b1495ba5653a150fa3d35624899435",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 514,
  "current_source_sequence_sha256": "f8a5be35733d188ee2bee1b5df23d995bfe0c9c4a31237aa6a8988f9038cf055",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 13,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A9E7LUJ4",
  "selected_historical_entry_version": 13,
  "selected_historical_record_sha256": "cc693d1dbb0e42a4104ad818ad2836ecd8bdd9e71e50b40a970a3f13d0b5e109",
  "selected_historical_source_sequence_length": 514,
  "selected_historical_source_sequence_sha256": "f8a5be35733d188ee2bee1b5df23d995bfe0c9c4a31237aa6a8988f9038cf055",
  "selected_historical_version": {
    "accession": "A0A9E7LUJ4",
    "database": "Swiss-Prot",
    "entryVersion": 13,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "AS_ALSSC",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUJ4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A9E7LUJ4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:52.163393+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "59fe739ed168944070cd38e29550519331b1495ba5653a150fa3d35624899435",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7LUJ4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUJ4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":14,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2023-05-03\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:52.163393+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "59fe739ed168944070cd38e29550519331b1495ba5653a150fa3d35624899435",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7LUJ4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUJ4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Dogbane\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Apocynaceae\",\"Rauvolfioideae\",\"Alstonieae\",\"Alstonia\"],\"scientificName\":\"Alstonia scholaris\",\"synonyms\":[\"Echites scholaris\"],\"taxonId\":52822}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:52.163393+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "59fe739ed168944070cd38e29550519331b1495ba5653a150fa3d35624899435",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7LUJ4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUJ4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"value\":\"Cytochrome P450 AS\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"value\":\"1.14.19.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"value\":\"Alstonine synthase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"value\":\"AsAS\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:52.163393+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "59fe739ed168944070cd38e29550519331b1495ba5653a150fa3d35624899435",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7LUJ4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUJ4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":24},\"start\":{\"modifier\":\"EXACT\",\"value\":4}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-01T06:24:52.163393+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "59fe739ed168944070cd38e29550519331b1495ba5653a150fa3d35624899435",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7LUJ4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUJ4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Wang Z.\",\"Xiao Y.\",\"Wu S.\",\"Chen J.\",\"Li A.\",\"Tatsis E.C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"36349266\"},{\"database\":\"DOI\",\"id\":\"10.1039/d2sc03612f\"}],\"citationType\":\"journal article\",\"firstPage\":\"12389\",\"id\":\"36349266\",\"journal\":\"Chem. Sci.\",\"lastPage\":\"12395\",\"publicationDate\":\"2022\",\"title\":\"Deciphering and reprogramming the cyclization regioselectivity in bifurcation of indole alkaloid biosynthesis.\",\"volume\":\"13\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"URS65382.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:24:52.163393+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "59fe739ed168944070cd38e29550519331b1495ba5653a150fa3d35624899435",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7LUJ4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7LUJ4?format=txt&versions=13)

```json
{
  "entry_version": 13,
  "evidence_id": "H1",
  "excerpt": "ID   AS_ALSSC                Reviewed;         514 AA.\nAC   A0A9E7LUJ4;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   03-MAY-2023, sequence version 1.\nDT   28-JAN-2026, entry version 13.\nDE   RecName: Full=Alstonine synthase {ECO:0000303|PubMed:36349266};\nDE            Short=AsAS {ECO:0000303|PubMed:36349266};\nDE            EC=1.14.19.- {ECO:0000269|PubMed:36349266};\nDE   AltName: Full=Cytochrome P450 AS {ECO:0000303|PubMed:36349266};\nGN   Name=AS {ECO:0000303|PubMed:36349266};\nOS   Alstonia scholaris (Dogbane) (Echites scholaris).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Alstonieae;\nOC   Alstonia.\nOX   NCBI_TaxID=52822;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:37.040905+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cc693d1dbb0e42a4104ad818ad2836ecd8bdd9e71e50b40a970a3f13d0b5e109",
  "url": "https://rest.uniprot.org/unisave/A0A9E7LUJ4?format=txt&versions=13"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7LUJ4?format=txt&versions=13)

```json
{
  "entry_version": 13,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:URS65382.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, AND PATHWAY.\nRX   PubMed=36349266; DOI=10.1039/d2sc03612f;\nRA   Wang Z., Xiao Y., Wu S., Chen J., Li A., Tatsis E.C.;\nRT   \"Deciphering and reprogramming the cyclization regioselectivity in\nRT   bifurcation of indole alkaloid biosynthesis.\";\nRL   Chem. Sci. 13:12389-12395(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:37.040905+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 17-23",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cc693d1dbb0e42a4104ad818ad2836ecd8bdd9e71e50b40a970a3f13d0b5e109",
  "url": "https://rest.uniprot.org/unisave/A0A9E7LUJ4?format=txt&versions=13"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7LUJ4?format=txt&versions=13)

```json
{
  "entry_version": 13,
  "evidence_id": "H3",
  "excerpt": "FT   TRANSMEM        4..24\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:37.040905+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 80-82",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cc693d1dbb0e42a4104ad818ad2836ecd8bdd9e71e50b40a970a3f13d0b5e109",
  "url": "https://rest.uniprot.org/unisave/A0A9E7LUJ4?format=txt&versions=13"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 35. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
