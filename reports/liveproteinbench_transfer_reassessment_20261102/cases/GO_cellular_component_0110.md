# GO_cellular_component_0110

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0110.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **D** — mitochondrion

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | uncertain | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSLSNKLAITDVDLKDKRVLIRVDFNVPLDADKKITNNQRIVGALPTIKYAIENGAKAVVLMSHLGRPDGKANPKYSLKPVATELEKLLSKSVIFAENCVGKETEEIVNKATGGQVILLENLRFHAEEEGSSKDAEGKKVKADKEKVEEFRKGLTALGDVYINDAFGTAHRAHSSMVGVDLPQKASGFLVKKELEYFAKALESPQRPFLAILGGAKVSDKIQLIDNLLPKVNSLIITGAMAFTFKKTLENVKIGNSLFDEAGSKIVGDIVEKAKKNNVKIVLPVDYVTADKFAADAKTGYATDADGIPDGYMGLDVGEKSVELYKKTIAEAKTILWNGPPGVFELEPFANATKKTLDAAVAAAQSGSIVIIGGGDTATVAAKYGAEAKLSHVSTGGGASLELLEGKVLPGVDALSSK

[Multiple Choices]
A. chromosome
B. centrosome
C. host cell nucleolus
D. mitochondrion
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

### Expected-answer support: uncertain

> The matched-sequence annotation reports experimental localization to both cytosol and mitochondrion, with mitochondrial localization specifically when phosphorylated. This supports mitochondrion as a location, but does not establish it as the protein’s primary compartment.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with phosphoglycerate kinase, a glycolytic enzyme generally associated with the cytosol; it has no obvious N-terminal mitochondrial targeting extension. That family-level knowledge does not meaningfully support mitochondrion over the other offered choices.


**Missing item-specific fact**

> The target’s experimentally reported, phosphorylation-dependent mitochondrial localization is not apparent from the sequence or choices.


**Reason**

> General family knowledge points toward the cytosol, which is not offered, and does not establish this protein’s unusual regulated mitochondrial localization. Distinguishing mitochondrion therefore depends on a fact about this exact protein not supplied in the original input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence reports cytosol and mitochondrion, but cytosol is not an offered choice. Among the offered options, only mitochondrion is reported; the uncertainty is whether it is the primary compartment, not which offered option is another supported location.


### Important caveats

