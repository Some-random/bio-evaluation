# EC_number_0136

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0136.txt)

**Task:** `EC_number`  
**Expected answer:** **D** — 2.1.1.5

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MEVNQKWNWDTKPILVKCGGFSSQLAKNVTEKVDGDPLWGSRFDATNPEAVIQTHLDFLRNGADIILTNTYQSSVEGFVKYLGVTRERGVELIQKSVQLAKQAKEQYLSEIGSEAESALPLIMGSIGPYGAYLHDGSEYTGNYADKMSKEELRAWHKTRIEICLAAGVDGLALETLPCLMEAEAVTELVLDNFPDAKFWVSLQCMDEKHMASGENFAEAALSLWRLVQSRKAENRLLGIGLNCVNPLFVTPLLSSLTKVAGSDRIPLVVYSNRGEIYDVEQGDWTGTGEEVVKFVPEWIQLGVRIVGGCCRVYPTDVLAIRKYVDGLNIKP

[Multiple Choices]
A. 2.1.1.393
B. 2.7.8.43
C. 2.1.1.395
D. 2.1.1.5
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

> The supplied sequence exactly matches the sequence in the retrieved UniProt entry, which assigns EC 2.1.1.5 and the reaction transferring a methyl group from betaine to homocysteine. The annotation is supported by transfer from UniProtKB:Q93088 (ECO:0000250), so it is homolog-based evidence rather than direct experimental evidence for this protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with the BHMT family: its length and conserved cysteine-containing region provide family-level clues, and transferable knowledge of this family links it to betaine-dependent homocysteine methylation (EC 2.1.1.5). That family-level inference meaningfully distinguishes D from the other offered methyltransferase ECs and the phosphotransferase option.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognizing the enzyme family from the sequence and applying the known reaction of that family offers a credible inference without needing the exact protein's database record. This is a family-level inference, not proof of the specific protein's activity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The offered choices identify distinct EC activities, and the BHMT-family inference supports D among these alternatives.


### Important caveats

