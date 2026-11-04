# active_site_0142

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0142.txt)

**Task:** `active_site`  
**Expected answer:** **B** — Position 12 (Proton acceptor)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAPLITNIYTADPSAHVFNGKLYIYPSHDRETDIQFNDNGDQYDMADYHVFSLDSLDPPSEVTDHGVVLKVEDIPWVSKQLWAPDAATKDGKYYLYFPARDKEGIFRIGVAVSDKPEGPFTPDPEPIKGSYSIDPAVFVDDDGSAYMYFGGLWGGQLQCYQKGNNIFDAEWSGPKEPSGSGAKALGPRVAKLTDDMRQFAEEVREIVILAPETGEPLAADDHDRRFFEAAWMHKYNGKYYFSYSTGDTHYLVYAVGDSPYGPFTYGGRILEPVLGWTTHHSIVEFQGRWWLFHHDCELSKGVDHLRSVKVKEIWYDKDGKIVTEKPE

[Multiple Choices]
A. Position 2340 (For beta-ketoacyl synthase 2 activity)
B. Position 12 (Proton acceptor)
C. Position 26 (Proton donor/acceptor)
D. Position 975 (Proton acceptor; for dehydratase activity 1)
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

> The sequence-matched UniProt record annotates residue 12 as the proton acceptor. This supports the key as an annotation, though the cited evidence is transferred from a homolog rather than direct experimental evidence for this exact protein.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is 327 residues long, so positions 975 and 2340 are out of range. Position 26 is Pro, an implausible proton acceptor/donor, whereas position 12 is Asp. Transferable knowledge of GH43 glycoside hydrolases supports an N-terminal catalytic Asp acting as a proton acceptor; that family-level pattern, together with the alternatives, meaningfully favors B.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The offered choices can be distinguished from sequence length, residue identity, and transferable knowledge of catalytic residues in GH43 enzymes; recalling this exact protein's annotation is not necessary.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The other position-based choices are either outside the sequence or assign a proton-transfer role to Pro at position 26.


### Important caveats

