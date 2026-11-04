# transmembrane_0112

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0112.txt)

**Task:** `transmembrane`  
**Expected answer:** **C** — 5..25; 46..66; 74..94; 179..199; 239..259; 264..284; 296..316

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MWLSTFLALLIFVECVIVVYIPAYIESKLSKIKKNRFFNMENFENIASGAILALAFLHMLPEVIILSNKKNMNLYYIFILVLVSVTFLNITDILYDHHFESTFDVNCTLACENSNNQIKNINDKEITTNYIDIKSNEVIDLELKAMDTNINNNNNNNNNNKTDPCKTNIFFEIFKSNSFFIVLSLFIHSFIEGLLMGSLKDKNAIIIVGLSMLAHKWAECLIVYKNVVNKIENPLLASIYAWSFILSLPLGVFIAIFSFPSNEFVEIIFSSIACGFFLYLSFNMTKEIKITKSNKHFISFSYFLGVGGMSTLMILFNSFESNNII

[Multiple Choices]
A. 5..25; 46..66; 179..199; 239..259; 264..284; 296..316
B. 4..24
C. 5..25; 46..66; 74..94; 179..199; 239..259; 264..284; 296..316
D. 5..25; 44..68; 74..94; 179..199; 239..259; 264..284; 296..316
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

> The sequence-matched historical UniProt record lists all seven intervals in choice C as transmembrane features, each annotated as helical with computational evidence code ECO:0000255. This supports the key as a database/computational annotation, not as independently verified experimental evidence.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains several long, strongly hydrophobic stretches characteristic of membrane-spanning alpha helices, including the stretches around positions 5–25, 46–66, and 74–94, as well as later hydrophobic segments. This transferable sequence pattern favors C: A and B omit obvious hydrophobic segments, while D extends the 46–66 interval into polar flanking residues. The sequence supports a meaningful prediction, although exact helix boundaries are not certain from sequence alone.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The offered choices differ in their coverage of conspicuous hydrophobic stretches and in whether they include polar flanks. Those features can be assessed from the input sequence using general knowledge of transmembrane helices; recalling this exact protein's annotation is not necessary.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although predicted transmembrane boundaries can vary by a few residues, the choices differ in broader coverage, and the strongly hydrophobic stretches favor C over the alternatives.


### Important caveats

