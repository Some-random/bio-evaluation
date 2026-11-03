# GO_cellular_component_0150: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/GO_cellular_component_0150.txt)

**Task:** `GO_cellular_component`  
**Author key, unchanged:** **B** — plasma membrane

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
MTTSSDSAMVNHTPSPWYKFGFKSFAEFNTYVTFVFLGMSIMMVASAVTSAPDFLTRYYVYATGDPDAVAETPLFWNNANTFYNAGTYVLQVLTELFSLTPFMRRIPLSVRLFVGLGIPFAELLLIIIVPAATIKSQHGAIAVIMVVACVGGFSKALCDSCTNALVGPFPTKFMNGAQWGLTVIALLMSIIQIILKVSMGTSFHDILTMSRIYFGICIGIQLFAIFELAILRFNPFAQKYIAEYRAGAQRNAQNNESTLEETAPSMNEPAAGDIADLPATVDDKERALNEEEGDEVRAVTSEEFHVKRGAVLTATGDADKMVDLDQTGNITSTEQLLRASAASVFKRVYPMLVCVFLIYFTSLLTFPGVFFLVSTTSGWYMTVIVTLFNAGDFISRMVLMFRPLRPSPKVVVAGTLGRLIIIPFLVLCVRGIIRGEALPYVLITLLGLTNGYFGCMACIHCPRTTTLRYAGERSLAAMLSGISIMLGLCFGSNLSLAITLTH

[Multiple Choices]
A. host cell plasma membrane
B. plasma membrane
C. vacuolar membrane
D. microtubule
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

> The sequence-matched UniProt record annotates the protein to the cell membrane with experimental evidence and maps it to plasma membrane in GO. Its many transmembrane segments are also consistent with a membrane-localized transporter.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The many hydrophobic transmembrane segments support membrane localization, but do not distinguish the plasma membrane from a vacuolar membrane. The sequence alone also does not identify which cell's membrane is involved.


**Missing item-specific fact**

> The protein-specific localization evidence that this transporter resides at its own cell membrane, and the annotation mapping that location to plasma membrane.


**Reason**

> The choices require a precise cellular location that cannot be inferred from the transmembrane topology alone. Selecting B over other membrane-related possibilities depends on protein-specific localization information absent from the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports the protein's own cell membrane, corresponding to B; A specifically refers to a host cell membrane, while C and D are not supported.


### Important caveats

