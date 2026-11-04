# transmembrane_0068

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0068.txt)

**Task:** `transmembrane`  
**Expected answer:** **C** — 6..26

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MEIMNFSLNSPVFLLLSFFFLLMVLMQLTGSRKYKGKRLPPGPKKLPIIGNLHQMVGSLPHRVLKNLADQYGPVMHLQIGELSAIVISSADKAKEVLNTHGILVADRPQTTVAKIMLYNSLGATFAPYGDYLKQLRQIYALELLSPKTVRSFWTIMEDELSTMVTSVKAEAGQPIVLHDRMLTYLYATLCRATVGSVCNGRETLIMAAKETSALSAAIRIEDLFPSVKILPVVSGLRTRLTNLLKQLDTVLEDIIGEREKKMFSSNNIQPSTEEEDMLGVLLLYKNGKGKDTKFRITNNDIKAIIFELILAGTLSSSAIVEWCMSEMIKNPRVMKKAQDEVRQVLKDKKKVSGSDLAKLEYVKMVIKESVRLHPPAPLLFPREVREDFEMDGMIIPKKSWVIINYWAVGIDPKIWDDAERFEPERFSNSPIDFYGSHFELIPFGAGRRICPGILFGTTNVELLLASFLYHFDWKLPGGMKPEELDMNELFGAGCIRENPLCLIPSISVAGN

[Multiple Choices]
A. 6..26; 303..323
B. 27..47; 67..87; 100..120; 144..164; 202..222; 241..261; 274..294
C. 6..26
D. 11..26
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

> The sequence-matched UniProt annotation identifies 6..26 as a transmembrane helical signal-anchor. This is computational annotation (ECO:0000255), not direct experimental evidence.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminus contains a hydrophobic stretch consistent with a signal-anchor, while the sequence also has a recognizable cytochrome-P450-like catalytic-domain motif. Transferable knowledge that such enzymes commonly have an N-terminal membrane anchor and a globular catalytic domain favors the N-terminal option over many internal spans or numerous transmembrane segments.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and family-level pattern provide a meaningful basis for distinguishing the N-terminal anchor from the internal alternatives without knowing this protein's database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> C matches the annotated full interval, but D covers most of the strongly hydrophobic N-terminal core. Since the question does not specify how to treat boundaries or whether a subsegment of the spanning helix counts, D is a plausible narrower interval, though C is better supported as the full region.


### Important caveats

