# transmembrane_0000

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0000.txt)

**Task:** `transmembrane`  
**Expected answer:** **B** — 237..255; 289..311; 332..357; 363..382; 394..416; 436..455; 476..499; 530..546; 567..585; 597..615; 635..657; 663..684

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MHQDNSMRRAINQSRNGGSDSCDINNDREHDNINRNSYINNFHIENINSDKNEQSYIYCSDRAQVTDSILGNRKYTHEENINSTEMFSRTNYEYSNKNNVDIEMYNISNNNFYNGNNNGHSNDIIDYINNNNVNKDLSNTSNNADINTYIKKLTSNQSTAYCDGKGYNESANGSNFDINFRDVIKNNNNKNYKNNNHVPDDMLELGDRSFDSSFYIHNNVEEIDTERSNRLSFMSKLKMYFNYFGPGWIVAIAYLDPGNICGNLNVGLIRSDDFINVNSSVKDYTGYRLLWVLVYGHILGFIFHTLSMKLGHITGLDLAALCRKEFSSKFSYFLYICVQIAIWGAHLQAIIGVFVAINLILGIPVKIAILYTLIEAFAYSFLENKSLDLLEKVLSLLIGILVCCFMFNVFMTPINFQEVASSILYPRIPKGKLLDTMGLLGSVISAHIFYLHSNLTSKKKPVIYNDRMVKRYNKLGTIESGGSLLVSCITNCIIVLTFAEVNISGDDRKADYNLFNAYDVMKKYFGKTSMYIWSFGLLSSGNNASFMCEYASKSVFEGFLNKNVNPFFRVIFSRIILFIMLYAYVSYDKYTIDQLSNFINVVQILLLPLAIIPLYRFSIHKNVLGKFAIKGAFKYLVFVLVISIIVANFLLTLFDFLQYAPSNLYVIFIFISSIFYLLFIIYFFNMPITKTYYKDS

[Multiple Choices]
A. 298..318
B. 237..255; 289..311; 332..357; 363..382; 394..416; 436..455; 476..499; 530..546; 567..585; 597..615; 635..657; 663..684
C. 237..255; 289..311; 332..357; 363..382; 394..416; 437..458; 476..499; 530..546; 567..585; 597..615; 635..657; 663..684
D. 237..255; 289..311; 332..357; 363..382; 436..455; 476..499; 530..546; 567..585; 597..615; 635..657; 663..684
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

> The sequence-matched historical UniProt record lists the same 12 transmembrane intervals as choice B. These are computational helical annotations (ECO:0000255), not evidence that every boundary was experimentally measured.

