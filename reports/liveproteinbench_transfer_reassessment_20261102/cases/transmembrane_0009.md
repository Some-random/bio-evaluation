# transmembrane_0009

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0009.txt)

**Task:** `transmembrane`  
**Expected answer:** **D** — 14..34; 47..67; 72..92; 121..141; 161..181

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTSHHSWYRYSINPFVLMGLVALFLAATANLTFFEKAMAVYPVSDNLGFIISMAVAVMGAMLLIVVLLSYRYVLKPVLILLLIMGAVTSYFTDTYGTVYDTTMLQNAMQTDQAESKDLMNLAFFVRIIGLGVLPSVLVAVAKVNYPTWGKGLIQRAMTWGVSLVLLLVPIGLFSSQYASFFRVHKPVRFYINPITPIYSVGKLASIEYKKATAPTDTIYHAKDAVQTTKPSERKPRLVVFVVGETARADHVQFNGYGRETFPQLAKVDGLANFSQVTSCGTSTAYSVPCMFSYLGQDDYDVDTAKYQENVLDTLDRLGVGILWRDNNSDSKGVMDKLPATQYFDYKSATNNTICNTNPYNECRDVGMLVGLDDYVSANNGKDMLIMLHQMGNHGPAYFKRYDEQFAKFTPVCEGNELAKCEHQSLINAYDNALLATDDFIAKSIDWLKTHEANYDVAMLYVSDHGESLGENGVYLHGMPNAFAPKEQRAVPAFFWSNNTTFKPTASDTVLTHDAITPTLLKLFDVTAGKVKDRAAFIQ

[Multiple Choices]
A. 14..34; 47..67; 72..92; 121..141
B. 30..50; 62..82; 108..128; 144..164; 186..206; 327..347; 357..377
C. 14..34; 47..67; 72..92; 122..141; 161..181
D. 14..34; 47..67; 72..92; 121..141; 161..181
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

> The sequence-matched UniProt records annotate five helical transmembrane regions at the coordinates in D. These annotations carry computational evidence code ECO:0000255, so they support the key as database annotations, not as direct experimental validation of every boundary.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has multiple strongly hydrophobic stretches in its N-terminal region, supporting a multi-pass membrane segment and making the options with substantially different regions implausible. Transferable sequence knowledge supports the five-helix pattern, but does not reliably distinguish whether the fourth segment starts at residue 121 or 122.


**Missing item-specific fact**

> The exact annotated start coordinate of the fourth transmembrane segment (121 versus 122) for this sequence.


**Reason**

> The offered choices include C and D, which otherwise specify the same five regions and differ by only one residue at that boundary. Hydropathy and general knowledge can support the membrane-spanning segments but do not meaningfully resolve that exact coordinate; the keyed distinction depends on a target-specific boundary annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> Both choices identify the same likely set of membrane-spanning helices, and a one-residue difference at a predicted helix boundary is not biologically distinguishable from the sequence alone.


### Important caveats

