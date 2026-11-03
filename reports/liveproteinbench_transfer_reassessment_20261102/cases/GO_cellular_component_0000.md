# GO_cellular_component_0000: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/GO_cellular_component_0000.txt)

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
MKQNPAKTARMWIIICLLFVLGQATDNDRDFKMCGKWLHGIAPQNLEYDLKTGCERIEISANESTLSIQGRITAKCTQSSSIQLDSNPHQNQSHFCVFWEPLLDLLIVEVNGKNHTLCKPNGLQGTCCTDLSQGVQDNAHMYGIVNGSVKGDIITGDLKGNYIFDGAHINCKEKFCDEARLKPRGANMIEEVVMRFNAKGRVDLPCAQGTVIEMDEEFTGHNFTVPAPRFVDANTIPSVYIPSSLRSVSRRKSKVVCTYYKNKTLFERGPSKSALLDDIVGLSVENETIRNLIEPVKIRFHHRPFAPDSSGRCVSWDTKQDNEVNWKDDGCDTVKINEEQTECHCNHLTYFAILVQVEQKSTVRHLKALTFITAVGCAVSLVSCLVLFYWLCKRRRGKKNQISLVHRGLVVAIFLLCLFFILTGILANVANETVCQLTGSLLHYGLLSTLCWMAMEVFHTFLLVRKVFNSPLPIWIFYLMGFGFPFLLVSILLSVGDIYGERKIKPSDDVNNPYRMCWMTEGDKSQLAHYIINIGLLAVVVSSGLVMLFLVVREIRNRPDWKKIHVAFLSIWGLTCLYGTTWALGFLDFGPFSEVTLFLFCIINSLQGFFLMLRYYALERMKKKDVSSSDGSSSGSSKQHMLQTNEKS

[Multiple Choices]
A. Dbf4-dependent protein kinase complex
B. neuronal cell body
C. plasma membrane
D. acrosomal membrane
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

> The exact-matching UniProt entry annotates the protein to the cell membrane and records plasma membrane as a GO cellular-component annotation. The localization is supported by database annotation, though the evidence is transferred or computational rather than a direct experimental localization shown here.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The signal peptide and multiple hydrophobic transmembrane segments support a membrane protein, consistent with an adhesion GPCR. They do not by themselves establish plasma membrane rather than another membrane compartment.


**Missing item-specific fact**

> The protein-specific localization annotation or experimental evidence establishing its cellular location is not supplied in the question.


**Reason**

> Sequence reasoning meaningfully favors a membrane-associated choice over the kinase complex and neuronal cell body, but resolving plasma membrane versus the specialized acrosomal membrane requires protein-specific localization information not given in the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence supports membrane localization broadly, but the supplied choices do not provide evidence that this protein is associated with sperm or the acrosome; reviewer-only annotations support plasma membrane.


### Important caveats

