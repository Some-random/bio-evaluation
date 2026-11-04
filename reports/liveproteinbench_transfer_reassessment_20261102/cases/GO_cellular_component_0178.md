# GO_cellular_component_0178

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0178.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **D** — primosome complex

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSVAHVALPVPLPRTFDYLLPEGMAVKAGCRVRVPFGKQERIGIVAAVSERSELPLDELKPVAEALDDEPVFSTTVWRLLMWAAEYYHHPIGDVLFHALPVMLRQGKPASATPLWYWFATEQGQVVDLNGLKRSRKQQQALAALRQGKIWRHQVGELEFNEAALQALRGKGLAELACEAPALTDWRSAYSVAGERLRLNTEQATAVGAIHSAADRFSAWLLAGITGSGKTEVYLSVLENVLAQGRQALVMVPEIGLTPQTIARFRQRFNAPVEVLHSGLNDSERLSAWLKAKNGEAAIVIGTRSSLFTPFKDLGVIVIDEEHDSSYKQQEGWRYHARDLAVWRAHSEQIPIILGSATPALETLHNVRQGKYRQLTLSKRAGNARPAQQHVLDLKGQPLQAGLSPALISRMRQHLQADNQVILFLNRRGFAPALLCHDCGWIAECPRCDSYYTLHQAQHHLRCHHCDSQRPIPRQCPSCGSTHLVPVGIGTEQLEQALAPLFPEVPISRIDRDTTSRKGALEEHLAAVHRGGARILIGTQMLAKGHHFPDVTLVSLLDVDGALFSADFRSAERFAQLYTQVSGRAGRAGKQGEVILQTHHPEHPLLQTLLYKGYDAFAEQALAERQTMQLPPWTSHVLIRAEDHNNQQAPLFLQQLRNLLQASPLADEKLWVLGPVPALAPKRGGRWRWQILLQHPSRVRLQHIVSGTLALINTLPEARKVKWVLDVDPIEG

[Multiple Choices]
A. early endosome membrane
B. host cell plasma membrane
C. glutamatergic synapse
D. primosome complex
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

> The sequence-matched UniProt record identifies the protein as replication restart protein PriA and annotates it to the primosome complex. That GO annotation is computational (IEA: UniProtKB-UniRule), not direct experimental localization evidence, but it is biologically consistent with PriA's role in replication restart. The cited structural work supports PriA's DNA-binding and ATPase functions, though it does not by itself establish primosome membership.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has the characteristics of a large ATP-dependent DNA helicase, including a P-loop NTPase motif (…GSGKTE…) and additional helicase-like sequence features. Transferable knowledge that bacterial PriA-family helicases participate in replication restart makes a replication-associated complex such as the primosome a credible choice. The other options describe eukaryotic membrane or synaptic locations and are poorly matched to this kind of soluble DNA-replication protein.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and biological role support a meaningful family-level inference toward the primosome complex without requiring recall of this exact protein's database annotation. The inference is probabilistic; the GO annotation itself is computational.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, the replication-associated complex is meaningfully distinguished from the membrane and synaptic alternatives.


### Important caveats

