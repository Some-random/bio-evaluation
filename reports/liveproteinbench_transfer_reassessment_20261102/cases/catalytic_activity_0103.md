# catalytic_activity_0103

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0103.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **C** — L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-L-aspartate + NADPH + H(+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSVKKAGVLGATGSVGQRFILLLSKHPEFEIHALGASSRSAGKKYKDAASWKQTETLPETEQDIVVQECKPEGNFLECDVVFSGLDADVAGDIEKSFVEAGLAVVSNAKNYRREKDVPLVVPIVNPEHIDVVENKVKQAVSKGGKKPGFIICISNCSTAGLVAPLKPLVEKFGPIDALTTTTLQAISGAGFSPGVSGMDILDNIVPYISGEEDKLEWETKKILGGVNAEGTEFVPIPESEMKVSAQCNRVPVIDGHTECISLRFANRPAPSVEDVKQCLREYECAASKLGCHSAPKQTIHVLDQPDRPQPRLDRDRDSGYGVSVGRIREDSLLDFKMVVLSHNTIIGAAGAGILIAEILKAKNII

[Multiple Choices]
A. a phosphate monoester + H2O = an alcohol + phosphate
B. daunorubicin(in) + ATP + H2O = daunorubicin(out) + ADP + phosphate + H(+)
C. L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-L-aspartate + NADPH + H(+)
D. (2R)-1,2-dihydrovomilenine + NADP(+) = vomilenine + NADPH + H(+)
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

> The sequence matches the referenced protein sequence, whose catalytic-activity annotation gives the reaction in choice C and cites experimental evidence codes (ECO:0000269). This supports the key for the supplied sequence, although the underlying papers were not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H8](#evidence-h8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has features consistent with the aspartate-semialdehyde dehydrogenase family, including a glycine-rich nucleotide-binding region and a conserved cysteine-containing catalytic region. Transferable knowledge of this enzyme family points to oxidation and phosphorylation of L-aspartate 4-semialdehyde using NADP and phosphate, distinguishing choice C from the phosphatase reaction in A, the drug-export ATPase reaction in B, and the alkaloid oxidation in D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level recognition from the sequence gives a meaningful basis for selecting C without needing the exact protein's database record. The sequence-based inference is not itself experimental confirmation, but it is discriminative among these alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The offered reactions describe distinct enzyme activities, and the sequence-family inference specifically favors C.


### Important caveats

- The exact reaction is supported by experimental evidence cited in the matched annotation; that evidence is separate from the transferable sequence-based inference available to the model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has features consistent with the aspartate-semialdehyde dehydrogenase family, including a glycine-rich nucleotide-binding region and a conserved cysteine-containing catalytic region. Transferable knowledge of this enzyme family points to oxidation and phosphorylation of L-aspartate 4-semialdehyde using NADP and phosphate, distinguishing choice C from the phosphatase reaction in A, the drug-export ATPase reaction in B, and the alkaloid oxidation in D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition from the sequence gives a meaningful basis for selecting C without needing the exact protein's database record. The sequence-based inference is not itself experimental confirmation, but it is discriminative among these alternatives."
  },
  "case_id": "catalytic_activity_0103",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H8"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the referenced protein sequence, whose catalytic-activity annotation gives the reaction in choice C and cites experimental evidence codes (ECO:0000269). This supports the key for the supplied sequence, although the underlying papers were not independently reviewed here."
  },
  "important_caveats": [
    "The exact reaction is supported by experimental evidence cited in the matched annotation; that evidence is separate from the transferable sequence-based inference available to the model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered reactions describe distinct enzyme activities, and the sequence-family inference specifically favors C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0103",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the referenced protein sequence, whose catalytic-activity annotation gives the reaction in choice C and cites experimental evidence codes (ECO:0000269). This supports the key for the supplied sequence, although the underlying papers were not independently reviewed here.",
    "evidence_ids": ["C1", "C5", "H8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has features consistent with the aspartate-semialdehyde dehydrogenase family, including a glycine-rich nucleotide-binding region and a conserved cysteine-containing catalytic region. Transferable knowledge of this enzyme family points to oxidation and phosphorylation of L-aspartate 4-semialdehyde using NADP and phosphate, distinguishing choice C from the phosphatase reaction in A, the drug-export ATPase reaction in B, and the alkaloid oxidation in D.",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition from the sequence gives a meaningful basis for selecting C without needing the exact protein's database record. The sequence-based inference is not itself experimental confirmation, but it is discriminative among these alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered reactions describe distinct enzyme activities, and the sequence-family inference specifically favors C."
  },
  "important_caveats": [
    "The exact reaction is supported by experimental evidence cited in the matched annotation; that evidence is separate from the transferable sequence-based inference available to the model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q5ALM0 (sequence matched, 365 aa) is annotated as Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11) with the exact reaction 'L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-L-aspartate + NADPH + H(+)'. This annotation is backed by experimental evidence (ECO:0000269) from multiple publications including X-ray crystallography (PDB 3HSK, 2.2 Å with NADP+ bound) and enzymatic assays. The expected answer C matches the recorded catalytic activity verbatim.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H8](#evidence-h8), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a canonical Rossmann-fold NAD(P)-binding motif 'VLGATGSVGQRF' (GxGxxG pattern), immediately narrowing the enzyme to an NAD(P)-dependent oxidoreductase and eliminating A (phosphatase, no cofactor) and B (ABC transporter, different domain architecture). Among the two NADP-dependent choices (C and D), the sequence exhibits the hallmark catalytic Cys-His-Glu triad of the aspartate-semialdehyde dehydrogenase (ASADH) family: the region 'VPVIDGHTECISLRF' encodes the catalytic His and Glu (GHTE) and the downstream Cys that forms the thioester intermediate unique to ASADH. Additionally, the conserved 'SNCSTAG' motif and the overall single-domain ~365-aa architecture are characteristic of ASADH family members across bacteria and fungi. Choice D (dihydrovomilenine dehydrogenase) is a plant alkaloid-biosynthesis enzyme with a different catalytic mechanism (hydride transfer without a thioester intermediate) and lacks the Cys-His-Glu catalytic cluster. The combination of Rossmann fold + catalytic Cys-His-Glu triad + family-specific motifs constitutes a well-known, transferable signature of the ASADH family.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model familiar with enzyme families can recognize the GxGxxG Rossmann fold (shared with many dehydrogenases) and then use the distinctive catalytic Cys-His-Glu triad and ASADH-specific conserved motifs to distinguish choice C from the other NADP-dependent option D. This is a family-level inference based on conserved sequence features learned from other ASADH homologs, not a lookup of this specific protein's record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent very different enzyme classes (phosphatase, ABC transporter, ASADH, plant alkaloid dehydrogenase). The sequence's Rossmann fold eliminates A and B; the catalytic Cys-His-Glu triad and ASADH-family motifs eliminate D. Only C is consistent with all observed sequence features.


### Important caveats

- The reviewer-only evidence confirms the annotation with experimental (ECO:0000269) support including crystallography, but this evidence was not available to the evaluated model.
- The GxGxxG motif is shared across many NAD(P)-binding enzymes; the discriminating power comes from the combination with the catalytic Cys-His-Glu triad and family-specific motifs.
- The physiological direction is recorded as right-to-left (reductive direction), but the reaction as written in choice C is the standard EC 1.2.1.11 forward direction and is the conventional way to state the catalytic activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a canonical Rossmann-fold NAD(P)-binding motif 'VLGATGSVGQRF' (GxGxxG pattern), immediately narrowing the enzyme to an NAD(P)-dependent oxidoreductase and eliminating A (phosphatase, no cofactor) and B (ABC transporter, different domain architecture). Among the two NADP-dependent choices (C and D), the sequence exhibits the hallmark catalytic Cys-His-Glu triad of the aspartate-semialdehyde dehydrogenase (ASADH) family: the region 'VPVIDGHTECISLRF' encodes the catalytic His and Glu (GHTE) and the downstream Cys that forms the thioester intermediate unique to ASADH. Additionally, the conserved 'SNCSTAG' motif and the overall single-domain ~365-aa architecture are characteristic of ASADH family members across bacteria and fungi. Choice D (dihydrovomilenine dehydrogenase) is a plant alkaloid-biosynthesis enzyme with a different catalytic mechanism (hydride transfer without a thioester intermediate) and lacks the Cys-His-Glu catalytic cluster. The combination of Rossmann fold + catalytic Cys-His-Glu triad + family-specific motifs constitutes a well-known, transferable signature of the ASADH family.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model familiar with enzyme families can recognize the GxGxxG Rossmann fold (shared with many dehydrogenases) and then use the distinctive catalytic Cys-His-Glu triad and ASADH-specific conserved motifs to distinguish choice C from the other NADP-dependent option D. This is a family-level inference based on conserved sequence features learned from other ASADH homologs, not a lookup of this specific protein's record."
  },
  "case_id": "catalytic_activity_0103",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H8",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q5ALM0 (sequence matched, 365 aa) is annotated as Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11) with the exact reaction 'L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-L-aspartate + NADPH + H(+)'. This annotation is backed by experimental evidence (ECO:0000269) from multiple publications including X-ray crystallography (PDB 3HSK, 2.2 Å with NADP+ bound) and enzymatic assays. The expected answer C matches the recorded catalytic activity verbatim."
  },
  "important_caveats": [
    "The reviewer-only evidence confirms the annotation with experimental (ECO:0000269) support including crystallography, but this evidence was not available to the evaluated model.",
    "The GxGxxG motif is shared across many NAD(P)-binding enzymes; the discriminating power comes from the combination with the catalytic Cys-His-Glu triad and family-specific motifs.",
    "The physiological direction is recorded as right-to-left (reductive direction), but the reaction as written in choice C is the standard EC 1.2.1.11 forward direction and is the conventional way to state the catalytic activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent very different enzyme classes (phosphatase, ABC transporter, ASADH, plant alkaloid dehydrogenase). The sequence's Rossmann fold eliminates A and B; the catalytic Cys-His-Glu triad and ASADH-family motifs eliminate D. Only C is consistent with all observed sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0103",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q5ALM0 (sequence matched, 365 aa) is annotated as Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11) with the exact reaction 'L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-L-aspartate + NADPH + H(+)'. This annotation is backed by experimental evidence (ECO:0000269) from multiple publications including X-ray crystallography (PDB 3HSK, 2.2 Å with NADP+ bound) and enzymatic assays. The expected answer C matches the recorded catalytic activity verbatim.",
    "evidence_ids": ["C4", "C5", "H8", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a canonical Rossmann-fold NAD(P)-binding motif 'VLGATGSVGQRF' (GxGxxG pattern), immediately narrowing the enzyme to an NAD(P)-dependent oxidoreductase and eliminating A (phosphatase, no cofactor) and B (ABC transporter, different domain architecture). Among the two NADP-dependent choices (C and D), the sequence exhibits the hallmark catalytic Cys-His-Glu triad of the aspartate-semialdehyde dehydrogenase (ASADH) family: the region 'VPVIDGHTECISLRF' encodes the catalytic His and Glu (GHTE) and the downstream Cys that forms the thioester intermediate unique to ASADH. Additionally, the conserved 'SNCSTAG' motif and the overall single-domain ~365-aa architecture are characteristic of ASADH family members across bacteria and fungi. Choice D (dihydrovomilenine dehydrogenase) is a plant alkaloid-biosynthesis enzyme with a different catalytic mechanism (hydride transfer without a thioester intermediate) and lacks the Cys-His-Glu catalytic cluster. The combination of Rossmann fold + catalytic Cys-His-Glu triad + family-specific motifs constitutes a well-known, transferable signature of the ASADH family.",
    "missing_item_specific_fact": "",
    "reason": "A model familiar with enzyme families can recognize the GxGxxG Rossmann fold (shared with many dehydrogenases) and then use the distinctive catalytic Cys-His-Glu triad and ASADH-specific conserved motifs to distinguish choice C from the other NADP-dependent option D. This is a family-level inference based on conserved sequence features learned from other ASADH homologs, not a lookup of this specific protein's record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent very different enzyme classes (phosphatase, ABC transporter, ASADH, plant alkaloid dehydrogenase). The sequence's Rossmann fold eliminates A and B; the catalytic Cys-His-Glu triad and ASADH-family motifs eliminate D. Only C is consistent with all observed sequence features."
  },
  "important_caveats": [
    "The reviewer-only evidence confirms the annotation with experimental (ECO:0000269) support including crystallography, but this evidence was not available to the evaluated model.",
    "The GxGxxG motif is shared across many NAD(P)-binding enzymes; the discriminating power comes from the combination with the catalytic Cys-His-Glu triad and family-specific motifs.",
    "The physiological direction is recorded as right-to-left (reductive direction), but the reaction as written in choice C is the standard EC 1.2.1.11 forward direction and is the conventional way to state the catalytic activity."
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
  "benchmark_sequence_length": 365,
  "benchmark_sequence_sha256": "6addf96ce62cae01385fdd88f8e959e42e783ffb39b551e1fdaa9f5898f59f56",
  "current_entry_audit": {
    "entryVersion": 147,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2005-04-26",
    "sequenceVersion": 1
  },
  "current_record_sha256": "8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 365,
  "current_source_sequence_sha256": "6addf96ce62cae01385fdd88f8e959e42e783ffb39b551e1fdaa9f5898f59f56",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 145,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q5ALM0",
  "selected_historical_entry_version": 145,
  "selected_historical_record_sha256": "ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d",
  "selected_historical_source_sequence_length": 365,
  "selected_historical_source_sequence_sha256": "6addf96ce62cae01385fdd88f8e959e42e783ffb39b551e1fdaa9f5898f59f56",
  "selected_historical_version": {
    "accession": "Q5ALM0",
    "database": "Swiss-Prot",
    "entryVersion": 145,
    "firstRelease": "2025_03/2025_03",
    "firstReleaseDate": "18-Jun-2025",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DHAS_CANAL",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q5ALM0\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:31:05.955388+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f",
  "url": "https://rest.uniprot.org/uniprotkb/Q5ALM0.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":147,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2005-04-26\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:31:05.955388+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f",
  "url": "https://rest.uniprot.org/uniprotkb/Q5ALM0.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Yeast\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000559\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Saccharomycotina\",\"Pichiomycetes\",\"Debaryomycetaceae\",\"Candida/Lodderomyces clade\",\"Candida\"],\"scientificName\":\"Candida albicans (strain SC5314 / ATCC MYA-2876)\",\"taxonId\":237561}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:31:05.955388+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f",
  "url": "https://rest.uniprot.org/uniprotkb/Q5ALM0.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"17419877\",\"source\":\"PubMed\"}],\"value\":\"CaASADH\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20124701\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29608391\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"32383780\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"34469014\",\"source\":\"PubMed\"}],\"value\":\"1.2.1.11\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Aspartate-semialdehyde dehydrogenase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:31:05.955388+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f",
  "url": "https://rest.uniprot.org/uniprotkb/Q5ALM0.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"right-to-left\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20124701\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29608391\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"32383780\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"34469014\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:24286\"}}],\"reaction\":{\"ecNumber\":\"1.2.1.11\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20124701\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29608391\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"32383780\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"34469014\",\"source\":\"PubMed\"}],\"name\":\"L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-L-aspartate + NADPH + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:24284\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:43474\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57535\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57783\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:537519\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:31:05.955388+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f",
  "url": "https://rest.uniprot.org/uniprotkb/Q5ALM0.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"van het Hoog M.\",\"Rast T.J.\",\"Martchenko M.\",\"Grindle S.\",\"Dignard D.\",\"Hogues H.\",\"Cuomo C.\",\"Berriman M.\",\"Scherer S.\",\"Magee B.B.\",\"Whiteway M.\",\"Chibana H.\",\"Nantel A.\",\"Magee P.T.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"17419877\"},{\"database\":\"DOI\",\"id\":\"10.1186/gb-2007-8-4-r52\"}],\"citationType\":\"journal article\",\"firstPage\":\"RESEARCH52.1\",\"id\":\"17419877\",\"journal\":\"Genome Biol.\",\"lastPage\":\"RESEARCH52.12\",\"publicationDate\":\"2007\",\"title\":\"Assembly of the Candida albicans genome into sixteen supercontigs aligned on the eight chromosomes.\",\"volume\":\"8\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000559\",\"source\":\"Proteomes\"}],\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000559\",\"source\":\"Proteomes\"}],\"type\":\"STRAIN\",\"value\":\"SC5314 / ATCC MYA-2876\"}],\"referenceNumber\":2,\"referencePositions\":[\"GENOME REANNOTATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:31:05.955388+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f",
  "url": "https://rest.uniprot.org/uniprotkb/Q5ALM0.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Dahal G.P.\",\"Viola R.E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"29608391\"},{\"database\":\"DOI\",\"id\":\"10.1177/2472555218767844\"}],\"citationType\":\"journal article\",\"firstPage\":\"520\",\"id\":\"29608391\",\"journal\":\"SLAS Discovery\",\"lastPage\":\"531\",\"publicationDate\":\"2018\",\"title\":\"A Fragment Library Screening Approach to Identify Selective Inhibitors against an Essential Fungal Enzyme.\",\"volume\":\"23\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":5,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-02T04:31:05.955388+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f",
  "url": "https://rest.uniprot.org/uniprotkb/Q5ALM0.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Dahal G.P.\",\"Launder D.\",\"McKeone K.M.M.\",\"Hunter J.P.\",\"Conti H.R.\",\"Viola R.E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"32383780\"},{\"database\":\"DOI\",\"id\":\"10.1002/ddr.21682\"}],\"citationType\":\"journal article\",\"firstPage\":\"736\",\"id\":\"32383780\",\"journal\":\"Drug Dev. Res.\",\"lastPage\":\"744\",\"publicationDate\":\"2020\",\"title\":\"Aspartate semialdehyde dehydrogenase inhibition suppresses the growth of the pathogenic fungus Candida albicans.\",\"volume\":\"81\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":6,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/5",
  "retrieved_utc": "2026-11-02T04:31:05.955388+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f",
  "url": "https://rest.uniprot.org/uniprotkb/Q5ALM0.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Friday S.N.\",\"Cheng D.W.\",\"Zagler S.G.\",\"Zanella B.S.\",\"Dietz J.D.\",\"Calbat C.N.\",\"Roach L.T.\",\"Bagnal C.\",\"Faile I.S.\",\"Halkides C.J.\",\"Viola R.E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"34469014\"},{\"database\":\"DOI\",\"id\":\"10.1002/ddr.21875\"}],\"citationType\":\"journal article\",\"firstPage\":\"447\",\"id\":\"34469014\",\"journal\":\"Drug Dev. Res.\",\"lastPage\":\"460\",\"publicationDate\":\"2022\",\"title\":\"Design and testing of selective inactivators against an antifungal enzyme target.\",\"volume\":\"83\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":7,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/6",
  "retrieved_utc": "2026-11-02T04:31:05.955388+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f",
  "url": "https://rest.uniprot.org/uniprotkb/Q5ALM0.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Arachea B.T.\",\"Liu X.\",\"Pavlovsky A.G.\",\"Viola R.E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"20124701\"},{\"database\":\"DOI\",\"id\":\"10.1107/s0907444909052834\"}],\"citationType\":\"journal article\",\"firstPage\":\"205\",\"id\":\"20124701\",\"journal\":\"Acta Crystallogr. D\",\"lastPage\":\"212\",\"publicationDate\":\"2010\",\"title\":\"Expansion of the aspartate beta-semialdehyde dehydrogenase family: the first structure of a fungal ortholog.\",\"volume\":\"66\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"3HSK\",\"source\":\"PDB\"}],\"referenceNumber\":8,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.20 ANGSTROMS) IN COMPLEX WITH NADP(+)\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/7",
  "retrieved_utc": "2026-11-02T04:31:05.955388+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f",
  "url": "https://rest.uniprot.org/uniprotkb/Q5ALM0.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)

```json
{
  "entry_version": 145,
  "evidence_id": "H1",
  "excerpt": "ID   DHAS_CANAL              Reviewed;         365 AA.\nAC   Q5ALM0;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   26-APR-2005, sequence version 1.\nDT   18-JUN-2025, entry version 145.\nDE   RecName: Full=Aspartate-semialdehyde dehydrogenase {ECO:0000305};\nDE            EC=1.2.1.11 {ECO:0000269|PubMed:20124701, ECO:0000269|PubMed:29608391, ECO:0000269|PubMed:32383780, ECO:0000269|PubMed:34469014};\nDE   AltName: Full=CaASADH {ECO:0000303|PubMed:17419877};\nGN   Name=HOM2 {ECO:0000303|PubMed:17419877};\nGN   OrderedLocusNames=CAALFM_C202370CA {ECO:0000312|EMBL:AOW27277.1},\nGN   orf19.9132 {ECO:0000312|CGD:CAL0000179646};\nOS   Candida albicans (strain SC5314 / ATCC MYA-2876) (Yeast).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Saccharomycotina; Pichiomycetes;\nOC   Debaryomycetaceae; Candida/Lodderomyces clade; Candida.\nOX   NCBI_TaxID=237561 {ECO:0000312|Proteomes:UP000000559};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:09.278811+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d",
  "url": "https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)

```json
{
  "entry_version": 145,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Aspartate-semialdehyde dehydrogenase {ECO:0000305};\nDE            EC=1.2.1.11 {ECO:0000269|PubMed:20124701, ECO:0000269|PubMed:29608391, ECO:0000269|PubMed:32383780, ECO:0000269|PubMed:34469014};\nDE   AltName: Full=CaASADH {ECO:0000303|PubMed:17419877};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:09.278811+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d",
  "url": "https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)

```json
{
  "entry_version": 145,
  "evidence_id": "H3",
  "excerpt": "RN   [2] {ECO:0000312|Proteomes:UP000000559}\nRP   GENOME REANNOTATION.\nRC   STRAIN=SC5314 / ATCC MYA-2876 {ECO:0000312|Proteomes:UP000000559};\nRX   PubMed=17419877; DOI=10.1186/gb-2007-8-4-r52;\nRA   van het Hoog M., Rast T.J., Martchenko M., Grindle S., Dignard D.,\nRA   Hogues H., Cuomo C., Berriman M., Scherer S., Magee B.B., Whiteway M.,\nRA   Chibana H., Nantel A., Magee P.T.;\nRT   \"Assembly of the Candida albicans genome into sixteen supercontigs aligned\nRT   on the eight chromosomes.\";\nRL   Genome Biol. 8:RESEARCH52.1-RESEARCH52.12(2007).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:09.278811+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 25-34",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d",
  "url": "https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)

```json
{
  "entry_version": 145,
  "evidence_id": "H4",
  "excerpt": "RN   [5] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, AND ACTIVITY REGULATION.\nRX   PubMed=29608391; DOI=10.1177/2472555218767844;\nRA   Dahal G.P., Viola R.E.;\nRT   \"A Fragment Library Screening Approach to Identify Selective Inhibitors\nRT   against an Essential Fungal Enzyme.\";\nRL   SLAS Discovery 23:520-531(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:09.278811+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 51-57",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d",
  "url": "https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)

```json
{
  "entry_version": 145,
  "evidence_id": "H5",
  "excerpt": "RN   [6] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, AND DISRUPTION\nRP   PHENOTYPE.\nRX   PubMed=32383780; DOI=10.1002/ddr.21682;\nRA   Dahal G.P., Launder D., McKeone K.M.M., Hunter J.P., Conti H.R.,\nRA   Viola R.E.;\nRT   \"Aspartate semialdehyde dehydrogenase inhibition suppresses the growth of\nRT   the pathogenic fungus Candida albicans.\";\nRL   Drug Dev. Res. 81:736-744(2020).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:09.278811+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 58-66",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d",
  "url": "https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)

```json
{
  "entry_version": 145,
  "evidence_id": "H6",
  "excerpt": "RN   [7] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, AND ACTIVITY REGULATION.\nRX   PubMed=34469014; DOI=10.1002/ddr.21875;\nRA   Friday S.N., Cheng D.W., Zagler S.G., Zanella B.S., Dietz J.D.,\nRA   Calbat C.N., Roach L.T., Bagnal C., Faile I.S., Halkides C.J., Viola R.E.;\nRT   \"Design and testing of selective inactivators against an antifungal enzyme\nRT   target.\";\nRL   Drug Dev. Res. 83:447-460(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:09.278811+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 67-74",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d",
  "url": "https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)

```json
{
  "entry_version": 145,
  "evidence_id": "H7",
  "excerpt": "RN   [8] {ECO:0007744|PDB:3HSK}\nRP   X-RAY CRYSTALLOGRAPHY (2.20 ANGSTROMS) IN COMPLEX WITH NADP(+), FUNCTION,\nRP   CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, AND SUBUNIT.\nRX   PubMed=20124701; DOI=10.1107/s0907444909052834;\nRA   Arachea B.T., Liu X., Pavlovsky A.G., Viola R.E.;\nRT   \"Expansion of the aspartate beta-semialdehyde dehydrogenase family: the\nRT   first structure of a fungal ortholog.\";\nRL   Acta Crystallogr. D 66:205-212(2010).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:09.278811+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 75-82",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d",
  "url": "https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)

```json
{
  "entry_version": 145,
  "evidence_id": "H8",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-\nCC         L-aspartate + NADPH + H(+); Xref=Rhea:RHEA:24284, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:43474, ChEBI:CHEBI:57535, ChEBI:CHEBI:57783,\nCC         ChEBI:CHEBI:58349, ChEBI:CHEBI:537519; EC=1.2.1.11;\nCC         Evidence={ECO:0000269|PubMed:20124701, ECO:0000269|PubMed:29608391,\nCC         ECO:0000269|PubMed:32383780, ECO:0000269|PubMed:34469014};\nCC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:24286;\nCC         Evidence={ECO:0000269|PubMed:20124701, ECO:0000269|PubMed:29608391,\nCC         ECO:0000269|PubMed:32383780, ECO:0000269|PubMed:34469014};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:09.278811+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 92-101",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d",
  "url": "https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 103. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
