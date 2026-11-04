# pathway_0158

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0158.txt)

**Task:** `pathway`  
**Expected answer:** **C** — Secondary metabolite biosynthesis

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MEESKEEVHVAFFPFMTPGHSIPMLDLVRLFIARGVKTTVFTTPLNAPNISKYLNIIQDSSSNKNTIYVTPFPSKEAGLPEGVESQDSTTSPEMTLKFFVAMELLQDPLDVFLKETKPHCLVADNFFPYATDIASKYGIPRFVFQFTGFFPMSVMMALNRFHPQNSVSSDDDPFLVPSLPHDIKLTKSQLQREYEGSDGIDTALSRLCNGAGRALFTSYGVIFNSFYQLEPDYVDYYTNTMGKRSRVWHVGPVSLCNRRHVEGKSGRGRSASISEHLCLEWLNAKEPNSVIYVCFGSLTCFSNEQLKEIATALERCEEYFIWVLKGGKDNEQEWLPQGFEERVEGKGLIIRGWAPQVLILDHEAIGGFVTHCGWNSTLESISAGVPMVTWPIYAEQFYNEKLVTDVLKVGVKVGSMKWSETTGATHLKHEEIEKALKQIMVGEEVLEMRKRASKLKEMAYNAVEEGGSSYSHLTSLIDDLMASKAVLQKF

[Multiple Choices]
A. Cofactor biosynthesis
B. ergot alkaloid biosynthesis. .
C. Secondary metabolite biosynthesis
D. peptidoglycan biosynthesis. .
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

> The sequence-matched UniProt pathway annotation assigns the protein to secondary metabolite and terpenoid biosynthesis, supporting choice C. The annotation cites experimental evidence, although the cited paper was not independently reviewed here.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the HCGWNS region characteristic of plant family-1 UDP-dependent glycosyltransferases, which also have a conserved C-terminal PSPG region. Such enzymes commonly glycosylate specialized plant metabolites. That family-level pattern favors secondary-metabolite biosynthesis over cofactor or peptidoglycan biosynthesis; ergot alkaloid biosynthesis is a more specific pathway not suggested by this plant-like UGT signature.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence provides a transferable family-level clue that meaningfully favors the broad secondary-metabolite option. It does not establish the exact substrate or pathway on its own, but that finer specificity is not needed to distinguish these offered choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered option is comparably supported by the recognizable UGT family signature and its common role in plant specialized metabolism.


### Important caveats

