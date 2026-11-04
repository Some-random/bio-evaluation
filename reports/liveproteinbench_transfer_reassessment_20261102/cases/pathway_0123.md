# pathway_0123

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0123.txt)

**Task:** `pathway`  
**Expected answer:** **D** — Secondary metabolite biosynthesis

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MELFFICGLVLFSTLSLISLFLLHNHSSARGYRLPPGRMGWPFIGESYEFLANGWKGYPEKFIFSRLAKYKPNQVFKTSILGEKVAVMCGATCNKFLFSNEGKLVNAWWPNSVNKIFPSSTQTSSKEEAKKMRKLLPTFFKPEALQRYIPIMDEIAIRHMEDEWEGKSKIEVFPLAKRYTFWLACRLFLSIDDPVHVAKFADPFNDIASGIISIPIDLPGTPFNRGIKASNVVRQELKTIIKQRKLDLSDNKASPTQDILSHMLLTPDEDGRYMNELDIADKILGLLIGGHDTASAACTFVVKFLAELPHIYDGVYKEQMEIAKSKKEGERLNWEDIQKMKYSWNVACEVMRLAPPLQGAFREALSDFMYAGFQIPKGWKLYWSANSTHRNPECFPEPEKFDPARFDGSGPAPYTYVPFGGGPRMCPGKEYARLEILVFMHNIVKRFKWEKLIPDETIVVNPMPTPAKGLPVRLRPHSKPVTVSA

[Multiple Choices]
A. L-threonine from L-aspartate: step 4/5. .
B. NAD(+) from nicotinamide D-ribonucleotide: step 1/1. .
C. chorismate biosynthesis
D. Secondary metabolite biosynthesis
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

> The exact sequence matches the source record, whose pathway annotation identifies secondary metabolite biosynthesis and terpenoid biosynthesis, with evidence attributed to a publication (C5, H3). The record also names the protein as a beta-amyrin monooxygenase (C4), consistent with that pathway. This supports D; the supplied excerpts report the curated annotation and its evidence attribution, rather than independently presenting the underlying experimental results.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal hydrophobic segment and conserved cytochrome P450 sequence features support recognizing this as a membrane-associated P450. Plant P450s commonly catalyze oxidation steps in specialized/terpenoid metabolism. That family-level pattern favors D over the offered specific primary-metabolism steps for threonine, NAD(+), or chorismate. It is a probabilistic pathway inference, not proof of the exact substrate or pathway.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable P450 and plant-metabolism knowledge offers a meaningful distinction among these alternatives. Identifying the precise enzyme annotation from a database is not necessary to favor the broad secondary-metabolite option.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices contrast a broad secondary-metabolism category with specific primary-metabolism pathway steps; the sequence-family inference favors D among those offered.


### Important caveats

