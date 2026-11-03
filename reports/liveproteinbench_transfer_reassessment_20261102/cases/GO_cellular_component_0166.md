# GO_cellular_component_0166: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/GO_cellular_component_0166.txt)

**Task:** `GO_cellular_component`  
**Author key, unchanged:** **D** — ATP-binding cassette (ABC) transporter complex

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |
| after | GPT-6 Luna | supported | reasoning-supported | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MTTLDLTARSDRGRVYWLLADCWNIVRRGLTHYQRQPVNIAWQLGFPILSVLLYGYVFGSAMKVPGGGDYKDFLMPGMFVMTMAFGFINTATLVVYDSTKGVIDRFRSMPMASSAVVAGRGVTDLITACAELAIMMLTAFAMGWRPDGGLGFLGAFGLLLWLRFALIWIGVWLGLLVPNPEAAGGLFAVAFPLTMISSIMVAPQLMPDWLGWVAMWNPISSTAAATRELFGTPVGGDTWVEQHALLMAGVWPVILTLVFLPLAVRRFKKLSR

[Multiple Choices]
A. nuclear periphery
B. cell surface
C. IRE1-TRAF2-ASK1 complex
D. ATP-binding cassette (ABC) transporter complex
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

## Four saved visible reviews

## Before: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The exact sequence matches a UniProt entry annotated to GO:0043190, ATP-binding cassette (ABC) transporter complex, by IEA:InterPro. This supports D as a database annotation, though not as direct experimental evidence.

