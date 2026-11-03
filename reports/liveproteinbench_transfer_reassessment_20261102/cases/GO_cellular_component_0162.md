# GO_cellular_component_0162: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/GO_cellular_component_0162.txt)

**Task:** `GO_cellular_component`  
**Author key, unchanged:** **C** — plasma membrane

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
MQVTSLLILVCFIAAFQVFSRASSPVNCKWDSYGPWSECNGCTKTQTRRRSVAVYGQYGGYPCEGSAFETQSCKPERGCPTEEGCGDRFRCFSGQCISKSLVCNGDPDCEEDGADEDKCENVANPSCNIDKPPPNIELTGYGYNVVTGQGKKRVINTKSFGGQCRKVFSGDGKDFYRLSGNILSYTFQVKVDNDFNYEFYNSSWSYIKHTSTEQNTFYSWKGLFSHSRNTYGHGSAKEEIDTKMKSYKLLVVQNTVEVAQFTNNNPEFLQVAEPFWKELSHLPTLYDYSAYRRLIDQYGTHYLQSGSLGGEYRVLFYVDSGSAKETGFQSDQDNACSSADFQFLFTSSADQRCMKQLETEKSTSGNKGRLLRGKPLVRGGDSGFVADLSFLDLDNPAGNKQRYSSWAGSVTRLPQVIKEKLAPLYELVKEVPCASVKRLYLKRAIEEYFDEFDPCHCRPCQNGGLAIVVETQCQCLCKPYTFGSACEQGVLVGDQAGGVDGGWNCWSSWSPCVQGKRTRSRECNNPPPRDDGKSCLGETTESKQCEDQDLEKLRLLEPHCFHSSLAPKEFCLSPPALKDGFVQGEGTMVPVGQSVVYACDEGYSLIGDPVARCGEDLQWLVGEMHCQKLACVLPGEMNGMQSHPQKPFYMVGEKVTLSCVGGMSLEGPSTLLCGSSLKWSPELKDAKCVQKATSTPPPAAPACQPWEKLQNSKCICKMPYECGSSLDVCARDESRNKILSLTICKMHVVHCHKRNYTLVGKESCTLPSPAEKVCGACPIWSKCDAQNGKCICREASECQTAGYRICVEVNGKEETMSECEAGILRCRGQSISITAIKPCAEEAAQ

[Multiple Choices]
A. host cell nucleus
B. P-body
C. plasma membrane
D. perinuclear region of cytoplasm
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

