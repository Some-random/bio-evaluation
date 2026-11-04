# transmembrane_0099

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0099.txt)

**Task:** `transmembrane`  
**Expected answer:** **D** — 483..503

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKAFSVTCLGFAVFSSSICVNINILQQIGYIKQQVRQLSYYSQSSSSYIVVKLLPNIQPTDNSCEFKSVTQYNKTLSNLLLPIAENINNIASPSPGSRRHKRFAGIAIGIAALGVATAAQVTAAVSLVQAQTNARAIAAMKNSIQATNRAIFEVKEGTQQLAIAVQAIQDHINTIMNTQLNNMTCQILDNQLATFLGLYLTELTTVFQPQLINPALSPISIQALRSLLGSMTPAVVQATLSTSISAAEILSAGLMEGQIVSVLLDEMQMIVKVNIPTIVTQSNALVIDFYSISSFINNQESIIQLPDRILEIGNEQWSYPAKNCKLTRHHIFCQYNEAERLSLESKLCLAGNISACVFSPIAGSYMRRFVALDGTIVANCRSLTCLCKSPSYPIYQPDHHAVTTIDLTACQTLSLDGLDFSIVSLSNITYAENLTISLSQTINTQPIDISTELSKVNASLQNAVKYIKESNHQLLSVSVNSKIGAIIVTALVLSILSIIISLLFCCWAYIATKEIRRINFKTNHINTISSSVDDLIRY

[Multiple Choices]
A. 278..286; 308..323
B. 483..507
C. 483..503; 567..591
D. 483..503
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

> The sequence-matched historical UniProt entry annotates residues 483–503 as a helical transmembrane region, supporting the key. The annotation is computationally evidenced (ECO:0000255), so this supports the answer as a database annotation, not as independently established experimental evidence.

