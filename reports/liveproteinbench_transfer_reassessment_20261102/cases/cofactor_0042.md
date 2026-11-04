# cofactor_0042

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0042.txt)

**Task:** `cofactor`  
**Expected answer:** **A** — heme

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MYYRETMLAFVPYLAVFVACYGLVYYRRKRQRLPLPPGPPQLPLVGNLYQIPEMNPWRTYREWHQKYGPIITVKSGLTNTIILGSHKAARDLLDKRNRNYGSRPHFILIGDFIYGGNQTSLLPTGQRWRIHRRILSAFGNVRTSQRYRILYDAESKRLLREILHGGDFFEPFHHYFVRILFALTYGKRVTGSHDPEARDVIEIVDVVLKEASRSSVPEAFPILNSLPGALAPWKRRAQLLFEQHSRLFDNHMNAALANKPWNFCKQALRLKASSEVDRVELNFILGSITEATHSGSMVLGVFIMANILHPDAVRWVQEEIDRVIGPDRLPSFDDMAKLPYLNAYLLEVMRWRPITPGGMPHASFQDDEYMGYHIPKGTTVVANHWSMDFDESVFTDPYEFRPQRWIEDPNLPSIAFGFGTRICPGRHIAESSIFIVAARLLWSFNFDYAYEDGKRQEIDSWNMTQGLDSGPMPFKASFKIRSPKHQEVMDRECGVSDLDIDAILDKIGADFL

[Multiple Choices]
A. heme
B. [2Fe-2S] cluster
C. Fe cation
D. heme b
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

> The sequence is consistent with a cytochrome P450, whose catalytic cofactor is heme. The matched UniProt annotation names heme, but its ECO:0000250 evidence indicates transfer by similarity rather than direct experimental evidence for this protein.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a P450-like N-terminal membrane anchor and a conserved cysteine-containing heme-binding region near its C-terminus. P450 family knowledge supports heme as the cofactor, distinguishing the heme choices from an iron-sulfur cluster or a free iron cation.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference from the sequence meaningfully identifies the heme category without needing the target's database annotation. It does not resolve whether the broad choice “heme” or the more specific “heme b” was intended.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> Heme b is a specific form of heme, and the alternatives do not make clear whether the broad cofactor label or the more specific form is required. Both are defensible for a P450.


### Important caveats

