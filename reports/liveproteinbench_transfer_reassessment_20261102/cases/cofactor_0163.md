# cofactor_0163

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0163.txt)

**Task:** `cofactor`  
**Expected answer:** **A** — FAD

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTQFKQLSFWSDAEPLECVTRTPEAPNVVTFSFQSPSGALFNHDPGQFVTLELPAPGGPLYRTYTISSAPSRPTALTITVKAQDGSTGTRWMLDNLHKGMRIRAIGPAGKFSIVHHPADKYLFISAGSGITPMVAMTTWLYDSGREPDVVFINCARRPSEIILRDRMELMASRIVGIDLKWVVEEPDPFRSWTGYRGMFNQIMLGLMAQDYLEREVFCCGPEPFMRAVREALAGLGYDMSRYHQESFTAEPGHAEDVPEDVIPDEQNHAEIAFALSGVTTRCSETDTILAAAKAAGLVIPSGCSMGICGTCKVRKTEGQVHMVHNGGITDEDVEDGYILACCSKPLRRVSVEA

[Multiple Choices]
A. FAD
B. Mn(2+)
C. FMN
D. Cu(2+)
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

> The sequence-matched UniProt entry annotates FAD binding, one FAD per subunit. The annotation is transferred from a homolog rather than presented here as direct experimental evidence for this exact protein, so it supports the key with that qualification.

