# pathway_0111

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0111.txt)

**Task:** `pathway`  
**Expected answer:** **C** — Amino-acid biosynthesis

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
A. capsule polysaccharide biosynthesis. .
B. peptidoglycan biosynthesis. .
C. Amino-acid biosynthesis
D. L-isoleucine from 2-oxobutanoate: step 3/4. .
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Pathway Prediction, which is to predict the primary metabolic or signaling pathway in which a given protein functions. Biological pathways are series of chemical reactions occurring within a cell that are essential for life. Based on the protein's amino acid sequence, you should identify the most relevant pathway from the given options.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt entry annotates this protein in amino-acid biosynthesis, including methionine and threonine biosynthesis. Those pathway annotations cite experimental evidence (ECO:0000269).

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with an aspartate-semialdehyde dehydrogenase family enzyme. That enzyme acts in the aspartate-family amino-acid biosynthetic pathway, making the broad amino-acid biosynthesis option a meaningful fit. The other options name capsule or peptidoglycan biosynthesis, or a specific isoleucine-pathway step, rather than this broader pathway role.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level recognition and the known metabolic role of aspartate-semialdehyde dehydrogenases provide a credible distinction among the offered choices without requiring the exact protein's database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The broad amino-acid biosynthesis choice fits the enzyme's pathway role; none of the other choices is comparably supported by the sequence and transferable family knowledge.


### Important caveats