- The reviewer-only annotation is homolog-transferred evidence, not direct experimental confirmation for the supplied protein.
- The sequence match verifies that the annotation concerns this sequence; it does not establish that the author used the same database snapshot.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with the BHMT family: its length and conserved cysteine-containing region provide family-level clues, and transferable knowledge of this family links it to betaine-dependent homocysteine methylation (EC 2.1.1.5). That family-level inference meaningfully distinguishes D from the other offered methyltransferase ECs and the phosphotransferase option.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognizing the enzyme family from the sequence and applying the known reaction of that family offers a credible inference without needing the exact protein's database record. This is a family-level inference, not proof of the specific protein's activity."
  },
  "case_id": "EC_number_0136",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the sequence in the retrieved UniProt entry, which assigns EC 2.1.1.5 and the reaction transferring a methyl group from betaine to homocysteine. The annotation is supported by transfer from UniProtKB:Q93088 (ECO:0000250), so it is homolog-based evidence rather than direct experimental evidence for this protein."
  },
  "important_caveats": [
    "The reviewer-only annotation is homolog-transferred evidence, not direct experimental confirmation for the supplied protein.",
    "The sequence match verifies that the annotation concerns this sequence; it does not establish that the author used the same database snapshot."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered choices identify distinct EC activities, and the BHMT-family inference supports D among these alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0136",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the sequence in the retrieved UniProt entry, which assigns EC 2.1.1.5 and the reaction transferring a methyl group from betaine to homocysteine. The annotation is supported by transfer from UniProtKB:Q93088 (ECO:0000250), so it is homolog-based evidence rather than direct experimental evidence for this protein.",
    "evidence_ids": ["C4", "C5", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with the BHMT family: its length and conserved cysteine-containing region provide family-level clues, and transferable knowledge of this family links it to betaine-dependent homocysteine methylation (EC 2.1.1.5). That family-level inference meaningfully distinguishes D from the other offered methyltransferase ECs and the phosphotransferase option.",
    "missing_item_specific_fact": "",
    "reason": "Recognizing the enzyme family from the sequence and applying the known reaction of that family offers a credible inference without needing the exact protein's database record. This is a family-level inference, not proof of the specific protein's activity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered choices identify distinct EC activities, and the BHMT-family inference supports D among these alternatives."
  },
  "important_caveats": [
    "The reviewer-only annotation is homolog-transferred evidence, not direct experimental confirmation for the supplied protein.",
    "The sequence match verifies that the annotation concerns this sequence; it does not establish that the author used the same database snapshot."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9VJ31 (BHMT_DROME) annotates EC 2.1.1.5 (Betaine-homocysteine S-methyltransferase) with evidence code ECO:0000250 (similarity to human BHMT Q93088). The sequence matches exactly (331 AA, SHA256 confirmed). The catalytic reaction (L-homocysteine + glycine betaine → N,N-dimethylglycine + L-methionine) is consistent with EC 2.1.1.5. Note: the annotation is based on homology transfer, not direct experimental characterization of the Drosophila enzyme.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains features characteristic of the BHMT (Betaine-homocysteine S-methyltransferase) family: (1) multiple cysteine residues (C12 in CGGFSSQ, Cys pairs in GGCCRVY) consistent with zinc coordination, a hallmark of BHMT which is a zinc metalloenzyme; (2) the GSIGPYGAY motif is part of a TIM-barrel fold rather than a Rossmann fold, distinguishing BHMT from typical SAM-dependent methyltransferases; (3) the overall ~331 residue length and glycine-rich composition match BHMT orthologs. Among the choices, 2.7.8.43 (phosphotransferase) is eliminated by the absence of phosphotransferase motifs. Among the three 2.1.1.x options, 2.1.1.393 and 2.1.1.395 are extremely obscure EC numbers for rarely characterized methyltransferases, while 2.1.1.5 is the well-known BHMT. A model recognizing the zinc-binding TIM-barrel architecture (distinctive among methyltransferases) would associate these features with BHMT rather than obscure SAM-dependent or other methyltransferases. The BHMT fold and zinc coordination are transferable knowledge from the extensively characterized human and mammalian BHMT enzymes.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The distinctive BHMT features (zinc-binding cysteines, TIM-barrel fold, lack of SAM-binding Rossmann motif, overall length) are well-established in the literature and transferable from human/mammalian BHMT. These features meaningfully distinguish 2.1.1.5 from a phosphotransferase (2.7.8.43) and from obscure methyltransferase EC numbers (2.1.1.393, 2.1.1.395) that do not share this specific zinc/TIM-barrel architecture. While the exact identity of 2.1.1.393 and 2.1.1.395 is not widely known, their obscurity combined with the positive identification of BHMT features supports a reasonable inference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The 2.7.8.43 option is clearly eliminated by sequence features. The 2.1.1.393 and 2.1.1.395 options are obscure EC numbers unlikely to match the distinctive BHMT zinc/TIM-barrel architecture. Only 2.1.1.5 aligns with the identifiable structural and functional features.


### Important caveats

- The UniProt annotation for EC 2.1.1.5 on Q9VJ31 is based on similarity (ECO:0000250) to human BHMT (Q93088), not direct experimental evidence for the Drosophila enzyme.
- The specific identities of EC 2.1.1.393 and 2.1.1.395 are very obscure; the argument that they do not match BHMT features relies on the assumption that these obscure enzymes do not share the zinc/TIM-barrel architecture, which is reasonable but not independently verified here.
- The GSIGPYGAY motif superficially resembles a Rossmann GxGxxG motif, which could mislead a model toward SAM-dependent methyltransferases; recognizing it as part of a TIM barrel requires BHMT-specific structural knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains features characteristic of the BHMT (Betaine-homocysteine S-methyltransferase) family: (1) multiple cysteine residues (C12 in CGGFSSQ, Cys pairs in GGCCRVY) consistent with zinc coordination, a hallmark of BHMT which is a zinc metalloenzyme; (2) the GSIGPYGAY motif is part of a TIM-barrel fold rather than a Rossmann fold, distinguishing BHMT from typical SAM-dependent methyltransferases; (3) the overall ~331 residue length and glycine-rich composition match BHMT orthologs. Among the choices, 2.7.8.43 (phosphotransferase) is eliminated by the absence of phosphotransferase motifs. Among the three 2.1.1.x options, 2.1.1.393 and 2.1.1.395 are extremely obscure EC numbers for rarely characterized methyltransferases, while 2.1.1.5 is the well-known BHMT. A model recognizing the zinc-binding TIM-barrel architecture (distinctive among methyltransferases) would associate these features with BHMT rather than obscure SAM-dependent or other methyltransferases. The BHMT fold and zinc coordination are transferable knowledge from the extensively characterized human and mammalian BHMT enzymes.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The distinctive BHMT features (zinc-binding cysteines, TIM-barrel fold, lack of SAM-binding Rossmann motif, overall length) are well-established in the literature and transferable from human/mammalian BHMT. These features meaningfully distinguish 2.1.1.5 from a phosphotransferase (2.7.8.43) and from obscure methyltransferase EC numbers (2.1.1.393, 2.1.1.395) that do not share this specific zinc/TIM-barrel architecture. While the exact identity of 2.1.1.393 and 2.1.1.395 is not widely known, their obscurity combined with the positive identification of BHMT features supports a reasonable inference."
  },
  "case_id": "EC_number_0136",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q9VJ31 (BHMT_DROME) annotates EC 2.1.1.5 (Betaine-homocysteine S-methyltransferase) with evidence code ECO:0000250 (similarity to human BHMT Q93088). The sequence matches exactly (331 AA, SHA256 confirmed). The catalytic reaction (L-homocysteine + glycine betaine → N,N-dimethylglycine + L-methionine) is consistent with EC 2.1.1.5. Note: the annotation is based on homology transfer, not direct experimental characterization of the Drosophila enzyme."
  },
  "important_caveats": [
    "The UniProt annotation for EC 2.1.1.5 on Q9VJ31 is based on similarity (ECO:0000250) to human BHMT (Q93088), not direct experimental evidence for the Drosophila enzyme.",
    "The specific identities of EC 2.1.1.393 and 2.1.1.395 are very obscure; the argument that they do not match BHMT features relies on the assumption that these obscure enzymes do not share the zinc/TIM-barrel architecture, which is reasonable but not independently verified here.",
    "The GSIGPYGAY motif superficially resembles a Rossmann GxGxxG motif, which could mislead a model toward SAM-dependent methyltransferases; recognizing it as part of a TIM barrel requires BHMT-specific structural knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The 2.7.8.43 option is clearly eliminated by sequence features. The 2.1.1.393 and 2.1.1.395 options are obscure EC numbers unlikely to match the distinctive BHMT zinc/TIM-barrel architecture. Only 2.1.1.5 aligns with the identifiable structural and functional features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0136",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9VJ31 (BHMT_DROME) annotates EC 2.1.1.5 (Betaine-homocysteine S-methyltransferase) with evidence code ECO:0000250 (similarity to human BHMT Q93088). The sequence matches exactly (331 AA, SHA256 confirmed). The catalytic reaction (L-homocysteine + glycine betaine → N,N-dimethylglycine + L-methionine) is consistent with EC 2.1.1.5. Note: the annotation is based on homology transfer, not direct experimental characterization of the Drosophila enzyme.",
    "evidence_ids": ["C4", "C5", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains features characteristic of the BHMT (Betaine-homocysteine S-methyltransferase) family: (1) multiple cysteine residues (C12 in CGGFSSQ, Cys pairs in GGCCRVY) consistent with zinc coordination, a hallmark of BHMT which is a zinc metalloenzyme; (2) the GSIGPYGAY motif is part of a TIM-barrel fold rather than a Rossmann fold, distinguishing BHMT from typical SAM-dependent methyltransferases; (3) the overall ~331 residue length and glycine-rich composition match BHMT orthologs. Among the choices, 2.7.8.43 (phosphotransferase) is eliminated by the absence of phosphotransferase motifs. Among the three 2.1.1.x options, 2.1.1.393 and 2.1.1.395 are extremely obscure EC numbers for rarely characterized methyltransferases, while 2.1.1.5 is the well-known BHMT. A model recognizing the zinc-binding TIM-barrel architecture (distinctive among methyltransferases) would associate these features with BHMT rather than obscure SAM-dependent or other methyltransferases. The BHMT fold and zinc coordination are transferable knowledge from the extensively characterized human and mammalian BHMT enzymes.",
    "missing_item_specific_fact": "",
    "reason": "The distinctive BHMT features (zinc-binding cysteines, TIM-barrel fold, lack of SAM-binding Rossmann motif, overall length) are well-established in the literature and transferable from human/mammalian BHMT. These features meaningfully distinguish 2.1.1.5 from a phosphotransferase (2.7.8.43) and from obscure methyltransferase EC numbers (2.1.1.393, 2.1.1.395) that do not share this specific zinc/TIM-barrel architecture. While the exact identity of 2.1.1.393 and 2.1.1.395 is not widely known, their obscurity combined with the positive identification of BHMT features supports a reasonable inference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The 2.7.8.43 option is clearly eliminated by sequence features. The 2.1.1.393 and 2.1.1.395 options are obscure EC numbers unlikely to match the distinctive BHMT zinc/TIM-barrel architecture. Only 2.1.1.5 aligns with the identifiable structural and functional features."
  },
  "important_caveats": [
    "The UniProt annotation for EC 2.1.1.5 on Q9VJ31 is based on similarity (ECO:0000250) to human BHMT (Q93088), not direct experimental evidence for the Drosophila enzyme.",
    "The specific identities of EC 2.1.1.393 and 2.1.1.395 are very obscure; the argument that they do not match BHMT features relies on the assumption that these obscure enzymes do not share the zinc/TIM-barrel architecture, which is reasonable but not independently verified here.",
    "The GSIGPYGAY motif superficially resembles a Rossmann GxGxxG motif, which could mislead a model toward SAM-dependent methyltransferases; recognizing it as part of a TIM barrel requires BHMT-specific structural knowledge."
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
  "benchmark_sequence_length": 331,
  "benchmark_sequence_sha256": "6bd107edc9e34f66f2c22eae9672febecece9154557d102db3fa92c074ab48db",
  "current_entry_audit": {
    "entryVersion": 181,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2000-05-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "d9e7ae75552fc6f8c0b82b0818c27c06ccc38e4edbafe213c0d1073bb6cc0f26",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 331,
  "current_source_sequence_sha256": "6bd107edc9e34f66f2c22eae9672febecece9154557d102db3fa92c074ab48db",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 179,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9VJ31",
  "selected_historical_entry_version": 179,
  "selected_historical_record_sha256": "0137a301084f29c9ad250967ed17fe809b86d9f9bf9482cf841c048eb041de62",
  "selected_historical_source_sequence_length": 331,
  "selected_historical_source_sequence_sha256": "6bd107edc9e34f66f2c22eae9672febecece9154557d102db3fa92c074ab48db",
  "selected_historical_version": {
    "accession": "Q9VJ31",
    "database": "Swiss-Prot",
    "entryVersion": 179,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "BHMT_DROME",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ31.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9VJ31\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:33:22.549548+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9e7ae75552fc6f8c0b82b0818c27c06ccc38e4edbafe213c0d1073bb6cc0f26",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VJ31.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ31.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":181,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2000-05-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:33:22.549548+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9e7ae75552fc6f8c0b82b0818c27c06ccc38e4edbafe213c0d1073bb6cc0f26",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VJ31.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ31.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Fruit fly\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000803\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Aparaglossata\",\"Panorpida\",\"Diptera\",\"Brachycera\",\"Muscomorpha\",\"Ephydroidea\",\"Drosophilidae\",\"Drosophila\",\"Sophophora\"],\"scientificName\":\"Drosophila melanogaster\",\"taxonId\":7227}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:33:22.549548+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9e7ae75552fc6f8c0b82b0818c27c06ccc38e4edbafe213c0d1073bb6cc0f26",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VJ31.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ31.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q93088\",\"source\":\"UniProtKB\"}],\"value\":\"2.1.1.5\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"FBgn0032727\",\"source\":\"FlyBase\"}],\"value\":\"Betaine-homocysteine S-methyltransferase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:33:22.549548+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9e7ae75552fc6f8c0b82b0818c27c06ccc38e4edbafe213c0d1073bb6cc0f26",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VJ31.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ31.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q93088\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:22337\"}}],\"reaction\":{\"ecNumber\":\"2.1.1.5\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q93088\",\"source\":\"UniProtKB\"}],\"name\":\"L-homocysteine + glycine betaine = N,N-dimethylglycine + L-methionine\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:22336\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17750\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57844\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58199\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58251\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:33:22.549548+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9e7ae75552fc6f8c0b82b0818c27c06ccc38e4edbafe213c0d1073bb6cc0f26",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VJ31.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VJ31?format=txt&versions=179)

```json
{
  "entry_version": 179,
  "evidence_id": "H1",
  "excerpt": "ID   BHMT_DROME              Reviewed;         331 AA.\nAC   Q9VJ31;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAY-2000, sequence version 1.\nDT   28-JAN-2026, entry version 179.\nDE   RecName: Full=Betaine-homocysteine S-methyltransferase {ECO:0000312|FlyBase:FBgn0032727};\nDE            EC=2.1.1.5 {ECO:0000250|UniProtKB:Q93088};\nGN   Name=Bhmt {ECO:0000312|FlyBase:FBgn0032727};\nGN   ORFNames=CG10623 {ECO:0000312|FlyBase:FBgn0032727};\nOS   Drosophila melanogaster (Fruit fly).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;\nOC   Drosophilidae; Drosophila; Sophophora.\nOX   NCBI_TaxID=7227 {ECO:0000312|Proteomes:UP000000803};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:24.773902+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0137a301084f29c9ad250967ed17fe809b86d9f9bf9482cf841c048eb041de62",
  "url": "https://rest.uniprot.org/unisave/Q9VJ31?format=txt&versions=179"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VJ31?format=txt&versions=179)

```json
{
  "entry_version": 179,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Betaine-homocysteine S-methyltransferase {ECO:0000312|FlyBase:FBgn0032727};\nDE            EC=2.1.1.5 {ECO:0000250|UniProtKB:Q93088};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:24.773902+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0137a301084f29c9ad250967ed17fe809b86d9f9bf9482cf841c048eb041de62",
  "url": "https://rest.uniprot.org/unisave/Q9VJ31?format=txt&versions=179"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VJ31?format=txt&versions=179)

```json
{
  "entry_version": 179,
  "evidence_id": "H3",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-homocysteine + glycine betaine = N,N-dimethylglycine + L-\nCC         methionine; Xref=Rhea:RHEA:22336, ChEBI:CHEBI:17750,\nCC         ChEBI:CHEBI:57844, ChEBI:CHEBI:58199, ChEBI:CHEBI:58251; EC=2.1.1.5;\nCC         Evidence={ECO:0000250|UniProtKB:Q93088};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:22337;\nCC         Evidence={ECO:0000250|UniProtKB:Q93088};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:24.773902+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 109-115",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0137a301084f29c9ad250967ed17fe809b86d9f9bf9482cf841c048eb041de62",
  "url": "https://rest.uniprot.org/unisave/Q9VJ31?format=txt&versions=179"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 136. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