Citations as saved: [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence’s cysteine-rich C-terminal region is consistent with an iron-sulfur electron-transfer domain, while its other region is consistent with a flavoprotein reductase component. In related electron-transfer reductases, that architecture commonly uses FAD, making FAD a meaningful choice over FMN or the standalone Mn(2+) and Cu(2+) alternatives. This is a family-level inference, not proof of the exact cofactor.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable knowledge of flavoprotein reductases and iron-sulfur electron-transfer architectures gives a plausible basis for distinguishing FAD among these choices without knowing this protein’s recorded annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The source also annotates a &#91;2Fe-2S&#93; cluster, but that cofactor is not offered; among the listed choices, the evidence supports FAD.


### Important caveats

- The supplied evidence supports FAD by a homology-based annotation; it does not establish direct experimental verification for this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence’s cysteine-rich C-terminal region is consistent with an iron-sulfur electron-transfer domain, while its other region is consistent with a flavoprotein reductase component. In related electron-transfer reductases, that architecture commonly uses FAD, making FAD a meaningful choice over FMN or the standalone Mn(2+) and Cu(2+) alternatives. This is a family-level inference, not proof of the exact cofactor.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of flavoprotein reductases and iron-sulfur electron-transfer architectures gives a plausible basis for distinguishing FAD among these choices without knowing this protein’s recorded annotation."
  },
  "case_id": "cofactor_0163",
  "expected_answer_check": {
    "evidence_ids": [
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates FAD binding, one FAD per subunit. The annotation is transferred from a homolog rather than presented here as direct experimental evidence for this exact protein, so it supports the key with that qualification."
  },
  "important_caveats": [
    "The supplied evidence supports FAD by a homology-based annotation; it does not establish direct experimental verification for this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The source also annotates a [2Fe-2S] cluster, but that cofactor is not offered; among the listed choices, the evidence supports FAD."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0163",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates FAD binding, one FAD per subunit. The annotation is transferred from a homolog rather than presented here as direct experimental evidence for this exact protein, so it supports the key with that qualification.",
    "evidence_ids": ["C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence’s cysteine-rich C-terminal region is consistent with an iron-sulfur electron-transfer domain, while its other region is consistent with a flavoprotein reductase component. In related electron-transfer reductases, that architecture commonly uses FAD, making FAD a meaningful choice over FMN or the standalone Mn(2+) and Cu(2+) alternatives. This is a family-level inference, not proof of the exact cofactor.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of flavoprotein reductases and iron-sulfur electron-transfer architectures gives a plausible basis for distinguishing FAD among these choices without knowing this protein’s recorded annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The source also annotates a [2Fe-2S] cluster, but that cofactor is not offered; among the listed choices, the evidence supports FAD."
  },
  "important_caveats": [
    "The supplied evidence supports FAD by a homology-based annotation; it does not establish direct experimental verification for this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for Q92ZP8 (Stachydrine N-demethylase reductase subunit Stc4) explicitly lists FAD as a cofactor (Binds 1 FAD per subunit), with evidence code ECO:0000250 (similarity to Q1QYU6). The &#91;2Fe-2S&#93; cluster is also annotated but is not among the answer choices. The expected answer FAD is directly supported by the database annotation.

Citations as saved: [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a clear Rossmann-fold glycine-rich motif 'IGPAGKF' (GxGxxG variant) near the N-terminus, characteristic of FAD/FMN-binding domains. Critically, the overall architecture—approximately 353 residues with an N-terminal flavin-binding domain and a C-terminal region rich in Cys/His residues ('GCSMGICGTCKVRKTEGQVHMVHNG') resembling a Rieske-type &#91;2Fe-2S&#93; cluster binding site—matches the two-domain putidaredoxin reductase/FNR family. This family, which serves as the reductase component of multi-component Rieske-type oxygenase systems, is overwhelmingly FAD-dependent (not FMN). FMN-dependent oxidoreductases (e.g., NADH:flavin oxidoreductase) have different domain architectures and lack the paired FAD+NADPH/FeS arrangement. Mn(2+) and Cu(2+) are metal cofactors of oxidases (SOD, laccase, etc.) and are not found in reductase subunits of oxygenase complexes; the sequence also lacks canonical metal-binding motifs (e.g., HxH for Cu, DxE for Mn). Thus, family-level knowledge of putidaredoxin reductases and the observed Rossmann-fold + Rieske-cluster architecture meaningfully distinguishes FAD (A) from FMN (C), Mn(2+) (B), and Cu(2+) (D).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence itself displays recognizable family features (Rossmann-fold GxGxxG motif, two-domain reductase architecture, Rieske-type Cys/His cluster motif) that, combined with well-established knowledge that putidaredoxin reductase/FNR-family reductase subunits of Rieske-type oxygenase systems are FAD-dependent, allow a knowledgeable model to select FAD over the other three choices without needing to look up this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While FAD and FMN are both flavin cofactors, the two-domain reductase architecture with a Rieske-type cluster motif is strongly diagnostic of the FAD-dependent putidaredoxin reductase family. Mn(2+) and Cu(2+) are clearly inconsistent with a reductase subunit lacking metal-binding motifs. No ambiguity among the four choices is identified.


### Important caveats

- The FAD annotation in UniProt is based on similarity (ECO:0000250 to Q1QYU6), not direct experimental evidence for this exact protein. However, the family-level pattern is well-supported across the putidaredoxin reductase superfamily.
- The &#91;2Fe-2S&#93; cluster is also annotated (via PROSITE-ProRule) but is not among the answer choices, so it does not create ambiguity.
- The sequence-level inference from Rossmann-fold motifs alone cannot strictly distinguish FAD from FMN; the discrimination relies on the broader family-level context (reductase subunit of a Rieske-type oxygenase system).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a clear Rossmann-fold glycine-rich motif 'IGPAGKF' (GxGxxG variant) near the N-terminus, characteristic of FAD/FMN-binding domains. Critically, the overall architecture—approximately 353 residues with an N-terminal flavin-binding domain and a C-terminal region rich in Cys/His residues ('GCSMGICGTCKVRKTEGQVHMVHNG') resembling a Rieske-type [2Fe-2S] cluster binding site—matches the two-domain putidaredoxin reductase/FNR family. This family, which serves as the reductase component of multi-component Rieske-type oxygenase systems, is overwhelmingly FAD-dependent (not FMN). FMN-dependent oxidoreductases (e.g., NADH:flavin oxidoreductase) have different domain architectures and lack the paired FAD+NADPH/FeS arrangement. Mn(2+) and Cu(2+) are metal cofactors of oxidases (SOD, laccase, etc.) and are not found in reductase subunits of oxygenase complexes; the sequence also lacks canonical metal-binding motifs (e.g., HxH for Cu, DxE for Mn). Thus, family-level knowledge of putidaredoxin reductases and the observed Rossmann-fold + Rieske-cluster architecture meaningfully distinguishes FAD (A) from FMN (C), Mn(2+) (B), and Cu(2+) (D).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence itself displays recognizable family features (Rossmann-fold GxGxxG motif, two-domain reductase architecture, Rieske-type Cys/His cluster motif) that, combined with well-established knowledge that putidaredoxin reductase/FNR-family reductase subunits of Rieske-type oxygenase systems are FAD-dependent, allow a knowledgeable model to select FAD over the other three choices without needing to look up this specific protein's annotation."
  },
  "case_id": "cofactor_0163",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for Q92ZP8 (Stachydrine N-demethylase reductase subunit Stc4) explicitly lists FAD as a cofactor (Binds 1 FAD per subunit), with evidence code ECO:0000250 (similarity to Q1QYU6). The [2Fe-2S] cluster is also annotated but is not among the answer choices. The expected answer FAD is directly supported by the database annotation."
  },
  "important_caveats": [
    "The FAD annotation in UniProt is based on similarity (ECO:0000250 to Q1QYU6), not direct experimental evidence for this exact protein. However, the family-level pattern is well-supported across the putidaredoxin reductase superfamily.",
    "The [2Fe-2S] cluster is also annotated (via PROSITE-ProRule) but is not among the answer choices, so it does not create ambiguity.",
    "The sequence-level inference from Rossmann-fold motifs alone cannot strictly distinguish FAD from FMN; the discrimination relies on the broader family-level context (reductase subunit of a Rieske-type oxygenase system)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While FAD and FMN are both flavin cofactors, the two-domain reductase architecture with a Rieske-type cluster motif is strongly diagnostic of the FAD-dependent putidaredoxin reductase family. Mn(2+) and Cu(2+) are clearly inconsistent with a reductase subunit lacking metal-binding motifs. No ambiguity among the four choices is identified."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0163",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for Q92ZP8 (Stachydrine N-demethylase reductase subunit Stc4) explicitly lists FAD as a cofactor (Binds 1 FAD per subunit), with evidence code ECO:0000250 (similarity to Q1QYU6). The [2Fe-2S] cluster is also annotated but is not among the answer choices. The expected answer FAD is directly supported by the database annotation.",
    "evidence_ids": ["C5", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a clear Rossmann-fold glycine-rich motif 'IGPAGKF' (GxGxxG variant) near the N-terminus, characteristic of FAD/FMN-binding domains. Critically, the overall architecture—approximately 353 residues with an N-terminal flavin-binding domain and a C-terminal region rich in Cys/His residues ('GCSMGICGTCKVRKTEGQVHMVHNG') resembling a Rieske-type [2Fe-2S] cluster binding site—matches the two-domain putidaredoxin reductase/FNR family. This family, which serves as the reductase component of multi-component Rieske-type oxygenase systems, is overwhelmingly FAD-dependent (not FMN). FMN-dependent oxidoreductases (e.g., NADH:flavin oxidoreductase) have different domain architectures and lack the paired FAD+NADPH/FeS arrangement. Mn(2+) and Cu(2+) are metal cofactors of oxidases (SOD, laccase, etc.) and are not found in reductase subunits of oxygenase complexes; the sequence also lacks canonical metal-binding motifs (e.g., HxH for Cu, DxE for Mn). Thus, family-level knowledge of putidaredoxin reductases and the observed Rossmann-fold + Rieske-cluster architecture meaningfully distinguishes FAD (A) from FMN (C), Mn(2+) (B), and Cu(2+) (D).",
    "missing_item_specific_fact": "",
    "reason": "The sequence itself displays recognizable family features (Rossmann-fold GxGxxG motif, two-domain reductase architecture, Rieske-type Cys/His cluster motif) that, combined with well-established knowledge that putidaredoxin reductase/FNR-family reductase subunits of Rieske-type oxygenase systems are FAD-dependent, allow a knowledgeable model to select FAD over the other three choices without needing to look up this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While FAD and FMN are both flavin cofactors, the two-domain reductase architecture with a Rieske-type cluster motif is strongly diagnostic of the FAD-dependent putidaredoxin reductase family. Mn(2+) and Cu(2+) are clearly inconsistent with a reductase subunit lacking metal-binding motifs. No ambiguity among the four choices is identified."
  },
  "important_caveats": [
    "The FAD annotation in UniProt is based on similarity (ECO:0000250 to Q1QYU6), not direct experimental evidence for this exact protein. However, the family-level pattern is well-supported across the putidaredoxin reductase superfamily.",
    "The [2Fe-2S] cluster is also annotated (via PROSITE-ProRule) but is not among the answer choices, so it does not create ambiguity.",
    "The sequence-level inference from Rossmann-fold motifs alone cannot strictly distinguish FAD from FMN; the discrimination relies on the broader family-level context (reductase subunit of a Rieske-type oxygenase system)."
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
  "benchmark_sequence_length": 353,
  "benchmark_sequence_sha256": "996a6a20a0a5002391c68773f3d74790bb9b31648f91b717008cfab5b574af88",
  "current_entry_audit": {
    "entryVersion": 139,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2001-12-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "3c1d543d5f9ff4a5c5d6f016184cb8023c255242831a10b322783818813586aa",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 353,
  "current_source_sequence_sha256": "996a6a20a0a5002391c68773f3d74790bb9b31648f91b717008cfab5b574af88",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 138,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q92ZP8",
  "selected_historical_entry_version": 138,
  "selected_historical_record_sha256": "ff322c1a58241eea2d2231f35615abcebd5711f06f1272aee74273503e49f783",
  "selected_historical_source_sequence_length": 353,
  "selected_historical_source_sequence_sha256": "996a6a20a0a5002391c68773f3d74790bb9b31648f91b717008cfab5b574af88",
  "selected_historical_version": {
    "accession": "Q92ZP8",
    "database": "Swiss-Prot",
    "entryVersion": 138,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "STC4_RHIME",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q92ZP8.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q92ZP8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:32:32.632769+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c1d543d5f9ff4a5c5d6f016184cb8023c255242831a10b322783818813586aa",
  "url": "https://rest.uniprot.org/uniprotkb/Q92ZP8.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q92ZP8.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":139,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2001-12-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:32:32.632769+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c1d543d5f9ff4a5c5d6f016184cb8023c255242831a10b322783818813586aa",
  "url": "https://rest.uniprot.org/uniprotkb/Q92ZP8.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q92ZP8.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Ensifer meliloti\",\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Alphaproteobacteria\",\"Hyphomicrobiales\",\"Rhizobiaceae\",\"Sinorhizobium/Ensifer group\",\"Sinorhizobium\"],\"scientificName\":\"Rhizobium meliloti (strain 1021)\",\"synonyms\":[\"Sinorhizobium meliloti\"],\"taxonId\":266834}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:32:32.632769+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c1d543d5f9ff4a5c5d6f016184cb8023c255242831a10b322783818813586aa",
  "url": "https://rest.uniprot.org/uniprotkb/Q92ZP8.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q92ZP8.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"10689197\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000305\",\"id\":\"22224443\",\"source\":\"PubMed\"}],\"value\":\"1.-.-.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Stachydrine N-demethylase reductase subunit Stc4\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:32:32.632769+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c1d543d5f9ff4a5c5d6f016184cb8023c255242831a10b322783818813586aa",
  "url": "https://rest.uniprot.org/uniprotkb/Q92ZP8.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q92ZP8.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:57692\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q1QYU6\",\"source\":\"UniProtKB\"}],\"name\":\"FAD\"}],\"commentType\":\"COFACTOR\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q1QYU6\",\"source\":\"UniProtKB\"}],\"value\":\"Binds 1 FAD per subunit.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:32:32.632769+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c1d543d5f9ff4a5c5d6f016184cb8023c255242831a10b322783818813586aa",
  "url": "https://rest.uniprot.org/uniprotkb/Q92ZP8.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q92ZP8.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:190135\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00465\",\"source\":\"PROSITE-ProRule\"}],\"name\":\"[2Fe-2S] cluster\"}],\"commentType\":\"COFACTOR\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00465\",\"source\":\"PROSITE-ProRule\"}],\"value\":\"Binds 1 2Fe-2S cluster.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:32:32.632769+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c1d543d5f9ff4a5c5d6f016184cb8023c255242831a10b322783818813586aa",
  "url": "https://rest.uniprot.org/uniprotkb/Q92ZP8.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q92ZP8.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Burnet M.W.\",\"Goldmann A.\",\"Message B.\",\"Drong R.\",\"El Amrani A.\",\"Loreau O.\",\"Slightom J.\",\"Tepfer D.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"10689197\"},{\"database\":\"DOI\",\"id\":\"10.1016/s0378-1119(99)00554-5\"}],\"citationType\":\"journal article\",\"firstPage\":\"151\",\"id\":\"10689197\",\"journal\":\"Gene\",\"lastPage\":\"161\",\"publicationDate\":\"2000\",\"title\":\"The stachydrine catabolism region in Sinorhizobium meliloti encodes a multi-enzyme complex similar to the xenobiotic degrading systems in other bacteria.\",\"volume\":\"244\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"Sm2011 / Rm2011 / 2011\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:32:32.632769+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c1d543d5f9ff4a5c5d6f016184cb8023c255242831a10b322783818813586aa",
  "url": "https://rest.uniprot.org/uniprotkb/Q92ZP8.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q92ZP8.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Daughtry K.D.\",\"Xiao Y.\",\"Stoner-Ma D.\",\"Cho E.\",\"Orville A.M.\",\"Liu P.\",\"Allen K.N.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"22224443\"},{\"database\":\"DOI\",\"id\":\"10.1021/ja2111898\"}],\"citationType\":\"journal article\",\"firstPage\":\"2823\",\"id\":\"22224443\",\"journal\":\"J. Am. Chem. Soc.\",\"lastPage\":\"2834\",\"publicationDate\":\"2012\",\"title\":\"Quaternary ammonium oxidative demethylation: X-ray crystallographic, resonance Raman, and UV-visible spectroscopic analysis of a Rieske-type demethylase.\",\"volume\":\"134\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"1021\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:32:32.632769+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c1d543d5f9ff4a5c5d6f016184cb8023c255242831a10b322783818813586aa",
  "url": "https://rest.uniprot.org/uniprotkb/Q92ZP8.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q92ZP8?format=txt&versions=138)

```json
{
  "entry_version": 138,
  "evidence_id": "H1",
  "excerpt": "ID   STC4_RHIME              Reviewed;         353 AA.\nAC   Q92ZP8;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-DEC-2001, sequence version 1.\nDT   28-JAN-2026, entry version 138.\nDE   RecName: Full=Stachydrine N-demethylase reductase subunit Stc4 {ECO:0000305};\nDE            EC=1.-.-.- {ECO:0000305|PubMed:10689197, ECO:0000305|PubMed:22224443};\nGN   Name=stc4 {ECO:0000303|PubMed:10689197};\nGN   OrderedLocusNames=RA0401 {ECO:0000305};\nGN   ORFNames=SMa0752 {ECO:0000312|EMBL:AAK65059.1};\nOS   Rhizobium meliloti (strain 1021) (Ensifer meliloti) (Sinorhizobium\nOS   meliloti).\nOG   Plasmid pSymA (megaplasmid 1).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Alphaproteobacteria;\nOC   Hyphomicrobiales; Rhizobiaceae; Sinorhizobium/Ensifer group; Sinorhizobium.\nOX   NCBI_TaxID=266834;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:34.787250+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ff322c1a58241eea2d2231f35615abcebd5711f06f1272aee74273503e49f783",
  "url": "https://rest.uniprot.org/unisave/Q92ZP8?format=txt&versions=138"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q92ZP8?format=txt&versions=138)

```json
{
  "entry_version": 138,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Stachydrine N-demethylase reductase subunit Stc4 {ECO:0000305};\nDE            EC=1.-.-.- {ECO:0000305|PubMed:10689197, ECO:0000305|PubMed:22224443};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:34.787250+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ff322c1a58241eea2d2231f35615abcebd5711f06f1272aee74273503e49f783",
  "url": "https://rest.uniprot.org/unisave/Q92ZP8?format=txt&versions=138"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q92ZP8?format=txt&versions=138)

```json
{
  "entry_version": 138,
  "evidence_id": "H3",
  "excerpt": "RN   [3]\nRP   FUNCTION, AND DISRUPTION PHENOTYPE.\nRC   STRAIN=Sm2011 / Rm2011 / 2011;\nRX   PubMed=10689197; DOI=10.1016/s0378-1119(99)00554-5;\nRA   Burnet M.W., Goldmann A., Message B., Drong R., El Amrani A., Loreau O.,\nRA   Slightom J., Tepfer D.;\nRT   \"The stachydrine catabolism region in Sinorhizobium meliloti encodes a\nRT   multi-enzyme complex similar to the xenobiotic degrading systems in other\nRT   bacteria.\";\nRL   Gene 244:151-161(2000).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:34.787250+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 45-54",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ff322c1a58241eea2d2231f35615abcebd5711f06f1272aee74273503e49f783",
  "url": "https://rest.uniprot.org/unisave/Q92ZP8?format=txt&versions=138"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q92ZP8?format=txt&versions=138)

```json
{
  "entry_version": 138,
  "evidence_id": "H4",
  "excerpt": "RN   [4]\nRP   FUNCTION.\nRC   STRAIN=1021;\nRX   PubMed=22224443; DOI=10.1021/ja2111898;\nRA   Daughtry K.D., Xiao Y., Stoner-Ma D., Cho E., Orville A.M., Liu P.,\nRA   Allen K.N.;\nRT   \"Quaternary ammonium oxidative demethylation: X-ray crystallographic,\nRT   resonance Raman, and UV-visible spectroscopic analysis of a Rieske-type\nRT   demethylase.\";\nRL   J. Am. Chem. Soc. 134:2823-2834(2012).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:34.787250+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 55-64",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ff322c1a58241eea2d2231f35615abcebd5711f06f1272aee74273503e49f783",
  "url": "https://rest.uniprot.org/unisave/Q92ZP8?format=txt&versions=138"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q92ZP8?format=txt&versions=138)

```json
{
  "entry_version": 138,
  "evidence_id": "H5",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=FAD; Xref=ChEBI:CHEBI:57692;\nCC         Evidence={ECO:0000250|UniProtKB:Q1QYU6};\nCC       Note=Binds 1 FAD per subunit. {ECO:0000250|UniProtKB:Q1QYU6};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:34.787250+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 73-76",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ff322c1a58241eea2d2231f35615abcebd5711f06f1272aee74273503e49f783",
  "url": "https://rest.uniprot.org/unisave/Q92ZP8?format=txt&versions=138"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q92ZP8?format=txt&versions=138)

```json
{
  "entry_version": 138,
  "evidence_id": "H6",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=[2Fe-2S] cluster; Xref=ChEBI:CHEBI:190135;\nCC         Evidence={ECO:0000255|PROSITE-ProRule:PRU00465};\nCC       Note=Binds 1 2Fe-2S cluster. {ECO:0000255|PROSITE-ProRule:PRU00465};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:34.787250+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 77-80",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ff322c1a58241eea2d2231f35615abcebd5711f06f1272aee74273503e49f783",
  "url": "https://rest.uniprot.org/unisave/Q92ZP8?format=txt&versions=138"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 163. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