- The source annotations are experimental and match the supplied sequence, but they describe conditional mitochondrial localization as well as cytosolic localization.
- The exact organism and source-record identity are reviewer-only and are not used as original-input clues.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with phosphoglycerate kinase, a glycolytic enzyme generally associated with the cytosol; it has no obvious N-terminal mitochondrial targeting extension. That family-level knowledge does not meaningfully support mitochondrion over the other offered choices.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The target’s experimentally reported, phosphorylation-dependent mitochondrial localization is not apparent from the sequence or choices.",
    "reason": "General family knowledge points toward the cytosol, which is not offered, and does not establish this protein’s unusual regulated mitochondrial localization. Distinguishing mitochondrion therefore depends on a fact about this exact protein not supplied in the original input."
  },
  "case_id": "GO_cellular_component_0110",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7"
    ],
    "judgment": "cannot_determine",
    "reason": "The matched-sequence annotation reports experimental localization to both cytosol and mitochondrion, with mitochondrial localization specifically when phosphorylated. This supports mitochondrion as a location, but does not establish it as the protein’s primary compartment."
  },
  "important_caveats": [
    "The source annotations are experimental and match the supplied sequence, but they describe conditional mitochondrial localization as well as cytosolic localization.",
    "The exact organism and source-record identity are reviewer-only and are not used as original-input clues."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence reports cytosol and mitochondrion, but cytosol is not an offered choice. Among the offered options, only mitochondrion is reported; the uncertainty is whether it is the primary compartment, not which offered option is another supported location."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0110",
  "expected_answer_check": {
    "judgment": "cannot_determine",
    "reason": "The matched-sequence annotation reports experimental localization to both cytosol and mitochondrion, with mitochondrial localization specifically when phosphorylated. This supports mitochondrion as a location, but does not establish it as the protein’s primary compartment.",
    "evidence_ids": ["C5", "C6", "C7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with phosphoglycerate kinase, a glycolytic enzyme generally associated with the cytosol; it has no obvious N-terminal mitochondrial targeting extension. That family-level knowledge does not meaningfully support mitochondrion over the other offered choices.",
    "missing_item_specific_fact": "The target’s experimentally reported, phosphorylation-dependent mitochondrial localization is not apparent from the sequence or choices.",
    "reason": "General family knowledge points toward the cytosol, which is not offered, and does not establish this protein’s unusual regulated mitochondrial localization. Distinguishing mitochondrion therefore depends on a fact about this exact protein not supplied in the original input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence reports cytosol and mitochondrion, but cytosol is not an offered choice. Among the offered options, only mitochondrion is reported; the uncertainty is whether it is the primary compartment, not which offered option is another supported location."
  },
  "important_caveats": [
    "The source annotations are experimental and match the supplied sequence, but they describe conditional mitochondrial localization as well as cytosolic localization.",
    "The exact organism and source-record identity are reviewer-only and are not used as original-input clues."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A7G5KET3) annotates this PGK1 protein to both 'Cytoplasm, cytosol' and 'Mitochondrion' with experimental evidence (ECO:0000269, PubMed:37754565). The note states 'Localizes to the mitochondrion when phosphorylated.' GO:0005739 (mitochondrion) is annotated with IDA evidence. Although the primary/default location is listed as cytosol and mitochondrial localization is conditional, 'mitochondrion' is an experimentally verified location for this protein. Among the four offered choices, only 'mitochondrion' matches any annotation; 'cytosol' is not offered. Thus the key is supported by the evidence.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the hallmark PGK-family motifs 'GGAKVSDKI' (active-site), 'GGGDTATVAAK', and 'GGGASLEL', identifying it as phosphoglycerate kinase (EC 2.7.2.3), a core glycolytic enzyme. From general biology, glycolytic enzymes reside in the cytosol or, in some organisms, the mitochondrial matrix; they are not components of chromosomes (structural DNA-protein complexes), centrosomes (microtubule-organizing centers), or nucleoli (rRNA-processing bodies). A knowledgeable model can eliminate A (chromosome), B (centrosome), and C (host cell nucleolus) as implausible compartments for a metabolic kinase, leaving D (mitochondrion) as the only compartment among the choices where a glycolytic enzyme could reside. This elimination does not require knowing this specific protein's annotation; it follows from the protein-family identity (PGK) and the general principle that metabolic enzymes localize to cytosol/mitochondria, not to structural or RNA-processing compartments.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognition of PGK family motifs in the sequence plus general knowledge that glycolytic enzymes are found in cytosol or mitochondria (not in chromosomes, centrosomes, or nucleoli) provides a concrete, transferable inference that meaningfully eliminates three of the four options and selects the remaining one. The model need not recall this exact protein's conditional mitochondrial localization; the family-level reasoning suffices to distinguish D from A, B, and C.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the protein's primary annotation is cytosol (not offered), among the four choices only mitochondrion is a biologically plausible location for a glycolytic enzyme. The other three options (chromosome, centrosome, host cell nucleolus) are structurally and functionally incompatible with a soluble kinase. No ambiguity exists among the offered alternatives.


### Important caveats

- The mitochondrial localization is conditional (only upon phosphorylation at Ser-203) and was reported in a 2023 study; the default/primary location is cytosol, which is not among the answer choices.
- The question asks for the 'primary' cellular component, yet the offered set excludes cytosol, effectively forcing a choice among four options where only one is even partially correct.
- The UniProt entry was first publicly released in February 2025; the 2023 PubMed paper (PMID:37754565) provides the experimental evidence for mitochondrial localization.
- The sequence lacks a canonical N-terminal mitochondrial targeting signal; mitochondrial import appears to be regulated post-translationally rather than directed by a classical presequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the hallmark PGK-family motifs 'GGAKVSDKI' (active-site), 'GGGDTATVAAK', and 'GGGASLEL', identifying it as phosphoglycerate kinase (EC 2.7.2.3), a core glycolytic enzyme. From general biology, glycolytic enzymes reside in the cytosol or, in some organisms, the mitochondrial matrix; they are not components of chromosomes (structural DNA-protein complexes), centrosomes (microtubule-organizing centers), or nucleoli (rRNA-processing bodies). A knowledgeable model can eliminate A (chromosome), B (centrosome), and C (host cell nucleolus) as implausible compartments for a metabolic kinase, leaving D (mitochondrion) as the only compartment among the choices where a glycolytic enzyme could reside. This elimination does not require knowing this specific protein's annotation; it follows from the protein-family identity (PGK) and the general principle that metabolic enzymes localize to cytosol/mitochondria, not to structural or RNA-processing compartments.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognition of PGK family motifs in the sequence plus general knowledge that glycolytic enzymes are found in cytosol or mitochondria (not in chromosomes, centrosomes, or nucleoli) provides a concrete, transferable inference that meaningfully eliminates three of the four options and selects the remaining one. The model need not recall this exact protein's conditional mitochondrial localization; the family-level reasoning suffices to distinguish D from A, B, and C."
  },
  "case_id": "GO_cellular_component_0110",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "H3",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A7G5KET3) annotates this PGK1 protein to both 'Cytoplasm, cytosol' and 'Mitochondrion' with experimental evidence (ECO:0000269, PubMed:37754565). The note states 'Localizes to the mitochondrion when phosphorylated.' GO:0005739 (mitochondrion) is annotated with IDA evidence. Although the primary/default location is listed as cytosol and mitochondrial localization is conditional, 'mitochondrion' is an experimentally verified location for this protein. Among the four offered choices, only 'mitochondrion' matches any annotation; 'cytosol' is not offered. Thus the key is supported by the evidence."
  },
  "important_caveats": [
    "The mitochondrial localization is conditional (only upon phosphorylation at Ser-203) and was reported in a 2023 study; the default/primary location is cytosol, which is not among the answer choices.",
    "The question asks for the 'primary' cellular component, yet the offered set excludes cytosol, effectively forcing a choice among four options where only one is even partially correct.",
    "The UniProt entry was first publicly released in February 2025; the 2023 PubMed paper (PMID:37754565) provides the experimental evidence for mitochondrial localization.",
    "The sequence lacks a canonical N-terminal mitochondrial targeting signal; mitochondrial import appears to be regulated post-translationally rather than directed by a classical presequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the protein's primary annotation is cytosol (not offered), among the four choices only mitochondrion is a biologically plausible location for a glycolytic enzyme. The other three options (chromosome, centrosome, host cell nucleolus) are structurally and functionally incompatible with a soluble kinase. No ambiguity exists among the offered alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0110",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A7G5KET3) annotates this PGK1 protein to both 'Cytoplasm, cytosol' and 'Mitochondrion' with experimental evidence (ECO:0000269, PubMed:37754565). The note states 'Localizes to the mitochondrion when phosphorylated.' GO:0005739 (mitochondrion) is annotated with IDA evidence. Although the primary/default location is listed as cytosol and mitochondrial localization is conditional, 'mitochondrion' is an experimentally verified location for this protein. Among the four offered choices, only 'mitochondrion' matches any annotation; 'cytosol' is not offered. Thus the key is supported by the evidence.",
    "evidence_ids": ["C5", "C7", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the hallmark PGK-family motifs 'GGAKVSDKI' (active-site), 'GGGDTATVAAK', and 'GGGASLEL', identifying it as phosphoglycerate kinase (EC 2.7.2.3), a core glycolytic enzyme. From general biology, glycolytic enzymes reside in the cytosol or, in some organisms, the mitochondrial matrix; they are not components of chromosomes (structural DNA-protein complexes), centrosomes (microtubule-organizing centers), or nucleoli (rRNA-processing bodies). A knowledgeable model can eliminate A (chromosome), B (centrosome), and C (host cell nucleolus) as implausible compartments for a metabolic kinase, leaving D (mitochondrion) as the only compartment among the choices where a glycolytic enzyme could reside. This elimination does not require knowing this specific protein's annotation; it follows from the protein-family identity (PGK) and the general principle that metabolic enzymes localize to cytosol/mitochondria, not to structural or RNA-processing compartments.",
    "missing_item_specific_fact": "",
    "reason": "Recognition of PGK family motifs in the sequence plus general knowledge that glycolytic enzymes are found in cytosol or mitochondria (not in chromosomes, centrosomes, or nucleoli) provides a concrete, transferable inference that meaningfully eliminates three of the four options and selects the remaining one. The model need not recall this exact protein's conditional mitochondrial localization; the family-level reasoning suffices to distinguish D from A, B, and C."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the protein's primary annotation is cytosol (not offered), among the four choices only mitochondrion is a biologically plausible location for a glycolytic enzyme. The other three options (chromosome, centrosome, host cell nucleolus) are structurally and functionally incompatible with a soluble kinase. No ambiguity exists among the offered alternatives."
  },
  "important_caveats": [
    "The mitochondrial localization is conditional (only upon phosphorylation at Ser-203) and was reported in a 2023 study; the default/primary location is cytosol, which is not among the answer choices.",
    "The question asks for the 'primary' cellular component, yet the offered set excludes cytosol, effectively forcing a choice among four options where only one is even partially correct.",
    "The UniProt entry was first publicly released in February 2025; the 2023 PubMed paper (PMID:37754565) provides the experimental evidence for mitochondrial localization.",
    "The sequence lacks a canonical N-terminal mitochondrial targeting signal; mitochondrial import appears to be regulated post-translationally rather than directed by a classical presequence."
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
  "benchmark_sequence_length": 417,
  "benchmark_sequence_sha256": "275622872aa5039ffd4e2fafadfa8fcabe446204f6ab488fbd8b5e29f8a6b5e4",
  "current_entry_audit": {
    "entryVersion": 19,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2021-02-10",
    "sequenceVersion": 1
  },
  "current_record_sha256": "79f801166dc030cf4959c0881b37cd1bd39704c428283cc65f9c68002c1fbb5b",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 417,
  "current_source_sequence_sha256": "275622872aa5039ffd4e2fafadfa8fcabe446204f6ab488fbd8b5e29f8a6b5e4",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 18,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A7G5KET3",
  "selected_historical_entry_version": 18,
  "selected_historical_record_sha256": "b429698fb3b322f2fc43bbd8bc72a321c4e8bcf2772d689c13b699dd201233ec",
  "selected_historical_source_sequence_length": 417,
  "selected_historical_source_sequence_sha256": "275622872aa5039ffd4e2fafadfa8fcabe446204f6ab488fbd8b5e29f8a6b5e4",
  "selected_historical_version": {
    "accession": "A0A7G5KET3",
    "database": "Swiss-Prot",
    "entryVersion": 18,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "PGK1_ASPFN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7G5KET3.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A7G5KET3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:25:35.568831+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "79f801166dc030cf4959c0881b37cd1bd39704c428283cc65f9c68002c1fbb5b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7G5KET3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7G5KET3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":19,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2021-02-10\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:25:35.568831+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "79f801166dc030cf4959c0881b37cd1bd39704c428283cc65f9c68002c1fbb5b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7G5KET3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7G5KET3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000596276\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Aspergillus\",\"Circumdati\"],\"scientificName\":\"Aspergillus flavus (strain ATCC 200026 / FGSC A1120 / IAM 13836 / NRRL 3357 / JCM 12722 / SRRC 167)\",\"taxonId\":332952}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:25:35.568831+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "79f801166dc030cf4959c0881b37cd1bd39704c428283cc65f9c68002c1fbb5b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7G5KET3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7G5KET3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P00560\",\"source\":\"UniProtKB\"}],\"value\":\"2.7.2.3\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"RU000532\",\"source\":\"RuleBase\"}],\"value\":\"Phosphoglycerate kinase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:25:35.568831+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "79f801166dc030cf4959c0881b37cd1bd39704c428283cc65f9c68002c1fbb5b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7G5KET3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7G5KET3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37754565\",\"source\":\"PubMed\"}],\"value\":\"Localizes to the mitochondrion when phosphorylated\"}]},\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37754565\",\"source\":\"PubMed\"}],\"id\":\"SL-0091\",\"value\":\"Cytoplasm, cytosol\"}},{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37754565\",\"source\":\"PubMed\"}],\"id\":\"SL-0173\",\"value\":\"Mitochondrion\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/5",
  "retrieved_utc": "2026-11-02T04:25:35.568831+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "79f801166dc030cf4959c0881b37cd1bd39704c428283cc65f9c68002c1fbb5b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7G5KET3.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7G5KET3.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"37754565\",\"source\":\"PubMed\"}],\"id\":\"GO:0005829\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:cytosol\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/9",
  "retrieved_utc": "2026-11-02T04:25:35.568831+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "79f801166dc030cf4959c0881b37cd1bd39704c428283cc65f9c68002c1fbb5b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7G5KET3.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7G5KET3.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"37754565\",\"source\":\"PubMed\"}],\"id\":\"GO:0005739\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:mitochondrion\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/10",
  "retrieved_utc": "2026-11-02T04:25:35.568831+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "79f801166dc030cf4959c0881b37cd1bd39704c428283cc65f9c68002c1fbb5b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7G5KET3.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7G5KET3.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhu Z.\",\"Yang M.\",\"Yang G.\",\"Zhang B.\",\"Cao X.\",\"Yuan J.\",\"Ge F.\",\"Wang S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"37754565\"},{\"database\":\"DOI\",\"id\":\"10.1128/mbio.00977-23\"}],\"citationType\":\"journal article\",\"firstPage\":\"e0097723\",\"id\":\"37754565\",\"journal\":\"MBio\",\"lastPage\":\"e0097723\",\"publicationDate\":\"2023\",\"title\":\"PP2C phosphatases Ptc1 and Ptc2 dephosphorylate PGK1 to regulate autophagy and aflatoxin synthesis in the pathogenic fungus Aspergillus flavus.\",\"volume\":\"14\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"SUBCELLULAR LOCATION\",\"DISRUPTION PHENOTYPE\",\"PHOSPHORYLATION AT SER-203\",\"MUTAGENESIS OF SER-203\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:25:35.568831+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "79f801166dc030cf4959c0881b37cd1bd39704c428283cc65f9c68002c1fbb5b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7G5KET3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7G5KET3?format=txt&versions=18)

```json
{
  "entry_version": 18,
  "evidence_id": "H1",
  "excerpt": "ID   PGK1_ASPFN              Reviewed;         417 AA.\nAC   A0A7G5KET3; B8NIQ9;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   10-FEB-2021, sequence version 1.\nDT   28-JAN-2026, entry version 18.\nDE   RecName: Full=Phosphoglycerate kinase {ECO:0000255|RuleBase:RU000532};\nDE            EC=2.7.2.3 {ECO:0000250|UniProtKB:P00560};\nGN   Name=pgk1 {ECO:0000303|PubMed:37754565};\nGN   ORFNames=F9C07_8361 {ECO:0000312|EMBL:QRD93909.1};\nOS   Aspergillus flavus (strain ATCC 200026 / FGSC A1120 / IAM 13836 / NRRL 3357\nOS   / JCM 12722 / SRRC 167).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;\nOC   Aspergillus subgen. Circumdati.\nOX   NCBI_TaxID=332952 {ECO:0000312|Proteomes:UP000596276};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:37.377118+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b429698fb3b322f2fc43bbd8bc72a321c4e8bcf2772d689c13b699dd201233ec",
  "url": "https://rest.uniprot.org/unisave/A0A7G5KET3?format=txt&versions=18"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7G5KET3?format=txt&versions=18)

```json
{
  "entry_version": 18,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, SUBCELLULAR LOCATION, DISRUPTION PHENOTYPE, PHOSPHORYLATION AT\nRP   SER-203, AND MUTAGENESIS OF SER-203.\nRX   PubMed=37754565; DOI=10.1128/mbio.00977-23;\nRA   Zhu Z., Yang M., Yang G., Zhang B., Cao X., Yuan J., Ge F., Wang S.;\nRT   \"PP2C phosphatases Ptc1 and Ptc2 dephosphorylate PGK1 to regulate autophagy\nRT   and aflatoxin synthesis in the pathogenic fungus Aspergillus flavus.\";\nRL   MBio 14:e0097723-e0097723(2023).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:37.377118+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 26-33",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b429698fb3b322f2fc43bbd8bc72a321c4e8bcf2772d689c13b699dd201233ec",
  "url": "https://rest.uniprot.org/unisave/A0A7G5KET3?format=txt&versions=18"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7G5KET3?format=txt&versions=18)

```json
{
  "entry_version": 18,
  "evidence_id": "H3",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Cytoplasm, cytosol {ECO:0000269|PubMed:37754565}.\nCC       Mitochondrion {ECO:0000269|PubMed:37754565}. Note=Localizes to the\nCC       mitochondrion when phosphorylated. {ECO:0000269|PubMed:37754565}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:37.377118+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 54-56",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b429698fb3b322f2fc43bbd8bc72a321c4e8bcf2772d689c13b699dd201233ec",
  "url": "https://rest.uniprot.org/unisave/A0A7G5KET3?format=txt&versions=18"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7G5KET3?format=txt&versions=18)

```json
{
  "entry_version": 18,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0005829; C:cytosol; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:37.377118+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 78-78",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b429698fb3b322f2fc43bbd8bc72a321c4e8bcf2772d689c13b699dd201233ec",
  "url": "https://rest.uniprot.org/unisave/A0A7G5KET3?format=txt&versions=18"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7G5KET3?format=txt&versions=18)

```json
{
  "entry_version": 18,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0005739; C:mitochondrion; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:37.377118+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 79-79",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b429698fb3b322f2fc43bbd8bc72a321c4e8bcf2772d689c13b699dd201233ec",
  "url": "https://rest.uniprot.org/unisave/A0A7G5KET3?format=txt&versions=18"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0005694\nname: chromosome\nnamespace: cellular_component\ndef: \"A structure composed of a very long molecule of DNA and associated proteins (e.g. histones) that carries hereditary information.\" [ISBN:0198547684]\ncomment: Chromosomes include parts that are not part of the chromatin. Examples include the kinetochore.\nsubset: goslim_agr\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_flybase_ribbon\nsubset: goslim_generic\nsubset: goslim_metagenomics\nsubset: goslim_pir\nsubset: goslim_prokaryote\nsubset: goslim_prokaryote_ribbon\nsubset: goslim_yeast\nsynonym: \"chromatid\" RELATED []\nsynonym: \"interphase chromosome\" NARROW []\nsynonym: \"prophase chromosome\" NARROW []\nxref: Wikipedia:Chromosome\nis_a: GO:0043232 ! intracellular membraneless organelle\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005694",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 58583-58605",
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
  "excerpt": "[Term]\nid: GO:0005739\nname: mitochondrion\nnamespace: cellular_component\ndef: \"A semiautonomous, self replicating organelle that occurs in varying numbers, shapes, and sizes in the cytoplasm of virtually all eukaryotic cells. It is notably the site of tissue respiration.\" [GOC:giardia, ISBN:0198506732]\ncomment: Some anaerobic or microaerophilic organisms (e.g. Entamoeba histolytica, Giardia intestinalis and several Microsporidia species) do not have mitochondria, and contain mitochondrion-related organelles (MROs) instead, called mitosomes or hydrogenosomes, very likely derived from mitochondria. To annotate gene products located in these mitochondrial relics in species such as Entamoeba histolytica, Giardia intestinalis or others, please use GO:0032047 'mitosome' or GO:0042566 'hydrogenosome'. (See PMID:24316280 for a list of species currently known to contain mitochondrion-related organelles.)\nsubset: goslim_agr\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_flybase_ribbon\nsubset: goslim_generic\nsubset: goslim_mouse\nsubset: goslim_pir\nsubset: goslim_plant\nsubset: goslim_plant_ribbon\nsubset: goslim_yeast\nsynonym: \"mitochondria\" EXACT []\nxref: NIF_Subcellular:sao1860313010\nxref: Wikipedia:Mitochondrion\nis_a: GO:0043231 ! intracellular membrane-bounded organelle\nrelationship: part_of GO:0005737 ! cytoplasm\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005739",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 58975-58998",
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
  "excerpt": "[Term]\nid: GO:0005813\nname: centrosome\nnamespace: cellular_component\ndef: \"A structure comprised of a core structure (in most organisms, a pair of centrioles) and peripheral material from which a microtubule-based structure, such as a spindle apparatus, is organized. Centrosomes occur close to the nucleus during interphase in many eukaryotic cells, though in animal cells it changes continually during the cell-division cycle.\" [GOC:mah, ISBN:0198547684]\nsubset: goslim_pir\nxref: Wikipedia:Centrosome\nis_a: GO:0005815 ! microtubule organizing center\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005813",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 59790-59798",
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
  "excerpt": "[Term]\nid: GO:0044196\nname: host cell nucleolus\nnamespace: cellular_component\ndef: \"A small, dense body one or more of which are present in the nucleus of eukaryotic host cells.\" [GOC:jl]\nis_a: GO:0044094 ! host cell nuclear part\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0044196",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 255128-255134",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 110. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
