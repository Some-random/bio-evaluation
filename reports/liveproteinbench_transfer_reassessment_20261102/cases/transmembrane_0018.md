# transmembrane_0018

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0018.txt)

**Task:** `transmembrane`  
**Expected answer:** **B** — 27..47; 67..87; 100..120; 144..164; 202..222; 241..261; 274..294

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MGSNITSTSIIFLLTGVPGLEAFHTWISIPFCFLSVTALLGNSLILFATITQPSLHEPMYYFLSMLSATDLGLSISTLVTMLSIFWFNVREISFNACLSHMFFIKFFTVMESSVLLAMAFDRFVAVSNPLRYAMILTDSRIAQIGVASVIRGLLMLTPMVALLIRLSYCHSQVLHHSYCYHPDVMKLSCTDTRINSAVGLTAMFSTVGVDLLLILLSYVLIIRTVLSVASPEERKETFSTCVSHIVAFAIYYIPLISLSIVHRFGKQAPAYVHTMIANTYLLISPLMNPVIYSVKTKQIRRAVIKILHSKET

[Multiple Choices]
A. 27..47; 67..87; 100..120; 144..164; 202..222; 241..261
B. 27..47; 67..87; 100..120; 144..164; 202..222; 241..261; 274..294
C. 27..47; 67..87; 100..120; 144..164; 202..222; 241..265; 274..294
D. 9..29; 41..61; 84..104; 118..138; 153..173; 175..195; 202..222; 231..251
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

