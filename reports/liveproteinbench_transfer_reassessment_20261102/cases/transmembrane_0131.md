# transmembrane_0131

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0131.txt)

**Task:** `transmembrane`  
**Expected answer:** **D** — 179..199; 357..377

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSNSPPSSSSSGKGLSIPRKLALNAINEIQNRSNDYLLSKRGGKGLEEGRKRAALAAVISTVSSVGADRLTKADFDELRDLSEQESHDKVHFMDKLTNKLLDAIPRRSDESMDELRKRLEDRHRVEQPGLSIKRISRNFKTLSSKMDLVFSLQYSIIHVISWDKPSLTLTFLILYTWGCLMPYLFLVYPVFYVLTGVLIPNYLYRHPLAKPDIIPTRARGDSSIFGFLRTENAWELDRQRILLERSRTLERILSQELELSTISSRTSTDSEDEGSSSLFYEVFTADSKSNLVFKAVLEEDEETTEKGRTGVVDKVKLLINMRDLQNLTSDIIKMMTRMQDSIYENYSFKDEKRSTKHFFNLIALILITIVLGPYIPWRAIFIITVWVLILLKHPNRQHILKQLKPATKHKLPPKHRTEVKRRASRLGELIVDDPPQYRTIQIYQIEKQDLIKPSVYELYMYSSSIFNESDTLRIQKKDPRGLPISHWCKLPAQAGNSRKRIGQWTPIRDPGASKTVSWMRWRLTESGHMTSPASIVVAVLCVRLSDTAGHQKSDRGSTMIPEPVRRKAV

[Multiple Choices]
A. 179..199; 360..375
B. 357..377
C. 734..754; 807..827; 833..853; 1286..1306
D. 179..199; 357..377
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

> The supplied sequence has two strong hydrophobic stretches matching the keyed regions, and the sequence-matched UniProt record annotates both as helical transmembrane regions. These annotations carry computational evidence code ECO:0000255, so they support the answer but are not evidence of direct experimental measurement.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains two conspicuously hydrophobic stretches, one around 179–199 and another around 357–377, consistent with membrane-spanning alpha helices. Their positions distinguish D, which gives both full stretches, from B, which gives only the latter; A gives a shortened interval within the latter stretch, and C gives coordinates beyond this sequence.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and transferable knowledge that long hydrophobic stretches commonly form membrane-spanning helices provide a meaningful basis for selecting D without knowing this protein's exact database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> D gives both full hydrophobic regions. A's second interval overlaps the hydrophobic stretch but omits its ends, so it is not an equally good identification of the region's start and end.


### Important caveats

