# cofactor_0139

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0139.txt)

**Task:** `cofactor`  
**Expected answer:** **D** — Mg(2+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKKIAIIFGGNSPEYTVSLASATSAIEALQSSPYDYDLSLIGIAPDAMDWYLYTGELENIRQDTWLLDTKHKQKIQPLFEGNGFWLSEEQQTLVPDVLFPIMHGKYGEDGSIQGLFELMKLPYVGCGVAGSALCMNKWLLHQAAAAIGVQSAPTILLTNQANQQEQIEAFIQTHGFPVFFKPNEAGSSKGITKVTCVEEIASALKEAFTYCSAVLLQKNIAGVEIGCGILGNDSLTVGACDAISLVDGFFDFEEKYQLISAKITVPAPLPETIETKVKEQAQLLYRSLGLKGLARIDFFVTERGELYLNEINTMPGFTSHSRYPAMMAAVGLSYQELLQKLLVLAKEEVK

[Multiple Choices]
A. heme b
B. Mn(2+)
C. Zn(2+)
D. Mg(2+)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Predicting Protein Cofactor, which is to identify the specific cofactor required for a given protein's catalytic activity. A cofactor is a non-protein chemical compound or metallic ion that is essential for an enzyme's function. Based on the provided protein sequence, you will need to determine which of the multiple-choice options is the correct cofactor.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt annotation lists Mg(2+) as a cofactor, supporting D. This is a PROSITE-ProRule annotation, not direct experimental confirmation in the supplied evidence; the same annotation also lists Mn(2+).

Citations as saved: [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with an ATP-dependent D-Ala ligase family enzyme. Transferable knowledge of ATP-dependent ligation chemistry favors Mg(2+) as the conventional catalytic metal, distinguishing it from heme and Zn and providing a reasonable probabilistic preference over Mn(2+).


**Missing item-specific fact**

> An experimental determination of whether this enzyme specifically prefers Mg(2+) over Mn(2+) would be needed to make that preference definitive.


**Reason**

> Family-level and chemical knowledge supports Mg(2+) as a reasonable choice from the alternatives, though it does not establish exclusive use or rule out Mn(2+).


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> The sequence-matched annotation states that the enzyme binds Mg(2+) or Mn(2+), so both listed ions are defensible even though the author key selects Mg(2+).


### Important caveats

- The cofactor annotation is computationally assigned by a PROSITE rule; the cited characterization papers are not, in the supplied excerpts, direct evidence for a unique metal preference.
- The sequence match supports applying the annotation to this protein, but does not resolve the Mg(2+) versus Mn(2+) alternative.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with an ATP-dependent D-Ala ligase family enzyme. Transferable knowledge of ATP-dependent ligation chemistry favors Mg(2+) as the conventional catalytic metal, distinguishing it from heme and Zn and providing a reasonable probabilistic preference over Mn(2+).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "An experimental determination of whether this enzyme specifically prefers Mg(2+) over Mn(2+) would be needed to make that preference definitive.",
    "reason": "Family-level and chemical knowledge supports Mg(2+) as a reasonable choice from the alternatives, though it does not establish exclusive use or rule out Mn(2+)."
  },
  "case_id": "cofactor_0139",
  "expected_answer_check": {
    "evidence_ids": [
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation lists Mg(2+) as a cofactor, supporting D. This is a PROSITE-ProRule annotation, not direct experimental confirmation in the supplied evidence; the same annotation also lists Mn(2+)."
  },
  "important_caveats": [
    "The cofactor annotation is computationally assigned by a PROSITE rule; the cited characterization papers are not, in the supplied excerpts, direct evidence for a unique metal preference.",
    "The sequence match supports applying the annotation to this protein, but does not resolve the Mg(2+) versus Mn(2+) alternative."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "The sequence-matched annotation states that the enzyme binds Mg(2+) or Mn(2+), so both listed ions are defensible even though the author key selects Mg(2+)."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0139",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation lists Mg(2+) as a cofactor, supporting D. This is a PROSITE-ProRule annotation, not direct experimental confirmation in the supplied evidence; the same annotation also lists Mn(2+).",
    "evidence_ids": ["H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with an ATP-dependent D-Ala ligase family enzyme. Transferable knowledge of ATP-dependent ligation chemistry favors Mg(2+) as the conventional catalytic metal, distinguishing it from heme and Zn and providing a reasonable probabilistic preference over Mn(2+).",
    "missing_item_specific_fact": "An experimental determination of whether this enzyme specifically prefers Mg(2+) over Mn(2+) would be needed to make that preference definitive.",
    "reason": "Family-level and chemical knowledge supports Mg(2+) as a reasonable choice from the alternatives, though it does not establish exclusive use or rule out Mn(2+)."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "The sequence-matched annotation states that the enzyme binds Mg(2+) or Mn(2+), so both listed ions are defensible even though the author key selects Mg(2+)."
  },
  "important_caveats": [
    "The cofactor annotation is computationally assigned by a PROSITE rule; the cited characterization papers are not, in the supplied excerpts, direct evidence for a unique metal preference.",
    "The sequence match supports applying the annotation to this protein, but does not resolve the Mg(2+) versus Mn(2+) alternative."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for Q47720 (VanC2, D-alanine--D-serine ligase, EC 6.3.2.35) lists Mg(2+) as a cofactor (ChEBI:18420) with the note 'Binds 2 Mg(2+) or Mn(2+) ions per subunit.' Mg(2+) is explicitly listed, so the expected answer D is supported. However, Mn(2+) is also listed as an equivalent cofactor, and the evidence code is ECO:0000255 (PROSITE-ProRule), a computational/protein-rule annotation rather than direct experimental measurement. The experimental papers (Park 1997, Healy 1998) characterize the enzyme but the specific cofactor preference detail is not independently verified here.

Citations as saved: [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains hallmark motifs of the D-alanine ligase (Ddl) family: the N-terminal 'GGNSPE' motif, the overall ~350-residue length, and conserved regions (e.g., the 'GCGILGNDSL' region resembling the Ddl active-site loop). VanC2 is a well-known Van-type D-Ala:D-Ser ligase, a homolog of Ddl. Across the entire Ddl/Van ligase superfamily (Ddl, VanA, VanB, VanC, VanD, VanE, VanG, VanM, VanN, VanP), Mg(2+) is the canonical and primary divalent-metal cofactor, used to coordinate ATP and the carboxylate groups of the D-alanine/D-serine substrates during the two-step ligase mechanism. This is one of the most established cofactor assignments in bacterial cell-wall biosynthesis biochemistry. While UniProt also lists Mn(2+) as a possible substitute (via PROSITE-ProRule), Mg(2+) is the canonical family-level answer. A knowledgeable model recognizing the Ddl/Van family fingerprint would select Mg(2+) (D) over Mn(2+) (B), Zn(2+) (C), and heme b (A). Zn(2+) and heme b are not associated with this family at all.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognition of the Ddl/Van ligase family from conserved sequence motifs, combined with the well-established family-level knowledge that Mg(2+) is the canonical cofactor for D-Ala:D-Ala and D-Ala:D-Ser ligases, provides a concrete and credible transferable inference that meaningfully distinguishes D (Mg(2+)) from A (heme b), C (Zn(2+)), and to a meaningful extent from B (Mn(2+)). The canonical family assignment favors Mg(2+) as the primary cofactor.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> The UniProt annotation explicitly lists both Mg(2+) and Mn(2+) as cofactors with the note 'Binds 2 Mg(2+) or Mn(2+) ions per subunit,' making both technically correct. However, Mg(2+) is the canonical primary cofactor for the Ddl/Van ligase family, so D is the stronger and more standard answer. B is defensible as a secondary/substituting cofactor but is not the canonical choice.


### Important caveats

- The cofactor annotation evidence code is ECO:0000255 (PROSITE-ProRule), a computational protein-rule assignment, not a direct experimental measurement of cofactor specificity for this exact protein.
- Both Mg(2+) and Mn(2+) are listed as cofactors in the UniProt entry; the question's single-answer format forces a choice between two technically valid options, though Mg(2+) is the canonical family-level answer.
- The experimental papers (Park et al. 1997, Healy et al. 1998) characterize VanC2 function and biophysical properties but the specific cofactor preference data were not independently retrieved or validated here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hallmark motifs of the D-alanine ligase (Ddl) family: the N-terminal 'GGNSPE' motif, the overall ~350-residue length, and conserved regions (e.g., the 'GCGILGNDSL' region resembling the Ddl active-site loop). VanC2 is a well-known Van-type D-Ala:D-Ser ligase, a homolog of Ddl. Across the entire Ddl/Van ligase superfamily (Ddl, VanA, VanB, VanC, VanD, VanE, VanG, VanM, VanN, VanP), Mg(2+) is the canonical and primary divalent-metal cofactor, used to coordinate ATP and the carboxylate groups of the D-alanine/D-serine substrates during the two-step ligase mechanism. This is one of the most established cofactor assignments in bacterial cell-wall biosynthesis biochemistry. While UniProt also lists Mn(2+) as a possible substitute (via PROSITE-ProRule), Mg(2+) is the canonical family-level answer. A knowledgeable model recognizing the Ddl/Van family fingerprint would select Mg(2+) (D) over Mn(2+) (B), Zn(2+) (C), and heme b (A). Zn(2+) and heme b are not associated with this family at all.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the Ddl/Van ligase family from conserved sequence motifs, combined with the well-established family-level knowledge that Mg(2+) is the canonical cofactor for D-Ala:D-Ala and D-Ala:D-Ser ligases, provides a concrete and credible transferable inference that meaningfully distinguishes D (Mg(2+)) from A (heme b), C (Zn(2+)), and to a meaningful extent from B (Mn(2+)). The canonical family assignment favors Mg(2+) as the primary cofactor."
  },
  "case_id": "cofactor_0139",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for Q47720 (VanC2, D-alanine--D-serine ligase, EC 6.3.2.35) lists Mg(2+) as a cofactor (ChEBI:18420) with the note 'Binds 2 Mg(2+) or Mn(2+) ions per subunit.' Mg(2+) is explicitly listed, so the expected answer D is supported. However, Mn(2+) is also listed as an equivalent cofactor, and the evidence code is ECO:0000255 (PROSITE-ProRule), a computational/protein-rule annotation rather than direct experimental measurement. The experimental papers (Park 1997, Healy 1998) characterize the enzyme but the specific cofactor preference detail is not independently verified here."
  },
  "important_caveats": [
    "The cofactor annotation evidence code is ECO:0000255 (PROSITE-ProRule), a computational protein-rule assignment, not a direct experimental measurement of cofactor specificity for this exact protein.",
    "Both Mg(2+) and Mn(2+) are listed as cofactors in the UniProt entry; the question's single-answer format forces a choice between two technically valid options, though Mg(2+) is the canonical family-level answer.",
    "The experimental papers (Park et al. 1997, Healy et al. 1998) characterize VanC2 function and biophysical properties but the specific cofactor preference data were not independently retrieved or validated here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "The UniProt annotation explicitly lists both Mg(2+) and Mn(2+) as cofactors with the note 'Binds 2 Mg(2+) or Mn(2+) ions per subunit,' making both technically correct. However, Mg(2+) is the canonical primary cofactor for the Ddl/Van ligase family, so D is the stronger and more standard answer. B is defensible as a secondary/substituting cofactor but is not the canonical choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0139",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for Q47720 (VanC2, D-alanine--D-serine ligase, EC 6.3.2.35) lists Mg(2+) as a cofactor (ChEBI:18420) with the note 'Binds 2 Mg(2+) or Mn(2+) ions per subunit.' Mg(2+) is explicitly listed, so the expected answer D is supported. However, Mn(2+) is also listed as an equivalent cofactor, and the evidence code is ECO:0000255 (PROSITE-ProRule), a computational/protein-rule annotation rather than direct experimental measurement. The experimental papers (Park 1997, Healy 1998) characterize the enzyme but the specific cofactor preference detail is not independently verified here.",
    "evidence_ids": ["C5", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains hallmark motifs of the D-alanine ligase (Ddl) family: the N-terminal 'GGNSPE' motif, the overall ~350-residue length, and conserved regions (e.g., the 'GCGILGNDSL' region resembling the Ddl active-site loop). VanC2 is a well-known Van-type D-Ala:D-Ser ligase, a homolog of Ddl. Across the entire Ddl/Van ligase superfamily (Ddl, VanA, VanB, VanC, VanD, VanE, VanG, VanM, VanN, VanP), Mg(2+) is the canonical and primary divalent-metal cofactor, used to coordinate ATP and the carboxylate groups of the D-alanine/D-serine substrates during the two-step ligase mechanism. This is one of the most established cofactor assignments in bacterial cell-wall biosynthesis biochemistry. While UniProt also lists Mn(2+) as a possible substitute (via PROSITE-ProRule), Mg(2+) is the canonical family-level answer. A knowledgeable model recognizing the Ddl/Van family fingerprint would select Mg(2+) (D) over Mn(2+) (B), Zn(2+) (C), and heme b (A). Zn(2+) and heme b are not associated with this family at all.",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the Ddl/Van ligase family from conserved sequence motifs, combined with the well-established family-level knowledge that Mg(2+) is the canonical cofactor for D-Ala:D-Ala and D-Ala:D-Ser ligases, provides a concrete and credible transferable inference that meaningfully distinguishes D (Mg(2+)) from A (heme b), C (Zn(2+)), and to a meaningful extent from B (Mn(2+)). The canonical family assignment favors Mg(2+) as the primary cofactor."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "The UniProt annotation explicitly lists both Mg(2+) and Mn(2+) as cofactors with the note 'Binds 2 Mg(2+) or Mn(2+) ions per subunit,' making both technically correct. However, Mg(2+) is the canonical primary cofactor for the Ddl/Van ligase family, so D is the stronger and more standard answer. B is defensible as a secondary/substituting cofactor but is not the canonical choice."
  },
  "important_caveats": [
    "The cofactor annotation evidence code is ECO:0000255 (PROSITE-ProRule), a computational protein-rule assignment, not a direct experimental measurement of cofactor specificity for this exact protein.",
    "Both Mg(2+) and Mn(2+) are listed as cofactors in the UniProt entry; the question's single-answer format forces a choice between two technically valid options, though Mg(2+) is the canonical family-level answer.",
    "The experimental papers (Park et al. 1997, Healy et al. 1998) characterize VanC2 function and biophysical properties but the specific cofactor preference data were not independently retrieved or validated here."
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
  "benchmark_sequence_length": 350,
  "benchmark_sequence_sha256": "b4602f311134ca7446d9c233196a8829e27e15dc29e27680e1d34564cbfdd19c",
  "current_entry_audit": {
    "entryVersion": 149,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "1996-11-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "06db9d8bdf71a60d46c0d76bf8119766f2c979bd548827237a9036af1752f4cd",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 350,
  "current_source_sequence_sha256": "b4602f311134ca7446d9c233196a8829e27e15dc29e27680e1d34564cbfdd19c",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 147,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q47720",
  "selected_historical_entry_version": 147,
  "selected_historical_record_sha256": "7cd95341b40880e3967efdffddc7f3a25c7982d99fb2b3f1cf21db004390d78a",
  "selected_historical_source_sequence_length": 350,
  "selected_historical_source_sequence_sha256": "b4602f311134ca7446d9c233196a8829e27e15dc29e27680e1d34564cbfdd19c",
  "selected_historical_version": {
    "accession": "Q47720",
    "database": "Swiss-Prot",
    "entryVersion": 147,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "VANC2_ENTCA",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q47720.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q47720\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:30:46.048238+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "06db9d8bdf71a60d46c0d76bf8119766f2c979bd548827237a9036af1752f4cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q47720.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q47720.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":149,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"1996-11-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:30:46.048238+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "06db9d8bdf71a60d46c0d76bf8119766f2c979bd548827237a9036af1752f4cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q47720.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q47720.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Enterococcus flavescens\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAA60990.1\",\"source\":\"EMBL\"}],\"lineage\":[\"Bacteria\",\"Bacillati\",\"Bacillota\",\"Bacilli\",\"Lactobacillales\",\"Enterococcaceae\",\"Enterococcus\"],\"scientificName\":\"Enterococcus casseliflavus\",\"taxonId\":37734}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:30:46.048238+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "06db9d8bdf71a60d46c0d76bf8119766f2c979bd548827237a9036af1752f4cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q47720.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q47720.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_00047\",\"source\":\"HAMAP-Rule\"}],\"value\":\"D-alanine--D-serine ligase\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"VanC2 ligase\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"9294159\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"9545431\",\"source\":\"PubMed\"}],\"value\":\"6.3.2.35\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"9294159\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Vancomycin C-type resistance protein VanC2\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:30:46.048238+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "06db9d8bdf71a60d46c0d76bf8119766f2c979bd548827237a9036af1752f4cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q47720.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q47720.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:18420\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00409\",\"source\":\"PROSITE-ProRule\"}],\"name\":\"Mg(2+)\"},{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:29035\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00409\",\"source\":\"PROSITE-ProRule\"}],\"name\":\"Mn(2+)\"}],\"commentType\":\"COFACTOR\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00409\",\"source\":\"PROSITE-ProRule\"}],\"value\":\"Binds 2 Mg(2+) or Mn(2+) ions per subunit.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:30:46.048238+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "06db9d8bdf71a60d46c0d76bf8119766f2c979bd548827237a9036af1752f4cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q47720.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q47720.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Park I.S.\",\"Lin C.H.\",\"Walsh C.T.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"9294159\"},{\"database\":\"DOI\",\"id\":\"10.1073/pnas.94.19.10040\"}],\"citationType\":\"journal article\",\"firstPage\":\"10040\",\"id\":\"9294159\",\"journal\":\"Proc. Natl. Acad. Sci. U.S.A.\",\"lastPage\":\"10044\",\"publicationDate\":\"1997\",\"title\":\"Bacterial resistance to vancomycin: overproduction, purification, and characterization of VanC2 from Enterococcus casseliflavus as a D-Ala-D-Ser ligase.\",\"volume\":\"94\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"9294159\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"ATCC 25788\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"ACTIVITY REGULATION\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:30:46.048238+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "06db9d8bdf71a60d46c0d76bf8119766f2c979bd548827237a9036af1752f4cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q47720.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q47720.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Healy V.L.\",\"Park I.S.\",\"Walsh C.T.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"9545431\"},{\"database\":\"DOI\",\"id\":\"10.1016/s1074-5521(98)90633-0\"}],\"citationType\":\"journal article\",\"firstPage\":\"197\",\"id\":\"9545431\",\"journal\":\"Chem. Biol.\",\"lastPage\":\"207\",\"publicationDate\":\"1998\",\"title\":\"Active-site mutants of the VanC2 D-alanyl-D-serine ligase, characteristic of one vancomycin-resistant bacterial phenotype, revert towards wild-type D-alanyl-D-alanine ligases.\",\"volume\":\"5\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":5,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"MUTAGENESIS OF PHE-250 AND ARG-322\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-02T04:30:46.048238+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "06db9d8bdf71a60d46c0d76bf8119766f2c979bd548827237a9036af1752f4cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q47720.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q47720?format=txt&versions=147)

```json
{
  "entry_version": 147,
  "evidence_id": "H1",
  "excerpt": "ID   VANC2_ENTCA             Reviewed;         350 AA.\nAC   Q47720;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-NOV-1996, sequence version 1.\nDT   28-JAN-2026, entry version 147.\nDE   RecName: Full=Vancomycin C-type resistance protein VanC2 {ECO:0000303|PubMed:9294159, ECO:0000305};\nDE            EC=6.3.2.35 {ECO:0000269|PubMed:9294159, ECO:0000269|PubMed:9545431};\nDE   AltName: Full=D-alanine--D-serine ligase {ECO:0000255|HAMAP-Rule:MF_00047};\nDE   AltName: Full=VanC2 ligase {ECO:0000305};\nGN   Name=vanC2 {ECO:0000303|PubMed:9294159, ECO:0000303|PubMed:9545431,\nGN   ECO:0000312|EMBL:ABX79432.1};\nGN   Synonyms=ddl {ECO:0000255|HAMAP-Rule:MF_00047},\nGN   vanC-2 {ECO:0000312|EMBL:AAA60990.1};\nGN   ORFNames=P7I34_04740 {ECO:0000312|EMBL:MDT2981959.1};\nOS   Enterococcus casseliflavus (Enterococcus flavescens).\nOC   Bacteria; Bacillati; Bacillota; Bacilli; Lactobacillales; Enterococcaceae;\nOC   Enterococcus.\nOX   NCBI_TaxID=37734 {ECO:0000312|EMBL:AAA60990.1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:51.643943+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-18",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7cd95341b40880e3967efdffddc7f3a25c7982d99fb2b3f1cf21db004390d78a",
  "url": "https://rest.uniprot.org/unisave/Q47720?format=txt&versions=147"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q47720?format=txt&versions=147)

```json
{
  "entry_version": 147,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Vancomycin C-type resistance protein VanC2 {ECO:0000303|PubMed:9294159, ECO:0000305};\nDE            EC=6.3.2.35 {ECO:0000269|PubMed:9294159, ECO:0000269|PubMed:9545431};\nDE   AltName: Full=D-alanine--D-serine ligase {ECO:0000255|HAMAP-Rule:MF_00047};\nDE   AltName: Full=VanC2 ligase {ECO:0000305};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:51.643943+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-9",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7cd95341b40880e3967efdffddc7f3a25c7982d99fb2b3f1cf21db004390d78a",
  "url": "https://rest.uniprot.org/unisave/Q47720?format=txt&versions=147"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q47720?format=txt&versions=147)

```json
{
  "entry_version": 147,
  "evidence_id": "H3",
  "excerpt": "RN   [4] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, ACTIVITY\nRP   REGULATION, AND SUBUNIT.\nRC   STRAIN=ATCC 25788 {ECO:0000303|PubMed:9294159};\nRX   PubMed=9294159; DOI=10.1073/pnas.94.19.10040;\nRA   Park I.S., Lin C.H., Walsh C.T.;\nRT   \"Bacterial resistance to vancomycin: overproduction, purification, and\nRT   characterization of VanC2 from Enterococcus casseliflavus as a D-Ala-D-Ser\nRT   ligase.\";\nRL   Proc. Natl. Acad. Sci. U.S.A. 94:10040-10044(1997).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:51.643943+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 42-51",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7cd95341b40880e3967efdffddc7f3a25c7982d99fb2b3f1cf21db004390d78a",
  "url": "https://rest.uniprot.org/unisave/Q47720?format=txt&versions=147"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q47720?format=txt&versions=147)

```json
{
  "entry_version": 147,
  "evidence_id": "H4",
  "excerpt": "RN   [5] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND\nRP   MUTAGENESIS OF PHE-250 AND ARG-322.\nRX   PubMed=9545431; DOI=10.1016/s1074-5521(98)90633-0;\nRA   Healy V.L., Park I.S., Walsh C.T.;\nRT   \"Active-site mutants of the VanC2 D-alanyl-D-serine ligase, characteristic\nRT   of one vancomycin-resistant bacterial phenotype, revert towards wild-type\nRT   D-alanyl-D-alanine ligases.\";\nRL   Chem. Biol. 5:197-207(1998).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:51.643943+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 52-60",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7cd95341b40880e3967efdffddc7f3a25c7982d99fb2b3f1cf21db004390d78a",
  "url": "https://rest.uniprot.org/unisave/Q47720?format=txt&versions=147"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q47720?format=txt&versions=147)

```json
{
  "entry_version": 147,
  "evidence_id": "H5",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=Mg(2+); Xref=ChEBI:CHEBI:18420;\nCC         Evidence={ECO:0000255|PROSITE-ProRule:PRU00409};\nCC       Name=Mn(2+); Xref=ChEBI:CHEBI:29035;\nCC         Evidence={ECO:0000255|PROSITE-ProRule:PRU00409};\nCC       Note=Binds 2 Mg(2+) or Mn(2+) ions per subunit. {ECO:0000255|PROSITE-\nCC       ProRule:PRU00409};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:51.643943+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 77-83",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7cd95341b40880e3967efdffddc7f3a25c7982d99fb2b3f1cf21db004390d78a",
  "url": "https://rest.uniprot.org/unisave/Q47720?format=txt&versions=147"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 139. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
