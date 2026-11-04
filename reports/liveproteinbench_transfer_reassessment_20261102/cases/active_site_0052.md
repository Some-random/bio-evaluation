# active_site_0052

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0052.txt)

**Task:** `active_site`  
**Expected answer:** **A** — Position 27 (Proton acceptor)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MGSNTEATEIPKMPLKIVFLTLPIAGHMLHIVDTASTFAIHGVECTIITTPANVPFIEKSISATNTTIRQFLSIRLVDFPHEAVGLPPGVENFSAVTCPDMRPKISKGLSIIQKPTEDLIKEISPDCIVSDMFYPWTSDFALEIGVPRVVFRGCGMFPMCCWHSIKSHLPHEKVDRDDEMIVLPTLPDHIEMRKSTLPDWVRKPTGYSYLMKMIDAAELKSYGVIVNSFSDLERDYEEYFKNVTGLKVWTVGPISLHVGRNEELEGSDEWVKWLDGKKLDSVIYVSFGGVAKFPPHQLREIAAGLESSGHDFVWVVRASDENGDQAEADEWSLQKFKEKMKKTNHGLVIESWVPQLMFLEHKAIGGMLTHVGWGTMLEGITAGLPLVTWPLYAEQFYNERLVVDVLKIGVGVGVKEFCGLDDIGKKETIGRENIEASVRLVMGDGEEAAAMRLRVKELSEASMKAVREGGSSKANIHDFLNELSTLRSLRQA

[Multiple Choices]
A. Position 27 (Proton acceptor)
B. Position 693 (For beta-ketoacyl synthase activity)
C. Position 327 (Proton acceptor)
D. Position 256 (Proton acceptor)
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

> The sequence-matched UniProt annotation identifies position 27 as a proton acceptor. This is a homology-based annotation, not direct experimental evidence for this exact protein, but it supports the expected answer.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a plant family-1 UDP-glycosyltransferase, including its C-terminal donor-binding signature. In this family, a conserved N-terminal histidine acts as the catalytic proton acceptor; position 27 is His in the supplied sequence. That transferable family-level pattern distinguishes A from the other listed positions and from the beta-ketoacyl synthase distractor.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The family-level catalytic-residue pattern provides a meaningful basis for choosing the listed position without recalling this exact protein's annotation. It supports a prediction, though not direct proof of this protein's activity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although several choices use the label “proton acceptor,” the family-level conserved catalytic histidine pattern supports position 27 among the offered positions.


### Important caveats

