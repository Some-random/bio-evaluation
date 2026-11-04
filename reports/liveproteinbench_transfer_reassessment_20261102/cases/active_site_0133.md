# active_site_0133

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0133.txt)

**Task:** `active_site`  
**Expected answer:** **B** — Position 318 (O-(5&#x27;-phospho-DNA)-tyrosine intermediate)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MNLCNVNNYYLIIAEKSKAAKKIAEALSEKPILCRKYNVSYWIIKDHNSSKYVIVPAAGHLFGLKGESGFPVYDADWKPLWEIDKNSYYTKRYYQLISSLSKYALGFINACDYDIEGSVIGYLIIKNLGDIKKAKRMKFSALTKSDILSAFRNISALDYDMINAGIARHKIDWLWGINVSRALMISLQDFAKKRVILSAGRVQSPTLVQVVNSEIERNLFIPLPKFTVSIIVKIKDYSLNIKVNKEFEKITEAKEFLNKLINKTVKVVEVENRVRLLERPSPFNLTDLQIEAGRIYGISPYNVERIAEDLYLDGLISYPRTNSQKIPSTISIYNIIKGLENSSYRKLVDLVRKITGGKYVVKQGIKDDPAHPAIHPTGEAPKNLPNSKFKIYDLIARRFLGSVSADAKLSNTIYTLKVSDFPLEFTVSYTKILERNWLDIYHFHNVKEDKPIFLSKGDEGKIVDGKVNISLSKPTSRYTKVSLLKWMESSNLGTEATRGRIIEILVKRKYLTNNGRYIIPTKLGFYIAEILNKFFPDIVDVRMTADMESKLEMIKTGKVLESKVIKENIEKLNKFIEEYKVNKDKVGESLAKALGLIKIVKCKYCDLEQYKDGLCKYHYEAKVRLLDAVEIWKERTKYDHKKILKRISSSKSTGKYVKDIVTYMLSSE

[Multiple Choices]
A. Position 1142 (Proton donor; for dehydratase activity 1)
B. Position 318 (O-(5'-phospho-DNA)-tyrosine intermediate)
C. Position 976 (Proton acceptor; for dehydratase activity 1)
D. Position 70 (Acyl-ester intermediate)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Active Site Prediction, which is to identify the key amino acid residues that form the active site of an enzyme. The active site is the specific region on the enzyme where a substrate binds and the chemical reaction is catalyzed. Based on the full protein sequence provided, you must select the option that correctly lists the amino acid residues (by their type and position) that constitute the enzyme's catalytic center.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt annotation assigns position 318 the DNA-phosphotyrosine intermediate role. This is a computational PROSITE-ProRule annotation, not direct experimental evidence in the supplied excerpts, but it accords with the established catalytic mechanism of type IA topoisomerases.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a type IA topoisomerase, whose conserved catalytic tyrosine forms a transient covalent phosphotyrosine linkage to DNA. That family-level mechanism matches option B; the dehydratase and acyl-ester alternatives describe different chemistries. Also, the sequence is only 668 residues long, so the positions in A and C are outside it.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family recognition and the conserved topoisomerase catalytic mechanism meaningfully distinguish B among the offered choices, without requiring recall of this exact protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only B matches the expected topoisomerase DNA-phosphotyrosine mechanism; A and C give out-of-range positions, and D proposes a different intermediate.


### Important caveats

- The cited active-site annotation is rule-based computational evidence, not direct experimental confirmation in these excerpts.
- The source record matches the sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a type IA topoisomerase, whose conserved catalytic tyrosine forms a transient covalent phosphotyrosine linkage to DNA. That family-level mechanism matches option B; the dehydratase and acyl-ester alternatives describe different chemistries. Also, the sequence is only 668 residues long, so the positions in A and C are outside it.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family recognition and the conserved topoisomerase catalytic mechanism meaningfully distinguish B among the offered choices, without requiring recall of this exact protein's annotation."
  },
  "case_id": "active_site_0133",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns position 318 the DNA-phosphotyrosine intermediate role. This is a computational PROSITE-ProRule annotation, not direct experimental evidence in the supplied excerpts, but it accords with the established catalytic mechanism of type IA topoisomerases."
  },
  "important_caveats": [
    "The cited active-site annotation is rule-based computational evidence, not direct experimental confirmation in these excerpts.",
    "The source record matches the sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only B matches the expected topoisomerase DNA-phosphotyrosine mechanism; A and C give out-of-range positions, and D proposes a different intermediate."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0133",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns position 318 the DNA-phosphotyrosine intermediate role. This is a computational PROSITE-ProRule annotation, not direct experimental evidence in the supplied excerpts, but it accords with the established catalytic mechanism of type IA topoisomerases.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a type IA topoisomerase, whose conserved catalytic tyrosine forms a transient covalent phosphotyrosine linkage to DNA. That family-level mechanism matches option B; the dehydratase and acyl-ester alternatives describe different chemistries. Also, the sequence is only 668 residues long, so the positions in A and C are outside it.",
    "missing_item_specific_fact": "",
    "reason": "Family recognition and the conserved topoisomerase catalytic mechanism meaningfully distinguish B among the offered choices, without requiring recall of this exact protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only B matches the expected topoisomerase DNA-phosphotyrosine mechanism; A and C give out-of-range positions, and D proposes a different intermediate."
  },
  "important_caveats": [
    "The cited active-site annotation is rule-based computational evidence, not direct experimental confirmation in these excerpts.",
    "The source record matches the sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q97ZJ8 (DNA topoisomerase 3 from Saccharolobus solfataricus) annotates position 318 as the active site with description 'O-(5'-phospho-DNA)-tyrosine intermediate' (evidence C5/H4). The residue at position 318 in the supplied sequence is indeed Tyrosine (Y), embedded in the conserved 'ISY' motif (I316-S317-Y318) characteristic of type IA topoisomerases. The annotation is computational (ECO:0000255, PROSITE-ProRule PRU01383), but the underlying catalytic mechanism of type IA topoisomerases forming a covalent phosphotyrosyl intermediate with DNA is well-established experimentally across the family. The sequence matches the benchmark exactly (SHA-256 confirmed).

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model can identify this protein as a type IA topoisomerase (Topo III) from several transferable features: (1) the C-terminal zinc-binding domain with Cys residues near positions 602-618, characteristic of Topo III; (2) the conserved 'ISY' catalytic motif at positions 316-318, which is the hallmark active-site signature of type IA topoisomerases identified by PROSITE pattern PRU01383; (3) the overall domain architecture. Type IA topoisomerases universally use a catalytic tyrosine to form a covalent O-(5'-phospho-DNA)-tyrosyl intermediate — this is the defining chemistry of the family. The distractors are easily eliminated: positions 1142 (A) and 976 (C) exceed the protein's 668-residue length; position 70 (D) is a Proline, and 'acyl-ester intermediate' describes serine hydrolase chemistry, not topoisomerase chemistry. The 'ISY' motif is a well-known conserved feature shared across Topo I, Topo III, and related type IA enzymes, making the catalytic tyrosine position identifiable by family-level pattern recognition and counting.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The answer can be reached by recognizing the protein as a type IA topoisomerase from its domain architecture (zinc finger, overall fold), identifying the conserved ISY catalytic motif, knowing the family mechanism (phosphotyrosyl intermediate), and eliminating impossible distractors (positions beyond protein length, wrong residue type/mechanism). This relies on transferable knowledge of the type IA topoisomerase family, not on recalling this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A (position 1142) and C (position 976) are beyond the 668-residue protein length, making them trivially impossible. Option D (position 70, acyl-ester intermediate) describes a Proline residue and a serine-hydrolase mechanism incompatible with topoisomerase chemistry. Only option B is consistent with the protein's identity, length, residue type, and mechanism.


### Important caveats

- The active-site annotation is computational (PROSITE-ProRule, ECO:0000255), not directly experimental for this specific protein, though the underlying mechanism is well-established for the type IA topoisomerase family.
- The protein was historically annotated as 'DNA topoisomerase III' (SsTop3/SsTopA); the current UniProt entry uses 'DNA topoisomerase 3'.
- The Zn(2+)-binding residues at positions 602, 605, 615, 618 are supported by PDB structures 6K8N/6K8O, confirming the Topo III zinc-finger domain and supporting family identification.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can identify this protein as a type IA topoisomerase (Topo III) from several transferable features: (1) the C-terminal zinc-binding domain with Cys residues near positions 602-618, characteristic of Topo III; (2) the conserved 'ISY' catalytic motif at positions 316-318, which is the hallmark active-site signature of type IA topoisomerases identified by PROSITE pattern PRU01383; (3) the overall domain architecture. Type IA topoisomerases universally use a catalytic tyrosine to form a covalent O-(5'-phospho-DNA)-tyrosyl intermediate — this is the defining chemistry of the family. The distractors are easily eliminated: positions 1142 (A) and 976 (C) exceed the protein's 668-residue length; position 70 (D) is a Proline, and 'acyl-ester intermediate' describes serine hydrolase chemistry, not topoisomerase chemistry. The 'ISY' motif is a well-known conserved feature shared across Topo I, Topo III, and related type IA enzymes, making the catalytic tyrosine position identifiable by family-level pattern recognition and counting.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The answer can be reached by recognizing the protein as a type IA topoisomerase from its domain architecture (zinc finger, overall fold), identifying the conserved ISY catalytic motif, knowing the family mechanism (phosphotyrosyl intermediate), and eliminating impossible distractors (positions beyond protein length, wrong residue type/mechanism). This relies on transferable knowledge of the type IA topoisomerase family, not on recalling this specific protein's database entry."
  },
  "case_id": "active_site_0133",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q97ZJ8 (DNA topoisomerase 3 from Saccharolobus solfataricus) annotates position 318 as the active site with description 'O-(5'-phospho-DNA)-tyrosine intermediate' (evidence C5/H4). The residue at position 318 in the supplied sequence is indeed Tyrosine (Y), embedded in the conserved 'ISY' motif (I316-S317-Y318) characteristic of type IA topoisomerases. The annotation is computational (ECO:0000255, PROSITE-ProRule PRU01383), but the underlying catalytic mechanism of type IA topoisomerases forming a covalent phosphotyrosyl intermediate with DNA is well-established experimentally across the family. The sequence matches the benchmark exactly (SHA-256 confirmed)."
  },
  "important_caveats": [
    "The active-site annotation is computational (PROSITE-ProRule, ECO:0000255), not directly experimental for this specific protein, though the underlying mechanism is well-established for the type IA topoisomerase family.",
    "The protein was historically annotated as 'DNA topoisomerase III' (SsTop3/SsTopA); the current UniProt entry uses 'DNA topoisomerase 3'.",
    "The Zn(2+)-binding residues at positions 602, 605, 615, 618 are supported by PDB structures 6K8N/6K8O, confirming the Topo III zinc-finger domain and supporting family identification."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A (position 1142) and C (position 976) are beyond the 668-residue protein length, making them trivially impossible. Option D (position 70, acyl-ester intermediate) describes a Proline residue and a serine-hydrolase mechanism incompatible with topoisomerase chemistry. Only option B is consistent with the protein's identity, length, residue type, and mechanism."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0133",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q97ZJ8 (DNA topoisomerase 3 from Saccharolobus solfataricus) annotates position 318 as the active site with description 'O-(5'-phospho-DNA)-tyrosine intermediate' (evidence C5/H4). The residue at position 318 in the supplied sequence is indeed Tyrosine (Y), embedded in the conserved 'ISY' motif (I316-S317-Y318) characteristic of type IA topoisomerases. The annotation is computational (ECO:0000255, PROSITE-ProRule PRU01383), but the underlying catalytic mechanism of type IA topoisomerases forming a covalent phosphotyrosyl intermediate with DNA is well-established experimentally across the family. The sequence matches the benchmark exactly (SHA-256 confirmed).",
    "evidence_ids": ["C5", "H4", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model can identify this protein as a type IA topoisomerase (Topo III) from several transferable features: (1) the C-terminal zinc-binding domain with Cys residues near positions 602-618, characteristic of Topo III; (2) the conserved 'ISY' catalytic motif at positions 316-318, which is the hallmark active-site signature of type IA topoisomerases identified by PROSITE pattern PRU01383; (3) the overall domain architecture. Type IA topoisomerases universally use a catalytic tyrosine to form a covalent O-(5'-phospho-DNA)-tyrosyl intermediate — this is the defining chemistry of the family. The distractors are easily eliminated: positions 1142 (A) and 976 (C) exceed the protein's 668-residue length; position 70 (D) is a Proline, and 'acyl-ester intermediate' describes serine hydrolase chemistry, not topoisomerase chemistry. The 'ISY' motif is a well-known conserved feature shared across Topo I, Topo III, and related type IA enzymes, making the catalytic tyrosine position identifiable by family-level pattern recognition and counting.",
    "missing_item_specific_fact": "",
    "reason": "The answer can be reached by recognizing the protein as a type IA topoisomerase from its domain architecture (zinc finger, overall fold), identifying the conserved ISY catalytic motif, knowing the family mechanism (phosphotyrosyl intermediate), and eliminating impossible distractors (positions beyond protein length, wrong residue type/mechanism). This relies on transferable knowledge of the type IA topoisomerase family, not on recalling this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A (position 1142) and C (position 976) are beyond the 668-residue protein length, making them trivially impossible. Option D (position 70, acyl-ester intermediate) describes a Proline residue and a serine-hydrolase mechanism incompatible with topoisomerase chemistry. Only option B is consistent with the protein's identity, length, residue type, and mechanism."
  },
  "important_caveats": [
    "The active-site annotation is computational (PROSITE-ProRule, ECO:0000255), not directly experimental for this specific protein, though the underlying mechanism is well-established for the type IA topoisomerase family.",
    "The protein was historically annotated as 'DNA topoisomerase III' (SsTop3/SsTopA); the current UniProt entry uses 'DNA topoisomerase 3'.",
    "The Zn(2+)-binding residues at positions 602, 605, 615, 618 are supported by PDB structures 6K8N/6K8O, confirming the Topo III zinc-finger domain and supporting family identification."
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
  "benchmark_sequence_length": 668,
  "benchmark_sequence_sha256": "f752bca03e316d62a9e83d6521be1e3d49c8db05486d213a3b3d45c489790488",
  "current_entry_audit": {
    "entryVersion": 134,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2001-10-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "4ec40a69735e225949e29a9f2298e3634559e703f08ec9c5d619bb337f1a11d5",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 668,
  "current_source_sequence_sha256": "f752bca03e316d62a9e83d6521be1e3d49c8db05486d213a3b3d45c489790488",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 132,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q97ZJ8",
  "selected_historical_entry_version": 132,
  "selected_historical_record_sha256": "77a05af9d1305445b3e0d4b67305724443fad1a6fc01422e81a6d8f5dc26d379",
  "selected_historical_source_sequence_length": 668,
  "selected_historical_source_sequence_sha256": "f752bca03e316d62a9e83d6521be1e3d49c8db05486d213a3b3d45c489790488",
  "selected_historical_version": {
    "accession": "Q97ZJ8",
    "database": "Swiss-Prot",
    "entryVersion": 132,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "TOP3_SACS2",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q97ZJ8.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q97ZJ8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:26.328266+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4ec40a69735e225949e29a9f2298e3634559e703f08ec9c5d619bb337f1a11d5",
  "url": "https://rest.uniprot.org/uniprotkb/Q97ZJ8.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q97ZJ8.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":134,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2001-10-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:26.328266+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4ec40a69735e225949e29a9f2298e3634559e703f08ec9c5d619bb337f1a11d5",
  "url": "https://rest.uniprot.org/uniprotkb/Q97ZJ8.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q97ZJ8.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Sulfolobus solfataricus\",\"lineage\":[\"Archaea\",\"Thermoproteota\",\"Thermoprotei\",\"Sulfolobales\",\"Sulfolobaceae\",\"Saccharolobus\"],\"scientificName\":\"Saccharolobus solfataricus (strain ATCC 35092 / DSM 1617 / JCM 11322 / P2)\",\"taxonId\":273057}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:26.328266+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4ec40a69735e225949e29a9f2298e3634559e703f08ec9c5d619bb337f1a11d5",
  "url": "https://rest.uniprot.org/uniprotkb/Q97ZJ8.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q97ZJ8.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"29253195\",\"source\":\"PubMed\"}],\"value\":\"DNA topoisomerase III\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"22722926\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29253195\",\"source\":\"PubMed\"}],\"value\":\"5.6.2.1\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"22722926\",\"source\":\"PubMed\"}],\"value\":\"DNA topoisomerase 3\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"22722926\",\"source\":\"PubMed\"}],\"value\":\"SsTop3\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"29253195\",\"source\":\"PubMed\"}],\"value\":\"SsTopA\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:26.328266+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4ec40a69735e225949e29a9f2298e3634559e703f08ec9c5d619bb337f1a11d5",
  "url": "https://rest.uniprot.org/uniprotkb/Q97ZJ8.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q97ZJ8.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"O-(5'-phospho-DNA)-tyrosine intermediate\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01383\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":318},\"start\":{\"modifier\":\"EXACT\",\"value\":318}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-01T06:25:26.328266+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4ec40a69735e225949e29a9f2298e3634559e703f08ec9c5d619bb337f1a11d5",
  "url": "https://rest.uniprot.org/uniprotkb/Q97ZJ8.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q97ZJ8.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6K8N\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6K8O\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29105\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29105\",\"name\":\"Zn(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":602},\"start\":{\"modifier\":\"EXACT\",\"value\":602}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-01T06:25:26.328266+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4ec40a69735e225949e29a9f2298e3634559e703f08ec9c5d619bb337f1a11d5",
  "url": "https://rest.uniprot.org/uniprotkb/Q97ZJ8.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q97ZJ8.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6K8N\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6K8O\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29105\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29105\",\"name\":\"Zn(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":605},\"start\":{\"modifier\":\"EXACT\",\"value\":605}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-01T06:25:26.328266+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4ec40a69735e225949e29a9f2298e3634559e703f08ec9c5d619bb337f1a11d5",
  "url": "https://rest.uniprot.org/uniprotkb/Q97ZJ8.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q97ZJ8.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6K8N\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6K8O\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29105\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29105\",\"name\":\"Zn(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":615},\"start\":{\"modifier\":\"EXACT\",\"value\":615}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-01T06:25:26.328266+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4ec40a69735e225949e29a9f2298e3634559e703f08ec9c5d619bb337f1a11d5",
  "url": "https://rest.uniprot.org/uniprotkb/Q97ZJ8.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q97ZJ8.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6K8N\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6K8O\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29105\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29105\",\"name\":\"Zn(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":618},\"start\":{\"modifier\":\"EXACT\",\"value\":618}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-01T06:25:26.328266+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4ec40a69735e225949e29a9f2298e3634559e703f08ec9c5d619bb337f1a11d5",
  "url": "https://rest.uniprot.org/uniprotkb/Q97ZJ8.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q97ZJ8.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Valenti A.\",\"De Felice M.\",\"Perugino G.\",\"Bizard A.\",\"Nadal M.\",\"Rossi M.\",\"Ciaramella M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"22722926\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m112.366377\"}],\"citationType\":\"journal article\",\"firstPage\":\"30282\",\"id\":\"22722926\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"30295\",\"publicationDate\":\"2012\",\"title\":\"Synergic and opposing activities of thermophilic RecQ-like helicase and topoisomerase 3 proteins in Holliday junction processing and replication fork stabilization.\",\"volume\":\"287\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"SUBUNIT\",\"INTERACTION WITH LHR\",\"DNA-BINDING\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:25:26.328266+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4ec40a69735e225949e29a9f2298e3634559e703f08ec9c5d619bb337f1a11d5",
  "url": "https://rest.uniprot.org/uniprotkb/Q97ZJ8.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q97ZJ8.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"citation\":{\"authors\":[\"Bizard A.H.\",\"Yang X.\",\"Debat H.\",\"Fogg J.M.\",\"Zechiedrich L.\",\"Strick T.R.\",\"Garnier F.\",\"Nadal M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"29253195\"},{\"database\":\"DOI\",\"id\":\"10.1093/nar/gkx1247\"}],\"citationType\":\"journal article\",\"firstPage\":\"861\",\"id\":\"29253195\",\"journal\":\"Nucleic Acids Res.\",\"lastPage\":\"872\",\"publicationDate\":\"2018\",\"title\":\"TopA, the Sulfolobus solfataricus topoisomerase III, is a decatenase.\",\"volume\":\"46\"},\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"ACTIVITY REGULATION\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-01T06:25:26.328266+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4ec40a69735e225949e29a9f2298e3634559e703f08ec9c5d619bb337f1a11d5",
  "url": "https://rest.uniprot.org/uniprotkb/Q97ZJ8.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q97ZJ8?format=txt&versions=132)

```json
{
  "entry_version": 132,
  "evidence_id": "H1",
  "excerpt": "ID   TOP3_SACS2              Reviewed;         668 AA.\nAC   Q97ZJ8;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-OCT-2001, sequence version 1.\nDT   28-JAN-2026, entry version 132.\nDE   RecName: Full=DNA topoisomerase 3 {ECO:0000303|PubMed:22722926};\nDE            Short=SsTop3 {ECO:0000303|PubMed:22722926};\nDE            Short=SsTopA {ECO:0000303|PubMed:29253195};\nDE            EC=5.6.2.1 {ECO:0000269|PubMed:22722926, ECO:0000269|PubMed:29253195};\nDE   AltName: Full=DNA topoisomerase III {ECO:0000303|PubMed:29253195};\nGN   Name=topA {ECO:0000303|PubMed:22722926, ECO:0000312|EMBL:AAK41190.1};\nGN   OrderedLocusNames=SSO0907 {ECO:0000312|EMBL:AAK41190.1};\nOS   Saccharolobus solfataricus (strain ATCC 35092 / DSM 1617 / JCM 11322 / P2)\nOS   (Sulfolobus solfataricus).\nOC   Archaea; Thermoproteota; Thermoprotei; Sulfolobales; Sulfolobaceae;\nOC   Saccharolobus.\nOX   NCBI_TaxID=273057;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:45.340278+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "77a05af9d1305445b3e0d4b67305724443fad1a6fc01422e81a6d8f5dc26d379",
  "url": "https://rest.uniprot.org/unisave/Q97ZJ8?format=txt&versions=132"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q97ZJ8?format=txt&versions=132)

```json
{
  "entry_version": 132,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, SUBUNIT, INTERACTION WITH LHR, AND\nRP   DNA-BINDING.\nRX   PubMed=22722926; DOI=10.1074/jbc.m112.366377;\nRA   Valenti A., De Felice M., Perugino G., Bizard A., Nadal M., Rossi M.,\nRA   Ciaramella M.;\nRT   \"Synergic and opposing activities of thermophilic RecQ-like helicase and\nRT   topoisomerase 3 proteins in Holliday junction processing and replication\nRT   fork stabilization.\";\nRL   J. Biol. Chem. 287:30282-30295(2012).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:45.340278+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 30-39",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "77a05af9d1305445b3e0d4b67305724443fad1a6fc01422e81a6d8f5dc26d379",
  "url": "https://rest.uniprot.org/unisave/Q97ZJ8?format=txt&versions=132"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q97ZJ8?format=txt&versions=132)

```json
{
  "entry_version": 132,
  "evidence_id": "H3",
  "excerpt": "RN   [3]\nRP   FUNCTION, CATALYTIC ACTIVITY, COFACTOR, ACTIVITY REGULATION, AND\nRP   BIOPHYSICOCHEMICAL PROPERTIES.\nRX   PubMed=29253195; DOI=10.1093/nar/gkx1247;\nRA   Bizard A.H., Yang X., Debat H., Fogg J.M., Zechiedrich L., Strick T.R.,\nRA   Garnier F., Nadal M.;\nRT   \"TopA, the Sulfolobus solfataricus topoisomerase III, is a decatenase.\";\nRL   Nucleic Acids Res. 46:861-872(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:45.340278+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 40-47",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "77a05af9d1305445b3e0d4b67305724443fad1a6fc01422e81a6d8f5dc26d379",
  "url": "https://rest.uniprot.org/unisave/Q97ZJ8?format=txt&versions=132"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q97ZJ8?format=txt&versions=132)

```json
{
  "entry_version": 132,
  "evidence_id": "H4",
  "excerpt": "FT   ACT_SITE        318\nFT                   /note=\"O-(5'-phospho-DNA)-tyrosine intermediate\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01383\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:45.340278+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 160-162",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "77a05af9d1305445b3e0d4b67305724443fad1a6fc01422e81a6d8f5dc26d379",
  "url": "https://rest.uniprot.org/unisave/Q97ZJ8?format=txt&versions=132"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q97ZJ8?format=txt&versions=132)

```json
{
  "entry_version": 132,
  "evidence_id": "H5",
  "excerpt": "FT   BINDING         602\nFT                   /ligand=\"Zn(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29105\"\nFT                   /evidence=\"ECO:0007744|PDB:6K8N, ECO:0007744|PDB:6K8O\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:45.340278+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 163-166",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "77a05af9d1305445b3e0d4b67305724443fad1a6fc01422e81a6d8f5dc26d379",
  "url": "https://rest.uniprot.org/unisave/Q97ZJ8?format=txt&versions=132"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q97ZJ8?format=txt&versions=132)

```json
{
  "entry_version": 132,
  "evidence_id": "H6",
  "excerpt": "FT   BINDING         605\nFT                   /ligand=\"Zn(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29105\"\nFT                   /evidence=\"ECO:0007744|PDB:6K8N, ECO:0007744|PDB:6K8O\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:45.340278+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 167-170",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "77a05af9d1305445b3e0d4b67305724443fad1a6fc01422e81a6d8f5dc26d379",
  "url": "https://rest.uniprot.org/unisave/Q97ZJ8?format=txt&versions=132"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q97ZJ8?format=txt&versions=132)

```json
{
  "entry_version": 132,
  "evidence_id": "H7",
  "excerpt": "FT   BINDING         615\nFT                   /ligand=\"Zn(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29105\"\nFT                   /evidence=\"ECO:0007744|PDB:6K8N, ECO:0007744|PDB:6K8O\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:45.340278+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 171-174",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "77a05af9d1305445b3e0d4b67305724443fad1a6fc01422e81a6d8f5dc26d379",
  "url": "https://rest.uniprot.org/unisave/Q97ZJ8?format=txt&versions=132"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q97ZJ8?format=txt&versions=132)

```json
{
  "entry_version": 132,
  "evidence_id": "H8",
  "excerpt": "FT   BINDING         618\nFT                   /ligand=\"Zn(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29105\"\nFT                   /evidence=\"ECO:0007744|PDB:6K8N, ECO:0007744|PDB:6K8O\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:45.340278+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 175-178",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "77a05af9d1305445b3e0d4b67305724443fad1a6fc01422e81a6d8f5dc26d379",
  "url": "https://rest.uniprot.org/unisave/Q97ZJ8?format=txt&versions=132"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 133. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
