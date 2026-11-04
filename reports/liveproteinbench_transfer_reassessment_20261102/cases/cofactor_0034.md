# cofactor_0034

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0034.txt)

**Task:** `cofactor`  
**Expected answer:** **B** — FMN

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTSSEPASPEIEQQANSAPRRPRILLAASGSVAAIKFGNLCHSFSEWAEVKAVATRASLHFIDRASLPKDVILYTEEDEWSTWNKVGDSVLHIELRSWADILVIAPLSANTLGKIAGGLCDNLLTCIVRAWDYSKPFFVAPAMNTLMWKNPFTEQHIMSIDELGVSLIPPVTKRLACGDYGNGAMAEPSVIYSTVRLFFESRVQQSGNIVQQPV

[Multiple Choices]
A. FAD
B. FMN
C. Mg(2+)
D. [2Fe-2S] cluster
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

> The sequence-matched UniProt record annotates one FMN per subunit, but explicitly bases this annotation on evidence transferred from a homolog (ECO:0000250), rather than reporting a direct measurement on this protein. This supports FMN as the expected answer, with that qualification.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is compatible with the small HAL3/PPCDC enzyme family. Transferable family knowledge associates phosphopantothenoylcysteine decarboxylases with FMN-dependent catalysis, distinguishing FMN from FAD, Mg2+, and an iron-sulfur cluster among these choices. This is a family-level inference, not a claim of direct experimental confirmation for this particular sequence.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognizing the enzyme family from its sequence and applying the known cofactor pattern of related proteins gives a meaningful basis for choosing FMN without recalling this exact protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The family-level cofactor inference distinguishes FMN from the other offered choices.


### Important caveats

