# active_site_0058

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0058.txt)

**Task:** `active_site`  
**Expected answer:** **D** — Position 2 (Schiff-base intermediate with DNA)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MPEGDTVFHTAAALRAALEGKTLTRCDVRVPRYATVDLSGAVVDEVLSRGKHLFIRAGSASIHSHLKMEGAWRIGHTKVAPHRIRIVLETADTRAIGIDLGILEVLDRGTDMDAVAYLGPDLLGPDWEPRVAADNLAADPDRPLAQALLDQRVMAGVGNVYCNELCFVFGRLPTAPVGTLKDPLRVVQRARDMLWLNRSRWNRTTTGDTRNGRQLWVYGRAGEPCRRCGTLIQTDRGGERVTYWCPVCQTAS

[Multiple Choices]
A. Position 250 (Proton acceptor)
B. Position 266 (Proton acceptor)
C. Position 283 (Proton donor/acceptor)
D. Position 2 (Schiff-base intermediate with DNA)
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

> The sequence-matched UniProt record annotates residue 2 as the Schiff-base intermediate with DNA, matching choice D. The annotation is supported by a PROSITE rule and cited literature; the excerpts do not provide the underlying experimental results directly.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A transferable feature of Nei/Fpg-family DNA glycosylase/AP lyases is the catalytic N-terminal proline, which forms a Schiff-base intermediate with DNA during lyase chemistry. The sequence has Pro at position 2, and choice D specifically pairs that position with this role, distinguishing it from the alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level knowledge about DNA glycosylase/AP lyase chemistry and the conserved catalytic N-terminal proline provides a meaningful basis for choosing D. The exact target annotation is not necessary for that inference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, only D matches the conserved catalytic N-terminal proline and its Schiff-base role.


### Important caveats

