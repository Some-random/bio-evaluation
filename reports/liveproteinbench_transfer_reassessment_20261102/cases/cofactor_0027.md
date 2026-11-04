# cofactor_0027

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0027.txt)

**Task:** `cofactor`  
**Expected answer:** **D** — heme

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MASEIYRRLPMELPAQHLLASLALVGALLSVGYLLLRPAKYQLPLPPGPRGLPIIGNLHQAPKEKAWEVYKQWSDRYGPIMSVNNGGMITIIVSSHEVVKNFLEKNNAVFSSRPQLLVLERALYGFTTPALPYGEKWLKHRALRGAVLKPAMAVRYRGLQDLESKQLLRDLLYSEDFTQCMRRQAASLFLGIAYGNRFPEETPEIIDIDQAVAQLGGISESMFQGTGMLREFFPVLKYFPGYDKFLKQLDDVGERLANIYVRRFRDGLSTPAWNWAKEYSKRPEAQGMGELELSFCIGSTYQASLTPYEILRIILLAAICHPEEKARLQKEIDLVVGKDNLPGWEHKDRIQFVQAFIYEALRWHAFSPLGAPRAVSRDIEYKGYFIPKGATLVLNQWAMDHDENVYDNPFTFRPQRWIDNPDLPHVIFGFGLRGCPGQHLARDHLFINTARLFWAFNFGNAYENGKKVELDLDELMQPRGGGSAFNQVPSFKASVIIRSSERRQIVENEWDAVEKDEQKILAEAMPLPE

[Multiple Choices]
A. tungstopterin
B. heme b
C. cob(II)alamin
D. heme
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

> The sequence-matched UniProt record annotates heme as the cofactor. This annotation is similarity-transferred rather than direct experimental evidence for this exact protein, but it is consistent with the protein being a cytochrome P450.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has features characteristic of a cytochrome P450, including a conserved C-terminal cysteine-containing heme-binding motif. P450 family knowledge supports a heme cofactor, distinguishing heme from tungstopterin and cob(II)alamin. That inference does not cleanly separate the generic term “heme” from the more specific “heme b.”


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference from the supplied sequence meaningfully identifies heme as the cofactor without requiring a target-specific database lookup. The overlap between two heme options creates a separate ambiguity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> Heme b is a specific form of heme, so both “heme b” and the broader “heme” can describe the P450 cofactor; the wording does not specify whether the more specific or generic label is intended.


### Important caveats