- The supporting database annotations are computational, not reported here as experimentally established.
- The sequence-matched source evidence is reviewer-only and was not part of the original input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains two conspicuously hydrophobic stretches, one around 179–199 and another around 357–377, consistent with membrane-spanning alpha helices. Their positions distinguish D, which gives both full stretches, from B, which gives only the latter; A gives a shortened interval within the latter stretch, and C gives coordinates beyond this sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and transferable knowledge that long hydrophobic stretches commonly form membrane-spanning helices provide a meaningful basis for selecting D without knowing this protein's exact database annotation."
  },
  "case_id": "transmembrane_0131",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence has two strong hydrophobic stretches matching the keyed regions, and the sequence-matched UniProt record annotates both as helical transmembrane regions. These annotations carry computational evidence code ECO:0000255, so they support the answer but are not evidence of direct experimental measurement."
  },
  "important_caveats": [
    "The supporting database annotations are computational, not reported here as experimentally established.",
    "The sequence-matched source evidence is reviewer-only and was not part of the original input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D gives both full hydrophobic regions. A's second interval overlaps the hydrophobic stretch but omits its ends, so it is not an equally good identification of the region's start and end."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0131",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence has two strong hydrophobic stretches matching the keyed regions, and the sequence-matched UniProt record annotates both as helical transmembrane regions. These annotations carry computational evidence code ECO:0000255, so they support the answer but are not evidence of direct experimental measurement.",
    "evidence_ids": ["C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains two conspicuously hydrophobic stretches, one around 179–199 and another around 357–377, consistent with membrane-spanning alpha helices. Their positions distinguish D, which gives both full stretches, from B, which gives only the latter; A gives a shortened interval within the latter stretch, and C gives coordinates beyond this sequence.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and transferable knowledge that long hydrophobic stretches commonly form membrane-spanning helices provide a meaningful basis for selecting D without knowing this protein's exact database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D gives both full hydrophobic regions. A's second interval overlaps the hydrophobic stretch but omits its ends, so it is not an equally good identification of the region's start and end."
  },
  "important_caveats": [
    "The supporting database annotations are computational, not reported here as experimentally established.",
    "The sequence-matched source evidence is reviewer-only and was not part of the original input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (W1QDU5, PEX24_OGAPD) annotates two transmembrane helices at exactly 179-199 and 357-377 (evidence IDs C5/C6, H3/H4). Both are flagged as 'Helical' with evidence code ECO:0000255 (inferred by sequence analysis/similarity), i.e., computational prediction rather than experimental determination. The sequence match is confirmed (569 AA, SHA-256 identical). The expected answer D (179..199; 357..377) matches the database annotation exactly.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Several transferable arguments distinguish D from the alternatives. (1) Option C lists positions 734-1306, far exceeding the 569-residue sequence length—immediately eliminable. (2) Scanning the sequence reveals two distinct hydrophobic stretches: one near residues 179-199 (CLMPYLFLVYPVFYVLTGVLIP—dense in Leu, Phe, Val, Tyr, Met, Ile) and another near 357-377 (HFFNLIALILITIVLGPYIPW—dense in Leu, Ile, Val, Phe). Option B captures only the second, missing the first, so it is eliminated. (3) Between A (360-375, 16 residues) and D (357-377, 21 residues): a 16-residue helix is borderline short for spanning a ~30 Å lipid bilayer (typically ≥18-20 hydrophobic residues needed); the first TM helix is 21 residues, suggesting a comparable length for the second. The residues HFF at 357-359 contain two phenylalanines (hydrophobic), and W377 is a classic membrane-interfacial aromatic residue commonly found at the lipid-water boundary of TM helices. Including these residues yields a more physically plausible 21-residue helix. A model trained on general TM-helix statistics (length ~20-25, aromatic residues at boundaries) would favor D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The question can be answered by identifying hydrophobic stretches in the provided sequence, applying general TM-helix length requirements (~20 residues), recognizing aromatic interfacial residues (Trp, Tyr, Phe), and eliminating impossible options (C exceeds sequence length; B misses a clear TM region). The A-vs-D distinction relies on helix-length plausibility and the presence of hydrophobic/interfacial residues at 357-359 and 376-377, all derivable from the sequence itself plus general membrane-protein biophysics.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option C is trivially wrong (positions beyond sequence). Option B misses an obvious TM region. The A-vs-D distinction, while subtle, favors D on helix-length grounds (16 vs 21 residues) and the presence of interfacial Trp at 377. No other option is defensible.


### Important caveats

- Both TM annotations carry evidence code ECO:0000255 (inferred by sequence analysis), meaning they are computational predictions, not experimentally validated topologies.
- The protein is PEX24 from Ogataea parapolymorpha, a peroxisomal membrane protein involved in ER-peroxisome tethering; the two TM helices are consistent with a small membrane-anchored protein.
- The A-vs-D boundary difference (360 vs 357 start, 375 vs 377 end) is within the typical ±2-3 residue uncertainty of computational TM predictors; however, the 16-residue option A is notably short for a bilayer-spanning helix.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Several transferable arguments distinguish D from the alternatives. (1) Option C lists positions 734-1306, far exceeding the 569-residue sequence length—immediately eliminable. (2) Scanning the sequence reveals two distinct hydrophobic stretches: one near residues 179-199 (CLMPYLFLVYPVFYVLTGVLIP—dense in Leu, Phe, Val, Tyr, Met, Ile) and another near 357-377 (HFFNLIALILITIVLGPYIPW—dense in Leu, Ile, Val, Phe). Option B captures only the second, missing the first, so it is eliminated. (3) Between A (360-375, 16 residues) and D (357-377, 21 residues): a 16-residue helix is borderline short for spanning a ~30 Å lipid bilayer (typically ≥18-20 hydrophobic residues needed); the first TM helix is 21 residues, suggesting a comparable length for the second. The residues HFF at 357-359 contain two phenylalanines (hydrophobic), and W377 is a classic membrane-interfacial aromatic residue commonly found at the lipid-water boundary of TM helices. Including these residues yields a more physically plausible 21-residue helix. A model trained on general TM-helix statistics (length ~20-25, aromatic residues at boundaries) would favor D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The question can be answered by identifying hydrophobic stretches in the provided sequence, applying general TM-helix length requirements (~20 residues), recognizing aromatic interfacial residues (Trp, Tyr, Phe), and eliminating impossible options (C exceeds sequence length; B misses a clear TM region). The A-vs-D distinction relies on helix-length plausibility and the presence of hydrophobic/interfacial residues at 357-359 and 376-377, all derivable from the sequence itself plus general membrane-protein biophysics."
  },
  "case_id": "transmembrane_0131",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (W1QDU5, PEX24_OGAPD) annotates two transmembrane helices at exactly 179-199 and 357-377 (evidence IDs C5/C6, H3/H4). Both are flagged as 'Helical' with evidence code ECO:0000255 (inferred by sequence analysis/similarity), i.e., computational prediction rather than experimental determination. The sequence match is confirmed (569 AA, SHA-256 identical). The expected answer D (179..199; 357..377) matches the database annotation exactly."
  },
  "important_caveats": [
    "Both TM annotations carry evidence code ECO:0000255 (inferred by sequence analysis), meaning they are computational predictions, not experimentally validated topologies.",
    "The protein is PEX24 from Ogataea parapolymorpha, a peroxisomal membrane protein involved in ER-peroxisome tethering; the two TM helices are consistent with a small membrane-anchored protein.",
    "The A-vs-D boundary difference (360 vs 357 start, 375 vs 377 end) is within the typical ±2-3 residue uncertainty of computational TM predictors; however, the 16-residue option A is notably short for a bilayer-spanning helix."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C is trivially wrong (positions beyond sequence). Option B misses an obvious TM region. The A-vs-D distinction, while subtle, favors D on helix-length grounds (16 vs 21 residues) and the presence of interfacial Trp at 377. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0131",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (W1QDU5, PEX24_OGAPD) annotates two transmembrane helices at exactly 179-199 and 357-377 (evidence IDs C5/C6, H3/H4). Both are flagged as 'Helical' with evidence code ECO:0000255 (inferred by sequence analysis/similarity), i.e., computational prediction rather than experimental determination. The sequence match is confirmed (569 AA, SHA-256 identical). The expected answer D (179..199; 357..377) matches the database annotation exactly.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Several transferable arguments distinguish D from the alternatives. (1) Option C lists positions 734-1306, far exceeding the 569-residue sequence length—immediately eliminable. (2) Scanning the sequence reveals two distinct hydrophobic stretches: one near residues 179-199 (CLMPYLFLVYPVFYVLTGVLIP—dense in Leu, Phe, Val, Tyr, Met, Ile) and another near 357-377 (HFFNLIALILITIVLGPYIPW—dense in Leu, Ile, Val, Phe). Option B captures only the second, missing the first, so it is eliminated. (3) Between A (360-375, 16 residues) and D (357-377, 21 residues): a 16-residue helix is borderline short for spanning a ~30 Å lipid bilayer (typically ≥18-20 hydrophobic residues needed); the first TM helix is 21 residues, suggesting a comparable length for the second. The residues HFF at 357-359 contain two phenylalanines (hydrophobic), and W377 is a classic membrane-interfacial aromatic residue commonly found at the lipid-water boundary of TM helices. Including these residues yields a more physically plausible 21-residue helix. A model trained on general TM-helix statistics (length ~20-25, aromatic residues at boundaries) would favor D.",
    "missing_item_specific_fact": "",
    "reason": "The question can be answered by identifying hydrophobic stretches in the provided sequence, applying general TM-helix length requirements (~20 residues), recognizing aromatic interfacial residues (Trp, Tyr, Phe), and eliminating impossible options (C exceeds sequence length; B misses a clear TM region). The A-vs-D distinction relies on helix-length plausibility and the presence of hydrophobic/interfacial residues at 357-359 and 376-377, all derivable from the sequence itself plus general membrane-protein biophysics."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C is trivially wrong (positions beyond sequence). Option B misses an obvious TM region. The A-vs-D distinction, while subtle, favors D on helix-length grounds (16 vs 21 residues) and the presence of interfacial Trp at 377. No other option is defensible."
  },
  "important_caveats": [
    "Both TM annotations carry evidence code ECO:0000255 (inferred by sequence analysis), meaning they are computational predictions, not experimentally validated topologies.",
    "The protein is PEX24 from Ogataea parapolymorpha, a peroxisomal membrane protein involved in ER-peroxisome tethering; the two TM helices are consistent with a small membrane-anchored protein.",
    "The A-vs-D boundary difference (360 vs 357 start, 375 vs 377 end) is within the typical ±2-3 residue uncertainty of computational TM predictors; however, the 16-residue option A is notably short for a bilayer-spanning helix."
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
  "benchmark_sequence_length": 569,
  "benchmark_sequence_sha256": "f07d5286e3331343754a8f9c72f442123b8ba918a4b647577c5e44137c6d2082",
  "current_entry_audit": {
    "entryVersion": 38,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2014-03-19",
    "sequenceVersion": 1
  },
  "current_record_sha256": "a935708ddec2d3b0ff86676a9c780f1b15c450d19ecc218103ca9285e46d273a",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 569,
  "current_source_sequence_sha256": "f07d5286e3331343754a8f9c72f442123b8ba918a4b647577c5e44137c6d2082",
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
  "requested_accession": "W1QDU5",
  "selected_historical_entry_version": 36,
  "selected_historical_record_sha256": "35693919ce4aaade7dbc7068810713aa80e421568f8ede865776b2f733bc2302",
  "selected_historical_source_sequence_length": 569,
  "selected_historical_source_sequence_sha256": "f07d5286e3331343754a8f9c72f442123b8ba918a4b647577c5e44137c6d2082",
  "selected_historical_version": {
    "accession": "W1QDU5",
    "database": "Swiss-Prot",
    "entryVersion": 36,
    "firstRelease": "2025_02/2025_02",
    "firstReleaseDate": "23-Apr-2025",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "PEX24_OGAPD",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QDU5.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"W1QDU5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:34:05.762905+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a935708ddec2d3b0ff86676a9c780f1b15c450d19ecc218103ca9285e46d273a",
  "url": "https://rest.uniprot.org/uniprotkb/W1QDU5.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QDU5.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":38,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2014-03-19\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:34:05.762905+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a935708ddec2d3b0ff86676a9c780f1b15c450d19ecc218103ca9285e46d273a",
  "url": "https://rest.uniprot.org/uniprotkb/W1QDU5.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QDU5.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Yeast\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Saccharomycotina\",\"Pichiomycetes\",\"Pichiales\",\"Pichiaceae\",\"Ogataea\"],\"scientificName\":\"Ogataea parapolymorpha (strain ATCC 26012 / BCRC 20466 / JCM 22074 / NRRL Y-7560 / DL-1)\",\"synonyms\":[\"Hansenula polymorpha\"],\"taxonId\":871575}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:34:05.762905+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a935708ddec2d3b0ff86676a9c780f1b15c450d19ecc218103ca9285e46d273a",
  "url": "https://rest.uniprot.org/uniprotkb/W1QDU5.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QDU5.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Peroxin-24\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32665322\",\"source\":\"PubMed\"}],\"value\":\"Peroxisomal membrane protein PEX24\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:34:05.762905+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a935708ddec2d3b0ff86676a9c780f1b15c450d19ecc218103ca9285e46d273a",
  "url": "https://rest.uniprot.org/uniprotkb/W1QDU5.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QDU5.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":199},\"start\":{\"modifier\":\"EXACT\",\"value\":179}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:34:05.762905+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a935708ddec2d3b0ff86676a9c780f1b15c450d19ecc218103ca9285e46d273a",
  "url": "https://rest.uniprot.org/uniprotkb/W1QDU5.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QDU5.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":377},\"start\":{\"modifier\":\"EXACT\",\"value\":357}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:34:05.762905+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a935708ddec2d3b0ff86676a9c780f1b15c450d19ecc218103ca9285e46d273a",
  "url": "https://rest.uniprot.org/uniprotkb/W1QDU5.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QDU5.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Wu F.\",\"de Boer R.\",\"Krikken A.M.\",\"Aksit A.\",\"Bordin N.\",\"Devos D.P.\",\"van der Klei I.J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"32665322\"},{\"database\":\"DOI\",\"id\":\"10.1242/jcs.246983\"}],\"citationType\":\"journal article\",\"firstPage\":\"0\",\"id\":\"32665322\",\"journal\":\"J. Cell Sci.\",\"lastPage\":\"0\",\"publicationDate\":\"2020\",\"title\":\"Pex24 and Pex32 are required to tether peroxisomes to the ER for organelle biogenesis, positioning and segregation in yeast.\",\"volume\":\"133\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:34:05.762905+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a935708ddec2d3b0ff86676a9c780f1b15c450d19ecc218103ca9285e46d273a",
  "url": "https://rest.uniprot.org/uniprotkb/W1QDU5.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QDU5?format=txt&versions=36)

