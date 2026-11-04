# transmembrane_0133

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0133.txt)

**Task:** `transmembrane`  
**Expected answer:** **B** — 139..159; 176..196; 247..267; 272..292; 297..317

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MESMVNNLWSSWDTLSQATASTGGDMDAASVASKQSPQESKMAASSMIWSSFSEPQKTPPTKRASSSFFDDMFTSSKDHSTTLTDKMFERFLSMALPTTTTQDGEELQSILERIEMQKSRPQLSLNVMSKNAIQLLSRLSVPFVLIDQVIIIFSWSKPLYTLTFLNVATLLILKPILLLSLPFFYTCFEIIVPAYMKRHPPDKHTILQNRNPIPAEGPSVSHVDVPRPVPELSREFVLNSTDLQNHMLLYVMSYDFVTSLIVKYLYFKDENITIFIFVALLTSGTLLTLFGAQVLSAMLPFIKVTLSVGLWAATIAMHPNYRSTLLDMLYSEDTRLRLLMMSNRLELWLNKELNLREQKEVKETEIFELQHLDPETHNWQLICFSSDPYPANSHARLNNLPLLGTLHLSQVKPPEGWKFVDVETAVNTRSVDGWLLDLTPEGWIKENFLNETMDIDEDEKWCYDLVTKFSYQAGLTTNEKKTRGEVRRRRWIRYCVRDIWDEDDQMEETVAHRRNKSMESSNSLHPVKSIDSVDG

[Multiple Choices]
A. 281..301
B. 139..159; 176..196; 247..267; 272..292; 297..317
C. 135..157; 176..196; 247..267; 272..292; 297..317
D. 139..159; 176..196; 247..267; 297..317
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

> The sequence-matched UniProt record annotates all five intervals in B as helical transmembrane regions. These annotations are computational (ECO:0000255), so they support the key as a prediction rather than independent experimental confirmation.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has several roughly 20-residue hydrophobic stretches consistent with membrane-spanning helices, supporting the multi-region choice over options that omit spans. For the differing first interval, B starts nearer the strongly hydrophobic stretch and excludes an upstream arginine included by C; it also extends across additional hydrophobic residues. This makes B a credible sequence-based preference, though not a definitive boundary measurement.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable hydropathy and membrane-helix patterns provide a meaningful basis for favoring B among these alternatives. Exact helix boundaries remain uncertain from sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The nearby boundary alternative in C is plausible, but B is better supported by the local sequence composition; the other choices omit or misrepresent predicted spans.


### Important caveats