- The cited UniProt cofactor annotation is supported by transferred evidence (ECO:0000250), not shown here as a direct experimental measurement for this exact protein.
- The reviewer-only protein identity and annotations were not available in the original input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has features characteristic of a cytochrome P450, including a conserved C-terminal cysteine-containing heme-binding motif. P450 family knowledge supports a heme cofactor, distinguishing heme from tungstopterin and cob(II)alamin. That inference does not cleanly separate the generic term “heme” from the more specific “heme b.”",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the supplied sequence meaningfully identifies heme as the cofactor without requiring a target-specific database lookup. The overlap between two heme options creates a separate ambiguity."
  },
  "case_id": "cofactor_0027",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates heme as the cofactor. This annotation is similarity-transferred rather than direct experimental evidence for this exact protein, but it is consistent with the protein being a cytochrome P450."
  },
  "important_caveats": [
    "The cited UniProt cofactor annotation is supported by transferred evidence (ECO:0000250), not shown here as a direct experimental measurement for this exact protein.",
    "The reviewer-only protein identity and annotations were not available in the original input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "Heme b is a specific form of heme, so both “heme b” and the broader “heme” can describe the P450 cofactor; the wording does not specify whether the more specific or generic label is intended."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0027",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates heme as the cofactor. This annotation is similarity-transferred rather than direct experimental evidence for this exact protein, but it is consistent with the protein being a cytochrome P450.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has features characteristic of a cytochrome P450, including a conserved C-terminal cysteine-containing heme-binding motif. P450 family knowledge supports a heme cofactor, distinguishing heme from tungstopterin and cob(II)alamin. That inference does not cleanly separate the generic term “heme” from the more specific “heme b.”",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the supplied sequence meaningfully identifies heme as the cofactor without requiring a target-specific database lookup. The overlap between two heme options creates a separate ambiguity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "Heme b is a specific form of heme, so both “heme b” and the broader “heme” can describe the P450 cofactor; the wording does not specify whether the more specific or generic label is intended."
  },
  "important_caveats": [
    "The cited UniProt cofactor annotation is supported by transferred evidence (ECO:0000250), not shown here as a direct experimental measurement for this exact protein.",
    "The reviewer-only protein identity and annotations were not available in the original input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A2Z5U6I9) annotates this protein as 'Cytochrome P450 monooxygenase okaD' (EC 1.14.99.-) and explicitly lists the cofactor as 'heme' (ChEBI:30413) with evidence code ECO:0000250 (similarity to P04798). The sequence contains the canonical P450 heme-binding motif FGxGxCxG ('FGFGLRGCPGQ') and the conserved P450 region 'FNFGNAYENG', confirming the P450 family assignment. The annotation is by similarity rather than direct experimental determination for this specific protein, but the P450-heme relationship is one of the most well-established facts in biochemistry.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the hallmark P450 heme-binding motif FGxGxCxG (specifically 'FGFGLRGCPGQ' where the Cys ligates the heme iron) and the conserved P450 region 'FNFGNAYENG', plus the overall domain architecture (N-terminal membrane-anchor region, catalytic domain). These features are diagnostic of the cytochrome P450 superfamily, which universally uses heme (iron-protoporphyrin IX) as its prosthetic group. This immediately eliminates tungstopterin (A; cofactor of tungsten-dependent formate dehydrogenases in anaerobic archaea/bacteria) and cob(II)alamin (C; cofactor of B12-dependent mutases and methyltransferases). Between 'heme' (D) and 'heme b' (B): in standard P450 biochemistry and database convention (including UniProt), the cofactor is denoted simply as 'heme.' While 'heme b' (Fe-protoporphyrin IX) is a more chemically specific synonym, the conventional and database-standard term for the P450 cofactor is 'heme,' making D the expected answer. A knowledgeable model recognizing the P450 family would select 'heme' as the standard cofactor designation.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Identification of the P450 family from the conserved FGxGxCxG motif and FNFGNAYENG region is a textbook-level transferable inference. The P450–heme association is universal across the superfamily and requires no protein-specific lookup. The distinction between 'heme' and 'heme b' is resolved by database convention (UniProt annotates P450 cofactor as 'heme'), which is part of standard biochemical knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> Both 'heme' (D) and 'heme b' (B) are scientifically valid descriptions of the P450 prosthetic group (iron-protoporphyrin IX). 'Heme b' is the more chemically specific term (distinguishing from heme a, c, d), while 'heme' is the conventional umbrella term used in P450 literature and UniProt annotations. The question's expected answer follows database convention, but a knowledgeable respondent could reasonably argue that 'heme b' is equally or more precise for P450s. The distinction is one of specificity level rather than correctness.


### Important caveats

- The UniProt cofactor annotation uses ECO:0000250 (similarity to P04798), meaning it is inferred by family-level transfer rather than direct experimental measurement of this specific protein's cofactor.
- The ambiguity between 'heme' and 'heme b' is a question-design issue: both refer to the same molecule (Fe-protoporphyrin IX) in the P450 context, differing only in specificity level.
- The sequence clearly matches the UniProt entry (529 aa, SHA-256 match confirmed), so the family identification applies directly to the supplied sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the hallmark P450 heme-binding motif FGxGxCxG (specifically 'FGFGLRGCPGQ' where the Cys ligates the heme iron) and the conserved P450 region 'FNFGNAYENG', plus the overall domain architecture (N-terminal membrane-anchor region, catalytic domain). These features are diagnostic of the cytochrome P450 superfamily, which universally uses heme (iron-protoporphyrin IX) as its prosthetic group. This immediately eliminates tungstopterin (A; cofactor of tungsten-dependent formate dehydrogenases in anaerobic archaea/bacteria) and cob(II)alamin (C; cofactor of B12-dependent mutases and methyltransferases). Between 'heme' (D) and 'heme b' (B): in standard P450 biochemistry and database convention (including UniProt), the cofactor is denoted simply as 'heme.' While 'heme b' (Fe-protoporphyrin IX) is a more chemically specific synonym, the conventional and database-standard term for the P450 cofactor is 'heme,' making D the expected answer. A knowledgeable model recognizing the P450 family would select 'heme' as the standard cofactor designation.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Identification of the P450 family from the conserved FGxGxCxG motif and FNFGNAYENG region is a textbook-level transferable inference. The P450–heme association is universal across the superfamily and requires no protein-specific lookup. The distinction between 'heme' and 'heme b' is resolved by database convention (UniProt annotates P450 cofactor as 'heme'), which is part of standard biochemical knowledge."
  },
  "case_id": "cofactor_0027",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A2Z5U6I9) annotates this protein as 'Cytochrome P450 monooxygenase okaD' (EC 1.14.99.-) and explicitly lists the cofactor as 'heme' (ChEBI:30413) with evidence code ECO:0000250 (similarity to P04798). The sequence contains the canonical P450 heme-binding motif FGxGxCxG ('FGFGLRGCPGQ') and the conserved P450 region 'FNFGNAYENG', confirming the P450 family assignment. The annotation is by similarity rather than direct experimental determination for this specific protein, but the P450-heme relationship is one of the most well-established facts in biochemistry."
  },
  "important_caveats": [
    "The UniProt cofactor annotation uses ECO:0000250 (similarity to P04798), meaning it is inferred by family-level transfer rather than direct experimental measurement of this specific protein's cofactor.",
    "The ambiguity between 'heme' and 'heme b' is a question-design issue: both refer to the same molecule (Fe-protoporphyrin IX) in the P450 context, differing only in specificity level.",
    "The sequence clearly matches the UniProt entry (529 aa, SHA-256 match confirmed), so the family identification applies directly to the supplied sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "Both 'heme' (D) and 'heme b' (B) are scientifically valid descriptions of the P450 prosthetic group (iron-protoporphyrin IX). 'Heme b' is the more chemically specific term (distinguishing from heme a, c, d), while 'heme' is the conventional umbrella term used in P450 literature and UniProt annotations. The question's expected answer follows database convention, but a knowledgeable respondent could reasonably argue that 'heme b' is equally or more precise for P450s. The distinction is one of specificity level rather than correctness."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0027",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A2Z5U6I9) annotates this protein as 'Cytochrome P450 monooxygenase okaD' (EC 1.14.99.-) and explicitly lists the cofactor as 'heme' (ChEBI:30413) with evidence code ECO:0000250 (similarity to P04798). The sequence contains the canonical P450 heme-binding motif FGxGxCxG ('FGFGLRGCPGQ') and the conserved P450 region 'FNFGNAYENG', confirming the P450 family assignment. The annotation is by similarity rather than direct experimental determination for this specific protein, but the P450-heme relationship is one of the most well-established facts in biochemistry.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the hallmark P450 heme-binding motif FGxGxCxG (specifically 'FGFGLRGCPGQ' where the Cys ligates the heme iron) and the conserved P450 region 'FNFGNAYENG', plus the overall domain architecture (N-terminal membrane-anchor region, catalytic domain). These features are diagnostic of the cytochrome P450 superfamily, which universally uses heme (iron-protoporphyrin IX) as its prosthetic group. This immediately eliminates tungstopterin (A; cofactor of tungsten-dependent formate dehydrogenases in anaerobic archaea/bacteria) and cob(II)alamin (C; cofactor of B12-dependent mutases and methyltransferases). Between 'heme' (D) and 'heme b' (B): in standard P450 biochemistry and database convention (including UniProt), the cofactor is denoted simply as 'heme.' While 'heme b' (Fe-protoporphyrin IX) is a more chemically specific synonym, the conventional and database-standard term for the P450 cofactor is 'heme,' making D the expected answer. A knowledgeable model recognizing the P450 family would select 'heme' as the standard cofactor designation.",
    "missing_item_specific_fact": "",
    "reason": "Identification of the P450 family from the conserved FGxGxCxG motif and FNFGNAYENG region is a textbook-level transferable inference. The P450–heme association is universal across the superfamily and requires no protein-specific lookup. The distinction between 'heme' and 'heme b' is resolved by database convention (UniProt annotates P450 cofactor as 'heme'), which is part of standard biochemical knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "Both 'heme' (D) and 'heme b' (B) are scientifically valid descriptions of the P450 prosthetic group (iron-protoporphyrin IX). 'Heme b' is the more chemically specific term (distinguishing from heme a, c, d), while 'heme' is the conventional umbrella term used in P450 literature and UniProt annotations. The question's expected answer follows database convention, but a knowledgeable respondent could reasonably argue that 'heme b' is equally or more precise for P450s. The distinction is one of specificity level rather than correctness."
  },
  "important_caveats": [
    "The UniProt cofactor annotation uses ECO:0000250 (similarity to P04798), meaning it is inferred by family-level transfer rather than direct experimental measurement of this specific protein's cofactor.",
    "The ambiguity between 'heme' and 'heme b' is a question-design issue: both refer to the same molecule (Fe-protoporphyrin IX) in the P450 context, differing only in specificity level.",
    "The sequence clearly matches the UniProt entry (529 aa, SHA-256 match confirmed), so the family identification applies directly to the supplied sequence."
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
  "benchmark_sequence_length": 529,
  "benchmark_sequence_sha256": "99280cdea8196dec317d2f18830c1825fab94ad5dea0f68ec9b853bab5214ffd",
  "current_entry_audit": {
    "entryVersion": 24,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2018-10-10",
    "sequenceVersion": 1
  },
  "current_record_sha256": "40a05d7310f4d79d3d8cc83398d816d9e515e9003ac315147b668ca6050d9c84",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 529,
  "current_source_sequence_sha256": "99280cdea8196dec317d2f18830c1825fab94ad5dea0f68ec9b853bab5214ffd",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 23,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A2Z5U6I9",
  "selected_historical_entry_version": 23,
  "selected_historical_record_sha256": "325b1f9f1545fcf13c71c1f0abd0af2223be88dff7649f9a3b61a997d58cc16f",
  "selected_historical_source_sequence_length": 529,
  "selected_historical_source_sequence_sha256": "99280cdea8196dec317d2f18830c1825fab94ad5dea0f68ec9b853bab5214ffd",
  "selected_historical_version": {
    "accession": "A0A2Z5U6I9",
    "database": "Swiss-Prot",
    "entryVersion": 23,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "OKAD_PENOH",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5U6I9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A2Z5U6I9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:54.111891+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40a05d7310f4d79d3d8cc83398d816d9e515e9003ac315147b668ca6050d9c84",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2Z5U6I9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5U6I9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":24,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2018-10-10\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:54.111891+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40a05d7310f4d79d3d8cc83398d816d9e515e9003ac315147b668ca6050d9c84",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2Z5U6I9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5U6I9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Penicillium\"],\"scientificName\":\"Penicillium ochrochloron\",\"taxonId\":69780}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:54.111891+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40a05d7310f4d79d3d8cc83398d816d9e515e9003ac315147b668ca6050d9c84",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2Z5U6I9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5U6I9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"28631282\",\"source\":\"PubMed\"}],\"value\":\"Okaramines biosynthesis cluster protein D\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"28631282\",\"source\":\"PubMed\"}],\"value\":\"1.14.99.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"28631282\",\"source\":\"PubMed\"}],\"value\":\"Cytochrome P450 monooxygenase okaD\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:54.111891+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40a05d7310f4d79d3d8cc83398d816d9e515e9003ac315147b668ca6050d9c84",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2Z5U6I9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5U6I9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:30413\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P04798\",\"source\":\"UniProtKB\"}],\"name\":\"heme\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:24:54.111891+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40a05d7310f4d79d3d8cc83398d816d9e515e9003ac315147b668ca6050d9c84",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2Z5U6I9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2Z5U6I9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Lai C.Y.\",\"Lo I.W.\",\"Hewage R.T.\",\"Chen Y.C.\",\"Chen C.T.\",\"Lee C.F.\",\"Lin S.\",\"Tang M.C.\",\"Lin H.C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"28631282\"},{\"database\":\"DOI\",\"id\":\"10.1002/anie.201705501\"}],\"citationType\":\"journal article\",\"firstPage\":\"9478\",\"id\":\"28631282\",\"journal\":\"Angew. Chem. Int. Ed.\",\"lastPage\":\"9482\",\"publicationDate\":\"2017\",\"title\":\"Biosynthesis of Complex Indole Alkaloids: Elucidation of the Concise Pathway of Okaramines.\",\"volume\":\"56\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:24:54.111891+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40a05d7310f4d79d3d8cc83398d816d9e515e9003ac315147b668ca6050d9c84",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2Z5U6I9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2Z5U6I9?format=txt&versions=23)

```json
{
  "entry_version": 23,
  "evidence_id": "H1",
  "excerpt": "ID   OKAD_PENOH              Reviewed;         529 AA.\nAC   A0A2Z5U6I9;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   10-OCT-2018, sequence version 1.\nDT   28-JAN-2026, entry version 23.\nDE   RecName: Full=Cytochrome P450 monooxygenase okaD {ECO:0000303|PubMed:28631282};\nDE            EC=1.14.99.- {ECO:0000269|PubMed:28631282};\nDE   AltName: Full=Okaramines biosynthesis cluster protein D {ECO:0000303|PubMed:28631282};\nGN   Name=okaD {ECO:0000303|PubMed:28631282};\nOS   Penicillium ochrochloron.\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Penicillium.\nOX   NCBI_TaxID=69780;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:57.209412+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "325b1f9f1545fcf13c71c1f0abd0af2223be88dff7649f9a3b61a997d58cc16f",
  "url": "https://rest.uniprot.org/unisave/A0A2Z5U6I9?format=txt&versions=23"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2Z5U6I9?format=txt&versions=23)

```json
{
  "entry_version": 23,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Cytochrome P450 monooxygenase okaD {ECO:0000303|PubMed:28631282};\nDE            EC=1.14.99.- {ECO:0000269|PubMed:28631282};\nDE   AltName: Full=Okaramines biosynthesis cluster protein D {ECO:0000303|PubMed:28631282};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:57.209412+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "325b1f9f1545fcf13c71c1f0abd0af2223be88dff7649f9a3b61a997d58cc16f",
  "url": "https://rest.uniprot.org/unisave/A0A2Z5U6I9?format=txt&versions=23"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2Z5U6I9?format=txt&versions=23)

```json
{
  "entry_version": 23,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, DISRUPTION PHENOTYPE, CATALYTIC ACTIVITY, AND PATHWAY.\nRX   PubMed=28631282; DOI=10.1002/anie.201705501;\nRA   Lai C.Y., Lo I.W., Hewage R.T., Chen Y.C., Chen C.T., Lee C.F., Lin S.,\nRA   Tang M.C., Lin H.C.;\nRT   \"Biosynthesis of Complex Indole Alkaloids: Elucidation of the Concise\nRT   Pathway of Okaramines.\";\nRL   Angew. Chem. Int. Ed. 56:9478-9482(2017).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:57.209412+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 24-31",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "325b1f9f1545fcf13c71c1f0abd0af2223be88dff7649f9a3b61a997d58cc16f",
  "url": "https://rest.uniprot.org/unisave/A0A2Z5U6I9?format=txt&versions=23"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2Z5U6I9?format=txt&versions=23)

```json
{
  "entry_version": 23,
  "evidence_id": "H4",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=heme; Xref=ChEBI:CHEBI:30413;\nCC         Evidence={ECO:0000250|UniProtKB:P04798};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:57.209412+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 67-69",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "325b1f9f1545fcf13c71c1f0abd0af2223be88dff7649f9a3b61a997d58cc16f",
  "url": "https://rest.uniprot.org/unisave/A0A2Z5U6I9?format=txt&versions=23"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 27. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