Citations as saved: [H4](#evidence-h4), [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16), [H18](#evidence-h18), [H20](#evidence-h20), [H22](#evidence-h22), [H24](#evidence-h24), [H26](#evidence-h26).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a long polar, low-complexity N-terminal region followed by a densely hydrophobic C-terminal region with repeated stretches of helix-compatible hydrophobic residues, a recognizable pattern of a multi-pass membrane transporter. That pattern strongly favors the many-span alternatives B/C over A, and the strongly hydrophobic stretches and intervening polar or charged regions provide transferable sequence-based evidence for locating the spans. D also omits a plausible hydrophobic span around 394–416. B and C differ only in the boundary of the 436-region helix; hydropathy and the transition to the following loop can favor B, although this fine boundary is less certain from sequence alone.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can distinguish the multi-pass transporter pattern and use hydrophobicity transitions to compare the offered intervals without knowing this protein's database record. Exact transmembrane boundaries can be uncertain by a few residues, but the key distinction is not wholly dependent on an annotation specific to this protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The close boundary alternatives B and C make the 436-region endpoint less certain, but the sequence pattern and the surrounding polar/charged transition favor B; the supplied matched annotation also supports B.


### Important caveats

- The reviewer-only database annotations support the key but were not available as original model input.
- The cited transmembrane features are computationally annotated; the evidence does not establish experimental validation of each residue-level boundary.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a long polar, low-complexity N-terminal region followed by a densely hydrophobic C-terminal region with repeated stretches of helix-compatible hydrophobic residues, a recognizable pattern of a multi-pass membrane transporter. That pattern strongly favors the many-span alternatives B/C over A, and the strongly hydrophobic stretches and intervening polar or charged regions provide transferable sequence-based evidence for locating the spans. D also omits a plausible hydrophobic span around 394–416. B and C differ only in the boundary of the 436-region helix; hydropathy and the transition to the following loop can favor B, although this fine boundary is less certain from sequence alone.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can distinguish the multi-pass transporter pattern and use hydrophobicity transitions to compare the offered intervals without knowing this protein's database record. Exact transmembrane boundaries can be uncertain by a few residues, but the key distinction is not wholly dependent on an annotation specific to this protein."
  },
  "case_id": "transmembrane_0000",
  "expected_answer_check": {
    "evidence_ids": [
      "H4",
      "H6",
      "H8",
      "H10",
      "H12",
      "H14",
      "H16",
      "H18",
      "H20",
      "H22",
      "H24",
      "H26"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record lists the same 12 transmembrane intervals as choice B. These are computational helical annotations (ECO:0000255), not evidence that every boundary was experimentally measured."
  },
  "important_caveats": [
    "The reviewer-only database annotations support the key but were not available as original model input.",
    "The cited transmembrane features are computationally annotated; the evidence does not establish experimental validation of each residue-level boundary."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The close boundary alternatives B and C make the 436-region endpoint less certain, but the sequence pattern and the surrounding polar/charged transition favor B; the supplied matched annotation also supports B."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0000",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record lists the same 12 transmembrane intervals as choice B. These are computational helical annotations (ECO:0000255), not evidence that every boundary was experimentally measured.",
    "evidence_ids": ["H4", "H6", "H8", "H10", "H12", "H14", "H16", "H18", "H20", "H22", "H24", "H26"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a long polar, low-complexity N-terminal region followed by a densely hydrophobic C-terminal region with repeated stretches of helix-compatible hydrophobic residues, a recognizable pattern of a multi-pass membrane transporter. That pattern strongly favors the many-span alternatives B/C over A, and the strongly hydrophobic stretches and intervening polar or charged regions provide transferable sequence-based evidence for locating the spans. D also omits a plausible hydrophobic span around 394–416. B and C differ only in the boundary of the 436-region helix; hydropathy and the transition to the following loop can favor B, although this fine boundary is less certain from sequence alone.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can distinguish the multi-pass transporter pattern and use hydrophobicity transitions to compare the offered intervals without knowing this protein's database record. Exact transmembrane boundaries can be uncertain by a few residues, but the key distinction is not wholly dependent on an annotation specific to this protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The close boundary alternatives B and C make the 436-region endpoint less certain, but the sequence pattern and the surrounding polar/charged transition favor B; the supplied matched annotation also supports B."
  },
  "important_caveats": [
    "The reviewer-only database annotations support the key but were not available as original model input.",
    "The cited transmembrane features are computationally annotated; the evidence does not establish experimental validation of each residue-level boundary."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for A0A077Y877 (DMT1_PLAYE) lists exactly 12 transmembrane helical regions at the coordinates specified in option B: 237..255, 289..311, 332..357, 363..382, 394..416, 436..455, 476..499, 530..546, 567..585, 597..615, 635..657, 663..684. These match option B precisely. The evidence codes are ECO:0000255 (similarity), indicating computational inference by similarity to Q8I3M7 (P. falciparum FVRT1), not direct experimental determination. The sequence match is confirmed (SHA-256 identical).

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C20](#evidence-c20), [C22](#evidence-c22), [C24](#evidence-c24), [C26](#evidence-c26), [C28](#evidence-c28).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Recognizing the Nramp/DMT1 family (12 TM helices, alternating cytoplasmic/luminal topology) allows elimination of option A (single TM) and option D (11 TMs, missing the 394..416 region). However, distinguishing B from C requires resolving the boundary of the 6th TM helix: 436..455 (B) vs 437..458 (C). This is a 1-residue shift at the N-terminus and a 3-residue shift at the C-terminus. Both 20-residue and 22-residue helices are within normal TM length, and both maintain the same alternating topology. No family-level structural principle or hydrophobicity heuristic reliably resolves a 1–3 residue boundary difference without running a specific TM-prediction tool (e.g., TMHMM, Phobius) or consulting the exact annotation.


**Missing item-specific fact**

> The exact residue-level boundary of the 6th transmembrane helix (whether it spans 436..455 or 437..458), which is a target-specific annotation derived by similarity transfer from Q8I3M7 and not determinable from general Nramp family knowledge or simple hydrophobicity analysis.


**Reason**

> Family-level knowledge (Nramp = 12 TM domains, alternating topology) eliminates A and D but cannot distinguish B from C. The 1–3 residue boundary difference in one TM helix is within the noise of sequence-based prediction and requires the specific database annotation or a computational prediction tool result for this exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> Options B and C differ only in the 6th TM region boundary (436..455 vs 437..458). Both are plausible TM helix lengths (20 vs 22 residues), both preserve the correct 12-TM alternating topology, and neither boundary is clearly favored by general hydrophobicity reasoning without a specific prediction tool. A knowledgeable model without the exact annotation could reasonably select either.


### Important caveats

- All UniProt TM annotations for this entry use evidence code ECO:0000255 (similarity), meaning they are computationally inferred by transfer from Q8I3M7 (P. falciparum FVRT1), not experimentally validated for this specific sequence.
- The 1–3 residue boundary difference between B and C is within the typical uncertainty of TM prediction tools; even different tools (TMHMM, Phobius, DeepTMHMM) may disagree by 1–3 residues at helix boundaries.
- The N-terminal 236 residues are highly polar (abundant N, S, D, E, K, R, Q), making the onset of TM regions around position 237 unambiguous; the ambiguity is confined to one internal boundary.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Recognizing the Nramp/DMT1 family (12 TM helices, alternating cytoplasmic/luminal topology) allows elimination of option A (single TM) and option D (11 TMs, missing the 394..416 region). However, distinguishing B from C requires resolving the boundary of the 6th TM helix: 436..455 (B) vs 437..458 (C). This is a 1-residue shift at the N-terminus and a 3-residue shift at the C-terminus. Both 20-residue and 22-residue helices are within normal TM length, and both maintain the same alternating topology. No family-level structural principle or hydrophobicity heuristic reliably resolves a 1–3 residue boundary difference without running a specific TM-prediction tool (e.g., TMHMM, Phobius) or consulting the exact annotation.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact residue-level boundary of the 6th transmembrane helix (whether it spans 436..455 or 437..458), which is a target-specific annotation derived by similarity transfer from Q8I3M7 and not determinable from general Nramp family knowledge or simple hydrophobicity analysis.",
    "reason": "Family-level knowledge (Nramp = 12 TM domains, alternating topology) eliminates A and D but cannot distinguish B from C. The 1–3 residue boundary difference in one TM helix is within the noise of sequence-based prediction and requires the specific database annotation or a computational prediction tool result for this exact protein."
  },
  "case_id": "transmembrane_0000",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C8",
      "C10",
      "C12",
      "C14",
      "C16",
      "C18",
      "C20",
      "C22",
      "C24",
      "C26",
      "C28"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for A0A077Y877 (DMT1_PLAYE) lists exactly 12 transmembrane helical regions at the coordinates specified in option B: 237..255, 289..311, 332..357, 363..382, 394..416, 436..455, 476..499, 530..546, 567..585, 597..615, 635..657, 663..684. These match option B precisely. The evidence codes are ECO:0000255 (similarity), indicating computational inference by similarity to Q8I3M7 (P. falciparum FVRT1), not direct experimental determination. The sequence match is confirmed (SHA-256 identical)."
  },
  "important_caveats": [
    "All UniProt TM annotations for this entry use evidence code ECO:0000255 (similarity), meaning they are computationally inferred by transfer from Q8I3M7 (P. falciparum FVRT1), not experimentally validated for this specific sequence.",
    "The 1–3 residue boundary difference between B and C is within the typical uncertainty of TM prediction tools; even different tools (TMHMM, Phobius, DeepTMHMM) may disagree by 1–3 residues at helix boundaries.",
    "The N-terminal 236 residues are highly polar (abundant N, S, D, E, K, R, Q), making the onset of TM regions around position 237 unambiguous; the ambiguity is confined to one internal boundary."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "Options B and C differ only in the 6th TM region boundary (436..455 vs 437..458). Both are plausible TM helix lengths (20 vs 22 residues), both preserve the correct 12-TM alternating topology, and neither boundary is clearly favored by general hydrophobicity reasoning without a specific prediction tool. A knowledgeable model without the exact annotation could reasonably select either."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0000",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for A0A077Y877 (DMT1_PLAYE) lists exactly 12 transmembrane helical regions at the coordinates specified in option B: 237..255, 289..311, 332..357, 363..382, 394..416, 436..455, 476..499, 530..546, 567..585, 597..615, 635..657, 663..684. These match option B precisely. The evidence codes are ECO:0000255 (similarity), indicating computational inference by similarity to Q8I3M7 (P. falciparum FVRT1), not direct experimental determination. The sequence match is confirmed (SHA-256 identical).",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "C20", "C22", "C24", "C26", "C28"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Recognizing the Nramp/DMT1 family (12 TM helices, alternating cytoplasmic/luminal topology) allows elimination of option A (single TM) and option D (11 TMs, missing the 394..416 region). However, distinguishing B from C requires resolving the boundary of the 6th TM helix: 436..455 (B) vs 437..458 (C). This is a 1-residue shift at the N-terminus and a 3-residue shift at the C-terminus. Both 20-residue and 22-residue helices are within normal TM length, and both maintain the same alternating topology. No family-level structural principle or hydrophobicity heuristic reliably resolves a 1–3 residue boundary difference without running a specific TM-prediction tool (e.g., TMHMM, Phobius) or consulting the exact annotation.",
    "missing_item_specific_fact": "The exact residue-level boundary of the 6th transmembrane helix (whether it spans 436..455 or 437..458), which is a target-specific annotation derived by similarity transfer from Q8I3M7 and not determinable from general Nramp family knowledge or simple hydrophobicity analysis.",
    "reason": "Family-level knowledge (Nramp = 12 TM domains, alternating topology) eliminates A and D but cannot distinguish B from C. The 1–3 residue boundary difference in one TM helix is within the noise of sequence-based prediction and requires the specific database annotation or a computational prediction tool result for this exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "Options B and C differ only in the 6th TM region boundary (436..455 vs 437..458). Both are plausible TM helix lengths (20 vs 22 residues), both preserve the correct 12-TM alternating topology, and neither boundary is clearly favored by general hydrophobicity reasoning without a specific prediction tool. A knowledgeable model without the exact annotation could reasonably select either."
  },
  "important_caveats": [
    "All UniProt TM annotations for this entry use evidence code ECO:0000255 (similarity), meaning they are computationally inferred by transfer from Q8I3M7 (P. falciparum FVRT1), not experimentally validated for this specific sequence.",
    "The 1–3 residue boundary difference between B and C is within the typical uncertainty of TM prediction tools; even different tools (TMHMM, Phobius, DeepTMHMM) may disagree by 1–3 residues at helix boundaries.",
    "The N-terminal 236 residues are highly polar (abundant N, S, D, E, K, R, Q), making the onset of TM regions around position 237 unambiguous; the ambiguity is confined to one internal boundary."
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
  "benchmark_sequence_length": 696,
  "benchmark_sequence_sha256": "5ba561d59da02d1e0aa0316281aa8d6da8602c10efd3e007cc12440132bf882d",
  "current_entry_audit": {
    "entryVersion": 40,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2014-10-29",
    "sequenceVersion": 1
  },
  "current_record_sha256": "40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 696,
  "current_source_sequence_sha256": "5ba561d59da02d1e0aa0316281aa8d6da8602c10efd3e007cc12440132bf882d",
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
  "requested_accession": "A0A077Y877",
  "selected_historical_entry_version": 38,
  "selected_historical_record_sha256": "37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47",
  "selected_historical_source_sequence_length": 696,
  "selected_historical_source_sequence_sha256": "5ba561d59da02d1e0aa0316281aa8d6da8602c10efd3e007cc12440132bf882d",
  "selected_historical_version": {
    "accession": "A0A077Y877",
    "database": "Swiss-Prot",
    "entryVersion": 38,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DMT1_PLAYE",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A077Y877\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:23:53.473191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8",
  "url": "https://rest.uniprot.org/uniprotkb/A0A077Y877.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":40,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2014-10-29\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:23:53.473191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8",
  "url": "https://rest.uniprot.org/uniprotkb/A0A077Y877.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Aconoidasida\",\"Haemosporida\",\"Plasmodiidae\",\"Plasmodium\",\"Vinckeia\"],\"scientificName\":\"Plasmodium yoelii\",\"taxonId\":5861}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:23:53.473191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8",
  "url": "https://rest.uniprot.org/uniprotkb/A0A077Y877.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8I3M7\",\"source\":\"UniProtKB\"}],\"value\":\"Food vacuole resident transporter 1\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38049852\",\"source\":\"PubMed\"}],\"value\":\"Divalent metal transporter 1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38049852\",\"source\":\"PubMed\"}],\"value\":\"PyDMT1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:23:53.473191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8",
  "url": "https://rest.uniprot.org/uniprotkb/A0A077Y877.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":236},\"start\":{\"modifier\":\"EXACT\",\"value\":1}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:23:53.473191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8",
  "url": "https://rest.uniprot.org/uniprotkb/A0A077Y877.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":255},\"start\":{\"modifier\":\"EXACT\",\"value\":237}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:23:53.473191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8",
  "url": "https://rest.uniprot.org/uniprotkb/A0A077Y877.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Vacuolar\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":288},\"start\":{\"modifier\":\"EXACT\",\"value\":256}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:23:53.473191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8",
  "url": "https://rest.uniprot.org/uniprotkb/A0A077Y877.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":311},\"start\":{\"modifier\":\"EXACT\",\"value\":289}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:23:53.473191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8",
  "url": "https://rest.uniprot.org/uniprotkb/A0A077Y877.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":331},\"start\":{\"modifier\":\"EXACT\",\"value\":312}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:23:53.473191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8",
  "url": "https://rest.uniprot.org/uniprotkb/A0A077Y877.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":357},\"start\":{\"modifier\":\"EXACT\",\"value\":332}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:23:53.473191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8",
  "url": "https://rest.uniprot.org/uniprotkb/A0A077Y877.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"Vacuolar\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":362},\"start\":{\"modifier\":\"EXACT\",\"value\":358}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:23:53.473191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8",
  "url": "https://rest.uniprot.org/uniprotkb/A0A077Y877.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":382},\"start\":{\"modifier\":\"EXACT\",\"value\":363}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:23:53.473191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8",
  "url": "https://rest.uniprot.org/uniprotkb/A0A077Y877.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":393},\"start\":{\"modifier\":\"EXACT\",\"value\":383}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-02T04:23:53.473191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8",
  "url": "https://rest.uniprot.org/uniprotkb/A0A077Y877.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":416},\"start\":{\"modifier\":\"EXACT\",\"value\":394}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-02T04:23:53.473191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8",
  "url": "https://rest.uniprot.org/uniprotkb/A0A077Y877.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"description\":\"Vacuolar\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":435},\"start\":{\"modifier\":\"EXACT\",\"value\":417}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/11",
  "retrieved_utc": "2026-11-02T04:23:53.473191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8",
  "url": "https://rest.uniprot.org/uniprotkb/A0A077Y877.json"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)

