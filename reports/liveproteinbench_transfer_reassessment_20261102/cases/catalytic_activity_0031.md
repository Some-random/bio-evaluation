# catalytic_activity_0031

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0031.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **D** — (2E,6E)-farnesyl diphosphate = (S,S)-drim-8-en-11-yl diphosphate

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MLNLTNVDDALHKGEEWLETNKKTFLSETETGISFKDNFADLLLLELSNRWDYPVIVPEDYPEDNDTNAVAFSILKPTDSRAKVLIDEILACKNADGIVQVHLDPNRPRIAPEVSANILSLFYSYGRGHEVQESLSYLQKAMALEEYQESRYYFLPEPLFFYTWRLLCIASGSALETIDNQRLPKELHTLRDHLIRRVSARLGTAKDNALCPALRILICHSLGIKNDVDLQLLLDLQEDDGSFGRAWFEGLDPSSARLHERGLHAARKTENNPRPPSDMQQRIHDPQMQYARWSDWPLAPSIARNDKGIQHDHHTLGSLESPRPSHDLLLLHH

[Multiple Choices]
A. UDP-N-acetyl-alpha-D-glucosamine = UDP-N-acetyl-alpha-D-mannosamine
B. a (3E,5Z)-dienoyl-CoA = a (2E,4E)-(5,6-saturated)-dienoyl-CoA
C. N-methyl-3-hydroxy-4,5-dimethoxyphenethylamine + S-adenosyl-L-methionine = N,N-dimethyl-3-hydroxy-4,5-dimethoxyphenethylamine + S-adenosyl-L-homocysteine + H(+)
D. (2E,6E)-farnesyl diphosphate = (S,S)-drim-8-en-11-yl diphosphate
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

> The supplied sequence exactly matches the sequence in the cited UniProt records, which assign the farnesyl-diphosphate-to-drimanyl-diphosphate reaction and attribute it to experimental evidence in a publication. The primary paper was not independently reviewed here.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a terpene cyclase: its length and enzyme-like, largely helical sequence, including clustered acidic residues, fit the general features of terpene-cyclase families that act on prenyl diphosphates. Transferable family knowledge therefore favors D, the only choice describing cyclization of a prenyl diphosphate; the other options describe sugar epimerization, CoA-dependent isomerization, or SAM-dependent methylation. This supports the reaction class, not the precise product stereochemistry from sequence alone.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level sequence inference meaningfully distinguishes D among these alternatives without requiring recall of this exact protein's annotation. The specific drimane product is not independently established by the argument, but the alternatives make that finer discrimination unnecessary.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four alternatives describe distinct reaction classes, and only D is a terpene-cyclization reaction.


### Important caveats

