# transmembrane_0079

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0079.txt)

**Task:** `transmembrane`  
**Expected answer:** **D** — 3..23; 301..321

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MWSLIPLTAIVLVLVAILHRLFFHPLSHVPGPFLARFSSLYLHSICYLGIEATVLRQLHIKYKTKVLRVAPNSVSISDSEAVGEIYVRGGGFPKDDRYKNFNLGPIVSIFSSLDREYRDVRAKAVAPLFSPAQLRAESGPQGVIGGCIAEFVDQLRKSKEAGIGADLMDMCARLSIDVVTGYLLGQKYGGLQENAHLPPQERQSHKLSANPFIFSIVAFSRFSLLPHRIFQFLYSTSQRLSTNDEVTESFLKLDRFTNNVLEGTTAGEKVSEKPNGGYYHERLISQAGISRMEAAAQSQAVLFAGADSTAVMLATILFHLVQNGAARSRLLCEVRSDKPQDMRFLRAVVKEGLRLGMANPTRMTRVVPKSGPGLRVGDVLLSPGTIVGCAAYNLHHDPEVFPDPFTFRPERWLDDGTDRGLRRPGMEKSMIPFGVGSRACIGKNLAQQQLHDTVVAVIDSEVLEGARTCQERIEIIEWFNADIKGHHLDIKWS

[Multiple Choices]
A. 310..337
B. 3..23
C. 6..26
D. 3..23; 301..321
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

> The exact-matching UniProt sequence has annotations for both 3..23 and 301..321 as helical transmembrane regions, supporting D. These annotations are computational (ECO:0000255), not experimental confirmation that both regions cross a membrane.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a strongly hydrophobic N-terminal stretch consistent with a membrane anchor, and another substantial hydrophobic stretch around 301..321. The latter is a better sequence-based candidate than 310..337, which extends beyond that hydrophobic stretch. This gives a transferable, probabilistic reason to favor D over choices describing only the N-terminal region or the shifted longer interval.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Both candidate regions can be identified from the supplied sequence and general knowledge of hydrophobic membrane-spanning helices. The second region is less decisive than the N-terminal anchor, so this supports a prediction rather than proving the exact boundaries or membrane topology.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The hydrophobic pattern provides a meaningful basis for preferring the two-region choice, although exact transmembrane boundaries and whether the second hydrophobic segment truly spans a membrane remain uncertain.


### Important caveats

