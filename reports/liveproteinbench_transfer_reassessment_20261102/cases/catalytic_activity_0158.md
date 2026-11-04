# catalytic_activity_0158

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0158.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **C** — 17-O-acetylnorajmaline + NADP(+) = (2R)-1,2-dihydrovomilenine + NADPH + 2 H(+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAGKSPEEQHPVKAYGWAATDSSGILSPFKFSRRATGDHDVRVKILYAGVCHSDLQSARNDMGCFTYPLVPGFETVGTATEVGSKVTKVKVGDKVAVGIMVGSCGKCDECVNDRECYCPEVITSYGRIDHDGTPTYGGFSSETVANEKFVFCFPEKLPMAAGAPLLNAGVSVYSAMRFYGLDKPGMHLGVVGLGGLGHLAVKFAKAFGVKVTVISTSTSKKGEAINDLGADAFLVSTDAEQMQAGSGTLDGILDTVPVVHPIEALLGLLKNHTKLVLVGATMGSFELPILPLGVGRKSVVSTIGGSTKETQEMLDFAAEHDITASVEIIPMDYVNTAMERIEKGDVRYRFVIDIGNTLTPPES

[Multiple Choices]
A. roxarsone (III) + AH2 + O2 = 4-hydroxy-3-nitrocyclohexa-2,5-dien-1-one + arsenite + A + H(+)
B. cephaeline + S-adenosyl-L-methionine = emetine + S-adenosyl-L-homocysteine + H(+)
C. 17-O-acetylnorajmaline + NADP(+) = (2R)-1,2-dihydrovomilenine + NADPH + 2 H(+)
D. beta-L-fucose 1-phosphate + GTP + H(+) = GDP-beta-L-fucose + diphosphate
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt entry annotates the C reaction as catalytic activity and cites evidence coded as experimental (ECO:0000269). This supports the key, though the supplied evidence is a database annotation rather than the underlying experimental report.

Citations as saved: [C5](#evidence-c5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with an NAD(P)-dependent reductase, and transferable knowledge of reductase families makes an NADP+-coupled reduction a good fit. Among these choices, C is the NADP+-dependent reductive reaction; A is an oxygen-dependent oxidation, B is a SAM-dependent methylation, and D is a GTP-dependent sugar-nucleotide formation.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and the sharply contrasting reaction chemistries provide a meaningful basis to favor C without recalling this protein's exact annotation. The sequence alone does not establish the precise alkaloid substrates or products, so the inference is class-level and probabilistic.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The offered reactions represent distinct enzyme chemistries, and only C matches the inferred NAD(P)-dependent reductase activity.


### Important caveats

- The precise substrate and product identities are not independently derivable from the sequence alone.
- The reviewer-only annotations support the expected answer but were not part of the original model input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with an NAD(P)-dependent reductase, and transferable knowledge of reductase families makes an NADP+-coupled reduction a good fit. Among these choices, C is the NADP+-dependent reductive reaction; A is an oxygen-dependent oxidation, B is a SAM-dependent methylation, and D is a GTP-dependent sugar-nucleotide formation.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and the sharply contrasting reaction chemistries provide a meaningful basis to favor C without recalling this protein's exact annotation. The sequence alone does not establish the precise alkaloid substrates or products, so the inference is class-level and probabilistic."
  },
  "case_id": "catalytic_activity_0158",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates the C reaction as catalytic activity and cites evidence coded as experimental (ECO:0000269). This supports the key, though the supplied evidence is a database annotation rather than the underlying experimental report."
  },
  "important_caveats": [
    "The precise substrate and product identities are not independently derivable from the sequence alone.",
    "The reviewer-only annotations support the expected answer but were not part of the original model input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered reactions represent distinct enzyme chemistries, and only C matches the inferred NAD(P)-dependent reductase activity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0158",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates the C reaction as catalytic activity and cites evidence coded as experimental (ECO:0000269). This supports the key, though the supplied evidence is a database annotation rather than the underlying experimental report.",
    "evidence_ids": ["C5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with an NAD(P)-dependent reductase, and transferable knowledge of reductase families makes an NADP+-coupled reduction a good fit. Among these choices, C is the NADP+-dependent reductive reaction; A is an oxygen-dependent oxidation, B is a SAM-dependent methylation, and D is a GTP-dependent sugar-nucleotide formation.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and the sharply contrasting reaction chemistries provide a meaningful basis to favor C without recalling this protein's exact annotation. The sequence alone does not establish the precise alkaloid substrates or products, so the inference is class-level and probabilistic."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered reactions represent distinct enzyme chemistries, and only C matches the inferred NAD(P)-dependent reductase activity."
  },
  "important_caveats": [
    "The precise substrate and product identities are not independently derivable from the sequence alone.",
    "The reviewer-only annotations support the expected answer but were not part of the original model input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A0U3S9Q3 (DHVOR_RAUSE) annotates the exact reaction '17-O-acetylnorajmaline + NADP(+) = (2R)-1,2-dihydrovomilenine + NADPH + 2 H(+)' as the primary catalytic activity (EC 1.3.1.73), supported by experimental evidence codes (ECO:0000269 from PubMed 12391554 and 38212296). The benchmark sequence matches the source entry sequence (SHA-256 match confirmed). The answer text in choice C is identical to the UniProt-annotated reaction.

Citations as saved: [C5](#evidence-c5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains hallmark features of a medium-chain dehydrogenase/reductase (MDR) with NAD(P)-binding capability: the Rossmann-fold motif 'GATMGS' (GxGxxG pattern for NAD(P) binding), a second glycine-rich loop 'GGLGHL', and a zinc-binding cysteine cluster 'GSCGKCDECVNDRECYCPEV' characteristic of zinc-dependent oxidoreductases (EC classes 1.1, 1.3, 1.5). This architecture is extensively documented across hundreds of MDR-family enzymes (alcohol dehydrogenases, enoyl reductases, etc.) and reliably indicates a NADP-dependent oxidoreductase. Among the four choices, only C involves NADP(+)→NADPH as cofactor in a reductase reaction. Choice A uses O2/AH2 (nitroreductase/monooxygenase), B uses SAM (methyltransferase), and D uses GTP (nucleotidyltransferase)—none of which are compatible with the observed Rossmann-fold NAD(P)-binding and zinc-binding motifs. Thus, recognizing the enzyme class from conserved sequence features eliminates three of four options without needing the specific substrate annotation.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The NAD(P)-binding Rossmann fold and zinc-binding cysteine cluster are well-known, transferable sequence features shared across the MDR superfamily. Identifying the enzyme as a NADP-dependent reductase from these motifs is sufficient to select C over A (O2/AH2 cofactor), B (SAM cofactor), and D (GTP cofactor). The specific substrate name (17-O-acetylnorajmaline) is not independently derivable from the sequence, but it is the only option consistent with the enzyme class identified from the sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only choice C is a NADP-dependent reductase reaction. The other three options involve fundamentally different cofactors and enzyme classes incompatible with the observed sequence architecture. No ambiguity among the offered choices.


### Important caveats

- The UniProt entry also annotates a secondary activity (vomilenine reductase, EC 1.5.1.-) for this enzyme, but that reaction is not among the offered choices, so it does not create ambiguity.
- The specific substrate (17-O-acetylnorajmaline) cannot be identified from the sequence alone; the discrimination relies on enzyme class and cofactor identification, which uniquely selects C among the four options.
- The reference paper describes this enzyme as 'CAD-like' (cinnamyl alcohol dehydrogenase-like), which is consistent with the MDR/zinc-dependent NADP-reductase architecture inferred from the sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hallmark features of a medium-chain dehydrogenase/reductase (MDR) with NAD(P)-binding capability: the Rossmann-fold motif 'GATMGS' (GxGxxG pattern for NAD(P) binding), a second glycine-rich loop 'GGLGHL', and a zinc-binding cysteine cluster 'GSCGKCDECVNDRECYCPEV' characteristic of zinc-dependent oxidoreductases (EC classes 1.1, 1.3, 1.5). This architecture is extensively documented across hundreds of MDR-family enzymes (alcohol dehydrogenases, enoyl reductases, etc.) and reliably indicates a NADP-dependent oxidoreductase. Among the four choices, only C involves NADP(+)→NADPH as cofactor in a reductase reaction. Choice A uses O2/AH2 (nitroreductase/monooxygenase), B uses SAM (methyltransferase), and D uses GTP (nucleotidyltransferase)—none of which are compatible with the observed Rossmann-fold NAD(P)-binding and zinc-binding motifs. Thus, recognizing the enzyme class from conserved sequence features eliminates three of four options without needing the specific substrate annotation.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The NAD(P)-binding Rossmann fold and zinc-binding cysteine cluster are well-known, transferable sequence features shared across the MDR superfamily. Identifying the enzyme as a NADP-dependent reductase from these motifs is sufficient to select C over A (O2/AH2 cofactor), B (SAM cofactor), and D (GTP cofactor). The specific substrate name (17-O-acetylnorajmaline) is not independently derivable from the sequence, but it is the only option consistent with the enzyme class identified from the sequence."
  },
  "case_id": "catalytic_activity_0158",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A0U3S9Q3 (DHVOR_RAUSE) annotates the exact reaction '17-O-acetylnorajmaline + NADP(+) = (2R)-1,2-dihydrovomilenine + NADPH + 2 H(+)' as the primary catalytic activity (EC 1.3.1.73), supported by experimental evidence codes (ECO:0000269 from PubMed 12391554 and 38212296). The benchmark sequence matches the source entry sequence (SHA-256 match confirmed). The answer text in choice C is identical to the UniProt-annotated reaction."
  },
  "important_caveats": [
    "The UniProt entry also annotates a secondary activity (vomilenine reductase, EC 1.5.1.-) for this enzyme, but that reaction is not among the offered choices, so it does not create ambiguity.",
    "The specific substrate (17-O-acetylnorajmaline) cannot be identified from the sequence alone; the discrimination relies on enzyme class and cofactor identification, which uniquely selects C among the four options.",
    "The reference paper describes this enzyme as 'CAD-like' (cinnamyl alcohol dehydrogenase-like), which is consistent with the MDR/zinc-dependent NADP-reductase architecture inferred from the sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only choice C is a NADP-dependent reductase reaction. The other three options involve fundamentally different cofactors and enzyme classes incompatible with the observed sequence architecture. No ambiguity among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0158",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A0U3S9Q3 (DHVOR_RAUSE) annotates the exact reaction '17-O-acetylnorajmaline + NADP(+) = (2R)-1,2-dihydrovomilenine + NADPH + 2 H(+)' as the primary catalytic activity (EC 1.3.1.73), supported by experimental evidence codes (ECO:0000269 from PubMed 12391554 and 38212296). The benchmark sequence matches the source entry sequence (SHA-256 match confirmed). The answer text in choice C is identical to the UniProt-annotated reaction.",
    "evidence_ids": ["C5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains hallmark features of a medium-chain dehydrogenase/reductase (MDR) with NAD(P)-binding capability: the Rossmann-fold motif 'GATMGS' (GxGxxG pattern for NAD(P) binding), a second glycine-rich loop 'GGLGHL', and a zinc-binding cysteine cluster 'GSCGKCDECVNDRECYCPEV' characteristic of zinc-dependent oxidoreductases (EC classes 1.1, 1.3, 1.5). This architecture is extensively documented across hundreds of MDR-family enzymes (alcohol dehydrogenases, enoyl reductases, etc.) and reliably indicates a NADP-dependent oxidoreductase. Among the four choices, only C involves NADP(+)→NADPH as cofactor in a reductase reaction. Choice A uses O2/AH2 (nitroreductase/monooxygenase), B uses SAM (methyltransferase), and D uses GTP (nucleotidyltransferase)—none of which are compatible with the observed Rossmann-fold NAD(P)-binding and zinc-binding motifs. Thus, recognizing the enzyme class from conserved sequence features eliminates three of four options without needing the specific substrate annotation.",
    "missing_item_specific_fact": "",
    "reason": "The NAD(P)-binding Rossmann fold and zinc-binding cysteine cluster are well-known, transferable sequence features shared across the MDR superfamily. Identifying the enzyme as a NADP-dependent reductase from these motifs is sufficient to select C over A (O2/AH2 cofactor), B (SAM cofactor), and D (GTP cofactor). The specific substrate name (17-O-acetylnorajmaline) is not independently derivable from the sequence, but it is the only option consistent with the enzyme class identified from the sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only choice C is a NADP-dependent reductase reaction. The other three options involve fundamentally different cofactors and enzyme classes incompatible with the observed sequence architecture. No ambiguity among the offered choices."
  },
  "important_caveats": [
    "The UniProt entry also annotates a secondary activity (vomilenine reductase, EC 1.5.1.-) for this enzyme, but that reaction is not among the offered choices, so it does not create ambiguity.",
    "The specific substrate (17-O-acetylnorajmaline) cannot be identified from the sequence alone; the discrimination relies on enzyme class and cofactor identification, which uniquely selects C among the four options.",
    "The reference paper describes this enzyme as 'CAD-like' (cinnamyl alcohol dehydrogenase-like), which is consistent with the MDR/zinc-dependent NADP-reductase architecture inferred from the sequence."
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
  "benchmark_sequence_length": 363,
  "benchmark_sequence_sha256": "9941adf9dcda8a9a678cb7bae23ca23f59278208d6b5e98e8fa474f1a99f1441",
  "current_entry_audit": {
    "entryVersion": 34,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2016-03-16",
    "sequenceVersion": 1
  },
  "current_record_sha256": "ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 363,
  "current_source_sequence_sha256": "9941adf9dcda8a9a678cb7bae23ca23f59278208d6b5e98e8fa474f1a99f1441",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 32,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A0U3S9Q3",
  "selected_historical_entry_version": 32,
  "selected_historical_record_sha256": "d736edca11739beb62ca2d5765f93a0db6fdd42ef122f9711acacccadcaabc22",
  "selected_historical_source_sequence_length": 363,
  "selected_historical_source_sequence_sha256": "9941adf9dcda8a9a678cb7bae23ca23f59278208d6b5e98e8fa474f1a99f1441",
  "selected_historical_version": {
    "accession": "A0A0U3S9Q3",
    "database": "Swiss-Prot",
    "entryVersion": 32,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DHVOR_RAUSE",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A0U3S9Q3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:41.228210+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":34,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2016-03-16\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:41.228210+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Serpentine wood\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Apocynaceae\",\"Rauvolfioideae\",\"Vinceae\",\"Rauvolfiinae\",\"Rauvolfia\"],\"scientificName\":\"Rauvolfia serpentina\",\"synonyms\":[\"Ophioxylon serpentinum\"],\"taxonId\":4060}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:41.228210+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"26715562\",\"source\":\"PubMed\"}],\"value\":\"Protein RR4\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"26715562\",\"source\":\"PubMed\"}],\"value\":\"RsRR4\"}]},{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26715562\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"1.5.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"26715562\",\"source\":\"PubMed\"}],\"value\":\"Vomilenine reductase 2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"26715562\",\"source\":\"PubMed\"}],\"value\":\"RsVR2\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"12391554\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"1.3.1.73\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"26715562\",\"source\":\"PubMed\"}],\"value\":\"1,2-Dihydrovomilenine reductase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"26715562\",\"source\":\"PubMed\"}],\"value\":\"RsDHVR\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:41.228210+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"right-to-left\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"12391554\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:12322\"}}],\"reaction\":{\"ecNumber\":\"1.3.1.73\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"12391554\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"name\":\"17-O-acetylnorajmaline + NADP(+) = (2R)-1,2-dihydrovomilenine + NADPH + 2 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:12320\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17372\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57783\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:77725\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:24:41.228210+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"right-to-left\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26715562\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:79637\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26715562\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"name\":\"(20S)-19,20-dihydrovomilenine + NADP(+) = vomilenine + NADPH + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:79635\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16408\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57783\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:230482\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-01T06:24:41.228210+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Geissler M.\",\"Burghard M.\",\"Volk J.\",\"Staniek A.\",\"Warzecha H.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"26715562\"},{\"database\":\"DOI\",\"id\":\"10.1007/s00425-015-2446-6\"}],\"citationType\":\"journal article\",\"firstPage\":\"813\",\"id\":\"26715562\",\"journal\":\"Planta\",\"lastPage\":\"824\",\"publicationDate\":\"2016\",\"title\":\"A novel cinnamyl alcohol dehydrogenase (CAD)-like reductase contributes to the structural diversity of monoterpenoid indole alkaloids in Rauvolfia.\",\"volume\":\"243\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"ALW82981.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA] (ISOFORM 1)\",\"PROTEIN SEQUENCE OF 5-13 AND 298-308\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\",\"TISSUE SPECIFICITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:24:41.228210+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Guo J.\",\"Gao D.\",\"Lian J.\",\"Qu Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38212296\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-024-44797-z\"}],\"citationType\":\"journal article\",\"firstPage\":\"457\",\"id\":\"38212296\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"457\",\"publicationDate\":\"2024\",\"title\":\"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.\",\"volume\":\"15\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"WKU61918.1\",\"source\":\"EMBL\"}],\"referenceNumber\":2,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA] (ISOFORM 2)\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\",\"TISSUE SPECIFICITY\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:24:41.228210+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Gao S.\",\"von Schumann G.\",\"Stoeckigt J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"12391554\"},{\"database\":\"DOI\",\"id\":\"10.1055/s-2002-34935\"}],\"citationType\":\"journal article\",\"firstPage\":\"906\",\"id\":\"12391554\",\"journal\":\"Planta Med.\",\"lastPage\":\"911\",\"publicationDate\":\"2002\",\"title\":\"A newly-detected reductase from Rauvolfia closes a gap in the biosynthesis of the antiarrhythmic alkaloid ajmaline.\",\"volume\":\"68\"},\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-01T06:24:41.228210+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H1",
  "excerpt": "ID   DHVOR_RAUSE             Reviewed;         363 AA.\nAC   A0A0U3S9Q3;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   16-MAR-2016, sequence version 1.\nDT   28-JAN-2026, entry version 32.\nDE   RecName: Full=1,2-Dihydrovomilenine reductase {ECO:0000303|PubMed:26715562};\nDE            Short=RsDHVR {ECO:0000303|PubMed:26715562};\nDE            EC=1.3.1.73 {ECO:0000269|PubMed:12391554, ECO:0000269|PubMed:38212296};\nDE   AltName: Full=Protein RR4 {ECO:0000303|PubMed:26715562};\nDE            Short=RsRR4 {ECO:0000303|PubMed:26715562};\nDE   AltName: Full=Vomilenine reductase 2 {ECO:0000303|PubMed:26715562};\nDE            Short=RsVR2 {ECO:0000303|PubMed:26715562};\nDE            EC=1.5.1.- {ECO:0000269|PubMed:26715562, ECO:0000269|PubMed:38212296};\nGN   Name=DHVR {ECO:0000303|PubMed:26715562};\nGN   Synonyms=RR4 {ECO:0000303|PubMed:26715562},\nGN   VR2 {ECO:0000303|PubMed:26715562};\nOS   Rauvolfia serpentina (Serpentine wood) (Ophioxylon serpentinum).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Vinceae;\nOC   Rauvolfiinae; Rauvolfia.\nOX   NCBI_TaxID=4060;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:20.990872+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-22",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d736edca11739beb62ca2d5765f93a0db6fdd42ef122f9711acacccadcaabc22",
  "url": "https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=1,2-Dihydrovomilenine reductase {ECO:0000303|PubMed:26715562};\nDE            Short=RsDHVR {ECO:0000303|PubMed:26715562};\nDE            EC=1.3.1.73 {ECO:0000269|PubMed:12391554, ECO:0000269|PubMed:38212296};\nDE   AltName: Full=Protein RR4 {ECO:0000303|PubMed:26715562};\nDE            Short=RsRR4 {ECO:0000303|PubMed:26715562};\nDE   AltName: Full=Vomilenine reductase 2 {ECO:0000303|PubMed:26715562};\nDE            Short=RsVR2 {ECO:0000303|PubMed:26715562};\nDE            EC=1.5.1.- {ECO:0000269|PubMed:26715562, ECO:0000269|PubMed:38212296};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:20.990872+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d736edca11739beb62ca2d5765f93a0db6fdd42ef122f9711acacccadcaabc22",
  "url": "https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H3",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:ALW82981.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA] (ISOFORM 1), PROTEIN SEQUENCE OF 5-13 AND\nRP   298-308, FUNCTION, CATALYTIC ACTIVITY, PATHWAY, TISSUE SPECIFICITY, AND\nRP   BIOPHYSICOCHEMICAL PROPERTIES.\nRX   PubMed=26715562; DOI=10.1007/s00425-015-2446-6;\nRA   Geissler M., Burghard M., Volk J., Staniek A., Warzecha H.;\nRT   \"A novel cinnamyl alcohol dehydrogenase (CAD)-like reductase contributes to\nRT   the structural diversity of monoterpenoid indole alkaloids in Rauvolfia.\";\nRL   Planta 243:813-824(2016).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:20.990872+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 23-31",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d736edca11739beb62ca2d5765f93a0db6fdd42ef122f9711acacccadcaabc22",
  "url": "https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H4",
  "excerpt": "RN   [2] {ECO:0000312|EMBL:WKU61918.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA] (ISOFORM 2), FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, TISSUE SPECIFICITY, AND\nRP   BIOTECHNOLOGY.\nRX   PubMed=38212296; DOI=10.1038/s41467-024-44797-z;\nRA   Guo J., Gao D., Lian J., Qu Y.;\nRT   \"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.\";\nRL   Nat. Commun. 15:457-457(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:20.990872+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 32-39",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d736edca11739beb62ca2d5765f93a0db6fdd42ef122f9711acacccadcaabc22",
  "url": "https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H5",
  "excerpt": "RN   [3]\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND PATHWAY.\nRX   PubMed=12391554; DOI=10.1055/s-2002-34935;\nRA   Gao S., von Schumann G., Stoeckigt J.;\nRT   \"A newly-detected reductase from Rauvolfia closes a gap in the biosynthesis\nRT   of the antiarrhythmic alkaloid ajmaline.\";\nRL   Planta Med. 68:906-911(2002).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:20.990872+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 40-46",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d736edca11739beb62ca2d5765f93a0db6fdd42ef122f9711acacccadcaabc22",
  "url": "https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H6",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=17-O-acetylnorajmaline + NADP(+) = (2R)-1,2-dihydrovomilenine\nCC         + NADPH + 2 H(+); Xref=Rhea:RHEA:12320, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:17372, ChEBI:CHEBI:57783, ChEBI:CHEBI:58349,\nCC         ChEBI:CHEBI:77725; EC=1.3.1.73;\nCC         Evidence={ECO:0000269|PubMed:12391554, ECO:0000269|PubMed:38212296};\nCC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:12322;\nCC         Evidence={ECO:0000269|PubMed:12391554, ECO:0000269|PubMed:38212296};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:20.990872+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 57-64",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d736edca11739beb62ca2d5765f93a0db6fdd42ef122f9711acacccadcaabc22",
  "url": "https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H7",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=(20S)-19,20-dihydrovomilenine + NADP(+) = vomilenine + NADPH +\nCC         H(+); Xref=Rhea:RHEA:79635, ChEBI:CHEBI:15378, ChEBI:CHEBI:16408,\nCC         ChEBI:CHEBI:57783, ChEBI:CHEBI:58349, ChEBI:CHEBI:230482;\nCC         Evidence={ECO:0000269|PubMed:26715562, ECO:0000269|PubMed:38212296};\nCC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:79637;\nCC         Evidence={ECO:0000269|PubMed:26715562, ECO:0000269|PubMed:38212296};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:20.990872+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 65-71",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d736edca11739beb62ca2d5765f93a0db6fdd42ef122f9711acacccadcaabc22",
  "url": "https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 158. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
