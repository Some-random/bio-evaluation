# GO_cellular_component_0046

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0046.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **D** — endoplasmic reticulum membrane

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSEPNVRASFADNRRPLSKTKGQLLNMPPVITTALYTAFPVIFLLDKVLAFLTWTNDDPYTNFIAIAIYIMVVKYWTVVACTVLPTIIALGTCASLWFLKTTIDDLRSETAPPTIEEIIDTLINMQARFSYIVEPFSYFGSLSGSDYFNLGFSLIAITPCYIWLMTRIFTVRSFLLVFGVAWLSFHSSWSVATRHLLWRSIVIRKILTFTTGLKFSLVDKNIELTVLNDFQISNVGTGKTVEFHILQNQRRWLGVGWSNTLLPFERGPFTTEDLEKSWDSLESFQFPEITQATCRWRWLDANWKTDDSFAPGEGWIYYNNSWEEPSNTDSLTRFTRTKRWKRRALVIVEDDGTT

[Multiple Choices]
A. recycling endosome membrane
B. trans-Golgi network membrane
C. vesicle
D. endoplasmic reticulum membrane
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Cellular Component Prediction, which is to predict the primary Cellular Component where a protein is located, according to the Gene Ontology (GO) framework. A protein's location within a cell (e.g., Nucleus, Mitochondria, Cytoplasm) is critical for its function and is often determined by specific targeting signals in its amino acid sequence. Based on the provided sequence, you must identify the most likely compartment where the protein resides.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt record reports experimental localization to the endoplasmic reticulum membrane, supporting D among the offered choices. It also reports peroxisomal membrane localization and accumulation at peroxisome–ER contact sites, so the evidence does not establish ER as the protein's exclusive location.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has multiple hydrophobic segments, which credibly suggests an integral membrane protein. That feature does not meaningfully distinguish ER membrane from recycling endosome or trans-Golgi network membrane; the remaining C-terminal sequence provides no clear targeting signal in the supplied input that selects among those compartments.


**Missing item-specific fact**

> A reliable identification of this protein as PEX32, or equivalent protein-specific localization knowledge showing its ER association, is needed to select D over the other membrane compartments.


**Reason**

> The general sequence features support membrane association but not a particular membrane system. The specific ER/peroxisome contact-site localization is not supplied and cannot be inferred with meaningful confidence from the generic multipass topology alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only D among the offered specific compartments is supported by the supplied reviewer evidence. However, the protein is also reported at the peroxisomal membrane, which is not an option, and the evidence describes contact-site accumulation rather than establishing an exclusive or uniquely primary membrane.


### Important caveats

