# active_site_0033

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0033.txt)

**Task:** `active_site`  
**Expected answer:** **C** — Position 176 (Proton donor)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MDNSSRLFSPLRLGKCQLRHRVAMSPLTRFRADDLSVQMPFAKEYYAQRASVPGTFLVSEATSISRESVGFSNVPGIWNAEQVRAWKEIADDVHCKGSFLFLQLWATGRSATPERLQSGDFDFASSSAVPMEPGGAVPRELTEEDIHDLIARFAEAARRAIDAGMDGIELHAANGYLIDQFTQASCNQRTDRWGGSIENRARFAIEVTRSVVAAVGADRVGVKLSPWGKIQGMGTMQDLVPQFQYLVSELRDMGLAYLRLSNSRWIDGVPQEEEDNSIYVHTWGASRPVLLEGGYDPISAQKEADIRFNGYDAVIAFGRFFISNPDLPFRIKAGVDLQKYNRDTFYTPISEKGYIDYPFSTAFLEEHSSKASLKL

[Multiple Choices]
A. Position 8 (Nucleophile)
B. Position 959 (Proton acceptor; for dehydratase activity)
C. Position 176 (Proton donor)
D. Position 17 (Proton acceptor)
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

> The exact-sequence-matched UniProt record annotates residue 176 as a proton donor. The annotation is transferred by similarity from another UniProt entry (ECO:0000250), so it supports the key but is not direct experimental evidence for this protein.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Position 176 is Tyr in the supplied sequence. The sequence is consistent with an OYE-like flavin-dependent enzyme, in which a conserved active-site Tyr can donate a proton; that family-level pattern makes C a meaningful choice. The other options are weaker: position 959 is beyond the 375-residue sequence, position 8 is Phe, and position 17 is Gln, not a typical catalytic proton acceptor in this enzyme-family context.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A transferable family-level catalytic pattern, combined with the residue identities and sequence length, meaningfully distinguishes C without needing the target's database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered options, C is the only plausible match to the catalytic proton-donor role.


### Important caveats

