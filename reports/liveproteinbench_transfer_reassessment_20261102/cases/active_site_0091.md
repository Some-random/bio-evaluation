# active_site_0091

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0091.txt)

**Task:** `active_site`  
**Expected answer:** **C** — Position 122 (Nucleophile)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MVCFSSLFVAASAIAGVFASPVDHEQLAKRQSTPSSQGTHDGYFYSWWTDGGAAATYTNLAGGEYSVSWSNGGNLVGGKGWNPGSARTITYSGTYNPNGNSYLAVYGWTRNPQPWLTPLVVEYYVVENFGTYNPSSGATARGQVTHDGALYRLFESTRTNQPSIDGTATFQQYWAVRDVKRTGGTVNMATFFNAWTAAGMRLGTHNYQVVATEGYFSSGSARINVAGGGGSTPSPPSTPSPPTTPSPPPVTPPPSGGGSCAARWGQCGGSGWNGATCCSAGTCQAQNQWYSQCL

[Multiple Choices]
A. Position 140 (Charge relay system)
B. Position 200 (Proton acceptor)
C. Position 122 (Nucleophile)
D. Position 381 (For beta-ketoacyl synthase activity)
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

> The supplied sequence matches the source sequence, whose UniProt annotation identifies residue 122 as the nucleophile. The annotation is based on a PROSITE-ProRule computational inference, not direct experimental evidence in the supplied excerpts.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a secretory signal and features consistent with a fungal GH11 xylanase. GH11 xylanases use conserved catalytic glutamates, including a nucleophile; residue 122 is a glutamate in this sequence and is a credible match for that role. This favors C, while position 381 in D is beyond the 294-residue sequence and the other listed positions/roles do not fit the conserved catalytic-residue pattern.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference from the sequence and conserved xylanase catalytic mechanism meaningfully distinguishes the offered choices; recalling this exact protein's database record is not necessary.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, only C provides a plausible catalytic-residue assignment consistent with the sequence and family mechanism.


### Important caveats