- The cited transmembrane features are computational annotations, not evidence that all boundaries were experimentally measured.
- The sequence matches the cited historical and current records, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has multiple strongly hydrophobic stretches in its N-terminal region, supporting a multi-pass membrane segment and making the options with substantially different regions implausible. Transferable sequence knowledge supports the five-helix pattern, but does not reliably distinguish whether the fourth segment starts at residue 121 or 122.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact annotated start coordinate of the fourth transmembrane segment (121 versus 122) for this sequence.",
    "reason": "The offered choices include C and D, which otherwise specify the same five regions and differ by only one residue at that boundary. Hydropathy and general knowledge can support the membrane-spanning segments but do not meaningfully resolve that exact coordinate; the keyed distinction depends on a target-specific boundary annotation."
  },
  "case_id": "transmembrane_0009",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H4",
      "H5",
      "H6",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt records annotate five helical transmembrane regions at the coordinates in D. These annotations carry computational evidence code ECO:0000255, so they support the key as database annotations, not as direct experimental validation of every boundary."
  },
  "important_caveats": [
    "The cited transmembrane features are computational annotations, not evidence that all boundaries were experimentally measured.",
    "The sequence matches the cited historical and current records, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "Both choices identify the same likely set of membrane-spanning helices, and a one-residue difference at a predicted helix boundary is not biologically distinguishable from the sequence alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0009",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt records annotate five helical transmembrane regions at the coordinates in D. These annotations carry computational evidence code ECO:0000255, so they support the key as database annotations, not as direct experimental validation of every boundary.",
    "evidence_ids": ["H3", "H4", "H5", "H6", "H7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has multiple strongly hydrophobic stretches in its N-terminal region, supporting a multi-pass membrane segment and making the options with substantially different regions implausible. Transferable sequence knowledge supports the five-helix pattern, but does not reliably distinguish whether the fourth segment starts at residue 121 or 122.",
    "missing_item_specific_fact": "The exact annotated start coordinate of the fourth transmembrane segment (121 versus 122) for this sequence.",
    "reason": "The offered choices include C and D, which otherwise specify the same five regions and differ by only one residue at that boundary. Hydropathy and general knowledge can support the membrane-spanning segments but do not meaningfully resolve that exact coordinate; the keyed distinction depends on a target-specific boundary annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "Both choices identify the same likely set of membrane-spanning helices, and a one-residue difference at a predicted helix boundary is not biologically distinguishable from the sequence alone."
  },
  "important_caveats": [
    "The cited transmembrane features are computational annotations, not evidence that all boundaries were experimentally measured.",
    "The sequence matches the cited historical and current records, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for this sequence (A0A1C3NEV1, MCR-2) lists exactly five transmembrane helical regions at 14..34, 47..67, 72..92, 121..141, and 161..181, all annotated with evidence code ECO:0000255 (by similarity/computational prediction). Option D matches these five regions exactly. The annotations are computational (by similarity), not experimental—the crystal structure (PDB 6A7W) covers only residues 215–538 and does not span the TM regions. Nonetheless, the recorded annotation fully supports choice D.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model can perform hydrophobicity analysis on the supplied 538-residue sequence. Option B is readily excluded because its proposed regions (e.g., 30..50 containing E, K, S, D, N, Y, P; 62..82 containing R, K, S, Y, P) include multiple charged and polar residues incompatible with a lipid-bilayer-spanning helix. Option A (four TM regions) can be excluded because positions 161–181 (V, S, L, V, L, L, L, V, P, I, G, L, F, S, S, Q, Y, A, S, F, F) contain a sufficient hydrophobic core (V, L, V, L, L, L, V, I, L, F, Y, A, F, F) to constitute a fifth TM helix, consistent with the known multi-helix TM domain architecture of MCR-family phosphoethanolamine transferases. The distinction between C (122..141) and D (121..141) rests on the boundary at position 121: residue 120 is N (polar), while residue 121 is L (strongly hydrophobic), making 121 the natural hydrophobic-segment start after the polar loop. This is a standard hydrophobicity-window inference. Family-level knowledge of MCR proteins (MCR-1, MCR-2, MCR-3) having a multi-helix TM domain in the N-terminal ~200 residues further supports identifying five rather than four TM segments.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The key distinctions among options can be made through hydrophobicity analysis of the supplied sequence and transferable knowledge of MCR-family TM domain architecture. Option B is eliminated by charged residues in proposed TM regions. Option A is eliminated by identifying the hydrophobic stretch at 161–181. The C-vs-D single-residue boundary difference (121 vs 122) is resolved by noting that L(121) is hydrophobic and immediately follows the polar N(120), making it the logical TM start. While the 1-residue boundary is marginal, the hydrophobicity argument is a legitimate transferable inference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> The difference between C (122..141) and D (121..141) is a single-residue boundary shift. Both L(121) and A(122) are hydrophobic, and TM prediction tools commonly have ±1–2 residue boundary uncertainty. While the hydrophobicity argument slightly favors starting at 121 (the first hydrophobic residue after polar N120), a model using a sliding-window approach might reasonably place the boundary at 122. This makes C and D nearly indistinguishable by pure sequence reasoning alone.


### Important caveats

- All five TM annotations carry evidence code ECO:0000255 (by similarity), meaning they are computational predictions transferred from homologs, not experimentally validated boundaries.
- The crystal structure (PDB 6A7W) resolves only residues 215–538 and does not cover the TM region, so no experimental boundary data exists for these helices.
- The C-vs-D distinction (121 vs 122 start) is at the limit of resolution achievable by hydrophobicity analysis alone; the annotation's choice of 121 is defensible but not uniquely determined by sequence.
- The protein is identified as MCR-2 (phosphoethanolamine transferase) from E. coli in the source record, but this identity was not provided to the evaluated model; the model must work from sequence and general TM-prediction principles.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can perform hydrophobicity analysis on the supplied 538-residue sequence. Option B is readily excluded because its proposed regions (e.g., 30..50 containing E, K, S, D, N, Y, P; 62..82 containing R, K, S, Y, P) include multiple charged and polar residues incompatible with a lipid-bilayer-spanning helix. Option A (four TM regions) can be excluded because positions 161–181 (V, S, L, V, L, L, L, V, P, I, G, L, F, S, S, Q, Y, A, S, F, F) contain a sufficient hydrophobic core (V, L, V, L, L, L, V, I, L, F, Y, A, F, F) to constitute a fifth TM helix, consistent with the known multi-helix TM domain architecture of MCR-family phosphoethanolamine transferases. The distinction between C (122..141) and D (121..141) rests on the boundary at position 121: residue 120 is N (polar), while residue 121 is L (strongly hydrophobic), making 121 the natural hydrophobic-segment start after the polar loop. This is a standard hydrophobicity-window inference. Family-level knowledge of MCR proteins (MCR-1, MCR-2, MCR-3) having a multi-helix TM domain in the N-terminal ~200 residues further supports identifying five rather than four TM segments.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The key distinctions among options can be made through hydrophobicity analysis of the supplied sequence and transferable knowledge of MCR-family TM domain architecture. Option B is eliminated by charged residues in proposed TM regions. Option A is eliminated by identifying the hydrophobic stretch at 161–181. The C-vs-D single-residue boundary difference (121 vs 122) is resolved by noting that L(121) is hydrophobic and immediately follows the polar N(120), making it the logical TM start. While the 1-residue boundary is marginal, the hydrophobicity argument is a legitimate transferable inference."
  },
  "case_id": "transmembrane_0009",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "H3",
      "H4",
      "H5",
      "H6",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for this sequence (A0A1C3NEV1, MCR-2) lists exactly five transmembrane helical regions at 14..34, 47..67, 72..92, 121..141, and 161..181, all annotated with evidence code ECO:0000255 (by similarity/computational prediction). Option D matches these five regions exactly. The annotations are computational (by similarity), not experimental—the crystal structure (PDB 6A7W) covers only residues 215–538 and does not span the TM regions. Nonetheless, the recorded annotation fully supports choice D."
  },
  "important_caveats": [
    "All five TM annotations carry evidence code ECO:0000255 (by similarity), meaning they are computational predictions transferred from homologs, not experimentally validated boundaries.",
    "The crystal structure (PDB 6A7W) resolves only residues 215–538 and does not cover the TM region, so no experimental boundary data exists for these helices.",
    "The C-vs-D distinction (121 vs 122 start) is at the limit of resolution achievable by hydrophobicity analysis alone; the annotation's choice of 121 is defensible but not uniquely determined by sequence.",
    "The protein is identified as MCR-2 (phosphoethanolamine transferase) from E. coli in the source record, but this identity was not provided to the evaluated model; the model must work from sequence and general TM-prediction principles."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "The difference between C (122..141) and D (121..141) is a single-residue boundary shift. Both L(121) and A(122) are hydrophobic, and TM prediction tools commonly have ±1–2 residue boundary uncertainty. While the hydrophobicity argument slightly favors starting at 121 (the first hydrophobic residue after polar N120), a model using a sliding-window approach might reasonably place the boundary at 122. This makes C and D nearly indistinguishable by pure sequence reasoning alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0009",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for this sequence (A0A1C3NEV1, MCR-2) lists exactly five transmembrane helical regions at 14..34, 47..67, 72..92, 121..141, and 161..181, all annotated with evidence code ECO:0000255 (by similarity/computational prediction). Option D matches these five regions exactly. The annotations are computational (by similarity), not experimental—the crystal structure (PDB 6A7W) covers only residues 215–538 and does not span the TM regions. Nonetheless, the recorded annotation fully supports choice D.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "H3", "H4", "H5", "H6", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model can perform hydrophobicity analysis on the supplied 538-residue sequence. Option B is readily excluded because its proposed regions (e.g., 30..50 containing E, K, S, D, N, Y, P; 62..82 containing R, K, S, Y, P) include multiple charged and polar residues incompatible with a lipid-bilayer-spanning helix. Option A (four TM regions) can be excluded because positions 161–181 (V, S, L, V, L, L, L, V, P, I, G, L, F, S, S, Q, Y, A, S, F, F) contain a sufficient hydrophobic core (V, L, V, L, L, L, V, I, L, F, Y, A, F, F) to constitute a fifth TM helix, consistent with the known multi-helix TM domain architecture of MCR-family phosphoethanolamine transferases. The distinction between C (122..141) and D (121..141) rests on the boundary at position 121: residue 120 is N (polar), while residue 121 is L (strongly hydrophobic), making 121 the natural hydrophobic-segment start after the polar loop. This is a standard hydrophobicity-window inference. Family-level knowledge of MCR proteins (MCR-1, MCR-2, MCR-3) having a multi-helix TM domain in the N-terminal ~200 residues further supports identifying five rather than four TM segments.",
    "missing_item_specific_fact": "",
    "reason": "The key distinctions among options can be made through hydrophobicity analysis of the supplied sequence and transferable knowledge of MCR-family TM domain architecture. Option B is eliminated by charged residues in proposed TM regions. Option A is eliminated by identifying the hydrophobic stretch at 161–181. The C-vs-D single-residue boundary difference (121 vs 122) is resolved by noting that L(121) is hydrophobic and immediately follows the polar N(120), making it the logical TM start. While the 1-residue boundary is marginal, the hydrophobicity argument is a legitimate transferable inference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "The difference between C (122..141) and D (121..141) is a single-residue boundary shift. Both L(121) and A(122) are hydrophobic, and TM prediction tools commonly have ±1–2 residue boundary uncertainty. While the hydrophobicity argument slightly favors starting at 121 (the first hydrophobic residue after polar N120), a model using a sliding-window approach might reasonably place the boundary at 122. This makes C and D nearly indistinguishable by pure sequence reasoning alone."
  },
  "important_caveats": [
    "All five TM annotations carry evidence code ECO:0000255 (by similarity), meaning they are computational predictions transferred from homologs, not experimentally validated boundaries.",
    "The crystal structure (PDB 6A7W) resolves only residues 215–538 and does not cover the TM region, so no experimental boundary data exists for these helices.",
    "The C-vs-D distinction (121 vs 122 start) is at the limit of resolution achievable by hydrophobicity analysis alone; the annotation's choice of 121 is defensible but not uniquely determined by sequence.",
    "The protein is identified as MCR-2 (phosphoethanolamine transferase) from E. coli in the source record, but this identity was not provided to the evaluated model; the model must work from sequence and general TM-prediction principles."
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
  "benchmark_sequence_length": 538,
  "benchmark_sequence_sha256": "ac11cd8f4c43b75871bc89c0dbaa1f186110d0c878b6152a899c2abf8270e1ac",
  "current_entry_audit": {
    "entryVersion": 40,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2016-11-02",
    "sequenceVersion": 1
  },
  "current_record_sha256": "919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 538,
  "current_source_sequence_sha256": "ac11cd8f4c43b75871bc89c0dbaa1f186110d0c878b6152a899c2abf8270e1ac",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 38,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A1C3NEV1",
  "selected_historical_entry_version": 38,
  "selected_historical_record_sha256": "d75fc4c8bc738f05806f3af9945e4dc68a9d390599953db777a2ada2b9fa9923",
  "selected_historical_source_sequence_length": 538,
  "selected_historical_source_sequence_sha256": "ac11cd8f4c43b75871bc89c0dbaa1f186110d0c878b6152a899c2abf8270e1ac",
  "selected_historical_version": {
    "accession": "A0A1C3NEV1",
    "database": "Swiss-Prot",
    "entryVersion": 38,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MCR2_ECOLX",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A1C3NEV1\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:32.663314+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":40,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2016-11-02\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:32.663314+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"SBV31106.1\",\"source\":\"EMBL\"}],\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Enterobacterales\",\"Enterobacteriaceae\",\"Escherichia\"],\"scientificName\":\"Escherichia coli\",\"taxonId\":562}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:32.663314+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A0R6L508\",\"source\":\"UniProtKB\"}],\"value\":\"Polymyxin resistance protein MCR-2\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"30194678\",\"source\":\"PubMed\"}],\"value\":\"2.7.8.43\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30194678\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"Ref.1\",\"source\":\"Reference\"}],\"value\":\"Phosphatidylethanolamine transferase Mcr-2\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:32.663314+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":34},\"start\":{\"modifier\":\"EXACT\",\"value\":14}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:24:32.663314+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":67},\"start\":{\"modifier\":\"EXACT\",\"value\":47}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:24:32.663314+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":92},\"start\":{\"modifier\":\"EXACT\",\"value\":72}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:24:32.663314+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":141},\"start\":{\"modifier\":\"EXACT\",\"value\":121}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:24:32.663314+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":181},\"start\":{\"modifier\":\"EXACT\",\"value\":161}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:24:32.663314+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Wang X.\",\"Lu Q.\",\"Qi J.\",\"Chai Y.\",\"Wang Y.\",\"Gao G.F.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30194678\"},{\"database\":\"DOI\",\"id\":\"10.1007/s11427-018-9363-4\"}],\"citationType\":\"journal article\",\"firstPage\":\"1432\",\"id\":\"30194678\",\"journal\":\"Sci. China Life Sci.\",\"lastPage\":\"1436\",\"publicationDate\":\"2018\",\"title\":\"Structural and functional insights into MCR-2 mediated colistin resistance.\",\"volume\":\"61\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6A7W\",\"source\":\"PDB\"}],\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"WHI04997.1\",\"source\":\"EMBL\"}],\"type\":\"PLASMID\",\"value\":\"unnamed5\"}],\"referenceNumber\":4,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.99 ANGSTROMS) OF 215-538 IN COMPLEX WITH ZN(2+)\",\"DISULFIDE BONDS\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"MUTAGENESIS OF PHE-91; TYR-99; MET-103; ASN-106; THR-110; GLU-114; SER-115; PHE-123; THR-283; LYS-331 AND HIS-476\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:24:32.663314+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H1",
  "excerpt": "ID   MCR2_ECOLX              Reviewed;         538 AA.\nAC   A0A1C3NEV1;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   02-NOV-2016, sequence version 1.\nDT   28-JAN-2026, entry version 38.\nDE   RecName: Full=Phosphatidylethanolamine transferase Mcr-2 {ECO:0000303|PubMed:30194678, ECO:0000303|Ref.1};\nDE            EC=2.7.8.43 {ECO:0000305|PubMed:30194678};\nDE   AltName: Full=Polymyxin resistance protein MCR-2 {ECO:0000250|UniProtKB:A0A0R6L508};\nGN   Name=mcr2 {ECO:0000305}; Synonyms=mcr-2 {ECO:0000312|EMBL:SBV31106.1};\nGN   ORFNames=QDW62_28200 {ECO:0000312|EMBL:WHI04997.1};\nOS   Escherichia coli.\nOG   Plasmid pKP37-BE {ECO:0000312|EMBL:SBV31106.1}, and\nOG   Plasmid unnamed5 {ECO:0000312|EMBL:WHI04997.1}.\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Enterobacterales; Enterobacteriaceae; Escherichia.\nOX   NCBI_TaxID=562 {ECO:0000312|EMBL:SBV31106.1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:35.172422+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d75fc4c8bc738f05806f3af9945e4dc68a9d390599953db777a2ada2b9fa9923",
  "url": "https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H2",
  "excerpt": "RN   [4] {ECO:0007744|PDB:6A7W}\nRP   X-RAY CRYSTALLOGRAPHY (2.99 ANGSTROMS) OF 215-538 IN COMPLEX WITH ZN(2+),\nRP   DISULFIDE BONDS, FUNCTION, CATALYTIC ACTIVITY, AND MUTAGENESIS OF PHE-91;\nRP   TYR-99; MET-103; ASN-106; THR-110; GLU-114; SER-115; PHE-123; THR-283;\nRP   LYS-331 AND HIS-476.\nRC   PLASMID=unnamed5 {ECO:0000312|EMBL:WHI04997.1};\nRX   PubMed=30194678; DOI=10.1007/s11427-018-9363-4;\nRA   Wang X., Lu Q., Qi J., Chai Y., Wang Y., Gao G.F.;\nRT   \"Structural and functional insights into MCR-2 mediated colistin\nRT   resistance.\";\nRL   Sci. China Life Sci. 61:1432-1436(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:35.172422+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 44-54",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d75fc4c8bc738f05806f3af9945e4dc68a9d390599953db777a2ada2b9fa9923",
  "url": "https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H3",
  "excerpt": "FT   TRANSMEM        14..34\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:35.172422+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 133-135",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d75fc4c8bc738f05806f3af9945e4dc68a9d390599953db777a2ada2b9fa9923",
  "url": "https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H4",
  "excerpt": "FT   TRANSMEM        47..67\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:35.172422+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 136-138",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d75fc4c8bc738f05806f3af9945e4dc68a9d390599953db777a2ada2b9fa9923",
  "url": "https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H5",
  "excerpt": "FT   TRANSMEM        72..92\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:35.172422+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 139-141",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d75fc4c8bc738f05806f3af9945e4dc68a9d390599953db777a2ada2b9fa9923",
  "url": "https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H6",
  "excerpt": "FT   TRANSMEM        121..141\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:35.172422+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 142-144",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d75fc4c8bc738f05806f3af9945e4dc68a9d390599953db777a2ada2b9fa9923",
  "url": "https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H7",
  "excerpt": "FT   TRANSMEM        161..181\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:35.172422+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 145-147",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d75fc4c8bc738f05806f3af9945e4dc68a9d390599953db777a2ada2b9fa9923",
  "url": "https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 9. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