- The supporting database annotation is similarity-based rather than direct experimental evidence for this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Position 176 is Tyr in the supplied sequence. The sequence is consistent with an OYE-like flavin-dependent enzyme, in which a conserved active-site Tyr can donate a proton; that family-level pattern makes C a meaningful choice. The other options are weaker: position 959 is beyond the 375-residue sequence, position 8 is Phe, and position 17 is Gln, not a typical catalytic proton acceptor in this enzyme-family context.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A transferable family-level catalytic pattern, combined with the residue identities and sequence length, meaningfully distinguishes C without needing the target's database record."
  },
  "case_id": "active_site_0033",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact-sequence-matched UniProt record annotates residue 176 as a proton donor. The annotation is transferred by similarity from another UniProt entry (ECO:0000250), so it supports the key but is not direct experimental evidence for this protein."
  },
  "important_caveats": [
    "The supporting database annotation is similarity-based rather than direct experimental evidence for this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered options, C is the only plausible match to the catalytic proton-donor role."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0033",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact-sequence-matched UniProt record annotates residue 176 as a proton donor. The annotation is transferred by similarity from another UniProt entry (ECO:0000250), so it supports the key but is not direct experimental evidence for this protein.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Position 176 is Tyr in the supplied sequence. The sequence is consistent with an OYE-like flavin-dependent enzyme, in which a conserved active-site Tyr can donate a proton; that family-level pattern makes C a meaningful choice. The other options are weaker: position 959 is beyond the 375-residue sequence, position 8 is Phe, and position 17 is Gln, not a typical catalytic proton acceptor in this enzyme-family context.",
    "missing_item_specific_fact": "",
    "reason": "A transferable family-level catalytic pattern, combined with the residue identities and sequence length, meaningfully distinguishes C without needing the target's database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered options, C is the only plausible match to the catalytic proton-donor role."
  },
  "important_caveats": [
    "The supporting database annotation is similarity-based rather than direct experimental evidence for this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (evidence C5/H3) records position 176 as ACT_SITE with description 'Proton donor', matching the author's expected answer. The evidence code is ECO:0000250 (inferred by similarity to Q4WZ70, an NTR/OYE-family enzyme), so this is a computational/similarity-based annotation rather than direct experimental evidence for this specific protein. However, the conserved tyrosine as proton donor is well-established in the OYE family mechanism. Position 176 in the supplied sequence is indeed Y (Tyrosine), consistent with the annotation.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model can eliminate three of four options using general biochemistry and family-level pattern recognition. (1) Position 959 is impossible: the sequence is only 375 residues. (2) Position 8 is F (Phenylalanine), which has no nucleophilic side chain (no heteroatom, no lone pair for nucleophilic attack); this is eliminated for any enzyme. (3) Position 17 is Q (Glutamine), whose amide side chain is not a recognized catalytic proton acceptor in oxidoreductases. (4) The C-terminal region (~positions 140–375) contains the classic FMN-binding Rossmann-fold motifs of the OYE/NTR family: 'GADRVGVK' (positions ~215–222), 'GKIQGMGTMQDLVPQFQYLVSELRDMGLAYLRLSNSRWIDGVPQEEEDNSIYVHTWGASRPVLLEGGY' — patterns shared with yeast OYE1, NTR (Q4WZ70), and other flavin-dependent enoate reductases. In the OYE family, the catalytic mechanism requires FMN plus a conserved tyrosine acting as the proton donor to the substrate. Position 176 is Y (Tyrosine), fitting this conserved role. Thus family-level recognition of the FMN-binding domain plus knowledge of the OYE catalytic mechanism distinguishes C from the other options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The FMN-binding domain motifs (GADRVGVK, GKIQGMGTMQDLVPQFQYLVSELRDMGLAYLRLSNSRWIDGVPQEEEDNSIYVHTWGASRPVLLEGGY) are recognizable family-level sequence features shared across OYE/NTR proteins. Knowledge that the OYE family uses a conserved tyrosine as proton donor is transferable from well-studied members (yeast OYE1 Tyr196, NTR Tyr). Combined with elimination of the other three options (impossible position, non-nucleophilic F, non-proton-accepting Q), this provides a concrete and credible inference chain to select C.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A (F as nucleophile), B (position 959, nonexistent), and D (Q as proton acceptor) are each clearly incompatible with basic biochemistry or the sequence length. Only C (Y176 as proton donor) is consistent with both the residue chemistry and the OYE-family mechanism. No ambiguity among the offered choices.


### Important caveats

- The UniProt annotation for position 176 uses evidence code ECO:0000250 (inferred by similarity to Q4WZ70), not direct experimental evidence for this specific protein. The proton donor role is well-supported at the family level but is a transferred annotation for FrzD specifically.
- The protein is annotated as 'Aldehyde reductase FrzD' / 'Flavin-dependent OYE' with EC 1.3.1.-, consistent with the OYE-family assignment used in the reasoning.
- The reviewer-only evidence (UniProt accession, organism, annotation details) was not available to the evaluated model; the reasoning relies solely on sequence motifs and family-level knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can eliminate three of four options using general biochemistry and family-level pattern recognition. (1) Position 959 is impossible: the sequence is only 375 residues. (2) Position 8 is F (Phenylalanine), which has no nucleophilic side chain (no heteroatom, no lone pair for nucleophilic attack); this is eliminated for any enzyme. (3) Position 17 is Q (Glutamine), whose amide side chain is not a recognized catalytic proton acceptor in oxidoreductases. (4) The C-terminal region (~positions 140–375) contains the classic FMN-binding Rossmann-fold motifs of the OYE/NTR family: 'GADRVGVK' (positions ~215–222), 'GKIQGMGTMQDLVPQFQYLVSELRDMGLAYLRLSNSRWIDGVPQEEEDNSIYVHTWGASRPVLLEGGY' — patterns shared with yeast OYE1, NTR (Q4WZ70), and other flavin-dependent enoate reductases. In the OYE family, the catalytic mechanism requires FMN plus a conserved tyrosine acting as the proton donor to the substrate. Position 176 is Y (Tyrosine), fitting this conserved role. Thus family-level recognition of the FMN-binding domain plus knowledge of the OYE catalytic mechanism distinguishes C from the other options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The FMN-binding domain motifs (GADRVGVK, GKIQGMGTMQDLVPQFQYLVSELRDMGLAYLRLSNSRWIDGVPQEEEDNSIYVHTWGASRPVLLEGGY) are recognizable family-level sequence features shared across OYE/NTR proteins. Knowledge that the OYE family uses a conserved tyrosine as proton donor is transferable from well-studied members (yeast OYE1 Tyr196, NTR Tyr). Combined with elimination of the other three options (impossible position, non-nucleophilic F, non-proton-accepting Q), this provides a concrete and credible inference chain to select C."
  },
  "case_id": "active_site_0033",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C5/H3) records position 176 as ACT_SITE with description 'Proton donor', matching the author's expected answer. The evidence code is ECO:0000250 (inferred by similarity to Q4WZ70, an NTR/OYE-family enzyme), so this is a computational/similarity-based annotation rather than direct experimental evidence for this specific protein. However, the conserved tyrosine as proton donor is well-established in the OYE family mechanism. Position 176 in the supplied sequence is indeed Y (Tyrosine), consistent with the annotation."
  },
  "important_caveats": [
    "The UniProt annotation for position 176 uses evidence code ECO:0000250 (inferred by similarity to Q4WZ70), not direct experimental evidence for this specific protein. The proton donor role is well-supported at the family level but is a transferred annotation for FrzD specifically.",
    "The protein is annotated as 'Aldehyde reductase FrzD' / 'Flavin-dependent OYE' with EC 1.3.1.-, consistent with the OYE-family assignment used in the reasoning.",
    "The reviewer-only evidence (UniProt accession, organism, annotation details) was not available to the evaluated model; the reasoning relies solely on sequence motifs and family-level knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A (F as nucleophile), B (position 959, nonexistent), and D (Q as proton acceptor) are each clearly incompatible with basic biochemistry or the sequence length. Only C (Y176 as proton donor) is consistent with both the residue chemistry and the OYE-family mechanism. No ambiguity among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0033",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C5/H3) records position 176 as ACT_SITE with description 'Proton donor', matching the author's expected answer. The evidence code is ECO:0000250 (inferred by similarity to Q4WZ70, an NTR/OYE-family enzyme), so this is a computational/similarity-based annotation rather than direct experimental evidence for this specific protein. However, the conserved tyrosine as proton donor is well-established in the OYE family mechanism. Position 176 in the supplied sequence is indeed Y (Tyrosine), consistent with the annotation.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model can eliminate three of four options using general biochemistry and family-level pattern recognition. (1) Position 959 is impossible: the sequence is only 375 residues. (2) Position 8 is F (Phenylalanine), which has no nucleophilic side chain (no heteroatom, no lone pair for nucleophilic attack); this is eliminated for any enzyme. (3) Position 17 is Q (Glutamine), whose amide side chain is not a recognized catalytic proton acceptor in oxidoreductases. (4) The C-terminal region (~positions 140–375) contains the classic FMN-binding Rossmann-fold motifs of the OYE/NTR family: 'GADRVGVK' (positions ~215–222), 'GKIQGMGTMQDLVPQFQYLVSELRDMGLAYLRLSNSRWIDGVPQEEEDNSIYVHTWGASRPVLLEGGY' — patterns shared with yeast OYE1, NTR (Q4WZ70), and other flavin-dependent enoate reductases. In the OYE family, the catalytic mechanism requires FMN plus a conserved tyrosine acting as the proton donor to the substrate. Position 176 is Y (Tyrosine), fitting this conserved role. Thus family-level recognition of the FMN-binding domain plus knowledge of the OYE catalytic mechanism distinguishes C from the other options.",
    "missing_item_specific_fact": "",
    "reason": "The FMN-binding domain motifs (GADRVGVK, GKIQGMGTMQDLVPQFQYLVSELRDMGLAYLRLSNSRWIDGVPQEEEDNSIYVHTWGASRPVLLEGGY) are recognizable family-level sequence features shared across OYE/NTR proteins. Knowledge that the OYE family uses a conserved tyrosine as proton donor is transferable from well-studied members (yeast OYE1 Tyr196, NTR Tyr). Combined with elimination of the other three options (impossible position, non-nucleophilic F, non-proton-accepting Q), this provides a concrete and credible inference chain to select C."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A (F as nucleophile), B (position 959, nonexistent), and D (Q as proton acceptor) are each clearly incompatible with basic biochemistry or the sequence length. Only C (Y176 as proton donor) is consistent with both the residue chemistry and the OYE-family mechanism. No ambiguity among the offered choices."
  },
  "important_caveats": [
    "The UniProt annotation for position 176 uses evidence code ECO:0000250 (inferred by similarity to Q4WZ70), not direct experimental evidence for this specific protein. The proton donor role is well-supported at the family level but is a transferred annotation for FrzD specifically.",
    "The protein is annotated as 'Aldehyde reductase FrzD' / 'Flavin-dependent OYE' with EC 1.3.1.-, consistent with the OYE-family assignment used in the reasoning.",
    "The reviewer-only evidence (UniProt accession, organism, annotation details) was not available to the evaluated model; the reasoning relies solely on sequence motifs and family-level knowledge."
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
  "benchmark_sequence_length": 375,
  "benchmark_sequence_sha256": "48d35685f95428a133d889977d9437954326f248d7bbb25058ab859a2c365157",
  "current_entry_audit": {
    "entryVersion": 13,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2021-06-02",
    "sequenceVersion": 1
  },
  "current_record_sha256": "c38628844912ac2c4aa489f4067b5327e7aad3e6384ffb308551b50b6f0b30ee",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 375,
  "current_source_sequence_sha256": "48d35685f95428a133d889977d9437954326f248d7bbb25058ab859a2c365157",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 11,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A7T8F1M9",
  "selected_historical_entry_version": 11,
  "selected_historical_record_sha256": "fd48d108f45a92963462c2f0a750dcecfac5cc36c43941b4ca5d31b971333839",
  "selected_historical_source_sequence_length": 375,
  "selected_historical_source_sequence_sha256": "48d35685f95428a133d889977d9437954326f248d7bbb25058ab859a2c365157",
  "selected_historical_version": {
    "accession": "A0A7T8F1M9",
    "database": "Swiss-Prot",
    "entryVersion": 11,
    "firstRelease": "2025_03/2025_03",
    "firstReleaseDate": "18-Jun-2025",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "FRZD_CLASX",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1M9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A7T8F1M9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:51.159757+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c38628844912ac2c4aa489f4067b5327e7aad3e6384ffb308551b50b6f0b30ee",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1M9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1M9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":13,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2021-06-02\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:51.159757+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c38628844912ac2c4aa489f4067b5327e7aad3e6384ffb308551b50b6f0b30ee",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1M9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1M9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Hypocreomycetidae\",\"Hypocreales\",\"Hypocreaceae\",\"Cladobotryum\"],\"scientificName\":\"Cladobotryum sp\",\"taxonId\":2040732}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:51.159757+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c38628844912ac2c4aa489f4067b5327e7aad3e6384ffb308551b50b6f0b30ee",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1M9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1M9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"FR901483 biosynthesis cluster protein D\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"Flavin-dependent old-yellow enzyme FrzD\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"Flavin-dependent OYE\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"1.3.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"Aldehyde reductase FrzD\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:51.159757+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c38628844912ac2c4aa489f4067b5327e7aad3e6384ffb308551b50b6f0b30ee",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1M9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1M9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Proton donor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q4WZ70\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":176},\"start\":{\"modifier\":\"EXACT\",\"value\":176}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-01T06:24:51.159757+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c38628844912ac2c4aa489f4067b5327e7aad3e6384ffb308551b50b6f0b30ee",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1M9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1M9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q4WZ70\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58210\",\"name\":\"FMN\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":61},\"start\":{\"modifier\":\"EXACT\",\"value\":61}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-01T06:24:51.159757+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c38628844912ac2c4aa489f4067b5327e7aad3e6384ffb308551b50b6f0b30ee",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1M9.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1M9.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q4WZ70\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58210\",\"name\":\"FMN\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":103},\"start\":{\"modifier\":\"EXACT\",\"value\":103}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-01T06:24:51.159757+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c38628844912ac2c4aa489f4067b5327e7aad3e6384ffb308551b50b6f0b30ee",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1M9.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1M9.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q4WZ70\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58210\",\"name\":\"FMN\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":171},\"start\":{\"modifier\":\"EXACT\",\"value\":171}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-01T06:24:51.159757+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c38628844912ac2c4aa489f4067b5327e7aad3e6384ffb308551b50b6f0b30ee",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1M9.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1M9.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q4WZ70\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58210\",\"name\":\"FMN\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":223},\"start\":{\"modifier\":\"EXACT\",\"value\":223}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-01T06:24:51.159757+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c38628844912ac2c4aa489f4067b5327e7aad3e6384ffb308551b50b6f0b30ee",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1M9.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1M9.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q4WZ70\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58210\",\"name\":\"FMN\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":294},\"start\":{\"modifier\":\"EXACT\",\"value\":294}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-01T06:24:51.159757+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c38628844912ac2c4aa489f4067b5327e7aad3e6384ffb308551b50b6f0b30ee",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1M9.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1M9.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q02899\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58210\",\"name\":\"FMN\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":319},\"start\":{\"modifier\":\"EXACT\",\"value\":319}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-01T06:24:51.159757+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c38628844912ac2c4aa489f4067b5327e7aad3e6384ffb308551b50b6f0b30ee",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1M9.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1M9.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhang Z.\",\"Tamura Y.\",\"Tang M.\",\"Qiao T.\",\"Sato M.\",\"Otsu Y.\",\"Sasamura S.\",\"Taniguchi M.\",\"Watanabe K.\",\"Tang Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33372776\"},{\"database\":\"DOI\",\"id\":\"10.1021/jacs.0c12352\"}],\"citationType\":\"journal article\",\"firstPage\":\"132\",\"id\":\"33372776\",\"journal\":\"J. Am. Chem. Soc.\",\"lastPage\":\"136\",\"publicationDate\":\"2021\",\"title\":\"Biosynthesis of the Immunosuppressant (-)-FR901483.\",\"volume\":\"143\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"11231\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:24:51.159757+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c38628844912ac2c4aa489f4067b5327e7aad3e6384ffb308551b50b6f0b30ee",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1M9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1M9?format=txt&versions=11)