> The sequence matches mouse complement component C7. Its annotation says it is secreted as a soluble protein and inserts into the target-cell membrane; a GO annotation also places it at the plasma membrane. This supports C among the listed choices, with the qualification that membrane insertion occurs in the complement context.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C9](#evidence-c9), [H2](#evidence-h2), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic signal peptide supports entry into the secretory pathway, making a cytosolic P-body or nuclear location unlikely. But secretion alone does not distinguish plasma-membrane insertion from other extracellular fates.


**Missing item-specific fact**

> The fact that this particular protein is complement C7, a soluble secreted protein that inserts into target-cell membranes as part of complement activity.


**Reason**

> The sequence offers broad clues about secretion, but selecting plasma membrane over the other options requires protein-specific functional or localization knowledge not supplied in the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> C is supported by the target-cell membrane annotation. However, the protein is also described as secreted and soluble, so plasma membrane should not be read as evidence that it is a constitutive plasma-membrane resident.


### Important caveats

- The subcellular-location annotation is transferred from human C7 (ECO:0000250); the plasma-membrane GO annotation is NAS:ComplexPortal.
- The sequence match and annotation support the key, but the question's use of “primary” location is imprecise for a protein secreted in soluble form that inserts into target-cell membranes.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic signal peptide supports entry into the secretory pathway, making a cytosolic P-body or nuclear location unlikely. But secretion alone does not distinguish plasma-membrane insertion from other extracellular fates.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The fact that this particular protein is complement C7, a soluble secreted protein that inserts into target-cell membranes as part of complement activity.",
    "reason": "The sequence offers broad clues about secretion, but selecting plasma membrane over the other options requires protein-specific functional or localization knowledge not supplied in the question."
  },
  "case_id": "GO_cellular_component_0162",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C9",
      "H2",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence matches mouse complement component C7. Its annotation says it is secreted as a soluble protein and inserts into the target-cell membrane; a GO annotation also places it at the plasma membrane. This supports C among the listed choices, with the qualification that membrane insertion occurs in the complement context."
  },
  "important_caveats": [
    "The subcellular-location annotation is transferred from human C7 (ECO:0000250); the plasma-membrane GO annotation is NAS:ComplexPortal.",
    "The sequence match and annotation support the key, but the question's use of “primary” location is imprecise for a protein secreted in soluble form that inserts into target-cell membranes."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "C is supported by the target-cell membrane annotation. However, the protein is also described as secreted and soluble, so plasma membrane should not be read as evidence that it is a constitutive plasma-membrane resident."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0162",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches mouse complement component C7. Its annotation says it is secreted as a soluble protein and inserts into the target-cell membrane; a GO annotation also places it at the plasma membrane. This supports C among the listed choices, with the qualification that membrane insertion occurs in the complement context.",
    "evidence_ids": ["C4", "C5", "C9", "H2", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic signal peptide supports entry into the secretory pathway, making a cytosolic P-body or nuclear location unlikely. But secretion alone does not distinguish plasma-membrane insertion from other extracellular fates.",
    "missing_item_specific_fact": "The fact that this particular protein is complement C7, a soluble secreted protein that inserts into target-cell membranes as part of complement activity.",
    "reason": "The sequence offers broad clues about secretion, but selecting plasma membrane over the other options requires protein-specific functional or localization knowledge not supplied in the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "C is supported by the target-cell membrane annotation. However, the protein is also described as secreted and soluble, so plasma membrane should not be read as evidence that it is a constitutive plasma-membrane resident."
  },
  "important_caveats": [
    "The subcellular-location annotation is transferred from human C7 (ECO:0000250); the plasma-membrane GO annotation is NAS:ComplexPortal.",
    "The sequence match and annotation support the key, but the question's use of “primary” location is imprecise for a protein secreted in soluble form that inserts into target-cell membranes."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry for D3YXF5 (Complement component C7, Mus musculus) directly annotates GO:0005886 (plasma membrane) with NAS:ComplexPortal evidence (C9/H6). The subcellular location comment states 'Secreted as soluble protein. Inserts into the cell membrane of target cells' (C5/H2). GO:0005579 (membrane attack complex) is annotated (C7/H4) and the ontology path confirms MAC is_a plasma membrane protein complex (GO:0098797) which is part_of GO:0005886 (plasma membrane). The evidence is primarily computational/transferred (ECO:0000250, NAS, ISO), not direct experimental localization, but it consistently supports plasma membrane as the functional compartment.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [C9](#evidence-c9), [H2](#evidence-h2), [H4](#evidence-h4), [H6](#evidence-h6), [GO2](#evidence-go2), [GO3](#evidence-go3), [GO6](#evidence-go6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal sequence MQVTSLLILVCFIAAFQVFSRA is a canonical hydrophobic signal peptide, indicating the protein enters the secretory pathway. This eliminates all intracellular compartments: nuclear proteins carry NLS motifs (not signal peptides), P-body proteins are cytoplasmic, and perinuclear cytoplasm proteins lack signal peptides. Additionally, the protein architecture contains multiple CCP/Sushi domains and a MACPF (membrane attack complex/perforin) domain — identifiable by their characteristic cysteine spacing and fold motifs — which are hallmarks of terminal complement components that insert into target cell membranes. Among the four options, only 'plasma membrane' is consistent with a signal-peptide-bearing, membrane-inserting secreted protein.


**Missing item-specific fact**

> None critical. A model needs to recognize the signal peptide and the MACPF/complement domain architecture, which are general protein-targeting and domain-level knowledge, not an item-specific database lookup.


**Reason**

> The signal peptide alone eliminates options A, B, and D by basic protein-targeting logic. The MACPF domain further supports membrane insertion. This constitutes a concrete biological argument from the sequence that meaningfully distinguishes C from the other choices without requiring memorization of this specific protein's GO annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The signal peptide and MACPF domain architecture clearly point to a secreted/membrane-inserting protein. Options A (host cell nucleus), B (P-body), and D (perinuclear region of cytoplasm) are all intracellular compartments incompatible with a signal-peptide-containing secretory protein. No other option is defensible given the sequence features.


### Important caveats

- The GO:0005886 annotation carries NAS (non-traceable author statement from ComplexPortal) evidence, not direct experimental localization. The 'plasma membrane' refers to the target cell membrane after MAC insertion, not the producing cell's membrane.
- C7 is also annotated as 'Secreted' and 'extracellular region' (GO:0005576, ISS). If 'extracellular' had been an option, it would compete with 'plasma membrane.' The question's four options do not include an extracellular choice, making plasma membrane the best fit.
- The subcellular location annotation is transferred by similarity (ECO:0000250 from human C7, P10643), not independently experimentally validated for the mouse protein.
- The sequence-match is confirmed against both current (v113) and historical (v111) UniProt entries; the benchmark sequence is canonical 845-aa precursor.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal sequence MQVTSLLILVCFIAAFQVFSRA is a canonical hydrophobic signal peptide, indicating the protein enters the secretory pathway. This eliminates all intracellular compartments: nuclear proteins carry NLS motifs (not signal peptides), P-body proteins are cytoplasmic, and perinuclear cytoplasm proteins lack signal peptides. Additionally, the protein architecture contains multiple CCP/Sushi domains and a MACPF (membrane attack complex/perforin) domain — identifiable by their characteristic cysteine spacing and fold motifs — which are hallmarks of terminal complement components that insert into target cell membranes. Among the four options, only 'plasma membrane' is consistent with a signal-peptide-bearing, membrane-inserting secreted protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. A model needs to recognize the signal peptide and the MACPF/complement domain architecture, which are general protein-targeting and domain-level knowledge, not an item-specific database lookup.",
    "reason": "The signal peptide alone eliminates options A, B, and D by basic protein-targeting logic. The MACPF domain further supports membrane insertion. This constitutes a concrete biological argument from the sequence that meaningfully distinguishes C from the other choices without requiring memorization of this specific protein's GO annotation."
  },
  "case_id": "GO_cellular_component_0162",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "C9",
      "H2",
      "H4",
      "H6",
      "GO2",
      "GO3",
      "GO6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry for D3YXF5 (Complement component C7, Mus musculus) directly annotates GO:0005886 (plasma membrane) with NAS:ComplexPortal evidence (C9/H6). The subcellular location comment states 'Secreted as soluble protein. Inserts into the cell membrane of target cells' (C5/H2). GO:0005579 (membrane attack complex) is annotated (C7/H4) and the ontology path confirms MAC is_a plasma membrane protein complex (GO:0098797) which is part_of GO:0005886 (plasma membrane). The evidence is primarily computational/transferred (ECO:0000250, NAS, ISO), not direct experimental localization, but it consistently supports plasma membrane as the functional compartment."
  },
  "important_caveats": [
    "The GO:0005886 annotation carries NAS (non-traceable author statement from ComplexPortal) evidence, not direct experimental localization. The 'plasma membrane' refers to the target cell membrane after MAC insertion, not the producing cell's membrane.",
    "C7 is also annotated as 'Secreted' and 'extracellular region' (GO:0005576, ISS). If 'extracellular' had been an option, it would compete with 'plasma membrane.' The question's four options do not include an extracellular choice, making plasma membrane the best fit.",
    "The subcellular location annotation is transferred by similarity (ECO:0000250 from human C7, P10643), not independently experimentally validated for the mouse protein.",
    "The sequence-match is confirmed against both current (v113) and historical (v111) UniProt entries; the benchmark sequence is canonical 845-aa precursor."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The signal peptide and MACPF domain architecture clearly point to a secreted/membrane-inserting protein. Options A (host cell nucleus), B (P-body), and D (perinuclear region of cytoplasm) are all intracellular compartments incompatible with a signal-peptide-containing secretory protein. No other option is defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0162",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry for D3YXF5 (Complement component C7, Mus musculus) directly annotates GO:0005886 (plasma membrane) with NAS:ComplexPortal evidence (C9/H6). The subcellular location comment states 'Secreted as soluble protein. Inserts into the cell membrane of target cells' (C5/H2). GO:0005579 (membrane attack complex) is annotated (C7/H4) and the ontology path confirms MAC is_a plasma membrane protein complex (GO:0098797) which is part_of GO:0005886 (plasma membrane). The evidence is primarily computational/transferred (ECO:0000250, NAS, ISO), not direct experimental localization, but it consistently supports plasma membrane as the functional compartment.",
    "evidence_ids": ["C5", "C7", "C9", "H2", "H4", "H6", "GO2", "GO3", "GO6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal sequence MQVTSLLILVCFIAAFQVFSRA is a canonical hydrophobic signal peptide, indicating the protein enters the secretory pathway. This eliminates all intracellular compartments: nuclear proteins carry NLS motifs (not signal peptides), P-body proteins are cytoplasmic, and perinuclear cytoplasm proteins lack signal peptides. Additionally, the protein architecture contains multiple CCP/Sushi domains and a MACPF (membrane attack complex/perforin) domain — identifiable by their characteristic cysteine spacing and fold motifs — which are hallmarks of terminal complement components that insert into target cell membranes. Among the four options, only 'plasma membrane' is consistent with a signal-peptide-bearing, membrane-inserting secreted protein.",
    "missing_item_specific_fact": "None critical. A model needs to recognize the signal peptide and the MACPF/complement domain architecture, which are general protein-targeting and domain-level knowledge, not an item-specific database lookup.",
    "reason": "The signal peptide alone eliminates options A, B, and D by basic protein-targeting logic. The MACPF domain further supports membrane insertion. This constitutes a concrete biological argument from the sequence that meaningfully distinguishes C from the other choices without requiring memorization of this specific protein's GO annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The signal peptide and MACPF domain architecture clearly point to a secreted/membrane-inserting protein. Options A (host cell nucleus), B (P-body), and D (perinuclear region of cytoplasm) are all intracellular compartments incompatible with a signal-peptide-containing secretory protein. No other option is defensible given the sequence features."
  },
  "important_caveats": [
    "The GO:0005886 annotation carries NAS (non-traceable author statement from ComplexPortal) evidence, not direct experimental localization. The 'plasma membrane' refers to the target cell membrane after MAC insertion, not the producing cell's membrane.",
    "C7 is also annotated as 'Secreted' and 'extracellular region' (GO:0005576, ISS). If 'extracellular' had been an option, it would compete with 'plasma membrane.' The question's four options do not include an extracellular choice, making plasma membrane the best fit.",
    "The subcellular location annotation is transferred by similarity (ECO:0000250 from human C7, P10643), not independently experimentally validated for the mouse protein.",
    "The sequence-match is confirmed against both current (v113) and historical (v111) UniProt entries; the benchmark sequence is canonical 845-aa precursor."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The exact sequence matches an entry annotated as a soluble secreted protein that inserts into target-cell membranes. Its plasma-membrane GO annotation is consistent with that target-membrane association, though it does not mean the protein is a constitutive membrane resident. The location annotation is partly transferred from a homolog, and the GO annotation is attributed to ComplexPortal rather than demonstrated here as a direct experiment.

Citations as saved: [C5](#evidence-c5), [C9](#evidence-c9), [H2](#evidence-h2), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence begins with a hydrophobic N-terminal signal peptide and has no evident later transmembrane segment, favoring a secreted protein over a nuclear, P-body, or perinuclear protein. Its long cysteine-rich regions and C-terminal membrane-attack-complex/perforin-like region are consistent with a complement terminal-pathway protein; transferable knowledge that such proteins can be secreted and then assemble at target membranes makes plasma membrane the meaningful best choice among the offered options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence features and family-level inference provide a concrete basis for choosing C over the intracellular alternatives. The inference is probabilistic, and the choices omit the protein's soluble extracellular state, but exact-protein annotation is not necessary to distinguish the offered answers.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The protein can be secreted and subsequently associate with target-cell membranes, but secretion/extracellular space is not an option. Of the listed choices, plasma membrane is the best-supported location.


### Important caveats

- The source annotation describes insertion into target-cell membranes, not constitutive residence in the protein-producing cell's plasma membrane.
- The supplied evidence includes a homolog-transferred subcellular-location annotation and a GO annotation; it does not independently establish the timing or extent of membrane association.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence begins with a hydrophobic N-terminal signal peptide and has no evident later transmembrane segment, favoring a secreted protein over a nuclear, P-body, or perinuclear protein. Its long cysteine-rich regions and C-terminal membrane-attack-complex/perforin-like region are consistent with a complement terminal-pathway protein; transferable knowledge that such proteins can be secreted and then assemble at target membranes makes plasma membrane the meaningful best choice among the offered options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence features and family-level inference provide a concrete basis for choosing C over the intracellular alternatives. The inference is probabilistic, and the choices omit the protein's soluble extracellular state, but exact-protein annotation is not necessary to distinguish the offered answers."
  },
  "case_id": "GO_cellular_component_0162",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C9",
      "H2",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches an entry annotated as a soluble secreted protein that inserts into target-cell membranes. Its plasma-membrane GO annotation is consistent with that target-membrane association, though it does not mean the protein is a constitutive membrane resident. The location annotation is partly transferred from a homolog, and the GO annotation is attributed to ComplexPortal rather than demonstrated here as a direct experiment."
  },
  "important_caveats": [
    "The source annotation describes insertion into target-cell membranes, not constitutive residence in the protein-producing cell's plasma membrane.",
    "The supplied evidence includes a homolog-transferred subcellular-location annotation and a GO annotation; it does not independently establish the timing or extent of membrane association."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein can be secreted and subsequently associate with target-cell membranes, but secretion/extracellular space is not an option. Of the listed choices, plasma membrane is the best-supported location."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0162",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches an entry annotated as a soluble secreted protein that inserts into target-cell membranes. Its plasma-membrane GO annotation is consistent with that target-membrane association, though it does not mean the protein is a constitutive membrane resident. The location annotation is partly transferred from a homolog, and the GO annotation is attributed to ComplexPortal rather than demonstrated here as a direct experiment.",
    "evidence_ids": ["C5", "C9", "H2", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence begins with a hydrophobic N-terminal signal peptide and has no evident later transmembrane segment, favoring a secreted protein over a nuclear, P-body, or perinuclear protein. Its long cysteine-rich regions and C-terminal membrane-attack-complex/perforin-like region are consistent with a complement terminal-pathway protein; transferable knowledge that such proteins can be secreted and then assemble at target membranes makes plasma membrane the meaningful best choice among the offered options.",
    "missing_item_specific_fact": "",
    "reason": "The sequence features and family-level inference provide a concrete basis for choosing C over the intracellular alternatives. The inference is probabilistic, and the choices omit the protein's soluble extracellular state, but exact-protein annotation is not necessary to distinguish the offered answers."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein can be secreted and subsequently associate with target-cell membranes, but secretion/extracellular space is not an option. Of the listed choices, plasma membrane is the best-supported location."
  },
  "important_caveats": [
    "The source annotation describes insertion into target-cell membranes, not constitutive residence in the protein-producing cell's plasma membrane.",
    "The supplied evidence includes a homolog-transferred subcellular-location annotation and a GO annotation; it does not independently establish the timing or extent of membrane association."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry D3YXF5 (Complement component C7, mouse) directly annotates GO:0005886 (plasma membrane) with NAS:ComplexPortal evidence (C9/H6). The subcellular location comment states the protein is 'Secreted as soluble protein. Inserts into the cell membrane of target cells' (C5/H2). Additionally, the membrane attack complex annotation (GO:0005579) is_a GO:0098797 (plasma membrane protein complex), which is part_of GO:0005886 (plasma membrane), providing an ontological path to plasma membrane. The author's answer of 'plasma membrane' is directly supported by the GO annotation and the functional description of C7 inserting into target cell membranes as part of the MAC.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [C9](#evidence-c9), [H2](#evidence-h2), [H4](#evidence-h4), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal sequence MQVTSLLILVCFIAAFQVFSRA is a classic hydrophobic signal peptide (a stretch of ~20 hydrophobic residues at the extreme N-terminus), which is the universal targeting signal for entry into the ER/secretory pathway. This immediately eliminates P-body (B, a cytoplasmic mRNA-processing granule), perinuclear region of cytoplasm (D, a cytoplasmic location), and host cell nucleus (A, an intracellular compartment typically relevant to viral proteins). A secreted protein cannot reside in the cytoplasm or nucleus. Among the four choices, only plasma membrane (C) is compatible with a secreted protein that subsequently associates with a membrane. Additionally, the large size (~845 aa) and the presence of multiple cysteine-rich domain repeats (Sushi/CCP, LDL-receptor class A, TSP type 1 domains) are hallmarks of complement pathway components, which are well-known secreted proteins that insert into target cell membranes during MAC assembly. This family-level knowledge, combined with the visible signal peptide, uniquely selects C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The N-terminal signal peptide is directly readable from the provided sequence and is a fundamental, transferable feature of secretory proteins. The general principle that signal peptides direct proteins away from the cytoplasm and nucleus eliminates options A, B, and D. The remaining option C (plasma membrane) is the only choice consistent with a secreted protein, and complement components' well-known role in membrane insertion provides further support. No target-specific annotation lookup is required.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The signal peptide unambiguously indicates secretion, which is incompatible with the three intracellular/cytoplasmic options (A, B, D). Among the four given choices, only plasma membrane is compatible with a secreted protein. While one could argue the 'primary' location of C7 is extracellular (it circulates in plasma), 'extracellular region' is not among the options, and plasma membrane is the only viable choice. No ambiguity among the offered alternatives.


### Important caveats

- C7 is primarily a circulating secreted protein; its association with the plasma membrane is transient (during MAC assembly on target cells). The GO annotation GO:0005886 is supported by ComplexPortal (NAS), reflecting the MAC complex context rather than a constitutive membrane residence.
- The GO term 'host cell nucleus' (GO:0042025) is typically used in the context of viral proteins exploiting host machinery, making it an implausible distractor for a mammalian secreted complement component.
- The signal peptide is the strongest and most transferable discriminator; no target-specific database lookup is needed to reach the answer.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal sequence MQVTSLLILVCFIAAFQVFSRA is a classic hydrophobic signal peptide (a stretch of ~20 hydrophobic residues at the extreme N-terminus), which is the universal targeting signal for entry into the ER/secretory pathway. This immediately eliminates P-body (B, a cytoplasmic mRNA-processing granule), perinuclear region of cytoplasm (D, a cytoplasmic location), and host cell nucleus (A, an intracellular compartment typically relevant to viral proteins). A secreted protein cannot reside in the cytoplasm or nucleus. Among the four choices, only plasma membrane (C) is compatible with a secreted protein that subsequently associates with a membrane. Additionally, the large size (~845 aa) and the presence of multiple cysteine-rich domain repeats (Sushi/CCP, LDL-receptor class A, TSP type 1 domains) are hallmarks of complement pathway components, which are well-known secreted proteins that insert into target cell membranes during MAC assembly. This family-level knowledge, combined with the visible signal peptide, uniquely selects C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The N-terminal signal peptide is directly readable from the provided sequence and is a fundamental, transferable feature of secretory proteins. The general principle that signal peptides direct proteins away from the cytoplasm and nucleus eliminates options A, B, and D. The remaining option C (plasma membrane) is the only choice consistent with a secreted protein, and complement components' well-known role in membrane insertion provides further support. No target-specific annotation lookup is required."
  },
  "case_id": "GO_cellular_component_0162",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "C9",
      "H2",
      "H4",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry D3YXF5 (Complement component C7, mouse) directly annotates GO:0005886 (plasma membrane) with NAS:ComplexPortal evidence (C9/H6). The subcellular location comment states the protein is 'Secreted as soluble protein. Inserts into the cell membrane of target cells' (C5/H2). Additionally, the membrane attack complex annotation (GO:0005579) is_a GO:0098797 (plasma membrane protein complex), which is part_of GO:0005886 (plasma membrane), providing an ontological path to plasma membrane. The author's answer of 'plasma membrane' is directly supported by the GO annotation and the functional description of C7 inserting into target cell membranes as part of the MAC."
  },
  "important_caveats": [
    "C7 is primarily a circulating secreted protein; its association with the plasma membrane is transient (during MAC assembly on target cells). The GO annotation GO:0005886 is supported by ComplexPortal (NAS), reflecting the MAC complex context rather than a constitutive membrane residence.",
    "The GO term 'host cell nucleus' (GO:0042025) is typically used in the context of viral proteins exploiting host machinery, making it an implausible distractor for a mammalian secreted complement component.",
    "The signal peptide is the strongest and most transferable discriminator; no target-specific database lookup is needed to reach the answer."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The signal peptide unambiguously indicates secretion, which is incompatible with the three intracellular/cytoplasmic options (A, B, D). Among the four given choices, only plasma membrane is compatible with a secreted protein. While one could argue the 'primary' location of C7 is extracellular (it circulates in plasma), 'extracellular region' is not among the options, and plasma membrane is the only viable choice. No ambiguity among the offered alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0162",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry D3YXF5 (Complement component C7, mouse) directly annotates GO:0005886 (plasma membrane) with NAS:ComplexPortal evidence (C9/H6). The subcellular location comment states the protein is 'Secreted as soluble protein. Inserts into the cell membrane of target cells' (C5/H2). Additionally, the membrane attack complex annotation (GO:0005579) is_a GO:0098797 (plasma membrane protein complex), which is part_of GO:0005886 (plasma membrane), providing an ontological path to plasma membrane. The author's answer of 'plasma membrane' is directly supported by the GO annotation and the functional description of C7 inserting into target cell membranes as part of the MAC.",
    "evidence_ids": ["C5", "C7", "C9", "H2", "H4", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal sequence MQVTSLLILVCFIAAFQVFSRA is a classic hydrophobic signal peptide (a stretch of ~20 hydrophobic residues at the extreme N-terminus), which is the universal targeting signal for entry into the ER/secretory pathway. This immediately eliminates P-body (B, a cytoplasmic mRNA-processing granule), perinuclear region of cytoplasm (D, a cytoplasmic location), and host cell nucleus (A, an intracellular compartment typically relevant to viral proteins). A secreted protein cannot reside in the cytoplasm or nucleus. Among the four choices, only plasma membrane (C) is compatible with a secreted protein that subsequently associates with a membrane. Additionally, the large size (~845 aa) and the presence of multiple cysteine-rich domain repeats (Sushi/CCP, LDL-receptor class A, TSP type 1 domains) are hallmarks of complement pathway components, which are well-known secreted proteins that insert into target cell membranes during MAC assembly. This family-level knowledge, combined with the visible signal peptide, uniquely selects C.",
    "missing_item_specific_fact": "",
    "reason": "The N-terminal signal peptide is directly readable from the provided sequence and is a fundamental, transferable feature of secretory proteins. The general principle that signal peptides direct proteins away from the cytoplasm and nucleus eliminates options A, B, and D. The remaining option C (plasma membrane) is the only choice consistent with a secreted protein, and complement components' well-known role in membrane insertion provides further support. No target-specific annotation lookup is required."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The signal peptide unambiguously indicates secretion, which is incompatible with the three intracellular/cytoplasmic options (A, B, D). Among the four given choices, only plasma membrane is compatible with a secreted protein. While one could argue the 'primary' location of C7 is extracellular (it circulates in plasma), 'extracellular region' is not among the options, and plasma membrane is the only viable choice. No ambiguity among the offered alternatives."
  },
  "important_caveats": [
    "C7 is primarily a circulating secreted protein; its association with the plasma membrane is transient (during MAC assembly on target cells). The GO annotation GO:0005886 is supported by ComplexPortal (NAS), reflecting the MAC complex context rather than a constitutive membrane residence.",
    "The GO term 'host cell nucleus' (GO:0042025) is typically used in the context of viral proteins exploiting host machinery, making it an implausible distractor for a mammalian secreted complement component.",
    "The signal peptide is the strongest and most transferable discriminator; no target-specific database lookup is needed to reach the answer."
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
  "requested_accession": "D3YXF5",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "dc93fe1d2b11f0267bd1960d07d9ec9a56f008cb367ad7597552e5252fb454ce",
  "benchmark_sequence_length": 845,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 113,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2012-10-03",
    "sequenceVersion": 2
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "55824c468bad99d86484b91307c62a1409deecde122a11e3c5d814db122530d2",
  "current_source_sequence_sha256": "dc93fe1d2b11f0267bd1960d07d9ec9a56f008cb367ad7597552e5252fb454ce",
  "current_source_sequence_length": 845,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 111,
  "selected_historical_version": {
    "accession": "D3YXF5",
    "database": "Swiss-Prot",
    "entryVersion": 111,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CO7_MOUSE",
    "sequenceVersion": 2
  },
  "selected_historical_record_sha256": "94d86c30e47a04ba17ec6abd0559bb6d1063264d0988b8e0cf5f89515164b588",
  "selected_historical_source_sequence_sha256": "dc93fe1d2b11f0267bd1960d07d9ec9a56f008cb367ad7597552e5252fb454ce",
  "selected_historical_source_sequence_length": 845,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 111,
      "exact_sequence_comparison": "matched",
      "sequence_version": 2
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3YXF5.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D3YXF5.json",
  "source_sha256": "55824c468bad99d86484b91307c62a1409deecde122a11e3c5d814db122530d2",
  "retrieved_utc": "2026-11-02T04:27:45.100729+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"D3YXF5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3YXF5.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D3YXF5.json",
  "source_sha256": "55824c468bad99d86484b91307c62a1409deecde122a11e3c5d814db122530d2",
  "retrieved_utc": "2026-11-02T04:27:45.100729+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":113,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2012-10-03\",\"sequenceVersion\":2}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3YXF5.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D3YXF5.json",
  "source_sha256": "55824c468bad99d86484b91307c62a1409deecde122a11e3c5d814db122530d2",
  "retrieved_utc": "2026-11-02T04:27:45.100729+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Mouse\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Euteleostomi\",\"Mammalia\",\"Eutheria\",\"Euarchontoglires\",\"Glires\",\"Rodentia\",\"Myomorpha\",\"Muroidea\",\"Muridae\",\"Murinae\",\"Mus\",\"Mus\"],\"scientificName\":\"Mus musculus\",\"taxonId\":10090}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3YXF5.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D3YXF5.json",
  "source_sha256": "55824c468bad99d86484b91307c62a1409deecde122a11e3c5d814db122530d2",
  "retrieved_utc": "2026-11-02T04:27:45.100729+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"flag\":\"Precursor\",\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Complement component C7\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3YXF5.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D3YXF5.json",
  "source_sha256": "55824c468bad99d86484b91307c62a1409deecde122a11e3c5d814db122530d2",
  "retrieved_utc": "2026-11-02T04:27:45.100729+00:00",
  "json_pointer": "/comments/3",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10643\",\"source\":\"UniProtKB\"}],\"value\":\"Secreted as soluble protein. Inserts into the cell membrane of target cells\"}]},\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10643\",\"source\":\"UniProtKB\"}],\"id\":\"SL-0243\",\"value\":\"Secreted\"}},{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10643\",\"source\":\"UniProtKB\"}],\"id\":\"SL-0451\",\"value\":\"Target cell membrane\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3YXF5.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D3YXF5.json",
  "source_sha256": "55824c468bad99d86484b91307c62a1409deecde122a11e3c5d814db122530d2",
  "retrieved_utc": "2026-11-02T04:27:45.100729+00:00",
  "json_pointer": "/uniProtKBCrossReferences/38",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005576\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:extracellular region\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISS:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3YXF5.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D3YXF5.json",
  "source_sha256": "55824c468bad99d86484b91307c62a1409deecde122a11e3c5d814db122530d2",
  "retrieved_utc": "2026-11-02T04:27:45.100729+00:00",
  "json_pointer": "/uniProtKBCrossReferences/39",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005579\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:membrane attack complex\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISO:GO_Central\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3YXF5.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D3YXF5.json",
  "source_sha256": "55824c468bad99d86484b91307c62a1409deecde122a11e3c5d814db122530d2",
  "retrieved_utc": "2026-11-02T04:27:45.100729+00:00",
  "json_pointer": "/uniProtKBCrossReferences/40",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0044218\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:other organism cell membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISO:GO_Central\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3YXF5.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D3YXF5.json",
  "source_sha256": "55824c468bad99d86484b91307c62a1409deecde122a11e3c5d814db122530d2",
  "retrieved_utc": "2026-11-02T04:27:45.100729+00:00",
  "json_pointer": "/uniProtKBCrossReferences/41",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30552328\",\"source\":\"PubMed\"}],\"id\":\"GO:0005886\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:plasma membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"NAS:ComplexPortal\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3YXF5?format=txt&versions=111)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/D3YXF5?format=txt&versions=111",
  "source_sha256": "94d86c30e47a04ba17ec6abd0559bb6d1063264d0988b8e0cf5f89515164b588",
  "retrieved_utc": "2026-11-02T04:27:47.074801+00:00",
  "source_locator": "lines 1-13",
  "excerpt": "ID   CO7_MOUSE               Reviewed;         845 AA.\nAC   D3YXF5;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   03-OCT-2012, sequence version 2.\nDT   28-JAN-2026, entry version 111.\nDE   RecName: Full=Complement component C7 {ECO:0000305};\nDE   Flags: Precursor;\nGN   Name=C7 {ECO:0000312|MGI:MGI:88235};\nOS   Mus musculus (Mouse).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;\nOC   Eutheria; Euarchontoglires; Glires; Rodentia; Myomorpha; Muroidea; Muridae;\nOC   Murinae; Mus; Mus.\nOX   NCBI_TaxID=10090;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 111,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3YXF5?format=txt&versions=111)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/D3YXF5?format=txt&versions=111",
  "source_sha256": "94d86c30e47a04ba17ec6abd0559bb6d1063264d0988b8e0cf5f89515164b588",
  "retrieved_utc": "2026-11-02T04:27:47.074801+00:00",
  "source_locator": "lines 49-52",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Secreted {ECO:0000250|UniProtKB:P10643}. Target\nCC       cell membrane {ECO:0000250|UniProtKB:P10643}. Note=Secreted as soluble\nCC       protein. Inserts into the cell membrane of target cells.\nCC       {ECO:0000250|UniProtKB:P10643}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 111,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3YXF5?format=txt&versions=111)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/D3YXF5?format=txt&versions=111",
  "source_sha256": "94d86c30e47a04ba17ec6abd0559bb6d1063264d0988b8e0cf5f89515164b588",
  "retrieved_utc": "2026-11-02T04:27:47.074801+00:00",
  "source_locator": "lines 97-97",
  "excerpt": "DR   GO; GO:0005615; C:extracellular space; IBA:GO_Central.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 111,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3YXF5?format=txt&versions=111)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/D3YXF5?format=txt&versions=111",
  "source_sha256": "94d86c30e47a04ba17ec6abd0559bb6d1063264d0988b8e0cf5f89515164b588",
  "retrieved_utc": "2026-11-02T04:27:47.074801+00:00",
  "source_locator": "lines 98-98",
  "excerpt": "DR   GO; GO:0005579; C:membrane attack complex; ISO:GO_Central.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 111,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3YXF5?format=txt&versions=111)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/D3YXF5?format=txt&versions=111",
  "source_sha256": "94d86c30e47a04ba17ec6abd0559bb6d1063264d0988b8e0cf5f89515164b588",
  "retrieved_utc": "2026-11-02T04:27:47.074801+00:00",
  "source_locator": "lines 99-99",
  "excerpt": "DR   GO; GO:0044218; C:other organism cell membrane; ISO:GO_Central.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 111,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3YXF5?format=txt&versions=111)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/D3YXF5?format=txt&versions=111",
  "source_sha256": "94d86c30e47a04ba17ec6abd0559bb6d1063264d0988b8e0cf5f89515164b588",
  "retrieved_utc": "2026-11-02T04:27:47.074801+00:00",
  "source_locator": "lines 100-100",
  "excerpt": "DR   GO; GO:0005886; C:plasma membrane; NAS:ComplexPortal.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 111,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3YXF5?format=txt&versions=111)

```json
{
  "evidence_id": "H7",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/D3YXF5?format=txt&versions=111",
  "source_sha256": "94d86c30e47a04ba17ec6abd0559bb6d1063264d0988b8e0cf5f89515164b588",
  "retrieved_utc": "2026-11-02T04:27:47.074801+00:00",
  "source_locator": "lines 101-101",
  "excerpt": "DR   GO; GO:1902495; C:transmembrane transporter complex; ISO:GO_Central.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 111,
  "sequence_version": 2,
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
  "source_locator": "lines 6737-6747",
  "excerpt": "[Term]\nid: GO:0000932\nname: P-body\nnamespace: cellular_component\ndef: \"A focus in the cytoplasm where mRNAs may become inactivated by decapping or some other mechanism. Protein and RNA localized to these foci are involved in mRNA degradation, nonsense-mediated mRNA decay (NMD), translational repression, and RNA-mediated gene silencing.\" [GOC:clt, PMID:12730603]\nsynonym: \"cytoplasmic foci\" RELATED []\nsynonym: \"cytoplasmic mRNA processing body\" EXACT []\nsynonym: \"P body\" EXACT []\nxref: Wikipedia:P_body\nis_a: GO:0036464 ! cytoplasmic ribonucleoprotein granule\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0000932"
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
  "source_locator": "lines 57517-57530",
  "excerpt": "[Term]\nid: GO:0005579\nname: membrane attack complex\nnamespace: cellular_component\ndef: \"A protein complex produced by sequentially activated components of the complement cascade inserted into a target cell membrane and forming a pore leading to cell lysis via ion and water flow.\" [GOC:add, ISBN:0198547684, ISBN:068340007X, ISBN:0781735149]\nsynonym: \"MAC\" EXACT []\nsynonym: \"membrane attack complex protein alphaM chain\" NARROW []\nsynonym: \"membrane attack complex protein beta2 chain\" NARROW []\nsynonym: \"TCC\" EXACT []\nsynonym: \"terminal complement complex\" EXACT []\nxref: Wikipedia:Complement_membrane_attack_complex\nis_a: GO:0046930 ! pore complex\nis_a: GO:0098797 ! plasma membrane protein complex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0005579"
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
  "source_locator": "lines 233685-233693",
  "excerpt": "[Term]\nid: GO:0042025\nname: host cell nucleus\nnamespace: cellular_component\nalt_id: GO:0033649\ndef: \"A membrane-bounded organelle as it is found in the host cell in which chromosomes are housed and replicated. The host is defined as the larger of the organisms involved in a symbiotic interaction.\" [GOC:pamgo_curators]\nsubset: goslim_virus\nis_a: GO:0033648 ! host intracellular membrane-bounded organelle\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0042025"
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
  "source_locator": "lines 303515-303523",
  "excerpt": "[Term]\nid: GO:0048471\nname: perinuclear region of cytoplasm\nnamespace: cellular_component\ndef: \"Cytoplasm situated near, or occurring around, the nucleus.\" [GOC:jid]\ncomment: Note that this term should not be confused with the cellular component term 'nuclear membrane lumen ; GO:0005641', which has the synonym 'perinuclear space'.\nis_a: GO:0110165 ! cellular anatomical structure\nrelationship: part_of GO:0005737 ! cytoplasm\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0048471"
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
  "source_locator": "lines 411036-411043",
  "excerpt": "[Term]\nid: GO:0098797\nname: plasma membrane protein complex\nnamespace: cellular_component\ndef: \"Any protein complex that is part of the plasma membrane.\" [GOC:dos]\nis_a: GO:0098796 ! membrane protein complex\nrelationship: part_of GO:0005886 ! plasma membrane\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0098797"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 162. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
