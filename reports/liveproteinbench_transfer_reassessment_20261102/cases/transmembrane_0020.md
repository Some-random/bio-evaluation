# transmembrane_0020

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0020.txt)

**Task:** `transmembrane`  
**Expected answer:** **D** — 48..68; 83..103; 121..141; 145..165; 171..191; 203..223; 236..256; 269..289; 298..318; 336..356; 374..394; 403..423; 438..460; 516..536

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MQTATALEDSANAPSPAASSQGQFDREIVPIDTADAGNSTKRSPLKVALIMVALCCAVFLHALDNTIITTALPTITAAFDLDAAYTWIGSTYLLAVAASTMVWAKISDVFGRKPIILSANLCFFTGSLIAALSANFAMLIAARAIQGIGGAGVNVLANICVGDLFSQRKRGLYYGVIGGVWAVALSLGPVVGGSLTESISWRWCFYINLPLCAVVFVIIILLLDVKTPKTPFGKGIAAIDWVGAALSIGSTLMILLALSLGGQTEPWNSATVICLVVFGFIGWILCFSWEASLAKYPLLPVSIFKQIPTLAVLAACFIQSYAFVASAYYLPLYFQAVLGATPILSGVYLLPTAVSISISSTATGVYMRKTGQYLTPIYIGFVLQTLGYGLFIDLGPTANWAKIIVFQIIGGLGVGFNFQAPMVALQAFISPRELAMATSAYNFMRNVSGAISVVIGQTVFQNEMSKHQESLATILGPQLAAKLAGTGASASTDLIRSLPSPQRDVVHGVFANSMKSMWIMYTAFSAAALVVCPFLGKMVLREDHTETVTGLAAENAAREERLRQEKEKKDAKIRKCQVN

[Multiple Choices]
A. 48..68; 83..103; 121..141; 171..191; 203..223; 236..256; 269..289; 298..318; 336..356; 374..394; 403..423; 438..460; 516..536
B. 1..21
C. 48..68; 83..103; 121..141; 145..165; 171..191; 203..223; 236..256; 269..289; 298..318; 336..356; 374..394; 401..421; 438..460; 516..536
D. 48..68; 83..103; 121..141; 145..165; 171..191; 203..223; 236..256; 269..289; 298..318; 336..356; 374..394; 403..423; 438..460; 516..536
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

