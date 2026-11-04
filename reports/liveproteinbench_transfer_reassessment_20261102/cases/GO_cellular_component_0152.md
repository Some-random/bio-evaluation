# GO_cellular_component_0152

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0152.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **A** — membrane

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAAFPPGGTFFDTLKRSFTDVPVESGKIATTQFLEACESLTTLFDVLGSTAFKPVKSDMTGNIKKIRDRQLAAPVDSETLQDLVRNELATKKHTATEGLVWLNRALDFTAQALRQNLTNSGEEVSVSFRSAYGNTLSKHHSFMIKPIFSAAMSATPYRKDFYAKLGDDQARVEKELGVWLSSLENIVKILNDFLASKEAKW

[Multiple Choices]
A. membrane
B. chromosome
C. ciliary basal body
D. peroxisomal matrix
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

> The exact sequence-matched UniProt record assigns GO:0016020 (membrane) by IEA:TreeGrafter, supporting the keyed option as a computational annotation. It also assigns cytosol, so the evidence does not establish membrane as the protein’s exclusive or primary location, and the supplied evidence is not experimental localization.

Citations as saved: [C6](#evidence-c6), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is a short, globular-looking protein without an obvious signal peptide or transmembrane segment, which argues against an integral membrane protein. But a soluble lipid-transfer protein can associate with membranes while moving lipids; among these choices, membrane is more credible than chromosome, ciliary basal body, or peroxisomal matrix, which would generally require distinct targeting or localization features.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable sequence and cell-biology patterns provide a probabilistic basis for choosing membrane among the offered alternatives, though they do not establish that membrane is the primary location.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The record also annotates cytosol, but cytosol is not an offered option; the supplied evidence does not make another listed choice comparably defensible.


### Important caveats

- The membrane annotation is computational (IEA:TreeGrafter), not direct experimental evidence.
- The sequence-matched record has both membrane and cytosol annotations, so the wording 'primary' is stronger than the evidence establishes.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a short, globular-looking protein without an obvious signal peptide or transmembrane segment, which argues against an integral membrane protein. But a soluble lipid-transfer protein can associate with membranes while moving lipids; among these choices, membrane is more credible than chromosome, ciliary basal body, or peroxisomal matrix, which would generally require distinct targeting or localization features.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable sequence and cell-biology patterns provide a probabilistic basis for choosing membrane among the offered alternatives, though they do not establish that membrane is the primary location."
  },
  "case_id": "GO_cellular_component_0152",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence-matched UniProt record assigns GO:0016020 (membrane) by IEA:TreeGrafter, supporting the keyed option as a computational annotation. It also assigns cytosol, so the evidence does not establish membrane as the protein’s exclusive or primary location, and the supplied evidence is not experimental localization."
  },
  "important_caveats": [
    "The membrane annotation is computational (IEA:TreeGrafter), not direct experimental evidence.",
    "The sequence-matched record has both membrane and cytosol annotations, so the wording 'primary' is stronger than the evidence establishes."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The record also annotates cytosol, but cytosol is not an offered option; the supplied evidence does not make another listed choice comparably defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0152",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence-matched UniProt record assigns GO:0016020 (membrane) by IEA:TreeGrafter, supporting the keyed option as a computational annotation. It also assigns cytosol, so the evidence does not establish membrane as the protein’s exclusive or primary location, and the supplied evidence is not experimental localization.",
    "evidence_ids": ["C6", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is a short, globular-looking protein without an obvious signal peptide or transmembrane segment, which argues against an integral membrane protein. But a soluble lipid-transfer protein can associate with membranes while moving lipids; among these choices, membrane is more credible than chromosome, ciliary basal body, or peroxisomal matrix, which would generally require distinct targeting or localization features.",
    "missing_item_specific_fact": "",
    "reason": "Transferable sequence and cell-biology patterns provide a probabilistic basis for choosing membrane among the offered alternatives, though they do not establish that membrane is the primary location."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The record also annotates cytosol, but cytosol is not an offered option; the supplied evidence does not make another listed choice comparably defensible."
  },
  "important_caveats": [
    "The membrane annotation is computational (IEA:TreeGrafter), not direct experimental evidence.",
    "The sequence-matched record has both membrane and cytosol annotations, so the wording 'primary' is stronger than the evidence establishes."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A223HDI2) carries GO:0016020 (membrane) as an annotation, albeit via IEA:TreeGrafter (computational prediction). The protein is named 'Glycolipid transfer protein' and the cited reference (PubMed:32003433) discusses 'transport and secretion of liamocins' (glycolipids), which is consistent with membrane association. The entry also carries GO:0005829 (cytosol) via the same evidence type, but cytosol is not among the offered options. The membrane annotation is present and not contradicted by experimental data in the record.

Citations as saved: [C6](#evidence-c6), [H4](#evidence-h4), [C4](#evidence-c4), [C7](#evidence-c7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model can reason through this using family-level and organism-level transferable knowledge. (1) The sequence, while not immediately recognizable by name, contains amphipathic helical segments and a fold reminiscent of lipid-binding/transfer domains; recognizing the GLTP (glycolipid transfer protein) superfamily (which includes START-domain proteins, CERT, OSBP, and fungal lipid-transfer proteins) provides strong prior knowledge that these proteins are membrane-associated, even if peripherally. (2) Chromosome (B) is eliminated: no DNA-binding motifs, no histone-fold, no nuclear localization signal. (3) Ciliary basal body (C) is strongly eliminated: the organism is an ascomycete fungus (Dothideomycetes), which lacks flagellated stages entirely; basal-body proteins are tubulins and centriolar components with very different sequences. (4) Peroxisomal matrix (D) is eliminated: no PTS1 motif (SKL or C-terminal tripeptide variant; the C-terminus ends in ...LASKEAKW) and no PTS2 signal at the N-terminus. (5) Membrane (A) remains as the functionally consistent option for a lipid-transfer protein, and the broad GO:0016020 term encompasses peripheral membrane association. This chain of family recognition plus elimination of clearly incompatible compartments provides a credible, transferable inference.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The combination of GLTP-family knowledge (membrane-associated lipid transfer), fungal biology (ascomycetes lack cilia/flagella, ruling out basal body), absence of peroxisomal targeting signals, and absence of DNA-binding/nuclear features allows a model to meaningfully distinguish the four offered choices without memorizing this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four offered choices, membrane is the only one consistent with GLTP-family function and the organism's biology. Chromosome, ciliary basal body, and peroxisomal matrix are each clearly incompatible with the sequence features and organism type. The UniProt also lists cytosol (IEA:TreeGrafter), but cytosol is not an option, so it does not create ambiguity among the presented alternatives.


### Important caveats

- Both the membrane and cytosol GO annotations in UniProt are IEA:TreeGrafter (computational predictions), not experimental evidence. The membrane assignment is a prediction, not an experimentally validated localization.
- The protein lacks obvious transmembrane helices; 'membrane' here likely refers to peripheral membrane association, which is consistent with the broad GO:0016020 definition.
- The sequence does not contain a canonical START-domain signature that would make family assignment trivially obvious from sequence alone; recognition may require broader pattern-matching or homology-aware reasoning.
- The reviewer-only evidence confirms the sequence matches UniProt A0A223HDI2, but this accession and the protein name 'Glycolipid transfer protein' were not provided to the evaluated model as original input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can reason through this using family-level and organism-level transferable knowledge. (1) The sequence, while not immediately recognizable by name, contains amphipathic helical segments and a fold reminiscent of lipid-binding/transfer domains; recognizing the GLTP (glycolipid transfer protein) superfamily (which includes START-domain proteins, CERT, OSBP, and fungal lipid-transfer proteins) provides strong prior knowledge that these proteins are membrane-associated, even if peripherally. (2) Chromosome (B) is eliminated: no DNA-binding motifs, no histone-fold, no nuclear localization signal. (3) Ciliary basal body (C) is strongly eliminated: the organism is an ascomycete fungus (Dothideomycetes), which lacks flagellated stages entirely; basal-body proteins are tubulins and centriolar components with very different sequences. (4) Peroxisomal matrix (D) is eliminated: no PTS1 motif (SKL or C-terminal tripeptide variant; the C-terminus ends in ...LASKEAKW) and no PTS2 signal at the N-terminus. (5) Membrane (A) remains as the functionally consistent option for a lipid-transfer protein, and the broad GO:0016020 term encompasses peripheral membrane association. This chain of family recognition plus elimination of clearly incompatible compartments provides a credible, transferable inference.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The combination of GLTP-family knowledge (membrane-associated lipid transfer), fungal biology (ascomycetes lack cilia/flagella, ruling out basal body), absence of peroxisomal targeting signals, and absence of DNA-binding/nuclear features allows a model to meaningfully distinguish the four offered choices without memorizing this specific protein's annotation."
  },
  "case_id": "GO_cellular_component_0152",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "H4",
      "C4",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A223HDI2) carries GO:0016020 (membrane) as an annotation, albeit via IEA:TreeGrafter (computational prediction). The protein is named 'Glycolipid transfer protein' and the cited reference (PubMed:32003433) discusses 'transport and secretion of liamocins' (glycolipids), which is consistent with membrane association. The entry also carries GO:0005829 (cytosol) via the same evidence type, but cytosol is not among the offered options. The membrane annotation is present and not contradicted by experimental data in the record."
  },
  "important_caveats": [
    "Both the membrane and cytosol GO annotations in UniProt are IEA:TreeGrafter (computational predictions), not experimental evidence. The membrane assignment is a prediction, not an experimentally validated localization.",
    "The protein lacks obvious transmembrane helices; 'membrane' here likely refers to peripheral membrane association, which is consistent with the broad GO:0016020 definition.",
    "The sequence does not contain a canonical START-domain signature that would make family assignment trivially obvious from sequence alone; recognition may require broader pattern-matching or homology-aware reasoning.",
    "The reviewer-only evidence confirms the sequence matches UniProt A0A223HDI2, but this accession and the protein name 'Glycolipid transfer protein' were not provided to the evaluated model as original input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four offered choices, membrane is the only one consistent with GLTP-family function and the organism's biology. Chromosome, ciliary basal body, and peroxisomal matrix are each clearly incompatible with the sequence features and organism type. The UniProt also lists cytosol (IEA:TreeGrafter), but cytosol is not an option, so it does not create ambiguity among the presented alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0152",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A223HDI2) carries GO:0016020 (membrane) as an annotation, albeit via IEA:TreeGrafter (computational prediction). The protein is named 'Glycolipid transfer protein' and the cited reference (PubMed:32003433) discusses 'transport and secretion of liamocins' (glycolipids), which is consistent with membrane association. The entry also carries GO:0005829 (cytosol) via the same evidence type, but cytosol is not among the offered options. The membrane annotation is present and not contradicted by experimental data in the record.",
    "evidence_ids": ["C6", "H4", "C4", "C7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model can reason through this using family-level and organism-level transferable knowledge. (1) The sequence, while not immediately recognizable by name, contains amphipathic helical segments and a fold reminiscent of lipid-binding/transfer domains; recognizing the GLTP (glycolipid transfer protein) superfamily (which includes START-domain proteins, CERT, OSBP, and fungal lipid-transfer proteins) provides strong prior knowledge that these proteins are membrane-associated, even if peripherally. (2) Chromosome (B) is eliminated: no DNA-binding motifs, no histone-fold, no nuclear localization signal. (3) Ciliary basal body (C) is strongly eliminated: the organism is an ascomycete fungus (Dothideomycetes), which lacks flagellated stages entirely; basal-body proteins are tubulins and centriolar components with very different sequences. (4) Peroxisomal matrix (D) is eliminated: no PTS1 motif (SKL or C-terminal tripeptide variant; the C-terminus ends in ...LASKEAKW) and no PTS2 signal at the N-terminus. (5) Membrane (A) remains as the functionally consistent option for a lipid-transfer protein, and the broad GO:0016020 term encompasses peripheral membrane association. This chain of family recognition plus elimination of clearly incompatible compartments provides a credible, transferable inference.",
    "missing_item_specific_fact": "",
    "reason": "The combination of GLTP-family knowledge (membrane-associated lipid transfer), fungal biology (ascomycetes lack cilia/flagella, ruling out basal body), absence of peroxisomal targeting signals, and absence of DNA-binding/nuclear features allows a model to meaningfully distinguish the four offered choices without memorizing this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four offered choices, membrane is the only one consistent with GLTP-family function and the organism's biology. Chromosome, ciliary basal body, and peroxisomal matrix are each clearly incompatible with the sequence features and organism type. The UniProt also lists cytosol (IEA:TreeGrafter), but cytosol is not an option, so it does not create ambiguity among the presented alternatives."
  },
  "important_caveats": [
    "Both the membrane and cytosol GO annotations in UniProt are IEA:TreeGrafter (computational predictions), not experimental evidence. The membrane assignment is a prediction, not an experimentally validated localization.",
    "The protein lacks obvious transmembrane helices; 'membrane' here likely refers to peripheral membrane association, which is consistent with the broad GO:0016020 definition.",
    "The sequence does not contain a canonical START-domain signature that would make family assignment trivially obvious from sequence alone; recognition may require broader pattern-matching or homology-aware reasoning.",
    "The reviewer-only evidence confirms the sequence matches UniProt A0A223HDI2, but this accession and the protein name 'Glycolipid transfer protein' were not provided to the evaluated model as original input."
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
  "benchmark_sequence_length": 201,
  "benchmark_sequence_sha256": "b1d76fee95e529dc62a98dbe71ec47c7f5e598d657362e420089f949181248da",
  "current_entry_audit": {
    "entryVersion": 16,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-01-28",
    "lastSequenceUpdateDate": "2017-10-25",
    "sequenceVersion": 1
  },
  "current_record_sha256": "cd27114264ad6d95907c9d0ca40d7087fc933a811ae632a7d10b4a29dd9c86d4",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 201,
  "current_source_sequence_sha256": "b1d76fee95e529dc62a98dbe71ec47c7f5e598d657362e420089f949181248da",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 16,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A223HDI2",
  "selected_historical_entry_version": 16,
  "selected_historical_record_sha256": "5250846a5879910a1cb487027efe195ee80b515fd2492b5e68903453b74cc6bb",
  "selected_historical_source_sequence_length": 201,
  "selected_historical_source_sequence_sha256": "b1d76fee95e529dc62a98dbe71ec47c7f5e598d657362e420089f949181248da",
  "selected_historical_version": {
    "accession": "A0A223HDI2",
    "database": "Swiss-Prot",
    "entryVersion": 16,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "GLTP_AURME",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI2.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A223HDI2\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:44.060643+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "cd27114264ad6d95907c9d0ca40d7087fc933a811ae632a7d10b4a29dd9c86d4",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDI2.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI2.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":16,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-01-28\",\"lastSequenceUpdateDate\":\"2017-10-25\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:44.060643+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "cd27114264ad6d95907c9d0ca40d7087fc933a811ae632a7d10b4a29dd9c86d4",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDI2.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI2.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Aureobasidium pullulans var. melanogenum\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Dothideomycetes\",\"Dothideomycetidae\",\"Dothideales\",\"Saccotheciaceae\",\"Aureobasidium\"],\"scientificName\":\"Aureobasidium melanogenum\",\"taxonId\":46634}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:44.060643+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "cd27114264ad6d95907c9d0ca40d7087fc933a811ae632a7d10b4a29dd9c86d4",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDI2.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI2.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32003433\",\"source\":\"PubMed\"}],\"value\":\"Glycolipid transfer protein\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:44.060643+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "cd27114264ad6d95907c9d0ca40d7087fc933a811ae632a7d10b4a29dd9c86d4",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDI2.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI2.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005829\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:cytosol\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:TreeGrafter\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/3",
  "retrieved_utc": "2026-11-02T04:24:44.060643+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "cd27114264ad6d95907c9d0ca40d7087fc933a811ae632a7d10b4a29dd9c86d4",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDI2.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI2.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0016020\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:TreeGrafter\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/4",
  "retrieved_utc": "2026-11-02T04:24:44.060643+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "cd27114264ad6d95907c9d0ca40d7087fc933a811ae632a7d10b4a29dd9c86d4",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDI2.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI2.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Xue S.J.\",\"Liu G.L.\",\"Chi Z.\",\"Gao Z.C.\",\"Hu Z.\",\"Chi Z.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"32003433\"},{\"database\":\"DOI\",\"id\":\"10.1042/bcj20190922\"}],\"citationType\":\"journal article\",\"firstPage\":\"887\",\"id\":\"32003433\",\"journal\":\"Biochem. J.\",\"lastPage\":\"903\",\"publicationDate\":\"2020\",\"title\":\"Genetic evidences for the core biosynthesis pathway, regulation, transport and secretion of liamocins in yeast-like fungal cells.\",\"volume\":\"477\"},\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:24:44.060643+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "cd27114264ad6d95907c9d0ca40d7087fc933a811ae632a7d10b4a29dd9c86d4",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDI2.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDI2?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H1",
  "excerpt": "ID   GLTP_AURME              Reviewed;         201 AA.\nAC   A0A223HDI2;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   25-OCT-2017, sequence version 1.\nDT   28-JAN-2026, entry version 16.\nDE   RecName: Full=Glycolipid transfer protein {ECO:0000303|PubMed:32003433};\nOS   Aureobasidium melanogenum (Aureobasidium pullulans var. melanogenum).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Dothideomycetes;\nOC   Dothideomycetidae; Dothideales; Saccotheciaceae; Aureobasidium.\nOX   NCBI_TaxID=46634;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:46.537205+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-10",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5250846a5879910a1cb487027efe195ee80b515fd2492b5e68903453b74cc6bb",
  "url": "https://rest.uniprot.org/unisave/A0A223HDI2?format=txt&versions=16"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDI2?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H2",
  "excerpt": "RN   [4]\nRP   FUNCTION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=32003433; DOI=10.1042/bcj20190922;\nRA   Xue S.J., Liu G.L., Chi Z., Gao Z.C., Hu Z., Chi Z.M.;\nRT   \"Genetic evidences for the core biosynthesis pathway, regulation, transport\nRT   and secretion of liamocins in yeast-like fungal cells.\";\nRL   Biochem. J. 477:887-903(2020).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:46.537205+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 29-35",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5250846a5879910a1cb487027efe195ee80b515fd2492b5e68903453b74cc6bb",
  "url": "https://rest.uniprot.org/unisave/A0A223HDI2?format=txt&versions=16"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDI2?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H3",
  "excerpt": "DR   GO; GO:0005829; C:cytosol; IEA:TreeGrafter.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:46.537205+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 69-69",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5250846a5879910a1cb487027efe195ee80b515fd2492b5e68903453b74cc6bb",
  "url": "https://rest.uniprot.org/unisave/A0A223HDI2?format=txt&versions=16"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDI2?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0016020; C:membrane; IEA:TreeGrafter.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:46.537205+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 70-70",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5250846a5879910a1cb487027efe195ee80b515fd2492b5e68903453b74cc6bb",
  "url": "https://rest.uniprot.org/unisave/A0A223HDI2?format=txt&versions=16"
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
  "excerpt": "[Term]\nid: GO:0005782\nname: peroxisomal matrix\nnamespace: cellular_component\nalt_id: GO:0031909\ndef: \"The volume contained within the membranes of a peroxisome; in many cells the matrix contains a crystalloid core largely composed of urate oxidase.\" [GOC:curators, ISBN:0815316194]\nsynonym: \"peroxisomal lumen\" EXACT []\nis_a: GO:0031907 ! microbody lumen\nrelationship: part_of GO:0005777 ! peroxisome\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005782",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 59440-59449",
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
  "excerpt": "[Term]\nid: GO:0016020\nname: membrane\nnamespace: cellular_component\nalt_id: GO:0016021\nalt_id: GO:0098589\nalt_id: GO:0098805\ndef: \"A lipid bilayer along with all the proteins and protein complexes embedded in it and attached to it.\" [GOC:dos, GOC:mah, ISBN:0815316194]\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_flybase_ribbon\nsubset: goslim_metagenomics\nsubset: goslim_pir\nsubset: goslim_plant\nsubset: goslim_yeast\nsynonym: \"integral component of membrane\" NARROW []\nsynonym: \"integral to membrane\" NARROW []\nsynonym: \"membrane region\" NARROW []\nsynonym: \"region of membrane\" NARROW []\nsynonym: \"transmembrane\" RELATED [GOC:mah]\nsynonym: \"whole membrane\" NARROW []\nxref: Wikipedia:Biological_membrane\nxref: Wikipedia:Transmembrane_protein\nis_a: GO:0110165 ! cellular anatomical structure\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0016020",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 122626-122650",
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
  "excerpt": "[Term]\nid: GO:0036064\nname: ciliary basal body\nnamespace: cellular_component\nalt_id: GO:0005932\ndef: \"A membrane-tethered, short cylindrical array of microtubules and associated proteins found at the base of a eukaryotic cilium (also called flagellum) that is similar in structure to a centriole and derives from it. The cilium basal body is the site of assembly and remodeling of the cilium and serves as a nucleation site for axoneme growth. As well as anchoring the cilium, it is thought to provide a selective gateway regulating the entry of ciliary proteins and vesicles by intraflagellar transport.\" [GOC:cilia, GOC:clt, PMID:21750193]\ncomment: In most eukaryotic cells, 'ciliary basal body' (GO:0036064) and 'centriole' (GO:0005814) represent a common entity that cycles through its function in cell division, then ciliogenesis, then cell division again. However, these structures are modified extensively as they transition into each other, and may contain different proteins, specific to each component.\nsynonym: \"basal body\" BROAD []\nsynonym: \"cilial basal body\" EXACT []\nsynonym: \"cilium basal body\" EXACT [GOC:bf]\nsynonym: \"kinetosome\" EXACT [PMID:11125699]\nsynonym: \"microtubule basal body\" EXACT []\nxref: NIF_Subcellular:sao11978067\nis_a: GO:0005815 ! microtubule organizing center\nrelationship: part_of GO:0005929 ! cilium\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0036064",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 224054-224069",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 152. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
