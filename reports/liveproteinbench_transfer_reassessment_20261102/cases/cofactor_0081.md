# cofactor_0081

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0081.txt)

**Task:** `cofactor`  
**Expected answer:** **D** — FMN

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAGSEPVSAEGESMAVDAAPRKPRILLAASGSVAAVKFANLCHCFSEWADVRAVSSSGSLHFIDRASMPKDVILYTDEDEWSSWKKLGDSVLHIELRKWADIMVIAPLSANTLGKIAGGLCDNLLTCIVRAWDYSKPFFVAPAMNTLMWNNPFTERHFISIDELGISLIPPVTKRLACGDYGNGAMAEPSTIYSTVRLFYESKAQQGRAVVTLR

[Multiple Choices]
A. heme b
B. Fe(2+)
C. FAD
D. FMN
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

> The supplied sequence matches the source record, which annotates one FMN per subunit. That annotation is transferred by similarity (ECO:0000250), so it supports FMN but is not direct experimental evidence for this exact protein.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 214-residue sequence is consistent with the HAL3/phosphopantothenoylcysteine decarboxylase family. Transferable knowledge of this enzyme family supports an FMN-dependent enzyme, distinguishing FMN from heme b and Fe(2+); family-level knowledge also distinguishes FMN from FAD.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognizing the family from sequence patterns and applying its known cofactor preference offers a meaningful basis for the keyed choice without recalling this exact protein’s database annotation. This is a probabilistic family inference, not proof of the individual protein’s cofactor requirement.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The family-level cofactor inference supports FMN among the offered choices; no other option is comparably defensible from the supplied sequence.


### Important caveats

