# GO_cellular_component_0153: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/GO_cellular_component_0153.txt)

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
MSIIGSFPPGGPRVEVQETRVQTDRVLTIPNILSMARLAGVPLFLWLILRPEFGGPQSDGWALLVLALSGVSDYLDGKLARRWNQISSLGRLLDPAADRLYILSTLVGLTWREILPLWLTLVLLAREAMLLVMVGILRRHGYPPPQVNFLGKAATFNLMYAFPLLLLSDGSGWIASLAAVFGWAFAGWGTTLYWWAGVLYVVQVRRLVRADVAAD

[Multiple Choices]
A. actin cytoskeleton
B. microvillus membrane
C. plasma membrane
D. trans-Golgi network membrane
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

> The sequence matches the Streptomyces coelicolor cardiolipin synthase record, which annotates the protein to the cell membrane. In GO, “cell membrane” is an exact synonym of “plasma membrane,” including in the prokaryotic context. The annotation is a literature-based manual assertion, while the GO plasma-membrane cross-reference is computationally assigned; neither should be mistaken for a directly supplied measurement.

Citations as saved: [H4](#evidence-h4), [C5](#evidence-c5), [H5](#evidence-h5), [C6](#evidence-c6), [GO1](#evidence-go1).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The many hydrophobic segments support that this is an integral membrane protein, but do not by themselves distinguish the plasma membrane from another membrane. Identifying a bacterial context could make the eukaryote-specific microvillus and trans-Golgi choices implausible, but does not establish this protein’s particular membrane localization from the supplied sequence alone.


**Missing item-specific fact**

> The protein-specific localization annotation or supporting literature that places this cardiolipin synthase at the cell membrane.


**Reason**

> The evidence supporting the key is reviewer-only and absent from the question. The sequence provides a membrane-protein clue, not sufficient grounds to select plasma membrane over all other membrane options.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The protein-specific cell-membrane annotation maps to the offered plasma-membrane choice; no other option is supported by the supplied evidence.


### Important caveats

- The accession and organism identity were inferred from reviewer-only metadata, not provided to the evaluated model.
- The cited UniProt location is a manual literature-based assertion; the GO plasma-membrane annotation is IEA:UniProtKB-SubCell.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The many hydrophobic segments support that this is an integral membrane protein, but do not by themselves distinguish the plasma membrane from another membrane. Identifying a bacterial context could make the eukaryote-specific microvillus and trans-Golgi choices implausible, but does not establish this protein’s particular membrane localization from the supplied sequence alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific localization annotation or supporting literature that places this cardiolipin synthase at the cell membrane.",
    "reason": "The evidence supporting the key is reviewer-only and absent from the question. The sequence provides a membrane-protein clue, not sufficient grounds to select plasma membrane over all other membrane options."
  },
  "case_id": "GO_cellular_component_0153",
  "expected_answer_check": {
    "evidence_ids": [
      "H4",
      "C5",
      "H5",
      "C6",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the Streptomyces coelicolor cardiolipin synthase record, which annotates the protein to the cell membrane. In GO, “cell membrane” is an exact synonym of “plasma membrane,” including in the prokaryotic context. The annotation is a literature-based manual assertion, while the GO plasma-membrane cross-reference is computationally assigned; neither should be mistaken for a directly supplied measurement."
  },
  "important_caveats": [
    "The accession and organism identity were inferred from reviewer-only metadata, not provided to the evaluated model.",
    "The cited UniProt location is a manual literature-based assertion; the GO plasma-membrane annotation is IEA:UniProtKB-SubCell."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein-specific cell-membrane annotation maps to the offered plasma-membrane choice; no other option is supported by the supplied evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0153",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the Streptomyces coelicolor cardiolipin synthase record, which annotates the protein to the cell membrane. In GO, “cell membrane” is an exact synonym of “plasma membrane,” including in the prokaryotic context. The annotation is a literature-based manual assertion, while the GO plasma-membrane cross-reference is computationally assigned; neither should be mistaken for a directly supplied measurement.",
    "evidence_ids": ["H4", "C5", "H5", "C6", "GO1"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The many hydrophobic segments support that this is an integral membrane protein, but do not by themselves distinguish the plasma membrane from another membrane. Identifying a bacterial context could make the eukaryote-specific microvillus and trans-Golgi choices implausible, but does not establish this protein’s particular membrane localization from the supplied sequence alone.",
    "missing_item_specific_fact": "The protein-specific localization annotation or supporting literature that places this cardiolipin synthase at the cell membrane.",
    "reason": "The evidence supporting the key is reviewer-only and absent from the question. The sequence provides a membrane-protein clue, not sufficient grounds to select plasma membrane over all other membrane options."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein-specific cell-membrane annotation maps to the offered plasma-membrane choice; no other option is supported by the supplied evidence."
  },
  "important_caveats": [
    "The accession and organism identity were inferred from reviewer-only metadata, not provided to the evaluated model.",
    "The cited UniProt location is a manual literature-based assertion; the GO plasma-membrane annotation is IEA:UniProtKB-SubCell."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q9KZP3 (Cardiolipin synthase CMP-forming, Streptomyces coelicolor) annotates subcellular location as 'Cell membrane; Multi-pass membrane protein' (evidence: ECO:0000305 from PubMed:19439403, an experimental study). The GO cross-reference maps this to GO:0005886 'plasma membrane' (IEA:UniProtKB-SubCell). GO:0005886 lists 'cell membrane' and 'cytoplasmic membrane' as EXACT synonyms, confirming the mapping. The 2009 J. Biol. Chem. paper (Sandoval-Calderon et al.) experimentally determined subcellular location. The sequence matches exactly (215 aa, SHA256 match).

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5), [GO1](#evidence-go1), [C7](#evidence-c7), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple hydrophobic stretches (e.g., MARLAGVPLFLWLILRPEFG, GWALLVLALSGVSDY, LSTLVGLTWREILPLWLTLVLLAREAMLLVMVGILRR, FNLMYAFPLLLLSDGSGWIASLAAVFGWAFAGWGTTLYWWAGVLYVVQVRRL) indicating a multi-pass transmembrane protein. The absence of eukaryotic signal peptides, no ER/Golgi targeting motifs, and the short length (215 aa) with amino acid composition consistent with a GC-rich actinobacterium point to a bacterial origin. Bacteria lack a Golgi apparatus (eliminating D: trans-Golgi network membrane), microvilli (eliminating B: microvillus membrane), and a true actin cytoskeleton (eliminating A: actin cytoskeleton). The only remaining viable compartment for a bacterial multi-pass membrane protein is the cell/plasma membrane (option C), which GO:0005886 explicitly includes 'cell membrane' and 'cytoplasmic membrane' as EXACT synonyms.


**Missing item-specific fact**

> None strictly required. The sequence features (multiple TM helices, bacterial-like composition, absence of eukaryotic targeting signals) combined with general knowledge that bacteria lack Golgi, microvilli, and actin cytoskeleton provide sufficient grounds to select C.


**Reason**

> A model can reason: (1) multiple TM domains → membrane protein; (2) no eukaryotic secretory-pathway targeting signals and bacterial-like sequence composition → bacterial origin; (3) bacteria lack Golgi, microvilli, and actin cytoskeleton → eliminate A, B, D; (4) bacterial cell membrane = plasma membrane in GO → select C. This is a concrete biological argument grounded in the sequence and general cell biology, not requiring recall of this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and D describe structures exclusive to eukaryotic cells. Given the bacterial sequence features, only C (plasma membrane) is biologically viable. No other option is defensible for a bacterial multi-pass membrane protein.


### Important caveats

- The GO annotation evidence code for plasma membrane is IEA:UniProtKB-SubCell (electronic inference from UniProt), but the underlying UniProt annotation traces to experimental determination in PubMed:19439403 (Sandoval-Calderon et al. 2009, J. Biol. Chem.).
- The organism (Streptomyces coelicolor) is not explicitly stated in the question; the model must infer bacterial origin from sequence features. This inference, while reasonable, adds a step of difficulty.
- The reviewer-only evidence confirms the answer but was not available to the evaluated model.
- GO:0005886 'plasma membrane' includes 'cell membrane' and 'cytoplasmic membrane' as EXACT synonyms per the ontology definition (GO1), making the mapping from bacterial 'cell membrane' annotation to 'plasma membrane' unambiguous.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple hydrophobic stretches (e.g., MARLAGVPLFLWLILRPEFG, GWALLVLALSGVSDY, LSTLVGLTWREILPLWLTLVLLAREAMLLVMVGILRR, FNLMYAFPLLLLSDGSGWIASLAAVFGWAFAGWGTTLYWWAGVLYVVQVRRL) indicating a multi-pass transmembrane protein. The absence of eukaryotic signal peptides, no ER/Golgi targeting motifs, and the short length (215 aa) with amino acid composition consistent with a GC-rich actinobacterium point to a bacterial origin. Bacteria lack a Golgi apparatus (eliminating D: trans-Golgi network membrane), microvilli (eliminating B: microvillus membrane), and a true actin cytoskeleton (eliminating A: actin cytoskeleton). The only remaining viable compartment for a bacterial multi-pass membrane protein is the cell/plasma membrane (option C), which GO:0005886 explicitly includes 'cell membrane' and 'cytoplasmic membrane' as EXACT synonyms.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. The sequence features (multiple TM helices, bacterial-like composition, absence of eukaryotic targeting signals) combined with general knowledge that bacteria lack Golgi, microvilli, and actin cytoskeleton provide sufficient grounds to select C.",
    "reason": "A model can reason: (1) multiple TM domains → membrane protein; (2) no eukaryotic secretory-pathway targeting signals and bacterial-like sequence composition → bacterial origin; (3) bacteria lack Golgi, microvilli, and actin cytoskeleton → eliminate A, B, D; (4) bacterial cell membrane = plasma membrane in GO → select C. This is a concrete biological argument grounded in the sequence and general cell biology, not requiring recall of this specific protein's database entry."
  },
  "case_id": "GO_cellular_component_0153",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5",
      "GO1",
      "C7",
      "H2"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q9KZP3 (Cardiolipin synthase CMP-forming, Streptomyces coelicolor) annotates subcellular location as 'Cell membrane; Multi-pass membrane protein' (evidence: ECO:0000305 from PubMed:19439403, an experimental study). The GO cross-reference maps this to GO:0005886 'plasma membrane' (IEA:UniProtKB-SubCell). GO:0005886 lists 'cell membrane' and 'cytoplasmic membrane' as EXACT synonyms, confirming the mapping. The 2009 J. Biol. Chem. paper (Sandoval-Calderon et al.) experimentally determined subcellular location. The sequence matches exactly (215 aa, SHA256 match)."
  },
  "important_caveats": [
    "The GO annotation evidence code for plasma membrane is IEA:UniProtKB-SubCell (electronic inference from UniProt), but the underlying UniProt annotation traces to experimental determination in PubMed:19439403 (Sandoval-Calderon et al. 2009, J. Biol. Chem.).",
    "The organism (Streptomyces coelicolor) is not explicitly stated in the question; the model must infer bacterial origin from sequence features. This inference, while reasonable, adds a step of difficulty.",
    "The reviewer-only evidence confirms the answer but was not available to the evaluated model.",
    "GO:0005886 'plasma membrane' includes 'cell membrane' and 'cytoplasmic membrane' as EXACT synonyms per the ontology definition (GO1), making the mapping from bacterial 'cell membrane' annotation to 'plasma membrane' unambiguous."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D describe structures exclusive to eukaryotic cells. Given the bacterial sequence features, only C (plasma membrane) is biologically viable. No other option is defensible for a bacterial multi-pass membrane protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0153",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q9KZP3 (Cardiolipin synthase CMP-forming, Streptomyces coelicolor) annotates subcellular location as 'Cell membrane; Multi-pass membrane protein' (evidence: ECO:0000305 from PubMed:19439403, an experimental study). The GO cross-reference maps this to GO:0005886 'plasma membrane' (IEA:UniProtKB-SubCell). GO:0005886 lists 'cell membrane' and 'cytoplasmic membrane' as EXACT synonyms, confirming the mapping. The 2009 J. Biol. Chem. paper (Sandoval-Calderon et al.) experimentally determined subcellular location. The sequence matches exactly (215 aa, SHA256 match).",
    "evidence_ids": ["C5", "C6", "H4", "H5", "GO1", "C7", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple hydrophobic stretches (e.g., MARLAGVPLFLWLILRPEFG, GWALLVLALSGVSDY, LSTLVGLTWREILPLWLTLVLLAREAMLLVMVGILRR, FNLMYAFPLLLLSDGSGWIASLAAVFGWAFAGWGTTLYWWAGVLYVVQVRRL) indicating a multi-pass transmembrane protein. The absence of eukaryotic signal peptides, no ER/Golgi targeting motifs, and the short length (215 aa) with amino acid composition consistent with a GC-rich actinobacterium point to a bacterial origin. Bacteria lack a Golgi apparatus (eliminating D: trans-Golgi network membrane), microvilli (eliminating B: microvillus membrane), and a true actin cytoskeleton (eliminating A: actin cytoskeleton). The only remaining viable compartment for a bacterial multi-pass membrane protein is the cell/plasma membrane (option C), which GO:0005886 explicitly includes 'cell membrane' and 'cytoplasmic membrane' as EXACT synonyms.",
    "missing_item_specific_fact": "None strictly required. The sequence features (multiple TM helices, bacterial-like composition, absence of eukaryotic targeting signals) combined with general knowledge that bacteria lack Golgi, microvilli, and actin cytoskeleton provide sufficient grounds to select C.",
    "reason": "A model can reason: (1) multiple TM domains → membrane protein; (2) no eukaryotic secretory-pathway targeting signals and bacterial-like sequence composition → bacterial origin; (3) bacteria lack Golgi, microvilli, and actin cytoskeleton → eliminate A, B, D; (4) bacterial cell membrane = plasma membrane in GO → select C. This is a concrete biological argument grounded in the sequence and general cell biology, not requiring recall of this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D describe structures exclusive to eukaryotic cells. Given the bacterial sequence features, only C (plasma membrane) is biologically viable. No other option is defensible for a bacterial multi-pass membrane protein."
  },
  "important_caveats": [
    "The GO annotation evidence code for plasma membrane is IEA:UniProtKB-SubCell (electronic inference from UniProt), but the underlying UniProt annotation traces to experimental determination in PubMed:19439403 (Sandoval-Calderon et al. 2009, J. Biol. Chem.).",
    "The organism (Streptomyces coelicolor) is not explicitly stated in the question; the model must infer bacterial origin from sequence features. This inference, while reasonable, adds a step of difficulty.",
    "The reviewer-only evidence confirms the answer but was not available to the evaluated model.",
    "GO:0005886 'plasma membrane' includes 'cell membrane' and 'cytoplasmic membrane' as EXACT synonyms per the ontology definition (GO1), making the mapping from bacterial 'cell membrane' annotation to 'plasma membrane' unambiguous."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches the cited UniProt record, which assigns the protein to the cell membrane and annotates GO:0005886, plasma membrane. The cell-membrane annotation cites a publication, while the GO annotation is IEA; these are database annotations, not independently reviewed experimental results here. In the GO context, plasma membrane includes the bacterial cell membrane.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is strongly hydrophobic across multiple regions, consistent with an integral multipass membrane protein rather than an actin-cytoskeleton component. Among the membrane choices, plasma membrane is the broad, plausible location: microvillus and trans-Golgi network membranes are specialized eukaryotic compartments, whereas the cell membrane is the general membrane location for many multipass membrane enzymes, including bacterial ones.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and the contrast among the options support a meaningful probabilistic choice of plasma membrane without knowing this protein’s recorded annotation. The sequence alone does not prove the precise membrane location, but the alternatives make the broad cell-membrane choice more plausible than the specialized eukaryotic compartments.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered choice is comparably supported by the multipass membrane sequence and the broad-versus-specialized distinction among the membrane options.


### Important caveats

- The organism is not provided in the original input, so the inference about bacterial-style cell-membrane localization is probabilistic rather than established from the prompt alone.
- The supplied GO annotation is computationally inferred (IEA); the cited cell-membrane annotation is recorded as literature-supported, but the underlying paper was not independently validated here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is strongly hydrophobic across multiple regions, consistent with an integral multipass membrane protein rather than an actin-cytoskeleton component. Among the membrane choices, plasma membrane is the broad, plausible location: microvillus and trans-Golgi network membranes are specialized eukaryotic compartments, whereas the cell membrane is the general membrane location for many multipass membrane enzymes, including bacterial ones.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and the contrast among the options support a meaningful probabilistic choice of plasma membrane without knowing this protein’s recorded annotation. The sequence alone does not prove the precise membrane location, but the alternatives make the broad cell-membrane choice more plausible than the specialized eukaryotic compartments."
  },
  "case_id": "GO_cellular_component_0153",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the cited UniProt record, which assigns the protein to the cell membrane and annotates GO:0005886, plasma membrane. The cell-membrane annotation cites a publication, while the GO annotation is IEA; these are database annotations, not independently reviewed experimental results here. In the GO context, plasma membrane includes the bacterial cell membrane."
  },
  "important_caveats": [
    "The organism is not provided in the original input, so the inference about bacterial-style cell-membrane localization is probabilistic rather than established from the prompt alone.",
    "The supplied GO annotation is computationally inferred (IEA); the cited cell-membrane annotation is recorded as literature-supported, but the underlying paper was not independently validated here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered choice is comparably supported by the multipass membrane sequence and the broad-versus-specialized distinction among the membrane options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0153",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the cited UniProt record, which assigns the protein to the cell membrane and annotates GO:0005886, plasma membrane. The cell-membrane annotation cites a publication, while the GO annotation is IEA; these are database annotations, not independently reviewed experimental results here. In the GO context, plasma membrane includes the bacterial cell membrane.",
    "evidence_ids": ["C5", "C6", "H4", "H5", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is strongly hydrophobic across multiple regions, consistent with an integral multipass membrane protein rather than an actin-cytoskeleton component. Among the membrane choices, plasma membrane is the broad, plausible location: microvillus and trans-Golgi network membranes are specialized eukaryotic compartments, whereas the cell membrane is the general membrane location for many multipass membrane enzymes, including bacterial ones.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and the contrast among the options support a meaningful probabilistic choice of plasma membrane without knowing this protein’s recorded annotation. The sequence alone does not prove the precise membrane location, but the alternatives make the broad cell-membrane choice more plausible than the specialized eukaryotic compartments."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered choice is comparably supported by the multipass membrane sequence and the broad-versus-specialized distinction among the membrane options."
  },
  "important_caveats": [
    "The organism is not provided in the original input, so the inference about bacterial-style cell-membrane localization is probabilistic rather than established from the prompt alone.",
    "The supplied GO annotation is computationally inferred (IEA); the cited cell-membrane annotation is recorded as literature-supported, but the underlying paper was not independently validated here."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9KZP3 (Cardiolipin synthase, CMP-forming, from Streptomyces coelicolor) is annotated as 'Cell membrane; Multi-pass membrane protein' with experimental support from PubMed:19439403 (ECO:0000305). GO:0005886 (plasma membrane) lists 'cell membrane' as an EXACT synonym, and the GO cross-reference GO:0005886 C:plasma membrane is present (IEA:UniProtKB-SubCell). The answer 'plasma membrane' is directly supported by the curated annotation.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 215-aa sequence is overwhelmingly hydrophobic with multiple long stretches of TM-like residues (e.g., 'VPLFLWLILRPEFGGPQSDGWALLVLALSGVSDYLDGKLARRWNQISSLGRLLDPAADRLYILSTLVGLTWREILPLWLTLVLLAREAMLLVMVGILRRHGYPPPQVNFLGKAATFNLMYAFPLLLLSDGSGWIASLAAVFGWAFAGWGTTLYWWAGVLYVVQVRRLVRADVAAD'), clearly indicating a multi-pass membrane protein. This eliminates option A (actin cytoskeleton, a non-membrane eukaryotic structure). The extreme hydrophobicity, short total length (215 aa), absence of N-glycosylation sequons, absence of ER/Golgi targeting signals (no cleavable signal peptide with a hydrophilic N-terminus followed by translocation), and absence of mitochondrial or nuclear targeting sequences are all hallmarks of a bacterial inner/plasma membrane protein. Bacteria lack actin cytoskeleton (A), microvilli (B), and Golgi apparatus (D), so recognizing the bacterial character of the sequence eliminates all three. Even without certainty about the organism, general principles apply: a compact multi-pass membrane protein with no organelle-specific targeting signals defaults to the plasma membrane rather than the highly specialized trans-Golgi network membrane (which requires specific retrieval/retention signals) or the extremely specialized microvillus membrane (restricted to epithelial brush borders). Thus, plasma membrane is the most defensible choice by elimination and by positive inference.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence's extreme hydrophobicity, multiple TM segments, short length, and absence of eukaryotic organelle targeting signals provide a concrete basis for inferring a bacterial plasma membrane location. Family-level knowledge (cardiolipin synthases are membrane enzymes; bacterial membrane proteins lack Golgi/microvillus/actin associations) and general cell biology (bacteria lack eukaryotic organelles) meaningfully distinguish C from A, B, and D without requiring the exact UniProt record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and D describe structures absent in bacteria (actin cytoskeleton, microvilli, Golgi). Option C (plasma membrane) is the only compartment among the four that exists in a prokaryote and is consistent with a multi-pass membrane protein lacking eukaryotic targeting signals. No other option is defensible given the sequence features.


### Important caveats

- The GO annotation for this protein is IEA:UniProtKB-SubCell, meaning the GO-level evidence is inferred from the subcellular location field rather than a direct GO curation; the underlying subcellular location annotation cites PubMed:19439403 with ECO:0000305 (curator inference from experimental data).
- The model must infer bacterial origin from sequence features alone; the organism name is not provided in the input. However, the extreme hydrophobicity, compact multi-pass architecture, and absence of eukaryotic signals make this inference highly reliable.
- The sequence match is confirmed (SHA256 identical to Q9KZP3), so the annotation applies to exactly this sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 215-aa sequence is overwhelmingly hydrophobic with multiple long stretches of TM-like residues (e.g., 'VPLFLWLILRPEFGGPQSDGWALLVLALSGVSDYLDGKLARRWNQISSLGRLLDPAADRLYILSTLVGLTWREILPLWLTLVLLAREAMLLVMVGILRRHGYPPPQVNFLGKAATFNLMYAFPLLLLSDGSGWIASLAAVFGWAFAGWGTTLYWWAGVLYVVQVRRLVRADVAAD'), clearly indicating a multi-pass membrane protein. This eliminates option A (actin cytoskeleton, a non-membrane eukaryotic structure). The extreme hydrophobicity, short total length (215 aa), absence of N-glycosylation sequons, absence of ER/Golgi targeting signals (no cleavable signal peptide with a hydrophilic N-terminus followed by translocation), and absence of mitochondrial or nuclear targeting sequences are all hallmarks of a bacterial inner/plasma membrane protein. Bacteria lack actin cytoskeleton (A), microvilli (B), and Golgi apparatus (D), so recognizing the bacterial character of the sequence eliminates all three. Even without certainty about the organism, general principles apply: a compact multi-pass membrane protein with no organelle-specific targeting signals defaults to the plasma membrane rather than the highly specialized trans-Golgi network membrane (which requires specific retrieval/retention signals) or the extremely specialized microvillus membrane (restricted to epithelial brush borders). Thus, plasma membrane is the most defensible choice by elimination and by positive inference.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence's extreme hydrophobicity, multiple TM segments, short length, and absence of eukaryotic organelle targeting signals provide a concrete basis for inferring a bacterial plasma membrane location. Family-level knowledge (cardiolipin synthases are membrane enzymes; bacterial membrane proteins lack Golgi/microvillus/actin associations) and general cell biology (bacteria lack eukaryotic organelles) meaningfully distinguish C from A, B, and D without requiring the exact UniProt record."
  },
  "case_id": "GO_cellular_component_0153",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q9KZP3 (Cardiolipin synthase, CMP-forming, from Streptomyces coelicolor) is annotated as 'Cell membrane; Multi-pass membrane protein' with experimental support from PubMed:19439403 (ECO:0000305). GO:0005886 (plasma membrane) lists 'cell membrane' as an EXACT synonym, and the GO cross-reference GO:0005886 C:plasma membrane is present (IEA:UniProtKB-SubCell). The answer 'plasma membrane' is directly supported by the curated annotation."
  },
  "important_caveats": [
    "The GO annotation for this protein is IEA:UniProtKB-SubCell, meaning the GO-level evidence is inferred from the subcellular location field rather than a direct GO curation; the underlying subcellular location annotation cites PubMed:19439403 with ECO:0000305 (curator inference from experimental data).",
    "The model must infer bacterial origin from sequence features alone; the organism name is not provided in the input. However, the extreme hydrophobicity, compact multi-pass architecture, and absence of eukaryotic signals make this inference highly reliable.",
    "The sequence match is confirmed (SHA256 identical to Q9KZP3), so the annotation applies to exactly this sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D describe structures absent in bacteria (actin cytoskeleton, microvilli, Golgi). Option C (plasma membrane) is the only compartment among the four that exists in a prokaryote and is consistent with a multi-pass membrane protein lacking eukaryotic targeting signals. No other option is defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0153",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9KZP3 (Cardiolipin synthase, CMP-forming, from Streptomyces coelicolor) is annotated as 'Cell membrane; Multi-pass membrane protein' with experimental support from PubMed:19439403 (ECO:0000305). GO:0005886 (plasma membrane) lists 'cell membrane' as an EXACT synonym, and the GO cross-reference GO:0005886 C:plasma membrane is present (IEA:UniProtKB-SubCell). The answer 'plasma membrane' is directly supported by the curated annotation.",
    "evidence_ids": ["C5", "C6", "C7", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 215-aa sequence is overwhelmingly hydrophobic with multiple long stretches of TM-like residues (e.g., 'VPLFLWLILRPEFGGPQSDGWALLVLALSGVSDYLDGKLARRWNQISSLGRLLDPAADRLYILSTLVGLTWREILPLWLTLVLLAREAMLLVMVGILRRHGYPPPQVNFLGKAATFNLMYAFPLLLLSDGSGWIASLAAVFGWAFAGWGTTLYWWAGVLYVVQVRRLVRADVAAD'), clearly indicating a multi-pass membrane protein. This eliminates option A (actin cytoskeleton, a non-membrane eukaryotic structure). The extreme hydrophobicity, short total length (215 aa), absence of N-glycosylation sequons, absence of ER/Golgi targeting signals (no cleavable signal peptide with a hydrophilic N-terminus followed by translocation), and absence of mitochondrial or nuclear targeting sequences are all hallmarks of a bacterial inner/plasma membrane protein. Bacteria lack actin cytoskeleton (A), microvilli (B), and Golgi apparatus (D), so recognizing the bacterial character of the sequence eliminates all three. Even without certainty about the organism, general principles apply: a compact multi-pass membrane protein with no organelle-specific targeting signals defaults to the plasma membrane rather than the highly specialized trans-Golgi network membrane (which requires specific retrieval/retention signals) or the extremely specialized microvillus membrane (restricted to epithelial brush borders). Thus, plasma membrane is the most defensible choice by elimination and by positive inference.",
    "missing_item_specific_fact": "",
    "reason": "The sequence's extreme hydrophobicity, multiple TM segments, short length, and absence of eukaryotic organelle targeting signals provide a concrete basis for inferring a bacterial plasma membrane location. Family-level knowledge (cardiolipin synthases are membrane enzymes; bacterial membrane proteins lack Golgi/microvillus/actin associations) and general cell biology (bacteria lack eukaryotic organelles) meaningfully distinguish C from A, B, and D without requiring the exact UniProt record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D describe structures absent in bacteria (actin cytoskeleton, microvilli, Golgi). Option C (plasma membrane) is the only compartment among the four that exists in a prokaryote and is consistent with a multi-pass membrane protein lacking eukaryotic targeting signals. No other option is defensible given the sequence features."
  },
  "important_caveats": [
    "The GO annotation for this protein is IEA:UniProtKB-SubCell, meaning the GO-level evidence is inferred from the subcellular location field rather than a direct GO curation; the underlying subcellular location annotation cites PubMed:19439403 with ECO:0000305 (curator inference from experimental data).",
    "The model must infer bacterial origin from sequence features alone; the organism name is not provided in the input. However, the extreme hydrophobicity, compact multi-pass architecture, and absence of eukaryotic signals make this inference highly reliable.",
    "The sequence match is confirmed (SHA256 identical to Q9KZP3), so the annotation applies to exactly this sequence."
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
  "requested_accession": "Q9KZP3",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "4d7ff8f97540a27b3e75118f82df28e82087f33a3652f781a7c4f3611ee726bb",
  "benchmark_sequence_length": 215,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 120,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2000-10-01",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "19159a513ac84423a492087d8961c46891339eef5cec5a9d995ec98e1cfe717c",
  "current_source_sequence_sha256": "4d7ff8f97540a27b3e75118f82df28e82087f33a3652f781a7c4f3611ee726bb",
  "current_source_sequence_length": 215,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 118,
  "selected_historical_version": {
    "accession": "Q9KZP3",
    "database": "Swiss-Prot",
    "entryVersion": 118,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CRLS1_STRCO",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "40068827609c34109c814e2d2c856e36a3bec9b7c2775a90bbcc5f7a21726d79",
  "selected_historical_source_sequence_sha256": "4d7ff8f97540a27b3e75118f82df28e82087f33a3652f781a7c4f3611ee726bb",
  "selected_historical_source_sequence_length": 215,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 118,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KZP3.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KZP3.json",
  "source_sha256": "19159a513ac84423a492087d8961c46891339eef5cec5a9d995ec98e1cfe717c",
  "retrieved_utc": "2026-11-01T06:25:27.611577+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"Q9KZP3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KZP3.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KZP3.json",
  "source_sha256": "19159a513ac84423a492087d8961c46891339eef5cec5a9d995ec98e1cfe717c",
  "retrieved_utc": "2026-11-01T06:25:27.611577+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":120,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2000-10-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KZP3.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KZP3.json",
  "source_sha256": "19159a513ac84423a492087d8961c46891339eef5cec5a9d995ec98e1cfe717c",
  "retrieved_utc": "2026-11-01T06:25:27.611577+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000001973\",\"source\":\"Proteomes\"}],\"lineage\":[\"Bacteria\",\"Bacillati\",\"Actinomycetota\",\"Actinomycetes\",\"Kitasatosporales\",\"Streptomycetaceae\",\"Streptomyces\",\"Streptomyces albidoflavus group\"],\"scientificName\":\"Streptomyces coelicolor (strain ATCC BAA-471 / A3(2) / M145)\",\"taxonId\":100226}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KZP3.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KZP3.json",
  "source_sha256": "19159a513ac84423a492087d8961c46891339eef5cec5a9d995ec98e1cfe717c",
  "retrieved_utc": "2026-11-01T06:25:27.611577+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"19439403\",\"source\":\"PubMed\"}],\"value\":\"2.7.8.41\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Cardiolipin synthase (CMP-forming)\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"CLS\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KZP3.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KZP3.json",
  "source_sha256": "19159a513ac84423a492087d8961c46891339eef5cec5a9d995ec98e1cfe717c",
  "retrieved_utc": "2026-11-01T06:25:27.611577+00:00",
  "json_pointer": "/comments/4",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"19439403\",\"source\":\"PubMed\"}],\"id\":\"SL-0039\",\"value\":\"Cell membrane\"},\"topology\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"id\":\"SL-9909\",\"value\":\"Multi-pass membrane protein\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KZP3.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KZP3.json",
  "source_sha256": "19159a513ac84423a492087d8961c46891339eef5cec5a9d995ec98e1cfe717c",
  "retrieved_utc": "2026-11-01T06:25:27.611577+00:00",
  "json_pointer": "/uniProtKBCrossReferences/15",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005886\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:plasma membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-SubCell\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KZP3.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KZP3.json",
  "source_sha256": "19159a513ac84423a492087d8961c46891339eef5cec5a9d995ec98e1cfe717c",
  "retrieved_utc": "2026-11-01T06:25:27.611577+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Sandoval-Calderon M.\",\"Geiger O.\",\"Guan Z.\",\"Barona-Gomez F.\",\"Sohlenkamp C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"19439403\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m109.006072\"}],\"citationType\":\"journal article\",\"firstPage\":\"17383\",\"id\":\"19439403\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"17390\",\"publicationDate\":\"2009\",\"title\":\"A eukaryote-like cardiolipin synthase is present in Streptomyces coelicolor and in most actinobacteria.\",\"volume\":\"284\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118",
  "source_sha256": "40068827609c34109c814e2d2c856e36a3bec9b7c2775a90bbcc5f7a21726d79",
  "retrieved_utc": "2026-11-01T06:28:47.509754+00:00",
  "source_locator": "lines 1-15",
  "excerpt": "ID   CRLS1_STRCO             Reviewed;         215 AA.\nAC   Q9KZP3;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-OCT-2000, sequence version 1.\nDT   28-JAN-2026, entry version 118.\nDE   RecName: Full=Cardiolipin synthase (CMP-forming) {ECO:0000305};\nDE            Short=CLS {ECO:0000305};\nDE            EC=2.7.8.41 {ECO:0000305|PubMed:19439403};\nGN   Name=clsA {ECO:0000303|PubMed:22409773};\nGN   OrderedLocusNames=SCO1389 {ECO:0000312|EMBL:CAB88885.1};\nGN   ORFNames=SC1A8A.09c {ECO:0000312|EMBL:CAB88885.1};\nOS   Streptomyces coelicolor (strain ATCC BAA-471 / A3(2) / M145).\nOC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Kitasatosporales;\nOC   Streptomycetaceae; Streptomyces; Streptomyces albidoflavus group.\nOX   NCBI_TaxID=100226 {ECO:0000312|Proteomes:UP000001973};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 118,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118",
  "source_sha256": "40068827609c34109c814e2d2c856e36a3bec9b7c2775a90bbcc5f7a21726d79",
  "retrieved_utc": "2026-11-01T06:28:47.509754+00:00",
  "source_locator": "lines 31-38",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, COFACTOR, BIOPHYSICOCHEMICAL PROPERTIES, AND\nRP   SUBCELLULAR LOCATION.\nRX   PubMed=19439403; DOI=10.1074/jbc.m109.006072;\nRA   Sandoval-Calderon M., Geiger O., Guan Z., Barona-Gomez F., Sohlenkamp C.;\nRT   \"A eukaryote-like cardiolipin synthase is present in Streptomyces\nRT   coelicolor and in most actinobacteria.\";\nRL   J. Biol. Chem. 284:17383-17390(2009).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 118,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118",
  "source_sha256": "40068827609c34109c814e2d2c856e36a3bec9b7c2775a90bbcc5f7a21726d79",
  "retrieved_utc": "2026-11-01T06:28:47.509754+00:00",
  "source_locator": "lines 39-46",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=22409773; DOI=10.1111/j.1365-2958.2012.08018.x;\nRA   Jyothikumar V., Klanbut K., Tiong J., Roxburgh J.S., Hunter I.S.,\nRA   Smith T.K., Herron P.R.;\nRT   \"Cardiolipin synthase is required for Streptomyces coelicolor\nRT   morphogenesis.\";\nRL   Mol. Microbiol. 84:181-197(2012).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 118,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118",
  "source_sha256": "40068827609c34109c814e2d2c856e36a3bec9b7c2775a90bbcc5f7a21726d79",
  "retrieved_utc": "2026-11-01T06:28:47.509754+00:00",
  "source_locator": "lines 66-67",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000305|PubMed:19439403};\nCC       Multi-pass membrane protein {ECO:0000255}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 118,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118",
  "source_sha256": "40068827609c34109c814e2d2c856e36a3bec9b7c2775a90bbcc5f7a21726d79",
  "retrieved_utc": "2026-11-01T06:28:47.509754+00:00",
  "source_locator": "lines 93-93",
  "excerpt": "DR   GO; GO:0005886; C:plasma membrane; IEA:UniProtKB-SubCell.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 118,
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
  "source_locator": "lines 60420-60454",
  "excerpt": "[Term]\nid: GO:0005886\nname: plasma membrane\nnamespace: cellular_component\nalt_id: GO:0005887\nalt_id: GO:0005904\ndef: \"The membrane surrounding a cell that separates the cell from its external environment. It consists of a phospholipid bilayer and associated proteins.\" [ISBN:0716731363]\nsubset: goslim_agr\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_generic\nsubset: goslim_metagenomics\nsubset: goslim_mouse\nsubset: goslim_plant\nsubset: goslim_plant_ribbon\nsubset: goslim_prokaryote\nsubset: goslim_prokaryote_ribbon\nsubset: goslim_yeast\nsynonym: \"bacterial inner membrane\" NARROW []\nsynonym: \"cell membrane\" EXACT []\nsynonym: \"cellular membrane\" EXACT [NIF_Subcellular:sao6433132645]\nsynonym: \"cytoplasmic membrane\" EXACT []\nsynonym: \"inner endospore membrane\" NARROW []\nsynonym: \"integral component of plasma membrane\" NARROW []\nsynonym: \"integral to plasma membrane\" NARROW []\nsynonym: \"juxtamembrane\" BROAD []\nsynonym: \"plasma membrane lipid bilayer\" NARROW [GOC:mah]\nsynonym: \"plasmalemma\" EXACT []\nxref: NIF_Subcellular:sao1663586795\nxref: Wikipedia:Cell_membrane\nis_a: GO:0016020 ! membrane\nrelationship: part_of GO:0071944 ! cell periphery\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0005886"
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
  "source_locator": "lines 119402-119408",
  "excerpt": "[Term]\nid: GO:0015629\nname: actin cytoskeleton\nnamespace: cellular_component\ndef: \"The part of the cytoskeleton (the internal framework of a cell) composed of actin and associated proteins. Includes actin cytoskeleton-associated complexes.\" [GOC:jl, ISBN:0395825172, ISBN:0815316194]\nis_a: GO:0005856 ! cytoskeleton\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0015629"
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
  "source_locator": "lines 177423-177430",
  "excerpt": "[Term]\nid: GO:0031528\nname: microvillus membrane\nnamespace: cellular_component\ndef: \"The portion of the plasma membrane surrounding a microvillus.\" [GOC:mah]\nis_a: GO:0031253 ! cell projection membrane\nrelationship: part_of GO:0005902 ! microvillus\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0031528"
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
  "source_locator": "lines 187565-187574",
  "excerpt": "[Term]\nid: GO:0032588\nname: trans-Golgi network membrane\nnamespace: cellular_component\ndef: \"The lipid bilayer surrounding any of the compartments that make up the trans-Golgi network.\" [GOC:mah]\nsynonym: \"Golgi trans face membrane\" RELATED []\nsynonym: \"trans Golgi network membrane\" EXACT []\nis_a: GO:0031090 ! organelle membrane\nrelationship: part_of GO:0005802 ! trans-Golgi network\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0032588"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 153. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
