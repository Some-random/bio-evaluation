# cofactor_0080

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0080.txt)

**Task:** `cofactor`  
**Expected answer:** **C** — FMN

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAGSEPVRAEGETMAVDAAPRKPRILLAASGSVAAVKFANLCHCFSEWADVRAVSTSASLHFIDRAAMPKDVILYTDDNEWSSWKKLGDSVLHIELRKWADIMVIAPLSANTLGKIAGGLCDNLLTCIVRAWDYSKPFFVAPAMNTFMWNNPFTERHLISIDELGISLIPPVTKRLACGDYGNGAMAEPSTIYSTVRLFYESKAQQGNGDI

[Multiple Choices]
A. Fe cation
B. FAD
C. FMN
D. Co(2+)
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

> The sequence-matched UniProt records annotate this protein as phosphopantothenoylcysteine decarboxylase and identify FMN as its cofactor. The cofactor annotation is transferred by similarity from another UniProt protein (ECO:0000250), so it supports the key but is not direct experimental confirmation for this exact protein.

Citations as saved: [H1](#evidence-h1), [H3](#evidence-h3), [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 211-residue sequence is compatible with the compact PPCDC/HAL3 enzyme family. Transferable family knowledge identifies PPCDCs as FMN-dependent enzymes, making FMN a meaningful choice over Fe, Co(2+), or FAD. The sequence-family assignment may require homology or profile recognition, rather than a simple motif alone.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference can distinguish the offered cofactor choices without knowing this protein's database record. The reviewer-only annotation corroborates that inference but is not needed as a target-specific fact for the judgment.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the PPCDC-family inference, FMN is the distinctively supported option among those offered.


### Important caveats

- The supplied source annotation is evidence by similarity, not reported direct experimental verification for this exact sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 211-residue sequence is compatible with the compact PPCDC/HAL3 enzyme family. Transferable family knowledge identifies PPCDCs as FMN-dependent enzymes, making FMN a meaningful choice over Fe, Co(2+), or FAD. The sequence-family assignment may require homology or profile recognition, rather than a simple motif alone.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference can distinguish the offered cofactor choices without knowing this protein's database record. The reviewer-only annotation corroborates that inference but is not needed as a target-specific fact for the judgment."
  },
  "case_id": "cofactor_0080",
  "expected_answer_check": {
    "evidence_ids": [
      "H1",
      "H3",
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt records annotate this protein as phosphopantothenoylcysteine decarboxylase and identify FMN as its cofactor. The cofactor annotation is transferred by similarity from another UniProt protein (ECO:0000250), so it supports the key but is not direct experimental confirmation for this exact protein."
  },
  "important_caveats": [
    "The supplied source annotation is evidence by similarity, not reported direct experimental verification for this exact sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the PPCDC-family inference, FMN is the distinctively supported option among those offered."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0080",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt records annotate this protein as phosphopantothenoylcysteine decarboxylase and identify FMN as its cofactor. The cofactor annotation is transferred by similarity from another UniProt protein (ECO:0000250), so it supports the key but is not direct experimental confirmation for this exact protein.",
    "evidence_ids": ["H1", "H3", "C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 211-residue sequence is compatible with the compact PPCDC/HAL3 enzyme family. Transferable family knowledge identifies PPCDCs as FMN-dependent enzymes, making FMN a meaningful choice over Fe, Co(2+), or FAD. The sequence-family assignment may require homology or profile recognition, rather than a simple motif alone.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference can distinguish the offered cofactor choices without knowing this protein's database record. The reviewer-only annotation corroborates that inference but is not needed as a target-specific fact for the judgment."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the PPCDC-family inference, FMN is the distinctively supported option among those offered."
  },
  "important_caveats": [
    "The supplied source annotation is evidence by similarity, not reported direct experimental verification for this exact sequence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry C6SZ50 explicitly annotates FMN as the cofactor (CHEBI:58210), stating 'Binds 1 FMN per subunit.' However, the evidence code is ECO:0000250 (similarity), transferred from Q9SWE5 (the yeast CDC21/PPCDC ortholog), making this a computational inference by homology rather than direct experimental measurement on this specific soybean protein. The annotation is nonetheless a valid database record supporting the expected answer.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 211-residue sequence is consistent with the CDC21/PPCDC (phosphopantothenoylcysteine decarboxylase, EC 4.1.1.36) family, a well-characterized group of ~200-250 aa FMN-dependent enzymes involved in coenzyme A biosynthesis. Key sequence features supporting family recognition include: (1) the overall length and compact globular architecture; (2) the N-terminal glycine-rich stretch 'ASGSVAAVK' reminiscent of the FMN-binding loop in CDC21 homologs; (3) the 'TDDNEWSSWKK' region containing conserved acidic residues near the catalytic center; and (4) the 'CHCF' cysteine pair seen in CDC21 orthologs. Once the CDC21/PPCDC family is recognized, the cofactor distinction is a well-established family-level fact: CDC21/PPCDC specifically binds FMN (not FAD). The yeast CDC21 (Q9SWE5) and human CDC21 are experimentally characterized as FMN-dependent. Fe cation and Co(2+) can be eliminated because the sequence lacks canonical metal-coordination motifs (e.g., HxxH, CxxC triads, or DxxH patterns typical of metalloenzymes). The FMN-vs-FAD distinction, while subtle from sequence alone, is resolved by family-level knowledge: the CDC21/PPCDC fold accommodates the smaller FMN molecule, and no adenylate-binding residues or extended FAD-binding domain are present.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the CDC21/PPCDC family from sequence features (length, glycine-rich FMN-binding loop, conserved catalytic acidic residues, cysteine pair) and apply the well-established family-level fact that CDC21/PPCDC uses FMN rather than FAD. The elimination of Fe and Co is straightforward from the absence of metal-binding motifs. This constitutes legitimate transfer from the well-studied yeast and human orthologs.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> FMN and FAD are the only flavin options and are distinguishable at the family level (CDC21/PPCDC uses FMN specifically). Fe and Co lack any supporting sequence motifs. No ambiguity among the offered choices.


### Important caveats

- The UniProt FMN annotation for C6SZ50 is transferred by similarity (ECO:0000250 from Q9SWE5), not derived from direct experimental cofactor-binding assays on the soybean protein.
- Recognition of the CDC21/PPCDC family from a 211-aa sequence without a highly conserved catalytic signature motif requires pattern-level familiarity with this relatively small protein family; a model without such training would struggle to distinguish FMN from FAD.
- The sequence was provided without any functional or organismal context, making family recognition the primary reasoning pathway.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 211-residue sequence is consistent with the CDC21/PPCDC (phosphopantothenoylcysteine decarboxylase, EC 4.1.1.36) family, a well-characterized group of ~200-250 aa FMN-dependent enzymes involved in coenzyme A biosynthesis. Key sequence features supporting family recognition include: (1) the overall length and compact globular architecture; (2) the N-terminal glycine-rich stretch 'ASGSVAAVK' reminiscent of the FMN-binding loop in CDC21 homologs; (3) the 'TDDNEWSSWKK' region containing conserved acidic residues near the catalytic center; and (4) the 'CHCF' cysteine pair seen in CDC21 orthologs. Once the CDC21/PPCDC family is recognized, the cofactor distinction is a well-established family-level fact: CDC21/PPCDC specifically binds FMN (not FAD). The yeast CDC21 (Q9SWE5) and human CDC21 are experimentally characterized as FMN-dependent. Fe cation and Co(2+) can be eliminated because the sequence lacks canonical metal-coordination motifs (e.g., HxxH, CxxC triads, or DxxH patterns typical of metalloenzymes). The FMN-vs-FAD distinction, while subtle from sequence alone, is resolved by family-level knowledge: the CDC21/PPCDC fold accommodates the smaller FMN molecule, and no adenylate-binding residues or extended FAD-binding domain are present.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the CDC21/PPCDC family from sequence features (length, glycine-rich FMN-binding loop, conserved catalytic acidic residues, cysteine pair) and apply the well-established family-level fact that CDC21/PPCDC uses FMN rather than FAD. The elimination of Fe and Co is straightforward from the absence of metal-binding motifs. This constitutes legitimate transfer from the well-studied yeast and human orthologs."
  },
  "case_id": "cofactor_0080",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry C6SZ50 explicitly annotates FMN as the cofactor (CHEBI:58210), stating 'Binds 1 FMN per subunit.' However, the evidence code is ECO:0000250 (similarity), transferred from Q9SWE5 (the yeast CDC21/PPCDC ortholog), making this a computational inference by homology rather than direct experimental measurement on this specific soybean protein. The annotation is nonetheless a valid database record supporting the expected answer."
  },
  "important_caveats": [
    "The UniProt FMN annotation for C6SZ50 is transferred by similarity (ECO:0000250 from Q9SWE5), not derived from direct experimental cofactor-binding assays on the soybean protein.",
    "Recognition of the CDC21/PPCDC family from a 211-aa sequence without a highly conserved catalytic signature motif requires pattern-level familiarity with this relatively small protein family; a model without such training would struggle to distinguish FMN from FAD.",
    "The sequence was provided without any functional or organismal context, making family recognition the primary reasoning pathway."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "FMN and FAD are the only flavin options and are distinguishable at the family level (CDC21/PPCDC uses FMN specifically). Fe and Co lack any supporting sequence motifs. No ambiguity among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0080",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry C6SZ50 explicitly annotates FMN as the cofactor (CHEBI:58210), stating 'Binds 1 FMN per subunit.' However, the evidence code is ECO:0000250 (similarity), transferred from Q9SWE5 (the yeast CDC21/PPCDC ortholog), making this a computational inference by homology rather than direct experimental measurement on this specific soybean protein. The annotation is nonetheless a valid database record supporting the expected answer.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 211-residue sequence is consistent with the CDC21/PPCDC (phosphopantothenoylcysteine decarboxylase, EC 4.1.1.36) family, a well-characterized group of ~200-250 aa FMN-dependent enzymes involved in coenzyme A biosynthesis. Key sequence features supporting family recognition include: (1) the overall length and compact globular architecture; (2) the N-terminal glycine-rich stretch 'ASGSVAAVK' reminiscent of the FMN-binding loop in CDC21 homologs; (3) the 'TDDNEWSSWKK' region containing conserved acidic residues near the catalytic center; and (4) the 'CHCF' cysteine pair seen in CDC21 orthologs. Once the CDC21/PPCDC family is recognized, the cofactor distinction is a well-established family-level fact: CDC21/PPCDC specifically binds FMN (not FAD). The yeast CDC21 (Q9SWE5) and human CDC21 are experimentally characterized as FMN-dependent. Fe cation and Co(2+) can be eliminated because the sequence lacks canonical metal-coordination motifs (e.g., HxxH, CxxC triads, or DxxH patterns typical of metalloenzymes). The FMN-vs-FAD distinction, while subtle from sequence alone, is resolved by family-level knowledge: the CDC21/PPCDC fold accommodates the smaller FMN molecule, and no adenylate-binding residues or extended FAD-binding domain are present.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the CDC21/PPCDC family from sequence features (length, glycine-rich FMN-binding loop, conserved catalytic acidic residues, cysteine pair) and apply the well-established family-level fact that CDC21/PPCDC uses FMN rather than FAD. The elimination of Fe and Co is straightforward from the absence of metal-binding motifs. This constitutes legitimate transfer from the well-studied yeast and human orthologs."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "FMN and FAD are the only flavin options and are distinguishable at the family level (CDC21/PPCDC uses FMN specifically). Fe and Co lack any supporting sequence motifs. No ambiguity among the offered choices."
  },
  "important_caveats": [
    "The UniProt FMN annotation for C6SZ50 is transferred by similarity (ECO:0000250 from Q9SWE5), not derived from direct experimental cofactor-binding assays on the soybean protein.",
    "Recognition of the CDC21/PPCDC family from a 211-aa sequence without a highly conserved catalytic signature motif requires pattern-level familiarity with this relatively small protein family; a model without such training would struggle to distinguish FMN from FAD.",
    "The sequence was provided without any functional or organismal context, making family recognition the primary reasoning pathway."
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
  "benchmark_sequence_length": 211,
  "benchmark_sequence_sha256": "42d591b72a59644dce840573d469e04fad803877d6364e70afe70b2cffcfd7ad",
  "current_entry_audit": {
    "entryVersion": 86,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2009-09-22",
    "sequenceVersion": 1
  },
  "current_record_sha256": "d2226dda9179b81f36d4679262e16bb210a289390044f58410d1a107b4408396",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 211,
  "current_source_sequence_sha256": "42d591b72a59644dce840573d469e04fad803877d6364e70afe70b2cffcfd7ad",
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
  "requested_accession": "C6SZ50",
  "selected_historical_entry_version": 84,
  "selected_historical_record_sha256": "1ce346fa691149ee6e809ca984b0d5dbda18272b4eb904ae9e28b38ca8688212",
  "selected_historical_source_sequence_length": 211,
  "selected_historical_source_sequence_sha256": "42d591b72a59644dce840573d469e04fad803877d6364e70afe70b2cffcfd7ad",
  "selected_historical_version": {
    "accession": "C6SZ50",
    "database": "Swiss-Prot",
    "entryVersion": 84,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "HAL3A_SOYBN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6SZ50.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"C6SZ50\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:27:34.573952+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d2226dda9179b81f36d4679262e16bb210a289390044f58410d1a107b4408396",
  "url": "https://rest.uniprot.org/uniprotkb/C6SZ50.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6SZ50.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":86,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2009-09-22\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:27:34.573952+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d2226dda9179b81f36d4679262e16bb210a289390044f58410d1a107b4408396",
  "url": "https://rest.uniprot.org/uniprotkb/C6SZ50.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6SZ50.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Soybean\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"rosids\",\"fabids\",\"Fabales\",\"Fabaceae\",\"Papilionoideae\",\"50 kb inversion clade\",\"NPAAA clade\",\"indigoferoid/millettioid clade\",\"Phaseoleae\",\"Glycine\",\"Glycine subgen. Soja\"],\"scientificName\":\"Glycine max\",\"synonyms\":[\"Glycine hispida\"],\"taxonId\":3847}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:27:34.573952+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d2226dda9179b81f36d4679262e16bb210a289390044f58410d1a107b4408396",
  "url": "https://rest.uniprot.org/uniprotkb/C6SZ50.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6SZ50.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"Ref.3\",\"source\":\"Reference\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"Ref.4\",\"source\":\"Reference\"}],\"value\":\"Halotolerance protein 3a\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"Ref.3\",\"source\":\"Reference\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"Ref.4\",\"source\":\"Reference\"}],\"value\":\"GmHAL3a\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"value\":\"4.1.1.36\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Phosphopantothenoylcysteine decarboxylase HAL3a\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"PPCDC\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:27:34.573952+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d2226dda9179b81f36d4679262e16bb210a289390044f58410d1a107b4408396",
  "url": "https://rest.uniprot.org/uniprotkb/C6SZ50.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6SZ50.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"name\":\"FMN\"}],\"commentType\":\"COFACTOR\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"value\":\"Binds 1 FMN per subunit.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:27:34.573952+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d2226dda9179b81f36d4679262e16bb210a289390044f58410d1a107b4408396",
  "url": "https://rest.uniprot.org/uniprotkb/C6SZ50.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84)

```json
{
  "entry_version": 84,
  "evidence_id": "H1",
  "excerpt": "ID   HAL3A_SOYBN             Reviewed;         211 AA.\nAC   C6SZ50;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   22-SEP-2009, sequence version 1.\nDT   28-JAN-2026, entry version 84.\nDE   RecName: Full=Phosphopantothenoylcysteine decarboxylase HAL3a {ECO:0000305};\nDE            Short=PPCDC {ECO:0000305};\nDE            EC=4.1.1.36 {ECO:0000250|UniProtKB:Q9SWE5};\nDE   AltName: Full=Halotolerance protein 3a {ECO:0000303|Ref.3, ECO:0000303|Ref.4};\nDE            Short=GmHAL3a {ECO:0000303|Ref.3, ECO:0000303|Ref.4};\nGN   Name=HAL3A {ECO:0000303|Ref.3, ECO:0000303|Ref.4};\nGN   OrderedLocusNames=Glyma03g020900 {ECO:0000312|EMBL:KRH65212.1};\nOS   Glycine max (Soybean) (Glycine hispida).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   rosids; fabids; Fabales; Fabaceae; Papilionoideae; 50 kb inversion clade;\nOC   NPAAA clade; indigoferoid/millettioid clade; Phaseoleae; Glycine;\nOC   Glycine subgen. Soja.\nOX   NCBI_TaxID=3847;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:36.741333+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-19",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1ce346fa691149ee6e809ca984b0d5dbda18272b4eb904ae9e28b38ca8688212",
  "url": "https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84)

```json
{
  "entry_version": 84,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Phosphopantothenoylcysteine decarboxylase HAL3a {ECO:0000305};\nDE            Short=PPCDC {ECO:0000305};\nDE            EC=4.1.1.36 {ECO:0000250|UniProtKB:Q9SWE5};\nDE   AltName: Full=Halotolerance protein 3a {ECO:0000303|Ref.3, ECO:0000303|Ref.4};\nDE            Short=GmHAL3a {ECO:0000303|Ref.3, ECO:0000303|Ref.4};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:36.741333+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-10",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1ce346fa691149ee6e809ca984b0d5dbda18272b4eb904ae9e28b38ca8688212",
  "url": "https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84)

```json
{
  "entry_version": 84,
  "evidence_id": "H3",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=FMN; Xref=ChEBI:CHEBI:58210;\nCC         Evidence={ECO:0000250|UniProtKB:Q9SWE5};\nCC       Note=Binds 1 FMN per subunit. {ECO:0000250|UniProtKB:Q9SWE5};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:36.741333+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 69-72",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1ce346fa691149ee6e809ca984b0d5dbda18272b4eb904ae9e28b38ca8688212",
  "url": "https://rest.uniprot.org/unisave/C6SZ50?format=txt&versions=84"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 80. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