> The sequence matches the cited UniProt record, whose annotated transmembrane helices are 27–47, 67–87, 100–120, 144–164, 202–222, 241–261, and 274–294, matching choice B. These features carry computational evidence code ECO:0000255, so they support the key as an annotation rather than establishing experimental validation.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [H3](#evidence-h3), [H5](#evidence-h5), [H7](#evidence-h7), [H9](#evidence-h9), [H11](#evidence-h11), [H13](#evidence-h13), [H15](#evidence-h15).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is strongly hydrophobic in multiple separated stretches and has the length and pattern typical of seven-pass GPCR-family proteins, including olfactory receptors. Transferable knowledge of this family supports seven membrane-spanning helices, distinguishing B/C (which include a seventh helix) from A and D. The segment around 241–261 is strongly hydrophobic, whereas the following stretch includes polar residues and a break before the next hydrophobic segment at 274, supporting B’s boundary over C’s extension to 265.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A credible family-level and sequence-hydropathy inference distinguishes the offered choices without needing the exact protein’s database annotation. The four-residue boundary difference between B and C is less certain from general inference than the seven-helix pattern, but the sequence’s local hydrophobicity provides a meaningful basis for B.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives differ in helix count and in a short boundary extension; the strongly hydrophobic sequence supports the seven-helix choice and disfavors extending the sixth segment into the following less hydrophobic stretch.


### Important caveats

- The supporting UniProt transmembrane features are computationally evidenced, not direct experimental measurements.
- Exact helix boundaries can vary by prediction method; the source supports the keyed boundaries but does not establish that they are uniquely experimentally determined.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is strongly hydrophobic in multiple separated stretches and has the length and pattern typical of seven-pass GPCR-family proteins, including olfactory receptors. Transferable knowledge of this family supports seven membrane-spanning helices, distinguishing B/C (which include a seventh helix) from A and D. The segment around 241–261 is strongly hydrophobic, whereas the following stretch includes polar residues and a break before the next hydrophobic segment at 274, supporting B’s boundary over C’s extension to 265.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A credible family-level and sequence-hydropathy inference distinguishes the offered choices without needing the exact protein’s database annotation. The four-residue boundary difference between B and C is less certain from general inference than the seven-helix pattern, but the sequence’s local hydrophobicity provides a meaningful basis for B."
  },
  "case_id": "transmembrane_0018",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C8",
      "C10",
      "C12",
      "C14",
      "C16",
      "C18",
      "H3",
      "H5",
      "H7",
      "H9",
      "H11",
      "H13",
      "H15"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the cited UniProt record, whose annotated transmembrane helices are 27–47, 67–87, 100–120, 144–164, 202–222, 241–261, and 274–294, matching choice B. These features carry computational evidence code ECO:0000255, so they support the key as an annotation rather than establishing experimental validation."
  },
  "important_caveats": [
    "The supporting UniProt transmembrane features are computationally evidenced, not direct experimental measurements.",
    "Exact helix boundaries can vary by prediction method; the source supports the keyed boundaries but does not establish that they are uniquely experimentally determined."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives differ in helix count and in a short boundary extension; the strongly hydrophobic sequence supports the seven-helix choice and disfavors extending the sixth segment into the following less hydrophobic stretch."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0018",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the cited UniProt record, whose annotated transmembrane helices are 27–47, 67–87, 100–120, 144–164, 202–222, 241–261, and 274–294, matching choice B. These features carry computational evidence code ECO:0000255, so they support the key as an annotation rather than establishing experimental validation.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "H3", "H5", "H7", "H9", "H11", "H13", "H15"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is strongly hydrophobic in multiple separated stretches and has the length and pattern typical of seven-pass GPCR-family proteins, including olfactory receptors. Transferable knowledge of this family supports seven membrane-spanning helices, distinguishing B/C (which include a seventh helix) from A and D. The segment around 241–261 is strongly hydrophobic, whereas the following stretch includes polar residues and a break before the next hydrophobic segment at 274, supporting B’s boundary over C’s extension to 265.",
    "missing_item_specific_fact": "",
    "reason": "A credible family-level and sequence-hydropathy inference distinguishes the offered choices without needing the exact protein’s database annotation. The four-residue boundary difference between B and C is less certain from general inference than the seven-helix pattern, but the sequence’s local hydrophobicity provides a meaningful basis for B."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives differ in helix count and in a short boundary extension; the strongly hydrophobic sequence supports the seven-helix choice and disfavors extending the sixth segment into the following less hydrophobic stretch."
  },
  "important_caveats": [
    "The supporting UniProt transmembrane features are computationally evidenced, not direct experimental measurements.",
    "Exact helix boundaries can vary by prediction method; the source supports the keyed boundaries but does not establish that they are uniquely experimentally determined."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (evidence code ECO:0000255, 'by similarity') records exactly seven transmembrane helices at positions 27-47, 67-87, 100-120, 144-164, 202-222, 241-261, and 274-294, matching option B precisely. The annotation is computational/by-similarity rather than experimental, but it is the recorded annotation for this sequence. The topology (extracellular N-terminus 1-26, cytoplasmic 48-66, etc.) is consistent with the GPCR 7TM architecture.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [H3](#evidence-h3), [H5](#evidence-h5), [H7](#evidence-h7), [H9](#evidence-h9), [H11](#evidence-h11), [H13](#evidence-h13), [H15](#evidence-h15).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the highly conserved NPxxY motif (MNPVI at ~positions 288-292), a hallmark of all GPCRs. The overall length (~312 aa), seven distinct hydrophobic stretches, and alternating topology are consistent with the canonical 7-transmembrane GPCR architecture. This eliminates option A (6 helices) and option D (8 helices with shifted positions). Between B and C, the only difference is whether TM6 ends at residue 261 or 265. Positions 262-265 encode V-H-R-F, containing two charged/polar residues (His, Arg) that are inconsistent with a hydrophobic TM helix core. Standard hydrophobicity principles (TM helix interiors require ~20 hydrophobic residues; charged residues are typically excluded from the bilayer-spanning segment) favor the shorter boundary at 261. Thus, family-level GPCR knowledge (7 TM helices, NPxxY motif) plus basic hydrophobicity reasoning distinguishes B from the alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The 7-TM GPCR topology is among the most fundamental and widely taught facts in membrane protein biology. The NPxxY motif is identifiable directly in the supplied sequence. The B-vs-C distinction relies on a standard hydrophobicity argument about charged residues in TM helix cores. A knowledgeable model can reach B without memorizing this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option A (6 TMs) and D (8 TMs) are eliminated by the well-established 7-TM GPCR topology. Option C differs from B only by a 4-residue extension of TM6 that includes charged residues (H, R), which is disfavored by hydrophobicity principles. While TM boundaries can have ±1-2 residue uncertainty in practice, the inclusion of two charged residues tips the balance clearly toward B.


### Important caveats

- The UniProt TM annotation uses evidence code ECO:0000255 (by similarity), meaning it is a computational/inference annotation rather than experimental determination.
- The B-vs-C distinction (4-residue difference at TM6 C-terminus) is within the typical uncertainty range of TM prediction tools, though the charged-residue argument provides a reasonable basis for preferring B.
- The DRY/ERY motif at the end of TM3 is not perfectly canonical in this olfactory receptor (appears as IRT rather than DRY/ERY), but the NPxxY motif and overall 7-TM pattern are sufficient for family identification.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the highly conserved NPxxY motif (MNPVI at ~positions 288-292), a hallmark of all GPCRs. The overall length (~312 aa), seven distinct hydrophobic stretches, and alternating topology are consistent with the canonical 7-transmembrane GPCR architecture. This eliminates option A (6 helices) and option D (8 helices with shifted positions). Between B and C, the only difference is whether TM6 ends at residue 261 or 265. Positions 262-265 encode V-H-R-F, containing two charged/polar residues (His, Arg) that are inconsistent with a hydrophobic TM helix core. Standard hydrophobicity principles (TM helix interiors require ~20 hydrophobic residues; charged residues are typically excluded from the bilayer-spanning segment) favor the shorter boundary at 261. Thus, family-level GPCR knowledge (7 TM helices, NPxxY motif) plus basic hydrophobicity reasoning distinguishes B from the alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The 7-TM GPCR topology is among the most fundamental and widely taught facts in membrane protein biology. The NPxxY motif is identifiable directly in the supplied sequence. The B-vs-C distinction relies on a standard hydrophobicity argument about charged residues in TM helix cores. A knowledgeable model can reach B without memorizing this specific protein's database entry."
  },
  "case_id": "transmembrane_0018",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C8",
      "C10",
      "C12",
      "C14",
      "C16",
      "C18",
      "H3",
      "H5",
      "H7",
      "H9",
      "H11",
      "H13",
      "H15"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence code ECO:0000255, 'by similarity') records exactly seven transmembrane helices at positions 27-47, 67-87, 100-120, 144-164, 202-222, 241-261, and 274-294, matching option B precisely. The annotation is computational/by-similarity rather than experimental, but it is the recorded annotation for this sequence. The topology (extracellular N-terminus 1-26, cytoplasmic 48-66, etc.) is consistent with the GPCR 7TM architecture."
  },
  "important_caveats": [
    "The UniProt TM annotation uses evidence code ECO:0000255 (by similarity), meaning it is a computational/inference annotation rather than experimental determination.",
    "The B-vs-C distinction (4-residue difference at TM6 C-terminus) is within the typical uncertainty range of TM prediction tools, though the charged-residue argument provides a reasonable basis for preferring B.",
    "The DRY/ERY motif at the end of TM3 is not perfectly canonical in this olfactory receptor (appears as IRT rather than DRY/ERY), but the NPxxY motif and overall 7-TM pattern are sufficient for family identification."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option A (6 TMs) and D (8 TMs) are eliminated by the well-established 7-TM GPCR topology. Option C differs from B only by a 4-residue extension of TM6 that includes charged residues (H, R), which is disfavored by hydrophobicity principles. While TM boundaries can have ±1-2 residue uncertainty in practice, the inclusion of two charged residues tips the balance clearly toward B."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0018",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence code ECO:0000255, 'by similarity') records exactly seven transmembrane helices at positions 27-47, 67-87, 100-120, 144-164, 202-222, 241-261, and 274-294, matching option B precisely. The annotation is computational/by-similarity rather than experimental, but it is the recorded annotation for this sequence. The topology (extracellular N-terminus 1-26, cytoplasmic 48-66, etc.) is consistent with the GPCR 7TM architecture.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "H3", "H5", "H7", "H9", "H11", "H13", "H15"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the highly conserved NPxxY motif (MNPVI at ~positions 288-292), a hallmark of all GPCRs. The overall length (~312 aa), seven distinct hydrophobic stretches, and alternating topology are consistent with the canonical 7-transmembrane GPCR architecture. This eliminates option A (6 helices) and option D (8 helices with shifted positions). Between B and C, the only difference is whether TM6 ends at residue 261 or 265. Positions 262-265 encode V-H-R-F, containing two charged/polar residues (His, Arg) that are inconsistent with a hydrophobic TM helix core. Standard hydrophobicity principles (TM helix interiors require ~20 hydrophobic residues; charged residues are typically excluded from the bilayer-spanning segment) favor the shorter boundary at 261. Thus, family-level GPCR knowledge (7 TM helices, NPxxY motif) plus basic hydrophobicity reasoning distinguishes B from the alternatives.",
    "missing_item_specific_fact": "",
    "reason": "The 7-TM GPCR topology is among the most fundamental and widely taught facts in membrane protein biology. The NPxxY motif is identifiable directly in the supplied sequence. The B-vs-C distinction relies on a standard hydrophobicity argument about charged residues in TM helix cores. A knowledgeable model can reach B without memorizing this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option A (6 TMs) and D (8 TMs) are eliminated by the well-established 7-TM GPCR topology. Option C differs from B only by a 4-residue extension of TM6 that includes charged residues (H, R), which is disfavored by hydrophobicity principles. While TM boundaries can have ±1-2 residue uncertainty in practice, the inclusion of two charged residues tips the balance clearly toward B."
  },
  "important_caveats": [
    "The UniProt TM annotation uses evidence code ECO:0000255 (by similarity), meaning it is a computational/inference annotation rather than experimental determination.",
    "The B-vs-C distinction (4-residue difference at TM6 C-terminus) is within the typical uncertainty range of TM prediction tools, though the charged-residue argument provides a reasonable basis for preferring B.",
    "The DRY/ERY motif at the end of TM3 is not perfectly canonical in this olfactory receptor (appears as IRT rather than DRY/ERY), but the NPxxY motif and overall 7-TM pattern are sufficient for family identification."
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
  "benchmark_sequence_length": 312,
  "benchmark_sequence_sha256": "2e8788df8496584049759195f5fde6a8aa4eb5ba3967d17a73b09b64771bfd14",
  "current_entry_audit": {
    "entryVersion": 35,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2018-12-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "413edf0d30a632c4d35f0ee6c062c8bf9f27b4551b6e1a829cb403d5b8de10f5",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 312,
  "current_source_sequence_sha256": "2e8788df8496584049759195f5fde6a8aa4eb5ba3967d17a73b09b64771bfd14",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 33,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A3B3IT45",
  "selected_historical_entry_version": 33,
  "selected_historical_record_sha256": "baa83bf26c0bb6c7471ba5998d88f9308542ba6a5a9c7c12ad2235d34b22e1f3",
  "selected_historical_source_sequence_length": 312,
  "selected_historical_source_sequence_sha256": "2e8788df8496584049759195f5fde6a8aa4eb5ba3967d17a73b09b64771bfd14",
  "selected_historical_version": {
    "accession": "A0A3B3IT45",
    "database": "Swiss-Prot",
    "entryVersion": 33,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "O51C1_HUMAN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A3B3IT45\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:25:02.741232+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "413edf0d30a632c4d35f0ee6c062c8bf9f27b4551b6e1a829cb403d5b8de10f5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":35,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2018-12-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:25:02.741232+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "413edf0d30a632c4d35f0ee6c062c8bf9f27b4551b6e1a829cb403d5b8de10f5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Human\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Euteleostomi\",\"Mammalia\",\"Eutheria\",\"Euarchontoglires\",\"Primates\",\"Haplorrhini\",\"Catarrhini\",\"Hominidae\",\"Homo\"],\"scientificName\":\"Homo sapiens\",\"taxonId\":9606}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:25:02.741232+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "413edf0d30a632c4d35f0ee6c062c8bf9f27b4551b6e1a829cb403d5b8de10f5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"HGNC:15191\",\"source\":\"HGNC\"}],\"value\":\"Olfactory receptor OR51C1\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:25:02.741232+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "413edf0d30a632c4d35f0ee6c062c8bf9f27b4551b6e1a829cb403d5b8de10f5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":26},\"start\":{\"modifier\":\"EXACT\",\"value\":1}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:25:02.741232+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "413edf0d30a632c4d35f0ee6c062c8bf9f27b4551b6e1a829cb403d5b8de10f5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical; Name=1\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":47},\"start\":{\"modifier\":\"EXACT\",\"value\":27}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:25:02.741232+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "413edf0d30a632c4d35f0ee6c062c8bf9f27b4551b6e1a829cb403d5b8de10f5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":66},\"start\":{\"modifier\":\"EXACT\",\"value\":48}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:25:02.741232+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "413edf0d30a632c4d35f0ee6c062c8bf9f27b4551b6e1a829cb403d5b8de10f5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Helical; Name=2\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":87},\"start\":{\"modifier\":\"EXACT\",\"value\":67}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:25:02.741232+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "413edf0d30a632c4d35f0ee6c062c8bf9f27b4551b6e1a829cb403d5b8de10f5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":99},\"start\":{\"modifier\":\"EXACT\",\"value\":88}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:25:02.741232+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "413edf0d30a632c4d35f0ee6c062c8bf9f27b4551b6e1a829cb403d5b8de10f5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"Helical; Name=3\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":120},\"start\":{\"modifier\":\"EXACT\",\"value\":100}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:25:02.741232+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "413edf0d30a632c4d35f0ee6c062c8bf9f27b4551b6e1a829cb403d5b8de10f5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":143},\"start\":{\"modifier\":\"EXACT\",\"value\":121}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:25:02.741232+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "413edf0d30a632c4d35f0ee6c062c8bf9f27b4551b6e1a829cb403d5b8de10f5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"Helical; Name=4\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":164},\"start\":{\"modifier\":\"EXACT\",\"value\":144}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:25:02.741232+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "413edf0d30a632c4d35f0ee6c062c8bf9f27b4551b6e1a829cb403d5b8de10f5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":201},\"start\":{\"modifier\":\"EXACT\",\"value\":165}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-02T04:25:02.741232+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "413edf0d30a632c4d35f0ee6c062c8bf9f27b4551b6e1a829cb403d5b8de10f5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"description\":\"Helical; Name=5\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":222},\"start\":{\"modifier\":\"EXACT\",\"value\":202}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-02T04:25:02.741232+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "413edf0d30a632c4d35f0ee6c062c8bf9f27b4551b6e1a829cb403d5b8de10f5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":240},\"start\":{\"modifier\":\"EXACT\",\"value\":223}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/11",
  "retrieved_utc": "2026-11-02T04:25:02.741232+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "413edf0d30a632c4d35f0ee6c062c8bf9f27b4551b6e1a829cb403d5b8de10f5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json)