- The exact-protein annotation is supported by homolog-based evidence, not direct experimental confirmation in the supplied sources.
- The author’s precise source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is 327 residues long, so positions 975 and 2340 are out of range. Position 26 is Pro, an implausible proton acceptor/donor, whereas position 12 is Asp. Transferable knowledge of GH43 glycoside hydrolases supports an N-terminal catalytic Asp acting as a proton acceptor; that family-level pattern, together with the alternatives, meaningfully favors B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The offered choices can be distinguished from sequence length, residue identity, and transferable knowledge of catalytic residues in GH43 enzymes; recalling this exact protein's annotation is not necessary."
  },
  "case_id": "active_site_0142",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates residue 12 as the proton acceptor. This supports the key as an annotation, though the cited evidence is transferred from a homolog rather than direct experimental evidence for this exact protein."
  },
  "important_caveats": [
    "The exact-protein annotation is supported by homolog-based evidence, not direct experimental confirmation in the supplied sources.",
    "The author’s precise source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The other position-based choices are either outside the sequence or assign a proton-transfer role to Pro at position 26."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0142",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates residue 12 as the proton acceptor. This supports the key as an annotation, though the cited evidence is transferred from a homolog rather than direct experimental evidence for this exact protein.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is 327 residues long, so positions 975 and 2340 are out of range. Position 26 is Pro, an implausible proton acceptor/donor, whereas position 12 is Asp. Transferable knowledge of GH43 glycoside hydrolases supports an N-terminal catalytic Asp acting as a proton acceptor; that family-level pattern, together with the alternatives, meaningfully favors B.",
    "missing_item_specific_fact": "",
    "reason": "The offered choices can be distinguished from sequence length, residue identity, and transferable knowledge of catalytic residues in GH43 enzymes; recalling this exact protein's annotation is not necessary."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The other position-based choices are either outside the sequence or assign a proton-transfer role to Pro at position 26."
  },
  "important_caveats": [
    "The exact-protein annotation is supported by homolog-based evidence, not direct experimental confirmation in the supplied sources.",
    "The author’s precise source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (C5, H3) confirms position 12 as 'Proton acceptor' active site. Position 12 in the 327-aa sequence is D (Aspartate), consistent with the canonical GH43 catalytic mechanism. The annotation evidence code is ECO:0000250 (similarity-based transfer from Q45071), so it is a computational inference rather than direct experimental proof for this exact protein, but it is consistent with well-established GH43 family catalytic chemistry. Options A (position 2340) and D (position 975) exceed the 327-residue sequence length and are physically impossible. Option C (position 26) corresponds to Proline in the sequence, which cannot serve as a proton donor/acceptor.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Three independent lines of transferable reasoning distinguish B from the other choices: (1) Sequence-length elimination: the provided sequence is 327 residues, so positions 2340 (A) and 975 (D) are immediately impossible. (2) Amino-acid chemistry at the candidate positions: position 12 is Asp (D), a canonical proton acceptor in glycoside hydrolases via its carboxylate side chain; position 26 is Pro (P), whose cyclic side chain lacks any ionizable or hydrogen-bonding group and whose backbone amide is locked in the pyrrolidine ring, making it chemically incapable of proton donation/acceptance. (3) GH43 family knowledge: the sequence contains hallmark GH43 motifs (e.g., YFP/YFG/YFSY patterns), and in GH43 β-propeller enzymes the proton acceptor is invariably an Asp or Glu positioned near the N-terminus of the first β-strand, while the proton donor is a second Asp/Glu ~200 residues downstream. Position 12 Asp fits this family-level pattern precisely. Together these arguments uniquely select B without needing to recall this protein's specific database entry.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can eliminate A and D by noting they exceed the 327-aa sequence length, eliminate C because Proline at position 26 cannot participate in proton transfer, and confirm B because Asp at position 12 is the canonical GH43 proton acceptor. This relies on general amino-acid chemistry, sequence-length arithmetic, and GH43 family catalytic-mechanism knowledge learned from other glycoside hydrolases.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> A and D are excluded by the 327-residue sequence length. C is excluded because Proline at position 26 cannot function as a proton donor/acceptor. Only B (Asp-12, proton acceptor) is chemically and family-consistent, leaving no ambiguity.


### Important caveats

- The UniProt annotation for position 12 carries evidence code ECO:0000250 (similarity-based inference from Q45071), not direct experimental validation for this exact protein.
- The full catalytic site of this GH43 enzyme also includes position 228 (proton donor) and position 134 (pKa-modulating site), but the question only asks for one active-site residue and the offered choices do not include 228 or 134.
- Options A and D reference positions far beyond the 327-residue sequence and appear to be distractors drawn from unrelated proteins (e.g., fatty-acid synthase or dehydratase entries).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Three independent lines of transferable reasoning distinguish B from the other choices: (1) Sequence-length elimination: the provided sequence is 327 residues, so positions 2340 (A) and 975 (D) are immediately impossible. (2) Amino-acid chemistry at the candidate positions: position 12 is Asp (D), a canonical proton acceptor in glycoside hydrolases via its carboxylate side chain; position 26 is Pro (P), whose cyclic side chain lacks any ionizable or hydrogen-bonding group and whose backbone amide is locked in the pyrrolidine ring, making it chemically incapable of proton donation/acceptance. (3) GH43 family knowledge: the sequence contains hallmark GH43 motifs (e.g., YFP/YFG/YFSY patterns), and in GH43 β-propeller enzymes the proton acceptor is invariably an Asp or Glu positioned near the N-terminus of the first β-strand, while the proton donor is a second Asp/Glu ~200 residues downstream. Position 12 Asp fits this family-level pattern precisely. Together these arguments uniquely select B without needing to recall this protein's specific database entry.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate A and D by noting they exceed the 327-aa sequence length, eliminate C because Proline at position 26 cannot participate in proton transfer, and confirm B because Asp at position 12 is the canonical GH43 proton acceptor. This relies on general amino-acid chemistry, sequence-length arithmetic, and GH43 family catalytic-mechanism knowledge learned from other glycoside hydrolases."
  },
  "case_id": "active_site_0142",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H3) confirms position 12 as 'Proton acceptor' active site. Position 12 in the 327-aa sequence is D (Aspartate), consistent with the canonical GH43 catalytic mechanism. The annotation evidence code is ECO:0000250 (similarity-based transfer from Q45071), so it is a computational inference rather than direct experimental proof for this exact protein, but it is consistent with well-established GH43 family catalytic chemistry. Options A (position 2340) and D (position 975) exceed the 327-residue sequence length and are physically impossible. Option C (position 26) corresponds to Proline in the sequence, which cannot serve as a proton donor/acceptor."
  },
  "important_caveats": [
    "The UniProt annotation for position 12 carries evidence code ECO:0000250 (similarity-based inference from Q45071), not direct experimental validation for this exact protein.",
    "The full catalytic site of this GH43 enzyme also includes position 228 (proton donor) and position 134 (pKa-modulating site), but the question only asks for one active-site residue and the offered choices do not include 228 or 134.",
    "Options A and D reference positions far beyond the 327-residue sequence and appear to be distractors drawn from unrelated proteins (e.g., fatty-acid synthase or dehydratase entries)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A and D are excluded by the 327-residue sequence length. C is excluded because Proline at position 26 cannot function as a proton donor/acceptor. Only B (Asp-12, proton acceptor) is chemically and family-consistent, leaving no ambiguity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0142",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H3) confirms position 12 as 'Proton acceptor' active site. Position 12 in the 327-aa sequence is D (Aspartate), consistent with the canonical GH43 catalytic mechanism. The annotation evidence code is ECO:0000250 (similarity-based transfer from Q45071), so it is a computational inference rather than direct experimental proof for this exact protein, but it is consistent with well-established GH43 family catalytic chemistry. Options A (position 2340) and D (position 975) exceed the 327-residue sequence length and are physically impossible. Option C (position 26) corresponds to Proline in the sequence, which cannot serve as a proton donor/acceptor.",
    "evidence_ids": ["C5", "H3", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Three independent lines of transferable reasoning distinguish B from the other choices: (1) Sequence-length elimination: the provided sequence is 327 residues, so positions 2340 (A) and 975 (D) are immediately impossible. (2) Amino-acid chemistry at the candidate positions: position 12 is Asp (D), a canonical proton acceptor in glycoside hydrolases via its carboxylate side chain; position 26 is Pro (P), whose cyclic side chain lacks any ionizable or hydrogen-bonding group and whose backbone amide is locked in the pyrrolidine ring, making it chemically incapable of proton donation/acceptance. (3) GH43 family knowledge: the sequence contains hallmark GH43 motifs (e.g., YFP/YFG/YFSY patterns), and in GH43 β-propeller enzymes the proton acceptor is invariably an Asp or Glu positioned near the N-terminus of the first β-strand, while the proton donor is a second Asp/Glu ~200 residues downstream. Position 12 Asp fits this family-level pattern precisely. Together these arguments uniquely select B without needing to recall this protein's specific database entry.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate A and D by noting they exceed the 327-aa sequence length, eliminate C because Proline at position 26 cannot participate in proton transfer, and confirm B because Asp at position 12 is the canonical GH43 proton acceptor. This relies on general amino-acid chemistry, sequence-length arithmetic, and GH43 family catalytic-mechanism knowledge learned from other glycoside hydrolases."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A and D are excluded by the 327-residue sequence length. C is excluded because Proline at position 26 cannot function as a proton donor/acceptor. Only B (Asp-12, proton acceptor) is chemically and family-consistent, leaving no ambiguity."
  },
  "important_caveats": [
    "The UniProt annotation for position 12 carries evidence code ECO:0000250 (similarity-based inference from Q45071), not direct experimental validation for this exact protein.",
    "The full catalytic site of this GH43 enzyme also includes position 228 (proton donor) and position 134 (pKa-modulating site), but the question only asks for one active-site residue and the offered choices do not include 228 or 134.",
    "Options A and D reference positions far beyond the 327-residue sequence and appear to be distractors drawn from unrelated proteins (e.g., fatty-acid synthase or dehydratase entries)."
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
  "benchmark_sequence_length": 327,
  "benchmark_sequence_sha256": "50d3469575943c69659937ec94d1f84b72a59b8d874475defb7b29759a02ee84",
  "current_entry_audit": {
    "entryVersion": 23,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2014-03-19",
    "sequenceVersion": 1
  },
  "current_record_sha256": "4161e2957710d391f76f21ebe451652d828870a93127025ad04961d04b1d3c73",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 327,
  "current_source_sequence_sha256": "50d3469575943c69659937ec94d1f84b72a59b8d874475defb7b29759a02ee84",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 21,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "V9TNS0",
  "selected_historical_entry_version": 21,
  "selected_historical_record_sha256": "9e4bf9e42b116a4202b7fa35da7f1678719e0062361cb3f723d101ecbaf0326f",
  "selected_historical_source_sequence_length": 327,
  "selected_historical_source_sequence_sha256": "50d3469575943c69659937ec94d1f84b72a59b8d874475defb7b29759a02ee84",
  "selected_historical_version": {
    "accession": "V9TNS0",
    "database": "Swiss-Prot",
    "entryVersion": 21,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "XY43A_HUMIN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TNS0.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"V9TNS0\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:29.909204+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4161e2957710d391f76f21ebe451652d828870a93127025ad04961d04b1d3c73",
  "url": "https://rest.uniprot.org/uniprotkb/V9TNS0.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TNS0.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":23,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2014-03-19\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:29.909204+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4161e2957710d391f76f21ebe451652d828870a93127025ad04961d04b1d3c73",
  "url": "https://rest.uniprot.org/uniprotkb/V9TNS0.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TNS0.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Soft-rot fungus\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Sordariomycetidae\",\"Sordariales\",\"Chaetomiaceae\",\"Mycothermus\"],\"scientificName\":\"Humicola insolens\",\"taxonId\":85995}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:29.909204+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4161e2957710d391f76f21ebe451652d828870a93127025ad04961d04b1d3c73",
  "url": "https://rest.uniprot.org/uniprotkb/V9TNS0.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TNS0.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"includes\":[{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24262572\",\"source\":\"PubMed\"}],\"value\":\"1,4-beta-D-xylan xylohydrolase\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24262572\",\"source\":\"PubMed\"}],\"value\":\"Xylan 1,4-beta-xylosidase\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24262572\",\"source\":\"PubMed\"}],\"value\":\"3.2.1.37\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24262572\",\"source\":\"PubMed\"}],\"value\":\"Beta-xylosidase\"}}},{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24262572\",\"source\":\"PubMed\"}],\"value\":\"3.2.1.55\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24262572\",\"source\":\"PubMed\"}],\"value\":\"Alpha-L-arabinofuranosidase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24262572\",\"source\":\"PubMed\"}],\"value\":\"Arabinosidase\"}]}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24262572\",\"source\":\"PubMed\"}],\"value\":\"Xylosidase/arabinosidase 43A\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:29.909204+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4161e2957710d391f76f21ebe451652d828870a93127025ad04961d04b1d3c73",
  "url": "https://rest.uniprot.org/uniprotkb/V9TNS0.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TNS0.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Proton acceptor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q45071\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":12},\"start\":{\"modifier\":\"EXACT\",\"value\":12}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-01T06:25:29.909204+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4161e2957710d391f76f21ebe451652d828870a93127025ad04961d04b1d3c73",
  "url": "https://rest.uniprot.org/uniprotkb/V9TNS0.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TNS0.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Proton donor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q45071\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":228},\"start\":{\"modifier\":\"EXACT\",\"value\":228}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-01T06:25:29.909204+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4161e2957710d391f76f21ebe451652d828870a93127025ad04961d04b1d3c73",
  "url": "https://rest.uniprot.org/uniprotkb/V9TNS0.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TNS0.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Important for catalytic activity, responsible for pKa modulation of the active site Glu and correct orientation of both the proton donor and substrate\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q45071\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":134},\"start\":{\"modifier\":\"EXACT\",\"value\":134}},\"type\":\"Site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-01T06:25:29.909204+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4161e2957710d391f76f21ebe451652d828870a93127025ad04961d04b1d3c73",
  "url": "https://rest.uniprot.org/uniprotkb/V9TNS0.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TNS0.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Yang X.\",\"Shi P.\",\"Huang H.\",\"Luo H.\",\"Wang Y.\",\"Zhang W.\",\"Yao B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"24262572\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.foodchem.2013.10.062\"}],\"citationType\":\"journal article\",\"firstPage\":\"381\",\"id\":\"24262572\",\"journal\":\"Food Chem.\",\"lastPage\":\"387\",\"publicationDate\":\"2014\",\"title\":\"Two xylose-tolerant GH43 bifunctional ?-xylosidase/?-arabinosidases and one GH11 xylanase from Humicola insolens and their synergy in the degradation of xylan.\",\"volume\":\"148\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"Y1\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBSTRATE SPECIFICITY\",\"ACTIVITY REGULATION\",\"SUBCELLULAR LOCATION\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:25:29.909204+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4161e2957710d391f76f21ebe451652d828870a93127025ad04961d04b1d3c73",
  "url": "https://rest.uniprot.org/uniprotkb/V9TNS0.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/V9TNS0?format=txt&versions=21)