- The source annotation is similarity-based, not identified here as experimentally established for this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 214-residue sequence is consistent with the HAL3/phosphopantothenoylcysteine decarboxylase family. Transferable knowledge of this enzyme family supports an FMN-dependent enzyme, distinguishing FMN from heme b and Fe(2+); family-level knowledge also distinguishes FMN from FAD.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognizing the family from sequence patterns and applying its known cofactor preference offers a meaningful basis for the keyed choice without recalling this exact protein’s database annotation. This is a probabilistic family inference, not proof of the individual protein’s cofactor requirement."
  },
  "case_id": "cofactor_0081",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches the source record, which annotates one FMN per subunit. That annotation is transferred by similarity (ECO:0000250), so it supports FMN but is not direct experimental evidence for this exact protein."
  },
  "important_caveats": [
    "The source annotation is similarity-based, not identified here as experimentally established for this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The family-level cofactor inference supports FMN among the offered choices; no other option is comparably defensible from the supplied sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0081",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches the source record, which annotates one FMN per subunit. That annotation is transferred by similarity (ECO:0000250), so it supports FMN but is not direct experimental evidence for this exact protein.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 214-residue sequence is consistent with the HAL3/phosphopantothenoylcysteine decarboxylase family. Transferable knowledge of this enzyme family supports an FMN-dependent enzyme, distinguishing FMN from heme b and Fe(2+); family-level knowledge also distinguishes FMN from FAD.",
    "missing_item_specific_fact": "",
    "reason": "Recognizing the family from sequence patterns and applying its known cofactor preference offers a meaningful basis for the keyed choice without recalling this exact protein’s database annotation. This is a probabilistic family inference, not proof of the individual protein’s cofactor requirement."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The family-level cofactor inference supports FMN among the offered choices; no other option is comparably defensible from the supplied sequence."
  },
  "important_caveats": [
    "The source annotation is similarity-based, not identified here as experimentally established for this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (C5, H3) lists FMN as the cofactor with evidence code ECO:0000250 (inferred by similarity from Q9SWE5, the yeast HAL3/PPCDC). While this is a homology-transferred annotation rather than direct experimental data on this specific soybean protein, the PPCDC family (EC 4.1.1.36) is well-established as FMN-dependent from crystal structures of human PPCDC (e.g., PDB 3O2E/3O2F). The annotation applies to the supplied sequence (214 aa, matched). The FMN assignment is consistent with the family-level experimental evidence.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 214-residue sequence contains recognizable PPCDC/HAL3 family signatures: the 'NACHCFSEW' motif near position 40 and the 'LACGDYGNG' motif near position 195, combined with the small overall size (~214 aa) characteristic of the HAL3/PPCDC family (PF03600). A model familiar with the PPCDC family from human, yeast, or bacterial homologs would recognize these patterns and recall that PPCDC is an FMN-dependent decarboxylase (EC 4.1.1.36) in the CoA biosynthesis pathway. This family-level knowledge distinguishes FMN (D) from FAD (C): PPCDC specifically binds FMN per subunit, not FAD, as demonstrated by crystal structures of human PPCDC. Heme b (A) and Fe(2+) (B) are excluded because PPCDC is a flavoprotein decarboxylase, not a heme or iron-dependent enzyme; the sequence lacks CXXCH heme-binding motifs or canonical iron-coordinating triads.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognition of the PPCDC/HAL3 family from conserved sequence motifs (CHCF, LACGDYGNG, small size) plus family-level knowledge from human and yeast PPCDC homologs provides a credible inference that the cofactor is FMN rather than FAD, heme b, or Fe(2+). This is legitimate transferable knowledge from related proteins, not a lookup of this specific soybean entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options are mechanistically distinct: heme b (tetrapyrrole iron), Fe(2+) (metal ion), FAD and FMN (flavins). PPCDC family knowledge clearly selects FMN over FAD (specific flavin preference established structurally) and excludes heme/iron options entirely. No ambiguity among the offered choices.


### Important caveats

- The UniProt annotation for this specific soybean protein uses ECO:0000250 (inferred by similarity), not direct experimental evidence on the soybean protein itself. The FMN assignment rests on homology to characterized PPCDC enzymes.
- The sequence lacks an obvious canonical Rossmann-fold GxGxxG motif, so family recognition depends on more subtle PPCDC-specific signatures rather than a generic flavin-binding motif.
- Distinguishing FMN from FAD at the sequence level without family recognition could be challenging, as both are flavins with similar binding modes; the PPCDC family's specific FMN preference is the key discriminating knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 214-residue sequence contains recognizable PPCDC/HAL3 family signatures: the 'NACHCFSEW' motif near position 40 and the 'LACGDYGNG' motif near position 195, combined with the small overall size (~214 aa) characteristic of the HAL3/PPCDC family (PF03600). A model familiar with the PPCDC family from human, yeast, or bacterial homologs would recognize these patterns and recall that PPCDC is an FMN-dependent decarboxylase (EC 4.1.1.36) in the CoA biosynthesis pathway. This family-level knowledge distinguishes FMN (D) from FAD (C): PPCDC specifically binds FMN per subunit, not FAD, as demonstrated by crystal structures of human PPCDC. Heme b (A) and Fe(2+) (B) are excluded because PPCDC is a flavoprotein decarboxylase, not a heme or iron-dependent enzyme; the sequence lacks CXXCH heme-binding motifs or canonical iron-coordinating triads.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the PPCDC/HAL3 family from conserved sequence motifs (CHCF, LACGDYGNG, small size) plus family-level knowledge from human and yeast PPCDC homologs provides a credible inference that the cofactor is FMN rather than FAD, heme b, or Fe(2+). This is legitimate transferable knowledge from related proteins, not a lookup of this specific soybean entry."
  },
  "case_id": "cofactor_0081",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H3) lists FMN as the cofactor with evidence code ECO:0000250 (inferred by similarity from Q9SWE5, the yeast HAL3/PPCDC). While this is a homology-transferred annotation rather than direct experimental data on this specific soybean protein, the PPCDC family (EC 4.1.1.36) is well-established as FMN-dependent from crystal structures of human PPCDC (e.g., PDB 3O2E/3O2F). The annotation applies to the supplied sequence (214 aa, matched). The FMN assignment is consistent with the family-level experimental evidence."
  },
  "important_caveats": [
    "The UniProt annotation for this specific soybean protein uses ECO:0000250 (inferred by similarity), not direct experimental evidence on the soybean protein itself. The FMN assignment rests on homology to characterized PPCDC enzymes.",
    "The sequence lacks an obvious canonical Rossmann-fold GxGxxG motif, so family recognition depends on more subtle PPCDC-specific signatures rather than a generic flavin-binding motif.",
    "Distinguishing FMN from FAD at the sequence level without family recognition could be challenging, as both are flavins with similar binding modes; the PPCDC family's specific FMN preference is the key discriminating knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are mechanistically distinct: heme b (tetrapyrrole iron), Fe(2+) (metal ion), FAD and FMN (flavins). PPCDC family knowledge clearly selects FMN over FAD (specific flavin preference established structurally) and excludes heme/iron options entirely. No ambiguity among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0081",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H3) lists FMN as the cofactor with evidence code ECO:0000250 (inferred by similarity from Q9SWE5, the yeast HAL3/PPCDC). While this is a homology-transferred annotation rather than direct experimental data on this specific soybean protein, the PPCDC family (EC 4.1.1.36) is well-established as FMN-dependent from crystal structures of human PPCDC (e.g., PDB 3O2E/3O2F). The annotation applies to the supplied sequence (214 aa, matched). The FMN assignment is consistent with the family-level experimental evidence.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 214-residue sequence contains recognizable PPCDC/HAL3 family signatures: the 'NACHCFSEW' motif near position 40 and the 'LACGDYGNG' motif near position 195, combined with the small overall size (~214 aa) characteristic of the HAL3/PPCDC family (PF03600). A model familiar with the PPCDC family from human, yeast, or bacterial homologs would recognize these patterns and recall that PPCDC is an FMN-dependent decarboxylase (EC 4.1.1.36) in the CoA biosynthesis pathway. This family-level knowledge distinguishes FMN (D) from FAD (C): PPCDC specifically binds FMN per subunit, not FAD, as demonstrated by crystal structures of human PPCDC. Heme b (A) and Fe(2+) (B) are excluded because PPCDC is a flavoprotein decarboxylase, not a heme or iron-dependent enzyme; the sequence lacks CXXCH heme-binding motifs or canonical iron-coordinating triads.",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the PPCDC/HAL3 family from conserved sequence motifs (CHCF, LACGDYGNG, small size) plus family-level knowledge from human and yeast PPCDC homologs provides a credible inference that the cofactor is FMN rather than FAD, heme b, or Fe(2+). This is legitimate transferable knowledge from related proteins, not a lookup of this specific soybean entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are mechanistically distinct: heme b (tetrapyrrole iron), Fe(2+) (metal ion), FAD and FMN (flavins). PPCDC family knowledge clearly selects FMN over FAD (specific flavin preference established structurally) and excludes heme/iron options entirely. No ambiguity among the offered choices."
  },
  "important_caveats": [
    "The UniProt annotation for this specific soybean protein uses ECO:0000250 (inferred by similarity), not direct experimental evidence on the soybean protein itself. The FMN assignment rests on homology to characterized PPCDC enzymes.",
    "The sequence lacks an obvious canonical Rossmann-fold GxGxxG motif, so family recognition depends on more subtle PPCDC-specific signatures rather than a generic flavin-binding motif.",
    "Distinguishing FMN from FAD at the sequence level without family recognition could be challenging, as both are flavins with similar binding modes; the PPCDC family's specific FMN preference is the key discriminating knowledge."
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
  "benchmark_sequence_length": 214,
  "benchmark_sequence_sha256": "dcaceed6f1d468598241beac0d585a8eb9ed9cdd0b98d0e7be38e1ae1801b687",
  "current_entry_audit": {
    "entryVersion": 86,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2009-09-22",
    "sequenceVersion": 1
  },
  "current_record_sha256": "4f24a50395840d689b2bca6503bac71363002becd9e9b0e170ac85361993f2a0",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 214,
  "current_source_sequence_sha256": "dcaceed6f1d468598241beac0d585a8eb9ed9cdd0b98d0e7be38e1ae1801b687",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 84,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "C6TA59",
  "selected_historical_entry_version": 84,
  "selected_historical_record_sha256": "9ba69ef0f337ff2a30393964c793af5f757c0c52e62614aa37894bfe6ab8f68d",
  "selected_historical_source_sequence_length": 214,
  "selected_historical_source_sequence_sha256": "dcaceed6f1d468598241beac0d585a8eb9ed9cdd0b98d0e7be38e1ae1801b687",
  "selected_historical_version": {
    "accession": "C6TA59",
    "database": "Swiss-Prot",
    "entryVersion": 84,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "HAL3B_SOYBN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6TA59.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"C6TA59\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:27:35.244012+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f24a50395840d689b2bca6503bac71363002becd9e9b0e170ac85361993f2a0",
  "url": "https://rest.uniprot.org/uniprotkb/C6TA59.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6TA59.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":86,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2009-09-22\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:27:35.244012+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f24a50395840d689b2bca6503bac71363002becd9e9b0e170ac85361993f2a0",
  "url": "https://rest.uniprot.org/uniprotkb/C6TA59.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6TA59.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Soybean\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"rosids\",\"fabids\",\"Fabales\",\"Fabaceae\",\"Papilionoideae\",\"50 kb inversion clade\",\"NPAAA clade\",\"indigoferoid/millettioid clade\",\"Phaseoleae\",\"Glycine\",\"Glycine subgen. Soja\"],\"scientificName\":\"Glycine max\",\"synonyms\":[\"Glycine hispida\"],\"taxonId\":3847}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:27:35.244012+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f24a50395840d689b2bca6503bac71363002becd9e9b0e170ac85361993f2a0",
  "url": "https://rest.uniprot.org/uniprotkb/C6TA59.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6TA59.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"Ref.3\",\"source\":\"Reference\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"Ref.4\",\"source\":\"Reference\"}],\"value\":\"Halotolerance protein 3b\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"Ref.3\",\"source\":\"Reference\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"Ref.4\",\"source\":\"Reference\"}],\"value\":\"GmHAL3b\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"value\":\"4.1.1.36\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Phosphopantothenoylcysteine decarboxylase HAL3b\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"PPCDC\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:27:35.244012+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f24a50395840d689b2bca6503bac71363002becd9e9b0e170ac85361993f2a0",
  "url": "https://rest.uniprot.org/uniprotkb/C6TA59.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6TA59.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"name\":\"FMN\"}],\"commentType\":\"COFACTOR\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"value\":\"Binds 1 FMN per subunit.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:27:35.244012+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f24a50395840d689b2bca6503bac71363002becd9e9b0e170ac85361993f2a0",
  "url": "https://rest.uniprot.org/uniprotkb/C6TA59.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6TA59?format=txt&versions=84)

```json
{
  "entry_version": 84,
  "evidence_id": "H1",
  "excerpt": "ID   HAL3B_SOYBN             Reviewed;         214 AA.\nAC   C6TA59;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   22-SEP-2009, sequence version 1.\nDT   28-JAN-2026, entry version 84.\nDE   RecName: Full=Phosphopantothenoylcysteine decarboxylase HAL3b {ECO:0000305};\nDE            Short=PPCDC {ECO:0000305};\nDE            EC=4.1.1.36 {ECO:0000250|UniProtKB:Q9SWE5};\nDE   AltName: Full=Halotolerance protein 3b {ECO:0000303|Ref.3, ECO:0000303|Ref.4};\nDE            Short=GmHAL3b {ECO:0000303|Ref.3, ECO:0000303|Ref.4};\nGN   Name=HAL3B {ECO:0000303|Ref.3, ECO:0000303|Ref.4};\nGN   OrderedLocusNames=Glyma07g082800 {ECO:0000312|EMBL:KRH48322.1};\nOS   Glycine max (Soybean) (Glycine hispida).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   rosids; fabids; Fabales; Fabaceae; Papilionoideae; 50 kb inversion clade;\nOC   NPAAA clade; indigoferoid/millettioid clade; Phaseoleae; Glycine;\nOC   Glycine subgen. Soja.\nOX   NCBI_TaxID=3847;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:37.263279+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-19",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9ba69ef0f337ff2a30393964c793af5f757c0c52e62614aa37894bfe6ab8f68d",
  "url": "https://rest.uniprot.org/unisave/C6TA59?format=txt&versions=84"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6TA59?format=txt&versions=84)

```json
{
  "entry_version": 84,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Phosphopantothenoylcysteine decarboxylase HAL3b {ECO:0000305};\nDE            Short=PPCDC {ECO:0000305};\nDE            EC=4.1.1.36 {ECO:0000250|UniProtKB:Q9SWE5};\nDE   AltName: Full=Halotolerance protein 3b {ECO:0000303|Ref.3, ECO:0000303|Ref.4};\nDE            Short=GmHAL3b {ECO:0000303|Ref.3, ECO:0000303|Ref.4};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:37.263279+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-10",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9ba69ef0f337ff2a30393964c793af5f757c0c52e62614aa37894bfe6ab8f68d",
  "url": "https://rest.uniprot.org/unisave/C6TA59?format=txt&versions=84"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6TA59?format=txt&versions=84)

```json
{
  "entry_version": 84,
  "evidence_id": "H3",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=FMN; Xref=ChEBI:CHEBI:58210;\nCC         Evidence={ECO:0000250|UniProtKB:Q9SWE5};\nCC       Note=Binds 1 FMN per subunit. {ECO:0000250|UniProtKB:Q9SWE5};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:37.263279+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 69-72",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9ba69ef0f337ff2a30393964c793af5f757c0c52e62614aa37894bfe6ab8f68d",
  "url": "https://rest.uniprot.org/unisave/C6TA59?format=txt&versions=84"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 81. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