- The reviewer-only record matches the supplied sequence. Its active-site annotation cites both computational rule-based evidence and literature, but the supplied excerpts do not independently demonstrate the experimental result.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A transferable feature of Nei/Fpg-family DNA glycosylase/AP lyases is the catalytic N-terminal proline, which forms a Schiff-base intermediate with DNA during lyase chemistry. The sequence has Pro at position 2, and choice D specifically pairs that position with this role, distinguishing it from the alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level knowledge about DNA glycosylase/AP lyase chemistry and the conserved catalytic N-terminal proline provides a meaningful basis for choosing D. The exact target annotation is not necessary for that inference."
  },
  "case_id": "active_site_0058",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates residue 2 as the Schiff-base intermediate with DNA, matching choice D. The annotation is supported by a PROSITE rule and cited literature; the excerpts do not provide the underlying experimental results directly."
  },
  "important_caveats": [
    "The reviewer-only record matches the supplied sequence. Its active-site annotation cites both computational rule-based evidence and literature, but the supplied excerpts do not independently demonstrate the experimental result."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, only D matches the conserved catalytic N-terminal proline and its Schiff-base role."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0058",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates residue 2 as the Schiff-base intermediate with DNA, matching choice D. The annotation is supported by a PROSITE rule and cited literature; the excerpts do not provide the underlying experimental results directly.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A transferable feature of Nei/Fpg-family DNA glycosylase/AP lyases is the catalytic N-terminal proline, which forms a Schiff-base intermediate with DNA during lyase chemistry. The sequence has Pro at position 2, and choice D specifically pairs that position with this role, distinguishing it from the alternatives.",
    "missing_item_specific_fact": "",
    "reason": "Family-level knowledge about DNA glycosylase/AP lyase chemistry and the conserved catalytic N-terminal proline provides a meaningful basis for choosing D. The exact target annotation is not necessary for that inference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, only D matches the conserved catalytic N-terminal proline and its Schiff-base role."
  },
  "important_caveats": [
    "The reviewer-only record matches the supplied sequence. Its active-site annotation cites both computational rule-based evidence and literature, but the supplied excerpts do not independently demonstrate the experimental result."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (evidence_id C5/H4) explicitly lists position 2 (Pro) as 'Schiff-base intermediate with DNA' with evidence from PROSITE-ProRule (PRU00392), PubMed 36610794, and PubMed 39012146. The PDB structure 8TJG and mutagenesis data (MUTAGENESIS OF PRO-2) further confirm Pro-2 as the Schiff-base residue. The sequence begins MPEG..., so position 2 is indeed Proline, consistent with the known N-terminal Pro Schiff-base mechanism of Endonuclease III-family AP lyases.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C13](#evidence-c13), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Multiple transferable inferences distinguish D from the alternatives: (1) The sequence is 252 residues long, so positions 266 (option B) and 283 (option C) are physically impossible—this eliminates two choices purely from the input. (2) The N-terminal Pro-Glu motif (MPEG...) is a hallmark of the Endonuclease III / AP lyase superfamily (Nei, EndoIII, EndoVIII, Fpg, etc.), where the N-terminal proline's α-amino group forms a Schiff base with the C1' of the abasic sugar. This is well-established family-level mechanism knowledge. (3) The C-terminal CXXC motif (CPVCQTAS at ~245-252) is the conserved Zn-binding module of this family, further supporting family identification. (4) The 'Schiff-base intermediate with DNA' description is mechanistically specific to AP lyases, not generic proton-transfer enzymes. (5) Position 250 is Threonine (from counting the last 8 residues CPVCQTAS), which is a chemically implausible proton acceptor for DNA backbone cleavage, making option A unattractive. Together, these family-level and sequence-level arguments converge on D without requiring the exact UniProt record for this protein.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can eliminate B and C by noting positions exceed the 252-residue sequence, identify the EndoIII/AP lyase family from the N-terminal Pro-Glu motif and C-terminal Zn-binding CXXC motif, apply the well-known family mechanism that the N-terminal Pro forms a Schiff base with abasic DNA, and reject position 250 (Thr) as an unlikely proton acceptor. This constitutes concrete transferable inference from family knowledge and sequence analysis.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B and C are eliminated by sequence length. Option A (position 250, Thr as proton acceptor) is chemically implausible for this enzyme class. Option D is uniquely supported by the N-terminal Pro Schiff-base mechanism characteristic of AP lyases. No ambiguity among the offered choices.


### Important caveats

- The sequence length (252 aa) is derivable from the provided input, making elimination of B and C a straightforward arithmetic check.
- The EndoIII/AP lyase family mechanism (N-terminal Pro Schiff base) is textbook-level knowledge transferable across many characterized members (E. coli EndoIII, Fpg, human APE1 homologs, etc.).
- The UniProt annotation for position 2 carries both PROSITE-ProRule (computational/family) and experimental (PubMed, PDB 8TJG) evidence codes, strengthening the key.
- The reviewer-only evidence confirms the sequence matches the source record exactly (SHA-256 match), so position numbering is canonical.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Multiple transferable inferences distinguish D from the alternatives: (1) The sequence is 252 residues long, so positions 266 (option B) and 283 (option C) are physically impossible—this eliminates two choices purely from the input. (2) The N-terminal Pro-Glu motif (MPEG...) is a hallmark of the Endonuclease III / AP lyase superfamily (Nei, EndoIII, EndoVIII, Fpg, etc.), where the N-terminal proline's α-amino group forms a Schiff base with the C1' of the abasic sugar. This is well-established family-level mechanism knowledge. (3) The C-terminal CXXC motif (CPVCQTAS at ~245-252) is the conserved Zn-binding module of this family, further supporting family identification. (4) The 'Schiff-base intermediate with DNA' description is mechanistically specific to AP lyases, not generic proton-transfer enzymes. (5) Position 250 is Threonine (from counting the last 8 residues CPVCQTAS), which is a chemically implausible proton acceptor for DNA backbone cleavage, making option A unattractive. Together, these family-level and sequence-level arguments converge on D without requiring the exact UniProt record for this protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate B and C by noting positions exceed the 252-residue sequence, identify the EndoIII/AP lyase family from the N-terminal Pro-Glu motif and C-terminal Zn-binding CXXC motif, apply the well-known family mechanism that the N-terminal Pro forms a Schiff base with abasic DNA, and reject position 250 (Thr) as an unlikely proton acceptor. This constitutes concrete transferable inference from family knowledge and sequence analysis."
  },
  "case_id": "active_site_0058",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C13",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence_id C5/H4) explicitly lists position 2 (Pro) as 'Schiff-base intermediate with DNA' with evidence from PROSITE-ProRule (PRU00392), PubMed 36610794, and PubMed 39012146. The PDB structure 8TJG and mutagenesis data (MUTAGENESIS OF PRO-2) further confirm Pro-2 as the Schiff-base residue. The sequence begins MPEG..., so position 2 is indeed Proline, consistent with the known N-terminal Pro Schiff-base mechanism of Endonuclease III-family AP lyases."
  },
  "important_caveats": [
    "The sequence length (252 aa) is derivable from the provided input, making elimination of B and C a straightforward arithmetic check.",
    "The EndoIII/AP lyase family mechanism (N-terminal Pro Schiff base) is textbook-level knowledge transferable across many characterized members (E. coli EndoIII, Fpg, human APE1 homologs, etc.).",
    "The UniProt annotation for position 2 carries both PROSITE-ProRule (computational/family) and experimental (PubMed, PDB 8TJG) evidence codes, strengthening the key.",
    "The reviewer-only evidence confirms the sequence matches the source record exactly (SHA-256 match), so position numbering is canonical."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and C are eliminated by sequence length. Option A (position 250, Thr as proton acceptor) is chemically implausible for this enzyme class. Option D is uniquely supported by the N-terminal Pro Schiff-base mechanism characteristic of AP lyases. No ambiguity among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0058",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence_id C5/H4) explicitly lists position 2 (Pro) as 'Schiff-base intermediate with DNA' with evidence from PROSITE-ProRule (PRU00392), PubMed 36610794, and PubMed 39012146. The PDB structure 8TJG and mutagenesis data (MUTAGENESIS OF PRO-2) further confirm Pro-2 as the Schiff-base residue. The sequence begins MPEG..., so position 2 is indeed Proline, consistent with the known N-terminal Pro Schiff-base mechanism of Endonuclease III-family AP lyases.",
    "evidence_ids": ["C5", "H4", "C13", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Multiple transferable inferences distinguish D from the alternatives: (1) The sequence is 252 residues long, so positions 266 (option B) and 283 (option C) are physically impossible—this eliminates two choices purely from the input. (2) The N-terminal Pro-Glu motif (MPEG...) is a hallmark of the Endonuclease III / AP lyase superfamily (Nei, EndoIII, EndoVIII, Fpg, etc.), where the N-terminal proline's α-amino group forms a Schiff base with the C1' of the abasic sugar. This is well-established family-level mechanism knowledge. (3) The C-terminal CXXC motif (CPVCQTAS at ~245-252) is the conserved Zn-binding module of this family, further supporting family identification. (4) The 'Schiff-base intermediate with DNA' description is mechanistically specific to AP lyases, not generic proton-transfer enzymes. (5) Position 250 is Threonine (from counting the last 8 residues CPVCQTAS), which is a chemically implausible proton acceptor for DNA backbone cleavage, making option A unattractive. Together, these family-level and sequence-level arguments converge on D without requiring the exact UniProt record for this protein.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate B and C by noting positions exceed the 252-residue sequence, identify the EndoIII/AP lyase family from the N-terminal Pro-Glu motif and C-terminal Zn-binding CXXC motif, apply the well-known family mechanism that the N-terminal Pro forms a Schiff base with abasic DNA, and reject position 250 (Thr) as an unlikely proton acceptor. This constitutes concrete transferable inference from family knowledge and sequence analysis."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and C are eliminated by sequence length. Option A (position 250, Thr as proton acceptor) is chemically implausible for this enzyme class. Option D is uniquely supported by the N-terminal Pro Schiff-base mechanism characteristic of AP lyases. No ambiguity among the offered choices."
  },
  "important_caveats": [
    "The sequence length (252 aa) is derivable from the provided input, making elimination of B and C a straightforward arithmetic check.",
    "The EndoIII/AP lyase family mechanism (N-terminal Pro Schiff base) is textbook-level knowledge transferable across many characterized members (E. coli EndoIII, Fpg, human APE1 homologs, etc.).",
    "The UniProt annotation for position 2 carries both PROSITE-ProRule (computational/family) and experimental (PubMed, PDB 8TJG) evidence codes, strengthening the key.",
    "The reviewer-only evidence confirms the sequence matches the source record exactly (SHA-256 match), so position numbering is canonical."
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
  "benchmark_sequence_length": 252,
  "benchmark_sequence_sha256": "3219f396f539d267333a763309b8cbd0a0d2cd246ccaaaf6d27d6db63a93ffaa",
  "current_entry_audit": {
    "entryVersion": 142,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2007-01-09",
    "sequenceVersion": 1
  },
  "current_record_sha256": "b72936fb186d87f999459cf22fcc46f87445018b9365aaa10ca9300a71265c48",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 252,
  "current_source_sequence_sha256": "3219f396f539d267333a763309b8cbd0a0d2cd246ccaaaf6d27d6db63a93ffaa",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 140,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0QT90",
  "selected_historical_entry_version": 140,
  "selected_historical_record_sha256": "cad634b3155da705ea406278043495c2debf7a3d6601408d3f08e21191494cfe",
  "selected_historical_source_sequence_length": 252,
  "selected_historical_source_sequence_sha256": "3219f396f539d267333a763309b8cbd0a0d2cd246ccaaaf6d27d6db63a93ffaa",
  "selected_historical_version": {
    "accession": "A0QT90",
    "database": "Swiss-Prot",
    "entryVersion": 140,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "END8B_MYCS2",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0QT90.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0QT90\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:56.186229+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b72936fb186d87f999459cf22fcc46f87445018b9365aaa10ca9300a71265c48",
  "url": "https://rest.uniprot.org/uniprotkb/A0QT90.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0QT90.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":142,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2007-01-09\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:56.186229+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b72936fb186d87f999459cf22fcc46f87445018b9365aaa10ca9300a71265c48",
  "url": "https://rest.uniprot.org/uniprotkb/A0QT90.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0QT90.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Mycobacterium smegmatis\",\"lineage\":[\"Bacteria\",\"Bacillati\",\"Actinomycetota\",\"Actinomycetes\",\"Mycobacteriales\",\"Mycobacteriaceae\",\"Mycolicibacterium\"],\"scientificName\":\"Mycolicibacterium smegmatis (strain ATCC 700084 / mc(2)155)\",\"taxonId\":246196}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:56.186229+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b72936fb186d87f999459cf22fcc46f87445018b9365aaa10ca9300a71265c48",
  "url": "https://rest.uniprot.org/uniprotkb/A0QT90.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0QT90.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P9WNC1\",\"source\":\"UniProtKB\"}],\"value\":\"Endonuclease 8 2\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00392\",\"source\":\"PROSITE-ProRule\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39012146\",\"source\":\"PubMed\"}],\"value\":\"3.2.2.-\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00392\",\"source\":\"PROSITE-ProRule\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36610794\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39012146\",\"source\":\"PubMed\"}],\"value\":\"4.2.99.18\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36610794\",\"source\":\"PubMed\"}],\"value\":\"DNA-(apurinic or apyrimidinic site) lyase Nei2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36610794\",\"source\":\"PubMed\"}],\"value\":\"AP lyase\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:56.186229+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b72936fb186d87f999459cf22fcc46f87445018b9365aaa10ca9300a71265c48",
  "url": "https://rest.uniprot.org/uniprotkb/A0QT90.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0QT90.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Schiff-base intermediate with DNA\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00392\",\"source\":\"PROSITE-ProRule\"},{\"evidenceCode\":\"ECO:0000305\",\"id\":\"36610794\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000305\",\"id\":\"39012146\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":2},\"start\":{\"modifier\":\"EXACT\",\"value\":2}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-01T06:24:56.186229+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b72936fb186d87f999459cf22fcc46f87445018b9365aaa10ca9300a71265c48",
  "url": "https://rest.uniprot.org/uniprotkb/A0QT90.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0QT90.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Proton donor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00392\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":3},\"start\":{\"modifier\":\"EXACT\",\"value\":3}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-01T06:24:56.186229+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b72936fb186d87f999459cf22fcc46f87445018b9365aaa10ca9300a71265c48",
  "url": "https://rest.uniprot.org/uniprotkb/A0QT90.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0QT90.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Proton donor (in beta-elimination)\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00392\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":51},\"start\":{\"modifier\":\"EXACT\",\"value\":51}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-01T06:24:56.186229+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b72936fb186d87f999459cf22fcc46f87445018b9365aaa10ca9300a71265c48",
  "url": "https://rest.uniprot.org/uniprotkb/A0QT90.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0QT90.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39012146\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8TJG\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29105\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29105\",\"name\":\"Zn(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":225},\"start\":{\"modifier\":\"EXACT\",\"value\":225}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-01T06:24:56.186229+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b72936fb186d87f999459cf22fcc46f87445018b9365aaa10ca9300a71265c48",
  "url": "https://rest.uniprot.org/uniprotkb/A0QT90.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0QT90.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39012146\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8TJG\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29105\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29105\",\"name\":\"Zn(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":228},\"start\":{\"modifier\":\"EXACT\",\"value\":228}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-01T06:24:56.186229+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b72936fb186d87f999459cf22fcc46f87445018b9365aaa10ca9300a71265c48",
  "url": "https://rest.uniprot.org/uniprotkb/A0QT90.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0QT90.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39012146\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8TJG\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29105\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29105\",\"name\":\"Zn(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":245},\"start\":{\"modifier\":\"EXACT\",\"value\":245}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-01T06:24:56.186229+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b72936fb186d87f999459cf22fcc46f87445018b9365aaa10ca9300a71265c48",
  "url": "https://rest.uniprot.org/uniprotkb/A0QT90.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0QT90.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39012146\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8TJG\",\"source\":\"PDB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:29105\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:29105\",\"name\":\"Zn(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":248},\"start\":{\"modifier\":\"EXACT\",\"value\":248}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-01T06:24:56.186229+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b72936fb186d87f999459cf22fcc46f87445018b9365aaa10ca9300a71265c48",
  "url": "https://rest.uniprot.org/uniprotkb/A0QT90.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0QT90.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"citation\":{\"authors\":[\"Warren G.M.\",\"Ejaz A.\",\"Fay A.\",\"Glickman M.S.\",\"Shuman S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"36610794\"},{\"database\":\"DOI\",\"id\":\"10.1093/nar/gkac1222\"}],\"citationType\":\"journal article\",\"firstPage\":\"218\",\"id\":\"36610794\",\"journal\":\"Nucleic Acids Res.\",\"lastPage\":\"235\",\"publicationDate\":\"2023\",\"title\":\"Mycobacterial helicase Lhr abets resistance to DNA crosslinking agents mitomycin C and cisplatin.\",\"volume\":\"51\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC 700084 / mc(2)155\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PROBABLE ACTIVE SITE\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-01T06:24:56.186229+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b72936fb186d87f999459cf22fcc46f87445018b9365aaa10ca9300a71265c48",
  "url": "https://rest.uniprot.org/uniprotkb/A0QT90.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0QT90.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"citation\":{\"authors\":[\"Warren G.M.\",\"Shuman S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39012146\"},{\"database\":\"DOI\",\"id\":\"10.1128/mbio.01248-24\"}],\"citationType\":\"journal article\",\"firstPage\":\"e0124824\",\"id\":\"39012146\",\"journal\":\"MBio\",\"lastPage\":\"e0124824\",\"publicationDate\":\"2024\",\"title\":\"Structure and in vivo psoralen DNA crosslink repair activity of mycobacterial Nei2.\",\"volume\":\"15\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8TJG\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC 700084 / mc(2)155\"}],\"referenceNumber\":5,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.45 ANGSTROMS) IN COMPLEX WITH ZN(2+)\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PROBABLE ACTIVE SITE\",\"COFACTOR\",\"SUBUNIT\",\"DISRUPTION PHENOTYPE\",\"MUTAGENESIS OF PRO-2; GLU-3 AND LYS-51\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-01T06:24:56.186229+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b72936fb186d87f999459cf22fcc46f87445018b9365aaa10ca9300a71265c48",
  "url": "https://rest.uniprot.org/uniprotkb/A0QT90.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0QT90?format=txt&versions=140)