```json
{
  "entry_version": 21,
  "evidence_id": "H1",
  "excerpt": "ID   XY43A_HUMIN             Reviewed;         327 AA.\nAC   V9TNS0;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   19-MAR-2014, sequence version 1.\nDT   28-JAN-2026, entry version 21.\nDE   RecName: Full=Xylosidase/arabinosidase 43A {ECO:0000303|PubMed:24262572};\nDE   Includes:\nDE     RecName: Full=Beta-xylosidase {ECO:0000303|PubMed:24262572};\nDE              EC=3.2.1.37 {ECO:0000269|PubMed:24262572};\nDE     AltName: Full=1,4-beta-D-xylan xylohydrolase {ECO:0000303|PubMed:24262572};\nDE     AltName: Full=Xylan 1,4-beta-xylosidase {ECO:0000303|PubMed:24262572};\nDE   Includes:\nDE     RecName: Full=Alpha-L-arabinofuranosidase {ECO:0000303|PubMed:24262572};\nDE              Short=Arabinosidase {ECO:0000303|PubMed:24262572};\nDE              EC=3.2.1.55 {ECO:0000269|PubMed:24262572};\nGN   Name=XylL43A {ECO:0000303|PubMed:24262572};\nOS   Humicola insolens (Soft-rot fungus).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Sordariomycetidae; Sordariales; Chaetomiaceae; Mycothermus.\nOX   NCBI_TaxID=85995;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:51.766326+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-20",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9e4bf9e42b116a4202b7fa35da7f1678719e0062361cb3f723d101ecbaf0326f",
  "url": "https://rest.uniprot.org/unisave/V9TNS0?format=txt&versions=21"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/V9TNS0?format=txt&versions=21)

```json
{
  "entry_version": 21,
  "evidence_id": "H2",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, SUBSTRATE SPECIFICITY, ACTIVITY REGULATION,\nRP   SUBCELLULAR LOCATION, AND BIOTECHNOLOGY.\nRC   STRAIN=Y1;\nRX   PubMed=24262572; DOI=10.1016/j.foodchem.2013.10.062;\nRA   Yang X., Shi P., Huang H., Luo H., Wang Y., Zhang W., Yao B.;\nRT   \"Two xylose-tolerant GH43 bifunctional ?-xylosidase/?-arabinosidases and\nRT   one GH11 xylanase from Humicola insolens and their synergy in the\nRT   degradation of xylan.\";\nRL   Food Chem. 148:381-387(2014).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:51.766326+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 21-31",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9e4bf9e42b116a4202b7fa35da7f1678719e0062361cb3f723d101ecbaf0326f",
  "url": "https://rest.uniprot.org/unisave/V9TNS0?format=txt&versions=21"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/V9TNS0?format=txt&versions=21)

