# transmembrane_0005

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0005.txt)

**Task:** `transmembrane`  
**Expected answer:** **C** — 9..29; 41..61; 84..104; 118..138; 153..173; 175..195; 202..222; 231..251

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKNNKISGFQWAMTIFVFFVITMALSIMLRDFQSIIGVKHFIFEVTDLAPLIAAIICILVFKYKKVQLAGLKFSISLKVIERLLLALILPLIILIIGMYSFNTFADSFILLQSTGLSVPITHILIGHILMAFVVEFGFRSYLQNIVETKMNTFFASIVVGLMYSVFSANTTYGTEFAAYNFLYTFSFSMILGELIRATKGRTIYIATTFHASMTFGLIFLFSEEIGDLFSIKVIAISTAIVAVGYIGLSLIIRGIAYLTTRRNLEELEPNNYLDHVNDDEETNHTEAEKSSSNIKDAEKTGVATASTVGVAKNDTENTVADEPSIHEGTEKTEPQHHIGNQTESNHDEDHDITSESVESAESVKQAPQSDDLTNDSNEDEIEQSLKEPVTYKEDRRSSVVIDAEKHIEKTEEQSSDKNK

[Multiple Choices]
A. 9..29; 42..61; 84..104; 118..138; 153..173; 175..195; 202..222; 231..251
B. 9..29; 41..61; 84..104; 118..138; 153..173; 175..195; 202..222
C. 9..29; 41..61; 84..104; 118..138; 153..173; 175..195; 202..222; 231..251
D. 3..23
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

> The sequence-matched historical UniProt record lists all eight helical transmembrane regions in choice C. These are computational annotations (ECO:0000255), not evidence of experimental validation; the author's exact source snapshot is unknown.

