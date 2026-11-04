# motif_position_0050

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/motif_position_0050.txt)

**Task:** `motif_position`  
**Expected answer:** **A** — 9..17

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MLLNSKRGQVSIEMLILILAVLLSGTIFAAHMTKNTVSHDEISDVKKQTFKSFLGSVEGSTASSLPEKISEEDTSPEEDTIPEEDTSPEEDTIPEEDTIPEEDTSTEIPIGKNVKIYNLPIKEEKQNWFLDILNTALDRISAILDGFFSLFGLDLFNNDEIIPNILVKDFEGNRIPLSFDWERLSYTTDWFYAKEIEFTGDSSAKYSKLDLFRIFPIYSYSDTTFRITDLSYNLTYDVPPSTAKKTITITSNIPEGIKCKVTYKIGGILTGDYYTLEIDEKTSSNKYNNVNIAFE

[Multiple Choices]
A. 9..17
B. 332..335
C. 316..323
D. 205..208
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Motif Position Prediction, which is to identify the specific positions of a conserved motif within a protein sequence. A motif is a short, recurring pattern in protein sequences that is often associated with a specific function or structure. Based on the provided protein sequence, you will need to determine the start and end positions of the motif.. The inputs provided by the user for this task include:

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

> The sequence-matched historical UniProt record annotates a motif at 9..17 with consensus QXSXEXXXL, matching choice A. This supports the key as a database annotation, not as experimental validation.

