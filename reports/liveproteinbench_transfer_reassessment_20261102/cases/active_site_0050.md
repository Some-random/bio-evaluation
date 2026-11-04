# active_site_0050

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0050.txt)

**Task:** `active_site`  
**Expected answer:** **B** — Position 20 (Proton acceptor)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MEESKEEVHVAFFPFMTPGHSIPMLDLVRLFIARGVKTTVFTTPLNAPNISKYLNIIQDSSSNKNTIYVTPFPSKEAGLPEGVESQDSTTSPEMTLKFFVAMELLQDPLDVFLKETKPHCLVADNFFPYATDIASKYGIPRFVFQFTGFFPMSVMMALNRFHPQNSVSSDDDPFLVPSLPHDIKLTKSQLQREYEGSDGIDTALSRLCNGAGRALFTSYGVIFNSFYQLEPDYVDYYTNTMGKRSRVWHVGPVSLCNRRHVEGKSGRGRSASISEHLCLEWLNAKEPNSVIYVCFGSLTCFSNEQLKEIATALERCEEYFIWVLKGGKDNEQEWLPQGFEERVEGKGLIIRGWAPQVLILDHEAIGGFVTHCGWNSTLESISAGVPMVTWPIYAEQFYNEKLVTDVLKVGVKVGSMKWSETTGATHLKHEEIEKALKQIMVGEEVLEMRKRASKLKEMAYNAVEEGGSSYSHLTSLIDDLMASKAVLQKF

[Multiple Choices]
A. Position 120 (Nucleophile)
B. Position 20 (Proton acceptor)
C. Position 486 (Proton donor)
D. Position 277 (Nucleophile)
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

> The sequence-matched UniProt annotation identifies position 20 as the proton acceptor, supporting choice B. Its evidence is similarity-based transfer from another UniProt entry, not direct experimental evidence for this protein.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Position 20 is a histidine, and the sequence has features consistent with a plant family-1 UDP-dependent glycosyltransferase, including its C-terminal signature region. In this enzyme family, a conserved N-terminal histidine commonly acts as a catalytic base that accepts a proton from the sugar acceptor. That provides a transferable reason to favor B over the offered nucleophile and proton-donor alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The family-level catalytic-base pattern and the residue identity at position 20 meaningfully distinguish the choices without needing the exact protein's recorded annotation. This is a credible inference, though not proof of the specific protein's activity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options assign distinct catalytic roles and positions; the family-level inference favors the histidine proton acceptor at position 20.


### Important caveats