- The source annotation is transferred by similarity (ECO:0000250); it is not evidence of direct experimental verification for this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a plant family-1 UDP-glycosyltransferase, including its C-terminal donor-binding signature. In this family, a conserved N-terminal histidine acts as the catalytic proton acceptor; position 27 is His in the supplied sequence. That transferable family-level pattern distinguishes A from the other listed positions and from the beta-ketoacyl synthase distractor.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The family-level catalytic-residue pattern provides a meaningful basis for choosing the listed position without recalling this exact protein's annotation. It supports a prediction, though not direct proof of this protein's activity."
  },
  "case_id": "active_site_0052",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies position 27 as a proton acceptor. This is a homology-based annotation, not direct experimental evidence for this exact protein, but it supports the expected answer."
  },
  "important_caveats": [
    "The source annotation is transferred by similarity (ECO:0000250); it is not evidence of direct experimental verification for this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although several choices use the label “proton acceptor,” the family-level conserved catalytic histidine pattern supports position 27 among the offered positions."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0052",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies position 27 as a proton acceptor. This is a homology-based annotation, not direct experimental evidence for this exact protein, but it supports the expected answer.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a plant family-1 UDP-glycosyltransferase, including its C-terminal donor-binding signature. In this family, a conserved N-terminal histidine acts as the catalytic proton acceptor; position 27 is His in the supplied sequence. That transferable family-level pattern distinguishes A from the other listed positions and from the beta-ketoacyl synthase distractor.",
    "missing_item_specific_fact": "",
    "reason": "The family-level catalytic-residue pattern provides a meaningful basis for choosing the listed position without recalling this exact protein's annotation. It supports a prediction, though not direct proof of this protein's activity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although several choices use the label “proton acceptor,” the family-level conserved catalytic histidine pattern supports position 27 among the offered positions."
  },
  "important_caveats": [
    "The source annotation is transferred by similarity (ECO:0000250); it is not evidence of direct experimental verification for this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (C5/H3) records an Active site at position 27 described as 'Proton acceptor,' with evidence code ECO:0000250 (by similarity, transferred from A0A0A1HA03). The residue at position 27 in the supplied 492-aa sequence is indeed Histidine (H), consistent with the well-characterized UGT catalytic mechanism in which a conserved N-terminal His acts as a general base to deprotonate the substrate hydroxyl. The annotation is computational (by similarity), not experimental, but it is the recorded database fact. A second active-site annotation at position 131 is labeled 'Charge relay' (C6/H4), consistent with the UGT His-Asp catalytic dyad. The expected answer matches the annotation.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein is 492 residues long, immediately eliminating option B (position 693 does not exist). The sequence length (~450–500 aa), N-terminal hydrophobic character, and overall composition are consistent with a plant UDP-glycosyltransferase (UGT). From knowledge of many other UGTs (e.g., human UGT1A/2B, plant UGT72/UGT74 families), the catalytic mechanism uses a conserved Histidine in the N-terminal Rossmann-like domain as a proton acceptor (general base), typically at positions ~25–35, while the C-terminal domain harbors the PSPG/UDP-sugar-binding region. Position 27 is H and falls squarely in this N-terminal catalytic window. Positions 327 and 256 lie in the C-terminal or linker regions, which in UGTs are associated with UDP-sugar binding, not proton abstraction. Thus, family-level knowledge of UGT domain architecture and catalytic residue positioning meaningfully distinguishes A from C and D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model familiar with the UGT superfamily can apply the well-established rule that the catalytic proton-acceptor His resides in the N-terminal Rossmann-like domain around residues 25–35, learned from structural and mutagenesis studies of numerous other UGTs. This family-level inference, combined with the elimination of B (impossible position) and the domain-architecture argument against C and D, provides a credible transferable basis for selecting A without needing this protein's specific database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option B is trivially eliminated (position 693 exceeds the 492-aa sequence). Among A, C, and D, the UGT family knowledge about the N-terminal location of the catalytic His cleanly distinguishes A. The 'proton acceptor' label in all three remaining choices does not create ambiguity because only one position can be the general base in the UGT catalytic dyad, and its N-terminal location is a conserved family feature.


### Important caveats

- The UniProt annotation for position 27 is by similarity (ECO:0000250), transferred from A0A0A1HA03, not directly experimentally validated for this specific protein.
- A canonical PSPG motif is not readily identifiable in the supplied sequence, which could make UGT family identification from sequence alone less straightforward for some models; however, size, N-terminal Rossmann-like character, and the choice context (proton acceptor vs. beta-ketoacyl synthase) provide supplementary cues.
- The exact position of the catalytic His varies slightly among UGT subfamilies (range ~20–40); position 27 is well within this range, but a model relying on a single reference UGT might expect a slightly different number.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein is 492 residues long, immediately eliminating option B (position 693 does not exist). The sequence length (~450–500 aa), N-terminal hydrophobic character, and overall composition are consistent with a plant UDP-glycosyltransferase (UGT). From knowledge of many other UGTs (e.g., human UGT1A/2B, plant UGT72/UGT74 families), the catalytic mechanism uses a conserved Histidine in the N-terminal Rossmann-like domain as a proton acceptor (general base), typically at positions ~25–35, while the C-terminal domain harbors the PSPG/UDP-sugar-binding region. Position 27 is H and falls squarely in this N-terminal catalytic window. Positions 327 and 256 lie in the C-terminal or linker regions, which in UGTs are associated with UDP-sugar binding, not proton abstraction. Thus, family-level knowledge of UGT domain architecture and catalytic residue positioning meaningfully distinguishes A from C and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model familiar with the UGT superfamily can apply the well-established rule that the catalytic proton-acceptor His resides in the N-terminal Rossmann-like domain around residues 25–35, learned from structural and mutagenesis studies of numerous other UGTs. This family-level inference, combined with the elimination of B (impossible position) and the domain-architecture argument against C and D, provides a credible transferable basis for selecting A without needing this protein's specific database record."
  },
  "case_id": "active_site_0052",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (C5/H3) records an Active site at position 27 described as 'Proton acceptor,' with evidence code ECO:0000250 (by similarity, transferred from A0A0A1HA03). The residue at position 27 in the supplied 492-aa sequence is indeed Histidine (H), consistent with the well-characterized UGT catalytic mechanism in which a conserved N-terminal His acts as a general base to deprotonate the substrate hydroxyl. The annotation is computational (by similarity), not experimental, but it is the recorded database fact. A second active-site annotation at position 131 is labeled 'Charge relay' (C6/H4), consistent with the UGT His-Asp catalytic dyad. The expected answer matches the annotation."
  },
  "important_caveats": [
    "The UniProt annotation for position 27 is by similarity (ECO:0000250), transferred from A0A0A1HA03, not directly experimentally validated for this specific protein.",
    "A canonical PSPG motif is not readily identifiable in the supplied sequence, which could make UGT family identification from sequence alone less straightforward for some models; however, size, N-terminal Rossmann-like character, and the choice context (proton acceptor vs. beta-ketoacyl synthase) provide supplementary cues.",
    "The exact position of the catalytic His varies slightly among UGT subfamilies (range ~20–40); position 27 is well within this range, but a model relying on a single reference UGT might expect a slightly different number."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option B is trivially eliminated (position 693 exceeds the 492-aa sequence). Among A, C, and D, the UGT family knowledge about the N-terminal location of the catalytic His cleanly distinguishes A. The 'proton acceptor' label in all three remaining choices does not create ambiguity because only one position can be the general base in the UGT catalytic dyad, and its N-terminal location is a conserved family feature."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0052",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (C5/H3) records an Active site at position 27 described as 'Proton acceptor,' with evidence code ECO:0000250 (by similarity, transferred from A0A0A1HA03). The residue at position 27 in the supplied 492-aa sequence is indeed Histidine (H), consistent with the well-characterized UGT catalytic mechanism in which a conserved N-terminal His acts as a general base to deprotonate the substrate hydroxyl. The annotation is computational (by similarity), not experimental, but it is the recorded database fact. A second active-site annotation at position 131 is labeled 'Charge relay' (C6/H4), consistent with the UGT His-Asp catalytic dyad. The expected answer matches the annotation.",
    "evidence_ids": ["C5", "H3", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein is 492 residues long, immediately eliminating option B (position 693 does not exist). The sequence length (~450–500 aa), N-terminal hydrophobic character, and overall composition are consistent with a plant UDP-glycosyltransferase (UGT). From knowledge of many other UGTs (e.g., human UGT1A/2B, plant UGT72/UGT74 families), the catalytic mechanism uses a conserved Histidine in the N-terminal Rossmann-like domain as a proton acceptor (general base), typically at positions ~25–35, while the C-terminal domain harbors the PSPG/UDP-sugar-binding region. Position 27 is H and falls squarely in this N-terminal catalytic window. Positions 327 and 256 lie in the C-terminal or linker regions, which in UGTs are associated with UDP-sugar binding, not proton abstraction. Thus, family-level knowledge of UGT domain architecture and catalytic residue positioning meaningfully distinguishes A from C and D.",
    "missing_item_specific_fact": "",
    "reason": "A model familiar with the UGT superfamily can apply the well-established rule that the catalytic proton-acceptor His resides in the N-terminal Rossmann-like domain around residues 25–35, learned from structural and mutagenesis studies of numerous other UGTs. This family-level inference, combined with the elimination of B (impossible position) and the domain-architecture argument against C and D, provides a credible transferable basis for selecting A without needing this protein's specific database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option B is trivially eliminated (position 693 exceeds the 492-aa sequence). Among A, C, and D, the UGT family knowledge about the N-terminal location of the catalytic His cleanly distinguishes A. The 'proton acceptor' label in all three remaining choices does not create ambiguity because only one position can be the general base in the UGT catalytic dyad, and its N-terminal location is a conserved family feature."
  },
  "important_caveats": [
    "The UniProt annotation for position 27 is by similarity (ECO:0000250), transferred from A0A0A1HA03, not directly experimentally validated for this specific protein.",
    "A canonical PSPG motif is not readily identifiable in the supplied sequence, which could make UGT family identification from sequence alone less straightforward for some models; however, size, N-terminal Rossmann-like character, and the choice context (proton acceptor vs. beta-ketoacyl synthase) provide supplementary cues.",
    "The exact position of the catalytic His varies slightly among UGT subfamilies (range ~20–40); position 27 is well within this range, but a model relying on a single reference UGT might expect a slightly different number."
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
  "benchmark_sequence_length": 492,
  "benchmark_sequence_sha256": "d01f6d4dbabab508bd73d7aac406c04cbfe1649f32055ff6cc318b8c504ba6c3",
  "current_entry_audit": {
    "entryVersion": 6,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2024-11-27",
    "sequenceVersion": 1
  },
  "current_record_sha256": "ff1d8de511ec47cbdc506fa8efe725b56c63c42715b9a2962823c3dd7244ffa7",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 492,
  "current_source_sequence_sha256": "d01f6d4dbabab508bd73d7aac406c04cbfe1649f32055ff6cc318b8c504ba6c3",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 5,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0AAW1K8I9",
  "selected_historical_entry_version": 5,
  "selected_historical_record_sha256": "46eff2d1174436813e2d0276cab6804ed02e27cf24990709a857ea963a1c34bb",
  "selected_historical_source_sequence_length": 492,
  "selected_historical_source_sequence_sha256": "d01f6d4dbabab508bd73d7aac406c04cbfe1649f32055ff6cc318b8c504ba6c3",
  "selected_historical_version": {
    "accession": "A0AAW1K8I9",
    "database": "Swiss-Prot",
    "entryVersion": 5,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "GT731_SAPOF",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1K8I9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0AAW1K8I9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:26:36.683131+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ff1d8de511ec47cbdc506fa8efe725b56c63c42715b9a2962823c3dd7244ffa7",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1K8I9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1K8I9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":6,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2024-11-27\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:26:36.683131+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ff1d8de511ec47cbdc506fa8efe725b56c63c42715b9a2962823c3dd7244ffa7",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1K8I9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1K8I9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Common soapwort\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"Caryophyllales\",\"Caryophyllaceae\",\"Caryophylleae\",\"Saponaria\"],\"scientificName\":\"Saponaria officinalis\",\"synonyms\":[\"Lychnis saponaria\"],\"taxonId\":3572}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:26:36.683131+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ff1d8de511ec47cbdc506fa8efe725b56c63c42715b9a2962823c3dd7244ffa7",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1K8I9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1K8I9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"2.4.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"UDP-glucosyl transferase 73DL1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"SoUGT73DL1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:26:36.683131+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ff1d8de511ec47cbdc506fa8efe725b56c63c42715b9a2962823c3dd7244ffa7",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1K8I9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1K8I9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Proton acceptor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A0A1HA03\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":27},\"start\":{\"modifier\":\"EXACT\",\"value\":27}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:26:36.683131+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ff1d8de511ec47cbdc506fa8efe725b56c63c42715b9a2962823c3dd7244ffa7",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1K8I9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1K8I9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Charge relay\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A0A1HA03\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":131},\"start\":{\"modifier\":\"EXACT\",\"value\":131}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:26:36.683131+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ff1d8de511ec47cbdc506fa8efe725b56c63c42715b9a2962823c3dd7244ffa7",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1K8I9.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1K8I9.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9M156\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58223\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58223\",\"name\":\"UDP\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":352},\"start\":{\"modifier\":\"EXACT\",\"value\":352}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:26:36.683131+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ff1d8de511ec47cbdc506fa8efe725b56c63c42715b9a2962823c3dd7244ffa7",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1K8I9.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1K8I9.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9M156\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58223\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58223\",\"name\":\"UDP\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":353},\"start\":{\"modifier\":\"EXACT\",\"value\":353}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:26:36.683131+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ff1d8de511ec47cbdc506fa8efe725b56c63c42715b9a2962823c3dd7244ffa7",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1K8I9.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1K8I9.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9M156\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58223\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58223\",\"name\":\"UDP\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":370},\"start\":{\"modifier\":\"EXACT\",\"value\":370}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:26:36.683131+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ff1d8de511ec47cbdc506fa8efe725b56c63c42715b9a2962823c3dd7244ffa7",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1K8I9.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1K8I9.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9M156\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58223\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58223\",\"name\":\"UDP\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":375},\"start\":{\"modifier\":\"EXACT\",\"value\":375}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:26:36.683131+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ff1d8de511ec47cbdc506fa8efe725b56c63c42715b9a2962823c3dd7244ffa7",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1K8I9.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1K8I9.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9M156\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58223\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58223\",\"name\":\"UDP\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":378},\"start\":{\"modifier\":\"EXACT\",\"value\":378}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:26:36.683131+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ff1d8de511ec47cbdc506fa8efe725b56c63c42715b9a2962823c3dd7244ffa7",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1K8I9.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1K8I9.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9M156\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58223\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58223\",\"name\":\"UDP\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":392},\"start\":{\"modifier\":\"EXACT\",\"value\":392}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:26:36.683131+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ff1d8de511ec47cbdc506fa8efe725b56c63c42715b9a2962823c3dd7244ffa7",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1K8I9.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1K8I9.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"citation\":{\"authors\":[\"Jo S.\",\"El-Demerdash A.\",\"Owen C.\",\"Srivastava V.\",\"Wu D.\",\"Kikuchi S.\",\"Reed J.\",\"Hodgson H.\",\"Harkess A.\",\"Shu S.\",\"Plott C.\",\"Jenkins J.\",\"Williams M.\",\"Boston L.-B.\",\"Lacchini E.\",\"Qu T.\",\"Goossens A.\",\"Grimwood J.\",\"Schmutz J.\",\"Leebens-Mack J.\",\"Osbourn A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39043959\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41589-024-01681-7\"}],\"citationType\":\"journal article\",\"firstPage\":\"215\",\"id\":\"39043959\",\"journal\":\"Nat. Chem. Biol.\",\"lastPage\":\"226\",\"publicationDate\":\"2025\",\"title\":\"Unlocking saponin biosynthesis in soapwort.\",\"volume\":\"21\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"WWM48158.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"TISSUE SPECIFICITY\",\"PATHWAY\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:26:36.683131+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ff1d8de511ec47cbdc506fa8efe725b56c63c42715b9a2962823c3dd7244ffa7",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1K8I9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1K8I9?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H1",
  "excerpt": "ID   GT731_SAPOF             Reviewed;         492 AA.\nAC   A0AAW1K8I9;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   27-NOV-2024, sequence version 1.\nDT   28-JAN-2026, entry version 5.\nDE   RecName: Full=UDP-glucosyl transferase 73DL1 {ECO:0000303|PubMed:39043959};\nDE            Short=SoUGT73DL1 {ECO:0000303|PubMed:39043959};\nDE            EC=2.4.1.- {ECO:0000269|PubMed:39043959};\nGN   Name=UGT73DL1 {ECO:0000303|PubMed:39043959};\nGN   Synonyms=Saoffv11029895m {ECO:0000303|PubMed:39043959};\nGN   ORFNames=RND81_06G065500 {ECO:0000312|EMBL:KAK9714013.1};\nOS   Saponaria officinalis (Common soapwort) (Lychnis saponaria).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   Caryophyllales; Caryophyllaceae; Caryophylleae; Saponaria.\nOX   NCBI_TaxID=3572;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:40.747220+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "46eff2d1174436813e2d0276cab6804ed02e27cf24990709a857ea963a1c34bb",
  "url": "https://rest.uniprot.org/unisave/A0AAW1K8I9?format=txt&versions=5"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1K8I9?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:WWM48158.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, TISSUE\nRP   SPECIFICITY, PATHWAY, AND BIOTECHNOLOGY.\nRX   PubMed=39043959; DOI=10.1038/s41589-024-01681-7;\nRA   Jo S., El-Demerdash A., Owen C., Srivastava V., Wu D., Kikuchi S., Reed J.,\nRA   Hodgson H., Harkess A., Shu S., Plott C., Jenkins J., Williams M.,\nRA   Boston L.-B., Lacchini E., Qu T., Goossens A., Grimwood J., Schmutz J.,\nRA   Leebens-Mack J., Osbourn A.;\nRT   \"Unlocking saponin biosynthesis in soapwort.\";\nRL   Nat. Chem. Biol. 21:215-226(2025).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:40.747220+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 17-26",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "46eff2d1174436813e2d0276cab6804ed02e27cf24990709a857ea963a1c34bb",
  "url": "https://rest.uniprot.org/unisave/A0AAW1K8I9?format=txt&versions=5"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1K8I9?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        27\nFT                   /note=\"Proton acceptor\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:A0A0A1HA03\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:40.747220+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 85-87",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "46eff2d1174436813e2d0276cab6804ed02e27cf24990709a857ea963a1c34bb",
  "url": "https://rest.uniprot.org/unisave/A0AAW1K8I9?format=txt&versions=5"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1K8I9?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H4",
  "excerpt": "FT   ACT_SITE        131\nFT                   /note=\"Charge relay\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:A0A0A1HA03\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:40.747220+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 88-90",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "46eff2d1174436813e2d0276cab6804ed02e27cf24990709a857ea963a1c34bb",
  "url": "https://rest.uniprot.org/unisave/A0AAW1K8I9?format=txt&versions=5"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1K8I9?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H5",
  "excerpt": "FT   BINDING         352\nFT                   /ligand=\"UDP\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58223\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9M156\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:40.747220+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 91-94",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "46eff2d1174436813e2d0276cab6804ed02e27cf24990709a857ea963a1c34bb",
  "url": "https://rest.uniprot.org/unisave/A0AAW1K8I9?format=txt&versions=5"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1K8I9?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H6",
  "excerpt": "FT   BINDING         353\nFT                   /ligand=\"UDP\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58223\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9M156\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:40.747220+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 95-98",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "46eff2d1174436813e2d0276cab6804ed02e27cf24990709a857ea963a1c34bb",
  "url": "https://rest.uniprot.org/unisave/A0AAW1K8I9?format=txt&versions=5"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1K8I9?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H7",
  "excerpt": "FT   BINDING         370\nFT                   /ligand=\"UDP\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58223\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9M156\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:40.747220+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 99-102",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "46eff2d1174436813e2d0276cab6804ed02e27cf24990709a857ea963a1c34bb",
  "url": "https://rest.uniprot.org/unisave/A0AAW1K8I9?format=txt&versions=5"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1K8I9?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H8",
  "excerpt": "FT   BINDING         375\nFT                   /ligand=\"UDP\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58223\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9M156\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:40.747220+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 103-106",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "46eff2d1174436813e2d0276cab6804ed02e27cf24990709a857ea963a1c34bb",
  "url": "https://rest.uniprot.org/unisave/A0AAW1K8I9?format=txt&versions=5"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1K8I9?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H9",
  "excerpt": "FT   BINDING         378\nFT                   /ligand=\"UDP\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58223\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9M156\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:40.747220+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 107-110",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "46eff2d1174436813e2d0276cab6804ed02e27cf24990709a857ea963a1c34bb",
  "url": "https://rest.uniprot.org/unisave/A0AAW1K8I9?format=txt&versions=5"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1K8I9?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H10",
  "excerpt": "FT   BINDING         392\nFT                   /ligand=\"UDP\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58223\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9M156\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:40.747220+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 111-114",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "46eff2d1174436813e2d0276cab6804ed02e27cf24990709a857ea963a1c34bb",
  "url": "https://rest.uniprot.org/unisave/A0AAW1K8I9?format=txt&versions=5"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 52. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
