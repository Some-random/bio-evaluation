# GO_molecular_function_0187

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0187.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **A** — UDP-glucosyltransferase activity

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MGTKELHIVMYPWLAFGHFIPYLHLSNKLAQKGHKITFLLPHRAKLQLDSQNLYPSLITLVPITVPQVDTLPLGAESTADIPLSQHGDLSIAMDRTRPEIESILSKLDPKPDLIFFDMAQWVPVIASKLGIKSVSYNIVCAISLDLVRDWYKKDDGSNVPSWTLKHDKSSHFGENISILERALIALGTPDAIGIRSCREIEGEYCDSIAERFKKPVLLSGTTLPEPSDDPLDPKWVKWLGKFEEGSVIFCCLGSQHVLDKPQLQELALGLEMTGLPFFLAIKPPLGYATLDEVLPEGFSERVRDRGVAHGGWVQQPQMLAHPSVGCFLCHCGSSSMWEALVSDTQLVLFPQIPDQALNAVLMADKLKVGVKVEREDDGGVSKEVWSRAIKSVMDKESEIAAEVKKNHTKWRDMLINEEFVNGYIDSFIKDLQDLVEK

[Multiple Choices]
A. UDP-glucosyltransferase activity
B. promoter-specific chromatin binding
C. calmodulin binding
D. URM1 activating enzyme activity
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Molecular Function Prediction, which is to predict the fundamental activity of a protein at the molecular level, as defined by the Gene Ontology (GO) 'Molecular Function' branch. This describes the elemental tasks a protein performs, such as catalysis, transport, or binding to specific molecules. Based on the protein's amino acid sequence, you are to select the option that best describes its primary molecular function.. The inputs provided by the user for this task include:

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

> The sequence-matched record annotates UDP-glucosyltransferase activity by InterPro inference, and independently supports UDP-glycosyltransferase activity experimentally. However, the reported specific reaction transfers xylose from UDP-xylose, not glucose from UDP-glucose, so the exact wording of option A is not a precise description of that reaction.