- The source supports the answer through computational transmembrane annotations; it does not establish experimental validation of each boundary.
- The sequence-matched annotation supports the expected intervals, but the exact source snapshot used by the benchmark author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains several long, strongly hydrophobic stretches characteristic of membrane-spanning alpha helices, including the stretches around positions 5–25, 46–66, and 74–94, as well as later hydrophobic segments. This transferable sequence pattern favors C: A and B omit obvious hydrophobic segments, while D extends the 46–66 interval into polar flanking residues. The sequence supports a meaningful prediction, although exact helix boundaries are not certain from sequence alone.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The offered choices differ in their coverage of conspicuous hydrophobic stretches and in whether they include polar flanks. Those features can be assessed from the input sequence using general knowledge of transmembrane helices; recalling this exact protein's annotation is not necessary."
  },
  "case_id": "transmembrane_0112",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record lists all seven intervals in choice C as transmembrane features, each annotated as helical with computational evidence code ECO:0000255. This supports the key as a database/computational annotation, not as independently verified experimental evidence."
  },
  "important_caveats": [
    "The source supports the answer through computational transmembrane annotations; it does not establish experimental validation of each boundary.",
    "The sequence-matched annotation supports the expected intervals, but the exact source snapshot used by the benchmark author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although predicted transmembrane boundaries can vary by a few residues, the choices differ in broader coverage, and the strongly hydrophobic stretches favor C over the alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0112",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record lists all seven intervals in choice C as transmembrane features, each annotated as helical with computational evidence code ECO:0000255. This supports the key as a database/computational annotation, not as independently verified experimental evidence.",
    "evidence_ids": ["H3", "H4", "H5", "H6", "H7", "H8", "H9"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains several long, strongly hydrophobic stretches characteristic of membrane-spanning alpha helices, including the stretches around positions 5–25, 46–66, and 74–94, as well as later hydrophobic segments. This transferable sequence pattern favors C: A and B omit obvious hydrophobic segments, while D extends the 46–66 interval into polar flanking residues. The sequence supports a meaningful prediction, although exact helix boundaries are not certain from sequence alone.",
    "missing_item_specific_fact": "",
    "reason": "The offered choices differ in their coverage of conspicuous hydrophobic stretches and in whether they include polar flanks. Those features can be assessed from the input sequence using general knowledge of transmembrane helices; recalling this exact protein's annotation is not necessary."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although predicted transmembrane boundaries can vary by a few residues, the choices differ in broader coverage, and the strongly hydrophobic stretches favor C over the alternatives."
  },
  "important_caveats": [
    "The source supports the answer through computational transmembrane annotations; it does not establish experimental validation of each boundary.",
    "The sequence-matched annotation supports the expected intervals, but the exact source snapshot used by the benchmark author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for Q8IJI1 (ZIPCO_PLAF7, sequence matched) lists exactly seven transmembrane helical regions at 5..25, 46..66, 74..94, 179..199, 239..259, 264..284, and 296..316, matching option C precisely. The evidence code ECO:0000255 indicates these are electronic/computational predictions rather than experimental determinations, but they are the recorded annotations. The sequence itself supports these boundaries: each region is ~21 residues of predominantly hydrophobic character, and the inter-region segments contain charged/polar residues incompatible with membrane spanning.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model can distinguish the options using standard TM-helix composition rules learned from many other membrane proteins. (1) Option B (single TM) is eliminated because the 325-residue sequence contains multiple long hydrophobic stretches inconsistent with a single-pass protein. (2) Option A omits the 74..94 region; inspecting that segment (YYIFILVLVSVTFLNITDILY) reveals a classic hydrophobic TM motif (IFILVLVSVTF), comparable in hydrophobicity to the other annotated helices, so a model recognizing hydrophobic stretches of ~20 residues would include it. (3) Option D extends the second TM to 44..68, but position 44 is Glu (charged) and position 68 is Lys (charged); TM helices strongly avoid buried charged residues, making 46..66 (starting at Ile, ending at Ser) far more plausible. These are general principles of TM helix composition (hydrophobic core, avoidance of charged residues in the bilayer interior) transferable from thousands of characterized membrane proteins.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence itself provides sufficient hydrophobicity information to identify the seven TM segments and to reject boundaries that include charged residues (E44, K68). The distinction between A and C (presence of the 74-94 helix) and between C and D (boundary precision) relies on well-established TM prediction principles rather than a fact unique to this protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The charged residues at positions 44 and 68 clearly disfavor D over C, and the strong hydrophobicity of region 74-94 clearly favors C over A. No two options are equally defensible given the sequence.


### Important caveats

- All TM annotations carry evidence code ECO:0000255 (inferred from electronic annotation), meaning they are computational predictions, not experimentally validated.
- The UniProt entry was first public on 2025-06-18; the author's source snapshot date is unknown, though the sequence matches across checked versions.
- The protein is annotated as a 'Putative metal ion transporter ZIPCO' from Plasmodium falciparum, but this identity was not given to the evaluated model; the reasoning relies solely on sequence hydrophobicity and general TM principles.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can distinguish the options using standard TM-helix composition rules learned from many other membrane proteins. (1) Option B (single TM) is eliminated because the 325-residue sequence contains multiple long hydrophobic stretches inconsistent with a single-pass protein. (2) Option A omits the 74..94 region; inspecting that segment (YYIFILVLVSVTFLNITDILY) reveals a classic hydrophobic TM motif (IFILVLVSVTF), comparable in hydrophobicity to the other annotated helices, so a model recognizing hydrophobic stretches of ~20 residues would include it. (3) Option D extends the second TM to 44..68, but position 44 is Glu (charged) and position 68 is Lys (charged); TM helices strongly avoid buried charged residues, making 46..66 (starting at Ile, ending at Ser) far more plausible. These are general principles of TM helix composition (hydrophobic core, avoidance of charged residues in the bilayer interior) transferable from thousands of characterized membrane proteins.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence itself provides sufficient hydrophobicity information to identify the seven TM segments and to reject boundaries that include charged residues (E44, K68). The distinction between A and C (presence of the 74-94 helix) and between C and D (boundary precision) relies on well-established TM prediction principles rather than a fact unique to this protein."
  },
  "case_id": "transmembrane_0112",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "C10",
      "C11"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for Q8IJI1 (ZIPCO_PLAF7, sequence matched) lists exactly seven transmembrane helical regions at 5..25, 46..66, 74..94, 179..199, 239..259, 264..284, and 296..316, matching option C precisely. The evidence code ECO:0000255 indicates these are electronic/computational predictions rather than experimental determinations, but they are the recorded annotations. The sequence itself supports these boundaries: each region is ~21 residues of predominantly hydrophobic character, and the inter-region segments contain charged/polar residues incompatible with membrane spanning."
  },
  "important_caveats": [
    "All TM annotations carry evidence code ECO:0000255 (inferred from electronic annotation), meaning they are computational predictions, not experimentally validated.",
    "The UniProt entry was first public on 2025-06-18; the author's source snapshot date is unknown, though the sequence matches across checked versions.",
    "The protein is annotated as a 'Putative metal ion transporter ZIPCO' from Plasmodium falciparum, but this identity was not given to the evaluated model; the reasoning relies solely on sequence hydrophobicity and general TM principles."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The charged residues at positions 44 and 68 clearly disfavor D over C, and the strong hydrophobicity of region 74-94 clearly favors C over A. No two options are equally defensible given the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0112",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for Q8IJI1 (ZIPCO_PLAF7, sequence matched) lists exactly seven transmembrane helical regions at 5..25, 46..66, 74..94, 179..199, 239..259, 264..284, and 296..316, matching option C precisely. The evidence code ECO:0000255 indicates these are electronic/computational predictions rather than experimental determinations, but they are the recorded annotations. The sequence itself supports these boundaries: each region is ~21 residues of predominantly hydrophobic character, and the inter-region segments contain charged/polar residues incompatible with membrane spanning.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "C11"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model can distinguish the options using standard TM-helix composition rules learned from many other membrane proteins. (1) Option B (single TM) is eliminated because the 325-residue sequence contains multiple long hydrophobic stretches inconsistent with a single-pass protein. (2) Option A omits the 74..94 region; inspecting that segment (YYIFILVLVSVTFLNITDILY) reveals a classic hydrophobic TM motif (IFILVLVSVTF), comparable in hydrophobicity to the other annotated helices, so a model recognizing hydrophobic stretches of ~20 residues would include it. (3) Option D extends the second TM to 44..68, but position 44 is Glu (charged) and position 68 is Lys (charged); TM helices strongly avoid buried charged residues, making 46..66 (starting at Ile, ending at Ser) far more plausible. These are general principles of TM helix composition (hydrophobic core, avoidance of charged residues in the bilayer interior) transferable from thousands of characterized membrane proteins.",
    "missing_item_specific_fact": "",
    "reason": "The sequence itself provides sufficient hydrophobicity information to identify the seven TM segments and to reject boundaries that include charged residues (E44, K68). The distinction between A and C (presence of the 74-94 helix) and between C and D (boundary precision) relies on well-established TM prediction principles rather than a fact unique to this protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The charged residues at positions 44 and 68 clearly disfavor D over C, and the strong hydrophobicity of region 74-94 clearly favors C over A. No two options are equally defensible given the sequence."
  },
  "important_caveats": [
    "All TM annotations carry evidence code ECO:0000255 (inferred from electronic annotation), meaning they are computational predictions, not experimentally validated.",
    "The UniProt entry was first public on 2025-06-18; the author's source snapshot date is unknown, though the sequence matches across checked versions.",
    "The protein is annotated as a 'Putative metal ion transporter ZIPCO' from Plasmodium falciparum, but this identity was not given to the evaluated model; the reasoning relies solely on sequence hydrophobicity and general TM principles."
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
  "benchmark_sequence_length": 325,
  "benchmark_sequence_sha256": "51b47d311ec092251e00deda53076d98d906bf56774394a39283c8e55aad4b9c",
  "current_entry_audit": {
    "entryVersion": 101,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2009-09-22",
    "sequenceVersion": 2
  },
  "current_record_sha256": "98ec602d5ce9074cc044866398ff14a3b6a28ea7f4a3afc0eb6d37bd83fd5f25",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 325,
  "current_source_sequence_sha256": "51b47d311ec092251e00deda53076d98d906bf56774394a39283c8e55aad4b9c",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 99,
      "exact_sequence_comparison": "matched",
      "sequence_version": 2
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q8IJI1",
  "selected_historical_entry_version": 99,
  "selected_historical_record_sha256": "a185b20a7b70bc0a98ff98aba7bf611816a4de98cce29ce98fad70203aaa6f76",
  "selected_historical_source_sequence_length": 325,
  "selected_historical_source_sequence_sha256": "51b47d311ec092251e00deda53076d98d906bf56774394a39283c8e55aad4b9c",
  "selected_historical_version": {
    "accession": "Q8IJI1",
    "database": "Swiss-Prot",
    "entryVersion": 99,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "ZIPCO_PLAF7",
    "sequenceVersion": 2
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IJI1.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q8IJI1\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:32:13.245159+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "98ec602d5ce9074cc044866398ff14a3b6a28ea7f4a3afc0eb6d37bd83fd5f25",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IJI1.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IJI1.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":101,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2009-09-22\",\"sequenceVersion\":2}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:32:13.245159+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "98ec602d5ce9074cc044866398ff14a3b6a28ea7f4a3afc0eb6d37bd83fd5f25",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IJI1.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IJI1.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000001450\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Aconoidasida\",\"Haemosporida\",\"Plasmodiidae\",\"Plasmodium\",\"Laverania\"],\"scientificName\":\"Plasmodium falciparum (isolate 3D7)\",\"taxonId\":36329}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:32:13.245159+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "98ec602d5ce9074cc044866398ff14a3b6a28ea7f4a3afc0eb6d37bd83fd5f25",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IJI1.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IJI1.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39575308\",\"source\":\"PubMed\"}],\"value\":\"ZIP domain-containing protein\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39575308\",\"source\":\"PubMed\"}],\"value\":\"PfZIPCO\"}]}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Putative metal ion transporter ZIPCO\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:32:13.245159+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "98ec602d5ce9074cc044866398ff14a3b6a28ea7f4a3afc0eb6d37bd83fd5f25",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IJI1.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IJI1.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":25},\"start\":{\"modifier\":\"EXACT\",\"value\":5}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:32:13.245159+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "98ec602d5ce9074cc044866398ff14a3b6a28ea7f4a3afc0eb6d37bd83fd5f25",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IJI1.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IJI1.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":66},\"start\":{\"modifier\":\"EXACT\",\"value\":46}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:32:13.245159+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "98ec602d5ce9074cc044866398ff14a3b6a28ea7f4a3afc0eb6d37bd83fd5f25",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IJI1.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IJI1.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":94},\"start\":{\"modifier\":\"EXACT\",\"value\":74}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:32:13.245159+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "98ec602d5ce9074cc044866398ff14a3b6a28ea7f4a3afc0eb6d37bd83fd5f25",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IJI1.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IJI1.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":199},\"start\":{\"modifier\":\"EXACT\",\"value\":179}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:32:13.245159+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "98ec602d5ce9074cc044866398ff14a3b6a28ea7f4a3afc0eb6d37bd83fd5f25",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IJI1.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IJI1.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":259},\"start\":{\"modifier\":\"EXACT\",\"value\":239}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:32:13.245159+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "98ec602d5ce9074cc044866398ff14a3b6a28ea7f4a3afc0eb6d37bd83fd5f25",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IJI1.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IJI1.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":284},\"start\":{\"modifier\":\"EXACT\",\"value\":264}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:32:13.245159+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "98ec602d5ce9074cc044866398ff14a3b6a28ea7f4a3afc0eb6d37bd83fd5f25",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IJI1.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IJI1.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":316},\"start\":{\"modifier\":\"EXACT\",\"value\":296}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:32:13.245159+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "98ec602d5ce9074cc044866398ff14a3b6a28ea7f4a3afc0eb6d37bd83fd5f25",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IJI1.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IJI1.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"citation\":{\"authors\":[\"Wunderlich J.\",\"Kotov V.\",\"Votborg-Novel L.\",\"Ntalla C.\",\"Geffken M.\",\"Peine S.\",\"Portugal S.\",\"Strauss J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39575308\"},{\"database\":\"DOI\",\"id\":\"10.3389/fcimb.2024.1480076\"}],\"citationType\":\"journal article\",\"firstPage\":\"1480076\",\"id\":\"39575308\",\"journal\":\"Front. Cell. Infect. Microbiol.\",\"lastPage\":\"1480076\",\"publicationDate\":\"2024\",\"title\":\"Iron transport pathways in the human malaria parasite Plasmodium falciparum revealed by RNA-sequencing.\",\"volume\":\"14\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"SUBCELLULAR LOCATION\",\"DEVELOPMENTAL STAGE\",\"INDUCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:32:13.245159+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "98ec602d5ce9074cc044866398ff14a3b6a28ea7f4a3afc0eb6d37bd83fd5f25",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IJI1.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IJI1?format=txt&versions=99)