```json
{
  "entry_version": 140,
  "evidence_id": "H1",
  "excerpt": "ID   END8B_MYCS2             Reviewed;         252 AA.\nAC   A0QT90; I7G4T3;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   09-JAN-2007, sequence version 1.\nDT   28-JAN-2026, entry version 140.\nDE   RecName: Full=DNA-(apurinic or apyrimidinic site) lyase Nei2 {ECO:0000303|PubMed:36610794};\nDE            Short=AP lyase {ECO:0000303|PubMed:36610794};\nDE            EC=3.2.2.- {ECO:0000255|PROSITE-ProRule:PRU00392, ECO:0000269|PubMed:39012146};\nDE            EC=4.2.99.18 {ECO:0000255|PROSITE-ProRule:PRU00392, ECO:0000269|PubMed:36610794, ECO:0000269|PubMed:39012146};\nDE   AltName: Full=Endonuclease 8 2 {ECO:0000250|UniProtKB:P9WNC1};\nGN   Name=nei2 {ECO:0000303|PubMed:36610794};\nGN   OrderedLocusNames=MSMEG_1756 {ECO:0000312|EMBL:ABK74586.1};\nOS   Mycolicibacterium smegmatis (strain ATCC 700084 / mc(2)155) (Mycobacterium\nOS   smegmatis).\nOC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Mycobacteriales;\nOC   Mycobacteriaceae; Mycolicibacterium.\nOX   NCBI_TaxID=246196;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:42.166883+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cad634b3155da705ea406278043495c2debf7a3d6601408d3f08e21191494cfe",
  "url": "https://rest.uniprot.org/unisave/A0QT90?format=txt&versions=140"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0QT90?format=txt&versions=140)

```json
{
  "entry_version": 140,
  "evidence_id": "H2",
  "excerpt": "RN   [4]\nRP   FUNCTION, CATALYTIC ACTIVITY, PROBABLE ACTIVE SITE, AND SUBUNIT.\nRC   STRAIN=ATCC 700084 / mc(2)155;\nRX   PubMed=36610794; DOI=10.1093/nar/gkac1222;\nRA   Warren G.M., Ejaz A., Fay A., Glickman M.S., Shuman S.;\nRT   \"Mycobacterial helicase Lhr abets resistance to DNA crosslinking agents\nRT   mitomycin C and cisplatin.\";\nRL   Nucleic Acids Res. 51:218-235(2023).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:42.166883+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 42-49",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cad634b3155da705ea406278043495c2debf7a3d6601408d3f08e21191494cfe",
  "url": "https://rest.uniprot.org/unisave/A0QT90?format=txt&versions=140"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0QT90?format=txt&versions=140)