- The cited database annotations are computational and do not independently establish experimental membrane insertion.
- A hydrophobic segment can occur within a folded protein without spanning a membrane; the second region is therefore less certain than the N-terminal anchor.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a strongly hydrophobic N-terminal stretch consistent with a membrane anchor, and another substantial hydrophobic stretch around 301..321. The latter is a better sequence-based candidate than 310..337, which extends beyond that hydrophobic stretch. This gives a transferable, probabilistic reason to favor D over choices describing only the N-terminal region or the shifted longer interval.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Both candidate regions can be identified from the supplied sequence and general knowledge of hydrophobic membrane-spanning helices. The second region is less decisive than the N-terminal anchor, so this supports a prediction rather than proving the exact boundaries or membrane topology."
  },
  "case_id": "transmembrane_0079",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H4",
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The exact-matching UniProt sequence has annotations for both 3..23 and 301..321 as helical transmembrane regions, supporting D. These annotations are computational (ECO:0000255), not experimental confirmation that both regions cross a membrane."
  },
  "important_caveats": [
    "The cited database annotations are computational and do not independently establish experimental membrane insertion.",
    "A hydrophobic segment can occur within a folded protein without spanning a membrane; the second region is therefore less certain than the N-terminal anchor."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The hydrophobic pattern provides a meaningful basis for preferring the two-region choice, although exact transmembrane boundaries and whether the second hydrophobic segment truly spans a membrane remain uncertain."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0079",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact-matching UniProt sequence has annotations for both 3..23 and 301..321 as helical transmembrane regions, supporting D. These annotations are computational (ECO:0000255), not experimental confirmation that both regions cross a membrane.",
    "evidence_ids": ["H3", "H4", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a strongly hydrophobic N-terminal stretch consistent with a membrane anchor, and another substantial hydrophobic stretch around 301..321. The latter is a better sequence-based candidate than 310..337, which extends beyond that hydrophobic stretch. This gives a transferable, probabilistic reason to favor D over choices describing only the N-terminal region or the shifted longer interval.",
    "missing_item_specific_fact": "",
    "reason": "Both candidate regions can be identified from the supplied sequence and general knowledge of hydrophobic membrane-spanning helices. The second region is less decisive than the N-terminal anchor, so this supports a prediction rather than proving the exact boundaries or membrane topology."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The hydrophobic pattern provides a meaningful basis for preferring the two-region choice, although exact transmembrane boundaries and whether the second hydrophobic segment truly spans a membrane remain uncertain."
  },
  "important_caveats": [
    "The cited database annotations are computational and do not independently establish experimental membrane insertion.",
    "A hydrophobic segment can occur within a folded protein without spanning a membrane; the second region is therefore less certain than the N-terminal anchor."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry P9WEG5 annotates two transmembrane helical regions: 3..23 (C5/H3) and 301..321 (C6/H4), matching option D exactly. Both annotations carry evidence code ECO:0000255 (inferred by similarity), indicating computational/transfer predictions rather than direct experimental measurements, but they are the canonical UniProt annotations. Sequence inspection confirms hydrophobic character at both positions: 3-23 (SLIPLTAIVLVLVAILHRLFF, strongly hydrophobic) and 301-321 (VLFAGADSTAVMLATILFHLV, moderately hydrophobic).

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a P450 heme-binding signature (FxxGxxxCxG around positions 433-442: FGVGSRACIG), identifying this as a cytochrome P450 monooxygenase. Fungal P450s commonly carry one or more N-terminal transmembrane anchors, a well-known family feature. The N-terminal stretch at positions 3-23 (SLIPLTAIVLVLVAILHRLFF) is a strongly hydrophobic ~21-residue segment, unambiguously a TM helix candidate. A second moderately hydrophobic stretch exists at 301-321 (VLFAGADSTAVMLATILFHLV), which, while less hydrophobic than the N-terminal region (interrupted by D, S, T, H), still has a positive average hydrophobicity and falls within the 18-25 residue length range typical of TM helices. A model performing sliding-window hydrophobicity analysis would flag both stretches. Option A (310..337) is readily excluded because it quickly becomes polar/charged (Q, N, G, R, S, E, D). Option C (6..26) is a minor shift of B and can be distinguished by noting the hydrophobic core is better defined starting at residue 3. The key B-vs-D distinction requires recognizing the second hydrophobic stretch; while the second TM is somewhat unusual for P450s (most have only N-terminal anchors), additional TM regions in the P450 fold are documented in the family, and the sequence evidence supports it. The task instruction to 'predict a region of the protein that spans across a cell membrane' in the context of a TM-prediction benchmark conventionally means identifying all TM helices, favoring D over B.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Both TM regions are identifiable from sequence hydrophobicity analysis combined with P450 family knowledge. The N-terminal TM is unambiguous. The second TM at 301-321 is moderately hydrophobic and detectable by standard sliding-window analysis, though it is less obvious than the first. Family-level knowledge of fungal P450 membrane anchoring supports the presence of multiple TM regions. A knowledgeable model could reasonably arrive at D through sequence analysis and family context, though the second TM is marginal.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> The question stem says 'a segment that crosses the membrane' (singular), which could be read as asking for one TM region, making B (3..23) a defensible answer. However, in the context of a TM-prediction benchmark, the convention is to identify all TM helices, favoring D. The second TM region (301-321) is moderately hydrophobic and somewhat unusual for a P450, so a model might reasonably omit it and select B. The distinction between B and D is not trivially clear from sequence alone.


### Important caveats

- Both UniProt TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred from related proteins, not experimentally validated measurements.
- The second TM region (301-321) has moderate hydrophobicity with several polar/charged interruptions (D, S, T, H); it is a borderline TM helix candidate. Standard TM predictors might or might not call it.
- The question stem uses singular 'a segment' while option D provides two segments, creating interpretive ambiguity between selecting one TM (B) versus all TMs (D).
- The protein identity (fungal P450) was not given to the evaluated model; it must be inferred from sequence features such as the P450 heme-binding motif.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a P450 heme-binding signature (FxxGxxxCxG around positions 433-442: FGVGSRACIG), identifying this as a cytochrome P450 monooxygenase. Fungal P450s commonly carry one or more N-terminal transmembrane anchors, a well-known family feature. The N-terminal stretch at positions 3-23 (SLIPLTAIVLVLVAILHRLFF) is a strongly hydrophobic ~21-residue segment, unambiguously a TM helix candidate. A second moderately hydrophobic stretch exists at 301-321 (VLFAGADSTAVMLATILFHLV), which, while less hydrophobic than the N-terminal region (interrupted by D, S, T, H), still has a positive average hydrophobicity and falls within the 18-25 residue length range typical of TM helices. A model performing sliding-window hydrophobicity analysis would flag both stretches. Option A (310..337) is readily excluded because it quickly becomes polar/charged (Q, N, G, R, S, E, D). Option C (6..26) is a minor shift of B and can be distinguished by noting the hydrophobic core is better defined starting at residue 3. The key B-vs-D distinction requires recognizing the second hydrophobic stretch; while the second TM is somewhat unusual for P450s (most have only N-terminal anchors), additional TM regions in the P450 fold are documented in the family, and the sequence evidence supports it. The task instruction to 'predict a region of the protein that spans across a cell membrane' in the context of a TM-prediction benchmark conventionally means identifying all TM helices, favoring D over B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Both TM regions are identifiable from sequence hydrophobicity analysis combined with P450 family knowledge. The N-terminal TM is unambiguous. The second TM at 301-321 is moderately hydrophobic and detectable by standard sliding-window analysis, though it is less obvious than the first. Family-level knowledge of fungal P450 membrane anchoring supports the presence of multiple TM regions. A knowledgeable model could reasonably arrive at D through sequence analysis and family context, though the second TM is marginal."
  },
  "case_id": "transmembrane_0079",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry P9WEG5 annotates two transmembrane helical regions: 3..23 (C5/H3) and 301..321 (C6/H4), matching option D exactly. Both annotations carry evidence code ECO:0000255 (inferred by similarity), indicating computational/transfer predictions rather than direct experimental measurements, but they are the canonical UniProt annotations. Sequence inspection confirms hydrophobic character at both positions: 3-23 (SLIPLTAIVLVLVAILHRLFF, strongly hydrophobic) and 301-321 (VLFAGADSTAVMLATILFHLV, moderately hydrophobic)."
  },
  "important_caveats": [
    "Both UniProt TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred from related proteins, not experimentally validated measurements.",
    "The second TM region (301-321) has moderate hydrophobicity with several polar/charged interruptions (D, S, T, H); it is a borderline TM helix candidate. Standard TM predictors might or might not call it.",
    "The question stem uses singular 'a segment' while option D provides two segments, creating interpretive ambiguity between selecting one TM (B) versus all TMs (D).",
    "The protein identity (fungal P450) was not given to the evaluated model; it must be inferred from sequence features such as the P450 heme-binding motif."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "The question stem says 'a segment that crosses the membrane' (singular), which could be read as asking for one TM region, making B (3..23) a defensible answer. However, in the context of a TM-prediction benchmark, the convention is to identify all TM helices, favoring D. The second TM region (301-321) is moderately hydrophobic and somewhat unusual for a P450, so a model might reasonably omit it and select B. The distinction between B and D is not trivially clear from sequence alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0079",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry P9WEG5 annotates two transmembrane helical regions: 3..23 (C5/H3) and 301..321 (C6/H4), matching option D exactly. Both annotations carry evidence code ECO:0000255 (inferred by similarity), indicating computational/transfer predictions rather than direct experimental measurements, but they are the canonical UniProt annotations. Sequence inspection confirms hydrophobic character at both positions: 3-23 (SLIPLTAIVLVLVAILHRLFF, strongly hydrophobic) and 301-321 (VLFAGADSTAVMLATILFHLV, moderately hydrophobic).",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a P450 heme-binding signature (FxxGxxxCxG around positions 433-442: FGVGSRACIG), identifying this as a cytochrome P450 monooxygenase. Fungal P450s commonly carry one or more N-terminal transmembrane anchors, a well-known family feature. The N-terminal stretch at positions 3-23 (SLIPLTAIVLVLVAILHRLFF) is a strongly hydrophobic ~21-residue segment, unambiguously a TM helix candidate. A second moderately hydrophobic stretch exists at 301-321 (VLFAGADSTAVMLATILFHLV), which, while less hydrophobic than the N-terminal region (interrupted by D, S, T, H), still has a positive average hydrophobicity and falls within the 18-25 residue length range typical of TM helices. A model performing sliding-window hydrophobicity analysis would flag both stretches. Option A (310..337) is readily excluded because it quickly becomes polar/charged (Q, N, G, R, S, E, D). Option C (6..26) is a minor shift of B and can be distinguished by noting the hydrophobic core is better defined starting at residue 3. The key B-vs-D distinction requires recognizing the second hydrophobic stretch; while the second TM is somewhat unusual for P450s (most have only N-terminal anchors), additional TM regions in the P450 fold are documented in the family, and the sequence evidence supports it. The task instruction to 'predict a region of the protein that spans across a cell membrane' in the context of a TM-prediction benchmark conventionally means identifying all TM helices, favoring D over B.",
    "missing_item_specific_fact": "",
    "reason": "Both TM regions are identifiable from sequence hydrophobicity analysis combined with P450 family knowledge. The N-terminal TM is unambiguous. The second TM at 301-321 is moderately hydrophobic and detectable by standard sliding-window analysis, though it is less obvious than the first. Family-level knowledge of fungal P450 membrane anchoring supports the presence of multiple TM regions. A knowledgeable model could reasonably arrive at D through sequence analysis and family context, though the second TM is marginal."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "The question stem says 'a segment that crosses the membrane' (singular), which could be read as asking for one TM region, making B (3..23) a defensible answer. However, in the context of a TM-prediction benchmark, the convention is to identify all TM helices, favoring D. The second TM region (301-321) is moderately hydrophobic and somewhat unusual for a P450, so a model might reasonably omit it and select B. The distinction between B and D is not trivially clear from sequence alone."
  },
  "important_caveats": [
    "Both UniProt TM annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred from related proteins, not experimentally validated measurements.",
    "The second TM region (301-321) has moderate hydrophobicity with several polar/charged interruptions (D, S, T, H); it is a borderline TM helix candidate. Standard TM predictors might or might not call it.",
    "The question stem uses singular 'a segment' while option D provides two segments, creating interpretive ambiguity between selecting one TM (B) versus all TMs (D).",
    "The protein identity (fungal P450) was not given to the evaluated model; it must be inferred from sequence features such as the P450 heme-binding motif."
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
  "benchmark_sequence_length": 493,
  "benchmark_sequence_sha256": "5f1ec0eac26ac312febaccb3855fd0772573fc6cede2b531165b6dbd6fc868e2",
  "current_entry_audit": {
    "entryVersion": 5,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-04-09",
    "sequenceVersion": 1
  },
  "current_record_sha256": "dc436df1e2d7691051ca6db34af02a9dec343983045b05a1d392790fcfc89365",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 493,
  "current_source_sequence_sha256": "5f1ec0eac26ac312febaccb3855fd0772573fc6cede2b531165b6dbd6fc868e2",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 3,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "P9WEG5",
  "selected_historical_entry_version": 3,
  "selected_historical_record_sha256": "af7833e0b12ec6f8aaae74c43fcace02a7efebe1a9b79c53957e96e46119ec32",
  "selected_historical_source_sequence_length": 493,
  "selected_historical_source_sequence_sha256": "5f1ec0eac26ac312febaccb3855fd0772573fc6cede2b531165b6dbd6fc868e2",
  "selected_historical_version": {
    "accession": "P9WEG5",
    "database": "Swiss-Prot",
    "entryVersion": 3,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MFMF_ANNMO",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG5.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P9WEG5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:30:16.026791+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dc436df1e2d7691051ca6db34af02a9dec343983045b05a1d392790fcfc89365",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG5.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG5.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":5,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-04-09\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:30:16.026791+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dc436df1e2d7691051ca6db34af02a9dec343983045b05a1d392790fcfc89365",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG5.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG5.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Filamentous fungus\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Xylariomycetidae\",\"Xylariales\",\"Hypoxylaceae\",\"Annulohypoxylon\"],\"scientificName\":\"Annulohypoxylon moriforme\",\"synonyms\":[\"Hypoxylon moriforme\"],\"taxonId\":326622}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:30:16.026791+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dc436df1e2d7691051ca6db34af02a9dec343983045b05a1d392790fcfc89365",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG5.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG5.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38404388\",\"source\":\"PubMed\"}],\"value\":\"11'-O-desmethylfendlerol biosynthesis cluster protein F\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38404388\",\"source\":\"PubMed\"}],\"value\":\"1.-.-.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38404388\",\"source\":\"PubMed\"}],\"value\":\"Cytochrome P450 monooxygenase mfmF\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:30:16.026791+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dc436df1e2d7691051ca6db34af02a9dec343983045b05a1d392790fcfc89365",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG5.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG5.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":23},\"start\":{\"modifier\":\"EXACT\",\"value\":3}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:30:16.026791+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dc436df1e2d7691051ca6db34af02a9dec343983045b05a1d392790fcfc89365",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG5.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG5.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":321},\"start\":{\"modifier\":\"EXACT\",\"value\":301}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:30:16.026791+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dc436df1e2d7691051ca6db34af02a9dec343983045b05a1d392790fcfc89365",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG5.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEG5.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Yan D.\",\"Matsuda Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38404388\"},{\"database\":\"DOI\",\"id\":\"10.1039/d3sc06001b\"}],\"citationType\":\"journal article\",\"firstPage\":\"3011\",\"id\":\"38404388\",\"journal\":\"Chem. Sci.\",\"lastPage\":\"3017\",\"publicationDate\":\"2024\",\"title\":\"Global genome mining-driven discovery of an unusual biosynthetic logic for fungal polyketide-terpenoid hybrids.\",\"volume\":\"15\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"CBS 123579\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:30:16.026791+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dc436df1e2d7691051ca6db34af02a9dec343983045b05a1d392790fcfc89365",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEG5.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEG5?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H1",
  "excerpt": "ID   MFMF_ANNMO              Reviewed;         493 AA.\nAC   P9WEG5;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   09-APR-2025, sequence version 1.\nDT   28-JAN-2026, entry version 3.\nDE   RecName: Full=Cytochrome P450 monooxygenase mfmF {ECO:0000303|PubMed:38404388};\nDE            EC=1.-.-.- {ECO:0000269|PubMed:38404388};\nDE   AltName: Full=11'-O-desmethylfendlerol biosynthesis cluster protein F {ECO:0000303|PubMed:38404388};\nGN   Name=mfmF {ECO:0000303|PubMed:38404388}; ORFNames=F4805DRAFT_472414;\nOS   Annulohypoxylon moriforme (Filamentous fungus) (Hypoxylon moriforme).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Xylariomycetidae; Xylariales; Hypoxylaceae; Annulohypoxylon.\nOX   NCBI_TaxID=326622;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:25.029219+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "af7833e0b12ec6f8aaae74c43fcace02a7efebe1a9b79c53957e96e46119ec32",
  "url": "https://rest.uniprot.org/unisave/P9WEG5?format=txt&versions=3"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEG5?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND PATHWAY.\nRC   STRAIN=CBS 123579;\nRX   PubMed=38404388; DOI=10.1039/d3sc06001b;\nRA   Yan D., Matsuda Y.;\nRT   \"Global genome mining-driven discovery of an unusual biosynthetic logic for\nRT   fungal polyketide-terpenoid hybrids.\";\nRL   Chem. Sci. 15:3011-3017(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:25.029219+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 28-35",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "af7833e0b12ec6f8aaae74c43fcace02a7efebe1a9b79c53957e96e46119ec32",
  "url": "https://rest.uniprot.org/unisave/P9WEG5?format=txt&versions=3"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEG5?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H3",
  "excerpt": "FT   TRANSMEM        3..23\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:25.029219+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 95-97",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "af7833e0b12ec6f8aaae74c43fcace02a7efebe1a9b79c53957e96e46119ec32",
  "url": "https://rest.uniprot.org/unisave/P9WEG5?format=txt&versions=3"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEG5?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H4",
  "excerpt": "FT   TRANSMEM        301..321\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:25.029219+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 98-100",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "af7833e0b12ec6f8aaae74c43fcace02a7efebe1a9b79c53957e96e46119ec32",
  "url": "https://rest.uniprot.org/unisave/P9WEG5?format=txt&versions=3"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 79. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
