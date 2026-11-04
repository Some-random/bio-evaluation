# GO_cellular_component_0188

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0188.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **B** — microvillus membrane

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAQWWLILLGLWTVLPSLAGGKLLNVCMNSKHHKQEPGPEDKLYFECMPWKDNACCTRDTSWEAHLDEPLLFNFSMTHCGLLTPLCHKHFIQAICFYECSPNLGPWIQPVVPNRQEEQRLWDVPLCLEDCEEWWKDCRTSHTCKADWLHGWVWDQGKNGCPAHAPCLPFSDYFPTPADLCEKIWNNTFKASPERRNSGRCLQKWFEPTHGNPNVEVALHFAGSASAPQLSYSITAFSLCLLLHA

[Multiple Choices]
A. kinetoplast
B. microvillus membrane
C. vitelline envelope
D. SAGA complex
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

> The matched-sequence UniProt record annotates the protein at the microvillus membrane and describes it as GPI-anchored at oolemma microvilli. However, that specific localization is supported by similarity-based evidence, while the supplied experimental evidence establishes plasma-membrane localization, not microvillus localization directly.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an N-terminal hydrophobic signal peptide and a C-terminal hydrophobic segment, consistent with a secretory-pathway protein carrying a GPI-anchor signal. Transferable knowledge of GPI-anchored, folate-receptor-like surface proteins favors a cell-surface membrane location over a kinetoplast, a nuclear SAGA complex, or an egg coat. Among the choices, the microvillus membrane is the membrane-associated option; the sequence alone does not establish the precise microvillar localization.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A credible sequence-based inference favors B among these alternatives, though the microvillus-level specificity is not independently demonstrated by the sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The hydrophobic termini favor a membrane-tethered protein over the other offered structures; no alternative is comparably supported by the provided sequence.


### Important caveats

