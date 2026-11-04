# active_site_0106

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0106.txt)

**Task:** `active_site`  
**Expected answer:** **A** — Position 237 (Proton donor)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTGFLPEPLRMLVTSPALLDFTSDGPLPYALRQKFTGKPPPVTSNLSLASQTVLVTGATSGVGLEAARQLAQLGPRLLILGVRNASKAEQIKSELERDTPNLTVQVAELDLESLLSVDRFVDELSANSIRLDLALLNAGFFAHDDRITDDGYSPLFQVNFLSTAYLTLKLLPLLHTTAPPHPPGTTTPPGPRLVLVTSEAHAWTTFPDVPRPTENRTQPILSVFQDKNTLGSADDQYARAKLLLALFGKELSRRLTAAENDTTVVITTPGFCASNFFPDGMMTRLIQLTSARSVQQGGALHVFAATAPGPEIHGAYLRDGKPTGLSKFAQGPQGQILQERLWGEMEEFFMQRGGSPLGM

[Multiple Choices]
A. Position 237 (Proton donor)
B. Position 154 (Acyl-thioester intermediate)
C. Position 458 (For beta-ketoacyl synthase activity)
D. Position 215 (Charge relay system)
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

> The sequence-matched UniProt annotation identifies position 237 as a proton donor, and the archived annotation available by the historical cutoff agrees. This is homology-based annotation, not direct experimental evidence for this exact protein.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains an SDR-like nucleotide-binding motif near its N-terminus and a catalytic YxxxK motif at positions 237–241. In short-chain dehydrogenase/reductases, the conserved Tyr commonly serves as a catalytic proton donor. That transferable family pattern supports choice A; position 458 is outside the 359-residue sequence, and the other choices describe roles inconsistent with this SDR-like motif.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence motifs and standard SDR catalytic chemistry provide a meaningful basis to distinguish the offered answer without needing the exact protein's database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, the conserved catalytic Tyr motif supports A; the alternatives do not present a comparably plausible SDR catalytic role.


### Important caveats