- The UniProt cell-membrane annotation cites experimental evidence; the GO plasma-membrane annotation is IEA (computationally assigned).
- The reviewer-only evidence matches the sequence, but the author's source snapshot is unknown and the accession was not provided in the question.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The many hydrophobic transmembrane segments support membrane localization, but do not distinguish the plasma membrane from a vacuolar membrane. The sequence alone also does not identify which cell's membrane is involved.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific localization evidence that this transporter resides at its own cell membrane, and the annotation mapping that location to plasma membrane.",
    "reason": "The choices require a precise cellular location that cannot be inferred from the transmembrane topology alone. Selecting B over other membrane-related possibilities depends on protein-specific localization information absent from the question."
  },
  "case_id": "GO_cellular_component_0150",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the protein to the cell membrane with experimental evidence and maps it to plasma membrane in GO. Its many transmembrane segments are also consistent with a membrane-localized transporter."
  },
  "important_caveats": [
    "The UniProt cell-membrane annotation cites experimental evidence; the GO plasma-membrane annotation is IEA (computationally assigned).",
    "The reviewer-only evidence matches the sequence, but the author's source snapshot is unknown and the accession was not provided in the question."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports the protein's own cell membrane, corresponding to B; A specifically refers to a host cell membrane, while C and D are not supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0150",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the protein to the cell membrane with experimental evidence and maps it to plasma membrane in GO. Its many transmembrane segments are also consistent with a membrane-localized transporter.",
    "evidence_ids": ["C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The many hydrophobic transmembrane segments support membrane localization, but do not distinguish the plasma membrane from a vacuolar membrane. The sequence alone also does not identify which cell's membrane is involved.",
    "missing_item_specific_fact": "The protein-specific localization evidence that this transporter resides at its own cell membrane, and the annotation mapping that location to plasma membrane.",
    "reason": "The choices require a precise cellular location that cannot be inferred from the transmembrane topology alone. Selecting B over other membrane-related possibilities depends on protein-specific localization information absent from the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports the protein's own cell membrane, corresponding to B; A specifically refers to a host cell membrane, while C and D are not supported."
  },
  "important_caveats": [
    "The UniProt cell-membrane annotation cites experimental evidence; the GO plasma-membrane annotation is IEA (computationally assigned).",
    "The reviewer-only evidence matches the sequence, but the author's source snapshot is unknown and the accession was not provided in the question."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q9GTP4 (CfNT2, Nucleoside transporter 2 from Crithidia fasciculata) is annotated as 'Cell membrane; Multi-pass membrane protein' with experimental evidence (ECO:0000269, PubMed:20037157). GO:0005886 (plasma membrane) is linked via IEA:UniProtKB-SubCell, and 'cell membrane' is an EXACT synonym of GO:0005886 (GO3). The protein is the organism's own nucleoside transporter, so 'plasma membrane' (B) is the correct GO term. Option A ('host cell plasma membrane', GO:0020002) applies to proteins localizing to a different cell's membrane (typically viral/parasitic context), not the organism's own membrane.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5), [GO3](#evidence-go3), [GO4](#evidence-go4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains ~11-12 long hydrophobic stretches consistent with multi-pass transmembrane topology, immediately eliminating microtubule (D). The protein belongs to the equilibrative nucleoside transporter (ENT) family, whose members import nucleosides from the extracellular milieu, requiring plasma membrane localization rather than vacuolar membrane (C). The protein is Crithidia fasciculata's own transporter for its own nucleoside uptake, so it resides in its own plasma membrane (B), not a 'host cell' plasma membrane (A), which by GO definition (GO:0020002, goslim_virus subset) refers to the membrane of a host cell distinct from the expressing organism.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The multi-pass TM architecture visible in the sequence eliminates microtubule. Recognizing the ENT family (long hydrophobic segments, characteristic topology) and knowing ENTs are plasma membrane importers argues against vacuolar membrane. The distinction between B and A follows from the biological meaning of 'host cell' (a different cell) versus the organism's own membrane—general reasoning about whose membrane a self-encoded transporter occupies.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and B are clearly distinguishable: 'host cell plasma membrane' (GO:0020002) is a goslim_virus term for proteins on a host cell's membrane, inapplicable to the organism's own transporter. Options C and D are eliminated by the multi-pass TM topology and transporter function. No ambiguity remains among the four choices.


### Important caveats

- The GO annotation for plasma membrane (GO:0005886) carries IEA:UniProtKB-SubCell evidence (inferred from UniProt's 'Cell membrane' annotation), but the underlying UniProt annotation itself is backed by experimental evidence (ECO:0000269, PubMed:20037157).
- The distinction between options A and B relies on understanding GO term semantics ('host cell' implies a different cell); this is general biological reasoning but also touches on GO ontology conventions.
- The protein was integrated into Swiss-Prot on 2025-02-05; the author's source snapshot date is unknown, though the sequence matches the current entry exactly.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains ~11-12 long hydrophobic stretches consistent with multi-pass transmembrane topology, immediately eliminating microtubule (D). The protein belongs to the equilibrative nucleoside transporter (ENT) family, whose members import nucleosides from the extracellular milieu, requiring plasma membrane localization rather than vacuolar membrane (C). The protein is Crithidia fasciculata's own transporter for its own nucleoside uptake, so it resides in its own plasma membrane (B), not a 'host cell' plasma membrane (A), which by GO definition (GO:0020002, goslim_virus subset) refers to the membrane of a host cell distinct from the expressing organism.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The multi-pass TM architecture visible in the sequence eliminates microtubule. Recognizing the ENT family (long hydrophobic segments, characteristic topology) and knowing ENTs are plasma membrane importers argues against vacuolar membrane. The distinction between B and A follows from the biological meaning of 'host cell' (a different cell) versus the organism's own membrane—general reasoning about whose membrane a self-encoded transporter occupies."
  },
  "case_id": "GO_cellular_component_0150",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5",
      "GO3",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q9GTP4 (CfNT2, Nucleoside transporter 2 from Crithidia fasciculata) is annotated as 'Cell membrane; Multi-pass membrane protein' with experimental evidence (ECO:0000269, PubMed:20037157). GO:0005886 (plasma membrane) is linked via IEA:UniProtKB-SubCell, and 'cell membrane' is an EXACT synonym of GO:0005886 (GO3). The protein is the organism's own nucleoside transporter, so 'plasma membrane' (B) is the correct GO term. Option A ('host cell plasma membrane', GO:0020002) applies to proteins localizing to a different cell's membrane (typically viral/parasitic context), not the organism's own membrane."
  },
  "important_caveats": [
    "The GO annotation for plasma membrane (GO:0005886) carries IEA:UniProtKB-SubCell evidence (inferred from UniProt's 'Cell membrane' annotation), but the underlying UniProt annotation itself is backed by experimental evidence (ECO:0000269, PubMed:20037157).",
    "The distinction between options A and B relies on understanding GO term semantics ('host cell' implies a different cell); this is general biological reasoning but also touches on GO ontology conventions.",
    "The protein was integrated into Swiss-Prot on 2025-02-05; the author's source snapshot date is unknown, though the sequence matches the current entry exactly."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and B are clearly distinguishable: 'host cell plasma membrane' (GO:0020002) is a goslim_virus term for proteins on a host cell's membrane, inapplicable to the organism's own transporter. Options C and D are eliminated by the multi-pass TM topology and transporter function. No ambiguity remains among the four choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0150",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q9GTP4 (CfNT2, Nucleoside transporter 2 from Crithidia fasciculata) is annotated as 'Cell membrane; Multi-pass membrane protein' with experimental evidence (ECO:0000269, PubMed:20037157). GO:0005886 (plasma membrane) is linked via IEA:UniProtKB-SubCell, and 'cell membrane' is an EXACT synonym of GO:0005886 (GO3). The protein is the organism's own nucleoside transporter, so 'plasma membrane' (B) is the correct GO term. Option A ('host cell plasma membrane', GO:0020002) applies to proteins localizing to a different cell's membrane (typically viral/parasitic context), not the organism's own membrane.",
    "evidence_ids": ["C5", "C6", "H4", "H5", "GO3", "GO4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains ~11-12 long hydrophobic stretches consistent with multi-pass transmembrane topology, immediately eliminating microtubule (D). The protein belongs to the equilibrative nucleoside transporter (ENT) family, whose members import nucleosides from the extracellular milieu, requiring plasma membrane localization rather than vacuolar membrane (C). The protein is Crithidia fasciculata's own transporter for its own nucleoside uptake, so it resides in its own plasma membrane (B), not a 'host cell' plasma membrane (A), which by GO definition (GO:0020002, goslim_virus subset) refers to the membrane of a host cell distinct from the expressing organism.",
    "missing_item_specific_fact": "",
    "reason": "The multi-pass TM architecture visible in the sequence eliminates microtubule. Recognizing the ENT family (long hydrophobic segments, characteristic topology) and knowing ENTs are plasma membrane importers argues against vacuolar membrane. The distinction between B and A follows from the biological meaning of 'host cell' (a different cell) versus the organism's own membrane—general reasoning about whose membrane a self-encoded transporter occupies."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and B are clearly distinguishable: 'host cell plasma membrane' (GO:0020002) is a goslim_virus term for proteins on a host cell's membrane, inapplicable to the organism's own transporter. Options C and D are eliminated by the multi-pass TM topology and transporter function. No ambiguity remains among the four choices."
  },
  "important_caveats": [
    "The GO annotation for plasma membrane (GO:0005886) carries IEA:UniProtKB-SubCell evidence (inferred from UniProt's 'Cell membrane' annotation), but the underlying UniProt annotation itself is backed by experimental evidence (ECO:0000269, PubMed:20037157).",
    "The distinction between options A and B relies on understanding GO term semantics ('host cell' implies a different cell); this is general biological reasoning but also touches on GO ontology conventions.",
    "The protein was integrated into Swiss-Prot on 2025-02-05; the author's source snapshot date is unknown, though the sequence matches the current entry exactly."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> For the sequence-matched protein, UniProt records cell-membrane localization with experimental evidence attributed to PubMed 20037157; its GO plasma-membrane annotation is computationally assigned. These support B, while the GO annotation’s evidence type should not be mistaken for experimental evidence.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The many hydrophobic stretches indicate a multipass membrane protein, and the sequence is consistent with the equilibrative nucleoside-transporter family. Transferable knowledge that such transporters commonly mediate nucleoside uptake across the cell surface makes plasma membrane (B) a credible choice over microtubule (D) or vacuolar membrane (C). Nothing in the input suggests localization on a host cell’s membrane (A).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence provides a meaningful, though probabilistic, localization inference from membrane-protein topology and transporter-family patterns. It does not prove the localization experimentally or exclude every intracellular membrane possibility.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence and transporter-like features favor the cell surface among the offered choices; the host-cell qualifier distinguishes A from the protein’s own plasma membrane.


### Important caveats

- The experimental support is a database attribution to a cited publication, not an independent review of that study here.
- The GO plasma-membrane annotation is marked IEA:UniProtKB-SubCell, a computational annotation.
- The source entry matches the sequence, but the author’s exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The many hydrophobic stretches indicate a multipass membrane protein, and the sequence is consistent with the equilibrative nucleoside-transporter family. Transferable knowledge that such transporters commonly mediate nucleoside uptake across the cell surface makes plasma membrane (B) a credible choice over microtubule (D) or vacuolar membrane (C). Nothing in the input suggests localization on a host cell’s membrane (A).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence provides a meaningful, though probabilistic, localization inference from membrane-protein topology and transporter-family patterns. It does not prove the localization experimentally or exclude every intracellular membrane possibility."
  },
  "case_id": "GO_cellular_component_0150",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "For the sequence-matched protein, UniProt records cell-membrane localization with experimental evidence attributed to PubMed 20037157; its GO plasma-membrane annotation is computationally assigned. These support B, while the GO annotation’s evidence type should not be mistaken for experimental evidence."
  },
  "important_caveats": [
    "The experimental support is a database attribution to a cited publication, not an independent review of that study here.",
    "The GO plasma-membrane annotation is marked IEA:UniProtKB-SubCell, a computational annotation.",
    "The source entry matches the sequence, but the author’s exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence and transporter-like features favor the cell surface among the offered choices; the host-cell qualifier distinguishes A from the protein’s own plasma membrane."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0150",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "For the sequence-matched protein, UniProt records cell-membrane localization with experimental evidence attributed to PubMed 20037157; its GO plasma-membrane annotation is computationally assigned. These support B, while the GO annotation’s evidence type should not be mistaken for experimental evidence.",
    "evidence_ids": ["C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The many hydrophobic stretches indicate a multipass membrane protein, and the sequence is consistent with the equilibrative nucleoside-transporter family. Transferable knowledge that such transporters commonly mediate nucleoside uptake across the cell surface makes plasma membrane (B) a credible choice over microtubule (D) or vacuolar membrane (C). Nothing in the input suggests localization on a host cell’s membrane (A).",
    "missing_item_specific_fact": "",
    "reason": "The sequence provides a meaningful, though probabilistic, localization inference from membrane-protein topology and transporter-family patterns. It does not prove the localization experimentally or exclude every intracellular membrane possibility."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence and transporter-like features favor the cell surface among the offered choices; the host-cell qualifier distinguishes A from the protein’s own plasma membrane."
  },
  "important_caveats": [
    "The experimental support is a database attribution to a cited publication, not an independent review of that study here.",
    "The GO plasma-membrane annotation is marked IEA:UniProtKB-SubCell, a computational annotation.",
    "The source entry matches the sequence, but the author’s exact source snapshot is unknown."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry annotates this protein (Q9GTP4, Nucleoside transporter 2 from Crithidia fasciculata) as 'Cell membrane; Multi-pass membrane protein' with direct assay evidence (ECO:0000269, PubMed:20037157). The GO cross-reference maps this to GO:0005886 'plasma membrane' (IEA:UniProtKB-SubCell). The protein's function as an equilibrative nucleoside transporter, experimentally characterized to mediate nucleoside uptake across the cell boundary, is consistent with plasma membrane localization. The sequence contains ~11 hydrophobic transmembrane segments consistent with multi-pass membrane topology.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> 1) The sequence displays ~11 long hydrophobic stretches (~20+ residues) separated by hydrophilic loops, clearly indicating a multi-pass membrane protein, which eliminates microtubule (D). 2) 'Host cell plasma membrane' (GO:0020002) is a GO term specifically in the goslim_virus subset, defined as 'The plasma membrane surrounding a host cell'—it applies to viral or viral-associated proteins in the context of host infection. A protein from a free-living unicellular protozoan (Crithidia) is the cell itself, not a virus infecting a host, so this term is inapplicable, eliminating A. 3) Equilibrative nucleoside transporters (ENT family) are universally characterized as plasma membrane proteins across organisms (human ENT1-4, bacterial ENT homologs, Leishmania/Trypanosoma nucleoside transporters), serving as the primary route for nucleoside/nucleobase uptake from the extracellular environment. In a unicellular organism, the plasma membrane is the primary interface for nutrient acquisition, making vacuolar membrane (C) a much less likely primary location for a nutrient uptake transporter. 4) The overall topology pattern (11 TMs, N-terminal cytoplasmic tail, alternating loops) is consistent with the well-studied ENT/MFS-type transporter architecture at the plasma membrane.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can use: (a) sequence hydrophobicity analysis to confirm multi-pass membrane topology and exclude microtubule; (b) GO ontology knowledge that 'host cell plasma membrane' is a virus-specific term (goslim_virus subset) inapplicable to a free-living protozoan's own membrane; (c) family-level knowledge that equilibrative nucleoside transporters are plasma membrane proteins across diverse organisms; (d) the biological principle that nutrient uptake transporters in unicellular organisms localize to the plasma membrane rather than intracellular compartments. These transferable arguments meaningfully distinguish B from A, C, and D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option A (host cell plasma membrane) is clearly distinguished from B (plasma membrane) by the GO ontology: GO:0020002 is a virus-specific term (goslim_virus subset) referring to the host's membrane during infection, not the organism's own membrane. Option D (microtubule) is eliminated by the obvious multi-pass membrane topology. Option C (vacuolar membrane) is disfavored by the well-established family-level pattern of nucleoside transporters localizing to the plasma membrane for extracellular nutrient uptake. The expected answer B is uniquely defensible.


### Important caveats

- The GO annotation for this protein is IEA (Inferred from Electronic Annotation) via UniProtKB-SubCell, but the underlying UniProt annotation has direct assay evidence (ECO:0000269) from a mutagenesis/subcellular localization study.
- The sequence does not explicitly state the organism name in the user input; however, the multi-pass membrane topology and transporter-like architecture are recognizable from the sequence alone.
- The distinction between 'plasma membrane' and 'host cell plasma membrane' relies on GO ontology structure knowledge (goslim_virus subset membership), which is standard bioinformatics knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "1) The sequence displays ~11 long hydrophobic stretches (~20+ residues) separated by hydrophilic loops, clearly indicating a multi-pass membrane protein, which eliminates microtubule (D). 2) 'Host cell plasma membrane' (GO:0020002) is a GO term specifically in the goslim_virus subset, defined as 'The plasma membrane surrounding a host cell'—it applies to viral or viral-associated proteins in the context of host infection. A protein from a free-living unicellular protozoan (Crithidia) is the cell itself, not a virus infecting a host, so this term is inapplicable, eliminating A. 3) Equilibrative nucleoside transporters (ENT family) are universally characterized as plasma membrane proteins across organisms (human ENT1-4, bacterial ENT homologs, Leishmania/Trypanosoma nucleoside transporters), serving as the primary route for nucleoside/nucleobase uptake from the extracellular environment. In a unicellular organism, the plasma membrane is the primary interface for nutrient acquisition, making vacuolar membrane (C) a much less likely primary location for a nutrient uptake transporter. 4) The overall topology pattern (11 TMs, N-terminal cytoplasmic tail, alternating loops) is consistent with the well-studied ENT/MFS-type transporter architecture at the plasma membrane.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use: (a) sequence hydrophobicity analysis to confirm multi-pass membrane topology and exclude microtubule; (b) GO ontology knowledge that 'host cell plasma membrane' is a virus-specific term (goslim_virus subset) inapplicable to a free-living protozoan's own membrane; (c) family-level knowledge that equilibrative nucleoside transporters are plasma membrane proteins across diverse organisms; (d) the biological principle that nutrient uptake transporters in unicellular organisms localize to the plasma membrane rather than intracellular compartments. These transferable arguments meaningfully distinguish B from A, C, and D."
  },
  "case_id": "GO_cellular_component_0150",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry annotates this protein (Q9GTP4, Nucleoside transporter 2 from Crithidia fasciculata) as 'Cell membrane; Multi-pass membrane protein' with direct assay evidence (ECO:0000269, PubMed:20037157). The GO cross-reference maps this to GO:0005886 'plasma membrane' (IEA:UniProtKB-SubCell). The protein's function as an equilibrative nucleoside transporter, experimentally characterized to mediate nucleoside uptake across the cell boundary, is consistent with plasma membrane localization. The sequence contains ~11 hydrophobic transmembrane segments consistent with multi-pass membrane topology."
  },
  "important_caveats": [
    "The GO annotation for this protein is IEA (Inferred from Electronic Annotation) via UniProtKB-SubCell, but the underlying UniProt annotation has direct assay evidence (ECO:0000269) from a mutagenesis/subcellular localization study.",
    "The sequence does not explicitly state the organism name in the user input; however, the multi-pass membrane topology and transporter-like architecture are recognizable from the sequence alone.",
    "The distinction between 'plasma membrane' and 'host cell plasma membrane' relies on GO ontology structure knowledge (goslim_virus subset membership), which is standard bioinformatics knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option A (host cell plasma membrane) is clearly distinguished from B (plasma membrane) by the GO ontology: GO:0020002 is a virus-specific term (goslim_virus subset) referring to the host's membrane during infection, not the organism's own membrane. Option D (microtubule) is eliminated by the obvious multi-pass membrane topology. Option C (vacuolar membrane) is disfavored by the well-established family-level pattern of nucleoside transporters localizing to the plasma membrane for extracellular nutrient uptake. The expected answer B is uniquely defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0150",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry annotates this protein (Q9GTP4, Nucleoside transporter 2 from Crithidia fasciculata) as 'Cell membrane; Multi-pass membrane protein' with direct assay evidence (ECO:0000269, PubMed:20037157). The GO cross-reference maps this to GO:0005886 'plasma membrane' (IEA:UniProtKB-SubCell). The protein's function as an equilibrative nucleoside transporter, experimentally characterized to mediate nucleoside uptake across the cell boundary, is consistent with plasma membrane localization. The sequence contains ~11 hydrophobic transmembrane segments consistent with multi-pass membrane topology.",
    "evidence_ids": ["C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "1) The sequence displays ~11 long hydrophobic stretches (~20+ residues) separated by hydrophilic loops, clearly indicating a multi-pass membrane protein, which eliminates microtubule (D). 2) 'Host cell plasma membrane' (GO:0020002) is a GO term specifically in the goslim_virus subset, defined as 'The plasma membrane surrounding a host cell'—it applies to viral or viral-associated proteins in the context of host infection. A protein from a free-living unicellular protozoan (Crithidia) is the cell itself, not a virus infecting a host, so this term is inapplicable, eliminating A. 3) Equilibrative nucleoside transporters (ENT family) are universally characterized as plasma membrane proteins across organisms (human ENT1-4, bacterial ENT homologs, Leishmania/Trypanosoma nucleoside transporters), serving as the primary route for nucleoside/nucleobase uptake from the extracellular environment. In a unicellular organism, the plasma membrane is the primary interface for nutrient acquisition, making vacuolar membrane (C) a much less likely primary location for a nutrient uptake transporter. 4) The overall topology pattern (11 TMs, N-terminal cytoplasmic tail, alternating loops) is consistent with the well-studied ENT/MFS-type transporter architecture at the plasma membrane.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use: (a) sequence hydrophobicity analysis to confirm multi-pass membrane topology and exclude microtubule; (b) GO ontology knowledge that 'host cell plasma membrane' is a virus-specific term (goslim_virus subset) inapplicable to a free-living protozoan's own membrane; (c) family-level knowledge that equilibrative nucleoside transporters are plasma membrane proteins across diverse organisms; (d) the biological principle that nutrient uptake transporters in unicellular organisms localize to the plasma membrane rather than intracellular compartments. These transferable arguments meaningfully distinguish B from A, C, and D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option A (host cell plasma membrane) is clearly distinguished from B (plasma membrane) by the GO ontology: GO:0020002 is a virus-specific term (goslim_virus subset) referring to the host's membrane during infection, not the organism's own membrane. Option D (microtubule) is eliminated by the obvious multi-pass membrane topology. Option C (vacuolar membrane) is disfavored by the well-established family-level pattern of nucleoside transporters localizing to the plasma membrane for extracellular nutrient uptake. The expected answer B is uniquely defensible."
  },
  "important_caveats": [
    "The GO annotation for this protein is IEA (Inferred from Electronic Annotation) via UniProtKB-SubCell, but the underlying UniProt annotation has direct assay evidence (ECO:0000269) from a mutagenesis/subcellular localization study.",
    "The sequence does not explicitly state the organism name in the user input; however, the multi-pass membrane topology and transporter-like architecture are recognizable from the sequence alone.",
    "The distinction between 'plasma membrane' and 'host cell plasma membrane' relies on GO ontology structure knowledge (goslim_virus subset membership), which is standard bioinformatics knowledge."
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
  "requested_accession": "Q9GTP4",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "6e53d808d65dc861f251d0ee2f1b1ba4738fbf7c8abbca765447ebb335e58560",
  "benchmark_sequence_length": 502,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 55,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-01-28",
    "lastSequenceUpdateDate": "2001-03-01",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "current_source_sequence_sha256": "6e53d808d65dc861f251d0ee2f1b1ba4738fbf7c8abbca765447ebb335e58560",
  "current_source_sequence_length": 502,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 55,
  "selected_historical_version": {
    "accession": "Q9GTP4",
    "database": "Swiss-Prot",
    "entryVersion": 55,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "NT2_CRIFA",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8",
  "selected_historical_source_sequence_sha256": "6e53d808d65dc861f251d0ee2f1b1ba4738fbf7c8abbca765447ebb335e58560",
  "selected_historical_source_sequence_length": 502,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 55,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP4.json",
  "source_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "retrieved_utc": "2026-11-02T04:32:48.296419+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"Q9GTP4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP4.json",
  "source_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "retrieved_utc": "2026-11-02T04:32:48.296419+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":55,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-01-28\",\"lastSequenceUpdateDate\":\"2001-03-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP4.json",
  "source_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "retrieved_utc": "2026-11-02T04:32:48.296419+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAG22611.1\",\"source\":\"EMBL\"}],\"lineage\":[\"Eukaryota\",\"Discoba\",\"Euglenozoa\",\"Kinetoplastea\",\"Metakinetoplastina\",\"Trypanosomatida\",\"Trypanosomatidae\",\"Leishmaniinae\",\"Crithidia\"],\"scientificName\":\"Crithidia fasciculata\",\"taxonId\":5656}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP4.json",
  "source_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "retrieved_utc": "2026-11-02T04:32:48.296419+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20037157\",\"source\":\"PubMed\"}],\"value\":\"Equilibrative nucleoside transporter 2\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"15694482\",\"source\":\"PubMed\"}],\"value\":\"Nucleoside transporter 2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"15694482\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20037157\",\"source\":\"PubMed\"}],\"value\":\"CfNT2\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP4.json",
  "source_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "retrieved_utc": "2026-11-02T04:32:48.296419+00:00",
  "json_pointer": "/comments/4",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20037157\",\"source\":\"PubMed\"}],\"id\":\"SL-0039\",\"value\":\"Cell membrane\"},\"topology\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"id\":\"SL-9909\",\"value\":\"Multi-pass membrane protein\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP4.json",
  "source_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "retrieved_utc": "2026-11-02T04:32:48.296419+00:00",
  "json_pointer": "/uniProtKBCrossReferences/5",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005886\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:plasma membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-SubCell\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP4.json",
  "source_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "retrieved_utc": "2026-11-02T04:32:48.296419+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Liu W.\",\"Arendt C.S.\",\"Gessford S.K.\",\"Ntaba D.\",\"Carter N.S.\",\"Ullman B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"15694482\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.molbiopara.2004.11.018\"}],\"citationType\":\"journal article\",\"firstPage\":\"1\",\"id\":\"15694482\",\"journal\":\"Mol. Biochem. Parasitol.\",\"lastPage\":\"12\",\"publicationDate\":\"2005\",\"title\":\"Identification and characterization of purine nucleoside transporters from Crithidia fasciculata.\",\"volume\":\"140\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"TRANSPORTER ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"INDUCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q9GTP4.json",
  "source_sha256": "3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73",
  "retrieved_utc": "2026-11-02T04:32:48.296419+00:00",
  "json_pointer": "/references/2",
  "excerpt": "{\"citation\":{\"authors\":[\"Arendt C.S.\",\"Ullman B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"20037157\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m109.074351\"}],\"citationType\":\"journal article\",\"firstPage\":\"6024\",\"id\":\"20037157\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"6035\",\"publicationDate\":\"2010\",\"title\":\"Role of transmembrane domain 4 in ligand permeation by Crithidia fasciculata equilibrative nucleoside transporter 2 (CfNT2).\",\"volume\":\"285\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"TRANSPORTER ACTIVITY\",\"SUBCELLULAR LOCATION\",\"MUTAGENESIS OF VAL-89; HIS-138; GLY-139; ALA-140; ILE-141; ALA-142; VAL-143; ILE-144; MET-145; VAL-146; VAL-147; ALA-148; VAL-150; GLY-151; GLY-152; PHE-153; SER-154; LYS-155; ALA-156; LEU-157; ASP-159; SER-160; THR-162; ASN-163; ALA-164; LEU-165; VAL-166; GLY-167; PRO-168; PHE-169; PRO-170; THR-171 AND LYS-172\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55",
  "source_sha256": "130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8",
  "retrieved_utc": "2026-11-02T04:32:52.675125+00:00",
  "source_locator": "lines 1-12",
  "excerpt": "ID   NT2_CRIFA               Reviewed;         502 AA.\nAC   Q9GTP4;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAR-2001, sequence version 1.\nDT   28-JAN-2026, entry version 55.\nDE   RecName: Full=Nucleoside transporter 2 {ECO:0000303|PubMed:15694482};\nDE            Short=CfNT2 {ECO:0000303|PubMed:15694482, ECO:0000303|PubMed:20037157};\nDE   AltName: Full=Equilibrative nucleoside transporter 2 {ECO:0000303|PubMed:20037157};\nOS   Crithidia fasciculata.\nOC   Eukaryota; Discoba; Euglenozoa; Kinetoplastea; Metakinetoplastina;\nOC   Trypanosomatida; Trypanosomatidae; Leishmaniinae; Crithidia.\nOX   NCBI_TaxID=5656 {ECO:0000312|EMBL:AAG22611.1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55",
  "source_sha256": "130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8",
  "retrieved_utc": "2026-11-02T04:32:52.675125+00:00",
  "source_locator": "lines 19-26",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, TRANSPORTER ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND\nRP   INDUCTION.\nRX   PubMed=15694482; DOI=10.1016/j.molbiopara.2004.11.018;\nRA   Liu W., Arendt C.S., Gessford S.K., Ntaba D., Carter N.S., Ullman B.;\nRT   \"Identification and characterization of purine nucleoside transporters from\nRT   Crithidia fasciculata.\";\nRL   Mol. Biochem. Parasitol. 140:1-12(2005).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55",
  "source_sha256": "130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8",
  "retrieved_utc": "2026-11-02T04:32:52.675125+00:00",
  "source_locator": "lines 27-38",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, TRANSPORTER ACTIVITY, SUBCELLULAR LOCATION, AND MUTAGENESIS OF\nRP   VAL-89; HIS-138; GLY-139; ALA-140; ILE-141; ALA-142; VAL-143; ILE-144;\nRP   MET-145; VAL-146; VAL-147; ALA-148; VAL-150; GLY-151; GLY-152; PHE-153;\nRP   SER-154; LYS-155; ALA-156; LEU-157; ASP-159; SER-160; THR-162; ASN-163;\nRP   ALA-164; LEU-165; VAL-166; GLY-167; PRO-168; PHE-169; PRO-170; THR-171 AND\nRP   LYS-172.\nRX   PubMed=20037157; DOI=10.1074/jbc.m109.074351;\nRA   Arendt C.S., Ullman B.;\nRT   \"Role of transmembrane domain 4 in ligand permeation by Crithidia\nRT   fasciculata equilibrative nucleoside transporter 2 (CfNT2).\";\nRL   J. Biol. Chem. 285:6024-6035(2010).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55",
  "source_sha256": "130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8",
  "retrieved_utc": "2026-11-02T04:32:52.675125+00:00",
  "source_locator": "lines 52-53",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000269|PubMed:20037157};\nCC       Multi-pass membrane protein {ECO:0000255}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q9GTP4?format=txt&versions=55",
  "source_sha256": "130ca0749d2c91bc4f41009fc3423401ec6f66d72dd1c0a97de44d68f33480c8",
  "retrieved_utc": "2026-11-02T04:32:52.675125+00:00",
  "source_locator": "lines 70-70",
  "excerpt": "DR   GO; GO:0005886; C:plasma membrane; IEA:UniProtKB-SubCell.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 55,
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
  "source_locator": "lines 59354-59361",
  "excerpt": "[Term]\nid: GO:0005774\nname: vacuolar membrane\nnamespace: cellular_component\ndef: \"The lipid bilayer surrounding the vacuole and separating its contents from the cytoplasm of the cell.\" [GOC:ai]\nis_a: GO:0098588 ! bounding membrane of organelle\nrelationship: part_of GO:0005773 ! vacuole\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0005774"
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
  "source_locator": "lines 60320-60333",
  "excerpt": "[Term]\nid: GO:0005874\nname: microtubule\nnamespace: cellular_component\ndef: \"Any of the long, generally straight, hollow tubes of internal diameter 12-15 nm and external diameter 24 nm found in a wide variety of eukaryotic cells; each consists (usually) of 13 protofilaments of polymeric tubulin, staggered in such a manner that the tubulin monomers are arranged in a helical pattern on the microtubular surface, and with the alpha/beta axes of the tubulin subunits parallel to the long axis of the tubule; exist in equilibrium with pool of tubulin monomers and can be rapidly assembled or disassembled in response to physiological stimuli; concerned with force generation, e.g. in the spindle.\" [ISBN:0879693568]\nsubset: goslim_metagenomics\nsynonym: \"microtubuli\" EXACT []\nsynonym: \"microtubulus\" EXACT []\nsynonym: \"neurotubule\" NARROW [NIF_Subcellular:sao248349196]\nxref: NIF_Subcellular:sao1846835077\nxref: Wikipedia:Microtubule\nis_a: GO:0099513 ! polymeric cytoskeletal fiber\nrelationship: part_of GO:0015630 ! microtubule cytoskeleton\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0005874"
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
  "source_locator": "lines 155120-155127",
  "excerpt": "[Term]\nid: GO:0020002\nname: host cell plasma membrane\nnamespace: cellular_component\ndef: \"The plasma membrane surrounding a host cell.\" [GOC:mb]\nsubset: goslim_virus\nis_a: GO:0033644 ! host cell membrane\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0020002"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 150. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