- The source annotation is computationally inferred by PROSITE-ProRule; the excerpts do not establish experimental validation of residue 122.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a secretory signal and features consistent with a fungal GH11 xylanase. GH11 xylanases use conserved catalytic glutamates, including a nucleophile; residue 122 is a glutamate in this sequence and is a credible match for that role. This favors C, while position 381 in D is beyond the 294-residue sequence and the other listed positions/roles do not fit the conserved catalytic-residue pattern.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence and conserved xylanase catalytic mechanism meaningfully distinguishes the offered choices; recalling this exact protein's database record is not necessary."
  },
  "case_id": "active_site_0091",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches the source sequence, whose UniProt annotation identifies residue 122 as the nucleophile. The annotation is based on a PROSITE-ProRule computational inference, not direct experimental evidence in the supplied excerpts."
  },
  "important_caveats": [
    "The source annotation is computationally inferred by PROSITE-ProRule; the excerpts do not establish experimental validation of residue 122."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, only C provides a plausible catalytic-residue assignment consistent with the sequence and family mechanism."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0091",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches the source sequence, whose UniProt annotation identifies residue 122 as the nucleophile. The annotation is based on a PROSITE-ProRule computational inference, not direct experimental evidence in the supplied excerpts.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a secretory signal and features consistent with a fungal GH11 xylanase. GH11 xylanases use conserved catalytic glutamates, including a nucleophile; residue 122 is a glutamate in this sequence and is a credible match for that role. This favors C, while position 381 in D is beyond the 294-residue sequence and the other listed positions/roles do not fit the conserved catalytic-residue pattern.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence and conserved xylanase catalytic mechanism meaningfully distinguishes the offered choices; recalling this exact protein's database record is not necessary."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, only C provides a plausible catalytic-residue assignment consistent with the sequence and family mechanism."
  },
  "important_caveats": [
    "The source annotation is computationally inferred by PROSITE-ProRule; the excerpts do not establish experimental validation of residue 122."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for G2X8M4 (EIX3, EC 3.2.1.8, endo-1,4-beta-xylanase) explicitly annotates position 122 as 'Nucleophile' active site with evidence code ECO:0000255|PROSITE-ProRule:PRU01097 (glycoside hydrolase family 11). The sequence at position 122 is Glu (E), consistent with the GH11 catalytic nucleophile. The annotation is computational (PROSITE-ProRule) rather than experimentally validated, but it is well-established for this enzyme family. The reviewer evidence (C5, H3) directly supports the author's key.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Several transferable inferences meaningfully distinguish C from the alternatives. (1) Option D (position 381) is eliminated immediately because the protein is only 294 residues long. (2) Option A ('Charge relay system') uses terminology specific to serine/cysteine proteases (Ser-His-Asp triad), not glycoside hydrolases, making it mechanistically inconsistent with the sequence's family. (3) The sequence contains hallmark GH11 xylanase features: ~294 aa length, the 'TITYSG' motif (~positions 95-100), multiple 'NP' patterns, and a beta-jelly-roll–compatible composition. Family-level knowledge of GH11 establishes that catalysis uses two Glu residues (nucleophile and proton donor) separated by ~90 residues. (4) The conserved GH11 nucleophile Glu appears in a 'VVE' context; positions 120-123 read 'VVEY', placing Glu at 122 in the canonical nucleophile slot. (5) Option B (position 200, 'Proton acceptor') is inconsistent: the GH11 proton donor is typically ~90 residues downstream of the nucleophile (position 213 in this family context), and the standard terminology is 'proton donor,' not 'proton acceptor.' Thus, family recognition plus mechanistic knowledge of GH11 catalysis distinguishes C from the other options without needing the exact database entry for this protein.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model recognizing GH11 family features in the sequence can apply well-established family-level catalytic mechanism knowledge (two Glu nucleophile/proton donor, conserved 'VVE' nucleophile context, ~90-residue spacing) to identify position 122 as the nucleophile. The distractors are eliminated by sequence length (D), wrong mechanism terminology (A), and wrong position/terminology (B). This is a defensible transferable inference from other GH11 enzymes.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option D is physically impossible (position 381 > 294 aa). Option A uses protease-specific terminology inapplicable to glycoside hydrolases. Option B has both a positional mismatch and non-standard terminology. Only C is consistent with GH11 family catalytic mechanism and the sequence context.


### Important caveats

- The UniProt annotation is computational (PROSITE-ProRule PRU01097), not experimentally determined by mutagenesis or crystallography for this specific protein.
- The PROSITE-ProRule assignment is a family-level transfer; it assumes the protein is a true GH11 member with the canonical catalytic Glu pair.
- The reviewer-only evidence (accession, organism, PROSITE rule) was not available to the evaluated model; the reasoning argument relies solely on sequence features and general GH11 family knowledge.
- The entry was only recently integrated into Swiss-Prot (first public date 2025-06-18), so it may not have been in training data at the time of benchmark construction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Several transferable inferences meaningfully distinguish C from the alternatives. (1) Option D (position 381) is eliminated immediately because the protein is only 294 residues long. (2) Option A ('Charge relay system') uses terminology specific to serine/cysteine proteases (Ser-His-Asp triad), not glycoside hydrolases, making it mechanistically inconsistent with the sequence's family. (3) The sequence contains hallmark GH11 xylanase features: ~294 aa length, the 'TITYSG' motif (~positions 95-100), multiple 'NP' patterns, and a beta-jelly-roll–compatible composition. Family-level knowledge of GH11 establishes that catalysis uses two Glu residues (nucleophile and proton donor) separated by ~90 residues. (4) The conserved GH11 nucleophile Glu appears in a 'VVE' context; positions 120-123 read 'VVEY', placing Glu at 122 in the canonical nucleophile slot. (5) Option B (position 200, 'Proton acceptor') is inconsistent: the GH11 proton donor is typically ~90 residues downstream of the nucleophile (position 213 in this family context), and the standard terminology is 'proton donor,' not 'proton acceptor.' Thus, family recognition plus mechanistic knowledge of GH11 catalysis distinguishes C from the other options without needing the exact database entry for this protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model recognizing GH11 family features in the sequence can apply well-established family-level catalytic mechanism knowledge (two Glu nucleophile/proton donor, conserved 'VVE' nucleophile context, ~90-residue spacing) to identify position 122 as the nucleophile. The distractors are eliminated by sequence length (D), wrong mechanism terminology (A), and wrong position/terminology (B). This is a defensible transferable inference from other GH11 enzymes."
  },
  "case_id": "active_site_0091",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for G2X8M4 (EIX3, EC 3.2.1.8, endo-1,4-beta-xylanase) explicitly annotates position 122 as 'Nucleophile' active site with evidence code ECO:0000255|PROSITE-ProRule:PRU01097 (glycoside hydrolase family 11). The sequence at position 122 is Glu (E), consistent with the GH11 catalytic nucleophile. The annotation is computational (PROSITE-ProRule) rather than experimentally validated, but it is well-established for this enzyme family. The reviewer evidence (C5, H3) directly supports the author's key."
  },
  "important_caveats": [
    "The UniProt annotation is computational (PROSITE-ProRule PRU01097), not experimentally determined by mutagenesis or crystallography for this specific protein.",
    "The PROSITE-ProRule assignment is a family-level transfer; it assumes the protein is a true GH11 member with the canonical catalytic Glu pair.",
    "The reviewer-only evidence (accession, organism, PROSITE rule) was not available to the evaluated model; the reasoning argument relies solely on sequence features and general GH11 family knowledge.",
    "The entry was only recently integrated into Swiss-Prot (first public date 2025-06-18), so it may not have been in training data at the time of benchmark construction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option D is physically impossible (position 381 > 294 aa). Option A uses protease-specific terminology inapplicable to glycoside hydrolases. Option B has both a positional mismatch and non-standard terminology. Only C is consistent with GH11 family catalytic mechanism and the sequence context."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0091",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for G2X8M4 (EIX3, EC 3.2.1.8, endo-1,4-beta-xylanase) explicitly annotates position 122 as 'Nucleophile' active site with evidence code ECO:0000255|PROSITE-ProRule:PRU01097 (glycoside hydrolase family 11). The sequence at position 122 is Glu (E), consistent with the GH11 catalytic nucleophile. The annotation is computational (PROSITE-ProRule) rather than experimentally validated, but it is well-established for this enzyme family. The reviewer evidence (C5, H3) directly supports the author's key.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Several transferable inferences meaningfully distinguish C from the alternatives. (1) Option D (position 381) is eliminated immediately because the protein is only 294 residues long. (2) Option A ('Charge relay system') uses terminology specific to serine/cysteine proteases (Ser-His-Asp triad), not glycoside hydrolases, making it mechanistically inconsistent with the sequence's family. (3) The sequence contains hallmark GH11 xylanase features: ~294 aa length, the 'TITYSG' motif (~positions 95-100), multiple 'NP' patterns, and a beta-jelly-roll–compatible composition. Family-level knowledge of GH11 establishes that catalysis uses two Glu residues (nucleophile and proton donor) separated by ~90 residues. (4) The conserved GH11 nucleophile Glu appears in a 'VVE' context; positions 120-123 read 'VVEY', placing Glu at 122 in the canonical nucleophile slot. (5) Option B (position 200, 'Proton acceptor') is inconsistent: the GH11 proton donor is typically ~90 residues downstream of the nucleophile (position 213 in this family context), and the standard terminology is 'proton donor,' not 'proton acceptor.' Thus, family recognition plus mechanistic knowledge of GH11 catalysis distinguishes C from the other options without needing the exact database entry for this protein.",
    "missing_item_specific_fact": "",
    "reason": "A model recognizing GH11 family features in the sequence can apply well-established family-level catalytic mechanism knowledge (two Glu nucleophile/proton donor, conserved 'VVE' nucleophile context, ~90-residue spacing) to identify position 122 as the nucleophile. The distractors are eliminated by sequence length (D), wrong mechanism terminology (A), and wrong position/terminology (B). This is a defensible transferable inference from other GH11 enzymes."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option D is physically impossible (position 381 > 294 aa). Option A uses protease-specific terminology inapplicable to glycoside hydrolases. Option B has both a positional mismatch and non-standard terminology. Only C is consistent with GH11 family catalytic mechanism and the sequence context."
  },
  "important_caveats": [
    "The UniProt annotation is computational (PROSITE-ProRule PRU01097), not experimentally determined by mutagenesis or crystallography for this specific protein.",
    "The PROSITE-ProRule assignment is a family-level transfer; it assumes the protein is a true GH11 member with the canonical catalytic Glu pair.",
    "The reviewer-only evidence (accession, organism, PROSITE rule) was not available to the evaluated model; the reasoning argument relies solely on sequence features and general GH11 family knowledge.",
    "The entry was only recently integrated into Swiss-Prot (first public date 2025-06-18), so it may not have been in training data at the time of benchmark construction."
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
  "benchmark_sequence_length": 294,
  "benchmark_sequence_sha256": "05a8aea7487a61591af456e59bbcc17e903fc702ebebaa05b6c55910156cc92b",
  "current_entry_audit": {
    "entryVersion": 62,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2011-11-16",
    "sequenceVersion": 1
  },
  "current_record_sha256": "0d3245ba74b9e0c578d36f87f7508c596ceb2d25929e23083625cf29ccee1e4b",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 294,
  "current_source_sequence_sha256": "05a8aea7487a61591af456e59bbcc17e903fc702ebebaa05b6c55910156cc92b",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 61,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "G2X8M4",
  "selected_historical_entry_version": 61,
  "selected_historical_record_sha256": "dbdf6ed8a8e0617cac295b004204625338e46a980bf24a819e409ad502cf70e7",
  "selected_historical_source_sequence_length": 294,
  "selected_historical_source_sequence_sha256": "05a8aea7487a61591af456e59bbcc17e903fc702ebebaa05b6c55910156cc92b",
  "selected_historical_version": {
    "accession": "G2X8M4",
    "database": "Swiss-Prot",
    "entryVersion": 61,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "EIX3_VERDV",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X8M4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"G2X8M4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:28:39.111291+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0d3245ba74b9e0c578d36f87f7508c596ceb2d25929e23083625cf29ccee1e4b",
  "url": "https://rest.uniprot.org/uniprotkb/G2X8M4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X8M4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":62,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2011-11-16\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:28:39.111291+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0d3245ba74b9e0c578d36f87f7508c596ceb2d25929e23083625cf29ccee1e4b",
  "url": "https://rest.uniprot.org/uniprotkb/G2X8M4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X8M4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Verticillium wilt\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Hypocreomycetidae\",\"Glomerellales\",\"Plectosphaerellaceae\",\"Verticillium\"],\"scientificName\":\"Verticillium dahliae (strain VdLs.17 / ATCC MYA-4575 / FGSC 10137)\",\"taxonId\":498257}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:28:39.111291+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0d3245ba74b9e0c578d36f87f7508c596ceb2d25929e23083625cf29ccee1e4b",
  "url": "https://rest.uniprot.org/uniprotkb/G2X8M4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X8M4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33205907\",\"source\":\"PubMed\"}],\"value\":\"Endo-1,4-beta-xylanase EIX3\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01097\",\"source\":\"PROSITE-ProRule\"}],\"value\":\"3.2.1.8\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33205907\",\"source\":\"PubMed\"}],\"value\":\"Ethylene-inducing xylanase 3\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33205907\",\"source\":\"PubMed\"}],\"value\":\"EIX3\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:28:39.111291+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0d3245ba74b9e0c578d36f87f7508c596ceb2d25929e23083625cf29ccee1e4b",
  "url": "https://rest.uniprot.org/uniprotkb/G2X8M4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X8M4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Nucleophile\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01097\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":122},\"start\":{\"modifier\":\"EXACT\",\"value\":122}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:28:39.111291+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0d3245ba74b9e0c578d36f87f7508c596ceb2d25929e23083625cf29ccee1e4b",
  "url": "https://rest.uniprot.org/uniprotkb/G2X8M4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X8M4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Proton donor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01097\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":213},\"start\":{\"modifier\":\"EXACT\",\"value\":213}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:28:39.111291+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0d3245ba74b9e0c578d36f87f7508c596ceb2d25929e23083625cf29ccee1e4b",
  "url": "https://rest.uniprot.org/uniprotkb/G2X8M4.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X8M4.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Yin Z.\",\"Wang N.\",\"Pi L.\",\"Li L.\",\"Duan W.\",\"Wang X.\",\"Dou D.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33205907\"},{\"database\":\"DOI\",\"id\":\"10.1111/jipb.13031\"}],\"citationType\":\"journal article\",\"firstPage\":\"949\",\"id\":\"33205907\",\"journal\":\"J. Integr. Plant Biol.\",\"lastPage\":\"960\",\"publicationDate\":\"2021\",\"title\":\"Nicotiana benthamiana LRR-RLP NbEIX2 mediates the perception of an EIX-like protein from Verticillium dahliae.\",\"volume\":\"63\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:28:39.111291+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0d3245ba74b9e0c578d36f87f7508c596ceb2d25929e23083625cf29ccee1e4b",
  "url": "https://rest.uniprot.org/uniprotkb/G2X8M4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X8M4?format=txt&versions=61)

