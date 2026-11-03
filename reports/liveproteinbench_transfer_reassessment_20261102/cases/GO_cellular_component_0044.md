# GO_cellular_component_0044: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/GO_cellular_component_0044.txt)

**Task:** `GO_cellular_component`  
**Author key, unchanged:** **C** — plasma membrane

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |
| after | GPT-6 Luna | no saved label | no saved label | output error (invalid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MLSLFNRLPWLHRVLITAFSAIIVFAIFFLPNSEDLRKPDAQREVGRHYPVTLDNQLVSTPEEEVIAPPSVMLRWETYQVANGESAALLFQRAGLSSRVLYELTSSNSDINNQLSKLMPKDELKFGFDKDNQLVQLKRTISPYETFVVTRSDSGFTSEFDKKEVTFQLNYAEAKITSNFWNAGVTAGLSANQIIELANMFGWDIDFALDIREGDQFKLLYQEKIVEGSVIGRGNIIAATFINQGSTFTAILDDNTGNYYDQNGRAMKKAFLRSPLDFRRVSSNFNPRRLHPVTGQIKAHRGTDYVAPVGTPIWAAGDGVVEKSSYNQFNGNYVYIRHSNTYITKYLHLQRRLVKTGERVKQGQTIGTLGGTGRVTGPHLHYEFLVNGIHKNPRTVELPQAQSLTGKAKETFIANAKQRMEKLERYSQLLYANQ

[Multiple Choices]
A. protein-containing complex
B. endoplasmic reticulum membrane
C. plasma membrane
D. extracellular region
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

> The sequence matches the protein annotated as localized to the bacterial inner membrane, on its periplasmic side. The source reports experimental localization, and the periplasmic side of the plasma membrane is part of the plasma membrane; thus C is supported.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5), [GO3](#evidence-go3), [GO6](#evidence-go6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic segment supports membrane association, but that alone does not distinguish a plasma membrane protein from an ER membrane protein. The large downstream domain could also be consistent with an exported or membrane-tethered protein.


**Missing item-specific fact**

> The protein-specific identity and localization: it is Vibrio cholerae ShyC, experimentally localized to the cell periphery and midcell, with a single-pass inner-membrane topology and periplasmic orientation.


**Reason**

> The sequence offers a useful membrane-association clue, but selecting C over another membrane location requires item-specific organism/function or localization information not supplied in the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The source evidence supports C as the annotated location; the periplasmic-side annotation is compatible with, and more specific than, the plasma membrane option.


### Important caveats

- Reviewer-only database and literature-derived evidence supports the key but was not available to the evaluated model.
- The UniProt sequence match is exact; its localization note cites experimental evidence, whereas the single-pass topology annotation is computational.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment supports membrane association, but that alone does not distinguish a plasma membrane protein from an ER membrane protein. The large downstream domain could also be consistent with an exported or membrane-tethered protein.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identity and localization: it is Vibrio cholerae ShyC, experimentally localized to the cell periphery and midcell, with a single-pass inner-membrane topology and periplasmic orientation.",
    "reason": "The sequence offers a useful membrane-association clue, but selecting C over another membrane location requires item-specific organism/function or localization information not supplied in the question."
  },
  "case_id": "GO_cellular_component_0044",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5",
      "GO3",
      "GO6"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the protein annotated as localized to the bacterial inner membrane, on its periplasmic side. The source reports experimental localization, and the periplasmic side of the plasma membrane is part of the plasma membrane; thus C is supported."
  },
  "important_caveats": [
    "Reviewer-only database and literature-derived evidence supports the key but was not available to the evaluated model.",
    "The UniProt sequence match is exact; its localization note cites experimental evidence, whereas the single-pass topology annotation is computational."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The source evidence supports C as the annotated location; the periplasmic-side annotation is compatible with, and more specific than, the plasma membrane option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0044",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the protein annotated as localized to the bacterial inner membrane, on its periplasmic side. The source reports experimental localization, and the periplasmic side of the plasma membrane is part of the plasma membrane; thus C is supported.",
    "evidence_ids": ["C5", "C6", "H4", "H5", "GO3", "GO6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment supports membrane association, but that alone does not distinguish a plasma membrane protein from an ER membrane protein. The large downstream domain could also be consistent with an exported or membrane-tethered protein.",
    "missing_item_specific_fact": "The protein-specific identity and localization: it is Vibrio cholerae ShyC, experimentally localized to the cell periphery and midcell, with a single-pass inner-membrane topology and periplasmic orientation.",
    "reason": "The sequence offers a useful membrane-association clue, but selecting C over another membrane location requires item-specific organism/function or localization information not supplied in the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The source evidence supports C as the annotated location; the periplasmic-side annotation is compatible with, and more specific than, the plasma membrane option."
  },
  "important_caveats": [
    "Reviewer-only database and literature-derived evidence supports the key but was not available to the evaluated model.",
    "The UniProt sequence match is exact; its localization note cites experimental evidence, whereas the single-pass topology annotation is computational."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt annotates Q9KU93 (ShyC) as a single-pass membrane protein on the periplasmic side of the cell inner membrane (C5, H4). The GO annotation GO:0098567 'periplasmic side of plasma membrane' (C6, IDA evidence from PubMed 23834664) is part_of GO:0005886 'plasma membrane' via GO:0009897 (ontology path confirmed in GO6, GO4, GO3). GO:0005886 also has 'bacterial inner membrane' as a NARROW synonym (GO3). For a bacterium, the cell inner membrane is the plasma membrane. The IEA-level GO:0005886 annotation (H5) further confirms this mapping.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5), [GO3](#evidence-go3), [GO4](#evidence-go4), [GO6](#evidence-go6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable M23 peptidase motifs (e.g., 'NQLVSTPEEE', 'NQLVQLKRT', 'NQLVQLKRT') characteristic of bacterial peptidoglycan hydrolases, identifying this as a bacterial protein. Bacteria lack an endoplasmic reticulum, eliminating option B. The N-terminal hydrophobic stretch 'LITAFSAIIVFAIFFLP' (~19 residues) is consistent with a transmembrane anchor, indicating membrane association and eliminating free extracellular region (D) and protein-containing complex (A) as the primary location. For a bacterium, the inner membrane is the plasma membrane in GO terminology (GO:0005886 synonym 'bacterial inner membrane'), yielding C.


**Missing item-specific fact**

> None critical. The reasoning relies on recognizing the peptidoglycan-related domain (bacterial origin) and the hydrophobic N-terminal transmembrane region, both derivable from the sequence, plus the general fact that bacteria lack ER and that bacterial inner membrane = plasma membrane in GO.


**Reason**

> A knowledgeable model can identify the M23 peptidase domain (peptidoglycan-related → bacterial), spot the hydrophobic N-terminal transmembrane segment, and apply the general biological facts that (1) bacteria have no ER and (2) the bacterial inner membrane is the plasma membrane in GO. These steps provide concrete, sequence-grounded reasoning to distinguish C from A, B, and D without needing to look up the specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option B (ER membrane) is definitively excluded for a bacterial protein. Option D (extracellular region) is excluded by the GO definition (GO:0005576), which explicitly states it is for gene products 'not attached to the cell surface'; a single-pass membrane protein is anchored. Option A (protein-containing complex) lacks any supporting evidence in the sequence or annotation. Only C is defensible.


### Important caveats

- The organism (Vibrio cholerae) is not stated in the question; the model must infer bacterial origin from sequence features (M23 peptidase motifs). This inference is reasonable but not trivially obvious for all models.
- The protein is annotated to the periplasmic side of the plasma membrane (GO:0098567), not the plasma membrane per se. The mapping to GO:0005886 is via part_of/is_a hierarchy, which is standard GO reasoning.
- The GO:0005886 annotation carries IEA evidence (inferred from subcellular location), while the primary experimental evidence supports the more specific GO:0098567. This is a normal GO annotation hierarchy and does not weaken the answer.
- The N-terminal hydrophobic region could also be interpreted as a signal peptide rather than a transmembrane domain by some predictors; however, UniProt annotates it as a single-pass membrane protein, and either interpretation supports membrane localization over the other options.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable M23 peptidase motifs (e.g., 'NQLVSTPEEE', 'NQLVQLKRT', 'NQLVQLKRT') characteristic of bacterial peptidoglycan hydrolases, identifying this as a bacterial protein. Bacteria lack an endoplasmic reticulum, eliminating option B. The N-terminal hydrophobic stretch 'LITAFSAIIVFAIFFLP' (~19 residues) is consistent with a transmembrane anchor, indicating membrane association and eliminating free extracellular region (D) and protein-containing complex (A) as the primary location. For a bacterium, the inner membrane is the plasma membrane in GO terminology (GO:0005886 synonym 'bacterial inner membrane'), yielding C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The reasoning relies on recognizing the peptidoglycan-related domain (bacterial origin) and the hydrophobic N-terminal transmembrane region, both derivable from the sequence, plus the general fact that bacteria lack ER and that bacterial inner membrane = plasma membrane in GO.",
    "reason": "A knowledgeable model can identify the M23 peptidase domain (peptidoglycan-related → bacterial), spot the hydrophobic N-terminal transmembrane segment, and apply the general biological facts that (1) bacteria have no ER and (2) the bacterial inner membrane is the plasma membrane in GO. These steps provide concrete, sequence-grounded reasoning to distinguish C from A, B, and D without needing to look up the specific UniProt entry."
  },
  "case_id": "GO_cellular_component_0044",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5",
      "GO3",
      "GO4",
      "GO6"
    ],
    "judgment": "supported",
    "reason": "UniProt annotates Q9KU93 (ShyC) as a single-pass membrane protein on the periplasmic side of the cell inner membrane (C5, H4). The GO annotation GO:0098567 'periplasmic side of plasma membrane' (C6, IDA evidence from PubMed 23834664) is part_of GO:0005886 'plasma membrane' via GO:0009897 (ontology path confirmed in GO6, GO4, GO3). GO:0005886 also has 'bacterial inner membrane' as a NARROW synonym (GO3). For a bacterium, the cell inner membrane is the plasma membrane. The IEA-level GO:0005886 annotation (H5) further confirms this mapping."
  },
  "important_caveats": [
    "The organism (Vibrio cholerae) is not stated in the question; the model must infer bacterial origin from sequence features (M23 peptidase motifs). This inference is reasonable but not trivially obvious for all models.",
    "The protein is annotated to the periplasmic side of the plasma membrane (GO:0098567), not the plasma membrane per se. The mapping to GO:0005886 is via part_of/is_a hierarchy, which is standard GO reasoning.",
    "The GO:0005886 annotation carries IEA evidence (inferred from subcellular location), while the primary experimental evidence supports the more specific GO:0098567. This is a normal GO annotation hierarchy and does not weaken the answer.",
    "The N-terminal hydrophobic region could also be interpreted as a signal peptide rather than a transmembrane domain by some predictors; however, UniProt annotates it as a single-pass membrane protein, and either interpretation supports membrane localization over the other options."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option B (ER membrane) is definitively excluded for a bacterial protein. Option D (extracellular region) is excluded by the GO definition (GO:0005576), which explicitly states it is for gene products 'not attached to the cell surface'; a single-pass membrane protein is anchored. Option A (protein-containing complex) lacks any supporting evidence in the sequence or annotation. Only C is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0044",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt annotates Q9KU93 (ShyC) as a single-pass membrane protein on the periplasmic side of the cell inner membrane (C5, H4). The GO annotation GO:0098567 'periplasmic side of plasma membrane' (C6, IDA evidence from PubMed 23834664) is part_of GO:0005886 'plasma membrane' via GO:0009897 (ontology path confirmed in GO6, GO4, GO3). GO:0005886 also has 'bacterial inner membrane' as a NARROW synonym (GO3). For a bacterium, the cell inner membrane is the plasma membrane. The IEA-level GO:0005886 annotation (H5) further confirms this mapping.",
    "evidence_ids": ["C5", "C6", "H4", "H5", "GO3", "GO4", "GO6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable M23 peptidase motifs (e.g., 'NQLVSTPEEE', 'NQLVQLKRT', 'NQLVQLKRT') characteristic of bacterial peptidoglycan hydrolases, identifying this as a bacterial protein. Bacteria lack an endoplasmic reticulum, eliminating option B. The N-terminal hydrophobic stretch 'LITAFSAIIVFAIFFLP' (~19 residues) is consistent with a transmembrane anchor, indicating membrane association and eliminating free extracellular region (D) and protein-containing complex (A) as the primary location. For a bacterium, the inner membrane is the plasma membrane in GO terminology (GO:0005886 synonym 'bacterial inner membrane'), yielding C.",
    "missing_item_specific_fact": "None critical. The reasoning relies on recognizing the peptidoglycan-related domain (bacterial origin) and the hydrophobic N-terminal transmembrane region, both derivable from the sequence, plus the general fact that bacteria lack ER and that bacterial inner membrane = plasma membrane in GO.",
    "reason": "A knowledgeable model can identify the M23 peptidase domain (peptidoglycan-related → bacterial), spot the hydrophobic N-terminal transmembrane segment, and apply the general biological facts that (1) bacteria have no ER and (2) the bacterial inner membrane is the plasma membrane in GO. These steps provide concrete, sequence-grounded reasoning to distinguish C from A, B, and D without needing to look up the specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option B (ER membrane) is definitively excluded for a bacterial protein. Option D (extracellular region) is excluded by the GO definition (GO:0005576), which explicitly states it is for gene products 'not attached to the cell surface'; a single-pass membrane protein is anchored. Option A (protein-containing complex) lacks any supporting evidence in the sequence or annotation. Only C is defensible."
  },
  "important_caveats": [
    "The organism (Vibrio cholerae) is not stated in the question; the model must infer bacterial origin from sequence features (M23 peptidase motifs). This inference is reasonable but not trivially obvious for all models.",
    "The protein is annotated to the periplasmic side of the plasma membrane (GO:0098567), not the plasma membrane per se. The mapping to GO:0005886 is via part_of/is_a hierarchy, which is standard GO reasoning.",
    "The GO:0005886 annotation carries IEA evidence (inferred from subcellular location), while the primary experimental evidence supports the more specific GO:0098567. This is a normal GO annotation hierarchy and does not weaken the answer.",
    "The N-terminal hydrophobic region could also be interpreted as a signal peptide rather than a transmembrane domain by some predictors; however, UniProt annotates it as a single-pass membrane protein, and either interpretation supports membrane localization over the other options."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** output error.
**Canonical saved status:** `invalid_review`.

**This saved response has an output error and is not a usable structured review.** Any labels below remain the original saved values; they are excluded from label distributions and agreement. This output status does not judge the benchmark question, author key or biological correctness. No field or option ID has been repaired.

**Validation errors:** `invalid_json:Expecting property name enclosed in double quotes: line 13 column 3 (char 1327)`.

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0044",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports experimental localization to the cell inner membrane, and a plasma-membrane annotation; in bacteria, the inner membrane corresponds to the plasma membrane. The localization evidence supports choice C.",
    "evidence_ids": ["C5", "H4", "H5", "GO3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The strongly hydrophobic N-terminal stretch is consistent with a single-pass membrane anchor, while most of the protein is nonhydrophobic and could form a functional domain on the other side of that membrane. This favors a membrane location over a freely extracellular protein or a protein-containing complex. The sequence architecture is also compatible with a bacterial cell-envelope enzyme; for such proteins, the cell membrane is the plasma membrane, not an endoplasmic-reticulum membrane.",
    "missing_item_specific_fact": "",
    "reason": "The N-terminal membrane-anchor pattern and transferable knowledge of bacterial envelope-associated proteins meaningfully favor C among these choices. This is a probabilistic sequence-based inference, not proof of the organism or exact localization.",
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The membrane anchor favors a membrane compartment, and the bacterial cell-envelope interpretation favors plasma membrane over ER membrane. The alternatives describing an unanchored extracellular protein or a complex are less consistent with the sequence."
  },
  "important_caveats": [
    "The experimental annotation describes localization at the cell periphery and midcell in a subset of cells; it does not imply uniform localization at all times.",
    "The source record is sequence-matched, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

**Saved parsed visible review:** `null`.

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (Q9KU93, ShyC from Vibrio cholerae) annotates this protein as 'Cell inner membrane, Single-pass membrane protein, Periplasmic side' (C5/H4). In bacterial nomenclature, the inner membrane is the plasma membrane; GO:0005886 (plasma membrane) lists 'bacterial inner membrane' as a NARROW synonym (GO3). The direct GO annotation is GO:0098567 (periplasmic side of plasma membrane, IDA evidence, C6), which is_a GO:0009897, which is part_of GO:0005886 (ontology path confirmed). Additionally, GO:0005886 is assigned via IEA:UniProtKB-SubCell (H5). The author's answer 'plasma membrane' (C) is well-supported by the annotation evidence.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5), [GO3](#evidence-go3), [GO6](#evidence-go6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal region 'LITAFSAIIVFAIFFLP' (~17 hydrophobic residues) is a classic single-pass transmembrane helix, indicating the protein is membrane-anchored. The large hydrophilic C-terminal domain (~400 residues) contains conserved motifs 'DDN', 'NIIAAT', 'DDNTG', 'NFWNAGVTAGL', 'GWDIDF' characteristic of peptidoglycan DD-endopeptidases (NlpC/P60 or related families). From knowledge of other peptidoglycan hydrolases (e.g., lysozymes, amidases, transpeptidases), these enzymes in bacteria are anchored to the inner membrane (plasma membrane) with catalytic domains facing the periplasm. This family-level inference distinguishes C (plasma membrane) from: B (ER membrane – a eukaryotic organelle; the sequence lacks ER signal peptides, KDEL retention signals, and the peptidoglycan hydrolase domain is exclusively bacterial); D (extracellular region – the TM helix means the protein is membrane-attached, and GO explicitly excludes surface-attached proteins from this term per GO1 definition); A (protein-containing complex – while the protein may participate in complexes, its primary subcellular location is the membrane, and the TM anchor is the defining feature).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The transmembrane helix is directly visible in the sequence, and the peptidoglycan hydrolase domain is recognizable by conserved motifs shared with other characterized bacterial cell-wall enzymes. Family-level knowledge that peptidoglycan hydrolases with TM anchors localize to the bacterial inner/plasma membrane provides a concrete, transferable inference that meaningfully distinguishes C from the other three options without requiring recall of this specific protein's database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The TM helix clearly excludes D (extracellular, defined as not attached to cell surface) and A (protein-containing complex is not a location per se). B (ER membrane) is excluded by the bacterial peptidoglycan hydrolase domain architecture and absence of ER-specific targeting features. C is the only option consistent with a single-pass membrane protein bearing a peptidoglycan hydrolase domain in a bacterial context.


### Important caveats

- The reviewer evidence confirms the organism is Vibrio cholerae (bacterium), but the model was not given this information. The bacterial inference must come from sequence features (peptidoglycan hydrolase domain, absence of eukaryotic targeting signals).
- The GO annotation for this protein is GO:0098567 (periplasmic side of plasma membrane) with IDA evidence; GO:0005886 (plasma membrane) is assigned via IEA (automatic). The author's choice of 'plasma membrane' is the parent term and is valid.
- The entry was first released as Swiss-Prot in 2025-04-09; the historical version 105 (entry version 105) already contained the subcellular location annotation based on PubMed:23834664 (2013), so the annotation predates the benchmark construction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal region 'LITAFSAIIVFAIFFLP' (~17 hydrophobic residues) is a classic single-pass transmembrane helix, indicating the protein is membrane-anchored. The large hydrophilic C-terminal domain (~400 residues) contains conserved motifs 'DDN', 'NIIAAT', 'DDNTG', 'NFWNAGVTAGL', 'GWDIDF' characteristic of peptidoglycan DD-endopeptidases (NlpC/P60 or related families). From knowledge of other peptidoglycan hydrolases (e.g., lysozymes, amidases, transpeptidases), these enzymes in bacteria are anchored to the inner membrane (plasma membrane) with catalytic domains facing the periplasm. This family-level inference distinguishes C (plasma membrane) from: B (ER membrane – a eukaryotic organelle; the sequence lacks ER signal peptides, KDEL retention signals, and the peptidoglycan hydrolase domain is exclusively bacterial); D (extracellular region – the TM helix means the protein is membrane-attached, and GO explicitly excludes surface-attached proteins from this term per GO1 definition); A (protein-containing complex – while the protein may participate in complexes, its primary subcellular location is the membrane, and the TM anchor is the defining feature).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The transmembrane helix is directly visible in the sequence, and the peptidoglycan hydrolase domain is recognizable by conserved motifs shared with other characterized bacterial cell-wall enzymes. Family-level knowledge that peptidoglycan hydrolases with TM anchors localize to the bacterial inner/plasma membrane provides a concrete, transferable inference that meaningfully distinguishes C from the other three options without requiring recall of this specific protein's database record."
  },
  "case_id": "GO_cellular_component_0044",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5",
      "GO3",
      "GO6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (Q9KU93, ShyC from Vibrio cholerae) annotates this protein as 'Cell inner membrane, Single-pass membrane protein, Periplasmic side' (C5/H4). In bacterial nomenclature, the inner membrane is the plasma membrane; GO:0005886 (plasma membrane) lists 'bacterial inner membrane' as a NARROW synonym (GO3). The direct GO annotation is GO:0098567 (periplasmic side of plasma membrane, IDA evidence, C6), which is_a GO:0009897, which is part_of GO:0005886 (ontology path confirmed). Additionally, GO:0005886 is assigned via IEA:UniProtKB-SubCell (H5). The author's answer 'plasma membrane' (C) is well-supported by the annotation evidence."
  },
  "important_caveats": [
    "The reviewer evidence confirms the organism is Vibrio cholerae (bacterium), but the model was not given this information. The bacterial inference must come from sequence features (peptidoglycan hydrolase domain, absence of eukaryotic targeting signals).",
    "The GO annotation for this protein is GO:0098567 (periplasmic side of plasma membrane) with IDA evidence; GO:0005886 (plasma membrane) is assigned via IEA (automatic). The author's choice of 'plasma membrane' is the parent term and is valid.",
    "The entry was first released as Swiss-Prot in 2025-04-09; the historical version 105 (entry version 105) already contained the subcellular location annotation based on PubMed:23834664 (2013), so the annotation predates the benchmark construction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The TM helix clearly excludes D (extracellular, defined as not attached to cell surface) and A (protein-containing complex is not a location per se). B (ER membrane) is excluded by the bacterial peptidoglycan hydrolase domain architecture and absence of ER-specific targeting features. C is the only option consistent with a single-pass membrane protein bearing a peptidoglycan hydrolase domain in a bacterial context."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0044",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (Q9KU93, ShyC from Vibrio cholerae) annotates this protein as 'Cell inner membrane, Single-pass membrane protein, Periplasmic side' (C5/H4). In bacterial nomenclature, the inner membrane is the plasma membrane; GO:0005886 (plasma membrane) lists 'bacterial inner membrane' as a NARROW synonym (GO3). The direct GO annotation is GO:0098567 (periplasmic side of plasma membrane, IDA evidence, C6), which is_a GO:0009897, which is part_of GO:0005886 (ontology path confirmed). Additionally, GO:0005886 is assigned via IEA:UniProtKB-SubCell (H5). The author's answer 'plasma membrane' (C) is well-supported by the annotation evidence.",
    "evidence_ids": ["C5", "C6", "H4", "H5", "GO3", "GO6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal region 'LITAFSAIIVFAIFFLP' (~17 hydrophobic residues) is a classic single-pass transmembrane helix, indicating the protein is membrane-anchored. The large hydrophilic C-terminal domain (~400 residues) contains conserved motifs 'DDN', 'NIIAAT', 'DDNTG', 'NFWNAGVTAGL', 'GWDIDF' characteristic of peptidoglycan DD-endopeptidases (NlpC/P60 or related families). From knowledge of other peptidoglycan hydrolases (e.g., lysozymes, amidases, transpeptidases), these enzymes in bacteria are anchored to the inner membrane (plasma membrane) with catalytic domains facing the periplasm. This family-level inference distinguishes C (plasma membrane) from: B (ER membrane – a eukaryotic organelle; the sequence lacks ER signal peptides, KDEL retention signals, and the peptidoglycan hydrolase domain is exclusively bacterial); D (extracellular region – the TM helix means the protein is membrane-attached, and GO explicitly excludes surface-attached proteins from this term per GO1 definition); A (protein-containing complex – while the protein may participate in complexes, its primary subcellular location is the membrane, and the TM anchor is the defining feature).",
    "missing_item_specific_fact": "",
    "reason": "The transmembrane helix is directly visible in the sequence, and the peptidoglycan hydrolase domain is recognizable by conserved motifs shared with other characterized bacterial cell-wall enzymes. Family-level knowledge that peptidoglycan hydrolases with TM anchors localize to the bacterial inner/plasma membrane provides a concrete, transferable inference that meaningfully distinguishes C from the other three options without requiring recall of this specific protein's database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The TM helix clearly excludes D (extracellular, defined as not attached to cell surface) and A (protein-containing complex is not a location per se). B (ER membrane) is excluded by the bacterial peptidoglycan hydrolase domain architecture and absence of ER-specific targeting features. C is the only option consistent with a single-pass membrane protein bearing a peptidoglycan hydrolase domain in a bacterial context."
  },
  "important_caveats": [
    "The reviewer evidence confirms the organism is Vibrio cholerae (bacterium), but the model was not given this information. The bacterial inference must come from sequence features (peptidoglycan hydrolase domain, absence of eukaryotic targeting signals).",
    "The GO annotation for this protein is GO:0098567 (periplasmic side of plasma membrane) with IDA evidence; GO:0005886 (plasma membrane) is assigned via IEA (automatic). The author's choice of 'plasma membrane' is the parent term and is valid.",
    "The entry was first released as Swiss-Prot in 2025-04-09; the historical version 105 (entry version 105) already contained the subcellular location annotation based on PubMed:23834664 (2013), so the annotation predates the benchmark construction."
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
  "requested_accession": "Q9KU93",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "888de842c37482558167fa97e9321ab347a672a53eb8aa7d6ae9b2562c828db3",
  "benchmark_sequence_length": 433,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 107,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2000-10-01",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "4c68a5a19b097a0a13e179bb05c32e6e535e30c5a35f230053fa015d7637a8eb",
  "current_source_sequence_sha256": "888de842c37482558167fa97e9321ab347a672a53eb8aa7d6ae9b2562c828db3",
  "current_source_sequence_length": 433,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 105,
  "selected_historical_version": {
    "accession": "Q9KU93",
    "database": "Swiss-Prot",
    "entryVersion": 105,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "SHYC_VIBCH",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "69827fcfb90c56fef1edc54124463fb027192860af52edf1a74b01902c49973c",
  "selected_historical_source_sequence_sha256": "888de842c37482558167fa97e9321ab347a672a53eb8aa7d6ae9b2562c828db3",
  "selected_historical_source_sequence_length": 433,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 105,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KU93.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KU93.json",
  "source_sha256": "4c68a5a19b097a0a13e179bb05c32e6e535e30c5a35f230053fa015d7637a8eb",
  "retrieved_utc": "2026-11-01T06:25:26.755646+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"Q9KU93\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KU93.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KU93.json",
  "source_sha256": "4c68a5a19b097a0a13e179bb05c32e6e535e30c5a35f230053fa015d7637a8eb",
  "retrieved_utc": "2026-11-01T06:25:26.755646+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":107,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2000-10-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KU93.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KU93.json",
  "source_sha256": "4c68a5a19b097a0a13e179bb05c32e6e535e30c5a35f230053fa015d7637a8eb",
  "retrieved_utc": "2026-11-01T06:25:26.755646+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAF93796.1\",\"source\":\"EMBL\"},{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000584\",\"source\":\"Proteomes\"}],\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Vibrionales\",\"Vibrionaceae\",\"Vibrio\"],\"scientificName\":\"Vibrio cholerae serotype O1 (strain ATCC 39315 / El Tor Inaba N16961)\",\"taxonId\":243277}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KU93.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KU93.json",
  "source_sha256": "4c68a5a19b097a0a13e179bb05c32e6e535e30c5a35f230053fa015d7637a8eb",
  "retrieved_utc": "2026-11-01T06:25:26.755646+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30782657\",\"source\":\"PubMed\"}],\"value\":\"Autolysin ShyC\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"23834664\",\"source\":\"PubMed\"}],\"value\":\"Sidewall hydrolase C\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30782657\",\"source\":\"PubMed\"}],\"value\":\"3.4.24.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30782657\",\"source\":\"PubMed\"}],\"value\":\"Peptidoglycan DD-endopeptidase ShyC\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KU93.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KU93.json",
  "source_sha256": "4c68a5a19b097a0a13e179bb05c32e6e535e30c5a35f230053fa015d7637a8eb",
  "retrieved_utc": "2026-11-01T06:25:26.755646+00:00",
  "json_pointer": "/comments/4",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23834664\",\"source\":\"PubMed\"}],\"value\":\"Localizes to the periphery of the cell and at the midcell in a subset of cells\"}]},\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"23834664\",\"source\":\"PubMed\"}],\"id\":\"SL-0037\",\"value\":\"Cell inner membrane\"},\"orientation\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"23834664\",\"source\":\"PubMed\"}],\"id\":\"SL-9916\",\"value\":\"Periplasmic side\"},\"topology\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"id\":\"SL-9904\",\"value\":\"Single-pass membrane protein\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KU93.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KU93.json",
  "source_sha256": "4c68a5a19b097a0a13e179bb05c32e6e535e30c5a35f230053fa015d7637a8eb",
  "retrieved_utc": "2026-11-01T06:25:26.755646+00:00",
  "json_pointer": "/uniProtKBCrossReferences/14",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"23834664\",\"source\":\"PubMed\"}],\"id\":\"GO:0098567\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:periplasmic side of plasma membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KU93.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KU93.json",
  "source_sha256": "4c68a5a19b097a0a13e179bb05c32e6e535e30c5a35f230053fa015d7637a8eb",
  "retrieved_utc": "2026-11-01T06:25:26.755646+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Doerr T.\",\"Cava F.\",\"Lam H.\",\"Davis B.M.\",\"Waldor M.K.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"23834664\"},{\"database\":\"DOI\",\"id\":\"10.1111/mmi.12323\"}],\"citationType\":\"journal article\",\"firstPage\":\"949\",\"id\":\"23834664\",\"journal\":\"Mol. Microbiol.\",\"lastPage\":\"962\",\"publicationDate\":\"2013\",\"title\":\"Substrate specificity of an elongation-specific peptidoglycan endopeptidase and its implications for cell wall architecture and growth of Vibrio cholerae.\",\"volume\":\"89\"},\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"23834664\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"ATCC 39315 / El Tor Inaba N16961\"}],\"referenceNumber\":2,\"referencePositions\":[\"SUBCELLULAR LOCATION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KU93.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KU93.json",
  "source_sha256": "4c68a5a19b097a0a13e179bb05c32e6e535e30c5a35f230053fa015d7637a8eb",
  "retrieved_utc": "2026-11-01T06:25:26.755646+00:00",
  "json_pointer": "/references/2",
  "excerpt": "{\"citation\":{\"authors\":[\"Murphy S.G.\",\"Alvarez L.\",\"Adams M.C.\",\"Liu S.\",\"Chappie J.S.\",\"Cava F.\",\"Doerr T.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30782657\"},{\"database\":\"DOI\",\"id\":\"10.1128/mbio.02620-18\"}],\"citationType\":\"journal article\",\"firstPage\":\"0\",\"id\":\"30782657\",\"journal\":\"MBio\",\"lastPage\":\"0\",\"publicationDate\":\"2019\",\"title\":\"Endopeptidase Regulation as a Novel Function of the Zur-Dependent Zinc Starvation Response.\",\"volume\":\"10\"},\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30782657\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"ATCC 39315 / El Tor Inaba N16961\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"PATHWAY\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KU93?format=txt&versions=105)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9KU93?format=txt&versions=105",
  "source_sha256": "69827fcfb90c56fef1edc54124463fb027192860af52edf1a74b01902c49973c",
  "retrieved_utc": "2026-11-01T06:28:46.934559+00:00",
  "source_locator": "lines 1-16",
  "excerpt": "ID   SHYC_VIBCH              Reviewed;         433 AA.\nAC   Q9KU93;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-OCT-2000, sequence version 1.\nDT   28-JAN-2026, entry version 105.\nDE   RecName: Full=Peptidoglycan DD-endopeptidase ShyC {ECO:0000303|PubMed:30782657};\nDE            EC=3.4.24.- {ECO:0000269|PubMed:30782657};\nDE   AltName: Full=Autolysin ShyC {ECO:0000303|PubMed:30782657};\nDE   AltName: Full=Sidewall hydrolase C {ECO:0000303|PubMed:23834664};\nGN   Name=shyC {ECO:0000303|PubMed:23834664, ECO:0000303|PubMed:30782657};\nGN   OrderedLocusNames=VC_0630 {ECO:0000303|PubMed:23834664,\nGN   ECO:0000312|EMBL:AAF93796.1};\nOS   Vibrio cholerae serotype O1 (strain ATCC 39315 / El Tor Inaba N16961).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria; Vibrionales;\nOC   Vibrionaceae; Vibrio.\nOX   NCBI_TaxID=243277 {ECO:0000312|EMBL:AAF93796.1, ECO:0000312|Proteomes:UP000000584};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 105,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KU93?format=txt&versions=105)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9KU93?format=txt&versions=105",
  "source_sha256": "69827fcfb90c56fef1edc54124463fb027192860af52edf1a74b01902c49973c",
  "retrieved_utc": "2026-11-01T06:28:46.934559+00:00",
  "source_locator": "lines 31-39",
  "excerpt": "RN   [2]\nRP   SUBCELLULAR LOCATION, AND DISRUPTION PHENOTYPE.\nRC   STRAIN=ATCC 39315 / El Tor Inaba N16961 {ECO:0000303|PubMed:23834664};\nRX   PubMed=23834664; DOI=10.1111/mmi.12323;\nRA   Doerr T., Cava F., Lam H., Davis B.M., Waldor M.K.;\nRT   \"Substrate specificity of an elongation-specific peptidoglycan\nRT   endopeptidase and its implications for cell wall architecture and growth of\nRT   Vibrio cholerae.\";\nRL   Mol. Microbiol. 89:949-962(2013).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 105,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KU93?format=txt&versions=105)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9KU93?format=txt&versions=105",
  "source_sha256": "69827fcfb90c56fef1edc54124463fb027192860af52edf1a74b01902c49973c",
  "retrieved_utc": "2026-11-01T06:28:46.934559+00:00",
  "source_locator": "lines 40-49",
  "excerpt": "RN   [3]\nRP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, PATHWAY, AND DISRUPTION\nRP   PHENOTYPE.\nRC   STRAIN=ATCC 39315 / El Tor Inaba N16961 {ECO:0000303|PubMed:30782657};\nRX   PubMed=30782657; DOI=10.1128/mbio.02620-18;\nRA   Murphy S.G., Alvarez L., Adams M.C., Liu S., Chappie J.S., Cava F.,\nRA   Doerr T.;\nRT   \"Endopeptidase Regulation as a Novel Function of the Zur-Dependent Zinc\nRT   Starvation Response.\";\nRL   MBio 10:0-0(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 105,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KU93?format=txt&versions=105)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9KU93?format=txt&versions=105",
  "source_sha256": "69827fcfb90c56fef1edc54124463fb027192860af52edf1a74b01902c49973c",
  "retrieved_utc": "2026-11-01T06:28:46.934559+00:00",
  "source_locator": "lines 64-68",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Cell inner membrane\nCC       {ECO:0000305|PubMed:23834664}; Single-pass membrane protein\nCC       {ECO:0000255}; Periplasmic side {ECO:0000305|PubMed:23834664}.\nCC       Note=Localizes to the periphery of the cell and at the midcell in a\nCC       subset of cells. {ECO:0000269|PubMed:23834664}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 105,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KU93?format=txt&versions=105)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9KU93?format=txt&versions=105",
  "source_sha256": "69827fcfb90c56fef1edc54124463fb027192860af52edf1a74b01902c49973c",
  "retrieved_utc": "2026-11-01T06:28:46.934559+00:00",
  "source_locator": "lines 93-93",
  "excerpt": "DR   GO; GO:0005886; C:plasma membrane; IEA:UniProtKB-SubCell.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 105,
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
  "source_locator": "lines 57481-57505",
  "excerpt": "[Term]\nid: GO:0005576\nname: extracellular region\nnamespace: cellular_component\ndef: \"The space external to the outermost structure of a cell. For cells without external protective or external encapsulating structures this refers to space outside of the plasma membrane. This term covers the host cell environment outside an intracellular parasite.\" [GOC:curators]\ncomment: Note that this term is intended to annotate gene products that are not attached to the cell surface. For gene products at the cell surface, consider annotating to external side of plasma membrane ; GO:0009897.\nsubset: goslim_agr\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_flybase_ribbon\nsubset: goslim_generic\nsubset: goslim_metagenomics\nsubset: goslim_mouse\nsubset: goslim_pir\nsubset: goslim_plant\nsubset: goslim_plant_ribbon\nsubset: goslim_prokaryote\nsubset: goslim_prokaryote_ribbon\nsubset: goslim_yeast\nsynonym: \"extracellular\" EXACT []\nxref: Wikipedia:Extracellular\nis_a: GO:0110165 ! cellular anatomical structure\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0005576"
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
  "source_locator": "lines 59526-59535",
  "excerpt": "[Term]\nid: GO:0005789\nname: endoplasmic reticulum membrane\nnamespace: cellular_component\ndef: \"The lipid bilayer surrounding the endoplasmic reticulum.\" [GOC:mah]\nsynonym: \"ER membrane\" EXACT []\nis_a: GO:0031090 ! organelle membrane\nrelationship: part_of GO:0042175 ! nuclear outer membrane-endoplasmic reticulum membrane network\nrelationship: part_of GO:0098827 ! endoplasmic reticulum subcompartment\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0005789"
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
  "source_locator": "lines 60420-60454",
  "excerpt": "[Term]\nid: GO:0005886\nname: plasma membrane\nnamespace: cellular_component\nalt_id: GO:0005887\nalt_id: GO:0005904\ndef: \"The membrane surrounding a cell that separates the cell from its external environment. It consists of a phospholipid bilayer and associated proteins.\" [ISBN:0716731363]\nsubset: goslim_agr\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_generic\nsubset: goslim_metagenomics\nsubset: goslim_mouse\nsubset: goslim_plant\nsubset: goslim_plant_ribbon\nsubset: goslim_prokaryote\nsubset: goslim_prokaryote_ribbon\nsubset: goslim_yeast\nsynonym: \"bacterial inner membrane\" NARROW []\nsynonym: \"cell membrane\" EXACT []\nsynonym: \"cellular membrane\" EXACT [NIF_Subcellular:sao6433132645]\nsynonym: \"cytoplasmic membrane\" EXACT []\nsynonym: \"inner endospore membrane\" NARROW []\nsynonym: \"integral component of plasma membrane\" NARROW []\nsynonym: \"integral to plasma membrane\" NARROW []\nsynonym: \"juxtamembrane\" BROAD []\nsynonym: \"plasma membrane lipid bilayer\" NARROW [GOC:mah]\nsynonym: \"plasmalemma\" EXACT []\nxref: NIF_Subcellular:sao1663586795\nxref: Wikipedia:Cell_membrane\nis_a: GO:0016020 ! membrane\nrelationship: part_of GO:0071944 ! cell periphery\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0005886"
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
  "source_locator": "lines 100773-100784",
  "excerpt": "[Term]\nid: GO:0009897\nname: external side of plasma membrane\nnamespace: cellular_component\ndef: \"The leaflet of the plasma membrane that faces the extracellular side of the cell, including any protein embedded in, attached to, or peripherally associated with it.\" [GOC:dos, GOC:tb]\nsynonym: \"external leaflet of plasma membrane\" EXACT [GOC:ab]\nsynonym: \"juxtamembrane\" BROAD []\nsynonym: \"outer surface of cytoplasmic membrane\" EXACT []\nis_a: GO:0098552 ! side of membrane\nrelationship: part_of GO:0005886 ! plasma membrane\nrelationship: part_of GO:0009986 ! cell surface\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0009897"
}
```

### Evidence GO5

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO5",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 192667-192686",
  "excerpt": "[Term]\nid: GO:0032991\nname: protein-containing complex\nnamespace: cellular_component\nalt_id: GO:0043234\ndef: \"A stable assembly of two or more macromolecules, i.e. proteins, nucleic acids, carbohydrates or lipids, in which at least one component is a protein and the constituent parts function together.\" [GOC:dos, GOC:mah]\ncomment: A protein complex in this context is meant as a stable set of interacting proteins which can be co-purified by an acceptable method, and where the complex has been shown to exist as an isolated, functional unit in vivo. Acceptable experimental methods include stringent protein purification followed by detection of protein interaction. The following methods should be considered non-acceptable: simple immunoprecipitation, pull-down experiments from cell extracts without further purification, colocalization and 2-hybrid screening. Interactions that should not be captured as protein complexes include: 1) enzyme/substrate, receptor/ligand or any similar transient interactions, unless these are a critical part of the complex assembly or are required e.g. for the receptor to be functional; 2) proteins associated in a pull-down/co-immunoprecipitation assay with no functional link or any evidence that this is a defined biological entity rather than a loose-affinity complex; 3) any complex where the only evidence is based on genetic interaction data; 4) partial complexes, where some subunits (e.g. transmembrane ones) cannot be expressed as recombinant proteins and are excluded from experiments (in this case, independent evidence is necessary to find out the composition of the full complex, if known). Interactions that may be captured as protein complexes include: 1) enzyme/substrate or receptor/ligand if the complex can only assemble and become functional in the presence of both classes of subunits; 2) complexes where one of the members has not been shown to be physically linked to the other(s), but is a homologue of, and has the same functionality as, a protein that has been experimentally demonstrated to form a complex with the other member(s); 3) complexes whose existence is accepted based on localization and pharmacological studies, but for which experimental evidence is not yet available for the complex as a whole.\nsubset: goslim_agr\nsubset: goslim_chembl\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_flybase_ribbon\nsubset: goslim_mouse\nsubset: goslim_pir\nsynonym: \"macromolecular complex\" EXACT []\nsynonym: \"macromolecule complex\" EXACT []\nsynonym: \"protein complex\" NARROW []\nsynonym: \"protein containing complex\" EXACT []\nsynonym: \"protein-protein complex\" NARROW []\nis_a: GO:0005575 ! cellular_component\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0032991"
}
```

### Evidence GO6

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO6",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 409072-409078",
  "excerpt": "[Term]\nid: GO:0098567\nname: periplasmic side of plasma membrane\nnamespace: cellular_component\ndef: \"The leaflet of the plasma membrane that faces the periplasm, including any protein embedded in, attached to, or peripherally associated with it.\" [GOC:dos]\nis_a: GO:0009897 ! external side of plasma membrane\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0098567"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 44. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