```json
{
  "evidence_id": "C16",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":455},\"start\":{\"modifier\":\"EXACT\",\"value\":436}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/12",
  "retrieved_utc": "2026-11-02T04:23:53.473191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8",
  "url": "https://rest.uniprot.org/uniprotkb/A0A077Y877.json"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)

```json
{
  "evidence_id": "C17",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":475},\"start\":{\"modifier\":\"EXACT\",\"value\":456}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/13",
  "retrieved_utc": "2026-11-02T04:23:53.473191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8",
  "url": "https://rest.uniprot.org/uniprotkb/A0A077Y877.json"
}
```

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)

```json
{
  "evidence_id": "C18",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":499},\"start\":{\"modifier\":\"EXACT\",\"value\":476}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/14",
  "retrieved_utc": "2026-11-02T04:23:53.473191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8",
  "url": "https://rest.uniprot.org/uniprotkb/A0A077Y877.json"
}
```

### Evidence C19

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)

```json
{
  "evidence_id": "C19",
  "excerpt": "{\"description\":\"Vacuolar\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":529},\"start\":{\"modifier\":\"EXACT\",\"value\":500}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/15",
  "retrieved_utc": "2026-11-02T04:23:53.473191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8",
  "url": "https://rest.uniprot.org/uniprotkb/A0A077Y877.json"
}
```

### Evidence C20

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)

```json
{
  "evidence_id": "C20",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":546},\"start\":{\"modifier\":\"EXACT\",\"value\":530}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/16",
  "retrieved_utc": "2026-11-02T04:23:53.473191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8",
  "url": "https://rest.uniprot.org/uniprotkb/A0A077Y877.json"
}
```

### Evidence C21

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)

```json
{
  "evidence_id": "C21",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":566},\"start\":{\"modifier\":\"EXACT\",\"value\":547}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/17",
  "retrieved_utc": "2026-11-02T04:23:53.473191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8",
  "url": "https://rest.uniprot.org/uniprotkb/A0A077Y877.json"
}
```

### Evidence C22

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)

```json
{
  "evidence_id": "C22",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":585},\"start\":{\"modifier\":\"EXACT\",\"value\":567}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/18",
  "retrieved_utc": "2026-11-02T04:23:53.473191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8",
  "url": "https://rest.uniprot.org/uniprotkb/A0A077Y877.json"
}
```

### Evidence C23

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)

```json
{
  "evidence_id": "C23",
  "excerpt": "{\"description\":\"Vacuolar\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":596},\"start\":{\"modifier\":\"EXACT\",\"value\":586}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/19",
  "retrieved_utc": "2026-11-02T04:23:53.473191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8",
  "url": "https://rest.uniprot.org/uniprotkb/A0A077Y877.json"
}
```

### Evidence C24

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)

```json
{
  "evidence_id": "C24",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":615},\"start\":{\"modifier\":\"EXACT\",\"value\":597}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/20",
  "retrieved_utc": "2026-11-02T04:23:53.473191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8",
  "url": "https://rest.uniprot.org/uniprotkb/A0A077Y877.json"
}
```

### Evidence C25

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)

```json
{
  "evidence_id": "C25",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":634},\"start\":{\"modifier\":\"EXACT\",\"value\":616}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/21",
  "retrieved_utc": "2026-11-02T04:23:53.473191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8",
  "url": "https://rest.uniprot.org/uniprotkb/A0A077Y877.json"
}
```

### Evidence C26

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)

```json
{
  "evidence_id": "C26",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":657},\"start\":{\"modifier\":\"EXACT\",\"value\":635}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/22",
  "retrieved_utc": "2026-11-02T04:23:53.473191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8",
  "url": "https://rest.uniprot.org/uniprotkb/A0A077Y877.json"
}
```

### Evidence C27

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)

```json
{
  "evidence_id": "C27",
  "excerpt": "{\"description\":\"Vacuolar\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":662},\"start\":{\"modifier\":\"EXACT\",\"value\":658}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/23",
  "retrieved_utc": "2026-11-02T04:23:53.473191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8",
  "url": "https://rest.uniprot.org/uniprotkb/A0A077Y877.json"
}
```

### Evidence C28

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)

```json
{
  "evidence_id": "C28",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":684},\"start\":{\"modifier\":\"EXACT\",\"value\":663}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/24",
  "retrieved_utc": "2026-11-02T04:23:53.473191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8",
  "url": "https://rest.uniprot.org/uniprotkb/A0A077Y877.json"
}
```

### Evidence C29

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)

```json
{
  "evidence_id": "C29",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":696},\"start\":{\"modifier\":\"EXACT\",\"value\":685}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/25",
  "retrieved_utc": "2026-11-02T04:23:53.473191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8",
  "url": "https://rest.uniprot.org/uniprotkb/A0A077Y877.json"
}
```

### Evidence C30

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)

```json
{
  "evidence_id": "C30",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhong M.\",\"Zhou B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38049852\"},{\"database\":\"DOI\",\"id\":\"10.1186/s12915-023-01776-y\"}],\"citationType\":\"journal article\",\"firstPage\":\"279\",\"id\":\"38049852\",\"journal\":\"BMC Biol.\",\"lastPage\":\"279\",\"publicationDate\":\"2023\",\"title\":\"Plasmodium yoelii iron transporter PyDMT1 interacts with host ferritin and is required in full activity for malarial pathogenesis.\",\"volume\":\"21\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"TRANSPORTER ACTIVITY\",\"SUBCELLULAR LOCATION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:23:53.473191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8",
  "url": "https://rest.uniprot.org/uniprotkb/A0A077Y877.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H1",
  "excerpt": "ID   DMT1_PLAYE              Reviewed;         696 AA.\nAC   A0A077Y877;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   29-OCT-2014, sequence version 1.\nDT   28-JAN-2026, entry version 38.\nDE   RecName: Full=Divalent metal transporter 1 {ECO:0000303|PubMed:38049852};\nDE            Short=PyDMT1 {ECO:0000303|PubMed:38049852};\nDE   AltName: Full=Food vacuole resident transporter 1 {ECO:0000250|UniProtKB:Q8I3M7};\nGN   Name=FVRT1 {ECO:0000250|UniProtKB:Q8I3M7};\nGN   ORFNames=PY17X_1241800 {ECO:0000312|EMBL:VTZ80216.1},\nGN   PYYM_1241000 {ECO:0000312|EMBL:CDU19580.1};\nOS   Plasmodium yoelii.\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;\nOC   Plasmodiidae; Plasmodium; Plasmodium (Vinckeia).\nOX   NCBI_TaxID=5861 {ECO:0000312|Proteomes:UP000072904};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:55.877262+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47",
  "url": "https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, TRANSPORTER ACTIVITY, SUBCELLULAR LOCATION, AND DISRUPTION\nRP   PHENOTYPE.\nRX   PubMed=38049852; DOI=10.1186/s12915-023-01776-y;\nRA   Zhong M., Zhou B.;\nRT   \"Plasmodium yoelii iron transporter PyDMT1 interacts with host ferritin and\nRT   is required in full activity for malarial pathogenesis.\";\nRL   BMC Biol. 21:279-279(2023).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:55.877262+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 29-36",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47",
  "url": "https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H3",
  "excerpt": "FT   TOPO_DOM        1..236\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:55.877262+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 91-93",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47",
  "url": "https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H4",
  "excerpt": "FT   TRANSMEM        237..255\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:55.877262+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 94-96",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47",
  "url": "https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H5",
  "excerpt": "FT   TOPO_DOM        256..288\nFT                   /note=\"Vacuolar\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:55.877262+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 97-99",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47",
  "url": "https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H6",
  "excerpt": "FT   TRANSMEM        289..311\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:55.877262+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 100-102",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47",
  "url": "https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H7",
  "excerpt": "FT   TOPO_DOM        312..331\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:55.877262+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 103-105",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47",
  "url": "https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H8",
  "excerpt": "FT   TRANSMEM        332..357\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:55.877262+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 106-108",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47",
  "url": "https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H9",
  "excerpt": "FT   TOPO_DOM        358..362\nFT                   /note=\"Vacuolar\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:55.877262+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 109-111",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47",
  "url": "https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H10",
  "excerpt": "FT   TRANSMEM        363..382\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:55.877262+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 112-114",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47",
  "url": "https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H11",
  "excerpt": "FT   TOPO_DOM        383..393\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:55.877262+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 115-117",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47",
  "url": "https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H12",
  "excerpt": "FT   TRANSMEM        394..416\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:55.877262+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 118-120",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47",
  "url": "https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H13",
  "excerpt": "FT   TOPO_DOM        417..435\nFT                   /note=\"Vacuolar\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:55.877262+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 121-123",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47",
  "url": "https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H14",
  "excerpt": "FT   TRANSMEM        436..455\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:55.877262+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 124-126",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47",
  "url": "https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38"
}
```

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H15",
  "excerpt": "FT   TOPO_DOM        456..475\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:55.877262+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 127-129",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47",
  "url": "https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38"
}
```

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H16",
  "excerpt": "FT   TRANSMEM        476..499\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:55.877262+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 130-132",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47",
  "url": "https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38"
}
```

### Evidence H17

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H17",
  "excerpt": "FT   TOPO_DOM        500..529\nFT                   /note=\"Vacuolar\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:55.877262+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 133-135",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47",
  "url": "https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38"
}
```

