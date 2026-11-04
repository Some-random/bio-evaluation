# transmembrane_0128

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0128.txt)

**Task:** `transmembrane`  
**Expected answer:** **B** — 278..286; 308..323

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MQAYESGDERGLIYGYVLNGRGGGRRVGRNQIAVLDLLPEESLWLHWDRGVPEAQAWLRDSAGLSEFACDLLLEEATRPRLLDLGAESLLVFLRGVNLNPGAEPEDMVSLRVFADARRVISLRLRPLKAVADLLEDLEAGKGPKTASEVVYYLAHYLTDRVDTLISGIADQLDAVEELVEADERASPDQHQLRTLRRRSAGLRRYLAPQRDIYSQLARYKLSWFVEDDADYWNELNNRLTRNLEELELIRERISVLQEAESRRITERMNRTMYLLGIITGFFLPMSFVTGLLGINVGGIPGADAPHGFWLACLLIGGVATFQWWVFRRLRWL

[Multiple Choices]
A. 278..286; 311..325
B. 278..286; 308..323
C. 24..44; 63..83; 84..104; 151..171; 173..193
D. 278..286
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

> The sequence-matched UniProt record annotates transmembrane regions at 278..286 and 308..323, matching B. The annotations cite experimental evidence and the 7NH9 structure; this supports the key, though the primary study was not independently reviewed here.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [H5](#evidence-h5), [H7](#evidence-h7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has a C-terminal hydrophobic region consistent with membrane-spanning helices, and transferable transporter knowledge could distinguish those options from the N-terminal, mostly nonhydrophobic regions in C. It does not, however, establish whether the second span should be placed at 308..323 or 311..325: both intervals cover a strongly hydrophobic stretch.


**Missing item-specific fact**

> The exact annotated or structurally assigned boundaries of the second transmembrane segment are needed to distinguish B from A.


**Reason**

> Sequence hydropathy and family-level reasoning support the general location and number of membrane spans, but do not meaningfully resolve the small boundary shift between A and B. The keyed coordinates are supported by reviewer-only evidence, not uniquely recoverable from the original input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> A and B share the same first interval and give overlapping, strongly hydrophobic windows for the second span. The sequence alone does not specify those precise endpoints, and either window is a plausible membrane-spanning segment.


### Important caveats

- Reviewer-only annotations match the supplied sequence; the cited evidence includes experimental and structural evidence, but the underlying paper was not independently validated.
- The exact extent assigned to a transmembrane helix can depend on structural or annotation conventions.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a C-terminal hydrophobic region consistent with membrane-spanning helices, and transferable transporter knowledge could distinguish those options from the N-terminal, mostly nonhydrophobic regions in C. It does not, however, establish whether the second span should be placed at 308..323 or 311..325: both intervals cover a strongly hydrophobic stretch.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact annotated or structurally assigned boundaries of the second transmembrane segment are needed to distinguish B from A.",
    "reason": "Sequence hydropathy and family-level reasoning support the general location and number of membrane spans, but do not meaningfully resolve the small boundary shift between A and B. The keyed coordinates are supported by reviewer-only evidence, not uniquely recoverable from the original input."
  },
  "case_id": "transmembrane_0128",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C8",
      "H5",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates transmembrane regions at 278..286 and 308..323, matching B. The annotations cite experimental evidence and the 7NH9 structure; this supports the key, though the primary study was not independently reviewed here."
  },
  "important_caveats": [
    "Reviewer-only annotations match the supplied sequence; the cited evidence includes experimental and structural evidence, but the underlying paper was not independently validated.",
    "The exact extent assigned to a transmembrane helix can depend on structural or annotation conventions."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "A and B share the same first interval and give overlapping, strongly hydrophobic windows for the second span. The sequence alone does not specify those precise endpoints, and either window is a plausible membrane-spanning segment."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0128",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates transmembrane regions at 278..286 and 308..323, matching B. The annotations cite experimental evidence and the 7NH9 structure; this supports the key, though the primary study was not independently reviewed here.",
    "evidence_ids": ["C6", "C8", "H5", "H7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has a C-terminal hydrophobic region consistent with membrane-spanning helices, and transferable transporter knowledge could distinguish those options from the N-terminal, mostly nonhydrophobic regions in C. It does not, however, establish whether the second span should be placed at 308..323 or 311..325: both intervals cover a strongly hydrophobic stretch.",
    "missing_item_specific_fact": "The exact annotated or structurally assigned boundaries of the second transmembrane segment are needed to distinguish B from A.",
    "reason": "Sequence hydropathy and family-level reasoning support the general location and number of membrane spans, but do not meaningfully resolve the small boundary shift between A and B. The keyed coordinates are supported by reviewer-only evidence, not uniquely recoverable from the original input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "A and B share the same first interval and give overlapping, strongly hydrophobic windows for the second span. The sequence alone does not specify those precise endpoints, and either window is a plausible membrane-spanning segment."
  },
  "important_caveats": [
    "Reviewer-only annotations match the supplied sequence; the cited evidence includes experimental and structural evidence, but the underlying paper was not independently validated.",
    "The exact extent assigned to a transmembrane helix can depend on structural or annotation conventions."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for Q9ZIH2 (CmaX/ZntB from P. aeruginosa) records exactly two transmembrane helices: 278..286 and 308..323, both supported by cryo-EM structure PDB 7NH9 (3.03 Å) and experimental topology data (PubMed 34175341). The topological domains confirm cytoplasmic 1-277, periplasmic loop 287-307, and cytoplasmic 324-332, consistent with exactly two membrane-spanning helices at the annotated positions. Choice B matches these boundaries exactly.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C5](#evidence-c5), [C7](#evidence-c7), [C9](#evidence-c9), [H5](#evidence-h5), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Multiple layers of transferable reasoning distinguish B from the alternatives: (1) The N-terminal 277 residues are clearly soluble/cytoplasmic (high charged-residue density, no long hydrophobic stretches), eliminating C which places TMs in that region. (2) The C-terminal ~55 residues contain two distinct hydrophobic stretches separated by a more polar loop (containing P, N, D, H), indicating two TMs rather than one, eliminating D. (3) For the second TM boundary, the well-established aromatic-residue-at-membrane-interface principle (Trp/Tyr enrichment at helix termini, observed across many membrane proteins) favors boundaries at W308 and W322-W323 (choice B: 308..323) over C311 and F325 (choice A: 311..325). Trp is the most prevalent residue at the lipid-water interface in TM helices, making W-L-A...W-W a classic helix signature, while starting at Cys and ending at Phe is less characteristic.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can apply: (a) hydrophobicity/topology reasoning to eliminate C and D, (b) the aromatic-interface rule (Trp at TM boundaries, a pattern learned from hundreds of membrane protein structures) to prefer 308..323 over 311..325, and (c) the presence of two hydrophobic stretches to reject the single-TM option. The distinction between B and A rests on the Trp residues at positions 308 and 322-323, which is a transferable biophysical principle rather than a protein-specific annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While B and A differ by only 3 residues at the start and 2 at the end of the second TM, the aromatic-residue interface principle provides a clear basis for preferring B (W at both boundaries) over A (C at start, F at end). Choice C is clearly wrong (N-terminal cytoplasmic region), and D is incomplete. No genuine ambiguity remains among the offered choices.


### Important caveats

- The first TM at 278..286 is only 9 residues, unusually short for a standard alpha-helical TM (typically 18-25 residues). This likely reflects a tilted helix or partial helix in the cryo-EM structure of the ZntB/CmaX fold. Since all relevant choices (A, B, D) include this segment, the model need not independently validate its length.
- The boundary distinction between B and A (±3 residues) is at the edge of what sequence-based reasoning can resolve with certainty; the aromatic-interface argument provides a strong but not absolute basis.
- The annotation derives from a 3.03 Å cryo-EM structure (PDB 7NH9), which is experimental but has limited resolution for defining exact helix termini.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Multiple layers of transferable reasoning distinguish B from the alternatives: (1) The N-terminal 277 residues are clearly soluble/cytoplasmic (high charged-residue density, no long hydrophobic stretches), eliminating C which places TMs in that region. (2) The C-terminal ~55 residues contain two distinct hydrophobic stretches separated by a more polar loop (containing P, N, D, H), indicating two TMs rather than one, eliminating D. (3) For the second TM boundary, the well-established aromatic-residue-at-membrane-interface principle (Trp/Tyr enrichment at helix termini, observed across many membrane proteins) favors boundaries at W308 and W322-W323 (choice B: 308..323) over C311 and F325 (choice A: 311..325). Trp is the most prevalent residue at the lipid-water interface in TM helices, making W-L-A...W-W a classic helix signature, while starting at Cys and ending at Phe is less characteristic.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can apply: (a) hydrophobicity/topology reasoning to eliminate C and D, (b) the aromatic-interface rule (Trp at TM boundaries, a pattern learned from hundreds of membrane protein structures) to prefer 308..323 over 311..325, and (c) the presence of two hydrophobic stretches to reject the single-TM option. The distinction between B and A rests on the Trp residues at positions 308 and 322-323, which is a transferable biophysical principle rather than a protein-specific annotation."
  },
  "case_id": "transmembrane_0128",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C8",
      "C5",
      "C7",
      "C9",
      "H5",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for Q9ZIH2 (CmaX/ZntB from P. aeruginosa) records exactly two transmembrane helices: 278..286 and 308..323, both supported by cryo-EM structure PDB 7NH9 (3.03 Å) and experimental topology data (PubMed 34175341). The topological domains confirm cytoplasmic 1-277, periplasmic loop 287-307, and cytoplasmic 324-332, consistent with exactly two membrane-spanning helices at the annotated positions. Choice B matches these boundaries exactly."
  },
  "important_caveats": [
    "The first TM at 278..286 is only 9 residues, unusually short for a standard alpha-helical TM (typically 18-25 residues). This likely reflects a tilted helix or partial helix in the cryo-EM structure of the ZntB/CmaX fold. Since all relevant choices (A, B, D) include this segment, the model need not independently validate its length.",
    "The boundary distinction between B and A (±3 residues) is at the edge of what sequence-based reasoning can resolve with certainty; the aromatic-interface argument provides a strong but not absolute basis.",
    "The annotation derives from a 3.03 Å cryo-EM structure (PDB 7NH9), which is experimental but has limited resolution for defining exact helix termini."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While B and A differ by only 3 residues at the start and 2 at the end of the second TM, the aromatic-residue interface principle provides a clear basis for preferring B (W at both boundaries) over A (C at start, F at end). Choice C is clearly wrong (N-terminal cytoplasmic region), and D is incomplete. No genuine ambiguity remains among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0128",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for Q9ZIH2 (CmaX/ZntB from P. aeruginosa) records exactly two transmembrane helices: 278..286 and 308..323, both supported by cryo-EM structure PDB 7NH9 (3.03 Å) and experimental topology data (PubMed 34175341). The topological domains confirm cytoplasmic 1-277, periplasmic loop 287-307, and cytoplasmic 324-332, consistent with exactly two membrane-spanning helices at the annotated positions. Choice B matches these boundaries exactly.",
    "evidence_ids": ["C6", "C8", "C5", "C7", "C9", "H5", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Multiple layers of transferable reasoning distinguish B from the alternatives: (1) The N-terminal 277 residues are clearly soluble/cytoplasmic (high charged-residue density, no long hydrophobic stretches), eliminating C which places TMs in that region. (2) The C-terminal ~55 residues contain two distinct hydrophobic stretches separated by a more polar loop (containing P, N, D, H), indicating two TMs rather than one, eliminating D. (3) For the second TM boundary, the well-established aromatic-residue-at-membrane-interface principle (Trp/Tyr enrichment at helix termini, observed across many membrane proteins) favors boundaries at W308 and W322-W323 (choice B: 308..323) over C311 and F325 (choice A: 311..325). Trp is the most prevalent residue at the lipid-water interface in TM helices, making W-L-A...W-W a classic helix signature, while starting at Cys and ending at Phe is less characteristic.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can apply: (a) hydrophobicity/topology reasoning to eliminate C and D, (b) the aromatic-interface rule (Trp at TM boundaries, a pattern learned from hundreds of membrane protein structures) to prefer 308..323 over 311..325, and (c) the presence of two hydrophobic stretches to reject the single-TM option. The distinction between B and A rests on the Trp residues at positions 308 and 322-323, which is a transferable biophysical principle rather than a protein-specific annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While B and A differ by only 3 residues at the start and 2 at the end of the second TM, the aromatic-residue interface principle provides a clear basis for preferring B (W at both boundaries) over A (C at start, F at end). Choice C is clearly wrong (N-terminal cytoplasmic region), and D is incomplete. No genuine ambiguity remains among the offered choices."
  },
  "important_caveats": [
    "The first TM at 278..286 is only 9 residues, unusually short for a standard alpha-helical TM (typically 18-25 residues). This likely reflects a tilted helix or partial helix in the cryo-EM structure of the ZntB/CmaX fold. Since all relevant choices (A, B, D) include this segment, the model need not independently validate its length.",
    "The boundary distinction between B and A (±3 residues) is at the edge of what sequence-based reasoning can resolve with certainty; the aromatic-interface argument provides a strong but not absolute basis.",
    "The annotation derives from a 3.03 Å cryo-EM structure (PDB 7NH9), which is experimental but has limited resolution for defining exact helix termini."
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
  "benchmark_sequence_length": 332,
  "benchmark_sequence_sha256": "988a45b94bdf9854fe2938f5dca65ebc73a07414f1d018dcbbc91c52ce85ad8a",
  "current_entry_audit": {
    "entryVersion": 155,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "1999-05-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "a00f4c0271bbd4fae7afeb16e71be27aaff79dadde11086a04686cc2d5355d0e",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 332,
  "current_source_sequence_sha256": "988a45b94bdf9854fe2938f5dca65ebc73a07414f1d018dcbbc91c52ce85ad8a",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 153,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9ZIH2",
  "selected_historical_entry_version": 153,
  "selected_historical_record_sha256": "ef1f3b913665475f320bd32d9a7e46b733d69ecc2d4104881ec5fd04fc3481b9",
  "selected_historical_source_sequence_length": 332,
  "selected_historical_source_sequence_sha256": "988a45b94bdf9854fe2938f5dca65ebc73a07414f1d018dcbbc91c52ce85ad8a",
  "selected_historical_version": {
    "accession": "Q9ZIH2",
    "database": "Swiss-Prot",
    "entryVersion": 153,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CMAX_PSEAE",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZIH2.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9ZIH2\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:33:54.880542+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a00f4c0271bbd4fae7afeb16e71be27aaff79dadde11086a04686cc2d5355d0e",
  "url": "https://rest.uniprot.org/uniprotkb/Q9ZIH2.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZIH2.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":155,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"1999-05-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:33:54.880542+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a00f4c0271bbd4fae7afeb16e71be27aaff79dadde11086a04686cc2d5355d0e",
  "url": "https://rest.uniprot.org/uniprotkb/Q9ZIH2.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZIH2.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Pseudomonadales\",\"Pseudomonadaceae\",\"Pseudomonas\"],\"scientificName\":\"Pseudomonas aeruginosa (strain ATCC 15692 / DSM 22644 / CIP 104116 / JCM 14847 / LMG 12228 / 1C / PRS 101 / PAO1)\",\"taxonId\":208964}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:33:54.880542+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a00f4c0271bbd4fae7afeb16e71be27aaff79dadde11086a04686cc2d5355d0e",
  "url": "https://rest.uniprot.org/uniprotkb/Q9ZIH2.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZIH2.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Divalent cation transporter CmaX\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:33:54.880542+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a00f4c0271bbd4fae7afeb16e71be27aaff79dadde11086a04686cc2d5355d0e",
  "url": "https://rest.uniprot.org/uniprotkb/Q9ZIH2.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZIH2.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"34175341\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":277},\"start\":{\"modifier\":\"EXACT\",\"value\":1}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:33:54.880542+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a00f4c0271bbd4fae7afeb16e71be27aaff79dadde11086a04686cc2d5355d0e",
  "url": "https://rest.uniprot.org/uniprotkb/Q9ZIH2.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZIH2.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"34175341\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7NH9\",\"source\":\"PDB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":286},\"start\":{\"modifier\":\"EXACT\",\"value\":278}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:33:54.880542+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a00f4c0271bbd4fae7afeb16e71be27aaff79dadde11086a04686cc2d5355d0e",
  "url": "https://rest.uniprot.org/uniprotkb/Q9ZIH2.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZIH2.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Periplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"34175341\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":307},\"start\":{\"modifier\":\"EXACT\",\"value\":287}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:33:54.880542+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a00f4c0271bbd4fae7afeb16e71be27aaff79dadde11086a04686cc2d5355d0e",
  "url": "https://rest.uniprot.org/uniprotkb/Q9ZIH2.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZIH2.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"34175341\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7NH9\",\"source\":\"PDB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":323},\"start\":{\"modifier\":\"EXACT\",\"value\":308}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:33:54.880542+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a00f4c0271bbd4fae7afeb16e71be27aaff79dadde11086a04686cc2d5355d0e",
  "url": "https://rest.uniprot.org/uniprotkb/Q9ZIH2.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZIH2.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"34175341\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":332},\"start\":{\"modifier\":\"EXACT\",\"value\":324}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:33:54.880542+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a00f4c0271bbd4fae7afeb16e71be27aaff79dadde11086a04686cc2d5355d0e",
  "url": "https://rest.uniprot.org/uniprotkb/Q9ZIH2.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZIH2.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Stetsenko A.\",\"Stehantsev P.\",\"Dranenko N.O.\",\"Gelfand M.S.\",\"Guskov A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"34175341\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.ijbiomac.2021.06.130\"}],\"citationType\":\"journal article\",\"firstPage\":\"760\",\"id\":\"34175341\",\"journal\":\"Int. J. Biol. Macromol.\",\"lastPage\":\"767\",\"publicationDate\":\"2021\",\"title\":\"Structural and biochemical characterization of a novel ZntB (CmaX) transporter protein from Pseudomonas aeruginosa.\",\"volume\":\"184\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7NH9\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC 15692 / DSM 22644 / CIP 104116 / JCM 14847 / LMG 12228 / 1C / PRS 101 / PAO1\"}],\"referenceNumber\":3,\"referencePositions\":[\"STRUCTURE BY ELECTRON MICROSCOPY (3.03 ANGSTROMS)\",\"FUNCTION\",\"TRANSPORTER ACTIVITY\",\"SUBUNIT\",\"SUBCELLULAR LOCATION\",\"TOPOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:33:54.880542+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a00f4c0271bbd4fae7afeb16e71be27aaff79dadde11086a04686cc2d5355d0e",
  "url": "https://rest.uniprot.org/uniprotkb/Q9ZIH2.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZIH2?format=txt&versions=153)

```json
{
  "entry_version": 153,
  "evidence_id": "H1",
  "excerpt": "ID   CMAX_PSEAE              Reviewed;         332 AA.\nAC   Q9ZIH2; A0A1S1C048; G3XD00; Q7DCE5;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAY-1999, sequence version 1.\nDT   28-JAN-2026, entry version 153.\nDE   RecName: Full=Divalent cation transporter CmaX {ECO:0000305};\nGN   Name=cmaX {ECO:0000303|PubMed:10438740, ECO:0000303|PubMed:34175341};\nGN   Synonyms=zntB {ECO:0000303|PubMed:34175341};\nGN   OrderedLocusNames=PA1773 {ECO:0000312|EMBL:AAG05162.1};\nOS   Pseudomonas aeruginosa (strain ATCC 15692 / DSM 22644 / CIP 104116 / JCM\nOS   14847 / LMG 12228 / 1C / PRS 101 / PAO1).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Pseudomonadales; Pseudomonadaceae; Pseudomonas.\nOX   NCBI_TaxID=208964;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:58.139616+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ef1f3b913665475f320bd32d9a7e46b733d69ecc2d4104881ec5fd04fc3481b9",
  "url": "https://rest.uniprot.org/unisave/Q9ZIH2?format=txt&versions=153"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZIH2?format=txt&versions=153)

```json
{
  "entry_version": 153,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:AAD11565.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA].\nRC   STRAIN=ATCC 15692 / DSM 22644 / CIP 104116 / JCM 14847 / LMG 12228 / 1C /\nRC   PRS 101 / PAO1;\nRX   PubMed=10438740; DOI=10.1128/jb.181.16.4746-4754.1999;\nRA   Brinkman F.S., Schoofs G., Hancock R.E., De Mot R.;\nRT   \"Influence of a putative ECF sigma factor on expression of the major outer\nRT   membrane protein, OprF, in Pseudomonas aeruginosa and Pseudomonas\nRT   fluorescens.\";\nRL   J. Bacteriol. 181:4746-4754(1999).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:58.139616+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 15-24",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ef1f3b913665475f320bd32d9a7e46b733d69ecc2d4104881ec5fd04fc3481b9",
  "url": "https://rest.uniprot.org/unisave/Q9ZIH2?format=txt&versions=153"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZIH2?format=txt&versions=153)

```json
{
  "entry_version": 153,
  "evidence_id": "H3",
  "excerpt": "RN   [3] {ECO:0007744|PDB:7NH9}\nRP   STRUCTURE BY ELECTRON MICROSCOPY (3.03 ANGSTROMS), FUNCTION, TRANSPORTER\nRP   ACTIVITY, SUBUNIT, SUBCELLULAR LOCATION, AND TOPOLOGY.\nRC   STRAIN=ATCC 15692 / DSM 22644 / CIP 104116 / JCM 14847 / LMG 12228 / 1C /\nRC   PRS 101 / PAO1;\nRX   PubMed=34175341; DOI=10.1016/j.ijbiomac.2021.06.130;\nRA   Stetsenko A., Stehantsev P., Dranenko N.O., Gelfand M.S., Guskov A.;\nRT   \"Structural and biochemical characterization of a novel ZntB (CmaX)\nRT   transporter protein from Pseudomonas aeruginosa.\";\nRL   Int. J. Biol. Macromol. 184:760-767(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:58.139616+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 39-48",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ef1f3b913665475f320bd32d9a7e46b733d69ecc2d4104881ec5fd04fc3481b9",
  "url": "https://rest.uniprot.org/unisave/Q9ZIH2?format=txt&versions=153"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZIH2?format=txt&versions=153)

```json
{
  "entry_version": 153,
  "evidence_id": "H4",
  "excerpt": "FT   TOPO_DOM        1..277\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000269|PubMed:34175341\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:58.139616+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 122-124",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ef1f3b913665475f320bd32d9a7e46b733d69ecc2d4104881ec5fd04fc3481b9",
  "url": "https://rest.uniprot.org/unisave/Q9ZIH2?format=txt&versions=153"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZIH2?format=txt&versions=153)

```json
{
  "entry_version": 153,
  "evidence_id": "H5",
  "excerpt": "FT   TRANSMEM        278..286\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000269|PubMed:34175341,\nFT                   ECO:0007744|PDB:7NH9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:58.139616+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 125-128",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ef1f3b913665475f320bd32d9a7e46b733d69ecc2d4104881ec5fd04fc3481b9",
  "url": "https://rest.uniprot.org/unisave/Q9ZIH2?format=txt&versions=153"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZIH2?format=txt&versions=153)

```json
{
  "entry_version": 153,
  "evidence_id": "H6",
  "excerpt": "FT   TOPO_DOM        287..307\nFT                   /note=\"Periplasmic\"\nFT                   /evidence=\"ECO:0000269|PubMed:34175341\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:58.139616+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 129-131",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ef1f3b913665475f320bd32d9a7e46b733d69ecc2d4104881ec5fd04fc3481b9",
  "url": "https://rest.uniprot.org/unisave/Q9ZIH2?format=txt&versions=153"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZIH2?format=txt&versions=153)

```json
{
  "entry_version": 153,
  "evidence_id": "H7",
  "excerpt": "FT   TRANSMEM        308..323\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000269|PubMed:34175341,\nFT                   ECO:0007744|PDB:7NH9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:58.139616+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 132-135",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ef1f3b913665475f320bd32d9a7e46b733d69ecc2d4104881ec5fd04fc3481b9",
  "url": "https://rest.uniprot.org/unisave/Q9ZIH2?format=txt&versions=153"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZIH2?format=txt&versions=153)

```json
{
  "entry_version": 153,
  "evidence_id": "H8",
  "excerpt": "FT   TOPO_DOM        324..332\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000269|PubMed:34175341\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:58.139616+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 136-138",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ef1f3b913665475f320bd32d9a7e46b733d69ecc2d4104881ec5fd04fc3481b9",
  "url": "https://rest.uniprot.org/unisave/Q9ZIH2?format=txt&versions=153"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 128. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