- The matching historical UniProt record annotates cell membrane and plasma membrane, but the cell-membrane localization is transferred from another UniProt entry and the GO annotation is IEA.
- The precise historical source snapshot used by the question author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The signal peptide and multiple hydrophobic transmembrane segments support a membrane protein, consistent with an adhesion GPCR. They do not by themselves establish plasma membrane rather than another membrane compartment.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific localization annotation or experimental evidence establishing its cellular location is not supplied in the question.",
    "reason": "Sequence reasoning meaningfully favors a membrane-associated choice over the kinase complex and neuronal cell body, but resolving plasma membrane versus the specialized acrosomal membrane requires protein-specific localization information not given in the input."
  },
  "case_id": "GO_cellular_component_0000",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact-matching UniProt entry annotates the protein to the cell membrane and records plasma membrane as a GO cellular-component annotation. The localization is supported by database annotation, though the evidence is transferred or computational rather than a direct experimental localization shown here."
  },
  "important_caveats": [
    "The matching historical UniProt record annotates cell membrane and plasma membrane, but the cell-membrane localization is transferred from another UniProt entry and the GO annotation is IEA.",
    "The precise historical source snapshot used by the question author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence supports membrane localization broadly, but the supplied choices do not provide evidence that this protein is associated with sperm or the acrosome; reviewer-only annotations support plasma membrane."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0000",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact-matching UniProt entry annotates the protein to the cell membrane and records plasma membrane as a GO cellular-component annotation. The localization is supported by database annotation, though the evidence is transferred or computational rather than a direct experimental localization shown here.",
    "evidence_ids": ["C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The signal peptide and multiple hydrophobic transmembrane segments support a membrane protein, consistent with an adhesion GPCR. They do not by themselves establish plasma membrane rather than another membrane compartment.",
    "missing_item_specific_fact": "The protein-specific localization annotation or experimental evidence establishing its cellular location is not supplied in the question.",
    "reason": "Sequence reasoning meaningfully favors a membrane-associated choice over the kinase complex and neuronal cell body, but resolving plasma membrane versus the specialized acrosomal membrane requires protein-specific localization information not given in the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence supports membrane localization broadly, but the supplied choices do not provide evidence that this protein is associated with sperm or the acrosome; reviewer-only annotations support plasma membrane."
  },
  "important_caveats": [
    "The matching historical UniProt record annotates cell membrane and plasma membrane, but the cell-membrane localization is transferred from another UniProt entry and the GO annotation is IEA.",
    "The precise historical source snapshot used by the question author is unknown."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (Q59I63, ADGRG1/GPR56 from Danio rerio) annotates the protein as a 'Cell membrane; Multi-pass membrane protein' (C5/H4) with GO:0005886 (plasma membrane) (C6/H5). The protein is identified as an Adhesion G protein-coupled receptor, a family universally localized to the plasma membrane. The evidence codes are ECO:0000250 (similarity to human ortholog Q9Y653) and ECO:0000255 (rule-based topology prediction), which are computational/similarity-based rather than direct experimental evidence for the zebrafish protein. However, GPCR localization to the plasma membrane is a universal biological principle, and the 7TM architecture visible in the sequence independently confirms this. The expected answer C (plasma membrane) is scientifically well-supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains seven distinct hydrophobic stretches of ~20-25 residues arranged in the canonical 7-transmembrane (7TM) GPCR architecture, preceded by a large extracellular N-terminal domain. The 7TM topology is a well-known structural signature: any protein with seven membrane-spanning helices in this arrangement is a GPCR, and all GPCRs reside at the plasma membrane. This reasoning chain (count hydrophobic segments → identify 7TM topology → GPCR → plasma membrane) is general biological knowledge. The distractors are eliminable by general reasoning: a Dbf4-dependent kinase complex (A) is nuclear with no TM domains; 'neuronal cell body' (B) denotes a subcellular region (soma), not a membrane compartment; acrosomal membrane (D) is a sperm-specific organelle incompatible with a broadly expressed receptor.


**Missing item-specific fact**

> None required. The 7TM architecture is directly observable in the sequence and the GPCR→plasma membrane mapping is general biology, not an item-specific annotation lookup.


**Reason**

> A model with knowledge of membrane protein topology can identify the seven hydrophobic segments in the sequence, recognize the 7TM GPCR fold, and conclude plasma membrane localization without needing to know the specific protein identity or its database annotation. The distractors are eliminated by general cell biology (kinase complexes are nuclear; acrosomal membranes are sperm-specific; 'neuronal cell body' is a soma region, not a membrane).


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The 7TM architecture unambiguously identifies a GPCR, whose primary cellular component is the plasma membrane. Option B (neuronal cell body) might seem tangentially relevant because ADGRG1 is expressed in neural cells, but as a GO Cellular Component term it denotes the soma region rather than the membrane, and the 7TM topology places the protein at the membrane itself. Options A and D are structurally incompatible with a multi-pass membrane protein. No alternative answer is defensible.


### Important caveats

- The UniProt subcellular location annotation uses ECO:0000250 (inferred by similarity to human Q9Y653) and ECO:0000255 (rule-based topology), not direct experimental evidence for the zebrafish protein. However, the universal GPCR-plasma membrane association and the visible 7TM sequence architecture provide independent confirmation.
- The GO annotation evidence is ISS/IEA (inferred from sequence similarity or electronic annotation), not direct experimental localization.
- The protein is a precursor with autoproteolytic cleavage (GPS motif), yielding N- and C-terminal fragments; both remain membrane-associated, so this does not alter the plasma membrane assignment.
- The reviewer-only accession (Q59I63) was inferred from dataset metadata and was not provided to the evaluated model; the model must reason from sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains seven distinct hydrophobic stretches of ~20-25 residues arranged in the canonical 7-transmembrane (7TM) GPCR architecture, preceded by a large extracellular N-terminal domain. The 7TM topology is a well-known structural signature: any protein with seven membrane-spanning helices in this arrangement is a GPCR, and all GPCRs reside at the plasma membrane. This reasoning chain (count hydrophobic segments → identify 7TM topology → GPCR → plasma membrane) is general biological knowledge. The distractors are eliminable by general reasoning: a Dbf4-dependent kinase complex (A) is nuclear with no TM domains; 'neuronal cell body' (B) denotes a subcellular region (soma), not a membrane compartment; acrosomal membrane (D) is a sperm-specific organelle incompatible with a broadly expressed receptor.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None required. The 7TM architecture is directly observable in the sequence and the GPCR→plasma membrane mapping is general biology, not an item-specific annotation lookup.",
    "reason": "A model with knowledge of membrane protein topology can identify the seven hydrophobic segments in the sequence, recognize the 7TM GPCR fold, and conclude plasma membrane localization without needing to know the specific protein identity or its database annotation. The distractors are eliminated by general cell biology (kinase complexes are nuclear; acrosomal membranes are sperm-specific; 'neuronal cell body' is a soma region, not a membrane)."
  },
  "case_id": "GO_cellular_component_0000",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H4",
      "H5",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (Q59I63, ADGRG1/GPR56 from Danio rerio) annotates the protein as a 'Cell membrane; Multi-pass membrane protein' (C5/H4) with GO:0005886 (plasma membrane) (C6/H5). The protein is identified as an Adhesion G protein-coupled receptor, a family universally localized to the plasma membrane. The evidence codes are ECO:0000250 (similarity to human ortholog Q9Y653) and ECO:0000255 (rule-based topology prediction), which are computational/similarity-based rather than direct experimental evidence for the zebrafish protein. However, GPCR localization to the plasma membrane is a universal biological principle, and the 7TM architecture visible in the sequence independently confirms this. The expected answer C (plasma membrane) is scientifically well-supported."
  },
  "important_caveats": [
    "The UniProt subcellular location annotation uses ECO:0000250 (inferred by similarity to human Q9Y653) and ECO:0000255 (rule-based topology), not direct experimental evidence for the zebrafish protein. However, the universal GPCR-plasma membrane association and the visible 7TM sequence architecture provide independent confirmation.",
    "The GO annotation evidence is ISS/IEA (inferred from sequence similarity or electronic annotation), not direct experimental localization.",
    "The protein is a precursor with autoproteolytic cleavage (GPS motif), yielding N- and C-terminal fragments; both remain membrane-associated, so this does not alter the plasma membrane assignment.",
    "The reviewer-only accession (Q59I63) was inferred from dataset metadata and was not provided to the evaluated model; the model must reason from sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The 7TM architecture unambiguously identifies a GPCR, whose primary cellular component is the plasma membrane. Option B (neuronal cell body) might seem tangentially relevant because ADGRG1 is expressed in neural cells, but as a GO Cellular Component term it denotes the soma region rather than the membrane, and the 7TM topology places the protein at the membrane itself. Options A and D are structurally incompatible with a multi-pass membrane protein. No alternative answer is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0000",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (Q59I63, ADGRG1/GPR56 from Danio rerio) annotates the protein as a 'Cell membrane; Multi-pass membrane protein' (C5/H4) with GO:0005886 (plasma membrane) (C6/H5). The protein is identified as an Adhesion G protein-coupled receptor, a family universally localized to the plasma membrane. The evidence codes are ECO:0000250 (similarity to human ortholog Q9Y653) and ECO:0000255 (rule-based topology prediction), which are computational/similarity-based rather than direct experimental evidence for the zebrafish protein. However, GPCR localization to the plasma membrane is a universal biological principle, and the 7TM architecture visible in the sequence independently confirms this. The expected answer C (plasma membrane) is scientifically well-supported.",
    "evidence_ids": ["C4", "C5", "C6", "H4", "H5", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains seven distinct hydrophobic stretches of ~20-25 residues arranged in the canonical 7-transmembrane (7TM) GPCR architecture, preceded by a large extracellular N-terminal domain. The 7TM topology is a well-known structural signature: any protein with seven membrane-spanning helices in this arrangement is a GPCR, and all GPCRs reside at the plasma membrane. This reasoning chain (count hydrophobic segments → identify 7TM topology → GPCR → plasma membrane) is general biological knowledge. The distractors are eliminable by general reasoning: a Dbf4-dependent kinase complex (A) is nuclear with no TM domains; 'neuronal cell body' (B) denotes a subcellular region (soma), not a membrane compartment; acrosomal membrane (D) is a sperm-specific organelle incompatible with a broadly expressed receptor.",
    "missing_item_specific_fact": "None required. The 7TM architecture is directly observable in the sequence and the GPCR→plasma membrane mapping is general biology, not an item-specific annotation lookup.",
    "reason": "A model with knowledge of membrane protein topology can identify the seven hydrophobic segments in the sequence, recognize the 7TM GPCR fold, and conclude plasma membrane localization without needing to know the specific protein identity or its database annotation. The distractors are eliminated by general cell biology (kinase complexes are nuclear; acrosomal membranes are sperm-specific; 'neuronal cell body' is a soma region, not a membrane)."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The 7TM architecture unambiguously identifies a GPCR, whose primary cellular component is the plasma membrane. Option B (neuronal cell body) might seem tangentially relevant because ADGRG1 is expressed in neural cells, but as a GO Cellular Component term it denotes the soma region rather than the membrane, and the 7TM topology places the protein at the membrane itself. Options A and D are structurally incompatible with a multi-pass membrane protein. No alternative answer is defensible."
  },
  "important_caveats": [
    "The UniProt subcellular location annotation uses ECO:0000250 (inferred by similarity to human Q9Y653) and ECO:0000255 (rule-based topology), not direct experimental evidence for the zebrafish protein. However, the universal GPCR-plasma membrane association and the visible 7TM sequence architecture provide independent confirmation.",
    "The GO annotation evidence is ISS/IEA (inferred from sequence similarity or electronic annotation), not direct experimental localization.",
    "The protein is a precursor with autoproteolytic cleavage (GPS motif), yielding N- and C-terminal fragments; both remain membrane-associated, so this does not alter the plasma membrane assignment.",
    "The reviewer-only accession (Q59I63) was inferred from dataset metadata and was not provided to the evaluated model; the model must reason from sequence alone."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt annotation places the protein at the cell membrane and describes it as a multipass membrane protein (C5). The plasma-membrane GO annotation is similarity-inferred (ISS), not direct experimental evidence (C6), but supports the keyed choice.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an extracellular N-terminal region followed by numerous strongly hydrophobic transmembrane segments, consistent with a multipass cell-surface receptor. Transferable knowledge about membrane-receptor architecture therefore favors plasma membrane (C) over a kinase complex (A), neuronal cell body (B), or the specialized acrosomal membrane (D).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence itself provides a meaningful membrane-protein signal, and receptor-family-level knowledge supports a cell-surface location among these choices. Exact localization is not proven by sequence alone, but distinguishing C from these alternatives does not require recalling this protein’s database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The many transmembrane segments support a membrane location, while the sequence gives no comparable reason to select the acrosomal membrane or neuronal cell body specifically.


### Important caveats

- The supplied annotations include similarity-based and computational evidence; they do not establish direct experimental localization.
- A multipass membrane sequence alone does not prove exclusive residence at the plasma membrane, but plasma membrane is the best-supported offered choice.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an extracellular N-terminal region followed by numerous strongly hydrophobic transmembrane segments, consistent with a multipass cell-surface receptor. Transferable knowledge about membrane-receptor architecture therefore favors plasma membrane (C) over a kinase complex (A), neuronal cell body (B), or the specialized acrosomal membrane (D).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence itself provides a meaningful membrane-protein signal, and receptor-family-level knowledge supports a cell-surface location among these choices. Exact localization is not proven by sequence alone, but distinguishing C from these alternatives does not require recalling this protein’s database record."
  },
  "case_id": "GO_cellular_component_0000",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation places the protein at the cell membrane and describes it as a multipass membrane protein (C5). The plasma-membrane GO annotation is similarity-inferred (ISS), not direct experimental evidence (C6), but supports the keyed choice."
  },
  "important_caveats": [
    "The supplied annotations include similarity-based and computational evidence; they do not establish direct experimental localization.",
    "A multipass membrane sequence alone does not prove exclusive residence at the plasma membrane, but plasma membrane is the best-supported offered choice."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The many transmembrane segments support a membrane location, while the sequence gives no comparable reason to select the acrosomal membrane or neuronal cell body specifically."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0000",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation places the protein at the cell membrane and describes it as a multipass membrane protein (C5). The plasma-membrane GO annotation is similarity-inferred (ISS), not direct experimental evidence (C6), but supports the keyed choice.",
    "evidence_ids": ["C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an extracellular N-terminal region followed by numerous strongly hydrophobic transmembrane segments, consistent with a multipass cell-surface receptor. Transferable knowledge about membrane-receptor architecture therefore favors plasma membrane (C) over a kinase complex (A), neuronal cell body (B), or the specialized acrosomal membrane (D).",
    "missing_item_specific_fact": "",
    "reason": "The sequence itself provides a meaningful membrane-protein signal, and receptor-family-level knowledge supports a cell-surface location among these choices. Exact localization is not proven by sequence alone, but distinguishing C from these alternatives does not require recalling this protein’s database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The many transmembrane segments support a membrane location, while the sequence gives no comparable reason to select the acrosomal membrane or neuronal cell body specifically."
  },
  "important_caveats": [
    "The supplied annotations include similarity-based and computational evidence; they do not establish direct experimental localization.",
    "A multipass membrane sequence alone does not prove exclusive residence at the plasma membrane, but plasma membrane is the best-supported offered choice."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry for this sequence (Q59I63, zebrafish ADGRG1/GPR56) annotates it as 'Cell membrane; Multi-pass membrane protein' (evidence C5, H4). The GO cross-reference GO:0005886 'plasma membrane' is assigned (C6, H5). GO:0005886 has 'cell membrane' as an EXACT synonym (GO2). The annotation evidence code is ISS/IEA (transferred from human Q9Y653), which is computational inference from homology rather than direct experimental evidence for this specific zebrafish protein, but the protein is unambiguously a 7-TM GPCR with a signal peptide, and all GPCRs are plasma membrane proteins. The expected answer C is well-supported.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits hallmark features of a 7-transmembrane GPCR: (1) an N-terminal signal peptide (MKQNPAKTARMWIIICLLFVLGQA, ~20 residues with a hydrophobic core and cleavage site), indicating entry into the ER/secretory pathway; (2) multiple long hydrophobic stretches distributed throughout the ~648-residue sequence, consistent with 7 TM helices. All GPCRs are multi-pass plasma membrane proteins. This directly supports choice C (plasma membrane). Choice A (Dbf4-dependent protein kinase complex) is a nuclear complex for DNA replication initiation — incompatible with a signal-peptide-containing multi-TM protein. Choice D (acrosomal membrane) is a specialized sperm-specific lysosomal membrane — no sequence feature suggests sperm-specific targeting. Choice B (neuronal cell body) describes a cell-type compartment rather than the subcellular localization of the protein itself; a multi-pass membrane protein's GO CC annotation is the membrane it resides in (plasma membrane), not the cell type expressing it. Family-level knowledge (all GPCRs → plasma membrane) plus sequence architecture (signal peptide + 7 TM domains) meaningfully and uniquely distinguishes C from all other options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the GPCR architecture from the sequence (signal peptide + multiple TM domains) and apply the universal rule that GPCRs are plasma membrane proteins. This family-level inference directly eliminates A (nuclear kinase complex), D (sperm-specific acrosome), and B (cell-type descriptor rather than subcellular membrane location). No target-specific database lookup is needed.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence clearly encodes a multi-pass transmembrane protein with a signal peptide. Among the four options, only 'plasma membrane' correctly describes the subcellular localization of such a protein. 'Neuronal cell body' describes a cell-type context, not the protein's membrane localization. The other two options are clearly incompatible with the sequence features.


### Important caveats

- The UniProt annotation uses ISS/IEA evidence (transferred from human ADGRG1 Q9Y653), not direct experimental localization in zebrafish. However, the GPCR-to-plasma-membrane mapping is a universal biological principle.
- ADGRG1 is indeed expressed in neural cells (oligodendrocytes, Schwann cells), so 'neuronal cell body' is not biologically nonsensical as a tissue context, but it is not the correct GO Cellular Component annotation for a multi-pass membrane protein.
- The sequence is 648 residues; the reviewer confirms it matches UniProt Q59I63 sequence version 2 exactly.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits hallmark features of a 7-transmembrane GPCR: (1) an N-terminal signal peptide (MKQNPAKTARMWIIICLLFVLGQA, ~20 residues with a hydrophobic core and cleavage site), indicating entry into the ER/secretory pathway; (2) multiple long hydrophobic stretches distributed throughout the ~648-residue sequence, consistent with 7 TM helices. All GPCRs are multi-pass plasma membrane proteins. This directly supports choice C (plasma membrane). Choice A (Dbf4-dependent protein kinase complex) is a nuclear complex for DNA replication initiation — incompatible with a signal-peptide-containing multi-TM protein. Choice D (acrosomal membrane) is a specialized sperm-specific lysosomal membrane — no sequence feature suggests sperm-specific targeting. Choice B (neuronal cell body) describes a cell-type compartment rather than the subcellular localization of the protein itself; a multi-pass membrane protein's GO CC annotation is the membrane it resides in (plasma membrane), not the cell type expressing it. Family-level knowledge (all GPCRs → plasma membrane) plus sequence architecture (signal peptide + 7 TM domains) meaningfully and uniquely distinguishes C from all other options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the GPCR architecture from the sequence (signal peptide + multiple TM domains) and apply the universal rule that GPCRs are plasma membrane proteins. This family-level inference directly eliminates A (nuclear kinase complex), D (sperm-specific acrosome), and B (cell-type descriptor rather than subcellular membrane location). No target-specific database lookup is needed."
  },
  "case_id": "GO_cellular_component_0000",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry for this sequence (Q59I63, zebrafish ADGRG1/GPR56) annotates it as 'Cell membrane; Multi-pass membrane protein' (evidence C5, H4). The GO cross-reference GO:0005886 'plasma membrane' is assigned (C6, H5). GO:0005886 has 'cell membrane' as an EXACT synonym (GO2). The annotation evidence code is ISS/IEA (transferred from human Q9Y653), which is computational inference from homology rather than direct experimental evidence for this specific zebrafish protein, but the protein is unambiguously a 7-TM GPCR with a signal peptide, and all GPCRs are plasma membrane proteins. The expected answer C is well-supported."
  },
  "important_caveats": [
    "The UniProt annotation uses ISS/IEA evidence (transferred from human ADGRG1 Q9Y653), not direct experimental localization in zebrafish. However, the GPCR-to-plasma-membrane mapping is a universal biological principle.",
    "ADGRG1 is indeed expressed in neural cells (oligodendrocytes, Schwann cells), so 'neuronal cell body' is not biologically nonsensical as a tissue context, but it is not the correct GO Cellular Component annotation for a multi-pass membrane protein.",
    "The sequence is 648 residues; the reviewer confirms it matches UniProt Q59I63 sequence version 2 exactly."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence clearly encodes a multi-pass transmembrane protein with a signal peptide. Among the four options, only 'plasma membrane' correctly describes the subcellular localization of such a protein. 'Neuronal cell body' describes a cell-type context, not the protein's membrane localization. The other two options are clearly incompatible with the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0000",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry for this sequence (Q59I63, zebrafish ADGRG1/GPR56) annotates it as 'Cell membrane; Multi-pass membrane protein' (evidence C5, H4). The GO cross-reference GO:0005886 'plasma membrane' is assigned (C6, H5). GO:0005886 has 'cell membrane' as an EXACT synonym (GO2). The annotation evidence code is ISS/IEA (transferred from human Q9Y653), which is computational inference from homology rather than direct experimental evidence for this specific zebrafish protein, but the protein is unambiguously a 7-TM GPCR with a signal peptide, and all GPCRs are plasma membrane proteins. The expected answer C is well-supported.",
    "evidence_ids": ["C5", "C6", "H4", "H5", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits hallmark features of a 7-transmembrane GPCR: (1) an N-terminal signal peptide (MKQNPAKTARMWIIICLLFVLGQA, ~20 residues with a hydrophobic core and cleavage site), indicating entry into the ER/secretory pathway; (2) multiple long hydrophobic stretches distributed throughout the ~648-residue sequence, consistent with 7 TM helices. All GPCRs are multi-pass plasma membrane proteins. This directly supports choice C (plasma membrane). Choice A (Dbf4-dependent protein kinase complex) is a nuclear complex for DNA replication initiation — incompatible with a signal-peptide-containing multi-TM protein. Choice D (acrosomal membrane) is a specialized sperm-specific lysosomal membrane — no sequence feature suggests sperm-specific targeting. Choice B (neuronal cell body) describes a cell-type compartment rather than the subcellular localization of the protein itself; a multi-pass membrane protein's GO CC annotation is the membrane it resides in (plasma membrane), not the cell type expressing it. Family-level knowledge (all GPCRs → plasma membrane) plus sequence architecture (signal peptide + 7 TM domains) meaningfully and uniquely distinguishes C from all other options.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the GPCR architecture from the sequence (signal peptide + multiple TM domains) and apply the universal rule that GPCRs are plasma membrane proteins. This family-level inference directly eliminates A (nuclear kinase complex), D (sperm-specific acrosome), and B (cell-type descriptor rather than subcellular membrane location). No target-specific database lookup is needed."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence clearly encodes a multi-pass transmembrane protein with a signal peptide. Among the four options, only 'plasma membrane' correctly describes the subcellular localization of such a protein. 'Neuronal cell body' describes a cell-type context, not the protein's membrane localization. The other two options are clearly incompatible with the sequence features."
  },
  "important_caveats": [
    "The UniProt annotation uses ISS/IEA evidence (transferred from human ADGRG1 Q9Y653), not direct experimental localization in zebrafish. However, the GPCR-to-plasma-membrane mapping is a universal biological principle.",
    "ADGRG1 is indeed expressed in neural cells (oligodendrocytes, Schwann cells), so 'neuronal cell body' is not biologically nonsensical as a tissue context, but it is not the correct GO Cellular Component annotation for a multi-pass membrane protein.",
    "The sequence is 648 residues; the reviewer confirms it matches UniProt Q59I63 sequence version 2 exactly."
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
  "requested_accession": "Q59I63",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "0aeb6f4623306585d8f08066b919f9b296ac122794d0737052b31610ace39de4",
  "benchmark_sequence_length": 648,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 121,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-06-18",
    "sequenceVersion": 2
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe",
  "current_source_sequence_sha256": "0aeb6f4623306585d8f08066b919f9b296ac122794d0737052b31610ace39de4",
  "current_source_sequence_length": 648,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 119,
  "selected_historical_version": {
    "accession": "Q59I63",
    "database": "Swiss-Prot",
    "entryVersion": 119,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "AGRG1_DANRE",
    "sequenceVersion": 2
  },
  "selected_historical_record_sha256": "b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0",
  "selected_historical_source_sequence_sha256": "0aeb6f4623306585d8f08066b919f9b296ac122794d0737052b31610ace39de4",
  "selected_historical_source_sequence_length": 648,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 119,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q59I63.json",
  "source_sha256": "a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe",
  "retrieved_utc": "2026-11-02T04:31:01.992326+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"Q59I63\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q59I63.json",
  "source_sha256": "a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe",
  "retrieved_utc": "2026-11-02T04:31:01.992326+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":121,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-06-18\",\"sequenceVersion\":2}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q59I63.json",
  "source_sha256": "a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe",
  "retrieved_utc": "2026-11-02T04:31:01.992326+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Zebrafish\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Euteleostomi\",\"Actinopterygii\",\"Neopterygii\",\"Teleostei\",\"Ostariophysi\",\"Cypriniformes\",\"Danionidae\",\"Danioninae\",\"Danio\"],\"scientificName\":\"Danio rerio\",\"synonyms\":[\"Brachydanio rerio\"],\"taxonId\":7955}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q59I63.json",
  "source_sha256": "a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe",
  "retrieved_utc": "2026-11-02T04:31:01.992326+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"25607772\",\"source\":\"PubMed\"}],\"value\":\"G protein-coupled receptor 56\"}}],\"contains\":[{\"alternativeNames\":[{\"fullName\":{\"value\":\"ADGRG1 N-terminal fragment\"},\"shortNames\":[{\"value\":\"ADGRG1 NT\"}]}],\"recommendedName\":{\"fullName\":{\"value\":\"Adhesion G protein-coupled receptor G1, N-terminal fragment\"}}},{\"alternativeNames\":[{\"fullName\":{\"value\":\"ADGRG1 C-terminal fragment\"},\"shortNames\":[{\"value\":\"ADGRG1 CT\"}]}],\"recommendedName\":{\"fullName\":{\"value\":\"Adhesion G protein-coupled receptor G1, C-terminal fragment\"}}}],\"flag\":\"Precursor\",\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Adhesion G protein-coupled receptor G1\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q59I63.json",
  "source_sha256": "a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe",
  "retrieved_utc": "2026-11-02T04:31:01.992326+00:00",
  "json_pointer": "/comments/3",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9Y653\",\"source\":\"UniProtKB\"}],\"id\":\"SL-0039\",\"value\":\"Cell membrane\"},\"topology\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"id\":\"SL-9909\",\"value\":\"Multi-pass membrane protein\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q59I63.json",
  "source_sha256": "a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe",
  "retrieved_utc": "2026-11-02T04:31:01.992326+00:00",
  "json_pointer": "/uniProtKBCrossReferences/26",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005886\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:plasma membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISS:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q59I63.json",
  "source_sha256": "a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe",
  "retrieved_utc": "2026-11-02T04:31:01.992326+00:00",
  "json_pointer": "/references/2",
  "excerpt": "{\"citation\":{\"authors\":[\"Ackerman S.D.\",\"Garcia C.\",\"Piao X.\",\"Gutmann D.H.\",\"Monk K.R.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"25607772\"},{\"database\":\"DOI\",\"id\":\"10.1038/ncomms7122\"}],\"citationType\":\"journal article\",\"firstPage\":\"6122\",\"id\":\"25607772\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"6122\",\"publicationDate\":\"2015\",\"title\":\"The adhesion GPCR Gpr56 regulates oligodendrocyte development via interactions with Galpha12/13 and RhoA.\",\"volume\":\"6\"},\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"DEVELOPMENTAL STAGE\",\"DISRUPTION PHENOTYPE\",\"MUTAGENESIS OF 325-ASN-TRP-326\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119",
  "source_sha256": "b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0",
  "retrieved_utc": "2026-11-02T04:31:04.584714+00:00",
  "source_locator": "lines 1-24",
  "excerpt": "ID   AGRG1_DANRE             Reviewed;         648 AA.\nAC   Q59I63; A0A0R4IXA8; A0A8M2BDY6; F1QZM9;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-JUN-2025, sequence version 2.\nDT   28-JAN-2026, entry version 119.\nDE   RecName: Full=Adhesion G-protein coupled receptor G1 {ECO:0000305};\nDE   AltName: Full=G-protein coupled receptor 56 {ECO:0000303|PubMed:25607772};\nDE   Contains:\nDE     RecName: Full=Adhesion G-protein coupled receptor G1, N-terminal fragment;\nDE     AltName: Full=ADGRG1 N-terminal fragment;\nDE              Short=ADGRG1 NT;\nDE   Contains:\nDE     RecName: Full=Adhesion G-protein coupled receptor G1, C-terminal fragment;\nDE     AltName: Full=ADGRG1 C-terminal fragment;\nDE              Short=ADGRG1 CT;\nDE   Flags: Precursor;\nGN   Name=adgrg1 {ECO:0000303|PubMed:29367382,\nGN   ECO:0000312|ZFIN:ZDB-GENE-030131-3671};\nGN   Synonyms=gpr56 {ECO:0000303|PubMed:25607772};\nOS   Danio rerio (Zebrafish) (Brachydanio rerio).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi;\nOC   Actinopterygii; Neopterygii; Teleostei; Ostariophysi; Cypriniformes;\nOC   Danionidae; Danioninae; Danio.\nOX   NCBI_TaxID=7955;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 119,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119",
  "source_sha256": "b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0",
  "retrieved_utc": "2026-11-02T04:31:04.584714+00:00",
  "source_locator": "lines 70-77",
  "excerpt": "RN   [3]\nRP   FUNCTION, DEVELOPMENTAL STAGE, DISRUPTION PHENOTYPE, AND MUTAGENESIS OF\nRP   325-ASN-TRP-326.\nRX   PubMed=25607772; DOI=10.1038/ncomms7122;\nRA   Ackerman S.D., Garcia C., Piao X., Gutmann D.H., Monk K.R.;\nRT   \"The adhesion GPCR Gpr56 regulates oligodendrocyte development via\nRT   interactions with Galpha12/13 and RhoA.\";\nRL   Nat. Commun. 6:6122-6122(2015).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 119,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119",
  "source_sha256": "b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0",
  "retrieved_utc": "2026-11-02T04:31:04.584714+00:00",
  "source_locator": "lines 78-85",
  "excerpt": "RN   [4]\nRP   FUNCTION.\nRX   PubMed=29367382; DOI=10.1084/jem.20161714;\nRA   Ackerman S.D., Luo R., Poitelon Y., Mogha A., Harty B.L., D'Rozario M.,\nRA   Sanchez N.E., Lakkaraju A.K.K., Gamble P., Li J., Qu J., MacEwan M.R.,\nRA   Ray W.Z., Aguzzi A., Feltri M.L., Piao X., Monk K.R.;\nRT   \"GPR56/ADGRG1 regulates development and maintenance of peripheral myelin.\";\nRL   J. Exp. Med. 215:941-961(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 119,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119",
  "source_sha256": "b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0",
  "retrieved_utc": "2026-11-02T04:31:04.584714+00:00",
  "source_locator": "lines 121-122",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000250|UniProtKB:Q9Y653};\nCC       Multi-pass membrane protein {ECO:0000255}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 119,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119",
  "source_sha256": "b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0",
  "retrieved_utc": "2026-11-02T04:31:04.584714+00:00",
  "source_locator": "lines 168-168",
  "excerpt": "DR   GO; GO:0005886; C:plasma membrane; IEA:UniProtKB-SubCell.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 119,
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
  "source_locator": "lines 14812-14819",
  "excerpt": "[Term]\nid: GO:0002080\nname: acrosomal membrane\nnamespace: cellular_component\ndef: \"The membrane that surrounds the acrosomal lumen. The acrosome is a special type of lysosome in the head of a spermatozoon that contains acid hydrolases and is concerned with the breakdown of the outer membrane of the ovum during fertilization.\" [GOC:dph]\nis_a: GO:0030667 ! secretory granule membrane\nrelationship: part_of GO:0001669 ! acrosomal vesicle\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0002080"
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
  "source_locator": "lines 60420-60454",
  "excerpt": "[Term]\nid: GO:0005886\nname: plasma membrane\nnamespace: cellular_component\nalt_id: GO:0005887\nalt_id: GO:0005904\ndef: \"The membrane surrounding a cell that separates the cell from its external environment. It consists of a phospholipid bilayer and associated proteins.\" [ISBN:0716731363]\nsubset: goslim_agr\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_generic\nsubset: goslim_metagenomics\nsubset: goslim_mouse\nsubset: goslim_plant\nsubset: goslim_plant_ribbon\nsubset: goslim_prokaryote\nsubset: goslim_prokaryote_ribbon\nsubset: goslim_yeast\nsynonym: \"bacterial inner membrane\" NARROW []\nsynonym: \"cell membrane\" EXACT []\nsynonym: \"cellular membrane\" EXACT [NIF_Subcellular:sao6433132645]\nsynonym: \"cytoplasmic membrane\" EXACT []\nsynonym: \"inner endospore membrane\" NARROW []\nsynonym: \"integral component of plasma membrane\" NARROW []\nsynonym: \"integral to plasma membrane\" NARROW []\nsynonym: \"juxtamembrane\" BROAD []\nsynonym: \"plasma membrane lipid bilayer\" NARROW [GOC:mah]\nsynonym: \"plasmalemma\" EXACT []\nxref: NIF_Subcellular:sao1663586795\nxref: Wikipedia:Cell_membrane\nis_a: GO:0016020 ! membrane\nrelationship: part_of GO:0071944 ! cell periphery\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0005886"
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
  "source_locator": "lines 176442-176452",
  "excerpt": "[Term]\nid: GO:0031431\nname: Dbf4-dependent protein kinase complex\nnamespace: cellular_component\ndef: \"A heterodimeric protein complex required for the activation of DNA replication origins; comprises a catalytic subunit and a regulatory subunit (in Saccharomyces, Cdc7p and Dbf4p, respectively); complexes identified in other species generally contain proteins related to the Saccharomyces proteins.\" [PMID:12045100]\nsynonym: \"Cdc7-Dbf4 complex\" NARROW []\nsynonym: \"DDK\" EXACT []\nsynonym: \"Hsk1-Dfp1 kinase complex\" NARROW []\nis_a: GO:0140513 ! nuclear protein-containing complex\nis_a: GO:1902554 ! serine/threonine protein kinase complex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0031431"
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
  "source_locator": "lines 243262-243275",
  "excerpt": "[Term]\nid: GO:0043025\nname: neuronal cell body\nnamespace: cellular_component\ndef: \"The portion of a neuron that includes the nucleus, but excludes cell projections such as axons and dendrites.\" [GOC:curators]\ncomment: Note that 'cell body' and 'cell soma' are not used in the literature for cells that lack projections, nor for some cells (e.g. yeast with mating projections) that do have projections.\nsubset: goslim_pir\nsynonym: \"neuron cell body\" EXACT []\nsynonym: \"neuronal cell soma\" EXACT []\nxref: NIF_Subcellular:sao1044911821\nxref: Wikipedia:Soma_(biology)\nis_a: GO:0044297 ! cell body\nrelationship: part_of GO:0036477 ! somatodendritic compartment\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0043025"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 0. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