Citations as saved: [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a conspicuous hydrophobic stretch near its C terminus, followed by a more polar/charged tail, a transferable pattern for a membrane anchor in a membrane glycoprotein. Its roughly membrane-length hydrophobic core favors D over the internal region in A; C also proposes positions beyond the 538-residue sequence. B overlaps the same anchor but extends farther into its flanking region.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence itself provides a credible basis for identifying the C-terminal membrane-spanning segment and favoring its hydrophobic core. Exact boundaries are less certain from sequence alone, but the main distinction does not require knowing this protein’s recorded annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> B and D share the same start and encompass the same strongly hydrophobic core; B extends the endpoint by four residues. Because membrane boundaries can be fuzzy and flanking hydrophobic or aromatic residues may lie at the membrane interface, sequence evidence alone does not make that endpoint distinction absolute. D remains the better match to the annotated core.


### Important caveats

- The historical annotation matches the supplied sequence, but its evidence code indicates computational annotation rather than experimental proof.
- The source evidence is reviewer-only and was not part of the original input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a conspicuous hydrophobic stretch near its C terminus, followed by a more polar/charged tail, a transferable pattern for a membrane anchor in a membrane glycoprotein. Its roughly membrane-length hydrophobic core favors D over the internal region in A; C also proposes positions beyond the 538-residue sequence. B overlaps the same anchor but extends farther into its flanking region.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence itself provides a credible basis for identifying the C-terminal membrane-spanning segment and favoring its hydrophobic core. Exact boundaries are less certain from sequence alone, but the main distinction does not require knowing this protein’s recorded annotation."
  },
  "case_id": "transmembrane_0099",
  "expected_answer_check": {
    "evidence_ids": [
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt entry annotates residues 483–503 as a helical transmembrane region, supporting the key. The annotation is computationally evidenced (ECO:0000255), so this supports the answer as a database annotation, not as independently established experimental evidence."
  },
  "important_caveats": [
    "The historical annotation matches the supplied sequence, but its evidence code indicates computational annotation rather than experimental proof.",
    "The source evidence is reviewer-only and was not part of the original input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "B and D share the same start and encompass the same strongly hydrophobic core; B extends the endpoint by four residues. Because membrane boundaries can be fuzzy and flanking hydrophobic or aromatic residues may lie at the membrane interface, sequence evidence alone does not make that endpoint distinction absolute. D remains the better match to the annotated core."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0099",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt entry annotates residues 483–503 as a helical transmembrane region, supporting the key. The annotation is computationally evidenced (ECO:0000255), so this supports the answer as a database annotation, not as independently established experimental evidence.",
    "evidence_ids": ["H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a conspicuous hydrophobic stretch near its C terminus, followed by a more polar/charged tail, a transferable pattern for a membrane anchor in a membrane glycoprotein. Its roughly membrane-length hydrophobic core favors D over the internal region in A; C also proposes positions beyond the 538-residue sequence. B overlaps the same anchor but extends farther into its flanking region.",
    "missing_item_specific_fact": "",
    "reason": "The sequence itself provides a credible basis for identifying the C-terminal membrane-spanning segment and favoring its hydrophobic core. Exact boundaries are less certain from sequence alone, but the main distinction does not require knowing this protein’s recorded annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "B and D share the same start and encompass the same strongly hydrophobic core; B extends the endpoint by four residues. Because membrane boundaries can be fuzzy and flanking hydrophobic or aromatic residues may lie at the membrane interface, sequence evidence alone does not make that endpoint distinction absolute. D remains the better match to the annotated core."
  },
  "important_caveats": [
    "The historical annotation matches the supplied sequence, but its evidence code indicates computational annotation rather than experimental proof.",
    "The source evidence is reviewer-only and was not part of the original input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (evidence code ECO:0000255, similarity-based) explicitly annotates a single transmembrane helix at 483..503, with the extracellular domain ending at 482 and the cytoplasmic domain beginning at 504. The sequence at 483-503 (IGAIIVTALVLSILSIIISLL) is a hydrophobic alpha-helical stretch consistent with a single-pass TM anchor. This matches choice D exactly.

Citations as saved: [C6](#evidence-c6), [H3](#evidence-h3), [C5](#evidence-c5), [H2](#evidence-h2), [C7](#evidence-c7), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Multiple transferable inferences distinguish D from the alternatives: (1) Option C references positions 567-591 in a 538-residue protein, immediately eliminating it. (2) Option A (278-286; 308-323) contains charged/polar residues (K, N, P, Q, D, R, E, G, N, Q) incompatible with a TM helix's hydrophobic core. (3) The sequence at 483-503 is a classic ~21-residue aliphatic hydrophobic stretch (I,G,A,I,I,V,T,A,L,V,L,S,I,L,S,I,I,I,S,L,L), the hallmark of a single-pass TM anchor. (4) Distinguishing D (483-503) from B (483-507): the additional residues at 504-507 (F,C,C,W) are aromatic residues characteristic of the membrane-water interface 'aromatic belt' that marks the TM/cytoplasmic boundary, not the hydrophobic core. This is a well-established principle in membrane protein biology (Trp/Tyr anchoring at lipid-water interfaces). (5) The protein architecture—a large extracellular domain (~480 residues) followed by a single C-terminal TM helix and a short cytoplasmic tail (~35 residues)—matches the known topology of paramyxovirus class I fusion glycoproteins (NDV F, measles F, RSV F homologs), all of which have a single TM anchor near the C-terminus. The annotation evidence code ECO:0000255 confirms this topology was transferred from related paramyxovirus F proteins.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can eliminate C by sequence length, eliminate A by hydrophobicity analysis, and distinguish D from B using the aromatic-belt boundary principle and the well-known single-TM topology of paramyxovirus fusion glycoproteins learned from homologs like NDV F and measles F. The hydrophobic core clearly ends at position 503, with aromatic residues at 504-507 serving as interface markers.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option C is invalid (exceeds protein length). Option A lacks hydrophobic character. Option B extends the TM by 4 aromatic residues that are more consistent with the interface/boundary rather than the hydrophobic core. Option D matches the canonical hydrophobic stretch and the known paramyxovirus F topology. While B vs D is the closest call, the aromatic-belt principle and family-level topology knowledge favor D.


### Important caveats

- The UniProt annotation uses evidence code ECO:0000255 (similarity-based transfer), meaning the TM boundaries were inferred from related proteins rather than determined experimentally for this exact sequence.
- The distinction between D (483-503) and B (483-507) is the most subtle aspect; some TM predictors might include the aromatic residues as part of the TM helix. However, the aliphatic-only core convention and the paramyxovirus F family topology favor the shorter definition.
- The protein identity (Mumps virus F glycoprotein) was not provided to the model; recognition relies on sequence features and family-level pattern matching.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Multiple transferable inferences distinguish D from the alternatives: (1) Option C references positions 567-591 in a 538-residue protein, immediately eliminating it. (2) Option A (278-286; 308-323) contains charged/polar residues (K, N, P, Q, D, R, E, G, N, Q) incompatible with a TM helix's hydrophobic core. (3) The sequence at 483-503 is a classic ~21-residue aliphatic hydrophobic stretch (I,G,A,I,I,V,T,A,L,V,L,S,I,L,S,I,I,I,S,L,L), the hallmark of a single-pass TM anchor. (4) Distinguishing D (483-503) from B (483-507): the additional residues at 504-507 (F,C,C,W) are aromatic residues characteristic of the membrane-water interface 'aromatic belt' that marks the TM/cytoplasmic boundary, not the hydrophobic core. This is a well-established principle in membrane protein biology (Trp/Tyr anchoring at lipid-water interfaces). (5) The protein architecture—a large extracellular domain (~480 residues) followed by a single C-terminal TM helix and a short cytoplasmic tail (~35 residues)—matches the known topology of paramyxovirus class I fusion glycoproteins (NDV F, measles F, RSV F homologs), all of which have a single TM anchor near the C-terminus. The annotation evidence code ECO:0000255 confirms this topology was transferred from related paramyxovirus F proteins.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate C by sequence length, eliminate A by hydrophobicity analysis, and distinguish D from B using the aromatic-belt boundary principle and the well-known single-TM topology of paramyxovirus fusion glycoproteins learned from homologs like NDV F and measles F. The hydrophobic core clearly ends at position 503, with aromatic residues at 504-507 serving as interface markers."
  },
  "case_id": "transmembrane_0099",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "H3",
      "C5",
      "H2",
      "C7",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence code ECO:0000255, similarity-based) explicitly annotates a single transmembrane helix at 483..503, with the extracellular domain ending at 482 and the cytoplasmic domain beginning at 504. The sequence at 483-503 (IGAIIVTALVLSILSIIISLL) is a hydrophobic alpha-helical stretch consistent with a single-pass TM anchor. This matches choice D exactly."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (similarity-based transfer), meaning the TM boundaries were inferred from related proteins rather than determined experimentally for this exact sequence.",
    "The distinction between D (483-503) and B (483-507) is the most subtle aspect; some TM predictors might include the aromatic residues as part of the TM helix. However, the aliphatic-only core convention and the paramyxovirus F family topology favor the shorter definition.",
    "The protein identity (Mumps virus F glycoprotein) was not provided to the model; recognition relies on sequence features and family-level pattern matching."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C is invalid (exceeds protein length). Option A lacks hydrophobic character. Option B extends the TM by 4 aromatic residues that are more consistent with the interface/boundary rather than the hydrophobic core. Option D matches the canonical hydrophobic stretch and the known paramyxovirus F topology. While B vs D is the closest call, the aromatic-belt principle and family-level topology knowledge favor D."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0099",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence code ECO:0000255, similarity-based) explicitly annotates a single transmembrane helix at 483..503, with the extracellular domain ending at 482 and the cytoplasmic domain beginning at 504. The sequence at 483-503 (IGAIIVTALVLSILSIIISLL) is a hydrophobic alpha-helical stretch consistent with a single-pass TM anchor. This matches choice D exactly.",
    "evidence_ids": ["C6", "H3", "C5", "H2", "C7", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Multiple transferable inferences distinguish D from the alternatives: (1) Option C references positions 567-591 in a 538-residue protein, immediately eliminating it. (2) Option A (278-286; 308-323) contains charged/polar residues (K, N, P, Q, D, R, E, G, N, Q) incompatible with a TM helix's hydrophobic core. (3) The sequence at 483-503 is a classic ~21-residue aliphatic hydrophobic stretch (I,G,A,I,I,V,T,A,L,V,L,S,I,L,S,I,I,I,S,L,L), the hallmark of a single-pass TM anchor. (4) Distinguishing D (483-503) from B (483-507): the additional residues at 504-507 (F,C,C,W) are aromatic residues characteristic of the membrane-water interface 'aromatic belt' that marks the TM/cytoplasmic boundary, not the hydrophobic core. This is a well-established principle in membrane protein biology (Trp/Tyr anchoring at lipid-water interfaces). (5) The protein architecture—a large extracellular domain (~480 residues) followed by a single C-terminal TM helix and a short cytoplasmic tail (~35 residues)—matches the known topology of paramyxovirus class I fusion glycoproteins (NDV F, measles F, RSV F homologs), all of which have a single TM anchor near the C-terminus. The annotation evidence code ECO:0000255 confirms this topology was transferred from related paramyxovirus F proteins.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate C by sequence length, eliminate A by hydrophobicity analysis, and distinguish D from B using the aromatic-belt boundary principle and the well-known single-TM topology of paramyxovirus fusion glycoproteins learned from homologs like NDV F and measles F. The hydrophobic core clearly ends at position 503, with aromatic residues at 504-507 serving as interface markers."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C is invalid (exceeds protein length). Option A lacks hydrophobic character. Option B extends the TM by 4 aromatic residues that are more consistent with the interface/boundary rather than the hydrophobic core. Option D matches the canonical hydrophobic stretch and the known paramyxovirus F topology. While B vs D is the closest call, the aromatic-belt principle and family-level topology knowledge favor D."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (similarity-based transfer), meaning the TM boundaries were inferred from related proteins rather than determined experimentally for this exact sequence.",
    "The distinction between D (483-503) and B (483-507) is the most subtle aspect; some TM predictors might include the aromatic residues as part of the TM helix. However, the aliphatic-only core convention and the paramyxovirus F family topology favor the shorter definition.",
    "The protein identity (Mumps virus F glycoprotein) was not provided to the model; recognition relies on sequence features and family-level pattern matching."
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
  "benchmark_sequence_length": 538,
  "benchmark_sequence_sha256": "ca344ce86c8ca532870fd703c59b36aa651563981a4288efac2646db70979fec",
  "current_entry_audit": {
    "entryVersion": 81,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2004-12-21",
    "sequenceVersion": 1
  },
  "current_record_sha256": "72eeca0dc4f0e1b54320c79e260ae9238e7fcefb733b978db81bae5e0d233fa9",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 538,
  "current_source_sequence_sha256": "ca344ce86c8ca532870fd703c59b36aa651563981a4288efac2646db70979fec",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 80,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q5SC53",
  "selected_historical_entry_version": 80,
  "selected_historical_record_sha256": "afb9ab9d6093f040c16474e49b884836fed8582e6d2cecfa0264668dfd09db66",
  "selected_historical_source_sequence_length": 538,
  "selected_historical_source_sequence_sha256": "ca344ce86c8ca532870fd703c59b36aa651563981a4288efac2646db70979fec",
  "selected_historical_version": {
    "accession": "Q5SC53",
    "database": "Swiss-Prot",
    "entryVersion": 80,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "FUS_MUMPZ",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC53.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q5SC53\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:22.414761+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "72eeca0dc4f0e1b54320c79e260ae9238e7fcefb733b978db81bae5e0d233fa9",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC53.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC53.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":81,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2004-12-21\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:22.414761+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "72eeca0dc4f0e1b54320c79e260ae9238e7fcefb733b978db81bae5e0d233fa9",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC53.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC53.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"MuV\",\"lineage\":[\"Viruses\",\"Riboviria\",\"Orthornavirae\",\"Negarnaviricota\",\"Haploviricotina\",\"Monjiviricetes\",\"Mononegavirales\",\"Paramyxoviridae\",\"Rubulavirinae\",\"Orthorubulavirus\",\"Orthorubulavirus parotitidis\",\"Mumps orthorubulavirus\"],\"scientificName\":\"Mumps virus genotype N (strain L-Zagreb vaccine)\",\"taxonId\":301186}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:22.414761+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "72eeca0dc4f0e1b54320c79e260ae9238e7fcefb733b978db81bae5e0d233fa9",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC53.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC53.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"contains\":[{\"recommendedName\":{\"fullName\":{\"value\":\"Fusion glycoprotein F2\"}}},{\"recommendedName\":{\"fullName\":{\"value\":\"Fusion glycoprotein F1\"}}}],\"flag\":\"Precursor\",\"recommendedName\":{\"fullName\":{\"value\":\"Fusion glycoprotein F0\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:22.414761+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "72eeca0dc4f0e1b54320c79e260ae9238e7fcefb733b978db81bae5e0d233fa9",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC53.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC53.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":482},\"start\":{\"modifier\":\"EXACT\",\"value\":20}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-01T06:25:22.414761+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "72eeca0dc4f0e1b54320c79e260ae9238e7fcefb733b978db81bae5e0d233fa9",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC53.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC53.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":503},\"start\":{\"modifier\":\"EXACT\",\"value\":483}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-01T06:25:22.414761+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "72eeca0dc4f0e1b54320c79e260ae9238e7fcefb733b978db81bae5e0d233fa9",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC53.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC53.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":538},\"start\":{\"modifier\":\"EXACT\",\"value\":504}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-01T06:25:22.414761+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "72eeca0dc4f0e1b54320c79e260ae9238e7fcefb733b978db81bae5e0d233fa9",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC53.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC53?format=txt&versions=80)

