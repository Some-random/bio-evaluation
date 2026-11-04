# GO_cellular_component_0117

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0117.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **B** — endoplasmic reticulum membrane

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MATTLTPTQRYAAGALLALALRQAQIHQSVLLGAHHHHDDDDEEQGRTSTSSGGGGGSSSSSSNSGAGADADLWTHDSHGLLRPVFRFLEIDPKAWSGLEETAASSEAKHHIGAFLRIIFEEDGESSSDRSVQELALAKGVDVMVMSLGNDSEVGNTIKGGDQDALPSSSGTDKSPGESSHDDQLGINKLTLDDIPANNHRKMALLFALLSACVADKPVSQEEEDRKSTRFRKGYDARHRVALRLLSTWLDVKWIKMEAIEVMVACSAMAAAKEQEQSQESASPKSKWEKWKRGGIIGAAALTGGALLAITGGLAAPAIAAGFGALAPTLGTLVPVIGASGFAAMATAAGSVAGSVAVAASFGAAGAGLTGSKMARRIGSVKEFEFKPIGENHNQGRLAVGILISGFAFDEDDFCRPWEGWQDNLERYILQWESKHIIAVSTAIQDWLTSRLAMELMKQGAMRTVLSGLLAAFAWPATLLAATDFIDSKWSVAIDRSDKAGKMLAEVLLKGLQGNRPVTLIGFSLGARVIFKCLQELALSSDNEGLVERVVLLGAPVSVKGERWEAARKMVAGRFVNVYSTDDWILGVTFRASLLTQGLAGIQAIDVPGVENVDVTELVDGHSSYLSAAQQILEHLELNTYYPVFVPLSAANEETDGTVAQ

[Multiple Choices]
A. kinetoplast
B. endoplasmic reticulum membrane
C. glutamatergic synapse
D. collagen-containing extracellular matrix
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

> The supplied sequence matches a UniProt record annotated to the endoplasmic reticulum membrane; the record includes experimental evidence codes for that localization and an IDA GO annotation. This supports the expected answer for this sequence.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple strongly hydrophobic stretches consistent with membrane-spanning helices, rather than the repeated collagen-like motifs expected for a collagen matrix protein. In eukaryotic cells, multipass membrane proteins are generally inserted into the ER membrane, making B a credible choice over the kinetoplast, glutamatergic synapse, and collagen-containing extracellular matrix alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence provides a transferable membrane-protein signal that meaningfully favors the ER-membrane option among those offered. It does not establish the protein’s precise localization independently, but the distractors are substantially less consistent with its sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered option is comparably supported by the sequence features and general cell biology.


### Important caveats

