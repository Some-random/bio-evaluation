# transmembrane_0022

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0022.txt)

**Task:** `transmembrane`  
**Expected answer:** **B** — 12..32; 181..201; 220..240; 244..264; 285..305; 312..332; 346..366; 398..418

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MIIDLFQSKKLIISIIILILRISLFSCAEHLFFNNNFNFFNFSENNHAKVNELNIDTKYLYQGLRNINIYLALSALNGITKEKINDISQWNGYKTRNNDETNISNVVVTEWKQLNKKSFFLKNNNISNNDNLIKGMPNPYFINSLTEDINNINLYFNIRNDIKYGEIIYKGTYIPHIYNNIFLIFLISYMYWFCIKILFNGYIKGKYVAKEYILKISTLFIFFVILKISLIFLPAILSCIVCLILTFYFYSISMSPCKDIFYLFESTRIKKEPIGWIIIVYAESILIGNVIYNFLCPPKIIIIFIRYIQNDFLVKIICLTIILFISFLIFFLMISNIFPAKKAQNFVFSFTSSYLIVSCFAYFWNIFLLRFLNNTNIFQIEPIMFFSYTPKFVFNRQNMFALFMIFAMSILSIIFPRIKKLKQNIFDMKENIYDSDIDIGKASKNRYNIILNYFT

[Multiple Choices]
A. 12..32; 181..201; 220..240; 249..261; 285..305; 312..332; 346..366; 398..418
B. 12..32; 181..201; 220..240; 244..264; 285..305; 312..332; 346..366; 398..418
C. 6..26
D. 12..32; 181..201; 220..240; 285..305; 312..332; 346..366; 398..418
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

> The sequence-matched UniProt annotation lists all eight spans in choice B, including 244..264. These are computationally supported helical transmembrane annotations (ECO:0000255), not evidence of experimental validation.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains several hydrophobic stretches that support a multipass membrane-protein interpretation. But the distinguishing interval around 244..264 is not an obvious uninterrupted hydrophobic helix: it includes multiple polar or charged residues. General membrane-protein knowledge therefore does not meaningfully resolve whether to include that span, or which nearby boundaries to use.


**Missing item-specific fact**

> A target-specific transmembrane-span annotation or experimental determination of whether and where the 244..264 region crosses the membrane.


**Reason**

> Transferable sequence reasoning supports several of the shared spans, but the choices differ on a marginal region and exact boundaries that the provided sequence does not clearly resolve.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> The sequence does not clearly establish whether the questionable 244..264 region is a membrane-spanning helix. Including it (B) follows the computational annotation; omitting it (D) is also plausible from the sequence alone.


### Important caveats