- The reviewer-only historical entry matches the supplied sequence, but the author's exact source snapshot is unknown.
- The localization evidence supports ER membrane association while also documenting peroxisomal membrane localization.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has multiple hydrophobic segments, which credibly suggests an integral membrane protein. That feature does not meaningfully distinguish ER membrane from recycling endosome or trans-Golgi network membrane; the remaining C-terminal sequence provides no clear targeting signal in the supplied input that selects among those compartments.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "A reliable identification of this protein as PEX32, or equivalent protein-specific localization knowledge showing its ER association, is needed to select D over the other membrane compartments.",
    "reason": "The general sequence features support membrane association but not a particular membrane system. The specific ER/peroxisome contact-site localization is not supplied and cannot be inferred with meaningful confidence from the generic multipass topology alone."
  },
  "case_id": "GO_cellular_component_0046",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports experimental localization to the endoplasmic reticulum membrane, supporting D among the offered choices. It also reports peroxisomal membrane localization and accumulation at peroxisome–ER contact sites, so the evidence does not establish ER as the protein's exclusive location."
  },
  "important_caveats": [
    "The reviewer-only historical entry matches the supplied sequence, but the author's exact source snapshot is unknown.",
    "The localization evidence supports ER membrane association while also documenting peroxisomal membrane localization."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only D among the offered specific compartments is supported by the supplied reviewer evidence. However, the protein is also reported at the peroxisomal membrane, which is not an option, and the evidence describes contact-site accumulation rather than establishing an exclusive or uniquely primary membrane."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0046",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports experimental localization to the endoplasmic reticulum membrane, supporting D among the offered choices. It also reports peroxisomal membrane localization and accumulation at peroxisome–ER contact sites, so the evidence does not establish ER as the protein's exclusive location.",
    "evidence_ids": ["C5", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has multiple hydrophobic segments, which credibly suggests an integral membrane protein. That feature does not meaningfully distinguish ER membrane from recycling endosome or trans-Golgi network membrane; the remaining C-terminal sequence provides no clear targeting signal in the supplied input that selects among those compartments.",
    "missing_item_specific_fact": "A reliable identification of this protein as PEX32, or equivalent protein-specific localization knowledge showing its ER association, is needed to select D over the other membrane compartments.",
    "reason": "The general sequence features support membrane association but not a particular membrane system. The specific ER/peroxisome contact-site localization is not supplied and cannot be inferred with meaningful confidence from the generic multipass topology alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only D among the offered specific compartments is supported by the supplied reviewer evidence. However, the protein is also reported at the peroxisomal membrane, which is not an option, and the evidence describes contact-site accumulation rather than establishing an exclusive or uniquely primary membrane."
  },
  "important_caveats": [
    "The reviewer-only historical entry matches the supplied sequence, but the author's exact source snapshot is unknown.",
    "The localization evidence supports ER membrane association while also documenting peroxisomal membrane localization."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (W1QHP2, PEX32 from Ogataea parapolymorpha) explicitly annotates the protein at both 'Peroxisome membrane' AND 'Endoplasmic reticulum membrane' with experimental evidence (ECO:0000269, PubMed:32665322). The GO term GO:0005789 (endoplasmic reticulum membrane) is annotated with EXP evidence. Since peroxisome membrane is not among the four offered choices, ER membrane (D) is the only annotated location present in the options. The note 'Predominantly accumulates at peroxisome-ER contact sites' confirms ER membrane involvement.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence encodes a small (~354 aa) multi-pass membrane protein with no cleavable signal peptide and no obvious organelle-specific trafficking motifs (no KKXX/RXR ER-retrieval, no Golgi-targeting, no endosome-specific signals). Transferable knowledge from membrane biology provides a probabilistic argument: (1) Small multi-pass membrane proteins without signal peptides are most commonly ER-resident, as the ER is the default site of membrane protein integration and many small multi-pass proteins (e.g., small transporters, tethering components) reside there. (2) Transport vesicles (option C) are small (~50-100 nm) and their membrane proteins are typically single-pass (e.g., SNAREs) or lipid-anchored; multi-pass membrane proteins are uncommon in vesicle membranes, providing a reasonable basis to deprioritize C. (3) Without evidence of forward trafficking signals or Golgi/endosome-specific motifs, the parsimonious default for a multi-pass membrane protein is ER retention. This probabilistic reasoning meaningfully distinguishes D from the alternatives, though it does not provide certainty.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can apply general principles of membrane protein biogenesis (small multi-pass proteins default to ER; vesicles rarely harbor multi-pass proteins; absence of trafficking signals favors ER residency) to arrive at D. The argument is probabilistic rather than definitive but meaningfully distinguishes the offered alternatives without requiring the specific PEX32 annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four offered options, only ER membrane (D) is annotated for this protein. Peroxisome membrane (the protein's primary identity) is not offered. The remaining options (recycling endosome, trans-Golgi network, vesicle) are not annotated locations for this protein. No ambiguity exists among the given choices.


### Important caveats

- The protein's primary identity is as a peroxisomal membrane protein (PEX32) that tethers peroxisomes to the ER. Calling ER membrane its 'primary' cellular component is somewhat misleading; it localizes at peroxisome-ER contact sites. However, since peroxisome membrane is not an offered option, D is the best available answer.
- The transferable argument (small multi-pass membrane protein → likely ER) is probabilistic. Many multi-pass membrane proteins traffic to Golgi or endosomes. The argument provides a reasonable prior but not certainty.
- The UniProt annotation lists both peroxisome membrane and ER membrane with equal experimental evidence codes (EXP). The 'primary' designation for ER among the given options relies on the elimination of peroxisome from the choices rather than on ER being the sole or dominant location.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence encodes a small (~354 aa) multi-pass membrane protein with no cleavable signal peptide and no obvious organelle-specific trafficking motifs (no KKXX/RXR ER-retrieval, no Golgi-targeting, no endosome-specific signals). Transferable knowledge from membrane biology provides a probabilistic argument: (1) Small multi-pass membrane proteins without signal peptides are most commonly ER-resident, as the ER is the default site of membrane protein integration and many small multi-pass proteins (e.g., small transporters, tethering components) reside there. (2) Transport vesicles (option C) are small (~50-100 nm) and their membrane proteins are typically single-pass (e.g., SNAREs) or lipid-anchored; multi-pass membrane proteins are uncommon in vesicle membranes, providing a reasonable basis to deprioritize C. (3) Without evidence of forward trafficking signals or Golgi/endosome-specific motifs, the parsimonious default for a multi-pass membrane protein is ER retention. This probabilistic reasoning meaningfully distinguishes D from the alternatives, though it does not provide certainty.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can apply general principles of membrane protein biogenesis (small multi-pass proteins default to ER; vesicles rarely harbor multi-pass proteins; absence of trafficking signals favors ER residency) to arrive at D. The argument is probabilistic rather than definitive but meaningfully distinguishes the offered alternatives without requiring the specific PEX32 annotation."
  },
  "case_id": "GO_cellular_component_0046",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (W1QHP2, PEX32 from Ogataea parapolymorpha) explicitly annotates the protein at both 'Peroxisome membrane' AND 'Endoplasmic reticulum membrane' with experimental evidence (ECO:0000269, PubMed:32665322). The GO term GO:0005789 (endoplasmic reticulum membrane) is annotated with EXP evidence. Since peroxisome membrane is not among the four offered choices, ER membrane (D) is the only annotated location present in the options. The note 'Predominantly accumulates at peroxisome-ER contact sites' confirms ER membrane involvement."
  },
  "important_caveats": [
    "The protein's primary identity is as a peroxisomal membrane protein (PEX32) that tethers peroxisomes to the ER. Calling ER membrane its 'primary' cellular component is somewhat misleading; it localizes at peroxisome-ER contact sites. However, since peroxisome membrane is not an offered option, D is the best available answer.",
    "The transferable argument (small multi-pass membrane protein → likely ER) is probabilistic. Many multi-pass membrane proteins traffic to Golgi or endosomes. The argument provides a reasonable prior but not certainty.",
    "The UniProt annotation lists both peroxisome membrane and ER membrane with equal experimental evidence codes (EXP). The 'primary' designation for ER among the given options relies on the elimination of peroxisome from the choices rather than on ER being the sole or dominant location."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four offered options, only ER membrane (D) is annotated for this protein. Peroxisome membrane (the protein's primary identity) is not offered. The remaining options (recycling endosome, trans-Golgi network, vesicle) are not annotated locations for this protein. No ambiguity exists among the given choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0046",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (W1QHP2, PEX32 from Ogataea parapolymorpha) explicitly annotates the protein at both 'Peroxisome membrane' AND 'Endoplasmic reticulum membrane' with experimental evidence (ECO:0000269, PubMed:32665322). The GO term GO:0005789 (endoplasmic reticulum membrane) is annotated with EXP evidence. Since peroxisome membrane is not among the four offered choices, ER membrane (D) is the only annotated location present in the options. The note 'Predominantly accumulates at peroxisome-ER contact sites' confirms ER membrane involvement.",
    "evidence_ids": ["C5", "C6", "C7", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence encodes a small (~354 aa) multi-pass membrane protein with no cleavable signal peptide and no obvious organelle-specific trafficking motifs (no KKXX/RXR ER-retrieval, no Golgi-targeting, no endosome-specific signals). Transferable knowledge from membrane biology provides a probabilistic argument: (1) Small multi-pass membrane proteins without signal peptides are most commonly ER-resident, as the ER is the default site of membrane protein integration and many small multi-pass proteins (e.g., small transporters, tethering components) reside there. (2) Transport vesicles (option C) are small (~50-100 nm) and their membrane proteins are typically single-pass (e.g., SNAREs) or lipid-anchored; multi-pass membrane proteins are uncommon in vesicle membranes, providing a reasonable basis to deprioritize C. (3) Without evidence of forward trafficking signals or Golgi/endosome-specific motifs, the parsimonious default for a multi-pass membrane protein is ER retention. This probabilistic reasoning meaningfully distinguishes D from the alternatives, though it does not provide certainty.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can apply general principles of membrane protein biogenesis (small multi-pass proteins default to ER; vesicles rarely harbor multi-pass proteins; absence of trafficking signals favors ER residency) to arrive at D. The argument is probabilistic rather than definitive but meaningfully distinguishes the offered alternatives without requiring the specific PEX32 annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four offered options, only ER membrane (D) is annotated for this protein. Peroxisome membrane (the protein's primary identity) is not offered. The remaining options (recycling endosome, trans-Golgi network, vesicle) are not annotated locations for this protein. No ambiguity exists among the given choices."
  },
  "important_caveats": [
    "The protein's primary identity is as a peroxisomal membrane protein (PEX32) that tethers peroxisomes to the ER. Calling ER membrane its 'primary' cellular component is somewhat misleading; it localizes at peroxisome-ER contact sites. However, since peroxisome membrane is not an offered option, D is the best available answer.",
    "The transferable argument (small multi-pass membrane protein → likely ER) is probabilistic. Many multi-pass membrane proteins traffic to Golgi or endosomes. The argument provides a reasonable prior but not certainty.",
    "The UniProt annotation lists both peroxisome membrane and ER membrane with equal experimental evidence codes (EXP). The 'primary' designation for ER among the given options relies on the elimination of peroxisome from the choices rather than on ER being the sole or dominant location."
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
  "benchmark_sequence_length": 354,
  "benchmark_sequence_sha256": "abe0e7534f8e5a7590c0c44dd5ef1187e54178fee63a913ef3b3fc143ae42ee1",
  "current_entry_audit": {
    "entryVersion": 40,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2014-03-19",
    "sequenceVersion": 1
  },
  "current_record_sha256": "496aea11aa2b41aaa21a1680c1288b30d7312fd99c41cdd11ef292e508959dcd",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 354,
  "current_source_sequence_sha256": "abe0e7534f8e5a7590c0c44dd5ef1187e54178fee63a913ef3b3fc143ae42ee1",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 38,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "W1QHP2",
  "selected_historical_entry_version": 38,
  "selected_historical_record_sha256": "95f12c3e5266dcfc076c0bab33c3d654a00f2c142918715c03c5fb98c2acd8be",
  "selected_historical_source_sequence_length": 354,
  "selected_historical_source_sequence_sha256": "abe0e7534f8e5a7590c0c44dd5ef1187e54178fee63a913ef3b3fc143ae42ee1",
  "selected_historical_version": {
    "accession": "W1QHP2",
    "database": "Swiss-Prot",
    "entryVersion": 38,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "PEX32_OGAPD",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QHP2.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"W1QHP2\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:30.706856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "496aea11aa2b41aaa21a1680c1288b30d7312fd99c41cdd11ef292e508959dcd",
  "url": "https://rest.uniprot.org/uniprotkb/W1QHP2.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QHP2.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":40,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2014-03-19\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:30.706856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "496aea11aa2b41aaa21a1680c1288b30d7312fd99c41cdd11ef292e508959dcd",
  "url": "https://rest.uniprot.org/uniprotkb/W1QHP2.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QHP2.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Yeast\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Saccharomycotina\",\"Pichiomycetes\",\"Pichiales\",\"Pichiaceae\",\"Ogataea\"],\"scientificName\":\"Ogataea parapolymorpha (strain ATCC 26012 / BCRC 20466 / JCM 22074 / NRRL Y-7560 / DL-1)\",\"synonyms\":[\"Hansenula polymorpha\"],\"taxonId\":871575}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:30.706856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "496aea11aa2b41aaa21a1680c1288b30d7312fd99c41cdd11ef292e508959dcd",
  "url": "https://rest.uniprot.org/uniprotkb/W1QHP2.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QHP2.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Peroxin-32\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32665322\",\"source\":\"PubMed\"}],\"value\":\"Peroxisomal membrane protein PEX32\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:30.706856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "496aea11aa2b41aaa21a1680c1288b30d7312fd99c41cdd11ef292e508959dcd",
  "url": "https://rest.uniprot.org/uniprotkb/W1QHP2.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QHP2.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"32665322\",\"source\":\"PubMed\"}],\"value\":\"Predominantly accumulates at peroxisome-ER contact sites\"}]},\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"32665322\",\"source\":\"PubMed\"}],\"id\":\"SL-0203\",\"value\":\"Peroxisome membrane\"},\"topology\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"id\":\"SL-9909\",\"value\":\"Multi-pass membrane protein\"}},{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"32665322\",\"source\":\"PubMed\"}],\"id\":\"SL-0097\",\"value\":\"Endoplasmic reticulum membrane\"},\"topology\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"id\":\"SL-9909\",\"value\":\"Multi-pass membrane protein\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:25:30.706856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "496aea11aa2b41aaa21a1680c1288b30d7312fd99c41cdd11ef292e508959dcd",
  "url": "https://rest.uniprot.org/uniprotkb/W1QHP2.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QHP2.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"32665322\",\"source\":\"PubMed\"}],\"id\":\"GO:0005789\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:endoplasmic reticulum membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"EXP:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/11",
  "retrieved_utc": "2026-11-01T06:25:30.706856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "496aea11aa2b41aaa21a1680c1288b30d7312fd99c41cdd11ef292e508959dcd",
  "url": "https://rest.uniprot.org/uniprotkb/W1QHP2.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QHP2.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"32665322\",\"source\":\"PubMed\"}],\"id\":\"GO:0005778\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:peroxisomal membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"EXP:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/12",
  "retrieved_utc": "2026-11-01T06:25:30.706856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "496aea11aa2b41aaa21a1680c1288b30d7312fd99c41cdd11ef292e508959dcd",
  "url": "https://rest.uniprot.org/uniprotkb/W1QHP2.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QHP2.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Wu F.\",\"de Boer R.\",\"Krikken A.M.\",\"Aksit A.\",\"Bordin N.\",\"Devos D.P.\",\"van der Klei I.J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"32665322\"},{\"database\":\"DOI\",\"id\":\"10.1242/jcs.246983\"}],\"citationType\":\"journal article\",\"firstPage\":\"0\",\"id\":\"32665322\",\"journal\":\"J. Cell Sci.\",\"lastPage\":\"0\",\"publicationDate\":\"2020\",\"title\":\"Pex24 and Pex32 are required to tether peroxisomes to the ER for organelle biogenesis, positioning and segregation in yeast.\",\"volume\":\"133\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:25:30.706856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "496aea11aa2b41aaa21a1680c1288b30d7312fd99c41cdd11ef292e508959dcd",
  "url": "https://rest.uniprot.org/uniprotkb/W1QHP2.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QHP2?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H1",
  "excerpt": "ID   PEX32_OGAPD             Reviewed;         354 AA.\nAC   W1QHP2;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   19-MAR-2014, sequence version 1.\nDT   28-JAN-2026, entry version 38.\nDE   RecName: Full=Peroxisomal membrane protein PEX32 {ECO:0000303|PubMed:32665322};\nDE   AltName: Full=Peroxin-32 {ECO:0000305};\nGN   Name=PEX32 {ECO:0000303|PubMed:32665322}; ORFNames=HPODL_04641;\nOS   Ogataea parapolymorpha (strain ATCC 26012 / BCRC 20466 / JCM 22074 / NRRL\nOS   Y-7560 / DL-1) (Yeast) (Hansenula polymorpha).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Saccharomycotina; Pichiomycetes;\nOC   Pichiales; Pichiaceae; Ogataea.\nOX   NCBI_TaxID=871575;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:55.253871+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "95f12c3e5266dcfc076c0bab33c3d654a00f2c142918715c03c5fb98c2acd8be",
  "url": "https://rest.uniprot.org/unisave/W1QHP2?format=txt&versions=38"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QHP2?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, DISRUPTION PHENOTYPE, AND SUBCELLULAR LOCATION.\nRX   PubMed=32665322; DOI=10.1242/jcs.246983;\nRA   Wu F., de Boer R., Krikken A.M., Aksit A., Bordin N., Devos D.P.,\nRA   van der Klei I.J.;\nRT   \"Pex24 and Pex32 are required to tether peroxisomes to the ER for organelle\nRT   biogenesis, positioning and segregation in yeast.\";\nRL   J. Cell Sci. 133:0-0(2020).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:55.253871+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 24-31",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "95f12c3e5266dcfc076c0bab33c3d654a00f2c142918715c03c5fb98c2acd8be",
  "url": "https://rest.uniprot.org/unisave/W1QHP2?format=txt&versions=38"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QHP2?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H3",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Peroxisome membrane\nCC       {ECO:0000269|PubMed:32665322}; Multi-pass membrane protein\nCC       {ECO:0000255}. Endoplasmic reticulum membrane\nCC       {ECO:0000269|PubMed:32665322}; Multi-pass membrane protein\nCC       {ECO:0000255}. Note=Predominantly accumulates at peroxisome-ER contact\nCC       sites. {ECO:0000269|PubMed:32665322}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:55.253871+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 35-40",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "95f12c3e5266dcfc076c0bab33c3d654a00f2c142918715c03c5fb98c2acd8be",
  "url": "https://rest.uniprot.org/unisave/W1QHP2?format=txt&versions=38"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QHP2?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0005789; C:endoplasmic reticulum membrane; IEA:UniProtKB-SubCell.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:55.253871+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 64-64",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "95f12c3e5266dcfc076c0bab33c3d654a00f2c142918715c03c5fb98c2acd8be",
  "url": "https://rest.uniprot.org/unisave/W1QHP2?format=txt&versions=38"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QHP2?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0005778; C:peroxisomal membrane; IEA:UniProtKB-SubCell.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:55.253871+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 65-65",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "95f12c3e5266dcfc076c0bab33c3d654a00f2c142918715c03c5fb98c2acd8be",
  "url": "https://rest.uniprot.org/unisave/W1QHP2?format=txt&versions=38"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0005789\nname: endoplasmic reticulum membrane\nnamespace: cellular_component\ndef: \"The lipid bilayer surrounding the endoplasmic reticulum.\" [GOC:mah]\nsynonym: \"ER membrane\" EXACT []\nis_a: GO:0031090 ! organelle membrane\nrelationship: part_of GO:0042175 ! nuclear outer membrane-endoplasmic reticulum membrane network\nrelationship: part_of GO:0098827 ! endoplasmic reticulum subcompartment\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005789",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 59526-59535",
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
  "excerpt": "[Term]\nid: GO:0031982\nname: vesicle\nnamespace: cellular_component\nalt_id: GO:0031988\ndef: \"Any small, fluid-filled, spherical organelle enclosed by membrane.\" [GOC:mah, GOC:pz, GOC:vesicles]\nsubset: goslim_pir\nsynonym: \"membrane-bounded vesicle\" RELATED []\nsynonym: \"membrane-enclosed vesicle\" RELATED []\nxref: NIF_Subcellular:sao221389602\nxref: Wikipedia:Vesicle_(biology)\nis_a: GO:0043227 ! membrane-bounded organelle\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0031982",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 181606-181618",
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
  "excerpt": "[Term]\nid: GO:0032588\nname: trans-Golgi network membrane\nnamespace: cellular_component\ndef: \"The lipid bilayer surrounding any of the compartments that make up the trans-Golgi network.\" [GOC:mah]\nsynonym: \"Golgi trans face membrane\" RELATED []\nsynonym: \"trans Golgi network membrane\" EXACT []\nis_a: GO:0031090 ! organelle membrane\nrelationship: part_of GO:0005802 ! trans-Golgi network\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0032588",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 187565-187574",
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
  "excerpt": "[Term]\nid: GO:0055038\nname: recycling endosome membrane\nnamespace: cellular_component\ndef: \"The lipid bilayer surrounding a recycling endosome.\" [GOC:jid, GOC:rph, PMID:10930469, PMID:15601896, PMID:16246101]\nis_a: GO:0010008 ! endosome membrane\nrelationship: part_of GO:0055037 ! recycling endosome\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0055038",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 342824-342831",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 46. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