- The sequence alone supports a family-level, probabilistic inference and does not establish the precise substrate or pathway.
- The pathway annotation is attributed to experimental evidence in the source record, but the primary paper was not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment and conserved cytochrome P450 sequence features support recognizing this as a membrane-associated P450. Plant P450s commonly catalyze oxidation steps in specialized/terpenoid metabolism. That family-level pattern favors D over the offered specific primary-metabolism steps for threonine, NAD(+), or chorismate. It is a probabilistic pathway inference, not proof of the exact substrate or pathway.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable P450 and plant-metabolism knowledge offers a meaningful distinction among these alternatives. Identifying the precise enzyme annotation from a database is not necessary to favor the broad secondary-metabolite option."
  },
  "case_id": "pathway_0123",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the source record, whose pathway annotation identifies secondary metabolite biosynthesis and terpenoid biosynthesis, with evidence attributed to a publication (C5, H3). The record also names the protein as a beta-amyrin monooxygenase (C4), consistent with that pathway. This supports D; the supplied excerpts report the curated annotation and its evidence attribution, rather than independently presenting the underlying experimental results."
  },
  "important_caveats": [
    "The sequence alone supports a family-level, probabilistic inference and does not establish the precise substrate or pathway.",
    "The pathway annotation is attributed to experimental evidence in the source record, but the primary paper was not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices contrast a broad secondary-metabolism category with specific primary-metabolism pathway steps; the sequence-family inference favors D among those offered."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0123",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the source record, whose pathway annotation identifies secondary metabolite biosynthesis and terpenoid biosynthesis, with evidence attributed to a publication (C5, H3). The record also names the protein as a beta-amyrin monooxygenase (C4), consistent with that pathway. This supports D; the supplied excerpts report the curated annotation and its evidence attribution, rather than independently presenting the underlying experimental results.",
    "evidence_ids": ["C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment and conserved cytochrome P450 sequence features support recognizing this as a membrane-associated P450. Plant P450s commonly catalyze oxidation steps in specialized/terpenoid metabolism. That family-level pattern favors D over the offered specific primary-metabolism steps for threonine, NAD(+), or chorismate. It is a probabilistic pathway inference, not proof of the exact substrate or pathway.",
    "missing_item_specific_fact": "",
    "reason": "Transferable P450 and plant-metabolism knowledge offers a meaningful distinction among these alternatives. Identifying the precise enzyme annotation from a database is not necessary to favor the broad secondary-metabolite option."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices contrast a broad secondary-metabolism category with specific primary-metabolism pathway steps; the sequence-family inference favors D among those offered."
  },
  "important_caveats": [
    "The sequence alone supports a family-level, probabilistic inference and does not establish the precise substrate or pathway.",
    "The pathway annotation is attributed to experimental evidence in the source record, but the primary paper was not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0AAW1NEA3) explicitly annotates the pathway as 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with experimental evidence (ECO:0000269, PubMed:39043959). The protein is CYP716A378 (Beta-amyrin 28-monooxygenase) from Saponaria officinalis, a cytochrome P450 involved in saponin (triterpenoid) biosynthesis, which falls squarely under secondary metabolite biosynthesis.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains unmistakable cytochrome P450 signature motifs: the heme-binding motif 'FGGGPRMCPGKEY' (FGxxGxxxCxG with the conserved heme-ligating cysteine), the conserved 'IAGGHDT' motif, and the 'FPLAKRYTF' (FxxKxR) motif. The N-terminal hydrophobic stretch (MELFFICGLVLFSTLSLISLFLLHNH) is a signal peptide typical of plant membrane-associated CYP450s. A knowledgeable model recognizes this as a plant CYP450. In plant biochemistry, CYP450 enzymes are overwhelmingly associated with secondary metabolite biosynthesis (terpenoids, alkaloids, phenylpropanoids, etc.) — this is a textbook-level association. The three distractors describe primary metabolic pathways that use entirely different enzyme classes: threonine biosynthesis (homoserine dehydrogenase, threonine synthase — EC 4.x.x.x), NAD+ biosynthesis (NAD synthetase — EC 6.3.1.5), and chorismate biosynthesis (EPSP synthase, chorismate synthase — EC 4.x.x.x). None of these pathways involve CYP450 monooxygenases. Thus, recognizing the CYP450 family and the well-known plant CYP450–secondary metabolism link cleanly eliminates A, B, and C, leaving D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The CYP450 family motifs are directly readable from the sequence, and the association of plant CYP450s with secondary metabolite biosynthesis is a broad, well-established biological principle learned from many plant CYP450s (e.g., CYP71, CYP72, CYP716 families in various species). The distractor pathways are primary metabolic routes that categorically do not employ CYP450 enzymes. No target-specific annotation or memorization of this particular protein's entry is needed.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractors (A, B, C) describe primary metabolic pathways whose constituent enzymes are dehydrogenases, synthases, and transferases — none are CYP450s. Once the CYP450 family is recognized, only option D (secondary metabolite biosynthesis) is compatible with a CYP450 enzyme. No other option is defensible.


### Important caveats

- The reviewer-only evidence confirms the protein is CYP716A378 (Beta-amyrin 28-monooxygenase) from Saponaria officinalis, but this specific identity was not available to the evaluated model.
- The pathway annotation in UniProt is backed by experimental evidence (ECO:0000269) from a 2025 Nat. Chem. Biol. paper on saponin biosynthesis in soapwort.
- The sequence match between the benchmark input and the UniProt entry is exact (SHA-256 match confirmed).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains unmistakable cytochrome P450 signature motifs: the heme-binding motif 'FGGGPRMCPGKEY' (FGxxGxxxCxG with the conserved heme-ligating cysteine), the conserved 'IAGGHDT' motif, and the 'FPLAKRYTF' (FxxKxR) motif. The N-terminal hydrophobic stretch (MELFFICGLVLFSTLSLISLFLLHNH) is a signal peptide typical of plant membrane-associated CYP450s. A knowledgeable model recognizes this as a plant CYP450. In plant biochemistry, CYP450 enzymes are overwhelmingly associated with secondary metabolite biosynthesis (terpenoids, alkaloids, phenylpropanoids, etc.) — this is a textbook-level association. The three distractors describe primary metabolic pathways that use entirely different enzyme classes: threonine biosynthesis (homoserine dehydrogenase, threonine synthase — EC 4.x.x.x), NAD+ biosynthesis (NAD synthetase — EC 6.3.1.5), and chorismate biosynthesis (EPSP synthase, chorismate synthase — EC 4.x.x.x). None of these pathways involve CYP450 monooxygenases. Thus, recognizing the CYP450 family and the well-known plant CYP450–secondary metabolism link cleanly eliminates A, B, and C, leaving D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The CYP450 family motifs are directly readable from the sequence, and the association of plant CYP450s with secondary metabolite biosynthesis is a broad, well-established biological principle learned from many plant CYP450s (e.g., CYP71, CYP72, CYP716 families in various species). The distractor pathways are primary metabolic routes that categorically do not employ CYP450 enzymes. No target-specific annotation or memorization of this particular protein's entry is needed."
  },
  "case_id": "pathway_0123",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0AAW1NEA3) explicitly annotates the pathway as 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with experimental evidence (ECO:0000269, PubMed:39043959). The protein is CYP716A378 (Beta-amyrin 28-monooxygenase) from Saponaria officinalis, a cytochrome P450 involved in saponin (triterpenoid) biosynthesis, which falls squarely under secondary metabolite biosynthesis."
  },
  "important_caveats": [
    "The reviewer-only evidence confirms the protein is CYP716A378 (Beta-amyrin 28-monooxygenase) from Saponaria officinalis, but this specific identity was not available to the evaluated model.",
    "The pathway annotation in UniProt is backed by experimental evidence (ECO:0000269) from a 2025 Nat. Chem. Biol. paper on saponin biosynthesis in soapwort.",
    "The sequence match between the benchmark input and the UniProt entry is exact (SHA-256 match confirmed)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (A, B, C) describe primary metabolic pathways whose constituent enzymes are dehydrogenases, synthases, and transferases — none are CYP450s. Once the CYP450 family is recognized, only option D (secondary metabolite biosynthesis) is compatible with a CYP450 enzyme. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0123",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0AAW1NEA3) explicitly annotates the pathway as 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with experimental evidence (ECO:0000269, PubMed:39043959). The protein is CYP716A378 (Beta-amyrin 28-monooxygenase) from Saponaria officinalis, a cytochrome P450 involved in saponin (triterpenoid) biosynthesis, which falls squarely under secondary metabolite biosynthesis.",
    "evidence_ids": ["C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains unmistakable cytochrome P450 signature motifs: the heme-binding motif 'FGGGPRMCPGKEY' (FGxxGxxxCxG with the conserved heme-ligating cysteine), the conserved 'IAGGHDT' motif, and the 'FPLAKRYTF' (FxxKxR) motif. The N-terminal hydrophobic stretch (MELFFICGLVLFSTLSLISLFLLHNH) is a signal peptide typical of plant membrane-associated CYP450s. A knowledgeable model recognizes this as a plant CYP450. In plant biochemistry, CYP450 enzymes are overwhelmingly associated with secondary metabolite biosynthesis (terpenoids, alkaloids, phenylpropanoids, etc.) — this is a textbook-level association. The three distractors describe primary metabolic pathways that use entirely different enzyme classes: threonine biosynthesis (homoserine dehydrogenase, threonine synthase — EC 4.x.x.x), NAD+ biosynthesis (NAD synthetase — EC 6.3.1.5), and chorismate biosynthesis (EPSP synthase, chorismate synthase — EC 4.x.x.x). None of these pathways involve CYP450 monooxygenases. Thus, recognizing the CYP450 family and the well-known plant CYP450–secondary metabolism link cleanly eliminates A, B, and C, leaving D.",
    "missing_item_specific_fact": "",
    "reason": "The CYP450 family motifs are directly readable from the sequence, and the association of plant CYP450s with secondary metabolite biosynthesis is a broad, well-established biological principle learned from many plant CYP450s (e.g., CYP71, CYP72, CYP716 families in various species). The distractor pathways are primary metabolic routes that categorically do not employ CYP450 enzymes. No target-specific annotation or memorization of this particular protein's entry is needed."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (A, B, C) describe primary metabolic pathways whose constituent enzymes are dehydrogenases, synthases, and transferases — none are CYP450s. Once the CYP450 family is recognized, only option D (secondary metabolite biosynthesis) is compatible with a CYP450 enzyme. No other option is defensible."
  },
  "important_caveats": [
    "The reviewer-only evidence confirms the protein is CYP716A378 (Beta-amyrin 28-monooxygenase) from Saponaria officinalis, but this specific identity was not available to the evaluated model.",
    "The pathway annotation in UniProt is backed by experimental evidence (ECO:0000269) from a 2025 Nat. Chem. Biol. paper on saponin biosynthesis in soapwort.",
    "The sequence match between the benchmark input and the UniProt entry is exact (SHA-256 match confirmed)."
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
  "benchmark_sequence_length": 485,
  "benchmark_sequence_sha256": "c4bff1f7e639d9ca658ce7a8d1b4bea128f38e1d86d04bfb0390444eed1c9e39",
  "current_entry_audit": {
    "entryVersion": 6,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2024-11-27",
    "sequenceVersion": 1
  },
  "current_record_sha256": "3395db4e25f9768c60ce7cac240774ed32dd3f474abfda702e2c591ef35e9a76",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 485,
  "current_source_sequence_sha256": "c4bff1f7e639d9ca658ce7a8d1b4bea128f38e1d86d04bfb0390444eed1c9e39",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 5,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0AAW1NEA3",
  "selected_historical_entry_version": 5,
  "selected_historical_record_sha256": "8601238c4d3910ff611c06a4f863e8c633074e9e3c66a978a480c31233a972f5",
  "selected_historical_source_sequence_length": 485,
  "selected_historical_source_sequence_sha256": "c4bff1f7e639d9ca658ce7a8d1b4bea128f38e1d86d04bfb0390444eed1c9e39",
  "selected_historical_version": {
    "accession": "A0AAW1NEA3",
    "database": "Swiss-Prot",
    "entryVersion": 5,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "C7168_SAPOF",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1NEA3.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0AAW1NEA3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:55.776537+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3395db4e25f9768c60ce7cac240774ed32dd3f474abfda702e2c591ef35e9a76",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1NEA3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1NEA3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":6,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2024-11-27\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:55.776537+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3395db4e25f9768c60ce7cac240774ed32dd3f474abfda702e2c591ef35e9a76",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1NEA3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1NEA3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Common soapwort\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"Caryophyllales\",\"Caryophyllaceae\",\"Caryophylleae\",\"Saponaria\"],\"scientificName\":\"Saponaria officinalis\",\"synonyms\":[\"Lychnis saponaria\"],\"taxonId\":3572}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:55.776537+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3395db4e25f9768c60ce7cac240774ed32dd3f474abfda702e2c591ef35e9a76",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1NEA3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1NEA3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"Cytochrome P450 716A378\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"SoCYP716A378\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"1.14.14.126\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Beta-amyrin 28-monooxygenase CYP716A378\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:55.776537+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3395db4e25f9768c60ce7cac240774ed32dd3f474abfda702e2c591ef35e9a76",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1NEA3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1NEA3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"Secondary metabolite biosynthesis; terpenoid biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-01T06:24:55.776537+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3395db4e25f9768c60ce7cac240774ed32dd3f474abfda702e2c591ef35e9a76",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1NEA3.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1NEA3.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Jo S.\",\"El-Demerdash A.\",\"Owen C.\",\"Srivastava V.\",\"Wu D.\",\"Kikuchi S.\",\"Reed J.\",\"Hodgson H.\",\"Harkess A.\",\"Shu S.\",\"Plott C.\",\"Jenkins J.\",\"Williams M.\",\"Boston L.-B.\",\"Lacchini E.\",\"Qu T.\",\"Goossens A.\",\"Grimwood J.\",\"Schmutz J.\",\"Leebens-Mack J.\",\"Osbourn A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39043959\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41589-024-01681-7\"}],\"citationType\":\"journal article\",\"firstPage\":\"215\",\"id\":\"39043959\",\"journal\":\"Nat. Chem. Biol.\",\"lastPage\":\"226\",\"publicationDate\":\"2025\",\"title\":\"Unlocking saponin biosynthesis in soapwort.\",\"volume\":\"21\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"WWM48148.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"TISSUE SPECIFICITY\",\"PATHWAY\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:24:55.776537+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3395db4e25f9768c60ce7cac240774ed32dd3f474abfda702e2c591ef35e9a76",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1NEA3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1NEA3?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H1",
  "excerpt": "ID   C7168_SAPOF             Reviewed;         485 AA.\nAC   A0AAW1NEA3;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   27-NOV-2024, sequence version 1.\nDT   28-JAN-2026, entry version 5.\nDE   RecName: Full=Beta-amyrin 28-monooxygenase CYP716A378 {ECO:0000305};\nDE            EC=1.14.14.126 {ECO:0000269|PubMed:39043959};\nDE   AltName: Full=Cytochrome P450 716A378 {ECO:0000303|PubMed:39043959};\nDE            Short=SoCYP716A378 {ECO:0000303|PubMed:39043959};\nGN   Name=CYP716A378 {ECO:0000303|PubMed:39043959};\nGN   Synonyms=Saoffv11003497m {ECO:0000303|PubMed:39043959};\nGN   ORFNames=RND81_01G137900 {ECO:0000312|EMBL:KAK9757076.1};\nOS   Saponaria officinalis (Common soapwort) (Lychnis saponaria).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   Caryophyllales; Caryophyllaceae; Caryophylleae; Saponaria.\nOX   NCBI_TaxID=3572;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:40.561544+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8601238c4d3910ff611c06a4f863e8c633074e9e3c66a978a480c31233a972f5",
  "url": "https://rest.uniprot.org/unisave/A0AAW1NEA3?format=txt&versions=5"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1NEA3?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:WWM48148.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, TISSUE\nRP   SPECIFICITY, PATHWAY, AND BIOTECHNOLOGY.\nRX   PubMed=39043959; DOI=10.1038/s41589-024-01681-7;\nRA   Jo S., El-Demerdash A., Owen C., Srivastava V., Wu D., Kikuchi S., Reed J.,\nRA   Hodgson H., Harkess A., Shu S., Plott C., Jenkins J., Williams M.,\nRA   Boston L.-B., Lacchini E., Qu T., Goossens A., Grimwood J., Schmutz J.,\nRA   Leebens-Mack J., Osbourn A.;\nRT   \"Unlocking saponin biosynthesis in soapwort.\";\nRL   Nat. Chem. Biol. 21:215-226(2025).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:40.561544+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 18-27",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8601238c4d3910ff611c06a4f863e8c633074e9e3c66a978a480c31233a972f5",
  "url": "https://rest.uniprot.org/unisave/A0AAW1NEA3?format=txt&versions=5"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1NEA3?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Secondary metabolite biosynthesis; terpenoid biosynthesis.\nCC       {ECO:0000269|PubMed:39043959}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:40.561544+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 55-56",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8601238c4d3910ff611c06a4f863e8c633074e9e3c66a978a480c31233a972f5",
  "url": "https://rest.uniprot.org/unisave/A0AAW1NEA3?format=txt&versions=5"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 123. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