```json
{
  "entry_version": 80,
  "evidence_id": "H1",
  "excerpt": "ID   FUS_MUMPZ               Reviewed;         538 AA.\nAC   Q5SC53;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   21-DEC-2004, sequence version 1.\nDT   28-JAN-2026, entry version 80.\nDE   RecName: Full=Fusion glycoprotein F0;\nDE   Contains:\nDE     RecName: Full=Fusion glycoprotein F2;\nDE   Contains:\nDE     RecName: Full=Fusion glycoprotein F1;\nDE   Flags: Precursor;\nGN   Name=F;\nOS   Mumps virus genotype N (strain L-Zagreb vaccine) (MuV).\nOC   Viruses; Riboviria; Orthornavirae; Negarnaviricota; Haploviricotina;\nOC   Monjiviricetes; Mononegavirales; Paramyxoviridae; Rubulavirinae;\nOC   Orthorubulavirus; Orthorubulavirus parotitidis; Mumps orthorubulavirus.\nOX   NCBI_TaxID=301186;\nOH   NCBI_TaxID=9606; Homo sapiens (Human).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:38.619336+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-18",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "afb9ab9d6093f040c16474e49b884836fed8582e6d2cecfa0264668dfd09db66",
  "url": "https://rest.uniprot.org/unisave/Q5SC53?format=txt&versions=80"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC53?format=txt&versions=80)

```json
{
  "entry_version": 80,
  "evidence_id": "H2",
  "excerpt": "FT   TOPO_DOM        20..482\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000250\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:38.619336+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 124-126",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "afb9ab9d6093f040c16474e49b884836fed8582e6d2cecfa0264668dfd09db66",
  "url": "https://rest.uniprot.org/unisave/Q5SC53?format=txt&versions=80"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC53?format=txt&versions=80)

```json
{
  "entry_version": 80,
  "evidence_id": "H3",
  "excerpt": "FT   TRANSMEM        483..503\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:38.619336+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 127-129",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "afb9ab9d6093f040c16474e49b884836fed8582e6d2cecfa0264668dfd09db66",
  "url": "https://rest.uniprot.org/unisave/Q5SC53?format=txt&versions=80"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC53?format=txt&versions=80)

```json
{
  "entry_version": 80,
  "evidence_id": "H4",
  "excerpt": "FT   TOPO_DOM        504..538\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000250\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:38.619336+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 130-132",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "afb9ab9d6093f040c16474e49b884836fed8582e6d2cecfa0264668dfd09db66",
  "url": "https://rest.uniprot.org/unisave/Q5SC53?format=txt&versions=80"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 99. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