```json
{
  "entry_version": 140,
  "evidence_id": "H3",
  "excerpt": "RN   [5] {ECO:0007744|PDB:8TJG}\nRP   X-RAY CRYSTALLOGRAPHY (1.45 ANGSTROMS) IN COMPLEX WITH ZN(2+), FUNCTION,\nRP   CATALYTIC ACTIVITY, PROBABLE ACTIVE SITE, COFACTOR, SUBUNIT, DISRUPTION\nRP   PHENOTYPE, AND MUTAGENESIS OF PRO-2; GLU-3 AND LYS-51.\nRC   STRAIN=ATCC 700084 / mc(2)155;\nRX   PubMed=39012146; DOI=10.1128/mbio.01248-24;\nRA   Warren G.M., Shuman S.;\nRT   \"Structure and in vivo psoralen DNA crosslink repair activity of\nRT   mycobacterial Nei2.\";\nRL   MBio 15:e0124824-e0124824(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:42.166883+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 50-59",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cad634b3155da705ea406278043495c2debf7a3d6601408d3f08e21191494cfe",
  "url": "https://rest.uniprot.org/unisave/A0QT90?format=txt&versions=140"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0QT90?format=txt&versions=140)

```json
{
  "entry_version": 140,
  "evidence_id": "H4",
  "excerpt": "FT   ACT_SITE        2\nFT                   /note=\"Schiff-base intermediate with DNA\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00392,\nFT                   ECO:0000305|PubMed:36610794, ECO:0000305|PubMed:39012146\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:42.166883+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 163-166",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cad634b3155da705ea406278043495c2debf7a3d6601408d3f08e21191494cfe",
  "url": "https://rest.uniprot.org/unisave/A0QT90?format=txt&versions=140"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0QT90?format=txt&versions=140)