- The supplied sequence supports approximate membrane-helix locations, but exact endpoints are inherently less certain than the presence of hydrophobic spans.
- The reviewer-only annotation is computational, not evidence of experimental determination.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has several roughly 20-residue hydrophobic stretches consistent with membrane-spanning helices, supporting the multi-region choice over options that omit spans. For the differing first interval, B starts nearer the strongly hydrophobic stretch and excludes an upstream arginine included by C; it also extends across additional hydrophobic residues. This makes B a credible sequence-based preference, though not a definitive boundary measurement.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable hydropathy and membrane-helix patterns provide a meaningful basis for favoring B among these alternatives. Exact helix boundaries remain uncertain from sequence alone."
  },
  "case_id": "transmembrane_0133",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates all five intervals in B as helical transmembrane regions. These annotations are computational (ECO:0000255), so they support the key as a prediction rather than independent experimental confirmation."
  },
  "important_caveats": [
    "The supplied sequence supports approximate membrane-helix locations, but exact endpoints are inherently less certain than the presence of hydrophobic spans.",
    "The reviewer-only annotation is computational, not evidence of experimental determination."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The nearby boundary alternative in C is plausible, but B is better supported by the local sequence composition; the other choices omit or misrepresent predicted spans."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0133",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates all five intervals in B as helical transmembrane regions. These annotations are computational (ECO:0000255), so they support the key as a prediction rather than independent experimental confirmation.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has several roughly 20-residue hydrophobic stretches consistent with membrane-spanning helices, supporting the multi-region choice over options that omit spans. For the differing first interval, B starts nearer the strongly hydrophobic stretch and excludes an upstream arginine included by C; it also extends across additional hydrophobic residues. This makes B a credible sequence-based preference, though not a definitive boundary measurement.",
    "missing_item_specific_fact": "",
    "reason": "Transferable hydropathy and membrane-helix patterns provide a meaningful basis for favoring B among these alternatives. Exact helix boundaries remain uncertain from sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The nearby boundary alternative in C is plausible, but B is better supported by the local sequence composition; the other choices omit or misrepresent predicted spans."
  },
  "important_caveats": [
    "The supplied sequence supports approximate membrane-helix locations, but exact endpoints are inherently less certain than the presence of hydrophobic spans.",
    "The reviewer-only annotation is computational, not evidence of experimental determination."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The expected answer B (139..159; 176..196; 247..267; 272..292; 297..317) matches exactly the five transmembrane helix annotations in UniProt entry W1QL91 (PEX29_OGAPD). All five regions are annotated with evidence code ECO:0000255 (similarity to other proteins), indicating computational predictions rather than experimental data. The sequence SHA256 matches the benchmark input. The annotation is the recorded database answer, so the key is supported by the source, though the underlying evidence is computational inference, not experimental validation.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Three transferable principles distinguish B from the alternatives. (1) B vs C: The first TM region starts at 139 (B) or 135 (C). Residue 138 is Arginine (R), a positively charged residue that is energetically prohibitive within a lipid-bilayer-spanning alpha-helix. Residue 137 is Serine (polar). Starting at 139 (Leu) avoids these, while starting at 135 would place a charged Arg inside the membrane. This is a well-established biophysical principle applicable to any TM helix. (2) B vs D: The difference is the inclusion of region 272-292 (ITIFIFVAL LTSGTLLTLFGA). Computing Kyte-Doolittle hydrophobicity for this 21-residue segment yields an average of approximately 2.1, which is actually HIGHER than the annotated TM region 247-267 (average ~1.3, which contains Asp and Lys). If 247-267 qualifies as a TM helix, then 272-292 should certainly qualify. Additionally, the spacing pattern—21-residue helices separated by 4-residue loops (268-271, 293-296)—is a hallmark of multi-pass membrane proteins and strongly supports the inclusion of 272-292. (3) A (single TM at 281-301) is inconsistent with the multiple hydrophobic stretches visible throughout the sequence and with the general architecture of multi-pass membrane proteins.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model with knowledge of TM helix biophysics (charged residues are excluded from the hydrophobic core), hydrophobicity scales, and the regular helix-loop spacing motif in multi-pass membrane proteins can meaningfully distinguish B from C (charged Arg at 138) and from D (272-292 is more hydrophobic than other TM regions in the same sequence and fits the spacing pattern). No target-specific database lookup is required.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While the B vs D boundary is somewhat close in absolute hydrophobicity terms, the comparative argument within the protein (272-292 is more hydrophobic than the already-included 247-267) and the regular spacing pattern provide a clear basis for inclusion. The B vs C distinction is unambiguous due to the charged Arg at position 138. A is trivially excluded. No two options are equally defensible.


### Important caveats

- All five TM annotations carry evidence code ECO:0000255 (similarity to other proteins), meaning they are computational predictions, not experimentally validated. The expected answer reflects the database annotation, which is appropriate for a prediction task but does not constitute experimental proof.
- The exact boundaries of TM helices are inherently fuzzy (±3-5 residues); the 4-residue difference between options B and C at the first TM start is within typical prediction uncertainty, but the charged-residue argument at position 138 resolves this in favor of B.
- The reviewer-only evidence confirms sequence identity (SHA256 match) and that the UniProt entry W1QL91 matches the benchmark sequence, but the model was not given the protein name, organism, or accession.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Three transferable principles distinguish B from the alternatives. (1) B vs C: The first TM region starts at 139 (B) or 135 (C). Residue 138 is Arginine (R), a positively charged residue that is energetically prohibitive within a lipid-bilayer-spanning alpha-helix. Residue 137 is Serine (polar). Starting at 139 (Leu) avoids these, while starting at 135 would place a charged Arg inside the membrane. This is a well-established biophysical principle applicable to any TM helix. (2) B vs D: The difference is the inclusion of region 272-292 (ITIFIFVAL LTSGTLLTLFGA). Computing Kyte-Doolittle hydrophobicity for this 21-residue segment yields an average of approximately 2.1, which is actually HIGHER than the annotated TM region 247-267 (average ~1.3, which contains Asp and Lys). If 247-267 qualifies as a TM helix, then 272-292 should certainly qualify. Additionally, the spacing pattern—21-residue helices separated by 4-residue loops (268-271, 293-296)—is a hallmark of multi-pass membrane proteins and strongly supports the inclusion of 272-292. (3) A (single TM at 281-301) is inconsistent with the multiple hydrophobic stretches visible throughout the sequence and with the general architecture of multi-pass membrane proteins.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model with knowledge of TM helix biophysics (charged residues are excluded from the hydrophobic core), hydrophobicity scales, and the regular helix-loop spacing motif in multi-pass membrane proteins can meaningfully distinguish B from C (charged Arg at 138) and from D (272-292 is more hydrophobic than other TM regions in the same sequence and fits the spacing pattern). No target-specific database lookup is required."
  },
  "case_id": "transmembrane_0133",
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
    "reason": "The expected answer B (139..159; 176..196; 247..267; 272..292; 297..317) matches exactly the five transmembrane helix annotations in UniProt entry W1QL91 (PEX29_OGAPD). All five regions are annotated with evidence code ECO:0000255 (similarity to other proteins), indicating computational predictions rather than experimental data. The sequence SHA256 matches the benchmark input. The annotation is the recorded database answer, so the key is supported by the source, though the underlying evidence is computational inference, not experimental validation."
  },
  "important_caveats": [
    "All five TM annotations carry evidence code ECO:0000255 (similarity to other proteins), meaning they are computational predictions, not experimentally validated. The expected answer reflects the database annotation, which is appropriate for a prediction task but does not constitute experimental proof.",
    "The exact boundaries of TM helices are inherently fuzzy (±3-5 residues); the 4-residue difference between options B and C at the first TM start is within typical prediction uncertainty, but the charged-residue argument at position 138 resolves this in favor of B.",
    "The reviewer-only evidence confirms sequence identity (SHA256 match) and that the UniProt entry W1QL91 matches the benchmark sequence, but the model was not given the protein name, organism, or accession."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the B vs D boundary is somewhat close in absolute hydrophobicity terms, the comparative argument within the protein (272-292 is more hydrophobic than the already-included 247-267) and the regular spacing pattern provide a clear basis for inclusion. The B vs C distinction is unambiguous due to the charged Arg at position 138. A is trivially excluded. No two options are equally defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0133",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The expected answer B (139..159; 176..196; 247..267; 272..292; 297..317) matches exactly the five transmembrane helix annotations in UniProt entry W1QL91 (PEX29_OGAPD). All five regions are annotated with evidence code ECO:0000255 (similarity to other proteins), indicating computational predictions rather than experimental data. The sequence SHA256 matches the benchmark input. The annotation is the recorded database answer, so the key is supported by the source, though the underlying evidence is computational inference, not experimental validation.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "H3", "H4", "H5", "H6", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Three transferable principles distinguish B from the alternatives. (1) B vs C: The first TM region starts at 139 (B) or 135 (C). Residue 138 is Arginine (R), a positively charged residue that is energetically prohibitive within a lipid-bilayer-spanning alpha-helix. Residue 137 is Serine (polar). Starting at 139 (Leu) avoids these, while starting at 135 would place a charged Arg inside the membrane. This is a well-established biophysical principle applicable to any TM helix. (2) B vs D: The difference is the inclusion of region 272-292 (ITIFIFVAL LTSGTLLTLFGA). Computing Kyte-Doolittle hydrophobicity for this 21-residue segment yields an average of approximately 2.1, which is actually HIGHER than the annotated TM region 247-267 (average ~1.3, which contains Asp and Lys). If 247-267 qualifies as a TM helix, then 272-292 should certainly qualify. Additionally, the spacing pattern—21-residue helices separated by 4-residue loops (268-271, 293-296)—is a hallmark of multi-pass membrane proteins and strongly supports the inclusion of 272-292. (3) A (single TM at 281-301) is inconsistent with the multiple hydrophobic stretches visible throughout the sequence and with the general architecture of multi-pass membrane proteins.",
    "missing_item_specific_fact": "",
    "reason": "A model with knowledge of TM helix biophysics (charged residues are excluded from the hydrophobic core), hydrophobicity scales, and the regular helix-loop spacing motif in multi-pass membrane proteins can meaningfully distinguish B from C (charged Arg at 138) and from D (272-292 is more hydrophobic than other TM regions in the same sequence and fits the spacing pattern). No target-specific database lookup is required."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the B vs D boundary is somewhat close in absolute hydrophobicity terms, the comparative argument within the protein (272-292 is more hydrophobic than the already-included 247-267) and the regular spacing pattern provide a clear basis for inclusion. The B vs C distinction is unambiguous due to the charged Arg at position 138. A is trivially excluded. No two options are equally defensible."
  },
  "important_caveats": [
    "All five TM annotations carry evidence code ECO:0000255 (similarity to other proteins), meaning they are computational predictions, not experimentally validated. The expected answer reflects the database annotation, which is appropriate for a prediction task but does not constitute experimental proof.",
    "The exact boundaries of TM helices are inherently fuzzy (±3-5 residues); the 4-residue difference between options B and C at the first TM start is within typical prediction uncertainty, but the charged-residue argument at position 138 resolves this in favor of B.",
    "The reviewer-only evidence confirms sequence identity (SHA256 match) and that the UniProt entry W1QL91 matches the benchmark sequence, but the model was not given the protein name, organism, or accession."
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
  "benchmark_sequence_length": 535,
  "benchmark_sequence_sha256": "74b2e779608146cca51114d9d1190337b5a9ad8a1f8c3db747e0491092d1ea4d",
  "current_entry_audit": {
    "entryVersion": 43,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2014-03-19",
    "sequenceVersion": 1
  },
  "current_record_sha256": "82521092a67ef997abdc31799f3577764b26227f0c47f2c09c813128fc009f23",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 535,
  "current_source_sequence_sha256": "74b2e779608146cca51114d9d1190337b5a9ad8a1f8c3db747e0491092d1ea4d",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 41,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "W1QL91",
  "selected_historical_entry_version": 41,
  "selected_historical_record_sha256": "2b59cad336a5f0f970c7aa6c93d04cd1ad5885189ae5de312c6383b733a569b7",
  "selected_historical_source_sequence_length": 535,
  "selected_historical_source_sequence_sha256": "74b2e779608146cca51114d9d1190337b5a9ad8a1f8c3db747e0491092d1ea4d",
  "selected_historical_version": {
    "accession": "W1QL91",
    "database": "Swiss-Prot",
    "entryVersion": 41,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "PEX29_OGAPD",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QL91.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"W1QL91\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:34:09.919107+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "82521092a67ef997abdc31799f3577764b26227f0c47f2c09c813128fc009f23",
  "url": "https://rest.uniprot.org/uniprotkb/W1QL91.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QL91.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":43,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2014-03-19\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:34:09.919107+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "82521092a67ef997abdc31799f3577764b26227f0c47f2c09c813128fc009f23",
  "url": "https://rest.uniprot.org/uniprotkb/W1QL91.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QL91.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Yeast\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Saccharomycotina\",\"Pichiomycetes\",\"Pichiales\",\"Pichiaceae\",\"Ogataea\"],\"scientificName\":\"Ogataea parapolymorpha (strain ATCC 26012 / BCRC 20466 / JCM 22074 / NRRL Y-7560 / DL-1)\",\"synonyms\":[\"Hansenula polymorpha\"],\"taxonId\":871575}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:34:09.919107+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "82521092a67ef997abdc31799f3577764b26227f0c47f2c09c813128fc009f23",
  "url": "https://rest.uniprot.org/uniprotkb/W1QL91.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QL91.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Peroxin-29\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32665322\",\"source\":\"PubMed\"}],\"value\":\"Peroxisomal membrane protein PEX29\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:34:09.919107+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "82521092a67ef997abdc31799f3577764b26227f0c47f2c09c813128fc009f23",
  "url": "https://rest.uniprot.org/uniprotkb/W1QL91.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QL91.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":159},\"start\":{\"modifier\":\"EXACT\",\"value\":139}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:34:09.919107+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "82521092a67ef997abdc31799f3577764b26227f0c47f2c09c813128fc009f23",
  "url": "https://rest.uniprot.org/uniprotkb/W1QL91.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QL91.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":196},\"start\":{\"modifier\":\"EXACT\",\"value\":176}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:34:09.919107+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "82521092a67ef997abdc31799f3577764b26227f0c47f2c09c813128fc009f23",
  "url": "https://rest.uniprot.org/uniprotkb/W1QL91.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QL91.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":267},\"start\":{\"modifier\":\"EXACT\",\"value\":247}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:34:09.919107+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "82521092a67ef997abdc31799f3577764b26227f0c47f2c09c813128fc009f23",
  "url": "https://rest.uniprot.org/uniprotkb/W1QL91.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QL91.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":292},\"start\":{\"modifier\":\"EXACT\",\"value\":272}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:34:09.919107+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "82521092a67ef997abdc31799f3577764b26227f0c47f2c09c813128fc009f23",
  "url": "https://rest.uniprot.org/uniprotkb/W1QL91.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QL91.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":317},\"start\":{\"modifier\":\"EXACT\",\"value\":297}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:34:09.919107+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "82521092a67ef997abdc31799f3577764b26227f0c47f2c09c813128fc009f23",
  "url": "https://rest.uniprot.org/uniprotkb/W1QL91.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QL91.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Wu F.\",\"de Boer R.\",\"Krikken A.M.\",\"Aksit A.\",\"Bordin N.\",\"Devos D.P.\",\"van der Klei I.J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"32665322\"},{\"database\":\"DOI\",\"id\":\"10.1242/jcs.246983\"}],\"citationType\":\"journal article\",\"firstPage\":\"0\",\"id\":\"32665322\",\"journal\":\"J. Cell Sci.\",\"lastPage\":\"0\",\"publicationDate\":\"2020\",\"title\":\"Pex24 and Pex32 are required to tether peroxisomes to the ER for organelle biogenesis, positioning and segregation in yeast.\",\"volume\":\"133\"},\"referenceNumber\":2,\"referencePositions\":[\"DISRUPTION PHENOTYPE\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:34:09.919107+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "82521092a67ef997abdc31799f3577764b26227f0c47f2c09c813128fc009f23",
  "url": "https://rest.uniprot.org/uniprotkb/W1QL91.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QL91?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H1",
  "excerpt": "ID   PEX29_OGAPD             Reviewed;         535 AA.\nAC   W1QL91;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   19-MAR-2014, sequence version 1.\nDT   28-JAN-2026, entry version 41.\nDE   RecName: Full=Peroxisomal membrane protein PEX29 {ECO:0000303|PubMed:32665322};\nDE   AltName: Full=Peroxin-29 {ECO:0000305};\nGN   Name=PEX29 {ECO:0000303|PubMed:32665322}; ORFNames=HPODL_00080;\nOS   Ogataea parapolymorpha (strain ATCC 26012 / BCRC 20466 / JCM 22074 / NRRL\nOS   Y-7560 / DL-1) (Yeast) (Hansenula polymorpha).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Saccharomycotina; Pichiomycetes;\nOC   Pichiales; Pichiaceae; Ogataea.\nOX   NCBI_TaxID=871575;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:13.232116+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2b59cad336a5f0f970c7aa6c93d04cd1ad5885189ae5de312c6383b733a569b7",
  "url": "https://rest.uniprot.org/unisave/W1QL91?format=txt&versions=41"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QL91?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   DISRUPTION PHENOTYPE, AND SUBCELLULAR LOCATION.\nRX   PubMed=32665322; DOI=10.1242/jcs.246983;\nRA   Wu F., de Boer R., Krikken A.M., Aksit A., Bordin N., Devos D.P.,\nRA   van der Klei I.J.;\nRT   \"Pex24 and Pex32 are required to tether peroxisomes to the ER for organelle\nRT   biogenesis, positioning and segregation in yeast.\";\nRL   J. Cell Sci. 133:0-0(2020).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:13.232116+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 24-31",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2b59cad336a5f0f970c7aa6c93d04cd1ad5885189ae5de312c6383b733a569b7",
  "url": "https://rest.uniprot.org/unisave/W1QL91?format=txt&versions=41"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QL91?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H3",
  "excerpt": "FT   TRANSMEM        139..159\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:13.232116+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 84-86",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2b59cad336a5f0f970c7aa6c93d04cd1ad5885189ae5de312c6383b733a569b7",
  "url": "https://rest.uniprot.org/unisave/W1QL91?format=txt&versions=41"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QL91?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H4",
  "excerpt": "FT   TRANSMEM        176..196\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:13.232116+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 87-89",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2b59cad336a5f0f970c7aa6c93d04cd1ad5885189ae5de312c6383b733a569b7",
  "url": "https://rest.uniprot.org/unisave/W1QL91?format=txt&versions=41"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QL91?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H5",
  "excerpt": "FT   TRANSMEM        247..267\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:13.232116+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 90-92",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2b59cad336a5f0f970c7aa6c93d04cd1ad5885189ae5de312c6383b733a569b7",
  "url": "https://rest.uniprot.org/unisave/W1QL91?format=txt&versions=41"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QL91?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H6",
  "excerpt": "FT   TRANSMEM        272..292\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:13.232116+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 93-95",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2b59cad336a5f0f970c7aa6c93d04cd1ad5885189ae5de312c6383b733a569b7",
  "url": "https://rest.uniprot.org/unisave/W1QL91?format=txt&versions=41"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QL91?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H7",
  "excerpt": "FT   TRANSMEM        297..317\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:34:13.232116+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 96-98",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2b59cad336a5f0f970c7aa6c93d04cd1ad5885189ae5de312c6383b733a569b7",
  "url": "https://rest.uniprot.org/unisave/W1QL91?format=txt&versions=41"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 133. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