```json
{
  "evidence_id": "C16",
  "excerpt": "{\"description\":\"Helical; Name=6\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":261},\"start\":{\"modifier\":\"EXACT\",\"value\":241}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/12",
  "retrieved_utc": "2026-11-02T04:25:02.741232+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "413edf0d30a632c4d35f0ee6c062c8bf9f27b4551b6e1a829cb403d5b8de10f5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json)

```json
{
  "evidence_id": "C17",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":273},\"start\":{\"modifier\":\"EXACT\",\"value\":262}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/13",
  "retrieved_utc": "2026-11-02T04:25:02.741232+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "413edf0d30a632c4d35f0ee6c062c8bf9f27b4551b6e1a829cb403d5b8de10f5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json"
}
```

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json)

```json
{
  "evidence_id": "C18",
  "excerpt": "{\"description\":\"Helical; Name=7\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":294},\"start\":{\"modifier\":\"EXACT\",\"value\":274}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/14",
  "retrieved_utc": "2026-11-02T04:25:02.741232+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "413edf0d30a632c4d35f0ee6c062c8bf9f27b4551b6e1a829cb403d5b8de10f5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json"
}
```

### Evidence C19

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json)

```json
{
  "evidence_id": "C19",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":312},\"start\":{\"modifier\":\"EXACT\",\"value\":295}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/15",
  "retrieved_utc": "2026-11-02T04:25:02.741232+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "413edf0d30a632c4d35f0ee6c062c8bf9f27b4551b6e1a829cb403d5b8de10f5",
  "url": "https://rest.uniprot.org/uniprotkb/A0A3B3IT45.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A3B3IT45?format=txt&versions=33)

```json
{
  "entry_version": 33,
  "evidence_id": "H1",
  "excerpt": "ID   O51C1_HUMAN             Reviewed;         312 AA.\nAC   A0A3B3IT45; Q8NH68;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-DEC-2018, sequence version 1.\nDT   28-JAN-2026, entry version 33.\nDE   RecName: Full=Olfactory receptor OR51C1 {ECO:0000312|HGNC:HGNC:15191};\nGN   Name=OR51C1 {ECO:0000312|HGNC:HGNC:15191};\nGN   Synonyms=OR51C1P {ECO:0000312|HGNC:HGNC:15191}, OR51C3P, OST734;\nOS   Homo sapiens (Human).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;\nOC   Eutheria; Euarchontoglires; Primates; Haplorrhini; Catarrhini; Hominidae;\nOC   Homo.\nOX   NCBI_TaxID=9606;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:05.547773+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "baa83bf26c0bb6c7471ba5998d88f9308542ba6a5a9c7c12ad2235d34b22e1f3",
  "url": "https://rest.uniprot.org/unisave/A0A3B3IT45?format=txt&versions=33"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A3B3IT45?format=txt&versions=33)

```json
{
  "entry_version": 33,
  "evidence_id": "H2",
  "excerpt": "FT   TOPO_DOM        1..26\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:05.547773+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 104-106",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "baa83bf26c0bb6c7471ba5998d88f9308542ba6a5a9c7c12ad2235d34b22e1f3",
  "url": "https://rest.uniprot.org/unisave/A0A3B3IT45?format=txt&versions=33"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A3B3IT45?format=txt&versions=33)

```json
{
  "entry_version": 33,
  "evidence_id": "H3",
  "excerpt": "FT   TRANSMEM        27..47\nFT                   /note=\"Helical; Name=1\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:05.547773+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 107-109",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "baa83bf26c0bb6c7471ba5998d88f9308542ba6a5a9c7c12ad2235d34b22e1f3",
  "url": "https://rest.uniprot.org/unisave/A0A3B3IT45?format=txt&versions=33"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A3B3IT45?format=txt&versions=33)

```json
{
  "entry_version": 33,
  "evidence_id": "H4",
  "excerpt": "FT   TOPO_DOM        48..66\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:05.547773+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 110-112",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "baa83bf26c0bb6c7471ba5998d88f9308542ba6a5a9c7c12ad2235d34b22e1f3",
  "url": "https://rest.uniprot.org/unisave/A0A3B3IT45?format=txt&versions=33"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A3B3IT45?format=txt&versions=33)

```json
{
  "entry_version": 33,
  "evidence_id": "H5",
  "excerpt": "FT   TRANSMEM        67..87\nFT                   /note=\"Helical; Name=2\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:05.547773+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 113-115",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "baa83bf26c0bb6c7471ba5998d88f9308542ba6a5a9c7c12ad2235d34b22e1f3",
  "url": "https://rest.uniprot.org/unisave/A0A3B3IT45?format=txt&versions=33"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A3B3IT45?format=txt&versions=33)

```json
{
  "entry_version": 33,
  "evidence_id": "H6",
  "excerpt": "FT   TOPO_DOM        88..99\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:05.547773+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 116-118",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "baa83bf26c0bb6c7471ba5998d88f9308542ba6a5a9c7c12ad2235d34b22e1f3",
  "url": "https://rest.uniprot.org/unisave/A0A3B3IT45?format=txt&versions=33"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A3B3IT45?format=txt&versions=33)

```json
{
  "entry_version": 33,
  "evidence_id": "H7",
  "excerpt": "FT   TRANSMEM        100..120\nFT                   /note=\"Helical; Name=3\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:05.547773+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 119-121",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "baa83bf26c0bb6c7471ba5998d88f9308542ba6a5a9c7c12ad2235d34b22e1f3",
  "url": "https://rest.uniprot.org/unisave/A0A3B3IT45?format=txt&versions=33"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A3B3IT45?format=txt&versions=33)

```json
{
  "entry_version": 33,
  "evidence_id": "H8",
  "excerpt": "FT   TOPO_DOM        121..143\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:05.547773+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 122-124",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "baa83bf26c0bb6c7471ba5998d88f9308542ba6a5a9c7c12ad2235d34b22e1f3",
  "url": "https://rest.uniprot.org/unisave/A0A3B3IT45?format=txt&versions=33"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A3B3IT45?format=txt&versions=33)

```json
{
  "entry_version": 33,
  "evidence_id": "H9",
  "excerpt": "FT   TRANSMEM        144..164\nFT                   /note=\"Helical; Name=4\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:05.547773+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 125-127",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "baa83bf26c0bb6c7471ba5998d88f9308542ba6a5a9c7c12ad2235d34b22e1f3",
  "url": "https://rest.uniprot.org/unisave/A0A3B3IT45?format=txt&versions=33"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A3B3IT45?format=txt&versions=33)

```json
{
  "entry_version": 33,
  "evidence_id": "H10",
  "excerpt": "FT   TOPO_DOM        165..201\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:05.547773+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 128-130",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "baa83bf26c0bb6c7471ba5998d88f9308542ba6a5a9c7c12ad2235d34b22e1f3",
  "url": "https://rest.uniprot.org/unisave/A0A3B3IT45?format=txt&versions=33"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A3B3IT45?format=txt&versions=33)

```json
{
  "entry_version": 33,
  "evidence_id": "H11",
  "excerpt": "FT   TRANSMEM        202..222\nFT                   /note=\"Helical; Name=5\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:05.547773+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 131-133",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "baa83bf26c0bb6c7471ba5998d88f9308542ba6a5a9c7c12ad2235d34b22e1f3",
  "url": "https://rest.uniprot.org/unisave/A0A3B3IT45?format=txt&versions=33"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A3B3IT45?format=txt&versions=33)

```json
{
  "entry_version": 33,
  "evidence_id": "H12",
  "excerpt": "FT   TOPO_DOM        223..240\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:05.547773+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 134-136",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "baa83bf26c0bb6c7471ba5998d88f9308542ba6a5a9c7c12ad2235d34b22e1f3",
  "url": "https://rest.uniprot.org/unisave/A0A3B3IT45?format=txt&versions=33"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A3B3IT45?format=txt&versions=33)

```json
{
  "entry_version": 33,
  "evidence_id": "H13",
  "excerpt": "FT   TRANSMEM        241..261\nFT                   /note=\"Helical; Name=6\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:05.547773+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 137-139",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "baa83bf26c0bb6c7471ba5998d88f9308542ba6a5a9c7c12ad2235d34b22e1f3",
  "url": "https://rest.uniprot.org/unisave/A0A3B3IT45?format=txt&versions=33"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A3B3IT45?format=txt&versions=33)

```json
{
  "entry_version": 33,
  "evidence_id": "H14",
  "excerpt": "FT   TOPO_DOM        262..273\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:05.547773+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 140-142",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "baa83bf26c0bb6c7471ba5998d88f9308542ba6a5a9c7c12ad2235d34b22e1f3",
  "url": "https://rest.uniprot.org/unisave/A0A3B3IT45?format=txt&versions=33"
}
```

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A3B3IT45?format=txt&versions=33)

```json
{
  "entry_version": 33,
  "evidence_id": "H15",
  "excerpt": "FT   TRANSMEM        274..294\nFT                   /note=\"Helical; Name=7\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:05.547773+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 143-145",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "baa83bf26c0bb6c7471ba5998d88f9308542ba6a5a9c7c12ad2235d34b22e1f3",
  "url": "https://rest.uniprot.org/unisave/A0A3B3IT45?format=txt&versions=33"
}
```

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A3B3IT45?format=txt&versions=33)

```json
{
  "entry_version": 33,
  "evidence_id": "H16",
  "excerpt": "FT   TOPO_DOM        295..312\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:05.547773+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 146-148",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "baa83bf26c0bb6c7471ba5998d88f9308542ba6a5a9c7c12ad2235d34b22e1f3",
  "url": "https://rest.uniprot.org/unisave/A0A3B3IT45?format=txt&versions=33"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 18. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