```json
{
  "entry_version": 21,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        12\nFT                   /note=\"Proton acceptor\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q45071\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:51.766326+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 105-107",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9e4bf9e42b116a4202b7fa35da7f1678719e0062361cb3f723d101ecbaf0326f",
  "url": "https://rest.uniprot.org/unisave/V9TNS0?format=txt&versions=21"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/V9TNS0?format=txt&versions=21)

```json
{
  "entry_version": 21,
  "evidence_id": "H4",
  "excerpt": "FT   ACT_SITE        228\nFT                   /note=\"Proton donor\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q45071\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:51.766326+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 108-110",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9e4bf9e42b116a4202b7fa35da7f1678719e0062361cb3f723d101ecbaf0326f",
  "url": "https://rest.uniprot.org/unisave/V9TNS0?format=txt&versions=21"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/V9TNS0?format=txt&versions=21)

```json
{
  "entry_version": 21,
  "evidence_id": "H5",
  "excerpt": "FT   SITE            134\nFT                   /note=\"Important for catalytic activity, responsible for\nFT                   pKa modulation of the active site Glu and correct\nFT                   orientation of both the proton donor and substrate\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q45071\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:51.766326+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 111-115",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9e4bf9e42b116a4202b7fa35da7f1678719e0062361cb3f723d101ecbaf0326f",
  "url": "https://rest.uniprot.org/unisave/V9TNS0?format=txt&versions=21"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 142. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