Citations as saved: [H1](#evidence-h1), [H4](#evidence-h4), [C1](#evidence-c1), [C6](#evidence-c6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The strongly hydrophobic sequence supports a multipass membrane protein, but that alone does not establish membership in an ABC transporter complex or distinguish that complex annotation from a membrane-associated location.


**Missing item-specific fact**

> The protein-specific identification as the DrrB2 ABC-transporter permease and its GO:0043190 annotation are not supplied in the question.


**Reason**

> Choosing D depends on identifying the protein or obtaining a family/complex annotation; the sequence’s general membrane topology does not by itself establish the specific GO complex.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence supports membrane association, but the cell-surface option is not equivalent to a membrane or transporter-complex annotation, and the supplied evidence does not establish external cell-surface localization.


### Important caveats

- The ABC-complex annotation is computational (IEA:InterPro), not reported here as direct experimental evidence.
- UniProt also records cell-membrane localization, with evidence transferred by similarity; that is not the same GO term as the cell-surface option.
- The reviewer evidence confirms an exact sequence match and a historical annotation, but that protein-specific information was absent from the evaluated input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The strongly hydrophobic sequence supports a multipass membrane protein, but that alone does not establish membership in an ABC transporter complex or distinguish that complex annotation from a membrane-associated location.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as the DrrB2 ABC-transporter permease and its GO:0043190 annotation are not supplied in the question.",
    "reason": "Choosing D depends on identifying the protein or obtaining a family/complex annotation; the sequence’s general membrane topology does not by itself establish the specific GO complex."
  },
  "case_id": "GO_cellular_component_0166",
  "expected_answer_check": {
    "evidence_ids": [
      "H1",
      "H4",
      "C1",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated to GO:0043190, ATP-binding cassette (ABC) transporter complex, by IEA:InterPro. This supports D as a database annotation, though not as direct experimental evidence."
  },
  "important_caveats": [
    "The ABC-complex annotation is computational (IEA:InterPro), not reported here as direct experimental evidence.",
    "UniProt also records cell-membrane localization, with evidence transferred by similarity; that is not the same GO term as the cell-surface option.",
    "The reviewer evidence confirms an exact sequence match and a historical annotation, but that protein-specific information was absent from the evaluated input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence supports membrane association, but the cell-surface option is not equivalent to a membrane or transporter-complex annotation, and the supplied evidence does not establish external cell-surface localization."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0166",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated to GO:0043190, ATP-binding cassette (ABC) transporter complex, by IEA:InterPro. This supports D as a database annotation, though not as direct experimental evidence.",
    "evidence_ids": ["H1", "H4", "C1", "C6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The strongly hydrophobic sequence supports a multipass membrane protein, but that alone does not establish membership in an ABC transporter complex or distinguish that complex annotation from a membrane-associated location.",
    "missing_item_specific_fact": "The protein-specific identification as the DrrB2 ABC-transporter permease and its GO:0043190 annotation are not supplied in the question.",
    "reason": "Choosing D depends on identifying the protein or obtaining a family/complex annotation; the sequence’s general membrane topology does not by itself establish the specific GO complex."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence supports membrane association, but the cell-surface option is not equivalent to a membrane or transporter-complex annotation, and the supplied evidence does not establish external cell-surface localization."
  },
  "important_caveats": [
    "The ABC-complex annotation is computational (IEA:InterPro), not reported here as direct experimental evidence.",
    "UniProt also records cell-membrane localization, with evidence transferred by similarity; that is not the same GO term as the cell-surface option.",
    "The reviewer evidence confirms an exact sequence match and a historical annotation, but that protein-specific information was absent from the evaluated input."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DXU6 (sequence matched) annotates GO:0043190 (ATP-binding cassette (ABC) transporter complex) with evidence code IEA:InterPro (C6, H4). The protein is named 'Daunorubicin resistance ABC transporter permease protein DrrB2' (C4, H1). The GO term definition (GO3) describes a complex with 'two membrane-associated domains and two ATP-binding domains,' and this protein provides the membrane-associated permease component. The annotation is computational (IEA:InterPro) rather than directly experimental, but it is consistent with the protein's identity as an ABC transporter permease and the multi-pass membrane topology noted in the subcellular location comment (C5, H3).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4), [GO3](#evidence-go3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains approximately 6-8 hydrophobic stretches consistent with multi-pass transmembrane helices, clearly indicating an integral membrane protein. Option A (nuclear periphery) is eliminated because the protein lacks nuclear localization signals and has obvious TM architecture. Option C (IRE1-TRAF2-ASK1 complex, GO:0009986) is eliminated because it is defined as an endoplasmic reticulum membrane complex in eukaryotes (GO4), incompatible with a bacterial multi-pass membrane protein lacking ER signal sequences. Option B (cell surface, GO:0009986) is defined as 'the external part of the cell wall and/or plasma membrane' for proteins 'attached (integrated or loosely bound)' to the surface (GO1); a protein with ~6-8 TM helices spanning the membrane is an integral membrane transporter, not a surface-attached protein. Option D (ABC transporter complex, GO:0043190) is defined as 'typically comprised of four domains; two membrane-associated domains and two ATP-binding domains' (GO3); the protein's multi-pass TM architecture without any Walker A/B nucleotide-binding motifs is consistent with the permease (membrane-associated) component of such a complex. These GO term definitions and membrane topology arguments provide concrete grounds to select D.


**Missing item-specific fact**

> Precise recognition of ABC transporter transmembrane domain signature motifs (e.g., Pfam ABC_transmem_1/2) to distinguish this from other multi-pass membrane transporter families (MFS, SMR) would require domain-database lookup, though the given options do not include competing transporter families.


**Reason**

> While the specific identification as ABC transporter (rather than another transporter family) benefits from domain-level knowledge, the provided options are sufficiently distinct that general reasoning about membrane topology, GO term semantics, and the absence of nucleotide-binding domains meaningfully narrows the answer to D. The distractors (nuclear periphery, eukaryotic ER complex, cell-surface attachment) are eliminable through standard cell biology knowledge without protein-specific lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and C are clearly incompatible with a bacterial multi-pass integral membrane transporter based on GO term definitions and basic cell biology. The UniProt entry also annotates plasma membrane (GO:0005886, ISS), but this is not among the choices. Among the four provided options, D is the only one consistent with an integral membrane transporter permease component.


### Important caveats

- The GO:0043190 annotation carries evidence code IEA:InterPro (automated/computational), not direct experimental evidence. The subcellular location 'Cell membrane' is annotated via ISS (similarity to P32011).
- The UniProt entry was first released 2025-02-05; the benchmark construction date is unknown, so the author may have relied on a different or earlier annotation source.
- The reviewer-only accession P0DXU6 was inferred from dataset metadata absent from the evaluated model input; the model must work from sequence alone.
- The protein name explicitly states 'ABC transporter permease,' but this name is not provided in the question input; reasoning must rely on sequence features and general knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains approximately 6-8 hydrophobic stretches consistent with multi-pass transmembrane helices, clearly indicating an integral membrane protein. Option A (nuclear periphery) is eliminated because the protein lacks nuclear localization signals and has obvious TM architecture. Option C (IRE1-TRAF2-ASK1 complex, GO:0009986) is eliminated because it is defined as an endoplasmic reticulum membrane complex in eukaryotes (GO4), incompatible with a bacterial multi-pass membrane protein lacking ER signal sequences. Option B (cell surface, GO:0009986) is defined as 'the external part of the cell wall and/or plasma membrane' for proteins 'attached (integrated or loosely bound)' to the surface (GO1); a protein with ~6-8 TM helices spanning the membrane is an integral membrane transporter, not a surface-attached protein. Option D (ABC transporter complex, GO:0043190) is defined as 'typically comprised of four domains; two membrane-associated domains and two ATP-binding domains' (GO3); the protein's multi-pass TM architecture without any Walker A/B nucleotide-binding motifs is consistent with the permease (membrane-associated) component of such a complex. These GO term definitions and membrane topology arguments provide concrete grounds to select D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise recognition of ABC transporter transmembrane domain signature motifs (e.g., Pfam ABC_transmem_1/2) to distinguish this from other multi-pass membrane transporter families (MFS, SMR) would require domain-database lookup, though the given options do not include competing transporter families.",
    "reason": "While the specific identification as ABC transporter (rather than another transporter family) benefits from domain-level knowledge, the provided options are sufficiently distinct that general reasoning about membrane topology, GO term semantics, and the absence of nucleotide-binding domains meaningfully narrows the answer to D. The distractors (nuclear periphery, eukaryotic ER complex, cell-surface attachment) are eliminable through standard cell biology knowledge without protein-specific lookup."
  },
  "case_id": "GO_cellular_component_0166",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H3",
      "H4",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DXU6 (sequence matched) annotates GO:0043190 (ATP-binding cassette (ABC) transporter complex) with evidence code IEA:InterPro (C6, H4). The protein is named 'Daunorubicin resistance ABC transporter permease protein DrrB2' (C4, H1). The GO term definition (GO3) describes a complex with 'two membrane-associated domains and two ATP-binding domains,' and this protein provides the membrane-associated permease component. The annotation is computational (IEA:InterPro) rather than directly experimental, but it is consistent with the protein's identity as an ABC transporter permease and the multi-pass membrane topology noted in the subcellular location comment (C5, H3)."
  },
  "important_caveats": [
    "The GO:0043190 annotation carries evidence code IEA:InterPro (automated/computational), not direct experimental evidence. The subcellular location 'Cell membrane' is annotated via ISS (similarity to P32011).",
    "The UniProt entry was first released 2025-02-05; the benchmark construction date is unknown, so the author may have relied on a different or earlier annotation source.",
    "The reviewer-only accession P0DXU6 was inferred from dataset metadata absent from the evaluated model input; the model must work from sequence alone.",
    "The protein name explicitly states 'ABC transporter permease,' but this name is not provided in the question input; reasoning must rely on sequence features and general knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C are clearly incompatible with a bacterial multi-pass integral membrane transporter based on GO term definitions and basic cell biology. The UniProt entry also annotates plasma membrane (GO:0005886, ISS), but this is not among the choices. Among the four provided options, D is the only one consistent with an integral membrane transporter permease component."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0166",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DXU6 (sequence matched) annotates GO:0043190 (ATP-binding cassette (ABC) transporter complex) with evidence code IEA:InterPro (C6, H4). The protein is named 'Daunorubicin resistance ABC transporter permease protein DrrB2' (C4, H1). The GO term definition (GO3) describes a complex with 'two membrane-associated domains and two ATP-binding domains,' and this protein provides the membrane-associated permease component. The annotation is computational (IEA:InterPro) rather than directly experimental, but it is consistent with the protein's identity as an ABC transporter permease and the multi-pass membrane topology noted in the subcellular location comment (C5, H3).",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H3", "H4", "GO3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains approximately 6-8 hydrophobic stretches consistent with multi-pass transmembrane helices, clearly indicating an integral membrane protein. Option A (nuclear periphery) is eliminated because the protein lacks nuclear localization signals and has obvious TM architecture. Option C (IRE1-TRAF2-ASK1 complex, GO:0009986) is eliminated because it is defined as an endoplasmic reticulum membrane complex in eukaryotes (GO4), incompatible with a bacterial multi-pass membrane protein lacking ER signal sequences. Option B (cell surface, GO:0009986) is defined as 'the external part of the cell wall and/or plasma membrane' for proteins 'attached (integrated or loosely bound)' to the surface (GO1); a protein with ~6-8 TM helices spanning the membrane is an integral membrane transporter, not a surface-attached protein. Option D (ABC transporter complex, GO:0043190) is defined as 'typically comprised of four domains; two membrane-associated domains and two ATP-binding domains' (GO3); the protein's multi-pass TM architecture without any Walker A/B nucleotide-binding motifs is consistent with the permease (membrane-associated) component of such a complex. These GO term definitions and membrane topology arguments provide concrete grounds to select D.",
    "missing_item_specific_fact": "Precise recognition of ABC transporter transmembrane domain signature motifs (e.g., Pfam ABC_transmem_1/2) to distinguish this from other multi-pass membrane transporter families (MFS, SMR) would require domain-database lookup, though the given options do not include competing transporter families.",
    "reason": "While the specific identification as ABC transporter (rather than another transporter family) benefits from domain-level knowledge, the provided options are sufficiently distinct that general reasoning about membrane topology, GO term semantics, and the absence of nucleotide-binding domains meaningfully narrows the answer to D. The distractors (nuclear periphery, eukaryotic ER complex, cell-surface attachment) are eliminable through standard cell biology knowledge without protein-specific lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C are clearly incompatible with a bacterial multi-pass integral membrane transporter based on GO term definitions and basic cell biology. The UniProt entry also annotates plasma membrane (GO:0005886, ISS), but this is not among the choices. Among the four provided options, D is the only one consistent with an integral membrane transporter permease component."
  },
  "important_caveats": [
    "The GO:0043190 annotation carries evidence code IEA:InterPro (automated/computational), not direct experimental evidence. The subcellular location 'Cell membrane' is annotated via ISS (similarity to P32011).",
    "The UniProt entry was first released 2025-02-05; the benchmark construction date is unknown, so the author may have relied on a different or earlier annotation source.",
    "The reviewer-only accession P0DXU6 was inferred from dataset metadata absent from the evaluated model input; the model must work from sequence alone.",
    "The protein name explicitly states 'ABC transporter permease,' but this name is not provided in the question input; reasoning must rely on sequence features and general knowledge."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The matched sequence has a UniProt GO annotation to the ABC transporter complex (GO:0043190), inferred by InterPro, and is annotated as a daunorubicin-resistance ABC transporter permease. This supports D, though the GO annotation is computational rather than direct experimental evidence.

Citations as saved: [C4](#evidence-c4), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 272-aa sequence is strongly multipass and membrane-protein-like, with no evident soluble ATPase domain. Bacterial ABC transporters commonly have separate multipass permease subunits and ATP-binding subunits, so this architecture supports a transporter-complex component (D) over the nuclear or eukaryotic signaling-complex alternatives. This is a family-level, probabilistic inference; multipass architecture alone does not uniquely identify ABC transporters.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A transferable inference from the sequence architecture and general organization of bacterial ABC transporters meaningfully favors D among these choices. Exact target annotation is not necessary for that inference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> D describes the protein's likely complex membership, while B can describe an integral protein at the cell surface. These cellular-component descriptions need not be mutually exclusive, and the prompt does not specify whether it seeks complex membership or membrane/surface location.


### Important caveats

- The sequence-matched GO annotation for D is IEA:InterPro, not direct experimental localization or complex-membership evidence.
- The source also describes the protein as a multipass cell-membrane protein; its subcellular-location annotation is transferred by similarity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 272-aa sequence is strongly multipass and membrane-protein-like, with no evident soluble ATPase domain. Bacterial ABC transporters commonly have separate multipass permease subunits and ATP-binding subunits, so this architecture supports a transporter-complex component (D) over the nuclear or eukaryotic signaling-complex alternatives. This is a family-level, probabilistic inference; multipass architecture alone does not uniquely identify ABC transporters.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A transferable inference from the sequence architecture and general organization of bacterial ABC transporters meaningfully favors D among these choices. Exact target annotation is not necessary for that inference."
  },
  "case_id": "GO_cellular_component_0166",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The matched sequence has a UniProt GO annotation to the ABC transporter complex (GO:0043190), inferred by InterPro, and is annotated as a daunorubicin-resistance ABC transporter permease. This supports D, though the GO annotation is computational rather than direct experimental evidence."
  },
  "important_caveats": [
    "The sequence-matched GO annotation for D is IEA:InterPro, not direct experimental localization or complex-membership evidence.",
    "The source also describes the protein as a multipass cell-membrane protein; its subcellular-location annotation is transferred by similarity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "D describes the protein's likely complex membership, while B can describe an integral protein at the cell surface. These cellular-component descriptions need not be mutually exclusive, and the prompt does not specify whether it seeks complex membership or membrane/surface location."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0166",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence has a UniProt GO annotation to the ABC transporter complex (GO:0043190), inferred by InterPro, and is annotated as a daunorubicin-resistance ABC transporter permease. This supports D, though the GO annotation is computational rather than direct experimental evidence.",
    "evidence_ids": ["C4", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 272-aa sequence is strongly multipass and membrane-protein-like, with no evident soluble ATPase domain. Bacterial ABC transporters commonly have separate multipass permease subunits and ATP-binding subunits, so this architecture supports a transporter-complex component (D) over the nuclear or eukaryotic signaling-complex alternatives. This is a family-level, probabilistic inference; multipass architecture alone does not uniquely identify ABC transporters.",
    "missing_item_specific_fact": "",
    "reason": "A transferable inference from the sequence architecture and general organization of bacterial ABC transporters meaningfully favors D among these choices. Exact target annotation is not necessary for that inference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "D describes the protein's likely complex membership, while B can describe an integral protein at the cell surface. These cellular-component descriptions need not be mutually exclusive, and the prompt does not specify whether it seeks complex membership or membrane/surface location."
  },
  "important_caveats": [
    "The sequence-matched GO annotation for D is IEA:InterPro, not direct experimental localization or complex-membership evidence.",
    "The source also describes the protein as a multipass cell-membrane protein; its subcellular-location annotation is transferred by similarity."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry P0DXU6 annotates this protein as 'Daunorubicin resistance ABC transporter permease protein DrrB2' from Streptomyces coeruleorubidus. The GO term GO:0043190 (ABC transporter complex) is assigned with IEA:InterPro evidence, and the subcellular location is 'Cell membrane; Multi-pass membrane protein' (ECO:0000250 by similarity to P32011). A 2024 publication (PubMed:39375957) confirms function in daunorubicin efflux via ABC transporters. The annotation is computational/similarity-based rather than direct experimental localization, but the protein's identity as an ABC permease is well-supported by literature.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is 272 aa, highly hydrophobic, with approximately 6-8 long hydrophobic stretches consistent with multi-pass transmembrane helices, and lacks any Walker A/B or nucleotide-binding motifs. This architecture is the hallmark of the transmembrane permease component of ABC transporters (e.g., MsbA, DrrB, MacB permeases), which are typically 200-400 aa multi-TM proteins that partner with separate NBD subunits. Bacterial origin (inferred from the sequence lacking eukaryotic features and the overall composition) immediately eliminates A (nuclear periphery — no nucleus in bacteria) and C (IRE1-TRAF2-ASK1 complex — an ER-specific eukaryotic signaling complex). Between B (cell surface) and D (ABC transporter complex): 'cell surface' (GO:0009986) is defined for gene products 'attached to the plasma membrane or cell wall,' typically surface-exposed or single-pass proteins. The multi-pass TM topology with characteristic ABC-permease helix spacing and the specific size (~270 aa) are far more consistent with an integral transporter permease than a generic surface-attached protein. Knowledge of other ABC permeases (Pfam PF01061, ABC transporter permease family) provides a transferable signature that distinguishes this from a generic membrane protein, making D the most specific and appropriate choice.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model with knowledge of ABC transporter permease architecture (multi-TM, ~250-350 aa, no NBD motifs, characteristic helix spacing) can recognize this sequence as an ABC permease component. Bacterial context eliminates eukaryotic-specific options. The multi-pass integral membrane topology distinguishes D from the more generic 'cell surface' option B. This is a family-level inference from other ABC transporters, not a lookup of this specific protein's record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B"
]
```

> Option B (cell surface) is technically applicable since the protein is integrated in the plasma membrane of a bacterium, and GO:0009986 covers membrane-integrated proteins. However, GO annotation practice favors the most specific applicable term, and the multi-pass transporter architecture makes D clearly more appropriate. B is a defensible but less specific choice; a well-informed model should prefer D.


### Important caveats

- The GO:0043190 annotation is IEA:InterPro (automated computational assignment based on domain match), not direct experimental evidence of complex membership.
- The subcellular location annotation uses similarity-based evidence (ECO:0000250|UniProtKB:P32011), transferring from a related ABC transporter.
- The protein was only integrated into Swiss-Prot in February 2025; the benchmark may have used TrEMBL or pre-publication data.
- The GO term 'cell surface' (GO:0009986) is broad enough to technically encompass membrane-integrated proteins, creating mild overlap with D, though GO specificity conventions resolve this.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is 272 aa, highly hydrophobic, with approximately 6-8 long hydrophobic stretches consistent with multi-pass transmembrane helices, and lacks any Walker A/B or nucleotide-binding motifs. This architecture is the hallmark of the transmembrane permease component of ABC transporters (e.g., MsbA, DrrB, MacB permeases), which are typically 200-400 aa multi-TM proteins that partner with separate NBD subunits. Bacterial origin (inferred from the sequence lacking eukaryotic features and the overall composition) immediately eliminates A (nuclear periphery — no nucleus in bacteria) and C (IRE1-TRAF2-ASK1 complex — an ER-specific eukaryotic signaling complex). Between B (cell surface) and D (ABC transporter complex): 'cell surface' (GO:0009986) is defined for gene products 'attached to the plasma membrane or cell wall,' typically surface-exposed or single-pass proteins. The multi-pass TM topology with characteristic ABC-permease helix spacing and the specific size (~270 aa) are far more consistent with an integral transporter permease than a generic surface-attached protein. Knowledge of other ABC permeases (Pfam PF01061, ABC transporter permease family) provides a transferable signature that distinguishes this from a generic membrane protein, making D the most specific and appropriate choice.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model with knowledge of ABC transporter permease architecture (multi-TM, ~250-350 aa, no NBD motifs, characteristic helix spacing) can recognize this sequence as an ABC permease component. Bacterial context eliminates eukaryotic-specific options. The multi-pass integral membrane topology distinguishes D from the more generic 'cell surface' option B. This is a family-level inference from other ABC transporters, not a lookup of this specific protein's record."
  },
  "case_id": "GO_cellular_component_0166",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry P0DXU6 annotates this protein as 'Daunorubicin resistance ABC transporter permease protein DrrB2' from Streptomyces coeruleorubidus. The GO term GO:0043190 (ABC transporter complex) is assigned with IEA:InterPro evidence, and the subcellular location is 'Cell membrane; Multi-pass membrane protein' (ECO:0000250 by similarity to P32011). A 2024 publication (PubMed:39375957) confirms function in daunorubicin efflux via ABC transporters. The annotation is computational/similarity-based rather than direct experimental localization, but the protein's identity as an ABC permease is well-supported by literature."
  },
  "important_caveats": [
    "The GO:0043190 annotation is IEA:InterPro (automated computational assignment based on domain match), not direct experimental evidence of complex membership.",
    "The subcellular location annotation uses similarity-based evidence (ECO:0000250|UniProtKB:P32011), transferring from a related ABC transporter.",
    "The protein was only integrated into Swiss-Prot in February 2025; the benchmark may have used TrEMBL or pre-publication data.",
    "The GO term 'cell surface' (GO:0009986) is broad enough to technically encompass membrane-integrated proteins, creating mild overlap with D, though GO specificity conventions resolve this."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B"
    ],
    "reason": "Option B (cell surface) is technically applicable since the protein is integrated in the plasma membrane of a bacterium, and GO:0009986 covers membrane-integrated proteins. However, GO annotation practice favors the most specific applicable term, and the multi-pass transporter architecture makes D clearly more appropriate. B is a defensible but less specific choice; a well-informed model should prefer D."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0166",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry P0DXU6 annotates this protein as 'Daunorubicin resistance ABC transporter permease protein DrrB2' from Streptomyces coeruleorubidus. The GO term GO:0043190 (ABC transporter complex) is assigned with IEA:InterPro evidence, and the subcellular location is 'Cell membrane; Multi-pass membrane protein' (ECO:0000250 by similarity to P32011). A 2024 publication (PubMed:39375957) confirms function in daunorubicin efflux via ABC transporters. The annotation is computational/similarity-based rather than direct experimental localization, but the protein's identity as an ABC permease is well-supported by literature.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is 272 aa, highly hydrophobic, with approximately 6-8 long hydrophobic stretches consistent with multi-pass transmembrane helices, and lacks any Walker A/B or nucleotide-binding motifs. This architecture is the hallmark of the transmembrane permease component of ABC transporters (e.g., MsbA, DrrB, MacB permeases), which are typically 200-400 aa multi-TM proteins that partner with separate NBD subunits. Bacterial origin (inferred from the sequence lacking eukaryotic features and the overall composition) immediately eliminates A (nuclear periphery — no nucleus in bacteria) and C (IRE1-TRAF2-ASK1 complex — an ER-specific eukaryotic signaling complex). Between B (cell surface) and D (ABC transporter complex): 'cell surface' (GO:0009986) is defined for gene products 'attached to the plasma membrane or cell wall,' typically surface-exposed or single-pass proteins. The multi-pass TM topology with characteristic ABC-permease helix spacing and the specific size (~270 aa) are far more consistent with an integral transporter permease than a generic surface-attached protein. Knowledge of other ABC permeases (Pfam PF01061, ABC transporter permease family) provides a transferable signature that distinguishes this from a generic membrane protein, making D the most specific and appropriate choice.",
    "missing_item_specific_fact": "",
    "reason": "A model with knowledge of ABC transporter permease architecture (multi-TM, ~250-350 aa, no NBD motifs, characteristic helix spacing) can recognize this sequence as an ABC permease component. Bacterial context eliminates eukaryotic-specific options. The multi-pass integral membrane topology distinguishes D from the more generic 'cell surface' option B. This is a family-level inference from other ABC transporters, not a lookup of this specific protein's record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B"],
    "reason": "Option B (cell surface) is technically applicable since the protein is integrated in the plasma membrane of a bacterium, and GO:0009986 covers membrane-integrated proteins. However, GO annotation practice favors the most specific applicable term, and the multi-pass transporter architecture makes D clearly more appropriate. B is a defensible but less specific choice; a well-informed model should prefer D."
  },
  "important_caveats": [
    "The GO:0043190 annotation is IEA:InterPro (automated computational assignment based on domain match), not direct experimental evidence of complex membership.",
    "The subcellular location annotation uses similarity-based evidence (ECO:0000250|UniProtKB:P32011), transferring from a related ABC transporter.",
    "The protein was only integrated into Swiss-Prot in February 2025; the benchmark may have used TrEMBL or pre-publication data.",
    "The GO term 'cell surface' (GO:0009986) is broad enough to technically encompass membrane-integrated proteins, creating mild overlap with D, though GO specificity conventions resolve this."
  ]
}
```

</details>

## Existing project source checks of the old Luna review only

These unchanged notes concern the earlier Luna claims. They do not validate either new review or the old Qwen review. No new scientific adjudication was performed.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Complete reviewer-only evidence and qualifications

All excerpts supplied in the original and revised reviewer user message follow. This material was not available to the original evaluated model. Accession identity came from dataset image-path metadata. Source support and transferable discrimination are separate judgments.

**Applicability metadata, unchanged:**

```json
{
  "requested_accession": "P0DXU6",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "59e638eb8cf60b05352d61e55cf16844ce8b914c1394940c66e4190daaf561d9",
  "benchmark_sequence_length": 272,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 6,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-02-05",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "4e7d0b296d64a4ffb645956bc9763e367bd0533eedf73ba35b4dc16bd7421217",
  "current_source_sequence_sha256": "59e638eb8cf60b05352d61e55cf16844ce8b914c1394940c66e4190daaf561d9",
  "current_source_sequence_length": 272,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 4,
  "selected_historical_version": {
    "accession": "P0DXU6",
    "database": "Swiss-Prot",
    "entryVersion": 4,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DRRB2_STRC4",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "372a99e71818628749a5230f6a3ea50eb4a3ab3f801909ad5a5e951310594fb7",
  "selected_historical_source_sequence_sha256": "59e638eb8cf60b05352d61e55cf16844ce8b914c1394940c66e4190daaf561d9",
  "selected_historical_source_sequence_length": 272,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 4,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "actual_author_source_snapshot": "unknown",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed."
}
```

**Qualifications, unchanged:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU6.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU6.json",
  "source_sha256": "4e7d0b296d64a4ffb645956bc9763e367bd0533eedf73ba35b4dc16bd7421217",
  "retrieved_utc": "2026-11-02T04:29:39.151534+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"P0DXU6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU6.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU6.json",
  "source_sha256": "4e7d0b296d64a4ffb645956bc9763e367bd0533eedf73ba35b4dc16bd7421217",
  "retrieved_utc": "2026-11-02T04:29:39.151534+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":6,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-02-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU6.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU6.json",
  "source_sha256": "4e7d0b296d64a4ffb645956bc9763e367bd0533eedf73ba35b4dc16bd7421217",
  "retrieved_utc": "2026-11-02T04:29:39.151534+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Bacillati\",\"Actinomycetota\",\"Actinomycetes\",\"Kitasatosporales\",\"Streptomycetaceae\",\"Streptomyces\"],\"scientificName\":\"Streptomyces coeruleorubidus\",\"taxonId\":116188}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU6.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU6.json",
  "source_sha256": "4e7d0b296d64a4ffb645956bc9763e367bd0533eedf73ba35b4dc16bd7421217",
  "retrieved_utc": "2026-11-02T04:29:39.151534+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Daunorubicin resistance ABC transporter permease protein DrrB2\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU6.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU6.json",
  "source_sha256": "4e7d0b296d64a4ffb645956bc9763e367bd0533eedf73ba35b4dc16bd7421217",
  "retrieved_utc": "2026-11-02T04:29:39.151534+00:00",
  "json_pointer": "/comments/2",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P32011\",\"source\":\"UniProtKB\"}],\"id\":\"SL-0039\",\"value\":\"Cell membrane\"},\"topology\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"id\":\"SL-9909\",\"value\":\"Multi-pass membrane protein\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU6.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU6.json",
  "source_sha256": "4e7d0b296d64a4ffb645956bc9763e367bd0533eedf73ba35b4dc16bd7421217",
  "retrieved_utc": "2026-11-02T04:29:39.151534+00:00",
  "json_pointer": "/uniProtKBCrossReferences/5",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0043190\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:ATP-binding cassette (ABC) transporter complex\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:InterPro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU6.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU6.json",
  "source_sha256": "4e7d0b296d64a4ffb645956bc9763e367bd0533eedf73ba35b4dc16bd7421217",
  "retrieved_utc": "2026-11-02T04:29:39.151534+00:00",
  "json_pointer": "/uniProtKBCrossReferences/6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005886\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:plasma membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISS:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU6?format=txt&versions=4)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXU6?format=txt&versions=4",
  "source_sha256": "372a99e71818628749a5230f6a3ea50eb4a3ab3f801909ad5a5e951310594fb7",
  "retrieved_utc": "2026-11-02T04:29:40.921406+00:00",
  "source_locator": "lines 1-12",
  "excerpt": "ID   DRRB2_STRC4             Reviewed;         272 AA.\nAC   P0DXU6;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-FEB-2025, sequence version 1.\nDT   28-JAN-2026, entry version 4.\nDE   RecName: Full=Daunorubicin resistance ABC transporter permease protein DrrB2 {ECO:0000305};\nGN   Name=drrB2 {ECO:0000303|PubMed:39375957};\nGN   ORFNames=R5U08_15990 {ECO:0000312|EMBL:WOT35540.1};\nOS   Streptomyces coeruleorubidus.\nOC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Kitasatosporales;\nOC   Streptomycetaceae; Streptomyces.\nOX   NCBI_TaxID=116188;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 4,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU6?format=txt&versions=4)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXU6?format=txt&versions=4",
  "source_sha256": "372a99e71818628749a5230f6a3ea50eb4a3ab3f801909ad5a5e951310594fb7",
  "retrieved_utc": "2026-11-02T04:29:40.921406+00:00",
  "source_locator": "lines 18-24",
  "excerpt": "RN   [2]\nRP   FUNCTION IN DAUNORUBICIN EFFLUX, INDUCTION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=39375957; DOI=10.1111/1751-7915.70023;\nRA   Dong J., Ning J., Tian Y., Li H., Chen H., Guan W.;\nRT   \"The involvement of multiple ABC transporters in daunorubicin efflux in\nRT   Streptomyces coeruleorubidus.\";\nRL   Microb. Biotechnol. 17:e70023-e70023(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 4,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU6?format=txt&versions=4)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXU6?format=txt&versions=4",
  "source_sha256": "372a99e71818628749a5230f6a3ea50eb4a3ab3f801909ad5a5e951310594fb7",
  "retrieved_utc": "2026-11-02T04:29:40.921406+00:00",
  "source_locator": "lines 33-34",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000250|UniProtKB:P32011};\nCC       Multi-pass membrane protein {ECO:0000255}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 4,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU6?format=txt&versions=4)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXU6?format=txt&versions=4",
  "source_sha256": "372a99e71818628749a5230f6a3ea50eb4a3ab3f801909ad5a5e951310594fb7",
  "retrieved_utc": "2026-11-02T04:29:40.921406+00:00",
  "source_locator": "lines 54-54",
  "excerpt": "DR   GO; GO:0043190; C:ATP-binding cassette (ABC) transporter complex; IEA:InterPro.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 4,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 101772-101784",
  "excerpt": "[Term]\nid: GO:0009986\nname: cell surface\nnamespace: cellular_component\nalt_id: GO:0009928\nalt_id: GO:0009929\ndef: \"The external part of the cell wall and/or plasma membrane.\" [GOC:jl, GOC:mtg_sensu, GOC:sm]\ncomment: Note that this term is intended to annotate gene products that are attached (integrated or loosely bound) to the plasma membrane or cell wall.\nsubset: goslim_pir\nsynonym: \"cell associated\" EXACT []\nsynonym: \"cell bound\" EXACT []\nis_a: GO:0110165 ! cellular anatomical structure\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0009986"
}
```

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO2",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 208650-208657",
  "excerpt": "[Term]\nid: GO:0034399\nname: nuclear periphery\nnamespace: cellular_component\ndef: \"The portion of the nuclear lumen proximal to the inner nuclear membrane.\" [GOC:krc, GOC:mah]\nis_a: GO:0110165 ! cellular anatomical structure\nrelationship: part_of GO:0031981 ! nuclear lumen\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0034399"
}
```

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO3",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 244782-244797",
  "excerpt": "[Term]\nid: GO:0043190\nname: ATP-binding cassette (ABC) transporter complex\nnamespace: cellular_component\nalt_id: GO:0043191\nalt_id: GO:0043192\ndef: \"A complex for the transport of metabolites into and out of the cell, typically comprised of four domains; two membrane-associated domains and two ATP-binding domains at the intracellular face of the membrane, that form a central pore through the plasma membrane. Each of the four core domains may be encoded as a separate polypeptide or the domains can be fused in any one of a number of ways into multidomain polypeptides. In Bacteria and Archaebacteria, ABC transporters also include substrate binding proteins to bind substrate external to the cytoplasm and deliver it to the transporter.\" [GOC:jl, GOC:mtg_sensu, PMID:11421269, PMID:15111107]\nsubset: goslim_metagenomics\nsubset: goslim_pir\nsynonym: \"ABC-type efflux permease complex\" NARROW []\nsynonym: \"ABC-type efflux porter complex\" NARROW []\nsynonym: \"ABC-type uptake permease complex\" NARROW []\nsynonym: \"mating pheromone exporter\" NARROW []\nis_a: GO:0098533 ! ATPase dependent transmembrane transport complex\nis_a: GO:0098797 ! plasma membrane protein complex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0043190"
}
```

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO4",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 553487-553496",
  "excerpt": "[Term]\nid: GO:1990604\nname: IRE1-TRAF2-ASK1 complex\nnamespace: cellular_component\ndef: \"A protein complex of the endoplasmic reticulum membrane that consists of IRE1 (Inositol-requiring enzyme-1), TRAF2 (TNF receptor-associated factor 2) and ASK1 (Apoptosis signal-regulating kinase 1, a MAP3K).\" [GOC:bf, GOC:PARL, PMID:12050113, PMID:23000344]\nsynonym: \"ERN1-TRAF2-ASK1 complex\" RELATED [HGNC:3449]\nis_a: GO:0098796 ! membrane protein complex\nis_a: GO:0140534 ! endoplasmic reticulum protein-containing complex\nrelationship: part_of GO:0005789 ! endoplasmic reticulum membrane\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:1990604"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 166. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