- UGT family membership alone does not determine substrate specificity or prove a particular pathway; the sequence-based inference is probabilistic.
- The reviewer-only pathway annotation is sequence-matched, but its cited primary study was not independently evaluated.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the HCGWNS region characteristic of plant family-1 UDP-dependent glycosyltransferases, which also have a conserved C-terminal PSPG region. Such enzymes commonly glycosylate specialized plant metabolites. That family-level pattern favors secondary-metabolite biosynthesis over cofactor or peptidoglycan biosynthesis; ergot alkaloid biosynthesis is a more specific pathway not suggested by this plant-like UGT signature.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence provides a transferable family-level clue that meaningfully favors the broad secondary-metabolite option. It does not establish the exact substrate or pathway on its own, but that finer specificity is not needed to distinguish these offered choices."
  },
  "case_id": "pathway_0158",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt pathway annotation assigns the protein to secondary metabolite and terpenoid biosynthesis, supporting choice C. The annotation cites experimental evidence, although the cited paper was not independently reviewed here."
  },
  "important_caveats": [
    "UGT family membership alone does not determine substrate specificity or prove a particular pathway; the sequence-based inference is probabilistic.",
    "The reviewer-only pathway annotation is sequence-matched, but its cited primary study was not independently evaluated."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option is comparably supported by the recognizable UGT family signature and its common role in plant specialized metabolism."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0158",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt pathway annotation assigns the protein to secondary metabolite and terpenoid biosynthesis, supporting choice C. The annotation cites experimental evidence, although the cited paper was not independently reviewed here.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the HCGWNS region characteristic of plant family-1 UDP-dependent glycosyltransferases, which also have a conserved C-terminal PSPG region. Such enzymes commonly glycosylate specialized plant metabolites. That family-level pattern favors secondary-metabolite biosynthesis over cofactor or peptidoglycan biosynthesis; ergot alkaloid biosynthesis is a more specific pathway not suggested by this plant-like UGT signature.",
    "missing_item_specific_fact": "",
    "reason": "The sequence provides a transferable family-level clue that meaningfully favors the broad secondary-metabolite option. It does not establish the exact substrate or pathway on its own, but that finer specificity is not needed to distinguish these offered choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option is comparably supported by the recognizable UGT family signature and its common role in plant specialized metabolism."
  },
  "important_caveats": [
    "UGT family membership alone does not determine substrate specificity or prove a particular pathway; the sequence-based inference is probabilistic.",
    "The reviewer-only pathway annotation is sequence-matched, but its cited primary study was not independently evaluated."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0AAW1J1B8) explicitly annotates the PATHWAY as 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with experimental evidence (ECO:0000269, PubMed:39043959). The protein is SoUGT73M2, a UDP-glucosyltransferase involved in saponin (triterpenoid) biosynthesis in Saponaria officinalis. Choice C 'Secondary metabolite biosynthesis' directly matches the annotated pathway.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The C-terminal region contains the highly conserved 'HCGWNST' motif, which is the core of the PSPG (Plant Secondary Product Glycosyltransferase) box. This motif is diagnostic of the plant UGT superfamily. From extensive knowledge of other plant UGTs (e.g., UGT72B1 in flavonoid glycosylation, UGT71G1 in triterpenoid glycosylation, UGT85H4 in glucosinolate metabolism), plant PSPG-containing UGTs are overwhelmingly involved in secondary metabolite biosynthesis (glycosylation of terpenoids, flavonoids, phenolics, alkaloids). This family-level pattern strongly distinguishes C (Secondary metabolite biosynthesis) from A (Cofactor biosynthesis), as cofactor biosynthesis enzymes (thiamine, biotin, folate pathways) have entirely different domain architectures and lack the PSPG motif. Furthermore, the eukaryotic/plant character of the sequence (no bacterial signal peptides, no prokaryotic-specific motifs) rules out D (peptidoglycan biosynthesis, a bacterial pathway) and B (ergot alkaloid biosynthesis, a fungal pathway).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The PSPG motif identification and the well-established association of plant UGTs with secondary metabolite glycosylation constitute a concrete, transferable family-level inference. A model recognizing the PSPG box can confidently assign this protein to secondary metabolite biosynthesis rather than cofactor biosynthesis, peptidoglycan biosynthesis, or ergot alkaloid biosynthesis without needing to recall the specific UniProt annotation for this exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The PSPG motif clearly identifies a plant UGT, and the plant origin of the sequence eliminates bacterial (D) and fungal (B) pathways. The overwhelming association of PSPG-containing plant UGTs with secondary metabolite glycosylation (as opposed to cofactor biosynthesis) makes C the clear choice over A. No genuine ambiguity exists among the four options.


### Important caveats