- The sequence does not itself identify the organism; the family-level inference is sufficient for the options presented.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with an aspartate-semialdehyde dehydrogenase family enzyme. That enzyme acts in the aspartate-family amino-acid biosynthetic pathway, making the broad amino-acid biosynthesis option a meaningful fit. The other options name capsule or peptidoglycan biosynthesis, or a specific isoleucine-pathway step, rather than this broader pathway role.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition and the known metabolic role of aspartate-semialdehyde dehydrogenases provide a credible distinction among the offered choices without requiring the exact protein's database record."
  },
  "case_id": "pathway_0111",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates this protein in amino-acid biosynthesis, including methionine and threonine biosynthesis. Those pathway annotations cite experimental evidence (ECO:0000269)."
  },
  "important_caveats": [
    "The sequence does not itself identify the organism; the family-level inference is sufficient for the options presented."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The broad amino-acid biosynthesis choice fits the enzyme's pathway role; none of the other choices is comparably supported by the sequence and transferable family knowledge."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0111",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates this protein in amino-acid biosynthesis, including methionine and threonine biosynthesis. Those pathway annotations cite experimental evidence (ECO:0000269).",
    "evidence_ids": ["C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with an aspartate-semialdehyde dehydrogenase family enzyme. That enzyme acts in the aspartate-family amino-acid biosynthetic pathway, making the broad amino-acid biosynthesis option a meaningful fit. The other options name capsule or peptidoglycan biosynthesis, or a specific isoleucine-pathway step, rather than this broader pathway role.",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition and the known metabolic role of aspartate-semialdehyde dehydrogenases provide a credible distinction among the offered choices without requiring the exact protein's database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The broad amino-acid biosynthesis choice fits the enzyme's pathway role; none of the other choices is comparably supported by the sequence and transferable family knowledge."
  },
  "important_caveats": [
    "The sequence does not itself identify the organism; the family-level inference is sufficient for the options presented."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q5ALM0 identifies this protein as Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11) from Candida albicans. Its annotated pathways are 'Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway; L-homoserine from L-aspartate: step 2/3' and 'Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine from L-aspartate: step 2/5.' Both fall under the broad category 'Amino-acid biosynthesis,' matching choice C.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H7](#evidence-h7), [H8](#evidence-h8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal sequence 'GVLGATGSVG' is a canonical Rossmann-fold NAD(P)-binding motif (GxGxxG), indicating an NAD(P)-dependent dehydrogenase. The internal motif 'IICISNCSTAG' contains the catalytic cysteine in the 'CIS' context that is a hallmark of the aspartate-semialdehyde dehydrogenase (ASADH) family (EC 1.2.1.11). The overall protein length (~365 aa) and the conserved aspartate-binding region 'GADADVAGD' further match the ASADH family architecture. ASADH catalyzes the NADPH-dependent reduction of aspartyl-4-phosphate to aspartate-semialdehyde, a committed step in the aspartate biosynthetic pathway (leading to methionine, threonine, and lysine). This places it squarely in amino-acid biosynthesis (C). It is NOT a glycosyltransferase or capsule machinery enzyme (rules out A), NOT a peptidoglycan enzyme (and Candida, a fungus, does not synthesize peptidoglycan; rules out B), and NOT involved in the isoleucine-from-2-oxobutanoate pathway which involves threonine deaminase, acetohydroxyacid synthase, dihydroxyacid dehydratase, and branched-chain aminotransferase (rules out D). The family-level recognition of ASADH via the Rossmann fold plus the diagnostic catalytic Cys motif provides a concrete, transferable inference from other ASADH homologs.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence contains multiple diagnostic family-level features (Rossmann fold NAD-binding motif, catalytic CIS motif, conserved substrate-binding region, characteristic length) that allow recognition of the ASADH family without needing the specific UniProt accession or annotation for this exact protein. Family-level knowledge of ASADH's pathway assignment (aspartate pathway → amino-acid biosynthesis) is standard transferable biochemistry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options are clearly distinct pathways. ASADH's role in the aspartate pathway (amino-acid biosynthesis) is unambiguous. Option D (isoleucine from 2-oxobutanoate) involves entirely different enzymes. Options A and B involve structurally unrelated enzyme classes. No option overlap or ambiguity exists.


### Important caveats

- The Rossmann fold is shared by many dehydrogenases; the catalytic CIS motif and overall architecture are needed to specifically identify ASADH rather than another NAD-dependent dehydrogenase.
- The reviewer evidence confirms the annotation via X-ray crystallography (PDB 3HSK) and multiple enzymatic studies, providing strong experimental support for the pathway assignment.
- Option C ('Amino-acid biosynthesis') is a broad category; the specific UniProt pathway entries are more granular (methionine step 2/3, threonine step 2/5), but the broad category is correct and is the only matching option.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal sequence 'GVLGATGSVG' is a canonical Rossmann-fold NAD(P)-binding motif (GxGxxG), indicating an NAD(P)-dependent dehydrogenase. The internal motif 'IICISNCSTAG' contains the catalytic cysteine in the 'CIS' context that is a hallmark of the aspartate-semialdehyde dehydrogenase (ASADH) family (EC 1.2.1.11). The overall protein length (~365 aa) and the conserved aspartate-binding region 'GADADVAGD' further match the ASADH family architecture. ASADH catalyzes the NADPH-dependent reduction of aspartyl-4-phosphate to aspartate-semialdehyde, a committed step in the aspartate biosynthetic pathway (leading to methionine, threonine, and lysine). This places it squarely in amino-acid biosynthesis (C). It is NOT a glycosyltransferase or capsule machinery enzyme (rules out A), NOT a peptidoglycan enzyme (and Candida, a fungus, does not synthesize peptidoglycan; rules out B), and NOT involved in the isoleucine-from-2-oxobutanoate pathway which involves threonine deaminase, acetohydroxyacid synthase, dihydroxyacid dehydratase, and branched-chain aminotransferase (rules out D). The family-level recognition of ASADH via the Rossmann fold plus the diagnostic catalytic Cys motif provides a concrete, transferable inference from other ASADH homologs.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence contains multiple diagnostic family-level features (Rossmann fold NAD-binding motif, catalytic CIS motif, conserved substrate-binding region, characteristic length) that allow recognition of the ASADH family without needing the specific UniProt accession or annotation for this exact protein. Family-level knowledge of ASADH's pathway assignment (aspartate pathway → amino-acid biosynthesis) is standard transferable biochemistry."
  },
  "case_id": "pathway_0111",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H7",
      "H8"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q5ALM0 identifies this protein as Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11) from Candida albicans. Its annotated pathways are 'Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway; L-homoserine from L-aspartate: step 2/3' and 'Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine from L-aspartate: step 2/5.' Both fall under the broad category 'Amino-acid biosynthesis,' matching choice C."
  },
  "important_caveats": [
    "The Rossmann fold is shared by many dehydrogenases; the catalytic CIS motif and overall architecture are needed to specifically identify ASADH rather than another NAD-dependent dehydrogenase.",
    "The reviewer evidence confirms the annotation via X-ray crystallography (PDB 3HSK) and multiple enzymatic studies, providing strong experimental support for the pathway assignment.",
    "Option C ('Amino-acid biosynthesis') is a broad category; the specific UniProt pathway entries are more granular (methionine step 2/3, threonine step 2/5), but the broad category is correct and is the only matching option."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are clearly distinct pathways. ASADH's role in the aspartate pathway (amino-acid biosynthesis) is unambiguous. Option D (isoleucine from 2-oxobutanoate) involves entirely different enzymes. Options A and B involve structurally unrelated enzyme classes. No option overlap or ambiguity exists."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0111",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q5ALM0 identifies this protein as Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11) from Candida albicans. Its annotated pathways are 'Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway; L-homoserine from L-aspartate: step 2/3' and 'Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine from L-aspartate: step 2/5.' Both fall under the broad category 'Amino-acid biosynthesis,' matching choice C.",
    "evidence_ids": ["C4", "C5", "C6", "H7", "H8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal sequence 'GVLGATGSVG' is a canonical Rossmann-fold NAD(P)-binding motif (GxGxxG), indicating an NAD(P)-dependent dehydrogenase. The internal motif 'IICISNCSTAG' contains the catalytic cysteine in the 'CIS' context that is a hallmark of the aspartate-semialdehyde dehydrogenase (ASADH) family (EC 1.2.1.11). The overall protein length (~365 aa) and the conserved aspartate-binding region 'GADADVAGD' further match the ASADH family architecture. ASADH catalyzes the NADPH-dependent reduction of aspartyl-4-phosphate to aspartate-semialdehyde, a committed step in the aspartate biosynthetic pathway (leading to methionine, threonine, and lysine). This places it squarely in amino-acid biosynthesis (C). It is NOT a glycosyltransferase or capsule machinery enzyme (rules out A), NOT a peptidoglycan enzyme (and Candida, a fungus, does not synthesize peptidoglycan; rules out B), and NOT involved in the isoleucine-from-2-oxobutanoate pathway which involves threonine deaminase, acetohydroxyacid synthase, dihydroxyacid dehydratase, and branched-chain aminotransferase (rules out D). The family-level recognition of ASADH via the Rossmann fold plus the diagnostic catalytic Cys motif provides a concrete, transferable inference from other ASADH homologs.",
    "missing_item_specific_fact": "",
    "reason": "The sequence contains multiple diagnostic family-level features (Rossmann fold NAD-binding motif, catalytic CIS motif, conserved substrate-binding region, characteristic length) that allow recognition of the ASADH family without needing the specific UniProt accession or annotation for this exact protein. Family-level knowledge of ASADH's pathway assignment (aspartate pathway → amino-acid biosynthesis) is standard transferable biochemistry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are clearly distinct pathways. ASADH's role in the aspartate pathway (amino-acid biosynthesis) is unambiguous. Option D (isoleucine from 2-oxobutanoate) involves entirely different enzymes. Options A and B involve structurally unrelated enzyme classes. No option overlap or ambiguity exists."
  },
  "important_caveats": [
    "The Rossmann fold is shared by many dehydrogenases; the catalytic CIS motif and overall architecture are needed to specifically identify ASADH rather than another NAD-dependent dehydrogenase.",
    "The reviewer evidence confirms the annotation via X-ray crystallography (PDB 3HSK) and multiple enzymatic studies, providing strong experimental support for the pathway assignment.",
    "Option C ('Amino-acid biosynthesis') is a broad category; the specific UniProt pathway entries are more granular (methionine step 2/3, threonine step 2/5), but the broad category is correct and is the only matching option."
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
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20124701\",\"source\":\"PubMed\"}],\"value\":\"Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway; L-homoserine from L-aspartate: step 2/3\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
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
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20124701\",\"source\":\"PubMed\"}],\"value\":\"Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine from L-aspartate: step 2/5\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/5",
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

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)

```json
{
  "evidence_id": "C8",
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

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)

```json
{
  "evidence_id": "C9",
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

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)

```json
{
  "evidence_id": "C10",
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

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)

```json
{
  "evidence_id": "C11",
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

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)

```json
{
  "entry_version": 145,
  "evidence_id": "H3",
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

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)

```json
{
  "entry_version": 145,
  "evidence_id": "H4",
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

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)

```json
{
  "entry_version": 145,
  "evidence_id": "H5",
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

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)

```json
{
  "entry_version": 145,
  "evidence_id": "H6",
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

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)

```json
{
  "entry_version": 145,
  "evidence_id": "H7",
  "excerpt": "CC   -!- PATHWAY: Amino-acid biosynthesis; L-methionine biosynthesis via de novo\nCC       pathway; L-homoserine from L-aspartate: step 2/3.\nCC       {ECO:0000269|PubMed:20124701}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:09.278811+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 114-116",
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
  "excerpt": "CC   -!- PATHWAY: Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine\nCC       from L-aspartate: step 2/5. {ECO:0000269|PubMed:20124701}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:09.278811+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 117-118",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d",
  "url": "https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 111. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