- The reaction annotation is attributed to experimental evidence in the cited publication, but that publication was not independently assessed.
- Sequence-based family recognition supports the reaction class more strongly than the exact product stereochemistry.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a terpene cyclase: its length and enzyme-like, largely helical sequence, including clustered acidic residues, fit the general features of terpene-cyclase families that act on prenyl diphosphates. Transferable family knowledge therefore favors D, the only choice describing cyclization of a prenyl diphosphate; the other options describe sugar epimerization, CoA-dependent isomerization, or SAM-dependent methylation. This supports the reaction class, not the precise product stereochemistry from sequence alone.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference meaningfully distinguishes D among these alternatives without requiring recall of this exact protein's annotation. The specific drimane product is not independently established by the argument, but the alternatives make that finer discrimination unnecessary."
  },
  "case_id": "catalytic_activity_0031",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the sequence in the cited UniProt records, which assign the farnesyl-diphosphate-to-drimanyl-diphosphate reaction and attribute it to experimental evidence in a publication. The primary paper was not independently reviewed here."
  },
  "important_caveats": [
    "The reaction annotation is attributed to experimental evidence in the cited publication, but that publication was not independently assessed.",
    "Sequence-based family recognition supports the reaction class more strongly than the exact product stereochemistry."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four alternatives describe distinct reaction classes, and only D is a terpene-cyclization reaction."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0031",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the sequence in the cited UniProt records, which assign the farnesyl-diphosphate-to-drimanyl-diphosphate reaction and attribute it to experimental evidence in a publication. The primary paper was not independently reviewed here.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a terpene cyclase: its length and enzyme-like, largely helical sequence, including clustered acidic residues, fit the general features of terpene-cyclase families that act on prenyl diphosphates. Transferable family knowledge therefore favors D, the only choice describing cyclization of a prenyl diphosphate; the other options describe sugar epimerization, CoA-dependent isomerization, or SAM-dependent methylation. This supports the reaction class, not the precise product stereochemistry from sequence alone.",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference meaningfully distinguishes D among these alternatives without requiring recall of this exact protein's annotation. The specific drimane product is not independently established by the argument, but the alternatives make that finer discrimination unnecessary."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four alternatives describe distinct reaction classes, and only D is a terpene-cyclization reaction."
  },
  "important_caveats": [
    "The reaction annotation is attributed to experimental evidence in the cited publication, but that publication was not independently assessed.",
    "Sequence-based family recognition supports the reaction class more strongly than the exact product stereochemistry."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The reviewer evidence (C5, H4) confirms the catalytic activity annotation as '(2E,6E)-farnesyl diphosphate = (S,S)-drim-8-en-11-yl diphosphate' with experimental evidence (ECO:0000269|PubMed:39310987). The protein is annotated as 'Terpene cyclase vviB' (EC 4.2.3.-) from Viridothelium virens. The benchmark sequence matches the source sequence exactly (SHA256 confirmed). The expected answer D matches the database annotation verbatim.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model can distinguish option D through family-level terpene cyclase recognition combined with elimination of alternatives: (1) The 333-aa length with predominantly α-helical character matches the all-α fold of fungal sesquiterpene cyclases (typically 300-400 aa). (2) A degenerate DxxxD motif is present ('DLQED' around position 258), a recognized variant of the canonical DDxxD metal-binding motif in terpene cyclases. (3) The C-terminal His-rich tail ('HH' at the terminus) is characteristic of fungal terpene cyclases. (4) Option C (SAM-dependent methyltransferase) is eliminated by the absence of Rossmann-fold SAM-binding motifs (no VIGXG or GXG motifs). (5) Option B (dienoyl-CoA isomerase) is eliminated by the larger size (these are typically 200-250 aa) and absence of isomerase-specific motifs. (6) Option A (UDP-GlcNAc epimerase) is eliminated by the absence of epimerase-specific motifs and the mismatch with the typical fold/size. Together, these family-level features and elimination arguments meaningfully favor D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence contains recognizable terpene cyclase family features (size, helical content, degenerate DxxxD motif, C-terminal His) and lacks the diagnostic motifs of the three alternative enzyme classes. This permits a credible family-level inference distinguishing D without requiring the exact database record for this protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent distinct enzyme classes (epimerase, isomerase, methyltransferase, terpene cyclase) with clearly different structural and mechanistic requirements. The terpene cyclase features present in the sequence and the absence of motifs diagnostic for the other three classes make D the only defensible choice.


### Important caveats

- The DDxxD motif is present only in a degenerate DxxxD variant, not the canonical form, so identification relies partly on probabilistic family-level matching rather than a single unambiguous motif.
- The NSE/DTE triad motif, commonly used to confirm terpene cyclase identity, is not clearly identifiable in this sequence.
- The reviewer evidence confirms the annotation is experimentally supported (ECO:0000269), but this evidence was not available to the evaluated model.
- The protein is from a lichen-forming fungus (Viridothelium virens), a taxonomic detail not provided in the original input; the fungal context is inferred from sequence features alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can distinguish option D through family-level terpene cyclase recognition combined with elimination of alternatives: (1) The 333-aa length with predominantly α-helical character matches the all-α fold of fungal sesquiterpene cyclases (typically 300-400 aa). (2) A degenerate DxxxD motif is present ('DLQED' around position 258), a recognized variant of the canonical DDxxD metal-binding motif in terpene cyclases. (3) The C-terminal His-rich tail ('HH' at the terminus) is characteristic of fungal terpene cyclases. (4) Option C (SAM-dependent methyltransferase) is eliminated by the absence of Rossmann-fold SAM-binding motifs (no VIGXG or GXG motifs). (5) Option B (dienoyl-CoA isomerase) is eliminated by the larger size (these are typically 200-250 aa) and absence of isomerase-specific motifs. (6) Option A (UDP-GlcNAc epimerase) is eliminated by the absence of epimerase-specific motifs and the mismatch with the typical fold/size. Together, these family-level features and elimination arguments meaningfully favor D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence contains recognizable terpene cyclase family features (size, helical content, degenerate DxxxD motif, C-terminal His) and lacks the diagnostic motifs of the three alternative enzyme classes. This permits a credible family-level inference distinguishing D without requiring the exact database record for this protein."
  },
  "case_id": "catalytic_activity_0031",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4"
    ],
    "judgment": "supported",
    "reason": "The reviewer evidence (C5, H4) confirms the catalytic activity annotation as '(2E,6E)-farnesyl diphosphate = (S,S)-drim-8-en-11-yl diphosphate' with experimental evidence (ECO:0000269|PubMed:39310987). The protein is annotated as 'Terpene cyclase vviB' (EC 4.2.3.-) from Viridothelium virens. The benchmark sequence matches the source sequence exactly (SHA256 confirmed). The expected answer D matches the database annotation verbatim."
  },
  "important_caveats": [
    "The DDxxD motif is present only in a degenerate DxxxD variant, not the canonical form, so identification relies partly on probabilistic family-level matching rather than a single unambiguous motif.",
    "The NSE/DTE triad motif, commonly used to confirm terpene cyclase identity, is not clearly identifiable in this sequence.",
    "The reviewer evidence confirms the annotation is experimentally supported (ECO:0000269), but this evidence was not available to the evaluated model.",
    "The protein is from a lichen-forming fungus (Viridothelium virens), a taxonomic detail not provided in the original input; the fungal context is inferred from sequence features alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent distinct enzyme classes (epimerase, isomerase, methyltransferase, terpene cyclase) with clearly different structural and mechanistic requirements. The terpene cyclase features present in the sequence and the absence of motifs diagnostic for the other three classes make D the only defensible choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0031",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The reviewer evidence (C5, H4) confirms the catalytic activity annotation as '(2E,6E)-farnesyl diphosphate = (S,S)-drim-8-en-11-yl diphosphate' with experimental evidence (ECO:0000269|PubMed:39310987). The protein is annotated as 'Terpene cyclase vviB' (EC 4.2.3.-) from Viridothelium virens. The benchmark sequence matches the source sequence exactly (SHA256 confirmed). The expected answer D matches the database annotation verbatim.",
    "evidence_ids": ["C5", "H4", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model can distinguish option D through family-level terpene cyclase recognition combined with elimination of alternatives: (1) The 333-aa length with predominantly α-helical character matches the all-α fold of fungal sesquiterpene cyclases (typically 300-400 aa). (2) A degenerate DxxxD motif is present ('DLQED' around position 258), a recognized variant of the canonical DDxxD metal-binding motif in terpene cyclases. (3) The C-terminal His-rich tail ('HH' at the terminus) is characteristic of fungal terpene cyclases. (4) Option C (SAM-dependent methyltransferase) is eliminated by the absence of Rossmann-fold SAM-binding motifs (no VIGXG or GXG motifs). (5) Option B (dienoyl-CoA isomerase) is eliminated by the larger size (these are typically 200-250 aa) and absence of isomerase-specific motifs. (6) Option A (UDP-GlcNAc epimerase) is eliminated by the absence of epimerase-specific motifs and the mismatch with the typical fold/size. Together, these family-level features and elimination arguments meaningfully favor D.",
    "missing_item_specific_fact": "",
    "reason": "The sequence contains recognizable terpene cyclase family features (size, helical content, degenerate DxxxD motif, C-terminal His) and lacks the diagnostic motifs of the three alternative enzyme classes. This permits a credible family-level inference distinguishing D without requiring the exact database record for this protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent distinct enzyme classes (epimerase, isomerase, methyltransferase, terpene cyclase) with clearly different structural and mechanistic requirements. The terpene cyclase features present in the sequence and the absence of motifs diagnostic for the other three classes make D the only defensible choice."
  },
  "important_caveats": [
    "The DDxxD motif is present only in a degenerate DxxxD variant, not the canonical form, so identification relies partly on probabilistic family-level matching rather than a single unambiguous motif.",
    "The NSE/DTE triad motif, commonly used to confirm terpene cyclase identity, is not clearly identifiable in this sequence.",
    "The reviewer evidence confirms the annotation is experimentally supported (ECO:0000269), but this evidence was not available to the evaluated model.",
    "The protein is from a lichen-forming fungus (Viridothelium virens), a taxonomic detail not provided in the original input; the fungal context is inferred from sequence features alone."
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
  "benchmark_sequence_length": 333,
  "benchmark_sequence_sha256": "a1c09443fedcb62c00aaf145cd007a77c82a9540e45d597a989a1635abab7d2f",
  "current_entry_audit": {
    "entryVersion": 14,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2020-06-17",
    "sequenceVersion": 1
  },
  "current_record_sha256": "3d39951d8d42c448594f2eec6c6a9e2cec322a8340d79db22032e12c77f0af30",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 333,
  "current_source_sequence_sha256": "a1c09443fedcb62c00aaf145cd007a77c82a9540e45d597a989a1635abab7d2f",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 12,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A6A6H2E0",
  "selected_historical_entry_version": 12,
  "selected_historical_record_sha256": "ba398b865fc9576814bd6954ed27346d14ab44b5850d578e50e8feb280836380",
  "selected_historical_source_sequence_length": 333,
  "selected_historical_source_sequence_sha256": "a1c09443fedcb62c00aaf145cd007a77c82a9540e45d597a989a1635abab7d2f",
  "selected_historical_version": {
    "accession": "A0A6A6H2E0",
    "database": "Swiss-Prot",
    "entryVersion": 12,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "VVIB_VIRVR",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6A6H2E0.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A6A6H2E0\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:25:29.065613+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3d39951d8d42c448594f2eec6c6a9e2cec322a8340d79db22032e12c77f0af30",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6A6H2E0.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6A6H2E0.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":14,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2020-06-17\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:25:29.065613+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3d39951d8d42c448594f2eec6c6a9e2cec322a8340d79db22032e12c77f0af30",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6A6H2E0.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6A6H2E0.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Speckled blister lichen\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Dothideomycetes\",\"Dothideomycetes incertae sedis\",\"Trypetheliales\",\"Trypetheliaceae\",\"Viridothelium\"],\"scientificName\":\"Viridothelium virens\",\"synonyms\":[\"Trypethelium virens\"],\"taxonId\":1048519}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:25:29.065613+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3d39951d8d42c448594f2eec6c6a9e2cec322a8340d79db22032e12c77f0af30",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6A6H2E0.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6A6H2E0.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39310987\",\"source\":\"PubMed\"}],\"value\":\"Sporulositol A biosynthesis cluster protein B\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39310987\",\"source\":\"PubMed\"}],\"value\":\"4.2.3.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39310987\",\"source\":\"PubMed\"}],\"value\":\"Terpene cyclase vviB\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:25:29.065613+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3d39951d8d42c448594f2eec6c6a9e2cec322a8340d79db22032e12c77f0af30",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6A6H2E0.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6A6H2E0.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39310987\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:80980\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39310987\",\"source\":\"PubMed\"}],\"name\":\"(2E,6E)-farnesyl diphosphate = (S,S)-drim-8-en-11-yl diphosphate\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:80979\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:175763\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231796\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:25:29.065613+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3d39951d8d42c448594f2eec6c6a9e2cec322a8340d79db22032e12c77f0af30",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6A6H2E0.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6A6H2E0.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Tang Y.J.\",\"Zou Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39310987\"},{\"database\":\"DOI\",\"id\":\"10.1021/acs.orglett.4c03154\"}],\"citationType\":\"journal article\",\"firstPage\":\"8366\",\"id\":\"39310987\",\"journal\":\"Org. Lett.\",\"lastPage\":\"8370\",\"publicationDate\":\"2024\",\"title\":\"Cyclo-farnesyl Diphosphate-Dependent Prenylation in Fungi.\",\"volume\":\"26\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:25:29.065613+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3d39951d8d42c448594f2eec6c6a9e2cec322a8340d79db22032e12c77f0af30",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6A6H2E0.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6A6H2E0?format=txt&versions=12)

```json
{
  "entry_version": 12,
  "evidence_id": "H1",
  "excerpt": "ID   VVIB_VIRVR              Reviewed;         333 AA.\nAC   A0A6A6H2E0;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   17-JUN-2020, sequence version 1.\nDT   28-JAN-2026, entry version 12.\nDE   RecName: Full=Terpene cyclase vviB {ECO:0000303|PubMed:39310987};\nDE            EC=4.2.3.- {ECO:0000269|PubMed:39310987};\nDE   AltName: Full=Sporulositol A biosynthesis cluster protein B {ECO:0000303|PubMed:39310987};\nGN   Name=vviB {ECO:0000303|PubMed:39310987}; ORFNames=EV356DRAFT_534741;\nOS   Viridothelium virens (Speckled blister lichen) (Trypethelium virens).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Dothideomycetes;\nOC   Dothideomycetes incertae sedis; Trypetheliales; Trypetheliaceae;\nOC   Viridothelium.\nOX   NCBI_TaxID=1048519;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:33.124614+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ba398b865fc9576814bd6954ed27346d14ab44b5850d578e50e8feb280836380",
  "url": "https://rest.uniprot.org/unisave/A0A6A6H2E0?format=txt&versions=12"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6A6H2E0?format=txt&versions=12)

```json
{
  "entry_version": 12,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Terpene cyclase vviB {ECO:0000303|PubMed:39310987};\nDE            EC=4.2.3.- {ECO:0000269|PubMed:39310987};\nDE   AltName: Full=Sporulositol A biosynthesis cluster protein B {ECO:0000303|PubMed:39310987};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:33.124614+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ba398b865fc9576814bd6954ed27346d14ab44b5850d578e50e8feb280836380",
  "url": "https://rest.uniprot.org/unisave/A0A6A6H2E0?format=txt&versions=12"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6A6H2E0?format=txt&versions=12)

```json
{
  "entry_version": 12,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND PATHWAY.\nRX   PubMed=39310987; DOI=10.1021/acs.orglett.4c03154;\nRA   Tang Y.J., Zou Y.;\nRT   \"Cyclo-farnesyl Diphosphate-Dependent Prenylation in Fungi.\";\nRL   Org. Lett. 26:8366-8370(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:33.124614+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 29-34",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ba398b865fc9576814bd6954ed27346d14ab44b5850d578e50e8feb280836380",
  "url": "https://rest.uniprot.org/unisave/A0A6A6H2E0?format=txt&versions=12"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6A6H2E0?format=txt&versions=12)

```json
{
  "entry_version": 12,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=(2E,6E)-farnesyl diphosphate = (S,S)-drim-8-en-11-yl\nCC         diphosphate; Xref=Rhea:RHEA:80979, ChEBI:CHEBI:175763,\nCC         ChEBI:CHEBI:231796; Evidence={ECO:0000269|PubMed:39310987};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:80980;\nCC         Evidence={ECO:0000269|PubMed:39310987};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:33.124614+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 39-44",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ba398b865fc9576814bd6954ed27346d14ab44b5850d578e50e8feb280836380",
  "url": "https://rest.uniprot.org/unisave/A0A6A6H2E0?format=txt&versions=12"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 31. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