- The specific microvillus localization in the matched record is similarity-based; experimental evidence cited there supports plasma-membrane localization.
- The evaluated input did not include organism identity or protein name, and target-specific record knowledge is not counted as transferable inference.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an N-terminal hydrophobic signal peptide and a C-terminal hydrophobic segment, consistent with a secretory-pathway protein carrying a GPI-anchor signal. Transferable knowledge of GPI-anchored, folate-receptor-like surface proteins favors a cell-surface membrane location over a kinetoplast, a nuclear SAGA complex, or an egg coat. Among the choices, the microvillus membrane is the membrane-associated option; the sequence alone does not establish the precise microvillar localization.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A credible sequence-based inference favors B among these alternatives, though the microvillus-level specificity is not independently demonstrated by the sequence."
  },
  "case_id": "GO_cellular_component_0188",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The matched-sequence UniProt record annotates the protein at the microvillus membrane and describes it as GPI-anchored at oolemma microvilli. However, that specific localization is supported by similarity-based evidence, while the supplied experimental evidence establishes plasma-membrane localization, not microvillus localization directly."
  },
  "important_caveats": [
    "The specific microvillus localization in the matched record is similarity-based; experimental evidence cited there supports plasma-membrane localization.",
    "The evaluated input did not include organism identity or protein name, and target-specific record knowledge is not counted as transferable inference."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The hydrophobic termini favor a membrane-tethered protein over the other offered structures; no alternative is comparably supported by the provided sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0188",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched-sequence UniProt record annotates the protein at the microvillus membrane and describes it as GPI-anchored at oolemma microvilli. However, that specific localization is supported by similarity-based evidence, while the supplied experimental evidence establishes plasma-membrane localization, not microvillus localization directly.",
    "evidence_ids": ["C5", "C6", "C7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an N-terminal hydrophobic signal peptide and a C-terminal hydrophobic segment, consistent with a secretory-pathway protein carrying a GPI-anchor signal. Transferable knowledge of GPI-anchored, folate-receptor-like surface proteins favors a cell-surface membrane location over a kinetoplast, a nuclear SAGA complex, or an egg coat. Among the choices, the microvillus membrane is the membrane-associated option; the sequence alone does not establish the precise microvillar localization.",
    "missing_item_specific_fact": "",
    "reason": "A credible sequence-based inference favors B among these alternatives, though the microvillus-level specificity is not independently demonstrated by the sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The hydrophobic termini favor a membrane-tethered protein over the other offered structures; no alternative is comparably supported by the provided sequence."
  },
  "important_caveats": [
    "The specific microvillus localization in the matched record is similarity-based; experimental evidence cited there supports plasma-membrane localization.",
    "The evaluated input did not include organism identity or protein name, and target-specific record knowledge is not counted as transferable inference."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry F1M928 (JUNO, rat) carries a GO annotation for microvillus membrane (GO:0031528) with IEA:UniProtKB-SubCell evidence, and the subcellular location comment states 'Cell projection, microvillus membrane; Lipid-anchor, GPI-anchor' with the note 'GPI-anchored at the oolemma microvilli.' The annotation is computational (IEA, transferred from mouse JUNO Q9EQF4 and A6ND01), while the direct experimental evidence (IDA, PubMed:37951137) supports the broader 'plasma membrane' (GO:0005886). Nevertheless, microvillus membrane is a valid and recorded GO cellular component annotation for this protein, so the author key is supported by the database record.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence shows (1) an N-terminal hydrophobic signal peptide (MAQWWLILLGLWTVLPSLA) indicating secretory/membrane targeting, and (2) a C-terminal hydrophobic tail (…FAGSASAPQLSYSITAFSLCLLLHA) characteristic of a GPI-anchor signal. These features identify the protein as a GPI-anchored membrane protein. Among the four choices: D (SAGA complex) is a nuclear transcription coactivator complex—completely incompatible with a signal-peptide/GPI-anchored protein. A (kinetoplast) is a mitochondrial DNA substructure found exclusively in kinetoplastid parasites (Trypanosoma, Leishmania); a protein with a vertebrate-type signal peptide and GPI-anchor signal would not localize there. C (vitelline envelope) is an extracellular glycoprotein egg coat; a GPI-anchored membrane protein is not an extracellular coat component. B (microvillus membrane) is a sub-compartment of the plasma membrane, and GPI-anchored proteins—particularly members of the folate receptor family, which this sequence resembles by its cysteine-rich pattern and overall ~244-aa architecture—are well-known to concentrate on microvilli (e.g., folate receptor alpha on intestinal/kidney microvilli). Thus, transferable knowledge about signal peptides, GPI-anchor signals, the folate receptor family, and the nature of the four GO compartments meaningfully distinguishes B from the other three.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the signal peptide and GPI-anchor signal from the sequence, eliminate the nuclear complex (D), the parasite-specific kinetoplast (A), and the extracellular egg coat (C), and arrive at the membrane microvillus location (B) using family-level knowledge of folate receptors and GPI-anchored protein biology without needing to recall this specific protein's database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent fundamentally different cellular compartments (parasite mitochondrial substructure, membrane microvillus, extracellular egg coat, nuclear complex). The signal peptide and GPI-anchor signal unambiguously point to a membrane protein, leaving only B as a viable membrane location. No other option is defensible given these sequence features.


### Important caveats

- The microvillus membrane GO annotation carries only IEA (Inferred from Electronic Annotation) evidence, transferred from the mouse JUNO ortholog. The direct experimental evidence (IDA) supports the broader 'plasma membrane' (GO:0005886). The more specific microvillus assignment is computational, not experimentally confirmed for the rat protein.
- The organism (Rattus norvegicus) is not stated in the original input; the model must infer a vertebrate/mammalian origin from the protein architecture, which is reasonable but not explicit.
- The folate receptor family resemblance (cysteine pattern, ~244 aa, GPI anchor) is a key transferable cue; if the model does not recognize this family, the reasoning path is slightly less direct but the signal peptide + GPI anchor still eliminates three of four choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence shows (1) an N-terminal hydrophobic signal peptide (MAQWWLILLGLWTVLPSLA) indicating secretory/membrane targeting, and (2) a C-terminal hydrophobic tail (…FAGSASAPQLSYSITAFSLCLLLHA) characteristic of a GPI-anchor signal. These features identify the protein as a GPI-anchored membrane protein. Among the four choices: D (SAGA complex) is a nuclear transcription coactivator complex—completely incompatible with a signal-peptide/GPI-anchored protein. A (kinetoplast) is a mitochondrial DNA substructure found exclusively in kinetoplastid parasites (Trypanosoma, Leishmania); a protein with a vertebrate-type signal peptide and GPI-anchor signal would not localize there. C (vitelline envelope) is an extracellular glycoprotein egg coat; a GPI-anchored membrane protein is not an extracellular coat component. B (microvillus membrane) is a sub-compartment of the plasma membrane, and GPI-anchored proteins—particularly members of the folate receptor family, which this sequence resembles by its cysteine-rich pattern and overall ~244-aa architecture—are well-known to concentrate on microvilli (e.g., folate receptor alpha on intestinal/kidney microvilli). Thus, transferable knowledge about signal peptides, GPI-anchor signals, the folate receptor family, and the nature of the four GO compartments meaningfully distinguishes B from the other three.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the signal peptide and GPI-anchor signal from the sequence, eliminate the nuclear complex (D), the parasite-specific kinetoplast (A), and the extracellular egg coat (C), and arrive at the membrane microvillus location (B) using family-level knowledge of folate receptors and GPI-anchored protein biology without needing to recall this specific protein's database record."
  },
  "case_id": "GO_cellular_component_0188",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry F1M928 (JUNO, rat) carries a GO annotation for microvillus membrane (GO:0031528) with IEA:UniProtKB-SubCell evidence, and the subcellular location comment states 'Cell projection, microvillus membrane; Lipid-anchor, GPI-anchor' with the note 'GPI-anchored at the oolemma microvilli.' The annotation is computational (IEA, transferred from mouse JUNO Q9EQF4 and A6ND01), while the direct experimental evidence (IDA, PubMed:37951137) supports the broader 'plasma membrane' (GO:0005886). Nevertheless, microvillus membrane is a valid and recorded GO cellular component annotation for this protein, so the author key is supported by the database record."
  },
  "important_caveats": [
    "The microvillus membrane GO annotation carries only IEA (Inferred from Electronic Annotation) evidence, transferred from the mouse JUNO ortholog. The direct experimental evidence (IDA) supports the broader 'plasma membrane' (GO:0005886). The more specific microvillus assignment is computational, not experimentally confirmed for the rat protein.",
    "The organism (Rattus norvegicus) is not stated in the original input; the model must infer a vertebrate/mammalian origin from the protein architecture, which is reasonable but not explicit.",
    "The folate receptor family resemblance (cysteine pattern, ~244 aa, GPI anchor) is a key transferable cue; if the model does not recognize this family, the reasoning path is slightly less direct but the signal peptide + GPI anchor still eliminates three of four choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent fundamentally different cellular compartments (parasite mitochondrial substructure, membrane microvillus, extracellular egg coat, nuclear complex). The signal peptide and GPI-anchor signal unambiguously point to a membrane protein, leaving only B as a viable membrane location. No other option is defensible given these sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0188",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry F1M928 (JUNO, rat) carries a GO annotation for microvillus membrane (GO:0031528) with IEA:UniProtKB-SubCell evidence, and the subcellular location comment states 'Cell projection, microvillus membrane; Lipid-anchor, GPI-anchor' with the note 'GPI-anchored at the oolemma microvilli.' The annotation is computational (IEA, transferred from mouse JUNO Q9EQF4 and A6ND01), while the direct experimental evidence (IDA, PubMed:37951137) supports the broader 'plasma membrane' (GO:0005886). Nevertheless, microvillus membrane is a valid and recorded GO cellular component annotation for this protein, so the author key is supported by the database record.",
    "evidence_ids": ["C5", "C6", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence shows (1) an N-terminal hydrophobic signal peptide (MAQWWLILLGLWTVLPSLA) indicating secretory/membrane targeting, and (2) a C-terminal hydrophobic tail (…FAGSASAPQLSYSITAFSLCLLLHA) characteristic of a GPI-anchor signal. These features identify the protein as a GPI-anchored membrane protein. Among the four choices: D (SAGA complex) is a nuclear transcription coactivator complex—completely incompatible with a signal-peptide/GPI-anchored protein. A (kinetoplast) is a mitochondrial DNA substructure found exclusively in kinetoplastid parasites (Trypanosoma, Leishmania); a protein with a vertebrate-type signal peptide and GPI-anchor signal would not localize there. C (vitelline envelope) is an extracellular glycoprotein egg coat; a GPI-anchored membrane protein is not an extracellular coat component. B (microvillus membrane) is a sub-compartment of the plasma membrane, and GPI-anchored proteins—particularly members of the folate receptor family, which this sequence resembles by its cysteine-rich pattern and overall ~244-aa architecture—are well-known to concentrate on microvilli (e.g., folate receptor alpha on intestinal/kidney microvilli). Thus, transferable knowledge about signal peptides, GPI-anchor signals, the folate receptor family, and the nature of the four GO compartments meaningfully distinguishes B from the other three.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the signal peptide and GPI-anchor signal from the sequence, eliminate the nuclear complex (D), the parasite-specific kinetoplast (A), and the extracellular egg coat (C), and arrive at the membrane microvillus location (B) using family-level knowledge of folate receptors and GPI-anchored protein biology without needing to recall this specific protein's database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent fundamentally different cellular compartments (parasite mitochondrial substructure, membrane microvillus, extracellular egg coat, nuclear complex). The signal peptide and GPI-anchor signal unambiguously point to a membrane protein, leaving only B as a viable membrane location. No other option is defensible given these sequence features."
  },
  "important_caveats": [
    "The microvillus membrane GO annotation carries only IEA (Inferred from Electronic Annotation) evidence, transferred from the mouse JUNO ortholog. The direct experimental evidence (IDA) supports the broader 'plasma membrane' (GO:0005886). The more specific microvillus assignment is computational, not experimentally confirmed for the rat protein.",
    "The organism (Rattus norvegicus) is not stated in the original input; the model must infer a vertebrate/mammalian origin from the protein architecture, which is reasonable but not explicit.",
    "The folate receptor family resemblance (cysteine pattern, ~244 aa, GPI anchor) is a key transferable cue; if the model does not recognize this family, the reasoning path is slightly less direct but the signal peptide + GPI anchor still eliminates three of four choices."
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
  "benchmark_sequence_length": 244,
  "benchmark_sequence_sha256": "491b1fe0d98325db3c5cc1549614442f2b71b04d8bb6234162026d81cf32a7f4",
  "current_entry_audit": {
    "entryVersion": 94,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2013-04-03",
    "sequenceVersion": 2
  },
  "current_record_sha256": "b56a36704099444e686e704fe8993d737b0fe848fed00c7247b8f75bf147a97d",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 244,
  "current_source_sequence_sha256": "491b1fe0d98325db3c5cc1549614442f2b71b04d8bb6234162026d81cf32a7f4",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 92,
      "exact_sequence_comparison": "matched",
      "sequence_version": 2
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "F1M928",
  "selected_historical_entry_version": 92,
  "selected_historical_record_sha256": "57bdb51b29963fdcfb395f44171ffb2ca0c93e66ec625c64278875faf6b4aa52",
  "selected_historical_source_sequence_length": 244,
  "selected_historical_source_sequence_sha256": "491b1fe0d98325db3c5cc1549614442f2b71b04d8bb6234162026d81cf32a7f4",
  "selected_historical_version": {
    "accession": "F1M928",
    "database": "Swiss-Prot",
    "entryVersion": 92,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "JUNO_RAT",
    "sequenceVersion": 2
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/F1M928.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"F1M928\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:28:11.745036+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b56a36704099444e686e704fe8993d737b0fe848fed00c7247b8f75bf147a97d",
  "url": "https://rest.uniprot.org/uniprotkb/F1M928.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/F1M928.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":94,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2013-04-03\",\"sequenceVersion\":2}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:28:11.745036+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b56a36704099444e686e704fe8993d737b0fe848fed00c7247b8f75bf147a97d",
  "url": "https://rest.uniprot.org/uniprotkb/F1M928.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/F1M928.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Rat\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Euteleostomi\",\"Mammalia\",\"Eutheria\",\"Euarchontoglires\",\"Glires\",\"Rodentia\",\"Myomorpha\",\"Muroidea\",\"Muridae\",\"Murinae\",\"Rattus\"],\"scientificName\":\"Rattus norvegicus\",\"taxonId\":10116}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:28:11.745036+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b56a36704099444e686e704fe8993d737b0fe848fed00c7247b8f75bf147a97d",
  "url": "https://rest.uniprot.org/uniprotkb/F1M928.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/F1M928.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"value\":\"Folate receptor 4\"}},{\"fullName\":{\"value\":\"Folate receptor delta\"},\"shortNames\":[{\"value\":\"FR-delta\"}]},{\"fullName\":{\"value\":\"IZUMO1 receptor protein JUNO\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"fullName\":{\"value\":\"Sperm-egg fusion protein Juno\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:28:11.745036+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b56a36704099444e686e704fe8993d737b0fe848fed00c7247b8f75bf147a97d",
  "url": "https://rest.uniprot.org/uniprotkb/F1M928.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/F1M928.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9EQF4\",\"source\":\"UniProtKB\"}],\"value\":\"GPI-anchored at the oolemma microvilli\"}]},\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37951137\",\"source\":\"PubMed\"}],\"id\":\"SL-0039\",\"value\":\"Cell membrane\"},\"topology\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9EQF4\",\"source\":\"UniProtKB\"}],\"id\":\"SL-9902\",\"value\":\"Lipid-anchor, GPI-anchor\"}},{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A6ND01\",\"source\":\"UniProtKB\"}],\"id\":\"SL-0294\",\"value\":\"Cell projection, microvillus membrane\"},\"topology\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9EQF4\",\"source\":\"UniProtKB\"}],\"id\":\"SL-9902\",\"value\":\"Lipid-anchor, GPI-anchor\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:28:11.745036+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b56a36704099444e686e704fe8993d737b0fe848fed00c7247b8f75bf147a97d",
  "url": "https://rest.uniprot.org/uniprotkb/F1M928.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/F1M928.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0031528\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:microvillus membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-SubCell\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/30",
  "retrieved_utc": "2026-11-02T04:28:11.745036+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b56a36704099444e686e704fe8993d737b0fe848fed00c7247b8f75bf147a97d",
  "url": "https://rest.uniprot.org/uniprotkb/F1M928.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/F1M928.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"37951137\",\"source\":\"PubMed\"}],\"id\":\"GO:0005886\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:plasma membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/31",
  "retrieved_utc": "2026-11-02T04:28:11.745036+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b56a36704099444e686e704fe8993d737b0fe848fed00c7247b8f75bf147a97d",
  "url": "https://rest.uniprot.org/uniprotkb/F1M928.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/F1M928.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Lai X.\",\"Liu R.\",\"Li M.\",\"Fan Y.\",\"Li H.\",\"Han G.\",\"Guo R.\",\"Ma H.\",\"Su H.\",\"Xing W.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"37951137\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.theriogenology.2023.10.031\"}],\"citationType\":\"journal article\",\"firstPage\":\"286\",\"id\":\"37951137\",\"journal\":\"Theriogenology\",\"lastPage\":\"297\",\"publicationDate\":\"2024\",\"title\":\"Participation of WD repeat-containing protein 54 (WDR54) in rat sperm-oocyte fusion through interaction with both IZUMO1 and JUNO.\",\"volume\":\"214\"},\"referenceNumber\":4,\"referencePositions\":[\"INTERACTION WITH WDR54\",\"SUBCELLULAR LOCATION\",\"TISSUE SPECIFICITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:28:11.745036+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b56a36704099444e686e704fe8993d737b0fe848fed00c7247b8f75bf147a97d",
  "url": "https://rest.uniprot.org/uniprotkb/F1M928.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/F1M928?format=txt&versions=92)

```json
{
  "entry_version": 92,
  "evidence_id": "H1",
  "excerpt": "ID   JUNO_RAT                Reviewed;         244 AA.\nAC   F1M928; A0A1B1W5N3; A6JNA9;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   03-APR-2013, sequence version 2.\nDT   28-JAN-2026, entry version 92.\nDE   RecName: Full=Sperm-egg fusion protein Juno;\nDE   AltName: Full=Folate receptor 4;\nDE   AltName: Full=Folate receptor delta;\nDE            Short=FR-delta;\nDE   AltName: Full=IZUMO1 receptor protein JUNO;\nDE   Flags: Precursor;\nGN   Name=Izumo1r; Synonyms=Folr4, JUNO {ECO:0000303|PubMed:37951137};\nOS   Rattus norvegicus (Rat).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;\nOC   Eutheria; Euarchontoglires; Glires; Rodentia; Myomorpha; Muroidea; Muridae;\nOC   Murinae; Rattus.\nOX   NCBI_TaxID=10116;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:13.956568+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "57bdb51b29963fdcfb395f44171ffb2ca0c93e66ec625c64278875faf6b4aa52",
  "url": "https://rest.uniprot.org/unisave/F1M928?format=txt&versions=92"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/F1M928?format=txt&versions=92)

```json
{
  "entry_version": 92,
  "evidence_id": "H2",
  "excerpt": "RN   [4]\nRP   INTERACTION WITH WDR54, SUBCELLULAR LOCATION, AND TISSUE SPECIFICITY.\nRX   PubMed=37951137; DOI=10.1016/j.theriogenology.2023.10.031;\nRA   Lai X., Liu R., Li M., Fan Y., Li H., Han G., Guo R., Ma H., Su H.,\nRA   Xing W.;\nRT   \"Participation of WD repeat-containing protein 54 (WDR54) in rat sperm-\nRT   oocyte fusion through interaction with both IZUMO1 and JUNO.\";\nRL   Theriogenology 214:286-297(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:13.956568+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 79-86",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "57bdb51b29963fdcfb395f44171ffb2ca0c93e66ec625c64278875faf6b4aa52",
  "url": "https://rest.uniprot.org/unisave/F1M928?format=txt&versions=92"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/F1M928?format=txt&versions=92)

```json
{
  "entry_version": 92,
  "evidence_id": "H3",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000269|PubMed:37951137};\nCC       Lipid-anchor, GPI-anchor {ECO:0000250|UniProtKB:Q9EQF4}. Cell\nCC       projection, microvillus membrane {ECO:0000250|UniProtKB:A6ND01}; Lipid-\nCC       anchor, GPI-anchor {ECO:0000250|UniProtKB:Q9EQF4}. Note=GPI-anchored at\nCC       the oolemma microvilli. {ECO:0000250|UniProtKB:Q9EQF4}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:13.956568+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 100-104",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "57bdb51b29963fdcfb395f44171ffb2ca0c93e66ec625c64278875faf6b4aa52",
  "url": "https://rest.uniprot.org/unisave/F1M928?format=txt&versions=92"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/F1M928?format=txt&versions=92)

```json
{
  "entry_version": 92,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0009897; C:external side of plasma membrane; IBA:GO_Central.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:13.956568+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 147-147",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "57bdb51b29963fdcfb395f44171ffb2ca0c93e66ec625c64278875faf6b4aa52",
  "url": "https://rest.uniprot.org/unisave/F1M928?format=txt&versions=92"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/F1M928?format=txt&versions=92)

```json
{
  "entry_version": 92,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0031528; C:microvillus membrane; IEA:UniProtKB-SubCell.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:13.956568+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 148-148",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "57bdb51b29963fdcfb395f44171ffb2ca0c93e66ec625c64278875faf6b4aa52",
  "url": "https://rest.uniprot.org/unisave/F1M928?format=txt&versions=92"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/F1M928?format=txt&versions=92)

```json
{
  "entry_version": 92,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0005886; C:plasma membrane; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:13.956568+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 149-149",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "57bdb51b29963fdcfb395f44171ffb2ca0c93e66ec625c64278875faf6b4aa52",
  "url": "https://rest.uniprot.org/unisave/F1M928?format=txt&versions=92"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0000124\nname: SAGA complex\nnamespace: cellular_component\nalt_id: GO:0000125\nalt_id: GO:0030914\ndef: \"A SAGA-type histone acetyltransferase complex that deubiquitinates H2A and/or H2B. This complex is organized into several functional submodules: a structural core including the activator binding module and consisting of ADA1 or a homolog, members of the SPT and TAF protein families as well as promotor recruitment factor TRRAP/TRA1, a histone acetyltransferase (HAT) module consisting of GCN5/KAT2A or PCAF/KAT2B, ADA2, ADA3/NGG1, and SGF29 or homologues thereof, a histone deubiquitinase (DUB) module consisting of ATXN7/SGF73, ATXN7L3/SGF11, ENY2/SUS1 and USP22/UBP8 or homologues thereof, and in some taxa a splicing module consisting of SF3B3 and SF3B5 or homologues thereof (not in fungi). In budding yeast also contains Spt8 which distinguishes it from SAGA-like (SLIK) complex (GO:0046695).\" [PMID:10637607, PMID:17337012, PMID:19056896, PMID:20838651, PMID:33004486]\nsynonym: \"PCAF complex\" NARROW []\nsynonym: \"PCAF histone acetylase-associated complex\" NARROW []\nsynonym: \"Spt-Ada-Gcn5-acetyltransferase complex\" EXACT []\nsynonym: \"SPT3-TAF9-GCN5 acetylase complex\" RELATED [GOC:rl, PMID:18838386]\nsynonym: \"SPT3-TAF9-PCAF acetylase complex\" NARROW [PMID:18838386]\nsynonym: \"STAGA coactivator complex\" RELATED []\nsynonym: \"STAGA complex\" RELATED [PMID:32616828, PMID:33004486, PMID:34112237]\nis_a: GO:0070461 ! SAGA-type complex\nis_a: GO:1905368 ! peptidase complex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0000124",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 1252-1268",
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
  "excerpt": "[Term]\nid: GO:0031528\nname: microvillus membrane\nnamespace: cellular_component\ndef: \"The portion of the plasma membrane surrounding a microvillus.\" [GOC:mah]\nis_a: GO:0031253 ! cell projection membrane\nrelationship: part_of GO:0005902 ! microvillus\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0031528",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 177423-177430",
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
  "excerpt": "[Term]\nid: GO:0060388\nname: vitelline envelope\nnamespace: cellular_component\ndef: \"A glycoprotein-based structure that lies outside the plasma membrane and surrounds the egg before fertilization.\" [GOC:dph, ISBN:0878932437]\nsynonym: \"fertilization membrane\" RELATED []\nis_a: GO:0035805 ! egg coat\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0060388",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 347268-347275",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 188. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