Citations as saved: [C7](#evidence-c7), [C8](#evidence-c8), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 437-aa sequence is consistent with a soluble plant family-1 UDP-dependent glycosyltransferase, including a conserved C-terminal UGT-like region. Transferable family knowledge supports a sugar-transfer enzyme, distinguishing option A from chromatin binding, calmodulin binding, and URM1-activating enzyme activity.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level sequence features and the contrast among the offered choices give a meaningful basis to select the glycosyltransferase option. The sequence alone is less informative about the exact sugar donor: the characterized reaction uses UDP-xylose, so the choice's glucose-specific wording should be treated as an approximation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only option A describes the relevant class of enzymatic activity among the choices, although its glucose-specific wording does not match the reported xylose-transfer reaction.


### Important caveats

- The exact GO-term annotation is computationally inferred; the record's experimentally supported reaction is UDP-xylose-dependent xylosyl transfer.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 437-aa sequence is consistent with a soluble plant family-1 UDP-dependent glycosyltransferase, including a conserved C-terminal UGT-like region. Transferable family knowledge supports a sugar-transfer enzyme, distinguishing option A from chromatin binding, calmodulin binding, and URM1-activating enzyme activity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence features and the contrast among the offered choices give a meaningful basis to select the glycosyltransferase option. The sequence alone is less informative about the exact sugar donor: the characterized reaction uses UDP-xylose, so the choice's glucose-specific wording should be treated as an approximation."
  },
  "case_id": "GO_molecular_function_0187",
  "expected_answer_check": {
    "evidence_ids": [
      "C7",
      "C8",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched record annotates UDP-glucosyltransferase activity by InterPro inference, and independently supports UDP-glycosyltransferase activity experimentally. However, the reported specific reaction transfers xylose from UDP-xylose, not glucose from UDP-glucose, so the exact wording of option A is not a precise description of that reaction."
  },
  "important_caveats": [
    "The exact GO-term annotation is computationally inferred; the record's experimentally supported reaction is UDP-xylose-dependent xylosyl transfer."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option A describes the relevant class of enzymatic activity among the choices, although its glucose-specific wording does not match the reported xylose-transfer reaction."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0187",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched record annotates UDP-glucosyltransferase activity by InterPro inference, and independently supports UDP-glycosyltransferase activity experimentally. However, the reported specific reaction transfers xylose from UDP-xylose, not glucose from UDP-glucose, so the exact wording of option A is not a precise description of that reaction.",
    "evidence_ids": ["C7", "C8", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 437-aa sequence is consistent with a soluble plant family-1 UDP-dependent glycosyltransferase, including a conserved C-terminal UGT-like region. Transferable family knowledge supports a sugar-transfer enzyme, distinguishing option A from chromatin binding, calmodulin binding, and URM1-activating enzyme activity.",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence features and the contrast among the offered choices give a meaningful basis to select the glycosyltransferase option. The sequence alone is less informative about the exact sugar donor: the characterized reaction uses UDP-xylose, so the choice's glucose-specific wording should be treated as an approximation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option A describes the relevant class of enzymatic activity among the choices, although its glucose-specific wording does not match the reported xylose-transfer reaction."
  },
  "important_caveats": [
    "The exact GO-term annotation is computationally inferred; the record's experimentally supported reaction is UDP-xylose-dependent xylosyl transfer."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry annotates this protein (A0AAW1MQS1, Saponaria officinalis UGT79L3) with GO:0035251 UDP-glucosyltransferase activity via IEA:InterPro (evidence C7/H5). The protein is named 'UDP-glucosyl transferase 79L3' and assigned EC 2.4.2.-. The experimental evidence (IDA) supports the parent term GO:0008194 UDP-glycosyltransferase activity, and the actual catalytic reaction transfers a xylosyl group from UDP-xylose rather than a glucosyl group from UDP-glucose. However, the specific GO:0035251 annotation is present in the database via InterPro domain matching to the UGT79 family, and the protein name reflects family nomenclature. The expected answer is supported by the database annotation, though the experimental substrate specificity (xylose transfer) aligns more precisely with the parent GO term.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [C8](#evidence-c8), [H1](#evidence-h1), [H3](#evidence-h3), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 437-residue sequence contains features consistent with the plant UDP-glycosyltransferase (UGT) superfamily: (1) the C-terminal ~100 residues contain a PSPG-box-like motif (visible patterns including 'GGWVQQPQ', 'CFLCHCGSSSMWEALVSDTQ', and the conserved 'PQ' and 'S' residues characteristic of plant UGTs); (2) the overall length and two-domain architecture (N-terminal acceptor-binding domain + C-terminal sugar-donor/PSPG domain) matches the canonical plant UGT fold; (3) plant UGTs are one of the largest enzyme families in plants, numbering hundreds of members, and the PSPG-box is a widely taught, transferable diagnostic feature. Against the distractors: Option B (promoter-specific chromatin binding) requires DNA/chromatin-binding domains (zinc fingers, homeodomains, etc.) absent here; Option C (calmodulin binding) requires amphipathic basic helical motifs not present; Option D (URM1 activating enzyme) requires an E1-like adenylation fold with distinct catalytic motifs not found in this sequence. The family-level recognition of plant UGT domain architecture meaningfully distinguishes A from B, C, and D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model familiar with plant UGT families can recognize the PSPG-box motif and two-domain architecture in the C-terminal region, the characteristic protein length (~437 AA), and the overall composition. This is a well-known, transferable family-level pattern shared across hundreds of plant UGTs. The three distractors represent completely unrelated molecular functions (chromatin binding, calmodulin binding, E1-enzyme activity) with no sequence features supporting them. The inference does not require knowing this exact protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four offered choices, only A describes a glycosyltransferase activity. The protein's actual catalytic activity transfers xylose (making it technically a UDP-xylosyltransferase, a child of UDP-glycosyltransferase), but option A (UDP-glucosyltransferase activity) is the closest and only glycosyltransferase option presented. Options B, C, and D are entirely unrelated functions with no supporting sequence evidence. No ambiguity exists among the offered alternatives.


### Important caveats

- The GO:0035251 annotation is IEA:InterPro (computational inference from domain match), while the experimental evidence (IDA) supports the broader parent term GO:0008194 UDP-glycosyltransferase activity.
- The actual catalytic reaction shows transfer of a xylosyl group from UDP-xylose, not a glucosyl group from UDP-glucose, making the protein technically a UDP-xylosyltransferase. The name 'UDP-glucosyl transferase 79L3' reflects UGT79 family nomenclature convention.
- The sequence was retrieved and matched to UniProt entry A0AAW1MQS1 (Saponaria officinalis), but organism identity and protein name were not provided to the evaluated model.
- The PSPG-box recognition argument relies on general plant UGT family knowledge transferable across hundreds of homologs, not on memorizing this specific protein's annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 437-residue sequence contains features consistent with the plant UDP-glycosyltransferase (UGT) superfamily: (1) the C-terminal ~100 residues contain a PSPG-box-like motif (visible patterns including 'GGWVQQPQ', 'CFLCHCGSSSMWEALVSDTQ', and the conserved 'PQ' and 'S' residues characteristic of plant UGTs); (2) the overall length and two-domain architecture (N-terminal acceptor-binding domain + C-terminal sugar-donor/PSPG domain) matches the canonical plant UGT fold; (3) plant UGTs are one of the largest enzyme families in plants, numbering hundreds of members, and the PSPG-box is a widely taught, transferable diagnostic feature. Against the distractors: Option B (promoter-specific chromatin binding) requires DNA/chromatin-binding domains (zinc fingers, homeodomains, etc.) absent here; Option C (calmodulin binding) requires amphipathic basic helical motifs not present; Option D (URM1 activating enzyme) requires an E1-like adenylation fold with distinct catalytic motifs not found in this sequence. The family-level recognition of plant UGT domain architecture meaningfully distinguishes A from B, C, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model familiar with plant UGT families can recognize the PSPG-box motif and two-domain architecture in the C-terminal region, the characteristic protein length (~437 AA), and the overall composition. This is a well-known, transferable family-level pattern shared across hundreds of plant UGTs. The three distractors represent completely unrelated molecular functions (chromatin binding, calmodulin binding, E1-enzyme activity) with no sequence features supporting them. The inference does not require knowing this exact protein's annotation."
  },
  "case_id": "GO_molecular_function_0187",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "C8",
      "H1",
      "H3",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry annotates this protein (A0AAW1MQS1, Saponaria officinalis UGT79L3) with GO:0035251 UDP-glucosyltransferase activity via IEA:InterPro (evidence C7/H5). The protein is named 'UDP-glucosyl transferase 79L3' and assigned EC 2.4.2.-. The experimental evidence (IDA) supports the parent term GO:0008194 UDP-glycosyltransferase activity, and the actual catalytic reaction transfers a xylosyl group from UDP-xylose rather than a glucosyl group from UDP-glucose. However, the specific GO:0035251 annotation is present in the database via InterPro domain matching to the UGT79 family, and the protein name reflects family nomenclature. The expected answer is supported by the database annotation, though the experimental substrate specificity (xylose transfer) aligns more precisely with the parent GO term."
  },
  "important_caveats": [
    "The GO:0035251 annotation is IEA:InterPro (computational inference from domain match), while the experimental evidence (IDA) supports the broader parent term GO:0008194 UDP-glycosyltransferase activity.",
    "The actual catalytic reaction shows transfer of a xylosyl group from UDP-xylose, not a glucosyl group from UDP-glucose, making the protein technically a UDP-xylosyltransferase. The name 'UDP-glucosyl transferase 79L3' reflects UGT79 family nomenclature convention.",
    "The sequence was retrieved and matched to UniProt entry A0AAW1MQS1 (Saponaria officinalis), but organism identity and protein name were not provided to the evaluated model.",
    "The PSPG-box recognition argument relies on general plant UGT family knowledge transferable across hundreds of homologs, not on memorizing this specific protein's annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four offered choices, only A describes a glycosyltransferase activity. The protein's actual catalytic activity transfers xylose (making it technically a UDP-xylosyltransferase, a child of UDP-glycosyltransferase), but option A (UDP-glucosyltransferase activity) is the closest and only glycosyltransferase option presented. Options B, C, and D are entirely unrelated functions with no supporting sequence evidence. No ambiguity exists among the offered alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0187",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry annotates this protein (A0AAW1MQS1, Saponaria officinalis UGT79L3) with GO:0035251 UDP-glucosyltransferase activity via IEA:InterPro (evidence C7/H5). The protein is named 'UDP-glucosyl transferase 79L3' and assigned EC 2.4.2.-. The experimental evidence (IDA) supports the parent term GO:0008194 UDP-glycosyltransferase activity, and the actual catalytic reaction transfers a xylosyl group from UDP-xylose rather than a glucosyl group from UDP-glucose. However, the specific GO:0035251 annotation is present in the database via InterPro domain matching to the UGT79 family, and the protein name reflects family nomenclature. The expected answer is supported by the database annotation, though the experimental substrate specificity (xylose transfer) aligns more precisely with the parent GO term.",
    "evidence_ids": ["C4", "C5", "C7", "C8", "H1", "H3", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 437-residue sequence contains features consistent with the plant UDP-glycosyltransferase (UGT) superfamily: (1) the C-terminal ~100 residues contain a PSPG-box-like motif (visible patterns including 'GGWVQQPQ', 'CFLCHCGSSSMWEALVSDTQ', and the conserved 'PQ' and 'S' residues characteristic of plant UGTs); (2) the overall length and two-domain architecture (N-terminal acceptor-binding domain + C-terminal sugar-donor/PSPG domain) matches the canonical plant UGT fold; (3) plant UGTs are one of the largest enzyme families in plants, numbering hundreds of members, and the PSPG-box is a widely taught, transferable diagnostic feature. Against the distractors: Option B (promoter-specific chromatin binding) requires DNA/chromatin-binding domains (zinc fingers, homeodomains, etc.) absent here; Option C (calmodulin binding) requires amphipathic basic helical motifs not present; Option D (URM1 activating enzyme) requires an E1-like adenylation fold with distinct catalytic motifs not found in this sequence. The family-level recognition of plant UGT domain architecture meaningfully distinguishes A from B, C, and D.",
    "missing_item_specific_fact": "",
    "reason": "A model familiar with plant UGT families can recognize the PSPG-box motif and two-domain architecture in the C-terminal region, the characteristic protein length (~437 AA), and the overall composition. This is a well-known, transferable family-level pattern shared across hundreds of plant UGTs. The three distractors represent completely unrelated molecular functions (chromatin binding, calmodulin binding, E1-enzyme activity) with no sequence features supporting them. The inference does not require knowing this exact protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four offered choices, only A describes a glycosyltransferase activity. The protein's actual catalytic activity transfers xylose (making it technically a UDP-xylosyltransferase, a child of UDP-glycosyltransferase), but option A (UDP-glucosyltransferase activity) is the closest and only glycosyltransferase option presented. Options B, C, and D are entirely unrelated functions with no supporting sequence evidence. No ambiguity exists among the offered alternatives."
  },
  "important_caveats": [
    "The GO:0035251 annotation is IEA:InterPro (computational inference from domain match), while the experimental evidence (IDA) supports the broader parent term GO:0008194 UDP-glycosyltransferase activity.",
    "The actual catalytic reaction shows transfer of a xylosyl group from UDP-xylose, not a glucosyl group from UDP-glucose, making the protein technically a UDP-xylosyltransferase. The name 'UDP-glucosyl transferase 79L3' reflects UGT79 family nomenclature convention.",
    "The sequence was retrieved and matched to UniProt entry A0AAW1MQS1 (Saponaria officinalis), but organism identity and protein name were not provided to the evaluated model.",
    "The PSPG-box recognition argument relies on general plant UGT family knowledge transferable across hundreds of homologs, not on memorizing this specific protein's annotation."
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
  "benchmark_sequence_length": 437,
  "benchmark_sequence_sha256": "6bb6cd7df8beb3e823913728b78639b24d082aeb08dc43d88a233bde6c26bfc9",
  "current_entry_audit": {
    "entryVersion": 6,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2024-11-27",
    "sequenceVersion": 1
  },
  "current_record_sha256": "38e19d62d1e2fd0bdb2dcb0078a06ec483bdc0582d78b80c6fe365d966217911",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 437,
  "current_source_sequence_sha256": "6bb6cd7df8beb3e823913728b78639b24d082aeb08dc43d88a233bde6c26bfc9",
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
  "requested_accession": "A0AAW1MQS1",
  "selected_historical_entry_version": 5,
  "selected_historical_record_sha256": "c9be8c78f74c494bf89b7deeee4376bf5b587b49421d7bfa1cdf2a6c1852ed8b",
  "selected_historical_source_sequence_length": 437,
  "selected_historical_source_sequence_sha256": "6bb6cd7df8beb3e823913728b78639b24d082aeb08dc43d88a233bde6c26bfc9",
  "selected_historical_version": {
    "accession": "A0AAW1MQS1",
    "database": "Swiss-Prot",
    "entryVersion": 5,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "GT793_SAPOF",
    "sequenceVersion": 1
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1MQS1.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0AAW1MQS1\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:26:42.921794+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "38e19d62d1e2fd0bdb2dcb0078a06ec483bdc0582d78b80c6fe365d966217911",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1MQS1.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1MQS1.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":6,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2024-11-27\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:26:42.921794+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "38e19d62d1e2fd0bdb2dcb0078a06ec483bdc0582d78b80c6fe365d966217911",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1MQS1.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1MQS1.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Common soapwort\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"Caryophyllales\",\"Caryophyllaceae\",\"Caryophylleae\",\"Saponaria\"],\"scientificName\":\"Saponaria officinalis\",\"synonyms\":[\"Lychnis saponaria\"],\"taxonId\":3572}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:26:42.921794+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "38e19d62d1e2fd0bdb2dcb0078a06ec483bdc0582d78b80c6fe365d966217911",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1MQS1.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1MQS1.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"2.4.2.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"UDP-glucosyl transferase 79L3\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"SoUGT79L3\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:26:42.921794+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "38e19d62d1e2fd0bdb2dcb0078a06ec483bdc0582d78b80c6fe365d966217911",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1MQS1.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1MQS1.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"Component of the oleanane-type triterpene saponins (e.g. saponarioside A and saponarioside B) biosynthetic pathway, leading to the production of natural products with detergent properties used as traditional sources of soap (PubMed:39043959). A glycosyltransferase that mediates the conversion of QA-triFR to QA-triFRX via the elongation of the C-28 sugar chain with a D-xylose (PubMed:39043959)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:26:42.921794+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "38e19d62d1e2fd0bdb2dcb0078a06ec483bdc0582d78b80c6fe365d966217911",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1MQS1.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1MQS1.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:85056\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"name\":\"3-O-{beta-D-Xyl-(1->3)-[beta-D-Gal-(1->2)]-beta-D-GlcA}-quillaic acid alpha-L-Rha-(1->2)-beta-D-Fuc ester + UDP-alpha-D-xylose = 3-O-{beta-D-Xyl-(1->3)-[beta-D-Gal-(1->2)]-beta-D-GlcA}-quillaic acid beta-D-Xyl-(1->4)-alpha-L-Rha-(1->2)-beta-D-Fuc ester + UDP + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:85055\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57632\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58223\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:234167\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:234168\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:26:42.921794+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "38e19d62d1e2fd0bdb2dcb0078a06ec483bdc0582d78b80c6fe365d966217911",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1MQS1.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1MQS1.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0035251\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:UDP-glucosyltransferase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:InterPro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/6",
  "retrieved_utc": "2026-11-02T04:26:42.921794+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "38e19d62d1e2fd0bdb2dcb0078a06ec483bdc0582d78b80c6fe365d966217911",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1MQS1.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1MQS1.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"id\":\"GO:0008194\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:UDP-glycosyltransferase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/7",
  "retrieved_utc": "2026-11-02T04:26:42.921794+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "38e19d62d1e2fd0bdb2dcb0078a06ec483bdc0582d78b80c6fe365d966217911",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1MQS1.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1MQS1.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Jo S.\",\"El-Demerdash A.\",\"Owen C.\",\"Srivastava V.\",\"Wu D.\",\"Kikuchi S.\",\"Reed J.\",\"Hodgson H.\",\"Harkess A.\",\"Shu S.\",\"Plott C.\",\"Jenkins J.\",\"Williams M.\",\"Boston L.-B.\",\"Lacchini E.\",\"Qu T.\",\"Goossens A.\",\"Grimwood J.\",\"Schmutz J.\",\"Leebens-Mack J.\",\"Osbourn A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39043959\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41589-024-01681-7\"}],\"citationType\":\"journal article\",\"firstPage\":\"215\",\"id\":\"39043959\",\"journal\":\"Nat. Chem. Biol.\",\"lastPage\":\"226\",\"publicationDate\":\"2025\",\"title\":\"Unlocking saponin biosynthesis in soapwort.\",\"volume\":\"21\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"WWM48150.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"TISSUE SPECIFICITY\",\"PATHWAY\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:26:42.921794+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "38e19d62d1e2fd0bdb2dcb0078a06ec483bdc0582d78b80c6fe365d966217911",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1MQS1.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1MQS1?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H1",
  "excerpt": "ID   GT793_SAPOF             Reviewed;         437 AA.\nAC   A0AAW1MQS1;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   27-NOV-2024, sequence version 1.\nDT   28-JAN-2026, entry version 5.\nDE   RecName: Full=UDP-glucosyl transferase 79L3 {ECO:0000303|PubMed:39043959};\nDE            Short=SoUGT79L3 {ECO:0000303|PubMed:39043959};\nDE            EC=2.4.2.- {ECO:0000269|PubMed:39043959};\nGN   Name=UGT79L3 {ECO:0000303|PubMed:39043959};\nGN   Synonyms=Saoffv11006237m {ECO:0000303|PubMed:39043959};\nGN   ORFNames=RND81_02G054000 {ECO:0000312|EMBL:KAK9748391.1};\nOS   Saponaria officinalis (Common soapwort) (Lychnis saponaria).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   Caryophyllales; Caryophyllaceae; Caryophylleae; Saponaria.\nOX   NCBI_TaxID=3572;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:44.890470+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c9be8c78f74c494bf89b7deeee4376bf5b587b49421d7bfa1cdf2a6c1852ed8b",
  "url": "https://rest.uniprot.org/unisave/A0AAW1MQS1?format=txt&versions=5"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1MQS1?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:WWM48150.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, TISSUE\nRP   SPECIFICITY, PATHWAY, AND BIOTECHNOLOGY.\nRX   PubMed=39043959; DOI=10.1038/s41589-024-01681-7;\nRA   Jo S., El-Demerdash A., Owen C., Srivastava V., Wu D., Kikuchi S., Reed J.,\nRA   Hodgson H., Harkess A., Shu S., Plott C., Jenkins J., Williams M.,\nRA   Boston L.-B., Lacchini E., Qu T., Goossens A., Grimwood J., Schmutz J.,\nRA   Leebens-Mack J., Osbourn A.;\nRT   \"Unlocking saponin biosynthesis in soapwort.\";\nRL   Nat. Chem. Biol. 21:215-226(2025).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:44.890470+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 17-26",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c9be8c78f74c494bf89b7deeee4376bf5b587b49421d7bfa1cdf2a6c1852ed8b",
  "url": "https://rest.uniprot.org/unisave/A0AAW1MQS1?format=txt&versions=5"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1MQS1?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Component of the oleanane-type triterpene saponins (e.g.\nCC       saponarioside A and saponarioside B) biosynthetic pathway, leading to\nCC       the production of natural products with detergent properties used as\nCC       traditional sources of soap (PubMed:39043959). A glycosyltransferase\nCC       that mediates the conversion of QA-triFR to QA-triFRX via the\nCC       elongation of the C-28 sugar chain with a D-xylose (PubMed:39043959).\nCC       {ECO:0000269|PubMed:39043959}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:44.890470+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 34-40",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c9be8c78f74c494bf89b7deeee4376bf5b587b49421d7bfa1cdf2a6c1852ed8b",
  "url": "https://rest.uniprot.org/unisave/A0AAW1MQS1?format=txt&versions=5"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1MQS1?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=3-O-{beta-D-Xyl-(1->3)-[beta-D-Gal-(1->2)]-beta-D-GlcA}-\nCC         quillaic acid alpha-L-Rha-(1->2)-beta-D-Fuc ester + UDP-alpha-D-\nCC         xylose = 3-O-{beta-D-Xyl-(1->3)-[beta-D-Gal-(1->2)]-beta-D-GlcA}-\nCC         quillaic acid beta-D-Xyl-(1->4)-alpha-L-Rha-(1->2)-beta-D-Fuc ester +\nCC         UDP + H(+); Xref=Rhea:RHEA:85055, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:57632, ChEBI:CHEBI:58223, ChEBI:CHEBI:234167,\nCC         ChEBI:CHEBI:234168; Evidence={ECO:0000269|PubMed:39043959};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:85056;\nCC         Evidence={ECO:0000269|PubMed:39043959};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:44.890470+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 41-50",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c9be8c78f74c494bf89b7deeee4376bf5b587b49421d7bfa1cdf2a6c1852ed8b",
  "url": "https://rest.uniprot.org/unisave/A0AAW1MQS1?format=txt&versions=5"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1MQS1?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0035251; F:UDP-glucosyltransferase activity; IEA:InterPro.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:44.890470+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 73-73",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c9be8c78f74c494bf89b7deeee4376bf5b587b49421d7bfa1cdf2a6c1852ed8b",
  "url": "https://rest.uniprot.org/unisave/A0AAW1MQS1?format=txt&versions=5"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1MQS1?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0008194; F:UDP-glycosyltransferase activity; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:44.890470+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 74-74",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c9be8c78f74c494bf89b7deeee4376bf5b587b49421d7bfa1cdf2a6c1852ed8b",
  "url": "https://rest.uniprot.org/unisave/A0AAW1MQS1?format=txt&versions=5"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0005516\nname: calmodulin binding\nnamespace: molecular_function\ndef: \"Binding to calmodulin, a calcium-binding protein with many roles, both in the calcium-bound and calcium-free states.\" [GOC:krc]\nsubset: goslim_chembl\nxref: Reactome:R-HSA-202110 \"eNOS:Caveolin-1 complex binds to CaM\"\nis_a: GO:0005515 ! protein binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005516",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 56977-56985",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO2",
  "excerpt": "[Term]\nid: GO:0035251\nname: UDP-glucosyltransferase activity\nnamespace: molecular_function\ndef: \"Catalysis of the transfer of a glucosyl group from UDP-glucose to an acceptor molecule.\" [PMID:19858195]\nxref: Reactome:R-HSA-1912353 \"Glucosylation of Pre-NOTCH by POGLUT1\"\nis_a: GO:0008194 ! UDP-glycosyltransferase activity\nis_a: GO:0046527 ! glucosyltransferase activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0035251",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 216295-216303",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO3",
  "excerpt": "[Term]\nid: GO:0042292\nname: URM1 activating enzyme activity\nnamespace: molecular_function\ndef: \"Catalysis of the activation of the small ubiquitin-related modifier URM1, through the formation of an ATP-dependent high-energy thiolester bond.\" [GOC:mah]\nis_a: GO:0008641 ! ubiquitin-like modifier activating enzyme activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0042292",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 236052-236058",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO4",
  "excerpt": "[Term]\nid: GO:1990841\nname: promoter-specific chromatin binding\nnamespace: molecular_function\ndef: \"Binding to a section of chromatin that is associated with gene promoter sequences of DNA.\" [PMID:19948729]\nis_a: GO:0003682 ! chromatin binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:1990841",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 555543-555549",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 187. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
