# EC_number_0073

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0073.txt)

**Task:** `EC_number`  
**Expected answer:** **C** — 4.1.1.36

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
A. 4.1.1.128
B. 1.14.14.187
C. 4.1.1.36
D. 1.1.1.136
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence.. The inputs provided by the user for this task include:

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

> The exact supplied sequence matches the annotated protein. Its EC 4.1.1.36 assignment and catalytic reaction are recorded, but the evidence is transferred by similarity from another UniProt protein (ECO:0000250), not presented as direct experimental evidence for this sequence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 214-residue sequence is consistent with the compact HAL3/PPCDC family profile, including a cysteine-containing conserved region. Family-level knowledge links PPCDC homologs to phosphopantothenoylcysteine decarboxylation (EC 4.1.1.36), distinguishing C from the other offered enzyme classes and the alternative decarboxylase. This is a transferable homology inference, not a claim of independent experimental verification.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model can use learned sequence-family patterns and the conserved function of PPCDC homologs to favor C without knowing this exact protein's database annotation. The inference is probabilistic, and the supplied evidence itself reflects transfer by similarity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options specify different EC activities; the PPCDC-family inference meaningfully favors EC 4.1.1.36.


### Important caveats

- The reviewer-only annotation supports the key by sequence-matched homology transfer; it does not establish that this particular protein's activity was experimentally measured.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 214-residue sequence is consistent with the compact HAL3/PPCDC family profile, including a cysteine-containing conserved region. Family-level knowledge links PPCDC homologs to phosphopantothenoylcysteine decarboxylation (EC 4.1.1.36), distinguishing C from the other offered enzyme classes and the alternative decarboxylase. This is a transferable homology inference, not a claim of independent experimental verification.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model can use learned sequence-family patterns and the conserved function of PPCDC homologs to favor C without knowing this exact protein's database annotation. The inference is probabilistic, and the supplied evidence itself reflects transfer by similarity."
  },
  "case_id": "EC_number_0073",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the annotated protein. Its EC 4.1.1.36 assignment and catalytic reaction are recorded, but the evidence is transferred by similarity from another UniProt protein (ECO:0000250), not presented as direct experimental evidence for this sequence."
  },
  "important_caveats": [
    "The reviewer-only annotation supports the key by sequence-matched homology transfer; it does not establish that this particular protein's activity was experimentally measured."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options specify different EC activities; the PPCDC-family inference meaningfully favors EC 4.1.1.36."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0073",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the annotated protein. Its EC 4.1.1.36 assignment and catalytic reaction are recorded, but the evidence is transferred by similarity from another UniProt protein (ECO:0000250), not presented as direct experimental evidence for this sequence.",
    "evidence_ids": ["C4", "C5", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 214-residue sequence is consistent with the compact HAL3/PPCDC family profile, including a cysteine-containing conserved region. Family-level knowledge links PPCDC homologs to phosphopantothenoylcysteine decarboxylation (EC 4.1.1.36), distinguishing C from the other offered enzyme classes and the alternative decarboxylase. This is a transferable homology inference, not a claim of independent experimental verification.",
    "missing_item_specific_fact": "",
    "reason": "A model can use learned sequence-family patterns and the conserved function of PPCDC homologs to favor C without knowing this exact protein's database annotation. The inference is probabilistic, and the supplied evidence itself reflects transfer by similarity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options specify different EC activities; the PPCDC-family inference meaningfully favors EC 4.1.1.36."
  },
  "important_caveats": [
    "The reviewer-only annotation supports the key by sequence-matched homology transfer; it does not establish that this particular protein's activity was experimentally measured."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry C6TA59 (HAL3B_SOYBN) annotates this 214-aa soybean protein as Phosphopantothenoylcysteine decarboxylase HAL3b with EC 4.1.1.36. The annotation is based on similarity evidence (ECO:0000250, transferred from Q9SWE5), so it is a computational/similarity inference rather than direct experimental validation for this exact sequence. Nevertheless, the HAL3/PPCDC family catalytic activity (N-&#91;(R)-4-phosphopantothenoyl&#93;-L-cysteine → (R)-4'-phosphopantetheine + CO2) is well-established across the family, and the sequence matches the annotated entry exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence (~214 aa) contains recognizable HAL3/PPCDC domain features: conserved 'LCHCF' and 'SLHFID' motifs, the characteristic cysteine/histidine pattern, and the overall domain architecture of the well-known HAL3 family (Pfam PF02871). The HAL3 family is extensively characterized in the literature as phosphopantothenoylcysteine decarboxylases (EC 4.1.1.36) in the CoA biosynthesis pathway; the 'Halotolerance' name is a historical misnomer. This family-level knowledge allows a model to (1) eliminate EC 1.14.14.187 and EC 1.1.1.136 (oxidoreductases) because the sequence lacks heme-binding FxxGxxxCxG motifs and Rossmann-fold NAD(P)-binding motifs, and (2) distinguish EC 4.1.1.36 from EC 4.1.1.128 by recognizing the specific HAL3/PPCDC family rather than a generic decarboxylase. The HAL3→PPCDC→EC 4.1.1.36 association is a widely taught and published family-level fact, not a fact unique to this single soybean protein.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can use well-established HAL3/PPCDC family biology (conserved domain motifs, historical 'halotolerance' misnomer, CoA pathway role) to identify the family and its EC number. This is transferable family-level knowledge applicable to all HAL3 homologs, not a lookup of this specific protein's database record. The oxidoreductase distractors are further eliminated by absence of characteristic cofactor-binding motifs.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The HAL3/PPCDC family is specifically and unambiguously associated with EC 4.1.1.36. The oxidoreductase options (B, D) lack any supporting sequence features. EC 4.1.1.128 is not a well-known or commonly referenced decarboxylase, making it a weak distractor. No other option is defensible given the HAL3 domain recognition.


### Important caveats

- The UniProt annotation uses evidence code ECO:0000250 (similarity to Q9SWE5), meaning the EC assignment for this exact soybean sequence is transferred by homology rather than directly measured. However, the HAL3/PPCDC family function is broadly validated across multiple organisms.
- EC 4.1.1.128 is an obscure entry; if it were a well-known decarboxylase with a similar fold, the A vs C distinction would be harder. Its obscurity reduces the practical difficulty of the question.
- The reviewer-only evidence (accession C6TA59, organism Glycine max, Swiss-Prot name HAL3B_SOYBN) was not available to the evaluated model; the reasoning above relies solely on sequence features and general HAL3-family biology.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence (~214 aa) contains recognizable HAL3/PPCDC domain features: conserved 'LCHCF' and 'SLHFID' motifs, the characteristic cysteine/histidine pattern, and the overall domain architecture of the well-known HAL3 family (Pfam PF02871). The HAL3 family is extensively characterized in the literature as phosphopantothenoylcysteine decarboxylases (EC 4.1.1.36) in the CoA biosynthesis pathway; the 'Halotolerance' name is a historical misnomer. This family-level knowledge allows a model to (1) eliminate EC 1.14.14.187 and EC 1.1.1.136 (oxidoreductases) because the sequence lacks heme-binding FxxGxxxCxG motifs and Rossmann-fold NAD(P)-binding motifs, and (2) distinguish EC 4.1.1.36 from EC 4.1.1.128 by recognizing the specific HAL3/PPCDC family rather than a generic decarboxylase. The HAL3→PPCDC→EC 4.1.1.36 association is a widely taught and published family-level fact, not a fact unique to this single soybean protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use well-established HAL3/PPCDC family biology (conserved domain motifs, historical 'halotolerance' misnomer, CoA pathway role) to identify the family and its EC number. This is transferable family-level knowledge applicable to all HAL3 homologs, not a lookup of this specific protein's database record. The oxidoreductase distractors are further eliminated by absence of characteristic cofactor-binding motifs."
  },
  "case_id": "EC_number_0073",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry C6TA59 (HAL3B_SOYBN) annotates this 214-aa soybean protein as Phosphopantothenoylcysteine decarboxylase HAL3b with EC 4.1.1.36. The annotation is based on similarity evidence (ECO:0000250, transferred from Q9SWE5), so it is a computational/similarity inference rather than direct experimental validation for this exact sequence. Nevertheless, the HAL3/PPCDC family catalytic activity (N-[(R)-4-phosphopantothenoyl]-L-cysteine → (R)-4'-phosphopantetheine + CO2) is well-established across the family, and the sequence matches the annotated entry exactly."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000250 (similarity to Q9SWE5), meaning the EC assignment for this exact soybean sequence is transferred by homology rather than directly measured. However, the HAL3/PPCDC family function is broadly validated across multiple organisms.",
    "EC 4.1.1.128 is an obscure entry; if it were a well-known decarboxylase with a similar fold, the A vs C distinction would be harder. Its obscurity reduces the practical difficulty of the question.",
    "The reviewer-only evidence (accession C6TA59, organism Glycine max, Swiss-Prot name HAL3B_SOYBN) was not available to the evaluated model; the reasoning above relies solely on sequence features and general HAL3-family biology."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The HAL3/PPCDC family is specifically and unambiguously associated with EC 4.1.1.36. The oxidoreductase options (B, D) lack any supporting sequence features. EC 4.1.1.128 is not a well-known or commonly referenced decarboxylase, making it a weak distractor. No other option is defensible given the HAL3 domain recognition."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0073",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry C6TA59 (HAL3B_SOYBN) annotates this 214-aa soybean protein as Phosphopantothenoylcysteine decarboxylase HAL3b with EC 4.1.1.36. The annotation is based on similarity evidence (ECO:0000250, transferred from Q9SWE5), so it is a computational/similarity inference rather than direct experimental validation for this exact sequence. Nevertheless, the HAL3/PPCDC family catalytic activity (N-[(R)-4-phosphopantothenoyl]-L-cysteine → (R)-4'-phosphopantetheine + CO2) is well-established across the family, and the sequence matches the annotated entry exactly.",
    "evidence_ids": ["C4", "C5", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence (~214 aa) contains recognizable HAL3/PPCDC domain features: conserved 'LCHCF' and 'SLHFID' motifs, the characteristic cysteine/histidine pattern, and the overall domain architecture of the well-known HAL3 family (Pfam PF02871). The HAL3 family is extensively characterized in the literature as phosphopantothenoylcysteine decarboxylases (EC 4.1.1.36) in the CoA biosynthesis pathway; the 'Halotolerance' name is a historical misnomer. This family-level knowledge allows a model to (1) eliminate EC 1.14.14.187 and EC 1.1.1.136 (oxidoreductases) because the sequence lacks heme-binding FxxGxxxCxG motifs and Rossmann-fold NAD(P)-binding motifs, and (2) distinguish EC 4.1.1.36 from EC 4.1.1.128 by recognizing the specific HAL3/PPCDC family rather than a generic decarboxylase. The HAL3→PPCDC→EC 4.1.1.36 association is a widely taught and published family-level fact, not a fact unique to this single soybean protein.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use well-established HAL3/PPCDC family biology (conserved domain motifs, historical 'halotolerance' misnomer, CoA pathway role) to identify the family and its EC number. This is transferable family-level knowledge applicable to all HAL3 homologs, not a lookup of this specific protein's database record. The oxidoreductase distractors are further eliminated by absence of characteristic cofactor-binding motifs."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The HAL3/PPCDC family is specifically and unambiguously associated with EC 4.1.1.36. The oxidoreductase options (B, D) lack any supporting sequence features. EC 4.1.1.128 is not a well-known or commonly referenced decarboxylase, making it a weak distractor. No other option is defensible given the HAL3 domain recognition."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000250 (similarity to Q9SWE5), meaning the EC assignment for this exact soybean sequence is transferred by homology rather than directly measured. However, the HAL3/PPCDC family function is broadly validated across multiple organisms.",
    "EC 4.1.1.128 is an obscure entry; if it were a well-known decarboxylase with a similar fold, the A vs C distinction would be harder. Its obscurity reduces the practical difficulty of the question.",
    "The reviewer-only evidence (accession C6TA59, organism Glycine max, Swiss-Prot name HAL3B_SOYBN) was not available to the evaluated model; the reasoning above relies solely on sequence features and general HAL3-family biology."
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
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:16794\"}}],\"reaction\":{\"ecNumber\":\"4.1.1.36\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9SWE5\",\"source\":\"UniProtKB\"}],\"name\":\"N-[(R)-4-phosphopantothenoyl]-L-cysteine + H(+) = (R)-4'-phosphopantetheine + CO2\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:16793\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16526\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59458\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:61723\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
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
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=N-[(R)-4-phosphopantothenoyl]-L-cysteine + H(+) = (R)-4'-\nCC         phosphopantetheine + CO2; Xref=Rhea:RHEA:16793, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:16526, ChEBI:CHEBI:59458, ChEBI:CHEBI:61723; EC=4.1.1.36;\nCC         Evidence={ECO:0000250|UniProtKB:Q9SWE5};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:16794;\nCC         Evidence={ECO:0000250|UniProtKB:Q9SWE5};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:37.263279+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 62-68",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9ba69ef0f337ff2a30393964c793af5f757c0c52e62614aa37894bfe6ab8f68d",
  "url": "https://rest.uniprot.org/unisave/C6TA59?format=txt&versions=84"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 73. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