```json
{
  "entry_version": 11,
  "evidence_id": "H1",
  "excerpt": "ID   FRZD_CLASX              Reviewed;         375 AA.\nAC   A0A7T8F1M9;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   02-JUN-2021, sequence version 1.\nDT   18-JUN-2025, entry version 11.\nDE   RecName: Full=Aldehyde reductase FrzD {ECO:0000303|PubMed:33372776};\nDE            EC=1.3.1.- {ECO:0000269|PubMed:33372776};\nDE   AltName: Full=FR901483 biosynthesis cluster protein D {ECO:0000303|PubMed:33372776};\nDE   AltName: Full=Flavin-dependent old-yellow enzyme FrzD {ECO:0000303|PubMed:33372776};\nDE            Short=Flavin-dependent OYE {ECO:0000303|PubMed:33372776};\nGN   Name=FrzD {ECO:0000303|PubMed:33372776};\nOS   Cladobotryum sp.\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Hypocreomycetidae; Hypocreales; Hypocreaceae; Cladobotryum.\nOX   NCBI_TaxID=2040732;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:35.126419+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fd48d108f45a92963462c2f0a750dcecfac5cc36c43941b4ca5d31b971333839",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1M9?format=txt&versions=11"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1M9?format=txt&versions=11)

```json
{
  "entry_version": 11,
  "evidence_id": "H2",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, CATALYTIC ACTIVITY, AND\nRP   PATHWAY.\nRC   STRAIN=11231;\nRX   PubMed=33372776; DOI=10.1021/jacs.0c12352;\nRA   Zhang Z., Tamura Y., Tang M., Qiao T., Sato M., Otsu Y., Sasamura S.,\nRA   Taniguchi M., Watanabe K., Tang Y.;\nRT   \"Biosynthesis of the Immunosuppressant (-)-FR901483.\";\nRL   J. Am. Chem. Soc. 143:132-136(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:35.126419+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 16-24",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fd48d108f45a92963462c2f0a750dcecfac5cc36c43941b4ca5d31b971333839",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1M9?format=txt&versions=11"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1M9?format=txt&versions=11)