Citations as saved: [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains repeated long, hydrophobic stretches characteristic of membrane-spanning helices, including a hydrophobic stretch around residues 231–251. This gives a credible sequence-based reason to favor the eight-region alternatives A or C over B, which omits that region, and D, which lists only one segment.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable knowledge about hydrophobic transmembrane helices meaningfully identifies the multi-pass pattern and supports the inclusion of the final hydrophobic segment. It does not resolve the one-residue start-coordinate difference between A and C.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> A and C differ only in whether the second span begins at residue 42 or 41. That one-residue boundary difference is not meaningfully distinguishable from the sequence as a membrane-crossing prediction, and both alternatives include the same evident hydrophobic spans.


### Important caveats

- The cited database annotations are computational predictions, not experimental measurements.
- The reviewer-only source sequence matches the input, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains repeated long, hydrophobic stretches characteristic of membrane-spanning helices, including a hydrophobic stretch around residues 231–251. This gives a credible sequence-based reason to favor the eight-region alternatives A or C over B, which omits that region, and D, which lists only one segment.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge about hydrophobic transmembrane helices meaningfully identifies the multi-pass pattern and supports the inclusion of the final hydrophobic segment. It does not resolve the one-residue start-coordinate difference between A and C."
  },
  "case_id": "transmembrane_0005",
  "expected_answer_check": {
    "evidence_ids": [
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9",
      "H10",
      "H11"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record lists all eight helical transmembrane regions in choice C. These are computational annotations (ECO:0000255), not evidence of experimental validation; the author's exact source snapshot is unknown."
  },
  "important_caveats": [
    "The cited database annotations are computational predictions, not experimental measurements.",
    "The reviewer-only source sequence matches the input, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "A and C differ only in whether the second span begins at residue 42 or 41. That one-residue boundary difference is not meaningfully distinguishable from the sequence as a membrane-crossing prediction, and both alternatives include the same evident hydrophobic spans."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0005",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record lists all eight helical transmembrane regions in choice C. These are computational annotations (ECO:0000255), not evidence of experimental validation; the author's exact source snapshot is unknown.",
    "evidence_ids": ["H4", "H5", "H6", "H7", "H8", "H9", "H10", "H11"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains repeated long, hydrophobic stretches characteristic of membrane-spanning helices, including a hydrophobic stretch around residues 231–251. This gives a credible sequence-based reason to favor the eight-region alternatives A or C over B, which omits that region, and D, which lists only one segment.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge about hydrophobic transmembrane helices meaningfully identifies the multi-pass pattern and supports the inclusion of the final hydrophobic segment. It does not resolve the one-residue start-coordinate difference between A and C."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "A and C differ only in whether the second span begins at residue 42 or 41. That one-residue boundary difference is not meaningfully distinguishable from the sequence as a membrane-crossing prediction, and both alternatives include the same evident hydrophobic spans."
  },
  "important_caveats": [
    "The cited database annotations are computational predictions, not experimental measurements.",
    "The reviewer-only source sequence matches the input, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for A0A0H3KA40 (sequence matched) lists exactly eight transmembrane helical segments at 9-29, 41-61, 84-104, 118-138, 153-173, 175-195, 202-222, and 231-251, matching choice C precisely. All annotations carry evidence code ECO:0000255 (similarity-based/computational inference), not experimental determination, but they constitute the recorded annotation that the key reflects.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein sequence shows a clear alternating pattern of hydrophobic and hydrophilic stretches characteristic of a multi-pass membrane protein, immediately eliminating D (single TM). The hydrophobic stretch at approximately residues 231-251 (IVAISITAIVAVGYIGLSLI) is a recognizable 21-residue hydrophobic segment flanked by a polar/charged N-side (…FSEEIGDLFSIK) and a strongly hydrophilic C-terminal tail (…IRGIAYLTTRRNLEELEPNNYLDHVNDDEET…), making it a credible eighth TM helix candidate. This distinguishes C (8 TMs) from B (7 TMs, which omits 231-251). The distinction between A and C is a single-residue boundary shift (second TM starting at 42 vs 41); residue 41 is F (phenylalanine, strongly hydrophobic) while residue 40 is H (histidine, polar/charged), so including F(41) in the TM helix is the more natural boundary assignment, marginally favoring C over A.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can (1) recognize the multi-pass membrane topology from the alternating hydrophobic/hydrophilic pattern, eliminating D; (2) identify the hydrophobic segment at ~231-251 as a TM helix bounded by a charged/polar loop on one side and a hydrophilic tail on the other, eliminating B; and (3) note that F(41) is hydrophobic while H(40) is polar, favoring a TM start at 41 over 42, which marginally favors C over A. The 1-residue boundary difference is within the normal ±1-2 residue uncertainty of any TM predictor, but the sequence context (H preceding F) provides a weak but real preference for C.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> A and C differ only by whether the second TM helix begins at residue 41 or 42. Both F(41) and I(42) are strongly hydrophobic, and TM helix boundaries are inherently uncertain to ±1-2 residues in any prediction method. A model could reasonably assign the boundary to either position. However, H(40) being polar/charged slightly favors starting the helix at F(41), giving a marginal edge to C. This is a minor boundary-assignment ambiguity, not a fundamental flaw.


### Important caveats

- All UniProt TM annotations carry evidence code ECO:0000255 (similarity-based), meaning they are computational predictions transferred from homologs, not experimentally determined boundaries.
- The 1-residue boundary difference between A and C is within the normal uncertainty of TM prediction tools (TMHMM, Phobius, etc.), so the distinction is not robustly derivable from sequence alone.
- The main discrimination (8 TMs vs 7 TMs, i.e., C vs B) is the substantive and answerable part of the question.
- The UniProt entry was first publicly released in June 2025; the author's source snapshot is unknown, though the sequence has been unchanged since September 2015.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein sequence shows a clear alternating pattern of hydrophobic and hydrophilic stretches characteristic of a multi-pass membrane protein, immediately eliminating D (single TM). The hydrophobic stretch at approximately residues 231-251 (IVAISITAIVAVGYIGLSLI) is a recognizable 21-residue hydrophobic segment flanked by a polar/charged N-side (…FSEEIGDLFSIK) and a strongly hydrophilic C-terminal tail (…IRGIAYLTTRRNLEELEPNNYLDHVNDDEET…), making it a credible eighth TM helix candidate. This distinguishes C (8 TMs) from B (7 TMs, which omits 231-251). The distinction between A and C is a single-residue boundary shift (second TM starting at 42 vs 41); residue 41 is F (phenylalanine, strongly hydrophobic) while residue 40 is H (histidine, polar/charged), so including F(41) in the TM helix is the more natural boundary assignment, marginally favoring C over A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can (1) recognize the multi-pass membrane topology from the alternating hydrophobic/hydrophilic pattern, eliminating D; (2) identify the hydrophobic segment at ~231-251 as a TM helix bounded by a charged/polar loop on one side and a hydrophilic tail on the other, eliminating B; and (3) note that F(41) is hydrophobic while H(40) is polar, favoring a TM start at 41 over 42, which marginally favors C over A. The 1-residue boundary difference is within the normal ±1-2 residue uncertainty of any TM predictor, but the sequence context (H preceding F) provides a weak but real preference for C."
  },
  "case_id": "transmembrane_0005",
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
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9",
      "H10",
      "H11"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for A0A0H3KA40 (sequence matched) lists exactly eight transmembrane helical segments at 9-29, 41-61, 84-104, 118-138, 153-173, 175-195, 202-222, and 231-251, matching choice C precisely. All annotations carry evidence code ECO:0000255 (similarity-based/computational inference), not experimental determination, but they constitute the recorded annotation that the key reflects."
  },
  "important_caveats": [
    "All UniProt TM annotations carry evidence code ECO:0000255 (similarity-based), meaning they are computational predictions transferred from homologs, not experimentally determined boundaries.",
    "The 1-residue boundary difference between A and C is within the normal uncertainty of TM prediction tools (TMHMM, Phobius, etc.), so the distinction is not robustly derivable from sequence alone.",
    "The main discrimination (8 TMs vs 7 TMs, i.e., C vs B) is the substantive and answerable part of the question.",
    "The UniProt entry was first publicly released in June 2025; the author's source snapshot is unknown, though the sequence has been unchanged since September 2015."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "A and C differ only by whether the second TM helix begins at residue 41 or 42. Both F(41) and I(42) are strongly hydrophobic, and TM helix boundaries are inherently uncertain to ±1-2 residues in any prediction method. A model could reasonably assign the boundary to either position. However, H(40) being polar/charged slightly favors starting the helix at F(41), giving a marginal edge to C. This is a minor boundary-assignment ambiguity, not a fundamental flaw."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0005",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for A0A0H3KA40 (sequence matched) lists exactly eight transmembrane helical segments at 9-29, 41-61, 84-104, 118-138, 153-173, 175-195, 202-222, and 231-251, matching choice C precisely. All annotations carry evidence code ECO:0000255 (similarity-based/computational inference), not experimental determination, but they constitute the recorded annotation that the key reflects.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "H11"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein sequence shows a clear alternating pattern of hydrophobic and hydrophilic stretches characteristic of a multi-pass membrane protein, immediately eliminating D (single TM). The hydrophobic stretch at approximately residues 231-251 (IVAISITAIVAVGYIGLSLI) is a recognizable 21-residue hydrophobic segment flanked by a polar/charged N-side (…FSEEIGDLFSIK) and a strongly hydrophilic C-terminal tail (…IRGIAYLTTRRNLEELEPNNYLDHVNDDEET…), making it a credible eighth TM helix candidate. This distinguishes C (8 TMs) from B (7 TMs, which omits 231-251). The distinction between A and C is a single-residue boundary shift (second TM starting at 42 vs 41); residue 41 is F (phenylalanine, strongly hydrophobic) while residue 40 is H (histidine, polar/charged), so including F(41) in the TM helix is the more natural boundary assignment, marginally favoring C over A.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can (1) recognize the multi-pass membrane topology from the alternating hydrophobic/hydrophilic pattern, eliminating D; (2) identify the hydrophobic segment at ~231-251 as a TM helix bounded by a charged/polar loop on one side and a hydrophilic tail on the other, eliminating B; and (3) note that F(41) is hydrophobic while H(40) is polar, favoring a TM start at 41 over 42, which marginally favors C over A. The 1-residue boundary difference is within the normal ±1-2 residue uncertainty of any TM predictor, but the sequence context (H preceding F) provides a weak but real preference for C."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "A and C differ only by whether the second TM helix begins at residue 41 or 42. Both F(41) and I(42) are strongly hydrophobic, and TM helix boundaries are inherently uncertain to ±1-2 residues in any prediction method. A model could reasonably assign the boundary to either position. However, H(40) being polar/charged slightly favors starting the helix at F(41), giving a marginal edge to C. This is a minor boundary-assignment ambiguity, not a fundamental flaw."
  },
  "important_caveats": [
    "All UniProt TM annotations carry evidence code ECO:0000255 (similarity-based), meaning they are computational predictions transferred from homologs, not experimentally determined boundaries.",
    "The 1-residue boundary difference between A and C is within the normal uncertainty of TM prediction tools (TMHMM, Phobius, etc.), so the distinction is not robustly derivable from sequence alone.",
    "The main discrimination (8 TMs vs 7 TMs, i.e., C vs B) is the substantive and answerable part of the question.",
    "The UniProt entry was first publicly released in June 2025; the author's source snapshot is unknown, though the sequence has been unchanged since September 2015."
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
  "benchmark_sequence_length": 419,
  "benchmark_sequence_sha256": "bf64f9d9785229636b37dbec53661c2fc5d174ff9bc941655a421585f73e403f",
  "current_entry_audit": {
    "entryVersion": 38,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2015-09-16",
    "sequenceVersion": 1
  },
  "current_record_sha256": "01b319fc1f34daeda156e8cfc7e6f4bb541e8c4bcb4a73e8f3c4f78c8d2c62d2",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 419,
  "current_source_sequence_sha256": "bf64f9d9785229636b37dbec53661c2fc5d174ff9bc941655a421585f73e403f",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 36,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A0H3KA40",
  "selected_historical_entry_version": 36,
  "selected_historical_record_sha256": "d02c88a1544f67f6b8c7af47b40f478812539c62fe01fc0b43e7958088f0d2ff",
  "selected_historical_source_sequence_length": 419,
  "selected_historical_source_sequence_sha256": "bf64f9d9785229636b37dbec53661c2fc5d174ff9bc941655a421585f73e403f",
  "selected_historical_version": {
    "accession": "A0A0H3KA40",
    "database": "Swiss-Prot",
    "entryVersion": 36,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "LYRA_STAAE",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A0H3KA40\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:09.578744+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "01b319fc1f34daeda156e8cfc7e6f4bb541e8c4bcb4a73e8f3c4f78c8d2c62d2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":38,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2015-09-16\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:09.578744+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "01b319fc1f34daeda156e8cfc7e6f4bb541e8c4bcb4a73e8f3c4f78c8d2c62d2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Bacillati\",\"Bacillota\",\"Bacilli\",\"Caryophanales\",\"Staphylococcaceae\",\"Staphylococcus\"],\"scientificName\":\"Staphylococcus aureus (strain Newman)\",\"taxonId\":426430}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:09.578744+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "01b319fc1f34daeda156e8cfc7e6f4bb541e8c4bcb4a73e8f3c4f78c8d2c62d2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20923422\",\"source\":\"PubMed\"}],\"value\":\"Abortive infectivity domain-containing protein\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20923422\",\"source\":\"PubMed\"}],\"value\":\"Surface protein display C\"}}],\"recommendedName\":{\"fullName\":{\"value\":\"Lysostaphin resistance protein A\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:09.578744+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "01b319fc1f34daeda156e8cfc7e6f4bb541e8c4bcb4a73e8f3c4f78c8d2c62d2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":29},\"start\":{\"modifier\":\"EXACT\",\"value\":9}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:24:09.578744+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "01b319fc1f34daeda156e8cfc7e6f4bb541e8c4bcb4a73e8f3c4f78c8d2c62d2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":61},\"start\":{\"modifier\":\"EXACT\",\"value\":41}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:24:09.578744+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "01b319fc1f34daeda156e8cfc7e6f4bb541e8c4bcb4a73e8f3c4f78c8d2c62d2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":104},\"start\":{\"modifier\":\"EXACT\",\"value\":84}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:24:09.578744+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "01b319fc1f34daeda156e8cfc7e6f4bb541e8c4bcb4a73e8f3c4f78c8d2c62d2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":138},\"start\":{\"modifier\":\"EXACT\",\"value\":118}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:24:09.578744+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "01b319fc1f34daeda156e8cfc7e6f4bb541e8c4bcb4a73e8f3c4f78c8d2c62d2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":173},\"start\":{\"modifier\":\"EXACT\",\"value\":153}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:24:09.578744+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "01b319fc1f34daeda156e8cfc7e6f4bb541e8c4bcb4a73e8f3c4f78c8d2c62d2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":195},\"start\":{\"modifier\":\"EXACT\",\"value\":175}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:24:09.578744+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "01b319fc1f34daeda156e8cfc7e6f4bb541e8c4bcb4a73e8f3c4f78c8d2c62d2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":222},\"start\":{\"modifier\":\"EXACT\",\"value\":202}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:24:09.578744+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "01b319fc1f34daeda156e8cfc7e6f4bb541e8c4bcb4a73e8f3c4f78c8d2c62d2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":251},\"start\":{\"modifier\":\"EXACT\",\"value\":231}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:24:09.578744+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "01b319fc1f34daeda156e8cfc7e6f4bb541e8c4bcb4a73e8f3c4f78c8d2c62d2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"citation\":{\"authors\":[\"Frankel M.B.\",\"Wojcik B.M.\",\"DeDent A.C.\",\"Missiakas D.M.\",\"Schneewind O.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"20923422\"},{\"database\":\"DOI\",\"id\":\"10.1111/j.1365-2958.2010.07334.x\"}],\"citationType\":\"journal article\",\"firstPage\":\"238\",\"id\":\"20923422\",\"journal\":\"Mol. Microbiol.\",\"lastPage\":\"252\",\"publicationDate\":\"2010\",\"title\":\"ABI domain-containing proteins contribute to surface protein display and cell division in Staphylococcus aureus.\",\"volume\":\"78\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:24:09.578744+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "01b319fc1f34daeda156e8cfc7e6f4bb541e8c4bcb4a73e8f3c4f78c8d2c62d2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H3KA40?format=txt&versions=36)

```json
{
  "entry_version": 36,
  "evidence_id": "H1",
  "excerpt": "ID   LYRA_STAAE              Reviewed;         419 AA.\nAC   A0A0H3KA40;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   16-SEP-2015, sequence version 1.\nDT   28-JAN-2026, entry version 36.\nDE   RecName: Full=Lysostaphin resistance protein A;\nDE   AltName: Full=Abortive infectivity domain-containing protein {ECO:0000303|PubMed:20923422};\nDE   AltName: Full=Surface protein display C {ECO:0000303|PubMed:20923422};\nGN   Name=lyrA {ECO:0000250|UniProtKB:Q2FVT1};\nGN   Synonyms=spdC {ECO:0000303|PubMed:33593946};\nGN   OrderedLocusNames=NWMN_2236 {ECO:0000312|EMBL:BAF68508.1};\nOS   Staphylococcus aureus (strain Newman).\nOC   Bacteria; Bacillati; Bacillota; Bacilli; Bacillales; Staphylococcaceae;\nOC   Staphylococcus.\nOX   NCBI_TaxID=426430 {ECO:0000312|Proteomes:UP000006386};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:11.851883+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d02c88a1544f67f6b8c7af47b40f478812539c62fe01fc0b43e7958088f0d2ff",
  "url": "https://rest.uniprot.org/unisave/A0A0H3KA40?format=txt&versions=36"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H3KA40?format=txt&versions=36)

```json
{
  "entry_version": 36,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, AND SUBCELLULAR LOCATION.\nRX   PubMed=20923422; DOI=10.1111/j.1365-2958.2010.07334.x;\nRA   Frankel M.B., Wojcik B.M., DeDent A.C., Missiakas D.M., Schneewind O.;\nRT   \"ABI domain-containing proteins contribute to surface protein display and\nRT   cell division in Staphylococcus aureus.\";\nRL   Mol. Microbiol. 78:238-252(2010).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:11.851883+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 25-31",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d02c88a1544f67f6b8c7af47b40f478812539c62fe01fc0b43e7958088f0d2ff",
  "url": "https://rest.uniprot.org/unisave/A0A0H3KA40?format=txt&versions=36"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H3KA40?format=txt&versions=36)

```json
{
  "entry_version": 36,
  "evidence_id": "H3",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, INTERACTION WITH SAGB, AND MUTAGENESIS OF GLU-135; ARG-139;\nRP   ARG-196 AND HIS-210.\nRX   PubMed=33593946; DOI=10.1128/jb.00014-21;\nRA   Willing S., Schneewind O., Missiakas D.;\nRT   \"Regulated cleavage of glycan strands by the murein hydrolase SagB in S.\nRT   aureus involves a direct interaction with LyrA (SpdC).\";\nRL   J. Bacteriol. 203:0-0(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:11.851883+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 32-39",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d02c88a1544f67f6b8c7af47b40f478812539c62fe01fc0b43e7958088f0d2ff",
  "url": "https://rest.uniprot.org/unisave/A0A0H3KA40?format=txt&versions=36"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H3KA40?format=txt&versions=36)

```json
{
  "entry_version": 36,
  "evidence_id": "H4",
  "excerpt": "FT   TRANSMEM        9..29\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:11.851883+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 96-98",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d02c88a1544f67f6b8c7af47b40f478812539c62fe01fc0b43e7958088f0d2ff",
  "url": "https://rest.uniprot.org/unisave/A0A0H3KA40?format=txt&versions=36"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H3KA40?format=txt&versions=36)

```json
{
  "entry_version": 36,
  "evidence_id": "H5",
  "excerpt": "FT   TRANSMEM        41..61\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:11.851883+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 99-101",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d02c88a1544f67f6b8c7af47b40f478812539c62fe01fc0b43e7958088f0d2ff",
  "url": "https://rest.uniprot.org/unisave/A0A0H3KA40?format=txt&versions=36"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H3KA40?format=txt&versions=36)

```json
{
  "entry_version": 36,
  "evidence_id": "H6",
  "excerpt": "FT   TRANSMEM        84..104\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:11.851883+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 102-104",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d02c88a1544f67f6b8c7af47b40f478812539c62fe01fc0b43e7958088f0d2ff",
  "url": "https://rest.uniprot.org/unisave/A0A0H3KA40?format=txt&versions=36"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H3KA40?format=txt&versions=36)

```json
{
  "entry_version": 36,
  "evidence_id": "H7",
  "excerpt": "FT   TRANSMEM        118..138\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:11.851883+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 105-107",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d02c88a1544f67f6b8c7af47b40f478812539c62fe01fc0b43e7958088f0d2ff",
  "url": "https://rest.uniprot.org/unisave/A0A0H3KA40?format=txt&versions=36"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H3KA40?format=txt&versions=36)

```json
{
  "entry_version": 36,
  "evidence_id": "H8",
  "excerpt": "FT   TRANSMEM        153..173\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:11.851883+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 108-110",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d02c88a1544f67f6b8c7af47b40f478812539c62fe01fc0b43e7958088f0d2ff",
  "url": "https://rest.uniprot.org/unisave/A0A0H3KA40?format=txt&versions=36"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H3KA40?format=txt&versions=36)

```json
{
  "entry_version": 36,
  "evidence_id": "H9",
  "excerpt": "FT   TRANSMEM        175..195\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:11.851883+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 111-113",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d02c88a1544f67f6b8c7af47b40f478812539c62fe01fc0b43e7958088f0d2ff",
  "url": "https://rest.uniprot.org/unisave/A0A0H3KA40?format=txt&versions=36"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H3KA40?format=txt&versions=36)

```json
{
  "entry_version": 36,
  "evidence_id": "H10",
  "excerpt": "FT   TRANSMEM        202..222\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:11.851883+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 114-116",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d02c88a1544f67f6b8c7af47b40f478812539c62fe01fc0b43e7958088f0d2ff",
  "url": "https://rest.uniprot.org/unisave/A0A0H3KA40?format=txt&versions=36"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H3KA40?format=txt&versions=36)

```json
{
  "entry_version": 36,
  "evidence_id": "H11",
  "excerpt": "FT   TRANSMEM        231..251\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:11.851883+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 117-119",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d02c88a1544f67f6b8c7af47b40f478812539c62fe01fc0b43e7958088f0d2ff",
  "url": "https://rest.uniprot.org/unisave/A0A0H3KA40?format=txt&versions=36"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 5. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