```json
{
  "entry_version": 99,
  "evidence_id": "H1",
  "excerpt": "ID   ZIPCO_PLAF7             Reviewed;         325 AA.\nAC   Q8IJI1;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   22-SEP-2009, sequence version 2.\nDT   28-JAN-2026, entry version 99.\nDE   RecName: Full=Putative metal ion transporter ZIPCO {ECO:0000305};\nDE   AltName: Full=ZIP domain-containing protein {ECO:0000303|PubMed:39575308};\nDE            Short=PfZIPCO {ECO:0000303|PubMed:39575308};\nGN   Name=ZIPCO {ECO:0000305};\nGN   ORFNames=PF3D7_1022300 {ECO:0000312|EMBL:CZT98478.1};\nOS   Plasmodium falciparum (isolate 3D7).\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;\nOC   Plasmodiidae; Plasmodium; Plasmodium (Laverania).\nOX   NCBI_TaxID=36329 {ECO:0000312|Proteomes:UP000001450};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:15.953075+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a185b20a7b70bc0a98ff98aba7bf611816a4de98cce29ce98fad70203aaa6f76",
  "url": "https://rest.uniprot.org/unisave/Q8IJI1?format=txt&versions=99"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IJI1?format=txt&versions=99)

```json
{
  "entry_version": 99,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, SUBCELLULAR LOCATION, DEVELOPMENTAL STAGE, INDUCTION, AND\nRP   DISRUPTION PHENOTYPE.\nRX   PubMed=39575308; DOI=10.3389/fcimb.2024.1480076;\nRA   Wunderlich J., Kotov V., Votborg-Novel L., Ntalla C., Geffken M., Peine S.,\nRA   Portugal S., Strauss J.;\nRT   \"Iron transport pathways in the human malaria parasite Plasmodium\nRT   falciparum revealed by RNA-sequencing.\";\nRL   Front. Cell. Infect. Microbiol. 14:1480076-1480076(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:15.953075+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 29-37",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a185b20a7b70bc0a98ff98aba7bf611816a4de98cce29ce98fad70203aaa6f76",
  "url": "https://rest.uniprot.org/unisave/Q8IJI1?format=txt&versions=99"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IJI1?format=txt&versions=99)

