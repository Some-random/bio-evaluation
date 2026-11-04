# active_site_0017

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0017.txt)

**Task:** `active_site`  
**Expected answer:** **D** — Position 146 (Proton acceptor)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTRKSILVTGASSGLGYAAVQKLAENGFYVFAAVREIRGMFSNIKNIKELKLDLANEQSIEELFIYIEATQKDYPLWGLVNNAGICVPSPLELLREFDLRQQLDTNVIGQLLVTQFALPFIRKSKGRIINITSGLGSIAVPYLGAYSIAQFAKMAFTDVLRRELKHSGVTVSVVQPGAIYTPIWDKFLVTGQEILDNSLDEKRKIYERSFIEFLKASQIGVNSVKTTRNDFAKVILDIFKAEIPETHYYVGDDAKNFSNKSKILTVTEIDEWFDLQSPTESEFKKI

[Multiple Choices]
A. Position 159 (Proton donor)
B. Position 250 (Proton acceptor)
C. Position 735 (For beta-ketoacyl synthase activity)
D. Position 146 (Proton acceptor)
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

> The matched UniProt record annotates residue 146 as a proton acceptor. This is a similarity-based annotation, not direct experimental confirmation for this protein.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> In the supplied sequence, residue 146 is Tyr, whereas residues 159 and 250 are Val; position 735 is outside the 286-residue sequence. Tyrosine can participate in proton transfer, while valine's side chain is not a plausible proton acceptor or donor. Thus D is meaningfully favored among these choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Residue chemistry and the offered positions distinguish D without requiring the target's recorded annotation. This makes D plausible, though sequence chemistry alone does not prove that Tyr146 is the active-site residue.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives at positions 159 and 250 are valines, and position 735 is beyond the sequence length; none is comparably plausible as a proton-transfer residue.


### Important caveats

