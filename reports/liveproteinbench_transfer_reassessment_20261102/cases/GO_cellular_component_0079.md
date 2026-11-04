# GO_cellular_component_0079

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0079.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **A** — nucleoplasm

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSQSQVPSRAGHYNMTALANALPQANYRQAPWNNGSQMRYNPAGASPNVVGQTQSSPQYNGQPGMGSMPNQGYYMPQQQQQQQQMPQYYGGPMSPSQPQPNMSSRPNVPFYGNQVMSNHQAHPSMGYYYAQVPAYALQGHPPHQAPVDSQSNVVRGPPRKPRQSGHAIWIGNLPSQTDLMSLVHHVCREAQGLESLFLISKSNCAFANFRDEASCLTAQQKLHESKFQSVRLVSRLRKNTVEGASGITAPTGPSATTPQQAVAPEVKEIEQIDSTETQSDNADTDTPTAVGTPDAKGPAVVDAAQKDRFFVLKSLTVEDLDLSVRTGIWATQSHNEEALNSAFKNAENVYLVFSANKSGEYFGYARMVSTINEDPAAAIEFAPKAQSVNEVDLPREIPTEPTKFTPKGRIIDDSARGTIFWEIAREDSSEGVTQEEPAPAVAEQDDTTGGLDGNSENKTWGKPFKLEWLSTTRLPFYRCRGLRNPWNSNREVKIARDGTELEPSVGRRLIGLFNRSHNSPGPRGPMMGMGQMMSPSQQQMPMGYPPPYS

[Multiple Choices]
A. nucleoplasm
B. nucleolus
C. glutamatergic synapse
D. egg chorion
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

> The exact sequence matches a UniProt entry annotated to nucleoplasm. The annotation is IEA:TreeGrafter, so it supports the key as a computational inference, not as direct experimental localization evidence. The author’s exact source snapshot is unknown.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The C-terminal region is consistent with a YTH-domain m6A RNA reader, while the N-terminus is low-complexity. Transferable knowledge of this protein family makes an RNA-processing compartment such as the nucleoplasm more plausible than the nucleolus, which is especially associated with ribosome biogenesis; the sequence offers no apparent basis for the specialized synapse or egg-chorion choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level recognition and the RNA-reader function provide a credible, though probabilistic, basis for preferring nucleoplasm among these options. YTH proteins can have varied localization, so this inference does not establish the protein’s experimentally observed primary location.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence does not prove an exclusive location, but the offered alternatives do not provide a comparably supported second choice.


### Important caveats