- The annotation supports the expected interval but is computational rather than experimental.
- Transmembrane boundaries can be approximate; the supplied sequence alone does not precisely establish residue-level endpoints.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminus contains a hydrophobic stretch consistent with a signal-anchor, while the sequence also has a recognizable cytochrome-P450-like catalytic-domain motif. Transferable knowledge that such enzymes commonly have an N-terminal membrane anchor and a globular catalytic domain favors the N-terminal option over many internal spans or numerous transmembrane segments.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and family-level pattern provide a meaningful basis for distinguishing the N-terminal anchor from the internal alternatives without knowing this protein's database record."
  },
  "case_id": "transmembrane_0068",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies 6..26 as a transmembrane helical signal-anchor. This is computational annotation (ECO:0000255), not direct experimental evidence."
  },
  "important_caveats": [
    "The annotation supports the expected interval but is computational rather than experimental.",
    "Transmembrane boundaries can be approximate; the supplied sequence alone does not precisely establish residue-level endpoints."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "C matches the annotated full interval, but D covers most of the strongly hydrophobic N-terminal core. Since the question does not specify how to treat boundaries or whether a subsegment of the spanning helix counts, D is a plausible narrower interval, though C is better supported as the full region."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0068",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies 6..26 as a transmembrane helical signal-anchor. This is computational annotation (ECO:0000255), not direct experimental evidence.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminus contains a hydrophobic stretch consistent with a signal-anchor, while the sequence also has a recognizable cytochrome-P450-like catalytic-domain motif. Transferable knowledge that such enzymes commonly have an N-terminal membrane anchor and a globular catalytic domain favors the N-terminal option over many internal spans or numerous transmembrane segments.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and family-level pattern provide a meaningful basis for distinguishing the N-terminal anchor from the internal alternatives without knowing this protein's database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "C matches the annotated full interval, but D covers most of the strongly hydrophobic N-terminal core. Since the question does not specify how to treat boundaries or whether a subsegment of the spanning helix counts, D is a plausible narrower interval, though C is better supported as the full region."
  },
  "important_caveats": [
    "The annotation supports the expected interval but is computational rather than experimental.",
    "Transmembrane boundaries can be approximate; the supplied sequence alone does not precisely establish residue-level endpoints."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DXJ2 annotates exactly one transmembrane feature at positions 6..26, described as 'Helical; Signal-anchor for type II membrane protein' (evidence ECO:0000255, by similarity). The sequence at positions 6-26 (FSLNSPVFLLLSFFFLLMVLM) is a hydrophobic N-terminal stretch consistent with a signal-anchor. No other TM region is annotated, which is consistent with the single-pass topology of cytochrome P450 enzymes. The heme-binding motif (FGAGRRICPGILFGTT near residues 443-459) confirms P450 family membership, for which a single N-terminal signal anchor is the established membrane-anchoring mechanism.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model can apply several transferable lines of reasoning: (1) The heme-binding signature 'FGAGRRICPGILFGTT' (around residues 443-459) identifies this as a cytochrome P450, a well-known single-pass membrane protein family anchored by an N-terminal signal-anchor helix, immediately eliminating option B (seven TM segments) as inconsistent with P450 topology. (2) The proposed second TM region in option A (303..323: AIIFELILAGTLSSSAIVEWC) contains multiple charged/polar residues (E, E, W, C) and lacks the sustained hydrophobicity required for a membrane-spanning helix, eliminating A. (3) Distinguishing C (6..26, 21 residues) from D (11..26, 16 residues): a transmembrane alpha-helix must span the ~30 Å hydrophobic core of the lipid bilayer, requiring approximately 20+ residues (at ~1.5 Å rise per residue). Sixteen residues (option D) would span only ~24 Å, which is below the minimum needed. Twenty-one residues (option C) is within the canonical 18-25 residue range. Additionally, the hydrophobic segment naturally begins at position 6 (F) and ends at position 26 (M), with position 27 (Q) being clearly polar, making 6..26 the natural boundary. While positions 6-10 contain some small polar residues (S, N), these are tolerated in signal-anchor helices, and the overall hydrophobic moment of the 21-residue segment is appropriate for membrane insertion.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The combination of P450 family recognition (from the heme-binding motif), single-pass membrane topology knowledge, and the biophysical length requirement for TM helices (~20+ residues) provides a concrete, transferable argument that meaningfully distinguishes C from all other options, particularly from D. No target-specific memorization is required.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While C (6..26) and D (11..26) overlap and differ only in the N-terminal boundary, the 16-residue length of D falls below the biophysical minimum for a membrane-spanning helix (~20 residues), and the natural hydrophobic boundary at position 6 (F) versus the clearly polar position 27 (Q) supports C as the unambiguous choice. The other options (A, B) are eliminated by topology and hydrophobicity arguments.


### Important caveats

- The UniProt annotation uses evidence code ECO:0000255 (by similarity), meaning the TM assignment is inferred from homology to related P450s rather than direct experimental measurement. However, the signal-anchor topology of P450s is extensively validated across the family.
- The distinction between C and D, while resolved by the length argument, is the tightest discrimination in this question. A model relying solely on hydrophobicity scoring without considering helix-length constraints might find D superficially attractive since positions 11-26 are more uniformly hydrophobic.
- The reviewer-only evidence confirms the sequence matches the UniProt entry exactly (SHA256 match), so the annotation applies directly to the supplied sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can apply several transferable lines of reasoning: (1) The heme-binding signature 'FGAGRRICPGILFGTT' (around residues 443-459) identifies this as a cytochrome P450, a well-known single-pass membrane protein family anchored by an N-terminal signal-anchor helix, immediately eliminating option B (seven TM segments) as inconsistent with P450 topology. (2) The proposed second TM region in option A (303..323: AIIFELILAGTLSSSAIVEWC) contains multiple charged/polar residues (E, E, W, C) and lacks the sustained hydrophobicity required for a membrane-spanning helix, eliminating A. (3) Distinguishing C (6..26, 21 residues) from D (11..26, 16 residues): a transmembrane alpha-helix must span the ~30 Å hydrophobic core of the lipid bilayer, requiring approximately 20+ residues (at ~1.5 Å rise per residue). Sixteen residues (option D) would span only ~24 Å, which is below the minimum needed. Twenty-one residues (option C) is within the canonical 18-25 residue range. Additionally, the hydrophobic segment naturally begins at position 6 (F) and ends at position 26 (M), with position 27 (Q) being clearly polar, making 6..26 the natural boundary. While positions 6-10 contain some small polar residues (S, N), these are tolerated in signal-anchor helices, and the overall hydrophobic moment of the 21-residue segment is appropriate for membrane insertion.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The combination of P450 family recognition (from the heme-binding motif), single-pass membrane topology knowledge, and the biophysical length requirement for TM helices (~20+ residues) provides a concrete, transferable argument that meaningfully distinguishes C from all other options, particularly from D. No target-specific memorization is required."
  },
  "case_id": "transmembrane_0068",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DXJ2 annotates exactly one transmembrane feature at positions 6..26, described as 'Helical; Signal-anchor for type II membrane protein' (evidence ECO:0000255, by similarity). The sequence at positions 6-26 (FSLNSPVFLLLSFFFLLMVLM) is a hydrophobic N-terminal stretch consistent with a signal-anchor. No other TM region is annotated, which is consistent with the single-pass topology of cytochrome P450 enzymes. The heme-binding motif (FGAGRRICPGILFGTT near residues 443-459) confirms P450 family membership, for which a single N-terminal signal anchor is the established membrane-anchoring mechanism."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (by similarity), meaning the TM assignment is inferred from homology to related P450s rather than direct experimental measurement. However, the signal-anchor topology of P450s is extensively validated across the family.",
    "The distinction between C and D, while resolved by the length argument, is the tightest discrimination in this question. A model relying solely on hydrophobicity scoring without considering helix-length constraints might find D superficially attractive since positions 11-26 are more uniformly hydrophobic.",
    "The reviewer-only evidence confirms the sequence matches the UniProt entry exactly (SHA256 match), so the annotation applies directly to the supplied sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While C (6..26) and D (11..26) overlap and differ only in the N-terminal boundary, the 16-residue length of D falls below the biophysical minimum for a membrane-spanning helix (~20 residues), and the natural hydrophobic boundary at position 6 (F) versus the clearly polar position 27 (Q) supports C as the unambiguous choice. The other options (A, B) are eliminated by topology and hydrophobicity arguments."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0068",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DXJ2 annotates exactly one transmembrane feature at positions 6..26, described as 'Helical; Signal-anchor for type II membrane protein' (evidence ECO:0000255, by similarity). The sequence at positions 6-26 (FSLNSPVFLLLSFFFLLMVLM) is a hydrophobic N-terminal stretch consistent with a signal-anchor. No other TM region is annotated, which is consistent with the single-pass topology of cytochrome P450 enzymes. The heme-binding motif (FGAGRRICPGILFGTT near residues 443-459) confirms P450 family membership, for which a single N-terminal signal anchor is the established membrane-anchoring mechanism.",
    "evidence_ids": ["C5", "H3", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model can apply several transferable lines of reasoning: (1) The heme-binding signature 'FGAGRRICPGILFGTT' (around residues 443-459) identifies this as a cytochrome P450, a well-known single-pass membrane protein family anchored by an N-terminal signal-anchor helix, immediately eliminating option B (seven TM segments) as inconsistent with P450 topology. (2) The proposed second TM region in option A (303..323: AIIFELILAGTLSSSAIVEWC) contains multiple charged/polar residues (E, E, W, C) and lacks the sustained hydrophobicity required for a membrane-spanning helix, eliminating A. (3) Distinguishing C (6..26, 21 residues) from D (11..26, 16 residues): a transmembrane alpha-helix must span the ~30 Å hydrophobic core of the lipid bilayer, requiring approximately 20+ residues (at ~1.5 Å rise per residue). Sixteen residues (option D) would span only ~24 Å, which is below the minimum needed. Twenty-one residues (option C) is within the canonical 18-25 residue range. Additionally, the hydrophobic segment naturally begins at position 6 (F) and ends at position 26 (M), with position 27 (Q) being clearly polar, making 6..26 the natural boundary. While positions 6-10 contain some small polar residues (S, N), these are tolerated in signal-anchor helices, and the overall hydrophobic moment of the 21-residue segment is appropriate for membrane insertion.",
    "missing_item_specific_fact": "",
    "reason": "The combination of P450 family recognition (from the heme-binding motif), single-pass membrane topology knowledge, and the biophysical length requirement for TM helices (~20+ residues) provides a concrete, transferable argument that meaningfully distinguishes C from all other options, particularly from D. No target-specific memorization is required."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While C (6..26) and D (11..26) overlap and differ only in the N-terminal boundary, the 16-residue length of D falls below the biophysical minimum for a membrane-spanning helix (~20 residues), and the natural hydrophobic boundary at position 6 (F) versus the clearly polar position 27 (Q) supports C as the unambiguous choice. The other options (A, B) are eliminated by topology and hydrophobicity arguments."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (by similarity), meaning the TM assignment is inferred from homology to related P450s rather than direct experimental measurement. However, the signal-anchor topology of P450s is extensively validated across the family.",
    "The distinction between C and D, while resolved by the length argument, is the tightest discrimination in this question. A model relying solely on hydrophobicity scoring without considering helix-length constraints might find D superficially attractive since positions 11-26 are more uniformly hydrophobic.",
    "The reviewer-only evidence confirms the sequence matches the UniProt entry exactly (SHA256 match), so the annotation applies directly to the supplied sequence."
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
  "benchmark_sequence_length": 511,
  "benchmark_sequence_sha256": "706fd69d57783df7add38c44c3e1cf2feb5cbcbc3afb9480407dd97165056ba4",
  "current_entry_audit": {
    "entryVersion": 4,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-06-18",
    "sequenceVersion": 1
  },
  "current_record_sha256": "0a578dd2253411bfb04df1ff174b97e1095a77d1afca3ac5d5c255b61dd81670",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 511,
  "current_source_sequence_sha256": "706fd69d57783df7add38c44c3e1cf2feb5cbcbc3afb9480407dd97165056ba4",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 2,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "P0DXJ2",
  "selected_historical_entry_version": 2,
  "selected_historical_record_sha256": "e16d6dbcf416765b91aad19c366057399ea06101f9cb2c5bb4976186438ed810",
  "selected_historical_source_sequence_length": 511,
  "selected_historical_source_sequence_sha256": "706fd69d57783df7add38c44c3e1cf2feb5cbcbc3afb9480407dd97165056ba4",
  "selected_historical_version": {
    "accession": "P0DXJ2",
    "database": "Swiss-Prot",
    "entryVersion": 2,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "SBE2_RAUSE",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ2.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DXJ2\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:29:30.229898+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a578dd2253411bfb04df1ff174b97e1095a77d1afca3ac5d5c255b61dd81670",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ2.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ2.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":4,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-06-18\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:29:30.229898+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a578dd2253411bfb04df1ff174b97e1095a77d1afca3ac5d5c255b61dd81670",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ2.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ2.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Serpentine wood\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Apocynaceae\",\"Rauvolfioideae\",\"Vinceae\",\"Rauvolfiinae\",\"Rauvolfia\"],\"scientificName\":\"Rauvolfia serpentina\",\"synonyms\":[\"Ophioxylon serpentinum\"],\"taxonId\":4060}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:29:30.229898+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a578dd2253411bfb04df1ff174b97e1095a77d1afca3ac5d5c255b61dd81670",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ2.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ2.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Cytochrome P450 SBE2\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P0DO13\",\"source\":\"UniProtKB\"}],\"value\":\"1.14.14.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"Sarpagan bridge enzyme 2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"RsSBE2\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:29:30.229898+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a578dd2253411bfb04df1ff174b97e1095a77d1afca3ac5d5c255b61dd81670",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ2.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ2.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical; Signal-anchor for type II membrane protein\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":26},\"start\":{\"modifier\":\"EXACT\",\"value\":6}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:29:30.229898+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a578dd2253411bfb04df1ff174b97e1095a77d1afca3ac5d5c255b61dd81670",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ2.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ2.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Guo J.\",\"Gao D.\",\"Lian J.\",\"Qu Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38212296\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-024-44797-z\"}],\"citationType\":\"journal article\",\"firstPage\":\"457\",\"id\":\"38212296\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"457\",\"publicationDate\":\"2024\",\"title\":\"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.\",\"volume\":\"15\"},\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"PATHWAY\",\"TISSUE SPECIFICITY\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:29:30.229898+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a578dd2253411bfb04df1ff174b97e1095a77d1afca3ac5d5c255b61dd81670",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ2.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ2?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H1",
  "excerpt": "ID   SBE2_RAUSE              Reviewed;         511 AA.\nAC   P0DXJ2;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-JUN-2025, sequence version 1.\nDT   28-JAN-2026, entry version 2.\nDE   RecName: Full=Sarpagan bridge enzyme 2 {ECO:0000303|PubMed:38212296};\nDE            Short=RsSBE2 {ECO:0000303|PubMed:38212296};\nDE            EC=1.14.14.- {ECO:0000250|UniProtKB:P0DO13};\nDE   AltName: Full=Cytochrome P450 SBE2 {ECO:0000305};\nGN   Name=SBE2 {ECO:0000303|PubMed:38212296};\nOS   Rauvolfia serpentina (Serpentine wood) (Ophioxylon serpentinum).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Vinceae;\nOC   Rauvolfiinae; Rauvolfia.\nOX   NCBI_TaxID=4060;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:34.434063+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e16d6dbcf416765b91aad19c366057399ea06101f9cb2c5bb4976186438ed810",
  "url": "https://rest.uniprot.org/unisave/P0DXJ2?format=txt&versions=2"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ2?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H2",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, PATHWAY, TISSUE SPECIFICITY, AND\nRP   BIOTECHNOLOGY.\nRX   PubMed=38212296; DOI=10.1038/s41467-024-44797-z;\nRA   Guo J., Gao D., Lian J., Qu Y.;\nRT   \"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.\";\nRL   Nat. Commun. 15:457-457(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:34.434063+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 17-23",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e16d6dbcf416765b91aad19c366057399ea06101f9cb2c5bb4976186438ed810",
  "url": "https://rest.uniprot.org/unisave/P0DXJ2?format=txt&versions=2"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ2?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H3",
  "excerpt": "FT   TRANSMEM        6..26\nFT                   /note=\"Helical; Signal-anchor for type II membrane protein\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:34.434063+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 116-118",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e16d6dbcf416765b91aad19c366057399ea06101f9cb2c5bb4976186438ed810",
  "url": "https://rest.uniprot.org/unisave/P0DXJ2?format=txt&versions=2"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 68. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