> The sequence-matched UniProt annotations list the transmembrane regions in D, including 145..165 and 403..423. These annotations are computationally evidenced (ECO:0000255), so they support the key as a prediction, not as direct experimental confirmation.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [C13](#evidence-c13), [C14](#evidence-c14), [C15](#evidence-c15), [C16](#evidence-c16), [C17](#evidence-c17), [C18](#evidence-c18).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains many long hydrophobic stretches characteristic of a multi-pass helical membrane protein. In particular, 145..165 is hydrophobic enough to support including that helix, making C or D more plausible than A, while B is incompatible with the nonhydrophobic N-terminus. But general sequence and family-level reasoning do not meaningfully distinguish the two-residue boundary shift between C and D.


**Missing item-specific fact**

> A target-specific boundary annotation or measurement distinguishing 403..423 from 401..421 is needed to select D rather than C.


**Reason**

> Transferable sequence features support the overall multi-pass topology and narrow the choices, but the remaining distinction between C and D is an exact two-residue boundary assignment that is not reliably inferable from the supplied sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> C and D describe the same apparent transmembrane helix with boundaries shifted by only two residues. Such small boundary differences are not meaningfully resolved by the sequence-based evidence available to the model.


### Important caveats

- The cited transmembrane features are computational annotations, not evidence of experimental validation.
- The source sequence matches the supplied sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains many long hydrophobic stretches characteristic of a multi-pass helical membrane protein. In particular, 145..165 is hydrophobic enough to support including that helix, making C or D more plausible than A, while B is incompatible with the nonhydrophobic N-terminus. But general sequence and family-level reasoning do not meaningfully distinguish the two-residue boundary shift between C and D.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "A target-specific boundary annotation or measurement distinguishing 403..423 from 401..421 is needed to select D rather than C.",
    "reason": "Transferable sequence features support the overall multi-pass topology and narrow the choices, but the remaining distinction between C and D is an exact two-residue boundary assignment that is not reliably inferable from the supplied sequence alone."
  },
  "case_id": "transmembrane_0020",
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
      "C13",
      "C14",
      "C15",
      "C16",
      "C17",
      "C18"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotations list the transmembrane regions in D, including 145..165 and 403..423. These annotations are computationally evidenced (ECO:0000255), so they support the key as a prediction, not as direct experimental confirmation."
  },
  "important_caveats": [
    "The cited transmembrane features are computational annotations, not evidence of experimental validation.",
    "The source sequence matches the supplied sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "C and D describe the same apparent transmembrane helix with boundaries shifted by only two residues. Such small boundary differences are not meaningfully resolved by the sequence-based evidence available to the model."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0020",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotations list the transmembrane regions in D, including 145..165 and 403..423. These annotations are computationally evidenced (ECO:0000255), so they support the key as a prediction, not as direct experimental confirmation.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "C14", "C15", "C16", "C17", "C18"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains many long hydrophobic stretches characteristic of a multi-pass helical membrane protein. In particular, 145..165 is hydrophobic enough to support including that helix, making C or D more plausible than A, while B is incompatible with the nonhydrophobic N-terminus. But general sequence and family-level reasoning do not meaningfully distinguish the two-residue boundary shift between C and D.",
    "missing_item_specific_fact": "A target-specific boundary annotation or measurement distinguishing 403..423 from 401..421 is needed to select D rather than C.",
    "reason": "Transferable sequence features support the overall multi-pass topology and narrow the choices, but the remaining distinction between C and D is an exact two-residue boundary assignment that is not reliably inferable from the supplied sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "C and D describe the same apparent transmembrane helix with boundaries shifted by only two residues. Such small boundary differences are not meaningfully resolved by the sequence-based evidence available to the model."
  },
  "important_caveats": [
    "The cited transmembrane features are computational annotations, not evidence of experimental validation.",
    "The source sequence matches the supplied sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt Swiss-Prot annotation for A0A455ZIM6 (MFS-type transporter ppz2 from Metarhizium majus) lists exactly 14 transmembrane helical segments at positions 48..68, 83..103, 121..141, 145..165, 171..191, 203..223, 236..256, 269..289, 298..318, 336..356, 374..394, 403..423, 438..460, 516..536, matching option D exactly. However, all annotations carry evidence code ECO:0000255 (inferred by similarity/prorule), meaning they are computational predictions transferred by homology rather than experimentally validated measurements. The sequence match is confirmed (SHA256 identical).

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [C13](#evidence-c13), [C14](#evidence-c14), [C15](#evidence-c15), [C16](#evidence-c16), [C17](#evidence-c17), [C18](#evidence-c18), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11), [H12](#evidence-h12), [H13](#evidence-h13), [H14](#evidence-h14), [H15](#evidence-h15), [H16](#evidence-h16), [H17](#evidence-h17).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Eliminating B is straightforward (N-terminus MQTATALEDSANAPSPAASS is clearly hydrophilic). The A vs C/D question (whether 145..165 is a TM) is borderline: the sequence IQGIGGAGVNVLANICVGDLF has average hydropathy ~1.27, below the typical TM threshold, though MFS-family knowledge (12-14 TMs, closely spaced helices) could weakly support its inclusion. However, the critical C vs D distinction (401..421 vs 403..423) is a 2-residue shift that cannot be resolved from sequence. Both regions (IIVFQIIGGLGVSFNFQAPMV vs VFQIIGGLGVSFNFQAPMVAL) have nearly identical hydrophobicity profiles, and no transferable pattern, spacing regularity, or family-level feature meaningfully distinguishes a start at 401 vs 403 or an end at 421 vs 423.


**Missing item-specific fact**

> The exact boundary positions of the 12th transmembrane helix (403..423 vs 401..421), which is a 2-residue annotation decision recorded in the UniProt entry that cannot be derived from sequence hydrophobicity, spacing patterns, or MFS-family knowledge.


**Reason**

> While a knowledgeable model can eliminate B and potentially argue for 14 TMs over 13 (A vs C/D) using MFS transporter family knowledge, the final distinction between C and D requires knowing the exact 2-residue boundary annotation for the 12th TM helix. No sequence feature, spacing regularity, or family-level inference meaningfully distinguishes a TM starting at 401 vs 403 or ending at 421 vs 423 when both boundaries fall in hydrophobic stretches of similar composition.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> Options C and D differ only by a 2-residue shift in the 12th TM boundary (401..421 vs 403..423). Both regions have comparable hydrophobicity and no clear sequence-based argument definitively favors one over the other. Option A (lacking 145..165) is also somewhat defensible since that region's hydropathy is borderline for a TM prediction.


### Important caveats

- All UniProt TM annotations for this entry use ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred from homologs, not experimentally determined boundaries.
- The 145..165 segment has notably lower hydropathy than the other annotated TMs, making its inclusion a judgment call that pure sequence analysis might not support.
- The 2-residue difference between options C and D represents annotation precision that exceeds what sequence-based reasoning can resolve.
- The protein is identified as an MFS-type transporter (from reviewer-only evidence), which typically has 12-14 TMs; this family knowledge could help with the A vs C/D question but not the C vs D distinction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Eliminating B is straightforward (N-terminus MQTATALEDSANAPSPAASS is clearly hydrophilic). The A vs C/D question (whether 145..165 is a TM) is borderline: the sequence IQGIGGAGVNVLANICVGDLF has average hydropathy ~1.27, below the typical TM threshold, though MFS-family knowledge (12-14 TMs, closely spaced helices) could weakly support its inclusion. However, the critical C vs D distinction (401..421 vs 403..423) is a 2-residue shift that cannot be resolved from sequence. Both regions (IIVFQIIGGLGVSFNFQAPMV vs VFQIIGGLGVSFNFQAPMVAL) have nearly identical hydrophobicity profiles, and no transferable pattern, spacing regularity, or family-level feature meaningfully distinguishes a start at 401 vs 403 or an end at 421 vs 423.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact boundary positions of the 12th transmembrane helix (403..423 vs 401..421), which is a 2-residue annotation decision recorded in the UniProt entry that cannot be derived from sequence hydrophobicity, spacing patterns, or MFS-family knowledge.",
    "reason": "While a knowledgeable model can eliminate B and potentially argue for 14 TMs over 13 (A vs C/D) using MFS transporter family knowledge, the final distinction between C and D requires knowing the exact 2-residue boundary annotation for the 12th TM helix. No sequence feature, spacing regularity, or family-level inference meaningfully distinguishes a TM starting at 401 vs 403 or ending at 421 vs 423 when both boundaries fall in hydrophobic stretches of similar composition."
  },
  "case_id": "transmembrane_0020",
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
      "C13",
      "C14",
      "C15",
      "C16",
      "C17",
      "C18",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9",
      "H10",
      "H11",
      "H12",
      "H13",
      "H14",
      "H15",
      "H16",
      "H17"
    ],
    "judgment": "supported",
    "reason": "The UniProt Swiss-Prot annotation for A0A455ZIM6 (MFS-type transporter ppz2 from Metarhizium majus) lists exactly 14 transmembrane helical segments at positions 48..68, 83..103, 121..141, 145..165, 171..191, 203..223, 236..256, 269..289, 298..318, 336..356, 374..394, 403..423, 438..460, 516..536, matching option D exactly. However, all annotations carry evidence code ECO:0000255 (inferred by similarity/prorule), meaning they are computational predictions transferred by homology rather than experimentally validated measurements. The sequence match is confirmed (SHA256 identical)."
  },
  "important_caveats": [
    "All UniProt TM annotations for this entry use ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred from homologs, not experimentally determined boundaries.",
    "The 145..165 segment has notably lower hydropathy than the other annotated TMs, making its inclusion a judgment call that pure sequence analysis might not support.",
    "The 2-residue difference between options C and D represents annotation precision that exceeds what sequence-based reasoning can resolve.",
    "The protein is identified as an MFS-type transporter (from reviewer-only evidence), which typically has 12-14 TMs; this family knowledge could help with the A vs C/D question but not the C vs D distinction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "Options C and D differ only by a 2-residue shift in the 12th TM boundary (401..421 vs 403..423). Both regions have comparable hydrophobicity and no clear sequence-based argument definitively favors one over the other. Option A (lacking 145..165) is also somewhat defensible since that region's hydropathy is borderline for a TM prediction."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0020",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt Swiss-Prot annotation for A0A455ZIM6 (MFS-type transporter ppz2 from Metarhizium majus) lists exactly 14 transmembrane helical segments at positions 48..68, 83..103, 121..141, 145..165, 171..191, 203..223, 236..256, 269..289, 298..318, 336..356, 374..394, 403..423, 438..460, 516..536, matching option D exactly. However, all annotations carry evidence code ECO:0000255 (inferred by similarity/prorule), meaning they are computational predictions transferred by homology rather than experimentally validated measurements. The sequence match is confirmed (SHA256 identical).",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "C14", "C15", "C16", "C17", "C18", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "H11", "H12", "H13", "H14", "H15", "H16", "H17"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Eliminating B is straightforward (N-terminus MQTATALEDSANAPSPAASS is clearly hydrophilic). The A vs C/D question (whether 145..165 is a TM) is borderline: the sequence IQGIGGAGVNVLANICVGDLF has average hydropathy ~1.27, below the typical TM threshold, though MFS-family knowledge (12-14 TMs, closely spaced helices) could weakly support its inclusion. However, the critical C vs D distinction (401..421 vs 403..423) is a 2-residue shift that cannot be resolved from sequence. Both regions (IIVFQIIGGLGVSFNFQAPMV vs VFQIIGGLGVSFNFQAPMVAL) have nearly identical hydrophobicity profiles, and no transferable pattern, spacing regularity, or family-level feature meaningfully distinguishes a start at 401 vs 403 or an end at 421 vs 423.",
    "missing_item_specific_fact": "The exact boundary positions of the 12th transmembrane helix (403..423 vs 401..421), which is a 2-residue annotation decision recorded in the UniProt entry that cannot be derived from sequence hydrophobicity, spacing patterns, or MFS-family knowledge.",
    "reason": "While a knowledgeable model can eliminate B and potentially argue for 14 TMs over 13 (A vs C/D) using MFS transporter family knowledge, the final distinction between C and D requires knowing the exact 2-residue boundary annotation for the 12th TM helix. No sequence feature, spacing regularity, or family-level inference meaningfully distinguishes a TM starting at 401 vs 403 or ending at 421 vs 423 when both boundaries fall in hydrophobic stretches of similar composition."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "Options C and D differ only by a 2-residue shift in the 12th TM boundary (401..421 vs 403..423). Both regions have comparable hydrophobicity and no clear sequence-based argument definitively favors one over the other. Option A (lacking 145..165) is also somewhat defensible since that region's hydropathy is borderline for a TM prediction."
  },
  "important_caveats": [
    "All UniProt TM annotations for this entry use ECO:0000255 (inferred by similarity), meaning they are computational predictions transferred from homologs, not experimentally determined boundaries.",
    "The 145..165 segment has notably lower hydropathy than the other annotated TMs, making its inclusion a judgment call that pure sequence analysis might not support.",
    "The 2-residue difference between options C and D represents annotation precision that exceeds what sequence-based reasoning can resolve.",
    "The protein is identified as an MFS-type transporter (from reviewer-only evidence), which typically has 12-14 TMs; this family knowledge could help with the A vs C/D question but not the C vs D distinction."
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
  "benchmark_sequence_length": 579,
  "benchmark_sequence_sha256": "351b6c74b4c2221103ffe06ad649dd3d536e0edd19c3a314131076b2cd6dfa5d",
  "current_entry_audit": {
    "entryVersion": 20,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-01-28",
    "lastSequenceUpdateDate": "2019-06-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "6f7707827365d1a1ffe9a48a865bb8667232a501e75af8734df730c3b24d6d20",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 579,
  "current_source_sequence_sha256": "351b6c74b4c2221103ffe06ad649dd3d536e0edd19c3a314131076b2cd6dfa5d",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 20,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A455ZIM6",
  "selected_historical_entry_version": 20,
  "selected_historical_record_sha256": "05abb0d30f13abffa1cbfd065ad8e5fdc4d8e89d823d113602496d99dc707e15",
  "selected_historical_source_sequence_length": 579,
  "selected_historical_source_sequence_sha256": "351b6c74b4c2221103ffe06ad649dd3d536e0edd19c3a314131076b2cd6dfa5d",
  "selected_historical_version": {
    "accession": "A0A455ZIM6",
    "database": "Swiss-Prot",
    "entryVersion": 20,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_03/2026_03",
    "lastReleaseDate": "02-Sep-2026",
    "name": "PPZ2_METMF",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A455ZIM6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:25:13.201191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6f7707827365d1a1ffe9a48a865bb8667232a501e75af8734df730c3b24d6d20",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":20,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-01-28\",\"lastSequenceUpdateDate\":\"2019-06-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:25:13.201191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6f7707827365d1a1ffe9a48a865bb8667232a501e75af8734df730c3b24d6d20",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Hypocreomycetidae\",\"Hypocreales\",\"Clavicipitaceae\",\"Metarhizium\",\"Metarhizium majus\"],\"scientificName\":\"Metarhizium majus (strain ARSEF 297)\",\"taxonId\":1276143}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:25:13.201191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6f7707827365d1a1ffe9a48a865bb8667232a501e75af8734df730c3b24d6d20",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30452111\",\"source\":\"PubMed\"}],\"value\":\"Pyrrolopyrazine biosynthesis cluster protein 2\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30452111\",\"source\":\"PubMed\"}],\"value\":\"MFS-type transporter ppz2\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:25:13.201191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6f7707827365d1a1ffe9a48a865bb8667232a501e75af8734df730c3b24d6d20",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":68},\"start\":{\"modifier\":\"EXACT\",\"value\":48}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:25:13.201191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6f7707827365d1a1ffe9a48a865bb8667232a501e75af8734df730c3b24d6d20",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":103},\"start\":{\"modifier\":\"EXACT\",\"value\":83}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:25:13.201191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6f7707827365d1a1ffe9a48a865bb8667232a501e75af8734df730c3b24d6d20",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":141},\"start\":{\"modifier\":\"EXACT\",\"value\":121}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:25:13.201191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6f7707827365d1a1ffe9a48a865bb8667232a501e75af8734df730c3b24d6d20",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":165},\"start\":{\"modifier\":\"EXACT\",\"value\":145}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:25:13.201191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6f7707827365d1a1ffe9a48a865bb8667232a501e75af8734df730c3b24d6d20",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":191},\"start\":{\"modifier\":\"EXACT\",\"value\":171}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:25:13.201191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6f7707827365d1a1ffe9a48a865bb8667232a501e75af8734df730c3b24d6d20",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":223},\"start\":{\"modifier\":\"EXACT\",\"value\":203}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:25:13.201191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6f7707827365d1a1ffe9a48a865bb8667232a501e75af8734df730c3b24d6d20",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":256},\"start\":{\"modifier\":\"EXACT\",\"value\":236}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:25:13.201191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6f7707827365d1a1ffe9a48a865bb8667232a501e75af8734df730c3b24d6d20",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":289},\"start\":{\"modifier\":\"EXACT\",\"value\":269}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:25:13.201191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6f7707827365d1a1ffe9a48a865bb8667232a501e75af8734df730c3b24d6d20",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":318},\"start\":{\"modifier\":\"EXACT\",\"value\":298}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-02T04:25:13.201191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6f7707827365d1a1ffe9a48a865bb8667232a501e75af8734df730c3b24d6d20",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":356},\"start\":{\"modifier\":\"EXACT\",\"value\":336}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-02T04:25:13.201191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6f7707827365d1a1ffe9a48a865bb8667232a501e75af8734df730c3b24d6d20",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":394},\"start\":{\"modifier\":\"EXACT\",\"value\":374}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/11",
  "retrieved_utc": "2026-11-02T04:25:13.201191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6f7707827365d1a1ffe9a48a865bb8667232a501e75af8734df730c3b24d6d20",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json)

```json
{
  "evidence_id": "C16",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":423},\"start\":{\"modifier\":\"EXACT\",\"value\":403}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/12",
  "retrieved_utc": "2026-11-02T04:25:13.201191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6f7707827365d1a1ffe9a48a865bb8667232a501e75af8734df730c3b24d6d20",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json)

```json
{
  "evidence_id": "C17",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":460},\"start\":{\"modifier\":\"EXACT\",\"value\":438}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/13",
  "retrieved_utc": "2026-11-02T04:25:13.201191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6f7707827365d1a1ffe9a48a865bb8667232a501e75af8734df730c3b24d6d20",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json"
}
```

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json)

```json
{
  "evidence_id": "C18",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":536},\"start\":{\"modifier\":\"EXACT\",\"value\":516}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/14",
  "retrieved_utc": "2026-11-02T04:25:13.201191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6f7707827365d1a1ffe9a48a865bb8667232a501e75af8734df730c3b24d6d20",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json"
}
```

### Evidence C19

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json)

```json
{
  "evidence_id": "C19",
  "excerpt": "{\"citation\":{\"authors\":[\"Berry D.\",\"Mace W.\",\"Rehner S.A.\",\"Grage K.\",\"Dijkwel P.P.\",\"Young C.A.\",\"Scott B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30452111\"},{\"database\":\"DOI\",\"id\":\"10.1111/1462-2920.14483\"}],\"citationType\":\"journal article\",\"firstPage\":\"928\",\"id\":\"30452111\",\"journal\":\"Environ. Microbiol.\",\"lastPage\":\"939\",\"publicationDate\":\"2019\",\"title\":\"Orthologous peramine and pyrrolopyrazine-producing biosynthetic gene clusters in Metarhizium rileyi, Metarhizium majus and Cladonia grayi.\",\"volume\":\"21\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ARSEF 297\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:25:13.201191+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6f7707827365d1a1ffe9a48a865bb8667232a501e75af8734df730c3b24d6d20",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZIM6.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H1",
  "excerpt": "ID   PPZ2_METMF              Reviewed;         579 AA.\nAC   A0A455ZIM6;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-JUN-2019, sequence version 1.\nDT   28-JAN-2026, entry version 20.\nDE   RecName: Full=MFS-type transporter ppz2 {ECO:0000303|PubMed:30452111};\nDE   AltName: Full=Pyrrolopyrazine biosynthesis cluster protein 2 {ECO:0000303|PubMed:30452111};\nGN   Name=ppz2 {ECO:0000303|PubMed:38578094};\nOS   Metarhizium majus (strain ARSEF 297).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Hypocreomycetidae; Hypocreales; Clavicipitaceae; Metarhizium;\nOC   Metarhizium majus.\nOX   NCBI_TaxID=1276143;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:15.261809+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "05abb0d30f13abffa1cbfd065ad8e5fdc4d8e89d823d113602496d99dc707e15",
  "url": "https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H2",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, AND PATHWAY.\nRC   STRAIN=ARSEF 297;\nRX   PubMed=30452111; DOI=10.1111/1462-2920.14483;\nRA   Berry D., Mace W., Rehner S.A., Grage K., Dijkwel P.P., Young C.A.,\nRA   Scott B.;\nRT   \"Orthologous peramine and pyrrolopyrazine-producing biosynthetic gene\nRT   clusters in Metarhizium rileyi, Metarhizium majus and Cladonia grayi.\";\nRL   Environ. Microbiol. 21:928-939(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:15.261809+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 14-22",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "05abb0d30f13abffa1cbfd065ad8e5fdc4d8e89d823d113602496d99dc707e15",
  "url": "https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, AND PATHWAY.\nRX   PubMed=38578094; DOI=10.1021/jacs.4c01419;\nRA   Rothchild K.W., Hagar M., Berry D., Ryan K.S.;\nRT   \"Two Iron(II), alpha-Ketoglutarate-Dependent Enzymes Encoded by the PPZ\nRT   Gene Cluster of Metarhizium majus Enable Production of 8-Hydroxyperamine.\";\nRL   J. Am. Chem. Soc. 146:10263-10267(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:15.261809+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 23-29",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "05abb0d30f13abffa1cbfd065ad8e5fdc4d8e89d823d113602496d99dc707e15",
  "url": "https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H4",
  "excerpt": "FT   TRANSMEM        48..68\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:15.261809+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 67-69",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "05abb0d30f13abffa1cbfd065ad8e5fdc4d8e89d823d113602496d99dc707e15",
  "url": "https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H5",
  "excerpt": "FT   TRANSMEM        83..103\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:15.261809+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 70-72",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "05abb0d30f13abffa1cbfd065ad8e5fdc4d8e89d823d113602496d99dc707e15",
  "url": "https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H6",
  "excerpt": "FT   TRANSMEM        121..141\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:15.261809+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 73-75",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "05abb0d30f13abffa1cbfd065ad8e5fdc4d8e89d823d113602496d99dc707e15",
  "url": "https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H7",
  "excerpt": "FT   TRANSMEM        145..165\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:15.261809+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 76-78",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "05abb0d30f13abffa1cbfd065ad8e5fdc4d8e89d823d113602496d99dc707e15",
  "url": "https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H8",
  "excerpt": "FT   TRANSMEM        171..191\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:15.261809+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 79-81",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "05abb0d30f13abffa1cbfd065ad8e5fdc4d8e89d823d113602496d99dc707e15",
  "url": "https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H9",
  "excerpt": "FT   TRANSMEM        203..223\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:15.261809+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 82-84",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "05abb0d30f13abffa1cbfd065ad8e5fdc4d8e89d823d113602496d99dc707e15",
  "url": "https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H10",
  "excerpt": "FT   TRANSMEM        236..256\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:15.261809+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 85-87",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "05abb0d30f13abffa1cbfd065ad8e5fdc4d8e89d823d113602496d99dc707e15",
  "url": "https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H11",
  "excerpt": "FT   TRANSMEM        269..289\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:15.261809+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 88-90",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "05abb0d30f13abffa1cbfd065ad8e5fdc4d8e89d823d113602496d99dc707e15",
  "url": "https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H12",
  "excerpt": "FT   TRANSMEM        298..318\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:15.261809+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 91-93",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "05abb0d30f13abffa1cbfd065ad8e5fdc4d8e89d823d113602496d99dc707e15",
  "url": "https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H13",
  "excerpt": "FT   TRANSMEM        336..356\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:15.261809+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 94-96",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "05abb0d30f13abffa1cbfd065ad8e5fdc4d8e89d823d113602496d99dc707e15",
  "url": "https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H14",
  "excerpt": "FT   TRANSMEM        374..394\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:15.261809+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 97-99",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "05abb0d30f13abffa1cbfd065ad8e5fdc4d8e89d823d113602496d99dc707e15",
  "url": "https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20"
}
```

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H15",
  "excerpt": "FT   TRANSMEM        403..423\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:15.261809+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 100-102",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "05abb0d30f13abffa1cbfd065ad8e5fdc4d8e89d823d113602496d99dc707e15",
  "url": "https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20"
}
```

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H16",
  "excerpt": "FT   TRANSMEM        438..460\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:15.261809+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 103-105",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "05abb0d30f13abffa1cbfd065ad8e5fdc4d8e89d823d113602496d99dc707e15",
  "url": "https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20"
}
```

### Evidence H17

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H17",
  "excerpt": "FT   TRANSMEM        516..536\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:15.261809+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 106-108",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "05abb0d30f13abffa1cbfd065ad8e5fdc4d8e89d823d113602496d99dc707e15",
  "url": "https://rest.uniprot.org/unisave/A0A455ZIM6?format=txt&versions=20"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 20. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
