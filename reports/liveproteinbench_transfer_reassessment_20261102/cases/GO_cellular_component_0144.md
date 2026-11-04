# GO_cellular_component_0144

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0144.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **B** — other organism cell membrane

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MQLKKQLIVIFFTYFIVVNESEAFFGALFKLATKIIPSLFRKRKGREVMMKRDLEQLFDPYQRNLELDRLLKQLPNY

[Multiple Choices]
A. matrilin complex
B. other organism cell membrane
C. external side of plasma membrane
D. phosphopantothenoylcysteine decarboxylase complex
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

> The sequence-matched historical record assigns the exact GO term “other organism cell membrane” (H6), and also describes the peptide as secreted and associated with a target cell membrane (H4). The exact GO assignment is computationally inferred, not direct experimental localization; the record separately reports experimental secretion.

Citations as saved: [H4](#evidence-h4), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal hydrophobic stretch is consistent with a secretion signal, while the short remainder is rich in basic and hydrophobic residues—a pattern compatible with secreted antimicrobial peptides that interact with other organisms’ membranes. That transferable pattern makes B more plausible than the cartilage-associated matrilin complex (A) or a CoA-biosynthesis enzyme complex (D), and favors a foreign target membrane over the external face of the protein-producing cell’s plasma membrane (C).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and peptide-pattern inference offer a meaningful, though probabilistic, distinction among the choices without needing the exact protein’s recorded annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> B best matches a secreted antimicrobial peptide acting at another organism’s membrane. C refers to the external side of a plasma membrane, not specifically a foreign target membrane.


### Important caveats

- The exact GO annotation for B is computationally inferred; the supplied evidence does not establish B by direct experimental localization.
- The evidence also supports secretion, so “primary” location may depend on how the task interprets a secreted peptide’s association with its target membrane.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic stretch is consistent with a secretion signal, while the short remainder is rich in basic and hydrophobic residues—a pattern compatible with secreted antimicrobial peptides that interact with other organisms’ membranes. That transferable pattern makes B more plausible than the cartilage-associated matrilin complex (A) or a CoA-biosynthesis enzyme complex (D), and favors a foreign target membrane over the external face of the protein-producing cell’s plasma membrane (C).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and peptide-pattern inference offer a meaningful, though probabilistic, distinction among the choices without needing the exact protein’s recorded annotation."
  },
  "case_id": "GO_cellular_component_0144",
  "expected_answer_check": {
    "evidence_ids": [
      "H4",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched historical record assigns the exact GO term “other organism cell membrane” (H6), and also describes the peptide as secreted and associated with a target cell membrane (H4). The exact GO assignment is computationally inferred, not direct experimental localization; the record separately reports experimental secretion."
  },
  "important_caveats": [
    "The exact GO annotation for B is computationally inferred; the supplied evidence does not establish B by direct experimental localization.",
    "The evidence also supports secretion, so “primary” location may depend on how the task interprets a secreted peptide’s association with its target membrane."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B best matches a secreted antimicrobial peptide acting at another organism’s membrane. C refers to the external side of a plasma membrane, not specifically a foreign target membrane."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0144",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched historical record assigns the exact GO term “other organism cell membrane” (H6), and also describes the peptide as secreted and associated with a target cell membrane (H4). The exact GO assignment is computationally inferred, not direct experimental localization; the record separately reports experimental secretion.",
    "evidence_ids": ["H4", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal hydrophobic stretch is consistent with a secretion signal, while the short remainder is rich in basic and hydrophobic residues—a pattern compatible with secreted antimicrobial peptides that interact with other organisms’ membranes. That transferable pattern makes B more plausible than the cartilage-associated matrilin complex (A) or a CoA-biosynthesis enzyme complex (D), and favors a foreign target membrane over the external face of the protein-producing cell’s plasma membrane (C).",
    "missing_item_specific_fact": "",
    "reason": "The sequence and peptide-pattern inference offer a meaningful, though probabilistic, distinction among the choices without needing the exact protein’s recorded annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B best matches a secreted antimicrobial peptide acting at another organism’s membrane. C refers to the external side of a plasma membrane, not specifically a foreign target membrane."
  },
  "important_caveats": [
    "The exact GO annotation for B is computationally inferred; the supplied evidence does not establish B by direct experimental localization.",
    "The evidence also supports secretion, so “primary” location may depend on how the task interprets a secreted peptide’s association with its target membrane."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry annotates this protein (antimicrobial peptide megicin-18) with 'Target cell membrane' (ECO:0000305, curator inference) and assigns GO:0044218 'other organism cell membrane' via IEA:UniProtKB-KW (keyword-based). The experimental evidence (ECO:0000269, PubMed:29896190) confirms secretion and antimicrobial activity against Gram-positive bacteria. The GO term 'other organism cell membrane' is defined as 'The cell membrane of a secondary organism with which the first organism is interacting,' which correctly describes the bacterial target membrane of a scorpion-derived AMP. The annotation is computational/keyword-derived rather than directly experimental for the membrane localization, but the biological reasoning is sound and consistent with the experimental data showing antimicrobial function.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [H4](#evidence-h4), [H6](#evidence-h6), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 77-aa sequence contains a clear N-terminal signal peptide (hydrophobic stretch: LIVIFFTYFIVVNESEAFFGALFKLATKIIPSLFRKRKG) followed by a small amphipathic mature region with alternating hydrophobic (VMMKRD, LELDRLL) and charged (R, K, D, E) residues. These features—signal peptide + small size + amphipathic mature domain—are hallmarks of antimicrobial peptides (AMPs), a well-characterized family (defensins, magainins, melittin, scorpion venom peptides like those from Mesobuthus). General AMP biology establishes that their functional target is bacterial cell membranes, not the producer's own membrane. This distinguishes B ('other organism cell membrane' = bacterial target membrane) from C ('external side of plasma membrane' = the scorpion's own membrane, a transit location). Options A (matrilin complex, a large cartilage ECM protein) and D (phosphopantothenoylcysteine decarboxylase complex, a metabolic enzyme for CoA synthesis) are eliminated by the peptide's small size, signal peptide, and lack of any catalytic or ECM-structural features. The inference from AMP family knowledge to 'target = bacterial membrane = other organism cell membrane' is standard transferable biology.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the signal peptide and amphipathic mature region as characteristic of antimicrobial peptides, apply general AMP biology (target = bacterial membranes), and thereby select 'other organism cell membrane' over 'external side of plasma membrane' (the producer's own membrane). The elimination of A and D is straightforward from size and domain architecture. No target-specific annotation lookup is strictly necessary.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C"
]
```

> Option C ('external side of plasma membrane') could be argued as a transit location during secretion, since the peptide passes through the scorpion's own plasma membrane on its way to the extracellular space. However, the question asks for the 'primary' cellular component, and for a secreted AMP the functional target (bacterial membrane) is conventionally considered the primary location rather than the transit membrane. The GO annotation explicitly uses 'Target cell membrane' rather than the producer's membrane, supporting B over C. The ambiguity is mild and B remains clearly preferred.


### Important caveats

- The GO annotation for 'other organism cell membrane' (GO:0044218) is keyword-based (IEA:UniProtKB-KW), not directly experimental. The experimental evidence confirms secretion and antimicrobial function but the specific membrane-targeting annotation is inferred by curator.
- The 'Target cell membrane' annotation uses ECO:0000305 (inferred by curator), which is weaker evidence than the ECO:0000269 (experimental) evidence for secretion.
- The sequence is from a scorpion venom gland transcriptome study; the mature peptide (residues 24-41) was synthesized and tested in circular dichroism assays, confirming membrane interaction.
- The benchmark sequence matches the full precursor (77 aa) including the signal peptide, not just the mature antimicrobial peptide.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 77-aa sequence contains a clear N-terminal signal peptide (hydrophobic stretch: LIVIFFTYFIVVNESEAFFGALFKLATKIIPSLFRKRKG) followed by a small amphipathic mature region with alternating hydrophobic (VMMKRD, LELDRLL) and charged (R, K, D, E) residues. These features—signal peptide + small size + amphipathic mature domain—are hallmarks of antimicrobial peptides (AMPs), a well-characterized family (defensins, magainins, melittin, scorpion venom peptides like those from Mesobuthus). General AMP biology establishes that their functional target is bacterial cell membranes, not the producer's own membrane. This distinguishes B ('other organism cell membrane' = bacterial target membrane) from C ('external side of plasma membrane' = the scorpion's own membrane, a transit location). Options A (matrilin complex, a large cartilage ECM protein) and D (phosphopantothenoylcysteine decarboxylase complex, a metabolic enzyme for CoA synthesis) are eliminated by the peptide's small size, signal peptide, and lack of any catalytic or ECM-structural features. The inference from AMP family knowledge to 'target = bacterial membrane = other organism cell membrane' is standard transferable biology.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the signal peptide and amphipathic mature region as characteristic of antimicrobial peptides, apply general AMP biology (target = bacterial membranes), and thereby select 'other organism cell membrane' over 'external side of plasma membrane' (the producer's own membrane). The elimination of A and D is straightforward from size and domain architecture. No target-specific annotation lookup is strictly necessary."
  },
  "case_id": "GO_cellular_component_0144",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C8",
      "H4",
      "H6",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry annotates this protein (antimicrobial peptide megicin-18) with 'Target cell membrane' (ECO:0000305, curator inference) and assigns GO:0044218 'other organism cell membrane' via IEA:UniProtKB-KW (keyword-based). The experimental evidence (ECO:0000269, PubMed:29896190) confirms secretion and antimicrobial activity against Gram-positive bacteria. The GO term 'other organism cell membrane' is defined as 'The cell membrane of a secondary organism with which the first organism is interacting,' which correctly describes the bacterial target membrane of a scorpion-derived AMP. The annotation is computational/keyword-derived rather than directly experimental for the membrane localization, but the biological reasoning is sound and consistent with the experimental data showing antimicrobial function."
  },
  "important_caveats": [
    "The GO annotation for 'other organism cell membrane' (GO:0044218) is keyword-based (IEA:UniProtKB-KW), not directly experimental. The experimental evidence confirms secretion and antimicrobial function but the specific membrane-targeting annotation is inferred by curator.",
    "The 'Target cell membrane' annotation uses ECO:0000305 (inferred by curator), which is weaker evidence than the ECO:0000269 (experimental) evidence for secretion.",
    "The sequence is from a scorpion venom gland transcriptome study; the mature peptide (residues 24-41) was synthesized and tested in circular dichroism assays, confirming membrane interaction.",
    "The benchmark sequence matches the full precursor (77 aa) including the signal peptide, not just the mature antimicrobial peptide."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C"
    ],
    "reason": "Option C ('external side of plasma membrane') could be argued as a transit location during secretion, since the peptide passes through the scorpion's own plasma membrane on its way to the extracellular space. However, the question asks for the 'primary' cellular component, and for a secreted AMP the functional target (bacterial membrane) is conventionally considered the primary location rather than the transit membrane. The GO annotation explicitly uses 'Target cell membrane' rather than the producer's membrane, supporting B over C. The ambiguity is mild and B remains clearly preferred."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0144",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry annotates this protein (antimicrobial peptide megicin-18) with 'Target cell membrane' (ECO:0000305, curator inference) and assigns GO:0044218 'other organism cell membrane' via IEA:UniProtKB-KW (keyword-based). The experimental evidence (ECO:0000269, PubMed:29896190) confirms secretion and antimicrobial activity against Gram-positive bacteria. The GO term 'other organism cell membrane' is defined as 'The cell membrane of a secondary organism with which the first organism is interacting,' which correctly describes the bacterial target membrane of a scorpion-derived AMP. The annotation is computational/keyword-derived rather than directly experimental for the membrane localization, but the biological reasoning is sound and consistent with the experimental data showing antimicrobial function.",
    "evidence_ids": ["C5", "C6", "C8", "H4", "H6", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 77-aa sequence contains a clear N-terminal signal peptide (hydrophobic stretch: LIVIFFTYFIVVNESEAFFGALFKLATKIIPSLFRKRKG) followed by a small amphipathic mature region with alternating hydrophobic (VMMKRD, LELDRLL) and charged (R, K, D, E) residues. These features—signal peptide + small size + amphipathic mature domain—are hallmarks of antimicrobial peptides (AMPs), a well-characterized family (defensins, magainins, melittin, scorpion venom peptides like those from Mesobuthus). General AMP biology establishes that their functional target is bacterial cell membranes, not the producer's own membrane. This distinguishes B ('other organism cell membrane' = bacterial target membrane) from C ('external side of plasma membrane' = the scorpion's own membrane, a transit location). Options A (matrilin complex, a large cartilage ECM protein) and D (phosphopantothenoylcysteine decarboxylase complex, a metabolic enzyme for CoA synthesis) are eliminated by the peptide's small size, signal peptide, and lack of any catalytic or ECM-structural features. The inference from AMP family knowledge to 'target = bacterial membrane = other organism cell membrane' is standard transferable biology.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the signal peptide and amphipathic mature region as characteristic of antimicrobial peptides, apply general AMP biology (target = bacterial membranes), and thereby select 'other organism cell membrane' over 'external side of plasma membrane' (the producer's own membrane). The elimination of A and D is straightforward from size and domain architecture. No target-specific annotation lookup is strictly necessary."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C"],
    "reason": "Option C ('external side of plasma membrane') could be argued as a transit location during secretion, since the peptide passes through the scorpion's own plasma membrane on its way to the extracellular space. However, the question asks for the 'primary' cellular component, and for a secreted AMP the functional target (bacterial membrane) is conventionally considered the primary location rather than the transit membrane. The GO annotation explicitly uses 'Target cell membrane' rather than the producer's membrane, supporting B over C. The ambiguity is mild and B remains clearly preferred."
  },
  "important_caveats": [
    "The GO annotation for 'other organism cell membrane' (GO:0044218) is keyword-based (IEA:UniProtKB-KW), not directly experimental. The experimental evidence confirms secretion and antimicrobial function but the specific membrane-targeting annotation is inferred by curator.",
    "The 'Target cell membrane' annotation uses ECO:0000305 (inferred by curator), which is weaker evidence than the ECO:0000269 (experimental) evidence for secretion.",
    "The sequence is from a scorpion venom gland transcriptome study; the mature peptide (residues 24-41) was synthesized and tested in circular dichroism assays, confirming membrane interaction.",
    "The benchmark sequence matches the full precursor (77 aa) including the signal peptide, not just the mature antimicrobial peptide."
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
  "benchmark_sequence_length": 77,
  "benchmark_sequence_sha256": "440eadef25b34c45b7ee569d11735cb43e037d0a2d30350701c97e1c5937c39e",
  "current_entry_audit": {
    "entryVersion": 10,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2014-09-03",
    "sequenceVersion": 1
  },
  "current_record_sha256": "0b37ec804df1d887a8fc20a4b9656eb96110b34fcfa95ba257de4953debbdb01",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 77,
  "current_source_sequence_sha256": "440eadef25b34c45b7ee569d11735cb43e037d0a2d30350701c97e1c5937c39e",
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
  "requested_accession": "A0A059U8Y9",
  "selected_historical_entry_version": 9,
  "selected_historical_record_sha256": "c4fa05fc93cbfcb42e459444d45c0bd60c528143457d820a39266c26a506b617",
  "selected_historical_source_sequence_length": 77,
  "selected_historical_source_sequence_sha256": "440eadef25b34c45b7ee569d11735cb43e037d0a2d30350701c97e1c5937c39e",
  "selected_historical_version": {
    "accession": "A0A059U8Y9",
    "database": "Swiss-Prot",
    "entryVersion": 9,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "NDBM_MESGB",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A059U8Y9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A059U8Y9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:36.328913+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0b37ec804df1d887a8fc20a4b9656eb96110b34fcfa95ba257de4953debbdb01",
  "url": "https://rest.uniprot.org/uniprotkb/A0A059U8Y9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A059U8Y9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":10,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2014-09-03\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:36.328913+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0b37ec804df1d887a8fc20a4b9656eb96110b34fcfa95ba257de4953debbdb01",
  "url": "https://rest.uniprot.org/uniprotkb/A0A059U8Y9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A059U8Y9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Mediterranean checkered scorpion\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Chelicerata\",\"Arachnida\",\"Scorpiones\",\"Buthida\",\"Buthoidea\",\"Buthidae\",\"Mesobuthus\"],\"scientificName\":\"Mesobuthus gibbosus\",\"synonyms\":[\"Buthus gibbosus\"],\"taxonId\":123226}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:36.328913+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0b37ec804df1d887a8fc20a4b9656eb96110b34fcfa95ba257de4953debbdb01",
  "url": "https://rest.uniprot.org/uniprotkb/A0A059U8Y9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A059U8Y9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24746279\",\"source\":\"PubMed\"}],\"value\":\"MgibC1\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24746279\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"29896190\",\"source\":\"PubMed\"}],\"value\":\"Antimicrobial peptide megicin-18\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:36.328913+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0b37ec804df1d887a8fc20a4b9656eb96110b34fcfa95ba257de4953debbdb01",
  "url": "https://rest.uniprot.org/uniprotkb/A0A059U8Y9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A059U8Y9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29896190\",\"source\":\"PubMed\"}],\"id\":\"SL-0243\",\"value\":\"Secreted\"}},{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"id\":\"SL-0451\",\"value\":\"Target cell membrane\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:24:36.328913+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0b37ec804df1d887a8fc20a4b9656eb96110b34fcfa95ba257de4953debbdb01",
  "url": "https://rest.uniprot.org/uniprotkb/A0A059U8Y9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A059U8Y9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29896190\",\"source\":\"PubMed\"}],\"id\":\"GO:0005576\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:extracellular region\"},{\"key\":\"GoEvidenceType\",\"value\":\"EXP:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/3",
  "retrieved_utc": "2026-11-01T06:24:36.328913+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0b37ec804df1d887a8fc20a4b9656eb96110b34fcfa95ba257de4953debbdb01",
  "url": "https://rest.uniprot.org/uniprotkb/A0A059U8Y9.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A059U8Y9.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Diego-Garcia E.\",\"Caliskan F.\",\"Tytgat J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"24746279\"},{\"database\":\"DOI\",\"id\":\"10.1186/1471-2164-15-295\"}],\"citationType\":\"journal article\",\"firstPage\":\"295\",\"id\":\"24746279\",\"journal\":\"BMC Genomics\",\"lastPage\":\"295\",\"publicationDate\":\"2014\",\"title\":\"The Mediterranean scorpion Mesobuthus gibbosus (Scorpiones, Buthidae): transcriptome analysis and organization of the genome encoding chlorotoxin-like peptides.\",\"volume\":\"15\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AHZ63106.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"type\":\"TISSUE\",\"value\":\"Venom gland\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:24:36.328913+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0b37ec804df1d887a8fc20a4b9656eb96110b34fcfa95ba257de4953debbdb01",
  "url": "https://rest.uniprot.org/uniprotkb/A0A059U8Y9.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A059U8Y9.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Liu G.\",\"Yang F.\",\"Li F.\",\"Li Z.\",\"Lang Y.\",\"Shen B.\",\"Wu Y.\",\"Li W.\",\"Harrison P.L.\",\"Strong P.N.\",\"Xie Y.\",\"Miller K.\",\"Cao Z.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"29896190\"},{\"database\":\"DOI\",\"id\":\"10.3389/fmicb.2018.01159\"}],\"citationType\":\"journal article\",\"firstPage\":\"1159\",\"id\":\"29896190\",\"journal\":\"Front. Microbiol.\",\"lastPage\":\"1159\",\"publicationDate\":\"2018\",\"title\":\"Therapeutic potential of a scorpion venom-derived antimicrobial peptide and its homologs against antibiotic-resistant Gram-positive bacteria.\",\"volume\":\"9\"},\"referenceComments\":[{\"type\":\"TISSUE\",\"value\":\"Venom\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"BIOASSAY\",\"SYNTHESIS OF 24-41\",\"CIRCULAR DICHROISM ANALYSIS\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:24:36.328913+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0b37ec804df1d887a8fc20a4b9656eb96110b34fcfa95ba257de4953debbdb01",
  "url": "https://rest.uniprot.org/uniprotkb/A0A059U8Y9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A059U8Y9?format=txt&versions=9)

```json
{
  "entry_version": 9,
  "evidence_id": "H1",
  "excerpt": "ID   NDBM_MESGB              Reviewed;          77 AA.\nAC   A0A059U8Y9;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   03-SEP-2014, sequence version 1.\nDT   28-JAN-2026, entry version 9.\nDE   RecName: Full=Antimicrobial peptide megicin-18 {ECO:0000303|PubMed:24746279, ECO:0000303|PubMed:29896190};\nDE   AltName: Full=MgibC1 {ECO:0000303|PubMed:24746279};\nDE   Flags: Precursor;\nOS   Mesobuthus gibbosus (Mediterranean checkered scorpion) (Buthus gibbosus).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Chelicerata; Arachnida;\nOC   Scorpiones; Buthida; Buthoidea; Buthidae; Mesobuthus.\nOX   NCBI_TaxID=123226;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:15.104172+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c4fa05fc93cbfcb42e459444d45c0bd60c528143457d820a39266c26a506b617",
  "url": "https://rest.uniprot.org/unisave/A0A059U8Y9?format=txt&versions=9"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A059U8Y9?format=txt&versions=9)

```json
{
  "entry_version": 9,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:AHZ63106.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA].\nRC   TISSUE=Venom gland;\nRX   PubMed=24746279; DOI=10.1186/1471-2164-15-295;\nRA   Diego-Garcia E., Caliskan F., Tytgat J.;\nRT   \"The Mediterranean scorpion Mesobuthus gibbosus (Scorpiones, Buthidae):\nRT   transcriptome analysis and organization of the genome encoding chlorotoxin-\nRT   like peptides.\";\nRL   BMC Genomics 15:295-295(2014).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:15.104172+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 13-21",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c4fa05fc93cbfcb42e459444d45c0bd60c528143457d820a39266c26a506b617",
  "url": "https://rest.uniprot.org/unisave/A0A059U8Y9?format=txt&versions=9"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A059U8Y9?format=txt&versions=9)

```json
{
  "entry_version": 9,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, BIOASSAY, SYNTHESIS OF 24-41, AND CIRCULAR DICHROISM ANALYSIS.\nRC   TISSUE=Venom;\nRX   PubMed=29896190; DOI=10.3389/fmicb.2018.01159;\nRA   Liu G., Yang F., Li F., Li Z., Lang Y., Shen B., Wu Y., Li W.,\nRA   Harrison P.L., Strong P.N., Xie Y., Miller K., Cao Z.;\nRT   \"Therapeutic potential of a scorpion venom-derived antimicrobial peptide\nRT   and its homologs against antibiotic-resistant Gram-positive bacteria.\";\nRL   Front. Microbiol. 9:1159-1159(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:15.104172+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 22-30",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c4fa05fc93cbfcb42e459444d45c0bd60c528143457d820a39266c26a506b617",
  "url": "https://rest.uniprot.org/unisave/A0A059U8Y9?format=txt&versions=9"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A059U8Y9?format=txt&versions=9)

```json
{
  "entry_version": 9,
  "evidence_id": "H4",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Secreted {ECO:0000269|PubMed:29896190}. Target\nCC       cell membrane {ECO:0000305}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:15.104172+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 44-45",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c4fa05fc93cbfcb42e459444d45c0bd60c528143457d820a39266c26a506b617",
  "url": "https://rest.uniprot.org/unisave/A0A059U8Y9?format=txt&versions=9"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A059U8Y9?format=txt&versions=9)

```json
{
  "entry_version": 9,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0005576; C:extracellular region; IEA:UniProtKB-SubCell.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:15.104172+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 60-60",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c4fa05fc93cbfcb42e459444d45c0bd60c528143457d820a39266c26a506b617",
  "url": "https://rest.uniprot.org/unisave/A0A059U8Y9?format=txt&versions=9"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A059U8Y9?format=txt&versions=9)

```json
{
  "entry_version": 9,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0044218; C:other organism cell membrane; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:15.104172+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 61-61",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c4fa05fc93cbfcb42e459444d45c0bd60c528143457d820a39266c26a506b617",
  "url": "https://rest.uniprot.org/unisave/A0A059U8Y9?format=txt&versions=9"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0009897\nname: external side of plasma membrane\nnamespace: cellular_component\ndef: \"The leaflet of the plasma membrane that faces the extracellular side of the cell, including any protein embedded in, attached to, or peripherally associated with it.\" [GOC:dos, GOC:tb]\nsynonym: \"external leaflet of plasma membrane\" EXACT [GOC:ab]\nsynonym: \"juxtamembrane\" BROAD []\nsynonym: \"outer surface of cytoplasmic membrane\" EXACT []\nis_a: GO:0098552 ! side of membrane\nrelationship: part_of GO:0005886 ! plasma membrane\nrelationship: part_of GO:0009986 ! cell surface\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0009897",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 100773-100784",
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
  "excerpt": "[Term]\nid: GO:0044218\nname: other organism cell membrane\nnamespace: cellular_component\nalt_id: GO:0044279\ndef: \"The cell membrane of a secondary organism with which the first organism is interacting.\" [GOC:jl]\nsynonym: \"foreign membrane\" RELATED []\nsynonym: \"other organism membrane\" BROAD []\nis_a: GO:0044217 ! other organism part\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0044218",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 255298-255307",
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
  "excerpt": "[Term]\nid: GO:0071513\nname: phosphopantothenoylcysteine decarboxylase complex\nnamespace: cellular_component\ndef: \"A protein complex that catalyzes decarboxylation of 4'-phosphopantothenoylcysteine to yield 4'-phosphopantetheine; this is the third step in the biosynthesis of Coenzyme A. The complex is homotrimeric in many eukaryotes, but is a heterotrimer in Saccharomyces.\" [GOC:jh, PMID:19915539]\ncomment: See also the molecular function term 'acetolactate synthase activity ; GO:0003984'.\nis_a: GO:1902494 ! catalytic complex\nrelationship: part_of GO:0005737 ! cytoplasm\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0071513",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 377848-377856",
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
  "excerpt": "[Term]\nid: GO:0120216\nname: matrilin complex\nnamespace: cellular_component\ndef: \"A cartilage extracellular matrix complex that mediates interactions between major components of the extracellular matrix such as collagens and proteoglycans and contributes to their fibrillar network. Exists as an obligate homotrimer.\" [PMID:10367731, PMID:15075323, PMID:29310791, PMID:9699631]\nsynonym: \"matrilin family complex\" RELATED [GOC:bhm]\nsynonym: \"matrilin-1 complex\" NARROW [GOC:bhm]\nsynonym: \"matrilin-2 complex\" NARROW [GOC:bhm]\nsynonym: \"matrilin-3 complex\" NARROW [GOC:bhm]\nsynonym: \"matrilin-4 complex\" NARROW [GOC:bhm]\nis_a: GO:0140392 ! extracellular protein-containing complex\nrelationship: part_of GO:0140149 ! non-collagenous component of interstitial matrix\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0120216",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 434047-434059",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 144. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
