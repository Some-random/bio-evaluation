# transmembrane_0006

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0006.txt)

**Task:** `transmembrane`  
**Expected answer:** **A** — 3..23

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSWPLIGAYALLAFVAIIALNVTYQFLFRLLNKTRPPLVFHWIPFIGSTIHYGMDPYGFFFSCREKYGDIFTFILLGRPTTVYLGTQGNEFILNGKLKDVNAEEVYSPLTTPVFGSDVVYDCPNSKLIEQKKFIKFGLSQTALEAHVPLIEKEVEDYLAMSPNFHGTSGEVDITAAMAEITIFTAGSALQGEEVRSKLTTEFAVLYHDLDKGFTPINFMLPWAPLPHNKKRDAAHARMRAIYIDIINKRRNAGDNVPEKLDMIGNLMQCTYKNGQPLPDKEIAHIMITLLMAGQHSSSSISSWIMLRLASQPAVVEELYQEQLANLERTGPNNSLAPLQYKDFDNLPLHQNVIRETLRLNSSIHSLMRKVKNPLPVPGTPYVIPTSHVLLSAPGVTALSDEYFPNAMAWDPHRWETQAPKENDKDDIVDYGYGAISKGTSSPYLPFGAGRHRCIGEKFAYLNLAVIVATMVRHLRFSNLDGQTGVPATDYSSLFSGPMKPARIRWERRAAKSG

[Multiple Choices]
A. 3..23
B. 3..23; 455..479
C. 278..286; 308..323
D. 4..20
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

> The sequence-matched UniProt annotation gives a helical transmembrane region at 3..23. This is computationally supported (ECO:0000255), not evidence of an experimental measurement; the historical record also contains the same annotation.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminus contains a continuous, strongly hydrophobic stretch extending roughly from residues 3 to 23, characteristic of a membrane-spanning alpha helix. That transferable sequence pattern distinguishes A from the nonhydrophobic internal intervals in C and the alternative interval in B. D overlaps the hydrophobic core but is a shorter truncation of the likely complete helix.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and choices provide a credible basis to identify the N-terminal membrane anchor without knowing this protein's database annotation. The exact annotated boundaries are not derivable with certainty from sequence alone, but the full hydrophobic stretch favors A over the shorter D interval.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> D covers a hydrophobic subsection of the same stretch, but it is shorter than the typical complete membrane-spanning helix; A better captures the full predicted interval.


### Important caveats