- The source annotation is supported by similarity evidence, so it should not be described as a direct experimental demonstration for this sequence.
- Reviewer evidence confirms the annotation on the sequence-matched entry, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Position 20 is a histidine, and the sequence has features consistent with a plant family-1 UDP-dependent glycosyltransferase, including its C-terminal signature region. In this enzyme family, a conserved N-terminal histidine commonly acts as a catalytic base that accepts a proton from the sugar acceptor. That provides a transferable reason to favor B over the offered nucleophile and proton-donor alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The family-level catalytic-base pattern and the residue identity at position 20 meaningfully distinguish the choices without needing the exact protein's recorded annotation. This is a credible inference, though not proof of the specific protein's activity."
  },
  "case_id": "active_site_0050",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies position 20 as the proton acceptor, supporting choice B. Its evidence is similarity-based transfer from another UniProt entry, not direct experimental evidence for this protein."
  },
  "important_caveats": [
    "The source annotation is supported by similarity evidence, so it should not be described as a direct experimental demonstration for this sequence.",
    "Reviewer evidence confirms the annotation on the sequence-matched entry, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options assign distinct catalytic roles and positions; the family-level inference favors the histidine proton acceptor at position 20."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0050",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies position 20 as the proton acceptor, supporting choice B. Its evidence is similarity-based transfer from another UniProt entry, not direct experimental evidence for this protein.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Position 20 is a histidine, and the sequence has features consistent with a plant family-1 UDP-dependent glycosyltransferase, including its C-terminal signature region. In this enzyme family, a conserved N-terminal histidine commonly acts as a catalytic base that accepts a proton from the sugar acceptor. That provides a transferable reason to favor B over the offered nucleophile and proton-donor alternatives.",
    "missing_item_specific_fact": "",
    "reason": "The family-level catalytic-base pattern and the residue identity at position 20 meaningfully distinguish the choices without needing the exact protein's recorded annotation. This is a credible inference, though not proof of the specific protein's activity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options assign distinct catalytic roles and positions; the family-level inference favors the histidine proton acceptor at position 20."
  },
  "important_caveats": [
    "The source annotation is supported by similarity evidence, so it should not be described as a direct experimental demonstration for this sequence.",
    "Reviewer evidence confirms the annotation on the sequence-matched entry, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (C5/H3) explicitly labels position 20 as 'Proton acceptor' active site. Position 20 in the sequence is indeed a Histidine (H), consistent with the well-known catalytic mechanism of plant UDP-glycosyltransferases (UGTs) where a conserved N-terminal His acts as a general base to deprotonate the substrate hydroxyl. The annotation evidence code is ECO:0000250 (inferred by similarity from A0A0A1HA03), making this a computational/family-level inference rather than direct experimental proof for this exact protein, but the mechanism is well-established across the UGT superfamily. The charge-relay Asp at position 124 (also annotated) further corroborates the His-Asp catalytic dyad typical of plant UGTs.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Multiple layers of transferable knowledge distinguish B from the alternatives: (1) Basic amino-acid chemistry immediately eliminates C (position 486 = Valine, which has no ionizable side chain and cannot act as a proton donor) and D (position 277 = Leucine, a hydrophobic residue with no nucleophilic capability). (2) Between A (Cys-120 as nucleophile) and B (His-20 as proton acceptor): recognizing the protein as a plant UGT is feasible from family-level features — the ~490 aa length, the PSPG-like motif region in the C-terminal domain (containing HCGW around positions 371-374), and the overall domain architecture. In plant UGTs, the well-characterized catalytic mechanism involves a conserved N-terminal His acting as a general base (proton acceptor) paired with an Asp charge relay, not a Cys nucleophile. The His at position 20 sits precisely in the N-terminal region where this catalytic His is conserved across the UGT family. (3) Even without full family identification, His is the archetypal general base/proton acceptor in enzyme catalysis (serine proteases, carbonic anhydrase, etc.), making B the chemically and mechanistically most plausible choice among the four options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can use basic amino-acid chemistry to eliminate C (Val as proton donor) and D (Leu as nucleophile), then apply UGT-family mechanistic knowledge (conserved N-terminal His as proton acceptor, PSPG motif in C-terminal domain) to select B over A. This does not require recalling the specific annotation of this exact protein; it relies on transferable family knowledge and fundamental biochemistry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options C and D are chemically impossible (Val cannot donate a proton; Leu cannot be a nucleophile). Option A (Cys as nucleophile) is mechanistically inconsistent with UGT catalysis. Only B (His as proton acceptor at the conserved N-terminal position) is chemically and mechanistically consistent with the protein's family identity and catalytic mechanism.


### Important caveats

- The UniProt active-site annotation at position 20 carries evidence code ECO:0000250 (similarity-based inference from A0A0A1HA03), not direct experimental validation for this specific Saponaria UGT73M2. However, the UGT catalytic mechanism is extensively characterized across the family.
- The protein function (UDP-glucosyl transferase, EC 2.4.2.-) was confirmed experimentally via the 2025 Nat. Chem. Biol. paper (PubMed:39043959), but the specific active-site residue assignment is by similarity.
- The model must correctly count residue positions from the raw sequence; an off-by-one error would shift all positions and mislead the answer.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Multiple layers of transferable knowledge distinguish B from the alternatives: (1) Basic amino-acid chemistry immediately eliminates C (position 486 = Valine, which has no ionizable side chain and cannot act as a proton donor) and D (position 277 = Leucine, a hydrophobic residue with no nucleophilic capability). (2) Between A (Cys-120 as nucleophile) and B (His-20 as proton acceptor): recognizing the protein as a plant UGT is feasible from family-level features — the ~490 aa length, the PSPG-like motif region in the C-terminal domain (containing HCGW around positions 371-374), and the overall domain architecture. In plant UGTs, the well-characterized catalytic mechanism involves a conserved N-terminal His acting as a general base (proton acceptor) paired with an Asp charge relay, not a Cys nucleophile. The His at position 20 sits precisely in the N-terminal region where this catalytic His is conserved across the UGT family. (3) Even without full family identification, His is the archetypal general base/proton acceptor in enzyme catalysis (serine proteases, carbonic anhydrase, etc.), making B the chemically and mechanistically most plausible choice among the four options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use basic amino-acid chemistry to eliminate C (Val as proton donor) and D (Leu as nucleophile), then apply UGT-family mechanistic knowledge (conserved N-terminal His as proton acceptor, PSPG motif in C-terminal domain) to select B over A. This does not require recalling the specific annotation of this exact protein; it relies on transferable family knowledge and fundamental biochemistry."
  },
  "case_id": "active_site_0050",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (C5/H3) explicitly labels position 20 as 'Proton acceptor' active site. Position 20 in the sequence is indeed a Histidine (H), consistent with the well-known catalytic mechanism of plant UDP-glycosyltransferases (UGTs) where a conserved N-terminal His acts as a general base to deprotonate the substrate hydroxyl. The annotation evidence code is ECO:0000250 (inferred by similarity from A0A0A1HA03), making this a computational/family-level inference rather than direct experimental proof for this exact protein, but the mechanism is well-established across the UGT superfamily. The charge-relay Asp at position 124 (also annotated) further corroborates the His-Asp catalytic dyad typical of plant UGTs."
  },
  "important_caveats": [
    "The UniProt active-site annotation at position 20 carries evidence code ECO:0000250 (similarity-based inference from A0A0A1HA03), not direct experimental validation for this specific Saponaria UGT73M2. However, the UGT catalytic mechanism is extensively characterized across the family.",
    "The protein function (UDP-glucosyl transferase, EC 2.4.2.-) was confirmed experimentally via the 2025 Nat. Chem. Biol. paper (PubMed:39043959), but the specific active-site residue assignment is by similarity.",
    "The model must correctly count residue positions from the raw sequence; an off-by-one error would shift all positions and mislead the answer."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are chemically impossible (Val cannot donate a proton; Leu cannot be a nucleophile). Option A (Cys as nucleophile) is mechanistically inconsistent with UGT catalysis. Only B (His as proton acceptor at the conserved N-terminal position) is chemically and mechanistically consistent with the protein's family identity and catalytic mechanism."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0050",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (C5/H3) explicitly labels position 20 as 'Proton acceptor' active site. Position 20 in the sequence is indeed a Histidine (H), consistent with the well-known catalytic mechanism of plant UDP-glycosyltransferases (UGTs) where a conserved N-terminal His acts as a general base to deprotonate the substrate hydroxyl. The annotation evidence code is ECO:0000250 (inferred by similarity from A0A0A1HA03), making this a computational/family-level inference rather than direct experimental proof for this exact protein, but the mechanism is well-established across the UGT superfamily. The charge-relay Asp at position 124 (also annotated) further corroborates the His-Asp catalytic dyad typical of plant UGTs.",
    "evidence_ids": ["C5", "H3", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Multiple layers of transferable knowledge distinguish B from the alternatives: (1) Basic amino-acid chemistry immediately eliminates C (position 486 = Valine, which has no ionizable side chain and cannot act as a proton donor) and D (position 277 = Leucine, a hydrophobic residue with no nucleophilic capability). (2) Between A (Cys-120 as nucleophile) and B (His-20 as proton acceptor): recognizing the protein as a plant UGT is feasible from family-level features — the ~490 aa length, the PSPG-like motif region in the C-terminal domain (containing HCGW around positions 371-374), and the overall domain architecture. In plant UGTs, the well-characterized catalytic mechanism involves a conserved N-terminal His acting as a general base (proton acceptor) paired with an Asp charge relay, not a Cys nucleophile. The His at position 20 sits precisely in the N-terminal region where this catalytic His is conserved across the UGT family. (3) Even without full family identification, His is the archetypal general base/proton acceptor in enzyme catalysis (serine proteases, carbonic anhydrase, etc.), making B the chemically and mechanistically most plausible choice among the four options.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use basic amino-acid chemistry to eliminate C (Val as proton donor) and D (Leu as nucleophile), then apply UGT-family mechanistic knowledge (conserved N-terminal His as proton acceptor, PSPG motif in C-terminal domain) to select B over A. This does not require recalling the specific annotation of this exact protein; it relies on transferable family knowledge and fundamental biochemistry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are chemically impossible (Val cannot donate a proton; Leu cannot be a nucleophile). Option A (Cys as nucleophile) is mechanistically inconsistent with UGT catalysis. Only B (His as proton acceptor at the conserved N-terminal position) is chemically and mechanistically consistent with the protein's family identity and catalytic mechanism."
  },
  "important_caveats": [
    "The UniProt active-site annotation at position 20 carries evidence code ECO:0000250 (similarity-based inference from A0A0A1HA03), not direct experimental validation for this specific Saponaria UGT73M2. However, the UGT catalytic mechanism is extensively characterized across the family.",
    "The protein function (UDP-glucosyl transferase, EC 2.4.2.-) was confirmed experimentally via the 2025 Nat. Chem. Biol. paper (PubMed:39043959), but the specific active-site residue assignment is by similarity.",
    "The model must correctly count residue positions from the raw sequence; an off-by-one error would shift all positions and mislead the answer."
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
  "benchmark_sequence_length": 490,
  "benchmark_sequence_sha256": "38574dde61c1837c70a51ac7df20c141558020651bad992714e5afc7349bcf3a",
  "current_entry_audit": {
    "entryVersion": 6,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2024-11-27",
    "sequenceVersion": 1
  },
  "current_record_sha256": "c673150bce8700e3ac48d0cf3cdfa8862b43c3fa1f362ecadc38dc4d2f8f245f",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 490,
  "current_source_sequence_sha256": "38574dde61c1837c70a51ac7df20c141558020651bad992714e5afc7349bcf3a",
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
  "requested_accession": "A0AAW1J1B8",
  "selected_historical_entry_version": 5,
  "selected_historical_record_sha256": "2d76ff4e8a8e533685cb991ace5dd8be42507b037a55e9b0396b1981c49ac7af",
  "selected_historical_source_sequence_length": 490,
  "selected_historical_source_sequence_sha256": "38574dde61c1837c70a51ac7df20c141558020651bad992714e5afc7349bcf3a",
  "selected_historical_version": {
    "accession": "A0AAW1J1B8",
    "database": "Swiss-Prot",
    "entryVersion": 5,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "GT732_SAPOF",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1J1B8.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0AAW1J1B8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:26:32.920868+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c673150bce8700e3ac48d0cf3cdfa8862b43c3fa1f362ecadc38dc4d2f8f245f",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1J1B8.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1J1B8.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":6,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2024-11-27\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:26:32.920868+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c673150bce8700e3ac48d0cf3cdfa8862b43c3fa1f362ecadc38dc4d2f8f245f",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1J1B8.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1J1B8.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Common soapwort\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"Caryophyllales\",\"Caryophyllaceae\",\"Caryophylleae\",\"Saponaria\"],\"scientificName\":\"Saponaria officinalis\",\"synonyms\":[\"Lychnis saponaria\"],\"taxonId\":3572}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:26:32.920868+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c673150bce8700e3ac48d0cf3cdfa8862b43c3fa1f362ecadc38dc4d2f8f245f",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1J1B8.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1J1B8.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"2.4.2.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"UDP-glucosyl transferase 73M2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"SoUGT73M2\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:26:32.920868+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c673150bce8700e3ac48d0cf3cdfa8862b43c3fa1f362ecadc38dc4d2f8f245f",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1J1B8.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1J1B8.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Proton acceptor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A0A1HA03\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":20},\"start\":{\"modifier\":\"EXACT\",\"value\":20}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:26:32.920868+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c673150bce8700e3ac48d0cf3cdfa8862b43c3fa1f362ecadc38dc4d2f8f245f",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1J1B8.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1J1B8.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Charge relay\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A0A1HA03\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":124},\"start\":{\"modifier\":\"EXACT\",\"value\":124}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:26:32.920868+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c673150bce8700e3ac48d0cf3cdfa8862b43c3fa1f362ecadc38dc4d2f8f245f",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1J1B8.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1J1B8.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9M156\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58223\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58223\",\"name\":\"UDP\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":297},\"start\":{\"modifier\":\"EXACT\",\"value\":297}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:26:32.920868+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c673150bce8700e3ac48d0cf3cdfa8862b43c3fa1f362ecadc38dc4d2f8f245f",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1J1B8.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1J1B8.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9M156\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58223\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58223\",\"name\":\"UDP\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":353},\"start\":{\"modifier\":\"EXACT\",\"value\":353}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:26:32.920868+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c673150bce8700e3ac48d0cf3cdfa8862b43c3fa1f362ecadc38dc4d2f8f245f",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1J1B8.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1J1B8.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9M156\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58223\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58223\",\"name\":\"UDP\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":354},\"start\":{\"modifier\":\"EXACT\",\"value\":354}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:26:32.920868+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c673150bce8700e3ac48d0cf3cdfa8862b43c3fa1f362ecadc38dc4d2f8f245f",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1J1B8.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1J1B8.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9M156\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58223\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58223\",\"name\":\"UDP\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":371},\"start\":{\"modifier\":\"EXACT\",\"value\":371}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:26:32.920868+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c673150bce8700e3ac48d0cf3cdfa8862b43c3fa1f362ecadc38dc4d2f8f245f",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1J1B8.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1J1B8.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9M156\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58223\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58223\",\"name\":\"UDP\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":375},\"start\":{\"modifier\":\"EXACT\",\"value\":375}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:26:32.920868+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c673150bce8700e3ac48d0cf3cdfa8862b43c3fa1f362ecadc38dc4d2f8f245f",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1J1B8.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1J1B8.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9M156\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58223\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58223\",\"name\":\"UDP\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":376},\"start\":{\"modifier\":\"EXACT\",\"value\":376}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:26:32.920868+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c673150bce8700e3ac48d0cf3cdfa8862b43c3fa1f362ecadc38dc4d2f8f245f",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1J1B8.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1J1B8.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9M156\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58223\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58223\",\"name\":\"UDP\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":379},\"start\":{\"modifier\":\"EXACT\",\"value\":379}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-02T04:26:32.920868+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c673150bce8700e3ac48d0cf3cdfa8862b43c3fa1f362ecadc38dc4d2f8f245f",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1J1B8.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1J1B8.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9M156\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58223\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58223\",\"name\":\"UDP\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":393},\"start\":{\"modifier\":\"EXACT\",\"value\":393}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-02T04:26:32.920868+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c673150bce8700e3ac48d0cf3cdfa8862b43c3fa1f362ecadc38dc4d2f8f245f",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1J1B8.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1J1B8.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"citation\":{\"authors\":[\"Jo S.\",\"El-Demerdash A.\",\"Owen C.\",\"Srivastava V.\",\"Wu D.\",\"Kikuchi S.\",\"Reed J.\",\"Hodgson H.\",\"Harkess A.\",\"Shu S.\",\"Plott C.\",\"Jenkins J.\",\"Williams M.\",\"Boston L.-B.\",\"Lacchini E.\",\"Qu T.\",\"Goossens A.\",\"Grimwood J.\",\"Schmutz J.\",\"Leebens-Mack J.\",\"Osbourn A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39043959\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41589-024-01681-7\"}],\"citationType\":\"journal article\",\"firstPage\":\"215\",\"id\":\"39043959\",\"journal\":\"Nat. Chem. Biol.\",\"lastPage\":\"226\",\"publicationDate\":\"2025\",\"title\":\"Unlocking saponin biosynthesis in soapwort.\",\"volume\":\"21\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"WWM48153.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"TISSUE SPECIFICITY\",\"PATHWAY\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:26:32.920868+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c673150bce8700e3ac48d0cf3cdfa8862b43c3fa1f362ecadc38dc4d2f8f245f",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1J1B8.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1J1B8?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H1",
  "excerpt": "ID   GT732_SAPOF             Reviewed;         490 AA.\nAC   A0AAW1J1B8;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   27-NOV-2024, sequence version 1.\nDT   28-JAN-2026, entry version 5.\nDE   RecName: Full=UDP-glucosyl transferase 73M2 {ECO:0000303|PubMed:39043959};\nDE            Short=SoUGT73M2 {ECO:0000303|PubMed:39043959};\nDE            EC=2.4.2.- {ECO:0000269|PubMed:39043959};\nGN   Name=UGT73M2 {ECO:0000303|PubMed:39043959};\nGN   Synonyms=Saoffv11038856m {ECO:0000303|PubMed:39043959};\nGN   ORFNames=RND81_08G000600 {ECO:0000312|EMBL:KAK9696842.1};\nOS   Saponaria officinalis (Common soapwort) (Lychnis saponaria).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   Caryophyllales; Caryophyllaceae; Caryophylleae; Saponaria.\nOX   NCBI_TaxID=3572;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:41.353913+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2d76ff4e8a8e533685cb991ace5dd8be42507b037a55e9b0396b1981c49ac7af",
  "url": "https://rest.uniprot.org/unisave/A0AAW1J1B8?format=txt&versions=5"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1J1B8?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:WWM48153.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, TISSUE\nRP   SPECIFICITY, PATHWAY, AND BIOTECHNOLOGY.\nRX   PubMed=39043959; DOI=10.1038/s41589-024-01681-7;\nRA   Jo S., El-Demerdash A., Owen C., Srivastava V., Wu D., Kikuchi S., Reed J.,\nRA   Hodgson H., Harkess A., Shu S., Plott C., Jenkins J., Williams M.,\nRA   Boston L.-B., Lacchini E., Qu T., Goossens A., Grimwood J., Schmutz J.,\nRA   Leebens-Mack J., Osbourn A.;\nRT   \"Unlocking saponin biosynthesis in soapwort.\";\nRL   Nat. Chem. Biol. 21:215-226(2025).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:41.353913+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 17-26",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2d76ff4e8a8e533685cb991ace5dd8be42507b037a55e9b0396b1981c49ac7af",
  "url": "https://rest.uniprot.org/unisave/A0AAW1J1B8?format=txt&versions=5"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1J1B8?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        20\nFT                   /note=\"Proton acceptor\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:A0A0A1HA03\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:41.353913+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 93-95",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2d76ff4e8a8e533685cb991ace5dd8be42507b037a55e9b0396b1981c49ac7af",
  "url": "https://rest.uniprot.org/unisave/A0AAW1J1B8?format=txt&versions=5"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1J1B8?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H4",
  "excerpt": "FT   ACT_SITE        124\nFT                   /note=\"Charge relay\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:A0A0A1HA03\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:41.353913+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 96-98",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2d76ff4e8a8e533685cb991ace5dd8be42507b037a55e9b0396b1981c49ac7af",
  "url": "https://rest.uniprot.org/unisave/A0AAW1J1B8?format=txt&versions=5"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1J1B8?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H5",
  "excerpt": "FT   BINDING         297\nFT                   /ligand=\"UDP\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58223\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9M156\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:41.353913+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 99-102",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2d76ff4e8a8e533685cb991ace5dd8be42507b037a55e9b0396b1981c49ac7af",
  "url": "https://rest.uniprot.org/unisave/A0AAW1J1B8?format=txt&versions=5"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1J1B8?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H6",
  "excerpt": "FT   BINDING         353\nFT                   /ligand=\"UDP\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58223\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9M156\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:41.353913+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 103-106",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2d76ff4e8a8e533685cb991ace5dd8be42507b037a55e9b0396b1981c49ac7af",
  "url": "https://rest.uniprot.org/unisave/A0AAW1J1B8?format=txt&versions=5"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1J1B8?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H7",
  "excerpt": "FT   BINDING         354\nFT                   /ligand=\"UDP\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58223\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9M156\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:41.353913+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 107-110",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2d76ff4e8a8e533685cb991ace5dd8be42507b037a55e9b0396b1981c49ac7af",
  "url": "https://rest.uniprot.org/unisave/A0AAW1J1B8?format=txt&versions=5"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1J1B8?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H8",
  "excerpt": "FT   BINDING         371\nFT                   /ligand=\"UDP\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58223\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9M156\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:41.353913+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 111-114",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2d76ff4e8a8e533685cb991ace5dd8be42507b037a55e9b0396b1981c49ac7af",
  "url": "https://rest.uniprot.org/unisave/A0AAW1J1B8?format=txt&versions=5"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1J1B8?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H9",
  "excerpt": "FT   BINDING         375\nFT                   /ligand=\"UDP\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58223\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9M156\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:41.353913+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 115-118",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2d76ff4e8a8e533685cb991ace5dd8be42507b037a55e9b0396b1981c49ac7af",
  "url": "https://rest.uniprot.org/unisave/A0AAW1J1B8?format=txt&versions=5"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1J1B8?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H10",
  "excerpt": "FT   BINDING         376\nFT                   /ligand=\"UDP\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58223\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9M156\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:41.353913+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 119-122",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2d76ff4e8a8e533685cb991ace5dd8be42507b037a55e9b0396b1981c49ac7af",
  "url": "https://rest.uniprot.org/unisave/A0AAW1J1B8?format=txt&versions=5"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1J1B8?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H11",
  "excerpt": "FT   BINDING         379\nFT                   /ligand=\"UDP\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58223\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9M156\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:41.353913+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 123-126",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2d76ff4e8a8e533685cb991ace5dd8be42507b037a55e9b0396b1981c49ac7af",
  "url": "https://rest.uniprot.org/unisave/A0AAW1J1B8?format=txt&versions=5"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1J1B8?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H12",
  "excerpt": "FT   BINDING         393\nFT                   /ligand=\"UDP\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58223\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9M156\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:41.353913+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 127-130",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2d76ff4e8a8e533685cb991ace5dd8be42507b037a55e9b0396b1981c49ac7af",
  "url": "https://rest.uniprot.org/unisave/A0AAW1J1B8?format=txt&versions=5"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 50. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