- The source annotation is transferred by similarity, not direct experimental evidence for this protein.
- The sequence-based P450 inference supports a heme cofactor but does not independently distinguish the overlapping heme and heme b choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a P450-like N-terminal membrane anchor and a conserved cysteine-containing heme-binding region near its C-terminus. P450 family knowledge supports heme as the cofactor, distinguishing the heme choices from an iron-sulfur cluster or a free iron cation.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence meaningfully identifies the heme category without needing the target's database annotation. It does not resolve whether the broad choice “heme” or the more specific “heme b” was intended."
  },
  "case_id": "cofactor_0042",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The sequence is consistent with a cytochrome P450, whose catalytic cofactor is heme. The matched UniProt annotation names heme, but its ECO:0000250 evidence indicates transfer by similarity rather than direct experimental evidence for this protein."
  },
  "important_caveats": [
    "The source annotation is transferred by similarity, not direct experimental evidence for this protein.",
    "The sequence-based P450 inference supports a heme cofactor but does not independently distinguish the overlapping heme and heme b choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "Heme b is a specific form of heme, and the alternatives do not make clear whether the broad cofactor label or the more specific form is required. Both are defensible for a P450."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0042",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence is consistent with a cytochrome P450, whose catalytic cofactor is heme. The matched UniProt annotation names heme, but its ECO:0000250 evidence indicates transfer by similarity rather than direct experimental evidence for this protein.",
    "evidence_ids": ["C5", "H4", "C4", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a P450-like N-terminal membrane anchor and a conserved cysteine-containing heme-binding region near its C-terminus. P450 family knowledge supports heme as the cofactor, distinguishing the heme choices from an iron-sulfur cluster or a free iron cation.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence meaningfully identifies the heme category without needing the target's database annotation. It does not resolve whether the broad choice “heme” or the more specific “heme b” was intended."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "Heme b is a specific form of heme, and the alternatives do not make clear whether the broad cofactor label or the more specific form is required. Both are defensible for a P450."
  },
  "important_caveats": [
    "The source annotation is transferred by similarity, not direct experimental evidence for this protein.",
    "The sequence-based P450 inference supports a heme cofactor but does not independently distinguish the overlapping heme and heme b choices."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A7T8F1L2) annotates the cofactor as 'heme' (ChEBI:30413) with evidence code ECO:0000250, indicating similarity-based transfer from P04798 (a well-characterized cytochrome P450). The protein is named 'Cytochrome P450 monooxygenase FrzL' (C4, H2). All P450s universally bind heme as their prosthetic group, so the annotation is well-supported by family-level biochemistry, even though the evidence code is computational transfer rather than direct experimental measurement on this protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the highly conserved P450 heme-binding motif 'FGFGTRICPGRHIA' (residues ~410-425), matching the canonical FxxGxxxCxG signature. The cysteine in this motif is the proximal axial ligand to the heme iron. This is one of the most recognizable sequence signatures in enzymology, shared across all cytochrome P450 superfamily members. A knowledgeable model recognizing this motif can confidently assign heme as the cofactor, eliminating B (&#91;2Fe-2S&#93; cluster, found in ferredoxins and Rieske proteins, not P450s) and C (free Fe cation, not a P450 cofactor). The distinction between A (heme) and D (heme b) is a specificity issue: all P450s use heme b (protoporphyrin IX-Fe), so both terms are scientifically accurate; the question design treats them as mutually exclusive, which is a design flaw rather than a knowledge gap.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The P450 heme-binding motif (FGFGxxxCxG) is a textbook family-level sequence signature. Recognizing it and concluding heme is the cofactor is standard transferable knowledge from the P450 superfamily. This clearly eliminates choices B and C. The A-vs-D ambiguity is a question-design issue (both are correct for P450s), not a lookup requirement.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> All cytochrome P450 enzymes use heme b (protoporphyrin IX-Fe) as their prosthetic group. 'Heme' (A) is the general term used in the UniProt annotation; 'heme b' (D) is the specific chemical identity. Both are scientifically correct descriptions of the P450 cofactor. The question presents them as mutually exclusive, but a knowledgeable model could defensibly select either. The expected answer A matches the exact UniProt annotation string, but D is arguably more precise.


### Important caveats

- The cofactor annotation carries evidence code ECO:0000250 (similarity transfer from P04798), not experimental evidence for this specific protein. However, since the P450 heme requirement is universal across the superfamily, this transfer is extremely reliable.
- The A vs D ambiguity is inherent to the question design: 'heme' and 'heme b' are not truly mutually exclusive for a P450. The benchmark likely expects the exact annotation term 'heme' rather than the more specific 'heme b'.
- The protein is from Cladobotryum sp. (a fungus) and participates in FR901483 biosynthesis, but this organism/function context is not needed to identify the cofactor from the P450 motif.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the highly conserved P450 heme-binding motif 'FGFGTRICPGRHIA' (residues ~410-425), matching the canonical FxxGxxxCxG signature. The cysteine in this motif is the proximal axial ligand to the heme iron. This is one of the most recognizable sequence signatures in enzymology, shared across all cytochrome P450 superfamily members. A knowledgeable model recognizing this motif can confidently assign heme as the cofactor, eliminating B ([2Fe-2S] cluster, found in ferredoxins and Rieske proteins, not P450s) and C (free Fe cation, not a P450 cofactor). The distinction between A (heme) and D (heme b) is a specificity issue: all P450s use heme b (protoporphyrin IX-Fe), so both terms are scientifically accurate; the question design treats them as mutually exclusive, which is a design flaw rather than a knowledge gap.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The P450 heme-binding motif (FGFGxxxCxG) is a textbook family-level sequence signature. Recognizing it and concluding heme is the cofactor is standard transferable knowledge from the P450 superfamily. This clearly eliminates choices B and C. The A-vs-D ambiguity is a question-design issue (both are correct for P450s), not a lookup requirement."
  },
  "case_id": "cofactor_0042",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A7T8F1L2) annotates the cofactor as 'heme' (ChEBI:30413) with evidence code ECO:0000250, indicating similarity-based transfer from P04798 (a well-characterized cytochrome P450). The protein is named 'Cytochrome P450 monooxygenase FrzL' (C4, H2). All P450s universally bind heme as their prosthetic group, so the annotation is well-supported by family-level biochemistry, even though the evidence code is computational transfer rather than direct experimental measurement on this protein."
  },
  "important_caveats": [
    "The cofactor annotation carries evidence code ECO:0000250 (similarity transfer from P04798), not experimental evidence for this specific protein. However, since the P450 heme requirement is universal across the superfamily, this transfer is extremely reliable.",
    "The A vs D ambiguity is inherent to the question design: 'heme' and 'heme b' are not truly mutually exclusive for a P450. The benchmark likely expects the exact annotation term 'heme' rather than the more specific 'heme b'.",
    "The protein is from Cladobotryum sp. (a fungus) and participates in FR901483 biosynthesis, but this organism/function context is not needed to identify the cofactor from the P450 motif."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "All cytochrome P450 enzymes use heme b (protoporphyrin IX-Fe) as their prosthetic group. 'Heme' (A) is the general term used in the UniProt annotation; 'heme b' (D) is the specific chemical identity. Both are scientifically correct descriptions of the P450 cofactor. The question presents them as mutually exclusive, but a knowledgeable model could defensibly select either. The expected answer A matches the exact UniProt annotation string, but D is arguably more precise."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0042",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A7T8F1L2) annotates the cofactor as 'heme' (ChEBI:30413) with evidence code ECO:0000250, indicating similarity-based transfer from P04798 (a well-characterized cytochrome P450). The protein is named 'Cytochrome P450 monooxygenase FrzL' (C4, H2). All P450s universally bind heme as their prosthetic group, so the annotation is well-supported by family-level biochemistry, even though the evidence code is computational transfer rather than direct experimental measurement on this protein.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the highly conserved P450 heme-binding motif 'FGFGTRICPGRHIA' (residues ~410-425), matching the canonical FxxGxxxCxG signature. The cysteine in this motif is the proximal axial ligand to the heme iron. This is one of the most recognizable sequence signatures in enzymology, shared across all cytochrome P450 superfamily members. A knowledgeable model recognizing this motif can confidently assign heme as the cofactor, eliminating B ([2Fe-2S] cluster, found in ferredoxins and Rieske proteins, not P450s) and C (free Fe cation, not a P450 cofactor). The distinction between A (heme) and D (heme b) is a specificity issue: all P450s use heme b (protoporphyrin IX-Fe), so both terms are scientifically accurate; the question design treats them as mutually exclusive, which is a design flaw rather than a knowledge gap.",
    "missing_item_specific_fact": "",
    "reason": "The P450 heme-binding motif (FGFGxxxCxG) is a textbook family-level sequence signature. Recognizing it and concluding heme is the cofactor is standard transferable knowledge from the P450 superfamily. This clearly eliminates choices B and C. The A-vs-D ambiguity is a question-design issue (both are correct for P450s), not a lookup requirement."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "All cytochrome P450 enzymes use heme b (protoporphyrin IX-Fe) as their prosthetic group. 'Heme' (A) is the general term used in the UniProt annotation; 'heme b' (D) is the specific chemical identity. Both are scientifically correct descriptions of the P450 cofactor. The question presents them as mutually exclusive, but a knowledgeable model could defensibly select either. The expected answer A matches the exact UniProt annotation string, but D is arguably more precise."
  },
  "important_caveats": [
    "The cofactor annotation carries evidence code ECO:0000250 (similarity transfer from P04798), not experimental evidence for this specific protein. However, since the P450 heme requirement is universal across the superfamily, this transfer is extremely reliable.",
    "The A vs D ambiguity is inherent to the question design: 'heme' and 'heme b' are not truly mutually exclusive for a P450. The benchmark likely expects the exact annotation term 'heme' rather than the more specific 'heme b'.",
    "The protein is from Cladobotryum sp. (a fungus) and participates in FR901483 biosynthesis, but this organism/function context is not needed to identify the cofactor from the P450 motif."
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
  "benchmark_sequence_length": 512,
  "benchmark_sequence_sha256": "02f6775f75a6bde5b1b4a75830d1b42077d392027632296a27a40235aff1c6f1",
  "current_entry_audit": {
    "entryVersion": 19,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2021-06-02",
    "sequenceVersion": 1
  },
  "current_record_sha256": "f00aff6a17b374aa36f10df5183bfa2190858ab4d3bbd58363dfccc724cff906",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 512,
  "current_source_sequence_sha256": "02f6775f75a6bde5b1b4a75830d1b42077d392027632296a27a40235aff1c6f1",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 17,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A7T8F1L2",
  "selected_historical_entry_version": 17,
  "selected_historical_record_sha256": "f0424c9067ab83539c73301f9b9c22ba80b885df6566cdc9a868e3422019628c",
  "selected_historical_source_sequence_length": 512,
  "selected_historical_source_sequence_sha256": "02f6775f75a6bde5b1b4a75830d1b42077d392027632296a27a40235aff1c6f1",
  "selected_historical_version": {
    "accession": "A0A7T8F1L2",
    "database": "Swiss-Prot",
    "entryVersion": 17,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "FRZL_CLASX",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1L2.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A7T8F1L2\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:50.474399+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f00aff6a17b374aa36f10df5183bfa2190858ab4d3bbd58363dfccc724cff906",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1L2.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1L2.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":19,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2021-06-02\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:50.474399+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f00aff6a17b374aa36f10df5183bfa2190858ab4d3bbd58363dfccc724cff906",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1L2.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1L2.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Hypocreomycetidae\",\"Hypocreales\",\"Hypocreaceae\",\"Cladobotryum\"],\"scientificName\":\"Cladobotryum sp\",\"taxonId\":2040732}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:50.474399+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f00aff6a17b374aa36f10df5183bfa2190858ab4d3bbd58363dfccc724cff906",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1L2.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1L2.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"FR901483 biosynthesis cluster protein L\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"1.-.-.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"Cytochrome P450 monooxygenase FrzL\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:50.474399+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f00aff6a17b374aa36f10df5183bfa2190858ab4d3bbd58363dfccc724cff906",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1L2.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1L2.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:30413\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P04798\",\"source\":\"UniProtKB\"}],\"name\":\"heme\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:24:50.474399+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f00aff6a17b374aa36f10df5183bfa2190858ab4d3bbd58363dfccc724cff906",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1L2.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1L2.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhang Z.\",\"Tamura Y.\",\"Tang M.\",\"Qiao T.\",\"Sato M.\",\"Otsu Y.\",\"Sasamura S.\",\"Taniguchi M.\",\"Watanabe K.\",\"Tang Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33372776\"},{\"database\":\"DOI\",\"id\":\"10.1021/jacs.0c12352\"}],\"citationType\":\"journal article\",\"firstPage\":\"132\",\"id\":\"33372776\",\"journal\":\"J. Am. Chem. Soc.\",\"lastPage\":\"136\",\"publicationDate\":\"2021\",\"title\":\"Biosynthesis of the Immunosuppressant (-)-FR901483.\",\"volume\":\"143\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"11231\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:24:50.474399+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f00aff6a17b374aa36f10df5183bfa2190858ab4d3bbd58363dfccc724cff906",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1L2.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1L2?format=txt&versions=17)

```json
{
  "entry_version": 17,
  "evidence_id": "H1",
  "excerpt": "ID   FRZL_CLASX              Reviewed;         512 AA.\nAC   A0A7T8F1L2;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   02-JUN-2021, sequence version 1.\nDT   28-JAN-2026, entry version 17.\nDE   RecName: Full=Cytochrome P450 monooxygenase FrzL {ECO:0000303|PubMed:33372776};\nDE            EC=1.-.-.- {ECO:0000269|PubMed:33372776};\nDE   AltName: Full=FR901483 biosynthesis cluster protein L {ECO:0000303|PubMed:33372776};\nOS   Cladobotryum sp.\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Hypocreomycetidae; Hypocreales; Hypocreaceae; Cladobotryum.\nOX   NCBI_TaxID=2040732;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:34.520828+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f0424c9067ab83539c73301f9b9c22ba80b885df6566cdc9a868e3422019628c",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1L2?format=txt&versions=17"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1L2?format=txt&versions=17)

```json
{
  "entry_version": 17,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Cytochrome P450 monooxygenase FrzL {ECO:0000303|PubMed:33372776};\nDE            EC=1.-.-.- {ECO:0000269|PubMed:33372776};\nDE   AltName: Full=FR901483 biosynthesis cluster protein L {ECO:0000303|PubMed:33372776};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:34.520828+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f0424c9067ab83539c73301f9b9c22ba80b885df6566cdc9a868e3422019628c",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1L2?format=txt&versions=17"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1L2?format=txt&versions=17)

```json
{
  "entry_version": 17,
  "evidence_id": "H3",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], AND FUNCTION.\nRC   STRAIN=11231;\nRX   PubMed=33372776; DOI=10.1021/jacs.0c12352;\nRA   Zhang Z., Tamura Y., Tang M., Qiao T., Sato M., Otsu Y., Sasamura S.,\nRA   Taniguchi M., Watanabe K., Tang Y.;\nRT   \"Biosynthesis of the Immunosuppressant (-)-FR901483.\";\nRL   J. Am. Chem. Soc. 143:132-136(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:34.520828+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 13-20",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f0424c9067ab83539c73301f9b9c22ba80b885df6566cdc9a868e3422019628c",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1L2?format=txt&versions=17"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1L2?format=txt&versions=17)

```json
{
  "entry_version": 17,
  "evidence_id": "H4",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=heme; Xref=ChEBI:CHEBI:30413;\nCC         Evidence={ECO:0000250|UniProtKB:P04798};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:34.520828+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 51-53",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f0424c9067ab83539c73301f9b9c22ba80b885df6566cdc9a868e3422019628c",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1L2?format=txt&versions=17"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 42. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