```json
{
  "entry_version": 36,
  "evidence_id": "H1",
  "excerpt": "ID   PEX24_OGAPD             Reviewed;         569 AA.\nAC   W1QDU5;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   19-MAR-2014, sequence version 1.\nDT   09-APR-2025, entry version 36.\nDE   RecName: Full=Peroxisomal membrane protein PEX24 {ECO:0000303|PubMed:32665322};\nDE   AltName: Full=Peroxin-24 {ECO:0000305};\nGN   Name=PEX24 {ECO:0000303|PubMed:32665322}; ORFNames=HPODL_03516;\nOS   Ogataea parapolymorpha (strain ATCC 26012 / BCRC 20466 / JCM 22074 / NRRL\nOS   Y-7560 / DL-1) (Yeast) (Hansenula polymorpha).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Saccharomycotina; Pichiomycetes;\nOC   Pichiales; Pichiaceae; Ogataea.\nOX   NCBI_TaxID=871575;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:09.234705+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "35693919ce4aaade7dbc7068810713aa80e421568f8ede865776b2f733bc2302",
  "url": "https://rest.uniprot.org/unisave/W1QDU5?format=txt&versions=36"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QDU5?format=txt&versions=36)

```json
{
  "entry_version": 36,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, DISRUPTION PHENOTYPE, AND SUBCELLULAR LOCATION.\nRX   PubMed=32665322; DOI=10.1242/jcs.246983;\nRA   Wu F., de Boer R., Krikken A.M., Aksit A., Bordin N., Devos D.P.,\nRA   van der Klei I.J.;\nRT   \"Pex24 and Pex32 are required to tether peroxisomes to the ER for organelle\nRT   biogenesis, positioning and segregation in yeast.\";\nRL   J. Cell Sci. 133:0-0(2020).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:09.234705+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 24-31",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "35693919ce4aaade7dbc7068810713aa80e421568f8ede865776b2f733bc2302",
  "url": "https://rest.uniprot.org/unisave/W1QDU5?format=txt&versions=36"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QDU5?format=txt&versions=36)

```json
{
  "entry_version": 36,
  "evidence_id": "H3",
  "excerpt": "FT   TRANSMEM        179..199\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:09.234705+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 78-80",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "35693919ce4aaade7dbc7068810713aa80e421568f8ede865776b2f733bc2302",
  "url": "https://rest.uniprot.org/unisave/W1QDU5?format=txt&versions=36"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QDU5?format=txt&versions=36)

```json
{
  "entry_version": 36,
  "evidence_id": "H4",
  "excerpt": "FT   TRANSMEM        357..377\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:09.234705+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 81-83",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "35693919ce4aaade7dbc7068810713aa80e421568f8ede865776b2f733bc2302",
  "url": "https://rest.uniprot.org/unisave/W1QDU5?format=txt&versions=36"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 131. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