### Evidence H18

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H18",
  "excerpt": "FT   TRANSMEM        530..546\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:55.877262+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 136-138",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47",
  "url": "https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38"
}
```

### Evidence H19

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H19",
  "excerpt": "FT   TOPO_DOM        547..566\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:55.877262+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 139-141",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47",
  "url": "https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38"
}
```

### Evidence H20

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H20",
  "excerpt": "FT   TRANSMEM        567..585\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:55.877262+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 142-144",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47",
  "url": "https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38"
}
```

### Evidence H21

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H21",
  "excerpt": "FT   TOPO_DOM        586..596\nFT                   /note=\"Vacuolar\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:55.877262+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 145-147",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47",
  "url": "https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38"
}
```

### Evidence H22

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H22",
  "excerpt": "FT   TRANSMEM        597..615\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:55.877262+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 148-150",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47",
  "url": "https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38"
}
```

### Evidence H23

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H23",
  "excerpt": "FT   TOPO_DOM        616..634\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:55.877262+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 151-153",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47",
  "url": "https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38"
}
```

### Evidence H24

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H24",
  "excerpt": "FT   TRANSMEM        635..657\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:55.877262+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 154-156",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47",
  "url": "https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38"
}
```

### Evidence H25

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H25",
  "excerpt": "FT   TOPO_DOM        658..662\nFT                   /note=\"Vacuolar\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:55.877262+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 157-159",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47",
  "url": "https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38"
}
```

### Evidence H26

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H26",
  "excerpt": "FT   TRANSMEM        663..684\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:55.877262+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 160-162",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47",
  "url": "https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38"
}
```

### Evidence H27

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H27",
  "excerpt": "FT   TOPO_DOM        685..696\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:55.877262+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 163-165",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47",
  "url": "https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 0. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
