# GO_cellular_component_0145

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0145.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **A** — endoplasmic reticulum membrane

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAVYSYYPIDMVLLAHLIGIIYLIIILGTLVMLFS

[Multiple Choices]
A. endoplasmic reticulum membrane
B. actin cytoskeleton
C. presynaptic active zone
D. dendrite
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

> The supplied sequence matches the 35-aa protein record, which annotates it to the endoplasmic reticulum membrane with experimental evidence (ECO:0000269). This supports choice A, though the cited primary study was not independently reviewed here.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a long, strongly hydrophobic stretch and is only 35 amino acids long, consistent with a very small single-pass membrane protein. Among the choices, the ER membrane is the most plausible broad localization: actin cytoskeleton is not a membrane compartment, while presynaptic active zone and dendrite imply specialized neuronal localization for which the input provides no supporting context. This is a probabilistic inference, not a way to determine ER rather than another membrane system with certainty.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable knowledge about hydrophobic transmembrane segments meaningfully favors a membrane location, and the alternatives make the ER membrane a defensible best choice. The sequence alone does not establish exact ER residency.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The transmembrane-like sequence makes membrane localization plausible, but the neuronal options lack supporting context and are less defensible as the best choice than the ER membrane.


### Important caveats

- The experimental annotation supports the key but was reviewer-only evidence, not an input to the evaluated model.
- A hydrophobic segment predicts membrane association more directly than it predicts the specific membrane compartment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a long, strongly hydrophobic stretch and is only 35 amino acids long, consistent with a very small single-pass membrane protein. Among the choices, the ER membrane is the most plausible broad localization: actin cytoskeleton is not a membrane compartment, while presynaptic active zone and dendrite imply specialized neuronal localization for which the input provides no supporting context. This is a probabilistic inference, not a way to determine ER rather than another membrane system with certainty.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge about hydrophobic transmembrane segments meaningfully favors a membrane location, and the alternatives make the ER membrane a defensible best choice. The sequence alone does not establish exact ER residency."
  },
  "case_id": "GO_cellular_component_0145",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches the 35-aa protein record, which annotates it to the endoplasmic reticulum membrane with experimental evidence (ECO:0000269). This supports choice A, though the cited primary study was not independently reviewed here."
  },
  "important_caveats": [
    "The experimental annotation supports the key but was reviewer-only evidence, not an input to the evaluated model.",
    "A hydrophobic segment predicts membrane association more directly than it predicts the specific membrane compartment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The transmembrane-like sequence makes membrane localization plausible, but the neuronal options lack supporting context and are less defensible as the best choice than the ER membrane."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0145",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches the 35-aa protein record, which annotates it to the endoplasmic reticulum membrane with experimental evidence (ECO:0000269). This supports choice A, though the cited primary study was not independently reviewed here.",
    "evidence_ids": ["C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a long, strongly hydrophobic stretch and is only 35 amino acids long, consistent with a very small single-pass membrane protein. Among the choices, the ER membrane is the most plausible broad localization: actin cytoskeleton is not a membrane compartment, while presynaptic active zone and dendrite imply specialized neuronal localization for which the input provides no supporting context. This is a probabilistic inference, not a way to determine ER rather than another membrane system with certainty.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge about hydrophobic transmembrane segments meaningfully favors a membrane location, and the alternatives make the ER membrane a defensible best choice. The sequence alone does not establish exact ER residency."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The transmembrane-like sequence makes membrane localization plausible, but the neuronal options lack supporting context and are less defensible as the best choice than the ER membrane."
  },
  "important_caveats": [
    "The experimental annotation supports the key but was reviewer-only evidence, not an input to the evaluated model.",
    "A hydrophobic segment predicts membrane association more directly than it predicts the specific membrane compartment."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry P9WEJ6 (YGR016C-A, S. cerevisiae) annotates the exact 35-aa sequence as 'Endoplasmic reticulum membrane; Single-pass membrane protein' with experimental evidence (ECO:0000269, PubMed:37927910, a 2023 MicroPubl. Biol. paper titled 'Unannotated open reading frame in Saccharomyces cerevisiae encodes protein localizing to the endoplasmic reticulum'). The GO annotation GO:0005789 carries EXP evidence. The sequence matches exactly (SHA-256 confirmed).

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 35-residue sequence MAVYSYYPIDMVLLAHLIGIIYLIIILGTLVMLFS contains a prominent C-terminal hydrophobic stretch (~22 residues: VLLAHLIGIIYLIIILGTLVMLFS) characteristic of a single-pass transmembrane helix. This immediately identifies the protein as a membrane protein. Among the four options, only A (ER membrane) is a membrane compartment; B (actin cytoskeleton) refers to filamentous/soluble cytoskeletal structures incompatible with a TM domain; C (presynaptic active zone) and D (dendrite) are neuron-specific structures that require large multi-domain scaffold proteins (e.g., RIM, bassoon, PSD-95-class proteins) and are irrelevant to a 35-aa single-pass membrane protein. Furthermore, the small size (~35 aa) combined with a single TM domain is a hallmark topology of small ER membrane proteins (e.g., tail-anchored or small single-pass ER residents), distinguishing A from the other three non-membrane or neuron-specific options. This inference relies on: (1) recognizing hydrophobic TM segments from sequence composition, (2) knowing that actin cytoskeleton components are large structural proteins, (3) knowing that presynaptic active zone and dendrite are neuronal structures requiring complex multi-domain proteins, and (4) the general pattern that small single-pass membrane proteins are enriched at the ER membrane.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The hydrophobic TM domain is directly visible in the supplied sequence. The elimination of B, C, and D follows from general biology (TM protein ≠ cytoskeleton; 35-aa protein ≠ neuronal scaffold; neuron-specific structures irrelevant to a generic small membrane protein). The positive assignment to ER membrane is supported by the well-known pattern that small single-pass membrane proteins are commonly ER residents. No target-specific annotation or memorized fact is needed to reach A among these four options.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B, C, and D are clearly incompatible with a 35-aa single-pass membrane protein. B is a non-membrane cytoskeletal structure, C and D are neuron-specific compartments requiring large multi-domain proteins. Only A is a membrane compartment consistent with the visible TM domain and small single-pass topology.


### Important caveats

- The reviewer evidence confirms experimental (not merely computational) support for ER membrane localization via PubMed:37927910.
- The model does not receive organism identity from the input; however, the sequence features alone (small size, single TM domain) are sufficient to eliminate B, C, and D without knowing the organism.
- A single-pass membrane protein could in principle reside in other membranes (Golgi, plasma membrane, mitochondrial outer membrane), but none of those alternatives are offered among the four choices.
- The protein is annotated as 'Uncharacterized' in UniProt, meaning its function is unknown; the localization was determined experimentally but the biological role remains unclear.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 35-residue sequence MAVYSYYPIDMVLLAHLIGIIYLIIILGTLVMLFS contains a prominent C-terminal hydrophobic stretch (~22 residues: VLLAHLIGIIYLIIILGTLVMLFS) characteristic of a single-pass transmembrane helix. This immediately identifies the protein as a membrane protein. Among the four options, only A (ER membrane) is a membrane compartment; B (actin cytoskeleton) refers to filamentous/soluble cytoskeletal structures incompatible with a TM domain; C (presynaptic active zone) and D (dendrite) are neuron-specific structures that require large multi-domain scaffold proteins (e.g., RIM, bassoon, PSD-95-class proteins) and are irrelevant to a 35-aa single-pass membrane protein. Furthermore, the small size (~35 aa) combined with a single TM domain is a hallmark topology of small ER membrane proteins (e.g., tail-anchored or small single-pass ER residents), distinguishing A from the other three non-membrane or neuron-specific options. This inference relies on: (1) recognizing hydrophobic TM segments from sequence composition, (2) knowing that actin cytoskeleton components are large structural proteins, (3) knowing that presynaptic active zone and dendrite are neuronal structures requiring complex multi-domain proteins, and (4) the general pattern that small single-pass membrane proteins are enriched at the ER membrane.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The hydrophobic TM domain is directly visible in the supplied sequence. The elimination of B, C, and D follows from general biology (TM protein ≠ cytoskeleton; 35-aa protein ≠ neuronal scaffold; neuron-specific structures irrelevant to a generic small membrane protein). The positive assignment to ER membrane is supported by the well-known pattern that small single-pass membrane proteins are commonly ER residents. No target-specific annotation or memorized fact is needed to reach A among these four options."
  },
  "case_id": "GO_cellular_component_0145",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry P9WEJ6 (YGR016C-A, S. cerevisiae) annotates the exact 35-aa sequence as 'Endoplasmic reticulum membrane; Single-pass membrane protein' with experimental evidence (ECO:0000269, PubMed:37927910, a 2023 MicroPubl. Biol. paper titled 'Unannotated open reading frame in Saccharomyces cerevisiae encodes protein localizing to the endoplasmic reticulum'). The GO annotation GO:0005789 carries EXP evidence. The sequence matches exactly (SHA-256 confirmed)."
  },
  "important_caveats": [
    "The reviewer evidence confirms experimental (not merely computational) support for ER membrane localization via PubMed:37927910.",
    "The model does not receive organism identity from the input; however, the sequence features alone (small size, single TM domain) are sufficient to eliminate B, C, and D without knowing the organism.",
    "A single-pass membrane protein could in principle reside in other membranes (Golgi, plasma membrane, mitochondrial outer membrane), but none of those alternatives are offered among the four choices.",
    "The protein is annotated as 'Uncharacterized' in UniProt, meaning its function is unknown; the localization was determined experimentally but the biological role remains unclear."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B, C, and D are clearly incompatible with a 35-aa single-pass membrane protein. B is a non-membrane cytoskeletal structure, C and D are neuron-specific compartments requiring large multi-domain proteins. Only A is a membrane compartment consistent with the visible TM domain and small single-pass topology."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0145",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry P9WEJ6 (YGR016C-A, S. cerevisiae) annotates the exact 35-aa sequence as 'Endoplasmic reticulum membrane; Single-pass membrane protein' with experimental evidence (ECO:0000269, PubMed:37927910, a 2023 MicroPubl. Biol. paper titled 'Unannotated open reading frame in Saccharomyces cerevisiae encodes protein localizing to the endoplasmic reticulum'). The GO annotation GO:0005789 carries EXP evidence. The sequence matches exactly (SHA-256 confirmed).",
    "evidence_ids": ["C5", "C6", "C7", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 35-residue sequence MAVYSYYPIDMVLLAHLIGIIYLIIILGTLVMLFS contains a prominent C-terminal hydrophobic stretch (~22 residues: VLLAHLIGIIYLIIILGTLVMLFS) characteristic of a single-pass transmembrane helix. This immediately identifies the protein as a membrane protein. Among the four options, only A (ER membrane) is a membrane compartment; B (actin cytoskeleton) refers to filamentous/soluble cytoskeletal structures incompatible with a TM domain; C (presynaptic active zone) and D (dendrite) are neuron-specific structures that require large multi-domain scaffold proteins (e.g., RIM, bassoon, PSD-95-class proteins) and are irrelevant to a 35-aa single-pass membrane protein. Furthermore, the small size (~35 aa) combined with a single TM domain is a hallmark topology of small ER membrane proteins (e.g., tail-anchored or small single-pass ER residents), distinguishing A from the other three non-membrane or neuron-specific options. This inference relies on: (1) recognizing hydrophobic TM segments from sequence composition, (2) knowing that actin cytoskeleton components are large structural proteins, (3) knowing that presynaptic active zone and dendrite are neuronal structures requiring complex multi-domain proteins, and (4) the general pattern that small single-pass membrane proteins are enriched at the ER membrane.",
    "missing_item_specific_fact": "",
    "reason": "The hydrophobic TM domain is directly visible in the supplied sequence. The elimination of B, C, and D follows from general biology (TM protein ≠ cytoskeleton; 35-aa protein ≠ neuronal scaffold; neuron-specific structures irrelevant to a generic small membrane protein). The positive assignment to ER membrane is supported by the well-known pattern that small single-pass membrane proteins are commonly ER residents. No target-specific annotation or memorized fact is needed to reach A among these four options."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B, C, and D are clearly incompatible with a 35-aa single-pass membrane protein. B is a non-membrane cytoskeletal structure, C and D are neuron-specific compartments requiring large multi-domain proteins. Only A is a membrane compartment consistent with the visible TM domain and small single-pass topology."
  },
  "important_caveats": [
    "The reviewer evidence confirms experimental (not merely computational) support for ER membrane localization via PubMed:37927910.",
    "The model does not receive organism identity from the input; however, the sequence features alone (small size, single TM domain) are sufficient to eliminate B, C, and D without knowing the organism.",
    "A single-pass membrane protein could in principle reside in other membranes (Golgi, plasma membrane, mitochondrial outer membrane), but none of those alternatives are offered among the four choices.",
    "The protein is annotated as 'Uncharacterized' in UniProt, meaning its function is unknown; the localization was determined experimentally but the biological role remains unclear."
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
  "benchmark_sequence_length": 35,
  "benchmark_sequence_sha256": "a035dc17cc8d8343ff023a58adb1ee754d1f6dda5c4f10ec9f1ea3e3d82f3cf0",
  "current_entry_audit": {
    "entryVersion": 5,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-02-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "93a966297fce68bace2aba191c1ce96de572405f36dcec82cd2e1abd71c74475",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 35,
  "current_source_sequence_sha256": "a035dc17cc8d8343ff023a58adb1ee754d1f6dda5c4f10ec9f1ea3e3d82f3cf0",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 3,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "P9WEJ6",
  "selected_historical_entry_version": 3,
  "selected_historical_record_sha256": "2b9116a361e289851a454b5ec0e6b4749004d2d6afc18e6ac189e5457a8359fd",
  "selected_historical_source_sequence_length": 35,
  "selected_historical_source_sequence_sha256": "a035dc17cc8d8343ff023a58adb1ee754d1f6dda5c4f10ec9f1ea3e3d82f3cf0",
  "selected_historical_version": {
    "accession": "P9WEJ6",
    "database": "Swiss-Prot",
    "entryVersion": 3,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "YG106_YEAST",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEJ6.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P9WEJ6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:18.932651+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "93a966297fce68bace2aba191c1ce96de572405f36dcec82cd2e1abd71c74475",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEJ6.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEJ6.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":5,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-02-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:18.932651+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "93a966297fce68bace2aba191c1ce96de572405f36dcec82cd2e1abd71c74475",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEJ6.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEJ6.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Baker's yeast\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Saccharomycotina\",\"Saccharomycetes\",\"Saccharomycetales\",\"Saccharomycetaceae\",\"Saccharomyces\"],\"scientificName\":\"Saccharomyces cerevisiae (strain ATCC 204508 / S288c)\",\"taxonId\":559292}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:18.932651+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "93a966297fce68bace2aba191c1ce96de572405f36dcec82cd2e1abd71c74475",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEJ6.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEJ6.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Uncharacterized protein YGR016C-A\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:18.932651+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "93a966297fce68bace2aba191c1ce96de572405f36dcec82cd2e1abd71c74475",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEJ6.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEJ6.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37927910\",\"source\":\"PubMed\"}],\"id\":\"SL-0097\",\"value\":\"Endoplasmic reticulum membrane\"},\"topology\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"id\":\"SL-9904\",\"value\":\"Single-pass membrane protein\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-01T06:25:18.932651+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "93a966297fce68bace2aba191c1ce96de572405f36dcec82cd2e1abd71c74475",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEJ6.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEJ6.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37927910\",\"source\":\"PubMed\"}],\"id\":\"GO:0005789\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:endoplasmic reticulum membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"EXP:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/7",
  "retrieved_utc": "2026-11-01T06:25:18.932651+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "93a966297fce68bace2aba191c1ce96de572405f36dcec82cd2e1abd71c74475",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEJ6.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P9WEJ6.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Chang S.\",\"Joyson M.\",\"Kelly A.\",\"Tang L.\",\"Iannotta J.\",\"Rich A.\",\"Castilho Coelho N.\",\"Carvunis A.R.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"37927910\"},{\"database\":\"DOI\",\"id\":\"10.17912/micropub.biology.000992\"}],\"citationType\":\"journal article\",\"firstPage\":\"0\",\"id\":\"37927910\",\"journal\":\"MicroPubl. Biol.\",\"lastPage\":\"0\",\"publicationDate\":\"2023\",\"title\":\"Unannotated open reading frame in Saccharomyces cerevisiae encodes protein localizing to the endoplasmic reticulum.\",\"volume\":\"2023\"},\"referenceNumber\":5,\"referencePositions\":[\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-01T06:25:18.932651+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "93a966297fce68bace2aba191c1ce96de572405f36dcec82cd2e1abd71c74475",
  "url": "https://rest.uniprot.org/uniprotkb/P9WEJ6.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEJ6?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H1",
  "excerpt": "ID   YG106_YEAST             Reviewed;          35 AA.\nAC   P9WEJ6; A0AAT9JHZ2;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-FEB-2025, sequence version 1.\nDT   28-JAN-2026, entry version 3.\nDE   RecName: Full=Uncharacterized protein YGR016C-A {ECO:0000305};\nGN   OrderedLocusNames=YGR016C-A {ECO:0000312|SGD:S000350096};\nOS   Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Saccharomycotina; Saccharomycetes;\nOC   Saccharomycetales; Saccharomycetaceae; Saccharomyces.\nOX   NCBI_TaxID=559292;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:28.375865+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-11",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2b9116a361e289851a454b5ec0e6b4749004d2d6afc18e6ac189e5457a8359fd",
  "url": "https://rest.uniprot.org/unisave/P9WEJ6?format=txt&versions=3"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEJ6?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H2",
  "excerpt": "RN   [5]\nRP   SUBCELLULAR LOCATION.\nRX   PubMed=37927910; DOI=10.17912/micropub.biology.000992;\nRA   Chang S., Joyson M., Kelly A., Tang L., Iannotta J., Rich A.,\nRA   Castilho Coelho N., Carvunis A.R.;\nRT   \"Unannotated open reading frame in Saccharomyces cerevisiae encodes protein\nRT   localizing to the endoplasmic reticulum.\";\nRL   MicroPubl. Biol. 2023:0-0(2023).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:28.375865+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 66-73",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2b9116a361e289851a454b5ec0e6b4749004d2d6afc18e6ac189e5457a8359fd",
  "url": "https://rest.uniprot.org/unisave/P9WEJ6?format=txt&versions=3"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEJ6?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H3",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Endoplasmic reticulum membrane\nCC       {ECO:0000269|PubMed:37927910}; Single-pass membrane protein\nCC       {ECO:0000255}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:28.375865+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 74-76",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2b9116a361e289851a454b5ec0e6b4749004d2d6afc18e6ac189e5457a8359fd",
  "url": "https://rest.uniprot.org/unisave/P9WEJ6?format=txt&versions=3"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P9WEJ6?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0005789; C:endoplasmic reticulum membrane; IEA:UniProtKB-SubCell.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:28.375865+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 89-89",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2b9116a361e289851a454b5ec0e6b4749004d2d6afc18e6ac189e5457a8359fd",
  "url": "https://rest.uniprot.org/unisave/P9WEJ6?format=txt&versions=3"
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
  "excerpt": "[Term]\nid: GO:0015629\nname: actin cytoskeleton\nnamespace: cellular_component\ndef: \"The part of the cytoskeleton (the internal framework of a cell) composed of actin and associated proteins. Includes actin cytoskeleton-associated complexes.\" [GOC:jl, ISBN:0395825172, ISBN:0815316194]\nis_a: GO:0005856 ! cytoskeleton\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0015629",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 119402-119408",
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
  "excerpt": "[Term]\nid: GO:0030425\nname: dendrite\nnamespace: cellular_component\ndef: \"A neuron projection that has a short, tapering, morphology. Dendrites receive and integrate signals from other neurons or from sensory stimuli, and conduct nerve impulses towards the axon or the cell body. In most neurons, the impulse is conveyed from dendrites to axon via the cell body, but in some types of unipolar neuron, the impulse does not travel via the cell body.\" [GOC:aruk, GOC:bc, GOC:dos, GOC:mah, GOC:nln, ISBN:0198506732]\nxref: NIF_Subcellular:sao1211023249\nxref: Wikipedia:Dendrite\nis_a: GO:0043005 ! neuron projection\nrelationship: part_of GO:0097447 ! dendritic tree\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0030425",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 166070-166079",
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
  "excerpt": "[Term]\nid: GO:0048786\nname: presynaptic active zone\nnamespace: cellular_component\ndef: \"A specialized region of the plasma membrane and cell cortex of a presynaptic neuron; encompasses a region of the plasma membrane where synaptic vesicles dock and fuse, and a specialized cortical cytoskeletal matrix.\" [GOC:dh, GOC:dl, GOC:ef, GOC:jid, GOC:pr, PMID:3152289]\nsubset: goslim_synapse\nsynonym: \"pre-synaptic active zone\" EXACT []\nsynonym: \"pre-synaptic active zone component\" NARROW [NIF_Subcellular:sao1911631652]\nsynonym: \"presynaptic specialization\" EXACT []\nxref: NIF_Subcellular:sao792027222\nis_a: GO:0110165 ! cellular anatomical structure\nrelationship: part_of GO:0098793 ! presynapse\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0048786",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 306510-306522",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 145. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