Citations as saved: [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> The prompt does not identify the motif or give its consensus or a homolog alignment showing which pattern is conserved; that information is needed to select its location.


**Reason**

> The N-terminal hydrophobic segment is recognizable, but that alone does not establish which conserved motif the task means or distinguish its annotated position from another in-range candidate. Choices B and C are outside the supplied sequence, but that still does not establish the motif location.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The prompt omits the motif identity, making the task dependent on an unstated annotation; the supplied evidence supports A, but does not establish another choice as a defensible annotated location.


### Important caveats

- The historical annotation is sequence-matched and predates the approximate benchmark cutoff, but the author's exact source snapshot is unknown.
- The annotation carries evidence code ECO:0000305; the supplied evidence does not establish experimental validation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The prompt does not identify the motif or give its consensus or a homolog alignment showing which pattern is conserved; that information is needed to select its location.",
    "reason": "The N-terminal hydrophobic segment is recognizable, but that alone does not establish which conserved motif the task means or distinguish its annotated position from another in-range candidate. Choices B and C are outside the supplied sequence, but that still does not establish the motif location."
  },
  "case_id": "motif_position_0050",
  "expected_answer_check": {
    "evidence_ids": [
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record annotates a motif at 9..17 with consensus QXSXEXXXL, matching choice A. This supports the key as a database annotation, not as experimental validation."
  },
  "important_caveats": [
    "The historical annotation is sequence-matched and predates the approximate benchmark cutoff, but the author's exact source snapshot is unknown.",
    "The annotation carries evidence code ECO:0000305; the supplied evidence does not establish experimental validation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The prompt omits the motif identity, making the task dependent on an unstated annotation; the supplied evidence supports A, but does not establish another choice as a defensible annotated location."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "motif_position_0050",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record annotates a motif at 9..17 with consensus QXSXEXXXL, matching choice A. This supports the key as a database annotation, not as experimental validation.",
    "evidence_ids": ["H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "The prompt does not identify the motif or give its consensus or a homolog alignment showing which pattern is conserved; that information is needed to select its location.",
    "reason": "The N-terminal hydrophobic segment is recognizable, but that alone does not establish which conserved motif the task means or distinguish its annotated position from another in-range candidate. Choices B and C are outside the supplied sequence, but that still does not establish the motif location."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The prompt omits the motif identity, making the task dependent on an unstated annotation; the supplied evidence supports A, but does not establish another choice as a defensible annotated location."
  },
  "important_caveats": [
    "The historical annotation is sequence-matched and predates the approximate benchmark cutoff, but the author's exact source snapshot is unknown.",
    "The annotation carries evidence code ECO:0000305; the supplied evidence does not establish experimental validation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (evidence C6/H3) explicitly records a MOTIF at positions 9..17 with the pattern 'QXSXEXXXL' (ECO:0000305, inferred by curator). The sequence at positions 9-17 is QVSIEMLIL, which perfectly matches Q-X-S-X-E-X-X-X-L. The sequence is confirmed to be 295 AA and matches the source entry.

Citations as saved: [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein displays a clear signal peptide (hydrophobic stretch ~residues 12-30: LILILAVLLSGTIFAAHMTK) followed by a processing site, identifying it as a secreted pilin-type protein. Archaeal type IV pilins are well-known to carry conserved N-terminal motifs immediately after the signal peptide cleavage site. The QXSXEXXXL pattern (Q-V-S-I-E-M-L-I-L at positions 9-17) is a recognizable conserved motif in this family. Options B (332..335) and C (316..323) are beyond the 295-residue sequence length and are trivially eliminated. Option D (205..208) falls in the middle of the mature pilin body, a location inconsistent with the known N-terminal conservation pattern of pilin motifs. Thus, family-level knowledge of pilin architecture (conserved N-terminal motifs) plus the visible QXSXEXXXL pattern in the sequence distinguishes A from the remaining viable option D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the pilin signal peptide, apply the general principle that archaeal pilins harbor conserved N-terminal motifs, spot the QXSXEXXXL pattern at positions 9-17, and eliminate out-of-range options B/C and the mid-protein option D based on pilin structural biology. This is transferable family-level inference, not a lookup of this specific entry's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B and C are beyond the 295-residue sequence, leaving only A and D. The N-terminal location and recognizable motif pattern make A clearly preferable over D for a pilin protein.


### Important caveats

- The motif annotation uses evidence code ECO:0000305 (inferred by curator), meaning it is a computational/curatorial assignment rather than experimentally validated.
- The QXSXEXXXL motif is a family-level conserved pattern in archaeal pilins; its specific definition as a 'motif' is a curation choice visible in UniProt.
- Options B and C being out of range makes them trivially eliminable, reducing the effective question to a binary A vs D choice.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein displays a clear signal peptide (hydrophobic stretch ~residues 12-30: LILILAVLLSGTIFAAHMTK) followed by a processing site, identifying it as a secreted pilin-type protein. Archaeal type IV pilins are well-known to carry conserved N-terminal motifs immediately after the signal peptide cleavage site. The QXSXEXXXL pattern (Q-V-S-I-E-M-L-I-L at positions 9-17) is a recognizable conserved motif in this family. Options B (332..335) and C (316..323) are beyond the 295-residue sequence length and are trivially eliminated. Option D (205..208) falls in the middle of the mature pilin body, a location inconsistent with the known N-terminal conservation pattern of pilin motifs. Thus, family-level knowledge of pilin architecture (conserved N-terminal motifs) plus the visible QXSXEXXXL pattern in the sequence distinguishes A from the remaining viable option D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the pilin signal peptide, apply the general principle that archaeal pilins harbor conserved N-terminal motifs, spot the QXSXEXXXL pattern at positions 9-17, and eliminate out-of-range options B/C and the mid-protein option D based on pilin structural biology. This is transferable family-level inference, not a lookup of this specific entry's annotation."
  },
  "case_id": "motif_position_0050",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C6/H3) explicitly records a MOTIF at positions 9..17 with the pattern 'QXSXEXXXL' (ECO:0000305, inferred by curator). The sequence at positions 9-17 is QVSIEMLIL, which perfectly matches Q-X-S-X-E-X-X-X-L. The sequence is confirmed to be 295 AA and matches the source entry."
  },
  "important_caveats": [
    "The motif annotation uses evidence code ECO:0000305 (inferred by curator), meaning it is a computational/curatorial assignment rather than experimentally validated.",
    "The QXSXEXXXL motif is a family-level conserved pattern in archaeal pilins; its specific definition as a 'motif' is a curation choice visible in UniProt.",
    "Options B and C being out of range makes them trivially eliminable, reducing the effective question to a binary A vs D choice."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and C are beyond the 295-residue sequence, leaving only A and D. The N-terminal location and recognizable motif pattern make A clearly preferable over D for a pilin protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "motif_position_0050",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C6/H3) explicitly records a MOTIF at positions 9..17 with the pattern 'QXSXEXXXL' (ECO:0000305, inferred by curator). The sequence at positions 9-17 is QVSIEMLIL, which perfectly matches Q-X-S-X-E-X-X-X-L. The sequence is confirmed to be 295 AA and matches the source entry.",
    "evidence_ids": ["C6", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein displays a clear signal peptide (hydrophobic stretch ~residues 12-30: LILILAVLLSGTIFAAHMTK) followed by a processing site, identifying it as a secreted pilin-type protein. Archaeal type IV pilins are well-known to carry conserved N-terminal motifs immediately after the signal peptide cleavage site. The QXSXEXXXL pattern (Q-V-S-I-E-M-L-I-L at positions 9-17) is a recognizable conserved motif in this family. Options B (332..335) and C (316..323) are beyond the 295-residue sequence length and are trivially eliminated. Option D (205..208) falls in the middle of the mature pilin body, a location inconsistent with the known N-terminal conservation pattern of pilin motifs. Thus, family-level knowledge of pilin architecture (conserved N-terminal motifs) plus the visible QXSXEXXXL pattern in the sequence distinguishes A from the remaining viable option D.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the pilin signal peptide, apply the general principle that archaeal pilins harbor conserved N-terminal motifs, spot the QXSXEXXXL pattern at positions 9-17, and eliminate out-of-range options B/C and the mid-protein option D based on pilin structural biology. This is transferable family-level inference, not a lookup of this specific entry's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and C are beyond the 295-residue sequence, leaving only A and D. The N-terminal location and recognizable motif pattern make A clearly preferable over D for a pilin protein."
  },
  "important_caveats": [
    "The motif annotation uses evidence code ECO:0000305 (inferred by curator), meaning it is a computational/curatorial assignment rather than experimentally validated.",
    "The QXSXEXXXL motif is a family-level conserved pattern in archaeal pilins; its specific definition as a 'motif' is a curation choice visible in UniProt.",
    "Options B and C being out of range makes them trivially eliminable, reducing the effective question to a binary A vs D choice."
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
  "benchmark_sequence_length": 295,
  "benchmark_sequence_sha256": "065d2f938129ed7993f2c85bb3e37d96c2a059ca6ef3081a985f035a35e84ef5",
  "current_entry_audit": {
    "entryVersion": 74,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2004-07-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "f65d8b6a81e43709b362bb1aff50762f04a31bac8e1a1b7b6ba493af5a50bfb2",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 295,
  "current_source_sequence_sha256": "065d2f938129ed7993f2c85bb3e37d96c2a059ca6ef3081a985f035a35e84ef5",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 73,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q6LZM3",
  "selected_historical_entry_version": 73,
  "selected_historical_record_sha256": "17589c2d3cb1884d286af6f6d4efa07afc0285ac6c6788da5a9fdf05c0f9061a",
  "selected_historical_source_sequence_length": 295,
  "selected_historical_source_sequence_sha256": "065d2f938129ed7993f2c85bb3e37d96c2a059ca6ef3081a985f035a35e84ef5",
  "selected_historical_version": {
    "accession": "Q6LZM3",
    "database": "Swiss-Prot",
    "entryVersion": 73,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "Y601_METMP",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LZM3.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q6LZM3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:31:38.071255+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f65d8b6a81e43709b362bb1aff50762f04a31bac8e1a1b7b6ba493af5a50bfb2",
  "url": "https://rest.uniprot.org/uniprotkb/Q6LZM3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LZM3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":74,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2004-07-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:31:38.071255+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f65d8b6a81e43709b362bb1aff50762f04a31bac8e1a1b7b6ba493af5a50bfb2",
  "url": "https://rest.uniprot.org/uniprotkb/Q6LZM3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LZM3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Archaea\",\"Methanobacteriati\",\"Methanobacteriota\",\"Methanomada group\",\"Methanococci\",\"Methanococcales\",\"Methanococcaceae\",\"Methanococcus\"],\"scientificName\":\"Methanococcus maripaludis (strain DSM 14266 / JCM 13030 / NBRC 101832 / S2 / LL)\",\"taxonId\":267377}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:31:38.071255+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f65d8b6a81e43709b362bb1aff50762f04a31bac8e1a1b7b6ba493af5a50bfb2",
  "url": "https://rest.uniprot.org/uniprotkb/Q6LZM3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LZM3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"flag\":\"Precursor\",\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Probable minor pilin MMP0601\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:31:38.071255+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f65d8b6a81e43709b362bb1aff50762f04a31bac8e1a1b7b6ba493af5a50bfb2",
  "url": "https://rest.uniprot.org/uniprotkb/Q6LZM3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LZM3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Disordered\",\"evidences\":[{\"evidenceCode\":\"ECO:0000256\",\"id\":\"MobiDB-lite\",\"source\":\"SAM\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":105},\"start\":{\"modifier\":\"EXACT\",\"value\":58}},\"type\":\"Region\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:31:38.071255+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f65d8b6a81e43709b362bb1aff50762f04a31bac8e1a1b7b6ba493af5a50bfb2",
  "url": "https://rest.uniprot.org/uniprotkb/Q6LZM3.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LZM3.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"QXSXEXXXL\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":17},\"start\":{\"modifier\":\"EXACT\",\"value\":9}},\"type\":\"Motif\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:31:38.071255+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f65d8b6a81e43709b362bb1aff50762f04a31bac8e1a1b7b6ba493af5a50bfb2",
  "url": "https://rest.uniprot.org/uniprotkb/Q6LZM3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6LZM3?format=txt&versions=73)

```json
{
  "entry_version": 73,
  "evidence_id": "H1",
  "excerpt": "ID   Y601_METMP              Reviewed;         295 AA.\nAC   Q6LZM3;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-JUL-2004, sequence version 1.\nDT   28-JAN-2026, entry version 73.\nDE   RecName: Full=Probable minor pilin MMP0601 {ECO:0000305};\nDE   Flags: Precursor;\nGN   OrderedLocusNames=MMP0601 {ECO:0000312|EMBL:CAF30157.1};\nOS   Methanococcus maripaludis (strain DSM 14266 / JCM 13030 / NBRC 101832 / S2\nOS   / LL).\nOC   Archaea; Methanobacteriati; Methanobacteriota; Methanomada group;\nOC   Methanococci; Methanococcales; Methanococcaceae; Methanococcus.\nOX   NCBI_TaxID=267377;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:40.632602+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "17589c2d3cb1884d286af6f6d4efa07afc0285ac6c6788da5a9fdf05c0f9061a",
  "url": "https://rest.uniprot.org/unisave/Q6LZM3?format=txt&versions=73"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6LZM3?format=txt&versions=73)

```json
{
  "entry_version": 73,
  "evidence_id": "H2",
  "excerpt": "FT   REGION          58..105\nFT                   /note=\"Disordered\"\nFT                   /evidence=\"ECO:0000256|SAM:MobiDB-lite\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:40.632602+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 76-78",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "17589c2d3cb1884d286af6f6d4efa07afc0285ac6c6788da5a9fdf05c0f9061a",
  "url": "https://rest.uniprot.org/unisave/Q6LZM3?format=txt&versions=73"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6LZM3?format=txt&versions=73)

```json
{
  "entry_version": 73,
  "evidence_id": "H3",
  "excerpt": "FT   MOTIF           9..17\nFT                   /note=\"QXSXEXXXL\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:40.632602+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 79-81",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "17589c2d3cb1884d286af6f6d4efa07afc0285ac6c6788da5a9fdf05c0f9061a",
  "url": "https://rest.uniprot.org/unisave/Q6LZM3?format=txt&versions=73"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/motif_position.json), zero-based source row 50. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