- Hydrophobic transmembrane segments alone do not uniquely identify the ER as the final or primary location; the inference is strongest relative to these particular alternatives.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple strongly hydrophobic stretches consistent with membrane-spanning helices, rather than the repeated collagen-like motifs expected for a collagen matrix protein. In eukaryotic cells, multipass membrane proteins are generally inserted into the ER membrane, making B a credible choice over the kinetoplast, glutamatergic synapse, and collagen-containing extracellular matrix alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence provides a transferable membrane-protein signal that meaningfully favors the ER-membrane option among those offered. It does not establish the protein’s precise localization independently, but the distractors are substantially less consistent with its sequence."
  },
  "case_id": "GO_cellular_component_0117",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches a UniProt record annotated to the endoplasmic reticulum membrane; the record includes experimental evidence codes for that localization and an IDA GO annotation. This supports the expected answer for this sequence."
  },
  "important_caveats": [
    "Hydrophobic transmembrane segments alone do not uniquely identify the ER as the final or primary location; the inference is strongest relative to these particular alternatives."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option is comparably supported by the sequence features and general cell biology."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0117",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches a UniProt record annotated to the endoplasmic reticulum membrane; the record includes experimental evidence codes for that localization and an IDA GO annotation. This supports the expected answer for this sequence.",
    "evidence_ids": ["C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple strongly hydrophobic stretches consistent with membrane-spanning helices, rather than the repeated collagen-like motifs expected for a collagen matrix protein. In eukaryotic cells, multipass membrane proteins are generally inserted into the ER membrane, making B a credible choice over the kinetoplast, glutamatergic synapse, and collagen-containing extracellular matrix alternatives.",
    "missing_item_specific_fact": "",
    "reason": "The sequence provides a transferable membrane-protein signal that meaningfully favors the ER-membrane option among those offered. It does not establish the protein’s precise localization independently, but the distractors are substantially less consistent with its sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option is comparably supported by the sequence features and general cell biology."
  },
  "important_caveats": [
    "Hydrophobic transmembrane segments alone do not uniquely identify the ER as the final or primary location; the inference is strongest relative to these particular alternatives."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q10SS2 annotates this protein as 'Endoplasmic reticulum membrane; Multi-pass membrane protein' with direct assay evidence (ECO:0000269) from two independent experimental studies (PubMed:35748750 and PubMed:36657664). The GO annotation GO:0005789 (C:endoplasmic reticulum membrane) carries IDA:UniProtKB evidence. The expected answer B is experimentally supported.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple long hydrophobic stretches (e.g., ~residues 130-160 'MALLFALLSACVADKPVSQEEEDRKSTRFRKGYDARHRVALRLLSTWLDVKWIKMEAIEVMVACSAMAAAKEQEQSQESASPKSKWEKWKRGGIIGAAALTGGALLAITGGLAAPAIAAGFGALAPTLGTLVPVIGASGFAAMATAAGSVAGSVAVAASFGAAGAGLTGSKMARRIGSVKEFEFKPIGENHNQGRLAVGILISGFAFDEDDFCRPWEGWQDNLERYILQWESKHIIAVSTAIQDWLTSRLAMELMKQGAMRTVLSGLLAAFAWPATLLAATDFIDSKWSVAIDRSDKAGKMLAEVLLKGLQGNRPVTLIGFSLGARVIFKCLQELALSSDNEGLVERVVLLGAPVSVKGERWEAARKMVAGRFVNVYSTDDWILGVTFRASLLTQGLAGIQAIDVPGVENVDVTELVDGHSSYLSAAQQILEHLELNTYYPVFVPLSAANEETDGTVAQ') indicating a multi-pass transmembrane protein. Among the four choices: (A) Kinetoplast is a mitochondrial DNA structure found exclusively in kinetoplastid parasites (Trypanosoma, Leishmania)—a multi-pass TM protein without mitochondrial targeting signals cannot be there; (C) Glutamatergic synapse is an animal neuronal structure requiring neurotransmitter receptors/channels with specific domain architectures (e.g., ionotropic glutamate receptor domains) absent here; (D) Collagen-containing ECM requires secreted proteins with collagen Gly-X-Y repeats and signal peptides, incompatible with a multi-pass TM architecture. Only (B) ER membrane is a membrane compartment compatible with a multi-pass TM protein. The general principle that multi-pass TM proteins without signal peptides for secretion or mitochondrial targeting reside in the ER membrane is well-established transferable knowledge.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The multi-pass transmembrane architecture is directly observable in the sequence and is a strong, transferable structural feature. Among the four offered choices, only B is a membrane compartment. The other three are eliminable by general biology: kinetoplast is organism-restricted to parasites, glutamatergic synapse requires animal neuronal machinery, and collagen ECM requires secreted proteins. No target-specific annotation is needed to distinguish B from the alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The multi-pass TM architecture uniquely points to a membrane compartment among the four choices. Kinetoplast (A) is restricted to kinetoplastids, glutamatergic synapse (C) to animal neurons, and collagen ECM (D) to secreted proteins. Only B is mechanistically compatible with the observed sequence features.


### Important caveats

- The reviewer evidence confirms experimental (IDA) support for ER membrane localization, but the model was not given the organism identity or protein name.
- The sequence is from rice (Oryza sativa), but the model must infer this or at least rule out animal-specific compartments from sequence features alone.
- Multi-pass TM proteins could theoretically reside at other membranes (Golgi, plasma membrane), but those are not among the offered choices, so B is the unique compatible answer.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple long hydrophobic stretches (e.g., ~residues 130-160 'MALLFALLSACVADKPVSQEEEDRKSTRFRKGYDARHRVALRLLSTWLDVKWIKMEAIEVMVACSAMAAAKEQEQSQESASPKSKWEKWKRGGIIGAAALTGGALLAITGGLAAPAIAAGFGALAPTLGTLVPVIGASGFAAMATAAGSVAGSVAVAASFGAAGAGLTGSKMARRIGSVKEFEFKPIGENHNQGRLAVGILISGFAFDEDDFCRPWEGWQDNLERYILQWESKHIIAVSTAIQDWLTSRLAMELMKQGAMRTVLSGLLAAFAWPATLLAATDFIDSKWSVAIDRSDKAGKMLAEVLLKGLQGNRPVTLIGFSLGARVIFKCLQELALSSDNEGLVERVVLLGAPVSVKGERWEAARKMVAGRFVNVYSTDDWILGVTFRASLLTQGLAGIQAIDVPGVENVDVTELVDGHSSYLSAAQQILEHLELNTYYPVFVPLSAANEETDGTVAQ') indicating a multi-pass transmembrane protein. Among the four choices: (A) Kinetoplast is a mitochondrial DNA structure found exclusively in kinetoplastid parasites (Trypanosoma, Leishmania)—a multi-pass TM protein without mitochondrial targeting signals cannot be there; (C) Glutamatergic synapse is an animal neuronal structure requiring neurotransmitter receptors/channels with specific domain architectures (e.g., ionotropic glutamate receptor domains) absent here; (D) Collagen-containing ECM requires secreted proteins with collagen Gly-X-Y repeats and signal peptides, incompatible with a multi-pass TM architecture. Only (B) ER membrane is a membrane compartment compatible with a multi-pass TM protein. The general principle that multi-pass TM proteins without signal peptides for secretion or mitochondrial targeting reside in the ER membrane is well-established transferable knowledge.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The multi-pass transmembrane architecture is directly observable in the sequence and is a strong, transferable structural feature. Among the four offered choices, only B is a membrane compartment. The other three are eliminable by general biology: kinetoplast is organism-restricted to parasites, glutamatergic synapse requires animal neuronal machinery, and collagen ECM requires secreted proteins. No target-specific annotation is needed to distinguish B from the alternatives."
  },
  "case_id": "GO_cellular_component_0117",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q10SS2 annotates this protein as 'Endoplasmic reticulum membrane; Multi-pass membrane protein' with direct assay evidence (ECO:0000269) from two independent experimental studies (PubMed:35748750 and PubMed:36657664). The GO annotation GO:0005789 (C:endoplasmic reticulum membrane) carries IDA:UniProtKB evidence. The expected answer B is experimentally supported."
  },
  "important_caveats": [
    "The reviewer evidence confirms experimental (IDA) support for ER membrane localization, but the model was not given the organism identity or protein name.",
    "The sequence is from rice (Oryza sativa), but the model must infer this or at least rule out animal-specific compartments from sequence features alone.",
    "Multi-pass TM proteins could theoretically reside at other membranes (Golgi, plasma membrane), but those are not among the offered choices, so B is the unique compatible answer."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The multi-pass TM architecture uniquely points to a membrane compartment among the four choices. Kinetoplast (A) is restricted to kinetoplastids, glutamatergic synapse (C) to animal neurons, and collagen ECM (D) to secreted proteins. Only B is mechanistically compatible with the observed sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0117",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q10SS2 annotates this protein as 'Endoplasmic reticulum membrane; Multi-pass membrane protein' with direct assay evidence (ECO:0000269) from two independent experimental studies (PubMed:35748750 and PubMed:36657664). The GO annotation GO:0005789 (C:endoplasmic reticulum membrane) carries IDA:UniProtKB evidence. The expected answer B is experimentally supported.",
    "evidence_ids": ["C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple long hydrophobic stretches (e.g., ~residues 130-160 'MALLFALLSACVADKPVSQEEEDRKSTRFRKGYDARHRVALRLLSTWLDVKWIKMEAIEVMVACSAMAAAKEQEQSQESASPKSKWEKWKRGGIIGAAALTGGALLAITGGLAAPAIAAGFGALAPTLGTLVPVIGASGFAAMATAAGSVAGSVAVAASFGAAGAGLTGSKMARRIGSVKEFEFKPIGENHNQGRLAVGILISGFAFDEDDFCRPWEGWQDNLERYILQWESKHIIAVSTAIQDWLTSRLAMELMKQGAMRTVLSGLLAAFAWPATLLAATDFIDSKWSVAIDRSDKAGKMLAEVLLKGLQGNRPVTLIGFSLGARVIFKCLQELALSSDNEGLVERVVLLGAPVSVKGERWEAARKMVAGRFVNVYSTDDWILGVTFRASLLTQGLAGIQAIDVPGVENVDVTELVDGHSSYLSAAQQILEHLELNTYYPVFVPLSAANEETDGTVAQ') indicating a multi-pass transmembrane protein. Among the four choices: (A) Kinetoplast is a mitochondrial DNA structure found exclusively in kinetoplastid parasites (Trypanosoma, Leishmania)—a multi-pass TM protein without mitochondrial targeting signals cannot be there; (C) Glutamatergic synapse is an animal neuronal structure requiring neurotransmitter receptors/channels with specific domain architectures (e.g., ionotropic glutamate receptor domains) absent here; (D) Collagen-containing ECM requires secreted proteins with collagen Gly-X-Y repeats and signal peptides, incompatible with a multi-pass TM architecture. Only (B) ER membrane is a membrane compartment compatible with a multi-pass TM protein. The general principle that multi-pass TM proteins without signal peptides for secretion or mitochondrial targeting reside in the ER membrane is well-established transferable knowledge.",
    "missing_item_specific_fact": "",
    "reason": "The multi-pass transmembrane architecture is directly observable in the sequence and is a strong, transferable structural feature. Among the four offered choices, only B is a membrane compartment. The other three are eliminable by general biology: kinetoplast is organism-restricted to parasites, glutamatergic synapse requires animal neuronal machinery, and collagen ECM requires secreted proteins. No target-specific annotation is needed to distinguish B from the alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The multi-pass TM architecture uniquely points to a membrane compartment among the four choices. Kinetoplast (A) is restricted to kinetoplastids, glutamatergic synapse (C) to animal neurons, and collagen ECM (D) to secreted proteins. Only B is mechanistically compatible with the observed sequence features."
  },
  "important_caveats": [
    "The reviewer evidence confirms experimental (IDA) support for ER membrane localization, but the model was not given the organism identity or protein name.",
    "The sequence is from rice (Oryza sativa), but the model must infer this or at least rule out animal-specific compartments from sequence features alone.",
    "Multi-pass TM proteins could theoretically reside at other membranes (Golgi, plasma membrane), but those are not among the offered choices, so B is the unique compatible answer."
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
  "benchmark_sequence_length": 661,
  "benchmark_sequence_sha256": "39874e66d1fa3c1f88df736d930d8be5e1b5b47d211b76fff951546b4ad15a7b",
  "current_entry_audit": {
    "entryVersion": 122,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2006-08-22",
    "sequenceVersion": 1
  },
  "current_record_sha256": "0a6a8d6a3c909a1dbd7c765a1a1d325767f551df7a3b5795f41c6d5c449c4e27",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 661,
  "current_source_sequence_sha256": "39874e66d1fa3c1f88df736d930d8be5e1b5b47d211b76fff951546b4ad15a7b",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 121,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q10SS2",
  "selected_historical_entry_version": 121,
  "selected_historical_record_sha256": "acc4e547beb155cdd1e60fb276d5cc6296693b0794b6f3a69d9c2d66a4f46eda",
  "selected_historical_source_sequence_length": 661,
  "selected_historical_source_sequence_sha256": "39874e66d1fa3c1f88df736d930d8be5e1b5b47d211b76fff951546b4ad15a7b",
  "selected_historical_version": {
    "accession": "Q10SS2",
    "database": "Swiss-Prot",
    "entryVersion": 121,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "STS1_ORYSJ",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q10SS2.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q10SS2\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:30:29.234158+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a6a8d6a3c909a1dbd7c765a1a1d325767f551df7a3b5795f41c6d5c449c4e27",
  "url": "https://rest.uniprot.org/uniprotkb/Q10SS2.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q10SS2.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":122,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2006-08-22\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:30:29.234158+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a6a8d6a3c909a1dbd7c765a1a1d325767f551df7a3b5795f41c6d5c449c4e27",
  "url": "https://rest.uniprot.org/uniprotkb/Q10SS2.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q10SS2.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Rice\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"Liliopsida\",\"Poales\",\"Poaceae\",\"BOP clade\",\"Oryzoideae\",\"Oryzeae\",\"Oryzinae\",\"Oryza\",\"Oryza sativa\"],\"scientificName\":\"Oryza sativa subsp. japonica\",\"taxonId\":39947}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:30:29.234158+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a6a8d6a3c909a1dbd7c765a1a1d325767f551df7a3b5795f41c6d5c449c4e27",
  "url": "https://rest.uniprot.org/uniprotkb/Q10SS2.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q10SS2.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35748750\",\"source\":\"PubMed\"}],\"value\":\"3.1.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Lipase STS1\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36657664\",\"source\":\"PubMed\"}],\"value\":\"Protein LEAKED AND DELAYED DEGRADED TAPETUM 1\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"35748750\",\"source\":\"PubMed\"}],\"value\":\"Protein SWOLLEN TAPETUM AND STERILITY 1\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Transmembrane and coiled-coil domain-containing protein STS1\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:30:29.234158+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a6a8d6a3c909a1dbd7c765a1a1d325767f551df7a3b5795f41c6d5c449c4e27",
  "url": "https://rest.uniprot.org/uniprotkb/Q10SS2.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q10SS2.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35748750\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36657664\",\"source\":\"PubMed\"}],\"id\":\"SL-0097\",\"value\":\"Endoplasmic reticulum membrane\"},\"topology\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"id\":\"SL-9909\",\"value\":\"Multi-pass membrane protein\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:30:29.234158+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a6a8d6a3c909a1dbd7c765a1a1d325767f551df7a3b5795f41c6d5c449c4e27",
  "url": "https://rest.uniprot.org/uniprotkb/Q10SS2.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q10SS2.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"35748750\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000314\",\"id\":\"36657664\",\"source\":\"PubMed\"}],\"id\":\"GO:0005789\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:endoplasmic reticulum membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/19",
  "retrieved_utc": "2026-11-02T04:30:29.234158+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a6a8d6a3c909a1dbd7c765a1a1d325767f551df7a3b5795f41c6d5c449c4e27",
  "url": "https://rest.uniprot.org/uniprotkb/Q10SS2.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q10SS2.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Yuan G.\",\"Zou T.\",\"He Z.\",\"Xiao Q.\",\"Li G.\",\"Liu S.\",\"Xiong P.\",\"Chen H.\",\"Peng K.\",\"Zhang X.\",\"Luo T.\",\"Zhou D.\",\"Yang S.\",\"Zhou F.\",\"Zhang K.\",\"Zheng K.\",\"Han Y.\",\"Zhu J.\",\"Liang Y.\",\"Deng Q.\",\"Wang S.\",\"Sun C.\",\"Yu X.\",\"Liu H.\",\"Wang L.\",\"Li P.\",\"Li S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"35748750\"},{\"database\":\"DOI\",\"id\":\"10.1093/plphys/kiac307\"}],\"citationType\":\"journal article\",\"firstPage\":\"352\",\"id\":\"35748750\",\"journal\":\"Plant Physiol.\",\"lastPage\":\"370\",\"publicationDate\":\"2022\",\"title\":\"SWOLLEN TAPETUM AND STERILITY 1 is required for tapetum degeneration and pollen wall formation in rice.\",\"volume\":\"190\"},\"referenceNumber\":7,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"SUBCELLULAR LOCATION\",\"INTERACTION WITH PKS10/PKS2 AND 4CLL9/ACOS12\",\"DEVELOPMENTAL STAGE\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/6",
  "retrieved_utc": "2026-11-02T04:30:29.234158+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a6a8d6a3c909a1dbd7c765a1a1d325767f551df7a3b5795f41c6d5c449c4e27",
  "url": "https://rest.uniprot.org/uniprotkb/Q10SS2.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q10SS2.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Sun Z.\",\"Liu K.\",\"Chen C.\",\"Chen D.\",\"Peng Z.\",\"Zhou R.\",\"Liu L.\",\"He D.\",\"Duan W.\",\"Chen H.\",\"Huang C.\",\"Ruan Z.\",\"Zhang Y.\",\"Cao L.\",\"Zhan X.\",\"Cheng S.\",\"Sun L.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"36657664\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.plantsci.2023.111596\"}],\"citationType\":\"journal article\",\"firstPage\":\"111596\",\"id\":\"36657664\",\"journal\":\"Plant Sci.\",\"lastPage\":\"111596\",\"publicationDate\":\"2023\",\"title\":\"OsLDDT1, encoding a transmembrane structural DUF726 family protein, is essential for tapetum degradation and pollen formation in rice.\",\"volume\":\"329\"},\"referenceNumber\":8,\"referencePositions\":[\"FUNCTION\",\"SUBCELLULAR LOCATION\",\"DEVELOPMENTAL STAGE\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/7",
  "retrieved_utc": "2026-11-02T04:30:29.234158+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0a6a8d6a3c909a1dbd7c765a1a1d325767f551df7a3b5795f41c6d5c449c4e27",
  "url": "https://rest.uniprot.org/uniprotkb/Q10SS2.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q10SS2?format=txt&versions=121)

```json
{
  "entry_version": 121,
  "evidence_id": "H1",
  "excerpt": "ID   STS1_ORYSJ              Reviewed;         661 AA.\nAC   Q10SS2; A3ADE3; Q10SS1;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   22-AUG-2006, sequence version 1.\nDT   28-JAN-2026, entry version 121.\nDE   RecName: Full=Transmembrane and coiled-coil domain-containing protein STS1 {ECO:0000305};\nDE   AltName: Full=Lipase STS1 {ECO:0000305};\nDE            EC=3.1.1.- {ECO:0000269|PubMed:35748750};\nDE   AltName: Full=Protein LEAKED AND DELAYED DEGRADED TAPETUM 1 {ECO:0000303|PubMed:36657664};\nDE   AltName: Full=Protein SWOLLEN TAPETUM AND STERILITY 1 {ECO:0000303|PubMed:35748750};\nGN   Name=STS1 {ECO:0000303|PubMed:35748750};\nGN   Synonyms=LDDT1 {ECO:0000303|PubMed:36657664};\nGN   OrderedLocusNames=Os03g0112800 {ECO:0000312|EMBL:BAS81940.1},\nGN   LOC_Os03g02170 {ECO:0000312|EMBL:ABF93614.1};\nGN   ORFNames=OsJ_09144 {ECO:0000312|EMBL:EAZ25332.1};\nOS   Oryza sativa subsp. japonica (Rice).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; Liliopsida; Poales; Poaceae; BOP clade;\nOC   Oryzoideae; Oryzeae; Oryzinae; Oryza; Oryza sativa.\nOX   NCBI_TaxID=39947;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:34.944114+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-20",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "acc4e547beb155cdd1e60fb276d5cc6296693b0794b6f3a69d9c2d66a4f46eda",
  "url": "https://rest.uniprot.org/unisave/Q10SS2?format=txt&versions=121"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q10SS2?format=txt&versions=121)

```json
{
  "entry_version": 121,
  "evidence_id": "H2",
  "excerpt": "RN   [7]\nRP   FUNCTION, CATALYTIC ACTIVITY, SUBCELLULAR LOCATION, INTERACTION WITH\nRP   PKS10/PKS2 AND 4CLL9/ACOS12, DEVELOPMENTAL STAGE, AND DISRUPTION PHENOTYPE.\nRX   PubMed=35748750; DOI=10.1093/plphys/kiac307;\nRA   Yuan G., Zou T., He Z., Xiao Q., Li G., Liu S., Xiong P., Chen H., Peng K.,\nRA   Zhang X., Luo T., Zhou D., Yang S., Zhou F., Zhang K., Zheng K., Han Y.,\nRA   Zhu J., Liang Y., Deng Q., Wang S., Sun C., Yu X., Liu H., Wang L., Li P.,\nRA   Li S.;\nRT   \"SWOLLEN TAPETUM AND STERILITY 1 is required for tapetum degeneration and\nRT   pollen wall formation in rice.\";\nRL   Plant Physiol. 190:352-370(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:34.944114+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 94-104",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "acc4e547beb155cdd1e60fb276d5cc6296693b0794b6f3a69d9c2d66a4f46eda",
  "url": "https://rest.uniprot.org/unisave/Q10SS2?format=txt&versions=121"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q10SS2?format=txt&versions=121)

```json
{
  "entry_version": 121,
  "evidence_id": "H3",
  "excerpt": "RN   [8]\nRP   FUNCTION, SUBCELLULAR LOCATION, DEVELOPMENTAL STAGE, AND DISRUPTION\nRP   PHENOTYPE.\nRX   PubMed=36657664; DOI=10.1016/j.plantsci.2023.111596;\nRA   Sun Z., Liu K., Chen C., Chen D., Peng Z., Zhou R., Liu L., He D., Duan W.,\nRA   Chen H., Huang C., Ruan Z., Zhang Y., Cao L., Zhan X., Cheng S., Sun L.;\nRT   \"OsLDDT1, encoding a transmembrane structural DUF726 family protein, is\nRT   essential for tapetum degradation and pollen formation in rice.\";\nRL   Plant Sci. 329:111596-111596(2023).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:34.944114+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 105-113",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "acc4e547beb155cdd1e60fb276d5cc6296693b0794b6f3a69d9c2d66a4f46eda",
  "url": "https://rest.uniprot.org/unisave/Q10SS2?format=txt&versions=121"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q10SS2?format=txt&versions=121)

```json
{
  "entry_version": 121,
  "evidence_id": "H4",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Endoplasmic reticulum membrane\nCC       {ECO:0000269|PubMed:35748750, ECO:0000269|PubMed:36657664}; Multi-pass\nCC       membrane protein {ECO:0000255}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:34.944114+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 123-125",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "acc4e547beb155cdd1e60fb276d5cc6296693b0794b6f3a69d9c2d66a4f46eda",
  "url": "https://rest.uniprot.org/unisave/Q10SS2?format=txt&versions=121"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q10SS2?format=txt&versions=121)

```json
{
  "entry_version": 121,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0005789; C:endoplasmic reticulum membrane; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:34.944114+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 161-161",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "acc4e547beb155cdd1e60fb276d5cc6296693b0794b6f3a69d9c2d66a4f46eda",
  "url": "https://rest.uniprot.org/unisave/Q10SS2?format=txt&versions=121"
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
  "excerpt": "[Term]\nid: GO:0020023\nname: kinetoplast\nnamespace: cellular_component\ndef: \"A sub-structure within the large single mitochondrion of kinetoplastid parasites and which is closely associated with the flagellar pocket and basal body of the flagellum.\" [GOC:mb]\nxref: Wikipedia:Kinetoplast\nis_a: GO:0110165 ! cellular anatomical structure\nrelationship: part_of GO:0005739 ! mitochondrion\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0020023",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 155291-155299",
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
  "excerpt": "[Term]\nid: GO:0098978\nname: glutamatergic synapse\nnamespace: cellular_component\ndef: \"A synapse that uses glutamate as a neurotransmitter.\" [GOC:dos]\nsubset: goslim_synapse\nis_a: GO:0045202 ! synapse\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0098978",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 412689-412696",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 117. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