- The supplied evidence supports FMN through a homolog-based annotation; it does not establish direct experimental measurement of FMN binding for this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is compatible with the small HAL3/PPCDC enzyme family. Transferable family knowledge associates phosphopantothenoylcysteine decarboxylases with FMN-dependent catalysis, distinguishing FMN from FAD, Mg2+, and an iron-sulfur cluster among these choices. This is a family-level inference, not a claim of direct experimental confirmation for this particular sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognizing the enzyme family from its sequence and applying the known cofactor pattern of related proteins gives a meaningful basis for choosing FMN without recalling this exact protein's database entry."
  },
  "case_id": "cofactor_0034",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates one FMN per subunit, but explicitly bases this annotation on evidence transferred from a homolog (ECO:0000250), rather than reporting a direct measurement on this protein. This supports FMN as the expected answer, with that qualification."
  },
  "important_caveats": [
    "The supplied evidence supports FMN through a homolog-based annotation; it does not establish direct experimental measurement of FMN binding for this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The family-level cofactor inference distinguishes FMN from the other offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0034",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates one FMN per subunit, but explicitly bases this annotation on evidence transferred from a homolog (ECO:0000250), rather than reporting a direct measurement on this protein. This supports FMN as the expected answer, with that qualification.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is compatible with the small HAL3/PPCDC enzyme family. Transferable family knowledge associates phosphopantothenoylcysteine decarboxylases with FMN-dependent catalysis, distinguishing FMN from FAD, Mg2+, and an iron-sulfur cluster among these choices. This is a family-level inference, not a claim of direct experimental confirmation for this particular sequence.",
    "missing_item_specific_fact": "",
    "reason": "Recognizing the enzyme family from its sequence and applying the known cofactor pattern of related proteins gives a meaningful basis for choosing FMN without recalling this exact protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The family-level cofactor inference distinguishes FMN from the other offered choices."
  },
  "important_caveats": [
    "The supplied evidence supports FMN through a homolog-based annotation; it does not establish direct experimental measurement of FMN binding for this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (both current and historical) lists FMN (CHEBI:58210) as the cofactor with evidence ECO:0000250 (inferred by similarity to Q9SWE5, Arabidopsis HAL3). The protein is identified as Phosphopantothenoylcysteine decarboxylase (PPCDC, EC 4.1.1.36), a well-characterized enzyme in the CoA biosynthesis pathway. FMN dependence is experimentally established across multiple PPCDC homologs (yeast CIS5, human PPCDC, Arabidopsis HAL3, E. coli CoaE). The PubMed reference (32761275) provides experimental catalytic activity data. The expected answer B (FMN) is consistent with the annotation and with well-established family biochemistry.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence (~214 aa) contains motifs consistent with the PPCDC (phosphopantothenoylcysteine decarboxylase, EC 4.1.1.36) family, including conserved SG, RAS, and AP motifs and a fold typical of this small flavoprotein. PPCDC is a universally FMN-dependent enzyme across all characterized homologs (yeast CIS5, human PPCDC, Arabidopsis HAL3, E. coli CoaE). This family-level regularity allows a knowledgeable model to: (1) rule out Mg(2+) and &#91;2Fe-2S&#93; because PPCDC is not a metalloenzyme and does not use iron-sulfur clusters; (2) distinguish FMN from FAD because every characterized PPCDC enzyme binds FMN specifically (mononucleotide form), never FAD. The FMN-vs-FAD distinction is a consistent, well-documented family-level fact transferable from multiple PPCDC homologs studied experimentally.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognition of the PPCDC family from sequence features combined with the well-established, experimentally verified family-level fact that all PPCDC enzymes use FMN (not FAD, not metals, not Fe-S clusters) provides a concrete transferable inference that meaningfully distinguishes option B from A, C, and D. This does not require memorizing this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options (FAD, FMN, Mg2+, &#91;2Fe-2S&#93;) are clearly distinguished by PPCDC family biochemistry. PPCDC is not a metalloenzyme (eliminates C and D), and it specifically uses FMN rather than FAD (eliminates A). No ambiguity remains among the offered choices.


### Important caveats

- The UniProt annotation for this specific entry uses evidence code ECO:0000250 (similarity-based transfer from Arabidopsis HAL3), not direct experimental proof on this exact apple protein. However, the underlying FMN dependence is experimentally confirmed in multiple PPCDC homologs.
- The reviewer-only source identified this as A0A498JQK2 (HAL3_MALDO, Malus domestica), but this identification was not available to the evaluated model; the reasoning relies on family recognition from sequence features alone.
- The sequence is 214 residues, consistent with the canonical PPCDC domain length, supporting family assignment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence (~214 aa) contains motifs consistent with the PPCDC (phosphopantothenoylcysteine decarboxylase, EC 4.1.1.36) family, including conserved SG, RAS, and AP motifs and a fold typical of this small flavoprotein. PPCDC is a universally FMN-dependent enzyme across all characterized homologs (yeast CIS5, human PPCDC, Arabidopsis HAL3, E. coli CoaE). This family-level regularity allows a knowledgeable model to: (1) rule out Mg(2+) and [2Fe-2S] because PPCDC is not a metalloenzyme and does not use iron-sulfur clusters; (2) distinguish FMN from FAD because every characterized PPCDC enzyme binds FMN specifically (mononucleotide form), never FAD. The FMN-vs-FAD distinction is a consistent, well-documented family-level fact transferable from multiple PPCDC homologs studied experimentally.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the PPCDC family from sequence features combined with the well-established, experimentally verified family-level fact that all PPCDC enzymes use FMN (not FAD, not metals, not Fe-S clusters) provides a concrete transferable inference that meaningfully distinguishes option B from A, C, and D. This does not require memorizing this specific protein's database entry."
  },
  "case_id": "cofactor_0034",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (both current and historical) lists FMN (CHEBI:58210) as the cofactor with evidence ECO:0000250 (inferred by similarity to Q9SWE5, Arabidopsis HAL3). The protein is identified as Phosphopantothenoylcysteine decarboxylase (PPCDC, EC 4.1.1.36), a well-characterized enzyme in the CoA biosynthesis pathway. FMN dependence is experimentally established across multiple PPCDC homologs (yeast CIS5, human PPCDC, Arabidopsis HAL3, E. coli CoaE). The PubMed reference (32761275) provides experimental catalytic activity data. The expected answer B (FMN) is consistent with the annotation and with well-established family biochemistry."
  },
  "important_caveats": [
    "The UniProt annotation for this specific entry uses evidence code ECO:0000250 (similarity-based transfer from Arabidopsis HAL3), not direct experimental proof on this exact apple protein. However, the underlying FMN dependence is experimentally confirmed in multiple PPCDC homologs.",
    "The reviewer-only source identified this as A0A498JQK2 (HAL3_MALDO, Malus domestica), but this identification was not available to the evaluated model; the reasoning relies on family recognition from sequence features alone.",
    "The sequence is 214 residues, consistent with the canonical PPCDC domain length, supporting family assignment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options (FAD, FMN, Mg2+, [2Fe-2S]) are clearly distinguished by PPCDC family biochemistry. PPCDC is not a metalloenzyme (eliminates C and D), and it specifically uses FMN rather than FAD (eliminates A). No ambiguity remains among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0034",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (both current and historical) lists FMN (CHEBI:58210) as the cofactor with evidence ECO:0000250 (inferred by similarity to Q9SWE5, Arabidopsis HAL3). The protein is identified as Phosphopantothenoylcysteine decarboxylase (PPCDC, EC 4.1.1.36), a well-characterized enzyme in the CoA biosynthesis pathway. FMN dependence is experimentally established across multiple PPCDC homologs (yeast CIS5, human PPCDC, Arabidopsis HAL3, E. coli CoaE). The PubMed reference (32761275) provides experimental catalytic activity data. The expected answer B (FMN) is consistent with the annotation and with well-established family biochemistry.",
    "evidence_ids": ["C5", "H4", "C4", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence (~214 aa) contains motifs consistent with the PPCDC (phosphopantothenoylcysteine decarboxylase, EC 4.1.1.36) family, including conserved SG, RAS, and AP motifs and a fold typical of this small flavoprotein. PPCDC is a universally FMN-dependent enzyme across all characterized homologs (yeast CIS5, human PPCDC, Arabidopsis HAL3, E. coli CoaE). This family-level regularity allows a knowledgeable model to: (1) rule out Mg(2+) and [2Fe-2S] because PPCDC is not a metalloenzyme and does not use iron-sulfur clusters; (2) distinguish FMN from FAD because every characterized PPCDC enzyme binds FMN specifically (mononucleotide form), never FAD. The FMN-vs-FAD distinction is a consistent, well-documented family-level fact transferable from multiple PPCDC homologs studied experimentally.",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the PPCDC family from sequence features combined with the well-established, experimentally verified family-level fact that all PPCDC enzymes use FMN (not FAD, not metals, not Fe-S clusters) provides a concrete transferable inference that meaningfully distinguishes option B from A, C, and D. This does not require memorizing this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options (FAD, FMN, Mg2+, [2Fe-2S]) are clearly distinguished by PPCDC family biochemistry. PPCDC is not a metalloenzyme (eliminates C and D), and it specifically uses FMN rather than FAD (eliminates A). No ambiguity remains among the offered choices."
  },
  "important_caveats": [
    "The UniProt annotation for this specific entry uses evidence code ECO:0000250 (similarity-based transfer from Arabidopsis HAL3), not direct experimental proof on this exact apple protein. However, the underlying FMN dependence is experimentally confirmed in multiple PPCDC homologs.",
    "The reviewer-only source identified this as A0A498JQK2 (HAL3_MALDO, Malus domestica), but this identification was not available to the evaluated model; the reasoning relies on family recognition from sequence features alone.",
    "The sequence is 214 residues, consistent with the canonical PPCDC domain length, supporting family assignment."
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
  "benchmark_sequence_sha256": "911d51c767ea28d1df72f610e8076aa0e869282e6e5b17fa85fd72483eb8d447",
  "current_entry_audit": {
    "entryVersion": 20,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2019-06-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "2c9613d7efc5e321099105e7df8e04bdd2092654fa07c37207bdc79f66b8d3b2",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 214,
  "current_source_sequence_sha256": "911d51c767ea28d1df72f610e8076aa0e869282e6e5b17fa85fd72483eb8d447",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 19,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A498JQK2",
  "selected_historical_entry_version": 19,
  "selected_historical_record_sha256": "0d82d450cb21391ae574aa004d536baec6b477d61421e803b284844ec1434bbd",
  "selected_historical_source_sequence_length": 214,
  "selected_historical_source_sequence_sha256": "911d51c767ea28d1df72f610e8076aa0e869282e6e5b17fa85fd72483eb8d447",
  "selected_historical_version": {
    "accession": "A0A498JQK2",
    "database": "Swiss-Prot",
    "entryVersion": 19,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "HAL3_MALDO",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A498JQK2.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A498JQK2\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:46.295142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2c9613d7efc5e321099105e7df8e04bdd2092654fa07c37207bdc79f66b8d3b2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A498JQK2.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A498JQK2.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":20,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2019-06-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:46.295142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2c9613d7efc5e321099105e7df8e04bdd2092654fa07c37207bdc79f66b8d3b2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A498JQK2.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A498JQK2.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Apple\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"rosids\",\"fabids\",\"Rosales\",\"Rosaceae\",\"Amygdaloideae\",\"Maleae\",\"Malus\"],\"scientificName\":\"Malus domestica\",\"synonyms\":[\"Pyrus malus\"],\"taxonId\":3750}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:46.295142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2c9613d7efc5e321099105e7df8e04bdd2092654fa07c37207bdc79f66b8d3b2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A498JQK2.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A498JQK2.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32761275\",\"source\":\"PubMed\"}],\"value\":\"Halotolerance protein 3\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32761275\",\"source\":\"PubMed\"}],\"value\":\"MdHAL3\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"32761275\",\"source\":\"PubMed\"}],\"value\":\"4.1.1.36\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Phosphopantothenoylcysteine decarboxylase HAL3\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32761275\",\"source\":\"PubMed\"}],\"value\":\"PPCDC\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:46.295142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2c9613d7efc5e321099105e7df8e04bdd2092654fa07c37207bdc79f66b8d3b2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A498JQK2.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A498JQK2.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"name\":\"FMN\"}],\"commentType\":\"COFACTOR\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"value\":\"Binds 1 FMN per subunit.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-01T06:24:46.295142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2c9613d7efc5e321099105e7df8e04bdd2092654fa07c37207bdc79f66b8d3b2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A498JQK2.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A498JQK2.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Yang S.\",\"Zhang F.\",\"Wang Y.\",\"Xue H.\",\"Jiang Q.\",\"Shi J.\",\"Dai H.\",\"Zhang Z.\",\"Li L.\",\"He P.\",\"Li Y.\",\"Ma Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"32761275\"},{\"database\":\"DOI\",\"id\":\"10.1007/s00299-020-02576-2\"}],\"citationType\":\"journal article\",\"firstPage\":\"1479\",\"id\":\"32761275\",\"journal\":\"Plant Cell Rep.\",\"lastPage\":\"1491\",\"publicationDate\":\"2020\",\"title\":\"MdHAL3, a 4'-phosphopantothenoylcysteine decarboxylase, is involved in the salt tolerance of autotetraploid apple.\",\"volume\":\"39\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"cv. GL-3\"},{\"type\":\"STRAIN\",\"value\":\"cv. Hanfu\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\",\"CATALYTIC ACTIVITY\",\"TISSUE SPECIFICITY\",\"INDUCTION BY SALT STRESS\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:24:46.295142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2c9613d7efc5e321099105e7df8e04bdd2092654fa07c37207bdc79f66b8d3b2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A498JQK2.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H1",
  "excerpt": "ID   HAL3_MALDO              Reviewed;         214 AA.\nAC   A0A498JQK2;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-JUN-2019, sequence version 1.\nDT   28-JAN-2026, entry version 19.\nDE   RecName: Full=Phosphopantothenoylcysteine decarboxylase HAL3 {ECO:0000305};\nDE            Short=PPCDC {ECO:0000303|PubMed:32761275};\nDE            EC=4.1.1.36 {ECO:0000269|PubMed:32761275};\nDE   AltName: Full=Halotolerance protein 3 {ECO:0000303|PubMed:32761275};\nDE            Short=MdHAL3 {ECO:0000303|PubMed:32761275};\nGN   Name=HAL3 {ECO:0000303|PubMed:32761275};\nGN   ORFNames=DVH24_008624 {ECO:0000312|EMBL:RXH96124.1};\nOS   Malus domestica (Apple) (Pyrus malus).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   rosids; fabids; Rosales; Rosaceae; Amygdaloideae; Maleae; Malus.\nOX   NCBI_TaxID=3750;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.570388+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0d82d450cb21391ae574aa004d536baec6b477d61421e803b284844ec1434bbd",
  "url": "https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Phosphopantothenoylcysteine decarboxylase HAL3 {ECO:0000305};\nDE            Short=PPCDC {ECO:0000303|PubMed:32761275};\nDE            EC=4.1.1.36 {ECO:0000269|PubMed:32761275};\nDE   AltName: Full=Halotolerance protein 3 {ECO:0000303|PubMed:32761275};\nDE            Short=MdHAL3 {ECO:0000303|PubMed:32761275};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.570388+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-10",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0d82d450cb21391ae574aa004d536baec6b477d61421e803b284844ec1434bbd",
  "url": "https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, DISRUPTION PHENOTYPE, CATALYTIC ACTIVITY, TISSUE SPECIFICITY,\nRP   INDUCTION BY SALT STRESS, AND SUBCELLULAR LOCATION.\nRC   STRAIN=cv. GL-3, and cv. Hanfu;\nRX   PubMed=32761275; DOI=10.1007/s00299-020-02576-2;\nRA   Yang S., Zhang F., Wang Y., Xue H., Jiang Q., Shi J., Dai H., Zhang Z.,\nRA   Li L., He P., Li Y., Ma Y.;\nRT   \"MdHAL3, a 4'-phosphopantothenoylcysteine decarboxylase, is involved in the\nRT   salt tolerance of autotetraploid apple.\";\nRL   Plant Cell Rep. 39:1479-1491(2020).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.570388+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 28-37",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0d82d450cb21391ae574aa004d536baec6b477d61421e803b284844ec1434bbd",
  "url": "https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H4",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=FMN; Xref=ChEBI:CHEBI:58210;\nCC         Evidence={ECO:0000250|UniProtKB:Q9SWE5};\nCC       Note=Binds 1 FMN per subunit. {ECO:0000250|UniProtKB:Q9SWE5};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.570388+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 51-54",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0d82d450cb21391ae574aa004d536baec6b477d61421e803b284844ec1434bbd",
  "url": "https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 34. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