- The source annotation is transferred by similarity to a homolog, so it should not be represented as direct experimental validation for this protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains an SDR-like nucleotide-binding motif near its N-terminus and a catalytic YxxxK motif at positions 237–241. In short-chain dehydrogenase/reductases, the conserved Tyr commonly serves as a catalytic proton donor. That transferable family pattern supports choice A; position 458 is outside the 359-residue sequence, and the other choices describe roles inconsistent with this SDR-like motif.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence motifs and standard SDR catalytic chemistry provide a meaningful basis to distinguish the offered answer without needing the exact protein's database record."
  },
  "case_id": "active_site_0106",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies position 237 as a proton donor, and the archived annotation available by the historical cutoff agrees. This is homology-based annotation, not direct experimental evidence for this exact protein."
  },
  "important_caveats": [
    "The source annotation is transferred by similarity to a homolog, so it should not be represented as direct experimental validation for this protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, the conserved catalytic Tyr motif supports A; the alternatives do not present a comparably plausible SDR catalytic role."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0106",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies position 237 as a proton donor, and the archived annotation available by the historical cutoff agrees. This is homology-based annotation, not direct experimental evidence for this exact protein.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains an SDR-like nucleotide-binding motif near its N-terminus and a catalytic YxxxK motif at positions 237–241. In short-chain dehydrogenase/reductases, the conserved Tyr commonly serves as a catalytic proton donor. That transferable family pattern supports choice A; position 458 is outside the 359-residue sequence, and the other choices describe roles inconsistent with this SDR-like motif.",
    "missing_item_specific_fact": "",
    "reason": "The sequence motifs and standard SDR catalytic chemistry provide a meaningful basis to distinguish the offered answer without needing the exact protein's database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, the conserved catalytic Tyr motif supports A; the alternatives do not present a comparably plausible SDR catalytic role."
  },
  "important_caveats": [
    "The source annotation is transferred by similarity to a homolog, so it should not be represented as direct experimental validation for this protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (P0DXW2) lists position 237 as 'Proton donor' active site. The sequence at position 237 is Tyrosine (Y), which is the catalytic proton donor in the SDR (Short-chain Dehydrogenase/Reductase) family's YxxxK motif. The annotation evidence code is ECO:0000250 (similarity-based transfer from O93868, another SDR), so it is computational/similarity-based rather than experimentally determined for this exact protein. However, the SDR catalytic mechanism is well-established, and the YxxxK motif (Y237-A238-R239-A240-K241) is clearly identifiable in the sequence, supporting the annotation.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains canonical SDR family motifs: the Rossmann-fold NAD(P)-binding motif 'GATSGVG' near position 55 (GxGxxG pattern), the 'GVRN' motif near position 81, and critically the YxxxK catalytic motif at positions 237-241 (Y-A-R-A-K). SDRs are among the best-characterized enzyme families, and their catalytic mechanism is textbook knowledge: the Tyr in the YxxxK motif serves as the proton donor during hydride transfer. A model recognizing the SDR fold from the NAD(P)-binding motifs can apply family-level knowledge to identify the catalytic Tyr. Option B (acyl-thioester) refers to serine hydrolase/thioesterase mechanisms irrelevant to SDRs. Option C (position 458) exceeds the 359-residue protein length. Option D (charge relay) describes serine protease triad chemistry, not SDR catalysis. Thus family-level SDR knowledge meaningfully distinguishes A from the alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognition of the SDR family from conserved NAD(P)-binding motifs (GxGxxG, GxGxxG, YxxxK) is transferable knowledge learned from many other SDR proteins. The catalytic role of Tyr as proton donor in the YxxxK motif is a well-established, generalizable feature of this large enzyme superfamily. The distractors are eliminable by family-level reasoning: acyl-thioester chemistry (B) belongs to a different enzyme class, position 458 (C) is beyond the protein length, and charge relay (D) is serine protease terminology. No fact specific to this exact protein's experimental characterization is needed.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option C references a non-existent position (458 > 359 residues). Option B invokes a mechanism (acyl-thioester intermediate) incompatible with SDR dehydrogenase chemistry. Option D invokes 'charge relay system' terminology associated with serine proteases, not SDRs. Only option A (Tyr237 as proton donor) is consistent with the identified SDR family and its well-known catalytic mechanism.


### Important caveats

- The UniProt active-site annotation uses evidence code ECO:0000250 (similarity-based transfer from O93868), not direct experimental determination for this specific protein. The annotation is nonetheless strongly supported by the clearly identifiable YxxxK motif in the sequence.
- The question asks for 'residues' (plural) constituting the catalytic center, but each option lists only a single position. This is a minor formatting quirk that does not affect answerability.
- Position 241 (Lys) is also annotated as active site ('Lowers pKa of active site Tyr') but is not offered as an option, so it does not create ambiguity among the given choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains canonical SDR family motifs: the Rossmann-fold NAD(P)-binding motif 'GATSGVG' near position 55 (GxGxxG pattern), the 'GVRN' motif near position 81, and critically the YxxxK catalytic motif at positions 237-241 (Y-A-R-A-K). SDRs are among the best-characterized enzyme families, and their catalytic mechanism is textbook knowledge: the Tyr in the YxxxK motif serves as the proton donor during hydride transfer. A model recognizing the SDR fold from the NAD(P)-binding motifs can apply family-level knowledge to identify the catalytic Tyr. Option B (acyl-thioester) refers to serine hydrolase/thioesterase mechanisms irrelevant to SDRs. Option C (position 458) exceeds the 359-residue protein length. Option D (charge relay) describes serine protease triad chemistry, not SDR catalysis. Thus family-level SDR knowledge meaningfully distinguishes A from the alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the SDR family from conserved NAD(P)-binding motifs (GxGxxG, GxGxxG, YxxxK) is transferable knowledge learned from many other SDR proteins. The catalytic role of Tyr as proton donor in the YxxxK motif is a well-established, generalizable feature of this large enzyme superfamily. The distractors are eliminable by family-level reasoning: acyl-thioester chemistry (B) belongs to a different enzyme class, position 458 (C) is beyond the protein length, and charge relay (D) is serine protease terminology. No fact specific to this exact protein's experimental characterization is needed."
  },
  "case_id": "active_site_0106",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (P0DXW2) lists position 237 as 'Proton donor' active site. The sequence at position 237 is Tyrosine (Y), which is the catalytic proton donor in the SDR (Short-chain Dehydrogenase/Reductase) family's YxxxK motif. The annotation evidence code is ECO:0000250 (similarity-based transfer from O93868, another SDR), so it is computational/similarity-based rather than experimentally determined for this exact protein. However, the SDR catalytic mechanism is well-established, and the YxxxK motif (Y237-A238-R239-A240-K241) is clearly identifiable in the sequence, supporting the annotation."
  },
  "important_caveats": [
    "The UniProt active-site annotation uses evidence code ECO:0000250 (similarity-based transfer from O93868), not direct experimental determination for this specific protein. The annotation is nonetheless strongly supported by the clearly identifiable YxxxK motif in the sequence.",
    "The question asks for 'residues' (plural) constituting the catalytic center, but each option lists only a single position. This is a minor formatting quirk that does not affect answerability.",
    "Position 241 (Lys) is also annotated as active site ('Lowers pKa of active site Tyr') but is not offered as an option, so it does not create ambiguity among the given choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C references a non-existent position (458 > 359 residues). Option B invokes a mechanism (acyl-thioester intermediate) incompatible with SDR dehydrogenase chemistry. Option D invokes 'charge relay system' terminology associated with serine proteases, not SDRs. Only option A (Tyr237 as proton donor) is consistent with the identified SDR family and its well-known catalytic mechanism."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0106",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (P0DXW2) lists position 237 as 'Proton donor' active site. The sequence at position 237 is Tyrosine (Y), which is the catalytic proton donor in the SDR (Short-chain Dehydrogenase/Reductase) family's YxxxK motif. The annotation evidence code is ECO:0000250 (similarity-based transfer from O93868, another SDR), so it is computational/similarity-based rather than experimentally determined for this exact protein. However, the SDR catalytic mechanism is well-established, and the YxxxK motif (Y237-A238-R239-A240-K241) is clearly identifiable in the sequence, supporting the annotation.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains canonical SDR family motifs: the Rossmann-fold NAD(P)-binding motif 'GATSGVG' near position 55 (GxGxxG pattern), the 'GVRN' motif near position 81, and critically the YxxxK catalytic motif at positions 237-241 (Y-A-R-A-K). SDRs are among the best-characterized enzyme families, and their catalytic mechanism is textbook knowledge: the Tyr in the YxxxK motif serves as the proton donor during hydride transfer. A model recognizing the SDR fold from the NAD(P)-binding motifs can apply family-level knowledge to identify the catalytic Tyr. Option B (acyl-thioester) refers to serine hydrolase/thioesterase mechanisms irrelevant to SDRs. Option C (position 458) exceeds the 359-residue protein length. Option D (charge relay) describes serine protease triad chemistry, not SDR catalysis. Thus family-level SDR knowledge meaningfully distinguishes A from the alternatives.",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the SDR family from conserved NAD(P)-binding motifs (GxGxxG, GxGxxG, YxxxK) is transferable knowledge learned from many other SDR proteins. The catalytic role of Tyr as proton donor in the YxxxK motif is a well-established, generalizable feature of this large enzyme superfamily. The distractors are eliminable by family-level reasoning: acyl-thioester chemistry (B) belongs to a different enzyme class, position 458 (C) is beyond the protein length, and charge relay (D) is serine protease terminology. No fact specific to this exact protein's experimental characterization is needed."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C references a non-existent position (458 > 359 residues). Option B invokes a mechanism (acyl-thioester intermediate) incompatible with SDR dehydrogenase chemistry. Option D invokes 'charge relay system' terminology associated with serine proteases, not SDRs. Only option A (Tyr237 as proton donor) is consistent with the identified SDR family and its well-known catalytic mechanism."
  },
  "important_caveats": [
    "The UniProt active-site annotation uses evidence code ECO:0000250 (similarity-based transfer from O93868), not direct experimental determination for this specific protein. The annotation is nonetheless strongly supported by the clearly identifiable YxxxK motif in the sequence.",
    "The question asks for 'residues' (plural) constituting the catalytic center, but each option lists only a single position. This is a minor formatting quirk that does not affect answerability.",
    "Position 241 (Lys) is also annotated as active site ('Lowers pKa of active site Tyr') but is not offered as an option, so it does not create ambiguity among the given choices."
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
  "benchmark_sequence_length": 359,
  "benchmark_sequence_sha256": "00a67859bfb5799f648543ed75c5168c3c4cc678d78363e0f961ad4cc8caaf9d",
  "current_entry_audit": {
    "entryVersion": 5,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-02-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "49814dbc0540f356312796fee8b194b75b6b25186a2dc9143b8e2d26b4cdfa13",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 359,
  "current_source_sequence_sha256": "00a67859bfb5799f648543ed75c5168c3c4cc678d78363e0f961ad4cc8caaf9d",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 3,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "P0DXW2",
  "selected_historical_entry_version": 3,
  "selected_historical_record_sha256": "4e45beb16fd49c0c1f92a0f6108115f68e9fd74fc759738d05578a39338e14e4",
  "selected_historical_source_sequence_length": 359,
  "selected_historical_source_sequence_sha256": "00a67859bfb5799f648543ed75c5168c3c4cc678d78363e0f961ad4cc8caaf9d",
  "selected_historical_version": {
    "accession": "P0DXW2",
    "database": "Swiss-Prot",
    "entryVersion": 3,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "RESG_ASPSL",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW2.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DXW2\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:29:52.717483+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "49814dbc0540f356312796fee8b194b75b6b25186a2dc9143b8e2d26b4cdfa13",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXW2.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW2.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":5,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-02-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:29:52.717483+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "49814dbc0540f356312796fee8b194b75b6b25186a2dc9143b8e2d26b4cdfa13",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXW2.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW2.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Aspergillus\",\"Circumdati\"],\"scientificName\":\"Aspergillus sclerotiorum\",\"taxonId\":138282}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:29:52.717483+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "49814dbc0540f356312796fee8b194b75b6b25186a2dc9143b8e2d26b4cdfa13",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXW2.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW2.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39105744\",\"source\":\"PubMed\"}],\"value\":\"Restricticin biosynthesis cluster protein G\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"39105744\",\"source\":\"PubMed\"}],\"value\":\"1.1.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39105744\",\"source\":\"PubMed\"}],\"value\":\"Short chain dehydrogenase resG\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:29:52.717483+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "49814dbc0540f356312796fee8b194b75b6b25186a2dc9143b8e2d26b4cdfa13",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXW2.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW2.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Proton donor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O93868\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":237},\"start\":{\"modifier\":\"EXACT\",\"value\":237}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:29:52.717483+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "49814dbc0540f356312796fee8b194b75b6b25186a2dc9143b8e2d26b4cdfa13",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXW2.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW2.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Lowers pKa of active site Tyr\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O93868\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":241},\"start\":{\"modifier\":\"EXACT\",\"value\":241}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:29:52.717483+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "49814dbc0540f356312796fee8b194b75b6b25186a2dc9143b8e2d26b4cdfa13",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXW2.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW2.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"L0E2Z4\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":87},\"start\":{\"modifier\":\"EXACT\",\"value\":87}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:29:52.717483+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "49814dbc0540f356312796fee8b194b75b6b25186a2dc9143b8e2d26b4cdfa13",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXW2.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW2.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"L0E2Z4\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":110},\"start\":{\"modifier\":\"EXACT\",\"value\":110}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:29:52.717483+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "49814dbc0540f356312796fee8b194b75b6b25186a2dc9143b8e2d26b4cdfa13",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXW2.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW2.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O93868\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":137},\"start\":{\"modifier\":\"EXACT\",\"value\":137}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:29:52.717483+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "49814dbc0540f356312796fee8b194b75b6b25186a2dc9143b8e2d26b4cdfa13",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXW2.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW2.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O93868\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":237},\"start\":{\"modifier\":\"EXACT\",\"value\":237}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:29:52.717483+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "49814dbc0540f356312796fee8b194b75b6b25186a2dc9143b8e2d26b4cdfa13",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXW2.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW2.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O93868\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58349\",\"name\":\"NADP(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":241},\"start\":{\"modifier\":\"EXACT\",\"value\":241}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:29:52.717483+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "49814dbc0540f356312796fee8b194b75b6b25186a2dc9143b8e2d26b4cdfa13",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXW2.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXW2.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"citation\":{\"authors\":[\"Lu Y.\",\"Li Y.\",\"Dou M.\",\"Liu D.\",\"Lin W.\",\"Fan A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39105744\"},{\"database\":\"DOI\",\"id\":\"10.1021/acs.jafc.4c04244\"}],\"citationType\":\"journal article\",\"firstPage\":\"18520\",\"id\":\"39105744\",\"journal\":\"J. Agric. Food Chem.\",\"lastPage\":\"18527\",\"publicationDate\":\"2024\",\"title\":\"Discovery of a hybrid molecule with phytotoxic activity by genome mining, heterologous expression, and OSMAC strategy.\",\"volume\":\"72\"},\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:29:52.717483+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "49814dbc0540f356312796fee8b194b75b6b25186a2dc9143b8e2d26b4cdfa13",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXW2.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW2?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H1",
  "excerpt": "ID   RESG_ASPSL              Reviewed;         359 AA.\nAC   P0DXW2;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-FEB-2025, sequence version 1.\nDT   28-JAN-2026, entry version 3.\nDE   RecName: Full=Short chain dehydrogenase resG {ECO:0000303|PubMed:39105744};\nDE            EC=1.1.1.- {ECO:0000305|PubMed:39105744};\nDE   AltName: Full=Restricticin biosynthesis cluster protein G {ECO:0000303|PubMed:39105744};\nGN   Name=resG {ECO:0000303|PubMed:39105744};\nOS   Aspergillus sclerotiorum.\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;\nOC   Aspergillus subgen. Circumdati.\nOX   NCBI_TaxID=138282;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:57.835506+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4e45beb16fd49c0c1f92a0f6108115f68e9fd74fc759738d05578a39338e14e4",
  "url": "https://rest.uniprot.org/unisave/P0DXW2?format=txt&versions=3"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW2?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H2",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, AND PATHWAY.\nRX   PubMed=39105744; DOI=10.1021/acs.jafc.4c04244;\nRA   Lu Y., Li Y., Dou M., Liu D., Lin W., Fan A.;\nRT   \"Discovery of a hybrid molecule with phytotoxic activity by genome mining,\nRT   heterologous expression, and OSMAC strategy.\";\nRL   J. Agric. Food Chem. 72:18520-18527(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:57.835506+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 15-21",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4e45beb16fd49c0c1f92a0f6108115f68e9fd74fc759738d05578a39338e14e4",
  "url": "https://rest.uniprot.org/unisave/P0DXW2?format=txt&versions=3"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW2?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        237\nFT                   /note=\"Proton donor\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:O93868\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:57.835506+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 60-62",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4e45beb16fd49c0c1f92a0f6108115f68e9fd74fc759738d05578a39338e14e4",
  "url": "https://rest.uniprot.org/unisave/P0DXW2?format=txt&versions=3"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW2?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H4",
  "excerpt": "FT   ACT_SITE        241\nFT                   /note=\"Lowers pKa of active site Tyr\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:O93868\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:57.835506+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 63-65",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4e45beb16fd49c0c1f92a0f6108115f68e9fd74fc759738d05578a39338e14e4",
  "url": "https://rest.uniprot.org/unisave/P0DXW2?format=txt&versions=3"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW2?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H5",
  "excerpt": "FT   BINDING         87\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:L0E2Z4\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:57.835506+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 66-69",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4e45beb16fd49c0c1f92a0f6108115f68e9fd74fc759738d05578a39338e14e4",
  "url": "https://rest.uniprot.org/unisave/P0DXW2?format=txt&versions=3"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW2?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H6",
  "excerpt": "FT   BINDING         110\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:L0E2Z4\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:57.835506+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 70-73",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4e45beb16fd49c0c1f92a0f6108115f68e9fd74fc759738d05578a39338e14e4",
  "url": "https://rest.uniprot.org/unisave/P0DXW2?format=txt&versions=3"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW2?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H7",
  "excerpt": "FT   BINDING         137\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:O93868\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:57.835506+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 74-77",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4e45beb16fd49c0c1f92a0f6108115f68e9fd74fc759738d05578a39338e14e4",
  "url": "https://rest.uniprot.org/unisave/P0DXW2?format=txt&versions=3"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW2?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H8",
  "excerpt": "FT   BINDING         237\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:O93868\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:57.835506+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 78-81",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4e45beb16fd49c0c1f92a0f6108115f68e9fd74fc759738d05578a39338e14e4",
  "url": "https://rest.uniprot.org/unisave/P0DXW2?format=txt&versions=3"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXW2?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H9",
  "excerpt": "FT   BINDING         241\nFT                   /ligand=\"NADP(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58349\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:O93868\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:57.835506+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 82-85",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4e45beb16fd49c0c1f92a0f6108115f68e9fd74fc759738d05578a39338e14e4",
  "url": "https://rest.uniprot.org/unisave/P0DXW2?format=txt&versions=3"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 106. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