```json
{
  "entry_version": 11,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        176\nFT                   /note=\"Proton donor\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q4WZ70\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:35.126419+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 97-99",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fd48d108f45a92963462c2f0a750dcecfac5cc36c43941b4ca5d31b971333839",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1M9?format=txt&versions=11"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1M9?format=txt&versions=11)

```json
{
  "entry_version": 11,
  "evidence_id": "H4",
  "excerpt": "FT   BINDING         61\nFT                   /ligand=\"FMN\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58210\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q4WZ70\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:35.126419+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 100-103",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fd48d108f45a92963462c2f0a750dcecfac5cc36c43941b4ca5d31b971333839",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1M9?format=txt&versions=11"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1M9?format=txt&versions=11)

```json
{
  "entry_version": 11,
  "evidence_id": "H5",
  "excerpt": "FT   BINDING         103\nFT                   /ligand=\"FMN\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58210\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q4WZ70\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:35.126419+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 104-107",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fd48d108f45a92963462c2f0a750dcecfac5cc36c43941b4ca5d31b971333839",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1M9?format=txt&versions=11"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1M9?format=txt&versions=11)

```json
{
  "entry_version": 11,
  "evidence_id": "H6",
  "excerpt": "FT   BINDING         171\nFT                   /ligand=\"FMN\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58210\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q4WZ70\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:35.126419+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 108-111",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fd48d108f45a92963462c2f0a750dcecfac5cc36c43941b4ca5d31b971333839",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1M9?format=txt&versions=11"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1M9?format=txt&versions=11)

```json
{
  "entry_version": 11,
  "evidence_id": "H7",
  "excerpt": "FT   BINDING         223\nFT                   /ligand=\"FMN\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58210\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q4WZ70\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:35.126419+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 112-115",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fd48d108f45a92963462c2f0a750dcecfac5cc36c43941b4ca5d31b971333839",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1M9?format=txt&versions=11"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1M9?format=txt&versions=11)

```json
{
  "entry_version": 11,
  "evidence_id": "H8",
  "excerpt": "FT   BINDING         294\nFT                   /ligand=\"FMN\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58210\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q4WZ70\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:35.126419+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 116-119",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fd48d108f45a92963462c2f0a750dcecfac5cc36c43941b4ca5d31b971333839",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1M9?format=txt&versions=11"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1M9?format=txt&versions=11)

```json
{
  "entry_version": 11,
  "evidence_id": "H9",
  "excerpt": "FT   BINDING         319\nFT                   /ligand=\"FMN\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58210\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q02899\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:35.126419+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 120-123",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fd48d108f45a92963462c2f0a750dcecfac5cc36c43941b4ca5d31b971333839",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1M9?format=txt&versions=11"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 33. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