- The supporting database feature is computational rather than experimentally established.
- A sequence-based inference supports the likely helix and approximate boundaries, not uniquely exact residue-level boundaries.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminus contains a continuous, strongly hydrophobic stretch extending roughly from residues 3 to 23, characteristic of a membrane-spanning alpha helix. That transferable sequence pattern distinguishes A from the nonhydrophobic internal intervals in C and the alternative interval in B. D overlaps the hydrophobic core but is a shorter truncation of the likely complete helix.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and choices provide a credible basis to identify the N-terminal membrane anchor without knowing this protein's database annotation. The exact annotated boundaries are not derivable with certainty from sequence alone, but the full hydrophobic stretch favors A over the shorter D interval."
  },
  "case_id": "transmembrane_0006",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation gives a helical transmembrane region at 3..23. This is computationally supported (ECO:0000255), not evidence of an experimental measurement; the historical record also contains the same annotation."
  },
  "important_caveats": [
    "The supporting database feature is computational rather than experimentally established.",
    "A sequence-based inference supports the likely helix and approximate boundaries, not uniquely exact residue-level boundaries."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D covers a hydrophobic subsection of the same stretch, but it is shorter than the typical complete membrane-spanning helix; A better captures the full predicted interval."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0006",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation gives a helical transmembrane region at 3..23. This is computationally supported (ECO:0000255), not evidence of an experimental measurement; the historical record also contains the same annotation.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminus contains a continuous, strongly hydrophobic stretch extending roughly from residues 3 to 23, characteristic of a membrane-spanning alpha helix. That transferable sequence pattern distinguishes A from the nonhydrophobic internal intervals in C and the alternative interval in B. D overlaps the hydrophobic core but is a shorter truncation of the likely complete helix.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and choices provide a credible basis to identify the N-terminal membrane anchor without knowing this protein's database annotation. The exact annotated boundaries are not derivable with certainty from sequence alone, but the full hydrophobic stretch favors A over the shorter D interval."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D covers a hydrophobic subsection of the same stretch, but it is shorter than the typical complete membrane-spanning helix; A better captures the full predicted interval."
  },
  "important_caveats": [
    "The supporting database feature is computational rather than experimentally established.",
    "A sequence-based inference supports the likely helix and approximate boundaries, not uniquely exact residue-level boundaries."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (evidence C5, H3) records a single Transmembrane region at positions 3..23, described as Helical, with evidence code ECO:0000255 (inferred by similarity/computational). The sequence at positions 3-23 (WPLIGAYALLAFVAIIALNV) is 21 residues of overwhelmingly hydrophobic character (W, L, I, A, F, V, I, A, L, V with only one polar N), consistent with a TM helix. This is a N-terminal membrane anchor typical of microsomal cytochrome P450 enzymes. The annotation is computational rather than experimentally determined, but it is the recorded fact and is consistent with sequence properties.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model can apply several transferable criteria: (1) TM helix length criterion: spanning the ~30 Å hydrophobic core of a lipid bilayer requires ~18-25 residues. Option A (3..23) = 21 residues fits perfectly; Option D (4..20) = 17 residues falls below the typical minimum; Option C includes a 9-residue segment (278..286) that is far too short. (2) CYP450 family knowledge: the conserved heme-binding motif 'AGRHRCIGE' (with the Cys coordinating the heme iron) is present around positions 455-465. A model familiar with CYP450 structure knows this region is a soluble catalytic domain, not a membrane-spanning helix, eliminating Option B's second TM claim. (3) Microsomal CYP450s are anchored by a single N-terminal TM helix (~20 residues), matching Option A. (4) The N-terminal segment 3-23 is highly hydrophobic (WPLIGAYALLAFVAIIALNV), while the 455-479 segment in B contains charged residues (E, K, R, R) incompatible with a TM helix.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The distinction among options relies on general TM helix length rules (18-25 residues), hydrophobicity assessment of the sequence, and CYP450 family structural knowledge (single N-terminal anchor, heme-binding motif location). These are all transferable biological principles learned from other proteins and membrane biophysics. The 17 vs 21 residue difference between A and D is meaningful under the standard length criterion. The heme-binding motif in B is recognizable by sequence pattern. The 9-residue segment in C is clearly insufficient.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While A and D overlap in the same hydrophobic N-terminal region, the length criterion (17 vs 21 residues relative to the 18-25 minimum for TM helices) provides a clear distinction favoring A. Option B is eliminated by the presence of charged residues and the heme-binding motif in the second claimed TM region. Option C is eliminated by the 9-residue segment being far too short.


### Important caveats

- The UniProt annotation uses evidence code ECO:0000255 (inferred by similarity), meaning the TM assignment is computational/predicted rather than experimentally verified.
- The distinction between A (3..23, 21 residues) and D (4..20, 17 residues) relies on the conventional 18-25 residue TM helix length criterion; 17 is below but not impossibly far from this range, though 21 is clearly within it.
- The reviewer-only evidence confirms the sequence matches the UniProt entry (SHA-256 match), but the identity/accession was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can apply several transferable criteria: (1) TM helix length criterion: spanning the ~30 Å hydrophobic core of a lipid bilayer requires ~18-25 residues. Option A (3..23) = 21 residues fits perfectly; Option D (4..20) = 17 residues falls below the typical minimum; Option C includes a 9-residue segment (278..286) that is far too short. (2) CYP450 family knowledge: the conserved heme-binding motif 'AGRHRCIGE' (with the Cys coordinating the heme iron) is present around positions 455-465. A model familiar with CYP450 structure knows this region is a soluble catalytic domain, not a membrane-spanning helix, eliminating Option B's second TM claim. (3) Microsomal CYP450s are anchored by a single N-terminal TM helix (~20 residues), matching Option A. (4) The N-terminal segment 3-23 is highly hydrophobic (WPLIGAYALLAFVAIIALNV), while the 455-479 segment in B contains charged residues (E, K, R, R) incompatible with a TM helix.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The distinction among options relies on general TM helix length rules (18-25 residues), hydrophobicity assessment of the sequence, and CYP450 family structural knowledge (single N-terminal anchor, heme-binding motif location). These are all transferable biological principles learned from other proteins and membrane biophysics. The 17 vs 21 residue difference between A and D is meaningful under the standard length criterion. The heme-binding motif in B is recognizable by sequence pattern. The 9-residue segment in C is clearly insufficient."
  },
  "case_id": "transmembrane_0006",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C5, H3) records a single Transmembrane region at positions 3..23, described as Helical, with evidence code ECO:0000255 (inferred by similarity/computational). The sequence at positions 3-23 (WPLIGAYALLAFVAIIALNV) is 21 residues of overwhelmingly hydrophobic character (W, L, I, A, F, V, I, A, L, V with only one polar N), consistent with a TM helix. This is a N-terminal membrane anchor typical of microsomal cytochrome P450 enzymes. The annotation is computational rather than experimentally determined, but it is the recorded fact and is consistent with sequence properties."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (inferred by similarity), meaning the TM assignment is computational/predicted rather than experimentally verified.",
    "The distinction between A (3..23, 21 residues) and D (4..20, 17 residues) relies on the conventional 18-25 residue TM helix length criterion; 17 is below but not impossibly far from this range, though 21 is clearly within it.",
    "The reviewer-only evidence confirms the sequence matches the UniProt entry (SHA-256 match), but the identity/accession was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While A and D overlap in the same hydrophobic N-terminal region, the length criterion (17 vs 21 residues relative to the 18-25 minimum for TM helices) provides a clear distinction favoring A. Option B is eliminated by the presence of charged residues and the heme-binding motif in the second claimed TM region. Option C is eliminated by the 9-residue segment being far too short."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0006",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C5, H3) records a single Transmembrane region at positions 3..23, described as Helical, with evidence code ECO:0000255 (inferred by similarity/computational). The sequence at positions 3-23 (WPLIGAYALLAFVAIIALNV) is 21 residues of overwhelmingly hydrophobic character (W, L, I, A, F, V, I, A, L, V with only one polar N), consistent with a TM helix. This is a N-terminal membrane anchor typical of microsomal cytochrome P450 enzymes. The annotation is computational rather than experimentally determined, but it is the recorded fact and is consistent with sequence properties.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model can apply several transferable criteria: (1) TM helix length criterion: spanning the ~30 Å hydrophobic core of a lipid bilayer requires ~18-25 residues. Option A (3..23) = 21 residues fits perfectly; Option D (4..20) = 17 residues falls below the typical minimum; Option C includes a 9-residue segment (278..286) that is far too short. (2) CYP450 family knowledge: the conserved heme-binding motif 'AGRHRCIGE' (with the Cys coordinating the heme iron) is present around positions 455-465. A model familiar with CYP450 structure knows this region is a soluble catalytic domain, not a membrane-spanning helix, eliminating Option B's second TM claim. (3) Microsomal CYP450s are anchored by a single N-terminal TM helix (~20 residues), matching Option A. (4) The N-terminal segment 3-23 is highly hydrophobic (WPLIGAYALLAFVAIIALNV), while the 455-479 segment in B contains charged residues (E, K, R, R) incompatible with a TM helix.",
    "missing_item_specific_fact": "",
    "reason": "The distinction among options relies on general TM helix length rules (18-25 residues), hydrophobicity assessment of the sequence, and CYP450 family structural knowledge (single N-terminal anchor, heme-binding motif location). These are all transferable biological principles learned from other proteins and membrane biophysics. The 17 vs 21 residue difference between A and D is meaningful under the standard length criterion. The heme-binding motif in B is recognizable by sequence pattern. The 9-residue segment in C is clearly insufficient."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While A and D overlap in the same hydrophobic N-terminal region, the length criterion (17 vs 21 residues relative to the 18-25 minimum for TM helices) provides a clear distinction favoring A. Option B is eliminated by the presence of charged residues and the heme-binding motif in the second claimed TM region. Option C is eliminated by the 9-residue segment being far too short."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (inferred by similarity), meaning the TM assignment is computational/predicted rather than experimentally verified.",
    "The distinction between A (3..23, 21 residues) and D (4..20, 17 residues) relies on the conventional 18-25 residue TM helix length criterion; 17 is below but not impossibly far from this range, though 21 is clearly within it.",
    "The reviewer-only evidence confirms the sequence matches the UniProt entry (SHA-256 match), but the identity/accession was not available to the evaluated model."
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
  "benchmark_sequence_length": 513,
  "benchmark_sequence_sha256": "19c16af699d50913a7bf4f55defbf96b0893917eaeb57b66b0dc53dd081e1b3c",
  "current_entry_audit": {
    "entryVersion": 40,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2015-11-11",
    "sequenceVersion": 1
  },
  "current_record_sha256": "d02dbb89f818b7eb87df130d530379b150615f58a7786d959f158367f6e7dbef",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 513,
  "current_source_sequence_sha256": "19c16af699d50913a7bf4f55defbf96b0893917eaeb57b66b0dc53dd081e1b3c",
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
  "requested_accession": "A0A0L1JEW4",
  "selected_historical_entry_version": 38,
  "selected_historical_record_sha256": "6c3d64c65d2f83b7569168450886015fb66b6ae6595088f32ba80d12e66f79e5",
  "selected_historical_source_sequence_length": 513,
  "selected_historical_source_sequence_sha256": "19c16af699d50913a7bf4f55defbf96b0893917eaeb57b66b0dc53dd081e1b3c",
  "selected_historical_version": {
    "accession": "A0A0L1JEW4",
    "database": "Swiss-Prot",
    "entryVersion": 38,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "RSTN2_ASPN3",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A0L1JEW4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:12.364317+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d02dbb89f818b7eb87df130d530379b150615f58a7786d959f158367f6e7dbef",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":40,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2015-11-11\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:12.364317+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d02dbb89f818b7eb87df130d530379b150615f58a7786d959f158367f6e7dbef",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Aspergillus\",\"Circumdati\"],\"scientificName\":\"Aspergillus nomiae NRRL (strain ATCC 15546 / NRRL 13137 / CBS 260.88 / M93)\",\"taxonId\":1509407}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:12.364317+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d02dbb89f818b7eb87df130d530379b150615f58a7786d959f158367f6e7dbef",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33857369\",\"source\":\"PubMed\"}],\"value\":\"Cytochrome P450 monooxygenase rstn2\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33857369\",\"source\":\"PubMed\"}],\"value\":\"Ergosterol biosynthesis protein rstn2\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33857369\",\"source\":\"PubMed\"}],\"value\":\"Restricticin biosynthesis cluster protein 2\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33857369\",\"source\":\"PubMed\"}],\"value\":\"1.14.14.154\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33857369\",\"source\":\"PubMed\"}],\"value\":\"Sterol 14-alpha demethylase rstn2\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:12.364317+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d02dbb89f818b7eb87df130d530379b150615f58a7786d959f158367f6e7dbef",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":23},\"start\":{\"modifier\":\"EXACT\",\"value\":3}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:24:12.364317+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d02dbb89f818b7eb87df130d530379b150615f58a7786d959f158367f6e7dbef",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Liu N.\",\"Abramyan E.D.\",\"Cheng W.\",\"Perlatti B.\",\"Harvey C.J.B.\",\"Bills G.F.\",\"Tang Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33857369\"},{\"database\":\"DOI\",\"id\":\"10.1021/jacs.1c01516\"}],\"citationType\":\"journal article\",\"firstPage\":\"6043\",\"id\":\"33857369\",\"journal\":\"J. Am. Chem. Soc.\",\"lastPage\":\"6047\",\"publicationDate\":\"2021\",\"title\":\"Targeted genome mining reveals the biosynthetic gene clusters of natural product CYP51 inhibitors.\",\"volume\":\"143\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:24:12.364317+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d02dbb89f818b7eb87df130d530379b150615f58a7786d959f158367f6e7dbef",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0L1JEW4?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H1",
  "excerpt": "ID   RSTN2_ASPN3             Reviewed;         513 AA.\nAC   A0A0L1JEW4;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   11-NOV-2015, sequence version 1.\nDT   28-JAN-2026, entry version 38.\nDE   RecName: Full=Sterol 14-alpha demethylase rstn2 {ECO:0000303|PubMed:33857369};\nDE            EC=1.14.14.154 {ECO:0000269|PubMed:33857369};\nDE   AltName: Full=Cytochrome P450 monooxygenase rstn2 {ECO:0000303|PubMed:33857369};\nDE   AltName: Full=Ergosterol biosynthesis protein rstn2 {ECO:0000303|PubMed:33857369};\nDE   AltName: Full=Restricticin biosynthesis cluster protein 2 {ECO:0000303|PubMed:33857369};\nGN   Name=rstn2 {ECO:0000303|PubMed:33857369}; ORFNames=ANOM_001443;\nOS   Aspergillus nomiae NRRL (strain ATCC 15546 / NRRL 13137 / CBS 260.88 /\nOS   M93).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;\nOC   Aspergillus subgen. Circumdati.\nOX   NCBI_TaxID=1509407;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:14.653166+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6c3d64c65d2f83b7569168450886015fb66b6ae6595088f32ba80d12e66f79e5",
  "url": "https://rest.uniprot.org/unisave/A0A0L1JEW4?format=txt&versions=38"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0L1JEW4?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND PATHWAY.\nRX   PubMed=33857369; DOI=10.1021/jacs.1c01516;\nRA   Liu N., Abramyan E.D., Cheng W., Perlatti B., Harvey C.J.B., Bills G.F.,\nRA   Tang Y.;\nRT   \"Targeted genome mining reveals the biosynthetic gene clusters of natural\nRT   product CYP51 inhibitors.\";\nRL   J. Am. Chem. Soc. 143:6043-6047(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:14.653166+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 26-33",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6c3d64c65d2f83b7569168450886015fb66b6ae6595088f32ba80d12e66f79e5",
  "url": "https://rest.uniprot.org/unisave/A0A0L1JEW4?format=txt&versions=38"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0L1JEW4?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H3",
  "excerpt": "FT   TRANSMEM        3..23\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:14.653166+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 212-214",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6c3d64c65d2f83b7569168450886015fb66b6ae6595088f32ba80d12e66f79e5",
  "url": "https://rest.uniprot.org/unisave/A0A0L1JEW4?format=txt&versions=38"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 6. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