- The source annotation matches the supplied sequence, but its evidence code indicates computational support rather than experimental confirmation.
- The reviewer-only source annotations were not part of the original model input and do not establish that the exact span is experimentally verified.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains several hydrophobic stretches that support a multipass membrane-protein interpretation. But the distinguishing interval around 244..264 is not an obvious uninterrupted hydrophobic helix: it includes multiple polar or charged residues. General membrane-protein knowledge therefore does not meaningfully resolve whether to include that span, or which nearby boundaries to use.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "A target-specific transmembrane-span annotation or experimental determination of whether and where the 244..264 region crosses the membrane.",
    "reason": "Transferable sequence reasoning supports several of the shared spans, but the choices differ on a marginal region and exact boundaries that the provided sequence does not clearly resolve."
  },
  "case_id": "transmembrane_0022",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "C10",
      "C11",
      "C12"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation lists all eight spans in choice B, including 244..264. These are computationally supported helical transmembrane annotations (ECO:0000255), not evidence of experimental validation."
  },
  "important_caveats": [
    "The source annotation matches the supplied sequence, but its evidence code indicates computational support rather than experimental confirmation.",
    "The reviewer-only source annotations were not part of the original model input and do not establish that the exact span is experimentally verified."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "The sequence does not clearly establish whether the questionable 244..264 region is a membrane-spanning helix. Including it (B) follows the computational annotation; omitting it (D) is also plausible from the sequence alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0022",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation lists all eight spans in choice B, including 244..264. These are computationally supported helical transmembrane annotations (ECO:0000255), not evidence of experimental validation.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains several hydrophobic stretches that support a multipass membrane-protein interpretation. But the distinguishing interval around 244..264 is not an obvious uninterrupted hydrophobic helix: it includes multiple polar or charged residues. General membrane-protein knowledge therefore does not meaningfully resolve whether to include that span, or which nearby boundaries to use.",
    "missing_item_specific_fact": "A target-specific transmembrane-span annotation or experimental determination of whether and where the 244..264 region crosses the membrane.",
    "reason": "Transferable sequence reasoning supports several of the shared spans, but the choices differ on a marginal region and exact boundaries that the provided sequence does not clearly resolve."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "The sequence does not clearly establish whether the questionable 244..264 region is a membrane-spanning helix. Including it (B) follows the computational annotation; omitting it (D) is also plausible from the sequence alone."
  },
  "important_caveats": [
    "The source annotation matches the supplied sequence, but its evidence code indicates computational support rather than experimental confirmation.",
    "The reviewer-only source annotations were not part of the original model input and do not establish that the exact span is experimentally verified."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for A0A509AKT6 (Pbs54) lists exactly 8 transmembrane helical regions at 12..32, 181..201, 220..240, 244..264, 285..305, 312..332, 346..366, and 398..418, matching option B precisely. However, all annotations carry evidence code ECO:0000255 (similarity-based computational prediction), not experimental evidence. The protein is described as 'Membrane protein Pbs54' with a PubMed reference on gamete fertilization function, but the TM boundaries are predicted by similarity rather than experimentally determined.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The critical distinction between options A and B is the 4th TM segment: 249..261 (13 residues) vs 244..264 (21 residues). A well-established biophysical principle in membrane biology is that a transmembrane alpha-helix requires approximately 19-21 hydrophobic residues to span the ~30 Å hydrophobic core of the lipid bilayer (1.5 Å rise per residue × 20 residues ≈ 30 Å). A 13-residue segment spans only ~19.5 Å, which is insufficient. This length criterion, learned from general membrane protein biology, eliminates option A. Option C (a single 21-residue segment at 6..26) is eliminated because the protein clearly contains multiple hydrophobic stretches distributed throughout its length, inconsistent with a single-pass protein. Option D omits the 4th TM region entirely; the sequence at 244-264 (LILTFYFYSISMSPCKDIFYL) contains a majority of hydrophobic residues (L, I, L, F, Y, F, Y, I, M, I, F, Y, L) despite some polar/charged residues (S, P, C, K, D), and its 21-residue length is consistent with a TM helix in a multi-pass membrane protein. Plasmodium membrane proteins are known to tolerate somewhat unusual TM helix compositions. Thus, transferable knowledge of TM helix length requirements and hydrophobicity assessment distinguishes B from A and supports B over D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The length criterion for transmembrane helices (~20 residues minimum) is a fundamental, well-established biophysical fact transferable from any membrane protein study. It directly eliminates option A's 13-residue segment. The hydrophobicity composition of the 244-264 region, combined with the multi-pass architecture evident from the other 7 TM segments, supports including this region. While the charged residues (K, D) in the middle of the 244-264 segment are atypical, they do not categorically exclude a TM helix, especially in Plasmodium proteins known for unusual membrane topologies. The reasoning chain is concrete and relies on general membrane biology rather than recall of this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option A is eliminated by the 13-residue length being below the minimum for TM helix spanning. Option C is eliminated as the protein clearly has multiple hydrophobic stretches. Option D is less certain than B because the 244-264 region contains charged residues, but the overall hydrophobic character and correct length make B more defensible. No two options are equally defensible given the biophysical constraints.


### Important caveats

- All TM annotations in UniProt carry ECO:0000255 (similarity-based computational prediction), not experimental evidence. The TM boundaries are predictions, not experimentally validated.
- The 244..264 region contains unusual residues for a TM helix (K, D, P, S), which makes the B vs D distinction less certain from sequence alone, though the length and overall hydrophobicity favor B.
- The reviewer-only evidence confirms the sequence matches the UniProt entry exactly (SHA256 match), but the identity of the protein (Pbs54, Plasmodium berghei) was not available to the evaluated model.
- The annotation evidence code ECO:0000255 means the TM boundaries were predicted by similarity to other proteins, so they carry inherent uncertainty typical of computational TM predictions.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The critical distinction between options A and B is the 4th TM segment: 249..261 (13 residues) vs 244..264 (21 residues). A well-established biophysical principle in membrane biology is that a transmembrane alpha-helix requires approximately 19-21 hydrophobic residues to span the ~30 Å hydrophobic core of the lipid bilayer (1.5 Å rise per residue × 20 residues ≈ 30 Å). A 13-residue segment spans only ~19.5 Å, which is insufficient. This length criterion, learned from general membrane protein biology, eliminates option A. Option C (a single 21-residue segment at 6..26) is eliminated because the protein clearly contains multiple hydrophobic stretches distributed throughout its length, inconsistent with a single-pass protein. Option D omits the 4th TM region entirely; the sequence at 244-264 (LILTFYFYSISMSPCKDIFYL) contains a majority of hydrophobic residues (L, I, L, F, Y, F, Y, I, M, I, F, Y, L) despite some polar/charged residues (S, P, C, K, D), and its 21-residue length is consistent with a TM helix in a multi-pass membrane protein. Plasmodium membrane proteins are known to tolerate somewhat unusual TM helix compositions. Thus, transferable knowledge of TM helix length requirements and hydrophobicity assessment distinguishes B from A and supports B over D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The length criterion for transmembrane helices (~20 residues minimum) is a fundamental, well-established biophysical fact transferable from any membrane protein study. It directly eliminates option A's 13-residue segment. The hydrophobicity composition of the 244-264 region, combined with the multi-pass architecture evident from the other 7 TM segments, supports including this region. While the charged residues (K, D) in the middle of the 244-264 segment are atypical, they do not categorically exclude a TM helix, especially in Plasmodium proteins known for unusual membrane topologies. The reasoning chain is concrete and relies on general membrane biology rather than recall of this specific protein's annotation."
  },
  "case_id": "transmembrane_0022",
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
      "H3",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9",
      "H10"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for A0A509AKT6 (Pbs54) lists exactly 8 transmembrane helical regions at 12..32, 181..201, 220..240, 244..264, 285..305, 312..332, 346..366, and 398..418, matching option B precisely. However, all annotations carry evidence code ECO:0000255 (similarity-based computational prediction), not experimental evidence. The protein is described as 'Membrane protein Pbs54' with a PubMed reference on gamete fertilization function, but the TM boundaries are predicted by similarity rather than experimentally determined."
  },
  "important_caveats": [
    "All TM annotations in UniProt carry ECO:0000255 (similarity-based computational prediction), not experimental evidence. The TM boundaries are predictions, not experimentally validated.",
    "The 244..264 region contains unusual residues for a TM helix (K, D, P, S), which makes the B vs D distinction less certain from sequence alone, though the length and overall hydrophobicity favor B.",
    "The reviewer-only evidence confirms the sequence matches the UniProt entry exactly (SHA256 match), but the identity of the protein (Pbs54, Plasmodium berghei) was not available to the evaluated model.",
    "The annotation evidence code ECO:0000255 means the TM boundaries were predicted by similarity to other proteins, so they carry inherent uncertainty typical of computational TM predictions."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option A is eliminated by the 13-residue length being below the minimum for TM helix spanning. Option C is eliminated as the protein clearly has multiple hydrophobic stretches. Option D is less certain than B because the 244-264 region contains charged residues, but the overall hydrophobic character and correct length make B more defensible. No two options are equally defensible given the biophysical constraints."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0022",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for A0A509AKT6 (Pbs54) lists exactly 8 transmembrane helical regions at 12..32, 181..201, 220..240, 244..264, 285..305, 312..332, 346..366, and 398..418, matching option B precisely. However, all annotations carry evidence code ECO:0000255 (similarity-based computational prediction), not experimental evidence. The protein is described as 'Membrane protein Pbs54' with a PubMed reference on gamete fertilization function, but the TM boundaries are predicted by similarity rather than experimentally determined.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The critical distinction between options A and B is the 4th TM segment: 249..261 (13 residues) vs 244..264 (21 residues). A well-established biophysical principle in membrane biology is that a transmembrane alpha-helix requires approximately 19-21 hydrophobic residues to span the ~30 Å hydrophobic core of the lipid bilayer (1.5 Å rise per residue × 20 residues ≈ 30 Å). A 13-residue segment spans only ~19.5 Å, which is insufficient. This length criterion, learned from general membrane protein biology, eliminates option A. Option C (a single 21-residue segment at 6..26) is eliminated because the protein clearly contains multiple hydrophobic stretches distributed throughout its length, inconsistent with a single-pass protein. Option D omits the 4th TM region entirely; the sequence at 244-264 (LILTFYFYSISMSPCKDIFYL) contains a majority of hydrophobic residues (L, I, L, F, Y, F, Y, I, M, I, F, Y, L) despite some polar/charged residues (S, P, C, K, D), and its 21-residue length is consistent with a TM helix in a multi-pass membrane protein. Plasmodium membrane proteins are known to tolerate somewhat unusual TM helix compositions. Thus, transferable knowledge of TM helix length requirements and hydrophobicity assessment distinguishes B from A and supports B over D.",
    "missing_item_specific_fact": "",
    "reason": "The length criterion for transmembrane helices (~20 residues minimum) is a fundamental, well-established biophysical fact transferable from any membrane protein study. It directly eliminates option A's 13-residue segment. The hydrophobicity composition of the 244-264 region, combined with the multi-pass architecture evident from the other 7 TM segments, supports including this region. While the charged residues (K, D) in the middle of the 244-264 segment are atypical, they do not categorically exclude a TM helix, especially in Plasmodium proteins known for unusual membrane topologies. The reasoning chain is concrete and relies on general membrane biology rather than recall of this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option A is eliminated by the 13-residue length being below the minimum for TM helix spanning. Option C is eliminated as the protein clearly has multiple hydrophobic stretches. Option D is less certain than B because the 244-264 region contains charged residues, but the overall hydrophobic character and correct length make B more defensible. No two options are equally defensible given the biophysical constraints."
  },
  "important_caveats": [
    "All TM annotations in UniProt carry ECO:0000255 (similarity-based computational prediction), not experimental evidence. The TM boundaries are predictions, not experimentally validated.",
    "The 244..264 region contains unusual residues for a TM helix (K, D, P, S), which makes the B vs D distinction less certain from sequence alone, though the length and overall hydrophobicity favor B.",
    "The reviewer-only evidence confirms the sequence matches the UniProt entry exactly (SHA256 match), but the identity of the protein (Pbs54, Plasmodium berghei) was not available to the evaluated model.",
    "The annotation evidence code ECO:0000255 means the TM boundaries were predicted by similarity to other proteins, so they carry inherent uncertainty typical of computational TM predictions."
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
  "benchmark_sequence_length": 455,
  "benchmark_sequence_sha256": "1460df501b8bcc92b33e8ca8893f41aacacbf2a45774542573ece53788a3b826",
  "current_entry_audit": {
    "entryVersion": 20,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2019-09-18",
    "sequenceVersion": 1
  },
  "current_record_sha256": "5f12f41d692d932165f3b4e32653a23e5a692f941e64b936309ea1b6a4bbad25",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 455,
  "current_source_sequence_sha256": "1460df501b8bcc92b33e8ca8893f41aacacbf2a45774542573ece53788a3b826",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 19,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A509AKT6",
  "selected_historical_entry_version": 19,
  "selected_historical_record_sha256": "6d40908ee73c41ed5a2c9670ef889cabc4ff6bd15769a8b8824958da5cb4a8f5",
  "selected_historical_source_sequence_length": 455,
  "selected_historical_source_sequence_sha256": "1460df501b8bcc92b33e8ca8893f41aacacbf2a45774542573ece53788a3b826",
  "selected_historical_version": {
    "accession": "A0A509AKT6",
    "database": "Swiss-Prot",
    "entryVersion": 19,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "PBS54_PLABA",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AKT6.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A509AKT6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:25:23.898557+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5f12f41d692d932165f3b4e32653a23e5a692f941e64b936309ea1b6a4bbad25",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AKT6.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AKT6.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":20,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2019-09-18\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:25:23.898557+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5f12f41d692d932165f3b4e32653a23e5a692f941e64b936309ea1b6a4bbad25",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AKT6.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AKT6.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000074855\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Aconoidasida\",\"Haemosporida\",\"Plasmodiidae\",\"Plasmodium\",\"Vinckeia\"],\"scientificName\":\"Plasmodium berghei (strain Anka)\",\"taxonId\":5823}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:25:23.898557+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5f12f41d692d932165f3b4e32653a23e5a692f941e64b936309ea1b6a4bbad25",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AKT6.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AKT6.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"37774810\",\"source\":\"PubMed\"}],\"value\":\"Membrane protein Pbs54\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"37774810\",\"source\":\"PubMed\"}],\"value\":\"Pbs54\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:25:23.898557+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5f12f41d692d932165f3b4e32653a23e5a692f941e64b936309ea1b6a4bbad25",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AKT6.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AKT6.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":32},\"start\":{\"modifier\":\"EXACT\",\"value\":12}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:25:23.898557+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5f12f41d692d932165f3b4e32653a23e5a692f941e64b936309ea1b6a4bbad25",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AKT6.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AKT6.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":201},\"start\":{\"modifier\":\"EXACT\",\"value\":181}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:25:23.898557+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5f12f41d692d932165f3b4e32653a23e5a692f941e64b936309ea1b6a4bbad25",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AKT6.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AKT6.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":240},\"start\":{\"modifier\":\"EXACT\",\"value\":220}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:25:23.898557+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5f12f41d692d932165f3b4e32653a23e5a692f941e64b936309ea1b6a4bbad25",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AKT6.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AKT6.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":264},\"start\":{\"modifier\":\"EXACT\",\"value\":244}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:25:23.898557+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5f12f41d692d932165f3b4e32653a23e5a692f941e64b936309ea1b6a4bbad25",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AKT6.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AKT6.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":305},\"start\":{\"modifier\":\"EXACT\",\"value\":285}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:25:23.898557+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5f12f41d692d932165f3b4e32653a23e5a692f941e64b936309ea1b6a4bbad25",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AKT6.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AKT6.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":332},\"start\":{\"modifier\":\"EXACT\",\"value\":312}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:25:23.898557+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5f12f41d692d932165f3b4e32653a23e5a692f941e64b936309ea1b6a4bbad25",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AKT6.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AKT6.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":366},\"start\":{\"modifier\":\"EXACT\",\"value\":346}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:25:23.898557+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5f12f41d692d932165f3b4e32653a23e5a692f941e64b936309ea1b6a4bbad25",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AKT6.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AKT6.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":418},\"start\":{\"modifier\":\"EXACT\",\"value\":398}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:25:23.898557+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5f12f41d692d932165f3b4e32653a23e5a692f941e64b936309ea1b6a4bbad25",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AKT6.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AKT6.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"citation\":{\"authors\":[\"Pang W.\",\"Bai J.\",\"Zhu L.\",\"Liu F.\",\"Wu Y.\",\"Yang F.\",\"Zheng L.\",\"Liu P.\",\"Zhang Y.\",\"Wang M.\",\"Li J.\",\"Zhu X.\",\"Cui L.\",\"Cao Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"37774810\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.ijpara.2023.08.003\"}],\"citationType\":\"journal article\",\"firstPage\":\"99\",\"id\":\"37774810\",\"journal\":\"Int. J. Parasitol.\",\"lastPage\":\"107\",\"publicationDate\":\"2024\",\"title\":\"Functional characterization of a conserved membrane protein, Pbs54, involved in gamete fertilization in Plasmodium berghei.\",\"volume\":\"54\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"SUBCELLULAR LOCATION\",\"DEVELOPMENTAL STAGE\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:25:23.898557+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5f12f41d692d932165f3b4e32653a23e5a692f941e64b936309ea1b6a4bbad25",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AKT6.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AKT6?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H1",
  "excerpt": "ID   PBS54_PLABA             Reviewed;         455 AA.\nAC   A0A509AKT6;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-SEP-2019, sequence version 1.\nDT   28-JAN-2026, entry version 19.\nDE   RecName: Full=Membrane protein Pbs54 {ECO:0000303|PubMed:37774810};\nDE            Short=Pbs54 {ECO:0000303|PubMed:37774810};\nGN   ORFNames=PBANKA_0813300 {ECO:0000312|EMBL:VUC55291.1};\nOS   Plasmodium berghei (strain Anka).\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;\nOC   Plasmodiidae; Plasmodium; Plasmodium (Vinckeia).\nOX   NCBI_TaxID=5823 {ECO:0000312|Proteomes:UP000074855};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:27.030552+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6d40908ee73c41ed5a2c9670ef889cabc4ff6bd15769a8b8824958da5cb4a8f5",
  "url": "https://rest.uniprot.org/unisave/A0A509AKT6?format=txt&versions=19"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AKT6?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, SUBCELLULAR LOCATION, DEVELOPMENTAL STAGE, AND DISRUPTION\nRP   PHENOTYPE.\nRX   PubMed=37774810; DOI=10.1016/j.ijpara.2023.08.003;\nRA   Pang W., Bai J., Zhu L., Liu F., Wu Y., Yang F., Zheng L., Liu P.,\nRA   Zhang Y., Wang M., Li J., Zhu X., Cui L., Cao Y.;\nRT   \"Functional characterization of a conserved membrane protein, Pbs54,\nRT   involved in gamete fertilization in Plasmodium berghei.\";\nRL   Int. J. Parasitol. 54:99-107(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:27.030552+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 25-33",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6d40908ee73c41ed5a2c9670ef889cabc4ff6bd15769a8b8824958da5cb4a8f5",
  "url": "https://rest.uniprot.org/unisave/A0A509AKT6?format=txt&versions=19"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AKT6?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H3",
  "excerpt": "FT   TRANSMEM        12..32\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:27.030552+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 82-84",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6d40908ee73c41ed5a2c9670ef889cabc4ff6bd15769a8b8824958da5cb4a8f5",
  "url": "https://rest.uniprot.org/unisave/A0A509AKT6?format=txt&versions=19"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AKT6?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H4",
  "excerpt": "FT   TRANSMEM        181..201\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:27.030552+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 85-87",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6d40908ee73c41ed5a2c9670ef889cabc4ff6bd15769a8b8824958da5cb4a8f5",
  "url": "https://rest.uniprot.org/unisave/A0A509AKT6?format=txt&versions=19"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AKT6?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H5",
  "excerpt": "FT   TRANSMEM        220..240\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:27.030552+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 88-90",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6d40908ee73c41ed5a2c9670ef889cabc4ff6bd15769a8b8824958da5cb4a8f5",
  "url": "https://rest.uniprot.org/unisave/A0A509AKT6?format=txt&versions=19"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AKT6?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H6",
  "excerpt": "FT   TRANSMEM        244..264\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:27.030552+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 91-93",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6d40908ee73c41ed5a2c9670ef889cabc4ff6bd15769a8b8824958da5cb4a8f5",
  "url": "https://rest.uniprot.org/unisave/A0A509AKT6?format=txt&versions=19"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AKT6?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H7",
  "excerpt": "FT   TRANSMEM        285..305\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:27.030552+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 94-96",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6d40908ee73c41ed5a2c9670ef889cabc4ff6bd15769a8b8824958da5cb4a8f5",
  "url": "https://rest.uniprot.org/unisave/A0A509AKT6?format=txt&versions=19"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AKT6?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H8",
  "excerpt": "FT   TRANSMEM        312..332\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:27.030552+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 97-99",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6d40908ee73c41ed5a2c9670ef889cabc4ff6bd15769a8b8824958da5cb4a8f5",
  "url": "https://rest.uniprot.org/unisave/A0A509AKT6?format=txt&versions=19"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AKT6?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H9",
  "excerpt": "FT   TRANSMEM        346..366\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:27.030552+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 100-102",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6d40908ee73c41ed5a2c9670ef889cabc4ff6bd15769a8b8824958da5cb4a8f5",
  "url": "https://rest.uniprot.org/unisave/A0A509AKT6?format=txt&versions=19"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AKT6?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H10",
  "excerpt": "FT   TRANSMEM        398..418\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:27.030552+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 103-105",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6d40908ee73c41ed5a2c9670ef889cabc4ff6bd15769a8b8824958da5cb4a8f5",
  "url": "https://rest.uniprot.org/unisave/A0A509AKT6?format=txt&versions=19"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 22. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