```json
{
  "entry_version": 140,
  "evidence_id": "H5",
  "excerpt": "FT   ACT_SITE        3\nFT                   /note=\"Proton donor\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00392\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:42.166883+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 167-169",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cad634b3155da705ea406278043495c2debf7a3d6601408d3f08e21191494cfe",
  "url": "https://rest.uniprot.org/unisave/A0QT90?format=txt&versions=140"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0QT90?format=txt&versions=140)

```json
{
  "entry_version": 140,
  "evidence_id": "H6",
  "excerpt": "FT   ACT_SITE        51\nFT                   /note=\"Proton donor (in beta-elimination)\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00392\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:42.166883+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 170-172",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cad634b3155da705ea406278043495c2debf7a3d6601408d3f08e21191494cfe",
  "url": "https://rest.uniprot.org/unisave/A0QT90?format=txt&versions=140"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0QT90?format=txt&versions=140)

```json
{
  "entry_version": 140,
  "evidence_id": "H7",
  "excerpt": "FT   BINDING         225\nFT                   /ligand=\"Zn(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29105\"\nFT                   /evidence=\"ECO:0000269|PubMed:39012146,\nFT                   ECO:0007744|PDB:8TJG\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:42.166883+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 173-177",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cad634b3155da705ea406278043495c2debf7a3d6601408d3f08e21191494cfe",
  "url": "https://rest.uniprot.org/unisave/A0QT90?format=txt&versions=140"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0QT90?format=txt&versions=140)

```json
{
  "entry_version": 140,
  "evidence_id": "H8",
  "excerpt": "FT   BINDING         228\nFT                   /ligand=\"Zn(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29105\"\nFT                   /evidence=\"ECO:0000269|PubMed:39012146,\nFT                   ECO:0007744|PDB:8TJG\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:42.166883+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 178-182",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cad634b3155da705ea406278043495c2debf7a3d6601408d3f08e21191494cfe",
  "url": "https://rest.uniprot.org/unisave/A0QT90?format=txt&versions=140"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0QT90?format=txt&versions=140)

```json
{
  "entry_version": 140,
  "evidence_id": "H9",
  "excerpt": "FT   BINDING         245\nFT                   /ligand=\"Zn(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29105\"\nFT                   /evidence=\"ECO:0000269|PubMed:39012146,\nFT                   ECO:0007744|PDB:8TJG\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:42.166883+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 183-187",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cad634b3155da705ea406278043495c2debf7a3d6601408d3f08e21191494cfe",
  "url": "https://rest.uniprot.org/unisave/A0QT90?format=txt&versions=140"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0QT90?format=txt&versions=140)

```json
{
  "entry_version": 140,
  "evidence_id": "H10",
  "excerpt": "FT   BINDING         248\nFT                   /ligand=\"Zn(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:29105\"\nFT                   /evidence=\"ECO:0000269|PubMed:39012146,\nFT                   ECO:0007744|PDB:8TJG\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:42.166883+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 188-192",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cad634b3155da705ea406278043495c2debf7a3d6601408d3f08e21191494cfe",
  "url": "https://rest.uniprot.org/unisave/A0QT90?format=txt&versions=140"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 58. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