```json
{
  "entry_version": 61,
  "evidence_id": "H1",
  "excerpt": "ID   EIX3_VERDV              Reviewed;         294 AA.\nAC   G2X8M4;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   16-NOV-2011, sequence version 1.\nDT   28-JAN-2026, entry version 61.\nDE   RecName: Full=Ethylene-inducing xylanase 3 {ECO:0000303|PubMed:33205907};\nDE            Short=EIX3 {ECO:0000303|PubMed:33205907};\nDE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};\nDE   AltName: Full=Endo-1,4-beta-xylanase EIX3 {ECO:0000303|PubMed:33205907};\nDE   Flags: Precursor;\nGN   Name=EIX3 {ECO:0000303|PubMed:33205907}; ORFNames=VDAG_06165;\nOS   Verticillium dahliae (strain VdLs.17 / ATCC MYA-4575 / FGSC 10137)\nOS   (Verticillium wilt).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Hypocreomycetidae; Glomerellales; Plectosphaerellaceae; Verticillium.\nOX   NCBI_TaxID=498257;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:41.833412+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dbdf6ed8a8e0617cac295b004204625338e46a980bf24a819e409ad502cf70e7",
  "url": "https://rest.uniprot.org/unisave/G2X8M4?format=txt&versions=61"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X8M4?format=txt&versions=61)

```json
{
  "entry_version": 61,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION.\nRX   PubMed=33205907; DOI=10.1111/jipb.13031;\nRA   Yin Z., Wang N., Pi L., Li L., Duan W., Wang X., Dou D.;\nRT   \"Nicotiana benthamiana LRR-RLP NbEIX2 mediates the perception of an EIX-\nRT   like protein from Verticillium dahliae.\";\nRL   J. Integr. Plant Biol. 63:949-960(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:41.833412+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 30-36",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dbdf6ed8a8e0617cac295b004204625338e46a980bf24a819e409ad502cf70e7",
  "url": "https://rest.uniprot.org/unisave/G2X8M4?format=txt&versions=61"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X8M4?format=txt&versions=61)

```json
{
  "entry_version": 61,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        122\nFT                   /note=\"Nucleophile\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01097\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:41.833412+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 117-119",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dbdf6ed8a8e0617cac295b004204625338e46a980bf24a819e409ad502cf70e7",
  "url": "https://rest.uniprot.org/unisave/G2X8M4?format=txt&versions=61"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X8M4?format=txt&versions=61)

```json
{
  "entry_version": 61,
  "evidence_id": "H4",
  "excerpt": "FT   ACT_SITE        213\nFT                   /note=\"Proton donor\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01097\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:41.833412+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 120-122",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "dbdf6ed8a8e0617cac295b004204625338e46a980bf24a819e409ad502cf70e7",
  "url": "https://rest.uniprot.org/unisave/G2X8M4?format=txt&versions=61"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 91. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