- The supplied GO annotation is UniRule-based rather than direct experimental evidence for complex membership.
- The reviewer-only sequence-matched record supports the key but was not part of the original model input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has the characteristics of a large ATP-dependent DNA helicase, including a P-loop NTPase motif (…GSGKTE…) and additional helicase-like sequence features. Transferable knowledge that bacterial PriA-family helicases participate in replication restart makes a replication-associated complex such as the primosome a credible choice. The other options describe eukaryotic membrane or synaptic locations and are poorly matched to this kind of soluble DNA-replication protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and biological role support a meaningful family-level inference toward the primosome complex without requiring recall of this exact protein's database annotation. The inference is probabilistic; the GO annotation itself is computational."
  },
  "case_id": "GO_cellular_component_0178",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record identifies the protein as replication restart protein PriA and annotates it to the primosome complex. That GO annotation is computational (IEA: UniProtKB-UniRule), not direct experimental localization evidence, but it is biologically consistent with PriA's role in replication restart. The cited structural work supports PriA's DNA-binding and ATPase functions, though it does not by itself establish primosome membership."
  },
  "important_caveats": [
    "The supplied GO annotation is UniRule-based rather than direct experimental evidence for complex membership.",
    "The reviewer-only sequence-matched record supports the key but was not part of the original model input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, the replication-associated complex is meaningfully distinguished from the membrane and synaptic alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0178",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record identifies the protein as replication restart protein PriA and annotates it to the primosome complex. That GO annotation is computational (IEA: UniProtKB-UniRule), not direct experimental localization evidence, but it is biologically consistent with PriA's role in replication restart. The cited structural work supports PriA's DNA-binding and ATPase functions, though it does not by itself establish primosome membership.",
    "evidence_ids": ["C4", "C5", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has the characteristics of a large ATP-dependent DNA helicase, including a P-loop NTPase motif (…GSGKTE…) and additional helicase-like sequence features. Transferable knowledge that bacterial PriA-family helicases participate in replication restart makes a replication-associated complex such as the primosome a credible choice. The other options describe eukaryotic membrane or synaptic locations and are poorly matched to this kind of soluble DNA-replication protein.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and biological role support a meaningful family-level inference toward the primosome complex without requiring recall of this exact protein's database annotation. The inference is probabilistic; the GO annotation itself is computational."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, the replication-associated complex is meaningfully distinguished from the membrane and synaptic alternatives."
  },
  "important_caveats": [
    "The supplied GO annotation is UniRule-based rather than direct experimental evidence for complex membership.",
    "The reviewer-only sequence-matched record supports the key but was not part of the original model input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A6TGC5, PRIA_KLEP7) annotates this protein as Replication restart protein PriA (ATP-dependent DNA helicase, EC 5.6.2.4) with GO:1990077 (primosome complex) via IEA:UniProtKB-UniRule. The GO definition for primosome complex explicitly includes proteins that 'form at the origin of replication or stalled replication forks and function in replication primer synthesis.' PriA is a well-characterized replication restart helicase that participates in primosome assembly. The annotation is computational (HAMAP rule MF_00983), but the protein's identity as a replication restart helicase is corroborated by PDB structures (4NL4, 4NL8) and PubMed:24379377.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H3](#evidence-h3), [GO4](#evidence-go4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains unambiguous Walker A (GSGKTEVYLSVLENVLAQ) and Walker B (IVIDEEHDSSY) motifs diagnostic of RecA-like ATP-dependent helicases, plus multiple Cys-rich zinc-binding clusters (CHDCGWIAECPRCDSYYTLHQAQHHLRCHHCDSQRPIPRQCPSCG) characteristic of replication restart helicases like PriA. The protein lacks any transmembrane segments, signal peptides, or eukaryotic targeting sequences, confirming a bacterial cytoplasmic/nucleoid protein. Among the four options, A (early endosome membrane), B (host cell plasma membrane), and C (glutamatergic synapse) are eukaryotic-specific compartments incompatible with a bacterial DNA helicase. The only DNA-replication-associated option is D (primosome complex), which the GO definition explicitly covers as a complex forming at stalled replication forks. Recognition of the RecA-like helicase + zinc-binding architecture as a replication-restart motif is transferable knowledge from E. coli PriA and related bacterial helicases.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can eliminate all three eukaryotic compartments (A, B, C) because the sequence is clearly bacterial (no eukaryotic targeting signals) and contains helicase motifs. The remaining option D (primosome complex) is the only DNA replication/restart-associated compartment, and the specific combination of RecA-like Walker motifs plus zinc-binding domains matches the replication-restart helicase family known from E. coli and other bacteria. This does not require recalling the exact annotation for this Klebsiella PriA entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and C describe eukaryotic-specific compartments (endosome, host cell membrane in viral context, neuronal synapse) that are categorically incompatible with a bacterial DNA helicase bearing Walker A/B and zinc-binding motifs. Only D is a bacterial DNA replication complex. No ambiguity exists among the offered choices.


### Important caveats

- The GO annotation for primosome complex is IEA:UniProtKB-UniRule (computational inference from HAMAP rule), not direct experimental evidence for this specific Klebsiella strain, though the protein family and function are well-established.
- The reviewer-only evidence confirms the sequence matches UniProt A6TGC5 exactly, but the model was not given the organism name or protein name; the reasoning relies solely on sequence motifs and general biological knowledge.
- The GO term 'host cell plasma membrane' (GO:0020002) is defined in the goslim_virus subset, referring to viral interactions with host membranes, further confirming its inapplicability to a bacterial replication protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains unambiguous Walker A (GSGKTEVYLSVLENVLAQ) and Walker B (IVIDEEHDSSY) motifs diagnostic of RecA-like ATP-dependent helicases, plus multiple Cys-rich zinc-binding clusters (CHDCGWIAECPRCDSYYTLHQAQHHLRCHHCDSQRPIPRQCPSCG) characteristic of replication restart helicases like PriA. The protein lacks any transmembrane segments, signal peptides, or eukaryotic targeting sequences, confirming a bacterial cytoplasmic/nucleoid protein. Among the four options, A (early endosome membrane), B (host cell plasma membrane), and C (glutamatergic synapse) are eukaryotic-specific compartments incompatible with a bacterial DNA helicase. The only DNA-replication-associated option is D (primosome complex), which the GO definition explicitly covers as a complex forming at stalled replication forks. Recognition of the RecA-like helicase + zinc-binding architecture as a replication-restart motif is transferable knowledge from E. coli PriA and related bacterial helicases.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate all three eukaryotic compartments (A, B, C) because the sequence is clearly bacterial (no eukaryotic targeting signals) and contains helicase motifs. The remaining option D (primosome complex) is the only DNA replication/restart-associated compartment, and the specific combination of RecA-like Walker motifs plus zinc-binding domains matches the replication-restart helicase family known from E. coli and other bacteria. This does not require recalling the exact annotation for this Klebsiella PriA entry."
  },
  "case_id": "GO_cellular_component_0178",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H3",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A6TGC5, PRIA_KLEP7) annotates this protein as Replication restart protein PriA (ATP-dependent DNA helicase, EC 5.6.2.4) with GO:1990077 (primosome complex) via IEA:UniProtKB-UniRule. The GO definition for primosome complex explicitly includes proteins that 'form at the origin of replication or stalled replication forks and function in replication primer synthesis.' PriA is a well-characterized replication restart helicase that participates in primosome assembly. The annotation is computational (HAMAP rule MF_00983), but the protein's identity as a replication restart helicase is corroborated by PDB structures (4NL4, 4NL8) and PubMed:24379377."
  },
  "important_caveats": [
    "The GO annotation for primosome complex is IEA:UniProtKB-UniRule (computational inference from HAMAP rule), not direct experimental evidence for this specific Klebsiella strain, though the protein family and function are well-established.",
    "The reviewer-only evidence confirms the sequence matches UniProt A6TGC5 exactly, but the model was not given the organism name or protein name; the reasoning relies solely on sequence motifs and general biological knowledge.",
    "The GO term 'host cell plasma membrane' (GO:0020002) is defined in the goslim_virus subset, referring to viral interactions with host membranes, further confirming its inapplicability to a bacterial replication protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C describe eukaryotic-specific compartments (endosome, host cell membrane in viral context, neuronal synapse) that are categorically incompatible with a bacterial DNA helicase bearing Walker A/B and zinc-binding motifs. Only D is a bacterial DNA replication complex. No ambiguity exists among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0178",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A6TGC5, PRIA_KLEP7) annotates this protein as Replication restart protein PriA (ATP-dependent DNA helicase, EC 5.6.2.4) with GO:1990077 (primosome complex) via IEA:UniProtKB-UniRule. The GO definition for primosome complex explicitly includes proteins that 'form at the origin of replication or stalled replication forks and function in replication primer synthesis.' PriA is a well-characterized replication restart helicase that participates in primosome assembly. The annotation is computational (HAMAP rule MF_00983), but the protein's identity as a replication restart helicase is corroborated by PDB structures (4NL4, 4NL8) and PubMed:24379377.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H3", "GO4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains unambiguous Walker A (GSGKTEVYLSVLENVLAQ) and Walker B (IVIDEEHDSSY) motifs diagnostic of RecA-like ATP-dependent helicases, plus multiple Cys-rich zinc-binding clusters (CHDCGWIAECPRCDSYYTLHQAQHHLRCHHCDSQRPIPRQCPSCG) characteristic of replication restart helicases like PriA. The protein lacks any transmembrane segments, signal peptides, or eukaryotic targeting sequences, confirming a bacterial cytoplasmic/nucleoid protein. Among the four options, A (early endosome membrane), B (host cell plasma membrane), and C (glutamatergic synapse) are eukaryotic-specific compartments incompatible with a bacterial DNA helicase. The only DNA-replication-associated option is D (primosome complex), which the GO definition explicitly covers as a complex forming at stalled replication forks. Recognition of the RecA-like helicase + zinc-binding architecture as a replication-restart motif is transferable knowledge from E. coli PriA and related bacterial helicases.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate all three eukaryotic compartments (A, B, C) because the sequence is clearly bacterial (no eukaryotic targeting signals) and contains helicase motifs. The remaining option D (primosome complex) is the only DNA replication/restart-associated compartment, and the specific combination of RecA-like Walker motifs plus zinc-binding domains matches the replication-restart helicase family known from E. coli and other bacteria. This does not require recalling the exact annotation for this Klebsiella PriA entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C describe eukaryotic-specific compartments (endosome, host cell membrane in viral context, neuronal synapse) that are categorically incompatible with a bacterial DNA helicase bearing Walker A/B and zinc-binding motifs. Only D is a bacterial DNA replication complex. No ambiguity exists among the offered choices."
  },
  "important_caveats": [
    "The GO annotation for primosome complex is IEA:UniProtKB-UniRule (computational inference from HAMAP rule), not direct experimental evidence for this specific Klebsiella strain, though the protein family and function are well-established.",
    "The reviewer-only evidence confirms the sequence matches UniProt A6TGC5 exactly, but the model was not given the organism name or protein name; the reasoning relies solely on sequence motifs and general biological knowledge.",
    "The GO term 'host cell plasma membrane' (GO:0020002) is defined in the goslim_virus subset, referring to viral interactions with host membranes, further confirming its inapplicability to a bacterial replication protein."
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
  "benchmark_sequence_length": 731,
  "benchmark_sequence_sha256": "b2380b00e1db13b71a8d25d047aeeaedeb18f37644b3d05f6dae89a8ab7f1dfe",
  "current_entry_audit": {
    "entryVersion": 117,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2007-08-21",
    "sequenceVersion": 1
  },
  "current_record_sha256": "6b4633bf75f6bfd60571af6aec15eee826dbfa4328f9de5dd2c25ee8c8147e5d",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 731,
  "current_source_sequence_sha256": "b2380b00e1db13b71a8d25d047aeeaedeb18f37644b3d05f6dae89a8ab7f1dfe",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 115,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A6TGC5",
  "selected_historical_entry_version": 115,
  "selected_historical_record_sha256": "c7fae64a6685e20b9641d98d65b5f6b293a504b0495a699330088a3a6792ce20",
  "selected_historical_source_sequence_length": 731,
  "selected_historical_source_sequence_sha256": "b2380b00e1db13b71a8d25d047aeeaedeb18f37644b3d05f6dae89a8ab7f1dfe",
  "selected_historical_version": {
    "accession": "A6TGC5",
    "database": "Swiss-Prot",
    "entryVersion": 115,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "PRIA_KLEP7",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A6TGC5.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A6TGC5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:27:05.788123+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6b4633bf75f6bfd60571af6aec15eee826dbfa4328f9de5dd2c25ee8c8147e5d",
  "url": "https://rest.uniprot.org/uniprotkb/A6TGC5.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A6TGC5.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":117,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2007-08-21\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:27:05.788123+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6b4633bf75f6bfd60571af6aec15eee826dbfa4328f9de5dd2c25ee8c8147e5d",
  "url": "https://rest.uniprot.org/uniprotkb/A6TGC5.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A6TGC5.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Enterobacterales\",\"Enterobacteriaceae\",\"Klebsiella\",\"Klebsiella pneumoniae complex\"],\"scientificName\":\"Klebsiella pneumoniae subsp. pneumoniae (strain ATCC 700721 / MGH 78578)\",\"taxonId\":272620}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:27:05.788123+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6b4633bf75f6bfd60571af6aec15eee826dbfa4328f9de5dd2c25ee8c8147e5d",
  "url": "https://rest.uniprot.org/uniprotkb/A6TGC5.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A6TGC5.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_00983\",\"source\":\"HAMAP-Rule\"},{\"evidenceCode\":\"ECO:0000305\",\"id\":\"24379377\",\"source\":\"PubMed\"}],\"value\":\"5.6.2.4\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_00983\",\"source\":\"HAMAP-Rule\"}],\"value\":\"ATP-dependent DNA helicase PriA\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_00983\",\"source\":\"HAMAP-Rule\"},{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"DNA 3'-5' helicase PriA\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24379377\",\"source\":\"PubMed\"}],\"value\":\"PriA DNA helicase\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_00983\",\"source\":\"HAMAP-Rule\"}],\"value\":\"Replication restart protein PriA\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:27:05.788123+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6b4633bf75f6bfd60571af6aec15eee826dbfa4328f9de5dd2c25ee8c8147e5d",
  "url": "https://rest.uniprot.org/uniprotkb/A6TGC5.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A6TGC5.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:1990077\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:primosome complex\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-UniRule\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/17",
  "retrieved_utc": "2026-11-02T04:27:05.788123+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6b4633bf75f6bfd60571af6aec15eee826dbfa4328f9de5dd2c25ee8c8147e5d",
  "url": "https://rest.uniprot.org/uniprotkb/A6TGC5.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A6TGC5.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Bhattacharyya B.\",\"George N.P.\",\"Thurmes T.M.\",\"Zhou R.\",\"Jani N.\",\"Wessel S.R.\",\"Sandler S.J.\",\"Ha T.\",\"Keck J.L.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"24379377\"},{\"database\":\"DOI\",\"id\":\"10.1073/pnas.1318001111\"}],\"citationType\":\"journal article\",\"firstPage\":\"1373\",\"id\":\"24379377\",\"journal\":\"Proc. Natl. Acad. Sci. U.S.A.\",\"lastPage\":\"1378\",\"publicationDate\":\"2014\",\"title\":\"Structural mechanisms of PriA-mediated DNA replication restart.\",\"volume\":\"111\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"4NL4\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"4NL8\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC 700721 / MGH 78578\"}],\"referenceNumber\":3,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.65 ANGSTROMS) IN COMPLEX WITH ADP AND ZN(2+)\",\"X-RAY CRYSTALLOGRAPHY (4.08 ANGSTROMS) IN COMPLEX WITH SSB\",\"FUNCTION AS AN ATPASE\",\"CATALYTIC ACTIVITY\",\"DOMAIN\",\"DNA-BINDING\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:27:05.788123+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6b4633bf75f6bfd60571af6aec15eee826dbfa4328f9de5dd2c25ee8c8147e5d",
  "url": "https://rest.uniprot.org/uniprotkb/A6TGC5.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A6TGC5?format=txt&versions=115)

```json
{
  "entry_version": 115,
  "evidence_id": "H1",
  "excerpt": "ID   PRIA_KLEP7              Reviewed;         731 AA.\nAC   A6TGC5;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   21-AUG-2007, sequence version 1.\nDT   28-JAN-2026, entry version 115.\nDE   RecName: Full=Replication restart protein PriA {ECO:0000255|HAMAP-Rule:MF_00983};\nDE   AltName: Full=ATP-dependent DNA helicase PriA {ECO:0000255|HAMAP-Rule:MF_00983};\nDE            EC=5.6.2.4 {ECO:0000255|HAMAP-Rule:MF_00983, ECO:0000305|PubMed:24379377};\nDE   AltName: Full=DNA 3'-5' helicase PriA {ECO:0000255|HAMAP-Rule:MF_00983, ECO:0000305};\nDE   AltName: Full=PriA DNA helicase {ECO:0000303|PubMed:24379377};\nGN   Name=priA {ECO:0000255|HAMAP-Rule:MF_00983, ECO:0000312|EMBL:ABR79609.1};\nGN   ORFNames=KPN_04230 {ECO:0000312|EMBL:ABR79609.1};\nOS   Klebsiella pneumoniae subsp. pneumoniae (strain ATCC 700721 / MGH 78578).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Enterobacterales; Enterobacteriaceae; Klebsiella/Raoultella group;\nOC   Klebsiella; Klebsiella pneumoniae complex.\nOX   NCBI_TaxID=272620;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:08.474025+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c7fae64a6685e20b9641d98d65b5f6b293a504b0495a699330088a3a6792ce20",
  "url": "https://rest.uniprot.org/unisave/A6TGC5?format=txt&versions=115"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A6TGC5?format=txt&versions=115)

```json
{
  "entry_version": 115,
  "evidence_id": "H2",
  "excerpt": "RN   [3] {ECO:0007744|PDB:4NL4, ECO:0007744|PDB:4NL8}\nRP   X-RAY CRYSTALLOGRAPHY (2.65 ANGSTROMS) IN COMPLEX WITH ADP AND ZN(2+),\nRP   X-RAY CRYSTALLOGRAPHY (4.08 ANGSTROMS) IN COMPLEX WITH SSB, FUNCTION AS AN\nRP   ATPASE, CATALYTIC ACTIVITY, DOMAIN, AND DNA-BINDING.\nRC   STRAIN=ATCC 700721 / MGH 78578;\nRX   PubMed=24379377; DOI=10.1073/pnas.1318001111;\nRA   Bhattacharyya B., George N.P., Thurmes T.M., Zhou R., Jani N., Wessel S.R.,\nRA   Sandler S.J., Ha T., Keck J.L.;\nRT   \"Structural mechanisms of PriA-mediated DNA replication restart.\";\nRL   Proc. Natl. Acad. Sci. U.S.A. 111:1373-1378(2014).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:08.474025+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 31-40",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c7fae64a6685e20b9641d98d65b5f6b293a504b0495a699330088a3a6792ce20",
  "url": "https://rest.uniprot.org/unisave/A6TGC5?format=txt&versions=115"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A6TGC5?format=txt&versions=115)

```json
{
  "entry_version": 115,
  "evidence_id": "H3",
  "excerpt": "DR   GO; GO:1990077; C:primosome complex; IEA:UniProtKB-UniRule.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:08.474025+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 116-116",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c7fae64a6685e20b9641d98d65b5f6b293a504b0495a699330088a3a6792ce20",
  "url": "https://rest.uniprot.org/unisave/A6TGC5?format=txt&versions=115"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0020002\nname: host cell plasma membrane\nnamespace: cellular_component\ndef: \"The plasma membrane surrounding a host cell.\" [GOC:mb]\nsubset: goslim_virus\nis_a: GO:0033644 ! host cell membrane\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0020002",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 155120-155127",
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
  "excerpt": "[Term]\nid: GO:0031901\nname: early endosome membrane\nnamespace: cellular_component\ndef: \"The lipid bilayer surrounding an early endosome.\" [GOC:pz]\nis_a: GO:0010008 ! endosome membrane\nrelationship: part_of GO:0005769 ! early endosome\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0031901",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 180777-180784",
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

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO4",
  "excerpt": "[Term]\nid: GO:1990077\nname: primosome complex\nnamespace: cellular_component\ndef: \"Any of a family of protein complexes that form at the origin of replication or stalled replication forks and function in replication primer synthesis in all organisms. Early complexes initiate double-stranded DNA unwinding. The core unit consists of a replicative helicase and a primase. The helicase further unwinds the DNA and recruits the polymerase machinery. The primase synthesizes RNA primers that act as templates for complementary stand replication by the polymerase machinery. The primosome contains a number of associated proteins and protein complexes and contributes to the processes of replication initiation, lagging strand elongation, and replication restart.\" [GOC:bhm, GOC:mah, PMID:21856207]\nsynonym: \"primosome\" EXACT []\nis_a: GO:0032993 ! protein-DNA complex\nrelationship: part_of GO:0030894 ! replisome\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:1990077",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 549032-549040",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 178. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