- The source annotation for residue 146 cites evidence transferred by similarity (ECO:0000250), rather than direct experimental evidence for this protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "In the supplied sequence, residue 146 is Tyr, whereas residues 159 and 250 are Val; position 735 is outside the 286-residue sequence. Tyrosine can participate in proton transfer, while valine's side chain is not a plausible proton acceptor or donor. Thus D is meaningfully favored among these choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Residue chemistry and the offered positions distinguish D without requiring the target's recorded annotation. This makes D plausible, though sequence chemistry alone does not prove that Tyr146 is the active-site residue."
  },
  "case_id": "active_site_0017",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The matched UniProt record annotates residue 146 as a proton acceptor. This is a similarity-based annotation, not direct experimental confirmation for this protein."
  },
  "important_caveats": [
    "The source annotation for residue 146 cites evidence transferred by similarity (ECO:0000250), rather than direct experimental evidence for this protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives at positions 159 and 250 are valines, and position 735 is beyond the sequence length; none is comparably plausible as a proton-transfer residue."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0017",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched UniProt record annotates residue 146 as a proton acceptor. This is a similarity-based annotation, not direct experimental confirmation for this protein.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "In the supplied sequence, residue 146 is Tyr, whereas residues 159 and 250 are Val; position 735 is outside the 286-residue sequence. Tyrosine can participate in proton transfer, while valine's side chain is not a plausible proton acceptor or donor. Thus D is meaningfully favored among these choices.",
    "missing_item_specific_fact": "",
    "reason": "Residue chemistry and the offered positions distinguish D without requiring the target's recorded annotation. This makes D plausible, though sequence chemistry alone does not prove that Tyr146 is the active-site residue."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives at positions 159 and 250 are valines, and position 735 is beyond the sequence length; none is comparably plausible as a proton-transfer residue."
  },
  "important_caveats": [
    "The source annotation for residue 146 cites evidence transferred by similarity (ECO:0000250), rather than direct experimental evidence for this protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (C5, H3) explicitly records ACT_SITE at position 146 with the note 'Proton acceptor'. The evidence code is ECO:0000250 (inferred from similarity to P00334, another SDR enzyme), meaning the annotation is transferred by homology rather than directly experimentally measured on this protein. However, the SDR catalytic tetrad mechanism (Ser-Tyr-Lys-Asn with Tyr as proton acceptor) is one of the most thoroughly characterized enzymatic mechanisms, and position 146 in this sequence is indeed a Tyrosine (Y) located in the structurally expected catalytic context. The annotation is scientifically well-supported.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal sequence 'TGASSGLGY' (positions ~10-18) is the hallmark Rossmann-fold NAD(P)-binding motif of the short-chain dehydrogenase/reductase (SDR) superfamily, one of the most extensively characterized enzyme families. In SDRs, the well-established catalytic tetrad (Ser-Tyr-Lys-Asn) mediates hydride transfer, with the catalytic Tyrosine acting as the proton acceptor/donor. Scanning the sequence for the catalytic Tyr in the expected structural context identifies Y146 (in the motif 'SGLGSIAVPYLGAYSIAQ'). The distractors are eliminable by basic checks: option C references position 735 in a 286-residue protein (impossible); options A (position 159 = Valine) and B (position 250 = Valine) are non-catalytic hydrophobic residues inconsistent with any proton transfer role. Thus, family recognition (SDR from the N-terminal motif) plus textbook SDR mechanism (Tyr = proton acceptor) plus simple elimination of impossible/absurd options uniquely identifies D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the SDR family from the conserved N-terminal 'TGASSGLGY' motif, recall that the catalytic tyrosine in SDRs serves as the proton acceptor in the hydride-transfer mechanism, locate the catalytic Tyr at position 146 in the sequence, and eliminate the other choices (position 735 exceeds the 286-residue length; positions 159 and 250 are Valine residues). This relies on family-level mechanistic knowledge transferable across the SDR superfamily, not on memorizing this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option C is impossible (position 735 > 286 residues). Options A and B identify Valine residues, which cannot function as proton donors or acceptors. Only option D identifies a Tyrosine at a position consistent with the SDR catalytic tetrad. No ambiguity among the offered choices.


### Important caveats

- The UniProt active-site annotation carries evidence code ECO:0000250 (inferred from similarity to P00334), so it is a computational homology transfer rather than a direct experimental measurement on this specific protein. The SDR catalytic mechanism is, however, extremely well-characterized across the superfamily.
- The protein is annotated as EC 1.1.-.- (oxidoreductase, 3-amino-tetrahydro-pyrrolizinone reductase) in Xenorhabdus hominickii, but this organism/function information was not provided to the evaluated model and is not needed for the reasoning path described.
- The question asks for a single residue; in reality the SDR catalytic tetrad involves multiple residues (Ser, Tyr, Lys, Asn), but the question's format and options focus on the single proton-acceptor Tyr, which is the most commonly highlighted active-site residue in SDR annotations.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal sequence 'TGASSGLGY' (positions ~10-18) is the hallmark Rossmann-fold NAD(P)-binding motif of the short-chain dehydrogenase/reductase (SDR) superfamily, one of the most extensively characterized enzyme families. In SDRs, the well-established catalytic tetrad (Ser-Tyr-Lys-Asn) mediates hydride transfer, with the catalytic Tyrosine acting as the proton acceptor/donor. Scanning the sequence for the catalytic Tyr in the expected structural context identifies Y146 (in the motif 'SGLGSIAVPYLGAYSIAQ'). The distractors are eliminable by basic checks: option C references position 735 in a 286-residue protein (impossible); options A (position 159 = Valine) and B (position 250 = Valine) are non-catalytic hydrophobic residues inconsistent with any proton transfer role. Thus, family recognition (SDR from the N-terminal motif) plus textbook SDR mechanism (Tyr = proton acceptor) plus simple elimination of impossible/absurd options uniquely identifies D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the SDR family from the conserved N-terminal 'TGASSGLGY' motif, recall that the catalytic tyrosine in SDRs serves as the proton acceptor in the hydride-transfer mechanism, locate the catalytic Tyr at position 146 in the sequence, and eliminate the other choices (position 735 exceeds the 286-residue length; positions 159 and 250 are Valine residues). This relies on family-level mechanistic knowledge transferable across the SDR superfamily, not on memorizing this specific protein's database entry."
  },
  "case_id": "active_site_0017",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H3) explicitly records ACT_SITE at position 146 with the note 'Proton acceptor'. The evidence code is ECO:0000250 (inferred from similarity to P00334, another SDR enzyme), meaning the annotation is transferred by homology rather than directly experimentally measured on this protein. However, the SDR catalytic tetrad mechanism (Ser-Tyr-Lys-Asn with Tyr as proton acceptor) is one of the most thoroughly characterized enzymatic mechanisms, and position 146 in this sequence is indeed a Tyrosine (Y) located in the structurally expected catalytic context. The annotation is scientifically well-supported."
  },
  "important_caveats": [
    "The UniProt active-site annotation carries evidence code ECO:0000250 (inferred from similarity to P00334), so it is a computational homology transfer rather than a direct experimental measurement on this specific protein. The SDR catalytic mechanism is, however, extremely well-characterized across the superfamily.",
    "The protein is annotated as EC 1.1.-.- (oxidoreductase, 3-amino-tetrahydro-pyrrolizinone reductase) in Xenorhabdus hominickii, but this organism/function information was not provided to the evaluated model and is not needed for the reasoning path described.",
    "The question asks for a single residue; in reality the SDR catalytic tetrad involves multiple residues (Ser, Tyr, Lys, Asn), but the question's format and options focus on the single proton-acceptor Tyr, which is the most commonly highlighted active-site residue in SDR annotations."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C is impossible (position 735 > 286 residues). Options A and B identify Valine residues, which cannot function as proton donors or acceptors. Only option D identifies a Tyrosine at a position consistent with the SDR catalytic tetrad. No ambiguity among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0017",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H3) explicitly records ACT_SITE at position 146 with the note 'Proton acceptor'. The evidence code is ECO:0000250 (inferred from similarity to P00334, another SDR enzyme), meaning the annotation is transferred by homology rather than directly experimentally measured on this protein. However, the SDR catalytic tetrad mechanism (Ser-Tyr-Lys-Asn with Tyr as proton acceptor) is one of the most thoroughly characterized enzymatic mechanisms, and position 146 in this sequence is indeed a Tyrosine (Y) located in the structurally expected catalytic context. The annotation is scientifically well-supported.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal sequence 'TGASSGLGY' (positions ~10-18) is the hallmark Rossmann-fold NAD(P)-binding motif of the short-chain dehydrogenase/reductase (SDR) superfamily, one of the most extensively characterized enzyme families. In SDRs, the well-established catalytic tetrad (Ser-Tyr-Lys-Asn) mediates hydride transfer, with the catalytic Tyrosine acting as the proton acceptor/donor. Scanning the sequence for the catalytic Tyr in the expected structural context identifies Y146 (in the motif 'SGLGSIAVPYLGAYSIAQ'). The distractors are eliminable by basic checks: option C references position 735 in a 286-residue protein (impossible); options A (position 159 = Valine) and B (position 250 = Valine) are non-catalytic hydrophobic residues inconsistent with any proton transfer role. Thus, family recognition (SDR from the N-terminal motif) plus textbook SDR mechanism (Tyr = proton acceptor) plus simple elimination of impossible/absurd options uniquely identifies D.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the SDR family from the conserved N-terminal 'TGASSGLGY' motif, recall that the catalytic tyrosine in SDRs serves as the proton acceptor in the hydride-transfer mechanism, locate the catalytic Tyr at position 146 in the sequence, and eliminate the other choices (position 735 exceeds the 286-residue length; positions 159 and 250 are Valine residues). This relies on family-level mechanistic knowledge transferable across the SDR superfamily, not on memorizing this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C is impossible (position 735 > 286 residues). Options A and B identify Valine residues, which cannot function as proton donors or acceptors. Only option D identifies a Tyrosine at a position consistent with the SDR catalytic tetrad. No ambiguity among the offered choices."
  },
  "important_caveats": [
    "The UniProt active-site annotation carries evidence code ECO:0000250 (inferred from similarity to P00334), so it is a computational homology transfer rather than a direct experimental measurement on this specific protein. The SDR catalytic mechanism is, however, extremely well-characterized across the superfamily.",
    "The protein is annotated as EC 1.1.-.- (oxidoreductase, 3-amino-tetrahydro-pyrrolizinone reductase) in Xenorhabdus hominickii, but this organism/function information was not provided to the evaluated model and is not needed for the reasoning path described.",
    "The question asks for a single residue; in reality the SDR catalytic tetrad involves multiple residues (Ser, Tyr, Lys, Asn), but the question's format and options focus on the single proton-acceptor Tyr, which is the most commonly highlighted active-site residue in SDR annotations."
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
  "benchmark_sequence_length": 286,
  "benchmark_sequence_sha256": "5ac667f5b9af33314dc3039989b8675644797300210825d6858552c1a9de52cb",
  "current_entry_audit": {
    "entryVersion": 30,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2018-01-31",
    "sequenceVersion": 1
  },
  "current_record_sha256": "5510f043b076696b57f87efa7739b48cfedb1b8f19f87a14fd6d5a4d3624e099",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 286,
  "current_source_sequence_sha256": "5ac667f5b9af33314dc3039989b8675644797300210825d6858552c1a9de52cb",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 28,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A2G0QDN4",
  "selected_historical_entry_version": 28,
  "selected_historical_record_sha256": "e9a43167d987f4d30c210cf3857bc305e9fa0ec071e154f20f0d529315825c29",
  "selected_historical_source_sequence_length": 286,
  "selected_historical_source_sequence_sha256": "5ac667f5b9af33314dc3039989b8675644797300210825d6858552c1a9de52cb",
  "selected_historical_version": {
    "accession": "A0A2G0QDN4",
    "database": "Swiss-Prot",
    "entryVersion": 28,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "XHPD_XENHO",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2G0QDN4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A2G0QDN4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:47.620054+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5510f043b076696b57f87efa7739b48cfedb1b8f19f87a14fd6d5a4d3624e099",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2G0QDN4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2G0QDN4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":30,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2018-01-31\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:47.620054+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5510f043b076696b57f87efa7739b48cfedb1b8f19f87a14fd6d5a4d3624e099",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2G0QDN4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2G0QDN4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Enterobacterales\",\"Morganellaceae\",\"Xenorhabdus\"],\"scientificName\":\"Xenorhabdus hominickii\",\"taxonId\":351679}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:47.620054+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5510f043b076696b57f87efa7739b48cfedb1b8f19f87a14fd6d5a4d3624e099",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2G0QDN4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2G0QDN4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39428351\",\"source\":\"PubMed\"}],\"value\":\"1.1.-.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"39428351\",\"source\":\"PubMed\"}],\"value\":\"3-amino-tetrahydro-pyrrolizinone reductase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:47.620054+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5510f043b076696b57f87efa7739b48cfedb1b8f19f87a14fd6d5a4d3624e099",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2G0QDN4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2G0QDN4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Proton acceptor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P00334\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":146},\"start\":{\"modifier\":\"EXACT\",\"value\":146}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:24:47.620054+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5510f043b076696b57f87efa7739b48cfedb1b8f19f87a14fd6d5a4d3624e099",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2G0QDN4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2G0QDN4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Effert J.\",\"Westphalen M.\",\"Calderari A.\",\"Shi Y.M.\",\"Elamri I.\",\"Najah S.\",\"Gruen P.\",\"Li Y.\",\"Gruez A.\",\"Weissman K.J.\",\"Bode H.B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39428351\"},{\"database\":\"DOI\",\"id\":\"10.1002/anie.202411258\"}],\"citationType\":\"journal article\",\"firstPage\":\"e202411258\",\"id\":\"39428351\",\"journal\":\"Angew. Chem. Int. Ed.\",\"lastPage\":\"e202411258\",\"publicationDate\":\"2024\",\"title\":\"Pyrrolizwilline, a unique bacterial alkaloid assembled by a nonribosomal peptide synthetase and non-enzymatic dimerization.\",\"volume\":\"63\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"DSM 17903 / CIP 109072 / KE01\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:24:47.620054+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5510f043b076696b57f87efa7739b48cfedb1b8f19f87a14fd6d5a4d3624e099",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2G0QDN4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2G0QDN4?format=txt&versions=28)

```json
{
  "entry_version": 28,
  "evidence_id": "H1",
  "excerpt": "ID   XHPD_XENHO              Reviewed;         286 AA.\nAC   A0A2G0QDN4;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   31-JAN-2018, sequence version 1.\nDT   28-JAN-2026, entry version 28.\nDE   RecName: Full=3-amino-tetrahydro-pyrrolizinone reductase {ECO:0000305|PubMed:39428351};\nDE            EC=1.1.-.- {ECO:0000269|PubMed:39428351};\nGN   Name=xhpD; ORFNames=Xhom_00313 {ECO:0000312|EMBL:PHM57347.1};\nOS   Xenorhabdus hominickii.\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Enterobacterales; Morganellaceae; Xenorhabdus.\nOX   NCBI_TaxID=351679;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:49.959850+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e9a43167d987f4d30c210cf3857bc305e9fa0ec071e154f20f0d529315825c29",
  "url": "https://rest.uniprot.org/unisave/A0A2G0QDN4?format=txt&versions=28"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2G0QDN4?format=txt&versions=28)

```json
{
  "entry_version": 28,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, AND CATALYTIC ACTIVITY.\nRC   STRAIN=DSM 17903 / CIP 109072 / KE01;\nRX   PubMed=39428351; DOI=10.1002/anie.202411258;\nRA   Effert J., Westphalen M., Calderari A., Shi Y.M., Elamri I., Najah S.,\nRA   Gruen P., Li Y., Gruez A., Weissman K.J., Bode H.B.;\nRT   \"Pyrrolizwilline, a unique bacterial alkaloid assembled by a nonribosomal\nRT   peptide synthetase and non-enzymatic dimerization.\";\nRL   Angew. Chem. Int. Ed. 63:e202411258-e202411258(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:49.959850+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 23-31",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e9a43167d987f4d30c210cf3857bc305e9fa0ec071e154f20f0d529315825c29",
  "url": "https://rest.uniprot.org/unisave/A0A2G0QDN4?format=txt&versions=28"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2G0QDN4?format=txt&versions=28)

```json
{
  "entry_version": 28,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        146\nFT                   /note=\"Proton acceptor\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P00334\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:49.959850+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 73-75",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e9a43167d987f4d30c210cf3857bc305e9fa0ec071e154f20f0d529315825c29",
  "url": "https://rest.uniprot.org/unisave/A0A2G0QDN4?format=txt&versions=28"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 17. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