- The matching GO annotation is computational (IEA:TreeGrafter), not experimental.
- The author’s annotation snapshot is unknown, and a primary-compartment prediction need not imply that the protein is found nowhere else.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The C-terminal region is consistent with a YTH-domain m6A RNA reader, while the N-terminus is low-complexity. Transferable knowledge of this protein family makes an RNA-processing compartment such as the nucleoplasm more plausible than the nucleolus, which is especially associated with ribosome biogenesis; the sequence offers no apparent basis for the specialized synapse or egg-chorion choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition and the RNA-reader function provide a credible, though probabilistic, basis for preferring nucleoplasm among these options. YTH proteins can have varied localization, so this inference does not establish the protein’s experimentally observed primary location."
  },
  "case_id": "GO_cellular_component_0079",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated to nucleoplasm. The annotation is IEA:TreeGrafter, so it supports the key as a computational inference, not as direct experimental localization evidence. The author’s exact source snapshot is unknown."
  },
  "important_caveats": [
    "The matching GO annotation is computational (IEA:TreeGrafter), not experimental.",
    "The author’s annotation snapshot is unknown, and a primary-compartment prediction need not imply that the protein is found nowhere else."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence does not prove an exclusive location, but the offered alternatives do not provide a comparably supported second choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0079",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated to nucleoplasm. The annotation is IEA:TreeGrafter, so it supports the key as a computational inference, not as direct experimental localization evidence. The author’s exact source snapshot is unknown.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The C-terminal region is consistent with a YTH-domain m6A RNA reader, while the N-terminus is low-complexity. Transferable knowledge of this protein family makes an RNA-processing compartment such as the nucleoplasm more plausible than the nucleolus, which is especially associated with ribosome biogenesis; the sequence offers no apparent basis for the specialized synapse or egg-chorion choices.",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition and the RNA-reader function provide a credible, though probabilistic, basis for preferring nucleoplasm among these options. YTH proteins can have varied localization, so this inference does not establish the protein’s experimentally observed primary location."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence does not prove an exclusive location, but the offered alternatives do not provide a comparably supported second choice."
  },
  "important_caveats": [
    "The matching GO annotation is computational (IEA:TreeGrafter), not experimental.",
    "The author’s annotation snapshot is unknown, and a primary-compartment prediction need not imply that the protein is found nowhere else."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry annotates this protein (YTH1 from Cryphonectria parasitica, an M6A reader) with GO:0005654 (nucleoplasm) via IEA:TreeGrafter. While the evidence code is computational (Inferred by Electronic Annotation), the functional context from the cited PubMed paper (m6A RNA modification, mRNA stability regulation) is consistent with nuclear localization. YTH domain-containing M6A readers that function in nuclear RNA processing are canonically nucleoplasmic. The annotation is supported but is computational rather than experimentally derived.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C6](#evidence-c6), [H2](#evidence-h2), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable YTH domain (the conserved ~130-residue m6A-binding domain with characteristic aromatic residues and the WQN motif region visible around residues 200-350). From family-level knowledge of YTH domain proteins: (1) Options C (glutamatergic synapse) and D (egg chorion) are immediately eliminable — synapses require animal neurons and chorions are insect/fish egg membranes; neither applies to any eukaryotic intracellular RNA-binding protein, and the sequence lacks signal peptides, transmembrane domains, or chorion-type cysteine-rich motifs. (2) The remaining choice is nucleoplasm vs. nucleolus. YTH domain proteins are well-characterized m6A RNA readers. Nuclear YTH readers (human YTHDC1, yeast ScYTH1, and homologs in other fungi) localize to the nucleoplasm to recognize m6A marks deposited co-transcriptionally on nascent transcripts. Nucleolar localization is associated with ribosome biogenesis factors (fibrillarin, nucleolin, snoRNP components), not YTH readers. The sequence also lacks nucleolar-targeting signals. Thus, recognizing the YTH domain and applying the well-established family-level localization pattern of nuclear m6A readers meaningfully distinguishes nucleoplasm (A) from nucleolus (B).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model trained on general protein biology can recognize the YTH domain from its conserved sequence features, recall that YTH domain proteins are m6A readers, and apply the well-established pattern that nuclear YTH readers (YTHDC1, ScYTH1) reside in the nucleoplasm rather than the nucleolus. Options C and D are trivially excluded by basic cell biology. The A-vs-B distinction is supported by transferable family-level knowledge about YTH domain protein localization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options C and D are clearly inapplicable to an intracellular fungal RNA-binding protein. The YTH domain family localization pattern (nucleoplasm for nuclear readers) provides a clear basis for choosing A over B. No genuine ambiguity exists among the offered choices.


### Important caveats

- The GO annotation is IEA:TreeGrafter (computational inference by homology), not direct experimental localization evidence.
- The organism (Cryphonectria parasitica, a fungus) is not stated in the original input but can be inferred from sequence features or recognized as a eukaryotic protein; fungal YTH homologs (ScYTH1) are well-studied nuclear proteins.
- The YTH domain is recognizable from sequence but requires domain-level knowledge; this is legitimate transferable knowledge from the broader protein family.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable YTH domain (the conserved ~130-residue m6A-binding domain with characteristic aromatic residues and the WQN motif region visible around residues 200-350). From family-level knowledge of YTH domain proteins: (1) Options C (glutamatergic synapse) and D (egg chorion) are immediately eliminable — synapses require animal neurons and chorions are insect/fish egg membranes; neither applies to any eukaryotic intracellular RNA-binding protein, and the sequence lacks signal peptides, transmembrane domains, or chorion-type cysteine-rich motifs. (2) The remaining choice is nucleoplasm vs. nucleolus. YTH domain proteins are well-characterized m6A RNA readers. Nuclear YTH readers (human YTHDC1, yeast ScYTH1, and homologs in other fungi) localize to the nucleoplasm to recognize m6A marks deposited co-transcriptionally on nascent transcripts. Nucleolar localization is associated with ribosome biogenesis factors (fibrillarin, nucleolin, snoRNP components), not YTH readers. The sequence also lacks nucleolar-targeting signals. Thus, recognizing the YTH domain and applying the well-established family-level localization pattern of nuclear m6A readers meaningfully distinguishes nucleoplasm (A) from nucleolus (B).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model trained on general protein biology can recognize the YTH domain from its conserved sequence features, recall that YTH domain proteins are m6A readers, and apply the well-established pattern that nuclear YTH readers (YTHDC1, ScYTH1) reside in the nucleoplasm rather than the nucleolus. Options C and D are trivially excluded by basic cell biology. The A-vs-B distinction is supported by transferable family-level knowledge about YTH domain protein localization."
  },
  "case_id": "GO_cellular_component_0079",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C6",
      "H2",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry annotates this protein (YTH1 from Cryphonectria parasitica, an M6A reader) with GO:0005654 (nucleoplasm) via IEA:TreeGrafter. While the evidence code is computational (Inferred by Electronic Annotation), the functional context from the cited PubMed paper (m6A RNA modification, mRNA stability regulation) is consistent with nuclear localization. YTH domain-containing M6A readers that function in nuclear RNA processing are canonically nucleoplasmic. The annotation is supported but is computational rather than experimentally derived."
  },
  "important_caveats": [
    "The GO annotation is IEA:TreeGrafter (computational inference by homology), not direct experimental localization evidence.",
    "The organism (Cryphonectria parasitica, a fungus) is not stated in the original input but can be inferred from sequence features or recognized as a eukaryotic protein; fungal YTH homologs (ScYTH1) are well-studied nuclear proteins.",
    "The YTH domain is recognizable from sequence but requires domain-level knowledge; this is legitimate transferable knowledge from the broader protein family."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are clearly inapplicable to an intracellular fungal RNA-binding protein. The YTH domain family localization pattern (nucleoplasm for nuclear readers) provides a clear basis for choosing A over B. No genuine ambiguity exists among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0079",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry annotates this protein (YTH1 from Cryphonectria parasitica, an M6A reader) with GO:0005654 (nucleoplasm) via IEA:TreeGrafter. While the evidence code is computational (Inferred by Electronic Annotation), the functional context from the cited PubMed paper (m6A RNA modification, mRNA stability regulation) is consistent with nuclear localization. YTH domain-containing M6A readers that function in nuclear RNA processing are canonically nucleoplasmic. The annotation is supported but is computational rather than experimentally derived.",
    "evidence_ids": ["C5", "H3", "C6", "H2", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable YTH domain (the conserved ~130-residue m6A-binding domain with characteristic aromatic residues and the WQN motif region visible around residues 200-350). From family-level knowledge of YTH domain proteins: (1) Options C (glutamatergic synapse) and D (egg chorion) are immediately eliminable — synapses require animal neurons and chorions are insect/fish egg membranes; neither applies to any eukaryotic intracellular RNA-binding protein, and the sequence lacks signal peptides, transmembrane domains, or chorion-type cysteine-rich motifs. (2) The remaining choice is nucleoplasm vs. nucleolus. YTH domain proteins are well-characterized m6A RNA readers. Nuclear YTH readers (human YTHDC1, yeast ScYTH1, and homologs in other fungi) localize to the nucleoplasm to recognize m6A marks deposited co-transcriptionally on nascent transcripts. Nucleolar localization is associated with ribosome biogenesis factors (fibrillarin, nucleolin, snoRNP components), not YTH readers. The sequence also lacks nucleolar-targeting signals. Thus, recognizing the YTH domain and applying the well-established family-level localization pattern of nuclear m6A readers meaningfully distinguishes nucleoplasm (A) from nucleolus (B).",
    "missing_item_specific_fact": "",
    "reason": "A model trained on general protein biology can recognize the YTH domain from its conserved sequence features, recall that YTH domain proteins are m6A readers, and apply the well-established pattern that nuclear YTH readers (YTHDC1, ScYTH1) reside in the nucleoplasm rather than the nucleolus. Options C and D are trivially excluded by basic cell biology. The A-vs-B distinction is supported by transferable family-level knowledge about YTH domain protein localization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are clearly inapplicable to an intracellular fungal RNA-binding protein. The YTH domain family localization pattern (nucleoplasm for nuclear readers) provides a clear basis for choosing A over B. No genuine ambiguity exists among the offered choices."
  },
  "important_caveats": [
    "The GO annotation is IEA:TreeGrafter (computational inference by homology), not direct experimental localization evidence.",
    "The organism (Cryphonectria parasitica, a fungus) is not stated in the original input but can be inferred from sequence features or recognized as a eukaryotic protein; fungal YTH homologs (ScYTH1) are well-studied nuclear proteins.",
    "The YTH domain is recognizable from sequence but requires domain-level knowledge; this is legitimate transferable knowledge from the broader protein family."
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
  "benchmark_sequence_length": 549,
  "benchmark_sequence_sha256": "9bc16b617f164832ddc73de3c0ad6682c3eeb589f7911dde78dbb48cc5f073c4",
  "current_entry_audit": {
    "entryVersion": 10,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2023-09-13",
    "sequenceVersion": 1
  },
  "current_record_sha256": "db50baf2da9c3578bbb0fd65f314e65acd497ae93fff839d779dccedf824beb7",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 549,
  "current_source_sequence_sha256": "9bc16b617f164832ddc73de3c0ad6682c3eeb589f7911dde78dbb48cc5f073c4",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 9,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A9P4XWM4",
  "selected_historical_entry_version": 9,
  "selected_historical_record_sha256": "c3b8596e9f966d9f9550fbc6c24f4aadbf3af136cfbef9ec39bac6ceeb6c8c94",
  "selected_historical_source_sequence_length": 549,
  "selected_historical_source_sequence_sha256": "9bc16b617f164832ddc73de3c0ad6682c3eeb589f7911dde78dbb48cc5f073c4",
  "selected_historical_version": {
    "accession": "A0A9P4XWM4",
    "database": "Swiss-Prot",
    "entryVersion": 9,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "YTH1_CRYP1",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P4XWM4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A9P4XWM4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:26:16.400481+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "db50baf2da9c3578bbb0fd65f314e65acd497ae93fff839d779dccedf824beb7",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9P4XWM4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P4XWM4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":10,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2023-09-13\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:26:16.400481+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "db50baf2da9c3578bbb0fd65f314e65acd497ae93fff839d779dccedf824beb7",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9P4XWM4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P4XWM4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Sordariomycetidae\",\"Diaporthales\",\"Cryphonectriaceae\",\"Cryphonectria-Endothia species complex\",\"Cryphonectria\"],\"scientificName\":\"Cryphonectria parasitica (strain ATCC 38755 / EP155)\",\"taxonId\":660469}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:26:16.400481+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "db50baf2da9c3578bbb0fd65f314e65acd497ae93fff839d779dccedf824beb7",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9P4XWM4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P4XWM4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39159278\",\"source\":\"PubMed\"}],\"value\":\"M6A reader YTH1\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39159278\",\"source\":\"PubMed\"}],\"value\":\"YTH domain-containing family protein 1\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:26:16.400481+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "db50baf2da9c3578bbb0fd65f314e65acd497ae93fff839d779dccedf824beb7",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9P4XWM4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P4XWM4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005654\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:nucleoplasm\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:TreeGrafter\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/5",
  "retrieved_utc": "2026-11-02T04:26:16.400481+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "db50baf2da9c3578bbb0fd65f314e65acd497ae93fff839d779dccedf824beb7",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9P4XWM4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P4XWM4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhao L.\",\"Wei X.\",\"Chen F.\",\"Yuan L.\",\"Chen B.\",\"Li R.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39159278\"},{\"database\":\"DOI\",\"id\":\"10.1371/journal.ppat.1012476\"}],\"citationType\":\"journal article\",\"firstPage\":\"e1012476\",\"id\":\"39159278\",\"journal\":\"PLoS Pathog.\",\"lastPage\":\"e1012476\",\"publicationDate\":\"2024\",\"title\":\"N6-methyladenosine RNA methyltransferase CpMTA1 mediates CpAphA mRNA stability through a YTHDF1-dependent m6A modification in the chestnut blight fungus.\",\"volume\":\"20\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:26:16.400481+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "db50baf2da9c3578bbb0fd65f314e65acd497ae93fff839d779dccedf824beb7",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9P4XWM4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9P4XWM4?format=txt&versions=9)

```json
{
  "entry_version": 9,
  "evidence_id": "H1",
  "excerpt": "ID   YTH1_CRYP1              Reviewed;         549 AA.\nAC   A0A9P4XWM4;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   13-SEP-2023, sequence version 1.\nDT   28-JAN-2026, entry version 9.\nDE   RecName: Full=YTH domain-containing family protein 1 {ECO:0000303|PubMed:39159278};\nDE   AltName: Full=M6A reader YTH1 {ECO:0000303|PubMed:39159278};\nGN   Name=YTH1 {ECO:0000303|PubMed:39159278}; ORFNames=M406DRAFT_352687;\nOS   Cryphonectria parasitica (strain ATCC 38755 / EP155).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Sordariomycetidae; Diaporthales; Cryphonectriaceae;\nOC   Cryphonectria-Endothia species complex; Cryphonectria.\nOX   NCBI_TaxID=660469;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:18.939090+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c3b8596e9f966d9f9550fbc6c24f4aadbf3af136cfbef9ec39bac6ceeb6c8c94",
  "url": "https://rest.uniprot.org/unisave/A0A9P4XWM4?format=txt&versions=9"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9P4XWM4?format=txt&versions=9)

```json
{
  "entry_version": 9,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=39159278; DOI=10.1371/journal.ppat.1012476;\nRA   Zhao L., Wei X., Chen F., Yuan L., Chen B., Li R.;\nRT   \"N6-methyladenosine RNA methyltransferase CpMTA1 mediates CpAphA mRNA\nRT   stability through a YTHDF1-dependent m6A modification in the chestnut\nRT   blight fungus.\";\nRL   PLoS Pathog. 20:e1012476-e1012476(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:18.939090+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 25-32",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c3b8596e9f966d9f9550fbc6c24f4aadbf3af136cfbef9ec39bac6ceeb6c8c94",
  "url": "https://rest.uniprot.org/unisave/A0A9P4XWM4?format=txt&versions=9"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9P4XWM4?format=txt&versions=9)

```json
{
  "entry_version": 9,
  "evidence_id": "H3",
  "excerpt": "DR   GO; GO:0005654; C:nucleoplasm; IEA:TreeGrafter.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:18.939090+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 53-53",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c3b8596e9f966d9f9550fbc6c24f4aadbf3af136cfbef9ec39bac6ceeb6c8c94",
  "url": "https://rest.uniprot.org/unisave/A0A9P4XWM4?format=txt&versions=9"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0005654\nname: nucleoplasm\nnamespace: cellular_component\ndef: \"That part of the nuclear content other than the chromosomes or the nucleolus.\" [GOC:ma, ISBN:0124325653]\nsubset: goslim_chembl\nsubset: goslim_generic\nsubset: goslim_plant\nxref: NIF_Subcellular:sao661522542\nxref: Wikipedia:Nucleoplasm\nis_a: GO:0110165 ! cellular anatomical structure\nrelationship: part_of GO:0031981 ! nuclear lumen\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005654",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 58222-58234",
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
  "excerpt": "[Term]\nid: GO:0005730\nname: nucleolus\nnamespace: cellular_component\ndef: \"A small, dense body one or more of which are present in the nucleus of eukaryotic cells. It is rich in RNA and protein, is not bounded by a limiting membrane, and is not seen during mitosis. Its prime function is the transcription of the nucleolar DNA into 45S ribosomal-precursor RNA, the processing of this RNA into 5.8S, 18S, and 28S components of ribosomal RNA, and the association of these components with 5S RNA and proteins synthesized outside the nucleolus. This association results in the formation of ribonucleoprotein precursors; these pass into the cytoplasm and mature into the 40S and 60S subunits of the ribosome.\" [ISBN:0198506732]\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_generic\nsubset: goslim_pir\nsubset: goslim_plant\nsubset: goslim_yeast\nxref: NIF_Subcellular:sao1820400233\nxref: Wikipedia:Nucleolus\nis_a: GO:0043232 ! intracellular membraneless organelle\nrelationship: part_of GO:0031981 ! nuclear lumen\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005730",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 58875-58891",
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
  "excerpt": "[Term]\nid: GO:0042600\nname: egg chorion\nnamespace: cellular_component\ndef: \"A protective, noncellular membrane that surrounds the eggs of various animals including insects and fish.\" [GOC:jl, ISBN:0721662544]\ncomment: Note that this term does not refer to the extraembryonic membrane surrounding the embryo of amniote vertebrates as this is an anatomical structure and is therefore not covered by GO.\nsubset: goslim_pir\nis_a: GO:0030312 ! external encapsulating structure\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0042600",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 239034-239042",
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

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 79. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