- The specific UniProt annotation is 'Secondary metabolite biosynthesis; terpenoid biosynthesis' (saponin glycosylation). The answer choice 'Secondary metabolite biosynthesis' is the broader parent category, which is correct but less specific than the full annotation.
- The reviewer-only evidence confirms this is SoUGT73M2 from Saponaria officinalis, but this organism/protein identity was not provided to the evaluated model; the reasoning relies solely on sequence features and family-level knowledge.
- The PSPG motif recognition and plant UGT → secondary metabolism association is a strong statistical pattern across hundreds of characterized plant UGTs, making this a well-supported transferable inference rather than a lookup.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The C-terminal region contains the highly conserved 'HCGWNST' motif, which is the core of the PSPG (Plant Secondary Product Glycosyltransferase) box. This motif is diagnostic of the plant UGT superfamily. From extensive knowledge of other plant UGTs (e.g., UGT72B1 in flavonoid glycosylation, UGT71G1 in triterpenoid glycosylation, UGT85H4 in glucosinolate metabolism), plant PSPG-containing UGTs are overwhelmingly involved in secondary metabolite biosynthesis (glycosylation of terpenoids, flavonoids, phenolics, alkaloids). This family-level pattern strongly distinguishes C (Secondary metabolite biosynthesis) from A (Cofactor biosynthesis), as cofactor biosynthesis enzymes (thiamine, biotin, folate pathways) have entirely different domain architectures and lack the PSPG motif. Furthermore, the eukaryotic/plant character of the sequence (no bacterial signal peptides, no prokaryotic-specific motifs) rules out D (peptidoglycan biosynthesis, a bacterial pathway) and B (ergot alkaloid biosynthesis, a fungal pathway).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The PSPG motif identification and the well-established association of plant UGTs with secondary metabolite glycosylation constitute a concrete, transferable family-level inference. A model recognizing the PSPG box can confidently assign this protein to secondary metabolite biosynthesis rather than cofactor biosynthesis, peptidoglycan biosynthesis, or ergot alkaloid biosynthesis without needing to recall the specific UniProt annotation for this exact protein."
  },
  "case_id": "pathway_0158",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0AAW1J1B8) explicitly annotates the PATHWAY as 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with experimental evidence (ECO:0000269, PubMed:39043959). The protein is SoUGT73M2, a UDP-glucosyltransferase involved in saponin (triterpenoid) biosynthesis in Saponaria officinalis. Choice C 'Secondary metabolite biosynthesis' directly matches the annotated pathway."
  },
  "important_caveats": [
    "The specific UniProt annotation is 'Secondary metabolite biosynthesis; terpenoid biosynthesis' (saponin glycosylation). The answer choice 'Secondary metabolite biosynthesis' is the broader parent category, which is correct but less specific than the full annotation.",
    "The reviewer-only evidence confirms this is SoUGT73M2 from Saponaria officinalis, but this organism/protein identity was not provided to the evaluated model; the reasoning relies solely on sequence features and family-level knowledge.",
    "The PSPG motif recognition and plant UGT → secondary metabolism association is a strong statistical pattern across hundreds of characterized plant UGTs, making this a well-supported transferable inference rather than a lookup."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The PSPG motif clearly identifies a plant UGT, and the plant origin of the sequence eliminates bacterial (D) and fungal (B) pathways. The overwhelming association of PSPG-containing plant UGTs with secondary metabolite glycosylation (as opposed to cofactor biosynthesis) makes C the clear choice over A. No genuine ambiguity exists among the four options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0158",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0AAW1J1B8) explicitly annotates the PATHWAY as 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with experimental evidence (ECO:0000269, PubMed:39043959). The protein is SoUGT73M2, a UDP-glucosyltransferase involved in saponin (triterpenoid) biosynthesis in Saponaria officinalis. Choice C 'Secondary metabolite biosynthesis' directly matches the annotated pathway.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The C-terminal region contains the highly conserved 'HCGWNST' motif, which is the core of the PSPG (Plant Secondary Product Glycosyltransferase) box. This motif is diagnostic of the plant UGT superfamily. From extensive knowledge of other plant UGTs (e.g., UGT72B1 in flavonoid glycosylation, UGT71G1 in triterpenoid glycosylation, UGT85H4 in glucosinolate metabolism), plant PSPG-containing UGTs are overwhelmingly involved in secondary metabolite biosynthesis (glycosylation of terpenoids, flavonoids, phenolics, alkaloids). This family-level pattern strongly distinguishes C (Secondary metabolite biosynthesis) from A (Cofactor biosynthesis), as cofactor biosynthesis enzymes (thiamine, biotin, folate pathways) have entirely different domain architectures and lack the PSPG motif. Furthermore, the eukaryotic/plant character of the sequence (no bacterial signal peptides, no prokaryotic-specific motifs) rules out D (peptidoglycan biosynthesis, a bacterial pathway) and B (ergot alkaloid biosynthesis, a fungal pathway).",
    "missing_item_specific_fact": "",
    "reason": "The PSPG motif identification and the well-established association of plant UGTs with secondary metabolite glycosylation constitute a concrete, transferable family-level inference. A model recognizing the PSPG box can confidently assign this protein to secondary metabolite biosynthesis rather than cofactor biosynthesis, peptidoglycan biosynthesis, or ergot alkaloid biosynthesis without needing to recall the specific UniProt annotation for this exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The PSPG motif clearly identifies a plant UGT, and the plant origin of the sequence eliminates bacterial (D) and fungal (B) pathways. The overwhelming association of PSPG-containing plant UGTs with secondary metabolite glycosylation (as opposed to cofactor biosynthesis) makes C the clear choice over A. No genuine ambiguity exists among the four options."
  },
  "important_caveats": [
    "The specific UniProt annotation is 'Secondary metabolite biosynthesis; terpenoid biosynthesis' (saponin glycosylation). The answer choice 'Secondary metabolite biosynthesis' is the broader parent category, which is correct but less specific than the full annotation.",
    "The reviewer-only evidence confirms this is SoUGT73M2 from Saponaria officinalis, but this organism/protein identity was not provided to the evaluated model; the reasoning relies solely on sequence features and family-level knowledge.",
    "The PSPG motif recognition and plant UGT → secondary metabolism association is a strong statistical pattern across hundreds of characterized plant UGTs, making this a well-supported transferable inference rather than a lookup."
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
  "benchmark_sequence_length": 490,
  "benchmark_sequence_sha256": "38574dde61c1837c70a51ac7df20c141558020651bad992714e5afc7349bcf3a",
  "current_entry_audit": {
    "entryVersion": 6,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2024-11-27",
    "sequenceVersion": 1
  },
  "current_record_sha256": "c673150bce8700e3ac48d0cf3cdfa8862b43c3fa1f362ecadc38dc4d2f8f245f",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 490,
  "current_source_sequence_sha256": "38574dde61c1837c70a51ac7df20c141558020651bad992714e5afc7349bcf3a",
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
  "requested_accession": "A0AAW1J1B8",
  "selected_historical_entry_version": 5,
  "selected_historical_record_sha256": "2d76ff4e8a8e533685cb991ace5dd8be42507b037a55e9b0396b1981c49ac7af",
  "selected_historical_source_sequence_length": 490,
  "selected_historical_source_sequence_sha256": "38574dde61c1837c70a51ac7df20c141558020651bad992714e5afc7349bcf3a",
  "selected_historical_version": {
    "accession": "A0AAW1J1B8",
    "database": "Swiss-Prot",
    "entryVersion": 5,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "GT732_SAPOF",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1J1B8.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0AAW1J1B8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:26:32.920868+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c673150bce8700e3ac48d0cf3cdfa8862b43c3fa1f362ecadc38dc4d2f8f245f",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1J1B8.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1J1B8.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":6,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2024-11-27\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:26:32.920868+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c673150bce8700e3ac48d0cf3cdfa8862b43c3fa1f362ecadc38dc4d2f8f245f",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1J1B8.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1J1B8.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Common soapwort\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"Caryophyllales\",\"Caryophyllaceae\",\"Caryophylleae\",\"Saponaria\"],\"scientificName\":\"Saponaria officinalis\",\"synonyms\":[\"Lychnis saponaria\"],\"taxonId\":3572}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:26:32.920868+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c673150bce8700e3ac48d0cf3cdfa8862b43c3fa1f362ecadc38dc4d2f8f245f",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1J1B8.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1J1B8.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"2.4.2.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"UDP-glucosyl transferase 73M2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"SoUGT73M2\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:26:32.920868+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c673150bce8700e3ac48d0cf3cdfa8862b43c3fa1f362ecadc38dc4d2f8f245f",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1J1B8.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1J1B8.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"Secondary metabolite biosynthesis; terpenoid biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:26:32.920868+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c673150bce8700e3ac48d0cf3cdfa8862b43c3fa1f362ecadc38dc4d2f8f245f",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1J1B8.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1J1B8.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Jo S.\",\"El-Demerdash A.\",\"Owen C.\",\"Srivastava V.\",\"Wu D.\",\"Kikuchi S.\",\"Reed J.\",\"Hodgson H.\",\"Harkess A.\",\"Shu S.\",\"Plott C.\",\"Jenkins J.\",\"Williams M.\",\"Boston L.-B.\",\"Lacchini E.\",\"Qu T.\",\"Goossens A.\",\"Grimwood J.\",\"Schmutz J.\",\"Leebens-Mack J.\",\"Osbourn A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39043959\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41589-024-01681-7\"}],\"citationType\":\"journal article\",\"firstPage\":\"215\",\"id\":\"39043959\",\"journal\":\"Nat. Chem. Biol.\",\"lastPage\":\"226\",\"publicationDate\":\"2025\",\"title\":\"Unlocking saponin biosynthesis in soapwort.\",\"volume\":\"21\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"WWM48153.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"TISSUE SPECIFICITY\",\"PATHWAY\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:26:32.920868+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c673150bce8700e3ac48d0cf3cdfa8862b43c3fa1f362ecadc38dc4d2f8f245f",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1J1B8.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1J1B8?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H1",
  "excerpt": "ID   GT732_SAPOF             Reviewed;         490 AA.\nAC   A0AAW1J1B8;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   27-NOV-2024, sequence version 1.\nDT   28-JAN-2026, entry version 5.\nDE   RecName: Full=UDP-glucosyl transferase 73M2 {ECO:0000303|PubMed:39043959};\nDE            Short=SoUGT73M2 {ECO:0000303|PubMed:39043959};\nDE            EC=2.4.2.- {ECO:0000269|PubMed:39043959};\nGN   Name=UGT73M2 {ECO:0000303|PubMed:39043959};\nGN   Synonyms=Saoffv11038856m {ECO:0000303|PubMed:39043959};\nGN   ORFNames=RND81_08G000600 {ECO:0000312|EMBL:KAK9696842.1};\nOS   Saponaria officinalis (Common soapwort) (Lychnis saponaria).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   Caryophyllales; Caryophyllaceae; Caryophylleae; Saponaria.\nOX   NCBI_TaxID=3572;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:41.353913+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2d76ff4e8a8e533685cb991ace5dd8be42507b037a55e9b0396b1981c49ac7af",
  "url": "https://rest.uniprot.org/unisave/A0AAW1J1B8?format=txt&versions=5"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1J1B8?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:WWM48153.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, TISSUE\nRP   SPECIFICITY, PATHWAY, AND BIOTECHNOLOGY.\nRX   PubMed=39043959; DOI=10.1038/s41589-024-01681-7;\nRA   Jo S., El-Demerdash A., Owen C., Srivastava V., Wu D., Kikuchi S., Reed J.,\nRA   Hodgson H., Harkess A., Shu S., Plott C., Jenkins J., Williams M.,\nRA   Boston L.-B., Lacchini E., Qu T., Goossens A., Grimwood J., Schmutz J.,\nRA   Leebens-Mack J., Osbourn A.;\nRT   \"Unlocking saponin biosynthesis in soapwort.\";\nRL   Nat. Chem. Biol. 21:215-226(2025).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:41.353913+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 17-26",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2d76ff4e8a8e533685cb991ace5dd8be42507b037a55e9b0396b1981c49ac7af",
  "url": "https://rest.uniprot.org/unisave/A0AAW1J1B8?format=txt&versions=5"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1J1B8?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Secondary metabolite biosynthesis; terpenoid biosynthesis.\nCC       {ECO:0000269|PubMed:39043959}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:41.353913+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 52-53",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2d76ff4e8a8e533685cb991ace5dd8be42507b037a55e9b0396b1981c49ac7af",
  "url": "https://rest.uniprot.org/unisave/A0AAW1J1B8?format=txt&versions=5"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 158. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