```json
{
  "entry_version": 99,
  "evidence_id": "H3",
  "excerpt": "FT   TRANSMEM        5..25\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:15.953075+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 87-89",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a185b20a7b70bc0a98ff98aba7bf611816a4de98cce29ce98fad70203aaa6f76",
  "url": "https://rest.uniprot.org/unisave/Q8IJI1?format=txt&versions=99"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IJI1?format=txt&versions=99)

```json
{
  "entry_version": 99,
  "evidence_id": "H4",
  "excerpt": "FT   TRANSMEM        46..66\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:15.953075+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 90-92",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a185b20a7b70bc0a98ff98aba7bf611816a4de98cce29ce98fad70203aaa6f76",
  "url": "https://rest.uniprot.org/unisave/Q8IJI1?format=txt&versions=99"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IJI1?format=txt&versions=99)

```json
{
  "entry_version": 99,
  "evidence_id": "H5",
  "excerpt": "FT   TRANSMEM        74..94\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:15.953075+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 93-95",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a185b20a7b70bc0a98ff98aba7bf611816a4de98cce29ce98fad70203aaa6f76",
  "url": "https://rest.uniprot.org/unisave/Q8IJI1?format=txt&versions=99"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IJI1?format=txt&versions=99)

```json
{
  "entry_version": 99,
  "evidence_id": "H6",
  "excerpt": "FT   TRANSMEM        179..199\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:15.953075+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 96-98",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a185b20a7b70bc0a98ff98aba7bf611816a4de98cce29ce98fad70203aaa6f76",
  "url": "https://rest.uniprot.org/unisave/Q8IJI1?format=txt&versions=99"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IJI1?format=txt&versions=99)

```json
{
  "entry_version": 99,
  "evidence_id": "H7",
  "excerpt": "FT   TRANSMEM        239..259\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:15.953075+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 99-101",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a185b20a7b70bc0a98ff98aba7bf611816a4de98cce29ce98fad70203aaa6f76",
  "url": "https://rest.uniprot.org/unisave/Q8IJI1?format=txt&versions=99"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IJI1?format=txt&versions=99)

```json
{
  "entry_version": 99,
  "evidence_id": "H8",
  "excerpt": "FT   TRANSMEM        264..284\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:15.953075+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 102-104",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a185b20a7b70bc0a98ff98aba7bf611816a4de98cce29ce98fad70203aaa6f76",
  "url": "https://rest.uniprot.org/unisave/Q8IJI1?format=txt&versions=99"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IJI1?format=txt&versions=99)

```json
{
  "entry_version": 99,
  "evidence_id": "H9",
  "excerpt": "FT   TRANSMEM        296..316\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:15.953075+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 105-107",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a185b20a7b70bc0a98ff98aba7bf611816a4de98cce29ce98fad70203aaa6f76",
  "url": "https://rest.uniprot.org/unisave/Q8IJI1?format=txt&versions=99"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 112. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
